"""Compare mouse Efr3a (Q8BG67) with human EFR3A (Q14156), mouse Efr3b (Q6ZQ18)
and human CDSN (Q15517, the donor of three MGI ISO rows).

Fetches sequences and PANTHER cross-references live from UniProt REST, reports
global-alignment identity, and checks the residues tested experimentally on
mouse EFR3A: the N-terminal palmitoylated cysteines (Cys6-Cys9; Nakatsu 2012)
and the basic patch K50/R53/R61/R68/R70 (Wu 2014).

Run: uv run python compare_sequences.py
"""

import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCESSIONS = {
    "Q8BG67": "mouse Efr3a",
    "Q14156": "human EFR3A",
    "Q6ZQ18": "mouse Efr3b",
    "Q15517": "human CDSN",
}


def fetch(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    with urllib.request.urlopen(url) as fh:
        return json.load(fh)


def panther_ids(entry: dict) -> list[str]:
    return [
        x["id"]
        for x in entry.get("uniProtKBCrossReferences", [])
        if x["database"] == "PANTHER"
    ]


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(a, b)[0]
    matches = 0
    aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        seg1, seg2 = a[s1:e1], b[s2:e2]
        aligned += len(seg1)
        matches += sum(x == y for x, y in zip(seg1, seg2))
    return 100.0 * matches / min(len(a), len(b)), aligned


def main() -> None:
    entries = {acc: fetch(acc) for acc in ACCESSIONS}
    seqs = {acc: e["sequence"]["value"] for acc, e in entries.items()}
    print("## Records")
    for acc, label in ACCESSIONS.items():
        genes = [g["geneName"]["value"] for g in entries[acc].get("genes", [])]
        print(f"{acc}\t{label}\tgene={genes}\tlength={len(seqs[acc])}\tPANTHER={panther_ids(entries[acc])}")
    print()
    print("## Global alignment identity vs mouse Efr3a (Q8BG67), % of shorter sequence")
    for acc in ["Q14156", "Q6ZQ18", "Q15517"]:
        pid, aligned = identity(seqs["Q8BG67"], seqs[acc])
        print(f"Q8BG67 vs {acc} ({ACCESSIONS[acc]}): identity={pid:.1f}% aligned_positions={aligned}")
    print()
    m = seqs["Q8BG67"]
    print("## Experimentally tested residues in mouse Efr3a (1-based)")
    print(f"residues 6-9: {m[5:9]}")
    for pos, expected in [(50, "K"), (53, "R"), (61, "R"), (68, "R"), (70, "R")]:
        obs = m[pos - 1]
        print(f"position {pos}: expected {expected}, observed {obs}, match={obs == expected}")


if __name__ == "__main__":
    main()
