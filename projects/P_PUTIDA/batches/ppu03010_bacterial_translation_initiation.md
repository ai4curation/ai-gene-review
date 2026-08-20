---
title: "PSEPK bacterial translation initiation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [infA, infB, infC]
autolink_gene_symbols: false
---

# PSEPK bacterial translation initiation

This focused batch complements the broad KEGG `ppu03010` ribosome map with the
three bacterial translation-initiation factors identified from the KT2440
proteome inventory. It models initiation-complex assembly, not ribosome
biogenesis or the full translation cycle.

## Boundary

1. IF2 and IF3 associate with the 30S initiation platform; IF3 maintains the
   pool of free, initiation-competent 30S subunits.
2. IF1 stabilizes IF2 and IF3 on the 30S subunit and supports preinitiation
   complex assembly.
3. IF2 promotes fMet-tRNA binding and hydrolyzes GTP during 70S-complex
   formation.

Initiator-tRNA charging/formylation, ribosomal proteins, elongation, and
termination are outside the module. RRF/EF-G-driven recycling remains outside,
while IF3 stabilization of newly split 30S subunits is retained as the
recycling-to-initiation interface.

## Status

- [x] Define a reusable three-role translation-initiation module.
- [x] Curate the three KT2440 gene reviews.
- [x] Add primary structural and kinetic evidence for IF1, IF2, and IF3.
- [ ] Complete OpenScientist gene and module + pathway + taxon research (jobs
      active; non-blocking for publication).
- [x] Complete the independent annotation-reviewer audit.
- [x] Validate and render all artifacts.
- [x] Open draft PR [#2521](https://github.com/ai4curation/ai-gene-review/pull/2521).

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `infA` | PP_4007 | P65117 | IF1 stabilization of the 30S preinitiation complex |
| `infB` | PP_4712 | Q88DV7 | IF2 initiator-tRNA recruitment and subunit joining |
| `infC` | PP_2466 | Q88K26 | IF3 maintenance of free 30S subunits |

The machine-readable focused set is recorded in
[`ppu03010_bacterial_translation_initiation.tsv`](ppu03010_bacterial_translation_initiation.tsv).

## Evidence and ordering

- PMID:11228145 grounds IF1 occupancy of the 30S A site and its effects on the
  decoding center.
- PMID:22562136 supports IF3/IF2 arrival before IF1 as a kinetically favored
  *E. coli* route, not an obligatory universal order; mRNA recruitment can occur
  at different points during assembly.
- PMID:10790378 directly measures IF2-dependent GTP hydrolysis during late
  initiation.
- PMID:16043510 shows that IF3 stabilizes 30S and 50S subunits transiently split
  from post-termination ribosomes by RRF and EF-G.
