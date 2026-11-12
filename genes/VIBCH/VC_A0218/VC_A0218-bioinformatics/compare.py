#!/usr/bin/env python3
"""Pairwise global identity of Q9KMV0 (V. cholerae VC_A0218) against

  * AAA92960.1  - V. cholerae E7946 lecithinase Lec (Fiore et al. 1997, U50074)
  * Q68CM4      - V. parahaemolyticus Tlh / lecithin-dependent haemolysin (LDH)
  * P10480      - Aeromonas hydrophila GCAT (glycerophospholipid:cholesterol acyltransferase)
  * O33407      - P. aeruginosa EstA (the sole seed of the PTN005219546 IBD)
  * Q9HUP2      - P. aeruginosa ChoE (second seed of the GO:0052689 IBD at the same node)
  * Q9LU14      - Arabidopsis APG, a plant leaf of the same PANTHER node

Also reports the GDSL/SGNH catalytic-residue columns.

Run:  uv run python compare.py
"""

from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices
from Bio.SeqIO import parse

DATA = Path(__file__).parent / "data"

LABELS = {
    "AAA92960": "V. cholerae E7946 Lec lecithinase (Fiore 1997)",
    "Q68CM4": "V. parahaemolyticus Tlh / LDH",
    "P10480": "A. hydrophila GCAT acyltransferase",
    "O33407": "P. aeruginosa EstA (IBD seed)",
    "Q9HUP2": "P. aeruginosa ChoE",
    "Q9LU14": "A. thaliana APG (plant leaf)",
}


def load(stem: str) -> str:
    (rec,) = parse(DATA / f"{stem}.fasta", "fasta")
    return str(rec.seq)


def main() -> None:
    aligner = Align.PairwiseAligner(scoring="blastp")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.mode = "global"

    query = load("Q9KMV0")
    print(f"Q9KMV0 VC_A0218: {len(query)} aa\n")
    print(f"{'subject':48s} {'len':>5s} {'ident%':>7s} {'aln_len':>8s}")
    for stem, label in LABELS.items():
        subject = load(stem)
        aln = aligner.align(query, subject)[0]
        a, b = aln[0], aln[1]
        matches = sum(1 for x, y in zip(a, b) if x == y and x != "-")
        ungapped = sum(1 for x, y in zip(a, b) if x != "-" and y != "-")
        pct = 100.0 * matches / ungapped if ungapped else 0.0
        print(f"{label:48s} {len(subject):5d} {pct:7.1f} {ungapped:8d}")

    # GDSL block in Q9KMV0
    i = query.find("GDSL")
    print(f"\nGDSL motif in Q9KMV0 at residues {i + 1}-{i + 4}: "
          f"{query[i - 6:i + 10]} (catalytic Ser = S{i + 3})")


if __name__ == "__main__":
    main()
