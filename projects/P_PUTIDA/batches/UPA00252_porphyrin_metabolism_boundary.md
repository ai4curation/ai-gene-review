---
title: "PSEPK UPA00252 porphyrin/protoheme support batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00252: porphyrin/protoheme support

- Module seed: `porphyrin_metabolism_boundary`
- Candidate genes from membership table: 2
- Primary bucket genes: 1
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_0189` | PP_0189 | Q88RE2 | unipathway:UPA00252 | PRESENT | CURATED | PRESENT | Heme biosynthesis protein |
| [x] | `hemH` | PP_0744 | Q88PV4 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Ferrochelatase (EC 4.98.1.1) (Heme synthase) (Protoheme ferro-lyase) |

## Notes

Generated UTC: 2026-07-10T01:39:01.379595+00:00

First-pass completed for the UniPathway `UPA00252` support view of the
existing `porphyrin_metabolism_boundary` module. The batch contains the
newly curated UniPathway-primary member `PP_0189` and already-curated `hemH`
context from the KEGG `ppu00860` porphyrin/tetrapyrrole batch.

`PP_0189` did not resolve through the usual symbol-based fetch, so the review
folder was seeded by accession alias Q88RE2. The review keeps the UniProt
inner-membrane localization, modifies the broad `heme metabolic process`
annotation to the more specific `heme biosynthetic process`, and deliberately
does not assert a molecular function in this first pass. The module now has a
separate `PP_0189` late-protoheme support annoton adjacent to the `hemH`
ferrochelatase step.

Both real Falcon calls were attempted and failed before report generation with
Edison HTTP 402 Payment Required. The queued outputs are:

- `modules/porphyrin_metabolism_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__porphyrin_metabolism_boundary__upa00252-deep-research-falcon.md`
