#!/usr/bin/env python3
"""Test to demonstrate the Greek letter validation bug in SupportingTextSubstringValidator.

This script shows that the validator's normalization works correctly in isolation,
but there's an issue when the full validation pipeline is run.
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from ai_gene_review.validation.supporting_text_validator import SupportingTextSubstringValidator
from ai_gene_review.validation.fuzzy_text_utils import find_fuzzy_match_in_text


def test_full_validation_pipeline():
    """Test the full validation pipeline with Greek letters."""

    validator = SupportingTextSubstringValidator()

    # The problematic text from CAMK2A
    supporting_text = "IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner (Fig. 2 A )"

    # Load the actual publication
    pmid = "11972023"
    pub_path = Path(f"publications/PMID_{pmid}.md")

    if not pub_path.exists():
        print(f"❌ Publication file not found: {pub_path}")
        return

    with open(pub_path, 'r') as f:
        publication_content = f.read()

    print("=" * 80)
    print("TESTING FULL VALIDATION PIPELINE")
    print("=" * 80)

    # Test 1: Direct normalization
    print("\n1. Direct Normalization Test:")
    print("-" * 40)
    norm_support = validator.normalize_whitespace(supporting_text)
    norm_pub = validator.normalize_whitespace(publication_content)

    print(f"Supporting text normalized: {norm_support[:100]}...")
    print(f"Is normalized supporting text in normalized publication? {norm_support in norm_pub}")

    # Test 2: The validate_substring_match method
    print("\n2. validate_substring_match Test:")
    print("-" * 40)
    is_valid, error_msg = validator.validate_substring_match(supporting_text, publication_content)
    print(f"Is valid: {is_valid}")
    print(f"Error message: {error_msg}")

    # Test 3: The find_text_in_publication method (used during validation)
    print("\n3. find_text_in_publication Test:")
    print("-" * 40)
    is_found, similarity, match_or_error = validator.find_text_in_publication(
        supporting_text, publication_content
    )
    print(f"Is found: {is_found}")
    print(f"Similarity: {similarity}")
    print(f"Match/Error: {match_or_error}")

    # Test 4: The fuzzy matching used for suggestions
    print("\n4. Fuzzy Matching (for suggestions) Test:")
    print("-" * 40)
    is_fuzzy, fuzzy_sim, fuzzy_match = find_fuzzy_match_in_text(
        supporting_text, publication_content, threshold=70.0
    )
    print(f"Fuzzy match found: {is_fuzzy}")
    print(f"Fuzzy similarity: {fuzzy_sim}")
    print(f"Fuzzy match text: {fuzzy_match}")

    # Test 5: Generate suggested fix
    print("\n5. Generate Suggested Fix Test:")
    print("-" * 40)
    suggested_fix = validator.generate_suggested_fix(
        supporting_text=supporting_text,
        reference_id=f"PMID:{pmid}",
        publication_content=publication_content,
        error_message=error_msg
    )
    print(f"Suggested fix: {suggested_fix}")

    # Test 6: The complete validation (as called during yaml validation)
    print("\n6. Complete Validation (validate_supporting_text_against_reference) Test:")
    print("-" * 40)
    result = validator.validate_supporting_text_against_reference(
        supporting_text=supporting_text,
        reference_id=f"PMID:{pmid}",
        annotation_path="test.path",
        yaml_data=None
    )

    if result:
        print(f"Is valid: {result.is_valid}")
        print(f"Error message: {result.error_message}")
        print(f"Suggested fix: {result.suggested_fix}")

    # Test 7: Try with spelled-out gamma
    print("\n7. Test with 'IFN-gamma' (spelled out):")
    print("-" * 40)
    spelled_out = supporting_text.replace("γ", "gamma")
    is_valid2, error_msg2 = validator.validate_substring_match(spelled_out, publication_content)
    print(f"Supporting text: {spelled_out[:50]}...")
    print(f"Is valid: {is_valid2}")
    print(f"Error message: {error_msg2}")

    # Test 8: Check what's actually in the publication at line 71
    print("\n8. Check Publication Content at Line 71:")
    print("-" * 40)
    lines = publication_content.split('\n')
    if len(lines) > 70:
        line71 = lines[70]  # 0-indexed
        print(f"Line 71: {line71}")
        print(f"Contains 'IFN-γ': {'IFN-γ' in line71}")
        print(f"Contains 'IFN-gamma': {'IFN-gamma' in line71}")

        # Check if our text is there
        if 'IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner (Fig. 2 A )' in line71:
            print("✓ Exact text found in line 71")
        else:
            print("✗ Exact text NOT found in line 71")

    print("\n" + "=" * 80)
    print("ANALYSIS:")
    print("=" * 80)

    if not is_valid and is_fuzzy:
        print("\n⚠️  BUG CONFIRMED: Validation fails but fuzzy matching succeeds!")
        print("This indicates that the normalizer is not being applied consistently.")
        print("\nThe issue is that:")
        print("1. Validation uses normalized text (γ → gamma)")
        print("2. But fuzzy suggestions use original text (keeping γ)")
        print("3. This creates misleading suggestions that won't actually work")


if __name__ == "__main__":
    test_full_validation_pipeline()