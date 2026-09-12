#!/usr/bin/env python3
"""Detect GATA-type (Cys4 / type-IV) zinc-finger motifs in protein sequences.

The canonical GATA zinc finger has the consensus:
    C-X2-C-X17-C-X2-C
(two CXXC pairs separated by a ~17-residue loop) followed by a basic tail that
contacts DNA. This script scans each input sequence with that regex-style pattern
and reports the match position and the Cys spacing. No results are hardcoded; all
output is derived from the input FASTA.

Usage:
    python find_gata_zinc_finger.py <input.fasta> [--json out.json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from Bio import SeqIO

# GATA / type-IV Cys4 zinc finger: C-X{2}-C-X{17,20}-C-X{2}-C
# Allow a small tolerance on the loop length (17 is canonical; some are 18-20).
GATA_ZF = re.compile(r"C.{2}C.{17,20}C.{2}C")


def scan_sequence(name: str, seq: str) -> list[dict]:
    """Return all GATA-type zinc-finger matches in a sequence."""
    matches = []
    for m in GATA_ZF.finditer(seq):
        motif = m.group(0)
        # positions of the four cysteines within the motif
        cys_local = [i for i, aa in enumerate(motif) if aa == "C"]
        # spacing between consecutive cysteines
        spacings = [cys_local[i + 1] - cys_local[i] for i in range(len(cys_local) - 1)]
        matches.append(
            {
                "id": name,
                "start_1based": m.start() + 1,
                "end_1based": m.end(),
                "motif": motif,
                "n_cys": motif.count("C"),
                "cys_spacings": spacings,
            }
        )
    return matches


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("fasta", type=Path)
    ap.add_argument("--json", type=Path, default=None)
    args = ap.parse_args()

    if not args.fasta.exists():
        print(f"ERROR: input not found: {args.fasta}", file=sys.stderr)
        return 1

    all_results = []
    for rec in SeqIO.parse(str(args.fasta), "fasta"):
        seq = str(rec.seq)
        hits = scan_sequence(rec.id, seq)
        all_results.append({"id": rec.id, "length": len(seq), "hits": hits})
        print(f"\n{rec.id}  (len={len(seq)})")
        if not hits:
            print("  no GATA-type Cys4 zinc finger detected by C-X2-C-X17-20-C-X2-C")
        for h in hits:
            print(
                f"  match {h['start_1based']}-{h['end_1based']}  "
                f"nCys={h['n_cys']}  cys_spacings={h['cys_spacings']}"
            )
            print(f"    motif: {h['motif']}")

    if args.json:
        args.json.write_text(json.dumps(all_results, indent=2))
        print(f"\nWrote JSON: {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
