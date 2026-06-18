"""Write per-gene PROTEOSTASIS PN consistency notes.

The notes are generated from the manually reviewed phase-1 dossier sections.
Each output file lives beside the gene review as:

    genes/human/GENE/GENE-pn-notes.md

The generated note is intentionally a curation artifact, not a replacement for
the review YAML. It records how the PN placement, projected GO pressure, local
AIGR review, and available deep-research files line up for that gene.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

import yaml


REPO_MARKER = "project.justfile"
PROJECT = "PROTEOSTASIS"


def repo_root() -> Path:
    """Return the repository root from this script path."""
    for parent in Path(__file__).resolve().parents:
        if (parent / REPO_MARKER).exists():
            return parent
    raise RuntimeError(f"Could not find repository root with {REPO_MARKER}")


def today() -> str:
    """Return the current local date for generated note stamps."""
    return date.today().isoformat()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def strip_heading(text: str, heading: str) -> str:
    """Remove the first markdown heading if it matches the expected heading."""
    lines = text.splitlines()
    if lines and lines[0].strip() == heading:
        lines = lines[1:]
        if lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines).strip()


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def markdown_link(path: Path, root: Path, base_dir: Path, label: str | None = None) -> str:
    display = label or rel(path, root)
    target = os.path.relpath(path, start=base_dir)
    return f"[{display}]({Path(target).as_posix()})"


def first_matching_finding(text: str, heading_prefixes: tuple[str, ...]) -> str:
    """Extract a one-paragraph finding from either bullet or bold-heading style."""
    candidates = [line.strip() for line in text.splitlines()]
    candidates.extend(paragraph.strip() for paragraph in re.split(r"\n\s*\n", text))
    for stripped in candidates:
        if not stripped:
            continue
        normalized = stripped[2:].strip() if stripped.startswith("- ") else stripped
        match = re.match(r"\*\*([^*]+?)\s*:?\*\*:?", normalized)
        if not match:
            continue
        heading = match.group(1).rstrip(":")
        if any(heading.startswith(prefix) for prefix in heading_prefixes):
            return f"- {normalized}"
    return ""


def review_metadata(review_path: Path) -> tuple[str, str, str, Counter[str]]:
    """Load a small review summary from GENE-ai-review.yaml."""
    if not review_path.exists():
        return "", "missing", "", Counter()

    data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    uniprot_id = str(data.get("id") or "")
    status = str(data.get("status") or "")
    description = str(data.get("description") or "").replace("\n", " ").strip()
    action_counts: Counter[str] = Counter()
    for annotation in data.get("existing_annotations", []) or []:
        action = ((annotation.get("review") or {}).get("action") or "").strip()
        if action:
            action_counts[action] += 1
    for function in data.get("core_functions", []) or []:
        action = ((function.get("review") or {}).get("action") or "").strip()
        if action:
            action_counts[action] += 1
    return uniprot_id, status, description, action_counts


def format_action_counts(action_counts: Counter[str]) -> str:
    if not action_counts:
        return "No reviewed annotation actions found."
    parts = [f"{action}: {count}" for action, count in sorted(action_counts.items())]
    return "; ".join(parts)


def batch_lookup(review_batches: Path) -> dict[str, dict[str, str]]:
    if not review_batches.exists():
        return {}
    with review_batches.open(encoding="utf-8") as handle:
        return {
            row["gene_symbol"]: row
            for row in csv.DictReader(handle, delimiter="\t")
            if row.get("gene_symbol")
        }


def priority_lookup(priority_genes: Path) -> dict[str, dict[str, str]]:
    if not priority_genes.exists():
        return {}
    with priority_genes.open(encoding="utf-8") as handle:
        return {
            row["gene_symbol"]: row
            for row in csv.DictReader(handle, delimiter="\t")
            if row.get("gene_symbol")
        }


def projection_lookup(projection_summary: Path) -> dict[str, list[dict[str, str]]]:
    if not projection_summary.exists():
        return {}
    rows_by_gene: dict[str, list[dict[str, str]]] = {}
    with projection_summary.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            gene = row.get("gene_symbol")
            if gene:
                rows_by_gene.setdefault(gene, []).append(row)
    return rows_by_gene


def gene_set_from_dossiers(dossier_dir: Path) -> list[str]:
    return sorted(
        path.stem
        for path in dossier_dir.glob("*.md")
        if not path.name.startswith("_")
    )


def deep_research_files(gene_dir: Path, gene: str) -> list[Path]:
    return sorted(gene_dir.glob(f"{gene}-deep-research*.md"))


def supporting_files(gene_dir: Path, gene: str) -> dict[str, Path]:
    return {
        "ai_review_yaml": gene_dir / f"{gene}-ai-review.yaml",
        "ai_review_html": gene_dir / f"{gene}-ai-review.html",
        "gene_notes": gene_dir / f"{gene}-notes.md",
        "goa": gene_dir / f"{gene}-goa.tsv",
        "uniprot": gene_dir / f"{gene}-uniprot.txt",
    }


def file_status_line(path: Path, root: Path, base_dir: Path, label: str) -> str:
    status = "present" if path.exists() else "missing"
    target = markdown_link(path, root, base_dir) if path.exists() else rel(path, root)
    return f"- {label}: {status} - {target}"


def deep_research_lines(root: Path, gene_dir: Path, gene: str) -> list[str]:
    deep_files = deep_research_files(gene_dir, gene)
    if not deep_files:
        return ["- No `*-deep-research*.md` file found in this gene directory."]
    return [f"- {markdown_link(path, root, gene_dir)}" for path in deep_files]


def base_source_lines(root: Path, gene_dir: Path, gene: str) -> list[str]:
    files = supporting_files(gene_dir, gene)
    return [
        file_status_line(files["ai_review_yaml"], root, gene_dir, "AIGR review YAML"),
        file_status_line(files["ai_review_html"], root, gene_dir, "AIGR review HTML"),
        file_status_line(files["gene_notes"], root, gene_dir, "Gene notes"),
        file_status_line(files["goa"], root, gene_dir, "GOA TSV"),
        file_status_line(files["uniprot"], root, gene_dir, "UniProt record"),
    ]


def projection_report_path(root: Path) -> Path:
    return (
        root
        / "projects"
        / PROJECT
        / "reports"
        / "pn_projection"
        / "pn_projected_gene_go_summary.tsv"
    )


def mapping_audit_path(root: Path) -> Path:
    return (
        root
        / "projects"
        / PROJECT
        / "reports"
        / "pn_mapping_audit"
        / "current_mapping_scrutiny.tsv"
    )


def review_snapshot_lines(
    review_path: Path,
) -> tuple[str, str, list[str]]:
    uniprot_id, review_status, description, action_counts = review_metadata(review_path)
    description_line = description or "No top-level review description found."
    return (
        uniprot_id,
        review_status,
        [
            f"- Description: {description_line}",
            f"- Existing/core annotation action counts: {format_action_counts(action_counts)}",
        ],
    )


def build_note(
    *,
    root: Path,
    gene: str,
    generated_date: str,
    dossier_path: Path,
    section_path: Path,
    batch_row: dict[str, str] | None,
) -> str:
    gene_dir = root / "genes" / "human" / gene
    files = supporting_files(gene_dir, gene)
    uniprot_id, review_status, snapshot_lines = review_snapshot_lines(
        files["ai_review_yaml"]
    )

    section = strip_heading(read_text(section_path), f"## {gene}")
    dossier = strip_heading(read_text(dossier_path), f"# PN dossier: {gene}")

    consistency = first_matching_finding(section, ("Consistency",))
    verdict = first_matching_finding(section, ("Verdict",))
    pn_story = first_matching_finding(
        section,
        (
            "PN story / NEW pressure",
            "Does the PN taxonomy tell a story GO misses?",
        ),
    )
    evidence = first_matching_finding(section, ("Evidence alignment",))

    batch_id = (batch_row or {}).get("batch_id", "")
    source_pr = (batch_row or {}).get("source_pr", "")
    change_status = (batch_row or {}).get("change_status", "")

    source_lines = base_source_lines(root, gene_dir, gene) + [
        f"- PN dossier: {markdown_link(dossier_path, root, gene_dir)}",
        f"- PN consistency section: {markdown_link(section_path, root, gene_dir)}",
        "- PN projection report: "
        + markdown_link(projection_report_path(root), root, gene_dir),
        "- PN mapping audit: " + markdown_link(mapping_audit_path(root), root, gene_dir),
    ]

    quick_findings = [
        consistency,
        pn_story,
        evidence,
        verdict,
    ]
    quick_findings = [line for line in quick_findings if line]

    return "\n".join(
        [
            f"# {gene} PN Consistency Notes",
            "",
            f"- Generated: {generated_date}",
            f"- Project: {PROJECT}",
            f"- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts",
            f"- UniProt: {uniprot_id or 'not found'}",
            f"- AIGR review status: {review_status or 'not found'}",
            f"- Review batch: {batch_id or 'not found'}"
            + (f" (PR {source_pr})" if source_pr else ""),
            f"- Batch change status: {change_status or 'not found'}",
            "",
            "## Source Files Checked",
            "",
            *source_lines,
            "",
            "### Deep Research Files",
            "",
            *deep_research_lines(root, gene_dir, gene),
            "",
            "## AIGR Review Snapshot",
            "",
            *snapshot_lines,
            "",
            "## PN Consistency Summary",
            "",
            *(quick_findings or ["No extracted one-line consistency findings found."]),
            "",
            "## Full Consistency Review",
            "",
            section or "No section text found.",
            "",
            "## PN Dossier Context",
            "",
            dossier or "No PN dossier text found.",
            "",
            "## Note",
            "",
            "This file is generated from the current PROTEOSTASIS phase-1 dossier and "
            "local gene-review artifacts. Edit the source review, PN mapping, or dossier "
            "rather than this generated note when correcting the underlying curation.",
            "",
        ]
    )


def projection_lines(projection_rows: list[dict[str, str]]) -> list[str]:
    if not projection_rows:
        return [
            "- No current PN projected GO row for this gene. Treat this priority item as "
            "an exception, boundary, or context-tracking case rather than a direct "
            "GO propagation candidate."
        ]

    lines: list[str] = []
    for row in projection_rows:
        target = f"{row.get('target_go_id', '')} {row.get('target_go_label', '')}".strip()
        lines.append(
            "- "
            + target
            + f" - {row.get('goa_status', 'unknown_goa_status')}; "
            + f"scope={row.get('mapping_scopes', 'unknown_scope')}; "
            + f"mapping={row.get('mapping_files', 'unknown_mapping_file')}; "
            + f"PN={row.get('pn_codes', 'unknown_pn_code')}"
        )
    return lines


def priority_mapping_strategy(category: str) -> str:
    strategies = {
        "positive_control": (
            "Use as a calibration case for PN-to-GO propagation: the PN placement "
            "should agree with an already well-supported local review rather than "
            "driving broad new ontology pressure."
        ),
        "domain_exception": (
            "Keep as an explicit exception to family/domain propagation. The PN "
            "family placement is informative, but the local review should decide "
            "whether canonical chaperone activity is actually supported."
        ),
        "isoform_context_exception": (
            "Keep canonical gene biology separate from readthrough, fusion, or "
            "isoform-specific PN context before propagating family-level mappings."
        ),
        "cc_tpr_exception": (
            "Do not propagate generic HSP90-cochaperone semantics from a TPR-domain "
            "placement when the reviewed biology points to a different mechanism."
        ),
        "multibranch_boundary_case": (
            "Use narrow, evidence-aligned PN mappings, but preserve exceptions "
            "against broad parent propagation across mixed proteostasis branches."
        ),
        "context_specific_ALP": (
            "Treat the PN ALP placement as context-specific regulatory biology. A "
            "non-core GO annotation may be warranted only if the gene-specific "
            "evidence supports it."
        ),
        "contextual_autophagy": (
            "Audit the specific autophagy assertion separately from established UPS "
            "biology; do not let the broad autophagy context override the reviewed "
            "core functions."
        ),
        "ontology_gap_bridge": (
            "Use as a bridge case for ontology design: the PN placement may expose "
            "missing or underspecified GO proteostasis terms rather than a simple "
            "gene-to-existing-term propagation."
        ),
    }
    return strategies.get(
        category,
        "Use the priority record as a boundary-tracking note until a full phase-1 dossier exists.",
    )


def build_priority_note(
    *,
    root: Path,
    gene: str,
    generated_date: str,
    priority_row: dict[str, str],
    projection_rows_for_gene: list[dict[str, str]],
) -> str:
    gene_dir = root / "genes" / "human" / gene
    files = supporting_files(gene_dir, gene)
    uniprot_id, review_status, snapshot_lines = review_snapshot_lines(
        files["ai_review_yaml"]
    )
    project_dir = root / "projects" / PROJECT
    priority_path = project_dir / "priority_genes.tsv"

    mapping_files = sorted(
        {
            filename
            for row in projection_rows_for_gene
            for filename in row.get("mapping_files", "").split(";")
            if filename
        }
    )
    mapping_file_lines = (
        [
            f"- PN mapping file: {markdown_link(project_dir / 'mappings' / filename, root, gene_dir)}"
            for filename in mapping_files
        ]
        if mapping_files
        else ["- PN mapping file: none from current projection rows."]
    )

    category = priority_row.get("category", "unknown")
    why_interesting = priority_row.get("why_interesting", "")
    suggested_next_step = priority_row.get("suggested_next_step", "")
    pn_annotations = priority_row.get("pn_annotations", "")
    local_status = priority_row.get("local_aigr_status", "")
    related_project = priority_row.get("related_project", "")
    strategy = priority_mapping_strategy(category)

    source_lines = base_source_lines(root, gene_dir, gene) + [
        f"- PROTEOSTASIS priority table: {markdown_link(priority_path, root, gene_dir)}",
        "- PN projection report: "
        + markdown_link(projection_report_path(root), root, gene_dir),
        "- PN mapping audit: " + markdown_link(mapping_audit_path(root), root, gene_dir),
        *mapping_file_lines,
    ]

    projection_summary = "; ".join(
        f"{row.get('target_go_id')} {row.get('target_go_label')} ({row.get('goa_status')})"
        for row in projection_rows_for_gene
    )
    pn_pressure = (
        f"Current projection rows: {projection_summary}."
        if projection_summary
        else "No current projected GO row; the value is exception/context tracking."
    )

    return "\n".join(
        [
            f"# {gene} PN Consistency Notes",
            "",
            f"- Generated: {generated_date}",
            f"- Project: {PROJECT}",
            "- Scope: priority-only PN rereview against local AIGR review and "
            "available deep-research artifacts",
            f"- UniProt: {uniprot_id or 'not found'}",
            f"- AIGR review status: {review_status or 'not found'}",
            f"- Priority category: {category}",
            f"- Local AIGR project status: {local_status or 'not found'}",
            f"- Related project: {related_project or 'not recorded'}",
            "",
            "## Source Files Checked",
            "",
            *source_lines,
            "",
            "### Deep Research Files",
            "",
            *deep_research_lines(root, gene_dir, gene),
            "",
            "## AIGR Review Snapshot",
            "",
            *snapshot_lines,
            "",
            "## PN Consistency Summary",
            "",
            f"- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `{local_status or 'not recorded'}`. PN placement: {pn_annotations or 'not recorded'}. Main issue: {why_interesting or 'not recorded'}",
            f"- **PN story / NEW pressure:** {pn_pressure}",
            f"- **Mapping strategy:** {strategy}",
            f"- **Verdict:** {suggested_next_step or 'Create a full phase-1/boundary dossier before changing GO annotations.'}",
            "",
            "## Priority Review Context",
            "",
            f"- Category: {category}",
            f"- PN annotations: {pn_annotations or 'not recorded'}",
            f"- Why interesting: {why_interesting or 'not recorded'}",
            f"- Suggested next step: {suggested_next_step or 'not recorded'}",
            f"- Related project: {related_project or 'not recorded'}",
            "",
            "## PN Projection Rows",
            "",
            *projection_lines(projection_rows_for_gene),
            "",
            "## PN Dossier Context",
            "",
            "No phase-1 dossier exists for this priority-only gene. This note preserves "
            "the current PROTEOSTASIS boundary or exception decision and should be "
            "superseded by a dossier section if the gene is promoted into a full "
            "phase-1 batch.",
            "",
            "## Note",
            "",
            "This file is generated from the current PROTEOSTASIS priority table, PN "
            "projection outputs, and local gene-review artifacts. Edit those source "
            "records rather than this generated note when correcting the underlying "
            "curation.",
            "",
        ]
    )


def write_notes(
    root: Path,
    genes: list[str],
    generated_date: str,
    overwrite: bool,
) -> list[dict[str, str]]:
    project_dir = root / "projects" / PROJECT
    dossier_dir = project_dir / "reports" / "phase1_dossiers"
    section_dir = dossier_dir / "_sections"
    batches = batch_lookup(project_dir / "review_batches.tsv")
    priorities = priority_lookup(project_dir / "priority_genes.tsv")
    projections = projection_lookup(projection_report_path(root))
    rows: list[dict[str, str]] = []

    for gene in genes:
        gene_dir = root / "genes" / "human" / gene
        note_path = gene_dir / f"{gene}-pn-notes.md"
        dossier_path = dossier_dir / f"{gene}.md"
        section_path = section_dir / f"{gene}.md"
        status = "written"
        reason = ""
        source_set = "phase1_dossier" if dossier_path.exists() else "priority_only"

        if not gene_dir.exists():
            status = "skipped"
            reason = "missing_gene_dir"
        elif note_path.exists() and not overwrite:
            status = "skipped"
            reason = "note_exists"
        elif dossier_path.exists() and not section_path.exists():
            status = "skipped"
            reason = "missing_consistency_section"
        elif dossier_path.exists():
            note = build_note(
                root=root,
                gene=gene,
                generated_date=generated_date,
                dossier_path=dossier_path,
                section_path=section_path,
                batch_row=batches.get(gene),
            )
            note_path.write_text(note, encoding="utf-8")
        elif gene in priorities:
            note = build_priority_note(
                root=root,
                gene=gene,
                generated_date=generated_date,
                priority_row=priorities[gene],
                projection_rows_for_gene=projections.get(gene, []),
            )
            note_path.write_text(note, encoding="utf-8")
        else:
            status = "skipped"
            reason = "missing_pn_dossier"

        rows.append(
            {
                "gene_symbol": gene,
                "status": status,
                "source_set": source_set,
                "reason": reason,
                "note_path": rel(note_path, root),
                "dossier_path": rel(dossier_path, root),
                "section_path": rel(section_path, root),
                "deep_research_file_count": str(
                    len(deep_research_files(gene_dir, gene)) if gene_dir.exists() else 0
                ),
            }
        )

    return rows


def write_manifest(root: Path, rows: list[dict[str, str]]) -> Path:
    output_path = (
        root
        / "projects"
        / PROJECT
        / "reports"
        / "pn_notes_manifest.tsv"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "gene_symbol",
        "status",
        "source_set",
        "reason",
        "note_path",
        "dossier_path",
        "section_path",
        "deep_research_file_count",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=fields,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    return output_path


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--date",
        default=today(),
        help="Generated date to stamp into notes, default: current date.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing GENE-pn-notes.md files.",
    )
    parser.add_argument(
        "--genes",
        nargs="*",
        help="Optional explicit gene symbols. Default: all phase-1 dossier genes.",
    )
    return parser


def main() -> None:
    root = repo_root()
    project_dir = root / "projects" / PROJECT
    dossier_dir = project_dir / "reports" / "phase1_dossiers"
    args = build_arg_parser().parse_args()
    if args.genes:
        genes = sorted(args.genes)
    else:
        priorities = priority_lookup(project_dir / "priority_genes.tsv")
        genes = sorted(set(gene_set_from_dossiers(dossier_dir)) | set(priorities))
    rows = write_notes(root, genes, args.date, args.overwrite)
    manifest_path = write_manifest(root, rows)
    counts = Counter(row["status"] for row in rows)
    print(
        f"Wrote PN notes manifest {manifest_path} "
        f"(genes={len(rows)} written={counts.get('written', 0)} "
        f"skipped={counts.get('skipped', 0)})"
    )


if __name__ == "__main__":
    main()
