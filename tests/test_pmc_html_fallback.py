"""Regression tests for PMC HTML full-text extraction."""

from ai_gene_review.etl.publication import (
    _classify_pmc_html_content,
    _extract_pmc_article_text,
)


def test_current_pmc_body_wins_over_legacy_section_fragment():
    """Extract all nested sections from PMC's current article-body markup."""
    fragment = "Misleading legacy fragment. " * 180
    methods = "The complete methods cite PMID: 12345 within the assay text. " * 35
    results = "The complete results report DOI: 10.1/example within the finding. " * 35
    discussion = "The discussion interprets the complete experiment. " * 35
    html = f"""
    <html><body>
      <div class="tsec"><h2>Results</h2><p>{fragment}</p></div>
      <main id="main-content"><article>
        <section aria-label="Article content">
          <section class="body main-article-body">
            <section><h2 class="pmc_sec_title">MATERIALS AND METHODS</h2>
              <section><h3 class="pmc_sec_title">Microscopy.</h3><p>{methods}</p></section>
            </section>
            <section><h2 class="pmc_sec_title">RESULTS</h2>
              <section><h3 class="pmc_sec_title">Rad3 localization.</h3><p>{results}</p></section>
            </section>
            <figure><figcaption><p>Excluded figure caption.</p></figcaption></figure>
            <section><h2 class="pmc_sec_title">DISCUSSION</h2><p>{discussion}</p></section>
          </section>
        </section>
      </article></main>
    </body></html>
    """
    content = _extract_pmc_article_text(html)
    result = _classify_pmc_html_content(content)

    assert result is not None
    assert result.is_complete is True
    assert result.extraction_method == "html"
    assert "MATERIALS AND METHODS" in result.content
    assert "Rad3 localization." in result.content
    assert "PMID: 12345" in result.content
    assert "DOI: 10.1/example" in result.content
    assert "Misleading legacy fragment" not in result.content
    assert "Excluded figure caption" not in result.content


def test_legacy_tsec_only_page_is_still_extracted():
    body = "Legacy PMC body paragraph with experimental findings. " * 80
    html = f"""
    <div class="tsec">
      <h2>Introduction</h2><p>{body}</p>
      <h2>Results</h2><p>{body}</p>
    </div>
    """

    content = _extract_pmc_article_text(html)
    result = _classify_pmc_html_content(content)

    assert result is not None
    assert result.is_complete is True
    assert "Introduction" in result.content
    assert "Results" in result.content


def test_abstract_only_content_is_not_marked_complete():
    abstract = "This abstract reports one concise experimental finding. " * 20
    html = f"<article><h2>Abstract</h2><p>{abstract}</p></article>"

    content = _extract_pmc_article_text(html)
    result = _classify_pmc_html_content(content)

    assert result is not None
    assert result.is_complete is False
    assert result.extraction_method == "html_abstract_only"


def test_headings_without_body_text_do_not_inflate_content():
    furniture = "".join(f"<h2>Navigation heading {index}</h2>" for index in range(200))

    content = _extract_pmc_article_text(f"<article>{furniture}</article>")

    assert content is None
