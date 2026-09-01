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
- [x] Finish fetching and reviewing the ten selected PSEPK proteins.
- [x] Attempt OpenScientist research for the module and all ten genes; eight
  gene reports completed in the first pass and two provider timeouts were
  documented in notes.
- [x] Complete initial module validation.
- [x] Validate and render module, gene, and project pages after evidence integration.
- [x] Merge the first-pass module/pathway curation in [PR #2177](https://github.com/ai4curation/ai-gene-review/pull/2177).

### Repair wave107

- [x] Remove KT2440-specific evidence, paralog gaps, and candidate exclusions
  from the reusable module.
- [x] Replace the module's PSEPK-only representative sets with reviewed
  non-PSEPK reaction exemplars.
- [x] Verify exact PANTHER labels and representative-member containment.
- [x] Add only PAINT nodes with explicit local IBD rows for the leaf activity.
- [x] Complete the two previously timed-out OpenScientist gene reports with a
  7200-second allowance and no cancellation.
- [x] Complete annotation-reviewer consultation and address its blocking findings.
- [x] Validate and render all changed outputs.
- [x] Open one PR and request review.

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
| `aruC`, `aspC` | Broad aminotransferases not substituted for the DapC-specific family without physiological evidence; the module report's DapL-like `aspC` mapping is treated as likely pathway-map over-propagation |
| `PP_2036` | DapA-like EC/name call in the metadata, but no lysine-pathway assignment or target review establishes it as a third pathway DapA |

## Module Decisions

- The module contains seven ordered reaction parts; it is not a one-enzyme
  wrapper around LysA.
- DapA, DapB, DapF, and LysA use exact PANTHER parent families with reviewed
  E. coli reaction exemplars. The PSEPK paralog sets remain part of this
  concrete satisfiability record rather than the reusable family definitions.
- DapD, DapC, and DapE explicitly model the succinylated route rather than
  collapsing all taxonomic DAP-pathway variants into one ambiguous step.
- DapA PTN000252718, DapB PTN000464618, DapE PTN000110566, DapF
  PTN000784348, and LysA PTN000159906 are asserted from explicit
  `GO_REF:0000033` IBD rows in the local PAINT exports. DapD and DapC retain no
  family or PTN identifiers because no clear function-specific assertion was
  established. DapE retains its exact activity PTN but no broad parent-family
  identifier.
- Molecular functions occur only on leaf annotons, and no module-level
  cytoplasm/cytosol pair is asserted.
- The obsolete GO:0009089 cross-reference is not authored as a new core term.
  Gene reviews use current GO:0009085 for L-lysine biosynthesis while
  preserving machine-sourced existing IDs for review.

## Research Interpretation

- The OpenScientist module/pathway/taxon report independently recovered all
  seven reactions and the diagnostic DapD/DapE succinylase-route boundary.
- The report found no direct KT2440 enzyme assays for the dedicated steps. Its
  sequence-identity-based rankings of DapA, DapF, and LysA copies are therefore
  retained as hypotheses, not used to exclude exact UniProt-supported
  paralogs from this first-pass reusable module.
- The gene-level DapF reports interpret the Q88GD4 UniProt CAUTION about
  conserved residues missing for HAMAP feature propagation as a putative
  paired-serine DapF-SS signature (Ser70/Ser205), alongside the
  canonical paired-cysteine Q88CF3 DapF-CC copy (Cys75/Cys219). PMID:40774471
  establishes the DapF-SS class, but neither KT2440 paralog has a direct assay;
  activity partitioning and gene-specific essentiality remain open.
- Eight gene-level OpenScientist reports completed in the first pass. The
  previously timed-out DapA-II (`dapA__Q88JL0`) and DapB reports completed in
  this repair with a 7200-second provider allowance and without cancellation.
- Both LysA reports support EC 4.1.1.20, but neither establishes the relative
  in-vivo contribution of Q88L58 and Q88CF4. The LysA-II report's inference
  from adjacency to `dapF` is retained as context, not as evidence that Q88CF4
  is the dominant or dedicated copy.
- PP_1588 has DapC-specific InterPro/NCBIfam signatures and remains the selected
  step-4 enzyme. The possible contribution of the broader ArgD/AruC family is a
  physiological flux question rather than a pathway hole.

## Validation

All ten pathway-gene reviews pass `just validate`; the five edited reviews were
revalidated after evidence corrections. The module passes LinkML validation and
semantic validation. The sole semantic advisory is intentional: the verified
DapA exemplar belongs to PTHR12128:SF66, whose official label names a different
aldolase, so the exact parent PTHR12128 label is retained instead of asserting a
misleading subfamily ID. The changed gene, module, and project pages render
successfully, and cache-only validation noise is excluded from the repair.
