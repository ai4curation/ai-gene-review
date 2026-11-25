"""Test whether BHF-UCL's RCA matrisome annotations are a category-to-term mapping.

Hypothesis (from projects/OMICS_EVIDENCE/rca.md, Pattern 1): BHF-UCL's RCA molecular-function
rows from ECM proteomics papers do not reflect protein-by-protein judgement of what the
protein does in the matrix. They reflect the protein's *category* in the Naba in-silico
matrisome (Collagens / Proteoglycans / ECM Glycoproteins), mapped to one GO term per
category, and the proteomics paper only decides which proteins are in scope.

Test: join every BHF-UCL RCA row (from data/rca_goa_all.tsv, produced by
rca_source_catalog.py) to the human matrisome masterlist by upper-cased gene symbol, and
cross-tabulate GO term x matrisome category. A category-driven mapping predicts a
near-diagonal table. Mouse and pig symbols are upper-cased to match human symbols, which
is exact for almost all matrisome genes; unmatched symbols are listed, not dropped.

Input: the Naba lab's human matrisome masterlist (Google Sheet linked from
https://sites.google.com/uic.edu/matrisome/matrisome-annotations/homo-sapiens), cached
as data/matrisome_hs_masterlist.tsv.

Usage:  python3 projects/OMICS_EVIDENCE/rca/rca_matrisome_crosswalk.py [--refresh]
"""

from __future__ import annotations

import argparse
import csv
import io
import os
import sys
import urllib.request
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
GOA_TSV = os.path.join(DATA, "rca_goa_all.tsv")
MASTERLIST = os.path.join(DATA, "matrisome_hs_masterlist.tsv")
SHEET_ID = "1GwwV3pFvsp7DKBbCgr8kLpf8Eh_xV8ks"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=xlsx"

TERMS = {
    "GO:0030020": "ECM structural constituent conferring tensile strength",
    "GO:0030021": "ECM structural constituent conferring compression resistance",
    "GO:0030023": "ECM constituent conferring elasticity",
    "GO:0005201": "ECM structural constituent",
}


def load_masterlist(refresh: bool) -> dict[str, tuple[str, str]]:
    if refresh or not os.path.exists(MASTERLIST):
        import openpyxl  # only needed for the download

        with urllib.request.urlopen(SHEET_URL, timeout=120) as resp:
            wb = openpyxl.load_workbook(io.BytesIO(resp.read()), read_only=True)
        rows = list(wb.worksheets[0].iter_rows(values_only=True))
        start = next(i for i, r in enumerate(rows) if r and r[0] == "Matrisome Division")
        with open(MASTERLIST, "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(["division", "category", "symbol", "name"])
            for r in rows[start + 1 :]:
                if r and r[2]:
                    w.writerow([r[0], r[1], r[2], r[3]])
    out = {}
    with open(MASTERLIST, newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            out[r["symbol"].upper()] = (r["division"], r["category"])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    if not os.path.exists(GOA_TSV):
        print("run rca_source_catalog.py first (needs data/rca_goa_all.tsv)", file=sys.stderr)
        return 2
    mat = load_masterlist(args.refresh)
    print(f"matrisome masterlist: {len(mat)} human genes")

    # distinct (gene symbol, term) pairs; rows repeat per paper and species
    pairs: set[tuple[str, str]] = set()
    rows = 0
    with open(GOA_TSV, newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["ASSIGNED BY"] == "BHF-UCL":
                rows += 1
                pairs.add((r["SYMBOL"].upper(), r["GO TERM"]))
    print(f"BHF-UCL RCA rows: {rows}; distinct symbol x term pairs: {len(pairs)}\n")

    table: dict[str, Counter] = defaultdict(Counter)
    off_diag: list[str] = []
    expected = {
        "Collagens": "GO:0030020",
        "Proteoglycans": "GO:0030021",
        "ECM Glycoproteins": "GO:0005201",
    }
    for sym, term in sorted(pairs):
        div, cat = mat.get(sym, ("not in masterlist", "not in masterlist"))
        table[term][cat] += 1
        if expected.get(cat) != term:
            off_diag.append(f"  {sym:10s} {term} ({TERMS.get(term, '?')})  matrisome: {div} / {cat}")

    cats = sorted({c for t in table.values() for c in t})
    print("## GO term x matrisome category (distinct symbol x term pairs)")
    print("  " + " | ".join(["term".ljust(11)] + [c[:18].ljust(18) for c in cats]))
    for term in TERMS:
        print("  " + " | ".join([term.ljust(11)] + [str(table[term][c]).ljust(18) for c in cats]))
    diag = sum(table[t][c] for c, t in expected.items())
    print(f"\non the category->term diagonal: {diag}/{len(pairs)} ({100 * diag / len(pairs):.1f}%)")
    print("\n## Off-diagonal pairs (term not predicted by matrisome category)")
    print("\n".join(off_diag))

    # what the category mapping would assert that our gene reviews have rejected
    print("\n## Core-matrisome categories of the genes the BHF-UCL rows cover")
    covered = Counter(mat.get(s, ("", "not in masterlist"))[1] for s in {s for s, _ in pairs})
    for k, v in covered.most_common():
        print(f"  {v:4d}  {k}")

    # How did this repository's gene reviews dispose of these rows, per category?
    reviewed = os.path.join(DATA, "rca_reviewed_rows.yaml")
    if os.path.exists(reviewed):
        import yaml

        rows_rev = yaml.safe_load(open(reviewed)) or []
        by_cat: dict[str, Counter] = defaultdict(Counter)
        genes_by_cat: dict[str, dict[str, Counter]] = defaultdict(lambda: defaultdict(Counter))
        for r in rows_rev:
            if r.get("cluster") != "BHF-UCL matrisome proteomics":
                continue
            cat = mat.get(r["gene"].upper(), ("", "not in masterlist"))[1]
            by_cat[cat][r["action"]] += 1
            genes_by_cat[cat][r["gene"]][r["action"]] += 1
        print("\n## Reviewed BHF-UCL matrisome rows (rca_reviewed_rows.yaml): category x action")
        for cat, c in sorted(by_cat.items()):
            n = sum(c.values())
            print(f"  {cat}: {n} rows, ACCEPT={c['ACCEPT']} ({100 * c['ACCEPT'] / n:.0f}%); "
                  + ", ".join(f"{k}={v}" for k, v in c.most_common() if k != "ACCEPT"))
            for g, gc in sorted(genes_by_cat[cat].items()):
                print(f"      {g:8s} " + ", ".join(f"{k}={v}" for k, v in gc.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
