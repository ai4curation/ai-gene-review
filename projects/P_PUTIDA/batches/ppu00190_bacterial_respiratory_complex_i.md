---
title: "PSEPK bacterial respiratory complex I"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [nuoA, nuoB, nuoC, nuoE, nuoF, nuoG, nuoH, nuoI, nuoJ, nuoK, nuoL, nuoM, nuoN]
autolink_gene_symbols: false
---

# PSEPK bacterial respiratory complex I

- Module: `bacterial_respiratory_complex_i`
- Source bucket: KEGG `ppu00190` (oxidative phosphorylation)
- Focused genes: 13 proteins encoding 14 canonical Nuo subunits
- Satisfiability: complete
- Module research: complete
- Gene-level OpenScientist research: running

## Boundary

The focused module is proton-translocating respiratory complex I (NDH-1), encoded
by the contiguous `nuoA-N` locus PP_4119-PP_4131. PP_4121 is a fused NuoC/D
protein, so one gene satisfies two conserved subunit roles. The broader KEGG
bucket also contains complexes II-V, terminal oxidases, polyphosphate enzymes,
and heme-biosynthesis proteins; those belong to separate modules.

`ndh`/PP_0626 is a type-II NADH dehydrogenase. It is non-homologous,
non-proton-pumping, and must not satisfy a complex I role. Eukaryotic
supernumerary NDUF subunits are not expected in the bacterial 14-subunit core.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| NADH-input N-module | NuoE Q88FH4, NuoF Q88FH3, NuoG Q88FH2 | Covered |
| Quinone-reduction Q-module | NuoB Q88FH6, fused NuoC/D Q88FH5, NuoI Q88FH0 | Covered |
| Membrane coupling interface | NuoA Q88FH7, NuoH Q88FH1, NuoJ Q88FG9, NuoK Q88FG8 | Covered |
| Antiporter-like proton-pumping arm | NuoL Q88FG7, NuoM Q88FG6, NuoN Q88FG5 | Covered |

## Gene Curation

| Gene | Locus | UniProt | Review | OpenScientist |
|---|---|---|---|---|
| `nuoA` | PP_4119 | Q88FH7 | Curated and validated | Running |
| `nuoB` | PP_4120 | Q88FH6 | Curated and validated | Running |
| `nuoC` | PP_4121 | Q88FH5 | Curated and validated; C/D fusion | Running |
| `nuoE` | PP_4122 | Q88FH4 | Curated and validated | Running |
| `nuoF` | PP_4123 | Q88FH3 | Curated and validated | Running |
| `nuoG` | PP_4124 | Q88FH2 | Curated and validated | Running |
| `nuoH` | PP_4125 | Q88FH1 | Curated and validated | Running |
| `nuoI` | PP_4126 | Q88FH0 | Curated and validated | Running |
| `nuoJ` | PP_4127 | Q88FG9 | Curated and validated | Running |
| `nuoK` | PP_4128 | Q88FG8 | Curated and validated | Running |
| `nuoL` | PP_4129 | Q88FG7 | Curated and validated | Running |
| `nuoM` | PP_4130 | Q88FG6 | Curated and validated | Running |
| `nuoN` | PP_4131 | Q88FG5 | Curated and validated | Running |

## Curation Findings

Individual subunits should not be represented as independently enabling the
complete NADH:quinone oxidoreductase reaction. Those IEA annotations were marked
as complex-level over-annotations while each core function records contribution
to the assembled activity. The explicitly non-electrogenic NADH dehydrogenase
term was removed from Nuo subunits because it contradicts the proton-pumping
NDH-1 system. Direct FMN, NAD(H), and iron-sulfur roles were retained on the
appropriate peripheral-arm proteins.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__mitochondrial_complex_i_core__ppu00190-deep-research-openscientist.md)
- `modules/bacterial_respiratory_complex_i.yaml`
