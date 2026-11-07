"""Global pairwise identity between UniProt sequences.

Usage: uv run python pairwise_identity.py ACC1 ACC2 [ACC3 ...]
Fetches each sequence from the UniProt REST API, aligns every pair with
Biopython's PairwiseAligner (global, BLOSUM62, gap open -10, extend -0.5),
and prints identity over aligned columns and over the shorter sequence.
"""
import sys
import urllib.request
from itertools import combinations

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from io import StringIO


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        return SeqIO.read(StringIO(fh.read().decode()), "fasta")


def main(accs):
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    seqs = {a: fetch(a) for a in accs}
    for a, b in combinations(accs, 2):
        sa, sb = str(seqs[a].seq), str(seqs[b].seq)
        aln = aligner.align(sa, sb)[0]
        ident = cols = 0
        for (s1, e1), (s2, e2) in zip(*aln.aligned):
            for i, j in zip(range(s1, e1), range(s2, e2)):
                cols += 1
                ident += sa[i] == sb[j]
        print(f"{a}({len(sa)} aa) vs {b}({len(sb)} aa): identical={ident} "
              f"aligned_cols={cols} id_aligned={100*ident/cols:.1f}% "
              f"id_shorter={100*ident/min(len(sa), len(sb)):.1f}%")


if __name__ == "__main__":
    main(sys.argv[1:])
