---
title: "PSEPK ppu00946 Degradation of flavonoids batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_3195, PP_3197, PP_3198, PP_3199, PP_3204, PP_3205, PP_3206]
autolink_gene_symbols: false
---

# PSEPK ppu00946: Degradation of flavonoids

- Module seed: `bacterial_flavonoid_degradation`
- Candidate genes from membership table: 7, plus PP_3199 recovered from the
  contiguous locus and the FdeD/FdeE reaction assignment
- Primary bucket genes: 6
- Existing review files: 8
- Curated review files: 2
- Existing completed OpenScientist research files: 2

## Required Workflow

- [ ] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [ ] Curate each selected gene review.
- [ ] Validate module and gene reviews.
- [x] Open [PR #2832](https://github.com/ai4curation/ai-gene-review/pull/2832)
  for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | MISSING | MISSING | MISSING | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) |
| [ ] | `PP_3195` | PP_3195 | Q88I07 | kegg:ppu00946 | MISSING | MISSING | MISSING | Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein |
| [x] | `PP_3197` | PP_3197 | Q88I05 | kegg:ppu00946 | PRESENT | CURATED | PRESENT | Predicted FdeC-like flavonoid A-ring dioxygenase |
| [ ] | `PP_3198` | PP_3198 | Q88I04 | kegg:ppu00946 | MISSING | MISSING | MISSING | Ferredoxin, 2Fe-2S |
| [x] | `PP_3199` | PP_3199 | Q88I03 | recovered from locus/KO reaction | PRESENT | DRAFT | PRESENT | Predicted FdeE-like FAD-dependent flavonoid monooxygenase; 40.4% identity to characterized Hsero_1007 |
| [ ] | `PP_3204` | PP_3204 | Q88HZ8 | kegg:ppu00946 | MISSING | MISSING | MISSING | Cupin type-2 domain-containing protein |
| [ ] | `PP_3205` | PP_3205 | Q88HZ7 | kegg:ppu00946 | MISSING | MISSING | MISSING | Fumarylacetoacetate hydrolase family protein |
| [ ] | `PP_3206` | PP_3206 | Q88HZ6 | kegg:ppu00946 | MISSING | MISSING | MISSING | NAD-dependent epimerase/dehydratase domain-containing protein |

## Notes

- KEGG defines a five-reaction naringenin route: FdeD/FdeE (R13074),
  FdeC/FdeH (R13075), FdeJ (R13076), FdeB (R13077), and FdeI (R13078).
- The organism-specific gene mapping covers PP_3195, PP_3197, PP_3198,
  PP_3204, PP_3205, and PP_3206 directly. PP_3199 is the adjacent
  monooxygenase candidate for the missing FdeE partner and requires explicit
  orthology/experimental review.
- bglX is a possible glycoside-entry enzyme, not part of the five-reaction
  naringenin-aglycone core. It will remain outside the core module unless the
  species-aware report establishes a connected entry branch.
