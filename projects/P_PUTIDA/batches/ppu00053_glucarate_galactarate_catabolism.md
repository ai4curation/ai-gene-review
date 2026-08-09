---
title: "PSEPK ppu00053 glucarate and galactarate catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00053: glucarate and galactarate catabolism

- Reusable module: `modules/glucarate_galactarate_catabolism.yaml`
- KEGG ppu00053 candidates inspected: 8
- Selected pathway proteins: 4
- Substrate-entry branches: 2
- Shared downstream reactions: 2
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a multi-step, species-neutral module boundary.
- [x] Separate the aldarate route from KEGG-map spillover and paralogous routes.
- [x] Fetch the four selected PSEPK genes.
- [x] Review every GOA annotation for the selected genes.
- [x] Integrate the module/pathway/taxon OpenScientist report.
- [x] Validate module and gene reviews.
- [x] Render module, gene, and project pages.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK gene | UniProt | Decision |
|---|---|---|---|---|
| 1a | D-glucarate dehydration | `gudD` | Q88DR6 | Covered by the glucarate-specific entry branch |
| 1b | D-galactarate dehydration | `garD` | Q88GW6 | Covered by the galactarate-specific entry branch |
| 2 | 5-dehydro-4-deoxyglucarate dehydration | `PP_3599` | Q88GW8 | Covered by reviewed KDGDH |
| 3 | 2,5-dioxovalerate oxidation to 2-oxoglutarate | `PP_3602` | Q88GW5 | Covered; NADP+ GO term accepted, NAD+ activity also predicted |

The route is satisfiable for both D-glucarate and D-galactarate in KT2440.
The two entry reactions converge on 5-dehydro-4-deoxy-D-glucarate and use the
same two downstream enzymes.

## Annotation Decisions

- The `PP_3599` TreeGrafter annotation to
  4-hydroxy-tetrahydrodipicolinate synthase is removed. Q88GW8 is a reviewed
  KDGDH with Rhea 24608 and three substrate-specific family assignments; the
  DapA annotation crossed a paralog boundary within the shared TIM-barrel fold.
- The `garD` D-galacturonate-catabolism annotation is removed. Q88GW6 is the
  GarD SF1 protein, whereas altronate/UxaA chemistry belongs to a different
  subfamily.
- Broad `lyase activity` and `oxidoreductase activity` mappings are marked as
  over-annotations when exact substrate-specific molecular functions exist.
- No module-level molecular function or redundant cytoplasm/cytosol pair is
  asserted.

## Excluded Candidates

| Gene | Reason outside this module boundary |
|---|---|
| `udh` | Oxidizes hexuronates to aldarates upstream of the substrate-specific entry reactions; it is not required when glucarate or galactarate is supplied |
| `udg` | UDP-glucose dehydrogenase belongs to nucleotide-sugar metabolism rather than this catabolic route |
| `PP_1256` | A 2,5-dioxovalerate dehydrogenase in the hydroxyproline locus; reserved for the separate hydroxyproline module |
| `PP_2585` | A paralogous 2,5-dioxovalerate dehydrogenase outside the local `garD`/KDGDH locus; OpenScientist found polyamine-associated neighborhood context, but its physiological route remains unverified |

## Module Decisions

- The reusable boundary contains a `ONE_OR_MORE` substrate-entry variant set
  followed by two required shared reactions.
- Every leaf carries an exact PSEPK UniProt exemplar and an additional reviewed
  exemplar where one was resolved.
- Canonical PAINT nodes PTN000350982 and PTN000776262 ground the GudD and GarD
  branch functions, respectively. No PTN is asserted for the downstream
  activities because the local PAINT files do not contain those exact terms.
- Transport, upstream uronate production, and downstream 2-oxoglutarate use are
  outside the pathway boundary.

## Research Status

The completed [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__glucarate_galactarate_catabolism__ppu00053-deep-research-openscientist.md)
supports the three-stage boundary and all four selected PSEPK assignments. It
also distinguishes the aldarate-locus PP_3602 from PP_1256 and PP_2585, finds no
GarL-supported *E. coli*-type downstream branch, and identifies PP_3600,
PP_4758, PP_3603, and PP_4759 as accessory transport/regulatory context rather
than core reaction steps. These are retrieval-supported conclusions; exact
reaction claims remain grounded in GO, Rhea, UniProt, PANTHER, and PAINT
records, and PP_2585 remains unresolved without direct physiological evidence.

## Validation

All four gene reviews pass `just validate`. The module passes LinkML
`ModuleReview` validation and the dedicated semantic module validator. The
module, four gene reviews, and project page render successfully; `git diff
--check` is clean.
