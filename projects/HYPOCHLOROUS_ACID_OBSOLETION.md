# Hypochlorous Acid Metabolic Process Terms — Obsoletion

## Overview

A GO obsoletion proposal targets three biological-process terms in the
hypochlorous acid (HOCl) branch:

- **GO:0002148 hypochlorous acid metabolic process** (BP, **already obsolete**)
- **GO:0002149 hypochlorous acid biosynthetic process** (BP, *active*, obsoletion proposed)
- **GO:0002150 hypochlorous acid catabolic process** (BP, *active*, obsoletion proposed)

The rationale, captured in go-ontology#22891, is that the original parentage
(`is_a` *organic acid metabolic process*, GO:0006082) is incorrect because
hypochlorous acid contains no carbon and so is not an organic acid. The
grouping-term obsoletion at the parent level (go-ontology#30524) already
removed GO:0002148, which had no remaining annotations. The two child terms
still carry annotations and need a curatorial decision before they can be
obsoleted.

This project tracks the impact on AI Gene Review. No genes in scope are
currently reviewed here.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6404](https://github.com/geneontology/go-annotation/issues/6404)
- Ontology ticket (incorrect is-a parent): [geneontology/go-ontology#22891](https://github.com/geneontology/go-ontology/issues/22891)
- Earlier grouping-term cleanup (GO:0002148 already obsoleted): [geneontology/go-ontology#30524](https://github.com/geneontology/go-ontology/issues/30524) — closed
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
EC 1.11.2.2; H2O2 + Cl- + H+ → HOCl + H2O). The molecular function
already has a precise MF term —
**GO:0140825 chloride peroxidase activity (HOCl-forming)** —
and the enzyme catalyzes one well-defined reaction whose product is HOCl.
The pending obsoletion is therefore a clean Type B refresh:

- Migrate the IMP annotation away from the soon-to-be-obsolete BP term to
  whichever target the upstream ticket settles on.
- Most likely target classes the curators are choosing between are:
  - `GO:0042554 superoxide anion generation` / sibling ROS-biosynthesis terms,
  - `GO:0042744 hydrogen peroxide catabolic process` (since Mpo consumes H2O2),
  - or a new term *hypochlorous acid biosynthesis from hydrogen peroxide*
    if upstream chooses to keep the chemistry and only fix the parentage.

The upstream `go-annotation#6404` body does not list a chosen replacement,
so this remains passive tracking until the upstream decision lands.

## Impact on this repo

- No genes annotated to GO:0002148/0002149/0002150 are currently reviewed.
- The mouse `genes/mouse/` tree exists and contains other genes, so adding
  Mpo is a natural extension — but the work should wait until upstream
  has a final replacement target so the review can record the correct
  `MODIFY` / `proposed_replacement_terms` decision.
- No isolated InterPro2GO, UniProt-Keywords, or UniRule mappings to any
  of the three terms are listed in the upstream issue.

## Candidate gene for review (deferred)

| Tier | Gene | Organism | UniProt | Existing in repo? | Notes |
|---|---|---|---|---|---|
| 1 | Mpo (myeloperoxidase) | Mus musculus | P11247 | No | Only gene with a direct IMP annotation to GO:0002149. Carries 20+ other GOA rows; a full `/review` would cover the broader heme-peroxidase / neutrophil-degranulation context. |
| (follow-on) | Mpo | Rattus norvegicus | A0A0G2K1A2 | No | ISO descendant; will follow the mouse migration automatically. |
| (follow-on) | MPO | Homo sapiens | P05164 | No | Not in the upstream affected list (no direct GO:0002149 annotation) but is the human ortholog and the textbook reference for the activity; reviewing only if the upstream replacement term is interesting cross-organism. |

## Proposed approach

1. **Wait for upstream replacement-term decision.** The current upstream
   ticket #6404 has zero comments and the ontology ticket #22891 only
   raises the is-a parentage problem; no obsoletion PR has been opened.
   There is no point migrating the annotation before the target is
   chosen, since the current MGI IMP row is otherwise well-evidenced
   (PMID:10085024).
2. **When upstream lands**, run `just fetch-gene mouse Mpo` and do a full
   `/review` — Mpo is a high-yield review target regardless of the
   obsoletion (peroxidase MF, neutrophil/granule CC, immune-defense BP,
   well-cited literature).
3. **Cross-reference GO:0140825** *chloride peroxidase activity
   (HOCl-forming)* — this MF is the precise activity catalyzed by Mpo
   and should appear in the `core_functions` section. The pending BP
   obsoletion does not affect this MF term.
4. **Defer the rat ISO row** — it will follow the mouse migration
   automatically through the standard ISO pipeline.

## Priority

**Low.** Only one direct experimental annotation is affected, the
obsoletion has no chosen target yet upstream, and the affected gene
(Mpo) is not currently reviewed here. The opportunity is that Mpo is
an otherwise unreviewed, well-characterized mammalian heme peroxidase
that would extend the repo's mouse coverage, not that any existing
review is blocked.

## Status

- 2026-05-20 — Project file created. Upstream annotation issue #6404
  open, no comments. Parent BP term GO:0002148 already obsoleted via
  go-ontology#30524 (closed). Two child BP terms (GO:0002149,
  GO:0002150) still active. No replacement target chosen upstream. No
  reviews started in this repo.
