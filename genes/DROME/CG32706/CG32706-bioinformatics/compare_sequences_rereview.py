"""Re-review: pairwise global alignment of CG32706 (Q8IRM9) with PANTHER PTHR12311:SF7
members human ABT1 (Q9ULW3) and budding-yeast Esf2 (P53743).

Fetches sequences live from UniProt REST and reports length, identity and similarity
over aligned columns. Run: uv run --with biopython --with requests compare_sequences_rereview.py
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"Q8IRM9": "CG32706 (fly)", "Q9ULW3": "ABT1 (human)", "P53743": "ESF2 (S. cerevisiae)"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    for a, s in seqs.items():
        print(f"{a}\t{ACCS[a]}\tlength={len(s)}")
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    blosum = aligner.substitution_matrix
    q = seqs["Q8IRM9"]
    for t in ("Q9ULW3", "P53743"):
        aln = aligner.align(q, seqs[t])[0]
        ident = sim = cols = 0
        for (qs, qe), (ts, te) in zip(*aln.aligned):
            for i, j in zip(range(qs, qe), range(ts, te)):
                cols += 1
                if q[i] == seqs[t][j]:
                    ident += 1
                if blosum[q[i]][seqs[t][j]] > 0:
                    sim += 1
        print(
            f"Q8IRM9 vs {t}: aligned_cols={cols} identity={ident / cols:.3f} "
            f"similarity={sim / cols:.3f} (identical={ident})"
        )
        print(aln)


if __name__ == "__main__":
    main()
