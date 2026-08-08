---
title: "PSEPK ppu00620 methylglyoxal detoxification batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00620: methylglyoxal detoxification

- Reusable module: `modules/methylglyoxal_detoxification.yaml`
- Correct boundary: two-step glutathione-dependent conversion of methylglyoxal to D-lactate
- Broad ppu00620 candidates inspected: 54
- Selected PSEPK proteins: 2
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate methylglyoxal detoxification from the broad pyruvate-metabolism map.
- [x] Identify the canonical GloA-GloB route and verify endogenous glutathione supply.
- [x] Treat methylglyoxal synthase absence as not expected rather than a pathway hole.
- [x] Keep reductive and DJ-1-family candidate routes outside the canonical module.
- [x] Fetch and curate `gloA` and `gloB`.
- [x] Integrate the OpenScientist report with local UniProt, GOA, PANTHER, InterPro, and Rhea data.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | S-lactoylglutathione formation | `gloA` / PP_3766 | Q88GF8 | Covered by GO:0004462, Rhea 19069, and PTHR10374:SF30 |
| 2 | S-lactoylglutathione hydrolysis | `gloB` / PP_4144 | Q88FF3 | Covered by reviewed HAMAP, GO:0004416, Rhea 21864, and PTHR43705:SF1 |

The two-reaction module is satisfiable. KT2440 also encodes GshA and GshB for
glutathione supply and several lactate dehydrogenases for downstream D-lactate
disposal; these are cross-module dependencies rather than additional parts.

## Annotation Decisions

- The exact existing catalytic molecular functions for GloA and GloB are accepted.
- Generic metal-ion binding on GloA is retained as non-core because metal
  dependence is real but the physiological Ni2+-versus-Zn2+ preference is unresolved.
- Valid `GO:0051596 methylglyoxal catabolic process` is added to GloA and
  accepted on GloB; obsolete route-specific GO:0019243 is not authored.
- PP_0772 remains a candidate glyoxalase-II-family paralog rather than an
  alternate implementation because its physiological substrate is untested.

## Boundary Decisions

- GshA/GshB glutathione synthesis supplies the required cofactor but belongs to
  glutathione metabolism.
- D-lactate oxidation to pyruvate belongs to central carbon metabolism.
- No MgsA methylglyoxal synthase was identified in KT2440; methylglyoxal
  generation is not required to satisfy a defensive detoxification module.
- `yeaE`, `dkgB`, and DJ-1/ThiJ-family proteins are possible parallel routes and
  require separate biochemical resolution.
- `ycgM`/PP_5153 is a fumarylacetoacetase-family enzyme and is excluded.

## Grounding

Both steps use exact PANTHER subfamilies, exact target UniProt entries, reviewed
Pseudomonas exemplars, GO molecular functions, and Rhea reactions. Molecular
functions occur only on leaf annotons, and the module contains no generic
cytoplasm/cytosol assertion.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Direct work on a *P. putida* glyoxalase I
supports the first reaction, while the KT2440 GloB assignment has reviewed
HAMAP support.

## Validation

Both gene reviews passed schema, reference, GOA, best-practice, and
ontology-term validation without warnings. The module passed LinkML and
semantic validation with no warnings. Gene, module, and project renderers
completed successfully.
