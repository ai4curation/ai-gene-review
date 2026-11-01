"""Tests for checking declared PAINT losses on gene-review rows against paint.tsv."""

from pathlib import Path

from ai_gene_review.validation.module_validator import PaintAnnotationRow
from ai_gene_review.validation.paint_loss_check import check_paint_losses
from ai_gene_review.validation.validation_report import ValidationReport


def row(node: str, go: str, evidence: str, negated: bool) -> PaintAnnotationRow:
    """One local PAINT slice row."""
    return PaintAnnotationRow(
        family="PTHR1", node_curie=node, go_id=go, aspect="F", evidence=evidence,
        negated=negated, seeds="PANTHER:PTN1", source_path=Path("unused"),
    )


INDEX = {
    "PANTHER:PTN2": [row("PANTHER:PTN2", "GO:1", "IRD", True), row("PANTHER:PTN2", "GO:2", "IBD", False)],
}


def review_with(loss: dict, term: str = "GO:1") -> dict:
    """A gene review with one IBA row declaring ``loss``."""
    return {"existing_annotations": [{
        "term": {"id": term}, "evidence_type": "IBA",
        "review": {"action": "ACCEPT", "propagation_review": {
            "root_cause": "NO_FAILURE_CORE", "paint_losses": [loss]}},
    }]}


def check(data: dict) -> list[str]:
    """Messages from the check."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_paint_losses(data, report, INDEX)
    return [i.message for i in report.issues]


def test_matching_loss_passes() -> None:
    """A declared IRD that paint.tsv records for the row's term raises nothing."""
    assert check(review_with({"node_id": "PANTHER:PTN2", "evidence": "IRD", "agreement": "CONTRADICTED"})) == []


def test_node_without_a_local_slice_is_not_checked() -> None:
    """Families with no paint.tsv slice cannot be checked, so nothing is reported."""
    assert check(review_with({"node_id": "PANTHER:PTN9", "evidence": "IRD", "agreement": "AGREES"})) == []


def test_wrong_term_or_evidence_warns() -> None:
    """The node is local, but it carries no loss of this term, or not with this code."""
    wrong_term = check(review_with({"node_id": "PANTHER:PTN2", "evidence": "IRD", "agreement": "AGREES"}, "GO:2"))
    wrong_code = check(review_with({"node_id": "PANTHER:PTN2", "evidence": "IKR", "agreement": "AGREES"}))
    assert len(wrong_term) == 1 and "no IRD/IKR loss of GO:2" in wrong_term[0]
    assert len(wrong_code) == 1 and "records IRD, not IKR" in wrong_code[0]
