"""Pairwise local alignment identity between S. pombe Aah3, Aah1 and A. niger AgtA.

Purpose: check how close the ISS donor for the 4-alpha-glucanotransferase
annotation (UniProtKB:A2QTS4, AgtA, biochemically characterized in
PMID:17496125) is to Aah3 (Q9Y7S9) and Aah1 (O74922).

Run: uv run --with biopython python pairwise_identity.py
Sequences are fetched live from the UniProt REST API.
"""

import io
import urllib.request

from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

ACCESSIONS = {
    "Q9Y7S9": "S. pombe Aah3",
    "O74922": "S. pombe Aah1",
    "A2QTS4": "A. niger AgtA",
}
PAIRS = [("Q9Y7S9", "A2QTS4"), ("O74922", "A2QTS4"), ("Q9Y7S9", "O74922")]


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        text = fh.read().decode()
    return str(next(SeqIO.parse(io.StringIO(text), "fasta")).seq)


def main() -> None:
    seqs = {acc: fetch(acc) for acc in ACCESSIONS}
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    print("query\tsubject\tquery_len\tsubject_len\tidentities\taligned_pairs\tpct_identity")
    for q, s in PAIRS:
        aln = aligner.align(seqs[q], seqs[s])[0]
        c = aln.counts()
        n = c.identities + c.mismatches
        print(f"{q} ({ACCESSIONS[q]})\t{s} ({ACCESSIONS[s]})\t{len(seqs[q])}\t{len(seqs[s])}\t"
              f"{c.identities}\t{n}\t{100 * c.identities / n:.1f}")


if __name__ == "__main__":
    main()
