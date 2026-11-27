# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Percent identity of horse F6W2H6 vs human Q9P275 within a human-coordinate window.

Usage: uv run --script domain_identity.py <query_uniprot.txt> <human.fasta> <start> <end>
Global alignment (BLOSUM62, open -10, extend -0.5); counts identical aligned pairs
whose human position falls in [start, end] (1-based).
"""
import sys
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices


def parse_flat(path):
    seq, inseq = [], False
    for line in open(path):
        if line.startswith("SQ"):
            inseq = True
            continue
        if line.startswith("//"):
            break
        if inseq:
            seq.append("".join(line.split()))
    return "".join(seq)


q = parse_flat(sys.argv[1])
h = str(next(SeqIO.parse(sys.argv[2], "fasta")).seq)
start, end = int(sys.argv[3]), int(sys.argv[4])
al = Align.PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                           open_gap_score=-10, extend_gap_score=-0.5)
a = al.align(q, h)[0]
pairs = ident = 0
for (qs, qe), (hs, he) in zip(*a.aligned):
    for i, j in zip(range(qs, qe), range(hs, he)):
        if start <= j + 1 <= end:
            pairs += 1
            ident += q[i] == h[j]
print(f"human {start}-{end}: aligned pairs {pairs}, identical {ident}, identity {100*ident/pairs:.2f}%")
