#!/usr/bin/env python3
"""Compare curated ProTrek and ProtNLM2 assessments on the same proteins.

Both evaluations use the de Crecy-Lagard et al. 2025 categories
(COR/CNN/LSP/UNC/PLI/NPI/REP) applied to the same 50 ARGO-ProtNLM-50 proteins by
the same review process, so the assessment distributions are comparable. The
prediction sets differ in size and construction -- ProtNLM2 emits a
confidence-filtered variable-length set (39 of the 50 proteins received GO
predictions), while ProTrek returns a ranked list cut here at depth 3 -- so
counts are reported per protein as well as in aggregate.

Usage:
  uv run python projects/PROTREK_EVALUATION/head_to_head_assessments.py \
      --out projects/PROTREK_EVALUATION/argo50_assessment_head_to_head.json
"""
from __future__ import annotations

import argparse
import glob
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CS = {"COR": 2, "CNN": 2, "LSP": 2, "UNC": 1, "PLI": 0, "NPI": 0, "REP": 0}
ORDER = ["COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP"]


def load(pattern: str, limit: int | None = None) -> dict[str, list[str]]:
    """Assessments per accession; ``limit`` keeps only the first N per protein.

    The reviews list predictions in ProTrek rank order, so limit=1 reproduces a
    top-1-only prediction set.
    """
    out: dict[str, list[str]] = {}
    for path in sorted(glob.glob(str(ROOT / pattern))):
        data = yaml.safe_load(Path(path).read_text())
        preds = [p["review"]["assessment"] for p in data.get("predictions") or []]
        out[data["id"]] = preds[:limit] if limit else preds
    return out


def stats(assess: dict[str, list[str]], accs: set[str]) -> dict:
    flat = [a for k, v in assess.items() if k in accs for a in v]
    if not flat:
        return {}
    counts = Counter(flat)
    return {
        "n_proteins_with_predictions": sum(1 for k, v in assess.items() if k in accs and v),
        "n_predictions": len(flat),
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

    trek = load("genes/*/*/*-protrek-predictions-review.yaml")
    trek_top1 = load("genes/*/*/*-protrek-predictions-review.yaml", limit=1)
    nlm = load("genes/*/*/*-protnlm-predictions-review.yaml")
    shared = {k for k in trek if k in nlm}

    result = {
        "note": (
            "ProTrek is scored at retrieval depth 3 (and separately at depth 1); "
            "ProtNLM2's set is variable-length and confidence-filtered by its Evidencer. "
            "Both were assessed on the same 50 proteins by the same review process."
        ),
        "protrek_top3": stats(trek, shared),
        "protrek_top1": stats(trek_top1, shared),
        "protnlm2": stats(nlm, shared),
        "n_shared_proteins": len(shared),
        "proteins_with_no_protnlm_prediction": sorted(
            acc for acc in shared if not nlm.get(acc)),
        "per_protein": {
            acc: {"protrek": trek.get(acc, []), "protnlm": nlm.get(acc, [])}
            for acc in sorted(set(trek) | set(nlm))
        },
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "per_protein"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
