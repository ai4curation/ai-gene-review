---
title: "Retraction check — supporting material"
---

# Retraction check — supporting material

Supporting material for the [Retracted Literature project](../RETRACTIONS.md).

## Contents

- `check_retractions.py` — the checker. Walks every `genes/*/*/*-ai-review.yaml`,
  collects each `PMID:` citation **with its citation site** (`reference`,
  `annotation` = an annotation's `original_reference_id`, or `supporting_text` =
  a `supported_by[].reference_id`), queries PubMed in batches of 200 through NCBI
  E-utilities `efetch`, and reads the `PublicationType` list and the
  `CommentsCorrections` `RefType`s. Records that are themselves retraction /
  expression-of-concern / erratum **notices** are excluded — citing the notice is
  good practice, not a defect.
- `retraction-check.tsv` — **generated**: one row per flagged PMID, with severity,
  the raw PubMed signals, the notice PMID(s), which genes cite it, how they cite
  it, and whether the review already records `is_invalid: true`.
- `retraction-check.json` — **generated**: the same data plus run totals and the
  PMIDs PubMed did not resolve.
- `retraction-register.md` — **generated** register (do not edit by hand):
  retractions first, then expressions of concern, then errata in a quiet
  informational section.

## Regenerate

```bash
uv run --no-dev python projects/RETRACTIONS/check_retractions.py
```

A full pass is ~126 `efetch` requests over ~25,000 PMIDs and takes the better part
of an hour; set `NCBI_API_KEY` to raise the rate limit. Useful variants:

```bash
# check specific PMIDs (still reports where they are cited in the reviews)
uv run --no-dev python projects/RETRACTIONS/check_retractions.py --pmids 19225519

# rebuild the register from the last run, no network
uv run --no-dev python projects/RETRACTIONS/check_retractions.py \
    --from-json projects/RETRACTIONS/retraction-check.json
```

## Severity tiers

| Tier | PubMed signal | Weight |
|---|---|---|
| `RETRACTED` | `Retracted Publication` publication type, or a `RetractionIn` reference | Actionable — the source is withdrawn |
| `EXPRESSION_OF_CONCERN` | `Expression of Concern` publication type, or an `ExpressionOfConcernIn` reference | Read the notice; not grounds for removing an annotation |
| `ERRATUM` | An `ErratumIn` reference | **Usually benign** — most errata are an author name, an affiliation or a figure legend |

The `citation_sites` column is what makes a row actionable: a retracted paper in a
`references:` list is bibliographic cleanup, whereas the same paper as an
annotation's `original_reference_id` is a curation question.
