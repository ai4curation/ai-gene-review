#!/usr/bin/env python3
"""Check whether S. pombe vms1 (O74977) retains the VLRF1 catalytic glutamine
that is experimentally required for polypeptidyl-tRNA cleavage in the
Vms1/ANKZF1 family.

Reference points (UniProt ACT_SITE features, PROSITE-ProRule:PRU01389):
  - Q9H8Y5 (human ANKZF1)          ACT_SITE 246; MUTAGEN Q246L abolishes
                                   polypeptidyl-tRNA cleavage
  - Q04311 (S. cerevisiae Vms1)    ACT_SITE 295
  - O74977 (S. pombe vms1)         ACT_SITE 249 (rule-inferred; this script
                                   tests whether the alignment supports it)

The script does global pairwise alignments (BLOSUM62) of the full-length
sequences and reports which residue in each query aligns to the reference
catalytic Gln, plus the local sequence context.

No result is hardcoded: everything printed is derived from the alignment.
"""

from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices
from Bio.SeqIO import parse

HERE = Path(__file__).parent

# accession -> (label, 1-based UniProt ACT_SITE position)
PROTEINS = {
    "Q9H8Y5": ("human ANKZF1", 246),
    "Q04311": ("S. cerevisiae Vms1", 295),
    "O74977": ("S. pombe vms1", 249),
}
REFERENCE = "Q9H8Y5"  # the only member with direct mutagenesis evidence
CONTEXT = 6


def load(acc: str) -> str:
    (record,) = parse(HERE / f"{acc}.fasta", "fasta")
    return str(record.seq)


def make_aligner() -> Align.PairwiseAligner:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    return aligner


def context(seq: str, pos1: int) -> str:
    """Sequence around a 1-based position, with the residue in brackets."""
    i = pos1 - 1
    lo, hi = max(0, i - CONTEXT), min(len(seq), i + CONTEXT + 1)
    return f"{seq[lo:i]}[{seq[i]}]{seq[i + 1:hi]}"


def projected_position(aligner, ref_seq: str, qry_seq: str, ref_pos1: int):
    """Return the 1-based query position aligned to ref_pos1, or None if gapped."""
    alignment = aligner.align(ref_seq, qry_seq)[0]
    ref_idx, qry_idx = alignment.indices  # -1 marks a gap
    target = ref_pos1 - 1
    for r, q in zip(ref_idx, qry_idx):
        if r == target:
            return (q + 1 if q >= 0 else None), alignment.score
    return None, alignment.score


def main() -> None:
    seqs = {acc: load(acc) for acc in PROTEINS}
    aligner = make_aligner()

    ref_label, ref_act = PROTEINS[REFERENCE]
    ref_seq = seqs[REFERENCE]
    print(f"Reference: {REFERENCE} ({ref_label}), {len(ref_seq)} aa")
    print(f"  annotated catalytic site {ref_act}: {context(ref_seq, ref_act)}")
    print()

    for acc, (label, act) in PROTEINS.items():
        if acc == REFERENCE:
            continue
        qry_seq = seqs[acc]
        pos, score = projected_position(aligner, ref_seq, qry_seq, ref_act)
        print(f"{acc} ({label}), {len(qry_seq)} aa  [alignment score {score:.1f}]")
        print(f"  UniProt ACT_SITE           : {act}  {context(qry_seq, act)}")
        if pos is None:
            print(f"  aligned to {REFERENCE}:{ref_act}      : GAP")
        else:
            print(
                f"  aligned to {REFERENCE}:{ref_act}      : "
                f"{pos}  {context(qry_seq, pos)}"
            )
            agree = "yes" if pos == act else "NO"
            print(f"  alignment agrees with ACT_SITE annotation: {agree}")
            print(f"  residue at aligned position: {qry_seq[pos - 1]}")
        print()


if __name__ == "__main__":
    main()
