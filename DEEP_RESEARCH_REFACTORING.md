# Deep Research Refactoring - DRY Implementation

## Summary of Changes

Refactored the deep research just targets to follow the DRY (Don't Repeat Yourself) principle by consolidating common logic into a reusable Python wrapper script.

## Before (Repetitive Code)

Each provider had ~20 lines of duplicate bash logic:

```just
deep-research-openai organism gene_or_uniprot *args="":
    #!/usr/bin/env bash
    if [[ "{{args}}" == *"--alias "* ]]; then
        alias=$(echo "{{args}}" | sed -n 's/.*--alias \([^ ]*\).*/\1/p')
        other_args=$(echo "{{args}}" | sed 's/--alias [^ ]*//')
        output_path="genes/{{organism}}/${alias}/${alias}-deep-research-openai.md"
        uv run deep-research-client research --template templates/gene_research_go_focused.md \
            --var "organism={{organism}}" \
            --var "gene_or_uniprot={{gene_or_uniprot}}" \
            --var "gene_symbol=${alias}" \
            --provider openai --output "$output_path" $other_args
    else
        output_path="genes/{{organism}}/{{gene_or_uniprot}}/{{gene_or_uniprot}}-deep-research-openai.md"
        uv run deep-research-client research --template templates/gene_research_go_focused.md \
            --var "organism={{organism}}" \
            --var "gene_or_uniprot={{gene_or_uniprot}}" \
            --provider openai --output "$output_path" {{args}}
    fi
```

**Problems:**
- Same logic duplicated 4 times (openai, perplexity, perplexity-lite, falcon)
- Manual extraction of `--alias` from args
- Gene symbol only used if `--alias` provided
- Hard to maintain - changes needed in 4 places

## After (DRY Implementation)

### 1. Created Wrapper Script: `scripts/deep_research_wrapper.py`

Consolidates all common logic:
- **Gene symbol lookup**: Automatically extracts gene symbol from UniProt file if `--alias` not provided
- **Path construction**: Builds correct output paths
- **Template variables**: ALWAYS passes both `gene_symbol` and `gene_id` to template
- **Provider-specific logic**: Handles differences between providers (e.g., perplexity-lite uses query instead of template)

### 2. Updated Template: `templates/gene_research_go_focused.md`

Now ALWAYS uses both gene symbol and gene ID (clearer naming):
```markdown
# Gene Research for Functional Annotation

Please provide a comprehensive research report on the gene {gene_symbol} ({gene_id}) in {organism}.

...

## Gene Information
- **Gene Symbol**: {gene_symbol}
- **Gene ID**: {gene_id}
- **Organism**: {organism}

Note: Gene ID may be a UniProt accession, locus tag, or gene symbol depending on the organism and data source.
```

**Key improvement**: Template now ALWAYS receives both values, not just when `--alias` is provided.

### 3. Simplified Just Targets

Each target is now just 1 line with clearer parameter naming:

```just
# Deep research using OpenAI (GPT models)
# Gene symbol automatically looked up from UniProt file if --alias not provided
deep-research-openai organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} openai {{args}}

deep-research-perplexity organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} perplexity {{args}}

deep-research-perplexity-lite organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} perplexity-lite {{args}}

deep-research-falcon organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} falcon {{args}}
```

**Note**: Parameter renamed from `gene_or_uniprot` to `gene_id` for clarity - it's the identifier used to organize data.

## Benefits

### 1. **Automatic Gene Symbol Lookup**
No more need to manually specify `--alias` for genes that already have UniProt files:

```bash
# Before: Always had to check if you needed --alias
just deep-research-perplexity METEA mxcE --alias mxcE  # Redundant!

# After: Automatically looks up gene symbol from UniProt
just deep-research-perplexity METEA mxcE  # Just works!
```

### 2. **Better Template Information**
Template now ALWAYS receives both gene symbol AND gene ID (not just with --alias):

```
# Without alias (automatic lookup):
Gene Symbol: mxcE
Gene ID: mxcE

# With alias:
Gene Symbol: mllA
Gene ID: C5B1I4

# Human gene (both same):
Gene Symbol: TP53
Gene ID: TP53
```

### 3. **Single Source of Truth**
- Logic changes only need to happen in one place (`deep_research_wrapper.py`)
- Template variable handling centralized
- Path construction standardized

### 4. **Reduced Code**
- **Before**: ~80 lines of bash code (20 lines × 4 providers)
- **After**: ~4 lines of just targets + 1 reusable Python script
- **Reduction**: 95% less duplicate code in justfile

## Usage Examples

### With automatic lookup
```bash
# Gene symbol automatically looked up from UniProt file
just deep-research-perplexity human TP53
# Looks up: TP53
# Passes to template: gene_symbol=TP53, gene_id=TP53

just deep-research-openai METEA mxcE
# Looks up: mxcE from UniProt file
# Passes to template: gene_symbol=mxcE, gene_id=mxcE
```

### With explicit alias
```bash
# For genes without UniProt files yet, or to use custom names
just deep-research-perplexity METEA C5B1I4 --alias mllA
# Uses alias: mllA
# Passes to template: gene_symbol=mllA, gene_id=C5B1I4
```

**Key Point**: Both `gene_symbol` and `gene_id` are ALWAYS passed to the template now, providing clear context.

### With extra arguments
```bash
# Pass additional args to deep-research-client
just deep-research-openai human TP53 --extra-args --param "model=gpt-4o"
```

## Testing

```bash
# Test gene symbol lookup from UniProt
uv run python scripts/deep_research_wrapper.py METEA mxcE perplexity --extra-args --help
# Output: Looked up gene symbol from UniProt: mxcE

# Test with alias
uv run python scripts/deep_research_wrapper.py METEA C5B1I4 perplexity --alias mllA --extra-args --help
# Uses gene_symbol=mllA (from --alias, not lookup)
```

## Migration Notes

### For existing workflows
All existing commands continue to work exactly as before:

```bash
# These all still work:
just deep-research-openai human TP53
just deep-research-perplexity METEA C5B1I4 --alias mllA
just deep-research-perplexity-lite ARATH BRI1
```

### For batch pipeline
The batch pipeline automatically uses the wrapper, so it also benefits from automatic gene symbol lookup.

## Files Changed

1. **Created**: `scripts/deep_research_wrapper.py` - Main wrapper script
2. **Modified**: `templates/gene_research_go_focused.md` - Now uses both gene_symbol and gene_or_uniprot
3. **Modified**: `project.justfile` - Simplified all deep-research-* targets

## Technical Details

### Gene Symbol Lookup Logic

The wrapper looks up gene symbols from UniProt files using this logic:

1. If `--alias` provided: Use it as gene_symbol
2. Else: Look for UniProt file at `genes/{organism}/{gene_or_uniprot}/{gene_or_uniprot}-uniprot.txt`
3. Parse the `GN   Name=...` line from UniProt file
4. Clean up annotations like `{ECO:0000313|EMBL:...}`
5. Use extracted gene name as gene_symbol

### Pattern Matching

Handles various UniProt gene name formats:
```
GN   Name=TP53; Synonyms=P53;                      → TP53
GN   Name=mxcE {ECO:0000313|EMBL:ACS42506.1};      → mxcE
GN   OrderedLocusNames=AT1G01010;                  → Skips, continues looking
```
