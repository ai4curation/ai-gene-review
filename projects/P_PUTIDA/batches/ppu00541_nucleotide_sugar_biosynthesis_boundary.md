---
title: "PSEPK ppu00541 Biosynthesis of various nucleotide sugars batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00541: Biosynthesis of various nucleotide sugars

- Module seed: `nucleotide_sugar_biosynthesis_boundary`
- Candidate genes from membership table: 26
- Primary bucket genes: 11
- Existing review files: 26
- Curated review files: 26
- Existing Asta research files: 26

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
| [x] | `gmhB` | PP_0059 | Q88RS0 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | D-glycero-beta-D-manno-heptose-1,7-bisphosphate 7-phosphatase (EC 3.1.3.82) (D,D-heptose 1,7-bisphosphate phosphatase) ( |
| [x] | `rmlC` | PP_0265 | Q88R69 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `PP_0500` | PP_0500 | Q88QJ2 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) |
| [x] | `kdsC` | PP_0956 | Q88P96 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC (EC 3.1.3.45) (KDO 8-P phosphatase) |
| [x] | `kdsD` | PP_0957 | Q88P95 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | Arabinose 5-phosphate isomerase (API) (EC 5.3.1.13) |
| [x] | `algA` | PP_1277 | Q88ND5 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphoman |
| [x] | `gmhA` | PP_1323 | Q88N89 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | Phosphoheptose isomerase (EC 5.3.1.28) (Sedoheptulose 7-phosphate isomerase) |
| [x] | `kdsA1` | PP_1611 | Q88MG0 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | 2-dehydro-3-deoxyphosphooctonate aldolase 1 (EC 2.5.1.55) (3-deoxy-D-manno-octulosonic acid 8-phosphate synthase 1) (KDO |
| [x] | `PP_1776` | PP_1776 | Q88M00 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) |
| [x] | `rfbC` | PP_1782 | Q88LZ4 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `rfbA` | PP_1783 | Q88LZ3 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) |
| [x] | `rfbD` | PP_1784 | Q88LZ2 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) |
| [x] | `rffG` | PP_1785 | Q88LZ1 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) |
| [x] | `gmd` | PP_1799 | Q88LX8 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose dehydratase) |
| [x] | `rmd` | PP_1800 | Q88LX7 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Oxidoreductase Rmd |
| [x] | `wbpV` | PP_1803 | Q88LX4 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | UDP-sugar epimerase |
| [x] | `wbpM` | PP_1805 | Q88LX2 | kegg:ppu00552 | PRESENT | CURATED | PRESENT | Polysaccharide biosynthesis protein |
| [x] | `PP_1806` | PP_1806 | Q88LX1 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | Arabinose 5-phosphate isomerase (API) (EC 5.3.1.13) |
| [x] | `kdsA2` | PP_1807 | Q88LX0 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | 2-dehydro-3-deoxyphosphooctonate aldolase 2 (EC 2.5.1.55) (3-deoxy-D-manno-octulosonic acid 8-phosphate synthase 2) (KDO |
| [x] | `rffE` | PP_1811 | Q88LW6 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) |
| [x] | `kdsB` | PP_1902 | Q88LM7 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | 3-deoxy-manno-octulosonate cytidylyltransferase (EC 2.7.7.38) (CMP-2-keto-3-deoxyoctulosonic acid synthase) (CKS) (CMP-K |
| [x] | `udg` | PP_2926 | Q88IS3 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) |
| [x] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |
| [x] | `hldE` | PP_4934 | Q88D93 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | Bifunctional protein HldE [Includes: D-beta-D-heptose 7-phosphate kinase (EC 2.7.1.167) (D-beta-D-heptose 7-phosphotrans |
| [x] | `PP_5212` | PP_5212 | Q88CG9 | kegg:ppu00541 | PRESENT | CURATED | PRESENT | Oxidoreductase, iron-sulfur-binding |
| [x] | `glmU` | PP_5411 | Q88BX6 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | Bifunctional protein GlmU [Includes: UDP-N-acetylglucosamine pyrophosphorylase (EC 2.7.7.23) (N-acetylglucosamine-1-phos |

## Notes

Generated UTC: 2026-07-08T01:00:14.750504+00:00

Completed first-pass curation on 2026-07-07 PDT / 2026-07-08 UTC. The
species-neutral boundary module is `modules/nucleotide_sugar_biosynthesis_boundary.yaml`.
All 26 KEGG `ppu00541` membership genes have review folders, Asta retrieval
reports, curated review YAMLs, successful `just validate PSEPK <gene>` runs,
and rendered review pages. The module passed both LinkML validation and
`ai_gene_review.validation.module_validator`.

Main curation conclusions:

- `ppu00541` is a composite nucleotide-sugar boundary map rather than a single
  linear biosynthetic pathway.
- ADP-heptose/LPS-core precursor chemistry is represented by `gmhA`, `hldE`,
  and `gmhB`.
- Kdo/CMP-Kdo chemistry is represented by `kdsD`, `PP_1806`, `kdsA1`,
  `kdsA2`, `kdsC`, and `kdsB`; paralog dominance for the API and KdsA pairs
  remains unresolved.
- dTDP-rhamnose/deoxy-sugar chemistry is represented by `rfbA`, `rffG`,
  `rmlC`, `rfbC`, `PP_0500`, and `rfbD`.
- GDP/UDP sugar branches and shared precursor context are represented by
  `algA`, `PP_1776`, `gmd`, `rmd`, `galU`, `udg`, `glmU`, and `rffE`.
- `wbpV`, `wbpM`, and `PP_5212` remain unresolved side nodes with no specific
  first-pass substrate or core molecular function assigned.
- `kdsC`'s CMP-sialic-acid cytidylyltransferase annotation was removed as a
  likely wrong spillover, and broad parent process, cofactor, catalytic, and
  localization terms were kept non-core or marked over-annotated where a
  specific enzyme term was available.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon nucleotide_sugar_biosynthesis_boundary`
  and `just module-pathway-deep-research-falcon nucleotide_sugar_biosynthesis_boundary ppu00541 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/nucleotide_sugar_biosynthesis_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__nucleotide_sugar_biosynthesis_boundary__ppu00541-deep-research-falcon.md`.
