---
title: Human Proteostasis Network
species: [human]
status: SCOPING
priority: high
scope: Full Proteostasis Consortium workbook and manuscripts; unfolded protein binding is a sub-use case
sidecars:
  priority_genes: PROTEOSTASIS/priority_genes.tsv
  mapping_sets_dir: PROTEOSTASIS/mappings
  tests_dir: PROTEOSTASIS/tests
  reports_dir: PROTEOSTASIS/reports
  upb_genes: UNFOLDED_PROTEIN_BINDING/genes.csv
related_projects:
  - UNFOLDED_PROTEIN_BINDING.md
  - RIBOSOME_QUALITY_CONTROL.md
  - INTEGRATED_STRESS_RESPONSE.md
  - ER_PHAGY.md
external_sources:
  - Human Proteostasis Network Annotation 2.0 workbook (release 2024-04-15)
  - Survey of the Human PN MS1 Translation Folding Transport
  - Survey of the Human PN MS2 ALP
  - Survey of the Human PN MS3 UPS
---
# Human Proteostasis Network Project

## Background

Proteostasis is used here in the broad systems sense: the cellular machinery that
supports protein synthesis, folding, trafficking, quality control, sequestration,
and degradation.

The source resource analyzed in this project is the **Human Proteostasis Network
Annotation 2.0** workbook together with three Proteostasis Consortium survey
manuscripts:

- `MS1` introduces the overall PN framework and covers translation, folding,
  transport, and organelle-specific proteostasis systems.
- `MS2` covers the autophagy-lysosome pathway (`ALP`) and provides the most
  detailed row-level notes and references in the current release.
- `MS3` covers the ubiquitin-proteasome system (`UPS`) and explains the
  domain-heavy inclusion and classification logic used for that branch.

The workbook used here is the `2024-04-15` PN release downloaded from the
Proteostasis Consortium PN annotation site, matching the supplementary
annotation release cited in the manuscript data-availability sections.

## Overview

The Proteostasis Consortium workbook and papers define a curated human proteostasis
membership and role taxonomy. They do **not** define a GO-ready annotation set.

This project asks three main questions:

- What biological claims do the PN annotations actually make?
- Which PN statements are close to GO terms, which imply ontology gaps, and which
  are better treated as systems metadata?
- Which workbook entries look especially useful, curious, or suspect in the
  context of AIGR?

Within this project:

- the PN resource provides systems architecture and candidate roles
- unfolded protein binding is treated as one mechanistic subdomain within proteostasis
- AIGR uses PN as a scaffold, a QA source, and a prioritization layer

See:

- [Priority genes](PROTEOSTASIS/priority_genes.tsv)
- [ALP mapping set](PROTEOSTASIS/mappings/autophagy_lysosome_pathway.yaml)
- [Chaperone mapping set](PROTEOSTASIS/mappings/chaperone_systems.yaml)
- [ER proteostasis mapping set](PROTEOSTASIS/mappings/er_proteostasis.yaml)
- [Mitochondrial proteostasis mapping set](PROTEOSTASIS/mappings/mitochondrial_proteostasis.yaml)
- [Nuclear proteostasis mapping set](PROTEOSTASIS/mappings/nuclear_proteostasis.yaml)
- [PN regulation mapping set](PROTEOSTASIS/mappings/pn_regulation.yaml)
- [Translation mapping set](PROTEOSTASIS/mappings/translation.yaml)
- [Project-local tests](PROTEOSTASIS/tests)
- [Project-local reports](PROTEOSTASIS/reports)
- [UPB gene list](UNFOLDED_PROTEIN_BINDING/genes.csv)
- [Unfolded Protein Binding project](UNFOLDED_PROTEIN_BINDING.md)
- [Ribosome Quality Control project](RIBOSOME_QUALITY_CONTROL.md)
- [Integrated Stress Response project](INTEGRATED_STRESS_RESPONSE.md)
- [ER-phagy project](ER_PHAGY.md)

## What The PN Resource Actually Contains

The workbook is a row-per-role annotation table, not a gene-centered review file.

- `2989` unique genes
- `3774` annotation rows
- `312` genes with cross-branch annotations
- `274` genes with multiple annotations within one branch
- `2403` genes with a single annotation

The custom hierarchy has:

- `9` Branches
- `32` Classes
- `253` Groups
- `562` Types
- `385` Subtypes

This is their own vocabulary:

- the workbook contains **no GO IDs or explicit GO term mappings**
- the papers explicitly describe the PN hierarchy as a taxonomy that **complements** structured vocabularies such as GO
- the manuscripts say GO, Reactome, KEGG, UniProt, and InterPro were used as **inputs** for building preliminary lists, not as the target representation

### Evidence Shape By Branch

The current release is uneven by design.

| Branch set | What is present in the workbook | What it means for reuse |
|------------|----------------------------------|--------------------------|
| ALP | Per-row notes for `1003/1003` rows and references for `1001/1003` rows | Best-supported branch for row-level reuse and audit |
| UPS | Principal domains for `1528/1528` rows and auxiliary domains for `1521/1528` rows | Strong domain/family scaffold, but weaker row-level functional justification in this release |
| Other 7 branches | No row-level notes, no row-level references, no domain columns | Useful as curated membership/context, but not ready to import into GO as-is |

### What Each Level Means

The hierarchy is semantically mixed, which is the main reason it does not map cleanly to GO.

| PN level | What it usually encodes | Relation to GO |
|----------|--------------------------|----------------|
| Branch | Localization or top-level pathway membership | BP/CC hybrid, not a GO class |
| Class | Function in proteostasis, except ALP where it is a stage of autophagy | MF/BP hybrid |
| Group | System, complex, pathway module, or mechanistic bucket | Sometimes GO-like, often not |
| Type | More specific mechanistic role, family, or complex membership | May correspond to MF, BP, CC, or family metadata |
| Subtype | Structural family, domain class, or finer mechanistic subdivision | Often outside GO scope |

Examples by level:

- `Branch`
  - `Cytonuclear proteostasis`
  - `ER proteostasis`
  - `Autophagy-Lysosome Pathway`
  - `Ubiquitin Proteasome System`
- `Class`
  - `Chaperone`
  - `Protein transport`
  - `Autophagophore initiation and elongation`
  - `E3 ubiquitin and UBL ligases`
- `Group`
  - `HSP70 system`
  - `TRAP complex component`
  - `Class 3 PI3K complex 1, direct`
  - `CRL family`
- `Type`
  - `HSP70 nucleotide exchange factor`
  - `J-domain containing HSP70 cochaperone`
  - `Modulator of class 3 PI3K complex 1 activity`
  - `BTB`
- `Subtype`
  - `BAG domain family`
  - `KCTD type`
  - `WD40`
  - many rows have no subtype

Fully expanded examples:

- `BAG1`
  - `Cytonuclear proteostasis -> Chaperone -> HSP70 system -> HSP70 nucleotide exchange factor -> BAG domain family`
- `STAT1`
  - `Autophagy-Lysosome Pathway -> Autophagy gene expression -> Transcriptional repressor`
- `KCTD11`
  - `Ubiquitin Proteasome System -> E3 ubiquitin and UBL ligases -> CRL family -> BTB -> KCTD type`

These are informative for humans, but they are not all GO terms and they are not all the same kind of thing.

## Relationship To GO

### Explicit GO mapping

There is essentially none in the released workbook.

- I searched the workbook for `GO:` and `Gene Ontology` strings and found none.
- The row schema is PN-native: `Branch/Class/Group/Type/Subtype`, plus optional notes, references, and UPS domain fields.
- The papers cite GO as a source database used to build candidate lists, especially for ALP, not as a field embedded back into the final annotation table.

### Implicit GO mapping

There is a lot of **implicit** overlap with GO, but it is inconsistent in kind.

Some PN rows look close to GO:

- `TRAP complex component`
- `Class 3 PI3K complex 1 component`
- `HSP70 nucleotide exchange factor`
- `Ribosome-associated QC`

But many PN labels are not GO-ready assertions:

- family labels like `BAG domain family`
- domain labels like `WD40` or `TPR domain containing`
- branch-local staging labels like `Autophagophore initiation and elongation`
- inclusive UPS buckets like `RING`, `BTB`, `DCAF`, `MEX3`

So the right reading is:

- the PN taxonomy is biologically meaningful
- some rows are close to GO MF/BP/CC concepts
- many rows are module, family, or pathway-context labels rather than GO-annotatable facts

## Strategy For Bringing PN Into GO

This section is independent of AIGR workflow.

### 1. Separate membership from GO assertion

A PN row first tells us:

- this gene belongs in proteostasis
- the authors place it in a particular proteostasis module

It does **not** automatically tell us:

- the correct GO aspect
- the exact GO term
- whether the role is core vs contextual
- whether the evidence is strong enough for manual GO curation

### 2. Tag each row by provenance

At minimum, rows should be split into:

- `entity_based_literature_supported`
- `domain_based_family_inference`
- `ALP_note_backed`
- `UPS_domain_backed`
- `cross_branch_context_only`

This is the biggest determinant of whether a row is GO-ready, prediction-like, or just useful context.

### 3. Decompose each PN row into candidate GO semantics

Each row should be classified into one of four buckets:

1. `exact_or_near_GO`
   Example: complex component, transport process, clear enzymatic role.
2. `GO_with_context_loss`
   Example: a GO term exists but loses the proteostasis-system framing.
3. `ontology_gap`
   Example: the biology is real but current GO lacks a clean term or term family.
4. `non_GO_metadata`
   Example: family/domain/subtype labels that should stay as supporting metadata.

### 4. Curate by branch, not all at once

The branches are not equally reusable.

- Start with ALP rows that have notes and references.
- Use non-ALP/non-UPS branches to identify likely GO-compatible roles and obvious positive controls.
- Treat UPS as a mixed case: many rows are probably best handled as prediction candidates or review leads until branch-specific evidence is inspected.

### 5. Keep domain-based rows conservative

The papers explicitly flag domain-based inclusions and borderline cases.

Concrete examples:

- `HSPA12A` and `HSPA12B` are included as HSP70-family PN components even though MS1 says their proteostasis functions are not yet known.
- UPS authors explicitly say they aimed to be inclusive and that domain weight is debatable in some cases.

These should not be imported into GO as manual curation without independent evidence.

### 6. Expect ontology-gap work

The PN resource reinforces that GO has missing or awkward coverage around:

- holdase chaperoning
- sensor/adaptor roles in quality control
- co-chaperone mechanistic MF space
- proteostasis-system context that mixes process and molecular role

## AIGR Triage Opportunities

The PN resource is useful inside AIGR primarily as a **triage and QA layer**.

### High-value positive controls

These are cases where PN and existing AIGR work largely agree and help validate the framework:

- `CRYAA`, `CRYAB`: PN small-HSP placement agrees with the UPB/holdase interpretation
- `SSR1`, `SSR2`: PN `TRAP complex component` fits existing ER protein-targeting/translocation GO work
- `EDF1`: PN ribosome-associated QC placement is consistent with the current AIGR review
- `KCTD11`: PN CRL/BTB placement matches the current AIGR view of a Cul3 adaptor

### Context-specific but plausible PN rows

These are probably real, but should be treated as non-core or secondary until checked carefully:

- `STAT1`: ALP transcriptional repressor role based on `ULK1` promoter regulation
- `BIRC6`: ALP docking/fusion regulator role on top of its core UPS E2/E3 biology
- `CIAO1`: UPS `DCAF` placement on top of its stronger Fe-S assembly/chaperone identity

### Domain- or family-driven caution cases

These are especially useful for AIGR because the papers themselves signal uncertainty or inclusivity:

- `HSPA12A`, `HSPA12B`: included as HSP70 PN components despite admitted lack of clear proteostasis function
- `AARSD1`: dual placement as `HSP90 cochaperone` and `tRNA synthetase`
- `BAG6`: split across GET-pathway transport and UPS; MS1 explicitly distinguishes it from canonical BAG-domain NEFs
- `TTC28`: PN places it as an HSP70-HSP90 joint cochaperone, but the current AIGR review treats it as a mitotic scaffold
- `MEX3B`: RING-family UPS placement may be real but needs distinction between family membership and core proteostasis role

### Existing-review rereview examples

On the `83`-gene existing-review queue, the useful distinction was not just the
pipeline label but whether the PN-projected term was actually a better GO
assertion than the current AIGR review. In practice,
`more_specific_than_existing_goa` is a projection label, not a guarantee that
the PN term remains the most specific biologically defensible choice after
manual rereview.

- `BCAP31` (`more_specific_than_existing_goa`): accepted `GO:0036503 ERAD pathway`.
  This is a good positive-control case where the PN mapping is exact and the
  biology holds up. The current review already supported direct ERAD
  participation, and the rereview added the pathway term because BCAP31 helps
  handle retrotranslocation of ERAD substrates rather than only acting in a
  looser ER-stress or regulatory context.
- `EDF1` (`new_to_goa`): PN suggested `GO:0002181 cytoplasmic translation`,
  `GO:0006412 translation`, and `GO:0006515 protein quality control for
  misfolded or incompletely synthesized proteins`. Only `GO:0006515` survived
  conservative rereview. The broad translation terms were not added because the
  best-supported biology is collided-ribosome surveillance and
  ribosome-associated quality control rather than generic translation.
- `TOMM20` (`more_specific_than_existing_goa` in the queue): rejected. The PN
  mitochondrial mapping propagates the group-level `Protein import` bucket to
  `GO:0017038 protein import`, but the current AIGR review already uses the
  route-specific mitochondrial import term `GO:0030150 protein import into
  mitochondrial matrix`. At the gene-review level, the PN suggestion was
  broader rather than more specific.
- `HSPA8` (`more_specific_than_existing_goa` in the queue): rejected. The PN
  `GO:0035973 aggrephagy` projection comes from a selective-autophagy-receptor
  path, whereas the current review already captures HSPA8's direct and much
  better supported CMA biology with `GO:0061684 chaperone-mediated autophagy`
  and `GO:0061740 protein targeting to lysosome involved in chaperone-mediated
  autophagy`. HSPA8 clearly participates in proteostasis and aggregate handling,
  but that did not justify promoting it to aggrephagy here.
- `RAB7A` (`more_specific_than_existing_goa` in the queue): rejected on
  conservative rereview. PN projected `GO:0061909 autophagosome-lysosome
  fusion`, but the local evidence base is mixed, and mammalian knockout work
  supports a stronger role in post-fusion autolysosome maturation than in the
  fusion step itself. That was not strong enough to add the more specific term
  to the human review.

## Priority Review Targets

See [priority_genes.tsv](PROTEOSTASIS/priority_genes.tsv).

Recommended first-pass jobs:

1. `BTF3`: fetch and review the true human `BTF3` gene (`P20290`) as the PN
   nascent-polypeptide-associated complex component.
2. `HSPA12A` and `HSPA12B`: fetch and review as explicit domain-based PN inclusions.
3. `AARSD1`: review the dual chaperone/translation placement.
4. `BAG6`: review as a multi-branch boundary case connecting transport, UBL biology, and proteostasis.
5. `TTC28`: explicitly test the PN cochaperone claim against the existing mitosis-focused review.

## PN-vs-UPB Comparison

- all `33/33` human UPB genes are present in the PN workbook
- most of those genes are consistent with PN placement at a coarse level
- the best bridge cases are the small HSPs, HSP70/J-domain systems, and the QC boundary genes

The UPB project is the best place to reason about:

- direct unfolded-protein binding
- holdase vs foldase vs co-chaperone distinctions
- GO MF correction and ontology-gap pressure

The PN project is broader:

- define the proteostasis universe
- understand the authors' own annotation model
- identify GO-compatible vs non-GO-compatible PN statements
- use PN to drive AIGR QA and job selection

## Next Steps

- Create a row-level PN-to-GO mapping table with provenance tags.
- Audit the highest-priority genes in [priority_genes.tsv](PROTEOSTASIS/priority_genes.tsv).
- Separate PN roles that belong in GO from roles better treated as prediction review inputs or systems metadata.
