# pymodulon Compatibility Issue

## Problem

Attempted to use `pymodulon` package for E. coli data access, but encountered pandas compatibility issue:

```python
from pymodulon.example_data import load_ecoli_data
ica_data = load_ecoli_data()

# Error:
# ValueError: invalid literal for int() with base 10: 'AllR/AraC/FucR'
```

## Root Cause

The pymodulon package (v0.2.1) has a pandas version compatibility issue:
- Tries to convert iModulon column names to integers
- Some columns contain strings like 'AllR/AraC/FucR' (regulator names)
- Fails with modern pandas versions

## Decision

**Continue with direct file parsing approach** instead of pymodulon:

### Pros of Direct Parsing
- ✅ Full control over data loading
- ✅ No external package dependencies to break
- ✅ Works with any pandas version
- ✅ Can handle both Excel (P. putida) and CSV (E. coli) formats
- ✅ Already working for P. putida

### Cons of pymodulon
- ❌ Version compatibility issues
- ❌ Unmaintained (last release 2021)
- ❌ Requires specific pandas version
- ❌ Doesn't support newest datasets
- ❌ Adds 47MB dependency

## Recommendation

Keep current implementation:
1. Excel parser for P. putida (working ✅)
2. Add CSV parser for E. coli (straightforward)
3. Remove pymodulon dependency (clean up)

## Next Steps

```bash
# Remove pymodulon
uv remove pymodulon

# Implement CSV parser directly
# Much simpler and more reliable!
```

## Alternative: Fix pymodulon

If we really wanted to use pymodulon, we'd need to:
1. Fork the package
2. Fix pandas compatibility
3. Submit PR
4. Wait for release

**Not worth it** - direct parsing is simpler and more maintainable.

## Conclusion

Direct file parsing is the right approach for this use case. We have full control and can support any organism format without depending on external packages that may break.
