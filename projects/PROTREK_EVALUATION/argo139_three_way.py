#!/usr/bin/env python3
"""Three-way VDCL comparison on ARGO139: ProTrek vs BioReason-SFT vs GO-GPT.

All three prediction sets were assessed with the de Crecy-Lagard et al. 2025
(VDCL) taxonomy against the same AIGR gene reviews, so their assessment
distributions are directly comparable. What is *not* comparable without care is
prediction-set construction:

  ProTrek        ranked retrieval, cut at a chosen depth (reported at 3 and 1)
  BioReason-SFT  HuggingFace protein_catalogue term list, includes ancestors
  GO-GPT         leaf-term output, includes ancestors and unresolved terms

The ancestor-inclusive sets carry very large UNC fractions for that reason, so
this script reports both the raw distribution and one restricted to resolved,
non-UNC calls, which is the closest to like-for-like.

Usage:
  uv run python projects/PROTREK_EVALUATION/argo139_three_way.py \
      --out projects/PROTREK_EVALUATION/argo139_three_way.json
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
COHORT = ROOT / "projects/PROTREK_EVALUATION/argo139_sequences.tsv"
CS = {"COR": 2, "CNN": 2, "LSP": 2, "UNC": 1, "PLI": 0, "NPI": 0, "REP": 0}
ORDER = ["COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP"]

SOURCES = {
    "protrek": "-protrek-predictions-review.yaml",
    "bioreason_sft": "-sft-predictions.yaml",
    "gogpt_leaf": "-gogpt-leaf-predictions.yaml",
}


def collect(suffix: str, limit: int | None = None) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for row in csv.DictReader(COHORT.open(), delimiter="\t"):
        f = ROOT / "genes" / row["species_dir"] / row["symbol"] / f"{row['symbol']}{suffix}"
        if not f.exists():
            continue
        data = yaml.safe_load(f.read_text()) or {}
        preds = [p["review"]["assessment"] for p in data.get("predictions") or []]
        out[f"{row['species_dir']}/{row['symbol']}"] = preds[:limit] if limit else preds
    return out


def summarise(assess: dict[str, list[str]], drop_uncertain: bool = False) -> dict:
    flat = [a for v in assess.values() for a in v if not (drop_uncertain and a == "UNC")]
    if not flat:
        return {}
    counts = Counter(flat)
    return {
        "n_genes": sum(1 for v in assess.values() if v),
        "n_predictions": len(flat),
        "predictions_per_gene": round(len(flat) / max(1, sum(1 for v in assess.values() if v)), 1),
        "counts": {k: counts.get(k, 0) for k in ORDER if counts.get(k)},
        "pct": {k: round(100 * counts.get(k, 0) / len(flat), 1) for k in ORDER if counts.get(k)},
        "mean_confidence_score": round(sum(CS[a] for a in flat) / len(flat), 3),
        "concordant_pct": round(100 * sum(1 for a in flat if CS[a] == 2) / len(flat), 1),
        "discordant_pct": round(100 * sum(1 for a in flat if CS[a] == 0) / len(flat), 1),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    raw = {k: collect(v) for k, v in SOURCES.items()}
    raw["protrek_top1"] = collect(SOURCES["protrek"], limit=1)

    result = {
        "cohort": "ARGO139",
        "note": (
            "Same genes, same VDCL taxonomy, same AIGR reference reviews. Prediction-set "
            "construction differs: ProTrek is a ranked retrieval cut at depth 3 (and 1); "
            "BioReason-SFT and GO-GPT term lists include ancestor terms, which is why their "
            "UNC fractions are large. 'excluding_UNC' is the closest like-for-like view."
        ),
        "all_predictions": {k: summarise(v) for k, v in raw.items()},
        "excluding_UNC": {k: summarise(v, drop_uncertain=True) for k, v in raw.items()},
        "genes_covered": {k: sum(1 for v in vv.values() if v) for k, vv in raw.items()},
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "note"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
