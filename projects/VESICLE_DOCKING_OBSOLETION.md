# Vesicle Docking BP Subtree — Obsoletion & MF Refactor (GO:0048278)

## Overview

A GO obsoletion proposal will retire the entire **`GO:0048278 vesicle docking`
biological-process subtree** plus its regulation terms, and redirect the
biology to two molecular-function terms:

- **GO:0160321 vesicle docking activity** (proposed MF; placeholder — not yet
  resolvable in OLS as of 2026-05-23) for the literal docking step, and
- a **proposed "vesicle tethering activity" MF** for the upstream tethering
  step. This MF is not yet minted in GO (a prospective placeholder
  `GO:7770062 vesicle membrane tethering activity` returned 404 from the GO
  API as of 2026-05-02; see `genes/human/TMF1/TMF1-notes.md:58`). Note that
  the existing **GO:0099023 vesicle tethering complex** is a cellular-component
  term, not the MF — it must not be reused as the MF replacement.

The rationale is the same as the parallel
[ER-PM](ER_PM_TETHERING_OBSOLETION.md),
[mito-ER](MITO_ER_TETHERING_OBSOLETION.md),
[ciliary basal-body](CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md), and
[synaptic vesicle docking](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md)
trackers in this repo: the docking step is best represented as a *binding
activity* (MF) rather than a *process* (BP).

This project is the **parent tracker** for the upstream
[geneontology/go-annotation#6379](https://github.com/geneontology/go-annotation/issues/6379)
annotation-review issue, which covers the whole BP subtree. The
[`SYNAPTIC_VESICLE_DOCKING_OBSOLETION`](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md)
tracker handles one sibling sub-issue (#6415, GO:0099148); a parallel
[`go-annotation#6375`](https://github.com/geneontology/go-annotation/issues/6375)
covers the related vesicle-tethering obsoletions and is **not yet tracked
here** (see "Related obsoletions" below).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6379](https://github.com/geneontology/go-annotation/issues/6379)
  — *"Review annotations to GO:0048278 vesicle docking, descendants and
  regulation terms"*
- Ontology ticket: [geneontology/go-ontology#31880](https://github.com/geneontology/go-ontology/issues/31880)
- Annotation review spreadsheet (not machine-accessible):
  `https://docs.google.com/spreadsheets/d/1ylWgI-uS6OuSff_3A6T8g9XQyfoNnBGZJfT7xnWpNOk`

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement (consider) |
|---|---|---|
| vesicle docking | GO:0048278 | MF: GO:0160321 vesicle docking activity (placeholder) |
| Golgi vesicle docking | GO:0048211 | MF: GO:0160321 |
| phagosome-lysosome docking | GO:0090384 | MF: GO:0160321 |
| regulation of vesicle docking | GO:0106020 | (likely retained regulatory BP) |
| positive regulation of vesicle docking | GO:0106022 | (likely retained regulatory BP) |
| negative regulation of vesicle docking | GO:0106021 | (likely retained regulatory BP) |
| vesicle docking involved in exocytosis | GO:0006904 | MF: GO:0160321 |
| synaptic vesicle docking | GO:0016081 | MF: GO:0160321 (docking) or the proposed "vesicle tethering activity" MF (not yet minted; see Overview) |
| dense core granule docking | GO:0061790 | MF: GO:0160321 |

OLS check (2026-05-23): all nine BP terms are still active. The replacement
MF **GO:0160321** is not yet resolvable in OLS — this is the same placeholder
state noted in the sibling synaptic-docking and ciliary-docking trackers, so
the obsoletion has not landed yet.

### Affected upstream groups (from issue body)

| Group | Annotations | Status (per upstream) |
|---|---:|---|
| ComplexPortal | 52 | pending |
| SGD | 15 | pending |
| UniProt | 12 | pending |
| SynGO | 10 | pending (8 sit under GO:0099148 — see sibling tracker) |
| FlyBase | 8 | DONE |
| MGI | 7 | DONE |
| RGD | 7 | DONE |
| BHF-UCL | 5 | done |
| PINC | 4 | pending |
| ParkinsonsUK-UCL | 4 | done |
| SynGO-UCL | 2 | done |
| HGNC-UCL | 1 | done |
| dictyBase | 1 | pending |
| WB | 1 | pending |
| DisProt | 1 | pending |

No InterPro2GO / UniProt-Keyword / UniRule mappings to the obsoleted terms
were listed in the upstream issue body.

## Impact on this repo

Direct overlap with existing reviews is **small** — most of the affected
genes (syntaxins, SNAREs, RABs, exocyst, Munc18/STXBP, tomosyn, septins,
TRAPP/COG/GARP subunits, etc.) are not yet covered here.

Verified by greppings `genes/*/*/*-goa.tsv` and `*-ai-review.yaml` for the
nine obsoleted IDs:

| Gene | Organism | File | Affected row |
|---|---|---|---|
| **USO1** | human | `genes/human/USO1/USO1-ai-review.yaml` | GO:0048211 Golgi vesicle docking, IBA from `PANTHER:PTN000000707` / `SGD:S000002216`, currently `action: ACCEPT` |

Also tracked under the sibling project
[`SYNAPTIC_VESICLE_DOCKING_OBSOLETION`](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md):

| Gene | Organism | Affected row |
|---|---|---|
| Camk2a | mouse | two GO:0099148 rows currently `ACCEPT` (see that tracker) |

The **USO1** annotation will need a refresh when the obsoletion lands. USO1
(p115) is a *bona fide* Golgi vesicle tether/docking factor, so this is one
of the cleaner candidates for a legitimate transfer onto the new
docking-activity MF — in contrast to e.g. CaMKIIα, which only *regulates*
docking. The current review text already notes that "the essential function
is SNARE assembly rather than tethering per se", so the refresh should
revisit whether the new MF (GO:0160321 vesicle docking activity) or the
proposed (not-yet-minted) "vesicle tethering activity" MF is the better fit.
(Note: GO:0099023 vesicle tethering complex is a CC term, not the
tethering-activity MF, and must not be used as the MF replacement here.)

## Scope

- **Organisms**: broadly cross-kingdom — yeast (SGD 15), human/rodent
  (BHF-UCL, ParkinsonsUK-UCL, HGNC-UCL, MGI, RGD, SynGO, PINC), invertebrate
  models (FlyBase, WB), Dictyostelium (dictyBase). UniProt and ComplexPortal
  contribute the bulk of pending rows.
- **GO branch**: a **BP→MF refactor**, not a within-branch swap. The
  `regulation of …` BP terms (GO:0106020, GO:0106021, GO:0106022, GO:0099148)
  are *not* expected to be cleanly transferable onto a binding-activity MF —
  expect per-gene `MODIFY` decisions distinguishing "performs docking" (→
  new MF) from "regulates docking" (→ a retained regulatory BP).
- **Type of fix**: structural ontology change; per-gene curator judgment is
  required for any gene that was annotated to a regulatory term.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` and confirm UniProt
accessions before starting.

### Tier 1 — refresh required (already in repo)

1. **USO1** (human, UniProt **O60763**) — `genes/human/USO1/`. The
   GO:0048211 IBA row is currently `ACCEPT`; refresh once the obsoletion
   lands. Likely a clean transfer to **GO:0160321 vesicle docking activity**
   or the **proposed "vesicle tethering activity" MF** (not yet minted; see
   Overview — *not* GO:0099023, which is the CC "vesicle tethering complex").
   p115 is the canonical Golgi tether — see existing notes mentioning
   GM130/giantin interactions and SNARE-assembly function.
2. **Camk2a** (mouse, UniProt **P11798**) — covered by sibling tracker
   [`SYNAPTIC_VESICLE_DOCKING_OBSOLETION`](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md);
   listed here only for completeness because it sits under the same
   #6379 umbrella.

### Tier 2 — clean new reviews for canonical docking factors

These are well-known docking/tethering proteins absent from the repo. Each
should be a relatively self-contained review (SNARE/tether biology is
well-characterised) and they collectively populate the new MF terms with
high-quality experimental anchors.

3. **STX1A** (human, UniProt **Q16623**) — syntaxin-1A; SNARE-complex
   component, classic synaptic vesicle docking factor.
4. **STXBP1** (human, UniProt **P61764**) — Munc18-1; binds STX1A and is a
   primary docking/priming factor at synapses. Disease-relevant (epileptic
   encephalopathy) → high curation value.
5. **EXOC4 / Sec8** (human, UniProt **Q96A65**) — exocyst component; the
   `GO:0090522 vesicle tethering involved in exocytosis` annotation is
   already flagged in the sibling tethering obsoletion #6375 (InterPro2GO
   mapping IPR039682 → GO:0090522).
6. **EXOC6 / Sec15** (human, UniProt **Q8TAG9**) — exocyst component; same
   #6375 InterPro2GO route (IPR007225 → GO:0090522).
7. **SEC18 / NSF** (human NSF, UniProt **P46459**) — ATPase that disassembles
   SNARE complexes after docking/fusion; a frequent annotation target for
   vesicle-fusion and docking terms.

### Tier 3 — yeast / Dictyostelium / fly cross-organism cases

8. **Uso1** (yeast, UniProt **P25386**, SGD `YDL058W`) — yeast ortholog of
   human USO1; sits in the SGD "15 pending" bucket and provides a clean
   cross-organism comparison against Tier 1 (#1).
9. **Sec1** (yeast, UniProt **P30619**) — Munc18 family / STXBP1 ortholog;
   docking factor at the plasma membrane.
10. **tom-1** (C. elegans, UniProt **A0A0K3ATN9**) — tomosyn; already listed
    under the sibling synaptic-docking tracker as the canonical negative
    regulator (`MODIFY` test case).

## Proposed approach

1. **Wait for the obsoletion to land.** The replacement MF **GO:0160321** is
   not yet minted (OLS check 2026-05-23). The ontology ticket
   [#31880](https://github.com/geneontology/go-ontology/issues/31880) is
   open and shared with the synaptic-docking and ciliary-docking trackers.
2. **Refresh `USO1` first** (Tier 1). p115 is the textbook Golgi vesicle
   tether/docking factor, so this is the cleanest test of "BP → new docking
   MF" transferability and most likely to be a straightforward `MODIFY`
   onto the new MF.
3. **Coordinate with the sibling tracker
   [`SYNAPTIC_VESICLE_DOCKING_OBSOLETION`](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md)**
   for Camk2a, Septin5, tom-1 — those genes belong to the same umbrella
   obsoletion (#6379) but are scoped under #6415 there to avoid duplicated
   work.
4. **Then queue Tier 2** (STX1A, STXBP1, EXOC4, EXOC6, NSF) as new reviews.
   STX1A + STXBP1 in particular pair with the existing Tier 1 USO1 review
   to populate the new MFs across both the Golgi-tether and the
   plasma-membrane-SNARE arms of the literature.
5. **Re-validate each affected review** with
   `just validate <organism> <gene>` after editing.

## Related obsoletions

The vesicle docking obsoletion in #6379 is part of a coordinated cluster of
"BP-tether/docking → MF binding activity" obsoletions. The other items in
the cluster:

- **[go-annotation#6375 vesicle tethering and children](https://github.com/geneontology/go-annotation/issues/6375)**
  — sibling obsoletion (GO:0099022 vesicle tethering and 4 children).
  **Not yet tracked here** as a separate project — would naturally pair
  with this one given how often the same gene gets both a tethering and a
  docking annotation. Recommend a follow-up project file if a maintainer
  picks it up.
- [`CILIARY_BASAL_BODY_DOCKING_OBSOLETION`](CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md)
  — sibling obsoletion (GO:0097711, #6405).
- [`SYNAPTIC_VESICLE_DOCKING_OBSOLETION`](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md)
  — sub-issue of this one (#6415, GO:0099148).
- [`ER_PM_TETHERING_OBSOLETION`](ER_PM_TETHERING_OBSOLETION.md) — sibling
  tether obsoletion (GO:0061817, #6383).
- [`MITO_ER_TETHERING_OBSOLETION`](MITO_ER_TETHERING_OBSOLETION.md) —
  sibling tether obsoletion (GO:1990456, #6397).

## Priority

**Medium.** Higher than purely-queueing obsoletion trackers because one
existing repo review (`USO1`) goes stale on obsoletion. Lower than
`SYNAPTIC_VESICLE_DOCKING_OBSOLETION` because USO1 is likely a clean
`MODIFY` onto the new MF (USO1 / p115 *is* a docking/tether factor),
whereas CaMKIIα is a regulator and forces a harder per-gene judgment.

## Status

- 2026-05-23 — Project file created. Tracking upstream
  [go-annotation#6379](https://github.com/geneontology/go-annotation/issues/6379)
  (last active 2026-05-12) and
  [go-ontology#31880](https://github.com/geneontology/go-ontology/issues/31880)
  (open). Obsoletion **not yet applied**; all nine BP terms still active in
  OLS; replacement MF **GO:0160321** not yet minted. Affected existing
  reviews: USO1 (human, in repo — needs refresh once obsoletion lands).
  No gene reviews started or refreshed yet under this tracker.
