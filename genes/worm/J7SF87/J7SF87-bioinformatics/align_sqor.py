"""Pairwise global alignment of J7SF87 (SQRD-2) and C6KRP5 (SQRD-1) against human SQOR (Q9Y6N5).

Reports identity and the residues aligned to human SQOR functional positions taken from the
Q9Y6N5 UniProt flat file (ACT_SITE and BINDING FAD features). Usage:
    uv run python align_sqor.py   (run from this folder; FASTA/flat files are downloaded alongside)
"""
import re
import sys
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

here = Path(__file__).parent
human = str(next(SeqIO.parse(here / "Q9Y6N5.fasta", "fasta")).seq)
feats = []
for line in (here / "Q9Y6N5.txt").read_text().splitlines():
    m = re.match(r"FT   (ACT_SITE|BINDING)\s+(\d+)(?:\.\.(\d+))?", line)
    if m:
        s, e = int(m.group(2)), int(m.group(3) or m.group(2))
        feats.extend((m.group(1), p) for p in range(s, e + 1))

al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -10, -0.5
al.mode = "global"

for acc in sys.argv[1:] or ["J7SF87", "C6KRP5"]:
    q = str(next(SeqIO.parse(here / f"{acc}.fasta", "fasta")).seq)
    a = al.align(human, q)[0]
    hmap = {}
    for (hs, he), (qs, qe) in zip(*a.aligned):
        for i in range(he - hs):
            hmap[hs + i + 1] = qs + i + 1
    ident = sum(1 for p, qp in hmap.items() if human[p - 1] == q[qp - 1])
    print(f"## {acc} (length {len(q)}) vs Q9Y6N5 (length {len(human)})")
    print(f"aligned positions: {len(hmap)}; identical: {ident}; identity over aligned: {ident/len(hmap):.1%}")
    fad = re.search(r"G.G..G", q[:60])
    print(f"N-terminal GxGxxG FAD motif in first 60 residues: {fad.group(0) + ' at ' + str(fad.start() + 1) if fad else 'absent'}")
    for kind, p in feats:
        qp = hmap.get(p)
        qr = q[qp - 1] if qp else "-"
        print(f"  {kind:8s} human {human[p-1]}{p} -> {acc} {qr}{qp if qp else ''}")
    print()

# Paralog comparison: SQRD-2 (J7SF87) vs SQRD-1 (C6KRP5)
p2 = str(next(SeqIO.parse(here / "J7SF87.fasta", "fasta")).seq)
p1 = str(next(SeqIO.parse(here / "C6KRP5.fasta", "fasta")).seq)
x = al.align(p2, p1)[0]
same = sum(1 for (s, e), (t, u) in zip(*x.aligned) for i in range(e - s) if p2[s + i] == p1[t + i])
print(f"## paralogs J7SF87 vs C6KRP5: identical {same} of {len(p2)} J7SF87 residues ({same/len(p2):.1%})")
