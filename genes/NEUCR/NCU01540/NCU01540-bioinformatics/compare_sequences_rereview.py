# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Global pairwise comparison of NCU01540 (Q7RWZ3) with the S. cerevisiae
Pho87/Pho90/Pho91 transporters and S. pombe plt1, and a check of the SPX
inositol-pyrophosphate-binding lysine corresponding to Pho91 K237
(PMID:41324358 used pho91-K237A).

Sequences are fetched live from UniProt REST. Output: results-rereview.json
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q7RWZ3": "NCU01540 (N. crassa; PTHR10283:SF92)",
    "P27514": "PHO91 (S. cerevisiae; SF92)",
    "O59712": "plt1 (S. pombe; SF92)",
    "P25360": "PHO87 (S. cerevisiae; SF110)",
    "P39535": "PHO90 (S. cerevisiae; SF110)",
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


def identity(a: str, b: str):
    aln = aligner.align(seqs[a], seqs[b])[0]
    s1, s2 = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(1 for x, y in pairs if x == y)
    return aln, ident, len(pairs)


def map_pos(aln, pos_b: int):
    """Map 1-based position in sequence B (target) to residue in sequence A (query)."""
    s1, s2 = aln[0], aln[1]
    ib = ia = 0
    for x, y in zip(s1, s2):
        if x != "-":
            ia += 1
        if y != "-":
            ib += 1
            if ib == pos_b:
                return (x, ia if x != "-" else None, y)
    return None


results = {"lengths": {a: len(s) for a, s in seqs.items()}, "pairwise": {}}
for other in ["P27514", "O59712", "P25360", "P39535"]:
    aln, ident, aligned = identity("Q7RWZ3", other)
    results["pairwise"][other] = {
        "label": ACCS[other],
        "identical": ident,
        "aligned_pairs": aligned,
        "pct_identity_over_aligned": round(100 * ident / aligned, 1),
    }

aln, _, _ = identity("Q7RWZ3", "P27514")
k = map_pos(aln, 237)
results["pho91_K237_equivalent"] = {
    "pho91_residue": seqs["P27514"][236],
    "ncu01540_residue": k[0] if k else None,
    "ncu01540_position": k[1] if k else None,
    "ncu01540_window": seqs["Q7RWZ3"][k[1] - 6 : k[1] + 5] if k and k[1] else None,
    "pho91_window": seqs["P27514"][231:242],
}
print(json.dumps(results, indent=2))
with open(__file__.replace("compare_sequences_rereview.py", "results-rereview.json"), "w") as fh:
    json.dump(results, fh, indent=2)
