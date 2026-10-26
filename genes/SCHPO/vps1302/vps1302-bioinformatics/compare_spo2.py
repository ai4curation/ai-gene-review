# /// script
# requires-python = ">=3.10"
# ///
"""Compare the Spo2 protein (C6Y4C2) with the vps1302 protein (O42926).

Reads the sequences from the UniProt flat files in the gene folders and reports
where (if anywhere) the Spo2 sequence occurs as an exact substring of Vps1302,
plus the best ungapped placement and its identity if no exact match exists.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENES = HERE.parents[1]


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("SQ "))
    seq = []
    for ln in lines[start + 1 :]:
        if ln.startswith("//"):
            break
        seq.append(ln.replace(" ", ""))
    return "".join(seq)


vps = read_seq(GENES / "vps1302" / "vps1302-uniprot.txt")
spo2 = read_seq(GENES / "spo2" / "spo2-uniprot.txt")
print(f"vps1302 (O42926) length: {len(vps)}")
print(f"spo2 (C6Y4C2) length: {len(spo2)}")

idx = vps.find(spo2)
if idx >= 0:
    print(f"Exact match of full Spo2 at vps1302 residues {idx + 1}-{idx + len(spo2)}")
else:
    print("No exact full-length match")

best = (0, -1)
for off in range(len(vps) - len(spo2) + 1):
    ident = sum(a == b for a, b in zip(spo2, vps[off : off + len(spo2)]))
    if ident > best[0]:
        best = (ident, off)
ident, off = best
print(
    f"Best ungapped placement: vps1302 {off + 1}-{off + len(spo2)}, "
    f"{ident}/{len(spo2)} identical ({100 * ident / len(spo2):.1f}%)"
)
# Spo2 starts with Met; check whether a Met in vps1302 aligns with Spo2 residue 1
print(f"Spo2 residue 1: {spo2[0]}; vps1302 residue at placement start: {vps[off]}")
print(f"vps1302 C-terminal end reached by placement: {off + len(spo2) == len(vps)}")
