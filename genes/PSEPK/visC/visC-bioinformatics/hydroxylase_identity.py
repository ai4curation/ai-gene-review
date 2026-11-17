#!/usr/bin/env python3
"""All-vs-all global identity among ubiquinone ring hydroxylases.

Reads protein sequences from UniProt flat files (the SQ block) given on the
command line and prints a table of pairwise percent identity from a global
Needleman-Wunsch alignment (BLOSUM62, gap open -10, gap extend -0.5).
Identity = identical aligned positions / aligned (non-gap) columns.

Usage (from the repository root):
  python genes/PSEPK/visC/visC-bioinformatics/hydroxylase_identity.py \
      genes/PSEPK/visC/visC-uniprot.txt genes/PSEPK/ubiH/ubiH-uniprot.txt \
      genes/ECOLI/ubiI/ubiI-uniprot.txt genes/ECOLI/ubiH/ubiH-uniprot.txt \
      genes/ECOLI/ubiF/ubiF-uniprot.txt
"""
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices


def read_uniprot(path: Path):
    acc, name, seq, in_sq = None, None, [], False
    for line in path.read_text().splitlines():
        if line.startswith("ID   ") and name is None:
            name = line.split()[1]
        elif line.startswith("AC   ") and acc is None:
            acc = line.split()[1].rstrip(";")
        elif line.startswith("SQ   "):
            in_sq = True
        elif line.startswith("//"):
            break
        elif in_sq:
            seq.append(line.replace(" ", ""))
    return acc, name, "".join(seq)


def identity(aligner, a, b):
    aln = aligner.align(a, b)[0]
    ident = cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += a[i] == b[j]
    return 100.0 * ident / cols, cols


def main(paths):
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    recs = [read_uniprot(Path(p)) for p in paths]
    for acc, name, seq in recs:
        print(f"# {acc}\t{name}\tlength={len(seq)}")
    print("query\ttarget\tpercent_identity\taligned_columns")
    for i, (a1, n1, s1) in enumerate(recs):
        for a2, n2, s2 in recs[i + 1:]:
            pid, cols = identity(aligner, s1, s2)
            print(f"{a1} {n1}\t{a2} {n2}\t{pid:.1f}\t{cols}")


if __name__ == "__main__":
    main(sys.argv[1:])
