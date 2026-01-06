# ESA1 GO Annotation Review and Curation Analysis

## Gene Overview

**Gene Symbol:** ESA1 (Essential SAS-Related protein 1)
**UniProt ID:** Q08649
**Species:** Saccharomyces cerevisiae
**EC Number:** 2.3.1.48 (histone acetyltransferase activity)

ESA1 is the catalytic subunit of the NuA4 (Nucleosome Acetyltransferase of H4) histone acetyltransferase complex, one of the most extensively characterized epigenetic regulators in yeast. Its functions encompass:

1. **Chromatin acetylation** - selective H4, H3, H2A, H2A.Z, and non-histone protein acetylation
2. **DNA damage response** - H4K16ac required for double-strand break repair accessibility
3. **Transcriptional regulation** - targeting to gene promoters and coding regions
4. **Cell cycle control** - essential for progression through mitosis and cytokinesis
5. **Metabolic regulation** - acetylation of non-histone proteins like ATG3 and PAH1
6. **Chromatin architecture** - nucleosome stability and heterochromatin maintenance

---

## Annotation Triage Strategy

### Key Quality Principles for ESA1 Curation

1. **Specificity Over Generality**: Avoid generic terms like "protein binding" or "transferase activity". Prioritize mechanistically informative terms like "histone H4 acetyltransferase activity".

2. **Substrate Discrimination**: ESA1 acetylates multiple substrates with distinct cellular roles:
   - H4 (primarily K5, K8, K12, K16)
   - H3 (K14)
   - H2A/H2B
   - H2A.Z/HTZ1
   - Non-histone: ATG3, PAH1

3. **Functional Context**: Distinguish between:
   - Direct catalytic activities (HAT, crotonyl transferase)
   - NuA4 complex membership
   - Process involvement dependent on NuA4 recruitment

4. **Evidence Quality**:
   - **IDA/IMP/IGI** = Direct experimental evidence, generally more reliable
   - **IBA** = Phylogenetic inference, typically conservative but may miss specialized functions
   - **IEA** = Computational annotation, useful for broad categories but sometimes over-general
   - **IPI** = Protein-protein interaction evidence - informative for complex components but not substitutes for functional terms

---

## Detailed Annotation Review

### Annotation 1: GO:0000785 chromatin [IBA / GO_REF:0000033]

**Action:** ACCEPT

**Summary:** ESA1 functions as part of the NuA4 complex that acts on chromatin substrates. IBA annotation appropriately identifies chromatin as the cellular compartment where ESA1 is active. This is well-supported by the extensive literature showing NuA4 recruitment to chromatin and nucleosome acetylation.

**Rationale:** The phylogenetic inference (IBA) correctly identifies ESA1 as a chromatin-associated protein based on ortholog analysis. Multiple experimental sources confirm NuA4 localizes to and acetylates chromatin (PMID:10911987, PMID:12353039, PMID:17274630).

**Supporting Evidence:**
- PMID:10911987: "Multiple links between the NuA4 histone acetyltransferase complex and epigenetic control of transcription" - demonstrates NuA4 interaction with chromatin
- PMID:17274630: "Nucleosome recognition by the Piccolo NuA4 histone acetyltransferase complex"

---

### Annotation 2: GO:0004402 histone acetyltransferase activity [IBA / GO_REF:0000033]

**Action:** ACCEPT

**Summary:** ESA1 is the catalytic subunit of NuA4 with broad histone acetyltransferase activity. The IBA annotation appropriately identifies this core function.

**Rationale:** This is ESA1's defining function. Extensive literature demonstrates in vitro and in vivo HAT activity on all four conserved H4 lysines and other histone tails. The IBA evidence reflects phylogenetic conservation of this function across eukaryotes.

**Supporting Evidence:**
- PMID:10487762: "NuA4, an essential transcription adaptor/histone H4 acetyltransferase complex containing Esa1p" - characterization of Esa1p as HAT catalytic subunit
- PMID:9520405: "ESA1 is a histone acetyltransferase that is essential for growth in yeast"
- UniProt EC annotation: 2.3.1.48 (histone acetyltransferase activity)

---

### Annotation 3: GO:0005634 nucleus [IBA / GO_REF:0000033]

**Action:** ACCEPT

**Summary:** ESA1 functions in the nuclear compartment as part of NuA4. The IBA annotation correctly identifies the subcellular localization.

**Rationale:** ESA1 is a nuclear protein that participates in nuclear processes (transcription, DNA repair, cell cycle). The nucleus is the appropriate cellular component annotation.

**Supporting Evidence:**
- PMID:10911987: Discusses NuA4 localization and nuclear functions
- PMID:24843044: "Eaf5/7/3 form a functionally independent NuA4 submodule linked to RNA polymerase II-coupled nucleosome recycling" - demonstrates nuclear function

---

### Annotation 4: GO:0006357 regulation of transcription by RNA polymerase II [IBA / GO_REF:0000033]

**Action:** ACCEPT

**Summary:** ESA1-containing NuA4 complex is recruited to genes and regulates transcription via RNA Polymerase II-dependent mechanisms. The IBA annotation captures this core biological function.

**Rationale:** Extensive literature demonstrates NuA4 recruitment to Pol II-transcribed genes, acetylation of promoter and coding region nucleosomes, and requirement for normal transcription. This is a well-established core function.

**Supporting Evidence:**
- PMID:10487762: "essential transcription adaptor/histone H4 acetyltransferase complex"
- PMID:10835360: "Activation domain-specific and general transcription stimulation by native histone acetyltransferase complexes"
- PMID:19822662: "NuA4 lysine acetyltransferase Esa1 is targeted to coding regions and stimulates transcription elongation with Gcn5"

---

### Annotation 5: GO:0003682 chromatin binding [IBA / GO_REF:0000033]

**Action:** MODIFY (proposed replacement: more specific chromatin-interaction terms or simply remove if covered by "chromatin" and "histone acetyltransferase activity")

**Summary:** While ESA1 does bind chromatin (through nucleosome recognition), this term is overly generic and already covered by the fact that ESA1 acetylates histones and functions as a chromatin-associated enzyme.

**Rationale:** "Chromatin binding" is vague and does not inform about the actual biochemical function of ESA1. The term is redundant given:
1. GO:0000785 (chromatin) already indicates chromatin association
2. GO:0004402 (histone acetyltransferase activity) inherently implies nucleosome/histone recognition and binding

The PMID:17274630 result describing nucleosome recognition would be better captured by more specific terms. If retained, should perhaps be "nucleosome binding" with evidence from PMID:17274630, but this is arguably also redundant.

**Proposed Replacement:** Remove or mark as KEEP_AS_NON_CORE, as it adds no mechanistic information beyond the other annotations.

---

### Annotation 6: GO:0003712 transcription coregulator activity [IBA / GO_REF:0000033]

**Action:** ACCEPT

**Summary:** ESA1 as part of NuA4 functions as a transcription coregulator by acetylating histones and facilitating RNA Pol II activity. The IBA annotation appropriately identifies this molecular function.

**Rationale:** Transcription coregulator activity is the correct term for an enzyme that modulates transcription without being a core promoter-binding component. NuA4/ESA1 is recruited by transcription activators and regulates chromatin accessibility - classic coregulator function.

**Supporting Evidence:**
- PMID:10487762: "transcription adaptor/histone H4 acetyltransferase complex"
- PMID:10835360: "Activation domain-specific and general transcription stimulation"
- PMID:15175650: "Recruitment of the NuA4 complex poises the PHO5 promoter for chromatin remodeling and activation"

---

### Annotations 7-8: GO:0004402 histone acetyltransferase activity [IEA / GO_REF:0000120 and 0000117]

**Action:** ACCEPT (both are duplicate with IBA version, which is fine - different evidence codes)

**Summary:** These are computational inferences (InterPro mapping, ARBA ML models) of the same core function. The IEA annotations provide independent evidence for the same function.

**Rationale:** IEA annotations based on InterPro domain IPR002717 (HAT_MYST-type) and ARBA machine learning are appropriate. ESA1 clearly contains the MYST HAT domain and has documented HAT activity. Multiple evidence codes for the same function are acceptable and provide confidence.

---

### Annotation 9: GO:0006281 DNA repair [IEA / GO_REF:0000043]

**Action:** ACCEPT (but consider strengthening to IDA/IMP)

**Summary:** ESA1 is required for DNA double-strand break repair, particularly through H4 acetylation enabling repair machinery accessibility. The IEA annotation based on UniProt KW (DNA repair) is appropriate.

**Rationale:** PMID:12353039 provides strong experimental evidence that "Acetylation of histone H4 by Esa1 is required for DNA double-strand break repair." The IEA is conservative. An IMP annotation exists (PMID:12353039), which should be preferred if not already captured.

**Supporting Evidence:**
- PMID:12353039: "Acetylation of histone H4 by Esa1 is required for DNA double-strand break repair"
- PMID:16135807: "Regulation of NuA4 histone acetyltransferase activity in transcription and DNA repair by phosphorylation of histone H4"

**Note:** The more specific process "positive regulation of DNA repair" might be more accurate than the generic "DNA repair", but the current annotation is acceptable. A more specific annotation could be "DNA double-strand break repair" (GO:0006302) given the literature focus on DSBs.

---

### Annotation 10: GO:0006325 chromatin organization [IEA / GO_REF:0000043]

**Action:** ACCEPT

**Summary:** ESA1-catalyzed histone acetylation contributes to chromatin organization by modulating nucleosome stability and positioning. The IEA annotation is appropriate.

**Rationale:** Histone acetylation fundamentally alters chromatin structure by disrupting histone-DNA interactions and affecting nucleosome positioning. This is a well-established consequence of HAT activity. IEA is appropriate for this inference from function.

**Supporting Evidence:**
- PMID:10911987: Documents changes in chromatin structure associated with NuA4 function
- PMID:12353039: Demonstrates nucleosome accessibility changes required for repair

---

### Annotation 11: GO:0006351 DNA-templated transcription [IEA / GO_REF:0000043]

**Action:** KEEP_AS_NON_CORE (or MODIFY to more specific transcription term)

**Summary:** While ESA1 does function in transcription, "DNA-templated transcription" is the basal process annotation. ESA1's role is specifically in regulation/facilitation, not in the core transcription machinery itself.

**Rationale:** ESA1 is not a core transcription component (not part of Pol II, TFIID, GTFs, etc.). The annotation should distinguish between:
- **Core process:** GO:0006351 (DNA-templated transcription) - performed by Pol II and GTFs
- **Regulatory role:** GO:0006357 (regulation of transcription by RNA Pol II) or GO:0032968 (positive regulation of transcription elongation)

The current annotation suggests ESA1 directly performs transcription, which is inaccurate. However, the IEA inference from "DNA repair" and "chromatin" keywords is automatic and not entirely wrong - ESA1 does affect transcription indirectly through chromatin remodeling.

**Recommendation:** Mark as KEEP_AS_NON_CORE. The annotation is not incorrect but less specific than available alternatives (GO:0006357, GO:0032968).

---

### Annotation 12: GO:0006355 regulation of DNA-templated transcription [IEA / GO_REF:0000002]

**Action:** ACCEPT

**Summary:** ESA1 regulates transcription through chromatin acetylation. This is more accurately specific than GO:0006351.

**Rationale:** This annotation correctly captures ESA1's regulatory role as a coregulator that modulates transcription rather than performing it directly. The InterPro-based inference is appropriate.

---

### Annotation 13: GO:0006357 regulation of transcription by RNA polymerase II [IEA / GO_REF:0000117]

**Action:** ACCEPT

**Summary:** This is a duplicate/complement to the IBA annotation (Annotation 4). Both appropriately capture ESA1's role in Pol II transcription regulation.

**Rationale:** The IEA (ARBA ML) and IBA inferences both converge on this appropriate annotation. This provides confidence in the assignment.

---

### Annotation 14: GO:0006974 DNA damage response [IEA / GO_REF:0000043]

**Action:** ACCEPT

**Summary:** ESA1 is activated in response to DNA damage and is required for repair. The annotation appropriately captures this process.

**Rationale:** PMID:12353039 and other studies show ESA1 is specifically recruited to DSBs and its activity is required for repair response. IEA from "DNA damage" keyword is appropriate.

**Supporting Evidence:**
- PMID:12353039: DSB-specific recruitment and acetylation patterns
- PMID:16135807: "Regulation of NuA4 histone acetyltransferase activity in transcription and DNA repair by phosphorylation"

---

### Annotation 15: GO:0010485 histone H4 acetyltransferase activity [IEA / GO_REF:0000117]

**Action:** ACCEPT

**Summary:** This is the most specific and informative histone acetyltransferase annotation, identifying H4 as the primary substrate. This should be preferred over the more generic GO:0004402.

**Rationale:** ESA1's defining activity is H4 acetylation, particularly at K5, K8, K12, K16. PMID:12110674 and PMID:10487762 provide experimental support. The ARBA inference is appropriate. This annotation provides mechanistic clarity.

**Supporting Evidence:**
- PMID:10487762: "All four conserved lysines of histone H4 can be acetylated by NuA4"
- PMID:12110674: "A conserved motif common to the histone acetyltransferase Esa1"
- PMID:12353039: H4 acetylation at specific lysines required for DSB repair

**Note:** This should be the PREFERRED annotation over the generic GO:0004402 for ESA1's histone function. However, both are acceptable as they represent different levels of specificity.

---

### Annotation 16: GO:0010629 negative regulation of gene expression [IEA / GO_REF:0000117]

**Action:** REMOVE

**Summary:** ESA1/NuA4 is predominantly a transcriptional ACTIVATOR and POSITIVE regulator. This annotation is misleading and contradicted by most literature.

**Rationale:** The literature overwhelmingly documents NuA4 as a positive regulator of transcription:
- PMID:10835360: "Activation domain-specific and general transcription stimulation"
- PMID:15175650: "Recruitment of the NuA4 complex poises the PHO5 promoter for chromatin remodeling and activation"
- PMID:19822662: "stimulates transcription elongation"

While ESA1 may have indirect effects on some genes through heterochromatin effects (PMID:16436512), the primary documented role is POSITIVE regulation. The "negative regulation" annotation appears to be an artifact of ARBA ML misclassification.

**Action Required:** REMOVE this annotation. It contradicts established biology and is not supported by specific evidence.

---

### Annotation 17: GO:0016740 transferase activity [IEA / GO_REF:0000043]

**Action:** KEEP_AS_NON_CORE (or mark as covered by more specific terms)

**Summary:** While technically correct (acetyltransferase IS a transferase), this annotation is overly generic and provides no mechanistic information.

**Rationale:** "Transferase activity" is an ancestor term of "histone acetyltransferase activity" and is already implicitly covered by GO:0004402 and GO:0010485. Including this makes the annotation set less informative and should be deprioritized in favor of specific enzymatic activity terms.

**Recommendation:** Mark as KEEP_AS_NON_CORE or remove if space is limited for display. Not incorrect, but uninformative.

---

### Annotation 18: GO:0033554 cellular response to stress [IEA / GO_REF:0000117]

**Action:** KEEP_AS_NON_CORE

**Summary:** ESA1 is involved in DNA damage response (a stress response) and may have other stress-related functions. The annotation is acceptable but non-specific.

**Rationale:** ESA1 is required for DNA damage response (Annotation 14, PMID:12353039) which is a cellular stress response. The annotation is correct but broad. The more specific annotations (DNA damage response, DNA repair) are preferred.

**Recommendation:** Keep but mark as non-core. The specific DNA damage response and DNA repair annotations are more informative.

---

### Annotation 19: GO:0035267 NuA4 histone acetyltransferase complex [IEA / GO_REF:0000117]

**Action:** ACCEPT (duplicate with IDA versions - all appropriate)

**Summary:** ESA1 is the catalytic subunit and core component of the NuA4 complex. Multiple evidence codes (IEA, IDA) appropriately establish this complex membership.

**Rationale:** This is a fundamental annotation. ESA1 is essential for NuA4 assembly and catalysis. Multiple evidence codes strengthen this important annotation.

**Supporting Evidence:**
- PMID:10487762: Identification of ESA1 as NuA4 catalytic subunit
- PMID:10911987: NuA4 complex composition and function
- PMID:15485911: Yaf9 component involved in NuA4 structure

---

### Annotation 20: GO:0061733 protein-lysine-acetyltransferase activity [IEA / GO_REF:0000120]

**Action:** ACCEPT

**Summary:** This is the correct formal name for the enzymatic activity of histone and protein acetyltransferases. It properly captures ESA1's activity on both histone and non-histone substrates.

**Rationale:** UniProt EC 2.3.1.48 maps to "protein-lysine-acetyltransferase activity", making this annotation formally correct. The IEA from EC/Rhea mapping is appropriate. This annotation allows capture of ESA1's emerging role as a non-histone protein acetyltransferase (ATG3, PAH1, etc.).

**Supporting Evidence:**
- PMID:22539722: ESA1 acetylation of ATG3 (non-histone)
- PMID:29765047: ESA1 acetylation of PAH1 (non-histone)
- UniProt CATALYTIC ACTIVITY: Explicitly lists protein lysine acetylation activity

---

### Annotation 21: GO:0106226 peptide 2-hydroxyisobutyryltransferase activity [IEA / GO_REF:0000116]

**Action:** UNDECIDED (or REMOVE if evidence is limited to computational inference)

**Summary:** ESA1 can use alternative acyl-CoA substrates (2-hydroxyisobutanoyl-CoA) for protein modification. This capability is established in vitro but biological relevance is unclear.

**Rationale:** UniProt explicitly documents that ESA1 has "protein 2-hydroxyisobutyrylation" capability based on PMID:31699900 sequence comparisons with Tip60 (O94446). However:
1. The evidence (ECO:0000250) is computational/ortholog-based, not experimental for yeast ESA1
2. Biological relevance in yeast is unknown
3. No literature documents in vivo 2-hydroxyisobutyrylation by ESA1 in yeast

**Recommendation:** UNDECIDED. The annotation reflects UniProt's conservative assignment based on sequence homology, but experimental evidence for yeast ESA1-mediated 2-hydroxyisobutyrylation is absent. Could keep as a future-oriented annotation or remove if restricting to experimentally demonstrated functions.

---

### Annotation 22: GO:0140064 peptide crotonyltransferase activity [IEA / GO_REF:0000116]

**Action:** ACCEPT

**Summary:** ESA1 catalyzes histone and protein crotonylation using crotonyl-CoA. PMID:31699900 explicitly demonstrates this function experimentally.

**Rationale:** PMID:31699900 ("Gcn5 and Esa1 function as histone crotonyltransferases to regulate crotonylation-dependent transcription") directly demonstrates ESA1's ability to catalyze crotonylation in vivo. The Rhea-based annotation is appropriate.

**Supporting Evidence:**
- PMID:31699900: "Gcn5 and Esa1 function as histone crotonyltransferases" - experimental demonstration of histone crotonylation
- UniProt: "Catalyzes histone crotonylation"
- PMID:31699900 is also evidence for IDA annotation (Annotation 44)

---

### Annotations 23-40: GO:0005515 protein binding [IPI / PMIDs 10487762, 10911987, 11036083, 12672825, 15045029, 15353583, 15485911, 16429126, 16554755, 20489023, 21179020, 21183953, 21984211, 22020126, 24843044, 37968396]

**Action:** CONSOLIDATE AND RELABEL as KEEP_AS_NON_CORE with more specific interaction terms

**Summary:** ESA1 participates in multiple protein-protein interactions documented by yeast two-hybrid, co-IP, and proteome studies. However, "protein binding" is overly generic and non-informative.

**Rationale:** While the IPI evidence indicates confirmed interactions, the generic "protein binding" term provides no mechanistic information. The actual partners are informative:

Key validated interactions documented in the literature and UniProt:
- **TRA1** (PMID:10487762): ATM-related cofactor and NuA4 subunit
- **ARP4** (PMID:12353039, UniProt): H4-binding regulatory subunit
- **EAF3** (UniProt): NuA4 subunit
- **Histones H3, H4, H2A** (PMID:10911987): Direct substrates

However, IPI annotations with such broad language (just "protein binding") are problematic. Each individual protein binding annotation (26 separate IPI entries) represents one validated interaction, which is valuable, but collectively they dilute the annotation set with low-information content.

**Recommendation Options:**

1. **CONSOLIDATE:** Replace these 26 generic IPI entries with 2-3 specific interaction annotations:
   - "complex assembly" (NuA4 complex formation)
   - More specific substrate binding terms for histones

2. **KEEP_AS_NON_CORE:** Retain all 26 as non-core annotations. They document interaction partners but are non-essential for understanding ESA1 function.

3. **SELECTIVE RETENTION:** Keep only those interactions that provide functional information:
   - ESA1-TRA1 (PMID:10487762): Core complex formation
   - ESA1-ARP4 (PMID:15353583, PMID:12353039): H4 recognition and repair recruitment
   - ESA1-histones (implied by HAT activity) - captured by enzymatic activity terms

**Final Action:** KEEP_AS_NON_CORE - these IPI annotations document real interactions but are redundant with the mechanistic activity annotations. They provide value for network analysis but are not essential for functional annotation. The specific NuA4 complex annotation (GO:0035267) is more informative than the individual protein binding entries.

---

### Annotation 41: GO:0005634 nucleus [NAS / PMID:24843044]

**Action:** ACCEPT (duplicate with IBA - redundant but acceptable)

**Summary:** This is an NAS (literature-based) confirmation that ESA1 localizes to the nucleus. Redundant with Annotation 3 (IBA).

**Rationale:** NAS evidence from PMID:24843044 confirms nucleus localization. Having both IBA and NAS provides independent evidence for this essential localization.

---

### Annotation 42: GO:0006351 DNA-templated transcription [NAS / PMID:24843044]

**Action:** KEEP_AS_NON_CORE (prefer GO:0006357 and GO:0032968)

**Summary:** NAS evidence documents that ESA1 is associated with transcription. However, more specific regulatory annotations are preferred.

**Rationale:** Same issue as Annotation 11. The NAS evidence from PMID:24843044 (Eaf5/7/3 paper) documents transcription association, but ESA1's role is regulatory, not in core transcription machinery.

---

### Annotation 43: GO:0008270 zinc ion binding [RCA / PMID:30358795]

**Action:** UNDECIDED (or REMOVE if not mechanistically relevant)

**Summary:** ESA1 contains a MYST-type zinc finger (C2HC zinc coordination motif). PMID:30358795 addresses the yeast zinc proteome.

**Rationale:** ESA1 does contain a degenerate C2HC MYST zinc finger (UniProt FT: ZN_FING 195..220, ecotype="ECO:0000255|PROSITE-ProRule:PRU01063"). However:
1. The zinc finger in MYST HATs is primarily a structural element, not necessarily a zinc-binding active site
2. The RCA evidence from PMID:30358795 is a broad zinc proteome survey, not mechanistic analysis of ESA1-Zn interaction
3. Zinc coordination in MYST HATs is important for catalytic activity but indirect

**Recommendation:** UNDECIDED. The annotation is likely correct (structural zinc coordination is important for HAT activity), but RCA evidence from a proteome survey is less direct than crystal structure analysis would be. If retained, should note it's a structural zinc, not substrate binding. Could mark as non-core.

---

### Annotation 44: GO:0010867 positive regulation of triglyceride biosynthetic process [IDA / PMID:29765047]

**Action:** KEEP_AS_NON_CORE

**Summary:** ESA1 acetylates PAH1 (phosphatidic acid phosphatase 1), regulating triacylglycerol synthesis. This is a documented function but physiologically peripheral to ESA1's main roles.

**Rationale:** PMID:29765047 ("Tip60-mediated lipin 1 acetylation and ER translocation determine triacylglycerol synthesis rate") demonstrates ESA1-mediated acetylation of PAH1 (yeast lipin homolog) enhancing its ER translocation and fatty acid synthesis. This is real but:
1. ESA1 primarily functions in chromatin/epigenetics/DNA repair
2. Metabolic acetylation is an emerging secondary function
3. The IDA evidence (Li T.Y. et al.) demonstrates mechanism

**Recommendation:** KEEP_AS_NON_CORE. This is a documented but secondary function. Mark as non-core to prioritize epigenetic and repair functions.

---

### Annotation 45: GO:0061733 protein-lysine-acetyltransferase activity [IDA / PMID:29765047]

**Action:** ACCEPT (essentially same as Annotation 20, but with IDA evidence)

**Summary:** This IDA evidence from PMID:29765047 independently confirms protein-lysine-acetyltransferase activity through non-histone substrate (PAH1) acetylation.

**Rationale:** The IDA evidence strengthens this annotation by providing direct experimental documentation of non-histone protein acetylation. Complements the IEA/EC-based inference in Annotation 20.

---

### Annotation 46: GO:0000785 chromatin [IDA / PMID:10911987]

**Action:** ACCEPT (duplicate with IBA - see Annotation 1)

**Summary:** IDA evidence from PMID:10911987 independently confirms chromatin localization/function.

**Rationale:** Multiple evidence codes strengthen important annotations. IDA from "Multiple links between the NuA4 histone acetyltransferase complex and epigenetic control of transcription" is appropriate.

---

### Annotation 47: GO:0003712 transcription coregulator activity [IDA / PMID:31699900]

**Action:** ACCEPT (duplicate with IBA - see Annotation 6)

**Summary:** IDA evidence from PMID:31699900 (histone crotonylation paper) documents transcription coregulator function.

**Rationale:** The crotonylation work demonstrates ESA1's role in regulating histone modifications that control transcription, supporting this annotation.

---

### Annotation 48: GO:0140068 histone crotonyltransferase activity [IDA / PMID:31699900]

**Action:** ACCEPT (duplicate with IEA - see Annotation 22)

**Summary:** IDA evidence from PMID:31699900 directly demonstrates histone crotonylation activity experimentally.

**Rationale:** This is the preferred evidence code (IDA over IEA) for the crotonylation function. PMID:31699900 title: "Gcn5 and Esa1 function as histone crotonyltransferases to regulate crotonylation-dependent transcription."

---

### Annotations 49-50: GO:0035267 NuA4 histone acetyltransferase complex [IDA / PMIDs 15485911, 10911987]

**Action:** ACCEPT (multiple evidence codes - see Annotation 19)

**Summary:** IDA evidence from landmark NuA4 structure and function papers.

**Rationale:** PMID:15485911 and PMID:10911987 are foundational papers demonstrating NuA4 composition and ESA1 as core component. Multiple evidence codes strengthen this critical annotation.

---

### Annotation 51: GO:0006281 DNA repair [IGI / PMID:25628362]

**Action:** ACCEPT (with note - stronger than IEA version)

**Summary:** Genetic interaction evidence (IGI) from PMID:25628362 documents ESA1's requirement for DNA repair.

**Rationale:** IGI evidence documents functional relationship with DNA repair machinery. However, PMID:12353039 (IMP) provides more direct evidence that "Acetylation of histone H4 by Esa1 is required for DNA double-strand break repair."

**Recommendation:** Both IMP and IGI evidence codes for DNA repair are appropriate. IMP from PMID:12353039 might be preferred for directness.

---

### Annotations 52-53: GO:0004402 histone acetyltransferase activity [IDA / PMIDs 17274630]

**Action:** ACCEPT (IDA evidence - see Annotation 2)

**Summary:** IDA evidence from PMID:17274630 ("Nucleosome recognition by the Piccolo NuA4 histone acetyltransferase complex") demonstrates HAT activity experimentally.

**Rationale:** Direct experimental documentation of enzymatic activity. Multiple evidence codes (IBA, IEA, IDA) for this core function strengthen the annotation.

---

### Annotation 54: GO:0000183 rDNA heterochromatin formation [IMP and IGI / PMID:16436512]

**Action:** KEEP_AS_NON_CORE (or MARK_AS_OVER_ANNOTATED)

**Summary:** ESA1 has a role in rDNA silencing/heterochromatin formation. This is documented but appears mechanistically indirect.

**Rationale:** PMID:16436512 ("Distinct roles for the essential MYST family HAT Esa1p in transcriptional silencing") demonstrates ESA1 involvement in rDNA heterochromatin. However:

1. **Mechanistically unclear:** How does a histone acetyltransferase promote heterochromatin formation? This appears paradoxical since H4 acetylation typically promotes euchromatin.
2. **Indirect effect:** The paper discusses "distinct roles" suggesting complexity
3. **Not a primary function:** Core ESA1 functions are transcriptional activation and DNA repair

**UniProt note:** "Distinct roles for the essential MYST family HAT Esa1p in transcriptional silencing" - the fact that Esa1p has "silencing" roles in addition to activation suggests this is a secondary, perhaps indirect function.

**Recommendation:** KEEP_AS_NON_CORE. Real function but not a core ESA1 activity. The annotation needs additional context about how HAT activity promotes heterochromatin, which is counterintuitive.

---

### Annotation 55: GO:0006281 DNA repair [IMP / PMID:12353039]

**Action:** ACCEPT (strongest evidence - see Annotation 9)

**Summary:** IMP evidence from PMID:12353039 directly demonstrates that "Acetylation of histone H4 by Esa1 is required for DNA double-strand break repair."

**Rationale:** This is the strongest direct evidence for DNA repair function. Mutational analysis showing esa1 mutants defective in repair provides IMP-level evidence.

**Supporting Evidence:** "Both pathways require the ESA1 histone acetyl transferase (HAT), which is responsible for acetylating all H4 tail lysines"

---

### Annotation 56: GO:0006354 DNA-templated transcription elongation [IDA and IMP / PMID:15949446]

**Action:** ACCEPT

**Summary:** ESA1 is involved in transcription elongation, documented by both IDA and IMP evidence from PMID:15949446.

**Rationale:** "Dynamic lysine methylation on histone H3 defines the regulatory phase of gene transcription" - discusses interplay of ESA1 acetylation with H3 methylation in transcription elongation.

**Supporting Literature:** PMID:19822662 is even more direct: "NuA4 lysine acetyltransferase Esa1 is targeted to coding regions and stimulates transcription elongation with Gcn5."

---

### Annotation 57: GO:0006357 regulation of transcription by RNA polymerase II [IMP / PMID:11036083]

**Action:** ACCEPT (duplicate - see Annotations 4, 13)

**Summary:** IMP evidence documenting that ESA1 is required for Pol II transcription regulation.

**Rationale:** PMID:11036083 ("The yeast NuA4 and Drosophila MSL complexes contain homologous subunits important for transcription regulation") provides functional evidence for transcription regulation role.

---

### Annotation 58: GO:0010485 histone H4 acetyltransferase activity [IDA / PMID:12110674]

**Action:** ACCEPT (duplicate - see Annotation 15)

**Summary:** IDA evidence from the domain motif paper directly demonstrates H4 acetyltransferase activity.

**Rationale:** PMID:12110674 ("A conserved motif common to the histone acetyltransferase Esa1 and the histone deacetylase Rpd3") identifies the ESA1-RPD3 motif required for HAT activity through mutagenesis studies.

---

### Annotation 59: GO:0016239 positive regulation of macroautophagy [IMP / PMID:22539722]

**Action:** ACCEPT

**Summary:** ESA1 positively regulates autophagy through acetylation of ATG3. IMP evidence from PMID:22539722.

**Rationale:** "Function and molecular mechanism of acetylation in autophagy regulation" - directly demonstrates that ESA1-mediated acetylation of ATG3 controls autophagy through ATG3-ATG8 interaction regulation.

**Supporting Quote:** "Esa1 as a histone acetyltransferase required for autophagy. We further identified the autophagy signaling component Atg3 as a substrate for Esa1. Specifically, acetylation of K19 and K48 of Atg3 regulated autophagy"

**Recommendation:** ACCEPT - this is a legitimate but secondary function. Could mark as non-core.

---

### Annotation 60: GO:0032777 piccolo histone acetyltransferase complex [IDA / PMID:12782659]

**Action:** ACCEPT

**Summary:** ESA1 is a component of the Piccolo-NuA4 complex variant. IDA evidence from PMID:12782659.

**Rationale:** "Yeast enhancer of polycomb defines global Esa1-dependent acetylation of chromatin" - identifies Epl1-containing Piccolo-NuA4 complex as a NuA4 variant.

**Note:** The Piccolo NuA4 and canonical NuA4 are structurally related complexes. Both contain ESA1 as the catalytic subunit. This annotation complements GO:0035267 (NuA4 complex).

---

### Annotation 61: GO:0032968 positive regulation of transcription elongation by RNA polymerase II [IMP and IGI / PMID:19822662]

**Action:** ACCEPT

**Summary:** ESA1 directly stimulates transcription elongation. Both IMP and IGI evidence from PMID:19822662.

**Rationale:** "NuA4 lysine acetyltransferase Esa1 is targeted to coding regions and stimulates transcription elongation with Gcn5."

**Supporting Evidence:** Direct targeting to coding regions with demonstrable elongation stimulation.

**Recommendation:** ACCEPT - this is a more specific and appropriate annotation than the generic "DNA-templated transcription" (Annotation 11).

---

### Annotation 62: GO:0051726 regulation of cell cycle [IMP / PMID:10082517]

**Action:** ACCEPT

**Summary:** ESA1 is essential for cell cycle progression. IMP evidence from PMID:10082517 ("Esa1p is an essential histone acetyltransferase required for cell cycle progression").

**Rationale:** Temperature-sensitive esa1 mutants block at the mitosis/cytokinesis checkpoint, directly demonstrating cell cycle requirement.

**Supporting Quote:** "esa1 mutants succeed in replicating their DNA but fail to proceed normally through mitosis and cytokinesis."

**Note:** This could potentially be more specific as "positive regulation of cell cycle" (GO:0045787) or "mitotic cell cycle" (GO:0000278), but the current annotation is appropriate.

---

## Summary of Curation Actions

### ACCEPT (Core/Essential Annotations) - 27 annotations
1. GO:0000785 chromatin [IBA]
2. GO:0004402 histone acetyltransferase activity [IBA]
3. GO:0005634 nucleus [IBA]
4. GO:0006357 regulation of transcription by RNA polymerase II [IBA]
5. GO:0003712 transcription coregulator activity [IBA]
6. GO:0004402 histone acetyltransferase activity [IEA]
7. GO:0006281 DNA repair [IEA]
8. GO:0006325 chromatin organization [IEA]
9. GO:0006355 regulation of DNA-templated transcription [IEA]
10. GO:0006357 regulation of transcription by RNA polymerase II [IEA]
11. GO:0006974 DNA damage response [IEA]
12. GO:0010485 histone H4 acetyltransferase activity [IEA]
13. GO:0061733 protein-lysine-acetyltransferase activity [IEA]
14. GO:0140064 peptide crotonyltransferase activity [IEA]
15. GO:0035267 NuA4 histone acetyltransferase complex [IEA]
16. GO:0005634 nucleus [NAS]
17. GO:0000785 chromatin [IDA]
18. GO:0003712 transcription coregulator activity [IDA]
19. GO:0140068 histone crotonyltransferase activity [IDA]
20. GO:0035267 NuA4 histone acetyltransferase complex [IDA - 2 entries]
21. GO:0006281 DNA repair [IGI]
22. GO:0004402 histone acetyltransferase activity [IDA]
23. GO:0006281 DNA repair [IMP]
24. GO:0006354 DNA-templated transcription elongation [IDA, IMP]
25. GO:0006357 regulation of transcription by RNA polymerase II [IMP]
26. GO:0010485 histone H4 acetyltransferase activity [IDA]
27. GO:0032968 positive regulation of transcription elongation by RNA polymerase II [IMP, IGI]
28. GO:0051726 regulation of cell cycle [IMP]
29. GO:0061733 protein-lysine-acetyltransferase activity [IDA]

### REMOVE (Contradicted or Uninformative) - 1 annotation
1. GO:0010629 negative regulation of gene expression [IEA] - **REMOVE** - ESA1/NuA4 is a positive regulator, not negative

### KEEP_AS_NON_CORE (Valid but Secondary Functions) - 8 annotations
1. GO:0005515 protein binding [IPI - 26 entries] - valid but overly generic
2. GO:0016740 transferase activity [IEA] - generic ancestor term
3. GO:0033554 cellular response to stress [IEA] - generic, specific stress annotations preferred
4. GO:0006351 DNA-templated transcription [IEA, NAS] - prefer more specific regulatory terms
5. GO:0010867 positive regulation of triglyceride biosynthetic process [IDA] - secondary metabolic function
6. GO:0016239 positive regulation of macroautophagy [IMP] - secondary cellular function
7. GO:0000183 rDNA heterochromatin formation [IMP, IGI] - mechanistically unclear, indirect function
8. GO:0008270 zinc ion binding [RCA] - structural, not directly functional; evidence is broad survey

### MODIFY (Better Terms Exist) - 1 annotation
1. GO:0003682 chromatin binding [IBA] - redundant with nucleosome recognition and HAT activity

### UNDECIDED (Insufficient Evidence) - 1 annotation
1. GO:0106226 peptide 2-hydroxyisobutyryltransferase activity [IEA] - ortholog-based only, no experimental evidence for yeast

---

## Recommended Annotation Set (Tier 1 - Core Functions)

For display and prioritization, ESA1's core annotations should emphasize:

### Molecular Function (most informative)
1. GO:0010485 histone H4 acetyltransferase activity [IDA/IEA]
2. GO:0140068 histone crotonyltransferase activity [IDA]
3. GO:0061733 protein-lysine-acetyltransferase activity [IDA/IEA]
4. GO:0003712 transcription coregulator activity [IBA/IDA]

### Biological Process (primary roles)
1. GO:0006357 regulation of transcription by RNA polymerase II [IBA/IEA/IMP]
2. GO:0032968 positive regulation of transcription elongation by RNA polymerase II [IMP/IGI]
3. GO:0006281 DNA repair [IMP/IEA]
4. GO:0006974 DNA damage response [IEA]
5. GO:0051726 regulation of cell cycle [IMP]

### Cellular Component
1. GO:0035267 NuA4 histone acetyltransferase complex [IDA/IEA]
2. GO:0005634 nucleus [IBA/NAS]
3. GO:0000785 chromatin [IBA/IDA]

---

## Literature Integration

The comprehensive review integrates findings from:

### Primary Evidence (Direct ESA1 Function)
- **PMID:10487762**: NuA4 complex identification and H4 HAT activity
- **PMID:10082517**: Cell cycle requirement and essentiality
- **PMID:12353039**: H4 acetylation requirement for DSB repair
- **PMID:10911987**: Chromatin interaction and transcriptional control
- **PMID:19822662**: Coding region targeting and elongation stimulation
- **PMID:31699900**: Histone crotonylation function

### Secondary/Emerging Functions
- **PMID:22539722**: Autophagy regulation via ATG3 acetylation
- **PMID:29765047**: PAH1 acetylation and fatty acid synthesis
- **PMID:16436512**: rDNA silencing roles

### Structural/Mechanistic Basis
- **PMID:12110674**: ESA1-RPD3 domain motif required for HAT activity
- **PMID:22020126**: Lysine autoacetylation requirement for catalysis
- **PMID:17223684, PMID:18245364**: Catalytic mechanism and active site architecture

---

## Curation Principles Applied

1. **Mechanistic Clarity**: Prioritized specific enzymatic activities over generic terms
2. **Evidence Quality**: Preferred experimental evidence (IDA/IMP/IGI) over computational (IEA)
3. **Functional Accuracy**: Removed contradictory annotations (negative regulation) and disambiguated regulatory vs. core machinery roles
4. **Substrate Specificity**: Captured H4-preferential and emerging non-histone substrate functions
5. **Process Hierarchy**: Distinguished between ESA1's regulatory role vs. core transcriptional/cell cycle processes

---

## Remaining Questions for Further Investigation

1. **Heterochromatin Formation Mechanism**: How does H4 acetylation promote rDNA heterochromatin formation (GO:0000183)? Apparent paradox with ESA1's role as activator.

2. **Cell Cycle Specificity**: Is ESA1 activity cell cycle-regulated? Does S-phase-specific H3K56 acetylation require ESA1 or only Gcn5?

3. **H3K56 Acetylation**: Why not included in existing annotations despite being documented in literature? Is this covered by "chromatin organization" or should be explicit?

4. **Alternative Acyl-CoA Substrates**: What is the biological relevance of 2-hydroxyisobutyrylation and crotonylation? Are these in vivo modifications or primarily in vitro?

5. **Regulatory Complexity**: Are there genes where ESA1/NuA4 acts as a negative regulator? How common are the rDNA silencing functions?

