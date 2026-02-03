# SPKW Autophagy Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

This subproject identifies human proteins annotated to "autophagy" (GO:0006914) where the **only** evidence comes from UniProt Keywords mapping (GO_REF:0000043).

## Summary Statistics

- **Total SPKW-only genes**: 123
- **Total SPKW annotations**: 172
- **% with no corroboration**: 71.5%
- **Source keyword**: UniProtKB-KW:KW-0073 (Autophagy)

## Status

- Batch 1 (4/4 complete): ABL1, BCL2, FOXO1, LRRK2
- Batch 2 (5/5 complete): DRAM1, DRAM2, DAP, CLTC, HMGB1
- Batch 3 (5/5 complete): IFI16, IRF8, LRPPRC, HAP1/APEX1, GRAMD1A
- Total reviewed: 14/123 genes (11.4%)
- Over-annotation rate: 79% (11/14)
- Legitimate annotations: 3 (DRAM1, DRAM2, DAP)
- Note: HDAC6 was removed from analysis (has corroborating IGI evidence)

## Key Concern

The UniProt "Autophagy" keyword may be applied to:
1. Core autophagy machinery (ATG proteins, VPS proteins) - LEGITIMATE
2. Proteins that **regulate** autophagy (kinases, transcription factors) - may be over-annotation
3. Proteins that are **substrates** of autophagy (cargo receptors, aggregates) - may be over-annotation
4. Proteins whose loss **affects** autophagy flux through pleiotropic effects

## Pilot Batch for Review

| Gene | UniProt | Description | Core Function (confirmed) | Status |
|------|---------|-------------|---------------------------|--------|
| ABL1 | P00519 | Tyrosine-protein kinase ABL1 | Non-receptor tyrosine kinase (cytoskeleton, DNA damage) | **OVER-ANNOTATION** |
| BCL2 | P10415 | Apoptosis regulator Bcl-2 | Anti-apoptotic (MOMP inhibition) | **OVER-ANNOTATION** |
| FOXO1 | Q12778 | Forkhead box protein O1 | Transcription factor (metabolism) | **OVER-ANNOTATION** |
| LRRK2 | Q5S007 | Leucine-rich repeat kinase 2 | Ser/Thr kinase + GTPase (Rab phosphorylation) | **OVER-ANNOTATION** |

**Result: 4/4 genes (100%) are OVER-ANNOTATED**

*Note: HDAC6 was initially included but removed from this analysis - it has corroborating evidence (IGI for GO:0061734 type 2 mitophagy from PMID:20457763), so it does not meet the SPKW-only criteria. The HDAC6 gene review was retained separately.*

## Criteria for Legitimate Autophagy Annotation

A legitimate annotation requires evidence that the gene:
1. Has an **evolved function** in autophagosome formation/maturation
2. Is part of the core autophagy machinery (ATG proteins, PI3K complex, LC3 system)
3. Functions as a selective autophagy receptor as its **primary function**
4. Has direct physical role in autophagy pathway (e.g., cargo trafficking to autophagosome)

NOT legitimate if:
- Regulates autophagy via upstream signaling (kinases, TFs)
- Is degraded by autophagy (substrate)
- Loss causes autophagy defects through pleiotropic effects

---

## Detailed Analysis - Autophagy Pilot

### ABL1 (P00519) - Tyrosine-protein kinase ABL1

**Core function:** Non-receptor tyrosine kinase (EC 2.7.10.2) with SH2-SH3-kinase architecture. Functions in DNA damage response (DDR), cytoskeletal dynamics (F-actin binding), and cell signaling. Famously drives CML when fused to BCR.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **tyrosine kinase activity**: DDR, cytoskeleton, BCR-ABL in leukemia, allosteric regulation
- No mention of autophagy in deep research
- Core function is tyrosine phosphorylation of diverse substrates (YAP1, HK2, RAD51)
- Any autophagy effects would be through signaling cascades, not direct participation

---

### BCL2 (P10415) - Apoptosis regulator Bcl-2

**Core function:** Anti-apoptotic regulator that prevents mitochondrial outer membrane permeabilization (MOMP). BH1-4 domains form hydrophobic groove that sequesters BH3-only proteins (BIM, PUMA) and restrains BAX/BAK.

**Why OVER-ANNOTATION:**
- Core evolved function is clearly **apoptosis regulation**
- BCL2 does interact with BECN1 (Beclin-1) and can regulate autophagy
- However, this is a **regulatory interaction** - BCL2's evolved function is to inhibit apoptosis, and its autophagy regulation is through the same BH3-groove mechanism
- BCL2 didn't evolve TO regulate autophagy - it evolved to regulate apoptosis, and BECN1 happens to have a BH3 domain
- The annotation "autophagy" implies direct participation, not regulatory crosstalk

---

### FOXO1 (Q12778) - Forkhead box protein O1

**Core function:** Forkhead transcription factor that binds 5′-TTGTTTAC-3′ consensus. Regulated by insulin/PI3K/AKT signaling. Primary functions in gluconeogenesis (activates PCK1, G6PC), oxidative stress, and metabolic homeostasis.

**Why OVER-ANNOTATION:**
- Deep research is about **metabolic control** and **transcription factor function**
- FOXO1 can transcriptionally activate autophagy genes as one of its many target gene programs
- But FOXO1's evolved function is as a **metabolic transcription factor**, not as autophagy machinery
- This is similar to annotating p53 to "apoptosis" - it regulates apoptosis genes but its core function is broader
- Transcriptional regulation of autophagy ≠ direct function in autophagy

---

### LRRK2 (Q5S007) - Leucine-rich repeat serine/threonine-protein kinase 2

**Core function:** Dual enzyme with Ser/Thr kinase (EC 2.7.11.1) and GTPase (EC 3.6.5.-) activities. Primary substrates are Rab GTPases (Rab10 Thr73, Rab8, Rab12). Regulates endolysosomal trafficking and ciliogenesis. Linked to Parkinson's disease.

**Why OVER-ANNOTATION:**
- Deep research is about **Rab phosphorylation** and **endolysosomal trafficking**
- LRRK2 affects the lysosomal system (LYTL - lysosomal tubulation/sorting)
- While autophagy ultimately requires lysosomes, LRRK2's evolved function is Rab-mediated membrane trafficking
- Autophagy defects from LRRK2 mutations are **downstream effects** of impaired endolysosomal trafficking
- Core function is Rab phosphorylation for trafficking, not autophagosome biogenesis

---

## Legitimate Genes Identified

Three genes were found to have legitimate autophagy annotations:

### DRAM1 - Lysosomal Membrane Protein

**Core function:** Lysosomal transmembrane protein that promotes autophagy.

**Why LEGITIMATE:**
- Localized to lysosomes and functions in autophagic flux
- Stabilizes VAMP8 to promote autophagosome-lysosome fusion
- p53-inducible as part of autophagy/cell death decisions
- Direct role in autophagy pathway

### DRAM2 - Lysosomal Membrane Protein

**Core function:** Lysosomal transmembrane protein similar to DRAM1.

**Why LEGITIMATE:**
- Functions in autophagy via lysosomal membrane localization
- Promotes autophagic flux
- Part of DRAM family with established autophagy roles

### DAP - Death-Associated Protein

**Core function:** mTORC1 substrate that regulates autophagy.

**Why LEGITIMATE:**
- Functions as a negative regulator of autophagy
- Direct mTORC1 substrate involved in autophagy control
- Evolved function in autophagy regulation pathway

---

## Key Findings

1. **Autophagy keyword too broadly applied:**
   - Applied to kinases that phosphorylate autophagy components
   - Applied to transcription factors that regulate autophagy genes
   - Applied to proteins with downstream effects on autophagy

2. **Result: 11/14 genes are over-annotated (79%)**

3. **Pattern similar to apoptosis:**
   - Regulatory crosstalk ≠ direct function
   - Transcriptional regulation ≠ participation
   - Downstream effects ≠ evolved function
