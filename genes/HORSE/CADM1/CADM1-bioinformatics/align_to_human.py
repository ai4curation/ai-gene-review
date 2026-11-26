"""Global alignment of a horse UniProt sequence to its human ortholog.

Usage (from this folder):
  uv run --with biopython python align_to_human.py ../GENE-uniprot.txt human-GENE-ACC.fasta [pos ...]
Biopython PairwiseAligner, global, BLOSUM62, gap open -10, gap extend -0.5.
Optional pos arguments are human residue numbers whose aligned horse residue is reported.
All numbers are computed at run time; nothing is hardcoded.
"""
import sys
from Bio import Align
from Bio.Align import substitution_matrices


def read_uniprot_seq(path):
    seq, acc, in_sq = [], None, False
    for line in open(path):
        if line.startswith("AC") and acc is None:
            acc = line.split()[1].rstrip(";")
        if line.startswith("SQ"):
            in_sq = True
            continue
        if in_sq:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", "").strip())
    return acc, "".join(seq)


def read_fasta(path):
    lines = open(path).read().splitlines()
    return lines[0].split("|")[1], "".join(l.strip() for l in lines[1:])


def ranges(missing, n):
    out, start = [], None
    for i in range(1, n + 1):
        if i in missing and start is None:
            start = i
        if i not in missing and start is not None:
            out.append((start, i - 1))
            start = None
    if start is not None:
        out.append((start, n))
    return ", ".join(f"{a}..{b}" for a, b in out) if out else "none"


dacc, dseq = read_uniprot_seq(sys.argv[1])
hacc, hseq = read_fasta(sys.argv[2])
positions = [int(p) for p in sys.argv[3:]]
aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(dseq, hseq)[0]
paired = ident = 0
hmap = {}
for (ds, de), (hs, he) in zip(*aln.aligned):
    for i in range(de - ds):
        paired += 1
        hmap[hs + i + 1] = (ds + i + 1, dseq[ds + i])
        if dseq[ds + i] == hseq[hs + i]:
            ident += 1
print(f"Horse {dacc}: {len(dseq)} aa; human {hacc}: {len(hseq)} aa")
print(f"Paired residues: {paired}; identical: {ident}; identity over paired: {100*ident/paired:.2f}%")
print(f"Coverage of human: {100*paired/len(hseq):.2f}%; coverage of horse: {100*paired/len(dseq):.2f}%")
hmiss = {i for i in range(1, len(hseq) + 1) if i not in hmap}
dcov = {v[0] for v in hmap.values()}
dmiss = {i for i in range(1, len(dseq) + 1) if i not in dcov}
print(f"Human ranges with no aligned horse residue: {ranges(hmiss, len(hseq))}")
print(f"Horse ranges with no aligned human residue: {ranges(dmiss, len(dseq))}")
for p in positions:
    if p in hmap:
        print(f"Human {hseq[p-1]}{p} -> horse {hmap[p][1]}{hmap[p][0]}")
    else:
        print(f"Human {hseq[p-1]}{p} -> not aligned in horse")
