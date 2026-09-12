#!/usr/bin/env python3
"""Search GO by label via QuickGO (the OLS MCP was unavailable in this session:
its venv's certifi bundle had been pruned from the uv cache).

An empty search is NOT evidence a term is absent -- confirm any load-bearing
absence with ``go_terms.py`` on a specific id (campaign brief).

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/go_search.py "nuclear speck"
"""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

URL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search"
UA = {"User-Agent": "ai-gene-review/AFF3 (cjmungall@lbl.gov)"}


def search(q: str, limit: int = 25) -> list[dict]:
    url = f"{URL}?query={urllib.parse.quote(q)}&limit={limit}&page=1"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as fh:
        d = json.load(fh)
    return d.get("results", [])


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit('usage: go_search.py "<query>"')
    for q in sys.argv[1:]:
        print(f"### {q}")
        hits = search(q)
        if not hits:
            print("   (no hits -- an empty search is NOT proof of absence)")
        for h in hits:
            print(f"   {h['id']}  {h.get('name')}  [{h.get('aspect')}]"
                  + ("  OBSOLETE" if h.get("isObsolete") else ""))
        print()


if __name__ == "__main__":
    main()
