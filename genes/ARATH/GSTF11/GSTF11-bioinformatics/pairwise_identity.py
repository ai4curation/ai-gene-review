"""Global pairwise identity of GSTF11 (At3g03190) against the two Kiyosue et al. 1993
dehydration-inducible phi GSTs: ERD11 (= GSTF6, At1g02930) and ERD13 (= GSTF10, At2g30870).

Question: could the aluminium-induced "GST" clone of Richards et al. 1998 (PMID:9449849),
reported as >98% identical to the Kiyosue et al. 1993 GST, correspond to GSTF11?

Sequences are read from UniProt flat files:
  - ../GSTF11-uniprot.txt                       (GSTF11, in-repo)
  - ../../GSTF6/GSTF6-uniprot.txt               (GSTF6 / ERD11, in-repo)
  - P42761-GSTF10-ERD13-uniprot.txt             (GSTF10 / ERD13, downloaded from
                                                  https://rest.uniprot.org/uniprotkb/P42761.txt)

Alignment: Needleman-Wunsch global alignment (Biopython PairwiseAligner) with BLOSUM62,
gap open -10, gap extend -0.5 (EMBOSS needle defaults). Identity is reported both as
identical positions / alignment length (EMBOSS convention, gaps included) and as
identical positions / length of the shorter sequence.

Run:
  /home/user/ai-gene-review/.venv/bin/python pairwise_identity.py
"""

from itertools import combinations
from pathlib import Path

from Bio import Align, SwissProt
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
FILES = {
    "GSTF11": HERE.parent / "GSTF11-uniprot.txt",
    "GSTF6_ERD11": HERE.parent.parent / "GSTF6" / "GSTF6-uniprot.txt",
    "GSTF10_ERD13": HERE / "P42761-GSTF10-ERD13-uniprot.txt",
}


def load(path: Path):
    with open(path) as fh:
        rec = SwissProt.read(fh)
    return rec.accessions[0], rec.gene_name, rec.sequence


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10.0
    a.extend_gap_score = -0.5
    # EMBOSS needle does not penalise end gaps by default
    a.end_gap_score = 0.0
    return a


def identity(aln, s1: str, s2: str):
    a1, a2 = aln[0], aln[1]
    length = len(a1)
    ident = sum(1 for x, y in zip(a1, a2) if x == y and x != "-")
    return ident, length, ident / length, ident / min(len(s1), len(s2))


def main() -> None:
    seqs = {}
    for name, path in FILES.items():
        acc, gn, seq = load(path)
        seqs[name] = seq
        name_field = gn[0].get("Name", "") if gn else ""
        print(f"{name}\t{acc}\tlength={len(seq)}\tGN={name_field.split(' ')[0]}")
    print()
    al = aligner()
    print("pair\tidentical\taln_length\tidentity_over_alignment\tidentity_over_shorter")
    for n1, n2 in combinations(FILES, 2):
        best = al.align(seqs[n1], seqs[n2])[0]
        ident, length, f_aln, f_short = identity(best, seqs[n1], seqs[n2])
        print(f"{n1} vs {n2}\t{ident}\t{length}\t{f_aln:.1%}\t{f_short:.1%}")


if __name__ == "__main__":
    main()
