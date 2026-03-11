#!/usr/bin/env python3
"""Generate a publication-centric annotation review stub from GOA TSV files.

This script scans local GOA files in the repository, extracts all annotations
that cite a target reference (typically a PMID), and writes a publication-based
review YAML where each focal annotation includes related annotation context.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

import requests

QUICKGO_ANNOTATION_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


# ---------------------------------------------------------------------------
# QuickGO API fetch by reference
# ---------------------------------------------------------------------------

def fetch_from_quickgo(reference_id: str, taxon_id: str | None = None) -> list[GoaRow]:
    """Query QuickGO for all annotations citing *reference_id*.

    Optionally filter by *taxon_id* (e.g. '9606' for human).
    Returns a flat list of GoaRow objects compatible with the rest of the pipeline.
    """
    all_results = []
    page = 1
    limit = 200

    while True:
        params: list[tuple[str, str]] = [
            ("reference", reference_id),
            ("includeFields", "goName"),
            ("includeFields", "taxonName"),
            ("includeFields", "name"),
            ("limit", str(limit)),
        ]
        if taxon_id:
            params.append(("taxonId", taxon_id))
        if page > 1:
            params.append(("page", str(page)))

        resp = requests.get(
            QUICKGO_ANNOTATION_URL,
            params=params,
            headers={"Accept": "application/json"},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
        if not results:
            break
        all_results.extend(results)
        page_info = data.get("pageInfo", {})
        total = page_info.get("total", 0)
        if len(all_results) >= total or len(results) < limit:
            break
        page += 1

    sentinel = Path("quickgo-api")
    rows: list[GoaRow] = []
    for r in all_results:
        raw_id = r.get("geneProductId", "")
        db, _, gene_product_id = raw_id.partition(":")
        rows.append(
            GoaRow(
                source_file=sentinel,
                gene_product_db=db,
                gene_product_id=gene_product_id or raw_id,
                symbol=r.get("symbol", ""),
                qualifier=r.get("qualifier", ""),
                go_term=r.get("goId", ""),
                go_name=r.get("goName", ""),
                go_aspect=r.get("goAspect", ""),
                eco_id=r.get("evidenceCode", ""),
                evidence_code=r.get("goEvidence", ""),
                reference=r.get("reference", ""),
                with_from=r.get("withFrom") or "",
                taxon_id=str(r.get("taxonId", "")),
                taxon_name=r.get("taxonName", ""),
                assigned_by=r.get("assignedBy", ""),
                gene_name=r.get("name", ""),
                date=r.get("date", ""),
            )
        )
    return rows


# ---------------------------------------------------------------------------
# Supporting-text lookup from existing gene review YAMLs
# ---------------------------------------------------------------------------

def _load_supporting_text_index(
    goa_file: Path,
    reference_id: str,
) -> dict[str, list[str]]:
    """Return {go_term_id: [supporting_text, ...]} for annotations in the
    gene review YAML that cite *reference_id* in their supported_by list.

    The review YAML is derived from the GOA file path, e.g.:
      genes/human/PTPN22/PTPN22-goa.tsv  →
      genes/human/PTPN22/PTPN22-ai-review.yaml
    """
    review_path = goa_file.parent / goa_file.name.replace("-goa.tsv", "-ai-review.yaml")
    if not review_path.exists():
        return {}

    with review_path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}

    index: dict[str, list[str]] = {}
    for ann in data.get("existing_annotations", []):
        term = ann.get("term", {})
        term_id = term.get("id", "") if isinstance(term, dict) else ""
        if not term_id:
            continue
        for sb in ann.get("review", {}).get("supported_by", []) or []:
            if sb.get("reference_id", "") == reference_id:
                text = sb.get("supporting_text", "").strip()
                if text:
                    index.setdefault(term_id, []).append(text)
    return index


@dataclass(frozen=True)
class GoaRow:
    source_file: Path
    gene_product_db: str
    gene_product_id: str
    symbol: str
    qualifier: str
    go_term: str
    go_name: str
    go_aspect: str
    eco_id: str
    evidence_code: str
    reference: str
    with_from: str
    taxon_id: str
    taxon_name: str
    assigned_by: str
    gene_name: str
    date: str

    @classmethod
    def from_dict(cls, source_file: Path, row: dict[str, str]) -> "GoaRow":
        return cls(
            source_file=source_file,
            gene_product_db=row.get("GENE PRODUCT DB", ""),
            gene_product_id=row.get("GENE PRODUCT ID", ""),
            symbol=row.get("SYMBOL", ""),
            qualifier=row.get("QUALIFIER", ""),
            go_term=row.get("GO TERM", ""),
            go_name=row.get("GO NAME", ""),
            go_aspect=row.get("GO ASPECT", ""),
            eco_id=row.get("ECO ID", ""),
            evidence_code=row.get("GO EVIDENCE CODE", ""),
            reference=row.get("REFERENCE", ""),
            with_from=row.get("WITH/FROM", ""),
            taxon_id=row.get("TAXON ID", ""),
            taxon_name=row.get("TAXON NAME", ""),
            assigned_by=row.get("ASSIGNED BY", ""),
            gene_name=row.get("GENE NAME", ""),
            date=row.get("DATE", ""),
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build a publication-centric annotation review YAML from local GOA files."
        )
    )
    parser.add_argument(
        "reference_id",
        help="Target reference identifier, e.g. PMID:23991106",
    )
    parser.add_argument(
        "--genes-root",
        default="genes",
        help="Path to genes directory (default: genes)",
    )
    parser.add_argument(
        "--organism",
        default=None,
        help="Optional organism folder filter (e.g. human, worm, ARATH)",
    )
    parser.add_argument(
        "--gene",
        default=None,
        help="Optional gene symbol filter (e.g. PTPN22). Can be combined with --organism.",
    )
    parser.add_argument(
        "--max-annotations",
        type=int,
        default=0,
        help="Optional cap on focal annotations (0 means no cap)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Output YAML path. Default: "
            "projects/publication_annotation_review/reviews/<REFERENCE>-annotation-review.yaml"
        ),
    )
    parser.add_argument(
        "--from-quickgo",
        action="store_true",
        default=False,
        help="Fetch annotations from QuickGO API instead of local GOA files.",
    )
    parser.add_argument(
        "--taxon",
        default=None,
        help="Taxon ID filter when using --from-quickgo (e.g. 9606 for human).",
    )
    return parser.parse_args()


def iter_goa_files(genes_root: Path, organism: str | None) -> list[Path]:
    if organism:
        return sorted((genes_root / organism).glob("*/*-goa.tsv"))
    return sorted(genes_root.glob("*/*/*-goa.tsv"))


def read_goa_rows(file_path: Path) -> list[GoaRow]:
    rows: list[GoaRow] = []
    with file_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            rows.append(GoaRow.from_dict(file_path, row))
    return rows


def compact_related(row: GoaRow) -> dict[str, str]:
    return {
        "gene_product_id": row.gene_product_id,
        "symbol": row.symbol,
        "qualifier": row.qualifier,
        "term_id": row.go_term,
        "term_label": row.go_name,
        "evidence_code": row.evidence_code,
        "eco_id": row.eco_id,
        "reference": row.reference,
        "assigned_by": row.assigned_by,
    }


def annotation_record(
    focal: GoaRow,
    all_rows_for_gene: list[GoaRow],
    all_focal_rows_for_publication: list[GoaRow],
    index: int,
    supporting_text_index: dict[str, list[str]] | None = None,
) -> dict[str, Any]:
    same_publication_same_gene = [
        compact_related(r)
        for r in all_rows_for_gene
        if r.reference == focal.reference and r != focal
    ]

    same_gene_same_term_any_reference = [
        compact_related(r) for r in all_rows_for_gene if r.go_term == focal.go_term and r != focal
    ]

    same_publication_same_term_other_genes = [
        compact_related(r)
        for r in all_focal_rows_for_publication
        if r.go_term == focal.go_term and r.gene_product_id != focal.gene_product_id
    ]

    source_publication = ""
    if focal.reference.startswith("PMID:"):
        pmid = focal.reference.split(":", 1)[1]
        source_publication = f"publications/PMID_{pmid}.md"

    return {
        "annotation_id": f"ANN-{index:05d}",
        "focal_annotation": {
            "gene_product_id": focal.gene_product_id,
            "gene_symbol": focal.symbol,
            "gene_name": focal.gene_name,
            "taxon_id": focal.taxon_id,
            "taxon_name": focal.taxon_name,
            "term": {
                "id": focal.go_term,
                "label": focal.go_name,
                "aspect": focal.go_aspect,
            },
            "qualifier": focal.qualifier,
            "evidence_code": focal.evidence_code,
            "eco_id": focal.eco_id,
            "reference": focal.reference,
            "with_from": focal.with_from,
            "assigned_by": focal.assigned_by,
            "date": focal.date,
            "source_goa_file": str(focal.source_file),
        },
        "context": {
            "related_annotations_same_publication_same_gene": same_publication_same_gene,
            "related_annotations_same_gene_same_term_any_reference": same_gene_same_term_any_reference,
            "related_annotations_same_publication_same_term_other_genes": same_publication_same_term_other_genes,
        },
        "review": {
            "term_correctness": {
                "decision": "PENDING",
                "rationale": "",
                "proposed_replacement_term": None,
            },
            "supporting_text_quality": {
                "decision": "PENDING",
                "rationale": "",
                "supporting_text": (
                    (supporting_text_index or {}).get(focal.go_term, [None])[0] or ""
                ),
                "all_supporting_texts": (supporting_text_index or {}).get(focal.go_term, []),
                "source_publication_file": source_publication,
            },
            "notes": "",
        },
    }


def main() -> None:
    args = parse_args()

    if args.from_quickgo:
        all_focal_rows = fetch_from_quickgo(args.reference_id, taxon_id=args.taxon)
        if args.gene:
            all_focal_rows = [r for r in all_focal_rows if r.symbol.upper() == args.gene.upper()]
        # Build per-file row lookup (sentinel file, no related local data)
        all_rows_by_file: dict[Path, list[GoaRow]] = {Path("quickgo-api"): all_focal_rows}
    else:
        genes_root = Path(args.genes_root)
        goa_files = iter_goa_files(genes_root, args.organism)
        if not goa_files:
            raise SystemExit(f"No GOA files found under {genes_root}")

        focal_by_file: dict[Path, list[GoaRow]] = {}
        all_rows_by_file = {}
        all_focal_rows = []

        for goa_file in goa_files:
            rows = read_goa_rows(goa_file)
            all_rows_by_file[goa_file] = rows
            focal_rows = [row for row in rows if row.reference == args.reference_id]
            if args.gene:
                focal_rows = [row for row in focal_rows if row.symbol.upper() == args.gene.upper()]
            if focal_rows:
                focal_by_file[goa_file] = focal_rows
                all_focal_rows.extend(focal_rows)

    if not all_focal_rows:
        raise SystemExit(
            f"No annotations found with reference {args.reference_id} in {genes_root}"
        )

    if args.max_annotations and args.max_annotations > 0:
        all_focal_rows = all_focal_rows[: args.max_annotations]

    output_path = (
        Path(args.output)
        if args.output
        else Path("projects/publication_annotation_review/reviews")
        / f"{args.reference_id.replace(':', '_')}-annotation-review.yaml"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    annotations: list[dict[str, Any]] = []
    for idx, focal in enumerate(all_focal_rows, start=1):
        st_index = _load_supporting_text_index(focal.source_file, args.reference_id)
        annotations.append(
            annotation_record(
                focal=focal,
                all_rows_for_gene=all_rows_by_file[focal.source_file],
                all_focal_rows_for_publication=all_focal_rows,
                index=idx,
                supporting_text_index=st_index,
            )
        )

    payload: dict[str, Any] = {
        "publication_review": {
            "reference_id": args.reference_id,
            "generated_at": datetime.now(UTC).isoformat(),
            "organism_filter": args.organism,
            "gene_filter": args.gene,
            "review_focus": {
                "term_correctness": True,
                "supporting_text_quality": True,
            },
            "total_focal_annotations": len(annotations),
            "annotations": annotations,
        }
    }

    with output_path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(payload, handle, sort_keys=False, allow_unicode=True, width=120)

    print(f"Wrote {len(annotations)} focal annotations to {output_path}")


if __name__ == "__main__":
    main()
