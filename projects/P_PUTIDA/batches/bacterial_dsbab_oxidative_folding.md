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
- [x] Add canonical primary literature and curator notes for DsbA and DsbB.
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
is retained as non-core because the official definition is reversible and does
not establish physiological direction despite the reductase label. DsbB core
function is instead GO:0009055 electron transfer activity, matching the
quinone-linked relay. The module models the reciprocal redox cycle instead of
an artificial one-way ordering and keeps DsbC/DsbD repair, protein export,
quinone biosynthesis, and substrate-specific downstream pathways outside the
boundary.

## Primary Evidence

- PMID:9342327 establishes that DsbA donates its active-site disulfide to
  substrate proteins and that respiratory electron transfer maintains DsbA
  oxidation through DsbB.
- PMID:12853466 directly characterizes DsbB-catalyzed oxidation of DsbA by
  ubiquinone.
- The KT2440 DsbB1 and DsbB2 assignments remain explicitly by-similarity
  transfers; the primary studies establish the conserved family mechanism.
