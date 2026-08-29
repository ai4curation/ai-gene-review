"""Tests for scripts/backfill_history_from_prs.py (pure parts, no gh calls)."""

import importlib.util
import sys
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

ROOT_DIR = Path(__file__).parent.parent
SCRIPT = ROOT_DIR / "scripts" / "backfill_history_from_prs.py"
HISTORY_SCHEMA_PATH = ROOT_DIR / "src" / "ai_gene_review" / "schema" / "history.yaml"


@pytest.fixture(scope="module")
def backfill():
    spec = importlib.util.spec_from_file_location("backfill_history_from_prs", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        HISTORY_SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_classify_gene_files_share_one_target(backfill):
    files = [
        {"filename": "genes/human/CFAP300/CFAP300-ai-review.yaml", "status": "modified"},
        {"filename": "genes/human/CFAP300/CFAP300-notes.md", "status": "added"},
        {"filename": "publications/PMID_123.md", "status": "added"},
    ]
    targets = backfill.collect_targets(files)
    assert len(targets) == 1
    t = targets[0]
    assert (t.kind, t.organism, t.slug) == ("gene", "human", "CFAP300")
    assert t.path == "genes/human/CFAP300/CFAP300-ai-review.yaml"
    assert set(t.files) == {
        "genes/human/CFAP300/CFAP300-ai-review.yaml",
        "genes/human/CFAP300/CFAP300-notes.md",
    }
    assert t.history_dir == Path("history/genes/human/CFAP300")


def test_classify_other_kinds(backfill):
    assert backfill.classify_file("modules/foo_pathway.yaml").kind == "module"
    assert backfill.classify_file("gocams/568b0f9600000284/568b0f9600000284-src.yaml").kind == "gocam"
    assert backfill.classify_file("projects/FOO.md").kind == "project"
    assert backfill.classify_file("src/ai_gene_review/schema/gene_review.yaml").kind == "schema"
    assert backfill.classify_file("cache/uniprot/x.txt") is None
    assert backfill.classify_file("reports/validation-all.tsv") is None


def test_gocam_src_only_target_is_reported_missing(backfill):
    """A gocam dir with only a cached -src.yaml has no valid record target.

    ``classify_file`` derives ``<MODEL>-review.yaml`` by convention, but the
    review file is optional and almost no model has one. Writing a record for
    such a target fails ``test_committed_history_records_follow_layout``, so
    the backfiller must recognise it as missing.
    """
    src_only = sorted(
        p
        for p in ROOT_DIR.glob("gocams/*/*-src.yaml")
        if not p.with_name(f"{p.parent.name}-review.yaml").exists()
    )
    assert src_only, "expected at least one gocam model without a -review.yaml"

    model_dir = src_only[0].parent
    target = backfill.classify_file(
        f"gocams/{model_dir.name}/{src_only[0].name}"
    )
    assert target.kind == "gocam"
    assert target.path == f"gocams/{model_dir.name}/{model_dir.name}-review.yaml"
    assert not backfill.target_path_exists(target)


def test_target_path_exists_for_a_real_gene_review(backfill):
    target = backfill.classify_file("genes/human/CFAP300/CFAP300-notes.md")
    assert target.path == "genes/human/CFAP300/CFAP300-ai-review.yaml"
    assert backfill.target_path_exists(target)


def test_target_path_exists_is_false_for_a_bogus_slug(backfill):
    target = backfill.classify_file("genes/human/NOT_A_REAL_GENE_XYZ/notes.md")
    assert target is not None
    assert not backfill.target_path_exists(target)


def _fake_pr(**overrides):
    pr = {
        "number": 2500,
        "title": "Review CFAP300",
        "body": "De-novo review.",
        "author": {"login": "cmungall"},
        "createdAt": "2026-08-01T10:00:00Z",
        "mergedAt": None,
        "state": "OPEN",
        "headRefName": "claude/review-cfap300-abc",
        "url": "https://github.com/ai4curation/ai-gene-review/pull/2500",
    }
    pr.update(overrides)
    return pr


def test_build_record_validates_and_is_deterministic(backfill, validator):
    files = [
        {"filename": "genes/human/CFAP300/CFAP300-ai-review.yaml", "status": "added"},
    ]
    (target,) = backfill.collect_targets(files)
    pr = _fake_pr()

    record, out_path = backfill.build_record(pr, target)
    record2, out_path2 = backfill.build_record(pr, target)
    assert out_path == out_path2, "shortid must be deterministic for idempotency"

    assert record["target"] == {
        "kind": "gene",
        "slug": "CFAP300",
        "organism": "human",
        "path": "genes/human/CFAP300/CFAP300-ai-review.yaml",
    }
    # Session timestamp comes from the PR, not from "now".
    assert record["session"]["timestamp"] == "2026-08-01T10:00:00Z"
    assert out_path.name.startswith("2026-08-01T100000Z-")
    # Branch prefix claude/ adds the agent actor ahead of the account.
    assert [a["name"] for a in record["session"]["actors"]] == ["claude-code", "cmungall"]
    assert record["events"][0]["type"] == "CREATE"
    assert "Backfilled from PR #2500" in record["events"][0]["details"]

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, [e.message for e in errors]


def test_build_record_edit_and_merged_timestamp(backfill):
    files = [{"filename": "modules/foo_pathway.yaml", "status": "modified"}]
    (target,) = backfill.collect_targets(files)
    pr = _fake_pr(
        state="MERGED",
        mergedAt="2026-08-02T12:30:45Z",
        headRefName="fix-typo",
        author={"login": "github-actions[bot]"},
    )

    record, out_path = backfill.build_record(pr, target)
    assert record["session"]["timestamp"] == "2026-08-02T12:30:45Z"
    assert record["events"][0]["type"] == "EDIT"
    # No agent branch prefix -> single actor; [bot] suffix -> automation.
    assert record["session"]["actors"] == [
        {"type": "automation", "name": "github-actions[bot]"}
    ]


def test_build_record_general_for_ancillary_only_changes(backfill):
    files = [{"filename": "genes/human/CFAP300/CFAP300-notes.md", "status": "added"}]
    (target,) = backfill.collect_targets(files)
    record, _ = backfill.build_record(_fake_pr(), target)
    assert record["events"][0]["type"] == "GENERAL"
