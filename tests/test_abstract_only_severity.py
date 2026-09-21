"""An unverifiable quote must not pass silently just because the cache lacks full text.

``validate_reference_finding_supporting_text`` used to downgrade a non-matching quote to a
WARNING on *either* of two conditions: the author declared ``full_text_unavailable``, or
the cached publication happened to be abstract-only. Those are very different situations.
The first is an acknowledged limitation. The second is silent -- a load-bearing claim can
rest on a quote nobody can check, and nothing distinguishes it from a verified one.

Splitting them keeps the warning for the declared case and makes the undeclared case an
error the author can actually act on: fix the quote, or say the text is not cached.
"""

from pathlib import Path

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


def findings_doc(quote: str, *, declared_on_reference=False, declared_on_finding=False):
    finding = {"statement": "s", "supporting_text": quote}
    if declared_on_finding:
        finding["full_text_unavailable"] = True
    reference = {"id": "PMID:1", "findings": [finding]}
    if declared_on_reference:
        reference["full_text_unavailable"] = True
    return {"references": [reference]}


def severities(doc, pubs) -> list[ValidationSeverity]:
    report = ValidationReport(file_path="t.yaml", is_valid=True)
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
def test_declared_unavailable_stays_a_warning(abstract_only_cache, where):
    """An acknowledged limitation must not block: the text genuinely is not cached."""
    doc = findings_doc(
        "a sentence that is not in the abstract",
        declared_on_reference=(where == "reference"),
        declared_on_finding=(where == "finding"),
    )
    assert severities(doc, abstract_only_cache) == [ValidationSeverity.WARNING]


def test_a_quote_present_in_the_abstract_is_silent(abstract_only_cache):
    """Abstract-only is not itself a defect -- most such quotes verify normally."""
    doc = findings_doc("the protein localises to the nucleus")
    assert severities(doc, abstract_only_cache) == []


def test_error_message_names_the_missing_declaration(abstract_only_cache):
    """The message has to say which of the two remedies is available."""
    report = ValidationReport(file_path="t.yaml", is_valid=True)
    validate_reference_finding_supporting_text(
        findings_doc("not in the abstract at all"), report, abstract_only_cache
    )
    (issue,) = [i for i in report.issues if i.check_type == "reference_finding_supporting_text"]
    assert "does not declare" in issue.message
    assert "full_text_unavailable" in (issue.suggestion or "")
