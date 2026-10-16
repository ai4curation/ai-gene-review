---
title: "ER-phagy (Selective ER Autophagy) Project"
maturity: SCOPING
last_reviewed: 2026-10-04
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [SEC62, ATL3, CALCOCO1, RETREG2, UBAC2, CDK5RAP3, MAP1LC3B, GABARAP, ULK1, ATG9A, ERN1, EIF2AK3]   # reviewed genes only; full candidate list is in the table below
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
autophagy of endoplasmic reticulum, carried out by ER-membrane receptors and
soluble or cytosolic cargo adaptors that bind ATG8-family proteins such as LC3B
and GABARAP. The candidate table below lists 16 seed or related human genes. No
review has been made specifically for this ER_PHAGY project and no local
`modules/*.yaml` module exists yet, although a cached human GO-CAM already covers
the UFMylation/CYB5R3 reticulophagy branch. Twelve table genes already have
local review folders from other projects: eight are COMPLETE (SEC62, ATL3,
CALCOCO1, RETREG2, UBAC2, CDK5RAP3, ERN1 and EIF2AK3), MAP1LC3B and GABARAP
are DRAFT, and ULK1 and ATG9A still have INITIALIZED CONDENSATES phagophore
reviews. SEC62 keeps its IMP `reticulophagy` (GO:0061709) annotation as
non-core; CALCOCO1, RETREG2 and UBAC2 capture reticulophagy as a core
receptor/adaptor process; CDK5RAP3 captures UFM1-dependent positive regulation
of reticulophagy; and the ATL3 review declined to add reticulophagy without
better evidence. The defining membrane receptors RETREG1, RTN3, CCPG1 and
TEX264 still have no review.

## Overview

ER-phagy is the selective autophagy of endoplasmic reticulum, mediated by receptor and adaptor proteins that link ER membranes to the autophagy machinery. Many receptors were characterized from the mid-2010s into the 2020s, making this a relatively new field with recent discoveries.

The cached GO-CAM model `65f3ae5c00000585` already captures one curated human
subpath, in which UFMylation of CYB5R3 promotes reticulophagy and CYB5R3
degradation. A future local module should therefore either reuse that
UFMylation/CYB5R3 branch or focus on the LC3/GABARAP-binding receptor set that is
not yet represented in `modules/`.

## Model Species

**Primary: Homo sapiens (human)**
- Most receptors characterized in human cells
- Disease relevance (neurodegeneration, viral infection)

## Core Pathway Architecture

### ER-phagy Receptors and Adaptors
Proteins that bridge ER to autophagosomes via LC3/GABARAP-binding motifs:
- **RETREG1** (FAM134B) - Reticulon-like, sheet ER-phagy
- **RTN3** - Reticulon 3, tubular ER
- **SEC62** - Translocon-associated, recovER-phagy
- **CCPG1** - Cell cycle progression gene 1
- **TEX264** - Three-way junction ER-phagy
- **ATL3** - Atlastin-3, tubular ER
- **CALCOCO1** - Soluble selective-autophagy adaptor for reticulophagy and Golgiphagy
- **RETREG2** - RETREG/FAM134-family ER-phagy receptor
- **UBAC2** - ER-membrane GABARAP-binding ER-phagy receptor
- **CDK5RAP3** - C53, UFM1/ATG8-binding reticulophagy regulator

### Core Autophagy Machinery
- **MAP1LC3B** - LC3B, autophagosome marker
- **GABARAP family** - Alternative ATG8 family members
- **ULK1 complex** - Autophagy initiation
- **ATG9A** - Membrane source

### ER Stress Connection
- **ERN1** - ER stress sensor
- **EIF2AK3** (PERK) - ER stress kinase

## Candidate Genes (16)

| Gene | UniProt | Function |
|------|---------|----------|
| RETREG1 | Q9H6L5 | ER-phagy receptor (sheets) |
| RTN3 | O95197 | ER-phagy receptor (tubules) |
| SEC62 | Q99442 | RecovER-phagy receptor |
| CCPG1 | Q9ULG6 | ER-phagy receptor |
| TEX264 | Q9Y6I9 | ER-phagy receptor |
| ATL3 | Q6DD88 | ER-phagy receptor |
| CALCOCO1 | Q9P1Z2 | Soluble ER/Golgi-phagy adaptor |
| RETREG2 | Q8NC44 | ER-phagy receptor |
| UBAC2 | Q8NBM4 | ER-phagy receptor |
| CDK5RAP3 | Q96JB5 | UFM1-dependent reticulophagy adaptor/regulator |
| MAP1LC3B | Q9GZQ8 | Autophagosome protein |
| GABARAP | O95166 | ATG8 family |
| ULK1 | O75385 | Autophagy kinase |
| ATG9A | Q7Z3C6 | Membrane trafficking |
| ERN1 | O75460 | ER stress sensor |
| EIF2AK3 | Q9NZJ5 | PERK, ER stress kinase |

## Key Recent Discoveries (2019+)

- TEX264 as ER-phagy receptor (2019-2020)
- ATL3 in tubular ER-phagy
- CALCOCO1 as a soluble ER/Golgi-phagy adaptor
- UFM1-dependent C53/CDK5RAP3 reticulophagy
- Structural basis of receptor-LC3 interactions
- ER-phagy in viral infection

## Disease Relevance

- Hereditary sensory neuropathy (RETREG1/FAM134B mutations)
- ER storage diseases
- Viral infection (Zika, Dengue exploit ER-phagy)

## Project Status

- [x] Cross-project reviews checked for SEC62, ATL3, CALCOCO1, RETREG2, UBAC2,
  CDK5RAP3, MAP1LC3B, GABARAP, ULK1, ATG9A, ERN1 and EIF2AK3
- [ ] Fetch and review RETREG1, RTN3, CCPG1 and TEX264
  ([#3957](https://github.com/ai4curation/ai-gene-review/issues/3957))
- [ ] Build an ER-phagy module around LC3/GABARAP-binding ER-phagy receptors and adaptors
