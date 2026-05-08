#!/usr/bin/env python3
"""Proposed fix for the [Ca 2+ ] issue.

Add chemical/ion notation detection to is_editorial_bracket() method.
This should be inserted BEFORE the multi-word check (before line 1353).
"""

import re

def is_chemical_or_ion_notation(content: str) -> bool:
    """Detect if bracketed content is chemical/ion notation.

    Common patterns in biology literature:
    - Ion charges: [Ca 2+ ], [Mg 2+ ], [Fe 3+ ]
    - Simple ions: [Na+], [K+], [Cl-], [H+], [OH-]
    - Ion concentrations: [Ca2+], [Mg2+]

    Returns:
        True if content appears to be chemical/ion notation

    Examples:
        >>> is_chemical_or_ion_notation("Ca 2+ ")
        True
        >>> is_chemical_or_ion_notation("Ca2+")
        True
        >>> is_chemical_or_ion_notation("Mg 2+ ")
        True
        >>> is_chemical_or_ion_notation("Na+")
        True
        >>> is_chemical_or_ion_notation("OH-")
        True
        >>> is_chemical_or_ion_notation("Fe 3+ ")
        True
        >>> is_chemical_or_ion_notation("The protein")
        False
        >>> is_chemical_or_ion_notation("important")
        False
    """
    content = content.strip()

    # Pattern 1: Element symbol followed by optional spaces, digits, and +/- charge
    # Examples: Ca 2+, Mg2+, Fe 3+, Na+, K+, Cl-
    # Chemical element symbols: 1-2 letters, first uppercase
    if re.match(r'^[A-Z][a-z]?\s*\d*\s*[+-]+\s*$', content):
        return True

    # Pattern 2: Simple chemical formulas with charges
    # Examples: OH-, H+, H2O, CO2
    if re.match(r'^[A-Z][a-z]?\d*[+-]?\s*$', content):
        return True

    # Pattern 3: More complex ions like NH4+, SO4 2-
    if re.match(r'^[A-Z][a-z]?\d*[A-Z]?\d*\s*\d*\s*[+-]+\s*$', content):
        return True

    return False


def test_cases():
    """Test the function with various inputs."""
    test_data = [
        # Should return True (chemical/ion notation)
        ("Ca 2+ ", True),
        ("Ca2+", True),
        ("Mg 2+ ", True),
        ("Mg2+", True),
        ("Fe 3+ ", True),
        ("Fe3+", True),
        ("Na+", True),
        ("K+", True),
        ("Cl-", True),
        ("H+", True),
        ("OH-", True),
        ("NH4+", True),
        ("SO4 2-", True),
        ("PO4 3-", True),

        # Should return False (editorial or other content)
        ("The protein", False),
        ("important", False),
        ("according to studies", False),
        ("cytoplasmic", False),
        ("Fig. 2 A", False),
        ("see text", False),
        ("A", False),  # Single letter - handled by existing logic
        ("14", False),  # Number - handled by existing logic
        ("G19", False),  # Gene coordinate - handled by existing logic
    ]

    print("Testing chemical/ion notation detection:")
    print("=" * 60)

    for content, expected in test_data:
        result = is_chemical_or_ion_notation(content)
        status = "✓" if result == expected else "✗"
        print(f"{status} [{content:20s}] -> {result:5} (expected {expected})")

    print("\n" + "=" * 60)
    passed = sum(1 for content, expected in test_data if is_chemical_or_ion_notation(content) == expected)
    total = len(test_data)
    print(f"Passed: {passed}/{total}")


if __name__ == "__main__":
    test_cases()
