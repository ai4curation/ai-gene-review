---
title: "PSEPK UPA00729 tRNA ms2io6A37 hydroxylation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00729: tRNA ms2io6A37 hydroxylation

- Pathway seed: `trna_ms2io6a37_hydroxylation` (single-step; no standalone module retained)
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
- [x] Open one PR for this module/pathway: [PR #2054](https://github.com/ai4curation/ai-gene-review/pull/2054).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `miaE` | PP_2188 | Q88KV1 | unipathway:UPA00729 | PRESENT | CURATED | PRESENT | tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37) hydroxylase (EC 1.14.99.69) (2-methylthio-N6-isopentenyladenosine( |

## Notes

Generated UTC: 2026-07-11T20:27:48.376449+00:00

- Retired the previous `modules/trna_ms2io6a37_hydroxylation.yaml` seed:
  UPA00729 is a single MiaE hydroxylation step and should not be represented as
  a standalone one-part module. Reintroduce it only inside a broader multi-part
  tRNA A37 hypermodification module.
- OpenScientist gene-level research completed:
  `genes/PSEPK/miaE/miaE-deep-research-openscientist.md`.
- OpenScientist generic retrieval completed:
  `modules/trna_ms2io6a37_hydroxylation-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research completed:
  `projects/P_PUTIDA/deep-research/PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-openscientist.md`.
- `miaE` is a covered enzyme step with direct P. putida experimental and
  structural evidence, so GO:0045301 remains accepted as the core molecular
  function.
- Important caveat from the taxon-aware report: KT2440 appears to lack canonical
  MiaB, the upstream methylthiotransferase that makes ms2i6A37. The native
  product may therefore be io6A37 rather than ms2io6A37 unless direct KT2440
  tRNA nucleoside profiling or a cryptic MiaB candidate supports ms2i6A37
  formation.
- Follow-up promoted by this batch: review PP_1197/RimO separately to prevent
  paralog over-propagation as MiaB.
