# Enzyme Specificity Project

## Overview

This project tracks genes where GO annotations fail to capture the correct enzyme specificity - either:
1. **Too narrow**: Annotation to one substrate when enzyme has broader specificity
2. **Too broad**: Generic enzyme class when specific activity is known
3. **Wrong reaction**: Incorrect reaction type based on domain classification

Enzyme specificity is crucial for accurate functional annotation. Misannotated specificity can:
- Mislead metabolic pathway reconstruction
- Cause errors in drug target identification
- Propagate incorrect annotations via IBA

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Categories

### 1. Substrate Specificity Errors

**The Problem**: Enzyme annotated to specific substrate when it has broader or different specificity.

**Example - LPL1 (C. albicans)**:
- Annotated: `GO:0004622` (phosphatidylcholine lysophospholipase activity)
- Actual: Phospholipase B with three distinct activities:
  1. sn-1/sn-2 fatty acid ester hydrolase
  2. Lysophospholipase activity (on ALL glycerophospholipids, not just PC)
  3. Transacylase activity
- **Action**: MODIFY → `GO:0102545` (phospholipase B activity)

### 2. Reaction Mechanism Errors

**The Problem**: Wrong reaction type inferred from domain classification.

**Example - PHYKPL (human)**:
- Domain: Aminotransferase III family
- Annotated: `GO:0008483` (transaminase activity)
- Actual: Phospho-lyase (EC 4.2.3.134), NOT a transaminase
- Evidence: "Unlike AGXT2, AGXT2L1 and AGXT2L2 did not act as transaminases"
- **Action**: REMOVE transaminase; ADD `GO:0016838` (carbon-oxygen lyase activity, acting on phosphates)

### 3. Cofactor Specificity Errors

**The Problem**: Enzyme annotated with wrong cofactor preference.

**Examples**:
- NAD+ vs NADP+ dependent dehydrogenases
- PLP-dependent enzymes with different reaction types

### 4. Non-Enzymatic Homologs

**The Problem**: Enzymatic activity annotated to proteins that have lost catalytic function.

**Example - Epe1 (S. pombe)** (see CONTESTED_FUNCTION.md):
- Annotated: Histone demethylase, oxidoreductase, dioxygenase
- Actual: Pseudo-enzyme with degenerate active site
- **Action**: REMOVE all enzymatic annotations

## Featured Examples

### LPL1 (Candida albicans)

**UniProt**: Q5AMS2
**Species**: CANAL
**Status**: COMPLETE

**Specificity Issue**:
- `GO:0004622` (phosphatidylcholine lysophospholipase) - too narrow
- Enzyme acts on ALL glycerophospholipids, not just PC
- Has three distinct activities (hydrolase, lysophospholipase, transacylase)

**Also**: `GO:0047372` (monoacylglycerol lipase activity) marked KEEP_AS_NON_CORE
- Likely substrate promiscuity, not primary function

### PHYKPL (Homo sapiens)

**UniProt**: Q8IUZ5
**Species**: human
**Status**: COMPLETE

**Specificity Issue**:
- Classified in aminotransferase family → annotated with transaminase activity
- Biochemically demonstrated to be a phospho-lyase
- Different reaction mechanism entirely

**Proposed New Terms**:
- `5-phosphooxy-L-lysine phospho-lyase activity` - specific MF for PHYKPL
- `5-phosphohydroxy-L-lysine catabolic process` - specific BP

### GND1 (Candida albicans)

**UniProt**: A0A1D8PFS4
**Species**: CANAL
**Status**: INITIALIZED (annotations pending review)

**Notes**: 6-phosphogluconate dehydrogenase with interesting dual localization (cytosol and peroxisome via alternative splicing). Review needed for specificity annotations.

## Genes for Review

### Priority 1: Completed
| Gene | Species | Issue | Status |
|------|---------|-------|--------|
| LPL1 | CANAL | Substrate specificity too narrow | COMPLETE |
| PHYKPL | human | Wrong reaction mechanism | COMPLETE |

### Priority 2: Pending
| Gene | Species | Issue | Status |
|------|---------|-------|--------|
| GND1 | CANAL | Review pending | INITIALIZED |

## Curation Principles

1. **Verify substrate range**: Don't assume specificity from one characterized reaction
2. **Check reaction mechanism**: Domain family doesn't guarantee mechanism
3. **Distinguish promiscuity from core function**: Secondary activities → KEEP_AS_NON_CORE
4. **Propose specific terms**: When existing terms are too broad or narrow

---

# STATUS

## Completed Reviews
- [x] CANAL/LPL1 - Phospholipase B specificity
- [x] human/PHYKPL - Phospho-lyase vs transaminase

## Pending Reviews
- [ ] CANAL/GND1 - 6-phosphogluconate dehydrogenase

Last updated: 2026-01-22

# NOTES

## 2026-01-22

**Project Creation**

Created project to track enzyme specificity annotation issues.

**LPL1 Key Points**:
- Phospholipase B enzymes have three activities in one protein
- Current annotation (`GO:0004622`) captures only lysophospholipase on PC
- Better term: `GO:0102545` (phospholipase B activity)
- Also: `GO:0047372` (monoacylglycerol lipase) kept as non-core (likely promiscuous)

**PHYKPL Key Points**:
- Domain classification misleading (aminotransferase family)
- Biochemically: "did not act as transaminases"
- Functions as phospho-lyase (EC 4.2.3.134)
- Needs specific GO term for its reaction
