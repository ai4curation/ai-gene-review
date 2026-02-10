#!/usr/bin/env python3
"""Extract all unique proteins from GREEKC dbTF target set."""
import json
import urllib.request
import concurrent.futures
import sys

BASE_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
PARAMS = "targetSet=dbTF&taxonId=9606&geneProductType=protein&geneProductSubset=Swiss-Prot&limit=100"

def fetch_page(page):
    """Fetch a single page and return gene product IDs."""
    url = f"{BASE_URL}?{PARAMS}&page={page}"
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read())
            return [r.get("geneProductId", "") for r in data.get("results", [])]
    except Exception as e:
        print(f"Error on page {page}: {e}", file=sys.stderr)
        return []

def main():
    # Total pages needed: ~604 for 60391 annotations
    total_pages = 605
    all_proteins = set()

    print(f"Fetching {total_pages} pages with 20 parallel workers...", file=sys.stderr)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(fetch_page, p): p for p in range(1, total_pages + 1)}
        done = 0
        for future in concurrent.futures.as_completed(futures):
            proteins = future.result()
            all_proteins.update(p for p in proteins if p)
            done += 1
            if done % 50 == 0:
                print(f"Progress: {done}/{total_pages} pages, {len(all_proteins)} unique proteins", file=sys.stderr)

    print(f"Total unique proteins: {len(all_proteins)}", file=sys.stderr)

    # Output sorted proteins
    for p in sorted(all_proteins):
        print(p)

if __name__ == "__main__":
    main()
