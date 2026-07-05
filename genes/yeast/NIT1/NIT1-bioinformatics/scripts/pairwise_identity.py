#!/usr/bin/env python3
"""Pairwise global identity of a query vs each other sequence in an alignment.

Generic: reads an aligned FASTA, picks the sequence whose id contains --ref,
and computes, over columns where BOTH have a residue (no gap), the fraction of
identical residues to every other sequence. Nothing is hardcoded.

Usage:
    pairwise_identity.py --alignment aln.fasta --ref P40447
"""
from __future__ import annotations

import argparse
from pathlib import Path

from Bio import AlignIO


def pct_identity(a: str, b: str) -> tuple[float, int]:
    same = 0
    aligned = 0
    for x, y in zip(a, b):
        if x == "-" or y == "-":
            continue
        aligned += 1
        if x == y:
            same += 1
    if aligned == 0:
        return (0.0, 0)
    return (100.0 * same / aligned, aligned)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--alignment", required=True, type=Path)
    p.add_argument("--ref", required=True)
    args = p.parse_args()

    aln = AlignIO.read(str(args.alignment), "fasta")
    ref = None
    for rec in aln:
        if args.ref in rec.id:
            ref = rec
            break
    if ref is None:
        raise SystemExit(f"reference {args.ref!r} not in alignment")

    print(f"# reference: {ref.id}")
    print("other_seq\tpct_identity\taligned_positions")
    for rec in aln:
        if rec.id == ref.id:
            continue
        pid, n = pct_identity(str(ref.seq), str(rec.seq))
        print(f"{rec.id}\t{pid:.1f}\t{n}")


if __name__ == "__main__":
    main()
