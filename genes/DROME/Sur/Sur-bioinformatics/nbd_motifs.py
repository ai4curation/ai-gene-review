"""Scan the Sur (Q9VL32) sequence from the cached UniProt record for ABC NBD motifs.

Reports Walker A at the UniProt FT BINDING ranges, candidate Walker B motifs
(hydrophobic stretch followed by D[E/Q]/D[D]) and ABC signature motifs.
Usage: python -I nbd_motifs.py ../Sur-uniprot.txt
"""
import re
import sys

text = open(sys.argv[1]).read()
seq = "".join(text.split("\nSQ ")[1].split("\n", 1)[1].replace("//", "").split())
print(f"sequence length: {len(seq)}")
for m in re.finditer(r"FT   BINDING\s+(\d+)\.\.(\d+)", text):
    a, b = int(m.group(1)), int(m.group(2))
    print(f"Walker A (FT BINDING {a}..{b}): {seq[a-1:b]}")
for m in re.finditer(r"[LIVMFA]{3,4}D[EDQ]", seq):
    print(f"candidate Walker B at {m.start()+1}: {m.group()}")
for m in re.finditer(r"[LIVMFYA]S[GA]G[QE]", seq):
    print(f"candidate ABC signature at {m.start()+1}: {m.group()}")
