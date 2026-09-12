---
title: "PSEPK MutH-independent mismatch repair"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [mutS, mutL, uvrD, xseA, xseB, sbcB, recJ]
autolink_gene_symbols: false
---

# PSEPK MutH-independent mismatch repair

- Pull request: [#2258](https://github.com/ai4curation/ai-gene-review/pull/2258)

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

The module also represents DnaN beta-clamp context, SSB-coated excision
intermediates, DnaE-mediated gap filling, and LigA-mediated nick sealing. These
are shared replication/repair functions and remain outside this focused
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
- Constrain broad MutL and UvrD PANTHER families with their required molecular
  functions, and use the Exonuclease I-specific `PTHR11046:SF11` selector
  rather than the RNA-exonuclease-containing parent family.
- Refine the RecJ directional parent to GO:0045145, which explicitly captures
  single-stranded DNA and 5'-to-3' exonuclease activity.

## Evidence

- PMID:31599106 directly establishes a MutS/MutL correction hierarchy in
  KT2440 and reports no canonical MutH component.
- PMID:30292721 directly supports a substantial but redundant UvrD
  contribution in KT2440.
- PMID:23969026 directly characterizes duplex-DNA nicking by the close
  *P. aeruginosa* MutL exemplar.
- The reproducible local Q88DD1-Q9HUL8 global alignment retains input FASTA
  records, checksums, scoring parameters, scripts, and output; it contains 521
  identical residues among 627 aligned residue pairs (83.0941%).

## Workflow

- [x] Fetch and curate the seven selected gene reviews.
- [x] Curate the reusable species-neutral module.
- [x] Validate the gene reviews.
- [x] Validate and render the final module.
- [x] Attempt module-level OpenScientist deep research; the corrected request
  exhausted the 7,200-second provider timeout without a report.
- [x] Attempt module + pathway + PSEPK OpenScientist deep research; the
  corrected request exhausted the 7,200-second provider timeout without a
  report.
- [x] Attempt OpenScientist deep research for selected genes; `uvrD`, `xseA`,
  `xseB`, `sbcB`, and `recJ` returned reports, while the corrected `mutS` and
  `mutL` requests each exhausted the 7,200-second provider timeout.
- [x] Open one PR for this module/pathway.
- [x] Address the first automated review, including family selectors,
  reproducible MutL sequence provenance, RecJ term specificity, and UvrD
  positive evidence.
- [ ] Shepherd the updated PR through re-review and CI.

## Notes

The [batch TSV](ppu03430_muth_independent_mismatch_repair.tsv) preserves the
KEGG-derived candidate inventory and adds current local review and
OpenScientist-retrieval status columns. It is useful for audit and later
curation of shared machinery, but is intentionally broader than this focused
review.

The generic and species-aware OpenScientist requests were each allowed the full
configured 7,200 seconds with three iterations. Neither returned a report, so
the module cites the direct Pseudomonas studies, exact gene reviews, UniProt
exemplars, and TreeGrafter provenance that can be inspected locally.

The completed UvrD report recovered the conserved 3'-to-5' SF1A helicase
mechanism and UvrD's participation in several DNA-maintenance pathways. Its
mismatch-repair discussion relies mainly on orthologs and does not supersede
the direct KT2440 result in PMID:30292721: UvrD makes a strong but nonexclusive
contribution, so it remains a pathway participant without being modeled as the
only possible repair helicase.

The XseA, XseB, SbcB, and RecJ reports corroborated the exact-record enzyme or
complex assignments and the conserved directional nuclease activities. Their
mismatch-repair claims remain orthology-based, so these proteins are retained
as alternative candidate excision routes rather than promoted to
organism-specific mismatch-repair annotations.

The reusable module now includes DnaN and SSB because they are mechanistically
central shared roles: beta-clamp context can orient or stimulate MutL incision,
and SSB stabilizes exposed ssDNA while coordinating processing proteins. They
are not promoted to dedicated PSEPK mismatch-repair gene targets in this batch.

Two genomic-context claims in the provider output were rejected against the
exact KT2440 records. The XseB report incorrectly identifies `PP_0528` as XseA
and infers an adjacent `xseA`/`xseB` operon; `PP_0528` is IspA, while XseA is
Q88P26 at `PP_1027`. The RecJ report likewise calls `recJ` (`PP_1477`) adjacent
to `recO` (`PP_1435`), although those loci are not adjacent. Neither claim is
used in the gene reviews or module.
