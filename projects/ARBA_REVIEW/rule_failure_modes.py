#!/usr/bin/env python
"""Derive the rule-level findings table from the ARBA rule reviews.

Reads every ``rules/arba/<ID>/<ID>-review.yaml`` and writes
``rule_failure_modes.yaml``: one row per rule with the review's action and its
structured judgements, and the findings those fields imply. Nothing here is a
new judgement; a finding is present exactly when the review records the field
that defines it (see ``FINDINGS``). Re-run after editing a review::

    uv run python projects/ARBA_REVIEW/rule_failure_modes.py

With ``--table`` it prints the summary table used in ``projects/ARBA_REVIEW.md``.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("rule_failure_modes.yaml")

FINDINGS = {
    "WITHDRAWN": "UniProt no longer serves the rule (rule.withdrawn).",
    "OBSOLETE_CONSEQUENT": "The asserted term is obsolete (annotation_assessments[].consequent_obsolete).",
    "WRONG_PROTEINS": "Named proteins are wrongly annotated (annotation_assessments[].incorrect_examples).",
    "HETEROGENEOUS": "The best curated term of some units lies outside the consequent "
    "(biological_meaning HETEROGENEOUS).",
    "UMBRELLA_TERM": "True, but units carry more specific descendant terms "
    "(biological_meaning TRUE_BUT_UNINFORMATIVE).",
    "EMITS_NOTHING": "Every condition set is covered by a rule for a more specific term "
    "(sets_covered_by_more_specific_rule equals the number of sets).",
    "SETS_DO_NO_WORK": "Some condition sets are redundant or match nothing (parsimony REDUNDANT or OVERLY_COMPLEX).",
    "TAXON_SCOPE": "The taxon restriction does not follow the biology (taxonomic_scope other than APPROPRIATE).",
    "NOT_EXAMINED": "The review reaches no verdict (action UNDECIDED).",
    "NONE": "No finding: accurate, coherent and parsimonious.",
}


def consequent(review: dict[str, Any]) -> str:
    """A short name for what the rule asserts.

    >>> consequent({"rule": {"go_annotations": [{"go_id": "GO:1", "go_label": "x"}]}})
    'GO:1 x'
    """
    rule = review.get("rule") or {}
    go = rule.get("go_annotations") or []
    if go:
        return "; ".join(f"{a.get('go_id')} {a.get('go_label', '')}".strip() for a in go)
    for assessment in review.get("annotation_assessments") or []:
        if assessment.get("value"):
            label = assessment.get("label")
            return f"{assessment['value']} {label}" if label else str(assessment["value"])
    return ""


def findings(review: dict[str, Any]) -> list[str]:
    """The findings a review's structured fields imply.

    >>> findings({"action": "ACCEPT", "biological_meaning": {"assessment": "COHERENT"}})
    ['NONE']
    >>> findings({"action": "SPLIT", "biological_meaning": {"assessment": "TRUE_BUT_UNINFORMATIVE"},
    ...           "parsimony": {"assessment": "REDUNDANT"}})
    ['UMBRELLA_TERM', 'SETS_DO_NO_WORK']
    """
    rule = review.get("rule") or {}
    if rule.get("withdrawn"):
        return ["WITHDRAWN"]
    assessments = review.get("annotation_assessments") or []
    meaning = review.get("biological_meaning") or {}
    total, covered = rule.get("source_condition_set_count"), meaning.get("sets_covered_by_more_specific_rule")
    found = []
    if any(a.get("consequent_obsolete") for a in assessments):
        found.append("OBSOLETE_CONSEQUENT")
    if any(a.get("incorrect_examples") for a in assessments):
        found.append("WRONG_PROTEINS")
    if meaning.get("assessment") == "HETEROGENEOUS":
        found.append("HETEROGENEOUS")
    if meaning.get("assessment") == "TRUE_BUT_UNINFORMATIVE":
        found.append("UMBRELLA_TERM")
    if isinstance(total, int) and isinstance(covered, int) and total > 0 and covered >= total:
        found.append("EMITS_NOTHING")
    elif (review.get("parsimony") or {}).get("assessment") in {"REDUNDANT", "OVERLY_COMPLEX"}:
        found.append("SETS_DO_NO_WORK")
    scope = (review.get("taxonomic_scope") or {}).get("assessment")
    if scope and scope != "APPROPRIATE":
        found.append("TAXON_SCOPE")
    if review.get("action") == "UNDECIDED":
        found.append("NOT_EXAMINED")
    return found or ["NONE"]


def row(review: dict[str, Any]) -> dict[str, Any]:
    """One table row for a review."""
    rule = review.get("rule") or {}
    out: dict[str, Any] = {
        "id": review["id"],
        "action": review.get("action"),
        "consequent": consequent(review),
        "condition_sets": rule.get("source_condition_set_count"),
        "meaning": (review.get("biological_meaning") or {}).get("assessment"),
        "parsimony": (review.get("parsimony") or {}).get("assessment"),
        "taxonomic_scope": (review.get("taxonomic_scope") or {}).get("assessment"),
        "findings": findings(review),
    }
    return {key: value for key, value in out.items() if value is not None}


def load_rows() -> list[dict[str, Any]]:
    """Rows for every committed ARBA rule review."""
    files = sorted((ROOT / "rules" / "arba").glob("*/*-review.yaml"))
    return [row(yaml.safe_load(path.read_text())) for path in files]


def table(rows: list[dict[str, Any]]) -> str:
    """Markdown summary: actions, then findings."""
    actions = Counter(r["action"] for r in rows)
    counts = Counter(f for r in rows for f in r["findings"])
    lines = ["| Action | Rules |", "|---|---:|"]
    lines += [f"| {action} | {n} |" for action, n in actions.most_common()]
    lines += ["", "| Finding | Rules | Defined by |", "|---|---:|---|"]
    lines += [f"| {name} | {counts[name]} | {FINDINGS[name]} |" for name in FINDINGS if counts[name]]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--table", action="store_true", help="print the markdown summary")
    args = parser.parse_args()
    rows = load_rows()
    header = (
        "# Rule-level findings of the ARBA rule reviews in rules/arba/.\n"
        "# Generated by rule_failure_modes.py from the reviews' structured fields; do not edit.\n"
        "# A finding is present exactly when the review records the field that defines it.\n"
        "# Selection caveat: most of these rules were chosen because GO curators had flagged\n"
        "# them, so the distribution describes flagged rules, not ARBA as a whole.\n"
    )
    OUT.write_text(header + yaml.safe_dump({"findings": FINDINGS, "rules": rows}, sort_keys=False, width=110))
    if args.table:
        print(table(rows))


if __name__ == "__main__":
    main()
