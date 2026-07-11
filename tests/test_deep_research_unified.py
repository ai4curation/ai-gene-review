"""Tests for the unified deep-research CLI helpers."""

import pytest

from ai_gene_review.tools.deep_research_unified import (
    extract_uniprot_fields,
    is_uniprot_accession,
)


@pytest.mark.parametrize(
    "value",
    [
        "Q9H2V7",  # canonical 6-char
        "P49069",
        "Q9HXE5",
        "A0A024R161",  # 10-char accession
        "P0DTC2",
    ],
)
def test_is_uniprot_accession_true(value: str) -> None:
    assert is_uniprot_accession(value)


@pytest.mark.parametrize(
    "value",
    [
        # Gene symbols 6-10 chars that the previous broad regex misclassified
        "ATP6AP1",
        "ATP6V1H",
        "CCDC47",
        "CACUL1",
        "TRAPPC12",
        "SERPINH1",
        "COLGALT1",
        # Short symbols
        "SPNS1",
        "CAMLG",
        "TP53",
    ],
)
def test_is_uniprot_accession_false_for_gene_symbols(value: str) -> None:
    assert not is_uniprot_accession(value)


def test_extract_uniprot_fields_parses_family_and_domains() -> None:
    uniprot_text = (
        "ID   SPNS1_HUMAN             Reviewed;         528 AA.\n"
        "AC   Q9H2V7;\n"
        "DE   RecName: Full=Protein spinster homolog 1;\n"
        "GN   Name=SPNS1; Synonyms=HSPIN1;\n"
        "OS   Homo sapiens (Human).\n"
        "OX   NCBI_TaxID=9606;\n"
        "CC   -!- FUNCTION: Lysosomal lysophospholipid transporter. {ECO:0000269|PubMed:36161949}\n"
        "CC   -!- SUBCELLULAR LOCATION: Lysosome membrane.\n"
        "CC   -!- SIMILARITY: Belongs to the major facilitator superfamily.\n"
        "CC       Spinster (TC 2.A.1.49) family.\n"
        "DR   Pfam; PF07690; MFS_1; 1.\n"
    )
    fields = extract_uniprot_fields(uniprot_text, "Q9H2V7")
    assert fields["protein_name"] == "Protein spinster homolog 1"
    assert fields["gene_name"] == "SPNS1"
    assert "major facilitator superfamily" in fields["protein_family"]
    assert fields["protein_domains"] == "MFS_1"
    # Evidence codes stripped from function text
    assert "{ECO:" not in fields["function"]
