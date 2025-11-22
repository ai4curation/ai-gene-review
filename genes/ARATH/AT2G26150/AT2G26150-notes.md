# HSFA2 (AT2G26150) Curation Notes

## Gene Summary
**Key transcriptional regulator of heat stress MEMORY and acquired thermotolerance** - NOT a master regulator like HSFA1, but functions DOWNSTREAM [deep-research:perplexity]

## Core Function (Molecular Activity)
- **DNA-binding transcription factor** - binds heat shock elements (HSE) like HSFA1 [deep-research]
- **"Hit-and-run" transcription factor** - transiently binds to promoters, then dissociates [deep-research]
- **Epigenetic regulator** - orchestrates sustained H3K4 methylation at memory loci [deep-research]
- Forms **heteromeric complexes** with other class A HSFs (HSFA1, HSFA3) [deep-research]

## Functional Distinction from HSFA1

### HSFA1 (Master Regulator):
- Initiates immediate heat response
- Constitutively expressed
- Essential for basal thermotolerance

### HSFA2 (Memory Regulator):
- **Secondary wave** of heat response
- **Most strongly induced** HSF during heat stress
- Required for **acquired/extended thermotolerance**
- Maintains expression during RECOVERY phase
- NOT required for immediate heat response but essential for MEMORY

## Key Biological Processes

### Acquired Thermotolerance (PRIMARY/CORE)
- **Required for extended thermotolerance** after heat stress [deep-research]
- **hsfa2 mutants** lose thermotolerance faster than WT [deep-research]
- Maintains HSP gene expression during recovery [deep-research]

### Transcriptional Memory (PRIMARY/CORE)
- Establishes **H3K4me3 marks** at target loci [deep-research]
- Memory persists for **several days** after heat stress [deep-research]
- "Hit-and-run" mechanism - HSFA2 dissociates but memory remains [deep-research]

### Heat Stress Response (SECONDARY)
- Works downstream of HSFA1A/B/D [deep-research]
- HSFA1 activates HSFA2 transcription [deep-research]
- Forms heterocomplexes with HSFA1 for cooperative activation [deep-research]

### Other Stress Responses
- Oxidative stress
- Hypoxia
- Phytohormone responses
- Broader stress adaptation [deep-research]

## Regulation of HSFA2

### Transcriptional Activation
- **HSFA1 directly activates HSFA2** transcription [deep-research]
- **Most strongly induced HSF** during heat stress [deep-research]
- Rapid induction upon heat stress

### Protein Localization
- Nuclear localization signal (NLS) [deep-research]
- Nuclear export signal (leucine-rich NES) regulates distribution [deep-research]
- Predominantly nuclear during stress [deep-research]

### Alternative Splicing
- **S-HSFA2** - short variant with distinct function [deep-research]
- May have regulatory roles [deep-research]

## Epigenetic Mechanism

### H3K4 Methylation
- HSFA2 recruits H3K4 methyltransferases [deep-research]
- **Transient binding** but **sustained methylation** [deep-research]
- H3K4me3 marks persist after HSFA2 dissociation [deep-research]
- Enables rapid re-induction upon subsequent stress [deep-research]

### Chromatin Remodeling
- Works with chromatin remodeling complexes [deep-research]
- Maintains open chromatin at memory loci [deep-research]

## Protein Interactions
- **HSFA1** - forms heterodimers/heteromers for cooperative activation [deep-research]
- **HSFA3** - collaborates in stress memory [deep-research]
- **H3K4 methyltransferases** - recruited to target loci [deep-research]
- **Transcriptional machinery** - via C-terminal activation domain [deep-research]
- Can form **trimers and hexamers** via oligomerization domain [deep-research]

## Subcellular Localization
- **Nuclear** (primary functional location) [deep-research]
- NLS mediates nuclear import [deep-research]
- NES regulates nuclear export [deep-research]

## Target Genes (Direct)
- **HSP genes**: HSP17, HSP70, HSP90, HSP101 (sustained expression during recovery) [deep-research]
- **APX2** (ascorbate peroxidase 2) - antioxidant enzyme [deep-research]
- **Memory-associated genes** with H3K4me3 marks [deep-research]
- Overlapping targets with HSFA1 but with different kinetics [deep-research]

## Genetic Evidence
- **hsfa2 mutants**:
  - Normal basal thermotolerance [deep-research]
  - **Impaired acquired thermotolerance** [deep-research]
  - Faster loss of thermotolerance during recovery [deep-research]
  - Reduced memory gene expression [deep-research]
- **Overexpression**:
  - Enhanced acquired thermotolerance [deep-research]
  - Prolonged memory [deep-research]

## Expression Pattern
- **Highly inducible by heat stress** (most strongly induced HSF) [deep-research]
- Low/absent under normal conditions [deep-research]
- Induced within 1 hour of heat stress [deep-research]
- Expression maintained during recovery phase [deep-research]

## Structural Features
- **DNA-binding domain (DBD)** with helix-turn-helix motif [deep-research]
- **Oligomerization domain (HR-A/B)** with heptad repeats [deep-research]
- **Class A-specific 21-aa insertion** in OD [deep-research]
- **Activation domain** (C-terminal) [deep-research]
- **Nuclear localization signal (NLS)** [deep-research]
- **Nuclear export signal (NES)** - leucine-rich motif [deep-research]

## Functional Model
1. Heat stress → HSFA1 activated
2. HSFA1 → induces HSFA2 transcription
3. HSFA2 → transiently binds target promoters
4. HSFA2 → recruits H3K4 methyltransferases
5. H3K4me3 established at memory loci
6. HSFA2 dissociates ("hit-and-run")
7. H3K4me3 persists → sustained expression
8. Memory enables faster/stronger response to subsequent heat stress

## Curation Strategy
1. **ACCEPT** core transcriptional memory and acquired thermotolerance annotations
2. **ACCEPT** DNA-binding transcription factor activity
3. **ACCEPT** nucleus localization
4. **KEEP_AS_NON_CORE** immediate heat response annotations (HSFA1 is primary)
5. **MODIFY** if annotations don't capture the MEMORY/RECOVERY function
6. **ADD** missing key functions:
   - Transcriptional memory
   - Acquired thermotolerance (distinct from basal)
   - Histone methylation recruitment
   - Hit-and-run mechanism
   - Heteromeric complex formation with HSFA1/3
7. **DISTINGUISH** from HSFA1 - HSFA2 is NOT master regulator

## Key Differences from HSFA1A
- HSFA1A: Master regulator, immediate response, constitutive expression
- HSFA2: Memory regulator, recovery/extended response, highly inducible
- HSFA1A: Required for basal thermotolerance
- HSFA2: Required for ACQUIRED thermotolerance
- Both bind HSEs but with different kinetics and functional outcomes

## References
- UniProt: Q9SIQ8
- Deep research: AT2G26150-deep-research-perplexity.md (42 citations)
- Key distinction: DOWNSTREAM of HSFA1, required for MEMORY not initiation
