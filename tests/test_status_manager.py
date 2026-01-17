"""Tests for status manager module."""

import tempfile
from pathlib import Path
import yaml


from ai_gene_review.status_manager import (
    compute_status_from_data,
    compute_status_from_file,
    check_and_update_status,
)


def test_compute_status_initialized():
    """Test status computation for INITIALIZED state (all PENDING)."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "existing_annotations": [
            {"review": {"action": "PENDING"}},
            {"review": {"action": "PENDING"}},
            {"review": {"action": "PENDING"}},
        ],
    }
    assert compute_status_from_data(data) == "INITIALIZED"


def test_compute_status_in_progress():
    """Test status computation for IN_PROGRESS state (some PENDING, some not)."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "existing_annotations": [
            {"review": {"action": "PENDING"}},
            {"review": {"action": "ACCEPT"}},
            {"review": {"action": "PENDING"}},
        ],
    }
    assert compute_status_from_data(data) == "IN_PROGRESS"


def test_compute_status_complete():
    """Test status computation for COMPLETE state (no PENDING, no warnings)."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "existing_annotations": [
            {"review": {"action": "ACCEPT"}},
            {"review": {"action": "MODIFY"}},
            {"review": {"action": "REMOVE"}},
        ],
    }
    # Without validation report, assumes no warnings
    assert compute_status_from_data(data) == "COMPLETE"


def test_compute_status_no_annotations():
    """Test status computation with no annotations."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "existing_annotations": [],
    }
    assert compute_status_from_data(data) == "INITIALIZED"


def test_compute_status_from_file():
    """Test computing status from a YAML file."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IPI",
                "review": {"action": "ACCEPT"},
            },
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_file = Path(f.name)

    try:
        # Without validation check (faster)
        status, report = compute_status_from_file(temp_file, check_validation=False)
        assert status == "COMPLETE"
        assert report is None
    finally:
        temp_file.unlink()


def test_check_and_update_status_dry_run():
    """Test checking status without updating the file."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IPI",
                "review": {"action": "PENDING"},
            },
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_file = Path(f.name)

    try:
        # Dry run should not update the file
        result = check_and_update_status(temp_file, dry_run=True)

        assert result["needs_update"] is True
        assert result["current_status"] is None
        assert result["expected_status"] == "INITIALIZED"
        assert result["updated"] is False

        # Verify file wasn't changed
        with open(temp_file, "r") as f:
            updated_data = yaml.safe_load(f)
        assert "status" not in updated_data
    finally:
        temp_file.unlink()


def test_check_and_update_status_update():
    """Test updating status in a file."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IPI",
                "review": {"action": "ACCEPT"},
            },
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_file = Path(f.name)

    try:
        # Update should modify the file
        result = check_and_update_status(temp_file, dry_run=False)

        assert result["needs_update"] is True
        assert result["current_status"] is None
        assert result["updated"] is True

        # Verify file was changed
        with open(temp_file, "r") as f:
            updated_data = yaml.safe_load(f)
        assert "status" in updated_data
        # We can't predict exact status without full validation,
        # but it should be set
        assert updated_data["status"] in ["INITIALIZED", "IN_PROGRESS", "DRAFT", "COMPLETE"]
    finally:
        temp_file.unlink()


def test_check_and_update_status_mismatch():
    """Test detecting status mismatch."""
    data = {
        "id": "Q123",
        "gene_symbol": "TEST1",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "status": "COMPLETE",  # Wrong status
        "existing_annotations": [
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "evidence_type": "IPI",
                "review": {"action": "PENDING"},
            },
        ],
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(data, f)
        temp_file = Path(f.name)

    try:
        result = check_and_update_status(temp_file, dry_run=True)

        assert result["needs_update"] is False
        assert result["status_mismatch"] is True
        assert result["current_status"] == "COMPLETE"
        assert result["expected_status"] == "INITIALIZED"
    finally:
        temp_file.unlink()
