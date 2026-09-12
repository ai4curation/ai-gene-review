#!/usr/bin/env python3
"""Download versioned direct records from official UniProt and InterPro APIs."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import requests


UNIPROT_BASE = "https://rest.uniprot.org/uniprotkb"
INTERPRO_BASE = "https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--accessions", nargs="+", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def get(session: requests.Session, url: str, timeout: int) -> requests.Response:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    return response


def write_bytes(path: Path, content: bytes) -> dict[str, object]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return {
        "path": path.as_posix(),
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
    }


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "ai-gene-review/LPA-protease-domain-analysis"})
    manifest: dict[str, object] = {
        "sources": {
            "uniprot": UNIPROT_BASE,
            "interpro": INTERPRO_BASE,
        },
        "records": [],
    }

    for accession in args.accessions:
        accession = accession.upper()
        json_url = f"{UNIPROT_BASE}/{accession}.json"
        fasta_url = f"{UNIPROT_BASE}/{accession}.fasta"
        interpro_url = f"{INTERPRO_BASE}/{accession}/?page_size=200"
        for source, url, suffix in (
            ("uniprot_json", json_url, ".json"),
            ("uniprot_fasta", fasta_url, ".fasta"),
            ("interpro_json", interpro_url, ".json"),
        ):
            response = get(session, url, args.timeout)
            relative = Path(source) / f"{accession}{suffix}"
            record = write_bytes(args.output_dir / relative, response.content)
            record.update(
                {
                    "accession": accession,
                    "source": source,
                    "url": url,
                    "etag": response.headers.get("ETag"),
                    "last_modified": response.headers.get("Last-Modified"),
                }
            )
            manifest["records"].append(record)
            time.sleep(0.1)

    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
