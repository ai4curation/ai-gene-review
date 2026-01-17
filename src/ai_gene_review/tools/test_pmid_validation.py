#!/usr/bin/env python3
"""Test script for PMID validation functionality."""
from pathlib import Path
import sys
sys.path.insert(0, 'src')

from ai_gene_review.tools.validate_pmid_references import extract_pmids_from_markdown

def test_pmid_extraction():
    """Test that PMID extraction correctly identifies valid and invalid PMIDs."""
    
    test_cases = [
        # (markdown_content, expected_valid, expected_invalid)
        (
            "This references [PMID:12345] and [PMID:67890]",
            {"PMID:12345", "PMID:67890"},
            set()
        ),
        (
            "This has invalid [PMID:xxx12345] and valid [PMID:67890]",
            {"PMID:67890"},
            {"PMID:xxx12345"}
        ),
        (
            "Mixed: [PMID:12345, PMID:xx8232552, PMID:9590172]",
            {"PMID:12345", "PMID:9590172"},
            {"PMID:xx8232552"}
        ),
        (
            "Without brackets: PMID:12345 and PMID:abc123",
            {"PMID:12345"},
            {"PMID:abc123"}
        ),
        (
            "Complex: [PMID:12345, \"some text\"], PMID:67890.",
            {"PMID:12345", "PMID:67890"},
            set()
        ),
        (
            "All invalid: [PMID:xxx123, PMID:abc456]",
            set(),
            {"PMID:xxx123", "PMID:abc456"}
        ),
    ]
    
    print("Testing PMID extraction...")
    all_passed = True
    
    for i, (content, expected_valid, expected_invalid) in enumerate(test_cases, 1):
        valid, invalid = extract_pmids_from_markdown(content)
        
        if valid == expected_valid and invalid == expected_invalid:
            print(f"  ✅ Test {i}: PASSED")
        else:
            print(f"  ❌ Test {i}: FAILED")
            print(f"     Content: {content[:50]}...")
            print(f"     Expected valid: {expected_valid}")
            print(f"     Got valid: {valid}")
            print(f"     Expected invalid: {expected_invalid}")
            print(f"     Got invalid: {invalid}")
            all_passed = False
    
    return all_passed

def test_jak1_pathway():
    """Test the actual JAK1 pathway file."""
    jak1_path = Path("genes/human/JAK1/JAK1-pathway.md")
    
    if not jak1_path.exists():
        print(f"❌ JAK1 pathway file not found: {jak1_path}")
        return False
    
    content = jak1_path.read_text()
    valid, invalid = extract_pmids_from_markdown(content)
    
    print(f"\nTesting {jak1_path}:")
    print(f"  Found {len(valid)} valid PMIDs")
    print(f"  Found {len(invalid)} invalid PMIDs")
    
    if invalid:
        print("  ❌ Invalid PMIDs detected:")
        for pmid in sorted(invalid):
            # Find line number
            lines = content.split('\n')
            for line_num, line in enumerate(lines, 1):
                if pmid in line:
                    print(f"    - {pmid} at line {line_num}")
                    break
        return False
    else:
        print("  ✅ All PMIDs are valid")
        return True

def main():
    """Run all tests."""
    print("="*60)
    print("PMID Validation Test Suite")
    print("="*60)
    
    # Run extraction tests
    extraction_passed = test_pmid_extraction()
    
    # Run JAK1 pathway test
    jak1_passed = test_jak1_pathway()
    
    print("\n" + "="*60)
    if extraction_passed and jak1_passed:
        print("✅ ALL TESTS PASSED")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()