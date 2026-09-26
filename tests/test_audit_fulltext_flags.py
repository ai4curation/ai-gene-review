"""Tests for the ``full_text_unavailable`` flag audit."""

from __future__ import annotations

import pytest

from ai_gene_review.tools.audit_fulltext_flags import (
    cached_full_text_availability,
    find_stale_flags,
    find_unaudited_flags,
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


# --- flags the reference-level PMID audit cannot see -------------------------------------
#
# ESL1 carried two finding-level flags under `file:yeast/ESL1/ESL1-uniprot.txt`, both quotes
# verbatim in that very file. `find_stale_flags` reads reference-level keys on `PMID:` ids
# only, so it scored them as clean; `cached_full_text_available` returns None (not False)
# for a non-literature prefix, so a separate audit scored them as accurate too.


def _unaudited_review(tmp_path, body: str):
    d = tmp_path / "genes" / "yeast" / "X"
    d.mkdir(parents=True, exist_ok=True)
    f = d / "X-ai-review.yaml"
    f.write_text(body)
    return f


def test_finding_level_flag_on_a_repo_file_is_reported(tmp_path, publications):
    """The ESL1 shape: flag on a findings[] entry, source checked into the repo."""
    src = tmp_path / "genes" / "yeast" / "X" / "X-uniprot.txt"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text("Present with 504 molecules/cell in log phase SD medium.\n")
    review = _unaudited_review(
        tmp_path,
        "references:\n"
        "- id: file:yeast/X/X-uniprot.txt\n"
        "  findings:\n"
        "  - statement: s\n"
        "    supporting_text: Present with 504 molecules/cell in log phase SD medium.\n"
        "    full_text_unavailable: true\n",
    )
    availability = cached_full_text_availability(publications)
    assert find_stale_flags([review], availability) == [], "precondition: the old audit is blind to it"

    (flag,) = find_unaudited_flags([review], availability, tmp_path)
    assert flag.finding_index == 0
    assert flag.reference_id == "file:yeast/X/X-uniprot.txt"
    assert "source file is in the repo" in flag.reason


def test_finding_level_flag_contradicted_by_the_cache_is_reported(tmp_path, publications):
    """Same blind spot, literature reference: the cache says full text is there."""
    review = _unaudited_review(
        tmp_path,
        "references:\n- id: PMID:111\n  findings:\n  - statement: s\n"
        "    full_text_unavailable: true\n",
    )
    availability = cached_full_text_availability(publications)
    assert find_stale_flags([review], availability) == []
    (flag,) = find_unaudited_flags([review], availability, tmp_path)
    assert flag.finding_index == 0
    assert "cached publication reports full text" in flag.reason


def test_an_accurate_finding_level_flag_is_not_reported(tmp_path, publications):
    """A flag on a genuinely abstract-only record is correct and must stay quiet.

    This is what keeps the check readable: 30 such flags sit in one PR's changed files, and
    an audit that reports all of them is an audit nobody reads.
    """
    review = _unaudited_review(
        tmp_path,
        "references:\n- id: PMID:222\n  findings:\n  - statement: s\n"
        "    full_text_unavailable: true\n",
    )
    assert find_unaudited_flags([review], cached_full_text_availability(publications), tmp_path) == []


def test_reference_level_file_flag_is_reported(tmp_path, publications):
    """The reference-level half of the same gap."""
    src = tmp_path / "genes" / "yeast" / "X" / "X-uniprot.txt"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text("some record text\n")
    review = _unaudited_review(
        tmp_path,
        "references:\n- id: file:yeast/X/X-uniprot.txt\n"
        "  full_text_unavailable: true\n  findings: []\n",
    )
    (flag,) = find_unaudited_flags([review], cached_full_text_availability(publications), tmp_path)
    assert flag.finding_index is None


def test_a_missing_repo_file_is_not_reported(tmp_path, publications):
    """A file: reference whose source is absent is genuinely uncached -- the flag is true."""
    review = _unaudited_review(
        tmp_path,
        "references:\n- id: file:yeast/X/does-not-exist.txt\n"
        "  full_text_unavailable: true\n  findings: []\n",
    )
    assert find_unaudited_flags([review], cached_full_text_availability(publications), tmp_path) == []


def test_fix_exits_nonzero_when_unaudited_flags_remain(tmp_path, publications, monkeypatch):
    """--fix removes what it can and must still fail on what it cannot.

    It previously printed "remove by hand, --fix does not touch these" and then returned 0,
    so a CI gate reading the exit code saw a clean run while the output named the flags that
    were not clean.
    """
    from ai_gene_review.tools.audit_fulltext_flags import audit

    (tmp_path / "publications").mkdir(exist_ok=True)
    for src in publications.glob("*.md"):
        (tmp_path / "publications" / src.name).write_text(src.read_text())
    genes = tmp_path / "genes" / "yeast" / "X"
    genes.mkdir(parents=True)
    (genes / "X-uniprot.txt").write_text("some record text\n")
    # Both kinds at once. That combination is the failing path: the early return already
    # gives 1 when there is nothing for --fix to remove, so a test with only an unaudited
    # flag passes without touching the code under test -- which is how this test first
    # passed its exit-code assertion while the message assertion failed.
    (genes / "X-ai-review.yaml").write_text(
        "references:\n"
        "- id: PMID:111\n"          # cache says full text -> stale, --fix removes it
        "  full_text_unavailable: true\n"
        "  findings: []\n"
        "- id: file:yeast/X/X-uniprot.txt\n"   # outside --fix's scope
        "  findings:\n"
        "  - statement: s\n    full_text_unavailable: true\n"
    )
    lines: list[str] = []
    rc = audit(tmp_path, fix=True, echo=lines.append)
    assert rc == 1, "a --fix run that leaves flags behind must not report success"
    assert any("outside --fix's scope remain" in line for line in lines)


def test_scope_mismatch_is_still_reported_when_unaudited_flags_exist(tmp_path, publications, monkeypatch):
    """The scope guard must print even when --fix has flags outside its scope.

    The first version of the unaudited block returned as soon as `unaudited` was non-empty,
    which is the normal state. A --fix run that under-removed then exited 1 -- the right code
    -- with no ERROR line, silently skipping the guard whose whole purpose is to catch a flag
    being stripped without being reported. The previous test could not see this: its fixture
    removed exactly the one stale flag it created, so both guards would have passed anyway.
    """
    from ai_gene_review.tools import audit_fulltext_flags as mod

    (tmp_path / "publications").mkdir(exist_ok=True)
    for src in publications.glob("*.md"):
        (tmp_path / "publications" / src.name).write_text(src.read_text())
    genes = tmp_path / "genes" / "yeast" / "X"
    genes.mkdir(parents=True)
    (genes / "X-uniprot.txt").write_text("some record text\n")
    (genes / "X-ai-review.yaml").write_text(
        "references:\n"
        "- id: PMID:111\n  full_text_unavailable: true\n  findings: []\n"
        "- id: file:yeast/X/X-uniprot.txt\n  findings:\n"
        "  - statement: s\n    full_text_unavailable: true\n"
    )
    # Force the mutator to under-remove, which is exactly what the scope guard exists for.
    monkeypatch.setattr(mod, "remove_stale_flags", lambda review_path, pmids: 0)

    lines: list[str] = []
    rc = mod.audit(tmp_path, fix=True, echo=lines.append)
    assert rc == 1
    assert any("scope mismatch" in line for line in lines), (
        "the scope guard must report even when unaudited flags are also present"
    )
    assert any("outside --fix's scope remain" in line for line in lines)


def test_availability_falls_back_to_content_type(tmp_path):
    """The audit and the validator must agree about what "has full text" means.

    The audit used to skip any record lacking ``full_text_available`` -- 1138 of them, at
    least 242 naming a full-text ``content_type`` -- so it and ``supporting_text`` disagreed
    by construction, and the audit's half is the one that hides a false flag. The live case:
    ``PMID:38296963`` (``content_type: full_text_pdf``, gold OA) carried the identical
    reference-level flag on ARL8A and ARL8B; the ARL8B one was removed by hand as the "one
    genuinely false declaration" and the ARL8A one was invisible here.
    """
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_1.md").write_text("---\ntitle: t\ncontent_type: full_text_pdf\n---\nbody\n")
    (pubs / "PMID_2.md").write_text("---\ntitle: t\ncontent_type: abstract_only\n---\nbody\n")
    (pubs / "PMID_3.md").write_text("---\ntitle: t\ncontent_type: full_text_xml\n---\nbody\n")
    (pubs / "PMID_4.md").write_text("---\ntitle: t\n---\nbody\n")  # neither key

    av = cached_full_text_availability(pubs)
    assert av["1"] is True, "full_text_pdf means full text"
    assert av["2"] is False
    assert av["3"] is True, "full_text_xml was the value the old allow-list dropped"
    assert "4" not in av, "no signal at all must still be absent, not guessed"


def test_explicit_full_text_available_wins_over_content_type(tmp_path):
    """The explicit key is authoritative; the fallback only applies when it is absent."""
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_1.md").write_text(
        "---\ntitle: t\nfull_text_available: false\ncontent_type: full_text_pdf\n---\nbody\n"
    )
    assert cached_full_text_availability(pubs)["1"] is False


def test_a_content_type_only_record_can_make_a_flag_stale(tmp_path, monkeypatch):
    """End to end: the ARL8A shape is now reported."""
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_38296963.md").write_text(
        "---\ntitle: t\ncontent_type: full_text_pdf\noa_status: gold\n---\nbody\n"
    )
    genes = tmp_path / "genes" / "human" / "X"
    genes.mkdir(parents=True)
    review = genes / "X-ai-review.yaml"
    review.write_text(
        "references:\n- id: PMID:38296963\n  full_text_unavailable: true\n  findings: []\n"
    )
    (stale,) = find_stale_flags([review], cached_full_text_availability(pubs))
    assert stale.pmid == "38296963"
    assert stale.suppressed_evidence, "zero findings is the signature the module documents"


def test_only_records_with_neither_key_are_absent(tmp_path):
    """Pin the docstring's contract, which drifted the moment the function widened.

    The opening sentence promised that omitting ``full_text_available`` was enough to be
    excluded. Widening removed that property and the sentence stayed, fifteen lines above
    the code contradicting it. Now only a record with neither key is absent, and this test
    fails if either half changes without the other.
    """
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_1.md").write_text("---\ntitle: t\nfull_text_available: true\n---\nbody\n")
    (pubs / "PMID_2.md").write_text("---\ntitle: t\ncontent_type: full_text_xml\n---\nbody\n")
    (pubs / "PMID_3.md").write_text("---\ntitle: t\n---\nbody\n")

    av = cached_full_text_availability(pubs)
    assert set(av) == {"1", "2"}, "only the record with neither key is absent"
    assert "3" not in av
