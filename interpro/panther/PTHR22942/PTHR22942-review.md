# PANTHER Family Review: PTHR22942

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR22942 |
| **Family Name** | DNA repair and recombination RadA/Rad51 (RecA/Rad51/RadA DNA strand-pairing family) |
| **InterPro Entry** | (none integrated in metadata) |
| **Total Proteins** | 12,413 |
| **Taxonomic Breadth** | 11,291 taxa |
| **Subfamilies** | 5 |
| **Representative Structure** | 2z43 (Structure of a twinned crystal of RadA) |
| **Anchor Gene** | S. pombe rhp51 / rad51 (P36601) |

## Executive Summary

PTHR22942 is the eukaryotic/archaeal **RecA/Rad51/RadA strand-pairing recombinase** family — the central catalytic engine of **homologous recombination (HR)**. All members are RecA-fold ATPases that bind single-stranded DNA (and dsDNA), assemble into helical nucleoprotein filaments, perform a homology search, and catalyze **DNA strand invasion and strand exchange** using cycles of ATP binding and hydrolysis. Through this conserved chemistry the family repairs DNA double-strand breaks, protects and restarts stalled/collapsed replication forks, and drives meiotic recombination.

The conserved core (ssDNA binding, dsDNA binding, DNA-dependent ATPase, strand exchange, recombinase filament assembly) is shared across the family. **Neofunctionalization** is modest and largely a division of labor between the **mitotic recombinase (Rad51)** and the **meiosis-specific recombinase (Dmc1/Lim15)**, plus accessory **Rad51 paralogs (RadB/Rad55/Rad57-type)** that act as mediators rather than primary strand-exchange enzymes. The fission-yeast anchor **rhp51 (Rad51)** is the canonical mitotic+meiotic recombinase.

## Subfamily Analysis

Based on the family entry table (103 members with PANTHER subfamily IDs):

### PTHR22942:SF30 — MEIOTIC RECOMBINATION PROTEIN DMC1/LIM15 HOMOLOG
**Members**: 62 (largest sampled subfamily)

**Key Members**:
- S. pombe dmc1 (O42634)
- Dmc1/Lim15 orthologs across plants, fungi, and animals

**Function**: Meiosis-specific strand-exchange recombinase. Same core chemistry as Rad51 but specialized for inter-homolog recombination during meiosis I.

### PTHR22942:SF47 — DNA REPAIR AND RECOMBINATION PROTEIN RADB
**Members**: 22

**Function**: RadB / Rad51-paralog-type proteins. These are accessory recombination factors (mediator/regulatory role) related to the core recombinase but generally not the primary strand-exchange enzyme.

### PTHR22942:SF39 — DNA REPAIR PROTEIN RAD51 HOMOLOG 1  *(ANCHOR SUBFAMILY)*
**Members**: 16

**Key Members**:
- **S. pombe rhp51 / rad51 (P36601)** — the anchor
- Human RAD51 (Q06609)
- Mouse Rad51 (Q08297), chicken RAD51A (P37383)
- S. cerevisiae RAD51 (P25454)
- Arabidopsis RAD51 (P94102), tomato (Q40134), maize RAD51B (Q9XED7)
- Drosophila spn-A (Q27297)

**Function**: The canonical **Rad51 mitotic + meiotic strand-exchange recombinase**. ATP-dependent assembly of presynaptic filaments on ssDNA, homology search, strand invasion and exchange. This is the anchor gene's subfamily, populated by bona fide RAD51 orthologs across the eukaryotic tree.

### PTHR22942:SF66 / SF69 — additional Rad51-paralog clades
**Members**: SF66 (2), SF69 (1).

**Notes**: SF66 includes S. pombe rhp57 (Q9UUL2), a Rad55/Rad57-type paralog (mediator complex with Rhp55). SF69 is annotated "DNA REPAIR PROTEIN RAD51 HOMOLOG A". These small clades represent paralogous mediators/sub-specializations rather than independent biochemical functions.

## IBA Annotation Assessment

IBAs (GO_REF:0000033) propagated to rhp51, with the PANTHER seed node and our recorded action:

| GO ID | GO label | Aspect | Node | Our action | Assessment |
|-------|----------|--------|------|------------|------------|
| GO:0003690 | double-stranded DNA binding | MF | PTN001415033 | ACCEPT | **CORRECT.** Filament formation involves dsDNA binding (homology search / heteroduplex). Conserved family function. |
| GO:0003697 | single-stranded DNA binding | MF | PTN001415033 | ACCEPT | **CORRECT.** Presynaptic filament assembly on resected ssDNA is the defining step of the recombinase; experimentally established for S. pombe Rad51. |
| GO:0000150 | DNA strand exchange activity | MF | PTN001415033 | ACCEPT | **CORRECT.** The core catalytic function; experimentally demonstrated for S. pombe Rad51 (forms filaments, catalyzes ATP-dependent strand exchange). |
| GO:0008094 | ATP-dependent activity, acting on DNA | MF | PTN001415033 | ACCEPT | **CORRECT.** DNA-stimulated ATPase powering filament dynamics; conserved RecA-fold property. |
| GO:0042148 | DNA strand invasion | BP | PTN001415033 | ACCEPT | **CORRECT.** Direct output of the strand-exchange reaction. |
| GO:0006312 | mitotic recombination | BP | PTN001415033 | ACCEPT | **CORRECT.** Rhp51 is required for mitotic HR (gene conversion, fork protection). |
| GO:0000730 | DNA recombinase assembly | BP | PTN001415033 | ACCEPT | **CORRECT.** Self-assembly into the helical filament is the active form of the recombinase. |
| GO:0007131 | reciprocal meiotic recombination | BP | PTN000534635 | KEEP_AS_NON_CORE | **REASONABLE.** Rhp51 contributes to meiotic recombination, but the meiosis-dedicated enzyme is Dmc1 (SF30); marking the meiotic BP non-core for the mitotic recombinase is well calibrated. |
| GO:0070192 | chromosome organization involved in meiotic cell cycle | BP | PTN000534635 | KEEP_AS_NON_CORE | **REASONABLE.** Meiotic-context process from the Dmc1-shared node; appropriately non-core. |
| GO:0000794 | condensed nuclear chromosome | CC | PTN000534635 | KEEP_AS_NON_CORE | **ACCEPTABLE (localization flag).** Rhp51 acts on nuclear chromatin and forms nuclear foci; the "condensed chromosome" CC comes from the meiosis-shared node. Consistent with known nuclear localization — no contradiction — but kept non-core. |

**Triage flags.** Several MF/BP terms carry `CROSS_SUBFAMILY` (other_sf includes PTHR22942:SF30, the Dmc1 clade). Per calibration this is **triage, not a verdict**: ssDNA binding, dsDNA binding, ATPase, strand exchange and recombinase assembly are **deeply conserved across the whole RecA/Rad51/RadA family**, so transfer from a node spanning Rad51 and Dmc1 is expected and biologically correct — both are strand-exchange recombinases doing the same chemistry. The terms anchored on the Dmc1-shared node PTN000534635 (meiotic recombination, condensed chromosome) are the only ones plausibly clade-skewed, and our review already demotes those to non-core rather than removing them. No IBA on rhp51 warrants REMOVE; there is no positive biological argument that any propagated function is wrong for a Rad51 ortholog.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata, family entry table, S. pombe rhp51 UniProt/GOA/AI-review, iba_propagation.tsv
