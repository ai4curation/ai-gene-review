---
title: "PSEPK Xer/FtsK chromosome dimer resolution batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [xerC, xerD, ftsK, PP_2841]
autolink_gene_symbols: false
---

# PSEPK Xer/FtsK chromosome dimer resolution batch

This completed sub-batch covers the XerC/XerD chromosome dimer
resolution system, the FtsK septal DNA translocase, and one related
integrase-family side candidate from the larger
`module:chromosome_partition_cell_cycle` functional bucket.

## Outputs

- Batch table: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_xer_ftsk.tsv`
- Module: `modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml`

## Gene Status

| Gene | Ordered locus | UniProt | Curation | Asta |
|---|---|---|---|---|
| `xerD` | `PP_1468` | `Q88MV0` | CURATED | PRESENT |
| `PP_2841` | `PP_2841` | `Q88J08` | CURATED | PRESENT |
| `ftsK` | `PP_4004` | `Q88FS8` | CURATED | PRESENT |
| `xerC` | `PP_5230` | `Q88CF1` | CURATED | PRESENT |

## Curation Notes

- xerC and xerD are curated as the core cytoplasmic tyrosine
  recombinase subunits that resolve chromosome dimers and support
  chromosome segregation.
- ftsK is curated as the septal membrane DNA translocase that couples
  cell division with chromosome segregation and activates XerCD-mediated
  chromosome unlinking.
- PP_2841 is retained as a predicted tyrosine recombinase/integrase-family
  boundary candidate, not as a core XerCD-FtsK chromosome dimer
  resolution component.
- Falcon module research was attempted for the completed module, but
  Edison returned HTTP 402 before producing
  `modules/chromosome_dimer_resolution_dna_translocation_boundary-deep-research-falcon.md`.
