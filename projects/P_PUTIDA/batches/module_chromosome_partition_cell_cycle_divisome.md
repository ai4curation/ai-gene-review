---
title: "PSEPK divisome/Z-ring/septation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [engB, PP_1309, zapE, ftsL, ftsQ, ftsA, ftsZ, ftsB, dedD, zipA, PP_5090, PP_5202]
autolink_gene_symbols: false
---

# PSEPK divisome/Z-ring/septation batch

This completed sub-batch covers the FtsZ ring, membrane anchors,
FtsB-FtsL-FtsQ subcomplex, Z-ring accessory proteins, EngB septation
context, and SPOR-domain peptidoglycan-binding septal factors from the
larger `module:chromosome_partition_cell_cycle` functional bucket.

## Outputs

- Batch table: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_divisome.tsv`
- Module: `modules/divisome_z_ring_septation_boundary.yaml`

## Gene Status

| Gene | Ordered locus | UniProt | Curation | Asta |
|---|---|---|---|---|
| `engB` | `PP_0124` | `Q88RK5` | CURATED | PRESENT |
| `PP_1309` | `PP_1309` | `Q88NA3` | CURATED | PRESENT |
| `zapE` | `PP_1312` | `Q88NA0` | CURATED | PRESENT |
| `ftsL` | `PP_1330` | `Q88N83` | CURATED | PRESENT |
| `ftsQ` | `PP_1340` | `Q88N73` | CURATED | PRESENT |
| `ftsA` | `PP_1341` | `Q88N72` | CURATED | PRESENT |
| `ftsZ` | `PP_1342` | `Q59692` | CURATED | PRESENT |
| `ftsB` | `PP_1613` | `Q88MF8` | CURATED | PRESENT |
| `dedD` | `PP_1998` | `Q88LD7` | CURATED | PRESENT |
| `zipA` | `PP_4275` | `Q88F24` | CURATED | PRESENT |
| `PP_5090` | `PP_5090` | `Q88CU0` | CURATED | PRESENT |
| `PP_5202` | `PP_5202` | `Q88CH9` | CURATED | PRESENT |

## Curation Notes

- ftsZ remains the central Z-ring GTPase from the existing curated review.
- ftsA and zipA are retained as membrane/Z-ring anchoring factors.
- ftsB, ftsL, and ftsQ are retained as the FtsB-FtsL-FtsQ divisome
  subcomplex.
- PP_5202 is retained as a ZapA-family Z-ring factor, and the
  TreeGrafter septin-ring assembly annotation is removed as a bacterial
  Z-ring/septation over-propagation.
- dedD and PP_5090 are retained as SPOR/RlpA-like peptidoglycan-binding
  septal or cell-division boundary factors.
