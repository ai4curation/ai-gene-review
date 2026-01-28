#!/usr/bin/env python3
from __future__ import annotations

import os

import requests

try:
    import pytest
except ImportError:  # pragma: no cover - used only when pytest isn't installed
    pytest = None

if pytest is not None:
    pytestmark = pytest.mark.integration

def goa_fetch(uniprot_id: str):
    url = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

    all_results = []
    page = 1
    limit = 400

    while True:
        params = [
            ("geneProductId", uniprot_id),
            ("includeFields", "goName"),
            ("includeFields", "taxonName"),
            ("includeFields", "name"),
            ("limit", str(limit)),
            ("page", str(page)),
        ]

        headers = {"Accept": "application/json"}

        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        results = data.get("results", [])

        print(f"Page {page}:")
        print(f"  numberOfHits: {data.get('numberOfHits', 0)}")
        print(f"  pageInfo.total: {data.get('pageInfo', {}).get('total', 0)}")
        print(f"  pageInfo.current: {data.get('pageInfo', {}).get('current', 0)}")
        print(f"  len(results): {len(results)}")

        if not results:
            print("  No results, stopping")
            break

        all_results.extend(results)

        page_info = data.get("pageInfo", {})
        total = page_info.get("total", 0)

        if len(all_results) >= total or len(results) < limit:
            print(f"  Stopping: have {len(all_results)} of {total}")
            break

        page += 1

    print(f"\nTotal annotations collected: {len(all_results)}")
    return all_results

def test_goa_fetch_smoke():
    if pytest is None:
        raise RuntimeError("pytest is required to run integration tests")
    if os.environ.get("AI_GENE_REVIEW_INTEGRATION") != "1":
        pytest.skip("Set AI_GENE_REVIEW_INTEGRATION=1 to run QuickGO tests.")
    goa_fetch("P38398")


if __name__ == "__main__":
    goa_fetch("P38398")
