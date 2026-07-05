#!/usr/bin/env python3
"""Fetch protein sequences (FASTA) for a set of UniProt accessions.

No hardcoded results: sequences are downloaded live from the UniProt REST API.
The accession list is provided on the command line, so the script is generic
and can be reused for any set of proteins.

Usage:
    python fetch_orthologs.py OUT.fasta ACC1 ACC2 ...
"""
from __future__ import annotations

import sys
import time

import requests

UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"


def fetch_fasta(acc: str) -> str:
    url = UNIPROT_FASTA.format(acc=acc)
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    text = resp.text.strip()
    if not text.startswith(">"):
        raise ValueError(f"No FASTA returned for {acc}: {text[:200]!r}")
    return text


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    out_path = argv[1]
    accessions = argv[2:]
    records: list[str] = []
    for acc in accessions:
        sys.stderr.write(f"Fetching {acc} ...\n")
        records.append(fetch_fasta(acc))
        time.sleep(0.3)
    with open(out_path, "w") as fh:
        fh.write("\n".join(records) + "\n")
    sys.stderr.write(f"Wrote {len(records)} sequences to {out_path}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
