---
title: "PSEPK glutathione-dependent formaldehyde detoxification"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [frmA, frmC]
autolink_gene_symbols: false
---

# PSEPK glutathione-dependent formaldehyde detoxification

This batch extracts the FrmA-FrmC branch from the broad KEGG `ppu00680`
"methane metabolism" map. KT2440 does not assimilate formaldehyde through this
route; it detoxifies it by oxidation to formate.

## Boundary

1. Glutathione captures formaldehyde as S-(hydroxymethyl)glutathione.
2. FrmA oxidizes that hemithioacetal to S-formylglutathione.
3. FrmC hydrolyzes S-formylglutathione to formate and regenerates glutathione.

Formate oxidation, alternative formaldehyde dehydrogenases, efflux, and damage
repair are separate pathways or response systems.

## Status

- [x] Define a reusable three-step formaldehyde-detoxification module.
- [x] Curate the two KT2440 gene reviews.
- [ ] Complete OpenScientist gene, module, and module + pathway + taxon research (jobs active; non-blocking for draft publication).
- [x] Complete independent annotation-reviewer and module audits.
- [x] Validate and render all artifacts.
- [x] Publish as one draft PR.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `frmA` | PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione oxidation |
| `frmC` | PP_1617 | Q88MF4 | S-formylglutathione hydrolysis |
