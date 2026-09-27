---
title: "Peroxisome Targeting Signal Binding — Obsoletion & Replacement"
maturity: SCOPING
tags: [OBSOLETION]
species: [human]
genes: [PEX5, PEX7, PEX19]
---

# Peroxisome Targeting Signal Binding — Obsoletion & Replacement

**Bottom line:** Peroxisomal proteins are imported by cytosolic receptors
that recognise short targeting signals: PEX5 reads PTS1, PEX7 reads PTS2,
and PEX19 reads the membrane signal mPTS. GO has obsoleted the three
signal-specific binding terms (GO:0005052, GO:0005053, GO:0033328) as
"a specific substrate" and folded them into their parent GO:0000268, now
named *peroxisome signal sequence receptor activity*. We recorded the
upstream tickets and listed every review in this repo that uses the old
terms, so the reviews can be refreshed once GOA catches up. The change
has landed: OLS now shows all three terms as obsolete, so the "not yet
applied" status entry below is out of date. The refresh is fixed in
#3233 (open). 19 `existing_annotations` rows carry the obsolete ids
(PEX5 10, PEX7 7, PEX19 2, counting PEX19's GO:0036105 mPTS class-1
row). The 18 ACCEPT rows among them become MODIFY → GO:0000268 (PEX5 9,
PEX7 7, PEX19 2), and the PEX5 GO:0033328 IPI row stays UNDECIDED,
because PEX5 is not an mPTS receptor. Author-supplied ids (five
`proposed_replacement_terms` in PEX5 and PEX7, and PEX19's
`core_functions` MF GO:0036105) now point to GO:0000268. The biology
does not change.

## Overview

A GO obsoletion proposal will collapse three sibling "targeting signal binding"
terms into their parent (renamed to a receptor activity term). The rationale is
that these distinct signal sequences are recognized by the same receptor in each
case, so the precise sequence type is beyond GO's scope.

This project tracks the impact on AI Gene Review reviews and queues the affected
gene reviews for refresh once the obsoletion lands.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6401](https://github.com/geneontology/go-annotation/issues/6401)
- Ontology ticket: [geneontology/go-ontology#31419](https://github.com/geneontology/go-ontology/issues/31419)

## Obsoletion plan (per upstream)

Three terms to be obsoleted, replaced by their (renamed) parent:

| Obsoleted term | ID | Replacement |
|---|---|---|
| peroxisome matrix targeting signal-1 binding | GO:0005052 | parent of "peroxisome targeting sequence binding", to be renamed "peroxisome signal sequence receptor activity" |
| peroxisome matrix targeting signal-2 binding | GO:0005053 | same parent |
| peroxisome membrane targeting sequence binding | GO:0033328 | same parent |

Affected upstream annotations (from issue body): 45 total — AspGD 2, ComplexPortal 2,
GeneDB 1, SGD 5, UniProt 30, UniProt-extensions 5. Plus an InterPro mapping
IPR044536 → GO:0005053 that will need to be redirected.

## Impact on this repo

The obsoleted terms appear in three already-reviewed human genes (existing
`existing_annotations` entries that will need refresh once the obsoletion lands):

| Gene | UniProt | File | Affected term(s) | Notes |
|---|---|---|---|---|
| PEX5 | P50542 | `genes/human/PEX5/PEX5-ai-review.yaml` | GO:0005052 (multiple IDA, IBA), GO:0033328 (IPI) | PTS1 receptor; multiple IDA-supported entries |
| PEX7 | O00628 | `genes/human/PEX7/PEX7-ai-review.yaml` | GO:0005053 (IDA, IBA, IEA from InterPro IPR044536) | PTS2 receptor; receives the InterPro2GO mapping that also needs redirection |
| PEX19 | P40855 | `genes/human/PEX19/PEX19-ai-review.yaml` | GO:0033328 (IBA), GO:0036105 (IDA; also in `core_functions`) | Cytosolic PMP receptor/chaperone |

All three are fixed in #3233 (open): 18 ACCEPT rows → MODIFY to GO:0000268
(PEX5 9, PEX7 7, PEX19 2); PEX5 GO:0033328 IPI stays UNDECIDED with an
obsoletion note. GOA `term.id`s are left as GOA supplies them.

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

## Candidate genes for refresh (once obsoletion lands)

Initial set — genes already reviewed in this repo whose annotations cite one of
the three to-be-obsoleted terms:

1. PEX5 (human) — PTS1 receptor; primary affected gene with both GO:0005052 and GO:0033328 annotations.
2. PEX7 (human) — PTS2 receptor; affected by GO:0005053 obsoletion and the IPR044536 → GO:0005053 mapping.
3. PEX19 (human) — Cytosolic PMP receptor; affected by GO:0033328 obsoletion.

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
- 2026-09-26 — Refresh fixed in #3233 (open) for PEX5, PEX7 and PEX19:
  18 ACCEPT rows → MODIFY to GO:0000268 peroxisome signal sequence
  receptor activity; PEX5 GO:0033328 stays UNDECIDED; author-supplied
  ids repointed to GO:0000268. Maturity stays SCOPING until #3233 merges;
  the yeast/Aspergillus orthologs remain optional.

## Slides

- [Slides](PEROXISOME_TARGETING_SIGNAL_OBSOLETION/slides/PEROXISOME_TARGETING_SIGNAL_OBSOLETION-slides.html) (Marp source: [PEROXISOME_TARGETING_SIGNAL_OBSOLETION-slides.md](PEROXISOME_TARGETING_SIGNAL_OBSOLETION/slides/PEROXISOME_TARGETING_SIGNAL_OBSOLETION-slides.md)) — AI generated
