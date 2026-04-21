"""Generate a minimal LinkML schema for Proteostasis Network taxonomy paths.

The Proteostasis Consortium workbook uses a custom five-level hierarchy:

Branch -> Class -> Group -> Type -> Subtype

This script reads the dense worksheet from the workbook, extracts the distinct
labels at each level, normalizes workbook placeholders such as ``(no Group)``
to missing values, and emits a small LinkML schema with:

- enums for each hierarchy level
- a PNPath class for category paths
- a PNToGOMapping tree-root class for curated GO mappings
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd
import yaml

DEFAULT_SHEET_NAME = "dense"
DEFAULT_WORKBOOK_RELEASE = "HPN2.0-2024-04-15"
PLACEHOLDER_PREFIX = "(no "


@dataclass(frozen=True)
class LevelSpec:
    """Configuration for one PN hierarchy level."""

    slot_name: str
    workbook_column: str
    enum_name: str


LEVEL_SPECS = (
    LevelSpec("branch", "Branch", "PNBranchEnum"),
    LevelSpec("pn_class", "Class", "PNClassEnum"),
    LevelSpec("pn_group", "Group", "PNGroupEnum"),
    LevelSpec("pn_type", "Type", "PNTypeEnum"),
    LevelSpec("pn_subtype", "Subtype", "PNSubtypeEnum"),
)


class _NoAliasSafeDumper(yaml.SafeDumper):
    """Disable YAML anchors to keep the generated schema readable."""

    def ignore_aliases(self, data: object) -> bool:  # pragma: no cover - PyYAML hook
        return True


def normalize_workbook_label(value: object) -> str | None:
    """Normalize workbook cells to meaningful taxonomy labels."""
    if pd.isna(value):
        return None
    text = str(value).strip()
    if not text or text.startswith(PLACEHOLDER_PREFIX):
        return None
    return text


def build_enum(labels: Iterable[str]) -> dict[str, dict[str, str]]:
    """Build LinkML permissible_values entries for a set of labels."""
    return {label: {} for label in sorted(set(labels), key=str.casefold)}


def collect_level_values(dataframe: pd.DataFrame) -> dict[str, list[str]]:
    """Collect distinct non-placeholder labels for each PN level."""
    level_values: dict[str, list[str]] = {}
    for level_spec in LEVEL_SPECS:
        values = [
            normalized
            for normalized in (
                normalize_workbook_label(value) for value in dataframe[level_spec.workbook_column]
            )
            if normalized is not None
        ]
        level_values[level_spec.enum_name] = sorted(set(values), key=str.casefold)
    return level_values


def build_schema(level_values: dict[str, list[str]], workbook_release: str) -> dict[str, object]:
    """Create the LinkML schema document."""
    schema: dict[str, object] = {
        "id": "https://ai4curation.io/ai-gene-review/schema/contrib/pn",
        "name": "proteostasis_network",
        "title": "Proteostasis Network taxonomy and GO mapping schema",
        "description": (
            "Minimal LinkML schema for representing Proteostasis Consortium taxonomy paths "
            "and curated mappings from those paths to Gene Ontology terms. Hierarchy labels "
            f"are derived from the Human Proteostasis Network workbook release {workbook_release}. "
            "Workbook placeholders such as '(no Group)', '(no Type)', and '(no Subtype)' "
            "are normalized to missing values rather than treated as vocabulary members."
        ),
        "prefixes": {
            "linkml": "https://w3id.org/linkml/",
            "pn": "https://ai4curation.io/ai-gene-review/pn/",
            "GO": "http://purl.obolibrary.org/obo/GO_",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
        },
        "imports": ["linkml:types"],
        "default_prefix": "pn",
        "default_range": "string",
        "slots": {
            "id": {"identifier": True},
            "label": {
                "required": True,
                "slot_uri": "rdfs:label",
                "description": "Human-readable label for the entity.",
            },
            "notes": {
                "range": "string",
                "description": "Supplementary notes or curation comments.",
            },
            "references": {
                "range": "string",
                "multivalued": True,
                "description": "Supporting manuscript IDs, workbook IDs, PMIDs, or local file references.",
            },
            "branch": {
                "range": "PNBranchEnum",
                "required": True,
                "description": "Top-level Proteostasis Network branch.",
            },
            "pn_class": {
                "range": "PNClassEnum",
                "description": "Proteostasis Network class label.",
            },
            "pn_group": {
                "range": "PNGroupEnum",
                "description": "Proteostasis Network group label.",
            },
            "pn_type": {
                "range": "PNTypeEnum",
                "description": "Proteostasis Network type label.",
            },
            "pn_subtype": {
                "range": "PNSubtypeEnum",
                "description": "Proteostasis Network subtype label.",
            },
            "path": {
                "range": "PNPath",
                "required": True,
                "inlined": True,
                "description": "Proteostasis Network path being mapped to GO.",
            },
            "relation": {
                "range": "string",
                "required": True,
                "description": (
                    "Semantic relationship between the PN path and the GO target. "
                    "Suggested values include exact, pn_narrower_than_go, "
                    "requires_composition, ontology_gap, and non_go_category."
                ),
            },
            "go_terms": {
                "range": "uriorcurie",
                "multivalued": True,
                "description": "Mapped GO term CURIEs, when an existing GO target is appropriate.",
            },
            "rationale": {
                "range": "string",
                "required": True,
                "description": "Human-authored explanation of the mapping decision.",
            },
        },
        "classes": {
            "PNPath": {
                "description": "A contiguous Proteostasis Network path at any granularity.",
                "slots": [
                    "branch",
                    "pn_class",
                    "pn_group",
                    "pn_type",
                    "pn_subtype",
                    "notes",
                ],
            },
            "PNToGOMapping": {
                "tree_root": True,
                "description": "A curated mapping from a PN path to one or more GO terms.",
                "slots": [
                    "id",
                    "label",
                    "path",
                    "relation",
                    "go_terms",
                    "rationale",
                    "references",
                    "notes",
                ],
            },
        },
        "enums": {},
    }

    for level_spec in LEVEL_SPECS:
        schema["enums"][level_spec.enum_name] = {
            "description": f"Valid Proteostasis Network labels for {level_spec.workbook_column}.",
            "permissible_values": build_enum(level_values[level_spec.enum_name]),
        }

    return schema


def generate_schema(
    workbook: Path,
    output: Path,
    sheet_name: str = DEFAULT_SHEET_NAME,
    workbook_release: str = DEFAULT_WORKBOOK_RELEASE,
) -> None:
    """Generate the PN LinkML schema from a workbook."""
    dataframe = pd.read_excel(workbook, sheet_name=sheet_name)
    dataframe.columns = [str(column).strip() for column in dataframe.columns]
    level_values = collect_level_values(dataframe)
    schema = build_schema(level_values, workbook_release=workbook_release)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        yaml.dump(
            schema,
            Dumper=_NoAliasSafeDumper,
            sort_keys=False,
            allow_unicode=False,
            width=120,
        ),
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, required=True, help="Path to the Proteostasis workbook (.xlsx).")
    parser.add_argument("--output", type=Path, required=True, help="Path to write the generated LinkML schema.")
    parser.add_argument(
        "--sheet-name",
        default=DEFAULT_SHEET_NAME,
        help=f"Workbook sheet to read. Default: {DEFAULT_SHEET_NAME}",
    )
    parser.add_argument(
        "--workbook-release",
        default=DEFAULT_WORKBOOK_RELEASE,
        help=f"Release label to record in the schema description. Default: {DEFAULT_WORKBOOK_RELEASE}",
    )
    return parser


def main() -> None:
    """Run the CLI."""
    parser = build_parser()
    args = parser.parse_args()
    generate_schema(
        workbook=args.workbook,
        output=args.output,
        sheet_name=args.sheet_name,
        workbook_release=args.workbook_release,
    )


if __name__ == "__main__":
    main()
