---
title: "PSEPK ppu00622 Benzoate upper degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00622: Benzoate upper degradation

- Module seed: `benzoate_upper_pathway`
- Candidate genes from membership table: 6
- Primary bucket genes: 4
- Existing review files: 4
- Curated review files: 4
- Existing OpenScientist research files: 0

## Scope

This batch treats the ppu00622 overlap as the upper benzoate route from
benzoate to catechol. The selected core genes are the four primary-bucket
BenABCD entries: `benA`, `benB`, `benC`, and `benD`. The batch generator also
reported `PP_1791` and `PP_2504` from overlapping ppu00621 lower-pathway
membership; those are explicitly out of scope for this module and should be
handled later with catechol/meta-cleavage or lower aromatic-catabolism modules.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Confirm all selected gene folders are already present.
- [x] Run OpenScientist deep research for selected genes.
- [x] Review each selected gene review for pathway consistency.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_1791` | PP_1791 | Q88LY5 | kegg:ppu00621 | MISSING | OUT_OF_SCOPE | NOT_RUN | Aldolase/synthase |
| [x] | `PP_2504` | PP_2504 | Q88JY9 | kegg:ppu00621 | MISSING | OUT_OF_SCOPE | NOT_RUN | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) |
| [x] | `benA` | PP_3161 | Q88I40 | kegg:ppu00622 | PRESENT | CURATED | COMPLETE | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) |
| [x] | `benB` | PP_3162 | Q88I39 | kegg:ppu00622 | PRESENT | CURATED | COMPLETE | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) |
| [x] | `benC` | PP_3163 | Q88I38 | kegg:ppu00622 | PRESENT | CURATED | COMPLETE | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) |
| [x] | `benD` | PP_3164 | Q88I37 | kegg:ppu00622 | PRESENT | CURATED | COMPLETE | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) |

## Notes

Generated UTC: 2026-07-13T18:15:17.012754+00:00

## 2026-07-13 curation notes

- Created `modules/benzoate_upper_pathway.yaml` as a two-step module:
  BenABC benzoate dioxygenation followed by BenD cis-diol dehydrogenation.
- Kept the root module at the process/pathway level; molecular-function terms
  are attached only to leaf annotons.
- Used InterPro family selectors with PSEPK UniProt exemplars:
  Q88I40/benA, Q88I39/benB, Q88I38/benC, and Q88I37/benD.
- Validated existing `benA`, `benB`, `benC`, and `benD` reviews before adding
  the module; all four passed `just validate PSEPK <gene>`.
- OpenScientist generic module research:
  `modules/benzoate_upper_pathway-deep-research-openscientist.md`.
- OpenScientist module+pathway+taxon research:
  `projects/P_PUTIDA/deep-research/PSEPK__benzoate_upper_pathway__ppu00622-deep-research-openscientist.md`.
- OpenScientist concluded the module is covered by `benA`/`benB`/`benC`/`benD`,
  that `PP_1791` and `PP_2504` are lower meta-cleavage spillover candidates,
  and that the KEGG `ppu00622` "Xylene degradation" label is misleading for
  plasmid-free KT2440. The biochemical anchor for this module is the
  benzoate-to-catechol upper segment, aligned with KEGG M00551/ppu00362 rather
  than genuine xylene/TOL meta-cleavage.
