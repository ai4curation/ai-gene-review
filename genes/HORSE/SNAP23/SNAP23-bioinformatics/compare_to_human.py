# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Global alignment of horse SNAP23 (A0A3Q2HTF1) to human SNAP23 (O00161).

Usage: uv run --script compare_to_human.py ../SNAP23-uniprot.txt human-SNAP23-O00161.fasta
Reports length, identity, and the horse residues aligned to human palmitoylated
cysteines (C79, C80, C83, C85, C87, C112) and the two SNARE motif ranges.
All values are computed at run time.
"""
import sys
from Bio import Align
from Bio.Align import substitution_matrices


def read_uniprot_seq(path):
    seq, in_sq = [], False
    for line in open(path):
        if line.startswith("SQ"):
            in_sq = True
            continue
        if in_sq:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", "").strip())
    return "".join(seq)


def read_fasta(path):
    lines = open(path).read().splitlines()
    return "".join(l.strip() for l in lines[1:])


horse = read_uniprot_seq(sys.argv[1])
human = read_fasta(sys.argv[2])
al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
al.mode = "global"
aln = al.align(horse, human)[0]
print(aln)
# map human pos -> horse residue
h2q = {}
ident = 0
aligned = 0
for (qs, qe), (ts, te) in zip(*aln.aligned):
    for k in range(qe - qs):
        h2q[ts + k + 1] = (qs + k + 1, horse[qs + k])
        aligned += 1
        if horse[qs + k] == human[ts + k]:
            ident += 1
print(f"horse length {len(horse)}; human length {len(human)}")
print(f"aligned pairs {aligned}; identical {ident}; identity over human length {ident/len(human):.3f}")
for p in [79, 80, 83, 85, 87, 112]:
    q = h2q.get(p)
    print(f"human {human[p-1]}{p} -> horse {q[1]}{q[0]}" if q else f"human {p} -> gap")
for name, (a, b) in {"SNARE motif 1 (Qb)": (14, 76), "SNARE motif 2 (Qc)": (146, 208)}.items():
    pairs = [h2q.get(i) for i in range(a, b + 1)]
    idn = sum(1 for i, x in zip(range(a, b + 1), pairs) if x and x[1] == human[i - 1])
    print(f"{name} human {a}..{b}: {idn}/{b-a+1} identical")
