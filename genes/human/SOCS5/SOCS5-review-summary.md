# SOCS5 Annotation Review Summary

## Overview
Comprehensive review of 31 existing GO annotations for human SOCS5 (Suppressor of cytokine signaling 5, UniProt O75159).

## Gene Function Summary
SOCS5 is a negative feedback regulator of cytokine and growth factor signaling. It functions as a substrate recognition component of an E3 ubiquitin ligase complex, mediating ubiquitination and proteasomal degradation of target receptors including EGFR and IL-4 receptor. SOCS5 plays key roles in:
- Inhibiting JAK-STAT signaling pathways
- Regulating T-helper cell differentiation (promoting Th1 while inhibiting Th2)
- Controlling EGFR homeostasis through receptor degradation

## Annotation Review Results

### Actions Assigned:
- **ACCEPT**: 21 annotations (68%)
- **KEEP_AS_NON_CORE**: 2 annotations (6%)
- **MARK_AS_OVER_ANNOTATED**: 3 annotations (10%)
- **MODIFY**: 2 annotations (6%)
- **UNDECIDED**: 3 annotations (10%)

### Core Functions Accepted (Representative Examples):

#### Biological Processes:
1. **Cytokine-mediated signaling pathway** (GO:0019221) - Multiple evidence codes (IBA, IEA, ISS)
   - Core function supported by phylogenetic inference and experimental data

2. **JAK-STAT signaling pathway** (GO:0007259)
   - Canonical mechanism for SOCS family proteins

3. **EGFR signaling pathway** (GO:0007173)
   - Well-documented with experimental support from PMID:15590694

4. **T-helper cell differentiation regulation**:
   - Positive regulation of Th1 (GO:0045627)
   - Negative regulation of Th2 (GO:0045629)
   - Key immunological function

5. **Proteasomal degradation** (GO:0032436)
   - Core mechanism: E3 ubiquitin ligase complex function
   - Supported by IEA and IMP evidence

#### Molecular Functions:
1. **Receptor tyrosine kinase binding** (GO:0030971)
   - Specific, informative term with IPI evidence

2. **EGFR binding** (GO:0005154)
   - Direct experimental support

3. **Negative regulation of EGFR activity** (GO:0007175)
   - Strong IDA evidence from PMID:15590694

#### Cellular Components:
1. **Cytosol** (GO:0005829) - 6 duplicate annotations
   - All from Reactome pathways (TAS evidence)
   - Consistent with intracellular regulatory function

### Non-Core/Peripheral Functions:
1. **Negative regulation of IL-6 production** (GO:0032715)
   - Secondary function compared to IL-4 regulation

2. **Negative regulation of inflammatory response** (GO:0050728)
   - Indirect/downstream consequence

### Over-Annotated Terms:
1. **Negative regulation of signal transduction** (GO:0009968) - 2 instances
   - Too broad, not informative
   - Better captured by specific pathway terms

2. **Intracellular signal transduction** (GO:0035556)
   - Overly general parent term

### Terms Requiring Modification:
1. **Protein binding** (GO:0005515) - 2 instances (IPI evidence)
   - Not informative per curation guidelines
   - Should be replaced with specific binding terms like receptor tyrosine kinase binding

### Undecided Annotations (Require Additional Literature):
1. **Cellular response to LDL particle stimulus** (GO:0071404)
   - No clear mechanistic connection to core SOCS5 functions
   - Transferred via orthology but lacks direct support

2. **Negative regulation of MCP-1 production** (GO:0071638)
   - Very specific, no direct evidence in available literature

3. **Vascular endothelial cell response to fluid shear stress** (GO:0097699)
   - Highly specific, no obvious connection to core functions

## Key Publications Referenced:
- **PMID:15590694**: Primary experimental paper demonstrating SOCS5 regulation of EGFR
- **PMID:10773671**: Original cloning paper describing SOCS5/CIS6
- **UniProt:O75159**: Comprehensive functional annotation
- **Reactome pathways**: Multiple pathways showing cytosolic localization and E3 ligase complex participation

## Recommendations:
1. Accept 21 core annotations representing well-established SOCS5 functions
2. Retain 2 peripheral functions as non-core
3. Flag 3 annotations as over-annotated (too general)
4. Modify 2 "protein binding" annotations to more specific terms
5. Mark 3 annotations as requiring additional literature review before final decision

## Evidence Quality:
- Strong experimental support: IDA, IMP, IPI evidence from PMID:15590694
- Phylogenetic support: IBA annotations for conserved SOCS family functions
- Convergent evidence: Multiple evidence codes supporting key functions (cytokine signaling, Th cell differentiation)
- Reactome pathways: Consistent cellular localization data
