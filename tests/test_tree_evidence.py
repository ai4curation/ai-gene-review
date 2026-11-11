"""Tests for the tree-evidence policy on gene-review rows that overrule an IBA."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from ai_gene_review.validation.tree_evidence import (
    check_tree_evidence,
    phylo_reference_ids,
)
from ai_gene_review.validation.validation_report import ValidationReport, ValidationSeverity

REVIEW = Path("genes/human/TEST/TEST-ai-review.yaml")
OWN = "file:human/TEST/TEST-phylo.yaml"
QUOTE = "GO:0000398 (mRNA splicing, via spliceosome): PAINT node PTN000391532 is a speciation node at Eukaryota"


def review(
    action: str = "REMOVE",
    evidence: str = "IBA",
    supported_by: list[dict[str, str]] | None = None,
    propagation_review: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """A gene review with one row on GO:0000398."""
    body: dict[str, Any] = {"action": action, "reason": "x"}
    if supported_by is not None:
        body["supported_by"] = supported_by
    if propagation_review is not None:
        body["propagation_review"] = propagation_review
    return {
        "existing_annotations": [
            {"term": {"id": "GO:0000398", "label": "mRNA splicing, via spliceosome"}, "evidence_type": evidence, "review": body}
        ]
    }


def check(data: dict[str, Any], yaml_file: Path | None = REVIEW) -> list[tuple[str | None, str]]:
    """``(check_type, message)`` of every issue the policy raises."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_tree_evidence(data, report, yaml_file)
    assert all(i.severity == ValidationSeverity.WARNING for i in report.issues)
    return [(i.check_type, i.message) for i in report.issues]


def test_phylo_reference_ids_follow_the_review_path() -> None:
    assert phylo_reference_ids(REVIEW) == {OWN, "file:genes/human/TEST/TEST-phylo.yaml"}
    assert phylo_reference_ids(Path("/abs/repo/genes/worm/sta-1/sta-1-ai-review.yaml")) == {
        "file:worm/sta-1/sta-1-phylo.yaml",
        "file:genes/worm/sta-1/sta-1-phylo.yaml",
    }
    # A review outside genes/ has no extract of its own to name.
    assert phylo_reference_ids(Path("tests/input/CFAP300-ai-review.yaml")) == set()
    assert phylo_reference_ids(None) == set()


@pytest.mark.parametrize("action", ["REMOVE", "MARK_AS_OVER_ANNOTATED"])
def test_overruling_an_iba_without_the_tree_warns(action: str) -> None:
    issues = check(review(action))
    assert [kind for kind, _ in issues] == ["missing_tree_evidence"]
    assert "GO:0000398" in issues[0][1] and action in issues[0][1]


def test_overruling_with_the_rows_own_summary_passes() -> None:
    assert check(review(supported_by=[{"reference_id": OWN, "supporting_text": QUOTE}])) == []
    assert check(review(supported_by=[{"reference_id": "file:genes/human/TEST/TEST-phylo.yaml", "supporting_text": QUOTE}])) == []


def test_other_support_does_not_stand_in_for_the_tree() -> None:
    issues = check(review(supported_by=[{"reference_id": "PMID:1", "supporting_text": "no splicing role"}]))
    assert [kind for kind, _ in issues] == ["missing_tree_evidence"]


def test_another_genes_extract_does_not_count() -> None:
    cited = [{"reference_id": "file:human/OTHER/OTHER-phylo.yaml", "supporting_text": QUOTE}]
    assert [kind for kind, _ in check(review(supported_by=cited))] == ["missing_tree_evidence"]


def test_quote_must_be_about_this_row() -> None:
    cited = [{"reference_id": OWN, "supporting_text": "GO:0005681 (spliceosomal complex): PAINT node PTN000391532 is"}]
    issues = check(review(supported_by=cited))
    assert [kind for kind, _ in issues] == ["tree_evidence_other_row"]
    assert "GO:0000398" in issues[0][1]


@pytest.mark.parametrize("action", ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "UNDECIDED", "TOO_GENERAL"])
def test_actions_that_keep_the_claim_are_not_asked_for_the_tree(action: str) -> None:
    assert check(review(action)) == []


@pytest.mark.parametrize("evidence", ["IEA", "ISS", "ISO", "IDA"])
def test_only_iba_rows_are_covered(evidence: str) -> None:
    assert check(review(evidence=evidence)) == []


def test_without_a_gene_folder_any_phylo_extract_is_accepted() -> None:
    cited = [{"reference_id": "file:human/OTHER/OTHER-phylo.yaml", "supporting_text": QUOTE}]
    assert check(review(supported_by=cited), yaml_file=None) == []
    assert [kind for kind, _ in check(review(), yaml_file=None)] == ["missing_tree_evidence"]


def test_residue_loss_argument_needs_a_residue_claim() -> None:
    cited = [{"reference_id": OWN, "supporting_text": QUOTE}]
    loss = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["PSEUDO_OR_SUBACTIVITY_LOSS"]}
    issues = check(review(supported_by=cited, propagation_review=loss))
    assert [kind for kind, _ in issues] == ["missing_residue_evidence"]

    with_claim = {**loss, "residue_claims": [{"claim_type": "LOST"}]}
    assert check(review(supported_by=cited, propagation_review=with_claim)) == []
    waived = {**loss, "residue_claims_not_applicable": "capping versus severing, not a point residue"}
    assert check(review(supported_by=cited, propagation_review=waived)) == []


def test_residue_rule_covers_other_propagated_rows_but_only_when_overruled() -> None:
    loss = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["PSEUDO_OR_SUBACTIVITY_LOSS"]}
    assert [k for k, _ in check(review(evidence="IEA", propagation_review=loss))] == ["missing_residue_evidence"]
    assert check(review("KEEP_AS_NON_CORE", evidence="IEA", propagation_review=loss)) == []


def test_rows_without_a_review_are_skipped() -> None:
    assert check({"existing_annotations": [{"term": {"id": "GO:1"}, "evidence_type": "IBA"}, "junk"]}) == []
    assert check({}) == []


GOA_COLUMNS = ["GENE PRODUCT DB", "GENE PRODUCT ID", "SYMBOL", "QUALIFIER", "GO TERM", "GO NAME", "GO ASPECT", "GO EVIDENCE CODE", "WITH/FROM"]


def gene_folder(tmp_path: Path, goa_rows: list[tuple[str, str, str]]) -> Path:
    """A ``genes/human/TEST`` folder whose GOA file holds ``(qualifier, term, evidence)`` rows."""
    folder = tmp_path / "genes" / "human" / "TEST"
    folder.mkdir(parents=True)
    lines = ["\t".join(GOA_COLUMNS)]
    for qualifier, term, evidence in goa_rows:
        lines.append("\t".join(["UniProtKB", "P00001", "TEST", qualifier, term, "a term", "biological_process", evidence, "PANTHER:PTN000391532|UniProtKB:P62995"]))
    (folder / "TEST-goa.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return folder / "TEST-ai-review.yaml"


def test_a_row_still_in_the_goa_file_is_asked_for_the_tree(tmp_path: Path) -> None:
    yaml_file = gene_folder(tmp_path, [("involved_in", "GO:0000398", "IBA")])
    assert [kind for kind, _ in check(review(), yaml_file)] == ["missing_tree_evidence"]


def test_a_row_paint_has_withdrawn_is_not_asked_for_the_tree(tmp_path: Path) -> None:
    # The gene's GOA file no longer has this IBA row, so its extract has no row to quote.
    yaml_file = gene_folder(tmp_path, [("involved_in", "GO:0005681", "IBA"), ("involved_in", "GO:0000398", "IEA")])
    assert check(review(), yaml_file) == []


def test_a_positive_row_is_not_matched_by_a_negated_goa_row(tmp_path: Path) -> None:
    yaml_file = gene_folder(tmp_path, [("NOT|involved_in", "GO:0000398", "IBA")])
    assert check(review(), yaml_file) == []
    negated = review()
    negated["existing_annotations"][0]["negated"] = True
    assert [kind for kind, _ in check(negated, yaml_file)] == ["missing_tree_evidence"]


def test_a_withdrawn_row_is_still_asked_for_its_residue_claim(tmp_path: Path) -> None:
    yaml_file = gene_folder(tmp_path, [("involved_in", "GO:0005681", "IBA")])
    loss = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["PSEUDO_OR_SUBACTIVITY_LOSS"]}
    assert [kind for kind, _ in check(review(propagation_review=loss), yaml_file)] == ["missing_residue_evidence"]
