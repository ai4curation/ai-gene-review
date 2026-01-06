# C. elegans Ciliopathy Project - Curation Recommendations

## Summary

**Total Genes Reviewed:** 20
**Total Annotations:** 477
**ACCEPT (Publication-Ready):** 368
**Changes Recommended:** 109

## Summary Table

| Gene | Priority | Total | ACCEPT | MODIFY | REMOVE | NEW | Other | Changes |
|------|----------|-------|--------|--------|--------|-----|-------|---------|
| daf-19 | P1 | 17 | 13 | 1 | 0 | 1 | 2 | 4 🟡 |
| osm-3 | P1 | 47 | 38 | 4 | 0 | 0 | 5 | 9 🔴 |
| osm-5 | P1 | 23 | 18 | 0 | 1 | 0 | 4 | 5 🔴 |
| che-2 | P1 | 21 | 11 | 1 | 0 | 1 | 8 | 10 🔴 |
| che-3 | P1 | 33 | 25 | 1 | 2 | 0 | 5 | 8 🔴 |
| bbs-1 | P1 | 22 | 17 | 1 | 3 | 0 | 1 | 5 🔴 |
| bbs-8 | P1 | 28 | 22 | 3 | 0 | 1 | 2 | 6 🔴 |
| mks-3 | P1 | 10 | 6 | 0 | 0 | 4 | 0 | 4 🟡 |
| nphp-1 | P2 | 17 | 12 | 2 | 0 | 0 | 3 | 5 🔴 |
| nphp-4 | P2 | 30 | 20 | 1 | 0 | 0 | 9 | 10 🔴 |
| mks-1 | P2 | 6 | 2 | 1 | 0 | 2 | 1 | 4 🟡 |
| mks-5 | P2 | 24 | 20 | 0 | 0 | 1 | 3 | 4 🟡 |
| mks-6 | P2 | 11 | 11 | 0 | 0 | 0 | 0 | 0 ✅ |
| mksr-2 | P2 | 17 | 9 | 3 | 0 | 0 | 5 | 8 🔴 |
| bbs-2 | P3 | 20 | 14 | 2 | 0 | 3 | 1 | 6 🔴 |
| bbs-5 | P3 | 17 | 14 | 1 | 0 | 0 | 2 | 3 🟡 |
| bbs-7 | P3 | 24 | 20 | 2 | 0 | 0 | 2 | 4 🟡 |
| lov-1 | P3 | 30 | 25 | 5 | 0 | 0 | 0 | 5 🔴 |
| pkd-2 | P3 | 60 | 60 | 0 | 0 | 0 | 0 | 0 ✅ |
| pef-1 | P3 | 20 | 11 | 1 | 2 | 3 | 3 | 9 🔴 |

## Status Key

- **✅ Publication-Ready:** All annotations ACCEPT (no changes needed)
- **🟡 Review-Ready:** 1-4 changes needed (minor consolidation)
- **🔴 Implementation-Needed:** 5+ changes needed (systematic review required)

## Gene-by-Gene Curation Recommendations

### DAF-19 🟡

**Total Annotations:** 17 | **Changes:** 4

#### MODIFY: GO:0010468 - regulation of gene expression
- **Evidence:** IMP
- **Issue:** While accurate, this annotation is quite general. DAF-19's primary role is as a transcriptional activator of ciliary gene expression. A more specific 
- **Proposed:** GO:0045724 - positive regulation of cilium assembly

#### KEEP_AS_NON_CORE: GO:0050829 - defense response to Gram-negative bacterium
- **Evidence:** IMP
- **Issue:** This is a legitimate function of DAF-19 supported by experimental evidence, but it represents a secondary/pleiotropic role rather than its core functi

#### KEEP_AS_NON_CORE: GO:0042427 - serotonin biosynthetic process
- **Evidence:** IMP
- **Issue:** This annotation reflects DAF-19's role in regulating serotonin biosynthesis through transcriptional control of tph-1. However, this is a secondary fun

#### NEW: GO:0045724 - positive regulation of cilium assembly
- **Evidence:** IMP
- **Issue:** This annotation is strongly supported by the literature and represents DAF-19's central role in ciliogenesis. This biological process annotation captu

### OSM-3 🔴

**Total Annotations:** 47 | **Changes:** 9

#### MODIFY: GO:0030030 - cell projection organization
- **Evidence:** IBA
- **Issue:** While technically accurate, this term is too general. OSM-3 has a specific role in cilium organization, not cell projections broadly.
- **Proposed:** GO:0060271 - cilium assembly
- **Proposed:** GO:1905515 - non-motile cilium assembly

#### MODIFY: GO:0005815 - microtubule organizing center
- **Evidence:** IBA
- **Issue:** While basal bodies are MTOCs, the more precise term for OSM-3 localization is ciliary basal body, which is experimentally validated.
- **Proposed:** GO:0036064 - ciliary basal body

#### MARK_AS_OVER_ANNOTATED: GO:0098971 - anterograde dendritic transport of neurotransmitter receptor complex
- **Evidence:** IBA
- **Issue:** This function is established for mammalian KIF17 but not demonstrated for C. elegans OSM-3. OSM-3 is specifically involved in ciliary transport, not g

#### MODIFY: GO:0007018 - microtubule-based movement
- **Evidence:** IEA
- **Issue:** While accurate, a more specific term exists for OSM-3's biological process.
- **Proposed:** GO:0035720 - intraciliary anterograde transport

#### MODIFY: GO:0032991 - protein-containing complex
- **Evidence:** IEA
- **Issue:** Too general. OSM-3 specifically forms kinesin complexes.
- **Proposed:** GO:0005871 - kinesin complex

#### UNDECIDED: GO:1902856 - negative regulation of non-motile cilium assembly
- **Evidence:** IGI
- **Issue:** The relationship between OSM-3 and negative regulation of cilium assembly is indirect and context-dependent (dyf-5 mutant background). OSM-3 primarily

#### KEEP_AS_NON_CORE: GO:0061066 - positive regulation of dauer larval development
- **Evidence:** IMP
- **Issue:** Dauer phenotype is secondary to ciliary defects. OSM-3 mutants have defective sensory cilia which impairs pheromone sensing required for dauer decisio

#### KEEP_AS_NON_CORE: GO:0043053 - dauer entry
- **Evidence:** IGI
- **Issue:** Dauer phenotype is secondary to ciliary defects. OSM-3's role in dauer is indirect through its effects on sensory cilia function.

#### MARK_AS_OVER_ANNOTATED: GO:0046626 - regulation of insulin receptor signaling pathway
- **Evidence:** IGI
- **Issue:** The connection to insulin signaling is indirect. OSM-3 mutations cause ciliary defects that affect sensory neuron function. Sensory neurons in turn re

### OSM-5 🔴

**Total Annotations:** 23 | **Changes:** 5

#### KEEP_AS_NON_CORE: GO:0006970 - response to osmotic stress
- **Evidence:** IMP
- **Issue:** The osmotic avoidance defect is a downstream consequence of defective sensory cilia, not a direct molecular function of OSM-5. The gene name "osm" der

#### KEEP_AS_NON_CORE: GO:0035641 - locomotory exploration behavior
- **Evidence:** IMP
- **Issue:** Exploration behavior is influenced by sensory input from ciliated neurons. The behavioral defect in osm-5 mutants is secondary to ciliary dysfunction,

#### KEEP_AS_NON_CORE: GO:0050921 - positive regulation of chemotaxis
- **Evidence:** IMP
- **Issue:** The chemotaxis defect in osm-5 mutants results from defective sensory cilia that cannot properly detect chemical signals. OSM-5 does not directly regu

#### KEEP_AS_NON_CORE: GO:0043053 - dauer entry
- **Evidence:** IGI
- **Issue:** Dauer entry requires functional chemosensory cilia to detect pheromone signals. osm-5 mutants fail to form dauers properly because they cannot sense t

#### REMOVE: GO:0003674 - molecular_function
- **Evidence:** ND
- **Issue:** This ND annotation is outdated. OSM-5 has established molecular functions including its role as an IFT-B structural component and kinesin binding. The

### CHE-2 🔴

**Total Annotations:** 21 | **Changes:** 10

#### MODIFY: GO:0042073 - intraciliary transport
- **Evidence:** NAS
- **Issue:** The annotation is correct but could be more specific. CHE-2/IFT80 is primarily involved in anterograde transport as part of the IFT-B complex. Conside
- **Proposed:** GO:0035720 - intraciliary anterograde transport

#### KEEP_AS_NON_CORE: GO:0090325 - regulation of locomotion involved in locomotory behavior
- **Evidence:** IGI
- **Issue:** This is a downstream consequence of cilium structure defects rather than a direct function of CHE-2. The effect on locomotion is indirect, mediated th

#### KEEP_AS_NON_CORE: GO:0090326 - positive regulation of locomotion involved in locomotory behavior
- **Evidence:** IMP
- **Issue:** Pleiotropic effect of cilium defects. CHE-2's primary role is in cilium assembly and IFT; the locomotory phenotype is an indirect consequence of senso

#### KEEP_AS_NON_CORE: GO:0040014 - regulation of multicellular organism growth
- **Evidence:** IGI
- **Issue:** Secondary phenotype resulting from defective sensory cilia. The primary function of CHE-2 is cilium assembly, not growth regulation per se.

#### KEEP_AS_NON_CORE: GO:0040018 - positive regulation of multicellular organism growth
- **Evidence:** IMP
- **Issue:** Indirect effect of cilium structure defects on sensory-mediated growth regulation. Not a direct molecular function of CHE-2.

#### KEEP_AS_NON_CORE: GO:0006935 - chemotaxis
- **Evidence:** IMP
- **Issue:** Chemotaxis defect is a consequence of abnormal cilium structure in sensory neurons. CHE-2 enables chemotaxis indirectly by being required for proper c

#### KEEP_AS_NON_CORE: GO:0040024 - dauer larval development
- **Evidence:** IGI
- **Issue:** Dauer development phenotype is secondary to cilium structure defects. che-2 mutants affect dauer formation because sensory cilia are required for envi

#### MARK_AS_OVER_ANNOTATED: GO:0030512 - negative regulation of transforming growth factor beta receptor signaling pathway
- **Evidence:** IGI
- **Issue:** This is an indirect effect mediated through cilium structure defects affecting sensory perception of environmental cues that regulate TGF-beta signali

#### KEEP_AS_NON_CORE: GO:0006935 - chemotaxis
- **Evidence:** IMP
- **Issue:** Chemotaxis defect is downstream of cilium structure defect. CHE-2 is required for cilium assembly in chemosensory neurons; without proper cilia, these

#### NEW: GO:0035720 - intraciliary anterograde transport
- **Evidence:** IBA
- **Issue:** More specific than GO:0042073 (intraciliary transport). IFT-B is specifically the anterograde transport machinery while IFT-A is retrograde. This term

### CHE-3 🔴

**Total Annotations:** 33 | **Changes:** 8

#### REMOVE: GO:0060294 - cilium movement involved in cell motility
- **Evidence:** IBA
- **Issue:** C. elegans sensory cilia are non-motile primary cilia-like structures (PMID:10790327). CHE-3 functions in retrograde IFT, not in ciliary motility. Thi

#### REMOVE: GO:0097729 - 9+2 motile cilium
- **Evidence:** IBA
- **Issue:** CHE-3 is localized to non-motile sensory cilia in C. elegans (PMID:10790327). The annotation to 9+2 motile cilium is incorrect for this species. The I

#### KEEP_AS_NON_CORE: GO:0050793 - regulation of developmental process
- **Evidence:** IEA
- **Issue:** The annotation is not incorrect but represents downstream phenotypic effects rather than core function. CHE-3's role in development is indirect, media

#### KEEP_AS_NON_CORE: GO:0043053 - dauer entry
- **Evidence:** IGI
- **Issue:** The annotation reflects real genetic data but represents an indirect effect of ciliary defects on chemosensory-dependent dauer signaling (PMID:1732156

#### KEEP_AS_NON_CORE: GO:0061066 - positive regulation of dauer larval development
- **Evidence:** IMP
- **Issue:** The phenotype is real but represents an indirect consequence of ciliary defects disrupting chemosensory signaling required for normal dauer induction.

#### MARK_AS_OVER_ANNOTATED: GO:0030512 - negative regulation of transforming growth factor beta receptor signaling pathway
- **Evidence:** IGI
- **Issue:** The genetic interaction is real but the annotation implies a more direct role in TGF-beta signaling than warranted. CHE-3's effect on TGF-beta signali

#### MODIFY: GO:0008104 - intracellular protein localization
- **Evidence:** IMP
- **Issue:** While not incorrect, the term is too general. CHE-3's role is specifically in retrograde IFT, which is a specialized form of intracellular transport. 
- **Proposed:** GO:0035721 - intraciliary retrograde transport

#### KEEP_AS_NON_CORE: GO:0007635 - chemosensory behavior
- **Evidence:** IMP
- **Issue:** The phenotype is well-documented but represents an indirect consequence of ciliary defects. CHE-3 does not directly participate in chemosensory signal

### BBS-1 🔴

**Total Annotations:** 22 | **Changes:** 5

#### MODIFY: GO:0005813 - centrosome
- **Evidence:** IBA
- **Issue:** In C. elegans, BBS-1 localizes predominantly to the ciliary base/basal body rather than a classical centrosome structure. The more accurate term would
- **Proposed:** GO:0036064 - ciliary basal body

#### REMOVE: GO:0005113 - patched binding
- **Evidence:** IBA
- **Issue:** C. elegans lacks Smoothened and canonical Hedgehog signaling. While C. elegans has Patched homologs (PTC-1, PTC-3), these have diverged functionally a

#### REMOVE: GO:0005119 - smoothened binding
- **Evidence:** IBA
- **Issue:** C. elegans lacks Smoothened entirely - the gene is absent from the genome. This is a well-documented evolutionary divergence of the Hedgehog signaling

#### REMOVE: GO:0003674 - molecular_function
- **Evidence:** ND
- **Issue:** This ND annotation is outdated. The gene now has IBA molecular function annotations (though the patched/smoothened binding ones are not valid for C. e

#### KEEP_AS_NON_CORE: GO:0043005 - neuron projection
- **Evidence:** IDA
- **Issue:** While technically correct that BBS-1 localizes to neuronal projections (specifically ciliated dendrites of sensory neurons), the more informative anno

### BBS-8 🔴

**Total Annotations:** 28 | **Changes:** 6

#### MODIFY: GO:0015031 - protein transport
- **Evidence:** IEA
- **Issue:** Correct but overly general. BBS-8 specifically functions in ciliary protein transport via IFT. A more specific term would better capture the actual fu
- **Proposed:** GO:0042073 - intraciliary transport

#### MODIFY: GO:0030030 - cell projection organization
- **Evidence:** IEA
- **Issue:** Overly general. The more specific term "cilium assembly" (GO:0060271) or "non-motile cilium assembly" (GO:1905515) would be more appropriate and is al
- **Proposed:** GO:0060271 - cilium assembly

#### MODIFY: GO:1904107 - protein localization to microvillus membrane
- **Evidence:** IMP
- **Issue:** The finger compartment of AFD neurons contains microvilli-like protrusions, but these are functionally a specialized ciliary signaling compartment. Th
- **Proposed:** GO:0061512 - protein localization to cilium

#### KEEP_AS_NON_CORE: GO:0008355 - olfactory learning
- **Evidence:** IMP
- **Issue:** This is a downstream phenotype rather than a direct function. BBS genes are required for AWC(ON) neuron function, and defects in this neuron lead to i

#### KEEP_AS_NON_CORE: GO:0006935 - chemotaxis
- **Evidence:** IMP
- **Issue:** This is a downstream phenotype resulting from ciliary sensory defects, not a direct molecular function of BBS-8. Chemotaxis defects are a consequence 

#### NEW: GO:0060090 - molecular adaptor activity
- **Evidence:** ISS
- **Issue:** This molecular function annotation is proposed based on the structural role of BBS-8 within the BBSome. The protein contains 7-8 TPR repeats (UniProt)

### MKS-3 🟡

**Total Annotations:** 10 | **Changes:** 4

#### NEW: GO:1905349 - ciliary transition zone assembly
- **Evidence:** IGI
- **Issue:** This annotation captures the role of MKS-3 in transition zone organization, which is distinct from but related to its localization there. The TEM stud

#### NEW: GO:1903565 - negative regulation of protein localization to cilium
- **Evidence:** IMP
- **Issue:** This is a critical annotation capturing the ciliary gate function of MKS-3. The paper directly demonstrates that TZ proteins including those in the MK

#### NEW: GO:0007635 - chemosensory behavior
- **Evidence:** IMP
- **Issue:** This annotation captures the physiological/behavioral consequence of MKS-3 function in sensory cilia. The osmotic avoidance assay tests chemosensory b

#### NEW: GO:0005198 - structural molecule activity
- **Evidence:** IDA
- **Issue:** This molecular function annotation captures MKS-3's role as a structural component of the MKS complex. Evidence shows MKS-3 is part of the TZ architec

### NPHP-1 🔴

**Total Annotations:** 17 | **Changes:** 5

#### KEEP_AS_NON_CORE: GO:0005737 - cytoplasm
- **Evidence:** IBA
- **Issue:** The annotation is not incorrect but does not represent the core localization of NPHP-1. The protein's critical function is at the transition zone. Cyt

#### UNDECIDED: GO:0090251 - protein localization involved in establishment of planar polarity
- **Evidence:** IBA
- **Issue:** While this may be a conserved function based on phylogenetic analysis, there is no direct experimental evidence for a role in planar polarity in C. el

#### MODIFY: GO:0036064 - ciliary basal body
- **Evidence:** IDA
- **Issue:** In C. elegans, the basal body and transition zone are distinct regions. Multiple detailed studies using GFP-tagged NPHP-1 show specific localization t
- **Proposed:** GO:0035869 - ciliary transition zone

#### KEEP_AS_NON_CORE: GO:0008340 - determination of adult lifespan
- **Evidence:** IMP
- **Issue:** This is a pleiotropic phenotype likely resulting from disrupted ciliary function affecting sensory signaling pathways that regulate lifespan (insulin/

#### MODIFY: GO:0008104 - intracellular protein localization
- **Evidence:** IGI
- **Issue:** This annotation is too general. NPHP-1 specifically functions at the TZ to regulate ciliary access of IFT components and other proteins. A more specif
- **Proposed:** GO:0035721 - intraciliary transport involved in cilium assembly

### NPHP-4 🔴

**Total Annotations:** 30 | **Changes:** 10

#### KEEP_AS_NON_CORE: GO:0090090 - negative regulation of canonical Wnt signaling pathway
- **Evidence:** IBA
- **Issue:** While human NPHP4 has been linked to Wnt signaling regulation and TZ proteins can modulate ciliary signaling, the core function of C. elegans NPHP-4 i

#### MARK_AS_OVER_ANNOTATED: GO:0005856 - cytoskeleton
- **Evidence:** IEA
- **Issue:** While technically not wrong (cilia are cytoskeletal structures), this is too broad and uninformative. The more specific ciliary component annotations 

#### KEEP_AS_NON_CORE: GO:0090090 - negative regulation of canonical Wnt signaling pathway
- **Evidence:** IEA
- **Issue:** Duplicate annotation by different method. The Wnt signaling role is likely secondary to core ciliary gating function.

#### KEEP_AS_NON_CORE: GO:0016358 - dendrite development
- **Evidence:** IGI
- **Issue:** The primary function is in cilia, but dendrite development is affected in double mutants with MKS module genes, likely as a secondary consequence of T

#### KEEP_AS_NON_CORE: GO:0023041 - neuronal signal transduction
- **Evidence:** IC
- **Issue:** While NPHP-4 is required for sensory neuron function, the primary defect is in ciliary structure/gating rather than direct signal transduction. The be

#### KEEP_AS_NON_CORE: GO:0034606 - response to hermaphrodite contact
- **Evidence:** IGI
- **Issue:** Behavioral phenotype that reflects ciliary sensory function rather than core molecular function. Important for understanding organismal role but secon

#### KEEP_AS_NON_CORE: GO:0034607 - turning behavior involved in mating
- **Evidence:** IGI
- **Issue:** Male-specific sensory behavior dependent on ciliary function. Secondary phenotype reflecting ciliary gating defects.

#### KEEP_AS_NON_CORE: GO:0008340 - determination of adult lifespan
- **Evidence:** IMP
- **Issue:** Pleiotropic phenotype that may result from altered ciliary signaling. Not a core function of NPHP-4 but represents downstream physiological consequenc

#### MODIFY: GO:0008104 - intracellular protein localization
- **Evidence:** IGI
- **Issue:** This is too broad. The annotation should more specifically reflect the role in regulating ciliary access and localization of specific IFT components.
- **Proposed:** GO:0072638 - intraciliary transport
- **Proposed:** GO:1904491 - protein localization to ciliary transition zone

#### KEEP_AS_NON_CORE: GO:0035177 - larval foraging behavior
- **Evidence:** IMP
- **Issue:** Behavioral phenotype reflecting sensory function. The foraging defect is likely due to chemosensory impairment from ciliary dysfunction rather than a 

### MKS-1 🟡

**Total Annotations:** 6 | **Changes:** 4

#### MODIFY: GO:0005929 - cilium
- **Evidence:** IEA
- **Issue:** The annotation is not incorrect since the transition zone is part of the cilium, but it is too general. MKS-1 specifically localizes to the ciliary tr
- **Proposed:** GO:0035869 - ciliary transition zone

#### MARK_AS_OVER_ANNOTATED: GO:0030030 - cell projection organization
- **Evidence:** IEA
- **Issue:** This term is too general. The more specific GO:0060271 (cilium assembly) annotation is already present and better captures the actual function of MKS-

#### NEW: GO:0035869 - ciliary transition zone
- **Evidence:** IDA
- **Issue:** Multiple publications directly demonstrate that MKS-1 localizes to the transition zone in C. elegans sensory neurons. This is a core annotation that a

#### NEW: GO:1905349 - ciliary transition zone assembly
- **Evidence:** IMP
- **Issue:** MKS-1 contributes to transition zone assembly as part of the MKS module. The function is only revealed in combination with NPHP mutations due to redun

### MKS-5 🟡

**Total Annotations:** 24 | **Changes:** 4

#### MARK_AS_OVER_ANNOTATED: GO:0005856 - cytoskeleton
- **Evidence:** IEA
- **Issue:** While cilia are cytoskeleton-related structures, this annotation is overly broad and uninformative. The specific localization to the ciliary transitio

#### MARK_AS_OVER_ANNOTATED: GO:0030030 - cell projection organization
- **Evidence:** IEA
- **Issue:** This IEA based on UniProt keyword mapping is too broad. The specific terms GO:0060271 (cilium assembly) and GO:1905515 (non-motile cilium assembly) be

#### KEEP_AS_NON_CORE: GO:0006935 - chemotaxis
- **Evidence:** IMP
- **Issue:** Chemotaxis is a downstream phenotype of ciliary dysfunction rather than a direct molecular function of MKS-5. The chemosensory defects arise as a cons

#### NEW: GO:0060090 - molecular adaptor activity
- **Evidence:** IMP
- **Issue:** This molecular function annotation is supported by extensive evidence from multiple studies. Williams et al. 2011 established MKS-5 as a central compo

### MKSR-2 🔴

**Total Annotations:** 17 | **Changes:** 8

#### MODIFY: GO:0060271 - cilium assembly
- **Evidence:** IBA
- **Issue:** While MKSR-2 is involved in cilium assembly, the annotation should be more specific. In C. elegans sensory neurons, these are non-motile primary cilia
- **Proposed:** GO:1905515 - non-motile cilium assembly

#### MODIFY: GO:0005929 - cilium
- **Evidence:** IEA
- **Issue:** MKSR-2 specifically localizes to the ciliary transition zone, not the cilium proper. The IEA annotation is too broad. The protein is found at the base
- **Proposed:** GO:0035869 - ciliary transition zone

#### MARK_AS_OVER_ANNOTATED: GO:0005515 - protein binding
- **Evidence:** IPI
- **Issue:** The term 'protein binding' (GO:0005515) is too generic and uninformative per GO curation guidelines. The interaction with MKSR-1 is biologically relev

#### MARK_AS_OVER_ANNOTATED: GO:0005515 - protein binding
- **Evidence:** IPI
- **Issue:** Same as above - 'protein binding' is too generic. The interaction data is valid but better captured by the MKS complex component annotation.

#### KEEP_AS_NON_CORE: GO:0008340 - determination of adult lifespan
- **Evidence:** IGI
- **Issue:** This is a secondary phenotype arising from ciliary dysfunction rather than a direct core function of MKSR-2. The lifespan extension in mutants results

#### MARK_AS_OVER_ANNOTATED: GO:0005515 - protein binding
- **Evidence:** IPI
- **Issue:** Same issue as other protein binding annotations - the term is too generic. The interaction with MKS-1 is biologically meaningful (they form the B9/MKS

#### MODIFY: GO:0008104 - intracellular protein localization
- **Evidence:** IMP
- **Issue:** This term is too generic. MKSR-2 specifically functions in localizing proteins to the ciliary transition zone. The more specific term GO:1904491 (prot
- **Proposed:** GO:1904491 - protein localization to ciliary transition zone

#### KEEP_AS_NON_CORE: GO:0035177 - larval foraging behavior
- **Evidence:** IGI
- **Issue:** Foraging behavior defects are a downstream consequence of sensory cilium dysfunction. C. elegans uses ciliated sensory neurons for chemosensation, whi

### BBS-2 🔴

**Total Annotations:** 20 | **Changes:** 6

#### MARK_AS_OVER_ANNOTATED: GO:0016020 - membrane
- **Evidence:** IBA
- **Issue:** While the BBSome is involved in membrane protein trafficking to cilia, this generic 'membrane' annotation is too broad to be informative. The protein 

#### MODIFY: GO:0031514 - motile cilium
- **Evidence:** IBA
- **Issue:** C. elegans cilia are sensory (non-motile) cilia, not motile cilia. The organism lacks motile cilia entirely - its sensory neurons have non-motile cili
- **Proposed:** GO:0097730 - non-motile cilium

#### MODIFY: GO:0015031 - protein transport
- **Evidence:** IEA
- **Issue:** While BBS-2 is involved in protein transport, this term is too general. The BBSome specifically functions in ciliary protein trafficking - sorting mem
- **Proposed:** GO:0042073 - intraciliary transport

#### NEW: GO:0042073 - intraciliary transport
- **Evidence:** IDA
- **Issue:** This is a core function annotation that should be added. PMID:22922713 provides definitive evidence that the BBSome controls IFT assembly and turnarou

#### NEW: GO:0035735 - intraciliary transport involved in cilium assembly
- **Evidence:** IMP
- **Issue:** This annotation links the BBSome's IFT function directly to cilium assembly. PMID:22922713 demonstrates that disruption of BBSome-IFT coupling leads t

#### NEW: GO:0005198 - structural molecule activity
- **Evidence:** IDA
- **Issue:** BBS-2 is a core structural component of the BBSome complex. PMID:22922713 demonstrates that BBS proteins form a complex using BiFC assays. The BBSome 

### BBS-5 🟡

**Total Annotations:** 17 | **Changes:** 3

#### MODIFY: GO:0015031 - protein transport
- **Evidence:** IEA
- **Issue:** While protein transport is accurate, a more specific term reflecting the ciliary transport function would be more informative. The annotation should b
- **Proposed:** GO:0035735 - intraciliary transport involved in cilium assembly
- **Proposed:** GO:0042073 - intraciliary transport

#### KEEP_AS_NON_CORE: GO:0030030 - cell projection organization
- **Evidence:** IEA
- **Issue:** This is a general parent term of cilium assembly. While not incorrect, it is less informative than the specific cilium assembly annotation. Keeping as

#### UNDECIDED: GO:0034451 - centriolar satellite
- **Evidence:** IEA
- **Issue:** While human BBS5 localizes to centriolar satellites, it is unclear if this is a significant localization for C. elegans BBS-5. The UniProt record note

### BBS-7 🟡

**Total Annotations:** 24 | **Changes:** 4

#### MODIFY: GO:0008104 - intracellular protein localization
- **Evidence:** IBA
- **Issue:** While the annotation captures BBS-7's role in protein localization, this term is too general. The more specific function is ciliary protein localizati
- **Proposed:** GO:0061512 - protein localization to cilium

#### MODIFY: GO:0016020 - membrane
- **Evidence:** IBA
- **Issue:** The term 'membrane' is too general for BBS-7 localization. BBS-7 specifically localizes to the ciliary membrane system and is involved in ciliary memb
- **Proposed:** GO:0005929 - cilium

#### KEEP_AS_NON_CORE: GO:1904107 - protein localization to microvillus membrane
- **Evidence:** IMP
- **Issue:** This is a specialized function in AFD thermosensory neurons rather than a core function. While experimentally validated, it represents a specific neur

#### KEEP_AS_NON_CORE: GO:0006935 - chemotaxis
- **Evidence:** IMP
- **Issue:** Secondary phenotype. Chemotaxis defects are a consequence of ciliary dysfunction rather than a direct molecular function of BBS-7. BBS-7's core functi

### LOV-1 🔴

**Total Annotations:** 30 | **Changes:** 5

#### MODIFY: GO:0005262 - calcium channel activity
- **Evidence:** IBA
- **Issue:** LOV-1 is a PC1-family member that partners with the TRPP channel PKD-2. The channel activity likely resides primarily in PKD-2, while LOV-1 functions 
- **Proposed:** GO:0015276 - ligand-gated ion channel activity

#### MODIFY: GO:0070588 - calcium ion transmembrane transport
- **Evidence:** IEA
- **Issue:** LOV-1 is part of a receptor-channel complex with PKD-2. The transport activity is more directly attributable to PKD-2. LOV-1's role is as a receptor/r
- **Proposed:** GO:0010959 - regulation of metal ion transport

#### MODIFY: GO:0005515 - protein binding
- **Evidence:** IPI
- **Issue:** The generic "protein binding" annotation is uninformative. LOV-1 interacts with ATP-2 via its PLAT domain, which should be captured with a more specif
- **Proposed:** GO:0019904 - protein domain specific binding

#### MODIFY: GO:0005515 - protein binding
- **Evidence:** IPI
- **Issue:** Generic "protein binding" is uninformative. The interaction with KIN-10 (casein kinase II regulatory subunit) is through the LOV-1 C-terminus. A more 
- **Proposed:** GO:0019904 - protein domain specific binding

#### MODIFY: GO:0005515 - protein binding
- **Evidence:** IPI
- **Issue:** This is a less informative duplicate of the protein domain specific binding annotation (GO:0019904) from the same reference. The interaction with STAM
- **Proposed:** GO:0019904 - protein domain specific binding

### PEF-1 🔴

**Total Annotations:** 20 | **Changes:** 9

#### REMOVE: GO:0005634 - nucleus
- **Evidence:** IBA
- **Issue:** No experimental evidence supports nuclear localization of PEF-1 in C. elegans. Both PMID:11312268 and PMID:39550471 show exclusive membrane/ciliary lo

#### KEEP_AS_NON_CORE: GO:0005829 - cytosol
- **Evidence:** IBA
- **Issue:** While membrane association is the predominant localization, some cytosolic presence may occur during protein synthesis/transport. However, the core fu

#### REMOVE: GO:0005506 - iron ion binding
- **Evidence:** IEA
- **Issue:** This is likely an incorrect inference. PPEF family phosphatases use manganese as the catalytic metal ion. UniProt annotation and experimental evidence

#### MARK_AS_OVER_ANNOTATED: GO:0016787 - hydrolase activity
- **Evidence:** IEA
- **Issue:** This is too general to be informative. The more specific GO:0004722 (protein serine/threonine phosphatase activity) already captures the molecular fun

#### MARK_AS_OVER_ANNOTATED: GO:0046872 - metal ion binding
- **Evidence:** IEA
- **Issue:** This is too general to be informative. The more specific GO:0030145 (manganese ion binding) and GO:0005509 (calcium ion binding) already capture the s

#### MODIFY: GO:0050906 - detection of stimulus involved in sensory perception
- **Evidence:** IEA
- **Issue:** While PEF-1 is involved in sensory processes, it is not a receptor that directly detects stimuli. Rather, it modulates sensory signaling in cilia. Mor
- **Proposed:** GO:0040040 - thermosensory behavior
- **Proposed:** GO:0050906 - detection of stimulus involved in sensory perception

#### NEW: GO:0005930 - axoneme
- **Evidence:** IDA
- **Issue:** Experimental evidence from PMID:39550471 demonstrates specific axonemal localization within cilia. This should be added as a new annotation with IDA e

#### NEW: GO:0097730 - non-motile cilium
- **Evidence:** IDA
- **Issue:** PEF-1 is specifically localized to non-motile sensory cilia in C. elegans. This is more specific than the generic cilium term.

#### NEW: GO:0040040 - thermosensory behavior
- **Evidence:** IMP
- **Issue:** Experimental mutant phenotype demonstrates PEF-1 function in thermosensory behavior. AFD neuron expression supports this role.


## Overall Statistics

### By Priority

**Priority 1 (Core IFT)**
- Annotations: 201 | Accept: 150 (74%) | Changes: 51

**Priority 2 (Transition Zone)**
- Annotations: 105 | Accept: 74 (70%) | Changes: 31

**Priority 3 (BBSome/PKD)**
- Annotations: 171 | Accept: 144 (84%) | Changes: 27

---

*Document generated from ciliopathy gene reviews*