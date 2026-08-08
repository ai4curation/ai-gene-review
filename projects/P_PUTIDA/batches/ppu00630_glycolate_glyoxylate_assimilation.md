---
title: "PSEPK ppu00630 Glyoxylate and dicarboxylate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00630: Glyoxylate and dicarboxylate metabolism

- Module seed: `glycolate_glyoxylate_assimilation`
- Candidate genes from membership table: 62
- Primary bucket genes: 9
- Existing review files: 24
- Curated review files: 24
- OpenScientist research files for selected genes: 9

## Scope

This batch treats KEGG `ppu00630` as a broad glyoxylate/dicarboxylate map but
uses a narrower reusable module boundary: bacterial glycolate and glyoxylate
assimilation through GlcDEF glycolate dehydrogenase and the Gcl/Hyi/GlxR
tartronate-semialdehyde branch. Phosphoglycolate phosphatase activity is
retained as an optional glycolate-source/salvage input, but the species-aware
OpenScientist pass argues that it is not the physiological ppu00630 entry route
in KT2440. The 62 KEGG members include substantial spillover from
catalase/peroxide defense, formate dehydrogenase, one-carbon folate metabolism,
glycine cleavage, TCA/glyoxylate shunt, and downstream glycerate handling. Those
are documented here but are not all core module members.

Selected primary-bucket genes for this pass: `PP_0094`, `PP_0416`, `PP_1907`,
`glcD`, `glcE`, `glcF`, `gcl`, `hyi`, and `glxR`.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_0094` | PP_0094 | Q88RN5 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | 5'-nucleotidase (EC 3.1.3.5) |
| [ ] | `katE` | PP_0115 | Q88RL4 | kegg:ppu04146 | MISSING | MISSING | MISSING | Catalase (EC 1.11.1.6) |
| [ ] | `glyA1` | PP_0322 | Q88R12 | kegg:ppu04981 | MISSING | MISSING | MISSING | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) |
| [ ] | `purU-I` | PP_0327 | Q88R07 | kegg:ppu00670 | MISSING | MISSING | MISSING | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [ ] | `glcB` | PP_0356 | Q88QX8 | kegg:ppu00620 | MISSING | MISSING | MISSING | Malate synthase G (EC 2.3.3.9) |
| [x] | `PP_0416` | PP_0416 | Q88QS2 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Phosphoglycolate phosphatase (PGP) (PGPase) (EC 3.1.3.18) |
| [ ] | `katA` | PP_0481 | Q88QK9 | kegg:ppu04146 | PRESENT | CURATED | MISSING | Catalase (EC 1.11.1.6) |
| [ ] | `fdoG` | PP_0489 | A0A140FVZ1 | kegg:ppu00680 | MISSING | MISSING | MISSING | Formate dehydrogenase-O major subunit (EC 1.2.1.2) |
| [ ] | `fdoH` | PP_0490 | Q88QK1 | kegg:ppu00680 | MISSING | MISSING | MISSING | Formate dehydrogenase iron-sulfur subunit |
| [ ] | `fdoI` | PP_0491 | Q88QK0 | kegg:ppu00680 | MISSING | MISSING | MISSING | Formate dehydrogenase-O, gamma subunit (EC 1.2.1.2) |
| [ ] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | MISSING | MISSING | MISSING | Thiolase family protein |
| [ ] | `mdh` | PP_0654 | Q88Q44 | kegg:ppu00566 | PRESENT | CURATED | MISSING | Probable malate dehydrogenase (EC 1.1.1.37) |
| [ ] | `glyA2` | PP_0671 | Q88Q27 | kegg:ppu04981 | MISSING | MISSING | MISSING | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) |
| [ ] | `hprA` | PP_0762 | Q88PT6 | kegg:ppu00680 | MISSING | MISSING | MISSING | Glycerate dehydrogenase |
| [ ] | `gcvT-I` | PP_0986 | Q88P67 | kegg:ppu00785 | MISSING | MISSING | MISSING | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [ ] | `gcvP1` | PP_0988 | Q88P65 | kegg:ppu00785 | MISSING | MISSING | MISSING | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) ( |
| [ ] | `gcvH1` | PP_0989 | Q88P64 | kegg:ppu00785 | MISSING | MISSING | MISSING | Glycine cleavage system H protein 1 |
| [ ] | `eda` | PP_1024 | Q88P29 | kegg:ppu00030 | PRESENT | CURATED | MISSING | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) |
| [ ] | `ghrB` | PP_1261 | Q88NF1 | kegg:ppu00030 | MISSING | MISSING | MISSING | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) |
| [ ] | `purU-II` | PP_1367 | Q88N49 | kegg:ppu00670 | MISSING | MISSING | MISSING | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [x] | `PP_1907` | PP_1907 | Q88LM3 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Hydrolase, haloacid dehalogenase-like family |
| [ ] | `purU-III` | PP_1943 | Q88LI9 | kegg:ppu00670 | MISSING | MISSING | MISSING | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) |
| [ ] | `acnA-I` | PP_2112 | Q88L24 | kegg:ppu00020 | PRESENT | CURATED | MISSING | Aconitate hydratase (Aconitase) (EC 4.2.1.3) |
| [ ] | `puuA-I` | PP_2178 | Q88KW1 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [ ] | `PP_2183` | PP_2183 | Q88KV6 | kegg:ppu00680 | MISSING | MISSING | MISSING | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase I subunit E) (NDH-1 subunit E) |
| [ ] | `PP_2184` | PP_2184 | Q88KV5 | kegg:ppu00680 | MISSING | MISSING | MISSING | NADH-quinone oxidoreductase subunit F (NADH dehydrogenase I subunit F) (NDH-1 subunit F) |
| [ ] | `PP_2185` | PP_2185 | Q88KV4 | kegg:ppu00680 | MISSING | MISSING | MISSING | Formate dehydrogenase, alpha subunit |
| [ ] | `PP_2186` | PP_2186 | Q88KV3 | kegg:ppu00680 | MISSING | MISSING | MISSING | Formate dehydrogenase, delta subunit |
| [x] | `PP_2213` | PP_2213 | Q88KS6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acyl-CoA synthetase (EC 6.2.1.-) |
| [ ] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | MISSING | MISSING | MISSING | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [ ] | `prpC` | PP_2335 | Q88KF5 | kegg:ppu00020 | PRESENT | CURATED | MISSING | Citrate synthase |
| [ ] | `acnB` | PP_2339 | Q88KF1 | kegg:ppu00020 | PRESENT | CURATED | MISSING | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate dehydratase) |
| [ ] | `PP_2887` | PP_2887 | Q88IW2 | kegg:ppu04146 | MISSING | MISSING | MISSING | Catalase-related peroxidase (EC 1.11.1.-) |
| [ ] | `PP_3148` | PP_3148 | Q88I53 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamine synthetase |
| [ ] | `garK` | PP_3178 | Q88I24 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerate kinase (EC 2.7.1.165) |
| [ ] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | MISSING | MISSING | MISSING | Beta-ketothiolase |
| [x] | `glcD` | PP_3745 | Q88GH8 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glycolate oxidase, putative FAD-linked subunit (EC 1.1.99.14) |
| [x] | `glcE` | PP_3746 | Q88GH7 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glycolate oxidase, putative FAD-binding subunit (EC 1.1.99.14) |
| [x] | `glcF` | PP_3747 | Q88GH6 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glycolate oxidase iron-sulfur subunit (EC 1.1.99.14) |
| [ ] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | MISSING | MISSING | MISSING | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [ ] | `aceA` | PP_4116 | Q88FI0 | kegg:ppu00640 | PRESENT | CURATED | MISSING | Isocitrate lyase (EC 4.1.3.1) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [ ] | `gltA` | PP_4194 | Q88FA4 | kegg:ppu00020 | PRESENT | CURATED | MISSING | Citrate synthase |
| [x] | `gcl` | PP_4297 | Q88F03 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Glyoxylate carboligase (EC 4.1.1.47) (Tartronate-semialdehyde synthase) |
| [x] | `hyi` | PP_4298 | Q88F02 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Hydroxypyruvate isomerase (EC 5.3.1.22) |
| [x] | `glxR` | PP_4299 | Q88F01 | kegg:ppu00630 | PRESENT | CURATED | PRESENT | Tartronate semialdehyde reductase (EC 1.1.1.60) |
| [ ] | `ttuD` | PP_4300 | Q88F00 | kegg:ppu00561 | MISSING | MISSING | MISSING | Hydroxypyruvate reductase (EC 1.1.1.81) |
| [ ] | `PP_4399` | PP_4399 | Q88EQ4 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamine synthetase |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `acsA1` | PP_4487 | Q88EH6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme |
| [ ] | `PP_4547` | PP_4547 | Q88EB9 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamine synthetase |
| [ ] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | MISSING | MISSING | MISSING | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `acsA2` | PP_4702 | Q88DW6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme |
| [ ] | `hutG` | PP_5029 | Q88D00 | kegg:ppu00340 | MISSING | MISSING | MISSING | N-formylglutamate deformylase (EC 3.5.1.68) |
| [x] | `glnA` | PP_5046 | Q88CY3 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase (EC 6.3.1.2) |
| [ ] | `spuB` | PP_5183 | Q88CJ7 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamylpolyamine synthetase |
| [ ] | `spuI` | PP_5184 | Q88CJ6 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamylpolyamine synthetase |
| [ ] | `gcvP2` | PP_5192 | Q88CI9 | kegg:ppu00785 | MISSING | MISSING | MISSING | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) ( |
| [ ] | `gcvH2` | PP_5193 | Q88CI8 | kegg:ppu00785 | MISSING | MISSING | MISSING | Glycine cleavage system H protein 2 |
| [ ] | `gcvT` | PP_5194 | Q88CI7 | kegg:ppu00785 | MISSING | MISSING | MISSING | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [ ] | `puuA-II` | PP_5299 | Q88C84 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-15T23:03:31.525943+00:00

## 2026-07-15 curation notes

- Added `modules/glycolate_glyoxylate_assimilation.yaml` as a bacterial,
  species-neutral multi-part module. It is intentionally separate from the
  existing human `glyoxylate_oxalate_metabolism.yaml` module.
- Kept the module process-level at the pathway/process layer; molecular
  functions are only attached to leaf annotons.
- Used PSEPK UniProt exemplars for PP_0416, GlcD, GlcE, GlcF, Gcl, Hyi, and
  GlxR. PP_0094 and PP_1907 are recorded as HAD-family phosphatase candidates
  requiring conservative gene-level review before they are treated as module
  satisfiers.
- Revised the module boundary after the species/pathway OpenScientist report:
  GlcDEF, Gcl, Hyi, and GlxR form the physiologically relevant KT2440 core, while
  PP_0416, PP_1907, and PP_0094 are optional phosphoglycolate or small
  phosphometabolite salvage candidates.
- Kept GclR-mediated repression/derepression, glycolate/glyoxylate transport,
  `ttuD`, and reductase paralogs such as `ghrB`/`hprA` as follow-up questions
  rather than forcing them into this module PR.
- Excluded `aceA`/`glcB` glyoxylate-shunt logic and `garK` downstream
  glycerate kinase from this module boundary; those belong in neighboring
  modules.
