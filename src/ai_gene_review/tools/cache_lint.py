#!/usr/bin/env python3
"""Guard: the committed term-validator caches must be sorted by CURIE and deduplicated.

``linkml-term-validator`` writes every cache (label caches ``cache/**/terms.csv``,
the ontology label table ``cache/ontologies/go.tsv``, and the dynamic-enum caches
``cache/enums/*.csv``) sorted by their first column (CURIE) with one row per CURIE.
Older / mixed tool versions used to *append* new entries to the tail instead, which
left the files unsorted and occasionally duplicated. That drift is invisible day to
day but makes git's line-based 3-way merge mis-align and silently duplicate rows on
a merge (see the TCDB project's cache-conflict investigation).

This module enforces the invariant so drift can never be committed again:

    uv run python -m ai_gene_review.tools.cache_lint          # check (non-zero on drift)
    uv run python -m ai_gene_review.tools.cache_lint --fix    # re-sort + dedup in place

The pytest ``tests/test_cache_sorted.py`` and a pre-commit hook both call the check.
The ``--fix`` path reproduces exactly what the validator would write (first column
sorted; duplicates collapsed keeping the LAST occurrence, matching
``load_cache_with_timestamps``' dict semantics).
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def default_repo_root() -> Path:
    """Return the repo root (the nearest ancestor that contains a ``cache/`` dir)."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "cache").is_dir():
            return parent
    return here.parents[3]  # src/ai_gene_review/tools/cache_lint.py -> repo root


def iter_cache_files(root: Path) -> list[Path]:
    """Every committed, header+CURIE cache file whose first column must be sorted."""
    files = sorted(root.glob("cache/**/*.csv")) + sorted(root.glob("cache/**/*.tsv"))
    return [f for f in files if f.is_file()]


def _delimiter(path: Path) -> str:
    return "\t" if path.suffix == ".tsv" else ","


def _read(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open(newline="") as f:
        rows = list(csv.reader(f, delimiter=_delimiter(path)))
    if not rows:
        return [], []
    return rows[0], rows[1:]


def check_file(path: Path) -> list[str]:
    """Return a list of problems (empty == OK): first column must be strictly increasing."""
    _header, data = _read(path)
    keys = [r[0] for r in data if r]
    problems: list[str] = []
    seen: set[str] = set()
    for prev, cur in zip(keys, keys[1:]):
        if cur < prev:
            problems.append(f"out of order: {prev!r} followed by {cur!r}")
    for k in keys:
        if k in seen:
            problems.append(f"duplicate CURIE: {k!r}")
        seen.add(k)
    # Report at most a few of each kind to keep failures readable.
    return problems[:10]


def normalize_file(path: Path) -> bool:
    """Sort by first column and dedup (last wins). Returns True if the file changed."""
    header, data = _read(path)
    by_key: dict[str, list[str]] = {}
    for row in data:
        if row:
            by_key[row[0]] = row  # last occurrence wins
    ordered = [by_key[k] for k in sorted(by_key)]
    if ordered == data:
        return False
    delim = _delimiter(path)
    with path.open("w", newline="") as f:
        w = csv.writer(f, delimiter=delim, lineterminator="\n")
        if header:
            w.writerow(header)
        w.writerows(ordered)
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true", help="re-sort + dedup drifted caches in place")
    ap.add_argument("--root", type=Path, default=default_repo_root(), help="repo root (default: auto)")
    ap.add_argument("paths", nargs="*", type=Path, help="specific cache files (default: all)")
    args = ap.parse_args(argv)

    files = args.paths or iter_cache_files(args.root)
    drifted = []
    for f in files:
        if check_file(f):
            drifted.append(f)

    if args.fix:
        changed = [f for f in drifted if normalize_file(f)]
        for f in changed:
            print(f"fixed: {f.relative_to(args.root) if f.is_relative_to(args.root) else f}")
        print(f"# normalized {len(changed)} file(s)")
        return 0

    if drifted:
        print("Cache files are not sorted/deduplicated (run: "
              "uv run python -m ai_gene_review.tools.cache_lint --fix):", file=sys.stderr)
        for f in drifted:
            rel = f.relative_to(args.root) if f.is_relative_to(args.root) else f
            for problem in check_file(f):
                print(f"  {rel}: {problem}", file=sys.stderr)
        return 1
    print(f"# {len(files)} cache file(s) sorted and deduplicated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
