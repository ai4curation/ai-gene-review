#!/usr/bin/env python3
"""Apply AUTOFIX supporting_text corrections from the extraction report.

Only applies fixes where similarity >= 0.95 AND the fix is safe:
- The best_match is a real substring of the publication
- We replace the old supporting_text with the best_match

Usage:
    uv run python scripts/fix_supporting_text_autofix.py --dry-run
    uv run python scripts/fix_supporting_text_autofix.py
"""

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

from ruamel.yaml import YAML

yaml_rt = YAML()
yaml_rt.preserve_quotes = True
yaml_rt.width = 80

SIMILARITY_THRESHOLD = 0.95


def clean_best_match(text: str) -> str:
    """Strip markdown artifacts from best_match."""
    if text.startswith("# "):
        text = text[2:]
    return text.strip()


def is_safe_replacement(old_text: str, new_text: str) -> bool:
    """Check if replacing old with new is safe.

    Safe when old (after stripping editorial brackets/ellipsis) is a
    substring of new, or vice versa. This catches truncation, bracket
    artifacts, and minor suffix diffs — but rejects cases where the
    best_match is a completely different sentence.
    """
    def normalize(t):
        t = re.sub(r"\[.*?\]", " ", t)
        t = re.sub(r"\.{2,}", " ", t)
        t = re.sub(r"[^a-zA-Z0-9\s]", " ", t.lower())
        return re.sub(r"\s+", " ", t).strip()

    old_norm = normalize(old_text)
    new_norm = normalize(new_text)
    return old_norm in new_norm or new_norm in old_norm


def load_fixes(report_path: Path) -> dict[str, list[dict]]:
    """Load AUTOFIX entries grouped by file."""
    fixes = defaultdict(list)
    with open(report_path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            if row["status"] != "AUTOFIX":
                continue
            if float(row["similarity"]) < SIMILARITY_THRESHOLD:
                continue
            fixes[row["file"]].append(row)
    return dict(fixes)


def apply_fixes(filepath: Path, fix_rows: list[dict], dry_run: bool) -> int:
    """Apply fixes to a YAML file. Returns number of replacements."""
    with open(filepath) as f:
        data = yaml_rt.load(f)

    replacements = 0

    for row in fix_rows:
        old_text = row["supporting_text"]
        new_text = clean_best_match(row["best_match"])

        if not new_text or old_text == new_text:
            continue

        # Walk the data structure and find the matching supporting_text
        replaced = _replace_in_data(data, old_text, new_text)
        replacements += replaced

    if replacements > 0 and not dry_run:
        with open(filepath, "w") as f:
            yaml_rt.dump(data, f)

    return replacements


def _replace_in_data(data, old_text: str, new_text: str) -> int:
    """Recursively find and replace supporting_text values."""
    count = 0
    if isinstance(data, dict):
        for key in list(data.keys()):
            if key == "supporting_text":
                val = str(data[key]) if data[key] else ""
                if val == old_text:
                    data[key] = new_text
                    count += 1
            else:
                count += _replace_in_data(data[key], old_text, new_text)
    elif isinstance(data, list):
        for item in data:
            count += _replace_in_data(item, old_text, new_text)
    return count


def main():
    dry_run = "--dry-run" in sys.argv
    report_path = Path("reports/supporting-text-fixes.tsv")

    fixes = load_fixes(report_path)
    print(f"Loaded AUTOFIX entries for {len(fixes)} files (>={SIMILARITY_THRESHOLD*100:.0f}%)")

    if dry_run:
        print("\n=== DRY RUN ===\n")

    total = 0
    skipped = 0
    for filepath_str, rows in sorted(fixes.items()):
        filepath = Path(filepath_str)
        gene = filepath.parent.name

        # Show planned changes
        changes = []
        for r in rows:
            old = r["supporting_text"]
            new = clean_best_match(r["best_match"])
            if old == new:
                skipped += 1
                continue
            if not is_safe_replacement(old, new):
                skipped += 1
                continue
            changes.append((old[:60], new[:60], r["similarity"]))

        if not changes:
            continue

        print(f"{gene} ({len(changes)} fixes):")
        for old, new, sim in changes:
            print(f"  [{sim}] '{old}...'")
            print(f"      -> '{new}...'")

        if not dry_run:
            n = apply_fixes(filepath, rows, dry_run)
            print(f"  WRITTEN ({n} replacements)")
            total += n
        else:
            total += len(changes)

    print(f"\nTotal: {total} fixes, {skipped} skipped (identical)")
    if dry_run:
        print("(dry run)")


if __name__ == "__main__":
    main()
