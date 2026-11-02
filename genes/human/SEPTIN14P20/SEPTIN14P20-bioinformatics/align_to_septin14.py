"""Local alignment of RBRP (C0HM01, SEPTIN14P20 product) against human SEPTIN14 (Q6ZU15)
and SEPTIN7 (Q16181) to ask whether the 71-aa peptide is read in the parental septin frame.

Usage: python align_to_septin14.py   (fetches sequences from UniProt REST)
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    lines = urllib.request.urlopen(url).read().decode().splitlines()
    return lines[0], "".join(lines[1:])


def main():
    _, rbrp = fetch("C0HM01")
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    for acc in ["Q6ZU15", "Q16181"]:
        hdr, seq = fetch(acc)
        aln = aligner.align(rbrp, seq)[0]
        ident = sum(1 for a, b in zip(*aln) if a == b and a != "-")
        cols = sum(1 for a, b in zip(*aln) if a != "-" and b != "-")
        q = aln.aligned[0]
        print(f"== RBRP vs {hdr[:60]}")
        print(f"score={aln.score:.1f} aligned_cols={cols} identities={ident} "
              f"pct_id={100*ident/max(cols,1):.1f} rbrp_span={q[0][0]+1}-{q[-1][1]}")
        print(aln)
    print("RBRP residue 19:", rbrp[18], "| residue 63:", rbrp[62])


if __name__ == "__main__":
    main()
