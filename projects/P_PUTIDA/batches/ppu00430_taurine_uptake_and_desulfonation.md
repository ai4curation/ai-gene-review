---
title: "PSEPK taurine uptake and desulfonation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [tauA, tauB, tauC, tauD]
autolink_gene_symbols: false
---

# PSEPK taurine uptake and desulfonation

- Module: `taurine_uptake_and_desulfonation`
- Pathway context: KEGG `ppu00430` (taurine and hypotaurine metabolism)
- Focused genes: 4
- KEGG-map candidates retained in TSV: 5

## Boundary

This batch covers two linked activities:

1. `tauA`, `tauB`, and `tauC` form the TauABC importer.
2. `tauD` converts imported taurine to aminoacetaldehyde and sulfite.

Downstream aminoacetaldehyde utilization, sulfite assimilation,
sulfur-starvation regulation, and alternative organosulfonate systems are
outside the module. The `pta`, `gdhB`, `PP_3535`, and `ggt` placements on the
broad KEGG map do not make them TauABC-TauD core members.

## Status

- [x] Fetch the four focused genes from UniProt and GOA.
- [x] Create the species-neutral two-part module.
- [ ] Complete OpenScientist research for the four genes.
- [x] Complete generic module OpenScientist research.
- [x] Complete module + `ppu00430` + PSEPK OpenScientist research.
- [x] Curate all four gene reviews.
- [ ] Validate and render the module, gene reviews, and batch page.
- [ ] Open and shepherd one PR for this module.

## Focused Genes

| Gene | Locus | UniProt | Module role |
|---|---|---|---|
| `tauA` | PP_0233 | Q88RA0 | periplasmic taurine-binding unit |
| `tauB` | PP_0232 | Q88RA1 | ATP-coupling unit |
| `tauC` | PP_0231 | Q88RA2 | transmembrane permease unit |
| `tauD` | PP_0230 | Q88RA3 | taurine dioxygenase |

## Evidence Notes

PMID:22221834 directly characterizes the PSEPK TauD reaction, kinetics,
structure, and tetrameric assembly. The TauABC organization and transport
stoichiometry are grounded in the reviewed Q88RA1 UniProtKB record. The broad
candidate inventory remains in
[`ppu00430_taurine_uptake_and_desulfonation.tsv`](ppu00430_taurine_uptake_and_desulfonation.tsv).
