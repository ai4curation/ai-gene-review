---
title: "PSEPK ppu03440 RecFOR single-strand-gap repair batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03440: RecFOR single-strand-gap repair

- Reusable module: `modules/bacterial_recfor_gap_repair.yaml`
- Correct pathway boundary: RecQ/RecJ gap extension, SSB coating, RecFOR-mediated RecA loading, and RecA strand exchange
- KEGG-derived candidates inspected: 24
- Newly reviewed PSEPK proteins: 6
- Revised existing review: 1
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Split the combined KEGG homologous-recombination map into reusable pathway modules.
- [x] Recover `recQ`, which is required for presynaptic gap extension but absent from the raw candidate list.
- [x] Retain `recJ` and `ssb` as shared RecFOR components despite their primary metadata buckets.
- [x] Model RecF, RecO, and RecR as a three-subunit mediator role.
- [x] End the module at RecA strand exchange rather than absorbing downstream RuvABC resolution.
- [x] Exclude RecBCD end resection, replisome subunits, replication restart, and SOS regulation.
- [x] Add reviewed UniProt exemplars and directly relevant RecQ and RecA PAINT nodes.
- [x] Validate and render the module, genes, and project page.
- [x] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Helicase-dependent gap extension | `recQ` | Q88EE9 | Covered; recovered outside raw KEGG candidates |
| 2 | Exonuclease-dependent gap extension | `recJ` | Q88MU1 | Covered; shared repair enzyme |
| 3 | Exposed ssDNA protection | `ssb` | Q88QK5 | Covered; shared with replication and other repair pathways |
| 4 | RecA loading mediator | `recF`, `recO`, `recR` | Q88RW7, Q88MY3, Q88F32 | Covered as a three-subunit role |
| 5 | Homology search and strand exchange | `recA` | Q88ME4 | Covered; direct KT2440 phenotype literature exists |

The five-part pathway is complete in KT2440. This is a gene-set satisfiability
statement, not a claim of efficient recombination: KT2440 has a documented weak
SOS response and poor homologous-recombination efficiency.

## Annotation Decisions

- RecJ's generic 5-prime-to-3-prime exonuclease annotation is modified to the
  single-stranded-DNA-specific child term GO:0045145.
- RecQ's exact directional helicase activity is retained; generic helicase,
  hydrolase, nucleotide-binding, and nucleic-acid-binding parents are marked
  over-annotated.
- RecA receives the exact DNA strand exchange activity GO:0000150, grounded by
  its UniProt mechanism and the local PAINT ancestral node.
- RecF's imported repair-synthesis annotation is removed because RecF loads
  recombinase and does not catalyze DNA synthesis.
- RecF, RecO, and RecR receive DNA recombinase assembly GO:0000730 as the
  specific shared process for their mediator role, using reviewed bacterial
  exemplars rather than the module itself as ISS evidence.
- RecO receives single-stranded DNA binding GO:0003697, filling the molecular-
  function gap on the RecO leaf with homolog-level experimental support.
- RecQ replisome membership is removed: replication-associated activity does
  not establish stable membership in the bacterial replisome.

## Boundary Decisions

- RecBCD processing of double-strand-break ends is a parallel presynaptic module.
- RuvABC branch migration and Holliday-junction resolution are a downstream module.
- PriA/PriC replication restart, RecX/RadA regulation, SbcCD end processing,
  DprA-mediated transformation, and SOS transcriptional control remain outside.
- DNA polymerase III subunits and generic exonucleases inherited from the KEGG
  map are not RecFOR module parts.
- Molecular functions occur only on leaf annotons; no cytoplasm/cytosol terms
  are repeated at module level.

## Grounding

Every leaf is grounded by a concrete KT2440 UniProt protein and a reviewed E. coli
exemplar from the matching PANTHER family. PTN000344873 grounds RecQ directional
helicase activity and recombination, while PTN000534381 grounds RecA strand
exchange and recombinational repair. Primary literature grounds RecO-mediated
SSB displacement (PMID:32297860), Pseudomonas RecR mediator complexes
(PMID:29633970), and the separable RecJ/RecQ and RecFOR presynaptic roles
(PMID:35653392).

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Local UniProt, GOA, PANTHER, PAINT, and GO
records were used to correct the report's module boundary and exact identifiers.

## Validation

The six new reviews, revised RecA review, reusable module, and project page are
validated and rendered before publication.
