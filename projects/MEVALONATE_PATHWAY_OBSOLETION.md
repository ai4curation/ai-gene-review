# Mevalonate Pathway Term Cleanup — Obsoletion & Replacement

## Overview

A GO ontology cleanup proposes to obsolete two overlapping "mevalonate pathway"
terms in favour of better-scoped existing terms. The two terms describe the
same biology already covered by `GO:0019287 isopentenyl diphosphate biosynthetic
process, mevalonate pathway` and/or `GO:0045337 farnesyl diphosphate biosynthetic
process`, so existing annotations need to be redirected (with evidence review)
rather than carried on stale terms.

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
| farnesyl diphosphate biosynthetic process, mevalonate pathway | GO:0010142 | consider `GO:0019287 isopentenyl diphosphate biosynthetic process, mevalonate pathway` or `GO:0045337 farnesyl diphosphate biosynthetic process` |

Verify all term IDs and labels in OLS before acting; the obsoletion is still
under discussion upstream at the time of this file.

The replacement is not a single 1:1 swap — `GO:1902767` and `GO:0010142` both
describe a multi-step pathway that runs through mevalonate to IPP and then on
to FPP. After obsoletion, each annotation needs to land on whichever of the
two replacement terms (or both) accurately describes the actual reaction(s)
that the experiment supports. That is a scientific judgement, not a mechanical
relabel.

## Affected annotations — upstream counts

From the ontology issue (geneontology/go-ontology#32082):

| Term | Direct EXP annotations | Genes listed in upstream |
|---|---|---|
| GO:1902767 (this issue) | 2 | erg9, yajO |
| GO:0010142 (companion #6439) | 21 | fps1, dps1, spo9, ERG12, ERG8, hcs1, Idi1, Hmgcr, Acat2, Hmgcs1, Fdps, Mvd, ACAT2, Pmvk, Mvk, hmgr |

Per #6440's body, the GO:1902767 list is now down to "1 EcoCyc" annotation
(the PomBase entry was already fixed). The exact remaining EcoCyc gene/PMID
is in the linked spreadsheet, which is gated behind Google sign-in and
should be retrieved via QuickGO when work starts.

For GO:0010142 (companion #6439), the full set should be re-pulled from
QuickGO at review time — many of the 21 listed genes will have been
reassigned in the interim.

## Impact on this repo

Scanning `genes/**/*-goa.tsv` for either GO ID returned a single hit:

- `genes/rat/Hmgcs2/Hmgcs2-goa.tsv` — rat HMGCS2 has two existing IBA/IEA
  annotations to `GO:0010142`, and the `Hmgcs2-notes.md` already flags both
  as inappropriate (paralog conflation with cholesterol-pathway HMGCS1).
  The existing review is consistent with the obsoletion direction.

None of the other listed genes (erg9, yajO, fps1, dps1, spo9, ERG12, ERG8,
hcs1, Idi1, Hmgcr, Fdps, Mvd, ACAT2, Pmvk, Mvk, hmgr, Hmgcs1, Acat2) have an
`*-ai-review.yaml` in this repo at the time of this writing.

## Scope

- Organism: cross-organism. Upstream lists yeast (ERG12, ERG8, Erg9, hcs1),
  fission yeast (fps1, dps1, spo9, hcs1 paralogs), mammalian (Hmgcr / Hmgcs1
  / Mvk / Mvd / Pmvk / Fdps / Acat2 / Idi1 / ACAT2 / hmgr / Hmgcs2), and
  bacterial (yajO).
- GO branch: biological process — sterol/isoprenoid precursor biosynthesis
  via the mevalonate route.
- Type of fix: scientific — for each annotation, decide whether the
  experiment supports `GO:0019287 (mevalonate-pathway IPP)`,
  `GO:0045337 (FPP biosynthesis)`, or one of the other neighbouring terms
  (`GO:0006695 cholesterol biosynthetic process`,
  `GO:0008299 isoprenoid biosynthetic process`,
  `GO:0010142 → replacement`, etc.) and pick the closest fit.

## Candidate genes for initial review

Listed in priority order. Each should be set up with
`just fetch-gene <organism> <gene>` before review begins.

1. **HMGCS1 (human, Q01581)** — Cytosolic HMG-CoA synthase, canonical entry
   to the mevalonate pathway in the cholesterol/isoprenoid branch. A clean
   reference for what `GO:0019287` should look like and a strong candidate
   for the `GO:0019287` replacement for any current `GO:0010142` annotation.
2. **MVK / MVD / PMVK (human)** — The three "pure mevalonate-to-IPP"
   enzymes. Strong candidates for `GO:0019287` replacement; useful as a
   batch because the same logic applies to all three.
3. **FDPS (human, P14324)** — Farnesyl diphosphate synthase. Catalyses the
   IPP → GPP → FPP steps, so any `GO:0010142` annotation here actually
   belongs on `GO:0045337 farnesyl diphosphate biosynthetic process` rather
   than the obsoleting term.
4. **HMGCR (human, P04035)** — HMG-CoA reductase. The rate-limiting step
   of the mevalonate route; likely annotated to `GO:0010142` but really
   covers only the upper (mevalonate-formation) half of the pathway. Worth
   a careful review because HMGCR is also heavily studied for
   statin/cholesterol biology and its non-pathway annotations should be
   left untouched.
5. **HMGCS2 (rat, P22791) — already in repo.** Two existing IBA/IEA
   `GO:0010142` annotations are already flagged for removal in
   `Hmgcs2-notes.md` because of paralog conflation with the cytosolic
   HMGCS1. The review file can be updated to record the obsoletion
   rationale in the `review.reason` for those two annotations.
6. **ERG9 / ERG12 / ERG8 (yeast)** — Yeast mevalonate-pathway enzymes,
   upstream-listed for both terms. Lower priority because the yeast
   annotations are already curator-maintained.
7. **yajO (E. coli)** — Listed under GO:1902767 in the ontology issue.
   The yajO assignment to a mevalonate pathway is dubious (E. coli uses
   the MEP/DXP pathway, not the mevalonate pathway). Worth a quick check
   to confirm whether this is the remaining "1 EcoCyc" annotation flagged
   in #6440.

## Proposed approach

1. **Wait for the obsoletion to land before bulk-rewriting.** GO ontology
   ticket #32082 is still under discussion. AI Gene Review reviews can
   proceed on the underlying biology now and record the currently-live
   term ID; the action codes (ACCEPT vs MODIFY vs REMOVE) are independent
   of whether the obsoletion has merged.
2. **Group the review by replacement target, not by the obsoleting term.**
   Genes whose experimental evidence supports the upper half of the
   pathway (mevalonate → IPP) want `GO:0019287`; genes covering the lower
   half (IPP → FPP) want `GO:0045337`; some may want both. Trying to
   review "every annotation to GO:0010142" without that split conflates
   two different replacements.
3. **Reuse Hmgcs2 as the worked example.** The existing
   `genes/rat/Hmgcs2/Hmgcs2-ai-review.yaml` already records the
   paralog-conflation logic that motivates the obsoletion. Updating its
   `review.reason` fields with explicit reference to this project is a
   useful first concrete step.
4. **Watch out for the bacterial annotation.** E. coli does not use the
   mevalonate pathway, so a `GO:1902767` annotation on yajO (or any other
   E. coli protein) is almost certainly wrong rather than just misnamed.
   This is a removal candidate, not a remap candidate.

## Priority

Low–medium — the per-annotation review work here is small (the upstream
lists are short and several entries have already been fixed at source).
The main repo-level effect is updating the rat HMGCS2 review to cite the
obsoletion rationale; the rest is queueing work for when human
HMGCS1/MVK/MVD/PMVK/FDPS/HMGCR enter the review cycle.

## Status

- 2026-06-06 — Project file created. Tracking upstream issue #6440
  (opened 2026-05-28) and companion issue #6439. Obsoletion not yet
  applied. No reviews started; the rat HMGCS2 entry is the only gene in
  this repo currently carrying an annotation to either obsoleting term.
