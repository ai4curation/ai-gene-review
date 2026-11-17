"""Collection counts stamped onto the front page at build time.

The hand-written ``index.html`` marks each count with an HTML comment such as
``<!-- count:genes -->``. :func:`stamp_site_counts` replaces each marker in the
staged copy with a number derived from the repository, so the published front
page shows how large each collection is without anyone editing it.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Callable, Iterable, Optional

from ai_gene_review.render_hubs import (
    MAPPINGS_COLLECTION,
    OBSOLETION_TAG,
    collection_members,
    projects_where,
    rule_review_count,
)
from ai_gene_review.render_modules import iter_module_files

COUNT_MARKER = re.compile(r"<!-- count:([a-z_]+) -->")


def _glob_count(*patterns: str) -> Callable[[Path], int]:
    """Return a counter of the files matching ``patterns`` under a repository root."""
    return lambda root: sum(len(list(root.glob(pattern))) for pattern in patterns)


def _count_projects(root: Path) -> int:
    """Top-level project pages; ``projects/README.md`` is not a project."""
    return sum(
        1 for path in (root / "projects").glob("*.md") if path.name != "README.md"
    )


#: Each count the front page can show, keyed by its marker name.
COUNTERS: dict[str, Callable[[Path], int]] = {
    "genes": _glob_count("genes/*/*/*-ai-review.yaml"),
    "families": _glob_count("interpro/*/*/*-review.yaml"),
    "gocam_reviews": _glob_count("gocams/*/*-review.yaml"),
    "prediction_reviews": _glob_count("genes/*/*/*predictions-review.yaml"),
    "rule_reviews": rule_review_count,
    "curated_rules": _glob_count("rules/curated/CR-*.yaml"),
    "projects": _count_projects,
    # The module renderer's own document filter, so the number matches its index.
    "modules": lambda root: len(iter_module_files(root / "modules")),
    "obsoletion_projects": lambda root: len(
        projects_where(root / "projects", "tags", OBSOLETION_TAG)
    ),
    "mapping_reviews": lambda root: len(
        collection_members(root / "projects", MAPPINGS_COLLECTION)
    ),
}


def collect_site_counts(
    repo_root: Path, keys: Optional[Iterable[str]] = None
) -> dict[str, int]:
    """Compute the named counts (all of them by default).

    An unknown key is an error, so a typo in the page cannot ship silently.

    >>> collect_site_counts(Path("."), ["gnees"])
    Traceback (most recent call last):
    ...
    KeyError: "Unknown count marker 'gnees'"
    """
    wanted = list(COUNTERS) if keys is None else sorted(set(keys))
    unknown = [key for key in wanted if key not in COUNTERS]
    if unknown:
        raise KeyError(f"Unknown count marker {unknown[0]!r}")
    return {key: COUNTERS[key](repo_root) for key in wanted}


def format_count(value: int) -> str:
    """Format a count with thousands separators.

    >>> format_count(5826)
    '5,826'
    >>> format_count(40)
    '40'
    """
    return f"{value:,}"


def fill_counts(html: str, counts: dict[str, int]) -> str:
    """Replace every ``<!-- count:KEY -->`` marker with its formatted count.

    >>> fill_counts("<b><!-- count:genes --></b> genes", {"genes": 5826})
    '<b>5,826</b> genes'
    """
    return COUNT_MARKER.sub(lambda match: format_count(counts[match.group(1)]), html)


def stamp_site_counts(output_dir: Path, repo_root: Path) -> None:
    """Fill the count markers in the staged front page.

    Only the counts the page asks for are computed.
    """
    homepage = output_dir / "index.html"
    html = homepage.read_text(encoding="utf-8")
    counts = collect_site_counts(repo_root, COUNT_MARKER.findall(html))
    homepage.write_text(fill_counts(html, counts), encoding="utf-8")
