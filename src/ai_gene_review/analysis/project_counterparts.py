"""Render curated counterpart assessments for a project's frontmatter genes.

Reads local review YAML only; does not select counterparts or repeat API searches.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import io
import os
from pathlib import Path
from urllib.parse import quote

import yaml

from ai_gene_review.render_projects import (
    build_symbol_to_species_index,
    parse_frontmatter,
    resolve_frontmatter_gene_links,
)


def collect_assessments(project: Path, root: Path) -> list[dict]:
    """Resolve the declared cohort and retain every assessment, including unassessed genes."""
    metadata, _ = parse_frontmatter(project.read_text())
    if not metadata.get("genes"):
        raise ValueError(f"No genes declared in {project}")
    species_hints = metadata.get("species", [])
    if isinstance(species_hints, str):
        species_hints = [species_hints]
    links, warnings = resolve_frontmatter_gene_links(
        metadata["genes"], build_symbol_to_species_index(root / "genes"),
        species_hints=species_hints, genes_dir=root / "genes",
    )
    unresolved = [link["label"] for link in links if not link["url"]]
    if warnings or unresolved:
        raise ValueError("; ".join(warnings + [f"Unresolved gene: {g}" for g in unresolved]))
    rows = []
    seen = set()
    for link in links:
        species, gene = link["species"], link["symbol"]
        path = Path("genes") / species / gene / f"{gene}-ai-review.yaml"
        if path in seen:
            continue
        seen.add(path)
        review = yaml.safe_load((root / path).read_text())
        blocks = [
            *review.get("alternative_records", []),
            *review.get("reference_proteome_assessments", []),
        ]
        for block in blocks or [{}]:
            rows.append({
                "accession": review["id"], "species": species, "gene": gene,
                "status": block.get("relationship", block.get("status", "NOT_ASSESSED"))
                    .removeprefix("REFERENCE_PROTEOME_"),
                "alternative": block.get("id", ""),
                "review_path": path.as_posix(),
                "reference_proteomes": ";".join(
                    [block["reference_proteome"]] if block.get("reference_proteome")
                    else block.get("reference_proteomes", [])
                ),
                "reviewed_on": str(block.get("reviewed_on", "")),
                "reason": block.get("reason", "No structured counterpart assessment recorded."),
                "evidence": block.get("evidence", []),
            })
    return rows


def cell(value: str) -> str:
    """Keep source prose inside a Markdown table cell."""
    return " ".join(str(value).split()).replace("|", "&#124;")


def local_link(path: Path, output: Path) -> str:
    return quote(os.path.relpath(path.resolve(), output.parent.resolve()), safe="/.-_")


def evidence_link(identifier: str, root: Path, output: Path) -> str:
    if identifier.startswith("file:"):
        relative = Path(identifier.removeprefix("file:"))
        path = root / "genes" / relative
        if not path.is_file():
            path = root / relative
        if not path.is_file():
            raise ValueError(f"Missing evidence source: {identifier}")
        return f"[{cell(identifier)}]({local_link(path, output)})"
    if identifier.startswith("PMID:"):
        return f"[{identifier}](https://pubmed.ncbi.nlm.nih.gov/{identifier.split(':', 1)[1]}/)"
    if identifier.startswith(("https://", "http://")):
        return f"[source]({identifier})"
    return f"`{identifier}`"


def render_markdown(rows: list[dict], project: Path, root: Path, output: Path) -> str:
    counts = Counter(row["status"] for row in rows)
    gene_count = len({row["review_path"] for row in rows})
    species_count = len({row["species"] for row in rows})
    command = f"just project-counterparts --project {project.relative_to(root).as_posix()}"
    lines = [
        "---", "title: Curated counterpart assessments",
        "autolink_gene_symbols: false", "---", "",
        "# Curated counterpart assessments", "",
        "<!-- Generated file: edit the gene review YAML or project frontmatter, then regenerate. -->",
        f"Generated from the genes declared in [{project.stem}]({local_link(project, output)}) "
        "and their review YAML. Do not edit this report by hand.", "",
        f"Regenerate: `{command}`. Add `--check` to detect stale outputs.", "",
        f"**{gene_count} gene reviews across {species_count} species directories; "
        f"{len(rows)} assessment rows.** Counts below are rows, so a gene with multiple "
        "assessments can contribute more than once. Unassessed genes remain visible.", "",
        "| Assessment | Rows |", "| --- | ---: |",
    ]
    lines.extend(f"| {status} | {count} |" for status, count in sorted(counts.items()))
    lines.extend([
        "", "Equivalence is a curated judgment and need not imply identical sequence. "
        "Locus counterparts may differ in function or integrity; candidates remain unresolved. "
        "A search with no supported counterpart does not establish gene absence. "
        "This report does not transfer GO annotations or change primary IDs.", "",
        "| Primary review | Alternative | Assessment | Reference proteomes | Reviewed |",
        "| --- | --- | --- | --- | --- |",
    ])
    for row in rows:
        primary = f"[{cell(row['species'] + '/' + row['gene'])}]({local_link(root / row['review_path'], output)})"
        primary += f" · [{row['accession']}](https://www.uniprot.org/uniprotkb/{row['accession']}/entry)"
        alt = row["alternative"]
        alternative = f"[{alt}](https://www.uniprot.org/uniprotkb/{alt}/entry)" if alt else "None asserted"
        proteomes = ", ".join(
            f"[{p}](https://www.uniprot.org/proteomes/{p})"
            for p in row["reference_proteomes"].split(";") if p
        )
        lines.append(f"| {primary} | {alternative} | {row['status']} | {proteomes} | {row['reviewed_on']} |")
    lines.extend(["", "## Rationale and evidence", ""])
    for row in rows:
        lines.extend([
            f"### {row['species']}/{row['gene']} — {row['accession']}", "",
            f"**{row['status']}**" + (f" → {row['alternative']}" if row["alternative"] else ""),
            "", cell(row["reason"]), "",
        ])
        for item in row["evidence"]:
            citations = list(dict.fromkeys(
                evidence_link(cite["reference_id"], root, output)
                for cite in item.get("supported_by", [])
            ))
            lines.append(f"- **{item['type']}**: {cell(item['description'])} " + "; ".join(citations))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_csv(rows: list[dict]) -> str:
    buffer = io.StringIO(newline="")
    fields = ["accession", "species", "gene", "status", "alternative", "review_path",
              "reference_proteomes", "reviewed_on", "reason"]
    writer = csv.DictWriter(buffer, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--project", type=Path, default=Path("projects/ORPHAN_CURATED.md"))
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are missing or stale")
    args = parser.parse_args()
    root = args.root.resolve()
    project = (root / args.project).resolve()
    output_dir = (root / args.output_dir).resolve() if args.output_dir else project.with_suffix("")
    try:
        rows = collect_assessments(project, root)
        markdown_path = output_dir / "COUNTERPARTS.md"
        outputs = {
            markdown_path: render_markdown(rows, project, root, markdown_path),
            output_dir / "counterpart-assessments.csv": render_csv(rows),
        }
        for path, content in outputs.items():
            if args.check:
                if not path.exists() or path.read_text() != content:
                    raise ValueError(f"Stale generated report: {path}; run just project-counterparts")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            print(f"{'Checked' if args.check else 'Wrote'} {path}")
    except ValueError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
