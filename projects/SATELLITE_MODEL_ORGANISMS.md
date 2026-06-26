---
title: "Satellite Model Organisms"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [CAEBR]
---

# Satellite Model Organisms

## Overview

This project collects gene reviews for **satellite model organisms** — species
that are studied primarily *in comparison to* an established model organism
database (MOD) reference, but are not themselves a MOD *sensu stricto*. They are
the comparison points that give a reference MOD its evolutionary and functional
context: close relatives used for comparative genomics, evo-devo, and
trait-evolution studies.

The canonical example here is the nematodes orbiting *Caenorhabditis elegans*.
*Pristionchus pacificus* is explicitly described in the literature as a
"satellite model organism" to *C. elegans*, and *Caenorhabditis briggsae* is the
standard congeneric comparison species for *C. elegans* genetics and genomics.
Their annotation status is uneven: many genes are known only through orthology to
the reference MOD, which makes them good targets for AI-assisted review that
synthesizes literature with comparative inference.

## What counts as a "satellite" here

- **Comparative, not reference.** The species is used to interpret a reference
  MOD (e.g. *C. elegans*, *D. melanogaster*, *S. cerevisiae*), rather than being
  the primary reference itself.
- **Not a MOD *sensu stricto*.** It is not one of the established GO Consortium
  reference-genome MODs with a dedicated, fully-staffed curation database. (Some
  satellites — e.g. *P. pacificus* via pristionchus.org, *C. briggsae* via
  WormBase — have substantial resources, but are still studied chiefly as
  comparators.)
- **Distinct from parasites.** Parasitic / host-associated species are tracked
  separately in [PARASITES](PARASITES.md). A species can be both a comparative
  model *and* a parasite (e.g. entomopathogenic nematodes); when in doubt, the
  parasite framing takes precedence for the gene biology and the satellite
  framing for the comparative-annotation angle. Cross-link rather than duplicate.

## Species in scope

| Species | UniProt code | Reference MOD | In repo? | Notes |
|---|---|---|---|---|
| *Caenorhabditis briggsae* | `CAEBR` | *C. elegans* (worm) | ✅ `genes/CAEBR/drd-5` | Standard congeneric comparator |
| *Pristionchus pacificus* | `PRIPA` (NCBITaxon:54126) | *C. elegans* (worm) | ❌ not yet | Necromenic beetle associate; evo-devo "satellite model" for mouthpart plasticity |

Other genera (e.g. comparative *Drosophila* species, *Saccharomyces* relatives)
may be added as gene reviews accrue.

## Genes for review

- [x] `CAEBR` **drd-5** — dopamine-receptor-family gene; reviewed (see
  `genes/CAEBR/drd-5/`).
- [ ] `PRIPA` (*P. pacificus*, NCBITaxon:54126) — seed gene(s) TBD; not yet
  fetched into the repo. Developmental-plasticity / predatory-morph genes are
  natural first candidates.

## Status / next steps

- **SCOPING.** Only *C. briggsae* `drd-5` is currently present.
- Identify a small seed set of *P. pacificus* genes (developmental-plasticity /
  predatory-morph genes are natural first candidates) and run
  `just fetch-gene PRIPA <gene>`.
- Where a satellite gene is annotated only by orthology to the reference MOD,
  record in the review whether the comparative inference is supported by direct
  evidence in the satellite species.

## Related projects

- [PARASITES](PARASITES.md) — parasitic / host-associated organisms (some
  nematodes overlap with this project).
- [CEPHALOPOD](CEPHALOPOD.md), [TARDIGRADE_STRESS_RESPONSE](TARDIGRADE_STRESS_RESPONSE.md)
  — other non-MOD organism gene-review collections.
