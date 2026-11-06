---
title: "PSEPK UPA00637 osmoregulated periplasmic glucan biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00637: Osmoregulated Periplasmic Glucan Biosynthesis

- Module seed: `osmoregulated_periplasmic_glucan_biosynthesis`
- Pull request: https://github.com/ai4curation/ai-gene-review/pull/2142
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing OpenScientist research files: 4

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `opgH` | PP_5025 | Q88D04 | unipathway:UPA00637 | PRESENT | DONE | PRESENT | Glucans biosynthesis glucosyltransferase H (EC 2.4.1.-) |
| [x] | `opgG` | PP_5026 | Q88D03 | unipathway:UPA00637 | PRESENT | DONE | PRESENT | Glucans biosynthesis protein G |

## Notes

The KT2440 OpgH/OpgG pair supports a qualified inference of OPG-associated biosynthesis. OpgH supplies the inferred membrane glucosyltransferase activity; OpgG participates in the pathway, but its native required chemistry is unresolved. Its inherited hydrolase annotation is retained with explicit ortholog-based evidence limits and is not imposed as the native pathway reaction.

The comparative module represents OpgH-associated synthesis and distinct processing roles across sampled Pseudomonadota. E. coli requires a compatible ACP in its membrane assay; Rhodobacter strain 2.4.1 requires OpgI alongside OpgG/OpgH, with the molecular role of OpgI unresolved. E. coli OpgD hydrolysis and Xanthomonas OpgD alpha-1,6 cyclization are separate reactions. Caulobacter OpgH is a comparative homolog with unresolved native glucan chemistry. Rhodobacter 2.4.1 genetics does not establish the precise product measured in strain WS8. Distinct Ndv/Chv/Cgs routes remain outside the represented mechanism; cyclic product topology alone is not the boundary.


Generated UTC: 2026-07-11T22:11:45.660422+00:00


## 2026-11-06 — comparative audit

The comparative OPG audit now covers 11 COMPLETE gene reviews across five species in Alphaproteobacteria and Gammaproteobacteria. All 91 original annotation payloads and 28 raw/provider sources are preserved; five supported additions yield 96 current rows. Thirteen curated literature references, including two comparative reviews, supply 18 findings. Seven parts and eight annotons distinguish OpgH-associated synthesis, OpgG participation with unresolved native chemistry, conditional OpgI and compatible ACP dependencies, E. coli OpgD hydrolysis, Xanthomonas OpgD cyclization, and the Caulobacter unresolved-product comparator. Two family reviews retain their mixed-function and PAINT-scope limitations. The executable checker passes 24 evidence-scoped cases and ten mutation cases. Full-corpus validation, publication to adopted PR #2142, renewed independent review, CI and actual merge remain pending.
