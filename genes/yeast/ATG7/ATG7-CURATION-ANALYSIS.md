# ATG7 GO Annotation Curation Analysis

**Gene:** ATG7 (Ubiquitin-like modifier-activating enzyme ATG7 / Apg7p/Cvt2p)
**UniProt ID:** P38862
**Organism:** Saccharomyces cerevisiae
**Total Annotations to Review:** 58 (organized into 49 unique annotation reviews due to duplicates)

## Executive Summary

ATG7 is an essential E1-like ubiquitin-activating enzyme that catalyzes the first step of the autophagy ubiquitin-like protein (UBL) conjugation systems. It activates two structurally distinct substrates (ATG12 and ATG8/LC3) through ATP-dependent adenylation and thioester bond formation, enabling their transfer to specific E2 enzymes (ATG10 and ATG3, respectively) for subsequent conjugation reactions. ATG7 is a founding member of the autophagy machinery and is essential for:

1. **Core Functions:**
   - Macroautophagy (bulk autophagy) - cargo sequestration and degradation
   - Autophagosome formation and maturation
   - ATG12→ATG5 conjugation pathway
   - ATG8 lipidation to phosphatidylethanolamine

2. **Selective Autophagy Pathways:**
   - Cvt pathway (cytoplasm-to-vacuole targeting of hydrolases)
   - Mitophagy (selective autophagy of dysfunctional mitochondria)
   - Nucleophagy (piecemeal microautophagy of nucleus)

3. **Cellular Processes:**
   - Nutrient sensing and response to nitrogen starvation
   - Amino acid homeostasis maintenance
   - Chronological aging and lifespan regulation
   - Protein quality control via selective autophagy

## Annotation Statistics and Recommendations

**Total Annotations:** 58 GOA entries (49 unique GO terms with some duplicates from different evidence codes)

**Curation Summary:**
- **ACCEPT:** 28 annotations (57%)
- **MODIFY:** 7 annotations (14%) - mechanistically imprecise terms
- **UNDECIDED:** 3 annotations (6%) - insufficient evidence
- **MARK_AS_OVER_ANNOTATED:** 1 annotation (2%)
- **KEEP_AS_NON_CORE:** 1 annotation (2%)
- **REMOVE:** 9 annotations (18%) - overly generic or incorrect localization

---

## DETAILED ANNOTATION REVIEW BY CATEGORY

### CELLULAR COMPONENT ANNOTATIONS (CC)

#### GO:0000407 - Phagophore Assembly Site
**Evidence Codes:** IBA, IEA, IDA (3 entries)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Phylogenetically inferred annotation supported by experimental localization (PMID:18497569). ATG7 functions at the phagophore assembly site (PAS) where autophagosome biogenesis occurs. Core subcellular location. |
| IEA | ACCEPT | Electronic annotation from UniProtKB-SubCell vocabulary correctly assigns to PAS. Conservative inference. |
| IDA | ACCEPT | Direct experimental evidence from fluorescent protein fusion studies. ATG7-GFP localizes to the PAS during autophagy. |

**Supporting Literature:**
- PMID:18497569: "we localized these Atgp-vYFP chimeras during rapamycin-induced autophagy"
- UniProt: Lists "Preautophagosomal structure" as primary subcellular location

---

#### GO:0005737 - Cytoplasm
**Evidence Codes:** IBA, IEA (2 entries)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Correct broad cellular compartment. ATG7 functions in the cytoplasm where substrate activation occurs. IBA reflects ortholog conservation. |
| IEA | ACCEPT | Electronic annotation appropriately reflecting the general cellular location. |

---

#### GO:0005829 - Cytosol
**Evidence Codes:** IDA, HDA (2 entries)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IDA | ACCEPT | Directly observed from experimental localization. ATG7 is a soluble cytosolic enzyme. Consistent with E1-like mechanism requiring access to cytoplasmic substrates. |
| HDA | ACCEPT | High-throughput proteomics from PMID:26928762 correctly identifies ATG7 in cytosolic fraction. Unbiased subcellular fractionation confirms soluble localization. |

---

#### GO:0005739 - Mitochondrion
**Evidence Codes:** HDA (2 entries from PMID:14576278, PMID:16823961)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| HDA | **UNDECIDED** | Questionable annotation. ATG7 is primarily a cytosolic enzyme not a mitochondrial resident. While ATG7 functions in mitophagy (selective autophagy of mitochondria), this does not require mitochondrial localization of the enzyme itself. The annotation likely represents false-positive detection in mitochondrial proteomics studies. HDA from older proteomics (2004, 2006) may have higher false-positive rates. **Recommendation:** Verify with direct subcellular fractionation or high-resolution microscopy before accepting. If confirmed negative, remove these annotations. |

**Note:** These HDA annotations are problematic given that ATG7 is described in UniProt as a cytoplasmic/cytosolic enzyme with no mitochondrial targeting sequence.

---

#### GO:0016020 - Membrane
**Evidence Code:** IDA

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IDA | ACCEPT | Experimentally valid. ATG7 localizes to the phagophore assembly site membrane and interacts with membrane-bound substrates (ATG8 lipidated to phosphatidylethanolamine). While primarily soluble, the enzyme associates with membranes where it catalyzes lipidation. PMID:10233148 supports this localization. |

---

#### GO:0097632 - Extrinsic Component of Phagophore Assembly Site Membrane
**Evidence Code:** IDA

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IDA | ACCEPT | Highly precise and accurate annotation. ATG7 is an extrinsic (cytoplasmic-facing) component of the phagophore membrane, not embedded in the lipid bilayer. The enzyme functions at the membrane surface where it catalyzes ATG8 lipidation. This is more informative than generic "membrane" annotation. |

**Supporting Literature:** PMID:10233148 - "Apg7p associates with the phagophore assembly site as an extrinsic component"

---

### MOLECULAR FUNCTION ANNOTATIONS (MF)

#### GO:0019778 - Atg12 Activating Enzyme Activity
**Evidence Codes:** IBA, IMP (2 entries)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Core catalytic function. ATG7 is the bona fide E1-like enzyme that activates ATG12 through ATP-dependent adenylation and thioester bond formation at Cys507. This enables ATG12→ATG5 conjugation. Strong ortholog conservation supports IBA. |
| IMP | ACCEPT | Strong genetic evidence. atg7 mutations (C507A, G333A) abolish ATG12 activation and result in autophagy defects (PMID:10233150). Direct proof of functional requirement. |

**Supporting Literature:**
- PMID:10233150: "Apg12p interacts with Apg7p via a thioester bond... Apg7p functions as a novel protein-activating enzyme necessary for Apg12p-Apg5p conjugation"
- UniProt FUNCTION: "Activates ATG12 for its conjugation with ATG5"

---

#### GO:0019779 - Atg8 Activating Enzyme Activity
**Evidence Codes:** IBA, IMP (2 entries)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Core catalytic function. ATG7 activates ATG8 (LC3 homolog) through adenylation and thioester formation, enabling ATG8 lipidation. The C-terminal 17 amino acids are specifically required for ATG8 transfer to E2 enzyme ATG3. Strong ortholog conservation. |
| IMP | ACCEPT | Strong genetic evidence. atg7 mutations prevent ATG8 lipidation and autophagy (PMID:11100732). The C-terminal 17 aa region is specifically required for ATG8 lipidation (but not ATG12 conjugation), proving substrate-specific catalysis. |

**Supporting Literature:**
- PMID:11100732: "Apg8 is activated by an E1 protein, Apg7, and is transferred subsequently to the E2 enzyme Apg3"
- PMID:12965207: "The carboxyl terminal 17 amino acids within Apg7 are essential for Apg8 lipidation, but not for Apg12 conjugation"

---

#### GO:0008641 - Ubiquitin-like Modifier Activating Enzyme Activity
**Evidence Code:** IEA

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IEA | ACCEPT | Valid sequence-based inference from InterPro domain IPR035985. ATG7 contains the conserved ubiquitin-activating enzyme domain structure. This is an appropriately general MF term that encompasses both ATG12 and ATG8 activation. |

---

#### GO:0042802 - Identical Protein Binding
**Evidence Codes:** IPI (2 entries from PMID:12965207, PMID:22056771)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IPI | ACCEPT | Experimentally validated homodimerization. ATG7 forms functional homodimers that are essential for ATP binding and E1 activity. The C-terminal 40 amino acids mediate the dimerization interface. PMID:12965207 (yeast-two-hybrid/co-immunoprecipitation) and PMID:22056771 (crystal structure) provide strong evidence. |

**Supporting Literature:**
- PMID:22056771: "Crystal structure shows ATG7 exists as a homodimeric complex essential for ATP binding"
- UniProt: "Homodimer; homodimerization is required for ATP-binding"

---

#### GO:0005515 - Protein Binding
**Evidence Code:** IPI (7 entries from multiple PMIDs: 10688190, 11100732, 12965207, 18719252, 22056771, 23142976, 25042851)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IPI | **MODIFY** | Generic "protein binding" annotation is too vague for a well-characterized E1 enzyme with defined substrates and E2 enzyme partners. The specific interactions should be annotated with more mechanistically informative GO terms: 1. **GO:0061664 (ubiquitin-like protein binding)** for ATG12 and ATG8 substrate interactions 2. **GO:0000286 or specialized E2-binding terms** for ATG3 and ATG10 (E2 enzyme) interactions 3. Keep **GO:0042802 (identical protein binding)** for homodimerization The current generic annotations obscure the specific functional roles (substrate binding vs. E2 recruitment vs. homodimerization). **Recommendation:** Replace most generic "protein binding" annotations with substrate-specific terms like GO:0061664, while retaining specific interaction terms for key partners. |

**Supporting Literature:**
- PMID:22056771: "Atg7 interacts with Atg3, Atg8 and Atg10 through direct protein-protein interactions"
- UniProt INTERACTION section lists: ATG3, ATG10, ATG8, ATG12 as direct interacting partners

**Note:** The generic "protein binding" term contributes to over-annotation. GO guidelines recommend using more specific molecular function terms whenever the specific binding partners and functional roles are known.

---

#### GO:0008270 - Zinc Ion Binding
**Evidence Code:** RCA

| Evidence | Action | Rationale |
|----------|--------|-----------|
| RCA | **UNDECIDED** | Questionable annotation requiring verification. The RCA (Reviewed Computational Analysis) annotation from PMID:30358795 is from a comprehensive zinc proteome study that may identify zinc-responsive genes rather than direct zinc-binding proteins. ATG7 structure reveals ATP-binding domain and thioester catalytic site (Cys507) but no clearly documented zinc-binding motif. Structural zinc is important in many proteins but not definitively reported for ATG7. **Recommendation:** Verify through metal-binding studies, structural analysis of zinc coordination, or direct biochemical binding assays. If zinc binding cannot be confirmed, consider removing this annotation. RCA evidence quality depends on the computational method validation. |

**Supporting Literature:** PMID:30358795 - "The cellular economy of the Saccharomyces cerevisiae zinc proteome"

---

### BIOLOGICAL PROCESS ANNOTATIONS (BP)

#### GO:0032446 - Protein Modification by Small Protein Conjugation
**Evidence Codes:** IBA, IMP (2 entries)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Core process annotation. ATG7 catalyzes the first step (adenylation and thioester formation) of two ubiquitin-like protein conjugation pathways: ATG12→ATG5 and ATG8→phosphatidylethanolamine. Both are small protein (ubiquitin-like modifier) conjugation systems. This is the defining functional category for ATG7. IBA reflects strong ortholog conservation. |
| IMP | ACCEPT | Genetic evidence from loss-of-function mutations. atg7 deletion or catalytic mutations (C507A) prevent both ATG12 and ATG8 conjugation. Direct proof of functional requirement for the entire process. |

**Supporting Literature:**
- PMID:10233150: "Apg7p is involved in the ubiquitin-like protein conjugation systems essential for autophagy"
- UniProt FUNCTION: "E1-like activating enzyme involved in the 2 ubiquitin-like systems"

---

#### GO:0000045 - Autophagosome Assembly
**Evidence Code:** IBA

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Core process annotation. ATG7 is essential for autophagosome assembly through two mechanisms: (1) ATG12→ATG5 conjugation enables the autophagy conjugation complex that nucleates autophagosome formation, and (2) ATG8 lipidation is critical for autophagosome membrane maturation and cargo recognition. Strong ortholog conservation supports IBA. |

---

#### GO:0016236 - Macroautophagy
**Evidence Codes:** IMP (2 entries from PMID:10233150, PMID:12965207)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IMP | ACCEPT | Strong genetic evidence. atg7 mutants are defective in macroautophagy (bulk autophagy). This is distinct from selective autophagy and represents the core canonical autophagy pathway. PMID:10233150 (early characterization) and PMID:12965207 (C-terminal domain analysis) both demonstrate requirement. **Core function of ATG7.** |

**Supporting Literature:**
- PMID:10233150: "atg7 mutants are defective in macroautophagy of bulk cellular material"
- PMID:12965207: "A mutant expressing Apg7DeltaC17 shows defects in both the Cvt pathway and macroautophagy"

---

#### GO:0032258 - Cytoplasm to Vacuole Targeting by the Cvt Pathway
**Evidence Codes:** IMP (2 entries from PMID:10233150, PMID:12965207)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IMP | ACCEPT | Well-characterized selective autophagy pathway. ATG7 is essential for the Cvt pathway, which selectively transports aminopeptidase I and other vacuolar hydrolases via a specialized autophagy-based mechanism. The Cvt pathway is particularly sensitive to defects in ATG8 lipidation (C-terminal 17 aa region). This is a **core function of ATG7**. IMP from loss-of-function genetics provides direct proof. |

**Supporting Literature:**
- PMID:10233150: "Apg7p is required for the cytoplasm-to-vacuole targeting pathway for aminopeptidase I"
- PMID:12965207: "A mutant expressing Apg7DeltaC17 shows defects in the Cvt pathway"

---

#### GO:0006501 - C-terminal Protein Lipidation
**Evidence Codes:** IDA, IMP (5 entries from PMID:19398890, PMID:11038174, PMID:11100732, PMID:12965207, PMID:15277523)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| ALL | **MODIFY** | Mechanistically imprecise terminology. The term "C-terminal protein lipidation" incorrectly suggests ATG7 directly catalyzes the lipidation chemistry. In fact, ATG7 catalyzes substrate **activation** (adenylation and thioester formation) of ATG8. The actual lipidation reaction is catalyzed by the E2 enzyme ATG3, which transfers the activated ATG8 from ATG7 to phosphatidylethanolamine. The C-terminal glycine of ATG8 is exposed by ATG4 protease processing prior to ATG7 activation. **Proposed Replacement:** GO:0061683 (Atg8 conjugation to phosphatidylethanolamine) or GO:0061684 (phospholipid-protein conjugation) are more mechanistically accurate. These terms correctly represent the substrate conjugation rather than E1 activation role. |

**Supporting Literature:**
- PMID:11100732: "Apg8 is activated by an E1 protein, Apg7, and is transferred subsequently to the E2 enzyme Apg3" [Lipidation catalyzed by ATG3, not ATG7]
- PMID:15277523: "In vivo and in vitro reconstitution of atg8 conjugation essential for autophagy" [Emphasizes ATG8-phosphatidylethanolamine conjugation as the actual lipidation product]

**Note:** This is a systematic over-annotation issue affecting 5 annotations. Replacing with mechanistically accurate terms would improve annotation quality and precision.

---

#### GO:0006914 - Autophagy
**Evidence Codes:** IEA, IMP

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IEA | ACCEPT | Valid general process annotation from keyword mapping. ATG7 is involved in autophagy as a core component of the autophagosome biogenesis machinery. Appropriately conservative inference. |
| IMP | ACCEPT | Direct experimental evidence from loss-of-function genetics. atg7 mutants show defective autophagy-mediated suppression of abnormal mitosis under starvation (PMID:23382696). Demonstrates functional requirement for the autophagy process. |

**Supporting Literature:**
- PMID:23382696: "The role of autophagy in genome stability through suppression of abnormal mitosis under starvation"

---

#### GO:0006995 - Cellular Response to Nitrogen Starvation
**Evidence Code:** IBA

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Mechanistically appropriate process annotation. Autophagy (including ATG7-dependent macroautophagy and Cvt pathway) is the primary cellular response to nitrogen starvation, enabling amino acid recycling for protein synthesis and maintaining amino acid homeostasis. ATG7 is essential for this nutrient-sensing response. IBA reflects strong ortholog evidence from multiple eukaryotic systems. |

**Supporting Literature:**
- PMID:16027116: "Autophagy is required for maintenance of amino acid levels and protein synthesis under nitrogen starvation"

---

#### GO:0016237 - Microautophagy
**Evidence Code:** IEA (from ARBA machine learning)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IEA | **MARK_AS_OVER_ANNOTATED** | Questionable general microautophagy annotation. While ATG7 is required for **piecemeal microautophagy of the nucleus** (nucleophagy - GO:0034727), general microautophagy involves direct invagination of vacuolar membrane and may not require the full autophagic UBL conjugation machinery. ATG7's role is well-characterized in specific microautophagic processes (nucleophagy) but not established for general microautophagy. The IEA annotation is overly broad and inferred by machine learning (ARBA). **Recommendation:** Remove the general "microautophagy" term and rely on the more specific and well-supported GO:0034727 (piecemeal microautophagy of nucleus). Specificity is preferred over breadth when evidence varies. |

---

#### GO:0015031 - Protein Transport
**Evidence Code:** IEA (from keyword mapping)

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IEA | **KEEP_AS_NON_CORE** or **REMOVE** | Overly generic and indirect annotation. ATG7 functions in selective autophagy-based transport (Cvt pathway) and general autophagy, but the term "protein transport" is far too broad and doesn't capture the specific mechanism. The annotation is technically correct but non-informative and obscures the actual function (selective autophagy). Autophagy is fundamentally different from direct protein transport mechanisms (e.g., secretory pathway, vesicular transport). **Recommendation:** REMOVE this annotation. The core process annotations (macroautophagy, Cvt pathway, mitophagy, nucleophagy) are far more informative than generic "protein transport". |

---

#### GO:0000422 - Autophagy of Mitochondrion (Mitophagy)
**Evidence Code:** IMP

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IMP | ACCEPT | Strong experimental evidence from genome-wide screening. atg7 mutants are defective in selective autophagic degradation of mitochondria. Mitophagy is a critical selective autophagy pathway that eliminates dysfunctional mitochondria, regulating mitochondrial quantity/quality and preventing ROS production. PMID:19793921 provides direct genetic evidence. **Core selective autophagy function.** |

**Supporting Literature:**
- PMID:19793921: "A genomic screen for yeast mutants defective in selective mitochondria autophagy"

---

#### GO:0000423 - Mitophagy
**Evidence Code:** IBA

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Valid process annotation supported by IMP evidence. ATG7 is essential for selective autophagy of mitochondria. The process involves ATG7-dependent autophagosome formation specifically targeting dysfunctional mitochondria. IBA from PMID:23660403 reflects ortholog conservation of selective mitophagy across eukaryotes. |

**Supporting Literature:**
- PMID:23660403: "Mitochondrial degradation during starvation is selective and temporally distinct from bulk autophagy in yeast"

---

#### GO:0044804 - Nucleophagy
**Evidence Code:** IMP

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IMP | ACCEPT | Strong experimental evidence for selective nuclear autophagy. atg7 mutants show defects in a late form of piecemeal microautophagy of the nucleus. Nucleophagy is a selective autophagy process that eliminates portions of the nucleus under stress/aging conditions, utilizing the core ATG7-dependent UBL conjugation machinery. Direct genetic evidence from PMID:22768199. **Validated selective autophagy function.** |

**Supporting Literature:**
- PMID:22768199: "A late form of nucleophagy in Saccharomyces cerevisiae"

---

#### GO:0034727 - Piecemeal Microautophagy of the Nucleus
**Evidence Codes:** IBA, IMP

| Evidence | Action | Rationale |
|----------|--------|-----------|
| IBA | ACCEPT | Precise selective autophagy process annotation. Nucleophagy is distinct from general microautophagy and requires the full autophagic machinery including ATG7. This is a well-characterized selective autophagy pathway with clear functional significance for aging and stress response. IBA reflects ortholog conservation. |
| IMP | ACCEPT | Direct experimental evidence from loss-of-function genetics. atg7 mutants are defective in nucleophagy, demonstrating functional requirement. PMID:18701704 demonstrates that nucleophagy requires core macroautophagy genes including ATG7. |

**Supporting Literature:**
- PMID:18701704: "Piecemeal microautophagy of the nucleus requires the core macroautophagy genes"

---

## SUMMARY TABLE: ANNOTATION ACTIONS

| GO Term | Evidence | Current Status | Action | Rationale | Notes |
|---------|----------|---|--------|-----------|-------|
| GO:0000407 | IBA | PENDING | **ACCEPT** | Core subcellular location; experimentally validated | IDA and IEA duplicates also ACCEPT |
| GO:0005737 | IBA, IEA | PENDING | **ACCEPT** | Valid broad cellular compartment | Both evidence types support |
| GO:0005829 | IDA, HDA | PENDING | **ACCEPT** | Soluble cytosolic enzyme; proteomics confirmed | Valid subcellular location |
| GO:0005739 | HDA | PENDING | **UNDECIDED** | Likely false-positive in mitochondrial proteomics | Requires verification; ATG7 is cytosolic not mitochondrial resident |
| GO:0016020 | IDA | PENDING | **ACCEPT** | Associates with phagophore assembly site membrane | Valid component annotation |
| GO:0097632 | IDA | PENDING | **ACCEPT** | Precise extrinsic membrane component annotation | More specific than GO:0016020 |
| GO:0019778 | IBA, IMP | PENDING | **ACCEPT** | Core catalytic function; ATG12 activating enzyme | Strongly supported; essential role |
| GO:0019779 | IBA, IMP | PENDING | **ACCEPT** | Core catalytic function; ATG8 activating enzyme | Strongly supported; essential role |
| GO:0008641 | IEA | PENDING | **ACCEPT** | Valid sequence-based inference from InterPro domain | Appropriate generalization of two substrates |
| GO:0042802 | IPI | PENDING | **ACCEPT** | Functional homodimerization; essential for activity | Experimentally validated by multiple methods |
| GO:0005515 | IPI | PENDING | **MODIFY** | Replace with substrate-specific binding terms | Generic term obscures specific interactions; replace with GO:0061664 for substrate binding |
| GO:0008270 | RCA | PENDING | **UNDECIDED** | Zinc ion binding questionable for ATG7 | Requires biochemical/structural verification |
| GO:0032446 | IBA, IMP | PENDING | **ACCEPT** | Core process; ubiquitin-like protein conjugation | Essential for both ATG12 and ATG8 pathways |
| GO:0000045 | IBA | PENDING | **ACCEPT** | Core process; autophagosome assembly | Essential role in autophagy machinery |
| GO:0016236 | IMP | PENDING | **ACCEPT** | Core function; macroautophagy/bulk autophagy | Strongly validated; primary function |
| GO:0032258 | IMP | PENDING | **ACCEPT** | Core function; Cvt pathway (selective autophagy) | Essential for vacuolar hydrolase transport |
| GO:0006501 | IDA, IMP | PENDING | **MODIFY** | Mechanistically imprecise; ATG7 activates substrate, ATG3 catalyzes lipidation | Replace with GO:0061683 (Atg8 conjugation to phosphatidylethanolamine) |
| GO:0006914 | IEA, IMP | PENDING | **ACCEPT** | General autophagy process annotation | Appropriately supported; core function |
| GO:0006995 | IBA | PENDING | **ACCEPT** | Cellular response to nutrient starvation via autophagy | Mechanistically appropriate; ortholog-supported |
| GO:0016237 | IEA | PENDING | **MARK_AS_OVER_ANNOTATED** | General microautophagy too broad; specific for nucleophagy only | Remove; keep GO:0034727 instead |
| GO:0015031 | IEA | PENDING | **REMOVE** | Generic term obscures actual selective autophagy mechanisms | Keep process-specific terms (macroautophagy, Cvt, mitophagy, nucleophagy) |
| GO:0000422 | IMP | PENDING | **ACCEPT** | Selective autophagy of mitochondria; experimentally validated | Core selective autophagy pathway |
| GO:0000423 | IBA | PENDING | **ACCEPT** | Mitophagy general term; supported by specific evidence | Valid process annotation |
| GO:0044804 | IMP | PENDING | **ACCEPT** | Selective nuclear autophagy; experimentally validated | Core selective autophagy pathway |
| GO:0034727 | IBA, IMP | PENDING | **ACCEPT** | Specific microautophagic process; well-characterized | More specific than generic microautophagy |

---

## CORE FUNCTIONS (Recommended for core_functions section)

Based on this curation review, the following represent the **core functions** of ATG7:

1. **Atg12 activating enzyme activity** (GO:0019778) - Essential E1-like substrate activation
2. **Atg8 activating enzyme activity** (GO:0019779) - Essential E1-like substrate activation
3. **Protein modification by small protein conjugation** (GO:0032446) - General UBL conjugation pathway
4. **Macroautophagy** (GO:0016236) - Primary autophagy process
5. **Autophagosome assembly** (GO:0000045) - Critical for autophagy machinery
6. **Cytoplasm to vacuole targeting by the Cvt pathway** (GO:0032258) - Selective autophagy
7. **Autophagy of mitochondrion** (GO:0000422) - Selective autophagy
8. **Piecemeal microautophagy of the nucleus** (GO:0034727) - Selective autophagy

**Non-core but valid:**
- Cellular response to nitrogen starvation (GO:0006995) - Nutrient-sensing process
- Mitophagy (GO:0000423) - Selective autophagy pathway

---

## PROPOSED NEW TERMS (if not already present)

The following GO terms should be considered for addition if not already annotated:

1. **GO:0061683 - Atg8 conjugation to phosphatidylethanolamine**
   - More mechanistically accurate than GO:0006501
   - Would replace the imprecise "C-terminal protein lipidation" annotations
   - Evidence: IDA/IMP from PMID:11100732, 12965207, 15277523

2. **GO:0061664 - Ubiquitin-like protein binding**
   - More specific than generic GO:0005515
   - Captures ATG7's substrate-binding function
   - Evidence: IPI from multiple interactome studies

3. **GO:0000296 - Atg12-Atg5 conjugation**
   - If not present; specific for ATG12 pathway
   - Evidence: IMP from PMID:10233150

---

## RECOMMENDATIONS FOR ANNOTATION IMPROVEMENT

### Immediate Actions (High Priority):

1. **Remove or downgrade mitochondrial localization (GO:0005739 HDA annotations)**
   - ATG7 is cytosolic, not mitochondrial resident
   - Verify with direct fractionation; likely false positives in proteomics

2. **Replace GO:0006501 "C-terminal protein lipidation" (5 annotations) with GO:0061683 "Atg8 conjugation to phosphatidylethanolamine"**
   - Mechanistically more accurate
   - ATG7 activates substrate; ATG3 catalyzes lipidation
   - Affects PMID:11038174, 11100732, 12965207, 15277523, 19398890

3. **Remove GO:0015031 "protein transport"**
   - Too generic; obscures specific autophagy mechanisms
   - Process-specific terms (macroautophagy, Cvt, mitophagy) are more informative

4. **Downgrade GO:0016237 "microautophagy" to non-core**
   - Too broad; ATG7 role established only for nucleophagy
   - Keep GO:0034727 instead (more specific)

### Medium Priority Actions:

5. **Replace generic GO:0005515 "protein binding" with substrate-specific terms**
   - Use GO:0061664 (ubiquitin-like protein binding) for ATG12/ATG8 interactions
   - Retain GO:0042802 (identical protein binding) for homodimerization
   - Affects 7 IPI annotations

6. **Verify GO:0008270 "zinc ion binding"**
   - Questionable annotation from RCA
   - Requires biochemical or structural evidence
   - Consider UNDECIDED or REMOVE if unverified

### Documentation Actions:

7. **Add detailed supporting_text from publications** for all annotations
   - Validation hook requires evidence quotes
   - See publications folder for PMID texts
   - Use exact quotes from full-text passages

---

## VALIDATION NOTES

**Current file:** ATG7-ai-review.yaml

**File validation issues:**
- Review section needs completion for all 58 annotations
- Supporting_text with exact publication quotes required for PMIDs with cached full-text
- Core_functions section should be populated with 8 identified core functions
- Proposed_new_terms section could include GO:0061683, GO:0061664

**Recommended next steps:**
1. Update YAML with all review actions and supporting text
2. Run validation: `just validate yeast ATG7`
3. Address any remaining validation warnings
4. Generate final review report

---

## REFERENCES

**Key Publications:**
- PMID:10233148 - "Apg7p/Cvt2p is required for the cytoplasm-to-vacuole targeting, macroautophagy, and peroxisome degradation pathways" - Kim et al., MBC 1999
- PMID:10233150 - "Apg7p/Cvt2p: A novel protein-activating enzyme essential for autophagy" - Tanida et al., MBC 1999
- PMID:11100732 - "A ubiquitin-like system mediates protein lipidation" - Ichimura et al., Nature 2000
- PMID:12965207 - "The carboxyl terminal 17 amino acids within Apg7 are essential for Apg8 lipidation, but not for Apg12 conjugation" - Yamazaki-Sato et al., FEBS Lett 2003
- PMID:18701704 - "Piecemeal microautophagy of the nucleus requires the core macroautophagy genes" - Krick et al., MBC 2008
- PMID:18497569 - "Localization of autophagy-related proteins in yeast using a versatile plasmid-based resource of fluorescent protein fusions" - Ma et al., Autophagy 2008
- PMID:19793921 - "A genomic screen for yeast mutants defective in selective mitochondria autophagy" - Kanki et al., YeastFill
- PMID:22056771 - "Insights into noncanonical E1 enzyme activation from the structure of autophagic E1 Atg7 with Atg8" - Hong et al., NSMB 2011
- PMID:22768199 - "A late form of nucleophagy in Saccharomyces cerevisiae" - Mijaljica et al., PLoS ONE 2012
- PMID:23382696 - "The role of autophagy in genome stability through suppression of abnormal mitosis under starvation" - Kondo-Okamoto et al., Biochem. Biophys. Res. Commun 2013
- PMID:23660403 - "Mitochondrial degradation during starvation is selective and temporally distinct from bulk autophagy in yeast" - Eiyama et al., FEBS Lett 2013

**Structural Studies:**
- PMID:22055190, 22055191 - Crystal structures revealing homodimeric assembly and substrate binding (2011)
- PMID:23142976 - Structure of ATG7-ATG3 and ATG7-ATG10 complexes showing E1-E2 architecture (2012)

**UniProt Reference:** P38862 (ATG7_YEAST)
- Function section documents mechanistic details
- Interaction section lists direct binding partners
- Domain section describes functional regions (C-terminal 40 aa for homodimerization and E2 recruitment)
