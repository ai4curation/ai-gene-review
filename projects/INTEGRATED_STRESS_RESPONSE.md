---
title: "Integrated Stress Response (ISR) Project"
maturity: SCOPING
last_reviewed: 2026-10-04
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [EIF2AK3, OMA1, GCN1, ATF4, ATF3, EIF2B4, ASNS]   # reviewed genes only; full candidate list is in the table below
manifest:
  slides:
    - href: INTEGRATED_STRESS_RESPONSE/slides/INTEGRATED_STRESS_RESPONSE-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/Lfky9QLttPtNhYWCDnYQyx
      title: Project brief
---

# Integrated Stress Response (ISR) Project

**Bottom line:** in the integrated stress response, four kinases (HRI, PKR,
PERK and GCN2) each sense a different stress and phosphorylate eIF2α, which
blocks the eIF2B exchange factor, dampens global translation and lets ATF4 be
translated. Scoped, not yet started as a project: this page lists 19 candidate
human genes, including the DELE1-OMA1 route from mitochondrial stress to HRI and
GCN1 upstream of GCN2. Seven candidates have local review files from other work:
six are COMPLETE (EIF2AK3, GCN1, ATF4, ATF3, EIF2B4 and ASNS), OMA1 is
IN_PROGRESS, and together they cover 545 annotations. Twelve have no gene
folder, including the hub EIF2S1 (eIF2α), three of the four kinases, DELE1 and
four of the five eIF2B subunits. There is no local ai-gene-review ISR module
yet, although cached production GO-CAMs already cover the PERK branch and
DELE1/HRI mitochondrial, iron-deficiency and SIFI-inhibition branches.

We scoped this because the ISR is a drug target (ISRIB), eIF2B mutations cause
vanishing white matter disease, the 2020 DELE1-HRI branch still lacks local
DELE1 and EIF2AK1 reviews, and the pathway needs an end-to-end local module even
though OMA1/ATF4 GOA rows and cached GO-CAMs already represent the mitochondrial
DELE1-HRI route.

## Overview

The Integrated Stress Response (ISR) is a conserved signaling pathway that responds to diverse cellular stresses by phosphorylating eIF2α, leading to global translation attenuation and selective translation of stress-response genes like ATF4. Recent discoveries include the DELE1-HRI mitochondrial stress pathway.

## Model Species

**Primary: Homo sapiens (human)**
- Therapeutic target (ISRIB and related compounds)
- Disease relevance across multiple conditions

## Core Pathway Architecture

### 1. eIF2α Kinases (Stress Sensors)
Four kinases sense different stresses:
- **EIF2AK1** (HRI) - Heme deficiency, mitochondrial stress
- **EIF2AK2** (PKR) - Viral dsRNA
- **EIF2AK3** (PERK) - ER stress
- **EIF2AK4** (GCN2) - Amino acid starvation

### 2. Mitochondrial Stress Signaling (New!)
- **DELE1** - Mitochondrial stress sensor, activates HRI
- **OMA1** - Protease that cleaves DELE1

### 3. Core Pathway
- **EIF2S1** (eIF2α) - Translation initiation factor, phosphorylation target
- **EIF2B1-5** - eIF2B complex, guanine nucleotide exchange factor
- **PPP1R15A** (GADD34) - Phosphatase regulatory subunit, negative feedback
- **PPP1R15B** (CReP) - Constitutive phosphatase

### 4. Transcriptional Response
- **ATF4** - Master ISR transcription factor
- **DDIT3** (CHOP) - Pro-apoptotic TF
- **ATF3** - Stress-responsive TF
- **ASNS** - ATF4 target gene (asparagine synthetase)

## Candidate genes (19 scoped)

| Gene | UniProt | Function |
|------|---------|----------|
| EIF2AK1 | Q9BQI3 | HRI kinase |
| EIF2AK2 | P19525 | PKR kinase |
| EIF2AK3 | Q9NZJ5 | PERK kinase |
| EIF2AK4 | Q9P2K8 | GCN2 kinase |
| GCN1 | Q92616 | Ribosome-associated GCN2 activator |
| EIF2S1 | P05198 | eIF2α |
| DELE1 | Q14154 | Mitochondrial sensor |
| OMA1 | Q96E52 | DELE1 protease |
| ATF4 | P18848 | Master TF |
| ATF3 | P18847 | Stress-responsive TF |
| ASNS | P08243 | ATF4 target gene; asparagine synthetase |
| DDIT3 | P35638 | CHOP |
| PPP1R15A | O75807 | GADD34 |
| PPP1R15B | Q5SWA1 | CReP |
| EIF2B1-5 | various | eIF2B complex |

## Key Recent Discoveries (2020+)

- DELE1-HRI pathway for mitochondrial stress (2020)
- ISRIB mechanism of action
- ISR in aging and neurodegeneration
- COVID-19 and ISR activation

## Disease Relevance

- Vanishing white matter disease (EIF2B mutations)
- Neurodegeneration
- Cancer (stress adaptation)
- Metabolic disease

## Project Status

- [x] Cross-project reviews checked for EIF2AK3, OMA1, GCN1, ATF4, ATF3,
  EIF2B4 and ASNS
- [ ] Fetch and review EIF2AK1, EIF2AK2, EIF2AK4, EIF2S1, DELE1, DDIT3,
  PPP1R15A, PPP1R15B, EIF2B1, EIF2B2, EIF2B3 and EIF2B5
  ([#3951](https://github.com/ai4curation/ai-gene-review/issues/3951))
- [ ] Build a local ISR module including the OMA1-DELE1 mitochondrial branch
  and the GCN1-GCN2 amino-acid-starvation branch
- EIF2AK3 (PERK): the review does not add GO:0140467 *integrated stress
  response signaling*. [PR #3219](https://github.com/ai4curation/ai-gene-review/pull/3219)
  removed that proposed `NEW` row: GO:0140467 is an ancestor of the
  already-accepted GO:0036499 *PERK-mediated unfolded protein response*, and
  the cited 1999 cloning paper (PMID:9930704) does not show ISR signalling.
  With #3219 merged, EIF2AK3 has 95 annotation rows, down from 96.
