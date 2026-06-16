#!/usr/bin/env python3
"""Fetch protein sequences (query + references) from the UniProt REST API.

Reads accessions from a TSV config (default: data/reference_accessions.tsv) and
writes a single multi-FASTA. No sequences are hardcoded; everything is fetched
live from UniProt so the analysis is reproducible from the accession list alone.

Usage:
    uv run python scripts/fetch_sequences.py \
        --accessions data/reference_accessions.tsv \
        --out data/sequences.fasta
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import requests

UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"


def read_accessions(path: Path) -> list[tuple[str, str]]:
    """Return list of (accession, label) from a TSV with header row."""
    rows: list[tuple[str, str]] = []
    with path.open() as fh:
        header = fh.readline().rstrip("\n").split("\t")
        acc_i = header.index("accession")
        lab_i = header.index("label")
        for line in fh:
            if not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            rows.append((parts[acc_i], parts[lab_i]))
    return rows


def fetch_fasta(acc: str, retries: int = 4) -> str:
    """Fetch a single FASTA record from UniProt with simple backoff."""
    url = UNIPROT_FASTA.format(acc=acc)
    for attempt in range(retries):
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200 and resp.text.startswith(">"):
            return resp.text.strip()
        time.sleep(2 ** attempt)
    raise RuntimeError(f"Failed to fetch {acc} from UniProt (last status {resp.status_code})")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--accessions", type=Path, default=Path("data/reference_accessions.tsv"))
    ap.add_argument("--out", type=Path, default=Path("data/sequences.fasta"))
    args = ap.parse_args()

    accs = read_accessions(args.accessions)
    if not accs:
        print("No accessions found", file=sys.stderr)
        return 1

    records: list[str] = []
    for acc, label in accs:
        fasta = fetch_fasta(acc)
        # Re-header with our label||accession so downstream labels are stable,
        # but keep the original UniProt description for provenance.
        first, *rest = fasta.splitlines()
        orig_desc = first[1:]
        new_header = f">{label}|{acc} {orig_desc}"
        records.append("\n".join([new_header, *rest]))
        print(f"  fetched {acc:12s} {label}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(records) + "\n")
    print(f"Wrote {len(records)} sequences to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
