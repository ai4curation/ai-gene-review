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
- Core pathway proteins: 4
- Terminal-enzyme paralogs reviewed: 3
- Substrate-entry branches: 2
- Shared downstream reactions: 2
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a multi-step, species-neutral module boundary.
- [x] Separate the aldarate route from KEGG-map spillover and paralogous routes.
- [x] Fetch the four core PSEPK genes and the two alternative terminal-enzyme paralogs.
- [x] Review every GOA annotation for all six proteins.
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
| 3 | 2,5-dioxovalerate oxidation to 2-oxoglutarate | `PP_3602` (leading candidate); `PP_1256`, `PP_2585` (alternatives) | Q88GW5; Q88NF5; Q88JR4 | Reaction covered at family level; paralog contribution and NAD+/NADP+ preference unresolved |

The reaction chain is satisfiable for both D-glucarate and D-galactarate in
KT2440. The two entry reactions converge on
5-dehydro-4-deoxy-D-glucarate. PP_3602 is the strongest terminal-enzyme
candidate by synteny, but the available evidence does not prove that it is the
unique physiological paralog.

## Annotation Decisions

- The `PP_3599` TreeGrafter annotation to
  4-hydroxy-tetrahydrodipicolinate synthase is removed. Q88GW8 is a reviewed
  KDGDH with Rhea 24608 and three substrate-specific family assignments; the
  DapA annotation crossed a paralog boundary within the shared TIM-barrel fold.
- The `garD` D-galacturonate-catabolism annotation is kept as non-core because
  characterized KT2440 Udh feeds D-galacturonate into D-galactarate before the
  GarD reaction; the direct D-galactarate process remains the core annotation.
- Broad `lyase activity` mappings are marked as over-annotations when exact
  substrate-specific terms are well supported. For the three terminal
  paralogs, GO:0016620 is retained as the defensible core molecular-function
  class because no assay resolves NAD+ versus NADP+ preference; the
  NADP+-specific GO:0047533 IEAs are left `UNDECIDED`.
- No module-level molecular function or redundant cytoplasm/cytosol pair is
  asserted.

## Excluded Candidates

| Gene | Reason outside this module boundary |
|---|---|
| `udh` | Oxidizes hexuronates to aldarates upstream of the substrate-specific entry reactions; it is not required when glucarate or galactarate is supplied |
| `udg` | UDP-glucose dehydrogenase belongs to nucleotide-sugar metabolism rather than this catabolic route |
| `PP_1256` | KGSADH-family paralog beside characterized hydroxyproline genes; candidate for that route, not established as aldarate-specific |
| `PP_2585` | KGSADH-family paralog outside the local `garD`/KDGDH locus; nearby amino-acid/polyamine genes suggest a hypothesis, not a demonstrated pathway assignment |

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
- The terminal leaf uses the cofactor-neutral GO:0016620 reaction class and
  records both RHEA:11296 and RHEA:47152. Q88GW5, Q88NF5, and Q88JR4 are shown
  as exact KT2440 family exemplars; this does not assert equal pathway usage.

## Research Status

The completed OpenScientist
[module-level report](../../../modules/bacterial_glucarate_and_galactarate_catabolism-deep-research-openscientist.md)
supports the reusable three-stage boundary. The separate
[module/pathway/taxon report](../deep-research/PSEPK__glucarate_galactarate_catabolism__ppu00053-deep-research-openscientist.md)
identifies aldarate-locus PP_3602 as the leading terminal candidate. Its claim
that PP_3602 is the uniquely correct paralog is stronger than the retrieved
evidence and is not adopted here. The report finds no
GarL-supported *E. coli*-type downstream branch, and identifies PP_3600,
PP_4758, PP_3603, and PP_4759 as accessory transport/regulatory context rather
than core reaction steps. These are retrieval-supported conclusions; exact
reaction claims remain grounded in GO, Rhea, UniProt, PANTHER, and PAINT
records. PP_1256 and PP_2585 remain unresolved without direct physiological
evidence, and none of the three paralogs has a measured NAD+/NADP+ preference.

## Validation

All six gene reviews pass `just validate`. The module passes LinkML
`ModuleReview` validation and the dedicated semantic module validator. The
module, six gene reviews, and project page render successfully; `git diff
--check` is clean.
