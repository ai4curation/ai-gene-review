# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Re-review check of the donkey GPC3 (A0A9L0J2B1) N-terminus against human GPC3 (P51654).

Finds where the shared conserved core begins (first exact 10-mer shared by the two
sequences), then reports identity of the segments before and after that anchor, and a
local alignment of the two N-terminal segments, to test whether the donkey gene model
carries the human signal peptide (P51654 FT SIGNAL 1..24).

Usage (from this folder):
    uv run --script compare_nterm_rereview.py ../GPC3-uniprot.txt human-GPC3-P51654.fasta
"""

import sys

from Bio import Align
from Bio.Align import substitution_matrices


def read_uniprot_flat(path: str) -> str:
    seq, in_sq = [], False
    for line in open(path):
        if line.startswith("SQ "):
            in_sq = True
            continue
        if in_sq:
            if line.startswith("//"):
                break
            seq.append("".join(line.split()))
    return "".join(seq)


def read_fasta(path: str) -> str:
    return "".join(line.strip() for line in open(path) if not line.startswith(">"))


def first_shared_kmer(a: str, b: str, k: int = 10) -> tuple[int, int]:
    kmers = {b[i : i + k]: i for i in range(len(b) - k + 1)}
    for i in range(len(a) - k + 1):
        if a[i : i + k] in kmers:
            return i, kmers[a[i : i + k]]
    raise ValueError("no shared k-mer")


def global_identity(a: str, b: str) -> tuple[int, int]:
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = paired = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for x, y in zip(a[s1:e1], b[s2:e2]):
            paired += 1
            ident += x == y
    return ident, paired


def main(donkey_path: str, human_path: str) -> None:
    donkey = read_uniprot_flat(donkey_path)
    human = read_fasta(human_path)
    d0, h0 = first_shared_kmer(donkey, human)
    print(f"Donkey length {len(donkey)}; human length {len(human)}")
    print(f"First shared 10-mer: donkey {d0 + 1}, human {h0 + 1} ({donkey[d0:d0 + 10]})")
    print(f"Donkey N-terminal segment 1..{d0}: {donkey[:d0]}")
    print(f"Human N-terminal segment 1..{h0}: {human[:h0]}")
    i, p = global_identity(donkey[:d0], human[:h0])
    print(f"N-terminal segments, global alignment: {i}/{p} identical paired residues")
    local = Align.PairwiseAligner(mode="local")
    local.substitution_matrix = substitution_matrices.load("BLOSUM62")
    local.open_gap_score = -10
    local.extend_gap_score = -0.5
    print(f"N-terminal segments, best local alignment score: {local.score(donkey[:d0], human[:h0]):.1f}")
    i2, p2 = global_identity(donkey[d0:], human[h0:])
    print(
        f"Downstream of anchor: {i2}/{p2} identical paired residues "
        f"({100 * i2 / p2:.2f}%)"
    )
    print(f"Human signal peptide (FT SIGNAL 1..24): {human[:24]}")
    print(f"Human signal peptide present verbatim in donkey: {human[:24] in donkey}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
