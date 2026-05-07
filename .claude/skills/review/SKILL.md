---
description: Review, either de-novo, or augment the review of an existing one. A list of deep research providers may be specified.
argument-hint: [ORGANISM] [GENE_SYMBOL] ( using [DEEP_RESEARCH_PROVIDER] )
---

Review the gene specified in $ARGUMENTS.

* ORGANISM should typically be a uniprot species code (in a few cases we use lowercase GO names)
* GENE_SYMBOL should be the human readable gene symbol for that org

IMPORTANT: you MUST consult the annotation-reviewer.md subagent for this task.

## Step 1: Ensure gene data is fetched

Run `just fetch-gene ORGANISM GENE_SYMBOL` if the gene directory doesn't exist yet.

## Step 2: Run deep research AND publication caching in parallel

Publication caching only needs the GOA file (created by fetch-gene), so it can run
concurrently with deep research. Launch both at the same time:

- **Deep research**: If the user specifies a deep research provider(s), use that provider(s),
  otherwise default to falcon. Use `--fallback perplexity-lite` so that if the primary
  provider times out, it automatically retries with perplexity-lite.
  E.g. `just deep-research-falcon ORGANISM GENE_SYMBOL --fallback perplexity-lite`
- **Publication caching**: `just fetch-gene-pmids ORGANISM GENE_SYMBOL`

Run these two steps **in parallel** (e.g. as concurrent background agents or shell jobs).
Do NOT wait for deep research to finish before starting publication caching.

## Step 3: Fetch additional data (bacterial organisms)

For bacterial organisms (e.g. PSEPK, ECOLI, SALTY, or any prokaryote), after deep research,
also fetch FEBA/RB-TnSeq fitness data if available:

```
just fetch-fitness ORGANISM GENE_SYMBOL
```

This creates a GENE-fitness.md file with mutant fitness phenotypes and cofitness partners.
The annotation-reviewer agent will use this data as additional evidence when reviewing annotations.

## Step 4: Run annotation review

Invoke the annotation-reviewer subagent to systematically review all annotations.
