#!/usr/bin/env python3
"""Parse Boltz-2 affinity outputs and rank candidate substrates.

After running `boltz predict` over the YAMLs from generate_inputs.py, point this
script at the Boltz output directory. It finds the per-prediction affinity JSON
files and produces a ranked table.

Boltz-2 affinity JSON fields used:
  - affinity_pred_value: log10(IC50) in micromolar; LOWER = stronger predicted binding
  - affinity_probability_binary: probability the ligand is a binder (HIGHER = more binder-like)

Interpretation caveats (see ../BOLTZ2_SUBSTRATE_SPECIFICITY.md):
  * This ranks BINDING, a proxy for (not proof of) being a catalytic substrate.
  * Affinity is relative; only compare candidates for the SAME enzyme.
  * Confirm the predicted pose is in the catalytic pocket before drawing conclusions.

Usage:
    python rank_affinity.py --results boltz_out [--tsv ranked.tsv]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def find_affinity_files(results: Path) -> list[Path]:
    """Recursively locate Boltz-2 affinity JSON files in an output tree."""
    return sorted(p for p in results.rglob("*.json")
                  if p.name.startswith("affinity"))


def candidate_name(path: Path) -> str:
    """Derive the candidate name from the affinity filename / parent dir.

    Boltz writes files like affinity_<name>.json under predictions/<name>/.
    """
    stem = path.stem  # e.g. affinity_glucose
    if stem.startswith("affinity_"):
        return stem[len("affinity_"):]
    return path.parent.name


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", required=True, type=Path,
                    help="Boltz output directory (e.g. boltz_out)")
    ap.add_argument("--tsv", type=Path, help="Optional path to write the ranked table as TSV")
    args = ap.parse_args()

    files = find_affinity_files(args.results)
    if not files:
        raise SystemExit(
            f"No affinity*.json found under {args.results}. "
            "Did `boltz predict` run with an `affinity` properties block?"
        )

    rows = []
    for f in files:
        data = json.loads(f.read_text())
        rows.append({
            "candidate": candidate_name(f),
            "log10_IC50_uM": data.get("affinity_pred_value"),
            "binder_prob": data.get("affinity_probability_binary"),
        })

    # Rank by predicted affinity (lower log10(IC50) = tighter). None sorts last.
    rows.sort(key=lambda r: (r["log10_IC50_uM"] is None, r["log10_IC50_uM"]))

    header = ["rank", "candidate", "log10_IC50_uM", "binder_prob"]
    print("\t".join(header))
    out_lines = ["\t".join(header)]
    for i, r in enumerate(rows, 1):
        val = "" if r["log10_IC50_uM"] is None else f"{r['log10_IC50_uM']:.3f}"
        prob = "" if r["binder_prob"] is None else f"{r['binder_prob']:.3f}"
        line = "\t".join([str(i), r["candidate"], val, prob])
        print(line)
        out_lines.append(line)

    if args.tsv:
        args.tsv.write_text("\n".join(out_lines) + "\n")
        print(f"\nWrote {args.tsv}")

    print("\nReminder: lower log10_IC50_uM = stronger predicted binding; "
          "binder_prob nearer 1 = more binder-like. Binding != catalytic substrate.")


if __name__ == "__main__":
    main()
