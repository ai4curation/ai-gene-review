#!/usr/bin/env python3
"""Run a parameterized global protein alignment and report pairwise identity."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--alignment-output", required=True, type=Path)
    parser.add_argument("--match-score", type=float, default=2.0)
    parser.add_argument("--mismatch-score", type=float, default=-1.0)
    parser.add_argument("--gap-open-score", type=float, default=-5.0)
    parser.add_argument("--gap-extend-score", type=float, default=-0.5)
    return parser.parse_args()


def read_single_fasta(path: Path) -> tuple[str, str]:
    records = list(SeqIO.parse(path, "fasta"))
    if len(records) != 1:
        raise ValueError(f"{path} must contain exactly one FASTA record")
    return records[0].id, str(records[0].seq)


def sha256(sequence: str) -> str:
    return hashlib.sha256(sequence.encode("ascii")).hexdigest()


def alignment_label(record_id: str) -> str:
    """Use the accession from a standard UniProt FASTA identifier."""
    fields = record_id.split("|")
    if len(fields) == 3 and fields[0] in {"sp", "tr"}:
        return fields[1]
    return record_id


def main() -> None:
    args = parse_args()
    query_id, query_sequence = read_single_fasta(args.query)
    target_id, target_sequence = read_single_fasta(args.target)

    aligner = PairwiseAligner(
        mode="global",
        match_score=args.match_score,
        mismatch_score=args.mismatch_score,
        open_gap_score=args.gap_open_score,
        extend_gap_score=args.gap_extend_score,
    )
    alignment = aligner.align(
        SeqRecord(Seq(query_sequence), id=alignment_label(query_id)),
        SeqRecord(Seq(target_sequence), id=alignment_label(target_id)),
    )[0]

    aligned_pairs: list[tuple[int, int]] = []
    for (query_start, query_end), (target_start, target_end) in zip(
        *alignment.aligned, strict=True
    ):
        aligned_pairs.extend(
            zip(
                range(query_start, query_end),
                range(target_start, target_end),
                strict=True,
            )
        )
    identical_pairs = sum(
        query_sequence[query_index] == target_sequence[target_index]
        for query_index, target_index in aligned_pairs
    )
    aligned_pair_count = len(aligned_pairs)
    identity_percent = 100.0 * identical_pairs / aligned_pair_count

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.alignment_output.parent.mkdir(parents=True, exist_ok=True)
    fields = {
        "query_id": query_id,
        "query_length": len(query_sequence),
        "query_sha256": sha256(query_sequence),
        "target_id": target_id,
        "target_length": len(target_sequence),
        "target_sha256": sha256(target_sequence),
        "alignment_columns": alignment.shape[1],
        "aligned_residue_pairs": aligned_pair_count,
        "identical_residue_pairs": identical_pairs,
        "identity_percent": f"{identity_percent:.4f}",
        "alignment_score": f"{alignment.score:.4f}",
        "match_score": args.match_score,
        "mismatch_score": args.mismatch_score,
        "gap_open_score": args.gap_open_score,
        "gap_extend_score": args.gap_extend_score,
        "biopython_version": __import__("Bio").__version__,
    }
    with args.output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=fields,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow(fields)
    args.alignment_output.write_text(
        str(alignment).rstrip() + "\n",
        encoding="utf-8",
    )
    print(args.output)
    print(args.alignment_output)


if __name__ == "__main__":
    main()
