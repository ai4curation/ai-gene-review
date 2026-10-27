# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Global alignment of horse FOXJ3 (F6SCJ5) against reviewed human (Q9UPW0) and mouse (Q8BUR3) FOXJ3.

Reads sequences from the UniProt flat files in this folder and prints identity,
gaps, and conservation of the fork-head domain (horse 78-173, per PROSITE PS50039).
"""
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
FH = (78, 173)


def load(path: Path) -> str:
    return str(next(SeqIO.parse(path, "swiss")).seq)


def main() -> None:
    horse = load(HERE.parent / "FOXJ3-uniprot.txt")
    aligner = PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    print(f"horse F6SCJ5 length: {len(horse)}")
    for name, fn in [("human Q9UPW0", "human-Q9UPW0-uniprot.txt"), ("mouse Q8BUR3", "mouse-Q8BUR3-uniprot.txt")]:
        other = load(HERE / fn)
        aln = aligner.align(horse, other)[0]
        a, b = aln[0], aln[1]
        cols = len(a)
        ident = sum(1 for x, y in zip(a, b) if x == y and x != "-")
        gaps_h = a.count("-")
        gaps_o = b.count("-")
        # fork-head region in horse coordinates
        hpos = 0
        fh_ident = fh_len = fh_gaps = 0
        for x, y in zip(a, b):
            if x != "-":
                hpos += 1
            if FH[0] <= hpos <= FH[1] and x != "-":
                fh_len += 1
                if y == "-":
                    fh_gaps += 1
                elif x == y:
                    fh_ident += 1
        print(f"\n== horse vs {name} (length {len(other)})")
        print(f"alignment columns: {cols}; identical: {ident}; identity over horse length: {100*ident/len(horse):.1f}%")
        print(f"gap columns in horse: {gaps_h}; in {name}: {gaps_o}")
        print(f"fork-head 78-173: {fh_ident}/{fh_len} identical, {fh_gaps} gaps")


if __name__ == "__main__":
    main()
