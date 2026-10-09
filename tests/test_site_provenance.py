"""Provenance comes from real Git history, never file mtimes or identities."""

from datetime import datetime, timezone
import json
import os
import subprocess

import pytest
from lxml import html

from ai_gene_review.render_projects import render_project
from ai_gene_review.site_provenance import SourceHistory, collect_build_info, stamp_site_build


def git(root, *args, date="2026-10-01T12:30:00+02:00"):
    """Run real Git with deterministic commit dates and a conspicuous identity."""
    return subprocess.run(
        ["git", "-C", str(root), "-c", "user.name=Hidden Test Person",
         "-c", "user.email=hidden-person@example.invalid", "-c", "commit.gpgsign=false", *args],
        env={**os.environ, "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date},
        check=True, capture_output=True, text=True,
    ).stdout.strip()


@pytest.fixture
def repo(tmp_path):
    git(tmp_path, "init", "-q")
    project = tmp_path / "projects/nested/A λ.md"
    project.parent.mkdir(parents=True)
    project.write_text("# A project\n\nSome evidence.\n")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-qm", "A message that must not be published")
    return tmp_path


def render(root, path=None):
    """Render a real project with its default footer."""
    output, _ = render_project(
        path or root / "projects/nested/A λ.md", root / "pages/projects",
        genes_dir=root / "genes", projects_dir=root / "projects",
    )
    return output.read_text()


def test_project_stamp_tracks_its_source_not_the_repo_tip(repo):
    original_commit = git(repo, "rev-parse", "HEAD")
    first = render(repo)
    (repo / "unrelated.txt").write_text("unrelated")
    git(repo, "add", "unrelated.txt")
    git(repo, "commit", "-qm", "Unrelated change", date="2026-10-09T18:00:00Z")
    assert render(repo) == first
    footer = html.fromstring(first).xpath('//footer')[0]
    assert "Source last changed:" in footer.text_content()
    assert footer.xpath('.//time/@datetime') == ["2026-10-01T10:30:00Z"]
    assert f"/commit/{original_commit}" in first
    assert f"/blob/{original_commit}/projects/nested/A%20%CE%BB.md" in first
    assert "Hidden Test Person" not in first
    assert "hidden-person@" not in first
    assert "A message that must not be published" not in first


@pytest.mark.parametrize("staged", [False, True])
def test_local_edits_do_not_claim_to_match_the_commit(repo, staged):
    project = repo / "projects/nested/A λ.md"
    project.write_text("# Local change\n")
    if staged:
        git(repo, "add", "projects")
    footer = html.fromstring(render(repo)).xpath('//footer')[0].text_content()
    assert "Local changes" in footer
    assert "Last committed source:" in footer
    assert "Source last changed:" not in footer


def test_new_untracked_source_has_no_fabricated_commit(repo):
    project = repo / "projects/new.md"
    project.write_text("# New\n")
    footer = html.fromstring(render(repo, project)).xpath('//footer')[0]
    assert "Local changes" in footer.text_content()
    assert not footer.xpath('.//time | .//a[contains(@href, "/commit/")]')


def test_rename_links_to_the_path_that_exists_at_the_recorded_commit(repo):
    renamed = repo / "projects/renamed.md"
    git(repo, "mv", "projects/nested/A λ.md", "projects/renamed.md")
    git(repo, "commit", "-qm", "Rename", date="2026-10-02T10:00:00Z")
    text = render(repo, renamed)
    assert f'/blob/{git(repo, "rev-parse", "HEAD")}/projects/renamed.md' in text
    assert "2026-10-02T10:00:00Z" in text


def test_shallow_boundary_does_not_masquerade_as_source_change(repo, tmp_path):
    (repo / "unrelated.txt").write_text("another commit")
    git(repo, "add", "unrelated.txt")
    git(repo, "commit", "-qm", "Unrelated", date="2026-10-09T00:00:00Z")
    clone = tmp_path / "shallow"
    git(repo, "clone", "--depth=1", repo.as_uri(), str(clone))
    footer = html.fromstring(render(clone)).xpath('//footer')[0]
    assert "Source history unavailable" in footer.text_content()
    assert not footer.xpath('.//time')


def test_no_git_history_keeps_standalone_rendering_working(tmp_path):
    source = tmp_path / "projects/standalone.md"
    source.parent.mkdir()
    source.write_text("# Standalone\n")
    text = render(tmp_path, source)
    assert "Generated from standalone.md" in text
    assert "Source last changed" not in text
    assert SourceHistory(tmp_path).for_file(source) is None


def test_build_stamp_uses_checked_out_head_and_pins_run_attempt(repo):
    info = collect_build_info(repo, built_at=datetime(2026, 10, 9, 8, 42, tzinfo=timezone.utc), environ={
        "GITHUB_ACTIONS": "true", "GITHUB_RUN_ID": "12345", "GITHUB_RUN_ATTEMPT": "2",
        "GITHUB_SHA": "0" * 40, "GITHUB_ACTOR": "Hidden Test Person",
    })
    assert info["built_at"] == "2026-10-09T08:42:00Z"
    assert info["source_commit"] == git(repo, "rev-parse", "HEAD")
    assert info["run_url"].endswith("/actions/runs/12345/attempts/2")
    assert "Hidden Test Person" not in json.dumps(info)
    assert set(info) == {"built_at", "source_commit", "source_url", "run_url"}


def test_stamped_artifact_is_self_contained_and_preserves_source(repo):
    source = '<html><body><h1>Site</h1><!-- site-build-info --></body></html>'
    (repo / "index.html").write_text(source)
    output = repo / "_site"
    output.mkdir()
    (output / "index.html").write_text(source)
    info = collect_build_info(repo, built_at=datetime(2026, 10, 9, 8, 42, tzinfo=timezone.utc), environ={})
    stamp_site_build(output, info)
    text = (output / "index.html").read_text()
    assert "Site built:" in text and "09 Oct 2026, 08:42 UTC" in text
    assert html.fromstring(text).xpath('//time/@datetime') == [info["built_at"]]
    assert json.loads((output / "build-info.json").read_text()) == info
    assert (repo / "index.html").read_text() == source
    assert "fetch(" not in text
    assert "hidden-person@" not in text
