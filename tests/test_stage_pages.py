from pathlib import Path

import pytest

from ai_gene_review.tools.stage_pages import stage_pages


def _write(path: Path, content: str = "fixture") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _site_fixture(root: Path) -> None:
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
