"""Scan CG33116 and comparators for the CDP-alcohol phosphotransferase (CAPT) motif
D(X)2DG(X)2(A/Y)R(X)8-16G(X)3D(X)3D (as given in PMID:23449981).
Reads rereview_seqs.fasta written by tree_rereview.py."""
import re
pat = re.compile(r"D..DG..[AY]R.{8,16}G...D...D")
name = None
seqs = {}
for line in open("rereview_seqs.fasta"):
    line = line.strip()
    if line.startswith(">"):
        name = line[1:]
        seqs[name] = ""
    else:
        seqs[name] += line
for n, s in seqs.items():
    m = pat.search(s)
    print(f"{n:20s}", f"{m.start()+1}-{m.end()} {m.group()}" if m else "NO MATCH")
