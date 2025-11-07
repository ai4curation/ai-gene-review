# xoxF1 Review Notes

## Gene Overview

**Gene**: xoxF1
**UniProt ID**: C5B120
**Organism**: Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1)
**Full Name**: Lanthanide-dependent methanol dehydrogenase
**EC**: 1.1.2.10

## Core Function Summary

XoxF1 is a **lanthanide-dependent methanol dehydrogenase** that catalyzes the oxidation of methanol to formaldehyde in the bacterial periplasm. This enzyme is fundamentally different from the calcium-dependent MxaFI methanol dehydrogenase because it:

1. **Requires lanthanides (La³⁺, Nd³⁺, Ce³⁺, Pr³⁺)** as essential cofactors - NOT calcium
2. Uses **pyrroloquinoline quinone (PQQ)** as its prosthetic group
3. Forms a **homodimer** structure
4. Localized to the **periplasm** (not membrane-bound)
5. Transfers electrons to **XoxG (cytochrome cL)** as the immediate electron acceptor
6. Part of the **xoxFGJ operon**

## Key Evidence from Literature

### PMID:23209751 - Nakagawa et al. 2012
- First demonstration of La³⁺-dependent methanol dehydrogenase activity
- Showed XoxF1 has catalytic role in methanol oxidation
- Purified enzyme showed ~15-fold higher activity than MxaFI under lanthanide conditions
- N-terminal sequencing confirmed signal peptide processing

### PMID:30862918 - Good et al. 2019
- Contrasting in vitro and in vivo methanol oxidation activities
- Kinetic characterization: Km = 44 μM for methanol (with La³⁺)
- XoxF1 can oxidize formaldehyde in vitro but this is not the primary in vivo function
- Highly upregulated in presence of lanthanides

### PMID:32366463 - Good et al. 2020
- Crystal structure with La³⁺ and PQQ
- Identified essential Asp-320 for metal coordination
- Mutation D320A eliminates activity and La³⁺ binding
- Shows enzyme is inactive with Ca²⁺ alone

## Critical Point: Calcium vs Lanthanide Binding

**VERY IMPORTANT**: The GO annotation "calcium ion binding" is INCORRECT for XoxF1.

From UniProt CC section:
> "Is inactive when binding Ca(2+) ions in the absence of La(3+)" [PMID:32366463]

XoxF1 specifically requires lanthanides. The diagnostic aspartate residue (Asp172 before the metal-coordinating Glu173) is unique to XoxF1-type enzymes and essential for lanthanide coordination, not calcium.

## Annotation Review Strategy

For each existing annotation, I will:
1. Evaluate correctness based on literature
2. Determine if it represents core function
3. Assign appropriate action (ACCEPT, REMOVE, MODIFY, etc.)
4. Provide supporting evidence with citations

## GO Annotation Review

### 1. GO:0003824 (catalytic activity)
- **Status**: CORRECT
- **Action**: ACCEPT
- **Rationale**: XoxF1 is an enzyme with well-characterized catalytic activity
- **Evidence**: IDA from kinetic studies [PMID:23209751, PMID:30862918, PMID:32366463]

### 2. GO:0005509 (calcium ion binding)
- **Status**: INCORRECT
- **Action**: REMOVE
- **Rationale**: XoxF1 binds LANTHANIDES, not calcium. In fact, it is INACTIVE with Ca²⁺ alone
- **Evidence**: "Is inactive when binding Ca(2+) ions in the absence of La(3+)" [PMID:32366463]
- **This is a clear misannotation** - likely from automated annotation not recognizing lanthanide specificity

### 3. GO:0015945 (methanol metabolic process)
- **Status**: CORRECT - CORE FUNCTION
- **Action**: ACCEPT
- **Rationale**: Primary biological role is methanol oxidation to formaldehyde
- **Evidence**: IDA, IGI [PMID:23209751, PMID:30862918]

### 4. GO:0016020 (membrane)
- **Status**: MISLEADING
- **Action**: REMOVE
- **Rationale**: XoxF1 is periplasmic, not membrane-bound. May loosely associate but primary localization is periplasm
- **Evidence**: Signal peptide directs to periplasm; immunoelectron microscopy shows periplasmic localization [PMID:23209751]

### 5. GO:0016491 (oxidoreductase activity)
- **Status**: CORRECT - CORE FUNCTION
- **Action**: ACCEPT
- **Rationale**: XoxF1 catalyzes oxidation-reduction reactions (methanol → formaldehyde)
- **Evidence**: IDA [PMID:23209751, PMID:30862918, PMID:32366463]

### 6. GO:0016614 (oxidoreductase activity, acting on CH-OH group of donors)
- **Status**: CORRECT - CORE FUNCTION
- **Action**: ACCEPT
- **Rationale**: Specifically oxidizes the CH-OH group of methanol
- **Evidence**: IDA [PMID:23209751, PMID:30862918]

### 7. GO:0030288 (outer membrane-bounded periplasmic space)
- **Status**: CORRECT
- **Action**: ACCEPT
- **Rationale**: Accurate description of periplasmic localization in Gram-negative bacteria
- **Evidence**: IDA from signal peptide analysis and immunolocalization [PMID:23209751]

### 8. GO:0042597 (periplasmic space)
- **Status**: CORRECT - PRIMARY LOCALIZATION
- **Action**: ACCEPT
- **Rationale**: Primary and most specific cellular component annotation
- **Evidence**: IDA [PMID:23209751, immunoelectron microscopy from deep research]

### 9. GO:0046872 (metal ion binding)
- **Status**: CORRECT but IMPRECISE
- **Action**: ACCEPT (but note need for more specific lanthanide term)
- **Rationale**: XoxF1 does bind metal ions - specifically lanthanides. This is technically correct but not specific enough. GO currently lacks specific lanthanide binding terms.
- **Evidence**: IDA from ICP-MS showing ~1 lanthanide per dimer [PMID:23209751, PMID:32366463]

### 10. GO:0070968 (pyrroloquinoline quinone binding)
- **Status**: CORRECT - ESSENTIAL COFACTOR
- **Action**: ACCEPT
- **Rationale**: PQQ is the prosthetic group essential for catalytic activity
- **Evidence**: IDA from crystal structure [PMID:32366463]

## Summary of Actions

- **ACCEPT**: 8 annotations (1, 3, 5, 6, 7, 8, 9, 10)
- **REMOVE**: 2 annotations (2, 4)

## Additional Terms to Consider Adding

Based on the literature, these terms might be appropriate:
- **GO:1990190** methanol dehydrogenase (cytochrome c) activity (if such a term exists - need to check)
- A specific **lanthanide ion binding** term (currently not in GO - would need to propose new term)
- **GO:0006118** electron transport (as secondary function through XoxG/cytochrome c)

## Proposed New GO Terms

The deep research document suggests these terms should be proposed:
1. **lanthanide-dependent methanol oxidation** (as BP term)
2. **lanthanide-dependent alcohol dehydrogenase activity** (as MF term)
3. **lanthanide ion binding** (as MF term)

These would more accurately capture the unique biology of XoxF1 and related enzymes.
