#!/usr/bin/env python
"""Render module YAML files to static HTML pages."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any, Optional
from urllib.parse import quote

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from ai_gene_review.module_qc import collect_module_qc, index_gene_reviews


def as_list(value: Any) -> list[Any]:
    """Return a value as a list, treating null and missing values as empty."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def load_module_yaml(yaml_path: Path) -> dict[str, Any]:
    """Load a module YAML file as a dictionary."""
    if not yaml_path.exists():
        raise FileNotFoundError(f"Module YAML file not found: {yaml_path}")

    data = yaml.safe_load(yaml_path.read_text()) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Module YAML must contain a mapping: {yaml_path}")
    if "module" not in data:
        raise ValueError(f"Module YAML is missing top-level 'module': {yaml_path}")
    return data


def is_module_document(path: Path) -> bool:
    """True if a YAML file is a ModuleReview document (has a top-level ``module:`` key).

    Cheap textual check (no full parse) so that non-module YAML colocated with a
    module -- e.g. a scan-target config, or stray package data under a ``.venv`` --
    is not mistaken for a module.
    """
    try:
        with path.open() as fh:
            for line in fh:
                # a top-level mapping key starts at column 0 (no indentation)
                if line[:1] in (" ", "\t", "#", "\n", "\r", ""):
                    continue
                if line.split(":", 1)[0].strip() == "module":
                    return True
    except OSError:
        return False
    return False


def iter_module_files(modules_dir: Path = Path("modules")) -> list[Path]:
    """Return ModuleReview YAML files under a module directory.

    Skips hidden / virtual-env / cache directories and only returns files that are
    actual module documents, so module-specific support files (configs, analyses,
    ``.venv`` package data) can safely live alongside a module.
    """
    if not modules_dir.exists():
        return []
    skip = {".venv", "__pycache__", ".scan_cache", ".git", "node_modules"}
    files = set()
    for pattern in ("*.yaml", "*.yml"):
        for path in modules_dir.rglob(pattern):
            if not path.is_file():
                continue
            if any(part in skip or part.startswith(".") for part in path.relative_to(modules_dir).parts):
                continue
            if is_module_document(path):
                files.add(path)
    return sorted(files)


def slugify(value: Any) -> str:
    """Make a stable HTML id fragment."""
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9_.:-]+", "-", text)
    text = text.strip("-")
    return text or "item"


def enum_label(value: Any) -> str:
    """Format enum-like strings for display."""
    if value is None:
        return ""
    return str(value).replace("_", " ").title()


def descriptor_text(descriptor: Any) -> str:
    """Return the preferred display text for a descriptor."""
    if not isinstance(descriptor, dict):
        return ""
    term_value = descriptor.get("term")
    term: dict[str, Any] = term_value if isinstance(term_value, dict) else {}
    return (
        descriptor.get("preferred_term")
        or term.get("label")
        or term.get("id")
        or ""
    )


def compact_text(value: Any, limit: int = 150) -> str:
    """Return a compact single-line-ish preview for long prose."""
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= limit:
        return text
    clipped = text[: limit - 1].rstrip()
    if " " in clipped:
        clipped = clipped.rsplit(" ", 1)[0]
    return f"{clipped}..."


def selector_summary(selector: Any) -> str:
    """Return a compact human-readable participant selector."""
    if not isinstance(selector, dict):
        return ""

    selector_type = enum_label(selector.get("selector_type"))
    ordered_slots = (
        "gene",
        "gene_product",
        "protein_complex",
        "family",
        "domain",
        "homolog_of",
        "ortholog_of",
        "required_function",
        "required_domain",
        "taxon",
    )
    for slot in ordered_slots:
        value = selector.get(slot)
        if isinstance(value, dict):
            label = descriptor_text(value)
            if label:
                return f"{selector_type}: {label}" if selector_type else label

    description = selector.get("description")
    if description:
        return f"{selector_type}: {description}" if selector_type else str(description)

    return selector_type


def term_url(term: Any) -> Optional[str]:
    """Return a useful external URL for a term dict when possible."""
    if not isinstance(term, dict):
        return None

    term_id = term.get("id")
    if not term_id or ":" not in term_id:
        return None

    prefix, local_id = term_id.split(":", 1)
    if prefix == "GO":
        return f"https://amigo.geneontology.org/amigo/term/{term_id}"
    if prefix == "NCBITaxon":
        return f"https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={local_id}"
    if prefix == "CHEBI":
        return f"https://www.ebi.ac.uk/chebi/searchId.do?chebiId={term_id}"
    if prefix == "UniProtKB":
        return f"https://www.uniprot.org/uniprotkb/{local_id}/entry"
    if prefix == "PANTHER":
        return f"https://www.pantherdb.org/panther/family.do?clsAccession={quote(local_id, safe='')}"
    if prefix == "CL":
        return f"https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_{local_id}"
    if prefix == "UBERON":
        return f"https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_{local_id}"
    return None


def evidence_url(evidence: Any) -> Optional[str]:
    """Return a useful external URL for an evidence item when possible."""
    if not isinstance(evidence, dict):
        return None
    if evidence.get("url"):
        return str(evidence["url"])

    source_id = evidence.get("source_id")
    if not source_id:
        return None
    if str(source_id).startswith("PMID:"):
        return f"https://pubmed.ncbi.nlm.nih.gov/{str(source_id).split(':', 1)[1]}/"
    if str(source_id).startswith("DOI:"):
        return f"https://doi.org/{str(source_id).split(':', 1)[1]}"
    if str(source_id).startswith("GO:"):
        return f"https://amigo.geneontology.org/amigo/term/{source_id}"
    if str(source_id).startswith("MetaCyc:"):
        return f"https://metacyc.org/META/NEW-IMAGE?type=PATHWAY&object={str(source_id).split(':', 1)[1]}"
    return None


def collect_module_stats(data: dict[str, Any]) -> dict[str, int]:
    """Collect simple recursive counts for a module document."""
    stats = {
        "nodes": 0,
        "annotons": 0,
        "parts": 0,
        "variant_sets": 0,
        "variants": 0,
        "connections": 0,
    }

    def walk(node: dict[str, Any]) -> None:
        stats["nodes"] += 1
        stats["annotons"] += len(as_list(node.get("annotons")))
        stats["connections"] += len(as_list(node.get("connections")))

        parts = as_list(node.get("parts"))
        stats["parts"] += len(parts)
        for part in parts:
            if isinstance(part, dict) and isinstance(part.get("node"), dict):
                walk(part["node"])

        variant_sets = as_list(node.get("variant_sets"))
        stats["variant_sets"] += len(variant_sets)
        for variant_set in variant_sets:
            if not isinstance(variant_set, dict):
                continue
            variants = as_list(variant_set.get("variants"))
            stats["variants"] += len(variants)
            for variant in variants:
                if isinstance(variant, dict):
                    walk(variant)

    module = data.get("module")
    if isinstance(module, dict):
        walk(module)
    return stats


def collect_module_taxa(data: dict[str, Any]) -> list[str]:
    """Collect unique taxon/context labels from a module document."""
    taxa: dict[str, str] = {}

    def add_taxon(descriptor: Any) -> None:
        if not isinstance(descriptor, dict):
            return
        text = descriptor_text(descriptor)
        if not text:
            return
        term = descriptor.get("term")
        key = (
            str(term.get("id"))
            if isinstance(term, dict) and term.get("id")
            else text.lower()
        )
        taxa.setdefault(key, text)

    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "taxa":
                    for descriptor in as_list(value):
                        add_taxon(descriptor)
                elif key == "taxon":
                    add_taxon(value)
                walk(value)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(data)
    return sorted(taxa.values(), key=str.lower)


def collect_ptn_ids(data: dict[str, Any]) -> list[str]:
    """Collect unique PANTHER PTN ids declared under ancestral_nodes."""
    ptn_ids: set[str] = set()

    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            ancestral_nodes = obj.get("ancestral_nodes")
            if isinstance(ancestral_nodes, list):
                for node in ancestral_nodes:
                    if not isinstance(node, dict):
                        continue
                    term = node.get("term")
                    if not isinstance(term, dict):
                        continue
                    term_id = term.get("id")
                    if isinstance(term_id, str) and re.match(r"^PANTHER:PTN\d+$", term_id):
                        ptn_ids.add(term_id)
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(data)
    return sorted(ptn_ids)


def collect_duplicate_ids(data: dict[str, Any]) -> list[str]:
    """Find duplicate node, annoton, and variant set IDs in a module document."""
    counts: dict[str, int] = {}

    def add(value: Any) -> None:
        if value:
            key = str(value)
            counts[key] = counts.get(key, 0) + 1

    def walk(node: dict[str, Any]) -> None:
        add(node.get("id"))
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict):
                add(annoton.get("id"))
        for connection in as_list(node.get("connections")):
            if isinstance(connection, dict):
                add(connection.get("id"))
        for variant_set in as_list(node.get("variant_sets")):
            if not isinstance(variant_set, dict):
                continue
            add(variant_set.get("id"))
            for variant in as_list(variant_set.get("variants")):
                if isinstance(variant, dict):
                    walk(variant)
        for part in as_list(node.get("parts")):
            if isinstance(part, dict) and isinstance(part.get("node"), dict):
                walk(part["node"])

    module = data.get("module")
    if isinstance(module, dict):
        walk(module)

    return sorted(key for key, count in counts.items() if count > 1)


def collect_anchor_map(data: dict[str, Any]) -> dict[str, str]:
    """Map document-scoped module element IDs to HTML anchors."""
    anchors: dict[str, str] = {}

    def add(kind: str, value: Any) -> None:
        if value:
            anchors.setdefault(str(value), f"#{kind}-{slugify(value)}")

    def walk(node: dict[str, Any]) -> None:
        add("node", node.get("id"))
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict):
                add("annoton", annoton.get("id"))
        for variant_set in as_list(node.get("variant_sets")):
            if not isinstance(variant_set, dict):
                continue
            add("variant-set", variant_set.get("id"))
            for variant in as_list(variant_set.get("variants")):
                if isinstance(variant, dict):
                    walk(variant)
        for part in as_list(node.get("parts")):
            if isinstance(part, dict) and isinstance(part.get("node"), dict):
                walk(part["node"])

    module = data.get("module")
    if isinstance(module, dict):
        walk(module)

    return anchors


def anchor_href(value: Any, anchor_map: dict[str, str]) -> str:
    """Return the best local anchor for a document-scoped ID."""
    if value is None:
        return "#"
    return anchor_map.get(str(value), f"#node-{slugify(value)}")


def relative_href(from_file: Path, to_file: Path) -> str:
    """Return a POSIX relative href from one file to another."""
    return os.path.relpath(to_file, start=from_file.parent).replace(os.sep, "/")


def output_path_for_module(
    yaml_path: Path,
    output_dir: Path = Path("pages/modules"),
    modules_dir: Path = Path("modules"),
) -> Path:
    """Return the HTML output path for a module YAML file."""
    try:
        relative = yaml_path.relative_to(modules_dir)
    except ValueError:
        relative = Path(yaml_path.name)
    return output_dir / relative.with_suffix(".html")


def make_summary(
    data: dict[str, Any],
    yaml_path: Path,
    output_path: Path,
    index_path: Path,
    qc: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Build a compact summary used by the module index page."""
    module_value = data.get("module")
    module: dict[str, Any] = module_value if isinstance(module_value, dict) else {}
    concepts = [
        descriptor_text(concept)
        for concept in as_list(module.get("concepts"))
        if descriptor_text(concept)
    ]
    return {
        "id": data.get("id"),
        "title": data.get("title") or module.get("label") or yaml_path.stem,
        "description": data.get("description") or module.get("description"),
        "description_preview": compact_text(
            data.get("description") or module.get("description")
        ),
        "description_is_truncated": (
            compact_text(data.get("description") or module.get("description"))
            != re.sub(
                r"\s+",
                " ",
                str(data.get("description") or module.get("description") or ""),
            ).strip()
        ),
        "status": data.get("status"),
        "scope": data.get("scope"),
        "source_path": yaml_path.as_posix(),
        "href": relative_href(index_path, output_path),
        "module_type": module.get("module_type"),
        "concepts": concepts,
        "taxa": collect_module_taxa(data),
        "ptn_ids": collect_ptn_ids(data),
        "stats": collect_module_stats(data),
        "qc": qc,
    }


def _environment(template_path: Path) -> Environment:
    env = Environment(
        loader=FileSystemLoader(template_path.parent),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["enum_label"] = enum_label
    env.filters["descriptor_text"] = descriptor_text
    env.globals["anchor_id"] = slugify
    env.globals["as_list"] = as_list
    env.globals["descriptor_text"] = descriptor_text
    env.globals["selector_summary"] = selector_summary
    env.globals["term_url"] = term_url
    env.globals["evidence_url"] = evidence_url
    env.globals["anchor_href"] = anchor_href
    env.globals["representative_slots"] = (
        "representative_members",
    )
    env.globals["participant_descriptor_slots"] = (
        "gene",
        "gene_product",
        "protein_complex",
        "family",
        "domain",
        "homolog_of",
        "ortholog_of",
        "required_function",
        "required_domain",
        "taxon",
    )
    env.globals["descriptor_slots"] = (
        "substrates",
        "products",
        "cofactors",
        "targets",
        "cargo",
        "inputs",
        "outputs",
        "occurs_in",
    )
    return env


def clean_rendered_html(html: str) -> str:
    """Strip trailing whitespace from generated HTML while preserving a final newline."""
    return "\n".join(line.rstrip() for line in html.splitlines()) + "\n"


def render_module(
    yaml_path: Path,
    output_dir: Path = Path("pages/modules"),
    modules_dir: Path = Path("modules"),
    template_path: Optional[Path] = None,
    gene_index: Optional[dict[str, Path]] = None,
    genes_dir: Path = Path("genes"),
) -> tuple[Path, list[str]]:
    """Render a single module YAML file to HTML.

    ``gene_index`` (base UniProt accession -> review path) may be supplied to
    avoid re-scanning the gene corpus when rendering many modules; it is built
    lazily inside the QC step when omitted.
    """
    data = load_module_yaml(yaml_path)

    if template_path is None:
        template_path = Path(__file__).parent / "templates" / "module.html.j2"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    output_path = output_path_for_module(yaml_path, output_dir, modules_dir)
    index_path = output_dir / "index.html"
    stats = collect_module_stats(data)
    anchor_map = collect_anchor_map(data)
    qc = collect_module_qc(
        yaml_path, data, gene_index=gene_index, genes_dir=genes_dir
    )
    warnings = [
        f"Duplicate module element id: {duplicate_id}"
        for duplicate_id in collect_duplicate_ids(data)
    ]

    template = _environment(template_path).get_template(template_path.name)
    html = template.render(
        data=data,
        module=data.get("module", {}),
        stats=stats,
        qc=qc,
        source_file=yaml_path.as_posix(),
        output_path=output_path.as_posix(),
        index_href=relative_href(output_path, index_path),
        anchor_map=anchor_map,
        warnings=warnings,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(clean_rendered_html(html), encoding="utf-8")
    return output_path, warnings


def render_modules_index(
    summaries: list[dict[str, Any]],
    output_dir: Path = Path("pages/modules"),
    template_path: Optional[Path] = None,
) -> Path:
    """Render an index page for module HTML pages."""
    if template_path is None:
        template_path = Path(__file__).parent / "templates" / "module_index.html.j2"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    index_path = output_dir / "index.html"
    template = _environment(template_path).get_template(template_path.name)
    html = template.render(
        title="Module KB",
        modules=summaries,
        total_modules=len(summaries),
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path.write_text(clean_rendered_html(html), encoding="utf-8")
    return index_path


def clean_module_html(output_dir: Path = Path("pages/modules")) -> None:
    """Remove previously generated module HTML files."""
    if not output_dir.exists():
        return
    for html_path in output_dir.rglob("*.html"):
        html_path.unlink()
    for directory in sorted(
        (path for path in output_dir.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        try:
            directory.rmdir()
        except OSError:
            pass


def render_all_modules(
    modules_dir: Path = Path("modules"),
    output_dir: Path = Path("pages/modules"),
    template_path: Optional[Path] = None,
    genes_dir: Path = Path("genes"),
) -> tuple[list[Path], list[str]]:
    """Render all module YAML files to HTML and create an index page."""
    output_paths: list[Path] = []
    all_warnings: list[str] = []
    summaries: list[dict[str, Any]] = []
    index_path = output_dir / "index.html"

    yaml_files = iter_module_files(modules_dir)
    if not yaml_files:
        print(f"No module YAML files found in {modules_dir}")
        return output_paths, all_warnings

    # Build the gene-review index once and reuse it across all modules.
    gene_index = index_gene_reviews(genes_dir)

    clean_module_html(output_dir)
    print(f"Found {len(yaml_files)} module files to render")
    for yaml_file in yaml_files:
        try:
            output_path, warnings = render_module(
                yaml_file,
                output_dir=output_dir,
                modules_dir=modules_dir,
                template_path=template_path,
                gene_index=gene_index,
                genes_dir=genes_dir,
            )
            data = load_module_yaml(yaml_file)
            qc = collect_module_qc(
                yaml_file, data, gene_index=gene_index, genes_dir=genes_dir
            )
            summaries.append(
                make_summary(data, yaml_file, output_path, index_path, qc=qc)
            )
            output_paths.append(output_path)

            if warnings:
                all_warnings.extend([f"{yaml_file}: {warning}" for warning in warnings])
                print(f"  {yaml_file} -> {output_path} ({len(warnings)} warnings)")
            else:
                print(f"  {yaml_file} -> {output_path}")
        except Exception as error:
            message = f"{yaml_file}: Error rendering - {error}"
            all_warnings.append(message)
            print(f"  {message}")

    index_output = render_modules_index(sorted(summaries, key=lambda item: item["title"]), output_dir)
    output_paths.append(index_output)
    print(f"\nRendered {len(output_paths) - 1}/{len(yaml_files)} modules to {output_dir}")
    print(f"Rendered module index to {index_output}")

    return output_paths, all_warnings


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m ai_gene_review.render_modules <module.yaml> [output_dir]")
        print("       python -m ai_gene_review.render_modules --all")
        raise SystemExit(1)

    if sys.argv[1] == "--all":
        render_all_modules()
    else:
        module_path = Path(sys.argv[1])
        target_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("pages/modules")
        html_path, render_warnings = render_module(module_path, output_dir=target_dir)
        print(f"Rendered to: {html_path}")
        if render_warnings:
            print(f"Warnings: {render_warnings}")
