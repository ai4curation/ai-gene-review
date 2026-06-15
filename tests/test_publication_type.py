"""Tests for ai_gene_review.etl.publication_type classification."""

import pytest

from ai_gene_review.etl.publication_type import (
    classify_pubmed_publication_type,
    classify_reference_id,
    parse_medline_publication_types,
    publication_type_for_reference,
)


@pytest.mark.parametrize(
    "pt_list,expected",
    [
        (["Journal Article"], "PRIMARY_RESEARCH"),
        (["Journal Article", "Research Support, N.I.H., Extramural"], "PRIMARY_RESEARCH"),
        (["Journal Article", "Review"], "REVIEW"),
        (["Review"], "REVIEW"),
        (["Review", "Systematic Review"], "SYSTEMATIC_REVIEW"),
        (["Journal Article", "Meta-Analysis", "Review"], "META_ANALYSIS"),
        (["Editorial"], "COMMENT_EDITORIAL"),
        (["Comment"], "COMMENT_EDITORIAL"),
        (["Letter"], "COMMENT_EDITORIAL"),
        (["Case Reports", "Journal Article"], "CASE_REPORT"),
        (["Preprint"], "PREPRINT"),
        (["Dataset"], "OTHER"),
        ([], "UNKNOWN"),
        (["", "  "], "UNKNOWN"),
    ],
)
def test_classify_pubmed_publication_type(pt_list, expected):
    assert classify_pubmed_publication_type(pt_list) == expected


def test_specific_review_type_wins_over_order():
    # Meta-analysis must win even if listed after Review/Journal Article.
    assert (
        classify_pubmed_publication_type(["Journal Article", "Review", "Meta-Analysis"])
        == "META_ANALYSIS"
    )


@pytest.mark.parametrize(
    "ref_id,expected",
    [
        ("PMID:12345", None),
        ("pmid:12345", None),
        ("GO_REF:0000043", "DATABASE"),
        ("Reactome:R-HSA-123", "DATABASE"),
        ("UniProtKB:P12345", "DATABASE"),
        ("file:human/TP53/TP53-deep-research-openai.md", "DEEP_RESEARCH"),
        ("file:human/TP53/TP53-bioinformatics/RESULTS.md", "BIOINFORMATICS"),
        ("file:human/TP53/TP53-notes.md", "BIOINFORMATICS"),
        ("DOI:10.1/x", "OTHER"),
    ],
)
def test_classify_reference_id(ref_id, expected):
    assert classify_reference_id(ref_id) == expected


def test_publication_type_for_reference_pmid_lookup():
    types = {"1": ["Journal Article", "Review"], "2": ["Journal Article"]}
    assert publication_type_for_reference("PMID:1", types) == "REVIEW"
    assert publication_type_for_reference("PMID:2", types) == "PRIMARY_RESEARCH"
    # Missing PMID -> UNKNOWN
    assert publication_type_for_reference("PMID:3", types) == "UNKNOWN"
    # Non-PMID resolved without needing the map
    assert publication_type_for_reference("GO_REF:1", types) == "DATABASE"


def test_parse_medline_publication_types():
    txt = (
        "PMID- 100\n"
        "TI  - A title\n"
        "PT  - Journal Article\n"
        "PT  - Review\n"
        "\n"
        "PMID- 200\n"
        "PT  - Editorial\n"
    )
    parsed = parse_medline_publication_types(txt)
    assert parsed == {"100": ["Journal Article", "Review"], "200": ["Editorial"]}


def test_enum_values_match_schema():
    """Every value produced by classification must be a valid PublicationTypeEnum."""
    from pathlib import Path

    from linkml_runtime.utils.schemaview import SchemaView

    schema = (
        Path(__file__).parent.parent
        / "src/ai_gene_review/schema/gene_review.yaml"
    )
    sv = SchemaView(str(schema))
    valid = set(sv.get_enum("PublicationTypeEnum").permissible_values)
    produced = {
        classify_pubmed_publication_type(["Review"]),
        classify_pubmed_publication_type([]),
        classify_pubmed_publication_type(["Dataset"]),
        classify_reference_id("GO_REF:1"),
        classify_reference_id("file:x-deep-research-openai.md"),
        classify_reference_id("file:x-bioinformatics/RESULTS.md"),
        classify_reference_id("DOI:1"),
    }
    assert produced <= valid
