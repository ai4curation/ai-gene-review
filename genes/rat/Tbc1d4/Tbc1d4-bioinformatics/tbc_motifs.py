"""Locate the TBC-domain catalytic finger motifs (arginine finger IxxDxxR and
glutamine finger YxQ) in rat Tbc1d4 (D3Z881), within the PROSITE PS50086
Rab-GAP TBC domain boundaries recorded in the UniProt flat file.

Usage: python -I tbc_motifs.py ../Tbc1d4-uniprot.txt
"""
import re
import sys

path = sys.argv[1]
lines = open(path).read().splitlines()
seq, in_sq = [], False
dom = None
for i, ln in enumerate(lines):
    if ln.startswith("SQ"):
        in_sq = True
        continue
    if ln.startswith("//"):
        in_sq = False
    if in_sq:
        seq.append(ln.replace(" ", ""))
    m = re.match(r"FT   DOMAIN\s+(\d+)\.\.(\d+)", ln)
    if m and i + 1 < len(lines) and "Rab-GAP TBC" in lines[i + 1]:
        dom = (int(m.group(1)), int(m.group(2)))
s = "".join(seq)
print(f"sequence length: {len(s)}")
print(f"TBC domain (FT DOMAIN, PS50086): {dom}")
start, end = dom
sub = s[start - 1:end]
for name, pat, idx in [("arginine finger IxxDxxR", r"I..D..R", 6), ("glutamine finger YxQ", r"Y.Q", 2)]:
    hits = [(m.start() + start, m.group(), m.start() + start + idx) for m in re.finditer(pat, sub)]
    for h in hits:
        print(f"{name}: motif {h[1]} at {h[0]}-{h[0]+len(h[1])-1}; catalytic residue {s[h[2]-1]}{h[2]}")
    if not hits:
        print(f"{name}: not found")
