"""Tests for finding-level review (finding_review) on references.findings.

A FindingReview lets a reviewer mark an individual finding within a reference as
disputed or overturned by later evidence, which is finer-grained than the
whole-reference reference_review.
"""

from pathlib import Path
import tempfile

import pytest
import yaml

from ai_gene_review.validation import validate_gene_review
from ai_gene_review.datamodel.gene_review_model import (
    FindingReview,
    FindingReviewStatusEnum,
)


def _base_review(finding_review: dict) -> dict:
    """Minimal valid GeneReview carrying one finding with a finding_review."""
    return {
        "id": "Q12345",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for finding-review validation",
        "references": [
            {
                "id": "PMID:11111",
                "title": "Older paper with a later-overturned claim",
                "findings": [
                    {
                        "statement": "Enzyme X is fully active on its own.",
                        "supporting_text": "Enzyme X is fully active on its own.",
                        "finding_review": finding_review,
                    }
                ],
            },
            {"id": "PMID:22222", "title": "Newer paper that overturns it"},
        ],
    }


def test_finding_review_dataclass_roundtrip():
    """The generated dataclass accepts finding_status and superseded_by."""
    fr = FindingReview(
        finding_status="OVERTURNED",
        superseded_by=["PMID:22222"],
        review_notes="Standalone activity was not reproducible.",
    )
    assert str(fr.finding_status) == "OVERTURNED"
    # superseded_by is normalized to a list of reference ids
    assert [str(r) for r in fr.superseded_by] == ["PMID:22222"]


def test_invalid_finding_status_rejected_by_dataclass():
    """An out-of-enum finding_status is rejected by the generated dataclass."""
    with pytest.raises(ValueError):
        FindingReview(finding_status="NOT_A_REAL_STATUS")


@pytest.mark.parametrize(
    "status", ["CURRENT", "CORROBORATED", "DISPUTED", "OVERTURNED", "UNVERIFIED"]
)
def test_finding_review_status_values_validate(status: str):
    """All permissible finding_status values pass schema validation."""
    data = _base_review(
        {
            "finding_status": status,
            "superseded_by": ["PMID:22222"],
            "review_notes": "Adjudicated against the newer study.",
        }
    )
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)
    try:
        report = validate_gene_review(temp_path, check_best_practices=False)
        assert report.is_valid, f"Unexpected validation failure: {report.issues}"
    finally:
        temp_path.unlink()


