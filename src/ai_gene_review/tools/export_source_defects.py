#!/usr/bin/env python3
"""Collect structured source-database defects for upstream reporting.

Reviews record defects that live in a *source* record, not in this repository,
under ``source_defects`` (see ``docs/source_defects.md``). They appear in two
places:

* ``existing_annotations[].review.source_defects`` in gene reviews
  (``genes/*/*/*-ai-review.yaml``), where the defective record is the GOA/MOD
  annotation row described by the enclosing ``existing_annotations`` entry;
* ``activity_reviews[].source_defects`` in GO-CAM reviews
  (``gocams/*/*-review.yaml``), where it is the GO-CAM activity.

This module flattens both into one row per defect and renders a Markdown report
per responsible resource (the thing that is actually sent upstream).

>>> row = _row(
...     source_path="genes/ARATH/X/X-ai-review.yaml",
...     context={"gene_symbol": "X", "subject_id": "UniProtKB:P1"},
...     defect={"defect_type": "WRONG_REFERENCE", "resource": "TAIR",
...             "asserted_value": "PMID:1", "confidence": "PROBABLE",
...             "explanation": "Mis-keyed."},
... )
>>> row["report_status"]
'NOT_REPORTED'
>>> row["resource"]
'TAIR'
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Iterator

from ruamel.yaml import YAML

COLUMNS = [
    "resource",
    "report_status",
    "defect_type",
    "confidence",
    "source_path",
    "gene_symbol",
    "subject_id",
    "record",
    "term_id",
    "term_label",
    "evidence_type",
    "original_reference_id",
    "qualifier",
    "asserted_value",
    "corrected_value",
    "corrected_label",
    "cause",
    "explanation",
    "supported_by",
    "report_url",
]

DEFAULT_TSV = Path("reports/source-defects.tsv")
DEFAULT_REPORT_DIR = Path("reports/source-defects")


def _load(path: Path) -> Any:
    """Load a YAML file, skipping files that do not mention source_defects."""
    text = path.read_text(encoding="utf-8")
    if "source_defects:" not in text:
        return None
    return YAML(typ="safe").load(text)


def _row(source_path: str, context: dict[str, Any], defect: dict[str, Any]) -> dict[str, str]:
    """Flatten one defect plus its record context into a TSV row."""
    row = {c: "" for c in COLUMNS}
    row.update({k: "" if v is None else str(v) for k, v in context.items()})
    for key in (
        "defect_type", "resource", "record", "asserted_value", "corrected_value",
        "corrected_label", "cause", "confidence", "explanation", "report_url",
    ):
        if defect.get(key) is not None:
            row[key] = " ".join(str(defect[key]).split())
    row["report_status"] = str(defect.get("report_status") or "NOT_REPORTED")
    row["supported_by"] = json.dumps(defect.get("supported_by") or [], ensure_ascii=False)
    row["source_path"] = source_path
    return row


def gene_review_rows(path: Path, root: Path) -> Iterator[dict[str, str]]:
    """Yield defect rows from a gene review's existing annotations."""
    data = _load(path)
    if not data:
        return
    for ann in data.get("existing_annotations") or []:
        review = ann.get("review") or {}
        for defect in review.get("source_defects") or []:
            term = ann.get("term") or {}
            context = {
                "gene_symbol": data.get("gene_symbol", ""),
                "subject_id": f"UniProtKB:{data.get('id', '')}",
                "term_id": term.get("id", ""),
                "term_label": term.get("label", ""),
                "evidence_type": ann.get("evidence_type", ""),
                "original_reference_id": ann.get("original_reference_id", ""),
                "qualifier": ann.get("qualifier", ""),
            }
            yield _row(str(path.relative_to(root)), context, defect)


def gocam_review_rows(path: Path, root: Path) -> Iterator[dict[str, str]]:
    """Yield defect rows from a GO-CAM review's activity reviews."""
    data = _load(path)
    if not data:
        return
    for act in data.get("activity_reviews") or []:
        for defect in act.get("source_defects") or []:
            context = {
                "subject_id": act.get("gene_product", ""),
                "term_id": act.get("molecular_function", ""),
            }
            row = _row(str(path.relative_to(root)), context, defect)
            if not row["record"]:
                row["record"] = act.get("activity_id", "")
            yield row


def collect(root: Path) -> list[dict[str, str]]:
    """Collect every source defect under ``root``, sorted for stable output."""
    rows: list[dict[str, str]] = []
    for path in sorted(root.glob("genes/*/*/*-ai-review.yaml")):
        rows.extend(gene_review_rows(path, root))
    for path in sorted(root.glob("gocams/*/*-review.yaml")):
        rows.extend(gocam_review_rows(path, root))
    rows.sort(key=lambda r: (r["resource"], r["source_path"], r["term_id"], r["asserted_value"]))
    return rows


def render_report(resource: str, rows: list[dict[str, str]]) -> str:
    """Render a Markdown report of open defects for one resource.

    Only rows that have not been fixed or declined are included.

    >>> md = render_report("TAIR", [{**{c: "" for c in COLUMNS}, "resource": "TAIR",
    ...     "report_status": "NOT_REPORTED", "defect_type": "WRONG_GENE_PRODUCT",
    ...     "confidence": "CONFIRMED", "asserted_value": "AGI_LocusCode:AT1G1",
    ...     "corrected_value": "AGI_LocusCode:AT1G2", "explanation": "Swap.",
    ...     "supported_by": "[]"}])
    >>> "AGI_LocusCode:AT1G1" in md and "→ AGI_LocusCode:AT1G2" in md
    True
    """
    open_rows = [r for r in rows if r["report_status"] not in ("FIXED", "DECLINED")]
    lines = [f"# Source-record defects for {resource}", ""]
    lines.append(
        f"{len(open_rows)} open defect(s), generated from `source_defects` blocks "
        "in this repository's reviews. Do not edit by hand."
    )
    for i, r in enumerate(open_rows, 1):
        target = r["record"] or (
            f"{r['subject_id']} {r['qualifier']} {r['term_id']} {r['term_label']} "
            f"({r['evidence_type']}, {r['original_reference_id']})"
        ).strip()
        change = r["asserted_value"]
        if r["corrected_value"]:
            label = f" ({r['corrected_label']})" if r["corrected_label"] else ""
            change += f" → {r['corrected_value']}{label}"
        else:
            change += " (no replacement value; see explanation)"
        lines += [
            "",
            f"## {i}. {r['defect_type']} ({r['confidence']}, {r['report_status']})",
            "",
            f"- **Record:** {target}",
            f"- **Change:** {change}",
        ]
        if r["cause"]:
            lines.append(f"- **Likely cause:** {r['cause']}")
        lines.append(f"- **Recorded in:** `{r['source_path']}`")
        lines += ["", r["explanation"]]
        for ev in json.loads(r["supported_by"] or "[]"):
            lines += ["", f"> {' '.join(str(ev.get('supporting_text', '')).split())}",
                      f"> — {ev.get('reference_id', '')}"]
    return "\n".join(lines) + "\n"


def write_outputs(root: Path, tsv: Path, report_dir: Path) -> list[dict[str, str]]:
    """Write the TSV and one Markdown report per resource; return the rows."""
    rows = collect(root)
    tsv.parent.mkdir(parents=True, exist_ok=True)
    with tsv.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    report_dir.mkdir(parents=True, exist_ok=True)
    for resource in sorted({r["resource"] for r in rows}):
        subset = [r for r in rows if r["resource"] == resource]
        (report_dir / f"{resource}.md").write_text(render_report(resource, subset), encoding="utf-8")
    return rows


def main() -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--tsv", type=Path, default=DEFAULT_TSV)
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    args = parser.parse_args()
    rows = write_outputs(args.root, args.tsv, args.report_dir)
    by_res: dict[str, int] = {}
    for r in rows:
        by_res[r["resource"]] = by_res.get(r["resource"], 0) + 1
    print(f"{len(rows)} source defect(s) -> {args.tsv}; reports in {args.report_dir}: {by_res}")


if __name__ == "__main__":
    main()
