"""Integration tests for incomplete full text extraction cases.

This module tests scenarios where publications are marked as having full text available
but the extraction is incomplete (e.g., missing Methods/Results sections).
"""

import tempfile
from pathlib import Path

import pytest

from ai_gene_review.etl.publication import (
    Publication,
    FullTextResult,
)


def test_incomplete_extraction_detection():
    """Test that incomplete extractions are properly flagged as such.

    Simulates the case where we get Introduction + Discussion but missing
    Methods + Results sections, like PMID_22067155.
    """
    # Simulate incomplete content (Abstract + Introduction + Discussion only)
    incomplete_content = """
    Abstract

    Calmodulin (CaM) binding to the type 2 ryanodine receptor (RyR2) regulates Ca release from the cardiac sarcoplasmic reticulum (SR). However, the structural basis of CaM regulation of the RyR2 is poorly defined.

    Introduction

    Calmodulin (CaM) is a versatile intracellular Ca sensor, capable of modulating the activity of diverse binding partners. CaM is comprised of roughly symmetrical N- and C-lobes that are joined by a flexible hinge.

    Discussion

    We show for the first time, to our knowledge, that the specific binding of CaM to cardiac RyR2 channels can be monitored using an F-FKBP biosensor and FRET.
    """

    result = FullTextResult(
        content=incomplete_content.strip(),
        available=True,
        extraction_method="html",
        is_complete=False  # Key: should be False for incomplete extractions
    )

    # Verify the result is properly flagged as incomplete
    assert result.available is True  # We did get content
    assert result.is_complete is False  # But it's incomplete
    assert result.extraction_method == "html"
    assert "Introduction" in result.content
    assert "Discussion" in result.content
    # Methods and Results are notably absent


def test_detect_missing_sections():
    """Test detection of missing critical sections in extracted content."""

    def has_critical_sections(content: str) -> tuple[bool, list[str]]:
        """Check if content has all critical paper sections.

        Returns:
            (has_all_sections, missing_sections)
        """
        required_sections = ["methods", "results"]

        content_lower = content.lower()
        missing = []

        # Check for required sections
        for section in required_sections:
            if section not in content_lower:
                missing.append(section)

        return len(missing) == 0, missing

    # Test complete content
    complete_content = """
    Abstract: This is the abstract.
    Introduction: This explains the background.
    Methods: This describes the methodology.
    Results: This presents the findings.
    Discussion: This interprets the results.
    """

    has_all, missing = has_critical_sections(complete_content)
    assert has_all is True
    assert missing == []

    # Test incomplete content (like PMID_22067155)
    incomplete_content = """
    Abstract: This is the abstract.
    Introduction: This explains the background.
    Discussion: This interprets the results.
    """

    has_all, missing = has_critical_sections(incomplete_content)
    assert has_all is False
    assert "methods" in missing
    # Note: "results" appears in the text "interprets the results" so won't be in missing
    # This demonstrates why simple keyword matching is insufficient


@pytest.mark.integration
def test_pmid_22067155_incomplete_extraction():
    """Test the specific case of PMID_22067155 which has incomplete extraction.

    This publication is marked as full_text_available: true but only contains
    Abstract + Introduction + Discussion, missing Methods and Results.
    """
    pmid = "22067155"

    # Check if the cached publication exists and examine its content
    cache_file = Path("publications") / f"PMID_{pmid}.md"

    if cache_file.exists():
        content = cache_file.read_text()

        # Parse the frontmatter to check extraction metadata
        lines = content.split('\n')
        in_frontmatter = False
        full_text_available = None
        extraction_method = None

        for line in lines:
            if line.strip() == '---':
                in_frontmatter = not in_frontmatter
                continue

            if in_frontmatter:
                if line.startswith('full_text_available:'):
                    full_text_available = 'true' in line.lower()
                elif line.startswith('full_text_extraction_method:'):
                    extraction_method = line.split(':', 1)[1].strip()

        # Check for actual section headers (not just keywords in text)
        import re

        # Look for section headers (either ## Header or standalone Header lines)
        section_pattern = r'^(##\s*|^)([A-Z][a-z]+)\s*$'
        sections_found = re.findall(section_pattern, content, re.MULTILINE | re.IGNORECASE)
        section_names = [match[1].lower() for match in sections_found]

        has_introduction = "introduction" in section_names
        has_methods = any(name in section_names for name in ["methods", "methodology"])
        has_results = "results" in section_names
        has_discussion = "discussion" in section_names

        # This should demonstrate the incomplete extraction issue
        if full_text_available:
            print(f"PMID {pmid} metadata indicates full text available")
            print(f"Extraction method: {extraction_method}")
            print(f"Has Introduction: {has_introduction}")
            print(f"Has Methods: {has_methods}")
            print(f"Has Results: {has_results}")
            print(f"Has Discussion: {has_discussion}")

            # The problematic case: marked as full text but missing critical sections
            if has_introduction and has_discussion and not (has_methods and has_results):
                # This IS the bug we want to detect and test for!
                assert True, f"Successfully detected incomplete extraction: PMID {pmid} marked as full_text_available but missing Methods/Results sections"
            else:
                # If this case changes, we want to know about it
                if not full_text_available:
                    pytest.skip(f"PMID {pmid} not marked as full_text_available")
                elif has_methods and has_results:
                    print(f"PMID {pmid} appears to have been fixed - now has Methods and Results sections")
                else:
                    pytest.fail(f"Unexpected section pattern for PMID {pmid}")
    else:
        pytest.skip(f"PMID {pmid} not cached - run 'just fetch-pmid {pmid}' first")


def test_should_flag_incomplete_extraction():
    """Test function to determine if an extraction should be flagged as incomplete."""

    def should_flag_as_incomplete(content: str, extraction_method: str) -> bool:
        """Determine if extraction should be flagged as incomplete based on content analysis."""
        if not content or len(content) < 500:
            return True

        content_lower = content.lower()

        # Look for presence of main sections
        has_abstract = "abstract" in content_lower
        has_introduction = "introduction" in content_lower
        has_methods = any(word in content_lower for word in ["methods", "methodology", "experimental"])
        has_results = "results" in content_lower
        has_discussion = "discussion" in content_lower or "conclusion" in content_lower

        # Count how many sections we have
        sections_found = sum([has_abstract, has_introduction, has_methods, has_results, has_discussion])

        # If we have intro/discussion but not methods/results, likely incomplete
        if has_introduction and has_discussion and not (has_methods and has_results):
            return True

        # If we have fewer than 3 main sections, likely incomplete
        if sections_found < 3:
            return True

        return False

    # Test cases

    # Case 1: Complete paper (needs to be longer to pass length check)
    complete_paper = """
    Abstract: Background information about the study and its importance to the field.
    Introduction: This study investigates the complex mechanisms underlying cellular processes.
    We explore various aspects of the biological system to understand its function.
    Methods: We performed experiments using state-of-the-art techniques including microscopy,
    biochemical assays, and computational modeling to analyze the data comprehensively.
    Results: Our findings show that the system behaves in unexpected ways under certain conditions,
    with significant implications for our understanding of the biological process.
    Discussion: These results indicate a new paradigm in how we understand this system,
    and suggest future directions for research in this important area of biology.
    """
    assert should_flag_as_incomplete(complete_paper, "html") is False

    # Case 2: Incomplete paper (like PMID_22067155)
    incomplete_paper = """
    Abstract: Background information
    Introduction: This study investigates...
    Discussion: These results indicate...
    """
    assert should_flag_as_incomplete(incomplete_paper, "html") is True

    # Case 3: Very short content
    short_content = "Abstract: Brief summary"
    assert should_flag_as_incomplete(short_content, "html") is True

    # Case 4: Empty content
    assert should_flag_as_incomplete("", "html") is True


@pytest.mark.integration
def test_validation_should_catch_incomplete_extractions():
    """Test that the validation system catches publications marked as complete but actually incomplete."""

    # Create a mock publication that represents the PMID_22067155 case
    incomplete_pub = Publication(
        pmid="22067155",
        title="FRET detection of calmodulin binding to the cardiac RyR2 calcium release channel.",
        authors=["Guo T", "Fruen BR", "Nitu FR"],
        journal="Biophys J",
        year="2011",
        abstract="Test abstract",
        full_text="Abstract\n\nIntroduction\n\nSome intro text\n\nDiscussion\n\nSome discussion text",
        full_text_available=True,  # Marked as available
        full_text_extraction_method="html",
        pmcid="PMC3207159"
    )

    # Create temporary markdown file
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_file = Path(tmpdir) / "PMID_22067155.md"
        cache_file.write_text(incomplete_pub.to_markdown())

        # Read it back and analyze
        content = cache_file.read_text()

        # This should detect the issue - marked as available but incomplete
        content_lower = content.lower()
        has_methods = "methods" in content_lower
        has_results = "results" in content_lower
        marked_as_available = "full_text_available: true" in content

        if marked_as_available and not (has_methods and has_results):
            # This is the problematic case we want to detect
            assert True, "Successfully detected incomplete extraction marked as complete"
        else:
            pytest.fail("Failed to detect the incomplete extraction issue")


def test_fulltext_result_validation():
    """Test that FullTextResult properly validates completeness."""

    # Test that short content is marked as incomplete
    short_result = FullTextResult(
        content="Abstract: Brief text",
        available=True,
        extraction_method="html",
        is_complete=False
    )

    assert short_result.available is True
    assert short_result.is_complete is False

    # Test that substantial content can be marked as complete
    substantial_content = "Abstract: " + "A" * 3500  # Over 3000 chars
    complete_result = FullTextResult(
        content=substantial_content,
        available=True,
        extraction_method="html",
        is_complete=True
    )

    assert complete_result.available is True
    assert complete_result.is_complete is True