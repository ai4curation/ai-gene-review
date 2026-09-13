---
title: "PSEPK ppu00541 ADP-heptose biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00541: ADP-heptose biosynthesis

- Reusable module: `modules/adp_heptose_biosynthesis.yaml`
- Canonical pathway boundary: KEGG M00064
- Broad ppu00541 candidates inspected: 26
- Selected PSEPK proteins: 3
- Covered reactions: 4
- Unresolved terminal stereochemical step: 1
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate ADP-heptose synthesis from CMP-KDO and other ppu00541 routes.
- [x] Fetch and curate the previously unreviewed `gmhA` and `hldE` records.
- [x] Reuse the existing curated `gmhB` review.
- [x] Represent the two HldE activities as separate pathway steps.
- [x] Model HldD-dependent C-6 epimerization as lineage-dependent maturation.
- [x] Integrate the OpenScientist report with local UniProt, GOA, PANTHER, and Rhea data.
- [x] Validate and render the module, genes, and project page.
- [x] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Reaction | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Sedoheptulose-7-phosphate to phosphoheptose anomers | `gmhA` / PP_1323 | Q88N89 | Covered by EC 5.3.1.28, Rhea 27489, and the GmhA InterPro/HAMAP assignment |
| 2 | Heptose-7-phosphate to heptose-1,7-bisphosphate | `hldE` / PP_4934, N-terminal domain | Q88D93 | Covered by reviewed EC 2.7.1.167, Rhea 27473, UniRule, and PTN005327360 |
| 3 | Heptose-1,7-bisphosphate to heptose-1-phosphate | `gmhB` / PP_0059 | Q88RS0 | Covered by reviewed and experimental GO evidence for EC 3.1.3.82 |
| 4 | Heptose-1-phosphate to ADP-D,D-heptose | `hldE` / PP_4934, C-terminal domain | Q88D93 | Covered by reviewed EC 2.7.7.70, Rhea 27465, UniRule, and PTN005327360 |
| 5 | ADP-D,D-heptose to ADP-L,D-heptose | no resolved HldD ortholog | none | Gap for the canonical L,D endpoint; may be unnecessary if KT2440 directly uses D,D-heptose |

The four reactions through ADP-D-glycero-beta-D-manno-heptose are satisfiable.
No KT2440 HldD/GmhD ortholog was resolved. This does not make the upstream
pathway incomplete: it leaves the concrete activated-heptose stereochemistry
unresolved. The reusable module therefore separates obligatory ADP-D,D-heptose
production from optional HldD-dependent maturation.

The inherited `gmhB` review is reconciled with this endpoint decision:
GO:0097171 is now `UNDECIDED` there as well and is no longer a core process.
GO:0009244 remains the endpoint-neutral LPS-core process anchor. Because GO
lacks a D,D-heptose biosynthetic-process term, `hldE` records an ontology
proposal beneath GO:0009226 rather than borrowing the L,D term.

## Annotation Decisions

- Exact GmhA, HldE kinase, GmhB phosphatase, and HldE adenylyltransferase
  molecular functions are accepted at gene and leaf-annoton level.
- Broad carbohydrate, catalytic, kinase, phosphotransferase,
  nucleotidyltransferase, and substrate-binding terms are marked
  over-annotated or retained as non-core.
- The PANTHER `PTHR30390:SF6` label calls PP_1323 a DiaA protein even though
  its UniProt/HAMAP, InterPro, EC, Rhea, pathway, and product assignments are
  GmhA-specific. The module therefore uses the GmhA-specific InterPro family
  rather than that misleading PANTHER subfamily label.
- The `hldE` GO:0097171 process row is left `UNDECIDED`: its L,D endpoint
  assumes terminal epimerization that has not been resolved in KT2440, while
  the two HldE molecular functions remain secure.
- The inherited `gmhB` GO:0097171 row is likewise `UNDECIDED` and removed from
  the core function, eliminating a contradictory endpoint assertion within the
  same pathway batch.

## Boundary Decisions

- GmhA, HldE kinase, GmhB, and HldE adenylyltransferase form the conserved
  precursor chain.
- HldD is a separate optional terminal maturation part, represented with the
  reviewed Pseudomonas aeruginosa Q9HYQ8 exemplar and exact Rhea 17577
  chemistry; no target gene is invented.
- WaaC/WaaF and other heptosyltransferases consume activated heptose and are
  downstream of this biosynthetic module.
- CMP-KDO, dTDP-rhamnose, GDP-mannose/fucose, and UDP-sugar genes in the broad
  ppu00541 map are separate modules.

## Grounding

All four covered reactions have exact KT2440 UniProt exemplars. The two HldE
leaf activities carry the current GOA PTN005327360 evidence, and reviewed
Escherichia coli or Pseudomonas exemplars orient every family. Exact Rhea
reactions define metabolite chaining. No molecular function or redundant
cytoplasm/cytosol term is placed at module level.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Its pathway-boundary and candidate-retrieval
results were checked against local UniProt and GOA records. The report's
negative HldD search is recorded as a realization-level gap, not promoted to a
claim that a specific substitute gene exists.

## Validation

Both newly curated gene reviews passed schema, reference, GOA, and ontology-term
validation with no warnings. The module passed LinkML and semantic validation;
the only semantic warning is the expected unconfigured `InterPro` prefix for a
family label. Gene, module, and project renderers completed successfully.
