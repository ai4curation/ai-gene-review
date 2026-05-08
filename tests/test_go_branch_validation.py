"""Test validation of GO term branch constraints in core_functions.

GO branch validation is handled by linkml-term-validator CLI with
dynamic enums defined in the schema (e.g., GOMolecularActivityEnum).
These tests invoke the CLI tool via subprocess.
"""

import subprocess
import tempfile
from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.validator import get_schema_path


def _run_term_validator(yaml_file: Path) -> subprocess.CompletedProcess:
    """Run linkml-term-validator on a file and return the result."""
    return subprocess.run(
        [
            "uv", "run", "linkml-term-validator", "validate-data",
            str(yaml_file),
            "-s", str(get_schema_path()),
            "-t", "GeneReview",
            "--labels",
            "-c", "conf/oak_config.yaml",
        ],
        capture_output=True, text=True,
    )


def test_molecular_function_must_be_mf_branch():
    """Test that molecular_function field requires MF branch GO terms."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for GO branch validation",
        "core_functions": [
            {
                "description": "Test function",
                "molecular_function": {
                    "id": "GO:0008150",  # biological_process root - wrong branch!
                    "label": "biological_process",
                },
            }
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        result = _run_term_validator(temp_path)
        output = result.stdout + result.stderr
        assert "GO:0008150" in output and "GOMolecularActivityEnum" in output, (
            f"Expected branch error for GO:0008150 in MF slot, got: {output}"
        )
    finally:
        temp_path.unlink()


def test_directly_involved_in_must_be_bp_branch():
    """Test that directly_involved_in field requires BP branch GO terms."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST2",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for GO branch validation",
        "core_functions": [
            {
                "description": "Test function",
                "molecular_function": {
                    "id": "GO:0003674",
                    "label": "molecular_function",
                },
                "directly_involved_in": [
                    {
                        "id": "GO:0003674",  # molecular_function root - wrong branch!
                        "label": "molecular_function",
                    }
                ],
            }
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        result = _run_term_validator(temp_path)
        output = result.stdout + result.stderr
        # GO:0003674 should fail in directly_involved_in (BP slot)
        assert "GO:0003674" in output and "GOBiologicalProcessEnum" in output, (
            f"Expected branch error for GO:0003674 in BP slot, got: {output}"
        )
    finally:
        temp_path.unlink()


def test_locations_must_be_cc_branch():
    """Test that locations field requires CC branch GO terms."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST3",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene for GO branch validation",
        "core_functions": [
            {
                "description": "Test function",
                "molecular_function": {
                    "id": "GO:0003674",
                    "label": "molecular_function",
                },
                "locations": [
                    {
                        "id": "GO:0008150",  # biological_process root - wrong branch!
                        "label": "biological_process",
                    }
                ],
            }
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        result = _run_term_validator(temp_path)
        output = result.stdout + result.stderr
        assert "GO:0008150" in output and "GOCellularLocationEnum" in output, (
            f"Expected branch error for GO:0008150 in CC slot, got: {output}"
        )
    finally:
        temp_path.unlink()


def test_correct_go_branches_pass():
    """Test that correctly placed GO terms pass validation."""
    data = {
        "id": "Q12345",
        "gene_symbol": "TEST4",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene with correct GO branches",
        "core_functions": [
            {
                "description": "Test function with correct branches",
                "molecular_function": {
                    "id": "GO:0003723",  # RNA binding - MF branch
                    "label": "RNA binding",
                },
                "directly_involved_in": [
                    {
                        "id": "GO:0006397",  # mRNA processing - BP branch
                        "label": "mRNA processing",
                    }
                ],
                "locations": [
                    {
                        "id": "GO:0005634",  # nucleus - CC branch
                        "label": "nucleus",
                    }
                ],
            }
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_path = Path(f.name)

    try:
        result = _run_term_validator(temp_path)
        output = result.stdout + result.stderr
        assert "Validation passed" in output, (
            f"Correct branches should pass, got: {output}"
        )
    finally:
        temp_path.unlink()


@pytest.mark.integration
def test_real_gene_branch_validation():
    """Test GO branch validation on a real gene file that should pass."""
    cfap300_file = Path("genes/human/CFAP300/CFAP300-ai-review.yaml")
    if not cfap300_file.exists():
        pytest.skip("CFAP300 file not found")

    result = _run_term_validator(cfap300_file)
    output = result.stdout + result.stderr
    assert "Validation passed" in output, (
        f"CFAP300 should pass branch validation, got: {output}"
    )
