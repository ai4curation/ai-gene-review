"""Global pairwise identity of fly Rhp (Q9XYY9) to vertebrate rhophilins.

Fetches sequences from UniProt REST and runs Needleman-Wunsch (BLOSUM62,
gap open -10, extend -0.5) with Biopython. Identity = identical aligned
positions / aligned columns excluding double gaps.

Run: uv run --with biopython --with requests python compare_rhophilins_rereview.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"Q9XYY9": "fly Rhp", "Q8IUC4": "human RHPN2", "Q8TCX5": "human RHPN1",
        "Q61085": "mouse Rhpn1", "Q8BWR8": "mouse Rhpn2"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    cols = sum(1 for x, y in zip(s1, s2) if not (x == "-" and y == "-"))
    return ident / cols, cols


seqs = {acc: fetch(acc) for acc in ACCS}
for acc in ACCS:
    print(f"{acc}\t{ACCS[acc]}\tlength={len(seqs[acc])}")
print("pair\tidentity\taligned_columns")
q = seqs["Q9XYY9"]
for acc in ["Q8IUC4", "Q8TCX5", "Q61085", "Q8BWR8"]:
    pid, cols = identity(q, seqs[acc])
    print(f"Q9XYY9 vs {acc} ({ACCS[acc]})\t{pid:.3f}\t{cols}")
pid, cols = identity(seqs["Q8IUC4"], seqs["Q8TCX5"])
print(f"Q8IUC4 vs Q8TCX5 (human RHPN2 vs RHPN1)\t{pid:.3f}\t{cols}")
