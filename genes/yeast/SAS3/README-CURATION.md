# SAS3 Gene Annotation Curation Review

## Overview
Comprehensive curation of 38 GO annotations (57 GOA entries) for yeast SAS3, the catalytic subunit of the NuA3 histone acetyltransferase complex.

## Key Findings

### Critical Discovery: Substrate Specificity Verification
- **Substrate:** Histone H3 lysine 14 (H3K14) - NOT H3K9 as sometimes confused with other HATs
- **Evidence:** UniProt function field, PMID:10817755, PMID:17157260, PMID:25104842
- **In vitro:** Also acetylates free histones H3 and H4 (PMID:10600516)

### Complex Organization: Two Functionally Distinct Forms
SAS3 is the catalytic subunit of NuA3, which exists in two forms:

**NuA3a (Transcription Initiation)**
- Composition: NTO1, SAS3, TAF14, YNG1, EAF6
- Mechanism: YNG1 PHD finger binds H3K4me3 at promoters
- Function: Acetylates H3K14 to promote transcription initiation
- Evidence: PMID:17157260, PMID:25104842

**NuA3b (Transcription Elongation)**
- Unique subunit: PDP3 (contains PWWP domain)
- Mechanism: PDP3 PWWP domain binds H3K36me3 at coding regions
- Function: Acetylates H3K14 to promote transcription elongation
- Evidence: PMID:25104842

---

## Curation Decisions Summary

### Annotations ACCEPTED (48/57 entries representing 31/38 unique GO terms)
Well-supported annotations with strong evidence:

| Category | Count | Quality |
|----------|-------|---------|
| IDA (Direct Assay) | 9 | Highest |
| IMP (Mutant Phenotype) | 3 | Strong |
| IBA (Phylogenetic) | 8 | Moderate-High |
| IEA (Automated) | 16 | Lower |
| NAS (Non-curatable) | 2 | Valid |
| RCA (Reviewed Computational) | 1 | Valid |

**All core functions supported by multiple evidence lines**

### Annotations REMOVED (7 entries)
**GO:0005515 (protein binding) - IPI evidence code**

- Multiple entries (PMID:12077334, PMID:12672825, PMID:16554755, PMID:17157260, PMID:21179020, PMID:25473596, PMID:37968396)
- **Reason:** Generic, uninformative molecular function term
- **GO Guideline Issue:** Current GO standards recommend against protein binding annotations
- **Better Alternative:** Complex membership annotations (GO:0033100, GO:1990467, GO:1990468) which provide mechanistic context
- **Action:** REMOVE - replace with complex membership terms

### Annotations MARKED AS OVER-ANNOTATED (2 terms)
**GO:0006351 (DNA-templated transcription)**
- Too broad/mechanistically misleading
- SAS3 regulates but doesn't catalyze transcription directly
- **Recommendation:** MODIFY to GO:0006357 (regulation of transcription by RNA polymerase II)

**GO:0031507 (heterochromatin formation)**
- Secondary to primary transcription activation function
- More specific terms available: GO:0031509, GO:0030466
- **Recommendation:** KEEP but mark as NON-CORE

### Annotations MARKED AS NON-CORE (2 terms)
**GO:0000781 (chromosome, telomeric region)**
- Logically valid but too general
- Specific functions better annotated by GO:0031509, GO:0030466

**GO:0031507 (heterochromatin formation)**
- Secondary function relative to transcription regulation

---

## New Annotations to Add

### GO:0036408 - histone H3K14 acetyltransferase activity
- **Evidence Code:** IDA (Direct Assay)
- **References:** PMID:10817755, PMID:17157260
- **Justification:** Critical substrate-specific function that is well-documented in the literature but missing from current annotations. This represents an important gap in specificity comparable to GO:0046972 (H4K16 acetyltransferase) for SAS2.
- **Status:** Should be added as NEW annotation with IDA evidence

---

## SAS3 vs SAS2 Comparison

| Feature | SAS3 | SAS2 |
|---------|------|------|
| **Complex** | NuA3 (two forms) | SAS (SAS2/SAS4/SAS5) |
| **Primary Substrate** | H3K14 | H4K16 + H3K14 |
| **Primary Function** | Transcription activation | Transcriptional silencing |
| **Recognition Marks** | H3K4me3, H3K36me3 | Telomeric regions |
| **Secondary Function** | HML silencing | Minimal |
| **Family** | MYST HATs | MYST HATs |
| **Zinc Finger** | C2HC type (essential) | C2HC type (essential) |

**Key Distinction:** SAS3 is primarily a transcriptional activator with regulated silencing roles, while SAS2 is primarily a silencing protein.

---

## Literature Summary

### Primary Sources (Foundational)
- **PMID:10817755** (2000) - Discovery of SAS3 as NuA3 catalytic subunit; biochemical characterization
- **PMID:17157260** (2006) - NuA3a mechanism; H3K4me3-YNG1-H3K14ac pathway
- **PMID:25104842** (2014) - NuA3b discovery; H3K36me3 recognition; elongation function

### Supporting Sources
- PMID:11731479 - SAS complex silencing roles
- PMID:12077334 - YNG1 modulation of SAS3
- PMID:14562095 - Protein localization studies
- PMID:30358795 - Zinc proteome database
- PMID:16554755 - Global protein complex landscape
- PMID:21179020 - Chromatin-associated interactome
- PMID:25473596 - Comprehensive NuA3 complex analysis
- PMID:37968396 - Protein interactome architecture

---

## Files in This Review

| File | Purpose |
|------|---------|
| **README-CURATION.md** | This file - overview and summary |
| **SAS3-CURATION-SUMMARY.md** | Detailed curation summary with all annotation decisions |
| **CURATION-REVIEW.txt** | Quick reference - curation decisions by category |
| **SAS3-ai-review.yaml** | YAML annotation review (schema-compliant) |
| **SAS3-goa.tsv** | Original GOA file with all 57 annotations |
| **SAS3-uniprot.txt** | UniProt record (P34218) |

---

## Quality Metrics

| Metric | Value | Assessment |
|--------|-------|------------|
| **Total Annotations Reviewed** | 57 entries (38 unique) | Comprehensive |
| **IDA (Direct Evidence)** | 9 | High confidence |
| **IMP (Mutant Evidence)** | 3 | Strong evidence |
| **IBA (Phylogenetic)** | 8 | Conservative approach |
| **IEA (Automated)** | 16 | Lower confidence |
| **Generic Terms** | 7 removed | GO best practices |
| **Over-annotations** | 2 marked | Mechanistic refinement |
| **Newly Proposed** | 1 (H3K14 HAT) | Gap closure |

**Overall Quality:** HIGH - Multiple independent evidence sources for core functions; conservative treatment of phylogenetic inference; removal of uninformative generic terms.

---

## Recommendations for GO Curators

1. **Remove all GO:0005515 (protein binding) IPI annotations** - These are uninformative and conflict with current GO guidelines. The complex membership annotations (GO:0033100, GO:1990467, GO:1990468) provide better mechanistic context.

2. **Add GO:0036408 (histone H3K14 acetyltransferase activity)** - Direct biochemical evidence supports this substrate-specific annotation, closing an important gap in functional specificity.

3. **Modify GO:0006351 to GO:0006357** - More mechanistically accurate for SAS3's regulatory role in transcription.

4. **Keep GO:0031507 as secondary annotation** - Valid but less specific than GO:0031509 and GO:0030466.

---

## Review Metadata

- **Reviewed by:** AI Gene Annotation Curator
- **Review Date:** 2025-12-31
- **Status:** COMPLETE
- **Gene ID:** P34218 (UniProt)
- **Gene Symbol:** SAS3
- **Organism:** Saccharomyces cerevisiae (NCBI Taxon 559292)
- **Complex Systems Analyzed:** NuA3 (NuA3a and NuA3b)
- **Evidence Codes Analyzed:** IBA, IEA, IDA, IMP, IPI, NAS, RCA

---

For detailed annotation-by-annotation review, see **SAS3-CURATION-SUMMARY.md**
