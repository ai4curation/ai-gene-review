"""Tests for family/gene cross-checking.

The value of this validator is that it *fires* when a family review and a gene review
disagree, so most tests construct a disagreement and assert a CONFLICT. A small synthetic
corpus is built on disk rather than pointing at `genes/`, so the tests are fast and do not
change meaning when the real corpus does.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.family_gene_crosscheck import (
    GeneRef,
    Verdict,
    check_family_gene_disagreement,
    check_pruning_conflicts,
    check_scope_violations,
    crosscheck_family_review,
    gene_actions_for_term,
    index_genes_by_family,
)

FAMILY = "PANTHER:PTHR11022"
CATALYTIC_SF = "PANTHER:PTHR11022:SF77"
RECEPTOR_SF = "PANTHER:PTHR11022:SF41"
TERM = "GO:0008745"


def _family_review(*, scope="SUBFAMILY_ONLY", allowed=(CATALYTIC_SF,), node_affects=()):
    review = {
        "family_id": FAMILY,
        "term_assessments": [
            {
                "assessed_term": {"id": TERM, "label": "amidase"},
                "scope": scope,
                "scope_reason": "test",
                "applicable_subfamilies": [{"id": sf, "label": "x"} for sf in allowed],
            }
        ],
    }
    if node_affects:
        review["node_assessments"] = [
            {
                "node_id": "PANTHER:PTN002475783",
                "asserted_term": {"id": TERM, "label": "amidase"},
                "assessment": "NEEDS_PRUNING",
                "assessment_reason": "test",
                "affected_subfamilies": [
                    {"id": sf, "label": "x"} for sf in node_affects
                ],
            }
        ]
    return review


def _write_gene(tmp_path: Path, symbol: str, sf: str | None, action: str,
                *, term=TERM, negated=False) -> GeneRef:
    """Write a minimal gene review + UniProt record into a synthetic corpus."""
    d = tmp_path / "genes" / "ANOGA" / symbol
    d.mkdir(parents=True, exist_ok=True)
    lines = [f"AC   {symbol}ACC;", "DR   PANTHER; PTHR11022; PEPTIDOGLYCAN RECOGNITION PROTEIN; 1."]
    if sf:
        lines.append(f"DR   PANTHER; {sf.split(':', 1)[1]}; SUBFAM; 1.")
    (d / f"{symbol}-uniprot.txt").write_text("\n".join(lines) + "\n")
    ann = {"term": {"id": term, "label": "x"}, "evidence_type": "IBA",
           "review": {"action": action}}
    if negated:
        ann["negated"] = True
    (d / f"{symbol}-ai-review.yaml").write_text(
        yaml.safe_dump({"id": f"{symbol}ACC", "existing_annotations": [ann]})
    )
    return GeneRef(f"{symbol}ACC", symbol, FAMILY, sf, d / f"{symbol}-ai-review.yaml")


@pytest.mark.parametrize(
    "sf,action,expected",
    [
        # gene outside the allowed subfamilies that keeps the term -> conflict
        (RECEPTOR_SF, "ACCEPT", Verdict.CONFLICT),
        (RECEPTOR_SF, "KEEP_AS_NON_CORE", Verdict.CONFLICT),
        # gene outside the allowed subfamilies that already flags it -> consistent
        (RECEPTOR_SF, "REMOVE", Verdict.OK),
        (RECEPTOR_SF, "MARK_AS_OVER_ANNOTATED", Verdict.OK),
    ],
)
def test_scope_violation_verdicts(tmp_path, sf, action, expected):
    gene = _write_gene(tmp_path, "PGRPLC", sf, action)
    (result,) = check_scope_violations(_family_review(), {FAMILY: [gene]})
    assert result.verdict is expected


def test_gene_inside_allowed_subfamily_is_not_reported(tmp_path):
    """A catalytic member keeping the amidase term is correct and must stay silent."""
    gene = _write_gene(tmp_path, "PGRPLB", CATALYTIC_SF, "ACCEPT")
    assert check_scope_violations(_family_review(), {FAMILY: [gene]}) == []


def test_not_applicable_scope_flags_every_member(tmp_path):
    """NOT_APPLICABLE means no member may retain the term, whatever its subfamily."""
    gene = _write_gene(tmp_path, "PGRPLB", CATALYTIC_SF, "ACCEPT")
    (result,) = check_scope_violations(
        _family_review(scope="NOT_APPLICABLE", allowed=()), {FAMILY: [gene]}
    )
    assert result.verdict is Verdict.CONFLICT
    assert "no member of this family may retain it" in result.message


def test_negated_annotation_is_agreement_not_conflict(tmp_path):
    """A curated NOT row asserts the gene lacks the function -- that agrees with the family."""
    gene = _write_gene(tmp_path, "PGRPLC", RECEPTOR_SF, "ACCEPT", negated=True)
    assert check_scope_violations(_family_review(), {FAMILY: [gene]}) == []


def test_gene_without_the_term_is_not_reported(tmp_path):
    gene = _write_gene(tmp_path, "PGRPLC", RECEPTOR_SF, "ACCEPT", term="GO:0042834")
    assert check_scope_violations(_family_review(), {FAMILY: [gene]}) == []


def test_pruning_conflict_fires_for_affected_subfamily(tmp_path):
    gene = _write_gene(tmp_path, "PGRPLC", RECEPTOR_SF, "ACCEPT")
    results = check_pruning_conflicts(
        _family_review(node_affects=(RECEPTOR_SF,)), {FAMILY: [gene]}
    )
    assert [r.verdict for r in results] == [Verdict.CONFLICT]
    assert "needs pruning" in results[0].message


def test_pruning_ignores_unaffected_subfamily(tmp_path):
    gene = _write_gene(tmp_path, "PGRPLB", CATALYTIC_SF, "ACCEPT")
    assert check_pruning_conflicts(
        _family_review(node_affects=(RECEPTOR_SF,)), {FAMILY: [gene]}
    ) == []


def test_converse_disagreement_family_says_safe_gene_removes(tmp_path):
    """The other direction: family covers this gene, gene removes the term anyway."""
    gene = _write_gene(tmp_path, "PGRPLB", CATALYTIC_SF, "REMOVE")
    (result,) = check_family_gene_disagreement(_family_review(), {FAMILY: [gene]})
    assert result.verdict is Verdict.CONFLICT
    assert "removes it" in result.message


def test_index_genes_by_family_extracts_join_keys(tmp_path):
    _write_gene(tmp_path, "PGRPLC", RECEPTOR_SF, "ACCEPT")
    _write_gene(tmp_path, "PGRPLB", CATALYTIC_SF, "ACCEPT")
    index = index_genes_by_family(tmp_path / "genes")
    refs = {g.symbol: g for g in index[FAMILY]}
    assert refs["PGRPLC"].subfamily == RECEPTOR_SF
    assert refs["PGRPLB"].subfamily == CATALYTIC_SF


def test_gene_with_no_subfamily_still_checked_against_scope(tmp_path):
    """A gene lacking an SF cross-reference cannot be in the allowed set, so it is flagged."""
    gene = _write_gene(tmp_path, "PGRPX", None, "ACCEPT")
    (result,) = check_scope_violations(_family_review(), {FAMILY: [gene]})
    assert result.verdict is Verdict.CONFLICT


def test_gene_actions_for_term_collects_multiple_rows(tmp_path):
    d = tmp_path / "g"
    d.mkdir()
    p = d / "x-ai-review.yaml"
    p.write_text(yaml.safe_dump({"existing_annotations": [
        {"term": {"id": TERM}, "review": {"action": "ACCEPT"}},
        {"term": {"id": TERM}, "review": {"action": "REMOVE"}},
    ]}))
    assert gene_actions_for_term(p)[TERM] == {"ACCEPT", "REMOVE"}


# --------------------------------------------------------------------------
# Against the real corpus
# --------------------------------------------------------------------------


@pytest.mark.integration
def test_real_pgrp_family_and_genes_agree():
    """The committed PGRP family review does not contradict any ANOGA PGRP gene review."""
    results = crosscheck_family_review(
        Path("interpro/panther/PTHR11022/PTHR11022-review.yaml")
    )
    conflicts = [r for r in results if r.verdict is Verdict.CONFLICT]
    assert not conflicts, [str(c) for c in conflicts]
    # and it really did join -- silence must not come from an empty join
    assert {r.gene for r in results} >= {"PGRPLC", "PGRPLD", "PGRPS1"}


@pytest.mark.integration
def test_flipping_a_real_gene_to_accept_produces_a_conflict(tmp_path):
    """Corrupting PGRPLC's action to ACCEPT makes the cross-check fire."""
    src = Path("genes/ANOGA/PGRPLC/PGRPLC-ai-review.yaml")
    doc = yaml.safe_load(src.read_text())
    flipped = 0
    for ann in doc["existing_annotations"]:
        if ann.get("term", {}).get("id") == TERM:
            ann.setdefault("review", {})["action"] = "ACCEPT"
            flipped += 1
    assert flipped, "expected PGRPLC to carry GO:0008745"

    corpus = tmp_path / "genes" / "ANOGA" / "PGRPLC"
    corpus.mkdir(parents=True)
    (corpus / "PGRPLC-ai-review.yaml").write_text(yaml.safe_dump(doc))
    (corpus / "PGRPLC-uniprot.txt").write_text(
        "AC   A7UTA1;\n"
        "DR   PANTHER; PTHR11022; PEPTIDOGLYCAN RECOGNITION PROTEIN; 1.\n"
        "DR   PANTHER; PTHR11022:SF41; PEPTIDOGLYCAN-RECOGNITION PROTEIN LC-RELATED; 1.\n"
    )
    review = yaml.safe_load(
        Path("interpro/panther/PTHR11022/PTHR11022-review.yaml").read_text()
    )
    index = index_genes_by_family(tmp_path / "genes")
    results = check_scope_violations(review, index) + check_pruning_conflicts(review, index)
    conflicts = [r for r in results if r.verdict is Verdict.CONFLICT]
    assert len(conflicts) == 2, [str(r) for r in results]
    assert {c.kind for c in conflicts} == {"SCOPE_VIOLATION", "PRUNING_CONFLICT"}
