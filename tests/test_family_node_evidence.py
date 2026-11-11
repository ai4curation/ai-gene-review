"""Tests for filling PAINT evidence/negation/seeds into family-review node assessments."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.family_node_evidence import (
    fill_review_text,
    planned_fields,
)
from ai_gene_review.validation.module_validator import PaintAnnotationRow

FAMILY = "PTHR99999"


def row(node: str, go_id: str, evidence: str, negated: bool, seeds: str) -> PaintAnnotationRow:
    """Build one PAINT slice row for FAMILY."""
    return PaintAnnotationRow(
        family=FAMILY,
        node_curie=f"PANTHER:{node}",
        go_id=go_id,
        aspect="F",
        evidence=evidence,
        negated=negated,
        seeds=seeds,
        source_path=Path("unused"),
    )


IRD = row("PTN2", "GO:0000002", "IRD", True, "PANTHER:PTN1")
IBD = row("PTN1", "GO:0000002", "IBD", False, "UniProtKB:P11111|MGI:MGI:1")
INDEX = {"PANTHER:PTN1": [IBD], "PANTHER:PTN2": [IRD]}


@pytest.mark.parametrize(
    ("assessment", "rows", "expected"),
    [
        # loss row with nothing declared: evidence, negation and the blocked IBD node
        (
            {"assessment": "UNRESOLVED"},
            [IRD],
            {"evidence": "IRD", "negated": True, "seeds": [{"id": "PANTHER:PTN1"}]},
        ),
        # loss row whose seeds a curator already wrote: seeds are left alone
        (
            {"assessment": "UNRESOLVED", "seeds": [{"id": "PANTHER:PTN1", "label": "x"}]},
            [IRD],
            {"evidence": "IRD", "negated": True},
        ),
        # gain row: only the evidence code; gain seeds are curated subsets, not touched
        ({"assessment": "SOUND"}, [IBD], {"evidence": "IBD"}),
        # already complete: nothing to add
        ({"assessment": "SOUND", "evidence": "IBD"}, [IBD], {}),
        # PAINT records the same node and term as both a gain and a loss: ambiguous, skip
        ({"assessment": "SOUND"}, [IBD, IRD], {}),
        # no PAINT rows (the validator reports this): nothing to add
        ({"assessment": "SOUND"}, [], {}),
    ],
)
def test_planned_fields(assessment: dict, rows: list, expected: dict) -> None:
    """Only fields PAINT determines, and never a verdict."""
    assert planned_fields(assessment, rows) == expected


def test_planned_fields_never_overrides_a_declared_negation() -> None:
    """An explicit ``negated: false`` on a loss row is a curator statement to report, not rewrite."""
    assert "negated" not in planned_fields({"assessment": "SOUND", "negated": False}, [IRD])


REVIEW = """\
family_id: PANTHER:PTHR99999
node_assessments:
- node_id: PANTHER:PTN1
  asserted_term:
    id: GO:0000002
    label: some activity
  paint_snapshot: '20260101'
  assessment: SOUND
  assessment_reason: >-
    A folded reason that must survive
    byte for byte.
- node_id: PANTHER:PTN2
  asserted_term:
    id: GO:0000002
    label: some activity
  assessment: SOUND
  assessment_reason: The clade lacks the activity.
references: []
"""


def test_fill_review_text_inserts_after_asserted_term_and_keeps_the_rest() -> None:
    """Edits are line insertions only; every original line survives unchanged and in order."""
    new_text, changes, problems = fill_review_text(REVIEW, FAMILY, INDEX)

    assert [c.node for c in changes] == ["PANTHER:PTN1", "PANTHER:PTN2"]
    original = REVIEW.splitlines()
    kept = [line for line in new_text.splitlines() if line in original]
    assert kept == original

    data = yaml.safe_load(new_text)
    first, second = data["node_assessments"]
    assert first["evidence"] == "IBD" and "negated" not in first
    assert second["evidence"] == "IRD" and second["negated"] is True
    assert second["seeds"] == [{"id": "PANTHER:PTN1"}]
    assert first["assessment_reason"] == "A folded reason that must survive byte for byte."
    # the verdict is untouched, and its remaining disagreement with PAINT is reported
    assert second["assessment"] == "SOUND"
    assert len(problems) == 1 and "verdict SOUND is for gain rows" in problems[0]


def test_fill_review_text_is_idempotent() -> None:
    """A second pass over filled text changes nothing."""
    once, _, _ = fill_review_text(REVIEW, FAMILY, INDEX)
    twice, changes, _ = fill_review_text(once, FAMILY, INDEX)
    assert twice == once and changes == []


def test_fill_review_text_ignores_other_families_rows() -> None:
    """PTN ids are not family-unique; another family's row for the node must not be used."""
    other = PaintAnnotationRow(
        family="PTHR11111", node_curie="PANTHER:PTN2", go_id="GO:0000002", aspect="F",
        evidence="IRD", negated=True, seeds="PANTHER:PTN1", source_path=Path("unused"),
    )
    _, changes, _ = fill_review_text(REVIEW, FAMILY, {"PANTHER:PTN2": [other]})
    assert changes == []
