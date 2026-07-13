---
title: "PSEPK ppu00330 Arginine and proline metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00330: Arginine and proline metabolism

- Module seed: `arginine_proline_metabolism`
- Candidate genes from membership table: 39
- Primary bucket genes: 30
- Existing review files: 39
- Curated review files: 39
- Existing Asta research files: 39

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Attempt module-level Falcon deep research; Edison returned HTTP 402 before report creation.
- [x] Attempt module + pathway + PSEPK Falcon deep research; Edison returned HTTP 402 before report creation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `aguA` | PP_0266 | Q88R68 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Agmatine deiminase (EC 3.5.3.12) (Agmatine iminohydrolase) |
| [x] | `speA` | PP_0567 | Q88QC7 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Biosynthetic arginine decarboxylase (ADC) (EC 4.1.1.19) |
| [x] | `proB` | PP_0691 | Q88Q07 | kegg:ppu00332 | PRESENT | CURATED | PRESENT | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK) |
| [x] | `speC` | PP_0864 | Q88PI6 | kegg:ppu04148 | PRESENT | CURATED | PRESENT | ornithine decarboxylase (EC 4.1.1.17) |
| [x] | `patD` | PP_1481 | Q88MT7 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC 1.2.1.54) |
| [x] | `speB` | PP_2196 | Q88KU3 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Agmatinase (EC 3.5.3.11) |
| [x] | `puuB` | PP_2448 | Q88K44 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Gamma-glutamylputrescine oxidase |
| [x] | `PP_2588` | PP_2588 | Q88JR1 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Aminotransferase, class III |
| [x] | `PP_2589` | PP_2589 | Q88JR0 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Aldehyde dehydrogenase family protein |
| [x] | `prr` | PP_2801 | Q88J48 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19) |
| [x] | `nspC` | PP_2929 | Q88IS0 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Carboxynorspermidine/carboxyspermidine decarboxylase (CANS DC/CAS DC) (CANSDC/CASDC) (EC 4.1.1.96) |
| [x] | `PP_2932` | PP_2932 | Q88IR7 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Amidase family protein |
| [x] | `PP_3146` | PP_3146 | Q88I55 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Oxidoreductase |
| [x] | `codA` | PP_3189 | Q88I13 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Cytosine deaminase / isoguanine deaminase (EC 3.5.4.-, EC 3.5.4.1) |
| [x] | `oplB` | PP_3514 | Q88H51 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | 5-oxoprolinase B (EC 3.5.2.9) |
| [x] | `oplA` | PP_3515 | Q88H50 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | 5-oxoprolinase A (EC 3.5.2.9) |
| [x] | `ocd__Q88H32` | PP_3533 | Q88H32 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Ornithine cyclodeaminase (OCD) (EC 4.3.1.12) |
| [x] | `creA` | PP_3667 | Q88GQ1 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Creatinase (EC 3.5.3.3) |
| [x] | `aruH` | PP_3721 | Q88GK0 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `aruI` | PP_3723 | A0A140FWH9 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | 2-ketoarginine decarboxylase AruI (EC 4.1.1.75) |
| [x] | `ldcC` | PP_4140 | A0A140FWL0 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Lysine decarboxylase (EC 4.1.1.18) |
| [x] | `ooxA` | PP_4456 | Q88EK6 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Opine oxidase subunit A (EC 1.-.-.-) |
| [x] | `ooxB` | PP_4457 | Q88EK5 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Opine oxidase subunit B (EC 1.-.-.-) |
| [x] | `astE` | PP_4475 | Q88EI7 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Succinylglutamate desuccinylase (EC 3.5.1.96) |
| [x] | `astB` | PP_4477 | Q88EI5 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | N-succinylarginine dihydrolase (EC 3.5.3.23) |
| [x] | `astD` | PP_4478 | Q88EI4 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | N-succinylglutamate 5-semialdehyde dehydrogenase (EC 1.2.1.71) (Succinylglutamic semialdehyde dehydrogenase) (SGSD) |
| [x] | `astA-I` | PP_4479 | Q88EI3 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Arginine N-succinyltransferase (EC 2.3.1.109) |
| [x] | `astA-II` | PP_4480 | Q88EI2 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Arginine N-succinyltransferase, subunit alpha (EC 2.3.1.109) |
| [x] | `argD` | PP_4481 | P59319 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Acetylornithine aminotransferase (ACOAT) (EC 2.6.1.11) |
| [x] | `PP_4523` | PP_4523 | Q88EE2 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Agmatinase |
| [x] | `PP_4548` | PP_4548 | Q88EB8 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Oxidoreductase |
| [x] | `proA` | PP_4811 | Q88DL4 | kegg:ppu00332 | PRESENT | CURATED | PRESENT | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialde |
| [x] | `putA` | PP_4947 | Q88D80 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Bifunctional protein PutA [Includes: Proline dehydrogenase (EC 1.5.5.2) (Proline oxidase); Delta-1-pyrroline-5-carboxyla |
| [x] | `PP_4983` | PP_4983 | Q88D45 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Tryptophan 2-monooxygenase (EC 1.13.12.3) |
| [x] | `pip` | PP_5028 | Q88D01 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Proline iminopeptidase (PIP) (EC 3.4.11.5) (Prolyl aminopeptidase) |
| [x] | `proI` | PP_5095 | Q88CT5 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Pyrroline-5-carboxylate reductase (P5C reductase) (P5CR) (EC 1.5.1.2) (PCA reductase) |
| [x] | `spuC-II` | PP_5182 | Q88CJ8 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Polyamine:pyruvate transaminase |
| [x] | `PP_5273` | PP_5273 | Q88CA8 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Oxidoreductase |
| [x] | `kauB` | PP_5278 | Q88CA3 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | 4-guanidinobutyraldehyde dehydrogenase (EC 1.2.1.54) |

## Notes

Generated UTC: 2026-07-07T20:42:17.604521+00:00

Curator notes, 2026-07-10:

- This batch is first-pass complete for gene and module curation: all 39 KEGG
  `ppu00330` membership genes have review folders, curated YAMLs with no
  remaining `PENDING` actions, and Asta gene-level reports.
- `modules/arginine_proline_metabolism.yaml` validates as the broad
  arginine/proline boundary module. It separates proline
  biosynthesis/interconversion, succinylated arginine catabolism,
  agmatine/putrescine/polyamine metabolism, 5-oxoproline/creatinine side
  chemistry, opine/2-ketoarginine context, and unresolved
  oxidoreductase/aminotransferase spillovers rather than treating KEGG
  `ppu00330` as one linear pathway.
- Real Falcon module-level research was reattempted with
  `just module-deep-research-falcon arginine_proline_metabolism`; Edison
  returned HTTP 402 before creating
  `modules/arginine_proline_metabolism-deep-research-falcon.md`.
- Real Falcon module + pathway + PSEPK research was reattempted with
  `just module-pathway-deep-research-falcon arginine_proline_metabolism ppu00330 PSEPK`;
  Edison returned HTTP 402 before creating
  `projects/P_PUTIDA/deep-research/PSEPK__arginine_proline_metabolism__ppu00330-deep-research-falcon.md`.
- Validation passed for the module with both LinkML validation and the module
  term-label validator. Focused gene-review validation remains as recorded in
  the project/module plan: no blocking errors, with only first-pass warnings
  for Asta citation coverage, generic side-node functions, the no-GOA/no-core
  `PP_2932` review, and the inherited `PP_4983` process-reflection warning.
