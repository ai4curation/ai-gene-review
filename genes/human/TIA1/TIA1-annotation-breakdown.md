# TIA1 GO Annotation Breakdown

## Summary by GO Aspect

### Molecular Function (MF) - 12 annotations
| GO ID | Term | Action | Evidence | Key Notes |
|-------|------|--------|----------|-----------|
| GO:0140517 | protein-RNA adaptor activity | ACCEPT | IBA | Core adaptor function |
| GO:0003676 | nucleic acid binding | MODIFY→GO:0003723 | IEA | Too general |
| GO:0003723 | RNA binding | ACCEPT (4×) | IEA, IDA, HDA(2×) | Core function, multiple confirmations |
| GO:0003730 | mRNA 3'-UTR binding | ACCEPT (2×) | IEA, ISS | 3'UTR binding for translation regulation |
| GO:0035925 | mRNA 3'-UTR AU-rich region binding | ACCEPT | IEA | Most specific 3'UTR binding term |
| GO:0008143 | poly(A) binding | ACCEPT | TAS | Historical characterization |
| GO:0005515 | protein binding | MODIFY (5×) | IPI | Too general, replace with GO:0140517 |

**MF Summary**: Core functions are RNA binding (U-rich/AU-rich specificity) and protein-RNA adaptor activity. Generic "protein binding" should be replaced with more informative terms.

### Biological Process (BP) - 11 annotations
| GO ID | Term | Action | Evidence | Key Notes |
|-------|------|--------|----------|-----------|
| GO:0000381 | regulation of alternative mRNA splicing, via spliceosome | ACCEPT (4×) | IBA, IEA, IDA(2×) | Core function, best characterized |
| GO:0006397 | mRNA processing | ACCEPT | IEA | Broad but correct |
| GO:0008380 | RNA splicing | ACCEPT | IEA | Broad but correct |
| GO:0048024 | regulation of mRNA splicing, via spliceosome | ACCEPT (2×) | IDA | Intermediate specificity |
| GO:0006915 | apoptotic process | ACCEPT (2×) | IEA, TAS | Context-dependent function |
| GO:0017148 | negative regulation of translation | ACCEPT (2×) | IEA, ISS | Core cytoplasmic function |
| GO:0034063 | stress granule assembly | ACCEPT | IDA | Core stress response function |
| GO:1903608 | protein localization to cytoplasmic stress granule | ACCEPT | IMP | Active recruitment role |

**BP Summary**: Three major biological processes - (1) alternative splicing regulation, (2) stress granule assembly and stress response, (3) translational repression. Apoptosis is context-dependent.

### Cellular Component (CC) - 20 annotations
| GO ID | Term | Action | Evidence | Key Notes |
|-------|------|--------|----------|-----------|
| GO:0005634 | nucleus | ACCEPT (3×) | IEA, IDA(2×) | Primary location under normal conditions |
| GO:0005654 | nucleoplasm | ACCEPT (2×) | IDA, TAS | More specific than nucleus |
| GO:0005737 | cytoplasm | ACCEPT (3×) | IEA, IDA(2×) | Stress-induced translocation |
| GO:0005829 | cytosol | ACCEPT | IDA | Specific cytoplasmic compartment |
| GO:0010494 | cytoplasmic stress granule | ACCEPT (5×) | IEA, IDA(2×), ISS | Core stress response location |
| GO:0097165 | nuclear stress granule | ACCEPT (2×) | IEA, IDA | Less common but documented |

**CC Summary**: Dynamic dual localization - nuclear (splicing) under normal conditions, cytoplasmic (stress granules, translation) under stress. Both cytoplasmic and nuclear stress granules documented.

## Evidence Code Distribution

| Evidence Code | Count | Interpretation |
|---------------|-------|----------------|
| IEA | 12 | Automated computational inference |
| IDA | 13 | Direct experimental assay |
| IBA | 2 | Phylogenetic inference |
| ISS | 3 | Sequence similarity inference |
| IPI | 5 | Protein interaction |
| IMP | 1 | Mutant phenotype |
| TAS | 3 | Traceable author statement |
| HDA | 2 | High-throughput direct assay |

**Total**: 41 evidence instances for 43 annotation lines (some have multiple instances of same term)

## Curation Actions by Evidence Type

### IEA (Electronic Annotation)
- **ACCEPT**: 11/12 (91.7%)
- **MODIFY**: 1/12 (8.3%) - GO:0003676 too general

### IDA (Direct Assay)
- **ACCEPT**: 13/13 (100%)
- High confidence experimental evidence

### IPI (Protein Interaction)
- **ACCEPT**: 0/5 (0%)
- **MODIFY**: 5/5 (100%)
- All instances of non-informative "protein binding" term

### Other Evidence (IBA, ISS, IMP, TAS, HDA)
- **ACCEPT**: 16/16 (100%)
- All validated as appropriate

## Key Findings

1. **Highly confident annotations**: IDA and IBA annotations are uniformly high quality
2. **Main curation issue**: Generic "protein binding" term (5 instances) needs replacement
3. **No incorrect annotations**: All terms represent valid aspects of TIA1 biology
4. **Well-balanced coverage**: Good representation across all three GO aspects
5. **Evidence diversity**: Mix of computational, experimental, and curated evidence
6. **Duplicate terms acceptable**: Multiple instances of same GO term with different evidence codes provides robust support

## Annotation Specificity Analysis

### Optimal Specificity
- GO:0035925 (mRNA 3'-UTR AU-rich region binding) - captures exact binding specificity
- GO:0000381 (regulation of alternative mRNA splicing, via spliceosome) - precise mechanism
- GO:0140517 (protein-RNA adaptor activity) - functionally informative
- GO:0034063 (stress granule assembly) - specific biological process

### Acceptable Broad Terms
- GO:0003723 (RNA binding) - fundamental activity
- GO:0006397 (mRNA processing) - general process
- GO:0005634 (nucleus), GO:0005737 (cytoplasm) - general locations

### Terms Requiring Replacement
- GO:0003676 (nucleic acid binding) - too general, replace with GO:0003723
- GO:0005515 (protein binding) - uninformative, replace with GO:0140517
