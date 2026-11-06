"""Tests for the EC-class consistency check (ec_class_conflict warnings)."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, FrozenSet

import pytest

from ai_gene_review.validation.ec_class_consistency import (
    CHECK_TYPE,
    check_ec_class_consistency,
    class_conflict,
    find_ec_class_conflicts,
    protein_ecs_for_review,
    uniprot_ec_numbers,
)
from ai_gene_review.validation.validation_report import ValidationReport

ROOT = Path(__file__).resolve().parent.parent
PP_2213 = ROOT / "genes/PSEPK/PP_2213/PP_2213-ai-review.yaml"

#: A fixed term -> EC table, so the logic is tested without the GO database.
TERM_ECS: Dict[str, FrozenSet[str]] = {
    "GO:0004321": frozenset({"2.3.1.86"}),  # fatty-acyl-CoA synthase (FAS reaction)
    "GO:0031956": frozenset({"6.2.1.2"}),  # medium-chain fatty acid-CoA ligase
    "GO:0016491": frozenset({"1.-.-.-"}),  # oxidoreductase activity (grouping)
    "GO:0043139": frozenset({"5.6.2.3"}),  # 5'-3' DNA helicase
    "GO:0004359": frozenset({"3.5.1.2"}),  # glutaminase
}


def lookup(term_id: str) -> FrozenSet[str]:
    """Term ECs from :data:`TERM_ECS` (empty when the term has none)."""
    return TERM_ECS.get(term_id, frozenset())


def row(term_id: str, action: str, **extra: Any) -> Dict[str, Any]:
    """A minimal existing-annotation row."""
    review = {"action": action, **extra.pop("review", {})}
    return {
        "term": {"id": term_id, "label": term_id},
        "evidence_type": "IEA",
        "review": review,
        **extra,
    }


@pytest.mark.parametrize(
    "term_ecs,protein_ecs,expected",
    [
        ({"2.3.1.86"}, {"6.2.1.-"}, True),
        ({"6.2.1.3"}, {"6.2.1.-"}, False),
        (
            {"2.3.1.86"},
            {"6.2.1.1", "2.3.1.41"},
            False,
        ),  # multifunctional: one class agrees
        ({"1.-.-.-"}, {"7.1.1.2"}, False),  # partial grouping EC ignored
        ({"5.6.2.3"}, {"3.6.4.12"}, False),  # benign helicase pair
        ({"3.5.1.2"}, {"6.3.5.5"}, False),  # benign glutaminase/amidotransferase pair
        ({"3.5.1.2"}, {"2.7.1.1"}, True),
        (set(), {"6.2.1.-"}, False),
        ({"2.3.1.86"}, set(), False),
    ],
)
def test_class_conflict(term_ecs: set, protein_ecs: set, expected: bool) -> None:
    """Conflict only when every full term EC is outside every protein EC class."""
    assert class_conflict(term_ecs, protein_ecs) is expected


@pytest.mark.parametrize(
    "annotation,flagged",
    [
        (row("GO:0004321", "ACCEPT"), True),
        (row("GO:0004321", "KEEP_AS_NON_CORE"), True),
        (row("GO:0004321", "NEW"), True),
        (
            row("GO:0004321", "MODIFY", review={"reason": "Replace this broad term"}),
            True,
        ),
        (
            row(
                "GO:0004321",
                "MODIFY",
                review={"reason": "Wrong reaction: FAS, not a ligase"},
            ),
            False,
        ),
        (row("GO:0004321", "REMOVE"), False),
        (row("GO:0004321", "MARK_AS_OVER_ANNOTATED"), False),
        (row("GO:0004321", "ACCEPT", negated=True), False),
        (row("GO:0004321", "ACCEPT", qualifier="contributes_to"), False),
        (row("GO:0031956", "ACCEPT"), False),
        (row("GO:0016491", "ACCEPT"), False),
    ],
)
def test_find_existing_annotation_conflicts(
    annotation: Dict[str, Any], flagged: bool
) -> None:
    """Kept rows and refinement-worded MODIFYs are flagged; rejected rows are not."""
    found = list(
        find_ec_class_conflicts(
            {"existing_annotations": [annotation]}, frozenset({"6.2.1.-"}), lookup
        )
    )
    assert bool(found) is flagged


def test_core_function_conflict() -> None:
    """A core-function molecular function is checked too."""
    data = {
        "core_functions": [{"molecular_function": {"id": "GO:0004321", "label": "x"}}]
    }
    found = list(find_ec_class_conflicts(data, frozenset({"6.2.1.-"}), lookup))
    assert [c.path for c in found] == ["core_functions[0].molecular_function"]


def test_no_protein_ec_means_no_conflict() -> None:
    """A record without EC numbers gives the check nothing to compare."""
    data = {"existing_annotations": [row("GO:0004321", "ACCEPT")]}
    assert list(find_ec_class_conflicts(data, frozenset(), lookup)) == []


def test_uniprot_ec_numbers_reads_pp_2213() -> None:
    """The PP_2213 record carries EC 6.2.1.- on its DE lines."""
    text = (ROOT / "genes/PSEPK/PP_2213/PP_2213-uniprot.txt").read_text()
    assert uniprot_ec_numbers(text) == frozenset({"6.2.1.-"})
    assert protein_ecs_for_review(PP_2213) == frozenset({"6.2.1.-"})


def test_check_reports_warning_with_check_type(tmp_path: Path) -> None:
    """The validator hook emits a WARNING tagged ec_class_conflict."""
    (tmp_path / "X-uniprot.txt").write_text(
        "DE   RecName: Full=Acyl-CoA synthetase;\nDE            EC=6.2.1.3;\n"
    )
    review = tmp_path / "X-ai-review.yaml"
    data = {
        "existing_annotations": [
            row("GO:0004321", "MODIFY", review={"reason": "less precise"})
        ]
    }
    report = ValidationReport(file_path=review, is_valid=True)
    check_ec_class_consistency(data, report, review, lookup)
    assert [i.check_type for i in report.issues] == [CHECK_TYPE]
    assert "treats it as too broad" in report.issues[0].message
    assert report.is_valid


def test_check_is_skipped_without_ontology(tmp_path: Path) -> None:
    """No term lookup (ontology checks off) means no warnings."""
    report = ValidationReport(file_path=tmp_path / "X-ai-review.yaml", is_valid=True)
    check_ec_class_consistency(
        {"existing_annotations": [row("GO:0004321", "ACCEPT")]},
        report,
        tmp_path / "X-ai-review.yaml",
        None,
    )
    assert report.issues == []


@pytest.mark.integration
def test_go_term_ecs_reads_go_database() -> None:
    """The oaklib-backed lookup returns GO's EC cross-references."""
    from ai_gene_review.validation.ec_class_consistency import go_term_ecs

    ecs = go_term_ecs()
    assert ecs("GO:0004321") == frozenset({"2.3.1.86"})
    assert ecs("GO:0015645") == frozenset()
