---
title: "PSEPK nitrogen-regulatory phosphotransferase system"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ptsP, ptsH, ptsN]
autolink_gene_symbols: false
---

# PSEPK nitrogen-regulatory phosphotransferase system

This batch resolves the regulatory branch of KEGG `ppu02060` separately from
the already curated FruB/FruA fructose-uptake PTS. The reusable module is
`modules/bacterial_nitrogen_regulatory_pts.yaml`.

## Boundary

1. PtsP enzyme I(Ntr) accepts phosphate from PEP.
2. NPr, called `ptsH`/PP_0948 by UniProt and `ptsO` in primary KT2440 studies,
   relays phosphate from PtsP.
3. PtsN EIIA(Ntr) receives phosphate and acts as the terminal
   phosphorylation-state-dependent regulator.

The branch has no sugar permease and does not transport or phosphorylate a
carbohydrate. Conditional phosphate input from FruB is documented cross-talk,
not a required part. PHA accumulation, potassium transport, and central-carbon
effects are downstream regulatory outputs.

## Status

- [x] Define a species-neutral three-part PtsP-NPr-PtsN module.
- [x] Fetch and curate the three KT2440 gene reviews.
- [x] Reconcile the `ptsH` versus `ptsO` naming discrepancy.
- [x] Remove propagated sugar-PTS interpretations from the regulatory proteins.
- [ ] Complete OpenScientist gene, module, and module + pathway + taxon research
  (ptsN complete; ptsP, ptsH, module, and taxon jobs active and non-gating).
- [x] Complete independent annotation-reviewer and module audit.
- [x] Validate and render all artifacts.
- [x] Open draft PR [#2525](https://github.com/ai4curation/ai-gene-review/pull/2525).

The independent audit confirmed all existing-annotation decisions across the
three reviews. It also tightened each module participant from a broad PANTHER
family to its verified nitrogen-regulatory subfamily.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `ptsP` | PP_5145 | Q88CN5 | PEP-dependent enzyme I(Ntr) |
| `ptsH` (`ptsO`/NPr) | PP_0948 | Q88PA2 | Intermediate phosphocarrier |
| `ptsN` | PP_0950 | Q88PA0 | Terminal EIIA(Ntr) regulator |

PMID:18296519 directly establishes the primary in vivo flow as PEP to PtsP to
NPr to PtsN and describes the branch as unrelated to sugar traffic.
