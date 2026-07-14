---
title: "PSEPK ppu00010 Glycolysis / Gluconeogenesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00010: Glycolysis / Gluconeogenesis

- Module seed: `entner_doudoroff_and_gluconeogenesis`
- Candidate genes from membership table: 38
- Supplemental hole-fill genes: 4
- Selected genes in batch: 42
- Primary bucket genes: 5
- Existing review files: 42
- Curated review files: 42
- Existing gene-level research/notes: 42 (38 Asta; 3 Falcon; 1 manual notes after OpenScientist timeout)

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for original KEGG-selected genes.
- [x] Use existing Falcon/manual notes for supplemental ED hole-fill genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Selection | Primary bucket | Existing review | Curation | Research | Protein |
|---|---|---|---|---|---|---|---|---|---|
| [x] | `aceF` | PP_0338 | Q88QZ6 | KEGG | kegg:ppu00785 | PRESENT | CURATED | PRESENT (asta) | Acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) |
| [x] | `aceE` | PP_0339 | Q88QZ5 | KEGG | kegg:ppu00785 | PRESENT | CURATED | PRESENT (asta) | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) |
| [x] | `aldB-I` | PP_0545 | Q88QE9 | KEGG | kegg:ppu00010 | PRESENT | CURATED | PRESENT (asta) | Aldehyde dehydrogenase (EC 1.2.1.3) |
| [x] | `acoC` | PP_0553 | Q88QE1 | KEGG | kegg:ppu00785 | PRESENT | CURATED | PRESENT (asta) | Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system (EC 2.3.1.12) |
| [x] | `gapA` | PP_1009 | Q88P44 | KEGG | kegg:ppu00710 | PRESENT | CURATED | PRESENT (asta) | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.-) |
| [x] | `edd` | PP_1010 | Q88P43 | hole-fill | kegg:ppu00030 | PRESENT | CURATED | PRESENT (falcon) | Phosphogluconate dehydratase (EC 4.2.1.12) |
| [x] | `glk` | PP_1011 | Q88P42 | KEGG | kegg:ppu00052 | PRESENT | CURATED | PRESENT (asta) | Glucokinase (EC 2.7.1.2) (Glucose kinase) |
| [x] | `zwfA` | PP_1022 | Q88P31 | hole-fill | kegg:ppu00480 | PRESENT | CURATED | MANUAL_NOTES (manual_after_openscientist_timeout) | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) |
| [x] | `pgl` | PP_1023 | Q88P30 | hole-fill | kegg:ppu00030 | PRESENT | CURATED | PRESENT (falcon) | 6-phosphogluconolactonase (6PGL) (EC 3.1.1.31) |
| [x] | `eda` | PP_1024 | Q88P29 | hole-fill | kegg:ppu00030 | PRESENT | CURATED | PRESENT (falcon) | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) |
| [x] | `PP_1165` | PP_1165 | Q88NP2 | KEGG | kegg:ppu00052 | PRESENT | CURATED | PRESENT (asta) | Aldose 1-epimerase |
| [x] | `pykA` | PP_1362 | Q88N54 | KEGG | kegg:ppu00010 | PRESENT | CURATED | PRESENT (asta) | Pyruvate kinase (EC 2.7.1.40) |
| [x] | `eno` | PP_1612 | Q88MF9 | KEGG | kegg:ppu03018 | PRESENT | CURATED | PRESENT (asta) | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase) (2-phosphoglycerate dehydratase) |
| [x] | `frmA` | PP_1616 | Q88MF5 | KEGG | kegg:ppu00626 | PRESENT | CURATED | PRESENT (asta) | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | KEGG | kegg:ppu00052 | PRESENT | CURATED | PRESENT (asta) | phosphomannomutase (EC 5.4.2.8) |
| [x] | `pgi1` | PP_1808 | Q88LW9 | KEGG | kegg:ppu00500 | PRESENT | CURATED | PRESENT (asta) | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) |
| [x] | `ppsA` | PP_2082 | Q88L53 | KEGG | kegg:ppu00680 | PRESENT | CURATED | PRESENT (asta) | Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2) (Pyruvate, water dikinase) |
| [x] | `gapB` | PP_2149 | Q88KZ0 | KEGG | kegg:ppu00710 | PRESENT | CURATED | PRESENT (asta) | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.-) |
| [x] | `PP_2213` | PP_2213 | Q88KS6 | KEGG | kegg:ppu00680 | PRESENT | CURATED | PRESENT (asta) | Acyl-CoA synthetase (EC 6.2.1.-) |
| [x] | `calA` | PP_2426 | Q88K65 | KEGG | kegg:ppu00561 | PRESENT | CURATED | PRESENT (asta) | Coniferyl alcohol dehydrogenase (EC 1.1.1.194) |
| [x] | `pedE` | PP_2674 | Q88JH5 | KEGG | kegg:ppu00625 | PRESENT | CURATED | PRESENT (asta) | Quinoprotein alcohol dehydrogenase PedE (EC 1.1.2.8) (Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Ca(2+)-dependent PQQ-ADH) |
| [x] | `pedH` | PP_2679 | Q88JH0 | KEGG | kegg:ppu00625 | PRESENT | CURATED | PRESENT (asta) | Quinoprotein alcohol dehydrogenase PedH (EC 1.1.2.-) (Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Lanthanide-dependent PQQ-ADH) |
| [x] | `aldB-II` | PP_2680 | Q88JG9 | KEGG | kegg:ppu00010 | PRESENT | CURATED | PRESENT (asta) | Aldehyde dehydrogenase (EC 1.2.1.3) |
| [x] | `PP_3382` | PP_3382 | Q88HH6 | KEGG | kegg:ppu00030 | PRESENT | CURATED | PRESENT (asta) | Gluconate 2-dehydrogenase cytochrome c subunit (EC 1.1.99.3) |
| [x] | `PP_3443` | PP_3443 | Q88HB7 | KEGG | kegg:ppu00030 | PRESENT | CURATED | PRESENT (asta) | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.59) |
| [x] | `pgm` | PP_3578 | Q88GY7 | KEGG | kegg:ppu00052 | PRESENT | CURATED | PRESENT (asta) | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `adhB` | PP_3623 | Q88GU4 | KEGG | kegg:ppu00030 | PRESENT | CURATED | PRESENT (asta) | Alcohol dehydrogenase cytochrome c subunit |
| [x] | `adhP` | PP_3839 | Q88G86 | KEGG | kegg:ppu00626 | PRESENT | CURATED | PRESENT (asta) | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | KEGG | kegg:ppu00785 | PRESENT | CURATED | PRESENT (asta) | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `pyk` | PP_4301 | Q88EZ9 | KEGG | kegg:ppu00010 | PRESENT | CURATED | PRESENT (asta) | Pyruvate kinase (EC 2.7.1.40) |
| [x] | `lpdV` | PP_4404 | Q88EP9 | KEGG | kegg:ppu00785 | PRESENT | CURATED | PRESENT (asta) | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `acsA1` | PP_4487 | Q88EH6 | KEGG | kegg:ppu00680 | PRESENT | CURATED | PRESENT (asta) | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) |
| [x] | `pgi2` | PP_4701 | Q88DW7 | KEGG | kegg:ppu00500 | PRESENT | CURATED | PRESENT (asta) | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) |
| [x] | `acsA2` | PP_4702 | Q88DW6 | KEGG | kegg:ppu00680 | PRESENT | CURATED | PRESENT (asta) | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) |
| [x] | `tpiA` | PP_4715 | Q88DV4 | KEGG | kegg:ppu00562 | PRESENT | CURATED | PRESENT (asta) | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase) |
| [x] | `fba` | PP_4960 | Q88D67 | KEGG | kegg:ppu00710 | PRESENT | CURATED | PRESENT (asta) | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) |
| [x] | `pgk` | PP_4963 | Q88D64 | KEGG | kegg:ppu00710 | PRESENT | CURATED | PRESENT (asta) | Phosphoglycerate kinase (EC 2.7.2.3) |
| [x] | `fbp` | PP_5040 | Q88CY9 | KEGG | kegg:ppu00710 | PRESENT | CURATED | PRESENT (asta) | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) |
| [x] | `gpmI` | PP_5056 | Q88CX4 | KEGG | kegg:ppu00680 | PRESENT | CURATED | PRESENT (asta) | 2,3-bisphosphoglycerate-independent phosphoglycerate mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4.2.12) |
| [x] | `algC` | PP_5288 | Q88C93 | KEGG | kegg:ppu00052 | PRESENT | CURATED | PRESENT (asta) | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |
| [x] | `PP_5332` | PP_5332 | Q88C51 | KEGG | kegg:ppu00010 | PRESENT | CURATED | PRESENT (asta) | Putative glucose-6-phosphate 1-epimerase (EC 5.1.3.15) |
| [x] | `lpd` | PP_5366 | Q88C17 | KEGG | kegg:ppu00785 | PRESENT | CURATED | PRESENT (asta) | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-06T12:45:16.735745+00:00

## Curation Notes

- Falcon supports modeling KT2440 central glucose metabolism as an
  Entner-Doudoroff/EMP/gluconeogenesis module rather than canonical forward EMP
  glycolysis.
- KEGG `ppu00010` is not sufficient by itself for pathway satisfiability. The
  core ED branch also needs `edd`, `zwfA`, `pgl`, and `eda`, which are present in
  PSEPK but assigned through neighboring pathway buckets. These four genes are
  now included as explicit `MODULE_HOLE_FILL` rows in this batch.
- The 38-gene candidate set includes real central-carbon steps plus KEGG
  spillover from pyruvate dehydrogenase, acetyl-CoA synthetase, aldehyde/alcohol
  dehydrogenases, phosphosugar mutases/epimerases, and periplasmic glucose
  oxidation. These peripheral genes were curated at first-pass depth, but should
  not all be promoted to core members of the ED/gluconeogenesis module.
- Asta retrieval reports are present for all 38 original KEGG-selected genes.
  The supplemental hole-fill rows use existing Falcon reports for `edd`, `eda`,
  and `pgl`; `zwfA` uses curated manual notes because OpenScientist timed out
  before writing an output file.
- For many generic enzyme symbols, the useful first-pass support still came from
  UniProt, GOA, EC/InterPro family context, and the module-level Falcon synthesis
  rather than gene-specific Asta hypotheses.
