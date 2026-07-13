---
title: "PSEPK ppu00310 Lysine degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00310: Lysine degradation

- Module seed: `lysine_degradation`
- Candidate genes from membership table: 32
- Primary bucket genes: 13
- Existing review files: 32
- Curated review files: 32
- Existing Asta research files: 32

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
| [x] | `gcdH` | PP_0158 | Q88RH2 | kegg:ppu00380 | PRESENT | CURATED | PRESENT | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) |
| [x] | `PP_0159` | PP_0159 | Q88RH1 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | CoA-transferase family III (EC 2.8.3.-) |
| [x] | `davD` | PP_0213 | Q88RC0 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) |
| [x] | `davT` | PP_0214 | Q88RB9 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | 5-aminovalerate aminotransferase DavT (EC 2.6.1.48) (5-aminovalerate transaminase) (Delta-aminovalerate aminotransferase |
| [x] | `davA` | PP_0382 | Q88QV2 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | 5-aminopentanamidase (EC 3.5.1.30) |
| [x] | `davB` | PP_0383 | Q88QV1 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | Tryptophan 2-monooxygenase (EC 1.13.12.3) |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `patD` | PP_1481 | Q88MT7 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC 1.2.1.54) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `sad-I` | PP_2488 | Q88K05 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `prr` | PP_2801 | Q88J48 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19) |
| [x] | `glaH` | PP_2909 | Q88IU0 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | Glutarate 2-hydroxylase (G-2-H) (EC 1.14.11.64) |
| [x] | `lhgO` | PP_2910 | Q88IT9 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | L-2-hydroxyglutarate oxidase (EC 1.1.3.15) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `dpkA` | PP_3591 | Q88GX6 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | Delta(1)-pyrroline-2-carboxylate/Delta(1)-piperideine-2-carboxylate reductase (EC 1.5.1.21) |
| [x] | `amaD` | PP_3596 | Q88GX1 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | D-lysine oxidase (EC 1.4.3.-) |
| [x] | `alr` | PP_3722 | Q88GJ9 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Broad specificity amino-acid racemase (EC 5.1.1.10) (Broad spectrum racemase) |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `PP_4108` | PP_4108 | Q88FI7 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | 2-aminoadipate transaminase (EC 2.6.1.39) (2-aminoadipate aminotransferase) (L-2AA aminotransferase) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `sucB` | PP_4188 | Q88FB0 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxogl |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `gabD-II` | PP_4422 | Q88EN2 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) |
| [x] | `ydiJ` | PP_4493 | Q88EH0 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | D-2-hydroxyglutarate dehydrogenase (D2HGDH) (EC 1.1.99.39) |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `amaA` | PP_5257 | Q88CC4 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | L-pipecolate oxidase (EC 1.5.3.7) |
| [x] | `amaB` | PP_5258 | Q88CC3 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | aldehyde dehydrogenase (NAD(+)) (EC 1.2.1.3) |
| [x] | `hglS` | PP_5260 | Q88CC1 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | 2-oxoadipate dioxygenase/decarboxylase (EC 1.13.11.93) (2-hydroxyglutarate synthase) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-07T20:09:47.569831+00:00

Workflow notes:

- Created and validated `modules/lysine_degradation.yaml`.
- Refreshed the pathway worklist and extracted 32 KEGG `ppu00310` membership genes.
- Fetched the previously missing review folders for PP_0159, davA, davB, patD, prr,
  lhgO, dpkA, amaD, PP_4108, amaA, and amaB.
- Ran Asta for the 14 genes that lacked provider files at batch start: the 11 new
  folders plus glaH, ydiJ, and hglS.
- Full 32-gene validation completed with no errors. The remaining 16 warnings are
  inherited Asta-citation notices on older boundary reviews: PP_0582, PP_2215,
  PP_2217, PP_3355, bktB, davD, davT, gabD-II, gcdH, lpd, lpdG, lpdV, paaF,
  sad-I, sucB, and yqeF.
- Rendered all 32 gene review pages.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon lysine_degradation` and
  `just module-pathway-deep-research-falcon lysine_degradation ppu00310 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/lysine_degradation-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__lysine_degradation__ppu00310-deep-research-falcon.md`.

Curation notes:

- The strict L-lysine-to-glutarate Dav route is davB, davA, davT, and davD.
- GlaH/CsiD and LhgO define the CoA-independent glutarate/L-2-hydroxyglutarate
  branch connected to L-lysine catabolism.
- PP_4108, hglS, ydiJ, amaD, amaA, amaB, dpkA, and alr are D-lysine,
  2-aminoadipate, D-2-hydroxyglutarate, and pipecolate side-route context.
- PP_0159 is retained as unresolved CoA-transferase/glutarate boundary context.
- PatD, Prr, GabD-II, Sad-I, beta-oxidation enzymes, thiolases, and lipoamide
  enzymes are cross-bucket aldehyde, GABA, beta-oxidation, or central-carbon
  spillovers unless future evidence supports a committed lysine-catabolic role.
