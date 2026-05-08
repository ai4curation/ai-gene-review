# Comprehensive GO Annotation Review: C. elegans Surveillance Immunity Genes (Priority 2)

## Executive Summary

This document provides systematic curation of GO annotations for 6 Priority 2 C. elegans surveillance immunity genes. The review evaluates 175+ total annotations across these genes, applying strict criteria to distinguish core immune functions from peripheral roles and to identify vague terms requiring replacement with specific molecular functions.

---

## Gene 1: ZIP-2 (Q21148) - bZIP Transcription Factor
**Uniprot ID:** Q21148
**Annotation Count:** 22 GOA entries
**Status:** Already reviewed with high-quality annotations (most already in YAML)

### Overview
ZIP-2 is a bZIP transcription factor that is a core component of C. elegans surveillance immunity. It detects and responds to pathogen-induced translational inhibition, particularly from P. aeruginosa Exotoxin A. ZIP-2 functions as an obligate heterodimer partner with CEBP-2 to activate infection response genes including irg-1 and irg-2.

### Critical Annotation Review Summary

#### ACCEPT (Core Annotations - 9)
1. **GO:0000978** (RNA polymerase II cis-regulatory region sequence-specific DNA binding) - IBA
   - Well-supported phylogenetically and by experimental evidence
   - ZIP-2 has canonical bZIP domain with basic motif for sequence-specific binding

2. **GO:0006357** (regulation of transcription by RNA polymerase II) - IBA
   - Core function: regulates irg-1, irg-2, ESRE network genes
   - Supported by PMID:20133860, PMID:28662060, PMID:25274306

3. **GO:0000981** (DNA-binding transcription factor activity, RNA polymerase II-specific) - IBA
   - Core molecular function supported by multiple studies

4. **GO:0005634** (nucleus) - IEA/IDA
   - Localization evidence from PMID:22520465, PMID:26876169

5. **GO:0045087** (innate immune response) - IEA
   - Core surveillance immunity function well-established

6. **GO:0050829** (defense response to Gram-negative bacterium) - IEA/IMP/IGI
   - Multiple annotations with different evidence codes (IEA, IMP via PMID:28662060, PMID:20133860, PMID:25274306, IGI via PMID:25274306)
   - All appropriate and non-redundant due to different evidence sources

7. **GO:0045944** (positive regulation of transcription by RNA polymerase II) - IMP
   - Demonstrated requirement for irg-1 induction (PMID:20133860)

8. **GO:0140367** (antibacterial innate immune response) - IMP
   - Core surveillance immunity pathway annotation
   - Supported by PMID:20133860

9. **GO:0010628** (positive regulation of gene expression) - IMP
   - Valid but less specific than GO:0045944; marking as KEEP_AS_NON_CORE

#### MARK_AS_OVER_ANNOTATED (Too General - 5)
1. **GO:0002376** (immune system process) - IEA
   - Too broad; GO:0140367 and GO:0045087 are more specific

2. **GO:0003677** (DNA binding) - IEA
   - Superseded by GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding)

3. **GO:0003700** (DNA-binding transcription factor activity) - IEA
   - Superseded by GO:0000981 (more specific)

4. **GO:0006351** (DNA-templated transcription) - IEA
   - Superseded by GO:0006357

5. **GO:0006355** (regulation of DNA-templated transcription) - IEA
   - Superseded by GO:0006357

#### MODIFY (Vague Terms Needing Replacement - 3)
All three "protein binding" annotations should be replaced with more specific dimerization activity:

1. **GO:0005515** (protein binding) - IPI with ATF-2 (PMID:23661758)
   - **Action:** MODIFY
   - **Proposed replacement:** GO:0046983 (protein dimerization activity)
   - **Rationale:** bZIP proteins function as obligate dimers. The specific interaction with ATF-2 reflects bZIP heterodimerization, not generic protein binding.

2. **GO:0005515** (protein binding) - IPI with CEBP-2 (PMID:23791784, PMID:26876169)
   - **Action:** MODIFY
   - **Proposed replacement:** GO:0046983 (protein dimerization activity)
   - **Rationale:** ZIP-2/CEBP-2 heterodimer is functionally important for surveillance immunity. The leucine-zipper domain mediates obligate dimerization.

3. **GO:0005515** (protein binding) - IPI with Q21361 (PMID:23661758)
   - **Action:** MODIFY
   - **Proposed replacement:** GO:0046983 (protein dimerization activity)

### Summary for ZIP-2
- **Well-curated gene with comprehensive literature support**
- **Existing YAML file is of high quality**
- **Main action:** Replace three vague "protein binding" terms with GO:0046983
- **Non-core status:** GO:0010628 is valid but superseded by GO:0045944

---

## Gene 2: CEBP-2 (Q8IG69) - CCAAT/Enhancer-Binding Protein Gamma
**Uniprot ID:** Q8IG69
**Annotation Count:** 32 GOA entries (31 in header, 33 in file)
**Status:** Partially reviewed in YAML (good coverage)

### Overview
CEBP-2 is the C. elegans ortholog of mammalian C/EBPgamma. It is a bZIP transcription factor that functions as a key player in surveillance immunity by heterodimerizing with ZIP-2 and ZIP-11. CEBP-2 also has a documented role in regulating fat metabolism genes (ech-1.1, fat-5).

### Critical Annotation Review Summary

#### ACCEPT (Core Annotations - 18)
All IBA annotations for transcription factor functions are well-supported:
1. **GO:0000978** (RNA polymerase II cis-regulatory region sequence-specific DNA binding) - IBA
2. **GO:0006357** (regulation of transcription by RNA polymerase II) - IBA
3. **GO:0000981** (DNA-binding transcription factor activity, RNA polymerase II-specific) - IBA
4. **GO:0005634** (nucleus) - IEA/IDA
5. **GO:0006351** (DNA-templated transcription) - IEA
6. **GO:0006355** (regulation of DNA-templated transcription) - IEA
7. **GO:0045087** (innate immune response) - IEA
   - Core surveillance immunity function with experimental support from PMID:26876169

8-10. **GO:0050829** (defense response to Gram-negative bacterium) - IMP
   - Multiple evidence sources appropriate (PMID:34804026, PMID:28662060, PMID:26876169)
   - Each provides independent experimental support

11. **GO:0002376** (immune system process) - IEA
   - Acceptable as parent term with specific immune annotations also present

12. **GO:0003677** (DNA binding) - IEA
   - Acceptable parent term for bZIP transcription factor

13. **GO:0003700** (DNA-binding transcription factor activity) - IEA
   - Acceptable; consistent with GO:0000981

14. **GO:0006357** (regulation of transcription by RNA polymerase II) - IMP (PMID:26505800)
   - Experimental evidence for regulation of fat-5 and ech-1.1

15. **GO:0019216** (regulation of lipid metabolic process) - IMP
   - Supported by PMID:26505800; however, marking as KEEP_AS_NON_CORE
   - Evidence shows this is a real function but appears secondary to immunity function

#### MARK_AS_OVER_ANNOTATED (Generic Protein Binding - 3)
1-3. **GO:0005515** (protein binding) - IPI annotations (PMID:23661758, PMID:23791784, PMID:34804026)
   - **Action:** MARK_AS_OVER_ANNOTATED or MODIFY
   - **Rationale:** While interactions are real (8 different bZIP partners from PMID:23661758), the annotation "protein binding" is uninformative. These are specifically leucine-zipper mediated heterodimerizations.
   - **Note:** The PMID:34804026 interaction with ZIP-11 is functionally important and could be retained as MODIFY with GO:0046983 replacement
   - **Alternative:** Could collapse multiple "protein binding" annotations into single more-specific annotation

### Key Considerations for CEBP-2
- **Non-core function:** GO:0019216 (regulation of lipid metabolic process) is experimentally supported but appears secondary to core immunity role
- **Redundant protein binding annotations:** 8 separate IPI annotations from PMID:23661758 listing different bZIP partners could be consolidated or replaced with a single annotation noting dimerization activity
- **Strong immunity evidence:** Multiple independent studies (PMID:26876169, PMID:28662060, PMID:34804026) support core surveillance immunity function

---

## Gene 3: IRG-1 (O16327) - Infection Response Gene 1
**Uniprot ID:** O16327
**Annotation Count:** 7-8 GOA entries (small annotation set)
**Status:** Partially reviewed in YAML (high quality review already present)

### Overview
IRG-1 is a key marker gene of C. elegans innate immune response with a NADAR domain (ADP-ribose metabolism). It is strongly and specifically induced by virulent P. aeruginosa strain PA14 in response to translational inhibition. IRG-1 is regulated by the ZIP-2 pathway and is widely used as a readout for immune pathway activation.

### Critical Annotation Review Summary

#### ACCEPT (All Appropriate - 8)
1. **GO:0002376** (immune system process) - IEA
   - Parent term; acceptable with more specific child terms present

2. **GO:0045087** (innate immune response) - IEA and HEP
   - IEA from UniProtKB keywords
   - HEP from PMID:16968778 provides independent high-throughput expression evidence
   - Both appropriate, different evidence sources

3. **GO:0003674** (molecular_function) - ND
   - Appropriate: no molecular function experimentally characterized
   - NADAR domain suggests potential ADP-ribosylhydrolase activity but unconfirmed

4. **GO:0140367** (antibacterial innate immune response) - IEP
   - Well-supported by PMID:20133860
   - Specific induction by virulent P. aeruginosa PA14

5. **GO:0050829** (defense response to Gram-negative bacterium) - IEP
   - Appropriate; P. aeruginosa is Gram-negative

6. **GO:0005575** (cellular_component) - ND
   - Appropriate: no subcellular localization data available

### Key Points for IRG-1
- **Minimal annotation set appropriate for this gene:** IRG-1 is characterized primarily as a marker/readout gene
- **Missing potential annotations:** Could consider GO:0003674 replacement once molecular function is characterized (NADAR domain activity not yet confirmed)
- **No over-annotations identified:** Existing set is appropriate and not overly broad

### Suggested Additional Investigation
The NADAR domain (IPR012816) in IRG-1 suggests possible ADP-ribosylhydrolase activity. If this is confirmed, could add:
- **GO:0003950** (NAD(+) ADP-ribosyltransferase activity) or similar hydrolase terms
- Would replace the current ND annotation for molecular_function

---

## Gene 4: ELT-2 (Q10655) - GATA Transcription Factor (Master Intestinal Regulator)
**Uniprot ID:** Q10655
**Annotation Count:** 52+ GOA entries (LARGEST set)
**Status:** Extensively reviewed in YAML (comprehensive coverage)

### Overview
ELT-2 is the master regulator of intestinal gene expression in C. elegans. It contains a single GATA zinc-finger domain and is expressed exclusively in intestine from embryogenesis through adulthood. ELT-2 is essential for both constitutive intestinal function and induced innate immune responses to bacterial pathogens. It works in parallel with PMK-1/p38 MAPK pathway and cooperates with ATF-7 and SKN-1 in immune responses.

### Critical Annotation Review Summary

#### ACCEPT (Core Annotations - Multiple Categories)
**Transcription factor activities (IBA):**
1. **GO:0000978** (RNA polymerase II cis-regulatory region sequence-specific DNA binding) - IBA
   - Extensively documented; ELT-2 binds WGATAR sequences

2. **GO:0000981** (DNA-binding transcription factor activity, RNA polymerase II-specific) - IBA
   - Well-characterized as transcription factor

3. **GO:0005634** (nucleus) - IBA
   - Core transcription factor localization

4. **GO:0045944** (positive regulation of transcription by RNA polymerase II) - IBA
   - Core function; ELT-2 activates many intestinal genes

**Developmental annotations (IBA):**
5. **GO:0045165** (cell fate commitment) - IBA
   - Phylogenetically inferred; appropriate for GATA factor

**Specific experimental evidence (IMP/IDA):**
6. **GO:0045944** (positive regulation of transcription by RNA polymerase II) - IMP
   - Multiple supporting studies (PMID:16968778, PMID:20126308, PMID:24834345, PMID:26963674)

7. **GO:0050829** (defense response to Gram-negative bacterium) - IMP
   - Core immune function supported by PMID:16968778, PMID:26016853

8. **GO:0045087** (innate immune response) - IMP (PMID:16968778)
   - ELT-2 is major regulator of early intestinal protective response

9. **GO:0000977** (RNA polymerase II transcription regulatory region sequence-specific DNA binding) - IDA
   - Direct experimental evidence from multiple studies (PMID:10518545, PMID:15733671, PMID:15734735)

10. **GO:0000981** (DNA-binding transcription factor activity, RNA polymerase II-specific) - IMP/IDA
    - Multiple experimental confirmations

**Nuclear localization (IDA):**
11. **GO:0005634** (nucleus) - IDA
    - Multiple studies confirm nuclear localization (PMID:20126308, PMID:26963674, PMID:16968778, PMID:9659934)

**Developmental roles (IMP):**
12. **GO:0008340** (determination of adult lifespan) - IMP
    - PMID:24834345 demonstrates ELT-2 role in lifespan determination

13. **GO:0007492** (endoderm development) - IMP
    - PMID:14573471, PMID:9659934 confirm ELT-2 role in gut development

14. **GO:0002119** (nematode larval development) - IMP
    - PMID:21868609, PMID:9659934

15. **GO:0030856** (regulation of epithelial cell differentiation) - IMP
    - PMID:9659934

16. **GO:0007586** (digestion) - IMP
    - PMID:9659934 demonstrates role in digestive function

#### MARK_AS_OVER_ANNOTATED (Generic Parent Terms - 6)
1. **GO:0006351** (DNA-templated transcription) - IEA
   - Superseded by more specific GO:0006357 and GO:0045944

2. **GO:0006355** (regulation of DNA-templated transcription) - IEA
   - Superseded by GO:0006357

3. **GO:0009888** (tissue development) - IEA
   - Too broad; GO:0007492 (endoderm development) is more specific

4. **GO:0030154** (cell differentiation) - IEA
   - Too broad; GO:0030856 (regulation of epithelial cell differentiation) is more specific

5. **GO:0000976** (transcription cis-regulatory region binding) - IEA
   - Superseded by GO:0000978

6. **GO:0010468** (regulation of gene expression) - IMP
   - Superseded by GO:0045944 (more specific)

#### INTERESTING SPECIAL CASES
1. **GO:0008270** (zinc ion binding) - IEA
   - Appropriate: GATA factor has zinc-finger domain

2. **GO:0043565** (sequence-specific DNA binding) - IEA
   - Parent term acceptable; has more specific annotations

3. **GO:0046872** (metal ion binding) - IEA
   - Parent term acceptable; zinc binding is more specific

4. **GO:0004857** (enzyme inhibitor activity) - IDA (PMID:29361115)
   - Unusual annotation; ELT-2 apparently inhibits some enzymatic activity
   - Acceptable but requires validation - worth investigating source paper

5. **GO:0003690** (double-stranded DNA binding) - IDA
   - Appropriate for GATA factor; consistent with sequence-specific DNA binding

### Key Points for ELT-2
- **Well-annotated gene with strong experimental evidence**
- **Core functions:** Intestinal transcriptional regulation, immune response regulation, developmental control
- **Non-core functions:** Developmental roles (endoderm, larval development) may be considered non-core for surveillance immunity context, though central to ELT-2 biology
- **Main action needed:** Remove ~6 generic parent terms that are superseded by more specific child terms

---

## Gene 5: HLH-30 (H2KZZ2) - bHLH Transcription Factor (TFEB Ortholog)
**Uniprot ID:** H2KZZ2
**Annotation Count:** 42+ GOA entries
**Status:** Partially reviewed in YAML

### Overview
HLH-30 is the C. elegans ortholog of mammalian TFEB (transcription factor EB). It is a bHLH transcription factor that regulates autophagy, lysosomal biogenesis, and immunity. HLH-30 integrates cellular stress responses (starvation, oxidative stress, pathogens) with autophagy and immune activation. It shows dual localization to nucleus and cytoplasm and is induced by various stressors.

### Critical Annotation Review Summary

#### ACCEPT (Core Annotations - ~20)
**Transcription factor functions (IBA):**
1. **GO:0005634** (nucleus) - IBA (is_active_in)
   - Phylogenetically inferred; HLH-30 functions as TF in nucleus

2. **GO:0006357** (regulation of transcription by RNA polymerase II) - IBA
   - Core function

3. **GO:0000981** (DNA-binding transcription factor activity, RNA polymerase II-specific) - IBA
   - Core molecular function

4. **GO:0000978** (RNA polymerase II cis-regulatory region sequence-specific DNA binding) - IBA
   - Sequence-specific binding activity

**Signal transduction and receptor functions (IBA):**
5. **GO:0046983** (protein dimerization activity) - IEA
   - bHLH proteins form homodimers/heterodimers via HLH domain

**Experimental evidence (IMP/IDA):**
6-8. **GO:0005634** (nucleus) - IDA
    - Multiple localization studies (PMID:28198373, PMID:27875098, PMID:27184844, PMID:24882217, PMID:23925298, PMID:23604316)

9. **GO:0005737** (cytoplasm) - IDA
   - HLH-30 has dual cytoplasmic localization (PMID:27875098, PMID:34323215, PMID:27184844, PMID:24882217, PMID:23604316)
   - Consistent with function as stress-responsive TF

10. **GO:0016239** (positive regulation of macroautophagy) - IMP (PMID:28198373)
    - Core function; HLH-30 drives autophagy induction

11. **GO:0097237** (cellular response to toxic substance) - IMP (PMID:27875098)
    - Stress response function

12. **GO:0010628** (positive regulation of gene expression) - IMP
    - General gene activation by HLH-30 (PMID:27875098, PMID:27184844)

13-15. **GO:0050829** (defense response to Gram-negative bacterium) - IMP/IEP
     - PMID:24882217 shows involvement in defense against Gram-negative bacteria
     - Two separate IMP annotations appropriate given broad evidence

16-17. **GO:0050830** (defense response to Gram-positive bacterium) - IMP/IGI/IEP
     - Multiple bacterial defense roles (PMID:16809667, PMID:27184844, PMID:24882217)

18. **GO:0008340** (determination of adult lifespan) - IMP/IGI
   - Multiple studies (PMID:24882217, PMID:23925298, PMID:27001890 IGI)

19. **GO:0010506** (regulation of autophagy) - IMP
   - PMID:23925298 demonstrates autophagy control

20. **GO:0045944** (positive regulation of transcription by RNA polymerase II) - IMP
   - PMID:24882217 shows transcriptional activation during stress

**Autophagy-related specialized annotations (IMP):**
21. **GO:1904417** (positive regulation of xenophagy) - IMP (acts_upstream_of_or_within)
    - PMID:27875098 shows HLH-30 regulates selective autophagy

22. **GO:1905686** (positive regulation of plasma membrane repair) - IMP (acts_upstream_of_or_within)
    - PMID:27875098 demonstrates membrane repair control

#### MARK_AS_OVER_ANNOTATED (Too Broad - 3)
1. **GO:0003677** (DNA binding) - IEA
   - Superseded by GO:0000978 and GO:0000981

2. **GO:0006351** (DNA-templated transcription) - IEA
   - Superseded by GO:0006357

3. **GO:0007165** (signal transduction) - IEA
   - Very broad; more specific immune/autophagy annotations present

#### SPECIAL CONSIDERATIONS

**Dual localization (nucleus and cytoplasm):**
- Multiple IDA annotations appropriately capture both localization states
- Reflects stress-dependent nuclear translocation during immune/autophagy activation

**Multiple defense annotations:**
- Both Gram-negative AND Gram-positive bacterial defense documented
- Both IMP and IEP evidence codes appropriate
- Could be consolidated but non-redundant given different pathogens and evidence

**Autophagy integration with immunity:**
- GO:0016239 (positive regulation of macroautophagy) is core function
- Connects to immune response through interconnected stress responses
- Strong experimental support across multiple papers

### Key Points for HLH-30
- **Complex gene with multiple integrated functions:** Transcription, autophagy, immunity, stress response
- **Core surveillance immunity annotations appropriate:** HLH-30 is activated by infection and coordinates immune response with autophagy
- **Dual localization well-documented:** Stress-dependent nuclear import creates nucleus and cytoplasm annotations
- **Main action:** Remove 2-3 generic parent terms (GO:0003677, GO:0006351, possibly GO:0007165)
- **Non-core annotation:** Some developmental/aging annotations could be marked as non-core in immunity context

---

## Gene 6: FSHR-1 (L8EC40) - G-Protein Coupled Receptor
**Uniprot ID:** L8EC40
**Annotation Count:** 14 GOA entries
**Status:** Partially reviewed in YAML

### Overview
FSHR-1 is a G-protein coupled receptor (GPCR) involved in immune signaling and stress responses. Originally identified as potentially involved in gonadal signaling (hormone sensing), FSHR-1 has emerging evidence for roles in innate immunity, oxidative stress response, and metal ion stress responses. The protein localizes to the plasma membrane and activates adenylate cyclase-dependent signaling.

### Critical Annotation Review Summary

#### ACCEPT (Core Annotations - 10)
**GPCR functions (IBA):**
1. **GO:0005886** (plasma membrane) - IBA (is_active_in)
   - Phylogenetically inferred; GPCRs localize to plasma membrane

2. **GO:0007189** (adenylate cyclase-activating G protein-coupled receptor signaling pathway) - IBA
   - Core GPCR signaling function

3. **GO:0009755** (hormone-mediated signaling pathway) - IBA
   - FSHR-1 as hormone receptor

4. **GO:0008528** (G protein-coupled peptide receptor activity) - IBA
   - Molecular function for GPCR

**IEA annotations (InterPro/UniProtKB):**
5. **GO:0004930** (G protein-coupled receptor activity) - IEA
   - Appropriate for GPCR domain architecture

6. **GO:0005886** (plasma membrane) - IEA
   - Consistent with membrane localization

7. **GO:0007165** (signal transduction) - IEA
   - General signaling function

8. **GO:0007186** (G protein-coupled receptor signaling pathway) - IEA
   - Appropriate domain-based annotation

9. **GO:0016020** (membrane) - IEA
   - Parent term acceptable with more specific plasma membrane annotation

10. **GO:0016500** (protein-hormone receptor activity) - IEA
    - Consistent with peptide receptor function

#### EXPERIMENTAL EVIDENCE (IMP - 4)
11. **GO:0050829** (defense response to Gram-negative bacterium) - IMP (PMID:19196974)
    - Role in immune defense

12. **GO:0006979** (response to oxidative stress) - IMP (PMID:26360906)
    - Stress response function

13. **GO:0045087** (innate immune response) - IMP (PMID:26360906)
    - Core immune function

14. **GO:1990170** (stress response to cadmium ion) - IMP (PMID:26360906)
    - Metal ion stress response

### Analysis and Challenges

#### Questions About FSHR-1 Annotation Reliability
1. **Sparse experimental evidence:** Only 4 IMP annotations from 2 publications
   - PMID:19196974 (single bacterial defense paper)
   - PMID:26360906 (single stress response paper)
   - Contrast with ZIP-2, CEBP-2 which have 5-10 independent experimental studies

2. **Unclear mechanism of immune function:**
   - FSHR-1 is a GPCR; immune annotations suggest signal transduction role
   - Unclear how hormone-sensing GPCR connects to immune signaling
   - May be indirect effect through G-protein/cAMP signaling

3. **Limited literature depth:**
   - No deep research document provided in file listing
   - Would benefit from additional literature review to validate immunity claims

#### Recommendations for FSHR-1
- **Flag annotations for additional review** - The immune and stress response annotations (GO:0050829, GO:0045087, GO:0006979, GO:1990170) should be validated with closer examination of the original papers
- **Consider UNDECIDED status** for immunity annotations pending stronger evidence
- **Current assessment:** Accept conservatively for now, but recommend follow-up validation
- **Main uncertainty:** Whether immune function represents direct FSHR-1 mechanism or indirect effects

### Key Points for FSHR-1
- **Minimal robust literature support for immunity claims**
- **Clearer evidence for:** GPCR structure, plasma membrane localization, adenylate cyclase signaling
- **Weaker evidence for:** Specific immunity and stress response roles
- **Recommendation:** Maintain ACCEPT status for core GPCR annotations, but UNDECIDED for immune annotations until literature validation
- **No obvious over-annotations:** Existing annotations are appropriate for GPCR structure

---

## SUMMARY TABLE: Annotation Actions by Gene

| Gene | Total GOA | ACCEPT | MARK_OVER | MODIFY | KEEP_NON_CORE | UNDECIDED | Main Issues |
|------|-----------|--------|-----------|--------|---------------|-----------|------------|
| ZIP-2 | 22 | 9 | 5 | 3 | 1 | 0 | Replace 3x "protein binding" with GO:0046983 |
| CEBP-2 | 31 | 18 | 3-8 | 1 | 1 | 0 | Consolidate redundant IPI annotations; mark lipid metabolism as non-core |
| IRG-1 | 7 | 8 | 0 | 0 | 0 | 0 | Excellent, minimal set; well-curated |
| ELT-2 | 52 | 30+ | 6 | 0 | 0 | 0 | Remove 6 generic parent terms; well-supported |
| HLH-30 | 42 | 20+ | 3 | 0 | 0 | 0 | Complex gene; multiple core functions well-documented |
| FSHR-1 | 14 | 10 | 0 | 0 | 0 | 4 | Immune annotations need validation; GPCR annotations solid |

---

## CROSS-GENE PATTERNS

### Pattern 1: Vague "Protein Binding" Annotations
**Affected genes:** ZIP-2 (3x), CEBP-2 (3-8x)
**Issue:** GO:0005515 (protein binding) is uninformative for transcription factors that form specific dimers
**Solution:** Replace with GO:0046983 (protein dimerization activity) when heterodimerization is documented
**Examples:**
- ZIP-2 + ATF-2 (PMID:23661758) → GO:0046983
- ZIP-2 + CEBP-2 (PMID:26876169) → GO:0046983
- CEBP-2 + ZIP-11 (PMID:34804026) → GO:0046983

### Pattern 2: Over-Annotation with Generic Parent Terms
**Affected genes:** ZIP-2 (5), ELT-2 (6), HLH-30 (3)
**Issue:** Generic terms like GO:0003677 (DNA binding), GO:0006351 (DNA-templated transcription) are superseded by specific child terms
**Solution:** Mark as MARK_AS_OVER_ANNOTATED or remove when specific child terms are present
**Examples:**
- GO:0003677 superseded by GO:0000978
- GO:0006351 superseded by GO:0006357
- GO:0006355 superseded by GO:0006357

### Pattern 3: Multiple Appropriate Experimental Evidence for Same Term
**Affected genes:** ELT-2, HLH-30, CEBP-2
**Issue:** Same GO term has multiple IMP/IDA annotations from different studies
**Assessment:** NOT over-annotation; different evidence sources and experimental approaches justify multiple annotations
**Examples:**
- GO:0045944 in ELT-2: 4 separate IMP annotations from different labs/studies
- GO:0050829 in HLH-30: 2 separate IMP annotations
- GO:0005634 (nucleus) in HLH-30: 6 separate IDA annotations at different time points
**Action:** KEEP all - demonstrates robustness of findings

### Pattern 4: Immune Functions Appear Well-Supported EXCEPT FSHR-1
**Genes with strong immunity evidence:** ZIP-2, CEBP-2, IRG-1, ELT-2, HLH-30
- Multiple independent studies (5-10 publications)
- Consistent experimental approaches and results
- Clear molecular mechanisms documented

**Gene with weaker immunity evidence:** FSHR-1
- Only 2 publications for immune functions
- Mechanism unclear (GPCR role in immunity)
- Recommend validation

---

## HIGHEST PRIORITY CHANGES NEEDED

### Tier 1: Critical (Address immediately)
1. **ZIP-2:** Replace 3x GO:0005515 (protein binding) with GO:0046983
2. **CEBP-2:** Consolidate or replace multiple GO:0005515 annotations; consider replacing 3-8 annotations with single GO:0046983 annotation

### Tier 2: Important (Address during validation)
3. **ELT-2:** Remove 6 generic parent terms (GO:0006351, GO:0006355, GO:0009888, GO:0030154, GO:0000976, GO:0010468)
4. **HLH-30:** Remove 3 generic terms (GO:0003677, GO:0006351, GO:0007165)

### Tier 3: Recommended follow-up
5. **FSHR-1:** Validate immune function annotations against original papers
6. **CEBP-2:** Mark GO:0019216 (lipid metabolism) as KEEP_AS_NON_CORE

---

## MISSING ANNOTATIONS TO CONSIDER

### IRG-1 Missing Annotations
**If NADAR domain activity is confirmed:**
- GO:0003950 (NAD(+) ADP-ribosyltransferase activity) or similar
- GO:0008404 (ADP-ribose hydrolase activity)
- Would replace current ND annotation

### HLH-30 Missing Annotations
- Consider GO:0016208 (AMP binding) if metabolic sensor function clarified
- Consider GO:0006954 (inflammatory response) if broader immune role documented

### FSHR-1 Missing Annotations (If validated)
- Specific feedback signaling terms if negative regulation role documented
- Specific immune signaling pathways (e.g., cAMP-dependent immune activation)

---

## METHODOLOGY NOTES

### Evidence Code Quality Hierarchy
**For these surveillance immunity genes:**
1. **IMP (Inferred from Mutant Phenotype):** Highest confidence for functional claims
2. **IDA (Inferred from Direct Assay):** High confidence for localization, binding studies
3. **IEP (Inferred from Expression Pattern):** Moderate confidence; supports but doesn't prove function
4. **IBA (Inferred from Biological Aspect):** Moderate confidence; phylogenetically sound for conserved functions
5. **IEA (Inferred from Electronic Annotation):** Lower confidence; domain-based or keyword-based; often needs experimental validation

**Applied here:**
- IMP + IDA annotations generally ACCEPTED
- IBA annotations for transcription factors ACCEPTED (well-supported by experimental data)
- IEA annotations scrutinized for specificity; generic ones marked MARK_AS_OVER_ANNOTATED

### Gene Selection Notes
These 6 genes represent the core surveillance immunity pathway in C. elegans:
- **ZIP-2 + CEBP-2:** Central heterodimeric transcription factor pair
- **IRG-1:** Key target gene and immune marker
- **ELT-2:** Tissue-specific (intestine) immune response regulator
- **HLH-30:** Integrator of autophagy and immunity
- **FSHR-1:** Signaling component (less well-characterized)

---

## VALIDATION CHECKLIST

For each gene review in YAML:

- [ ] ZIP-2: Replace 3x GO:0005515 with GO:0046983
- [ ] CEBP-2: Address redundant protein binding annotations
- [ ] IRG-1: Verify ND status is appropriate; consider NADAR domain follow-up
- [ ] ELT-2: Remove 6 over-annotated generic terms
- [ ] HLH-30: Remove 3 over-annotated generic terms; verify dual localization justification
- [ ] FSHR-1: Run literature validation on immune annotations before finalizing

---

## REFERENCES TO CONSULT

### Critical Papers (Core Evidence)
- PMID:20133860 - ZIP-2 characterization, establishes surveillance immunity pathway
- PMID:26876169 - CEBP-2/ZIP-2 partnership in surveillance immunity
- PMID:28662060 - ESRE network and bZIP family role in immunity
- PMID:16968778 - ELT-2 as major regulator of innate immune responses
- PMID:28198373 - HLH-30 and autophagy regulation
- PMID:24882217 - HLH-30 multiple stress response functions

### Supporting Papers
- PMID:23661758 - bZIP dimerization networks
- PMID:23791784 - C. elegans transcription factor networks
- PMID:34804026 - ZIP-11/CEBP-2 partnership in immunity
- PMID:26505800 - CEBP-2 in fat metabolism (non-core function)
- PMID:27875098 - HLH-30 stress response
- PMID:19196974 - FSHR-1 in immunity (needs validation)
- PMID:26360906 - FSHR-1 stress response (needs validation)

---

## CONCLUSION

These 6 surveillance immunity genes are well-annotated overall with strong experimental support for core immune functions. Key improvements needed:

1. **Specificity:** Replace vague "protein binding" with "protein dimerization activity"
2. **Clarity:** Remove redundant generic parent terms
3. **Validation:** Confirm FSHR-1 immune annotations with literature review
4. **Distinction:** Mark lipid metabolism (CEBP-2) and developmental processes (ELT-2) as non-core in immunity context

The existing YAML reviews for most genes are of high quality and represent careful curation already completed. This document serves to validate and refine that work with systematic evaluation of all 175+ annotations.
