"""Align Arabidopsis LPXD1 (F4JGP6) and LPXD2 (F4JIP6) to E. coli LpxD (P21645).

Reports pairwise identity, coverage of the E. coli N-terminal (uridine-binding)
region, and the residues aligned to E. coli LpxD key positions (catalytic
His239 and Arg293, the latter implicated in acyl-ACP binding by Li et al. 2011).
Sequences are fetched live from UniProt REST; nothing is hardcoded.
Run: uv run python align_lpxd.py
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

ACC = {"EcLpxD": "P21645", "AtLpxD1": "F4JGP6", "AtLpxD2": "F4JIP6"}


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url).read().decode()
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def aligner():
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    a.end_gap_score = 0  # free end gaps (transit peptides, length differences)
    return a


def mapping(aln):
    """Map target (seqA) positions (1-based) to query (seqB) positions."""
    m = {}
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            m[ts + i + 1] = qs + i + 1
    return m


def identity(aln):
    ident = alen = 0
    a, b = aln.target, aln.query
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            alen += 1
            ident += a[ts + i] == b[qs + i]
    return ident, alen


seqs = {k: fetch(v) for k, v in ACC.items()}
for k, s in seqs.items():
    print(f"{k} ({ACC[k]}): length {len(s)}")
al = aligner()
ec = seqs["EcLpxD"]
for name in ("AtLpxD1", "AtLpxD2"):
    aln = al.align(ec, seqs[name])[0]
    ident, alen = identity(aln)
    m = mapping(aln)
    covered_nterm = sum(1 for p in range(1, 101) if p in m)
    print(f"\n{name} vs EcLpxD: identity {ident}/{alen} aligned = {100*ident/alen:.1f}%")
    print(f"  EcLpxD residues 1-100 (N-terminal domain) aligned: {covered_nterm}/100")
    first = min(m)
    print(f"  first aligned EcLpxD residue: {first} -> {name} {m[first]}")
    for pos in (239, 293):
        q = m.get(pos)
        res = seqs[name][q - 1] if q else "-"
        print(f"  EcLpxD {ec[pos-1]}{pos} -> {name} {res}{q if q else ''}")
aln = al.align(seqs["AtLpxD1"], seqs["AtLpxD2"])[0]
ident, alen = identity(aln)
print(f"\nAtLpxD1 vs AtLpxD2: identity {ident}/{alen} aligned = {100*ident/alen:.1f}%")
