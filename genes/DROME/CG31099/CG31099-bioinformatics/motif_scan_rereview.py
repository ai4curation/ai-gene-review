"""Locate APH/CHK-type kinase catalytic-loop (Brenner HxDxxxxN) and Mg-binding
D motifs in the Q8IMT2 sequence read from the local UniProt flat file.

Run: python3 motif_scan_rereview.py
"""
import re
from pathlib import Path

here = Path(__file__).resolve().parent
txt = (here.parent / "CG31099-uniprot.txt").read_text()
seq = "".join(txt.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//")[0].split())
print(f"length={len(seq)}")
for m in re.finditer(r"(?=(H.D....N))", seq):
    print(f"Brenner HxDxxxxN at {m.start()+1}-{m.start()+8}: {m.group(1)}")
# Mg2+-binding aspartate in APH-type kinases sits ~10-25 residues after the
# catalytic loop asparagine; report D residues in that window for inspection.
for m in re.finditer(r"(?=(H.D....N))", seq):
    n_pos = m.start() + 8
    window = seq[n_pos:n_pos + 30]
    ds = [n_pos + 1 + i for i, c in enumerate(window) if c == "D"]
    print(f"D residues within 30 aa after N{n_pos}: {ds}; window={window}")
