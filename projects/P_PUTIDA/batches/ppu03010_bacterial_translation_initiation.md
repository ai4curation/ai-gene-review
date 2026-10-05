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
biogenesis or the full translation cycle. The selected reviews contain 21 GOA
rows: 8 for `infA`, 6 for `infB`, and 7 for `infC`.

## Boundary

1. IF2 and IF3 associate with the 30S initiation platform; IF3 maintains the
   pool of free, initiation-competent 30S subunits.
2. IF1 stabilizes IF2 and IF3 on the 30S subunit and supports preinitiation
   complex assembly.
3. IF2 promotes fMet-tRNA binding and hydrolyzes GTP during 70S-complex
   formation.

Initiator-tRNA charging/formylation, ribosomal proteins, elongation,
termination, and RRF/EF-G-driven recycling are outside the module. IF3 binding
to an already-free 30S subunit defines the initiation boundary; its contextual
role in stabilizing recycled subunits remains in the gene review rather than
the module annoton.

## Status

- [x] Retain a reusable three-part, bacteria-scoped initiation module rather
      than treating the 54-protein KEGG ribosome inventory as one flat module.
- [x] Verify the exact KT2440 `infA`, `infB`, and `infC` accessions and audit all
      21 GOA rows.
- [x] Complete the mandatory independent annotation-reviewer consultation.
- [x] Add direct structural, kinetic, recycling-interface, and start-codon
      discrimination evidence for IF1, IF2, and IF3.
- [x] Complete and assess generic-module and module + pathway + taxon
      OpenScientist reports.
- [x] Revalidate and render all changed artifacts after research integration.
- [x] Record the original curation in merged PR
      [#2521](https://github.com/ai4curation/ai-gene-review/pull/2521).

## Focused Genes

| Gene | Locus | UniProt | GOA rows | Core role | Audit result |
|---|---|---|---:|---|---|
| `infA` | PP_4007 | P65117 | 8 | IF1 stabilization of the 30S preinitiation complex | Exact initiation-factor and process terms accepted; broad binding/location parents retained as non-core or modified to a more precise term |
| `infB` | PP_4712 | Q88DV7 | 6 | IF2 initiator-tRNA recruitment and subunit joining | Initiation-factor and GTPase activities accepted; GTP binding and broad cytoplasm retained as non-core |
| `infC` | PP_2466 | Q88K26 | 7 | IF3 free-30S maintenance and initiation-site discrimination | Spurious membrane removed; disassembly retained only as non-core gene context; generic ribosome binding modified to small-subunit binding |

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
- PMID:8858589 provides in-vivo evidence that IF3 discriminates efficient from
  inefficient bacterial initiation codons.

## Family and exemplar grounding

- `P65117` and E. coli K-12 `P69222` are verified members of
  `PANTHER:PTHR33370`, whose exact official label is the surprising
  `TRANSLATION INITIATION FACTOR IF-1, CHLOROPLASTIC`.
- `Q88DV7` and E. coli K-12 `P0A705` are verified members of
  `PANTHER:PTHR43381` (`TRANSLATION INITIATION FACTOR IF-2-RELATED`).
- `Q88K26` and E. coli K-12 `P0A707` are verified members of
  `PANTHER:PTHR10938` (`TRANSLATION INITIATION FACTOR IF-3`).
- The module makes no ancestral-node claim. GOA `WITH/FROM` PTNs remain row
  provenance and were not promoted to `ancestral_nodes` without matching
  current local PAINT support.

## Research assessment

- The generic OpenScientist module run completed in 6,797 seconds (about 113
  minutes) using the full three-iteration allowance. Its Markdown report and
  HTML/PDF artifacts support the three-factor boundary, IF3 fidelity and
  anti-association roles, and the non-obligate interpretation of factor order.
- The module + pathway + taxon run completed in 4,588 seconds (about 76
  minutes) using the full three-iteration allowance. Its Markdown report and
  HTML/PDF artifacts classify `infA`, `infB`, and `infC` as
  `covered_offbucket`: all three factors exist in KT2440, while the 54-member
  KEGG `ppu03010` inventory is restricted to ribosomal proteins.
- Neither report identifies a missing translation-initiation factor in KT2440.
  The broader ribosome-protein inventory remains a separate curation target.

## Residual uncertainty

- The four primary studies characterize E. coli factors; the exact KT2440
  proteins are strongly supported by conserved family, UniProt, and GOA
  evidence but lack target-specific initiation biochemistry in this batch.
- Factor association is dynamic. The IF2/IF3-before-IF1 connection represents
  one kinetically favored E. coli route and is not asserted as a universal
  obligatory order.
- KEGG `ppu03010` supplies 54 ribosomal-protein candidates but omits `infA`,
  `infB`, and `infC`; the focused inventory therefore comes from the complete
  KT2440 proteome partition rather than KEGG membership alone.
