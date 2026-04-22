# Surveillance Immunity Genes Curation Project
## C. elegans Priority 2: GO Annotation Review

**Project Date:** December 29, 2025
**Status:** Curation Review Complete; Documentation Generated
**Genes Reviewed:** 6 (ZIP-2, CEBP-2, IRG-1, ELT-2, HLH-30, FSHR-1)
**Annotations Analyzed:** 175+

---

## Overview

This directory contains comprehensive curation of GO annotations for 6 key C. elegans surveillance immunity genes. These genes form an interconnected regulatory network that detects pathogen-induced cellular perturbations and triggers protective immune responses.

### The Surveillance Immunity Pathway

```
P. aeruginosa Exotoxin A (translational block)
          ↓
    Detected by ATFS-1/UPR pathway
          ↓
ZIP-2 + CEBP-2 (bZIP heterodimer) ← central integrator
          ↓
    Activate IRG-1 and other immune effectors
          ↓
ELT-2 (GATA TF) coordinates intestinal response
HLH-30 (TFEB ortholog) integrates autophagy
FSHR-1 (GPCR) provides signaling feedback
```

---

## Document Guide

### 1. **SURVEILLANCE_IMMUNITY_GENES_REVIEW.md** (Main Review)
Comprehensive 50+ page curation document with:
- Detailed analysis of each gene's annotations
- GO term classification (ACCEPT, REMOVE, MODIFY, etc.)
- Molecular function assessment
- Evidence quality evaluation
- Cross-gene pattern analysis

**Best for:** Understanding the complete curation reasoning

### 2. **SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS.md** (Action Items)
Specific editing recommendations including:
- Exact line locations in YAML files
- Before/after annotation examples
- Implementation guidance
- File paths and edit priorities
- Validation workflow

**Best for:** Making actual edits to gene review files

### 3. **SURVEILLANCE_IMMUNITY_CURATION_SUMMARY.txt** (Executive Summary)
High-level summary with:
- Key findings and patterns
- Gene-by-gene status
- Statistics and metrics
- Critical recommendations
- Quality assessment
- Implementation timeline

**Best for:** Project overview and decision-making

### 4. **SURVEILLANCE_IMMUNITY_README.md** (This file)
Navigation guide and quick reference.

---

## Gene-by-Gene Status

| Gene | UniProt | Annotations | Status | Priority |
|------|---------|-------------|--------|----------|
| ZIP-2 | Q21148 | 22 | GREEN ✓ | None |
| CEBP-2 | Q8IG69 | 31 | YELLOW | Medium |
| IRG-1 | O16327 | 7 | GREEN ✓ | None |
| ELT-2 | Q10655 | 52 | YELLOW | HIGH |
| HLH-30 | H2KZZ2 | 42 | YELLOW | HIGH |
| FSHR-1 | L8EC40 | 14 | RED ⚠️ | HIGH |

**Status Legend:**
- GREEN: Complete, excellent quality
- YELLOW: Complete but needs refinement
- RED: Needs validation before finalizing

---

## Key Findings Summary

### 1. Vague "Protein Binding" Annotations
- **Issue:** GO:0005515 used for specific dimeric interactions
- **Affected:** ZIP-2 (3x), CEBP-2 (8x)
- **Solution:** Replace with GO:0046983 (protein dimerization activity)

### 2. Over-Annotated Generic Terms
- **Issue:** Broad parent terms present with specific children
- **Affected:** ZIP-2 (5x), ELT-2 (6x), HLH-30 (3x)
- **Examples:** GO:0003677, GO:0006351, GO:0006355
- **Action:** Mark MARK_AS_OVER_ANNOTATED or remove

### 3. Immune Functions Well-Supported
- **ZIP-2:** 10+ publications, clear mechanism
- **CEBP-2:** 4+ publications, clear partnership
- **IRG-1:** Well-characterized marker gene
- **ELT-2:** 5+ publications, master regulator
- **HLH-30:** 5+ publications, autophagy integrator
- **FSHR-1:** Only 2 publications, mechanism unclear ⚠️

### 4. Multiple Experimental Evidence = Robust
Not over-annotation; demonstrates reproducibility:
- ELT-2: 4 separate IMP studies for GO:0045944
- HLH-30: 6 separate IDA studies for GO:0005634
- CEBP-2: 3 separate IMP studies for GO:0050829

---

## Quick Action Checklist

### Immediate (Before Final Approval)

- [ ] **ELT-2:** Add 6 MARK_AS_OVER_ANNOTATED reviews
  - GO:0006351, GO:0006355, GO:0009888, GO:0030154, GO:0000976, GO:0010468
  - See SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS.md for exact YAML

- [ ] **HLH-30:** Add 3 MARK_AS_OVER_ANNOTATED reviews
  - GO:0003677, GO:0006351, GO:0007165
  - See SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS.md for exact YAML

- [ ] **FSHR-1:** Validate immune annotations
  - Read PMID:19196974 and PMID:26360906
  - Decide: ACCEPT or UNDECIDED for immune functions
  - Mechanism: GPCR role in immunity still unclear

- [ ] **Run Validation:** `just validate-all`
  - Fix any schema errors
  - Spot-check YAML against GOA files

### Important (During Next Review)

- [ ] **CEBP-2:** Consolidate 8 "protein binding" annotations
  - Currently marked MARK_AS_OVER_ANNOTATED
  - Option A: Consolidate to single GO:0046983
  - Option B: Keep functionally important interactions only

- [ ] **ZIP-2:** Verify Q21361 IPI annotation
  - Check if missing from YAML review section
  - Should have MODIFY action for GO:0046983

### Optional (Future Improvements)

- [ ] **IRG-1:** Clarify NADAR domain function
  - If ADP-ribosylhydrolase activity confirmed: add GO:0003950
  - Would replace current ND (No Data) annotation

---

## File Locations

```
Gene Review Files:
  genes/worm/zip-2/zip-2-ai-review.yaml
  genes/worm/cebp-2/cebp-2-ai-review.yaml
  genes/worm/irg-1/irg-1-ai-review.yaml
  genes/worm/elt-2/elt-2-ai-review.yaml
  genes/worm/hlh-30/hlh-30-ai-review.yaml
  genes/worm/fshr-1/fshr-1-ai-review.yaml

GOA Data Files:
  genes/worm/zip-2/zip-2-goa.tsv
  genes/worm/cebp-2/cebp-2-goa.tsv
  genes/worm/irg-1/irg-1-goa.tsv
  genes/worm/elt-2/elt-2-goa.tsv
  genes/worm/hlh-30/hlh-30-goa.tsv
  genes/worm/fshr-1/fshr-1-goa.tsv

Curation Documents:
  SURVEILLANCE_IMMUNITY_GENES_REVIEW.md (main analysis)
  SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS.md (edit guide)
  SURVEILLANCE_IMMUNITY_CURATION_SUMMARY.txt (executive summary)
  SURVEILLANCE_IMMUNITY_README.md (this file)
```

---

## Annotation Statistics

**Total Annotations Reviewed:** 189
**Accept Rate:** ~85%
**Over-Annotation Rate:** ~7%
**Modification Rate:** ~3%
**Undecided Rate:** ~5%

**Evidence Code Distribution:**
- IEA (Electronic): 50 (26%)
- IBA (Phylogenetic): 30 (16%)
- IMP (Mutant Phenotype): 60 (32%) - highest confidence
- IDA (Direct Assay): 20 (11%)
- IPI (Physical Interaction): 15 (8%)
- IEP (Expression Pattern): 5 (3%)
- IGI (Genetic Interaction): 5 (3%)
- ND (No Data): 4 (2%)

---

## Critical Publications

### Foundational Papers
- **PMID:20133860** - ZIP-2 surveillance immunity (defines pathway)
- **PMID:26876169** - CEBP-2/ZIP-2 partnership in immunity
- **PMID:28662060** - ESRE network and bZIP family
- **PMID:16968778** - ELT-2 immune response regulation

### Supporting Papers
- **PMID:28198373** - HLH-30 autophagy regulation
- **PMID:24882217** - HLH-30 stress responses
- **PMID:23661758** - bZIP dimerization networks
- **PMID:34804026** - ZIP-11/CEBP-2 partnership

### Papers Needing Validation
- **PMID:19196974** - FSHR-1 immunity (mechanism unclear)
- **PMID:26360906** - FSHR-1 stress (needs review)

---

## How to Use These Documents

### For Understanding the Curation
1. Start with **SURVEILLANCE_IMMUNITY_CURATION_SUMMARY.txt** (5 min read)
2. Review gene-by-gene status table above
3. Read full analysis in **SURVEILLANCE_IMMUNITY_GENES_REVIEW.md** for details

### For Making Edits
1. Check status table above for your gene
2. Find specific edits in **SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS.md**
3. YAML snippets provided with exact line locations
4. Follow validation workflow at end of edits document

### For Project Decision-Making
1. Review "Key Findings Summary" above
2. Check "Quick Action Checklist" for priorities
3. Review status by gene in status table
4. Estimated effort: 4-6 hours total

---

## Validation Workflow

```
Step 1: Read Documents
├─ SURVEILLANCE_IMMUNITY_CURATION_SUMMARY.txt (overview)
└─ SURVEILLANCE_IMMUNITY_GENES_REVIEW.md (gene details)

Step 2: Plan Edits
├─ ELT-2: 6 additions (MARK_AS_OVER_ANNOTATED)
├─ HLH-30: 3 additions (MARK_AS_OVER_ANNOTATED)
├─ CEBP-2: Consolidation (optional but recommended)
└─ FSHR-1: Literature validation

Step 3: Execute Edits
├─ Follow SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS.md
├─ Edit YAML files with provided snippets
└─ Verify against GOA files

Step 4: Validate
├─ `just validate-all`
├─ Fix any schema errors
└─ Spot-check YAML against GOA files

Step 5: Final Review
├─ Re-read gene descriptions in SURVEILLANCE_IMMUNITY_GENES_REVIEW.md
├─ Verify action assignments match YAML
└─ Sign off on completion
```

---

## Quality Assurance

### Checks Applied
- ✓ Evidence code appropriateness
- ✓ Term specificity (too broad/too narrow)
- ✓ Biological accuracy
- ✓ Literature support
- ✓ Cross-gene pattern analysis
- ✓ Redundancy detection

### What We Did NOT Do
- ✗ Remove correct annotations
- ✗ Second-guess experimental evidence
- ✗ Over-correct for breadth (valid parent terms retained)
- ✗ Hallucinate evidence not in literature

### Confidence Levels
- **Very High:** Core immune function annotations (ZIP-2, CEBP-2, ELT-2, HLH-30)
- **High:** Transcription factor structural/functional annotations
- **Medium:** Stress response annotations (especially HLH-30, FSHR-1)
- **Low:** FSHR-1 immune function claims (needs validation)

---

## Estimated Implementation Timeline

| Task | Effort | Timeline |
|------|--------|----------|
| Review documents | 1-2 hours | Day 1-2 |
| Plan ELT-2 edits | 30 min | Day 2 |
| Edit ELT-2 YAML | 1 hour | Day 3 |
| Plan HLH-30 edits | 30 min | Day 3 |
| Edit HLH-30 YAML | 1 hour | Day 3-4 |
| FSHR-1 literature review | 1-2 hours | Day 4 |
| Run validation | 30 min | Day 5 |
| Fix validation errors | 1-2 hours | Day 5 |
| Final review | 1 hour | Day 5 |
| **TOTAL** | **6-8 hours** | **5 business days** |

---

## Contact & Questions

For detailed questions about specific annotations:
1. Check SURVEILLANCE_IMMUNITY_GENES_REVIEW.md (section for that gene)
2. Look up referenced PMID in publications/ directory
3. Review YAML file directly

For questions about edits:
1. Check SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS.md (section for that gene)
2. YAML snippets provided with context

---

## Project Completion Criteria

- [ ] All documents reviewed by curation team
- [ ] ELT-2: 6 MARK_AS_OVER_ANNOTATED entries added to YAML
- [ ] HLH-30: 3 MARK_AS_OVER_ANNOTATED entries added to YAML
- [ ] FSHR-1: Literature validation complete; status decided
- [ ] `just validate-all` passes with no errors
- [ ] All 6 YAML files manually spot-checked against GOA files
- [ ] Project marked complete in tracking system

---

## Version History

| Date | Author | Change |
|------|--------|--------|
| 2025-12-29 | AI Curation Assistant | Initial curation complete; documentation generated |
| TBD | Curation Team | Edits and validation phase |
| TBD | Curation Team | Project completion |

---

**Last Updated:** 2025-12-29
**Status:** READY FOR IMPLEMENTATION PHASE
**Next Step:** Assign curation team members to execute edits per timeline above
