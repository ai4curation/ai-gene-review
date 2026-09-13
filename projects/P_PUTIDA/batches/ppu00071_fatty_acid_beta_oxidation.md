---
title: "PSEPK ppu00071 bacterial fatty acid beta-oxidation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [fadE, fadB, fadA]
autolink_gene_symbols: false
---

# PSEPK ppu00071: bacterial fatty acid beta-oxidation

- Module: `bacterial_fatty_acid_beta_oxidation`
- Pathway context: KEGG `ppu00071` (fatty acid degradation)
- Focused genes: 3
- Broad membership-table candidates: 22

## Boundary

This batch covers the four-reaction saturated fatty acid beta-oxidation spiral:

1. `fadE` (PP_1893/Q88LN6): ETF-dependent acyl-CoA dehydrogenation
2. `fadB` (PP_2136/Q88L02): trans-2-enoyl-CoA hydration
3. `fadB` (PP_2136/Q88L02): NAD-dependent 3-hydroxyacyl-CoA oxidation
4. `fadA` (PP_2137/Q88L01): thiolytic cleavage and two-carbon shortening

Fatty-acid activation by FadD is upstream of the repeating spiral. Auxiliary
reactions for unsaturated substrates and pathway-specific acyl-CoA enzyme
paralogs are outside this module. The broad KEGG list is retained in the TSV;
membership alone is not evidence that a paralog performs the core spiral in
KT2440.

## Status

- [x] Fetch the focused genes from UniProt and GOA.
- [x] Consult the annotation-reviewer workflow on the PSEPK realization.
- [x] Complete module + `ppu00071` + PSEPK OpenScientist research.
- [x] Curate the three focused gene reviews.
- [x] Create a reusable four-reaction bacterial module with exact PSEPK exemplars.
- [ ] Complete OpenScientist gene-level research for FadE and FadA (FadE complete; FadA running).
- [x] Validate the module and focused gene reviews.
- [ ] Render the gene reviews and batch page.
- [ ] Open one PR for this module and shepherd review and CI.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `fadE` | PP_1893 | Q88LN6 | medium/long-chain acyl-CoA dehydrogenase | Retain the two specific activities and beta-oxidation process; localization remains uncertain |
| `fadB` | PP_2136 | Q88L02 | enoyl-CoA hydratase and hydroxyacyl-CoA dehydrogenase | Existing review already supports both core reactions and FadBA complex membership |
| `fadA` | PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase | Retain thiolase and beta-oxidation; add FadBA complex; remove electronic phenylacetate propagation |

## Evidence Notes

The exact UniProt records define the four reaction leaves and identify Q88L02
and Q88L01 as the alpha and beta subunits of the FadBA complex. The
species-aware OpenScientist report independently recovered FadE, FadB, and
FadA as the primary four-step realization, but also proposed several plausible
paralogs using homology and KEGG membership. Those paralogs are left as a
curation gap because their chain-length or pathway specificity has not been
established for KT2440.

The module uses Rhea reactions for direction-aware chemistry, exact UniProt
exemplars, and FadE/FadB/FadA family selectors. It has no module-level molecular
function or generic cytoplasm/cytosol assertion. The broad candidate inventory
is retained in
[`ppu00071_fatty_acid_beta_oxidation.tsv`](ppu00071_fatty_acid_beta_oxidation.tsv).
