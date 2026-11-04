---
title: "PSEPK ImuABC damage-induced mutagenesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [recA, lexA2, PP_3117, imuB, dnaE2]
autolink_gene_symbols: false
---

# PSEPK ImuABC damage-induced mutagenesis

This batch models the PP_3116-PP_3119 LexA2-ImuA-ImuB-DnaE2 cassette and its
RecA damage signal as a reusable bacterial damage-induced mutagenesis module.
The three ImuABC effector roles are mandatory; RecA/LexA regulation is explicit
but optional because induction architecture and LexA paralog usage vary among
bacteria.

## Workflow

- [x] Confirm no existing ImuABC/DnaE2 module or pathway PR.
- [x] Reuse the curated KT2440 recA and lexA2 reviews.
- [x] Fetch current UniProt and GOA records for PP_3117, imuB, and dnaE2.
- [x] Start full-allowance OpenScientist research for the three uncured genes.
- [x] Curate the three GOA sets and synthesize core functions.
- [x] Run and integrate reusable-module and PSEPK cassette research.
- [x] Validate and render all new artifacts.
- [x] Open one draft PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK gene | UniProt | Initial assessment |
|---|---|---|---|---|
| 1 | RecA damage signal | recA / PP_1629 | Q88ME4 | Covered by the already curated RecA ATP-dependent DNA damage sensor |
| 2 | Cassette repression/derepression | lexA2 / PP_3116 | P59479 | Covered by organism-specific experimental evidence for local cassette repression |
| 3 | ImuA accessory role | PP_3117 | Q88I84 | Covered by IPR047610 and PTHR35369:SF3; molecular mechanism remains incomplete |
| 4 | ImuB recruitment scaffold | imuB / PP_3118 | Q88I83 | Covered by the IMS/UmuC-like noncatalytic accessory family and cassette context |
| 5 | Mutagenic DNA synthesis | dnaE2 / PP_3119 | Q88I82 | Covered by reviewed HAMAP MF_01902 DnaE2 polymerase |

## Boundary

- Include damage induction, cassette derepression, accessory recruitment, and DnaE2 synthesis.
- Exclude canonical excision repair and homologous recombination chemistry.
- Exclude constitutive chromosome replication by the housekeeping DnaE polymerase.
- Do not assign catalytic molecular functions to ImuA or ImuB without direct evidence.

Generated UTC: 2026-08-12

2026-08-13: Review follow-up added direct P. putida evidence. The species data
show that ImuB and DnaE2 have context-dependent, sometimes antagonistic effects
on mutation accumulation, while ImuC/DnaE2 participates in alkylation-damage
tolerance. ImuB is modeled as an adaptor rather than a polymerase contributor.

2026-11-04: Module generalized beyond PSEPK and promoted to COMPLETE. The
cassette is characterized experimentally in three distant lineages, so the
module is now species-neutral (scope ABSTRACT) with KT2440 as one exemplar of
three, alongside Caulobacter crescentus (PMID:15886391) and Mycobacterium
tuberculosis (PMID:20615954). Six new COMPLETE gene reviews were added for those
exemplars (CAUVC imuA/imuB/dnaE2, MYCTU Rv3395c/Rv3394c/dnaE2) and the five
KT2440 reviews listed above were promoted from DRAFT to COMPLETE. The accessory
role became a REALIZER variant set, because actinobacteria have no ImuA homolog
and use the non-orthologous ImuA' (Rv3395c) instead; the boundary rule above
against assigning catalytic functions to ImuA or ImuB is kept, and no molecular
function is asserted for either accessory protein. PANTHER family reviews were
written for all four families the module touches (PTHR45900, PTHR33516,
PTHR35369, PTHR32294); the PTHR35369 review records that the family's only PAINT
node places DNA repair at the root and so reaches the SulA cell-division
inhibitors.
