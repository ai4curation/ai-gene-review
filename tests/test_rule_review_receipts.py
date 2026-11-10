"""Receipt checks for rule reviews: one case per error the 2026-11 audit found."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from ai_gene_review.validation.rule_review_receipts import (
    check_review,
    experimental_annotations,
    labels_agree,
)
from ai_gene_review.validation.validation_report import ValidationReport

LABELS = {
    "interpro": {
        "IPR000999": "Ribonuclease III domain",
        "IPR000571": "Zinc finger, CCCH-type",
    },
    "go": {"GO:0010605": "negative regulation of macromolecule metabolic process"},
    "funfam": {},
}

DICER_SET = {
    "number": 1,
    "conditions": [
        {"condition_type": "INTERPRO", "value": "IPR000999", "label": "Ribonuclease III domain"}
    ],
}


def review(**overrides: Any) -> dict[str, Any]:
    """A minimal review that passes every offline check."""
    base: dict[str, Any] = {
        "id": "ARBA00000001",
        "rule_type": "ARBA",
        "action": "UNDECIDED",
        "rule": {
            "rule_id": "ARBA00000001",
            "condition_sets": [DICER_SET],
            "retrieved_date": "2026-11-10",
            "source_condition_set_count": 1,
            "go_annotations": [
                {"go_id": "GO:0010605", "go_label": "negative regulation of macromolecule metabolic process"}
            ],
        },
    }
    base.update(overrides)
    return base


def checks(data: dict[str, Any], tmp_path: Path, severity: str = "error") -> set[str]:
    report = ValidationReport(is_valid=True)
    check_review(data, report, project_root=tmp_path, labels=LABELS)
    return {str(issue.check_type) for issue in report.issues if issue.severity == severity}


def test_clean_review_has_no_issues(tmp_path: Path) -> None:
    assert checks(review(), tmp_path) == set()
    assert checks(review(), tmp_path, "warning") == set()


@pytest.mark.parametrize(
    "overrides,expected",
    [
        pytest.param(
            {"action": "MODIFY", "suggested_modifications": ["x"], "rule": {"rule_id": "A", "condition_sets": []}},
            "verdict_without_conditions",
            id="verdict on unread rule",
        ),
        pytest.param(
            {"action": "ACCEPT", "rule": {"rule_id": "A", "condition_sets": [DICER_SET], "source_condition_set_count": 343}},
            "accept_on_partial_examination",
            id="accept after sampling",
        ),
        pytest.param(
            {"rule": {"rule_id": "A", "condition_sets": [{"conditions": [
                {"condition_type": "INTERPRO", "value": "IPR000999", "label": "Ribonucleoside-diphosphate reductase"}]}]}},
            "condition_label_mismatch",
            id="wrong InterPro label",
        ),
        pytest.param(
            {"review_summary": "IPR000571 (protein kinase catalytic region) is unrelated to the term."},
            "prose_identifier_label_mismatch",
            id="wrong name in prose",
        ),
        pytest.param(
            {"action": "MODIFY", "confidence": 0.8, "suggested_modifications": ["x"],
             "action_rationale": "343 condition sets exceed the recommended maximum of 12."},
            "size_as_evidence",
            id="size as evidence",
        ),
        pytest.param(
            {"literature_support": {"assessment": "CONTRADICTED", "supported_by": [
                {"reference_id": "file:rules/arba/A/A-deep-research-manual.md", "supporting_text": "x"}]}},
            "literature_verdict_without_literature",
            id="own notes as literature",
        ),
        pytest.param(
            {"supported_by": [{"reference_id": "analysis:complexity", "supporting_text": "x"}]},
            "unresolvable_reference",
            id="pseudo-reference",
        ),
        pytest.param(
            {"supported_by": [{"reference_id": "file:rules/arba/A/A.enriched.json", "supporting_text": "x"}]},
            "missing_cited_file",
            id="cited file missing",
        ),
        pytest.param(
            {"action": "DEPRECATE", "confidence": 0.95},
            "deprecate_without_counterexample",
            id="deprecate without a wrongly annotated protein",
        ),
        pytest.param(
            {"action": "DEPRECATE", "confidence": 0.05, "annotation_assessments": [
                {"annotation_kind": "GO_TERM", "value": "GO:0010605", "assessment": "INCORRECT",
                 "incorrect_examples": ["Q08649"]}]},
            "low_confidence_verdict",
            id="verdict at confidence 0.05",
        ),
        pytest.param({"action": "MODIFY"}, "modify_without_modification", id="modify with no change named"),
        pytest.param(
            {"action": "MODIFY", "suggested_modifications": ["x"]},
            "verdict_without_confidence",
            id="verdict with confidence left out",
        ),
        pytest.param(
            {"action": "ACCEPT", "confidence": 0.9,
             "rule": {"rule_id": "A", "condition_sets": [DICER_SET], "retrieved_date": "2026-11-10"}},
            "missing_rule_snapshot",
            id="accept with set count left out",
        ),
        pytest.param(
            {"action": "ACCEPT", "confidence": 0.9,
             "rule": {"rule_id": "A", "condition_sets": [DICER_SET], "source_condition_set_count": 1}},
            "missing_rule_snapshot",
            id="accept with retrieval date left out",
        ),
        pytest.param(
            {"action": "DEPRECATE", "confidence": 0.9, "annotation_assessments": [
                {"annotation_kind": "GO_TERM", "value": "GO:0010605", "assessment": "INCORRECT",
                 "notes": "The consequent is not obsolete."}]},
            "deprecate_without_counterexample",
            id="the word obsolete in a note is not a receipt",
        ),
        pytest.param(
            {"literature_support": {"assessment": "STRONG", "notes": "Well studied."},
             "references": [{"id": "PMID:1", "title": "Unrelated"}]},
            "literature_verdict_without_literature",
            id="a PMID elsewhere in the file does not support the literature block",
        ),
        pytest.param(
            {"annotation_assessments": [{"annotation_kind": "GO_TERM", "value": "GO:0010605",
                                         "assessment": "CORRECT", "correct_examples": ["ESA1"]}]},
            "example_not_an_accession",
            id="gene symbol as example",
        ),
    ],
)
def test_audit_error_is_caught(overrides: dict[str, Any], expected: str, tmp_path: Path) -> None:
    assert expected in checks(review(**overrides), tmp_path)


def test_deprecate_with_counterexample_passes(tmp_path: Path) -> None:
    data = review(
        action="DEPRECATE",
        confidence=0.9,
        annotation_assessments=[
            {"annotation_kind": "GO_TERM", "value": "GO:0010605", "assessment": "INCORRECT",
             "incorrect_examples": ["P12345"]}
        ],
    )
    assert checks(data, tmp_path) == set()


def test_withdrawn_rule_can_be_deprecated_without_sets(tmp_path: Path) -> None:
    data = review(action="DEPRECATE", confidence=0.9, rule={"rule_id": "A", "condition_sets": [], "withdrawn": True,
                                            "retrieved_date": "2026-11-10"})
    assert checks(data, tmp_path) == set()


def test_naming_the_analysis_cap_is_allowed_when_undecided(tmp_path: Path) -> None:
    data = review(review_summary="12 of 343 sets were read, the analysis limit of 12 being the tool default.")
    assert checks(data, tmp_path) == set()


def test_obsolete_consequent_justifies_deprecate(tmp_path: Path) -> None:
    data = review(
        action="DEPRECATE",
        confidence=0.9,
        annotation_assessments=[
            {"annotation_kind": "GO_TERM", "value": "GO:0010605", "assessment": "UNDECIDED", "consequent_obsolete": True}
        ],
    )
    assert checks(data, tmp_path) == set()


def test_withdrawn_claims_are_not_rechecked(tmp_path: Path) -> None:
    data = review(corrections=[{
        "withdrawn_claim": "IPR000999 (ribonucleoside-diphosphate reductase) exceeds the threshold of 12",
        "correction": "IPR000999 (Ribonuclease III domain)",
    }])
    assert checks(data, tmp_path) == set()


@pytest.mark.parametrize(
    "stated,official,agree",
    [
        ("glycosyl transferases", "Chromo/chromo shadow domain", False),
        ("chromo domain", "Chromo/chromo shadow domain", True),
        ("cellular response to heat", "monoatomic cation homeostasis", False),
        ("Sortilin C-terminal", "Sortilin, C-terminal", True),
    ],
)
def test_labels_agree(stated: str, official: str, agree: bool) -> None:
    assert labels_agree(stated, official) is agree


@pytest.mark.integration
def test_alleged_false_positive_with_experimental_annotation() -> None:
    """ESA1 was called a false positive for GO:0010629; SGD annotates a descendant by IMP."""
    rows = experimental_annotations("Q08649", "GO:0010629")
    assert any("GO:0000183" in row for row in rows)
