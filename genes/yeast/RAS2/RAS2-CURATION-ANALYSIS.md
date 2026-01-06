# RAS2 GO Annotation Curation Analysis

## Gene Overview
RAS2 (P01120) is a small GTPase in *Saccharomyces cerevisiae* that functions as the primary regulator of cAMP-dependent protein kinase (PKA) signaling. The protein cycles between GTP-bound (active) and GDP-bound (inactive) states, with CDC25 as its guanine nucleotide exchange factor (GEF) and IRA1/IRA2 as its GTPase-activating proteins (GAPs).

## Key Biological Functions

### 1. Primary Function: cAMP/PKA Signal Transduction
RAS2 is the critical effector controlling adenylate cyclase (CYR1) activity, which produces cAMP. This is the central regulatory pathway for:
- Nutrient-dependent growth control
- Glucose sensing and metabolic enzyme regulation
- Stress response and survival
- Replicative lifespan determination

### 2. Morphogenetic Functions
RAS2 also signals through Cdc42/MAPK pathway to regulate:
- Pseudohyphal growth (filamentous growth response to nitrogen starvation)
- Cell division polarity
- Protein localization to bud neck

### 3. Cellular Compartments
RAS2 localizes to:
- Plasma membrane (primary site for PKA signaling)
- ER membrane (site of initial lipid modifications)
- Nucleus (role in transcriptional regulation)
- Mitochondria (minor fraction, potential metabolic role)

## Annotation Curation Decisions

### Group 1: IBA Annotations (Phylogenetic Inference)

#### GO:0005886 - Plasma Membrane (IBA)
**Action: ACCEPT**
Well-supported by experimental evidence. RAS2 is farnesylated and palmitoylated, anchoring it to membranes. Direct experimental evidence confirms plasma membrane localization (IDA annotations from PMID:20162532, PMID:23127800).

#### GO:0007163 - Establishment or Maintenance of Cell Polarity (IBA)
**Action: ACCEPT**
Well-founded IBA annotation. RAS2 regulates protein localization to bud neck (PMID:12782684, PMID:15917658) and controls cell division polarity through Cdc42/MAPK signaling. The pseudohyphal growth phenotype demonstrates morphogenetic function.

#### GO:0007265 - Ras Protein Signal Transduction (IBA)
**Action: ACCEPT**
This is core function for RAS2. The IBA annotation correctly identifies the intrinsic Ras signaling function. Supported by multiple direct evidence annotations (IDA for GTPase activity, IMP for PKA pathway processes).

#### GO:0003924 - GTPase Activity (IBA)
**Action: ACCEPT**
Core catalytic function. RAS2 has intrinsic GTPase activity (hydrolyzes GTP to GDP), experimentally characterized by PMID:8106517. This is the fundamental biochemical activity enabling regulation of signaling.

### Group 2: IEA Annotations (Computational/Indirect)

#### GO:0000166 - Nucleotide Binding (IEA)
**Action: ACCEPT**
Appropriate computational annotation based on UniProtKB-KW mapping. RAS2 binds guanine nucleotides (GTP/GDP) as essential for GTPase function. Less specific than "GTP binding" but not redundant due to distinct curated relationships.

#### GO:0003924 - GTPase Activity (IEA - InterPro)
**Action: ACCEPT**
Redundant with IBA GTPase activity but represents valid InterPro-based inference. Keep both as different evidence types are acceptable. The InterPro domain IPR001806 correctly identifies this as a small GTPase.

#### GO:0003925 - G Protein Activity (IEA)
**Action: ACCEPT**
Valid computational inference from EC number 3.6.5.2. RAS2 is a G protein (GTP-binding protein) with GTPase activity. This is appropriate as a broader category than "Ras protein signal transduction."

#### GO:0005525 - GTP Binding (IEA)
**Action: ACCEPT**
Appropriate computational annotation. RAS2 canonically binds and hydrolyzes GTP. Supported by experimental evidence (IDA from PMID:6438624). Multiple annotations of same term with different evidence types are acceptable.

#### GO:0005886 - Plasma Membrane (IEA)
**Action: ACCEPT**
Computational annotation from UniProtKB subcellular location mapping. Consistent with IBA and IDA evidence. Represents valid inference from UniProt annotation.

#### GO:0007165 - Signal Transduction (IEA)
**Action: ACCEPT**
Broad category appropriate for RAS2's signaling function. IEA from InterPro is reasonable. Less specific than "Ras protein signal transduction" but not redundant.

#### GO:0016020 - Membrane (IEA)
**Action: ACCEPT**
Appropriate parent term. RAS2 is a membrane protein (plasma membrane anchored by lipid modifications). IEA from InterPro classification is valid.

#### GO:0016787 - Hydrolase Activity (IEA)
**Action: ACCEPT**
Appropriate parent term for GTPase activity (hydrolysis of GTP). UniProtKB-KW mapping is correct for a protein with EC number 3.6.5.2 (GTPase).

#### GO:0097271 - Protein Localization to Bud Neck (IEA - ARBA)
**Action: REMOVE**
This annotation is too specific for computational inference. While RAS2 does localize to the bud neck (supported by IGI evidence PMID:12782684), an IEA annotation for this specific subcellular localization is overly detailed for computational inference. The specific experimental evidence (IGI) is already provided. Remove the IEA version to avoid over-annotation.

### Group 3: Experimental Protein Binding Annotations (IPI)

#### GO:0005515 - Protein Binding (IPI) - Multiple PMIDs
**Action: REMOVE (all instances)**
RAS2 has multiple IPI annotations for protein binding, but this term is not informative per GO curation guidelines. The generic "protein binding" term does not specify the functional interaction. Instead, specific interaction terms should be used:
- RAS1 (PMID:11805837, PMID:16554755) - effector/signaling interaction
- LTE1 (PMID:12782684) - protein localization function
- CDC25 (PMID:21073870) - GEF interaction
- RAF1 (PMID:21457714) - cross-species interaction
- YCF1 (PMID:23831759) - ABC transporter interaction

Since UniProt already curates these specific interactions in the feature annotations, and we have specific process terms (signal transduction, protein localization), the generic "protein binding" terms are redundant and should be removed per GO best practices.

### Group 4: HDA Annotations (Human Directed Annotation)

#### GO:0005739 - Mitochondrion (HDA - PMID:24769239)
**Action: KEEP_AS_NON_CORE**
The supporting paper shows that during respiratory growth, a minor fraction of RAS2 associates with mitochondria. However, this is not a primary site of RAS2 function. The major signaling occurs at the plasma membrane. Keep as non-core annotation documenting secondary localization.

#### GO:0071944 - Cell Periphery (HDA - PMID:26928762)
**Action: KEEP_AS_NON_CORE**
Appropriate general localization category. Cell periphery encompasses both plasma membrane and ER membrane localizations. Keep but mark as non-core since "plasma membrane" is more specific.

#### GO:0005886 - Plasma Membrane (HDA - PMID:11914276, PMID:16622836)
**Action: ACCEPT**
Redundant with existing IBA and IDA annotations for plasma membrane. These HDA annotations add proteomics evidence supporting the primary localization. Keep as additional evidence.

### Group 5: Experimental Process Annotations (IMP/IGI/IDA)

#### GO:0010603 - Regulation of Cytoplasmic mRNA Processing Body Assembly (IMP - PMID:21925385)
**Action: ACCEPT**
Supported by PMID:21925385 showing cAMP/PKA pathway regulates P body formation. RAS2 activates this pathway, so this annotation is accurate. Direct involvement in PKA-dependent P body regulation.

#### GO:0042149 - Cellular Response to Glucose Starvation (IMP - PMID:21925385)
**Action: ACCEPT**
RAS2 is critical for nutrient starvation response. Loss of RAS2 leads to constitutive starvation response. PMID:21925385 shows PKA pathway (activated by RAS2) is key regulator of glucose starvation response.

#### GO:0016236 - Macroautophagy (IGI - PMID:15016820)
**Action: MODIFY**
PMID:15016820 shows RAS/PKA pathway *inhibits* autophagy during growth. The IGI annotation (genetic interaction) reflects this inhibitory relationship. Consider whether "involved_in" relationship is mechanistically accurate, or if "negative_regulation_of" would be more precise. The paper demonstrates that elevated RAS/PKA signaling blocks autophagy. Suggest modifying to GO:0031406 (negative regulation of autophagy).

#### GO:0032258 - Cytoplasm to Vacuole Targeting by the Cvt Pathway (IMP - PMID:15016820)
**Action: MODIFY**
Like macroautophagy, PMID:15016820 shows RAS/PKA pathway *inhibits* Cvt pathway during growth. The annotation should reflect this inhibitory regulation rather than simple involvement. Suggest: GO:0051804 (negative regulation of cytoplasm to vacuole targeting).

#### GO:2000222 - Positive Regulation of Pseudohyphal Growth (IMP - PMID:1547504, PMID:8643578)
**Action: ACCEPT**
Well-supported annotations. Both papers demonstrate RAS2 (constitutively active RAS2val19) promotes pseudohyphal growth in response to starvation. PMID:8643578 further demonstrates this proceeds through Cdc42/MAPK pathway. Core morphogenetic function of RAS2.

#### GO:0005634 - Nucleus (IDA - PMID:23127800)
**Action: ACCEPT**
PMID:23127800 demonstrates RAS2-GTP localizes to nucleus. Supports transcriptional functions and PKA substrate localization.

#### GO:0005886 - Plasma Membrane (IDA - PMID:23127800, PMID:20162532)
**Action: ACCEPT**
Primary localization confirmed by direct experimental evidence. Both papers confirm plasma membrane targeting essential for RAS2 function.

#### GO:0097271 - Protein Localization to Bud Neck (IGI - PMID:12782684)
**Action: ACCEPT**
PMID:12782684 (Ras recruits mitotic exit regulator Lte1 to bud cortex) demonstrates RAS2 directly targets proteins to bud neck. IGI evidence appropriate for this protein-protein localization interaction.

#### GO:0000411 - Positive Regulation of Transcription by Galactose (IMP - PMID:16292676)
**Action: UNDECIDED**
PMID:16292676 addresses phosphoglucomutase activity and galactose growth defects with elevated RAS signaling. The paper examines metabolic enzyme activity (phosphoglucomutase) rather than transcriptional regulation. Need to verify if RAS2 directly regulates galactose-responsive transcription or if this is secondary to metabolic changes. Cannot confirm mechanistic basis without seeing full paper details.

#### GO:0030437 - Ascospore Formation (IMP - PMID:2558958)
**Action: KEEP_AS_NON_CORE**
RAS2 is involved in sporulation (meiosis), but this represents a secondary/developmental function. RAS2 plays permissive roles in stationary phase/nutrient starvation responses that enable sporulation, but is not a primary regulator of meiosis. Keep as documented but mark non-core.

#### GO:0032880 - Regulation of Protein Localization (IMP - PMID:15917658)
**Action: ACCEPT**
PMID:15917658 (Ras and Rho effector Cla4 collaborate to target and anchor Lte1) demonstrates RAS2 regulates protein localization to bud cortex. Core function for cell division control.

#### GO:0005789 - Endoplasmic Reticulum Membrane (IDA - PMID:22575457)
**Action: ACCEPT**
PMID:22575457 demonstrates RAS2 transiently localizes to ER membrane during lipid modification and ER-to-Golgi trafficking. Site of initial farnesylation and C-terminal processing before plasma membrane targeting.

#### GO:0005739 - Mitochondrion (IDA - PMID:22575457)
**Action: KEEP_AS_NON_CORE**
PMID:22575457 shows minor mitochondrial localization of RAS2. While technically present in cells, this is not a primary site of RAS2 signaling function. The paper shows RAS2 primarily at plasma membrane and some ER localization. Mitochondrial localization may be artifact of cell fractionation or represent transient interaction. Keep as non-core, secondary localization.

## Summary of Actions

### ACCEPT (Core Functions)
- GO:0007265 (Ras protein signal transduction) - primary function
- GO:0003924 (GTPase activity) - catalytic function
- GO:0005525 (GTP binding) - substrate binding
- GO:0005886 (plasma membrane) - localization for signaling
- GO:0007163 (cell polarity establishment) - morphogenetic function
- GO:2000222 (positive regulation of pseudohyphal growth) - developmental response
- GO:0032880 (regulation of protein localization) - cell division function
- GO:0042149 (cellular response to glucose starvation) - nutrient sensing
- GO:0010603 (regulation of P body assembly) - stress response
- GO:0005634 (nucleus) - localization for transcription
- GO:0097271 (protein localization to bud neck) - mitotic function

### ACCEPT (Computational/Parent Terms - Keep for Completeness)
- GO:0000166 (nucleotide binding) - parent term, not redundant
- GO:0003925 (G protein activity) - parent category
- GO:0007165 (signal transduction) - parent category
- GO:0016020 (membrane) - general localization
- GO:0016787 (hydrolase activity) - parent for GTPase
- GO:0005739 (mitochondrion - IDA) - experimental evidence for secondary site
- GO:0005789 (ER membrane - IDA) - site of post-translational modification
- GO:0071944 (cell periphery) - general periphery localization

### KEEP_AS_NON_CORE
- GO:0005739 (mitochondrion - HDA) - minor secondary localization
- GO:0030437 (ascospore formation) - secondary developmental function
- GO:0071944 (cell periphery - HDA) - less specific than plasma membrane

### MODIFY
- GO:0016236 (macroautophagy) - should be "negative regulation of" (inhibitory function)
- GO:0032258 (Cvt pathway) - should be "negative regulation of" (inhibitory function)

### UNDECIDED
- GO:0000411 (positive regulation of transcription by galactose) - insufficient information on mechanism

### REMOVE
- GO:0005515 (protein binding - all IPI) - non-informative generic term per GO guidelines
- GO:0097271 (protein localization to bud neck - IEA) - redundant with IGI, too specific for IEA

## Additional Recommended New Annotations

### GO:0019003 - GDP Binding
Already exists as computational (IBA) but should be added as experimental if nucleotide binding studies exist.

### GO:0005515 (Protein Binding) Alternative
Rather than generic protein binding, could add specific binding functions:
- GO:0001948 (protein binding, bridging) - for adaptor functions
- GO:0043565 (sequence-specific DNA binding) - if transcriptional effects confirmed
- GO:0019899 (protein phosphorylation) - if PKA-dependent phosphorylation exists

However, these require strong evidence and are currently not supported by provided data.

## Overall Assessment
RAS2 has a well-curated annotation set covering its primary function as a cAMP/PKA pathway regulator. The main improvements needed are:
1. Remove generic "protein binding" terms (non-informative)
2. Correct macroautophagy and Cvt pathway annotations to reflect inhibition rather than involvement
3. Clarify galactose transcription annotation mechanism
4. Mark developmental/secondary functions as non-core
