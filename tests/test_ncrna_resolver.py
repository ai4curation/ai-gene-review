"""Tests for resolving an ncRNA gene symbol to its GO-annotated RNAcentral ids."""

from __future__ import annotations

import pytest

from ai_gene_review.etl import gene
from ai_gene_review.etl.gene import (
    RNAcentralCandidate,
    product_type_for_rna_type,
    resolve_gene_to_rnacentral,
)

# Shape of the MIR155 case: HGNC points at the precursor, but the curated
# rows sit on the mature 5p arm.
MIR155 = [
    RNAcentralCandidate("URS000062749E_9606", "hsa-mir-155 precursor", "pre miRNA"),
    RNAcentralCandidate("URS0000338542_9606", "hsa-miR-155-5p", "miRNA"),
    RNAcentralCandidate("URS000000AAAA_9606", "hsa-miR-155-3p", "miRNA"),
]
ROWS = {
    ("URS000062749E_9606", None): 2,
    ("URS000062749E_9606", gene.EXPERIMENTAL_EVIDENCE_ECO): 0,
    ("URS0000338542_9606", None): 132,
    ("URS0000338542_9606", gene.EXPERIMENTAL_EVIDENCE_ECO): 105,
    ("URS000000AAAA_9606", None): 0,
}


@pytest.fixture
def offline(monkeypatch):
    seen_taxa = []

    def search(symbol, taxon_id):
        seen_taxa.append(taxon_id)
        return [RNAcentralCandidate(c.id, c.description, c.rna_type) for c in MIR155]

    monkeypatch.setattr(gene, "search_rnacentral_candidates", search)
    monkeypatch.setattr(gene, "count_goa_rows", lambda pid, eco=None: ROWS[(pid, eco)])
    return seen_taxa


def test_primary_is_the_most_experimentally_annotated_sequence(offline):
    ranked = resolve_gene_to_rnacentral("MIR155", "human")
    assert [c.id for c in ranked] == ["URS0000338542_9606", "URS000062749E_9606"]
    assert ranked[0].experimental_rows == 105


def test_search_is_restricted_to_the_species_taxon(offline):
    resolve_gene_to_rnacentral("MIR155", "mouse")
    assert offline == ["10090"]


def test_no_annotated_sequence_is_an_error_naming_the_candidates(monkeypatch):
    monkeypatch.setattr(
        gene, "search_rnacentral_candidates", lambda s, t: [RNAcentralCandidate("URS1_9606", "orphan", "lncRNA")]
    )
    monkeypatch.setattr(gene, "count_goa_rows", lambda pid, eco=None: 0)
    with pytest.raises(ValueError, match=r"URS1_9606 \(orphan\)"):
        resolve_gene_to_rnacentral("ORPHAN1", "human")


def test_a_tie_for_first_place_is_an_error(monkeypatch):
    copies = [RNAcentralCandidate(f"URS{i}_9606", f"U3 copy {i}", "snoRNA") for i in (1, 2)]
    monkeypatch.setattr(gene, "search_rnacentral_candidates", lambda s, t: copies)
    monkeypatch.setattr(gene, "count_goa_rows", lambda pid, eco=None: 0 if eco else 2)
    with pytest.raises(ValueError, match="2 RNAcentral sequences for SNORD3A tie"):
        resolve_gene_to_rnacentral("SNORD3A", "human")


@pytest.mark.parametrize(
    "rna_type,expected",
    [("pre miRNA", "MIRNA"), ("miRNA", "MIRNA"), ("lncRNA", "LNCRNA"), ("snoRNA", "SNORNA"), ("Y_RNA", "OTHER_NCRNA")],
)
def test_product_type_for_rna_type(rna_type, expected):
    assert product_type_for_rna_type(rna_type) == expected
