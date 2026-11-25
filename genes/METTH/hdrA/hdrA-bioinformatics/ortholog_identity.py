"""Global pairwise identity between M. thermautotrophicus Delta H subunits of the
MvhADG/HdrABC complex and their biochemically characterised M. marburgensis orthologs.

Usage: uv run python genes/METTH/hdrA/hdrA-bioinformatics/ortholog_identity.py
Fetches sequences from the UniProt REST API, aligns them with Biopython's
PairwiseAligner (global, BLOSUM62, gap open -10, extend -0.5) and prints
identity over aligned columns and over the shorter sequence. Also checks
cysteine conservation at the HdrB C-terminal CCG cluster ligands reported for
M. marburgensis HdrB (C153, C193, C194, C234; PMID:17929940).
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

PAIRS = [
    ("HdrA", "O27434", "Q50756"),
    ("HdrB", "O27907", "Q50755"),
    ("MvhA", "Q50783", "P60227"),
]


def fetch(acc):
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
        lines = r.read().decode().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def main():
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    seqs = {}
    for name, a, b in PAIRS:
        for acc in (a, b):
            seqs.setdefault(acc, fetch(acc))
        aln = aligner.align(seqs[a], seqs[b])[0]
        ident = cols = 0
        mapping = {}
        for (s1, e1), (s2, e2) in zip(*aln.aligned):
            for i, j in zip(range(s1, e1), range(s2, e2)):
                cols += 1
                ident += seqs[a][i] == seqs[b][j]
                mapping[j + 1] = i + 1
        short = min(len(seqs[a]), len(seqs[b]))
        print(f"{name}: {a} ({len(seqs[a])} aa) vs {b} ({len(seqs[b])} aa): "
              f"{ident}/{cols} aligned identical = {100*ident/cols:.1f}%; "
              f"{100*ident/short:.1f}% of shorter sequence")
        if name == "HdrB":
            for pos in (153, 193, 194, 234):
                q = mapping.get(pos)
                res_b = seqs[b][pos - 1]
                res_a = seqs[a][q - 1] if q else "-"
                print(f"  {b} {res_b}{pos} -> {a} {res_a}{q}")


if __name__ == "__main__":
    main()
