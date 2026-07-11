---
title: "PSEPK ppu00910 Nitrogen metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00910: Nitrogen metabolism

- Module seed: `nitrogen_cycle`
- Candidate genes from membership table: 20
- Primary bucket genes: 19
- Existing review files: 20
- Curated review files: 20
- Existing Asta research files: 20

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `cynT` | PP_0100 | Q88RM9 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Carbonic anhydrase (EC 4.2.1.1) (Carbonate dehydratase) |
| [x] | `PP_0430` | PP_0430 | Q88QQ8 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Uncharacterized protein |
| [x] | `gdhA` | PP_0675 | Q88Q23 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate dehydrogenase |
| [x] | `arcC` | PP_0999 | Q88P54 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Carbamate kinase |
| [x] | `nirB` | PP_1705 | Q88M69 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Nitrite reductase [NAD(P)H] large subunit (EC 1.7.1.4) |
| [x] | `nirD` | PP_1706 | Q88M68 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Nitrite reductase |
| [x] | `gdhB` | PP_2080 | Q88L55 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) |
| [x] | `nasA` | PP_2092 | Q88L43 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Nitrate/nitrite transporter |
| [x] | `puuA-I` | PP_2178 | Q88KW1 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [x] | `PP_3148` | PP_3148 | Q88I53 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `PP_3392` | PP_3392 | Q88HG6 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Gamma carbonic anhydrase family protein |
| [x] | `yrpB` | PP_3827 | Q88G98 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Nitronate monooxygenase (Propionate 3-nitronate monooxygenase) |
| [x] | `PP_4399` | PP_4399 | Q88EQ4 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `PP_4547` | PP_4547 | Q88EB9 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `glnA` | PP_5046 | Q88CY3 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase (EC 6.3.1.2) |
| [x] | `gltD` | PP_5075 | Q88CV5 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate synthase (NADPH) beta subunit (EC 1.4.1.13) |
| [x] | `gltB` | PP_5076 | Q88CV4 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate synthase [NADPH] large chain (EC 1.4.1.13) (Glutamate synthase subunit alpha) |
| [x] | `spuB` | PP_5183 | Q88CJ7 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `spuI` | PP_5184 | Q88CJ6 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `puuA-II` | PP_5299 | Q88C84 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |

## Notes

Generated UTC: 2026-07-07T14:55:01.137680+00:00

## Workflow Notes

- Reused and validated the existing species-neutral module
  `modules/nitrogen_cycle.yaml`.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon nitrogen_cycle` and
  `just module-pathway-deep-research-falcon nitrogen_cycle ppu00910 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/nitrogen_cycle-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__nitrogen_cycle__ppu00910-deep-research-falcon.md`.
- Asta retrieval is present for all 20 genes. PP_3148 required one retry after a
  transient Asta network failure.
- All 20 candidate gene reviews validate with no errors. Remaining warnings are
  expected first-pass notices about Asta context not being cited as direct
  evidence and the intentional no-core review for PP_3392.
- Gene review pages rendered for all 20 candidates.

## Curation Notes

- KT2440 ppu00910 is an assimilation/boundary nitrogen-metabolism map rather
  than a complete nitrogen-cycle redox repertoire.
- `nasA`, `nirB`, and `nirD` cover the assimilatory nitrate/nitrite branch.
  `nirD` is treated as the 2Fe-2S/Rieske subunit contributing to NirBD nitrite
  reductase activity.
- `glnA`, `gltB`, `gltD`, `gdhA`, and `gdhB` cover central ammonia/glutamate
  assimilation and dehydrogenase chemistry. The `gdhB` aspartate
  aminotransferase transfer was removed.
- `puuA-I`, `puuA-II`, `spuB`, and `spuI` are polyamine-catabolic GS-fold
  enzymes; electronic glutamine synthetase or L-glutamine biosynthesis transfers
  were removed where product/EC evidence supports glutamate-putrescine or
  glutamylpolyamine ligase chemistry.
- `cynT`, PP_0430, `yrpB`, and PP_3392 are carbonic-anhydrase/nitronate boundary
  nodes. PP_3392 remains unresolved because it has no GOA annotations.
