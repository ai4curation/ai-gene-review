---
title: "PSEPK ppu00240 Pyrimidine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00240: Pyrimidine metabolism

- Module seed: `pyrimidine_metabolism`
- Candidate genes from membership table: 36
- Primary bucket genes: 24
- Existing review files: 36
- Curated review files: 36
- Existing Asta research files: 36

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
| [x] | `PP_0488` | PP_0488 | Q88QK2 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | NADP-dependent dehydrogenase HI_1430 (EC 1.1.1.-) |
| [x] | `PP_0614` | PP_0614 | Q88Q81 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) |
| [x] | `upp` | PP_0746 | Q88PV2 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Uracil phosphoribosyltransferase (EC 2.4.2.9) (UMP pyrophosphorylase) (UPRTase) |
| [x] | `ndk` | PP_0849 | Q88PK1 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC 2.7.4.6) (Nucleoside-2-P kinase) |
| [x] | `maf-1` | PP_0936 | Q88PB4 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | dTTP/UTP pyrophosphatase (dTTPase/UTPase) (EC 3.6.1.9) (Nucleoside triphosphate pyrophosphatase) (Nucleotide pyrophospha |
| [x] | `pyrC` | PP_1086 | Q88NW7 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Dihydroorotase (DHOase) (EC 3.5.2.3) |
| [x] | `dcd` | PP_1100 | Q88NV4 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | dCTP deaminase (EC 3.5.4.13) (Deoxycytidine triphosphate deaminase) |
| [x] | `nrdB` | PP_1177 | Q88NN0 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Ribonucleoside-diphosphate reductase subunit beta (EC 1.17.4.1) |
| [x] | `nrdA` | PP_1179 | Q88NM8 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Ribonucleoside-diphosphate reductase (EC 1.17.4.1) |
| [x] | `ushA` | PP_1414 | Q88N04 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5'-nucleotidase-2',3'-cyclic phosphodiesterase (EC 3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) |
| [x] | `pyrH` | PP_1593 | Q88MH8 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Uridylate kinase (UK) (EC 2.7.4.22) (Uridine monophosphate kinase) (UMP kinase) (UMPK) |
| [x] | `pyrG` | PP_1610 | Q88MG1 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | CTP synthase (EC 6.3.4.2) (Cytidine 5'-triphosphate synthase) (Cytidine triphosphate synthetase) (CTP synthetase) (CTPS) |
| [x] | `surE` | PP_1620 | Q88MF1 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5'-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5'-monophosphate phosphohydrolase) |
| [x] | `mazG` | PP_1657 | Q88MB7 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) |
| [x] | `cmk` | PP_1771 | Q88M04 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Cytidylate kinase (CK) (EC 2.7.4.25) (Cytidine monophosphate kinase) (CMP kinase) |
| [x] | `pyrF` | PP_1815 | Q88LW2 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Orotidine 5'-phosphate decarboxylase (EC 4.1.1.23) (OMP decarboxylase) (OMPDCase) (OMPdecase) |
| [x] | `pyrD` | PP_2095 | Q88L40 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Dihydroorotate dehydrogenase (quinone) (EC 1.3.5.2) (DHOdehase) (DHOD) (DHODase) (Dihydroorotate oxidase) |
| [x] | `PP_2531` | PP_2531 | Q88JW6 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5-nucleotidase |
| [x] | `codA` | PP_3189 | Q88I13 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Cytosine deaminase / isoguanine deaminase (EC 3.5.4.-, EC 3.5.4.1) |
| [x] | `PP_3238` | PP_3238 | Q88HW5 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Transcriptional regulator PyrR |
| [x] | `PP_3662` | PP_3662 | Q88GQ6 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | AMP nucleosidase (EC 3.2.2.4) (AMP nucleosidase) |
| [x] | `hyuC` | PP_4034 | Q88FQ3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) |
| [x] | `pydB` | PP_4036 | A0A140FWK2 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) |
| [x] | `pydX` | PP_4037 | Q88FQ1 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [x] | `pydA` | PP_4038 | Q88FQ0 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [x] | `ppnP` | PP_4248 | Q88F51 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1) (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase)  |
| [x] | `carB` | PP_4723 | Q88DU6 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Carbamoyl phosphate synthase large chain (EC 6.3.4.16) (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) |
| [x] | `carA` | PP_4724 | Q88DU5 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Carbamoyl phosphate synthase small chain (EC 6.3.5.5) (Carbamoyl phosphate synthetase glutamine chain) |
| [x] | `ydfG` | PP_4862 | Q88DG3 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | 3-hydroxy acid dehydrogenase, NADP-dependent / malonic semialdehyde reductase (EC 1.1.1.276, EC 1.1.1.298) |
| [x] | `ygjP` | PP_4958 | Q88D69 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Metal-dependent hydrolase |
| [x] | `pyrR` | PP_4997 | Q88D31 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Pyrimidine operon regulatory protein/uracil phosphoribosyltransferase (EC 2.4.2.9) |
| [x] | `pyrB` | PP_4998 | Q88D30 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Aspartate carbamoyltransferase catalytic subunit (EC 2.1.3.2) (Aspartate transcarbamylase) (ATCase) |
| [x] | `pyrC'` | PP_4999 | Q88D29 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Dihydroorotase-like protein (EC 3.5.2.3) |
| [x] | `thyA` | PP_5141 | Q88CN9 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Thymidylate synthase (TS) (TSase) (EC 2.1.1.45) |
| [x] | `dut` | PP_5286 | Q88C95 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Deoxyuridine 5'-triphosphate nucleotidohydrolase (dUTPase) (EC 3.6.1.23) (dUTP pyrophosphatase) |
| [x] | `pyrE` | PP_5291 | Q88C92 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Orotate phosphoribosyltransferase (OPRT) (OPRTase) (EC 2.4.2.10) |

## Notes

Generated UTC: 2026-07-07T16:42:48.329464+00:00

### Workflow Notes

- Created and validated `modules/pyrimidine_metabolism.yaml`.
- Registered `kegg:ppu00240` in `projects/P_PUTIDA/build_pathway_worklist.py`
  as a broad pyrimidine-metabolism boundary module.
- Fetched 18 missing review folders. `pyrC'` required direct CLI fetch because
  `just fetch-gene` shell interpolation does not handle apostrophes safely:
  `uv run --no-dev ai-gene-review fetch-gene PSEPK "pyrC'" --uniprot-id Q88D29 --output-dir .`
- Ran Asta for 19 missing gene-level reports with `uv run python
  scripts/deep_research_wrapper.py PSEPK <gene> asta`; no provider retries were
  needed after using the project Python environment.
- Curated 18 pending or annotation-empty review YAMLs. The final batch has
  36/36 review folders present, 36/36 Asta reports present, and 36/36 reviews
  curated.
- Validated the module and all 36 candidate gene reviews. Warnings are limited
  to expected first-pass Asta-context notices, intentional no-core warnings for
  `PP_3238`, `ygjP`, and `pyrC'`, and the pre-existing `thyA` cytosol-location
  warning.
- Rendered all 36 gene pages. `pyrC'` required explicit render output to avoid
  the same apostrophe path issue:
  `uv run python -m ai_gene_review.render "genes/PSEPK/pyrC'/pyrC'-ai-review.yaml" -o "genes/PSEPK/pyrC'/pyrC'-ai-review.html"`.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon pyrimidine_metabolism` and
  `just module-pathway-deep-research-falcon pyrimidine_metabolism ppu00240 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/pyrimidine_metabolism-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__pyrimidine_metabolism__ppu00240-deep-research-falcon.md`.

### Curation Notes

- The strict de novo UMP route is covered by CarAB precursor supply, PyrB,
  PyrC, PyrD, PyrE, and PyrF.
- Downstream ribonucleotide branch coverage is represented by PyrH, Ndk, PyrG,
  and Cmk; the deoxypyrimidine/dTMP branch by NrdA/NrdB, Dcd, Dut, and ThyA.
- Salvage and recycling are represented by Upp, PyrR, PpnP, and broad
  nucleotidase/nucleoside-phosphorylase side nodes.
- Reductive pyrimidine catabolism and beta-alanine context are represented by
  PydA/PydX, PydB, HyuC/PP_0614, and YdfG.
- `pyrC'` is intentionally unresolved because GOA evidence mixes
  dihydroorotase/pyrimidine-biosynthesis and allantoinase/purine-catabolism
  interpretations; existing annotations were left `UNDECIDED`.
- `PP_3238` and `ygjP` remain conservative, annotation-empty candidate/context
  genes pending stronger evidence.
