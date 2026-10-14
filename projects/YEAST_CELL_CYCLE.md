---
title: "Yeast Cell Cycle & Translation Control"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [yeast]
last_reviewed: '2026-10-05'
genes: [CLN3, CLN2, SIC1, WHI5, CLB5, CLB2, CDC28, SWE1, SUI2, TOR1]   # reviewed genes only; full candidate list is in the checklist below
manifest:
  slides:
    - href: YEAST_CELL_CYCLE/slides/YEAST_CELL_CYCLE-slides.html
      description: Yeast cell-cycle translation-control slides
---

# Yeast Cell Cycle & Translation Control

**Bottom line:** scoped, with the Start/CDK core partly reviewed. Budding yeast
commits to division at Start, where Cln3-Cdc28 inactivates the Whi5 repressor
and the G1 cyclins, the CDK inhibitor Sic1 and the B-type cyclins then drive
entry into S phase. This project plans to review the GO annotations of 23
*S. cerevisiae* rows spanning that circuit and the translation and
ribosome-biogenesis machinery thought to time it. The aim is to test whether GO
captures translational control of the cell cycle as well as it captures the
transcriptional program. Ten rows now have gene reviews in the repo when the
EIF2A entry is normalized to the standard yeast symbol SUI2 (493 annotations
assessed); the remaining rows still need review or symbol triage. The list also
needs cleanup before the translation branch starts: yeast eIF1 is SUI1, "EIF3"
names a complex rather than a gene, and SHE2 needs a narrower rationale than
ribosome biogenesis.

## Overview

This project reviews *Saccharomyces cerevisiae* genes central to **cell cycle regulation** with emphasis on novel **translational control mechanisms** discovered in 2024. The focus bridges classical cell cycle biology with emerging understanding of how **translation factors** and **ribosome dynamics** control cell-cycle-dependent gene expression independent of transcriptional regulation.

## Key Research Areas

1. **G1 Phase & Cell Cycle Entry** - Transcriptional and translational mechanisms controlling Start
2. **Cyclin-CDK Complexes** - CLN (G1 cyclins), CLB (S/G2/M cyclins) and regulation
3. **Cell Size Checkpoint Control** - Cln3, Whi5, and emerging translational checkpoints
4. **mRNA Translation During Cell Cycle** - Global and gene-specific translation changes
5. **Ribosome Biogenesis** - Coupled to cell cycle and cell size
6. **CDK Inhibitors & Regulation** - Sic1, Cdk inhibition mechanisms

## Biological Significance

- **Conservation** - Cell cycle mechanisms highly conserved in higher eukaryotes
- **Translation as regulatory layer** - Post-transcriptional control drives cell-cycle timing
- **Cell size sensing** - Novel mechanisms linking growth, ribosome capacity, and cycle entry
- **Disease relevance** - Cancer cells dysregulate similar mechanisms
- **Synthetic biology** - Engineering cell cycle timing for biotechnology

## Project Goals

- Review genes controlling G1-S transition with focus on translational regulation
- Assess GO annotations for cell-cycle-dependent translation control
- Identify genes at intersection of ribosome biogenesis and cell cycle
- Propose refined annotations reflecting translational checkpoints
- Create reference for cell cycle regulation research

---

# STATUS

Last updated: 2026-10-04

## Genes to Review

### G1 Cyclins & Cell Cycle Entry
- Done: CLN3 - G1 cyclin (cell size sensor, upstream of translational control)
- Todo: CLN1 - G1 cyclin (redundant with CLN2)
- Done: CLN2 - G1 cyclin (critical output of Start mechanism)
- Done: SIC1 - CDK inhibitor (Clb-CDK inhibitor)
- Done: WHI5 - Start transcriptional corepressor of SBF-dependent G1-S genes

### S/G2/M Cyclins & Checkpoint Control
- Done: CLB5 - S-phase cyclin (replication-origin firing)
- Todo: CLB6 - S-phase cyclin (replication-origin firing)
- Todo: CLB1 - M-phase cyclin
- Done: CLB2 - M-phase cyclin

### CDK & Cell Cycle Kinases
- Done: CDC28 - CDK (master cell cycle kinase)
- Todo: DBF4 - Cdc7-Dbf4 regulatory subunit for replication-origin firing
- Done: SWE1 - Wee1-family Cdc28 Tyr19 kinase (morphogenesis checkpoint)

### Ribosome Biogenesis & RNA Localization
- Todo: `RPS3` - 40S ribosomal subunit protein
- Todo: RPL3 - 60S ribosomal subunit protein
- Todo: IMP3 - Ribosome biogenesis factor
- Todo: SHE2 - ASH1 mRNA localization factor; confirm the cell-cycle rationale
- Todo: RRN3 - rRNA transcription factor

### Translation Factors & Regulators
- Todo: SUI1 - eIF1 translation initiation factor
- Done: SUI2 - eIF2 alpha subunit
- Todo: eIF3 subunit TBD - eIF3 is a complex; select the yeast subunit(s) before review
- Todo: TIF1 - Eukaryotic initiation factor 4A (DEAD-box helicase)

### Cell Size & Growth Control
- Done: TOR1 - Target of rapamycin (growth/nutrient sensing)
- Todo: MSN2 - Stress response transcription factor

## Progress

- Total rows: 23
- Reviewed: 10
- Open review or symbol-triage rows: 13
- In progress: 0
- Remaining work: [#3960](https://github.com/ai4curation/ai-gene-review/issues/3960)

---

# NOTES

## 2025-12-30

- Project initialized
- Focus: cell cycle entry, G1-S transition, translational checkpoints
- Selected 23 genes spanning cyclins, CDK machinery, ribosome biogenesis, and translation factors
- Emphasis on emerging translational control mechanisms (Cln3/Whi5 regulatory circuits)
- Ready to begin gene review workflow
