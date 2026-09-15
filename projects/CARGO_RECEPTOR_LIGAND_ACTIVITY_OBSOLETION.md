---
title: "Cargo Receptor Ligand Activity (GO:0140355) — Obsoletion & Transfer"
maturity: SCOPING
tags: [OBSOLETION]
species:
  - human
  - mouse
  - rat
genes:
  - TCN1
  - TCN2
  - CBLIF
  - CD320
  - CUBN
  - AMN
---

# Cargo Receptor Ligand Activity (GO:0140355) — Obsoletion & Transfer

## Overview

A GO obsoletion proposal will retire the molecular-function term
**GO:0140355 cargo receptor ligand activity** — *"The activity of a gene
product that interacts with a cargo receptor and initiates endocytosis."*
(synonym: *cargo*; verified in OLS 2026-09-12, still active, `is_a
GO:0005515 protein binding`, no children).

The objection is that the term describes **what is done to a gene product**,
not an activity the gene product carries out. Being recognised by a cargo
receptor is a role in someone else's activity, and the causal direction GO
would need runs the other way: the *receptor* has the activity, and the ligand
is its input. Val Wood's framing in the ontology ticket:

> CD320 (cargo receptor) → Transcobalamin (B12 carrier) → has_input B12
>
> especially since we are moving away from binding terms, which would render:
> CD320 (cargo receptor) ← Transcobalamin (B12 carrier) → has_input B12
> (incorrect causal direction)

There is **no `replaced_by` term**. The proposal is to capture the
relationship as a `has_input` on the receptor's `GO:0038024 cargo receptor
activity`, or in a GO-CAM model, and to let the ligand keep the terms that
describe what it actually does (cobalamin binding, cobalamin transport).

This obsoletion is unusually tractable: the term's entire footprint of 172
annotations fans out from **three** seed annotations, and all three affected
human genes already carry the replacement content.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6533](https://github.com/geneontology/go-annotation/issues/6533)
  — *"Review annotations to GO:0140355 cargo receptor ligand activity"*
  (OPEN; labels `annotation review`, `direct_ann_to_list_of_terms`). Impacted
  groups listed as MGI 2, Reactome 3, SGD 1. MGI has already reported done
  (2026-09-11); Reactome's contact was reassigned to Lisa Matthews.
- Ontology ticket: [geneontology/go-ontology#32466](https://github.com/geneontology/go-ontology/issues/32466)
  — *"Obsoletion request: GO:0140355 cargo receptor ligand activity"* (OPEN).
- Term origin, for context: [go-annotation#2364](https://github.com/geneontology/go-annotation/issues/2364)
  (apolipoprotein annotation review, where the gap was identified) →
  [go-ontology#17391](https://github.com/geneontology/go-ontology/issues/17391)
  (NTR, 2019). The term was minted to describe ApoB acting as the ligand for
  LDLR — a use case that, notably, **is not among the annotations that
  actually exist today**.

### How the ontology ticket converged

Worth reading before acting, because the recommendation reversed mid-thread:
an initial analysis argued *against* obsoletion on design-pattern grounds
(the "X receptor binding" family, `GO:0048018 receptor ligand activity`),
then withdrew that argument on inspection of the actual axiomatisation — the
sibling terms are all inside the **signaling**-receptor branch
(`GO:0005124 scavenger receptor binding is_a signaling receptor binding`;
`GO:0048018 is_a signaling receptor activator activity`), whereas GO:0140355
is `is_a protein binding` with **no logical relationship to
`GO:0038024 cargo receptor activity` anywhere in the ontology**, and cargo
receptors and signaling receptors are disjoint in GO. The resemblance was
nominal. The same thread's first annotation count (15 non-IEA rows over 5 gene
products, including *Hpse*) was also corrected on re-query. The counts below
were re-derived here independently from QuickGO rather than taken from either
version of that thread.

## Affected annotations (verified via QuickGO, 2026-09-12)

172 annotations across 164 gene products, **all molecular_function, all
`enables`**. Evidence split: 157 IEA, 9 ISO, 3 IDA, 3 EXP.

### (A) The six manual experimental rows — the actual curation job

| Gene product | Species | UniProt | Ev | Reference | Assigned by |
|---|---|---|---|---|---|
| **TCN1** (haptocorrin) | human | P20061 | EXP | PMID:22547309 | Reactome |
| **TCN2** (transcobalamin-2) | human | P20062 | EXP | PMID:3782074 | Reactome |
| **CBLIF** (gastric intrinsic factor) | human | P27352 | EXP | PMID:17954916 | Reactome |
| **`Tcn2`** | mouse | O88968 | IDA | PMID:237480 | MGI |
| **Cblif** | mouse | P52787 | IDA | PMID:14321840 | MGI |
| **`ATG5`** | *S. cerevisiae* | Q12380 | IDA | PMID:27879200 | SGD |

Reference titles confirmed against PubMed (2026-09-12):

- PMID:22547309 — *Vitamin B12 transport from food to the body's cells — a
  sophisticated, multistep pathway.* Nat Rev Gastroenterol Hepatol 2012. A
  **review**, not a primary TCN1 assay.
- PMID:3782074 — *Purification and molecular characterization of human
  transcobalamin II.* J Biol Chem 1986.
- PMID:17954916 — *Crystal structure of human intrinsic factor: cobalamin
  complex at 2.6-Å resolution.* PNAS 2007.
- PMID:237480 — *Transport of vitamin B12 into mouse leukemia cells.* Arch
  Biochem Biophys 1975.
- PMID:14321840 — *Studies on the interaction of vitamin B12: intrinsic factor
  and receptors…* Arch Biochem Biophys 1965.
- PMID:27879200 — *Mechanism of cargo-directed Atg8 conjugation during
  selective autophagy.* eLife 2016.

Two observations on this table:

1. **The three B12-carrier papers are B12-binding/structure papers**, two of
   them predating the cargo-receptor concept by decades (1965, 1975). What
   they establish — high-affinity cobalamin binding, and delivery of B12 into
   cells — maps onto `GO:0031419 cobalamin binding` and
   `GO:0015889 cobalamin transport`, both of which **all three human genes
   already carry** (see below). No experimental content is lost by dropping
   GO:0140355.
2. **The yeast row is a different kind of error and should not be transferred
   at all.** PMID:27879200 is about the `Atg12`–`Atg5`–`Atg16` conjugation
   machinery being recruited near a cargo receptor to direct Atg8 lipidation;
   `Atg5` is not cargo recognised by a receptor. The ontology ticket's author
   has said he will fix this SGD annotation directly.

### (B) Nine ISO rows that follow automatically

| Gene product | Species | UniProt | Source (WITH/FROM) | Assigned by |
|---|---|---|---|---|
| `Tcn2` | mouse | O88968 | UniProtKB:P20062 | GO_Central |
| Cblif | mouse | P52787 | UniProtKB:P27352 (×2), RGD:62084 | MGI (×2), GO_Central |
| Cblif | rat | P17267 | UniProtKB:P27352, MGI:MGI:1202394 | RGD |
| `Tcn2` | rat | Q9R0D6 | UniProtKB:P20062, MGI:MGI:98534 | RGD |
| **Hpse** | mouse | Q6YGZ1 | UniProtKB:Q9Y251 (PMID:24788042) | MGI |

All but the last are orthology transfers within the TCN2/CBLIF set and
disappear with their sources. **The mouse *Hpse* row is an orphan worth
flagging upstream**: its WITH/FROM source, human HPSE (Q9Y251), carries **no
current GO:0140355 annotation** — it is not among the 172 rows. The ISO
therefore rests on a source annotation that no longer exists, and its
reference (PMID:24788042, *Processing of heparanase is mediated by syndecan-1
cytoplasmic domain and involves syntenin and α-actinin*, Cell Mol Life Sci
2014) is about syndecan-1-mediated heparanase processing, not cargo-receptor
recognition. It should be removed on its own merits, independent of the
obsoletion. It is also not counted in the upstream issue's "Impacted groups"
tally (MGI 2 = the two IDA rows), so it risks being missed.

### (C) 157 IEA rows — a three-seed fan-out

Every IEA row is `GO_REF:0000107` (Ensembl/EnsemblFungi orthology) and traces
to exactly one of three seeds:

| Seed | Species | IEA rows projected |
|---|---|---|
| O88968 (mouse `Tcn2`) | mouse | 77 |
| P52787 (mouse Cblif) | mouse | 68 |
| Q12380 (yeast `ATG5`) | *S. cerevisiae* | 12 (EnsemblFungi) |

So the 157 vertebrate/fungal orthologs need no individual attention: they are
regenerated from the seeds on each Ensembl release and vanish when the two
mouse IDAs and the SGD IDA go. Note that **the two Ensembl seeds are the mouse
annotations, not the human ones** — clearing the human Reactome rows alone
would leave the entire fan-out standing. The 12 fungal rows are riding
entirely on the one mis-applied yeast `ATG5` IDA.

**Net human curation effort: 6 rows.** Everything else is downstream.

## Impact on this repo

### Tier 1 — two reviews break validation when the obsoletion lands

`core_functions` term ids are strictly validated in this repo (GOA-sourced
`existing_annotations[].term.id` values are not). Two reviews use GO:0140355
as a `core_functions[].molecular_function`:

| Review | Where | Current action | What happens |
|---|---|---|---|
| `genes/human/CBLIF/CBLIF-ai-review.yaml` | `existing_annotations` row (EXP, PMID:17954916, `ACCEPT`) **and** `core_functions[].molecular_function` | ACCEPT, called "an informative, core molecular function" | `just validate human CBLIF` should be expected to fail on the `core_functions` entry |
| `genes/human/TCN2/TCN2-ai-review.yaml` | `existing_annotations` row (EXP, PMID:3782074, `ACCEPT`) **and** `core_functions[].molecular_function` | ACCEPT, "a core molecular function" | same |

Both reviews additionally argue *from* GO:0140355: TCN2 downgrades its
`GO:0005515 protein binding` row to `MARK_AS_OVER_ANNOTATED` on the grounds
that "the informative molecular function … [is] better represented by
GO:0140355". That reasoning has to be rewritten, not just the id swapped.

### Tier 2 — one row, no core_functions exposure

`genes/human/TCN1/TCN1-ai-review.yaml` carries the EXP row
(PMID:22547309) with `action: KEEP_AS_NON_CORE`, and already reasons that the
ligand behaviour "follows from its cobalamin binding" and "is a downstream
consequence" — which anticipates the obsoletion rationale. Only the
`existing_annotations` row needs re-terming; nothing in `core_functions`
depends on it.

### Tier 3 — prose mention only

`genes/human/HSPA12A/HSPA12A-ai-review.yaml` cites GO:0140355 in a
`proposed_new_terms[].justification` (as a term it considered and rejected,
correctly, because HSPA12A binds a receptor's *cytoplasmic tail*). Non-blocking;
reword when convenient.

### Tier 4 — the receptor side is already curated here

The counterpart cargo receptors all have reviews carrying
`GO:0038024 cargo receptor activity`: `genes/human/CD320` (the transcobalamin
receptor), `genes/human/CUBN` and `genes/human/AMN` (the ileal cubam receptor
for holo-intrinsic-factor). This repo therefore holds **both halves** of the
B12 uptake system, which makes it a good place to check that the proposed
re-modelling is lossless: everything GO:0140355 was asserting about the ligand
should be recoverable as `has_input` on the receptor activities already
reviewed here.

## Candidate destination terms (all verified in OLS, 2026-09-12)

| GO id | Label | Aspect | Status for the three B12 carriers |
|---|---|---|---|
| GO:0140355 | cargo receptor ligand activity (**to be obsoleted**; still active) | MF | — |
| GO:0031419 | cobalamin binding | MF | **already annotated on all three** (TCN1, TCN2, CBLIF) |
| GO:0015889 | cobalamin transport | BP | **already annotated on all three** |
| GO:0038024 | cargo receptor activity | MF | belongs to the *receptor* (CD320, CUBN/AMN), with the carrier as `has_input` |
| GO:0140104 | molecular carrier activity | MF | **candidate** — see caveat |
| GO:0140313 | molecular sequestering activity | MF | already on TCN1 (PMID:23846701, PMID:27411955); fits haptocorrin's B12-analogue-scavenging role |

**On GO:0140104 molecular carrier activity** — *"Directly binding to a
specific ion or molecule and delivering it either to an acceptor molecule or
to a specific location"*, with the explicit note that *"a carrier moves with
its substrate/cargo, while a transporter does not"*. That is a close fit for
what transcobalamin and intrinsic factor actually do, and it matches Val
Wood's own framing of transcobalamin as "a carrier of its target molecule".
The caveat is this repo's own precedent in `genes/human/AFP`, where
GO:0140104 was deliberately **not** proposed because binding was demonstrated
but *delivery to an acceptor* was not. For the B12 carriers, delivery *is*
demonstrated (receptor-mediated endocytosis releases cobalamin intracellularly),
so the AFP objection does not obviously apply — but this is a judgement for a
curator, and GO:0140104 is offered here as a candidate, not a conclusion. If
it is rejected, GO:0031419 + GO:0015889 (both already present) carry the
content on their own and the correct action is a plain `REMOVE`.

## Scope

- **Organisms**: human (TCN1, TCN2, CBLIF), mouse (`Tcn2`, Cblif, Hpse), rat
  (`Tcn2`, Cblif), *S. cerevisiae* (`ATG5`); 157 further Ensembl/EnsemblFungi
  ortholog projections follow automatically.
- **GO branch**: MF obsoletion with **no replacement term**. Content moves
  either to terms the genes already have, or onto the receptor's activity as
  `has_input` / into a GO-CAM model.
- **Type of fix in this repo's vocabulary**: `REMOVE` for the
  `existing_annotations` rows (the term is being retired, and the content is
  already captured elsewhere on the same genes) — *not* `MODIFY`, since there
  is no one-to-one replacement. The `core_functions` entries need re-pointing
  to `GO:0031419` and/or `GO:0140104`, with the accompanying prose rewritten.
- **Not in scope**: the wider question the ticket raises — whether the
  "ligand-of-a-receptor" MF pattern is legitimate at all — which affects the
  signaling-side family (GO:0048018 and children) and is not being touched.

## Candidate genes for initial review

Confirm accessions with `just fetch-gene <organism> <gene>` before starting.

### Tier 1 — existing reviews go stale (do these first)

1. **TCN2** (human, P20062) — `genes/human/TCN2/`. GO:0140355 is both an
   `ACCEPT`ed row and a `core_functions` MF, and it is the stated reason for
   downgrading the CD320 `protein binding` row. The most entangled of the
   three; also the cleanest biology, since the holo-TC:CD320 co-crystal makes
   the ligand relationship unambiguous — the question is only whether GO calls
   it an activity.
2. **CBLIF** (human, P27352) — `genes/human/CBLIF/`. Same shape as TCN2
   (row + `core_functions` MF), with the cubam (CUBN/AMN) receptor rather than
   CD320. Pairs directly with the existing `genes/human/CUBN` and
   `genes/human/AMN` reviews.

### Tier 2 — single row, low risk

3. **TCN1** (human, P20061) — `genes/human/TCN1/`. Already `KEEP_AS_NON_CORE`
   with reasoning that anticipates the obsoletion. Re-term the row; consider
   whether `GO:0140313 molecular sequestering activity` (already present)
   plus `GO:0031419` fully covers haptocorrin's role.

### Tier 3 — not yet reviewed here, useful as validation

4. **CD320** (human, Q9NPF0) — `genes/human/CD320/` **exists**; re-check that
   its `GO:0038024` annotation plus a `has_input` on holo-transcobalamin
   really does capture what the obsoleted ligand term was asserting. This is
   the test of whether the re-modelling is lossless.
5. **HPSE** (human, Q9Y251) / **Hpse** (mouse, Q6YGZ1) — no review here. Only
   needed if someone wants to chase the orphaned ISO row; the annotation
   should go regardless of the obsoletion.
6. **`ATG5`** (*S. cerevisiae*, Q12380) — no `genes/yeast/ATG5` review here
   (`genes/human/ATG5` and `genes/SCHPO/atg5` exist and are unaffected). The
   SGD row is being fixed upstream; no action needed here beyond watching that
   the 12 EnsemblFungi projections clear with it.

## Proposed approach

1. **Wait for the obsoletion to land** before editing `core_functions` — the
   ids are still active, so premature edits would swap a valid term for a
   judgement call that curators may still overturn (the ticket has already
   reversed direction once).
2. When it lands, fix TCN2 and CBLIF together: they share a rationale and a
   destination-term decision, and both have a receptor-side review in this
   repo to check against.
3. Decide the GO:0140104 question once, in one place, and apply it to all
   three carriers consistently.
4. Re-run `just validate human TCN2 / CBLIF / TCN1` and confirm the
   `core_functions` strict-validation errors clear.

## Open questions

- Does `GO:0140104 molecular carrier activity` fit a secreted vitamin carrier
  whose cargo is released only after receptor-mediated endocytosis of the
  whole complex — or does GO consider that transport rather than carriage?
- Should the `has_input` re-modelling be made explicit in the existing
  `CD320`, `CUBN`, and `AMN` reviews, or left to GO-CAM?
- Is there a residual gap for the **original** use case the term was minted
  for — ApoB as the LDLR ligand (go-ontology#17391)? No apolipoprotein is
  annotated to GO:0140355 today, so the obsoletion strands nothing; but the
  2019 curation problem that motivated it ("we don't have an activity for
  this") is not solved by the obsoletion either.
