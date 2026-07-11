---
title: "PSEPK UPA00989 tRNA m7G46 methylation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00989: tRNA m7G46 methylation

- Module seed: `trna_m7g46_methylation`
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
- [x] Open one PR for this module/pathway: [PR #2052](https://github.com/ai4curation/ai-gene-review/pull/2052).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `trmB` | PP_5103 | Q88CS7 | unipathway:UPA00989 | PRESENT | CURATED | PRESENT | tRNA (guanine-N(7)-)-methyltransferase (EC 2.1.1.33) (tRNA (guanine(46)-N(7))-methyltransferase) (tRNA(m7G46)-methyltran |

## Notes

Generated UTC: 2026-07-10T01:06:56.581466+00:00

- Fetched, Asta-backed, curated, and validated the single UniPathway member:
  `trmB` / PP_5103 / Q88CS7.
- Created and validated `modules/trna_m7g46_methylation.yaml` as a compact
  single-reaction UPA00989 module.
- `trmB` accepts the specific GO:0008176 tRNA
  (guanine(46)-N7)-methyltransferase activity and the GO:0106004 tRNA
  (guanine-N7)-methylation process.
- The TreeGrafter `GO:0043527` tRNA methyltransferase complex annotation was
  marked over-annotated because local first-pass evidence supports the TrmB
  enzyme/reaction but not a stable methyltransferase-complex membership.
- Falcon/Edison generic and taxon-aware runs were attempted earlier and failed
  before report creation with Edison HTTP 402 Payment Required, so the batch was
  re-run with OpenScientist.
- OpenScientist generic module research completed:
  `modules/trna_m7g46_methylation-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research completed and resolved the
  expected local UniPathway candidate set: one candidate, `trmB` / PP_5103 /
  Q88CS7:
  `projects/P_PUTIDA/deep-research/PSEPK__trna_m7g46_methylation__upa00989-deep-research-openscientist.md`.
- OpenScientist found UPA00989 covered by the sole KT2440 TrmB candidate. It
  reinforced the existing curation call that GO:0043527 `tRNA
  methyltransferase complex` is likely over-propagated for bacterial TrmB and
  that no Trm82/WDR4-like second subunit should be opened as a missing bacterial
  module step.
- Follow-up biology note: direct KT2440 TrmB biochemical/knockout evidence was
  not located; same-genus Pseudomonas experimental evidence and reviewed
  UniProt/UniRule support are strong enough for a covered call, while KT2440
  substrate scope and phenotype remain optional experiments.
