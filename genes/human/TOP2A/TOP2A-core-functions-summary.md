# TOP2A Core Functions Summary

## Overview
Based on comprehensive analysis of existing annotations, deep research, and literature evidence, I have synthesized three distinct core functions for human TOP2A. These are structured as GO-CAM-like activity units that capture the essential biological roles of this type II DNA topoisomerase.

## Core Function 1: DNA Topology Resolution During Replication

**Activity Description:** Catalyzing ATP-dependent double-strand DNA passage to resolve DNA supercoiling, unknotting, and catenation during DNA replication

**Key Characteristics:**
- **Molecular Function:** DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) activity (GO:0003918)
- **Biological Process:** DNA topological change (GO:0006265)
- **Location:** Nucleoplasm (GO:0005654)
- **Cell Cycle Context:** S-phase, during active DNA replication

**Rationale:** This represents TOP2A's fundamental enzymatic activity in its replication context. During S-phase, TOP2A resolves topological stress that accumulates ahead of and behind replication forks. The enzyme's ability to perform double-strand breaks, pass another DNA duplex through the break, and religate is essential for removing positive supercoils, unknotting DNA, and resolving precatenanes. This function is supported by strong biochemical evidence (PMID:22323612) demonstrating the Mg2+-dependent DNA cleavage mechanism.

## Core Function 2: Sister Chromatid Decatenation for Mitotic Segregation

**Activity Description:** Decatenating interlinked sister chromatids to enable chromosome segregation during mitosis

**Key Characteristics:**
- **Molecular Function:** DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) activity (GO:0003918)
- **Biological Processes:**
  - Sister chromatid segregation (GO:0000819)
  - Chromosome segregation (GO:0007059)
- **Locations:**
  - Condensed chromosome (GO:0000793)
  - Chromosome, centromeric region (GO:0000775)
- **Cell Cycle Context:** Mitosis (prophase through metaphase)

**Rationale:** This is TOP2A's most critical and essential function in proliferating cells. After DNA replication, sister chromatids remain topologically interlinked as catenanes. TOP2A is absolutely required to resolve these catenanes, particularly at centromeric regions where entanglements persist until the metaphase-anaphase transition. Loss of TOP2A function results in anaphase bridges and chromosome mis-segregation. This function is spatially and temporally distinct from the replication function, occurring on condensed chromosomes during mitosis rather than in nucleoplasm during S-phase.

## Core Function 3: Chromosome Scaffold Organization

**Activity Description:** Organizing chromatin structure as a major scaffold component of condensed mitotic chromosomes

**Key Characteristics:**
- **Molecular Function:** Chromatin binding (GO:0003682)
- **Biological Processes:**
  - Chromosome condensation (GO:0030261)
  - Chromatin organization (GO:0006325)
- **Location:** Condensed chromosome (GO:0000793)
- **Molecular Context:** Functions as part of the DNA topoisomerase type II homodimeric complex (GO:0009330)
- **Cell Cycle Context:** Mitosis

**Rationale:** Beyond its catalytic topoisomerase activity, TOP2A serves a structural role as the most abundant scaffold protein by mass on mitotic chromosomes. Proteomic studies show that TOP2A remains tightly bound to chromosomes even after high-salt extraction, indicating a non-enzymatic architectural function. The enzyme's chromatin binding activity contributes to chromosome condensation and overall chromatin organization during mitosis. This scaffold function is mechanistically distinct from its catalytic decatenation activity, though both occur on mitotic chromosomes.

## Integration with Annotation Review

These core functions are based on annotations with **ACCEPT** decisions in the review:

1. **Function 1 (Replication)** - Integrates:
   - GO:0003918 (topoisomerase activity) - ACCEPT
   - GO:0006265 (DNA topological change) - ACCEPT
   - GO:0005654 (nucleoplasm) - ACCEPT

2. **Function 2 (Decatenation)** - Integrates:
   - GO:0000819 (sister chromatid segregation) - ACCEPT
   - GO:0007059 (chromosome segregation) - ACCEPT
   - GO:0000775 (chromosome, centromeric region) - ACCEPT
   - GO:0000793 (condensed chromosome) - ACCEPT

3. **Function 3 (Scaffold)** - Integrates:
   - GO:0003682 (chromatin binding) - ACCEPT
   - GO:0030261 (chromosome condensation) - ACCEPT
   - GO:0006325 (chromatin organization) - ACCEPT
   - GO:0009330 (topoisomerase II complex) - ACCEPT

## Non-Core Functions

Several annotations were marked as **KEEP_AS_NON_CORE** because they represent context-specific or peripheral activities:
- GO:0045870 (viral RNA replication regulation) - HIV-1 specific
- GO:0042752 (circadian rhythm regulation) - Peripheral
- GO:0002244 (hematopoietic progenitor cell differentiation) - Developmental context
- GO:0040016 (embryonic cleavage) - Developmental context
- GO:0045944 (transcription regulation) - Secondary to TOP2B

These were excluded from core functions as they don't represent the primary, constitutive biological roles of TOP2A.

## GO-CAM Style Approach

Each core function follows GO-CAM principles:
1. **Activity-oriented descriptions** - Focus on what TOP2A does ("Catalyzing...", "Decatenating...", "Organizing...")
2. **Molecular function as the central node** - Each function centers on a specific molecular activity
3. **Biological process context** - Links activity to its biological outcome
4. **Localization specificity** - Places the activity in its cellular/chromosomal context
5. **Evidence-based** - All assertions supported by literature or deep research evidence

## Temporal and Spatial Distinction

The three core functions are spatially and temporally separated:
- **Function 1** occurs in nucleoplasm during S-phase
- **Functions 2 & 3** occur on condensed chromosomes during mitosis
- Functions 2 and 3 are co-localized but mechanistically distinct (catalytic vs. structural)

This organization reflects the cell cycle-dependent expression and localization of TOP2A, which is highly expressed in proliferating cells and concentrated on chromosomes during mitosis.
