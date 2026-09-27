---
title: "Yeast Cell Cycle & Translation Control"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [yeast]
---

# Yeast Cell Cycle & Translation Control

**Bottom line:** scoped, not yet started. Budding yeast commits to division at
Start, where Cln3-Cdc28 inactivates the Whi5 repressor and the G1 cyclins, the
CDK inhibitor Sic1 and the B-type cyclins then drive entry into S phase. This
project plans to review the GO annotations of 23 *S. cerevisiae* genes spanning
that circuit and the translation and ribosome-biogenesis machinery thought to
time it. The aim is to test whether GO captures translational control of the
cell cycle as well as it captures the transcriptional program. As of this
update only TOR1 has a gene review in the repo (67 annotations assessed);
the other 22 genes have no review folder, and the checklist below
still reads 0 of 23. The list also needs a symbol check before work starts:
yeast eIF1 is SUI1, and "EIF3" names a complex rather than a gene.

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

Last updated: 2025-12-30

## Genes to Review

### G1 Cyclins & Cell Cycle Entry
- [ ] CLN3 - G1 cyclin (cell size sensor, upstream of translational control)
- [ ] CLN1 - G1 cyclin (redundant with CLN2)
- [ ] CLN2 - G1 cyclin (critical output of Start mechanism)
- [ ] SIC1 - CDK inhibitor (Clb-CDK inhibitor)
- [ ] WHI5 - CKI (transcriptional repressor of G1-S genes)

### S/G2/M Cyclins & Checkpoint Control
- [ ] CLB5 - S-phase cyclin (replication licensing)
- [ ] CLB6 - S-phase cyclin (replication licensing)
- [ ] CLB1 - M-phase cyclin
- [ ] CLB2 - M-phase cyclin

### CDK & Cell Cycle Kinases
- [ ] CDC28 - CDK (master cell cycle kinase)
- [ ] DBF4 - Cdc7 binding partner (licensing factor)
- [ ] SWE1 - CDK inhibitor (checkpoint control)

### Ribosome Biogenesis & Translation
- [ ] RPS3 - 40S ribosomal subunit protein
- [ ] RPL3 - 60S ribosomal subunit protein
- [ ] IMP3 - Ribosome biogenesis factor
- [ ] SHE2 - Ribosome biogenesis factor
- [ ] RRN3 - rRNA transcription factor

### Translation Factors & Regulators
- [ ] EIF1 - Translation initiation factor
- [ ] EIF2A - Translation initiation factor
- [ ] EIF3 - Translation initiation factor
- [ ] TIF1 - Eukaryotic initiation factor 4A (DEAD-box helicase)

### Cell Size & Growth Control
- [ ] TOR1 - Target of rapamycin (growth/nutrient sensing)
- [ ] MSN2 - Stress response transcription factor

## Progress

- Total genes: 23
- Reviewed: 0
- In progress: 0
- Completed: 0

---

# NOTES

## 2025-12-30

- Project initialized
- Focus: cell cycle entry, G1-S transition, translational checkpoints
- Selected 23 genes spanning cyclins, CDK machinery, ribosome biogenesis, and translation factors
- Emphasis on emerging translational control mechanisms (Cln3/Whi5 regulatory circuits)
- Ready to begin gene review workflow

## Slides

- [Slides](YEAST_CELL_CYCLE/slides/YEAST_CELL_CYCLE-slides.html) (Marp source: [YEAST_CELL_CYCLE-slides.md](YEAST_CELL_CYCLE/slides/YEAST_CELL_CYCLE-slides.md)) — AI generated
