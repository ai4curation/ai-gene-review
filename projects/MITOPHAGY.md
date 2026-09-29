---
title: "PINK1-Parkin Mitophagy Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [OPTN, CALCOCO2, SQSTM1, TAX1BP1, NBR1, TBK1, BNIP3L, VCP]   # reviewed genes only; full candidate list is in the table below
manifest:
  slides:
    - href: MITOPHAGY/slides/MITOPHAGY-slides.html
  artifacts:
    - href: https://claude.ai/artifact/6cKsT95CWm1eYy7upcA6HU
      title: Project brief
---

# PINK1-Parkin Mitophagy Project

**Bottom line:** scoped, not yet started as a project. In PINK1-Parkin
mitophagy, the PINK1 kinase accumulates on damaged mitochondria and makes
phospho-ubiquitin, which activates the Parkin (PRKN) E3 ligase; ubiquitin-binding
receptors (OPTN, CALCOCO2, SQSTM1, TAX1BP1, NBR1) then link the organelle to
the autophagosome. The candidate table below lists 14 human genes, but there is
no mitophagy module and PINK1 and PRKN themselves have not been reviewed. Eight
candidates already have reviews made for Proteostasis and other projects (OPTN,
CALCOCO2, SQSTM1, TAX1BP1, NBR1, TBK1, BNIP3L, VCP). In those reviews mitophagy
is a core function of OPTN (`type 2 mitophagy`, GO:0061734), CALCOCO2 and
BNIP3L, and a non-core role of SQSTM1. BNIP3, FUNDC1, PHB2 and MFN2 are also
unreviewed. The worm counterpart, [CAEEL_MITOPHAGY](CAEEL_MITOPHAGY.md), is
much further along.

## Overview

Mitophagy is the selective autophagy of damaged mitochondria. The PINK1-Parkin pathway is the best-characterized mitophagy pathway, where mitochondrial damage stabilizes PINK1 kinase, which recruits and activates the Parkin E3 ubiquitin ligase.

## Model Species

**Primary: Homo sapiens (human)**
- Parkinson's disease relevance
- Well-characterized pathway

## Core Pathway Architecture

### 1. Damage Sensing
- **PINK1** - Kinase, stabilized on damaged mitochondria
- **TOMM complex** - PINK1 import/stabilization

### 2. Ubiquitin Ligase
- **PRKN** (Parkin) - E3 ubiquitin ligase
- **Phospho-ubiquitin** - PINK1 product, Parkin activator

### 3. Mitophagy Receptors
Ubiquitin-binding autophagy receptors:
- **OPTN** - Optineurin
- **CALCOCO2** (NDP52) - Autophagy receptor
- **SQSTM1** (p62) - Autophagy receptor
- **TAX1BP1** - Autophagy receptor
- **NBR1** - Autophagy receptor

### 4. Autophagy Machinery
- **ULK1 complex** - Initiation
- **LC3/GABARAP** - Autophagosome proteins
- **TBK1** - Phosphorylates receptors

### 5. Alternative Mitophagy
PINK1/Parkin-independent:
- **BNIP3/BNIP3L** (NIX) - Receptor-mediated
- **FUNDC1** - Hypoxia-induced
- **PHB2** - Inner membrane receptor

## Candidate Genes (14)

| Gene | UniProt | Function |
|------|---------|----------|
| PINK1 | Q9BXM7 | Kinase |
| PRKN | O60260 | E3 ligase |
| OPTN | Q96CV9 | Receptor |
| CALCOCO2 | Q13137 | NDP52 receptor |
| SQSTM1 | Q13501 | p62 receptor |
| TAX1BP1 | Q86VP1 | Receptor |
| NBR1 | Q14596 | Receptor |
| TBK1 | Q9UHD2 | Kinase |
| BNIP3 | Q12983 | Receptor |
| BNIP3L | O60238 | NIX receptor |
| FUNDC1 | Q8IVP5 | Receptor |
| PHB2 | Q99623 | Inner membrane receptor |
| VCP | P55072 | Extraction |
| MFN2 | O95140 | Parkin substrate |

## Disease Relevance

- Parkinson's disease (PINK1, PRKN mutations)
- ALS (OPTN, TBK1 mutations)
- Mitochondrial diseases

## Project Status

- [ ] Stub - needs gene folder setup
