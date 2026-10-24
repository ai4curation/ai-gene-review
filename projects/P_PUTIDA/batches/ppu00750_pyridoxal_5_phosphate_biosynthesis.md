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

- [x] Re-audit the reusable module boundary against the module-curation standard.
- [x] Preserve the six DXP-dependent de novo reactions and keep DXP supply,
  salvage, and the PdxS/PdxT route outside the module.
- [x] Replace the exemplar-only PSEPK framing with reviewed cross-species
  UniProt exemplars plus the concrete PSEPK pathway-instance members.
- [x] Verify family labels, representative containment, and exact PAINT IBD
  activity nodes; omit uncertain family or ancestry assertions.
- [x] Re-audit all six PSEPK gene reviews conservatively.
- [x] Complete generic module OpenScientist retrieval; the module report
  completed after 2835.67 seconds and the missing PdxJ report after 1810.63
  seconds, both with the full allowance.
- [x] Record the required annotation-reviewer consultation and address its
  blocking biological/evidence findings.
- [x] Validate and render the repaired module, batch, and all six reviews.
- [ ] Open the wave111 repair PR and shepherd it through review.

### Initial Pass

- [x] Define a multi-step, species-neutral module boundary.
- [x] Separate de novo synthesis from salvage and PLP-enzyme map spillover.
- [x] Fetch the six selected PSEPK genes.
- [x] Review every GOA annotation for the selected genes.
- [x] Run OpenScientist module and gene research; record provider timeouts.
- [x] Validate the initial module and gene-review curation.
- [x] Render module, gene, and project pages.
- [x] Open one draft PR for this module/pathway: [#2174](https://github.com/ai4curation/ai-gene-review/pull/2174).
- [x] Merge the initial module/pathway PR: [#2174](https://github.com/ai4curation/ai-gene-review/pull/2174).

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
  GO:0004648 represents only the phosphoserine reaction, so the distinct PdxF
  reaction is recorded as an explicit molecular-function ontology gap rather
  than being assigned the wrong GO term.
- GO:0008615 is retained by convention for the five upstream enzymes that make
  pyridoxine 5'-phosphate (PNP), although the GO label names pyridoxine. It is
  removed from PdxH because PdxH acts downstream by consuming PNP/PMP to form
  PLP; the existing GO:0042823 PLP-biosynthesis annotation captures that role.
- Specific de novo PLP and PLP-salvage process annotations are proposed for
  PdxH, while the broad vitamin-B6 metabolic-process annotation is non-core.
- Generic oxidoreductase, nitrogenous-group transferase, metal-binding, and
  dimerization terms were marked non-core or over-annotated when a specific
  reaction term was already present.
- Duplicate cytoplasm/cytosol pairs on PdxB and PdxJ were reduced to the useful
  bacterial cytoplasm context in the review decisions.

## Module Decisions

- The reusable module contains six ordered reaction parts and is not a wrapper
  around a single protein.
- Molecular functions are attached only to leaf annotons.
- The SerC/PdxF leaf is intentionally ungrounded at GO MF level pending a term
  for RHEA:16573; GO:0004648 is not reused for that distinct reaction.
- Every leaf has a reviewed E. coli K-12 UniProt exemplar and the concrete
  PSEPK pathway-instance member.
- Exact PANTHER subfamily labels and PSEPK member containment were retained for
  SerC, PdxA, PdxJ, and PdxH. Epd retains its exact NCBIfam equivalog and PdxB
  its exact InterPro family; no unrelated PANTHER label was substituted merely
  to obtain a PTHR identifier.
- Exact local PAINT IBD activity nodes are asserted for PdxA, PdxJ, and PdxH.
  Epd has no exact GO:0048001 node. The available SerC node grounds the distinct
  GO:0004648 phosphoserine reaction, not RHEA:16573, so it is not used for this
  leaf. The candidate PdxB node was omitted because its enclosing local PANTHER
  family label is not an honest PdxB family descriptor.
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

Gene-level OpenScientist reports are now integrated for all six genes. The
initial PdxJ request reached OpenScientist's 3600-second service ceiling and
returned no report; the wave111 retry completed after 1810.63 seconds with the
full 7200-second allowance. It found no direct Q88MY2 assay, so the review keeps
the exact UniProt/HAMAP reaction and ortholog evidence while declining
target-specific kinetic, structural, oligomeric, or essentiality claims.

The required annotation-reviewer pass checked all six reviews against their
GOA, UniProt, notes, and available research. Its blocking findings were
addressed: Epd pathway claims now carry explicit ortholog evidence and accurate
family wording; PdxJ's activity has direct UniProt and provider support; the
PdxH salvage quote is verbatim; PdxH's broad vitamin-B6 process is non-core; and
the upstream-PNP versus downstream-PdxH treatment of GO:0008615 is explicit.
The reviewer independently confirmed that GO:0004648 covers only the separate
SerC phosphoserine reaction and that RHEA:16573 has no exact GO MF term.

The generic OpenScientist module review completed after 2835.67 seconds. It
independently recovered the fixed six-step order and the same boundary around
DXP supply, salvage, and the non-homologous PdxS/PdxT pathway. Its broader
cross-organism mechanistic synthesis is retained as research context rather
than treated as direct evidence for the six KT2440 proteins.

## Validation

All six selected gene reviews pass `just validate`. The module passes LinkML
and semantic validation; the only semantic advisories are the expected local
resolver warnings for exact NCBIfam and InterPro family prefixes. All six gene
pages, the module page, and this batch page render successfully. Final checks
will be repeated after rebasing onto the latest `origin/main`.
