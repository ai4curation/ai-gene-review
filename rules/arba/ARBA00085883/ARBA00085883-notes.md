# Re-review Notes for ARBA00085883

## Summary
Rule predicts GO:0030167 (proteoglycan catabolic process) for four lysosomal enzymes: beta-galactosidase, alpha-L-iduronidase, beta-hexosaminidase, and N-acetylglucosamine-6-sulfatase.

## Review Log

### 2024-12-02 - Initial Re-review

Review has action MODIFY with confidence 0.6.

### Issues Correctly Identified

1. **Dual-function enzyme conflation**:
   - IDUA (CS2), GNS (CS4) = dedicated GAG-degrading enzymes (appropriate)
   - GLB1 (CS1), Hex (CS3) = primary ganglioside degradation, secondary proteoglycan role
   - Clinical: GLB1 deficiency → GM1 gangliosidosis; Hex deficiency → Tay-Sachs/Sandhoff

2. **Taxonomic inconsistencies**:
   - CS1: Eukaryota (broad)
   - CS3: Mus only (too narrow, arbitrary)
   - Should expand CS3 to Mammalia/Vertebrata

3. **FunFam redundancy in CS2**:
   - All three IDUA FunFams match same 3 proteins (Jaccard = 1.0)

4. **GO term appropriateness**:
   - Appropriate for IDUA/GNS
   - Misleading for GLB1/Hex - should have ganglioside terms as primary

### Action Decision Analysis

MODIFY with confidence 0.6 is appropriate:
- Rule has legitimate biology but conflates distinct enzyme roles
- Not severe enough for DEPRECATE - core annotations are correct
- Moderate confidence reflects the nuanced situation

### Recommendations from Review
1. Consider splitting into dedicated vs dual-function enzyme rules
2. Add primary ganglioside annotations for GLB1/Hex
3. Expand CS3 from Mus to Mammalia
4. Remove redundant IDUA FunFams

## Status: REVIEW APPROVED
The analysis is thorough and the MODIFY decision with 0.6 confidence appropriately reflects the nuanced issues.
