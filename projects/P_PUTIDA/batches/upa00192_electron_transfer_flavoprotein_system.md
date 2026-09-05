---
title: "PSEPK electron-transfer flavoprotein system"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [etfA, etfB, PP_4203, PP_0312, PP_0313]
autolink_gene_symbols: false
---

# PSEPK electron-transfer flavoprotein system

- Module: `electron_transfer_flavoprotein_system`
- Focused genes: two ETF alpha/beta pairs and one ETF:quinone oxidoreductase
- Satisfiability: core relay complete at PP_4201-PP_4203
- Module research: running
- Gene-level OpenScientist research: running

## Boundary

This module covers the conserved ETF electron relay, not every upstream
flavin-dependent dehydrogenase that can donate electrons to it. The PP_4201-
PP_4203 locus encodes an ETF alpha/beta heterodimer and ETF:quinone
oxidoreductase, satisfying both stages of the relay. PP_0312-PP_0313 encode a
second ETF-family alpha/beta pair. Their family identity is clear, but this
first pass does not assign a specific physiological donor pathway to that pair.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Soluble ETF electron acceptor | EtfA Q88F97 and EtfB Q88F96 | Covered |
| ETF reoxidation and quinone reduction | PP_4203 Q88F95 | Covered |
| Alternative ETF heterodimer | PP_0312 Q88R22 and PP_0313 Q88R21 | Present; donor specificity unresolved |

## Gene Curation

| Gene | Locus | UniProt | Review | OpenScientist |
|---|---|---|---|---|
| `etfA` | PP_4201 | Q88F97 | Curated and validated | Running |
| `etfB` | PP_4202 | Q88F96 | Curated and validated | Running |
| `PP_4203` | PP_4203 | Q88F95 | Curated and validated | Running |
| `PP_0312` | PP_0312 | Q88R22 | Curated and validated | Running |
| `PP_0313` | PP_0313 | Q88R21 | Curated and validated | Running |

## Curation Findings

The reusable module now represents bacterial and mitochondrial ETF systems
without making mitochondrial localization part of the universal definition.
Electron transfer is assigned directly to the redox-active alpha subunit and
ETF:quinone oxidoreductase; the beta subunit is represented as a necessary
partner that contributes to heterodimer function. The second KT2440 ETF pair is
retained as a family-grounding exemplar without an unsupported substrate claim.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-electron-transfer-flavoprotein-system__ppu00071-deep-research-openscientist.md)
- `modules/electron_transfer_flavoprotein_system.yaml`
