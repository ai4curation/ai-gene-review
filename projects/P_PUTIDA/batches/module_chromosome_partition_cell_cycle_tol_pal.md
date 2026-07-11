---
title: "PSEPK Tol-Pal envelope/division coordination batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [tolQ, tolR, tolA, tolB, pal, cpoB]
autolink_gene_symbols: false
---

# PSEPK Tol-Pal envelope/division coordination batch

This completed sub-batch covers the TolQ/TolR/TolA/TolB/Pal
envelope-spanning Tol-Pal machinery and the adjacent CpoB
periplasmic envelope-constriction coordinator. TolA was promoted
from `module:transport_membrane_efflux` because it is a missing core
Tol-Pal component needed for module satisfiability.

## Outputs

- Batch table: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_tol_pal.tsv`
- Module: `modules/tol_pal_cell_division_envelope_coordination_boundary.yaml`

## Gene Status

| Gene | Ordered locus | UniProt | Curation | Asta |
|---|---|---|---|---|
| `tolQ` | `PP_1219` | `Q88NI8` | CURATED | PRESENT |
| `tolR` | `PP_1220` | `Q88NI7` | CURATED | PRESENT |
| `tolB` | `PP_1222` | `P0A173` | CURATED | PRESENT |
| `pal` | `PP_1223` | `P0A138` | CURATED | PRESENT |
| `cpoB` | `PP_1224` | `P0A130` | CURATED | PRESENT |
| `tolA` | `PP_1221` | `Q88NI6` | CURATED | PRESENT |

## Curation Notes

- tolQ and tolR are retained as inner-membrane Tol-Pal
  energy-coupling components involved in cell division; broad protein
  transport/import and generic transporter annotations are non-core or
  over-propagated.
- tolA was promoted from the transport/membrane bucket as the missing
  core Tol-Pal connector. Nucleosome, nucleosome assembly, DNA binding,
  and structural constituent of chromatin annotations were removed as
  H1/H5-like InterPro over-propagations.
- tolB and pal form the periplasmic/outer-membrane Tol-Pal arm; Pal's
  core molecular function remains peptidoglycan binding.
- cpoB is retained as an adjacent periplasmic coordinator of
  peptidoglycan synthesis and outer-membrane constriction during
  FtsZ-dependent cytokinesis, not as a Tol-Pal core subunit.
- Falcon module research was attempted for the completed module, but
  Edison returned HTTP 402 before producing
  `modules/tol_pal_cell_division_envelope_coordination_boundary-deep-research-falcon.md`.
