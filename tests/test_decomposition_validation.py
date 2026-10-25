"""Validation of decomposed precomposed ("X involved in Y") annotations."""

from pathlib import Path
import tempfile

import pytest
import yaml

from ai_gene_review.datamodel.gene_review_model import Review
from ai_gene_review.validation import ValidationReport, validate_gene_review

PRECOMPOSED = {
    "id": "GO:0061740",
    "label": "protein targeting to lysosome involved in chaperone-mediated autophagy",
}
GENUS = {"id": "GO:0006622", "label": "protein targeting to lysosome"}
# Real repository fixtures: a cached GO-CAM and a module with a known node id.
GOCAM = "gomodel:63c0ac2b00001252"
MODULE = "apoptotic_execution_phase"
MODULE_ELEMENT = "apoptotic_execution_phase"


def _validate(review: dict) -> ValidationReport:
    """Validate a one-annotation review with the given review block."""
    doc = {
        "id": "P11142",
        "gene_symbol": "HSPA8",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene",
        "references": [{"id": "GO_REF:0000033", "title": "test"}],
        "existing_annotations": [
            {
                "term": PRECOMPOSED,
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {"summary": "test", "reason": "test", **review},
            }
        ],
    }
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "HSPA8-ai-review.yaml"
        path.write_text(yaml.dump(doc))
        return validate_gene_review(path, check_best_practices=True)


def _checks(report: ValidationReport) -> set[str]:
    return {i.check_type for i in report.issues if i.check_type}


def test_review_model_accepts_decomposition_slots():
    review = Review(
        summary="s",
        action="MODIFY",
        proposed_replacement_terms=[GENUS],
        decomposed_into={
            "gocam_associations": [{"model": GOCAM}],
            "module_associations": [{"module": MODULE, "element": MODULE_ELEMENT}],
            "in_core_functions": True,
        },
    )
    assert review.decomposed_into.module_associations[0].module == MODULE


@pytest.mark.parametrize(
    "extra,expected",
    [
        ({}, "decomposition_context_dropped_silently"),
        ({"decomposed_into": {"gocam_associations": [{"model": GOCAM}]}}, None),
        ({"decomposed_into": {"in_core_functions": True}}, None),
        ({"decomposed_into": {"context_dropped": True}}, None),
        (
            {
                "decomposed_into": {
                    "gocam_associations": [{"model": "gomodel:0000000000000000"}]
                }
            },
            "decomposition_gocam_not_found",
        ),
        (
            {
                "decomposed_into": {
                    "module_associations": [{"module": "no_such_module"}]
                }
            },
            "decomposition_module_not_found",
        ),
        (
            {
                "decomposed_into": {
                    "module_associations": [{"module": MODULE, "element": "nope"}]
                }
            },
            "decomposition_element_not_found",
        ),
        (
            {
                "decomposed_into": {
                    "module_associations": [
                        {"module": MODULE, "element": MODULE_ELEMENT}
                    ]
                }
            },
            None,
        ),
        (
            {
                "decomposed_into": {
                    "context_dropped": True,
                    "gocam_associations": [{"model": GOCAM}],
                }
            },
            "decomposition_contradictory",
        ),
    ],
)
def test_modify_to_genus(extra, expected):
    report = _validate(
        {"action": "MODIFY", "proposed_replacement_terms": [GENUS], **extra}
    )
    found = {c for c in _checks(report) if c.startswith("decomposition_")}
    assert found == ({expected} if expected else set())


def test_lateral_modify_does_not_warn():
    report = _validate(
        {
            "action": "MODIFY",
            "proposed_replacement_terms": [
                {"id": "GO:0061684", "label": "chaperone-mediated autophagy"}
            ],
        }
    )
    assert "decomposition_context_dropped_silently" not in _checks(report)


@pytest.mark.parametrize("action", ["ACCEPT", "KEEP_AS_NON_CORE"])
def test_slots_require_modify(action):
    report = _validate(
        {"action": action, "decomposed_into": {"in_core_functions": True}}
    )
    assert "decomposition_requires_modify" in _checks(report)
