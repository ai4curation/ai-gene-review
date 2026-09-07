---
title: "PSEPK bacterial RNA degradation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [rne, rhlB, rhlE, pnp, rnr]
autolink_gene_symbols: false
---

# PSEPK bacterial RNA degradation

- Module: `bacterial_rna_degradation`
- Source bucket: KEGG `ppu03018` (RNA degradation)
- Selected reviews: `rne`, `rhlB`, `rhlE`, `pnp`, and `rnr`
- OpenScientist module/pathway/taxon research: complete in 1,237.09 seconds

## Boundary

This curation does not reproduce the broad KEGG bucket. The reusable module
covers an RNase E-initiated RNA-decay route with three substantive parts:
endonucleolytic initiation and organization, optional DEAD-box-helicase
assistance for structured substrates, and processive 3'-to-5' exonucleolysis.
It is scoped to Gammaproteobacteria because the modeled RNase E-centered
architecture and partner variants are not universal bacterial machinery.

RppH-dependent 5'-end priming, PAP I, Hfq-mediated regulation, polyphosphate
metabolism, chaperones, RecQ, Rho, and ribosome-biogenesis machinery are
adjacent to RNA turnover but outside this boundary. Enolase Q88MF9 remains in
the KEGG source bucket but is excluded because no direct evidence establishes
its recruitment into a KT2440 RNA-degradation complex.

## Functional Parts

| Part | Reusable alternatives | PSEPK exemplars | Assessment |
|---|---|---|---|
| RNase E initiation and organization | RNase E | Q88LM4 (`rne`) | Enzyme identity covered; exact partner recruitment unresolved |
| Optional structured-RNA unwinding | RhlB or RhlE | Q88NB7 (`rhlB`), Q88D48 (`rhlE`) | Both enzyme identities covered; complex membership unresolved |
| Processive 3'-to-5' exonucleolysis | PNPase or RNase R | Q88DW0 (`pnp`), Q88DE6 (`rnr`) | Both enzyme identities covered; complex membership unresolved |

Verified E. coli K-12 exemplars orient each conserved family: P21513 (RNase E),
P0A8J8 (RhlB), P25888 (RhlE), P05055 (PNPase), and P21499 (RNase R). Only the
RhlE PANTHER subfamily is asserted because its official label and membership of
both Q88D48 and P25888 were verified; the other families use checked InterPro
identifiers rather than uncertain PANTHER/PTN claims.

## Annotation-Reviewer Passes

Every selected gene received a complete annotation-reviewer pass:

- `rne`: 14/14 GOA rows adjudicated; no pending actions.
- `rhlB`: 8/8 GOA rows adjudicated; no pending actions.
- `rhlE`: 11/11 GOA rows adjudicated; temperature response remains explicitly `UNDECIDED`.
- `pnp`: 10/10 GOA rows adjudicated; no pending actions.
- `rnr`: 9/9 GOA rows adjudicated; no pending actions.

The reviews distinguish conserved molecular function from target-specific
complex composition. Same-genus evidence supports RhlE/RNase R as a reusable
alternative, but it is not treated as proof that KT2440 uses that complex.
The earlier dedicated `rhlB` OpenScientist request exhausted 7,200 seconds and
produced no artifact; its review uses UniProt, full-text E. coli biochemistry,
and the module-level species-aware research instead.

The wave134 OpenScientist report completed successfully in 1,237.09 seconds
(20 minutes 37 seconds) and returned nine citations plus HTML/PDF artifacts. It
supports module satisfiability and exclusion of broad KEGG co-listings, but is
used as retrieval support rather than authority. In particular, its expanded
boundary includes RppH, PcnB, and Hfq as accessory steps, whereas the curated
module keeps those upstream/regulatory activities separate. It also infers
KT2440 partner recruitment from other Pseudomonas species more confidently than
the direct target evidence warrants. The module therefore retains both partner
axes as unresolved KT2440 alternatives.

## Status

- [x] Define a coherent, species-neutral, three-part boundary.
- [x] Curate all selected PSEPK gene reviews.
- [x] Document annotation-reviewer consultation for every selected gene.
- [x] Verify cross-species exemplars and retained PANTHER membership.
- [x] Complete and assess OpenScientist module/pathway/taxon research.
- [x] Run gene, module, and route validation before the final rebase.
- [x] Run final post-rebase validation.
- [x] Render final gene, module, research, and project outputs.
- [x] Rebase current `origin/main` and regenerate rendered outputs from final sources.
- [x] Prepare the rebased branch for a non-draft PR and review request.

## Evidence

- `modules/bacterial_rna_degradation.yaml`
- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial_rna_degradation__ppu03018-deep-research-openscientist.md)
- `PMID:16275923`: functional RhlB-PNPase coupling in E. coli.
- `PMID:15705581`: same-genus RNase E-RhlE-RNase R complex.
- `PMID:33089610`: direct KT2440 ribonuclease deletion study.
- `PMID:40096066`: Pseudomonas RNase E scaffold interactions.
