---
title: "PSEPK ppu00627 hydroxycinnamate and vanillate catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00627: hydroxycinnamate and vanillate catabolism

- Reusable module: `modules/hydroxycinnamate_vanillate_catabolism.yaml`
- Correct boundary: serial ferulate-to-protocatechuate peripheral pathway
- Broad ppu00627 candidates inspected: 12
- Selected PSEPK proteins: 5
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate the coherent Fcs-Ech-Vdh-VanAB route from the aminobenzoate overview map.
- [x] Keep gallate cleavage and the protocatechuate beta-ketoadipate pathway as separate modules.
- [x] Reuse curated `fcs`, `vanA`, and `vanB` reviews; fetch and curate `ech` and `vdh`.
- [x] Replace the wrong Ech isoprenoid-process propagation with ferulate catabolism.
- [x] Integrate the OpenScientist report with UniProt, GOA, PANTHER, GO, and Rhea data.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Ferulate activation | `fcs` / PP_3356 | Q88HK0 | Covered by GO:0050563 and Rhea 36251 |
| 2 | Feruloyl-CoA hydration and cleavage | `ech` / PP_3358 | Q88HJ8 | Covered by GO:0050547, Rhea 62412, CoA-bound structures, and direct genetics |
| 3 | Vanillin oxidation | `vdh` / PP_3357 | Q88HJ9 | Covered by GO:0050608, Rhea 13309, and direct genetics |
| 4 | Vanillate O-demethylation | `vanA` / PP_3736 plus `vanB` / PP_3737 | Q88GI6; Q88GI5 | Covered by the two-component oxygenase/reductase implementation and Rhea 13021 |

The four-part pathway is satisfiable and has direct KT2440 evidence for every
reaction. Protocatechuate is the module exit and feeds a separate
beta-ketoadipate pathway.

## Annotation Decisions

- The precise Fcs activity and ferulate-catabolic process are retained.
- Ech's `GO:0008300 isoprenoid catabolic process` is a wrong-subfamily
  TreeGrafter propagation and is replaced by `GO:1901067 ferulate catabolic
  process`; exact `GO:0050547` is added.
- Vdh's exact `GO:0050608` activity is accepted, while two generic oxidoreductase
  parents are marked over-annotated; ferulate catabolism is added.
- VanA retains the complex's substrate-specific monooxygenase activity. VanB
  retains electron-transfer activity and contributes to the VanAB complex-level
  function rather than independently enabling it.

## Boundary Decisions

- GalA-dependent gallate ring cleavage is a parallel pathway and is not a fifth
  serial part of this module.
- Protocatechuate ring cleavage belongs to the downstream beta-ketoadipate module.
- Aromatic-acid uptake and formaldehyde detoxification are separate dependencies.
- UbiX, PP_2805, PP_2932, NfnB, PP_2217, and PaaF are broad-map inclusions and
  do not satisfy this route.

## Grounding

Every step has exact GO and Rhea chemistry plus an exact UniProt ortholog
selector. Ortholog selectors are used deliberately because available PANTHER
subfamily labels mix distinct substrate specificities. Molecular functions
occur only on leaf annotons, with no module-level function or generic
cytoplasm/cytosol assertion.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. It recovered target-strain loss-of-function,
reconstitution, structural, and biochemical evidence for the complete route.

## Validation

All five gene reviews passed schema, reference, GOA, best-practice, and
ontology-term validation without warnings. The module passed LinkML and
semantic validation with no warnings. Gene, module, and project renderers
completed successfully.
