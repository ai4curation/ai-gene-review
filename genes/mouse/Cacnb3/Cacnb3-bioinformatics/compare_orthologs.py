"""Compare mouse Cacnb3 (P54285) with human CACNB3 (P54284), rat Cacnb3 (P54287)
and the mouse beta paralogs.

Reports (1) PANTHER 19.0 subfamily assignment for each protein, read from the
release-pinned PANTHER classification files in .cache/panther/, and (2) global
pairwise identity (Needleman-Wunsch, BLOSUM62) of P54285 against each protein,
using sequences downloaded live from UniProt REST.

Run: uv run --with biopython --with requests python compare_orthologs.py
"""

from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

REPO = Path(__file__).resolve().parents[4]
PANTHER_DIR = REPO / ".cache" / "panther"
QUERY = "P54285"
PROTEINS = {
    "P54285": ("mouse", "Cacnb3"),
    "P54284": ("human", "CACNB3"),
    "P54287": ("rat", "Cacnb3"),
    "Q8R3Z5": ("mouse", "Cacnb1"),
    "Q8CC27": ("mouse", "Cacnb2"),
    "Q8R0S4": ("mouse", "Cacnb4"),
}


def fetch_seq(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def panther_assignment(acc: str) -> str:
    for f in sorted(PANTHER_DIR.glob("PTHR19.0_*")):
        for line in f.open():
            cols = line.rstrip("\n").split("\t")
            if len(cols) > 3 and cols[1] == acc:
                return f"{cols[3]} ({cols[5]})"
    return "not found in PANTHER 19.0 classification files"


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    matches = sum(
        1
        for (s1, e1), (s2, e2) in zip(*aln.aligned)
        for i, j in zip(range(s1, e1), range(s2, e2))
        if a[i] == b[j]
    )
    return 100.0 * matches / min(len(a), len(b)), matches


def main() -> None:
    seqs = {acc: fetch_seq(acc) for acc in PROTEINS}
    print("| accession | species | gene | length | PANTHER 19.0 subfamily | identity to P54285 (% of shorter) |")
    print("|---|---|---|---|---|---|")
    for acc, (sp, gene) in PROTEINS.items():
        pid, _ = identity(seqs[QUERY], seqs[acc])
        print(f"| {acc} | {sp} | {gene} | {len(seqs[acc])} | {panther_assignment(acc)} | {pid:.1f} |")


if __name__ == "__main__":
    main()
