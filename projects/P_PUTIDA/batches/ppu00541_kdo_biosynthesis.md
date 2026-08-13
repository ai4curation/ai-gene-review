---
title: "PSEPK ppu00541 CMP-KDO biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00541: CMP-KDO biosynthesis

- Reusable module: `modules/kdo_biosynthesis.yaml`
- Correct pathway boundary: KEGG M00063
- Broad ppu00541 candidates inspected: 26
- Selected PSEPK proteins: 6
- Biochemical reactions: 4
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Replace the ppu00541 overview boundary with CMP-KDO module M00063.
- [x] Separate ADP-heptose and unrelated nucleotide-sugar modules.
- [x] Fetch and review all six selected PSEPK proteins.
- [x] Represent API and KdsA paralogs as alternatives rather than serial parts.
- [x] Integrate the OpenScientist report with local UniProt, GOA, and Rhea data.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Reaction | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Ribulose-5-phosphate to arabinose-5-phosphate | `kdsD`; alternative `PP_1806` | Q88P95; Q88LX1 | Covered by two API-family candidates; paralog contribution unresolved |
| 2 | Arabinose-5-phosphate to KDO-8-phosphate | `kdsA1`; alternative `kdsA2` | Q88MG0; Q88LX0 | Covered by two exact EC 2.5.1.55 assignments |
| 3 | KDO-8-phosphate to KDO | `kdsC` | Q88P96 | Covered by KdsC family, EC 3.1.3.45, and Rhea 11500 |
| 4 | KDO to CMP-KDO | `kdsB` | Q88LM7 | Covered by reviewed HAMAP assignment, EC 2.7.7.38, and Rhea 23448 |

All four reactions are satisfiable. No direct KT2440 enzyme assay was found, so
the gene-level evidence remains homology/rule based. Consecutive PP_1806 and
PP_1807 locus tags support a second API/KdsA pair, but specialization relative
to the housekeeping copies remains an explicit question.

## Annotation Decisions

- The `kdsC` TreeGrafter N-acylneuraminate cytidylyltransferase annotation is
  removed as a paralog transfer within the mixed CMAS/KdsC PANTHER family.
- Exact API, KDO-8-phosphate synthase, KDO-8-phosphate phosphatase, and CMP-KDO
  synthetase molecular functions are accepted.
- Broad carbohydrate, carboxylic-acid, isomerase, hydrolase, and binding terms
  are marked over-annotated or retained as non-core.
- The compatible `kdsB` cytoplasm and cytosol rows are retained as non-core
  evidence and omitted from the core function rather than duplicated there.
- `kdsD` receives the missing lipopolysaccharide-biosynthesis process row from
  its explicit UniProt pathway assignment. `PP_1806` retains only the API
  molecular function because its KDO-pathway contribution is unresolved.

## Boundary Decisions

- `gmhA`, `gmhB`, and `hldE` belong to the separate ADP-heptose module M00064.
- WaaA consumes CMP-KDO in LPS core assembly and lies downstream of this module.
- dTDP-rhamnose, GDP-mannose/fucose, UDP-GlcNAc, and UDP-glucose genes share
  the broad ppu00541 overview but are not CMP-KDO biosynthesis parts.

## Grounding

Every alternative or required reaction has a KT2440 UniProt exemplar. Reviewed
E. coli KdsD, GutQ, and KdsA exemplars orient the paralog families. Exact Rhea
reactions define chaining; no molecular function is placed at module level.
Both KT2440 API candidates map to `PTHR42745:SF1`; the SF2 selector therefore
cannot be used to distinguish PP_1806 without contradicting its UniProt record.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Database-derived pathway structure was
checked locally. Report-only sequence-identity estimates were not used as
primary evidence in annotation decisions. Comparative primary literature now
grounds the E. coli second-API/redundancy paradigm (PMID:16199563 and
PMID:16765569), while Bacteroides API feedback inhibition (PMID:24891442) is
retained only as non-target pathway context.

## Validation

All six gene reviews passed schema, reference, GOA, and ontology-term
validation. The module passed LinkML and semantic module validation; the only
semantic warning is the expected unconfigured `InterPro` prefix for family
labels. Gene, module, and project renderers completed successfully.
