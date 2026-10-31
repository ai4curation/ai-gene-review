"""Compare mouse Sirt5 (Q8K2C6) and human SIRT5 (Q9NXA8) sequences from the cached
UniProt flat files: overall identity (both 310 aa, gapless comparison) and the residues
at the acyl-pocket (Y102, R105), catalytic His158 and zinc-binding Cys positions.

Run: python3 compare_acyl_pocket.py  (from this folder; stdlib only)
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENES = HERE.parent.parent.parent


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ   "))
    seq = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


mouse = read_seq(GENES / "mouse/Sirt5/Sirt5-uniprot.txt")
human = read_seq(GENES / "human/SIRT5/SIRT5-uniprot.txt")
print(f"mouse length {len(mouse)}, human length {len(human)}")
if len(mouse) == len(human):
    same = sum(a == b for a, b in zip(mouse, human))
    print(f"gapless identity: {same}/{len(mouse)} = {100 * same / len(mouse):.1f}%")
    # mature chain after the 36-residue transit peptide
    m, h = mouse[36:], human[36:]
    same_m = sum(a == b for a, b in zip(m, h))
    print(f"mature-chain (37-310) identity: {same_m}/{len(m)} = {100 * same_m / len(m):.1f}%")
for label, pos in [("acyl pocket Y102", 102), ("acyl pocket R105", 105),
                   ("catalytic H158", 158), ("Zn C166", 166), ("Zn C169", 169),
                   ("Zn C207", 207), ("Zn C212", 212)]:
    print(f"{label}: mouse {mouse[pos - 1]} human {human[pos - 1]}")
