---
title: "PSEPK trehalose synthesis from alpha-glucosides batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [treY, treZ, treSA]
autolink_gene_symbols: false
---

# PSEPK trehalose synthesis from alpha-glucans and maltose

## Workflow

- [x] Fetch or reuse the three selected gene reviews.
- [x] Attempt fresh OpenScientist research for TreY, TreZ, and TreSA; all three jobs finished without reports.
- [x] Attempt generic module research; the job finished without a report.
- [x] Attempt module + pathway + PSEPK research; the job finished without a report.
- [x] Reconcile route usage and add verified broader exemplars.
- [x] Curate all GOA rows and complete annotation review.
- [x] Validate and render all artifacts.
- [x] Open one draft PR: [#2572](https://github.com/ai4curation/ai-gene-review/pull/2572).

## Boundary

- TreY and TreZ form a coupled two-reaction route from maltooligosaccharide to trehalose.
- TreS is an alternative reversible route from maltose, not a third sequential step.
- Nucleotide-sugar-dependent trehalose synthesis and trehalose degradation are excluded.
- The bifunctional TreSB-Mak fusion is represented in the separate
  TreS-Mak-GlgE alpha-glucan-biosynthesis module because its genomic and domain
  context supports maltose-1-phosphate supply rather than a standalone
  trehalose-synthesis architecture.

## Notes

2026-08-13: Started as module 14 of the current 20-module batch. The module
keeps the two architectures explicit and avoids treating the one-step TreS
route as a standalone module.

2026-08-13: Annotation review completed. TreSA's sole GOA annotation was
accepted after checking EC/family evidence and direct KT2440 recombinant-enzyme
work. The cloning primer in a companion primary article matches the Q88IT1
N terminus, distinguishing the assayed standalone enzyme from TreSB. The three
gene-level and two module-level OpenScientist jobs all completed without output
files; this missing coverage is retained as a limitation rather than replaced
with synthetic provider reports.

The TreY-TreZ steps use the characterized Arthrobacter sp. Q36 proteins Q44315
and Q44316 as broader exemplars. The standalone route uses reviewed,
biochemically characterized Mycolicibacterium smegmatis TreS A0R6E0 alongside
the exact KT2440 TreSA Q88IT1 exemplar.
