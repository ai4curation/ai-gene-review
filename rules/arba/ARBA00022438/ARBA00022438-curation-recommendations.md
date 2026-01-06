# ARBA00022438 Curation Recommendations for GO Curators

## Executive Summary

**Rule**: ARBA00022438 - Aminopeptidase annotation rule  
**Current Status**: Problematic mega-rule requiring immediate attention  
**Recommendation**: MODIFY - Decompose into family-specific rules  
**Priority**: HIGH (affects 212,202 proteins)  
**Confidence**: Very High (multiple critical issues identified)

## Critical Issues Identified

### 1. **Missing GO Annotations** (Critical)
- **Current**: Only keyword annotation (KW-0031 "Aminopeptidase")
- **Missing**: Essential GO terms for enzyme function
- **Impact**: Proteins lack proper molecular function and biological process annotations
- **Required Action**: Add GO:0004177 (aminopeptidase activity) and GO:0006508 (proteolysis) at minimum

### 2. **Excessive Complexity** (High)
- **Current**: 86 condition sets across multiple enzyme families
- **Problem**: Impossible to manually validate; high maintenance burden
- **Impact**: Increased false positive risk; curation bottleneck
- **Required Action**: Decompose into focused rules with <20 condition sets each

### 3. **Mechanistic Incoherence** (High)
- **Current**: Combines zinc-dependent, iron-dependent, and serine proteases
- **Problem**: Different catalytic mechanisms, cofactors, and evolutionary origins
- **Impact**: Inappropriate unification of distinct enzyme families
- **Required Action**: Separate rules for each mechanistic family

## Detailed Curation Recommendations

### Immediate Actions Required

1. **Suspend Current Rule**
   - Stop automated application of ARBA00022438
   - Review recent annotations for false positives
   - Plan systematic replacement strategy

2. **Create Family-Specific Rules**
   - **ARBA-M1-aminopeptidases**: Leucyl/methionyl aminopeptidases
     - Target InterPro domains: IPR000819, IPR011356
     - GO terms: GO:0004177, GO:0006508, GO:0008235 (metalloexopeptidase activity)
   - **ARBA-M24-methionine-aminopeptidases**: Co-translational processing
     - Target InterPro domains: IPR001261
     - GO terms: GO:0004177, GO:0018206 (peptidyl-methionine modification)
   - **ARBA-M2-ACE-family**: Angiotensin-converting enzyme family
     - Target InterPro domains: IPR001375
     - GO terms: GO:0004177, GO:0008237 (metallopeptidase activity)

### GO Annotation Strategy

Each replacement rule should include:

**Core Molecular Function**:
- GO:0004177 (aminopeptidase activity) - universal
- Family-specific cofactor terms (e.g., GO:0008235 for zinc-dependent)

**Core Biological Process**:
- GO:0006508 (proteolysis) - universal
- Family-specific processes (e.g., GO:0018206 for methionine processing)

**Cellular Component** (as appropriate):
- GO:0005737 (cytoplasm) for cytoplasmic aminopeptidases
- GO:0005886 (plasma membrane) for membrane-bound forms
- GO:0005783 (endoplasmic reticulum) for ER-associated forms

### Quality Control Measures

1. **Validation Requirements**
   - Each new rule must have <20 condition sets
   - Manual review of representative proteins from each condition set
   - Literature validation of GO term assignments
   - Cross-check with existing rules for conflicts

2. **Testing Protocol**
   - Apply new rules to test dataset
   - Compare annotations with manual curation
   - Validate absence of false positives in related enzyme families

3. **Documentation Standards**
   - Clear biological rationale for each condition set
   - Literature citations supporting GO term choices
   - Taxonomic scope justification
   - Regular review schedule (annually)

### Taxonomic Considerations

1. **Universal Families** (M24 methionine aminopeptidases)
   - Apply across all kingdoms
   - No taxonomic restrictions needed

2. **Eukaryote-Specific Families** (ERAP1/2-like)
   - Restrict to eukaryotic taxa
   - Consider organellar localization

3. **Lineage-Specific Variants** (some bacterial forms)
   - Create separate rules for distinct lineages
   - Account for horizontal gene transfer events

### Implementation Timeline

**Week 1-2**: Suspend current rule, analyze affected proteins  
**Week 3-4**: Design replacement rules with appropriate GO terms  
**Week 5-6**: Test and validate replacement rules  
**Week 7-8**: Deploy new rules, monitor for issues  
**Week 9-12**: Comprehensive validation and adjustment period

### Success Metrics

1. **Coverage**: Maintain annotation of legitimate aminopeptidases
2. **Precision**: Reduce false positive rate by >90%
3. **GO Compliance**: 100% of annotated proteins have appropriate GO terms
4. **Maintainability**: Each rule manageable by single curator (<2 hours review time)

### Long-term Strategy

This case highlights the need for systematic review of mega-rules in the ARBA system. Recommend:

1. **Complexity Audit**: Identify all rules with >50 condition sets
2. **GO Coverage Analysis**: Rules lacking essential GO annotations
3. **Family Coherence Review**: Rules spanning multiple enzyme families
4. **Automated Monitoring**: Flag rules exceeding complexity thresholds

### Contact Information

For implementation questions or additional analysis:
- **Primary Contact**: GO Curation Team
- **Technical Support**: UniProt ARBA Development Team
- **Review Status**: Complete analysis available in ARBA00022438-review.yaml

## Conclusion

ARBA00022438 represents a classic example of over-ambitious rule design that prioritizes coverage over accuracy and maintainability. While well-intentioned, it violates fundamental principles of computational annotation systems. The recommended decomposition strategy will provide more accurate, maintainable, and GO-compliant annotations for the aminopeptidase family while serving as a model for addressing similar mega-rules in the ARBA system.

**Immediate action required to prevent continued propagation of inadequate annotations.**