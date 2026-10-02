#!/usr/bin/env python3
"""Calculate global pairwise identities among like InterPro-defined regions."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from itertools import combinations
from pathlib import Path

from Bio import Align, SeqIO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def identity(alignment: Align.Alignment) -> tuple[int, int, float]:
    a, b = (str(row) for row in alignment)
    paired = [(x, y) for x, y in zip(a, b, strict=True) if x != "-" and y != "-"]
    matches = sum(x == y for x, y in paired)
    aligned = len(paired)
    return matches, aligned, 100.0 * matches / aligned if aligned else 0.0


def main() -> None:
    args = parse_args()
    groups = defaultdict(list)
    for record in SeqIO.parse(args.regions, "fasta"):
        accession, domain, coordinates = record.id.split("|")
        groups[domain].append((accession, coordinates, str(record.seq)))
    aligner = Align.PairwiseAligner(mode="global")
    aligner.match_score = 1.0
    aligner.mismatch_score = 0.0
    aligner.open_gap_score = -1.0
    aligner.extend_gap_score = -0.1
    rows = []
    for domain, records in sorted(groups.items()):
        for left, right in combinations(records, 2):
            alignment = aligner.align(left[2], right[2])[0]
            matches, aligned, percent = identity(alignment)
            rows.append(
                {
                    "domain": domain,
                    "accession_1": left[0],
                    "coordinates_1": left[1],
                    "accession_2": right[0],
                    "coordinates_2": right[1],
                    "identical_residues": matches,
                    "aligned_residue_pairs": aligned,
                    "percent_identity": f"{percent:.2f}",
                    "alignment_score": f"{alignment.score:.2f}",
                }
            )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
