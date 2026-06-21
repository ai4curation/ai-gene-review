---
name: gocam-curation
description: >
  Evaluate and review GO-CAM (Gene Ontology Causal Activity Model) activities /
  annotons — molecular-function typing, has-input, causal relations, complexes,
  evidence — and check their consistency with gene annotation reviews. Use when
  reviewing cached GO-CAMs under gocams/, filling a GoCamReview YAML
  (gocams/<id>/<id>-review.yaml), or grounding a module in GO-CAM models.
---

# GO-CAM curation & review

Use this skill to **read and assess** GO-CAM models. This project is read-only:
we never edit or upload models. We cache them (`gocams/<id>/<id>-src.yaml`),
index their activities (`gocams/index.tsv`), and record assessments in
`gocams/<id>/<id>-review.yaml` (schema class `GoCamReview`).

## What an activity (annoton) is

Each GO-CAM activity couples:

- `enabled_by` — the **gene product** carrying the activity;
- `molecular_function` — the GO MF term;
- `part_of` — optional **biological process** it contributes to;
- `occurs_in` — optional **cellular component** it happens in;
- `causal_associations` — directed edges to **downstream** activities.

In the cached YAML these are fields of each entry under `activities:`; they are
flattened one-row-per-activity into `gocams/index.tsv` (join key:
`gene_product`).

## How to evaluate an activity

For each activity, work through these and record the outcome in the
`GoCamActivityReview`:

1. **Molecular function** — most specific correct term; not a bare `binding`
   term; the real role (catalytic / receptor / adaptor / sequestering).
   → `references/molecular-function.md`
2. **`has input`** — names the substrate / target-gene / effector / cargo, not a
   ligand or raw DNA. → `references/has-input.md`
3. **Causal edges** — direct vs indirect, subject→object directionality,
   mechanism vs phenotype. → `references/causal-relations.md`
4. **Complexes** — right active subunit vs complex term.
   → `references/complexes.md`
5. **Context & evidence** — `occurs_in`, `part_of`, ECO + reference present.
6. **Verdict, QC flags, and consistency with the gene review** — the controlled
   vocabularies and the final checklist.
   → `references/qc-and-consistency.md`

Anchor every non-trivial verdict in **verbatim** `supporting_text` from a cited
reference, the same discipline as gene-review `supporting_text`. Biological
plausibility alone is not evidence.

## Progressive disclosure

The `references/` files hold the detailed rules; read the relevant one only when
you hit that case. They map directly onto the schema enums (`GoCamClaimVerdictEnum`,
`GoCamQcFlagEnum`, `GoCamConsistencyEnum`) so a review is machine-checkable:

- `references/molecular-function.md` — MF specificity, binding≠function, adaptor/sequestering/catalytic.
- `references/has-input.md` — `has input` semantics per activity type.
- `references/causal-relations.md` — direct/indirect causal, directionality, mechanism vs phenotype.
- `references/complexes.md` — complex subunit representation.
- `references/qc-and-consistency.md` — verdict scale, QC-flag glossary, consistency categories, checklist.

## Workflow

```bash
just seed-gocam-review <model_id>      # one PENDING entry per cached annoton
# ... assess each activity using this skill ...
just validate-gocam-review gocams/<model_id>/<model_id>-review.yaml
```

The point of caching GO-CAMs here is the cross-check: join `gocams/index.tsv` to
`genes/**/<gene>-ai-review.yaml` on gene product and record a
`GoCamConsistencyEnum` verdict per activity. `CONFLICT` (the review removed /
negated / over-annotated this function) and `NOT_IN_REVIEW` (a candidate gap) are
the signals worth surfacing.

## Attribution

Adapted from the GO Consortium GO-CAM annotation guidelines and the
`gocam-best-practice` / `validate-claims` skills in
[`geneontology/gocam-agent`](https://github.com/geneontology/gocam-agent),
tuned for this project's read-only ingestion and consistency-checking.
