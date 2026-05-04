"""Render an interactive Proteostasis Network mapping tree browser."""

from __future__ import annotations

import argparse
import csv
import json
import os
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


DEFAULT_COVERAGE_PATH = Path(
    "projects/PROTEOSTASIS/reports/pn_mapping_coverage/pn_mapping_code_coverage.tsv"
)
DEFAULT_PROJECTION_PATH = Path(
    "projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv"
)
DEFAULT_AUDIT_PATH = Path(
    "projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv"
)
DEFAULT_MAPPING_DIR = Path("projects/PROTEOSTASIS/mappings")
DEFAULT_OUTPUT_PATH = Path("projects/PROTEOSTASIS/pn.html")
PROJECT_PAGE_PATH = Path("pages/projects/PROTEOSTASIS.html")
UNUSUAL_PROPAGATIONS_PATH = Path(
    "projects/PROTEOSTASIS/reports/pn_mapping_audit/unusual_propagations.tsv"
)

LEVELS = ("branch", "class", "group", "type", "subtype")
CANDIDATE_STATUSES = {
    "more_specific_than_existing_goa",
    "supported_by_goa_regulation",
    "new_to_goa",
}
STATUS_LABELS = {
    "mapped": "Mapped",
    "no_mapping": "No mapping",
    "deferred": "Deferred",
    "pending_review": "Pending review",
    "uncovered": "Uncovered",
    "mapped_and_unmapped": "Conflict",
}
UNMAPPED_STATUS_LABELS = {
    "no_mapping_appropriate": "No mapping appropriate",
    "deferred": "Deferred",
    "pending_review": "Pending review",
}


def load_tsv(path: Path) -> list[dict[str, str]]:
    """Load a tab-separated report file."""
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def prefixes(code: str) -> list[str]:
    """Return path prefixes for a PN source code."""
    parts = [part for part in code.split("|") if part]
    return ["|".join(parts[:index]) for index in range(1, len(parts) + 1)]


def split_semicolon(value: str) -> list[str]:
    """Split semicolon-separated report values."""
    return [part.strip() for part in value.split(";") if part.strip()]


def format_conditions(raw_conditions: Any) -> str:
    """Render mapping condition objects as a compact string."""
    if not raw_conditions:
        return ""
    return "; ".join(
        f"{condition.get('condition_level', '')}={condition.get('condition_code', '')}"
        for condition in raw_conditions
    )


def load_curation_entries(mapping_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Load direct mapping and explicit-unmapped entries from branch YAML files."""
    mapping_entries: list[dict[str, Any]] = []
    unmapped_entries: list[dict[str, Any]] = []

    for path in sorted(mapping_dir.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for entry in data.get("mappings", []):
            target_term = entry.get("target_term") or {}
            mapping_entries.append(
                {
                    "mapping_file": path.name,
                    "subject_code": entry.get("subject_code", ""),
                    "subject_level": entry.get("subject_level", ""),
                    "mapping_scope": entry.get("mapping_scope", ""),
                    "target_go_id": target_term.get("id", ""),
                    "target_go_label": target_term.get("label", ""),
                    "representative_genes": entry.get("representative_genes", []) or [],
                    "conditions": format_conditions(entry.get("conditions")),
                    "rationale": entry.get("rationale", ""),
                    "notes": entry.get("notes", ""),
                    "references": entry.get("references", []) or [],
                }
            )
        for entry in data.get("unmapped_subjects", []):
            unmapped_entries.append(
                {
                    "mapping_file": path.name,
                    "subject_code": entry.get("subject_code", ""),
                    "subject_level": entry.get("subject_level", ""),
                    "unmapped_status": entry.get("unmapped_status", ""),
                    "conditions": format_conditions(entry.get("conditions")),
                    "rationale": entry.get("rationale", ""),
                    "notes": entry.get("notes", ""),
                    "references": entry.get("references", []) or [],
                }
            )

    return mapping_entries, unmapped_entries


def build_data(
    coverage_rows: list[dict[str, str]],
    projection_rows: list[dict[str, str]],
    audit_rows: list[dict[str, str]],
    mapping_dir: Path = DEFAULT_MAPPING_DIR,
) -> dict[str, Any]:
    """Build browser data from PN reports."""
    nodes: dict[str, dict[str, Any]] = {}
    children: dict[str, list[str]] = defaultdict(list)
    mapping_entries, unmapped_entries = load_curation_entries(mapping_dir)
    mappings_by_subject = defaultdict(list)
    unmapped_by_subject = defaultdict(list)
    for entry in mapping_entries:
        mappings_by_subject[(entry["mapping_file"], entry["subject_level"], entry["subject_code"])].append(
            entry
        )
    for entry in unmapped_entries:
        unmapped_by_subject[
            (entry["mapping_file"], entry["subject_level"], entry["subject_code"])
        ].append(entry)

    for row in coverage_rows:
        code = row["code"]
        path = code.split("|")
        parent = "|".join(path[:-1])
        nodes[code] = {
            "id": code,
            "label": path[-1],
            "path": path,
            "level": row["level"],
            "status": row["status"],
            "status_label": STATUS_LABELS.get(row["status"], row["status"]),
            "mapping_files": split_semicolon(row["mapping_files"]),
            "mapping_subjects": split_semicolon(row["mapping_subjects"]),
            "unmapped_files": split_semicolon(row["unmapped_files"]),
            "unmapped_subjects": split_semicolon(row["unmapped_subjects"]),
            "direct_mappings": [],
            "direct_unmapped": [],
            "direct_mapping_scopes": [],
            "projection_rows": 0,
            "projected_gene_count": 0,
            "projected_gene_go_count": 0,
            "candidate_gene_go_count": 0,
            "goa_status_counts": {},
            "audit_count": 0,
            "manual_review_count": 0,
            "scrutiny_decision_counts": {},
            "target_terms": [],
            "gene_examples": [],
            "children": [],
        }
        for file_name in nodes[code]["mapping_files"]:
            for subject_code in nodes[code]["mapping_subjects"]:
                nodes[code]["direct_mappings"].extend(
                    mappings_by_subject.get((file_name, row["level"], subject_code), [])
                )
        for file_name in nodes[code]["unmapped_files"]:
            for subject_code in nodes[code]["unmapped_subjects"]:
                nodes[code]["direct_unmapped"].extend(
                    unmapped_by_subject.get((file_name, row["level"], subject_code), [])
                )
        nodes[code]["direct_mapping_scopes"] = sorted(
            {entry["mapping_scope"] for entry in nodes[code]["direct_mappings"]}
        )
        children[parent].append(code)

    node_gene_sets: dict[str, set[str]] = defaultdict(set)
    node_gene_go_sets: dict[str, set[tuple[str, str]]] = defaultdict(set)
    node_candidate_sets: dict[str, set[tuple[str, str]]] = defaultdict(set)
    node_goa_counts: dict[str, Counter[str]] = defaultdict(Counter)
    node_target_counts: dict[str, Counter[str]] = defaultdict(Counter)
    node_gene_examples: dict[str, set[str]] = defaultdict(set)

    compact_projection_rows: list[dict[str, str]] = []
    for row in projection_rows:
        compact_projection_rows.append(
            {
                "gene_symbol": row["gene_symbol"],
                "gene_name": row["gene_name"],
                "pn_code": row["pn_code"],
                "target_go_id": row["target_go_id"],
                "target_go_label": row["target_go_label"],
                "goa_status": row["goa_status"],
                "mapping_scope": row["mapping_scope"],
                "mapping_subject_code": row["mapping_subject_code"],
            }
        )
        gene_symbol = row["gene_symbol"]
        go_id = row["target_go_id"]
        go_label = row["target_go_label"]
        goa_status = row["goa_status"]
        for prefix in prefixes(row["pn_code"]):
            if prefix not in nodes:
                continue
            nodes[prefix]["projection_rows"] += 1
            if gene_symbol:
                node_gene_sets[prefix].add(gene_symbol)
                if len(node_gene_examples[prefix]) < 50:
                    node_gene_examples[prefix].add(gene_symbol)
            if gene_symbol and go_id:
                node_gene_go_sets[prefix].add((gene_symbol, go_id))
                if goa_status in CANDIDATE_STATUSES:
                    node_candidate_sets[prefix].add((gene_symbol, go_id))
            if goa_status:
                node_goa_counts[prefix][goa_status] += 1
            if go_id:
                node_target_counts[prefix][f"{go_id} {go_label}".strip()] += 1

    compact_audit_rows: list[dict[str, str]] = []
    for row in audit_rows:
        subject_code = row["subject_code"]
        attached_code = ""
        if subject_code in nodes:
            attached_code = subject_code
        else:
            matches = [
                code
                for code, node in nodes.items()
                if node["level"] == row["subject_level"]
                and subject_code in node["mapping_subjects"]
                and row["mapping_file"] in node["mapping_files"]
            ]
            if len(matches) == 1:
                attached_code = matches[0]

        compact_audit_rows.append(
            {
                "attached_code": attached_code,
                "mapping_file": row["mapping_file"],
                "subject_level": row["subject_level"],
                "subject_code": subject_code,
                "mapping_scope": row["mapping_scope"],
                "target_go_id": row["target_go_id"],
                "target_go_label": row["target_go_label"],
                "target_aspect": row["target_aspect"],
                "flags": row["flags"],
                "scrutiny_decision": row["scrutiny_decision"],
                "rationale": row["rationale"],
            }
        )

        if not attached_code:
            continue
        for prefix in prefixes(attached_code):
            if prefix not in nodes:
                continue
            nodes[prefix]["audit_count"] += 1
            if row["scrutiny_decision"] == "manual_gene_level_review_required_before_gene_review_change":
                nodes[prefix]["manual_review_count"] += 1
            counts = Counter(nodes[prefix]["scrutiny_decision_counts"])
            counts[row["scrutiny_decision"]] += 1
            nodes[prefix]["scrutiny_decision_counts"] = dict(counts)

    for code, node in nodes.items():
        node["projected_gene_count"] = len(node_gene_sets[code])
        node["projected_gene_go_count"] = len(node_gene_go_sets[code])
        node["candidate_gene_go_count"] = len(node_candidate_sets[code])
        node["goa_status_counts"] = dict(node_goa_counts[code])
        node["target_terms"] = [
            {"term": term, "count": count}
            for term, count in node_target_counts[code].most_common(12)
        ]
        node["gene_examples"] = sorted(node_gene_examples[code])[:50]

    for parent, child_codes in children.items():
        child_codes.sort(key=lambda code: nodes[code]["label"].lower())
        if parent in nodes:
            nodes[parent]["children"] = child_codes

    subtree_counts: dict[str, Counter[str]] = {}

    def summarize_subtree(code: str) -> Counter[str]:
        node = nodes[code]
        counts = Counter({node["status"]: 1})
        leaf_count = 0 if node["children"] else 1
        for child_code in node["children"]:
            counts.update(summarize_subtree(child_code))
            leaf_count += nodes[child_code]["subtree_leaf_codes"]
        subtree_counts[code] = counts
        node["subtree_status_counts"] = dict(counts)
        node["subtree_total_codes"] = sum(counts.values())
        node["subtree_leaf_codes"] = leaf_count
        return counts

    root_codes = sorted(children[""], key=lambda code: nodes[code]["label"].lower())
    for root_code in root_codes:
        summarize_subtree(root_code)

    def public_tree(code: str) -> dict[str, Any]:
        node = dict(nodes[code])
        node["children"] = [public_tree(child_code) for child_code in nodes[code]["children"]]
        return node

    status_counts = Counter(row["status"] for row in coverage_rows)
    level_counts = Counter(row["level"] for row in coverage_rows)
    leaf_code_count = sum(1 for node in nodes.values() if not node["children"])
    projection_status_counts = Counter(row["goa_status"] for row in projection_rows)
    audit_decision_counts = Counter(row["scrutiny_decision"] for row in audit_rows)
    mapping_scope_counts = Counter(entry["mapping_scope"] for entry in mapping_entries)
    unmapped_status_counts = Counter(entry["unmapped_status"] for entry in unmapped_entries)

    return {
        "generated_from": {
            "coverage": str(DEFAULT_COVERAGE_PATH),
            "projection": str(DEFAULT_PROJECTION_PATH),
            "audit": str(DEFAULT_AUDIT_PATH),
            "mappings": str(mapping_dir),
        },
        "summary": {
            "total_codes": len(coverage_rows),
            "leaf_codes": leaf_code_count,
            "status_counts": dict(status_counts),
            "level_counts": dict(level_counts),
            "projection_rows": len(projection_rows),
            "unique_projected_gene_go_pairs": len(
                {
                    (row["gene_symbol"], row["target_go_id"])
                    for row in projection_rows
                    if row["gene_symbol"] and row["target_go_id"]
                }
            ),
            "candidate_gene_go_pairs": len(
                {
                    (row["gene_symbol"], row["target_go_id"])
                    for row in projection_rows
                    if row["gene_symbol"]
                    and row["target_go_id"]
                    and row["goa_status"] in CANDIDATE_STATUSES
                }
            ),
            "projection_status_counts": dict(projection_status_counts),
            "mapping_scope_counts": dict(mapping_scope_counts),
            "mapping_entries": len(mapping_entries),
            "unmapped_entries": len(unmapped_entries),
            "unmapped_status_counts": dict(unmapped_status_counts),
            "audit_rows": len(audit_rows),
            "audit_decision_counts": dict(audit_decision_counts),
        },
        "root_codes": root_codes,
        "tree": [public_tree(code) for code in root_codes],
        "nodes": nodes,
        "projection_rows": compact_projection_rows,
        "audit_rows": compact_audit_rows,
    }


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Human Proteostasis Network Tree Browser</title>
  <style>
    :root {
      --bg: #f8fafc;
      --panel: #ffffff;
      --ink: #172033;
      --muted: #637083;
      --line: #d6deea;
      --mapped: #1f7a52;
      --deferred: #9a6700;
      --uncovered: #b42318;
      --conflict: #7a3db8;
      --accent: #2468b4;
      --soft-blue: #e8f1fb;
      --soft-green: #e7f5ee;
      --soft-amber: #fff6dc;
      --soft-red: #fdecec;
      --shadow: 0 12px 28px rgba(32, 45, 66, 0.08);
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--ink);
    }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }
    header {
      background: #ffffff;
      border-bottom: 1px solid var(--line);
      padding: 18px 24px 14px;
    }
    .title-row {
      align-items: baseline;
      display: flex;
      flex-wrap: wrap;
      gap: 10px 18px;
      justify-content: space-between;
    }
    h1 {
      font-size: 24px;
      line-height: 1.2;
      margin: 0;
      letter-spacing: 0;
    }
    .nav-links {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      font-size: 14px;
    }
    .summary {
      display: grid;
      gap: 10px;
      grid-template-columns: repeat(6, minmax(120px, 1fr));
      margin-top: 16px;
    }
    .metric {
      background: var(--bg);
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 10px 12px;
    }
    .metric strong { display: block; font-size: 20px; line-height: 1.1; }
    .metric span { color: var(--muted); display: block; font-size: 12px; margin-top: 4px; }
    .help-panel {
      background: var(--bg);
      border: 1px solid var(--line);
      border-radius: 8px;
      margin-top: 12px;
      padding: 0 12px;
    }
    .help-panel summary {
      cursor: pointer;
      font-size: 14px;
      font-weight: 600;
      padding: 10px 0;
    }
    .help-grid {
      display: grid;
      gap: 14px;
      grid-template-columns: repeat(3, minmax(180px, 1fr));
      padding: 0 0 12px;
    }
    .help-section h2 {
      font-size: 13px;
      margin: 0 0 7px;
    }
    .help-section dl {
      display: grid;
      gap: 5px;
      margin: 0;
    }
    .help-section dt {
      color: var(--ink);
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 12px;
      font-weight: 700;
    }
    .help-section dd {
      color: var(--muted);
      font-size: 12px;
      line-height: 1.35;
      margin: 0 0 6px;
    }
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.95em;
    }
    .toolbar {
      align-items: center;
      background: #ffffff;
      border-bottom: 1px solid var(--line);
      display: grid;
      gap: 10px;
      grid-template-columns: minmax(220px, 1fr) 220px auto auto;
      padding: 12px 24px;
      position: sticky;
      top: 0;
      z-index: 10;
    }
    input, select, button {
      border: 1px solid var(--line);
      border-radius: 6px;
      color: var(--ink);
      font: inherit;
      min-height: 38px;
    }
    input, select {
      background: #ffffff;
      padding: 8px 10px;
      width: 100%;
    }
    button {
      background: var(--soft-blue);
      cursor: pointer;
      padding: 8px 12px;
    }
    button:hover { border-color: var(--accent); }
    .filters {
      align-items: center;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .filters label {
      align-items: center;
      display: inline-flex;
      gap: 5px;
      font-size: 13px;
      white-space: nowrap;
    }
    .filters input { min-height: auto; width: auto; }
    .button-row { display: flex; gap: 8px; justify-content: flex-end; }
    main {
      display: grid;
      gap: 18px;
      grid-template-columns: minmax(380px, 0.48fr) minmax(420px, 0.52fr);
      padding: 18px 24px 24px;
    }
    .panel {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: var(--shadow);
      min-width: 0;
    }
    .panel-header {
      align-items: center;
      border-bottom: 1px solid var(--line);
      display: flex;
      justify-content: space-between;
      padding: 12px 14px;
    }
    .panel-header h2 {
      font-size: 16px;
      margin: 0;
    }
    #tree {
      max-height: calc(100vh - 248px);
      overflow: auto;
      padding: 8px 8px 14px;
    }
    .tree-row {
      align-items: center;
      border-radius: 6px;
      cursor: pointer;
      display: grid;
      gap: 8px;
      grid-template-columns: 24px minmax(0, 1fr) auto;
      min-height: 34px;
      padding: 4px 6px;
    }
    .tree-row:hover { background: #f1f5f9; }
    .tree-row.selected {
      background: #e8f1fb;
      outline: 1px solid #9fc3eb;
    }
    .toggle {
      align-items: center;
      border: 0;
      border-radius: 4px;
      color: var(--muted);
      display: inline-flex;
      height: 24px;
      justify-content: center;
      width: 24px;
    }
    .label {
      min-width: 0;
    }
    .label strong {
      display: block;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .label small {
      color: var(--muted);
      display: block;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .badges {
      align-items: center;
      display: inline-flex;
      flex-wrap: wrap;
      gap: 5px;
      justify-content: flex-end;
    }
    .pill {
      border-radius: 999px;
      display: inline-flex;
      font-size: 12px;
      line-height: 1;
      padding: 5px 7px;
      white-space: nowrap;
    }
    .status-mapped { background: var(--soft-green); color: var(--mapped); }
    .status-no_mapping { background: #e8f7ee; color: #27644d; }
    .status-deferred { background: var(--soft-amber); color: var(--deferred); }
    .status-pending_review { background: #eef2f7; color: #526176; }
    .status-uncovered { background: var(--soft-red); color: var(--uncovered); }
    .status-mapped_and_unmapped { background: #efe7fb; color: var(--conflict); }
    .pill-neutral { background: #eef2f7; color: #526176; }
    .pill-risk { background: #fdecec; color: #9f1d1d; }
    .scope-exact { background: #dff7ea; color: #16633f; }
    .scope-ok_for_propagation_to_go { background: #e8f1fb; color: #1f5d99; }
    .scope-too_broad_to_propagate { background: #fff1d1; color: #835600; }
    .curation-card {
      border: 1px solid var(--line);
      border-radius: 8px;
      display: grid;
      gap: 8px;
      margin: 8px 0;
      padding: 10px 12px;
    }
    .curation-card h4 {
      align-items: center;
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      font-size: 14px;
      margin: 0;
    }
    .kv {
      color: var(--ink);
      font-size: 13px;
      line-height: 1.45;
      overflow-wrap: anywhere;
    }
    .kv strong { color: var(--muted); }
    .detail {
      max-height: calc(100vh - 248px);
      overflow: auto;
      padding: 16px;
    }
    .detail h2 {
      font-size: 22px;
      margin: 0 0 4px;
      overflow-wrap: anywhere;
    }
    .path {
      color: var(--muted);
      font-size: 13px;
      margin-bottom: 14px;
      overflow-wrap: anywhere;
    }
    .detail-grid {
      display: grid;
      gap: 10px;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      margin-bottom: 16px;
    }
    .mini {
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 9px 10px;
    }
    .mini strong { display: block; font-size: 18px; }
    .mini span { color: var(--muted); font-size: 12px; }
    h3 {
      border-top: 1px solid var(--line);
      font-size: 15px;
      margin: 18px 0 8px;
      padding-top: 14px;
    }
    table {
      border-collapse: collapse;
      font-size: 13px;
      width: 100%;
    }
    th, td {
      border-bottom: 1px solid var(--line);
      padding: 7px 8px;
      text-align: left;
      vertical-align: top;
    }
    th {
      color: var(--muted);
      font-weight: 600;
    }
    td { overflow-wrap: anywhere; }
    .empty {
      color: var(--muted);
      padding: 10px 0;
    }
    .bar-list {
      display: grid;
      gap: 6px;
    }
    .bar-row {
      align-items: center;
      display: grid;
      gap: 8px;
      grid-template-columns: minmax(150px, 1fr) minmax(80px, 0.8fr) 44px;
    }
    .bar {
      background: #eef2f7;
      border-radius: 999px;
      height: 8px;
      overflow: hidden;
    }
    .bar > span {
      background: var(--accent);
      display: block;
      height: 100%;
    }
    @media (max-width: 1050px) {
      .summary { grid-template-columns: repeat(3, minmax(120px, 1fr)); }
      .help-grid { grid-template-columns: 1fr; }
      .toolbar { grid-template-columns: 1fr; }
      .button-row { justify-content: flex-start; }
      main { grid-template-columns: 1fr; }
      #tree, .detail { max-height: none; }
    }
    @media (max-width: 620px) {
      header, .toolbar, main { padding-left: 12px; padding-right: 12px; }
      .summary { grid-template-columns: repeat(2, minmax(120px, 1fr)); }
      .detail-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .tree-row { grid-template-columns: 24px minmax(0, 1fr); }
      .badges { grid-column: 2; justify-content: flex-start; }
    }
  </style>
</head>
<body>
  <header>
    <div class="title-row">
      <h1>Human Proteostasis Network Tree Browser</h1>
      <nav class="nav-links">
        <a href="__PROJECT_PAGE_HREF__">Project page</a>
        <a href="__COVERAGE_HREF__">Coverage TSV</a>
        <a href="__UNUSUAL_PROPAGATIONS_HREF__">Unusual propagation TSV</a>
      </nav>
    </div>
    <section class="summary" id="summary"></section>
    <details class="help-panel">
      <summary>Definitions</summary>
      <div class="help-grid">
        <section class="help-section">
          <h2>Node Curation</h2>
          <dl>
            <dt>mapped</dt>
            <dd>A completed PN-to-GO mapping exists for this source node.</dd>
            <dt>no_mapping</dt>
            <dd>Reviewed and concluded that no GO mapping should be made.</dd>
            <dt>deferred</dt>
            <dd>Reviewed, but needs more evidence, a better GO term, or narrower child-level handling.</dd>
            <dt>pending_review</dt>
            <dd>Tracked for coverage, but not yet manually analyzed in depth.</dd>
            <dt>uncovered</dt>
            <dd>No mapping or unmapped-status record exists for this node.</dd>
          </dl>
        </section>
        <section class="help-section">
          <h2>Mapping Scope</h2>
          <dl>
            <dt>exact</dt>
            <dd>The PN node is a direct semantic match to the GO target.</dd>
            <dt>ok_for_propagation_to_go</dt>
            <dd>The mapping is not exact, but can generate candidate gene-GO annotations for review.</dd>
            <dt>too_broad_to_propagate</dt>
            <dd>Useful context, but unsafe to project as candidate gene annotations.</dd>
          </dl>
        </section>
        <section class="help-section">
          <h2>Projection Status</h2>
          <dl>
            <dt>already_in_goa_exact</dt>
            <dd>The exact GO target is already present in local GOA for the gene.</dd>
            <dt>entailed_by_goa_closure</dt>
            <dd>Local GOA has a more specific descendant, so the projection adds no new term.</dd>
            <dt>more_specific_than_existing_goa</dt>
            <dd>The projection is more specific than an existing broader GOA term.</dd>
            <dt>supported_by_goa_regulation</dt>
            <dd>GOA has a regulation term related to the projected process.</dd>
            <dt>new_to_goa</dt>
            <dd>No exact, closure, or regulation support was found in local GOA.</dd>
            <dt>no_local_goa</dt>
            <dd>No GOA record was available from the configured source, currently <code>~/repos/go-db/db/goa_human.ddb</code>; this is a data-availability state, not biological evidence.</dd>
          </dl>
        </section>
      </div>
    </details>
  </header>

  <section class="toolbar">
    <input id="search" type="search" placeholder="Search PN code, GO term, gene, or mapping file">
    <select id="branch"></select>
    <div class="filters">
      <label><input type="checkbox" value="mapped" checked> Mapped</label>
      <label><input type="checkbox" value="no_mapping" checked> No mapping</label>
      <label><input type="checkbox" value="deferred" checked> Deferred</label>
      <label><input type="checkbox" value="pending_review" checked> Pending</label>
      <label><input type="checkbox" value="uncovered" checked> Uncovered</label>
      <label><input type="checkbox" value="too_broad_to_propagate" checked> Too broad</label>
      <label><input type="checkbox" value="risk" checked> Risk</label>
    </div>
    <div class="button-row">
      <button id="expand">Expand</button>
      <button id="collapse">Collapse</button>
    </div>
  </section>

  <main>
    <section class="panel">
      <div class="panel-header">
        <h2>PN Hierarchy</h2>
        <span id="tree-count" class="pill pill-neutral"></span>
      </div>
      <div id="tree"></div>
    </section>
    <section class="panel">
      <div class="panel-header">
        <h2>Selected Code</h2>
        <span id="selection-status" class="pill pill-neutral"></span>
      </div>
      <div id="detail" class="detail"></div>
    </section>
  </main>

  <script>
    const DATA = __DATA_JSON__;
    const nodeById = new Map();
    const parentById = new Map();
    const expanded = new Set(DATA.root_codes);
    let selectedId = DATA.root_codes[0] || "";

    function indexNode(node, parent = "") {
      nodeById.set(node.id, node);
      parentById.set(node.id, parent);
      for (const child of node.children) indexNode(child, node.id);
    }
    DATA.tree.forEach(node => indexNode(node));

    function escapeHtml(value) {
      return String(value ?? "").replace(/[&<>"']/g, char => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
      }[char]));
    }

    function statusClass(status) {
      return `status-${status || "uncovered"}`;
    }

    function scopeClass(scope) {
      return `scope-${scope || "unknown"}`;
    }

    function subtreeMatch(rowCode, nodeId) {
      return rowCode === nodeId || rowCode.startsWith(`${nodeId}|`);
    }

    function compactNumber(value) {
      return Number(value || 0).toLocaleString();
    }

    function selectedStatuses() {
      return new Set([...document.querySelectorAll(".filters input[type=checkbox]:checked")].map(input => input.value));
    }

    function nodeSearchText(node) {
      return [
        node.id,
        node.level,
        node.status_label,
        node.mapping_files.join(" "),
        node.mapping_subjects.join(" "),
        node.unmapped_files.join(" "),
        node.direct_mapping_scopes.join(" "),
        node.direct_mappings.map(mapping => [
          mapping.target_go_id,
          mapping.target_go_label,
          mapping.rationale,
          mapping.notes,
          mapping.representative_genes.join(" ")
        ].join(" ")).join(" "),
        node.direct_unmapped.map(item => [
          item.unmapped_status,
          item.rationale,
          item.notes
        ].join(" ")).join(" "),
        node.target_terms.map(item => item.term).join(" "),
        node.gene_examples.join(" ")
      ].join(" ").toLowerCase();
    }

    function nodePassesFilters(node, query, statuses, branch) {
      if (branch && node.path[0] !== branch) return false;
      const statusPass = statuses.has(node.status);
      const riskPass = statuses.has("risk") && node.manual_review_count > 0;
      const tooBroadPass = statuses.has("too_broad_to_propagate") && node.direct_mapping_scopes.includes("too_broad_to_propagate");
      if (!statusPass && !riskPass && !tooBroadPass) return false;
      if (!query) return true;
      return nodeSearchText(node).includes(query);
    }

    function visibleTree(node, query, statuses, branch) {
      const childViews = node.children
        .map(child => visibleTree(child, query, statuses, branch))
        .filter(Boolean);
      if (nodePassesFilters(node, query, statuses, branch) || childViews.length) {
        return { node, childViews };
      }
      return null;
    }

    function renderSummary() {
      const summary = DATA.summary;
      const mapped = summary.status_counts.mapped || 0;
      const noMapping = summary.status_counts.no_mapping || 0;
      const deferred = summary.status_counts.deferred || 0;
      const pendingReview = summary.status_counts.pending_review || 0;
      const uncovered = summary.status_counts.uncovered || 0;
      const tooBroad = summary.mapping_scope_counts.too_broad_to_propagate || 0;
      const propagating = (summary.mapping_scope_counts.exact || 0) + (summary.mapping_scope_counts.ok_for_propagation_to_go || 0);
      document.getElementById("summary").innerHTML = [
        ["Total nodes", summary.total_codes],
        ["Leaf nodes", summary.leaf_codes],
        ["Mapped codes", mapped],
        ["No mapping", noMapping],
        ["Deferred", deferred],
        ["Pending review", pendingReview],
        ["Propagating mappings", propagating],
        ["Too broad mappings", tooBroad],
        ["Candidate gene-GO", summary.candidate_gene_go_pairs],
        ["Uncovered", uncovered]
      ].map(([label, value]) => `<div class="metric"><strong>${compactNumber(value)}</strong><span>${escapeHtml(label)}</span></div>`).join("");

      const branchSelect = document.getElementById("branch");
      branchSelect.innerHTML = `<option value="">All branches</option>` + DATA.root_codes
        .map(code => `<option value="${escapeHtml(code)}">${escapeHtml(code)}</option>`)
        .join("");
    }

    function renderTreeRow(view, depth = 0) {
      const node = view.node;
      const isExpanded = expanded.has(node.id);
      const hasChildren = view.childViews.length > 0;
      const indent = depth * 18;
      const risk = node.manual_review_count > 0 ? `<span class="pill pill-risk">${compactNumber(node.manual_review_count)} review</span>` : "";
      const candidate = node.candidate_gene_go_count ? `<span class="pill pill-neutral">${compactNumber(node.candidate_gene_go_count)} cand</span>` : "";
      const genes = node.projected_gene_count ? `<span class="pill pill-neutral">${compactNumber(node.projected_gene_count)} genes</span>` : "";
      const scopes = node.direct_mapping_scopes.map(scope => `<span class="pill ${scopeClass(scope)}">${escapeHtml(scope)}</span>`).join("");
      const row = `
        <div class="tree-row ${selectedId === node.id ? "selected" : ""}" data-id="${escapeHtml(node.id)}" style="padding-left: ${6 + indent}px">
          <span class="toggle">${hasChildren ? (isExpanded ? "v" : ">") : ""}</span>
          <span class="label">
            <strong>${escapeHtml(node.label)}</strong>
            <small>${escapeHtml(node.level)} | ${escapeHtml(node.id)}</small>
          </span>
          <span class="badges">
            <span class="pill ${statusClass(node.status)}">${escapeHtml(node.status_label)}</span>
            ${scopes}${candidate}${genes}${risk}
          </span>
        </div>`;
      if (!isExpanded) return row;
      return row + view.childViews.map(child => renderTreeRow(child, depth + 1)).join("");
    }

    function renderTree() {
      const query = document.getElementById("search").value.trim().toLowerCase();
      const statuses = selectedStatuses();
      const branch = document.getElementById("branch").value;
      if (query) {
        for (const node of nodeById.values()) {
          if (nodeSearchText(node).includes(query)) {
            for (let id = node.id; id; id = parentById.get(id)) expanded.add(id);
          }
        }
      }
      const views = DATA.tree
        .map(node => visibleTree(node, query, statuses, branch))
        .filter(Boolean);
      document.getElementById("tree").innerHTML = views.length
        ? views.map(view => renderTreeRow(view)).join("")
        : `<div class="empty">No matching PN codes.</div>`;
      const visibleCount = document.querySelectorAll(".tree-row").length;
      document.getElementById("tree-count").textContent = `${compactNumber(visibleCount)} visible`;
      document.querySelectorAll(".tree-row").forEach(row => {
        row.addEventListener("click", event => {
          const id = row.dataset.id;
          if (event.target.classList.contains("toggle")) {
            expanded.has(id) ? expanded.delete(id) : expanded.add(id);
          } else {
            selectedId = id;
          }
          render();
        });
      });
    }

    function statusBars(counts) {
      const entries = Object.entries(counts || {}).sort((a, b) => b[1] - a[1]);
      if (!entries.length) return `<div class="empty">No projection statuses.</div>`;
      const max = Math.max(...entries.map(([, count]) => count), 1);
      return `<div class="bar-list">` + entries.map(([label, count]) => `
        <div class="bar-row">
          <span>${escapeHtml(label)}</span>
          <span class="bar"><span style="width: ${(count / max) * 100}%"></span></span>
          <span>${compactNumber(count)}</span>
        </div>`).join("") + `</div>`;
    }

    function rowsForNode(rows, key, nodeId) {
      return rows.filter(row => row[key] && subtreeMatch(row[key], nodeId));
    }

    function auditRowsForNode(nodeId) {
      return DATA.audit_rows.filter(row => row.attached_code && subtreeMatch(row.attached_code, nodeId));
    }

    function renderProjectionTable(rows) {
      if (!rows.length) return `<div class="empty">No projected GO rows in this subtree.</div>`;
      const limited = rows.slice(0, 80);
      return `<table>
        <thead><tr><th>Gene</th><th>PN code</th><th>GO target</th><th>Status</th></tr></thead>
        <tbody>${limited.map(row => `
          <tr>
            <td><strong>${escapeHtml(row.gene_symbol)}</strong><br>${escapeHtml(row.gene_name)}</td>
            <td>${escapeHtml(row.pn_code)}</td>
            <td>${escapeHtml(row.target_go_id)} ${escapeHtml(row.target_go_label)}</td>
            <td>${escapeHtml(row.goa_status)}</td>
          </tr>`).join("")}</tbody>
      </table>${rows.length > limited.length ? `<div class="empty">Showing ${limited.length} of ${rows.length} rows.</div>` : ""}`;
    }

    function renderAuditTable(rows) {
      if (!rows.length) return `<div class="empty">No scrutiny audit rows in this subtree.</div>`;
      const limited = rows.slice(0, 60);
      return `<table>
        <thead><tr><th>Subject</th><th>GO target</th><th>Flags</th><th>Decision</th></tr></thead>
        <tbody>${limited.map(row => `
          <tr>
            <td><strong>${escapeHtml(row.subject_level)}</strong><br>${escapeHtml(row.subject_code)}<br><small>${escapeHtml(row.mapping_file)}</small></td>
            <td>${escapeHtml(row.target_go_id)} ${escapeHtml(row.target_go_label)}</td>
            <td>${escapeHtml(row.flags || "none")}</td>
            <td>${escapeHtml(row.scrutiny_decision)}</td>
          </tr>`).join("")}</tbody>
      </table>${rows.length > limited.length ? `<div class="empty">Showing ${limited.length} of ${rows.length} rows.</div>` : ""}`;
    }

    function renderTargets(node) {
      if (!node.target_terms.length) return `<div class="empty">No projected GO targets.</div>`;
      return `<table>
        <thead><tr><th>GO target</th><th>Rows</th></tr></thead>
        <tbody>${node.target_terms.map(item => `
          <tr><td>${escapeHtml(item.term)}</td><td>${compactNumber(item.count)}</td></tr>`).join("")}</tbody>
      </table>`;
    }

    function listValue(values) {
      return (values || []).length ? values.map(value => escapeHtml(value)).join("; ") : "";
    }

    function statusForUnmapped(status) {
      if (status === "no_mapping_appropriate") return "no_mapping";
      if (status === "deferred") return "deferred";
      return "pending_review";
    }

    function labelForUnmapped(status) {
      if (status === "no_mapping_appropriate") return "No mapping appropriate";
      if (status === "deferred") return "Deferred";
      return "Pending review";
    }

    function renderDirectCuration(node) {
      const mappingCards = (node.direct_mappings || []).map(mapping => `
        <div class="curation-card">
          <h4>
            <span class="pill ${scopeClass(mapping.mapping_scope)}">${escapeHtml(mapping.mapping_scope)}</span>
            ${escapeHtml(mapping.target_go_id)} ${escapeHtml(mapping.target_go_label)}
          </h4>
          <div class="kv"><strong>Subject:</strong> ${escapeHtml(mapping.subject_code)}</div>
          <div class="kv"><strong>File:</strong> ${escapeHtml(mapping.mapping_file)}</div>
          ${mapping.conditions ? `<div class="kv"><strong>Conditions:</strong> ${escapeHtml(mapping.conditions)}</div>` : ""}
          ${mapping.representative_genes?.length ? `<div class="kv"><strong>Representative genes:</strong> ${listValue(mapping.representative_genes)}</div>` : ""}
          ${mapping.rationale ? `<div class="kv"><strong>Rationale:</strong> ${escapeHtml(mapping.rationale)}</div>` : ""}
          ${mapping.notes ? `<div class="kv"><strong>Notes:</strong> ${escapeHtml(mapping.notes)}</div>` : ""}
          ${mapping.references?.length ? `<div class="kv"><strong>References:</strong> ${listValue(mapping.references)}</div>` : ""}
        </div>
      `);
      const unmappedCards = (node.direct_unmapped || []).map(item => `
        <div class="curation-card">
          <h4><span class="pill status-${escapeHtml(statusForUnmapped(item.unmapped_status))}">${escapeHtml(labelForUnmapped(item.unmapped_status))}</span></h4>
          <div class="kv"><strong>Subject:</strong> ${escapeHtml(item.subject_code)}</div>
          <div class="kv"><strong>File:</strong> ${escapeHtml(item.mapping_file)}</div>
          <div class="kv"><strong>Unmapped status:</strong> ${escapeHtml(item.unmapped_status)}</div>
          ${item.conditions ? `<div class="kv"><strong>Conditions:</strong> ${escapeHtml(item.conditions)}</div>` : ""}
          ${item.rationale ? `<div class="kv"><strong>Rationale:</strong> ${escapeHtml(item.rationale)}</div>` : ""}
          ${item.notes ? `<div class="kv"><strong>Notes:</strong> ${escapeHtml(item.notes)}</div>` : ""}
          ${item.references?.length ? `<div class="kv"><strong>References:</strong> ${listValue(item.references)}</div>` : ""}
        </div>
      `);
      const cards = [...mappingCards, ...unmappedCards];
      return cards.length ? cards.join("") : `<div class="empty">No direct curation record on this node.</div>`;
    }

    function renderDetail() {
      const node = nodeById.get(selectedId) || DATA.tree[0];
      if (!node) {
        document.getElementById("detail").innerHTML = `<div class="empty">No PN codes loaded.</div>`;
        return;
      }
      document.getElementById("selection-status").textContent = node.status_label;
      document.getElementById("selection-status").className = `pill ${statusClass(node.status)}`;
      const projectionRows = rowsForNode(DATA.projection_rows, "pn_code", node.id);
      const candidateRows = projectionRows.filter(row => ["more_specific_than_existing_goa", "supported_by_goa_regulation", "new_to_goa"].includes(row.goa_status));
      const auditRows = auditRowsForNode(node.id);
      const mappedCounts = node.subtree_status_counts || {};
      const mappingFiles = [...new Set([...node.mapping_files, ...node.unmapped_files])];
      document.getElementById("detail").innerHTML = `
        <h2>${escapeHtml(node.label)}</h2>
        <div class="path">${escapeHtml(node.id)}</div>
        <div class="badges">
          <span class="pill ${statusClass(node.status)}">${escapeHtml(node.status_label)}</span>
          <span class="pill pill-neutral">${escapeHtml(node.level)}</span>
          ${node.manual_review_count ? `<span class="pill pill-risk">${compactNumber(node.manual_review_count)} manual-review flags</span>` : ""}
        </div>

        <div class="detail-grid">
          <div class="mini"><strong>${compactNumber(node.subtree_total_codes || 1)}</strong><span>codes in subtree</span></div>
          <div class="mini"><strong>${compactNumber(node.subtree_leaf_codes || 0)}</strong><span>leaf nodes in subtree</span></div>
          <div class="mini"><strong>${compactNumber(node.projected_gene_count)}</strong><span>projected genes</span></div>
          <div class="mini"><strong>${compactNumber(node.projected_gene_go_count)}</strong><span>gene-GO pairs</span></div>
          <div class="mini"><strong>${compactNumber(node.candidate_gene_go_count)}</strong><span>candidate pairs</span></div>
        </div>

        <h3>Subtree Coverage</h3>
        <div class="badges">
          <span class="pill status-mapped">${compactNumber(mappedCounts.mapped || 0)} mapped</span>
          <span class="pill status-no_mapping">${compactNumber(mappedCounts.no_mapping || 0)} no mapping</span>
          <span class="pill status-deferred">${compactNumber(mappedCounts.deferred || 0)} deferred</span>
          <span class="pill status-pending_review">${compactNumber(mappedCounts.pending_review || 0)} pending</span>
          <span class="pill status-uncovered">${compactNumber(mappedCounts.uncovered || 0)} uncovered</span>
          ${(mappedCounts.mapped_and_unmapped || 0) ? `<span class="pill status-mapped_and_unmapped">${compactNumber(mappedCounts.mapped_and_unmapped)} conflicts</span>` : ""}
        </div>

        <h3>Mapping Files</h3>
        ${mappingFiles.length ? `<div class="badges">${mappingFiles.map(file => `<span class="pill pill-neutral">${escapeHtml(file)}</span>`).join("")}</div>` : `<div class="empty">No exact mapping or non-map file on this code.</div>`}

        <h3>Direct Curation</h3>
        ${renderDirectCuration(node)}

        <h3>Projection Status</h3>
        ${statusBars(node.goa_status_counts)}

        <h3>Top GO Targets</h3>
        ${renderTargets(node)}

        <h3>Candidate Additions</h3>
        ${renderProjectionTable(candidateRows)}

        <h3>Scrutiny Audit</h3>
        ${renderAuditTable(auditRows)}

        <h3>Projected Rows</h3>
        ${renderProjectionTable(projectionRows)}
      `;
    }

    function render() {
      renderTree();
      renderDetail();
    }

    document.getElementById("search").addEventListener("input", render);
    document.getElementById("branch").addEventListener("change", render);
    document.querySelectorAll(".filters input").forEach(input => input.addEventListener("change", render));
    document.getElementById("expand").addEventListener("click", () => {
      for (const id of nodeById.keys()) expanded.add(id);
      render();
    });
    document.getElementById("collapse").addEventListener("click", () => {
      expanded.clear();
      DATA.root_codes.forEach(id => expanded.add(id));
      render();
    });

    renderSummary();
    render();
  </script>
</body>
</html>
"""


def relative_href(output_path: Path, target_path: Path) -> str:
    """Return a POSIX relative href from an HTML output file to a repo path."""
    return Path(os.path.relpath(target_path, start=output_path.parent)).as_posix()


def render_html(data: dict[str, Any], output_path: Path) -> str:
    """Render a standalone HTML document with embedded browser data."""
    html = HTML_TEMPLATE.replace(
        "__DATA_JSON__",
        json.dumps(data, ensure_ascii=True, separators=(",", ":")),
    )
    return (
        html.replace("__PROJECT_PAGE_HREF__", relative_href(output_path, PROJECT_PAGE_PATH))
        .replace("__COVERAGE_HREF__", relative_href(output_path, DEFAULT_COVERAGE_PATH))
        .replace(
            "__UNUSUAL_PROPAGATIONS_HREF__",
            relative_href(output_path, UNUSUAL_PROPAGATIONS_PATH),
        )
    )


def build_argument_parser() -> argparse.ArgumentParser:
    """Build CLI arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--coverage",
        type=Path,
        default=DEFAULT_COVERAGE_PATH,
        help=f"Coverage TSV path (default: {DEFAULT_COVERAGE_PATH})",
    )
    parser.add_argument(
        "--projection",
        type=Path,
        default=DEFAULT_PROJECTION_PATH,
        help=f"Projection TSV path (default: {DEFAULT_PROJECTION_PATH})",
    )
    parser.add_argument(
        "--audit",
        type=Path,
        default=DEFAULT_AUDIT_PATH,
        help=f"Mapping audit TSV path (default: {DEFAULT_AUDIT_PATH})",
    )
    parser.add_argument(
        "--mapping-dir",
        type=Path,
        default=DEFAULT_MAPPING_DIR,
        help=f"Mapping YAML directory (default: {DEFAULT_MAPPING_DIR})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help=f"Output HTML path (default: {DEFAULT_OUTPUT_PATH})",
    )
    return parser


def main() -> None:
    """Run the tree browser renderer."""
    parser = build_argument_parser()
    args = parser.parse_args()

    data = build_data(
        coverage_rows=load_tsv(args.coverage),
        projection_rows=load_tsv(args.projection),
        audit_rows=load_tsv(args.audit),
        mapping_dir=args.mapping_dir,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_html(data, args.output), encoding="utf-8")
    print(f"Wrote PN tree browser to {args.output}")


if __name__ == "__main__":
    main()
