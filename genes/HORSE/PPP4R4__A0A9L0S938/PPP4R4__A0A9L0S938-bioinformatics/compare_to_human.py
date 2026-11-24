"""Global alignment of horse PPP4R4 canonical (A0A9L0S938) with human PPP4R4 (Q6NUP7)
and the horse benchmark isoform (A0A9L0S961), using the cached UniProt flat files.

Run from the repository root:
    uv run python genes/HORSE/PPP4R4__A0A9L0S938/PPP4R4__A0A9L0S938-bioinformatics/compare_to_human.py
"""

import json
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

FILES = {
    "A0A9L0S938_horse_canonical": "genes/HORSE/PPP4R4__A0A9L0S938/PPP4R4__A0A9L0S938-uniprot.txt",
    "Q6NUP7_human": "genes/human/PPP4R4/PPP4R4-uniprot.txt",
    "A0A9L0S961_horse_isoform": "genes/HORSE/PPP4R4/PPP4R4-uniprot.txt",
}


def load(path: str) -> str:
    return str(next(SeqIO.parse(path, "swiss")).seq)


def compare(a: str, b: str) -> dict:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.end_gap_score = 0
    aln = aligner.align(a, b)[0]
    pairs = ident = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            pairs += 1
            ident += a[i] == b[j]
    return {
        "len_a": len(a),
        "len_b": len(b),
        "aligned_pairs": pairs,
        "identity_pct": round(100 * ident / pairs, 1),
        "coverage_of_b_pct": round(100 * pairs / len(b), 1),
        "c_terminal_a": a[-15:],
        "c_terminal_b": b[-15:],
    }


def main() -> None:
    seqs = {k: load(v) for k, v in FILES.items()}
    q = seqs["A0A9L0S938_horse_canonical"]
    out = {
        "vs_human_Q6NUP7": compare(q, seqs["Q6NUP7_human"]),
        "vs_horse_A0A9L0S961": compare(q, seqs["A0A9L0S961_horse_isoform"]),
    }
    print(json.dumps(out, indent=2))
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
