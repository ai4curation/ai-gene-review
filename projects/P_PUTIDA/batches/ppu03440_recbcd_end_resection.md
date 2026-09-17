---
title: "PSEPK ppu03440 RecBCD double-strand-end resection batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03440: RecBCD double-strand-end resection

- Reusable module: `modules/bacterial_recbcd_end_resection.yaml`
- Correct pathway boundary: double-strand-end engagement, bipolar unwinding, regulated resection, and RecA loading
- KEGG-derived candidates inspected: 24
- Newly reviewed PSEPK proteins: 2
- Revised existing review: 1
- Reused downstream RecA review: 1
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate RecBCD double-strand-end processing from RecFOR gap repair.
- [x] Confirm the contiguous KT2440 `recD-recB-recC` operon and exact UniProt accessions.
- [x] Distinguish RecB and RecD motor directionality.
- [x] Restrict independent Exonuclease V catalysis to RecB while recording RecC/RecD contributions.
- [x] Retain a taxon-dependent switching step without importing the E. coli Chi octamer.
- [x] End at RecA loading rather than absorbing strand exchange or RuvABC resolution.
- [x] Add reviewed UniProt exemplars and a directly relevant RecB-family PAINT node.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | End engagement and holoenzyme organization | `recC` | Q88DZ4 | Covered |
| 2 | 3-prime-to-5-prime unwinding motor | `recB` | Q88DZ5 | Covered |
| 2 | 5-prime-to-3-prime unwinding motor | `recD` | Q88DZ6 | Covered |
| 3 | Recombinogenic resection switch | `recC` plus unknown signal | Q88DZ4 | Protein covered; KT2440 signal unresolved |
| 4 | Exonuclease V resection and 3-prime-tail generation | `recB` | Q88DZ5 | Covered |
| 5 | RecA loading | `recB`, `recA` | Q88DZ5, Q88ME4 | Covered by conserved mechanism; target-strain detail inferred |

The core RecBCD pathway is complete in KT2440. The unresolved item is regulatory
signal identity, not a missing protein. Primary P. aeruginosa and P. putida
clone experiments show that their RecBCD-like enzymes do not activate the
E. coli Chi octamer.

## Annotation Decisions

- RecC's imported DNA-helicase, ATP-binding, and catalytic-DNA-activity terms are
  removed because RecC is the non-motor scaffold and recognition subunit.
- RecC and RecD no longer independently enable Exonuclease V activity; their
  core summaries use `contributes_to_molecular_function`, while RecB retains the
  catalytic GO:0008854 assignment.
- RecD's exact 5-prime-to-3-prime DNA helicase activity is core; generic helicase
  and single-stranded-DNA helicase terms are retained as true non-core views.
- The existing RecB review is corrected to state that the E. coli Chi octamer
  is not recognized and that the KT2440 switching signal is unknown.

## Boundary Decisions

- RecFOR/RecJ/RecQ gap repair is a parallel presynaptic pathway.
- RecA strand exchange and RuvABC branch migration/resolution are downstream.
- SbcCD, ExoI, ExoVII, replication restart, replisome subunits, and NHEJ remain
  separate modules or accessory context.
- AddAB is a lineage alternative and is not expected in this RecBCD-containing taxon.
- Molecular functions occur only on leaf annotons; no generic cytoplasmic
  locations are repeated at module level.

## Grounding

The three subunit roles are grounded by concrete KT2440 UniProt proteins and
reviewed E. coli exemplars. PTN000116141 supports the RecB directional helicase
activity. PMID:20195537 supplies pseudomonad genetic context, including the
unusual requirement for RecD in DNA-damage resistance. PMID:2559208 is the
primary P. aeruginosa/P. putida source for failure to activate E. coli Chi.
The RecD selector uses NCBIfam:TIGR01447 because the broader PTHR43788:SF6
subfamily also contains standalone RecD2/HelB helicases.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Local UniProt, GOA, PANTHER, PAINT, Rhea,
and cached full-text records were used to correct qualifier and taxon-transfer errors.

## Validation

The two new reviews, revised RecB review, reusable module, and project page are
validated and rendered before publication.
