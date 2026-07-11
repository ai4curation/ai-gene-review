---
title: "PSEPK ppu00770 Pantothenate and CoA biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00770: Pantothenate and CoA biosynthesis

- Module seed: `pantothenate_and_coa_biosynthesis`
- Candidate genes from membership table: 24
- Primary bucket genes: 10
- Existing review files: 24
- Curated review files: 24
- Existing Asta research files: 24

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `coaX` | PP_0438 | Q88QQ0 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Type III pantothenate kinase (EC 2.7.1.33) (PanK-III) (Pantothenic acid kinase) |
| [x] | `PP_0614` | PP_0614 | Q88Q81 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) |
| [x] | `coaE` | PP_0631 | Q88Q65 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Dephospho-CoA kinase (EC 2.7.1.24) (Dephosphocoenzyme A kinase) |
| [x] | `PP_0922` | PP_0922 | Q88PC8 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | ACP phosphodiesterase |
| [x] | `PP_1157` | PP_1157 | Q877U6 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase |
| [x] | `PP_1183` | PP_1183 | Q88NM4 | kegg:ppu00074 | PRESENT | CURATED | PRESENT | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) |
| [x] | `panE` | PP_1351 | Q88N64 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) |
| [x] | `PP_1394` | PP_1394 | Q88N22 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase, large subunit |
| [x] | `mazG` | PP_1657 | Q88MB7 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) |
| [x] | `PP_2325` | PP_2325 | Q88KG5 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) |
| [x] | `PP_2998` | PP_2998 | Q88IK1 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) |
| [x] | `ilvE` | PP_3511 | Q88H54 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) |
| [x] | `hyuC` | PP_4034 | Q88FQ3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) |
| [x] | `pydB` | PP_4036 | A0A140FWK2 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) |
| [x] | `pydX` | PP_4037 | Q88FQ1 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [x] | `pydA` | PP_4038 | Q88FQ0 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [x] | `ilvC` | PP_4678 | Q88DZ0 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86) (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta- |
| [x] | `ilvH` | PP_4679 | Q88DY9 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) |
| [x] | `ilvI` | PP_4680 | Q88DY8 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase (EC 2.2.1.6) |
| [x] | `panB` | PP_4699 | Q88DW9 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 3-methyl-2-oxobutanoate hydroxymethyltransferase (EC 2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT) |
| [x] | `panC` | PP_4700 | Q88DW8 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme) |
| [x] | `coaD` | PP_5123 | Q88CQ7 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Phosphopantetheine adenylyltransferase (EC 2.7.7.3) (Dephospho-CoA pyrophosphorylase) (Pantetheine-phosphate adenylyltra |
| [x] | `ilvD` | PP_5128 | Q88CQ2 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) |
| [x] | `dfp` | PP_5285 | Q88C96 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Coenzyme A biosynthesis bifunctional protein CoaBC (DNA/pantothenate metabolism flavoprotein) (Phosphopantothenoylcystei |

## Notes

- Module and pathway/taxon Falcon reports are complete. PP_2325, PP_2998, and
  UniPathway-only PP_4452 remain candidate-uncertain ketopantoate reductase
  paralogs rather than accepted core enzymes.

Generated UTC: 2026-07-07T12:18:09.651403+00:00
