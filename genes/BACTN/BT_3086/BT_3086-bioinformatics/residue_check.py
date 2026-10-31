"""Align BT_3086 (Q8A369) with FjDex31A (A5FBI1, Fjoh_4430) and report the residues
at FjDex31A positions highlighted in its crystal-structure paper (PMID:31552702):
Gly273, Leu308, Gln309, Trp376, Asp412 (D412A mutant used for substrate complex,
i.e. the catalytic nucleophile), Tyr524. Also reports query-vs-FjDex31A identity.
Sequences are fetched live from UniProt REST.
Usage: uv run --with biopython python residue_check.py
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url, timeout=60).read().decode()
    return "".join(txt.splitlines()[1:])

QUERY, REF = "Q8A369", "A5FBI1"
q, r = fetch(QUERY), fetch(REF)
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
aligner.mode = "global"
aln = aligner.align(q, r)[0]

# map ref position -> query position
ref2q = {}
ident = alnlen = 0
for (qs, qe), (rs, re_) in zip(*aln.aligned):
    for i in range(qe - qs):
        ref2q[rs + i + 1] = qs + i + 1
        alnlen += 1
        ident += q[qs + i] == r[rs + i]
print(f"{QUERY} length {len(q)}; {REF} length {len(r)}")
print(f"aligned positions {alnlen}; identical {ident}; identity over aligned {ident/alnlen:.1%}")
print("FjDex31A_residue\tquery_position\tquery_residue\tmatch")
for pos in [273, 308, 309, 376, 412, 524]:
    qp = ref2q.get(pos)
    qa = q[qp - 1] if qp else "-"
    print(f"{r[pos-1]}{pos}\t{qp}\t{qa}\t{'yes' if qa == r[pos-1] else 'no'}")
