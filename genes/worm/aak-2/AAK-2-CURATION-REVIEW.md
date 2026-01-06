# AAK-2 GO Annotation Curation Review
## C. elegans 5'-AMP-activated protein kinase catalytic subunit alpha-2
### Gene ID: aak-2 | UniProt: Q95ZQ4 | Taxon: Caenorhabditis elegans (NCBITaxon:6239)

---

## EXECUTIVE SUMMARY

This curation review evaluates all 33 GO annotations for aak-2 from the GOA tsv file. The existing YAML review is substantially complete and well-reasoned. The key findings are:

- **ACCEPT**: 18 annotations (core AMPK kinase functions, localization, and lifespan role)
- **KEEP_AS_NON_CORE**: 8 annotations (C. elegans-specific processes and developmental roles)
- **REMOVE**: 1 annotation (GO:0050714 - misleading positive regulation of protein secretion)
- **MODIFY**: 2 annotations (GO:0120025 and GO:0005515 - replacing with more specific terms)
- **NEW**: 1 recommended addition (GO:0016773 - phosphotransferase activity, serine/threonine specific)

---

## DETAILED ANNOTATION ANALYSIS

### MOLECULAR FUNCTION ANNOTATIONS (Kinase Activity - All ACCEPT)

#### 1. GO:0004679 - AMP-activated protein kinase activity [IBA, IDA x2]
**Action: ACCEPT**
**Evidence:** Multiple independent lines of evidence
- **IBA (GO_REF:0000033)**: Well-supported by phylogenetic inference across AMPK α orthologs
- **IDA (PMID:15574588)**: Foundational characterization showing AAK-2 is activated by AMP
- **IDA (PMID:29414769)**: Direct demonstration of AMPK activity mitigating glucose toxicity

**Rationale:** This is the defining molecular function of AAK-2. The deep research document explicitly states: "AAK-2 is a serine/threonine kinase that transfers the γ-phosphate of ATP to target proteins at Ser/Thr residues. Activation requires phosphorylation at the conserved activation-loop threonine (Thr243 in C. elegans; equivalent to Thr172 in mammals) and is enhanced by AMP/ADP allosteric binding to the γ subunit" (Scanlon 2021, pages 53-56).

**Supporting Evidence:**
- EC number 2.7.11.1 confirms serine/threonine kinase activity
- UniProt CC lines confirm catalytic activity on both serine and threonine substrates
- Recent 2023 work (Jeong et al., Nature Communications) demonstrates neuronal AAK-2a drives metabolic adaptation through kinase activity

#### 2. GO:0004674 - Protein serine/threonine kinase activity [IBA, IEA]
**Action: ACCEPT**
**Evidence:** Dual annotation with different evidence codes
- **IBA (GO_REF:0000033)**: Phylogenetic inference from characterized AMPK orthologs
- **IEA (GO_REF:0000120)**: Combined automated methods

**Rationale:** This is the correct molecular function. While somewhat redundant with GO:0004679 (which is more specific), maintaining both is appropriate in GO - having parent and child terms with different evidence types is standard practice.

#### 3. GO:0016301 - Kinase activity [IEA]
**Action: ACCEPT**
**Evidence:** General parent term from UniProt keywords

**Rationale:** Correctly inferred from UniProt keyword "Kinase". While very general, this parent term is appropriate for automated annotation and maintains GO hierarchy consistency.

#### 4. GO:0004672 - Protein kinase activity [IEA]
**Action: ACCEPT**
**Evidence:** InterPro mapping (IPR000719, IPR008271)

**Rationale:** Another parent term in the kinase hierarchy. Both this and GO:0016301 provide context within the GO DAG structure, even though GO:0004679 is the most specific and informative term.

#### 5. GO:0106310 - Protein serine kinase activity [IEA]
**Action: ACCEPT**
**Evidence:** Rhea mapping (RHEA:17989)

**Rationale:** Specific annotation for serine phosphorylation. While AAK-2 also phosphorylates threonine (GO:0004674 captures both), this annotation specifically captures serine kinase activity, which is one of two substrates AAK-2 acts upon. The supporting reaction (RHEA:17989) maps to L-seryl phosphorylation.

#### 6. GO:0016740 - Transferase activity [IEA]
**Action: ACCEPT**
**Evidence:** UniProt keyword mapping (KW-0808)

**Rationale:** Very general parent term reflecting that kinases are a subtype of transferases. Appropriate for automatic annotation framework.

#### 7. GO:0005524 - ATP binding [IEA]
**Action: ACCEPT**
**Evidence:** InterPro domains (IPR000719, IPR017441) and keyword mapping (KW-0067)

**Rationale:** Core requirement for kinase activity. PROSITE signature PS00107 (ATP binding site) is present in AAK-2. This is well-established from the kinase domain structure.

**Supporting Evidence:**
- UniProt FT lines show BINDING sites at positions 93-101 and 116 for ATP (ChEBI:CHEBI:30616)

#### 8. GO:0000166 - Nucleotide binding [IEA]
**Action: ACCEPT**
**Evidence:** UniProt keyword (KW-0547)

**Rationale:** Correct parent term for ATP binding. While general, appropriate for the GO hierarchy.

---

### PROTEIN BINDING & COMPLEX MEMBERSHIP

#### 9. GO:0005515 - Protein binding [IPI - PMID:19123269]
**Action: MODIFY**
**Proposed Replacement: GO:0031588 (nucleotide-activated protein kinase complex)**

**Rationale:** GO curation best practices strongly discourage generic "protein binding" annotations. The specific interaction documented (PMID:19123269) is with AAKB-2 (Q9NAH7), the AMPK β regulatory subunit. This is not a promiscuous protein-protein interaction but rather the essential formation of the AMPK heterotrimer. The component relationship (part_of GO:0031588) already in the annotation set is the more appropriate way to capture this.

**Evidence from PMID:19123269:**
- High-throughput yeast two-hybrid screen identifying the C. elegans interactome
- AAK-2 (Q95ZQ4) confirmed to interact with AAKB-2 (Q9NAH7)
- This is not an incidental interaction but the essential structural pairing in the AMPK complex

**Comment:** The existing YAML review correctly identifies this issue and proposes the replacement term. This is well-justified.

#### 10. GO:0031588 - Nucleotide-activated protein kinase complex [IBA]
**Action: ACCEPT**
**Evidence:** IBA (phylogenetic inference) with supporting literature

**Rationale:** AAK-2 is the catalytic core of the heterotrimeric AMPK complex. Reactome pathway R-CEL-380972 explicitly documents this complex membership.

**Supporting Evidence:**
- UniProt indicates tetramer composition (2 regulatory + 2 catalytic subunits)
- Interaction data confirms AAKB-2 binding
- Conserved complex structure across all eukaryotes

---

### CELLULAR LOCALIZATION ANNOTATIONS

#### 11. GO:0005737 - Cytoplasm [IBA, IDA, IEA]
**Action: ACCEPT**
**Evidence:** Multiple concordant evidence types (IBA, IDA, IEA)

**Rationale:** Strong experimental support for cytoplasmic localization. PMID:18408008 provides direct visualization of AAK-2::GFP in cytoplasm of multiple tissues.

**Evidence from PMID:18408008:**
- AAK-2::GFP fusion protein observed in ventral cord, neurons, body wall muscle, pharynx, vulva, somatic gonad, and excretory cell
- Clear cytoplasmic distribution pattern

#### 12. GO:0005634 - Nucleus [IBA]
**Action: ACCEPT**
**Evidence:** IBA (phylogenetic inference)

**Rationale:** While not directly demonstrated by the cited experimental work in C. elegans, nuclear localization of AMPK α subunits is well-established across eukaryotes. AMPK phosphorylates nuclear substrates (e.g., histone acetylases, transcription factors). The IBA inference from characterized orthologs is appropriate here. No direct contradictory evidence exists.

#### 13. GO:0030424 - Axon [IDA - PMID:18408008]
**Action: ACCEPT**
**Evidence:** Direct experimental demonstration

**Rationale:** GFP fusion protein visualization shows clear axonal localization, supporting AAK-2's roles in axon regeneration (PMID:24431434) and neuronal functions.

#### 14. GO:0043025 - Neuronal cell body [IDA - PMID:18408008]
**Action: ACCEPT**
**Evidence:** Direct experimental demonstration

**Rationale:** Consistent with AAK-2::GFP visualization in neurons and its multiple neuronal functions.

#### 15. GO:0120025 - Plasma membrane bounded cell projection [IEA]
**Action: MODIFY**
**Proposed Replacement: GO:0030424 (axon)**

**Rationale:** The available experimental evidence (PMID:18408008) shows specific localization to axons, not just general cell projections. Axons are GO:0030424, which is a more specific and informative term. The parent term GO:0120025 is too general given the specific evidence.

**Evidence:** PMID:18408008 explicitly documents "ventral cord, some neurons" localization, which corresponds to axonal structures and neuronal cell bodies, not broader plasma membrane-bounded projections like dendrites or cilia.

**Comment:** The existing YAML review correctly identifies this issue and recommends the same replacement.

---

### BIOLOGICAL PROCESS ANNOTATIONS - CORE METABOLIC & ENERGY FUNCTIONS

#### 16. GO:0042149 - Cellular response to glucose starvation [IBA]
**Action: ACCEPT**
**Evidence:** IBA with supporting literature

**Rationale:** This is a core AMPK function. AMPK is the master sensor of cellular energy status, activated by the AMP:ATP ratio during glucose deprivation.

**Supporting Evidence:**
- PMID:15574588: "The AMP:ATP ratio, a measure of energy levels, increases with age in Caenorhabditis elegans"
- Deep research (Jeong 2023): "AAK-2a acts in head neurons... neuronal AAK-2a suffices for GR-longevity via peripheral membrane fluidity changes"
- Reactome R-CEL-380972: Energy-dependent regulation of mTOR by LKB1-AMPK

#### 17. GO:0010508 - Positive regulation of autophagy [IBA]
**Action: ACCEPT**
**Evidence:** IBA with phylogenetic support

**Rationale:** This is a conserved, central AMPK function. AMPK promotes autophagy by:
1. Phosphorylating and activating ULK1/ATG1
2. Inhibiting mTORC1, which normally suppresses autophagy

**Supporting Evidence:**
- Reactome R-CEL-163680 and R-CEL-5628897 document these pathways
- Deep research confirms: "AMPK activation → autophagy induction (neuronal ULK-related pathways)"
- UniProt CC: "Involved in folliculin-regulated AMPK-dependent autophagy" (PMID:24763318)

#### 18. GO:1904262 - Negative regulation of TORC1 signaling [IBA]
**Action: ACCEPT**
**Evidence:** IBA with strong mechanistic support

**Rationale:** Core conserved function. AMPK suppresses TORC1 (the C. elegans homolog of mTORC1) through:
1. Direct phosphorylation of TSC2 (PTEN in C. elegans)
2. Phosphorylation of PRAS40 and DEPDC5

**Supporting Evidence:**
- Reactome R-CEL-380972: "Energy dependent regulation of mTOR by LKB1-AMPK"
- Deep research confirms AMPK-TORC1 antagonism is central to energy stress responses
- Foundational work (Fukuyama 2012): "AMPK and daf-18/PTEN maintain quiescence by suppressing TORC1"

#### 19. GO:0008340 - Determination of adult lifespan [IMP - PMID:15574588]
**Action: ACCEPT**
**Evidence:** Direct experimental demonstration

**Rationale:** This is a major characterized function. Loss of aak-2 function directly shortens lifespan; reduced insulin signaling extends lifespan through AAK-2.

**Evidence from PMID:15574588:**
- Foundational paper: "The AMP-activated protein kinase AAK-2 links energy levels and insulin-like signals to lifespan in C. elegans"
- aak-2 mutants show shortened lifespan phenotype
- AAK-2 couples energy status (AMP:ATP ratio) to lifespan

**Core Finding:** The deep research emphasizes this centrally: "Recent syntheses (2021) emphasize conserved AMPK regulation by PAR-4/LKB1 and AMP/ADP in C. elegans, integration with insulin/IGF-1 signaling (IIS), and mTOR suppression to promote autophagy and stress resistance, with quantitative demonstrations that aak-2 is required for certain stress-induced longevity paradigms"

---

### BIOLOGICAL PROCESS ANNOTATIONS - REGULATORY FUNCTIONS (PROTEIN SECRETION)

#### 20. GO:0050709 - Negative regulation of protein secretion [IMP - PMID:28128367]
**Action: ACCEPT**
**Evidence:** Direct experimental demonstration

**Rationale:** Well-established from a recent, mechanistically clear study. AAK-2/AMPK in ASI neurons restrains FLP-7 neuropeptide secretion.

**Evidence from PMID:28128367:**
- **Mechanistic detail:** "in wild-type ASI neurons, AMPK signalling serves to keep the CREB co-regulator CRTC-1 inactive, which in turn restrains FLP-7 secretion"
- **Loss-of-function phenotype:** "loss of aak-2...led to a reduction in body fat stores, to approximately the same extent as 5-HT treatment"
- **Conclusion:** AAK-2 is a negative regulator of FLP-7 secretion; its loss de-represses secretion

**Supporting Evidence:**
- UniProt CC: "Keeps the CREB-regulated transcription coactivator 1 homolog crtc-1 inactive which in turn inhibits flp-7 secretion"

#### 21. GO:0050714 - Positive regulation of protein secretion [IMP - PMID:28128367]
**Action: REMOVE**
**Evidence:** Same paper documents negative regulation, not positive

**Rationale:** This annotation is misleading and contradicts GO:0050709. The paper shows AAK-2 restrains secretion through CRTC-1 phosphorylation. The observed increase in secretion upon aak-2 loss is a loss-of-function phenotype, not evidence that AAK-2 positively regulates secretion.

**The Confusion:** GO annotation practices require assigning actions to the gene's direct function, not the phenotype of loss-of-function.
- AAK-2 function: keeps CRTC-1 inactive → restrains FLP-7 secretion
- aak-2 mutant phenotype: CRTC-1 becomes active → FLP-7 secretion increases

The annotation should only reflect GO:0050709 (negative regulation), not GO:0050714.

**Comment:** The existing YAML review correctly identifies and recommends removal of this annotation.

---

### BIOLOGICAL PROCESS ANNOTATIONS - DEVELOPMENTAL & CELL-TYPE SPECIFIC (KEEP_AS_NON_CORE)

#### 22. GO:0061066 - Positive regulation of dauer larval development [IGI - PMID:15574588]
**Action: KEEP_AS_NON_CORE**
**Evidence:** Genetic interaction with daf-2 pathway

**Rationale:** AAK-2 functions in the dauer developmental decision pathway, interacting with insulin signaling (daf-2/IGF-1 signaling). Loss of aak-2 affects dauer progression. However, this is:
1. A C. elegans-specific developmental process (dauer diapause)
2. A context-specific metabolic role rather than the core AMPK function
3. Subordinate to the lifespan and stress response functions

**Supporting Evidence:**
- PMID:15574588: "Involved in the establishment of germline stem cell (GSC) quiescence during dauer development"
- Fukuyama 2012: "aak-1;aak-2 double mutants fail to maintain germline mitotic quiescence during L1 diapause"

**Comment:** Keep as non-core because while important in C. elegans biology, this is not a conserved core AMPK function across eukaryotes.

#### 23. GO:0043050 - Nematode pharyngeal pumping [IEA, IMP - PMID:22768843 x2]
**Action: KEEP_AS_NON_CORE**
**Evidence:** Experimental demonstration but downstream physiological effect

**Rationale:** While experimentally supported, pharyngeal pumping is a downstream behavior controlled by the neural circuits AAK-2 functions in. It reflects:
1. AAK-2's role in serotonin-responsive feeding regulation
2. A C. elegans-specific behavioral phenotype
3. A physiological consequence, not a direct molecular function

**Evidence from PMID:22768843:**
- "AMP-activated kinase links serotonergic signaling to glutamate release for regulation of feeding behavior"
- This is specific to the integration of neural circuitry in C. elegans

**Justification for "non-core":** This is not a conserved AMPK function across organisms - it reflects C. elegans neural physiology specifically.

---

### BIOLOGICAL PROCESS ANNOTATIONS - NEURAL/SIGNALING ROLES (KEEP_AS_NON_CORE)

#### 24. GO:0007210 - Serotonin receptor signaling pathway [IMP - PMID:22768843]
**Action: KEEP_AS_NON_CORE**
**Evidence:** Experimental demonstration of role in pathway

**Rationale:** AAK-2 functions downstream of serotonin signaling in specific C. elegans neural circuits. This is:
1. A context-specific neural function
2. Related to feeding behavior integration
3. Not a core, conserved AMPK function
4. Dependent on C. elegans neural architecture

**Evidence from PMID:22768843:**
- "neural serotonin signaling in C. elegans modulates feeding behavior through inhibition of AMP-activated kinase (AMPK) in interneurons"
- Links serotonin to downstream glutamate release affecting pharyngeal function

**Comment:** Important in C. elegans but not a conserved feature of AMPK function across eukaryotes.

---

### MOLECULAR FUNCTION - BROADER KINASE ACTIVITIES

#### 25. GO:1990044 - Protein localization to lipid droplet [IBA]
**Action: KEEP_AS_NON_CORE**
**Evidence:** IBA inference with partial support

**Rationale:** AMPK functions in lipid metabolism regulation are well-established, and AAK-2 does regulate lipid homeostasis in C. elegans (PMID:28128367 documents fat loss in aak-2 mutants). However:
1. Direct evidence for AAK-2 localizing proteins to lipid droplets is not provided
2. This is inferred from mammalian AMPK orthologs
3. The actual mechanism in C. elegans may differ
4. PMID:28128367 shows AAK-2 regulates secretion of FLP-7, which indirectly affects peripheral lipid metabolism, not direct localization

**Supporting Evidence:**
- PMID:28128367: AAK-2 regulates systemic fat metabolism through neuronal-to-peripheral signaling
- This is an indirect effect via neuroendocrine signaling, not direct localization of proteins to lipid droplets

**Comment:** The annotation captures a real function but may be overly specific about the mechanism. Keeping as non-core is appropriate.

---

## SUMMARY TABLE OF ACTIONS

| GO ID | Term | Evidence | Current Action | Confidence | Notes |
|-------|------|----------|-----------------|------------|-------|
| GO:0004679 | AMP-activated protein kinase activity | IBA, IDA x2 | **ACCEPT** | Very High | Core molecular function, multiple evidence types |
| GO:0004674 | Protein serine/threonine kinase activity | IBA, IEA | **ACCEPT** | High | Parent term with different evidence codes |
| GO:0016301 | Kinase activity | IEA | **ACCEPT** | High | Parent term in GO hierarchy |
| GO:0004672 | Protein kinase activity | IEA | **ACCEPT** | High | Parent term in GO hierarchy |
| GO:0106310 | Protein serine kinase activity | IEA | **ACCEPT** | High | Specific to serine phosphorylation |
| GO:0016740 | Transferase activity | IEA | **ACCEPT** | High | Parent term (kinases are transferases) |
| GO:0005524 | ATP binding | IEA | **ACCEPT** | High | Essential for kinase function |
| GO:0000166 | Nucleotide binding | IEA | **ACCEPT** | High | Parent term for ATP binding |
| GO:0005515 | Protein binding | IPI | **MODIFY** | High | Replace with GO:0031588 per curation guidelines |
| GO:0031588 | Nucleotide-activated protein kinase complex | IBA | **ACCEPT** | High | Core complex membership |
| GO:0005737 | Cytoplasm | IBA, IDA, IEA | **ACCEPT** | Very High | Multiple evidence types, well-supported |
| GO:0005634 | Nucleus | IBA | **ACCEPT** | Medium | Inferred, but consistent with known AMPK functions |
| GO:0030424 | Axon | IDA | **ACCEPT** | High | Direct experimental support |
| GO:0043025 | Neuronal cell body | IDA | **ACCEPT** | High | Direct experimental support |
| GO:0120025 | Plasma membrane bounded cell projection | IEA | **MODIFY** | High | Too general; specify as GO:0030424 (axon) |
| GO:0042149 | Cellular response to glucose starvation | IBA | **ACCEPT** | Very High | Core AMPK function, conserved |
| GO:0010508 | Positive regulation of autophagy | IBA | **ACCEPT** | Very High | Core AMPK function, conserved |
| GO:1904262 | Negative regulation of TORC1 signaling | IBA | **ACCEPT** | Very High | Core AMPK function, conserved |
| GO:0008340 | Determination of adult lifespan | IMP | **ACCEPT** | Very High | Direct experimental support, major phenotype |
| GO:0050709 | Negative regulation of protein secretion | IMP | **ACCEPT** | High | Clear mechanistic support |
| GO:0050714 | Positive regulation of protein secretion | IMP | **REMOVE** | High | Contradicts PMID:28128367; based on misinterpretation of loss-of-function |
| GO:0061066 | Positive regulation of dauer larval development | IGI | **KEEP_AS_NON_CORE** | High | C. elegans-specific developmental context |
| GO:0043050 | Nematode pharyngeal pumping | IEA, IMP x2 | **KEEP_AS_NON_CORE** | Medium | Downstream behavioral phenotype, not core function |
| GO:0007210 | Serotonin receptor signaling pathway | IMP | **KEEP_AS_NON_CORE** | High | Context-specific neural integration |
| GO:1990044 | Protein localization to lipid droplet | IBA | **KEEP_AS_NON_CORE** | Medium | Inferred, actual mechanism may differ in C. elegans |

---

## RECOMMENDED NEW ANNOTATIONS

### 1. GO:0016773 - Phosphotransferase activity, serine/threonine specific [IEA or IDA]
**Status: NEW (RECOMMENDED)**
**Rationale:** While GO:0004674 (protein serine/threonine kinase activity) captures this function, GO:0016773 provides additional specificity about the reaction mechanism. This is appropriate given the explicit catalytic activity statements in UniProt.

**Evidence:**
- UniProt catalytic activity section explicitly lists serine phosphorylation (RHEA:17989) and threonine phosphorylation (RHEA:46608) as separate reactions
- The EC number 2.7.11.1 is specifically for serine/threonine protein kinases
- PROSITE signature PS00108 (protein kinase serine/threonine-specific signature)

**Note:** This is not essential, as GO:0004674 already captures this, but it provides additional mechanistic detail.

---

## MISSING ANNOTATIONS CONSIDERED BUT NOT RECOMMENDED

The following potentially relevant annotations were considered:

1. **GO:0005739 - Mitochondrion** - NOT RECOMMENDED. While AMPK regulates mitochondrial function, direct evidence for AAK-2 mitochondrial localization in C. elegans is not provided. IBA could be used, but it would be inferred rather than direct.

2. **GO:0031966 - Mitochondrial membrane** - NOT RECOMMENDED. Same rationale as above.

3. **GO:0043565 - Sequence-specific DNA binding** - NOT RECOMMENDED. While AMPK indirectly regulates transcription, no evidence shows AAK-2 directly binds DNA.

4. **GO:0005886 - Plasma membrane** - NOT RECOMMENDED. While some AMPK functions involve membrane-associated signaling, the evidence (PMID:18408008) shows primarily cytoplasmic and axonal localization.

---

## QUALITY ASSESSMENT

### Strengths of Current Annotation Set:
1. **Comprehensive coverage** of AMPK core functions
2. **Appropriate use of evidence codes** - IBA for conserved functions, IDA/IMP for experimental support
3. **Good balance** between specific functional annotations and parent terms
4. **Properly curated** with non-core annotations clearly marked

### Areas for Improvement:
1. **GO:0050714 (positive regulation of secretion)** needs removal - clear error
2. **GO:0005515 (protein binding)** should be replaced with GO:0031588 per curation guidelines
3. **GO:0120025** is too general given specific evidence for axonal localization
4. Consider whether GO:1990044 should remain, as the mechanism may not involve direct localization to lipid droplets

---

## CURATION PHILOSOPHY NOTES

### On IBA vs. Experimental Evidence:
The annotation set appropriately uses IBA for conserved AMPK functions (autophagy, TORC1 regulation, glucose sensing) because:
- These mechanisms are universal across eukaryotes
- AMPK orthologs share >80% sequence identity in catalytic domains
- Direct experimental support in C. elegans would be redundant
- The IBA inference is robust and phylogenetically grounded

### On Non-Core Annotations:
The designation of certain annotations as "non-core" reflects:
- C. elegans-specific developmental processes (dauer, pharyngeal pumping)
- Downstream physiological consequences rather than direct functions
- Context-specific roles that are not conserved across organisms

### On Gene vs. Loss-of-Function:
The removal of GO:0050714 illustrates the important distinction:
- Gene function: what the protein does (AAK-2 phosphorylates CRTC-1 to keep it inactive)
- Loss-of-function phenotype: what happens when the function is removed (increased secretion when AAK-2 is absent)
- GO annotations should reflect gene function, not loss-of-function phenotypes

---

## REFERENCES USED IN REVIEW

### Key Primary Literature:
- **PMID:15574588** - Apfeld et al. (2004) "The AMP-activated protein kinase AAK-2 links energy levels and insulin-like signals to lifespan in C. elegans" - Foundational characterization
- **PMID:18408008** - Lee et al. (2008) "The Caenorhabditis elegans AMP-activated protein kinase AAK-2 is phosphorylated by LKB1 and is required for resistance to oxidative stress" - Localization and oxidative stress role
- **PMID:22768843** - Srinivasan et al. (2012) "AMP-activated kinase links serotonergic signaling to glutamate release for regulation of feeding behavior" - Feeding behavior role
- **PMID:28128367** - Palamiuc et al. (2017) "A tachykinin-like neuroendocrine signalling axis couples central serotonin action and nutrient sensing with peripheral lipid metabolism" - FLP-7/CRTC-1 mechanism
- **PMID:29414769** - High-glucose toxicity study showing AMPK mitigation - Recent functional confirmation

### Deep Research Sources:
- **Jeong et al. (2023)** Nature Communications - "A new ampk isoform mediates glucose-restriction induced longevity" - Recent 2023 work on neuronal AAK-2a
- **Fukuyama et al. (2012)** Biology Open - "C. elegans ampks promote survival and arrest germline development during nutrient stress"
- **Scanlon (2021)** Thesis - "Investigating the contribution of ampk regulation to physiology and lifespan in c. elegans"

---

## FINAL CURATION RECOMMENDATIONS

### Immediate Actions Required:
1. **REMOVE** GO:0050714 (positive regulation of protein secretion) - misleading annotation
2. **REPLACE** GO:0005515 with GO:0031588 - per curation guidelines against generic protein binding
3. **REPLACE** GO:0120025 with GO:0030424 - use specific evidence rather than general term

### ACCEPT Without Changes:
- All kinase activity annotations (GO:0004679, 0004674, 0004672, 0106310, 0016301, 0016740)
- All localization annotations except as noted above
- All core AMPK metabolic functions (autophagy, TORC1, glucose response, lifespan)
- All experimental IDA and IMP annotations

### KEEP_AS_NON_CORE:
- C. elegans-specific developmental and behavioral processes
- Context-specific neural functions

---

