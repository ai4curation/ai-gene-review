---
title: "PSEPK bacterial F-type ATP synthase"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [atpA, atpB, atpC, atpD, atpE, atpF, atpG, atpH]
autolink_gene_symbols: false
---

# PSEPK bacterial F-type ATP synthase

- Module: `bacterial_f_type_atp_synthase`
- Source bucket: KEGG `ppu00190` (oxidative phosphorylation)
- Focused genes: eight proteins in the contiguous `atpC-D-G-A-H-F-E-B` locus
- Satisfiability: complete
- Module research: running
- Gene-level OpenScientist research: running

## Boundary

This batch covers the canonical bacterial F1Fo ATP synthase. The F1 catalytic
head, central rotor, peripheral stator, and Fo proton-translocating rotor are
modeled as four distinct functional parts. The broader oxidative-phosphorylation
bucket also contains respiratory dehydrogenases, cytochrome complexes, terminal
oxidases, pyrophosphatase, and polyphosphate enzymes; those do not satisfy ATP
synthase subunit roles and are curated in separate modules.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| F1 alpha/beta catalytic head | AtpA Q88BX2, AtpD Q88BX4 | Covered |
| Gamma/epsilon central rotor | AtpG Q88BX3, AtpC Q88BX5 | Covered |
| Peripheral stator | AtpF Q88BX0, AtpH Q88BX1 | Covered |
| Fo proton channel and c ring | AtpB Q88BW8, AtpE Q88BW9 | Covered |

## Gene Curation

| Gene | Locus | UniProt | Review | OpenScientist |
|---|---|---|---|---|
| `atpC` | PP_5412 | Q88BX5 | Curated and validated | Running |
| `atpD` | PP_5413 | Q88BX4 | Curated and validated | Running |
| `atpG` | PP_5414 | Q88BX3 | Curated and validated | Running |
| `atpA` | PP_5415 | Q88BX2 | Curated and validated | Running |
| `atpH` | PP_5416 | Q88BX1 | Curated and validated | Running |
| `atpF` | PP_5417 | Q88BX0 | Curated and validated | Running |
| `atpE` | PP_5418 | Q88BW9 | Curated and validated | Running |
| `atpB` | PP_5419 | Q88BW8 | Curated and validated | Running |

## Curation Findings

The complete proton-driven rotary ATP-synthesis activity belongs to the
assembled F1Fo complex, not independently to each structural subunit. Subunit
reviews therefore distinguish direct properties such as nucleotide binding,
proton translocation, lipid interaction, and complex membership from
contribution to the assembled enzyme's activity. The module carries no
molecular-function assertion at its root; functions are attached only to the
subunit annotons that directly perform them.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-f-type-atp-synthase__ppu00190-deep-research-openscientist.md)
- `modules/bacterial_f_type_atp_synthase.yaml`
