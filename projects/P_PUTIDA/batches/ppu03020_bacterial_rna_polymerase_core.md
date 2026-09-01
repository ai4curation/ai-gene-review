---
title: "PSEPK ppu03020 RNA polymerase batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03020: RNA polymerase

- Module seed: `bacterial_rna_polymerase_core`
- Candidate genes from membership table: 4
- Primary bucket genes: 4
- Existing review files: 4
- Curated review files: 4
- Existing complete gene-level OpenScientist research files: 2

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Perform and document an annotation-reviewer pass for every selected gene.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `rpoB` | PP_0447 | Q88QP2 | kegg:ppu03020 | PRESENT | CURATED | FAILED_TIMEOUT | DNA-directed RNA polymerase subunit beta (RNAP subunit beta) (EC 2.7.7.6) (RNA polymerase subunit beta) (Transcriptase s |
| [x] | `rpoC` | PP_0448 | Q88QP1 | kegg:ppu03020 | PRESENT | CURATED | PRESENT | DNA-directed RNA polymerase subunit beta' (RNAP subunit beta') (EC 2.7.7.6) (RNA polymerase subunit beta') (Transcriptas |
| [x] | `rpoA` | PP_0479 | Q88QL1 | kegg:ppu03020 | PRESENT | CURATED | PRESENT | DNA-directed RNA polymerase subunit alpha (RNAP subunit alpha) (EC 2.7.7.6) (RNA polymerase subunit alpha) (Transcriptas |
| [x] | `rpoZ` | PP_5301 | Q88C82 | kegg:ppu03020 | PRESENT | CURATED | FAILED_TIMEOUT | DNA-directed RNA polymerase subunit omega (RNAP omega subunit) (EC 2.7.7.6) (RNA polymerase omega subunit) (Transcriptas |

## Notes

Generated UTC: 2026-07-16T17:08:08.373869+00:00

2026-07-16: OpenScientist timed out after 7200s for the module + pathway + PSEPK report, `rpoB`, and `rpoZ`; no report files were produced for those runs.

2026-09-01: Wave127 re-ran module + pathway + PSEPK research with
OpenScientist using the full 7200-second allowance. The four selected reviews
received explicit annotation-reviewer passes documented in each gene's notes.
The reusable module retains alpha assembly, beta/beta-prime catalytic-cleft,
and omega assembly/stability roles; molecular functions remain on leaf
annotons, the shared cytosol assertion is stated only at module level, and both
PSEPK and E. coli K-12 proteins ground the family roles. The completed 2026-07-16
gene reports for `rpoA` and `rpoC` were reused. Historical `rpoB` and `rpoZ`
gene-level timeouts remain documented rather than being replaced with manual
provider-named files.

The Wave127 taxon report completed successfully in 877.65 seconds with six
citations and two provider artifacts. It found the module completely
satisfiable with the four selected single-copy genes, identified no missing
role or lineage-specific replacement, and supported keeping sigma factors and
stringent-response effectors outside this module.
