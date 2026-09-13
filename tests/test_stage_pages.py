from pathlib import Path
import subprocess

import pytest

from ai_gene_review.tools.stage_pages import _safe_clean_output, stage_pages


def _write(path: Path, content: str = "fixture") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _site_fixture(root: Path) -> None:
    subprocess.run(["git", "init", "--quiet", str(root)], check=True)
    _write(root / "index.html")
    _write(root / ".nojekyll", "")
    _write(root / "genes" / "human" / "ABC1" / "ABC1-ai-review.yaml")
    _write(
        root / "genes" / "human" / "ABC1" / "ABC1-ai-review.html",
        '<a href="ABC1-analysis/result.json">analysis</a>',
    )
    _write(root / "genes" / "human" / "ABC1" / "ABC1-analysis" / "result.json")
    _write(root / "genes" / "human" / "ABC1" / "ABC1-notes.md")
    _write(root / "genes" / "human" / "OLD1" / "OLD1-ai-review.html")
    _write(root / "pages" / "projects" / "index.html")
    _write(root / "pages" / "modules" / "index.html")
    _write(root / "pages" / ".DS_Store")
    for filename in ("index.html", "data.js", "schema.js"):
        _write(root / "app" / filename)
    _write(root / "app" / "developer-only.txt")


def test_stage_pages_preserves_urls_and_copies_linked_sources(tmp_path: Path) -> None:
    _site_fixture(tmp_path)
    output = tmp_path / "_site"

    manifest = stage_pages(tmp_path, output)

    assert (output / "index.html").is_file()
    assert (output / ".nojekyll").is_file()
    assert (output / "genes/human/ABC1/ABC1-ai-review.html").is_file()
    assert not (output / "genes/human/ABC1/ABC1-ai-review.yaml").exists()
    assert not (output / "genes/human/ABC1/ABC1-notes.md").exists()
    assert not (output / "genes/human/OLD1/OLD1-ai-review.html").exists()
    assert (output / "pages/projects/index.html").is_file()
    assert not (output / "pages/.DS_Store").exists()
    assert (output / "app/data.js").is_file()
    assert not (output / "app/developer-only.txt").exists()
    assert manifest.gene_pages == 1
    assert manifest.project_pages == 1
    assert manifest.module_pages == 1
    assert (
        output / "genes/human/ABC1/ABC1-analysis/result.json"
    ).read_text() == "fixture"
    assert manifest.linked_source_files_not_staged == 0
    assert manifest.linked_source_bytes_not_staged == 0


def test_stage_pages_includes_transitive_publication_dependencies(
    tmp_path: Path,
) -> None:
    """Reports and their styles, images, downloads, and directory URLs still work."""
    _site_fixture(tmp_path)
    _write(
        tmp_path / "index.html",
        """<a href="docs/stats_report.html">Stats</a>
        <a href="/ai-gene-review/evaluation/?view=all&amp;sort=name">Evaluation</a>""",
    )
    report = """<link rel="stylesheet" href="assets/report.css">
        <a href="../genes/human/ABC1/ABC1-notes.md">Notes</a>
        <a href="report.pdf">PDF</a>
        <a href="/ai-gene-review/rules/arba/index.html">Rules</a>
        <img srcset="assets/small.png 1x, assets/large%20image.png 2x">"""
    _write(tmp_path / "docs/stats_report.html", report)
    _write(
        tmp_path / "docs/assets/report.css",
        '@import "theme.css"; body { background: url(background.png) }',
    )
    _write(tmp_path / "docs/assets/theme.css", "@font-face { src: url(font.woff2) }")
    for relative in (
        "docs/report.pdf",
        "docs/assets/small.png",
        "docs/assets/large image.png",
        "docs/assets/background.png",
        "docs/assets/font.woff2",
        "evaluation/index.html",
        "rules/arba/index.html",
    ):
        _write(tmp_path / relative)
    # Cycle through already-discovered pages must not cause repeated copying.
    _write(tmp_path / "evaluation/index.html", '<a href="../index.html">Home</a>')

    manifest = stage_pages(tmp_path, tmp_path / "_site")

    for relative in (
        "docs/stats_report.html",
        "docs/report.pdf",
        "docs/assets/report.css",
        "docs/assets/theme.css",
        "docs/assets/background.png",
        "docs/assets/font.woff2",
        "docs/assets/small.png",
        "docs/assets/large image.png",
        "evaluation/index.html",
        "rules/arba/index.html",
        "genes/human/ABC1/ABC1-notes.md",
    ):
        assert (tmp_path / "_site" / relative).read_bytes() == (
            tmp_path / relative
        ).read_bytes()
    assert manifest.linked_source_files_not_staged == 0


def test_stage_pages_does_not_follow_private_or_external_dependencies(
    tmp_path: Path,
) -> None:
    """Only public repository paths can enter the publication tree."""
    _site_fixture(tmp_path)
    _write(tmp_path / ".private/secret.txt", "secret")
    _write(
        tmp_path / "index.html",
        """<a href=".git/config">Git</a>
        <a href="_site/index.html">Staging</a>
        <a href=".private/secret.txt">Private</a>
        <a href="https://example.org/external.html">External</a>
        <a href="../../outside.txt">Outside</a>""",
    )

    stage_pages(tmp_path, tmp_path / "_site")

    assert not (tmp_path / "_site/.git").exists()
    assert not (tmp_path / "_site/.private").exists()
    assert not (tmp_path / "_site/_site").exists()


def test_stage_pages_respects_base_urls_and_static_script_downloads(
    tmp_path: Path,
) -> None:
    """Resolve browser-relative URLs without rewriting the document."""
    _site_fixture(tmp_path)
    _write(
        tmp_path / "index.html",
        """<base href="/ai-gene-review/docs/">
        <script src="report.js"></script><a href="report.html">Report</a>""",
    )
    _write(
        tmp_path / "docs/report.js",
        'fetch("data.json?view=all"); import("./extra.js");',
    )
    _write(tmp_path / "docs/extra.js", 'fetch("more.json");')
    for name in ("report.html", "data.json", "more.json"):
        _write(tmp_path / "docs" / name)

    stage_pages(tmp_path, tmp_path / "_site")

    for name in ("report.html", "report.js", "extra.js", "data.json", "more.json"):
        assert (tmp_path / "_site/docs" / name).is_file()


def test_script_fetch_uses_document_url_not_script_url(tmp_path: Path) -> None:
    """An external script fetches relative to the page, not its own directory."""
    _site_fixture(tmp_path)
    _write(tmp_path / "index.html", '<script src="scripts/report.js"></script>')
    _write(tmp_path / "scripts/report.js", 'fetch("data.json");')
    _write(tmp_path / "data.json", "public data")
    _write(tmp_path / "scripts/data.json", "wrong data")

    stage_pages(tmp_path, tmp_path / "_site")

    assert (tmp_path / "_site/data.json").read_text() == "public data"
    assert not (tmp_path / "_site/scripts/data.json").exists()


def test_stage_pages_reports_linked_orphan_review_instead_of_copying(
    tmp_path: Path,
) -> None:
    """A stale navigation link must not resurrect a deleted gene review."""
    _site_fixture(tmp_path)
    _write(
        tmp_path / "index.html",
        '<a href="genes/human/OLD1/OLD1-ai-review.html">Old</a>',
    )

    manifest = stage_pages(tmp_path, tmp_path / "_site")

    assert not (tmp_path / "_site/genes/human/OLD1/OLD1-ai-review.html").exists()
    assert manifest.linked_source_files_not_staged == 1
    assert manifest.linked_source_bytes_not_staged == len("fixture")
    assert not manifest.deployable


def test_stage_pages_removes_stale_output(tmp_path: Path) -> None:
    _site_fixture(tmp_path)
    output = tmp_path / "_site"
    _write(output / "stale.html")

    stage_pages(tmp_path, output)

    assert not (output / "stale.html").exists()


def test_stage_pages_fails_when_a_review_was_not_rendered(tmp_path: Path) -> None:
    _site_fixture(tmp_path)
    (tmp_path / "genes/human/ABC1/ABC1-ai-review.html").unlink()

    with pytest.raises(FileNotFoundError, match="Missing rendered gene pages"):
        stage_pages(tmp_path, tmp_path / "_site")


def test_stage_pages_refuses_to_clean_repository_root(tmp_path: Path) -> None:
    _site_fixture(tmp_path)

    with pytest.raises(ValueError, match="must be inside"):
        stage_pages(tmp_path, tmp_path)


@pytest.mark.parametrize("directory", ["genes", "pages", "app", ".git", "custom"])
def test_stage_pages_preserves_non_staging_directories(
    tmp_path: Path, directory: str
) -> None:
    """Reject source and arbitrary directories before removing any contents."""
    _site_fixture(tmp_path)
    sentinel = tmp_path / directory / "keep.txt"
    _write(sentinel, "keep me")

    with pytest.raises(ValueError, match="_site"):
        stage_pages(tmp_path, tmp_path / directory)

    assert sentinel.read_text() == "keep me"
    assert (tmp_path / "genes/human/ABC1/ABC1-ai-review.yaml").is_file()


def test_stage_pages_rejects_staging_symlink_to_sources(tmp_path: Path) -> None:
    """Resolving the output must not turn a staging path into a source deletion."""
    _site_fixture(tmp_path)
    (tmp_path / "_site").symlink_to(tmp_path / "genes", target_is_directory=True)

    with pytest.raises(ValueError, match="_site"):
        stage_pages(tmp_path, tmp_path / "_site")

    assert (tmp_path / "genes/human/ABC1/ABC1-ai-review.yaml").is_file()


@pytest.mark.parametrize("nested_in_repository", [False, True])
def test_stage_pages_requires_git_worktree_root(
    tmp_path: Path, nested_in_repository: bool
) -> None:
    """An arbitrary directory or repository subdirectory is not a staging root."""
    if nested_in_repository:
        subprocess.run(["git", "init", "--quiet", str(tmp_path)], check=True)
    root = tmp_path / "arbitrary"
    sentinel = root / "_site" / "keep.txt"
    _write(sentinel, "keep me")

    with pytest.raises(ValueError, match="Git worktree root"):
        stage_pages(root, root / "_site")

    assert sentinel.read_text() == "keep me"


def test_cleanup_supports_linked_git_worktrees(tmp_path: Path) -> None:
    """A worktree with a .git file is a valid root, just like a regular clone."""
    repository = tmp_path / "repository"
    subprocess.run(["git", "init", "--quiet", str(repository)], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.com",
            "-c",
            "commit.gpgsign=false",
            "commit",
            "--quiet",
            "--allow-empty",
            "-m",
            "Fixture",
        ],
        check=True,
    )
    worktree = tmp_path / "worktree"
    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "worktree",
            "add",
            "--quiet",
            "--detach",
            str(worktree),
            "HEAD",
        ],
        check=True,
    )
    _write(worktree / "_site/stale.html")
    assert (worktree / ".git").is_file()

    _safe_clean_output(worktree, worktree / "_site")

    assert list((worktree / "_site").iterdir()) == []
    assert (worktree / ".git").is_file()


def test_broken_links_block_deployment(tmp_path: Path) -> None:
    _site_fixture(tmp_path)
    _write(tmp_path / "index.html", '<a href="missing.pdf">Missing</a>')
    manifest = stage_pages(tmp_path, tmp_path / "_site")
    assert manifest.broken_local_links == 1
    assert manifest.broken_local_link_paths == ["missing.pdf"]
    assert manifest.linked_source_files_not_staged == 0
    assert not manifest.deployable


@pytest.mark.parametrize(
    "size,deployable", [(1_000_000_000, True), (1_000_000_001, False)]
)
def test_exact_size_budget(tmp_path: Path, size: int, deployable: bool) -> None:
    from dataclasses import replace

    _site_fixture(tmp_path)
    manifest = replace(stage_pages(tmp_path, tmp_path / "_site"), total_bytes=size)
    assert manifest.size_budget_bytes == 1_000_000_000
    assert manifest.deployable is deployable


def test_cli_serializes_readiness_and_reports_broken_links(tmp_path: Path) -> None:
    import json
    import sys

    _site_fixture(tmp_path)
    _write(tmp_path / "index.html", '<a href="missing.pdf">Missing</a>')
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "ai_gene_review.tools.stage_pages",
            "--repo-root",
            str(tmp_path),
            "--manifest",
            "manifest.json",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert manifest["deployable"] is False
    assert manifest["size_budget_bytes"] == 1_000_000_000
    assert manifest["broken_local_links"] == 1
    assert manifest["broken_local_link_paths"] == ["missing.pdf"]
    assert "Broken local Pages links" in result.stdout
