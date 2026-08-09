---
title: "PSEPK ppu00543 alginate polymerization and export batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00543: alginate polymerization and export

- Reusable module: `modules/alginate_polymerization_export.yaml`
- Correct boundary: synthase-dependent alginate polymerization, periplasmic handling, and outer-membrane export
- Broad ppu00543 candidates inspected: 11
- Selected PSEPK proteins: 6
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate alginate from the broad exopolysaccharide overview map.
- [x] Add `algL`, `algG`, `algE`, and `algK`, which ppu00543 omitted.
- [x] Exclude four CysE-like serine acetyltransferases and the separate PslH-family glycosyltransferase.
- [x] Fetch and curate `alg8`, `alg44`, and `algL`; reuse existing `algG`, `algE`, and `algK` reviews.
- [x] Keep precursor synthesis and O-acetylation as separate module boundaries.
- [x] Integrate the OpenScientist report with local UniProt, GOA, PANTHER, InterPro, and Rhea data.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Alginate polymerization | `alg8` / PP_1287 plus `alg44` / PP_1286 | Q88NC5; Q88NC6 | Covered by the catalytic GT2 mannuronan synthase and c-di-GMP-responsive copolymerase |
| 2 | Mannuronate C5 epimerization | `algG` / PP_1283 | Q88NC9 | Covered by EC 5.1.3.37, Rhea 45572, and the exact AlgG family |
| 3 | Periplasmic polymer guidance | `algK` / PP_1285 | Q88NC7 | Covered by the AlgK-specific TPR scaffold family and direct P. putida AlgK-AlgX structural evidence in the existing review |
| 4 | Escaped-polymer quality control | `algL` / PP_1281 | Q88ND1 | Covered by reviewed HAMAP EC 4.2.2.3 and GO:0045135 |
| 5 | Outer-membrane export | `algE` / PP_1284 | Q88NC8 | Covered by the AlgE-specific channel family and outer-membrane assignment |

The polymerization/export module is satisfiable. AlgG product-composition
editing and AlgL quality control are represented as optional parts rather than
forced serial reactions. O-acetylation is handled in its own module because it
has a distinct multi-protein acyl-transfer pathway and is not required to
define the Alg8-to-AlgE polymer conduit.

## Annotation Decisions

- The `alg8` TreeGrafter node `PTN002740694` propagates hyaluronan synthase,
  hyaluronan biosynthesis, and extracellular-matrix assembly to a
  target labeled as a PANTHER `PTHR22913:SF12` mannuronan synthase. The
  hyaluronan rows are removed; extracellular-matrix assembly is retained only
  as an over-annotated, condition-dependent consequence of alginate production.
- `GO:0047643 alginate synthase activity` is added to Alg8 as the exact
  replacement molecular function.
- Alg44 retains cyclic-di-GMP binding and is annotated as contributing to,
  rather than independently enabling, alginate synthase activity.
- AlgL retains the exact poly-beta-D-mannuronate lyase activity, while the
  generic alginic-acid catabolic process is modified to the biosynthetic
  quality-control context.
- The PANTHER SF19 efflux-protein label for Alg44 is not used as family
  grounding; Alg44-specific InterPro domains and reviewed Pseudomonas exemplars
  provide the selector instead.

## Boundary Decisions

- AlgA, AlgC-type phosphomannomutases, and AlgD supply GDP-mannuronate and
  belong to a precursor-synthesis module.
- AlgI, AlgJ, AlgF, and the O-acetyltransferase function of AlgX belong to the
  separate alginate O-acetylation module.
- PP_0228, `cysE`/PP_0840, PP_1110, and PP_3136 are cysteine-biosynthesis
  serine acetyltransferases, not alginate proteins.
- PP_2124 is a PslH-family glycosyltransferase in another exopolysaccharide
  system.

## Grounding

Every modeled role has an exact KT2440 UniProt exemplar and a reviewed
Pseudomonas aeruginosa comparator. The Alg8 ortholog selector is anchored to
reviewed KT2440 Q88NC5, with Q52463 retained as the characterized comparator,
because the nominal PANTHER SF12 mixes Alg8, HasA, and NodC. Other family
selections use specific InterPro accessions, with misleading broad-family labels
explicitly excluded.
Molecular functions occur only on leaf annotons. No generic cytoplasm/cytosol
term is asserted at module level.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Primary studies PMID:25968647,
PMID:25817996, and PMID:23503314 ground the Alg8-Alg44 interaction, cytoplasmic
c-di-GMP sensing, and envelope-spanning complex, respectively. Direct P. putida
phenotypic evidence supports an intact, conditionally deployed alginate system,
while mechanistic assignments remain explicit ortholog transfers where
KT2440-specific biochemistry is unavailable.

## Validation

The three newly curated gene reviews passed schema, reference, GOA, and
ontology-term validation with no warnings. The module passed LinkML and
semantic validation; the only semantic warning is the expected unconfigured
`InterPro` prefix for family labels. Gene, module, and project renderers
completed successfully.
