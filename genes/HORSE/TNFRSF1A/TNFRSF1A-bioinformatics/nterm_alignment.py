# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Print the full global alignments of each horse TNFRSF1A model vs human P19438
(BLOSUM62, gap open -10, extend -0.5) so the N-terminal and CRD differences can be read."""
import requests
from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
human = fetch("P19438")
for acc in ["A0A5F5Q204", "F6YIE3", "A0A5F5PQM0"]:
    print(f"=== {acc} (query) vs P19438 (target)")
    print(al.align(fetch(acc), human)[0])
