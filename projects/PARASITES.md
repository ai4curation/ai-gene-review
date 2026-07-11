---
title: "Parasites"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [STECR, 9BILA, BRUMA]
---

# Parasites

## Overview

This project is a broad umbrella for gene reviews of **parasitic and
host-associated organisms** — species whose biology is defined by a parasitic
(or otherwise intimate host-exploiting) lifestyle. It collects the gene biology
that is specific to parasitism: host invasion, host-immune evasion/modulation,
nutrient acquisition from the host, and the molecular machinery of the
parasite–host (and parasite–symbiont) interface.

It serves as a hub that ties together more focused parasite-related efforts
rather than duplicating them — see [Related projects](#related-projects).

## Scope

- **Animal-parasitic and insect-parasitic nematodes**, including
  entomopathogenic nematodes (EPNs) such as *Steinernema*, which kill insect
  hosts in mutualistic partnership with *Xenorhabdus*/*Photorhabdus* bacteria.
- **Other metazoan and protozoan parasites** as gene reviews accrue
  (helminths, apicomplexans, etc.).
- **Host-modulating secreted proteins** of parasites and blood-feeders —
  these are the subject of the existing
  [PARASITE_IMMUNE_MODULATORS](PARASITE_IMMUNE_MODULATORS.md) project, treated
  here as a sub-topic.

A note on boundaries: not every host-associated nematode is a parasite.
*Necromenic* associates (e.g. *Pristionchus pacificus*, which rides live beetles
but only feeds after they die) and free-living comparators (e.g.
*Caenorhabditis briggsae*) are **not** parasites and are tracked under
[SATELLITE_MODEL_ORGANISMS](SATELLITE_MODEL_ORGANISMS.md). True insect-parasitic
nematodes that are *also* used as comparative models are cross-listed.

## Species in scope

| Species | Parasitic lifestyle | In repo? | Notes |
|---|---|---|---|
| *Steinernema carpocapsae* | Entomopathogenic (insect-parasitic) nematode | ✅ `genes/STECR/nas-8` | Best-annotated EPN. UniProt code `STECR`, NCBITaxon:34508. **Holds the genus's only reviewed (Swiss-Prot) entry:** `D2KBH9` (NAS8_STECR), a secreted astacin metalloprotease — the parasitism-relevant anchor seed. |
| *Steinernema hermaphroditum* | Entomopathogenic (insect-parasitic) nematode | ❌ not yet | Mutualist of *Xenorhabdus*; emerging genetic model for EPN/symbiosis biology. UniProt code `9BILA` (provisional, auto-assigned), NCBITaxon:289476 → `genes/9BILA/`. No reviewed entries. |
| *Brugia malayi* | Filarial (human lymphatic filariasis), mosquito-borne | ✅ 5 genes seeded (see below) | Model filarial nematode, UniProt code `BRUMA`, NCBITaxon:6279. **The reviewed-rich anchor for the project (68 Swiss-Prot entries)** — provides experimentally-characterized host-interaction/immune-evasion proteins to review. |

The EPNs most biologically aligned with *Steinernema* (*Heterorhabditis
bacteriophora*, `HETBA`) and *Strongyloides ratti* (`STRRB`) have **0 reviewed
entries**, so *B. malayi* was chosen as the reviewed-rich nematode anchor.
Additional parasites (other filariae — *Onchocerca volvulus* `ONCVO` 43,
*Ascaris suum* `ASCSU` 67 — parasitic helminths, protozoan parasites) to be added
as reviews are scoped.

## Genes for review

- [x] *Steinernema carpocapsae* `STECR` **nas-8** (`D2KBH9`, zinc metalloproteinase
  / astacin, EC 3.4.24.21) — seeded into `genes/STECR/nas-8/`; annotations are
  PENDING review. Secreted protease relevant to host invasion; carries an **EXP**
  metalloendopeptidase-activity annotation from PMID:20670659 (Sc-AST
  characterization) plus IEA terms.
- [ ] *Steinernema hermaphroditum* (`9BILA`, NCBITaxon:289476) — seed gene(s)
  TBD; not yet fetched into the repo. No reviewed entries, so any seed is a
  TrEMBL accession. Candidate areas: infective-juvenile development, host-immune
  evasion, and the *Xenorhabdus* symbiosis interface.
- **`BRUMA` (*B. malayi*) host-interaction / immune-evasion set** — reviewed,
  protein-level (PE=1) filarial genes; seeded, annotations PENDING:
  - [ ] **cpi-2** (`A0A0K0IP23`) — cystatin; secreted immunomodulator (inhibits
    host cysteine proteases / modulates antigen presentation). Has experimental
    annotations.
  - [ ] **far-1** (`Q93142`) — fatty-acid & retinol-binding protein (Bm20), a
    classic secreted excretory–secretory immunomodulator. Has experimental
    annotations.
  - [ ] **dpy-31** (`A8Q2D1`) — zinc metalloproteinase / astacin (procollagen
    C-proteinase), cuticle biogenesis — parallels the *Steinernema* nas-8 astacin.
  - [ ] **gp29** (`P67877`) — cuticular glutathione peroxidase, major surface
    antigen (oxidative defense at the host interface).
  - [ ] **mf1** (`P29030`) — endochitinase (MF1 antigen), microfilarial
    sheath / vaccine candidate.

## Status / next steps

- **SCOPING.** Parasite seeds present: *S. carpocapsae* `nas-8` (EPN anchor) and
  a 5-gene *B. malayi* host-interaction set (reviewed-rich filarial anchor) — all
  PENDING review.
- **Annotation availability (UniProt, 2026-06):** across the **whole genus
  *Steinernema*** there is exactly **1 reviewed (Swiss-Prot) entry** — `D2KBH9`
  (NAS8_STECR, *S. carpocapsae* astacin metalloprotease). *S. hermaphroditum*
  (`9BILA`) has **0 reviewed** entries (~36,000 TrEMBL); *S. carpocapsae*
  (`STECR`) has 1 reviewed + ~35,200 TrEMBL.
- **Next:** complete the PENDING annotation review of *S. carpocapsae* `nas-8`
  (start from the EXP PMID:20670659 evidence), then expand to *S. hermaphroditum*
  TrEMBL genes paired with literature + bioinformatics rather than relying on
  existing GO annotation.
- Pull the [PARASITE_IMMUNE_MODULATORS](PARASITE_IMMUNE_MODULATORS.md) candidate
  list under this umbrella's "host-modulation" sub-topic.

## Related projects

- [PARASITE_IMMUNE_MODULATORS](PARASITE_IMMUNE_MODULATORS.md) — parasite/
  blood-feeder secreted proteins that modulate host immunity (sub-topic).
- [SATELLITE_MODEL_ORGANISMS](SATELLITE_MODEL_ORGANISMS.md) — non-parasitic
  comparative nematodes (*C. briggsae*) and necromenic associates
  (*P. pacificus*); some insect-parasitic nematodes are cross-listed there.
