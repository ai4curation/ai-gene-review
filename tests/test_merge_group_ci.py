"""Protect the required integration check and cancellation boundaries."""

import os
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


def test_queue_rollout_is_bounded_and_does_not_bypass_protection():
    config = yaml.safe_load((ROOT / ".github/merge-queue-ruleset.yaml").read_text())
    assert config["bypass_actors"] == []
    assert config["conditions"]["ref_name"]["include"] == ["refs/heads/main"]
    rule, = config["rules"]
    assert rule["type"] == "merge_queue"
    assert rule["parameters"]["max_entries_to_build"] == 1
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
