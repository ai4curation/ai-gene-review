#!/usr/bin/env python3
"""Compute pairwise % identity of SET6 vs each panel protein (global alignment).

Uses Biopython's PairwiseAligner (Needleman-Wunsch, BLOSUM62). Reports identity and
alignment coverage so we can see which panel member is SET6's closest relative
(expected: its SMYD paralog Set5). No conclusions are hardcoded.
"""
from __future__ import annotations

import sys
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
DATA = PROJ / "data"
RESULTS = PROJ / "results"


def main() -> int:
    recs = {r.id: str(r.seq) for r in SeqIO.parse(DATA / "reference_sequences.fasta", "fasta")}
    set6_id = [i for i in recs if i.startswith("Q12529")][0]
    set6 = recs[set6_id]

    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"

    lines = ["# Pairwise identity: SET6 vs panel", "",
             f"Reference: {set6_id} ({len(set6)} aa)", "",
             f"{'protein':22s} {'len':>5s} {'score':>8s} {'ident':>6s} {'%id':>6s} {'alnlen':>7s}"]
    results = []
    for rid, seq in recs.items():
        if rid == set6_id:
            continue
        aln = aligner.align(set6, seq)[0]
        a, b = aln[0], aln[1]
        idents = sum(1 for x, y in zip(a, b) if x == y and x != "-")
        alnlen = sum(1 for x, y in zip(a, b) if x != "-" and y != "-")
        pid = 100.0 * idents / alnlen if alnlen else 0.0
        results.append((pid, rid, len(seq), aln.score, idents, alnlen))

    for pid, rid, ln, score, idents, alnlen in sorted(results, reverse=True):
        lines.append(f"{rid:22s} {ln:5d} {score:8.1f} {idents:6d} {pid:6.1f} {alnlen:7d}")

    text = "\n".join(lines) + "\n"
    (RESULTS / "pairwise_identity.txt").write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
