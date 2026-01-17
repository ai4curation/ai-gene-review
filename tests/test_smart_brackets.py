"""Test for smart bracket detection to prevent false positives with scientific notation."""

import pytest
from ai_gene_review.validation.supporting_text_validator import SupportingTextSubstringValidator


class TestSmartBracketDetection:
    """Test smart detection of editorial vs scientific brackets."""

    @pytest.fixture
    def validator(self):
        return SupportingTextSubstringValidator()

    @pytest.mark.parametrize("content,expected", [
        # Scientific notation - should NOT be editorial
        ("+21", False),
        ("14", False),
        ("-3", False),
        ("A", False),
        ("G19", False),
        ("U+21", False),
        ("Cas7.5", False),
        # Editorial - should be editorial
        ("important", True),
        ("The protein", True),
        ("according to studies", True),
        ("...", True),
        ("unclear mechanism ...", True),
        ("cytoplasmic", True),
        ("directly", True),
    ])
    def test_is_editorial_bracket(self, validator, content, expected):
        """Test editorial bracket detection."""
        assert validator.is_editorial_bracket(content) == expected

    def test_scientific_notation_preserved(self, validator):
        """Test that scientific notation brackets are preserved."""
        supporting_text = "nucleotides (U[+21], U[+22], G[+23]) of crRNA"
        source_text = "nucleotides (U[+21], U[+22], G[+23]) of crRNA is important"
        
        is_valid, error = validator.validate_substring_match(supporting_text, source_text)
        assert is_valid, f"Should be valid but got error: {error}"

    def test_editorial_brackets_removed(self, validator):
        """Test that editorial brackets are removed."""
        supporting_text = "The [important] protein functions in cytoplasm"
        source_text = "The protein functions in cytoplasm normally"
        
        is_valid, error = validator.validate_substring_match(supporting_text, source_text)
        assert is_valid, f"Should be valid but got error: {error}"

    def test_mixed_brackets(self, validator):
        """Test mixed editorial and scientific brackets."""
        supporting_text = "The [important] protein at position G[14] binds target"
        source_text = "The protein at position G[14] binds target molecule"
        
        is_valid, error = validator.validate_substring_match(supporting_text, source_text)
        assert is_valid, f"Should be valid but got error: {error}"

    def test_explicit_editorial_with_ellipsis(self, validator):
        """Test that [...] is treated as editorial."""
        supporting_text = "protein [unclear mechanism ...] binds [directly] to target molecule"
        
        # This should work - editorial removed
        norm = validator.normalize_whitespace(supporting_text)
        query_spans, ignored = validator.parse_bracketed_text(norm)
        
        assert len(ignored) == 2
        assert "[unclear mechanism ...]" in " ".join(ignored)
        assert "[directly]" in " ".join(ignored)

    def test_acrf8_real_world_case(self, validator):
        """Test the real AcrF8 case that was a false positive."""
        supporting_text = (
            "The distance between the residues T29, I31, A32, N33 of AcrF8 "
            "and the nucleobases of three nucleotides (U[+21], U[+22], G[+23]) "
            "of crRNA is less than 4 Å, which is close enough to form multiple "
            "hydrogen bonds and nonbonded interactions"
        )
        source_text = (
            "The distance between the residues T29, I31, A32, N33 of AcrF8 "
            "and the nucleobases of three nucleotides (U[+21], U[+22], G[+23]) "
            "of crRNA is less than 4 Å, which is close enough to form multiple "
            "hydrogen bonds and nonbonded interactions (Fig. 3 B and C)."
        )
        
        is_valid, error = validator.validate_substring_match(supporting_text, source_text)
        assert is_valid, f"AcrF8 case should be valid but got error: {error}"

    def test_unicode_dash_normalization(self, validator):
        """Test that various unicode dashes are normalized to standard hyphen."""
        # Test with different dash types between supporting text and source
        test_cases = [
            # (supporting_text_dash, source_text_dash, description)
            ('-', '–', 'hyphen vs en-dash'),
            ('-', '—', 'hyphen vs em-dash'),
            ('-', '−', 'hyphen vs minus'),
            ('–', '-', 'en-dash vs hyphen'),
            ('—', '–', 'em-dash vs en-dash'),
        ]
        
        for support_dash, source_dash, desc in test_cases:
            supporting_text = f"protein acrIF8{support_dash}aca2 operon is regulated"
            source_text = f"protein acrIF8{source_dash}aca2 operon is regulated in cells"
            
            is_valid, error = validator.validate_substring_match(supporting_text, source_text)
            assert is_valid, f"Unicode dash normalization failed for {desc}: {error}"

    def test_aca2_real_world_dash_issue(self, validator):
        """Test the real ACA2 case with hyphen vs en-dash."""
        # Supporting text with hyphen (what was incorrectly in YAML)
        supporting_text = (
            "Aca2 is a dimer that represses the expression of the acrIF8-aca2 "
            "operon, and that this autoregulation is mediated through binding to "
            "inverted repeats in the promoter region"
        )
        # Source with en-dash (what's in the publication)
        source_text = (
            "Here, we show that Aca2 is a dimer that represses the expression of "
            "the acrIF8–aca2 operon, and that this autoregulation is mediated through "
            "binding to inverted repeats in the promoter region."
        )
        
        is_valid, error = validator.validate_substring_match(supporting_text, source_text)
        assert is_valid, f"ACA2 dash normalization should work but got: {error}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
