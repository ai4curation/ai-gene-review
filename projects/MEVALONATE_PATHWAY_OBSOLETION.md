---
title: "Mevalonate Pathway Term Cleanup — Obsoletion & Replacement"
maturity: IN_PROGRESS
tags: [OBSOLETION]
species: [human, rat, yeast]
genes: [HMGCS1, HMGCR, MVK, PMVK, MVD, FDPS, IDI1, Hmgcs2, ERG19]
last_reviewed: "2026-10-04"
sidecars:
  slide_assets:
    - MEVALONATE_PATHWAY_OBSOLETION/slides/pathway-split.svg
    - MEVALONATE_PATHWAY_OBSOLETION/slides/term-map.svg
manifest:
  slides:
    - href: MEVALONATE_PATHWAY_OBSOLETION/slides/MEVALONATE_PATHWAY_OBSOLETION-slides.html
      description: AI generated
---

# Mevalonate Pathway Term Cleanup — Obsoletion & Replacement

**Bottom line:** GO had two overlapping process terms for the route from
acetyl-CoA through mevalonate to isoprenoid precursors: GO:1902767 *isoprenoid
biosynthetic process via mevalonate* and GO:0010142 *farnesyl diphosphate
biosynthetic process, mevalonate pathway*. Both are now obsolete in OLS
(checked 2026-09-26), with annotations to be redirected to GO:0019287
*isopentenyl diphosphate biosynthetic process, mevalonate pathway* (the steps
up to IPP) or GO:0045337 *trans, trans-farnesyl diphosphate biosynthetic
process* (IPP to FPP). We tracked the upstream lists (2 and 21 experimental
annotations) and argued that each row needs a per-enzyme choice between the
two replacements, not a relabel. The human mevalonate enzymes HMGCS1, HMGCR,
MVK, PMVK, MVD, IDI1 and FDPS are now reviewed (PRs #1998, #2153) with
`mevalonate_pathway` and `isoprenoid_diphosphate_biosynthesis` modules; MVK,
PMVK and MVD accept GO:0019287 while FDPS accepts GO:0045337. Two reviews
carried obsolete-term rows, both resolved in #3232: yeast ERG19's GO:0010142
RCA row is now `REMOVE`, since its replacement GO:0019287 is already accepted,
and rat Hmgcs2's GO:0010142 IBA and IEA rows stay `UNDECIDED`, with the
obsoletion recorded in `reason`.

## Overview

GO obsoleted two overlapping "mevalonate pathway" terms in favour of
better-scoped existing terms. The two old terms described pathway spans already
covered by `GO:0019287 isopentenyl diphosphate biosynthetic process,
mevalonate pathway` and/or `GO:0045337 trans,trans-farnesyl diphosphate
biosynthetic process`, so existing annotations need to be redirected or removed
after evidence review rather than carried on stale terms.

This project tracks both obsoletions as a single piece of work because they
share an upstream ontology ticket (geneontology/go-ontology#32082) and the
replacement target choice is the same for either source term.

## Upstream tickets

- Annotation tracker (this project): [geneontology/go-annotation#6440](https://github.com/geneontology/go-annotation/issues/6440) — review annotations to `GO:1902767 isoprenoid biosynthetic process via mevalonate`
- Companion annotation tracker: [geneontology/go-annotation#6439](https://github.com/geneontology/go-annotation/issues/6439) — review annotations to `GO:0010142 farnesyl diphosphate biosynthetic process, mevalonate pathway`
- Ontology ticket: [geneontology/go-ontology#32082](https://github.com/geneontology/go-ontology/issues/32082) — mevalonate pathway terms cleanup

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement(s) |
|---|---|---|
| isoprenoid biosynthetic process via mevalonate | GO:1902767 | consider `GO:0019287 isopentenyl diphosphate biosynthetic process, mevalonate pathway` or `GO:0045337 farnesyl diphosphate biosynthetic process` |
| farnesyl diphosphate biosynthetic process, mevalonate pathway | GO:0010142 | consider `GO:0019287 isopentenyl diphosphate biosynthetic process, mevalonate pathway` or `GO:0045337 trans,trans-farnesyl diphosphate biosynthetic process` |

Both terms are obsolete in the GO release dated 2026-07-26.

The replacement is not a single 1:1 swap — `GO:1902767` and `GO:0010142` both
describe a multi-step pathway that runs through mevalonate to IPP and then on
to FPP. After obsoletion, each annotation needs to land on whichever of the
two replacement terms (or both) accurately describes the actual reaction(s)
that the experiment supports. That is a scientific judgement, not a mechanical
relabel.

## Upstream annotation counts

From the ontology issue (geneontology/go-ontology#32082):

| Term | Direct EXP annotations | Genes listed in upstream |
|---|---|---|
| GO:1902767 (this issue) | 2 | erg9, yajO |
| GO:0010142 (companion #6439) | 21 | fps1, dps1, spo9, ERG12, ERG8, hcs1, Idi1, Hmgcr, Acat2, Hmgcs1, Fdps, Mvd, ACAT2, Pmvk, Mvk, hmgr |

Per #6440's body, the GO:1902767 list was later down to "1 EcoCyc"
annotation after the PomBase entry was fixed. Identifying that remaining
EcoCyc row, and confirming whether it is the E. coli `yajO` entry, is tracked
in [#1401](https://github.com/ai4curation/ai-gene-review/issues/1401).

For GO:0010142 (companion #6439), the full set should be re-pulled from
QuickGO at review time — many of the 21 listed genes will have been
reassigned in the interim.

## Current repo outcomes

The repo now carries reviews for the seven human pathway enzymes plus rat
Hmgcs2 and yeast ERG19. A 2026-10-04 check of those review YAMLs found no
`GO:1902767` rows. The obsolete `GO:0010142` rows are limited to the two rat
Hmgcs2 rows and the one yeast ERG19 row already handled in PR #3232.

| Gene | Relevant rows | Review outcome |
|---|---|---|
| human MVK, PMVK, MVD | two `GO:0019287` rows each | `ACCEPT`: the enzymes perform the mevalonate-to-IPP steps |
| human FDPS | two `GO:0045337` rows | `ACCEPT`: FDPS performs the IPP/GPP-to-FPP steps |
| human HMGCS1, HMGCR | no `GO:0010142`, `GO:1902767`, `GO:0019287` or `GO:0045337` rows | reviewed without an obsolete-term row |
| human IDI1 | no `GO:0010142`, `GO:1902767`, `GO:0019287` or `GO:0045337` rows | reviewed; IDI1 supports FPP synthesis indirectly by interconverting IPP and DMAPP |
| rat Hmgcs2 | two `GO:0010142` rows | `UNDECIDED`: obsoletion recorded, no replacement proposed because native mevalonate-pathway participation is unresolved |
| yeast ERG19 | one `GO:0010142` RCA row and one `GO:0019287` IEA row | obsolete RCA row `REMOVE`; `GO:0019287` is already `ACCEPT`ed |

## Replacement logic

The replacement choice is grouped by the step each enzyme catalyzes, not by
the obsolete source term:

1. Upper mevalonate-pathway enzymes whose direct output is IPP belong on
   `GO:0019287`: MVK, PMVK and MVD.
2. FDPS belongs on `GO:0045337`, because it condenses IPP/DMAPP through GPP
   to trans,trans-FPP.
3. Obsolete rows that already have a valid replacement in the same review
   should be removed rather than duplicated, as for yeast ERG19.
4. Mitochondrial ketogenic Hmgcs2 is not simply a cytosolic HMGCS1 row that
   needs remapping. Its native role remains unresolved with respect to
   mevalonate-pathway flux, so the old rows stay `UNDECIDED`.
5. E. coli uses the MEP/DXP pathway, not the mevalonate pathway, so a
   `GO:1902767` annotation on `yajO` would be a removal candidate rather than a
   remap candidate.

## Open follow-up

Repo-local obsolete rows have been handled. The remaining follow-up is to
identify the "1 EcoCyc" `GO:1902767` annotation still mentioned on the
upstream GO annotation ticket, confirm whether it is the historical E. coli
`yajO` row, and raise a GO annotation request if it still exists. That work is
tracked in [#1401](https://github.com/ai4curation/ai-gene-review/issues/1401).

## Status

- 2026-06-06 — Project file created. Tracking upstream issue #6440
  (opened 2026-05-28) and companion issue #6439. Obsoletion not yet
  applied. No reviews started; the rat HMGCS2 entry was then the only gene
  in this repo carrying an annotation to either obsoleting term.
- 2026-09-26 — OLS lists both GO:1902767 and GO:0010142 as obsolete, each
  pointing to GO:0019287 or GO:0045337. Human HMGCS1, HMGCR, MVK, PMVK, MVD
  (PR #1998) and FDPS, IDI1 (PR #2153) are reviewed. Rows on the obsolete
  terms remain in rat Hmgcs2 (IBA + IEA, UNDECIDED) and yeast ERG19 (RCA,
  KEEP_AS_NON_CORE).
- 2026-09-27 — Obsoletion is in the GO release 2026-07-26. PR #3232
  applied it: rat Hmgcs2 (two `UNDECIDED` GO:0010142 rows) now records the
  obsoletion in `reason` without proposing a replacement, since native
  mevalonate-pathway participation is unresolved; yeast ERG19's GO:0010142
  RCA row is `REMOVE`, because its only applicable replacement
  (GO:0019287) is already an `ACCEPT`ed row. No other review carries a
  GO:0010142 GOA row.
- 2026-10-04 — Re-read the nine current frontmatter reviews. MVK, PMVK and
  MVD each accept two `GO:0019287` rows; FDPS accepts two `GO:0045337` rows;
  HMGCS1, HMGCR and IDI1 carry neither obsolete term nor either replacement
  process; Hmgcs2 and ERG19 remain the only tracked reviews with obsolete
  `GO:0010142` rows, already handled as above.
