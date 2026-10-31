# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Align mec-14 (Q20127) to characterised PTHR42686:SF1 members and to its fly
co-orthologs, and report the residues at the AKR catalytic-tetrad positions
(Asp, Tyr, Lys, His) of Arabidopsis L-galactose dehydrogenase (O81884).

Reference positions in O81884 (1-based): Tyr59 (UniProt ACT_SITE proton donor),
His124 (UniProt substrate-binding), and the tetrad Asp54 and Lys87. The script
prints the reference residue at each position so the reference can be checked,
and prints the full mec-14 alignment for inspection. Nothing is hard-coded in
the target sequences."""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "O81884": "LGALDH (Arabidopsis)",
    "Q20127": "mec-14 (C. elegans)",
    "Q04212": "ARA2 (yeast)",
    "Q9VGF3": "CG18547 (fly)",
    "Q9VGF2": "CG12224 (fly)",
}
REF_POS = {"Asp": 54, "Tyr": 59, "Lys": 87, "His": 124}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"


def mapping(a: str, b: str):
    aln = aligner.align(a, b)[0]
    m = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i in range(e1 - s1):
            m[s1 + i] = s2 + i
    return m, aln


seqs = {a: fetch(a) for a in ACCS}
ref = seqs["O81884"]
print("Lengths:", {f"{a} {ACCS[a]}": len(s) for a, s in seqs.items()})
print("Reference residues in O81884:", {f"{k}{p}": ref[p - 1] for k, p in REF_POS.items()})

for acc in ["Q20127", "Q04212", "Q9VGF3", "Q9VGF2"]:
    m, _ = mapping(ref, seqs[acc])
    same = sum(1 for i, j in m.items() if ref[i] == seqs[acc][j])
    print(f"\nO81884 vs {acc} {ACCS[acc]}: aligned {len(m)}, identical {same} ({100*same/len(m):.1f}%)")
    for name, p in REF_POS.items():
        i = p - 1
        j = m.get(i)
        if j is None:
            print(f"  {ref[i]}{p}: gap in {acc}")
        else:
            print(f"  {ref[i]}{p} [{ref[max(0,i-4):i+5]}] -> {seqs[acc][j]}{j+1} [{seqs[acc][max(0,j-4):j+5]}]")

# Pairwise identity of mec-14 to the other members (mec-14 as query)
print()
for acc in ["Q04212", "Q9VGF3", "Q9VGF2"]:
    m, _ = mapping(seqs["Q20127"], seqs[acc])
    same = sum(1 for i, j in m.items() if seqs["Q20127"][i] == seqs[acc][j])
    print(f"Q20127 vs {acc}: aligned {len(m)}, identical {same} ({100*same/len(m):.1f}%)")

_, aln = mapping(ref, seqs["Q20127"])
print("\nAlignment O81884 (target) vs Q20127 (query):")
print(aln)
