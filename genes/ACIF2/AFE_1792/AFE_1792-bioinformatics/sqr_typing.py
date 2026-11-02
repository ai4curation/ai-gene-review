"""Pairwise identity and active-site cysteine mapping for acidophile SQR candidates.

Global alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5).
Identity = identical aligned positions / length of the shorter sequence.
Active-site mapping projects the characterized cysteines of B7JBP8 (C128, C160,
C356; Type I, PMID:20303979/22542586) and Q7ZAG8 (C178, C350; Type V,
PMID:19438211, UniProt ACT_SITE) onto each query and reports the aligned residue.
Also reports total length and the length of the C-terminal extension past the
last aligned residue of the Q7ZAG8 Type V reference.
"""
import sys
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

here = Path(__file__).parent
recs = {r.id.split("|")[1]: r for r in SeqIO.parse(here / "sequences.fasta", "fasta")}
label = {k: r.id.split("|")[2] for k, r in recs.items()}

al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
al.mode = "global"


def align(a, b):
    return al.align(str(recs[a].seq), str(recs[b].seq))[0]


def identity(a, b):
    aln = align(a, b)
    s1, s2 = str(recs[a].seq), str(recs[b].seq)
    ident = 0
    for (x0, x1), (y0, y1) in zip(*aln.aligned):
        for i, j in zip(range(x0, x1), range(y0, y1)):
            ident += s1[i] == s2[j]
    return 100.0 * ident / min(len(s1), len(s2))


def map_pos(ref, query, pos):
    """1-based ref position -> (query residue, 1-based query position) or None."""
    aln = align(ref, query)
    for (x0, x1), (y0, y1) in zip(*aln.aligned):
        if x0 <= pos - 1 < x1:
            j = y0 + (pos - 1 - x0)
            return str(recs[query].seq)[j], j + 1
    return None


targets = ["B7JBP8", "F9ZQD6", "A0A060UVE9", "A0A543Q349", "A0A059XTE6"]
refs = [k for k in recs]

print("## Percent identity (over shorter sequence) of each target vs every sequence\n")
print("| accession | entry | length | " + " | ".join(targets) + " |")
print("|---|---|---|" + "---|" * len(targets))
for r in refs:
    row = [f"{identity(t, r):.1f}" if t != r else "-" for t in targets]
    print(f"| {r} | {label[r]} | {len(recs[r].seq)} | " + " | ".join(row) + " |")

print("\n## Residues aligned to characterized active-site cysteines\n")
sites = [("B7JBP8", 128), ("B7JBP8", 160), ("B7JBP8", 356), ("Q7ZAG8", 178), ("Q7ZAG8", 350)]
print("| query | " + " | ".join(f"{r} C{p}" for r, p in sites) + " |")
print("|---|" + "---|" * len(sites))
for q in refs:
    cells = []
    for r, p in sites:
        if q == r:
            cells.append(f"C{p}")
            continue
        m = map_pos(r, q, p)
        cells.append(f"{m[0]}{m[1]}" if m else "gap")
    print(f"| {q} ({label[q]}) | " + " | ".join(cells) + " |")

print("\n## C-terminal extension beyond the Q7ZAG8 (Type V) C-terminus\n")
for q in refs:
    if q == "Q7ZAG8":
        continue
    aln = align("Q7ZAG8", q)
    last_q = aln.aligned[1][-1][1]
    print(f"- {q} ({label[q]}): length {len(recs[q].seq)}, residues after last position aligned to Q7ZAG8: {len(recs[q].seq) - last_q}")
