#!/usr/bin/env python3
"""Head-to-head comparison of ProTrek and ProtNLM2 on the ARGO-ProtNLM-50 proteins.

Both models are asked the same question (what GO terms does this protein have?)
for the same 50 TrEMBL proteins, and both are scored against the same frozen
GOA snapshot with the same overlap categories, so the distributions are directly
comparable. ProtNLM2's calls are read from the committed
``projects/PROTNLM_EVALUATION/bench50_evaluation_results.csv``.

Note the two models emit different numbers of predictions per protein: ProtNLM2
emits a variable-length, confidence-filtered set, while ProTrek returns a ranked
list that has to be cut at a chosen depth. Comparisons are therefore reported
both over the full sets and restricted to each model's top prediction.

Usage:
  uv run python projects/PROTREK_EVALUATION/compare_with_protnlm.py \
      --protrek projects/PROTREK_EVALUATION/argo50_protrek_go_calls.csv \
      --protnlm projects/PROTNLM_EVALUATION/bench50_evaluation_results.csv \
      --out projects/PROTREK_EVALUATION/argo50_head_to_head.json
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

CATS = ["EXACT", "LESS_SPECIFIC", "MORE_SPECIFIC", "NO_OVERLAP", "NOT_IN_GOA",
        "OBSOLETE_TERM", "UNRESOLVED"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--protrek", required=True, type=Path)
    ap.add_argument("--protnlm", required=True, type=Path)
    ap.add_argument("--depth", type=int, default=3, help="ProTrek ranks treated as the prediction set")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    trek = [r for r in csv.DictReader(args.protrek.open()) if int(r["rank"]) <= args.depth]
    nlm = list(csv.DictReader(args.protnlm.open()))

    trek_by_acc = defaultdict(list)
    for r in trek:
        trek_by_acc[r["accession"]].append(r)
    nlm_by_acc = defaultdict(list)
    for r in nlm:
        nlm_by_acc[r["accession"]].append(r)

    trek_terms = {a: {r["pred_id"] for r in rs if r["pred_id"]} for a, rs in trek_by_acc.items()}
    nlm_terms = {a: {r["pred_id"] for r in rs if r["pred_id"]} for a, rs in nlm_by_acc.items()}

    shared = sorted(set(trek_terms) & set(nlm_terms))
    overlap_counts = Counter()
    per_protein_overlap = {}
    for acc in shared:
        inter = trek_terms[acc] & nlm_terms[acc]
        per_protein_overlap[acc] = {
            "protrek_terms": len(trek_terms[acc]),
            "protnlm_terms": len(nlm_terms[acc]),
            "identical_terms": sorted(inter),
        }
        overlap_counts["proteins_with_shared_term"] += 1 if inter else 0
        overlap_counts["shared_term_instances"] += len(inter)

    summary = {
        "protrek_depth": args.depth,
        "n_proteins_protrek": len(trek_by_acc),
        "n_proteins_protnlm": len(nlm_by_acc),
        "n_proteins_both": len(shared),
        "n_predictions_protrek": len(trek),
        "n_predictions_protnlm": len(nlm),
        "protrek_match_categories": {c: sum(1 for r in trek if r["match_category"] == c)
                                     for c in CATS if any(r["match_category"] == c for r in trek)},
        "protnlm_match_categories": {c: sum(1 for r in nlm if r["match_category"] == c)
                                     for c in CATS if any(r["match_category"] == c for r in nlm)},
        "protrek_top1_match_categories": dict(Counter(
            r["match_category"] for r in csv.DictReader(args.protrek.open()) if r["rank"] == "1")),
        "term_level_agreement": {
            "proteins_compared": len(shared),
            "proteins_with_at_least_one_identical_term": overlap_counts["proteins_with_shared_term"],
            "identical_term_instances": overlap_counts["shared_term_instances"],
        },
        "aspect_mix_protrek": dict(Counter(r["aspect"] for r in trek)),
        "aspect_mix_protnlm": dict(Counter(
            (r["pred_label"].split(":")[0] if ":" in r["pred_label"] else "?") for r in nlm)),
    }

    args.out.write_text(json.dumps({"summary": summary, "per_protein": per_protein_overlap}, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
