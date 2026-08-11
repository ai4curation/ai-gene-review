---
title: "PSEPK bacterial chromosomal DNA replication"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [dnaA, dnaN, dnaB, dnaG, ssb, dnaEA, dnaX, dnaQ, ligA]
autolink_gene_symbols: false
---

# PSEPK bacterial chromosomal DNA replication

- Module: `bacterial_chromosomal_dna_replication`
- Source bucket: KEGG `ppu03030` (DNA replication)
- Focused genes: nine proteins spanning seven mechanistic parts
- Satisfiability: complete at the conserved replisome level
- OpenScientist module and gene research: running

## Boundary

This module covers DnaA initiation, DnaB/SSB fork opening and protection, DnaG
priming, DNA polymerase III synthesis and proofreading, DnaN processivity,
DnaX clamp loading, and LigA nick sealing. DNA polymerase I, RNase H, repair
exonucleases, and LigB are adjacent replication/repair activities outside this
focused replisome realization.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Origin initiation | DnaA P0A116 | Covered |
| Fork unwinding and protection | DnaB Q88DF2 and SSB Q88QK5 | Covered |
| Primer synthesis | DnaG P0A118 | Covered |
| Polymerase core and proofreading | DnaE Q88MG5 and DnaQ Q88FF6 | Covered |
| Sliding-clamp processivity | DnaN P0A120 | Covered |
| Clamp loading | DnaX Q88F30 | Covered |
| Nick sealing | LigA Q88F25 | Covered |

## Curation Findings

Catalytic molecular functions are attached only to DnaB, DnaG, DnaE, DnaQ,
and LigA leaves. Structural replisome components are represented by their roles
rather than being assigned the molecular function of the complete complex. The
obsolete DNA primase term is not authored; DnaG uses current RNA-polymerase and
primer-synthesis terms.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-chromosomal-dna-replication__ppu03030-deep-research-openscientist.md)
- `modules/bacterial_chromosomal_dna_replication.yaml`
