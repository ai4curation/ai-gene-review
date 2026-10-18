"""Enforce that project markdown files carry YAML frontmatter with a title.

Only top-level project pages (``projects/*.md``) must begin with a YAML
frontmatter block that defines a non-empty ``title``. Files nested inside a
project's subdirectories (sub-pages, generated reports/dossiers, deep-research
dumps, ``*.citations.md`` sidecars) are not required to carry frontmatter.
"""

from pathlib import Path

import datetime
import re

import pytest
import yaml

from ai_gene_review.render_projects import (
    MANIFEST_ENTRY_KEYS,
    MANIFEST_KINDS,
    manifest_errors,
)

PROJECTS_DIR = Path(__file__).resolve().parents[1] / "projects"

#: Controlled vocabulary for the project lifecycle ``maturity`` field.
VALID_MATURITY = {"SCOPING", "IN_PROGRESS", "MATURE", "COMPLETE", "ARCHIVED"}

#: Controlled vocabulary for the project ``tags`` list.
VALID_TAGS = {
    "FLAGSHIP",
    "OBSOLETION",
    "PIPELINE",
    "BIOLOGY_DOMAIN",
    "EVALUATION",
    "ML_PREDICTIONS",
}

#: Controlled vocabulary for a manual review's ``status``.
VALID_REVIEW_STATUS = {"READY", "CHANGES_REQUESTED"}

#: Allowed keys inside a single ``manual_reviews`` entry.
REVIEW_KEYS = {"reviewed_by", "date", "notes", "todos", "status"}

#: Resource lists allowed under ``manifest`` (defined once, in the renderer).
VALID_MANIFEST_KINDS = set(MANIFEST_KINDS)

#: Allowed keys inside a single ``manifest`` entry.
MANIFEST_KEYS = MANIFEST_ENTRY_KEYS

#: YYYY-MM-DD date strings (YAML may also parse these into ``datetime.date``).
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


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


def _parse_frontmatter(text: str) -> dict:
    """Return the parsed leading YAML frontmatter block as a dict (or {})."""
    if not text.startswith("---"):
        return {}
    lines = text.split("\n")
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}
    data = yaml.safe_load("\n".join(lines[1:end_idx])) or {}
    return data if isinstance(data, dict) else {}


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


@pytest.mark.parametrize(
    "md_path",
    _project_markdown_files(),
    ids=lambda p: str(p.relative_to(PROJECTS_DIR)),
)
def test_project_maturity_is_controlled(md_path: Path) -> None:
    """If a project declares ``maturity`` it must use the controlled vocabulary.

    ``maturity`` replaces the old free-text ``status`` field; ``status`` should
    no longer appear at the top level of a project page.
    """
    fm = _parse_frontmatter(md_path.read_text())
    assert "status" not in fm, (
        f"{md_path.relative_to(PROJECTS_DIR)} uses the retired 'status' field; "
        "rename it to 'maturity' using one of "
        f"{sorted(VALID_MATURITY)}."
    )
    maturity = fm.get("maturity")
    if maturity is not None:
        assert maturity in VALID_MATURITY, (
            f"{md_path.relative_to(PROJECTS_DIR)} has invalid maturity "
            f"{maturity!r}; must be one of {sorted(VALID_MATURITY)}."
        )


@pytest.mark.parametrize(
    "md_path",
    _project_markdown_files(),
    ids=lambda p: str(p.relative_to(PROJECTS_DIR)),
)
def test_project_tags_are_controlled(md_path: Path) -> None:
    """If a project declares ``tags`` every tag must be in the vocabulary."""
    fm = _parse_frontmatter(md_path.read_text())
    tags = fm.get("tags")
    if tags is None:
        return
    assert isinstance(tags, list), (
        f"{md_path.relative_to(PROJECTS_DIR)} 'tags' must be a list."
    )
    invalid = sorted(set(map(str, tags)) - VALID_TAGS)
    assert not invalid, (
        f"{md_path.relative_to(PROJECTS_DIR)} has invalid tag(s) {invalid}; "
        f"allowed tags are {sorted(VALID_TAGS)}."
    )


@pytest.mark.parametrize(
    "md_path",
    _project_markdown_files(),
    ids=lambda p: str(p.relative_to(PROJECTS_DIR)),
)
def test_project_manual_reviews_are_well_formed(md_path: Path) -> None:
    """If a project declares ``manual_reviews`` each entry must be well-formed.

    ``manual_reviews`` is an optional list of reviewer sign-offs::

        manual_reviews:
          - reviewed_by: cjm
            date: 2024-01-15
            status: CHANGES_REQUESTED
            notes: ...
            todos:
              - ...

    Each entry needs a non-empty ``reviewed_by``; ``status`` (if given) must use
    the controlled vocabulary; ``date`` (if given) must be YYYY-MM-DD; ``todos``
    must be a list and ``notes`` a string. Unknown keys are rejected to catch
    typos.
    """
    fm = _parse_frontmatter(md_path.read_text())
    reviews = fm.get("manual_reviews")
    if reviews is None:
        return

    rel = md_path.relative_to(PROJECTS_DIR)
    assert isinstance(reviews, list), f"{rel} 'manual_reviews' must be a list."

    for i, review in enumerate(reviews):
        assert isinstance(review, dict), (
            f"{rel} manual_reviews[{i}] must be a mapping."
        )

        unknown = sorted(set(review) - REVIEW_KEYS)
        assert not unknown, (
            f"{rel} manual_reviews[{i}] has unknown key(s) {unknown}; "
            f"allowed keys are {sorted(REVIEW_KEYS)}."
        )

        reviewer = review.get("reviewed_by")
        assert reviewer is not None and str(reviewer).strip(), (
            f"{rel} manual_reviews[{i}] needs a non-empty 'reviewed_by'."
        )

        status = review.get("status")
        if status is not None:
            assert status in VALID_REVIEW_STATUS, (
                f"{rel} manual_reviews[{i}] has invalid status {status!r}; "
                f"must be one of {sorted(VALID_REVIEW_STATUS)}."
            )

        date = review.get("date")
        if date is not None:
            valid_date = isinstance(date, datetime.date) or (
                isinstance(date, str) and bool(_DATE_RE.match(date))
            )
            assert valid_date, (
                f"{rel} manual_reviews[{i}] 'date' must be YYYY-MM-DD; got {date!r}."
            )

        todos = review.get("todos")
        if todos is not None:
            assert isinstance(todos, list), (
                f"{rel} manual_reviews[{i}] 'todos' must be a list."
            )

        notes = review.get("notes")
        if notes is not None:
            assert isinstance(notes, str), (
                f"{rel} manual_reviews[{i}] 'notes' must be a string."
            )


#: Registry of project collections (key -> title/index/description).
COLLECTIONS = yaml.safe_load((PROJECTS_DIR / "collections.yaml").read_text()) or {}


@pytest.mark.parametrize("key", sorted(COLLECTIONS))
def test_collection_index_page_exists(key: str) -> None:
    """Every registered collection names an existing top-level index page."""
    index = COLLECTIONS[key].get("index")
    assert index, f"collection {key} must declare an 'index' project slug"
    assert (PROJECTS_DIR / f"{index}.md").is_file(), (
        f"collection {key} index projects/{index}.md does not exist"
    )


@pytest.mark.parametrize(
    "md_path",
    _project_markdown_files(),
    ids=lambda p: str(p.relative_to(PROJECTS_DIR)),
)
def test_project_collections_are_registered(md_path: Path) -> None:
    """``collections`` must be a list of keys from ``projects/collections.yaml``."""
    fm = _parse_frontmatter(md_path.read_text())
    collections = fm.get("collections")
    if collections is None:
        return
    rel = md_path.relative_to(PROJECTS_DIR)
    assert isinstance(collections, list), f"{rel} 'collections' must be a list."
    unknown = sorted(set(map(str, collections)) - set(COLLECTIONS))
    assert not unknown, (
        f"{rel} has unregistered collection(s) {unknown}; "
        f"register them in projects/collections.yaml ({sorted(COLLECTIONS)})."
    )


@pytest.mark.parametrize(
    "md_path",
    _project_markdown_files(),
    ids=lambda p: str(p.relative_to(PROJECTS_DIR)),
)
def test_project_manifest_is_well_formed(md_path: Path) -> None:
    """If a project declares ``manifest`` its resource links must be valid.

    ``manifest`` is an optional mapping of typed resource lists::

        manifest:
          slides:
            - href: FOO/slides/FOO-slides.html   # relative to projects/, or https
              title: Project deck                # optional
          artifacts:
            - href: https://claude.ai/artifact/XXXX
              title: Project brief

    Allowed lists are ``VALID_MANIFEST_KINDS``; each entry needs ``href`` and
    may carry ``title``/``description`` (``MANIFEST_KEYS``). A local slides
    href must be an existing deck under projects/ with its Marp ``.md``
    source beside it; artifact hrefs must be https URLs.
    """
    fm = _parse_frontmatter(md_path.read_text())
    if "manifest" not in fm:
        return
    errors = manifest_errors(fm["manifest"], PROJECTS_DIR)
    assert not errors, f"{md_path.relative_to(PROJECTS_DIR)}: " + "; ".join(errors)


@pytest.fixture
def deck_projects(tmp_path: Path) -> Path:
    """A projects/ dir holding one Marp deck (html + md) and one orphan html."""
    slides = tmp_path / "projects" / "FOO" / "slides"
    slides.mkdir(parents=True)
    (slides / "FOO-slides.html").write_text("<html></html>")
    (slides / "FOO-slides.md").write_text("---\nmarp: true\n---\n")
    (slides / "orphan.html").write_text("<html></html>")
    (tmp_path / "outside.html").write_text("<html></html>")
    return tmp_path / "projects"


@pytest.mark.parametrize(
    "manifest",
    [
        {},
        {"slides": [{"href": "FOO/slides/FOO-slides.html"}]},
        {"slides": [{"href": "FOO/slides/FOO-slides.html", "title": "Deck",
                     "description": "Overview deck"}]},
        {"slides": [{"href": "https://example.org/deck.html"}]},
        {"artifacts": [{"href": "https://claude.ai/artifact/abc", "title": "Project brief"}]},
        {"slides": [], "artifacts": []},
    ],
)
def test_manifest_good(deck_projects: Path, manifest: dict) -> None:
    assert manifest_errors(manifest, deck_projects) == []


@pytest.mark.parametrize(
    "manifest,expected",
    [
        ([], "must be a mapping"),
        ({"decks": []}, "unknown key(s) ['decks']"),
        ({"slides": {"href": "FOO/slides/FOO-slides.html"}}, "manifest.slides must be a list"),
        ({"slides": ["FOO/slides/FOO-slides.html"]}, "slides[0] must be a mapping"),
        ({"slides": [{"title": "Deck"}]}, "needs a non-empty string 'href'"),
        ({"slides": [{"href": "FOO/slides/FOO-slides.html", "url": "x"}]}, "unknown key(s) ['url']"),
        ({"slides": [{"href": "FOO/slides/FOO-slides.html", "title": 3}]}, "'title' must be a string"),
        ({"slides": [{"href": "FOO/slides/missing.html"}]}, "does not exist under projects/"),
        ({"slides": [{"href": "FOO/slides/orphan.html"}]}, "no sibling orphan.md source"),
        ({"slides": [{"href": "../outside.html"}]}, "path under projects/"),
        ({"slides": [{"href": "http://example.org/deck.html"}]}, "path under projects/"),
        ({"artifacts": [{"href": "FOO/slides/FOO-slides.html"}]}, "must be an https URL"),
        ({"artifacts": [{"href": "http://claude.ai/artifact/abc"}]}, "must be an https URL"),
    ],
)
def test_manifest_bad(deck_projects: Path, manifest, expected: str) -> None:
    errors = manifest_errors(manifest, deck_projects)
    assert any(expected in e for e in errors), errors
