---
title: "PSEPK bacterial cytochrome bc1 complex"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [petA, petB, petC]
autolink_gene_symbols: false
---

# PSEPK bacterial cytochrome bc1 complex

- Module: `bacterial_cytochrome_bc1_complex`
- Source bucket: KEGG `ppu00190`
- Focused genes: `petABC`/PP_1317-PP_1319
- Satisfiability: complete
- Module and gene OpenScientist research: running

## Boundary

This module covers the canonical three-subunit cytochrome bc1 respiratory
complex. It excludes complexes I, II, IV, ATP synthase, and the terminal
oxidases that share the broad oxidative-phosphorylation map. It also excludes
non-homologous alternative complex III systems.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Rieske high-potential electron branch | PetA Q88N95 | Covered |
| Cytochrome b Q-cycle membrane core | PetB Q88N94 | Covered |
| Cytochrome c1 output branch | PetC Q88N93 | Covered |

## Gene Curation

| Gene | Locus | UniProt | Review | OpenScientist |
|---|---|---|---|---|
| `petA` | PP_1317 | Q88N95 | Curated and validated | Running |
| `petB` | PP_1318 | Q88N94 | Curated and validated | Running |
| `petC` | PP_1319 | Q88N93 | Curated and validated | Running |

## Curation Findings

The complete quinol:cytochrome c reductase reaction requires all three
subunits. Existing `enables GO:0008121` annotations on PetA and PetB were
therefore marked as complex-level over-annotations, while core synthesis records
their contribution to the assembled activity. Direct electron-transfer,
2Fe-2S, b-heme, c-heme, membrane, and complex-membership roles are retained at
the corresponding leaves.

## Evidence

- `modules/bacterial_cytochrome_bc1_complex.yaml`
- PSEPK UniProt and GOA records for PetA, PetB, and PetC
