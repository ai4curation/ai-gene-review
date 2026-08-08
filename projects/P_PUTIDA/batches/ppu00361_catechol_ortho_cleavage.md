---
title: "PSEPK ppu00361 catechol ortho-cleavage batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00361: Catechol ortho-cleavage branch

- Module seed: `catechol_ortho_cleavage`
- Candidate genes from membership table: 3
- Required neighboring-bucket genes added during curation: 1
- Primary bucket genes: 3
- Existing review files: 4
- Curated review files: 4
- Deep-research files: 3 gene-level Falcon, 1 gene-level OpenScientist, 2 module-level OpenScientist
- Pull request: [#2141](https://github.com/ai4curation/ai-gene-review/pull/2141)

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Complete OpenScientist deep research for newly fetched CatA-II; retain existing Falcon reports for catA-I, catB, and catC.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Deep research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `catA-II` | PP_3166 | Q88I35 | kegg:ppu00361 | PRESENT | CURATED | OPENSCIENTIST | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `catA-I` | PP_3713 | Q88GK8 | kegg:ppu00361 | PRESENT | CURATED | FALCON | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `catB` | PP_3715 | Q88GK6 | kegg:ppu00361 | PRESENT | CURATED | FALCON | Muconate cycloisomerase 1 (EC 5.5.1.1) |
| [x] | `catC` | PP_3714 | Q88GK7 | accessory:catechol_ortho_cleavage | PRESENT | CURATED | FALCON | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) |

## Notes

Generated UTC: 2026-07-15T13:31:09.639696+00:00

2026-07-15 curation notes:

- Created `modules/catechol_ortho_cleavage.yaml` as the three-step catechol
  branch from catechol to beta-ketoadipate enol-lactone: CatA catechol
  1,2-dioxygenase, CatB muconate cycloisomerase, and CatC muconolactone
  delta-isomerase.
- Treated the KEGG `ppu00361` "chlorocyclohexane and chlorobenzene degradation"
  label as a broad map artifact for KT2440. The native module is catechol
  ortho-cleavage in the beta-ketoadipate pathway, not a complete
  chlorinated-aromatic degradation route.
- Added `catC`/PP_3714 as a required module-completion gene even though its
  primary partition is a neighboring aromatic-catabolism bucket; without CatC,
  the CatA/CatB branch stops at muconolactone and is not a complete reusable
  catechol branch.
- Fetched and curated `catA-II`/PP_3166 separately from the existing `catA`
  review. CatA-II is the ben-locus-associated catA2 paralog and is represented
  alongside CatA-I as an exemplar for the first module step.
- Module-level OpenScientist retrieval supports the species-neutral CatA -> CatB
  -> CatC boundary, the start at catechol, and the stop before the shared lower
  beta-ketoadipate chemistry.
- PSEPK module/pathway OpenScientist retrieval concludes that the KT2440 module
  is fully satisfiable after adding CatC/PP_3714. The original three-gene
  `ppu00361` candidate list omitted CatC because KEGG partitions PP_3714 into
  neighboring `ppu00362`, not because the pathway is absent or incomplete.
