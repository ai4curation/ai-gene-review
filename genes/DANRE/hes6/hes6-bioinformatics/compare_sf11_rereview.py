# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Pairwise global identity among PANTHER PTHR10985:SF11 (Transcription cofactor HES-6) members.

Fetches sequences live from UniProt REST; prints identity/similarity of each pair
(BLOSUM62, gap open -10, extend -0.5), and checks the C-terminal WRPW motif.
"""
import itertools
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q6P0J1": "zebrafish hes6/her13.2",
    "Q568A5": "zebrafish her13",
    "Q96HZ4": "human HES6",
    "Q9JHE6": "mouse Hes6",
    "O14503": "human BHLHE40 (out-group, other subfamily)",
    "Q14469": "human HES1 (out-group, other subfamily)",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
blosum = aligner.substitution_matrix

for a in ACCS:
    print(f"{a}\t{ACCS[a]}\tlen={len(seqs[a])}\tC-term={seqs[a][-4:]}")
print()
print("acc1\tacc2\tidentity\tsimilarity\taligned_cols")
for a, b in itertools.combinations(ACCS, 2):
    aln = aligner.align(seqs[a], seqs[b])[0]
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(x == y for x, y in cols)
    sim = sum(blosum[x][y] > 0 for x, y in cols)
    n = len(cols)
    print(f"{a}\t{b}\t{ident / n:.3f}\t{sim / n:.3f}\t{n}")
