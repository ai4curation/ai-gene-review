"""Compare mouse Ptprn2 (P80560) with rat phogrin (Q63475) and human PTPRN2 (Q92932).

Fetches canonical sequences from UniProt REST, performs global pairwise alignments,
reports percent identity, and maps the rat catalytic cysteine (C934, mutated to Ser in
PMID:20097759) and the PTP signature motif region onto mouse.

Run: uv run --with biopython --with requests python compare_orthologs.py
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"mouse": "P80560", "rat": "Q63475", "human": "Q92932"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def align(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    return aligner.align(a, b)[0]


def identity(aln) -> float:
    s1, s2 = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    same = sum(1 for x, y in pairs if x == y)
    return 100.0 * same / min(len(s1.replace("-", "")), len(s2.replace("-", "")))


def map_pos(aln, pos_in_b: int) -> int | None:
    """Map 1-based position in sequence b (target) to 1-based position in sequence a (query)."""
    ia = ib = 0
    for x, y in zip(aln[0], aln[1]):
        if x != "-":
            ia += 1
        if y != "-":
            ib += 1
            if ib == pos_in_b:
                return ia if x != "-" else None
    return None


seqs = {k: fetch(v) for k, v in ACCS.items()}
for k, s in seqs.items():
    print(f"{k} {ACCS[k]} length={len(s)}")

for other in ("rat", "human"):
    aln = align(seqs["mouse"], seqs[other])
    print(f"mouse vs {other}: identity={identity(aln):.1f}%")

aln_rat = align(seqs["mouse"], seqs["rat"])
rat_c = 934
print(f"rat residue {rat_c} = {seqs['rat'][rat_c - 1]}")
m = map_pos(aln_rat, rat_c)
print(f"maps to mouse residue {m} = {seqs['mouse'][m - 1] if m else None}")
if m:
    print(f"mouse context {m - 5}-{m + 6}: {seqs['mouse'][m - 6 : m + 6]}")
    print(f"rat context   {rat_c - 5}-{rat_c + 6}: {seqs['rat'][rat_c - 6 : rat_c + 6]}")
