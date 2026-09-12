#!/usr/bin/env python3
"""Analyse a MAFFT protein alignment for catalytic-triad conservation and coverage.

Generic: given an aligned FASTA and the id of a reference sequence plus a set of
1-based *ungapped* positions in that reference, it maps each reference position
to an alignment column and reports the residue every other sequence has in that
column. This lets us ask, without hardcoding anything, whether the residues at
the reference's predicted catalytic positions are conserved across the family,
and how far each sequence extends relative to the reference (a proxy for
truncation).

Usage:
    analyze_alignment.py --alignment aln.fasta --ref REFID \
        --ref-positions 44,135,169 --labels E,K,C
"""
from __future__ import annotations

import argparse
from pathlib import Path

from Bio import AlignIO


def ungapped_to_column(aln_seq: str, ungapped_pos: int) -> int | None:
    """Map a 1-based ungapped position to a 0-based alignment column."""
    count = 0
    for col, ch in enumerate(aln_seq):
        if ch != "-":
            count += 1
            if count == ungapped_pos:
                return col
    return None


def coverage(aln_seq: str) -> tuple[int, int, int]:
    """Return (first_col, last_col, n_residues) of non-gap span."""
    residue_cols = [i for i, ch in enumerate(aln_seq) if ch != "-"]
    if not residue_cols:
        return (-1, -1, 0)
    return (residue_cols[0], residue_cols[-1], len(residue_cols))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--alignment", required=True, type=Path)
    p.add_argument("--ref", required=True, help="id (or id substring) of reference seq")
    p.add_argument("--ref-positions", required=True, help="comma-separated 1-based ungapped positions in ref")
    p.add_argument("--labels", default=None, help="comma-separated labels for positions, e.g. E,K,C")
    args = p.parse_args()

    aln = AlignIO.read(str(args.alignment), "fasta")
    positions = [int(x) for x in args.ref_positions.split(",")]
    labels = args.labels.split(",") if args.labels else [""] * len(positions)

    ref_rec = None
    for rec in aln:
        if args.ref in rec.id:
            ref_rec = rec
            break
    if ref_rec is None:
        raise SystemExit(f"reference {args.ref!r} not found in alignment")

    aln_len = aln.get_alignment_length()
    print(f"# alignment: {aln_len} columns, {len(aln)} sequences")
    print(f"# reference: {ref_rec.id}")

    # Map ref positions to columns.
    cols = []
    for pos, lab in zip(positions, labels):
        col = ungapped_to_column(str(ref_rec.seq), pos)
        cols.append(col)
        print(f"# ref position {pos} ({lab}) -> alignment column {None if col is None else col + 1}")

    print()
    print("## Catalytic-triad column occupancy across all sequences")
    header = ["seq_id"] + [f"col{c+1 if c is not None else 'NA'}({labels[i] or positions[i]})" for i, c in enumerate(cols)]
    print("\t".join(header))
    for rec in aln:
        row = [rec.id]
        s = str(rec.seq)
        for col in cols:
            row.append("-" if col is None else (s[col] if col < len(s) else "?"))
        print("\t".join(row))

    print()
    print("## Coverage / span per sequence (proxy for truncation)")
    print("seq_id\tfirst_col\tlast_col\tn_residues")
    for rec in aln:
        first, last, n = coverage(str(rec.seq))
        print(f"{rec.id}\t{first+1}\t{last+1}\t{n}")


if __name__ == "__main__":
    main()
