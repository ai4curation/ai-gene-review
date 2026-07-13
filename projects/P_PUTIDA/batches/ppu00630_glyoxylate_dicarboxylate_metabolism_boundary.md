---
title: "PSEPK ppu00630 Glyoxylate and dicarboxylate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00630: Glyoxylate and dicarboxylate metabolism

- Module seed: `glyoxylate_dicarboxylate_metabolism_boundary`
- Candidate genes from membership table: 62
- Primary bucket genes: 9
- Existing review files: 62
- Curated review files: 62
- Existing Asta research files: 62

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
| [x] | `PP_0094` | PP_0094 | Q88RN5 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | 5'-nucleotidase (EC 3.1.3.5) |
| [x] | `katE` | PP_0115 | Q88RL4 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase (EC 1.11.1.6) |
| [x] | `glyA1` | PP_0322 | Q88R12 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) |
| [x] | `purU-I` | PP_0327 | Q88R07 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [x] | `glcB` | PP_0356 | Q88QX8 | kegg:ppu00620 | PRESENT | CURATED | PRESENT | Malate synthase G (EC 2.3.3.9) |
| [x] | `PP_0416` | PP_0416 | Q88QS2 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Phosphoglycolate phosphatase (PGP) (PGPase) (EC 3.1.3.18) |
| [x] | `katA` | PP_0481 | Q88QK9 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase (EC 1.11.1.6) |
| [x] | `fdoG` | PP_0489 | A0A140FVZ1 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase-O major subunit (EC 1.2.1.2) |
| [x] | `fdoH` | PP_0490 | Q88QK1 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase iron-sulfur subunit |
| [x] | `fdoI` | PP_0491 | Q88QK0 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase-O, gamma subunit (EC 1.2.1.2) |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `mdh` | PP_0654 | Q88Q44 | kegg:ppu00566 | PRESENT | CURATED | PRESENT | Probable malate dehydrogenase (EC 1.1.1.37) |
| [x] | `glyA2` | PP_0671 | Q88Q27 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) |
| [x] | `hprA` | PP_0762 | Q88PT6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Glycerate dehydrogenase |
| [x] | `gcvT-I` | PP_0986 | Q88P67 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `gcvP1` | PP_0988 | Q88P65 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) ( |
| [x] | `gcvH1` | PP_0989 | Q88P64 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 1 |
| [x] | `eda` | PP_1024 | Q88P29 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) |
| [x] | `ghrB` | PP_1261 | Q88NF1 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) |
| [x] | `purU-II` | PP_1367 | Q88N49 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [x] | `PP_1907` | PP_1907 | Q88LM3 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Hydrolase, haloacid dehalogenase-like family |
| [x] | `purU-III` | PP_1943 | Q88LI9 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [x] | `acnA-I` | PP_2112 | Q88L24 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Aconitate hydratase (Aconitase) (EC 4.2.1.3) |
| [x] | `puuA-I` | PP_2178 | Q88KW1 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [x] | `PP_2183` | PP_2183 | Q88KV6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase I subunit E) (NDH-1 subunit E) |
| [x] | `PP_2184` | PP_2184 | Q88KV5 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit F (NADH dehydrogenase I subunit F) (NDH-1 subunit F) |
| [x] | `PP_2185` | PP_2185 | Q88KV4 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase, alpha subunit |
| [x] | `PP_2186` | PP_2186 | Q88KV3 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Formate dehydrogenase, delta subunit |
| [x] | `PP_2213` | PP_2213 | Q88KS6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acyl-CoA synthetase (EC 6.2.1.-) |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `prpC` | PP_2335 | Q88KF5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Citrate synthase |
| [x] | `acnB` | PP_2339 | Q88KF1 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate dehydratase) |
| [x] | `PP_2887` | PP_2887 | Q88IW2 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase-related peroxidase (EC 1.11.1.-) |
| [x] | `PP_3148` | PP_3148 | Q88I53 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `garK` | PP_3178 | Q88I24 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerate kinase (EC 2.7.1.165) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `glcD` | PP_3745 | Q88GH8 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glycolate oxidase, putative FAD-linked subunit (EC 1.1.99.14) |
| [x] | `glcE` | PP_3746 | Q88GH7 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glycolate oxidase, putative FAD-binding subunit (EC 1.1.99.14) |
| [x] | `glcF` | PP_3747 | Q88GH6 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glycolate oxidase iron-sulfur subunit (EC 1.1.99.14) |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `aceA` | PP_4116 | Q88FI0 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | Isocitrate lyase (EC 4.1.3.1) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `gltA` | PP_4194 | Q88FA4 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Citrate synthase |
| [x] | `gcl` | PP_4297 | Q88F03 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glyoxylate carboligase (EC 4.1.1.47) (Tartronate-semialdehyde synthase) |
| [x] | `hyi` | PP_4298 | Q88F02 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Hydroxypyruvate isomerase (EC 5.3.1.22) |
| [x] | `glxR` | PP_4299 | Q88F01 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Tartronate semialdehyde reductase (EC 1.1.1.60) |
| [x] | `ttuD` | PP_4300 | Q88F00 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Hydroxypyruvate reductase (EC 1.1.1.81) |
| [x] | `PP_4399` | PP_4399 | Q88EQ4 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `acsA1` | PP_4487 | Q88EH6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme |
| [x] | `PP_4547` | PP_4547 | Q88EB9 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `acsA2` | PP_4702 | Q88DW6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme |
| [x] | `hutG` | PP_5029 | Q88D00 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | N-formylglutamate deformylase (EC 3.5.1.68) |
| [x] | `glnA` | PP_5046 | Q88CY3 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase (EC 6.3.1.2) |
| [x] | `spuB` | PP_5183 | Q88CJ7 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `spuI` | PP_5184 | Q88CJ6 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `gcvP2` | PP_5192 | Q88CI9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) ( |
| [x] | `gcvH2` | PP_5193 | Q88CI8 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 2 |
| [x] | `gcvT` | PP_5194 | Q88CI7 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `puuA-II` | PP_5299 | Q88C84 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-08T12:53:47.849307+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon glyoxylate_dicarboxylate_metabolism_boundary`
  and `just module-pathway-deep-research-falcon glyoxylate_dicarboxylate_metabolism_boundary ppu00630 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/glyoxylate_dicarboxylate_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__glyoxylate_dicarboxylate_metabolism_boundary__ppu00630-deep-research-falcon.md`.
