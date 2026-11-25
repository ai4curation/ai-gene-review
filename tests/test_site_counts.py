"""Tests for the collection counts stamped onto the front page."""

from pathlib import Path

import pytest

from ai_gene_review.site_counts import (
    COUNT_MARKER,
    collect_site_counts,
    fill_counts,
    stamp_site_counts,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def _touch(root: Path, relative: str, text: str = "") -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    for relative in (
        "genes/human/TP53/TP53-ai-review.yaml",
        "genes/human/BRCA1/BRCA1-ai-review.yaml",
        "genes/human/TP53/TP53-protnlm-predictions-review.yaml",
        "interpro/panther/PTHR1/PTHR1-review.yaml",
        "gocams/abc/abc-review.yaml",
        "gocams/def/def-src.yaml",
        "projects/FOO.md",
        "projects/README.md",
        "rules/arba/ARBA1/ARBA1-review.yaml",
        "rules/curated/CR-0001.yaml",
        "rules/curated/README.md",
    ):
        _touch(tmp_path, relative)
    _touch(tmp_path, "modules/m.yaml", "id: MODULE:m\ntitle: M\nmodule:\n  id: m\n")
    _touch(
        tmp_path,
        "projects/collections.yaml",
        "MAPPINGS:\n  title: Mapping reviews\n  index: MAPPING_REVIEWS\n",
    )
    _touch(tmp_path, "projects/OLD.md", "---\ntitle: Old\ntags: [OBSOLETION]\n---\n")
    _touch(
        tmp_path, "projects/M2GO.md", "---\ntitle: M2GO\ncollections: [MAPPINGS]\n---\n"
    )
    return tmp_path


def test_collect_site_counts(repo: Path) -> None:
    counts = collect_site_counts(repo)
    assert counts["genes"] == 2
    assert counts["prediction_reviews"] == 1
    assert counts["families"] == 1
    assert counts["gocam_reviews"] == 1
    assert counts["projects"] == 3
    assert counts["obsoletion_projects"] == 1
    assert counts["mapping_reviews"] == 1
    assert counts["rule_reviews"] == 1
    assert counts["curated_rules"] == 1
    assert counts["modules"] == 1


def test_stamp_fills_markers_in_staged_homepage(repo: Path, tmp_path: Path) -> None:
    site = tmp_path / "_site"
    site.mkdir()
    (site / "index.html").write_text("<span><!-- count:genes --> genes</span>")
    stamp_site_counts(site, repo)
    assert (site / "index.html").read_text() == "<span>2 genes</span>"


def test_stamp_computes_only_requested_counts(tmp_path: Path) -> None:
    """A page without project markers needs no projects/collections.yaml."""
    site = tmp_path / "_site"
    site.mkdir()
    (site / "index.html").write_text("<p>no markers</p>")
    stamp_site_counts(site, tmp_path)
    assert (site / "index.html").read_text() == "<p>no markers</p>"


def test_unknown_marker_fails(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text("<!-- count:gnees -->")
    with pytest.raises(KeyError, match="gnees"):
        stamp_site_counts(tmp_path, tmp_path)


def test_front_page_markers_are_all_known() -> None:
    """Every marker in the real front page must name a count we collect."""
    html = (REPO_ROOT / "index.html").read_text()
    markers = set(COUNT_MARKER.findall(html))
    assert markers, "the front page should carry count markers"
    counts = collect_site_counts(REPO_ROOT)
    assert markers <= set(counts)
    assert all(counts[key] > 0 for key in markers)
    assert "<!-- count:" not in fill_counts(html, counts)
