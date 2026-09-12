---
title: "PSEPK ppu03440 RuvABC Holliday-junction-processing batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03440: RuvABC Holliday-junction processing

- Reusable module: `modules/bacterial_ruvabc_holliday_junction_processing.yaml`
- Correct pathway boundary: RuvA junction recognition, RuvB or RecG branch migration, and RuvC resolution
- KEGG-derived candidates inspected: 24
- Newly reviewed PSEPK proteins: 4
- Revised existing review: 1
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate late Holliday-junction processing from RecFOR, RecBCD, RecA strand exchange, and replication restart.
- [x] Confirm the contiguous KT2440 `ruvCAB` locus and exact protein accessions.
- [x] Assign junction binding to RuvA, ATP-dependent motor activity to RuvB, and nuclease catalysis to RuvC.
- [x] Model RecG as a parallel branch-migration route rather than a RuvABC subunit or resolvase.
- [x] Exclude PP_0151 as a spurious ML-named resolvase candidate.
- [x] Add reviewed bacterial exemplars and the directly relevant RuvB PAINT node.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Four-way-junction recognition and motor loading | `ruvA` | Q88NJ1 | Covered |
| 2 | Canonical ATP-dependent branch migration | `ruvB` | Q88NJ0 | Covered |
| 2 | Alternative branched-DNA migration | `recG` | Q88C73 | Covered as a parallel route |
| 3 | Symmetric junction cleavage and resolution | `ruvC` | Q88NJ2 | Covered |

The core RuvABC pathway is complete in KT2440, with RecG providing additional
branch-migration capacity. The lack of a RusA-like backup is not a pathway hole
because RuvC supplies the conserved required resolution activity.

## Annotation Decisions

- RuvA independently enables four-way-junction DNA binding and contributes to
  RuvAB helicase activity. Generic independent helicase activity is marked
  over-annotated, while ATP binding is removed because the ATPase motor is RuvB.
- RuvB independently enables the branch-migration motor. Generic DNA binding is
  retained as non-core direct-contact evidence, while the imported `enables`
  qualifier on four-way-junction binding is modified to a complex contribution.
- RuvB's duplicate core-function summaries are consolidated, and generic
  cytoplasmic localization is retained only as non-core context.
- RuvC retains exact crossover-junction endonuclease activity; broad DNA
  endonuclease and nucleic-acid-binding parents are marked over-annotated.
- RecG retains exact 3-prime-to-5-prime DNA-helicase and ATP-hydrolysis activities.
- PP_0151 has no GOA annotations and is described as a secreted DUF2388 protein
  of unknown function, not as a Holliday-junction resolvase.

## Boundary Decisions

- RecFOR gap repair, RecBCD end resection, and RecA strand exchange are upstream modules.
- Replication restart and fork-reversal consequences remain outside this narrowly defined module.
- RecG is parallel to RuvAB; it is not forced into the canonical RuvABC complex.
- The RecG-to-RuvC connection is unverified because the downstream resolver of
  RecG-generated junctions is taxon-dependent and has not been tested in KT2440.
- No family selector uses the broad PTHR47964 assignment because that family conflates RecG and Mfd.
- Molecular functions occur only on leaf annotons; no generic cytoplasmic locations appear at module level.

## Grounding

Every leaf has a concrete KT2440 UniProt implementation and a reviewed E. coli
exemplar. PTN000349951 grounds RuvB four-way-junction helicase activity and
recombinational repair. Ortholog-of selectors anchored to reviewed E. coli proteins
ground RuvA and RecG where a PANTHER selector would be absent or misleading, and
PTHR30194:SF3 grounds RuvC. Primary studies PMID:9501105 and PMID:7923356 establish
the canonical RuvA-RuvB-RuvC division of labor and RuvC catalytic architecture;
PMID:18375550 supports RecG as a separate, taxon-sensitive migration route.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Local UniProt, GOA, PANTHER, PAINT, InterPro,
and Rhea records were used to resolve exact identifiers and reject PP_0151.

## Validation

The four new reviews, revised RuvB review, reusable module, and project page are
validated and rendered before publication.
