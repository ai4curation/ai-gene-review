"""Check canonical protein-kinase catalytic motifs in FRK1 (O64483) from the cached UniProt record.

Usage: python kinase_motifs.py  (run from this directory; no dependencies)
Reports positions/sequence of the glycine-rich loop, VAIK lysine, alphaC Glu,
HRD catalytic loop and DFG motif. Prints what it finds; does not assume results.
"""
import re
from pathlib import Path

rec = Path(__file__).resolve().parent.parent / "FRK1-uniprot.txt"
txt = rec.read_text()
seq = "".join(txt.split("\nSQ ")[1].split("\n", 1)[1].replace("//", "").split())
kd_start, kd_end = 574, 847  # UniProt DOMAIN Protein kinase
kd = seq[kd_start - 1:kd_end]
print(f"sequence length {len(seq)}; kinase domain {kd_start}-{kd_end}")

def report(name, pattern):
    m = re.search(pattern, kd)
    if m:
        print(f"{name}: {m.group(0)} at {kd_start + m.start()}-{kd_start + m.end() - 1}")
    else:
        print(f"{name}: NOT FOUND (pattern {pattern})")

report("Gly-rich loop GxGxxG", r"G.G..G")
report("beta3 lysine (VAIK-like)", r"[VI]A[IVL]K")
report("alphaC glutamate region (E within helix)", r"F..E[VIL]")
report("catalytic loop HRD", r"H[RL]D.K..N")
report("activation loop DFG", r"DFG")
