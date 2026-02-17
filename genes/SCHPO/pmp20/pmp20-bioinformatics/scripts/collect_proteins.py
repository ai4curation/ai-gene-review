#!/usr/bin/env python3
"""Collect protein records from local UniProt TXT files or UniProt accessions."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def parse_location_token(token: str) -> tuple[int, int] | None:
    cleaned = token.replace("<", "").replace(">", "").replace("?", "").strip()
    if not cleaned:
        return None
    if ".." in cleaned:
        start_text, end_text = cleaned.split("..", 1)
    else:
        start_text, end_text = cleaned, cleaned
    if not start_text.isdigit() or not end_text.isdigit():
        return None
    return int(start_text), int(end_text)


def parse_uniprot_txt(text: str) -> dict[str, Any]:
    accessions: list[str] = []
    organism_lines: list[str] = []
    function_lines: list[str] = []
    act_sites: list[int] = []
    disulfid_pairs: list[list[int]] = []
    sequence_parts: list[str] = []

    entry_name = ""
    gene_name = ""
    alphafold_accession = ""

    in_sequence = False
    collecting_function = False

    for line in text.splitlines():
        if in_sequence:
            if line.startswith("//"):
                in_sequence = False
                continue
            sequence_parts.append(re.sub(r"[^A-Z]", "", line.upper()))
            continue

        if line.startswith("ID"):
            parts = line.split()
            if len(parts) > 1:
                entry_name = parts[1]
            continue

        if line.startswith("AC"):
            entries = [item.strip() for item in line[5:].split(";") if item.strip()]
            accessions.extend(entries)
            continue

        if line.startswith("GN") and not gene_name:
            match = re.search(r"Name=([^;\s]+)", line)
            if match:
                gene_name = match.group(1)
            continue

        if line.startswith("OS"):
            organism_lines.append(line[5:].strip())
            continue

        if line.startswith("CC   -!- FUNCTION:"):
            collecting_function = True
            function_lines.append(line.split("FUNCTION:", 1)[1].strip())
            continue

        if collecting_function:
            if line.startswith("CC       "):
                function_lines.append(line[9:].strip())
                continue
            collecting_function = False

        if line.startswith("DR   AlphaFoldDB;"):
            parts = [item.strip() for item in line.split(";")]
            if len(parts) >= 2:
                alphafold_accession = parts[1]
            continue

        if line.startswith("FT"):
            parts = line.split()
            if len(parts) >= 3 and parts[1] == "ACT_SITE":
                location = parse_location_token(parts[2])
                if location:
                    act_sites.append(location[0])
            if len(parts) >= 3 and parts[1] == "DISULFID":
                location = parse_location_token(parts[2])
                if location:
                    disulfid_pairs.append([location[0], location[1]])
            continue

        if line.startswith("SQ"):
            in_sequence = True
            continue

    sequence = "".join(sequence_parts)
    cysteine_positions = [index + 1 for index, aa in enumerate(sequence) if aa == "C"]

    return {
        "entry_name": entry_name,
        "accession": accessions[0] if accessions else "",
        "all_accessions": accessions,
        "gene_name": gene_name,
        "organism": " ".join(organism_lines).rstrip("."),
        "sequence": sequence,
        "sequence_length": len(sequence),
        "cysteine_positions": cysteine_positions,
        "act_site_positions": sorted(set(act_sites)),
        "disulfid_pairs": disulfid_pairs,
        "alphafold_accession": alphafold_accession,
        "function_text": " ".join(function_lines),
    }


def fetch_uniprot_txt(accession: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.txt"
    request = Request(url, headers={"User-Agent": "pmp20-bioinformatics/0.1"})
    with urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def write_fasta(records: list[dict[str, Any]], path: Path) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            header = ">{protein_id}|{accession}|{display_name}".format(
                protein_id=record["protein_id"],
                accession=record.get("accession", ""),
                display_name=record.get("display_name", ""),
            )
            handle.write(header + "\n")
            sequence = record["sequence"]
            for index in range(0, len(sequence), 80):
                handle.write(sequence[index : index + 80] + "\n")


def write_summary_tsv(records: list[dict[str, Any]], path: Path) -> None:
    columns = [
        "protein_id",
        "display_name",
        "role",
        "activity_label",
        "accession",
        "entry_name",
        "gene_name",
        "sequence_length",
        "cysteine_positions",
        "act_site_positions",
        "disulfid_pairs",
        "alphafold_accession",
        "uniprot_txt_path",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        for record in records:
            row = {key: record.get(key, "") for key in columns}
            row["cysteine_positions"] = ",".join(str(x) for x in record["cysteine_positions"])
            row["act_site_positions"] = ",".join(str(x) for x in record["act_site_positions"])
            row["disulfid_pairs"] = ",".join(
                f"{pair[0]}..{pair[1]}" for pair in record["disulfid_pairs"]
            )
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-tsv", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-fasta", required=True, type=Path)
    parser.add_argument("--output-summary-tsv", required=True, type=Path)
    parser.add_argument("--cache-dir", required=True, type=Path)
    args = parser.parse_args()

    args.cache_dir.mkdir(parents=True, exist_ok=True)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_fasta.parent.mkdir(parents=True, exist_ok=True)
    args.output_summary_tsv.parent.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []

    with args.input_tsv.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for raw_row in reader:
            row = {key: (value.strip() if isinstance(value, str) else value) for key, value in raw_row.items()}
            if not row.get("protein_id"):
                continue

            source_type = row.get("source_type", "")
            source_value = row.get("source", "")

            if source_type == "local_uniprot_txt":
                candidate = Path(source_value)
                if not candidate.is_absolute():
                    candidate = (args.input_tsv.parent / candidate).resolve()
                uniprot_path = candidate
                text = uniprot_path.read_text(encoding="utf-8")
            elif source_type == "uniprot_accession":
                accession = source_value
                uniprot_path = args.cache_dir / f"{accession}.txt"
                if uniprot_path.exists():
                    text = uniprot_path.read_text(encoding="utf-8")
                else:
                    try:
                        text = fetch_uniprot_txt(accession)
                    except (HTTPError, URLError) as exc:
                        raise SystemExit(f"Failed to download UniProt accession {accession}: {exc}") from exc
                    uniprot_path.write_text(text, encoding="utf-8")
            else:
                raise SystemExit(f"Unsupported source_type: {source_type!r}")

            parsed = parse_uniprot_txt(text)
            record = {
                "protein_id": row.get("protein_id", ""),
                "display_name": row.get("display_name", ""),
                "source_type": source_type,
                "source": source_value,
                "role": row.get("role", ""),
                "activity_label": row.get("activity_label", ""),
                "notes": row.get("notes", ""),
                **parsed,
                "uniprot_txt_path": str(uniprot_path),
            }
            records.append(record)

    args.output_json.write_text(json.dumps(records, indent=2), encoding="utf-8")
    write_fasta(records, args.output_fasta)
    write_summary_tsv(records, args.output_summary_tsv)

    print(f"Collected {len(records)} protein records")
    print(f"JSON: {args.output_json}")
    print(f"FASTA: {args.output_fasta}")
    print(f"Summary TSV: {args.output_summary_tsv}")


if __name__ == "__main__":
    main()
