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
                        "gene_file": gene.get("gene_file", ""),
                        "term_id": ann.get("term_id", ""),
                        "term_label": ann.get("term_label", ""),
                        "previous_action": ann.get("previous_action", ""),
                        "action": ann.get("action", ""),
                        "outcome": ann.get("outcome", ""),
                        "merged_into": gene.get("merged_into", ""),
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
    # Three different things get called "genes" here, so each is counted and
    # named separately rather than collapsed into one ambiguous figure:
    #   - entries: one per gene entry in the batch records. Keyed on gene_file,
    #     not the label, because two paralogs can share a label (PSEPK/dapF
    #     named two proteins), which silently undercounted.
    #   - proteins: entries minus those the audit established are a second
    #     record of a protein already counted. `merged_into` marks those, so
    #     this is derived from the records rather than adjusted by hand.
    #   - rows / adjudications: likewise, a merged entry's rows duplicate the
    #     surviving twin's, so they are recorded but not distinct decisions.
    entries = {r["gene_file"] or r["gene"] for r in rows}
    proteins = {
        r["gene_file"] or r["gene"] for r in rows if not r["merged_into"]
    }
    adjudications = [r for r in rows if not r["merged_into"]]

    out = os.path.join(HERE, "summary.tsv")
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["section", "key", "value", "count"])
        # `annotations`/`genes` were ambiguous: the first counted recorded rows
        # and the second entries, but neither label said so, and a reader
        # comparing them against the protein counts found them off by one.
        w.writerow(["totals", "recorded_rows", "", len(rows)])
        w.writerow(["totals", "distinct_adjudications", "", len(adjudications)])
        w.writerow(["totals", "gene_entries", "", len(entries)])
        w.writerow(["totals", "proteins", "", len(proteins)])
        for k, n in sorted(outcomes.items()):
            w.writerow(["outcome", k, "", n])
        for (prev, new), n in sorted(transitions.items(), key=lambda kv: -kv[1]):
            w.writerow(["transition", prev, new, n])
        # The per-term table is capped, so say so in the file itself: a reader
        # otherwise cannot tell a short tail from a complete one.
        top = relaxed_terms.most_common(TOP_TERMS)
        shown_rows = sum(n for _, n in top)
        remainder = sum(relaxed_terms.values()) - shown_rows
        # Each label says its unit: the counts below mix distinct terms and rows.
        w.writerow(["relaxed_distinct_terms", "", "", len(relaxed_terms)])
        w.writerow(["relaxed_terms_shown", "", "", len(top)])
        w.writerow(["relaxed_rows_shown", "", "", shown_rows])
        w.writerow(["relaxed_rows_not_shown", "",
                    f"spread over {len(relaxed_terms) - len(top)} further terms", remainder])
        for (tid, label), n in top:
            w.writerow(["relaxed_term", tid, label, n])
    print(
        f"wrote {out}: {len(rows)} recorded rows "
        f"({len(adjudications)} distinct adjudications) across "
        f"{len(entries)} gene entries for {len(proteins)} proteins"
    )
    for (prev, new), n in sorted(transitions.items(), key=lambda kv: -kv[1]):
        print(f"  {prev} -> {new}: {n}")


if __name__ == "__main__":
    main()
