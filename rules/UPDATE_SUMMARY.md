# Rule Review Updates - 2025-12-01

## Summary

Updated 4 ARBA rule reviews based on corrected assessments from `entries` field analysis. The key methodological insight was that **low containment to GO terms does NOT indicate inaccuracy when proteins are annotated to more specific child terms**. However, **low pairwise overlap between conditions using AND logic DOES indicate logical errors**.

## Files Updated

### ARBA00047244: Amide Catabolic Process - **DEPRECATE**

**Changes:**
- `action`: MODIFY → **DEPRECATE**
- `parsimony.assessment`: ACCEPTABLE → **OVERLY_COMPLEX**
- Removed deprecated `global_pairwise_overlap` and `global_pairwise_overlap_thresholds` fields

**Key Issues Identified:**
1. **Fatal AND logic error in CS1**: Urease domains have only 4-10% pairwise overlap but use AND logic, creating a triple intersection of ≤10 proteins from 851 total urease proteins (99% false negative rate)
2. **Perfect redundancy in CS2**: Two PM20D1 FunFams with identical 10-protein sets (1.10.150.900:FF:000003 ≡ 3.40.630.10:FF:000027)
3. **Subsetting issue in CS3**: UAH (2 proteins) ⊆ AAH (7 proteins) with AND logic, missing 5 AAH-only proteins
4. **Biological context issue**: PM20D1's primary role is thermogenic lipid signaling, not nitrogen catabolism

**Rationale:** Each urease domain individually predicts GO:0043605 with 100% containment, proving each is sufficient and AND logic is incorrect.

---

### ARBA00089174: Adaptive Thermogenesis - **MODIFY**

**Changes:**
- `parsimony.assessment`: ACCEPTABLE → **REDUNDANT**

**Key Issues Identified:**
1. **Perfect redundancy in CS1**: Two PM20D1 FunFams with identical 10-protein sets (same as ARBA00047244)
   - `1.10.150.900:FF:000003` ≡ `3.40.630.10:FF:000027` (containment=1.0, jaccard=1.0, intersection=10/10)

**Rationale:** One FunFam should be removed to eliminate redundancy. The 70% containment to GO:1990845 likely reflects appropriate use of more specific thermogenesis terms, not inaccuracy.

---

### ARBA00026249: Thioredoxin-Disulfide Reductase - **NO CHANGES**

**Assessment:** MODIFY (unchanged)
- `parsimony.assessment`: ACCEPTABLE (unchanged)

**Notes:**
- CS1 AND logic is CORRECT here: IPR005982 is a perfect subset of other domains (all 65 proteins have all 3 domains)
- CS3 provides unique coverage (~17-18 proteins with ZERO overlap with IPR005982)
- CS1/CS2 may be redundant if InterPro2GO covers IPR005982 → GO:0004791 (needs verification)

---

### ARBA00085883: Proteoglycan Catabolic Process - **NO CHANGES**

**Assessment:** MODIFY (unchanged)
- `parsimony.assessment`: REDUNDANT (unchanged - already correct)

**Notes:**
- 3-way perfect redundancy correctly identified: `2.60.40.10:FF:001526` ≡ `2.60.40.1500:FF:000001` ≡ `3.20.20.80:FF:000059`
- All three are identical 3-protein sets

---

## Validation

All 4 files validated successfully against the schema:

```bash
just rules-validate rules/arba/ARBA00047244/ARBA00047244-review.yaml \
                   rules/arba/ARBA00089174/ARBA00089174-review.yaml \
                   rules/arba/ARBA00026249/ARBA00026249-review.yaml \
                   rules/arba/ARBA00085883/ARBA00085883-review.yaml
```

**Result:** ✓ All 4 review(s) valid

---

## Key Methodological Lessons

### 1. AND Logic Requires High Overlap

**Rule of Thumb:** If condition set uses AND logic, conditions should have >50% pairwise overlap. Lower overlap indicates logical error (false negatives).

**Exception:** When one condition is a perfect subset of all others (like ARBA00026249 CS1), AND logic works but may be redundant.

### 2. Low Containment ≠ Inaccuracy

Containment to GO term shows *direct* annotation frequency. Low containment may indicate:
- **Good**: Proteins use more specific child terms (desired)
- **Neutral**: Proteins use parent terms or different aspects
- **Bad**: Missing annotations (least common)

Check biological context before concluding low containment is a problem.

### 3. Perfect Redundancy (containment=1.0, jaccard=1.0) = Remove One

When `entries` shows EQUIV relationship with perfect overlap, one condition adds no value and creates computational overhead. Always remove.

### 4. Subsetting (A ⊆ B with containment=1.0)

If A is perfect subset of B:
- **With AND logic**: Only get A's proteins (B's exclusive proteins lost) - May be intentional for specificity or may be error
- **With OR logic**: Get all B's proteins (A is redundant) - A can be removed

Check if subsetting is intentional (increasing specificity) or accidental (losing coverage).

---

## References

- rules/CORRECTED_ASSESSMENTS.md - Detailed corrected assessments
- rules/CRITICAL_FINDINGS_FROM_ENTRIES_ANALYSIS.md - Detailed analysis of ARBA00047244 AND logic error
- rules/RULE_RE-REVIEW_ANALYSIS.md - Initial re-review using `entries` field
