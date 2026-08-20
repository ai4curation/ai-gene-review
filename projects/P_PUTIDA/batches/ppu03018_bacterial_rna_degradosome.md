---
title: "PSEPK bacterial RNA degradosome"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [rne, rhlB, pnp, eno]
autolink_gene_symbols: false
---

# PSEPK bacterial RNA degradosome

- Module: `bacterial_rna_degradosome`
- Source bucket: KEGG `ppu03018` (RNA degradation)
- Focused genes: four canonical core components
- Satisfiability: complete
- OpenScientist module and gene research: running

## Boundary

This module covers the RNase E-centered degradosome core and the coupled
endonucleolytic, helicase, and phosphorolytic activities. PAP I, RppH, Hfq,
RNase R, other DEAD-box helicases, polyphosphate enzymes, chaperones, RecQ, and
Rho are related RNA-decay or stress proteins but are not assigned to the core
complex from KEGG membership alone.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Core assembly | RNase E Q88LM4 and enolase Q88MF9 | Covered |
| Endonucleolytic initiation | RNase E Q88LM4 | Covered |
| RNA unwinding | RhlB Q88NB7 | Covered |
| Phosphorolytic exonucleolysis | PNPase Q88DW0 | Covered |

## Curation Findings

Enolase is included as a structural degradosome participant, but its glycolytic
molecular function is not misrepresented as RNA catalysis. Molecular functions
are attached only to the RNase E, RhlB, and PNPase activity leaves. The broad
KEGG RNA-degradation bucket is retained only as discovery context.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-rna-degradosome__ppu03018-deep-research-openscientist.md)
- `modules/bacterial_rna_degradosome.yaml`
