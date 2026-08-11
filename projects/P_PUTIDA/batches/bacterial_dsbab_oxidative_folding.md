---
title: "PSEPK DsbA/DsbB oxidative protein folding"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [dsbA, dsbB1, dsbB2]
autolink_gene_symbols: false
---

# PSEPK DsbA/DsbB oxidative protein folding

This focused batch models the two-stage oxidative folding relay in the
Gram-negative cell envelope rather than folding all envelope-redox systems into
one module.

## Boundary

1. Oxidized DsbA introduces disulfide bonds into newly exported proteins and
   becomes reduced.
2. DsbB transfers electrons from reduced DsbA toward the quinone pool,
   regenerating oxidized DsbA for another catalytic turnover.

DsbC/DsbD-mediated isomerization and repair, Sec/Tat export, quinone
biosynthesis, and downstream substrate-specific pathways are outside the core.

## Status

- [x] Define a reusable two-reaction DsbA/DsbB module.
- [x] Curate the three KT2440 gene reviews.
- [ ] Complete OpenScientist gene, module, and taxon research (active; not a publication gate).
- [x] Complete independent annotation-reviewer and module-curation audits.
- [x] Validate and render all artifacts.
- [x] Prepare one dedicated draft PR.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `dsbA` | PP_0127 | Q88RK2 | Periplasmic substrate disulfide introduction |
| `dsbB1` | PP_0809 | P59345 | Membrane DsbA reoxidation |
| `dsbB2` | PP_0190 | P59344 | Second membrane DsbA-reoxidation paralog |

## Independent Audit

Every fetched GOA row for `dsbA`, `dsbB1`, and `dsbB2` was independently
reviewed. The broad DsbA oxidoreductase parent was changed from an
over-annotation judgment to non-core retention. The DsbB GO:0015035 assignment
was retained because the current GO definition explicitly runs from reduced
protein to oxidized protein, matching DsbA reoxidation. The module now models
the reciprocal redox cycle instead of an artificial one-way ordering and keeps
DsbC/DsbD repair, protein export, quinone biosynthesis, and substrate-specific
downstream pathways outside the boundary.
