"""Browser payload compaction helpers."""

from __future__ import annotations

from typing import Any


GO_REF_CODENAMES = {
    "GO_REF:0000002": "InterPro2GO",
    "GO_REF:0000003": "EC2GO",
    "GO_REF:0000004": "Keyword2GO",
    "GO_REF:0000008": "MGI orthology",
    "GO_REF:0000015": "InterPro2GO",
    "GO_REF:0000024": "Curated orthology",
    "GO_REF:0000033": "Phylogenetic trees",
    "GO_REF:0000036": "Multi-source manual",
    "GO_REF:0000041": "UniPathway2GO",
    "GO_REF:0000043": "UniProtKB-KW",
    "GO_REF:0000044": "UniProtKB-SubCell",
    "GO_REF:0000050": "Seq-model transfer",
    "GO_REF:0000051": "PomBase keyword",
    "GO_REF:0000052": "IF localization",
    "GO_REF:0000054": "Fusion localization",
    "GO_REF:0000096": "Mouse-rat ortholog",
    "GO_REF:0000104": "UniRule",
    "GO_REF:0000107": "Ensembl Compara",
    "GO_REF:0000108": "Logical inference",
    "GO_REF:0000109": "SubCellular2GO",
    "GO_REF:0000110": "FlyBase",
    "GO_REF:0000111": "IC+ISS inference",
    "GO_REF:0000113": "TFClass2GO",
    "GO_REF:0000114": "Source pipeline 114",
    "GO_REF:0000115": "Rfam2GO",
    "GO_REF:0000116": "Rhea2GO",
    "GO_REF:0000117": "ARBA",
    "GO_REF:0000118": "TreeGrafter2GO",
    "GO_REF:0000119": "Mouse-human orth",
    "GO_REF:0000120": "Combined IEA",
    "GO_REF:0000121": "Source pipeline 121",
    "GO_REF:0000122": "AtSubP",
    "GO_REF:0000123": "YeastPathways2GO",
}

BROWSER_TEXT_LIMITS = {
    "original_reference_title": 20,
    "review.reason": 50,
    "review.summary": 50,
}


def truncate_text(value: str, max_chars: int) -> str:
    """Truncate text to at most max_chars, using an ellipsis when shortened."""
    if len(value) <= max_chars:
        return value
    if max_chars <= 3:
        return value[:max_chars]
    return value[: max_chars - 3].rstrip() + "..."


def compact_browser_row(row: dict[str, Any]) -> dict[str, Any]:
    """Drop inert values and shorten text-heavy browser fields."""
    compact: dict[str, Any] = {}
    reference_id = row.get("original_reference_id")

    for key, value in row.items():
        if value is None or value == []:
            continue

        if key == "original_reference_title":
            if isinstance(reference_id, str) and reference_id.startswith("GO_REF:"):
                value = GO_REF_CODENAMES.get(reference_id, reference_id)
            elif isinstance(value, str):
                value = truncate_text(value, BROWSER_TEXT_LIMITS[key])
        elif key in BROWSER_TEXT_LIMITS and isinstance(value, str):
            value = truncate_text(value, BROWSER_TEXT_LIMITS[key])

        compact[key] = value

    return compact


def compact_browser_rows(data: object) -> object:
    """Compact row-oriented linkml-browser data without changing its JS contract."""
    if not isinstance(data, list):
        return data
    return [
        compact_browser_row(row) if isinstance(row, dict) else row
        for row in data
    ]
