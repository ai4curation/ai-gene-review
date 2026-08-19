---
title: "PSEPK ppu00230 Purine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00230: Purine metabolism

- Module seed: `bacterial_purine_salvage`
- Candidate genes from membership table: 65
- Primary bucket genes: 36
- Existing review files: 24
- Curated review files: 21
- Existing OpenScientist research files: 5

## Curation Boundary

This batch inventory preserves all 65 KEGG purine-metabolism members for
provenance, but the PpnP-linked salvage realization selects four catalytic
genes: `ppnP`, `apt`, `PP_0747`, and `xpt`. Purine transporters, de novo
synthesis, nucleotide interconversion, and oxidative degradation are assigned
to separate modules. `yfiH` is curated as a boundary false positive: direct
YfiH/PgeF evidence and its PTHR30616:SF2 family support peptidoglycan precursor
editing as the bacterial core function. Weak family-level PNP activity is real
in vitro, but recent genetic and kinetic evidence does not support using it to
satisfy physiological purine salvage.

The species-aware report also nominated `PP_3254` as a possible unrecognized
classical phosphorylase because it contains PF01048. Targeted review places it
in PTHR46832:SF1 with MTA/SAH **nucleosidase** activities, so it is a
sulfur-metabolite recycling boundary gene rather than a substitute for PpnP.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2637](https://github.com/ai4curation/ai-gene-review/pull/2637).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Satisfiability Assessment

| Module step | PSEPK assignment | Status | Evidence boundary |
|---|---|---|---|
| Purine nucleoside phosphorolysis | `ppnP` / PP_4248 | covered, family-inferred | Exact PpnP family and reviewed UniProt assignment; direct KT2440 flux evidence is absent. |
| Adenine to AMP | `apt` / PP_4266 | covered | Exact APRT family, HAMAP rule, and reviewed UniProt reaction assignment. |
| Hypoxanthine/guanine to IMP/GMP | `PP_0747` | candidate uncertain | Exact HGPRT family supports both reactions, but Q88PV1 is unreviewed and lacks a direct assay. |
| Xanthine to XMP | `xpt` / PP_5265 | covered, family-inferred | Exact Xpt subfamily, HAMAP rule, and reviewed UniProt reaction assignment. |

`yfiH` is excluded because its physiological bacterial role is peptidoglycan
precursor editing. `PP_3254` is excluded because it is an MtnN-family
MTA/SAH nucleosidase rather than a phosphate-dependent PNP.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `yrfG` | PP_0259 | Q88R75 | kegg:ppu00230 | MISSING | MISSING | MISSING | Purine nucleotidase (EC 3.1.3.5) |
| [ ] | `nudE` | PP_0260 | Q88R74 | kegg:ppu00230 | MISSING | MISSING | MISSING | ADP-sugar pyrophosphorylase (EC 3.6.1.21) |
| [ ] | `apaH` | PP_0399 | Q88QT8 | kegg:ppu00230 | PRESENT | CURATED | MISSING | Bis(5'-nucleosyl)-tetraphosphatase, symmetrical (EC 3.6.1.41) (Ap4A hydrolase) (Diadenosine 5',5'''-P1,P4-tetraphosphate |
| [ ] | `PP_0591` | PP_0591 | Q88QA3 | kegg:ppu00230 | MISSING | MISSING | MISSING | Adenine deaminase (ADE) (EC 3.5.4.2) (Adenine aminohydrolase) (AAH) |
| [x] | `yfiH` | PP_0624 | Q88Q72 | kegg:ppu00270 | MISSING | MISSING | MISSING | Purine nucleoside phosphorylase |
| [ ] | `prs` | PP_0722 | Q88PX6 | kegg:ppu00030 | PRESENT | CURATED | MISSING | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosy |
| [x] | `PP_0747` | PP_0747 | Q88PV1 | kegg:ppu00230 | PRESENT | PENDING | MISSING | Hypoxanthine-guanine phosphoribosyltransferase |
| [ ] | `ndk` | PP_0849 | Q88PK1 | kegg:ppu00240 | MISSING | MISSING | MISSING | Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC 2.7.4.6) (Nucleoside-2-P kinase) |
| [ ] | `arcC` | PP_0999 | Q88P54 | kegg:ppu00910 | MISSING | MISSING | MISSING | Carbamate kinase |
| [ ] | `guaB` | PP_1031 | Q88P22 | kegg:ppu00230 | MISSING | MISSING | MISSING | Inosine-5'-monophosphate dehydrogenase (IMP dehydrogenase) (IMPD) (IMPDH) (EC 1.1.1.205) |
| [ ] | `guaA` | PP_1032 | Q88P21 | kegg:ppu00230 | MISSING | MISSING | MISSING | GMP synthase [glutamine-hydrolyzing] (EC 6.3.5.2) (GMP synthetase) (Glutamine amidotransferase) |
| [ ] | `purL` | PP_1037 | Q88P16 | kegg:ppu00230 | PRESENT | CURATED | MISSING | Phosphoribosylformylglycinamidine synthase (FGAM synthase) (FGAMS) (EC 6.3.5.3) (Formylglycinamide ribonucleotide amidot |
| [ ] | `nrdB` | PP_1177 | Q88NN0 | kegg:ppu00240 | MISSING | MISSING | MISSING | Ribonucleoside-diphosphate reductase subunit beta (EC 1.17.4.1) |
| [ ] | `nrdA` | PP_1179 | Q88NM8 | kegg:ppu00240 | MISSING | MISSING | MISSING | Ribonucleoside-diphosphate reductase (EC 1.17.4.1) |
| [x] | `purC` | PP_1240 | Q88NG9 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Phosphoribosylaminoimidazole-succinocarboxamide synthase (EC 6.3.2.6) (SAICAR synthetase) |
| [ ] | `cysD` | PP_1303 | Q88NA9 | kegg:ppu00261 | PRESENT | CURATED | MISSING | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) |
| [ ] | `cysNC` | PP_1304 | Q88NA8 | kegg:ppu00261 | PRESENT | CURATED | MISSING | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) |
| [ ] | `ushA` | PP_1414 | Q88N04 | kegg:ppu00760 | MISSING | MISSING | MISSING | 5'-nucleotidase-2',3'-cyclic phosphodiesterase (EC 3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) |
| [ ] | `purT` | PP_1457 | Q88MW1 | kegg:ppu00230 | PRESENT | CURATED | MISSING | Formate-dependent phosphoribosylglycinamide formyltransferase (EC 6.3.1.21) (5'-phosphoribosylglycinamide transformylase |
| [ ] | `adk` | PP_1506 | P0A136 | kegg:ppu00730 | MISSING | MISSING | MISSING | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate ki |
| [ ] | `surE` | PP_1620 | Q88MF1 | kegg:ppu00760 | MISSING | MISSING | MISSING | 5'-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5'-monophosphate phosphohydrolase) |
| [ ] | `relA` | PP_1656 | Q88MB8 | kegg:ppu00230 | PRESENT | CURATED | MISSING | GTP pyrophosphokinase ((p)ppGpp synthase) (ATP:GTP 3'-pyrophosphotransferase) (ppGpp synthase I) |
| [x] | `mazG` | PP_1657 | Q88MB7 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) |
| [x] | `purN` | PP_1664 | Q88MB0 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2) (5'-phosphoribosylglycinamide transformylase) (GAR transformyla |
| [ ] | `purM` | PP_1665 | Q88MA9 | kegg:ppu00230 | PRESENT | CURATED | MISSING | Phosphoribosylformylglycinamidine cyclo-ligase (EC 6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthet |
| [ ] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | MISSING | phosphomannomutase (EC 5.4.2.8) |
| [x] | `purF` | PP_2000 | Q88LD5 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14) (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase) |
| [ ] | `dgt` | PP_2102 | Q88L33 | kegg:ppu00230 | MISSING | MISSING | MISSING | Deoxyguanosinetriphosphate triphosphohydrolase-like protein |
| [ ] | `PP_2531` | PP_2531 | Q88JW6 | kegg:ppu00760 | MISSING | MISSING | MISSING | 5-nucleotidase |
| [ ] | `PP_2744` | PP_2744 | Q88JA5 | kegg:ppu00030 | MISSING | MISSING | MISSING | ribose-phosphate diphosphokinase (EC 2.7.6.1) |
| [ ] | `ureA` | PP_2843 | Q88J06 | kegg:ppu00220 | MISSING | MISSING | MISSING | Urease subunit gamma (EC 3.5.1.5) (Urea amidohydrolase subunit gamma) |
| [ ] | `ureB` | PP_2844 | Q88J05 | kegg:ppu00220 | MISSING | MISSING | MISSING | Urease subunit beta (EC 3.5.1.5) (Urea amidohydrolase subunit beta) |
| [ ] | `ureC` | PP_2845 | Q88J04 | kegg:ppu00220 | MISSING | MISSING | MISSING | Urease subunit alpha (EC 3.5.1.5) (Urea amidohydrolase subunit alpha) |
| [ ] | `paoA` | PP_3308 | Q88HP5 | kegg:ppu00230 | MISSING | MISSING | MISSING | Promiscuous aromatic aldehyde dehydrogenase, 2Fe-2S subunit (EC 1.2.99.7) |
| [ ] | `paoB` | PP_3309 | Q88HP4 | kegg:ppu00230 | MISSING | MISSING | MISSING | Promiscuous aromatic aldehyde dehydrogenase, FAD-binding subunit (EC 1.2.99.7) |
| [ ] | `paoC` | PP_3310 | Q88HP3 | kegg:ppu00230 | MISSING | MISSING | MISSING | Promiscuous aromatic aldehyde dehydrogenase, molybdopterin-binding subunit (EC 1.2.99.7) |
| [ ] | `allE` | PP_3530 | Q88H35 | kegg:ppu00230 | MISSING | MISSING | MISSING | S-ureidoglycine aminohydrolase (EC 3.5.3.-) |
| [ ] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Phosphoglucomutase (EC 5.4.2.2) |
| [ ] | `PP_3662` | PP_3662 | Q88GQ6 | kegg:ppu00240 | MISSING | MISSING | MISSING | AMP nucleosidase (EC 3.2.2.4) (AMP nucleosidase) |
| [ ] | `purB` | PP_4016 | Q88FR7 | kegg:ppu00250 | PRESENT | CURATED | MISSING | Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase) |
| [x] | `ppnP` | PP_4248 | Q88F51 | kegg:ppu00240 | PRESENT | CURATED | MISSING | Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1) (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase)  |
| [x] | `apt` | PP_4266 | Q88F33 | kegg:ppu00230 | PRESENT | PENDING | MISSING | Adenine phosphoribosyltransferase (APRT) (EC 2.4.2.7) |
| [ ] | `xdhA` | PP_4278 | Q88F21 | kegg:ppu00230 | MISSING | MISSING | MISSING | Xanthine dehydrogenase subunit XdhA (EC 1.17.1.4) |
| [ ] | `xdhB` | PP_4279 | Q88F20 | kegg:ppu00230 | MISSING | MISSING | MISSING | Xanthine dehydrogenase subunit XdhB (EC 1.17.1.4) |
| [ ] | `guaD` | PP_4281 | Q88F18 | kegg:ppu00230 | MISSING | MISSING | MISSING | Guanine deaminase (Guanase) (EC 3.5.4.3) (Guanine aminohydrolase) |
| [ ] | `pucM` | PP_4285 | Q88F14 | kegg:ppu00230 | MISSING | MISSING | MISSING | 5-hydroxyisourate hydrolase (HIU hydrolase) (HIUHase) (EC 3.5.2.17) |
| [ ] | `puuE` | PP_4286 | Q88F13 | kegg:ppu00230 | MISSING | MISSING | MISSING | Allantoinase (EC 3.5.2.5) |
| [ ] | `pucL` | PP_4287 | Q88F12 | kegg:ppu00230 | MISSING | MISSING | MISSING | 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline decarboxylase (EC 4.1.1.97) |
| [ ] | `allA` | PP_4288 | P59285 | kegg:ppu00230 | MISSING | MISSING | MISSING | Ureidoglycolate lyase (EC 4.3.2.3) (Ureidoglycolatase) |
| [ ] | `PP_4310` | PP_4310 | Q88EZ0 | kegg:ppu00230 | MISSING | MISSING | MISSING | Hydantoin racemase (EC 5.1.99.5) |
| [ ] | `amn` | PP_4779 | Q88DP5 | kegg:ppu00230 | MISSING | MISSING | MISSING | AMP nucleosidase (EC 3.2.2.4) |
| [ ] | `purH` | PP_4822 | Q88DK3 | kegg:ppu00670 | PRESENT | CURATED | MISSING | Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2 |
| [x] | `purD` | PP_4823 | Q88DK2 | kegg:ppu00230 | PRESENT | CURATED | PRESENT | Phosphoribosylamine--glycine ligase (EC 6.3.4.13) (GARS) (Glycinamide ribonucleotide synthetase) (Phosphoribosylglycinam |
| [ ] | `purA` | PP_4889 | Q88DD8 | kegg:ppu00250 | MISSING | MISSING | MISSING | Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4) (IMP--aspartate ligase) |
| [ ] | `pde` | PP_4917 | Q88DB0 | kegg:ppu02025 | MISSING | MISSING | MISSING | 3',5'-cyclic-nucleotide phosphodiesterase (EC 3.1.4.17) |
| [ ] | `nudF` | PP_4919 | Q88DA8 | kegg:ppu00740 | MISSING | MISSING | MISSING | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphori |
| [ ] | `PP_5100` | PP_5100 | Q88CT0 | kegg:ppu00230 | MISSING | MISSING | MISSING | dITP/XTP pyrophosphatase (EC 3.6.1.66) (Non-canonical purine NTP pyrophosphatase) (Non-standard purine NTP pyrophosphata |
| [ ] | `ppx` | PP_5216 | Q88CG5 | kegg:ppu00230 | MISSING | MISSING | MISSING | Exopolyphosphatase (EC 3.6.1.11) |
| [ ] | `cyaA` | PP_5222 | Q88CF9 | kegg:ppu00230 | MISSING | MISSING | MISSING | Adenylate cyclase (EC 4.6.1.1, EC 4.6.1.6) |
| [x] | `xpt` | PP_5265 | Q88CB6 | kegg:ppu00230 | PRESENT | PENDING | MISSING | Xanthine phosphoribosyltransferase (XPRTase) (EC 2.4.2.22) |
| [ ] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |
| [ ] | `gmk` | PP_5296 | Q88C87 | kegg:ppu00230 | MISSING | MISSING | MISSING | Guanylate kinase (EC 2.7.4.8) (GMP kinase) |
| [ ] | `spoT` | PP_5302 | Q88C81 | kegg:ppu00230 | MISSING | MISSING | MISSING | guanosine-3',5'-bis(diphosphate) 3'-diphosphatase (EC 3.1.7.2) |
| [ ] | `purK` | PP_5335 | Q88C48 | kegg:ppu00230 | PRESENT | CURATED | MISSING | N5-carboxyaminoimidazole ribonucleotide synthase (N5-CAIR synthase) (EC 6.3.4.18) (5-(carboxyamino)imidazole ribonucleot |
| [ ] | `purE` | PP_5336 | Q88C47 | kegg:ppu00230 | PRESENT | CURATED | MISSING | N5-carboxyaminoimidazole ribonucleotide mutase (N5-CAIR mutase) (EC 5.4.99.18) (5-(carboxyamino)imidazole ribonucleotide |

## Notes

Generated UTC: 2026-08-13T15:16:00.996332+00:00
