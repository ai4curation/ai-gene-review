#!/usr/bin/env python3
"""Test script to fetch and inspect PaperBlast HTML structure."""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def fetch_paperblast_html(uniprot_id: str, output_file: str = None):
    """Fetch PaperBlast HTML for inspection.

    Args:
        uniprot_id: UniProt accession
        output_file: Optional file to save HTML to
    """
    url = f"https://papers.genomics.lbl.gov/cgi-bin/litSearch.cgi?query={uniprot_id}&Search=Search"

    print(f"Fetching: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print("Loading page...")
        page.goto(url, timeout=60000, wait_until="networkidle")

        # Wait a bit for any dynamic content
        page.wait_for_timeout(5000)

        content = page.content()

        # Take a screenshot for debugging
        screenshot_path = f"{uniprot_id}_paperblast.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

        browser.close()

        if output_file:
            Path(output_file).write_text(content, encoding="utf-8")
            print(f"HTML saved to: {output_file}")
        else:
            # Print first 2000 chars to inspect structure
            print("\n" + "="*80)
            print("HTML PREVIEW (first 2000 chars):")
            print("="*80)
            print(content[:2000])
            print("\n" + "="*80)

            # Look for key elements
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content, "html.parser")

            print("\nTABLES found:", len(soup.find_all("table")))
            print("DIVs found:", len(soup.find_all("div")))
            print("LINKs found:", len(soup.find_all("a")))

            # Look for PMIDs
            import re
            pmids = re.findall(r'PMID[:\s]*(\d{7,})', content)
            print(f"\nPMIDs found: {len(set(pmids))}")
            if pmids:
                print(f"Sample PMIDs: {list(set(pmids))[:5]}")

        return content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_paperblast.py <uniprot_id> [output.html]")
        sys.exit(1)

    uniprot_id = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    fetch_paperblast_html(uniprot_id, output_file)
