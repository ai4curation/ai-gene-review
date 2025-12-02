# Re-review Notes for ARBA00089176

## Summary
Rule predicts GO:1990840 (response to lectin) for serine/threonine kinases and p300/CBP acetyltransferases.

## Review Log

### 2024-12-02 - Initial Re-review

Review has action DEPRECATE with confidence 0.25.

### Critical Design Flaw (CORRECTLY IDENTIFIED)

The rule uses **generic downstream signaling components** to predict a **stimulus-specific response**:
- Non-specific serine/threonine kinase domains → participate in hundreds of pathways
- p300/CBP → interacts with ~400 proteins across diverse pathways

This is fundamentally flawed logic - like using "has a kinase domain" to predict "responds to insulin."

### Quantitative Evidence

Low containment values confirm the problem:
- Kinase domain: only 9% of proteins have GO:1990840
- p300 domains: only 40% of proteins have GO:1990840

### Other Issues
- Complete redundancy in CS2 (Jaccard = 1.0)
- Disjoint condition sets (Jaccard = 0.0 between kinases and p300)
- Arbitrary taxonomic restrictions (Primates, Catarrhini)

### Why DEPRECATE is CORRECT

Cannot be salvaged because:
1. Fundamental logic flaw
2. Would need CTLD/CLR pathway-specific signatures instead
3. Generic effectors should get core MF annotations, not pathway-specific BP

### Quality Assessment

**EXCELLENT REVIEW**:
- Correctly identifies fundamental design flaw
- Strong quantitative evidence
- Good literature analysis
- Appropriate low confidence (0.25) for deprecated rule

## Status: REVIEW APPROVED
Textbook example of how NOT to design an annotation rule. Correctly deprecated.
