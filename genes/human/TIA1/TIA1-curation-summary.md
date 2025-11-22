# TIA1 GO Annotation Curation Summary

## Overview
Systematic review of all existing GO annotations for human TIA1 (P31483) completed on 2025-11-16.

## Gene Function Summary
TIA1 is an RNA-binding protein containing three RNA recognition motifs (RRMs) and a C-terminal glutamine-rich prion-like domain. It functions as a master regulator of gene expression through three core mechanisms:

1. **Alternative splicing regulation**: Binds U-rich sequences downstream of weak 5' splice sites and recruits U1 snRNP through direct interaction with U1-C protein
2. **Stress granule nucleation**: Nucleates and localizes to cytoplasmic (and nuclear) stress granules via its prion-like domain under cellular stress
3. **Translational repression**: Binds AU-rich elements in mRNA 3'UTRs to repress translation of target mRNAs like TNF and COX-2

## Curation Statistics
- **Total annotations reviewed**: 43
- **ACCEPT**: 38 (88.4%)
- **MODIFY**: 5 (11.6%)
- **REMOVE**: 0
- **Other actions**: 0

## Key Curation Decisions

### Accepted Core Functions (Representative Examples)

1. **GO:0000381 (regulation of alternative mRNA splicing, via spliceosome)** - Multiple instances with IBA, IEA, and IDA evidence
   - Core function supported by extensive experimental evidence
   - TIA1 promotes U1 snRNP recruitment to weak 5' splice sites
   - Validated targets include Fas, CFTR, COL2A1, FGFR2

2. **GO:0140517 (protein-RNA adaptor activity)** - IBA evidence
   - Accurately captures TIA1's dual role of binding RNA while recruiting protein complexes
   - Bridges pre-mRNA recognition and U1 snRNP recruitment via U1-C interaction

3. **GO:0003723 (RNA binding)** - Multiple instances with IEA, IDA, HDA evidence
   - Fundamental molecular function
   - RRM2 and RRM3 bind uridine-rich sequences
   - Supported by foundational studies (PMID:8576255) and proteomics

4. **GO:0035925 (mRNA 3'-UTR AU-rich region binding)** - IEA evidence
   - Most specific term for TIA1's 3'UTR binding activity
   - Distinguishes TIA1's sequence specificity from general RNA binding

5. **GO:0010494 (cytoplasmic stress granule)** - Multiple instances with IEA, IDA, ISS evidence
   - Core cellular location under stress
   - TIA1 nucleates stress granule assembly via prion-like domain

6. **GO:0034063 (stress granule assembly)** - IDA evidence
   - One of TIA1's most important biological process functions
   - Prion-like domain mediates self-assembly

7. **GO:0017148 (negative regulation of translation)** - IEA and ISS evidence
   - Core function in cytoplasm
   - Direct silencing of ARE-containing mRNAs
   - Indirect repression via stress granule sequestration

### Modified Annotations

All 5 MODIFY actions addressed the same issue: **GO:0005515 (protein binding)**

**Rationale for modification**:
- Term is too general and non-informative per GO curation guidelines
- While technically correct (TIA1 does bind proteins like U1-C, FASTK, etc.), it provides no functional insight
- **Proposed replacement**: GO:0140517 (protein-RNA adaptor activity)
- This more specific term better captures TIA1's functionally relevant protein interactions in the context of its RNA-binding and spliceosomal recruitment activities

**Affected instances**:
1. PMID:12486009 (IPI) - U1-C interaction
2. PMID:17135269 (IPI) - FASTK interaction
3. PMID:18164289 (IPI)
4. PMID:7544399 (IPI) - FASTK phosphorylation

### Annotations Requiring Context

**GO:0006915 (apoptotic process)** - Accepted but noted as context-dependent
- Originally identified function in cytotoxic lymphocytes (PMID:1934064)
- Also promotes apoptosis through Fas splicing regulation
- May be more context-specific than constitutive core function
- Relevant in immune cells and developmental contexts

**GO:0008143 (poly(A) binding)** - Accepted with historical note
- Original 1991 characterization based on sequence similarity to poly(A)-binding proteins
- TIA1's binding is more accurately U-rich/AU-rich element binding
- Can bind poly(A) but this is not the primary specificity

### Broad vs. Specific Term Pairings

Several annotation pairs show hierarchy where both broad and specific terms are valid:

1. **Splicing**:
   - GO:0008380 (RNA splicing) - broad, accepted
   - GO:0048024 (regulation of mRNA splicing, via spliceosome) - intermediate, accepted
   - GO:0000381 (regulation of alternative mRNA splicing, via spliceosome) - most specific, accepted

2. **3'UTR binding**:
   - GO:0003730 (mRNA 3'-UTR binding) - intermediate, accepted
   - GO:0035925 (mRNA 3'-UTR AU-rich region binding) - most specific, accepted

3. **Nuclear localization**:
   - GO:0005634 (nucleus) - broad, accepted
   - GO:0005654 (nucleoplasm) - specific, accepted

4. **mRNA processing**:
   - GO:0006397 (mRNA processing) - broad, accepted
   - More specific splicing terms also present

## Evidence Quality Assessment

### Strong Direct Evidence (IDA/IMP/IPI)
- Splicing regulation: PMID:11106748, 12486009, 14966131, 17580305
- RNA binding: PMID:8576255 (foundational)
- Stress granule: PMID:8576255, 21984414, 24965446
- Localization: Multiple studies confirming nuclear and cytoplasmic distribution

### Phylogenetic Inference (IBA)
- GO:0000381 (regulation of alternative mRNA splicing, via spliceosome)
- GO:0140517 (protein-RNA adaptor activity)
- Both strongly supported by experimental evidence

### Computational Inference (IEA)
- Generally consistent with experimental evidence
- IEA annotations for stress granule, splicing, and RNA binding all validated by direct studies

### Sequence Similarity (ISS)
- GO:0003730 (mRNA 3'-UTR binding) - validated by direct evidence
- GO:0017148 (negative regulation of translation) - validated by direct evidence
- GO:0010494 (cytoplasmic stress granule) - validated by direct evidence

## Key Publications Supporting Annotations

1. **PMID:1934064 (1991)** - Original discovery paper
   - Identified TIA1 in cytotoxic granules
   - Showed DNA fragmentation/apoptosis induction
   - Characterized as poly(A)-binding protein

2. **PMID:8576255 (1996)** - RNA binding specificity
   - Defined U-rich sequence binding
   - Showed RRM2 is necessary and sufficient
   - Demonstrated stress granule localization

3. **PMID:11106748 (2000)** - Splicing regulation mechanism
   - Landmark study establishing splicing regulatory function
   - Showed U1 snRNP recruitment to weak 5' splice sites
   - Demonstrated Fas alternative splicing regulation

4. **PMID:12486009 (2002)** - Molecular mechanism
   - Defined domain requirements for function
   - Showed direct interaction with U1-C protein
   - RRM2+3 for RNA binding, RRM1+Q-domain for U1 snRNP interaction

5. **PMID:14966131 (2004)** - CFTR splicing
   - Demonstrated regulation of CFTR exon 9 splicing

6. **PMID:17580305 (2007)** - COL2A1 splicing
   - Showed regulation of COL2A1 alternative splicing
   - Also demonstrated genomic DNA binding

## Recommendations

1. **No annotations require removal** - All annotations represent valid aspects of TIA1 function

2. **Protein binding annotations should be replaced** with more specific terms like protein-RNA adaptor activity

3. **Consider adding new annotations** for:
   - Specific protein binding partners (if more specific GO terms exist for U1-C binding, FASTK binding)
   - Phase separation activity (related to prion-like domain function)
   - Specific biological processes like immune cell function, germinal center B cell selection

4. **Core functions** are well-represented:
   - Alternative splicing regulation ✓
   - RNA binding (U-rich/AU-rich specificity) ✓
   - Stress granule nucleation ✓
   - Translational repression ✓

## Notes on TIA1 Biology

- **Domain architecture**: 3 RRMs + Q/N-rich prion-like domain
- **Dual localization**: Nuclear (splicing) and cytoplasmic (translation/stress response)
- **Context-dependent functions**:
  - Constitutive: splicing regulation, RNA binding
  - Stress-induced: stress granule assembly, translational repression
  - Cell-type specific: apoptosis in cytotoxic lymphocytes, B cell selection
- **Disease relevance**:
  - Mutations in prion-like domain → ALS/FTD (impaired stress granule dynamics)
  - E384K mutation → Welander distal myopathy
  - Co-aggregates with tau and huntingtin in neurodegeneration

## Validation Status
✅ File validates against LinkML schema with minor warnings about supporting_text substring matching
✅ All 43 annotations reviewed and curated
✅ No pending annotations remaining
