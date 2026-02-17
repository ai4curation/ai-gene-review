"""Auto-fix ontology term labels in YAML files using cache.

This script reads YAML files, finds ontology terms with incorrect labels,
and updates them based on the committed cache files. Uses ruamel.yaml
round-trip mode to preserve formatting (multi-line strings, comments, etc.).
"""

from pathlib import Path
from typing import Any, List, Tuple

import pandas as pd
from ruamel.yaml import YAML

# Paths under which proposed replacement terms live — these may contain
# hallucinated GO IDs that are not in the cache and should be skipped by default.
_PROPOSED_PATH_FRAGMENTS = {"proposed_replacement_terms", "proposed_new_terms"}


class LabelFixer:
    """Fix ontology term labels in YAML files."""

    def __init__(self, repo_root: Path, *, skip_proposed: bool = True):
        """Initialize the label fixer.

        Args:
            repo_root: Root directory of the repository
            skip_proposed: If True, skip terms inside proposed_replacement_terms
        """
        self.repo_root = Path(repo_root)
        self.cache_dir = self.repo_root / "cache" / "ontologies"
        self.label_cache: dict[str, str] = {}
        self.skip_proposed = skip_proposed
        self._load_caches()

    def _load_caches(self):
        """Load all ontology caches into memory."""
        if not self.cache_dir.exists():
            print(f"Error: Cache directory not found at {self.cache_dir}")
            print("Run 'just update-cache' first to build the cache.")
            return

        for cache_file in self.cache_dir.glob("*.tsv"):
            df = pd.read_csv(cache_file, sep="\t")
            for _, row in df.iterrows():
                self.label_cache[row["term_id"]] = row["label"]
            print(f"Loaded {len(df)} terms from {cache_file.name}")

        print(f"Total cached terms: {len(self.label_cache)}\n")

    def _should_skip(self, path: str) -> bool:
        """Check whether a path falls under a proposed-terms section."""
        if not self.skip_proposed:
            return False
        return any(frag in path for frag in _PROPOSED_PATH_FRAGMENTS)

    def fix_labels_in_data(
        self, data: Any, path: str = ""
    ) -> List[Tuple[str, str, str, str]]:
        """Recursively fix labels in a ruamel.yaml data structure *in place*.

        Args:
            data: The data structure to fix (CommentedMap / CommentedSeq / scalar)
            path: Current path in the data structure

        Returns:
            List of (path, term_id, old_label, new_label) for each change made
        """
        changes: list[tuple[str, str, str, str]] = []

        if hasattr(data, "items"):  # dict-like (CommentedMap)
            if "id" in data and "label" in data:
                term_id = data["id"]
                if isinstance(term_id, str) and ":" in term_id and not self._should_skip(path):
                    old_label = data["label"]
                    correct_label = self.label_cache.get(term_id)
                    if correct_label and old_label != correct_label:
                        data["label"] = correct_label
                        changes.append((path, term_id, old_label, correct_label))

            for key in data:
                new_path = f"{path}.{key}" if path else str(key)
                changes.extend(self.fix_labels_in_data(data[key], new_path))

        elif isinstance(data, list):
            for i, item in enumerate(data):
                new_path = f"{path}[{i}]"
                changes.extend(self.fix_labels_in_data(item, new_path))

        return changes

    def fix_file(self, yaml_file: Path, dry_run: bool = False) -> int:
        """Fix labels in a single YAML file.

        Args:
            yaml_file: Path to the YAML file
            dry_run: If True, don't write changes, just report them

        Returns:
            Number of changes made
        """
        yml = YAML()
        yml.preserve_quotes = True
        yml.width = 1000  # prevent rewrapping

        with open(yaml_file) as f:
            data = yml.load(f)

        changes = self.fix_labels_in_data(data)

        if changes:
            print(f"\n{yaml_file.relative_to(self.repo_root)}:")
            for path, term_id, old_label, new_label in changes:
                print(f"  {term_id} at {path}")
                print(f"    OLD: {old_label}")
                print(f"    NEW: {new_label}")

            if not dry_run:
                with open(yaml_file, "w") as f:
                    yml.dump(data, f)
                print(f"  Fixed {len(changes)} labels")
            else:
                print(f"  [DRY RUN] Would fix {len(changes)} labels")

        return len(changes)

    def fix_all_files(self, pattern: str = "*-ai-review.yaml", dry_run: bool = False):
        """Fix labels in all matching YAML files.

        Args:
            pattern: Glob pattern for files to fix
            dry_run: If True, don't write changes, just report them
        """
        genes_dir = self.repo_root / "genes"
        yaml_files = list(genes_dir.rglob(pattern))

        if not yaml_files:
            print(f"No files matching pattern '{pattern}' found in {genes_dir}")
            return

        print(f"Found {len(yaml_files)} files to check\n")

        total_changes = 0
        files_changed = 0

        for yaml_file in sorted(yaml_files):
            num_changes = self.fix_file(yaml_file, dry_run=dry_run)
            if num_changes > 0:
                total_changes += num_changes
                files_changed += 1

        print(f"\n{'='*60}")
        if dry_run:
            print(f"[DRY RUN] Would fix {total_changes} labels in {files_changed} files")
        else:
            print(f"Fixed {total_changes} labels in {files_changed} files")
        print(f"{'='*60}")


def main():
    """Main entry point for label fixing."""
    import argparse

    parser = argparse.ArgumentParser(description="Fix ontology term labels in YAML files")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without actually changing it",
    )
    parser.add_argument(
        "--file",
        type=Path,
        help="Fix a specific file instead of all files",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root directory",
    )
    parser.add_argument(
        "--skip-proposed",
        action="store_true",
        default=True,
        help="Skip terms in proposed_replacement_terms (default: True)",
    )
    parser.add_argument(
        "--no-skip-proposed",
        action="store_true",
        help="Also fix terms in proposed_replacement_terms",
    )

    args = parser.parse_args()

    skip_proposed = args.skip_proposed and not args.no_skip_proposed

    fixer = LabelFixer(args.repo_root, skip_proposed=skip_proposed)

    if not fixer.label_cache:
        print("No cache loaded. Exiting.")
        return

    if args.file:
        fixer.fix_file(args.file, dry_run=args.dry_run)
    else:
        fixer.fix_all_files(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
