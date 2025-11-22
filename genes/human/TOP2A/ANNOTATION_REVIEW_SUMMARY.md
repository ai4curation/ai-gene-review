# TOP2A Annotation Review Summary

## Overview
Completed systematic review of all 93 existing GO annotations for human TOP2A (DNA topoisomerase II-alpha, UniProt P11388).

## Review Statistics

- **Total annotations reviewed**: 93
- **ACCEPT**: 67 annotations (72%)
- **REMOVE**: 18 annotations (19%) - All generic "protein binding" terms
- **KEEP_AS_NON_CORE**: 8 annotations (9%) - Peripheral or context-specific functions

## Core Functions Identified

TOP2A's core evolved function is captured in a unified GO-CAM-like representation:

**Molecular Function**: GO:0003918 (DNA topoisomerase type II activity)
- ATP-dependent double-strand DNA passage catalysis
- Resolves topological entanglements in DNA

**Biological Processes**:
- GO:0006265 (DNA topological change) - Direct result of catalytic activity
- GO:0007059 (chromosome segregation) - Essential for sister chromatid separation
- GO:0030261 (chromosome condensation) - Both enzymatic and structural role

**Cellular Locations**:
- GO:0005634 (nucleus) - Primary localization
- GO:0005654 (nucleoplasm) - Interphase distribution
- GO:0000793 (condensed chromosome) - Mitotic scaffold component

## Key Curation Decisions

### Accepted Annotations (ACCEPT)

**Molecular Functions**:
- Core catalytic activity (GO:0003918) - 3 annotations with IBA, IDA, IMP evidence
- DNA binding (GO:0003677) - General but accurate
- Chromatin binding (GO:0003682) - Important for scaffold role
- DNA binding, bending (GO:0008301) - Mechanistically important
- ATP-dependent activity (GO:0008094) - Broader but correct
- ATP binding (GO:0005524), nucleotide binding (GO:0000166) - Required for mechanism
- Magnesium ion binding (GO:0000287) - Essential cofactor
- Protein homodimerization (GO:0042803) - Functions as dimer
- Protein heterodimerization (GO:0046982) - Can form with TOP2B
- Protein kinase C binding (GO:0005080) - Functionally relevant regulation
- Ubiquitin binding (GO:0043130) - Regulatory interaction
- RNA binding (GO:0003723) - HDA evidence, may reflect RNP complex associations
- Isomerase activity (GO:0016853) - Correct enzyme classification

**Biological Processes**:
- DNA topological change (GO:0006265) - Core process, 2 IDA annotations
- Chromosome segregation (GO:0007059) - Essential function, 3 IMP annotations
- Sister chromatid segregation (GO:0000819) - More specific IBA annotation
- Chromosome condensation (GO:0030261) - Well-supported IEA
- Apoptotic chromosome condensation (GO:0030263) - Context-specific, 2 IDA annotations
- Chromatin organization (GO:0006325) - IMP evidence
- Resolution of meiotic recombination intermediates (GO:0000712) - IBA annotation
- Female meiotic nuclear division (GO:0007143) - IEA from orthologs
- DNA damage response (GO:0006974) - IDA evidence
- Positive regulation of apoptotic process (GO:0043065) - Context-dependent
- DNA metabolic process (GO:0006259) - Very broad parent term

**Cellular Components**:
- Nucleus (GO:0005634) - 5 annotations, multiple IDA studies
- Nucleoplasm (GO:0005654) - 5 annotations (IDA, TAS from Reactome)
- Nucleolus (GO:0005730) - 5 IDA annotations
- Cytoplasm (GO:0005737) - 2 IDA annotations, minor localization
- Nuclear chromosome (GO:0000228) - IDA evidence
- Chromosome, centromeric region (GO:0000775) - IEA, functionally important
- Condensed chromosome (GO:0000793) - Major scaffold component
- DNA topoisomerase type II complex (GO:0009330) - Homodimeric complex
- Protein-containing complex (GO:0032991) - General but correct
- Ribonucleoprotein complex (GO:1990904) - DHX9 interaction
- Centriole (GO:0005814) - Minor localization observed

### Removed Annotations (REMOVE)

All 18 "protein binding" (GO:0005515) annotations with IPI evidence were removed per curation guidelines:
- PMIDs: 15965487, 16611985, 17983804, 23698369, 23213405, 36271492, 10959840, 11062478, 11136718, 17567603, 26030138, 23652018, 12711669, 18790802, 20457750, 19390626, 10666337, 10788521

**Rationale**: "Protein binding" is too vague and provides no useful functional information. TOP2A does interact with many proteins (BRCA1, PKC, histone deacetylase, 14-3-3, p53, DHX9, condensins, etc.), but more specific binding terms like "protein kinase C binding" (GO:0005080) are retained where appropriate.

### Non-Core Annotations (KEEP_AS_NON_CORE)

**Viral replication**:
- GO:0045870 (positive regulation of single stranded viral RNA replication via double stranded DNA intermediate) - IEA and IMP
  - Very specific term for HIV-1 replication context
  - Represents general role in resolving topological stress during reverse transcription

**Circadian/rhythmic processes**:
- GO:0042752 (regulation of circadian rhythm) - IEA and ISS
- GO:0048511 (rhythmic process) - IEA
  - Peripheral to core function
  - May relate to transcriptional regulation or cell cycle timing

**Transcriptional regulation**:
- GO:0045944 (positive regulation of transcription by RNA polymerase II) - IEA
  - Not a primary function (TOP2B is main isoform for transcription)
  - TOP2A contributes in rapidly dividing cells

**Developmental processes**:
- GO:0002244 (hematopoietic progenitor cell differentiation) - IEA
- GO:0040016 (embryonic cleavage) - IEA
  - Reflect TOP2A requirement in proliferating cells
  - Context-dependent rather than specialized functions

## Evidence Assessment

### IBA Annotations (Phylogenetic Inference)
All 5 IBA annotations were ACCEPTED:
- GO:0003918 (DNA topoisomerase type II activity)
- GO:0005634 (nucleus)
- GO:0000819 (sister chromatid segregation)
- GO:0000712 (resolution of meiotic recombination intermediates)
- GO:0030263 (apoptotic chromosome condensation)

**Assessment**: IBA annotations are well-curated and represent appropriate level of specificity for core TOP2A functions.

### IDA/IMP Annotations (Direct Experimental)
26 annotations with direct experimental evidence (IDA/IMP) were all ACCEPTED.
Key experimental studies:
- PMID:15491148 - DNA topoisomerase activity
- PMID:12711669 - Chromatin organization, DHX9 interaction
- PMID:16611985 - PKC binding, DNA damage response, apoptosis
- PMID:22323612 - Mg2+ binding, DNA bending, topological change
- PMID:10959840 - Apoptotic chromosome condensation
- Multiple studies - Nuclear/nucleolar localization

### IEA Annotations (Electronic Inference)
34 IEA annotations reviewed:
- Most ACCEPTED as correct but general terms
- Some marked KEEP_AS_NON_CORE for developmental/context-specific processes
- Provide useful hierarchical classification despite being computationally inferred

## Supporting Evidence Sources

Primary evidence from:
1. **Deep research file** (TOP2A-deep-research-openai.md) - Comprehensive literature synthesis
2. **UniProt entry** (P11388) - Curated protein information
3. **Primary literature** - 40+ PMIDs cited in annotations
4. **Reactome pathways** - 3 pathway annotations (SUMOylation, DREAM complex regulation)

## Recommendations for GO

### Terms to Retain
All ACCEPT and KEEP_AS_NON_CORE annotations should be retained in GO databases.

### Terms to Remove
Consider removing the 18 generic "protein binding" IPI annotations from public GO databases as they provide minimal functional information compared to more specific interaction terms.

### Annotation Quality
- Core functions very well annotated with appropriate evidence codes
- Good balance of specific (type II topoisomerase) and hierarchical (isomerase) terms
- Cellular component annotations comprehensive and well-supported
- Biological process annotations capture both core (segregation, condensation) and context-specific (apoptosis, viral replication) roles

## Conclusion

TOP2A is exceptionally well-annotated in GO. The core functions are captured accurately at the appropriate level of specificity. The main curation improvement is removing uninformative generic "protein binding" terms while retaining more specific protein interaction annotations. The reviewed annotation set provides a comprehensive and accurate representation of TOP2A's essential role as an ATP-dependent type II topoisomerase required for DNA replication, chromosome condensation, and mitotic chromosome segregation.
