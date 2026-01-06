# Integrated Stress Response (ISR) Project

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

- [ ] Stub - needs gene folder setup
