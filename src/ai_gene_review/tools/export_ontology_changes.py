#!/usr/bin/env python3
"""Collect proposed ontology changes for upstream term-tracker reporting.

Reviews record changes an *ontology* should make -- obsolete a term, merge two,
fix a definition, reparent, drop a mapping -- under ``proposed_ontology_changes``.
They appear in two places:

* top level of a gene review (``genes/*/*/*-ai-review.yaml``);
* top level of a module review (``modules/*.yaml``), which is where subtree-level
  obsoletions are usually noticed.

This module flattens both into one row per change and renders a Markdown report
per *ontology* -- the thing that is actually sent upstream, since each ontology
has its own tracker. It is the ontology-side counterpart of
``export_source_defects``, which reports annotation-record defects per resource.

>>> row = _row(
...     source_path="modules/m.yaml",
...     context={"gene_symbol": ""},
...     change={"change_type": "NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
...             "ontology": "GO", "about_node": {"id": "GO:1", "label": "x"},
...             "justification": "Wrong.", "confidence": "PROBABLE"},
... )
>>> row["report_status"]
'NOT_REPORTED'
>>> row["change_dsl"]
'obsolete GO:1'
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Iterator

from ruamel.yaml import YAML

from ai_gene_review.validation.ontology_change_policy import kgcl_dsl

COLUMNS = [
    "ontology",
    "report_status",
    "change_type",
    "confidence",
    "source_path",
    "gene_symbol",
    "about_node",
    "about_node_label",
    "change_dsl",
    "has_direct_replacement",
    "has_direct_replacement_label",
    "has_nondirect_replacement",
    "old_value",
    "new_value",
    "subject",
    "predicate",
    "justification",
    "affected_annotations",
    "supported_by",
    "term_tracker_issue",
    "pull_request",
    "see_also",
]

DEFAULT_TSV = Path("reports/ontology-changes.tsv")
DEFAULT_REPORT_DIR = Path("reports/ontology-changes")

#: Statuses that mean there is nothing left to send.
CLOSED_STATUSES = ("FIXED", "DECLINED")


def _load(path: Path) -> Any:
    """Load a YAML file, skipping files that do not mention proposed_ontology_changes."""
    text = path.read_text(encoding="utf-8")
    if "proposed_ontology_changes:" not in text:
        return None
    return YAML(typ="safe").load(text)


def _term(value: Any) -> tuple[str, str]:
    """Split an inlined term into ``(id, label)``.

    >>> _term({"id": "GO:1", "label": "x"})
    ('GO:1', 'x')
    >>> _term(None)
    ('', '')
    """
    if isinstance(value, dict):
        return str(value.get("id") or ""), str(value.get("label") or "")
    return "", ""


def _row(
    source_path: str, context: dict[str, Any], change: dict[str, Any]
) -> dict[str, str]:
    """Flatten one proposed change plus its review context into a TSV row."""
    row = {c: "" for c in COLUMNS}
    row.update({k: "" if v is None else str(v) for k, v in context.items()})
    for key in (
        "ontology",
        "change_type",
        "confidence",
        "old_value",
        "new_value",
        "predicate",
        "term_tracker_issue",
        "pull_request",
    ):
        if change.get(key) is not None:
            row[key] = " ".join(str(change[key]).split())
    row["justification"] = " ".join(str(change.get("justification") or "").split())
    row["about_node"], row["about_node_label"] = _term(change.get("about_node"))
    direct_id, direct_label = _term(change.get("has_direct_replacement"))
    row["has_direct_replacement"] = direct_id
    row["has_direct_replacement_label"] = direct_label
    row["has_nondirect_replacement"] = "|".join(
        f"{i} {label}".strip()
        for i, label in (
            _term(t) for t in (change.get("has_nondirect_replacement") or [])
        )
        if i
    )
    row["subject"] = _term(change.get("subject"))[0]
    row["affected_annotations"] = "|".join(
        str(a) for a in (change.get("affected_annotations") or [])
    )
    row["see_also"] = "|".join(str(u) for u in (change.get("see_also") or []))
    row["supported_by"] = json.dumps(
        change.get("supported_by") or [], ensure_ascii=False
    )
    row["report_status"] = str(change.get("report_status") or "NOT_REPORTED")
    # The DSL is optional in the YAML; derive it when absent so every row that
    # can be expressed as KGCL carries it.
    row["change_dsl"] = " ".join(
        str(change.get("change_dsl") or kgcl_dsl(change) or "").split()
    )
    row["source_path"] = source_path
    return row


def _review_rows(
    path: Path, root: Path, context: dict[str, Any]
) -> Iterator[dict[str, str]]:
    """Yield change rows from one review file."""
    data = _load(path)
    if not data:
        return
    resolved = {k: v(data) if callable(v) else v for k, v in context.items()}
    for change in data.get("proposed_ontology_changes") or []:
        if isinstance(change, dict):
            yield _row(str(path.relative_to(root)), resolved, change)


def collect(root: Path) -> list[dict[str, str]]:
    """Collect every proposed ontology change under ``root``, sorted for stable output."""
    rows: list[dict[str, str]] = []
    for path in sorted(root.glob("genes/*/*/*-ai-review.yaml")):
        rows.extend(
            _review_rows(
                path, root, {"gene_symbol": lambda d: d.get("gene_symbol", "")}
            )
        )
    for path in sorted(root.glob("modules/*.yaml")):
        rows.extend(_review_rows(path, root, {}))
    rows.sort(
        key=lambda r: (
            r["ontology"],
            r["about_node"],
            r["source_path"],
            r["change_type"],
        )
    )
    return rows


def _describe(r: dict[str, str]) -> str:
    """One line naming the change, preferring its KGCL DSL.

    >>> _describe({"change_dsl": "obsolete GO:1", "change_type": "X", "about_node": "GO:1"})
    'obsolete GO:1'
    >>> _describe({"change_dsl": "", "change_type": "COMPLEX_CHANGE", "about_node": "GO:1"})
    'COMPLEX_CHANGE on GO:1 (see justification)'
    """
    if r["change_dsl"]:
        return r["change_dsl"]
    return f"{r['change_type']} on {r['about_node']} (see justification)"


def render_report(ontology: str, rows: list[dict[str, str]]) -> str:
    """Render a Markdown report of open change requests for one ontology.

    Only rows that are neither fixed nor declined are included.

    >>> md = render_report("GO", [{**{c: "" for c in COLUMNS}, "ontology": "GO",
    ...     "report_status": "NOT_REPORTED", "change_type": "NODE_RENAME",
    ...     "about_node": "GO:1", "about_node_label": "old",
    ...     "old_value": "old", "new_value": "new", "confidence": "PROBABLE",
    ...     "justification": "Miscased.", "supported_by": "[]"}])
    >>> "GO:1" in md and "Miscased." in md
    True
    """
    open_rows = [r for r in rows if r["report_status"] not in CLOSED_STATUSES]
    lines = [f"# Proposed ontology changes for {ontology}", ""]
    lines.append(
        f"{len(open_rows)} open request(s), generated from `proposed_ontology_changes` "
        "blocks in this repository's reviews. Do not edit by hand."
    )
    lines.append("")
    lines.append(
        "Each request is a change to an existing term. Where a `Change` line is given "
        "in KGCL's controlled English it can be applied with `oaklib apply`; a "
        "COMPLEX_CHANGE or OTHER request has no such form and the rationale carries it."
    )
    for i, r in enumerate(open_rows, 1):
        label = f" *{r['about_node_label']}*" if r["about_node_label"] else ""
        lines += [
            "",
            f"## {i}. {r['change_type']} ({r['confidence']}, {r['report_status']})",
            "",
            f"- **Term:** {r['about_node']}{label}",
            f"- **Change:** {_describe(r)}",
        ]
        if r["has_direct_replacement"]:
            rep_label = (
                f" *{r['has_direct_replacement_label']}*"
                if r["has_direct_replacement_label"]
                else ""
            )
            lines.append(
                f"- **Replacement (term replaced by):** {r['has_direct_replacement']}{rep_label}"
            )
        if r["has_nondirect_replacement"]:
            alts = ", ".join(r["has_nondirect_replacement"].split("|"))
            lines.append(f"- **Alternatives (consider):** {alts}")
        if r["change_type"] == "REMOVE_MAPPING":
            # A removal has no new value, so an arrow to an empty string is noise.
            if r["old_value"]:
                lines.append(f"- **Mapping to remove:** `{r['old_value']}`")
        elif r["old_value"] or r["new_value"]:
            lines.append(f"- **Value:** `{r['old_value']}` → `{r['new_value']}`")
        if r["subject"]:
            lines.append(f"- **Other end of edge:** {r['predicate']} {r['subject']}")
        if r["affected_annotations"]:
            lines.append("- **Depends on it here:**")
            for a in r["affected_annotations"].split("|"):
                lines.append(f"  - `{a}`")
        lines.append(f"- **Recorded in:** `{r['source_path']}`")
        if r["term_tracker_issue"]:
            lines.append(f"- **Tracker:** {r['term_tracker_issue']}")
        if r["pull_request"]:
            lines.append(f"- **Pull request:** {r['pull_request']}")
        if r["see_also"]:
            for u in r["see_also"].split("|"):
                lines.append(f"- **See also:** {u}")
        lines += ["", r["justification"]]
        for ev in json.loads(r["supported_by"] or "[]"):
            text = " ".join(str(ev.get("supporting_text") or "").split())
            if text:
                lines += ["", f"> {text}", f"> — {ev.get('reference_id', '')}"]
            else:
                lines += ["", f"- **Evidence reference:** {ev.get('reference_id', '')}"]
    return "\n".join(lines) + "\n"


def write_outputs(root: Path, tsv: Path, report_dir: Path) -> list[dict[str, str]]:
    """Write the TSV and one Markdown report per ontology; return the rows."""
    rows = collect(root)
    tsv.parent.mkdir(parents=True, exist_ok=True)
    with tsv.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)
    report_dir.mkdir(parents=True, exist_ok=True)
    for ontology in sorted({r["ontology"] for r in rows}):
        subset = [r for r in rows if r["ontology"] == ontology]
        (report_dir / f"{ontology}.md").write_text(
            render_report(ontology, subset), encoding="utf-8"
        )
    return rows


def main() -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--tsv", type=Path, default=DEFAULT_TSV)
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    args = parser.parse_args()
    rows = write_outputs(args.root, args.tsv, args.report_dir)
    by_ont: dict[str, int] = {}
    for r in rows:
        by_ont[r["ontology"]] = by_ont.get(r["ontology"], 0) + 1
    print(
        f"{len(rows)} proposed ontology change(s) -> {args.tsv}; "
        f"reports in {args.report_dir}: {by_ont}"
    )


if __name__ == "__main__":
    main()
