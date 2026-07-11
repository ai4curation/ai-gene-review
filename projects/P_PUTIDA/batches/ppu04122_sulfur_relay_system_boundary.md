---
title: "PSEPK ppu04122 Sulfur relay system batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04122: Sulfur relay system

- Module seed: `sulfur_relay_system_boundary`
- Candidate genes from membership table: 19
- Primary bucket genes: 19
- Existing review files: 19
- Curated review files: 19
- Existing Asta research files: 19

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
| [x] | `moeB` | PP_0735 | Q88PW3 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdopterin-synthase adenylyltransferase (EC 2.7.7.80) (MoaD protein adenylase) (Molybdopterin-converting factor subun |
| [x] | `tusA-I` | PP_1233 | Q88NH6 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfurtransferase (EC 2.8.1.-) |
| [x] | `moaC` | PP_1292 | Q88NC0 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17) (Molybdenum cofactor biosynthesis protein C) |
| [x] | `moaD` | PP_1293 | Q88NB9 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdopterin synthase sulfur carrier subunit |
| [x] | `moaE` | PP_1294 | Q88NB8 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdopterin synthase catalytic subunit (EC 2.8.1.12) (MPT synthase subunit 2) (Molybdenum cofactor biosynthesis protei |
| [x] | `PP_1969` | PP_1969 | Q88LG4 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein A |
| [x] | `tusA` | PP_2116 | Q88L21 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfur carrier protein TusA |
| [x] | `moaB-I` | PP_2122 | Q88L15 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein B |
| [x] | `PP_2482` | PP_2482 | Q88K11 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein A |
| [x] | `tusD` | PP_3993 | Q88FT9 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfur transfer protein complex, TusD subunit |
| [x] | `PP_3994` | PP_3994 | Q88FT8 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | tRNA 5-methylaminomethyl-2-thiouridine synthase (TusC-like) |
| [x] | `PP_3995` | PP_3995 | Q88FT7 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfurtransferase complex subunit TusB |
| [x] | `tusE` | PP_3996 | Q88FT6 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfurtransferase (EC 2.8.1.-) |
| [x] | `mnmA` | PP_4014 | Q88FR9 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | tRNA-specific 2-thiouridylase MnmA (EC 2.8.1.13) |
| [x] | `moaA` | PP_4597 | Q88E69 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | GTP 3',8-cyclase (EC 4.1.99.22) (Molybdenum cofactor biosynthesis protein A) |
| [x] | `moaB-II` | PP_4600 | Q88E67 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein B |
| [x] | `rhdA` | PP_4907 | Q88DC0 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfurtransferase |
| [x] | `PP_5105` | PP_5105 | Q88CS5 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Sulfur carrier protein ThiS |
| [x] | `sseA` | PP_5118 | Q88CR2 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) |

## Notes

Generated UTC: 2026-07-09T12:34:24.030860+00:00

2026-07-11 PDT status sync: gene-level work is complete via the partition
sub-batches. The boundary TSV now has 19/19 review folders, 19/19 Asta
reports, and 19/19 review YAMLs with no remaining `PENDING` actions. The
single parent Falcon boxes remain unchecked because Edison Falcon is currently
failing with HTTP 402; the parent boundary module now exists as an index over
the completed sub-batches rather than as one generic sulfur-relay pathway.

This primary-only 19-gene checklist is now synchronized to the partition output
for gene-level status, but the curation-complete evidence lives in the
partitioned sub-batches.

Current partition artifacts:

- `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.tsv`
- `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.md`
- `projects/P_PUTIDA/partition_ppu04122_sulfur_relay.py`

Next curation should select one curation-scale bucket, especially
molybdopterin/MoCo sulfur relay or Tus/MnmA tRNA thiolation. Keep `PP_5105`
with thiamine biosynthesis, and keep `rhdA`/`sseA` with general
sulfur-metabolism sulfurtransferase context unless a more specific
sulfur-relay mechanism is selected.

2026-07-11 PDT parent-module sync: created and validated
`modules/sulfur_relay_system_boundary.yaml` as an umbrella/index module over
the completed MoCo sulfur-relay and Tus/MnmA tRNA-thiolation submodules, plus
ThiS thiamine and rhodanese/mercaptopyruvate sulfurtransferase side contexts.

Real Falcon commands were run:

```bash
just module-deep-research-falcon sulfur_relay_system_boundary
just module-pathway-deep-research-falcon sulfur_relay_system_boundary ppu04122 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no
Falcon reports were written. Expected output paths remain:

- `modules/sulfur_relay_system_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__sulfur_relay_system_boundary__ppu04122-deep-research-falcon.md`
