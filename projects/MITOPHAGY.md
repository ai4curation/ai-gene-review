# PINK1-Parkin Mitophagy Project

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

## Candidate Genes (~18)

| Gene | UniProt | Function |
|------|---------|----------|
| PINK1 | Q9BXM7 | Kinase |
| PRKN | O60260 | E3 ligase |
| OPTN | Q96CV9 | Receptor |
| CALCOCO2 | Q13137 | NDP52 receptor |
| SQSTM1 | Q13501 | p62 receptor |
| TAX1BP1 | Q86VP1 | Receptor |
| TBK1 | Q9UHD2 | Kinase |
| BNIP3 | Q12983 | Receptor |
| BNIP3L | O60238 | NIX receptor |
| FUNDC1 | Q8IVP5 | Receptor |
| VCP | P55072 | Extraction |
| MFN2 | O95140 | Parkin substrate |

## Disease Relevance

- Parkinson's disease (PINK1, PRKN mutations)
- ALS (OPTN, TBK1 mutations)
- Mitochondrial diseases

## Project Status

- [ ] Stub - needs gene folder setup
