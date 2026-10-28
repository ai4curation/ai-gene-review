"""Align Thiobacillus denitrificans MerA (Q3SJ73) with Tn501 MerA (P00392).

Reports global identity and which Q3SJ73 residues align to the experimentally
characterised Tn501 catalytic cysteines and NmerA GMTCXXC motif.
Run: uv run python genes/THIDA/merA/merA-bioinformatics/compare_tn501.py
"""
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def fasta(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url).read().decode()
    return "".join(txt.split("\n")[1:])


q = fasta("Q3SJ73")
t = fasta("P00392")
print(f"Q3SJ73 length {len(q)}; P00392 (Tn501 MerA) length {len(t)}")

al = Align.PairwiseAligner()
al.mode = "global"
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
aln = al.align(q, t)[0]

# map target positions -> query positions
t2q = {}
ident = aligned = 0
for (qs, qe), (ts, te) in zip(*aln.aligned):
    for i in range(qe - qs):
        t2q[ts + i + 1] = qs + i + 1
        aligned += 1
        ident += q[qs + i] == t[ts + i]
print(f"aligned positions {aligned}; identical {ident}; identity {100*ident/aligned:.1f}% of aligned")

# Tn501 landmarks: locate in the P00392 sequence by motif rather than hard-coding numbers
landmarks = {}
m = re.search(r"GMTC..C", t)
landmarks["NmerA GMTCxxC first Cys"] = m.start() + 4
landmarks["NmerA GMTCxxC second Cys"] = m.start() + 7
m = re.search(r"C....C", t[100:200])
landmarks["redox-active disulfide Cys1"] = 100 + m.start() + 1
landmarks["redox-active disulfide Cys2"] = 100 + m.start() + 6
for pos in (558, 559):
    landmarks[f"Tn501 Cys{pos} (C-terminal pair)"] = pos
for name, tp in landmarks.items():
    qp = t2q.get(tp)
    print(f"{name}: P00392 {t[tp-1]}{tp} -> Q3SJ73 " + (f"{q[qp-1]}{qp}" if qp else "gap"))
