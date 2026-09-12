#!/usr/bin/env python3
"""Reference-projection test: for each reference AFF3's GOA rows rest on, ask how
many DISTINCT gene products and which terms that reference annotates across all of GOA.

Two questions, not one (campaign brief):
  1. how many entities does the reference annotate?  (a complex-plus-every-subunit
     pattern is a projection, not N independent findings)
  2. does the functional/phenotype term spread across the set, or stay on the
     perturbed gene?

An ANNOTATION count is not an ENTITY count -- entities are derived as a distinct set
of gene-product ids. Pagination is asserted, never assumed: if the service clamps
instead of erroring, ``numberOfHits > len(results)`` catches it and the test reports
itself as unreliable rather than quoting one page.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/reference_projection.py
"""

from __future__ import annotations

import json
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
UA = {"User-Agent": "ai-gene-review/AFF3 (cjmungall@lbl.gov)"}
SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

REFS = [
    ("PMID:20444755", "sole support for the GO:0034612 response-to-TNF IMP"),
    ("PMID:18616733", "sole support for the GO:0035116 embryonic hindlimb morphogenesis IMP"),
    ("PMID:8555498", "sole support for the GO:0005634 nucleus IDA"),
    ("PMID:22547686", "the SEC-L3 isolation paper; seeds AFF1's GO:0006354 EXP"),
]
PAGE = 200  # QuickGO's documented max for this endpoint


def fetch_all(ref: str) -> tuple[list[dict], int, bool]:
    """Return (results, numberOfHits, complete). Never infer a total from a constant."""
    url = f"{SEARCH}?reference={urllib.parse.quote(ref)}&limit={PAGE}&page=1"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as fh:
        d = json.load(fh)
    total = d.get("numberOfHits", 0)
    results = list(d.get("results", []))
    page = 2
    # Compare against len(results), not against PAGE: a service that CLAMPS rather
    # than errors would sail past a constant-based guard.
    while len(results) < total:
        url = f"{SEARCH}?reference={urllib.parse.quote(ref)}&limit={PAGE}&page={page}"
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=90) as fh:
            d2 = json.load(fh)
        got = d2.get("results") or []
        if not got:
            return results, total, False  # cannot complete -> say so
        results.extend(got)
        page += 1
        if page > 60:
            return results, total, False
    return results, total, True


def main() -> None:
    out = []
    for ref, why in REFS:
        results, total, complete = fetch_all(ref)
        entities = {r["geneProductId"] for r in results}
        by_term: dict[str, set[str]] = defaultdict(set)
        for r in results:
            by_term[f"{r['goId']} [{r['goEvidence']}]"].add(r["geneProductId"])
        print(f"== {ref}")
        print(f"   {why}")
        print(f"   annotations: {total}   retrieved: {len(results)}   "
              f"complete: {complete}")
        if not complete:
            print("   !! pagination incomplete -- entity counts UNAVAILABLE, "
                  "projection test unreliable for this reference")
        else:
            print(f"   distinct gene products: {len(entities)}  -> {sorted(entities)}")
            for k in sorted(by_term):
                print(f"      {k}: {len(by_term[k])} entities  {sorted(by_term[k])}")
        print()
        out.append({
            "reference": ref, "why": why, "n_annotations": total,
            "n_retrieved": len(results), "pagination_complete": complete,
            "n_entities": len(entities) if complete else None,
            "entities": sorted(entities) if complete else None,
            "terms": {k: sorted(v) for k, v in by_term.items()} if complete else None,
        })
    (HERE / "reference_projection.json").write_text(json.dumps(out, indent=2))
    print(f"wrote {HERE / 'reference_projection.json'}")


if __name__ == "__main__":
    main()
