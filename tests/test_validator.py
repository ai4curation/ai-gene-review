"""Tests for the gene review validator.

Schema validation is handled by ``linkml-validate`` CLI (tested via subprocess).
Best-practices checks are tested via ``validate_gene_review()`` Python API.
"""

import subprocess
import tempfile
from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation import (
    validate_gene_review,
    validate_multiple_files,
    ValidationSeverity,
)
from ai_gene_review.validation.validator import get_schema_path


# ---------------------------------------------------------------------------
# Schema validation (linkml-validate CLI)
# ---------------------------------------------------------------------------

def test_schema_valid_file():
    """Test that a valid file passes schema validation via CLI."""
    yaml_file = Path("tests/input/CFAP300-ai-review.yaml")
    if not yaml_file.exists():
        pytest.skip("CFAP300 test input not found")

    result = subprocess.run(
        ["uv", "run", "linkml-validate",
         "--schema", str(get_schema_path()),
         "--target-class", "GeneReview",
         str(yaml_file)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, f"Valid file should pass: {result.stdout + result.stderr}"


def test_schema_invalid_file():
    """Test that missing required fields are caught by schema validation CLI."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump({"id": "TEST123"}, f)  # Missing gene_symbol
        temp_file = Path(f.name)

    try:
        result = subprocess.run(
            ["uv", "run", "linkml-validate",
             "--schema", str(get_schema_path()),
             "--target-class", "GeneReview",
             str(temp_file)],
            capture_output=True, text=True,
        )
        assert result.returncode != 0, "Missing gene_symbol should fail schema validation"
    finally:
        temp_file.unlink()


def test_schema_invalid_taxon_id():
    """Test that numeric taxon ID (should be string) is caught by schema validation CLI."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump({
            "id": "Q456",
            "gene_symbol": "GENE2",
            "description": "Test gene",
            "taxon": {"id": 9606, "label": "Homo sapiens"},
        }, f)
        temp_file = Path(f.name)

    try:
        result = subprocess.run(
            ["uv", "run", "linkml-validate",
             "--schema", str(get_schema_path()),
             "--target-class", "GeneReview",
             str(temp_file)],
            capture_output=True, text=True,
        )
        assert result.returncode != 0, "Numeric taxon ID should fail schema validation"
        assert "not of type 'string'" in result.stdout + result.stderr
    finally:
        temp_file.unlink()


# ---------------------------------------------------------------------------
# Best-practices validation (Python API)
# ---------------------------------------------------------------------------

def test_validate_valid_file():
    """Test best-practices validation of a valid gene review file."""
    yaml_file = Path("tests/input/CFAP300-ai-review.yaml")

    if yaml_file.exists():
        report = validate_gene_review(yaml_file)
        assert report.is_valid, (
            f"Valid file should pass validation, but got errors: {report.issues}"
        )
        assert report.error_count == 0


def test_validate_nonexistent_file():
    """Test validation of a non-existent file."""
    report = validate_gene_review("nonexistent.yaml")
    assert not report.is_valid
    assert any("not found" in issue.message.lower() for issue in report.issues)


def test_validate_multiple_files():
    """Test batch validation of multiple files."""
    test_files = []

    for i in range(2):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            yaml.dump({
                "id": f"Q{i}",
                "gene_symbol": f"GENE{i}",
                "description": f"Test gene {i}",
                "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            }, f)
            test_files.append(Path(f.name))

    try:
        batch_report = validate_multiple_files(test_files)
        assert len(batch_report.reports) == 2
        assert batch_report.valid_files == 2
    finally:
        for f in test_files:
            f.unlink()


def test_validation_summary():
    """Test the validation summary function."""
    from ai_gene_review.validation import BatchValidationReport, ValidationReport

    batch = BatchValidationReport()

    batch.reports.append(ValidationReport(file_path=Path("file1.yaml"), is_valid=True))
    batch.reports.append(ValidationReport(file_path=Path("file3.yaml"), is_valid=True))

    invalid_report = ValidationReport(file_path=Path("file2.yaml"), is_valid=False)
    invalid_report.add_issue(
        ValidationSeverity.ERROR,
        "Missing required field: gene_symbol",
        path="gene_symbol",
    )
    batch.reports.append(invalid_report)

    summary = batch.summary()

    assert "3" in summary
    assert "Valid: 2" in summary
    assert "Invalid: 1" in summary


@pytest.mark.parametrize(
    "gene_data,should_be_valid",
    [
        # Valid minimal structure
        (
            {
                "id": "Q123",
                "gene_symbol": "GENE1",
                "description": "Test gene",
                "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            },
            True,
        ),
        # Valid with references
        (
            {
                "id": "Q789",
                "gene_symbol": "GENE3",
                "description": "Test gene",
                "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
                "references": [{"id": "PMID:12345", "title": "Test paper"}],
            },
            True,
        ),
    ],
)
def test_various_gene_review_structures(gene_data, should_be_valid):
    """Test best-practices validation of various gene review structures."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(gene_data, f)
        temp_file = Path(f.name)

    try:
        report = validate_gene_review(temp_file, check_best_practices=False)
        if should_be_valid:
            assert report.is_valid, f"Should be valid but got errors: {report.issues}"
        else:
            assert not report.is_valid, "Should be invalid but passed validation"
    finally:
        temp_file.unlink()
