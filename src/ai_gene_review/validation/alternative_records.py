"""Integrity checks for manually curated cross-record equivalence claims."""

from typing import Any

from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)


def validate_alternative_records(
    data: dict[str, Any], report: ValidationReport
) -> None:
    """Require a distinct target, cited evidence, and actual equivalence support.

    Sequence or locus evidence and proteome-membership evidence must both be
    present for reference-proteome candidates, equivalents, and locus counterparts.
    Historical absence or qualitative
    context is useful but cannot substitute for either. This validates the shape
    of the curator's argument, not the biological truth of that argument.
    """
    references = {
        r.get("id") for r in data.get("references") or [] if isinstance(r, dict)
    }
    seen: set[str] = set()

    def error(message: str, path: str) -> None:
        report.add_issue(
            ValidationSeverity.ERROR,
            message,
            path=path,
            validation_category="BestPractices",
            check_type="alternative_records",
        )

    def check_sources(evidence: list[dict[str, Any]], path: str) -> None:
        if not evidence:
            error("Assessments require cited evidence", path + ".evidence")
        for j, item in enumerate(evidence):
            sources = item.get("supported_by") or []
            if not sources:
                error(
                    "Evidence requires supported_by citations", f"{path}.evidence[{j}]"
                )
            for k, source in enumerate(sources):
                if source.get("reference_id") not in references:
                    error(
                        f"Evidence cites undeclared reference: {source.get('reference_id')}",
                        f"{path}.evidence[{j}].supported_by[{k}].reference_id",
                    )

    for i, record in enumerate(data.get("alternative_records") or []):
        path = f"alternative_records[{i}]"
        accession = record.get("id")
        if accession == str(data.get("id", "")).removeprefix("UniProtKB:"):
            error(
                "An alternative record cannot be the primary accession itself",
                path + ".id",
            )
        if accession in seen:
            error(f"Duplicate alternative record: {accession}", path + ".id")
        seen.add(accession)
        evidence = record.get("evidence") or []
        if not evidence:
            error("Alternative records require cited evidence", path + ".evidence")
        kinds = {e.get("type") for e in evidence}
        if record.get("relationship") in {
            "REFERENCE_PROTEOME_EQUIVALENT",
            "REFERENCE_PROTEOME_CANDIDATE",
            "REFERENCE_PROTEOME_LOCUS_COUNTERPART",
        }:
            if not record.get("reference_proteome"):
                error(
                    "Reference-proteome relationship requires a proteome identifier",
                    path,
                )
            if "PROTEOME_MEMBERSHIP" not in kinds:
                error(
                    "Reference-proteome relationship requires PROTEOME_MEMBERSHIP evidence",
                    path + ".evidence",
                )
            if not kinds & {"SEQUENCE_COMPARISON", "LOCUS_MAPPING"}:
                error(
                    "Reference-proteome relationship requires sequence or locus evidence; history/context alone is insufficient",
                    path + ".evidence",
                )
        check_sources(evidence, path)

    for i, assessment in enumerate(data.get("reference_proteome_assessments") or []):
        path = f"reference_proteome_assessments[{i}]"
        evidence = assessment.get("evidence") or []
        kinds = {e.get("type") for e in evidence}
        if not {"PROTEOME_SEARCH", "PROTEOME_MEMBERSHIP"} <= kinds:
            error(
                "A no-counterpart assessment requires PROTEOME_SEARCH and PROTEOME_MEMBERSHIP evidence",
                path,
            )
        if not assessment.get("reference_proteomes"):
            error("Assessment must identify the searched reference proteomes", path)
        check_sources(evidence, path)
