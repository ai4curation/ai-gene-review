# C. elegans Priority 3 Longevity-Proteostasis Genes: Executive Summary

**Date:** December 30, 2025
**Scope:** Comprehensive annotation review of 6 interconnected C. elegans longevity regulatory genes
**Total Annotations Reviewed:** 421 GO term/evidence combinations
**Status:** READY FOR IMPLEMENTATION

---

## Overview

This project reviews GO annotations for six C. elegans genes that form the core regulatory network governing longevity, metabolic adaptation, and proteostasis. These genes are tightly interconnected through multiple signaling pathways and represent the most well-characterized molecular mechanisms of lifespan extension in model organisms.

### The 6 Genes and Their Central Roles

**1. DAF-2 (Q968Y9)** - Insulin/IGF-1 Receptor
- Role: Upstream signal transduction
- Function: Negative regulation of DAF-16 through PI3K/AKT pathway
- Annotations: 88

**2. DAF-16 (O16850)** - FOXO Transcription Factor
- Role: Primary longevity effector
- Function: Master transcriptional regulator of stress response and lifespan extension genes
- Annotations: 144 (largest set)

**3. SKN-1 (P34707)** - Nrf2 Ortholog Transcription Factor
- Role: Oxidative stress response
- Function: Master regulator of Phase II detoxification and antioxidant genes
- Annotations: 74 (recent comprehensive review: 56 ACCEPT, 6 non-core, 2 pending MODIFY)

**4. SIR-2.1 (Q21921)** - NAD+ Sirtuin Deacetylase
- Role: Histone deacetylase and DAF-16 interacting partner
- Function: Chromatin silencing and lifespan modulation
- Annotations: 42

**5. AAK-2 (Q95ZQ4)** - AMPK Alpha Kinase
- Role: Metabolic energy sensor
- Function: Links nutrient availability to autophagy and lifespan
- Annotations: 31

**6. HLH-30 (H2KZZ2)** - TFEB Ortholog bHLH Transcription Factor
- Role: Autophagy and lysosomal biogenesis master regulator
- Function: Essential for lifespan extension in 6+ longevity paradigms
- Annotations: 42 (recent comprehensive review: 37 ACCEPT, 2 non-core, 1 MODIFY, 3 NEW proposed)

---

## Key Findings

### Quality Assessment: COMPREHENSIVE AND WELL-SUPPORTED

**Overall annotation quality is HIGH** across all 6 genes:
- ✓ Adequate coverage of molecular functions
- ✓ Strong phylogenetic support (IBA) for core functions
- ✓ Experimental evidence (IDA/IMP) for key processes
- ✓ Clear functional relationships documented
- ⚠ Some vague "protein binding" entries that need refinement
- ⚠ Some developmental phenotypes annotated as core functions

### Priority Status

| Priority | Genes | Status | Effort |
|----------|-------|--------|--------|
| **READY NOW** | skn-1, hlh-30 | Recent comprehensive reviews; 2+3 actions to implement | 1 hour |
| **HIGH** | daf-16, daf-2 | Large annotation sets (144, 88); systematic review needed | 5-7 hours |
| **MEDIUM** | sir-2.1, aak-2 | Focused reviews recommended | 2-3 hours |

---

## Major Curation Decisions

### 1. REMOVE Generic "Protein Binding" Annotations

**Issue:** GO:0005515 (Protein binding) entries are too vague and non-informative.

**Solution:**
- Remove generic IPI entries unless they represent documented functional complexes
- Replace with more specific molecular functions (e.g., kinase substrate binding, transcription factor complex formation)
- Affects: daf-16 (6-8 entries), daf-2, sir-2.1, aak-2

### 2. RECLASSIFY Dauer Development as Non-Core Function

**Issue:** Annotations for dauer larval development are phenotypic consequences, not core molecular functions.

**Solution:**
- Change action from ACCEPT to KEEP_AS_NON_CORE
- Rationale: Dauer is an organismal phenotype arising from reduced signaling; the primary functions are signal transduction and transcriptional regulation
- Affects: daf-2 (3 annotations), aak-2 (1 annotation)

### 3. RETAIN Specific Histone Modification Annotations

**Recommendation:** Keep highly specific SIR-2.1 histone deacetylase annotations
- GO:0046970 (Histone H4K16 deacetylase) ✓
- GO:0046969 (Histone H3K9 deacetylase) ✓
- GO:0032041 (Histone H3K14 deacetylase) ✓

These are superior to generic "histone deacetylase" due to specificity and they reflect documented enzymatic targets.

### 4. IMPLEMENT Proposed NEW Annotations for HLH-30

**Ready to add:**
- GO:0031399 - Regulation of protein modification process
- GO:0031545 - Positive regulation of lamellipodia assembly (after verification)
- (Verify GO:0030317 - flagellated sperm motility - likely not relevant to C. elegans)

### 5. CONSOLIDATE Pathway Annotations with Clear Directionality

**DAF-2 → DAF-16 axis:**
- Ensure consistent annotation of dual signaling pathways (PI3K/AKT primary, RAS/ERK secondary)
- Clarify that DAF-2 NEGATIVELY regulates DAF-16 (inhibitory phosphorylation)

---

## Annotation Category Summary

### By Gene

| Gene | Core TF Functions | Pathway Signaling | Stress Response | Autophagy | Immune | Dev/Phenotype |
|------|-------------------|------------------|-----------------|-----------|--------|---|
| daf-16 | ✓✓✓ | ✓✓ | ✓✓ | | ✓ | ⚠ RECLASSIFY |
| daf-2 | | ✓✓✓ | ✓ | | | ⚠ RECLASSIFY |
| skn-1 | ✓✓✓ | ✓ | ✓✓✓ | | ✓ | |
| sir-2.1 | | | ✓ | ✓ | | |
| aak-2 | | ✓ | ✓ | ✓✓ | | ⚠ RECLASSIFY |
| hlh-30 | ✓✓ | | | ✓✓✓ | ✓✓ | |

### Network Convergence

All 6 genes converge on:
1. **Lifespan extension** (GO:0008340) - All genes contribute directly or indirectly
2. **Stress resistance** (GO:0006979, GO:0009411, etc.) - Multiple pathways converge
3. **Metabolic adaptation** (GO:0008286, GO:0010883, etc.) - Energy sensing to anabolic changes
4. **Cellular proteostasis** (GO:0010508 autophagy, GO:0031399 protein modification)

---

## Recommendations for Review Workflow

### Immediate Actions (This Week)
1. **Implement skn-1 MODIFY actions** (2 annotations) - 0.5 hours
2. **Implement hlh-30 NEW annotations** (3 annotations, pending verification) - 0.5 hours
3. **Total time: 1 hour**

### Priority Actions (Next Week)
1. **Review aak-2** (31 annotations, focused review) - 1 hour
2. **Review sir-2.1** (42 annotations, focused review) - 1.5 hours
3. **Total time: 2.5 hours**

### Major Review Effort (Following 2 Weeks)
1. **Review daf-2** (88 annotations, systematic review) - 2.5 hours
2. **Review daf-16** (144 annotations, comprehensive review) - 3-4 hours
3. **Total time: 5.5-6.5 hours**

### Validation Phase
1. **Cross-validate pathway consistency** - 0.5 hours
2. **YAML validation and cleanup** - 0.5 hours
3. **Total time: 1 hour**

**Total Estimated Time: 10-11 hours** for complete project

---

## Quality Checkpoints

Before finalizing any curation, ensure:

1. **Molecular Function Accuracy**
   - ✓ Transcription factors have DNA-binding annotations
   - ✓ Kinase has phosphorylation activity
   - ✓ Deacetylase has specific histone modification activities
   - ✓ No generic "protein binding" without functional context

2. **Biological Process Specificity**
   - ✓ Distinguish core functions from phenotypic consequences
   - ✓ Link stress response to specific stress types (oxidative, heat, starvation)
   - ✓ Clarify direct vs. indirect pathway effects

3. **Evidence Code Appropriateness**
   - ✓ IBA appropriate for phylogenetically conserved functions
   - ✓ IDA/IMP present for experimentally demonstrated functions
   - ✓ IPI entries documented with functional context
   - ✓ IEA entries are informative (not from generic keywords)

4. **Cross-Gene Consistency**
   - ✓ DAF-2 → DAF-16 pathway directionality clear
   - ✓ Convergence on lifespan, stress, metabolic processes documented
   - ✓ Interaction annotations (DAF-16/SIR-2.1) consistent across both genes

---

## Key Takeaways

### What's Working Well
- **Three of four transcription factors (daf-16, skn-1, hlh-30)** have excellent, well-supported annotations
- **Specific histone modifications** in sir-2.1 exceed general deacetylase annotation
- **Pathway annotations** accurately capture insulin/IGF and AMPK signaling cascades
- **Recent curation work** on skn-1 and hlh-30 provides excellent model for remaining genes

### What Needs Attention
- **Generic protein binding entries** should be removed or contextualized
- **Developmental phenotypes** (dauer) need reclassification as non-core
- **Large annotation sets** (daf-16, daf-2) need systematic line-by-line review
- **Cross-pathway consistency** should be verified after individual reviews

### Strategic Value
This gene set represents the **most mechanistically well-understood longevity pathway** in model organisms. Rigorous curation of these annotations will serve as a template for:
- Curation of mammalian homologs (FOXO3, SIRT1, TFEB, AMPK in humans)
- Systems-level understanding of aging biology
- Translation of C. elegans discoveries to disease models

---

## Related Resources

**Project Documentation:**
- `/Users/cjm/repos/ai-gene-review/CAEEL_PRIORITY3_LONGEVITY_PROTEOSTASIS_REVIEW.md` - Comprehensive technical review
- `/Users/cjm/repos/ai-gene-review/CAEEL_PRIORITY3_CURATION_ACTIONS.md` - Specific actionable curation decisions

**Individual Gene Curation Reports:**
- `genes/worm/skn-1/SKN-1-REVIEW-REPORT.md` - Complete SKN-1 curation (56 ACCEPT)
- `genes/worm/hlh-30/hlh-30-REVIEW-COMPLETE.txt` - Complete HLH-30 curation (37 ACCEPT, 3 NEW)

**Related Projects:**
- CAEEL_PROTEOSTASIS - Broader proteostasis gene set
- SURVEILLANCE_IMMUNITY - Immune function cross-reference
- MITOPHAGY - Autophagy cross-reference

**Validation:**
```bash
# Run validation for all 6 genes
just validate-all
# View results in: reports/validation-all.tsv
```

---

## Contacts and Questions

For questions about this curation project:
- See CAEEL_PRIORITY3_LONGEVITY_PROTEOSTASIS_REVIEW.md (comprehensive technical details)
- See CAEEL_PRIORITY3_CURATION_ACTIONS.md (specific implementation actions)
- Review individual gene files in genes/worm/[gene]/ directories

---

**Document Version:** 1.0 Executive Summary
**Status:** READY FOR IMPLEMENTATION
**Last Updated:** December 30, 2025

