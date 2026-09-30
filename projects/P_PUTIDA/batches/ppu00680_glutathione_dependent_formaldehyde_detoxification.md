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

Formate oxidation, PP_3970-associated formaldehyde mineralization, other
alternative formaldehyde dehydrogenases, efflux, and damage repair are separate
pathways or response systems. PP_3970 is excluded because it is not evidence
for either defined FrmA/FrmC step; its name, substrate chemistry, and
glutathione dependence remain unresolved.

## Status

- [x] Define a reusable three-step formaldehyde-detoxification module.
- [x] Curate the two KT2440 gene reviews.
- [x] Complete OpenScientist gene, module, and module + pathway + taxon research.
- [x] Complete independent annotation-reviewer and module audits.
- [x] Validate and render all artifacts.
- [x] Publish as one draft PR.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `frmA` | PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione oxidation |
| `frmC` | PP_1617 | Q88MF4 | S-formylglutathione hydrolysis |

## Research Integration

The completed generic and PSEPK-specific OpenScientist reports support the
three-step boundary and find the branch satisfiable through FrmA and FrmC.
They also support treating glutathione capture as spontaneous and the FrmA
oxidation as NAD+-biased. The stronger provider interpretation that this is a
secondary or backup route is retained as an inference: KT2440 genetics show
parallel formaldehyde oxidation capacity, but do not directly quantify flux
through FrmA-FrmC. PP_3970 remains outside this module because its precise
substrate chemistry and glutathione dependence are unresolved.
