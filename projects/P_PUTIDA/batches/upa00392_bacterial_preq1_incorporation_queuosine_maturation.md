---
title: "PSEPK bacterial preQ1 incorporation and queuosine maturation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00392: preQ1 incorporation and queuosine maturation

- Module seed: `bacterial_preq1_incorporation_queuosine_maturation`
- Candidate genes from membership table: 4
- Primary bucket genes: 3
- Existing review files: 4
- Curated review files: 4
- Selected module genes: 4
- Selected gene reviews curated: 4
- Selected OpenScientist reports: 1 of 4 complete

## Curated Boundary

- Required reactions: `queF`, `tgt`, `queA`, and one terminal epoxyqueuosine
  reductase.
- QueF reduces preQ0 to preQ1; Tgt inserts preQ1 into target tRNAs; QueA adds
  the ribosylaminomethyl group; QueG or the nonhomologous QueH family performs
  the final epoxyqueuosine reduction.
- P. putida KT2440 uses QueG (`Q88DC7`). QueH is a reusable alternative in
  other bacteria, represented by reviewed Thermotoga maritima `Q9WZJ0`.
- Upstream preQ0 biosynthesis is treated as an external input.
- Bacterial Tgt inserts preQ1 and must not be conflated with the free-queuine
  reaction represented by GO:0008479.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2324](https://github.com/ai4curation/ai-gene-review/pull/2324).
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-07-26: OpenScientist timed out after 7200s for the module + pathway +
PSEPK report; no report file was produced.

2026-07-26: Gene-level OpenScientist completed for `tgt`; the earlier `queF`
run timed out after 7200s without producing a report.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `queA` | PP_0832 | Q88PL8 | unipathway:UPA00392 | PRESENT | CURATED | MISSING | S-adenosylmethionine:tRNA ribosyltransferase-isomerase (EC 2.4.99.17) (Queuosine biosynthesis protein QueA) |
| [x] | `tgt` | PP_0833 | Q88PL7 | unipathway:UPA00392 | PRESENT | CURATED | PRESENT | Queuine tRNA-ribosyltransferase (EC 2.4.2.29) (Guanine insertion enzyme) (tRNA-guanine transglycosylase) |
| [x] | `queF` | PP_2160 | Q88KX9 | kegg:ppu00790 | PRESENT | CURATED | MISSING | NADPH-dependent 7-cyano-7-deazaguanine reductase (EC 1.7.1.13) (7-cyano-7-carbaguanine reductase) (NADPH-dependent nitri |
| [x] | `queG` | PP_4900 | Q88DC7 | unipathway:UPA00392 | PRESENT | CURATED | MISSING | Epoxyqueuosine reductase (EC 1.17.99.6) (Queuosine biosynthesis protein QueG) |

## Notes

The four checked genes span the complete modeled route from preQ0 reduction
through mature queuosine in tRNA. The UniPathway bucket omits the upstream QueF
reaction, so that cross-bucket member is included explicitly. Reusable-module
research identified QueH as a nonhomologous alternative to QueG; it does not
add a fifth PSEPK gene because this genome carries the QueG implementation.

Generated UTC: 2026-07-27T01:17:00.454824+00:00
