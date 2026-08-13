---
title: "PSEPK ppu00260 bacterial aspartate-to-threonine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_4473, asd__Q88LE4, asd__Q88LE2, hom, PP_0664, thrB, thrC, PP_0662]
autolink_gene_symbols: false
---

# PSEPK ppu00260: bacterial aspartate-to-threonine biosynthesis

- Reusable module: `modules/bacterial_aspartate_to_threonine_biosynthesis.yaml`
- Full-length pathway or paralog candidates reviewed: 8
- Ordered reactions modeled: 5
- Shared aspartate-family trunk reactions: 2
- Homoserine branch reaction shared with methionine: 1
- Threonine-specific reactions: 2
- Gene-level provider: OpenScientist
- Generic module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a five-part aspartate-to-threonine module.
- [x] Separate the shared aspartate-family trunk from threonine-specific steps.
- [x] Fetch the five canonical PSEPK proteins and three full-length paralog candidates.
- [x] Consult the annotation-reviewer for all eight current GOA sets.
- [x] Review every GOA annotation and document candidate uncertainty.
- [x] Integrate the OpenScientist reports completed before publication.
- [x] Complete gene, module, project, render, and test validation.
- [ ] Open one draft PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK protein(s) | UniProt | Decision |
|---|---|---|---|---|
| 1 | L-aspartate activation | `PP_4473` | Q88EI9 | Covered by the directly assayed monofunctional aspartate kinase; shared trunk |
| 2 | L-aspartate 4-semialdehyde formation | `asd__Q88LE4`; candidate `asd__Q88LE2` | Q88LE4; Q88LE2 | Covered by Q88LE4; Q88LE2 is an unconfirmed PTHR46278:SF2 USG-like candidate without HAMAP or UniPathway support |
| 3 | L-homoserine formation | `hom`; `PP_0664` | Q88MU8; Q88Q34 | Covered by Q88MU8; Q88Q34 is a shorter same-EC paralog with unresolved pathway partitioning |
| 4 | L-homoserine phosphorylation | `thrB` | Q88RK8 | Covered; first threonine-specific reaction in this boundary |
| 5 | O-phospho-L-homoserine conversion to L-threonine | `thrC`; candidate `PP_0662` | Q88MU7; Q88Q36 | Covered by Q88MU7; Q88Q36 is a predicted PLP-dependent threonine-synthase-like protein without direct catalytic or genetic evidence and does not independently satisfy the step |

The canonical five-reaction route is satisfiable in KT2440. Satisfiability does
not depend on promoting the weaker paralog candidates: Q88EI9, Q88LE4, Q88MU8,
Q88RK8, and Q88MU7 supply one evidence-grounded representative for each ordered
reaction.

## Boundary Decisions

- Aspartate kinase and aspartate-semialdehyde dehydrogenase are included because
  this module begins at L-aspartate, but they remain explicitly shared with the
  lysine and methionine branches.
- Homoserine dehydrogenase is shared with methionine biosynthesis. The reusable
  methionine module begins at homoserine and is not duplicated here.
- Homoserine kinase and threonine synthase are the threonine-specific portion of
  this bacterial boundary.
- L-threonine degradation, threonine aldolysis, and conversion to 2-oxobutanoate
  for isoleucine biosynthesis are downstream and excluded.
- The broad KEGG ppu00260 map also contains serine/glycine, methylated-glycine,
  phospholipid, vitamin B6, and catabolic reactions. They are not members of this
  focused module merely because they share the map.

## Candidate Decisions

| Candidate | Decision |
|---|---|
| `asd__Q88LE2` / PP_1992 | Retain as an unconfirmed Asd-family candidate only. PTHR46278:SF2 groups with USG-like proteins, and the record lacks the HAMAP and UniPathway support present for Q88LE4/SF4. |
| `PP_0664` | Retain as a predicted short homoserine dehydrogenase and possible redundant contributor; relative use versus `hom` is unresolved. |
| `PP_0662` | Retain a conservative predicted threonine-synthase-like function, but keep it outside terminal-step satisfaction until biochemical or genetic evidence establishes EC 4.2.3.1 and its role relative to canonical `thrC` in KT2440. |
| PP_1147 / Q88NQ8 | Exclude: the 109-residue record lacks EC, GO, InterPro, Pfam, and PANTHER support for a complete Asd enzyme. |

## Historical Source Review

The read-only preservation commit `86cf4fd8e9` was inspected for target-specific
Asta and first-pass curation content. It correctly surfaced the canonical five
steps and the Q88Q34/Q88Q36 paralog questions, but its broad
`glycine_serine_threonine_metabolism` boundary mixed several independent
pathways and placed multiple activities in one part. No files were cherry-picked.
Only locus identities and conservative candidate caveats that remain supported
by current UniProt metadata were retained.

## Research Status

OpenScientist was started for all eight selected genes, the generic reusable
module, and the combined module + ppu00260 + PSEPK question with wrapper timeout
8100 seconds, provider timeout 7200 seconds, and three iterations. Reports for
PP_0664, ThrB, and PP_0662 completed before publication and were integrated;
the other runs did not produce reports and were not treated as evidence.

The annotation-reviewer independently audited all eight GOA sets and the
module boundary. Its paralog-family analysis strengthened the Q88LE2 caveat,
supported Q88Q34 as a credible short-form Hom isozyme, and confirmed that
Q88Q36 must not satisfy the terminal step.

## Validation

All eight gene reviews pass `just validate`. The module passes LinkML and
semantic module validation, and the focused module/project rendering test suite
passes.
