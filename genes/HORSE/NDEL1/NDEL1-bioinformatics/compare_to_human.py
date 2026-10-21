# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Global alignment of horse NDEL1 (A0A5F5PSW5) vs human NDEL1 (Q9GZM8) and
the donkey NDEL1 model, reading sequences from the cached UniProt flat files."""
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[3]

def seq_from_flat(p: Path) -> str:
    lines = p.read_text().splitlines()
    i = next(k for k, l in enumerate(lines) if l.startswith("SQ "))
    out = []
    for l in lines[i + 1:]:
        if l.startswith("//"):
            break
        out.append(l.replace(" ", ""))
    return "".join(out)

horse = seq_from_flat(ROOT / "HORSE/NDEL1/NDEL1-uniprot.txt")
human = seq_from_flat(ROOT / "human/NDEL1/NDEL1-uniprot.txt")
al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5,
                           substitution_matrix=substitution_matrices.load("BLOSUM62"))
a = al.align(horse, human)[0]
print(f"horse length {len(horse)}; human length {len(human)}")
print(a)
# identity over human-aligned blocks
ident = sum(horse[i] == human[j] for (s1, e1), (s2, e2) in zip(*a.aligned) for i, j in zip(range(s1, e1), range(s2, e2)))
alen = sum(e - s for s, e in a.aligned[1])
print(f"aligned human residues {alen}; identical {ident} ({ident/alen:.1%})")
# longest exact prefix shared
k = 0
while k < min(len(horse), len(human)) and horse[k] == human[k]:
    k += 1
print(f"identical N-terminal prefix length: {k}")
# where does human C-terminal tail (316-345) appear in horse?
tail = human[315:]
print("human 316-345:", tail, "found exactly in horse:", tail in horse)
print("human 1-315 found exactly in horse:", human[:315] in horse)
for motif_name, motif in [("human Cys273 context", human[268:278])]:
    print(motif_name, motif, "at horse pos", horse.find(motif) + 1)
print("horse residues after human-shared region:", horse[horse.find(human[300:315]) + 15:])
