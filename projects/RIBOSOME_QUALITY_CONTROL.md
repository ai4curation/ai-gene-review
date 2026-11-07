---
title: "Ribosome Quality Control (RQC) Project"
maturity: IN_PROGRESS
last_reviewed: 2026-10-30
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
project; the stale "Stub" line has been cleared. Across the
12 RQC genes (VCP excluded) the reviews assess 430 GOA rows: 276 ACCEPT, 95
KEEP_AS_NON_CORE, 20 REMOVE, 18 MARK_AS_OVER_ANNOTATED, 17 MODIFY and 4 NEW.
The 97 rows that use RQC-specific terms, such as `rescue of stalled cytosolic
ribosome` (GO:0072344) and `RQC complex` (GO:1990112), were all accepted or
added; the corrections fall on generic `protein binding` rows and on off-pathway
terms such as DNA replication for ASCC2/ASCC3. The pathway is now modelled in
[`modules/ribosome_quality_control.yaml`](../modules/ribosome_quality_control.yaml),
a concrete human module in six ordered parts, and the six production GO-CAMs in
`gocams/` that cover parts of the pathway have been cross-checked against the
reviews — they agree on nine molecular functions and diverge on three, all
recorded in the module notes.

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

## Module

[`modules/ribosome_quality_control.yaml`](../modules/ribosome_quality_control.yaml)
(`CONCRETE`, human) models the pathway in six ordered parts: ZNF598/EDF1
collision sensing; the optional GIGYF2-4EHP shutdown of initiation on the
defective message; subunit dissociation, as a `ONE_OR_MORE` variant set over the
ubiquitin-dependent RQT/ASCC route and the A-site-vacancy PELO-HBS1L-ABCE1 route;
NEMF-LTN1-TCF25 nascent-chain ubiquitination with NEMF CAT tailing; ANKZF1
cleavage of the 60S-bound P-site tRNA; and VCP/p97 extraction of the chain. Every
molecular function is the participant's own reviewed core function, so the module
QC function-consistency check reports `CORE_SUPPORTED` throughout. EIF4E2, which
is not one of the 13 candidates below, is included because the GIGYF2 arm is not
a complete repression step without it; its review already exists. Curation
decisions, the GO-CAM cross-check table and the open items are in
[`modules/ribosome_quality_control-notes.md`](../modules/ribosome_quality_control-notes.md).

## Project Status

- [x] Review all 13 candidate genes listed here
- [x] Build an RQC module spanning ZNF598/EDF1 collision sensing,
  PELO-HBS1L-ABCE1 splitting and NEMF-LTN1 nascent-chain handling
  ([#3952](https://github.com/ai4curation/ai-gene-review/issues/3952))
- [x] Cross-check the six production GO-CAMs that already model parts of the
  pathway against the curated gene reviews
  ([#3952](https://github.com/ai4curation/ai-gene-review/issues/3952))
- [ ] Generate a module-level deep research report
  (`just module-deep-research-perplexity ribosome-quality-control`)
- [ ] Review ASCC1 and TRIP4 so the RQT complex descriptor can carry all four
  subunits as active units
- [ ] Report the three GO-CAM divergences upstream (ABCE1 `GO:0017111` vs
  `GO:0016887`; ANKZF1 `GO:0004521` vs `GO:0004549`; and the EDF1/TCF25/VCP
  coverage gaps)
