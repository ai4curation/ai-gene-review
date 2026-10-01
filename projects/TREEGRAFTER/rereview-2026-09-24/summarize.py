#!/usr/bin/env python3
"""Summarise the 2026-09-24 TreeGrafter rejection re-review.

Reads every ``batch-*.yaml`` in this folder and writes ``summary.tsv`` next to
them: transition counts (previous action -> new action), retained/changed
totals, and the terms most often relaxed. No numbers are hard-coded.

Run:
  uv run --with pyyaml projects/TREEGRAFTER/rereview-2026-09-24/summarize.py
"""
from __future__ import annotations

import csv
import glob
import os
from collections import Counter

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
TREEGRAFTER_REF = "GO_REF:0000118"
TOP_TERMS = 20  # cap on the per-term table; the TSV records what it leaves out


def main() -> None:
    rows = []
    for path in sorted(glob.glob(os.path.join(HERE, "batch-*.yaml"))):
        with open(path) as fh:
            doc = yaml.safe_load(fh) or {}
        for gene in doc.get("genes") or []:
            for ann in gene.get("annotations") or []:
                if ann.get("original_reference_id") != TREEGRAFTER_REF:
                    continue
                rows.append(
                    {
                        "batch": os.path.basename(path),
                        "gene": gene.get("gene", ""),
                        "term_id": ann.get("term_id", ""),
                        "term_label": ann.get("term_label", ""),
                        "previous_action": ann.get("previous_action", ""),
                        "action": ann.get("action", ""),
                        "outcome": ann.get("outcome", ""),
                    }
                )

    transitions = Counter((r["previous_action"], r["action"]) for r in rows)
    outcomes = Counter(r["outcome"] for r in rows)
    # Every row whose action moved, so the table's total matches `outcome changed`.
    # Filtering on the *new* action instead silently dropped the
    # REMOVE -> MARK_AS_OVER_ANNOTATED rows, which are relaxations too.
    relaxed_terms = Counter(
        (r["term_id"], r["term_label"])
        for r in rows
        if r["previous_action"] != r["action"]
    )
    genes = {r["gene"] for r in rows}

    out = os.path.join(HERE, "summary.tsv")
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["section", "key", "value", "count"])
        w.writerow(["totals", "annotations", "", len(rows)])
        w.writerow(["totals", "genes", "", len(genes)])
        for k, n in sorted(outcomes.items()):
            w.writerow(["outcome", k, "", n])
        for (prev, new), n in sorted(transitions.items(), key=lambda kv: -kv[1]):
            w.writerow(["transition", prev, new, n])
        # The per-term table is capped, so say so in the file itself: a reader
        # otherwise cannot tell a short tail from a complete one.
        top = relaxed_terms.most_common(TOP_TERMS)
        w.writerow(["relaxed_term_total_distinct", "", "", len(relaxed_terms)])
        w.writerow(["relaxed_term_shown", "", "", len(top)])
        for (tid, label), n in top:
            w.writerow(["relaxed_term", tid, label, n])
        remainder = sum(relaxed_terms.values()) - sum(n for _, n in top)
        if remainder:
            w.writerow(["relaxed_term_other", "", f"{len(relaxed_terms) - len(top)} further terms", remainder])
    print(f"wrote {out}: {len(rows)} annotations across {len(genes)} genes")
    for (prev, new), n in sorted(transitions.items(), key=lambda kv: -kv[1]):
        print(f"  {prev} -> {new}: {n}")


if __name__ == "__main__":
    main()
