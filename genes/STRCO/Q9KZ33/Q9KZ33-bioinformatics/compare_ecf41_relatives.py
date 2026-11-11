"""Pairwise comparison of Q9KZ33 (SCO7099) with M. tuberculosis ECF41 sigma factors.

Fetches sequences from UniProt REST and reports global-alignment identity for the
whole protein and for the N-terminal sigma2/sigma4 region vs the C-terminal extension.
Run: uv run --with biopython --with requests python compare_ecf41_relatives.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q9KZ33": "S. coelicolor SCO7099 (PTHR30173:SF43)",
    "P9WGH3": "M. tuberculosis SigI Rv1189 (PTHR30173:SF43)",
    "L0TCG5": "M. tuberculosis SigJ Rv3328c (PTHR30173:SF36; IBA seed)",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a: str, b: str) -> tuple[float, int]:
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    aln = al.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(1 for x, y in cols if x == y)
    return 100 * ident / len(cols), len(cols)


seqs = {a: fetch(a) for a in ACCS}
for a, s in seqs.items():
    print(f"{a}\t{len(s)} aa\t{ACCS[a]}")
q = seqs["Q9KZ33"]
SPLIT = 170  # approx end of sigma4 helix-turn-helix in Q9KZ33 (residue ~160)
for other in ("P9WGH3", "L0TCG5"):
    o = seqs[other]
    full = identity(q, o)
    nterm = identity(q[:SPLIT], o[:SPLIT])
    cterm = identity(q[SPLIT:], o[SPLIT:])
    print(f"Q9KZ33 vs {other}: full {full[0]:.1f}% over {full[1]} aligned cols; "
          f"N-term(1-{SPLIT}) {nterm[0]:.1f}% ({nterm[1]}); C-term {cterm[0]:.1f}% ({cterm[1]})")
print("C-terminal 'NPDKL' present:", {a: ("NPDKL" in s) for a, s in seqs.items()})
