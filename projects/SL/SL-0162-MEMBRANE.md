---
title: "SL-0162 Membrane"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, mouse, worm, yeast, ANOGA, DANRE, DROME, SCHPO, DORPE]
autolink_gene_symbols: false
---

# SL-0162 Membrane → GO:0016020

The largest under-specified subcellular location in the corpus, and the cleanest example of
the SL project's [core finding](../SL.md). 61 SL-unique annotations reviewed; **19 carry a
hard issue (31%)** — the highest rate of any location above n=10.

## What the reviewers actually objected to

Every single flagged case is the same complaint, stated in different words: the term is true
and useless. A sample, verbatim from `review.reason`:

| gene | verdict | reviewer's words |
|---|---|---|
| human PET100 | MARK_OVER | "'membrane' is an unspecific location that adds no information beyond the more precise GO:0005743 … It reflects the generic single-pass-membrane-protein SubCell keyword rather than a distinct localization." |
| yeast DCV1 | MARK_OVER | "a bona fide integral membrane protein … so the annotation is not wrong, but 'membrane' is the uninformative parent of the more specific compartment terms already present" |
| worm daf-2 | MODIFY | "too general. The more specific term plasma membrane (GO:0005886) is already annotated" |
| human ABHD14A | MARK_OVER | "Marked over-annotated for lack of specificity rather than for lack of membrane association" |
| human GP9 | MODIFY | "While 'membrane' is technically correct, this term is too general." |

Not one flagged case disputes that the protein is in a membrane. **`GO:0016020` is being
flagged for what it fails to say.**

Where reviewers proposed a replacement, it was always a specific compartment already implied
by the protein's topology or known biology: ER membrane (DANRE cyp51, worm atf-6, yeast
PHO86, human DNAJC25), plasma membrane (worm daf-2, mouse Egf, human GP9), lysosomal
membrane (human ATP6V0E1), mitochondrial inner membrane (human PET100).

## Batch reviewed under this subproject

Five annotations moved `ACCEPT` → `MARK_AS_OVER_ANNOTATED`, selected as the clearest cases:
SL-unique, and the gene already carries a strictly more specific CC term from independent
(non-SL) evidence.

| gene | already carries | source |
|---|---|---|
| human DNAJC25 | GO:0005789 endoplasmic reticulum membrane | IBA |
| human IL2RA | GO:0005893 interleukin-2 receptor complex; GO:0009897 external side of plasma membrane | TAS |
| human FGFRL1 | GO:0005886 plasma membrane | IBA |
| ANOGA TOLL9 | GO:0005886 plasma membrane | IBA |
| yeast MCH2 | GO:0005886 plasma membrane | IBA |

`MARK_AS_OVER_ANNOTATED` rather than `MODIFY`: the precise term is already present, so there
is nothing to replace the broad one with. Knock-on edit: DNAJC25's `core_functions.locations`
listed `GO:0016020` and now lists `GO:0005789`.

One candidate was dropped after checking — yeast MNT4 has no independent more-specific CC
term, so the broad annotation is the only thing placing it anywhere.

## What this subproject does *not* show

The obvious mechanical fix — suppress an SL-derived CC term when the gene already carries a
descendant — **does not work**. See the [redundancy test](../SL.md#the-redundancy-hypothesis-tested-and-refuted):
across the whole corpus, redundant SL-unique annotations were flagged at a rate barely
distinguishable from non-redundant ones. Within SL-0162 itself, before this batch, redundant
cases ran 26% and non-redundant 19% — a gap, but nothing like the clean separation the rule
would need.

The reason is visible in the reviewer quotes above: ABHD14A and DCV1 were flagged for
*vagueness*, not duplication. A gene whose only annotation is `membrane` is just as
uninformatively annotated as one that has `membrane` plus five specific terms — arguably
worse. Deduplication would fix the second case and miss the first.
