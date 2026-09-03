---
title: "PSEPK bacterial succinate dehydrogenase"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [sdhA, sdhB, sdhC, sdhD, sdhE]
autolink_gene_symbols: false
---

# PSEPK bacterial succinate dehydrogenase

- Module: `bacterial_succinate_dehydrogenase`
- Source buckets: KEGG `ppu00020` and `ppu00190`
- Structural complex: SdhABCD
- Maturation factor: SdhE
- Satisfiability: complete
- Module OpenScientist research: running

## Boundary

This module covers the non-proton-pumping succinate dehydrogenase/respiratory
complex II system. It includes SdhE-mediated SdhA flavinylation, the SdhA/SdhB
catalytic head, and the SdhC/SdhD membrane quinone domain. The paralogous
fumarate reductase reaction and mitochondrial-specific assembly machinery are
outside scope.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| SdhA covalent flavin maturation | SdhE Q88MZ4 | Covered |
| Succinate oxidation and Fe-S relay | SdhA Q88FA7, SdhB Q88FA8 | Covered |
| Membrane anchoring and quinone reduction | SdhC Q88FA5, SdhD Q88FA6 | Covered |

## Gene Curation

| Gene | Locus | UniProt | Review | OpenScientist |
|---|---|---|---|---|
| `sdhA` | PP_4191 | Q88FA7 | Revised and validated | Present |
| `sdhB` | PP_4190 | Q88FA8 | Revised and validated | Present |
| `sdhC` | PP_4193 | Q88FA5 | Revised and validated | Present |
| `sdhD` | PP_4192 | Q88FA6 | Revised and validated | Present |
| `sdhE` | PP_1424 | Q88MZ4 | Curated and validated | Running |

## Curation Findings

SdhA directly enables the FAD-dependent succinate-oxidation half-reaction, and
SdhB directly enables electron transfer. Neither independently performs the
complete quinone-coupled SdhABCD reaction, so the existing whole-complex MF was
reclassified as an over-annotation and retained in core synthesis through
`contributes_to_molecular_function`. Complex membership is recorded with
GO:0045273. SdhE is an assembly factor, not a stoichiometric complex subunit.

## Evidence

- Existing PSEPK SdhA, SdhB, SdhC, and SdhD OpenScientist reports
- `modules/bacterial_succinate_dehydrogenase.yaml`
