# Proposed Fix for [Ca 2+ ] Issue

## Problem
The validator incorrectly treats `[Ca 2+ ]` (calcium ion notation) as editorial content because it contains spaces. This causes the text to be stripped during validation, resulting in false positive errors.

## Solution
Add chemical/ion notation detection to the `is_editorial_bracket()` method in `src/ai_gene_review/validation/supporting_text_validator.py`.

## Implementation

### Location
Insert the new check at **line 1352**, right **before** the multi-word check.

### Code to Insert

```python
# Chemical/ion notation: [Ca 2+ ], [Mg2+], [Na+], [OH-]
# Pattern matches: Element symbol (1-2 letters) + optional spaces/digits + charge
if re.match(r'^[A-Z][a-z]?\s*\d*\s*[+-]+\s*$', content):
    return False  # Not editorial - it's chemical notation

# Complex ions: [NH4+], [SO4 2-], [PO4 3-]
if re.match(r'^[A-Z][a-z]?\d*[A-Z]?\d*\s*\d*\s*[+-]+\s*$', content):
    return False  # Not editorial - it's ion notation
```

### Updated Method Structure

```python
def is_editorial_bracket(self, content: str) -> bool:
    content = content.strip()

    # Empty - not editorial
    if not content:
        return False

    # Explicit editorial marker: contains "..."
    if "..." in content:
        return True

    # Very short content (1-2 chars) - likely scientific
    if len(content) <= 2:
        return False

    # Pure numbers: [14], [123], [-3]
    if re.match(r'^[+-]?\d+$', content):
        return False

    # Single uppercase letter: [A], [B], [C]
    if re.match(r'^[A-Z]$', content):
        return False

    # Position notation: [+21], [-3]
    if re.match(r'^[+-]\d+$', content):
        return False

    # Scientific notation: [G14], [U21], [U+21]
    if re.match(r'^[A-Za-z][+-]?\d+$', content):
        return False

    # Decimal notation: [Cas7.4], [7.5]
    if re.match(r'^[A-Za-z0-9]+\.[\d]+$', content):
        return False

    ### NEW CODE INSERTED HERE (before line 1353) ###
    # Chemical/ion notation: [Ca 2+ ], [Mg2+], [Na+], [OH-]
    if re.match(r'^[A-Z][a-z]?\s*\d*\s*[+-]+\s*$', content):
        return False

    # Complex ions: [NH4+], [SO4 2-], [PO4 3-]
    if re.match(r'^[A-Z][a-z]?\d*[A-Z]?\d*\s*\d*\s*[+-]+\s*$', content):
        return False
    ### END NEW CODE ###

    # Multi-word content - definitely editorial (existing line 1353)
    if len(content.split()) > 1:
        return True

    # Single word longer than 3 characters - likely editorial
    if len(content) > 3 and re.match(r'^[A-Z a-z]+$', content):
        return True

    # Default: conservative - treat as scientific
    return False
```

## Test Coverage

Add tests to verify the fix:

```python
def test_chemical_ion_notation(self, validator):
    """Test that chemical and ion notation is NOT treated as editorial."""
    # Common ion notations
    assert validator.is_editorial_bracket("Ca 2+ ") == False
    assert validator.is_editorial_bracket("Ca2+") == False
    assert validator.is_editorial_bracket("Mg 2+ ") == False
    assert validator.is_editorial_bracket("Fe 3+ ") == False
    assert validator.is_editorial_bracket("Na+") == False
    assert validator.is_editorial_bracket("K+") == False
    assert validator.is_editorial_bracket("Cl-") == False
    assert validator.is_editorial_bracket("H+") == False
    assert validator.is_editorial_bracket("OH-") == False

    # Complex ions
    assert validator.is_editorial_bracket("NH4+") == False
    assert validator.is_editorial_bracket("SO4 2-") == False
    assert validator.is_editorial_bracket("PO4 3-") == False

    # Still recognize editorial content
    assert validator.is_editorial_bracket("The protein") == True
    assert validator.is_editorial_bracket("important") == True
```

## Example Use Case

### Before Fix
Supporting text: `IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i`
- Normalized to: `ifn-gamma induced a rapid and sharp increase in i`
- `[Ca 2+ ]` is stripped → validation fails ❌

### After Fix
Supporting text: `IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i`
- Normalized to: `ifn-gamma induced a rapid and sharp increase in [ca 2+ ] i`
- `[Ca 2+ ]` is preserved → validation succeeds ✓

## Benefits

1. **No escape characters needed** - keeps YAML clean and readable
2. **Handles common biology notation** - Ca²⁺, Mg²⁺, Na⁺, K⁺, etc.
3. **Backwards compatible** - doesn't break existing validation
4. **Future-proof** - covers complex ions like NH₄⁺, SO₄²⁻
5. **Conservative** - still correctly identifies editorial content

## Alternative: Escape Character Approach

If you prefer escape characters instead:

```yaml
# Option 1: Backslash escape (like Markdown)
supporting_text: "IFN-γ induced a rapid increase in \[Ca 2+ \] i"

# Option 2: Double brackets (like wiki syntax)
supporting_text: "IFN-γ induced a rapid increase in [[Ca 2+ ]] i"
```

**Cons:**
- Harder to remember and document
- Makes YAML less readable
- Requires updating all existing files
- More complex parsing logic

**Recommendation:** Go with the pattern recognition approach - it's cleaner and more intuitive.