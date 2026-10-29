"""Locate Cys-loop and loop-C vicinal cysteine motifs in the acr-18 UniProt sequence.

Usage: python cys_motifs.py ../acr-18-uniprot.txt
"""
import re
import sys

text = open(sys.argv[1]).read()
seq = "".join(re.findall(r"^     (.*)$", text, re.M)).replace(" ", "")
print(f"length\t{len(seq)}")
cys = [i + 1 for i, c in enumerate(seq) if c == "C"]
print(f"cysteines\t{','.join(map(str, cys))}")
# Cys-loop: two cysteines separated by 13 residues within the N-terminal ECD
for a in cys:
    b = a + 14
    if b in cys and b < 240:
        print(f"cys_loop_pair\tC{a}-C{b}\t{seq[a-1:b]}")
for m in re.finditer("CC", seq[:240]):
    s = m.start()
    print(f"vicinal_cys\tC{s+1}-C{s+2}\t{seq[s-6:s+8]}")
