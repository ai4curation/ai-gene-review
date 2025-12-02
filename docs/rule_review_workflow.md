# Rule Review Workflow

This document describes the complete workflow for reviewing ARBA and UniRule annotation rules.

## Overview

The rule review workflow consists of several distinct phases, each with specific dependencies:

1. **Initialize** - Create review file with proper structure
2. **Analyze** - Compute domain overlaps and redundancy
3. **Sync** - Populate review file with analysis data
4. **Research** - Gather literature support
5. **Review** - Fill in TODO placeholders with AI/human curation
6. **Render** - Generate HTML visualization

## Quick Start

For a new rule, run these commands in order:

```bash
# 1. Initialize the review file
just init-rule-review ARBA00026249

# 2. Analyze the rule (computes overlaps)
just analyze-rule ARBA00026249

# 3. Sync analysis data into review YAML
just sync-rule-review-single ARBA00026249

# 4. Research literature support
just rules-deep-research-perplexity ARBA00026249

# 5. Edit the review YAML to fill in TODO placeholders
# (Do this manually or with AI assistance)

# 6. Render HTML
just render-rule ARBA00026249
```

## Detailed Workflow Steps

### Step 1: Initialize Review File

```bash
just init-rule-review ARBA00026249
```

**What it does:**
- Creates `rules/arba/ARBA00026249/ARBA00026249-review.yaml` with proper structure
- Fetches and enriches the rule if `ARBA00026249.enriched.json` doesn't exist
- Populates all required fields with TODO placeholders

**IMPORTANT: Will NOT overwrite existing review YAML files**
- If the review YAML already exists, you'll get an error: `FileExistsError: Review file already exists`
- This prevents accidental overwrites that could lose manual edits
- To refresh a review file, manually delete it first: `rm rules/arba/ARBA00026249/ARBA00026249-review.yaml`

**Creates:**
- `ARBA00026249-review.yaml` (review file with TODO stubs) - **WILL NOT OVERWRITE IF EXISTS**
- `ARBA00026249.enriched.json` (if missing)

**Dependencies:**
- None (this is the first step)

**Output structure:**
```yaml
id: ARBA00026249
description: TODO: Provide a concise description
status: IN_PROGRESS
rule_type: ARBA
rule:
  rule_id: ARBA00026249
  condition_sets:
    - number: 1
      conditions: [...]
      notes: TODO: Describe this condition set
      # pairwise_overlap will be added by sync-rule-review-single
  go_annotations: [...]
  # entries field will be added by sync-rule-review-single
review_summary: TODO: Summarize the overall quality
action: UNDECIDED
# ... more TODO fields
```

### Step 2: Analyze Rule

```bash
just analyze-rule ARBA00026249
```

**What it does:**
- Computes pairwise domain overlaps (Jaccard, containment)
- Identifies InterPro2GO redundancies
- Generates heatmap visualization
- Creates analysis files in YAML, JSON, and text formats

**Creates:**
- `ARBA00026249-analysis.yaml` (required for sync step)
- `ARBA00026249-analysis.json`
- `ARBA00026249-analysis.txt`
- `ARBA00026249-heatmap.png`

**Dependencies:**
- `ARBA00026249.enriched.json`

**Lazy evaluation:**
Skips analysis if both `enriched.json` AND `analysis.yaml` already exist. Use `--force` to rebuild.

### Step 3: Sync Analysis Data

```bash
just sync-rule-review-single ARBA00026249
```

**What it does:**
- Reads `ARBA00026249-analysis.yaml`
- Populates the `entries` field in `ARBA00026249-review.yaml`
- Adds `pairwise_overlap` sections to each condition set

**Modifies:**
- `ARBA00026249-review.yaml` (adds `entries` and `pairwise_overlap` fields)

**Dependencies:**
- `ARBA00026249-review.yaml` (from init-rule-review)
- `ARBA00026249-analysis.yaml` (automatically created by analyze-rule dependency)

**Critical:** This step populates the `entries` field that is REQUIRED for HTML rendering to work correctly.

### Step 4: Research Literature

```bash
just rules-deep-research-perplexity ARBA00026249
```

**What it does:**
- Uses Perplexity AI to research literature support
- Creates a markdown file with citations and findings

**Creates:**
- `ARBA00026249-deep-research-perplexity.md`

**Dependencies:**
- None (can run in parallel with other steps)

**Alternatives:**
- `just rules-deep-research-falcon ARBA00026249` (local model)
- `just rules-deep-research-openai ARBA00026249` (GPT models)
- `just rules-deep-research-perplexity-lite ARBA00026249` (faster, cheaper)

### Step 5: Manual Review

Edit `ARBA00026249-review.yaml` to replace TODO placeholders with actual content:

**Key fields to fill in:**
- `description` - Concise summary of rule purpose
- `condition_sets[].notes` - Analysis of each condition set
- `review_summary` - Overall quality assessment
- `action` - ACCEPT, MODIFY, DEPRECATE, or UNDECIDED
- `action_rationale` - Justification for the action
- `parsimony.assessment` - PARSIMONIOUS, ACCEPTABLE, REDUNDANT, or OVERLY_COMPLEX
- `parsimony.notes` - Detailed parsimony analysis
- `literature_support.assessment` - STRONG, MODERATE, or WEAK
- `literature_support.notes` - Literature evidence summary
- `condition_overlap.notes` - Domain overlap interpretation
- `go_specificity.notes` - GO term specificity assessment
- `taxonomic_scope.notes` - Taxonomic restriction evaluation
- `confidence` - 0.0-1.0 confidence score

**Important:** The `entries` field should NOT be edited manually - it's populated automatically by `sync-rule-review-single`.

### Step 6: Render HTML

```bash
just render-rule ARBA00026249
```

**What it does:**
- Generates interactive HTML visualization
- Shows domain overlap heatmap
- Displays condition sets with pairwise overlaps
- Shows entries with relationships

**Creates:**
- `ARBA00026249-review.html`

**Dependencies:**
- `ARBA00026249-review.yaml` with populated `entries` field
- `ARBA00026249-analysis.yaml` (automatically created by analyze-rule dependency)

**Critical:** If `entries` field is missing, the HTML will be incomplete (missing CS labels, domain overlap tables, etc.).

## Dependency Graph

```
init-rule-review
    ↓ (creates review.yaml + enriched.json)
    ├─→ analyze-rule
    │       ↓ (creates analysis.yaml)
    │       ↓
    │   sync-rule-review-single
    │       ↓ (populates entries field in review.yaml)
    │       ↓
    │   render-rule ────→ HTML
    │
    └─→ rules-deep-research-*
            ↓ (creates deep-research.md)
            ↓
        (use for filling in review.yaml manually)
```

## File Dependencies Summary

| File | Created By | Required By | Purpose |
|------|-----------|-------------|---------|
| `{rule_id}.enriched.json` | init-rule-review | analyze-rule | Enriched rule data from UniProt |
| `{rule_id}-review.yaml` | init-rule-review | sync-rule-review-single, render-rule | Main review file |
| `{rule_id}-analysis.yaml` | analyze-rule | sync-rule-review-single, render-rule | Domain overlap analysis |
| `{rule_id}-analysis.json` | analyze-rule | - | JSON format of analysis |
| `{rule_id}-analysis.txt` | analyze-rule | - | Human-readable analysis report |
| `{rule_id}-heatmap.png` | analyze-rule | - | Overlap visualization |
| `{rule_id}-deep-research-*.md` | rules-deep-research-* | - | Literature research |
| `{rule_id}-review.html` | render-rule | - | Final HTML output |

## Common Issues

### Issue: HTML Missing CS Labels

**Symptom:** HTML shows domain overlap data but no "CS 1", "CS 2" labels.

**Cause:** Missing `entries` field in review YAML.

**Fix:** Run `just sync-rule-review-single ARBA00026249`

### Issue: HTML Shows All Dashes (----)

**Symptom:** Overlap table shows "----" instead of protein counts.

**Cause:** Analysis doesn't support that domain type (e.g., PANTHER support was added recently).

**Fix:** Re-run `just analyze-rule ARBA00026249` to regenerate analysis with updated code.

### Issue: Review File Exists Error

**Symptom:** `init-rule-review` fails with `FileExistsError: Review file already exists`.

**Cause:** Trying to initialize a rule that already has a review file. This is intentional to prevent accidental overwrites.

**Fix:**
1. **If you want to keep the existing review**: Skip `init-rule-review` and go directly to `analyze-rule` and `sync-rule-review-single`.
2. **If you want to start fresh**: Delete the existing file and re-run:
   ```bash
   rm rules/arba/ARBA00026249/ARBA00026249-review.yaml
   just init-rule-review ARBA00026249
   ```

### Issue: Analysis Skipped

**Symptom:** `analyze-rule` says "already exist, skipping expensive rebuild".

**Cause:** Lazy evaluation detected existing analysis files.

**Fix:** This is intentional. To force rebuild, delete the analysis files or add `--force` flag.

## Batch Operations

### Batch Initialize Multiple Rules

```bash
for rule_id in ARBA00026249 ARBA00026372 ARBA00047244; do
    just init-rule-review $rule_id
done
```

### Batch Analyze and Sync

```bash
for rule_id in ARBA00026249 ARBA00026372 ARBA00047244; do
    just analyze-rule $rule_id
    just sync-rule-review-single $rule_id
done
```

### Batch Render All Reviews

```bash
just render-all-rules
```

This automatically analyzes any rules that don't have analysis files yet.

## Best Practices

1. **Always run init-rule-review first** for new rules - don't manually create YAML files
2. **Run sync-rule-review-single after any re-analysis** to keep `entries` field up to date
3. **Don't edit the `entries` field manually** - it's auto-generated from analysis
4. **Use lazy evaluation** - `analyze-rule` won't re-compute if files exist unless forced
5. **Check HTML after rendering** to verify all data is present (CS labels, overlap tables, etc.)
6. **Keep analysis and review files in sync** - if you re-analyze, re-sync
7. **Use deep research output** to inform your manual review of TODO placeholders

## Advanced: Custom Cache Directory

For UniRule reviews, use a different cache directory:

```bash
just init-rule-review UR000000070 --cache-dir rules/unirule
just analyze-rule UR000000070 --cache-dir rules/unirule
just sync-rule-review-single UR000000070 rules/unirule
just render-rule UR000000070 rules/unirule
```

## See Also

- [Rule Analysis Documentation](rule_analysis.md) - Details on the analysis algorithm
- [Rule Review HTML Documentation](rule_review_html.md) - Details on HTML rendering
- [Rule Reviewer Agent Guide](../docs/agents/rule-reviewer.md) - AI-assisted review workflow
