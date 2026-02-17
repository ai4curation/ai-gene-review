#!/usr/bin/env python3
"""Download AlphaFold models for proteins in the collected record set."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def get_prediction_metadata(accession: str) -> dict[str, Any]:
    api_url = f"https://alphafold.ebi.ac.uk/api/prediction/{accession}"
    request = Request(api_url, headers={"User-Agent": "pmp20-bioinformatics/0.1"})
    with urlopen(request, timeout=60) as response:
        payload = response.read().decode("utf-8")
    data = json.loads(payload)
    if isinstance(data, list) and data:
        return data[0]
    if isinstance(data, dict):
        return data
    raise ValueError(f"Unexpected AlphaFold API response for {accession}")


def download_file(url: str, output_path: Path) -> None:
    request = Request(url, headers={"User-Agent": "pmp20-bioinformatics/0.1"})
    with urlopen(request, timeout=120) as response:
        content = response.read()
    output_path.write_bytes(content)


def write_manifest_tsv(rows: list[dict[str, Any]], path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "protein_id",
            "accession",
            "alphafold_lookup_accession",
            "status",
            "error",
            "pdb_url",
            "local_pdb_path",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proteins-json", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pdb_dir = args.output_dir / "pdb"
    pdb_dir.mkdir(parents=True, exist_ok=True)

    records = json.loads(args.proteins_json.read_text(encoding="utf-8"))
    manifest_rows: list[dict[str, Any]] = []

    for record in records:
        accession = record.get("accession", "")
        lookup_accession = record.get("alphafold_accession") or accession
        protein_id = record.get("protein_id", "")

        row: dict[str, Any] = {
            "protein_id": protein_id,
            "accession": accession,
            "alphafold_lookup_accession": lookup_accession,
            "status": "",
            "error": "",
            "pdb_url": "",
            "local_pdb_path": "",
        }

        if not lookup_accession:
            row["status"] = "skipped"
            row["error"] = "No accession available"
            manifest_rows.append(row)
            continue

        try:
            metadata = get_prediction_metadata(lookup_accession)
            pdb_url = metadata.get("pdbUrl")
            if not pdb_url:
                raise ValueError("AlphaFold metadata did not contain pdbUrl")

            output_path = pdb_dir / f"{protein_id}_{lookup_accession}.pdb"
            if not output_path.exists():
                download_file(pdb_url, output_path)

            row["status"] = "downloaded"
            row["pdb_url"] = pdb_url
            row["local_pdb_path"] = str(output_path)

        except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            row["status"] = "failed"
            row["error"] = str(exc)

        manifest_rows.append(row)

    manifest_json_path = args.output_dir / "alphafold_manifest.json"
    manifest_tsv_path = args.output_dir / "alphafold_manifest.tsv"
    manifest_json_path.write_text(json.dumps(manifest_rows, indent=2), encoding="utf-8")
    write_manifest_tsv(manifest_rows, manifest_tsv_path)

    print(f"Wrote {manifest_json_path}")
    print(f"Wrote {manifest_tsv_path}")


if __name__ == "__main__":
    main()
