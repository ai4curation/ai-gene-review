---
title: "PSEPK ppu02020 Two-component system batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02020: Two-component system

- Module seed: `two_component_system_boundary`
- Candidate genes from membership table: 99
- Primary bucket genes: 99
- Existing review files: 99
- Curated review files: 99
- Existing Asta research files: 99

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
| [x] | `dnaA` | PP_0010 | P0A116 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Chromosomal replication initiator protein DnaA |
| [x] | `czcR-I` | PP_0029 | Q88RV0 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Two component heavy metal response regulator |
| [x] | `czrSA` | PP_0030 | Q88RU9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Sensor protein (EC 2.7.13.3) |
| [x] | `czcR-II` | PP_0047 | Q88RT2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Response regulator |
| [x] | `kinB` | PP_0132 | Q88RJ7 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `algB` | PP_0133 | Q88RJ6 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Alginate biosynthesis transcriptional regulatory protein AlgB |
| [x] | `PP_0161` | PP_0161 | Q88RG9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor |
| [x] | `PP_0162` | PP_0162 | Q88RG8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | RNA polymerase sigma-70 factor, ECF subfamily |
| [x] | `algR` | PP_0185 | Q88RE6 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Positive alginate biosynthesis regulatory protein |
| [x] | `ompR` | PP_0246 | Q88R87 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | DNA-binding dual transcriptional regulator OmpR (Transcriptional regulatory protein OmpR) |
| [x] | `envZ` | PP_0247 | Q88R86 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `dctD-I` | PP_0263 | Q88R71 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | HTH-type transcriptional regulatory protein TyrR |
| [x] | `PP_0264` | PP_0264 | Q88R70 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | C4-dicarboxylate transport sensor protein DctB (EC 2.7.13.3) |
| [x] | `PP_0351` | PP_0351 | Q88QY3 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor protein |
| [x] | `PP_0352` | PP_0352 | Q88QY2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | RNA polymerase sigma-70 factor, ECF subfamily |
| [x] | `uhpA` | PP_0410 | Q88QS8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | DNA-binding response regulator UhpA |
| [x] | `pfeS-I` | PP_0533 | Q88QG1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_0534` | PP_0534 | Q88QG0 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transcriptional regulator PfeR |
| [x] | `PP_0574` | PP_0574 | Q88QC0 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | DNA-binding response regulator, LuxR family |
| [x] | `pilA` | PP_0634 | Q88Q62 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Pilin |
| [x] | `PP_0667` | PP_0667 | Q88Q31 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | RNA polymerase sigma-70 factor, ECF subfamily |
| [x] | `PP_0703` | PP_0703 | Q88PZ5 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor |
| [x] | `PP_0704` | PP_0704 | Q88PZ4 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | RNA polymerase sigma-70 factor, ECF subfamily |
| [x] | `PP_0866` | PP_0866 | Q88PI4 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor |
| [x] | `PP_0887` | PP_0887 | Q88PG3 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `regA` | PP_0888 | Q88PG2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Photosynthetic apparatus regulatory protein RegA |
| [x] | `PP_1007` | PP_1007 | Q88P46 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor |
| [x] | `dctD-II` | PP_1066 | Q88NY7 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | C4-dicarboxylate transport transcriptional regulatory protein |
| [x] | `PP_1067` | PP_1067 | Q88NY6 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | C4-dicarboxylate transport sensor protein DctB (EC 2.7.13.3) |
| [x] | `bvgA` | PP_1090 | Q88NW4 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Virulence factors positive transcription regulator BvgA |
| [x] | `PP_1167` | PP_1167 | Q88NP0 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | TRAP transporter large permease protein |
| [x] | `PP_1168` | PP_1168 | Q88NN9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | TRAP transporter small permease protein |
| [x] | `dctP` | PP_1169 | Q88NN8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | TRAP dicarboxylate transporter, DctP subunit |
| [x] | `PP_1181` | PP_1181 | Q88NM6 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | DNA-binding response regulator |
| [x] | `PP_1182` | PP_1182 | Q88NM5 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `dctA` | PP_1188 | Q88NL9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | C4-dicarboxylate transport protein |
| [x] | `dctD-III` | PP_1401 | Q88N15 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | C4-dicarboxylate transport transcriptional regulatory protein |
| [x] | `dctB` | PP_1402 | Q88N14 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_1416` | PP_1416 | Q88N02 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Tricarboxylate transport protein TctA |
| [x] | `PP_1417` | PP_1417 | Q88N01 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Tricarboxylate transport protein TctB |
| [x] | `PP_1418` | PP_1418 | Q88N00 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Tricarboxylate transport protein TctC |
| [x] | `tctD` | PP_1420 | Q88MZ8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transcriptional regulatory protein tctD |
| [x] | `PP_1421` | PP_1421 | Q88MZ7 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_1437` | PP_1437 | Q88MY1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Sensor protein (EC 2.7.13.3) |
| [x] | `czcR-III` | PP_1438 | Q88MY0 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Response regulator |
| [x] | `wspC` | PP_1490 | Q88MS8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Probable biofilm formation methyltransferase WspC (EC 2.1.1.-) |
| [x] | `glnD` | PP_1589 | Q88MI2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Bifunctional uridylyltransferase/uridylyl-removing enzyme (UTase/UR) (Bifunctional [protein-PII] modification enzyme) (B |
| [x] | `PP_1651` | PP_1651 | Q88MC2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Two-component response regulator |
| [x] | `pfeS-II` | PP_1652 | Q88MC1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `fimD` | PP_1889 | Q88LP0 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Type 1 pili subunit FimD |
| [x] | `PP_1890` | PP_1890 | Q88LN9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Type 1 pili chaperone protein FimC |
| [x] | `etp` | PP_1903 | Q88LM6 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | protein-tyrosine-phosphatase (EC 3.1.3.48) |
| [x] | `dctA-II` | PP_2056 | Q88L79 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | C4-dicarboxylate transport protein |
| [x] | `PP_2100` | PP_2100 | Q88L35 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `evgA` | PP_2101 | Q88L34 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | DNA-binding response regulator in two-component regulatory system with EvgS |
| [x] | `PP_2157` | PP_2157 | Q88KY2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Sensor protein (EC 2.7.13.3) |
| [x] | `copR-I` | PP_2158 | Q88KY1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transcriptional activator protein |
| [x] | `fepA` | PP_2242 | Q88KP8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Ferric enterobactin transport system outer membrane subunit |
| [x] | `dctA-III` | PP_2255 | Q88KN5 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | C4-dicarboxylate transport protein |
| [x] | `PP_2356` | PP_2356 | Q88KD4 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_2357` | PP_2357 | Q88KD3 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Type 1 pili protein CsuB |
| [x] | `PP_2358` | PP_2358 | Q88KD2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Type 1 pili subunit CsuA/B protein |
| [x] | `PP_2359` | PP_2359 | Q88KD1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Type 1 pili subunit CsuA/B protein |
| [x] | `PP_2360` | PP_2360 | Q88KD0 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Type 1 pili subunit CsuA/B protein |
| [x] | `PP_2361` | PP_2361 | Q88KC9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Chaperone protein |
| [x] | `PP_2362` | PP_2362 | Q88KC8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Usher protein |
| [x] | `PP_2363` | PP_2363 | Q88KC7 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Spore coat protein U/FanG domain-containing protein |
| [x] | `PP_2671` | PP_2671 | Q88JH8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_3085` | PP_3085 | Q88IB4 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor |
| [x] | `PP_3086` | PP_3086 | Q88IB3 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | RNA polymerase sigma-70 factor |
| [x] | `PP_3124` | PP_3124 | Q88I77 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Short chain fatty acid transporter |
| [x] | `PP_3126` | PP_3126 | Q88I75 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Polysaccharide exported protein |
| [x] | `PP_3412` | PP_3412 | Q88HE8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | DNA-binding response regulator, LuxR family |
| [x] | `PP_3413` | PP_3413 | Q88HE7 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_3576` | PP_3576 | Q88GY9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor |
| [x] | `fecI` | PP_3577 | Q88GY8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | RNA polymerase, sigma 19 factor |
| [x] | `mdtC` | PP_3583 | Q88GY2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Multidrug efflux transport system-membrane subunit |
| [x] | `mdtB` | PP_3584 | A0A140FWF8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Multidrug efflux transport system-membrane subunit |
| [x] | `mdtA` | PP_3585 | Q88GY1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Multidrug efflux transport system-putative membrane fusion protein |
| [x] | `kdpD` | PP_4158 | Q88FD9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `kdpC` | PP_4159 | Q88FD8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Potassium-transporting ATPase KdpC subunit (ATP phosphohydrolase [potassium-transporting] C chain) (Potassium-binding an |
| [x] | `kdpB` | PP_4160 | A0A140FWL1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Potassium-transporting ATPase ATP-binding subunit (EC 7.2.2.6) (ATP phosphohydrolase [potassium-transporting] B chain) ( |
| [x] | `kdpA` | PP_4161 | Q88FD7 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Potassium-transporting ATPase potassium-binding subunit (ATP phosphohydrolase [potassium-transporting] A chain) (Potassi |
| [x] | `fleS` | PP_4372 | Q88ET1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_4607` | PP_4607 | Q88E61 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transmembrane sensor |
| [x] | `PP_4611` | PP_4611 | Q88E57 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | RNA polymerase sigma-70 factor, ECF subfamily |
| [x] | `PP_4612` | PP_4612 | Q88E56 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | FecR protein |
| [x] | `PP_4696` | PP_4696 | Q88DX2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Alginate biosynthesis transcriptional regulatory protein AlgB |
| [x] | `glnL` | PP_5047 | Q88CY2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Sensory histidine kinase/phosphatase NtrB (EC 2.7.13.3) (Nitrogen regulation protein NR(II)) (Nitrogen regulator II) |
| [x] | `glnG` | PP_5048 | Q88CY1 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | DNA-binding transcriptional regulator NtrC (Nitrogen regulation protein NR(I)) |
| [x] | `phoB` | PP_5320 | Q88C63 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Phosphate regulon transcriptional regulatory protein PhoB |
| [x] | `phoR` | PP_5321 | Q88C62 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Phosphate regulon sensor protein PhoR (EC 2.7.13.3) |
| [x] | `copR-II` | PP_5383 | Q88C00 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Transcriptional activator protein |
| [x] | `copS` | PP_5384 | Q88BZ9 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Sensor protein (EC 2.7.13.3) |
| [x] | `czcC` | PP_5385 | Q88BZ8 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Metal RND efflux outer membrane protein, CzcC family |
| [x] | `cusB` | PP_5386 | Q88BZ7 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Probable copper RND efflux membrane fusion protein, CzcB family |
| [x] | `cusA` | PP_5387 | Q88BZ6 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Probable copper efflux transporter, CzcA family |
| [x] | `cusF` | PP_5388 | Q88BZ5 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Probable exported copper efflux protein |
| [x] | `kdpF` | PP_5660 | A0A140FWL2 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Potassium-transporting ATPase F |

## Notes

Generated UTC: 2026-07-09T21:14:14.947474+00:00

2026-07-11 PDT status sync: created and validated `modules/two_component_system_boundary.yaml` as the ppu02020 parent boundary module. The module records ppu02020 as a partitioned KEGG umbrella map, with gene-level claims delegated to the curated submodules in `projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.md`: metal/copper/zinc response, iron uptake regulation, alginate/biofilm regulation, osmotic/envelope/efflux regulation, dicarboxylate/tricarboxylate transport regulation, ECF sigma/anti-sigma systems, nutrient homeostasis, pili/surface adhesion, orphan/generic TCS proteins, plus `dnaA` and `etp` side-context spillovers.

Module validation passed with both module validators. The existing workflow already records 99/99 review files, 99/99 curated review YAMLs, 99/99 Asta reports, and gene-review validation as complete.

Real Falcon commands were run:

```bash
just module-deep-research-falcon two_component_system_boundary
just module-pathway-deep-research-falcon two_component_system_boundary ppu02020 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. The taxon-aware wrapper resolved the pathway context as 99 primary genes and 217 total local members. Expected output paths remain:

- `modules/two_component_system_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__two_component_system_boundary__ppu02020-deep-research-falcon.md`
