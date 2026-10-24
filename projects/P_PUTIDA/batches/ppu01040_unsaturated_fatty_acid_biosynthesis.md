---
title: "PSEPK ppu01040 unsaturated-fatty-acid biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [fabA, fabB, fabF]
autolink_gene_symbols: false
---

# PSEPK ppu01040: unsaturated-fatty-acid biosynthesis

- Reusable module: `modules/bacterial_unsaturated_fatty_acid_biosynthesis.yaml`
- KEGG ppu01040 candidates inspected: 3
- Defining PSEPK branch proteins selected: 3
- Required branch proteins: 2
- Optional long-chain extension protein: 1
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Test whether the KEGG `tesA`, `tesB`, and `PP_5331` set forms a pathway.
- [x] Resolve the ACP-bound route that introduces cis unsaturation in KT2440.
- [x] Reuse and audit the curated `fabA`, `fabB`, and `fabF` reviews.
- [x] Represent distinct FabA dehydration and isomerization reactions as separate parts.
- [x] Keep molecular functions on leaf annotons and use exact UniProt exemplars.
- [x] Narrow FabA, FabB, and FabF to their verified PANTHER subfamilies and add reviewed E. coli exemplars.
- [x] Complete an independent annotation-reviewer audit and incorporate all actionable findings.
- [x] Complete OpenScientist module/pathway/taxon and focused-gene research.
- [x] Validate and render the module, genes, and project page.
- [ ] Shepherd review and CI.

## Biological Conclusion

KEGG ppu01040 does not define a satisfiable three-enzyme biosynthetic pathway
in KT2440. Its three mapped proteins are hydrolases: TesA has multifunctional
thioesterase, lysophospholipase, and protease assignments, whereas TesB and
PP_5331 hydrolyze acyl-CoA thioesters. None has a supported ACP-dependent
reaction that introduces or elongates cis unsaturation. They are retained as
adjacent release or turnover candidates, not forced into the module.

The defensible route is the canonical oxygen-independent type-II fatty-acid
synthesis branch. FabA first dehydrates 3-hydroxydecanoyl-ACP and then
isomerizes trans-2-decenoyl-ACP to cis-3-decenoyl-ACP. FabB condenses that
committed intermediate with malonyl-ACP and preserves the cis double bond
through elongation. FabF is an optional downstream KAS-II step that extends
palmitoleoyl-ACP into the cis-vaccenoyl branch. Calling this the "anaerobic"
route describes its lack of an oxygen-requiring desaturase, not an obligate
anaerobic growth condition.

## Satisfiability

| Order | Reaction | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | 3-hydroxydecanoyl-ACP to trans-2-decenoyl-ACP | `fabA` / PP_4174 | Q88FC4 | Covered by reviewed EC 4.2.1.59 and Rhea 41860 |
| 2 | trans-2-decenoyl-ACP to cis-3-decenoyl-ACP | `fabA` / PP_4174 | Q88FC4 | Covered by reviewed EC 5.3.3.14 and Rhea 23568 |
| 3 | cis-3-decenoyl-ACP committed elongation | `fabB` / PP_4175 | Q88FC3 | Covered by EC 2.3.1.41 and Rhea 54940 |
| 4 | palmitoleoyl-ACP extension toward cis-vaccenoyl-ACP | `fabF` / PP_1916 | Q88LL4 | Optional product-distribution step covered by EC 2.3.1.179 and Rhea 55040 |

The defining two-protein FabA/FabB branch is satisfiable. Generic FabG,
FabA/FabZ, and FabV reactions complete intervening elongation cycles but are
shared with saturated-fatty-acid synthesis, so duplicating them here would
blur this focused module's boundary.

## Annotation Review

The focused `fabA`, `fabB`, and `fabF` gene reviews were assessed under the
annotation-reviewer criteria. All GOA rows already have explicit decisions and
no `PENDING` annotations remain. FabA retains both exact molecular functions
as separate core activities. FabB and FabF retain the specific
3-oxoacyl-ACP-synthase term while generic acyltransferase parents and redundant
cytosol/cytoplasm calls are not promoted into the module.

## Boundary Decisions

- FabA and FabB are the required branch-specific proteins.
- FabF controls downstream C16:1-to-C18:1 extension and is optional at module level.
- FabZ and the reductive FAS-II reactions are shared pathway context.
- TesA, TesB, and PP_5331 are excluded hydrolase/release candidates.
- Oxygen-dependent acyl desaturases are alternative routes in other lineages,
  not inferred for KT2440 without an exact supported target.
- Phospholipid acyltransferases consume the resulting acyl chains downstream.

## Grounding

Every leaf activity has an exact KT2440 UniProt exemplar. FabA is grounded by
reviewed UniProt/HAMAP assignments for both exact reactions. FabB and FabF are
grounded by ARBA/PIRNR rule-derived exact Rhea reactions in their local UniProt
records; their current GOA rows also carry PAINT nodes PTN002270989 and
PTN004296092 respectively.
FabA is grounded on `PTHR30272:SF8` with reviewed E. coli P0A6Q3 and the
dehydratase-specific PAINT node PTN008624492. FabB is grounded on
`PTHR11712:SF306` with reviewed E. coli P0A953, while FabF is grounded on
`PTHR11712:SF336` with reviewed E. coli P0AAI5. The official SF336 label
contains "mitochondrial" despite including bacterial FabF proteins; it is
retained verbatim as required and is not interpreted as localization evidence.
The target TreeGrafter PTNs are not promoted to ancestral-node claims because
they are absent from the local PAINT IBD export. No molecular function or
redundant cytoplasm/cytosol term is placed at module level, and electronic
cellular locations are retained only as non-core gene annotations.

## Research Status

OpenScientist module and module/pathway/taxon retrieval completed. Both reports
independently recover the FabA/FabB branch, conditional FabF extension, and the
mis-scoped `ppu01040` thioesterase set. Their stronger paralog and literature
claims were not imported automatically; the curated boundary remains grounded
in the checked local UniProt, GOA, UniPathway, PANTHER, publication, and
project-partition records.

## Validation

The focused gene reviews contain no pending annotations. The module passes
LinkML and semantic validation, and the module, gene, and project renderers
complete successfully.
