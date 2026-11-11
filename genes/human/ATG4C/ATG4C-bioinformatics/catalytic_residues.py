# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Check conservation of the ATG4 catalytic triad in human ATG4C relative to ATG4B.

Fetches sequences from UniProt REST, aligns each against human ATG4C (Q96DT6)
with a global BLOSUM62 alignment, and reports percent identity plus the residue
aligned to each ATG4C catalytic-triad position (Cys111, Asp345, His347, as
annotated by UniProt by similarity to ATG4B Cys74/Asp278/His280).
Results are printed, not hardcoded.
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "Q96DT6"  # human ATG4C
OTHERS = {
    "Q9Y4P1": "human ATG4B",
    "Q8WYN0": "human ATG4A",
    "Q86TL0": "human ATG4D",
    "Q811C2": "mouse Atg4c",
    "A0A9L0IIU3": "donkey ATG4C (TrEMBL)",
}
TRIAD = [111, 345, 347]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    q = fetch(QUERY)
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    print(f"query {QUERY} length {len(q)}; triad residues: "
          + ", ".join(f"{q[p-1]}{p}" for p in TRIAD))
    print("subject\tlabel\tlength\tidentity_over_aligned_cols\ttriad_in_subject")
    for acc, label in OTHERS.items():
        s = fetch(acc)
        aln = aligner.align(q, s)[0]
        qmap = {}
        ident = cols = 0
        for (qs, qe), (ss, se) in zip(*aln.aligned):
            for i in range(qe - qs):
                qmap[qs + i] = ss + i
                cols += 1
                ident += q[qs + i] == s[ss + i]
        triad = []
        for p in TRIAD:
            j = qmap.get(p - 1)
            triad.append(f"{s[j]}{j+1}" if j is not None else "gap")
        print(f"{acc}\t{label}\t{len(s)}\t{100*ident/cols:.1f}% ({ident}/{cols})\t{','.join(triad)}")


if __name__ == "__main__":
    main()
