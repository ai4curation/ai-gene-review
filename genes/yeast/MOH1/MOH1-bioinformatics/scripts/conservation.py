#!/usr/bin/env python3
"""Pairwise conservation of a query protein vs a set of homologs.

For each homolog, performs a global pairwise alignment (BLOSUM62) against the
query and reports:
  - percent identity over aligned (non-gap) columns
  - alignment length
  - whether each user-specified query residue position maps to the SAME residue
    (identity), a similar residue, or a gap in the homolog.

This lets us test, e.g., whether the four putative Zn-binding cysteines of the
query are conserved in each homolog.

Nothing is hardcoded: query, homolog FASTA, and the positions to probe are all
supplied on the command line.

Usage:
    python conservation.py QUERY.fasta HOMOLOGS.fasta POS1,POS2,...
"""
from __future__ import annotations

import sys

from Bio import Align, SeqIO
from Bio.Align import substitution_matrices


def read_single(path: str):
    records = list(SeqIO.parse(path, "fasta"))
    if len(records) != 1:
        raise ValueError(f"Expected 1 record in {path}, got {len(records)}")
    return records[0]


def build_aligner() -> Align.PairwiseAligner:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    return aligner


def aligned_columns(alignment):
    """Yield (q_char, h_char) for each column of the top alignment."""
    q_aln, h_aln = alignment[0], alignment[1]
    for qc, hc in zip(q_aln, h_aln):
        yield qc, hc


def map_query_positions(alignment, positions_1based: list[int]) -> dict[int, str]:
    """For each 1-based query position, return the aligned homolog residue.

    Returns '-' if aligned to a gap, or the homolog char otherwise.
    """
    result: dict[int, str] = {}
    q_index = 0  # 0-based over ungapped query
    wanted = set(positions_1based)
    for qc, hc in aligned_columns(alignment):
        if qc != "-":
            q_index += 1
            if q_index in wanted:
                result[q_index] = hc
    return result


def pct_identity(alignment) -> tuple[float, int, int]:
    ident = 0
    cols = 0
    for qc, hc in aligned_columns(alignment):
        if qc == "-" or hc == "-":
            continue
        cols += 1
        if qc == hc:
            ident += 1
    pct = 100.0 * ident / cols if cols else 0.0
    return pct, ident, cols


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__)
        return 2
    query = read_single(argv[1])
    q_seq = str(query.seq)
    positions = [int(p) for p in argv[3].split(",") if p.strip()]

    for p in positions:
        if p < 1 or p > len(q_seq):
            raise ValueError(f"position {p} out of range 1..{len(q_seq)}")

    aligner = build_aligner()

    print("homolog_id\tlength\tpct_identity\tident/cols\t" +
          "\t".join(f"q{p}({q_seq[p-1]})" for p in positions))

    for hom in SeqIO.parse(argv[2], "fasta"):
        h_seq = str(hom.seq)
        aln = aligner.align(q_seq, h_seq)[0]
        pct, ident, cols = pct_identity(aln)
        mapped = map_query_positions(aln, positions)
        cells = []
        for p in positions:
            hc = mapped.get(p, "?")
            tag = "=" if hc == q_seq[p - 1] else ("~" if hc != "-" else "gap")
            cells.append(f"{hc}[{tag}]")
        print(f"{hom.id}\t{len(h_seq)}\t{pct:.1f}\t{ident}/{cols}\t" +
              "\t".join(cells))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
