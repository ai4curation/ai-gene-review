"""Compare cysteines in the fibrillar collagen NC1 (C-propeptide) domain of
zebrafish col1a1a (Q6U1J5) and col1a1b (Q6PEI9), using the cached UniProt
records. Run from the repository root:

    uv run python genes/DANRE/col1a1b/col1a1b-bioinformatics/cpropeptide_cys.py
"""
import re
from Bio import Align
from Bio.Align import substitution_matrices


def seq(path):
    txt = open(path).read()
    body = txt.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", body)


def nc1_start(path):
    # first residue of the 'Fibrillar collagen NC1' DOMAIN feature
    txt = open(path).read()
    m = re.search(r"FT   DOMAIN\s+(\d+)\.\.(\d+)\nFT\s+/note=\"Fibrillar collagen NC1\"", txt)
    return int(m.group(1))


A_PATH = "genes/DANRE/col1a1a/col1a1a-uniprot.txt"
B_PATH = "genes/DANRE/col1a1b/col1a1b-uniprot.txt"
a, b = seq(A_PATH), seq(B_PATH)
sa, sb = nc1_start(A_PATH), nc1_start(B_PATH)
print(f"col1a1a length {len(a)}, NC1 starts at {sa}; col1a1b length {len(b)}, NC1 starts at {sb}")

al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score, al.mode = -10, -0.5, "global"
aln = al.align(a[sa - 1:], b[sb - 1:])[0]
ra, rb = aln[0], aln[1]
ia, ib = sa, sb
print("Cys count in NC1: col1a1a", a[sa - 1:].count("C"), "col1a1b", b[sb - 1:].count("C"))
for ca, cb in zip(ra, rb):
    if (ca == "C") != (cb == "C"):
        print(f"Cys not conserved: col1a1a {ca}{ia if ca != '-' else ''} <-> col1a1b {cb}{ib if cb != '-' else ''}")
    if ca != "-":
        ia += 1
    if cb != "-":
        ib += 1
