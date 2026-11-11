"""Global alignment of dog A0A8I3PI07 against human CNNM4 (Q6P4Q7) and paralogs.

Reads sequences from the cached UniProt flat files in the repo (no network).
Reports identity/similarity, length, and gap blocks (insertions/deletions)
relative to human CNNM4, plus identity to human CNNM1/2/3 if their records
are cached, to confirm orthology vs paralogy.

Run: uv run python compare_to_human_mouse_cnnm4.py   (from this folder)
"""
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENES = HERE.parents[2]
TARGET = GENES / "CANLF/A0A8I3PI07/A0A8I3PI07-uniprot.txt"
COMPARATORS = {
    "human CNNM4 Q6P4Q7": GENES / "human/CNNM4/CNNM4-uniprot.txt",
    "human CNNM2 Q9H8M5": GENES / "human/CNNM2/CNNM2-uniprot.txt",
    "human CNNM1": GENES / "human/CNNM1/CNNM1-uniprot.txt",
    "human CNNM3": GENES / "human/CNNM3/CNNM3-uniprot.txt",
}


def read_seq(path: Path) -> str:
    return str(next(SeqIO.parse(str(path), "swiss")).seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def gap_blocks(aln_t: str, aln_c: str):
    """Yield (kind, target_start, length) blocks in 1-based target coordinates."""
    pos_t = 0
    i = 0
    while i < len(aln_t):
        if aln_t[i] == "-" or aln_c[i] == "-":
            kind = "deletion_in_target" if aln_t[i] == "-" else "insertion_in_target"
            j = i
            while j < len(aln_t) and ((aln_t[j] == "-") == (kind == "deletion_in_target")) and (aln_t[j] == "-" or aln_c[j] == "-"):
                j += 1
            yield kind, pos_t + 1, j - i
            pos_t += 0 if kind == "deletion_in_target" else j - i
            i = j
        else:
            pos_t += 1
            i += 1


def main() -> None:
    t = read_seq(TARGET)
    print(f"target A0A8I3PI07 length={len(t)}")
    blosum = substitution_matrices.load("BLOSUM62")
    for name, path in COMPARATORS.items():
        if not path.exists():
            print(f"{name}: record not cached, skipped")
            continue
        c = read_seq(path)
        aln = aligner().align(t, c)[0]
        at, ac = aln[0], aln[1]
        cols = [(x, y) for x, y in zip(at, ac) if x != "-" and y != "-"]
        ident = sum(x == y for x, y in cols)
        sim = sum(blosum[x][y] > 0 for x, y in cols)
        print(f"{name}: length={len(c)} aligned={len(cols)} identity={ident/len(cols):.3f} "
              f"similarity={sim/len(cols):.3f} identity_over_target={ident/len(t):.3f}")
        if "CNNM4" in name:
            for kind, start, length in gap_blocks(at, ac):
                if length >= 3:
                    print(f"   {kind} at target pos ~{start}, length {length}")


if __name__ == "__main__":
    main()
