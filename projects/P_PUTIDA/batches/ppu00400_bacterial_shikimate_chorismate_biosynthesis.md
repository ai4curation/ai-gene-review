---
title: "PSEPK shikimate and chorismate biosynthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [aroH, aroF-I, aroF-II, aroB, aroQ1, aroQ2, aroQ-III, aroE__Q88RQ5, aroE__Q88K85, aroE__Q88IJ7, PP_2608, aroK, aroA, aroC]
autolink_gene_symbols: false
---

# PSEPK shikimate and chorismate biosynthesis

- Module: `bacterial_shikimate_chorismate_biosynthesis`
- Source bucket: KEGG `ppu00400` (aromatic amino-acid biosynthesis)
- Focused genes: 13 pathway proteins plus one assessed family candidate
- Satisfiability: complete, with multiple alternative family members
- Module research: running
- Gene-level OpenScientist research: running

## Boundary

This batch converts phosphoenolpyruvate and erythrose 4-phosphate to chorismate.
Downstream tryptophan, phenylalanine, tyrosine, folate, and ubiquinone branches
are separate modules. AroA/PP_1770 is a fusion: its EPSP-synthase domain belongs
here, while its prephenate-dehydrogenase activity belongs to the tyrosine branch.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| DAHP and dehydroquinate formation | AroH Q88LR3, AroF-I Q88KG6, AroF-II Q88IB9, AroB Q88CV2 | Covered |
| Dehydroquinate to shikimate | AroQ1 Q88QD4, AroQ2 Q88K84, AroQ-III Q88IJ6; three canonical AroE-family proteins | Covered |
| Shikimate to EPSP | AroK Q88CV1, AroA Q88M05 | Covered |
| Chorismate formation | AroC Q88LU7 | Covered |

## Curation Findings

Paralogous DAHP synthases, dehydroquinases, and shikimate dehydrogenases are
modeled as alternative implementations of conserved reactions rather than as
duplicate pathway steps. PP_2608 was assessed as an AroE-family candidate but
is excluded from the module because direct characterization identifies it as
the divergent RifI2 oxidoreductase without an established shikimate-pathway
role. The AroA fusion is
split conceptually so its prephenate-dehydrogenase activity is not conflated
with EPSP synthesis.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-shikimate-and-chorismate-biosynthesis__ppu00400-deep-research-openscientist.md)
- `modules/bacterial_shikimate_chorismate_biosynthesis.yaml`
