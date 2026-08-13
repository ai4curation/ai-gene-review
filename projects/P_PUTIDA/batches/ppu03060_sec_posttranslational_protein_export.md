---
title: "PSEPK ppu03060 post-translational Sec protein-export batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03060: post-translational Sec protein export

- Reusable module: `modules/bacterial_sec_posttranslational_protein_export.yaml`
- Correct pathway boundary: SecB precursor carriage, SecA ATPase motor, SecYEG
  channel, SecDF-YajC accessory completion, and LepB signal-peptide cleavage
- KEGG-derived candidates inspected: 19 proteins and 2 overlapping ncRNA features
- Newly reviewed PSEPK proteins: 8
- Revised existing review: 1
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate the post-translational Sec route from cotranslational SRP targeting.
- [x] Separate Tat export of folded proteins and YidC membrane insertion into sibling modules.
- [x] Keep lipoprotein signal peptidase II in the existing bacterial lipoprotein-maturation module.
- [x] Keep Xcp type II outer-membrane secretion outside the inner-membrane Sec module.
- [x] Assign ATPase activity only to SecA and transporter activity to the appropriate channel leaves.
- [x] Add exact KT2440 implementations, reviewed E. coli exemplars, and relevant PAINT nodes.
- [x] Validate and render the module, gene reviews, and project page.
- [x] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Unfolded-precursor carriage and SecA delivery | `secB` | Q88CX7 | Covered |
| 2 | ATP-driven protein-export motor | `secA` | Q88N69 | Covered |
| 3 | SecYEG protein-conducting channel | `secY`, `secE`, `secG` | Q88QL5, Q88QP7, A0A140FWQ9 | Covered |
| 4 | PMF-assisted SecDF-YajC completion complex | `secD`, `secF`, `yajC` | Q88PL5, Q88PL4, Q88PL6 | Present; accessory |
| 5 | Type I signal-peptide cleavage | `lepB` | Q88MY6 | Covered |

The canonical Gram-negative post-translational Sec route is complete in KT2440.
SecDF-YajC is represented as an accessory completion and throughput complex,
not as an absolute requirement for every substrate.

## Annotation Decisions

- SecB is modeled as an unfolded-protein carrier that maintains precursor
  translocation competence; the imported protein-folding annotation is removed.
- SecA alone retains protein-exporting ATPase activity.
- SecY independently carries the channel activity, while SecE and SecG
  contribute to the assembled SecYEG transporter.
- The protein-transporting ATPase annotations on SecG, SecD, and SecF are
  corrected: these subunits do not hydrolyze ATP. SecD and SecF contribute to
  `GO:0009977` proton-motive-force-dependent protein transmembrane transporter
  activity; SecG contributes to `GO:0008320` protein transmembrane transporter
  activity as a channel accessory. None independently enables those collective
  transporter functions.
- YajC is retained as a SecDF-associated complex subunit, but it receives no
  individual MF or BP assertion because direct genetics does not establish one.
- LepB retains exact signal peptidase activity, and broad `GO:0051604` protein
  maturation is refined to live `GO:0016485` protein processing. The authoritative
  QuickGO API returned `isObsolete: true` for `GO:0006465` on 2026-08-08 and
  recommends MF `GO:0009003`; the stale UniProt InterPro process cross-reference
  is therefore not propagated.

## Boundary Decisions

- Ffh, FtsY, and the single 4.5S SRP RNA locus belong to a cotranslational
  targeting module.
- The two experimentally functional TatABC clusters belong to a folded-protein
  translocation module.
- YidC belongs to a membrane-protein insertion module because it can act with
  SecYEG or independently.
- LspA remains in `bacterial_lipoprotein_maturation.yaml`; LepB handles
  non-lipoprotein type I signal peptides here.
- Xcp type II secretion begins after periplasmic delivery and remains in
  ppu03070.
- Molecular functions occur only on leaf annotons. The module has no redundant
  module-level localization.
- SecDF-YajC is an optional enhancer connected to SecYEG by positive regulation;
  SecYEG connects directly to LepB, so the graph does not require SecDF for every substrate.

## Grounding

Every leaf has an exact KT2440 UniProt implementation and a reviewed E. coli
exemplar. PTN000770133 grounds the bacterial SecA transport role,
PTN000097217 grounds SecY transporter activity, and PTN000763987 grounds the
conserved SecD/SecF protein-transport role. Exact PANTHER subfamilies are used
where their labels are reliable; LepB uses the correctly named parent PANTHER
family rather than its misleading chloroplast-centered subfamily label.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Local UniProt, GOA, PANTHER, PAINT, and
InterPro records, primary Sec literature, and provenance-bearing notes for all
nine reviewed genes were used to resolve exact identifiers and subunit-level
annotation actions.

## Validation

The eight new reviews, revised SecA review, reusable module, and project page
are validated and rendered before publication.
