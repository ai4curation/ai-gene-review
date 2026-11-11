# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Align horse PDIA4 (A0A3Q2IEH6) to human PDIA4 (P13667) and map key features.

Reads the two UniProt flat files in this folder and the parent gene folder,
does a global alignment (BLOSUM62), reports identity/coverage and maps the
human redox-active disulfides, signal peptide and C-terminal ER retention motif
onto the horse sequence. Prints a Markdown report to stdout.
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
HORSE = HERE.parent / "PDIA4-uniprot.txt"
HUMAN = HERE / "human-P13667-uniprot.txt"


def load(path: Path) -> str:
    return str(next(SeqIO.parse(str(path), "swiss")).seq)


def main() -> None:
    horse = load(HORSE)
    human = load(HUMAN)
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(human, horse)[0]

    # map human position (1-based) -> horse position (1-based)
    hmap: dict[int, int] = {}
    pairs = 0
    ident = 0
    for (hs, he), (qs, qe) in zip(*aln.aligned):
        for i in range(he - hs):
            hmap[hs + i + 1] = qs + i + 1
            pairs += 1
            if human[hs + i] == horse[qs + i]:
                ident += 1

    print("# Horse PDIA4 (A0A3Q2IEH6) vs human PDIA4 (P13667)\n")
    print(f"Horse length: {len(horse)} aa; human length: {len(human)} aa.\n")
    print(
        f"Global alignment: {100 * ident / pairs:.2f}% identity over {pairs} paired residues; "
        f"paired coverage {100 * pairs / len(human):.1f}% of human and {100 * pairs / len(horse):.1f}% of horse.\n"
    )
    print("## Human redox-active CXXC sites mapped to horse\n")
    for a, b in [(91, 94), (206, 209), (555, 558)]:
        ha, hb = hmap.get(a), hmap.get(b)
        hmotif = human[a - 1 : b]
        qmotif = horse[ha - 1 : hb] if ha and hb else "unaligned"
        print(f"- human {a}-{b} {hmotif} -> horse {ha}-{hb} {qmotif}")
    print("\n## Termini\n")
    print(f"- human N-terminus (signal peptide 1-20): {human[:20]}")
    print(f"- horse N-terminus 1-24: {horse[:24]}")
    print(f"- human C-terminal 4 residues: {human[-4:]}")
    print(f"- horse C-terminal 4 residues: {horse[-4:]}")


if __name__ == "__main__":
    main()
