---
title: "PSEPK ppu00230 Purine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00230: Purine metabolism

- Module seed: `purine_metabolism`
- Candidate genes from membership table: 65
- Primary bucket genes: 36
- Existing review files: 65
- Curated review files: 65
- Existing Asta research files: 65

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
| [x] | `yrfG` | PP_0259 | Q88R75 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Purine nucleotidase (EC 3.1.3.5) |
| [x] | `nudE` | PP_0260 | Q88R74 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | ADP-sugar pyrophosphorylase (EC 3.6.1.21) |
| [x] | `apaH` | PP_0399 | Q88QT8 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Bis(5'-nucleosyl)-tetraphosphatase, symmetrical (EC 3.6.1.41) (Ap4A hydrolase) (Diadenosine 5',5'''-P1,P4-tetraphosphate |
| [x] | `PP_0591` | PP_0591 | Q88QA3 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Adenine deaminase (ADE) (EC 3.5.4.2) (Adenine aminohydrolase) (AAH) |
| [x] | `yfiH` | PP_0624 | Q88Q72 | kegg:ppu00270 | PRESENT | CURATED | PRESENT | Purine nucleoside phosphorylase |
| [x] | `prs` | PP_0722 | Q88PX6 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosy |
| [x] | `PP_0747` | PP_0747 | Q88PV1 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Hypoxanthine-guanine phosphoribosyltransferase |
| [x] | `ndk` | PP_0849 | Q88PK1 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC 2.7.4.6) (Nucleoside-2-P kinase) |
| [x] | `arcC` | PP_0999 | Q88P54 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Carbamate kinase |
| [x] | `guaB` | PP_1031 | Q88P22 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Inosine-5'-monophosphate dehydrogenase (IMP dehydrogenase) (IMPD) (IMPDH) (EC 1.1.1.205) |
| [x] | `guaA` | PP_1032 | Q88P21 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | GMP synthase [glutamine-hydrolyzing] (EC 6.3.5.2) (GMP synthetase) (Glutamine amidotransferase) |
| [x] | `purL` | PP_1037 | Q88P16 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Phosphoribosylformylglycinamidine synthase (FGAM synthase) (FGAMS) (EC 6.3.5.3) (Formylglycinamide ribonucleotide amidot |
| [x] | `nrdB` | PP_1177 | Q88NN0 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Ribonucleoside-diphosphate reductase subunit beta (EC 1.17.4.1) |
| [x] | `nrdA` | PP_1179 | Q88NM8 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Ribonucleoside-diphosphate reductase (EC 1.17.4.1) |
| [x] | `purC` | PP_1240 | Q88NG9 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Phosphoribosylaminoimidazole-succinocarboxamide synthase (EC 6.3.2.6) (SAICAR synthetase) |
| [x] | `cysD` | PP_1303 | Q88NA9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `cysNC` | PP_1304 | Q88NA8 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `ushA` | PP_1414 | Q88N04 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5'-nucleotidase-2',3'-cyclic phosphodiesterase (EC 3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) |
| [x] | `purT` | PP_1457 | Q88MW1 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Formate-dependent phosphoribosylglycinamide formyltransferase (EC 6.3.1.21) (5'-phosphoribosylglycinamide transformylase |
| [x] | `adk` | PP_1506 | P0A136 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate ki |
| [x] | `surE` | PP_1620 | Q88MF1 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5'-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5'-monophosphate phosphohydrolase) |
| [x] | `relA` | PP_1656 | Q88MB8 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | GTP pyrophosphokinase ((p)ppGpp synthase) (ATP:GTP 3'-pyrophosphotransferase) (ppGpp synthase I) |
| [x] | `mazG` | PP_1657 | Q88MB7 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) |
| [x] | `purN` | PP_1664 | Q88MB0 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2) (5'-phosphoribosylglycinamide transformylase) (GAR transformyla |
| [x] | `purM` | PP_1665 | Q88MA9 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Phosphoribosylformylglycinamidine cyclo-ligase (EC 6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthet |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | phosphomannomutase (EC 5.4.2.8) |
| [x] | `purF` | PP_2000 | Q88LD5 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14) (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase) |
| [x] | `dgt` | PP_2102 | Q88L33 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Deoxyguanosinetriphosphate triphosphohydrolase-like protein |
| [x] | `PP_2531` | PP_2531 | Q88JW6 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5-nucleotidase |
| [x] | `PP_2744` | PP_2744 | Q88JA5 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | ribose-phosphate diphosphokinase (EC 2.7.6.1) |
| [x] | `ureA` | PP_2843 | Q88J06 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Urease subunit gamma (EC 3.5.1.5) (Urea amidohydrolase subunit gamma) |
| [x] | `ureB` | PP_2844 | Q88J05 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Urease subunit beta (EC 3.5.1.5) (Urea amidohydrolase subunit beta) |
| [x] | `ureC` | PP_2845 | Q88J04 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Urease subunit alpha (EC 3.5.1.5) (Urea amidohydrolase subunit alpha) |
| [x] | `paoA` | PP_3308 | Q88HP5 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Promiscuous aromatic aldehyde dehydrogenase, 2Fe-2S subunit (EC 1.2.99.7) |
| [x] | `paoB` | PP_3309 | Q88HP4 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Promiscuous aromatic aldehyde dehydrogenase, FAD-binding subunit (EC 1.2.99.7) |
| [x] | `paoC` | PP_3310 | Q88HP3 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Promiscuous aromatic aldehyde dehydrogenase, molybdopterin-binding subunit (EC 1.2.99.7) |
| [x] | `allE` | PP_3530 | Q88H35 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | S-ureidoglycine aminohydrolase (EC 3.5.3.-) |
| [x] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `PP_3662` | PP_3662 | Q88GQ6 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | AMP nucleosidase (EC 3.2.2.4) (AMP nucleosidase) |
| [x] | `purB` | PP_4016 | Q88FR7 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase) |
| [x] | `ppnP` | PP_4248 | Q88F51 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1) (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase)  |
| [x] | `apt` | PP_4266 | Q88F33 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Adenine phosphoribosyltransferase (APRT) (EC 2.4.2.7) |
| [x] | `xdhA` | PP_4278 | Q88F21 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Xanthine dehydrogenase subunit XdhA (EC 1.17.1.4) |
| [x] | `xdhB` | PP_4279 | Q88F20 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Xanthine dehydrogenase subunit XdhB (EC 1.17.1.4) |
| [x] | `guaD` | PP_4281 | Q88F18 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Guanine deaminase (Guanase) (EC 3.5.4.3) (Guanine aminohydrolase) |
| [x] | `pucM` | PP_4285 | Q88F14 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | 5-hydroxyisourate hydrolase (HIU hydrolase) (HIUHase) (EC 3.5.2.17) |
| [x] | `puuE` | PP_4286 | Q88F13 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Allantoinase (EC 3.5.2.5) |
| [x] | `pucL` | PP_4287 | Q88F12 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline decarboxylase (EC 4.1.1.97) |
| [x] | `allA` | PP_4288 | P59285 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Ureidoglycolate lyase (EC 4.3.2.3) (Ureidoglycolatase) |
| [x] | `PP_4310` | PP_4310 | Q88EZ0 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Hydantoin racemase (EC 5.1.99.5) |
| [x] | `amn` | PP_4779 | Q88DP5 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | AMP nucleosidase (EC 3.2.2.4) |
| [x] | `purH` | PP_4822 | Q88DK3 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2 |
| [x] | `purD` | PP_4823 | Q88DK2 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Phosphoribosylamine--glycine ligase (EC 6.3.4.13) (GARS) (Glycinamide ribonucleotide synthetase) (Phosphoribosylglycinam |
| [x] | `purA` | PP_4889 | Q88DD8 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4) (IMP--aspartate ligase) |
| [x] | `pde` | PP_4917 | Q88DB0 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | 3',5'-cyclic-nucleotide phosphodiesterase (EC 3.1.4.17) |
| [x] | `nudF` | PP_4919 | Q88DA8 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphori |
| [x] | `PP_5100` | PP_5100 | Q88CT0 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | dITP/XTP pyrophosphatase (EC 3.6.1.66) (Non-canonical purine NTP pyrophosphatase) (Non-standard purine NTP pyrophosphata |
| [x] | `ppx` | PP_5216 | Q88CG5 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Exopolyphosphatase (EC 3.6.1.11) |
| [x] | `cyaA` | PP_5222 | Q88CF9 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Adenylate cyclase (EC 4.6.1.1, EC 4.6.1.6) |
| [x] | `xpt` | PP_5265 | Q88CB6 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Xanthine phosphoribosyltransferase (XPRTase) (EC 2.4.2.22) |
| [x] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |
| [x] | `gmk` | PP_5296 | Q88C87 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Guanylate kinase (EC 2.7.4.8) (GMP kinase) |
| [x] | `spoT` | PP_5302 | Q88C81 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | guanosine-3',5'-bis(diphosphate) 3'-diphosphatase (EC 3.1.7.2) |
| [x] | `purK` | PP_5335 | Q88C48 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | N5-carboxyaminoimidazole ribonucleotide synthase (N5-CAIR synthase) (EC 6.3.4.18) (5-(carboxyamino)imidazole ribonucleot |
| [x] | `purE` | PP_5336 | Q88C47 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | N5-carboxyaminoimidazole ribonucleotide mutase (N5-CAIR mutase) (EC 5.4.99.18) (5-(carboxyamino)imidazole ribonucleotide |

## Notes

## Workflow Notes

- Created and validated `modules/purine_metabolism.yaml`.
- Registered `kegg:ppu00230` in the pathway worklist as a broad
  `purine_metabolism` boundary module.
- Fetched the 44 missing review folders and ran Asta for the 47 genes that
  lacked `*-deep-research-asta.md`; `pde` succeeded on the single retry after a
  transient Asta internal-server error.
- Curated the 44 pending review YAMLs; all 65 batch genes now have no
  `PENDING` actions.
- Validated all 65 gene reviews and rendered all 65 gene review pages.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon purine_metabolism` and
  `just module-pathway-deep-research-falcon purine_metabolism ppu00230 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/purine_metabolism-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__purine_metabolism__ppu00230-deep-research-falcon.md`.

## Curation Notes

- Treat ppu00230 as a broad purine-metabolism map with separate de novo IMP,
  AMP/GMP branch, salvage, catabolism, nucleotide-housekeeping, and signaling
  components.
- Strict de novo/branch coverage is PurF, PurD, PurN/PurT, PurL, PurM, PurK,
  PurE, PurC, PurB, PurH, PurA, GuaB, and GuaA.
- Salvage and pool-maintenance context includes PP_0747, Apt, Xpt, Amn,
  PP_3662, PpnP, YfiH, Ndk, Gmk, Dgt, PP_5100, ApaH, NudE/NudF, Ppx, CyaA,
  RelA, and SpoT.
- Catabolism is PP_0591, GuaD, XdhA/XdhB, PucM, PucL, PuuE, AllE, and AllA.
  PaoABC remains boundary xanthine/aldehyde-oxidoreductase context pending
  stronger evidence for a dedicated purine-catabolic role.
- Removed or rejected clear electronic spillovers: `purC` cobalamin
  biosynthesis, `purM` PurD/GAR-synthetase activity, `puuE` carbohydrate
  metabolism, and `yrfG` DNA repair/phosphoglycolate phosphatase.

Generated UTC: 2026-07-07T16:14:28.939609+00:00
