# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Retrieve HID1-family members from UniProt, report their PANTHER subfamily, and
compute global pairwise identity to human HID1 (Q8IV36).

Run: uv run hid1_orthologs.py > RESULTS-orthologs.tsv

Nothing is hardcoded except the accession list; all subfamily assignments,
lengths and identities are computed from live UniProt records.
"""

import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "Q8IV36"
ACCESSIONS = [
    "Q8IV36",  # human HID1
    "Q8R1F6",  # mouse Hid1
    "D4A0C3",  # rat Hid1
    "Q0E9B5",  # Drosophila CG8841
    "G5EG65",  # C. elegans hid-1
    "O13776",  # S. pombe SPAC17A5.16
]

FIELDS = "accession,gene_primary,organism_name,length,xref_panther,sequence"


def fetch(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}?fields={FIELDS}&format=tsv"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    header, row = r.text.strip().split("\n")[:2]
    return dict(zip(header.split("\t"), row.split("\t")))


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(a, b)[0]
    ident = 0
    cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            if a[i] == b[j]:
                ident += 1
    return ident / cols if cols else 0.0, cols


def main() -> None:
    recs = {acc: fetch(acc) for acc in ACCESSIONS}
    qseq = recs[QUERY]["Sequence"]
    print("accession\tgene\torganism\tlength\tpanther\tidentity_to_Q8IV36\taligned_cols")
    for acc, r in recs.items():
        pid, cols = identity(qseq, r["Sequence"])
        print(
            f"{acc}\t{r['Gene Names (primary)']}\t{r['Organism']}\t{r['Length']}\t"
            f"{r['PANTHER']}\t{pid:.3f}\t{cols}"
        )
    sys.stdout.flush()


if __name__ == "__main__":
    main()
