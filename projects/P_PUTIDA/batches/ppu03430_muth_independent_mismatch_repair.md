---
title: "PSEPK MutH-independent mismatch repair"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [mutS, mutL, uvrD, xseA, xseB, sbcB, recJ]
autolink_gene_symbols: false
---

# PSEPK MutH-independent mismatch repair

This batch curates the dedicated recognition, incision, unwinding, and candidate
excision machinery for the MutH-independent mismatch-repair route in
*Pseudomonas putida* KT2440. The broad KEGG membership extract is retained in
the accompanying TSV for provenance, but shared replication proteins are not
treated as pathway-specific gene-review targets.

## Scope

- `mutS` (PP_1626; Q88ME7): ATP-dependent mismatch recognition.
- `mutL` (PP_4896; Q88DD1): repair coordination and inferred strand incision.
- `uvrD` (PP_5352; Q88C31): directly supported but nonexclusive repair helicase.
- `sbcB` (PP_1365; Q88N51): candidate 3'-to-5' excision route.
- `recJ` (PP_1477; Q88MU1): candidate 5'-to-3' excision route.
- `xseA` (PP_1027; Q88P26) and `xseB` (PP_0529; Q88QG5):
  candidate bidirectional Exonuclease VII route.

The module also represents DnaE-mediated gap filling and LigA-mediated nick
sealing. These are shared replication/repair functions and remain outside this
gene-review batch.

## Curation Decisions

- Model the pathway without MutH or Dam-directed strand discrimination.
- Place molecular functions on leaf annotons, not on pathway-level nodes.
- Represent the three candidate exonuclease implementations as `ONE_OR_MORE`;
  current PSEPK evidence does not resolve a single obligatory route.
- Preserve the finding that UvrD contributes strongly to mismatch repair while
  residual repair persists in its absence.
- Use the directly characterized *Pseudomonas aeruginosa* MutL as the
  endonuclease exemplar for the close PSEPK ortholog; do not portray the
  inferred activity as direct KT2440 biochemistry.

## Evidence

- PMID:31599106 directly establishes a MutS/MutL correction hierarchy in
  KT2440 and reports no canonical MutH component.
- PMID:30292721 directly supports a substantial but redundant UvrD
  contribution in KT2440.
- PMID:23969026 directly characterizes duplex-DNA nicking by the close
  *P. aeruginosa* MutL exemplar.

## Workflow

- [x] Fetch and curate the seven selected gene reviews.
- [x] Curate the reusable species-neutral module.
- [x] Validate the gene reviews.
- [x] Validate and render the final module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [ ] Run OpenScientist deep research for selected genes.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Notes

The batch TSV is the unmodified KEGG-derived candidate inventory. It is useful
for audit and later curation of shared machinery, but is intentionally broader
than this focused review.
