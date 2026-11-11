"""Align the KBase Dark Protein Atlas query CAKXSP010000006.1_105 to UniProt Q8A2H7 (BT_3328)
and report identity, differences, and the N-terminal lipoprotein signal.
Usage: python align.py <uniprot.txt> <query.fasta>"""
import sys
from Bio import Align
from Bio.Align import substitution_matrices

def uniprot_seq(path):
    lines = open(path).read().split("\n")
    i = next(k for k, l in enumerate(lines) if l.startswith("SQ "))
    return "".join("".join(l.split()) for l in lines[i + 1:] if not l.startswith("//")).strip()

def fasta_seq(path):
    return "".join(l.strip() for l in open(path) if not l.startswith(">"))

ref, qry = uniprot_seq(sys.argv[1]), fasta_seq(sys.argv[2])
al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
a = al.align(ref, qry)[0]
r, q = a[0], a[1]
cols = len(r)
ident = sum(1 for x, y in zip(r, q) if x == y and x != "-")
print(f"Q8A2H7 length {len(ref)}; query length {len(qry)}; alignment columns {cols}")
print(f"identical positions {ident}; identity {100*ident/cols:.1f}% over alignment")
diffs, ri = [], 0
for x, y in zip(r, q):
    if x != "-":
        ri += 1
    if x != y:
        diffs.append(f"{x}{ri}{y}")
print("differences (Q8A2H7 residue, position, query residue):", " ".join(diffs))
print("N-terminus Q8A2H7 1-25:", ref[:25])
print(f"lipobox Q8A2H7 residues 16-19: {ref[15:19]} (Cys19 = {ref[18]})")
print(f"residues following Cys19 (20-25): {ref[19:25]}")
print("Pfam PF16378 DUF4988 25-199 and PF16315 DUF4955 716-867 (KBase InterProScan on query)")
