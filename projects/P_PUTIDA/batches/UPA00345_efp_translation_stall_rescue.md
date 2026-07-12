---
title: "PSEPK UPA00345 EF-P translation stall rescue batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00345: EF-P translation stall rescue

- Module seed: `efp_translation_stall_rescue`
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing Asta research files: 1

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [PR #2051](https://github.com/ai4curation/ai-gene-review/pull/2051).
- [x] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `efp` | PP_1858 | Q88LS0 | unipathway:UPA00345 | PRESENT | CURATED | PRESENT | Elongation factor P (EF-P) |

## Notes

Generated UTC: 2026-07-10T01:23:19.469718+00:00

- Fetched by accession alias, Asta-backed, curated, and validated the single
  UniPathway member: `efp` / PP_1858 / Q88LS0.
- Created and validated `modules/efp_translation_stall_rescue.yaml` as a compact
  single-gene UPA00345 module with two EF-P roles: stalled-ribosome engagement
  and EF-P-dependent elongation/stall rescue.
- Follow-up after PR #2051 review: generalized the reusable module from a
  PSEPK-centered wording to a species-neutral bacterial EF-P-family module.
  `efp` / PP_1858 / Q88LS0 is now recorded as the PSEPK UniProt exemplar rather
  than as the module's full scope, with additional representative EF-P members
  and PAINT/PTN anchors recorded in the module.
- Follow-up after PR #2071 review: removed module-level molecular-function
  concepts, collapsed redundant cytoplasm/cytosol locations to cytosol, and
  split the module into explicit ribosome-engagement and elongation/stall-rescue
  roles.
- Corrected the accession-based seed so `gene_symbol` is `efp` rather than
  `Q88LS0`.
- `efp` accepts translation elongation factor activity, translational
  elongation, cytosolic localization, and rescue of stalled cytosolic ribosome
  as core annotations.
- Broad `regulation of translation` and `peptide biosynthetic process`
  annotations were retained as non-core context because the more informative
  module core is EF-P-dependent elongation and stall rescue.
- EarP-dependent Arg32 rhamnosylation and dTDP-rhamnose supply are recorded as
  activation context, not members of this single-gene UniPathway bucket.
- Falcon/Edison generic and taxon-aware runs were attempted earlier and failed
  before report creation with Edison HTTP 402 Payment Required, so the batch was
  re-run with OpenScientist.
- OpenScientist generic module research completed:
  `modules/efp_translation_stall_rescue-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research completed and resolved the
  expected local UniPathway candidate set: one candidate, `efp` / PP_1858 /
  Q88LS0:
  `projects/P_PUTIDA/deep-research/PSEPK__efp_translation_stall_rescue__upa00345-deep-research-openscientist.md`.
- OpenScientist found the UPA00345 core step satisfied by `efp` alone. It also
  reinforced the module boundary: EarP/PP_1857 and the rml/rfb dTDP-L-rhamnose
  genes are activation context rather than UPA00345 members, the E. coli-style
  EpmA/EpmB/EpmC beta-lysylation route is not expected in KT2440, and KT2440 has
  no EfpL/YeiP paralog ambiguity.
- Follow-up curation note: the adjacent EarP/Q88LS1 UniProt text reportedly
  describes the EF-P target residue as Lys-32 even though pseudomonad EF-P is
  Arg32-rhamnosylated; this should be checked in a separate EarP review or
  UniProt correction workflow.
