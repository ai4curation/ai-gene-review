#!/usr/bin/env python3
import requests

def test_goa_fetch(uniprot_id):
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

# Test with BRCA1
results = test_goa_fetch("P38398")