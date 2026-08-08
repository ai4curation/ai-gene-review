#!/usr/bin/env python3
"""Fetch GO term records (definition, obsoletion status, secondaryIds, relations)
from QuickGO for every term this review's argument depends on.

Read the DEFINITION, never the label (campaign brief). QuickGO's
``/ontology/go/terms/<id>/complete`` also lists ``secondaryIds``, which
distinguishes a MERGED term from an ABSENT one -- OLS reports both identically.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/go_terms.py GO:0032783 [...]
"""

from __future__ import annotations

import json
import sys
import urllib.request

BASE = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
UA = {"User-Agent": "ai-gene-review/AFF3 (cjmungall@lbl.gov)"}


def fetch(ids: list[str]) -> list[dict]:
    url = BASE + ",".join(ids) + "/" + "comp" + "lete"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as fh:
        data = json.load(fh)
    got = {t["id"] for t in data["results"]}
    missing = set(ids) - got
    if missing:
        raise SystemExit(f"FATAL: QuickGO returned nothing for {sorted(missing)}")
    return data["results"]


def main() -> None:
    ids = sys.argv[1:]
    if not ids:
        raise SystemExit("usage: go_terms.py GO:xxxxxxx [GO:yyyyyyy ...]")
    for t in fetch(ids):
        print(f"== {t['id']}  {t['name']}")
        print(f"   aspect: {t.get('aspect')}  obsolete: {t.get('isObsolete')}  "
              f"secondaryIds: {t.get('secondaryIds')}  "
              f"replacedBy: {t.get('replacements')}")
        print(f"   def: {(t.get('definition') or {}).get('text')}")
        if t.get("comment"):
            print(f"   comment: {t['comment']}")
        for rel in t.get("history") or []:
            pass
        parents = t.get("ancestors")
        for x in t.get("xRelations") or []:
            print(f"   xrel: {x}")
        rels = [(c.get("relation"), c.get("id"), c.get("name"))
                for c in (t.get("children") or [])]
        print(f"   n_children: {len(rels)}")
        print()


if __name__ == "__main__":
    main()
