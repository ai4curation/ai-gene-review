"""Pairwise identity between the dimethylglycine-locus ETF subunits and the
canonical ETF paralogs of P. putida KT2440 and C. salexigens DSM 3043.

Fetches sequences from the UniProt REST API and reports global (Needleman-Wunsch,
BLOSUM62, gap open -10, extend -0.5) identity over aligned columns.

Run from the repository root:
    uv run python genes/PSEPK/PP_0312/PP_0312-bioinformatics/paralog_identity.py
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

LABELS = {
    "Q88R22": "PP_0312 (KT2440, dgc-locus ETF alpha)",
    "Q1QYV9": "Csal_0992 EtfA (C. salexigens, dgc-locus ETF alpha)",
    "Q88F97": "PP_4201 EtfA (KT2440, second ETF alpha)",
    "Q1QX41": "Csal_1614 (C. salexigens, second ETF alpha)",
    "P13804": "human ETFA",
    "Q88R21": "PP_0313 (KT2440, dgc-locus ETF beta)",
    "Q1QYV8": "Csal_0993 EtfB (C. salexigens, dgc-locus ETF beta)",
    "Q88F96": "PP_4202 EtfB (KT2440, second ETF beta)",
    "Q1QX42": "Csal_1613 (C. salexigens, second ETF beta)",
    "P38117": "human ETFB",
}
ALPHA = ["Q88R22", "Q1QYV9", "Q88F97", "Q1QX41", "P13804"]
BETA = ["Q88R21", "Q1QYV8", "Q88F96", "Q1QX42", "P38117"]


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def aligner():
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def identity(a, s1, s2):
    aln = a.align(s1, s2)[0]
    cols = [(i, j) for i, j in zip(aln[0], aln[1]) if i != "-" and j != "-"]
    same = sum(1 for i, j in cols if i == j)
    return same, len(cols)


def main():
    a = aligner()
    seqs = {acc: fetch(acc) for acc in LABELS}
    for group, accs in (("alpha", ALPHA), ("beta", BETA)):
        print(f"## ETF {group}")
        for acc in accs:
            print(f"- {acc} {LABELS[acc]}: {len(seqs[acc])} aa")
        print("| A | B | identical/aligned | identity |")
        print("|---|---|---|---|")
        for i, x in enumerate(accs):
            for y in accs[i + 1:]:
                same, n = identity(a, seqs[x], seqs[y])
                print(f"| {x} | {y} | {same}/{n} | {same / n:.1%} |")
        print()


if __name__ == "__main__":
    main()
