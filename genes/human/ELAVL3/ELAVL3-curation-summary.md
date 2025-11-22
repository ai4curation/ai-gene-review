# ELAVL3 Gene Annotation Curation Summary

## Overview
Completed systematic review of all existing GO annotations for human ELAVL3 (HuC), a neuron-specific RNA-binding protein.

## Gene Description
ELAVL3 (HuC) is a neuron-specific RNA-binding protein with three RNA recognition motifs (RRMs) that binds to AU-rich elements in the 3'-UTRs of target mRNAs to regulate mRNA stability, alternative splicing, and transcript abundance. It plays essential roles in neuronal differentiation, maintenance, and synaptic integrity, particularly in the cerebellum and hippocampus.

## Annotation Review Summary

### Accepted Annotations (6)
1. **GO:0140517 (protein-RNA adaptor activity)** - IBA
   - Core molecular function representing ELAVL3's role as an adaptor between RNA and regulatory machinery
   
2. **GO:0003723 (RNA binding)** - IEA
   - General but accurate molecular function term
   
3. **GO:0003730 (mRNA 3'-UTR binding)** - IEA
   - Specific and accurate molecular function
   
4. **GO:0007399 (nervous system development)** - IEA
   - Well-supported biological process
   
5. **GO:1990904 (ribonucleoprotein complex)** - IEA
   - Appropriate cellular component
   
6. **GO:0035925 (mRNA 3'-UTR AU-rich region binding)** - IEA
   - Most specific molecular function term

7. **GO:0035925 (mRNA 3'-UTR AU-rich region binding)** - IDA (PMID:10710437)
   - Gold standard experimental evidence for core function

### Modified Annotations (2)
1. **GO:0003676 (nucleic acid binding)** → GO:0003723 (RNA binding)
   - Too broad; ELAVL3 specifically binds RNA, not DNA
   
2. **GO:0030154 (cell differentiation)** → GO:0030182 (neuron differentiation)
   - Too general; ELAVL3 is brain-specific and specifically involved in neuronal differentiation

### Removed Annotations (2)
1. **GO:0005515 (protein binding)** - IPI (PMID:36950384)
   - Generic uninformative term from large-scale proteomics study
   
2. **GO:0005515 (protein binding)** - IPI (PMID:37207277)
   - Same rationale as above

## Core Functions Defined

### Primary Function
Binds to AU-rich elements in the 3'-UTRs of target mRNAs to regulate their stability, alternative splicing, and abundance, particularly for genes involved in neuronal function and glutamate synthesis.

**Key Evidence:**
- Direct experimental evidence (PMID:10710437) showing HuC binding to VEGF and c-myc 3'-UTRs
- IBA annotation supporting protein-RNA adaptor activity
- Involvement in nervous system development and neuron differentiation

### Cellular Localization
Forms ribonucleoprotein complexes in both nucleus and cytoplasm of neurons.

## Key References Used
- **PMID:10710437** - Direct experimental evidence for AU-rich element binding
- **Deep research file** - Comprehensive literature review
- **UniProt Q14576** - Protein annotation and domain information

## Validation Status
✓ File validates successfully with no errors
- Status: COMPLETE
- All 11 annotations reviewed and actioned
- Core functions defined with supporting evidence
