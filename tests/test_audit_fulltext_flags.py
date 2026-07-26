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


def test_nested_finding_level_flag_is_not_removed(tmp_path, publications):
    """The mutator must not strip a flag the detector never inspects.

    A first version matched the flag at any indentation until the next `id:` line, so it also
    stripped a Finding-level flag under `findings:` (this happened to genes/MYCTU/clpP2,
    PMID:35507665). `find_stale_flags` only inspects reference-level flags, so the post-fix
    re-check was structurally blind to the over-removal.
    """
    review = _review(
        tmp_path,
        "N-ai-review.yaml",
        """references:
- id: PMID:111
  title: reference-level flag is stale
  full_text_unavailable: true
  findings:
  - statement: a finding carrying its own flag
    full_text_unavailable: true
""",
    )
    assert remove_stale_flags(review, {"111"}) == 1
    text = review.read_text()
    assert "  title: reference-level flag is stale\n  findings:" in text
    # The nested flag, which find_stale_flags never reports, survives.
    assert "    full_text_unavailable: true\n" in text
    assert text.count("full_text_unavailable: true") == 1


def test_reference_id_block_does_not_capture_a_nested_flag(tmp_path):
    """A SupportingTextInReference block is keyed by `reference_id:`, not `id:`.

    If that key reset the current reference, a flag nested under it could be attributed to the
    wrong PMID and removed.
    """
    review = _review(
        tmp_path,
        "R-ai-review.yaml",
        """existing_annotations:
- term:
    id: GO:0000001
  review:
    supported_by:
    - reference_id: PMID:111
      supporting_text: quoted text
      full_text_unavailable: true
references:
- id: PMID:111
  full_text_unavailable: true
""",
    )
    assert remove_stale_flags(review, {"111"}) == 1
    text = review.read_text()
    # The nested one under reference_id: is untouched; only the top-level reference lost its flag.
    assert "      full_text_unavailable: true\n" in text
    assert text.count("full_text_unavailable: true") == 1


def test_audit_returns_nonzero_while_flags_remain_and_zero_after_fix(
    tmp_path, publications
):
    """The exit code is the CI-gate contract, so pin it."""
    from ai_gene_review.tools.audit_fulltext_flags import audit

    genes = tmp_path / "genes" / "human" / "G"
    genes.mkdir(parents=True)
    (genes / "G-ai-review.yaml").write_text(
        "references:\n- id: PMID:111\n  full_text_unavailable: true\n"
    )
    assert audit(tmp_path, fix=False, echo=lambda *_: None) == 1
    assert audit(tmp_path, fix=True, echo=lambda *_: None) == 0
    assert audit(tmp_path, fix=False, echo=lambda *_: None) == 0


def test_audit_raises_when_publications_dir_is_absent(tmp_path):
    from ai_gene_review.tools.audit_fulltext_flags import audit

    with pytest.raises(FileNotFoundError):
        audit(tmp_path, echo=lambda *_: None)


def test_frontmatter_key_found_beyond_a_fixed_byte_window(tmp_path):
    """Parsing the real frontmatter block has no truncation cliff."""
    pubs = tmp_path / "publications"
    pubs.mkdir()
    padding = "\n".join(f"note_{i}: filler value for padding" for i in range(400))
    (pubs / "PMID_555.md").write_text(
        f"---\ntitle: t\n{padding}\nfull_text_available: true\n---\nbody\n"
    )
    assert cached_full_text_availability(pubs) == {"555": True}
