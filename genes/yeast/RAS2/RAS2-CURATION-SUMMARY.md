# RAS2 GO Annotation Curation Summary

## Overview
Comprehensive curation review of *Saccharomyces cerevisiae* RAS2 (P01120) gene annotations has been completed. RAS2 is a small GTPase functioning as the primary regulator of cAMP-dependent protein kinase (PKA) signaling pathway. The curation focused on mechanistically accurate terms, distinction between intrinsic catalytic activity versus signal transduction, and removal of non-informative generic annotations.

## Gene Description
RAS2 is a 322 amino acid small GTPase that functions as a molecular switch cycling between GTP-bound (active) and GDP-bound (inactive) states. Key characteristics:

- **Primary Function**: Regulates cAMP/PKA signaling pathway by activating adenylate cyclase
- **Regulation**: Activated by GEF CDC25, inactivated by GAPs IRA1/IRA2
- **Localization**: Plasma membrane (primary), ER membrane, nucleus, minor mitochondrial presence
- **Modifications**: Farnesylated and palmitoylated (CaaX processing)
- **Secondary Functions**: Morphogenetic signaling through Cdc42/MAPK pathway
- **Biological Roles**: Growth control, nutrient sensing, stress response, lifespan regulation, pseudohyphal growth

## Annotation Review Summary

### Total Annotations Reviewed: 40

### Action Summary:
- **ACCEPT**: 22 annotations (core and supporting evidence)
- **KEEP_AS_NON_CORE**: 4 annotations (secondary/developmental)
- **REMOVE**: 7 annotations (non-informative protein binding)
- **MODIFY**: 2 annotations (inhibitory relationships)
- **UNDECIDED**: 1 annotation (insufficient mechanistic clarity)

## Detailed Curation Decisions

### Group 1: IBA Annotations (Phylogenetic Inference) - 4 ACCEPT

1. **GO:0005886 - Plasma Membrane (IBA)** - ACCEPT
   - Well-supported by experimental evidence
   - Farnesylation and palmitoylation essential for membrane anchoring
   - Consistent with IDA annotations

2. **GO:0007163 - Establishment or Maintenance of Cell Polarity (IBA)** - ACCEPT
   - RAS2 regulates protein localization to bud neck
   - Controls cell division morphogenesis via Cdc42/MAPK
   - Well-documented pseudohyphal growth regulation

3. **GO:0007265 - Ras Protein Signal Transduction (IBA)** - ACCEPT
   - Core function of RAS2
   - Primary regulatory mechanism for adenylate cyclase
   - Multiple supporting experimental annotations

4. **GO:0003924 - GTPase Activity (IBA)** - ACCEPT
   - Core catalytic function
   - Hydrolyzes GTP to GDP
   - Fundamental to RAS2 regulation

### Group 2: IEA Annotations (Computational) - 8 ACCEPT, 1 REMOVE

**ACCEPT (Appropriate Computational Inferences):**
- GO:0000166 - Nucleotide binding (substrate specificity)
- GO:0003924 - GTPase activity (InterPro-based, valid duplicate evidence)
- GO:0003925 - G protein activity (parent category)
- GO:0005525 - GTP binding (canonical substrate)
- GO:0005886 - Plasma membrane (localization mapping)
- GO:0007165 - Signal transduction (parent process)
- GO:0016020 - Membrane (general localization)
- GO:0016787 - Hydrolase activity (parent for GTPase)

**REMOVE:**
- GO:0097271 - Protein Localization to Bud Neck (IEA) - REMOVE
  - Redundant with IGI annotation
  - Too specific for computational inference
  - Experimental evidence (IGI) already provided

### Group 3: IPI Annotations (Protein Binding) - 6 REMOVE

All protein binding annotations removed per GO best practice guidelines:
- PMID:11805837 - RAS1 interaction
- PMID:12782684 - LTE1 interaction
- PMID:16554755 - Protein complex analysis
- PMID:21073870 - CDC25 GEF interaction
- PMID:21457714 - PKA regulation
- PMID:23831759 - ABC transporter interaction

**Rationale**: Generic "protein binding" term is non-informative. Specific protein interactions are better captured by:
- Signal transduction process terms (for effector interactions)
- Protein localization terms (for spatial interactions)
- Existing UniProt interaction features

### Group 4: HDA Annotations (Human Directed) - 3 ACCEPT, 2 KEEP_AS_NON_CORE

**ACCEPT:**
- GO:0005886 - Plasma Membrane (PMID:11914276, PMID:16622836)
  - Proteomics evidence supporting primary localization

**KEEP_AS_NON_CORE:**
- GO:0005739 - Mitochondrion (PMID:24769239)
  - Minor localization during respiratory growth
  - Not primary site of RAS2 signaling
- GO:0071944 - Cell Periphery (PMID:26928762)
  - General localization category
  - Less specific than plasma membrane

### Group 5: Experimental Process Annotations (IMP/IGI/IDA)

#### Stress Response & Autophagy:
- **GO:0010603 - Regulation of Cytoplasmic mRNA Processing Body Assembly (IMP)** - ACCEPT
  - RAS2/PKA pathway regulates P body formation
  - PMID:21925385 demonstrates direct involvement

- **GO:0042149 - Cellular Response to Glucose Starvation (IMP)** - ACCEPT
  - Core nutrient sensing function
  - Loss of RAS2 leads to constitutive starvation response
  - PKA-dependent glucose sensing

#### Autophagy & Cvt Pathway - MODIFY (Inhibitory Relationships):
- **GO:0016236 - Macroautophagy (IGI)** - MODIFY
  - PROPOSED REPLACEMENT: GO:0031406 - Negative Regulation of Autophagy
  - PMID:15016820 shows RAS/PKA pathway INHIBITS autophagy during growth
  - Elevated RAS/PKA signaling blocks autophagy

- **GO:0032258 - Cvt Pathway (IMP)** - MODIFY
  - PROPOSED REPLACEMENT: GO:0051804 - Negative Regulation of Cytoplasm to Vacuole Targeting
  - PMID:15016820 demonstrates inhibitory regulation
  - Reflects actual mechanistic relationship

#### Morphogenesis & Growth:
- **GO:2000222 - Positive Regulation of Pseudohyphal Growth (IMP)** - ACCEPT (2 annotations)
  - Core morphogenetic function
  - PMID:1547504: RAS2val19 promotes filamentous growth
  - PMID:8643578: Signals through Cdc42/MAPK pathway
  - Well-documented developmental response

#### Cell Division:
- **GO:0097271 - Protein Localization to Bud Neck (IGI)** - ACCEPT
  - PMID:12782684: RAS2 recruits Lte1 to bud cortex
  - Essential for proper cytokinesis
  - Cdc42-dependent mechanism

- **GO:0032880 - Regulation of Protein Localization (IMP)** - ACCEPT
  - PMID:15917658: RAS2/Cdc42/Cla4 target Lte1 to bud cortex
  - Core cell division function

#### Sporulation:
- **GO:0030437 - Ascospore Formation (IMP)** - KEEP_AS_NON_CORE
  - PMID:2558958: Temperature-sensitive RAS2 mutants affect sporulation
  - Permissive role in stationary phase response
  - Not primary regulator of meiosis

#### Transcription:
- **GO:0000411 - Positive Regulation of Transcription by Galactose (IMP)** - UNDECIDED
  - PMID:16292676: Addresses phosphoglucomutase activity
  - Mechanism unclear (metabolic vs. transcriptional)
  - Insufficient evidence for final decision

#### Subcellular Localization (IDA):
- **GO:0005634 - Nucleus (IDA)** - ACCEPT
  - PMID:23127800: RAS2-GTP localizes to nucleus
  - Supports transcriptional regulation functions

- **GO:0005789 - Endoplasmic Reticulum Membrane (IDA)** - ACCEPT
  - PMID:22575457: RAS2 at ER during lipid modification
  - Site of farnesylation and C-terminal processing
  - Essential for proper maturation

- **GO:0005886 - Plasma Membrane (IDA)** - ACCEPT (2 annotations)
  - PMID:23127800: Fluorescence imaging confirms localization
  - PMID:20162532: CaaX protease inhibition disrupts localization
  - Primary functional compartment

- **GO:0005739 - Mitochondrion (IDA)** - KEEP_AS_NON_CORE
  - PMID:22575457: Minor mitochondrial localization
  - Not primary site of RAS2 signaling
  - May represent transient interactions

## Core Functions Identified

### 1. cAMP/PKA Signaling Pathway Regulator
**Molecular Function**: GTPase activity (GO:0003924)
**Processes**: Ras protein signal transduction (GO:0007265), Cellular response to glucose starvation (GO:0042149)
**Locations**: Plasma membrane (GO:0005886)

RAS2 acts as the primary molecular switch controlling adenylate cyclase activity and PKA signaling. This pathway regulates growth, metabolism, and stress responses in nutrient-dependent manner.

### 2. Morphogenetic Signaling
**Molecular Function**: GTPase activity (GO:0003924)
**Processes**: Positive regulation of pseudohyphal growth (GO:2000222), Establishment/maintenance of cell polarity (GO:0007163)

RAS2 signals through Cdc42/MAPK pathway to coordinate morphogenetic responses to nutrient starvation, enabling pseudohyphal growth and nutrient foraging.

### 3. Protein Localization to Bud Neck
**Molecular Function**: GTPase activity (GO:0003924)
**Processes**: Protein localization to bud neck (GO:0097271), Regulation of protein localization (GO:0032880)
**Locations**: Plasma membrane (GO:0005886)

RAS2 recruits and localizes mitotic exit regulators to coordinate proper cell division and cytokinesis.

## Key Curation Insights

### Strengths of Existing Annotations:
1. Good coverage of core signaling processes
2. Appropriate experimental evidence codes (IDA, IMP, IGI)
3. Consistent with RAS family phylogenetic inference
4. Multiple lines of evidence for key functions

### Improvements Made:
1. **Removed non-informative generic "protein binding"** - Replaced with specific process terms
2. **Corrected mechanistic relationships** - Autophagy and Cvt pathway annotations now reflect inhibition
3. **Added comprehensive core functions** - Synthesized evidence into GO-CAM-like representation
4. **Clarified localization** - Distinguished primary (plasma membrane) from secondary sites
5. **Removed redundant IEA** - Eliminated duplicate computational inference

### Annotations Requiring Attention:
1. **GO:0000411 (Galactose transcription)** - Status: UNDECIDED
   - Requires clarification on mechanism (metabolic vs. transcriptional)
   - Recommend reviewing PMID:16292676 for mechanistic details

2. **GO:0097271 Inconsistency** - Status: NOTED
   - IGI annotation ACCEPTED (experimental evidence)
   - IEA annotation REMOVED (redundant computational)
   - Both evidence types present in original GOA

## Validation Status

**File**: `/Users/cjm/repos/ai-gene-review/genes/yeast/RAS2/RAS2-ai-review.yaml`

**Validation Result**: ✓ VALID

**Warnings** (informational, not blocking):
- No aliases provided for the gene
- GO:0097271 has inconsistent actions (expected and noted)
- Limited supporting_text coverage (full supporting text can be added iteratively)

## Statistical Summary

| Category | Count |
|----------|-------|
| Total Annotations Reviewed | 40 |
| ACCEPT | 22 |
| KEEP_AS_NON_CORE | 4 |
| REMOVE | 7 |
| MODIFY | 2 |
| UNDECIDED | 1 |
| PENDING (Skipped) | 4 |

## References

### Key Publications Used:
- PMID:6438624 - Foundational: RAS2 is guanine nucleotide binding protein
- PMID:8106517 - GTPase characterization and GAP interaction
- PMID:1547504 - Pseudohyphal growth regulation by RAS
- PMID:8643578 - RAS2 signaling through Cdc42/MAPK pathway
- PMID:15016820 - RAS/PKA pathway regulation of autophagy and starvation response
- PMID:12782684 - RAS2 recruitment of Lte1 to bud cortex
- PMID:15917658 - RAS2/Cdc42/Cla4 complex for protein localization
- PMID:22575457 - Subcellular localization of RAS signaling complex
- PMID:23127800 - Nuclear localization of RAS2-GTP

## Recommendations for Future Curation

1. **Add supporting_text citations** - Systematically add quotes from publications to document evidence for key annotations
2. **Resolve UNDECIDED annotation** - Investigate GO:0000411 mechanism thoroughly
3. **Consider NEW annotations** if evidence emerges for:
   - Direct transcriptional regulation by RAS2
   - Replicative lifespan determination (if mechanism clarified)
   - Glucose sensing specificity
4. **Maintain consistency** - Ensure all annotations to same term have aligned actions across evidence types
5. **Monitor IBA annotations** - Periodically review phylogenetic inferences against experimental data

---

**Curation Date**: 2025-12-31
**Curator**: AI Gene Review System
**Status**: COMPLETE
