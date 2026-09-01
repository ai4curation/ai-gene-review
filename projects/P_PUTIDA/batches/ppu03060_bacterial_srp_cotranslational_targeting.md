---
title: "PSEPK bacterial SRP cotranslational targeting"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ffh, ftsY]
autolink_gene_symbols: false
---

# PSEPK bacterial SRP cotranslational targeting

This batch extracts the bacterial signal-recognition-particle targeting cycle
from the broad KEGG `ppu03060` protein-export map.

## Boundary

1. Ffh and 4.5S RNA recognize a hydrophobic nascent chain on the ribosome.
2. FtsY captures the SRP-ribosome complex at the cytoplasmic membrane.
3. The reciprocal Ffh/FtsY GTPase cycle drives handoff to SecYEG and targeting-factor
   dissociation.

SecYEG-mediated insertion/translocation, Tat and post-translational Sec export,
ribosome assembly, and membrane-protein folding are outside this targeting module.

## Status

- [x] Define a reusable three-role bacterial SRP module.
- [x] Curate the two KT2440 protein reviews.
- [x] Complete SRP-specific OpenScientist module + pathway + taxon research
      (754.85 seconds; report and artifacts retained).
- [x] Complete annotation-reviewer passes for `ffh` and `ftsY`.
- [x] Complete the module-curation audit.
- [x] Validate and render all artifacts.
- [x] Merge the original curation in PR [#2530](https://github.com/ai4curation/ai-gene-review/pull/2530).
- [ ] Open the wave132 repair PR and request review.

### 2026-09-01 repair audit

The annotation-reviewer pass rechecked every GOA row and every added assertion
for both selected proteins. The `ffh` review covers all nine GOA rows plus the
two evidence-backed `NEW` assertions for signal-sequence binding and its
recognition subprocess. The `ftsY` review covers all eleven GOA rows, retains
cytoplasm as non-core, and treats plasma-membrane SRP binding and GTPase activity
as its core roles. Both reviews validate without blocking findings, so this
repair does not rewrite their adjudications.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `ffh` | PP_1461 | Q88MV7 | SRP signal recognition and GTPase handoff |
| `ftsY` | PP_5111 | Q88CR9 | Membrane SRP receptor and partner GTPase |

## Required non-protein component

The [SRP-specific OpenScientist report](../deep-research/PSEPK__bacterial_srp_cotranslational_targeting__ppu03060-deep-research-openscientist.md)
resolves the noncoding component as `ffs` / `PP_RS22200` / `PP_mr50` (NCBI Gene
26969983). NCBI Gene independently confirms those aliases, taxon 160488, and the
reference-chromosome locus on `NC_002947.4`. The older `PP_mr49` KEGG feature
overlaps this locus and is not counted as a second RNA gene. The module therefore
counts one `RFAM:RF00169` RNA participant and is fully satisfiable in KT2440.
This curation decision does not edit the underlying source annotation.

The machine-readable focused set is recorded in
[`ppu03060_bacterial_srp_cotranslational_targeting.tsv`](ppu03060_bacterial_srp_cotranslational_targeting.tsv).
The receiving SecYEG machinery is curated separately in the sibling
[`ppu03060` post-translational Sec batch](ppu03060_sec_posttranslational_protein_export.md).
