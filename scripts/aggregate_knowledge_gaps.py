#!/usr/bin/env python3
"""Aggregate all curated KnowledgeGap entries into a structured register.

Knowledge gaps can be attached at five levels in the schema:

- ``GeneReview.knowledge_gaps``            (whole-gene gap)
- ``ExistingAnnotation.review.knowledge_gaps``  (per-annotation residual sub-gap)
- ``CoreFunction.knowledge_gaps``          (per-core-function residual sub-gap)
- ``ModuleReview.knowledge_gaps``          (whole-module gap)
- ``ModuleNode.knowledge_gaps`` (recursively, via parts/variant_sets)  (per-step gap)

This walks every ``genes/**/*-ai-review.yaml`` and ``modules/*.yaml`` file, pulls
out each gap, and writes two artifacts:

- ``reports/knowledge_gaps.tsv`` — one row per gap, for querying/triage.
- ``projects/FUNCTION_KNOWLEDGE_GAPS/structured-gaps.md`` — a rendered Markdown
  register that the Function Knowledge Gaps project page links to.

The Markdown register is the "render from data" surface: the project page no
longer has to hand-maintain the worked-gap list — running this script keeps the
structured register in sync with what curators have actually recorded in the YAML.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
GENES_DIR = REPO_ROOT / "genes"
MODULES_DIR = REPO_ROOT / "modules"
TSV_OUT = REPO_ROOT / "reports" / "knowledge_gaps.tsv"
MD_OUT = REPO_ROOT / "projects" / "FUNCTION_KNOWLEDGE_GAPS" / "structured-gaps.md"


@dataclass
class GapRow:
    """A single knowledge gap flattened for tabular output."""

    source_file: str
    entity_id: str
    entity_symbol: str
    level: str
    gap_statement: str
    gap_kind: str
    dark_aspect: str
    status: str
    n_provenance: int
    provenance_refs: list[str] = field(default_factory=list)


def _as_gaps(obj: Any) -> list[dict]:
    """Return the knowledge_gaps list of a mapping, or an empty list."""
    if isinstance(obj, dict):
        gaps = obj.get("knowledge_gaps")
        if isinstance(gaps, list):
            return [g for g in gaps if isinstance(g, dict)]
    return []


def _gap_rows(
    gaps: Iterable[dict],
    *,
    source_file: str,
    entity_id: str,
    entity_symbol: str,
    level: str,
) -> list[GapRow]:
    rows: list[GapRow] = []
    for gap in gaps:
        provenance = gap.get("provenance") or []
        refs = [
            str(p.get("reference_id", "")).strip()
            for p in provenance
            if isinstance(p, dict)
        ]
        kind = gap.get("gap_kind") or []
        rows.append(
            GapRow(
                source_file=source_file,
                entity_id=entity_id,
                entity_symbol=entity_symbol,
                level=level,
                gap_statement=" ".join(str(gap.get("gap_statement", "")).split()),
                gap_kind="|".join(kind) if isinstance(kind, list) else str(kind),
                dark_aspect=str(gap.get("dark_aspect", "") or ""),
                status=str(gap.get("status", "") or ""),
                n_provenance=len(refs),
                provenance_refs=[r for r in refs if r],
            )
        )
    return rows


def _walk_module_node(
    node: dict,
    *,
    source_file: str,
    module_id: str,
    module_label: str,
) -> list[GapRow]:
    """Recursively collect gaps from a ModuleNode and its parts/variant_sets."""
    rows: list[GapRow] = []
    label = node.get("label") or node.get("id") or module_label
    rows.extend(
        _gap_rows(
            _as_gaps(node),
            source_file=source_file,
            entity_id=str(node.get("id", module_id)),
            entity_symbol=str(label),
            level="module_node",
        )
    )
    for part in node.get("parts") or []:
        if isinstance(part, dict) and isinstance(part.get("node"), dict):
            rows.extend(
                _walk_module_node(
                    part["node"],
                    source_file=source_file,
                    module_id=module_id,
                    module_label=module_label,
                )
            )
    for vset in node.get("variant_sets") or []:
        if isinstance(vset, dict):
            for variant in vset.get("variants") or []:
                if isinstance(variant, dict):
                    rows.extend(
                        _walk_module_node(
                            variant,
                            source_file=source_file,
                            module_id=module_id,
                            module_label=module_label,
                        )
                    )
    return rows


def collect_gene_gaps(path: Path) -> list[GapRow]:
    """Collect all gaps from a single gene review file."""
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        return []
    rel = str(path.relative_to(REPO_ROOT))
    gene_id = str(data.get("id", ""))
    symbol = str(data.get("gene_symbol", path.parent.name))
    rows: list[GapRow] = []
    rows.extend(
        _gap_rows(
            _as_gaps(data),
            source_file=rel,
            entity_id=gene_id,
            entity_symbol=symbol,
            level="gene",
        )
    )
    for ann in data.get("existing_annotations") or []:
        if isinstance(ann, dict) and isinstance(ann.get("review"), dict):
            term = ann.get("term") or {}
            term_label = term.get("label") if isinstance(term, dict) else None
            rows.extend(
                _gap_rows(
                    _as_gaps(ann["review"]),
                    source_file=rel,
                    entity_id=gene_id,
                    entity_symbol=f"{symbol} / {term_label or 'annotation'}",
                    level="annotation",
                )
            )
    for cf in data.get("core_functions") or []:
        if isinstance(cf, dict):
            rows.extend(
                _gap_rows(
                    _as_gaps(cf),
                    source_file=rel,
                    entity_id=gene_id,
                    entity_symbol=f"{symbol} (core function)",
                    level="core_function",
                )
            )
    return rows


def collect_module_gaps(path: Path) -> list[GapRow]:
    """Collect all gaps from a single module file."""
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        return []
    rel = str(path.relative_to(REPO_ROOT))
    module_id = str(data.get("id", path.stem))
    title = str(data.get("title", module_id))
    rows: list[GapRow] = []
    rows.extend(
        _gap_rows(
            _as_gaps(data),
            source_file=rel,
            entity_id=module_id,
            entity_symbol=title,
            level="module",
        )
    )
    module = data.get("module")
    if isinstance(module, dict):
        rows.extend(
            _walk_module_node(
                module,
                source_file=rel,
                module_id=module_id,
                module_label=title,
            )
        )
    return rows


def collect_all() -> list[GapRow]:
    """Collect gaps across all gene reviews and modules."""
    rows: list[GapRow] = []
    for path in sorted(GENES_DIR.rglob("*-ai-review.yaml")):
        rows.extend(collect_gene_gaps(path))
    if MODULES_DIR.exists():
        for path in sorted(MODULES_DIR.glob("*.yaml")):
            rows.extend(collect_module_gaps(path))
    return rows


def write_tsv(rows: list[GapRow], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(
            [
                "source_file",
                "entity_id",
                "entity_symbol",
                "level",
                "status",
                "gap_kind",
                "dark_aspect",
                "n_provenance",
                "provenance_refs",
                "gap_statement",
            ]
        )
        for r in rows:
            writer.writerow(
                [
                    r.source_file,
                    r.entity_id,
                    r.entity_symbol,
                    r.level,
                    r.status,
                    r.gap_kind,
                    r.dark_aspect,
                    r.n_provenance,
                    ";".join(r.provenance_refs),
                    r.gap_statement,
                ]
            )


def write_markdown(rows: list[GapRow], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    n = len(rows)
    by_status: dict[str, int] = {}
    by_kind: dict[str, int] = {}
    for r in rows:
        by_status[r.status or "—"] = by_status.get(r.status or "—", 0) + 1
        for k in r.gap_kind.split("|") if r.gap_kind else ["—"]:
            by_kind[k] = by_kind.get(k, 0) + 1

    lines: list[str] = []
    lines.append("---")
    lines.append('title: "Structured Knowledge-Gap Register"')
    lines.append("---")
    lines.append("")
    lines.append("# Structured Knowledge-Gap Register")
    lines.append("")
    lines.append(
        "<!-- GENERATED FILE. Do not edit by hand. "
        "Regenerate with `python scripts/aggregate_knowledge_gaps.py` "
        "(or `just aggregate-knowledge-gaps`). -->"
    )
    lines.append("")
    lines.append(
        "This register is rendered directly from the `knowledge_gaps` entries curated in "
        "the gene-review and module YAML (see the [KnowledgeGap schema class]"
        "(../../src/ai_gene_review/schema/gene_review.yaml)). It is the structured, "
        "queryable counterpart to the worked prose entries on the "
        "[parent project page](../FUNCTION_KNOWLEDGE_GAPS.md)."
    )
    lines.append("")
    lines.append(f"**{n} curated gap(s)** across genes and modules.")
    lines.append("")
    if by_status:
        lines.append(
            "- **By status:** "
            + ", ".join(f"{k} ({v})" for k, v in sorted(by_status.items()))
        )
    if by_kind:
        lines.append(
            "- **By kind:** "
            + ", ".join(f"{k} ({v})" for k, v in sorted(by_kind.items()))
        )
    lines.append("")
    lines.append("| Entity | Level | Status | Kind | Aspect | Prov. | Gap statement |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: (x.entity_symbol.lower(), x.level)):
        statement = r.gap_statement
        if len(statement) > 240:
            statement = statement[:237] + "…"
        statement = statement.replace("|", "\\|")
        symbol = r.entity_symbol.replace("|", "\\|")
        kind = r.gap_kind.replace("|", " + ") if r.gap_kind else "—"
        lines.append(
            f"| {symbol} | {r.level} | {r.status or '—'} | {kind} | "
            f"{r.dark_aspect or '—'} | {r.n_provenance} | {statement} |"
        )
    lines.append("")
    out.write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tsv", type=Path, default=TSV_OUT)
    parser.add_argument("--markdown", type=Path, default=MD_OUT)
    args = parser.parse_args()

    rows = collect_all()
    write_tsv(rows, args.tsv)
    write_markdown(rows, args.markdown)
    print(f"Collected {len(rows)} knowledge gap(s).")
    print(f"  TSV:      {args.tsv.relative_to(REPO_ROOT)}")
    print(f"  Markdown: {args.markdown.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
