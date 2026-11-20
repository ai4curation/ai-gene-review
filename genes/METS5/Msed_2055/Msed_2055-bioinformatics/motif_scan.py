"""Locate the B12-binding DXHXXG / SXL / GG motif elements in Msed_2055 (A4YIE3).

Usage: python motif_scan.py ../Msed_2055-uniprot.txt
Reads the sequence from the UniProt flat file and reports regex matches (1-based).
"""
import re
import sys


def read_seq(path):
    seq, in_sq = [], False
    for line in open(path):
        if line.startswith("SQ"):
            in_sq = True
            continue
        if line.startswith("//"):
            break
        if in_sq:
            seq.append(line.replace(" ", "").strip())
    return "".join(seq)


seq = read_seq(sys.argv[1])
print(f"length\t{len(seq)}")
for name, pat in [("DXHXXG", r"D.H..G"), ("SXL", r"S.L"), ("GG", r"GG")]:
    hits = [(m.start() + 1, m.group(1)) for m in re.finditer(f"(?=({pat}))", seq)]
    print(f"{name}\t" + ", ".join(f"{p}:{s}" for p, s in hits))
# conserved His of DXHXXG = axial cobalt ligand in base-off/His-on binding
m = re.search(r"D.H..G", seq)
if m:
    print(f"candidate_axial_His\tH{m.start() + 3}")
