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
- Candidate genes curated: 7
- Core module genes: 6
- Context gene excluded from the carnitine-specific module: 1
- Curated review files: 7
- OpenScientist gene research files: 7

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
- [x] Complete OpenScientist research for the six newly selected genes.
- [x] Research the expanded reusable module and its PSEPK instance.
- [x] Curate the multi-part module and all selected gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `lcdH` | PP_0302 | Q88R32 | unipathway:UPA00117 | PRESENT | CURATED | PRESENT | L-carnitine dehydrogenase (CDH) (L-CDH) (EC 1.1.1.108) |
| [x] | `cbcV` | PP_0294 | Q88R40 | pathway extension | PRESENT | CURATED | PRESENT | shared ABC-transporter ATP-binding subunit |
| [x] | `cbcW` | PP_0295 | Q88R39 | pathway extension | PRESENT | CURATED | PRESENT | shared ABC-transporter membrane subunit |
| [x] | `cbcX` | PP_0296 | Q88R38 | pathway context | PRESENT | CURATED | PRESENT | choline-selective binding component; excluded from the carnitine module |
| [x] | `PP_0301` | PP_0301 | Q88R33 | pathway extension | PRESENT | CURATED | PRESENT | inferred CdhB betainyl-CoA thioesterase |
| [x] | `PP_0303` | PP_0303 | Q88R31 | pathway extension | PRESENT | CURATED | PRESENT | inferred CdhC 3-dehydrocarnitine cleavage enzyme |
| [x] | `caiX` | PP_0304 | Q88R30 | pathway extension | PRESENT | CURATED | PRESENT | carnitine-selective substrate-binding component |

## Notes

2026-08-13: Expanded the prior single UPA00117 reaction into the biologically
coherent PP_0301-PP_0304 carnitine-utilization sequence: uptake, LcdH
oxidation, 3-dehydrocarnitine cleavage, and betainyl-CoA hydrolysis. The
PP_0294/PP_0295 CbcVW form the shared transporter core. CaiX/PP_0304 is the
carnitine-selective receptor inferred from the experimentally characterized
P. aeruginosa system, whereas PP_0296 CbcX is choline-selective and is retained
only as curated locus context. CdhR is regulatory context and is not a required
catalytic part.

- OpenScientist gene-level research is complete for all seven curated genes.
- The expanded species-aware synthesis is
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_l_carnitine_catabolism__upa00117-deep-research-openscientist.md`.
- The reusable four-part module covers CaiX-CbcWV import, LcdH oxidation, CdhC
  cleavage, and CdhB hydrolysis. KT2440 CdhC and CdhB remain orthology/locus
  inferences rather than directly assayed enzymes.

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
