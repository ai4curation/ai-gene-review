#!/usr/bin/env python3
"""Fetch the PANTHER family data associated with a cached gene record."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from ai_gene_review.etl.gene import (
    _extract_panther_family_id,
    _fetch_panther_family_data,
)


def find_panther_family(
    organism: str, gene: str, base_path: Path = Path(".")
) -> str:
    """Return the PANTHER family recorded in a gene's cached UniProt file."""
    uniprot_path = base_path / "genes" / organism / gene / f"{gene}-uniprot.txt"
    if not uniprot_path.is_file():
        raise FileNotFoundError(f"UniProt record not found: {uniprot_path}")

    family_id = _extract_panther_family_id(
        uniprot_path.read_text(encoding="utf-8")
    )
    if family_id is None:
        raise ValueError(f"No PANTHER family found in {uniprot_path}")
    return family_id


def main(argv: Sequence[str] | None = None) -> int:
    """Resolve the gene's PANTHER family and fetch its InterPro artifacts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("organism", help="Gene organism directory, e.g. yeast")
    parser.add_argument("gene", help="Gene symbol, e.g. YDJ1")
    parser.add_argument(
        "--base-path",
        type=Path,
        default=Path("."),
        help="Repository root (default: current directory)",
    )
    args = parser.parse_args(argv)

    try:
        family_id = find_panther_family(args.organism, args.gene, args.base_path)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Found PANTHER family {family_id} for {args.organism}/{args.gene}")
    if not _fetch_panther_family_data(family_id, args.base_path):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
