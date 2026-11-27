---
title: "Hypochlorous Acid Metabolic Process Terms — Obsoletion"
maturity: IN_PROGRESS
last_reviewed: 2026-10-16
tags: [OBSOLETION]
species: [mouse]
genes: [Mpo]
manifest:
  slides:
    - href: HYPOCHLOROUS_ACID_OBSOLETION/slides/HYPOCHLOROUS_ACID_OBSOLETION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/TzdUqWUZ2PZqr9iAxh7GBe
      title: Project brief
---

# Hypochlorous Acid Metabolic Process Terms — Obsoletion

**Bottom line:** GO has obsoleted all three hypochlorous acid (HOCl)
process terms — the grouping term GO:0002148 first, then the biosynthetic
(GO:0002149) and catabolic (GO:0002150) terms — with the obsolete records
giving the reason "this BP term represents a MF term"; the originating ticket
(go-ontology#22891) had instead flagged the wrong `is_a` parent (see Overview).
The affected annotation was a single MGI IMP on mouse Mpo (PMID:10085024), plus
a rat ISO copy. **Both are already gone:** a fresh `just fetch-gene mouse Mpo`
returns 85 GOA rows (84 distinct annotations) with no GO:0002149, and QuickGO returns 65 rat Mpo rows
with none to GO:0002149, so the migration landed upstream and the rat row
followed the mouse one as predicted. Mouse **Mpo** is now fully reviewed here
(`genes/mouse/Mpo/`), which closes the deferred-review item and settles the MF
question: GO has **no** term for the myeloperoxidase reaction
(chloride + H2O2 + H+ = hypochlorous acid + H2O, EC 1.11.2.2, **RHEA:28218** —
*not* RHEA:43232, which is isatin hydrolase), and the review therefore accepts
GO:0004601 *peroxidase activity* — which carries "myeloperoxidase activity" as a
narrow synonym and the Reactome xref for MPO-dependent HOCl production — while
proposing a child term for the reaction itself (*hypochlorous acid synthase
activity*, named so as not to read as a child of GO:0016691). GO:0016691 is organic
chlorination and GO:0140825 is lactoperoxidase activity, as suspected.
Remaining work is upstream (create the MF term) or optional (a human MPO review).

## Overview

A GO obsoletion proposal targets three biological-process terms in the
hypochlorous acid (HOCl) branch:

- **GO:0002148 hypochlorous acid metabolic process** (BP, **already obsolete**)
- **GO:0002149 hypochlorous acid biosynthetic process** (BP, now obsolete in OLS)
- **GO:0002150 hypochlorous acid catabolic process** (BP, now obsolete in OLS)

The two rationales come from different stages. The originating ticket,
go-ontology#22891, argued that the original parentage
(`is_a` *organic acid metabolic process*, GO:0006082) is incorrect because
hypochlorous acid contains no carbon and so is not an organic acid. The
grouping-term obsoletion at the parent level (go-ontology#30524) removed
GO:0002148, which had no remaining annotations. GO has since obsoleted the
two child terms too; their obsolete definitions record a different final
reason, "The reason for obsoletion is that this BP term represents a MF
term" (QuickGO, GO:0002149/GO:0002150, rechecked 2026-10-16). The MGI mouse
Mpo row has since left GO:0002149 in the GOA download, and the rat ISO copy
with it, so the AI Gene Review action — review Mpo against the MF and
host-defence context together — has now been carried out.

This project tracks the impact on AI Gene Review. Mouse `Mpo` is reviewed as
of 2026-10-16.

## Upstream tickets

- Local follow-up tracker: [ai4curation/ai-gene-review#4098](https://github.com/ai4curation/ai-gene-review/issues/4098)
- Annotation tracker: [geneontology/go-annotation#6404](https://github.com/geneontology/go-annotation/issues/6404) — open as of 2026-10-04
- Ontology ticket (incorrect is-a parent): [geneontology/go-ontology#22891](https://github.com/geneontology/go-ontology/issues/22891) — closed 2026-06-08
- Earlier grouping-term cleanup (GO:0002148 already obsoleted): [geneontology/go-ontology#30524](https://github.com/geneontology/go-ontology/issues/30524) — closed 2025-12-05
- Affected annotations spreadsheet: [Google Sheet](https://docs.google.com/spreadsheets/d/1cEjK-1SbwIesQymn2RpMVtWx5mVwzO9f60GtILYOH3o/edit?usp=sharing)
- Impacted groups (per upstream issue): MGI — 1 annotation to GO:0002149

## Annotation inventory (verified via QuickGO 2026-05-20)

| Aspect | Term | Gene | UniProt | Taxon | Evidence | Reference | Assigned by | Qualifier |
|---|---|---|---|---|---|---|---|---|
| BP | GO:0002149 hypochlorous acid biosynthetic process | Mpo | P11247 | NCBITaxon:10090 (mouse) | IMP | PMID:10085024 | MGI | acts_upstream_of_or_within |
| BP | GO:0002149 hypochlorous acid biosynthetic process | Mpo | A0A0G2K1A2 | NCBITaxon:10116 (rat) | ISO (ECO:0000266) | GO_REF:0000121 | RGD | acts_upstream_of_or_within (with-from MGI:97137 = mouse Mpo) |
| BP | GO:0002150 hypochlorous acid catabolic process | — | — | — | — | — | — | (no direct protein annotations returned by QuickGO) |

The rat annotation is ISO-propagated from the mouse one; if the mouse
annotation is migrated, the rat record will follow automatically through
the next ISO pipeline. The catabolic-process term (GO:0002150) appears to
have no direct protein annotations, so its obsoletion is purely
terminological.

## Why this fits AI Gene Review

Single concrete gene: **mouse myeloperoxidase (Mpo, P11247)**. Myeloperoxidase
is the textbook HOCl-generating enzyme of neutrophils (RHEA:43232,
EC 1.11.2.2; H2O2 + Cl- + H+ → HOCl + H2O). The enzyme catalyzes one well-defined reaction whose product is HOCl.
An earlier draft of this page named **GO:0140825** as the precise MF term
for it, but OLS labels GO:0140825 *lactoperoxidase activity* ("2 a phenolic
donor + H2O2 = 2 a phenolic radical donor + 2 H2O"), which is not the
HOCl-forming reaction. The nearest GO term found by name,
GO:0016691 *chloride peroxidase activity*, is defined as organic
chlorination ("2 R-H + 2 chloride + H2O2 = 2 R-Cl + 2 H2O").

**Resolved 2026-10-16.** Two corrections and one conclusion:

1. The reaction identifier used earlier on this page and in issue #4098,
   RHEA:43232, is wrong: it is `isatin + H2O = isatinate + H(+)`. The
   myeloperoxidase reaction is **RHEA:28218**, which is what UniProt P11247
   itself cites ("Reaction=chloride + H2O2 + H(+) = hypochlorous acid + H2O;
   Xref=Rhea:RHEA:28218 … EC=1.11.2.2").
2. Searching GO for RHEA:28218 and EC:1.11.2.2 (QuickGO term search plus an
   xref scan of the local ontology build) returns **no term**. GO:0016691 is
   EC:1.11.1.10 (organic chlorination) and GO:0140825 is EC:1.11.1.7; the only
   other live HOCl-named terms are GO:1901531 *hypochlorite binding* and
   GO:1901530 *response to hypochlorite*, neither catalytic.
3. GO currently files this activity under **GO:0004601 peroxidase activity**,
   which carries *myeloperoxidase activity* as a narrow synonym and the
   Reactome xrefs R-HSA-6789126 / R-HSA-6789031 ("Myeloperoxidase (MPO)
   produces hypochlorous acid (HOCl)"). The Mpo review therefore accepts
   GO:0004601 as the most precise existing term and proposes a child,
   *hypochlorous acid synthase activity* (skos:exactMatch RHEA:28218) - named to
   avoid reading as a child of GO:0016691 - modelled on the sibling term GO:0036393
   *thiocyanate peroxidase activity* (RHEA:69416), which already exists for the
   pseudohalide version of the same reaction and is annotated to Mpo by the Rhea
   pipeline. Creating the term is an upstream GO request.
The cached human neutrophil extracellular trap GO-CAM `68fac5ed00000028`
already models human MPO as GO:0004601 *peroxidase activity* with H2O2 input
and HOCl output, which reinforces the GO-CAM/MF shape of the assertion
while leaving the need for a precise HOCl-forming MF term unresolved.
The GOA update is therefore a clean Type B refresh:

- Migrate the IMP annotation away from the now-obsolete BP term to
  whichever target the upstream ticket settles on.
- Most likely target classes the curators are choosing between are:
  - `GO:0042744 hydrogen peroxide catabolic process` (since Mpo consumes H2O2),
  - a broader ROS-biosynthesis term such as
    `GO:1903409 reactive oxygen species biosynthetic process`,
  - or a new term *hypochlorous acid biosynthesis from hydrogen peroxide*
    if upstream chooses to keep the chemistry and only fix the parentage.

  Note: `GO:0042554 superoxide anion generation` is **not** a defensible
  target for Mpo — that term is the NADPH-oxidase (NOX2/CYBB) step
  upstream of Mpo in the respiratory burst (NADPH oxidase → O2•- → SOD
  → H2O2 → Mpo → HOCl); Mpo consumes H2O2 rather than generating
  superoxide.

The upstream `go-annotation#6404` body does not list a chosen replacement,
so this remains passive tracking until the upstream decision lands.

## Impact on this repo

- Mouse **Mpo** (P11247) is now reviewed: `genes/mouse/Mpo/Mpo-ai-review.yaml`
  (84 distinct GOA annotations, status COMPLETE) with working notes in
  `genes/mouse/Mpo/Mpo-notes.md`.
- The obsoleted terms are **not** in the current GOA download for mouse Mpo, nor
  in QuickGO's 65 rows for rat Mpo, so no review in this repo carries
  GO:0002148/0002149/0002150 and none needs a `MODIFY` to a replacement term.
- The chemistry the obsoleted BP term described is captured in the review by the
  MF rows `GO:0004601 peroxidase activity` (IDA and IMP, both PMID:10085024 —
  the same reference that backed GO:0002149) and by the process rows
  `GO:0042744 hydrogen peroxide catabolic process` (IDA and IMP from the same
  paper), all accepted.
- Human `MPO` (P05164) is still unreviewed. It is the source of most ISS/ISO
  rows in the mouse review and appears twice in the cached NET GO-CAM
  `68fac5ed00000028`, so it is a worthwhile review on its own merits — but it
  carried no GO:0002149 annotation and is not blocked by the obsoletion. Left as
  an optional follow-on rather than a project dependency.
- No isolated InterPro2GO, UniProt-Keywords, or UniRule mappings to any
  of the three terms are listed in the upstream issue.

## Genes in scope

| Tier | Gene | Organism | UniProt | Reviewed here? | Status |
|---|---|---|---|---|---|
| 1 | Mpo (myeloperoxidase) | Mus musculus | P11247 | **Yes (2026-10-16)** | The only gene that had a direct IMP to GO:0002149. Full review of all 84 distinct GOA annotations (85 TSV rows, one duplicated); HOCl chemistry retained as MF + H2O2 catabolism; a child of GO:0004601 proposed for the reaction. |
| (follow-on) | Mpo | Rattus norvegicus | A0A0G2K1A2 | No | ISO descendant; verified in QuickGO this session to carry no GO:0002149 row, so it followed the mouse migration. No residual RGD follow-up. |
| (follow-on) | MPO | Homo sapiens | P05164 | No | Human ortholog; optional review, not required by the obsoletion. |

## Remaining work

1. **Upstream GO ontology request** — create a molecular-function child of
   GO:0004601 for `chloride + H2O2 + H(+) = hypochlorous acid + H2O`
   (EC 1.11.2.2, RHEA:28218). The proposal text, with parentage and mapping,
   is in `proposed_new_terms` of the Mpo review. Not actionable in this repo.
2. **Upstream annotation ticket** — geneontology/go-annotation#6404 can be
   closed once the MGI migration is confirmed on their side; the GOA download
   already shows the row gone. (That repository is not reachable from the
   session that made this change, so its comment state was not re-read.)
3. **Optional** — review human `MPO` (P05164), which would also let the cached
   NET GO-CAM `68fac5ed00000028` be assessed against a gene review.

## Priority

**Low, and mostly finished.** One experimental annotation was affected, it has
already migrated upstream, and the gene behind it is now reviewed. What is left
is an ontology request that only GO can act on, plus an optional human review.

## Status

- 2026-05-20 — Project file created. Upstream annotation issue #6404
  open, no comments. Parent BP term GO:0002148 already obsoleted via
  go-ontology#30524 (closed). Two child BP terms (GO:0002149,
  GO:0002150) still active. No replacement target chosen upstream. No
  reviews started in this repo.
- 2026-10-04 — Rechecked OLS and GitHub state. GO:0002149 and GO:0002150
  are obsolete with the "represents a MF term" rationale; go-annotation#6404
  remains open for the MGI row with no comments; go-ontology#22891 is
  closed; no mouse Mpo, rat Mpo, or human MPO review exists in this repo.
  Opened #4098 to track the deferred Mpo review and the still-unresolved MF
  lookup for RHEA:43232 / EC 1.11.2.2.
- 2026-10-16 — Follow-ups worked through (issue #4098). Corrected the reaction
  identifier (RHEA:28218, not RHEA:43232) and established that GO has no MF
  term for it; completed the mouse `Mpo` review; confirmed via GOA and QuickGO
  that both the mouse and rat GO:0002149 rows are gone; decided human `MPO` is
  an optional follow-on rather than a dependency. Remaining item is the upstream
  ontology request.
