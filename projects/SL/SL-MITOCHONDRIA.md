---
title: "SL mitochondrial granularity triple"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, mouse, yeast, SCHPO, rat, ARTAN]
autolink_gene_symbols: false
---

# The mitochondrial granularity triple

A controlled comparison. Three UniProt locations, one organelle, one pipeline, one set of
curators — differing only in how specific the location is.

| SL | GO term | Reviewed | Issues | Rate |
|---|---|---|---|---|
| SL-0171 | GO:0031966 mitochondrial **membrane** | 13 | 4 | **31%** |
| SL-0168 | GO:0005743 mitochondrial **inner** membrane | 19 | 2 | **11%** |
| SL-0170 | GO:0005759 mitochondrial **matrix** | 14 | 1 | **7%** |

The under-specified location is flagged three to four times as often as its precise siblings.
Because the organelle, the pipeline, the mapping mechanism, and the reviewer pool are all held
constant, the difference is attributable to specificity itself rather than to anything about
mitochondria.

## The SL-0171 flags are all the same complaint

All four resolve to "should be the inner membrane":

- **yeast PET100** — "Pet100 is an inner-membrane protein, so the broader mitochondrial
  membrane annotation should be replaced by the specific compartment." → GO:0005743
- **mouse Surf1** — "the mechanistic evidence places SURF1 in the inner membrane COX assembly
  machinery. GO:0005743 is the better curated cellular component term." → GO:0005743
- **human TIMM21** — "Use mitochondrial inner membrane and TIM23 complex annotations instead
  of generic mitochondrial membrane."
- **SCHPO alo1** — MODIFY

## The specific siblings fail differently, and more interestingly

The three flags on SL-0168 and SL-0170 are *not* granularity complaints. They are substantive
localization errors that a precise term makes visible:

- **SCHPO tim10** (SL-0168) — "Tim10 is primarily localized in the mitochondrial intermembrane
  space as a soluble protein. While it associates peripherally with the inner membrane during
  substrate handoff to TIM22, its primary localization is the IMS." → GO:0005758. A
  **wrong sub-compartment** call.
- **rat Tp53** (SL-0170) — "Mitochondrial p53 acts at the OMM with BCL-2 proteins, not in the
  matrix; IEA subcellular-location mapping is too imprecise." Another wrong sub-compartment,
  and one where the imprecision runs the other way — the location is *too* confident.
- **ARTAN A0A2U1PS28** (SL-0168) — "OpenScientist deep research revealed a critical organelle
  mis-assignment. A0A2U1PS28 is classified by PANTHER as PTHR43512:SF4 (CHLOROPLASTIC) and
  clusters with chloroplastic orthologs across 8 plant species." A **wrong organelle
  entirely** — the most serious error type found anywhere in the SL corpus, and one that only
  surfaced because a specific term made the claim falsifiable.

## What this implies

Under-specification and mis-assignment are different diseases with different treatments.
Making an SL location more specific does not reduce the number of *errors*; it converts
un-checkable vagueness into checkable claims, some of which then turn out to be wrong. That is
an improvement — a 7% error rate on precise terms is more useful than a 31% vagueness rate on
imprecise ones — but it should not be sold as error reduction.

No annotations were changed under this subproject; all four SL-0171 cases had already been
flagged by prior reviews.
