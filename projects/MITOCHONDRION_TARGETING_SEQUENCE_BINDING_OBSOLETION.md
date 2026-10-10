---
title: "Mitochondrion Targeting Sequence Binding — Obsoletion & Replacement"
maturity: SCOPING
last_reviewed: "2026-10-04"
tags: [OBSOLETION, FLAGSHIP]
species: [human, yeast, worm]
genes: [TOMM20, TOMM22, TOMM40, TOMM70, TIMM50, TIMM22, TIM22, TOM22, ACL4, tomm-22]
sidecars:
  slide_assets:
    - MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION/slides/import-route.svg
    - MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION/slides/term-map.svg
manifest:
  slides:
    - href: MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION/slides/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION-slides.html
      description: AI generated
---

# Mitochondrion Targeting Sequence Binding — Obsoletion & Replacement

**Bottom line:** Most mitochondrial proteins are imported by receptors of the
TOM and TIM complexes that recognise an N-terminal targeting presequence. GO
has obsoleted the generic binding term GO:0030943 *mitochondrion targeting
sequence binding* "in favor of more specific molecular functions", and the
receptor term the project was waiting for now exists as GO:0140436
*mitochondrial signal sequence receptor activity* (OLS, checked 2026-09-26).
We listed the 18 curated annotations on the old term and sorted them into
classes, because only the TOM receptors (and probably TIM50) are true
presequence receptors: the TIM23 and TIM22 channels, a plant phosphatase and
the TIM23 complex records need individual decisions, so upstream ruled out a
blanket `replaced_by`. In this repo, the local obsoletion set comprised 10
reviews: seven still preserve obsolete GOA source rows with `MODIFY`/`REMOVE`
reviews, and three receptor ortholog reviews added `NEW` GO:0140436 rows.
Five core functions now use GO:0140436. The local replacement pass is complete
after PR #3234 and later PAINT-aware re-reviews: receptors moved to GO:0140436;
human TOMM40/TIMM22 moved to GO:0008320 *protein transmembrane transporter
activity*; yeast TIM22 moved to GO:0032977 *membrane insertase activity*; and
yeast ACL4's stale IBA was removed rather than replaced. The per-row outcomes
are in Impact on this repo and Status below. The upstream triage of the yeast
TIM23 channel rows, Arabidopsis `PAP2`, and the TIM23 ComplexPortal rows is
GO-consortium work rather than local AI Gene Review work.

## Overview

GO has obsoleted the molecular-function term `GO:0030943 mitochondrion
targeting sequence binding` (defined as "Binding to a mitochondrion targeting
sequence, a specific peptide sequence that acts as a signal to localize the
protein within the mitochondrion"). The upstream rationale was that the curated
content is better captured by a **non-binding receptor activity** term rather
than a generic "binding" term, mirroring the existing nuclear/vacuolar pattern
(`GO:0061608 nuclear import signal receptor activity`,
`GO:0005049 nuclear export signal receptor activity`,
`GO:0010209 vacuolar sorting signal receptor activity`).

Crucially, the go-annotation curators note that **a simple `replaced_by`
cannot be applied**, because the existing annotations are *not only to the
receptor* — they span TOM cytosolic receptors, inner-membrane TIM
channel/receptor components, the TIM23 holo-complex, and at least one
non-canonical plant protein. Each annotation therefore needs individual review
to decide whether the new receptor MF is appropriate or whether a different
term (or removal) is the right outcome.

This is part of the broader mitochondrial-import GO-CAM reorganization
(go-ontology#31711) and is a sibling of the "signal sequence binding and
children" review (go-ontology#31419, which also drives the
`GO:0008139 nuclear localization sequence binding` obsoletion in
go-annotation#6435). It complements — but does not overlap with — the
BP-focused [[MITOCHONDRIAL_IMPORT_PATHWAYS]] project, which covers the import
*pathway* terms rather than this MF term.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6437](https://github.com/geneontology/go-annotation/issues/6437)
- Ontology ticket (NTR + obsoletion): [geneontology/go-ontology#32142](https://github.com/geneontology/go-ontology/issues/32142)
- Parent reorganization: [geneontology/go-ontology#31711](https://github.com/geneontology/go-ontology/issues/31711) (CLOSED — "Reorganization of mitochondrial import pathways based on GO-CAM modelling")
- Sibling "signal sequence binding" review: [geneontology/go-ontology#31419](https://github.com/geneontology/go-ontology/issues/31419)

## Upstream obsoletion outcome

| Obsoleted term | ID | Replacement / triage target |
|---|---|---|
| mitochondrion targeting sequence binding (MF) | GO:0030943 | GO:0140436 mitochondrial signal sequence receptor activity for presequence receptors; GO:0008320 protein transmembrane transporter activity or GO:0032977 membrane insertase activity for channels; removal for over-propagated rows |

Term labels verified in OLS on 2026-05-28:

- `GO:0030943` (`mitochondrion targeting sequence binding`) — live, slated for
  obsoletion. Parent is `GO:0005048 signal sequence binding`. Synonym:
  "mitochondrial targeting sequence binding".
- `GO:0005048` (`signal sequence binding`) — live parent MF.
- `GO:0061608` (`nuclear import signal receptor activity`) — live; the model
  the NTR is patterned on.
- `GO:0010209` (`vacuolar sorting signal receptor activity`) — live; analogous
  receptor MF.
- **`mitochondrial signal sequence receptor activity`** — the proposed NTR was
  **not yet present in OLS as of 2026-05-28** (no GO ID minted). This is the
  key open dependency: nothing can be remapped until the new MF is created.
  *Update 2026-09-26:* resolved. The NTR was minted as `GO:0140436`
  (`mitochondrial signal sequence receptor activity`, live in OLS) and
  GO:0030943 is now obsolete; see Status.

## Affected experimental / curated annotations (18)

Retrieved from the QuickGO annotation API on 2026-05-28
(`goId=GO:0030943`, manual / experimental + ComplexPortal NAS). Matches the
upstream group tally (ComplexPortal 4, FlyBase 2, HGNC-UCL 1, RGD 2, SGD 7,
TAIR 2 = 18).

| # | Source | Accession | Symbol | Organism | Evidence | Reference |
|---|---|---|---|---|---|---|
| 1 | RGD | UniProtKB:A4F267 | Tomm40l | Rat | IDA | PMID:17437969 |
| 2 | RGD | UniProtKB:Q62760 | Tomm20 | Rat | IDA | PMID:16511083 |
| 3 | SGD | UniProtKB:P07213 | TOM70 | *S. cerevisiae* | IMP | PMID:11054285 |
| 4 | SGD | UniProtKB:P32897 | TIM23 | *S. cerevisiae* | IDA | PMID:8858146 |
| 5 | SGD | UniProtKB:P32897 | TIM23 | *S. cerevisiae* | IMP | PMID:8858146 |
| 6 | SGD | UniProtKB:P35180 | TOM20 | *S. cerevisiae* | IDA | PMID:9252394 |
| 7 | SGD | UniProtKB:Q02776 | TIM50 | *S. cerevisiae* | IDA | PMID:18418384 |
| 8 | SGD | UniProtKB:Q02776 | TIM50 | *S. cerevisiae* | IDA | PMID:19144822 |
| 9 | SGD | UniProtKB:Q12328 | TIM22 | *S. cerevisiae* | IDA | PMID:11864609 |
| 10 | HGNC-UCL | UniProtKB:Q15388 | TOMM20 | Human | IDA | PMID:14557246 |
| 11 | FlyBase | UniProtKB:Q15388 | TOMM20 | Human | IDA | PMID:35733257 |
| 12 | FlyBase | UniProtKB:Q9NS69 | TOMM22 | Human | IDA | PMID:35733257 |
| 13 | TAIR | UniProtKB:Q9LMG7 | `PAP2` | *A. thaliana* | IPI | PMID:26304849 |
| 14 | TAIR | UniProtKB:Q9LMG7 | `PAP2` | *A. thaliana* | IPI | PMID:26304849 |
| 15 | ComplexPortal | ComplexPortal:CPX-539 | TIM23 complex (yeast) | *S. cerevisiae* | NAS | PMID:16107694 |
| 16 | ComplexPortal | ComplexPortal:CPX-6127 | TIM23 complex (yeast) | *S. cerevisiae* | NAS | PMID:16107694 |
| 17 | ComplexPortal | ComplexPortal:CPX-6129 | TIM23 complex (human) | Human | NAS | PMID:10339406 |
| 18 | ComplexPortal | ComplexPortal:CPX-6130 | TIM23 complex (human) | Human | NAS | PMID:10339406 |

Note: rows 11–12 carry `assignedBy=FlyBase` on human accessions — confirmed
directly from QuickGO, presumably a cross-organism assertion; flagged here for
the curator's awareness.

On 2026-05-28, before obsoletion, GO:0030943 had **~12,091 total
annotations** in QuickGO, overwhelmingly IEA (TreeGrafter, `GO_REF:0000118`)
and IBA (`GO_REF:0000033`). That volume illustrates how far a small set of
curated TOM-receptor annotations had propagated.

## Why a blanket `replaced_by` does not work

The annotations fall into biologically distinct classes, only some of which are
true presequence *receptors*:

- **Outer-membrane TOM targeting-signal handlers** — `TOMM20`/`TOM20`
  (human, rat and yeast) and `TOMM22` are the canonical cytosolic presequence
  receptors; yeast `TOM70` is a cytosolic receptor/adaptor for hydrophobic,
  chaperone-delivered precursors with internal targeting signals; rat
  `Tomm40l` is Tom40-like and should be triaged with channel/pore rows rather
  than assumed to be a presequence receptor.
- **Trans-side (IMS) receptor** — yeast `TIM50` hands the presequence from TOM
  to the TIM23 channel; receptor-like, the NTR likely fits.
- **Channel components** — yeast `TIM23` (presequence translocation channel).
  Whether a "receptor activity" MF is the right home, versus modelling TIM23 as
  a transporter that is an input to the matrix-import BP, needs curator input.
- **Carrier-pathway channel** — yeast `TIM22`. Carrier substrates (e.g.,
  metabolite carriers) use **internal** targeting signals, not cleavable
  N-terminal presequences. Annotating TIM22 to "mitochondrion targeting
  sequence binding" is already noted as a loose fit in this repo's
  `genes/yeast/TIM22` review; the new presequence-receptor MF may **not** be
  the correct replacement for TIM22.
- **Non-canonical / plant** — Arabidopsis `PAP2` (purple acid phosphatase 2,
  Q9LMG7), an IPI annotation (PMID:26304849). Needs individual review to decide
  whether a receptor MF applies at all.
- **Complex-level** — ComplexPortal TIM23 holo-complex entries (CPX-539,
  CPX-6127, CPX-6129, CPX-6130). Map to the complex's receptor/transporter
  activity once the NTR exists.

## Impact on this repo

Several affected gene products — or their human orthologs — already have
`*-ai-review.yaml` files that annotate `GO:0030943` (re-verified 2026-09-27):

| Gene | Path | Relation to affected set | Before local pass | Current outcome |
|---|---|---|---|---|
| TOMM20 (human, Q15388) | `genes/human/TOMM20` | Directly affected (rows 10–11) | IBA + IDA rows `ACCEPT`; core MF; also the `proposed_replacement_terms` target of the obsolete GO:0051082 row | IBA + IDA rows `MODIFY` → GO:0140436; core MF and the GO:0051082 row's replacement → GO:0140436 |
| TOMM22 (human, Q9NS69) | `genes/human/TOMM22` | Directly affected (row 12) | IDA row `ACCEPT`; core MF | IDA row `MODIFY` → GO:0140436; core MF → GO:0140436 |
| TOMM70 (human) | `genes/human/TOMM70` | Ortholog of affected yeast TOM70 | IBA + ISS rows `ACCEPT` | IBA + ISS rows `MODIFY` → GO:0140436 |
| TOMM40 (human) | `genes/human/TOMM40` | TOM channel; carries term via IBA | IBA row `ACCEPT` | IBA row `MODIFY` → GO:0008320 (channel) |
| TIM22 (yeast, Q12328) | `genes/yeast/TIM22` | Directly affected (row 9) | IBA + IDA rows `ACCEPT` | IBA + IDA rows `MODIFY` → GO:0032977 (membrane insertase activity) |
| TOM22 (yeast) | `genes/yeast/TOM22` | Ortholog of human TOMM22 | core MF only (no GOA row) | `NEW` GO:0140436 row; core MF → GO:0140436 |
| TIMM50 (human) | `genes/human/TIMM50` | Ortholog of affected yeast TIM50 | `NEW` row (NAS); core MF | `NEW` row and core MF → GO:0140436 |
| tomm-22 (worm) | `genes/worm/tomm-22` | Ortholog of human TOMM22 | `NEW` row (ISS); core MF | `NEW` row and core MF → GO:0140436 |
| TIMM22 (human) | `genes/human/TIMM22` | Ortholog of affected yeast TIM22 | IBA row `MARK_AS_OVER_ANNOTATED` | IBA row `MODIFY` → GO:0008320 (same PTN000364156 node as yeast TIM22) |
| ACL4 (yeast) | `genes/yeast/ACL4` | Not in curated set; IBA over-propagation | IBA row `UNDECIDED` (unresolved PAINT inference) | GO:0030943 and GO:0008320 IBA rows `REMOVE`; no replacement |

The first per-row remapping landed in #3234; later yeast TIM22 and ACL4
re-reviews refined the carrier channel to GO:0032977 and removed the stale ACL4
IBA rather than carrying it forward.

The receptor/channel split follows the classes above: GO:0140436 only for
the TOM presequence receptors and TIM50, GO:0008320 for the human
TOMM40/TIMM22 channels, GO:0032977 for yeast TIM22, and no replacement for
stale ACL4 propagation.

## Scope

- **GO branch:** Molecular Function (single term obsoletion + one NTR).
- **Organisms:** Human, rat, *Saccharomyces cerevisiae*, *Arabidopsis
  thaliana* (curated set); plus the large IEA/IBA tail across all eukaryotes.
- **Gene set:** TOM complex receptors (TOM20/TOMM20, TOMM22, TOM70/TOMM70,
  Tomm40l), TIM23-complex components (TIM23, TIM50), the TIM22 carrier channel,
  the TIM23 holo-complexes (ComplexPortal), and Arabidopsis `PAP2`.
- **Type of fix:** Curation hygiene / refactor. The biology is well established
  (TOM20/TOM22 are the canonical presequence receptors); the work is about
  moving from a generic "binding" MF to a precise "receptor activity" MF and
  triaging the annotations that are not really receptor functions.

## Local review outcomes

1. **TOMM20 / TOMM22 / TOMM70** — obsolete source rows now point to
   `GO:0140436`, with TOMM20 and TOMM22 also using it as the core MF.
2. **TIMM50 / TOM22 / tomm-22** — no preserved `GO:0030943` source row; `NEW`
   `GO:0140436` rows back the core MF.
3. **TOMM40 / TIMM22 / TIM22** — channel or insertase cases remapped away from
   the receptor MF.
4. **ACL4** — stale TOM70-family IBA propagation removed without replacement.

## Upstream-only rows still to triage

The remaining non-local records are the SGD TIM23 channel rows, Arabidopsis
`PAP2` (UniProtKB:Q9LMG7; no local review), and the TIM23 ComplexPortal rows.
Those are GO-consortium work rather than local AI Gene Review work, and are
the reason upstream avoided a blanket `replaced_by`.

The GO_Central IBA and TreeGrafter IEA pipelines will need to be reseeded
against the appropriate MF after obsoletion. The yeast `ACL4` review is the
concrete example of an IBA that should not be carried over: newer PAINT no
longer propagates the IBD to Acl4, and target-specific evidence supports
Rpl4-loop sequestration rather than mitochondrial targeting-sequence
recognition.

Coordinate with [[MITOCHONDRIAL_IMPORT_PATHWAYS]] so MF remapping and the BP
pathway model stay consistent for shared TOM/TIM genes.

## Priority

Medium. Only 18 curated annotations, and several of the key genes already have
reviews here, so the marginal curation effort was low once GO:0140436 was
minted. The receptor biology is uncontroversial, while SGD TIM23, Arabidopsis
`PAP2`, and TIM23 complex-level rows remain upstream case-by-case work. The
large IEA/IBA tail makes this more impactful than the very small obsoletions,
but no curator group is blocked waiting on AI Gene Review.

## Status

- 2026-05-28 — Project file created. Tracking go-annotation#6437 (opened
  2026-05-27) and go-ontology#32142 (closed; NTR + obsoletion request). The 18
  affected curated annotations were retrieved from QuickGO and reconciled
  against the upstream group tally. GO:0030943 confirmed live in OLS (parent
  `GO:0005048`); the proposed replacement MF
  `mitochondrial signal sequence receptor activity` is **not yet in OLS** — the
  key open dependency. Eight existing repo reviews already touch GO:0030943 and
  will need a MODIFY pass once the new term exists. No InterPro2GO / UniRule /
  UniProt-Keyword mappings to GO:0030943 were listed by upstream.
- 2026-09-26 — OLS lists GO:0030943 as obsolete, and the replacement
  GO:0140436 `mitochondrial signal sequence receptor activity` is live. Ten
  repo reviews touch GO:0030943: human TOMM20, TOMM22, TOMM40, TOMM70, TIMM50,
  TIMM22; yeast TIM22, TOM22, ACL4; worm tomm-22. Five list it in
  `core_functions` (TOMM20, TOMM22, TIMM50, tomm-22, TOM22). The local
  `cache/ontologies/go.tsv` still records GO:0030943 as live, so validation
  does not flag these yet. None of the reviews uses GO:0140436. TOMM20 also
  uses GO:0030943 as the `proposed_replacement_terms` target of its obsolete
  GO:0051082 (unfolded protein binding) row, so that replacement must also
  move to GO:0140436.
- 2026-09-26 — GO:0030943 is obsolete and the NTR is minted as `GO:0140436`
  `mitochondrial signal sequence receptor activity`. PR #3234 remapped the
  repo reviews. Receptors got `MODIFY` → GO:0140436: human TOMM20 (IDA, IBA),
  TOMM22 (IDA) and TOMM70 (IBA, ISS). Receptors with no GO:0030943 row got a
  `NEW` GO:0140436 row backing their core MF: human TIMM50, yeast TOM22 and worm
  tomm-22. Channels got `MODIFY` → `GO:0008320` protein transmembrane
  transporter activity, folded into the GO:0008320 annotation each gene already
  carries: human TOMM40 (IBA), yeast TIM22 (IDA, IBA) and human TIMM22 (IBA,
  same PTN000364156 node as yeast TIM22). Yeast ACL4 stays `UNDECIDED` with no
  replacement. This corrects the earlier "already `REMOVE`" description of ACL4.
  The SGD TIM23, `PAP2`, and ComplexPortal TIM23 cases remain open.
- 2026-10-04 — Re-audited the post-#3234 repo state. The ten genes in
  frontmatter are the exact local obsoletion set; adjacent human TIMM23 is now
  reviewed as a TIM23 channel but never carried GO:0030943. Receptors point
  obsolete rows or NEW rows to GO:0140436; human TOMM40/TIMM22 point obsolete
  rows to GO:0008320; yeast TIM22 points obsolete binding and transporter rows
  to GO:0032977; ACL4 removes stale GO:0030943 and GO:0008320 IBA rows without
  replacement.
  Related local tracker: [ai4curation/ai-gene-review#658](https://github.com/ai4curation/ai-gene-review/issues/658).
