# PANTHER Family Review: PTHR10574

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10574 |
| **Family Name** | Laminin/Netrin Extracellular Matrix |
| **Short Name** | Laminin/Netrin_ECM |
| **InterPro Entry** | IPR050440 |
| **Total Proteins** | 31,327 |
| **Subfamilies** | 37 |
| **Taxonomic Breadth** | 4,860 taxa |
| **Representative Structure** | 5lf2 (Laminin beta2 LE5-LF-LE6) |

## Executive Summary

PTHR10574 is a large protein family encoding **extracellular matrix (ECM) proteins** involved in:
1. **Laminins**: Structural components of basement membranes
2. **Netrins**: Secreted axon guidance cues

**CRITICAL**: This family contains **NO transcription factors**. All members are **secreted extracellular proteins** that function outside the cell. Any annotations suggesting nuclear localization or transcription factor activity are **ERRONEOUS**.

## Subfamily Analysis

### Laminins (Basement Membrane Components)

Laminins are heterotrimeric glycoproteins composed of α, β, and γ chains. They are major components of basement membranes.

| Subfamily | Representative | Function |
|-----------|----------------|----------|
| **SF409** | LAMA1 (Laminin α1) | Basement membrane structure |
| **SF291** | LAMA2 (Laminin α2) | Muscle basement membrane |
| **SF406** | LAMA5 (Laminin α5) | Epithelial basement membrane |
| **SF233** | LAMB1 (Laminin β1) | Basement membrane structure |
| **SF36** | LAMB2 (Laminin β2) | Neuromuscular junction |
| **SF279** | LAMB4 (Laminin β4) | Less characterized |
| **SF270** | LAMC1 (Laminin γ1) | Basement membrane structure |
| **SF435** | LAMC2 (Laminin γ2) | Anchoring filaments |

### Netrins (Axon Guidance Cues)

Netrins are secreted proteins that guide axon migration during development. They bind netrin receptors (DCC, UNC5, neogenin).

| Subfamily | Representative | Function |
|-----------|----------------|----------|
| **SF378** | NTN1 (Netrin-1) | Axon guidance, chemoattractant/repellent |
| **SF292** | NTN3 (Netrin-3) | Axon guidance |
| **SF** | NTN4 (Netrin-4) | Axon guidance, angiogenesis |
| **SF262** | NTN5 (Netrin-5) | Less characterized |
| **SF** | NTNG1 (Netrin-G1) | GPI-anchored, synapse formation |
| **SF** | NTNG2 (Netrin-G2) | GPI-anchored, synapse formation |
| **SF365** | UNC-6 (C. elegans) | Prototypical netrin |

## Domain Architecture

All family members share characteristic domains:

| Domain | IPR | Function |
|--------|-----|----------|
| **Laminin N-terminal (VI)** | IPR001791 | Polymerization, chain assembly |
| **Laminin EGF-like** | IPR002049 | Calcium binding, protein interactions |
| **Laminin G-like** | IPR001791 | Receptor binding (integrins, dystroglycan) |
| **NTR (Netrin) domain** | IPR001791 | C-terminal domain in netrins |

**NO DNA-binding domains are present in any family member.**

## Functional Diversity

### Core Functions (All Members)

1. **Extracellular localization** - All members are secreted or GPI-anchored
2. **Protein-protein interactions** - Receptor binding, ECM assembly
3. **Cell signaling** - Through receptor activation

### Laminin-Specific Functions

- Basement membrane assembly
- Cell adhesion and migration
- Tissue organization during development

### Netrin-Specific Functions

- Axon guidance (attraction and repulsion)
- Neuronal migration
- Angiogenesis regulation
- Apoptosis modulation

## CRITICAL ANNOTATION ERROR

### Erroneous IBA Annotations on NTN1 and NTN3

**NTN1 (O95631) and NTN3 (O00634)** have erroneous IBA annotations to transcription factor activity:

| GO Term | Evidence | Status |
|---------|----------|--------|
| GO:0000981 (DNA-binding TF activity, RNAP II-specific) | IBA from PTN000180816 | **REMOVE** |
| GO:0006357 (regulation of transcription by RNAP II) | IBA from PTN000180816 | **REMOVE** |
| GO:0000978 (cis-regulatory region sequence-specific DNA binding) | IBA from PTN000180816 | **REMOVE** |

### Root Cause

The IBA annotations were propagated from PANTHER node **PTN000180816**, which erroneously grouped netrins with **POU-domain transcription factors** (PTHR11636):

| Evidence Protein | Family | Function |
|------------------|--------|----------|
| P14859 (POU2F1/OCT1) | PTHR11636 | POU-domain TF |
| P28069 (POU1F1/Pit-1) | PTHR11636 | POU-domain TF |
| Q01860 (POU5F1/OCT4) | PTHR11636 | POU-domain TF |

This is a clear error - PTHR10574 (laminins/netrins) and PTHR11636 (POU TFs) are **unrelated families** with completely different:
- Domain architecture
- Subcellular localization
- Molecular function

### Evidence Against TF Function

1. **Netrins are SECRETED proteins** - they have signal peptides and function extracellularly
2. **No DNA-binding domains** - Netrins contain laminin/EGF/NTR domains, NOT POU/homeodomain
3. **Receptor-mediated signaling** - Netrins bind DCC/UNC5 receptors, don't enter the nucleus
4. **Literature consensus** - PMID:28945198: *"Netrin-1 is a secreted protein that was first identified 20 years ago as an axon guidance molecule"*

## GO Annotation Recommendations

### Core Annotations (Appropriate for ALL Family Members)

| GO Term | GO ID | Aspect | Notes |
|---------|-------|--------|-------|
| extracellular region | GO:0005576 | CC | All members are secreted/extracellular |
| extracellular matrix | GO:0031012 | CC | ECM components |
| protein binding | GO:0005515 | MF | Receptor/ECM interactions |

### Laminin-Specific Annotations

| GO Term | GO ID | Aspect |
|---------|-------|--------|
| basement membrane | GO:0005604 | CC |
| cell adhesion | GO:0007155 | BP |
| extracellular matrix organization | GO:0030198 | BP |
| laminin binding | GO:0043236 | MF |
| integrin binding | GO:0005178 | MF |

### Netrin-Specific Annotations

| GO Term | GO ID | Aspect |
|---------|-------|--------|
| axon guidance | GO:0007411 | BP |
| netrin receptor binding | GO:1990890 | MF |
| chemorepulsion of axon | GO:0061643 | BP |
| positive regulation of axon extension | GO:0045773 | BP |
| signaling receptor binding | GO:0005102 | MF |

### Annotations to NEVER Apply

| GO Term | GO ID | Reason |
|---------|-------|--------|
| DNA-binding transcription factor activity | GO:0003700 | **WRONG** - No DNA binding |
| nucleus | GO:0005634 | **WRONG** - Extracellular proteins |
| transcription by RNA polymerase II | GO:0006366 | **WRONG** - Not TFs |
| sequence-specific DNA binding | GO:0043565 | **WRONG** - No DNA-binding domains |

## Structural Biology

**Representative Structure**: PDB 5lf2
- Laminin beta2 LE5-LF-LE6 domains
- Shows characteristic laminin fold

**Additional Structures**:
- Multiple laminin chain structures available
- Netrin structures show laminin-like fold

## Key Literature

### Recent Reviews (2024-2025)

| Source | Title | Key Points |
|--------|-------|------------|
| J Transl Med 2025 | The role of laminins in cancer pathobiology | Laminin chain diversity, LG domain receptor binding, BM assembly |
| J Cell Mol Med 2024 | Research progress of netrins and receptors in cancer | NTN1/3/4/5 and netrin-G biology, DCC/UNC5 receptor mechanisms |
| Curr Opin Neurobiol 2025 | Expanding ligand-receptor interaction networks for axon guidance | Netrin-DCC/UNC5 structural insights, signaling polarity |
| Biology 2024 | Basement membranes, brittlestar tendons | Three-arm laminin polymerization model |

### Classic References

| PMID | Title | Key Finding |
|------|-------|-------------|
| PMID:28945198 | Netrin-1: A multifunctional protein | Comprehensive netrin review |
| PMID:26190107 | Functions of netrin-1 beyond axon guidance | Netrin signaling pathways |
| PMID:9143507 | Netrin-3, a mouse homolog of human NTN2L | NTN3 characterization |

## Recommendations for GO Consortium

### 1. Remove Erroneous Annotations
- NTN1: Remove GO:0000981, GO:0006357, GO:0000978 (IBA)
- NTN3: Remove GO:0000981, GO:0006357, GO:0000978 (IBA)

### 2. Review PANTHER Node PTN000180816
- Investigate why netrins were grouped with POU TFs
- Correct the phylogenetic inference

### 3. Add NOT Annotations (Optional)
Consider adding explicit NOT annotations to prevent future errors:
- NTN1: NOT enables GO:0003700 (DNA-binding TF activity)

## Review Status

- **Date**: 2026-02-05
- **Reviewer**: AI-assisted review
- **Status**: COMPLETE
- **Based on**: UniProt, PANTHER, InterPro, GOA, published literature
- **Deep research**: Falcon (17 citations, 2024-2025 literature)

## Related Files

- `PTHR10574-metadata.yaml` - Family metadata from InterPro
- `PTHR10574-entries.csv` - 58 reviewed protein members
- `../../../projects/TRANSCRIPTION_FACTORS/PANTHER-IBA-error-report.md` - Detailed error report
- `../../../genes/human/NTN1/NTN1-ai-review.yaml` - NTN1 annotation review
- `../../../genes/human/NTN3/NTN3-ai-review.yaml` - NTN3 annotation review
