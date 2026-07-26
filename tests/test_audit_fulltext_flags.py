"""Tests for the ``full_text_unavailable`` flag audit."""

from __future__ import annotations

import pytest

from ai_gene_review.tools.audit_fulltext_flags import (
    cached_full_text_availability,
    find_stale_flags,
    remove_stale_flags,
)


@pytest.fixture
def publications(tmp_path):
    """A cache with one full-text record, one abstract-only, and one missing the key."""
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_111.md").write_text(
        "---\ntitle: has full text\nfull_text_available: true\n---\nbody\n"
    )
    (pubs / "PMID_222.md").write_text(
        "---\ntitle: abstract only\nfull_text_available: false\n---\n"
    )
    (pubs / "PMID_333.md").write_text("---\ntitle: key absent\n---\n")
    return pubs


def test_availability_omits_records_without_the_key(publications):
    """A cache that never recorded availability must not be read as 'unavailable'."""
    availability = cached_full_text_availability(publications)
    assert availability == {"111": True, "222": False}
    assert "333" not in availability


def test_availability_ignores_the_key_beyond_the_frontmatter(tmp_path):
    """The key is only meaningful in frontmatter; full text may quote it in prose."""
    pubs = tmp_path / "publications"
    pubs.mkdir()
    body = (
        "---\ntitle: t\n---\n" + ("filler line\n" * 900) + "full_text_available: true\n"
    )
    (pubs / "PMID_444.md").write_text(body)
    assert cached_full_text_availability(pubs) == {}


def _review(tmp_path, name: str, body: str):
    path = tmp_path / name
    path.write_text(body)
    return path


def test_finds_only_the_contradicted_direction(tmp_path, publications):
    """Flagged-but-available is a defect; the converse and the unflagged case are not."""
    review = _review(
        tmp_path,
        "X-ai-review.yaml",
        """
references:
- id: PMID:111
  title: stale flag, cache has full text
  full_text_unavailable: true
- id: PMID:222
  title: correctly flagged, cache is abstract-only
  full_text_unavailable: true
- id: PMID:111
  title: available and not flagged
- id: PMID:333
  title: availability unknown
  full_text_unavailable: true
""",
    )
    stale = find_stale_flags([review], cached_full_text_availability(publications))
    assert [f.pmid for f in stale] == ["111"]


def test_zero_findings_marks_suppressed_evidence(tmp_path, publications):
    """The signature of the defect is a stale flag on a reference with no findings."""
    review = _review(
        tmp_path,
        "Y-ai-review.yaml",
        """
references:
- id: PMID:111
  title: no findings extracted
  full_text_unavailable: true
""",
    )
    (stale,) = find_stale_flags([review], cached_full_text_availability(publications))
    assert stale.n_findings == 0
    assert stale.suppressed_evidence


def test_findings_present_is_not_flagged_as_suppressed(tmp_path, publications):
    review = _review(
        tmp_path,
        "Z-ai-review.yaml",
        """
references:
- id: PMID:111
  title: findings were extracted anyway
  full_text_unavailable: true
  findings:
  - statement: something
    supporting_text: body
""",
    )
    (stale,) = find_stale_flags([review], cached_full_text_availability(publications))
    assert stale.n_findings == 1
    assert not stale.suppressed_evidence


def test_removal_touches_only_the_named_reference(tmp_path, publications):
    """Editing must not disturb an adjacent reference that is correctly flagged."""
    review = _review(
        tmp_path,
        "W-ai-review.yaml",
        """references:
- id: PMID:111
  title: stale
  full_text_unavailable: true
- id: PMID:222
  title: correct
  full_text_unavailable: true
""",
    )
    assert remove_stale_flags(review, {"111"}) == 1
    text = review.read_text()
    assert "PMID:111\n  title: stale\n" in text
    # The legitimately flagged neighbour keeps its flag.
    assert text.count("full_text_unavailable: true") == 1
    assert "title: correct\n  full_text_unavailable: true" in text
    assert find_stale_flags([review], cached_full_text_availability(publications)) == []


def test_removal_preserves_block_scalars_and_key_order(tmp_path):
    """A line-wise edit must not reformat the rest of the document."""
    original = """references:
- id: PMID:111
  title: keeps formatting
  full_text_unavailable: true
  findings:
  - statement: >-
      a folded block scalar that a yaml round-trip would rewrite
    supporting_text: 'single quoted'
"""
    review = _review(tmp_path, "V-ai-review.yaml", original)
    assert remove_stale_flags(review, {"111"}) == 1
    expected = original.replace("  full_text_unavailable: true\n", "")
    assert review.read_text() == expected


def test_removal_is_a_noop_for_unlisted_pmids(tmp_path):
    original = "references:\n- id: PMID:999\n  full_text_unavailable: true\n"
    review = _review(tmp_path, "U-ai-review.yaml", original)
    assert remove_stale_flags(review, {"111"}) == 0
    assert review.read_text() == original
