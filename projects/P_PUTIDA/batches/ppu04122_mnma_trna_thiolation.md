---
title: "PSEPK MnmA tRNA wobble-uridine thiolation sulfur relay"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [iscS, tusA, tusD, PP_3994, PP_3995, tusE, mnmA]
autolink_gene_symbols: false
---

# PSEPK MnmA tRNA wobble-uridine thiolation sulfur relay

This batch extracts the MnmA branch from the broad KEGG `ppu04122` sulfur relay
bucket. The reusable module is `modules/bacterial_mnma_trna_thiolation.yaml`.

## Boundary

1. IscS mobilizes sulfur from cysteine.
2. TusA carries sulfur to the TusBCD complex.
3. TusBCD organizes the intermediate transfer, with TusD as sulfur carrier.
4. TusE carries sulfur from TusBCD to MnmA.
5. MnmA catalyzes ATP-dependent 2-thiolation of tRNA wobble uridine.

Other IscS-dependent pathways, the molybdenum-cofactor sulfur relay, ThiI-driven
tRNA U8 thiolation, and downstream MnmC chemistry are outside this module.

## Status

- [x] Define a species-neutral five-part MnmA sulfur-relay module.
- [x] Fetch the seven KT2440 gene review scaffolds and source records.
- [x] Curate all existing GO annotations and core functions.
- [ ] Complete OpenScientist gene, module, and module + pathway + taxon research.
- [x] Obtain annotation-reviewer subagent sign-off.
- [x] Validate and render all current curation artifacts.
- [ ] Open one draft PR.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `iscS` | PP_0842 | Q88PK8 | Sulfur mobilization from cysteine |
| `tusA` | PP_2116 | Q88L21 | Initial sulfur carrier |
| `tusD` | PP_3993 | Q88FT9 | Sulfur-bearing TusBCD subunit |
| `PP_3994` | PP_3994 | Q88FT8 | TusC-family TusBCD subunit |
| `PP_3995` | PP_3995 | Q88FT7 | TusB-family TusBCD subunit |
| `tusE` | PP_3996 | Q88FT6 | Terminal sulfur carrier |
| `mnmA` | PP_4014 | Q88FR9 | tRNA-uridine 2-sulfurtransferase |
