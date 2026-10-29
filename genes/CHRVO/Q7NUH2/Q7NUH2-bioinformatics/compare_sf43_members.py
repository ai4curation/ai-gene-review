# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Pairwise global identity of CV_2726 (Q7NUH2) against characterized MarR proteins,
inside and outside its PANTHER subfamily (PTHR33164:SF43), with PANTHER placement
read live from UniProt. Also reports CV_2726 genomic neighbours from KEGG."""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q7NUH2"
COMPARATORS = ["P9WME9", "Q9F4G3", "P70993", "O33817", "P27245", "O31541"]


def fetch(acc):
    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).text
    seq = "".join(l[5:].replace(" ", "") for l in txt.splitlines() if l.startswith("     "))
    gn = next((l[5:] for l in txt.splitlines() if l.startswith("GN ")), "")
    os_ = next((l[5:] for l in txt.splitlines() if l.startswith("OS ")), "")
    panther = [l.split(";")[1].strip() for l in txt.splitlines() if l.startswith("DR   PANTHER")]
    return seq, gn.strip(), os_.strip(), panther


aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

tseq, tgn, tos, tpan = fetch(TARGET)
print(f"# Target {TARGET} len={len(tseq)} PANTHER={';'.join(tpan)}")
print("accession\tgene\torganism\tlength\tPANTHER\taligned_pairs\tidentity_pct_of_shorter")
for acc in COMPARATORS:
    seq, gn, os_, pan = fetch(acc)
    aln = aligner.align(tseq, seq)[0]
    ident = pairs = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i, j in zip(range(a0, a1), range(b0, b1)):
            pairs += 1
            ident += tseq[i] == seq[j]
    pct = 100 * ident / min(len(tseq), len(seq))
    print(f"{acc}\t{gn[:40]}\t{os_[:40]}\t{len(seq)}\t{';'.join(pan)}\t{pairs}\t{pct:.1f}")

print("\n# KEGG genomic neighbourhood of cvi:CV_2726")
for n in range(2722, 2731):
    print(requests.get(f"https://rest.kegg.jp/list/cvi:CV_{n}", timeout=60).text.strip())
