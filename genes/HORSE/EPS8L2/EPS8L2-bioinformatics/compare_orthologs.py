# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare horse EPS8L2 (F7BFV0) with human (Q9H6S3) and mouse (Q99K30) EPS8L2
and human EPS8 (Q12929) / EPS8L1 (Q8TE68) by global pairwise alignment.

Reports: lengths, percent identity over aligned columns, and the extent of any
terminal overhang of the horse model relative to each comparator.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "horse_EPS8L2": "F7BFV0",
    "human_EPS8L2": "Q9H6S3",
    "mouse_Eps8l2": "Q99K30",
    "human_EPS8L1": "Q8TE68",
    "human_EPS8": "Q12929",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {k: fetch(v) for k, v in ACCS.items()}
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.end_gap_score = 0  # free end gaps so terminal extensions show as overhangs

q = seqs["horse_EPS8L2"]
print(f"horse_EPS8L2 F7BFV0 length {len(q)}")
for name, s in seqs.items():
    if name == "horse_EPS8L2":
        continue
    aln = aligner.align(q, s)[0]
    a, b = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    ident = sum(1 for x, y in cols if x == y)
    # leading overhang of horse before comparator starts
    lead = 0
    for x, y in zip(a, b):
        if y == "-" and x != "-":
            lead += 1
        else:
            break
    print(
        f"{name} {ACCS[name]} length {len(s)}: aligned cols {len(cols)}, "
        f"identity {ident}/{len(cols)} = {100*ident/len(cols):.1f}%, "
        f"horse N-terminal overhang {lead} aa"
    )
    if name == "human_EPS8L2":
        start = q.find(s[:8])
        print(f"  exact match of human N-terminal 8-mer {s[:8]!r} in horse at position {start+1 if start>=0 else 'none'}")
        print(f"  horse residues before that: {q[:start] if start>0 else ''}")
