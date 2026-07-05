#!/usr/bin/env python3
"""Report residues at given (1-based) positions in a protein FASTA.

Generic tool: it takes a FASTA file and a list of 1-based positions and prints
the residue found at each position. It is used here to check whether the
nitrilase-superfamily catalytic triad (canonically Glu ... Lys ... Cys, the
"E-K-C" triad) is present at the positions UniProt/PROSITE predicts for a given
protein. NO positions or residues are hardcoded to a specific gene; everything
is passed on the command line so the same script works for any protein.

Usage:
    catalytic_triad.py --fasta seq.fasta --positions 44,135,169 \
        --expected E,K,C
"""
from __future__ import annotations

import argparse
from pathlib import Path

from Bio import SeqIO

# One-letter -> full residue name, used only for human-readable output.
AA3 = {
    "A": "Ala", "R": "Arg", "N": "Asn", "D": "Asp", "C": "Cys",
    "E": "Glu", "Q": "Gln", "G": "Gly", "H": "His", "I": "Ile",
    "L": "Leu", "K": "Lys", "M": "Met", "F": "Phe", "P": "Pro",
    "S": "Ser", "T": "Thr", "W": "Trp", "Y": "Tyr", "V": "Val",
}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fasta", required=True, type=Path)
    p.add_argument(
        "--positions",
        required=True,
        help="Comma-separated 1-based positions, e.g. 44,135,169",
    )
    p.add_argument(
        "--expected",
        default=None,
        help="Comma-separated expected 1-letter residues aligned to --positions",
    )
    args = p.parse_args()

    positions = [int(x) for x in args.positions.split(",")]
    expected = args.expected.split(",") if args.expected else [None] * len(positions)
    if len(expected) != len(positions):
        raise SystemExit("--expected must have same length as --positions")

    record = next(SeqIO.parse(str(args.fasta), "fasta"))
    seq = str(record.seq)
    print(f"# sequence: {record.id}  (length {len(seq)} aa)")
    print("pos\tresidue\tname\texpected\tmatch\tcontext(±5)")
    for pos, exp in zip(positions, expected):
        if pos < 1 or pos > len(seq):
            print(f"{pos}\tOUT_OF_RANGE\t-\t{exp or '-'}\t-\t-")
            continue
        aa = seq[pos - 1]
        lo = max(0, pos - 6)
        hi = min(len(seq), pos + 5)
        ctx = seq[lo:hi]
        match = "" if exp is None else ("YES" if aa == exp else "NO")
        print(f"{pos}\t{aa}\t{AA3.get(aa, '?')}\t{exp or '-'}\t{match}\t{ctx}")


if __name__ == "__main__":
    main()
