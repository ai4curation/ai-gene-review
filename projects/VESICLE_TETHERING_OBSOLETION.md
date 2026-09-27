---
title: "Vesicle Tethering BP Subtree — Obsoletion & MF Refactor (GO:0099022)"
maturity: IN_PROGRESS
tags: [OBSOLETION]
species: [human]
genes: [TMF1, TRAPPC1, TRAPPC3, TRAPPC4, TRAPPC5, TRAPPC8, TRAPPC11, TRAPPC12, TRAPPC13]
---

# Vesicle Tethering BP Subtree — Obsoletion & MF Refactor (GO:0099022)

**Bottom line:** Before a vesicle docks and fuses, a tether (a long
coiled-coil golgin or a multisubunit complex such as TRAPP, COG or the
exocyst) makes first contact and bridges it to the target membrane. GO
has obsoleted GO:0099022 *vesicle tethering* and four children because
tethering is a binding activity, and minted the MF GO:7770062 *vesicle
membrane tethering activity* in its place; the recommended pattern is
that MF with a `part_of` link to the transport process it serves. We
recorded the upstream plan, the InterPro and UniRule mappings already
removed, and the reviews in this repo that touch the terms. The
obsoletion has landed: OLS shows GO:0099022 and GO:0099041 obsolete and
GO:7770062 minted, so the "placeholder", "not yet minted" and "not yet applied" notes
below are out of date, and the "Impact on this repo" table predates and
omits the eight TRAPP reviews. Partly done: eight human TRAPP subunit reviews
(TRAPPC1, 3, 4, 5, 8, 11, 12, 13), written after this page, already
MODIFY their NAS row on the obsolete GO:0099022 to GO:0006888 *ER to
Golgi vesicle-mediated transport*. TMF1 is fixed in #3237 (merged): its
NEW MF row and core MF move from the stand-in GO:0060090 to GO:7770062,
the obsolete GO:0099041 NEW row and core BP are removed, and the
"vesicle tethering activity" `proposed_new_terms` entry is dropped now
that GO has minted it. The same PR moves USO1's docking row to
GO:7770062. The tether-subunit new reviews (Tier 2 onward) have not
started.

This is the tethering step of the vesicle refactor. The docking step is
tracked in [VESICLE_DOCKING_OBSOLETION](VESICLE_DOCKING_OBSOLETION.md)
(#6379) and its regulation sub-issue in
[SYNAPTIC_VESICLE_DOCKING_OBSOLETION](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md)
(#6415); the targeting terms that fold into transport processes are in
[VESICLE_TARGETING_OBSOLETION](VESICLE_TARGETING_OBSOLETION.md) (#6424).

## Overview

A GO obsoletion proposal will retire **`GO:0099022 vesicle tethering` and four
children** (BPs), redirecting the biology to a single molecular-function term:

- **GO:7770062 vesicle membrane tethering activity** (proposed MF; placeholder —
  not yet resolvable in OLS as of 2026-05-25; same state noted in the parallel
  vesicle-docking tracker).

The rationale matches the parallel
[vesicle docking](VESICLE_DOCKING_OBSOLETION.md),
[ER-PM tethering](ER_PM_TETHERING_OBSOLETION.md),
[mito-ER tethering](MITO_ER_TETHERING_OBSOLETION.md),
[ciliary basal-body docking](CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md), and
[synaptic vesicle docking](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md) trackers:
the tethering *step* is best represented as a *binding activity* (MF) rather
than a *process* (BP). Note that the existing **GO:0099023 vesicle tethering
complex** is a cellular-component term, not the MF — it must not be reused as
the MF replacement.

Per @ValWood on the upstream issue, the recommended post-obsoletion pattern is
the new MF in a `part_of` annotation extension to the relevant transport BP,
e.g. `GO:7770062 vesicle membrane tethering activity part_of GO:0006888
endoplasmic reticulum to Golgi vesicle-mediated transport`. Curators may also
fall back to existing or expanded "fusion" descendant BPs where they cover the
full tethering→docking→fusion pathway.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6375](https://github.com/geneontology/go-annotation/issues/6375)
  — *"Review annotations to GO:0099022 vesicle tethering and children"*
- Ontology tickets (from upstream body):
  - [geneontology/go-ontology#31868](https://github.com/geneontology/go-ontology/issues/31868)
  - [geneontology/go-ontology#31871](https://github.com/geneontology/go-ontology/issues/31871)
  - [geneontology/go-ontology#31872](https://github.com/geneontology/go-ontology/issues/31872)
  - [geneontology/go-ontology#31881](https://github.com/geneontology/go-ontology/issues/31881)
- Annotation review spreadsheet (not machine-accessible):
  `https://docs.google.com/spreadsheets/d/1PN2Z6gl1XhUsNHs3eJXpm8ZkQCJYtfPDj3ogLWxgAa8`

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement (consider) |
|---|---|---|
| vesicle tethering | GO:0099022 | MF: GO:7770062 vesicle membrane tethering activity (placeholder) |
| synaptic vesicle tethering involved in synaptic vesicle exocytosis | GO:0099069 | MF: GO:7770062 |
| vesicle tethering involved in exocytosis | GO:0090522 | MF: GO:7770062 |
| vesicle tethering to endoplasmic reticulum | GO:0099044 | MF: GO:7770062 |
| vesicle tethering to Golgi | GO:0099041 | MF: GO:7770062 |

OLS check (2026-05-25): all five BP terms are still **active** (not yet
obsoleted). The replacement MF **GO:7770062** is not yet resolvable in OLS —
the obsoletion has not landed yet.

### Affected upstream groups (from issue body, 2026-04-15)

| Group | Annotations | Status (per upstream) |
|---|---:|---|
| ComplexPortal | 95 | pending |
| UniProt | 11 | pending |
| PomBase | 8 | DONE |
| SGD | 6 | pending |
| FlyBase | 5 | DONE |
| UOS_MCB | 3 | pending |
| WB | 1 | DONE |
| MGI | 1 | DONE |

Mappings flagged by upstream for review (InterPro2GO / UniRule):

| Term | Source | Mapping |
|---|---|---|
| GO:0090522 | InterPro2GO | InterPro:IPR007225 Exocyst complex component EXOC6/Sec15 → GO:0090522 |
| GO:0090522 | InterPro2GO | InterPro:IPR039682 Exocyst complex component Sec8/EXOC4 → GO:0090522 |
| GO:0090522 | UniRule | UniRule:UR000459766 → GO:0090522 |
| GO:0090522 | UniRule | UniRule:UR001419783 → GO:0090522 |
| GO:0099041 | InterPro2GO | InterPro:IPR028280 Protein Njmu-R1 → GO:0099041 |

InterPro has already removed the GO:0090522 mappings from IPR007225, IPR039682
and the UniRule entries (per @sarach06's 2026-04-22 comment); the new GO term
will be added once minted.

## Impact on this repo

Two genes currently in the repo have annotation-level or core_function-level
references to the obsoleted terms:

| Gene | Organism | File | Affected row | Notes |
|---|---|---|---|---|
| **TMF1** | human | `genes/human/TMF1/TMF1-ai-review.yaml` | GO:0099041 NEW row; also in `core_functions` and `proposed_new_terms` (GO:0099022 / GO:7770062) | Fixed in #3237 (merged): NEW MF row and core MF GO:0060090 → GO:7770062; GO:0099041 NEW row, core BP and the `proposed_new_terms` entry removed. |
| **USO1** | human | `genes/human/USO1/USO1-ai-review.yaml` | No direct rows under the 5 obsoleted IDs; its GO:0048211 IBA row is tracked under [VESICLE_DOCKING_OBSOLETION](VESICLE_DOCKING_OBSOLETION.md) (#6379). | That row now MODIFYs to the tethering MF GO:7770062, fixed in #3237 (merged). |

Verified by `grep -r "GO:00990(22\|41\|44\|69)\|GO:0090522" genes/` across
`-goa.tsv` and `-ai-review.yaml` files.

**TMF1 was the highest-priority follow-up here; fixed in #3237 (merged).** The
paragraph records the original plan. Its review explicitly cites
this obsoletion plan and uses GO:0060090 *molecular adaptor activity* as a
stand-in for the not-yet-minted tether MF (see `TMF1-ai-review.yaml:600-668`).
Once GO:7770062 lands, TMF1 should be refreshed to (a) update the
`proposed_new_terms` entry to reference the minted MF, (b) replace or annotate
the GO:0099041 NAS row, and (c) reconsider whether GO:0060090 is still the
best stand-in MF for `core_functions`.

## Scope

- **Organisms**: predominantly human and yeast (ComplexPortal 95 + UniProt 11 +
  SGD 6 are the pending bulk), with smaller cross-kingdom tails (FlyBase, MGI,
  WB already done). Most ComplexPortal rows are macromolecular tethering
  complexes (TRAPPI/II/III, COG, exocyst, GARP, HOPS/CORVET, Dsl1, Golgin
  family) rather than individual genes.
- **GO branch**: a **BP→MF refactor**, not a within-branch swap. Annotations
  that meant "this protein *is* a tether/bridge" map cleanly onto
  GO:7770062 (likely `MODIFY`). Annotations that meant "this protein
  participates in a tethering-mediated transport event" should retain the
  upstream transport BP (GO:0006888 ER→Golgi, GO:0006891 intra-Golgi,
  GO:0006893 Golgi→PM, GO:0048278 vesicle docking, etc., the last of which is
  itself being obsoleted under [#6379](VESICLE_DOCKING_OBSOLETION.md) — so
  cross-check with that tracker) and add the MF in `part_of` extensions.
- **Type of fix**: structural ontology change; per-gene curator judgment is
  required to choose the correct upstream transport BP and to distinguish
  "performs tethering" from "regulates tethering".

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` and confirm UniProt
accessions before starting.

### Tier 1 — refresh required (already in repo)

1. **TMF1** (human, UniProt **P82094**) — `genes/human/TMF1/`. Direct
   GO:0099041 NAS row + `proposed_new_terms` already references GO:0099022 and
   GO:7770062. The single cleanest test case for transferring an existing
   review onto the new tether MF. Fixed in #3237 (merged): now on GO:7770062.

### Tier 2 — InterPro2GO–flagged tether subunits (high-priority new reviews)

These genes are *directly* implicated in the upstream issue's flagged mapping
table — they are the most defensible new reviews because the obsoletion
spreadsheet will name them explicitly.

2. **EXOC4 / Sec8** (human, UniProt **Q96A65**) — exocyst component. Flagged
   in #6375 via InterPro2GO mapping IPR039682 → GO:0090522. Also listed as a
   Tier 2 candidate in the sibling [VESICLE_DOCKING_OBSOLETION](VESICLE_DOCKING_OBSOLETION.md);
   pick *one* tracker to host the review when it is started.
3. **EXOC6 / Sec15** (human, UniProt **Q8TAG9**) — exocyst component. Flagged
   in #6375 via InterPro2GO mapping IPR007225 → GO:0090522.
4. **NJMU-R1 / RIPPLY3** family — flagged in #6375 via InterPro2GO mapping
   IPR028280 → GO:0099041. The InterPro family is small and rodent/human-only;
   pick a representative once UniProt accessions are checked. (Note: confirm
   the human gene symbol before fetch — the InterPro family name "Protein
   Njmu-R1" is older; current HGNC symbol is **RIPPLY3** if matched, but the
   identification needs verification at fetch time.)

### Tier 3 — canonical golgin / tether complex subunits

These are well-known tethers absent from the repo. They sit in the
ComplexPortal (95) and UniProt (11) buckets and would substantially populate
the new MF with high-quality experimental anchors.

5. **GMAP-210 / TRIP11** (human, UniProt **Q15643**) — golgin; tethers
   COPI-derived vesicles to the cis-Golgi via N-terminal amphipathic helix.
6. **Golgin-84 / GOLGA5** (human, UniProt **Q8TBA6**) — golgin tether for
   intra-Golgi transport vesicles; shares the N-terminal motif noted in
   TMF1-ai-review.yaml as conserved across golgin tethers.
7. **GORAB** (human, UniProt **Q5T7V8**) — GRIP-domain golgin tether involved
   in retrograde trafficking; disease-relevant (gerodermia osteodysplastica).
8. **RAB6A** (human, UniProt **P20340**) — recruits TMF1 and other golgin
   tethers via GTP-bound state; central upstream node for several of the
   genes above.

## Proposed approach

1. **Wait for the obsoletion to land.** The replacement MF **GO:7770062** is
   not yet minted (OLS check 2026-05-25). The cluster of ontology tickets
   (#31868, #31871, #31872, #31881) is open and shared with the wider
   tether/docking refactor.
2. **Refresh `TMF1` first** (Tier 1). It is the only existing review in this
   repo with a direct annotation to one of the five obsoleted terms, and the
   review's `proposed_new_terms` block already names this exact obsoletion
   plan — so a refresh will close the loop cleanly.
3. **Coordinate with sibling trackers**:
   - [VESICLE_DOCKING_OBSOLETION](VESICLE_DOCKING_OBSOLETION.md) (#6379) —
     EXOC4 is a shared Tier 2 candidate; pick one tracker to host the new
     review when started.
   - [ER_PM_TETHERING_OBSOLETION](ER_PM_TETHERING_OBSOLETION.md) (#6383),
     [MITO_ER_TETHERING_OBSOLETION](MITO_ER_TETHERING_OBSOLETION.md) (#6397),
     [CILIARY_BASAL_BODY_DOCKING_OBSOLETION](CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md) (#6405),
     [SYNAPTIC_VESICLE_DOCKING_OBSOLETION](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md) (#6415) —
     parallel BP→MF refactors; review-text wording should stay consistent
     across the cluster.
4. **Then queue Tier 2** (EXOC4, EXOC6, NJMU-R1/RIPPLY3) as new reviews —
   these are the genes upstream curators will inevitably touch when working
   through the InterPro2GO mapping fix.
5. **Re-validate each affected review** with
   `just validate <organism> <gene>` after editing.

## Related obsoletions

This is one item in a coordinated cluster of "BP-tether/docking → MF binding
activity" obsoletions. Cross-reference the parallel trackers:

- [VESICLE_DOCKING_OBSOLETION](VESICLE_DOCKING_OBSOLETION.md) — sibling
  obsoletion (GO:0048278 and BP children, #6379). Notes that #6375 is the
  parallel tether obsoletion; this project file is that parallel tracker.
- [SYNAPTIC_VESICLE_DOCKING_OBSOLETION](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md)
  — sub-issue of #6379 (#6415, GO:0099148).
- [CILIARY_BASAL_BODY_DOCKING_OBSOLETION](CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md)
  — sibling docking obsoletion (GO:0097711, #6405).
- [ER_PM_TETHERING_OBSOLETION](ER_PM_TETHERING_OBSOLETION.md) — sibling
  tether obsoletion (GO:0061817, #6383).
- [MITO_ER_TETHERING_OBSOLETION](MITO_ER_TETHERING_OBSOLETION.md) — sibling
  tether obsoletion (GO:1990456, #6397).

## Priority

**Medium.** Higher than purely-queueing obsoletion trackers because one
existing repo review (`TMF1`) explicitly references this obsoletion plan in
its `proposed_new_terms` and will need a follow-up edit once GO:7770062 is
minted. Lower than `SYNAPTIC_VESICLE_DOCKING_OBSOLETION` because the affected
existing-review count is small (1 vs 2+), and TMF1 is likely a clean `MODIFY`
onto the new MF (TMF1 *is* a Golgi vesicle tether), with no awkward
regulator-vs-effector judgment calls of the kind that complicate the docking
trackers.

## Status

- 2026-05-25 — Project file created. Tracking upstream
  [go-annotation#6375](https://github.com/geneontology/go-annotation/issues/6375)
  (last active 2026-04-23) and the four ontology tickets in the cluster.
  Obsoletion **not yet applied**; all five BP terms still active in OLS;
  replacement MF **GO:7770062** not yet minted. Affected existing reviews:
  **TMF1** (direct GO:0099041 row; review's `proposed_new_terms` already
  references GO:0099022 / GO:7770062). No gene reviews started or refreshed
  yet under this tracker.
- 2026-09-26 — TMF1 refresh fixed in #3237 (merged): NEW MF row and core
  MF GO:0060090 → GO:7770062 vesicle membrane tethering activity;
  obsolete GO:0099041 NEW row and core BP removed; `proposed_new_terms`
  entry removed because GO has minted the MF. USO1's GO:0048211 row
  also moves to GO:7770062 in the same PR. The TRAPPC1/3/4/5/8/11/12/13
  GO:0099022 rows already MODIFY to GO:0006888 and are unchanged. Tier 2
  new reviews not started, so maturity stays IN_PROGRESS.
- 2026-09-27 — #3237 merged, so the TMF1 and USO1 refreshes are on
  `main`. Tier 2 new reviews not started; maturity stays IN_PROGRESS.

## Slides

- [Slides](VESICLE_TETHERING_OBSOLETION/slides/VESICLE_TETHERING_OBSOLETION-slides.html) (Marp source: [VESICLE_TETHERING_OBSOLETION-slides.md](VESICLE_TETHERING_OBSOLETION/slides/VESICLE_TETHERING_OBSOLETION-slides.md)) — AI generated
