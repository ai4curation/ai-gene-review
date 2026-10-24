"""Compare public expression records for a zebrafish paralog pair.

Usage (from repo root):
    uv run python genes/DANRE/tmc2a/tmc2a-bioinformatics/expression_compare.py tmc2a tmc2b

Sources (fetched live; nothing hardcoded):
  - ZFIN wild-type expression download
    (https://zfin.org/downloads/wildtype-expression_fish.txt): curated anatomy
    terms, stage, assay and ZFIN publication for each gene.
  - Bgee REST API (gene expression calls, all data types, anatomical entity and
    cell type conditions) using the Ensembl gene id from the Ensembl REST API.

For each source the script prints per-gene records and the anatomy terms that
are shared or specific to one copy. Absence from a curated resource is not
evidence of absence of expression; it often reflects which copy was assayed.
"""

import csv
import io
import json
import sys
import urllib.request
from collections import defaultdict

ZFIN_URL = "https://zfin.org/downloads/wildtype-expression_fish.txt"


def fetch(url: str) -> bytes:
    # Bgee rejects the default Python user agent (HTTP 403)
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review-expression-compare"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def ensembl_id(symbol: str) -> str:
    url = f"https://rest.ensembl.org/lookup/symbol/danio_rerio/{symbol}?content-type=application/json"
    return json.loads(fetch(url))["id"]


def zfin_records(symbols):
    text = fetch(ZFIN_URL).decode("utf-8", errors="replace")
    recs = defaultdict(list)
    for row in csv.reader(io.StringIO(text), delimiter="\t"):
        if len(row) > 11 and row[1] in symbols:
            anat = row[4] + (f" > {row[6]}" if row[6] else "")
            recs[row[1]].append((anat, row[7], row[9], row[11]))
    return recs


def bgee_calls(ens: str):
    url = (
        "https://www.bgee.org/api/?page=gene&action=expression"
        f"&gene_id={ens}&species_id=7955&display_type=json"
        "&cond_param=anat_entity&cond_param=cell_type"
    )
    d = json.loads(fetch(url))["data"]
    out = []
    for c in d.get("calls", []):
        cond = c["condition"]
        anat = cond.get("anatEntity", {}).get("name", "")
        cell = cond.get("cellType", {}).get("name", "")
        name = anat + (f" > {cell}" if cell and cell != "cell" else "")
        out.append((name, float(c["expressionScore"]["expressionScore"]), c["expressionState"], ",".join(c.get("dataTypesWithData", []))))
    return out


def main():
    a, b = sys.argv[1], sys.argv[2]
    print(f"# Public expression records: {a} / {b}\n")
    print("## ZFIN wild-type expression (curated)\n")
    z = zfin_records({a, b})
    for g in (a, b):
        print(f"### {g} ({len(z[g])} records)\n")
        print("| Anatomy | Stage (start) | Assay | ZFIN publication |")
        print("|---|---|---|---|")
        for r in sorted(set(z[g])):
            print("| " + " | ".join(r) + " |")
        print()
    za = {r[0] for r in z[a]}
    zb = {r[0] for r in z[b]}
    print(f"- Shared ZFIN anatomy terms: {', '.join(sorted(za & zb)) or 'none'}")
    print(f"- {a} only: {', '.join(sorted(za - zb)) or 'none'}")
    print(f"- {b} only: {', '.join(sorted(zb - za)) or 'none'}\n")

    print("## Bgee expression calls (all data types)\n")
    calls = {g: bgee_calls(ensembl_id(g)) for g in (a, b)}
    for g in (a, b):
        print(f"### {g} ({len(calls[g])} calls)\n")
        print("| Condition | Expression score | State | Data types |")
        print("|---|---|---|---|")
        for name, score, state, dt in sorted(calls[g], key=lambda x: -x[1]):
            print(f"| {name} | {score:.2f} | {state} | {dt} |")
        print()
    ba = {c[0] for c in calls[a] if c[2] == "expressed"}
    bb = {c[0] for c in calls[b] if c[2] == "expressed"}
    print(f"- Shared Bgee conditions: {', '.join(sorted(ba & bb)) or 'none'}")
    print(f"- {a} only: {', '.join(sorted(ba - bb)) or 'none'}")
    print(f"- {b} only: {', '.join(sorted(bb - ba)) or 'none'}")


if __name__ == "__main__":
    main()
