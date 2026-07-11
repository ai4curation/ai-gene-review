---
title: "PSEPK chromosome/cell-cycle broad spillovers"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_1105, tig]
autolink_gene_symbols: false
---

# PSEPK chromosome/cell-cycle broad spillovers

This completed spillover batch covers the two genes that entered
`module:chromosome_partition_cell_cycle` only through broad cell-cycle
or cell-division keywords. They are reviewed here to close the
functional bucket, but neither is represented in a chromosome/cell-cycle
module.

## Outputs

- Batch table: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_spillovers.tsv`
- Module: none; both genes are routed to more appropriate pathway contexts.

## Gene Status

| Gene | Ordered locus | UniProt | Curation | Asta | Routing |
|---|---|---|---|---|---|
| `PP_1105` | `PP_1105` | `Q88NU9` | CURATED | PRESENT | DNA ligase / DNA repair and DNA metabolism |
| `tig` | `PP_2299` | `Q88KJ1` | CURATED | PRESENT | Trigger factor chaperone / cotranslational protein folding |

## Curation Notes

- PP_1105 is an ATP-dependent DNA ligase (EC 6.5.1.1). Its
  supported core role is DNA ligase chemistry in DNA repair and
  related DNA metabolism, not a chromosome/cell-cycle module role.
- tig encodes trigger factor, the ribosome-associated FKBP-type
  PPIase/chaperone for de novo cotranslational protein folding.
  The existing review keeps the broad protein-transport term as
  non-core and removes protein unfolding as mis-aspected.
- No module-level Falcon run is needed for this spillover bucket
  because the two genes are deliberately reassigned or kept out.
