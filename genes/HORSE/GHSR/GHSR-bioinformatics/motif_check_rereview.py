"""Re-review check: conserved class A GPCR motifs and curated human GHSR sites in horse F6QF00.

Run from the repository root:
    python3 genes/HORSE/GHSR/GHSR-bioinformatics/motif_check_rereview.py

Both records are 366 aa and align gaplessly (see alignment.txt), so human
positions map 1:1 onto horse positions; the script verifies equal length
before comparing positions.
"""
import re
from pathlib import Path

ROOT = Path("genes")


def uniprot_seq(path: Path) -> str:
    text = path.read_text()
    block = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", block)


def feature_positions(path: Path, kind: str) -> list[tuple[int, int]]:
    out = []
    for line in path.read_text().splitlines():
        m = re.match(rf"FT   {kind}\s+(\d+)(?:\.\.(\d+))?", line)
        if m:
            out.append((int(m.group(1)), int(m.group(2) or m.group(1))))
    return out


human_f = ROOT / "human/GHSR/GHSR-uniprot.txt"
horse_f = ROOT / "HORSE/GHSR/GHSR-uniprot.txt"
h, e = uniprot_seq(human_f), uniprot_seq(horse_f)
print(f"human Q92847 length {len(h)}; horse F6QF00 length {len(e)}")
assert len(h) == len(e), "lengths differ; positional comparison invalid"
diffs = [(i + 1, a, b) for i, (a, b) in enumerate(zip(h, e)) if a != b]
print(f"substitutions ({len(diffs)}): " + ", ".join(f"{a}{p}{b}" for p, a, b in diffs))

print("\nClass A GPCR motifs (regex, 1-based start): human | horse")
for name, pat in [("D/ERY (TM3)", "[DE]RY"), ("NPxxY (TM7)", "NP..Y"), ("CWxP (TM6)", "CW.P")]:
    hs = [m.start() + 1 for m in re.finditer(pat, h)]
    es = [m.start() + 1 for m in re.finditer(pat, e)]
    print(f"  {name}: {hs} | {es}")

print("\nCurated human sites (UniProt FT) and horse residue")
for kind in ["DISULFID", "BINDING", "SITE", "MOD_RES", "LIPID", "CARBOHYD"]:
    for s, t in feature_positions(human_f, kind):
        pos = (s, t) if kind == "DISULFID" else tuple(range(s, t + 1))
        for p in pos:
            print(f"  {kind} {p}: human {h[p-1]} horse {e[p-1]} {'same' if h[p-1]==e[p-1] else 'DIFFERENT'}")
