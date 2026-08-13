---
title: "PSEPK bacterial putrescine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [speA, speB, speC]
autolink_gene_symbols: false
---

# PSEPK bacterial putrescine biosynthesis

## Workflow

- [x] Fetch the SpeA, SpeB, and SpeC gene-review inputs.
- [x] Consume all materialized OpenScientist research; no separate gene-level reports were produced.
- [x] Consume the generic module context embedded in the consolidated report; no separate generic report was produced.
- [x] Complete module + pathway + PSEPK research.
- [x] Reconcile route usage and literature evidence.
- [x] Curate every GOA row and complete annotation review.
- [x] Validate and render all artifacts.
- [ ] Open one draft PR.

## Boundary

- SpeA and SpeB form the coupled arginine-to-agmatine-to-putrescine route.
- SpeC is the alternative direct ornithine-to-putrescine route.
- Spermidine synthesis and gamma-glutamyl putrescine catabolism are excluded.
- The AguA-dependent deiminase branch is excluded from the core model because
  KT2440 lacks a verified completing N-carbamoylputrescine amidohydrolase.

## Notes

2026-08-13: Started as module 15 of the current 20-module batch. Exact PSEPK
UniProt exemplars and PTN identifiers from GOA are recorded, while broad
PANTHER families are constrained by the required molecular functions.

2026-08-13: The completed consolidated OpenScientist module + `ppu00330` +
PSEPK report and its HTML/PDF artifacts were reviewed. It supports all three
core candidates by orthology but found no KT2440-specific functional assays.
No separate SpeA, SpeB, SpeC, or generic-module report files materialized; this
missing provider coverage is recorded rather than reconstructed.

The module now uses explicit `ONE_OR_MORE` route variants. SpeA and SpeB are
connected only within the two-reaction arginine/agmatine route; SpeC is an
independent one-reaction ornithine route, with no artificial linear connection
between alternatives. Exact KT2440 UniProt exemplars are paired with broader
verified exemplars: E. coli P21170 for SpeA, E. coli P60651 for SpeB, and
same-family P. aeruginosa Q9HVQ3 for SpeC.

Residual uncertainties are target-specific: all three KT2440 assignments are
homology-based; Q88KU3 still needs substrate-specificity testing; relative
SpeA-SpeB versus SpeC flux is unknown; and PP_3019 remains an untested candidate
for the missing deiminase-branch completion step.
