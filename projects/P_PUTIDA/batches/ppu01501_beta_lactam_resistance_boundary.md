---
title: "PSEPK ppu01501 beta-Lactam resistance batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01501: beta-Lactam resistance

- Module seed: `beta_lactam_resistance_boundary`
- Candidate genes from membership table: 20
- Primary bucket genes: 20
- Existing review files: 20
- Curated review files: 20
- Existing Asta research files: 20

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
| [x] | `PP_0906` | PP_0906 | Q88PE4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Multidrug efflux RND transporter |
| [x] | `PP_0907` | PP_0907 | Q88PE3 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | RND efflux membrane fusion protein-related protein |
| [x] | `oprD` | PP_1206 | Q88NK1 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Basic-amino-acid specific porin OprD (EC 3.4.21.-) |
| [x] | `PP_1263` | PP_1263 | Q88NE9 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Fusaric acid resistance protein |
| [x] | `ftsI` | PP_1331 | Q88N82 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase FtsI (EC 3.4.16.4) (Penicillin-binding protein 3) (PBP-3) |
| [x] | `ampG` | PP_1355 | Q88N61 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Muropeptide permease AmpG |
| [x] | `ttgC` | PP_1384 | Q88N32 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Probable efflux pump outer membrane protein TtgC |
| [x] | `ttgB` | PP_1385 | Q88N31 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Probable efflux pump membrane transporter TtgB |
| [x] | `ttgA` | PP_1386 | Q88N30 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Probable efflux pump periplasmic linker TtgA |
| [x] | `PP_1798` | PP_1798 | Q88LX9 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Outer membrane efflux protein |
| [x] | `nagZ` | PP_2145 | Q88KZ4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Beta-hexosaminidase (EC 3.2.1.52) (Beta-N-acetylhexosaminidase) (N-acetyl-beta-glucosaminidase) |
| [x] | `ampC` | PP_2876 | Q88IX3 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Beta-lactamase (EC 3.5.2.6) |
| [x] | `PP_3455` | PP_3455 | Q88HA5 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Multidrug efflux RND membrane fusion protein |
| [x] | `mexB` | PP_3456 | Q88HA4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Efflux pump membrane transporter |
| [x] | `PP_3582` | PP_3582 | Q88GY3 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | RND efflux transporter, outer membrane protein |
| [x] | `mrdA-I` | PP_3741 | Q88GI2 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) |
| [x] | `opmQ` | PP_4211 | Q88F87 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Pyoverdine export outer membrane protein OpmQ |
| [x] | `mrdA-II` | PP_4807 | Q88DL8 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) |
| [x] | `PP_4923` | PP_4923 | Q88DA4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Outer membrane efflux protein |
| [x] | `mrcA` | PP_5084 | Q88CU6 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Penicillin-binding protein 1A (EC 2.4.99.28) (EC 3.4.16.4) |

## Notes

Generated UTC: 2026-07-08T19:05:54.187236+00:00

2026-07-11 PDT status sync: `modules/beta_lactam_resistance_boundary.yaml` is curated and validates with both module validators. The module separates direct AmpC beta-lactam hydrolysis, AmpG/NagZ peptidoglycan-recycling context, penicillin-binding peptidoglycan targets, RND/MFP/OMF efflux systems, and OprD/OpmQ permeability or export side nodes instead of treating KEGG ppu01501 as one linear pathway.

The ppu01501 batch TSV has 20/20 review files, 20/20 curated review YAMLs, and 20/20 Asta reports. The existing workflow already records gene-review validation as complete.

Real Falcon commands were run:

```bash
just module-deep-research-falcon beta_lactam_resistance_boundary
just module-pathway-deep-research-falcon beta_lactam_resistance_boundary ppu01501 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/beta_lactam_resistance_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__beta_lactam_resistance_boundary__ppu01501-deep-research-falcon.md`
