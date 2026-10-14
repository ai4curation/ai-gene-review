#!/usr/bin/env python3
"""Export top-level proposed_new_terms from ai-gene-review YAML to TSV."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML


COLUMNS = [
    "source_path",
    "organism",
    "gene_directory",
    "review_id",
    "gene_symbol",
    "taxon_id",
    "taxon_label",
    "term_index",
    "proposed_name",
    "proposed_definition",
    "justification",
    "proposed_parent_id",
    "proposed_parent_label",
    "proposed_mappings",
    "supported_by",
]


DEFAULT_OUTPUT_PATH = Path("reports/proposed_new_terms.tsv")

PROPOSED_NEW_TERMS_BLOCK = re.compile(
    r"^proposed_new_terms:(?![ \t]*\[\][ \t]*(?:#.*)?$)", re.MULTILINE
)


def clean_scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return compact_json(value)
    return " ".join(str(value).split())


def compact_json(value: Any) -> str:
    if not value:
        return ""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def clean_nested(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: clean_nested(nested) for key, nested in value.items()}
    if isinstance(value, list):
        return [clean_nested(nested) for nested in value]
    return value


def expand_inputs(inputs: list[Path]) -> list[Path]:
    if not inputs:
        inputs = [Path("genes")]

    paths: set[Path] = set()
    for input_path in inputs:
        if input_path.is_dir():
            paths.update(input_path.rglob("*-ai-review.yaml"))
        elif input_path.is_file():
            paths.add(input_path)
        else:
            raise FileNotFoundError(f"Review input does not exist: {input_path}")

    return sorted(paths, key=lambda path: path.as_posix())


def path_context(path: Path) -> tuple[str, str]:
    parts = path.parts
    if "genes" not in parts:
        return "", ""

    genes_index = parts.index("genes")
    if len(parts) <= genes_index + 2:
        return "", ""

    return parts[genes_index + 1], parts[genes_index + 2]


def format_mappings(term: dict[str, Any]) -> str:
    mappings = [
        clean_nested(mapping) for mapping in term.get("proposed_mappings") or []
    ]
    return compact_json(mappings)


def format_supported_by(term: dict[str, Any]) -> str:
    evidence = []
    for source in term.get("supported_by") or []:
        evidence.append(clean_nested(source))
    return compact_json(evidence)


def read_review_with_proposed_terms(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    if not PROPOSED_NEW_TERMS_BLOCK.search(text):
        return None
    return text


def rows_for_review(path: Path, review_text: str, yaml: YAML) -> list[dict[str, str]]:
    data = yaml.load(review_text)
    if not isinstance(data, dict):
        return []

    proposed_terms = data.get("proposed_new_terms") or []
    if not isinstance(proposed_terms, list):
        raise TypeError(f"{path}: proposed_new_terms must be a list")

    taxon = data.get("taxon") or {}
    organism, gene_directory = path_context(path)
    rows = []
    for index, term in enumerate(proposed_terms, start=1):
        if not isinstance(term, dict):
            raise TypeError(
                f"{path}: proposed_new_terms[{index - 1}] must be a mapping"
            )

        parent = term.get("proposed_parent") or {}
        rows.append(
            {
                "source_path": path.as_posix(),
                "organism": organism,
                "gene_directory": gene_directory,
                "review_id": clean_scalar(data.get("id")),
                "gene_symbol": clean_scalar(data.get("gene_symbol")),
                "taxon_id": clean_scalar(taxon.get("id")),
                "taxon_label": clean_scalar(taxon.get("label")),
                "term_index": str(index),
                "proposed_name": clean_scalar(term.get("proposed_name")),
                "proposed_definition": clean_scalar(term.get("proposed_definition")),
                "justification": clean_scalar(term.get("justification")),
                "proposed_parent_id": clean_scalar(parent.get("id")),
                "proposed_parent_label": clean_scalar(parent.get("label")),
                "proposed_mappings": format_mappings(term),
                "supported_by": format_supported_by(term),
            }
        )
    return rows


def export_proposed_terms(review_paths: list[Path], output_path: Path) -> int:
    yaml = YAML(typ="safe")
    rows: list[dict[str, str]] = []
    for path in expand_inputs(review_paths):
        review_text = read_review_with_proposed_terms(path)
        if review_text is None:
            continue
        rows.extend(rows_for_review(path, review_text, yaml))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=COLUMNS,
            delimiter="\t",
            quotechar=None,
            quoting=csv.QUOTE_NONE,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export top-level proposed_new_terms entries to TSV."
    )
    parser.add_argument(
        "reviews",
        nargs="*",
        type=Path,
        help="Review YAML files or directories to scan. Defaults to genes/.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help=f"TSV output path. Defaults to {DEFAULT_OUTPUT_PATH}.",
    )
    args = parser.parse_args()

    row_count = export_proposed_terms(args.reviews, args.output)
    print(f"Wrote {row_count} proposed term rows to {args.output}")


if __name__ == "__main__":
    main()
