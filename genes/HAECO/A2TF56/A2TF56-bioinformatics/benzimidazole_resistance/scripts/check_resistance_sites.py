#!/usr/bin/env python3
"""Map beta-tubulin resistance-site residues onto a target sequence."""

import argparse
import csv
import sys
from pathlib import Path


def read_fasta(path: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    current_id: str | None = None
    chunks: list[str] = []
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_id is not None:
                records[current_id] = "".join(chunks)
            current_id = line[1:].split()[0]
            chunks = []
        else:
            if current_id is None:
                raise ValueError(f"Sequence before FASTA header in {path}")
            chunks.append(line)
    if current_id is not None:
        records[current_id] = "".join(chunks)
    return records


def best_ungapped_offset(target: str, query: str) -> tuple[int, int, int]:
    """Place query onto target, allowing truncation at either sequence end."""
    best = (-10**9, 0, 0, 0)
    for offset in range(-len(query) + 1, len(target)):
        matches = 0
        compared = 0
        for query_index, residue in enumerate(query):
            target_index = offset + query_index
            if 0 <= target_index < len(target):
                compared += 1
                matches += residue == target[target_index]
        if compared == 0:
            continue
        mismatches = compared - matches
        score = matches - mismatches
        if (score, compared, matches, -abs(offset)) > best:
            best = (score, compared, matches, -abs(offset))
            best_offset = offset
    return best_offset, best[1], best[2]


def residue_at(sequence: str, one_based_position: int) -> str:
    return sequence[one_based_position - 1]


def residue_for_target_position(
    query: str, offset: int, one_based_position: int
) -> str:
    query_index = one_based_position - 1 - offset
    if not 0 <= query_index < len(query):
        return ""
    return query[query_index]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=Path, required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--positions", nargs="+", type=int, default=[167, 198, 200])
    args = parser.parse_args()

    records = read_fasta(args.fasta)
    target = records.get(args.target)
    if target is None:
        raise SystemExit(f"Target {args.target!r} not found in {args.fasta}")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    fieldnames = ["query", "offset", "compared", "matches", "identity"]
    for position in args.positions:
        fieldnames.extend([f"target_{position}", f"query_at_{position}"])
    writer.writerow(fieldnames)

    for query_id, query in records.items():
        if query_id == args.target:
            continue
        offset, compared, matches = best_ungapped_offset(target, query)
        identity = matches / compared
        row: list[str | int | float] = [
            query_id,
            offset,
            compared,
            matches,
            f"{identity:.3f}",
        ]
        for position in args.positions:
            row.extend(
                [
                    residue_at(target, position),
                    residue_for_target_position(query, offset, position),
                ]
            )
        writer.writerow(row)


if __name__ == "__main__":
    main()
