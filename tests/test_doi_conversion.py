"""Tests for DOI-to-PMID conversion functionality."""

import tempfile
from pathlib import Path

import pytest

from ai_gene_review.etl.publication import (
    doi_to_pmid,
    convert_doi_publication,
)


@pytest.mark.integration
def test_doi_to_pmid_returns_none_for_unfound():
    """doi_to_pmid should return None for a DOI that can't be resolved."""
    result = doi_to_pmid("10.9999/nonexistent-fake-doi-xyz")
    assert result is None


@pytest.mark.integration
def test_doi_to_pmid_real():
    """Test DOI-to-PMID resolution with a known mapping."""
    result = doi_to_pmid("10.1038/s41431-018-0141-z")
    assert result == "29727692"


def test_convert_doi_publication_creates_pmid_file():
    """convert_doi_publication should create a PMID-keyed file and remove the DOI file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pub_dir = Path(tmpdir)

        doi_content = """---
reference_id: DOI:10.1234/test.2024.001
title: Test Article Title
authors:
- Smith J
- Doe J
journal: Test Journal
year: '2024'
doi: 10.1234/test.2024.001
content_type: abstract_only
---

# Test Article Title
**Authors:** Smith J, Doe J
**Journal:** Test Journal (2024)

## Content

This is the abstract text.
"""
        doi_file = pub_dir / "DOI_10.1234_test.2024.001.md"
        doi_file.write_text(doi_content)

        result = convert_doi_publication(doi_file, pub_dir, pmid="99887766")

        assert result is True
        pmid_file = pub_dir / "PMID_99887766.md"
        assert pmid_file.exists()

        content = pmid_file.read_text()
        assert "pmid:" in content
        assert "full_text_available:" in content
        assert "reference_id:" not in content
        assert "content_type:" not in content

        assert not doi_file.exists()


def test_convert_doi_publication_skips_if_pmid_file_exists():
    """Should not overwrite an existing PMID file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pub_dir = Path(tmpdir)

        doi_file = pub_dir / "DOI_10.1234_test.md"
        doi_file.write_text("""---
reference_id: DOI:10.1234/test
title: Test
authors: []
journal: J
year: '2024'
doi: 10.1234/test
content_type: unavailable
---
# Test
""")

        pmid_file = pub_dir / "PMID_11111111.md"
        pmid_file.write_text("existing content")

        result = convert_doi_publication(doi_file, pub_dir, pmid="11111111")

        assert result is False
        assert pmid_file.read_text() == "existing content"
        assert doi_file.exists()
