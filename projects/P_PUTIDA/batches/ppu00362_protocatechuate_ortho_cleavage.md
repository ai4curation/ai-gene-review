---
title: "PSEPK protocatechuate ortho-cleavage branch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [pcaG, pcaH, pcaB, pcaC, pcaD]
autolink_gene_symbols: false
---

# PSEPK protocatechuate ortho-cleavage branch

- Module: `protocatechuate_ortho_cleavage`
- Source bucket: KEGG `ppu00362` (benzoate degradation)
- Focused genes: five proteins implementing four consecutive reactions
- Satisfiability: complete
- Module research: running
- Gene-level OpenScientist research: running

## Boundary

This batch converts protocatechuate to 3-oxoadipate. Aromatic-acid uptake and
upper pathways that produce protocatechuate are upstream. The shared PcaIJF
lower pathway, which activates and cleaves 3-oxoadipate to central metabolites,
is intentionally separate.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Intradiol ring cleavage | PcaG Q88E13 and PcaH Q88E12 | Covered as a two-subunit complex |
| Carboxymuconate cycloisomerization | PcaB Q88N37 | Covered |
| Carboxymuconolactone decarboxylation | PcaC Q88N35 | Covered |
| Enol-lactone hydrolysis | PcaD Q88N36 | Covered |

## Curation Findings

The PcaGH molecular function belongs to the assembled dioxygenase complex;
neither subunit is modeled as independently enabling the reaction. Each
downstream catalytic molecular function is attached to its reaction-level leaf
annoton. No generic cytoplasmic localization is asserted at module level.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__protocatechuate-ortho-cleavage__ppu00362-deep-research-openscientist.md)
- `modules/protocatechuate_ortho_cleavage.yaml`
