"""Tests for the decision-record GO guidelines (ai_gene_review.guidelines)."""

from pathlib import Path
from typing import Any, Dict, Optional

import pytest
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.guidelines import (
    BROWSER_DIR,
    GUIDELINES_DIR,
    build,
    browser_href,
    dump_frontmatter,
    load,
    term_errors,
    validate,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def _rule(rid: str, **extra: Any) -> Dict[str, Any]:
    meta: Dict[str, Any] = {
        "id": rid,
        "title": f"Rule {rid}",
        "status": "proposed",
        "topic": rid.split("-")[0],
        "provenance": "GOC",
    }
    meta.update(extra)
    return meta


def _write(root: Path, rel: str, meta: Dict[str, Any], body: str = "# Title\n\n## Decision\n\nDo it.\n") -> Path:
    path = root / GUIDELINES_DIR / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_frontmatter(meta) + "\n" + body)
    return path


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal repository: one split chapter (XX), one unsplit chapter (QN-7)."""
    _write(tmp_path, "XX/README.md", {"id": "XX", "title": "Example", "status": "proposed"}, "# Example\n")
    _write(tmp_path, "XX/XX-1.md", _rule("XX-1", related=["XX-2", "QN-7"]),
           "# XX-1\n\n## Decision\n\nSee [XX-2](XX-2.md) and [QN-7](../qn.md#qn-7).\n")
    _write(tmp_path, "XX/XX-2.md", _rule("XX-2", sources=[{"kind": "wiki", "title": "W", "url": "https://w.org/x"}]))
    (tmp_path / GUIDELINES_DIR / "qn.md").write_text("### QN-7. Legacy rule\n")
    build(tmp_path)
    return tmp_path


def _edit(root: Path, rel: str, **changes: Any) -> None:
    path = root / GUIDELINES_DIR / rel
    from ai_gene_review.render_projects import parse_frontmatter

    meta, body = parse_frontmatter(path.read_text())
    for key, value in changes.items():
        if value is None:
            meta.pop(key, None)
        else:
            meta[key] = value
    path.write_text(dump_frontmatter(meta) + "\n" + body)


def test_repository_guidelines_are_valid() -> None:
    """The committed records pass schema, reference and staleness checks."""
    assert validate(REPO_ROOT) == []


def test_built_fixture_is_valid_and_has_generated_blocks(repo: Path) -> None:
    assert validate(repo) == []
    text = (repo / GUIDELINES_DIR / "XX/XX-1.md").read_text()
    assert "| Related | [XX-2](XX-2.md), [QN-7](../qn.md#qn-7) |" in text
    readme = (repo / GUIDELINES_DIR / "XX/README.md").read_text()
    assert "| [XX-2](XX-2.md) | Rule XX-2 | proposed | [GOC] |" in readme
    assert (repo / BROWSER_DIR / "data.js").read_text().startswith("window.GUIDELINES_DATA = ")
    assert build(repo) == []  # idempotent


@pytest.mark.parametrize(
    "rel, changes, expected",
    [
        ("XX/XX-1.md", {"provenance": "MAYBE"}, "MAYBE"),
        ("XX/XX-1.md", {"id": "XX-9"}, "does not match file name"),
        ("XX/XX-1.md", {"related": ["XX-99"]}, "unknown guideline XX-99"),
        ("XX/XX-1.md", {"status": "superseded"}, "must go together"),
        ("XX/XX-1.md", {"status": "superseded", "superseded_by": "XX-2"}, "does not list XX-1 in supersedes"),
        ("XX/XX-1.md", {"enforced_by": ["src/missing.py"]}, "enforced_by path src/missing.py"),
        ("XX/XX-2.md", {"sources": [{"kind": "repo", "title": "x"}]}, "exactly one of url or path"),
        ("XX/XX-2.md", {"title": "Renamed"}, "generated text is stale"),
    ],
)
def test_validate_reports_problems(repo: Path, rel: str, changes: Dict[str, Any], expected: str) -> None:
    _edit(repo, rel, **changes)
    errors = validate(repo)
    assert any(expected in e for e in errors), errors


def test_rule_both_split_and_legacy_is_an_error(repo: Path) -> None:
    (repo / GUIDELINES_DIR / "qn.md").write_text("### QN-7. Legacy rule\n### XX-2. Duplicate\n")
    assert any("also still a heading" in e for e in validate(repo))


def test_supersession_both_ways_is_valid(repo: Path) -> None:
    _edit(repo, "XX/XX-1.md", status="superseded", superseded_by="XX-2")
    _edit(repo, "XX/XX-2.md", supersedes=["XX-1"])
    build(repo)
    assert validate(repo) == []


@pytest.mark.parametrize(
    "target, expected",
    [
        ("XX-2.md", "#XX-2"),
        ("README.md", "#chapter/XX"),
        ("../qn.md#qn-7", "#QN-7"),
        ("../../../FOO.md#bar", "../../pages/projects/FOO.html#bar"),
        ("../../../../CLAUDE.md", "https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md"),
        ("https://example.org/x", "https://example.org/x"),
    ],
)
def test_browser_href(repo: Path, target: str, expected: str) -> None:
    coll = load(repo)
    assert browser_href(coll, GUIDELINES_DIR / "XX/XX-1.md", target) == expected


class FakeAdapter:
    def __init__(self, labels: Dict[str, Optional[str]], obsolete: set):
        self._labels, self._obsolete = labels, obsolete

    def obsoletes(self):
        return iter(self._obsolete)

    def label(self, curie: str) -> Optional[str]:
        return self._labels.get(curie)


def test_term_errors(repo: Path) -> None:
    _edit(repo, "XX/XX-1.md", go_terms=[
        {"term_id": "GO:0000001", "label": "right"},
        {"term_id": "GO:0000002", "label": "wrong"},
        {"term_id": "GO:0000003", "label": "x"},
        {"term_id": "GO:0000004", "obsolete": True},
        {"term_id": "GO:0000005", "obsolete": True},
    ])
    adapter = FakeAdapter({"GO:0000001": "right", "GO:0000002": "other", "GO:0000005": "live"}, {"GO:0000003", "GO:0000004"})
    errors = term_errors(load(repo), adapter)
    assert len(errors) == 3
    assert any("should be 'other'" in e for e in errors)
    assert any("GO:0000003 is obsolete but not flagged" in e for e in errors)
    assert any("flagged obsolete but is live" in e for e in errors)


def test_cli_validate_and_build(repo: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["guidelines", "validate", "--root", str(repo)])
    assert result.exit_code == 0, result.output
    assert "guidelines OK" in result.output
    _edit(repo, "XX/XX-2.md", title="Renamed")
    assert runner.invoke(app, ["guidelines", "validate", "--root", str(repo)]).exit_code == 1
    result = runner.invoke(app, ["guidelines", "build", "--root", str(repo)])
    assert "updated" in result.output
    assert runner.invoke(app, ["guidelines", "validate", "--root", str(repo)]).exit_code == 0
