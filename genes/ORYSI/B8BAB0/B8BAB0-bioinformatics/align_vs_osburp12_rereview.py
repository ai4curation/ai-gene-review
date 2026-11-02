"""Print the full global alignment of B8BAB0 (indica, OsI_29064) vs its japonica
allele Q6ZA27 (OsBURP12, Os08g0380100) to locate gene-model differences.
Run: uv run python align_vs_osburp12_rereview.py
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc: str) -> str:
    text = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode()
    return "".join(text.splitlines()[1:])


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    a, b = fetch("B8BAB0"), fetch("Q6ZA27")
    aln = aligner.align(a, b)[0]
    print(aln)
    blocks = list(zip(*aln.aligned))
    print("Aligned blocks (B8BAB0 range -> Q6ZA27 range, 0-based half-open):")
    for (s1, e1), (s2, e2) in blocks:
        print(f"  {s1}-{e1} -> {s2}-{e2}")


if __name__ == "__main__":
    main()
