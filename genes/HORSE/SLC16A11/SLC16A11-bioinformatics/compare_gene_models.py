# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare horse SLC16A11 gene models (F6YMY3 and other TrEMBL entries) to human Q8NCK7.

Fetches sequences live from UniProt REST, runs global alignments (BLOSUM62),
and reports identity, coverage of the human sequence, and terminal overhangs.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

HUMAN = "Q8NCK7"
HORSE = ["F6YMY3", "A0A9L0RBE3", "A0A5F5PX05", "A0A9L0SA34", "A0A9L0SMV2"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aligner.end_gap_score = 0  # free terminal gaps (overhangs)
    hs = fetch(HUMAN)
    print(f"{HUMAN}\tlength={len(hs)}")
    for acc in HORSE:
        eq = fetch(acc)
        aln = aligner.align(eq, hs)[0]
        coords = aln.aligned  # (eq_blocks, hs_blocks)
        ident = 0
        aligned = 0
        for (a0, a1), (b0, b1) in zip(*coords):
            for i, j in zip(range(a0, a1), range(b0, b1)):
                aligned += 1
                ident += eq[i] == hs[j]
        eq_start, eq_end = coords[0][0][0], coords[0][-1][1]
        hs_start, hs_end = coords[1][0][0], coords[1][-1][1]
        # human residues aligned to an identical horse residue = high-confidence coverage
        print(
            f"{acc}\tlength={len(eq)}\taligned_pairs={aligned}\tidentical={ident}"
            f"\tpct_identity_over_aligned={100*ident/aligned:.1f}"
            f"\thorse_aligned_span={eq_start+1}-{eq_end}\thuman_aligned_span={hs_start+1}-{hs_end}"
            f"\thorse_N_overhang={eq_start}\thorse_C_overhang={len(eq)-eq_end}"
        )
        # local identity in sliding windows of human positions, to locate divergent segments
        hmap = {}
        for (a0, a1), (b0, b1) in zip(*coords):
            for i, j in zip(range(a0, a1), range(b0, b1)):
                hmap[j] = eq[i] == hs[j]
        win = 40
        segs = []
        for s in range(0, len(hs) - win + 1, 20):
            v = sum(hmap.get(j, False) for j in range(s, s + win)) / win
            segs.append(f"{s+1}-{s+win}:{v:.2f}")
        print(f"  human-window identity ({win} aa): " + " ".join(segs))


if __name__ == "__main__":
    main()
