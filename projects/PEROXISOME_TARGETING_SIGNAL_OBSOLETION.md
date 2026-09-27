---
title: "Peroxisome Targeting Signal Binding — Obsoletion & Replacement"
maturity: COMPLETE
tags: [OBSOLETION]
species: [human]
genes: [PEX5, PEX7, PEX19]
---

# Peroxisome Targeting Signal Binding — Obsoletion & Replacement

**Bottom line:** Peroxisomal proteins are imported by cytosolic receptors
that recognise short targeting signals: PEX5 reads PTS1, PEX7 reads PTS2,
and PEX19 reads the membrane signal mPTS. GO release 2026-07-26 obsoleted
four signal-specific binding terms (GO:0005052, GO:0005053, GO:0033328
and its child GO:0036105) as "a specific substrate", each with
`replaced_by` GO:0000268, now named *peroxisome signal sequence receptor
activity*. We recorded the upstream tickets and listed every review in
this repo that uses the old terms. The refresh was merged in #3233.
19 `existing_annotations` rows carry the obsolete ids (PEX5 10, PEX7 7,
PEX19 2, counting PEX19's GO:0036105 IDA row). The 18 ACCEPT rows among
them become MODIFY → GO:0000268 (PEX5 9, PEX7 7, PEX19 2), and the PEX5
GO:0033328 IPI row stays UNDECIDED, because PEX5 is not an mPTS receptor.
Of the five author-supplied `proposed_replacement_terms` that used the
obsolete ids, three now point to GO:0000268. The two on generic
protein-binding rows were dropped instead, because a peroxin–peroxin
contact is not signal-sequence recognition: PEX5 PMID:10562279 (PEX12/PEX10
contact) becomes MARK_AS_OVER_ANNOTATED and PEX7 PMID:11546814 (PEX5L
co-receptor contact) becomes REMOVE. PEX19's `core_functions` MF
GO:0036105 becomes GO:0000268. The Proposed approach and Priority
sections below still describe the plan as it stood before the obsoletion
("Wait for obsoletion to land", "Do not pre-emptively edit reviews"); the
obsoletion, impact and refreshed-genes sections have been updated to the
four applied terms and the #3233 outcome. The body's predictions that the
refresh would be purely mechanical ("the underlying biology is unchanged", "The biological
conclusion should not change", "mechanical ... rather than scientific")
held for the 19 rows annotated to the obsoleted terms, but not for the
two protein-binding rows whose replacements were dropped above: there
the refresh changed the action, because the contact is not signal
recognition.

## Overview

A GO obsoletion (go-ontology#31419, closed 2026-05-28; applied in GO release
2026-07-26) collapsed four sibling "targeting signal binding" terms into
their parent GO:0000268, renamed "peroxisome signal sequence receptor
activity". The rationale is
that these distinct signal sequences are recognized by the same receptor in each
case, so the precise sequence type is beyond GO's scope.

This project tracked the impact on AI Gene Review reviews and the refresh of the
affected gene reviews.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6401](https://github.com/geneontology/go-annotation/issues/6401)
- Ontology ticket: [geneontology/go-ontology#31419](https://github.com/geneontology/go-ontology/issues/31419)

## Obsoletion (applied in GO release 2026-07-26)

Four terms obsoleted, each with `replaced_by: GO:0000268` (checked against OLS4,
2026-09-26):

| Obsoleted term | ID | Replacement |
|---|---|---|
| peroxisome matrix targeting signal-1 binding | GO:0005052 | GO:0000268, formerly "peroxisome targeting sequence binding", renamed "peroxisome signal sequence receptor activity" |
| peroxisome matrix targeting signal-2 binding | GO:0005053 | same parent |
| peroxisome membrane targeting sequence binding | GO:0033328 | same parent |
| peroxisome membrane class-1 targeting sequence binding | GO:0036105 | same parent (was a child of GO:0033328) |

Affected upstream annotations (from issue body): 45 total — AspGD 2, ComplexPortal 2,
GeneDB 1, SGD 5, UniProt 30, UniProt-extensions 5. Plus an InterPro mapping
IPR044536 → GO:0005053 that will need to be redirected.

## Impact on this repo

The obsoleted terms appear in three already-reviewed human genes; all three were
refreshed in PR #3233:

| Gene | UniProt | File | Affected term(s) | Notes |
|---|---|---|---|---|
| PEX5 | P50542 | `genes/human/PEX5/PEX5-ai-review.yaml` | GO:0005052 (multiple IDA, IBA), GO:0033328 (IPI) | PTS1 receptor; multiple IDA-supported entries |
| PEX7 | O00628 | `genes/human/PEX7/PEX7-ai-review.yaml` | GO:0005053 (IDA, IBA, IEA from InterPro IPR044536) | PTS2 receptor; receives the InterPro2GO mapping that also needs redirection |
| PEX19 | P40855 | `genes/human/PEX19/PEX19-ai-review.yaml` | GO:0033328 (IBA), GO:0036105 (IDA; also in `core_functions`) | Cytosolic PMP receptor/chaperone |

All three are fixed in #3233: 18 ACCEPT rows → MODIFY to GO:0000268
(PEX5 9, PEX7 7, PEX19 2); PEX5 GO:0033328 IPI stays UNDECIDED with an
obsoletion note; two generic protein-binding rows whose replacement pointed
at an obsolete id become MARK_AS_OVER_ANNOTATED (PEX5) and REMOVE (PEX7). GOA `term.id`s are left as GOA supplies them.

These genes are already part of the broader [PEROXISOME](PEROXISOME.md) project.

## Scope

- Organism: primarily human in this repo, but obsoletion is species-agnostic
  (yeast SGD, AspGD, ComplexPortal entries are also impacted upstream).
- GO branch: molecular function — receptor/binding activities of the matrix and
  membrane import pathways.
- Type of fix: terminological/structural in GO — the underlying biology is
  unchanged; reviews need their term IDs and labels refreshed and the merged
  parent term should be evaluated for whether it captures the receptor function
  as well or better than the children did.

## Genes refreshed

Initial set — genes already reviewed in this repo whose annotations cite one of
the four obsoleted terms:

1. PEX5 (human) — done (PR #3233). GO:0005052 rows → MODIFY to GO:0000268 (already held by IDA); GO:0033328 IPI row kept UNDECIDED.
2. PEX7 (human) — done (PR #3233). GO:0005053 rows → MODIFY to GO:0000268.
3. PEX19 (human) — done (PR #3233). GO:0033328 rows and the GO:0036105 core_functions MF → GO:0000268.

Additional candidates to consider once the obsoletion is applied (not yet in
this repo, but flagged by the upstream tally — do not add without verifying via
`just fetch-gene`):

4. SGD: Pex5p/Pex7p/Pex19p (S. cerevisiae orthologs) — the issue lists 5 SGD annotations.
5. AspGD: Aspergillus PEX5/PEX7 orthologs — 2 annotations.
6. GeneDB / ComplexPortal entries referenced by the upstream spreadsheet.

## Proposed approach

1. **Wait for obsoletion to land.** The decision is not yet final — comment
   thread on go-ontology#31419 should be monitored. Do not pre-emptively edit
   reviews against terms that may still survive.
2. **After obsoletion**, regenerate GOA files for PEX5, PEX7, PEX19 with
   `just fetch-gene human <gene>`; the merged parent term should appear in
   place of the obsoleted children.
3. **Re-review the affected `existing_annotations` entries.** The biological
   conclusion should not change (the receptors still bind their cognate
   signals), but action codes may need updating where reviews previously
   accepted the more specific child term as core function. Consider whether
   the renamed parent ("peroxisome signal sequence receptor activity") is an
   appropriate ACCEPT for core_functions, or whether a more informative MF
   term should be proposed.
4. **InterPro2GO mapping** — flag for upstream that IPR044536 will need
   redirection to the merged parent (this is upstream's responsibility, not
   ours, but worth noting in PEX7 review).
5. **Decide on yeast/Aspergillus orthologs.** If the broader peroxisome
   project expands beyond human, add SGD/AspGD orthologs at that point rather
   than as part of this obsoletion-tracking work.

## Priority

Low/medium — passive tracking until the obsoletion is approved and applied.
The biology of the affected reviews is well-characterized and the change is
mechanical (term ID/label refresh) rather than scientific.

## Status

- 2026-05-01 — Project file created, tracking upstream issue #6401 (opened
  same day). Obsoletion not yet applied. No review edits required at this time.
- 2026-09-26 — Obsoletion applied upstream (GO release 2026-07-26; GO:0036105 was
  obsoleted too). PEX5, PEX7 and PEX19 refreshed in PR #3233, including review
  prose that cited the obsolete ids. Yeast/Aspergillus orthologs remain out of scope.
- 2026-09-26 — Row-level outcome of the #3233 refresh for PEX5, PEX7 and PEX19:
  18 ACCEPT rows → MODIFY to GO:0000268 peroxisome signal sequence
  receptor activity; PEX5 GO:0033328 stays UNDECIDED; three of five
  `proposed_replacement_terms` and PEX19's core MF repointed to
  GO:0000268, and two peroxin–peroxin protein-binding rows dropped their
  replacement (PEX5 → MARK_AS_OVER_ANNOTATED, PEX7 → REMOVE).
  With #3233 merged, maturity is COMPLETE; the yeast/Aspergillus orthologs remain optional.

## Slides

- [Slides](PEROXISOME_TARGETING_SIGNAL_OBSOLETION/slides/PEROXISOME_TARGETING_SIGNAL_OBSOLETION-slides.html) (Marp source: [PEROXISOME_TARGETING_SIGNAL_OBSOLETION-slides.md](PEROXISOME_TARGETING_SIGNAL_OBSOLETION/slides/PEROXISOME_TARGETING_SIGNAL_OBSOLETION-slides.md)) — AI generated
