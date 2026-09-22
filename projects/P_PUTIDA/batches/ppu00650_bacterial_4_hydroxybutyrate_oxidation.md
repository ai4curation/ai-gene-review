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
- Focused gene providers: complete for Sad-I, Sad-II, and GabD-II

## Workflow

- [x] Define a two-reaction pathway rather than a single-enzyme module.
- [x] Confirm the Gbd accession and curate its predicted catalytic activity.
- [x] Review the three initial succinate-semialdehyde dehydrogenase candidates.
- [x] Retain the Sad-family implementation and exclude GabD-II after resolving its competing doe-locus context.
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
| Boundary | Doe-like ectoine catabolism | `gabD-II` | Q88EN2 | Excluded from this module; substrate remains unresolved |

The chemistry is satisfiable in KT2440, but current evidence does not
identify which succinate-semialdehyde dehydrogenase is paired with Gbd during
growth on 4-hydroxybutyrate. The module therefore records candidate coverage
without choosing between Sad-I and Sad-II. The listed enzymes are focused
candidates recovered by product-name and family review, not an exhaustive
genome-wide enumeration. GabD-II is retained as a reviewed boundary case but
removed from the module because its doe-like locus supports a competing
ectoine-catabolic substrate hypothesis. This pathway exclusion is not a claim
that Q88EN2 lacks succinate-semialdehyde dehydrogenase side activity.

## Annotation Decisions

- Gbd retains GO:0047577 as its core molecular function; compatible broad
  activity annotations are modified to that specific catalytic term.
- Sad-I and Sad-II use substrate-specific, cofactor-neutral GO:0009013 as core;
  their NAD-specific GO:0004777 annotations are `MODIFY` to GO:0009013 because
  the proteins are supported as succinate-semialdehyde dehydrogenases but their
  cofactor preferences remain unresolved.
- GabD-II uses substrate-neutral GO:0004030 as core. Its NAD-specific
  GO:0004777, NADP-specific GO:0036243, and GABA-catabolism GO:0009450 rows are
  `UNDECIDED` because no direct Q88EN2 assay resolves the conflict between the
  submitted SSADH assignment and the DoeC-like ectoine-locus hypothesis.

## Boundary Decisions

- The module starts with the Gbd reaction and ends with succinate formation.
- Transport and upstream 4-hydroxybutyrate production are separate concerns.
- The GABA shunt is a neighboring source of the same aldehyde intermediate.
- Succinate entry into the TCA cycle is downstream.
- Molecular functions are placed only on leaf annotons.
- The second reaction uses the Sad family with Sad-I and Sad-II as candidate
  exemplars; current evidence does not justify choosing one operative paralog.
- No gene-level 4-hydroxybutyrate catabolic-process annotation is proposed:
  GO lacks a specific process term and the operative KT2440 proteins remain
  unresolved. The module records this as an ontology/curation knowledge gap.

## Research Status

The module OpenScientist report is complete and was reconciled with primary
literature. Focused OpenScientist reports for `sad-I`, `sad-II`, and `gabD-II` are complete;
their provider-generated locus and residue mappings are recorded as research
leads rather than published evidence. The GabD-II report's DoeC hypothesis is
corroborated by local neighborhood metadata but remains unconfirmed without a
target-specific enzyme assay. Unresolved substrate, cofactor, and paralog
assignments are recorded explicitly rather than converted into pathway claims.

## Validation

All four gene reviews, the reusable module, and this project page are validated
and rendered before publication.
