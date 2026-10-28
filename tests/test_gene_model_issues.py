"""Gene model issues carry evidence, and CONFIRMED needs independent lines of it."""

from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest

from ai_gene_review.validation.gene_model_issues import validate_gene_model_issues
from ai_gene_review.validation.validation_report import ValidationReport

ISSUE: dict[str, Any] = {
    "issue_type": "FUSED_GENE_MODEL",
    "status": "CONFIRMED",
    "description": "Two neighbouring genes joined into one model.",
    "components": [
        {"accession": "A0A2T0ACV7", "segment": "1-650"},
        {"accession": "A0A2T0ACW0", "segment": "645-1419"},
    ],
    "reviewed_segment": "645-1419",
    "evidence_types": ["TILING", "GENETIC_SEPARATION"],
    "supported_by": [
        {"reference_id": "file:X/X/RESULTS.md", "supporting_text": "tiled by two genes"}
    ],
}


def check(issue: dict[str, Any]) -> list[str | None]:
    report = ValidationReport(file_path=Path("t.yaml"), is_valid=True)
    validate_gene_model_issues({"gene_model_issues": [issue]}, report)
    return [i.check_type for i in report.issues]


def test_well_formed_issue_passes() -> None:
    assert check(ISSUE) == []


def test_issue_without_supporting_quotes_warns() -> None:
    issue = deepcopy(ISSUE)
    del issue["supported_by"]
    assert check(issue) == ["gene_model_issue_unsupported"]


def test_confirmed_needs_two_kinds_of_evidence() -> None:
    issue = deepcopy(ISSUE)
    issue["evidence_types"] = ["TILING"]
    assert check(issue) == ["gene_model_issue_confirmed_single_evidence"]


def test_suspected_with_one_kind_of_evidence_passes() -> None:
    issue = deepcopy(ISSUE)
    issue["status"] = "SUSPECTED"
    issue["evidence_types"] = ["ORTHOLOG_COMPARISON"]
    assert check(issue) == []


@pytest.mark.parametrize(
    "path,value",
    [("reviewed_segment", "900-645"), ("components", [{"segment": "650-1"}])],
)
def test_reversed_segment_warns(path: str, value: object) -> None:
    issue = deepcopy(ISSUE)
    issue[path] = value
    assert check(issue) == ["gene_model_issue_segment_order"]


def test_reviews_without_issues_are_ignored() -> None:
    report = ValidationReport(file_path=Path("t.yaml"), is_valid=True)
    validate_gene_model_issues({"gene_symbol": "X"}, report)
    assert report.issues == []
