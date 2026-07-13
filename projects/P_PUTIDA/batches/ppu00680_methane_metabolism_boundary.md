---
title: "PSEPK ppu00680 Methane metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00680: Methane metabolism

- Module seed: `methane_metabolism_boundary`
- Candidate genes from membership table: 30
- Primary bucket genes: 18
- Existing review files: 30
- Curated review files: 30
- Existing Asta research files: 30

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
| [x] | `glyA1` | PP_0322 | Q88R12 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) |
| [x] | `fdhA` | PP_0328 | Q88R06 | kegg:ppu00625 | PRESENT | CURATED | PRESENT | Formaldehyde dehydrogenase (EC 1.2.1.46) |
| [x] | `fdoG` | PP_0489 | A0A140FVZ1 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase-O major subunit (EC 1.2.1.2) |
| [x] | `fdoH` | PP_0490 | Q88QK1 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase iron-sulfur subunit |
| [x] | `fdoI` | PP_0491 | Q88QK0 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase-O, gamma subunit (EC 1.2.1.2) |
| [x] | `mdh` | PP_0654 | Q88Q44 | kegg:ppu00566 | PRESENT | CURATED | PRESENT | Probable malate dehydrogenase (EC 1.1.1.37) |
| [x] | `glyA2` | PP_0671 | Q88Q27 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) |
| [x] | `hprA` | PP_0762 | Q88PT6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Glycerate dehydrogenase |
| [x] | `pta` | PP_0774 | Q88PS4 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) |
| [x] | `ppc` | PP_1505 | Q88MR4 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC 4.1.1.31) |
| [x] | `eno` | PP_1612 | Q88MF9 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase) (2-phosphoglycerate dehydratase) |
| [x] | `frmA` | PP_1616 | Q88MF5 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrog |
| [x] | `frmC` | PP_1617 | Q88MF4 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | S-formylglutathione hydrolase (EC 3.1.2.12) |
| [x] | `serC` | PP_1768 | Q88M07 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) |
| [x] | `ppsA` | PP_2082 | Q88L53 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2) (Pyruvate, water dikinase) |
| [x] | `PP_2183` | PP_2183 | Q88KV6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase I subunit E) (NDH-1 subunit E) |
| [x] | `PP_2184` | PP_2184 | Q88KV5 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit F (NADH dehydrogenase I subunit F) (NDH-1 subunit F) |
| [x] | `PP_2185` | PP_2185 | Q88KV4 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase, alpha subunit |
| [x] | `PP_2186` | PP_2186 | Q88KV3 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase, delta subunit |
| [x] | `PP_2213` | PP_2213 | Q88KS6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acyl-CoA synthetase (EC 6.2.1.-) |
| [x] | `PP_2533` | PP_2533 | Q88JW4 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | D-isomer specific 2-hydroxyacid dehydrogenase family protein |
| [x] | `ttuD` | PP_4300 | Q88F00 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Hydroxypyruvate reductase (EC 1.1.1.81) |
| [x] | `acsA1` | PP_4487 | Q88EH6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme |
| [x] | `acsA2` | PP_4702 | Q88DW6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme |
| [x] | `serB` | PP_4909 | Q88DB8 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Phosphoserine phosphatase (EC 3.1.3.3) (O-phosphoserine phosphohydrolase) |
| [x] | `fba` | PP_4960 | Q88D67 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) |
| [x] | `fbp` | PP_5040 | Q88CY9 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class |
| [x] | `gpmI` | PP_5056 | Q88CX4 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | 2,3-bisphosphoglycerate-independent phosphoglycerate mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4 |
| [x] | `serA` | PP_5155 | Q88CM5 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC 1.1.1.95) (2-oxoglutarate reductase) |
| [x] | `peaA` | PP_5602 | A0A140FWF3 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Quinohaemoprotein amine dehydrogenase, alpha subunit (EC 1.4.9.1, EC 1.4.99.-) |

## Notes

Generated UTC: 2026-07-08T14:32:09.859404+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon methane_metabolism_boundary`
  and `just module-pathway-deep-research-falcon methane_metabolism_boundary ppu00680 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/methane_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__methane_metabolism_boundary__ppu00680-deep-research-falcon.md`.
