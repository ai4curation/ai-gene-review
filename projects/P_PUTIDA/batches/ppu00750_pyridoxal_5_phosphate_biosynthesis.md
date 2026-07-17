---
title: "PSEPK ppu00750 de novo PLP biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00750: DXP-dependent de novo PLP biosynthesis

- Reusable module: `modules/pyridoxal_5_phosphate_biosynthesis.yaml`
- KEGG ppu00750 candidates inspected: 9
- De novo pathway core: 6 proteins covering 6 ordered reactions
- Pathway-map context excluded from this module: 3 proteins
- Gene-level provider: OpenScientist
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a multi-step, species-neutral module boundary.
- [x] Separate de novo synthesis from salvage and PLP-enzyme map spillover.
- [x] Fetch the six selected PSEPK genes.
- [x] Review every GOA annotation for the selected genes.
- [ ] Complete OpenScientist module and gene reports.
- [x] Validate the initial module and gene-review curation.
- [ ] Render module, gene, and project pages.
- [ ] Open one draft PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK gene | UniProt | Decision |
|---|---|---|---|---|
| 1 | Erythrose 4-phosphate dehydrogenase | `epd` | Q88D63 | Covered; NCBIfam-supported first branch reaction |
| 2 | 4-phosphoerythronate dehydrogenase | `pdxB` | Q88L20 | Covered |
| 3 | Phosphohydroxythreonine aminotransferase | `serC` | Q88M07 | Covered by the same SerC enzyme used in serine biosynthesis |
| 4 | 4-hydroxythreonine-4-phosphate dehydrogenase | `pdxA` | Q88QT5 | Covered |
| 5 | Pyridoxine 5'-phosphate synthase | `pdxJ` | Q88MY2 | Covered; consumes the shared DXP input |
| 6 | Pyridoxine/pyridoxamine 5'-phosphate oxidase | `pdxH` | Q88NS5 | Covered; terminal PLP formation and a shared salvage activity |

The DXP-dependent de novo pathway is satisfiable in KT2440. DXP production by
Dxs is shared with thiamine and isoprenoid metabolism and is modeled as an
upstream input, not as an extra vitamin-B6-specific module part.

## Excluded Candidates

| Gene | Reason outside the module boundary |
|---|---|
| `pdxY` | Pyridoxal kinase of vitamin-B6 salvage, not de novo ring synthesis |
| `thrC` | Threonine synthase and PLP user; no reaction in de novo PLP formation |
| `PP_0662` | Unreviewed threonine-synthase-family paralog without a de novo PLP-pathway reaction |

## Annotation Decisions

- Exact reaction terms were retained as core molecular functions for Epd,
  PdxB, PdxA, PdxJ, and PdxH.
- SerC retains both its serine-biosynthesis and vitamin-B6-biosynthesis roles;
  its dual use is real shared metabolism rather than pathway overreach.
- Generic oxidoreductase, nitrogenous-group transferase, metal-binding, and
  dimerization terms were marked non-core or over-annotated when a specific
  reaction term was already present.
- Duplicate cytoplasm/cytosol pairs on PdxB and PdxJ were reduced to the useful
  bacterial cytoplasm context in the review decisions.

## Module Decisions

- The reusable module contains six ordered reaction parts and is not a wrapper
  around a single protein.
- Molecular functions are attached only to leaf annotons.
- Every leaf has a concrete PSEPK UniProt exemplar; no PTN was asserted without
  exact PAINT ancestry.
- No module-level cytoplasm/cytosol context is used.
- The boundary is explicitly DXP-dependent. The unrelated PdxS/PdxT route and
  vitamin-B6 salvage belong in separate reusable modules.

## Research Status

The module/pathway/taxon OpenScientist report confirms that all six de novo
steps are present, that `dxs` supplies a shared external DXP input, and that
`pdxY`, `thrC`, and `PP_0662` do not add de novo module reactions. It also
identified direct species-level isotope-labeling evidence: glutamate nitrogen
is incorporated into pyridoxine in *P. putida* (PMID:10885790), supporting the
DXP-dependent route. This is organism-level pathway evidence, not a direct
KT2440 assay of any individual enzyme.

## Validation

Initial LinkML, module-validator, and per-gene validation passed. Final
validation and rendering will be repeated after provider-report integration.
