# Implementation Plan: Suggested Fixes for Supporting Text Validation

## Overview
Add actionable fix suggestions to the substring validator TSV output to help users quickly fix validation errors.

## Current State
- TSV output has `suggestion` column (already exists!)
- `SupportingTextValidationResult` has `suggested_fix` field (already exists!)
- `validator.py` line 1006 already passes `suggestion=st_result.suggested_fix` to issues
- **Problem**: `suggested_fix` is never populated in `supporting_text_validator.py`

## Changes Needed

### File: `src/ai_gene_review/validation/supporting_text_validator.py`

#### 1. Add helper method to generate suggested fixes

```python
def generate_suggested_fix(
    self,
    supporting_text: str,
    reference_id: str,
    best_match: Optional[str],
    similarity: float,
    publication_content: str
) -> Optional[str]:
    """Generate actionable fix suggestion based on validation failure.

    Args:
        supporting_text: The text that failed validation
        reference_id: PMID/Reactome/UniProt ID
        best_match: Best matching text from source (if any)
        similarity: Similarity score
        publication_content: Full publication text

    Returns:
        Suggested fix string or None
    """
    suggestions = []

    # Add reference context
    suggestions.append(f"Source: {reference_id}")

    # Check for ellipsis (non-contiguous text)
    if "..." in supporting_text:
        # Extract first part before ellipsis
        first_part = supporting_text.split("...")[0].strip()
        if len(first_part) >= 20:
            suggestions.append(f"Remove '...' and use contiguous text: \"{first_part}\"")

    # Check if text is too short
    non_bracket_text = re.sub(r'\[.*?\]', '', supporting_text).strip()
    if len(non_bracket_text) < 20:
        if len(non_bracket_text) == 0:
            suggestions.append("All bracketed content - use publication title or abstract excerpt instead")
        else:
            suggestions.append(f"Text too short ({len(non_bracket_text)} chars) - extend with surrounding context from source")

    # Check for capitalization issues
    if best_match and similarity > 0.85:
        # Case-insensitive match found - likely capitalization issue
        if supporting_text.lower() == best_match.lower():
            suggestions.append(f"Capitalization issue - use: \"{best_match}\"")
        else:
            suggestions.append(f"Close match found (similarity {similarity:.0%}) - try: \"{best_match[:100]}...\"")
    elif best_match and similarity > 0.5:
        suggestions.append(f"Partial match found (similarity {similarity:.0%})")
        # Show first 150 chars of best match
        preview = best_match[:150] + "..." if len(best_match) > 150 else best_match
        suggestions.append(f"Consider: \"{preview}\"")

    return " | ".join(suggestions) if suggestions else None
```

#### 2. Update validation methods to populate suggested_fix

In the PMID validation section (around line 770-787), after line 787, add:

```python
if not is_found:
    # ... existing error message code ...

    # Generate suggested fix
    result.suggested_fix = self.generate_suggested_fix(
        supporting_text=supporting_text,
        reference_id=reference_id,
        best_match=best_match,
        similarity=similarity,
        publication_content=publication_content
    )
```

Similarly for UniProt validation (around line 822-837) and Reactome validation.

#### 3. Include reference_id in error messages

Update error messages to include reference context:

```python
result.error_message = f"[{reference_id}] {text_preview} not found in source"
```

## Expected Output

After implementation, `reports/validation-all.tsv` will have populated suggestion column:

```
file_path	severity	validation_category	check_type	path	message	suggestion	details	timestamp
genes/METAC/mcrA/mcrA-ai-review.yaml	warning	SupportingTextSubstringValidator	supporting_text_substring_not_found	existing_annotations[4].review.supported_by[0].supporting_text	"[PMID:29743535] identification of a unique radical sam methyltrans..." not found in source	Source: PMID:29743535 | Capitalization issue - use: "Identification of a unique radical SAM methyltransferase required for the sp3-C-methylation..."		2025-11-19T08:58:13.908383
```

## Testing

1. Run validation on known error files:
   ```bash
   just validate-all
   grep "substring_not_found" reports/validation-all.tsv | cut -f7 | head -10
   ```

2. Verify suggestions appear and are actionable

3. Test different error types:
   - Capitalization (mcrA, lexA)
   - Ellipsis (SAMD8)
   - Too short (Q88CC1, MBR_10393)
   - All brackets (ARCN1)

## Benefits

1. **Faster fixes**: Users see exact fix without manual searching
2. **Better DX**: Actionable errors vs cryptic failures
3. **Scalable**: Works for all 197 remaining errors
4. **Extensible**: Easy to add more suggestion types

## Implementation Time

- Core changes: ~30 minutes
- Testing: ~15 minutes
- Total: ~45 minutes

## Follow-up Enhancements

1. Add `--auto-fix` flag to apply suggestions automatically
2. Interactive mode: show suggestion and prompt "Apply? [y/n]"
3. Confidence scores for suggestions
4. Learn from user corrections
