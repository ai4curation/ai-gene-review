"""Global pairwise alignment of KT2440 DgcA/DgcB with the characterized
Chromohalobacter DdhC/Csal_0991 proteins, read from the cached UniProt flat files.

Run from the repository root:
    uv run python genes/PSEPK/dgcA/dgcA-bioinformatics/pairwise_orthologs.py
"""
import re
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
PAIRS = [
    ("genes/PSEPK/dgcA/dgcA-uniprot.txt", "genes/CHRI1/ddhC/ddhC-uniprot.txt"),
    ("genes/PSEPK/dgcB/dgcB-uniprot.txt", "genes/CHRI1/Csal_0991/Csal_0991-uniprot.txt"),
]


def read_seq(path: Path) -> tuple[str, str]:
    acc, seq, in_sq = None, [], False
    for line in path.read_text().splitlines():
        if line.startswith("AC   ") and acc is None:
            acc = line[5:].split(";")[0].strip()
        elif line.startswith("SQ   "):
            in_sq = True
        elif line.startswith("//"):
            break
        elif in_sq:
            seq.append(line.replace(" ", ""))
    return acc, "".join(seq)


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    print("query\tquery_len\ttarget\ttarget_len\taligned_cols\tidentical\tpct_identity_over_aligned\tpct_identity_over_shorter")
    for q, t in PAIRS:
        qa, qs = read_seq(ROOT / q)
        ta, ts = read_seq(ROOT / t)
        aln = aligner.align(qs, ts)[0]
        counts = aln.counts()
        aligned = counts.identities + counts.mismatches
        print(
            f"{qa}\t{len(qs)}\t{ta}\t{len(ts)}\t{aligned}\t{counts.identities}\t"
            f"{100 * counts.identities / aligned:.1f}\t{100 * counts.identities / min(len(qs), len(ts)):.1f}"
        )


def motif_scan() -> None:
    """List 4Fe-4S ferredoxin-type cysteine motifs (CxxCxxCxxxC) in DgcB and Csal_0991."""
    print("\naccession\tmotif_start\tmotif")
    for path in ("genes/PSEPK/dgcB/dgcB-uniprot.txt", "genes/CHRI1/Csal_0991/Csal_0991-uniprot.txt"):
        acc, seq = read_seq(ROOT / path)
        for m in re.finditer(r"C..C..C...C", seq):
            print(f"{acc}\t{m.start() + 1}\t{m.group()}")


if __name__ == "__main__":
    main()
    motif_scan()
