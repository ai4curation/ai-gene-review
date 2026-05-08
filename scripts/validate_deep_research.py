#!/usr/bin/env python3
"""Validate provider-named deep research markdown files."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import yaml


PROVIDER_FILE_RE = re.compile(r".+-deep-research-(openai|falcon|perplexity)\.md$")
REQUIRED_FIELDS = ("provider", "start_time", "end_time")
SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
}


def iter_candidate_files(paths: list[Path]) -> list[Path]:
    """Return provider-named deep research files beneath the given paths."""
    candidates: list[Path] = []

    for path in paths:
        if not path.exists():
            continue
        if path.is_file():
            if PROVIDER_FILE_RE.fullmatch(path.name):
                candidates.append(path)
            continue

        for root, dirnames, filenames in os.walk(path):
            dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
            for filename in sorted(filenames):
                if PROVIDER_FILE_RE.fullmatch(filename):
                    candidates.append(Path(root) / filename)

    return sorted(set(candidates))


def parse_frontmatter(path: Path) -> tuple[dict | None, list[str]]:
    """Parse YAML frontmatter from a markdown file."""
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, [f"could not read file: {exc}"]

    lines = content.splitlines()
    if not lines or lines[0] != "---":
        return None, ["missing YAML frontmatter at start of file"]

    end_idx = next((i for i in range(1, len(lines)) if lines[i] == "---"), None)
    if end_idx is None:
        return None, ["frontmatter is not closed with a second --- line"]

    frontmatter_text = "\n".join(lines[1:end_idx])
    try:
        parsed = yaml.safe_load(frontmatter_text) or {}
    except yaml.YAMLError as exc:
        return None, [f"invalid YAML frontmatter: {exc}"]

    if not isinstance(parsed, dict):
        return None, ["frontmatter must parse to a YAML mapping"]

    missing = [field for field in REQUIRED_FIELDS if not parsed.get(field)]
    if missing:
        return parsed, [f"missing required frontmatter field(s): {', '.join(missing)}"]

    return parsed, []


def validate_files(paths: list[Path]) -> int:
    """Validate all matching files and return a process exit code."""
    candidates = iter_candidate_files(paths)
    if not candidates:
        print("No provider-named deep research files found.")
        return 0

    failures: list[tuple[Path, list[str]]] = []
    for path in candidates:
        _, errors = parse_frontmatter(path)
        if errors:
            failures.append((path, errors))

    if failures:
        print(
            f"Deep research validation failed for {len(failures)} of {len(candidates)} file(s):"
        )
        for path, errors in failures:
            print(f"- {path.as_posix()}")
            for error in errors:
                print(f"  - {error}")
        return 1

    print(f"Validated {len(candidates)} provider-named deep research file(s): all passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate provider-named deep research files have required YAML frontmatter."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["genes"],
        help="Files or directories to scan (defaults to genes/).",
    )
    args = parser.parse_args()

    return validate_files([Path(path) for path in args.paths])


if __name__ == "__main__":
    sys.exit(main())
