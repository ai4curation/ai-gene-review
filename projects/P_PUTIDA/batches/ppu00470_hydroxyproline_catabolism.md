---
title: "PSEPK ppu00470 hydroxyproline catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00470: hydroxyproline catabolism

- Reusable module: `modules/hydroxyproline_catabolism.yaml`
- KEGG ppu00470 candidates inspected: 21
- Selected pathway proteins: 4
- Ordered reactions: 4
- Direct KT2440 enzymology: `proR`
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a multi-step, species-neutral bacterial module boundary.
- [x] Separate hydroxyproline catabolism from D-amino-acid KEGG-map spillover.
- [x] Fetch the four selected PSEPK genes.
- [x] Review every GOA annotation for the selected genes.
- [ ] Integrate the module/pathway/taxon OpenScientist report.
- [x] Validate module and gene reviews.
- [x] Render module, gene, and project pages.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK gene | UniProt | Decision |
|---|---|---|---|---|
| 1 | trans-L/cis-D 4-hydroxyproline epimerization | `proR` | Q88NF3 | Covered by direct KT2440 biochemical evidence |
| 2 | cis-4-hydroxy-D-proline oxidation | `PP_1255` | Q88NF6 | Covered by locus and FAD-dependent DAO-like fold; electron acceptor unresolved |
| 3 | Cyclic-imine deamination to 2,5-dioxopentanoate | `PP_1257` | Q88NF4 | Covered by EC 3.5.4.22 and Rhea 10560 |
| 4 | 2,5-dioxopentanoate oxidation to 2-oxoglutarate | `PP_1256` | Q88NF5 | Covered by EC 1.2.1.26 and the pathway locus |

The four-reaction route is satisfiable in KT2440. `proR` is experimentally
characterized; the other three assignments remain predictions supported by
reaction mapping, fold, and the compact PP_1255-PP_1258 locus.

## Annotation Decisions

- The `PP_1257` TreeGrafter annotation to
  4-hydroxy-tetrahydrodipicolinate synthase is removed. It is a paralog transfer
  across the DapA-like fold; EC 3.5.4.22 and pathway continuity support the
  hydroxyproline deaminase.
- The exact `PP_1257` deaminase and `PP_1256` 2,5-dioxovalerate-dehydrogenase
  annotations are accepted.
- Broad lyase and oxidoreductase terms are marked as over-annotations when an
  exact substrate-specific molecular function exists.
- GO has no exact cis-4-hydroxy-D-proline-oxidase term. `PP_1255` retains an
  exact prose function with GO:0016491 used only as a broad ontology handle;
  no identifier is invented.
- The `PP_1255` cytoplasm row is kept as non-core and is not duplicated at the
  module level.

## Excluded KEGG Candidates

The remaining ppu00470 entries are D-amino-acid-map neighbors rather than
members of this route: peptidoglycan enzymes (`murI`, `murD`, `ddlA`, `ddlB`,
`dapF` paralogs, `lysA` paralogs), broad amino-acid racemases/dehydrogenases
(`alr`, `dadX`, `dadA1`, `dadA2`, `dauA`, `PP_4311`), `ansB`, and two
2,5-dioxovalerate-dehydrogenase paralogs outside the hydroxyproline locus
(`PP_2585`, `PP_3602`).

## Module Decisions

- The reusable module exposes four ordered leaf reactions rather than a
  one-step ProR wrapper.
- Every leaf has an exact PSEPK UniProt exemplar; the experimentally reviewed
  Pseudomonas aeruginosa epimerase and a reviewed KgsD-family protein provide
  additional orientation where appropriate.
- Transport and downstream 2-oxoglutarate use are outside the boundary.
- Molecular functions remain on leaf annotons, with no generic MF or redundant
  cytoplasm/cytosol pair at module level.

## Research Status

The long-running OpenScientist module/pathway/taxon retrieval is in progress.
The provider report will be integrated without overriding exact reaction and
target-specific evidence.

## Validation

All four selected gene reviews pass `just validate`. The module passes LinkML
`ModuleReview` validation and the dedicated semantic module validator; the only
messages are expected namespace-label warnings for InterPro and Pfam family
selectors. The module, genes, and project page render successfully, and `git
diff --check` is clean.
