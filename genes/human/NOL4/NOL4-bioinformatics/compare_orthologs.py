"""Global pairwise identity of human NOL4 (O94818) against mouse Nol4 (P60954)
and human NOL4L (Q96MY1), plus PANTHER subfamily assignments from UniProt.

Run: uv run --with biopython --with requests python compare_orthologs.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"human_NOL4": "O94818", "mouse_Nol4": "P60954", "human_NOL4L": "Q96MY1"}


def fetch(acc: str) -> tuple[str, list[str]]:
    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).text
    panther = [line.strip() for line in txt.splitlines() if line.startswith("DR   PANTHER")]
    fasta = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60).text
    seq = "".join(fasta.splitlines()[1:])
    return seq, panther


def identity(a: str, b: str) -> tuple[float, int, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += a[i] == b[j]
    return ident / aligned, ident, aligned


seqs = {}
for name, acc in ACCS.items():
    seq, panther = fetch(acc)
    seqs[name] = seq
    print(f"{name}\t{acc}\tlength={len(seq)}")
    for p in panther:
        print(f"  {p}")

for other in ("mouse_Nol4", "human_NOL4L"):
    frac, ident, aligned = identity(seqs["human_NOL4"], seqs[other])
    print(f"human_NOL4 vs {other}: identity={frac:.3f} ({ident}/{aligned} aligned positions)")
