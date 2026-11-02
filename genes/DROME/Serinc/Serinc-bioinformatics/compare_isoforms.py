"""Compare Serinc isoform products (FlyBase PA-PF) against M9PCT1 (isoform C)
and against yeast TMS1 (same PANTHER subfamily PTHR10383:SF9).

Run: uv run --with biopython python compare_isoforms.py
Input: serinc_isoforms_and_TMS1.fasta (downloaded from rest.uniprot.org)
"""
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

recs = {r.id.split("|")[1]: r for r in SeqIO.parse("serinc_isoforms_and_TMS1.fasta", "fasta")}
ref = recs["M9PCT1"]
aln = PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
aln.substitution_matrix = substitution_matrices.load("BLOSUM62")


def diff_segments(a, b):
    """Return list of (a_start,a_end,b_start,b_end) blocks where alignment differs."""
    best = aln.align(a, b)[0]
    s1, s2 = best[0], best[1]
    segs, i, j, cur = [], 0, 0, None
    for x, y in zip(s1, s2):
        same = x == y and x != "-"
        if not same and cur is None:
            cur = [i + 1, None, j + 1, None]
        if same and cur is not None:
            cur[1], cur[3] = i, j
            segs.append(tuple(cur))
            cur = None
        if x != "-":
            i += 1
        if y != "-":
            j += 1
    if cur is not None:
        cur[1], cur[3] = i, j
        segs.append(tuple(cur))
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    return segs, ident


for acc, r in recs.items():
    segs, ident = diff_segments(str(ref.seq), str(r.seq))
    print(f"{acc}\tlen={len(r.seq)}\tidentical_positions_vs_M9PCT1={ident}\tdiff_blocks(M9PCT1 a..b / other c..d)={segs if len(segs) < 15 else str(len(segs)) + ' blocks'}")
