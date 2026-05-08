# ARBA00027169 Manual Analysis

## Rule Summary
- **Rule ID**: ARBA00027169
- **GO Annotation**: GO:0120114 "Sm-like protein family complex"
- **Condition Sets**: 28 (exceeds analysis limit of 12)
- **Created**: 2021-10-20
- **Modified**: 2025-05-15

## Condition Set Breakdown

### InterPro-based Conditions (Sets 1-4)
1. **Set 1**: IPR001163 (Sm domain) + IPR010920 (LSM superfamily) + Taphrinomycotina
2. **Set 2**: IPR016487 (Lsm6/SmF) + IPR047575 (Sm domain) + Eukaryota  
3. **Set 3**: IPR027141 (LSm4/SmD1/SmD3) + Fungi
4. **Set 4**: IPR034105 (Lsm3) + IPR040002 (U6 snRNA Lsm3)

### CATH FunFam-based Conditions (Sets 5-28)
#### U1/U2 snRNP Components
- Set 5: U2 snRNP B'' + U1 snRNP A (Eukaryota)
- Set 19: U1 snRNP C (Mammalia)
- Set 20: U2 snRNP A (Craniata)

#### U5 snRNP Components  
- Sets 8-9: U5 snRNP helicases
- Set 21: U5 snRNP subunit 40

#### U6 snRNP/Lsm Components
- Set 6: Lsm3
- Set 7: Lsm6  
- Set 18: Lsm11 (Chordata)
- Set 22: Lsm4
- Set 25: Lsm5

#### Sm Proteins
- Set 16: SmD3 (Ascomycota)
- Set 17: Sm proteins (Rattus)
- Sets 23-26: SmG, SmD2, SmF

#### Splicing Factors
- Set 11: SF3B1 subunits
- Set 12: PRPF8 (multiple FunFams)
- Set 15: SF3A1
- Set 27: PRP24
- Set 29: DIB1

#### Problematic Inclusions
- Set 13: Translation elongation factor 2 + U5 component (Fungi) - **WRONG**
- Set 14: Various splicing factors
- Set 28: Hsh49p

## Major Issues Identified

### 1. Excessive Complexity
- 28 condition sets is far too many for a single rule
- Creates maintenance burden and unclear logic
- Violates parsimony principles

### 2. Taxonomic Inconsistency
- Broad eukaryotic scope mixed with very specific restrictions
- Some conditions limited to Mammalia, Chordata, Craniata
- Others specific to fungal groups (Ascomycota, Taphrinomycotina)
- One condition specific to Rattus genus

### 3. Functional Heterogeneity  
- Includes legitimate Sm/Lsm proteins
- Includes spliceosomal components without Sm domains
- Incorrectly includes translation elongation factor
- Mixes core snRNP components with auxiliary factors

### 4. GO Term Appropriateness
- GO:0120114 "Sm-like protein family complex" is cellular component
- Too broad for the diverse proteins captured
- Some proteins don't form complexes with Sm proteins

### 5. Domain Promiscuity Risk
- Sm domains appear in various contexts
- Rule may capture unrelated proteins with Sm-like domains
- Lack of additional constraints increases false positive risk

## Recommendations

### Primary Recommendation: REMOVE
This rule should be deprecated and replaced with multiple focused rules:

1. **Core Sm protein rule**: Classical Sm proteins (SmB/B', SmD1-3, SmE-G)
2. **Lsm protein rule**: Lsm1-8 proteins for U6 snRNP and mRNA decay
3. **U7-specific rule**: Lsm10/11 for histone mRNA processing
4. **Spliceosomal component rules**: Separate rules for different snRNP components

### Specific Issues to Address
1. Remove translation elongation factor condition (Set 13)
2. Establish consistent taxonomic scope
3. Use more specific GO terms where appropriate
4. Add negative conditions to exclude false positives

## Risk Assessment
- **False Positive Risk**: HIGH - overly broad conditions
- **False Negative Risk**: LOW - comprehensive coverage
- **Maintenance Risk**: VERY HIGH - too complex
- **Biological Accuracy**: MODERATE - mostly correct but includes wrong proteins