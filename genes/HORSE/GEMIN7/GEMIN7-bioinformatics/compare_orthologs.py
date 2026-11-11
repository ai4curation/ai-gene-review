# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Global pairwise comparison of horse GEMIN7 (A0A9L0T0I7) with characterised
PTHR14679:SF1 members (human, mouse, bovine GEMIN7; S. pombe gem7).

Sequences are fetched live from UniProt REST. Results printed as a markdown table.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "A0A9L0T0I7"
OTHERS = {"Q9H840": "human GEMIN7", "Q9CWY4": "mouse Gemin7",
          "Q17QA0": "bovine GEMIN7", "G2TRR1": "S. pombe gem7"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

q = fetch(QUERY)
print(f"Query {QUERY} length {len(q)}\n")
print("| accession | name | length | aligned identical | identity over shorter seq |")
print("|---|---|---|---|---|")
for acc, name in OTHERS.items():
    s = fetch(acc)
    aln = aligner.align(q, s)[0]
    ident = sum(1 for a, b in zip(*aln) if a == b and a != "-")
    print(f"| {acc} | {name} | {len(s)} | {ident} | {100*ident/min(len(q), len(s)):.1f}% |")
    if acc == "Q9H840":
        print("\n```\n" + str(aln) + "```\n")
