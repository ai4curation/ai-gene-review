---
title: "PSEPK chromosome partition/condensation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [parB, PP_0002, PP_0693, PP_0694, PP_2161, PP_2412, PP_3700, smc, PP_4334, PP_4497, scpA, PP_5070]
autolink_gene_symbols: false
---

# PSEPK chromosome partition/condensation batch

This completed sub-batch covers the ParB/PP_0002 origin-region
partition candidates, MksEF-like condensation candidates, ParA-family
side ATPases, and the Smc-ScpA-ScpB condensin machinery. PP_0002 was
promoted from `unknown:function_unknown` because it is immediately
adjacent to parB and carries Soj/ParA-like DNA-partitioning ATPase
signatures.

## Outputs

- Batch table: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition_condensation.tsv`
- Module: `modules/chromosome_partition_condensation_boundary.yaml`

## Gene Status

| Gene | Ordered locus | UniProt | Curation | Asta |
|---|---|---|---|---|
| `parB` | `PP_0001` | `P0A151` | CURATED | PRESENT |
| `PP_0693` | `PP_0693` | `Q88Q05` | CURATED | PRESENT |
| `PP_0694` | `PP_0694` | `Q88Q04` | CURATED | PRESENT |
| `PP_2161` | `PP_2161` | `Q88KX8` | CURATED | PRESENT |
| `PP_2412` | `PP_2412` | `Q88K79` | CURATED | PRESENT |
| `PP_3700` | `PP_3700` | `Q88GM1` | CURATED | PRESENT |
| `smc` | `PP_4276` | `Q88F23` | CURATED | PRESENT |
| `PP_4334` | `PP_4334` | `Q88EW8` | CURATED | PRESENT |
| `PP_4497` | `PP_4497` | `Q88EG7` | CURATED | PRESENT |
| `scpA` | `PP_4498` | `Q88EG6` | CURATED | PRESENT |
| `PP_5070` | `PP_5070` | `Q88CW0` | CURATED | PRESENT |
| `PP_0002` | `PP_0002` | `P0A149` | CURATED | PRESENT |

## Curation Notes

- parB is retained as the origin-region ParB/Spo0J-family DNA-binding
  chromosome partition protein; the sporulation process annotation is
  removed as an inappropriate family-level spillover for P. putida.
- PP_0002 is promoted as the missing Soj/ParA-like DNA-partitioning
  ATPase candidate next to parB, but its KT2440 role remains
  experimentally unresolved.
- PP_0693 and PP_0694 are treated as MksF/MksE-like condensin
  candidates rather than canonical ParA ATPases.
- PP_2412, PP_3700, PP_4334, and PP_5070 remain candidate ParA-family
  partition ATPases; the review avoids assigning all of them to the
  core chromosomal ParAB system without partner/context evidence.
- smc, scpA, and PP_4497 form the strongest Smc-ScpA-ScpB
  condensation/segregation submodule. The smc sister-chromatid
  cohesion annotation is modified toward chromosome organization and
  chromosome condensation.
- Falcon module research was attempted for the completed module, but
  Edison returned HTTP 402 before producing
  `modules/chromosome_partition_condensation_boundary-deep-research-falcon.md`.
