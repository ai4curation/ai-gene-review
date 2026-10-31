"""Pairwise global comparison of CG3515 (Q9VQD1) with fly Wdr82 (Q9VLN1), human WDR82 (Q6UXN9)
and yeast Swd2 (P36104). Sequences are fetched live from UniProt REST.

Run: uv run --with biopython --with requests python compare_swd2_paralogs_rereview.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"CG3515": "Q9VQD1", "Wdr82_fly": "Q9VLN1", "WDR82_human": "Q6UXN9", "Swd2_yeast": "P36104"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a: str, b: str) -> tuple[float, int, int]:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    aln = al.align(a, b)[0]
    ident = 0
    aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += a[i] == b[j]
    return ident / aligned, ident, aligned


seqs = {k: fetch(v) for k, v in ACCS.items()}
for k, s in seqs.items():
    print(f"{k}\t{ACCS[k]}\tlength={len(s)}")
names = list(seqs)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        f, n, m = identity(seqs[names[i]], seqs[names[j]])
        print(f"{names[i]} vs {names[j]}\tidentity={f:.3f} ({n}/{m} aligned positions)")
