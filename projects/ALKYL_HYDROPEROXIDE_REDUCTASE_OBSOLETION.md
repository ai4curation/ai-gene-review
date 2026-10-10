---
title: "Alkyl Hydroperoxide Reductase Activity — Obsoletion & Replacement"
maturity: SCOPING
tags: [OBSOLETION]
species: [ECOLI, PSEAE, PSEPK]
manifest:
  slides:
    - href: ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION/slides/ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/QG3qUxoDDS2zn4KB6e6ydj
      title: Project brief
---

# Alkyl Hydroperoxide Reductase Activity — Obsoletion & Replacement

**Bottom line:** GO obsoleted the molecular function term GO:0008785
*alkyl hydroperoxide reductase activity*, whose definition fixed a single
substrate (octane hydroperoxide) that no known enzyme is specific for, and
merged it into GO:0102039 *NADH-dependent peroxiredoxin activity*
(EC 1.11.1.26). The ontology change is merged upstream
(geneontology/go-ontology#32015). In this repo, E. coli **AhpF** is now reviewed against the
migrated GO:0102039 row: the review keeps GO:0102039 as a whole-system
activity that AhpF contributes to, but scopes AhpF's own molecular function to
GO:0047134 *protein-disulfide reductase [NAD(P)H] activity* and seeds a
concrete `bacterial_alkyl_hydroperoxide_reductase` module.
The remaining direct follow-on is P. aeruginosa PA3529/Q9HY81, an `AhpC`-type
peroxiredoxin that still lacks a local review. The P. putida **ahpC** review
provides the other relevant precedent: its GO:0102039 IEA row is modified to
the donor-independent GO:0051920 *peroxiredoxin activity* because `AhpC` is
the peroxide-attacking subunit and `AhpF` supplies the NADH electrons.

## Overview

A GO obsoletion has retired one molecular function term and merged its
annotations into a broader, more accurate term:

- **GO:0008785 alkyl hydroperoxide reductase activity** (MF, obsolete)

Replaced by:

- **GO:0102039 NADH-dependent peroxiredoxin activity** (MF;
  EC 1.11.1.26; RHEA:62628)

The rationale, captured in the upstream go-ontology ticket, is that
GO:0008785 was defined with a substrate-specific stoichiometry
(octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol) that is
more specific than the specificity of any known gene product, and
"alkyl hydroperoxide reductase" is listed by Expasy as a synonym of
EC 1.11.1.26 — i.e. exactly the broader term GO:0102039.

This project tracks the impact on AI Gene Review, the AhpF follow-on
review now in the repo, and the PA3529 review that still needs to be
started.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6396](https://github.com/geneontology/go-annotation/issues/6396)
- Ontology ticket: [geneontology/go-ontology#31961](https://github.com/geneontology/go-ontology/issues/31961)
- Ontology obsoletion PR: [geneontology/go-ontology#32015](https://github.com/geneontology/go-ontology/pull/32015) — **merged**, so the obsoletion is already in production.
- The closely-related "alkyl hydroperoxide reductase complex" CC term
  GO:0009321 had its `comment` updated by the obsoletion PR to point
  to GO:0102039 — it is **not** obsolete and remains the right CC for
  the `AhpC`/`AhpF` complex.

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| alkyl hydroperoxide reductase activity | GO:0008785 (obsolete) | GO:0102039 NADH-dependent peroxiredoxin activity |

### Affected experimental annotations (from upstream issue body)

The upstream issue body listed 2 direct experimental annotations against
GO:0008785 that needed review:

| Group | Gene | Species | Source ID | Reference | Evidence | PANTHER | Status |
|---|---|---|---|---|---|---|---|
| EcoliWiki | AhpF | E. coli K-12 (NCBITaxon:83333) | EcoCyc:EG11385-MONOMER | PMID:11717276 | IGI (with `ahpC`, `katE`, `katG`) | — | current GOA has GO:0102039; local review complete |
| PseudoCAP | PA3529 | P. aeruginosa PAO1 (NCBITaxon:208964) | UniProtKB:Q9HY81 | PMID:21674802 | IDA | PTHR10681 | pending local review |

No InterPro2GO, UniProt-Keywords, or UniRule mappings to GO:0008785
were listed in the upstream issue.

## Impact on this repo

No pre-existing AI Gene Review entry carried GO:0008785, so no old local
review needed refresh for the obsoletion itself. The project instead
created a new ECOLI AhpF review after current GOA had already migrated
that gene to GO:0102039, then used the existing PSEPK ahpC review to
check how the replacement term should be handled on the peroxide-attacking
subunit.

The remaining direct-annotation gap is PA3529/Q9HY81 in `genes/PSEAE/`
([#514](https://github.com/ai4curation/ai-gene-review/issues/514)).
Completing ECOLI `ahpC` would also finish the peroxide-consuming half of the
new `bacterial_alkyl_hydroperoxide_reductase` module
([#4032](https://github.com/ai4curation/ai-gene-review/issues/4032)).

The PANTHER family **PTHR10681** (the peroxiredoxin/`AhpC` family, not the
AhpF reductase family) appears in the with/from column for the PA3529
IDA annotation. IBA propagation from this family should be reviewed once
GOA pipelines pick up the obsoletion, but per the upstream issue no IBA
migrations are listed as separate items, so this is opportunistic rather
than required.

## Scope

- **Organisms**: E. coli K-12 (`genes/ECOLI/`) and P. aeruginosa
  PAO1 (`genes/PSEAE/`) for the two direct obsoletion rows, with
  P. putida KT2440 (`genes/PSEPK/`) as the already-reviewed `AhpC`
  comparison.
- **GO branches**: MF only — the obsoletion is a substrate-specificity
  collapse to the broader EC 1.11.1.26 term. No BP or CC changes.
- **Type of fix**: terminological — the biology (NADH-dependent
  peroxide reduction) is unchanged; reviews would evaluate whether
  GO:0102039 captures the gene's core function or whether more
  specific peroxiredoxin descendants are appropriate.
- **Related complex term**: GO:0009321 alkyl hydroperoxide reductase
  complex (CC) is **not** obsoleted and remains the correct cellular
  component for `AhpC`/`AhpF` holocomplex annotations.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting
and confirm UniProt accessions. AhpF has been reviewed; PA3529 is still absent.

### Tier 1 — reviewed direct annotation

1. **AhpF** (E. coli K-12, EcoCyc:EG11385-MONOMER) — the FAD-containing
   NADH-dependent disulfide reductase subunit of the `AhpC`/`AhpF` system.
   Reduces oxidized `AhpC` (the peroxiredoxin subunit) at the expense
   of NADH. The IGI annotation from PMID:11717276 was made together
   with `ahpC`, `katE`, and `katG`, so the biological context is peroxide
   detoxification in concert with catalases. The 2026-10-02 ECOLI AhpF
   review modifies GO:0102039 to GO:0047134 for AhpF's own activity and
   records GO:0102039 as a contributed whole-system activity.

### Tier 2 — direct annotation, less canonical

2. **PA3529 / Q9HY81** (P. aeruginosa PAO1) — IDA annotation from
   PMID:21674802 by PseudoCAP. UniProt has no recommended gene symbol
   beyond the ordered locus name and places Q9HY81 in the `AhpC`/Prx1
   peroxiredoxin family PTHR10681. Verify that `PA3529` is still the
   best local folder name before creating the review. This is now the
   direct upstream experimental row without a local review.

## Proposed approach

1. **Obsoletion has landed.** GO:0008785 is already obsolete in the
   ontology (PR #32015 merged). The 2 direct annotations in the
   upstream tracker have **not yet been migrated** as of project
   creation date — that is the open work upstream issue #6396 is
   tracking.
2. **E. coli AhpF is reviewed.** Current GOA had already migrated AhpF
   to GO:0102039; the review modifies that row to GO:0047134 for AhpF's
   direct reductase activity while retaining GO:0102039 as a contributed
   system-level activity.
3. **Follow with P. aeruginosa PA3529** (Q9HY81). The UniProt entry
   still exposes only the ordered locus name, so use `PA3529` unless
   `just fetch-gene PSEAE PA3529` resolves to a better symbol.
4. **Complete the E. coli `AhpC`/`AhpF` pair** by reviewing the cognate
   `ahpC` subunit ([#4032](https://github.com/ai4curation/ai-gene-review/issues/4032)).
   GO:0009321 (alkyl hydroperoxide reductase complex,
   CC) is intact and remains the correct CC for the `AhpC`/`AhpF`
   holocomplex; the new `bacterial_alkyl_hydroperoxide_reductase`
   module deliberately records `AhpC` as a knowledge gap until that
   review exists.
5. **Defer IBA-propagation review** for PTHR10681 until the next GOA
   release reflects the obsoletion; the upstream issue lists no IBA
   migration as required, so this is opportunistic.

## Priority

**Low.** Only 2 direct annotations were affected and the ontology
change is already in production. The opportunity here is extending
bacterial redox-enzyme coverage: AhpF now has a local review/module,
PA3529 is still unreviewed, and completing E. coli `ahpC` would close
the half-module boundary left by the AhpF pass.

## Status

- 2026-05-12 — Project file created. Upstream annotation issue
  #6396 still open (no comments). Ontology obsoletion PR
  geneontology/go-ontology#32015 already merged. No gene reviews
  started in this repo.
- 2026-10-02 — Started the E. coli AhpF follow-on review from current GOA.
  `just fetch-gene ECOLI AhpF` seeded 20 annotations for UniProtKB:P35340; the
  live GOA pull has already migrated AhpF from obsolete GO:0008785 to
  GO:0102039. Added a concrete `bacterial_alkyl_hydroperoxide_reductase` module
  for the `AhpF` NADH-to-`AhpC` electron-transfer reaction. The review keeps
  GO:0102039 as the whole-system peroxidase activity that AhpF contributes to,
  but scopes AhpF's own molecular function to GO:0047134
  *protein-disulfide reductase [NAD(P)H] activity*.
- 2026-10-04 — Project audit verified the ECOLI AhpF and PSEPK ahpC reviews,
  confirmed that PA3529/Q9HY81 is the remaining PSEAE direct-annotation gap
  tracked by [#514](https://github.com/ai4curation/ai-gene-review/issues/514),
  opened [#4032](https://github.com/ai4curation/ai-gene-review/issues/4032)
  for the ECOLI `ahpC` module gap, and refreshed this page/deck now that the
  AhpF follow-on is no longer just queued.
