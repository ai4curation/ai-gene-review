---
title: "Stress Granule Assembly Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [TIA1, TIAL1, USP10, TARDBP, HNRNPA2B1, VCP]   # reviewed genes only; full candidate list is in the table below
---

# Stress Granule Assembly Project

**Bottom line:** scoped, not yet started as a project. Stress granules are
membraneless RNA-protein condensates that form when translation initiation
stalls under stress; G3BP1/G3BP2 and TIA1/TIAL1 nucleate them, and several
ALS/FTD proteins (TDP-43, FUS, hnRNPA1/A2B1, ATXN2) partition into them. The
candidate table below lists 16 human genes, but there is no stress granule module and
the core nucleators G3BP1 and G3BP2 have not been reviewed. Six candidates
already have reviews made for other projects (TIA1, TIAL1, USP10, TARDBP,
HNRNPA2B1, VCP). The stress-granule rows were accepted for TIA1 (8 rows,
including `stress granule assembly`, GO:0034063), TIAL1 (with `stress granule
assembly` added as NEW), TARDBP, and VCP (including `stress granule
disassembly`, GO:0035617). USP10's three `negative regulation of stress granule
assembly` rows were kept as non-core. Ten candidates, including CAPRIN1,
FUS, HNRNPA1, ATXN2 and PABPC1, are unreviewed. The related [CONDENSATES](CONDENSATES.md) project
covers how GO should represent condensates in general.

## Overview

Stress granules are membraneless organelles formed via liquid-liquid phase separation (LLPS) during cellular stress. They sequester stalled translation initiation complexes and are implicated in neurodegenerative diseases including ALS and FTD.

## Model Species

**Primary: Homo sapiens (human)**
- Major disease relevance (ALS, FTD)
- Well-characterized in human cells

## Core Pathway Architecture

### 1. Core Nucleators
Proteins essential for stress granule assembly:
- **G3BP1** - Core nucleator, Ras-GTPase activating SH3 binding protein
- **G3BP2** - G3BP1 paralog
- **TIA1** - T-cell intracellular antigen 1
- **TIAR** (TIAL1) - TIA1-related protein

### 2. RNA-Binding Proteins
Recruited to stress granules:
- **PABPC1** - Poly(A) binding protein
- **CAPRIN1** - G3BP interactor
- **USP10** - G3BP interactor, deubiquitinase
- **FMR1** (FMRP) - Fragile X protein

### 3. Disease-Associated Proteins
Mutated in ALS/FTD:
- **TARDBP** (TDP-43) - RNA binding protein
- **FUS** - Fused in sarcoma
- **HNRNPA1/A2B1** - hnRNPs
- **ATXN2** - Ataxin-2

### 4. Translation Machinery
- **EIF2S1** (eIF2α) - Phosphorylation triggers SG assembly
- **EIF4G1** - Translation initiation factor
- **40S ribosomal subunits**

### 5. Disassembly Factors
- **VCP** (p97) - AAA+ ATPase
- **Chaperones** (HSP70 family)

## Candidate Genes (16)

| Gene | UniProt | Function |
|------|---------|----------|
| G3BP1 | Q13283 | Core nucleator |
| G3BP2 | Q9UN86 | Core nucleator |
| TIA1 | P31483 | Nucleator |
| TIAL1 | Q01085 | TIAR |
| CAPRIN1 | Q14444 | G3BP interactor |
| USP10 | Q14694 | G3BP regulator |
| TARDBP | Q13148 | TDP-43 |
| FUS | P35637 | ALS gene |
| HNRNPA1 | P09651 | RNA binding |
| HNRNPA2B1 | P22626 | RNA binding |
| ATXN2 | Q99700 | ALS modifier |
| VCP | P55072 | Disassembly |
| PABPC1 | P11940 | Poly(A) binding |
| FMR1 | Q06787 | FMRP |
| EIF2S1 | P05198 | eIF2α |
| EIF4G1 | Q04637 | Translation initiation |

## Key Recent Discoveries (2020+)

- G3BP1/2 as core nucleators (structural basis)
- Phase separation dynamics
- Stress granule-autophagy crosstalk
- Role in viral infection

## Disease Relevance

- ALS (TDP-43, FUS, ATXN2 mutations)
- Frontotemporal dementia
- Viral infection
- Cancer (stress adaptation)

## Project Status

- [ ] Stub - needs gene folder setup

## Slides

- [Slides](STRESS_GRANULES/slides/STRESS_GRANULES-slides.html) (Marp source: [STRESS_GRANULES-slides.md](STRESS_GRANULES/slides/STRESS_GRANULES-slides.md)) — AI generated
