# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Compare horse SLC27A5 (A0A5F5PXH2) with characterised SLC27A5 orthologs and the
SLC27A2 paralog, and check conservation of the AMP-binding (ATP/AMP P-loop) motif.

Run from this directory:
    uv run --script compare_orthologs.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
QUERY = "A0A5F5PXH2"
OTHERS = {
    "Q9Y2P5": "human SLC27A5 (PTHR43107:SF25)",
    "Q4LDG0": "mouse Slc27a5 (PTHR43107:SF25)",
    "O14975": "human SLC27A2 (paralog, different subfamily)",
}
# Human SLC27A5 AMP-binding region annotated in UniProt Q9Y2P5 (residues 292-303).
HUMAN_MOTIF_START, HUMAN_MOTIF_END = 292, 303


def load(acc: str) -> str:
    return str(next(SeqIO.parse(HERE / f"{acc}.fasta", "fasta")).seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def identity(aln) -> tuple[int, int]:
    pairs = ident = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            pairs += 1
            ident += aln.target[i] == aln.query[j]
    return pairs, ident


def map_position(aln, pos_in_query_1based: int) -> int | None:
    """Map a 1-based position in the aligned 'query' (second) sequence to the target."""
    p = pos_in_query_1based - 1
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        if s2 <= p < e2:
            return s1 + (p - s2) + 1
    return None


def main() -> None:
    q = load(QUERY)
    print(f"{QUERY} length {len(q)}")
    a = aligner()
    for acc, label in OTHERS.items():
        s = load(acc)
        aln = a.align(q, s)[0]
        pairs, ident = identity(aln)
        print(f"\n## {QUERY} vs {acc} {label} (len {len(s)})")
        print(f"aligned pairs {pairs}; identical {ident}; identity {100 * ident / pairs:.2f}%")
        if acc == "Q9Y2P5":
            hs = s[HUMAN_MOTIF_START - 1 : HUMAN_MOTIF_END]
            qs_start = map_position(aln, HUMAN_MOTIF_START)
            qs_end = map_position(aln, HUMAN_MOTIF_END)
            if qs_start is None or qs_end is None:
                print("AMP-binding motif: could not be mapped (gap at an end)")
            else:
                hq = q[qs_start - 1 : qs_end]
                print(
                    f"AMP-binding motif human {HUMAN_MOTIF_START}-{HUMAN_MOTIF_END} {hs}; "
                    f"horse {qs_start}-{qs_end} {hq}; identical={hs == hq}"
                )


if __name__ == "__main__":
    main()
