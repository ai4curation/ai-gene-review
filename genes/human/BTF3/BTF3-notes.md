# BTF3 (BTN3A3) Gene Review Notes

## Review Completed: 2025-11-16

### Key Findings

**Gene Identity Issue:**
- The gene symbol BTF3 is actually a synonym for BTN3A3 (Butyrophilin subfamily 3 member A3)
- UniProt ID: O00478
- The primary gene symbol should be BTN3A3, not BTF3

### Annotation Review Summary

Reviewed all 13 existing GO annotations for BTN3A3:

**ACCEPT (7 annotations):**
1. GO:0009897 (external side of plasma membrane) - IBA - Well-supported by protein topology
2. GO:0002250 (adaptive immune response) - IEA - Appropriate general term
3. GO:0002376 (immune system process) - IEA - Correct broad term
4. GO:0005886 (plasma membrane) - IEA, TAS, IDA - Multiple lines of evidence
5. GO:0016020 (membrane) - HDA - General but correct
6. GO:0002456 (T cell mediated immunity) - IMP - Core function from PMID:22767497

**KEEP_AS_NON_CORE (2 annotations):**
1. GO:0001817 (regulation of cytokine production) - IBA - Limited specific evidence for BTN3A3
2. GO:0050852 (T cell receptor signaling pathway) - IBA - BTN3A1 is primary, BTN3A3 supporting

**MODIFY (4 annotations):**
1. GO:0005102 (signaling receptor binding) - IBA - Too vague, should be immune receptor activity or protein heterodimerization activity
2. GO:0005515 (protein binding) x2 - IPI - Per guidelines, should be protein heterodimerization activity

### Critical Literature

1. **PMID:22767497** - Key study demonstrating CD277/BTN3A role in Vγ9Vδ2 T cell activation
   - Showed BTN3A1 is primary functional isoform
   - BTN3A3 can activate T cells with agonist antibody but doesn't respond to phosphoantigens alone

2. **PMID:29339503** - Demonstrated heteromeric interactions
   - BTN3A3 can heterodimerize with BTN3A1
   - BTN3A3 has potential to functionally collaborate with BTN3A1

### Core vs. Non-Core Functions

**Core Functions:**
- Type I transmembrane protein localized to plasma membrane
- Protein heterodimerization (with BTN3A1)
- T cell mediated immunity (supporting role)

**Non-Core/Supporting:**
- Regulation of cytokine production (indirect)
- T cell receptor signaling (via collaboration with BTN3A1)

### Proposed Improvements

1. Replace vague "protein binding" and "signaling receptor binding" terms with:
   - GO:0140375 (immune receptor activity)
   - GO:0046982 (protein heterodimerization activity)

2. Consider adding new annotations for:
   - Protein homodimerization activity (BTN3A3 can homodimerize)
   - B30.2/SPRY domain function

### Notes

- BTN3A3 is less functionally active than BTN3A1 but can complement/support BTN3A1 function
- The protein structure includes: 2 extracellular Ig domains (IgV, IgC), transmembrane domain, intracellular B30.2 (PRYSPRY) domain
- Expression detected in peripheral blood mononuclear cells, T-cells, spleen, lymphocytes
- Potential roles in cancer biology (breast cancer, NSCLC) per deep research
