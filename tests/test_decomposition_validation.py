"""Validation of decomposed precomposed ("X involved in Y") annotations."""

from pathlib import Path
import tempfile

import pytest
import yaml

from ai_gene_review.datamodel.gene_review_model import Review
from ai_gene_review.validation import ValidationReport, validate_gene_review
from ai_gene_review.validation.decomposition import check_decomposition
from ai_gene_review.validation.validator import get_project_root

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


def _check(review: dict, term: dict = PRECOMPOSED, **lookups) -> set[str]:
    """Run check_decomposition directly, optionally with ontology lookups."""
    report = ValidationReport(file_path=Path("test"), is_valid=True)
    data = {"existing_annotations": [{"term": term, "review": review}]}
    check_decomposition(data, report, get_project_root(), **lookups)
    return {i.check_type for i in report.issues if i.check_type}


DRIFTED = {
    "id": "GO:0003252",
    "label": "obsolete negative regulation of cell proliferation involved in heart valve morphogenesis",
}
NEG_PROLIF = {"id": "GO:0008285", "label": "negative regulation of cell population proliferation"}


def test_genus_label_drift_needs_ontology():
    """GO relabelled 'cell proliferation' to 'cell population proliferation'."""
    review = {"action": "MODIFY", "proposed_replacement_terms": [NEG_PROLIF]}
    assert "decomposition_context_dropped_silently" not in _check(review, DRIFTED)
    synonyms = lambda i: frozenset({NEG_PROLIF["label"], "negative regulation of cell proliferation"})  # noqa: E731
    assert "decomposition_context_dropped_silently" in _check(review, DRIFTED, names=synonyms)


def test_is_a_ancestor_counts_as_genus_but_part_of_context_does_not():
    review = {"action": "MODIFY", "proposed_replacement_terms": [{"id": "GO:0006622", "label": "x"}]}
    assert "decomposition_context_dropped_silently" in _check(
        review, is_a_ancestors=lambda t: frozenset({"GO:0006622"})
    )
    to_context = {"action": "MODIFY", "proposed_replacement_terms": [{"id": "GO:0061684", "label": "y"}]}
    assert "decomposition_context_dropped_silently" not in _check(
        to_context, is_a_ancestors=lambda t: frozenset({"GO:0006622"})
    )


@pytest.mark.parametrize(
    "activity,expected",
    [
        ("gomodel:63c0ac2b00001252/63c0ac2b00001260", None),
        ("gomodel:63c0ac2b00001252/0000000000000000", "decomposition_activity_not_found"),
    ],
)
def test_gocam_activity_must_exist(activity, expected):
    review = {
        "action": "MODIFY",
        "proposed_replacement_terms": [GENUS],
        "decomposed_into": {"gocam_associations": [{"model": GOCAM, "activity": activity}]},
    }
    found = {c for c in _check(review) if c.startswith("decomposition_")}
    assert found == ({expected} if expected else set())


def test_module_element_cannot_be_a_cited_curie():
    review = {
        "action": "MODIFY",
        "proposed_replacement_terms": [GENUS],
        "decomposed_into": {"module_associations": [{"module": MODULE, "element": "GO:0097194"}]},
    }
    assert "decomposition_element_not_found" in _check(review)


def test_empty_decomposed_into_is_an_error():
    review = {"action": "MODIFY", "proposed_replacement_terms": [GENUS], "decomposed_into": {}}
    assert "decomposition_empty" in _check(review)


@pytest.mark.integration
def test_real_go_synonym_catches_label_drift():
    from ai_gene_review.validation.decomposition import go_names

    review = {"action": "MODIFY", "proposed_replacement_terms": [NEG_PROLIF]}
    assert "decomposition_context_dropped_silently" in _check(review, DRIFTED, names=go_names)
