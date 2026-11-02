---
title: "Integrated Stress Response (ISR) Project"
maturity: SCOPING
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
translated. This page lists about 18 candidate human genes, including the
DELE1-OMA1 route from mitochondrial stress to HRI. As of 2026-11-02, 15 of them
have reviews: three of the four kinases (EIF2AK1/HRI, EIF2AK3/PERK,
EIF2AK4/GCN2), the DELE1-OMA1 branch, all five eIF2B subunits, the
transcriptional arm (ATF4, ATF3, ASNS) and now the hub itself, **EIF2S1**
(eIF2α, 102 annotation rows). Four candidates still have no gene folder:
EIF2AK2 (PKR) and the three remaining feedback/output genes DDIT3 (CHOP),
PPP1R15A (GADD34) and PPP1R15B (CReP). There is no ISR module yet.

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

- [x] Gene folders set up for 15 of the ~18 candidates
- [ ] Remaining gene reviews: EIF2AK2 (PKR), DDIT3 (CHOP), PPP1R15A (GADD34),
      PPP1R15B (CReP)
- [ ] ISR module, including the OMA1-DELE1 mitochondrial branch
- EIF2S1 (eIF2α): reviewed 2026-11-02 (DRAFT, 102 rows). Notes on the curation
  decisions are in
  [EIF2S1-notes.md](../genes/human/EIF2S1/EIF2S1-notes.md). Three points that
  affect the rest of the project:
  - The branch-signalling terms are annotated across the whole transduction
    chain, not just the kinase: GO:0140468 *HRI-mediated signaling* carries
    OMA1, DELE1, EIF2AK1, EIF2S1, ATF4 and DDIT3. EIF2S1 likewise carries
    GO:0036499 *PERK-mediated unfolded protein response*. The GCN2 sibling
    GO:0140469 *GCN2-mediated signaling* is annotated to EIF2AK4, GCN1, IMPACT
    and MAP3K20 but **not** to EIF2S1; that asymmetry looks like a gap, but the
    human evidence for the GCN2→eIF2α step is `By similarity` in UniProt and
    ISS/IEA in GOA, so it was raised as a question rather than proposed as a
    `NEW` row.
  - eIF2α's mitochondrial location is kept at the root organelle term.
    PMID:38340717 gives two direct lines plus an ER-marker control, but the
    protein has no TM segment or presequence and the association is
    stress-dependent peripheral recruitment to the cytosolic face, so
    GO:0005741 was not added.
  - Reactome already models three of the four phosphorylation events
    (R-HSA-381111 PERK, R-HSA-9835885 PKR, R-HSA-9840415 DELE1-HRI), which is a
    useful starting skeleton for the module.
- EIF2AK3 (PERK): the review does not add GO:0140467 *integrated stress
  response signaling*. [PR #3219](https://github.com/ai4curation/ai-gene-review/pull/3219)
  removed that proposed `NEW` row: GO:0140467 is an ancestor of the
  already-accepted GO:0036499 *PERK-mediated unfolded protein response*, and
  the cited 1999 cloning paper (PMID:9930704) does not show ISR signalling.
  With #3219 merged, EIF2AK3 has 95 annotation rows, down from 96.
