"""Check NOT-qualified RCA annotations against positive annotations to the same location.

TAIR's proteomics-derived RCA rows are all NOT|located_in: proteins *absent* from a
fraction's robust protein set (PMID:21166475, cytosol) or called contaminants of a purified
organelle (PMID:22430844, Golgi). This script asks, for every such row, whether GOA
also holds a positive annotation for the same gene product to the same term or one of
its is_a/part_of descendants -- i.e. whether the negative inference is contradicted.

Predicates:
  * input: NOT-qualified rows of data/rca_goa_all.tsv (from rca_source_catalog.py)
  * contradiction: a non-NOT annotation of the same gene product to the NOT row's GO term
    or an is_a/part_of descendant, any evidence code (counted separately per code)
  * "experimental" contradiction: evidence in EXPERIMENTAL (incl. HTP codes)
  * a gene product counts once per (NOT row, evidence code), whatever its number of
    supporting rows

Output: data/rca_not_contradictions.tsv (one line per NOT row) and a summary on stdout.

Usage:  python3 projects/RCA_EVIDENCE/rca_not_contradictions.py [--refresh]
"""

from __future__ import annotations

import argparse
import csv
import io
import os
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
GOA_TSV = os.path.join(DATA, "rca_goa_all.tsv")
POSITIVES = os.path.join(DATA, "rca_not_positive_annotations.tsv")
OUT = os.path.join(DATA, "rca_not_contradictions.tsv")
DL = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def fetch_positives(not_rows: list[dict]) -> list[dict]:
    by_term: dict[str, set[str]] = defaultdict(set)
    for r in not_rows:
        by_term[r["GO TERM"]].add(f'{r["GENE PRODUCT DB"]}:{r["GENE PRODUCT ID"]}')
    out: list[dict] = []
    for term, gps in sorted(by_term.items()):
        gps_sorted = sorted(gps)
        for i in range(0, len(gps_sorted), 100):
            q = urllib.parse.urlencode(
                {
                    "geneProductId": ",".join(gps_sorted[i : i + 100]),
                    "goId": term,
                    "goUsage": "descendants",
                    "goUsageRelationships": "is_a,part_of",
                    "downloadLimit": 50000,
                    "selectedFields": "geneProductId,symbol,qualifier,goId,goEvidence,reference,assignedBy",
                }
            )
            req = urllib.request.Request(f"{DL}?{q}", headers={"Accept": "text/tsv"})
            with urllib.request.urlopen(req, timeout=300) as resp:
                text = resp.read().decode()
            for r in csv.DictReader(io.StringIO(text), delimiter="\t"):
                r["QUERY TERM"] = term
                out.append(r)
            time.sleep(0.3)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    with open(GOA_TSV, newline="") as fh:
        not_rows = [r for r in csv.DictReader(fh, delimiter="\t") if r["QUALIFIER"].startswith("NOT")]
    print(f"NOT-qualified RCA rows: {len(not_rows)}")

    if args.refresh or not os.path.exists(POSITIVES):
        pos = fetch_positives(not_rows)
        fields = list(pos[0].keys()) if pos else []
        with open(POSITIVES, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
            w.writeheader()
            w.writerows(pos)
    with open(POSITIVES, newline="") as fh:
        pos = [r for r in csv.DictReader(fh, delimiter="\t") if not r["QUALIFIER"].startswith("NOT")]

    support: dict[tuple[str, str], set[str]] = defaultdict(set)
    refs: dict[tuple[str, str], set[str]] = defaultdict(set)
    for r in pos:
        key = (r["GENE PRODUCT ID"], r["QUERY TERM"])
        support[key].add(r["GO EVIDENCE CODE"])
        refs[key].add(f'{r["GO EVIDENCE CODE"]}:{r["REFERENCE"]}')

    summary: dict[str, Counter] = defaultdict(Counter)
    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["gene_product", "symbol", "not_term", "rca_reference", "contradicted",
                    "experimental_contradiction", "positive_evidence_codes", "positive_references"])
        for r in not_rows:
            key = (r["GENE PRODUCT ID"], r["GO TERM"])
            codes = support.get(key, set())
            exp = bool(codes & EXPERIMENTAL)
            label = f'{r["REFERENCE"]} NOT {r["GO TERM"]}'
            summary[label]["rows"] += 1
            summary[label]["contradicted (any code)"] += bool(codes)
            summary[label]["contradicted (experimental/HTP)"] += exp
            summary[label]["contradicted (IDA/EXP only, low-throughput)"] += bool(codes & {"IDA", "EXP"})
            for c in codes:
                summary[label][f"  by {c}"] += 1
            w.writerow([r["GENE PRODUCT ID"], r["SYMBOL"], r["GO TERM"], r["REFERENCE"], bool(codes), exp,
                        ",".join(sorted(codes)), ";".join(sorted(refs.get(key, set())))])

    for label, c in summary.items():
        n = c["rows"]
        print(f"\n## {label}  ({n} rows)")
        for k in ["contradicted (any code)", "contradicted (experimental/HTP)",
                  "contradicted (IDA/EXP only, low-throughput)"]:
            print(f"  {c[k]:5d}  {100 * c[k] / n:5.1f}%  {k}")
        for k, v in sorted(((k, v) for k, v in c.items() if k.startswith("  by")), key=lambda kv: -kv[1]):
            print(f"  {v:5d}  {100 * v / n:5.1f}% {k}")

    # which references supply the positive HDA calls (another proteome, typically)
    hda = Counter(r["REFERENCE"] for r in pos if r["GO EVIDENCE CODE"] == "HDA")
    print("\n## references behind contradicting HDA rows (top 10)")
    for k, v in hda.most_common(10):
        print(f"  {v:5d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
