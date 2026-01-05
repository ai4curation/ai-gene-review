# TOR1 Gene Review - Complete Curation Package

## Overview
Comprehensive GO annotation curation review for yeast TOR1 (Serine/threonine-protein kinase TOR1, UniProt P35169), a master regulator of cell growth and nutrient sensing in response to nitrogen, carbon, and amino acid availability.

## Files in This Directory

### Core Review Files
- **TOR1-ai-review.yaml** - Main reviewed annotation file (VALIDATED)
  - 67 GO annotations with detailed curation actions
  - 3 core molecular functions identified
  - Evidence-based justification for all actions

### Summary and Analysis Documents
- **TOR1-REVIEW-COMPLETE.md** - Comprehensive final report
  - Executive summary of curation results
  - Detailed findings by functional category
  - Evidence quality assessment
  - Literature references
  - Recommendations for further annotation

- **TOR1-CURATION-SUMMARY.md** - Detailed analysis table
  - Annotation breakdown by evidence code
  - Action distribution (ACCEPT, NON-CORE, OVER-ANNOTATED)
  - Specific rationale for each curation decision
  - Reference mapping

- **INDEX.md** - This file

### Reference Materials
- **TOR1-uniprot.txt** - UniProt record (official source)
- **TOR1-goa.tsv** - Original GOA annotations
- **generate_tor1_reviews.py** - Script documenting curation logic
- **update_tor1_reviews.py** - Script used to apply reviews

## Quick Reference

### Curation Statistics
| Category | Count | Percent |
|----------|-------|---------|
| ACCEPT | 52 | 78% |
| KEEP_AS_NON_CORE | 9 | 13% |
| MARK_AS_OVER_ANNOTATED | 6 | 9% |
| **TOTAL** | **67** | **100%** |

### Evidence Code Distribution
- IEA: 16 (Electronic)
- IDA: 14 (Direct Assay)
- IMP: 13 (Mutant Phenotype)
- IPI: 7 (Protein Interaction)
- IBA: 6 (Phylogenetic)
- IGI: 5 (Genetic Interaction)
- NAS: 4 (Non-traceable)
- EXP: 1 (Experimental)
- HDA: 1 (Homology)

### Core Functions
1. **Protein serine/threonine kinase activity** (GO:0004674)
2. **ATP binding** (GO:0005524)
3. **Protein-containing complex binding** (GO:0044877)

## Key Findings

### ACCEPT Annotations (52 total)

**Master Regulatory Pathways**
- TORC1 signaling (GO:0038202, GO:0031929)
- TORC1 complex membership (GO:0031931)
- Nutrient sensing and response

**Critical Growth Control Functions**
- Negative regulation of autophagy (GO:0016242, GO:0010507)
- Ribosome biogenesis (GO:0042254)
- Translational initiation (GO:0006413)
- Cell growth regulation (GO:0001558)
- Cell cycle regulation (GO:0051726)

**Subcellular Localizations** (8 locations)
- Nucleus, cytoplasm, vacuolar/plasma membranes, endosome, Golgi

### KEEP_AS_NON_CORE Annotations (9 total)

**Peripheral Stress Response and Metabolic Outputs**
- ER stress response, oxidative stress, heat response
- DNA damage response
- Cell wall organization, sphingolipid biosynthesis
- snRNA pseudouridylation
- Mitochondrial retrograde signaling

### MARK_AS_OVER_ANNOTATED Annotations (6 total)

**Generic Protein Binding Terms**
- GO:0005515 (protein binding) with multiple IPI references
- Recommendation: Consolidate into GO:0031931 (TORC1 complex) and GO:0044877 (complex binding)

## How to Use This Review

### For GO Annotation Updates
1. Read **TOR1-ai-review.yaml** for the structured curation data
2. Review **TOR1-REVIEW-COMPLETE.md** for evidence-based justification
3. Check specific annotations in **TOR1-CURATION-SUMMARY.md** for detailed rationale

### For Reference Literature
See **TOR1-REVIEW-COMPLETE.md** Literature References section for:
- PMID:12408816 - TORC1/TORC2 discovery
- PMID:9461583 - Autophagy control
- PMID:8741837 - Translation and G1 control
- And 7 additional key references

### For Further Research
Recommended research areas for annotation enhancement:
1. Substrate-specific phosphorylation terms (Tap42, Sch9, Ypk3, S6)
2. Nutrient-specific sensing pathways (nitrogen, carbon, amino acids)
3. Complex composition refinement
4. Consolidation of generic protein-binding annotations

## Validation Status

✓ **PASSED** - All 67 annotations reviewed and validated
- Schema validation: SUCCESS
- Evidence quality: HIGH (multiple evidence codes per function)
- Completeness: COMPREHENSIVE (all annotations addressed)

## Generation Information

- **Generated**: December 31, 2025
- **Organism**: *Saccharomyces cerevisiae* (strain ATCC 204508 / S288c)
- **Gene**: TOR1 (Target of Rapamycin 1)
- **UniProt ID**: P35169
- **Protein Size**: 2470 amino acids
- **EC Number**: 2.7.11.1 (Serine/threonine kinase)

---

For questions about this curation, see the detailed analysis documents or original publication references cited throughout.
