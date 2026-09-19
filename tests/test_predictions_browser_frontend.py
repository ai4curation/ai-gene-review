"""Exercise the shared predictions browser in Chromium with local JS payloads."""

from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

import pytest
from playwright.sync_api import expect, sync_playwright

from ai_gene_review.tools.build_prediction_browser import encode_prediction_data_js

pytestmark = pytest.mark.integration
BROWSER = Path(__file__).parents[1] / "src/ai_gene_review/browser"


@pytest.fixture
def page():
    """Open a real browser; no network service or mocked browser API is needed."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def prediction_page(tmp_path: Path) -> str:
    """Write term, empty, narrative and superseded review records."""
    shared = {
        "source_method": "ProtNLM2", "source_version": "2026 snapshot",
        "species": "DROME", "taxon_label": "Drosophila melanogaster",
        "projects": ["PROTNLM_EVALUATION"], "cohorts": ["FLY41"],
        "output_type": "GO terms", "output_state": "GO/EC predictions present",
        "review_state": "Complete", "document_status": "COMPLETE",
        "representation": "standard", "assessment_scheme": "VDCL",
        "assessment_categories": ["CNN"], "claim_count": 1,
        "summary": "Evidence supports the prediction.", "source_file": "review.yaml",
        "source_link": "../../genes/test/review.yaml", "raw_link": "../../genes/test/source.json",
        "review_link": "../../genes/test/review.html", "default_visible": True,
        "quality_notes": [],
    }
    sets = [
        {**shared, "set_id": "empty", "gene_symbol": "Lcp3", "protein_id": "P1",
         "output_state": "No GO/EC predictions", "claim_count": 0, "source_version": "",
         "assessment_categories": [], "summary": 'Missing cuticle function <img src=x onerror="window.bad=1">'},
        {**shared, "set_id": "current", "gene_symbol": "Lip", "protein_id": "P2",
         "claims_link": "?dataset=claims&set_id=current"},
        {**shared, "set_id": "older", "gene_symbol": "Lip-old", "protein_id": "P2",
         "default_visible": False, "superseded_by": "current", "representation": "full",
         "source_version": "Previous <snapshot>", "quality_notes": ["Superseded by leaf review."]},
        {**shared, "set_id": "narrative", "gene_symbol": "Narr", "protein_id": "P3",
         "source_method": "BioReason", "output_type": "Functional summary", "claim_count": None,
         "assessment_scheme": "Narrative", "assessment_categories": [], "correctness": 4,
         "completeness": 2, "input_quality": "Wrong input sequence", "input_protein_id": "WRONG1",
         "reference_protein_id": "P3", "performance_included": False, "metadata_status": "Conflicting",
         "prediction_summary": "Model predicts secreted receptor activity."},
    ]
    claims = [
        {**sets[1], "claim_id": "current-1", "term_id": "GO:0016298", "term_label": "lipase activity",
         "term_type": "GO_MF", "assessment": "CNN", "review_score": 2, "error_type": "",
         "evidence": "Direct assay", "set_link": "?dataset=sets&set_id=current"},
    ]
    (tmp_path / "data.js").write_text(encode_prediction_data_js({"sets": sets, "claims": claims, "metadata": {}}))
    (tmp_path / "index.html").write_text((BROWSER / "index.html").read_text())
    schema = BROWSER / "predictions_schema.js"
    (tmp_path / "schema.js").write_text(schema.read_text() if schema.exists() else "")
    return (tmp_path / "index.html").as_uri()


def test_prediction_sets_include_empty_summaries_and_safe_source_links(page, prediction_page):
    """Empty output remains visible without creating a claim or assessment score."""
    page.goto(prediction_page)
    expect(page.locator("#appTitle")).to_have_text("Prediction Review Browser")
    expect(page.locator("#resultsCount")).to_contain_text("3 of 3 prediction sets")
    expect(page.locator("#datasetTabs")).to_contain_text("Prediction sets (4)")
    expect(page.locator("#datasetTabs")).to_contain_text("Claims (1)")
    expect(page.locator("#activeFilters")).to_contain_text("Current representation")
    expect(page.locator('a[href="../index.html"]')).to_have_text("Gene annotations")
    page.locator('[data-view="card"]').click()
    cards = page.locator(".result-card")
    expect(cards).to_have_count(3)
    empty = cards.filter(has_text="Lcp3")
    expect(empty).to_contain_text("No GO/EC predictions")
    expect(empty).to_contain_text('<img src=x onerror="window.bad=1">')
    expect(empty).not_to_contain_text("Review score")
    expect(empty).not_to_contain_text("Quality notes")
    expect(empty).not_to_contain_text("Recorded assessment categories")
    expect(empty.locator("img")).to_have_count(0)
    assert page.evaluate("window.bad") is None
    expect(empty.locator('a[href="../../genes/test/review.yaml"]')).to_have_count(1)
    narrative = cards.filter(has_text="Narrative correctness")
    expect(narrative).to_contain_text("Model functional summary")
    expect(narrative).to_contain_text("Model predicts secreted receptor activity.")
    expect(narrative).to_contain_text("WRONG1")
    expect(narrative).to_contain_text("false")
    expect(narrative).not_to_contain_text("Emitted term claims")
    expect(narrative).not_to_contain_text("Review score")


def test_prediction_url_filters_tabs_and_browser_history(page, prediction_page):
    """Repeated facets, text and view survive sharing, tabs and back/forward."""
    page.goto(prediction_page + "?species=DROME&source_method=ProtNLM2&source_method=Other&projects=PROTNLM_EVALUATION")
    expect(page.locator("#resultsCount")).to_contain_text("2 of 2")
    page.locator("#searchBox").fill("Lip")
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")
    assert parse_qs(urlsplit(page.url).query)["q"] == ["Lip"]
    page.locator('[data-view="card"]').click()
    expect(page.locator(".result-card")).to_have_count(1)
    claims_tab = page.locator('#datasetTabs a[data-dataset="claims"]')
    params = parse_qs(urlsplit(claims_tab.get_attribute("href")).query)
    assert params["source_method"] == ["ProtNLM2", "Other"]
    assert params["q"] == ["Lip"]
    claims_tab.click()
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1 claims")
    expect(page.locator(".result-card")).to_contain_text("lipase activity")
    expect(page.locator(".result-card")).to_contain_text("Review score")
    page.go_back()
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1 prediction sets")
    page.locator("#clearFilters").click()
    expect(page.locator("#resultsCount")).to_contain_text("4 of 4")
    page.go_back()
    expect(page.locator("#searchBox")).to_have_value("Lip")
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")
    page.go_forward()
    expect(page.locator("#resultsCount")).to_contain_text("4 of 4")
    page.reload()
    expect(page.locator("#resultsCount")).to_contain_text("4 of 4")


def test_facets_and_removable_filters_update_shared_url(page, prediction_page):
    """Sidebar selections are reflected in the URL and removable active chips."""
    page.goto(prediction_page)
    page.locator('.facet-item[data-filter="output_state"][data-value="No GO/EC predictions"]').click()
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")
    assert parse_qs(urlsplit(page.url).query)["output_state"] == ["No GO/EC predictions"]
    page.get_by_role("button", name="Remove Output state filter").click()
    expect(page.locator("#resultsCount")).to_contain_text("3 of 3")
    assert "output_state" not in parse_qs(urlsplit(page.url).query)
    page.reload()
    expect(page.locator("#resultsCount")).to_contain_text("3 of 3")


def test_mobile_starts_with_results_and_expandable_filters(page, prediction_page):
    """Small screens should not require scrolling past the full facet inventory."""
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(prediction_page + "?q=Lcp3&view=card")
    expect(page.locator("#facetsPanel")).to_have_class("sidebar collapsed")
    expect(page.locator("#toggleFacets")).to_have_text("Show")
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")
    assert page.evaluate("document.documentElement.scrollWidth") == 390
    page.locator("#toggleFacets").click()
    expect(page.locator("#facetsPanel")).to_have_class("sidebar")


def test_narrative_dimensions_filter_and_export_without_claim_scores(page, prediction_page):
    """Narrative evaluation and input identity remain distinct from term scores."""
    page.goto(prediction_page + "?correctness.min=4&correctness.max=5&performance_included=false")
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")
    with page.expect_download() as download_info:
        page.locator("#exportTsv").click()
    text = Path(download_info.value.path()).read_text()
    assert "Input protein accession" in text
    assert "Model functional summary" in text
    assert "WRONG1" in text
    assert "Review score" not in text


def test_blank_source_version_filter_survives_reload(page, prediction_page):
    """The original blank value can be filtered without inventing a version."""
    page.goto(prediction_page)
    option = page.locator('.facet-item[data-filter="source_version"][data-value=""]')
    expect(option).to_contain_text("Not recorded")
    option.click()
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")
    assert parse_qs(urlsplit(page.url).query, keep_blank_values=True)["source_version"] == [""]
    page.reload()
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")


def test_direct_set_link_can_show_superseded_record(page, prediction_page):
    """An explicit set identity bypasses the default current-representation filter."""
    page.goto(prediction_page + "?set_id=older&view=card")
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1")
    expect(page.locator(".result-card")).to_contain_text("Lip-old")
    expect(page.locator(".result-card")).to_contain_text("Superseded by leaf review.")
    expect(page.locator(".result-card")).to_contain_text("full")
    expect(page.locator("#activeFilters")).to_contain_text("older")
    assert "default_visible" not in parse_qs(urlsplit(page.url).query)
    page.goto(prediction_page + "?dataset=claims&set_id=empty")
    expect(page.locator("#resultsCount")).to_contain_text("0 of 0 claims")
    expect(page.locator(".no-results")).to_be_visible()


def test_generic_browser_keeps_url_behavior_opt_in(page, tmp_path: Path):
    """Existing browser schemas without syncUrl ignore query state as before."""
    (tmp_path / "index.html").write_text((BROWSER / "index.html").read_text())
    (tmp_path / "data.js").write_text('window.searchData=[{name:"alpha"},{name:"beta"}];')
    (tmp_path / "schema.js").write_text('window.searchSchema={searchableFields:["name"], facets:[], displayFields:[{field:"name",label:"Name"}]};')
    page.goto((tmp_path / "index.html").as_uri() + "?q=beta")
    expect(page.locator("#resultsCount")).to_contain_text("2 of 2 items")
    page.locator("#searchBox").fill("alpha")
    expect(page.locator("#resultsCount")).to_contain_text("1 of 1 items")
    assert urlsplit(page.url).query == "q=beta"


def test_empty_claim_dataset_is_a_valid_browser_view(page, tmp_path: Path):
    """A valid empty claim list is not a loading or format error."""
    (tmp_path / "index.html").write_text((BROWSER / "index.html").read_text())
    (tmp_path / "data.js").write_text(encode_prediction_data_js({"sets": [], "claims": [], "metadata": {}}))
    (tmp_path / "schema.js").write_text((BROWSER / "predictions_schema.js").read_text())
    page.goto((tmp_path / "index.html").as_uri() + "?dataset=claims")
    expect(page.locator("#resultsCount")).to_have_text("Showing 0 of 0 claims")
    expect(page.locator("#datasetTabs")).to_contain_text("Claims (0)")
    expect(page.locator(".no-results")).to_be_visible()


def test_claim_table_distinguishes_seeded_and_reviewed_unc(page, prediction_page):
    """An identical UNC value must not hide whether its claim has been reviewed."""
    data_path = Path(unquote(urlsplit(prediction_page).path)).with_name("data.js")
    page.goto(prediction_page)
    data = page.evaluate("window.predictionData")
    claim = data["claims"][0]
    data["claims"] = [
        {**claim, "claim_id": "awaiting-1", "assessment": "UNC", "review_score": 1,
         "review_state": "Awaiting review"},
        {**claim, "claim_id": "reviewed-1", "assessment": "UNC", "review_score": 1,
         "review_state": "Reviewed"},
    ]
    data_path.write_text(encode_prediction_data_js(data))
    page.goto(prediction_page + "?dataset=claims")
    rows = page.locator(".results-table tbody tr")
    expect(rows).to_have_count(2)
    for state in ["Awaiting review", "Reviewed"]:
        row = rows.filter(has_text=state)
        expect(row).to_have_count(1)
        expect(row.locator(".table-cell-assessment")).to_contain_text("UNC")
        expect(row.locator(".table-cell-review_score")).to_have_text("1")
