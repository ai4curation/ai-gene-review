# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Compare horse GPAT2 (A0A3Q2HKJ8) with human/mouse GPAT2 and human GPAM.

Reports length, global-alignment identity, and the residues aligned to the
mouse GPAT2 HXXXXD motif (Q14DK4 205-210) and the human GPAT2 motif.
Run: uv run --script compare_sequences.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent


def load(name: str) -> str:
    return str(next(SeqIO.parse(HERE / name, "fasta")).seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def mapping(aln) -> dict[int, int]:
    """Map 1-based positions of target (seq A) to query (seq B)."""
    m: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(a1 - a0):
            m[a0 + i + 1] = b0 + i + 1
    return m


def identity(aln, s1: str, s2: str) -> tuple[int, int]:
    ident = 0
    aligned = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(a1 - a0):
            aligned += 1
            if s1[a0 + i] == s2[b0 + i]:
                ident += 1
    return ident, aligned


def main() -> None:
    horse = load("horse-A0A3Q2HKJ8.fasta")
    refs = {
        "human GPAT2 Q6NUI2": load("human-Q6NUI2.fasta"),
        "mouse GPAT2 Q14DK4": load("mouse-Q14DK4.fasta"),
        "human GPAM Q9HCL2": load("human-GPAM-Q9HCL2.fasta"),
    }
    print(f"horse A0A3Q2HKJ8 length: {len(horse)}")
    a = aligner()
    for name, ref in refs.items():
        aln = a.align(ref, horse)[0]
        ident, n = identity(aln, ref, horse)
        print(f"\n{name}: length {len(ref)}; aligned {n}; identical {ident}; "
              f"identity over aligned = {100 * ident / n:.1f}%; "
              f"identity over ref length = {100 * ident / len(ref):.1f}%")
        m = mapping(aln)
        if name.startswith("mouse GPAT2"):
            print("  mouse HXXXXD motif 205-210 -> horse:")
            for p in range(205, 211):
                hp = m.get(p)
                print(f"    mouse {ref[p - 1]}{p} -> horse "
                      f"{horse[hp - 1] + str(hp) if hp else 'gap'}")
            for lo, hi in [(306, 332), (450, 472)]:
                hp = [m[p] for p in range(lo, hi + 1) if p in m]
                print(f"  mouse predicted TM {lo}-{hi} -> horse "
                      f"{min(hp) if hp else 'gap'}-{max(hp) if hp else 'gap'}")
        # coverage of the reference N/C termini
        first = min(m) if m else None
        last = max(m) if m else None
        print(f"  ref aligned span: {first}-{last}")
    # locate HXXXXD motifs in horse
    hits = [i + 1 for i in range(len(horse) - 5)
            if horse[i] == "H" and horse[i + 5] == "D"]
    print(f"\nHXXXXD occurrences in horse: {hits}")
    for h in hits:
        print(f"  {h}: {horse[h - 1:h + 5]}")


if __name__ == "__main__":
    main()
