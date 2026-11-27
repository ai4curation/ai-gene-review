# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "biopython"]
# ///
"""Compare donkey GEMIN7 (A0A9L0J5X5) with characterised GEMIN7 orthologs.

Fetches UniProt entries, reports PANTHER family/subfamily cross-references and
global pairwise identity (BLOSUM62, Needleman-Wunsch) to the donkey sequence.

Usage: uv run --script compare_orthologs.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "A0A9L0J5X5"
OTHERS = {
    "Q9H840": "human GEMIN7 (Swiss-Prot)",
    "Q17QA0": "bovine GEMIN7 (Swiss-Prot)",
    "A0A9L0T0I7": "horse GEMIN7",
    "A0A9L0ICL9": "donkey GEMIN7 long model",
    "G2TRR1": "S. pombe gem7 (Swiss-Prot)",
}


def fetch(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def panther(entry: dict) -> list[str]:
    return [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"]


def identity(a: str, b: str) -> tuple[int, int, float]:
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    cols = len(s1)
    return ident, cols, 100.0 * ident / cols


def main() -> None:
    t = fetch(TARGET)
    tseq = t["sequence"]["value"]
    print(f"{TARGET} donkey GEMIN7 length {len(tseq)} PANTHER {panther(t)} entryType {t['entryType']}")
    for acc, label in OTHERS.items():
        e = fetch(acc)
        seq = e["sequence"]["value"]
        ident, cols, pct = identity(tseq, seq)
        suffix = " (donkey seq is exact substring)" if tseq in seq else ""
        print(f"{acc} {label}: length {len(seq)} PANTHER {panther(e)} entryType {e['entryType']}; "
              f"identity {ident}/{cols} aligned columns = {pct:.1f}%{suffix}")


if __name__ == "__main__":
    main()
