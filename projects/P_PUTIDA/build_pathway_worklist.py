#!/usr/bin/env python3
"""Build a pathway/module worklist for the PSEPK curation project."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_PROJECT_DIR = Path("projects/P_PUTIDA")
MODULE_MAP = {
    # KEGG ppu00400 is broader than this module; keep this as a seeded submodule.
    "kegg:ppu00400": {
        "module": "tryptophan_biosynthesis",
        "module_file": "modules/tryptophan_biosynthesis.yaml",
        "scope_note": "Seeded submodule; KEGG bucket also includes phenylalanine, tyrosine, and chorismate genes.",
        "priority_phase": "3",
    },
    "kegg:ppu00270": {
        "module": "methionine_biosynthesis",
        "module_file": "modules/methionine_biosynthesis.yaml",
        "scope_note": "Seeded submodule; KEGG bucket includes cysteine and methionine metabolism.",
        "priority_phase": "3",
    },
    "kegg:ppu00020": {
        "module": "tca_cycle",
        "module_file": "",
        "scope_note": "Needs species-neutral central-carbon module or split module.",
        "priority_phase": "1",
    },
    "kegg:ppu00030": {
        "module": "pentose_phosphate_pathway",
        "module_file": "",
        "scope_note": "Needs species-neutral central-carbon module.",
        "priority_phase": "1",
    },
    "kegg:ppu00010": {
        "module": "entner_doudoroff_and_gluconeogenesis",
        "module_file": "",
        "scope_note": "P. putida lacks canonical EMP glycolysis; needs careful split from generic glycolysis/gluconeogenesis.",
        "priority_phase": "1",
    },
    "kegg:ppu00362": {
        "module": "benzoate_degradation",
        "module_file": "",
        "scope_note": "Aromatic-catabolism priority bucket.",
        "priority_phase": "2",
    },
    "kegg:ppu01220": {
        "module": "aromatic_compound_degradation",
        "module_file": "",
        "scope_note": "Broad aromatic-compound bucket; likely split into beta-ketoadipate and route-specific modules.",
        "priority_phase": "2",
    },
    "kegg:ppu00622": {
        "module": "benzoate_upper_pathway",
        "module_file": "",
        "scope_note": "Aromatic-catabolism priority bucket.",
        "priority_phase": "2",
    },
}


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


def count_existing_gene_reviews(rows: list[dict[str, str]]) -> tuple[int, int]:
    existing = 0
    asta = 0
    for row in rows:
        gene = row.get("suggested_review_name", "")
        if not gene:
            continue
        gene_dir = Path("genes") / "PSEPK" / gene
        if (gene_dir / f"{gene}-ai-review.yaml").exists():
            existing += 1
        if list(gene_dir.glob(f"{gene}-deep-research-asta.md")):
            asta += 1
    return existing, asta


def build_worklist(project_dir: Path) -> list[dict[str, str]]:
    buckets = read_tsv(project_dir / "data" / "psepk_pathway_buckets.tsv")
    partition = read_tsv(project_dir / "data" / "psepk_pathway_partition.tsv")
    memberships = read_tsv(project_dir / "data" / "psepk_pathway_membership.tsv")

    primary_rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in partition:
        primary_rows[row.get("primary_bucket_id", "")].append(row)

    membership_counts = Counter(
        f"{row['membership_source'].casefold()}:{row['pathway_id']}"
        for row in memberships
        if row.get("pathway_scope") != "overview"
    )

    worklist: list[dict[str, str]] = []
    for bucket in buckets:
        bucket_id = bucket.get("bucket_id", "")
        mapping = MODULE_MAP.get(bucket_id, {})
        module_file = mapping.get("module_file", "")
        module_name = mapping.get("module", "")
        provider_slug = "falcon"
        module_research_path = ""
        if module_file:
            module_research_path = (
                Path(module_file)
                .with_name(Path(module_file).stem + f"-deep-research-{provider_slug}.md")
                .as_posix()
            )
        pathway_token = bucket_id.split(":", 1)[1] if ":" in bucket_id else bucket_id
        taxon_research_path = (
            project_dir
            / "deep-research"
            / f"PSEPK__{module_name or bucket_id.replace(':', '-')}__{pathway_token}-deep-research-falcon.md"
        )

        rows = primary_rows.get(bucket_id, [])
        review_count, asta_count = count_existing_gene_reviews(rows)
        gene_count = int(bucket.get("gene_count", "0") or 0)
        missing_reviews = max(gene_count - review_count, 0)
        membership_key = bucket_id.replace("kegg:", "kegg:").replace(
            "unipathway:", "unipathway:"
        )
        row = {
            "bucket_id": bucket_id,
            "bucket_label": bucket.get("bucket_label", ""),
            "bucket_type": bucket.get("bucket_type", ""),
            "module_area": bucket.get("module_area", ""),
            "gene_count": str(gene_count),
            "specific_membership_count": str(membership_counts.get(membership_key, gene_count)),
            "reviewed_gene_count": bucket.get("reviewed_count", ""),
            "existing_review_files": str(review_count),
            "missing_review_files": str(missing_reviews),
            "asta_research_files": str(asta_count),
            "module": module_name,
            "module_file": module_file,
            "module_file_exists": "true"
            if module_file and Path(module_file).exists()
            else "false",
            "module_research_falcon": "DONE"
            if module_research_path and Path(module_research_path).exists()
            else "TODO",
            "module_research_path": module_research_path,
            "taxon_research_falcon": "DONE" if taxon_research_path.exists() else "TODO",
            "taxon_research_path": taxon_research_path.as_posix(),
            "priority_phase": mapping.get("priority_phase", ""),
            "batch_status": "SEEDED" if module_name else "UNMAPPED",
            "pr_status": "NOT_STARTED",
            "pr_url": "",
            "scope_note": mapping.get("scope_note", ""),
        }
        if not module_name and bucket.get("bucket_type") == "kegg_pathway":
            row["batch_status"] = "NEEDS_MODULE_MAPPING"
        elif bucket.get("bucket_type") in {"unknown", "orphan"}:
            row["batch_status"] = "ORPHAN_OR_UNKNOWN_QUEUE"
        worklist.append(row)

    def sort_key(row: dict[str, str]) -> tuple[int, int, str]:
        phase = int(row["priority_phase"]) if row["priority_phase"].isdigit() else 99
        mapped = 0 if row["module"] else 1
        return (phase, mapped, row["bucket_id"])

    return sorted(worklist, key=sort_key)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build PSEPK pathway worklist.")
    parser.add_argument("--project-dir", type=Path, default=DEFAULT_PROJECT_DIR)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_PROJECT_DIR / "data" / "psepk_pathway_worklist.tsv",
    )
    args = parser.parse_args()

    rows = build_worklist(args.project_dir)
    fields = [
        "bucket_id",
        "bucket_label",
        "bucket_type",
        "module_area",
        "gene_count",
        "specific_membership_count",
        "reviewed_gene_count",
        "existing_review_files",
        "missing_review_files",
        "asta_research_files",
        "module",
        "module_file",
        "module_file_exists",
        "module_research_falcon",
        "module_research_path",
        "taxon_research_falcon",
        "taxon_research_path",
        "priority_phase",
        "batch_status",
        "pr_status",
        "pr_url",
        "scope_note",
    ]
    write_tsv(args.output, rows, fields)
    args.output.with_suffix(".manifest.txt").write_text(
        "\n".join(
            [
                f"generated_utc: {datetime.now(timezone.utc).isoformat()}",
                f"project_dir: {args.project_dir.as_posix()}",
                f"output: {args.output.as_posix()}",
                f"rows: {len(rows)}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote {len(rows)} pathway buckets to {args.output}")


if __name__ == "__main__":
    main()
