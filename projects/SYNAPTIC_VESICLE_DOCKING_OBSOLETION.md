---
title: "Regulation of Synaptic Vesicle Docking — Obsoletion & MF Refactor"
maturity: IN_PROGRESS
last_reviewed: 2026-10-05
autolink_gene_symbols: false
tags: [OBSOLETION, FLAGSHIP]
species: [mouse, worm]
genes: [Camk2a]
manifest:
  slides:
    - href: SYNAPTIC_VESICLE_DOCKING_OBSOLETION/slides/SYNAPTIC_VESICLE_DOCKING_OBSOLETION-slides.html
---

# Regulation of Synaptic Vesicle Docking — Obsoletion & MF Refactor

**Bottom line:** Before a synaptic vesicle fuses, it docks at the active
zone, held there by specific binding proteins. GO has retired the whole
vesicle-docking process subtree and now represents docking as a
molecular function, GO:0160321 *vesicle docking activity*. This page
tracks one piece of that change: GO:0099148 *regulation of synaptic
vesicle docking*, flagged by SynGO (go-annotation#6415), whose
experimental annotations sit on three genes: mouse Camk2a, mouse
Septin5 and worm tom-1. We listed those rows and argued that most
should not become the new MF, because a kinase such as CaMKIIα
regulates docking without doing it. The obsoletion has now landed:
OLS shows GO:0099148 obsolete and GO:0160321 minted. The one affected
review is fixed in #3237 (merged): mouse Camk2a's GO:0099148 entries,
from PMID:17660813, move from ACCEPT to MODIFY → GO:0048172 *regulation of
short-term neuronal synaptic plasticity*, not the docking MF, because
the paper shows αCaMKII regulates the number of docked vesicles without
docking them. Septin5 and tom-1 still have no review here.

This is the regulation branch of the docking refactor. The parent
tracker [VESICLE_DOCKING_OBSOLETION](VESICLE_DOCKING_OBSOLETION.md)
covers the docking terms themselves (#6379), and
[VESICLE_TETHERING_OBSOLETION](VESICLE_TETHERING_OBSOLETION.md) covers
the earlier tethering step (#6375).

## Overview

GO has retired the vesicle-docking biological-process hierarchy and replaced
it with a **molecular function** term:

- **GO:0160321 vesicle docking activity** (MF), defined for the binding
  activity of a protein that directly mediates stable transport-vesicle
  attachment to a target membrane and brings the two membranes into close
  apposition, under **GO:0140177 membrane-membrane adaptor activity**.

The upstream ontology ticket scopes the obsoletion broadly across the whole
`GO:0048278 vesicle docking` BP subtree and its regulation terms. This project
tracks the annotation-review issue for one of those terms,
**GO:0099148 regulation of synaptic vesicle docking** (BP), flagged by the
SynGO group.

The rationale (per the ontology editors' checklist) is explicit: *"the reason
for obsoletion is that this term represents a molecular function."* The
docking step is the binding activity of a specific adaptor/tether protein, so
the curators are moving the representation from a BP process to an MF binding
activity.

This project differs from the other obsoletion trackers in this repo because
**one directly affected gene — mouse `Camk2a` — already has a review here**
(`genes/mouse/Camk2a/`), so this is both a *refresh-existing-review* and a
*queue-new-genes* tracker.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6415](https://github.com/geneontology/go-annotation/issues/6415)
- Ontology ticket: [geneontology/go-ontology#31880](https://github.com/geneontology/go-ontology/issues/31880)
  — *"New term request and Obsoletion request: GO:0048278 vesicle docking,
  descendants and regulation terms"*
- Annotation review spreadsheet (SynGO; not machine-accessible):
  `https://docs.google.com/spreadsheets/d/1oP8qDeDVhVD_43GcnN2_IQgWO4vPxVGAYPY-o_zWq1o`

## Upstream obsoletion outcome

The upstream obsoletion retired `GO:0048278 vesicle docking`, its descendants,
and the associated regulation terms. All are now obsolete; the literal docking
terms carry `consider` pointers to both **GO:0160321 vesicle docking activity**
and **GO:7770062 vesicle membrane tethering activity**, while the regulation
terms, including **GO:0099148 regulation of synaptic vesicle docking**, carry
`consider: GO:0160321`:

| Obsoleted term | ID |
|---|---|
| vesicle docking | GO:0048278 |
| synaptic vesicle docking | GO:0016081 |
| Golgi vesicle docking | GO:0048211 |
| phagosome-lysosome docking | GO:0090384 |
| vesicle docking involved in exocytosis | GO:0006904 |
| dense core granule docking | GO:0061790 |
| regulation of vesicle docking | GO:0106020 |
| positive regulation of vesicle docking | GO:0106022 |
| negative regulation of vesicle docking | GO:0106021 |
| **regulation of synaptic vesicle docking** (focus of #6415) | **GO:0099148** |

Focus term consider replacement: **GO:0160321 vesicle docking activity** (MF).

### Affected annotations to GO:0099148 (verified via QuickGO, 2026-05-16)

Experimental / curated rows (the SynGO "8 annotations"):

| Group | Gene | Species | UniProt | Reference | Evidence | In repo? |
|---|---|---|---|---|---|---|
| SynGO | **Camk2a** | M. musculus | **P11798** | PMID:17660813 | IMP + IDA (×2) | **YES — `genes/mouse/Camk2a`, fixed in #3237** |
| RGD | Camk2a | R. norvegicus | P11275 | GO_REF:0000121 | ISO | no |
| SynGO | **Septin5** | M. musculus | **Q9Z2Q6** | PMID:20624595 | IMP + IDA | no |
| RGD | Septin5 | R. norvegicus | Q9JJM9 | GO_REF:0000121 | ISO | no |
| SynGO | **tom-1** | C. elegans | **A0A0K3ATN9** | PMID:16895441 | IMP (×2) + IDA (×2) | no |

Plus ~60 `IEA` orthology rows (GO_REF:0000107, Ensembl / EnsemblMetazoa) on
CAMK2A orthologs across many species — these are electronic and will follow
the obsoletion automatically; no manual action needed.

No InterPro2GO / UniProt-Keyword / UniRule mappings to GO:0099148 were listed
in the upstream issue.

## Impact on this repo

**Mouse `Camk2a` is already reviewed here and is directly affected.**
`genes/mouse/Camk2a/Camk2a-ai-review.yaml` carries two GO:0099148 rows
(IMP and IDA, both `PMID:17660813`), each formerly `action: ACCEPT`. Both are
now `MODIFY` → GO:0048172 regulation of short-term neuronal synaptic
plasticity, fixed in #3237 (merged), which also replaced the supporting text
with the abstract's sentences on docked-vesicle number and short-term
presynaptic plasticity.

The refresh is **not** a mechanical relabel. CaMKIIα is a Ser/Thr kinase that
*regulates* presynaptic vesicle docking; it is not itself a vesicle-docking
adaptor/tether, so transferring a `regulation of synaptic vesicle docking` BP
annotation onto the new `vesicle docking activity` **MF** is biologically
questionable for this gene. The correct outcome was `MODIFY` toward a
retained regulatory BP rather than a literal docking-activity MF — exactly the
curator-judgment question this repo exists to evaluate.

`Septin5` and `tom-1` are **not** in the repo. The human Septin5 ortholog is
**SEPTIN5 / UniProt Q99719** (not yet reviewed; `genes/human/` has no SEPT/
SEPTIN entry).

## Scope

- **Organisms**: mouse (`Camk2a`, `Septin5`), C. elegans (`tom-1`); rat ISO
  rows mirror the mouse annotations; human `SEPTIN5` (Q99719) is the natural
  cross-organism follow-up.
- **GO branch**: a **BP→MF refactor**, not a within-branch terminological
  swap. A `regulation of …` BP annotation does not map 1:1 onto a binding-
  activity MF, so each affected gene needs an individual reannotation decision.
- **Type of fix**: structural ontology change. The substantive curation
  question per gene is whether the protein *performs* docking (→ new MF) or
  merely *regulates*/modulates it (→ keep a regulatory BP, `MODIFY`).

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` and confirm UniProt
accessions before starting.

### Tier 1 — refresh required (already in repo)

- **Camk2a** (mouse, UniProt **P11798**) — `genes/mouse/Camk2a/`. Its
   GO:0099148 entries were `ACCEPT`; now `MODIFY` → GO:0048172, fixed in
   #3237 (merged). The decision was `MODIFY` (regulatory kinase, not a
   docking adaptor), not a clean transfer to the new MF.

### Tier 2 — direct SynGO experimental annotations, not yet in repo

- **Septin5 / SEPTIN5** (mouse UniProt **Q9Z2Q6**; human ortholog
   **Q99719**) — presynaptic septin / CDCrel-1, syntaxin-1A interactor;
   strong SynGO experimental annotation from **PMID:20624595**. A genuine
   structural component of the docking/SNARE machinery, so this one *may*
   legitimately move to the new docking-activity MF — a good contrast case
   against Camk2a.
- **tom-1** (C. elegans, UniProt **A0A0K3ATN9**) — tomosyn ortholog; classic
   negative regulator of synaptic-vesicle priming/docking
   (**PMID:16895441**). Tests the "regulator, not effector" reannotation
   pattern in an invertebrate model.

## Proposed approach

1. **Record the upstream outcome.** GO:0099148 is obsolete and GO:0160321
   vesicle docking activity is live, so this page no longer depends on a
   placeholder MF term.
2. **Camk2a: done.** #3237 regenerated mouse Camk2a, moved the GO:0099148
   entries to GO:0048172, and corrected the PMID:17660813 support.
3. **Queue `Septin5`** (mouse, with human SEPTIN5 follow-up) as a clean
   new review — the strongest candidate for a legitimate transfer to the new
   docking MF.
4. **Then `tom-1`** (C. elegans) to cover the invertebrate negative-regulator
   case.
5. **Cross-reference** the parallel docking/tethering obsoletions already
   tracked here — [`CILIARY_BASAL_BODY_DOCKING_OBSOLETION`](CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md)
   and the ER-PM / mito-ER tether trackers — since the new
   membrane-membrane-adaptor MF family is the common destination.

## Priority

**Medium.** Higher than the purely queueing obsoletion trackers because an
existing repo review (`Camk2a`) did go stale when the obsoletion landed, and
the BP→MF refactor made the correct reannotation non-obvious. Camk2a is fixed
now; Septin5 and tom-1 are the remaining direct experimental cases.

## Status

- 2026-05-16 — Project file created. Tracking upstream
  [go-annotation#6415](https://github.com/geneontology/go-annotation/issues/6415)
  (last active 2026-05-15) and
  [go-ontology#31880](https://github.com/geneontology/go-ontology/issues/31880)
  (open). Obsoletion **not yet applied**; GO:0099148 still active and
  GO:0160321 not yet minted. Affected experimental annotations: Camk2a
  (mouse, in repo — needs refresh), Septin5 (mouse, not in repo), tom-1
  (C. elegans, not in repo). No gene reviews started or refreshed yet.
- 2026-09-26 — Camk2a refresh fixed in #3237 (merged): both GO:0099148
  rows (IMP, IDA; PMID:17660813) ACCEPT → MODIFY to GO:0048172
  regulation of short-term neuronal synaptic plasticity (regulator, not
  docker, as this page anticipated); supporting text now quotes the
  abstract. Septin5 and tom-1 reviews not started, so maturity stays
  SCOPING.
- 2026-09-27 — #3237 merged, so the Camk2a refresh is on `main`.
  Maturity moves to IN_PROGRESS: the one affected review is done and
  only the Septin5 and tom-1 new reviews remain.
- 2026-10-04 — Re-audited the repo after #3237: Camk2a validates with the
  obsolete GO:0099148 entries marked `MODIFY`, and no mouse Septin5, human
  SEPTIN5 or worm tom-1 review exists yet. Frontmatter now lists only Camk2a,
  the reviewed gene already tied to this tracker.
