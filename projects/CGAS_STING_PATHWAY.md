---
title: "cGAS-STING Cytosolic DNA Sensing Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
---

# cGAS-STING Cytosolic DNA Sensing Project

**Bottom line:** cGAS senses DNA in the cytosol and makes the second messenger
2'3'-cGAMP, which activates the ER adaptor STING1; STING1 then recruits TBK1 to
phosphorylate IRF3 and switch on type I interferon. Scoped, not yet started as
a project: this page lists ten candidate human genes and the pathway
architecture, but no project-specific review work has been done. Three
candidates already have complete reviews from other projects (STING1, TBK1 and
IFI16, 529 annotations between them). The other seven, including the sensor
CGAS itself, have no gene folder. The next step is `just fetch-gene human
<GENE>` for CGAS, IRF3, TREX1, ENPP1, SAMHD1, IRF7 and IFNB1, then review.

We scoped this because the pathway links innate immunity to autoimmune disease
(AGS, SAVI, lupus), cancer immunotherapy and senescence, and many of its
regulators were described after 2020, so existing GO annotation is likely to lag
the literature.

## Overview

The cGAS-STING pathway is a critical innate immune signaling system that detects cytosolic DNA (from pathogens, damaged mitochondria, or genomic instability) and triggers type I interferon responses. Many regulators and disease connections have been discovered 2020+.

## Model Species

**Primary: Homo sapiens (human)**
- Cancer immunotherapy relevance
- Autoimmune disease connections

## Core Pathway Architecture

### 1. DNA Sensing
- **CGAS** (MB21D1) - Cyclic GMP-AMP synthase, DNA sensor
- **IFI16** - Alternative DNA sensor

### 2. Second Messenger
- **cGAMP** - 2'3'-cyclic GMP-AMP (product of cGAS)
- **ENPP1** - Degrades extracellular cGAMP

### 3. Signal Transduction
- **STING1** (TMEM173) - ER-resident adaptor
- **TBK1** - Tank-binding kinase 1
- **IRF3** - Interferon regulatory factor 3
- **NFKB1** - NF-κB pathway

### 4. Negative Regulators
- **TREX1** - Cytosolic exonuclease (prevents self-DNA sensing)
- **SAMHD1** - dNTPase, HIV restriction factor
- **Various ubiquitin regulators**

### 5. Downstream Effectors
- **Type I interferons** - IFNA, IFNB
- **Inflammatory cytokines**

## Candidate Genes (~15)

| Gene | UniProt | Function |
|------|---------|----------|
| CGAS | Q8N884 | DNA sensor |
| STING1 | Q86WV6 | Adaptor protein |
| TBK1 | Q9UHD2 | Kinase |
| IRF3 | Q14653 | Transcription factor |
| TREX1 | Q9NSU2 | Negative regulator |
| ENPP1 | P22413 | cGAMP hydrolase |
| IFI16 | Q16666 | DNA sensor |
| SAMHD1 | Q9Y3Z3 | dNTPase |
| IRF7 | Q92985 | Transcription factor |
| IFNB1 | P01574 | Type I interferon |

## Key Recent Discoveries (2020+)

- STING trafficking and degradation mechanisms
- cGAMP transfer between cells
- STING agonists in cancer therapy
- Mitochondrial DNA sensing in aging
- STING in senescence

## Disease Relevance

- Cancer immunotherapy (STING agonists)
- Autoimmunity (AGS, SAVI, lupus)
- Viral infection
- Aging/senescence

## Project Status

- [ ] Stub - needs gene folder setup
