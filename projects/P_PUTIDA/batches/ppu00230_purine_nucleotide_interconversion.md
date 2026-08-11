---
title: "PSEPK bacterial purine nucleotide interconversion"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [purA, purB, guaB, guaA, adk, gmk, ndk]
autolink_gene_symbols: false
---

# PSEPK bacterial purine nucleotide interconversion

This batch extracts seven proteins from KEGG `ppu00230` to test a reusable
bacterial module spanning the IMP branch point and connected nucleotide
phosphate-state interconversion. It is deliberately separate from the existing
human-focused purine nucleotide-cycle module.

## Workflow

- [x] Inspect the 65-member `ppu00230` source snapshot and prior de novo IMP PR.
- [x] Fetch exact KT2440 UniProt and GOA records for the six missing reviews.
- [x] Audit all 51 GOA rows across the seven focused gene reviews.
- [x] Model a species-neutral module with four substantive root parts.
- [x] Run full generic OpenScientist research; the request exhausted its
  7,200-second provider window without producing a report.
- [ ] Module + `ppu00230` + PSEPK OpenScientist research is active and
  non-blocking at publication time.
- [x] Validate the seven focused gene reviews.

## Module Boundary

| Part | Reactions | KT2440 exemplars |
|---|---|---|
| IMP to AMP | IMP to adenylosuccinate to AMP | `purA` / PP_4889 / Q88DD8; `purB` / PP_4016 / Q88FR7 |
| IMP to GMP | IMP to XMP to GMP | `guaB` / PP_1031 / Q88P22; `guaA` / PP_1032 / Q88P21 |
| Adenylate exchange | AMP + ATP reversible with 2 ADP | `adk` / PP_1506 / P0A136 |
| Guanylate phosphorylation | GMP to GDP to GTP | `gmk` / PP_5296 / Q88C87; `ndk` / PP_0849 / Q88PK1 |

PurB appears in both this module and de novo IMP synthesis for different
physiological reactions: adenylosuccinate cleavage belongs here, whereas SAICAR
cleavage remains in the PRPP-to-IMP module. Ndk is retained because GDP-to-GTP
phosphorylation is the shared terminal step of the guanine branch; its UTP,
CTP, and deoxyribonucleotide roles remain valid in the gene review but are not
expanded into module branches.

## Exclusions

The module does not include PRPP-to-IMP synthesis, purine uptake or
phosphoribosyltransferase salvage entry, AMP deamination, alarmone metabolism,
cyclic-nucleotide signaling, noncanonical NTP sanitization, or broad purine
degradation. Those are distinct pathways or regulatory contexts despite their
co-occurrence on KEGG `ppu00230`.

## Annotation Review

- Exact catalytic activities and specific biosynthetic processes are accepted.
- Generic catalytic, oxidoreductase, kinase, and broad biosynthetic parents are
  modified to verified enzyme-specific or branch-specific terms.
- ATP/GTP/nucleotide and metal-binding annotations are retained as non-core
  where chemically valid.
- Redundant `cytoplasm` is modified to `cytosol` only for Gmk, where both terms
  occur in the same GOA record.
- Ndk's UTP and CTP biosynthetic annotations are retained as valid non-purine
  functions rather than removed to fit this module's scope.

The dedicated source table is
[`ppu00230_purine_nucleotide_interconversion.tsv`](ppu00230_purine_nucleotide_interconversion.tsv).

## Research

The generic OpenScientist request was allowed its full 7,200-second timeout and
returned no provider artifact. The species-aware request was launched with the
same full timeout and is not required to complete before this draft PR opens.
