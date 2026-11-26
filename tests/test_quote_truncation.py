"""Tests for :mod:`ai_gene_review.validation.quote_truncation`.

A ``supporting_text`` that ends on a hyphen is usually a quote that was copied
out of a line-wrapped source and cut in the middle of a word. The quote still
passes ``validate-quotes``, because that check collapses whitespace before
matching, so nothing in the corpus notices that the claim lost the very term it
was adduced for (``formation of L-aspartate-`` for aspartate-semialdehyde
dehydrogenase, whose product is L-aspartate-4-semialdehyde).

These tests pin the three cases apart: a cut inside a word on one line, a cut at
a line wrap, and a quote that merely ends at a real hyphenated token boundary.
"""

from __future__ import annotations

import pytest

from ai_gene_review.validation.quote_truncation import (
    CutKind,
    find_truncation,
    scan_document,
)


def test_quote_not_ending_in_hyphen_is_not_a_cut() -> None:
    """A quote that ends on a word is not a truncation candidate."""
    assert find_truncation("formation of L-aspartate-4-semialdehyde", "x") is None


@pytest.mark.parametrize(
    "quote,source,continuation",
    [
        # cut inside a word, source all on one line
        (
            "formation of L-aspartate-",
            "Catalyzes the formation of L-aspartate-4-semialdehyde from L-aspartyl.",
            "4-semialdehyde",
        ),
        # cut inside a word at a line wrap
        (
            "formation of L-aspartate-",
            "Catalyzes the formation of L-aspartate-\n4-semialdehyde from L-aspartyl.",
            "4-semialdehyde",
        ),
        # the quote itself spans a wrap in the source
        (
            "gamma-elimination of phosphate from L-",
            "Catalyzes the gamma-elimination of\nphosphate from L-phosphohomoserine.",
            "phosphohomoserine",
        ),
    ],
)
def test_mid_word_cut_reports_the_completing_token(
    quote: str, source: str, continuation: str
) -> None:
    """The completion is the rest of the cut word, not the rest of the sentence."""
    cut = find_truncation(quote, source)
    assert cut is not None
    assert cut.continuation == continuation
    assert cut.kind is CutKind.MID_WORD


def test_hyphen_followed_by_space_is_a_token_boundary_not_a_mid_word_cut() -> None:
    """``both (R)-`` ends on a real token, so it is reported as a weaker kind.

    The quote is still incomplete as an argument -- the claim is about the
    ``(R)``/``(S)`` pair -- but it is not a word broken in half, and the two
    must not be conflated: only the mid-word case is certainly defective.
    """
    cut = find_truncation(
        "remove glutathione from both (R)-",
        "the only enzyme needed to remove glutathione from both (R)- and (S)-isomers",
    )
    assert cut is not None
    assert cut.kind is CutKind.TOKEN_BOUNDARY
    assert cut.continuation == "and"


def test_quote_absent_from_source_is_not_reported() -> None:
    """No completion can be proposed for a quote this source does not contain.

    Such a quote is ``validate-quotes``' business, not this check's; reporting it
    here would claim a truncation on evidence that does not exist.
    """
    assert (
        find_truncation("not in the source-", "an unrelated sentence entirely") is None
    )


def test_quote_running_to_the_end_of_the_source_has_no_completion() -> None:
    """A hyphen with nothing after it in the source cannot be completed."""
    assert (
        find_truncation("ends on a hyphen-", "a sentence that ends on a hyphen-")
        is None
    )


def test_whitespace_collapse_matches_the_quote_checker() -> None:
    """Matching ignores how the source wraps, as ``supporting_text`` does.

    Otherwise this check would disagree with ``validate-quotes`` about whether a
    quote is in its source at all.
    """
    cut = find_truncation(
        "responsible for mono-",
        "G9a and GLP are   responsible\n\tfor mono-methylation of H3K9.",
    )
    assert cut is not None
    assert cut.continuation == "methylation"


def test_trailing_whitespace_and_quotes_do_not_hide_a_cut() -> None:
    """A quote stored with trailing space still ends on its hyphen."""
    cut = find_truncation(
        "both the light-  ", "responsible for both the light-induced step"
    )
    assert cut is not None
    assert cut.kind is CutKind.MID_WORD
    assert cut.continuation == "induced"


def test_scan_document_finds_a_cut_against_a_cached_publication(tmp_path) -> None:
    """End-to-end on real files: a YAML quote checked against a cached abstract.

    No mocks -- the scanner resolves the source the same way ``validate-quotes``
    does, so a test that stubbed resolution would not tell us it works.
    """
    (tmp_path / "publications").mkdir()
    (tmp_path / "publications" / "PMID_1825082.md").write_text(
        "# A paper\n\nStressed cells accumulate trehalose by a futile cycle involving\n"
        "overproduction, excretion, and degradation to glucose, which is re-\n"
        "utilized by the cell.\n"
    )
    doc = tmp_path / "x-ai-review.yaml"
    doc.write_text(
        "id: P0A000\n"
        "existing_annotations:\n"
        "  - term: {id: 'GO:0071474', label: cellular hyperosmotic response}\n"
        "    review:\n"
        "      supported_by:\n"
        "        - reference_id: PMID:1825082\n"
        "          supporting_text: 'degradation to glucose, which is re-'\n"
    )
    findings = scan_document(doc, project_root=tmp_path)
    assert len(findings) == 1
    assert findings[0].reference_id == "PMID:1825082"
    assert findings[0].truncation.continuation == "utilized"
    assert findings[0].truncation.kind is CutKind.MID_WORD


def test_scan_document_ignores_an_unresolvable_source(tmp_path) -> None:
    """A quote whose source is not cached is reported by neither check.

    Claiming a truncation here would assert something about text we never read.
    """
    (tmp_path / "publications").mkdir()
    doc = tmp_path / "y-ai-review.yaml"
    doc.write_text(
        "id: P0A000\n"
        "references:\n"
        "  - id: PMID:9999999\n"
        "    supporting_text: 'a quote ending in a hyphen-'\n"
    )
    assert scan_document(doc, project_root=tmp_path) == []


def test_uniprot_line_code_is_not_offered_as_the_completion(tmp_path) -> None:
    """A quote wrapped inside a ``CC`` block is completed by the record, not the margin.

    Regression: the first corpus run proposed ``formation of L-aspartate-CC``,
    because the continuation line of a UniProt flat file begins with the file's
    two-letter line code. The real product is L-aspartate-semialdehyde.
    """
    genes = tmp_path / "genes" / "ECOLI" / "asd"
    genes.mkdir(parents=True)
    (genes / "asd-uniprot.txt").write_text(
        "ID   ASD_ECOLI               Reviewed;         367 AA.\n"
        "CC   -!- FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate-\n"
        "CC       semialdehyde (L-ASA) by the reductive dephosphorylation.\n"
    )
    doc = tmp_path / "asd-ai-review.yaml"
    doc.write_text(
        "id: P0A9Q9\n"
        "references:\n"
        "  - id: file:ECOLI/asd/asd-uniprot.txt\n"
        "    supporting_text: 'NADPH-dependent formation of L-aspartate-'\n"
    )
    findings = scan_document(doc, project_root=tmp_path)
    assert len(findings) == 1
    assert findings[0].truncation.continuation == "semialdehyde"
    assert findings[0].truncation.completed.endswith("L-aspartate-semialdehyde")


def test_folding_matches_a_quote_written_with_an_en_dash(tmp_path) -> None:
    """A quote re-typed with a unicode dash still finds its source."""
    (tmp_path / "publications").mkdir()
    (tmp_path / "publications" / "PMID_1.md").write_text(
        "the light-induced step was measured"
    )
    doc = tmp_path / "z-ai-review.yaml"
    doc.write_text(
        "id: P0\nreferences:\n  - id: PMID:1\n    supporting_text: 'the light‐'\n"
    )
    findings = scan_document(doc, project_root=tmp_path)
    assert len(findings) == 1
    assert findings[0].truncation.continuation == "induced"


@pytest.mark.parametrize("conjunction", ["and", "or", "nor"])
def test_suspended_hyphen_is_a_token_boundary_however_the_source_wraps(
    conjunction: str,
) -> None:
    """``in a CTP- and Mg2+-dependent manner`` holds a real hyphen, not a broken word.

    A suspended hyphen is correct English, so the quote ends on a whole token
    whatever the source does at that point. Without this, the class depended on
    where the source file happened to wrap: the TAM41 and ALG11 quotes are the
    same construction and were classified differently for that reason alone.
    """
    wrapped = (
        f"converted NBD-PA to CDP-DAG in a CTP-\n  {conjunction} Mg2+-dependent manner"
    )
    cut = find_truncation("to CDP-DAG in a CTP-", wrapped)
    assert cut is not None
    assert cut.kind is CutKind.TOKEN_BOUNDARY
    assert cut.continuation == conjunction


def test_a_wrapped_word_beginning_with_an_is_still_mid_word() -> None:
    """The conjunction rule keys on the whole token, not a prefix of it.

    ``andro-`` must not read as ``and``.
    """
    cut = find_truncation(
        "levels of andro-", "levels of andro-\nstenedione were measured"
    )
    assert cut is not None
    assert cut.kind is CutKind.MID_WORD
    assert cut.continuation == "stenedione"
