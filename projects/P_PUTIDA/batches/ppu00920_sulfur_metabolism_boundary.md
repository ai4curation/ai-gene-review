---
title: "PSEPK ppu00920 Sulfur metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00920: Sulfur metabolism

- Module seed: `sulfur_metabolism_boundary`
- Candidate genes from membership table: 54
- Primary bucket genes: 33
- Existing review files: 54
- Curated review files: 54
- Existing Asta research files: 54

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
| [x] | `PP_0053` | PP_0053 | Q88RS6 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfide:quinone oxidoreductase |
| [x] | `PP_0170` | PP_0170 | Q88RG0 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ABC transporter, periplasmic binding protein |
| [x] | `PP_0171` | PP_0171 | Q88RF9 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ABC transporter, ATP-binding protein |
| [x] | `PP_0172` | PP_0172 | Q88RF8 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ABC transporter, permease protein |
| [x] | `PP_0207` | PP_0207 | Q88RC5 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_0208` | PP_0208 | Q88RC4 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Nitrate ABC transporter, permease protein |
| [x] | `tauB-I` | PP_0209 | Q88RC3 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ATP-binding taurine transporter subunit (EC 3.6.3.36) |
| [x] | `PP_0228` | PP_0228 | Q88RA5 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | serine O-acetyltransferase (EC 2.3.1.30) |
| [x] | `tauD` | PP_0230 | Q88RA3 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Alpha-ketoglutarate-dependent taurine dioxygenase (EC 1.14.11.17) |
| [x] | `tauC` | PP_0231 | Q88RA2 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Taurine ABC transporter permease subunit (EC 3.6.3.36) |
| [x] | `tauB` | PP_0232 | Q88RA1 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Taurine import ATP-binding protein TauB (EC 7.6.2.7) |
| [x] | `tauA` | PP_0233 | Q88RA0 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Taurine ABC transporter periplasmic binding subunit |
| [x] | `ssuE` | PP_0236 | Q88R97 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) |
| [x] | `ssuA` | PP_0237 | Q88R96 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `ssuD` | PP_0238 | Q88R95 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Alkanesulfonate monooxygenase (EC 1.14.14.5) (FMNH2-dependent aliphatic sulfonate monooxygenase) |
| [x] | `ssuC` | PP_0239 | Q88R94 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Aliphatic sulfonate ABC transporter-permease subunit / transport of isethionate |
| [x] | `ssuB` | PP_0240 | Q88R93 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Aliphatic sulfonates import ATP-binding protein SsuB (EC 7.6.2.14) |
| [x] | `cysQ` | PP_0261 | Q88R73 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | 3'(2'),5'-bisphosphate nucleotidase CysQ (EC 3.1.3.7) (3'(2'),5-bisphosphonucleoside 3'(2')-phosphohydrolase) (3'-phosph |
| [x] | `PP_0368` | PP_0368 | Q88QW6 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) |
| [x] | `PP_0370` | PP_0370 | Q88QW4 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) |
| [x] | `glpE` | PP_0398 | Q88QT9 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Thiosulfate sulfurtransferase GlpE (EC 2.8.1.1) |
| [x] | `metB` | PP_0659 | Q88Q39 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine gamma-synthase |
| [x] | `cysE` | PP_0840 | Q88PL0 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | serine O-acetyltransferase (EC 2.3.1.30) |
| [x] | `PP_0860` | PP_0860 | Q88PJ0 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Sulfite reductase, flavoprotein component |
| [x] | `PP_1110` | PP_1110 | Q88NU4 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | serine O-acetyltransferase (EC 2.3.1.30) |
| [x] | `cysD` | PP_1303 | Q88NA9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `cysNC` | PP_1304 | Q88NA8 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `PP_1703` | PP_1703 | Q88M71 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Assimilatory nitrate reductase/sulfite reductase (EC 1.7.99.4) |
| [x] | `metZ` | PP_2001 | Q88LD4 | kegg:ppu00270 | PRESENT | CURATED | PRESENT | O-succinylhomoserine sulfhydrylase (OSH sulfhydrylase) (OSHS sulfhydrylase) (EC 2.5.1.-) |
| [x] | `PP_2048` | PP_2048 | Q88L87 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) |
| [x] | `cysH` | PP_2328 | Q88KG2 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Adenosine 5'-phosphosulfate reductase (APS reductase) (EC 1.8.4.10) (5'-adenylylsulfate reductase) (Thioredoxin-dependen |
| [x] | `cysI` | PP_2371 | Q88KB9 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Sulphite reductase hemoprotein, beta subunit |
| [x] | `PP_2677` | PP_2677 | Q88JH2 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Quinoprotein dehydrogenase-associated SoxYZ-like carrier |
| [x] | `msuE` | PP_2764 | Q88J85 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) |
| [x] | `PP_2765` | PP_2765 | Q88J84 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfonate monooxygenase MsuD |
| [x] | `PP_2795` | PP_2795 | Q88J54 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | AMP-binding domain protein |
| [x] | `PP_3136` | PP_3136 | Q88I65 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Serine acetyltransferase (EC 2.3.1.30) |
| [x] | `PP_3217` | PP_3217 | Q88HY6 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_3219` | PP_3219 | Q88HY4 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Alkansulfonate monooxygenase |
| [x] | `PP_3228` | PP_3228 | Q88HX5 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_3229` | PP_3229 | Q88HX4 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_3528` | PP_3528 | Q88H37 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_3553` | PP_3553 | Q88H12 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | AMP-binding domain protein |
| [x] | `PP_3554` | PP_3554 | Q88H11 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) |
| [x] | `PP_3822` | PP_3822 | Q88GA3 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Cytochrome c family protein |
| [x] | `sbp-I` | PP_4305 | Q88EZ5 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate ABC transporter |
| [x] | `cysK` | PP_4571 | Q88E95 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Cysteine synthase (EC 2.5.1.47) |
| [x] | `rhdA` | PP_4907 | Q88DC0 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfurtransferase |
| [x] | `metXS` | PP_5097 | Q88CT3 | kegg:ppu00270 | PRESENT | CURATED | PRESENT | Homoserine O-succinyltransferase (HST) (EC 2.3.1.46) (Homoserine transsuccinylase) (HTS) |
| [x] | `sseA` | PP_5118 | Q88CR2 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) |
| [x] | `cysA` | PP_5168 | Q88CL2 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate/thiosulfate import ATP-binding protein CysA (EC 7.3.2.3) (Sulfate-transporting ATPase) |
| [x] | `cysW` | PP_5169 | Q88CL1 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate transport system permease protein CysW |
| [x] | `cysU` | PP_5170 | Q88CL0 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate transport system permease protein CysT |
| [x] | `sbp-II` | PP_5171 | Q88CK9 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate ABC transporter |

## Notes

Generated UTC: 2026-07-08T16:55:18.089385+00:00

2026-07-11 PDT status sync: `modules/sulfur_metabolism_boundary.yaml` is curated and validates with both module validators. The ppu00920 batch TSV has 54/54 review files, 54/54 Asta reports, and 54/54 review YAMLs with no `PENDING` actions. The module records sulfur metabolism as a boundary across sulfate/thiosulfate import and assimilation, cystine/sulfur-compound ABC import, taurine/alkanesulfonate acquisition, sulfur redox/electron-transfer side nodes, sulfurtransferases, methionine/cysteine side chemistry, and organosulfur CoA/AMP candidates rather than one monolithic pathway.

Real Falcon commands were run:

```bash
just module-deep-research-falcon sulfur_metabolism_boundary
just module-pathway-deep-research-falcon sulfur_metabolism_boundary ppu00920 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/sulfur_metabolism_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__sulfur_metabolism_boundary__ppu00920-deep-research-falcon.md`
