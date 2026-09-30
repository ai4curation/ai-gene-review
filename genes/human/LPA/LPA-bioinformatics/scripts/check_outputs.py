#!/usr/bin/env python3
"""Fail if expected source and result records are missing or internally inconsistent."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--expected-accessions", nargs="+", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = json.loads((args.input_dir / "manifest.json").read_text())
    for record in manifest["records"]:
        path = args.input_dir.parent / record["path"]
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != record["sha256"]:
            raise ValueError(f"Checksum mismatch: {path}")
    with (args.output_dir / "record_summary.tsv").open() as handle:
        accessions = {row["accession"] for row in csv.DictReader(handle, delimiter="\t")}
    if accessions != set(args.expected_accessions):
        raise ValueError(f"Unexpected analyzed accessions: {accessions}")
    with (args.output_dir / "active_site_comparison.tsv").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != 3 * (len(args.expected_accessions) - 1):
        raise ValueError("Each target must have three mapped reference catalytic residues")
    print(f"PASS: verified {len(manifest['records'])} source files and {len(rows)} site mappings")


if __name__ == "__main__":
    main()
