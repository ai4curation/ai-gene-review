"""Test supporting_text validation with whitespace handling.

This test module specifically addresses false positives in the validation
where text that exists in publications is not found due to line breaks.
"""

import pytest
from pathlib import Path
import tempfile
from ai_gene_review.validation.supporting_text_validator import SupportingTextValidator


def test_multiline_text_matching():
    """Test that text split across multiple lines is correctly matched.

    This addresses the issue where text like:
    "The mutant GATA3 significantly reduced luciferase
    reporter activity by more than 65% (P < 0.001)"

    Is not found when the supporting_text is:
    "The mutant GATA3 significantly reduced luciferase reporter activity by more than 65% (P < 0.001)."
    """
    validator = SupportingTextValidator()

    # Simulate the actual publication content with line break
    publication_content = """
    demonstrated that the mutant GATA3 resulted in a loss of interaction with ZnF1
    and ZnF6 of the cofactor FOG2. The mutant GATA3 significantly reduced luciferase
    reporter activity by more than 65% (P < 0.001), and three-dimensional modeling
    """

    # The supporting_text as it appears in the YAML (single line)
    supporting_text = "The mutant GATA3 significantly reduced luciferase reporter activity by more than 65% (P < 0.001)."

    # This should find the text despite the line break
    found, score, best_match = validator._find_single_text_in_publication(
        supporting_text, publication_content
    )

    assert found, f"Text should be found. Score: {score}, Best match: {best_match}"
    assert score >= 0.85, f"Similarity score should be high, got {score}"


def test_normalize_preserves_essential_content():
    """Test that normalization doesn't lose essential content."""
    validator = SupportingTextValidator()

    # Test with the actual problematic text
    text1 = "The mutant GATA3 significantly reduced luciferase reporter activity by more than 65% (P < 0.001)."
    text2 = """The mutant GATA3 significantly reduced luciferase
    reporter activity by more than 65% (P < 0.001)"""

    norm1 = validator.normalize_text(text1)
    norm2 = validator.normalize_text(text2)

    # After normalization, these should be identical or very similar
    assert norm1 == norm2, f"Normalized texts should match:\n{norm1}\nvs\n{norm2}"


def test_exact_substring_with_newlines():
    """Test that exact substring matching works even with newlines in source."""
    validator = SupportingTextValidator()

    # The publication has newlines
    publication = "This is line one.\nThis continues on line two."

    # Supporting text without newline
    supporting_text = "This is line one. This continues on line two."

    # Should still find it after normalization
    found, score, _ = validator._find_single_text_in_publication(
        supporting_text, publication
    )

    assert found, "Should find text that spans lines"


def test_sentence_splitter_handles_multiline():
    """Test that sentence splitter doesn't break on mid-sentence newlines."""
    validator = SupportingTextValidator()

    text = """The mutant GATA3 significantly reduced luciferase
    reporter activity by more than 65% (P < 0.001). This is another sentence."""

    sentences = validator.split_into_sentences(text)

    # Should get two sentences, not three
    # The first sentence should contain the full text despite the newline
    assert len([s for s in sentences if len(s) > 20]) <= 2

    # Check that the full first sentence is preserved
    full_text_normalized = validator.normalize_text(text)
    assert "mutant gata3 significantly reduced luciferase reporter activity" in full_text_normalized


@pytest.mark.parametrize("line_ending", ["\n", "\r\n", "\r"])
def test_different_line_endings(line_ending):
    """Test that different line ending styles are handled correctly."""
    validator = SupportingTextValidator()

    publication = f"First part{line_ending}second part of the same sentence."
    supporting_text = "First part second part of the same sentence."

    found, score, _ = validator._find_single_text_in_publication(
        supporting_text, publication
    )

    assert found, f"Should find text with {repr(line_ending)} line ending"


def test_real_pmid_19723756_case():
    """Test the actual case from PMID:19723756 that's causing false positives."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pub_dir = Path(tmpdir)

        # Create the publication file with the actual content
        pub_file = pub_dir / "PMID_19723756.md"
        pub_content = """---
pmid: '19723756'
title: A missense GATA3 mutation causes HDR syndrome
---

# Abstract

EMSAs showed it to reduce DNA binding affinity, but not stability, and yeast two-hybrid assays
demonstrated that the mutant GATA3 resulted in a loss of interaction with ZnF1
and ZnF6 of the cofactor FOG2. The mutant GATA3 significantly reduced luciferase
reporter activity by more than 65% (P < 0.001), and three-dimensional modeling
predicted disruption of ZnF1 structure.
"""
        pub_file.write_text(pub_content)

        validator = SupportingTextValidator(publications_dir=pub_dir)

        # Test the exact supporting_text from the YAML
        supporting_text = "The mutant GATA3 significantly reduced luciferase reporter activity by more than 65% (P < 0.001)."

        # Load the publication
        pub_text = validator.load_publication("19723756")
        assert pub_text is not None

        # Find the text
        found, score, best_match = validator._find_single_text_in_publication(
            supporting_text, pub_text
        )

        assert found, f"Should find the text. Score: {score}, Best match: {best_match}"
        assert score >= 0.85, f"Score should be >= 0.85, got {score}"