---
title: "PSEPK ppu00620 Pyruvate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00620: Pyruvate metabolism

- Module seed: `pyruvate_metabolism_boundary`
- Candidate genes from membership table: 54
- Primary bucket genes: 9
- Existing review files: 54
- Curated review files: 54
- Existing Asta research files: 54

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
| [x] | `scpC` | PP_0154 | Q88RH5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Propionyl-CoA:succinate CoA transferase (EC 2.8.3.-) |
| [x] | `aceF` | PP_0338 | Q88QZ6 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) |
| [x] | `aceE` | PP_0339 | Q88QZ5 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) |
| [x] | `glcB` | PP_0356 | Q88QX8 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | Malate synthase G (EC 2.3.3.9) |
| [x] | `aldB-I` | PP_0545 | Q88QE9 | kegg:ppu00010 | PRESENT | CURATED | PRESENT | Aldehyde dehydrogenase (EC 1.2.1.3) |
| [x] | `acoC` | PP_0553 | Q88QE1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system (EC 2.3.1.12) |
| [x] | `accC` | PP_0558 | Q88QD6 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) |
| [x] | `accB` | PP_0559 | Q88QD5 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Biotin carboxyl carrier protein of acetyl-CoA carboxylase |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `mdh` | PP_0654 | Q88Q44 | kegg:ppu00566 | PRESENT | CURATED | PRESENT | Probable malate dehydrogenase (EC 1.1.1.37) |
| [x] | `mqo1` | PP_0751 | Q88PU7 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Probable malate:quinone oxidoreductase 1 (EC 1.1.5.4) (MQO 1) (Malate dehydrogenase [quinone] 1) |
| [x] | `PP_0772` | PP_0772 | Q88PS6 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | Metallo-beta-lactamase family protein |
| [x] | `pta` | PP_0774 | Q88PS4 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) |
| [x] | `PP_0897` | PP_0897 | Q88PF3 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Fumarate hydratase class I (EC 4.2.1.2) |
| [x] | `fumC-I` | PP_0944 | Q88PA6 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) |
| [x] | `leuA` | PP_1025 | Q88P28 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | 2-isopropylmalate synthase (EC 2.3.3.13) (Alpha-IPM synthase) (Alpha-isopropylmalate synthase) |
| [x] | `mqo2` | PP_1251 | Q88NF9 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Probable malate:quinone oxidoreductase 2 (EC 1.1.5.4) (MQO 2) (Malate dehydrogenase [quinone] 2) |
| [x] | `ghrB` | PP_1261 | Q88NF1 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) |
| [x] | `pykA` | PP_1362 | Q88N54 | kegg:ppu00010 | PRESENT | CURATED | PRESENT | Pyruvate kinase (EC 2.7.1.40) |
| [x] | `PP_1389` | PP_1389 | Q88N27 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | Oxaloacetate decarboxylase (EC 4.1.1.112) |
| [x] | `ppc` | PP_1505 | Q88MR4 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC 4.1.1.31) |
| [x] | `accA` | PP_1607 | Q88MG4 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A carboxylase carboxyl transferase subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyl |
| [x] | `frmA` | PP_1616 | Q88MF5 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrog |
| [x] | `ldhA` | PP_1649 | Q88MC4 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | D-lactate dehydrogenase (EC 1.1.1.28) |
| [x] | `fumC` | PP_1755 | Q88M20 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) |
| [x] | `accD` | PP_1996 | Q88LD9 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltr |
| [x] | `ppsA` | PP_2082 | Q88L53 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2) (Pyruvate, water dikinase) |
| [x] | `PP_2213` | PP_2213 | Q88KS6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acyl-CoA synthetase (EC 6.2.1.-) |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `calA` | PP_2426 | Q88K65 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Coniferyl alcohol dehydrogenase (EC 1.1.1.194) |
| [x] | `pedE` | PP_2674 | Q88JH5 | kegg:ppu00625 | PRESENT | CURATED | PRESENT | Quinoprotein alcohol dehydrogenase PedE (EC 1.1.2.8) (Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydr |
| [x] | `pedH` | PP_2679 | Q88JH0 | kegg:ppu00625 | PRESENT | CURATED | PRESENT | Quinoprotein alcohol dehydrogenase PedH (EC 1.1.2.-) (Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol de |
| [x] | `aldB-II` | PP_2680 | Q88JG9 | kegg:ppu00010 | PRESENT | CURATED | PRESENT | Aldehyde dehydrogenase (EC 1.2.1.3) |
| [x] | `mqo3` | PP_2925 | Q88IS4 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Probable malate:quinone oxidoreductase 3 (EC 1.1.5.4) (MQO 3) (Malate dehydrogenase [quinone] 3) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `PP_3382` | PP_3382 | Q88HH6 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | Gluconate 2-dehydrogenase cytochrome c subunit (EC 1.1.99.3) |
| [x] | `adhB` | PP_3623 | Q88GU4 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | Alcohol dehydrogenase cytochrome c subunit |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `gloA` | PP_3766 | Q88GF8 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | Lactoylglutathione lyase (EC 4.4.1.5) (Glyoxalase I) |
| [x] | `adhP` | PP_3839 | Q88G86 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) |
| [x] | `gloB` | PP_4144 | Q88FF3 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | Hydroxyacylglutathione hydrolase (EC 3.1.2.6) (Glyoxalase II) (Glx II) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `pyk` | PP_4301 | Q88EZ9 | kegg:ppu00010 | PRESENT | CURATED | PRESENT | Pyruvate kinase (EC 2.7.1.40) |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `acsA1` | PP_4487 | Q88EH6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `acsA2` | PP_4702 | Q88DW6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme |
| [x] | `lldD` | PP_4736 | Q88DT3 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | L-lactate dehydrogenase (EC 1.1.-.-) |
| [x] | `dld2` | PP_4737 | Q88DT2 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | D-lactate dehydrogenase (EC 1.1.-.-) |
| [x] | `maeB` | PP_5085 | Q88CU5 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | NADP-dependent malic enzyme (EC 1.1.1.40) |
| [x] | `ycgM` | PP_5153 | Q88CM7 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | Isomerase/hydrolase (EC 3.-.-.-) |
| [x] | `pycB` | PP_5346 | Q88C37 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Pyruvate carboxylase subunit B (EC 6.4.1.1) |
| [x] | `pycA` | PP_5347 | Q88C36 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Biotin carboxylase (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-08T11:51:11.835910+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon pyruvate_metabolism_boundary`
  and `just module-pathway-deep-research-falcon pyruvate_metabolism_boundary ppu00620 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/pyruvate_metabolism_boundary-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__pyruvate_metabolism_boundary__ppu00620-deep-research-falcon.md`.
