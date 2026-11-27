# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Global alignment of horse LOXL3 (A0A9L0TKN1) against human LOXL3 (P58215).

Reports length, identity, and conservation of the human UniProt-annotated
catalytic features (Cu-binding His 607/609/611, LTQ Lys634-Tyr670 crosslink).
"""
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
GENES = HERE.parents[2]


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    i = next(n for n, l in enumerate(lines) if l.startswith("SQ   "))
    out = []
    for l in lines[i + 1:]:
        if l.startswith("//"):
            break
        out.append(l.replace(" ", ""))
    return "".join(out)


horse = read_seq(GENES / "HORSE/LOXL3/LOXL3-uniprot.txt")
human = read_seq(GENES / "human/LOXL3/LOXL3-uniprot.txt")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aln = aligner.align(human, horse)[0]

# map human positions -> horse positions
hmap = {}
ident = aligned = 0
for (hs, he), (qs, qe) in zip(*aln.aligned):
    for k in range(he - hs):
        hmap[hs + k + 1] = qs + k + 1
        aligned += 1
        if human[hs + k] == horse[qs + k]:
            ident += 1

print(f"human P58215 length: {len(human)}")
print(f"horse A0A9L0TKN1 length: {len(horse)}")
print(f"aligned positions: {aligned}; identical: {ident}; "
      f"identity over human length: {100*ident/len(human):.1f}%")

sites = {607: "Cu-binding His", 609: "Cu-binding His", 611: "Cu-binding His",
         634: "LTQ Lys (crosslink)", 670: "LTQ Tyr (topaquinone)"}
for pos, name in sites.items():
    q = hmap.get(pos)
    print(f"human {human[pos-1]}{pos} ({name}) -> horse "
          f"{horse[q-1] + str(q) if q else 'GAP'}")

# copper-binding motif region
q = hmap.get(600)
print("human 600-615:", human[599:615])
if q:
    print("horse aligned:", horse[q - 1:q + 15])
