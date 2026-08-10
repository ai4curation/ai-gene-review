#!/usr/bin/env python3
"""Fetch canonical UniProtKB FASTA records for explicit accessions."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.request import urlopen


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("accessions", nargs="+", help="UniProtKB accessions")
    parser.add_argument("--output-dir", required=True, type=Path)
    return parser.parse_args()


def fetch_fasta(accession: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    with urlopen(url, timeout=60) as response:
        text = response.read().decode("utf-8")
    if not text.startswith(">") or "\n" not in text:
        raise ValueError(f"UniProtKB returned an invalid FASTA record for {accession}")
    sequence = "".join(
        line.strip() for line in text.splitlines() if not line.startswith(">")
    )
    if not sequence.isalpha():
        raise ValueError(
            f"UniProtKB returned an invalid protein sequence for {accession}"
        )
    return text.rstrip() + "\n"


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for accession in args.accessions:
        output = args.output_dir / f"{accession}.fasta"
        output.write_text(fetch_fasta(accession), encoding="utf-8")
        print(output)


if __name__ == "__main__":
    main()
