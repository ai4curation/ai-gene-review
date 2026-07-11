---
title: "PSEPK UPA00219 UniPathway UPA00219 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00219: UniPathway UPA00219

- Module seed: `peptidoglycan_biosynthesis`
- Candidate genes from membership table: 25
- Primary bucket genes: 3
- Existing review files: 25
- Curated review files: 25
- Existing Asta research files: 25

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `pbpC` | PP_0572 | Q88QC2 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | peptidoglycan glycosyltransferase (EC 2.4.99.28) |
| [x] | `murJ` | PP_0601 | Q88Q94 | unipathway:UPA00219 | PRESENT | CURATED | PRESENT | Probable lipid II flippase MurJ |
| [x] | `murI` | PP_0736 | Q88PW2 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Glutamate racemase (EC 5.1.1.3) |
| [x] | `murA` | PP_0964 | Q88P88 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC 2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enol |
| [x] | `ftsI` | PP_1331 | Q88N82 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase FtsI (EC 3.4.16.4) (Penicillin-binding protein 3) (PBP-3) |
| [x] | `murE` | PP_1332 | Q88N81 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diam |
| [x] | `murF` | PP_1333 | Q88N80 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) |
| [x] | `mraY` | PP_1334 | Q88N79 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | Phospho-N-acetylmuramoyl-pentapeptide-transferase (EC 2.7.8.13) (UDP-MurNAc-pentapeptide phosphotransferase) |
| [x] | `murD` | PP_1335 | Q88N78 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC 6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-ala |
| [x] | `ftsW` | PP_1336 | Q88N77 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | Probable peptidoglycan glycosyltransferase FtsW (PGT) (EC 2.4.99.28) (Cell division protein FtsW) (Cell wall polymerase) |
| [x] | `murG` | PP_1337 | Q88N76 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol N-acetylglucosamine transferase (EC  |
| [x] | `murC` | PP_1338 | Q88N75 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramate--L-alanine ligase (EC 6.3.2.8) (UDP-N-acetylmuramoyl-L-alanine synthetase) |
| [x] | `ddlB` | PP_1339 | Q88N74 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala ligase B) (D-alanylalanine synthetase B) |
| [x] | `PP_1451` | PP_1451 | Q88MW7 | unipathway:UPA00219 | PRESENT | CURATED | PRESENT | L,D-TPase catalytic domain-containing protein |
| [x] | `murB` | PP_1904 | Q88LM5 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98) (UDP-N-acetylmuramate dehydrogenase) |
| [x] | `PP_2320` | PP_2320 | Q88KH0 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | L,D-TPase catalytic domain-containing protein |
| [x] | `mrdA-I` | PP_3741 | Q88GI2 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) |
| [x] | `ddlA` | PP_4346 | Q88EV6 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A) |
| [x] | `mrcB` | PP_4683 | Q88DY5 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | Penicillin-binding protein 1B (PBP-1b) (PBP1b) (Murein polymerase) |
| [x] | `dacA` | PP_4803 | Q88DM2 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | serine-type D-Ala-D-Ala carboxypeptidase (EC 3.4.16.4) |
| [x] | `mrdB` | PP_4806 | Q88DL9 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | Peptidoglycan glycosyltransferase MrdB (PGT) (EC 2.4.99.28) (Cell elongation protein RodA) (Cell wall polymerase) (Pepti |
| [x] | `mrdA-II` | PP_4807 | Q88DL8 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) |
| [x] | `mrcA` | PP_5084 | Q88CU6 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Penicillin-binding protein 1A (EC 2.4.99.28) (EC 3.4.16.4) |
| [x] | `mtgA` | PP_5107 | Q88CS3 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | Biosynthetic peptidoglycan transglycosylase (EC 2.4.99.28) (Glycan polymerase) (Peptidoglycan glycosyltransferase MtgA)  |
| [x] | `ddl` | PP_5673 | A0A140FWM5 | unipathway:UPA00219 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase (EC 6.3.2.4) (D-Ala-D-Ala ligase) (D-alanylalanine synthetase) |

## Notes

Generated UTC: 2026-07-10T02:28:40.306578+00:00

Session update:

- UPA00219 is treated as the broad UniPathway peptidoglycan-biosynthesis route view inside the existing `peptidoglycan_biosynthesis` module.
- `PP_1451` and `ddl` were the two missing review folders; both were fetched, Asta-retrieved, curated, and validated.
- `PP_1451` is curated as a predicted signal-peptide-bearing YkuD/L,D-transpeptidase-family peptidoglycan remodeling candidate.
- `ddl` is curated as a cytoplasmic D-alanine-D-alanine ligase paralog, distinct from already curated `ddlA` and `ddlB`.
- `modules/peptidoglycan_biosynthesis.yaml` now records the UPA00219-specific `ddl` paralog and the `PP_1451`/`PP_2320` L,D-transpeptidase-family remodeling candidates.
- Module validation and `just validate PSEPK PP_1451` / `just validate PSEPK ddl` pass. Both new gene validations have only the expected Asta-not-cited warning because Asta was used for identity retrieval, not as curation-changing evidence.
- The generic peptidoglycan Falcon report remains absent after the earlier real `just module-deep-research-falcon peptidoglycan_biosynthesis` run failed with Edison HTTP 402.
- The real pathway-specific Falcon command was run for `peptidoglycan_biosynthesis UPA00219 PSEPK`; Edison returned `402 Payment Required`, so no `projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00219-deep-research-falcon.md` report was produced.
