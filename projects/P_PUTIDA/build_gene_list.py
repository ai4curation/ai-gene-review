#!/usr/bin/env python3
"""Build a curator-facing PSEPK gene list from UniProt metadata."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_METADATA = Path("projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv")
DEFAULT_OUTPUT = Path("projects/P_PUTIDA/data/psepk_gene_list.tsv")
LOCUS_RE = re.compile(r"\bPP_\d{4,5}\b")


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def primary_gene(gene_names: str) -> str:
    names = gene_names.split()
    return names[0] if names else ""


def ordered_locus(gene_names: str) -> str:
    match = LOCUS_RE.search(gene_names)
    return match.group(0) if match else ""


def base_review_name(row: dict[str, str]) -> str:
    return (
        row.get("primary_gene")
        or row.get("ordered_locus")
        or row.get("uniprot_accession")
        or "unknown"
    )


def locus_sort_key(locus: str) -> tuple[int, int | str]:
    match = LOCUS_RE.fullmatch(locus)
    if match:
        return (0, int(locus.split("_", 1)[1]))
    return (1, locus)


def build_gene_list(metadata_path: Path) -> list[dict[str, str]]:
    with metadata_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = []
        for source in reader:
            gene_names = source.get("Gene Names", "")
            row = {
                "uniprot_accession": source.get("Entry", ""),
                "entry_name": source.get("Entry Name", ""),
                "primary_gene": primary_gene(gene_names),
                "ordered_locus": ordered_locus(gene_names),
                "all_gene_names": gene_names,
                "protein_name": source.get("Protein names", ""),
                "reviewed": source.get("Reviewed", ""),
                "annotation_score": source.get("Annotation", ""),
                "length": source.get("Length", ""),
                "ec_numbers": source.get("EC number", ""),
                "go_ids": source.get("Gene Ontology IDs", ""),
                "interpro_ids": source.get("InterPro", ""),
                "pfam_ids": source.get("Pfam", ""),
                "panther_ids": source.get("PANTHER", ""),
                "kegg_ids": source.get("KEGG", ""),
                "biocyc_ids": source.get("BioCyc", ""),
                "unipathway_ids": source.get("UniPathway", ""),
                "refseq_ids": source.get("RefSeq", ""),
                "keywords": source.get("Keywords", ""),
            }
            row["base_review_name"] = base_review_name(row)
            rows.append(row)

    counts = Counter(row["base_review_name"] for row in rows)
    for row in rows:
        base = row["base_review_name"]
        if counts[base] == 1:
            row["suggested_review_name"] = base
            row["review_name_collision"] = "false"
        else:
            row["suggested_review_name"] = f"{base}__{row['uniprot_accession']}"
            row["review_name_collision"] = "true"

    rows.sort(
        key=lambda row: (
            locus_sort_key(row["ordered_locus"]),
            row["primary_gene"].casefold(),
            row["uniprot_accession"],
        )
    )
    return rows


def write_manifest(output_path: Path, metadata_path: Path, rows: int) -> None:
    manifest_path = output_path.with_suffix(".manifest.txt")
    manifest_path.write_text(
        "\n".join(
            [
                f"generated_utc: {datetime.now(timezone.utc).isoformat()}",
                f"metadata: {metadata_path.as_posix()}",
                f"output: {output_path.as_posix()}",
                f"data_rows: {rows}",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a simplified PSEPK gene list from UniProt metadata."
    )
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = build_gene_list(args.metadata)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "suggested_review_name",
        "review_name_collision",
        "uniprot_accession",
        "entry_name",
        "primary_gene",
        "ordered_locus",
        "all_gene_names",
        "protein_name",
        "reviewed",
        "annotation_score",
        "length",
        "ec_numbers",
        "go_ids",
        "interpro_ids",
        "pfam_ids",
        "panther_ids",
        "kegg_ids",
        "biocyc_ids",
        "unipathway_ids",
        "refseq_ids",
        "keywords",
    ]
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, delimiter="\t", fieldnames=fieldnames, extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(rows)

    write_manifest(args.output, args.metadata, len(rows))
    print(f"Wrote {len(rows)} genes to {args.output}")


if __name__ == "__main__":
    main()
