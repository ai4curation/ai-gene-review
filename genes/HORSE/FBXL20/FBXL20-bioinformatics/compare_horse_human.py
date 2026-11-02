# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Compare horse FBXL20 (A0A9L0TR23) with human FBXL20 (Q96IG2) from the cached UniProt flat files.

Reports lengths, ungapped identity (only meaningful when lengths are equal; otherwise reports
that an alignment is needed), the F-box span from each record's FT DOMAIN line, and the
C-terminal residues (CAAX-like prenylation motif region).

Run from the repository root:
    uv run --script genes/HORSE/FBXL20/FBXL20-bioinformatics/compare_horse_human.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def parse(path: Path) -> tuple[str, str, list[str]]:
    text = path.read_text()
    acc = re.search(r"^AC   (\w+);", text, re.M).group(1)
    sq = text.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//")[0]
    seq = re.sub(r"\s", "", sq)
    fbox = re.findall(r"^FT   DOMAIN\s+(\d+\.\.\d+)\n(?:FT\s+/.*\n)*?FT\s+/note=\"F-box\"", text, re.M)
    return acc, seq, fbox


horse = parse(ROOT / "HORSE/FBXL20/FBXL20-uniprot.txt")
human = parse(ROOT / "human/FBXL20/FBXL20-uniprot.txt")
for acc, seq, fbox in (horse, human):
    print(f"{acc}: length {len(seq)}; F-box {fbox}; C-terminal 10 residues {seq[-10:]}")
hs, us = horse[1], human[1]
if len(hs) == len(us):
    ident = sum(a == b for a, b in zip(hs, us))
    diffs = [(i + 1, a, b) for i, (a, b) in enumerate(zip(hs, us)) if a != b]
    print(f"equal length {len(hs)}; identical positions {ident}; identity {100 * ident / len(hs):.2f}%")
    print(f"differences (pos, horse, human): {diffs}")
else:
    print("lengths differ; ungapped comparison not valid, an alignment is required")
