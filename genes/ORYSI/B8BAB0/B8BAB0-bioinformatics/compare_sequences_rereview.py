"""Pairwise global alignment of B8BAB0 against characterised PTHR31458 members.

Fetches sequences from UniProt REST and reports identity/coverage using
Biopython PairwiseAligner (BLOSUM62, gap open -10, extend -0.5).
Run: uv run python compare_sequences_rereview.py
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "B8BAB0"
COMPARATORS = {
    "Q6ZA27": "OsBURP12 (O. sativa japonica, Os08g0380100), PTHR31458:SF2",
    "Q7XES5": "OsBURP16 (O. sativa japonica), PTHR31458:SF2",
    "Q40161": "Tomato GP1 / PG1 beta subunit, PTHR31458:SF2",
    "O80760": "Arabidopsis PGL2 (AT1G70370), PTHR31458:SF2",
    "P92982": "Arabidopsis PGL1, PTHR31458:SF10",
    "P92990": "Arabidopsis PGL3, PTHR31458:SF10",
    "Q6K2M1": "OsBURP14, PTHR31458:SF4",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    return "".join(text.splitlines()[1:])


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    target = fetch(TARGET)
    print(f"{TARGET}\tlength={len(target)}")
    print("comparator\tdescription\tlength\tidentical\taligned_pairs\tidentity_over_aligned\tidentity_over_target")
    for acc, desc in COMPARATORS.items():
        seq = fetch(acc)
        aln = aligner.align(target, seq)[0]
        ident = 0
        pairs = 0
        for (s1, e1), (s2, e2) in zip(*aln.aligned):
            for i, j in zip(range(s1, e1), range(s2, e2)):
                pairs += 1
                if target[i] == seq[j]:
                    ident += 1
        print(f"{acc}\t{desc}\t{len(seq)}\t{ident}\t{pairs}\t{ident / pairs:.3f}\t{ident / len(target):.3f}")


if __name__ == "__main__":
    main()
