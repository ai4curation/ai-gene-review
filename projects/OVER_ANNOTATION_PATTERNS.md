# Over-Annotation Patterns Project

## Overview

This project documents systematic patterns of over-annotation discovered through AI-assisted gene review. Over-annotation occurs when GO terms are assigned that are technically correct but provide minimal functional insight, or when terms are too broad/generic to be useful for understanding gene function.

These patterns emerge from multiple sources:
- High-throughput screens that generate generic annotations
- Domain-based IEA annotations that don't reflect actual activity
- IBA annotations that over-generalize from distantly related proteins
- Keyword-based mappings that assign parent terms unnecessarily

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Categories of Over-Annotation

### 1. Generic "Protein Binding" (GO:0005515)

**The Problem**: High-throughput interactome studies generate thousands of IPI annotations to "protein binding" that provide no functional information.

**Examples from Reviews**:
- **PHYKPL**: 4 protein binding annotations from HTP screens showing interactions with POT1, USO1, VAC14, LNX2 - none related to its metabolic function
- **UBA7**: 6 protein binding annotations from interactome studies - UBA7 obviously binds proteins (ISG15, UBE2L6) but the generic term adds nothing
- **Epe1**: Protein binding annotation when specific HP1/Swi6 binding and SAGA complex binding are more informative

**Recommended Action**: REMOVE generic protein binding when more specific functional annotations exist or when interactions are from HTP screens without validation.

### 2. Overly Broad Enzymatic Terms

**The Problem**: Generic enzymatic terms (hydrolase activity, oxidoreductase activity, ligase activity) assigned when more specific terms exist.

**Examples**:
- **LPL1**: `GO:0016787` (hydrolase activity) when `GO:0102545` (phospholipase B activity) is more specific
- **Epe1**: `GO:0016491` (oxidoreductase activity) assigned despite protein lacking catalytic activity
- **UBA7**: `GO:0016874` (ligase activity) when `GO:0019782` (ISG15 activating enzyme activity) is specific

**Recommended Action**: REMOVE or MODIFY to more specific child terms.

### 3. Domain-Based Predictions Without Validation

**The Problem**: IEA annotations from domain presence (InterPro, Pfam) that don't reflect actual biochemical activity.

**Examples**:
- **Epe1**: JmjC domain → histone demethylase activity, dioxygenase activity, metal ion binding (ALL INCORRECT - pseudo-enzyme)
- **PHYKPL**: Aminotransferase domain → transaminase activity (INCORRECT - functions as phospho-lyase)

**Recommended Action**: REMOVE when biochemical evidence contradicts domain prediction.

### 4. Indirect Downstream Process Annotations

**The Problem**: Genes annotated to broad biological processes based on indirect effects rather than direct function.

**Pattern**: Gene affects X → X affects Y → Gene annotated to Y

**Examples**:
- Kinase that phosphorylates one transcription factor annotated to "regulation of cell proliferation"
- Enzyme in metabolic pathway annotated to disease process it indirectly affects

**Recommended Action**: Use more proximal process terms; annotate to direct function, not downstream consequences.

### 5. Duplicate IEA Annotations

**The Problem**: Multiple automated pipelines annotate the same term, creating redundancy.

**Examples**:
- **GND1**: Same term (`GO:0004616`) from both IBA and IEA sources
- **UBA7**: Cytoplasm annotation from IBA, IEA, and IDA sources

**Note**: This is less problematic as multiple evidence codes can provide confidence, but creates clutter.

### 6. Predicted Localization Conflicts

**The Problem**: Automated transmembrane predictions leading to incorrect membrane annotations.

**Examples**:
- **LPL1**: `GO:0016020` (membrane) from transmembrane prediction, but protein localizes to lipid droplets (monolayer, not bilayer membrane)

**Recommended Action**: REMOVE when experimental localization data contradicts prediction.

## Genes Exemplifying Patterns

| Gene | Species | Over-Annotation Pattern | Status |
|------|---------|------------------------|--------|
| PHYKPL | human | Protein binding, transaminase (wrong mechanism) | COMPLETE |
| UBA7 | human | Protein binding, generic ligase | COMPLETE |
| Epe1 | pombe | Domain-based demethylase (pseudo-enzyme) | COMPLETE |
| LPL1 | CANAL | Generic hydrolase, membrane localization | COMPLETE |

## Recommended Curation Principles

1. **Specificity over breadth**: Always prefer the most specific accurate term
2. **Remove uninformative annotations**: Generic protein binding from HTP screens
3. **Validate domain predictions**: Especially for enzymatic activity
4. **Distinguish direct vs. indirect**: Annotate to proximal function
5. **Consider pseudo-enzymes**: Domains don't guarantee activity

## Impact on Annotation Quality

These over-annotation patterns:
- Dilute the signal from informative annotations
- Create false impressions of functional understanding
- Complicate enrichment analyses
- Propagate through IBA to other species

---

# STATUS

## Documented Patterns
- [x] Generic protein binding
- [x] Overly broad enzymatic terms
- [x] Domain-based predictions without validation
- [x] Indirect downstream processes
- [x] Predicted localization conflicts

## Genes Analyzed
- [x] human/PHYKPL - transaminase vs phospho-lyase
- [x] human/UBA7 - protein binding from HTP, generic ligase
- [x] pombe/Epe1 - pseudo-demethylase
- [x] CANAL/LPL1 - hydrolase, membrane prediction

Last updated: 2026-01-22

# NOTES

## 2026-01-22

**Project Creation**

Documented systematic over-annotation patterns discovered through AI review.

**Key Insight**: The most common over-annotation is generic "protein binding" (GO:0005515) from high-throughput interactome studies. These annotations:
- Provide no functional information
- Often represent false positives or indirect interactions
- Should be removed when specific functional annotations exist

**Curation Recommendation**: Consider flagging or filtering HTP-derived protein binding annotations during curation review.
