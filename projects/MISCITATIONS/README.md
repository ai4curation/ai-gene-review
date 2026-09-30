---
title: "Miscitation review — supporting material"
---

# Miscitation review — supporting material

Supporting material for the [Miscitation Review project](../MISCITATIONS.md).

## Contents

- `aggregate_miscitations.py` — reproducible aggregator. Walks every
  `genes/*/*/*-ai-review.yaml`, pulls out each `references[].reference_review`
  block, and writes the register and the TSV below. It reads only what reviewers
  have already recorded; it makes no judgment of its own.
- `miscitation-register.md` — **generated** register (do not edit by hand):
  counts by `correctness`, counts by organism, and a table of every non-`VERIFIED`
  reference with gene, identifier, title and `review_notes`.
- `reports/miscitations.tsv` (written at the repo root, not here) — one row per
  adjudicated reference, with the **untruncated** `review_notes`, for querying
  and triage.

## Regenerate

```bash
uv run python projects/MISCITATIONS/aggregate_miscitations.py
```

Re-run after new reviews land, or after adjudicating references in an existing
review. The register is regenerated wholesale from the current state of the YAML,
so it never needs hand-editing.

## What counts as "flagged"

`ReferenceCorrectnessEnum` has six values. The register treats them in three groups:

| Group | Values | Meaning |
|---|---|---|
| Clean | `VERIFIED` | Checked; identifier resolves to the intended, supporting paper |
| Unchecked | `UNVERIFIED` | Adjudication started but this reference not yet checked |
| **Flagged** | `WRONG_IDENTIFIER`, `MISCITED`, `DISPUTED`, `LOW_QUALITY` | A reviewer has positively judged this citation to be a problem |

Percentages on the project page are *flagged / adjudicated*, not flagged / all
references — most references in the repo carry no `reference_review` at all and
are simply unexamined.
