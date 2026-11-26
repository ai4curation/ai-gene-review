"""Pairwise global identity of B. subtilis YtcI (C0SPB0) to characterised PTHR43605:SF10 relatives.

Fetches sequences live from the UniProt REST API and aligns them with
Biopython's PairwiseAligner (global, BLOSUM62, gap open -10, extend -0.5).
Identity is reported over aligned (non-gap) columns and over the query length.
Run from the repository root:  uv run python genes/BACSU/ytcI/ytcI-bioinformatics/pairwise_identity.py
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "C0SPB0"  # B. subtilis YtcI
TARGETS = {
    "A0A0H2XHR6": "S. aureus USA300 MbcS (SAUSA300_2542), PMID:36806679",
    "A4YDT1": "M. sedula Msed_0406 4-hydroxybutyrate-CoA ligase, PMID:23258541",
    "Q88KS6": "P. putida PP_2213 (uncharacterised)",
    "Q08AH3": "human ACSM2A (mitochondrial medium-chain acyl-CoA synthetase)",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    q = fetch(QUERY)
    print(f"query\t{QUERY}\tlength={len(q)}")
    print("target\tdescription\tlength\taligned_cols\tidentical\tpct_id_aligned\tpct_id_query")
    for acc, desc in TARGETS.items():
        t = fetch(acc)
        aln = aligner.align(q, t)[0]
        ident = aligned = 0
        for (qs, qe), (ts, te) in zip(*aln.aligned):
            for i, j in zip(range(qs, qe), range(ts, te)):
                aligned += 1
                ident += q[i] == t[j]
        print(f"{acc}\t{desc}\t{len(t)}\t{aligned}\t{ident}\t{100*ident/aligned:.1f}\t{100*ident/len(q):.1f}")


if __name__ == "__main__":
    main()
