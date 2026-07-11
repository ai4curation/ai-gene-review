#!/usr/bin/env python3
"""Deep-research wrapper for a module/pathway in a target taxon.

This complements module_deep_research_wrapper.py. Generic module research should
stay organism-neutral; this wrapper adds an explicit species/taxon constraint and
can include local candidate genes from a project partition table.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from module_deep_research_wrapper import (
    command_for_log,
    deep_research_client_command,
    format_connections,
    format_outline,
    load_module_yaml,
    resolve_module_path,
    slugify,
)


PROVIDERS = (
    "openai",
    "perplexity",
    "perplexity-lite",
    "falcon",
    "cyberian",
    "codex",
    "openscientist",
)
DEFAULT_TEMPLATE = Path("templates/module_pathway_taxon_research.md.j2")
DEFAULT_MAX_GENES = 80
UNRESOLVED_PLACEHOLDER_PATTERNS = (
    "{module_title}",
    "{pathway_query}",
    "{species_name}",
    "{candidate_genes}",
    "{{ module_title }}",
    "{{ pathway_query }}",
    "{{ species_name }}",
    "{{ candidate_genes }}",
)

ORGANISM_DEFAULTS = {
    "PSEPK": {
        "species_name": "Pseudomonas putida KT2440",
        "taxon_id": "160488",
        "proteome_id": "UP000000556",
        "project": "P_PUTIDA",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.casefold())


def project_dir_for(args: argparse.Namespace) -> Path | None:
    if args.project_dir:
        return args.project_dir
    if args.project:
        return Path("projects") / args.project
    default = ORGANISM_DEFAULTS.get(args.organism.upper(), {}).get("project")
    if default:
        return Path("projects") / default
    return None


def organism_defaults(organism: str) -> dict[str, str]:
    defaults = ORGANISM_DEFAULTS.get(organism.upper(), {}).copy()
    defaults.setdefault("species_name", organism)
    defaults.setdefault("taxon_id", "unspecified")
    defaults.setdefault("proteome_id", "unspecified")
    return defaults


def module_context(module_ref: str, modules_dir: Path) -> dict[str, str]:
    try:
        module_path = resolve_module_path(module_ref, modules_dir)
        data = load_module_yaml(module_path)
    except (FileNotFoundError, ValueError):
        return {
            "module_title": module_ref,
            "module_summary": "No module YAML was resolved; use the pathway and taxon context.",
            "module_outline": "No module YAML outline available.",
            "module_connections": "No module YAML connections available.",
            "module_slug": slugify(module_ref),
            "module_source": "free-text module query",
        }

    module = data.get("module") if isinstance(data.get("module"), dict) else {}
    title = str(data.get("title") or module.get("label") or module_path.stem)
    return {
        "module_title": title,
        "module_summary": str(data.get("description") or module.get("description") or ""),
        "module_outline": format_outline(data),
        "module_connections": format_connections(data),
        "module_slug": module_path.stem,
        "module_source": module_path.as_posix(),
    }


def kegg_names(project_dir: Path | None) -> dict[str, str]:
    if not project_dir:
        return {}
    names: dict[str, str] = {}
    path = project_dir / "data" / "psepk_kegg_pathway_names.tsv"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or "\t" not in line:
                continue
            pathway_id, name = line.split("\t", 1)
            names[pathway_id] = name
    return names


def resolve_bucket(
    pathway_query: str,
    project_dir: Path | None,
) -> dict[str, str]:
    query_norm = normalize(pathway_query)
    pathway_id = pathway_query
    if re.fullmatch(r"ppu\d{5}", pathway_query):
        pathway_id = pathway_query
    elif re.fullmatch(r"kegg:ppu\d{5}", pathway_query):
        pathway_id = pathway_query.split(":", 1)[1]

    if project_dir:
        bucket_rows = read_tsv(project_dir / "data" / "psepk_pathway_buckets.tsv")
    else:
        bucket_rows = []

    exact_matches = []
    substring_matches = []
    for row in bucket_rows:
        bucket_id = row.get("bucket_id", "")
        label = row.get("bucket_label", "")
        candidates = {
            bucket_id,
            bucket_id.replace("kegg:", ""),
            bucket_id.replace("unipathway:", ""),
            label,
        }
        if query_norm in {normalize(candidate) for candidate in candidates if candidate}:
            exact_matches.append(row)
        elif query_norm and query_norm in normalize(label):
            substring_matches.append(row)

    match = exact_matches[0] if len(exact_matches) == 1 else None
    if match is None and not exact_matches and len(substring_matches) == 1:
        match = substring_matches[0]

    names = kegg_names(project_dir)
    if match:
        bucket_id = match.get("bucket_id", "")
        resolved_pathway_id = bucket_id.split(":", 1)[1] if ":" in bucket_id else bucket_id
        return {
            "bucket_id": bucket_id,
            "pathway_id": resolved_pathway_id,
            "pathway_name": match.get("bucket_label", "") or names.get(resolved_pathway_id, ""),
            "pathway_source": match.get("bucket_source", "") or match.get("bucket_type", ""),
            "pathway_context": (
                f"Resolved local bucket {bucket_id} with {match.get('gene_count', 'unknown')} "
                f"primary genes; module area: {match.get('module_area', 'unspecified')}."
            ),
        }

    if re.fullmatch(r"ppu\d{5}", pathway_id):
        return {
            "bucket_id": f"kegg:{pathway_id}",
            "pathway_id": pathway_id,
            "pathway_name": names.get(pathway_id, "unresolved KEGG pathway name"),
            "pathway_source": "KEGG",
            "pathway_context": "Resolved as a KEGG organism-specific pathway ID.",
        }

    return {
        "bucket_id": "",
        "pathway_id": pathway_query,
        "pathway_name": pathway_query,
        "pathway_source": "free-text pathway query",
        "pathway_context": "No local pathway bucket was resolved for this query.",
    }


def index_partition_rows(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    index: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        for key in (
            ("ordered_locus", row.get("ordered_locus", "")),
            ("uniprot_accession", row.get("uniprot_accession", "")),
            ("suggested_review_name", row.get("suggested_review_name", "")),
        ):
            if key[1]:
                index[key] = row
    return index


def candidate_rows(
    bucket: dict[str, str],
    project_dir: Path | None,
) -> list[dict[str, str]]:
    if not project_dir:
        return []
    partition_rows = read_tsv(project_dir / "data" / "psepk_pathway_partition.tsv")
    if not partition_rows:
        return []

    bucket_id = bucket.get("bucket_id", "")
    pathway_id = bucket.get("pathway_id", "")
    if bucket_id and not bucket_id.startswith("kegg:"):
        return [row for row in partition_rows if row.get("primary_bucket_id") == bucket_id]

    membership_rows = read_tsv(project_dir / "data" / "psepk_pathway_membership.tsv")
    if pathway_id and membership_rows:
        index = index_partition_rows(partition_rows)
        matches: list[dict[str, str]] = []
        seen: set[str] = set()
        for member in membership_rows:
            if member.get("pathway_id") != pathway_id:
                continue
            row = (
                index.get(("ordered_locus", member.get("ordered_locus", "")))
                or index.get(("uniprot_accession", member.get("uniprot_accession", "")))
                or index.get(("suggested_review_name", member.get("suggested_review_name", "")))
            )
            if not row:
                continue
            key = row.get("uniprot_accession") or row.get("ordered_locus") or row.get("suggested_review_name", "")
            if key and key not in seen:
                matches.append(row)
                seen.add(key)
        if matches:
            return matches

    if bucket_id:
        return [row for row in partition_rows if row.get("primary_bucket_id") == bucket_id]
    return []


def sort_gene_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    def key(row: dict[str, str]) -> tuple[int, str, str]:
        locus = row.get("ordered_locus", "")
        match = re.fullmatch(r"PP_(\d+)", locus)
        locus_num = int(match.group(1)) if match else 999999
        return (locus_num, row.get("suggested_review_name", ""), row.get("uniprot_accession", ""))

    return sorted(rows, key=key)


def format_candidate_genes(rows: list[dict[str, str]], max_genes: int) -> str:
    if not rows:
        return "No local candidate gene table was available or no genes matched this pathway/bucket."

    lines = []
    for row in sort_gene_rows(rows)[:max_genes]:
        name = row.get("suggested_review_name") or row.get("primary_gene") or row.get("ordered_locus")
        locus = row.get("ordered_locus", "")
        accession = row.get("uniprot_accession", "")
        protein = row.get("protein_name", "")
        ec = row.get("ec_numbers", "")
        primary_bucket = row.get("primary_bucket_id", "")
        details = [part for part in [locus, accession, protein] if part]
        suffix_parts = []
        if ec:
            suffix_parts.append(f"EC {ec}")
        if primary_bucket:
            suffix_parts.append(f"primary bucket {primary_bucket}")
        suffix = f" ({'; '.join(suffix_parts)})" if suffix_parts else ""
        lines.append(f"- {name}: {' | '.join(details)}{suffix}")

    remaining = len(rows) - max_genes
    if remaining > 0:
        lines.append(f"- ... {remaining} additional candidate genes omitted from prompt.")
    return "\n".join(lines)


def actual_provider(provider: str) -> str:
    if provider == "perplexity-lite":
        return "perplexity"
    if provider == "codex":
        return "cyberian"
    return provider


def output_path_for(
    *,
    output: Path | None,
    output_dir: Path | None,
    project_dir: Path | None,
    organism: str,
    module_slug: str,
    pathway_query: str,
    provider: str,
) -> Path:
    if output:
        return output
    directory = output_dir or (project_dir / "deep-research" if project_dir else Path("terms"))
    pathway_slug = slugify(pathway_query)
    return directory / f"{organism}__{module_slug}__{pathway_slug}-deep-research-{provider}.md"


def build_command(
    *,
    variables: dict[str, str],
    provider: str,
    output_path: Path,
    template: Path,
    extra_args: list[str] | None,
) -> list[str]:
    cmd = [
        *deep_research_client_command(),
        "research",
        "--template",
        str(template),
    ]
    for key, value in variables.items():
        cmd.extend(["--var", f"{key}={value}"])
    cmd.extend(["--provider", actual_provider(provider), "--output", str(output_path)])
    if provider == "codex":
        cmd.extend(["--param", "agent_type=codex"])
    if provider == "perplexity-lite":
        cmd.extend(["--param", "reasoning_effort=low", "--param", "model=sonar-pro"])
    if extra_args:
        cmd.extend(extra_args)
    return cmd


def output_contains_unresolved_placeholders(output_path: Path) -> bool:
    if not output_path.exists():
        return False
    text = output_path.read_text(encoding="utf-8", errors="replace")
    return any(pattern in text for pattern in UNRESOLVED_PLACEHOLDER_PATTERNS)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deep research for a module/pathway constrained to a species or taxon."
    )
    parser.add_argument("module", help="Module YAML ref or free-text module name")
    parser.add_argument("pathway", help="Pathway ID, bucket ID, or free-text pathway name")
    parser.add_argument("organism", help="Organism code, species label, or taxon shorthand")
    parser.add_argument("provider", choices=PROVIDERS, help="Deep research provider")
    parser.add_argument(
        "--modules-dir",
        type=Path,
        default=Path("modules"),
        help="Module YAML directory for module lookup (default: modules)",
    )
    parser.add_argument("--project", help="Project slug for local data, e.g. P_PUTIDA")
    parser.add_argument("--project-dir", type=Path, help="Project directory override")
    parser.add_argument("--species-name", help="Target species/strain display name")
    parser.add_argument("--taxon-id", help="NCBI taxon ID")
    parser.add_argument("--proteome-id", help="UniProt proteome ID")
    parser.add_argument("--max-genes", type=int, default=DEFAULT_MAX_GENES)
    parser.add_argument("--output-dir", type=Path, help="Output directory override")
    parser.add_argument("--output", type=Path, help="Output file override")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the deep-research-client command without running it",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        help="Timeout for deep-research-client subprocess in seconds",
    )
    parser.add_argument(
        "--extra-args",
        nargs=argparse.REMAINDER,
        help="Extra args to pass to deep-research-client",
    )
    args = parser.parse_args()

    project_dir = project_dir_for(args)
    defaults = organism_defaults(args.organism)
    species_name = args.species_name or defaults["species_name"]
    taxon_id = args.taxon_id or defaults["taxon_id"]
    proteome_id = args.proteome_id or defaults["proteome_id"]

    module = module_context(args.module, args.modules_dir)
    bucket = resolve_bucket(args.pathway, project_dir)
    rows = candidate_rows(bucket, project_dir)

    variables = {
        "module_title": module["module_title"],
        "module_summary": module["module_summary"],
        "module_outline": module["module_outline"],
        "module_connections": module["module_connections"],
        "pathway_query": args.pathway,
        "pathway_id": bucket["pathway_id"],
        "pathway_name": bucket["pathway_name"],
        "pathway_source": bucket["pathway_source"],
        "pathway_context": bucket["pathway_context"],
        "organism": args.organism,
        "species_name": species_name,
        "taxon_id": taxon_id,
        "proteome_id": proteome_id,
        "candidate_gene_count": str(len(rows)),
        "candidate_genes": format_candidate_genes(rows, args.max_genes),
    }
    output_path = output_path_for(
        output=args.output,
        output_dir=args.output_dir,
        project_dir=project_dir,
        organism=args.organism,
        module_slug=module["module_slug"],
        pathway_query=args.pathway,
        provider=args.provider,
    )
    cmd = build_command(
        variables=variables,
        provider=args.provider,
        output_path=output_path,
        template=args.template,
        extra_args=args.extra_args,
    )

    print(f"Module: {module['module_title']} ({module['module_source']})")
    print(f"Pathway: {bucket['pathway_name']} ({bucket['pathway_id']})")
    print(f"Taxon: {species_name} / {args.organism} / NCBITaxon:{taxon_id}")
    print(f"Candidate genes: {len(rows)}")
    print(f"Provider: {args.provider}")
    print(f"Output: {output_path}")
    print(f"Command: {command_for_log(cmd)}")
    if args.dry_run:
        print("Dry run only; not running deep-research-client.")
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(cmd, timeout=args.timeout)
    except subprocess.TimeoutExpired:
        print(
            f"Error: deep-research-client timed out after {args.timeout}s",
            file=sys.stderr,
        )
        return 124
    if result.returncode != 0:
        return result.returncode
    if output_contains_unresolved_placeholders(output_path):
        print(
            f"Error: generated report still contains unresolved template placeholders: {output_path}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
