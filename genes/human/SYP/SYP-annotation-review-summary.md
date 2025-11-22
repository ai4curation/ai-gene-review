# Synaptophysin (SYP) GO Annotation Review Summary

**Gene:** SYP (Synaptophysin)  
**UniProt ID:** P08247  
**Organism:** Homo sapiens  
**Review Date:** 2025-11-16  
**Total Annotations Reviewed:** 38

## Overview

Synaptophysin is a major integral membrane protein of synaptic vesicles with four transmembrane domains (MARVEL domain). It regulates synaptic vesicle endocytosis kinetics, interacts with synaptobrevin-2/VAMP2, binds cholesterol for vesicle biogenesis, and modulates synaptic plasticity. Forms hexameric structures and acts as a membrane elastomer regulating vesicle size and neurotransmitter-dependent expansion.

## Curation Action Summary

| Action | Count | Percentage | Description |
|--------|-------|------------|-------------|
| **ACCEPT** | 29 | 76.3% | Annotations accepted as core or valid functions |
| **KEEP_AS_NON_CORE** | 3 | 7.9% | Correct but peripheral annotations |
| **MODIFY** | 1 | 2.6% | Annotations requiring more specific terms |
| **REMOVE** | 5 | 13.2% | Annotations to be removed |
| **TOTAL** | 38 | 100% | |

## Key Findings

### Core Functions Confirmed

1. **Synaptic Vesicle Membrane Localization** (GO:0030672)
   - Most abundant integral membrane protein on synaptic vesicles
   - Multiple lines of evidence (IBA, IEA, NAS)
   - Represents defining localization

2. **Cholesterol Binding** (GO:0015485)
   - Direct experimental evidence (IDA)
   - Essential for vesicle biogenesis and membrane organization
   - PMID:10620806 demonstrates specific cholesterol binding

3. **Synaptic Vesicle Endocytosis** (Modified from broad endocytosis)
   - Critical role in regulating endocytosis kinetics
   - Modified from GO:0006897 to GO:0048488 for specificity
   - Essential for maintaining synaptic transmission during sustained activity

4. **Synaptic Plasticity Regulation**
   - Short-term plasticity (GO:0048172) - well-documented
   - Long-term plasticity (GO:0048169) - supported by multiple studies
   - Acts by regulating vesicle dynamics and release probability

5. **Hexamer Formation** (GO:0042802 - identical protein binding)
   - Forms hexameric ring structures
   - Critical for organizing synaptobrevin-2 complexes
   - Confirmed by structural studies

### Annotations Removed

1. **Protein Binding (GO:0005515)** - 3 instances
   - **Rationale:** Too generic and uninformative
   - Specific interactions (VAMP2, cholesterol, synapsin) should be annotated instead
   - Based on generic interactome studies that don't capture meaningful biology

2. **Regulation of Synaptic Vesicle Priming (GO:0010807)**
   - **Rationale:** Acts downstream of priming, not in regulating priming itself
   - Knockout studies show effects on fusion, not priming
   - Conflates priming with fusion regulation

3. **Regulation of Opioid Receptor Signaling (GO:2000474)**
   - **Rationale:** No evidence in primary human synaptophysin literature
   - Likely over-interpretation from ISS annotation
   - Not a specific function of synaptophysin

### Non-Core Annotations Retained

1. **Neuromuscular Junction (GO:0031594)**
   - Present but not primary localization
   - Main research focuses on CNS synapses

2. **Perinuclear Region (GO:0048471)**
   - Likely transient during biosynthesis
   - Not a functional localization

3. **Schaffer Collateral-CA1 Synapse (GO:0098685)**
   - Overly specific anatomical annotation
   - Synaptophysin is general synaptic protein

### Modified Annotations

1. **Endocytosis → Synaptic Vesicle Endocytosis**
   - Original: GO:0006897 (endocytosis)
   - Proposed: GO:0048488 (synaptic vesicle endocytosis)
   - **Rationale:** Captures the specific biological process more accurately

## Evidence Sources

### Key Publications
- **PMID:10620806** - Cholesterol binding and vesicle biogenesis
- **PMID:8838578** - Hippocampal synapse localization
- **PMID:1975480** - Human gene structure

### Primary Evidence Sources
- **Deep Research Report:** Comprehensive review of synaptophysin literature
- **UniProt Entry:** Curated functional annotations
- **GO Annotations:** IBA (phylogenetic), IDA (direct), ISS (sequence similarity), IEA (electronic)

## Molecular Functions

### Confirmed Core Molecular Functions
1. **Cholesterol binding** (GO:0015485) - IDA evidence
2. **Identical protein binding** (GO:0042802) - Hexamer formation
3. **SH2 domain binding** (GO:0042169) - Via tyrosine phosphorylation sites

### Biological Processes

#### Core Processes
1. Synaptic vesicle endocytosis (modified from GO:0006897 to GO:0048488)
2. Synaptic vesicle membrane organization (GO:0048499)
3. Synaptic vesicle maturation (GO:0016188)
4. Regulation of short-term neuronal synaptic plasticity (GO:0048172)
5. Regulation of long-term neuronal synaptic plasticity (GO:0048169)
6. Modulation of chemical synaptic transmission (GO:0050804)

### Cellular Components

#### Primary Localizations
1. **Synaptic vesicle membrane** (GO:0030672) - Core localization
2. **Presynaptic active zone** (GO:0048786) - Functional site
3. **Presynapse** (GO:0098793) - Exclusive presynaptic localization
4. **Terminal bouton** (GO:0043195) - Nerve terminals

## Recommendations

### For GO Curators

1. **Replace generic "protein binding" annotations** with specific molecular function terms:
   - Consider annotations for VAMP2/synaptobrevin-2 binding
   - Consider annotations for synapsin binding
   - Consider annotations for V-ATPase interaction

2. **Add missing specific functions:**
   - Membrane elastomer function
   - Regulation of vesicle size
   - Regulation of release probability (inhibitory role)

3. **Clarify priming vs. fusion regulation:**
   - Current annotation conflates these processes
   - Synaptophysin acts downstream of priming on fusion itself

### Future Annotation Priorities

1. Document interaction with synaptobrevin-2 (VAMP2)
2. Document role in organizing synaptic vesicle clusters with synapsin
3. Document membrane elasticity function
4. Document V-ATPase interaction (recent discovery)
5. Document role as inhibitor of neurotransmitter release

## Notes

- Evidence codes: IDA (Inferred from Direct Assay), IBA (Inferred from Biological aspect of Ancestor), ISS (Inferred from Sequence or structural Similarity), IEA (Inferred from Electronic Annotation), NAS (Non-traceable Author Statement), IPI (Inferred from Physical Interaction)
- IBA annotations generally represent well-curated phylogenetic inferences
- Multiple annotations with same GO ID but different evidence codes are acceptable and provide supporting evidence from different sources
