# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Align the short donkey PIKFYVE entry against the full-length donkey product of the same gene.

Usage: uv run --script compare_to_donkey_canonical_rereview.py ../PIKFYVE-uniprot.txt donkey-A0A8C4L106-canonical.fasta
Prints identity, coverage, and the canonical-sequence segments that have no partner in the short entry.
"""
import sys
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def read_seq(path):
    fmt = "swiss" if path.endswith(".txt") else "fasta"
    return str(next(SeqIO.parse(path, fmt)).seq)


short = read_seq(sys.argv[1])
canon = read_seq(sys.argv[2])
al = PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5,
                     substitution_matrix=substitution_matrices.load("BLOSUM62"))
al.end_gap_score = 0
aln = al.align(short, canon)[0]
pairs = ident = 0
covered = [False] * len(canon)
for (s0, s1), (c0, c1) in zip(*aln.aligned):
    for i, j in zip(range(s0, s1), range(c0, c1)):
        pairs += 1
        ident += short[i] == canon[j]
        covered[j] = True
gaps, start = [], None
for j, c in enumerate(covered + [True]):
    if not c and start is None:
        start = j
    elif c and start is not None:
        gaps.append((start + 1, j))
        start = None
print(f"short length {len(short)}, canonical length {len(canon)}")
print(f"paired residues {pairs}, identical {ident} ({100*ident/pairs:.2f}%)")
print(f"coverage of short {100*pairs/len(short):.2f}%, of canonical {100*pairs/len(canon):.2f}%")
print("canonical segments without a short-entry partner (len>=5):",
      [g for g in gaps if g[1] - g[0] + 1 >= 5])
