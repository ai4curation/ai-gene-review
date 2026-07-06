#!/usr/bin/env python3
"""Fetch lightweight UniProt metadata for P. putida KT2440."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import requests


BASE_URL = "https://rest.uniprot.org/uniprotkb/search"
DEFAULT_QUERY = "proteome:UP000000556"
DEFAULT_OUTPUT = Path("projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv")
DEFAULT_FIELDS = [
    "accession",
    "id",
    "gene_names",
    "protein_name",
    "organism_id",
    "length",
    "reviewed",
    "annotation_score",
    "cc_function",
    "ec",
    "go_id",
    "xref_interpro",
    "xref_pfam",
    "xref_panther",
    "xref_kegg",
    "xref_biocyc",
    "xref_unipathway",
    "xref_refseq",
    "keyword",
]


def next_link(link_header: str | None) -> str | None:
    """Return the UniProt pagination URL from an RFC 5988 Link header."""
    if not link_header:
        return None
    match = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
    return match.group(1) if match else None


def fetch_tsv_lines(query: str, fields: list[str], size: int) -> Iterable[str]:
    """Yield TSV lines from UniProt, suppressing duplicate page headers."""
    session = requests.Session()
    params: dict[str, str | int] | None = {
        "query": f"({query})",
        "format": "tsv",
        "fields": ",".join(fields),
        "size": size,
    }
    url: str | None = BASE_URL
    first_page = True

    while url:
        response = session.get(url, params=params, timeout=60)
        response.raise_for_status()
        page_lines = response.text.splitlines()
        if page_lines:
            if first_page:
                yield from page_lines
            else:
                yield from page_lines[1:]
        first_page = False
        url = next_link(response.headers.get("Link"))
        params = None


def write_manifest(path: Path, query: str, fields: list[str], rows: int, size: int) -> None:
    manifest = path.with_suffix(".manifest.txt")
    manifest.write_text(
        "\n".join(
            [
                f"retrieved_utc: {datetime.now(timezone.utc).isoformat()}",
                f"source: {BASE_URL}",
                f"query: ({query})",
                f"format: tsv",
                f"size: {size}",
                f"fields: {','.join(fields)}",
                f"data_rows: {rows}",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download lightweight UniProt TSV metadata for PSEPK/KT2440."
    )
    parser.add_argument("--query", default=DEFAULT_QUERY, help="UniProt search query.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output TSV path.",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=500,
        help="UniProt page size.",
    )
    parser.add_argument(
        "--fields",
        default=",".join(DEFAULT_FIELDS),
        help="Comma-separated UniProt field list.",
    )
    args = parser.parse_args()

    fields = [field.strip() for field in args.fields.split(",") if field.strip()]
    args.output.parent.mkdir(parents=True, exist_ok=True)

    lines = list(fetch_tsv_lines(args.query, fields, args.size))
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    data_rows = max(len(lines) - 1, 0)
    write_manifest(args.output, args.query, fields, data_rows, args.size)
    print(f"Wrote {data_rows} UniProt records to {args.output}")


if __name__ == "__main__":
    main()
