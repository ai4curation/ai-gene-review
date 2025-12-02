# Re-review Notes for ARBA00089180

## Summary
Rule predicts GO:1990858 (cellular response to lectin) - essentially same issues as ARBA00089176.

## Review Log

### 2024-12-02 - Initial Re-review

Review has action DEPRECATE with confidence 0.95.

### Near-Duplicate of ARBA00089176

This rule has the SAME fundamental problems:
- Same generic domains (kinases, p300)
- Same disjoint condition sets
- Same very low GO term coverage (3-40% containment)
- Same taxonomic issues (Primates/Catarrhini)

Only difference: GO:1990858 (cellular response to lectin) vs GO:1990840 (response to lectin)

### Literature Support: CONTRADICTED

Review correctly notes:
- "Rule conflates involvement in lectin signaling with direct participation in lectin response"
- p300/CBP interacts with ~400 proteins in diverse pathways
- Domain architecture cannot justify this annotation

### Why Higher Confidence Than ARBA00089176

Confidence 0.95 (vs 0.25 for ARBA00089176) because:
- Literature explicitly CONTRADICTS the rule logic
- Same fatal flaws, but even clearer evidence against

### Questions

1. Why do two nearly identical rules exist (ARBA00089176 and ARBA00089180)?
2. Should these be flagged as duplicates in a tracking system?

## Status: REVIEW APPROVED
The 0.95 confidence in DEPRECATE is justified. This is essentially a duplicate of ARBA00089176 with the same fatal flaws.
