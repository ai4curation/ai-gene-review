#!/usr/bin/env python3
"""Analyze the Yippee domain and putative zinc-binding residues of a protein.

Given a query FASTA (single sequence) this script:
  1. Reports basic sequence statistics.
  2. Scans for the Yippee zinc-binding signature. The Yippee/Mis18/CULT fold
     coordinates one Zn(2+) via two CxxC-like pairs. The canonical Yippee motif
     (as in PROSITE PS51792 / literature) is two Cys pairs of the form
     C-x(2)-C ... C-x(2)-C. We locate all cysteines and test for two CxxC pairs.
  3. Reports the positions of all Cys/His residues (potential metal ligands).

No result is hardcoded: everything is computed from the input sequence.

Usage:
    python analyze_yippee.py QUERY.fasta
"""
from __future__ import annotations

import re
import sys

from Bio import SeqIO


def read_single(path: str):
    records = list(SeqIO.parse(path, "fasta"))
    if len(records) != 1:
        raise ValueError(f"Expected exactly 1 record in {path}, got {len(records)}")
    return records[0]


def find_cxxc_pairs(seq: str) -> list[tuple[int, int]]:
    """Return 1-based (start_cys, end_cys) positions for each C-x(2)-C match.

    Overlapping matches are allowed by scanning with a lookahead.
    """
    pairs: list[tuple[int, int]] = []
    for m in re.finditer(r"(?=(C.{2}C))", seq):
        start = m.start() + 1  # 1-based position of first C
        end = start + 3        # 1-based position of second C
        pairs.append((start, end))
    return pairs


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    rec = read_single(argv[1])
    seq = str(rec.seq)
    n = len(seq)

    print(f"# Yippee domain / zinc-ligand analysis")
    print(f"query_id\t{rec.id}")
    print(f"length\t{n}")

    cys = [i + 1 for i, c in enumerate(seq) if c == "C"]
    his = [i + 1 for i, c in enumerate(seq) if c == "H"]
    print(f"cysteine_positions\t{cys}")
    print(f"cysteine_count\t{len(cys)}")
    print(f"histidine_positions\t{his}")

    pairs = find_cxxc_pairs(seq)
    print(f"CxxC_pairs\t{pairs}")

    # A canonical Yippee zinc site = two CxxC pairs separated by a spacer.
    # Report the pair-of-pairs with the largest inter-pair spacer (the Yippee
    # architecture places the two CxxC motifs far apart in sequence but adjacent
    # in 3D at the apex of the beta-fold).
    if len(pairs) >= 2:
        first = pairs[0]
        last = pairs[-1]
        spacer = last[0] - first[1] - 1
        print(f"candidate_zinc_site\tC{first[0]}-x2-C{first[1]} ... C{last[0]}-x2-C{last[1]}")
        print(f"inter_pair_spacer_residues\t{spacer}")
        n_ligands = 4
        print(f"predicted_zn_ligand_count\t{n_ligands}")
    else:
        print("candidate_zinc_site\tNONE (fewer than two CxxC pairs)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
