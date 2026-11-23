#!/usr/bin/env python3
"""Warn when content PRs also edit shared project pages or rendered pages."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterable, Sequence
from pathlib import PurePosixPath

CONTENT_PREFIXES = (
    "genes/",
    "gocams/",
    "modules/",
    "publications/",
    "reactome/",
    "rules/curated/",
)

CONTENT_HISTORY_PREFIXES = (
    "history/gocams/",
    "history/genes/",
    "history/modules/",
    "history/other/",
    "history/rules/",
)

SHARED_PREFIXES = ("cache/",)
SHARED_SINGLE_FILE_PATHS = {
    "interpro/panther/panther.obo",
    "projects/collections.yaml",
}


def is_top_level_project_page(path: str) -> bool:
    posix = PurePosixPath(path)
    return len(posix.parts) == 2 and posix.parts[0] == "projects" and posix.suffix == ".md"


def is_rendered_page(path: str) -> bool:
    return path.startswith("pages/")


def is_family_review_path(path: str) -> bool:
    posix = PurePosixPath(path)
    return (
        len(posix.parts) >= 3
        and posix.parts[0] == "interpro"
        and posix.parts[1] == "panther"
        and posix.parts[2].startswith("PTHR")
    )


def is_shared_path(path: str) -> bool:
    return (
        is_top_level_project_page(path)
        or is_rendered_page(path)
        or path in SHARED_SINGLE_FILE_PATHS
        or path.startswith(SHARED_PREFIXES)
    )


def is_content_path(path: str) -> bool:
    return path.startswith(CONTENT_PREFIXES + CONTENT_HISTORY_PREFIXES) or is_family_review_path(
        path
    )


def shared_paths(paths: Iterable[str]) -> list[str]:
    return sorted(path for path in set(paths) if is_shared_path(path))


def content_paths(paths: Iterable[str]) -> list[str]:
    return sorted(path for path in set(paths) if is_content_path(path))


def escape_github_command(value: str) -> str:
    return (
        value.replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
        .replace(":", "%3A")
        .replace(",", "%2C")
    )


def warn(shared: Sequence[str], content: Sequence[str]) -> None:
    if not shared or not content:
        print("No shared project/page paths mixed with content paths.")
        return

    print(
        "::warning title=Shared project/page files in content PR::"
        "Content PRs should avoid top-level projects/*.md status pages, "
        "shared cache files, and rendered pages/** output. Move status ticks "
        "and cache refreshes to separate PRs after content merges, and let "
        "generate-pages render HTML from main."
    )
    print("Shared files to move out of this content PR:")
    for path in shared:
        print(f"- {path}")
        print(
            "::warning "
            f"file={escape_github_command(path)},"
            "title=Shared file in content PR::"
            "Move this status, cache, or rendered file to a separate status, "
            "refresh, or generated artifact PR."
        )
    print("Content files that made this a content PR:")
    for path in content:
        print(f"- {path}")


def read_changed_paths(args: Sequence[str]) -> list[str]:
    if not args:
        return [line.strip() for line in sys.stdin if line.strip()]
    return [path for path in args if path]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="Changed paths. If none are given, paths are read from stdin.",
    )
    args = parser.parse_args(argv)
    paths = read_changed_paths(args.paths)
    warn(shared_paths(paths), content_paths(paths))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
