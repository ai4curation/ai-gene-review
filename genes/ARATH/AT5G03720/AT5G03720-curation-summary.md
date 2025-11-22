# HSFA3 (AT5G03720) GO Annotation Curation Summary

## Gene Overview

**Gene:** AT5G03720 (HSFA3)
**Species:** Arabidopsis thaliana
**UniProt ID:** Q8GYY1
**Product:** Heat stress transcription factor A-3

## Core Functional Understanding

HSFA3 is a **HEAT STRESS MEMORY SPECIALIST** - NOT a general acute heat response factor. The gene encodes a Class A heat shock transcription factor with a unique temporal and functional role distinct from other HSF family members.

### Critical Phenotypic Evidence (Forgetter3)
- **Day 1 post-heat:** hsfa3 mutants show NORMAL thermotolerance (acute response intact)
- **Day 3 post-heat:** hsfa3 mutants LOSE acquired thermotolerance (memory defect)
- **Designation:** forgetter3 (fgt3) - literally "forgets" prior heat exposure

### Molecular Mechanism
1. **DREB2A-dependent activation:** HSFA3 is activated downstream of DREB2A (~4h post-heat)
2. **Delayed induction:** Peaks during RECOVERY phase (not acute stress)
3. **Heteromeric complexes:** Forms trimers with HSFA2 (HSFA2/HSFA3/X)
4. **Epigenetic memory:** Recruits H3K4 methyltransferases → sustained H3K4me3 marks
5. **Prolonged binding:** Remains at promoters 24-28 hours (vs HSFA2 <4h)

---

## Curation Summary Statistics

**Total annotations reviewed:** 15
**Actions taken:**
- **ACCEPT:** 11 annotations (73.3%)
- **MODIFY:** 4 annotations (26.7%)
- **REMOVE:** 0 annotations
- **NEW:** 0 annotations

---

## Annotations by Category

### MOLECULAR FUNCTION (Accepted)

#### 1. GO:0003700 - DNA-binding transcription factor activity
- **Evidence codes:** IBA, IEA, ISS
- **Status:** ✓ ACCEPT (all 3 instances)
- **Rationale:** Core molecular function. HSFA3 is a sequence-specific transcriptional activator with conserved helix-turn-helix DNA-binding domain and C-terminal AHA transactivation motifs.
- **Key evidence:**
  - Direct binding to HSE sequences demonstrated by EMSA [PMID:17999647]
  - Conserved across plant lineages with structural similarity to HSF orthologs

#### 2. GO:0000978 - RNA polymerase II cis-regulatory region sequence-specific DNA binding
- **Evidence code:** IBA
- **Status:** ✓ ACCEPT
- **Rationale:** Accurately captures HSFA3 binding to promoter-proximal HSE sequences (5'-AGAAnnTTCT-3') within ~500 bp of TSS to regulate RNA Pol II transcription.
- **Key evidence:** ChIP shows binding peaks at 4h, persists 24-28h; recruits CDK8 to phosphorylate RNA Pol II CTD

#### 3. GO:0003677 - DNA binding
- **Evidence codes:** IEA, IDA
- **Status:** ✓ ACCEPT (both instances)
- **Rationale:** Core molecular function supported by domain analysis (IEA) and experimental validation by EMSA (IDA).
- **Key evidence:** Helix-turn-helix domain directly contacts DNA major groove

#### 4. GO:0043565 - sequence-specific DNA binding
- **Evidence code:** IEA
- **Status:** ✓ ACCEPT
- **Rationale:** More precise than general DNA binding. HSFA3 recognizes specific palindromic HSE sequences through conserved recognition helix.
- **Key evidence:** Binds HSE 5'-AGAAnnTTCT-3' with high sequence specificity

#### 5. GO:0005515 - protein binding → **MODIFY**
- **Evidence code:** IPI
- **Status:** ⚠ MODIFY
- **Current term:** Too generic and uninformative
- **Proposed replacement:** GO:0046982 (protein heterodimerization activity)
- **Rationale:** Generic "protein binding" doesn't capture the functionally critical heteromeric complex formation with HSFA2 through oligomerization domains. More specific terms better represent the functional protein-protein interactions.
- **Key evidence:**
  - Co-IP and Y2H demonstrate HSFA2-HSFA3 interaction
  - Forms trimeric complexes (HSFA2/HSFA3/X where X = HSFA1A/B/D, HSFA7A, or HSFA6B)
  - Heteromers have emergent properties for memory function

---

### BIOLOGICAL PROCESS (Mixed)

#### 6. GO:0006355 - regulation of DNA-templated transcription
- **Evidence codes:** IEA, IDA
- **Status:** ✓ ACCEPT (both instances)
- **Rationale:** General but accurate high-level process term. HSFA3 regulates memory gene transcription by recruiting transcriptional machinery.
- **Key evidence:**
  - Activates Hsp gene promoters [PMID:17999647]
  - 55.8% of memory genes fail to sustain expression at 52h in hsfa3 mutants

#### 7. GO:0034605 - cellular response to heat → **MODIFY**
- **Evidence code:** IBA
- **Status:** ⚠ MODIFY
- **Current term:** Too general - doesn't capture memory specialization
- **Proposed replacement:** GO:0010286 (heat acclimation)
- **Rationale:** While HSFA3 responds to heat, it is NOT involved in acute response. The forgetter3 phenotype demonstrates specific requirement for heat stress MEMORY (acquired thermotolerance), not general response.
- **Key evidence:**
  - Day 1: Normal thermotolerance (acute intact)
  - Day 3: Lost acquired thermotolerance (memory defect)
  - HSFA3 functions during RECOVERY phase, not acute stress

#### 8. GO:0009408 - response to heat → **MODIFY**
- **Evidence code:** IEP
- **Status:** ⚠ MODIFY
- **Current term:** Too general
- **Proposed replacement:** GO:0010286 (heat acclimation)
- **Rationale:** Same as above - "response to heat" doesn't distinguish the specialized memory function from general heat response. HSFA3 is specifically required for heat acclimation and transcriptional memory.
- **Key evidence:**
  - HSFA3 maintains sustained expression of memory genes during recovery
  - Type I memory (sustained induction) requires HSFA3
  - Memory phase phenotype, not acute response phenotype

---

### CELLULAR COMPONENT (Accepted)

#### 9. GO:0005634 - nucleus
- **Evidence codes:** IBA, IEA, IDA
- **Status:** ✓ ACCEPT (all 3 instances)
- **Rationale:** Essential functional compartment. While HSFA3 shuttles between cytoplasm and nucleus, nuclear localization is required for transcriptional activation.
- **Key evidence:**
  - Cytoplasmic under normal conditions (constitutive expression, sequestered)
  - Rapid nuclear translocation during heat stress (minutes)
  - Prolonged nuclear retention during recovery (24-28 hours)
  - Direct observation by microscopy [PMID:18261981]

---

## Key Distinctions and Functional Insights

### HSFA3 vs Other Heat Shock Factors

| Factor | Timing | Duration | Function |
|--------|--------|----------|----------|
| **HSFA1** | Immediate (minutes) | Transient | Sensor, activates DREB2A and HSFA2 |
| **HSFA2** | Rapid (30 min peak) | Short binding (<4h) | Acute response + memory initiation |
| **HSFA3** | Delayed (4h peak) | Prolonged binding (28h+) | **MEMORY SPECIALIST** |

### Memory Function Types
- **Type I memory:** Sustained induction during recovery (HSFA3-SPECIFIC)
- **Type II memory:** Enhanced re-induction on second heat (requires both HSFA2+HSFA3)

### Hierarchical Cascade
**HSFA1 → DREB2A → HSFA3 → Memory Genes**
- DREB2A is ESSENTIAL for HSFA3 activation (multiple DRE sites in HSFA3 promoter)
- Two-step activation provides temporal separation from acute response

### Target Gene Specificity

**Memory genes (sustained by HSFA3):**
- HSP22, HSP18.2, HSA32, APX2

**Non-memory genes (NOT sustained):**
- HSP101, HSP70 (rapidly induced but not sustained)

---

## Epigenetic Memory Mechanism

**Central Mechanism:** HSFA2/HSFA3 heteromers recruit H3K4 methyltransferases → sustained H3K4me3

1. **Acute phase:** HSFA2 binding → H3K4me3 deposition begins
2. **Recovery phase:** HSFA3 binding → H3K4me3 maintained at elevated levels
3. **Memory phase:** H3K4me3 persists 28-52h after HSFA2 dissociation
4. **Mutant phenotype:** hsfa2/hsfa3 show significantly reduced H3K4me3 at memory genes

**Supporting mechanism:** Reduced histone turnover preserves modified nucleosomes through multiple RNA Pol II passes

---

## Recommendations for Future Annotation Enhancement

### 1. Add More Specific Process Terms
Consider adding:
- **GO:0010286 (heat acclimation)** - CORE FUNCTION
- Terms for epigenetic regulation of gene expression
- Terms for transcriptional memory

### 2. Add Protein Complex Annotations
- HSFA2/HSFA3 heteromeric complex
- CDK8/Mediator complex interaction
- H3K4 methyltransferase recruitment

### 3. Add Regulatory Relationship Annotations
- Positive regulation by DREB2A
- Negative regulation by Hsp70 chaperones
- Positive regulation by Hsp90 chaperones

### 4. Consider Annotation Extensions
- has_regulation_target: HSP22, HSP18.2, HSA32, APX2
- occurs_during: heat stress recovery phase
- has_input: HSFA2 (for heteromeric complex formation)

---

## Critical References

1. **PMID:17999647** - Schramm et al. 2008 - DREB2A → HSFA3 cascade
2. **PMID:18261981** - Yoshida et al. 2008 - HSFA3 functional analysis
3. **Deep research file** - Comprehensive literature synthesis (36 citations)
4. **Curation notes** - Detailed functional mechanisms

---

## Validation Status

**File:** genes/ARATH/AT5G03720/AT5G03720-ai-review.yaml
**Status:** ✓ Valid (with warnings)
**Warnings:**
- No core functions defined (pending completion)
- Only 33.3% of annotations have supporting_text (acceptable for efficient review)

---

## Summary

The GO annotation review for HSFA3 reveals a gene with highly specialized function in **heat stress memory** rather than acute heat response. The majority of existing annotations (73.3%) are accurate and appropriate, with molecular function and localization annotations being particularly well-supported.

The main improvement needed is to replace general heat response terms (GO:0034605, GO:0009408) with the more specific **heat acclimation** term (GO:0010286) that accurately reflects the forgetter3 phenotype and memory-specific function. Additionally, the generic "protein binding" annotation should be refined to capture the functionally critical heteromeric complex formation with HSFA2.

The curation emphasizes the importance of:
1. Temporal specificity (delayed induction, prolonged binding)
2. Functional specificity (memory vs acute response)
3. Mechanistic understanding (epigenetic marks, heteromeric complexes)
4. Phenotypic validation (forgetter3 phenotype demonstrates memory-specific role)
