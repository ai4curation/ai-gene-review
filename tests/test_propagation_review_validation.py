"""Validation checks for structured propagation reviews on inferred annotations."""

from pathlib import Path
import tempfile

import yaml

from ai_gene_review.datamodel.gene_review_model import Review
from ai_gene_review.validation import validate_gene_review


def _validate(yaml_data: dict) -> object:
    """Validate a minimal gene review YAML from a temporary file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "TEST-ai-review.yaml"
        path.write_text(yaml.dump(yaml_data))
        return validate_gene_review(path, check_best_practices=True)


def _base_annotation(evidence_type: str, action: str, review_extra: dict | None = None) -> dict:
    """Build a single existing annotation row for propagation-review tests."""
    review = {
        "summary": "test",
        "action": action,
        "reason": "test",
    }
    if review_extra:
        review.update(review_extra)
    return {
        "term": {"id": "GO:0005515", "label": "protein binding"},
        "evidence_type": evidence_type,
        "original_reference_id": "GO_REF:0000033",
        "review": review,
    }


def _base_yaml(annotation: dict) -> dict:
    """Construct a minimal review document for a single annotation."""
    return {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene",
        "references": [
            {
                "id": "GO_REF:0000033",
                "title": "Annotation inferences using phylogenetic trees",
            }
        ],
        "existing_annotations": [annotation],
    }


def _has_missing_propagation_review_warning(report: object) -> bool:
    """Return whether the propagation-review best-practice warning fired."""
    return any(
        issue.check_type == "missing_propagation_review"
        for issue in report.issues
    )


def test_iba_remove_without_propagation_review_warns():
    """Corrective IBA actions should carry structured propagation-review metadata."""
    report = _validate(_base_yaml(_base_annotation("IBA", "REMOVE")))
    assert _has_missing_propagation_review_warning(report)


def test_iso_modify_with_propagation_review_does_not_warn():
    """The warning is suppressed when propagation_review is present."""
    annotation = _base_annotation(
        "ISO",
        "MODIFY",
        {
            "propagation_review": {
                "root_cause": "PROPAGATION_BAD",
                "failure_modes": ["WRONG_ORTHOLOG_OR_PARALOG"],
                "source_entities": [
                    {
                        "source_id": "UniProtKB:P03950",
                        "source_label": "ANG",
                        "source_status": "SUPPORTS_SOURCE_BUT_NOT_TARGET",
                        "comment": "Source supports angiogenesis for human ANG; transfer to mouse Ang2 is unsafe.",
                    }
                ],
            }
        },
    )
    report = _validate(_base_yaml(annotation))
    assert not _has_missing_propagation_review_warning(report)


def test_experimental_remove_without_propagation_review_does_not_warn():
    """Experimental evidence rows are not propagation-review targets."""
    report = _validate(_base_yaml(_base_annotation("IDA", "REMOVE")))
    assert not _has_missing_propagation_review_warning(report)


def test_iba_accept_without_propagation_review_does_not_warn():
    """Accepted IBA rows may omit propagation_review during gradual adoption."""
    report = _validate(_base_yaml(_base_annotation("IBA", "ACCEPT")))
    assert not _has_missing_propagation_review_warning(report)


def test_generated_review_model_accepts_propagation_review():
    """The generated Pydantic model accepts the new structured metadata."""
    review = Review(
        action="REMOVE",
        reason="test",
        propagation_review={
            "root_cause": "SOURCE_BAD",
            "failure_modes": ["SOURCE_MISCITATION"],
            "source_entities": [
                {
                    "source_id": "UniProtKB:P03950",
                    "source_label": "ANG",
                    "source_status": "SOURCE_BAD",
                    "comment": "Wrong source annotation for this transfer.",
                }
            ],
        },
    )

    assert review.propagation_review is not None
    assert review.propagation_review.root_cause == "SOURCE_BAD"
    assert review.propagation_review.source_entities is not None
    assert review.propagation_review.source_entities[0].source_id == "UniProtKB:P03950"
