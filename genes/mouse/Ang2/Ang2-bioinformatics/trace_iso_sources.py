#!/usr/bin/env python3
"""Trace mouse Ang2 ISO annotations back to their human ANG source annotations.

This script uses the local GOA export for mouse Ang2 plus the QuickGO annotation
API for the current source gene product (`UniProtKB:P03950`, human ANG) to
classify each local ISO annotation as:

- `DIRECT_EXPERIMENTAL_SOURCE`: current human source has direct experimental GO evidence
- `STATEMENT_SOURCE`: current human source has TAS/NAS support
- `INFERRED_SOURCE_ONLY`: current human source exists but only with inferred/electronic evidence
- `NO_CURRENT_SOURCE_TERM`: no current human ANG annotation matches the transferred term

It also records whether mouse Ang2 already has a non-ISO local annotation for the
same GO term, which helps flag redundant transfers.
"""

from __future__ import annotations

import csv
import json
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SCRIPT_DIR = Path(__file__).resolve().parent
GENE_DIR = SCRIPT_DIR.parent
GOA_PATH = GENE_DIR / "Ang2-goa.tsv"
OUTPUT_TSV = SCRIPT_DIR / "iso_trace.tsv"

MOUSE_UNIPROT_ID = "Q64438"
HUMAN_SOURCE_ID = "P03950"
QUICKGO_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:{gene_product_id}&limit=200"

DIRECT_EXPERIMENTAL_CODES = {
    "EXP",
    "IDA",
    "IPI",
    "IMP",
    "IGI",
    "IEP",
    "HTP",
    "HDA",
    "HMP",
    "HGI",
    "HEP",
}
STATEMENT_CODES = {"TAS", "NAS"}


@dataclass(frozen=True)
class LocalAnnotation:
    row_number: int
    qualifier: str
    go_id: str
    go_name: str
    evidence_code: str
    reference: str
    with_from: str


@dataclass(frozen=True)
class QuickGOAnnotation:
    qualifier: str
    go_id: str
    evidence_code: str
    reference: str
    assigned_by: str


def fetch_quickgo_annotations(gene_product_id: str) -> list[QuickGOAnnotation]:
    """Fetch current annotations for a gene product from QuickGO."""
    url = QUICKGO_URL.format(gene_product_id=gene_product_id)
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request) as response:
        payload = json.load(response)

    annotations: list[QuickGOAnnotation] = []
    for row in payload["results"]:
        references = row.get("reference") or []
        if isinstance(references, str):
            references = [references]
        annotations.append(
            QuickGOAnnotation(
                qualifier=row.get("qualifier") or "",
                go_id=row.get("goId") or "",
                evidence_code=row.get("goEvidence") or "",
                reference="|".join(references),
                assigned_by=row.get("assignedBy") or "",
            )
        )
    return annotations


def load_local_annotations(path: Path) -> list[LocalAnnotation]:
    """Load local GOA annotations from the project TSV export."""
    annotations: list[LocalAnnotation] = []
    with path.open() as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for index, row in enumerate(reader, start=1):
            annotations.append(
                LocalAnnotation(
                    row_number=index,
                    qualifier=row["QUALIFIER"],
                    go_id=row["GO TERM"],
                    go_name=row["GO NAME"],
                    evidence_code=row["GO EVIDENCE CODE"],
                    reference=row["REFERENCE"],
                    with_from=row["WITH/FROM"],
                )
            )
    return annotations


def join_unique(values: Iterable[str]) -> str:
    """Join unique, truthy values in stable sorted order."""
    uniq = sorted({value for value in values if value})
    return "|".join(uniq)


def classify_source(evidence_codes: set[str]) -> str:
    """Classify the current human source support for a transferred term."""
    if not evidence_codes:
        return "NO_CURRENT_SOURCE_TERM"
    if evidence_codes & DIRECT_EXPERIMENTAL_CODES:
        return "DIRECT_EXPERIMENTAL_SOURCE"
    if evidence_codes & STATEMENT_CODES:
        return "STATEMENT_SOURCE"
    return "INFERRED_SOURCE_ONLY"


def main() -> None:
    """Generate the ISO source trace TSV."""
    local_annotations = load_local_annotations(GOA_PATH)
    mouse_non_iso_by_term: dict[str, list[LocalAnnotation]] = defaultdict(list)
    for annotation in local_annotations:
        if annotation.evidence_code != "ISO":
            mouse_non_iso_by_term[annotation.go_id].append(annotation)

    human_annotations = fetch_quickgo_annotations(HUMAN_SOURCE_ID)
    human_by_term: dict[str, list[QuickGOAnnotation]] = defaultdict(list)
    for annotation in human_annotations:
        human_by_term[annotation.go_id].append(annotation)

    iso_annotations = [annotation for annotation in local_annotations if annotation.evidence_code == "ISO"]
    OUTPUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_TSV.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "mouse_row_number",
                "mouse_gene_product_id",
                "qualifier",
                "go_id",
                "go_name",
                "mouse_reference",
                "source_entity",
                "source_match_count",
                "source_evidence_codes",
                "source_references",
                "source_assigned_by",
                "source_status",
                "mouse_non_iso_same_term_codes",
                "mouse_non_iso_same_term_refs",
            ]
        )
        for annotation in iso_annotations:
            source_matches = human_by_term.get(annotation.go_id, [])
            source_evidence_codes = {match.evidence_code for match in source_matches}
            writer.writerow(
                [
                    annotation.row_number,
                    f"UniProtKB:{MOUSE_UNIPROT_ID}",
                    annotation.qualifier,
                    annotation.go_id,
                    annotation.go_name,
                    annotation.reference,
                    f"UniProtKB:{HUMAN_SOURCE_ID}",
                    len(source_matches),
                    join_unique(match.evidence_code for match in source_matches),
                    join_unique(match.reference for match in source_matches),
                    join_unique(match.assigned_by for match in source_matches),
                    classify_source(source_evidence_codes),
                    join_unique(match.evidence_code for match in mouse_non_iso_by_term.get(annotation.go_id, [])),
                    join_unique(match.reference for match in mouse_non_iso_by_term.get(annotation.go_id, [])),
                ]
            )


if __name__ == "__main__":
    main()
