# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Map human GEMIN5 RNA-contact residues mutated in PMID:27881601 onto horse models.

Run: uv run check_residues_rereview.py
"""
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
# residues mutated in PMID:27881601 (human numbering, wild-type residue)
SITES = ["N13", "W14", "Y15", "R33", "R335", "M357", "R359", "F381", "Y383", "M403", "W422", "Y474"]


def load(acc):
    return str(next(SeqIO.parse(HERE / f"{acc}.fasta", "fasta")).seq)


def main():
    human = load("Q8TEQ6")
    al = PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                         open_gap_score=-10, extend_gap_score=-0.5,
                         end_insertion_score=0, end_deletion_score=0)
    for acc in ["A0A9L0R5P7", "F6WDM0"]:
        horse = load(acc)
        aln = al.align(human, horse)[0]
        hmap = {}
        for (ts, te), (qs, qe) in zip(*aln.aligned):
            for i, j in zip(range(ts, te), range(qs, qe)):
                hmap[i] = j
        out = []
        for s in SITES:
            aa, pos = s[0], int(s[1:])
            assert human[pos - 1] == aa, f"human numbering mismatch at {s}"
            j = hmap.get(pos - 1)
            out.append(f"{s}->{horse[j] + str(j + 1) if j is not None else 'gap'}")
        print(acc, " ".join(out))


if __name__ == "__main__":
    main()
