#!/usr/bin/env python3
"""Record SwissProt review status for a ProTrek query cohort.

This is the single most important interpretive control for the ARGO139 cohort.
ProTrek was trained on 14 million SwissProt protein-text pairs, and the text index
searched here is built from SwissProt GO annotations -- so for a SwissProt-reviewed
query, the protein's *own* GO sentences are in the index being searched. Recovering
them is recall of training data, not prediction.

ARGO-ProtNLM-50 is entirely TrEMBL and so measures generalisation; ARGO139 is
overwhelmingly SwissProt and so measures memorisation. Reported rates from the two
cohorts must not be pooled or compared without this stratification.

Usage:
  uv run python projects/PROTREK_EVALUATION/check_swissprot_membership.py \
      --queries projects/PROTREK_EVALUATION/argo139_sequences.tsv \
      --out projects/PROTREK_EVALUATION/argo139_swissprot_status.csv
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def review_status(flat: Path) -> str:
    """SwissProt entries carry 'Reviewed' on the ID line, TrEMBL 'Unreviewed'."""
    head = flat.read_text().splitlines()[0]
    if "Unreviewed" in head:
        return "TrEMBL"
    if "Reviewed" in head:
        return "SwissProt"
    return "unknown"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    rows = list(csv.DictReader(args.queries.open(), delimiter="\t"))
    out = []
    for r in rows:
        # ARGO139 rows carry species_dir/symbol; ARGO-ProtNLM-50 rows are accession-named.
        symbol = r.get("symbol") or r["accession"]
        flat = ROOT / "genes" / r["species_dir"] / symbol / f"{symbol}-uniprot.txt"
        out.append({
            "accession": r["accession"],
            "species_dir": r["species_dir"],
            "symbol": symbol,
            "uniprot_section": review_status(flat) if flat.exists() else "missing",
            "in_protrek_text_index_by_construction":
                str(review_status(flat) == "SwissProt") if flat.exists() else "unknown",
        })

    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    n_sp = sum(1 for r in out if r["uniprot_section"] == "SwissProt")
    summary = {"n": len(out), "swissprot": n_sp, "trembl": len(out) - n_sp,
               "swissprot_pct": round(100 * n_sp / len(out), 1)}
    print(json.dumps(summary, indent=2))
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
