# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython", "requests"]
# ///
"""Compare donkey SAT1 (A0A9L0KCT9) with human SAT1 (P21673, PANTHER SF36) and
human SAT2 (Q96F10, PANTHER SF51), fetched from UniProt REST.

Usage: uv run --script compare_paralogs_rereview.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"donkey_SAT1": "A0A9L0KCT9", "human_SAT1": "P21673", "human_SAT2": "Q96F10"}
# Human SAT1 residues: Tyr140 general acid, Glu92 general base (PMID:17516632)
SITES = [92, 140]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    q = seqs["donkey_SAT1"]
    for name in ("human_SAT1", "human_SAT2"):
        t = seqs[name]
        a = al.align(q, t)[0]
        pairs = []
        for (qs, qe), (ts, te) in zip(*a.aligned):
            for i, j in zip(range(qs, qe), range(ts, te)):
                pairs.append((i, j))
        ident = sum(q[i] == t[j] for i, j in pairs)
        print(f"donkey_SAT1 vs {name} ({ACCS[name]}, {len(t)} aa): "
              f"{ident}/{len(pairs)} identical paired residues = {100*ident/len(pairs):.1f}%")
    # map human SAT1 catalytic residues onto donkey
    h = seqs["human_SAT1"]
    for p in SITES:
        print(f"human SAT1 {h[p-1]}{p} -> donkey {q[p-1]}{p}")
    print(f"donkey length {len(q)}")


if __name__ == "__main__":
    main()
