"""Compare Arabidopsis cpLEPA (Q9FNM5) with LepA/GUF1 relatives.

Fetches sequences and PANTHER assignments from UniProt REST, computes global
(Needleman-Wunsch, BLOSUM62) percent identity, and scans for the conserved
translational-GTPase G-domain motifs. Run: uv run python compare_lepa.py
"""
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q9FNM5"
OTHERS = {
    "P60785": "E. coli LepA",
    "Q9FLE4": "Arabidopsis GUF1 (mitochondrial)",
    "P46943": "yeast GUF1 (mitochondrial)",
    "Q8N442": "human GUF1 (mitochondrial)",
}
MOTIFS = {
    "G1 P-loop [AG]x4GK[ST]": r"[AG].{4}GK[ST]",
    "G3 D..G": r"D[A-Z]{2}G[HQ]",
    "G4 NKxD": r"NK.D",
}


def fetch(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.txt") as r:
        return r.read().decode()


def seq_of(txt: str) -> str:
    return "".join(txt.split("\nSQ ")[1].split("\n", 1)[1].split()).replace("//", "")


def panther(txt: str) -> list[str]:
    return [l for l in txt.splitlines() if l.startswith("DR   PANTHER") and ":SF" in l]


aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

ttxt = fetch(TARGET)
tseq = seq_of(ttxt)
print(f"{TARGET} length {len(tseq)}; {panther(ttxt)}")
for name, pat in MOTIFS.items():
    if pat:
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, tseq)]
        print(f"  motif {name}: {hits[:3]}")
for acc, label in OTHERS.items():
    txt = fetch(acc)
    s = seq_of(txt)
    aln = aligner.align(tseq, s)[0]
    ident = sum(1 for a, b in zip(*aln) if a == b and a != "-")
    cols = sum(1 for a, b in zip(*aln) if a != "-" and b != "-")
    print(
        f"{acc} {label} len={len(s)} identity/aligned={100*ident/cols:.1f}% "
        f"identity/shorter={100*ident/min(len(s), len(tseq)):.1f}% {panther(txt)}"
    )
