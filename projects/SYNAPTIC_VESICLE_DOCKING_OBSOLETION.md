# Regulation of Synaptic Vesicle Docking — Obsoletion & MF Refactor

## Overview

A GO obsoletion proposal will retire the vesicle-docking biological-process
hierarchy and replace it with a new **molecular function** term:

- **GO:0160321 vesicle docking activity** (proposed MF; placeholder ID — not
  yet minted, see "Replacement-term status" below), defined as *"the binding
  activity of a protein that directly mediates the stable attachment of a
  transport vesicle to a target membrane, bringing the two membranes into
  close apposition"*, proposed parent **GO:0140177 membrane-membrane adaptor
  activity**.

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

## Obsoletion plan (per upstream)

The full upstream proposal retires `GO:0048278 vesicle docking` plus its
descendants and the associated regulation terms, all redirected to the new MF
`GO:0160321 vesicle docking activity`:

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

Replacement (consider term): **GO:0160321 vesicle docking activity** (MF).

### Affected annotations to GO:0099148 (verified via QuickGO, 2026-05-16)

Experimental / curated rows (the SynGO "8 annotations"):

| Group | Gene | Species | UniProt | Reference | Evidence | In repo? |
|---|---|---|---|---|---|---|
| SynGO | **Camk2a** | M. musculus | **P11798** | PMID:17660813 | IMP + IDA (×2) | **YES — `genes/mouse/Camk2a`, both rows currently `ACCEPT`** |
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
(IMP and IDA, both `PMID:17660813`), each currently `action: ACCEPT`. Once the
obsoletion is applied these become annotations to an obsolete term and the
review must be refreshed.

The refresh is **not** a mechanical relabel. CaMKIIα is a Ser/Thr kinase that
*regulates* presynaptic vesicle docking; it is not itself a vesicle-docking
adaptor/tether, so transferring a `regulation of synaptic vesicle docking` BP
annotation onto the new `vesicle docking activity` **MF** is biologically
questionable for this gene. The likely correct outcome is `MODIFY` toward a
retained regulatory BP (or the synaptic-vesicle-cycle process) rather than a
literal docking-activity MF — exactly the curator-judgment question this repo
exists to evaluate. The existing `supporting_text` on those rows (*"Kinase
activity is not required for αCaMKII-dependent presynaptic plasticity at
CA3-CA1 synapses"*) is also only tangential to docking and should be revisited
against PMID:17660813.

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

1. **Camk2a** (mouse, UniProt **P11798**) — `genes/mouse/Camk2a/`. Two
   GO:0099148 rows currently `ACCEPT`; must be re-evaluated once the term is
   obsoleted. Highest priority because an existing review goes stale on
   obsoletion. Expect `MODIFY` (regulatory kinase, not a docking adaptor),
   not a clean transfer to the new MF.

### Tier 2 — direct SynGO experimental annotations, not yet in repo

2. **Septin5 / SEPTIN5** (mouse UniProt **Q9Z2Q6**; human ortholog
   **Q99719**) — presynaptic septin / CDCrel-1, syntaxin-1A interactor;
   strong SynGO experimental annotation from **PMID:20624595**. A genuine
   structural component of the docking/SNARE machinery, so this one *may*
   legitimately move to the new docking-activity MF — a good contrast case
   against Camk2a.
3. **tom-1** (C. elegans, UniProt **A0A0K3ATN9**) — tomosyn ortholog; classic
   negative regulator of synaptic-vesicle priming/docking
   (**PMID:16895441**). Tests the "regulator, not effector" reannotation
   pattern in an invertebrate model.

## Proposed approach

1. **Wait for the obsoletion to land.** As of 2026-05-16, GO:0099148 is still
   active in OLS (`is_obsolete: false`) and the replacement `GO:0160321` is
   not yet resolvable via OLS or the GO API (placeholder, like the
   `GO:7770065` placeholder in [#423](https://github.com/ai4curation/ai-gene-review/issues/423)).
   The ontology ticket #31880 is open.
2. **Refresh `Camk2a` first** once the obsoletion is applied: regenerate GOA
   (`just fetch-gene mouse Camk2a`), then re-review the two GO:0099148 rows —
   expect `MODIFY` away from a literal docking-activity MF toward a retained
   regulatory BP, with corrected `supporting_text`. Re-validate
   (`just validate mouse Camk2a`).
3. **Then queue `Septin5`** (mouse, with human SEPTIN5 follow-up) as a clean
   new review — the strongest candidate for a legitimate transfer to the new
   docking MF.
4. **Then `tom-1`** (C. elegans) to cover the invertebrate negative-regulator
   case.
5. **Cross-reference** the parallel docking/tethering obsoletions already
   tracked here — [`CILIARY_BASAL_BODY_DOCKING_OBSOLETION`](CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md)
   and the ER-PM / mito-ER tether trackers — since the new
   membrane-membrane-adaptor MF family is the common destination.

## Priority

**Medium.** Higher than the purely-queueing obsoletion trackers because an
existing repo review (`Camk2a`) goes stale the moment the obsoletion is
applied, and the BP→MF refactor makes the correct reannotation non-obvious.
Nothing is broken until the obsoletion lands, so no immediate action is
required.

## Status

- 2026-05-16 — Project file created. Tracking upstream
  [go-annotation#6415](https://github.com/geneontology/go-annotation/issues/6415)
  (last active 2026-05-15) and
  [go-ontology#31880](https://github.com/geneontology/go-ontology/issues/31880)
  (open). Obsoletion **not yet applied**; GO:0099148 still active and
  GO:0160321 not yet minted. Affected experimental annotations: Camk2a
  (mouse, in repo — needs refresh), Septin5 (mouse, not in repo), tom-1
  (C. elegans, not in repo). No gene reviews started or refreshed yet.
