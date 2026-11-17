---
title: "Chromatin Silencing Complex (GO:0005677): Obsolete, Merge or Rename?"
maturity: SCOPING
tags: [OBSOLETION]
species: [ARATH, yeast, human, DROME, MAIZE]
genes: [CLF, FIE, MSI1, SWN, VIN3, VRN2, VRN5, EZ1, BAZ2A, SIRT1, EZH2, SIR2, SIR3, SIR4, Elba1, Elba2, Elba3]
collections: [GO_TRACKER_BACKLOG]
---

# Chromatin Silencing Complex (GO:0005677): Obsolete, Merge or Rename?

**Bottom line:** PomBase opened a GO tracker issue in 2020 to obsolete the
grouping term GO:0005677 *chromatin silencing complex*, because "silencing"
is no longer a GO process. The thread stalled in 2022 between three options:
obsolete it, merge it into GO:0140513 *nuclear protein-containing complex*
(which now exists), or rename it *gene silencing complex*. Meanwhile the
term gained a logical definition (protein-containing complex capable of
part_of GO:0031507 *heterochromatin formation*), so it now has a computable
meaning. Seventeen reviewed genes carry it, nearly all ACCEPT. Every option
needs a specific complex for each annotated gene, and gene reviews can
supply that. For two groups GO has no specific term: yeast SIR2/SIR3/SIR4
and the fly Elba proteins. Scoped, not started.

## Upstream ticket

| Issue | Opened | Last substantive comment |
|---|---|---|
| [go-ontology#19574](https://github.com/geneontology/go-ontology/issues/19574) | 2020-06-03 | 2022-02-09 |

Thread summary as of 2026-11-16, and term states from a go-ontology checkout
of 2026-11-12. Nothing has been posted to the issue.

## Where the thread stands

- **The case for obsoletion** (2020-07-20): "This term was intended as a
  grouping term for complexes involved in "silencing". However, the concept
  of silencing as a process is no longer included in GO". PomBase found the
  direct annotations poor. Mouse Baz2a belongs in GO:0090536 *NoRC complex*,
  and mouse Suv39h1 is an adaptor rather than a clear complex member. About
  30 experimental rows were counted, some sound, such as the yeast RENT
  complex rows.
- **Merge** (2020-09-21): into *nuclear protein-containing complex*, once
  that was created. It now exists as GO:0140513.
- **Obsolete rather than merge** (2021-02-12): 34 experimental rows could be
  made more specific.
- **Rename** (2022-02-09): an editor offered *gene silencing complex*.
  PomBase replied that most transcriptional-silencing complexes are not
  children of the term anyway.

In go-edit.obo the definition is unchanged ("Any protein complex that
mediates changes in chromatin structure that result in transcriptional
silencing."). The is_a children are RENT, eNoSc, chromatin lock, HUSH and
HUSH2 complexes. The new logical definition means the reasoner will classify
any complex capable of part of heterochromatin formation under it. That
argues against simply obsoleting it.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py)
(`--descendants GO:0005677`).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0005677 chromatin silencing complex | 24 | 17 | 17 | 6 | 1 | 0 | 0 | 0 |  | 2 |
| GO:0030869 RENT complex | 3 | 2 | 3 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0061793 chromatin lock complex | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0061773 eNoSc complex | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0140283 HUSH complex | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0140286 HUSH2 complex | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 |

The 17 genes on GO:0005677, with the specific complex a review would
consider:

| Genes | Review action | Complex | Specific GO term? |
|---|---|---|---|
| ARATH CLF, FIE, MSI1, SWN, VRN2; MAIZE EZ1 | ACCEPT | plant PRC2 (VRN-PRC2, EMF-PRC2) | GO:0035098 ESC/E(Z) complex |
| ARATH VIN3, VRN5 | ACCEPT | PHD-PRC2 accessory proteins | GO:0035098 (as accessory), or GO:0031519 PcG protein complex |
| human EZH2 | MODIFY | PRC2 | GO:0035098 |
| human BAZ2A | ACCEPT (ISS) | NoRC | GO:0090536 NoRC complex (the thread's own example) |
| human SIRT1 | ACCEPT | eNoSc | GO:0061773 eNoSc complex |
| yeast SIR2, SIR3, SIR4 | ACCEPT | SIR complex (Sir2-Sir3-Sir4) | none found in go-edit.obo; SIR2 is also on GO:0030869 RENT |
| DROME Elba1, Elba2, Elba3 | KEEP_AS_NON_CORE | Elba insulator complex (FlyBase IDA, ComplexPortal IPI) | none found |

The PRC2 rows come mostly from UniProt IDA, the SIR rows from SGD IDA, and
the Elba rows from FlyBase and ComplexPortal.

## What gene review can and cannot settle

- **Can settle, per gene:** the specific complex each GO:0005677 row should
  name. This is the migration map any of the three options needs.
- **Can identify:** complexes that would be left with no term. The SIR
  complex and the Elba complex are the clear cases, and either is a
  `proposed_new_terms` candidate (Complex Portal can be the source).
- **Cannot settle:** obsolete versus rename versus merge. The new logical
  definition shifts that choice, and it is the editors' call.

## Plan

- [ ] Re-check the 13 ACCEPT reviews: does each also carry the specific
      complex term? If so, GO:0005677 is redundant there. If not, record the
      specific term.
  - [ ] ARATH CLF, FIE, MSI1, SWN, VIN3, VRN2, VRN5; MAIZE EZ1: GO:0035098
  - [ ] human BAZ2A: GO:0090536; human SIRT1: GO:0061773
  - [ ] yeast SIR2, SIR3, SIR4: no specific term; draft a SIR complex NTR
- [ ] DROME Elba1-3: confirm the Elba complex has no GO term. Draft an NTR or
      record the gap.
- [ ] Draft the per-gene migration table as a note for the issue owners.
      Posting it is the project lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No reviews started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Thread read
  in full.
- GO:0005677 carries no term_tracker_item, so the logical definition's
  origin is not linked from the term.
- No SIR complex term was found by name or synonym in go-edit.obo
  (2026-11-12). Check Complex Portal before drafting an NTR.
