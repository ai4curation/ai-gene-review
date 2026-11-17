"""Collection counts stamped onto the front page at build time.

The hand-written ``index.html`` marks each count with an HTML comment such as
``<!-- count:genes -->``. :func:`stamp_site_counts` replaces each marker in the
staged copy with a number derived from the repository, so the published front
page shows how large each collection is without anyone editing it.
"""

from __future__ import annotations

import re
from pathlib import Path

from ai_gene_review.render_modules import iter_module_files

COUNT_MARKER = re.compile(r"<!-- count:([a-z_]+) -->")

#: Glob patterns (relative to the repository root) whose matches are counted.
GLOB_COUNTS: dict[str, tuple[str, ...]] = {
    "genes": ("genes/*/*/*-ai-review.yaml",),
    "families": ("interpro/*/*/*-review.yaml",),
    "gocam_reviews": ("gocams/*/*-review.yaml",),
    "prediction_reviews": ("genes/*/*/*predictions-review.yaml",),
    "projects": ("projects/*.md",),
    "rule_reviews": ("rules/arba/*/*-review.yaml", "rules/unirule/*/*-review.yaml"),
    "curated_rules": ("rules/curated/CR-*.yaml",),
}


def collect_site_counts(repo_root: Path) -> dict[str, int]:
    """Count the items in each published collection.

    ``projects/README.md`` is not a project, and modules are counted with the
    module renderer's own document filter so the number matches the index.
    """
    counts = {
        key: sum(len(list(repo_root.glob(pattern))) for pattern in patterns)
        for key, patterns in GLOB_COUNTS.items()
    }
    if (repo_root / "projects" / "README.md").is_file():
        counts["projects"] -= 1
    counts["modules"] = len(iter_module_files(repo_root / "modules"))
    return counts


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

    An unknown key is an error, so a typo in the page cannot ship silently.

    >>> fill_counts("<b><!-- count:genes --></b> genes", {"genes": 5826})
    '<b>5,826</b> genes'
    >>> fill_counts("<!-- count:gnees -->", {"genes": 1})
    Traceback (most recent call last):
    ...
    KeyError: "Unknown count marker 'gnees'; known: genes"
    """

    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in counts:
            known = ", ".join(sorted(counts))
            raise KeyError(f"Unknown count marker {key!r}; known: {known}")
        return format_count(counts[key])

    return COUNT_MARKER.sub(replace, html)


def stamp_site_counts(output_dir: Path, counts: dict[str, int]) -> None:
    """Fill the count markers in the staged front page."""
    homepage = output_dir / "index.html"
    homepage.write_text(
        fill_counts(homepage.read_text(encoding="utf-8"), counts), encoding="utf-8"
    )
