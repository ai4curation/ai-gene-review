---
title: "Yeast Cell Cycle & Translation Control"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [yeast]
last_reviewed: '2026-10-29'
genes: [CLN3, CLN2, CLN1, SIC1, WHI5, CLB5, CLB6, CLB2, CDC28, SWE1, SUI2, TOR1]   # reviewed genes only; full candidate list is in the checklist below
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
transcriptional program. Twelve rows now have gene reviews in the repo when the
EIF2A entry is normalized to the standard yeast symbol SUI2 (542 annotations
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

Last updated: 2026-10-29

## Genes to Review

### G1 Cyclins & Cell Cycle Entry
- Done: CLN3 - G1 cyclin (cell size sensor, upstream of translational control)
- Done: CLN1 - G1 cyclin (G1/S cyclin paralogous to CLN2)
- Done: CLN2 - G1 cyclin (critical output of Start mechanism)
- Done: SIC1 - CDK inhibitor (Clb-CDK inhibitor)
- Done: WHI5 - Start transcriptional corepressor of SBF-dependent G1-S genes

### S/G2/M Cyclins & Checkpoint Control
- Done: CLB5 - S-phase cyclin (replication-origin firing)
- Done: CLB6 - S-phase cyclin (early replication origins; Clb6-specific Swi6 and Rnr2 substrates)
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
- Reviewed: 12
- Open review or symbol-triage rows: 11
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

## 2026-10-23

- CLN1 reviewed (24 GOA annotations), completing the G1 cyclin trio alongside
  CLN2 and CLN3. Actions mirror the CLN2 review because CLN1's annotation set is
  a strict subset of CLN2's: `GO:0016538` refined to `GO:0061575`, the seven bare
  `GO:0005515` rows to `GO:0019901`, and the two unsigned "regulation of G1/S"
  rows to `GO:1900087`.
- One candidate `NEW` was considered and rejected on a comparator check:
  `GO:0180040 negative regulation of pheromone response MAPK cascade` is carried
  by only PPQ1 and AKR1 in budding yeast, and not by CLN2 despite its stronger
  Ste5 evidence. SGD's convention for the Cln-pheromone relationship is
  `GO:0000321` instead. Recorded as a suggested question.
- Deep research was unavailable this run (no provider API keys), so CLN1's
  literature synthesis is in `CLN1-notes.md` rather than a
  `-deep-research-<provider>.md` file.
- Remaining queue (12 rows): CLB6, CLB1, DBF4, RPS3, RPL3, IMP3, SHE2, RRN3,
  SUI1, an eIF3 subunit selection, TIF1, MSN2.

## 2026-10-29

- CLB6 reviewed (25 GOA annotations), completing the S-phase cyclin pair with
  CLB5. The review turns on the two ways Clb6 is *not* interchangeable with
  Clb5: it fires only early origins and it is destroyed at the G1/S border by
  SCF-Cdc4, so the phenotypic asymmetry between the paralogs is largely one of
  protein lifetime (hyperstabilized Clb6 rescues the clb5 slow S phase).
- Four actions differ from the CLB5 review because CLB6-specific full-text
  evidence exists where CLB5's did not. `GO:0032880 regulation of protein
  localization` was refined to `GO:0046827 positive regulation of protein export
  from nucleus`: Clb6-Cdc28 is the only one of the nine Cdc28 cyclins that
  phosphorylates Swi6 Ser160 (driving its nuclear export) and Rnr2 at its TPSK
  motif (releasing Rnr2-Rnr4 from the Wtm1 anchor), two independent substrates
  agreeing on the direction. The `regulation of DNA-templated transcription`
  row, left UNDECIDED for CLB5, is supportable for CLB6 through the Swi6
  mechanism and is kept as non-core; the sign is not assignable because
  exporting Swi6 removes SBF activation and relieves MBF repression at once.
- The four `GO:0016538` rows were refined to `GO:0061575`, matching the CLN1 and
  CLN2 treatment: Clb5 and Clb6 are described as the primary activators of the
  S-phase function of Cdc28, so the unsigned regulator term is one step too
  general. The propagated `microtubule organizing center` and `traversing Start`
  rows were flagged as over-annotations on the same grounds as in CLB5 (the MTOC
  sub-node is seeded by mitotic cyclins, and Clb6 is gone before spindle
  assembly).
- No new annotations were proposed. The `clb5 clb6` sister-chromatid cohesion
  defect under replication stress is real but is only published for the double
  mutant, so it is recorded in `CLB6-notes.md` rather than asserted for CLB6.
- Deep research was again unavailable (no provider API keys), so the literature
  synthesis is in `CLB6-notes.md`.
- Remaining queue (11 rows): CLB1, DBF4, RPS3, RPL3, IMP3, SHE2, RRN3, SUI1, an
  eIF3 subunit selection, TIF1, MSN2.
