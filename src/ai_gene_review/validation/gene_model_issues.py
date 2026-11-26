"""Best-practice checks for curated gene model issues (fused, split, truncated models)."""

from typing import Any

from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)


def _reversed(segment: object) -> bool:
    """True for a well-formed ``start-end`` range whose start is after its end.

    >>> _reversed("650-1"), _reversed("1-650"), _reversed("650"), _reversed(None)
    (True, False, False, False)
    """
    if not isinstance(segment, str) or "-" not in segment:
        return False
    start, _, end = segment.partition("-")
    return start.isdigit() and end.isdigit() and int(start) > int(end)


def validate_gene_model_issues(
    data: dict[str, Any], report: ValidationReport
) -> None:
    """Warn when a gene model issue is unsupported or overstates its status.

    Every issue should quote its evidence. ``CONFIRMED`` means independent lines
    of evidence (the enum's own definition), so it needs at least two distinct
    ``evidence_types``. Residue ranges must run start to end. This checks the
    shape of the curator's argument, not whether the gene model is really wrong.
    """

    def warn(message: str, path: str, check_type: str, suggestion: str) -> None:
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=path,
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type=check_type,
        )

    for i, issue in enumerate(data.get("gene_model_issues") or []):
        path = f"gene_model_issues[{i}]"
        if not issue.get("supported_by"):
            warn(
                "Gene model issue has no supporting quotes",
                path + ".supported_by",
                "gene_model_issue_unsupported",
                "Quote the analysis or record that shows the gene model problem",
            )
        kinds = set(issue.get("evidence_types") or [])
        if issue.get("status") == "CONFIRMED" and len(kinds) < 2:
            warn(
                "CONFIRMED gene model issue lists fewer than two kinds of evidence",
                path + ".evidence_types",
                "gene_model_issue_confirmed_single_evidence",
                "Use SUSPECTED, or record the independent line of evidence",
            )
        segments = [("reviewed_segment", issue.get("reviewed_segment"))] + [
            (f"components[{j}].segment", c.get("segment"))
            for j, c in enumerate(issue.get("components") or [])
        ]
        for where, segment in segments:
            if _reversed(segment):
                warn(
                    f"Residue range {segment} runs backwards",
                    f"{path}.{where}",
                    "gene_model_issue_segment_order",
                    "Write residue ranges as start-end",
                )
