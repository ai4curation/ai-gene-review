---
title: "PSEPK ppu03010 Ribosome batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03010: Ribosome

- Module seed: `bacterial_ribosome_boundary`
- Candidate genes from membership table: 54
- Primary bucket genes: 54
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
| [x] | `rpmH` | PP_0009 | P0A161 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL34 (50S ribosomal protein L34) |
| [x] | `rpsU` | PP_0389 | P0A165 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein bS21 (30S ribosomal protein S21) |
| [x] | `rplK` | PP_0443 | Q88QP5 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL11 (50S ribosomal protein L11) |
| [x] | `rplA` | PP_0444 | Q88QP4 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL1 (50S ribosomal protein L1) |
| [x] | `rplJ` | PP_0445 | Q88QP3 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL10 (50S ribosomal protein L10) |
| [x] | `rplL` | PP_0446 | P0A157 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL12 (50S ribosomal protein L7/L12) |
| [x] | `rpsL` | PP_0449 | Q88QP0 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS12 (30S ribosomal protein S12) |
| [x] | `rpsG` | PP_0450 | Q88QN9 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS7 (30S ribosomal protein S7) |
| [x] | `rpsJ` | PP_0453 | Q88QN6 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS10 (30S ribosomal protein S10) |
| [x] | `rplC` | PP_0454 | Q88QN5 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL3 (50S ribosomal protein L3) |
| [x] | `rplD` | PP_0455 | Q88QN4 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL4 (50S ribosomal protein L4) |
| [x] | `rplW` | PP_0456 | Q88QN3 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL23 (50S ribosomal protein L23) |
| [x] | `rplB` | PP_0457 | Q88QN2 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL2 (50S ribosomal protein L2) |
| [x] | `rpsS` | PP_0458 | Q88QN1 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS19 (30S ribosomal protein S19) |
| [x] | `rplV` | PP_0459 | Q88QN0 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL22 (50S ribosomal protein L22) |
| [x] | `rpsC` | PP_0460 | Q88QM9 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS3 (30S ribosomal protein S3) |
| [x] | `rplP` | PP_0461 | Q88QM8 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL16 (50S ribosomal protein L16) |
| [x] | `rpmC` | PP_0462 | Q88QM7 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL29 (50S ribosomal protein L29) |
| [x] | `rpsQ` | PP_0463 | Q88QM6 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS17 (30S ribosomal protein S17) |
| [x] | `rplN` | PP_0464 | Q88QM5 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL14 (50S ribosomal protein L14) |
| [x] | `rplX` | PP_0465 | Q88QM4 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL24 (50S ribosomal protein L24) |
| [x] | `rplE` | PP_0466 | Q88QM3 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL5 (50S ribosomal protein L5) |
| [x] | `rpsN` | PP_0467 | Q88QM2 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS14 (30S ribosomal protein S14) |
| [x] | `rpsH` | PP_0468 | Q88QM1 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS8 (30S ribosomal protein S8) |
| [x] | `rplF` | PP_0469 | Q88QM0 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL6 (50S ribosomal protein L6) |
| [x] | `rplR` | PP_0470 | Q88QL9 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL18 (50S ribosomal protein L18) |
| [x] | `rpsE` | PP_0471 | Q88QL8 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS5 (30S ribosomal protein S5) |
| [x] | `rpmD` | PP_0472 | Q88QL7 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL30 (50S ribosomal protein L30) |
| [x] | `rplO` | PP_0473 | Q88QL6 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL15 (50S ribosomal protein L15) |
| [x] | `rpmJ` | PP_0475 | P61113 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL36 (50S ribosomal protein L36) |
| [x] | `rpsM` | PP_0476 | Q88QL3 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS13 (30S ribosomal protein S13) |
| [x] | `rpsK` | PP_0477 | P59374 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS11 (30S ribosomal protein S11) |
| [x] | `rpsD` | PP_0478 | Q88QL2 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS4 (30S ribosomal protein S4) |
| [x] | `rplQ` | PP_0480 | Q88QL0 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL17 (50S ribosomal protein L17) |
| [x] | `rpsT` | PP_0600 | Q88Q95 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein bS20 (30S ribosomal protein S20) |
| [x] | `rplU` | PP_0688 | Q88Q10 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL21 (50S ribosomal protein L21) |
| [x] | `rpmA` | PP_0689 | Q88Q09 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL27 (50S ribosomal protein L27) |
| [x] | `rplY` | PP_0721 | Q88PX7 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL25 (50S ribosomal protein L25) (General stress protein CTC) |
| [x] | `rplM` | PP_1315 | Q88N97 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein uL13 (50S ribosomal protein L13) |
| [x] | `rpsI` | PP_1316 | Q88N96 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS9 (30S ribosomal protein S9) |
| [x] | `rpsP` | PP_1462 | Q88MV6 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein bS16 (30S ribosomal protein S16) |
| [x] | `rplS` | PP_1465 | Q88MV3 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL19 (50S ribosomal protein L19) |
| [x] | `rpsB` | PP_1591 | Q88MI0 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS2 (30S ribosomal protein S2) |
| [x] | `rpsA` | PP_1772 | Q88M03 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | 30S ribosomal protein S1 |
| [x] | `rpmF` | PP_1911 | Q88LL9 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL32 (50S ribosomal protein L32) |
| [x] | `rpmI` | PP_2467 | Q88K25 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL35 (50S ribosomal protein L35) |
| [x] | `rplT` | PP_2468 | Q88K24 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL20 (50S ribosomal protein L20) |
| [x] | `rpsO` | PP_4709 | Q88DV9 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein uS15 (30S ribosomal protein S15) |
| [x] | `rplI` | PP_4874 | Q88DF1 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL9 (50S ribosomal protein L9) |
| [x] | `rpsR` | PP_4876 | Q88DE9 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein bS18 (30S ribosomal protein S18) |
| [x] | `rpsF` | PP_4877 | Q88DE8 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Small ribosomal subunit protein bS6 (30S ribosomal protein S6) |
| [x] | `rpmE` | PP_5087 | Q88CU3 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL31 (50S ribosomal protein L31) |
| [x] | `rpmG` | PP_5281 | Q88CA0 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL33 (50S ribosomal protein L33) |
| [x] | `rpmB` | PP_5282 | Q88C99 | kegg:ppu03010 | PRESENT | CURATED | PRESENT | Large ribosomal subunit protein bL28 (50S ribosomal protein L28) |

## Notes

Generated UTC: 2026-07-09T16:38:38.628631+00:00

2026-07-11 PDT status sync: created and validated
`modules/bacterial_ribosome_boundary.yaml` as an umbrella/index module over the
completed ppu03010 30S and 50S ribosomal-protein sub-batches. The parent batch
TSV shows 54/54 review files present, 54/54 curated review YAMLs, and 54/54 Asta
reports. Module validation passed with `linkml-validate -C ModuleReview` and the
module term-label validator. Gene review validation passed for all 54 batch
review files with `uv run ai-gene-review validate --verbose --terms --tsv-output
reports/validation-psepk-ppu03010.tsv <54 files from the batch TSV>`; the report
contains only the TSV header and no validation rows.

Falcon status: ran the real module-level command
`just module-deep-research-falcon bacterial_ribosome_boundary`; it reached Edison
and failed with HTTP 402 Payment Required, so
`modules/bacterial_ribosome_boundary-deep-research-falcon.md` was not created.
Also ran the real module + pathway + taxon command
`just module-pathway-deep-research-falcon bacterial_ribosome_boundary ppu03010 PSEPK`;
it reached Edison and failed with the same HTTP 402 Payment Required response, so
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_ribosome_boundary__ppu03010-deep-research-falcon.md`
was not created. The Falcon workflow boxes remain unchecked.
