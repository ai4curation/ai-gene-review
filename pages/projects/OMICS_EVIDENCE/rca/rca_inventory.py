"""Inventory every RCA (Inferred from Reviewed Computational Analysis) annotation in the corpus.

Every figure on projects/OMICS_EVIDENCE/rca.md comes from this script, so a reader can
re-derive them.

PREDICATES (stated once, applied to every figure):
  * a GOA row is RCA when column 9 (`GO EVIDENCE CODE`) is exactly "RCA". Matching
    `\\tRCA\\t` anywhere in the line is wrong: Arabidopsis RCA (Rubisco activase) is a
    gene SYMBOL and would contribute ~30 false rows.
  * a review row is RCA when `existing_annotations[].evidence_type == "RCA"`.
  * rows are counted as ANNOTATION ROWS (term x reference x with/from), not as distinct
    terms; duplicates in GOA (same term, same reference) are counted as GOA reports them.
  * a GOA RCA row is "covered" when the gene's review has an RCA row with the same
    GO term id and the same original_reference_id.

Usage:  python3 projects/OMICS_EVIDENCE/rca/rca_inventory.py [--yaml OUT.yaml] [--list]
"""

from __future__ import annotations

import argparse
import csv
import glob
import os
import sys
from collections import Counter, defaultdict

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


# Cluster = the computational analysis behind the row, keyed on its reference. Review rows
# carry no assigned_by, so the reference is the only join key that works on both sides.
MATRISOME_REFS = {
    "PMID:20551380", "PMID:23979707", "PMID:25037231", "PMID:27068509",
    "PMID:27559042", "PMID:28327460", "PMID:28675934",
}
CLUSTERS = {
    "PMID:30358795": "SGD zinc proteome",
    "GO_REF:0000123": "SGD YeastPathways import",
    "PMID:21166475": "TAIR proteome absence (NOT cytosol)",
    "PMID:12819136": "MGI mouse-human comparative genomics",
}


def cluster(ref: str | None, action: str | None = None) -> str:
    if action == "NEW":
        return "reviewer-authored NEW"
    if ref in MATRISOME_REFS:
        return "BHF-UCL matrisome proteomics"
    if ref in CLUSTERS:
        return CLUSTERS[ref]
    return "other (single-paper RCA)"


def goa_rows():
    """Yield (organism, gene_dir, row-dict) for every RCA row in a *-goa.tsv file."""
    for path in sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-goa.tsv"))):
        org = path.split(os.sep)[-3]
        gene = path.split(os.sep)[-2]
        with open(path, newline="") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            for row in reader:
                if (row.get("GO EVIDENCE CODE") or "").strip() == "RCA":
                    yield org, gene, row


def review_rows():
    """Yield (organism, gene_dir, annotation-dict) for every RCA existing annotation."""
    for path in sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-ai-review.yaml"))):
        org = path.split(os.sep)[-3]
        gene = path.split(os.sep)[-2]
        with open(path) as fh:
            text = fh.read()
        # cheap prefilter: fully parsing every review in the corpus takes minutes
        if "evidence_type: RCA" not in text:
            continue
        try:
            doc = yaml.load(text, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader)) or {}
        except yaml.YAMLError as exc:
            print(f"WARN: cannot parse {path}: {exc}", file=sys.stderr)
            continue
        for ann in doc.get("existing_annotations") or []:
            if ann.get("evidence_type") == "RCA":
                yield org, gene, ann


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--yaml", help="write per-row inventory to this YAML file")
    ap.add_argument("--list", action="store_true", help="print every reviewed row")
    args = ap.parse_args()

    goa = list(goa_rows())
    rev = list(review_rows())
    if not goa:
        print("ERROR: no RCA rows found in any GOA file", file=sys.stderr)
        return 2

    print(f"GOA RCA rows: {len(goa)} in {len({(o, g) for o, g, _ in goa})} gene folders")
    print(f"Reviewed RCA rows: {len(rev)} in {len({(o, g) for o, g, _ in rev})} gene folders\n")

    def table(title, counter):
        print(f"## {title}")
        for k, v in counter.most_common():
            print(f"  {v:4d}  {k}")
        print()

    table("GOA rows by assigned_by", Counter(r["ASSIGNED BY"] for _, _, r in goa))
    table("GOA rows by organism folder", Counter(o for o, _, _ in goa))
    table("GOA rows by aspect", Counter(r["GO ASPECT"] for _, _, r in goa))
    table("GOA rows by reference", Counter(r["REFERENCE"] for _, _, r in goa))
    table(
        "GOA rows by term",
        Counter(f'{r["GO TERM"]} {r["GO NAME"]}' for _, _, r in goa),
    )
    table(
        "GOA rows by assigned_by x term",
        Counter(f'{r["ASSIGNED BY"]}: {r["GO TERM"]} {r["GO NAME"]}' for _, _, r in goa),
    )

    # Coverage: is each GOA RCA row present in its review?
    reviewed_keys = {
        (o, g, a.get("term", {}).get("id"), a.get("original_reference_id")) for o, g, a in rev
    }
    has_review = {
        (path.split(os.sep)[-3], path.split(os.sep)[-2])
        for path in glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-ai-review.yaml"))
    }
    uncovered = [
        (o, g, r)
        for o, g, r in goa
        if (o, g, r["GO TERM"], r["REFERENCE"]) not in reviewed_keys
    ]
    print(f"## GOA RCA rows with no matching reviewed RCA row: {len(uncovered)}")
    for o, g, r in uncovered:
        why = "no review file" if (o, g) not in has_review else "not in review"
        print(f'  {o}/{g}  {r["GO TERM"]} {r["GO NAME"]}  {r["REFERENCE"]}  ({why})')
    print()

    # Review actions
    actions = Counter((a.get("review") or {}).get("action", "MISSING") for _, _, a in rev)
    table("Reviewed RCA rows by action", actions)

    table("GOA rows by cluster", Counter(cluster(r["REFERENCE"]) for _, _, r in goa))
    by_cluster: dict[str, Counter] = defaultdict(Counter)
    for _, _, a in rev:
        act = (a.get("review") or {}).get("action", "MISSING")
        by_cluster[cluster(a.get("original_reference_id"), act)][act] += 1
    print("## Reviewed RCA rows: cluster x action")
    for name, c in sorted(by_cluster.items(), key=lambda kv: -sum(kv[1].values())):
        print(f"  {sum(c.values()):4d}  {name}  " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
    print()

    by_term_action: dict[str, Counter] = defaultdict(Counter)
    by_ref_action: dict[str, Counter] = defaultdict(Counter)
    for _, _, a in rev:
        term = f'{a.get("term", {}).get("id")} {a.get("term", {}).get("label")}'
        act = (a.get("review") or {}).get("action", "MISSING")
        by_term_action[term][act] += 1
        by_ref_action[a.get("original_reference_id", "?")][act] += 1

    print("## Reviewed RCA rows: term x action")
    for term, c in sorted(by_term_action.items(), key=lambda kv: -sum(kv[1].values())):
        print(f"  {sum(c.values()):4d}  {term}  " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
    print()
    print("## Reviewed RCA rows: reference x action")
    for ref, c in sorted(by_ref_action.items(), key=lambda kv: -sum(kv[1].values())):
        print(f"  {sum(c.values()):4d}  {ref}  " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
    print()

    if args.list:
        print("## Reviewed rows")
        for o, g, a in rev:
            act = (a.get("review") or {}).get("action", "MISSING")
            print(
                f'  {o}/{g}\t{a.get("term", {}).get("id")}\t{a.get("term", {}).get("label")}'
                f'\t{a.get("original_reference_id")}\t{act}'
            )

    if args.yaml:
        out = []
        for o, g, a in rev:
            review = a.get("review") or {}
            out.append(
                {
                    "organism": o,
                    "gene": g,
                    "term_id": a.get("term", {}).get("id"),
                    "term_label": a.get("term", {}).get("label"),
                    "negated": bool(a.get("negated", False)),
                    "reference": a.get("original_reference_id"),
                    "action": review.get("action"),
                    "cluster": cluster(a.get("original_reference_id"), review.get("action")),
                    "proposed_replacement_terms": [
                        f'{t.get("id")} {t.get("label")}'
                        for t in review.get("proposed_replacement_terms") or []
                    ]
                    or None,
                }
            )
        out = [{k: v for k, v in row.items() if v not in (None, False)} for row in out]
        with open(args.yaml, "w") as fh:
            fh.write("# Generated by projects/OMICS_EVIDENCE/rca/rca_inventory.py -- do not edit\n")
            yaml.safe_dump(out, fh, sort_keys=False, width=120)
        print(f"wrote {len(out)} rows to {args.yaml}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
