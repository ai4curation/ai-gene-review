---
title: "PSEPK ppu00332 glutamate-to-P5C precursor batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00332: bacterial glutamate-to-P5C precursor module

- Module seed: `bacterial_glutamate_to_p5c_biosynthesis`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing OpenScientist research files: 2

## Curated Boundary

- Required PSEPK realization: `proB` followed by `proA`.
- The reusable module covers ATP-dependent glutamate phosphorylation and
  NADPH-dependent reduction to L-glutamate 5-semialdehyde, which cyclizes to
  P5C.
- The downstream ProC/P5C-reductase reaction is outside this precursor module,
  so this is not a complete proline-biosynthesis model.
- `ppu00332` is retained as source-bucket provenance only. Its carbapenem label
  is a KEGG cross-map artifact and does not describe a carbapenem pathway in
  PSEPK.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `proB` | PP_0691 | Q88Q07 | kegg:ppu00332 | PRESENT | CURATED | FAILED_TIMEOUT | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK) |
| [x] | `proA` | PP_4811 | Q88DL4 | kegg:ppu00332 | PRESENT | CURATED | FAILED_TIMEOUT | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialde |

## Notes

Generated UTC: 2026-07-16T17:37:22.072385+00:00

2026-07-16: OpenScientist timed out after 7200s for `proB` and `proA`; no gene-level report files were produced for those runs.

2026-09-01 wave109 repair: Reused the completed generic and PSEPK pathway
OpenScientist reports, both generated with the configured 7200s provider
timeout. Removed redundant module-level cytoplasm while retaining supported
leaf locations and leaf molecular functions. Added reviewed, experimentally
characterized E. coli ProB/P0A7B5 and ProA/P07004 exemplars plus exact PAINT
nodes `PTN000115542` and `PTN000115463`. Misleading PANTHER subfamily IDs were
omitted. The required annotation-reviewer pass retained all proB/proA actions;
it requested only a more cautious, cited rationale for the proB RNA-binding
over-annotation, and no proA YAML change.

2026-09-01 validation: Module schema and semantic validation passed; the only
advisory was an unavailable ontology lookup for `NCBITaxon:2`. Both `proB` and
`proA` reviews passed full validation. The module, changed gene review, and
batch page were rendered, and `git diff --check` passed.
