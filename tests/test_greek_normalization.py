#!/usr/bin/env python3
"""Unit tests for Greek letter normalization in supporting text validator.

This test module verifies that the Greek letter normalization is working
correctly in the supporting text validator, particularly for cases like
IFN-γ (IFN-gamma) which are common in biological literature.
"""

import pytest
from ai_gene_review.validation.supporting_text_validator import SupportingTextSubstringValidator


@pytest.fixture
def validator():
    """Create a validator instance for testing."""
    return SupportingTextSubstringValidator()


class TestGreekLetterNormalization:
    """Test Greek letter normalization in supporting text validation."""

    def test_basic_greek_normalization(self, validator):
        """Test that Greek letters are normalized to spelled-out equivalents."""
        # Test lowercase Greek letters
        assert validator.normalize_whitespace("α") == "alpha"
        assert validator.normalize_whitespace("β") == "beta"
        assert validator.normalize_whitespace("γ") == "gamma"
        assert validator.normalize_whitespace("δ") == "delta"
        assert validator.normalize_whitespace("θ") == "theta"

    def test_uppercase_greek_normalization(self, validator):
        """Test that uppercase Greek letters are also normalized."""
        # Uppercase Greek normalizes but then gets lowercased
        assert validator.normalize_whitespace("Α") == "alpha"  # Uppercase Alpha -> alpha (lowercase)
        assert validator.normalize_whitespace("Β") == "beta"   # Uppercase Beta -> beta
        assert validator.normalize_whitespace("Γ") == "gamma"  # Uppercase Gamma -> gamma
        assert validator.normalize_whitespace("Δ") == "delta"  # Uppercase Delta -> delta

    def test_ifn_gamma_normalization(self, validator):
        """Test the specific IFN-γ case that's causing validation issues."""
        # The actual case from CAMK2A
        assert validator.normalize_whitespace("IFN-γ") == "ifn-gamma"
        assert validator.normalize_whitespace("IFN-gamma") == "ifn-gamma"
        assert validator.normalize_whitespace("ifn-γ") == "ifn-gamma"

        # Test with various capitalizations
        assert validator.normalize_whitespace("IFN-Γ") == "ifn-gamma"  # Uppercase gamma
        assert validator.normalize_whitespace("ifn-GAMMA") == "ifn-gamma"

    def test_protein_names_with_greek(self, validator):
        """Test common protein names containing Greek letters."""
        assert validator.normalize_whitespace("TNFα") == "tnfalpha"
        assert validator.normalize_whitespace("TNF-α") == "tnf-alpha"
        assert validator.normalize_whitespace("IIα protein") == "iialpha protein"
        assert validator.normalize_whitespace("NF-κB") == "nf-kappab"
        assert validator.normalize_whitespace("TGF-β") == "tgf-beta"
        assert validator.normalize_whitespace("IL-1β") == "il-1beta"

    def test_complete_phrase_normalization(self, validator):
        """Test normalization of complete phrases with Greek letters."""
        # The exact phrase from CAMK2A file
        original = "IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner (Fig. 2 A )"
        expected = "ifn-gamma induced a rapid and sharp increase in [ca 2+ ] i in a dose-dependent manner (fig. 2 a )"
        assert validator.normalize_whitespace(original) == expected

        # Another example with multiple Greek letters
        text = "Both TNF-α and IL-1β activate NF-κB signaling"
        expected = "both tnf-alpha and il-1beta activate nf-kappab signaling"
        assert validator.normalize_whitespace(text) == expected

    def test_dash_normalization_with_greek(self, validator):
        """Test that various dashes are normalized along with Greek letters."""
        # Em-dash with Greek
        assert validator.normalize_whitespace("IFN—γ") == "ifn-gamma"
        # En-dash with Greek
        assert validator.normalize_whitespace("IFN–γ") == "ifn-gamma"
        # Minus sign with Greek
        assert validator.normalize_whitespace("IFN−γ") == "ifn-gamma"
        # Unicode hyphen with Greek
        assert validator.normalize_whitespace("IFN‐γ") == "ifn-gamma"

    def test_mixed_case_and_spacing(self, validator):
        """Test normalization handles mixed case and spacing correctly."""
        assert validator.normalize_whitespace("  IFN-γ  ") == "ifn-gamma"
        assert validator.normalize_whitespace("IFN - γ") == "ifn - gamma"
        assert validator.normalize_whitespace("IFN\tγ") == "ifn gamma"
        assert validator.normalize_whitespace("IFN\n\nγ") == "ifn gamma"

    @pytest.mark.parametrize("greek_char,expected", [
        ("α", "alpha"),
        ("β", "beta"),
        ("γ", "gamma"),
        ("δ", "delta"),
        ("ε", "epsilon"),
        ("ζ", "zeta"),
        ("η", "eta"),
        ("θ", "theta"),
        ("κ", "kappa"),
        ("λ", "lambda"),
        ("μ", "mu"),
        ("π", "pi"),
        ("σ", "sigma"),
        ("τ", "tau"),
        ("φ", "phi"),
        ("ω", "omega"),
    ])
    def test_all_common_greek_letters(self, validator, greek_char, expected):
        """Test all commonly used Greek letters in biological contexts."""
        assert validator.normalize_whitespace(f"protein-{greek_char}") == f"protein-{expected}"
        assert validator.normalize_whitespace(f"Protein-{greek_char}") == f"protein-{expected}"

    def test_substring_matching_with_normalization(self, validator):
        """Test that substring matching works correctly with normalized text."""
        source_text = "IFN-γ induced a rapid and sharp increase in intracellular calcium"
        query_text = "IFN-gamma induced a rapid and sharp increase"

        # Both should normalize to the same thing
        source_norm = validator.normalize_whitespace(source_text)
        query_norm = validator.normalize_whitespace(query_text)

        # The normalized query should be found in the normalized source
        assert query_norm in source_norm

    def test_real_world_examples(self, validator):
        """Test with real-world examples from gene annotation files."""
        # Example 1: From CAMK2A
        text1 = "IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i"
        text2 = "IFN-gamma induced a rapid and sharp increase in [Ca 2+ ] i"
        assert validator.normalize_whitespace(text1) == validator.normalize_whitespace(text2)

        # Example 2: Common receptor names
        text1 = "TNF-α receptor signaling"
        text2 = "TNF-alpha receptor signaling"
        assert validator.normalize_whitespace(text1) == validator.normalize_whitespace(text2)

        # Example 3: Transcription factors
        text1 = "NF-κB activation"
        text2 = "NF-kappaB activation"
        assert validator.normalize_whitespace(text1) == validator.normalize_whitespace(text2)


class TestValidationWithGreekLetters:
    """Test the full validation process with Greek letter normalization."""

    def test_validate_supporting_text_with_greek(self, validator):
        """Test that validation works correctly when Greek letters are involved."""
        # Source contains Greek letter
        source_text = "IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner"

        # Query uses spelled-out form
        supporting_text = "IFN-gamma induced a rapid and sharp increase in [Ca 2+ ] i"

        # This should validate successfully because of normalization
        is_valid, error_msg = validator.validate_substring_match(
            supporting_text=supporting_text,
            source_text=source_text
        )

        # Should pass validation
        assert is_valid is True

    def test_bidirectional_greek_matching(self, validator):
        """Test that matching works in both directions (Greek→Latin and Latin→Greek)."""
        # Source has spelled-out, query has Greek
        source_text = "TNF-alpha is a cytokine"
        supporting_text_with_greek = "TNF-α is a cytokine"
        is_valid, error_msg = validator.validate_substring_match(
            supporting_text=supporting_text_with_greek,
            source_text=source_text
        )
        assert is_valid is True

        # Source has Greek, query has spelled-out
        source_text_greek = "TNF-α is a cytokine"
        supporting_text_spelled = "TNF-alpha is a cytokine"
        is_valid, error_msg = validator.validate_substring_match(
            supporting_text=supporting_text_spelled,
            source_text=source_text_greek
        )
        assert is_valid is True


class TestChemicalIonNotation:
    """Test that chemical and ion notation is NOT treated as editorial."""

    def test_calcium_ion_notation(self, validator):
        """Test calcium ion notation with spaces."""
        assert validator.is_editorial_bracket("Ca 2+ ") == False
        assert validator.is_editorial_bracket("Ca 2+") == False
        assert validator.is_editorial_bracket("Ca2+") == False

    def test_common_ion_notation(self, validator):
        """Test common biological ions."""
        # Common cations
        assert validator.is_editorial_bracket("Mg 2+ ") == False
        assert validator.is_editorial_bracket("Fe 3+ ") == False
        assert validator.is_editorial_bracket("Na+") == False
        assert validator.is_editorial_bracket("K+") == False
        assert validator.is_editorial_bracket("H+") == False

        # Common anions
        assert validator.is_editorial_bracket("Cl-") == False
        assert validator.is_editorial_bracket("OH-") == False

    def test_complex_ions(self, validator):
        """Test complex polyatomic ions."""
        assert validator.is_editorial_bracket("NH4+") == False
        assert validator.is_editorial_bracket("SO4 2-") == False
        assert validator.is_editorial_bracket("PO4 3-") == False
        assert validator.is_editorial_bracket("CO3 2-") == False

    def test_editorial_content_still_detected(self, validator):
        """Ensure editorial content is still correctly identified."""
        assert validator.is_editorial_bracket("The protein") == True
        assert validator.is_editorial_bracket("important") == True
        assert validator.is_editorial_bracket("according to studies") == True
        assert validator.is_editorial_bracket("cytoplasmic") == True

    def test_calcium_in_full_text(self, validator):
        """Test that [Ca 2+ ] is preserved in full supporting text."""
        text = "IFN-γ induced a rapid increase in [Ca 2+ ] i"
        query_spans, ignored_spans = validator.parse_bracketed_text(text)

        # [Ca 2+ ] should NOT be in ignored_spans
        assert "[Ca 2+ ]" not in ignored_spans

        # The full text should be preserved in query spans
        assert any("[Ca 2+ ]" in span or "ca 2+" in span.lower() for span in query_spans)

    def test_validate_calcium_text(self, validator):
        """Test full validation with calcium ion notation."""
        source = "IFN-gamma induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner"
        query = "IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner"

        is_valid, error_msg = validator.validate_substring_match(query, source)

        # Should be valid after the fix
        assert is_valid == True, f"Validation failed: {error_msg}"


class TestUnicodeQuoteNormalization:
    """Test that Unicode curly quotes are normalized to ASCII quotes."""

    @pytest.fixture
    def validator(self):
        return SupportingTextSubstringValidator()

    def test_double_curly_quote_normalization(self, validator):
        """Test that Unicode curly double quotes are normalized to ASCII."""
        # \u201c = " (left double quote)
        # \u201d = " (right double quote)
        text_with_curly = 'The protein is \u201cshuttled\u201d by His37'

        normalized = validator.normalize_whitespace(text_with_curly)

        # Should have ASCII quotes after normalization
        assert '"' in normalized
        assert '\u201c' not in normalized
        assert '\u201d' not in normalized

    def test_single_curly_quote_normalization(self, validator):
        """Test that Unicode curly single quotes are normalized to ASCII."""
        # \u2018 = ' (left single quote)
        # \u2019 = ' (right single quote)
        text_with_curly = "The gene\u2019s function is important"

        normalized = validator.normalize_whitespace(text_with_curly)

        # Should have ASCII apostrophe after normalization
        assert "'" in normalized
        assert '\u2018' not in normalized
        assert '\u2019' not in normalized

    def test_mixed_quote_normalization(self, validator):
        """Test normalization of mixed quote types."""
        # Mix of different Unicode quotes using escape sequences
        text = "He said \u201cit\u2019s a \u2018complex\u2019 mechanism\u201d"

        normalized = validator.normalize_whitespace(text)

        # All should be normalized to ASCII
        assert '\u201c' not in normalized
        assert '\u201d' not in normalized
        assert '\u2018' not in normalized
        assert '\u2019' not in normalized

    def test_m2_shuttled_text_validation(self, validator):
        """Test the actual M2 shuttled text case with curly quotes."""
        # Publication has Unicode curly quotes (using escape sequences)
        pub_text = 'protons diffuse along a water wire until reaching His37, where they are then \u201cshuttled\u201d by His37'

        # YAML has ASCII straight quotes
        yaml_text = 'protons diffuse along a water wire until reaching His37, where they are then "shuttled" by His37'

        is_valid, error_msg = validator.validate_substring_match(yaml_text, pub_text)

        # Should be valid after quote normalization
        assert is_valid == True, f"Validation failed: {error_msg}"

    def test_low_9_quotation_marks(self, validator):
        """Test normalization of low-9 quotation marks (used in some languages)."""
        # \u201a = ‚ (single low-9 quotation mark)
        # \u201e = „ (double low-9 quotation mark)
        text_with_low9 = '\u201asingle\u201b and \u201edouble\u201d quotes'

        normalized = validator.normalize_whitespace(text_with_low9)

        # Should be normalized to ASCII
        assert '\u201a' not in normalized
        assert '\u201e' not in normalized

    def test_full_m2_text_with_quotes(self, validator):
        """Test the full M2 text that had the quote issue."""
        # Full text with Unicode curly quotes (as in publication)
        pub_text = 'An early model envisioned a continuous aqueous channel that was gated by pH (shutter mechanism), 20 versus the currently accepted model in which protons diffuse along a water wire until reaching His37, where they are then \u201cshuttled\u201d by His37 through alternate protonation and deprotonation events'

        # Same text with ASCII quotes (as in YAML)
        yaml_text = 'An early model envisioned a continuous aqueous channel that was gated by pH (shutter mechanism), 20 versus the currently accepted model in which protons diffuse along a water wire until reaching His37, where they are then "shuttled" by His37 through alternate protonation and deprotonation events'

        is_valid, error_msg = validator.validate_substring_match(yaml_text, pub_text)

        # Should be valid after normalization
        assert is_valid == True, f"Validation failed: {error_msg}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])