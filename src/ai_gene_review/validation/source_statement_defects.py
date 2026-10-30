"""Check that statement defects quote the source text they report.

A ``WRONG_STATEMENT`` or ``OUTDATED_STATEMENT`` source defect on a reference
(``references[].reference_review.source_defects``) reports a sentence in that
reference's own text: a MOD gene description cited as its
``-deep-research-<mod>.md`` file, or a UniProt comment cited as the
``-uniprot.txt`` file. Its ``asserted_value`` is that sentence, verbatim, so the
report can show the resource exactly what to revise and a later re-fetch can
show whether it changed. This check warns when the value is not found in the
cited file (for example a record id, or a paraphrase). Matching uses the same
normalisation as supporting-text quotes. ``MISSING_STATEMENT`` reports an
omission, so its ``asserted_value`` names the record and is not checked.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator, Tuple

from ai_gene_review.validation.local_source_text import (
    PROJECT_ROOT,
    quote_matches,
    resolve_local_source,
)
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

STATEMENT_DEFECT_CHECK = "statement_defect_not_in_source"
QUOTED_TYPES = ("WRONG_STATEMENT", "OUTDATED_STATEMENT")


def iter_statement_defects(data: Any) -> Iterator[Tuple[str, str, dict]]:
    """Yield ``(path, reference_id, defect)`` for quoted statement defects on references.

    >>> data = {"references": [{"id": "file:x.md", "reference_review": {"source_defects": [
    ...     {"defect_type": "WRONG_STATEMENT", "asserted_value": "a"},
    ...     {"defect_type": "MISSING_STATEMENT", "asserted_value": "WB:1"}]}}]}
    >>> [(p, r) for p, r, _ in iter_statement_defects(data)]
    [('references[0].reference_review.source_defects[0]', 'file:x.md')]
    """
    if not isinstance(data, dict):
        return
    for i, ref in enumerate(data.get("references") or []):
        if not isinstance(ref, dict):
            continue
        review = ref.get("reference_review") or {}
        for j, defect in enumerate(review.get("source_defects") or []):
            if isinstance(defect, dict) and defect.get("defect_type") in QUOTED_TYPES:
                yield f"references[{i}].reference_review.source_defects[{j}]", str(ref.get("id", "")), defect


def validate_statement_defects(
    data: Any, report: ValidationReport, project_root: Path = PROJECT_ROOT
) -> None:
    """Warn when a quoted statement defect's asserted_value is not in the cited source file."""
    for path, ref_id, defect in iter_statement_defects(data):
        value = str(defect.get("asserted_value") or "")
        source = resolve_local_source(ref_id, project_root)
        if source is None:
            message = f"Statement defect on {ref_id} cannot be checked: the reference is not a local source file"
        elif value and quote_matches(value, source):
            continue
        else:
            message = f"Statement defect asserted_value is not found verbatim in {ref_id}: {value[:80]!r}"
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=f"{path}.asserted_value",
            suggestion=(
                "Set asserted_value to the offending sentence copied from the cited source text "
                "(see docs/source_defects.md, 'Cited source text')"
            ),
            validation_category="BestPractices",
            check_type=STATEMENT_DEFECT_CHECK,
        )
