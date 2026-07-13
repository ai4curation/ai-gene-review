---
title: "PSEPK ppu03010 Ribosome partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03010: Ribosome partition

KEGG ppu03010 is a coherent bacterial ribosome protein set. There is
no unknown/spillover bucket in the primary PSEPK membership, but the
54-gene list should be curated as 30S and 50S subunit batches rather
than as one all-ribosome PR.

## Outputs

- Source batch: `projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_boundary.tsv`
- Partition table: `projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Example genes |
|---|---:|---|---|---|
| `bacterial_30s_ribosomal_subunit` | 21 | `bacterial_30s_ribosomal_subunit_boundary` | NEW_SUBMODULE | `rpsU`, `rpsL`, `rpsG`, `rpsJ`, `rpsS`, `rpsC`, `rpsQ`, `rpsN`, `rpsH`, `rpsE` |
| `bacterial_50s_ribosomal_subunit` | 33 | `bacterial_50s_ribosomal_subunit_boundary` | NEW_SUBMODULE | `rpmH`, `rplK`, `rplA`, `rplJ`, `rplL`, `rplC`, `rplD`, `rplW`, `rplB`, `rplV` |

## Current Curation Status

| Bucket | Genes | Review folders | Curated reviews | Asta reports | Module file |
|---|---:|---:|---:|---:|---|
| `bacterial_30s_ribosomal_subunit` | 21 | 21 | 21 | 21 | `modules/bacterial_30s_ribosomal_subunit_boundary.yaml` |
| `bacterial_50s_ribosomal_subunit` | 33 | 33 | 33 | 33 | `modules/bacterial_50s_ribosomal_subunit_boundary.yaml` |

## Working Decisions

- Do not curate all 54 primary genes as one first-pass ribosome PR.
- There is no unknown bucket: every primary member is a small- or
  large-subunit ribosomal protein.
- Split curation into 30S and 50S subunit modules to keep complex
  membership, rRNA binding, and translation contributions tractable.

## Next Steps

- Keep ppu03010 registered as `PARTITIONED` in the pathway worklist
  until both subunit batches are complete.
- Treat a subunit bucket as complete once all rows are present,
  curated, Asta-backed, validated, and rendered, and the matching
  `modules/<subunit>_boundary.yaml` validates.
- Once both subunit buckets are complete, treat ppu03010 as a
  completed partitioned pathway rather than collapsing the two
  modules into one 54-gene review unit.
- Run real Falcon module/pathway commands only after one subunit module
  is selected; current Edison Falcon access failure mode is HTTP 402.
