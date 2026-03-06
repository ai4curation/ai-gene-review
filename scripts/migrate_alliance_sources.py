#!/usr/bin/env python3
"""Migrate 'source: Alliance' to 'source: Alliance_Imported' or 'source: Alliance_Automated'.

Uses source_type (curated → Alliance_Imported, automated → Alliance_Automated)
to determine the new source name. Operates on the raw YAML text to preserve
formatting, reviews, and all other content.

Usage:
    python scripts/migrate_alliance_sources.py [--dry-run]
"""

import re
import sys
from pathlib import Path


def migrate_file(path: Path, dry_run: bool = False) -> bool:
    """Migrate Alliance source names in a single descriptions YAML file.

    Returns True if the file was modified.
    """
    text = path.read_text(encoding="utf-8")
    if "source: Alliance\n" not in text:
        return False

    # Strategy: find each "- source: Alliance\n" and look for the
    # source_type line within the same description block to decide the name.
    # A description block starts with "- source:" and ends at the next
    # "- source:" or end of file.

    lines = text.split("\n")
    modified = False

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped in ("source: Alliance", "- source: Alliance"):
            # Find source_type in the next ~20 lines (within same block)
            source_type = None
            for j in range(i + 1, min(i + 30, len(lines))):
                sj = lines[j].lstrip()
                if sj.startswith("source_type:"):
                    source_type = sj.split(":", 1)[1].strip()
                    break
                # Stop if we hit the next description entry
                if sj.startswith("- source:"):
                    break

            if source_type == "curated":
                new_source = "Alliance_Imported"
            elif source_type == "automated":
                new_source = "Alliance_Automated"
            else:
                print(f"  WARNING: {path}:{i+1} has source: Alliance with unknown source_type={source_type!r}, skipping")
                continue

            lines[i] = line.replace("source: Alliance", f"source: {new_source}")
            modified = True

    if modified:
        new_text = "\n".join(lines)
        if dry_run:
            print(f"  WOULD update: {path}")
        else:
            path.write_text(new_text, encoding="utf-8")
            print(f"  Updated: {path}")

    return modified


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN - no files will be modified\n")

    base = Path(__file__).resolve().parent.parent
    genes_dir = base / "genes"

    # Find all *-descriptions.yaml files
    desc_files = sorted(genes_dir.glob("**/*-descriptions.yaml"))
    print(f"Found {len(desc_files)} description files")

    modified_count = 0
    for f in desc_files:
        if migrate_file(f, dry_run=dry_run):
            modified_count += 1

    print(f"\n{'Would modify' if dry_run else 'Modified'} {modified_count} files")


if __name__ == "__main__":
    main()
