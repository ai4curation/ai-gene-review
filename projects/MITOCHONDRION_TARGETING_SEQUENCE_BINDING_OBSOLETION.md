# Mitochondrion Targeting Sequence Binding — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will obsolete the molecular-function term
`GO:0030943 mitochondrion targeting sequence binding` (defined as "Binding to a
mitochondrion targeting sequence, a specific peptide sequence that acts as a
signal to localize the protein within the mitochondrion"). The upstream
rationale is that the curated content is better captured by a **non-binding
receptor activity** term rather than a generic "binding" term: the ontology
ticket proposes a New Term Request (NTR) for
**`mitochondrial signal sequence receptor activity`** as the replacement,
mirroring the existing nuclear/vacuolar pattern
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

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Proposed replacement |
|---|---|---|
| mitochondrion targeting sequence binding (MF) | GO:0030943 | NTR `mitochondrial signal sequence receptor activity` (a *receptor*, non-binding MF) — applied per-annotation, not as a blanket `replaced_by` |

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
| 13 | TAIR | UniProtKB:Q9LMG7 | PAP2 | *A. thaliana* | IPI | PMID:26304849 |
| 14 | TAIR | UniProtKB:Q9LMG7 | PAP2 | *A. thaliana* | IPI | PMID:26304849 |
| 15 | ComplexPortal | ComplexPortal:CPX-539 | TIM23 complex (yeast) | *S. cerevisiae* | NAS | PMID:16107694 |
| 16 | ComplexPortal | ComplexPortal:CPX-6127 | TIM23 complex (yeast) | *S. cerevisiae* | NAS | PMID:16107694 |
| 17 | ComplexPortal | ComplexPortal:CPX-6129 | TIM23 complex (human) | Human | NAS | PMID:10339406 |
| 18 | ComplexPortal | ComplexPortal:CPX-6130 | TIM23 complex (human) | Human | NAS | PMID:10339406 |

Note: rows 11–12 carry `assignedBy=FlyBase` on human accessions — confirmed
directly from QuickGO, presumably a cross-organism assertion; flagged here for
the curator's awareness.

On top of these 18 curated records, GO:0030943 currently has **~12,091 total
annotations** (QuickGO, 2026-05-28), overwhelmingly IEA (TreeGrafter,
`GO_REF:0000118`) and IBA (`GO_REF:0000033`). These will be retired/redirected
automatically once the term is obsoleted, but the volume illustrates how far a
small set of curated TOM-receptor annotations has propagated.

## Why a blanket `replaced_by` does not work

The annotations fall into biologically distinct classes, only some of which are
true presequence *receptors*:

- **Cytosolic TOM receptors** — `TOMM20`/`TOM20` (human/rat/yeast), `TOMM22`,
  rat `Tomm40l`, yeast `TOM70`. These directly recognize the amphipathic
  N-terminal presequence on the cytosolic face. The NTR
  `mitochondrial signal sequence receptor activity` is a clean fit here.
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
`*-ai-review.yaml` files that annotate `GO:0030943` (verified 2026-05-28):

| Gene | Path | Relation to affected set | Current handling of GO:0030943 |
|---|---|---|---|
| TOMM20 (human, Q15388) | `genes/human/TOMM20` | Directly affected (rows 10–11) | `ACCEPT` (core MF — presequence receptor) |
| TOMM22 (human, Q9NS69) | `genes/human/TOMM22` | Directly affected (row 12) | present (IDA + IBA) |
| TIM22 (yeast, Q12328) | `genes/yeast/TIM22` | Directly affected (row 9) | retained as "best available", with a caveat that the term is broader than the internal-signal binding it actually does |
| TOMM70 (human) | `genes/human/TOMM70` | Ortholog of affected yeast TOM70 | present (IBA) |
| TOMM40 (human) | `genes/human/TOMM40` | TOM channel; carries term via IBA | present (IBA) |
| TIMM50 (human) | `genes/human/TIMM50` | Ortholog of affected yeast TIM50 | present |
| TIMM22 (human) | `genes/human/TIMM22` | Ortholog of affected yeast TIM22 | present |
| ACL4 (yeast) | `genes/yeast/ACL4` | Not in curated set; IBA over-propagation | already `REMOVE` (Acl4 is an Rpl4 chaperone; no MTS binding) — a worked example of the IBA fallout |

When the obsoletion + NTR land, these reviews will need a `MODIFY` pass:
remap the TOM-receptor annotations to the new
`mitochondrial signal sequence receptor activity` MF, and handle TIM22 and any
complex/plant cases per the considerations above.

## Scope

- **GO branch:** Molecular Function (single term obsoletion + one NTR).
- **Organisms:** Human, rat, *Saccharomyces cerevisiae*, *Arabidopsis
  thaliana* (curated set); plus the large IEA/IBA tail across all eukaryotes.
- **Gene set:** TOM complex receptors (TOM20/TOMM20, TOMM22, TOM70/TOMM70,
  Tomm40l), TIM23-complex components (TIM23, TIM50), the TIM22 carrier channel,
  the TIM23 holo-complexes (ComplexPortal), and Arabidopsis PAP2.
- **Type of fix:** Curation hygiene / refactor. The biology is well established
  (TOM20/TOM22 are the canonical presequence receptors); the work is about
  moving from a generic "binding" MF to a precise "receptor activity" MF and
  triaging the annotations that are not really receptor functions.

## Candidate genes for initial review

Listed in priority order. The first three are the clean, high-value receptor
cases that already have reviews in this repo and would directly exercise the
new MF once minted.

1. **TOMM20 (human, Q15388)** — canonical N-terminal presequence receptor;
   directly affected by two of the 18 annotations; review already
   `ACCEPT`s GO:0030943 as the core MF. Best positive control for the new
   `mitochondrial signal sequence receptor activity`.
2. **TOMM22 (human, Q9NS69)** — TOM central/co-receptor; directly affected.
3. **TOMM70 (human)** — receptor for carrier/hydrophobic precursors; ortholog
   of the affected yeast TOM70 (P07213, IMP).
4. **TIM50 / TIMM50** — trans-side presequence handoff receptor; affected yeast
   TIM50 (Q02776) plus the human ortholog review here.
5. **TIM22 (yeast, Q12328)** — special case: carrier pathway uses internal
   signals; decide whether the new receptor MF applies or whether the
   annotation should be removed/replaced with a carrier-import term.
6. **PAP2 (Arabidopsis, Q9LMG7)** — non-canonical IPI annotation; case-by-case.
7. **TIM23 complex (ComplexPortal CPX-539/6127/6129/6130)** — complex-level
   handling once the NTR exists.

## Proposed approach

1. **Wait for the NTR + obsoletion to land.** The replacement MF
   (`mitochondrial signal sequence receptor activity`) is not yet minted in GO
   (OLS, 2026-05-28). go-ontology#32142 is closed but the new GO ID must be
   confirmed before any remapping.
2. **Pre-stage MODIFY proposals** on the existing repo reviews (TOMM20, TOMM22,
   TOMM70, TIMM50, TIMM22, TOMM40), changing `GO:0030943` → the new receptor MF
   for the genuine cytosolic/trans-side receptors.
3. **Triage the non-receptor cases** explicitly: TIM22 (internal-signal carrier
   channel), PAP2 (plant IPI), and the TIM23 holo-complex records. These are
   the reason upstream avoided a blanket `replaced_by`.
4. **Note the IBA/IEA fallout** (~12k annotations): once GO:0030943 is
   obsoleted, the GO_Central IBA and TreeGrafter IEA pipelines will need to be
   reseeded against the new MF. The yeast `ACL4` review (already `REMOVE`) is a
   concrete example of an IBA that should *not* be carried over to the new
   receptor term.
5. **Coordinate with [[MITOCHONDRIAL_IMPORT_PATHWAYS]]** so MF remapping and the
   BP pathway model stay consistent for shared TOM/TIM genes.

## Priority

Medium. Only 18 curated annotations, and several of the key genes already have
reviews here, so the marginal curation effort is low. The receptor biology is
uncontroversial, so the main blocker is external (the NTR GO ID is not yet
minted). The large IEA/IBA tail makes this more impactful than the very small
obsoletions, but no curator group is blocked waiting on AI Gene Review.

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
