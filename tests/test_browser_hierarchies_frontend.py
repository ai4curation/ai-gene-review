"""Exercise hierarchical filtering in a real browser, including multiple parents."""

import json
from pathlib import Path

import pytest
from playwright.sync_api import expect, sync_playwright

from ai_gene_review.tools.build_browser_hierarchies import append_hierarchies

pytestmark = pytest.mark.integration
BROWSER = Path(__file__).parents[1] / "src/ai_gene_review/browser/index.html"


@pytest.fixture
def page():
    """Use Chromium against local static files."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def hierarchy_page(tmp_path):
    """One annotation reaches the root by two routes; another is on a sibling."""
    rows = [
        {"gene": "A", "term_id": "detail", "species": "human"},
        {"gene": "B", "term_id": "detail", "species": "yeast"},
        {"gene": "C", "term_id": "other", "species": "human"},
        {"gene": "D", "term_id": "unknown", "species": "human"},
    ]
    schema = {
        "title": "Facets",
        "syncUrl": True,
        "quietMissingFields": True,
        "searchableFields": ["gene"],
        "defaultView": "table",
        "facets": [{"field": "species", "label": "Species", "type": "string"}],
        "displayFields": [{"field": "gene", "label": "Gene", "type": "string"}],
    }
    facet = {
        "field": "go_slim",
        "sourceField": "term_id",
        "type": "hierarchy",
        "label": "GO slim",
        "nodes": {
            "root": {"label": "All processes", "parents": []},
            "a": {"label": "Branch A", "parents": ["root"]},
            "b": {"label": "Branch B", "parents": ["root"]},
            "leaf": {"label": "Shared child", "parents": ["a", "b"]},
            "unmapped": {"label": "Unmapped", "parents": []},
        },
        "memberships": {
            "detail": ["root", "a", "b", "leaf"],
            "other": ["root", "b"],
            "unknown": ["unmapped"],
        },
    }
    (tmp_path / "index.html").write_text(BROWSER.read_text())
    (tmp_path / "data.js").write_text("window.searchData = " + json.dumps(rows) + ";")
    (tmp_path / "schema.js").write_text(
        "window.searchSchema = " + json.dumps(schema) + ";"
    )
    append_hierarchies(tmp_path / "schema.js", [facet], {})
    return (tmp_path / "index.html").as_uri()


def test_diamond_selection_counts_and_url(page, hierarchy_page):
    page.goto(hierarchy_page)
    expect(page.locator('.facet-item[data-value="root"] .facet-count')).to_have_text(
        "3"
    )
    page.get_by_role("button", name="Expand All processes", exact=True).click()
    page.get_by_role("button", name="Expand Branch A", exact=True).click()
    page.get_by_role("button", name="Expand Branch B", exact=True).click()
    copies = page.locator('.facet-item[data-value="leaf"] input')
    expect(copies).to_have_count(2)
    copies.first.check()
    expect(copies.nth(0)).to_be_checked()
    expect(copies.nth(1)).to_be_checked()
    expect(page.locator("#resultsCount")).to_contain_text("2")
    # Sibling counts ignore this facet's selection; they remain navigable.
    expect(page.locator('.facet-item[data-value="b"] .facet-count')).to_have_text("3")
    page.locator('.facet-item[data-filter="species"][data-value="human"]').click()
    expect(page.locator('.facet-item[data-value="root"] .facet-count')).to_have_text(
        "2"
    )
    expect(page.locator("#activeFilters")).to_contain_text("Shared child")
    assert "go_slim=leaf" in page.url
    page.reload()
    expect(page.locator("#activeFilters")).to_contain_text("Shared child")
    expect(page.locator("#resultsCount")).to_contain_text("1")
    page.get_by_role("button", name="Remove GO slim filter").click()
    expect(page.locator("#resultsCount")).to_contain_text("3")


def test_search_modes_or_selection_and_export(page, hierarchy_page):
    page.goto(hierarchy_page)
    search = page.get_by_role("searchbox", name="Search GO slim categories")
    search.fill("Shared")
    expect(page.locator('.facet-item[data-value="leaf"]')).to_have_count(2)
    expect(search).to_be_focused()
    page.locator('.facet-item[data-value="leaf"] input').first.check()
    search.fill("")
    page.get_by_role("button", name="Most used", exact=True).click()
    expect(page.locator('.facet-item[data-value="leaf"]')).to_have_count(1)
    page.locator('.facet-item[data-value="b"] input').check()
    expect(page.locator("#resultsCount")).to_contain_text("3")
    with page.expect_download() as info:
        page.locator("#exportTsv").click()
    exported = Path(info.value.path()).read_text()
    assert "A" in exported and "C" in exported and "D" not in exported
    page.locator("#clearFilters").click()
    expect(page.locator("#resultsCount")).to_contain_text("4")
    page.go_back()
    expect(page.locator("#resultsCount")).to_contain_text("3")


def test_hierarchy_search_escapes_text_and_mobile_fits(page, hierarchy_page):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(hierarchy_page)
    search = page.get_by_role("searchbox", name="Search GO slim categories")
    search.fill('<img src=x onerror="window.bad=1">')
    expect(page.locator(".hierarchy-body")).to_contain_text("No matching categories")
    assert page.evaluate("window.bad") is None
    assert page.evaluate("document.documentElement.scrollWidth") == 390


def test_focus_stays_on_second_parent_path(page, hierarchy_page):
    page.goto(hierarchy_page)
    page.get_by_role("button", name="Expand All processes", exact=True).click()
    page.get_by_role("button", name="Expand Branch A", exact=True).click()
    page.get_by_role("button", name="Expand Branch B", exact=True).click()
    copies = page.locator('.facet-item[data-value="leaf"] input')
    copies.nth(1).focus()
    copies.nth(1).press("Space")
    expect(copies.nth(1)).to_be_focused()
    expect(copies.nth(0)).to_be_checked()
    expect(copies.nth(1)).to_be_checked()


def test_category_search_has_no_inert_collapse_buttons(page, hierarchy_page):
    page.goto(hierarchy_page)
    page.get_by_role("searchbox", name="Search GO slim categories").fill("Shared")
    expect(page.locator('.facet-item[data-value="leaf"]')).to_have_count(2)
    expect(page.locator("[data-hierarchy-expand]")).to_have_count(0)
    page.get_by_role("searchbox", name="Search GO slim categories").fill("")
    page.get_by_role("button", name="Expand All processes", exact=True).click()
    expect(page.locator('.facet-item[data-value="a"]')).to_have_count(1)


def test_unmapped_new_data_and_default_source_field(page, hierarchy_page, tmp_path):
    """Stale hierarchy metadata cannot hide new source values from the facet."""
    schema = tmp_path / "schema.js"
    with schema.open("a") as stream:
        stream.write("""
            const facet = window.searchSchema.hierarchies.facets[0];
            facet.field = 'term_id';
            delete facet.sourceField;
            delete facet.memberships.unknown;
            delete facet.nodes.unmapped;
        """)
    page.goto(hierarchy_page)
    expect(page.locator('.facet-item[data-value="root"] .facet-count')).to_have_text(
        "3"
    )
    expect(
        page.locator('.facet-item[data-value="unmapped"] .facet-count')
    ).to_have_text("1")
    page.locator('.facet-item[data-value="unmapped"] input').check()
    expect(page.locator("#resultsCount")).to_have_text("Showing 1 of 1 items")
    expect(page.locator("#resultsGrid")).to_contain_text("D")
    page.reload()
    expect(page.locator("#resultsCount")).to_have_text("Showing 1 of 1 items")
