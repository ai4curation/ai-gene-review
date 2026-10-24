"""Compare rabbit G1TUN6 with UBE2L6 orthologs and the UBE2L3 paralog.

Fetches sequences from UniProt REST, runs global pairwise alignments
(BLOSUM62, gap open -10, extend -0.5) and reports identity, length and
whether the active-site Cys (UniProt ACT_SITE 86 in G1TUN6) aligns to a Cys.

Run: uv run --with biopython --with requests python compare_sequences.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "G1TUN6"
OTHERS = {
    "O14933": "human UBE2L6 (UbcH8)",
    "Q9QZU9": "mouse Ube2l6",
    "P68036": "human UBE2L3 (UbcH7)",
    "P68037": "mouse Ube2l3",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

t = fetch(TARGET)
print(f"{TARGET} length {len(t)}; residue 86 = {t[85]}")
for acc, name in OTHERS.items():
    s = fetch(acc)
    aln = aligner.align(t, s)[0]
    ident = 0
    pairs = 0
    cys_partner = None
    for (ts, te), (ss, se) in zip(*aln.aligned):
        for i, j in zip(range(ts, te), range(ss, se)):
            pairs += 1
            if t[i] == s[j]:
                ident += 1
            if i == 85:
                cys_partner = (j + 1, s[j])
    print(
        f"{acc}\t{name}\tlen={len(s)}\taligned_pairs={pairs}\t"
        f"identity={100 * ident / pairs:.1f}%\tG1TUN6_C86_aligns_to={cys_partner}"
    )
