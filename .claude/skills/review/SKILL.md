---
name: review
description: Review, either de-novo, or augment the review of an existing one. A list of deep research providers may be specified.
argument-hint: "[ORGANISM] [GENE_SYMBOL] (using [DEEP_RESEARCH_PROVIDER])"
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
- **MOD gene description** (non-human model organisms): `just mod-description-deep-research
  ORGANISM GENE_SYMBOL`. This is quick and should always be run. It writes the MOD's
  hand-written description (WormBase, FlyBase, SGD, MGI, ...) as
  `GENE-deep-research-<mod>.md`. Treat that file as a sparse, partly trusted deep-research
  source: it has no citations and no date, and it is often years old. Use it as a recall
  checklist. Each claim should be either covered in the review (traced to a publication)
  or set aside in `reference_review.review_notes` (for example "stale: superseded by
  PMID:..."). A claim found only in the MOD text is a lead for a literature search. Set that reference's
  `correctness` by one rule: `DISPUTED` if any claim is wrong, otherwise `UNVERIFIED`
  if any claim could not be traced (name it in `review_notes`), otherwise `VERIFIED`.

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

Two standing rules from the annotation-reviewer skill that apply to every review:

- **Do not second-guess deterministic pipeline outputs.** Term ids, labels, evidence
  codes, qualifiers and obsoletion status come from deterministic tooling; never assert
  from memory that a term is obsolete, merged, or renamed — verify via OLS/QuickGO
  before any rationale depends on it.
- **Review from the YAML; the GOA tsv is just its seed.** The reviewer works from the
  review YAML's `existing_annotations` (seeded deterministically from the tsv) and
  judges each row on "does this gene product execute a function in this process". The
  tsv never needs to be opened; if it is, ignore the gene-product-to-term relationship
  type (QUALIFIER column). The only annotation flags that matter are NOT
  (`negated: true`) and `qualifier: contributes_to`, which must be respected.
  Ortholog source reviews (e.g. `genes/human/<GENE>/`) are in scope when the defect
  is on the donor side.
