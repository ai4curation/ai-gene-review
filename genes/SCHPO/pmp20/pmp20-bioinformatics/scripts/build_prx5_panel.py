#!/usr/bin/env python3
"""Build a UniProt accession panel for reviewed eukaryotic Prx5-like proteins."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from urllib.parse import quote_plus
from urllib.request import Request, urlopen


DEFAULT_QUERY = "reviewed:true AND xref:interpro-IPR037944 AND taxonomy_id:2759"


def fetch_search_tsv(query: str, size: int) -> str:
    encoded_query = quote_plus(query)
    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query={encoded_query}"
        "&fields=accession,id,gene_primary,organism_name,length"
        f"&format=tsv&size={size}"
    )
    request = Request(url, headers={"User-Agent": "pmp20-bioinformatics/0.1"})
    with urlopen(request, timeout=120) as response:
        return response.read().decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-tsv", required=True, type=Path)
    parser.add_argument("--query", default=DEFAULT_QUERY)
    parser.add_argument("--target-accession", default="O14313")
    parser.add_argument("--max-results", type=int, default=120)
    parser.add_argument("--min-length", type=int, default=130)
    parser.add_argument("--max-length", type=int, default=260)
    args = parser.parse_args()

    payload = fetch_search_tsv(args.query, args.max_results)
    reader = csv.DictReader(payload.splitlines(), delimiter="\t")

    rows = []
    seen_accessions: set[str] = set()

    for record in reader:
        accession = (record.get("Entry") or "").strip()
        entry_name = (record.get("Entry Name") or "").strip()
        gene_name = (record.get("Gene Names (primary)") or "").strip()
        organism = (record.get("Organism") or "").strip()

        if not accession or accession in seen_accessions:
            continue

        try:
            length = int((record.get("Length") or "0").strip())
        except ValueError:
            continue

        if length < args.min_length or length > args.max_length:
            continue

        protein_id = f"{gene_name.lower()}_{accession.lower()}" if gene_name else accession.lower()
        role = "target" if accession == args.target_accession else "homolog"
        activity_label = "unknown" if role == "target" else "family_member"
        notes = f"{entry_name} | {organism}"

        rows.append(
            {
                "protein_id": protein_id,
                "display_name": entry_name,
                "source_type": "uniprot_accession",
                "source": accession,
                "role": role,
                "activity_label": activity_label,
                "notes": notes,
            }
        )
        seen_accessions.add(accession)

    if args.target_accession not in {row["source"] for row in rows}:
        rows.insert(
            0,
            {
                "protein_id": f"target_{args.target_accession.lower()}",
                "display_name": f"TARGET_{args.target_accession}",
                "source_type": "uniprot_accession",
                "source": args.target_accession,
                "role": "target",
                "activity_label": "unknown",
                "notes": "Inserted target accession not returned by query",
            },
        )

    rows.sort(key=lambda row: (row["role"] != "target", row["source"]))

    args.output_tsv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_tsv.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "protein_id",
            "display_name",
            "source_type",
            "source",
            "role",
            "activity_label",
            "notes",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Wrote panel with {len(rows)} proteins: {args.output_tsv}")


if __name__ == "__main__":
    main()
