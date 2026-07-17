---
title: "PSEPK ppu00300 L-lysine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00300: L-lysine biosynthesis

- Reusable module: `modules/lysine_biosynthesis.yaml`
- KEGG ppu00300 candidates inspected: 19
- Selected pathway proteins: 10
- Dedicated succinylated-DAP reactions covered: 7
- Retained paralog pairs: DapA, DapF, and LysA
- Excluded upstream, downstream, broad-family, or weak paralog candidates: 9
- Gene-level provider: OpenScientist
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a seven-part succinylated-diaminopimelate module.
- [x] Separate shared aspartate-semialdehyde supply from the dedicated route.
- [x] Separate meso-diaminopimelate use in peptidoglycan from L-lysine formation.
- [ ] Finish fetching and reviewing the ten selected PSEPK proteins.
- [ ] Complete OpenScientist module and gene reports.
- [x] Complete initial module validation.
- [ ] Validate and render module, gene, and project pages after evidence integration.
- [x] Open one draft PR for this module/pathway: [PR #2177](https://github.com/ai4curation/ai-gene-review/pull/2177).
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK protein(s) | UniProt | Decision |
|---|---|---|---|---|
| 1 | Aspartate semialdehyde plus pyruvate to hydroxytetrahydrodipicolinate | `dapA__Q88NH2`, `dapA__Q88JL0` | Q88NH2, Q88JL0 | Covered by two DapA-specific paralogs |
| 2 | Hydroxytetrahydrodipicolinate reduction | `dapB` | Q88DU4 | Covered |
| 3 | Tetrahydrodipicolinate succinylation | `dapD` | Q88MP1 | Covered; establishes the succinylase route |
| 4 | N-succinyl-diaminopimelate transamination | `dapC` | Q88MI3 | Covered by the beta/gammaproteobacterial DapC family |
| 5 | N-succinyl-diaminopimelate desuccinylation | `dapE` | Q88MP5 | Covered |
| 6 | LL-diaminopimelate epimerization to meso-diaminopimelate | `dapF__Q88GD4`, `dapF__Q88CF3` | Q88GD4, Q88CF3 | Covered by two DapF-family paralogs |
| 7 | meso-Diaminopimelate decarboxylation to L-lysine | `lysA-I`, `lysA` (`lysA-II`) | Q88L58, Q88CF4 | Covered by two LysA-family paralogs |

All seven dedicated reactions of the succinylated DAP route are present in
KT2440. The module is satisfiable without assigning generic aspartate-pathway
enzymes or peptidoglycan ligases as lysine-specific members. The retained DapA,
DapF, and LysA pairs create redundancy/condition-specificity questions, not
pathway holes.

## Shared Boundaries

- Aspartate kinase and aspartate-semialdehyde dehydrogenase produce the shared
  aspartate-semialdehyde input used by lysine, threonine, and methionine
  synthesis. The dedicated module begins with DapA.
- DapF produces meso-diaminopimelate, which can either enter LysA for L-lysine
  formation or be incorporated into peptidoglycan. MurE and MurF belong to the
  latter branch and are not L-lysine-biosynthesis members.

## Excluded Candidates

| Gene | Reason outside the curated core boundary |
|---|---|
| `PP_4473`, `asd__Q88LE4` | Shared upstream aspartate-pathway precursor supply rather than dedicated DAP-route membership |
| `PP_0664`, `hom` | Homoserine dehydrogenases serving threonine/methionine-family metabolism, not the DAP route |
| `murE`, `murF` | Downstream peptidoglycan assembly enzymes that consume meso-diaminopimelate-containing precursors |
| `aruC`, `aspC` | Broad aminotransferases not substituted for the DapC-specific family without physiological evidence |
| `PP_2036` | DapA-like EC/name call but lacks the DapA-specific InterPro/HAMAP and lysine-pathway signatures present on Q88NH2 and Q88JL0 |

## Module Decisions

- The module contains seven ordered reaction parts; it is not a one-enzyme
  wrapper around LysA.
- DapA, DapF, and LysA are family-selected steps with two exact PSEPK UniProt
  exemplars each. Current evidence supports the chemistry of both copies but
  does not establish their relative in-vivo flux.
- DapD, DapC, and DapE explicitly model the succinylated route rather than
  collapsing all taxonomic DAP-pathway variants into one ambiguous step.
- Molecular functions occur only on leaf annotons, and no module-level
  cytoplasm/cytosol pair is asserted.
- The obsolete GO:0009089 DAP-route process term is not authored as a new core
  term. Gene reviews use current GO:0009085 for L-lysine biosynthesis while
  preserving machine-sourced existing IDs for review.

## Research Interpretation

- The OpenScientist module/pathway/taxon report independently recovered all
  seven reactions and the diagnostic DapD/DapE succinylase-route boundary.
- The report found no direct KT2440 enzyme assays for the dedicated steps. Its
  sequence-identity-based rankings of DapA, DapF, and LysA copies are therefore
  retained as hypotheses, not used to exclude exact UniProt-supported
  paralogs from this first-pass reusable module.
- PP_1588 has DapC-specific InterPro/NCBIfam signatures and remains the selected
  step-4 enzyme. The possible contribution of the broader ArgD/AruC family is a
  physiological flux question rather than a pathway hole.

## Validation

The initial LinkML and module-validator checks pass. Gene validations and final
rendering will be completed after the accession-disambiguated fetch and
OpenScientist evidence pass.
