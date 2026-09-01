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
- Focused reviews: RNase E, RhlB, and PNPase; enolase assessed and excluded
- Satisfiability: RNase E covered; accessory-partner realization unresolved
- OpenScientist module/pathway/taxon research: complete; rhlB gene research
  attempted but timed out after the full 7,200-second provider allowance

## Boundary

This module covers the RNase E-centered degradosome scaffold and the coupled
endonucleolytic, helicase-assisted, and 3'-to-5' exonucleolytic activities. PAP
I, RppH, Hfq, polyphosphate enzymes, chaperones, RecQ, and Rho are related
RNA-decay or stress proteins but are not assigned to the core complex from KEGG
membership alone. The reusable module is scoped to Gammaproteobacteria and
allows lineage-variable helicase and exonuclease partners.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Core scaffold | RNase E Q88LM4 | Covered |
| Endonucleolytic initiation | RNase E Q88LM4 | Covered |
| RNA unwinding | RhlB Q88NB7; RhlE-family alternative Q88D48 | Candidate uncertain |
| 3'-to-5' exonucleolysis | PNPase Q88DW0; RNase R Q88DE6 alternative | Candidate uncertain |

## Curation Findings

Enolase Q88MF9 remains in the KEGG source bucket but is not used to satisfy the
module: its existing KT2440 review states that degradosome membership has not
been demonstrated, and pathway membership alone is not complex-membership
evidence. Molecular functions are attached only to activity leaves, including
the RhlB/RhlE and PNPase/RNase R alternatives. The broad KEGG RNA-degradation bucket is retained only
as discovery context.

The completed OpenScientist module report found direct KT2440 evidence for
RNase E and PNPase function but not the exact complex composition. It therefore
prompted two reusable variant axes: RhlB versus RhlE-family helicases and
phosphorolytic PNPase versus hydrolytic RNase R. These alternatives are grounded
in same-genus and close-relative evidence and remain unresolved in KT2440.

The dedicated rhlB OpenScientist request exhausted the provider's 7,200-second
allowance on 2026-08-31 and produced no report artifact. The rhlB review therefore
uses the fetched UniProt record, cached full-text PMID:16275923, and the completed
module-level species-aware report; the failed run is not represented as research
evidence.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial_rna_degradosome__ppu03018-deep-research-openscientist.md)
- `modules/bacterial_rna_degradosome.yaml`
