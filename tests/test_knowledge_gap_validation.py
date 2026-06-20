"""Tests for the KnowledgeGap class.

A KnowledgeGap is a curated, literature-grounded statement of what is NOT known
about a gene product, core function, module, or step. It can be attached at the
gene level (GeneReview.knowledge_gaps), the annotation level
(ExistingAnnotation.review.knowledge_gaps), the core-function level
(CoreFunction.knowledge_gaps), or the module level (ModuleReview.knowledge_gaps
and ModuleNode.knowledge_gaps). Its provenance reuses SupportingTextInReference,
so the field's own admissions of ignorance are verbatim-checked exactly like
supported_by.
"""

from pathlib import Path
import tempfile

import pytest
import yaml

from ai_gene_review.validation import validate_gene_review
from ai_gene_review.datamodel.gene_review_model import (
    KnowledgeGap,
    KnowledgeGapKindEnum,
    KnowledgeGapAspectEnum,
    KnowledgeGapStatusEnum,
)


def _gap(**overrides) -> dict:
    """A minimal, schema-valid KnowledgeGap dict."""
    gap = {
        "gap_statement": "The catalytic activity and direct substrate are undetermined.",
        "boundary": "The gene is required for process X and localizes to compartment Y.",
        "gap_kind": ["BIOLOGY"],
        "dark_aspect": "MF_DARK",
        "status": "OPEN",
        "significance": "Closing this would assign the gene a molecular function.",
        "resolution": "In vitro reconstitution plus proximity proteomics.",
    }
    gap.update(overrides)
    return gap


def _base_review(knowledge_gaps: list[dict]) -> dict:
    """Minimal valid GeneReview carrying top-level knowledge_gaps."""
    return {
        "id": "Q12345",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for knowledge-gap validation",
        "references": [],
        "knowledge_gaps": knowledge_gaps,
    }


def test_knowledge_gap_dataclass_roundtrip():
    """The generated dataclass accepts all gap fields and normalizes enums."""
    gap = KnowledgeGap(
        gap_statement="The cognate GEF and GAP are unidentified.",
        boundary="A bona fide Rab GTPase with a defined cycle and known effectors.",
        gap_kind=["BIOLOGY"],
        dark_aspect="RESIDUAL_SUBGAP",
        status="OPEN",
        significance="The regulatory logic of the pathway is incomplete.",
        resolution="GEF/GAP screen with a cargo mis-sorting readout.",
    )
    assert gap.gap_statement.startswith("The cognate GEF")
    assert [str(k) for k in gap.gap_kind] == ["BIOLOGY"]
    assert str(gap.dark_aspect) == "RESIDUAL_SUBGAP"
    assert str(gap.status) == "OPEN"


def test_knowledge_gap_enums_have_expected_values():
    """The three gap enums expose their documented permissible values."""
    assert {e.value for e in KnowledgeGapKindEnum} == {
        "BIOLOGY",
        "CURATION",
        "ONTOLOGY",
    }
    assert {e.value for e in KnowledgeGapAspectEnum} == {
        "MF_DARK",
        "BP_DARK",
        "CC_DARK",
        "WHOLLY_DARK",
        "RESIDUAL_SUBGAP",
    }
    assert {e.value for e in KnowledgeGapStatusEnum} == {
        "OPEN",
        "NARROWING",
        "CLOSING",
        "RESOLVED",
    }


def test_gap_statement_is_required():
    """gap_statement is the one required field on a KnowledgeGap."""
    with pytest.raises(Exception):
        KnowledgeGap(boundary="something is known")  # type: ignore[call-arg]


@pytest.mark.parametrize("status", ["OPEN", "NARROWING", "CLOSING", "RESOLVED"])
def test_gap_status_values_validate(status: str):
    """All permissible gap status values pass schema validation."""
    data = _base_review([_gap(status=status)])
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)
    try:
        report = validate_gene_review(temp_path, check_best_practices=False)
        assert report.is_valid, f"Unexpected validation failure: {report.issues}"
    finally:
        temp_path.unlink()


def test_invalid_gap_kind_rejected():
    """An out-of-enum gap_kind is rejected by the generated model."""
    with pytest.raises(Exception):
        KnowledgeGap(gap_statement="x", gap_kind=["NOT_A_REAL_KIND"])


def test_gap_provenance_reuses_supporting_text_in_reference():
    """A gap can carry provenance quotes via SupportingTextInReference."""
    gap = _gap(
        provenance=[
            {
                "reference_id": "PMID:11111",
                "supporting_text": "the precise role remains to be determined",
            }
        ]
    )
    data = _base_review([gap])
    data["references"] = [{"id": "PMID:11111", "title": "A paper that admits the gap"}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)
    try:
        # Schema-level validation only; verbatim quote checking is done by the
        # separate linkml-reference-validator CLI.
        report = validate_gene_review(temp_path, check_best_practices=False)
        assert report.is_valid, f"Unexpected validation failure: {report.issues}"
    finally:
        temp_path.unlink()
