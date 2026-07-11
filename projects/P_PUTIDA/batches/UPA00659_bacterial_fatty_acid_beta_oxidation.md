---
title: "PSEPK UPA00659 fatty-acid beta-oxidation support batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00659: fatty-acid beta-oxidation support

- Module seed: `bacterial_fatty_acid_beta_oxidation`
- Candidate genes from membership table: 4
- Primary bucket genes: 1
- Existing review files: 4
- Curated review files: 4
- Existing Asta research files: 4

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
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
| [x] | `fadE` | PP_1893 | Q88LN6 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | Acyl-coenzyme A dehydrogenase (EC 1.3.8.7) (EC 1.3.8.8) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `fadA__Q88L01` | PP_2137 | Q88L01 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex sub |
| [x] | `PP_4030` | PP_4030 | Q88FQ7 | unipathway:UPA00659 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase/isomerase family protein |

## Notes

Generated UTC: 2026-07-10T01:48:04.623442+00:00

First-pass completed for the UniPathway `UPA00659` support view of the
existing `bacterial_fatty_acid_beta_oxidation` module. The batch covers
already-curated core beta-oxidation genes `fadE`, `fadB`, and
`fadA__Q88L01`, plus the newly fetched and curated UniPathway-primary member
`PP_4030`.

`PP_4030` is a cytoplasmic enoyl-CoA hydratase/isomerase-family protein in
UniPathway UPA00659. The first-pass review marks generic catalytic activity as
over-broad, accepts fatty acid beta-oxidation context, and modifies broad
`isomerase activity` toward proposed replacement
`delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity` based on the PANTHER
subfamily call. The beta-oxidation module now keeps PP_4030 as an auxiliary
unsaturated-fatty-acid beta-oxidation candidate, separate from the core FadB
hydration and hydroxyacyl-CoA oxidation steps.

The generic Falcon module report already exists:

- `modules/bacterial_fatty_acid_beta_oxidation-deep-research-falcon.md`

The real UPA00659 module+pathway+PSEPK Falcon command was attempted and failed
before report generation with Edison HTTP 402 Payment Required. The queued
output is:

- `projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00659-deep-research-falcon.md`
