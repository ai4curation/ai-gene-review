---
title: "Substrate Localization to Autophagosome (GO:0061753) — Obsoletion & Transfer"
maturity: SCOPING
tags: [OBSOLETION]
species:
  - human
  - mouse
genes:
  - TOM1
  - IRGQ
  - SMURF1
  - STBD1
  - GABARAPL1
  - RETREG2
---

# Substrate Localization to Autophagosome (GO:0061753) — Obsoletion & Transfer

## Overview

A GO obsoletion proposal will retire the biological-process term
**GO:0061753 substrate localization to autophagosome** — *"The localization
process by which an autophagic substrate is delivered to a forming
autophagosome."*

The ontology ticket is labelled `MF_in_BP`: the term describes what an
autophagy cargo receptor/adaptor *does* (a binding activity, now covered by
**GO:0160247 autophagy cargo adaptor activity**), not a distinct biological
process. There is no single replacement BP. Instead each annotation must be
transferred to the **specific selective-autophagy process** that the cited
paper actually supports (glycophagy, mitophagy, aggrephagy, xenophagy,
autophagosome-lysosome fusion, …), which makes this a per-annotation curation
job rather than a mechanical relabel.

Unlike most obsoletion trackers in this repo, **one affected review already
exists here** — `genes/human/RETREG2` carries a GO:0061753 row *and* uses the
term in `core_functions`, where term ids are strictly validated. That review
breaks the moment the obsoletion lands.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6497](https://github.com/geneontology/go-annotation/issues/6497)
  — *"Review annotations to GO:0061753 substrate localization to autophagosome"*
- Ontology ticket: [geneontology/go-ontology#32304](https://github.com/geneontology/go-ontology/issues/32304)
  — *"Obsoletion request: GO:0061753 substrate localization to autophagosome"*
  (OPEN, labels: `obsoletion`, `ready`, `MF_in_BP`, `vesicle-mediated-transport`)
- MF adaptor re-parenting: [geneontology/go-ontology#31866](https://github.com/geneontology/go-ontology/issues/31866)
  — *"Migrate terms under protein membrane adaptor to correct parent"* (**CLOSED**)

**Replacement-term status.** No new term needs minting. Every proposed
destination already exists and resolves in OLS (verified 2026-08-08):

| GO id | Label | Aspect |
|---|---|---|
| GO:0061753 | substrate localization to autophagosome (**to be obsoleted**; still active) | BP |
| GO:0061723 | glycophagy | BP |
| GO:0061909 | autophagosome-lysosome fusion | BP |
| GO:0061734 | type 2 mitophagy | BP |
| GO:0098792 | xenophagy | BP |
| GO:0035973 | aggrephagy | BP |
| GO:0016236 | macroautophagy | BP |
| GO:0006515 | protein quality control for misfolded or incompletely synthesized proteins | BP |
| GO:0160247 | autophagy cargo adaptor activity | MF |
| GO:0140580 | mitochondrion autophagosome adaptor activity | MF |
| GO:0140506 | endoplasmic reticulum-autophagosome adaptor activity | MF |
| GO:0038024 | cargo receptor activity | MF |
| GO:0043495 | protein-membrane adaptor activity | MF |
| GO:0030674 | protein-macromolecule adaptor activity | MF |

## Affected annotations (independently verified via QuickGO, 2026-08-08)

All UniProt accessions below were confirmed against the UniProt REST API; the
annotation rows were pulled from QuickGO directly rather than taken from the
upstream issue text.

### (A) Direct experimental annotations to GO:0061753

| Gene product | Species | UniProt | Ev | Reference | Extension | Upstream recommendation |
|---|---|---|---|---|---|---|
| **TOM1** | human | O60784 | IMP | PMID:23023224 | — | → **GO:0061909** autophagosome-lysosome fusion (± **GO:0035973** aggrephagy) |
| **Stbd1** | mouse | Q8C7E7 | IMP | PMID:20810658 | `part_of(GO:0061723)` | → **GO:0061723** glycophagy; drop now-redundant extension |
| **Stbd1** | mouse | Q8C7E7 | IMP | PMID:27358407 | — | → **GO:0061723** glycophagy |
| **IRGQ** | human | Q8WZA9 | IDA | PMID:39481378 | — | → **GO:0006515** + **GO:0016236** (no MHC-I-selective-autophagy term exists) |
| **SMURF1** | human | Q9HCE7 | IMP | PMID:22020285 | `has_target_start_location(GO:0005739)`, `part_of(GO:0061734)` | → **GO:0061734** type 2 mitophagy, plus **GO:0098792** xenophagy from the same paper |

### (B) Experimental MF annotations carrying GO:0061753 in an extension

| Gene product | Species | UniProt | MF term | Ev | Reference | Recommendation |
|---|---|---|---|---|---|---|
| **Stbd1** | mouse | Q8C7E7 | GO:0038024 | IDA | PMID:20810658 | drop `part_of(GO:0061753)`; keep `part_of(GO:0061723)` |
| **Stbd1** | mouse | Q8C7E7 | GO:0038024 | IMP | PMID:27358407 | swap `part_of(GO:0061753)` → `part_of(GO:0061723)` |
| **Gabarapl1** | mouse | Q8R3R8 | GO:0043495 | **ISO** | PMID:21893048 | swap `part_of(GO:0061753)` → `part_of(GO:0061723)` |
| **IRGQ** | human | Q8WZA9 | GO:0030674 | IDA | PMID:39481378 | drop `part_of(GO:0061753)`; `part_of(GO:0006515)` already present |
| **IRGQ** | human | Q8WZA9 | GO:0030674 | IDA | PMID:39481378 | as above (differs only in `has_input`) |

### Two corrections to the upstream issue table

Worth flagging back to go-annotation#6497 before curators act on it:

1. **Gabarapl1 Q8R3R8 also has a *direct* GO:0061753 annotation** (`involved_in`,
   **ISO**, PMID:21893048, assigned by MGI) that the issue's section (A) does not
   list — it only appears there as an MF-extension row. It needs a transfer
   decision too (presumably `GO:0061723` glycophagy, matching the same paper).
2. The Gabarapl1 MF row is **ISO assigned by MGI**, not an experimental
   GO Central annotation; the issue's "Impacted groups" table attributes it to
   "GO Central / mouse".

### (C) Inferred rows that follow automatically

Ten further manual-but-non-experimental rows (ISS `GO_REF:0000024`, ISO
`GO_REF:0000119` / `GO_REF:0000121`) exist on orthologs and will follow the
experimental transfers: rat `Smurf1` (A0A0G2K612), rat `Irgq` (A0A8I5ZUT2),
rat `Tom1` (A0ACM8Q5W0), rat `Stbd1` (Q5FVN1), chicken `TOM1` (O12940), mouse
`Tom1` (O88746, ISS + ISO), mouse `Irgq` (Q8VIM9, ISS + ISO), mouse `Smurf1`
(Q9CUN6, ISO). Thousands of IEA rows (`GO_REF:0000107` Ensembl,
`GO_REF:0000108` GOC inter-ontology) propagate automatically and are out of
scope, per the upstream issue.

## Impact on this repo

### Tier 1 — an existing review goes stale

**`genes/human/RETREG2/RETREG2-ai-review.yaml`** is the only review in the repo
touching GO:0061753, and it is affected twice:

- an `existing_annotations` row — GO:0061753, **IEA**, `GO_REF:0000108`,
  `involved_in`, currently `action: ACCEPT`;
- a `core_functions[].directly_involved_in` entry listing GO:0061753 alongside
  GO:0061709 reticulophagy.

The `core_functions` occurrence is the hard problem: per CLAUDE.md, GOA-sourced
`existing_annotations[].term.id` values are *not* hard-validated, but
`core_functions` term ids **are**. Once GO:0061753 is obsoleted,
`just validate human RETREG2` should be expected to flag the `core_functions`
entry. The fix is straightforward on the biology — RETREG2/FAM134A is an ER-phagy
receptor, so the reticulophagy BP (GO:0061709, already present) plus the MF
**GO:0140506 endoplasmic reticulum-autophagosome adaptor activity** (also already
on that review) carry the content; the GO:0061753 entry is redundant rather than
wrong and should simply be dropped.

### Tier 2 — related MF adaptor annotations, no action expected

The upstream issue notes that MF adaptor classes under GO:0160247 need
re-parenting; that work is go-ontology#31866, which is **already closed**. Repo
reviews carrying those MF terms should be spot-checked once the obsoletion lands
but are not expected to change:

- **GO:0140580** mitochondrion autophagosome adaptor activity —
  `worm/fndc-1`, `worm/phb-2`, `worm/dct-1`, `human/BCL2L13`
- **GO:0140506** ER-autophagosome adaptor activity — `human/RETREG2`
- **GO:0160247** autophagy cargo adaptor activity — `worm/sqst-1`,
  `SOLTU/JOKA2`, `human/CCDC50`, `human/NBR1`, `human/NUFIP1`, `human/NCOA4`,
  `human/TRIM5`, `human/TRIM17`, `human/CALCOCO1`, `human/CALCOCO2`,
  `human/TAX1BP1`

### Tier 3 — destination terms already used here

Reviews already annotating the transfer destinations give useful precedent for
how these BPs are used in this repo: **GO:0061723 glycophagy** —
`human/GAA` (two rows, both `KEEP_AS_NON_CORE`), `human/ATG2A`, `human/ATG2B`,
`SCHPO/atg2`, `worm/atg-18`. `human/GAA` is directly relevant: PMID:27358407
(the Stbd1/GAA double-knockout paper behind transfer A3) is the same
experimental system.

**None of the five directly affected gene products has a review in this repo**
(`genes/human/TOM1`, `genes/human/IRGQ`, `genes/human/SMURF1`,
`genes/mouse/Stbd1`, `genes/mouse/Gabarapl1` all absent).

## Scope

- **Organisms**: human (TOM1, IRGQ, SMURF1), mouse (Stbd1, Gabarapl1); rat and
  chicken ISS/ISO rows mirror these.
- **GO branch**: BP obsoletion with **no single replacement**. The content
  splits between an existing MF (GO:0160247 and its children) and
  cargo-specific selective-autophagy BPs. Each annotation therefore needs an
  individual, evidence-grounded destination.
- **Type of fix**: `MODIFY` in this repo's vocabulary — the essence of each
  annotation is sound, the term is wrong.
- **Known gap**: the IRGQ case has no adequate GO term. MHC-I quality-control
  autophagy is not represented; the upstream issue suggests a new-term request.
  This is the most interesting curation question in the set.

## Candidate genes for initial review

Confirm accessions with `just fetch-gene <organism> <gene>` before starting.

### Tier 1 — refresh required

1. **RETREG2** (human, UniProt Q8NC44) — `genes/human/RETREG2/`. Already
   reviewed; both the GO:0061753 `existing_annotations` row and the
   `core_functions` entry need revisiting. Highest priority: an existing review
   goes stale, and `core_functions` validation is strict.

### Tier 2 — directly affected, not yet in repo

2. **STBD1** (mouse Q8C7E7; human ortholog **O95210**) — the cleanest case: two
   independent IMP papers, an unambiguous destination (GO:0061723 glycophagy),
   and an MF cargo-receptor annotation whose extension needs the same swap.
   Pairs naturally with the existing `human/GAA` review.
3. **IRGQ** (human Q8WZA9) — the hard case. PMID:39481378 shows IRGQ routing
   misfolded MHC-I to lysosomal degradation via GABARAPL2/LC3B. No suitable
   selective-autophagy child exists, so this is a genuine
   `proposed_new_terms` opportunity rather than a transfer.
4. **SMURF1** (human Q9HCE7) — PMID:22020285 supports *two* destinations from
   one paper (GO:0061734 type 2 mitophagy and GO:0098792 xenophagy); a good test
   of one-annotation-splits-into-two.
5. **TOM1** (human O60784) — PMID:23023224; the recommendation moves the
   annotation from a cargo-sequestration BP to a *fusion* BP (GO:0061909), a
   different step of the pathway. Worth checking whether the myosin VI/TOM1
   evidence really supports fusion rather than delivery.
6. **GABARAPL1** (mouse Q8R3R8; human ortholog **Q9H0R8**) — an ATG8-family
   protein annotated as a `GO:0043495` adaptor. Both its direct ISO row and its
   MF extension point at GO:0061753. Lower priority (ISO, not experimental) but
   it is the only ATG8-family member in the affected set.

## Proposed approach

1. **Wait for the obsoletion to land.** As of 2026-08-08 GO:0061753 is still
   active in OLS (`is_obsolete: false`), though go-ontology#32304 is labelled
   `ready`, so this could move soon.
2. **Refresh RETREG2 first**, ideally *before* the obsoletion, since the fix
   (dropping a redundant `core_functions` entry) does not depend on the final
   destination chosen upstream. Regenerate with
   `just fetch-gene human RETREG2`, re-review the GO:0061753 row, then
   `just validate human RETREG2`.
3. **Then STBD1** as the clean transfer case, cross-checking against the
   existing `human/GAA` review.
4. **Then IRGQ**, and use it to draft a `proposed_new_terms` entry for MHC-I
   quality-control autophagy — the concrete deliverable this project can send
   back upstream.
5. **Then SMURF1 and TOM1**; **GABARAPL1** last.
6. **Report the two table corrections** (missing direct Gabarapl1 row; its ISO/MGI
   provenance) back to go-annotation#6497.
7. **Cross-reference** the sibling obsoletion trackers in this repo — the
   [ER exit site](ER_EXIT_SITE_LOCALIZATION_OBSOLETION.md),
   [vesicle targeting](VESICLE_TARGETING_OBSOLETION.md) and
   [synaptic vesicle docking](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md) pages —
   which share the same `MF_in_BP` "this BP is really a molecular function"
   rationale.

## Priority

**Medium.** Only five experimental annotations are in play and none of those
gene products is reviewed here yet, so the immediate blast radius is small. It
ranks above the pure queueing trackers because (a) `RETREG2` is an existing
review that breaks on obsoletion, in the strictly-validated `core_functions`
slot, and (b) the IRGQ term gap is an actionable new-term contribution.
Nothing is broken until the obsoletion is applied.

## Status

- **2026-08-08** — Project file created. Tracking
  [go-annotation#6497](https://github.com/geneontology/go-annotation/issues/6497)
  (opened 2026-08-08) and
  [go-ontology#32304](https://github.com/geneontology/go-ontology/issues/32304)
  (OPEN, labelled `ready`). Obsoletion **not yet applied**; GO:0061753 still
  active in OLS. All five direct experimental annotations, all five MF-extension
  rows, and ten downstream ISS/ISO rows independently verified against QuickGO;
  all UniProt accessions verified against the UniProt REST API; all fourteen GO
  ids verified in OLS. Two discrepancies found in the upstream table (see above).
  Repo impact: `human/RETREG2` only. No gene reviews started or refreshed yet.
