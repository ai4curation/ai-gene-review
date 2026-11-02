---
title: "Vesicle Targeting (GO:0006903) & Descendants — Obsoletion & Replacement"
maturity: SCOPING
last_reviewed: 2026-10-05
tags: [OBSOLETION, FLAGSHIP]
species: [human, yeast]
genes: [YKT6, CLASP1, CLASP2, WIPI1, AP1AR, GLTP, SPA2]
manifest:
  slides:
    - href: VESICLE_TARGETING_OBSOLETION/slides/VESICLE_TARGETING_OBSOLETION-slides.html
      description: Vesicle targeting obsoletion slides
---

# Vesicle Targeting (GO:0006903) & Descendants — Obsoletion & Replacement

**Bottom line:** Vesicles are moved along the cytoskeleton and delivered
to the right membrane before they tether, dock and fuse. GO has
obsoleted GO:0006903 *vesicle targeting* and nine descendants because
the line between vesicle "targeting" and vesicle-mediated "transport"
was never applied consistently; unlike the sibling tethering and
docking changes, no new term was minted, and annotations move to
existing transport processes such as GO:0016192 *vesicle-mediated
transport* and GO:0006895 *Golgi to endosome transport*. We pulled the
22 experimental annotations from QuickGO (they fall on 4 of the 10
terms, 6 of them on human genes), mapped each to its replacement, and
queued the human trafficking genes (YKT6, CLASP1, CLASP2, WIPI1, AP1AR)
for new reviews. The obsoletion has started to appear in released
ontology snapshots: by the 2026-10-04 audit, OLS showed GO:0006903 and
GO:0048203 as obsolete. Scoped, not yet started: none of the queued
human genes has a review here. The only in-repo exact hit is now
historical: yeast `SPA2` retains a retired ComplexPortal NAS annotation
to GO:0006903 for the polarisome, kept as non-core, while the current
SPA2 GOA has no GO:0006903 row or GO:0016192 successor row.

Sibling trackers cover the later steps of vesicle delivery, which GO
did move to new molecular functions:
[VESICLE_TETHERING_OBSOLETION](VESICLE_TETHERING_OBSOLETION.md)
(#6375),
[VESICLE_DOCKING_OBSOLETION](VESICLE_DOCKING_OBSOLETION.md) (#6379) and
[SYNAPTIC_VESICLE_DOCKING_OBSOLETION](SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md)
(#6415).

## Overview

The GO obsoletion retired `GO:0006903 vesicle targeting` and its
descendant hierarchy. These BP terms conflated a *vesicle-mediated
transport* process with a *targeting/tethering* step in a way that GO
no longer considers meaningful, so each was collapsed onto a broader,
well-defined vesicle-transport parent. The biology is unchanged; the
fix is terminological (move annotations to the designated replacement
transport term).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6424](https://github.com/geneontology/go-annotation/issues/6424)
- Ontology ticket: [geneontology/go-ontology#31865](https://github.com/geneontology/go-ontology/issues/31865) — **closed 2026-05-16**
- Upstream review spreadsheet (curator-maintained): `https://docs.google.com/spreadsheets/d/1o5T_b5I9RNLdWUgcnaHxv4lqiY88_Al3CvpC4ul3Sv8`
- Local follow-up: [ai4curation/ai-gene-review#569](https://github.com/ai4curation/ai-gene-review/issues/569)
  — tracks the remaining YKT6, CLASP1/CLASP2, WIPI1, AP1AR, GLTP, and
  yeast AP-1 review queue

## Obsoletion plan (per upstream issue)

| Obsoleted term | ID | Replacement |
|---|---|---|
| vesicle targeting | GO:0006903 | GO:0016192 vesicle-mediated transport |
| vesicle targeting to fusome | GO:0045479 | (no explicit replacement listed) |
| clathrin coating of Golgi vesicle, plasma membrane to endosome targeting | GO:0010785 | (no explicit replacement listed) |
| vesicle targeting, plasma membrane to endosome | GO:0048201 | (no explicit replacement listed) |
| vesicle targeting, to, from or within Golgi | GO:0048199 | GO:0048193 Golgi vesicle transport |
| vesicle targeting, rough ER to cis-Golgi | GO:0048207 | GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport |
| regulation of vesicle targeting, to, from or within Golgi | GO:0048209 | (no explicit replacement listed) |
| vesicle targeting, cis-Golgi to rough endoplasmic reticulum | GO:0048206 | GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum |
| vesicle targeting, inter-Golgi cisterna | GO:0048204 | GO:0048219 inter-Golgi cisterna vesicle-mediated transport |
| vesicle targeting, trans-Golgi to endosome | GO:0048203 | GO:0006895 Golgi to endosome transport |

At project creation, all ten source terms were still **active** in
QuickGO / GO API on 2026-05-17: the ontology ticket had merged, but the
obsoletion had not yet propagated to the released ontology or annotations.
By the 2026-10-04 audit, OLS already listed at least GO:0006903 and
GO:0048203 as obsolete. Re-pull QuickGO before starting YKT6 or the other
queued human reviews so the local GOA reflects any completed upstream
annotation transfers.

## Affected experimental / direct annotations

Pulled from QuickGO (`goUsage=exact`, experimental evidence
`ECO:0000269` descendants) on 2026-05-17. **22** experimental
annotations fall on just **4** of the 10 obsoleted terms; the other
six terms (GO:0045479, GO:0010785, GO:0048201, GO:0048209,
GO:0048206, GO:0048204) have **zero** experimental annotations and
will be handled entirely by IEA/IBA auto-migration.

### GO:0006903 vesicle targeting → GO:0016192 vesicle-mediated transport (12)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:O15498 | **YKT6** | Homo sapiens (9606) | IDA | PMID:9211930 |
| UniProtKB:Q7Z460 | **CLASP1** | Homo sapiens (9606) | IMP | PMID:24859005 |
| UniProtKB:O75122 | **CLASP2** | Homo sapiens (9606) | IMP | PMID:24859005 |
| UniProtKB:Q61161 | Map4k2 | Mus musculus (10090) | IDA | PMID:8643544 |
| UniProtKB:Q8K3E5 | `Ahi1` | Mus musculus (10090) | IMP (acts_upstream_of_or_within) | PMID:20592197 |
| UniProtKB:P21707 | Syt1 | Rattus norvegicus (10116) | IDA | PMID:14715137 |
| UniProtKB:P61023 | Chp1 | Rattus norvegicus (10116) | IDA | PMID:8626580 |
| UniProtKB:Q258K2 | `MYH9` | Canis lupus familiaris (9615) | IMP | PMID:18504258 |
| UniProtKB:P53141 | MLC1 | S. cerevisiae S288C (559292) | IMP | PMID:12456647 |
| ComplexPortal:CPX-3188 | polarisome | S. cerevisiae S288C (559292) | IMP | PMID:16166638 |
| UniProtKB:P0CY31 | SEC4 | Candida albicans SC5314 (237561) | IGI | PMID:9639314 |
| UniProtKB:Q9C744 | DELTA-ADR | Arabidopsis thaliana (3702) | IEP (acts_upstream_of_or_within) | PMID:28559361 |

### GO:0048203 vesicle targeting, trans-Golgi to endosome → GO:0006895 Golgi to endosome transport (7)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:Q5MNZ9 | **WIPI1** | Homo sapiens (9606) | IDA | PMID:15020712 |
| UniProtKB:Q63HQ0 | **AP1AR** | Homo sapiens (9606) | IDA | PMID:19706427 |
| UniProtKB:P35181 | APS1 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| UniProtKB:P36000 | APL2 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| UniProtKB:P38700 | APM2 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| UniProtKB:Q12028 | APL4 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| ComplexPortal:CPX-533 | AP-1 complex | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |

### GO:0048199 vesicle targeting, to, from or within Golgi → GO:0048193 Golgi vesicle transport (2)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:Q63584 | Tmed10 | Rattus norvegicus (10116) | IEP | PMID:17101722 |
| UniProtKB:Q9D1D4 | Tmed10 | Mus musculus (10090) | IEP | PMID:17101722 |

### GO:0048207 vesicle targeting, rough ER to cis-Golgi → GO:0006888 ER to Golgi vesicle-mediated transport (1)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:Q9NZD2 | GLTP | Homo sapiens (9606) | IMP | DOI:10.1101/2025.06.17.657375 (preprint) |

A large pool of **IEA** annotations (~2,470 across these terms in
QuickGO) and any **IBA** propagations will be remapped automatically
once the obsoletion lands and the next pipeline runs. These do not
need per-annotation work here.

### Mapping cleanup (per upstream issue)

- **InterPro2GO:** `InterPro:IPR031483` (AP-1 complex-associated
  regulatory protein) → GO:0048203 — needs remapping to the
  replacement GO:0006895 by the InterPro2GO maintainers. This is an
  InterPro mapping concern, not a per-gene review item.
- No ARBA / UniRule mappings to the obsoleted terms were listed
  (UniRule appears in the upstream template header only).

## Impact on this repo

Only one in-repo review currently touches the obsoleted subtree
historically: `genes/yeast/SPA2/SPA2-ai-review.yaml` retains a retired
ComplexPortal polarisome GO:0006903 row and keeps it as non-core. The
current SPA2 GOA no longer carries GO:0006903 or a GO:0016192 successor
for the polarisome assertion, and the human queue above (`YKT6`, `CLASP1`,
`CLASP2`, `WIPI1`, `AP1AR`, `GLTP`) remains unreviewed here.

So no active local review is waiting on a deterministic term swap. Watch
future SPA2 GOA pulls for a successor ComplexPortal transport row, while
the human work remains forward-looking. This differs from the
synaptic-vesicle-docking tracker (go-annotation#6415), where `mouse Camk2a`
had to be queued for a refresh. Here the project is mostly an opportunity
to add high-value, currently-unreviewed human trafficking genes.

## Scope

- **Organisms**: human (6 of 22 EXP rows, 6 distinct human genes)
  and *S. cerevisiae* (7 rows, all the AP-1 / polarisome / MLC1
  complex annotations) carry most of the experimental signal. Rat, mouse,
  dog, Candida, and Arabidopsis rows are orthologs that
  will largely follow automatically once the model-organism groups
  remap.
- **GO branches**: BP only — a transport-vs-targeting collapse onto
  broader vesicle-transport parents. No MF or CC changes.
- **Type of fix**: terminological. Reviews should ask whether the
  designated replacement is the *most informative* available term
  for the gene's core role, or whether a more specific extant BP
  (or an MF) better captures the function — e.g. YKT6 is a SNARE
  whose core MF (SNARE binding / SNAP receptor activity) is more
  informative than any generic transport BP.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` and confirm the
UniProt accession before starting. None are currently in the repo.

### Tier 1 — human, well-characterized, strong direct evidence

1. **YKT6 / O15498** (Homo sapiens) — longin-domain R-SNARE central
   to ER–Golgi and autophagosome–lysosome fusion. IDA on GO:0006903
   (PMID:9211930). Best single candidate: heavily studied, core MF
   anchor (SNARE / SNAP receptor activity) is far more informative
   than the generic GO:0016192 replacement, so this is a good test
   of MODIFY-vs-transfer judgement.
2. **CLASP1 / Q7Z460** and **CLASP2 / O75122** (Homo sapiens) —
   microtubule plus-end tracking proteins; both IMP on GO:0006903
   from the same study (PMID:24859005) implicating them in
   Golgi-derived vesicle transport. Reviewable as a pair.
3. **WIPI1 / Q5MNZ9** (Homo sapiens) — PI3P-binding autophagy
   effector; IDA on GO:0048203 (PMID:15020712, trans-Golgi to
   endosome). Review should weigh the GO:0006895 replacement against
   WIPI1's better-characterized autophagy/PI3P-binding roles.

### Tier 2 — human, adaptor / less direct

4. **AP1AR / Q63HQ0** (Homo sapiens) — AP-1 complex-associated
   regulatory protein (gadkin); IDA on GO:0048203 (PMID:19706427).
   Note this gene is also the subject of the InterPro2GO mapping
   cleanup (IPR031483 → GO:0048203).

### Tier 3 — opportunistic / lower value

5. **GLTP / Q9NZD2** (Homo sapiens) — glycolipid transfer protein;
   IMP on GO:0048207 but the only reference is an unpublished
   preprint (DOI:10.1101/2025.06.17.657375). Lower priority until a
   peer-reviewed reference exists.
6. *S. cerevisiae* AP-1 clathrin-adaptor subunits (**APL2/APL4/
   APM2/APS1**, PMID:17003107) — a coherent yeast complex set, but
   all IMP from a single study; consider only if extending yeast
   coverage. SGD / ComplexPortal curators will likely remap these
   directly.

## Proposed approach

1. **Re-pull GOA before each review.** The ontology obsoletion has
   landed, but GOA transfer status still needs to be checked gene by
   gene. Run `just fetch-gene` immediately before starting a queued
   review so the local GOA reflects any upstream migration from the
   retired targeting term to its transport replacement.
2. **Start with human YKT6.** Run `just fetch-gene human YKT6`, then
   review per CLAUDE.md. Expect the right call to be MODIFY toward a
   more informative SNARE MF rather than a literal transfer to the
   generic transport BP.
3. **Follow with CLASP1/CLASP2 (as a pair), then WIPI1, then
   AP1AR.** Each review evaluates whether the designated
   replacement BP is the most informative term or whether a
   narrower extant BP / cognate MF is warranted.
4. **Defer Tier 3** (GLTP preprint-only; yeast AP-1 subunits) unless
   they surface via other workstreams.
5. **Do not create reviews for the ortholog rows** (rat, mouse, dog,
   Candida, or Arabidopsis) or the IEA/IBA pool — these auto-migrate.

## Priority

**Medium.** 22 experimental annotations across 7 organisms — larger
than most obsoletion trackers in this repo — and several affected
human genes (YKT6, CLASP1/2, WIPI1) are biologically important
trafficking proteins with **no review yet in this repo**. The
obsoletion is a good trigger to add them, but the work should wait
for a fresh per-gene GOA pull so reviewers can see whether upstream
has already migrated each targeting row.

## Status

- 2026-05-17 — Project file created. Upstream annotation issue
  go-annotation#6424 open (last updated 2026-05-15); ontology ticket
  go-ontology#31865 closed 2026-05-16. All ten source terms still
  active in QuickGO/GO API; all six replacement targets valid. No
  affected gene is reviewed in this repo, so nothing needs refresh —
  held as a forward-looking tracking project. No gene reviews
  started.
- 2026-10-04 — Re-audited local reviews. The six queued human genes
  remain absent, but yeast SPA2 now has a review retaining the retired
  ComplexPortal GO:0006903 row as non-core; the current SPA2 GOA no
  longer carries GO:0006903 or a GO:0016192 successor.
