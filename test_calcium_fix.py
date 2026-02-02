#!/usr/bin/env python3
"""Test that the calcium fix is working."""

from src.ai_gene_review.validation.supporting_text_validator import SupportingTextSubstringValidator

validator = SupportingTextSubstringValidator()

# Test 1: Check that [Ca 2+ ] is NOT treated as editorial
print("Test 1: is_editorial_bracket('Ca 2+ '):", validator.is_editorial_bracket("Ca 2+ "))
assert not validator.is_editorial_bracket("Ca 2+ "), "Ca 2+ should not be editorial"
print("✓ Pass\n")

# Test 2: Check that it's preserved in parse_bracketed_text
print("Test 2: parse_bracketed_text with [Ca 2+ ]")
text = "increase in [Ca 2+ ] i"
query_spans, ignored_spans = validator.parse_bracketed_text(text)
print(f"  Query spans: {query_spans}")
print(f"  Ignored spans: {ignored_spans}")
assert "[Ca 2+ ]" not in ignored_spans, "[Ca 2+ ] should not be ignored"
print("✓ Pass\n")

# Test 3: Check normalization
print("Test 3: normalize_whitespace")
text = "IFN-γ induced a rapid increase in [Ca 2+ ] i"
normalized = validator.normalize_whitespace(text)
print(f"  Original: {text}")
print(f"  Normalized: {normalized}")
assert "ca 2+" in normalized, "Ca 2+ should be in normalized text"
print("✓ Pass\n")

# Test 4: Full validation with just calcium (no Greek)
print("Test 4: validate_substring_match with calcium")
source = "increase in [Ca 2+ ] i in a dose"
query = "increase in [Ca 2+ ] i in a dose"
is_valid, error_msg = validator.validate_substring_match(query, source)
print(f"  Source: {source}")
print(f"  Query: {query}")
print(f"  Valid: {is_valid}")
if not is_valid:
    print(f"  Error: {error_msg}")
print()

# Test 5: Full validation with both Greek and calcium
print("Test 5: validate_substring_match with Greek AND calcium")
source = "IFN-γ induced a rapid increase in [Ca 2+ ] i"
query = "IFN-γ induced a rapid increase in [Ca 2+ ] i"
is_valid, error_msg = validator.validate_substring_match(query, source)
print(f"  Source: {source}")
print(f"  Query: {query}")
print(f"  Valid: {is_valid}")
if not is_valid:
    print(f"  Error: {error_msg}")
else:
    print("✓ Pass")
