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
    ModuleReview,
    ModuleNode,
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


def _review_with_gap_at(level: str) -> dict:
    """Build a GeneReview that carries one gap at the requested attachment point.

    Covers the three attachment points reachable from a GeneReview target:
    the whole gene, a single existing annotation's review, and a core function.
    (ModuleReview / ModuleNode are validated under the ModuleReview target.)
    """
    base: dict[str, object] = {
        "id": "Q12345",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for knowledge-gap attachment points",
        "references": [],
    }
    if level == "gene":
        base["knowledge_gaps"] = [_gap()]
    elif level == "annotation":
        base["existing_annotations"] = [
            {
                "term": {"id": "GO:0003924", "label": "GTPase activity"},
                "evidence_type": "IEA",
                "original_reference_id": "GO_REF:0000002",
                "review": {
                    "summary": "core activity",
                    "action": "ACCEPT",
                    "knowledge_gaps": [_gap(dark_aspect="RESIDUAL_SUBGAP")],
                },
            }
        ]
    elif level == "core_function":
        base["core_functions"] = [
            {
                "description": "core function carrying a residual sub-gap",
                "molecular_function": {
                    "id": "GO:0003924",
                    "label": "GTPase activity",
                },
                "knowledge_gaps": [_gap(dark_aspect="RESIDUAL_SUBGAP")],
            }
        ]
    else:  # pragma: no cover - guard against typos in parametrize
        raise ValueError(level)
    return base


@pytest.mark.parametrize("level", ["gene", "annotation", "core_function"])
def test_gap_validates_at_each_attachment_point(level: str):
    """A gap validates whether attached at the gene, annotation, or core function."""
    data = _review_with_gap_at(level)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)
    try:
        report = validate_gene_review(temp_path, check_best_practices=False)
        assert report.is_valid, f"Unexpected validation failure: {report.issues}"
    finally:
        temp_path.unlink()


def test_gap_attaches_to_module_and_module_node():
    """The remaining two attachment points — ModuleReview and ModuleNode — accept gaps.

    These live under the ModuleReview target (separate from GeneReview), so they are
    exercised through the generated model rather than validate_gene_review. Together with
    test_gap_validates_at_each_attachment_point this covers all five attachment points.
    """
    node = ModuleNode(
        id="node:1",
        label="a module step with a residual sub-gap",
        knowledge_gaps=[KnowledgeGap(**_gap(dark_aspect="RESIDUAL_SUBGAP"))],
    )
    module = ModuleReview(
        id="MODULE:1",
        title="test module",
        module=node,
        knowledge_gaps=[KnowledgeGap(**_gap())],
    )
    assert len(module.knowledge_gaps) == 1
    assert module.knowledge_gaps[0].gap_statement
    assert len(module.module.knowledge_gaps) == 1
    assert str(module.module.knowledge_gaps[0].dark_aspect) == "RESIDUAL_SUBGAP"


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
        # separate linkml-reference-validator CLI, which schema-walks every
        # SupportingTextInReference instance (including KnowledgeGap.provenance).
        # That path was confirmed by deliberately corrupting a CFAP300 provenance
        # quote and observing the validator flag
        # knowledge_gaps[0].provenance[0].supporting_text.
        report = validate_gene_review(temp_path, check_best_practices=False)
        assert report.is_valid, f"Unexpected validation failure: {report.issues}"
    finally:
        temp_path.unlink()
