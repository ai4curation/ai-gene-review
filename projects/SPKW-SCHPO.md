# SPKW S. pombe (Schizosaccharomyces pombe) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

S. pombe is a well-curated model organism with extensive experimental annotations from PomBase. This makes it an ideal test case for identifying TRUE SPKW-unique annotations that are not subsumed by more specific experimental evidence.

## Query Methodology

Used closure-based query to find TRUE SPKW-unique annotations:
- An SPKW annotation to term X is NOT unique if there exists a non-SPKW annotation to term Y where Y is_a X
- This excludes cases where SPKW provides a broad term but experimental evidence exists for a specific child term

## Key Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| Naive SPKW-unique (gene-term pairs) | 7,221 |
| TRUE SPKW-unique (after closure filtering) | 1,963 |
| Reduction from closure filtering | 73% |

The 73% reduction demonstrates the importance of using closure-based queries. Most SPKW annotations to broad terms are subsumed by more specific experimental annotations to child terms.

## Identified Over-Annotation Pattern: Meiotic Cell Cycle

207 genes have TRUE SPKW-unique "meiotic cell cycle" (GO:0051321) annotations.

**Notable case: ATG autophagy genes**

7 genes have BOTH "meiotic cell cycle" AND "autophagy" SPKW annotations:
- atg101, atg13, atg16, atg2, atg38, atg5, snx41

These genes have extensive experimental evidence for autophagy functions (IMP for macroautophagy, mitophagy, reticulophagy) but **zero** experimental evidence for meiotic cell cycle.

**Root cause**: UniProt assigns "Meiosis" keyword because autophagy is upregulated during sporulation (meiosis in yeast). This is the same logic error as human apoptosis annotations - a support process gets conflated with the main process.

**GO subset status**: GO:0051321 is in goslim_yeast and goslim_drosophila (NOT in gocheck_do_not_annotate). The specific meiotic phases (prophase I, metaphase II, etc.) ARE in do-not-annotate.

## Full Gene Reviews Completed (2026-01-31)

All 7 ATG genes underwent complete annotation review with deep research. Results:

| Gene | UniProt | Annotations Reviewed | Meiotic Cell Cycle Action | Core Function |
|------|---------|---------------------|---------------------------|---------------|
| atg101 | O13978 | 21 | **REMOVE** | Atg1/ULK1 kinase complex component |
| atg13 | O36019 | 31 | **REMOVE** | Atg1 kinase regulator, autophagy initiation |
| atg16 | O94656 | 11 | **REMOVE** | E3-like ligase for Atg8 lipidation |
| atg2 | O94649 | 26 | **REMOVE** | Lipid transfer protein, ER-phagophore bridge |
| atg38 | O94427 | 10 | **REMOVE** | PtdIns3K complex I subunit |
| atg5 | O74971 | 25 | **REMOVE** | Atg12-Atg5-Atg16 complex component |
| snx41 | O60107 | 19 | **REMOVE** | Sorting nexin for retrograde transport/autophagy |

**Key evidence supporting REMOVE decisions:**

1. **Gene naming misleading**: All genes have "mug" synonyms (meiotically up-regulated gene) based on expression studies (PMID:16303567), but transcriptional upregulation ≠ functional involvement

2. **Experimental evidence is for autophagy, not meiosis**:
   - PMID:19778961: "autophagy-defective cells with amino acid auxotrophy were able to recover sporulation when an excess of required amino acids was supplied"
   - This proves autophagy provides nutrients during sporulation, not meiotic regulation

3. **Consistent pattern**: All 7 genes had the same over-annotation logic - upregulation during meiosis was conflated with functional involvement in meiotic cell cycle

## Lessons Learned from S. pombe Analysis

1. **Expression ≠ Function**: Genes upregulated during a biological process are not necessarily functional regulators of that process

2. **Support processes get conflated**: Autophagy supports meiosis/sporulation by providing nutrients, but ATG genes are not meiotic regulators

3. **Gene naming can mislead**: The "mug" (meiotically up-regulated gene) nomenclature led to inappropriate keyword assignments

4. **Closure filtering is essential**: 73% of naive SPKW-unique annotations were redundant with more specific experimental evidence

5. **Well-curated organisms still have systematic over-annotation**: Even with extensive PomBase curation, SPKW-derived annotations introduced errors

## Review Files Location

```
genes/SCHPO/
├── atg101/atg101-ai-review.yaml
├── atg13/atg13-ai-review.yaml
├── atg16/atg16-ai-review.yaml
├── atg2/atg2-ai-review.yaml
├── atg38/atg38-ai-review.yaml
├── atg5/atg5-ai-review.yaml
└── snx41/snx41-ai-review.yaml
```
