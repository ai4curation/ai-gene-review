"""Tests for scripts/populate_project_manifest.py."""

import doctest
import importlib.util
import sys
from pathlib import Path

import pytest
from typer.testing import CliRunner

from ai_gene_review.render_projects import manifest_errors, parse_frontmatter

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "populate_project_manifest.py"


@pytest.fixture(scope="module")
def script():
    spec = importlib.util.spec_from_file_location("populate_project_manifest", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_doctests(script):
    assert doctest.testmod(script).failed == 0


PAGE = """---
title: "Foo"
tags: [PIPELINE]
---
# Foo

Body.

## Slides

- [Slides](FOO/slides/FOO-slides.html) (Marp source: [FOO-slides.md](FOO/slides/FOO-slides.md)) — AI generated
"""


@pytest.fixture
def projects(tmp_path: Path) -> Path:
    projects_dir = tmp_path / "projects"
    slides = projects_dir / "FOO" / "slides"
    slides.mkdir(parents=True)
    (slides / "FOO-slides.html").write_text("<html></html>")
    (slides / "FOO-slides.md").write_text("---\nmarp: true\n---\n")
    (projects_dir / "FOO.md").write_text(PAGE)
    (projects_dir / "BAR.md").write_text("---\ntitle: Bar\n---\n# Bar\n")
    (projects_dir / "README.md").write_text("---\ntitle: Projects\n---\n")
    (tmp_path / "briefs.tsv").write_text(
        "FOO\thttps://claude.ai/artifact/foo\n"
        "BAR\thttps://claude.ai/artifact/bar\tBar brief\n"
        "GONE\thttps://claude.ai/artifact/gone\n"
    )
    return projects_dir


def test_cli_populates_manifest_and_drops_slides_section(script, projects):
    args = ["--artifacts", str(projects.parent / "briefs.tsv"),
            "--projects-dir", str(projects)]
    result = CliRunner().invoke(script.app, args)
    assert result.exit_code == 0, result.output
    assert "pages changed: 2" in result.output
    assert "artifact rows with no top-level page: ['GONE']" in result.output

    foo = (projects / "FOO.md").read_text()
    fm, body = parse_frontmatter(foo)
    assert fm["manifest"] == {
        "slides": [{"href": "FOO/slides/FOO-slides.html", "description": "AI generated"}],
        "artifacts": [{"href": "https://claude.ai/artifact/foo", "title": "Project brief"}],
    }
    assert manifest_errors(fm["manifest"], projects) == []
    assert foo.startswith('---\ntitle: "Foo"\ntags: [PIPELINE]\nmanifest:\n')
    assert body == "# Foo\n\nBody.\n"

    bar_fm, _ = parse_frontmatter((projects / "BAR.md").read_text())
    assert bar_fm["manifest"] == {
        "artifacts": [{"href": "https://claude.ai/artifact/bar", "title": "Bar brief"}]
    }
    assert "manifest" not in (projects / "README.md").read_text()

    rerun = CliRunner().invoke(script.app, args)
    assert "pages changed: 0" in rerun.output
