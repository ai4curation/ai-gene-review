"""Tests for review.curation_error on existing annotations.

A CurationError records what went wrong when an annotation was curated from its
cited reference (e.g. a background sentence curated as the paper's own result),
separately from review.action and from the reference-level reference_review.
"""

from pathlib import Path

import pytest
from linkml.validator import validate as linkml_validate

from ai_gene_review.datamodel.gene_review_model import CurationError

SCHEMA = Path(__file__).parent.parent / "src/ai_gene_review/schema/gene_review.yaml"


def _base_review(curation_error: dict) -> dict:
    """Minimal valid GeneReview whose one annotation carries a curation_error."""
    return {
        "id": "Q12345",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for curation-error validation",
        "references": [
            {"id": "PMID:11111", "title": "Paper whose background was curated"},
            {"id": "PMID:22222", "title": "Earlier paper with the actual evidence"},
        ],
        "existing_annotations": [
            {
                "term": {"id": "GO:0014029", "label": "neural crest formation"},
                "evidence_type": "IMP",
                "original_reference_id": "PMID:11111",
                "review": {
                    "summary": "IMP resting on a background sentence.",
                    "action": "REMOVE",
                    "reason": "The paper has no crest experiments.",
                    "curation_error": curation_error,
                },
            }
        ],
    }


def _schema_errors(data: dict) -> list[str]:
    """Strict LinkML schema validation of a GeneReview; returns error messages."""
    report = linkml_validate(data, str(SCHEMA), target_class="GeneReview", strict=True)
    return [r.message for r in report.results]


def test_curation_error_model_roundtrip():
    """The generated model accepts the full set of fields."""
    ce = CurationError(
        error_type="BACKGROUND_CLAIM_CURATED",
        responsible_source="UniProt",
        evidence_reference_ids=["PMID:22222"],
        report_status="NOT_REPORTED",
    )
    assert str(ce.error_type) == "BACKGROUND_CLAIM_CURATED"
    assert [str(r) for r in ce.evidence_reference_ids] == ["PMID:22222"]


def test_curation_error_requires_error_type():
    """error_type is required."""
    with pytest.raises(ValueError):
        CurationError(responsible_source="MGI")


def test_invalid_error_type_rejected_by_model():
    """An out-of-enum error_type is rejected."""
    with pytest.raises(ValueError):
        CurationError(error_type="NOT_A_REAL_ERROR")


@pytest.mark.parametrize(
    "error_type",
    [
        "BACKGROUND_CLAIM_CURATED",
        "NO_SUPPORTING_CONTENT",
        "WRONG_GENE_OR_HOMONYM",
        "EVIDENCE_CODE_MISMATCH",
        "OVERINTERPRETED_RESULT",
        "OTHER",
    ],
)
def test_curation_error_types_validate(error_type: str):
    """All permissible error_type values pass schema validation."""
    errors = _schema_errors(
        _base_review(
            {
                "error_type": error_type,
                "responsible_source": "UniProt",
                "misread_text": [
                    {
                        "reference_id": "PMID:11111",
                        "supporting_text": "X is an essential regulator of Y",
                        "reference_section_type": "ABSTRACT",
                    }
                ],
                "evidence_reference_ids": ["PMID:22222"],
                "report_status": "NOT_REPORTED",
                "report_url": "https://example.org/ticket/1",
            }
        )
    )
    assert not errors, errors


def test_invalid_report_status_fails_schema_validation():
    """An out-of-enum report_status fails schema validation."""
    errors = _schema_errors(
        _base_review(
            {"error_type": "BACKGROUND_CLAIM_CURATED", "report_status": "MAYBE"}
        )
    )
    assert errors


def test_missing_error_type_fails_schema_validation():
    """A curation_error without error_type fails schema validation."""
    assert _schema_errors(_base_review({"responsible_source": "MGI"}))
