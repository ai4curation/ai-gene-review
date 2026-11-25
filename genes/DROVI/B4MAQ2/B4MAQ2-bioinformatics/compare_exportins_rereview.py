"""Global pairwise identity of B4MAQ2 against characterised exportins.

Fetches sequences from UniProt REST and aligns with Biopython PairwiseAligner
(BLOSUM62, gap open -10, extend -0.5). Prints identity over aligned columns.

Run: uv run --with biopython --with requests python compare_exportins_rereview.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "B4MAQ2": "D. virilis target (Dvir GJ15622)",
    "Q9VWE7": "D. melanogaster Ranbp21/Exp5 (PTHR11223:SF3)",
    "Q9HAV4": "Human XPO5 (PTHR11223:SF3)",
    "O14980": "Human XPO1/CRM1 (PTHR11223:SF2)",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    return lines[0], "".join(lines[1:])


def identity(a: str, b: str) -> tuple[float, int]:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    aln = al.align(a, b)[0]
    ident = 0
    cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += a[i] == b[j]
    return ident / cols, cols


seqs = {}
for acc in ACCS:
    header, seq = fetch(acc)
    seqs[acc] = seq
    print(f"{acc}\tlen={len(seq)}\t{header[:90]}")

target = seqs["B4MAQ2"]
for acc, desc in ACCS.items():
    if acc == "B4MAQ2":
        continue
    pid, cols = identity(target, seqs[acc])
    print(f"B4MAQ2 vs {acc} ({desc}): identity={pid:.3f} over {cols} aligned columns")
