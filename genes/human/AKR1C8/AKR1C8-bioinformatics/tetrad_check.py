"""Compare the AKR catalytic tetrad of AKR1C8 (Q5T2L2) with characterized AKR1C enzymes.

The AKR1C tetrad is Asp50, Tyr55, Lys84, His117 in AKR1C1-4 numbering. AKR1C8 is
aligned to AKR1C1 with a global pairwise alignment (Biopython) and the residues at
the aligned positions are reported. Run: uv run python tetrad_check.py
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"AKR1C8": "Q5T2L2", "AKR1C1": "Q04828", "AKR1C2": "P52895", "AKR1C3": "P42330", "AKR1C4": "P17516"}
TETRAD_C1 = {"Asp": 50, "Tyr": 55, "Lys": 84, "His": 117}


def fasta(acc: str) -> str:
    txt = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode()
    return "".join(txt.splitlines()[1:])


def map_positions(ref: str, qry: str) -> dict[int, int]:
    al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a = al.align(ref, qry)[0]
    m = {}
    for (r0, r1), (q0, q1) in zip(*a.aligned):
        for k in range(r1 - r0):
            m[r0 + k + 1] = q0 + k + 1
    return m


seqs = {g: fasta(a) for g, a in ACCS.items()}
ref = seqs["AKR1C1"]
print("| gene | accession | length | identity to AKR1C1 | " + " | ".join(f"{n}{p} (AKR1C1 numbering)" for n, p in TETRAD_C1.items()) + " |")
print("|---" * (4 + len(TETRAD_C1)) + "|")
for g, s in seqs.items():
    m = map_positions(ref, s)
    ident = sum(1 for rp, qp in m.items() if ref[rp - 1] == s[qp - 1]) / len(ref)
    cells = [f"{s[m[p] - 1]}{m[p]}" if p in m else "gap" for p in TETRAD_C1.values()]
    print(f"| {g} | {ACCS[g]} | {len(s)} | {ident:.0%} | " + " | ".join(cells) + " |")
