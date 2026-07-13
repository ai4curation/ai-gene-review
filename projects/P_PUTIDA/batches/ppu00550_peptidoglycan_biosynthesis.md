---
title: "PSEPK ppu00550 Peptidoglycan biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00550: Peptidoglycan biosynthesis

- Module seed: `peptidoglycan_biosynthesis`
- Candidate genes from membership table: 24
- Primary bucket genes: 10
- Existing review files: 24
- Curated review files: 24
- Existing Asta research files: 24

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
| [x] | `pbpC` | PP_0572 | Q88QC2 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | peptidoglycan glycosyltransferase (EC 2.4.99.28) |
| [x] | `murJ` | PP_0601 | Q88Q94 | unipathway:UPA00219 | PRESENT | CURATED | PRESENT | Probable lipid II flippase MurJ |
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
| [x] | `uppS` | PP_1595 | Q88MH6 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis |
| [x] | `murB` | PP_1904 | Q88LM5 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98) (UDP-N-acetylmuramate dehydrogenase) |
| [x] | `dacB` | PP_2098 | Q88L37 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | D-alanyl-D-alanine carboxypeptidase |
| [x] | `uppP` | PP_2862 | Q88IY7 | kegg:ppu00552 | PRESENT | CURATED | PRESENT | Undecaprenyl-diphosphatase (EC 3.6.1.27) (Bacitracin resistance protein) (Undecaprenyl pyrophosphate phosphatase) |
| [x] | `mrdA-I` | PP_3741 | Q88GI2 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) |
| [x] | `ddlA` | PP_4346 | Q88EV6 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A) |
| [x] | `mrcB` | PP_4683 | Q88DY5 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | Penicillin-binding protein 1B (PBP-1b) (PBP1b) (Murein polymerase) |
| [x] | `dacA` | PP_4803 | Q88DM2 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | serine-type D-Ala-D-Ala carboxypeptidase (EC 3.4.16.4) |
| [x] | `mrdB` | PP_4806 | Q88DL9 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | Peptidoglycan glycosyltransferase MrdB (PGT) (EC 2.4.99.28) (Cell elongation protein RodA) (Cell wall polymerase) (Pepti |
| [x] | `mrdA-II` | PP_4807 | Q88DL8 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) |
| [x] | `mrcA` | PP_5084 | Q88CU6 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Penicillin-binding protein 1A (EC 2.4.99.28) (EC 3.4.16.4) |
| [x] | `mtgA` | PP_5107 | Q88CS3 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | Biosynthetic peptidoglycan transglycosylase (EC 2.4.99.28) (Glycan polymerase) (Peptidoglycan glycosyltransferase MtgA)  |

## Notes

Generated UTC: 2026-07-08T10:16:06.489745+00:00

Completed first-pass curation on 2026-07-08 UTC.

Main conclusions:

- The 24-gene batch covers cytosolic UDP-MurNAc-peptide assembly (`murA`,
  `murB`, `murC`, `murD`, `murE`, `murF`, `ddlA`, `ddlB`), lipid-carrier and
  lipid-linked precursor assembly/recycling (`uppS`, `uppP`, `mraY`, `murG`),
  lipid II flipping (`murJ`), SEDS-family glycan polymerization (`ftsW`,
  `mrdB`), class A PBPs/glycosyltransferases (`mrcA`, `mrcB`, `pbpC`, `mtgA`),
  class B PBPs/transpeptidases (`ftsI`, `mrdA-I`, `mrdA-II`), and
  carboxypeptidase/remodeling side nodes (`dacA`, `dacB`).
- `murJ` was promoted from UniPathway UPA00219 because lipid II flipping is an
  expected peptidoglycan step but is absent from the KEGG `ppu00550` membership.
- SEDS proteins `ftsW` and `mrdB` were curated as peptidoglycan polymerases, not
  lipid-linked peptidoglycan transporters; their TreeGrafter/GOC transport
  annotations were removed.
- Class B PBPs `ftsI`, `mrdA-I`, and `mrdA-II` were kept as
  D,D-transpeptidase/carboxypeptidase-family enzymes. The `ftsI`
  glycosyltransferase row and the MrdA L,D-transpeptidase rows were removed as
  over-propagated computational assignments.
- `uppP` received a first-pass `NEW` peptidoglycan biosynthetic process lead
  from UniProt because the local GOA block only carried the phosphatase,
  localization, and antibiotic-response annotations.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon peptidoglycan_biosynthesis`
  and `just module-pathway-deep-research-falcon peptidoglycan_biosynthesis ppu00550 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/peptidoglycan_biosynthesis-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__ppu00550-deep-research-falcon.md`.
