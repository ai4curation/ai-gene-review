#!/usr/bin/env python3
"""Remove root GO terms from core_functions fields.

Root terms (GO:0003674, GO:0005575, GO:0008150) are uninformative placeholders
excluded from the dynamic enum expansions. This script removes them.

Usage:
    uv run python scripts/fix_root_terms.py --dry-run
    uv run python scripts/fix_root_terms.py
"""

import sys
from pathlib import Path

from ruamel.yaml import YAML

import yaml as pyyaml

yaml_rt = YAML()
yaml_rt.preserve_quotes = True
yaml_rt.width = 80

ROOT_TERMS = {"GO:0003674", "GO:0005575", "GO:0008150"}

# Fields where root terms appear and how to fix them
SINGLE_FIELDS = {"molecular_function", "contributes_to_molecular_function"}
LIST_FIELDS = {"directly_involved_in", "locations"}


def analyze_file(filepath: Path) -> list[dict]:
    """Analyze a file for root terms in core_functions."""
    changes = []
    try:
        with open(filepath) as f:
            data = pyyaml.safe_load(f)
    except pyyaml.YAMLError:
        return []

    if not data or "core_functions" not in data or not data["core_functions"]:
        return []

    for i, cf in enumerate(data["core_functions"]):
        for field in SINGLE_FIELDS:
            val = cf.get(field)
            if isinstance(val, dict) and val.get("id") in ROOT_TERMS:
                changes.append({
                    "type": "remove_single",
                    "cf_idx": i,
                    "field": field,
                    "term_id": val["id"],
                    "term_label": val.get("label", "?"),
                })

        for field in LIST_FIELDS:
            vals = cf.get(field)
            if not isinstance(vals, list):
                continue
            for j, val in enumerate(vals):
                if isinstance(val, dict) and val.get("id") in ROOT_TERMS:
                    changes.append({
                        "type": "remove_from_list",
                        "cf_idx": i,
                        "field": field,
                        "list_idx": j,
                        "term_id": val["id"],
                        "term_label": val.get("label", "?"),
                    })

    return changes


def apply_changes(filepath: Path, changes: list[dict]):
    """Apply changes using ruamel.yaml."""
    with open(filepath) as f:
        data = yaml_rt.load(f)

    for change in changes:
        i = change["cf_idx"]
        cf = data["core_functions"][i]

        if change["type"] == "remove_single":
            field = change["field"]
            if field in cf:
                del cf[field]

        elif change["type"] == "remove_from_list":
            field = change["field"]
            term_id = change["term_id"]
            if field in cf and isinstance(cf[field], list):
                cf[field] = [v for v in cf[field] if not (hasattr(v, 'get') and v.get("id") == term_id)]
                if not cf[field]:
                    del cf[field]

    with open(filepath, "w") as f:
        yaml_rt.dump(data, f)


def main():
    dry_run = "--dry-run" in sys.argv

    genes_dir = Path("genes")
    review_files = sorted(genes_dir.rglob("*-ai-review.yaml"))
    print(f"Found {len(review_files)} review files")

    if dry_run:
        print("\n=== DRY RUN ===\n")

    total_fixes = 0
    for filepath in review_files:
        changes = analyze_file(filepath)
        if not changes:
            continue

        print(f"{filepath}:")
        for c in changes:
            if c["type"] == "remove_single":
                print(f"  REMOVE cf[{c['cf_idx']}].{c['field']}: {c['term_id']} ({c['term_label']})")
            elif c["type"] == "remove_from_list":
                print(f"  REMOVE cf[{c['cf_idx']}].{c['field']}[{c['list_idx']}]: {c['term_id']} ({c['term_label']})")
            total_fixes += 1

        if not dry_run:
            apply_changes(filepath, changes)
            print("  WRITTEN")

    print(f"\nTotal fixes: {total_fixes}")
    if dry_run:
        print("(dry run - no files modified)")


if __name__ == "__main__":
    main()
