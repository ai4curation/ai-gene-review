"""Align KT2440 ThiG (Q88CS6) to E. coli (P30139) and B. subtilis (O31618) ThiG and
check that the residues UniProt marks as active site / DXP binding in the reference
entries map to identical residues in Q88CS6.

Usage: python thig_active_site.py thiG-uniprot.txt > thig_active_site.out
"""
import io
import sys
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

REFS = ["P30139", "O31618"]


def fetch_txt(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    with urllib.request.urlopen(url, timeout=120) as r:
        return SeqIO.read(io.StringIO(r.read().decode()), "swiss")


def sites(rec):
    out = []
    for f in rec.features:
        if f.type in ("ACT_SITE", "BINDING"):
            for pos in range(int(f.location.start), int(f.location.end)):
                out.append((f.type, pos, f.qualifiers.get("evidence", "")))
    return out


def main():
    q = SeqIO.read(sys.argv[1], "swiss")
    qs = str(q.seq)
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    for acc in REFS:
        ref = fetch_txt(acc)
        rs = str(ref.seq)
        aln = a.align(rs, qs)[0]
        # map ref index -> query index
        m = {}
        for (r0, r1), (q0, q1) in zip(*aln.aligned):
            for i in range(r1 - r0):
                m[r0 + i] = q0 + i
        ident = sum(1 for i, j in m.items() if rs[i] == qs[j])
        print(f"{acc} ({len(rs)} aa) vs Q88CS6 ({len(qs)} aa): {ident} identical of {len(m)} aligned "
              f"positions ({100*ident/len(m):.1f}%)")
        for typ, pos, ev in sites(ref):
            j = m.get(pos)
            qres = f"{qs[j]}{j+1}" if j is not None else "gap"
            print(f"  {typ} {rs[pos]}{pos+1} [{ev}] -> Q88CS6 {qres}")


if __name__ == "__main__":
    main()
