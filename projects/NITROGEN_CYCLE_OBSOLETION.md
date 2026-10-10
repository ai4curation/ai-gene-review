---
title: "Nitrogen Cycle Metabolic Process — do_not_annotate / Regulation Term Obsoletion"
maturity: SCOPING
last_reviewed: "2026-10-04"
tags: [OBSOLETION]
species: [mouse, human, AZOVI]
genes: [nifA, SEC63]
sidecars:
  slide_assets:
    - NITROGEN_CYCLE_OBSOLETION/slides/n-cycle.svg
    - NITROGEN_CYCLE_OBSOLETION/slides/term-map.svg
manifest:
  slides:
    - href: NITROGEN_CYCLE_OBSOLETION/slides/NITROGEN_CYCLE_OBSOLETION-slides.html
      description: AI generated
---

# Nitrogen Cycle Metabolic Process — do_not_annotate / Regulation Term Obsoletion

**Bottom line:** GO:0071941 *nitrogen cycle metabolic process* names the
ecosystem-level nitrogen cycle, whose real pathways (denitrification,
nitrification, nitrogen fixation, mineralization) are its children. Upstream
closed the ontology cleanup: GO:0071941 stays live as a non-annotatable
grouping term, while GO:1903314, GO:1903315 and GO:1903316 are obsolete. The
May 2026 exact annotation set had six experimental rows on GO:0071941: five
mouse kidney/liver genes from polycystic-disease and liver-zonation papers and
one bacterial periplasmic nitrate reductase. Current QuickGO has only the
CACAO `napA` row left on GO:0071941, and that row should move to GO:0019333
*denitrification pathway*. The obsolete-term hit in this repo was *A.
vinelandii* nifA; #3235 removed GO:1903316 from authored term slots and left a
request for a new *positive regulation of nitrogen fixation* term.

## Overview

The upstream cleanup has two parts:

- Treat **GO:0071941 nitrogen cycle metabolic process** as a live grouping term
  whose direct annotations should move to descendant pathway terms such as
  denitrification, nitrogen fixation, nitrification, or mineralization.
- Obsolete the three regulation terms outright:
  - GO:1903314 regulation of nitrogen cycle metabolic process
  - GO:1903315 negative regulation of nitrogen cycle metabolic process
  - GO:1903316 positive regulation of nitrogen cycle metabolic process

The motivation (per upstream) is that "nitrogen cycle metabolic process" is an
ecosystem-level grouping term: real biology happens in its children
(denitrification, nitrification, nitrogen fixation, mineralization). Direct
annotation to the parent erases mechanistic detail and — more importantly — has
attracted over-annotations of mammalian genes that have nothing to do with the
ecological nitrogen cycle.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6411](https://github.com/geneontology/go-annotation/issues/6411)
  (closed 2026-05-26)
- Ontology ticket: [geneontology/go-ontology#27220](https://github.com/geneontology/go-ontology/issues/27220)
  (closed 2026-05-13)

## Obsoletion / do_not_annotate outcome

| Term | ID | Action | Replacement strategy |
|---|---|---|---|
| nitrogen cycle metabolic process | GO:0071941 | `do_not_annotate` (stays as grouping term) | Re-route to a specific descendant: e.g. GO:0019333 denitrification pathway, GO:0009399 nitrogen fixation, or a nitrification/mineralization child as appropriate |
| regulation of nitrogen cycle metabolic process | GO:1903314 | obsolete | No replacement currently slated — only relevant if a child regulation term exists for the specific pathway |
| negative regulation of nitrogen cycle metabolic process | GO:1903315 | obsolete | Same |
| positive regulation of nitrogen cycle metabolic process | GO:1903316 | obsolete | Same |

GO:0071941 and GO:0009399 remained live in QuickGO on 2026-10-04;
GO:1903314/GO:1903315/GO:1903316 returned as obsolete.

## Affected experimental annotations

The upstream issue cites 5 MGI + 1 CACAO experimental annotations.
QuickGO (exact-term query against GO:0071941, evidence codes IDA / IMP / IGI /
IPI / IEP) on 2026-05-13 returns 6 direct experimental annotations — matching
the upstream count:

| # | Gene | Accession | Taxon | Qualifier | Evidence | PMID | Assigned by | Replacement plan |
|---|---|---|---|---|---|---|---|---|
| 1 | Prkcsh | UniProtKB:O08795 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Prkcsh is glucosidase II β / Pkd-network polycystic-liver gene; no nitrogen-cycle role |
| 2 | Pkd1 | UniProtKB:O08852 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Polycystin-1, cystogenic Ca²⁺ signalling; no nitrogen-cycle role |
| 3 | Pkd1 (dup) | UniProtKB:O08852 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Duplicate row; flag both annotations |
| 4 | Apc | UniProtKB:Q61315 | Mus musculus (10090) | acts_upstream_of_or_within | IMP | PMID:16740478 | MGI | **REMOVE** — Adenomatous polyposis coli (Wnt pathway / liver zonation); no nitrogen-cycle role |
| 5 | Sec63 | UniProtKB:Q8VHE0 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Sec63 translocon component; no nitrogen-cycle role |
| 6 | napA | UniProtKB:O88111 | Cereibacter sphaeroides f. sp. denitrificans (39723) | involved_in | IMP | PMID:10227138 | CACAO | **MODIFY → GO:0019333 denitrification pathway** — Periplasmic nitrate reductase; legitimate denitrification gene |

Five of the six annotations look like classic over-annotation of mammalian
kidney/liver genes (PKD1, PRKCSH, SEC63 are the canonical autosomal dominant
polycystic kidney/liver disease genes; APC drives a liver-zonation phenotype).
The 1999 paper supporting napA (PMID:10227138, Biosci. Biotechnol. Biochem.) is
explicitly about denitrification in Rhodobacter (Cereibacter) sphaeroides, so
the bacterial annotation is biologically sound but should be moved to the
specific child term GO:0019333 (denitrification pathway), not stranded on the
parent.

At the 2026-05-13 pre-obsoletion impact check, the three regulation children
(GO:1903314 / 1903315 / GO:1903316) had **zero experimental annotations** in
QuickGO, so their obsoletion was uncontested from an annotation-impact
standpoint.

## Impact on this repo

The original six GO:0071941 rows were in mouse and *Cereibacter* GOA. A
2026-10-04 QuickGO exact-term query now returns only the *Cereibacter* `napA`
row, so the five MGI mouse rows appear to have been removed upstream. Human
SEC63 has been reviewed, but its current GOA file has no GO:0071941 row. The
one local obsolete-term hit was in
`genes/AZOVI/nifA/nifA-ai-review.yaml`: before #3235, the review used obsolete
GO:1903316 as a replacement for the GO:0009399 *nitrogen fixation* row, a NEW
annotation and a `core_functions` term. #3235 removed those authored uses,
retained a live GO:0045893 replacement for the row as the current best fit, and
requested a new *positive regulation of nitrogen fixation* child term.

## Scope

- **Organisms involved:** mouse (Mus musculus, 4 of the 5 MGI annotations
  collapse to 4 distinct genes after the Pkd1 duplicate) and Cereibacter
  sphaeroides f. sp. denitrificans (1 CACAO annotation).
- **GO branch:** biological process — nitrogen metabolism / microbial
  nitrogen-cycle pathways and their mammalian over-annotations.
- **Type of fix:**
  - Five mammalian annotations are scientifically incorrect (these genes do
    not act in the nitrogen cycle as defined by the term) and should be
    **removed**, not relabelled. The annotation pattern suggests automatic
    propagation from a kidney/liver phenotype to "nitrogen handling" without
    discriminating ecological nitrogen cycle (microbial) from mammalian
    nitrogen excretion biology.
  - One bacterial annotation is correct in spirit but should be **modified**
    to a specific child term (GO:0019333 denitrification pathway).

## Remaining exact annotation

**napA (Cereibacter sphaeroides f. sp. denitrificans, UniProtKB:O88111)** is
the only remaining exact GO:0071941 hit in QuickGO. It encodes periplasmic
nitrate reductase. The PMID:10227138 IMP evidence supports involvement in
denitrification, so the parent-term annotation should be **modified** to
GO:0019333 denitrification pathway. Use the species code corresponding to
taxon 39723 (Cereibacter sphaeroides f. sp. denitrificans). This is a
non-canonical organism for the repo and may not have an obvious species
subdirectory yet; check before invoking `just fetch-gene`.

The five MGI rows on mouse Pkd1, Prkcsh, Sec63 and Apc appear to have been
removed upstream. Human SEC63 is already reviewed in this repo and has no
GO:0071941 row to remove.

## Follow-up queue

1. **Pattern-document the mammalian over-annotation first.** Add a short
   section to `projects/OVER_ANNOTATION_PATTERNS.md` (or a new entry there)
   noting that GO:0071941 has attracted polycystic kidney/liver genes via
   IGI/IMP propagation from PMID:21685914 and PMID:16740478. This is a
   reusable insight even if the obsoletion is delayed.
2. **Move the remaining napA row if it is still present when Cereibacter is
   seeded.** It is biologically correct and only needs a term refinement
   (MODIFY); if the *Cereibacter* species directory does not yet exist, this
   is a small enough single-annotation case to defer.
3. **Keep #542 focused on the historical six GO:0071941 rows and the one
   current napA direct row.** The upstream tickets are closed, and the only
   stale authored GO:1903316 use in this repo was fixed by #3235.

## Priority

Medium-low. The total remaining exact annotation set is tiny (one current
`napA` row), but the original over-annotation pattern is illustrative — five
out of six annotations on a microbial-ecology term were on mammalian
kidney/liver genes. Documenting that pattern fits the repo's existing emphasis
on cleaning up over-annotations of pleiotropic genes (see
`projects/OVER_ANNOTATION_PATTERNS.md`).

## Status

- 2026-05-13 — Project file created. Tracking upstream issue #6411 (opened
  prior; last upstream activity 2026-05-12). Term labels and the proposed
  replacement (GO:0019333) verified in OLS. Affected annotation set
  cross-checked via the QuickGO REST API (6 hits, matching the upstream
  count). No reviews started; none of the 5 distinct affected genes are in
  the repo yet.
- 2026-09-26 — OLS listed GO:1903314/1903315/1903316 as obsolete ("regulation
  at that level is not biologically meaningful at the gene-product level");
  GO:0071941 was still live. Human SEC63 now had a review, but its GOA file
  had no GO:0071941 row. `genes/AZOVI/nifA/nifA-ai-review.yaml` used GO:1903316 in
  three places (MODIFY target for GO:0009399, a NEW row, and
  `core_functions`); the local `cache/ontologies/go.tsv` still listed it as
  live, so validation does not flag it.
- 2026-09-26 (later) — The nifA GO:1903316 replacement was tracked in #3235,
  which recorded the per-row outcome in the nifA review. The six GO:0071941
  annotations remained unreviewed here.
- 2026-10-04 — Rechecked QuickGO: GO:0071941 and GO:0009399 are live;
  GO:1903314, GO:1903315 and GO:1903316 are obsolete. #3235 merged on
  2026-09-27, and `genes/AZOVI/nifA/nifA-ai-review.yaml` no longer uses
  GO:1903316 in any authored term slot. An exact GO:0071941 QuickGO search
  now returns only the CACAO `napA` row; the five MGI mouse rows appear to
  have been removed upstream. Issue #542 remains open for that direct parent
  row and for documenting the historical over-annotation pattern.
