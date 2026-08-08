#!/usr/bin/env python3
"""Locate a citable reference for ARFGAP1's catalytic arginine.

`arfgap_domain.py` uses ARFGAP1 Arg-50 as the positive control that validates its
motif-based derivation.  A control asserted from memory is not a control, so the
reference is looked up here and the result recorded.
"""

from __future__ import annotations

import json
import pathlib
import sys
import time
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import get_json  # noqa: E402

HERE = pathlib.Path(__file__).parent
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

TERMS = [
    'Mandiyan ArfGAP arginine 1999',
    '"catalytic arginine"[tiab] AND (ArfGAP1[tiab] OR "ARF GAP"[tiab])',
    'ArfGAP1[tiab] AND (Arg50[tiab] OR "R50"[tiab] OR "arginine 50"[tiab])',
    'Luo[au] AND Randazzo[au] AND ArfGAP1[tiab] AND arginine[tiab]',
    '"Consensus nomenclature for the human ArfGAP domain-containing proteins"[ti]',
    'Consensus nomenclature ArfGAP domain-containing proteins',
    'ASAP1[tiab] AND (R497[tiab] OR "arginine 497"[tiab])',
    'Schlacht Dacks Arf GAP subfamily opisthokont 2013',
    '(ArfGAP[tiab] OR "Arf GAP"[tiab]) AND "zinc finger"[tiab] AND arginine[tiab] AND (mutant[tiab] OR mutation[tiab])',
]


def esearch(term: str) -> dict:
    d = get_json(f"{E}/esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": term, "retmode": "json", "retmax": 10}))["esearchresult"]
    return {"count": int(d["count"]), "pmids": d.get("idlist", [])}


def esummary(pmids: list[str]) -> dict:
    if not pmids:
        return {}
    d = get_json(f"{E}/esummary.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "json"}))["result"]
    return {p: {"title": d[p].get("title"), "journal": d[p].get("fulljournalname"),
                "year": (d[p].get("pubdate") or "")[:4]} for p in d.get("uids", [])}


def main() -> None:
    out = {}
    for t in TERMS:
        r = esearch(t)
        r["titles"] = esummary(r["pmids"])
        out[t] = r
        time.sleep(0.4)
        print(f"\n=== {t}  ({r['count']} hits)")
        for p, v in r["titles"].items():
            print(f"  {p} ({v['year']}) {v['journal']} — {v['title']}")
    (HERE / "control_ref.json").write_text(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
