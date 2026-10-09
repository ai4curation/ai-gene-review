"""A snippet must be deterministically checkable against the cache; a mismatch is an error.

``validate_reference_finding_supporting_text`` used to downgrade a non-matching quote to a
WARNING whenever the author declared ``full_text_unavailable``, whenever the cached record
was abstract-only, or whenever the check itself raised. Each of those made an *unverified*
quote indistinguishable from a *verified* one -- which is the only distinction this check
exists to draw.

There is now no downgrade path. ``full_text_unavailable`` remains meaningful as metadata
about the cached record, but declaring that you cannot check a quote is not the same as
checking it, so it no longer excuses a mismatch.
"""

from pathlib import Path
from typing import Any

from types import SimpleNamespace

import pytest

from ai_gene_review.validation.validation_report import ValidationReport, ValidationSeverity
from ai_gene_review.validation.validator import (
    validate_reference_finding_supporting_text,
)


@pytest.fixture
def abstract_only_cache(tmp_path: Path) -> Path:
    """A publications cache whose single record carries only an abstract."""
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_1.md").write_text(
        "---\npmid: '1'\ntitle: A paper\nfull_text_available: false\n---\n\n"
        "# A paper\n\nThe abstract says the protein localises to the nucleus.\n"
    )
    return pubs


def findings_doc(
    quote: str,
    *,
    declared_on_reference: bool = False,
    declared_on_finding: bool = False,
) -> dict[str, Any]:
    finding: dict[str, Any] = {"statement": "s", "supporting_text": quote}
    if declared_on_finding:
        finding["full_text_unavailable"] = True
    reference: dict[str, Any] = {"id": "PMID:1", "findings": [finding]}
    if declared_on_reference:
        reference["full_text_unavailable"] = True
    return {"references": [reference]}


def severities(doc: dict[str, Any], pubs: Path) -> list[ValidationSeverity]:
    report = ValidationReport(file_path=Path("t.yaml"), is_valid=True)
    validate_reference_finding_supporting_text(doc, report, pubs)
    return [
        i.severity
        for i in report.issues
        if i.check_type == "reference_finding_supporting_text"
    ]


def test_undeclared_unverifiable_quote_is_an_error(abstract_only_cache):
    """The silent case: nothing declared, quote not in the abstract."""
    got = severities(findings_doc("a sentence that is not in the abstract"), abstract_only_cache)
    assert got == [ValidationSeverity.ERROR]


@pytest.mark.parametrize("where", ["reference", "finding"])
def test_declaring_unavailable_does_not_excuse_a_mismatch(abstract_only_cache, where):
    """The escape hatch is gone: a declaration is not a check.

    This reverses the previous behaviour deliberately. Allowing the flag to downgrade a
    mismatch meant an author could silence the one signal that distinguishes a verified
    quote from an unverified one, by asserting the very thing that makes it unverifiable.
    """
    doc = findings_doc(
        "a sentence that is not in the abstract",
        declared_on_reference=(where == "reference"),
        declared_on_finding=(where == "finding"),
    )
    assert severities(doc, abstract_only_cache) == [ValidationSeverity.ERROR]


def test_a_check_that_raises_is_an_error_not_a_pass(abstract_only_cache, monkeypatch):
    """A crash while checking must not let the snippet through.

    Downgrading here would skip validation for reasons unrelated to whether the quote is
    correct, which is exactly what the rule forbids.
    """
    import ai_gene_review.validation.validator as v

    class Boom:
        def validate(self, *a, **k):
            raise RuntimeError("cache unreadable")

    monkeypatch.setattr(
        v, "build_supporting_text_validator", lambda d=None: (Boom(), abstract_only_cache)
    )
    doc = findings_doc("anything at all")
    assert severities(doc, abstract_only_cache) == [ValidationSeverity.ERROR]


def test_a_quote_present_in_the_abstract_is_silent(abstract_only_cache):
    """Abstract-only is not itself a defect -- most such quotes verify normally."""
    doc = findings_doc("the protein localises to the nucleus")
    assert severities(doc, abstract_only_cache) == []


def test_error_message_offers_a_real_remedy(abstract_only_cache):
    """The remedies must be things that actually make the quote checkable.

    Declaring ``full_text_unavailable`` is no longer one of them, so the message must not
    suggest it -- that would send an author to a flag that no longer resolves the error.
    """
    report = ValidationReport(file_path=Path("t.yaml"), is_valid=True)
    validate_reference_finding_supporting_text(
        findings_doc("not in the abstract at all"), report, abstract_only_cache
    )
    (issue,) = [i for i in report.issues if i.check_type == "reference_finding_supporting_text"]
    suggestion = issue.suggestion or ""
    assert "abstract-only cache" in issue.message
    assert "full text into the cache" in suggestion
    assert "full_text_unavailable" not in suggestion


@pytest.fixture
def stub_cache(tmp_path: Path) -> Path:
    """A cached record that has neither full text nor an abstract body.

    Six of these existed in the repository, each written by a failed metadata fetch:
    ``authors: []`` and a body of "Cached metadata for local validation.". They are not
    abstract-only papers -- they are broken records.
    """
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_2.md").write_text(
        "---\npmid: '2'\ntitle: A stub\nauthors: []\nfull_text_available: false\n"
        "full_text_attempted: true\n---\n\n# A stub\n\n## Abstract\n\n"
        "Cached metadata for local validation.\n"
    )
    return pubs


def _issue(doc, pubs):
    report = ValidationReport(file_path=Path("t.yaml"), is_valid=True)
    validate_reference_finding_supporting_text(doc, report, pubs)
    (issue,) = [
        i for i in report.issues if i.check_type == "reference_finding_supporting_text"
    ]
    return issue


def test_a_bodyless_stub_does_not_get_impossible_advice(stub_cache):
    """"Quote the cached abstract" is not a remedy when there is no abstract.

    The old message sent an author to text that does not exist. The real fault is a failed
    metadata fetch, and the fix is ``cache_publication(pmid, force=True)`` -- which re-fetches
    by PMID regardless of ``full_text_attempted``. Doing exactly that to the six stubs in this
    repository recovered full text for three of them and real abstracts for the rest, which
    turned two deleted quotes on wspR back into verifiable ones.
    """
    doc: dict[str, Any] = {
        "references": [{"id": "PMID:2", "findings": [{"statement": "s", "supporting_text": "anything"}]}]
    }
    issue = _issue(doc, stub_cache)
    assert issue.severity == ValidationSeverity.ERROR
    assert "no abstract or full-text body" in issue.message
    suggestion = issue.suggestion or ""
    assert "force=True" in suggestion
    assert "cached abstract" not in suggestion, "the impossible advice must not appear here"


def test_an_abstract_only_record_keeps_the_ordinary_advice(abstract_only_cache):
    """The discriminator has to be narrow: a real abstract still gets the quote-it advice."""
    doc: dict[str, Any] = {
        "references": [
            {"id": "PMID:1", "findings": [{"statement": "s", "supporting_text": "not in there"}]}
        ]
    }
    issue = _issue(doc, abstract_only_cache)
    assert "abstract-only cache" in issue.message
    assert "quote a verbatim substring of the cached abstract" in (issue.suggestion or "").lower()


def test_a_full_text_record_gets_the_verbatim_substring_message(tmp_path: Path):
    """The third branch, which no test pinned.

    When the cache *has* full text, a mismatch is neither "unfetchable" nor "abstract-only" --
    it is simply not a substring, and the message must say so rather than blaming cache state
    the author could fix.
    """
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_3.md").write_text(
        "---\npmid: '3'\ntitle: Full paper\nfull_text_available: true\n---\n\n"
        "# Full paper\n\n## Full Text\n\nThe protein localises to the nucleus in all conditions.\n"
    )
    doc: dict[str, Any] = {
        "references": [
            {"id": "PMID:3", "findings": [{"statement": "s", "supporting_text": "a sentence nobody wrote"}]}
        ]
    }
    issue = _issue(doc, pubs)
    assert issue.severity == ValidationSeverity.ERROR
    assert "not a verbatim publication substring" in issue.message
    assert "exact substring from the cached publication" in (issue.suggestion or "")


def test_an_uncached_reference_does_not_get_impossible_advice(tmp_path: Path, monkeypatch):
    """The impossible advice survived one case over: nothing cached at all.

    A missing cache file used to fall through to "an exact substring from the cached
    publication", which is not a thing that exists here.

    The validator is stubbed rather than real, for two reasons found the hard way. The first
    version of this test used ``PMID:404`` against an empty directory -- and PMID:404 is a
    real 1975 PubMed record, so the live validator **fetched and cached it**, leaving the
    reference cached, the branch unreached and the test asserting nothing. It also made a
    network call from a unit test. A stub makes the uncached state actually hold.
    """
    import ai_gene_review.validation.validator as v

    pubs = tmp_path / "publications"
    pubs.mkdir()

    class Mismatch:
        def validate(self, supporting_text, reference_id):
            return SimpleNamespace(
                is_valid=False, message="Text part not found as substring: 'anything'"
            )

    monkeypatch.setattr(v, "build_supporting_text_validator", lambda d=None: (Mismatch(), pubs))
    doc: dict[str, Any] = {
        "references": [
            {"id": "PMID:99999999", "findings": [{"statement": "s", "supporting_text": "anything"}]}
        ]
    }
    issue = _issue(doc, pubs)
    assert issue.severity == ValidationSeverity.ERROR
    assert "no cached publication" in issue.message
    suggestion = issue.suggestion or ""
    assert "from the cached publication" not in suggestion, "no cached publication exists"
    assert "Cache the publication first" in suggestion


def test_clear_publication_caches_clears_all_three(tmp_path: Path):
    """The documented trap needs a closed loop, not just a note.

    These three predicates are ``lru_cache``d filesystem reads with no invalidation, so a
    repair workflow that calls ``cache_publication(pmid, force=True)`` and re-validates in
    the same process reads the pre-repair answer. Exactly that sequence repaired six stub
    records here and only escaped the trap because the steps ran as separate processes.

    Asserts the helper clears **all three** -- adding a fourth predicate and forgetting it
    is the obvious next version of this bug.
    """
    from ai_gene_review.validation.supporting_text import (
        cached_full_text_available,
        cached_record_has_no_body,
        cached_text_missing,
        clear_publication_caches,
    )

    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_7.md").write_text(
        "---\npmid: '7'\ntitle: t\nfull_text_available: false\n---\n\n# t\n\n"
        "## Abstract\n\nCached metadata for local validation.\n"
    )
    predicates = (cached_full_text_available, cached_record_has_no_body, cached_text_missing)

    assert cached_full_text_available("PMID:7", pubs) is False
    assert cached_record_has_no_body("PMID:7", pubs) is True
    assert cached_text_missing("PMID:7", pubs) is False
    assert all(f.cache_info().currsize > 0 for f in predicates), "precondition: all warm"

    clear_publication_caches()
    assert all(f.cache_info().currsize == 0 for f in predicates)

    # and the cleared cache actually re-reads: repair the stub, ask again
    (pubs / "PMID_7.md").write_text(
        "---\npmid: '7'\ntitle: t\nfull_text_available: true\n---\n\n# t\n\n"
        "## Full Text\n\nA real body with enough prose to count as content.\n"
    )
    assert cached_full_text_available("PMID:7", pubs) is True, "stale read after clear"
    assert cached_record_has_no_body("PMID:7", pubs) is False
