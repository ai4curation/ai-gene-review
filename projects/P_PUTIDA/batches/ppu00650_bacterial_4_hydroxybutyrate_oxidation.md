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
- Module research provider: OpenScientist (complete)
- Focused gene providers: active for three SSADH candidates (non-blocking)

## Workflow

- [x] Define a two-reaction pathway rather than a single-enzyme module.
- [x] Confirm the Gbd accession and curate its predicted catalytic activity.
- [x] Review all three local succinate-semialdehyde dehydrogenase candidates.
- [x] Model Sad- and GabD-family implementations with unresolved cofactor preference.
- [x] Keep GABA catabolism, uptake, upstream 4-hydroxybutyrate production, and the TCA cycle outside the module.
- [x] Validate and render the module, genes, and project page.
- [x] Complete independent annotation-reviewer and module-curation audit.
- [x] Open one draft PR for this module: [#2534](https://github.com/ai4curation/ai-gene-review/pull/2534).
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | 4-hydroxybutyrate oxidation | `gbd` | Q88JJ9 | Covered |
| 2 | Sad-family succinate-semialdehyde oxidation | `sad-I`, `sad-II` | Q88K05, Q88I50 | NAD(P)-linked candidate alternatives; cofactor and physiological assignment unresolved |
| 2 | GabD-family succinate-semialdehyde oxidation | `gabD-II` | Q88EN2 | NAD(P)-linked candidate alternative; may primarily serve the GABA shunt |

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
- Sad-I and Sad-II retain cofactor-neutral GO:0004030 as core; their
  NAD-specific GO:0004777 annotations are `UNDECIDED` because submitter and
  family metadata conflict.
- GabD-II retains cofactor-neutral GO:0016620 as core. Both its NAD-specific
  TreeGrafter annotation and EC-derived NADP annotation are `UNDECIDED` because
  neither assignment is supported by a direct Q88EN2 assay.
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
- No gene-level 4-hydroxybutyrate catabolic-process annotation is proposed:
  GO lacks a specific process term and the operative KT2440 proteins remain
  unresolved. The module records this as an ontology/curation knowledge gap.

## Research Status

The module OpenScientist report is complete and was reconciled with primary
literature. Focused OpenScientist jobs for `sad-I`, `sad-II`, and `gabD-II`
remain active with full provider timeouts and are not publication blockers.
Unresolved cofactor and paralog assignments are recorded explicitly rather than
converted into pathway claims.

## Validation

All four gene reviews, the reusable module, and this project page are validated
and rendered before publication.
