---
title: "Parasites"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [STECR, 9BILA]
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
| *Steinernema carpocapsae* | Entomopathogenic (insect-parasitic) nematode | ❌ not yet | Best-annotated EPN. UniProt code `STECR`, NCBITaxon:34508. **Holds the genus's only reviewed (Swiss-Prot) entry:** `D2KBH9` (NAS8_STECR), a secreted astacin metalloprotease — a natural parasitism-relevant anchor. |
| *Steinernema hermaphroditum* | Entomopathogenic (insect-parasitic) nematode | ❌ not yet | Mutualist of *Xenorhabdus*; emerging genetic model for EPN/symbiosis biology. UniProt code `9BILA` (provisional, auto-assigned), NCBITaxon:289476 → `genes/9BILA/`. No reviewed entries. |

Additional parasites (other *Steinernema*/*Heterorhabditis* EPNs, parasitic
helminths, protozoan parasites) to be added as reviews are scoped.

## Genes for review

- [ ] *Steinernema carpocapsae* `STECR` **nas-8** (`D2KBH9`, zinc metalloproteinase
  / astacin, EC 3.4.24.21) — the genus's only Swiss-Prot entry and the
  recommended first parasite seed; secreted protease relevant to host invasion.
  Fetch with `just fetch-gene STECR D2KBH9 --alias nas-8`.
- [ ] *Steinernema hermaphroditum* (`9BILA`, NCBITaxon:289476) — seed gene(s)
  TBD; not yet fetched into the repo. No reviewed entries, so any seed is a
  TrEMBL accession. Candidate areas: infective-juvenile development, host-immune
  evasion, and the *Xenorhabdus* symbiosis interface.

## Status / next steps

- **SCOPING.** No parasite genes from the nematode scope are in the repo yet.
- **Annotation availability (UniProt, 2026-06):** across the **whole genus
  *Steinernema*** there is exactly **1 reviewed (Swiss-Prot) entry** — `D2KBH9`
  (NAS8_STECR, *S. carpocapsae* astacin metalloprotease). *S. hermaphroditum*
  (`9BILA`) has **0 reviewed** entries (~36,000 TrEMBL); *S. carpocapsae*
  (`STECR`) has 1 reviewed + ~35,200 TrEMBL.
- **Recommended anchor:** seed *S. carpocapsae* `nas-8` (`D2KBH9`) first — it is
  reviewed and parasitism-relevant — then expand to *S. hermaphroditum* TrEMBL
  genes paired with literature + bioinformatics rather than relying on existing
  GO annotation.
- Pull the [PARASITE_IMMUNE_MODULATORS](PARASITE_IMMUNE_MODULATORS.md) candidate
  list under this umbrella's "host-modulation" sub-topic.

## Related projects

- [PARASITE_IMMUNE_MODULATORS](PARASITE_IMMUNE_MODULATORS.md) — parasite/
  blood-feeder secreted proteins that modulate host immunity (sub-topic).
- [SATELLITE_MODEL_ORGANISMS](SATELLITE_MODEL_ORGANISMS.md) — non-parasitic
  comparative nematodes (*C. briggsae*) and necromenic associates
  (*P. pacificus*); some insect-parasitic nematodes are cross-listed there.
