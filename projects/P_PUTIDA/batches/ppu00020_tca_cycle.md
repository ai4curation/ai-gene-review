---
title: "PSEPK ppu00020 Citrate cycle (TCA cycle) batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00020: Citrate cycle (TCA cycle)

- Module seed: `tca_cycle`
- Candidate genes from membership table: 30
- Primary bucket genes: 17
- Existing review files: 30
- Curated review files: 30
- Existing OpenScientist research files: 30

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `scpC` | PP_0154 | Q88RH5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Propionyl-CoA:succinate CoA transferase (EC 2.8.3.-) |
| [x] | `aceF` | PP_0338 | Q88QZ6 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) |
| [x] | `aceE` | PP_0339 | Q88QZ5 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) |
| [x] | `acoC` | PP_0553 | Q88QE1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system (EC 2.3.1.12) |
| [x] | `mdh` | PP_0654 | Q88Q44 | kegg:ppu00566 | PRESENT | CURATED | PRESENT | Probable malate dehydrogenase (EC 1.1.1.37) |
| [x] | `mqo1` | PP_0751 | Q88PU7 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Probable malate:quinone oxidoreductase 1 (EC 1.1.5.4) (MQO 1) (Malate dehydrogenase [quinone] 1) |
| [x] | `PP_0897` | PP_0897 | Q88PF3 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Fumarate hydratase class I (EC 4.2.1.2) |
| [x] | `fumC-I` | PP_0944 | Q88PA6 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) |
| [x] | `mqo2` | PP_1251 | Q88NF9 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Probable malate:quinone oxidoreductase 2 (EC 1.1.5.4) (MQO 2) (Malate dehydrogenase [quinone] 2) |
| [x] | `fumC` | PP_1755 | Q88M20 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) |
| [x] | `acnA-I` | PP_2112 | Q88L24 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Aconitate hydratase (Aconitase) (EC 4.2.1.3) |
| [x] | `prpC` | PP_2335 | Q88KF5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Citrate synthase |
| [x] | `acnB` | PP_2339 | Q88KF1 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate dehydratase) |
| [x] | `mqo3` | PP_2925 | Q88IS4 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Probable malate:quinone oxidoreductase 3 (EC 1.1.5.4) (MQO 3) (Malate dehydrogenase [quinone] 3) |
| [x] | `icd` | PP_4011 | Q88FS2 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) |
| [x] | `idh` | PP_4012 | Q88FS1 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) (Oxalosuccinate decarboxylase) |
| [x] | `sucD` | PP_4185 | Q88FB3 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Succinate--CoA ligase [ADP-forming] subunit alpha (EC 6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha) |
| [x] | `sucC` | PP_4186 | Q88FB2 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Succinate--CoA ligase [ADP-forming] subunit beta (EC 6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `sucB` | PP_4188 | Q88FB0 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxogl |
| [x] | `sucA` | PP_4189 | Q88FA9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoglutarate dehydrogenase E1 component (EC 1.2.4.2) (Alpha-ketoglutarate dehydrogenase) |
| [x] | `sdhB` | PP_4190 | Q88FA8 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1) |
| [x] | `sdhA` | PP_4191 | Q88FA7 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1) |
| [x] | `sdhD` | PP_4192 | Q88FA6 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase hydrophobic membrane anchor subunit |
| [x] | `sdhC` | PP_4193 | Q88FA5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase cytochrome b556 subunit |
| [x] | `gltA` | PP_4194 | Q88FA4 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Citrate synthase |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `pycB` | PP_5346 | Q88C37 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Pyruvate carboxylase subunit B (EC 6.4.1.1) |
| [x] | `pycA` | PP_5347 | Q88C36 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Biotin carboxylase (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-12T00:20:26.410305+00:00

Completed pass:

- Added the species-neutral `modules/tca_cycle.yaml` module review and
  OpenScientist module/pathway reports.
- Generated OpenScientist gene-level reports for all 30 batch genes.
- Curated and validated all 30 selected PSEPK gene review files.
