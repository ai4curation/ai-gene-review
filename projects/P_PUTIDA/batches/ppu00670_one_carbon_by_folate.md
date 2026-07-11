---
title: "PSEPK ppu00670 One carbon pool by folate batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00670: One carbon pool by folate

- Module seed: `one_carbon_by_folate`
- Candidate genes from membership table: 31
- Primary bucket genes: 14
- Existing review files: 31
- Curated review files: 31
- Existing Asta research files: 31

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
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
| [x] | `purU-I` | PP_0327 | Q88R07 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [x] | `glyA2` | PP_0671 | Q88Q27 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) |
| [x] | `PP_0708` | PP_0708 | Q88PZ0 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Betaine-aldehyde dehydrogenase |
| [x] | `gcvT-I` | PP_0986 | Q88P67 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `gcvP1` | PP_0988 | Q88P65 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) ( |
| [x] | `gcvH1` | PP_0989 | Q88P64 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 1 |
| [x] | `purU-II` | PP_1367 | Q88N49 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [x] | `purN` | PP_1664 | Q88MB0 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2) (5'-phosphoribosylglycinamide transformylase) (GAR transformyla |
| [x] | `purU-III` | PP_1943 | Q88LI9 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [x] | `folD1` | PP_1945 | Q88LI7 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Bifunctional protein FolD 1 [Includes: Methylenetetrahydrofolate dehydrogenase (EC 1.5.1.5); Methenyltetrahydrofolate cy |
| [x] | `folD2` | PP_2265 | Q88KM5 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Bifunctional protein FolD 2 [Includes: Methylenetetrahydrofolate dehydrogenase (EC 1.5.1.5); Methenyltetrahydrofolate cy |
| [x] | `metH` | PP_2375 | Q88KB5 | kegg:ppu04980 | PRESENT | CURATED | PRESENT | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `PP_4594` | PP_4594 | Q88E72 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine gamma-synthase |
| [x] | `folM` | PP_4632 | Q88E36 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Dihydromonapterin reductase (EC 1.5.1.3) (EC 1.5.1.50) (Dihydrofolate reductase) |
| [x] | `PP_4638` | PP_4638 | Q88E30 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Methylenetetrahydrofolate reductase |
| [x] | `purH` | PP_4822 | Q88DK3 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2 |
| [x] | `metK` | PP_4967 | Q88D60 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | S-adenosylmethionine synthase (AdoMet synthase) (EC 2.5.1.6) (MAT) (Methionine adenosyltransferase) |
| [x] | `ahcY` | PP_4976 | A0A140FWS3 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Adenosylhomocysteinase (EC 3.13.2.1) (S-adenosyl-L-homocysteine hydrolase) (AdoHcyase) |
| [x] | `metF` | PP_4977 | Q88D51 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Methylenetetrahydrofolate reductase (EC 1.5.1.54) |
| [x] | `betB` | PP_5063 | Q88CW7 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8) |
| [x] | `betA` | PP_5064 | Q88CW6 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Oxygen-dependent choline dehydrogenase (CDH) (CHD) (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) |
| [x] | `folA` | PP_5132 | Q88CP8 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Dihydrofolate reductase (EC 1.5.1.3) |
| [x] | `thyA` | PP_5141 | Q88CN9 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Thymidylate synthase (TS) (TSase) (EC 2.1.1.45) |
| [x] | `gcvP2` | PP_5192 | Q88CI9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) ( |
| [x] | `gcvH2` | PP_5193 | Q88CI8 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 2 |
| [x] | `gcvT` | PP_5194 | Q88CI7 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `fau` | PP_5203 | Q88CH8 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | 5-formyltetrahydrofolate cyclo-ligase (EC 6.3.3.2) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-07T14:32:12.546192+00:00

## Workflow Notes

- Created and validated the species-neutral module
  `modules/one_carbon_by_folate.yaml`.
- Ran `just module-deep-research-falcon one_carbon_by_folate` and
  `just module-pathway-deep-research-falcon one_carbon_by_folate ppu00670
  PSEPK`. Both reached Edison and failed at task creation with HTTP 402 Payment
  Required, so `modules/one_carbon_by_folate-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__one_carbon_by_folate__ppu00670-deep-research-falcon.md`
  were not created. Captured logs: `reports/falcon-ppu00670-module.log` and
  `reports/falcon-ppu00670-pathway.log`.
- Asta retrieval is present for all 31 genes. PP_0708, `gcvT-I`, `gcvP1`,
  `purN`, and `betA` required one retry after transient Asta service/network
  failures.
- All 31 candidate gene reviews validate with no errors. Remaining warnings are
  expected first-pass notices about Asta context not being cited as direct
  evidence, non-core location terms used in core-function location fields, and
  the intentional no-core review for PP_0708.
- Gene review pages rendered for all 31 candidates.

## Curation Notes

- Strict folate one-carbon carrier interconversion is covered by `folD1`,
  `folD2`, `metF`, PP_4638, and `fau`.
- Folate-dependent consumer reactions are represented by `purN`, `purH`,
  `thyA`, `metH`, `folA`, and `folM`.
- The two GCV clusters are kept as glycine-cleavage input to the folate C1 pool:
  `gcvT-I`/`gcvP1`/`gcvH1` and `gcvT`/`gcvP2`/`gcvH2`.
- The three `purU` paralogs are curated as formyltetrahydrofolate deformylases;
  their direct purine-biosynthesis process annotations are marked
  over-annotated.
- `betA`, `betB`, PP_0708, `lpd`/`lpdG`/`lpdV`, `metK`, `ahcY`, and PP_4594 are
  boundary nodes. PP_0708 remains unresolved because GOA currently supports only
  generic oxidoreductase activity.
