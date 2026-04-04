# Ifi204 (Mouse) - Research Notes

## Gene Identity

- **Gene symbol**: Ifi204 (Interferon-activable protein 204, also called p204)
- **UniProt**: P0DOV2
- **Organism**: Mus musculus (Mouse)
- **Human ortholog**: IFI16 (Q16666) - note p204 is considered the murine functional homolog of human IFI16
- **Family**: PYHIN (IFI200/HIN-200) family

## Mouse PYHIN Paralog Expansion

This is a critical context for understanding Ifi204. According to PubMed, the mammalian PYHIN family shows massive lineage-specific expansion in mouse: humans have 4 PYHIN genes (IFI16, AIM2, IFIX, MNDA) while mice have 14 genes on chromosome 1 [PMID:22871040, DOI:10.1186/1471-2148-12-140]. Only AIM2 has clear orthology across species. The other 13 mouse genes arose by duplication and rearrangement within the mouse lineage [PMID:22871040]. The original characterization of the gene cluster was by Choubey et al. 1989 [PMID:2477366, DOI:10.1016/s0021-9258(18)71476-2], who showed the 201, 202, and 204 genes share highly similar regulatory regions with interferon-responsive enhancers.

This means Ifi204 is NOT a simple 1:1 ortholog of human IFI16 -- it is a product of the mouse-specific paralog expansion. While it is often described as the "murine homolog of IFI16," this is a many-to-one relationship. ISO annotations from IFI16 should be treated with some caution due to possible subfunctionalization.

## Domain Architecture

- N-terminal PYRIN/DAPIN domain (aa 1-88): death-fold domain for homotypic protein-protein interactions
- Death-like domain superfamily (aa 2-93)
- HIN-200/IF120x domain A (HINa, aa 213-413): tandem OB-fold, binds dsDNA
- HIN-200/IF120x domain B (HINb, aa 417-615): tandem OB-fold, binds dsDNA
- Crystal structures available: 5YZP (HINa), 5YZW (HINb), 5Z7D (HINab:DNA complex)

## Core Functions from Literature

### 1. Cytosolic DNA sensor / Innate immune signaling
- Cooperates with cGAS to sense dsDNA and activate STING-dependent type I IFN pathway [PMID:25710914, "cGAS and Ifi204 cooperate to produce type I IFNs in response to Francisella infection"]
- Gets acetylated upon bacterial infection, translocates from nucleus to cytoplasm, recruits STING for TBK1-IRF3 activation and IFN-beta release [PMID:28529930, "The Central Role of IFI204 in IFN-beta Release and Autophagy Activation during M. bovis Infection"]
- IFI204 KO mice show increased susceptibility to S. aureus pulmonary infection, with decreased inflammatory cytokines, impaired STING-IRF3 and NF-kB pathways, and defective extracellular trap formation [PMID:30936875, "DNA Sensor IFI204 Contributes to Host Defense Against Staphylococcus aureus Infection in Mice"]
- Crystal structure of HINab:dsDNA complex reveals non-sequence-specific binding mode via alpha-2 helices and linker [PMID:33619523, "Structural mechanism of DNA recognition by the p204 HIN domain"]

### 2. Transcriptional regulation / rRNA transcription inhibition
- Binds UBF1 (ribosomal RNA-specific transcription factor) and inhibits rRNA transcription, mediating interferon's growth-inhibitory effects [PMID:10329630, "The interferon-inducible nucleolar p204 protein binds the ribosomal RNA-specific UBF1 transcription factor and inhibits ribosomal RNA transcription"]
- Interacts with Tpr protein (nuclear pore complex component), which mediates p204 translocation from cytoplasm to nucleus after IFN treatment [PMID:12513910]

### 3. Cell differentiation roles
- **Osteoblast differentiation**: Acts as transcriptional coactivator of Cbfa1/Runx2, enhances BMP-2-induced osteoblast differentiation. Expressed in embryonic osteoblasts and hypertrophic chondrocytes [PMID:15557274, "The interferon-inducible p204 protein acts as a transcriptional coactivator of Cbfa1 and enhances osteoblast differentiation"]
- **Myoblast differentiation**: Required for C2C12 myoblast-to-myotube fusion. Overcomes inhibition by Id proteins (Id1, Id2, Id3) by binding/sequestering them, promoting their ubiquitination and degradation [PMID:11940648, "The MyoD-inducible p204 protein overcomes the inhibition of myoblast differentiation by Id proteins"]
- **Cardiac myocyte differentiation**: Required for P19 cell differentiation to beating cardiac myocytes. Expression activated by Gata4, Nkx2.5, and Tbx5 [PMID:16556595, PMID:16556596]
- **Macrophage differentiation**: Activated by M-CSF, favors macrophage differentiation in myeloid progenitors [PMID:16244109]

### 4. Tumor suppressor activity
- Inhibits cell growth via p53/TP53 and RB1-dependent and independent pathways
- p205 (closely related family member) study shows growth inhibition via multiple cell cycle pathways [PMID:16458891]

## Review of Cited References in GOA

### PMID:12513910 (De Andrea et al., 2002) - REAL
"The mouse interferon-inducible gene Ifi204 product interacts with the Tpr protein, a component of the nuclear pore complex." Directly about Ifi204. Supports: nucleolus localization (IDA), protein binding/interaction with Tpr (IPI), cellular response to IFN-alpha (IDA), nuclear inclusion body (IDA).

### PMID:14654789 (Aglipay et al., 2003) - REAL but about human IFI16, not Ifi204
"A member of the Pyrin family, IFI16, is a novel BRCA1-associated protein involved in the p53-mediated apoptosis pathway." This paper is about HUMAN IFI16 (Q16666). Used for ISO annotations transferred to mouse Ifi204. Valid for: nucleoplasm, nucleolus localization (ISO from IFI16). The apoptosis annotation via ISO is reasonable but should be noted as inferred from the human ortholog.

### PMID:15557274 (Liu et al., 2005) - REAL
"The interferon-inducible p204 protein acts as a transcriptional coactivator of Cbfa1 and enhances osteoblast differentiation." Directly about p204/Ifi204. Supports: transcription coregulator activity (IGI with Cbfa1), protein binding with Cbfa1 (IPI), regulation of transcription by RNA Pol II (IDA), positive regulation of osteoblast differentiation (IGI with Cbfa1).

### PMID:19158679 (Burckstummer et al., 2009) - REAL but about AIM2, not directly Ifi204
"An orthogonal proteomic-genomic screen identifies AIM2 as a cytoplasmic DNA sensor for the inflammasome." This paper primarily characterizes AIM2 as the cytoplasmic DNA sensor. Used for ISO from IFI16 for nucleus/nuclear speck localization, and IDA for dsDNA binding and IFN-beta response. The IDA annotations for Ifi204 based on this reference are questionable -- the paper is about AIM2, and p204/Ifi204 is not the main subject.

### PMID:21795542 (Lu et al., 2011) - REAL but likely over-annotation
"Developmental profiling of spiral ganglion neurons reveals insights into auditory circuit assembly." This is a transcriptomics profiling study of spiral ganglion neurons. Ifi204 is one of many genes with altered expression. The IDA annotation for "inner ear development" based on expression profiling alone is an over-annotation -- expression in a developing tissue does not demonstrate functional involvement.

### PMID:23012479 (Archambaud et al., 2012) - REAL but tangential
"Impact of lactobacilli on orally acquired listeriosis." Ifi204 is mentioned as one of many interferon-stimulated genes (ISGs) affected by lactobacilli treatment during Listeria infection. The IEP annotation for "response to bacterium" is based solely on expression change. This is a very indirect connection.

## Key Observations

1. Ifi204 has dual functions: (a) innate immune DNA sensing in cytoplasm, and (b) transcriptional regulation/differentiation in nucleus
2. Subcellular shuttling is key: nuclear in proliferating cells, translocates to cytoplasm upon infection/differentiation (regulated by acetylation)
3. The "inner ear development" annotation (PMID:21795542) is poorly supported -- just expression data
4. The "protein binding" annotations (GO:0005515) are uninformative per curation guidelines
5. The ISO annotations from IFI16 are reasonable but should be noted as coming from a non-orthologous relationship (paralog expansion)
6. The PMID:19158679 paper is primarily about AIM2 -- some annotations attributed to this reference for Ifi204 may be questionable

## BioReason Analysis Evaluation

The BioReason thinking trace correctly identifies:
- PYHIN family membership
- DAPIN/PYRIN domain for protein-protein interactions
- Tandem HIN OB-fold domains for dsDNA binding
- Transcriptional coregulation
- Innate immune sensing

BioReason incorrectly claims:
- "CARD-mediated assemblies" -- Ifi204 has a PYRIN domain, not a CARD domain. PYRIN interacts with ASC via PYD-PYD interactions, not CARD-CARD
- "CARD-bearing adaptors" -- ASC has both a PYD and a CARD, but the interaction with p204 would be PYD-PYD
- Lists NLRC4 as an interaction partner -- no evidence for this
- Claims Caspase-1 interaction -- p204 is not primarily an inflammasome-forming protein like AIM2. Its main functions are transcriptional regulation and DNA sensing for type I IFN production via STING, not inflammasome activation
- The BioReason model conflates AIM2 (inflammasome) biology with p204/IFI16 (STING pathway) biology
