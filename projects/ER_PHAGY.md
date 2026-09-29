---
title: "ER-phagy (Selective ER Autophagy) Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [SEC62, ATL3, ULK1, ATG9A, EIF2AK3]   # reviewed genes only; full candidate list is in the table below
manifest:
  slides:
    - href: ER_PHAGY/slides/ER_PHAGY-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/JUWPntJaSWNzA2RferrHAX
      title: Project brief
---

# ER-phagy (Selective ER Autophagy) Project

**Bottom line:** scoped, not yet started as a project. ER-phagy is the selective
autophagy of endoplasmic reticulum, carried out by ER-membrane receptors
(FAM134B/RETREG1, RTN3, SEC62, CCPG1, TEX264, ATL3) that bind ATG8-family
proteins such as LC3B and GABARAP. The candidate table below lists 12 human genes, but
no ER-phagy-specific work has been done: there is no module and no gene review
made for this project. Five candidates were reviewed for other projects (SEC62
and ATL3 for Proteostasis, ULK1 and ATG9A for the CONDENSATES phagophore audit,
EIF2AK3 as a Proteostasis review). Of those, SEC62 keeps its IMP `reticulophagy`
(GO:0061709) annotation as non-core, and the ATL3 review declined to add
reticulophagy without better evidence. The receptors that define the field,
RETREG1, RTN3, CCPG1 and TEX264, have no review yet.

## Overview

ER-phagy is the selective autophagy of endoplasmic reticulum, mediated by specific receptor proteins that link ER membranes to the autophagy machinery. Most receptors were characterized 2017-2023, making this a relatively new field with recent discoveries.

## Model Species

**Primary: Homo sapiens (human)**
- Most receptors characterized in human cells
- Disease relevance (neurodegeneration, viral infection)

## Core Pathway Architecture

### ER-phagy Receptors
Proteins that bridge ER to autophagosomes via LC3-interacting regions (LIRs):
- **FAM134B** (RETREG1) - Reticulon-like, sheet ER-phagy
- **RTN3** - Reticulon 3, tubular ER
- **SEC62** - Translocon-associated, recovER-phagy
- **CCPG1** - Cell cycle progression gene 1
- **TEX264** - Three-way junction ER-phagy
- **ATL3** - Atlastin-3, tubular ER

### Core Autophagy Machinery
- **MAP1LC3B** - LC3B, autophagosome marker
- **GABARAP family** - Alternative ATG8 family members
- **ULK1 complex** - Autophagy initiation
- **ATG9A** - Membrane source

### ER Stress Connection
- **ERN1** (IRE1α) - ER stress sensor
- **EIF2AK3** (PERK) - ER stress kinase

## Candidate Genes (12)

| Gene | UniProt | Function |
|------|---------|----------|
| FAM134B | Q9H6L5 | ER-phagy receptor (sheets) |
| RTN3 | O95197 | ER-phagy receptor (tubules) |
| SEC62 | Q99442 | RecovER-phagy receptor |
| CCPG1 | Q9ULG6 | ER-phagy receptor |
| TEX264 | Q9Y6I9 | ER-phagy receptor |
| ATL3 | Q6DD88 | ER-phagy receptor |
| MAP1LC3B | Q9GZQ8 | Autophagosome protein |
| GABARAP | O95166 | ATG8 family |
| ULK1 | O75385 | Autophagy kinase |
| ATG9A | Q7Z3C6 | Membrane trafficking |
| ERN1 | O75460 | IRE1α, ER stress sensor |
| EIF2AK3 | Q9NZJ5 | PERK, ER stress kinase |

## Key Recent Discoveries (2020+)

- TEX264 as ER-phagy receptor (2019-2020)
- ATL3 in tubular ER-phagy
- Structural basis of receptor-LC3 interactions
- ER-phagy in viral infection

## Disease Relevance

- Hereditary sensory neuropathy (FAM134B mutations)
- ER storage diseases
- Viral infection (Zika, Dengue exploit ER-phagy)

## Project Status

- [ ] Stub - needs gene folder setup
