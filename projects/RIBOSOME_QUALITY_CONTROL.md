---
title: "Ribosome Quality Control (RQC) Project"
maturity: IN_PROGRESS
last_reviewed: 2026-10-05
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [ZNF598, EDF1, GIGYF2, PELO, HBS1L, ABCE1, NEMF, LTN1, TCF25, ANKZF1, ASCC3, ASCC2, VCP]
manifest:
  slides:
    - href: RIBOSOME_QUALITY_CONTROL/slides/RIBOSOME_QUALITY_CONTROL-slides.html
      description: AI generated
---

# Ribosome Quality Control (RQC) Project

**Bottom line:** ribosome quality control detects stalled and colliding
ribosomes, splits them, and destroys the incomplete nascent chain: ZNF598 and
EDF1 sense collisions, PELO-HBS1L and ABCE1 split the ribosome, and the NEMF-LTN1
RQC complex ubiquitinates the chain left on the 60S subunit. All 13 candidate
genes on this page now have complete gene reviews, made during the Proteostasis
batches, whose co-translational QC selection covers RQC, rather than under this
project; the stale "Stub" line has been cleared and the remaining module/GO-CAM
follow-up is tracked in
[#3952](https://github.com/ai4curation/ai-gene-review/issues/3952). Across the
12 RQC genes (VCP excluded) the reviews assess 430 GOA rows: 276 ACCEPT, 95
KEEP_AS_NON_CORE, 20 REMOVE, 18 MARK_AS_OVER_ANNOTATED, 17 MODIFY and 4 NEW.
The 97 rows that use RQC-specific terms, such as `rescue of stalled cytosolic
ribosome` (GO:0072344) and `RQC complex` (GO:1990112), were all accepted or
added; the corrections fall on generic `protein binding` rows and on off-pathway
terms such as DNA replication for ASCC2/ASCC3. No RQC module has been built yet,
although six production GO-CAMs in `gocams/` already model parts of the pathway.

## Overview

Ribosome quality control is a cytosolic surveillance pathway that detects stalled
and collided ribosomes during translation, represses defective messages,
disassembles stalled ribosomes, and targets incomplete nascent chains for
ubiquitin-dependent degradation. The gene-level reviews are now complete for the
human core on this page; the remaining work is to turn those reviewed functions
into a compact RQC module and reconcile them with existing GO-CAM pathway models.

## Model Species

**Primary: Homo sapiens (human)**
- Best characterized in human and mammalian systems
- Links to neurodegenerative disease (ALS, etc.)

## Core Pathway Architecture

### 1. Collision Sensors
Detect ribosome collisions:
- **ZNF598** - Ubiquitinates collided ribosomes (RPS10, RPS20)
- **EDF1** - Collision sensor, recruits GIGYF2
- **GIGYF2** - Recruits 4EHP to repress translation

### 2. Ribosome Splitting
Disassemble stalled ribosomes:
- **PELO** - Dom34 homolog, promotes subunit splitting
- **HBS1L** - GTPase, works with PELO
- **ABCE1** - ATPase that physically separates subunits

### 3. RQC Complex
Handles 60S-nascent chain complexes:
- **NEMF** - Recruits LTN1, stabilizes nascent chain
- **LTN1** - E3 ubiquitin ligase (Listerin)
- **TCF25** - RQC complex component
- **ANKZF1** - Vms1 homolog, releases stalled peptides

### 4. mRNA Decay
Targets problematic mRNAs:
- **No-go decay pathway genes**

### 5. Downstream Quality Control
- **VCP/p97** - Extracts ubiquitinated substrates
- **Proteasome** - Degrades aberrant proteins

## Candidate Genes

| Gene | UniProt | Function |
|------|---------|----------|
| ZNF598 | Q86UK7 | Collision sensor, E3 ligase |
| EDF1 | O60869 | Collision sensor |
| GIGYF2 | Q6Y7W6 | Translation repressor |
| PELO | Q9BRX2 | Ribosome rescue |
| HBS1L | Q9Y450 | GTPase for splitting |
| ABCE1 | P61221 | Ribosome splitting ATPase |
| NEMF | O60524 | RQC complex |
| LTN1 | O94822 | E3 ubiquitin ligase |
| TCF25 | Q9BQ70 | RQC complex |
| ANKZF1 | Q9H8Y5 | Peptide release |
| ASCC3 | Q8N3C0 | Helicase, collision resolution |
| ASCC2 | Q9H1I8 | ASCC complex |
| VCP | P55072 | AAA+ ATPase |

## Key Mechanistic Themes

- EDF1 as collision sensor (2020)
- ASCC complex structure and function
- Structural basis of ribosome splitting
- Links to neurodegeneration

## Disease Relevance

- ALS/neurodegeneration (C9orf72 repeat expansions cause ribosome stalling)
- NEMF mutations cause neurological disease
- Proteostasis disorders

## Project Status

- [x] Review all 13 candidate genes listed here
- [ ] Build an RQC module spanning ZNF598/EDF1 collision sensing,
  PELO-HBS1L-ABCE1 splitting and NEMF-LTN1 nascent-chain handling
  ([#3952](https://github.com/ai4curation/ai-gene-review/issues/3952))
- [ ] Cross-check the six production GO-CAMs that already model parts of the
  pathway against the curated gene reviews
  ([#3952](https://github.com/ai4curation/ai-gene-review/issues/3952))
