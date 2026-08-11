---
title: "PSEPK ppu00650 bacterial 4-hydroxybutyrate oxidation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00650: bacterial 4-hydroxybutyrate oxidation

- Reusable module: `modules/bacterial_4_hydroxybutyrate_oxidation.yaml`
- Correct pathway boundary: oxidation of 4-hydroxybutyrate through succinate semialdehyde to succinate
- Newly reviewed PSEPK proteins: 4
- Module/pathway/taxon provider: OpenScientist (active, non-blocking)

## Workflow

- [x] Define a two-reaction pathway rather than a single-enzyme module.
- [x] Confirm the Gbd accession and specific catalytic activity.
- [x] Review all three local succinate-semialdehyde dehydrogenase candidates.
- [x] Model NAD- and NADP-linked implementations as alternatives.
- [x] Keep GABA catabolism, uptake, upstream 4-hydroxybutyrate production, and the TCA cycle outside the module.
- [x] Validate and render the module, genes, and project page.
- [x] Complete independent annotation-reviewer and module-curation audit.
- [x] Open one draft PR for this module: [#2534](https://github.com/ai4curation/ai-gene-review/pull/2534).
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | 4-hydroxybutyrate oxidation | `gbd` | Q88JJ9 | Covered |
| 2 | NAD-linked succinate-semialdehyde oxidation | `sad-I`, `sad-II` | Q88K05, Q88I50 | Candidate alternatives; physiological assignment unresolved |
| 2 | NADP-linked succinate-semialdehyde oxidation | `gabD-II` | Q88EN2 | Candidate alternative; may primarily serve the GABA shunt |

The chemistry is satisfiable in KT2440, but current evidence does not
identify which succinate-semialdehyde dehydrogenase is paired with Gbd during
growth on 4-hydroxybutyrate. The module therefore records candidate coverage
without choosing a paralog. The three listed enzymes are the focused candidates
recovered by product-name and family review, not an exhaustive genome-wide
enumeration; the `gabD-II` suffix is not treated as proof that all related
paralogs have been found.

## Annotation Decisions

- Gbd retains GO:0047577 as its core molecular function; compatible broad
  activity annotations are modified to that specific catalytic term.
- Sad-I and Sad-II retain the NAD-specific GO:0004777 activity without a
  pathway-process claim.
- GabD-II retains GO:0036243 as the current EC-derived NADP working prediction.
  Its conflicting NAD-specific TreeGrafter annotation is `UNDECIDED`, not
  removed, because neither cofactor assignment is supported by a direct assay.
- GabD-II's GABA catabolic-process annotation is also `UNDECIDED`: family
  inference does not resolve whether this paralog serves the GABA shunt,
  4-hydroxybutyrate oxidation, or another source of succinate semialdehyde.

## Boundary Decisions

- The module starts with the Gbd reaction and ends with succinate formation.
- Transport and upstream 4-hydroxybutyrate production are separate concerns.
- The GABA shunt is a neighboring source of the same aldehyde intermediate.
- Succinate entry into the TCA cycle is downstream.
- Molecular functions are placed only on leaf annotons.
- The second-reaction variants use `ONE_OR_MORE`; current evidence does not
  justify forcing exactly one paralog or cofactor implementation per organism.

## Research Status

OpenScientist sessions `25074` and `98912` remain active with their full provider
timeouts and are not publication blockers. UniProt and GOA records support this
conservative first-pass curation; unresolved cofactor and paralog assignments
are recorded explicitly rather than converted into pathway claims.

## Validation

All four gene reviews, the reusable module, and this project page are validated
and rendered before publication.
