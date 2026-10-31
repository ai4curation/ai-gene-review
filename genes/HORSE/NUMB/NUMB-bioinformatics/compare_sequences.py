# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Global alignment of horse NUMB (A0A5F5PK46) against human NUMB (P49757,
canonical isoform 1) and mouse Numb (Q9QZS3).

Reports length, identity, and gap blocks (insertions/deletions relative to the
reference), so that isoform status (PTB 11-aa insert, PRR 48-aa insert) can be
read off. Also checks for the NPF and DPF endocytic motifs and the C-terminal
alpha-adaptin binding region.

Run: uv run --script compare_sequences.py
"""

import re
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent


def load(name: str) -> str:
    return str(next(SeqIO.parse(HERE / f"{name}.fasta", "fasta")).seq)


def gap_blocks(a: str, b: str):
    """Yield (kind, ref_pos, length) for gap runs in aligned strings a (query) and b (ref)."""
    blocks = []
    ref_pos = 0
    i = 0
    while i < len(a):
        if a[i] == "-" or b[i] == "-":
            kind = "deletion_in_query" if a[i] == "-" else "insertion_in_query"
            j = i
            while j < len(a) and (a[j] == "-") == (a[i] == "-") and (a[j] == "-" or b[j] == "-"):
                j += 1
            blocks.append((kind, ref_pos, j - i))
            if kind == "deletion_in_query":
                ref_pos += j - i
            i = j
        else:
            ref_pos += 1
            i += 1
    return blocks


def main() -> None:
    horse = load("A0A5F5PK46")
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    print(f"A0A5F5PK46 (horse) length: {len(horse)}")
    for ref_id in ["P49757", "Q9QZS3"]:
        ref = load(ref_id)
        aln = aligner.align(horse, ref)[0]
        a, b = aln[0], aln[1]
        ident = sum(1 for x, y in zip(a, b) if x == y and x != "-")
        print(f"\n== vs {ref_id} (length {len(ref)}) ==")
        print(f"identical positions: {ident}; identity over ref: {ident / len(ref):.3f}")
        for kind, pos, length in gap_blocks(a, b):
            print(f"  {kind}: {length} aa after ref position {pos}")
    for motif, pat in [("NPF", "NPF"), ("DPF", "DPF")]:
        hits = [m.start() + 1 for m in re.finditer(pat, horse)]
        print(f"\n{motif} motif positions in horse: {hits}")


if __name__ == "__main__":
    main()
