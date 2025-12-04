# Re-review Notes for ARBA00026372

## Summary
Rule predicts GO:0051998 (protein carboxyl O-methyltransferase activity) for ICMT and PIMT enzymes.

## Review Log

### 2024-12-02 - Initial Re-review
**CORRECTION**: My initial notes were incorrect. I thought this was about UDP-glycosyltransferases - that's a different rule! This rule is about protein carboxyl methyltransferases.

The review is EXCELLENT:
- Correctly identifies that rule conflates two distinct enzyme families (ICMT vs PIMT)
- These families are completely DISJOINT (0% protein overlap)
- Literature explicitly contradicts combining them
- Action is DEPRECATE with confidence 0.95

### Key Issues Correctly Identified
1. **Two distinct enzyme families**:
   - ICMT: ER membrane protein, methylates prenylated Cys, permanent modification
   - PIMT: Cytosolic repair enzyme, methylates isoaspartyl, transient repair cycle

2. **GO term too broad**: GO:0051998 is generic parent; should use:
   - GO:0004671 for ICMT
   - GO:0004719 for PIMT

3. **Internal redundancy**: IPR025770 completely contained in IPR007269

4. **Taxonomic incoherence**: Some CSs have no restriction, others Fungi-only, others Metazoa-only

### Recommendations from Review
1. DEPRECATE this rule
2. Create separate ICMT rule → GO:0004671
3. Create separate PIMT rule → GO:0004719

## Status: REVIEW APPROVED
This is an excellent review. No modifications needed - the analysis is thorough and the DEPRECATE decision is well-justified.
