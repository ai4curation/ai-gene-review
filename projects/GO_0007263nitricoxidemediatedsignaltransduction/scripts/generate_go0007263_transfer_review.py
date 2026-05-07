#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests
import yaml

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP"
}
QUICKGO_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
TARGET_TERMS = {
    "GO:0007263": "nitric oxide mediated signal transduction",
    "GO:0010749": "regulation of nitric oxide mediated signal transduction",
    "GO:0010750": "positive regulation of nitric oxide mediated signal transduction",
    "GO:0010751": "negative regulation of nitric oxide mediated signal transduction",
}


@dataclass(frozen=True)
class GoaRow:
    source_file: Path
    gene_product_id: str
    symbol: str
    qualifier: str
    go_term: str
    go_name: str
    go_aspect: str
    eco_id: str
    evidence_code: str
    reference: str
    taxon_id: str
    taxon_name: str
    assigned_by: str
    gene_name: str

    @classmethod
    def from_dict(cls, source_file: Path, row: dict[str, str]) -> "GoaRow":
        return cls(
            source_file=source_file,
            gene_product_id=row.get("GENE PRODUCT ID", ""),
            symbol=row.get("SYMBOL", ""),
            qualifier=row.get("QUALIFIER", ""),
            go_term=row.get("GO TERM", ""),
            go_name=row.get("GO NAME", ""),
            go_aspect=row.get("GO ASPECT", ""),
            eco_id=row.get("ECO ID", ""),
            evidence_code=row.get("GO EVIDENCE CODE", ""),
            reference=row.get("REFERENCE", ""),
            taxon_id=row.get("TAXON ID", ""),
            taxon_name=row.get("TAXON NAME", ""),
            assigned_by=row.get("ASSIGNED BY", ""),
            gene_name=row.get("GENE NAME", ""),
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate transfer-review candidates for GO:0007263 annotations"
    )
    parser.add_argument("--genes-root", default="genes")
    parser.add_argument("--organism", default=None)
    parser.add_argument("--gene", default=None, help="Gene symbol filter, e.g. NOS2")
    parser.add_argument(
        "--all-evidence",
        action="store_true",
        default=False,
        help="Include non-experimental evidence (default is experimental only)",
    )
    parser.add_argument(
        "--output",
        default="projects/GO_0007263nitricoxidemediatedsignaltransduction/reviews/GO_0007263-transfer-review.yaml",
    )
    parser.add_argument(
        "--from-quickgo",
        action="store_true",
        default=False,
        help="Fetch GO:0007263 annotations directly from QuickGO API instead of local GOA files.",
    )
    parser.add_argument(
        "--taxon",
        default=None,
        help="Taxon ID filter for --from-quickgo (e.g. 9606, 10090).",
    )
    return parser.parse_args()


def iter_goa_files(genes_root: Path, organism: str | None) -> list[Path]:
    if organism:
        return sorted((genes_root / organism).glob("*/*-goa.tsv"))
    return sorted(genes_root.glob("*/*/*-goa.tsv"))


def read_goa(file_path: Path) -> list[GoaRow]:
    rows: list[GoaRow] = []
    with file_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            rows.append(GoaRow.from_dict(file_path, row))
    return rows


def compact(row: GoaRow) -> dict[str, str]:
    return {
        "gene_product_id": row.gene_product_id,
        "symbol": row.symbol,
        "term_id": row.go_term,
        "term_label": row.go_name,
        "evidence_code": row.evidence_code,
        "reference": row.reference,
        "assigned_by": row.assigned_by,
    }


def fetch_quickgo_rows(taxon: str | None = None) -> list[GoaRow]:
    all_results: list[dict[str, Any]] = []
    for go_id in TARGET_TERMS:
        page = 1
        limit = 200
        collected_for_term = 0
        expected_for_term: int | None = None
        while True:
            params: list[tuple[str, str]] = [
                ("goId", go_id),
                ("includeFields", "goName"),
                ("includeFields", "taxonName"),
                ("includeFields", "name"),
                ("limit", str(limit)),
            ]
            if taxon:
                params.append(("taxonId", taxon))
            if page > 1:
                params.append(("page", str(page)))

            resp = requests.get(QUICKGO_URL, params=params, headers={"Accept": "application/json"}, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            results = data.get("results", [])
            if not results:
                break

            all_results.extend(results)
            collected_for_term += len(results)
            if expected_for_term is None:
                expected_for_term = int(data.get("numberOfHits", 0) or 0)

            if len(results) < limit:
                break
            if expected_for_term and collected_for_term >= expected_for_term:
                break
            page += 1

    rows: list[GoaRow] = []
    source = Path("quickgo-api")
    for r in all_results:
        raw_gene_id = r.get("geneProductId", "")
        _, _, gene_product_id = raw_gene_id.partition(":")
        rows.append(
            GoaRow(
                source_file=source,
                gene_product_id=gene_product_id or raw_gene_id,
                symbol=r.get("symbol", ""),
                qualifier=r.get("qualifier", ""),
                go_term=r.get("goId", ""),
                go_name=r.get("goName", ""),
                go_aspect=r.get("goAspect", ""),
                eco_id=r.get("evidenceCode", ""),
                evidence_code=r.get("goEvidence", ""),
                reference=r.get("reference", ""),
                taxon_id=str(r.get("taxonId", "")),
                taxon_name=r.get("taxonName", ""),
                assigned_by=r.get("assignedBy", ""),
                gene_name=r.get("name", ""),
            )
        )
    return rows


def main() -> None:
    args = parse_args()
    all_rows_by_file: dict[Path, list[GoaRow]] = {}
    focal_rows: list[GoaRow] = []

    if args.from_quickgo:
        rows = fetch_quickgo_rows(args.taxon)
        all_rows_by_file[Path("quickgo-api")] = rows
        for row in rows:
            if row.go_term not in TARGET_TERMS:
                continue
            if args.gene and row.symbol.upper() != args.gene.upper():
                continue
            if not args.all_evidence and row.evidence_code not in EXPERIMENTAL_CODES:
                continue
            focal_rows.append(row)
    else:
        genes_root = Path(args.genes_root)
        goa_files = iter_goa_files(genes_root, args.organism)
        if not goa_files:
            raise SystemExit(f"No GOA files found under {genes_root}")

        for goa_file in goa_files:
            rows = read_goa(goa_file)
            all_rows_by_file[goa_file] = rows
            for row in rows:
                if row.go_term not in TARGET_TERMS:
                    continue
                if args.gene and row.symbol.upper() != args.gene.upper():
                    continue
                if not args.all_evidence and row.evidence_code not in EXPERIMENTAL_CODES:
                    continue
                focal_rows.append(row)

    annotations: list[dict[str, Any]] = []
    for idx, focal in enumerate(focal_rows, start=1):
        related = [
            compact(r)
            for r in all_rows_by_file[focal.source_file]
            if r.gene_product_id == focal.gene_product_id and r != focal
        ]

        annotations.append(
            {
                "annotation_id": f"GO0007263-{idx:05d}",
                "focal_annotation": {
                    "gene_product_id": focal.gene_product_id,
                    "gene_symbol": focal.symbol,
                    "gene_name": focal.gene_name,
                    "taxon_id": focal.taxon_id,
                    "taxon_name": focal.taxon_name,
                    "term": {"id": focal.go_term, "label": focal.go_name, "aspect": focal.go_aspect},
                    "qualifier": focal.qualifier,
                    "evidence_code": focal.evidence_code,
                    "eco_id": focal.eco_id,
                    "reference": focal.reference,
                    "assigned_by": focal.assigned_by,
                    "source_goa_file": str(focal.source_file),
                },
                "context": {
                    "related_annotations_same_gene_any_reference": related,
                },
                "review": {
                    "action": "PENDING",
                    "rationale": "",
                    "proposed_replacement_term": None,
                    "alternative_candidate_terms": [],
                    "ntr_note": "",
                },
            }
        )

    payload = {
        "term_obsoletion_review": {
            "focus_terms": [
                {"id": term_id, "label": label}
                for term_id, label in TARGET_TERMS.items()
            ],
            "generated_at": datetime.now(UTC).isoformat(),
            "organism_filter": args.organism,
            "taxon_filter": args.taxon,
            "gene_filter": args.gene,
            "source": "quickgo" if args.from_quickgo else "local-goa",
            "evidence_filter": {
                "experimental_only": (not args.all_evidence),
                "evidence_codes": sorted(EXPERIMENTAL_CODES),
            },
            "total_focal_annotations": len(annotations),
            "annotations": annotations,
        }
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(payload, handle, sort_keys=False, allow_unicode=True, width=120)

    if annotations:
        print(f"Wrote {len(annotations)} annotations to {output}")
    else:
        print(f"No matching GO:0007263 annotations found; wrote empty scaffold to {output}")


if __name__ == "__main__":
    main()
