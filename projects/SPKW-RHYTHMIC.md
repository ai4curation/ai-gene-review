# SPKW Rhythmic Process Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

This subproject identifies human proteins annotated to "rhythmic process" (GO:0048511) where the **only** evidence comes from UniProt Keywords mapping (GO_REF:0000043). Notably, 100% of SPKW annotations to this term lack corroborating evidence from any other source.

## Summary Statistics

- **Total SPKW-only genes**: 146
- **Total SPKW annotations**: 146
- **% with no corroboration**: 100%
- **Source keyword**: UniProtKB-KW:KW-0151 (Biological rhythms)

## Status

- Total reviewed: 5/146 genes (3.4%)
- Over-annotation rate: **100%** (5/5)
- Legitimate annotations: 0 (none in pilot)

## Key Concern

The UniProt "Biological rhythms" keyword appears to be applied broadly to any protein whose expression or activity oscillates with circadian rhythm, OR to proteins that affect rhythmic processes. This is different from proteins whose **evolved core function** is to generate or maintain biological rhythms.

**Core circadian clock genes** (likely LEGITIMATE):
- CLOCK, BMAL1, BMAL2, PER1, PER2, PER3, CRY1, CRY2, TIMELESS, CIART, NR1D1, NR1D2

**Genes with other core functions** (likely OVER-ANNOTATION):
- ATG7 (autophagy), CDK1 (cell cycle), CREB1 (transcription factor), TP53 (tumor suppressor)

## Pilot Batch for Review

| Gene | UniProt | Description | Core Function (confirmed) | Status |
|------|---------|-------------|---------------------------|--------|
| ATG7 | O95352 | Autophagy-related protein 7 | Autophagy (E1-like enzyme) | **OVER-ANNOTATION** |
| CREB1 | P16220 | cAMP-responsive element-binding protein 1 | Transcription factor | **OVER-ANNOTATION** |
| SIRT1 | Q96EB6 | NAD-dependent protein deacetylase sirtuin-1 | Deacetylase (many substrates) | **OVER-ANNOTATION** |
| TARDBP | Q13148 | TAR DNA-binding protein 43 | RNA binding/splicing | **OVER-ANNOTATION** |
| TP53 | P04637 | Cellular tumor antigen p53 | Tumor suppressor | **OVER-ANNOTATION** |

**Result: 5/5 genes (100%) are OVER-ANNOTATED**

## Criteria for Legitimate Rhythmic Process Annotation

A legitimate annotation requires evidence that the gene:
1. Has an **evolved function** in generating/maintaining biological rhythms
2. Is part of the core molecular clock machinery (TTFL components)
3. Regulates clock gene expression as its **primary function**

NOT legitimate if:
- Expression oscillates but core function is elsewhere
- Affects rhythms through downstream/pleiotropic effects
- Is a target/substrate of clock-controlled processes

---

## Detailed Analysis - Rhythmic Process Pilot

### ATG7 (O95352) - Autophagy-related protein 7

**Core function:** E1-like ubiquitin-activating enzyme that activates ATG8 (LC3/GABARAP) and ATG12 in the ubiquitin-like conjugation cascades for autophagosome formation.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **autophagy** (canonical autophagy, LC3 lipidation, CASM)
- No mention of rhythmic process or circadian rhythm
- Core function is autophagy E1-like enzyme activity
- If autophagy flux oscillates with circadian rhythm, that doesn't make ATG7 a "rhythmic process" gene

---

### CREB1 (P16220) - cAMP-responsive element-binding protein 1

**Core function:** bZIP transcription factor that binds CRE elements (TGACGTCA) to regulate gene expression in response to cAMP/PKA, Ca2+/CaMK, and MAPK signaling.

**Why OVER-ANNOTATION:**
- Deep research covers neuronal activity-dependent transcription, metabolic regulation, cancer, immune function
- **No mention of circadian rhythm or rhythmic process** in the deep research
- Core function is cAMP-responsive transcription
- CREB may regulate clock gene expression, but that doesn't make rhythm its core function

---

### SIRT1 (Q96EB6) - NAD-dependent protein deacetylase sirtuin-1

**Core function:** NAD-dependent lysine deacetylase with broad substrate specificity.

**Why OVER-ANNOTATION:**
- Deep research mentions circadian briefly: "deacetylates core clock components (BMAL1/PER2)"
- But this is **ONE of MANY substrates**: p53 (apoptosis), NF-κB (inflammation), FOXO (stress), HIF (hypoxia), PGC-1α (metabolism), histones (chromatin)
- Core function is NAD-dependent deacetylation, not rhythm generation
- The clock deacetylation is a downstream effect of the enzymatic activity, not an evolved rhythmic function

---

### TARDBP (Q13148) - TAR DNA-binding protein 43 (TDP-43)

**Core function:** RNA-binding protein essential for splicing repression (cryptic exon suppression), mRNA stability/transport, and autoregulation.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **RNA metabolism** and **ALS/FTD neurodegeneration**
- No mention of rhythmic process or circadian rhythm
- Core function is RNA binding/splicing regulation
- TDP-43 proteinopathy in 95-97% of ALS cases - this is about neurodegeneration, not rhythm

---

### TP53 (P04637) - Cellular tumor antigen p53

**Core function:** Tumor suppressor transcription factor that coordinates cell-cycle arrest, apoptosis, senescence, DNA repair, and metabolic reprogramming.

**Why OVER-ANNOTATION:**
- Deep research is entirely about **tumor suppression**: DNA damage response, MDM2 regulation, apoptosis, ferroptosis, cancer therapy
- No mention of rhythmic process or circadian rhythm
- Core function is stress-responsive transcription for cell fate decisions
- Most frequently mutated tumor suppressor - this is about cancer, not rhythm

---

## Key Finding: Rhythmic Process has 100% Over-Annotation Rate in Pilot

This is **worse than apoptosis** (which had 80% over-annotation rate).

The UniProt "Biological rhythms" keyword (KW-0151) appears to be applied to:
1. Proteins whose expression oscillates with circadian rhythm (not the same as function IN rhythm)
2. Proteins that affect rhythm through pleiotropic effects (transcription factors, enzymes)
3. Proteins that are substrates/targets of clock machinery

**Recommendation:** The GO term GO:0048511 "rhythmic process" should be reviewed systematically. With 146 SPKW-only genes and 100% over-annotation in pilot, this mapping may be fundamentally problematic.
