#!/usr/bin/env python3
"""Benchmark computational vs experimental GO annotations against expert review.

For every reviewed S. cerevisiae gene (genes/yeast/*/*-ai-review.yaml), this script
reads each existing annotation's GO evidence code and the reviewer's action
(ACCEPT / KEEP_AS_NON_CORE / MODIFY / MARK_AS_OVER_ANNOTATED / REMOVE / ...), then
stratifies review outcomes by evidence class (computational vs experimental vs
author/curator).

The point: the curated reviews in this repo are a gold standard. This measures how
well *computational* annotations (IBA/IEA/ISS...) survive expert scrutiny relative to
*experimental* ones (IDA/IMP/IPI...) — the kind of prediction-vs-truth evaluation the
"virtual yeast" Perspective (Nature 655, 2026) lacks for its foundation-model
building blocks.

No results are hardcoded. Run: `python3 score_predictions.py [--genes-dir DIR]`.
An empty or inconclusive result is a valid outcome.
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
    sys.exit("PyYAML required: pip install pyyaml")

# GO evidence-code classes (ECO-aligned groupings).
# Computational = phylogenetic/electronic/sequence-similarity inference (a "prediction").
COMPUTATIONAL = {"IBA", "IBD", "IKR", "IRD", "IEA", "ISS", "ISA", "ISM", "ISO", "RCA", "IGC"}
# Experimental = direct wet-lab evidence.
EXPERIMENTAL = {"IDA", "IMP", "IPI", "IGI", "IEP", "EXP", "HDA", "HMP", "HGI", "HEP"}
# Author/curator statements.
AUTHOR = {"TAS", "NAS", "IC", "ND"}

# Actions that mean the annotation did NOT survive review as a correct, retained call.
NEGATIVE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
# Actions that retain the annotation (possibly re-scoped).
RETAINED_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE", "MODIFY"}


def classify_evidence(code: str) -> str:
    code = (code or "").upper().strip()
    if code in COMPUTATIONAL:
        return "computational"
    if code in EXPERIMENTAL:
        return "experimental"
    if code in AUTHOR:
        return "author"
    return "other"


def iter_annotations(genes_dir: str):
    pattern = os.path.join(genes_dir, "*", "*-ai-review.yaml")
    for path in sorted(glob.glob(pattern)):
        gene = os.path.basename(os.path.dirname(path))
        try:
            with open(path) as fh:
                doc = yaml.safe_load(fh) or {}
        except yaml.YAMLError as e:
            print(f"WARN: skipping unparseable {path}: {e}", file=sys.stderr)
            continue
        for ann in doc.get("existing_annotations") or []:
            review = ann.get("review") or {}
            action = (review.get("action") or "").upper().strip()
            if not action or action == "PENDING":
                continue  # not yet reviewed
            yield {
                "gene": gene,
                "evidence": (ann.get("evidence_type") or "").upper().strip(),
                "evidence_class": classify_evidence(ann.get("evidence_type")),
                "action": action,
            }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genes-dir", default="genes/yeast",
                    help="directory of reviewed genes (default: genes/yeast)")
    ap.add_argument("--out-tsv", default=None, help="optional path to write per-annotation TSV")
    args = ap.parse_args()

    rows = list(iter_annotations(args.genes_dir))
    if not rows:
        print("No reviewed annotations found (inconclusive). Check --genes-dir.")
        return

    genes = {r["gene"] for r in rows}
    by_class_action = defaultdict(Counter)  # class -> action -> n
    evidence_counts = Counter()             # raw evidence code -> n
    for r in rows:
        by_class_action[r["evidence_class"]][r["action"]] += 1
        evidence_counts[r["evidence"]] += 1

    print(f"# Yeast prediction-vs-review benchmark")
    print(f"# genes with reviewed annotations: {len(genes)}")
    print(f"# total reviewed annotations: {len(rows)}\n")

    # Main table: retention vs rejection by evidence class.
    header = ["evidence_class", "n", "retained", "retained_%", "over_annot/removed",
              "rejected_%", "undecided"]
    print("\t".join(header))
    for cls in ["experimental", "computational", "author", "other"]:
        actions = by_class_action.get(cls)
        if not actions:
            continue
        n = sum(actions.values())
        retained = sum(v for a, v in actions.items() if a in RETAINED_ACTIONS)
        rejected = sum(v for a, v in actions.items() if a in NEGATIVE_ACTIONS)
        undecided = actions.get("UNDECIDED", 0)
        print("\t".join([
            cls, str(n), str(retained), f"{100*retained/n:.1f}",
            str(rejected), f"{100*rejected/n:.1f}", str(undecided),
        ]))

    # Full action breakdown by class.
    print("\n# Full action breakdown by evidence class")
    all_actions = sorted({a for c in by_class_action.values() for a in c})
    print("\t".join(["evidence_class"] + all_actions))
    for cls in ["experimental", "computational", "author", "other"]:
        actions = by_class_action.get(cls)
        if not actions:
            continue
        print("\t".join([cls] + [str(actions.get(a, 0)) for a in all_actions]))

    # Raw evidence-code frequencies (transparency).
    print("\n# Evidence-code frequencies")
    for code, n in evidence_counts.most_common():
        print(f"{code or '(none)'}\t{n}\t{classify_evidence(code)}")

    if args.out_tsv:
        with open(args.out_tsv, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["gene", "evidence", "evidence_class", "action"],
                               delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"\n# wrote per-annotation rows -> {args.out_tsv}", file=sys.stderr)


if __name__ == "__main__":
    main()
