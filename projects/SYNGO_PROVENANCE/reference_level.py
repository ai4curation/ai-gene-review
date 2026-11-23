"""Reference-level view: every SynGO annotation QuickGO holds for one paper.

Used before recording a wrong-gene defect, to see how SynGO annotated the paper
as a whole (which genes got which terms). Queries the QuickGO annotation API
and writes a sorted table to ``data/reference_level/<PMID>.yaml``, with the
query URL and retrieval date, so the check can be re-run and diffed.

    python projects/SYNGO_PROVENANCE/reference_level.py PMID:19666514
"""
from __future__ import annotations

import datetime
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
API = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def fetch(reference: str, assigned_by: str) -> tuple[str, list[dict]]:
    params = {"reference": reference, "assignedBy": assigned_by, "limit": 100,
              "includeFields": "goName"}
    url = f"{API}?{urllib.parse.urlencode(params)}"
    rows, page = [], 1
    while True:
        req = urllib.request.Request(f"{url}&page={page}", headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
        rows += data.get("results", [])
        if page >= data.get("pageInfo", {}).get("total", 1):
            return url, rows
        page += 1


def main() -> None:
    reference = sys.argv[1] if len(sys.argv) > 1 else "PMID:19666514"
    assigned_by = sys.argv[2] if len(sys.argv) > 2 else "SynGO"
    url, rows = fetch(reference, assigned_by)
    table = sorted({(r.get("taxonId"), r.get("geneProductId"), r.get("symbol"), r.get("goId"), r.get("goName"),
                     r.get("qualifier"), r.get("goEvidence")) for r in rows},
                   key=lambda t: tuple(str(v) for v in t))
    out = ROOT / "projects/SYNGO_PROVENANCE/data/reference_level" / f"{reference.replace(':', '_')}.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = {
        "reference": reference,
        "assigned_by": assigned_by,
        "query": url,
        "retrieved": datetime.date.today().isoformat(),
        "annotations": [dict(zip(("taxon", "gene_product", "symbol", "go_id", "go_name", "qualifier", "evidence"), t))
                        for t in table],
    }
    with out.open("w") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, width=120)
    for a in doc["annotations"]:
        print(a["taxon"], a["symbol"], a["go_id"], a["go_name"], a["evidence"], sep="\t")
    print(f"wrote {out.relative_to(ROOT)} ({len(table)} rows)")


if __name__ == "__main__":
    main()
