---
title: "PSEPK ppu00260 Glycine, serine and threonine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00260: Glycine, serine and threonine metabolism

- Module seed: `glycine_serine_threonine_metabolism`
- Candidate genes from membership table: 66
- Primary bucket genes: 16
- Existing review files: 66
- Curated review files: 66
- Existing Asta research files: 66

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
| [x] | `trpA` | PP_0082 | Q88RP7 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Tryptophan synthase alpha chain (EC 4.2.1.20) |
| [x] | `trpB` | PP_0083 | Q88RP6 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Tryptophan synthase beta chain (EC 4.2.1.20) |
| [x] | `thrB` | PP_0121 | Q88RK8 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Homoserine kinase (HK) (HSK) (EC 2.7.1.39) |
| [x] | `tdcG-I` | PP_0297 | Q88R37 | kegg:ppu00270 | PRESENT | CURATED | PRESENT | L-serine dehydratase (EC 4.3.1.17) |
| [x] | `dgcA` | PP_0310 | Q88R24 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Dimethylglycine dehydrogenase subunit (EC 1.5.8.-) |
| [x] | `dgcB` | PP_0311 | Q88R23 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Dimethylglycine dehydrogenase subunit (EC 1.5.8.-) |
| [x] | `PP_0312` | PP_0312 | Q88R22 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Electron transfer flavoprotein, alpha subunit |
| [x] | `PP_0313` | PP_0313 | Q88R21 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Electron transfer flavoprotein beta subunit |
| [x] | `gbcA` | PP_0315 | Q88R19 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Glycine-betaine dioxygenase subunit (EC 1.13.-.-) |
| [x] | `gbcB` | PP_0316 | Q88R18 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Glycine-betaine dioxygenase subunit (EC 1.13.-.-) |
| [x] | `ltaE` | PP_0321 | Q88R13 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | L-threonine aldolase (EC 4.1.2.48) |
| [x] | `glyA1` | PP_0322 | Q88R12 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) |
| [x] | `soxB` | PP_0323 | Q88R11 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Sarcosine oxidase subunit beta (EC 1.5.3.24) (Sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) subunit beta) ( |
| [x] | `soxD` | PP_0324 | Q88R10 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Sarcosine oxidase subunit delta (EC 1.5.3.1) |
| [x] | `soxA` | PP_0325 | Q88R09 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Sarcosine oxidase subunit alpha (EC 1.5.3.1) |
| [x] | `soxG` | PP_0326 | Q88R08 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Sarcosine oxidase subunit gamma (EC 1.5.3.1) |
| [x] | `PP_0488` | PP_0488 | Q88QK2 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | NADP-dependent dehydrogenase HI_1430 (EC 1.1.1.-) |
| [x] | `PP_0662` | PP_0662 | Q88Q36 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Threonine synthase |
| [x] | `PP_0664` | PP_0664 | Q88Q34 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | homoserine dehydrogenase (EC 1.1.1.3) |
| [x] | `glyA2` | PP_0671 | Q88Q27 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) |
| [x] | `PP_0708` | PP_0708 | Q88PZ0 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Betaine-aldehyde dehydrogenase |
| [x] | `pcs` | PP_0731 | Q88PW7 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphatidylcholine synthase (EC 2.7.8.24) |
| [x] | `hprA` | PP_0762 | Q88PT6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Glycerate dehydrogenase |
| [x] | `gcvT-I` | PP_0986 | Q88P67 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `tdcG-II` | PP_0987 | Q88P66 | kegg:ppu00270 | PRESENT | CURATED | PRESENT | L-serine dehydratase (EC 4.3.1.17) |
| [x] | `gcvP1` | PP_0988 | Q88P65 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) ( |
| [x] | `gcvH1` | PP_0989 | Q88P64 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 1 |
| [x] | `ghrB` | PP_1261 | Q88NF1 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) |
| [x] | `hom` | PP_1470 | Q88MU8 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Homoserine dehydrogenase (EC 1.1.1.3) |
| [x] | `thrC` | PP_1471 | Q88MU7 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Threonine synthase (EC 4.2.3.1) |
| [x] | `serC` | PP_1768 | Q88M07 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) |
| [x] | `asd__Q88LE4` | PP_1989 | Q88LE4 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase) (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenas |
| [x] | `PP_2533` | PP_2533 | Q88JW4 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | D-isomer specific 2-hydroxyacid dehydrogenase family protein |
| [x] | `PP_2800` | PP_2800 | Q88J49 | kegg:ppu00975 | PRESENT | CURATED | PRESENT | Diaminobutyrate-2-oxoglutarate transaminase |
| [x] | `PP_2930` | PP_2930 | Q88IR9 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | L-serine ammonia-lyase (EC 4.3.1.17) |
| [x] | `tdcG-III` | PP_3144 | Q88I57 | kegg:ppu00270 | PRESENT | CURATED | PRESENT | L-serine dehydratase (EC 4.3.1.17) |
| [x] | `garK` | PP_3178 | Q88I24 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerate kinase (EC 2.7.1.165) |
| [x] | `PP_3191` | PP_3191 | Q88I11 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Threonine ammonia-lyase / dehydratase (EC 4.3.1.19) |
| [x] | `ilvA-I` | PP_3446 | Q88HB4 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) |
| [x] | `pssA` | PP_3664 | Q88GQ4 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) |
| [x] | `creA` | PP_3667 | Q88GQ1 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Creatinase (EC 3.5.3.3) |
| [x] | `alr` | PP_3722 | Q88GJ9 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Broad specificity amino-acid racemase (EC 5.1.1.10) (Broad spectrum racemase) |
| [x] | `PP_3775` | PP_3775 | Q88GE9 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Sarcosine oxidase (EC 1.5.3.1) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `pvdH` | PP_4223 | Q88F75 | kegg:ppu00975 | PRESENT | CURATED | PRESENT | Diaminobutyrate-2-oxoglutarate transaminase (EC 2.6.1.76) |
| [x] | `ttuD` | PP_4300 | Q88F00 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Hydroxypyruvate reductase (EC 1.1.1.81) |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `PP_4421` | PP_4421 | Q88EN3 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `PP_4423` | PP_4423 | Q88EN1 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Succinylglutamate desuccinylase/Aspartoacylase catalytic domain-containing protein |
| [x] | `PP_4430` | PP_4430 | Q88EM4 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Threonine dehydratase (EC 4.3.1.19) |
| [x] | `PP_4432` | PP_4432 | Q88EM2 | kegg:ppu00260 | PRESENT | CURATED | PRESENT | Xaa-Pro aminopeptidase |
| [x] | `PP_4473` | PP_4473 | Q88EI9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) |
| [x] | `PP_4594` | PP_4594 | Q88E72 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine gamma-synthase |
| [x] | `PP_4677` | PP_4677 | Q88DZ1 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (Phosphatidylserine synthase) |
| [x] | `ydfG` | PP_4862 | Q88DG3 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | 3-hydroxy acid dehydrogenase, NADP-dependent / malonic semialdehyde reductase (EC 1.1.1.276, EC 1.1.1.298) |
| [x] | `serB` | PP_4909 | Q88DB8 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Phosphoserine phosphatase (EC 3.1.3.3) (O-phosphoserine phosphohydrolase) |
| [x] | `PP_4983` | PP_4983 | Q88D45 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Tryptophan 2-monooxygenase (EC 1.13.12.3) |
| [x] | `gpmI` | PP_5056 | Q88CX4 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | 2,3-bisphosphoglycerate-independent phosphoglycerate mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4 |
| [x] | `betB` | PP_5063 | Q88CW7 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8) |
| [x] | `betA` | PP_5064 | Q88CW6 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Oxygen-dependent choline dehydrogenase (CDH) (CHD) (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) |
| [x] | `ilvA-II` | PP_5149 | Q88CN1 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) |
| [x] | `serA` | PP_5155 | Q88CM5 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC 1.1.1.95) (2-oxoglutarate reductase) |
| [x] | `gcvP2` | PP_5192 | Q88CI9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) ( |
| [x] | `gcvH2` | PP_5193 | Q88CI8 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 2 |
| [x] | `gcvT` | PP_5194 | Q88CI7 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-07T17:48:03.392932+00:00

## Workflow Notes

- Created and validated `modules/glycine_serine_threonine_metabolism.yaml`.
- Registered `kegg:ppu00260` in `projects/P_PUTIDA/build_pathway_worklist.py`
  as the `glycine_serine_threonine_metabolism` module.
- Fetched 28 missing review folders:
  `thrB`, `dgcA`, `dgcB`, `PP_0312`, `PP_0313`, `gbcA`, `gbcB`, `ltaE`,
  `soxB`, `soxD`, `soxA`, `soxG`, `pcs`, `hprA`, `PP_2800`, `garK`,
  `PP_3191`, `ilvA-I`, `pssA`, `creA`, `PP_3775`, `PP_4421`, `PP_4423`,
  `PP_4430`, `PP_4432`, `PP_4677`, `serB`, and `ilvA-II`.
- Ran Asta for those 28 genes plus existing curated `pvdH`, which was missing
  a gene-level Asta report.
- Curated all 27 pending stubs plus `PP_4432`, which had no GOA annotations.
  `PP_4421` and `PP_4432` received provisional `NEW` first-pass annotations
  from UniProt/PANTHER identity because GOA lacked a usable activity row.
- Validated all 66 batch gene reviews and rendered all 66 gene pages.
- 2026-07-11 PDT status sync: ran the real Falcon commands:
  `just module-deep-research-falcon glycine_serine_threonine_metabolism` and
  `just module-pathway-deep-research-falcon glycine_serine_threonine_metabolism ppu00260 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/glycine_serine_threonine_metabolism-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__glycine_serine_threonine_metabolism__ppu00260-deep-research-falcon.md`.

## Curation Notes

- KEGG ppu00260 is a broad hub. The strict center includes serine biosynthesis
  (`serA`, `serC`, `serB`), homoserine/threonine biosynthesis (`hom`, `thrB`,
  `thrC`), serine-glycine one-carbon chemistry (`glyA1`, `glyA2`), glycine
  cleavage (`gcvP/H/T` clusters plus Lpd-family partners), threonine aldolase
  (`ltaE`), and sarcosine/dimethylglycine/glycine-betaine oxidation.
- The `PP_0310`-`PP_0316` cluster was curated as methylated-glycine/betaine
  catabolism context: DgcA/DgcB predicted dimethylglycine dehydrogenase
  components, PP_0312/PP_0313 ETF electron-transfer partners, and GbcA/GbcB
  predicted glycine-betaine dioxygenase subunits.
- The `soxB/soxD/soxA/soxG` cluster was treated as a tetrameric sarcosine
  oxidase system; subunit core functions use complex-contribution language
  rather than asserting that every subunit independently catalyzes the whole
  reaction.
- Boundary nodes were kept in their real primary contexts: `pcs` and
  `PP_4677` are phospholipid enzymes using serine as substrate, `pvdH` and
  `PP_2800` are diaminobutyrate/pyoverdine aminotransferase context,
  `PP_3191`/`PP_4430`/`ilvA-I`/`ilvA-II` are threonine-dehydratase family
  paralogs, and `creA` is a creatinase/guanidino-compound side node.
- The PP_4421-PP_4432 region remains substrate-uncertain. `PP_4421` is a
  class-III aminotransferase, `PP_4423` is a succinylglutamate
  desuccinylase/aspartoacylase-family hydrolase, and `PP_4432` is a predicted
  Xaa-Pro aminopeptidase. These should be revisited with deeper module-level
  evidence.
- Full-batch validation passed. Non-blocking warnings are expected Asta-context
  notices plus a few pre-existing carry-in warnings in older curated genes
  (for example unreflected cytosol/location/process terms or no-core warnings
  on some boundary reviews).
