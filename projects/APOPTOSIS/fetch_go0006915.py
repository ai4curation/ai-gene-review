#!/usr/bin/env python3
"""Fetch exact GO:0006915 annotations from QuickGO."""

from __future__ import annotations

import argparse
import csv
import json
import time
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests


QUICKGO_SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
GO_ID = "GO:0006915"
LIMIT = 200
TAXA = {
    "human": 9606,
    "mouse": 10090,
    "zebrafish": 7955,
}

ROW_FIELDS = [
    "row_id",
    "gene_product_id",
    "symbol",
    "name",
    "qualifier",
    "go_id",
    "go_name",
    "go_evidence",
    "evidence_code",
    "reference",
    "with_from",
    "taxon_id",
    "taxon_name",
    "assigned_by",
    "date",
]

ROLLUP_FIELDS = [
    "taxon_id",
    "taxon_label",
    "symbol",
    "row_count",
    "accession_count",
    "accessions",
    "evidence_codes",
    "assigned_by",
    "references",
    "with_from",
    "first_date",
    "last_date",
]


def quickgo_with_from(value: list[dict[str, Any]] | None) -> str:
    """Flatten QuickGO with/from groups into a compact stable string."""

    if not value:
        return ""

    groups = []
    for group in value:
        xrefs = group.get("connectedXrefs") or []
        group_values = [f"{x.get('db')}:{x.get('id')}" for x in xrefs if x.get("db") and x.get("id")]
        if group_values:
            groups.append("|".join(group_values))
    return ";".join(groups)


def fetch_exact_annotations(taxon_id: int) -> list[dict[str, Any]]:
    """Fetch all exact GO:0006915 annotations for one NCBI taxon."""

    all_results: list[dict[str, Any]] = []
    page = 1

    while True:
        params: list[tuple[str, str]] = [
            ("goId", GO_ID),
            ("goUsage", "exact"),
            ("taxonId", str(taxon_id)),
            ("includeFields", "goName"),
            ("includeFields", "taxonName"),
            ("includeFields", "name"),
            ("limit", str(LIMIT)),
        ]

        if page > 1:
            params.append(("page", str(page)))

        response = requests.get(
            QUICKGO_SEARCH,
            params=params,
            headers={"Accept": "application/json"},
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        all_results.extend(results)

        expected = int(data.get("numberOfHits") or 0)
        if len(results) < LIMIT or len(all_results) >= expected:
            return all_results

        page += 1
        time.sleep(0.2)


def normalize_row(row: dict[str, Any]) -> dict[str, str]:
    return {
        "row_id": row.get("id") or "",
        "gene_product_id": row.get("geneProductId") or "",
        "symbol": row.get("symbol") or "",
        "name": row.get("name") or "",
        "qualifier": row.get("qualifier") or "",
        "go_id": row.get("goId") or "",
        "go_name": row.get("goName") or GO_ID,
        "go_evidence": row.get("goEvidence") or "",
        "evidence_code": row.get("evidenceCode") or "",
        "reference": row.get("reference") or "",
        "with_from": quickgo_with_from(row.get("withFrom")),
        "taxon_id": str(row.get("taxonId") or ""),
        "taxon_name": row.get("taxonName") or "",
        "assigned_by": row.get("assignedBy") or "",
        "date": row.get("date") or "",
    }


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def rollup(label: str, rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_symbol: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_symbol[row["symbol"] or row["gene_product_id"]].append(row)

    rolled = []
    for symbol, symbol_rows in by_symbol.items():
        evidence_counts = Counter(row["go_evidence"] for row in symbol_rows)
        assigned_counts = Counter(row["assigned_by"] for row in symbol_rows)
        accessions = sorted({row["gene_product_id"] for row in symbol_rows})
        references = sorted({row["reference"] for row in symbol_rows})
        with_from = sorted({row["with_from"] for row in symbol_rows if row["with_from"]})
        dates = sorted(row["date"] for row in symbol_rows if row["date"])

        rolled.append(
            {
                "taxon_id": symbol_rows[0]["taxon_id"],
                "taxon_label": label,
                "symbol": symbol,
                "row_count": str(len(symbol_rows)),
                "accession_count": str(len(accessions)),
                "accessions": "|".join(accessions),
                "evidence_codes": "|".join(
                    f"{key}:{value}" for key, value in sorted(evidence_counts.items())
                ),
                "assigned_by": "|".join(
                    f"{key}:{value}" for key, value in sorted(assigned_counts.items())
                ),
                "references": "|".join(references),
                "with_from": "|".join(with_from),
                "first_date": dates[0] if dates else "",
                "last_date": dates[-1] if dates else "",
            }
        )

    return sorted(rolled, key=lambda row: (-int(row["row_count"]), row["symbol"]))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f"Fetch exact {GO_ID} annotations from QuickGO."
    )
    parser.add_argument(
        "--taxon",
        action="append",
        choices=sorted(TAXA),
        dest="taxa",
        help="Taxon label to fetch. Repeat to fetch several taxa; default: all.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selected_labels = args.taxa or list(TAXA)

    outdir = Path(__file__).resolve().parent / "go0006915"
    outdir.mkdir(parents=True, exist_ok=True)

    combined_rollup = []
    metadata: dict[str, Any] = {
        "fetched_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "quickgo_search": QUICKGO_SEARCH,
        "go_id": GO_ID,
        "go_usage": "exact",
        "limit": LIMIT,
        "taxa": {},
    }
    for label in selected_labels:
        taxon_id = TAXA[label]
        raw_rows = fetch_exact_annotations(taxon_id)
        rows = [normalize_row(row) for row in raw_rows]
        metadata["taxa"][label] = {
            "taxon_id": taxon_id,
            "rows": len(rows),
        }

        raw_path = outdir / f"{label}-go0006915-raw.json"
        raw_path.write_text(json.dumps(raw_rows, indent=2, sort_keys=True) + "\n")

        write_tsv(outdir / f"{label}-go0006915.tsv", rows, ROW_FIELDS)

        rolled = rollup(label, rows)
        combined_rollup.extend(rolled)
        write_tsv(outdir / f"{label}-go0006915-symbol-rollup.tsv", rolled, ROLLUP_FIELDS)

        print(f"{label}: {len(rows)} exact {GO_ID} rows across {len(rolled)} symbols")

    stem = "-".join(selected_labels)
    if len(selected_labels) > 1:
        write_tsv(outdir / f"{stem}-go0006915-symbol-rollup.tsv", combined_rollup, ROLLUP_FIELDS)
    metadata_name = "metadata.json" if selected_labels == list(TAXA) else f"{stem}-metadata.json"
    (outdir / metadata_name).write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
