# Batch Gene Pipeline

## Overview

The batch gene pipeline allows you to process multiple genes at once, fetching gene data and running deep research providers for each gene in a single command.

## Quick Start

### 1. Create an input file

Create a text file with your genes, one per line. The file supports both CSV and TSV format:

```
# Format: organism,gene[,uniprot_id][,alias]

# Simple format:
human,TP53
human,BRCA1

# With UniProt ID:
human,ACTB,P60709

# With alias (for directory/file naming):
METEA,C5B1I4,,mllA
9BACT,F0JBF1,,HgcB

# Arabidopsis:
ARATH,BRI1
ARATH,FT
```

See `batch_genes_example.txt` for a complete example.

### 2. Run the pipeline

```bash
# Fetch genes only (no deep research)
just batch-pipeline genes.txt

# Fetch genes and run perplexity research
just batch-pipeline genes.txt --providers perplexity

# Fetch genes and run multiple research providers
just batch-pipeline genes.txt --providers openai perplexity perplexity-lite

# Skip fetch if genes already exist, only run research
just batch-pipeline genes.txt --skip-fetch --providers perplexity

# Force overwrite existing files
just batch-pipeline genes.txt --providers perplexity --force
```

## Input File Format

The input file supports two formats (auto-detected):

### Format 1: Gene-first (for genes without UniProt ID or when using locus tags)

**Basic:**
```
organism,gene
```
Example:
```
human,TP53
mouse,Trp53
```

**With UniProt ID:**
```
organism,gene,uniprot_id
```
Example:
```
human,TP53,P04637
human,BRCA1,P38398
```

**With alias:**
```
organism,gene,uniprot_id,alias
```
The alias is used for directory and file naming. Leave uniprot_id empty if not needed:
```
METEA,C5B1I4,,mllA
9BACT,F0JBF1,,HgcB
```

### Format 2: UniProt-first (auto-detected when column 1 looks like UniProt ID)

This format is convenient when you have a list of UniProt IDs with gene symbols:

```
organism,uniprot_id,gene_symbol
```

Example:
```
human,P15941,MUC1
human,O60763,USO1
human,P04118,CLPS
```

**How it works:**
- Automatically detected when the second column matches UniProt ID pattern (e.g., P15941, Q9Y6A1)
- The UniProt ID becomes the gene_id (used for directory organization)
- The gene symbol becomes the alias (used for gene naming)
- Equivalent to: `fetch-gene human P15941 --alias MUC1`

### Comments and blank lines

Lines starting with `#` are treated as comments and ignored. Blank lines are also ignored:

```
# This is a comment
human,TP53

# Another comment
human,BRCA1
```

## Available Deep Research Providers

You can specify one or more providers:

- **openai** - GPT-based deep research (most comprehensive)
- **perplexity** - Perplexity AI with sonar models (good balance)
- **perplexity-lite** - Faster Perplexity with reduced reasoning (quickest)
- **falcon** - Local models (if configured)

## Options

### `--providers` (optional)
Specify which deep research providers to run. Can specify multiple:
```bash
just batch-pipeline genes.txt --providers openai perplexity
```

### `--skip-fetch` (optional)
Skip the fetch-gene step if genes already exist. Useful for re-running research:
```bash
just batch-pipeline genes.txt --skip-fetch --providers perplexity-lite
```

### `--force` (optional)
Force overwrite existing UniProt and GOA files when fetching:
```bash
just batch-pipeline genes.txt --force
```

### `--dry-run` (optional)
Show what would be processed without actually running any commands:
```bash
just batch-pipeline genes.txt --providers perplexity --dry-run
```

### `--continue-on-error` (default: true)
Continue processing remaining genes even if one fails. This is enabled by default.

## Examples

### Example 0: Preview what will be processed (dry-run)
```bash
# See what would be processed without running anything
just batch-pipeline my_genes.txt --providers perplexity --dry-run
```

### Example 1: Fetch a batch of human genes
```bash
# Create input file
cat > my_genes.txt << EOF
human,TP53
human,BRCA1
human,EGFR
human,KRAS
EOF

# Fetch all genes
just batch-pipeline my_genes.txt
```

### Example 2: Fetch and research with Perplexity
```bash
# Create input file for METEA genes
cat > metea_genes.txt << EOF
METEA,C5B1I4,,mllA
METEA,C5B1I5,,mllB
METEA,C5B1I6,,mllC
EOF

# Fetch and research
just batch-pipeline metea_genes.txt --providers perplexity
```

### Example 3: Run research only on existing genes
```bash
# Genes already fetched, just run research
just batch-pipeline my_genes.txt --skip-fetch --providers openai perplexity
```

### Example 4: UniProt ID format (auto-detected)
```bash
# Create file with UniProt IDs and gene symbols
cat > uniprot_genes.txt << EOF
human,P15941,MUC1
human,O60763,USO1
human,P04118,CLPS
EOF

# Auto-detects UniProt format and uses gene symbols as aliases
just batch-pipeline uniprot_genes.txt --providers perplexity
```

### Example 5: Mixed organism batch
```bash
cat > mixed_genes.txt << EOF
human,TP53
mouse,Trp53
ARATH,BRI1
yeast,YBR078W
EOF

just batch-pipeline mixed_genes.txt --providers perplexity-lite
```

## Output

For each gene, the pipeline will:

1. **Fetch gene data** (unless `--skip-fetch` is used):
   - Download UniProt record to `genes/<organism>/<gene>/<gene>-uniprot.txt`
   - Download GOA annotations to `genes/<organism>/<gene>/<gene>-goa.tsv`
   - Create stub YAML file at `genes/<organism>/<gene>/<gene>-ai-review.yaml`

2. **Run deep research** (if `--providers` specified):
   - Create research file at `genes/<organism>/<gene>/<gene>-deep-research-<provider>.md`

## Pipeline Summary

At the end of execution, you'll see a summary like:

```
============================================================
SUMMARY
============================================================
Total genes: 10
Fetch successful: 9
Fetch failed: 1

perplexity successful: 8
perplexity failed: 2
```

## Troubleshooting

### "Gene data already exists" warning
By default, existing files are not overwritten. Use `--force` to override:
```bash
just batch-pipeline genes.txt --force
```

### Some genes fail
The pipeline continues processing remaining genes by default. Check the output for specific error messages.

### Re-run research only
If genes are already fetched, skip the fetch step:
```bash
just batch-pipeline genes.txt --skip-fetch --providers perplexity
```

## Direct Script Usage

You can also run the script directly:

```bash
uv run python scripts/batch_gene_pipeline.py genes.txt --providers perplexity
```

Use `--help` for full options:
```bash
uv run python scripts/batch_gene_pipeline.py --help
```
