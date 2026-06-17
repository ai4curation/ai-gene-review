"""Enforce that project markdown files carry YAML frontmatter with a title.

Only top-level project pages (``projects/*.md``) must begin with a YAML
frontmatter block that defines a non-empty ``title``. Files nested inside a
project's subdirectories (sub-pages, generated reports/dossiers, deep-research
dumps, ``*.citations.md`` sidecars) are not required to carry frontmatter.
"""

from pathlib import Path

import pytest

PROJECTS_DIR = Path(__file__).resolve().parents[1] / "projects"


def _is_exempt(path: Path) -> bool:
    """Auto-generated files that should not be hand-edited are exempt."""
    name = path.name
    return "-deep-research-" in name or name.endswith(".citations.md")


def _project_markdown_files() -> list[Path]:
    if not PROJECTS_DIR.is_dir():
        return []
    return sorted(p for p in PROJECTS_DIR.glob("*.md") if not _is_exempt(p))


def _parse_frontmatter_title(text: str) -> str | None:
    """Return the title from a leading YAML frontmatter block, or None.

    Mirrors the detection used by render_projects.parse_frontmatter: the block is
    delimited by a leading ``---`` line and the next line that is exactly ``---``.
    """
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None
    import yaml

    block = "\n".join(lines[1:end_idx])
    data = yaml.safe_load(block) or {}
    if not isinstance(data, dict):
        return None
    title = data.get("title")
    if title is None:
        return None
    return str(title).strip() or None


@pytest.mark.parametrize(
    "md_path",
    _project_markdown_files(),
    ids=lambda p: str(p.relative_to(PROJECTS_DIR)),
)
def test_project_file_has_frontmatter_title(md_path: Path) -> None:
    """Each project markdown file must start with frontmatter containing a title."""
    text = md_path.read_text()
    assert text.startswith("---"), (
        f"{md_path.relative_to(PROJECTS_DIR)} is missing a YAML frontmatter block. "
        "Add a leading '---' ... '---' block with a 'title:' field."
    )
    title = _parse_frontmatter_title(text)
    assert title, (
        f"{md_path.relative_to(PROJECTS_DIR)} frontmatter must define a non-empty 'title'."
    )
