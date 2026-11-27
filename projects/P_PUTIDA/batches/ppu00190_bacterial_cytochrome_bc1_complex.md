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
| `petA` | PP_1317 | Q88N95 | Curated and validated | Complete — `genes/PSEPK/petA/petA-deep-research-openscientist.md` |
| `petB` | PP_1318 | Q88N94 | Curated and validated | Running |
| `petC` | PP_1319 | Q88N93 | Curated and validated | Running |

## Curation Findings

The complete quinol:cytochrome c reductase reaction requires all three
subunits, so neither PetA nor PetB `enables GO:0008121` on its own. The two
existing annotations were handled differently because the two genes are not in
the same position. PetB already carries `GO:0009055 electron transfer activity`
in its own GOA, so its `GO:0008121` row is `MARK_AS_OVER_ANNOTATED` and the
subunit-level function is simply the term it already has. PetA has no
`GO:0009055` row, so there is nothing to defer to: its row is `MODIFY` with
`proposed_replacement_terms: GO:0009055`, following the same treatment of this
subunit and term in `genes/human/UQCRFS1` and `genes/worm/isp-1`. In both cases
`core_functions` records `GO:0008121` as a `contributes_to` activity of complex
III. Direct electron-transfer, 2Fe-2S, b-heme, c-heme, membrane, and
complex-membership roles are retained at the corresponding leaves.

## Evidence

- `modules/bacterial_cytochrome_bc1_complex.yaml`
- PSEPK UniProt and GOA records for PetA, PetB, and PetC
