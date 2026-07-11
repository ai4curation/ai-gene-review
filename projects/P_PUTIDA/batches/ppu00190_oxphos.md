---
title: "PSEPK ppu00190 Oxidative phosphorylation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00190: Oxidative phosphorylation

- Module seed: `oxphos`
- Candidate genes from membership table: 54
- Primary bucket genes: 44
- Existing review files: 54
- Curated review files: 54
- Existing Asta research files: 54

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
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
| [x] | `PP_0103` | PP_0103 | Q88RM6 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome c oxidase subunit 2 (EC 7.1.1.9) |
| [x] | `ctaD` | PP_0104 | Q88RM5 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome c oxidase subunit 1 (EC 7.1.1.9) |
| [x] | `PP_0105` | PP_0105 | Q88RM4 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome c oxidase assembly protein CtaG |
| [x] | `PP_0106` | PP_0106 | Q88RM3 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Probable cytochrome c oxidase subunit 3 (EC 7.1.1.9) (Cytochrome aa3 subunit 3) (Cytochrome c oxidase polypeptide III) |
| [x] | `PP_0109` | PP_0109 | Q88RM0 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Cytochrome B |
| [x] | `cyoE1` | PP_0110 | Q88RL9 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Protoheme IX farnesyltransferase 1 (EC 2.5.1.141) (Heme B farnesyltransferase 1) (Heme O synthase 1) |
| [x] | `ppa` | PP_0538 | Q88QF6 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Inorganic pyrophosphatase (EC 3.6.1.1) (Pyrophosphate phospho-hydrolase) (PPase) |
| [x] | `ndh` | PP_0626 | Q88Q70 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH dehydrogenase (EC 1.6.99.3) |
| [x] | `ppkB` | PP_0712 | Q88PY6 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | ADP/GDP-polyphosphate phosphotransferase (EC 2.7.4.-) (Polyphosphate kinase PPK2) |
| [x] | `cyoA` | PP_0812 | Q88PN7 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Ubiquinol oxidase subunit 2 |
| [x] | `cyoB` | PP_0813 | Q88PN6 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome bo(3) ubiquinol oxidase subunit 1 (EC 7.1.1.3) (Cytochrome o ubiquinol oxidase subunit 1) (Oxidase bo(3) subu |
| [x] | `cyoC` | PP_0814 | Q88PN5 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome bo(3) ubiquinol oxidase subunit 3 (Cytochrome o ubiquinol oxidase subunit 3) (Oxidase bo(3) subunit 3) (Ubiqu |
| [x] | `cyoD` | PP_0815 | Q88PN4 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome bo(3) ubiquinol oxidase subunit 4 (Cytochrome o ubiquinol oxidase subunit 4) (Oxidase bo(3) subunit 4) (Ubiqu |
| [x] | `cyoE2` | PP_0816 | Q88PN3 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Protoheme IX farnesyltransferase 2 (EC 2.5.1.141) (Heme B farnesyltransferase 2) (Heme O synthase 2) |
| [x] | `petA` | PP_1317 | Q88N95 | kegg:ppu04148 | PRESENT | CURATED | PRESENT | Ubiquinol-cytochrome c reductase iron-sulfur subunit (EC 7.1.1.8) |
| [x] | `petB` | PP_1318 | Q88N94 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome b |
| [x] | `petC` | PP_1319 | Q88N93 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Ubiquinol--cytochrome c reductase, cytochrome c1 |
| [x] | `PP_2867` | PP_2867 | Q88IY2 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Pyridine nucleotide-disulphide oxidoreductase family protein |
| [x] | `nuoA` | PP_4119 | Q88FH7 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit A (EC 7.1.1.-) (NADH dehydrogenase I subunit A) (NDH-1 subunit A) (NUO1) |
| [x] | `nuoB` | PP_4120 | Q88FH6 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit B (EC 7.1.1.-) (NADH dehydrogenase I subunit B) (NDH-1 subunit B) |
| [x] | `nuoC` | PP_4121 | Q88FH5 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit C/D (EC 7.1.1.-) (NADH dehydrogenase I subunit C/D) (NDH-1 subunit C/D) |
| [x] | `nuoE` | PP_4122 | Q88FH4 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase I subunit E) (NDH-1 subunit E) |
| [x] | `nuoF` | PP_4123 | Q88FH3 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit F (EC 7.1.1.-) |
| [x] | `nuoG` | PP_4124 | Q88FH2 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit G (EC 7.1.1.-) (NADH dehydrogenase I subunit G) (NDH-1 subunit G) |
| [x] | `nuoH` | PP_4125 | Q88FH1 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit H (EC 7.1.1.-) (NADH dehydrogenase I subunit H) (NDH-1 subunit H) |
| [x] | `nuoI` | PP_4126 | Q88FH0 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit I (EC 7.1.1.-) (NADH dehydrogenase I subunit I) (NDH-1 subunit I) |
| [x] | `nuoJ` | PP_4127 | Q88FG9 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit J (EC 7.1.1.-) |
| [x] | `nuoK` | PP_4128 | Q88FG8 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit K (EC 7.1.1.-) (NADH dehydrogenase I subunit K) (NDH-1 subunit K) |
| [x] | `nuoL` | PP_4129 | Q88FG7 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit L (NADH dehydrogenase I subunit L) (NDH-1 subunit L) |
| [x] | `nuoM` | PP_4130 | Q88FG6 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit M (NADH dehydrogenase I subunit M) (NDH-1 subunit M) |
| [x] | `nuoN` | PP_4131 | Q88FG5 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | NADH-quinone oxidoreductase subunit N (EC 7.1.1.-) (NADH dehydrogenase I subunit N) (NDH-1 subunit N) |
| [x] | `sdhB` | PP_4190 | Q88FA8 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1) |
| [x] | `sdhA` | PP_4191 | Q88FA7 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1) |
| [x] | `sdhD` | PP_4192 | Q88FA6 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase hydrophobic membrane anchor subunit |
| [x] | `sdhC` | PP_4193 | Q88FA5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase cytochrome b556 subunit |
| [x] | `ccoN-I` | PP_4250 | Q88F49 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | cytochrome-c oxidase (EC 7.1.1.9) |
| [x] | `ccoO-I` | PP_4251 | Q88F48 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome c oxidase subunit, cbb3-type |
| [x] | `ccoQ-I` | PP_4252 | Q88F47 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome c oxidase subunit, cbb3-type |
| [x] | `ccoP-I` | PP_4253 | Q88F46 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cbb3-type cytochrome c oxidase subunit |
| [x] | `ccoN-II` | PP_4255 | Q88F44 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | cytochrome-c oxidase (EC 7.1.1.9) |
| [x] | `ccoO-II` | PP_4256 | Q88F43 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome c oxidase subunit, cbb3-type |
| [x] | `ccoQ-II` | PP_4257 | Q88F42 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cytochrome c oxidase subunit, cbb3-type |
| [x] | `ccoP-II` | PP_4258 | Q88F41 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Cbb3-type cytochrome c oxidase subunit |
| [x] | `cioB` | PP_4650 | Q88E18 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Ubiquinol oxidase subunit II, cyanide insensitive |
| [x] | `cioA` | PP_4651 | Q88E17 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | Ubiquinol oxidase subunit I, cyanide insensitive |
| [x] | `ppk` | PP_5217 | Q88CG4 | kegg:ppu03018 | PRESENT | CURATED | PRESENT | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate phosphotransferase) (Polyphosphoric acid kinase) |
| [x] | `atpC` | PP_5412 | Q88BX5 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase epsilon chain (ATP synthase F1 sector epsilon subunit) (F-ATPase epsilon subunit) |
| [x] | `atpD` | PP_5413 | Q88BX4 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase subunit beta (EC 7.1.2.2) (ATP synthase F1 sector subunit beta) (F-ATPase subunit beta) |
| [x] | `atpG` | PP_5414 | Q88BX3 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase gamma chain (ATP synthase F1 sector gamma subunit) (F-ATPase gamma subunit) |
| [x] | `atpA` | PP_5415 | Q88BX2 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase subunit alpha (EC 7.1.2.2) (ATP synthase F1 sector subunit alpha) (F-ATPase subunit alpha) |
| [x] | `atpH` | PP_5416 | Q88BX1 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase subunit delta (ATP synthase F(1) sector subunit delta) (F-type ATPase subunit delta) (F-ATPase subunit delt |
| [x] | `atpF` | PP_5417 | Q88BX0 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase subunit b (ATP synthase F(0) sector subunit b) (ATPase subunit I) (F-type ATPase subunit b) (F-ATPase subun |
| [x] | `atpE` | PP_5418 | Q88BW9 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase subunit c (ATP synthase F(0) sector subunit c) (F-type ATPase subunit c) (F-ATPase subunit c) (Lipid-bindin |
| [x] | `atpB` | PP_5419 | Q88BW8 | kegg:ppu00190 | PRESENT | CURATED | PRESENT | ATP synthase subunit a (ATP synthase F0 sector subunit a) (F-ATPase subunit 6) |

## Notes

Generated UTC: 2026-07-07T13:18:10.223781+00:00

Workflow notes as of 2026-07-07:

- Reused and validated the existing species-neutral module:
  `modules/oxphos.yaml`.
- Generic module-level Falcon research completed:
  `modules/oxphos-deep-research-falcon.md`.
- Ran `just module-pathway-deep-research-falcon oxphos ppu00190 PSEPK`; it
  reached Edison and failed at task creation with HTTP 402 Payment Required, so
  `projects/P_PUTIDA/deep-research/PSEPK__oxphos__ppu00190-deep-research-falcon.md`
  was not created. Captured log: `reports/falcon-ppu00190-pathway.log`.
- All 54 candidate gene reviews validate with `just validate PSEPK <gene>`.
  Remaining validator messages are warnings about Asta being recorded as
  retrieval context and about core-function context terms not being accepted as
  standalone existing annotations.
- All 54 gene review pages were rendered with `just render PSEPK <gene>`.

First-pass curation notes:

- The strict respiratory chain is represented by Complex I (`nuoA`-`nuoN`),
  type-II NADH dehydrogenase `ndh`, succinate dehydrogenase, bc1
  (`petA`/`petB`/`petC`), aa3, bo3, duplicated cbb3, cyanide-insensitive
  oxidase (`cioA`/`cioB`), and F1Fo ATP synthase (`atpC`-`atpB`) branches.
- bo3 subunit reviews modify generic cytochrome-c oxidase activity to
  donor-specific cytochrome bo3 ubiquinol oxidase activity where appropriate.
- Nuo complex-I subunit reviews use the more specific NADH dehydrogenase
  (ubiquinone) activity as the complex-level contribution.
- `ccoQ-I` and `ccoQ-II` had no GOA annotations but were retained as
  cbb3-type cytochrome c oxidase subunits based on UniProt/module context.
- `ppa`, `ppk`, `ppkB`, heme O/heme A context genes, and other phosphate/heme
  side nodes are boundary context for KEGG `ppu00190`, not strict OXPHOS
  catalytic steps.
