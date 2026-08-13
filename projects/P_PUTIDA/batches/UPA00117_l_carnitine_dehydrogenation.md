---
title: "PSEPK UPA00117 UniPathway UPA00117 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK L-carnitine catabolism through 3-dehydrocarnitine

- Pathway seed: `l_carnitine_dehydrogenation` (UPA00117), expanded into the
  reusable multi-part `bacterial_l_carnitine_catabolism` module.
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing OpenScientist research files: 1

## Required Workflow

- [x] Assess module granularity and record the single-step pathway curation.
- [x] Run generic OpenScientist retrieval for the pathway seed.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate gene review; standalone module retired/deferred.
- [x] Fetch the PP_0294-PP_0296 transporter, caiX/PP_0304, PP_0301, and
  PP_0303.
- [ ] Complete OpenScientist research for the six newly selected genes.
- [ ] Research the expanded reusable module and its PSEPK instance.
- [ ] Curate the multi-part module and all selected gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `lcdH` | PP_0302 | Q88R32 | unipathway:UPA00117 | PRESENT | CURATED | PRESENT | L-carnitine dehydrogenase (CDH) (L-CDH) (EC 1.1.1.108) |
| [ ] | `cbcV` | PP_0294 | Q88R40 | pathway extension | PRESENT | PENDING | RUNNING | shared ABC-transporter ATP-binding subunit |
| [ ] | `cbcW` | PP_0295 | Q88R39 | pathway extension | PRESENT | PENDING | RUNNING | shared ABC-transporter membrane subunit |
| [ ] | `cbcX` | PP_0296 | Q88R38 | pathway extension | PRESENT | PENDING | RUNNING | choline/betaine/carnitine-binding component |
| [ ] | `PP_0301` | PP_0301 | Q88R33 | pathway extension | PRESENT | PENDING | RUNNING | candidate betainyl-CoA thioesterase |
| [ ] | `PP_0303` | PP_0303 | Q88R31 | pathway extension | PRESENT | PENDING | RUNNING | candidate 3-dehydrocarnitine cleavage enzyme |
| [ ] | `caiX` | PP_0304 | Q88R30 | pathway extension | PRESENT | PENDING | RUNNING | uncertain alternative carnitine-binding component |

## Notes

2026-08-13: Expanded the prior single UPA00117 reaction into the biologically
coherent PP_0301-PP_0304 carnitine-utilization sequence: uptake, LcdH
oxidation, 3-dehydrocarnitine cleavage, and betainyl-CoA hydrolysis. The
PP_0294-PP_0296 CbcVWX complex has direct KT2440 fitness support for carnitine
uptake; CaiX is retained as an uncertain alternative receptor. CdhR is
regulatory context and is not a required catalytic part.

Generated UTC: 2026-07-11T21:08:35.324367+00:00

- Retired the previous `modules/l_carnitine_dehydrogenation.yaml` seed:
  UPA00117 is a single LcdH oxidation step and should not be represented as a
  standalone one-part module. Reintroduce it only inside a broader multi-part
  carnitine-utilization module.
- OpenScientist gene-level research completed:
  `genes/PSEPK/lcdH/lcdH-deep-research-openscientist.md`.
- OpenScientist generic retrieval completed:
  `modules/l_carnitine_dehydrogenation-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research completed:
  `projects/P_PUTIDA/deep-research/PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-openscientist.md`.
- Curation decision: UPA00117 is covered by the single KT2440 candidate
  `lcdH` / PP_0302 / Q88R32 for NAD(+)-dependent L-carnitine oxidation to
  3-dehydrocarnitine.
- Boundary call: PP_0301, PP_0303, PP_0304, PP_0305 are adjacent
  carnitine-utilization context, not members of this single-step UniPathway
  bucket.
- Quality-control call: the OpenScientist reports mention GO:0008859 as
  carnitine 3-dehydrogenase activity, but OAK/GO lookup shows GO:0008859 is
  exoribonuclease II activity. The correct fetched GOA term retained here is
  GO:0047728.
