"""Tests for finding PAINT IRD/IKR losses on a gene's lineage."""

import pytest

from ai_gene_review.etl.panther_paint import parse_ibd_gaf
from ai_gene_review.etl.panther_trees import ancestors_of, leaf_nodes_for, leaves_below
from ai_gene_review.validation.gene_paint_losses import losses_on_lineage, review_rows

# PTN1 (root) -> PTN2 -> {PTN4 (P1), PTN5 (P2)}; PTN1 -> PTN3 (P3)
TREE = {
    "leaves": {"PTN3": {"uniprot": "P3"}, "PTN4": {"uniprot": "P1"}, "PTN5": {"uniprot": "P2"}},
    "under": {"PTN1": ["PTN4", "PTN5", "PTN3"], "PTN2": ["PTN4", "PTN5"]},
}


def gaf(node: str, go: str, evidence: str, negated: bool, with_from: str) -> str:
    """One IBD.gaf line."""
    return (
        f"PANTHER\t{node}\t{node}\t{'NOT' if negated else ''}\t{go}\tGO_REF:0000033\t{evidence}"
        f"\t{with_from}\tF\t\t\tprotein\ttaxon:\t20260101\tGO_Central\t\t"
    )


IBD = parse_ibd_gaf([
    gaf("PTN1", "GO:1", "IBD", False, "UniProtKB:P3"),
    gaf("PTN2", "GO:1", "IRD", True, "PANTHER:PTN1"),
    gaf("PTN5", "GO:1", "IBD", False, "UniProtKB:P2"),
    gaf("PTN3", "GO:2", "IKR", True, "PANTHER:PTN1"),
])


def test_tree_helpers() -> None:
    """Leaf lookup, ancestors and clades."""
    assert leaf_nodes_for(TREE, "P1") == ["PTN4"]
    assert ancestors_of(TREE, "PTN4") == {"PTN1", "PTN2", "PTN4"}
    assert leaves_below(TREE, "PTN2") == ["PTN4", "PTN5"]


@pytest.mark.parametrize(
    ("leaf", "expected"),
    [
        # P1 sits under the IRD and nothing below re-annotates GO:1
        ("PTN4", [("PTN2", "GO:1", "IRD", ["PTN1"], 2, False)]),
        # P2 sits under the IRD, but PAINT gives its own leaf GO:1 again
        ("PTN5", [("PTN2", "GO:1", "IRD", ["PTN1"], 2, True)]),
        # P3 is outside the IRD clade; the IKR on its own leaf applies
        ("PTN3", [("PTN3", "GO:2", "IKR", ["PTN1"], 1, False)]),
    ],
)
def test_losses_on_lineage(leaf: str, expected: list) -> None:
    """Only losses on the leaf's own lineage are reported, with re-annotation flagged."""
    got = [
        (x.node, x.go_id, x.evidence, x.ancestral_nodes, x.clade_size, x.reannotated_below)
        for x in losses_on_lineage(TREE, leaf, IBD)
    ]
    assert got == expected


def test_review_rows_report_existing_annotations_and_core_functions() -> None:
    """Rows on the blocked term, including NOTs and core functions, are listed."""
    review = {
        "existing_annotations": [
            {"term": {"id": "GO:1"}, "evidence_type": "IBA", "review": {"action": "ACCEPT"}},
            {"term": {"id": "GO:1"}, "evidence_type": "IDA", "negated": True,
             "review": {"action": "ACCEPT"}},
            {"term": {"id": "GO:9"}, "evidence_type": "IEA", "review": {"action": "REMOVE"}},
        ],
        "core_functions": [{"molecular_function": {"id": "GO:1"}}],
    }
    assert review_rows(review, "GO:1") == ["IBA:ACCEPT", "NOT IDA:ACCEPT", "CORE_FUNCTION"]
