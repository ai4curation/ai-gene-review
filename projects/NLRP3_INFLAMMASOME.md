---
title: "NLRP3 Inflammasome Assembly Project"
maturity: SCOPING
last_reviewed: "2026-10-04"
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [NLRP3, CASP4, GSDMD]   # reviewed genes only; full candidate list is in the table below
manifest:
  slides:
    - href: NLRP3_INFLAMMASOME/slides/NLRP3_INFLAMMASOME-slides.html
      description: AI generated
---

# NLRP3 Inflammasome Assembly Project

**Bottom line:** the NLRP3 inflammasome is a danger-sensing complex in which
the sensor NLRP3 recruits the adaptor PYCARD (ASC) to activate caspase-1, which
matures IL-1β and IL-18 and cleaves gasdermin D to open pyroptotic pores.
Scoped, not yet started as a project: this page lists ten candidate human genes
and the pathway architecture, but no project-specific review work has been
done. Three candidates already have complete reviews from other work (NLRP3,
CASP4 and GSDMD, 364 annotations between them; most removals are generic
`protein binding` rows, 24 of 25 on NLRP3), and the NLRP3 review proposes a
new GO term, *inflammasome sensor activity*, because GO:0140299 molecular
sensor activity requires binding the sensed molecule. The adaptor PYCARD, the effector
`CASP1`, `CASP5`, `IL1B`, `IL18`, `NEK7` and `BRCC3` have no gene folder. A draft
[NLR signaling module](../modules/nlr_signaling.html) already includes NLRP3,
`PYCARD` and `CASP1` and is the natural home for an inflammasome model.

We scoped this because NLRP3 is a major therapeutic target and drives
autoinflammatory disease (CAPS) and inflammation in gout, atherosclerosis and
Alzheimer disease, and recent work on activation sites, post-translational
control and structure is likely to be under-represented in GO.

## Overview

The NLRP3 inflammasome is a multiprotein complex that activates inflammatory caspases in response to diverse danger signals, leading to IL-1β/IL-18 release and pyroptotic cell death. Recent discoveries have clarified activation mechanisms and identified new regulators.

## Model Species

**Primary: Homo sapiens (human)**
- Major therapeutic target
- Autoinflammatory disease relevance

## Core Pathway Architecture

### 1. Sensor
- **NLRP3** - NOD-like receptor, sensor component

### 2. Adaptor
- **`PYCARD`** (ASC) - Adaptor with PYD and CARD domains

### 3. Effector Caspases
- **`CASP1`** - Caspase-1, cleaves pro-IL-1β
- **CASP4/`CASP5`** - Non-canonical inflammasome

### 4. Substrates/Outputs
- **`IL1B`** - Pro-inflammatory cytokine
- **`IL18`** - Pro-inflammatory cytokine
- **GSDMD** - Gasdermin D, pore-forming executioner

### 5. Critical Regulators
- **`NEK7`** - NLRP3 licensing cofactor/regulator
- **`BRCC3`** - Deubiquitinase
- **Various negative regulators**

### 6. Priming/Licensing
- **NFKB pathway** - Transcriptional priming

## Candidate Genes

| Gene | UniProt | Function |
|------|---------|----------|
| NLRP3 | Q96P20 | Sensor |
| `PYCARD` | Q9ULZ3 | ASC adaptor |
| `CASP1` | P29466 | Effector caspase |
| CASP4 | P49662 | Non-canonical |
| `CASP5` | P51878 | Non-canonical |
| GSDMD | P57764 | Pore formation |
| `IL1B` | P01584 | Cytokine |
| `IL18` | Q14116 | Cytokine |
| `NEK7` | Q8TDX7 | NLRP3 licensing cofactor |
| `BRCC3` | P46736 | Deubiquitinase |

## Key Recent Discoveries (2020+)

- Trans-Golgi network as NLRP3 activation site
- Post-translational modifications regulating assembly
- Structural basis of inflammasome assembly
- GSDMD pore structure

## Disease Relevance

- CAPS (Cryopyrin-associated periodic syndromes)
- Gout, atherosclerosis
- Alzheimer's disease
- COVID-19 severity

## Project Status

- [x] Cross-project reviews checked for NLRP3, CASP4 and GSDMD
- [ ] Fetch and review `PYCARD`, `CASP1`, `CASP5`, `IL1B`, `IL18`, `NEK7`
  and `BRCC3`
  ([#3954](https://github.com/ai4curation/ai-gene-review/issues/3954))
- [ ] Extend the draft NLR signaling module with inflammasome assembly,
  caspase-1 activation and gasdermin D cleavage after the core genes are reviewed
