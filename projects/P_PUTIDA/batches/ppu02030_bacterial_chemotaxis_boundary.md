---
title: "PSEPK ppu02030 Bacterial chemotaxis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02030: Bacterial chemotaxis

- Module seed: `bacterial_chemotaxis_boundary`
- Candidate genes from membership table: 41
- Primary bucket genes: 41
- Existing review files: 41
- Curated review files: 41
- Existing Asta research files: 41

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
| [ ] | `PP_0317` | PP_0317 | Q88R17 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer |
| [ ] | `mcpH` | PP_0320 | Q88R14 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein McpH |
| [ ] | `ctpL` | PP_0562 | Q88QD2 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein CtpL |
| [ ] | `PP_0584` | PP_0584 | Q88QB0 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer |
| [ ] | `PP_0779` | PP_0779 | Q88PR9 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer/sensory box protein |
| [ ] | `PP_0802` | PP_0802 | Q88PP6 | kegg:ppu02030 | MISSING | MISSING | MISSING | Chemotaxis protein |
| [x] | `dppA-I` | PP_0882 | Q88PG8 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) |
| [x] | `dppA-II` | PP_0884 | Q88PG6 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) |
| [x] | `dppA-III` | PP_0885 | Q88PG5 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) |
| [ ] | `mcpU` | PP_1228 | Q88NI1 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein McpU |
| [ ] | `mcpG` | PP_1371 | Q88N45 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein McpG |
| [ ] | `PP_1819` | PP_1819 | Q88LV8 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer |
| [ ] | `PP_1940` | PP_1940 | Q88LJ2 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer |
| [ ] | `PP_2111` | PP_2111 | Q88L25 | kegg:ppu02030 | MISSING | MISSING | MISSING | Aerotaxis receptor |
| [ ] | `ctpH` | PP_2120 | Q88L17 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein CtpH |
| [ ] | `PP_2128` | PP_2128 | Q88L09 | kegg:ppu02030 | MISSING | MISSING | MISSING | CheV-like chemotaxis protein |
| [ ] | `mcpA` | PP_2249 | Q88KP1 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein McpA |
| [ ] | `PP_2257` | PP_2257 | Q88KN3 | kegg:ppu02030 | MISSING | MISSING | MISSING | Aerotaxis receptor |
| [x] | `rbsB` | PP_2454 | Q88K38 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Ribose ABC transporter, periplasmic ribose-binding subunit |
| [ ] | `pcaY` | PP_2643 | Q88JK6 | kegg:ppu02030 | PRESENT | CURATED | MISSING | Methyl-accepting chemotaxis protein PcaY (PcaY_PP) |
| [x] | `PP_2757` | PP_2757 | Q88J92 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Sugar-binding protein |
| [x] | `PP_2758` | PP_2758 | Q88J91 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Ribose ABC transporter, periplasmic ribose-binding protein |
| [ ] | `PP_2823` | PP_2823 | Q88J26 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer |
| [ ] | `mcpP` | PP_2861 | Q88IY8 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein McpP |
| [ ] | `PP_3414` | PP_3414 | Q88HE6 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer/sensory box protein |
| [ ] | `PP_3557` | PP_3557 | Q88H08 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer |
| [ ] | `PP_3759` | PP_3759 | Q88GG5 | kegg:ppu02030 | MISSING | MISSING | MISSING | protein-glutamate methylesterase (EC 3.1.1.61) |
| [ ] | `cheR3` | PP_3760 | Q88GG4 | kegg:ppu02030 | MISSING | MISSING | MISSING | Putative methyltransferase Cher3 (EC 2.1.1.-) |
| [ ] | `PP_4332` | PP_4332 | Q88EX0 | kegg:ppu02030 | MISSING | MISSING | MISSING | Chemotaxis protein CheW |
| [ ] | `PP_4333` | PP_4333 | Q88EW9 | kegg:ppu02030 | MISSING | MISSING | MISSING | CheW domain protein |
| [ ] | `cheB1` | PP_4337 | Q88EW5 | kegg:ppu02030 | MISSING | MISSING | MISSING | Protein-glutamate methylesterase/protein-glutamine glutaminase of group 1 operon (EC 3.1.1.61) (EC 3.5.1.44) |
| [ ] | `cheA` | PP_4338 | Q88EW4 | kegg:ppu02030 | PRESENT | CURATED | MISSING | Chemotaxis protein CheA (EC 2.7.13.3) |
| [ ] | `cheZ` | PP_4339 | Q88EW3 | kegg:ppu02030 | PRESENT | CURATED | MISSING | Protein phosphatase CheZ (EC 3.1.3.-) (Chemotaxis protein CheZ) |
| [ ] | `cheY` | PP_4340 | Q88EW2 | kegg:ppu02030 | PRESENT | CURATED | MISSING | Response regulator for chemotactic signal transduction |
| [ ] | `cheR2` | PP_4392 | Q88ER1 | kegg:ppu02030 | MISSING | MISSING | MISSING | Chemotaxis protein methyltransferase Cher2 (EC 2.1.1.80) |
| [ ] | `PP_4393` | PP_4393 | Q88ER0 | kegg:ppu02030 | MISSING | MISSING | MISSING | Chemotaxis protein |
| [ ] | `PP_4521` | PP_4521 | Q88EE4 | kegg:ppu02030 | MISSING | MISSING | MISSING | Aerotaxis receptor |
| [ ] | `mcpS` | PP_4658 | Q88E10 | kegg:ppu02030 | PRESENT | CURATED | MISSING | Methyl-accepting chemotaxis protein McpS |
| [ ] | `mcpQ` | PP_5020 | Q88D09 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis protein McpQ |
| [ ] | `PP_5021` | PP_5021 | Q88D08 | kegg:ppu02030 | MISSING | MISSING | MISSING | Methyl-accepting chemotaxis transducer |
| [x] | `dppA-IV` | PP_5283 | Q88C98 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Periplasmic dipeptide transport protein |

## Notes

Generated UTC: 2026-07-09T12:20:02.335464+00:00

2026-07-11 PDT status sync: gene-level work is complete via the partition
sub-batches. The boundary TSV now has 41/41 review folders, 41/41 Asta
reports, and 41/41 review YAMLs with no remaining `PENDING` actions. The
single parent Falcon boxes remain unchecked because Edison Falcon is currently
failing with HTTP 402; the parent boundary module now exists as an index over
the completed sub-batches rather than as one satisfiable bacterial chemotaxis
module.

This primary-only 41-gene checklist was generated before partition completion
and remains a partitioning view; the authoritative current gene-level status is
the partition TSV.

Current partition artifacts:

- `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.tsv`
- `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.md`
- `projects/P_PUTIDA/partition_ppu02030_chemotaxis.py`

Next curation should select one curation-scale bucket such as the core Che
signal-transduction cluster, the named receptor panel, or the
adaptation/accessory group. Do not curate all 41 primary genes as one
bacterial-chemotaxis PR.

2026-07-11 PDT parent-module sync: created and validated
`modules/bacterial_chemotaxis_boundary.yaml` as an umbrella/index module over
the completed core Che, named receptor, orphan MCP/aerotaxis receptor, and
adaptation/accessory submodules, with dipeptide/ribose/sugar-binding proteins
kept as transport spillovers.

Real Falcon commands were run:

```bash
just module-deep-research-falcon bacterial_chemotaxis_boundary
just module-pathway-deep-research-falcon bacterial_chemotaxis_boundary ppu02030 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no
Falcon reports were written. Expected output paths remain:

- `modules/bacterial_chemotaxis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_boundary__ppu02030-deep-research-falcon.md`
