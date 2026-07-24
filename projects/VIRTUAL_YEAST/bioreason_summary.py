#!/usr/bin/env python3
"""Aggregate existing BioReason-Pro (RL) review scores and compare to InterPro2GO.

BioReason-Pro is a reasoning-LLM function predictor: unlike InterPro2GO it emits free
GO calls from a chain-of-thought over sequence+domains, so its output is *not* constrained
to the domain->GO table. The repo already contains 23 curated pombe BioReason reviews
(genes/SCHPO/*/*-bioreason-rl-review.md), each scoring Correctness and Completeness on a
0-5 scale and often explicitly comparing to interpro2go. This script aggregates those
curated scores and scans the review prose for recurrent error signatures. Nothing is
hardcoded; it reads whatever review files are present.

Run: python3 bioreason_summary.py [--genes-dir genes/SCHPO]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from collections import Counter

CORR_RE = re.compile(r"Correctness\**:?\s*\**\s*([0-5])\s*/\s*5", re.I)
COMPL_RE = re.compile(r"Completeness\**:?\s*\**\s*([0-5])\s*/\s*5", re.I)

# Error-signature phrases (lower-cased substring match on review prose).
SIGNATURES = {
    "repeats/agrees-with interpro2go": ["repeats these interpro2go", "reinforces the same",
                                        "does not improve on interpro2go",
                                        "same as interpro2go", "matches interpro2go"],
    "localization default (cytoplasm)": ["localization is wrong", "assigns cytoplasm",
                                         "cytoplasmic localization, which is incorrect",
                                         "default", "mislocali"],
    "pseudoenzyme / activity overstated": ["pseudo-enzyme", "pseudoenzyme",
                                           "catalytic activity overstated",
                                           "missing catalytic", "lacks the conserved"],
    "overstates specificity/function": ["overstate", "too specific", "overreach",
                                        "not supported"],
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genes-dir", default="genes/SCHPO")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.genes_dir, "*", "*-bioreason-rl-review.md")))
    if not files:
        print("No BioReason review files found (inconclusive).")
        return

    corr, compl = [], []
    sig_counts = Counter()
    rows = []
    for f in files:
        text = open(f).read()
        low = text.lower()
        cm = CORR_RE.search(text)
        pm = COMPL_RE.search(text)
        c = int(cm.group(1)) if cm else None
        p = int(pm.group(1)) if pm else None
        if c is not None:
            corr.append(c)
        if p is not None:
            compl.append(p)
        gene = os.path.basename(os.path.dirname(f))
        hit = []
        for name, phrases in SIGNATURES.items():
            if any(ph in low for ph in phrases):
                sig_counts[name] += 1
                hit.append(name)
        rows.append((gene, c, p, hit))

    n = len(files)
    mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")
    print(f"# BioReason-Pro (RL) review aggregate  ({args.genes_dir})")
    print(f"# reviews: {n}")
    print(f"# mean correctness:  {mean(corr):.2f}/5  (n={len(corr)})")
    print(f"# mean completeness: {mean(compl):.2f}/5  (n={len(compl)})")

    print("\n# Correctness distribution (0-5)")
    cdist = Counter(corr)
    for s in range(6):
        bar = "#" * cdist.get(s, 0)
        print(f"  {s}/5: {cdist.get(s,0):2d} {bar}")
    lo = sum(1 for c in corr if c <= 2)
    print(f"# reviews with correctness <=2/5: {lo}/{len(corr)} ({100*lo/len(corr):.0f}%)")

    print("\n# Error-signature frequency (curated-reviewer prose)")
    for name, cnt in sig_counts.most_common():
        print(f"  {cnt:2d}\t{name}")

    print("\n# Per-gene")
    print("gene\tcorrectness\tcompleteness\tsignatures")
    for gene, c, p, hit in rows:
        print(f"{gene}\t{c}\t{p}\t{';'.join(hit) if hit else '-'}")


if __name__ == "__main__":
    main()
