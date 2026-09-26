"""Section navigation reflects the content actually rendered on a gene page."""

from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from ai_gene_review.render import enrich_gene_data, render_html


TEMPLATE = (
    Path(__file__).parents[1] / "src/ai_gene_review/templates/gene_review.html.j2"
)


def test_navigation_counts_and_targets() -> None:
    """Count predictions across reports and link to distinct rendered sections."""
    prediction = {
        "predicted_term": {"id": "GO:0031012", "label": "extracellular matrix"}
    }
    data = enrich_gene_data(
        {
            "gene_symbol": "TEST",
            "existing_annotations": [{"term": {"id": "GO:0005615"}}] * 3,
            "core_functions": [{"description": "Core function"}],
            "references": [{"id": "PMID:1", "title": "Reference"}],
            "deep_research_sections": [
                {"title": "Report", "content": '<h2 id="references">References</h2>'}
            ]
            * 2,
            "markdown_sections": [{"title": "Notes", "content": "Notes"}],
            "prediction_reviews": [
                {"title": "Method A", "review": {"predictions": [prediction] * 2}},
                {"title": "Method B", "review": {"predictions": [prediction]}},
            ],
        }
    )
    soup = BeautifulSoup(render_html(data, TEMPLATE), "html.parser")
    nav = soup.select_one('nav[aria-label="Page sections"]')
    assert nav is not None
    links = {link["href"]: link.get_text(" ", strip=True) for link in nav.select("a")}
    assert links == {
        "#review-annotations": "3 Annotations",
        "#review-research": "2 Research",
        "#external-predictions": "3 External",
        "#review-core-functions": "1 Core Function",
        "#review-references": "1 References",
        "#review-documentation": "1 Documents",
        "#review-raw-yaml": "Raw YAML",
    }
    for target in links:
        assert isinstance(target, str)
        assert len(soup.select(target)) == 1
    assert len(soup.select("#review-annotations .annotations-table tbody tr")) == 3
    assert len(soup.select("#external-predictions .prediction-card")) == 3
    header = soup.select_one(".header")
    assert header is not None
    assert header.find_next_sibling() == nav


@pytest.mark.parametrize("value", [None, []])
def test_navigation_omits_empty_sections(value: object) -> None:
    """Sparse pages have no dead links or zero-count boxes."""
    data = enrich_gene_data({"gene_symbol": "TEST"})
    for key in [
        "existing_annotations",
        "core_functions",
        "prediction_reviews",
        "references",
        "deep_research_sections",
        "markdown_sections",
    ]:
        data[key] = value
    soup = BeautifulSoup(render_html(data, TEMPLATE), "html.parser")
    nav = soup.select_one('nav[aria-label="Page sections"]')
    assert nav is not None
    assert [a["href"] for a in nav.select("a")] == ["#review-raw-yaml"]
    assert soup.select_one("#review-raw-yaml details")


def test_navigation_includes_additional_review_sections() -> None:
    """Optional review sections have working anchors too."""
    data = enrich_gene_data(
        {
            "gene_symbol": "TEST",
            "functional_isoforms": [
                {"id": "test", "name": "Isoform", "type": "SPLICE_VARIANT"}
            ],
            "proposed_new_terms": [{"proposed_name": "Proposed term"}],
            "suggested_questions": [{"question": "Question"}],
            "suggested_experiments": [{"description": "Experiment"}],
            "tags": ["tag"],
        }
    )
    soup = BeautifulSoup(render_html(data, TEMPLATE), "html.parser")
    targets = {a["href"] for a in soup.select('nav[aria-label="Page sections"] a')}
    assert targets == {
        "#review-isoforms",
        "#review-proposed-terms",
        "#review-questions",
        "#review-experiments",
        "#review-raw-yaml",
    }
    for target in targets:
        assert isinstance(target, str)
        assert len(soup.select(target)) == 1
