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
- [ ] Complete OpenScientist gene, module, and module + pathway + taxon research
      (session `20685` remains active and is non-blocking for publication).
- [x] Complete the independent annotation-reviewer and module-curation audit.
- [x] Validate and render all artifacts.
- [ ] Open one draft PR.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `ffh` | PP_1461 | Q88MV7 | SRP signal recognition and GTPase handoff |
| `ftsY` | PP_5111 | Q88CR9 | Membrane SRP receptor and partner GTPase |

The 4.5S SRP RNA is required biologically but is not assigned a guessed protein
identifier or locus in this protein-centered batch.

The machine-readable focused set is recorded in
[`ppu03060_bacterial_srp_cotranslational_targeting.tsv`](ppu03060_bacterial_srp_cotranslational_targeting.tsv).
The receiving SecYEG machinery is curated separately in the sibling
[`ppu03060` post-translational Sec batch](ppu03060_sec_posttranslational_protein_export.md).
