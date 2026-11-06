---
title: "Integrated Stress Response (ISR) Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
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
translated. The hub and most of the periphery are now reviewed: of the 20
genes named below, 15 have reviews (1,036 annotation rows between them) and 5
have no gene folder — PKR/EIF2AK2, the beta subunit EIF2S2, DDIT3/CHOP, and
both phosphatase regulatory subunits PPP1R15A/GADD34 and PPP1R15B/CReP.
EIF2S1 (eIF2α) itself was reviewed on
2026-10-29 and is the one place in the pathway where a `NEW` molecular function
was needed: `GO:1990624` *guanyl nucleotide exchange factor inhibitor activity*,
the actual ISR mechanism, which PomBase already carries on the *S. pombe*
ortholog but human GOA did not. There is still no ISR module.

We scoped this because the ISR is a drug target (ISRIB), eIF2B mutations cause
vanishing white matter disease, and the DELE1-HRI branch was only described in
2020, so current GO annotation may not reflect it.

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

## Candidate Genes (~18)

| Gene | UniProt | Function |
|------|---------|----------|
| EIF2AK1 | Q9BQI3 | HRI kinase |
| EIF2AK2 | P19525 | PKR kinase |
| EIF2AK3 | Q9NZJ5 | PERK kinase |
| EIF2AK4 | Q9P2K8 | GCN2 kinase |
| EIF2S1 | P05198 | eIF2α |
| DELE1 | Q14154 | Mitochondrial sensor |
| OMA1 | Q96E52 | DELE1 protease |
| ATF4 | P18848 | Master TF |
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

Reviewed (15): EIF2AK1, EIF2AK3, EIF2AK4, EIF2S1, EIF2S3, DELE1, OMA1, ATF4,
ATF3, ASNS, EIF2B1, EIF2B2, EIF2B3, EIF2B4, EIF2B5.

Remaining review queue (5):

- [ ] `just fetch-gene human EIF2AK2` and review EIF2AK2 (PKR)
- [ ] `just fetch-gene human EIF2S2` and review EIF2S2 (eIF2β)
- [ ] `just fetch-gene human DDIT3` and review DDIT3 (CHOP)
- [ ] `just fetch-gene human PPP1R15A` and review PPP1R15A (GADD34)
- [ ] `just fetch-gene human PPP1R15B` and review PPP1R15B (CReP)
- [ ] Build an ISR module including the OMA1-DELE1 mitochondrial branch

Curation decisions to carry into the remaining reviews:

- EIF2S1 (eIF2α): the review adds `GO:1990624` *guanyl nucleotide exchange
  factor inhibitor activity* as a `NEW` molecular function — phospho-eIF2 binds
  eIF2B in the exchange-inactive mode (PMID:31048492, PMID:29599213), and
  PomBase already carries the term on *S. pombe* tif211 from the same paper.
  As with EIF2AK3 below, `GO:0140467` was **not** proposed: it is an ancestor
  of the already-accepted `GO:0036499` and `GO:0140468`. The stress-input terms
  (amino acid starvation, oxidative stress, heat, UV, kainic acid,
  manganese-induced ER stress) are kept non-core, since they name upstream
  contexts feeding the single `GO:0032057` mechanism rather than separate
  functions. Expect the same pattern on the kinases and on DDIT3.
- EIF2AK3 (PERK): the review does not add GO:0140467 *integrated stress
  response signaling*. [PR #3219](https://github.com/ai4curation/ai-gene-review/pull/3219)
  removed that proposed `NEW` row: GO:0140467 is an ancestor of the
  already-accepted GO:0036499 *PERK-mediated unfolded protein response*, and
  the cited 1999 cloning paper (PMID:9930704) does not show ISR signalling.
  With #3219 merged, EIF2AK3 has 95 annotation rows, down from 96.
