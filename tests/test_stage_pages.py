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


def test_stage_pages_preserves_urls_without_copying_gene_sources(tmp_path: Path) -> None:
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
    assert manifest.linked_source_files_not_staged == 1
    assert manifest.linked_source_bytes_not_staged == len("fixture")


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
        ["git", "-C", str(repository), "-c", "user.name=Test",
         "-c", "user.email=test@example.com", "-c", "commit.gpgsign=false",
         "commit", "--quiet", "--allow-empty", "-m", "Fixture"],
        check=True,
    )
    worktree = tmp_path / "worktree"
    subprocess.run(
        ["git", "-C", str(repository), "worktree", "add", "--quiet",
         "--detach", str(worktree), "HEAD"],
        check=True,
    )
    _write(worktree / "_site/stale.html")
    assert (worktree / ".git").is_file()

    _safe_clean_output(worktree, worktree / "_site")

    assert list((worktree / "_site").iterdir()) == []
    assert (worktree / ".git").is_file()
