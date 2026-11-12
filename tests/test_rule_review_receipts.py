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


UNIT = {
    "name": "Dicer-like RNase III",
    "unit_kind": "FAMILY",
    "condition_sets": [1],
    "example_proteins": ["Q9UPY3"],
    "most_informative_term_id": "GO:0010605",
    "most_informative_term_label": "negative regulation of macromolecule metabolic process",
    "term_relation": "SAME_AS_CONSEQUENT",
    "evidence": ["Q9UPY3 GO:0010605 IDA PMID:1"],
}
MEANING: dict[str, Any] = {
    "biological_meaning": {"assessment": "COHERENT", "notes": "One family, one term."},
    "biological_units": [UNIT],
    "parsimony": {"assessment": "PARSIMONIOUS", "notes": "One set."},
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
            {"references": [{"id": "PMID:1", "title": "t", "findings": [
                {"statement": "Relevant to condition sets 1, 8 and 21."}]}]},
            "condition_set_out_of_range",
            id="finding cites a set the rule does not have",
        ),
        pytest.param(
            {"review_summary": "CS25 matches DPM1."},
            "condition_set_out_of_range",
            id="prose cites a set the rule does not have",
        ),
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
        **MEANING,
        annotation_assessments=[
            {"annotation_kind": "GO_TERM", "value": "GO:0010605", "assessment": "INCORRECT",
             "incorrect_examples": ["P12345"]}
        ],
    )
    assert checks(data, tmp_path) == set()


def test_withdrawn_rule_can_be_deprecated_without_sets(tmp_path: Path) -> None:
    withdrawn_rule = {"rule_id": "A", "condition_sets": [], "withdrawn": True, "retrieved_date": "2026-11-10"}
    assert checks(review(action="WITHDRAWN", rule=withdrawn_rule), tmp_path) == set()
    assert "withdrawn_action_mismatch" in checks(review(action="DEPRECATE", confidence=0.9, rule=withdrawn_rule), tmp_path)
    assert "withdrawn_action_mismatch" in checks(review(action="WITHDRAWN"), tmp_path)


def test_accept_with_a_meaning_judgement_passes(tmp_path: Path) -> None:
    assert checks(review(action="ACCEPT", confidence=0.8, **MEANING), tmp_path) == set()


def _meaning(assessment: str, units: list[dict[str, Any]], parsimony: str = "PARSIMONIOUS") -> dict[str, Any]:
    return {"biological_meaning": {"assessment": assessment}, "biological_units": units,
            "parsimony": {"assessment": parsimony}}


@pytest.mark.parametrize(
    "overrides,expected",
    [
        pytest.param({"action": "ACCEPT", "confidence": 0.8}, "verdict_without_meaning",
                     id="accurate per set, never asked whether the rule means anything"),
        pytest.param({"action": "ACCEPT", "confidence": 0.8, **_meaning("NOT_ASSESSED", [UNIT])},
                     "verdict_without_meaning", id="accept with meaning not assessed"),
        pytest.param({"action": "ACCEPT", "confidence": 0.8, **_meaning("TRUE_BUT_UNINFORMATIVE", [UNIT])},
                     "accept_of_uninformative_rule", id="accepting an umbrella term"),
        pytest.param({"action": "ACCEPT", "confidence": 0.8, **_meaning("COHERENT", [UNIT], "REDUNDANT")},
                     "accept_without_parsimony", id="accepting a redundant rule"),
        pytest.param({"action": "SPLIT", "confidence": 0.8, **_meaning("HETEROGENEOUS", [UNIT, {"name": "other"}])},
                     "split_without_units", id="split with one target term"),
        pytest.param({"action": "MODIFY", "confidence": 0.8, "suggested_modifications": "x",
                      **_meaning("TRUE_BUT_UNINFORMATIVE", [UNIT])},
                     "uninformative_without_units", id="uninformative with no more specific term shown"),
        pytest.param({"action": "MODIFY", "confidence": 0.8, "suggested_modifications": "x",
                      **_meaning("HETEROGENEOUS", [UNIT])},
                     "heterogeneous_without_units", id="heterogeneous with one unit"),
        pytest.param({"action": "ACCEPT", "confidence": 0.8,
                      **_meaning("COHERENT", [{**UNIT, "most_informative_term_label": "gene silencing"}])},
                     "unit_term_label_mismatch", id="unit term label from memory"),
        pytest.param({"action": "ACCEPT", "confidence": 0.8, **_meaning("COHERENT", [{**UNIT, "evidence": []}])},
                     "unit_term_without_evidence", id="unit term with no curated annotation"),
        pytest.param({"action": "ACCEPT", "confidence": 0.8, **_meaning("COHERENT", [{**UNIT, "condition_sets": [7]}])},
                     "condition_set_out_of_range", id="unit cites a set the rule lacks"),
        pytest.param({"action": "ACCEPT", "confidence": 0.8,
                      **_meaning("COHERENT", [{**UNIT, "example_proteins": ["DICER1"]}])},
                     "example_not_an_accession", id="unit example is a gene symbol"),
    ],
)
def test_meaning_error_is_caught(overrides: dict[str, Any], expected: str, tmp_path: Path) -> None:
    assert expected in checks(review(**overrides), tmp_path)


def test_redundancy_figures_are_checked_against_the_table(tmp_path: Path) -> None:
    rule = {"rule_id": "ARBA00026480", "condition_sets": [DICER_SET], "retrieved_date": "2026-11-10",
            "source_condition_set_count": 355,
            "go_annotations": [{"go_id": "GO:0010605",
                                "go_label": "negative regulation of macromolecule metabolic process"}]}
    data = review(id="ARBA00026480", rule=rule,
                  biological_meaning={"assessment": "NOT_ASSESSED", "consequent_descendant_count": 12})
    assert "redundancy_receipt_mismatch" in checks(data, tmp_path)
    data["biological_meaning"]["consequent_descendant_count"] = 524
    assert "redundancy_receipt_mismatch" not in checks(data, tmp_path)


def test_naming_the_analysis_cap_is_allowed_when_undecided(tmp_path: Path) -> None:
    data = review(review_summary="12 of 343 sets were read, the analysis limit of 12 being the tool default.")
    assert checks(data, tmp_path) == set()


def test_obsolete_consequent_justifies_deprecate(tmp_path: Path) -> None:
    data = review(
        action="DEPRECATE",
        confidence=0.9,
        **MEANING,
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


RULE_REVIEWS = sorted((Path(__file__).resolve().parents[1] / "rules").rglob("*-review.yaml"))


@pytest.mark.parametrize("review_file", RULE_REVIEWS, ids=lambda path: path.parent.name)
def test_committed_rule_reviews_pass_offline_receipt_checks(review_file: Path) -> None:
    """Every committed rule review keeps its receipts.

    The schema check and ``rules-validate`` are run by hand or by the authoring
    hook; this test is what makes a later edit that drops a confidence, a rule
    snapshot or a correct label fail in CI. If a label error appears after an
    InterPro or GO rename, refresh the cache with ``--refresh-labels``.
    """
    from ai_gene_review.validation.rule_review_receipts import validate_rule_review_receipts

    report = ValidationReport(file_path=review_file, is_valid=True)
    validate_rule_review_receipts(review_file, report)
    errors = [str(issue) for issue in report.issues if issue.is_error()]
    assert not errors, "\n".join(errors)


def test_rule_reviews_were_found() -> None:
    assert len(RULE_REVIEWS) >= 78


@pytest.mark.integration
@pytest.mark.parametrize(
    "term,relation,expected",
    [
        ("GO:0010605", "SAME_AS_CONSEQUENT", False),
        ("GO:0010629", "DESCENDANT_OF_CONSEQUENT", False),  # negative regulation of gene expression
        ("GO:0010629", "OUTSIDE_CONSEQUENT", True),
        ("GO:0006412", "DESCENDANT_OF_CONSEQUENT", True),  # translation is not under GO:0010605
    ],
)
def test_unit_term_relation_is_checked_against_the_ontology(term: str, relation: str, expected: bool) -> None:
    from ai_gene_review.validation.rule_review_receipts import check_review_online

    unit = {**UNIT, "most_informative_term_id": term, "term_relation": relation}
    data = review(rule={"rule_id": "X", "go_annotations": [{"go_id": "GO:0010605"}]}, biological_units=[unit])
    report = ValidationReport(is_valid=True)
    check_review_online(data, report)
    fired = any(issue.check_type == "unit_term_relation_mismatch" for issue in report.issues)
    assert fired is expected


def test_deprecate_of_a_rule_that_does_no_work(tmp_path: Path) -> None:
    meaning = {**MEANING, "biological_meaning": {"assessment": "COHERENT", "sets_covered_by_more_specific_rule": 1}}
    assert checks(review(action="DEPRECATE", confidence=0.8, **meaning), tmp_path) == set()
    meaning["biological_meaning"]["sets_covered_by_more_specific_rule"] = 0
    assert "deprecate_without_counterexample" in checks(review(action="DEPRECATE", confidence=0.8, **meaning), tmp_path)
