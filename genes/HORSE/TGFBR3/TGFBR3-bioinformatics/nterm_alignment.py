# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Print the N-terminal 140 columns of the horse F7E1V2 vs human Q03167 TGFBR3 alignment,
and the cytoplasmic tail region, to inspect the signal-peptide region of the horse gene model."""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])

horse, human = fetch("F7E1V2"), fetch("Q03167")
al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5,
                           substitution_matrix=substitution_matrices.load("BLOSUM62"))
a = al.align(human, horse)[0]
s = str(a).splitlines()
print("\n".join(s[:12]))
