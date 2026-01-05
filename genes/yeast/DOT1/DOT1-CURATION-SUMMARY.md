# DOT1 Gene Curation Review Summary

## Gene Overview
DOT1 (Disruptor of telomeric silencing 1) is the unique histone H3 lysine-79 (H3K79) methyltransferase in *Saccharomyces cerevisiae*. UniProt ID: Q04089

## Review Statistics
- **Total Annotations Reviewed:** 41
- **Status:** COMPLETE

## Action Summary

### ACCEPT (30 annotations)
Core function annotations with strong evidence. These represent well-established DOT1 functions:
- **H3K79 methyltransferase activity** (4 annotations): Core enzymatic function supported by IBA, IEA, IDA, and IMP evidence
- **DNA damage checkpoint signaling** (4 annotations): Critical function in G1 and intra-S phase checkpoints
- **Subtelomeric heterochromatin formation** (4 annotations): Well-characterized role in telomeric silencing
- **DNA repair pathways** (6 annotations): Multiple repair processes including HR, NER, and GG-NER
- **Nucleosome interactions** (2 annotations): Essential for binding and catalysis
- **Nuclear localization** (3 annotations): Consistent evidence from multiple sources
- **Histone interactions** (1 annotation): H3 and H4 binding during catalysis
- **Meiotic checkpoint control** (1 annotation): Pachytene checkpoint surveillance
- **DNA damage tolerance** (1 annotation): Negative regulation of translesion synthesis
- **Negative heterochromatin regulation** (1 annotation): Prevention of ectopic heterochromatin spreading
- **Recombinational repair** (2 annotations): Support for homologous recombination pathways

### KEEP_AS_NON_CORE (7 annotations)
Correct but secondary or peripheral functions:
- **GO:0003677 - DNA binding** (IEA): In vitro activity with unclear physiological relevance
- **GO:0006325 - chromatin organization** (IEA): Broad consequence of DOT1 activity
- **GO:0006351 - DNA-templated transcription** (IEA): Indirect support through heterochromatin prevention
- **GO:0051726 - regulation of cell cycle** (IEA): Indirect effect through checkpoint functions
- **GO:0006334 - nucleosome assembly** (IDA): Methylation-independent histone chaperone activity
- **GO:0005634 - nucleus (IEA)** and **GO:0031509 - subtelomeric heterochromatin formation (IEA)**: Redundant with stronger evidence versions

### MARK_AS_OVER_ANNOTATED (4 annotations)
Technically correct but uninformative due to excessive generality:
- **GO:0008168 - methyltransferase activity**: Too broad; specific H3K79 term preferred
- **GO:0016740 - transferase activity**: Excessively general parent term
- **GO:0032259 - methylation**: Generic process term lacking specificity
- Recommendation: Deprioritize in favor of specific functional terms

### REMOVE (1 annotation)
- **GO:0005515 - protein binding** (IPI, PMID:16554755): Violates curation guidelines against vague "protein binding" annotations. No functional context provided. Specific protein interactions should be captured through targeted functional annotations instead.

### MODIFY (1 annotation)
- **GO:0000781 - chromosome, telomeric region** (IEA): Misleading localization annotation. DOT1 is a global enzyme found throughout nucleus, not specifically enriched at telomeres. Proposed replacement: GO:0005634 (nucleus)

## Key Curation Decisions

### 1. Consistent Evidence for Core Functions
Multiple evidence types (IBA, IMP, IDA, IGI) support DOT1's primary roles:
- H3K79 methyltransferase activity
- DNA damage checkpoint signaling
- Subtelomeric heterochromatin formation through indirect mechanisms

### 2. Redundancy in Evidence
Several annotations are represented by multiple evidence codes:
- GO:0031151 (H3K79 methyltransferase activity): 5 annotations (IBA, IEA x2, IDA x2, IMP)
- GO:0000077 (DNA damage checkpoint signaling): 4 annotations (IBA, IEA, IMP, IGI)
- GO:0031509 (Subtelomeric heterochromatin formation): 4 annotations (IBA, IEA, IMP x2)

All redundant annotations ACCEPTED as they provide complementary evidence from different sources.

### 3. Avoidance of Vague Terms
Removed generic "protein binding" annotation per curation guidelines emphasizing specific functional terms over uninformative general annotations.

### 4. Specificity Assessment
Flagged overly broad terms (methyltransferase activity, transferase activity, methylation, chromatin organization) as over-annotated when more specific terms already capture the function.

### 5. Localization Annotation Correction
Modified misleading telomeric region localization to more accurate nuclear localization, as DOT1 is a global histone methyltransferase with genome-wide distribution.

## Evidence Code Analysis

| Evidence Code | Count | Primary Use |
|---|---|---|
| IBA | 5 | Phylogenetic inference - strong for conserved functions |
| IEA | 9 | Computational inference - supplementary evidence |
| IMP | 10 | Mutant phenotype - strong for functional validation |
| IGI | 6 | Genetic interaction - pathway context |
| IDA | 6 | Direct observation - strongest for enzyme function |
| IPI | 1 | Protein interaction - uninformative without context |
| Total | 41 | |

## Literature Evidence
Review heavily weighted recent experimental evidence from:
- Checkpoint function: Wysocki et al. (2005), Giannattasio et al. (2005), Kiakos et al. (2012)
- Meiotic control: San-Segundo & Roeder (2000)
- Catalytic activity: Ng et al. (2002), structural studies
- DNA damage repair: Multiple 2005-2012 studies

## Curation Quality Metrics
- **Well-supported annotations (IMP, IDA, IGI):** 22/41 (54%)
- **Computational evidence only (IEA, IBA):** 14/41 (34%)
- **Annotations removed due to poor specificity:** 1/41 (2%)
- **Annotations modified for accuracy:** 1/41 (2%)

## Recommendations for Future Work
1. Add core_functions section summarizing primary DOT1 roles
2. Reference deep research document for additional context
3. Consider adding supporting_text from key publications
4. Flag redundant annotations for potential consolidation in GO database
5. Maintain specific functional annotations over generic parent terms

