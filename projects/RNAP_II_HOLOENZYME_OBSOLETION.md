---
title: "RNA Polymerase II Holoenzyme (GO:0016591) Obsoletion"
maturity: SCOPING
tags: [OBSOLETION]
species: [human, yeast, SCHPO]
collections: [GO_TRACKER_BACKLOG]
index_group: GO_TRACKER_BACKLOG
---

# RNA Polymerase II Holoenzyme (GO:0016591) Obsoletion

**Bottom line:** The oldest open content issue on the GO tracker (opened
2013-09-06) asks to obsolete GO:0016591 *RNA polymerase II, holoenzyme*.
The reason: "holoenzyme" names many different purifications, with no
consistent composition. An obsoletion notice went out in 2018, and in
January 2023 an editor set four action points, but the reporter disagreed
about the "consider" target and the thread stopped. Two separate things
block it in go-edit.obo. GO:0005665 *RNA polymerase II, core complex* is
logically defined as part_of GO:0016591. Seven general-factor complexes
(TFIIA, TFIID, TFIIE, TFIIF, TFIIH, Paf1, TFTC) still hang off the term by
part_of. Only one reviewed gene here carries the term (GTF2F2, as an IEA kept
non-core), so this project is mostly about the subcomplex members, not
repairing our reviews. Scoped, not started.

## Upstream ticket

| Issue | Opened | Last substantive comment |
|---|---|---|
| [go-ontology#10556](https://github.com/geneontology/go-ontology/issues/10556) | 2013-09-06 | 2023-01-17 |

Related:
[go-ontology#15870](https://github.com/geneontology/go-ontology/issues/15870)
(closed), the transcription group's proposal to merge the term into the
preinitiation complex. Thread summary as of 2026-11-16, and term states from
a go-ontology checkout of 2026-11-12. Nothing has been posted to either issue.

## Where the thread stands

- **The problem** (2013-09-06): "The phrase "RNAP II holoenzyme" is used by
  lots of people for many different "purifications" making it impossible to
  define a consistent composition."
- **2018:** an obsoletion notice listed 46 manual annotations (28
  experimental) and one InterPro mapping. An MGI editor pointed out that an
  earlier redefinition had broadened the term, but the invalid part_of links
  were never removed.
- **2023-01-13 action points:**
  1. obsolete GO:0016591 with consider GO:0097550 *transcription
     preinitiation complex*;
  2. move GO:0097550 under GO:0055029;
  3. move the holoenzyme's children under the preinitiation complex;
  4. redefine GO:0055029.

  The same editor reported the annotations fixed and the InterPro mapping
  passed on.
- **The reporter's objection** (2023-01-17): "what we really need as a
  consider term for GO:0016591 RNAP II holoenzyme would be "RNA polymerase II
  transcription preinitiation complex"". They also asked that GO:0055029 be
  left unchanged. No reply since.

In go-edit.obo:

- None of the four action points is done.
- GO:0016591 is live, is_a GO:0055029.
- GO:0097550 is live and generic (no RNA polymerase II-specific
  preinitiation complex exists).
- GO:0005665's logical definition still uses part_of GO:0016591.
- GO:0005669, GO:0005672, GO:0005673, GO:0005674, GO:0005675, GO:0016593
  and GO:0033276 still carry part_of GO:0016591.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0016591 RNA polymerase II, holoenzyme | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0097550 transcription preinitiation complex | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0005665 RNA polymerase II, core complex | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0005669 transcription factor TFIID complex | 2 | 2 | 0 | 0 | 2 | 0 | 0 | 0 |  | 0 |
| GO:0005674 transcription factor TFIIF complex | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0005675 transcription factor TFIIH holo complex | 14 | 6 | 13 | 0 | 0 | 0 | 1 | 0 |  | 2 |
| GO:0016593 Cdc73/Paf1 complex | 8 | 2 | 6 | 0 | 0 | 0 | 2 | 0 |  | 1 |
| GO:0033276 transcription factor TFTC complex | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |

The reviewed genes are human GTF2F2 (holoenzyme IEA, kept non-core;
TFIIF ACCEPT), CDK7, ERCC2, ERCC3 (TFIIH; ERCC3 also on the preinitiation
complex), CDC73 (Paf1), ATXN7 (TFTC), HORSE CDK7 and SCHPO mcs6. No RNA
polymerase II subunit (POLR2A-L) and no Mediator subunit is reviewed.

## What gene review can and cannot settle

- **Can settle, per gene:** the specific complex each former holoenzyme
  annotation should point to (core polymerase, a general factor, Mediator,
  Paf1, the preinitiation complex), from the experimental evidence. This is
  the re-annotation the 2018 notice needed.
- **Can document:** whether the reviewed subcomplex members' evidence is for
  a DNA-bound preinitiation complex or a free holoenzyme-like assembly. That
  is the reporter's distinction between the two consider targets.
- **Cannot settle:** the GO:0005665 logical definition, the choice of consider
  term, or whether an RNA polymerase II-specific preinitiation complex term is
  created. These are editor decisions.

## Plan

- [ ] Re-check human/GTF2F2: replace the holoenzyme IEA judgement with the
      TFIIF row as core, and record the obsoletion in the review.
- [ ] Re-check ERCC2 (TFIID MODIFY) and ERCC3 (TFIID MODIFY, preinitiation
      complex ACCEPT) for consistency with the TFIIH rows.
- [ ] New reviews, chosen from the genes named in #15870. Check each for a
      GO:0016591 row in GOA before starting; the 2018 notice listed 46 manual
      rows across all species.
  - [ ] human POLR2M, RPAP2, RPRD1A, RPRD1B;
  - [ ] SCHPO rpb3, rpb4, rpb7;
  - [ ] yeast IWR1.
- [ ] Note for the issue owners: which reviewed genes would lose their only
      complex term if GO:0016591 goes. Posting it is the project lead's
      decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No reviews started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Thread and
  #15870 read in full.
- The live blocker is the disagreement over the consider target, not the
  annotations, which an editor reported fixed in 2023.
