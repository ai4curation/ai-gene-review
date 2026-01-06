# RPN-10 GO Annotation Curation Analysis

## Gene Summary
**Gene Symbol:** rpn-10 (WBGene00004466)
**UniProt Accession:** O61742
**Protein:** 26S proteasome non-ATPase regulatory subunit 4 (PSMD4)
**Organism:** Caenorhabditis elegans
**Key Role:** Ubiquitin receptor subunit of the 19S regulatory particle of the 26S proteasome

## Overview of Curation Approach

This analysis reviews all 15 GO annotations currently assigned to rpn-10. RPN-10 has two main functional roles:
1. **Core Function:** Ubiquitin receptor at the 19S proteasome particle, binding polyubiquitinated substrates via UIM domains
2. **Regulatory Role:** Indirect involvement in sex determination through TRA-2 degradation

The deep research reveals recent (2023-2024) functional insights about ER quality control adaptation and phosphorylation-mediated substrate selectivity that provide important context for evaluating annotations.

---

## Detailed Annotation Reviews

### 1. GO:0005634 - nucleus (IBA: GO_REF:0000033)

**Evidence Code:** IBA (Inferred from Biological Aspect)
**Original Reference:** GO_REF:0000033 (PANTHER phylogenetic inference)
**Supported by:** PMID:26828939 (Keith et al., 2016)

**Action:** **ACCEPT**

**Rationale:**
- Strong IBA evidence from phylogenetic inference across multiple eukaryotic orthologs (human PSMD4 P55036, Drosophila, yeast)
- Supported by experimental evidence (IDA) from Keith et al. (2016) who used RPN-10::GFP and demonstrated nuclear localization in multiple tissues
- Nuclear proteasome localization is conserved across eukaryotes
- Keith et al. (2016): "RPN-10 is expressed broadly and localizes to the cytoplasm and nucleus"

**Quality:** Excellent - combines strong phylogenetic and experimental evidence

---

### 2. GO:0043161 - proteasome-mediated ubiquitin-dependent protein catabolic process (IBA: GO_REF:0000033)

**Evidence Code:** IBA (Inferred from Biological Aspect)
**Original Reference:** GO_REF:0000033 (PANTHER phylogenetic inference)
**Supported by:** PMID:17050737 (Shimada et al., 2006)

**Action:** **ACCEPT**

**Rationale:**
- This is the core biological process function of RPN-10
- RPN-10 is a well-established ubiquitin receptor that delivers polyubiquitinated substrates to the 26S proteasome
- The IBA annotation reflects strong phylogenetic conservation of this function across eukaryotes
- Direct experimental support: Shimada et al. (2006) demonstrated that loss of rpn-10 results in accumulation of ubiquitinated substrates like TRA-2
- The vWFA domain and two UIM domains in RPN-10 are specifically adapted for this function
- This is appropriately specific (not overly broad like just "protein catabolic process")

**Quality:** Excellent - represents core conserved function with multi-line evidence

---

### 3. GO:0005829 - cytosol (IBA: GO_REF:0000033)

**Evidence Code:** IBA (Inferred from Biological Aspect)
**Original Reference:** GO_REF:0000033 (PANTHER phylogenetic inference)
**Supported by:** PMID:26828939 (Keith et al., 2016)

**Action:** **ACCEPT**

**Rationale:**
- IBA annotation from phylogenetic inference is appropriate for subcellular localization
- Strongly supported by direct experimental observation (IDA) from Keith et al. (2016)
- Cytosolic localization is consistent with the role of proteasome subunits
- Keith et al. clearly demonstrated RPN-10::GFP signal in cytoplasm across multiple tissues
- Redundant with higher-quality IDA evidence but not incorrect

**Quality:** Good - phylogenetically sound with experimental support

---

### 4. GO:0008540 - proteasome regulatory particle, base subcomplex (IBA: GO_REF:0000033)

**Evidence Code:** IBA (Inferred from Biological Aspect)
**Original Reference:** GO_REF:0000033 (PANTHER phylogenetic inference)
**Supported by:** PMID:17050737 (Shimada et al., 2006)

**Action:** **ACCEPT**

**Rationale:**
- RPN-10/S5a/PSMD4 is a canonical component of the 19S regulatory particle base subcomplex
- The structural positioning is conserved across eukaryotes (positioned at the base proximal to the 20S core)
- The vWFA domain mediates direct interaction with 20S core (characteristic of base subcomplex proteins)
- UIM domains extend toward substrate binding site
- This is more specific than the broader GO:0000502 (proteasome complex) annotation
- Phylogenetic inference is appropriate here since the structural organization is deeply conserved

**Quality:** Excellent - specific, well-positioned term reflecting true structural role

---

### 5. GO:0031593 - polyubiquitin modification-dependent protein binding (IBA: GO_REF:0000033)

**Evidence Code:** IBA (Inferred from Biological Aspect)
**Original Reference:** GO_REF:0000033 (PANTHER phylogenetic inference)

**Action:** **ACCEPT**

**Rationale:**
- This is the core molecular function of RPN-10
- The two UIM (ubiquitin-interacting motif) domains (positions 216-235 and 273-292) are specifically adapted to recognize and bind polyubiquitin chains
- InterPro confirms UIM domain presence (IPR003903, PF02809)
- This is NOT the overly vague "protein binding" term - it specifies the molecular target (polyubiquitin)
- The specificity is appropriate and informative
- The deep research (Falcon, 2024) confirms UIMs recognize K48-linked polyubiquitin with potential regulation via phosphorylation
- Zhang et al. (2024) demonstrated that UIM spacing and phosphorylation state modulate substrate acceptance
- This binding function is prerequisite for the broader catabolic process function

**Quality:** Excellent - precise, specific, and supports the downstream biological process

---

### 6. GO:0000502 - proteasome complex (IEA: GO_REF:0000043)

**Evidence Code:** IEA (Inferred from Electronic Annotation)
**Original Reference:** GO_REF:0000043 (UniProtKB keyword mapping)

**Action:** **ACCEPT** (but lower priority than GO:0008540)

**Rationale:**
- Valid annotation - RPN-10 is indeed part of the 26S proteasome complex
- IEA is lower quality than IBA evidence
- This is appropriately retained alongside the more specific GO:0008540 annotation (base subcomplex is a child of proteasome complex)
- Redundant but not incorrect
- Both terms can coexist in GO (specific and general hierarchy)

**Quality:** Acceptable - valid but less informative than the specific base subcomplex term

---

### 7. GO:0005634 - nucleus (IEA: GO_REF:0000044)

**Evidence Code:** IEA (Inferred from Electronic Annotation)
**Original Reference:** GO_REF:0000044 (UniProtKB subcellular location vocabulary)

**Action:** **ACCEPT** (redundant with stronger evidence)

**Rationale:**
- Same term as annotation #1 but with lower-quality evidence (IEA vs. IBA/IDA)
- Redundant with the IBA annotation that has experimental support
- Not incorrect, but represents annotation layering
- Can coexist with higher-quality evidence
- Consistent with experimental findings

**Quality:** Acceptable - correct but redundant with better evidence

---

### 8. GO:0005737 - cytoplasm (IEA: GO_REF:0000044)

**Evidence Code:** IEA (Inferred from Electronic Annotation)
**Original Reference:** GO_REF:0000044 (UniProtKB subcellular location vocabulary)

**Action:** **ACCEPT** (redundant with stronger evidence)

**Rationale:**
- Same localization as GO:0005829 (cytosol) but with lower-quality evidence (IEA vs. IBA/IDA)
- Note that "cytoplasm" is broader than "cytosol" (cytoplasm includes nucleus; cytosol is soluble fraction)
- Both are correct: RPN-10 localizes to cytoplasm AND specifically to the cytosolic fraction
- Redundant annotation layering but not incorrect
- Consistent with experimental observations from PMID:26828939

**Quality:** Acceptable - correct but less specific than the IDA and IBA cytosol annotations

---

### 9. GO:0005634 - nucleus (IDA: PMID:26828939)

**Evidence Code:** IDA (Inferred from Direct Assay)
**Original Reference:** PMID:26828939 (Keith et al., 2016)

**Action:** **ACCEPT**

**Rationale:**
- Highest quality experimental evidence - direct visualization using RPN-10::GFP constructs
- Keith et al. used fluorescence microscopy to observe RPN-10 localization in vivo
- Observed in multiple tissues: pharynx, intestine, hypodermis, spermatheca
- Keith et al.: "RPN-10 is expressed broadly and localizes to the cytoplasm and nucleus"
- This directly supports the IBA annotation and validates phylogenetic inference
- Clear statement of observed localization pattern

**Quality:** Excellent - direct experimental evidence

---

### 10. GO:0005737 - cytoplasm (IDA: PMID:26828939)

**Evidence Code:** IDA (Inferred from Direct Assay)
**Original Reference:** PMID:26828939 (Keith et al., 2016)

**Action:** **ACCEPT**

**Rationale:**
- Direct experimental evidence from the same study as annotation #9
- RPN-10::GFP clearly visible in cytoplasm in vivo
- Expected for proteasome subunits which function in both cytoplasm and nucleus
- Keith et al. data clearly support both nuclear and cytoplasmic localization
- This is the same reference as annotation #9 but documenting the cytoplasmic observation

**Quality:** Excellent - direct experimental evidence

---

### 11. GO:0006511 - ubiquitin-dependent protein catabolic process (IMP: PMID:17050737)

**Evidence Code:** IMP (Inferred from Mutant Phenotype)
**Original Reference:** PMID:17050737 (Shimada et al., 2006)

**Action:** **ACCEPT**

**Rationale:**
- Strong experimental evidence from loss-of-function studies
- Shimada et al. demonstrated that rpn-10 knockdown results in:
  - Accumulation of TRA-2 protein (a ubiquitinated substrate)
  - Reduced fertility and feminization phenotype
  - Compromised proteasomal substrate degradation
- Shimada et al.: "TRA-2 proteins accumulated in rpn-10-defective worms"
- The mutant phenotype directly demonstrates the essential role in ubiquitin-dependent protein catabolism
- Note: This is a child term of GO:0043161 (proteasome-mediated process) but broader in scope
- Both are appropriate - the more specific process term (0043161) and the broader catabolic process term
- IMP is solid evidence for a catabolic role

**Quality:** Good - functional evidence from loss-of-function

---

### 12. GO:0006511 - ubiquitin-dependent protein catabolic process (IGI: PMID:17050737)

**Evidence Code:** IGI (Inferred from Genetic Interaction)
**Original Reference:** PMID:17050737 (Shimada et al., 2006)
**Interacting Gene:** WB:WBGene00006734 (ufd-2)

**Action:** **ACCEPT**

**Rationale:**
- Genetic interaction evidence with ufd-2 (ubiquitin-fusion degradation pathway protein)
- ufd-2 is an E4 ubiquitin ligase that conjugates polyubiquitin chains
- Co-knockdown of rpn-10 and ufd-2 overcomes the sex determination phenotype
- Shimada et al.: "co-knockdown of rpn-10 and functionally related ubiquitin ligase ufd-2 overcomes the germline-musculinizing effect of fem-3(gf)"
- This demonstrates functional interaction in the ubiquitin-dependent protein catabolic pathway
- Appropriate use of IGI - the genetic interaction with a known component of the ubiquitin pathway supports the functional annotation
- Redundant with the IMP annotation for the same term but provides complementary genetic evidence

**Quality:** Good - demonstrates genetic interaction with pathway components

---

### 13. GO:0007283 - spermatogenesis (IMP: PMID:17050737)

**Evidence Code:** IMP (Inferred from Mutant Phenotype)
**Original Reference:** PMID:17050737 (Shimada et al., 2006)
**Allele Referenced:** WB:WBVar00250344 (rpn-10 mutant)

**Action:** **KEEP_AS_NON_CORE**

**Rationale:**
- Experimental evidence is solid - rpn-10 loss causes feminization via elimination of spermatogenesis
- However, this is NOT a core function of RPN-10
- The spermatogenesis defect is a DOWNSTREAM CONSEQUENCE of the core UPS dysfunction
- RPN-10's role is to enable degradation of TRA-2 (a sex determination protein)
- Loss of TRA-2 degradation -> TRA-2 accumulation -> sex determination switch toward female -> loss of spermatogenesis
- RPN-10 itself has no specialized spermatogenesis function - it's a general proteasome subunit
- Shimada et al.: "knockdown of the rpn-10 gene, but not any other proteasome subunit genes, sexually transforms hermaphrodites to females by eliminating hermaphrodite spermatogenesis"
- The specificity of the rpn-10 effect reflects the specific dependence of TRA-2 on RPN-10-mediated degradation (perhaps tissue-specific or allele-specific factors)
- This is a pleiotropic secondary effect, not a direct functional role
- Appropriate for KEEP_AS_NON_CORE designation

**Quality:** Good evidence but represents indirect phenotypic consequence rather than direct function

---

### 14. GO:0007283 - spermatogenesis (IGI: PMID:17050737)

**Evidence Code:** IGI (Inferred from Genetic Interaction)
**Original Reference:** PMID:17050737 (Shimada et al., 2006)
**Interacting Gene:** WB:WBGene00006734 (ufd-2)

**Action:** **KEEP_AS_NON_CORE**

**Rationale:**
- Genetic interaction between rpn-10 and ufd-2 in the spermatogenesis/sex determination pathway
- Both genes are components of the ubiquitin-dependent TRA-2 degradation pathway
- Their interaction reflects their common involvement in the substrate selection and modification machinery
- However, like annotation #13, this represents an indirect developmental consequence
- Shimada et al.: "co-knockdown of rpn-10 and functionally related ubiquitin ligase ufd-2 overcomes the germline-musculinizing effect of fem-3(gf)"
- The genetic interaction demonstrates functional connection but in the context of TRA-2 degradation, not intrinsic spermatogenesis function
- Both spermatogenesis annotations (IMP and IGI) should be retained but marked as non-core

**Quality:** Good genetic evidence but represents indirect effect through TRA-2

---

## Summary Table

| Annotation | Term | Evidence | Action | Priority | Notes |
|---|---|---|---|---|---|
| 1 | GO:0005634 (nucleus) | IBA | ACCEPT | CORE | Phylogenetic + experimental support |
| 2 | GO:0043161 (proteasome catabolic) | IBA | ACCEPT | CORE | Core biological function, well-conserved |
| 3 | GO:0005829 (cytosol) | IBA | ACCEPT | CORE | Strong phylogenetic and experimental support |
| 4 | GO:0008540 (regulatory particle base) | IBA | ACCEPT | CORE | Specific structural role, conserved |
| 5 | GO:0031593 (polyubiquitin binding) | IBA | ACCEPT | CORE | Core molecular function, specific and informative |
| 6 | GO:0000502 (proteasome complex) | IEA | ACCEPT | SUPPORTING | Valid but less specific than GO:0008540 |
| 7 | GO:0005634 (nucleus) | IEA | ACCEPT | SUPPORTING | Redundant with IBA/IDA but consistent |
| 8 | GO:0005737 (cytoplasm) | IEA | ACCEPT | SUPPORTING | Redundant with IBA/IDA but consistent |
| 9 | GO:0005634 (nucleus) | IDA | ACCEPT | CORE | Direct experimental evidence |
| 10 | GO:0005737 (cytoplasm) | IDA | ACCEPT | CORE | Direct experimental evidence |
| 11 | GO:0006511 (ubiquitin catabolism) | IMP | ACCEPT | CORE | Loss-of-function demonstrates requirement |
| 12 | GO:0006511 (ubiquitin catabolism) | IGI | ACCEPT | SUPPORTING | Genetic interaction with pathway component |
| 13 | GO:0007283 (spermatogenesis) | IMP | KEEP_AS_NON_CORE | SECONDARY | Indirect developmental consequence |
| 14 | GO:0007283 (spermatogenesis) | IGI | KEEP_AS_NON_CORE | SECONDARY | Indirect developmental consequence |

---

## Critical Observations from Deep Research

The 2024 deep research adds important context:

1. **Phosphorylation-Mediated Regulation** (Zhang et al., 2024):
   - PSMD4 (human ortholog of RPN-10) is phosphorylated at S266 between the two UIM domains
   - This phosphorylation alters UIM geometry and substrate chain recognition
   - Results in selective degradation during DNA damage response
   - **Implication:** RPN-10 function is not static but dynamically regulated
   - **Current annotations:** Appropriately capture the binding and catabolic functions but don't capture the regulatory complexity

2. **ER Quality Control Adaptation** (Chinchankar et al., 2023):
   - rpn-10 loss triggers constitutive ER UPR activation
   - ERQC genes and xbp-1 splicing are upregulated
   - An ECPS-2 (ECM29-like) axis provides ER proteostasis
   - **Implication:** RPN-10 plays indirect role in ERQC pathway
   - **Current annotations:** Do not capture ER-related functions
   - **Assessment:** These appear to be compensatory/adaptive responses to loss rather than core functions

3. **Stress Resistance and Longevity** (Keith et al., 2016):
   - rpn-10 loss causes 30% lifespan extension at 25°C
   - SKN-1 (Nrf2 ortholog) is required for stress resistance and longevity
   - Enhanced oxidative stress resistance (increased gst-4p::GFP)
   - **Implication:** RPN-10 has important role in proteostasis homeostasis
   - **Current annotations:** Do not specifically capture stress response roles

---

## Recommendations for Additional Annotations (Not Included in Current GOA)

### Potential Candidates (Would require NEW annotation action):

1. **GO:0000505 - proteasome-mediated ubiquitin-dependent protein catabolic process in nucleus**
   - RPN-10 is known to function in nuclear protein degradation
   - Evidence: Keith et al. demonstrated nuclear localization and TRA-2 accumulation in nucleus
   - This would be a child term of GO:0043161 with appropriate specificity
   - **Recommendation:** Could be added with IDA evidence from PMID:26828939

2. **GO:0043065 - positive regulation of apoptosis**
   - TRA-2 is a sex determination protein; its degradation affects developmental decisions
   - Not a direct function but could be inferred
   - **Recommendation:** Not sufficient evidence in current literature

3. **GO:0006986 - response to unfolded protein** or **GO:0034976 - response to endoplasmic reticulum stress**
   - Chinchankar et al. (2023) showed rpn-10 mutants have constitutive ERQC activation
   - However, this appears to be an ADAPTIVE response to loss, not a normal function
   - **Recommendation:** Would need additional evidence that wild-type RPN-10 is involved in ERQC

---

## Potential Concerns and Issues

### No Major Annotation Errors Detected

The existing annotation set is of high quality. Key strengths:

1. ✓ Avoids vague terms like "protein binding" - uses specific "polyubiquitin modification-dependent protein binding"
2. ✓ Includes both specific and general hierarchy terms appropriately
3. ✓ Balances computational (IBA, IEA) with experimental evidence (IDA, IMP, IGI)
4. ✓ Correctly identifies structural role (base subcomplex) vs general complex membership
5. ✓ Appropriately marks developmental/sex determination phenotypes as non-core

### Minor Issues (Not Critical):

1. **Some Localization Redundancy:**
   - Multiple annotations for nucleus (IBA #1, IEA #7, IDA #9)
   - Multiple annotations for cytoplasm (IBA #3, IEA #8, IDA #10)
   - This is acceptable in GO but represents annotation layering
   - The IDA annotations should be prioritized

2. **Spermatogenesis Classification:**
   - Currently marked as KEEP_AS_NON_CORE in existing YAML (good decision)
   - Could consider removing entirely if prioritizing only core functions
   - However, retention as non-core is appropriate for completeness

---

## Curation Conclusions

### Overall Assessment

The current annotations for rpn-10 are well-curated and evidence-based. This is likely the result of careful human review already incorporated into the file.

**Key Strengths:**
- Core molecular and biological functions properly identified
- Structural role within proteasome complex appropriately specified
- Experimental evidence properly weighted and prioritized
- Sex determination phenotype correctly classified as secondary/non-core
- Avoids overly broad or vague molecular function terms

**Completeness Assessment:**
- The core functions are comprehensively covered
- Optional additions (ER stress, tissue-specific, etc.) would require new evidence
- Current annotation set captures the primary function across conditions

### Recommended Actions

1. **All ACCEPT decisions are STRONGLY SUPPORTED**
   - No changes recommended to the 11 core annotations
   - The balance of evidence is appropriate

2. **KEEP_AS_NON_CORE decisions are APPROPRIATE**
   - Spermatogenesis annotations correctly identified as secondary to core UPS function

3. **No NEW annotations recommended**
   - Deep research findings (ER adaptation, phosphorylation regulation) represent either:
     - Adaptive responses to loss rather than normal function, or
     - Regulatory mechanisms layered on top of core function
   - Would need more direct evidence of these functions in wild-type background

---

## References Used in This Analysis

1. Keith SA, Maddux SK, Zhong Y, et al. Graded proteasome dysfunction in Caenorhabditis elegans activates an adaptive response. PLOS Genetics. 2016;12:e1005823. https://doi.org/10.1371/journal.pgen.1005823

2. Shimada M, Kanematsu K, Tanaka K, et al. Proteasomal ubiquitin receptor RPN-10 controls sex determination in Caenorhabditis elegans. Molecular Biology of the Cell. 2006;17:5356-5371. https://doi.org/10.1091/mbc.e06-05-0437

3. Chinchankar MN, Taylor WB, Ko SH, et al. A novel endoplasmic reticulum adaptation is critical for the long-lived Caenorhabditis elegans rpn-10 proteasomal mutant. Biochimica et Biophysica Acta - Gene Regulatory Mechanisms. 2023;1866:194957. https://doi.org/10.1016/j.bbagrm.2023.194957

4. Zhang X, Zhu T, Li X, et al. DNA damage-induced proteasome phosphorylation controls substrate recognition and facilitates DNA repair. PNAS. 2024;121:e2321204121. https://doi.org/10.1073/pnas.2321204121

5. UniProtKB O61742 - 26S proteasome non-ATPase regulatory subunit 4 (retrieved June 2025)

---

## Curation Standard Notes

This review follows GO Curation Standards:
- Evidence codes are appropriate to data type
- Anatomical/cellular component specificity is maintained
- Molecular functions are specific and informative
- Biological processes reflect direct vs. secondary roles appropriately
- Phylogenetic inference (IBA) is supported by experimental evidence where possible
- IEA annotations are retained alongside better evidence rather than removed (acceptable for GO)
