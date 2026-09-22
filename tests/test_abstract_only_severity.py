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
