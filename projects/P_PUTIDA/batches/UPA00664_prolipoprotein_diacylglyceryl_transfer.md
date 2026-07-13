---
title: "PSEPK UPA00664 prolipoprotein diacylglyceryl transfer batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00664: prolipoprotein diacylglyceryl transfer

- Pathway seed: `prolipoprotein_diacylglyceryl_transfer` (single-step; no standalone module retained)
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing OpenScientist gene research files: 1

## Required Workflow

- [x] Assess module granularity and record the single-step pathway curation.
- [x] Run generic OpenScientist retrieval for the pathway seed.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate gene review; standalone module retired/deferred.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `lgt` | PP_5142 | Q88CN8 | unipathway:UPA00664 | PRESENT | CURATED | PRESENT | Phosphatidylglycerol--prolipoprotein diacylglyceryl transferase (EC 2.5.1.145) |

## Notes

Generated UTC: 2026-07-11T21:26:52.045157+00:00

Curator notes, 2026-07-11:

- Retired the previous `modules/prolipoprotein_diacylglyceryl_transfer.yaml`
  seed: UPA00664 is a single Lgt diacylglyceryl-transfer step and should not be
  represented as a standalone one-part module. Reintroduce it only inside a
  broader multi-part bacterial lipoprotein maturation module.
- Fetched, OpenScientist-backed, curated, and validated the single UniPathway
  member: `lgt` / PP_5142 / Q88CN8.
- `lgt` accepts GO:0008961
  `phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity`,
  GO:0042158 `lipoprotein biosynthetic process`, and GO:0005886 `plasma
  membrane`.
- OpenScientist generic retrieval completed:
  `modules/prolipoprotein_diacylglyceryl_transfer-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research completed and resolved the
  expected local UniPathway candidate set: one candidate, `lgt` / PP_5142 /
  Q88CN8:
  `projects/P_PUTIDA/deep-research/PSEPK__prolipoprotein_diacylglyceryl_transfer__upa00664-deep-research-openscientist.md`.
- OpenScientist gene-level research completed:
  `genes/PSEPK/lgt/lgt-deep-research-openscientist.md`.
- Boundary call: UPA00664 is the Lgt diacylglyceryl transfer step. Downstream
  LspA cleavage, Lnt N-acylation, and Lol sorting remain adjacent biology
  outside this single-gene UniPathway member set.
- Curation caveat: OpenScientist flagged PP_4236/Q88F63 as a possible
  over-propagated Lgt-like annotation; it should not be counted as a second
  UPA00664 member without a separate gene review.
