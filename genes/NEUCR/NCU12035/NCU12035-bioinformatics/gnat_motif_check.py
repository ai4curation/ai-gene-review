# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Check the GNAT acetyl-CoA-binding motif A and simple sequence features in V5ILC0.

Reads the sequence from the cached UniProt flat file and reports:
- matches to GNAT motif A, the acetyl-CoA pyrophosphate-binding loop, (R/Q)-x-x-G-x-(G/A)
- the PROSITE GNAT domain span recorded in the UniProt FT line
- composition of the region C-terminal to the GNAT domain
- the maximum Kyte-Doolittle hydropathy in 19-residue windows (crude TM screen)
"""
import re
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
uniprot = here.parent / "NCU12035-uniprot.txt"
text = uniprot.read_text()
seq = "".join(
    line.strip().replace(" ", "")
    for line in text.split("SQ   SEQUENCE", 1)[1].splitlines()[1:]
    if not line.startswith("//")
)
print(f"length={len(seq)}")

dom = re.search(r"FT   DOMAIN\s+(\d+)\.\.(\d+)", text)
dstart, dend = int(dom.group(1)), int(dom.group(2))
print(f"GNAT domain (PROSITE PS51186) = {dstart}..{dend}")

for m in re.finditer(r"(?=([RQ]..G.[GA]))", seq):
    pos = m.start() + 1
    inside = dstart <= pos <= dend
    print(f"motif A candidate {m.group(1)} at {pos}-{pos+5} inside_domain={inside}")

tail = seq[dend:]
print(f"C-terminal tail {dend+1}..{len(seq)} ({len(tail)} aa): {tail}")
st_p = sum(tail.count(a) for a in "STP")
print(f"S+T+P fraction in tail = {st_p/len(tail):.2f}")

kd = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
          L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)
w = 19
best = max(((sum(kd[a] for a in seq[i:i+w]) / w, i + 1) for i in range(len(seq) - w + 1)))
print(f"max KD hydropathy ({w}-aa window) = {best[0]:.2f} starting at {best[1]} "
      f"(values >1.6 suggest a TM helix)")
sys.exit(0)
