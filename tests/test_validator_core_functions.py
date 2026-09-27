"""Test the core functions validation rules."""

import tempfile
from pathlib import Path
import yaml
from linkml.validator import validate as linkml_validate

from ai_gene_review.validation import validate_gene_review
from ai_gene_review.validation.validation_report import ValidationSeverity


def test_core_function_without_support_or_accepted_term():
    """Test that core functions must either come from ACCEPTED annotations or have supported_by."""
    
    # Create a test YAML with a core function that is neither from ACCEPTED nor has supported_by
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "A test gene for validation",
        "existing_annotations": [
            {
                "term": {"id": "GO:0005524", "label": "ATP binding"},
                "evidence_type": "IEA",
                "review": {
                    "action": "REMOVE",  # Not ACCEPTED
                    "reason": "Too general"
                }
            }
        ],
        "core_functions": [
            {
                "molecular_function": {
                    "id": "GO:0004672",  # protein kinase activity - not from ACCEPTED
                    "label": "protein kinase activity"
                },
                "description": "Test function"
                # No supported_by field
            }
        ]
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(data, f)
        test_file = Path(f.name)
    
    try:
        report = validate_gene_review(test_file, check_goa=False)
        
        # Should have an error about the core function
        errors = [issue for issue in report.issues if issue.severity == ValidationSeverity.ERROR]
        assert any(
            "GO:0004672" in issue.message and "not from an ACCEPTED/NEW annotation" in issue.message
            for issue in errors
        ), "Should report error for core function not from ACCEPTED annotation and lacking supported_by"
    finally:
        test_file.unlink()


def test_core_function_from_accepted_annotation():
    """Test that core functions from ACCEPTED annotations are valid."""
    
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "A test gene for validation",
        "existing_annotations": [
            {
                "term": {"id": "GO:0005524", "label": "ATP binding"},
                "evidence_type": "IEA",
                "review": {
                    "action": "ACCEPT",  # ACCEPTED
                    "reason": "Well supported"
                }
            }
        ],
        "core_functions": [
            {
                "molecular_function": {
                    "id": "GO:0005524",  # Same as ACCEPTED annotation
                    "label": "ATP binding"
                },
                "description": "Binds ATP"
                # No supported_by needed since it's from ACCEPTED
            }
        ]
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(data, f)
        test_file = Path(f.name)
    
    try:
        report = validate_gene_review(test_file, check_goa=False)
        
        # Should not have errors about this core function
        errors = [issue for issue in report.issues if issue.severity == ValidationSeverity.ERROR]
        assert not any(
            "GO:0005524" in issue.message and "not from an ACCEPTED/NEW annotation" in issue.message
            for issue in errors
        ), "Should not report error for core function from ACCEPTED annotation"
    finally:
        test_file.unlink()


def test_core_function_with_supported_by():
    """Test that core functions with supported_by are valid even if not from ACCEPTED."""
    
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "A test gene for validation",
        "references": [
            {"id": "PMID:12345", "title": "Test paper"}
        ],
        "existing_annotations": [],  # No existing annotations
        "core_functions": [
            {
                "molecular_function": {
                    "id": "GO:0004672",
                    "label": "protein kinase activity"
                },
                "description": "Novel kinase function",
                "supported_by": [
                    {
                        "reference_id": "PMID:12345",
                        "supporting_text": "The protein shows kinase activity"
                    }
                ]
            }
        ]
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(data, f)
        test_file = Path(f.name)
    
    try:
        report = validate_gene_review(test_file, check_goa=False, check_supporting_text=False)
        
        # Should not have errors about this core function
        errors = [issue for issue in report.issues if issue.severity == ValidationSeverity.ERROR]
        assert not any(
            "GO:0004672" in issue.message and "not from an ACCEPTED/NEW annotation" in issue.message
            for issue in errors
        ), "Should not report error for core function with supported_by"
    finally:
        test_file.unlink()


def test_core_function_from_proposed_replacement():
    """Test that core functions from proposed_replacement_terms in MODIFY actions are valid."""
    
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "A test gene for validation",
        "existing_annotations": [
            {
                "term": {"id": "GO:0005524", "label": "ATP binding"},
                "evidence_type": "IEA",
                "review": {
                    "action": "MODIFY",
                    "reason": "More specific term available",
                    "proposed_replacement_terms": [
                        {"id": "GO:0004672", "label": "protein kinase activity"}
                    ]
                }
            }
        ],
        "core_functions": [
            {
                "molecular_function": {
                    "id": "GO:0004672",  # From proposed_replacement_terms
                    "label": "protein kinase activity"
                },
                "description": "Kinase function"
            }
        ]
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(data, f)
        test_file = Path(f.name)
    
    try:
        report = validate_gene_review(test_file, check_goa=False)
        
        # Should not have errors about this core function
        errors = [issue for issue in report.issues if issue.severity == ValidationSeverity.ERROR]
        assert not any(
            "GO:0004672" in issue.message and "not from an ACCEPTED/NEW annotation" in issue.message
            for issue in errors
        ), "Should not report error for core function from proposed_replacement_terms"
    finally:
        test_file.unlink()

def _holdase_review(proposed_name: str) -> dict:
    """A review whose core activity has no GO term yet (in-situ holdase)."""
    return {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "A test small heat shock protein",
        "existing_annotations": [
            {
                "term": {"id": "GO:0005737", "label": "cytoplasm"},
                "evidence_type": "IEA",
                "review": {"action": "ACCEPT", "reason": "Cytosolic chaperone"},
            }
        ],
        "core_functions": [
            {
                "description": "Holds unfolded clients in solution without refolding them",
                "proposed_molecular_function": proposed_name,
                "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            }
        ],
        "proposed_new_terms": [
            {
                "proposed_name": "holdase chaperone activity",
                "proposed_definition": "Binding an unfolded protein to prevent its aggregation without refolding it.",
                "supported_by": [
                    {"reference_id": "PMID:12345", "supporting_text": "prevents aggregation"}
                ],
            }
        ],
    }


def _issues(data: dict) -> list:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        path = Path(f.name)
    try:
        report = validate_gene_review(path, check_goa=False)
    finally:
        path.unlink()
    return report.issues


def _errors(data: dict) -> list:
    return [i for i in _issues(data) if i.severity == ValidationSeverity.ERROR]


def _pmf_errors(data: dict) -> list:
    return [e for e in _errors(data) if "proposed_molecular_function" in str(e.path)]


def test_proposed_molecular_function_matching_a_proposed_new_term_is_valid():
    """A core function can carry a not-yet-existing MF by naming a proposed_new_terms entry."""
    data = _holdase_review("holdase chaperone activity")
    errors = _errors(data)
    assert not [e for e in errors if "proposed_molecular_function" in str(e.path)]

    # The slot must also be accepted by the LinkML schema itself.
    schema = Path(__file__).parent.parent / "src/ai_gene_review/schema/gene_review.yaml"
    report = linkml_validate(data, str(schema), target_class="GeneReview", strict=True)
    assert not report.results, [r.message for r in report.results]


def test_proposed_molecular_function_must_match_a_proposed_new_term():
    """A proposed_molecular_function that names no proposed_new_terms entry is an error."""
    errors = _pmf_errors(_holdase_review("holdase activity"))
    assert len(errors) == 1, errors
    # the error lists the available names, so a near-miss is easy to fix
    assert "'holdase chaperone activity'" in errors[0].message


def test_proposed_molecular_function_needs_supporting_evidence():
    """A proposed activity can never trace to an annotation, so it must be grounded."""
    data = _holdase_review("holdase chaperone activity")
    del data["proposed_new_terms"][0]["supported_by"]
    errors = _pmf_errors(data)
    assert any("no supported_by" in e.message for e in errors), errors
    # evidence on the core function itself is also enough
    data["core_functions"][0]["supported_by"] = [
        {"reference_id": "PMID:12345", "supporting_text": "prevents aggregation"}
    ]
    assert not _pmf_errors(data)


def test_proposed_molecular_function_excludes_molecular_function():
    """Keeping the obsolete id alongside the proposal is the migration mistake to catch."""
    data = _holdase_review("holdase chaperone activity")
    data["core_functions"][0]["molecular_function"] = {
        "id": "GO:0051082",
        "label": "unfolded protein binding",
    }
    errors = _pmf_errors(data)
    assert any("both molecular_function and proposed_molecular_function" in e.message for e in errors), errors


def test_proposed_molecular_function_must_be_a_string():
    """A {id, label} term here is reported, not a crash that skips later checks."""
    data = _holdase_review("holdase chaperone activity")
    data["core_functions"][0]["proposed_molecular_function"] = {
        "id": "NTR",
        "label": "holdase chaperone activity",
    }
    errors = _pmf_errors(data)
    assert any("must be a proposed_new_terms name" in e.message for e in errors), errors


def test_ntr_replacement_label_should_name_a_proposed_term():
    """A MODIFY's NTR replacement should point at the same proposal as the core function."""
    data = _holdase_review("holdase chaperone activity")
    data["existing_annotations"][0]["review"] = {
        "action": "MODIFY",
        "reason": "Interim",
        "proposed_replacement_terms": [{"id": "NTR", "label": "something else"}],
    }
    assert any(
        i.check_type == "ntr_replacement_not_in_proposed_new_terms" for i in _issues(data)
    )
    data["existing_annotations"][0]["review"]["proposed_replacement_terms"][0]["label"] = (
        "holdase chaperone activity (NTR needed)"
    )
    assert not any(
        i.check_type == "ntr_replacement_not_in_proposed_new_terms" for i in _issues(data)
    )
