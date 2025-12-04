# Corrected Rule Assessments Based on `entries` Analysis
**Date**: 2025-12-01

## Summary of Changes

| Rule | Old Action | New Action | Old Parsimony | New Parsimony | Key Issue |
|------|-----------|-----------|---------------|---------------|-----------|
| ARBA00047244 | MODIFY | REJECT | ACCEPTABLE | UNACCEPTABLE | AND logic with low overlap = fatal error |
| ARBA00089174 | MODIFY | MODIFY | ACCEPTABLE | REDUNDANT | Perfect redundancy in FunFams |
| ARBA00026249 | MODIFY | MODIFY | ACCEPTABLE | ACCEPTABLE | CS3 provides unique coverage, but InterPro2GO may cover CS1 |
| ARBA00085883 | MODIFY | MODIFY | REDUNDANT | REDUNDANT | 3-way perfect redundancy confirmed |

---

## ARBA00047244: Amide Catabolic Process - REJECT

### Critical Errors Identified

1. **CS1 (Urease) - Fatal AND Logic Error**
   - Requires all 3 InterPro domains via AND logic
   - But pairwise overlaps are only 10-29 proteins (~4-10%)
   - Triple intersection ≤ 10 proteins out of 851 total
   - Each domain individually has 100% containment to GO:0043605
   - **This is a 99% false negative rate**

2. **CS2 (PM20D1) - Perfect Redundancy**
   - `1.10.150.900:FF:000003` ≡ `3.40.630.10:FF:000027` (10/10 proteins identical)
   - One FunFam should be removed

3. **CS3 (Ureide enzymes) - Subsetting Issue**
   - `3.30.70.360:FF:000012` (UAH, 2 proteins) is 100% subset of `3.40.630.10:FF:000044` (AAH, 7 proteins)
   - With AND logic, rule only captures 2 proteins, missing 5 AAH-only proteins

### Corrected Assessment

**action: REJECT**

**action_rationale**: Rule has fundamental logical errors that invalidate it:

1. CS1 uses AND logic requiring 3 urease domains that have LOW overlap (4-10%), creating a triple intersection of ≤10 proteins when there are 851 total urease proteins. This is a 99% false negative rate. Each domain individually predicts GO:0043605 with 100% containment, proving each is sufficient and AND logic is incorrect.

2. CS2 contains perfect redundancy - two PM20D1 FunFams with identical 10-protein sets.

3. CS3 uses AND logic with a perfect subset (UAH ⊆ AAH), missing 5 AAH-only proteins.

Additionally, PM20D1's primary biological role is thermogenic lipid signaling, not nitrogen catabolism - the 70% containment to GO:0043605 reflects that 30% are correctly annotated to more specific metabolic/thermogenic terms.

**parsimony.assessment: UNACCEPTABLE**

**parsimony.notes**: The rule's AND logic creates massive false negatives. CS1 should use OR logic or be split into 3 separate condition sets. CS2 has redundant FunFams. CS3's subsetting means 5 proteins are excluded. The rule groups mechanistically diverse enzymes under overly broad GO term, obscuring biological specificity.

---

## ARBA00089174: Adaptive Thermogenesis - MODIFY

### Issues Identified

1. **Perfect Redundancy in CS (likely CS1 or CS2)**
   - `1.10.150.900:FF:000003` ≡ `3.40.630.10:FF:000027` (10/10 proteins identical)
   - **These are the SAME PM20D1 FunFams as in ARBA00047244!**
   - One should be removed

2. **Moderate-Low GO Term Containment**
   - Most entries show 53-70% containment to GO:1990845
   - This likely reflects correct annotation to parent/child thermogenesis terms
   - NOT necessarily an accuracy problem

### Corrected Assessment

**action: MODIFY** (unchanged)

**action_rationale**: Remove one of the redundant PM20D1 FunFams (either `1.10.150.900:FF:000003` or `3.40.630.10:FF:000027`). The moderate containment values (53-70%) may reflect appropriate use of more general or specific thermogenesis terms and should be investigated before concluding there's an accuracy problem.

**parsimony.assessment: REDUNDANT** (changed from ACCEPTABLE)

**parsimony.notes**: Rule contains perfect redundancy between two PM20D1 FunFams with identical 10-protein sets. One FunFam should be removed to eliminate redundancy.

---

## ARBA00026249: Thioredoxin-Disulfide Reductase - MODIFY (Check InterPro2GO)

### Issues Identified

1. **CS1 May Be Redundant with InterPro2GO**
   - CS1 uses AND logic requiring 3 domains
   - IPR005982 is 100% subset of IPR008255 and IPR023753 (all 65 proteins have all 3)
   - **The AND logic is correct here** (unlike ARBA00047244) because it achieves specificity
   - However, IPR005982 alone is sufficient (containment=1.0)
   - **If InterPro2GO already has IPR005982 → GO:0004791, CS1 is redundant**

2. **CS2 May Be Redundant**
   - Notes claim CS2 provides zero additional coverage
   - All 18 CS2 proteins also have CS1 signatures

3. **CS3 Provides Unique Coverage**
   - FunFams `3.30.390.30:FF:000004` and `3.50.50.60:FF:000190` have ZERO overlap with IPR005982
   - Captures ~17-18 unique proteins
   - Both show 100% containment to GO:0004791
   - **CS3 is valuable**

### Corrected Assessment

**action: MODIFY** (unchanged)

**action_rationale**: CS1 may be redundant if IPR005982 → GO:0004791 mapping exists in InterPro2GO (needs verification). CS2 appears redundant with CS1. CS3 provides valuable unique coverage of 17-18 proteins lacking InterPro domain but with FunFam evidence. Recommend: (1) Check InterPro2GO for IPR005982 mapping, (2) Remove CS2 if redundant, (3) Keep CS3, (4) Possibly simplify CS1 to IPR005982 alone.

**parsimony.assessment: ACCEPTABLE** (unchanged, but contingent on InterPro2GO check)

**parsimony.notes**: CS1's AND logic is appropriate here (unlike ARBA00047244) because IPR005982 is a perfect subset of the other domains, so the intersection equals IPR005982 alone. However, the two additional domains provide no additional specificity. CS3 provides genuine unique coverage. CS2 is redundant.

---

## ARBA00085883: Proteoglycan Catabolic Process - MODIFY

### Issues Identified

1. **3-Way Perfect Redundancy**
   - `2.60.40.10:FF:001526` ≡ `2.60.40.1500:FF:000001` ≡ `3.20.20.80:FF:000059`
   - All three are identical 3-protein sets
   - Two of these should be removed

2. **Variable GO Term Containment**
   - Ranges from 30% to 100%
   - Entries with 100%: The three redundant FunFams (3/3 proteins each)
   - Entries with lower containment may use more specific terms

### Corrected Assessment

**action: MODIFY** (unchanged)

**action_rationale**: Remove two of the three perfectly redundant FunFams (`2.60.40.10:FF:001526`, `2.60.40.1500:FF:000001`, `3.20.20.80:FF:000059`). Keep only one. Investigate whether low-containment entries (30-50%) are using more specific proteoglycan catabolic terms or represent genuine annotation gaps.

**parsimony.assessment: REDUNDANT** (unchanged - this was already correct)

**parsimony.notes**: Rule contains 3-way perfect redundancy where three FunFams represent identical 3-protein sets. This is excessive redundancy that should be eliminated by removing two of the three conditions.

---

## Key Methodological Lessons

### 1. AND Logic Requires High Overlap

**Rule of Thumb**: If condition set uses AND logic, conditions should have >50% pairwise overlap. Lower overlap indicates:
- Logical error (false negatives)
- Conditions from different contexts being inappropriately combined
- Need to switch to OR logic or separate condition sets

**Exception**: When one condition is a perfect subset of all others (like ARBA00026249 CS1), AND logic works but may be redundant.

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
- Check if subsetting is intentional (increasing specificity) or accidental (losing coverage)

---

## Implementation Notes

The following fields need to be updated in the YAML files:

### ARBA00047244
- `action`: "MODIFY" → "REJECT"
- `parsimony.assessment`: "ACCEPTABLE" → "UNACCEPTABLE"
- `action_rationale`: Replace with new text emphasizing fatal AND logic error
- `parsimony.notes`: Replace with new text explaining 99% false negative rate

### ARBA00089174
- `parsimony.assessment`: "ACCEPTABLE" → "REDUNDANT"
- `parsimony.notes`: Add text about PM20D1 FunFam redundancy

### ARBA00026249
- No changes to assessment values, but add note about needing InterPro2GO verification

### ARBA00085883
- No changes needed (already correctly assessed as REDUNDANT)

