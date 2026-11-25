#!/usr/bin/env python3
"""Collect structured PAINT change requests from family reviews.

A family review (``interpro/panther/<PTHR>/<PTHR>-review.yaml``) judges PAINT rows in
``node_assessments``. When it disputes one, ``proposed_action`` records the change it
asks PAINT curators to make (``paint_action`` plus, for moves and added losses,
``target_node_id``); ``family_residue_validator`` checks the action against the verdict
and the PANTHER tree. This module flattens every proposed action into one row and
renders one Markdown report per family, which is the unit a PAINT curator works in.

Requests that cannot all be carried out are flagged, not resolved. A PAINT row (node and
term) has one verdict, so two different requests on it conflict, including a move or a
removal next to an added loss: a moved IBD may no longer sit above the loss target. The
one exception is several losses requested below the same IBD, which are independent.

>>> row = _row(
...     "interpro/panther/PTHR1/PTHR1-review.yaml",
...     {"family_id": "PANTHER:PTHR1", "family_name": "F"},
...     {"node_id": "PANTHER:PTN1", "asserted_term": {"id": "GO:1", "label": "t"},
...      "evidence": "IBD", "assessment": "TOO_DEEP",
...      "proposed_action": {"paint_action": "MOVE_IBD", "target_node_id": "PANTHER:PTN2"}},
... )
>>> row["request"]
'Move the IBD of GO:1 (t) from PANTHER:PTN1 to PANTHER:PTN2'
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

COLUMNS = [
    "family_id",
    "family_name",
    "node_id",
    "node_taxon",
    "evidence",
    "paint_snapshot",
    "term_id",
    "term_label",
    "assessment",
    "paint_action",
    "target_node_id",
    "target_node_taxon",
    "request",
    "assessment_reason",
    "supported_by",
    "source_path",
]

DEFAULT_TSV = Path("reports/paint-change-requests.tsv")
DEFAULT_REPORT_DIR = Path("reports/paint-change-requests")


def _label(value: Any) -> str:
    """Return the label of an ``{id, label}`` mapping, or the value itself.

    >>> _label({"id": "NCBITaxon:6072", "label": "Eumetazoa"})
    'Eumetazoa'
    >>> _label(None)
    ''
    """
    if isinstance(value, dict):
        return str(value.get("label") or value.get("id") or "")
    return "" if value is None else str(value)


def describe_request(row: dict[str, str]) -> str:
    """Describe a PAINT change request in one line.

    >>> base = {"paint_action": "", "node_id": "PANTHER:PTN1", "target_node_id": "",
    ...         "term_id": "GO:1", "term_label": "t", "evidence": "IBD"}
    >>> describe_request({**base, "paint_action": "REMOVE_IBD"})
    'Remove the IBD of GO:1 (t) at PANTHER:PTN1'
    >>> describe_request({**base, "paint_action": "ADD_IKR", "target_node_id": "PANTHER:PTN3"})
    'Add an IKR (loss) of GO:1 (t) at PANTHER:PTN3, below the IBD at PANTHER:PTN1'
    >>> describe_request({**base, "paint_action": "MOVE_LOSS", "evidence": "IRD",
    ...                   "target_node_id": "PANTHER:PTN4"})
    'Move the IRD of GO:1 (t) from PANTHER:PTN1 to PANTHER:PTN4'
    >>> describe_request({**base, "paint_action": "REMOVE_LOSS", "evidence": ""})
    'Remove the loss of GO:1 (t) at PANTHER:PTN1'
    """
    term = f"{row['term_id']} ({row['term_label']})" if row["term_label"] else row["term_id"]
    node, target, action = row["node_id"], row["target_node_id"], row["paint_action"]
    evidence = row["evidence"]
    if action == "MOVE_IBD":
        return f"Move the IBD of {term} from {node} to {target}"
    if action == "REMOVE_IBD":
        return f"Remove the IBD of {term} at {node}"
    if action in ("ADD_IRD", "ADD_IKR"):
        code = action.removeprefix("ADD_")
        return f"Add an {code} (loss) of {term} at {target}, below the IBD at {node}"
    loss = evidence if evidence in ("IRD", "IKR") else "loss"
    if action == "REMOVE_LOSS":
        return f"Remove the {loss} of {term} at {node}"
    if action == "MOVE_LOSS":
        return f"Move the {loss} of {term} from {node} to {target}"
    return f"{action} on {term} at {node}"


def _row(source_path: str, family: dict[str, str], assessment: dict[str, Any]) -> dict[str, str]:
    """Flatten one node assessment with a proposed action into a TSV row."""
    action = assessment.get("proposed_action") or {}
    term = assessment.get("asserted_term") or {}
    row = {c: "" for c in COLUMNS}
    row.update(family)
    row.update({
        "node_id": str(assessment.get("node_id") or ""),
        "node_taxon": _label(assessment.get("node_taxon")),
        "evidence": str(assessment.get("evidence") or ""),
        "paint_snapshot": str(assessment.get("paint_snapshot") or ""),
        "term_id": str(term.get("id") or ""),
        "term_label": str(term.get("label") or ""),
        "assessment": str(assessment.get("assessment") or ""),
        "paint_action": str(action.get("paint_action") or ""),
        "target_node_id": str(action.get("target_node_id") or ""),
        "target_node_taxon": _label(action.get("target_node_taxon")),
        "assessment_reason": " ".join(str(assessment.get("assessment_reason") or "").split()),
        "supported_by": json.dumps(assessment.get("supported_by") or [], ensure_ascii=False),
        "source_path": source_path,
    })
    row["request"] = describe_request(row)
    return row


def family_review_rows(path: Path, root: Path) -> Iterator[dict[str, str]]:
    """Yield one row per node assessment that carries a proposed action."""
    text = path.read_text(encoding="utf-8")
    if "proposed_action:" not in text:
        return
    data = YAML(typ="safe").load(text) or {}
    family = {
        "family_id": str(data.get("family_id") or ""),
        "family_name": str(data.get("family_name") or ""),
    }
    for assessment in data.get("node_assessments") or []:
        if assessment.get("proposed_action"):
            yield _row(str(path.relative_to(root)), family, assessment)


def collect(root: Path) -> list[dict[str, str]]:
    """Collect every proposed PAINT action under ``root``, sorted for stable output."""
    rows: list[dict[str, str]] = []
    for path in sorted(root.glob("interpro/panther/*/*-review.yaml")):
        rows.extend(family_review_rows(path, root))
    rows.sort(key=lambda r: (r["family_id"], r["node_id"], r["term_id"], r["paint_action"]))
    return rows


def conflicts(rows: list[dict[str, str]]) -> list[str]:
    """Return requests in the same family that cannot all be carried out.

    A PAINT row (the same node and term) has one verdict, so any two different
    requests on it are flagged, except several added losses (``ADD_IRD``/``ADD_IKR``),
    which prune independent clades below one IBD. A move or removal next to a loss is
    flagged: removing the IBD makes the loss moot, and a moved IBD may no longer sit
    above the loss target (deciding that needs the tree, which this module does not
    load).

    >>> r = {c: "" for c in COLUMNS}
    >>> a = {**r, "family_id": "F", "node_id": "N", "term_id": "GO:1",
    ...      "paint_action": "MOVE_IBD", "target_node_id": "T1"}
    >>> conflicts([a, {**a, "target_node_id": "T1"}])
    []
    >>> conflicts([a, {**a, "paint_action": "REMOVE_IBD", "target_node_id": ""}])
    ['F: N GO:1 has conflicting requests: MOVE_IBD to T1; REMOVE_IBD']
    >>> conflicts([a, {**a, "target_node_id": "T2"}])
    ['F: N GO:1 has conflicting requests: MOVE_IBD to T1; MOVE_IBD to T2']
    >>> conflicts([{**a, "paint_action": "REMOVE_IBD", "target_node_id": ""},
    ...            {**a, "paint_action": "ADD_IKR", "target_node_id": "T3"}])
    ['F: N GO:1 has conflicting requests: ADD_IKR to T3; REMOVE_IBD']
    >>> conflicts([a, {**a, "paint_action": "ADD_IKR", "target_node_id": "T3"}])
    ['F: N GO:1 has conflicting requests: ADD_IKR to T3; MOVE_IBD to T1']
    >>> loss = {**a, "paint_action": "ADD_IKR", "target_node_id": "T3"}
    >>> conflicts([loss, {**loss, "paint_action": "ADD_IRD", "target_node_id": "T4"}])
    []
    """
    requests: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    losses: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for r in rows:
        key = (r["family_id"], r["node_id"], r["term_id"])
        target = f" to {r['target_node_id']}" if r["target_node_id"] else ""
        # Several losses below one IBD are compatible with each other, so they are kept
        # apart; any other request on the row conflicts with them.
        bucket = losses if r["paint_action"].startswith("ADD_") else requests
        bucket[key].add(r["paint_action"] + target)
    problems = []
    for key in sorted(set(requests) | set(losses)):
        found, added = requests.get(key, set()), losses.get(key, set())
        if len(found) > 1 or (found and added):
            fam, node, term = key
            listed = "; ".join(sorted(found | added))
            problems.append(f"{fam}: {node} {term} has conflicting requests: {listed}")
    return problems


def render_report(family_id: str, rows: list[dict[str, str]]) -> str:
    """Render the Markdown change-request report for one family.

    >>> row = {c: "" for c in COLUMNS}
    >>> row.update({"family_id": "PANTHER:PTHR1", "family_name": "F", "node_id": "PANTHER:PTN1",
    ...     "term_id": "GO:1", "assessment": "TOO_DEEP", "paint_action": "REMOVE_IBD",
    ...     "request": "Remove the IBD of GO:1 at PANTHER:PTN1", "assessment_reason": "Why.",
    ...     "supported_by": '[{"reference_id": "PMID:1", "supporting_text": "x"}]',
    ...     "source_path": "p.yaml"})
    >>> md = render_report("PANTHER:PTHR1", [row])
    >>> "## 1. Remove the IBD of GO:1 at PANTHER:PTN1" in md and "> — PMID:1" in md
    True
    """
    name = rows[0]["family_name"] if rows else ""
    title = f"# PAINT change requests for {family_id}" + (f" ({name})" if name else "")
    lines = [
        title,
        "",
        (
            f"{len(rows)} request(s), generated from `node_assessments[].proposed_action` in "
            "this repository's family review. Do not edit by hand. PAINT prunes per "
            "annotation, so each request concerns only the term it names."
        ),
    ]
    problems = conflicts(rows)
    if problems:
        lines += ["", "**Conflicting requests (resolve before filing):**", ""]
        lines += [f"- {p}" for p in problems]
    for i, r in enumerate(rows, 1):
        node = r["node_id"] + (f" ({r['node_taxon']})" if r["node_taxon"] else "")
        lines += ["", f"## {i}. {r['request']}", ""]
        term = f"{r['term_id']} {r['term_label']}" if r["term_label"] else r["term_id"]
        lines.append(f"- **PAINT row:** {r['evidence'] or 'annotation'} of {term} at {node}")
        if r["paint_snapshot"]:
            lines.append(f"- **PAINT snapshot reviewed:** {r['paint_snapshot']}")
        lines.append(f"- **Verdict:** {r['assessment']}")
        lines.append(f"- **Action:** {r['paint_action']}")
        if r["target_node_id"]:
            taxon = f" ({r['target_node_taxon']})" if r["target_node_taxon"] else ""
            lines.append(f"- **Target node:** {r['target_node_id']}{taxon}")
        lines.append(f"- **Recorded in:** `{r['source_path']}`")
        if r["assessment_reason"]:
            lines += ["", r["assessment_reason"]]
        for ev in json.loads(r["supported_by"] or "[]"):
            text = " ".join(str(ev.get("supporting_text") or "").split())
            if text:
                lines += ["", f"> {text}", ">", f"> — {ev.get('reference_id', '')}"]
            else:
                lines += ["", f"- **Evidence reference:** {ev.get('reference_id', '')}"]
    return "\n".join(lines) + "\n"


def _report_name(family_id: str) -> str:
    """Return the report file stem for a family id.

    >>> _report_name("PANTHER:PTHR24416")
    'PTHR24416'
    """
    return family_id.removeprefix("PANTHER:") or "unknown"


def write_outputs(root: Path, tsv: Path, report_dir: Path) -> list[dict[str, str]]:
    """Write the TSV and one Markdown report per family; return the rows."""
    rows = collect(root)
    tsv.parent.mkdir(parents=True, exist_ok=True)
    with tsv.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    report_dir.mkdir(parents=True, exist_ok=True)
    for family_id in sorted({r["family_id"] for r in rows}):
        subset = [r for r in rows if r["family_id"] == family_id]
        (report_dir / f"{_report_name(family_id)}.md").write_text(
            render_report(family_id, subset), encoding="utf-8")
    return rows


def main() -> None:
    """Command-line entry point. Exits 1 if any family has conflicting requests."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--tsv", type=Path, default=DEFAULT_TSV)
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    args = parser.parse_args()
    rows = write_outputs(args.root, args.tsv, args.report_dir)
    families = len({r["family_id"] for r in rows})
    print(f"{len(rows)} PAINT change request(s) in {families} family review(s) -> {args.tsv}; "
          f"reports in {args.report_dir}")
    problems = conflicts(rows)
    for p in problems:
        print(f"CONFLICT: {p}")
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
