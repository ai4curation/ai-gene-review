"""Check the PAINT losses declared on gene-review rows against the local PAINT slices.

A row's ``review.propagation_review.paint_losses`` says that a PAINT IRD or IKR at a
node now blocks the row's term on the gene's lineage. That is checkable against the
family's ``interpro/panther/<PTHR>/<PTHR>-paint.tsv``: the node must carry a loss row
for the same term, with the declared evidence code. Families without a local slice
cannot be checked and are skipped; a mismatch is a warning, since a slice can lag
the PAINT release the review was written against.
"""

from __future__ import annotations

from typing import Any

from ai_gene_review.validation.module_validator import PaintIndex
from ai_gene_review.validation.validation_report import ValidationReport, ValidationSeverity

LOSS_CODES = ("IRD", "IKR")


def loss_problem(node: str, term: str, evidence: str, paint_index: PaintIndex) -> str | None:
    """Why a declared loss disagrees with the local PAINT rows, or None if it agrees.

    Returns None as well when the node has no local rows at all (nothing to check).
    """
    rows = paint_index.get(node, [])
    if not rows:
        return None
    losses = [r for r in rows if r.go_id == term and (r.negated or r.evidence in LOSS_CODES)]
    if not losses:
        return f"{node} has no IRD/IKR loss of {term} in the local paint.tsv"
    codes = sorted({r.evidence for r in losses})
    if evidence not in codes:
        return f"{node} records {'/'.join(codes)}, not {evidence}, for {term}"
    return None


def check_paint_losses(data: dict[str, Any], report: ValidationReport, paint_index: PaintIndex) -> None:
    """Warn on declared PAINT losses that the local paint.tsv does not record."""
    for i, annotation in enumerate(data.get("existing_annotations") or []):
        if not isinstance(annotation, dict):
            continue
        prop = ((annotation.get("review") or {}).get("propagation_review") or {})
        term = (annotation.get("term") or {}).get("id", "")
        for j, loss in enumerate(prop.get("paint_losses") or []):
            problem = loss_problem(str(loss.get("node_id", "")), term, str(loss.get("evidence", "")), paint_index)
            if problem:
                report.add_issue(
                    ValidationSeverity.WARNING,
                    f"Declared PAINT loss does not match PAINT: {problem}",
                    path=f"existing_annotations[{i}].review.propagation_review.paint_losses[{j}]",
                    suggestion="Run `just paint-losses <org> <GENE>` and copy the node, code and date it lists",
                    validation_category="BestPractices",
                    check_type="paint_loss_mismatch",
                )


def has_paint_losses(data: dict[str, Any]) -> bool:
    """True when any row declares a PAINT loss (so the PAINT index is worth loading).

    >>> has_paint_losses({"existing_annotations": [{"review": {"propagation_review": {"paint_losses": [{}]}}}]})
    True
    >>> has_paint_losses({"existing_annotations": [{"review": {}}]})
    False
    """
    return any(
        ((a.get("review") or {}).get("propagation_review") or {}).get("paint_losses")
        for a in data.get("existing_annotations") or []
        if isinstance(a, dict)
    )
