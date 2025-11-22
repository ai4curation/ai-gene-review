# Arabidopsis Heat Stress Gene Curation Project

**Project Start Date:** 2025-11-07
**Organism:** *Arabidopsis thaliana* (ARATH)
**Focus:** Heat stress response network

## Project Overview

This document tracks the curation of 10 key heat stress response genes in Arabidopsis. These genes represent the core regulatory and molecular chaperone network that enables thermotolerance.

## Gene List and Curation Status

### TIER 1 - Master Regulators (Highest Priority)

| Gene Symbol | Locus | Status | UniProt Fetched | GOA Fetched | Deep Research | Review Started | Review Completed | Notes |
|-------------|-------|--------|-----------------|-------------|---------------|----------------|------------------|-------|
| HSFA1A | AT4G17750 | ✅ COMPLETE | ✅ | ✅ (22 annots) | ✅ (37 cites) | ✅ | ✅ | Master regulator, all 22 annots ACCEPTED |
| HSFA1B | AT5G16820 | ✅ COMPLETE | ✅ | ✅ (20 annots) | ✅ (42 cites) | ✅ | ✅ | Co-master regulator, 17 ACCEPT, 2 MODIFY, 1 NON-CORE |
| HSFA1D | AT1G32330 | ✅ COMPLETE | ✅ | ✅ (14 annots) | ✅ (40 cites) | ✅ | ✅ | Co-master regulator, 12 ACCEPT, 2 MODIFY |
| HSFA2 | AT2G26150 | ✅ COMPLETE | ✅ | ✅ (41 annots) | ✅ (42 cites) | ✅ | ✅ | Memory regulator, 23 ACCEPT, 11 NON-CORE |

### TIER 2 - Essential Molecular Chaperones

| Gene Symbol | Locus | Status | UniProt Fetched | GOA Fetched | Deep Research | Review Started | Review Completed | Notes |
|-------------|-------|--------|-----------------|-------------|---------------|----------------|------------------|-------|
| HSP101 | AT1G74310 | ✅ COMPLETE | ✅ | ✅ (21 annots) | ✅ (53 cites) | ✅ | ✅ | Essential disaggregase, 14 ACCEPT, 3 MODIFY, 3 NEW |
| HSC70-1 | AT5G02500 | ✅ COMPLETE | ✅ | ✅ (48 annots) | ✅ (56 cites) | ✅ | ✅ | Negative HSF regulator, 30 ACCEPT, 10 NON-CORE |
| HSP90.1 | AT5G52640 | ✅ COMPLETE | ✅ | ✅ (33 annots) | ✅ (54 cites) | ✅ | ✅ | Signaling protein chaperone, 14 ACCEPT, 7 MODIFY, 8 NON-CORE, 4 REMOVE |

### TIER 3 - Key Transcriptional Integrators

| Gene Symbol | Locus | Status | UniProt Fetched | GOA Fetched | Deep Research | Review Started | Review Completed | Notes |
|-------------|-------|--------|-----------------|-------------|---------------|----------------|------------------|-------|
| DREB2A | AT5G05410 | ✅ COMPLETE | ✅ | ✅ (39 annots) | ✅ (37 cites) | ✅ | ✅ | Cross-stress integrator, 15 ACCEPT, 9 MODIFY, 7 OVER-ANNOTATED, 8 NON-CORE |
| HSFA3 | AT5G03720 | ✅ COMPLETE | ✅ | ✅ (15 annots) | ✅ (36 cites) | ✅ | ✅ | Memory specialist (forgetter3), 11 ACCEPT, 4 MODIFY |
| HSFA1E | AT3G02990 | ✅ COMPLETE | ✅ | ✅ (13 annots) | ✅ (38 cites) | ✅ | ✅ | Osmotic/salt specialist, 12 ACCEPT, 1 NON-CORE, 4 NEW |

## Scientific Background

### The Heat Stress Response Network

The heat stress response in Arabidopsis operates through a hierarchical transcriptional cascade:

1. **Master Regulators (HSFA1A/B/D/E)** - Sense heat stress and activate the entire cascade
2. **Amplifiers (HSFA2)** - Most strongly induced, extends acquired thermotolerance
3. **Molecular Chaperones (HSP101, HSC70-1, HSP90.1)** - Protect proteins, regulate HSF activity
4. **Cross-talk Regulators (DREB2A, HSFA3)** - Integrate heat with drought stress responses

### Key Functional Relationships

- HSFA1s → activate → HSFA2
- DREB2A → activates → HSFA3 (exceptional - HSF not regulated by HSFs)
- HSP70/HSP90 ↔ physically interact with → HSFs (feedback regulation)
- HSFA1 triple KO (a/b/d) → dramatic thermotolerance defects
- HSP101 knockout (hot1-3) → complete loss of thermotolerance

## Curation Strategy

### Phase 1: Data Collection (In Progress)
1. Fetch UniProt records for all 10 genes
2. Fetch GO annotations from QuickGO
3. Generate deep research files using perplexity

### Phase 2: Master Regulators Review
Focus on HSFA1A, HSFA2, HSFA1B, HSFA1D first as they control the entire network

### Phase 3: Chaperones and Integrators
Review HSP101, HSC70-1, HSP90.1, DREB2A, HSFA3, HSFA1E

### Phase 4: Network Integration
Ensure annotations capture:
- Hierarchical regulatory relationships
- Protein-protein interactions (HSP-HSF)
- Cross-talk with drought stress
- Developmental context (pollen development)

## Key Literature References

### Foundational Papers
- PMID:21931939 - HsfA1s as main positive regulators
- PMID:17999647 - DREB2A/HSFA3 cascade
- PMID:32573848 - HSC70-1 negative regulation
- PMID:24634180 - HsfA1a overexpression studies

### Review Articles
- PMID:26715648 - Transcriptional cascade regulation
- PMID:17519032 - Transcriptional profiling of HSPs and HSFs

## Curation Guidelines

### Annotation Priorities
1. Capture **hierarchical relationships** (master regulator → amplifier → target genes)
2. Document **physical interactions** (HSP70/90 with HSFs)
3. Include **stress response specificity** (heat vs. drought vs. cold)
4. Note **genetic evidence** (mutant phenotypes, complementation)
5. Distinguish **core vs. non-core functions**

### Common Pitfalls to Avoid
- Over-annotation of general terms (e.g., "protein binding" without specificity)
- Missing regulatory hierarchy in annotations
- Not capturing feedback regulation (HSPs regulate HSFs)
- Ignoring cross-talk with other stress pathways

## Progress Tracking

**Last Updated:** 2025-11-08

**Overall Progress:** 10/10 genes complete (100%) ✅✅✅
**Data Collection:** 10/10 genes fetched (100%)
**Deep Research:** 10/10 genes COMPLETE (100%) - **435 total citations** ✅
**Annotation Review:** 10/10 genes (100%) ✅

**Current Phase:** ✅ PROJECT COMPLETE ✅

**✅ ALL 10 GENES FULLY CURATED:**

### TIER 1 - Master Regulators (COMPLETE)
1. ✅ **HSFA1A** - 22 annotations reviewed (22 ACCEPT)
2. ✅ **HSFA1B** - 20 annotations reviewed (17 ACCEPT, 2 MODIFY, 1 NON-CORE)
3. ✅ **HSFA1D** - 14 annotations reviewed (12 ACCEPT, 2 MODIFY)
4. ✅ **HSFA1E** - 13 annotations reviewed (12 ACCEPT, 1 NON-CORE) + 4 NEW
5. ✅ **HSFA2** - 41 annotations reviewed (23 ACCEPT, 11 NON-CORE, 3 MODIFY, 4 OVER-ANNOTATED)

### TIER 2 - Essential Molecular Chaperones (COMPLETE)
6. ✅ **HSP101** - 21 annotations reviewed (14 ACCEPT, 3 MODIFY, 2 REMOVE, 2 NON-CORE) + 3 NEW
7. ✅ **HSC70-1** - 48 annotations reviewed (30 ACCEPT, 10 NON-CORE, 5 OVER-ANNOTATED, 2 MODIFY, 2 REMOVE)
8. ✅ **HSP90.1** - 33 annotations reviewed (14 ACCEPT, 7 MODIFY, 8 NON-CORE, 4 REMOVE)

### TIER 3 - Key Transcriptional Integrators (COMPLETE)
9. ✅ **DREB2A** - 39 annotations reviewed (15 ACCEPT, 9 MODIFY, 7 OVER-ANNOTATED, 8 NON-CORE)
10. ✅ **HSFA3** - 15 annotations reviewed (11 ACCEPT, 4 MODIFY)

**Total Annotations Reviewed:** 266 across all 10 genes
**Total Deep Research Citations:** 435 citations

## Key Achievements

### 1. Complete HSFA1 Family Characterization
All four HSFA1 family members fully characterized with functional distinctions:
- **HSFA1A/B/D**: Primary heat stress master regulators (>65% of heat genes)
- **HSFA1E**: Specialized for osmotic/salt stress, minor heat role (subfunctionalization)

### 2. Chaperone Network Paradoxes Documented
- **HSP101**: ESSENTIAL positive effector (hot1 KO = no thermotolerance)
- **HSC70-1**: NEGATIVE regulator (hsc70-1 KO = enhanced basal thermotolerance)
- **HSP90.1**: Specialized for signaling proteins (not general chaperone)

### 3. Hierarchical Regulatory Cascades Captured
- **Immediate**: HSFA1a/b/d → DREB2A + HSFA2
- **Delayed**: DREB2A → HSFA3 (memory specialist)
- **Memory**: HSFA2/HSFA3 heteromers → H3K4me3 epigenetic marks

### 4. Cross-Stress Integration
- **DREB2A**: Coordinates BOTH drought AND heat responses (distinct programs)
- **HSFA3**: Memory specialist with pathogen defense cross-talk
- **HSFA1E**: Osmotic/salt specialist (subfunctionalization)

**Summary of Fetched Data:**
- Total GO annotations: 266 across all 10 genes
- Total publications cached: 71 unique PMIDs
- PANTHER families identified: 5 families
  - PTHR10015: Heat Shock Transcription Factor (HSFA1A/B/D/E, HSFA2, HSFA3)
  - PTHR11638: ATP-dependent Clp protease/Chaperone (HSP101)
  - PTHR19375: Heat Shock Protein 70kDa (HSC70-1)
  - PTHR11528: Heat Shock Protein 90 Family (HSP90.1)
  - PTHR31241: AP2/ERF Transcription Factor (DREB2A)

## Notes

- All gene symbols follow TAIR nomenclature
- Locus identifiers (AT codes) confirmed via TAIR database
- Focus on experimentally validated functions
- Pay special attention to mutant phenotypes (triple KO, hot1-3, hsfa2)
