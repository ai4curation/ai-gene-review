# SNF5 Gene Annotation Curation Review
## Saccharomyces cerevisiae (UniProt P18480)

### Review Status: COMPLETE
**Total Annotations Reviewed:** 36 review rows covering 44 GOA annotation rows

---

## CURATION SUMMARY

### Annotation Actions Breakdown

**ACCEPT (23 review rows - 63.9%)**
- Core function annotations supported by experimental evidence
- Proper localization to nuclear/chromatin compartments
- Well-supported biological and molecular processes
- High-quality evidence codes (IDA, IMP, IGI, IPI)

**KEEP_AS_NON_CORE (3 review rows - 8.3%)**
- Cytosol localization (1 annotation)
  - Minor/transient localization, not primary functional compartment
- Invasive growth and double-strand break repair processes (2 annotations)
  - Valid but pleiotropic effect of general transcriptional role

**REMOVE (9 review rows - 25.0%)**
- Generic "protein binding" annotations with no specific molecular-function replacement
  - Physical interactions are not disputed, but GO:0005515 does not describe a
    specific SNF5 activity

**MODIFY (1 review row - 2.8%)**
- PMID:32188938 generic "protein binding" refined to GO:0031491 nucleosome binding
  based on cryo-EM support for Snf5 acidic-patch engagement

---

## ANNOTATION CATEGORIES

### LOCALIZATION (ACCEPTED)
- **Nuclear chromosome** (GO:0000228) - IEA from InterPro
- **Nucleus** (GO:0005634) - IDA from PMID:2233708 and PMID:22932476  
- **Nucleus** (GO:0005634) - IEA from UniProt SubCell
- **Chromatin** (GO:0000785) - NAS from ComplexPortal

### MOLECULAR FUNCTION (ACCEPTED)
- **RNA polymerase II-specific DNA-binding transcription factor binding** (GO:0061629)
  - IPI from PMID:11865042 (direct activator interaction)
  - IMP from PMID:14580348 (targeting activity essential)
  - IPI from PMID:14580348 (complementary evidence)

### MOLECULAR FUNCTION (NON-CORE)
- **Protein binding** (GO:0005515) - 8 instances
  - All IPI evidence from proteomics, crystal structures, or complex studies
  - Valid but generic; more specific terms preferred (histone binding, complex subunit interaction)

### BIOLOGICAL PROCESSES (ACCEPTED)
- **Chromatin remodeling** (GO:0006338) - 4 annotations
  - IEA from InterPro (GO_REF:0000002)
  - IDA from PMID:11163188 (ATP-dependent superhelical torsion generation)
  - IMP from PMID:1459453 (landmark 1992 study)
  - IGI from PMID:1459453 (genetic suppression analysis)

- **DNA-templated transcription** (GO:0006351) - IEA
  - Indirect but valid through chromatin accessibility

- **Regulation of transcription by RNA polymerase II** (GO:0006357) - IDA
  - From PMID:28249159 (complex function in Pol II regulation)

- **Positive regulation of transcription by RNA polymerase II** (GO:0045944) - 3 annotations
  - IMP from PMID:1339306 (global activator)
  - IGI from PMID:1901413 (functional interdependence)
  - IMP from PMID:3542227 (HO gene cell cycle control)

- **Carbon catabolite activation of transcription** (GO:0045991) - IGI
  - From PMID:14580348 (metabolic adaptation role)

### CELLULAR COMPONENT (ACCEPTED)
- **SWI/SNF complex** (GO:0016514) - 5 annotations
  - Multiple IDA annotations from biochemical/structural studies
  - IMP from PMID:8159677 (functional requirement)
  - Strong evidence of core complex membership

### LOCALIZATION (NON-CORE)
- **Cytosol** (GO:0005829) - IDA from PMID:22932476
  - Minor transient localization during nuclear import

### BIOLOGICAL PROCESSES (NON-CORE)
- **Positive regulation of invasive growth in response to glucose limitation** (GO:2000219)
  - Valid but represents specific metabolic context
  - Pleiotropic effect of general transcriptional activation

- **Double-strand break repair via homologous recombination** (GO:0000724)
  - Valid but likely indirect (chromatin accessibility)
  - Pleiotropic effect of general chromatin remodeling

---

## KEY FINDINGS

### Core SNF5 Functions Confirmed
1. **SWI/SNF complex component** - Essential structural/regulatory subunit
2. **Nucleosome anchoring** - Via arginine-rich repeat domains binding histone acidic patch
3. **Chromatin remodeling** - ATP-dependent nucleosome repositioning
4. **Transcription factor recruitment** - Activation domain binding for complex targeting
5. **Gene-specific transcriptional activation** - Required for Pol II-dependent expression
6. **Nucleosome positioning** - Control at promoter regions affects transcription
7. **Metabolic adaptation** - Glucose starvation/carbon source switching responses

### Evidence Quality Assessment
- **High Quality:** IDA, IMP from single studies (experimental direct evidence)
- **Good Quality:** IPI from multiple proteomics/structural studies
- **Conservative:** IEA from InterPro/UniProt (appropriate for established functions)

### Annotation Redundancies
- Multiple "protein binding" annotations represent same biological fact (complex membership)
- Multiple chromatin remodeling annotations support single core function
- Multiple Pol II transcription annotations support single core function

---

## RECOMMENDATIONS

### For Annotation Enhancement
1. **Retain specific replacements for protein binding** where evidence supports them:
   - The PMID:32188938 GO:0005515 row is now refined to GO:0031491 nucleosome binding
   - Other generic GO:0005515 rows should remain removed unless a specific,
     evidence-backed molecular function is identified

2. **Consider new annotations for:**
   - Histone acetylation sensing (SNF5-specific feature from deep research)
   - Nucleosome unwrapping/DNA translocation
   - Complex assembly coordination

3. **Upgrade evidence** for key annotations:
   - Use cryo-EM structures (PMID:32188938) as IDA evidence
   - Leverage deep research on metabolic sensing role

### For Core Function Definition
The 36 review rows cleanly support ~7 core functions:
1. SWI/SNF complex membership (structural)
2. Nucleosome anchoring (biochemical)
3. Chromatin remodeling (catalytic)
4. Transcription factor recruitment (regulatory)
5. Gene-specific activation (biological outcome)
6. Metabolic adaptation (biological outcome)
7. Chromatin organization at promoters (regulatory)

---

## EVIDENCE CODES USED

| Code | Count | Description | Quality |
|------|-------|-------------|---------|
| IEA | 3 | Inferred from Electronic Annotation | Conservative |
| IDA | 9 | Inferred from Direct Assay | High |
| IPI | 15 | Inferred from Physical Interaction | Good |
| IMP | 6 | Inferred from Mutant Phenotype | High |
| IGI | 2 | Inferred from Genetic Interaction | High |
| NAS | 1 | Non-Asserted Statement | Good |

---

## LITERATURE FOUNDATION

**Key References Cited:**
- PMID:2233708 - Foundational 1990 characterization (nuclear localization, transcriptional activation)
- PMID:1459453 - Landmark 1992 evidence for chromatin remodeling mechanism
- PMID:8016655 - 1994 biochemical complex characterization
- PMID:14580348 - Targeting activity requirement for complex function
- PMID:11163188 - ATP-dependent remodeling activity
- PMID:32188938 - Modern cryo-EM structures
- PMID:22932476 - Oxygen regulation and subcellular localization

**Deep Research Integration:**
All major findings from SNF5-deep-research-perplexity.md have been incorporated:
- Histone acidic patch binding mechanism
- Nucleosome anchoring and DNA translocation coupling
- SNF5-specific glutamine-rich metabolic sensor region
- Tumor suppressor role of mammalian SMARCB1 ortholog
- Essential role in cell differentiation programs

---

## VALIDATION NOTES

The comprehensive review demonstrates that SNF5 annotations are:
- **Well-supported:** 63.9% of review rows accepted as core functions
- **Appropriately conservative:** 8.3% marked as non-core but evidentially valid
- **Specific:** 25.0% removed and 2.8% refined to eliminate generic protein-binding assertions
- **Complete:** 44 GOA annotation rows addressed in 36 review rows

The generic "protein binding" annotations were removed or, where PMID:32188938
independently supported acidic-patch engagement, refined to nucleosome binding;
they should not be retained as standalone molecular-function annotations.
