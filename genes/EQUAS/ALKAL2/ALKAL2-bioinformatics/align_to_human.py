"""Global alignment of a donkey UniProt sequence to its human ortholog.

Usage: python align_to_human.py DONKEY_UNIPROT.txt HUMAN_UNIPROT.txt [pos ...]
Reads sequences from UniProt flat files, aligns with Biopython PairwiseAligner
(global, BLOSUM62, gap open -10, extend -0.5) and reports identity/coverage.
Optional human positions (1-based) are mapped to donkey residues.
"""
import sys
from Bio import Align
from Bio.Align import substitution_matrices


def read_seq(path):
    acc, seq, inseq = None, [], False
    for line in open(path):
        if line.startswith("AC") and acc is None:
            acc = line.split()[1].rstrip(";")
        if line.startswith("SQ"):
            inseq = True
            continue
        if line.startswith("//"):
            break
        if inseq:
            seq.append(line.replace(" ", "").strip())
    return acc, "".join(seq)


da, ds = read_seq(sys.argv[1])
ha, hs = read_seq(sys.argv[2])
al = Align.PairwiseAligner()
al.mode = "global"
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
aln = al.align(ds, hs)[0]
pairs = ident = 0
hmap = {}
for (ds0, de0), (hs0, he0) in zip(*aln.aligned):
    for i, j in zip(range(ds0, de0), range(hs0, he0)):
        pairs += 1
        ident += ds[i] == hs[j]
        hmap[j + 1] = (i + 1, ds[i], hs[j])
print(f"donkey {da} length {len(ds)}; human {ha} length {len(hs)}")
print(f"aligned pairs {pairs}; identical {ident}; identity over aligned pairs {100*ident/pairs:.2f}%")
print(f"coverage of human {100*pairs/len(hs):.1f}%; coverage of donkey {100*pairs/len(ds):.1f}%")
# report unaligned human segments
gaps, start = [], None
for p in range(1, len(hs) + 1):
    if p not in hmap and start is None:
        start = p
    if p in hmap and start is not None:
        gaps.append((start, p - 1)); start = None
if start is not None:
    gaps.append((start, len(hs)))
print("human segments without aligned donkey residue:", gaps if gaps else "none")
for a in sys.argv[3:]:
    p = int(a)
    if p in hmap:
        i, dr, hr = hmap[p]
        print(f"human {hr}{p} -> donkey {dr}{i}")
    else:
        print(f"human position {p} unaligned")

# Per-window identity along the donkey sequence (windows of 50 donkey residues)
dmap = {v[0]: k for k, v in hmap.items()}
for w in range(0, len(ds), 50):
    idx = [i for i in range(w + 1, min(w + 50, len(ds)) + 1) if i in dmap]
    same = sum(ds[i - 1] == hs[dmap[i] - 1] for i in idx)
    rng = f"human {dmap[idx[0]]}-{dmap[idx[-1]]}" if idx else "unaligned"
    print(f"donkey {w+1}-{min(w+50, len(ds))}: aligned {len(idx)}, identical {same} ({rng})")
