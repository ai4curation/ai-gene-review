# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Compare A0A8B6BFL6 with PTHR33050:SF7 members of known biology.

Inputs (FASTA, downloaded from UniProt REST into this folder):
  A0A8B6BFL6.fasta  target (Mytilus galloprovincialis)
  O96849.fasta      Dictyostelium DIRS-1 ORF2 (RT/RNase H), PTHR33050:SF7
  P03162.fasta      Duck hepatitis B virus polymerase P, PTHR33050:SF7
  O96848.fasta      Dictyostelium DIRS-1 ORF3 (tyrosine recombinase), PTHR31660

Reports pairwise local-alignment identity and lists conserved RT/RNase H
motif positions in the target. Run: uv run compare_sequences_rereview.py
"""

import random
import re
import statistics
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent


def load(acc: str) -> str:
    return str(next(SeqIO.parse(HERE / f"{acc}.fasta", "fasta")).seq)


def local_identity(a: str, b: str) -> dict:
    aligner = PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aln = aligner.align(a, b)[0]
    ident = 0
    cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += a[i] == b[j]
    return {
        "score": aln.score,
        "target_span": (aln.aligned[0][0][0] + 1, aln.aligned[0][-1][1]),
        "subject_span": (aln.aligned[1][0][0] + 1, aln.aligned[1][-1][1]),
        "aligned_columns": cols,
        "identity_pct": round(100 * ident / cols, 1) if cols else 0.0,
    }


def main() -> None:
    target = load("A0A8B6BFL6")
    print(f"target length: {len(target)}")
    for acc, label in [
        ("O96849", "DIRS-1 ORF2 RT/RNase H (DICDI, PTHR33050:SF7)"),
        ("P03162", "DHBV polymerase P (PTHR33050:SF7)"),
        ("O96848", "DIRS-1 ORF3 tyrosine recombinase (DICDI, PTHR31660)"),
    ]:
        subj = load(acc)
        r = local_identity(target, subj)
        rng = random.Random(42)
        null = []
        for _ in range(50):
            shuf = list(subj)
            rng.shuffle(shuf)
            null.append(local_identity(target, "".join(shuf))["score"])
        z = (r["score"] - statistics.mean(null)) / statistics.stdev(null)
        print(f"{acc} {label} len={len(subj)}: {r}")
        print(f"   shuffled-subject null (n=50): mean={statistics.mean(null):.1f} "
              f"sd={statistics.stdev(null):.1f} z={z:.1f}")

    # Polymerase motif C (YXDD) and RNase H candidate motifs.
    for name, pat in [
        ("RT motif C (Y/F-x-D-D)", r"[YF].DD"),
        ("RNase H 'SDA'-type first carboxylate", r"[ST]D[AG]"),
    ]:
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, target)]
        print(f"{name}: {hits}")


if __name__ == "__main__":
    main()
