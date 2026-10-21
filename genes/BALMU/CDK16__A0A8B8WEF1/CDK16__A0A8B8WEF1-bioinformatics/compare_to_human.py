# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Global alignment of blue whale CDK16 (A0A8B8WEF1) against human CDK16 (Q00536).

Reports identity and checks residues at experimentally studied human positions
(Ser12, Ser95, Ser119, Ser153 regulatory sites; Lys194 ATP-binding; Asp304 HRD
catalytic aspartate region; DFG motif), mapped through the alignment.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


whale = fetch("A0A8B8WEF1")
human = fetch("Q00536")
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(whale, human)[0]
wa, ha = aln[0], aln[1]
cols = len(wa)
ident = sum(1 for a, b in zip(wa, ha) if a == b and a != "-")
gaps = sum(1 for a, b in zip(wa, ha) if a == "-" or b == "-")
print(f"whale_length\t{len(whale)}")
print(f"human_length\t{len(human)}")
print(f"alignment_columns\t{cols}")
print(f"identical_positions\t{ident}")
print(f"gap_columns\t{gaps}")
print(f"percent_identity_over_human\t{100*ident/len(human):.2f}")

# map human position -> whale residue
hpos = wpos = 0
h2w = {}
for a, b in zip(wa, ha):
    if a != "-":
        wpos += 1
    if b != "-":
        hpos += 1
        h2w[hpos] = (wpos if a != "-" else None, a)
for p in [12, 95, 119, 153, 194, 286, 304, 322, 323, 324]:
    w, res = h2w[p]
    print(f"human_{human[p-1]}{p}\twhale_{res}{w}")
diffs = [(i + 1, human[i], h2w[i + 1][1]) for i in range(len(human)) if h2w[i + 1][1] != human[i]]
print("differences_human_pos_hres_wres\t" + ";".join(f"{p}{h}>{w}" for p, h, w in diffs))
