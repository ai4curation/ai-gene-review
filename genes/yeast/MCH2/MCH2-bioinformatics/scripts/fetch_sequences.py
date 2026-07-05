#!/usr/bin/env python3
"""Fetch protein sequences from UniProt for MCH2 comparative analysis.

Downloads FASTA sequences for a configurable set of UniProt accessions and
writes them to an output FASTA file. No sequences are hardcoded; only
accession IDs (identifiers, not data) are specified.

Usage:
    python fetch_sequences.py --accessions accessions.tsv --out data/panel.fasta
"""
import argparse
import sys
import time
from pathlib import Path

import requests

UNIPROT_FASTA_URL = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"


def fetch_fasta(acc: str, retries: int = 3, pause: float = 1.0) -> str:
    """Fetch a single FASTA record from UniProt by accession."""
    url = UNIPROT_FASTA_URL.format(acc=acc)
    last_err = None
    for attempt in range(retries):
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200 and resp.text.startswith(">"):
            return resp.text.strip() + "\n"
        last_err = f"HTTP {resp.status_code}"
        time.sleep(pause * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {acc}: {last_err}")


def read_accessions(path: Path) -> list[tuple[str, str]]:
    """Read a TSV of accession<TAB>label lines (comment lines start with #)."""
    entries = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        acc = parts[0].strip()
        label = parts[1].strip() if len(parts) > 1 else acc
        entries.append((acc, label))
    return entries


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--accessions", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    entries = read_accessions(args.accessions)
    if not entries:
        print("No accessions provided", file=sys.stderr)
        return 1

    records = []
    for acc, label in entries:
        print(f"Fetching {acc} ({label})...", file=sys.stderr)
        fasta = fetch_fasta(acc)
        # Rewrite the header to a clean, stable label while preserving the accession
        seq_lines = fasta.splitlines()
        header = f">{acc}|{label}"
        body = "\n".join(seq_lines[1:])
        records.append(f"{header}\n{body}\n")
        time.sleep(0.3)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("".join(records))
    print(f"Wrote {len(records)} sequences to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
