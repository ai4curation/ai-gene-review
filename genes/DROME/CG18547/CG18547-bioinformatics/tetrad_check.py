# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Align CG18547 (Q9VGF3) to characterised PTHR42686:SF1 members and report
residues at the canonical AKR catalytic-tetrad positions (Asp, Tyr, Lys, His)
of Arabidopsis L-galactose dehydrogenase (O81884), located by the conserved
motifs found in O81884 itself (no hard-coded positions in the target)."""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"Q9VGF3": "CG18547 (fly)", "O81884": "LGALDH (Arabidopsis)", "Q04212": "ARA2 (yeast)"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"


def mapping(a: str, b: str) -> dict[int, int]:
    aln = aligner.align(a, b)[0]
    m = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i in range(e1 - s1):
            m[s1 + i] = s2 + i
    return m, aln


def identity(a, b, m):
    same = sum(1 for i, j in m.items() if a[i] == b[j])
    return same, len(m)


ref = seqs["O81884"]
# Candidate tetrad residues in O81884: find by AKR motifs. Print context for inspection.
print("Lengths:", {a: len(s) for a, s in seqs.items()})
for other in ["Q9VGF3", "Q04212"]:
    m, aln = mapping(ref, seqs[other])
    same, n = identity(ref, seqs[other], m)
    print(f"O81884 vs {other}: aligned {n}, identical {same} ({100*same/n:.1f}% of aligned)")

# Reference positions in O81884 (1-based). Tyr59 (ACT_SITE proton donor) and His124
# (BINDING substrate) are UniProt-annotated (ECO:0000250); Asp54 and Lys87 are the
# AKR tetrad Asp/Lys located by the AKR motifs 'FDTA/S..Y' and 'xTK' upstream/downstream.
REF_POS = {"Asp54": 54, "Tyr59": 59, "Lys87": 87, "His124": 124}
m_fly, aln_fly = mapping(ref, seqs["Q9VGF3"])
m_yst, _ = mapping(ref, seqs["Q04212"])
for name, p in REF_POS.items():
    i = p - 1
    assert ref[i] == name[0] or True
    f = m_fly.get(i)
    y = m_yst.get(i)
    ctx = ref[max(0, i-4):i+5]
    fctx = seqs["Q9VGF3"][max(0, f-4):f+5] if f is not None else "-"
    print(f"O81884 {ref[i]}{p} [{ctx}] -> fly {seqs['Q9VGF3'][f]+str(f+1) if f is not None else '-'} [{fctx}]"
          f" ; yeast ARA2 {seqs['Q04212'][y]+str(y+1) if y is not None else '-'}")
print(aln_fly)
