# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython"]
# ///
"""Global alignment of horse KRIT1 (A0A3Q2GZV2) against human KRIT1 (O00522).

Reads sequences from the local UniProt flat files and reports identity,
gaps, and conservation of key motifs (NPxY/F motifs, Rap1-binding FERM).
Run: uv run compare_to_human.py
"""
from pathlib import Path
import re
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
GENES = HERE.parents[2]


def read_seq(path: Path) -> str:
    text = path.read_text()
    sq = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", sq)


horse = read_seq(HERE.parent / "KRIT1__A0A3Q2GZV2-uniprot.txt")
human = read_seq(GENES / "human" / "KRIT1" / "KRIT1-uniprot.txt")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aln = aligner.align(horse, human)[0]

a, b = aln[0], aln[1]
pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
ident = sum(1 for x, y in pairs if x == y)
gaps_h = a.count("-")
gaps_q = b.count("-")
print(f"horse length: {len(horse)}")
print(f"human length: {len(human)}")
print(f"aligned pairs: {len(pairs)}; identical: {ident} ({100*ident/len(pairs):.1f}%)")
print(f"gap columns in horse: {gaps_h}; in human: {gaps_q}")

# NPx(Y/F) motifs in the N-terminal half (ICAP1/CCM2-binding motifs)
for name, seq in [("horse", horse), ("human", human)]:
    hits = [(m.start() + 1, m.group()) for m in re.finditer(r"NP.[YF]", seq[:300])]
    print(f"{name} NPx(Y/F) motifs in residues 1-300: {hits}")

# Regions annotated in human UniProt O00522 (1-based, inclusive)
regions = {
    "Nudix-like N-terminal domain 1-170": (1, 170),
    "ITGB1BP1 interaction 172-195": (172, 195),
    "ANK repeats 287-419": (287, 419),
    "RAP1B interaction 430-452": (430, 452),
    "FERM domain 420-734": (420, 734),
}
# alignment is gapless (checked above), so positions correspond 1:1
assert gaps_h == 0 and gaps_q == 0
for label, (s0, e0) in regions.items():
    hs, us = horse[s0 - 1:e0], human[s0 - 1:e0]
    same = sum(1 for x, y in zip(hs, us) if x == y)
    print(f"{label}: {same}/{len(us)} identical")

# list mismatched columns
diffs = []
hpos = qpos = 0
for x, y in zip(a, b):
    if x != "-":
        hpos += 1
    if y != "-":
        qpos += 1
    if x != y:
        diffs.append(f"horse {hpos if x!='-' else '-'}{x} / human {qpos if y!='-' else '-'}{y}")
print(f"differing columns ({len(diffs)}):")
for d in diffs:
    print("  " + d)
