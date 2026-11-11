"""Protect the required integration check and cancellation boundaries."""

import os
import fnmatch
import shlex
from pathlib import Path
import subprocess

import pytest

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_queue_runs_required_check_without_cancelling_other_groups():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    assert "merge_group" in workflow.get("on", workflow.get(True))
    assert workflow["jobs"]["test"]["strategy"]["matrix"]["python-version"] == ["3.12"]
    concurrency = workflow["concurrency"]
    assert concurrency["cancel-in-progress"] == (
        "${{ github.event_name == 'pull_request' || github.event_name == 'push' }}"
    )
    assert "(github.event_name == 'push' && github.ref)" in concurrency["group"]
    assert "github.run_id" in concurrency["group"]
    steps = workflow["jobs"]["validation"]["steps"] + workflow["jobs"]["suite"]["steps"]
    assert next(s for s in steps if s.get("id") == "changes")["uses"] == "dorny/paths-filter@v4"
    for name in ("Run test suite", "Test valid/invalid examples", "Check agentic automation",
                 "Validate modules (scoped)", "Validate family reviews (scoped)",
                 "Validate history records (scoped)",
                 "Fetch benchmark baseline and review snapshot commits",
                 "Validate all gene schemas (merge queue)"):
        step = next(s for s in steps if s.get("name") == name)
        assert "github.event_name == 'merge_group'" in step["if"]
    paint = next(s for s in steps if s.get("name", "").startswith("Verify PAINT slices"))
    assert "merge_group" not in paint["if"]


def test_queue_template_bounds_builds_and_introduces_no_bypass_actors():
    config = yaml.safe_load((ROOT / ".github/merge-queue-ruleset.yaml").read_text())
    assert config["bypass_actors"] == []
    assert config["conditions"]["ref_name"]["include"] == ["refs/heads/main"]
    rule, = config["rules"]
    assert rule["type"] == "merge_queue"
    assert rule["parameters"]["max_entries_to_build"] == 8
    assert rule["parameters"]["max_entries_to_merge"] == 1
    assert rule["parameters"]["grouping_strategy"] == "ALLGREEN"
    assert rule["parameters"]["check_response_timeout_minutes"] == 360


def test_workers_are_independent_and_share_path_filters():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    for name in ("validation", "suite"):
        job = workflow["jobs"][name]
        assert "needs" not in job and "if" not in job
        assert not job.get("continue-on-error")
        changes = next(s for s in job["steps"] if s.get("id") == "changes")
        assert changes["with"]["list-files"] == "shell"
        assert changes["with"]["filters"] == ".github/ci-path-filters.yaml"
    filters = yaml.safe_load((ROOT / ".github/ci-path-filters.yaml").read_text())
    # Editing CI itself must exercise the complete suite before reaching the queue.
    assert ".github/workflows/main.yaml" in filters["src"]
    assert ".github/ci-path-filters.yaml" in filters["src"]


@pytest.mark.parametrize("validation", ["success", "failure", "cancelled", "skipped"])
@pytest.mark.parametrize("suite", ["success", "failure", "cancelled", "skipped"])
def test_required_gate_rejects_failed_cancelled_or_skipped_workers(validation, suite):
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    gate = workflow["jobs"]["test"]
    assert set(gate["needs"]) == {"validation", "suite"}
    assert gate["if"] == "${{ always() }}"
    assert not gate.get("continue-on-error")
    step, = gate["steps"]
    assert "if" not in step and not step.get("continue-on-error")
    assert step["env"] == {
        "VALIDATION_RESULT": "${{ needs.validation.result }}",
        "SUITE_RESULT": "${{ needs.suite.result }}",
    }
    result = subprocess.run(
        ["bash", "-e", "-o", "pipefail", "-c", step["run"]],
        env={**os.environ, "VALIDATION_RESULT": validation, "SUITE_RESULT": suite},
        capture_output=True, text=True,
    )
    assert (result.returncode == 0) == (validation == suite == "success")



def _run_changed_gene_recipe(tmp_path, paths, fail_validation=False):
    """Execute the real recipe; replace only its external validation commands."""
    recipe = (ROOT / "project.justfile").read_text().split("validate-changed *files:\n", 1)[1]
    recipe = recipe.split("\n# conf/local_quote_baseline.yaml", 1)[0]
    script = "\n".join(line[4:] if line.startswith("    ") else line
                       for line in recipe.splitlines())
    script = script.replace("{{files}}", " ".join(shlex.quote(path) for path in paths))
    calls = tmp_path / "calls"
    stub = tmp_path / "bin"
    stub.mkdir(exist_ok=True)
    uv = stub / "uv"
    uv.write_text(
        '#!/bin/sh\nprintf "%s\\0" "$@" >> "$CALL_LOG"\nprintf "\\n" >> "$CALL_LOG"\n'
        'if [ "$2" = "ai-gene-review" ] && [ "$FAIL_VALIDATION" = "1" ]; then exit 1; fi\n'
    )
    uv.chmod(0o755)
    result = subprocess.run(
        ["bash", "-c", script], cwd=tmp_path,
        env={**os.environ, "PATH": str(stub) + os.pathsep + os.environ["PATH"],
             "CALL_LOG": str(calls), "FAIL_VALIDATION": "1" if fail_validation else "0"},
        capture_output=True, text=True,
    )
    recorded = ([line.decode().rstrip("\0").split("\0")
                 for line in calls.read_bytes().splitlines()] if calls.exists() else [])
    return result, recorded


@pytest.mark.parametrize("source,state", [
    ("FN1-goa.tsv", "added"),
    ("FN1-goa-20261031.tsv", "modified"),
    ("arbitrary-snapshot.tsv", "modified"),
    ("arbitrary-snapshot.tsv", "deleted"),
    ("FN1-goa.tsv", "deleted"),
    ("FN1-goa-snapshots.yaml", "deleted"),
    ("FN1-goa-snapshots.yaml", "malformed"),
])
def test_source_only_changes_validate_the_affected_review(tmp_path, source, state):
    directory = tmp_path / "genes/human/FN1"
    directory.mkdir(parents=True)
    review = "genes/human/FN1/FN1-ai-review.yaml"
    (tmp_path / review).write_text("id: P02751\n")
    unrelated = tmp_path / "genes/human/OTHER/OTHER-ai-review.yaml"
    unrelated.parent.mkdir()
    unrelated.write_text("id: OTHER\n")
    changed = f"genes/human/FN1/{source}"
    if state != "deleted":
        (tmp_path / changed).write_text("snapshots: [broken" if state == "malformed" else state)
    filters = yaml.safe_load((ROOT / ".github/ci-path-filters.yaml").read_text())
    # These positive, simple glob cases exercise the configured selection scope;
    # the actual CI service still applies its own picomatch implementation.
    assert any(fnmatch.fnmatchcase(changed, pattern) for pattern in filters["genes"])
    assert not any(fnmatch.fnmatchcase(changed, pattern) for pattern in filters["infra"])
    result, calls = _run_changed_gene_recipe(tmp_path, [changed])
    assert result.returncode == 0, result.stdout + result.stderr
    assert calls == [
        ["run", "ai-gene-review", "validate", "--verbose", "--terms", review],
        ["run", "python", "src/ai_gene_review/tools/validate_pmid_references.py", "genes/human/FN1"],
    ]


def test_changed_sources_and_reviews_are_deduplicated(tmp_path):
    directory = tmp_path / "genes/human/FN1"
    directory.mkdir(parents=True)
    reviews = ["genes/human/FN1/FN1-ai-review.yaml", "genes/human/FN1/SECOND-ai-review.yaml"]
    for review in reviews:
        (tmp_path / review).write_text("id: P02751\n")
    result, calls = _run_changed_gene_recipe(tmp_path, [
        reviews[0], "genes/human/FN1/FN1-goa.tsv", "genes/human/FN1/FN1-goa-snapshots.yaml",
    ])
    assert result.returncode == 0, result.stdout + result.stderr
    assert calls[0] == ["run", "ai-gene-review", "validate", "--verbose", "--terms", *reviews]
    assert len(calls) == 2  # The PMID check also runs once for the shared directory.


def test_changed_source_validation_failure_is_not_hidden(tmp_path):
    directory = tmp_path / "genes/human/FN1"
    directory.mkdir(parents=True)
    (directory / "FN1-ai-review.yaml").write_text("id: P02751\n")
    (directory / "FN1-goa-snapshots.yaml").write_text("snapshots: [broken")
    result, calls = _run_changed_gene_recipe(
        tmp_path, ["genes/human/FN1/FN1-goa-snapshots.yaml"], fail_validation=True,
    )
    assert result.returncode == 1
    assert len(calls) == 2


def test_unrelated_paths_and_deleted_reviews_do_not_select_other_genes(tmp_path):
    directory = tmp_path / "genes/human/FN1"
    directory.mkdir(parents=True)
    (directory / "FN1-ai-review.yaml").write_text("id: P02751\n")
    result, calls = _run_changed_gene_recipe(tmp_path, [
        "docs/source.tsv", "genes/human/DELETED/DELETED-ai-review.yaml",
    ])
    assert result.returncode == 0
    assert calls == []
