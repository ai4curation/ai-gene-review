---
title: "PSEPK bacterial terminal oxidase branches"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_0103, ctaD, PP_0105, PP_0106, cyoA, cyoB, cyoC, cyoD, ccoN-I, ccoO-I, ccoQ-I, ccoP-I, ccoN-II, ccoO-II, ccoQ-II, ccoP-II, cioA, cioB]
autolink_gene_symbols: false
---

# PSEPK bacterial terminal oxidase branches

- Module: `bacterial_terminal_oxidases`
- Source bucket: KEGG `ppu00190`
- Focused genes: 18
- Terminal branches: aa3, bo3, two cbb3 operons, and CioAB
- Satisfiability: multiple branches present
- Module and gene OpenScientist research: running

## Boundary

The terminal-oxidase layer is a branched respiratory module, not one protein
complex. Cytochrome c oxidases and quinol oxidases use different electron donors,
and KT2440 retains several coexisting variants with different physiological
regimes. Complexes I-III, ATP synthase, heme synthesis, and unrelated ppu00190
members are outside this module.

## Branches

| Donor class | Variant | PSEPK realization | Assessment |
|---|---|---|---|
| Cytochrome c | aa3 oxidase | PP_0103, CtaD Q88RM5, CtaG PP_0105, PP_0106 | Covered |
| Cytochrome c | cbb3 oxidase I | CcoN/O/Q/P-I, Q88F49-Q88F46 | Covered |
| Cytochrome c | cbb3 oxidase II | CcoN/O/Q/P-II, Q88F44-Q88F41 | Covered |
| Quinol | bo3 oxidase | CyoA-D, Q88PN7-Q88PN4 | Covered |
| Quinol | cyanide-insensitive oxidase | CioA Q88E17, CioB Q88E18 | Covered |

## Curation Findings

The complete oxygen-reduction activities belong to assembled oxidase complexes.
Those MFs were marked as over-annotations when propagated as independently
enabled by individual subunits. Core synthesis now records direct cofactor or
electron-transfer roles where present and uses
`contributes_to_molecular_function` for the complex reaction. CtaG is kept as
an aa3 copper-center assembly factor rather than a stoichiometric oxidase
subunit. Generic membrane terms were removed when a more precise plasma-membrane
annotation was already present.

## Focused Genes

| Branch | Genes | Review status |
|---|---|---|
| aa3 | `PP_0103`, `ctaD`, `PP_0105`, `PP_0106` | Curated and validated |
| bo3 | `cyoA`, `cyoB`, `cyoC`, `cyoD` | Curated and validated |
| cbb3-I | `ccoN-I`, `ccoO-I`, `ccoQ-I`, `ccoP-I` | Curated and validated |
| cbb3-II | `ccoN-II`, `ccoO-II`, `ccoQ-II`, `ccoP-II` | Curated and validated |
| Cio | `cioA`, `cioB` | Curated and validated |

## Evidence

- `modules/bacterial_terminal_oxidases.yaml`
- PSEPK UniProt and GOA records for all 18 focused proteins
- OpenScientist terminal-oxidase module report and gene reports are in progress
