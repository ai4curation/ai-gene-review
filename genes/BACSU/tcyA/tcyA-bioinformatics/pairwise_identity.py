"""Global pairwise identity of TcyA (P42199) to comparators, and the TcyA residues
aligned to Ngo0372 (Q5F9M1) Tyr59 and Trp97, binding-pocket residues tested by
mutagenesis in PMID:22138345. The paper's numbering need not match UniProt precursor
numbering, so the residues are located in the UniProt sequence as Tyr/Trp pairs with the
paper's spacing (97 - 59 = 38); every such pair is reported.

Usage (from repo root): uv run python genes/BACSU/tcyA/tcyA-bioinformatics/pairwise_identity.py
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "P42199"
COMPARATORS = ["D3VIU4", "P42400", "O34406", "P0AEM9", "Q5F9M1"]
PAPER_TYR, PAPER_TRP = 59, 97


def seq(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as fh:
        lines = fh.read().decode().splitlines()
    return "".join(lines[1:])


aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

t = seq(TARGET)
print("comparator\tidentity_over_aligned_columns\taligned_columns")
alns = {}
for acc in COMPARATORS:
    s = seq(acc)
    aln = aligner.align(t, s)[0]
    alns[acc] = (aln, s)
    ident = cols = 0
    for (ts, te), (ss, se) in zip(*aln.aligned):
        for i, j in zip(range(ts, te), range(ss, se)):
            cols += 1
            ident += t[i] == s[j]
    print(f"{acc}\t{ident / cols:.3f}\t{cols}")

aln, s = alns["Q5F9M1"]
spacing = PAPER_TRP - PAPER_TYR
pairs = [i + 1 for i in range(len(s) - spacing) if s[i] == "Y" and s[i + spacing] == "W"]
print(f"\nNgo0372 Tyr/Trp pairs with spacing {spacing} (UniProt numbering of Tyr): {pairs}")
positions = [p for y in pairs for p in (y, y + spacing)]
print("Ngo0372_pos\tNgo0372_res\tTcyA_pos\tTcyA_res")
for pos in positions:
    hit = None
    for (ts, te), (ss, se) in zip(*aln.aligned):
        if ss <= pos - 1 < se:
            i = ts + (pos - 1 - ss)
            hit = (i + 1, t[i])
    print(f"{pos}\t{s[pos - 1]}\t{hit[0] if hit else 'gap'}\t{hit[1] if hit else '-'}")
