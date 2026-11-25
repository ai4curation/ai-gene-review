"""PANTHER 19.0 placement of snk, its SF147 co-members, and the IBA donors.

Inputs (relative to repo root):
  .cache/panther/PTHR19.0_fruit_fly   PANTHER 19.0 HMM classification, fruit fly
  genes/DROME/snk/snk-goa.tsv         GOA rows (only WITH/FROM of IBA rows used)
  genes/DROME/snk/snk-uniprot.txt     sequence + annotated active-site positions

Run from repo root:  python3 genes/DROME/snk/snk-bioinformatics/panther_placement.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
CLS = ROOT / ".cache/panther/PTHR19.0_fruit_fly"
GOA = ROOT / "genes/DROME/snk/snk-goa.tsv"
UNI = ROOT / "genes/DROME/snk/snk-uniprot.txt"

fb2sf = {}
fb2name = {}
for line in CLS.read_text().splitlines():
    cols = line.split("\t")
    m = re.search(r"FlyBase=(FBgn\d+)", cols[0])
    if m:
        fb2sf[m.group(1)] = cols[3]
        fb2name[m.group(1)] = cols[2]

snk_sf = fb2sf["FBgn0003450"]
print(f"snk (FBgn0003450) PANTHER 19.0 subfamily: {snk_sf}")
members = sorted(fb2name[f] for f, sf in fb2sf.items() if sf == snk_sf)
print(f"{snk_sf} fruit-fly members ({len(members)}): {', '.join(members)}")
print()

print("IBA rows: WITH/FROM FlyBase donors and their PANTHER 19.0 subfamily")
for line in GOA.read_text().splitlines():
    cols = line.split("\t")
    if len(cols) < 9 or "ECO:0000318" not in line:
        continue
    term = next(c for c in cols if c.startswith("GO:"))
    donors = re.findall(r"FB:(FBgn\d+)", line)
    print(f"  {term}:")
    for d in donors:
        sf = fb2sf.get(d, "not classified")
        same = "SAME as snk" if sf == snk_sf else "different"
        print(f"    {d} {fb2name.get(d, '?')}: {sf} ({same})")
print()

seq = "".join(
    l.strip().replace(" ", "")
    for l in UNI.read_text().split("\nSQ ")[1].splitlines()[1:]
    if not l.startswith("//")
)
print(f"Sequence length: {len(seq)}")
for pos in re.findall(r"ACT_SITE\s+(\d+)", UNI.read_text()):
    p = int(pos)
    print(f"  ACT_SITE {p}: {seq[p-1]}  context {seq[p-4:p+3]}")
print(f"  Zymogen region around Leu185/Ile186: {seq[179:192]} (residues 180-192)")
