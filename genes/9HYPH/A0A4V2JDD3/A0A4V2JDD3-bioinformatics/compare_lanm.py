"""Compare Hans-LanM (A0A4V2JDD3) with Mex-LanM (C5B164).

Reads both sequences from the cached UniProt flat files in this repository,
locates candidate 12-residue EF-hand loops by the canonical N/D-x-D/N-x-D/N/S
start pattern, reports position-2 residues, and computes a global pairwise
identity (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5) over
full-length and signal-peptide-free (24-133) sequences.

Usage (from repository root):
  uv run python genes/9HYPH/A0A4V2JDD3/A0A4V2JDD3-bioinformatics/compare_lanm.py
"""
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "Hans-LanM A0A4V2JDD3": ROOT / "genes/9HYPH/A0A4V2JDD3/A0A4V2JDD3-uniprot.txt",
    "Mex-LanM C5B164": ROOT / "genes/METEA/lanM/lanM-uniprot.txt",
}


def read_seq(path: Path) -> str:
    text = path.read_text()
    block = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//", 1)[0]
    return re.sub(r"\s", "", block)


def ef_loops(seq: str):
    # canonical EF loop positions 1,3,5 are D/N/S; require 12-residue window
    # with E or D at position 12 (bidentate glutamate in canonical loops).
    hits = []
    for i in range(len(seq) - 11):
        w = seq[i : i + 12]
        if w[0] in "DN" and w[2] in "DN" and w[4] in "DNS" and w[11] in "ED":
            hits.append((i + 1, w))
    return hits


def identity(a: str, b: str) -> tuple[float, int]:
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    aln = al.align(a, b)[0]
    ident = sum(
        1
        for (s1, e1), (s2, e2) in zip(*aln.aligned)
        for x, y in zip(a[s1:e1], b[s2:e2])
        if x == y
    )
    return ident, aln


def main() -> int:
    seqs = {k: read_seq(v) for k, v in FILES.items()}
    for name, s in seqs.items():
        print(f"## {name} (length {len(s)})")
        for pos, w in ef_loops(s):
            print(f"  candidate EF loop start {pos}: {w}  position2={w[1]}")
    a, b = seqs["Hans-LanM A0A4V2JDD3"], seqs["Mex-LanM C5B164"]
    for label, x, y in (("full-length", a, b), ("mature 24-133", a[23:], b[23:])):
        ident, aln = identity(x, y)
        print(f"\n## Global identity ({label}): {ident} identical residues; "
              f"{100*ident/len(x):.1f}% of Hans-LanM length, "
              f"{100*ident/aln.shape[1]:.1f}% of alignment columns")
        print(aln)
    return 0


if __name__ == "__main__":
    sys.exit(main())
