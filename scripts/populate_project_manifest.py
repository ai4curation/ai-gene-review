#!/usr/bin/env python
"""Populate ``manifest`` frontmatter (slides + artifact briefs) on project pages.

For every top-level ``projects/*.md`` page this:

* collects its Marp decks -- ``*.html`` files whose name contains ``slides``
  and that have a sibling ``.md`` source -- from ``projects/<STEM>/slides/``
  (matched case-insensitively, so ``PAINT.md`` finds ``paint/slides/``) and
  from decks the page body already links to;
* adds ``manifest.artifacts`` from a TSV of ``stem<TAB>url[<TAB>title]``
  (title defaults to ``Project brief``);
* writes ``manifest`` with :func:`set_frontmatter_key`, leaving all other
  frontmatter lines untouched;
* removes the in-body ``## Slides`` section when it only repeats the deck
  link. If the section also holds page-footer lines (``---``,
  ``Last updated:``, ``**Source**:``) those are kept and only the heading and
  deck link go; any other content is kept with only the deck link dropped.

Usage::

    uv run python scripts/populate_project_manifest.py --artifacts briefs.tsv
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from urllib.parse import urlparse

import typer

from ai_gene_review.render_projects import parse_frontmatter, set_frontmatter_key

DEFAULT_ARTIFACT_TITLE = "Project brief"
SLIDES_HEADING = re.compile(r"^##\s+Slides\s*$")
DECK_LINE = re.compile(r"^- \[Slides\]\((?P<href>[^)]+)\)")
FOOTER_LINE = re.compile(r"^(---|Last updated:.*|\*\*Source\*\*:.*)$")

app = typer.Typer(add_completion=False)


def is_deck(path: Path) -> bool:
    """A rendered Marp deck: ``*slides*.html`` with its ``.md`` source beside it."""
    return (
        path.suffix == ".html"
        and "slides" in path.stem.lower()
        and path.is_file()
        and path.with_suffix(".md").is_file()
    )


def find_decks(md_path: Path, projects_dir: Path) -> list[str]:
    """Deck hrefs (relative to ``projects_dir``) for one project page."""
    found: list[Path] = []
    for folder in projects_dir.iterdir():
        if folder.is_dir() and folder.name.casefold() == md_path.stem.casefold():
            slides = folder / "slides"
            if slides.is_dir():
                found.extend(sorted(p for p in slides.iterdir() if is_deck(p)))
    body = parse_frontmatter(md_path.read_text())[1]
    for href in re.findall(r"\]\(([^)\s]+\.html)\)", body):
        if urlparse(href).scheme:
            continue
        candidate = (md_path.parent / href).resolve()
        if candidate.is_relative_to(projects_dir.resolve()) and is_deck(candidate):
            found.append(candidate)
    hrefs: list[str] = []
    for path in found:
        href = path.resolve().relative_to(projects_dir.resolve()).as_posix()
        if href not in hrefs:
            hrefs.append(href)
    return hrefs


def strip_slides_sections(text: str, deck_names: set[str]) -> tuple[str, str | None]:
    """Remove redundant ``## Slides`` sections; return (text, what_was_done).

    >>> page = "# P\\n\\n## Results\\n\\nx\\n\\n## Slides\\n\\n- [Slides](F/slides/F-slides.html) (AI)\\n"
    >>> out, action = strip_slides_sections(page, {"F-slides.html"})
    >>> out, action
    ('# P\\n\\n## Results\\n\\nx\\n', 'section')
    >>> page = "## Slides\\n\\n- [Slides](F/slides/F-slides.html)\\n\\nLast updated: 2026\\n"
    >>> strip_slides_sections(page, {"F-slides.html"})
    ('Last updated: 2026\\n', 'heading+link')
    >>> page = "## Slides\\n\\nSee the talk.\\n\\n- [Slides](F/slides/F-slides.html)\\n"
    >>> strip_slides_sections(page, {"F-slides.html"})
    ('## Slides\\n\\nSee the talk.\\n', 'link')
    >>> strip_slides_sections("## Slides\\n\\n- [Slides](other.html)\\n", {"F-slides.html"})[1] is None
    True
    """
    lines = text.split("\n")
    starts = [i for i, line in enumerate(lines) if SLIDES_HEADING.match(line)]
    if len(starts) != 1:
        return text, None
    start = starts[0]
    stop = next(
        (i for i in range(start + 1, len(lines)) if re.match(r"^#{1,2}\s", lines[i])),
        len(lines),
    )
    section = lines[start + 1 : stop]
    deck_idx = [
        i
        for i, line in enumerate(section)
        if (m := DECK_LINE.match(line)) and Path(m["href"]).name in deck_names
    ]
    if not deck_idx:
        return text, None
    rest = [line for i, line in enumerate(section) if i not in deck_idx]
    other = [line for line in rest if line.strip()]
    if not other:
        kept: list[str] = []
        action = "section"
    elif all(FOOTER_LINE.match(line.strip()) for line in other):
        kept = rest
        action = "heading+link"
    else:
        kept = [lines[start]] + rest
        action = "link"
    # Collapse the blank lines left where the heading/link were.
    kept = _collapse_blank_runs(kept)
    before = lines[:start]
    after = lines[stop:]
    if action != "link":
        while before and not before[-1].strip():
            before.pop()
        while kept and not kept[0].strip():
            kept.pop(0)
        if before and (kept or after):
            before.append("")
    while kept and not kept[-1].strip() and not after:
        kept.pop()
    new = before + kept + after
    while len(new) > 1 and not new[-1].strip() and not new[-2].strip():
        new.pop()
    if new and new[-1].strip():
        new.append("")
    return "\n".join(new), action


def _collapse_blank_runs(lines: list[str]) -> list[str]:
    """Collapse runs of blank lines to one.

    >>> _collapse_blank_runs(["a", "", "", "b"])
    ['a', '', 'b']
    """
    out: list[str] = []
    for line in lines:
        if not line.strip() and out and not out[-1].strip():
            continue
        out.append(line)
    return out


def load_artifacts(path: Path) -> dict[str, list[dict[str, str]]]:
    """Read ``stem<TAB>url[<TAB>title]`` rows into manifest artifact entries."""
    entries: dict[str, list[dict[str, str]]] = {}
    with path.open() as handle:
        for row in csv.reader(handle, delimiter="\t"):
            if not row or not row[0].strip():
                continue
            title = row[2] if len(row) > 2 and row[2].strip() else DEFAULT_ARTIFACT_TITLE
            entries.setdefault(row[0].strip(), []).append(
                {"href": row[1].strip(), "title": title}
            )
    return entries


@app.command()
def main(
    artifacts: Path = typer.Option(..., help="TSV: stem, artifact URL, optional title."),
    projects_dir: Path = typer.Option(Path("projects"), help="Projects directory."),
    changed_list: Path | None = typer.Option(None, help="Write changed stems here."),
) -> None:
    """Add manifest.slides / manifest.artifacts to every project page."""
    briefs = load_artifacts(artifacts)
    changed: list[str] = []
    counts = {"slides": 0, "artifacts": 0}
    actions: dict[str, list[str]] = {}
    for md_path in sorted(projects_dir.glob("*.md")):
        if md_path.name == "README.md":
            continue
        text = md_path.read_text()
        manifest: dict[str, list[dict[str, str]]] = {}
        decks = find_decks(md_path, projects_dir)
        if decks:
            manifest["slides"] = [{"href": href} for href in decks]
        if md_path.stem in briefs:
            manifest["artifacts"] = briefs[md_path.stem]
        if not manifest:
            continue
        for kind in manifest:
            counts[kind] += 1
        new = set_frontmatter_key(text, "manifest", manifest)
        new, action = strip_slides_sections(new, {Path(d).name for d in decks})
        if action:
            actions.setdefault(action, []).append(md_path.stem)
        if new != text:
            md_path.write_text(new)
            changed.append(md_path.stem)
    unused = sorted(set(briefs) - {p.stem for p in projects_dir.glob("*.md")})
    typer.echo(f"pages changed: {len(changed)}")
    typer.echo(f"with slides: {counts['slides']}  with artifacts: {counts['artifacts']}")
    for action, stems in sorted(actions.items()):
        typer.echo(f"slides section removal [{action}]: {len(stems)} {stems if action != 'section' else ''}")
    typer.echo(f"artifact rows with no top-level page: {unused}")
    if changed_list:
        changed_list.write_text("\n".join(changed) + "\n")


if __name__ == "__main__":
    app()
