#!/usr/bin/env python3
"""Debug script to understand why CAMK2A validation is failing."""

import os
from ai_gene_review.validation.supporting_text_validator import SupportingTextSubstringValidator

# Initialize validator
validator = SupportingTextSubstringValidator()

# The text from both CAMK2A and the publication
text_in_file = "IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner (Fig. 2 A )"
text_in_publication = "IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner (Fig. 2 A )"

print("Original texts:")
print(f"  File:        {text_in_file}")
print(f"  Publication: {text_in_publication}")
print()

# Test normalization
normalized_file = validator.normalize_whitespace(text_in_file)
normalized_pub = validator.normalize_whitespace(text_in_publication)

print("Normalized texts:")
print(f"  File:        {normalized_file}")
print(f"  Publication: {normalized_pub}")
print(f"  Match:       {normalized_file == normalized_pub}")
print()

# Check substring match
if normalized_file in normalized_pub:
    print("✓ Normalized file text IS found in normalized publication text")
else:
    print("✗ Normalized file text NOT found in normalized publication text")
print()

# Now let's check what the validator actually sees from the publication
pmid = "PMID:11972023"
pub_path = f"publications/{pmid.replace(':', '_')}.md"

if os.path.exists(pub_path):
    print(f"Loading publication from: {pub_path}")
    with open(pub_path, 'r') as f:
        content = f.read()

    # Check if the exact text is in the publication
    if text_in_publication in content:
        print("✓ Exact text found in publication file")
    else:
        print("✗ Exact text NOT found in publication file")

    # Check if normalized text would match
    content_norm = validator.normalize_whitespace(content)
    if normalized_file in content_norm:
        print("✓ Normalized text would be found in normalized publication")
    else:
        print("✗ Normalized text NOT found in normalized publication")

    # Let's check for a simpler substring
    simple_test = "ifn-gamma induced a rapid"
    if simple_test in content_norm:
        print(f"✓ Simple test '{simple_test}' found")
    else:
        print(f"✗ Simple test '{simple_test}' NOT found")

    # Check what the validator truncates to
    truncated = text_in_file[:50] + "..."
    print(f"\nValidator would show as: '{truncated}'")

    # Let's see what the validator normalizes for the truncated version
    truncated_norm = validator.normalize_whitespace(text_in_file[:50])
    print(f"Truncated normalized: '{truncated_norm}...'")
else:
    print(f"Publication file not found at: {pub_path}")