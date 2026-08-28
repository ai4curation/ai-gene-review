"""Test validation of reference IDs in annotations."""

from pathlib import Path
import tempfile
import pytest
import yaml

from ai_gene_review.validation import validate_gene_review, ValidationSeverity
from ai_gene_review.validation import validator as validator_module


def test_valid_reference_ids():
    """Test that annotations with valid reference IDs pass validation."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for validation",
        "references": [
            {"id": "PMID:12345", "title": "Test paper 1"},
            {"id": "PMID:67890", "title": "Test paper 2"},
        ],
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IPI",
                "original_reference_id": "PMID:12345",
                "review": {"summary": "Valid reference", "action": "ACCEPT"},
            },
            {
                "term": {"id": "GO:0005737", "label": "cytoplasm"},
                "evidence_type": "ISS",
                "original_reference_id": "PMID:67890",
                "review": {"summary": "Another valid reference", "action": "ACCEPT"},
            },
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        # Disable best practices to avoid term validation errors
        report = validate_gene_review(temp_path, check_best_practices=False)
        # Should not have any errors about reference IDs
        ref_errors = [
            issue
            for issue in report.issues
            if issue.severity == ValidationSeverity.ERROR
            and "non-existent reference ID" in issue.message
        ]
        assert len(ref_errors) == 0, f"Unexpected reference errors: {ref_errors}"
        assert report.is_valid
    finally:
        temp_path.unlink()


def _finding_quote_review(*findings, reference_flag=False):
    """Build a minimal review containing parent-PMID finding quotes."""
    reference = {
        "id": "PMID:12345",
        "title": "Test publication",
        "findings": list(findings),
    }
    if reference_flag:
        reference["full_text_unavailable"] = True
    return {
        "id": "P10592",
        "gene_symbol": "SSA2",
        "taxon": {"id": "NCBITaxon:559292", "label": "Saccharomyces cerevisiae"},
        "description": "A test review with reference findings.",
        "references": [reference],
    }


def _write_cached_publication(tmp_path, *, full_text_available):
    publications_dir = tmp_path / "publications"
    publications_dir.mkdir()
    availability = "true" if full_text_available else "false"
    (publications_dir / "PMID_12345.md").write_text(
        f"---\nfull_text_available: {availability}\n---\n\n"
        "This exact evidence sentence is cached.\n"
    )


def test_reference_finding_supporting_text_is_validated(tmp_path, monkeypatch):
    """The public validation path accepts exact text and rejects fabricated text."""
    _write_cached_publication(tmp_path, full_text_available=True)
    monkeypatch.setattr(validator_module, "get_project_root", lambda: tmp_path)
    data = {
        **_finding_quote_review(
            {
                "statement": "Grounded result.",
                "supporting_text": "This exact evidence sentence is cached.",
            },
            {
                "statement": "Invented result.",
                "supporting_text": "This sentence is not in the publication.",
            },
        )
    }

    review_path = tmp_path / "review.yaml"
    review_path.write_text(yaml.safe_dump(data))
    report = validate_gene_review(review_path, check_goa=False)
    quote_errors = [
        issue
        for issue in report.issues
        if issue.check_type == "reference_finding_supporting_text"
        and issue.severity == ValidationSeverity.ERROR
    ]
    assert len(quote_errors) == 1
    assert quote_errors[0].path == "references[0].findings[1].supporting_text"


def test_abstract_only_finding_mismatch_is_warning(tmp_path, monkeypatch):
    """A quote absent from an abstract-only cache does not block validation."""
    _write_cached_publication(tmp_path, full_text_available=False)
    monkeypatch.setattr(validator_module, "get_project_root", lambda: tmp_path)
    review_path = tmp_path / "review.yaml"
    review_path.write_text(
        yaml.safe_dump(
            _finding_quote_review(
                {
                    "statement": "Full-text result.",
                    "supporting_text": "A sentence available only in full text.",
                }
            )
        )
    )

    report = validate_gene_review(review_path, check_goa=False)
    quote_issues = [
        issue
        for issue in report.issues
        if issue.check_type == "reference_finding_supporting_text"
    ]
    assert len(quote_issues) == 1
    assert quote_issues[0].severity == ValidationSeverity.WARNING


@pytest.mark.parametrize("flag_location", ["reference", "finding"])
def test_full_text_unavailable_flag_downgrades_mismatch(
    tmp_path, monkeypatch, flag_location
):
    """Reference- and finding-level escape hatches prevent false hard errors."""
    _write_cached_publication(tmp_path, full_text_available=True)
    monkeypatch.setattr(validator_module, "get_project_root", lambda: tmp_path)
    finding = {
        "statement": "Full-text result.",
        "supporting_text": "A sentence available only in uncached full text.",
    }
    if flag_location == "finding":
        finding["full_text_unavailable"] = True
    data = _finding_quote_review(
        finding,
        reference_flag=flag_location == "reference",
    )
    review_path = tmp_path / "review.yaml"
    review_path.write_text(yaml.safe_dump(data))

    report = validate_gene_review(review_path, check_goa=False)
    quote_issues = [
        issue
        for issue in report.issues
        if issue.check_type == "reference_finding_supporting_text"
    ]
    assert len(quote_issues) == 1
    assert quote_issues[0].severity == ValidationSeverity.WARNING


def test_invalid_reference_id():
    """Test that annotations with invalid reference IDs are caught."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST2",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for validation with bad reference",
        "references": [{"id": "PMID:12345", "title": "Test paper 1"}],
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IPI",
                "original_reference_id": "PMID:12345",
                "review": {"summary": "Valid reference", "action": "ACCEPT"},
            },
            {
                "term": {"id": "GO:0005737", "label": "cytoplasm"},
                "evidence_type": "ISS",
                "original_reference_id": "PMID:99999",  # This ID doesn't exist in references
                "review": {"summary": "Invalid reference", "action": "ACCEPT"},
            },
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        # Enable best practices to check references (this is what we're testing)
        report = validate_gene_review(temp_path, check_best_practices=True)
        # Should have an error about the invalid reference ID
        ref_errors = [
            issue
            for issue in report.issues
            if issue.severity == ValidationSeverity.ERROR
            and "PMID:99999" in issue.message
        ]
        assert len(ref_errors) == 1, (
            f"Expected 1 reference error, got {len(ref_errors)}: {ref_errors}"
        )
        # The file might not be valid overall due to other checks, but we should have the ref error
        assert "non-existent reference ID" in ref_errors[0].message
    finally:
        temp_path.unlink()


def test_annotations_without_references():
    """Test that annotations work when no references section exists."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST3",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene without references section",
        # No references section at all
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IPI",
                "original_reference_id": "PMID:12345",
                "review": {
                    "summary": "Reference without references section",
                    "action": "ACCEPT",
                },
            }
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        report = validate_gene_review(temp_path)
        # Should have an error about the missing reference
        ref_errors = [
            issue
            for issue in report.issues
            if issue.severity == ValidationSeverity.ERROR
            and "PMID:12345" in issue.message
        ]
        assert len(ref_errors) == 1, (
            f"Expected 1 reference error, got {len(ref_errors)}"
        )
        assert not report.is_valid

        # Should also have a warning about missing references section
        ref_warnings = [
            issue
            for issue in report.issues
            if issue.severity == ValidationSeverity.WARNING
            and "No references provided" in issue.message
        ]
        assert len(ref_warnings) == 1
    finally:
        temp_path.unlink()


def test_annotation_without_original_reference_id():
    """Test that annotations without original_reference_id are OK."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST4",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene with annotation lacking reference ID",
        "references": [{"id": "PMID:12345", "title": "Test paper"}],
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IEA",
                # No original_reference_id field
                "review": {"summary": "Automated annotation", "action": "ACCEPT"},
            }
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        # Disable best practices to avoid term validation errors
        report = validate_gene_review(temp_path, check_best_practices=False)
        # Should not have errors about reference IDs
        ref_errors = [
            issue
            for issue in report.issues
            if issue.severity == ValidationSeverity.ERROR
            and "non-existent reference ID" in issue.message
        ]
        assert len(ref_errors) == 0
        assert report.is_valid
    finally:
        temp_path.unlink()
