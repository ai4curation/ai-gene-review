#!/usr/bin/env python3
"""Extract a per-pathway gene curation batch from the PSEPK partition."""

from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml


DEFAULT_PROJECT_DIR = Path("projects/P_PUTIDA")
_PSEPK_REVIEW_INDEX: tuple[dict[str, Path], dict[str, Path]] | None = None


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, delimiter="\t", fieldnames=fieldnames, extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(rows)


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", text.strip())
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned.lower() or "pathway"


def locus_key(row: dict[str, str]) -> tuple[int, str]:
    locus = row.get("ordered_locus", "")
    match = re.fullmatch(r"PP_(\d+)", locus)
    if match:
        return (int(match.group(1)), row.get("suggested_review_name", ""))
    return (999999, row.get("suggested_review_name", ""))


def psepk_review_index() -> tuple[dict[str, Path], dict[str, Path]]:
    global _PSEPK_REVIEW_INDEX
    if _PSEPK_REVIEW_INDEX is not None:
        return _PSEPK_REVIEW_INDEX

    by_accession: dict[str, Path] = {}
    by_symbol: dict[str, Path] = {}
    for review in Path("genes/PSEPK").glob("*/*-ai-review.yaml"):
        try:
            data = yaml.safe_load(review.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        accession = data.get("id", "")
        symbol = data.get("gene_symbol", "")
        if accession:
            by_accession.setdefault(str(accession), review)
        if symbol:
            by_symbol.setdefault(str(symbol), review)

    _PSEPK_REVIEW_INDEX = (by_accession, by_symbol)
    return _PSEPK_REVIEW_INDEX


def locate_review(row: dict[str, str]) -> Path:
    gene = row.get("suggested_review_name", "")
    direct = Path("genes") / "PSEPK" / gene / f"{gene}-ai-review.yaml"
    by_accession, by_symbol = psepk_review_index()
    accession = row.get("uniprot_accession", "")
    return by_accession.get(accession) or by_symbol.get(gene) or direct


def review_status(row: dict[str, str]) -> dict[str, str]:
    gene = row.get("suggested_review_name", "")
    review = locate_review(row)
    gene_dir = review.parent
    review_stem = review.name.removesuffix("-ai-review.yaml")
    asta_candidates = [gene_dir / f"{gene}-deep-research-asta.md"]
    if review_stem != gene:
        asta_candidates.append(gene_dir / f"{review_stem}-deep-research-asta.md")
    asta = next(
        (candidate for candidate in asta_candidates if candidate.exists()),
        asta_candidates[0],
    )
    curation = "MISSING"
    if review.exists():
        curation = "CURATED"
        try:
            data = yaml.safe_load(review.read_text(encoding="utf-8")) or {}
            annotations = data.get("existing_annotations") or []
            if not annotations:
                description = str(data.get("description") or "")
                curation = (
                    "CURATED"
                    if description and not description.startswith("TODO:")
                    else "NO_ANNOTATIONS"
                )
            for annotation in annotations:
                action = (annotation.get("review") or {}).get("action", "")
                if not action or action == "PENDING":
                    curation = "PENDING"
                    break
        except Exception:
            curation = "CHECK"
    return {
        "gene_dir": gene_dir.as_posix(),
        "review_file": review.as_posix() if review.exists() else "",
        "review_status": "PRESENT" if review.exists() else "MISSING",
        "curation_status": curation,
        "asta_research_file": asta.as_posix() if asta.exists() else "",
        "asta_research_status": "PRESENT" if asta.exists() else "MISSING",
    }


def pathway_members(
    project_dir: Path, pathway: str
) -> tuple[str, str, list[dict[str, str]]]:
    pathway_id = pathway.replace("kegg:", "").replace("unipathway:", "")
    primary_bucket_ids = {f"kegg:{pathway_id}", f"unipathway:{pathway_id}", pathway_id}
    partition = read_tsv(project_dir / "data" / "psepk_pathway_partition.tsv")
    membership = read_tsv(project_dir / "data" / "psepk_pathway_membership.tsv")
    by_key: dict[tuple[str, str], dict[str, str]] = {}
    for row in partition:
        for key_name in ("ordered_locus", "uniprot_accession", "suggested_review_name"):
            value = row.get(key_name, "")
            if value:
                by_key[(key_name, value)] = row

    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    pathway_name = pathway_id
    for member in membership:
        if member.get("pathway_id") != pathway_id:
            continue
        pathway_name = member.get("pathway_name") or pathway_name
        source = member.get("membership_source", "")
        row = (
            by_key.get(("ordered_locus", member.get("ordered_locus", "")))
            or by_key.get(("uniprot_accession", member.get("uniprot_accession", "")))
            or by_key.get(("suggested_review_name", member.get("suggested_review_name", "")))
        )
        if not row:
            continue
        key = row.get("uniprot_accession") or row.get("ordered_locus") or row.get("suggested_review_name", "")
        if key in seen:
            continue
        seen.add(key)
        rows.append(
            {
                **row,
                "membership_source": source,
                "membership_pathway_id": pathway_id,
                "membership_pathway_name": pathway_name,
                "is_primary_for_pathway": "true"
                if row.get("primary_bucket_id") in primary_bucket_ids
                else "false",
                **review_status(row),
            }
        )
    return pathway_id, pathway_name, sorted(rows, key=locus_key)


def add_extra_genes(
    project_dir: Path,
    *,
    rows: list[dict[str, str]],
    extra_genes: list[str],
    pathway_id: str,
    pathway_name: str,
) -> list[dict[str, str]]:
    if not extra_genes:
        return rows

    partition = read_tsv(project_dir / "data" / "psepk_pathway_partition.tsv")
    by_key: dict[str, dict[str, str]] = {}
    for row in partition:
        for key_name in ("suggested_review_name", "ordered_locus", "uniprot_accession"):
            value = row.get(key_name, "")
            if value:
                by_key[value] = row

    seen = {
        row.get("uniprot_accession")
        or row.get("ordered_locus")
        or row.get("suggested_review_name", "")
        for row in rows
    }
    combined = list(rows)
    for spec in extra_genes:
        gene, source = (spec.split("=", 1) + ["MANUAL"])[:2] if "=" in spec else (spec, "MANUAL")
        row = by_key.get(gene)
        if not row:
            raise SystemExit(f"Extra gene not found in partition: {gene}")
        key = row.get("uniprot_accession") or row.get("ordered_locus") or row.get("suggested_review_name", "")
        if key in seen:
            continue
        seen.add(key)
        combined.append(
            {
                **row,
                "membership_source": source,
                "membership_pathway_id": pathway_id,
                "membership_pathway_name": pathway_name,
                "is_primary_for_pathway": "false",
                **review_status(row),
            }
        )
    return sorted(combined, key=locus_key)


def write_markdown(
    path: Path,
    *,
    pathway_id: str,
    pathway_name: str,
    module: str,
    rows: list[dict[str, str]],
    validated: bool,
) -> None:
    review_present = sum(row["review_status"] == "PRESENT" for row in rows)
    curated_present = sum(row["curation_status"] == "CURATED" for row in rows)
    asta_present = sum(row["asta_research_status"] == "PRESENT" for row in rows)
    primary_count = sum(row["is_primary_for_pathway"] == "true" for row in rows)
    lines = [
        "---",
        f'title: "PSEPK {pathway_id} {pathway_name} batch"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        f"# PSEPK {pathway_id}: {pathway_name}",
        "",
        f"- Module seed: `{module or 'UNASSIGNED'}`",
        f"- Candidate genes from membership table: {len(rows)}",
        f"- Primary bucket genes: {primary_count}",
        f"- Existing review files: {review_present}",
        f"- Curated review files: {curated_present}",
        f"- Existing Asta research files: {asta_present}",
        "",
        "## Required Workflow",
        "",
        "- [ ] Curate or update the species-neutral module.",
        "- [ ] Run module-level Falcon deep research.",
        "- [ ] Run module + pathway + PSEPK Falcon deep research.",
        f"- [{'x' if review_present == len(rows) else ' '}] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.",
        f"- [{'x' if asta_present == len(rows) else ' '}] Run Asta deep research for selected genes.",
        f"- [{'x' if curated_present == len(rows) else ' '}] Curate each selected gene review.",
        f"- [{'x' if validated else ' '}] Validate module and gene reviews.",
        "- [ ] Open one PR for this module/pathway.",
        "- [ ] Shepherd PR through review, CI, and merge readiness.",
        "",
        "## Candidate Genes",
        "",
        "| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        done = (
            row["review_status"] == "PRESENT"
            and row["curation_status"] == "CURATED"
            and row["asta_research_status"] == "PRESENT"
        )
        lines.append(
            f"| [{'x' if done else ' '}] | "
            f"`{row['suggested_review_name']}` | "
            f"{row['ordered_locus']} | "
            f"{row['uniprot_accession']} | "
            f"{row['primary_bucket_id']} | "
            f"{row['review_status']} | "
            f"{row['curation_status']} | "
            f"{row['asta_research_status']} | "
            f"{row['protein_name'].replace('|', '/')[:120]} |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            f"Generated UTC: {datetime.now(timezone.utc).isoformat()}",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract a PSEPK pathway batch.")
    parser.add_argument("pathway", help="KEGG or UniPathway ID such as ppu00400 or UPA00392")
    parser.add_argument("--module", default="", help="Species-neutral module seed")
    parser.add_argument(
        "--extra-gene",
        action="append",
        default=[],
        help="Additional partition gene to include, optionally as GENE=SOURCE.",
    )
    parser.add_argument("--project-dir", type=Path, default=DEFAULT_PROJECT_DIR)
    parser.add_argument("--output-prefix", type=Path)
    parser.add_argument(
        "--validated",
        action="store_true",
        help="Mark validation complete in the generated markdown checklist.",
    )
    parser.add_argument(
        "--primary-only",
        action="store_true",
        help="Include only genes whose primary partition bucket is this pathway.",
    )
    args = parser.parse_args()

    pathway_id, pathway_name, rows = pathway_members(args.project_dir, args.pathway)
    if args.primary_only:
        rows = [row for row in rows if row.get("is_primary_for_pathway") == "true"]
    rows = add_extra_genes(
        args.project_dir,
        rows=rows,
        extra_genes=args.extra_gene,
        pathway_id=pathway_id,
        pathway_name=pathway_name,
    )
    prefix = args.output_prefix or (
        args.project_dir
        / "batches"
        / f"{pathway_id}_{slugify(args.module or pathway_name)}"
    )
    tsv_path = prefix.with_suffix(".tsv")
    md_path = prefix.with_suffix(".md")
    fields = [
        "suggested_review_name",
        "ordered_locus",
        "uniprot_accession",
        "entry_name",
        "primary_gene",
        "all_gene_names",
        "protein_name",
        "reviewed",
        "annotation_score",
        "ec_numbers",
        "go_ids",
        "primary_bucket_id",
        "primary_bucket_label",
        "is_primary_for_pathway",
        "membership_source",
        "membership_pathway_id",
        "membership_pathway_name",
        "gene_dir",
        "review_status",
        "review_file",
        "curation_status",
        "asta_research_status",
        "asta_research_file",
    ]
    write_tsv(tsv_path, rows, fields)
    write_markdown(
        md_path,
        pathway_id=pathway_id,
        pathway_name=pathway_name,
        module=args.module,
        rows=rows,
        validated=args.validated,
    )
    print(f"Wrote {len(rows)} genes to {tsv_path}")
    print(f"Wrote checklist to {md_path}")


if __name__ == "__main__":
    main()
