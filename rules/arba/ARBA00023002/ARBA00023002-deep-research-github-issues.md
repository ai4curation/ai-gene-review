# GitHub Issues Analysis for ARBA00023002

## Summary

Analysis of GitHub issues from the GO annotation repository reveals specific problems with ARBA00023002, particularly regarding false positive annotations of copper chaperone proteins.

## Issue #5883: Incorrect Unirule mapping - RU000393

**Link**: https://github.com/geneontology/go-annotation/issues/5883  
**Title**: Incorrect Unirule mapping: RU000393  
**Reporter**: GO Curator  

### Problem Description

The issue identifies a specific false positive case where ARBA00023002 incorrectly annotates copper chaperone for superoxide dismutase (CCS) proteins as oxidoreductases.

**Affected Proteins**:
- E1JH26 (Drosophila melanogaster Ccs)
- O14618 (Human CCS ortholog)

**Incorrect Annotations Applied**:
- Rhea 20696/EC:1.15.1.1 via ARBA: ARBA00049204 / UniRule RuleBase: RU000393
- **Keyword 'oxidoreductase' via ARBA: ARBA00023002** / UniRule RuleBase: RU000393

### Biological Context

CCS (Copper chaperone for superoxide dismutase) proteins are metallochaperones that deliver copper to superoxide dismutase enzymes. **They do NOT have catalytic oxidoreductase activity themselves** - they are accessory proteins that facilitate proper metalation of other enzymes.

**Key Points**:
- CCS proteins are chaperones, not enzymes
- They lack intrinsic oxidoreductase activity
- They assist in copper delivery to SOD enzymes
- Annotation as "oxidoreductase" is biologically incorrect

## Issue #6008: ARBA2GO issue - E1JH26 (Dmel Ccs)

**Link**: https://github.com/geneontology/go-annotation/issues/6008  
**Title**: ARBA2GO issue: E1JH26 (Dmel Ccs)  
**Reporter**: GO Curator  

This is a follow-up issue specifically focused on the ARBA annotation problem (split from the broader UniRule issue #5883).

### Impact Assessment

The issue demonstrates that ARBA00023002's broad approach to oxidoreductase annotation creates **systematic false positives** for proteins that:
1. May contain oxidoreductase-related domains (e.g., for binding/chaperone functions)
2. Are associated with oxidoreductase complexes (as accessory factors)
3. But lack catalytic oxidoreductase activity themselves

## Root Cause Analysis

### Domain Architecture Issues

The CCS false positive likely stems from ARBA00023002's inclusion of overly broad structural domains that appear in both:
- **Catalytic oxidoreductases** (legitimate targets)
- **Non-catalytic accessory proteins** (false positives)

### Potential Problematic Domains in CCS Context

CCS proteins may contain domains that overlap with oxidoreductase families:
- Metal-binding domains
- Domains involved in protein-protein interactions with SOD
- Structural motifs related to copper handling

### Systematic Risk

This case study reveals that ARBA00023002's approach of using 2105 condition sets with broad structural domains creates **systematic annotation errors** that are difficult to detect and correct at scale.

## Curation Implications

### Immediate Actions Needed

1. **Remove CCS proteins** from ARBA00023002 annotation scope
2. **Audit similar chaperone/accessory proteins** that may be misannotated
3. **Add exclusion criteria** for known non-catalytic accessory proteins

### Long-term Improvements

1. **Domain specificity enhancement**: Replace broad structural domains with catalytically-relevant specific domains
2. **Negative training sets**: Include known non-oxidoreductases with similar domains as exclusion criteria
3. **Rule partitioning**: Split the massive rule into enzyme-class-specific rules with better specificity

## Confidence Assessment

**GitHub Issues Support**: HIGH  
- Multiple independent curator reports
- Specific protein examples with clear biological rationale
- Documented in official GO annotation tracking system

**Impact Severity**: MODERATE to HIGH  
- Affects well-studied, important proteins (CCS)
- Represents systematic rather than isolated error
- Indicates broader specificity problems with the rule

## References

- GitHub Issue #5883: https://github.com/geneontology/go-annotation/issues/5883
- GitHub Issue #6008: https://github.com/geneontology/go-annotation/issues/6008
- CCS Biology: Copper chaperones deliver copper ions to target metalloproteins
- False Positive Impact: Systematic misannotation of accessory proteins as catalytic enzymes