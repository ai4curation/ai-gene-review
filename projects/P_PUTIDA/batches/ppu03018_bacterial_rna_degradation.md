---
title: "PSEPK ppu03018 RNA degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03018: RNA degradation

- Module seed: `bacterial_rna_degradation`
- Candidate genes from membership table: 17
- Primary bucket genes: 15
- Existing review files: 17
- Curated review files: 17
- Existing Asta research files: 17

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
| [x] | `ppkB` | PP_0712 | Q88PY6 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | ADP/GDP-polyphosphate phosphotransferase (EC 2.7.4.-) (Polyphosphate kinase PPK2) |
| [x] | `rhlB` | PP_1295 | Q88NB7 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | ATP-dependent RNA helicase RhlB (EC 3.6.4.13) |
| [x] | `groEL` | PP_1361 | Q88N55 | kegg:ppu04156 | PRESENT | CURATED | PRESENT | Chaperonin GroEL (EC 5.6.1.7) (60 kDa chaperonin) (Chaperonin-60) (Cpn60) |
| [x] | `eno` | PP_1612 | Q88MF9 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase) (2-phosphoglycerate dehydratase) |
| [x] | `deaD` | PP_1868 | Q88LR1 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | ATP-dependent RNA helicase DeaD (EC 3.6.4.13) (Cold-shock DEAD box protein A) |
| [x] | `rne` | PP_1905 | Q88LM4 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Ribonuclease E (RNase E) (EC 3.1.26.12) |
| [x] | `recQ` | PP_4516 | Q88EE9 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | DNA helicase RecQ (EC 5.6.2.4) |
| [x] | `pcnB` | PP_4697 | Q88DX1 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Poly(A) polymerase I (PAP I) (EC 2.7.7.19) |
| [x] | `pnp` | PP_4708 | Q88DW0 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Polyribonucleotide nucleotidyltransferase (EC 2.7.7.8) (Polynucleotide phosphorylase) (PNPase) |
| [x] | `dnaK` | PP_4727 | Q88DU2 | kegg:ppu04156 | PRESENT | CURATED | PRESENT | Chaperone protein DnaK (HSP70) (Heat shock 70 kDa protein) (Heat shock protein 70) |
| [x] | `rhlE-I` | PP_4766 | Q88DQ7 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | DEAD-box ATP-dependent RNA helicase RhpA (EC 3.6.4.13) |
| [x] | `rnr` | PP_4880 | Q88DE6 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Ribonuclease R (RNase R) (EC 3.1.13.1) |
| [x] | `hfq` | PP_4894 | Q88DD3 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | RNA-binding protein Hfq |
| [x] | `rhlE` | PP_4980 | Q88D48 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | ATP-dependent RNA helicase RhlE (EC 3.6.4.13) |
| [x] | `rppH` | PP_5146 | Q88CN4 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | RNA pyrophosphohydrolase (EC 3.6.1.-) ((Di)nucleoside polyphosphate hydrolase) |
| [x] | `rho` | PP_5214 | Q88CG7 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Transcription termination factor Rho (EC 3.6.4.-) (ATP-dependent helicase Rho) |
| [x] | `ppk` | PP_5217 | Q88CG4 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate phosphotransferase) (Polyphosphoric acid kinase) |

## Notes

Generated UTC: 2026-07-09T10:33:33.412605+00:00

2026-07-09 PDT checkpoint: 17/17 review folders, 17/17 curated review YAMLs,
and 17/17 Asta gene-level reports are present. The module was created and
validated as `modules/bacterial_rna_degradation.yaml`.

2026-07-11 PDT status sync: re-ran both module validators for
`modules/bacterial_rna_degradation.yaml`; `linkml-validate -C ModuleReview`
and the module term-label validator both pass. The Falcon boxes remain
unchecked because the real Edison requests below failed with HTTP 402 and no
Falcon report files were written.

Falcon retrieval was attempted with the real commands:

```bash
just module-deep-research-falcon bacterial_rna_degradation
just module-pathway-deep-research-falcon bacterial_rna_degradation ppu03018 PSEPK
```

Both failed immediately at Edison task creation with HTTP 402, so no Falcon
output artifacts were written.
