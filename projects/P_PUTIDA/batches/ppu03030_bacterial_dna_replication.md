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
- Focused reviews: nine proteins spanning seven mechanistic parts
- Additional loader exemplars: HolA, HolB, and HolC
- Cross-species grounding: reviewed Escherichia coli K-12 exemplars for every modeled role
- Satisfiability: complete at the conserved replisome level
- OpenScientist module + pathway + taxon research: complete in 2,293.92 seconds

## Boundary

This module covers DnaA initiation, DnaB/SSB fork opening and protection, DnaG
priming, DNA polymerase III synthesis and proofreading, DnaN processivity,
DnaX/HolA/HolB/HolC clamp loading, and LigA nick sealing. DNA polymerase I,
RNase H, repair exonucleases, and LigB are adjacent replication/repair
activities outside this focused replisome realization.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Origin initiation | DnaA P0A116 | Covered |
| Fork unwinding and protection | DnaB Q88DF2 and SSB Q88QK5 | Covered |
| Primer synthesis | DnaG P0A118 | Covered |
| Polymerase core and proofreading | DnaE Q88MG5 and DnaQ Q88FF6 | Covered |
| Sliding-clamp processivity | DnaN P0A120 | Covered |
| Clamp loading | DnaX Q88F30, HolA Q88DM9, HolB Q88LG7, HolC Q88P74 | Covered; psi/theta assignment unresolved |
| Nick sealing | LigA Q88F25 | Covered |

## Curation Findings

Molecular functions are attached only to leaf annotons, including DnaA origin
binding, SSB single-stranded DNA binding, DnaN processivity-factor activity,
and DnaX contribution to the multisubunit clamp-loader activity. DnaB and DnaE
use the specific activities selected by their gene reviews. The obsolete DNA
primase term is not authored; DnaG uses current RNA-polymerase and
primer-synthesis terms.

The annotation-reviewer workflow was applied to every current GOA row for dnaA,
dnaB, dnaEA, dnaG, dnaN, dnaQ, dnaX, ligA, and ssb; each gene's notes record the
consultation outcome. Complex-level DNA polymerase assignments were removed
from noncatalytic DnaN and DnaX, polymerase assignments were removed from the
DnaQ proofreading subunit, and the unverified DnaEA PHP-domain exonuclease
claim remains explicitly undecided.

The regenerated KEGG batch contains all 18 current `ppu03030` members. It marks
the eight pathway-bucket genes curated here as complete while retaining the
out-of-boundary DNA polymerase I, RNase H, repair-exonuclease, auxiliary clamp-
loader, and LigB entries as unreviewed. DnaA is included in the focused module
from its origin-initiation role but is primarily partitioned to `ppu02020`, so
it is not a `ppu03030` TSV member.

The completed OpenScientist report independently recovers all seven parts. It
also flags PP_0353, PP_4768, and PP_3893 as non-core candidates requiring
separate gene review; none is used to satisfy the module because DnaQ and DnaB
already cover the corresponding proofreading and helicase roles.

The report proposes PP_1552/Q88ML9 as a DnaC helicase loader, but current
UniProt and the local gene list instead identify it only as an unnamed phage
replication protein and expose no KT2440 dnaC, dnaI, or dciA entry. That
assignment is not imported into the module. Pol I and RNase H are retained as
adjacent Okazaki-maturation context rather than required parts of this focused
replisome module.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial_chromosomal_dna_replication__ppu03030-deep-research-openscientist.md)
- `modules/bacterial_chromosomal_dna_replication.yaml`
