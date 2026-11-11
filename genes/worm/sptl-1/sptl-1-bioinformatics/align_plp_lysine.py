"""Align C. elegans SPTL-1 (P91079) to human SPTLC1 (O15269) and SPTLC2 (O15270).

Reports global identity and the SPTL-1 residues aligned to (a) the SPTLC2
PLP Schiff-base lysine (K379 in O15270) and (b) the SPTLC1 HSAN1 residue C133.
Inputs: FASTA files downloaded from rest.uniprot.org (in this folder).
Usage: uv run python align_plp_lysine.py
"""
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent


def load(acc):
    return str(SeqIO.read(HERE / f"{acc}.fasta", "fasta").seq)


def aligner():
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def map_positions(aln):
    """Map 1-based positions in target (seqB) to query (seqA) residues."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(a1 - a0):
            m[b0 + i + 1] = a0 + i + 1
    return m


def identity(aln, a, b):
    same = n = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(a1 - a0):
            n += 1
            same += a[a0 + i] == b[b0 + i]
    return same, n


worm = load("P91079")
for acc, pos in [("O15270", 379), ("O15269", 133)]:
    other = load(acc)
    aln = aligner().align(worm, other)[0]
    same, n = identity(aln, worm, other)
    m = map_positions(aln)
    print(f"P91079 vs {acc}: identity {same}/{n} aligned = {100*same/n:.1f}%")
    print(f"  {acc} residue {pos} = {other[pos-1]}; window {other[pos-6:pos+5]}")
    if pos in m:
        w = m[pos]
        print(f"  aligned P91079 residue {w} = {worm[w-1]}; window {worm[w-6:w+5]}")
    else:
        print("  position falls in a gap in P91079")
