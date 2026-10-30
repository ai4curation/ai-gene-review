"""Tests for the gene descriptions ETL module."""

import pytest
from pathlib import Path

from ai_gene_review.etl.descriptions import (
    extract_uniprot_function,
    extract_uniprot_xref,
    extract_uniprot_id,
    GeneDescriptions,
    SourceDescription,
    DescriptionReview,
    DescriptionReviewRubric,
    Finding,
    save_gene_descriptions,
    load_gene_descriptions,
    _clean_dict,
)


SAMPLE_UNIPROT = """ID   CACP_YEAST              Reviewed;         670 AA.
AC   P32796; D6VZD3;
DT   01-OCT-1993, integrated into UniProtKB/Swiss-Prot.
CC   -!- FUNCTION: Carnitine acetylase is specific for short chain fatty acids.
CC       Carnitine acetylase seems to affect the flux through the pyruvate
CC       dehydrogenase complex. It may be involved as well in the transport of
CC       acetyl-CoA into mitochondria. {ECO:0000269|PubMed:8420957}.
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(R)-carnitine + acetyl-CoA = O-acetyl-(R)-carnitine + CoA;
DR   SGD; S000004506; CAT2.
DR   GeneID; 854965; -.
DR   HGNC; 28188; CFAP300.
"""


class TestUniProtParsing:
    def test_extract_function(self):
        result = extract_uniprot_function(SAMPLE_UNIPROT)
        assert result is not None
        assert "Carnitine acetylase" in result
        assert "short chain fatty acids" in result
        assert "ECO:" not in result  # evidence codes stripped

    def test_extract_function_missing(self):
        assert extract_uniprot_function("ID   TEST\nAC   Q12345;\n") is None

    def test_extract_xref_sgd(self):
        assert extract_uniprot_xref(SAMPLE_UNIPROT, "SGD") == "S000004506"

    def test_extract_xref_geneid(self):
        assert extract_uniprot_xref(SAMPLE_UNIPROT, "GeneID") == "854965"

    def test_extract_xref_hgnc(self):
        assert extract_uniprot_xref(SAMPLE_UNIPROT, "HGNC") == "28188"

    def test_extract_xref_missing(self):
        assert extract_uniprot_xref(SAMPLE_UNIPROT, "PDB") is None

    def test_extract_uniprot_id(self):
        assert extract_uniprot_id(SAMPLE_UNIPROT) == "P32796"


class TestDataModel:
    def test_gene_descriptions_basic(self):
        gd = GeneDescriptions(gene_symbol="CAT2", organism="yeast")
        assert gd.gene_symbol == "CAT2"
        assert gd.descriptions == []
        assert gd.findings == []

    def test_source_description(self):
        sd = SourceDescription(source="UniProt", text="A function", source_type="curated")
        assert sd.source == "UniProt"

    def test_review_rubrics(self):
        review = DescriptionReview(
            reviewer="AI",
            rubrics=[
                DescriptionReviewRubric(rubric="correctness", score=4, notes="Good"),
                DescriptionReviewRubric(rubric="completeness", score=3),
            ],
        )
        assert len(review.rubrics) == 2
        assert review.rubrics[0].score == 4

    def test_finding(self):
        f = Finding(category="consensus", text="Both sources agree on transferase activity")
        assert f.category == "consensus"


class TestSerialization:
    def test_roundtrip(self, tmp_path: Path):
        gd = GeneDescriptions(
            gene_symbol="CAT2",
            organism="yeast",
            uniprot_id="P32796",
            taxon_id="NCBITaxon:559292",
            descriptions=[
                SourceDescription(
                    source="UniProt",
                    text="A carnitine transferase",
                    source_type="curated",
                    url="https://uniprot.org/P32796",
                    source_id="P32796",
                    review=DescriptionReview(
                        reviewer="AI",
                        rubrics=[DescriptionReviewRubric(rubric="correctness", score=4)],
                        overall_notes="Solid description",
                    ),
                ),
            ],
            findings=[
                Finding(category="consensus", text="All sources agree", sources=["UniProt", "Alliance_Imported"]),
            ],
            review=DescriptionReview(
                reviewer="AI",
                rubrics=[DescriptionReviewRubric(rubric="overall", score=4, notes="Good coverage")],
            ),
            fetch_date="2026-03-06",
        )

        path = tmp_path / "test-descriptions.yaml"
        save_gene_descriptions(gd, path)
        assert path.exists()

        loaded = load_gene_descriptions(path)
        assert loaded.gene_symbol == "CAT2"
        assert loaded.uniprot_id == "P32796"
        assert len(loaded.descriptions) == 1
        assert loaded.descriptions[0].source == "UniProt"
        assert loaded.descriptions[0].review is not None
        assert loaded.descriptions[0].review.rubrics[0].score == 4
        assert len(loaded.findings) == 1
        assert loaded.findings[0].sources == ["UniProt", "Alliance_Imported"]
        assert loaded.review is not None
        assert loaded.review.rubrics[0].notes == "Good coverage"

    def test_clean_dict(self):
        assert _clean_dict({"a": 1, "b": None, "c": []}) == {"a": 1}
        assert _clean_dict({"a": {"b": None, "c": 2}}) == {"a": {"c": 2}}


@pytest.mark.integration
class TestFetchIntegration:
    """Integration tests that hit external APIs. Run with: pytest -m integration"""

    def test_fetch_gene_descriptions_yeast(self):
        from ai_gene_review.etl.descriptions import fetch_gene_descriptions

        gd = fetch_gene_descriptions("yeast", "CAT2")
        assert gd.gene_symbol == "CAT2"
        assert gd.uniprot_id == "P32796"
        assert len(gd.descriptions) >= 2  # at least UniProt + Alliance curated
        sources = [d.source for d in gd.descriptions]
        assert "UniProt" in sources
        assert "Alliance_Imported" in sources


def _reviewed(text_a: str = "A text", text_b: str = "B text"):
    from ai_gene_review.etl.descriptions import (
        DescriptionReview, DescriptionReviewRubric, Finding, GeneDescriptions, SourceDescription,
    )

    def rv(score: int) -> DescriptionReview:
        return DescriptionReview(reviewer="AI", rubrics=[DescriptionReviewRubric(rubric="correctness", score=score)])

    return GeneDescriptions(
        gene_symbol="g", organism="worm",
        descriptions=[
            SourceDescription(source="UniProt", text=text_a, review=rv(4)),
            SourceDescription(source="Alliance_Imported", text=text_b, review=rv(2)),
        ],
        findings=[Finding(category="gap", text="x")],
        review=rv(3),
    )


def test_refetch_keeps_reviews_when_texts_unchanged(tmp_path):
    """Re-saving freshly fetched, unreviewed data keeps the existing reviews."""
    from ai_gene_review.etl.descriptions import (
        GeneDescriptions, SourceDescription, load_gene_descriptions,
        save_gene_descriptions, save_preserving_reviews,
    )
    path = tmp_path / "g-descriptions.yaml"
    save_gene_descriptions(_reviewed(), path)
    fresh = GeneDescriptions(gene_symbol="g", organism="worm", descriptions=[
        SourceDescription(source="UniProt", text="A text"),
        SourceDescription(source="Alliance_Imported", text="B text"),
    ])
    save_preserving_reviews(fresh, path)
    gd = load_gene_descriptions(path)
    assert [d.review.rubrics[0].score for d in gd.descriptions] == [4, 2]
    assert gd.review is not None and len(gd.findings) == 1
    assert gd.status == "COMPLETE"


def test_refetch_drops_reviews_of_changed_text(tmp_path):
    """A source whose text changed loses its stale review, and so does the cross-source review."""
    from ai_gene_review.etl.descriptions import (
        GeneDescriptions, SourceDescription, load_gene_descriptions,
        save_gene_descriptions, save_preserving_reviews,
    )
    path = tmp_path / "g-descriptions.yaml"
    save_gene_descriptions(_reviewed(), path)
    fresh = GeneDescriptions(gene_symbol="g", organism="worm", descriptions=[
        SourceDescription(source="UniProt", text="A text"),
        SourceDescription(source="Alliance_Imported", text="B text, revised"),
    ])
    save_preserving_reviews(fresh, path)
    gd = load_gene_descriptions(path)
    assert gd.descriptions[0].review is not None
    assert gd.descriptions[1].review is None
    assert gd.review is None and gd.findings == []
    assert gd.status == "IN_PROGRESS"
