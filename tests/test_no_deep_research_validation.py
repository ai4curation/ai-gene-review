"""Test validation for NoDeepResearchResults check."""

import pytest
from pathlib import Path
import tempfile
import yaml
from ai_gene_review.validation import validate_gene_review, ValidationSeverity


def test_no_deep_research_warning():
    """Test that warning is raised when deep research files exist but are not referenced.

    This test verifies the NoDeepResearchResults validation check which ensures
    that if deep research files (*research*.md) are available, at least some
    annotations should reference them in their supported_by fields.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)

        # Create a deep research file
        research_file = tmpdir_path / "TEST-deep-research.md"
        research_file.write_text("""# Deep Research for TEST Gene

        This gene has been studied extensively...
        """)

        # Create another research file
        falcon_file = tmpdir_path / "TEST-falcon-research.md"
        falcon_file.write_text("# Falcon research results")

        # Create a YAML file with annotations that don't reference the research
        yaml_data = {
            "id": "Q12345",
            "gene_symbol": "TEST",
            "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            "description": "Test gene for validation",
            "references": [
                {"id": "PMID:12345", "title": "Test paper"}
            ],
            "existing_annotations": [
                {
                    "term": {"id": "GO:0005515", "label": "protein binding"},
                    "evidence_type": "IDA",
                    "original_reference_id": "PMID:12345",
                    "review": {
                        "action": "ACCEPT",
                        "supported_by": [
                            {
                                "reference_id": "PMID:12345",
                                "supporting_text": "The protein binds..."
                            }
                        ]
                    }
                }
            ]
        }

        yaml_file = tmpdir_path / "TEST-ai-review.yaml"
        with open(yaml_file, "w") as f:
            yaml.dump(yaml_data, f)

        # Validate - should get warning about unused research files
        report = validate_gene_review(yaml_file, check_best_practices=True)

        # Find the specific warning
        warning_found = False
        for issue in report.issues:
            if (issue.severity == ValidationSeverity.WARNING and
                issue.check_type == "no_deep_research_results" and
                "TEST-deep-research.md" in issue.message):
                warning_found = True
                break

        assert warning_found, "Should warn about unused deep research files"


def test_deep_research_referenced_no_warning():
    """Test that no warning is raised when deep research is properly referenced."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)

        # Create a deep research file
        research_file = tmpdir_path / "TEST-deep-research.md"
        research_file.write_text("# Deep Research for TEST Gene")

        # Create a YAML file with annotations that DO reference the research
        yaml_data = {
            "id": "Q12345",
            "gene_symbol": "TEST",
            "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            "description": "Test gene for validation",
            "references": [
                {"id": "PMID:12345", "title": "Test paper"},
                {"id": "file:TEST-deep-research.md", "title": "Deep research"}
            ],
            "existing_annotations": [
                {
                    "term": {"id": "GO:0005515", "label": "protein binding"},
                    "evidence_type": "IDA",
                    "original_reference_id": "PMID:12345",
                    "review": {
                        "action": "ACCEPT",
                        "supported_by": [
                            {
                                "reference_id": "file:TEST-deep-research.md",
                                "supporting_text": "Based on deep analysis..."
                            }
                        ]
                    }
                }
            ]
        }

        yaml_file = tmpdir_path / "TEST-ai-review.yaml"
        with open(yaml_file, "w") as f:
            yaml.dump(yaml_data, f)

        # Validate - should NOT get warning about unused research
        report = validate_gene_review(yaml_file, check_best_practices=True)

        # Verify no warning about deep research
        warning_found = False
        for issue in report.issues:
            if issue.check_type == "no_deep_research_results":
                warning_found = True
                break

        assert not warning_found, "Should NOT warn when deep research is referenced"


def test_no_research_files_no_warning():
    """Test that no warning is raised when no research files exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)

        # Create a YAML file without any research files in directory
        yaml_data = {
            "id": "Q12345",
            "gene_symbol": "TEST",
            "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            "description": "Test gene for validation",
            "existing_annotations": [
                {
                    "term": {"id": "GO:0005515", "label": "protein binding"},
                    "evidence_type": "IDA",
                    "original_reference_id": "PMID:12345",
                    "review": {
                        "action": "ACCEPT"
                    }
                }
            ]
        }

        yaml_file = tmpdir_path / "TEST-ai-review.yaml"
        with open(yaml_file, "w") as f:
            yaml.dump(yaml_data, f)

        # Validate - should NOT get warning when no research files exist
        report = validate_gene_review(yaml_file, check_best_practices=True)

        # Verify no warning about deep research
        warning_found = False
        for issue in report.issues:
            if issue.check_type == "no_deep_research_results":
                warning_found = True
                break

        assert not warning_found, "Should NOT warn when no research files exist"


@pytest.mark.parametrize("research_filename", [
    "TEST-openai-research.md",
    "TEST-falcon-research.md",
    "TEST-llm-research-notes.md",
    "TEST-research-summary.md",
    "research-TEST.md"
])
def test_various_research_file_patterns(research_filename):
    """Test that various research file naming patterns are detected."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)

        # Create a research file with the given name
        research_file = tmpdir_path / research_filename
        research_file.write_text("# Research content")

        # Create YAML without referencing the research
        yaml_data = {
            "id": "Q12345",
            "gene_symbol": "TEST",
            "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            "description": "Test gene",
            "existing_annotations": [
                {
                    "term": {"id": "GO:0005515", "label": "protein binding"},
                    "evidence_type": "IDA",
                    "original_reference_id": "PMID:12345",
                    "review": {"action": "REMOVE"}
                }
            ]
        }

        yaml_file = tmpdir_path / "TEST-ai-review.yaml"
        with open(yaml_file, "w") as f:
            yaml.dump(yaml_data, f)

        # Validate
        report = validate_gene_review(yaml_file, check_best_practices=True)

        # Should warn about the unused research file
        warning_found = False
        for issue in report.issues:
            if (issue.check_type == "no_deep_research_results" and
                research_filename in issue.message):
                warning_found = True
                break

        assert warning_found, f"Should detect and warn about unused {research_filename}"