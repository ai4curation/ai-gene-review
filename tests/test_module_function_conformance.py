"""Functional assertions must agree with reviewed gene evidence, not just presence."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.module_function_conformance import gene_function_findings

MF = "GO:0051498"
PARENT = "GO:0010333"
OTHER = "GO:0034279"


def module(participant=None, function_id=MF):
    function = {"preferred_term": "test activity"}
    if function_id:
        function["term"] = {"id": function_id, "label": "test activity"}
    return {
        "module": {
            "id": "root",
            "annotons": [
                {
                    "id": "activity",
                    "function": function,
                    "participant": participant
                    or {
                        "selector_type": "GENE",
                        "gene": {
                            "preferred_term": "CPS4",
                            "term": {"id": "UniProtKB:Q0JF02"},
                        },
                    },
                }
            ],
        }
    }


def write_review(tmp_path, *, core=None, annotations=None):
    path = tmp_path / "CPS4-ai-review.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "id": "Q0JF02",
                "gene_symbol": "CPS4",
                "core_functions": core or [],
                "existing_annotations": annotations or [],
            }
        )
    )
    return {"Q0JF02": path}


def annotation(action, term=MF, **extra):
    return {"term": {"id": term}, "review": {"action": action}, **extra}


def findings(doc, index, **kwargs):
    return gene_function_findings(doc, gene_index=index, **kwargs)


def test_core_supported_and_missing_review_are_separate(tmp_path):
    index = write_review(tmp_path, core=[{"molecular_function": {"id": MF}}])
    assert findings(module(), index)[0]["status"] == "CORE_SUPPORTED"
    row = findings(module(), {})[0]
    assert row["status"] == "REVIEW_MISSING"
    assert row["severity"] == "warning"


@pytest.mark.parametrize(
    "action,status",
    [
        ("ACCEPT", "ANNOTATION_SUPPORTED"),
        ("NEW", "ANNOTATION_SUPPORTED"),
        ("KEEP_AS_NON_CORE", "NON_CORE_SUPPORTED"),
        ("PENDING", "FUNCTION_UNREVIEWED"),
        ("UNDECIDED", "FUNCTION_UNREVIEWED"),
        ("REMOVE", "REVIEW_DISAGREEMENT"),
        ("MARK_AS_OVER_ANNOTATED", "REVIEW_DISAGREEMENT"),
    ],
)
def test_review_action_meanings(tmp_path, action, status):
    index = write_review(tmp_path, annotations=[annotation(action)])
    row = findings(module(), index)[0]
    assert row["status"] == status
    assert (
        row["severity"] != "error"
    )  # evidence rejection alone is not a biological NOT


def test_modified_annotation_uses_replacement_not_original(tmp_path):
    ann = annotation("MODIFY", OTHER)
    ann["review"]["proposed_replacement_terms"] = [{"id": MF}]
    index = write_review(tmp_path, annotations=[ann])
    assert findings(module(), index)[0]["status"] == "ANNOTATION_SUPPORTED"
    assert (
        findings(module(function_id=OTHER), index)[0]["status"] == "REVIEW_DISAGREEMENT"
    )


def test_removed_evidence_does_not_cancel_core_support(tmp_path):
    index = write_review(
        tmp_path,
        core=[{"molecular_function": {"id": MF}}],
        annotations=[annotation("REMOVE")],
    )
    assert findings(module(), index)[0]["status"] == "CORE_SUPPORTED"


def test_retained_not_conflicts_even_if_core_also_claims_function(tmp_path):
    index = write_review(
        tmp_path,
        core=[{"molecular_function": {"id": MF}}],
        annotations=[annotation("ACCEPT", negated=True)],
    )
    row = findings(module(), index)[0]
    assert row["status"] == "CONTRADICTED"
    assert row["severity"] == "error"


@pytest.mark.parametrize(
    "extra", [{"isoform": "Q0JF02-2"}, {"extensions": ["occurs_in(CL:1)"]}]
)
def test_scoped_not_does_not_refute_generic_module(tmp_path, extra):
    index = write_review(
        tmp_path, annotations=[annotation("ACCEPT", negated=True, **extra)]
    )
    assert findings(module(), index)[0]["status"] == "CONTEXT_REQUIRED"


def test_target_isoform_matches_only_compatible_annotations(tmp_path):
    participant = {
        "selector_type": "GENE_PRODUCT",
        "gene_product": {"term": {"id": "UniProtKB:Q0JF02-2"}},
    }
    index = write_review(
        tmp_path, annotations=[annotation("ACCEPT", isoform="Q0JF02-1")]
    )
    assert findings(module(participant), index)[0]["status"] == "CONTEXT_REQUIRED"
    index = write_review(
        tmp_path, annotations=[annotation("ACCEPT", isoform="Q0JF02-2", negated=True)]
    )
    assert findings(module(participant), index)[0]["status"] == "CONTRADICTED"


def test_contributes_to_cannot_support_independent_activity(tmp_path):
    index = write_review(
        tmp_path,
        core=[{"contributes_to_molecular_function": {"id": MF}}],
        annotations=[annotation("ACCEPT", qualifier="contributes_to")],
    )
    assert findings(module(), index)[0]["status"] == "CONTRIBUTES_ONLY"


def test_more_specific_review_supports_broader_module_but_not_reverse(tmp_path):
    # A tiny explicitly supplied ontology relation, not a mocked remote service.
    def subclass(child, parent):
        return child == parent or (child, parent) == (MF, PARENT)

    index = write_review(tmp_path, core=[{"molecular_function": {"id": MF}}])
    assert (
        findings(module(function_id=PARENT), index, subclass_of=subclass)[0]["status"]
        == "CORE_SUPPORTED"
    )
    index = write_review(tmp_path, core=[{"molecular_function": {"id": PARENT}}])
    assert (
        findings(module(), index, subclass_of=subclass)[0]["status"]
        == "FUNCTION_UNREVIEWED"
    )
    index = write_review(
        tmp_path, annotations=[annotation("ACCEPT", PARENT, negated=True)]
    )
    assert (
        findings(module(), index, subclass_of=subclass)[0]["status"] == "CONTRADICTED"
    )


def test_free_text_function_is_uncheckable_not_supported(tmp_path):
    index = write_review(tmp_path, core=[{"molecular_function": {"id": MF}}])
    assert findings(module(function_id=None), index)[0]["status"] == "NO_FUNCTION_ID"


def test_family_representatives_are_checked_individually(tmp_path):
    index = write_review(tmp_path, core=[{"molecular_function": {"id": MF}}])
    participant = {
        "selector_type": "FAMILY",
        "family": {
            "preferred_term": "example family",
            "representative_members": [
                {"term": {"id": "UniProtKB:Q0JF02"}},
                {"term": {"id": "UniProtKB:Q99999"}},
            ],
        },
    }
    rows = findings(module(participant), index)
    assert [(r["scope"], r["status"]) for r in rows] == [
        ("family_representative", "CORE_SUPPORTED"),
        ("family_representative", "REVIEW_MISSING"),
    ]


def test_complex_activity_is_not_assigned_to_each_subunit(tmp_path):
    index = write_review(tmp_path, core=[{"molecular_function": {"id": MF}}])
    gene = module()["module"]["annotons"][0]["participant"]
    participant = {
        "selector_type": "PROTEIN_COMPLEX",
        "protein_complex": {
            "preferred_term": "complex",
            "active_units": [
                {
                    "id": "has_role",
                    "participant": gene,
                    "function": {"term": {"id": MF}},
                },
                {"id": "no_role", "participant": gene},
            ],
        },
    }
    rows = findings(module(participant, function_id=OTHER), index)
    unit_rows = [r for r in rows if r["scope"] == "complex_unit"]
    assert len(unit_rows) == 1
    assert unit_rows[0]["function_id"] == MF
    assert unit_rows[0]["status"] == "CORE_SUPPORTED"


def test_real_cps4_core_function_matches():
    root = Path(__file__).resolve().parents[1]
    index = {"Q0JF02": root / "genes/ORYSJ/CPS4/CPS4-ai-review.yaml"}
    assert findings(module(), index)[0]["status"] == "CORE_SUPPORTED"


def test_modified_not_checks_replacement_polarity(tmp_path):
    ann = annotation("MODIFY", OTHER, negated=True)
    ann["review"]["proposed_replacement_terms"] = [{"id": MF}]
    index = write_review(tmp_path, annotations=[ann])
    assert findings(module(), index)[0]["status"] == "CONTRADICTED"
    assert findings(module(function_id=OTHER), index)[0]["status"] != "CONTRADICTED"


def test_required_function_is_checked_in_addition_to_annoton_function(tmp_path):
    index = write_review(tmp_path, core=[{"molecular_function": {"id": MF}}])
    doc = module()
    annoton = doc["module"]["annotons"][0]
    annoton["participant"]["required_function"] = {"term": {"id": OTHER}}
    rows = findings(doc, index)
    assert [(r["annoton_id"], r["status"]) for r in rows] == [
        ("activity", "CORE_SUPPORTED"),
        ("activity:required_function", "FUNCTION_UNREVIEWED"),
    ]
    annoton["participant"]["required_function"] = {"term": {"id": MF}}
    assert len(findings(doc, index)) == 1
    del annoton["function"]
    assert findings(doc, index)[0]["status"] == "CORE_SUPPORTED"


def test_complex_unit_required_function_is_its_own_assertion(tmp_path):
    index = write_review(tmp_path, core=[{"molecular_function": {"id": MF}}])
    gene = module()["module"]["annotons"][0]["participant"]
    gene["required_function"] = {"term": {"id": MF}}
    doc = module(
        {
            "selector_type": "PROTEIN_COMPLEX",
            "protein_complex": {
                "active_units": [{"id": "catalyst", "participant": gene}]
            },
        },
        function_id=OTHER,
    )
    rows = [r for r in findings(doc, index) if r["scope"] == "complex_unit"]
    assert [(r["annoton_id"], r["function_id"], r["status"]) for r in rows] == [
        ("activity/catalyst", MF, "CORE_SUPPORTED")
    ]


@pytest.mark.parametrize("negated", [False, True])
def test_generic_annotation_does_not_resolve_an_explicit_isoform(tmp_path, negated):
    participant = {
        "selector_type": "GENE_PRODUCT",
        "gene_product": {"term": {"id": "UniProtKB:Q0JF02-2"}},
    }
    index = write_review(tmp_path, annotations=[annotation("ACCEPT", negated=negated)])
    assert findings(module(participant), index)[0]["status"] == "CONTEXT_REQUIRED"


def test_validator_exposes_function_compliance_and_blocks_applicable_not(tmp_path):
    from ai_gene_review.validation.module_validator import validate_module_file

    index = write_review(tmp_path, annotations=[annotation("ACCEPT", negated=True)])
    path = tmp_path / "module.yaml"
    path.write_text(yaml.safe_dump(module()))
    # A real config explicitly skips label lookup, isolating the separate corpus join.
    config = tmp_path / "oak.yaml"
    config.write_text("ontology_adapters:\n  GO: null\n  UniProtKB: null\n")
    result = validate_module_file(
        path,
        config_path=config,
        gene_index=index,
        family_reviews_dir=tmp_path / "panther",
        pfam_reviews_dir=tmp_path / "pfam",
    )
    assert not result.is_valid
    assert result.function_conformance["conflicts"] == 1
    assert any("CONTRADICTED" in e for e in result.errors)


def test_missing_review_is_advisory_in_validator(tmp_path):
    from ai_gene_review.validation.module_validator import validate_module_file

    path = tmp_path / "module.yaml"
    path.write_text(yaml.safe_dump(module()))
    config = tmp_path / "oak.yaml"
    config.write_text("ontology_adapters:\n  GO: null\n  UniProtKB: null\n")
    result = validate_module_file(
        path,
        config_path=config,
        gene_index={},
        family_reviews_dir=tmp_path / "panther",
        pfam_reviews_dir=tmp_path / "pfam",
    )
    assert result.is_valid
    assert result.function_conformance["counts"]["REVIEW_MISSING"] == 1
    assert any("REVIEW_MISSING" in w for w in result.warnings)


def test_family_representative_not_is_advisory(tmp_path):
    index = write_review(tmp_path, annotations=[annotation("ACCEPT", negated=True)])
    participant = {
        "selector_type": "FAMILY",
        "family": {"representative_members": [{"term": {"id": "UniProtKB:Q0JF02"}}]},
    }
    row = findings(module(participant), index)[0]
    assert row["status"] == "CONTRADICTED"
    assert row["severity"] == "warning"
    assert "representative" in row["message"]
    assert findings(module(), index)[0]["severity"] == "error"


def test_failed_go_adapter_is_cached_and_reported(tmp_path):
    from ai_gene_review.module_function_conformance import (
        go_subclass_predicate,
        module_function_conformance,
    )

    predicate = go_subclass_predicate("unsupported-conformance-test:missing")
    index = write_review(tmp_path, core=[{"molecular_function": {"id": OTHER}}])
    result = module_function_conformance(
        module(), gene_index=index, subclass_of=predicate
    )
    assert result["counts"]["ONTOLOGY_UNAVAILABLE"] == 1
    assert "exact" in result["rows"][-1]["message"]
    assert (
        predicate.adapter is None
    )  # Failed construction is a cached value, not an exception.
    assert "adapter" in vars(predicate)
    assert not predicate(PARENT, OTHER)
    assert predicate(MF, MF)
    assert predicate.adapter is None
    repeated = module_function_conformance(
        module(), gene_index=index, subclass_of=predicate
    )
    assert repeated["counts"]["ONTOLOGY_UNAVAILABLE"] == 1
    assert "Ontology unavailable" in repeated["rows"][0]["message"]
