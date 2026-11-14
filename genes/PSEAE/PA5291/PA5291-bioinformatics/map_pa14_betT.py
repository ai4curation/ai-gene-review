"""Map the PA14 BCCT loci named in Malek et al. 2011 (PMID:21478341) to PAO1 loci.

Malek et al. name BetT1, BetT2 and BetT3 by PA14 locus tags (PA14_70980,
PA14_12990, PA14_69850). This script fetches those PA14 proteins and the three
PAO1 BCCT proteins from UniProt and reports pairwise identity (global
Needleman-Wunsch, via Biopython PairwiseAligner) so the PA14 names can be
assigned to PAO1 loci. Nothing is hard-coded except the accessions.

Usage: uv run --no-project --with biopython python map_pa14_betT.py
"""
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

PA14 = {
    "PA14_70980 (BetT1)": "A0A0H2ZIB8",
    "PA14_12990 (BetT2)": "A0A0H2ZFQ2",
    "PA14_69850 (BetT3)": "A0A0H2ZJC5",
}
PAO1 = {"PA5375": "Q9HTI9", "PA3933": "Q9HX83", "PA5291": "Q9HTR3"}


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as r:
        lines = r.read().decode().splitlines()
    return "".join(lines[1:])


def identity(a, b, aligner):
    aln = aligner.align(a, b)[0]
    ident = 0
    cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += a[i] == b[j]
    return ident, cols


def main():
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    seqs = {k: fetch(v) for k, v in {**PA14, **PAO1}.items()}
    print("query\tsubject\tlen_query\tlen_subject\tidentical\taligned\tpct_identity\texact_match")
    for p14 in PA14:
        for p in PAO1:
            a, b = seqs[p14], seqs[p]
            ident, cols = identity(a, b, aligner)
            print(f"{p14}\t{p}\t{len(a)}\t{len(b)}\t{ident}\t{cols}\t{100*ident/cols:.1f}\t{a == b}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
