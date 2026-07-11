---
title: "PSEPK UPA00664 prolipoprotein diacylglyceryl transfer batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00664: prolipoprotein diacylglyceryl transfer

- Module seed: `prolipoprotein_diacylglyceryl_transfer`
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing OpenScientist gene research files: 1

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `lgt` | PP_5142 | Q88CN8 | unipathway:UPA00664 | PRESENT | CURATED | PRESENT | Phosphatidylglycerol--prolipoprotein diacylglyceryl transferase (EC 2.5.1.145) |

## Notes

Generated UTC: 2026-07-11T21:26:52.045157+00:00

Curator notes, 2026-07-11:

- New module created and validated:
  `modules/prolipoprotein_diacylglyceryl_transfer.yaml`.
- Fetched, OpenScientist-backed, curated, and validated the single UniPathway
  member: `lgt` / PP_5142 / Q88CN8.
- `lgt` accepts GO:0008961
  `phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity`,
  GO:0042158 `lipoprotein biosynthetic process`, and GO:0005886 `plasma
  membrane`.
- OpenScientist generic module research completed:
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
