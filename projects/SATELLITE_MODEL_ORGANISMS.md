---
title: "Satellite Model Organisms"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [CAEBR, PRIPA]
genes: [drd-5, tra-1, tra-2, fem-3, she-1, cep-1, trr-1, kin-1, peb-1, ubl-1, oaz]
---

# Satellite Model Organisms

**Bottom line:** satellite model organisms are species studied mainly as
comparators to a reference model organism; here, the nematodes
*Caenorhabditis briggsae* and *Pristionchus pacificus* alongside
*C. elegans*. Most of their GO annotations are transferred by orthology, so we
reviewed them to see whether the comparative inference holds up. We reviewed
11 genes: 10 *C. briggsae* genes (drd-5, the sex-determination set tra-1,
tra-2, fem-3 and she-1, and five other protein-level entries) and oaz, the only
Swiss-Prot entry for *P. pacificus*. All 11 reviews are complete. They cover 115
existing annotation rows (52 ACCEPT, 43 KEEP_AS_NON_CORE, 11
MARK_AS_OVER_ANNOTATED, 6 MODIFY, 3 REMOVE) and propose 4 NEW terms; she-1 had
no GO annotations and was curated from the literature. The open question is
whether to add the TrEMBL-only *P. pacificus* plasticity genes such as eud-1.

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
| *Caenorhabditis briggsae* | `CAEBR` | *C. elegans* (worm) | ✅ 10 genes seeded (see below) | Standard congeneric comparator; sex-determination genes are the flagship comparative-evolution set |
| *Pristionchus pacificus* | `PRIPA` (NCBITaxon:54126) | *C. elegans* (worm) | ✅ `genes/PRIPA/oaz` | Necromenic beetle associate; evo-devo "satellite model" for mouthpart plasticity |

Other genera (e.g. comparative *Drosophila* species, *Saccharomyces* relatives)
may be added as gene reviews accrue.

## Genes for review

- [x] `CAEBR` **drd-5** — short-chain dehydrogenase/reductase family enzyme ("dietary restriction down regulated"); reviewed (see
  `genes/CAEBR/drd-5/`).
- **`CAEBR` sex-determination set** — seeded as the flagship comparative-evolution
  batch (sex determination is the canonical *C. briggsae* vs *C. elegans* evo-devo
  story); reviewed:
  - [x] **tra-1** (`Q17308`) — Gli/Ci-family transcription factor, terminal global
    regulator of the sex-determination pathway (PE=1; has experimental annotation).
  - [x] **tra-2** (`Q17307`) — membrane receptor-type regulator of sex
    determination (PE=1; has experimental annotations).
  - [x] **fem-3** (`Q8I8U6`) — sex-determination protein FEM-3 (PE=1; has
    experimental annotations).
  - [x] **she-1** (`A8XDR5`) — F-box "spermless hermaphrodites" protein, a
    *C. briggsae*-lineage-specific gene required for hermaphrodite spermatogenesis;
    **no GO annotations yet** (annotation gap — a good de-novo curation target).
- **`CAEBR` other protein-level (PE=1) genes** — the remaining *C. briggsae*
  entries with experimental protein-level evidence; reviewed:
  - [x] **cep-1** (`A8WW61`) — p53/p63/p73-family transcription factor
    (germline DNA-damage apoptosis); 31 GOA annotations.
  - [x] **trr-1** (`A8WTE8`) — TRRAP-like transcription-associated protein.
  - [x] **kin-1** (`A8XW88`) — cAMP-dependent protein kinase catalytic subunit (PKA).
  - [x] **peb-1** (`A8XJ98`) — FLYWCH-type zinc-finger pharyngeal regulator
    (has an experimental annotation).
  - [x] **ubl-1** (`P37164`) — ubiquitin-like / ribosomal eS31 fusion protein.
- [x] `PRIPA` **oaz** (`Q9NHZ4`, ornithine decarboxylase antizyme) — seeded into
  `genes/PRIPA/oaz/`; reviewed. This is the species' only
  reviewed (Swiss-Prot) entry; its 4 GOA annotations are all IBA/IEA (no
  experimental evidence).
- [ ] `PRIPA` developmental-plasticity / predatory-morph genes — TrEMBL-only;
  candidates for future review from literature + bioinformatics.

## Status / next steps

- **IN_PROGRESS.** All 11 seeded genes are reviewed: *C. briggsae* `drd-5`, the
  sex-determination set (`tra-1`, `tra-2`, `fem-3`, `she-1`), five other PE=1
  genes, and *P. pacificus* `oaz`.
- *C. briggsae* has 582 reviewed entries; the protein-level (PE=1)
  experimentally-characterized ones cluster on sex determination, which is why
  that set was chosen as the first comparative batch.
- **Annotation availability (UniProt, 2026-06):** `PRIPA` has just **1 reviewed
  (Swiss-Prot) entry** — `Q9NHZ4` (OAZ_PRIPA, ornithine decarboxylase antizyme,
  142 aa), now seeded as `genes/PRIPA/oaz/` — alongside ~26,000 unreviewed TrEMBL
  entries. The classic developmental-plasticity / predatory-morph genes are all
  TrEMBL-only, so seeding those means working from unreviewed accessions.
- Next: decide whether to pull in TrEMBL plasticity genes (e.g. the *eud-1*/sulfatase morph
  switch) backed by literature + bioinformatics.
- Where a satellite gene is annotated only by orthology to the reference MOD,
  record in the review whether the comparative inference is supported by direct
  evidence in the satellite species.

## Related projects

- [PARASITES](PARASITES.md) — parasitic / host-associated organisms (some
  nematodes overlap with this project).
- [CEPHALOPOD](CEPHALOPOD.md), [TARDIGRADE_STRESS_RESPONSE](TARDIGRADE_STRESS_RESPONSE.md)
  — other non-MOD organism gene-review collections.

## Slides

- [Slides](SATELLITE_MODEL_ORGANISMS/slides/SATELLITE_MODEL_ORGANISMS-slides.html) (Marp source: [SATELLITE_MODEL_ORGANISMS-slides.md](SATELLITE_MODEL_ORGANISMS/slides/SATELLITE_MODEL_ORGANISMS-slides.md)) — AI generated
