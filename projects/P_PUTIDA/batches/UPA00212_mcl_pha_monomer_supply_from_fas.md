---
title: "PSEPK UPA00212 UniPathway UPA00212 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00212: UniPathway UPA00212

- Module seed: `mcl_pha_monomer_supply_from_fas`
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
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `phaG` | PP_1408 | O85207 | unipathway:UPA00212 | PRESENT | CURATED | PRESENT | (R)-3-hydroxydecanoyl-ACP:CoA transacylase (EC 2.4.1.-) (3-hydroxyacyl-CoA-acyl carrier protein transferase) |

## Notes

Generated UTC: 2026-07-09T23:50:21.922208+00:00

Curator notes, 2026-07-09:

- New module created and validated:
  `modules/mcl_pha_monomer_supply_from_fas.yaml`.
- `phaG` already had a valid curated review and gene-level Falcon report; Asta
  first-pass retrieval was run for current provider coverage but did not add
  stronger direct evidence than PMID:9727022, UniProt, and the existing Falcon
  gene report.
- Falcon/Edison generic and taxon-aware runs were attempted earlier and failed
  before report creation with Edison HTTP 402 Payment Required, so the batch was
  re-run with OpenScientist.
- OpenScientist generic module research completed:
  `modules/mcl_pha_monomer_supply_from_fas-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research completed and resolved the
  expected local UniPathway candidate set: one candidate, `phaG` / PP_1408 /
  O85207:
  `projects/P_PUTIDA/deep-research/PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-openscientist.md`.
- OpenScientist flagged a module satisfiability issue: if PhaG's native activity
  is thioesterase-like rather than direct ACP:CoA transacylation, complete
  CoA-thioester monomer supply likely requires PP_0763 / Q88PT5, currently an
  orphan-bucket medium-chain-fatty-acid CoA ligase candidate. This is recorded
  as a module knowledge gap and should become a follow-up `fetch-gene` review
  before adding PP_0763 as a confirmed module annoton.
- Boundary call: UPA00212 is the PhaG fatty-acid-synthesis-to-mcl-PHA
  monomer-supply bridge. Downstream PhaC1/PhaC2 polymerization and alternative
  beta-oxidation/PhaJ monomer-supply routes remain adjacent PHA biology outside
  this single-gene UniPathway member set.
