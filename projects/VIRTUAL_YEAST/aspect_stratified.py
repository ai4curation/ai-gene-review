#!/usr/bin/env python3
"""Review-outcome stratified by evidence class x GO aspect (MF/BP/CC), any organism.

Extends the retention pilot (score_predictions.py) along two axes the paper's critique
cares about: which GO *aspect* attracts over-annotation, and whether the pattern holds in
an independent curated organism (S. pombe). GO aspect is joined per gene from the cached
GOA TSV (its "GO ASPECT" column), so nothing is hardcoded.

Run: python3 aspect_stratified.py --genes-dir genes/yeast [--genes-dir genes/SCHPO]
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import sys
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required")

COMPUTATIONAL = {"IBA", "IBD", "IKR", "IRD", "IEA", "ISS", "ISA", "ISM", "ISO", "RCA", "IGC"}
EXPERIMENTAL = {"IDA", "IMP", "IPI", "IGI", "IEP", "EXP", "HDA", "HMP", "HGI", "HEP"}
RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE", "MODIFY"}
NEGATIVE = {"MARK_AS_OVER_ANNOTATED", "REMOVE"}
ASPECT_SHORT = {"molecular_function": "MF", "biological_process": "BP",
                "cellular_component": "CC"}


def ev_class(code: str) -> str:
    code = (code or "").upper()
    if code in COMPUTATIONAL:
        return "computational"
    if code in EXPERIMENTAL:
        return "experimental"
    return "other"


def term_aspect_map(goa_tsv: str) -> dict[str, str]:
    m: dict[str, str] = {}
    with open(goa_tsv) as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if not header:
            return m
        try:
            t_i, a_i = header.index("GO TERM"), header.index("GO ASPECT")
        except ValueError:
            t_i, a_i = 4, 6
        for row in reader:
            if len(row) > max(t_i, a_i) and row[t_i].startswith("GO:"):
                m[row[t_i]] = ASPECT_SHORT.get(row[a_i], row[a_i])
    return m


def analyze(genes_dir: str):
    # cell[(ev_class, aspect)] -> Counter(action)
    cell: dict[tuple, Counter] = defaultdict(Counter)
    n_genes = 0
    for gdir in sorted(glob.glob(os.path.join(genes_dir, "*"))):
        rev = glob.glob(os.path.join(gdir, "*-ai-review.yaml"))
        goa = glob.glob(os.path.join(gdir, "*-goa.tsv"))
        if not rev or not goa:
            continue
        try:
            doc = yaml.safe_load(open(rev[0])) or {}
        except yaml.YAMLError:
            continue
        aspects = term_aspect_map(goa[0])
        counted = False
        for ann in doc.get("existing_annotations") or []:
            action = ((ann.get("review") or {}).get("action") or "").upper()
            if not action or action == "PENDING":
                continue
            term = ((ann.get("term") or {}).get("id")) or ""
            aspect = aspects.get(term, "?")
            cell[(ev_class(ann.get("evidence_type")), aspect)][action] += 1
            counted = True
        n_genes += int(counted)
    return cell, n_genes


def report(genes_dir: str, cell, n_genes) -> None:
    total = sum(sum(c.values()) for c in cell.values())
    print(f"\n## {genes_dir}  (genes={n_genes}, annotations={total})")
    if total == 0:
        print("  (no reviewed annotations - inconclusive)")
        return
    print("evidence_class\taspect\tn\tretained_%\tover-annot/removed_%")
    for evc in ["experimental", "computational"]:
        for aspect in ["MF", "BP", "CC"]:
            c = cell.get((evc, aspect))
            if not c:
                continue
            n = sum(c.values())
            ret = sum(v for a, v in c.items() if a in RETAINED)
            neg = sum(v for a, v in c.items() if a in NEGATIVE)
            print(f"{evc}\t{aspect}\t{n}\t{100*ret/n:.1f}\t{100*neg/n:.1f}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genes-dir", action="append", required=True,
                    help="repeatable; e.g. --genes-dir genes/yeast --genes-dir genes/SCHPO")
    args = ap.parse_args()
    print("# Review outcomes by evidence class x GO aspect")
    for gd in args.genes_dir:
        cell, n = analyze(gd)
        report(gd, cell, n)


if __name__ == "__main__":
    main()
