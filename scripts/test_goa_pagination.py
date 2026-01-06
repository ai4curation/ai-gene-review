#!/usr/bin/env python3
import requests

def test_goa_pagination(uniprot_id):
    """Test GOA pagination to see if we're getting all results"""
    url = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

    all_results = []
    page = 1
    limit = 200

    while True:
        params = [
            ("geneProductId", uniprot_id),
            ("includeFields", "goName"),
            ("includeFields", "taxonName"),
            ("includeFields", "name"),
            ("limit", str(limit)),
        ]

        if page > 1:
            params.append(("page", str(page)))

        headers = {"Accept": "application/json"}

        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        results = data.get("results", [])

        print(f"Page {page}:")
        print(f"  numberOfHits: {data.get('numberOfHits', 0)}")
        print(f"  pageInfo.total: {data.get('pageInfo', {}).get('total', 0)}")
        print(f"  pageInfo.current: {data.get('pageInfo', {}).get('current', 0)}")
        print(f"  pageInfo.totalPages: {data.get('pageInfo', {}).get('totalPages', 0)}")
        print(f"  len(results): {len(results)}")
        print(f"  total so far: {len(all_results) + len(results)}")

        if not results:
            print("  No results, stopping")
            break

        all_results.extend(results)

        page_info = data.get("pageInfo", {})
        total = page_info.get("total", 0)
        total_pages = page_info.get("totalPages", 0)

        # Check various stopping conditions
        print(f"  Checking: len(all_results)={len(all_results)} >= total={total}? {len(all_results) >= total}")
        print(f"  Checking: len(results)={len(results)} < limit={limit}? {len(results) < limit}")
        print(f"  Checking: page={page} >= totalPages={total_pages}? {page >= total_pages}")

        # The current buggy condition
        if len(all_results) >= total or len(results) < limit:
            print(f"  Current logic says STOP (have {len(all_results)} of {total})")
            break

        page += 1

    print(f"\nTotal annotations collected: {len(all_results)}")
    return all_results

# Test with TP53 which likely has many annotations
print("Testing TP53 (P04637):")
results = test_goa_pagination("P04637")