---
title: "Satellite Model Organisms"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [CAEBR, PRIPA]
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
| *Caenorhabditis briggsae* | `CAEBR` | *C. elegans* (worm) | ✅ `drd-5`, `tra-1`, `tra-2`, `fem-3`, `she-1` | Standard congeneric comparator; sex-determination genes are the flagship comparative-evolution set |
| *Pristionchus pacificus* | `PRIPA` (NCBITaxon:54126) | *C. elegans* (worm) | ✅ `genes/PRIPA/oaz` | Necromenic beetle associate; evo-devo "satellite model" for mouthpart plasticity |

Other genera (e.g. comparative *Drosophila* species, *Saccharomyces* relatives)
may be added as gene reviews accrue.

## Genes for review

- [x] `CAEBR` **drd-5** — dopamine-receptor-family gene; reviewed (see
  `genes/CAEBR/drd-5/`).
- **`CAEBR` sex-determination set** — seeded as the flagship comparative-evolution
  batch (sex determination is the canonical *C. briggsae* vs *C. elegans* evo-devo
  story); annotations are PENDING review:
  - [ ] **tra-1** (`Q17308`) — Gli/Ci-family transcription factor, terminal global
    regulator of the sex-determination pathway (PE=1; has experimental annotation).
  - [ ] **tra-2** (`Q17307`) — membrane receptor-type regulator of sex
    determination (PE=1; has experimental annotations).
  - [ ] **fem-3** (`Q8I8U6`) — sex-determination protein FEM-3 (PE=1; has
    experimental annotations).
  - [ ] **she-1** (`A8XDR5`) — F-box "spermless hermaphrodites" protein, a
    *C. briggsae*-lineage-specific gene required for hermaphrodite spermatogenesis;
    **no GO annotations yet** (annotation gap — a good de-novo curation target).
- [ ] `PRIPA` **oaz** (`Q9NHZ4`, ornithine decarboxylase antizyme) — seeded into
  `genes/PRIPA/oaz/`; annotations are PENDING review. This is the species' only
  reviewed (Swiss-Prot) entry; its 4 GOA annotations are all IBA/IEA (no
  experimental evidence).
- [ ] `PRIPA` developmental-plasticity / predatory-morph genes — TrEMBL-only;
  candidates for future review from literature + bioinformatics.

## Status / next steps

- **SCOPING.** *C. briggsae* `drd-5` + sex-determination set (`tra-1`, `tra-2`,
  `fem-3`, `she-1`) and *P. pacificus* `oaz` are present.
- *C. briggsae* has 582 reviewed entries; the protein-level (PE=1)
  experimentally-characterized ones cluster on sex determination, which is why
  that set was chosen as the first comparative batch.
- **Annotation availability (UniProt, 2026-06):** `PRIPA` has just **1 reviewed
  (Swiss-Prot) entry** — `Q9NHZ4` (OAZ_PRIPA, ornithine decarboxylase antizyme,
  142 aa), now seeded as `genes/PRIPA/oaz/` — alongside ~26,000 unreviewed TrEMBL
  entries. The classic developmental-plasticity / predatory-morph genes are all
  TrEMBL-only, so seeding those means working from unreviewed accessions.
- Next: complete the PENDING annotation review of `PRIPA` `oaz`, and decide
  whether to pull in TrEMBL plasticity genes (e.g. the *eud-1*/sulfatase morph
  switch) backed by literature + bioinformatics.
- Where a satellite gene is annotated only by orthology to the reference MOD,
  record in the review whether the comparative inference is supported by direct
  evidence in the satellite species.

## Related projects

- [PARASITES](PARASITES.md) — parasitic / host-associated organisms (some
  nematodes overlap with this project).
- [CEPHALOPOD](CEPHALOPOD.md), [TARDIGRADE_STRESS_RESPONSE](TARDIGRADE_STRESS_RESPONSE.md)
  — other non-MOD organism gene-review collections.
