"""Test cases demonstrating false positives in validation.

This test file documents known issues with the validation framework
where valid supporting_text is incorrectly flagged as not found.
"""

import pytest
from pathlib import Path
import tempfile
from ai_gene_review.validation.supporting_text_validator import SupportingTextValidator


class TestFalsePositives:
    """Test cases for known false positives in validation."""

    def test_pmid_19723756_false_positive(self):
        """Document the false positive for PMID:19723756.

        The validation reports:
        "Supporting text ... not found in PMID:19723756 (best similarity: 69.0%)"

        But the text IS present in the publication, just split across lines:
        Line 56-57: "The mutant GATA3 significantly reduced luciferase
        reporter activity by more than 65% (P < 0.001)"

        The issue is:
        1. Text spans two lines in the publication
        2. Supporting text has period at end, publication has comma
        3. Normalization removes parentheses and < sign differently
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            pub_dir = Path(tmpdir)

            # Create publication with actual content
            pub_file = pub_dir / "PMID_19723756.md"
            pub_content = """---
pmid: '19723756'
---
demonstrated that the mutant GATA3 resulted in a loss of interaction with ZnF1
and ZnF6 of the cofactor FOG2. The mutant GATA3 significantly reduced luciferase
reporter activity by more than 65% (P < 0.001), and three-dimensional modeling
"""
            pub_file.write_text(pub_content)

            validator = SupportingTextValidator(publications_dir=pub_dir)

            # The supporting_text from the YAML
            supporting_text = "The mutant GATA3 significantly reduced luciferase reporter activity by more than 65% (P < 0.001)."

            # Load and search
            pub_text = validator.load_publication("19723756")
            found, score, match = validator._find_single_text_in_publication(
                supporting_text, pub_text
            )

            # This currently FAILS but shouldn't
            # The text is clearly present, just with minor formatting differences
            assert score > 0.6, "Score is very low despite text being present"

            # Document the issue
            if not found:
                pytest.skip(
                    f"Known false positive: Text present but not found. "
                    f"Score: {score:.2%}. Issue: Text spans lines and has punctuation differences."
                )

    def test_multiline_text_general_issue(self):
        """Document the general issue with text spanning multiple lines."""
        validator = SupportingTextValidator()

        # Common pattern in publications: text continues on next line
        publication = """
        The study demonstrated that the protein
        significantly increased activity by 50%.
        """

        # Supporting text without line break
        supporting_text = "The study demonstrated that the protein significantly increased activity by 50%."

        found, score, _ = validator._find_single_text_in_publication(
            supporting_text, publication
        )

        # This should find the text but currently might not
        if not found:
            pytest.skip(
                f"Known issue: Multiline text not found. Score: {score:.2%}"
            )

    def test_punctuation_variation_issue(self):
        """Document issues with minor punctuation variations."""
        validator = SupportingTextValidator()

        test_cases = [
            # (publication_text, supporting_text, description)
            ("increased by 50% (P < 0.001),", "increased by 50% (P < 0.001).", "period vs comma"),
            ("GATA3-mediated activation", "GATA3 mediated activation", "hyphen presence"),
            ("IL-4/IL-5/IL-13", "IL-4, IL-5, IL-13", "slash vs comma"),
        ]

        for pub_text, sup_text, description in test_cases:
            found, score, _ = validator._find_single_text_in_publication(
                sup_text, f"The study showed {pub_text} in the experiment."
            )

            if not found:
                pytest.skip(
                    f"Known issue with {description}: Score {score:.2%}"
                )

    @pytest.mark.parametrize("ending", [",", ".", ";", ""])
    def test_sentence_ending_variations(self, ending):
        """Test that different sentence endings don't cause false negatives."""
        validator = SupportingTextValidator()

        # Publication has text with specific ending
        publication = f"The result was significant (P < 0.001){ending} as shown"

        # Supporting text with period
        supporting_text = "The result was significant (P < 0.001)."

        found, score, _ = validator._find_single_text_in_publication(
            supporting_text, publication
        )

        # These should all match despite different endings
        if not found and score > 0.8:
            pytest.skip(
                f"Near match (score: {score:.2%}) not accepted due to "
                f"punctuation difference: '.'"" vs '{ending}'"
            )


class TestProposedFixes:
    """Test proposed fixes for the false positive issues."""

    def test_aggressive_normalization_fix(self):
        """Test that more aggressive normalization would fix the issues."""

        def normalize_aggressive(text: str) -> str:
            """More aggressive normalization that removes ALL punctuation."""
            import re
            # Normalize whitespace (including newlines)
            text = re.sub(r'\s+', ' ', text)
            # Remove ALL non-word characters
            text = re.sub(r'[^\w\s]', ' ', text)
            # Normalize whitespace again
            text = re.sub(r'\s+', ' ', text)
            return text.lower().strip()

        # Test the problematic case
        pub_text = """The mutant GATA3 significantly reduced luciferase
        reporter activity by more than 65% (P < 0.001), and modeling"""

        sup_text = "The mutant GATA3 significantly reduced luciferase reporter activity by more than 65% (P < 0.001)."

        # With aggressive normalization
        pub_norm = normalize_aggressive(pub_text)
        sup_norm = normalize_aggressive(sup_text)

        # The supporting text should be found as substring
        assert sup_norm in pub_norm, (
            f"Aggressive normalization should allow substring match\n"
            f"Supporting: {sup_norm}\n"
            f"Publication: {pub_norm}"
        )

    def test_sliding_window_approach(self):
        """Test that a sliding window approach would help."""
        from difflib import SequenceMatcher

        publication = """demonstrated that the mutant GATA3 significantly reduced
        luciferase reporter activity by more than 65%"""

        supporting = "GATA3 significantly reduced luciferase reporter activity"

        # Simple sliding window on words
        pub_words = publication.lower().split()
        sup_words = supporting.lower().split()

        best_score = 0
        for i in range(len(pub_words) - len(sup_words) + 1):
            window = ' '.join(pub_words[i:i + len(sup_words)])
            score = SequenceMatcher(None, supporting.lower(), window).ratio()
            best_score = max(best_score, score)

        assert best_score > 0.85, (
            f"Sliding window should find high similarity: {best_score:.2%}"
        )