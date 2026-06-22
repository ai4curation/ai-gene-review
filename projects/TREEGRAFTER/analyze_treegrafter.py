#!/usr/bin/env python3
"""Evaluate TreeGrafter / PANTHER (IBA) inferences against AIGR reviews.

TreeGrafter is the InterProScan tool that grafts query proteins onto PANTHER
reference phylogenetic trees, propagating the PAINT/GO_Central ancestral GO
annotations. In GOA these surface as ``IBA`` (Inferred from Biological aspect
of Ancestor) evidence with reference ``GO_REF:0000033`` and assigned-by
``GO_Central``. This script mines every ``*-ai-review.yaml`` for those
annotations and tabulates the reviewer's adjudication (ACTION) so we can ask:
how good are TreeGrafter-style phylogenetic inferences when held to GO review
criteria?

Outputs (written next to this script):
  - treegrafter_iba_review.tsv   one row per reviewed IBA annotation
  - treegrafter_summary.tsv      action counts + per-aspect breakdown

Run:
  uv run --with pyyaml projects/TREEGRAFTER/analyze_treegrafter.py
or:
  python3 projects/TREEGRAFTER/analyze_treegrafter.py
"""
from __future__ import annotations

import csv
import glob
import os
from collections import Counter, defaultdict

import yaml

# Resolve the repo root from this file's location (projects/TREEGRAFTER/).
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# GO aspect prefixes are not stored in the review YAML, so we infer aspect from
# the well-known root-term neighbourhoods only where present; otherwise leave
# blank. We instead group by the high-level action which is what we care about.
TREEGRAFTER_REF = "GO_REF:0000033"


def is_treegrafter(ann: dict) -> bool:
    """True if an existing_annotation came from the PANTHER/PAINT (IBA) pipeline."""
    if ann.get("evidence_type") != "IBA":
        return False
    ref = ann.get("original_reference_id") or ""
    # PANTHER/PAINT IBA annotations carry GO_REF:0000033. A handful of reviews
    # leave the ref blank; IBA is itself unambiguous for the phylogenetic
    # pipeline, so we also count blank-ref IBA. We do NOT count other GO_REFs.
    return ref == TREEGRAFTER_REF or ref == ""


def main() -> None:
    rows = []
    files = sorted(glob.glob(os.path.join(ROOT, "genes", "**", "*-ai-review.yaml"),
                             recursive=True))
    for path in files:
        try:
            with open(path) as fh:
                doc = yaml.safe_load(fh)
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"WARN: failed to parse {path}: {exc}")
            continue
        if not isinstance(doc, dict):
            continue
        gene = doc.get("gene_symbol", "")
        taxon = (doc.get("taxon") or {}).get("label", "")
        rel = os.path.relpath(path, ROOT)
        for ann in doc.get("existing_annotations") or []:
            if not isinstance(ann, dict) or not is_treegrafter(ann):
                continue
            review = ann.get("review") or {}
            term = ann.get("term") or {}
            rows.append({
                "gene": gene,
                "taxon": taxon,
                "term_id": term.get("id", ""),
                "term_label": term.get("label", ""),
                "action": (review.get("action") or "UNREVIEWED").strip(),
                "negated": bool(ann.get("negated", False)),
                "has_replacement": bool(review.get("proposed_replacement_terms")),
                "file": rel,
            })

    # Write per-annotation rows.
    out_rows = os.path.join(HERE, "treegrafter_iba_review.tsv")
    with open(out_rows, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else
                           ["gene", "taxon", "term_id", "term_label", "action",
                            "negated", "has_replacement", "file"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # Summaries.
    action_counts = Counter(r["action"] for r in rows)
    genes_with_iba = len({r["file"] for r in rows})
    total_genes = len(files)
    # Most-common terms that get REMOVE / MARK_AS_OVER_ANNOTATED (problem terms).
    problem_actions = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}
    problem_terms = Counter(
        (r["term_id"], r["term_label"]) for r in rows if r["action"] in problem_actions
    )

    out_sum = os.path.join(HERE, "treegrafter_summary.tsv")
    with open(out_sum, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["metric", "value"])
        w.writerow(["total_review_files", total_genes])
        w.writerow(["genes_with_treegrafter_iba", genes_with_iba])
        w.writerow(["total_treegrafter_iba_annotations", len(rows)])
        w.writerow([])
        w.writerow(["action", "count"])
        for action, n in action_counts.most_common():
            w.writerow([action, n])
        w.writerow([])
        w.writerow(["top_problematic_terms (REMOVE/MODIFY/OVER_ANNOTATED)", "count"])
        for (tid, label), n in problem_terms.most_common(25):
            w.writerow([f"{tid} {label}", n])

    # Console report.
    total = len(rows)
    print(f"Scanned {total_genes} review files")
    print(f"Genes with >=1 TreeGrafter/PANTHER IBA annotation: {genes_with_iba}")
    print(f"Total reviewed TreeGrafter IBA annotations: {total}\n")
    if total:
        print("Action breakdown:")
        for action, n in action_counts.most_common():
            print(f"  {action:24s} {n:5d}  ({100*n/total:5.1f}%)")
    print(f"\nWrote {os.path.relpath(out_rows, ROOT)}")
    print(f"Wrote {os.path.relpath(out_sum, ROOT)}")


if __name__ == "__main__":
    main()
