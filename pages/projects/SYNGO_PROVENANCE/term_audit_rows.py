"""List every SynGO annotation to one GO term, grouped by cited paper.

Queries the QuickGO annotation API (exact term, assigned by SynGO) and writes
``data/term_audit/<GO_ID>-rows.yaml``: the query URL, retrieval date, and one
entry per reference with the annotated gene products, taxa and evidence codes.
This is the work list for a per-paper audit; verdicts live in a separate,
hand-curated file.

    python projects/SYNGO_PROVENANCE/term_audit_rows.py GO:0099507
"""
from __future__ import annotations

import collections
import datetime
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
API = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def fetch(go_id: str, assigned_by: str) -> tuple[str, list[dict]]:
    params = {"goId": go_id, "goUsage": "exact", "assignedBy": assigned_by, "limit": 100}
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
    go_id = sys.argv[1] if len(sys.argv) > 1 else "GO:0099507"
    url, rows = fetch(go_id, "SynGO")
    by_ref: dict = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in rows:
        key = (r.get("geneProductId"), r.get("symbol"), r.get("taxonId"), r.get("qualifier"))
        by_ref[r.get("reference")][key].add(r.get("goEvidence"))
    papers = []
    for ref in sorted(by_ref):
        prods = [{"gene_product": gp, "symbol": sym, "taxon": tax, "qualifier": q, "evidence": sorted(ev)}
                 for (gp, sym, tax, q), ev in sorted(by_ref[ref].items(), key=lambda kv: tuple(str(x) for x in kv[0]))]
        papers.append({"reference": ref, "annotations": prods})
    out = ROOT / "projects/SYNGO_PROVENANCE/data/term_audit" / f"{go_id.replace(':', '_')}-rows.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = {"go_id": go_id, "assigned_by": "SynGO", "query": url, "retrieved": datetime.date.today().isoformat(),
           "rows": len(rows), "papers": len(papers), "claims": sum(len(p["annotations"]) for p in papers),
           "by_reference": papers}
    with out.open("w") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, width=120)
    print(f"{go_id}: {len(rows)} rows, {doc['claims']} gene-product claims, {len(papers)} papers -> {out.relative_to(ROOT)}")
    for p in papers:
        print(p["reference"], "; ".join(f"{a['symbol']}({a['taxon']})" for a in p["annotations"]))


if __name__ == "__main__":
    main()
