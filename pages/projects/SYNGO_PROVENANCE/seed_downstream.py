"""Count the annotations derived from each SynGO seed of one GO term.

For a GO term (default GO:0099507), fetch every annotation to that exact term
from QuickGO, then attribute each non-SynGO annotation to the SynGO seed(s)
named in its WITH/FROM (the UniProtKB accessions of the source gene products:
Ensembl orthology projection GO_REF:0000107, RGD/GO_Central ISO, UniProt rows).
Annotations whose WITH/FROM names no UniProtKB accession (for example UniProt
ARBA rules) are counted separately as ``rule_only``.

Seeds come from ``data/term_audit/<GO>-rows.yaml`` (written by
``term_audit_rows.py``). Output: ``data/term_audit/<GO>-downstream.yaml``,
one record per seed gene product, sorted by downstream count.

    python projects/SYNGO_PROVENANCE/seed_downstream.py GO:0099507
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
DATA = ROOT / "projects/SYNGO_PROVENANCE/data/term_audit"
API = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def fetch(go_id: str) -> tuple[str, list[dict]]:
    """Return the query URL and every QuickGO annotation to exactly ``go_id``."""
    url = f"{API}?{urllib.parse.urlencode({'goId': go_id, 'goUsage': 'exact', 'limit': 100})}"
    rows, page = [], 1
    while True:
        req = urllib.request.Request(f"{url}&page={page}", headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
        rows += data.get("results", [])
        if page >= data.get("pageInfo", {}).get("total", 1):
            return url, rows
        page += 1


def seed_accessions(go_id: str) -> dict[str, dict]:
    """Map each SynGO seed accession to its symbol, taxon and references."""
    doc = yaml.safe_load((DATA / f"{go_id.replace(':', '_')}-rows.yaml").read_text())
    seeds: dict[str, dict] = {}
    for paper in doc["by_reference"]:
        for ann in paper["annotations"]:
            acc = ann["gene_product"].split(":", 1)[1]
            rec = seeds.setdefault(acc, {"symbol": ann["symbol"], "taxon": ann["taxon"], "references": []})
            rec["references"].append(paper["reference"])
    return seeds


def main() -> None:
    go_id = sys.argv[1] if len(sys.argv) > 1 else "GO:0099507"
    url, rows = fetch(go_id)
    seeds = seed_accessions(go_id)
    per_seed: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    taxa: dict[str, set] = collections.defaultdict(set)
    rule_only = collections.Counter()
    unmatched = collections.Counter()
    syngo_rows = 0
    for r in rows:
        if r.get("assignedBy") == "SynGO":
            syngo_rows += 1
            continue
        accs = {x["id"] for g in r.get("withFrom") or [] for x in g["connectedXrefs"] if x["db"] == "UniProtKB"}
        source = f"{r.get('assignedBy')} {r.get('goEvidence')} {r.get('reference')}"
        if not accs:
            rule_only[source] += 1
        for acc in accs:
            if acc in seeds:
                per_seed[acc][source] += 1
                taxa[acc].add(r.get("taxonId"))
            else:
                unmatched[acc] += 1
    records = [
        {"gene_product": f"UniProtKB:{acc}", **seeds[acc], "downstream_rows": sum(per_seed[acc].values()),
         "downstream_taxa": len(taxa[acc]), "by_source": dict(per_seed[acc].most_common())}
        for acc in seeds
    ]
    records.sort(key=lambda x: (-x["downstream_rows"], x["symbol"]))
    doc = {"go_id": go_id, "query": url, "retrieved": datetime.date.today().isoformat(),
           "all_rows": len(rows), "syngo_rows": syngo_rows,
           "derived_rows_naming_a_seed": sum(sum(c.values()) for c in per_seed.values()),
           "rule_only_rows": dict(rule_only.most_common()),
           "rows_naming_a_non_seed_accession": dict(unmatched.most_common()),
           "seeds": records}
    accounted = doc["syngo_rows"] + doc["derived_rows_naming_a_seed"] + sum(rule_only.values())
    assert accounted == doc["all_rows"], f"rows do not reconcile: {accounted} attributed, {doc['all_rows']} fetched"
    out = DATA / f"{go_id.replace(':', '_')}-downstream.yaml"
    with out.open("w") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, width=120)
    for rec in records:
        print(rec["downstream_rows"], rec["symbol"], rec["taxon"], rec["gene_product"], sep="\t")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
