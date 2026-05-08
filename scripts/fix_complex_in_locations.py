#!/usr/bin/env python3
"""Fix complex terms incorrectly placed in `locations` instead of `in_complex`.

Pattern 1: Remove from locations when in_complex already has the same term.
Pattern 2: Move to in_complex when no conflict exists.
Skips edge cases (viral terms, multiple complexes, root terms).

Uses ruamel.yaml to preserve formatting (block scalars, comments, etc).

Usage:
    uv run python scripts/fix_complex_in_locations.py --dry-run
    uv run python scripts/fix_complex_in_locations.py
"""

import sqlite3
import sys
from pathlib import Path

from ruamel.yaml import YAML

yaml_rt = YAML()
yaml_rt.preserve_quotes = True
yaml_rt.width = 80
yaml_rt.best_map_representor = True

# For dry-run analysis only
import yaml as pyyaml

GO_DB = Path.home() / ".data/oaklib/go.db"
COMPLEX_ROOT = "GO:0032991"

# Edge cases to skip entirely
SKIP_TERMS = {
    "GO:0055036",  # virion membrane - not a complex
    "GO:0019028",  # viral capsid - not a complex
    "GO:0032991",  # root term - too general
}

# Files with known multi-complex edge cases to skip
SKIP_FILES = {
    "genes/human/ACTB/ACTB-ai-review.yaml",  # cf[2] has 2 complex terms in locations
    "genes/human/GLRX5/GLRX5-ai-review.yaml",  # 2 different complex terms, in_complex already set to one
}


def get_complex_terms(db_path: Path) -> set[str]:
    """Get all terms that are IS-A protein-containing complex."""
    db = sqlite3.connect(str(db_path))
    rows = db.execute(
        "SELECT DISTINCT subject FROM entailed_edge "
        "WHERE predicate = 'rdfs:subClassOf' AND object = ?",
        (COMPLEX_ROOT,),
    ).fetchall()
    db.close()
    return {r[0] for r in rows}


def analyze_file(filepath: Path, complex_terms: set[str]) -> list[dict]:
    """Analyze a file and return planned changes (without modifying it)."""
    changes = []

    try:
        with open(filepath) as f:
            data = pyyaml.safe_load(f)
    except pyyaml.YAMLError:
        return [{"type": "skip", "msg": "YAML parse error"}]

    if not data or "core_functions" not in data or not data["core_functions"]:
        return changes

    for i, cf in enumerate(data["core_functions"]):
        locations = cf.get("locations")
        if not locations or not isinstance(locations, list):
            continue

        existing_in_complex = cf.get("in_complex")

        complex_locs = []
        non_complex_locs = []
        for loc in locations:
            if isinstance(loc, dict) and loc.get("id") in complex_terms:
                complex_locs.append(loc)
            else:
                non_complex_locs.append(loc)

        if not complex_locs:
            continue

        # Filter skip terms
        filtered = []
        for cl in complex_locs:
            if cl.get("id") in SKIP_TERMS:
                changes.append({"type": "skip", "msg": f"cf[{i}]: {cl['id']} ({cl.get('label','?')}) - edge case term"})
            else:
                filtered.append(cl)
        complex_locs = filtered

        if not complex_locs:
            continue

        if len(complex_locs) > 1:
            changes.append({"type": "skip", "msg": f"cf[{i}]: multiple complex terms: {[c['id'] for c in complex_locs]}"})
            continue

        complex_loc = complex_locs[0]
        term_id = complex_loc["id"]
        term_label = complex_loc.get("label", "?")

        if existing_in_complex:
            existing_id = existing_in_complex.get("id") if isinstance(existing_in_complex, dict) else None
            if existing_id == term_id:
                changes.append({"type": "remove", "cf_idx": i, "term_id": term_id, "term_label": term_label})
            else:
                changes.append({"type": "skip", "msg": f"cf[{i}]: in_complex={existing_id}, can't move {term_id}"})
        else:
            changes.append({"type": "move", "cf_idx": i, "term_id": term_id, "term_label": term_label})

    return changes


def apply_changes(filepath: Path, changes: list[dict]):
    """Apply changes to a file using ruamel.yaml to preserve formatting."""
    with open(filepath) as f:
        data = yaml_rt.load(f)

    for change in changes:
        if change["type"] not in ("move", "remove"):
            continue

        i = change["cf_idx"]
        term_id = change["term_id"]
        cf = data["core_functions"][i]
        locations = cf.get("locations", [])

        # Find and remove the complex term from locations
        new_locations = [loc for loc in locations if not (hasattr(loc, 'get') and loc.get("id") == term_id)]

        if change["type"] == "move":
            # Find the complex term dict to move
            complex_loc = next(loc for loc in locations if hasattr(loc, 'get') and loc.get("id") == term_id)
            cf["in_complex"] = complex_loc

        # Update locations
        if new_locations:
            cf["locations"] = new_locations
        else:
            del cf["locations"]

    with open(filepath, "w") as f:
        yaml_rt.dump(data, f)


def main():
    dry_run = "--dry-run" in sys.argv

    if not GO_DB.exists():
        print(f"ERROR: GO database not found at {GO_DB}")
        sys.exit(1)

    complex_terms = get_complex_terms(GO_DB)
    print(f"Loaded {len(complex_terms)} protein-containing complex terms")

    genes_dir = Path("genes")
    review_files = sorted(genes_dir.rglob("*-ai-review.yaml"))
    print(f"Found {len(review_files)} review files")

    if dry_run:
        print("\n=== DRY RUN ===\n")

    total_fixes = 0
    total_skips = 0
    for filepath in review_files:
        rel = str(filepath)
        if rel in SKIP_FILES:
            print(f"{rel}: SKIPPED (edge case file)")
            total_skips += 1
            continue

        changes = analyze_file(filepath, complex_terms)
        if not changes:
            continue

        actionable = [c for c in changes if c["type"] in ("move", "remove")]
        skips = [c for c in changes if c["type"] == "skip"]

        if actionable or skips:
            print(f"{rel}:")

        for c in skips:
            print(f"  SKIP {c['msg']}")
            total_skips += 1

        for c in actionable:
            if c["type"] == "move":
                print(f"  MOVE cf[{c['cf_idx']}].locations -> in_complex: {c['term_id']} ({c['term_label']})")
            elif c["type"] == "remove":
                print(f"  REMOVE cf[{c['cf_idx']}].locations: {c['term_id']} ({c['term_label']}) [duplicate of in_complex]")
            total_fixes += 1

        if actionable and not dry_run:
            apply_changes(filepath, changes)
            print("  WRITTEN")

    print(f"\nTotal fixes: {total_fixes}, Total skips: {total_skips}")
    if dry_run:
        print("(dry run - no files modified)")


if __name__ == "__main__":
    main()
