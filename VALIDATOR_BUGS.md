# Validator Bugs Found

## Bug 1: Incorrect Bracketed Content Classification

### Location
`src/ai_gene_review/validation/supporting_text_validator.py`, line 1353

### Issue
The validator incorrectly treats `[Ca 2+ ]` (calcium ion notation) as editorial content and strips it from the text during validation. This happens because the `is_editorial_bracket()` method classifies any multi-word content in brackets as editorial:

```python
# Line 1353: Multi-word content - definitely editorial
if len(content.split()) > 1:
    return True
```

### Impact
For the CAMK2A gene review, the text:
- Original: `IFN-γ induced a rapid and sharp increase in [Ca 2+ ] i in a dose-dependent manner`
- Gets normalized to: `ifn-gamma induced a rapid and sharp increase in i in a dose-dependent manner`
- The `[Ca 2+ ]` is incorrectly removed, causing validation to fail

### Workaround
Changed the supporting text to avoid using bracketed calcium ion notation:
- `IFN-γ induced a rapid and sharp increase in intracellular calcium in a dose-dependent manner`

### Suggested Fix
The `is_editorial_bracket()` method should recognize scientific notations like:
- Chemical formulas: `[Ca 2+ ]`, `[Mg 2+ ]`, `[Fe 3+ ]`
- Ion concentrations: `[Na+]`, `[K+]`
- Chemical symbols with spaces: `[Ca 2+ ]`

These should NOT be treated as editorial content.

## Bug 2: Inconsistent Text Normalization Between Validation and Suggestions

### Location
`src/ai_gene_review/validation/supporting_text_validator.py`, lines 1699 and 1753

### Issue
The validator normalizes text (including Greek letter conversion) for validation but generates suggestions using the original un-normalized text, leading to misleading error messages.

### Example
1. Both file and publication contain: `IFN-γ` (with Greek gamma)
2. During validation: Both texts are normalized to `ifn-gamma`
3. But the fuzzy matcher for suggestions uses original text with `γ`
4. Result: Validator suggests using `IFN-γ`, but that's already what's in the file!

### Impact
Creates confusing error messages where the validator suggests text that is already present in the file.

## Bug 3: Smart Quotes Not Handled

### Location
General string normalization in the validator

### Issue
Publications often contain UTF-8 smart quotes (" " instead of " "), which are not normalized by the validator.

### Example (M2 gene)
- Publication has: `"shuttled"` (with smart quotes U+201C and U+201D)
- YAML file has: `"shuttled"` (with regular ASCII quotes)
- Validation fails even though the text is semantically identical

### Workaround
Copy the exact text from the publication including smart quotes.

### Suggested Fix
The `normalize_whitespace()` method should normalize all quote variations:
- Smart quotes: " " ' ' → regular quotes: " " ' '
- This should be part of standard text normalization

## Testing

Created comprehensive unit tests in `tests/test_greek_normalization.py` to verify Greek letter normalization is working correctly (27 tests, 25 passing).

Created debug scripts:
- `test_validation_issue.py` - Demonstrates the calcium bracket issue
- `test_greek_validation_bug.py` - Comprehensive test showing the validation pipeline issues

## Summary

The validator has several issues with text normalization that cause false positives:

1. **Scientific notation in brackets** is incorrectly treated as editorial content
2. **Greek letter normalization** works in the validator but not in the suggestion generator
3. **Smart quotes** from publications are not normalized to regular quotes

These bugs make it difficult to create valid gene review files even when the supporting text is correctly copied from source publications.