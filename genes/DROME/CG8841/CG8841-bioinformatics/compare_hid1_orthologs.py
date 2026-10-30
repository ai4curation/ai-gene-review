"""Compare Drosophila CG8841 (Q0E9B5) with experimentally studied PTHR21575:SF12 members.

Fetches sequences from UniProt REST, runs global pairwise alignments (BLOSUM62),
reports percent identity, and checks the N-terminal myristoylation motif (Gly2)
plus conservation of the C-terminal region (last 150 residues of each partner).
Usage: uv run --with biopython --with requests python compare_hid1_orthologs.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q0E9B5": "D. melanogaster CG8841",
    "Q8IV36": "H. sapiens HID1",
    "Q8R1F6": "M. musculus Hid1",
    "D4A0C3": "R. norvegicus Hid1",
    "Q9P7M6": "S. pombe hid3 (SPAC17A5.16)",
    "Q06673": "S. cerevisiae ECM30",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a: str, b: str, aligner: Align.PairwiseAligner) -> tuple[float, float]:
    aln = aligner.align(a, b)[0]
    matches = sum(1 for x, y in zip(aln[0], aln[1]) if x == y and x != "-")
    aligned = sum(1 for x, y in zip(aln[0], aln[1]) if x != "-" and y != "-")
    return 100 * matches / aligned, 100 * matches / len(a)


aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

seqs = {acc: fetch(acc) for acc in ACCS}
q = seqs["Q0E9B5"]
print(f"Q0E9B5 length {len(q)}; N-terminus {q[:8]}; Gly2={q[1] == 'G'}")
for acc, label in ACCS.items():
    if acc == "Q0E9B5":
        continue
    s = seqs[acc]
    pid_aln, pid_q = identity(q, s, aligner)
    ct_aln, _ = identity(q[-150:], s[-150:], aligner)
    print(
        f"{acc}\t{label}\tlen={len(s)}\tNterm={s[:8]}\tGly2={s[1] == 'G'}"
        f"\tid_over_aligned={pid_aln:.1f}%\tid_over_query={pid_q:.1f}%\tCterm150_id={ct_aln:.1f}%"
    )
