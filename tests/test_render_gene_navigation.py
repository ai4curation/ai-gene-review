"""Section navigation reflects the content actually rendered on a gene page."""

from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from ai_gene_review.render import enrich_gene_data, render_html


TEMPLATE = (
    Path(__file__).parents[1] / "src/ai_gene_review/templates/gene_review.html.j2"
)


GENE_MODEL_ISSUE = {
    "issue_type": "FUSED_GENE_MODEL",
    "status": "CONFIRMED",
    "description": "Joins two neighbouring genes; named after the first part.",
    "components": [
        {"accession": "A0A2T0ACV7", "segment": "1-650", "description": "Part one"},
        {"accession": "A0A2T0ACW0", "segment": "645-1419", "description": "Part two"},
    ],
    "reviewed_segment": "645-1419",
    "evidence_types": ["TILING", "GENETIC_SEPARATION"],
    "supported_by": [
        {"reference_id": "file:TEST/TEST/RESULTS.md", "supporting_text": "tiled by two genes"}
    ],
}


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
            "gene_model_issues": [GENE_MODEL_ISSUE],
        }
    )
    soup = BeautifulSoup(render_html(data, TEMPLATE), "html.parser")
    targets = {a["href"] for a in soup.select('nav[aria-label="Page sections"] a')}
    assert targets == {
        "#review-gene-model",
        "#review-isoforms",
        "#review-proposed-terms",
        "#review-questions",
        "#review-experiments",
        "#review-raw-yaml",
    }
    for target in targets:
        assert isinstance(target, str)
        assert len(soup.select(target)) == 1


def test_gene_model_issues_section_renders_all_fields() -> None:
    """The gene model section shows type, status, evidence, segments and quotes."""
    data = enrich_gene_data(
        {"gene_symbol": "TEST", "gene_model_issues": [GENE_MODEL_ISSUE]}
    )
    soup = BeautifulSoup(render_html(data, TEMPLATE), "html.parser")
    nav = soup.select_one('nav[aria-label="Page sections"] a[href="#review-gene-model"]')
    assert nav is not None
    assert nav.get_text(" ", strip=True) == "1 Gene Model"
    section = soup.select_one("#review-gene-model")
    assert section is not None
    badges = [b.get_text(strip=True) for b in section.select(".badge")]
    assert badges == ["FUSED GENE MODEL", "CONFIRMED", "TILING", "GENETIC SEPARATION"]
    text = section.get_text(" ", strip=True)
    assert "Joins two neighbouring genes" in text
    assert "residues 645-1419" in text
    components = [li.get_text(" ", strip=True) for li in section.select("ul")[0].select("li")]
    assert components == [
        "residues 1-650 A0A2T0ACV7 : Part one",
        "residues 645-1419 A0A2T0ACW0 : Part two",
    ]
    assert '"tiled by two genes"' in text
    assert "file:TEST/TEST/RESULTS.md" in text


def test_gene_model_issue_source_without_quote_renders_no_empty_quotes() -> None:
    """A supported_by entry with only a reference shows the reference, not ``""``."""
    issue = {
        **GENE_MODEL_ISSUE,
        "supported_by": [{"reference_id": "file:TEST/TEST/RESULTS.md"}],
    }
    data = enrich_gene_data({"gene_symbol": "TEST", "gene_model_issues": [issue]})
    soup = BeautifulSoup(render_html(data, TEMPLATE), "html.parser")
    section = soup.select_one("#review-gene-model")
    assert section is not None
    quotes = section.select("ul")[1].select("li")
    assert [li.get_text(" ", strip=True) for li in quotes] == ["file:TEST/TEST/RESULTS.md"]
    assert '""' not in section.get_text()
