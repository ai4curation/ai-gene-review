#!/usr/bin/env python3
"""Download reviewed UniProtKB and InterPro records for a manifest of accessions."""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.request
from pathlib import Path


def fetch_json(url: str, attempts: int = 3) -> dict:
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/1.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except Exception:
            if attempt + 1 == attempts:
                raise
            time.sleep(2**attempt)
    raise RuntimeError("unreachable")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--uniprot-dir", type=Path, required=True)
    parser.add_argument("--interpro-dir", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.uniprot_dir.mkdir(parents=True, exist_ok=True)
    args.interpro_dir.mkdir(parents=True, exist_ok=True)
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    with args.manifest.open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    metadata = []
    for row in rows:
        accession = row["accession"]
        uniprot = fetch_json(f"https://rest.uniprot.org/uniprotkb/{accession}.json")
        if uniprot.get("entryType") != "UniProtKB reviewed (Swiss-Prot)":
            raise ValueError(f"{accession} is not a reviewed UniProtKB entry")
        observed = uniprot.get("primaryAccession")
        if observed != accession:
            raise ValueError(f"requested {accession}, received {observed}")
        interpro = fetch_json(
            f"https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/{accession}?format=json"
        )
        (args.uniprot_dir / f"{accession}.json").write_text(
            json.dumps(uniprot, indent=2, sort_keys=True) + "\n"
        )
        (args.interpro_dir / f"{accession}.json").write_text(
            json.dumps(interpro, indent=2, sort_keys=True) + "\n"
        )
        sequence = uniprot["sequence"]["value"]
        (args.uniprot_dir / f"{accession}.fasta").write_text(
            f">{accession}|{uniprot['uniProtkbId']}\n"
            + "\n".join(sequence[i : i + 60] for i in range(0, len(sequence), 60))
            + "\n"
        )
        genes = uniprot.get("genes", [])
        gene = genes[0].get("geneName", {}).get("value", "") if genes else ""
        organism = uniprot.get("organism", {})
        metadata.append(
            {
                **row,
                "uniprot_id": uniprot["uniProtkbId"],
                "gene": gene,
                "organism": organism.get("scientificName", ""),
                "taxon_id": organism.get("taxonId", ""),
                "length": len(sequence),
                "entry_version": uniprot.get("entryAudit", {}).get("entryVersion", ""),
                "annotation_date": uniprot.get("entryAudit", {}).get("lastAnnotationUpdateDate", ""),
            }
        )
    fields = list(metadata[0])
    with args.metadata.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(metadata)


if __name__ == "__main__":
    main()
