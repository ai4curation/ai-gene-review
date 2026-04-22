#!/usr/bin/env python3
"""Fix malformed reference_id values in gene review YAML files.

Reads the diagnostic report from diagnose_malformed_refs.py and applies
automatable fixes using ruamel.yaml to preserve formatting.

Categories fixed:
- missing_file_prefix_dr: Add file:SPECIES/GENE/ prefix to deep-research refs
- missing_file_prefix_data: Add file:SPECIES/GENE/ prefix to data files
- missing_file_prefix_research: Add file:SPECIES/GENE/ prefix to research refs
- missing_file_prefix_notes: Add file:SPECIES/GENE/ prefix to notes files
- bare_uniprot: Add UniProtKB: prefix
- lowercase_doi: Capitalize doi: to DOI:
- generic_deep_research: Map to actual deep-research file if available
- curator_inference: Leave as-is (will add to skip_prefixes instead)

Usage:
    uv run python scripts/fix_malformed_refs.py --dry-run
    uv run python scripts/fix_malformed_refs.py
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

from ruamel.yaml import YAML

yaml_rt = YAML()
yaml_rt.preserve_quotes = True
yaml_rt.width = 80


AUTOFIX_CATEGORIES = {
    "missing_file_prefix_dr",
    "missing_file_prefix_data",
    "missing_file_prefix_research",
    "missing_file_prefix_notes",
    "bare_uniprot",
    "lowercase_doi",
    "generic_deep_research",
}


def resolve_generic_deep_research(filepath: Path) -> str | None:
    """Find the best deep-research file for a generic 'Deep research' reference."""
    gene_dir = filepath.parent
    candidates = sorted(gene_dir.glob("*deep-research*"))
    if candidates:
        genes_root = None
        for p in filepath.parents:
            if p.name == "genes":
                genes_root = p
                break
        if genes_root:
            rel = candidates[0].relative_to(genes_root)
            return f"file:{rel}"
    return None


def load_fixes(report_path: Path) -> dict[str, list[tuple[str, str, str]]]:
    """Load fixes from diagnostic report, grouped by file."""
    fixes_by_file = defaultdict(list)

    with open(report_path) as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader)  # skip header
        for row in reader:
            if len(row) < 5:
                continue
            filepath, yaml_path, ref_id, category, suggested_fix = row[:5]

            if category not in AUTOFIX_CATEGORIES:
                continue

            if suggested_fix.startswith("LOOKUP_NEEDED:") or suggested_fix.startswith("MANUAL_REVIEW:"):
                continue

            fixes_by_file[filepath].append((ref_id, suggested_fix, category))

    return dict(fixes_by_file)


def apply_fixes_to_data(data, ref_id: str, new_ref_id: str, path="") -> int:
    """Recursively find and fix reference_id values. Returns count of fixes."""
    count = 0
    if isinstance(data, dict):
        for key in list(data.keys()):
            if key in ("source_reference_id", "original_reference_id"):
                continue
            if key == "reference_id" and data[key] == ref_id:
                data[key] = new_ref_id
                count += 1
            else:
                count += apply_fixes_to_data(data[key], ref_id, new_ref_id, path + "." + key)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            count += apply_fixes_to_data(item, ref_id, new_ref_id, path + f"[{i}]")
    return count


def main():
    dry_run = "--dry-run" in sys.argv
    report_path = Path("/tmp/malformed-refs-report.tsv")

    if not report_path.exists():
        print("ERROR: Run diagnose_malformed_refs.py first")
        sys.exit(1)

    fixes_by_file = load_fixes(report_path)
    print(f"Loaded fixes for {len(fixes_by_file)} files")

    if dry_run:
        print("\n=== DRY RUN ===\n")

    total_fixes = 0
    total_skips = 0

    for filepath_str, fixes in sorted(fixes_by_file.items()):
        filepath = Path(filepath_str)

        # Deduplicate: same ref_id -> same fix
        unique_fixes = {}
        for ref_id, new_ref_id, category in fixes:
            if category == "generic_deep_research":
                resolved = resolve_generic_deep_research(filepath)
                if resolved:
                    new_ref_id = resolved
                else:
                    print(f"  SKIP {filepath}: can't resolve generic deep-research")
                    total_skips += 1
                    continue
            unique_fixes[ref_id] = (new_ref_id, category)

        if not unique_fixes:
            continue

        print(f"{filepath}:")
        for ref_id, (new_ref_id, category) in unique_fixes.items():
            count = sum(1 for r, _, _ in fixes if r == ref_id)
            print(f"  {category}: '{ref_id}' -> '{new_ref_id}' ({count}x)")

        if not dry_run:
            with open(filepath) as f:
                data = yaml_rt.load(f)

            file_fixes = 0
            for ref_id, (new_ref_id, _) in unique_fixes.items():
                file_fixes += apply_fixes_to_data(data, ref_id, new_ref_id)

            with open(filepath, "w") as f:
                yaml_rt.dump(data, f)
            print(f"  WRITTEN ({file_fixes} replacements)")
            total_fixes += file_fixes
        else:
            total_fixes += sum(len([r for r, _, _ in fixes if r == ref_id]) for ref_id in unique_fixes)

    print(f"\nTotal fixes: {total_fixes}, Total skips: {total_skips}")
    if dry_run:
        print("(dry run - no files modified)")


if __name__ == "__main__":
    main()
