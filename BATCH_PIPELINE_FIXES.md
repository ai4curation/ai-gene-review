# Batch Pipeline Fixes

## Issue
Command failed: `uv run python scripts/batch_gene_pipeline.py paint/human-no-IBA-simple.csv --providers openai perplexity perplexity-lite falcon`

## Root Causes

### 1. File Format Mismatch
**Problem:** The input file `paint/human-no-IBA-simple.csv` uses format:
```
organism,uniprot_id,gene_symbol
human,P15941,MUC1
```

But the parser expected format:
```
organism,gene,[uniprot_id],[alias]
human,TP53
human,TP53,P04637
```

**Result:** Parser was treating UniProt ID as gene and gene symbol as UniProt ID, causing fetch to fail.

### 2. Provider Name Mapping
**Problem:** `perplexity-lite` is an internal convenience name, but deep-research-client only knows about `perplexity`.

**Result:** Error: "Provider 'perplexity-lite' not available"

## Solutions

### 1. Smart Format Detection
Added auto-detection for UniProt-first format:

```python
def looks_like_uniprot_id(s: str) -> bool:
    """Check if string looks like a UniProt accession (e.g., P15941, Q9Y6A1)."""
    return bool(re.match(r'^[A-Z][0-9][A-Z0-9]{3,8}$', s))

# In parser:
if len(parts) == 3 and looks_like_uniprot_id(parts[1]):
    # Format: organism,uniprot_id,gene_symbol
    gene = parts[1]  # UniProt ID becomes gene_id
    uniprot_id = None
    alias = parts[2]  # Gene symbol becomes alias
else:
    # Format: organism,gene[,uniprot_id][,alias]
    # ... original logic
```

**How it works:**
- Detects UniProt ID pattern in column 1
- Automatically treats it as: organism, gene_id (UniProt), alias (gene symbol)
- Generates command: `fetch-gene human P15941 --alias MUC1`

### 2. Provider Name Mapping
Added mapping in `deep_research_wrapper.py`:

```python
# Map internal provider names to deep-research-client provider names
actual_provider = "perplexity" if provider == "perplexity-lite" else provider
```

Now `perplexity-lite` correctly maps to `perplexity` provider with low reasoning parameters.

## Supported Formats

### Format 1: Gene-first
```
organism,gene                    # human,TP53
organism,gene,uniprot_id         # human,TP53,P04637
organism,gene,uniprot_id,alias   # METEA,C5B1I4,,mllA
```

### Format 2: UniProt-first (auto-detected)
```
organism,uniprot_id,gene_symbol  # human,P15941,MUC1
```

**Auto-detection:** If column 1 matches pattern `[A-Z][0-9][A-Z0-9]{3,8}` (UniProt ID pattern)

## Testing

### Test 1: Format detection
```bash
# Input: human,P15941,MUC1
# Parsed as: organism=human, gene=P15941, alias=MUC1
# Command: fetch-gene human P15941 --alias MUC1
✅ PASS
```

### Test 2: All providers dry-run
```bash
uv run python scripts/batch_gene_pipeline.py test.csv \
  --providers openai perplexity perplexity-lite falcon --dry-run

✅ PASS - All providers generate correct commands
```

### Test 3: Provider mapping
```bash
just deep-research-perplexity-lite human TP53
# Maps to: --provider perplexity with params
✅ PASS
```

## Files Modified

1. **`scripts/batch_gene_pipeline.py`**
   - Added `looks_like_uniprot_id()` function
   - Updated `parse_gene_file()` with format auto-detection
   - Updated help text to document both formats

2. **`scripts/deep_research_wrapper.py`**
   - Added provider name mapping: `perplexity-lite` → `perplexity`
   - Updated docstrings

3. **`examples/README_batch_pipeline.md`**
   - Documented both input formats
   - Added auto-detection explanation
   - Added UniProt format examples

## Usage Examples

### Example 1: Original format
```bash
cat > genes.txt << EOF
human,TP53
METEA,C5B1I4,,mllA
EOF

just batch-pipeline genes.txt --providers perplexity
```

### Example 2: UniProt format (from user's file)
```bash
# File: paint/human-no-IBA-simple.csv
# Format: organism,uniprot_id,gene_symbol
just batch-pipeline paint/human-no-IBA-simple.csv \
  --providers openai perplexity perplexity-lite falcon
```

## Verification

The command that was failing now works:
```bash
uv run python scripts/batch_gene_pipeline.py paint/human-no-IBA-simple.csv \
  --providers openai perplexity perplexity-lite falcon

# ✅ Now correctly parses UniProt format
# ✅ All providers work (including perplexity-lite)
```
