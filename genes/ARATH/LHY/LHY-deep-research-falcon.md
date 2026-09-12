Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for GO Annotation Review

## Target

- Gene symbol: LHY
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q6R0H1
Entry Name: LHY_ARATH
Gene Name: LHY
Locus Tag: At1g01060 {ECO:0000312|Araport:AT1G01060}
Protein Name: Protein LHY
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: Transcription factor involved in the circadian clock. Binds to the promoter region of APRR1/TOC1 and TCP21/CHE to repress their transcription. Represses both CCA1 and itself. May recognize the promoter of JMJ14 to regulates its expression during the night in a circadian manner (PubMed:31429787).
Subcellular Location: Nucleus
Subunit: Homodimer or heterodimer with CCA1. Interacts with CCA1 (via internal domain); independently of photoperiod. Functions probably as part of a large complex. Interacts with CKB1 and CKB3. Interacts with LNK1 and LNK2 (PubMed:25012192).
======================

## Research Objective

Prepare a comprehensive literature-backed research report for GO annotation review of the target gene.

Focus on:

1. The core biochemical activity of the gene product and any substrate specificity.
2. The activation or maturation mechanism of the protein, including proteolytic processing if relevant.
3. The best-supported subcellular localization and complexes where the active protein functions.
4. The strongest experimentally supported biological processes in the target organism, or in very close orthologs when transfer is justified.
5. Which annotations appear to reflect core function versus context-specific, pleiotropic, or over-extended roles.
6. Any evidence bearing on apoptosis, developmental cell death, neuronal roles, inflammatory signaling, pyroptosis, synaptic remodeling, protein processing, and localization to cytoplasm, cytosol, nucleus, or signaling complexes.

## Output Requirements

Structure the report as:

1. Executive summary
2. Molecular function
3. Biological process roles
4. Cellular localization and complexes
5. Annotation-risk assessment
6. Key literature

Use citations for all substantive claims.


# Gene Research Report for GO Annotation Review: **LHY (At1g01060)** in *Arabidopsis thaliana*

**Gene/Protein:** LATE ELONGATED HYPOCOTYL (LHY); UniProt Q6R0H1 (LHY_ARATH)  
**Organism:** *Arabidopsis thaliana* (taxon:3702)

## 1. Executive summary

LHY encodes a **dawn-phased MYB-related transcription factor** that binds specific cis-elements (the **Evening Element, EE**, and closely related **CCA1-binding site, CBS**) in promoters to regulate transcriptional programs that underpin the *Arabidopsis* circadian oscillator and its major outputs. The strongest direct molecular evidence supports **sequence-specific DNA binding** (EE/CBS) and **transcriptional repression** of evening genes (notably **TOC1/APRR1** and **GI**) via recruitment of the **corepressor DET1** (as part of the COP10–DET1–DDB1 “CDD” complex). Genetic evidence shows that LHY is essential for robust rhythms: **single mutants show short-period phenotypes** while **cca1 lhy double mutants rapidly lose rhythmicity** under constant conditions. (davies2013transcriptionfactorinteractions pages 21-25, kamioka2016directrepressionof pages 1-2, lau2011interactionofarabidopsis pages 4-5)

Recent (2024) work expands validated, direct LHY targets into stress signaling: LHY **binds the ABF3 promoter in vivo (ChIP)** and participates in reciprocal regulation between core clock genes and ABA/stress responses; ABF3 overexpression and cca1/lhy clock defects are linked to **shortened circadian period** and stress-modulated transcription factor binding. (liang2024theinterplaybetween pages 3-6)

For GO review, the most defensible annotations center on **(i) sequence-specific DNA binding**, **(ii) transcriptional regulator activity in the nucleus**, and **(iii) circadian rhythm regulation**. Several downstream phenotypes (flowering time, freezing tolerance, ABA/drought traits) are best treated as **clock outputs** or context-specific roles unless supported by direct LHY promoter occupancy and causal regulation in the specific experimental context. (dong2011circadianclockassociated1 pages 1-2, park2016lateelongatedhypocotyl pages 2-4)

## 2. Molecular function

### 2.1 Key concepts/definitions (current understanding)

**Circadian morning MYB-related repressors.** LHY and its close paralog CCA1 are single-MYB transcription factors expressed near dawn that regulate the plant clock through **transcriptional–translational feedback loops**. (davies2013transcriptionfactorinteractions pages 21-25, dong2011circadianclockassociated1 pages 1-2)

**DNA-binding motif specificity (substrate specificity).** LHY recognizes promoter cis-elements closely related to one another:

- **Evening Element (EE):** **AAAATATCT** (michael2002phasespecificcircadianclock pages 1-2, harmer2005positiveandnegative pages 1-2)
- **CCA1-binding site (CBS):** reported as **AAAAATCT** (and in some notations **AAAAAATCT**) (michael2002phasespecificcircadianclock pages 1-2, harmer2005positiveandnegative pages 5-7)

A key mechanistic point for annotation is that the EE and CBS differ by a **single nucleotide**, and swapping EE→CBS can shift circadian phase of transcription, demonstrating motif-level “substrate” specificity relevant to cis-regulatory binding. (michael2002phasespecificcircadianclock pages 1-2)

**Direct binding by LHY.** EMSA experiments using extracts containing GST-LHY and oligonucleotides containing EE sequences provide direct evidence that **LHY can bind EE-containing probes** in vitro (alongside GST-CCA1). (harmer2005positiveandnegative pages 5-7)

### 2.2 Biochemical activity and directionality (activation vs repression)

**Primary activity supported:** LHY acts mainly as a **transcriptional repressor** of key evening-phased clock genes, especially **TOC1** (and also GI), forming the core negative feedback architecture of the plant oscillator. (davies2013transcriptionfactorinteractions pages 21-25, dong2011circadianclockassociated1 pages 1-2, lau2011interactionofarabidopsis pages 4-5)

**Mechanism: recruitment of DET1 corepressor.** A strong experimentally supported mechanistic model is that LHY (with CCA1) recruits **DET1** to EE-containing promoter regions of targets such as **TOC1** and **GI**, enabling transcriptional repression:

- DET1 physically interacts with LHY (and CCA1) by in vitro pull-down and in vivo split-luciferase complementation (lau2011interactionofarabidopsis pages 4-5, lau2011interactionofarabidopsis pages 16-19)
- DET1 binds EE-containing regions of TOC1/GI promoters; DET1 promoter binding peaks around **ZT0** and is reduced by **ZT12**; recruitment is diminished/abolished in **cca1 lhy** backgrounds (lau2011interactionofarabidopsis pages 4-5)
- DET1 overexpression reduces an EE reporter by ~**70%** in a transient assay (lau2011interactionofarabidopsis pages 4-5)

These findings strongly support annotating LHY under **negative regulation of transcription** (by RNA polymerase II) and **protein binding** in a nuclear repression context, rather than any enzymatic activity. (lau2011interactionofarabidopsis pages 4-5)

**Activation roles exist but are target/context dependent.** Multiple sources describe LHY/CCA1 as also contributing to activation of some clock genes (e.g., PRR7/PRR9 induction) within the oscillator network. (dong2011circadianclockassociated1 pages 1-2, kamioka2016directrepressionof pages 1-2) GO terms should avoid forcing LHY into a unidirectional “activator only” or “repressor only” role.

### 2.3 Activation/maturation mechanisms (processing)

No evidence in the retrieved primary literature indicates that LHY requires proteolytic processing or zymogen-like maturation to become active. Regulation is best supported as occurring through (i) transcriptional feedback, (ii) promoter occupancy changes, and (iii) protein–protein interactions (e.g., with DET1 and LNKs), with broader circadian systems showing prominent post-translational regulation for other core proteins. (lau2011interactionofarabidopsis pages 4-5, maeda2024coldinduceddegradationof pages 7-8)

## 3. Biological process roles

### 3.1 Core biological process: circadian rhythm generation and regulation

**Strongest evidence (core oscillator role):**

- LHY/CCA1 are core components of the oscillator; **single mutants** show circadian defects (e.g., short period), while **cca1 lhy double mutants lose rhythmic expression rapidly** under constant light, demonstrating essentiality for robust oscillation. (davies2013transcriptionfactorinteractions pages 21-25)
- LHY/CCA1 directly repress **TOC1** by binding EE/CBS-like elements in the TOC1 promoter, placing LHY in the central negative feedback loop. (davies2013transcriptionfactorinteractions pages 21-25, dong2011circadianclockassociated1 pages 1-2)

### 3.2 Photoperiodic flowering and phase transition (clock output)

LHY affects photoperiodic flowering primarily through **clock phase control**, not necessarily by direct binding to floral integrator promoters:

- In lhy mutants, the expression peaks of photoperiod pathway genes **GI** and **FKF1** are advanced by ~**4 hours**, and **FT** is up-regulated; mutants flower early under both LD and SD. (park2016lateelongatedhypocotyl pages 2-4)
- Importantly, Park et al. report that **CCA1 binds strongly to the FT promoter, whereas LHY does not show such DNA-binding activity** to the FT promoter in their assays, supporting an *indirect* LHY→FT mechanism mediated by clock timing rather than direct repression at FT. (park2016lateelongatedhypocotyl pages 2-4)

**GO implication:** “regulation of flowering time/photoperiodism” is supportable, but “direct regulation of FT transcription” by LHY is not supported by the cited evidence and is an annotation risk. (park2016lateelongatedhypocotyl pages 2-4)

### 3.3 Abiotic stress and ABA signaling (2024 mechanistic update)

A 2024 PNAS study provides direct mechanistic evidence linking LHY to ABA/stress transcriptional networks:

- **LHY binds the ABF3 promoter in vivo** (ChIP using anti-LHY beads) and the ABF3 promoter contains an EE-like segment (**AAATATC**) (liang2024theinterplaybetween pages 3-6)
- ABF3 provides reciprocal regulation: ABF3 binds promoters of **CCA1** and **LHY**, and ABA enhances ABF3 DNA-binding activity, thereby modulating core clock gene expression under stress (liang2024theinterplaybetween pages 3-6)
- Quantitative design elements include period assays with **n = 12** (means ± SEM) and significance **P < 0.01** for stress/ABA effects in the reported assays (liang2024theinterplaybetween pages 3-6)

**GO implication:** This supports “regulation of response to abscisic acid/abiotic stress via circadian clock” as a plausible BP annotation when properly qualified, but it remains more context-specific than the core oscillator function. (liang2024theinterplaybetween pages 3-6)

### 3.4 Cold/freezing tolerance via CBF pathway (clock output)

Dong et al. provide evidence that CCA1/LHY control the circadian timing of the CBF cold-response pathway:

- In WT, **CBF1/CBF3** show circadian peaks around **ZT8** and troughs around **ZT20**; in **cca1-11/lhy-21**, circadian regulation of CBF1/CBF3 is essentially eliminated and cold induction of **CBF1–3** is greatly impaired (dong2011circadianclockassociated1 pages 1-2)

**GO implication:** Support for “regulation of cold acclimation/freezing tolerance” exists, but again may be best treated as a clock-controlled output pathway unless the annotation is scoped to “circadian regulation of cold response”. (dong2011circadianclockassociated1 pages 1-2)

## 4. Cellular localization and complexes

### 4.1 Subcellular localization

The most defensible cellular component assignment for active LHY is the **nucleus**, supported by nuclear interaction/ChIP frameworks and nuclear reporter reconstitution assays:

- DET1–LHY in vivo interaction assays (split-luciferase/LCI) and promoter ChIP assays operate in a nuclear chromatin context; DET1 is described as a nuclear protein, and LHY promoter binding is shown alongside DET1 binding at TOC1/GI promoters (lau2011interactionofarabidopsis pages 4-5, lau2011interactionofarabidopsis pages 16-19)
- LNK1/2 interactions with LHY were detected by BiFC/LCI with **nuclear signals** in the reported experimental systems (xie2014lnk1andlnk2 pages 2-4)

No primary evidence in this run supports stable LHY function in cytosolic signaling complexes.

### 4.2 Complex partners (experimentally supported)

**DET1/CDD-associated repression complex.** LHY physically interacts with DET1; DET1 recruitment to TOC1 promoter is dependent on CCA1/LHY; DET1 binding is rhythmic and functionally represses EE reporters. (lau2011interactionofarabidopsis pages 4-5, lau2011interactionofarabidopsis pages 16-19)

**LNK1/LNK2 coactivator interactions.** LHY (and CCA1) physically interacts with LNK1/LNK2 in planta (BiFC and LCI), implicating LHY in multi-protein regulatory assemblies that integrate activator/coactivator roles in oscillator transcriptional regulation. (xie2014lnk1andlnk2 pages 2-4, xie2014lnk1andlnk2 pages 1-2)

**Evidence gaps for this run:** Direct experimental evidence for **LHY homodimer/heterodimer (with CCA1)** and for direct interaction with specific **CK2 subunits (CKB proteins)** was not retrieved in the excerpts analyzed here; such statements appear in curated resources (e.g., UniProt metadata) but should be treated as requiring primary citation support for GO. (lau2011interactionofarabidopsis pages 4-5)

## 5. Annotation-risk assessment (core vs context-specific; avoid over-extension)

### 5.1 Core-function annotations (high confidence)

Recommended to treat as core, broadly applicable annotations:

- **Sequence-specific DNA binding transcription factor activity** targeting EE/CBS-like promoter elements (EE: AAAATATCT; CBS: AAAAATCT/AAAAAATCT) (michael2002phasespecificcircadianclock pages 1-2, harmer2005positiveandnegative pages 5-7)
- **Negative regulation of transcription** for key clock targets (e.g., TOC1) with experimentally supported corepressor recruitment (DET1) (lau2011interactionofarabidopsis pages 4-5)
- **Circadian rhythm / regulation of circadian rhythm** (strong genetics; core oscillator dependence) (davies2013transcriptionfactorinteractions pages 21-25)
- **Nuclear localization** as primary active compartment (protein–protein interaction and chromatin association context) (lau2011interactionofarabidopsis pages 4-5, xie2014lnk1andlnk2 pages 2-4)

### 5.2 Context-specific or pleiotropic outputs (moderate confidence; scope carefully)

Support exists, but these are best described as clock outputs or condition-specific roles unless direct promoter binding + functional causality is demonstrated for the specific process:

- **Photoperiodic flowering regulation**: strong phenotype and phase-shift evidence, but **LHY does not show FT promoter binding** in the cited work; avoid direct FT-binding annotation for LHY. (park2016lateelongatedhypocotyl pages 2-4)
- **ABA/abiotic stress crosstalk**: direct ABF3 promoter binding by LHY is strong, but downstream drought/salt phenotypes represent a broader network; annotations should reflect “regulation of ABA-responsive transcription” or “circadian modulation of ABA signaling” rather than implying LHY is an ABA receptor pathway component. (liang2024theinterplaybetween pages 3-6)
- **Cold/freezing tolerance**: supported via CBF pathway regulation; annotate as circadian regulation of cold response rather than general “cold tolerance” unless specifically justified. (dong2011circadianclockassociated1 pages 1-2)

### 5.3 Over-extended / inappropriate domains (strongly discourage)

No evidence in the examined corpus supports annotation of LHY to animal-specific pathways:

- apoptosis, pyroptosis, neuronal roles, synaptic remodeling, inflammatory signaling  

These terms are biologically inappropriate for *Arabidopsis* LHY based on the retrieved evidence; plant defense/stress signaling is described in plant-specific terms and does not provide support for cross-kingdom immune/cell-death modules. (davies2013transcriptionfactorinteractions pages 111-117, liang2024theinterplaybetween pages 3-6, davies2013transcriptionfactorinteractions pages 107-111)

### 5.4 Protein processing / maturation

No evidence of proteolytic processing/maturation mechanisms for LHY was found; do not add “protein processing” annotations absent specific evidence. (maeda2024coldinduceddegradationof pages 7-8)

## 6. Evidence synthesis table (for GO curation)

| Aspect (MF/BP/CC) | Claim (succinct) | Key experimental evidence (assay types) | Important quantitative/statistical details | Notes for GO annotation (core vs context-specific) | Primary source and URL |
|---|---|---|---|---|---|
| MF | LHY is a dawn-phased single-Myb/MYB-related DNA-binding transcription factor that recognizes EE/CBS-like cis-elements | In vitro promoter-binding and motif analyses; functional circadian reporter assays; EMSA with GST-LHY/CCA1 on EE probes; promoter mutagenesis/conversion between EE and CBS (michael2002phasespecificcircadianclock pages 1-2, andronis2008theclockprotein pages 1-2, harmer2005positiveandnegative pages 1-2, harmer2005positiveandnegative pages 5-7, davies2013transcriptionfactorinteractions pages 21-25) | EE sequence reported as **AAAATATCT**; CBS reported as **AAAAATCT** or **AAAAAATCT** in different notations; single-base EE→CBS conversion shifted peak transcription from evening to morning; multimerized CBS reporters showed evening acrophases around CT11.8 and CT12.7 in one assay context (michael2002phasespecificcircadianclock pages 1-2, harmer2005positiveandnegative pages 5-7) | Strong support for **sequence-specific DNA binding transcription factor activity** and **cis-regulatory region sequence-specific DNA binding**. Sequence notation varies slightly across papers, so motif-level GO notes should mention EE/CBS family rather than one rigid 8–9 bp string (michael2002phasespecificcircadianclock pages 1-2, andronis2008theclockprotein pages 1-2) | Michael 2002, *Plant Physiology* — https://doi.org/10.1104/pp.004929; Harmer 2005, *Plant Cell* — https://doi.org/10.1105/tpc.105.033035 |
| BP | LHY is a core circadian clock component required for robust rhythms | Loss- and gain-of-function genetics; circadian transcriptional profiling under constant light; reporter phenotypes (davies2013transcriptionfactorinteractions pages 21-25, li2025transcriptionalactivationand pages 3-4, park2016lateelongatedhypocotyl pages 2-4) | lhy or cca1 single mutants show short-period rhythms; **cca1 lhy double mutants rapidly lose rhythmic expression within ~2 days in constant light**; LHY overexpression abolishes rhythmic expression and causes long hypocotyl/late flowering phenotypes (davies2013transcriptionfactorinteractions pages 21-25) | Very strong support for **circadian rhythm / regulation of circadian rhythm** as core BP terms. This is the highest-confidence biological role for annotation (davies2013transcriptionfactorinteractions pages 21-25, park2016lateelongatedhypocotyl pages 2-4) | Davies 2013, thesis summary of primary studies — no stable journal URL in context; Li 2025 review summarizes primary evidence — https://doi.org/10.1016/j.xplc.2025.101415 |
| MF/BP | LHY directly represses evening-phased clock genes including TOC1/APRR1 and GI | In vitro promoter binding to TOC1 EE/CBS-related elements; transient reporter repression; ChIP-supported recruitment models; genetic phase analyses (davies2013transcriptionfactorinteractions pages 21-25, dong2011circadianclockassociated1 pages 1-2, kamioka2016directrepressionof pages 1-2, lau2011interactionofarabidopsis pages 4-5) | DET1 binding to TOC1 promoter peaks at **ZT0** and is reduced at **ZT12**; DET1 overexpression reduced EE-reporter activity by **~70%** and repressed TOC1 reporter activity; det1 mutants showed earlier TOC1/GI phase and short period, phenocopying cca1/lhy defects (lau2011interactionofarabidopsis pages 4-5) | Appropriate for **negative regulation of transcription by RNA polymerase II** and core clock repression roles. TOC1 repression is core; GI repression is well-supported but can be treated as part of the clock/output interface rather than the single defining function (davies2013transcriptionfactorinteractions pages 21-25, lau2011interactionofarabidopsis pages 4-5) | Lau 2011, *Molecular Cell* — https://doi.org/10.1016/j.molcel.2011.07.013; Dong 2011, *PNAS* — https://doi.org/10.1073/pnas.1103741108 |
| BP | LHY/CCA1 activate morning/midday PRR genes such as PRR7 and PRR9 | ChIP and genetic analysis in core oscillator studies; expression analyses in mutants (dong2011circadianclockassociated1 pages 1-2, kamioka2016directrepressionof pages 1-2, xie2014lnk1andlnk2 pages 1-2) | No exact fold change provided in retrieved excerpts, but multiple studies summarized direct binding to **PRR7** and **PRR9** promoters with activation (dong2011circadianclockassociated1 pages 1-2, kamioka2016directrepressionof pages 1-2) | Suitable as part of **circadian transcriptional network regulation**. Because activation is target-specific while repression dominates other targets, avoid over-generalizing LHY as only an activator or only a repressor (dong2011circadianclockassociated1 pages 1-2, kamioka2016directrepressionof pages 1-2) | Dong 2011, *PNAS* — https://doi.org/10.1073/pnas.1103741108; Kamioka 2016, *Plant Cell* — https://doi.org/10.1105/tpc.15.00737 |
| MF/CC | LHY recruits/works with DET1 as a transcriptional corepressor mechanism at target promoters | In vitro pull-downs; BiFC; luciferase complementation imaging; ChIP at TOC1/GI promoters; reporter repression assays (lau2011interactionofarabidopsis pages 4-5, lau2011interactionofarabidopsis pages 1-2, lau2011interactionofarabidopsis pages 2-4) | DET1 N-terminal **aa 26–87** interacts with CCA1/LHY; Gal4DBD-DET1 repressed yeast reporter by **~40%** and plant luciferase reporter by **~70%**; DET1 binding to TOC1 promoter was reduced in **cca1 lhy** mutant background (lau2011interactionofarabidopsis pages 4-5, lau2011interactionofarabidopsis pages 2-4) | Strong support for annotating LHY as functioning in a **nuclear transcriptional repressor complex/context**, but DET1 itself is the corepressor; GO should not imply LHY is an enzyme. Best used to support **protein binding** and **negative regulation of transcription** rather than assigning a highly specific stable complex unless ontology term fits CDD-associated repression (lau2011interactionofarabidopsis pages 4-5, lau2011interactionofarabidopsis pages 1-2) | Lau 2011, *Molecular Cell* — https://doi.org/10.1016/j.molcel.2011.07.013 |
| CC/MF | LHY physically interacts with nuclear LNK1/LNK2, linking the dawn complex to transcriptional coactivation | GFP localization, BiFC and firefly luciferase complementation imaging in planta; promoter recruitment logic from clock network studies (xie2014lnk1andlnk2 pages 2-4, xie2014lnk1andlnk2 pages 1-2) | Complemented YFP and luciferase signals were observed **in the nucleus** for LNK1/2 with LHY or CCA1; no numeric binding constants in excerpt (xie2014lnk1andlnk2 pages 2-4) | Supports **nuclear localization** and **protein binding**. Because LNK1/2 are coactivators lacking DNA-binding domains, annotate LHY as part of a broader regulatory complex, but avoid overstating LHY as a universal coactivator; this interaction is target/context dependent (xie2014lnk1andlnk2 pages 2-4, xie2014lnk1andlnk2 pages 1-2) | Xie 2014, *Plant Cell* — https://doi.org/10.1105/tpc.114.126573 |
| BP | LHY directly binds the ABF3 promoter and participates in clock–ABA/abiotic stress crosstalk | ChIP with anti-LHY beads; promoter motif analysis; RT-qPCR in WT/LHY-OX/cca1 lhy; circadian luciferase period assays under ABA/NaCl; germination phenotyping (liang2024theinterplaybetween pages 3-6) | ABF3 promoter contains an EE-like segment **AAATATC**; period assays used **n=12**, means ± SEM, with **P < 0.01** for significant effects; **ABF3-OX, cca1, and lhy mutants all had short circadian periods**; ABA treatment enhanced ABF3 DNA binding activity to CCA1/LHY promoters (liang2024theinterplaybetween pages 3-6) | Useful for **regulation of response to abscisic acid / abiotic stress via circadian clock**, but should be considered **context-specific downstream regulation**, not the most core GO BP relative to circadian oscillator function (liang2024theinterplaybetween pages 3-6) | Liang 2024, *PNAS* — https://doi.org/10.1073/pnas.2316825121 |
| BP | LHY/CCA1 directly regulate the CBF cold-response pathway and freezing tolerance outputs | ChIP/genetic analysis; expression timing of CBF genes; freezing tolerance phenotype (dong2011circadianclockassociated1 pages 1-2) | In WT, **CBF1/CBF3 peak ~ZT8 and trough ~ZT20**; in **cca1-11/lhy-21**, cold induction of **CBF1–3** is greatly impaired and circadian regulation of **CBF1/CBF3** is essentially eliminated (dong2011circadianclockassociated1 pages 1-2) | Good support for **circadian regulation of cold-responsive transcription**, but this is best treated as a clock output process rather than LHY’s most defining GO BP after circadian rhythm itself (dong2011circadianclockassociated1 pages 1-2) | Dong 2011, *PNAS* — https://doi.org/10.1073/pnas.1103741108 |
| BP | LHY contributes to photoperiodic flowering primarily through circadian phase control, with FT effects largely indirect for LHY | Mutant flowering phenotypes; diel expression analysis of GI/FKF1/CO/FT/SOC1; promoter-binding comparison with CCA1 (park2016lateelongatedhypocotyl pages 2-4) | **lhy-7** and **lhy-20** flower early; **GI** and **FKF1** expression peaks advance by **~4 h**; **FT** is elevated but **CO** waveform is not detectably altered; significance reported at **P < 0.01**; authors note **CCA1 binds FT strongly but LHY does not show such FT promoter binding** (park2016lateelongatedhypocotyl pages 2-4) | Appropriate for **photoperiodism, flowering** or **regulation of flowering time** with caution: evidence supports LHY acting **via the clock**, not as a direct FT repressor. Avoid direct FT-binding annotation for LHY based on current evidence set (park2016lateelongatedhypocotyl pages 2-4) | Park 2016, *BMC Plant Biology* — https://doi.org/10.1186/s12870-016-0810-8 |
| CC | Active LHY functions in the nucleus | Nuclear interaction/readout assays with DET1 and LNK1/2; localization of associated factors; UniProt-supported consensus (lau2011interactionofarabidopsis pages 4-5, xie2014lnk1andlnk2 pages 2-4) | Nuclear BiFC/LCI signals reported for DET1–LHY and LNK–LHY interactions; no alternate stable cytosolic compartment supported in retrieved primary evidence (lau2011interactionofarabidopsis pages 4-5, xie2014lnk1andlnk2 pages 2-4) | Strong support for **nucleus**. Current evidence does **not** support stable annotation to cytosol/cytoplasm as main active location, except trivial transit during synthesis (lau2011interactionofarabidopsis pages 4-5, xie2014lnk1andlnk2 pages 2-4) | Lau 2011, *Molecular Cell* — https://doi.org/10.1016/j.molcel.2011.07.013; Xie 2014, *Plant Cell* — https://doi.org/10.1105/tpc.114.126573 |
| BP/context | Temperature compensation studies place LHY in the core temperature-buffering network, but direct LHY ubiquitination was not shown in Maeda 2024 | Circadian period assays across temperature series; protein abundance and ubiquitination assays focused on PRR5/TOC1; comparative discussion of CCA1/LHY levels (maeda2024coldinduceddegradationof pages 7-8, maeda2024coldinduceddegradationof pages 2-3, maeda2024coldinduceddegradationof pages 1-2, maeda2024coldinduceddegradationof pages 3-4) | WT period changed from **24.21 ± 0.12 h at 12°C** to **21.34 ± 0.18 h at 25°C** (**Q10 = 1.12**); **prr5 toc1** changed from **21.52 ± 0.18 h** to **17.00 ± 0.07 h** (**Q10 = 1.30**); TOC1-F decreased **75%** at 12°C, PRR5-F by **~90%**; MG132 rescued TOC1-F **25-fold** at 12°C; TOC1/PRR5 ubiquitination increased **~5.5× / ~17.4×** at 12°C; CCA1/LHY protein amounts were noted as reduced at **4°C** but not directly mechanistically dissected here (maeda2024coldinduceddegradationof pages 7-8, maeda2024coldinduceddegradationof pages 2-3, maeda2024coldinduceddegradationof pages 3-4) | Important annotation caution: this supports LHY involvement in **temperature compensation/circadian temperature response**, but **does not justify direct ubiquitination or LKP2-substrate annotation for LHY** from this paper alone (maeda2024coldinduceddegradationof pages 7-8, maeda2024coldinduceddegradationof pages 3-4) | Maeda 2024, *Science Advances* — https://doi.org/10.1126/sciadv.adq0187 |
| MF/context | No evidence in the retrieved set for proteolytic maturation/processing of LHY into a distinct active form | Literature review across primary studies; no cleavage/maturation mechanism reported (li2025transcriptionalactivationand pages 3-4, lau2011interactionofarabidopsis pages 4-5, maeda2024coldinduceddegradationof pages 7-8) | None reported | Do **not** assign proteolytic processing/maturation annotations. Regulation is mainly through transcriptional feedback, protein interactions, phosphorylation, and stability control rather than zymogen-like activation (lau2011interactionofarabidopsis pages 4-5, maeda2024coldinduceddegradationof pages 7-8) | Multiple primary studies; see Lau 2011 and Maeda 2024 URLs above |
| Annotation risk | No support for apoptosis, pyroptosis, neuronal, synaptic, or animal inflammatory-signaling annotations; plant defense/stress links are plant-specific clock outputs | Negative evidence from surveyed LHY literature; retrieved studies discuss plant ABA, cold, pathogen/stress, flowering, and circadian outputs only (davies2013transcriptionfactorinteractions pages 111-117, davies2013transcriptionfactorinteractions pages 92-97, liang2024theinterplaybetween pages 3-6, davies2013transcriptionfactorinteractions pages 107-111) | None | Strong recommendation to reject cross-kingdom over-annotations such as apoptosis, pyroptosis, neuronal/synaptic remodeling, or inflammatory signaling. If any cell-death-related term were considered, it would require direct plant-specific evidence not present here (davies2013transcriptionfactorinteractions pages 111-117, davies2013transcriptionfactorinteractions pages 107-111) | Liang 2024, *PNAS* — https://doi.org/10.1073/pnas.2316825121; Davies 2013 thesis excerpts — no stable journal URL in context |


*Table: This table summarizes experimentally supported molecular functions, biological processes, cellular localization, and annotation cautions for Arabidopsis LHY (At1g01060). It is designed to help distinguish core circadian-clock annotations from downstream or context-specific roles.*

## 7. Key literature (with URLs and publication dates)

**Recent (prioritize 2023–2024):**

1. Liang T. et al. (Feb 2024). *PNAS* — “The interplay between the circadian clock and abiotic stress responses mediated by ABF3 and CCA1/LHY.” https://doi.org/10.1073/pnas.2316825121 (liang2024theinterplaybetween pages 3-6)
2. Maeda A.E. et al. (Sep 2024). *Science Advances* — “Cold-induced degradation of core clock proteins implements temperature compensation in the Arabidopsis circadian clock.” https://doi.org/10.1126/sciadv.adq0187 (maeda2024coldinduceddegradationof pages 1-2, maeda2024coldinduceddegradationof pages 3-4)

**Foundational mechanistic / high-authority primary studies:**

3. Lau O.S. et al. (Sep 2011). *Molecular Cell* — “Interaction of Arabidopsis DET1 with CCA1 and LHY in mediating transcriptional repression in the plant circadian clock.” https://doi.org/10.1016/j.molcel.2011.07.013 (lau2011interactionofarabidopsis pages 4-5)
4. Dong M.A. et al. (Apr 2011). *PNAS* — “CCA1 and LHY regulate expression of the CBF pathway in Arabidopsis.” https://doi.org/10.1073/pnas.1103741108 (dong2011circadianclockassociated1 pages 1-2)
5. Park M.-J. et al. (May 2016). *BMC Plant Biology* — “LHY regulates photoperiodic flowering via the circadian clock in Arabidopsis.” https://doi.org/10.1186/s12870-016-0810-8 (park2016lateelongatedhypocotyl pages 2-4)
6. Kamioka M. et al. (Mar 2016). *Plant Cell* — “Direct repression of evening genes by CCA1…” https://doi.org/10.1105/tpc.15.00737 (kamioka2016directrepressionof pages 1-2)
7. Xie Q. et al. (Jul 2014). *The Plant Cell* — “LNK1 and LNK2 are transcriptional coactivators in the Arabidopsis circadian oscillator.” https://doi.org/10.1105/tpc.114.126573 (xie2014lnk1andlnk2 pages 2-4)
8. Michael T.P. & McClung C.R. (Oct 2002). *Plant Physiology* — “Phase-specific circadian clock regulatory elements in Arabidopsis.” https://doi.org/10.1104/pp.004929 (michael2002phasespecificcircadianclock pages 1-2)
9. Harmer S.L. & Kay S.A. (May 2005). *Plant Cell* — “Positive and negative factors confer phase-specific circadian regulation of transcription in Arabidopsis.” https://doi.org/10.1105/tpc.105.033035 (harmer2005positiveandnegative pages 1-2, harmer2005positiveandnegative pages 5-7)

## Notes on limitations of this evidence package

- Direct experimental excerpts supporting **LHY–CCA1 dimerization** and **CK2 subunit binding** were not retrieved in this run; if these are needed for GO CC/complex terms, consult the primary interaction and phosphorylation papers cited in broader reviews/UniProt or obtain full texts not captured here. (lau2011interactionofarabidopsis pages 4-5)
- Evidence on **LHY ubiquitination/proteasome turnover** specifically (as a substrate) was not directly captured here; Maeda 2024 provides strong quantitative ubiquitination data for TOC1/PRR5, not LHY. (maeda2024coldinduceddegradationof pages 3-4)


References

1. (davies2013transcriptionfactorinteractions pages 21-25): SEW Davies. Transcription factor interactions at the promoter of the arabidopsis circadian clock gene lhy. Unknown journal, 2013.

2. (kamioka2016directrepressionof pages 1-2): Mari Kamioka, Saori Takao, Takamasa Suzuki, Kyomi Taki, Tetsuya Higashiyama, Toshinori Kinoshita, and Norihito Nakamichi. Direct repression of evening genes by circadian clock-associated1 in the arabidopsis circadian clock[open]. Plant Cell, 28:696-711, Mar 2016. URL: https://doi.org/10.1105/tpc.15.00737, doi:10.1105/tpc.15.00737. This article has 325 citations and is from a highest quality peer-reviewed journal.

3. (lau2011interactionofarabidopsis pages 4-5): On Sun Lau, Xi Huang, Jean-Benoit Charron, Jae-Hoon Lee, Gang Li, and Xing Wang Deng. Interaction of arabidopsis det1 with cca1 and lhy in mediating transcriptional repression in the plant circadian clock. Molecular cell, 43 5:703-12, Sep 2011. URL: https://doi.org/10.1016/j.molcel.2011.07.013, doi:10.1016/j.molcel.2011.07.013. This article has 160 citations and is from a highest quality peer-reviewed journal.

4. (liang2024theinterplaybetween pages 3-6): Tong Liang, Shi Yu, Yuanzhong Pan, Jiarui Wang, and Steve A. Kay. The interplay between the circadian clock and abiotic stress responses mediated by abf3 and cca1/lhy. Proceedings of the National Academy of Sciences of the United States of America, Feb 2024. URL: https://doi.org/10.1073/pnas.2316825121, doi:10.1073/pnas.2316825121. This article has 39 citations and is from a highest quality peer-reviewed journal.

5. (dong2011circadianclockassociated1 pages 1-2): Malia A. Dong, Eva M. Farré, and Michael F. Thomashow. Circadian clock-associated 1 and late elongated hypocotyl regulate expression of the c-repeat binding factor (cbf) pathway in arabidopsis. Proceedings of the National Academy of Sciences, 108:7241-7246, Apr 2011. URL: https://doi.org/10.1073/pnas.1103741108, doi:10.1073/pnas.1103741108. This article has 505 citations and is from a highest quality peer-reviewed journal.

6. (park2016lateelongatedhypocotyl pages 2-4): Mi-Jeong Park, Young-Ju Kwon, Kyung-Eun Gil, and Chung-Mo Park. Late elongated hypocotyl regulates photoperiodic flowering via the circadian clock in arabidopsis. BMC Plant Biology, May 2016. URL: https://doi.org/10.1186/s12870-016-0810-8, doi:10.1186/s12870-016-0810-8. This article has 74 citations and is from a peer-reviewed journal.

7. (michael2002phasespecificcircadianclock pages 1-2): Todd P. Michael and C. Robertson McClung. Phase-specific circadian clock regulatory elements in arabidopsis1. Plant Physiology, 130:627-638, Oct 2002. URL: https://doi.org/10.1104/pp.004929, doi:10.1104/pp.004929. This article has 191 citations and is from a highest quality peer-reviewed journal.

8. (harmer2005positiveandnegative pages 1-2): Stacey L. Harmer and Steve A. Kay. Positive and negative factors confer phase-specific circadian regulation of transcription in arabidopsisw⃞. The Plant Cell Online, 17:1926-1940, May 2005. URL: https://doi.org/10.1105/tpc.105.033035, doi:10.1105/tpc.105.033035. This article has 260 citations.

9. (harmer2005positiveandnegative pages 5-7): Stacey L. Harmer and Steve A. Kay. Positive and negative factors confer phase-specific circadian regulation of transcription in arabidopsisw⃞. The Plant Cell Online, 17:1926-1940, May 2005. URL: https://doi.org/10.1105/tpc.105.033035, doi:10.1105/tpc.105.033035. This article has 260 citations.

10. (lau2011interactionofarabidopsis pages 16-19): On Sun Lau, Xi Huang, Jean-Benoit Charron, Jae-Hoon Lee, Gang Li, and Xing Wang Deng. Interaction of arabidopsis det1 with cca1 and lhy in mediating transcriptional repression in the plant circadian clock. Molecular cell, 43 5:703-12, Sep 2011. URL: https://doi.org/10.1016/j.molcel.2011.07.013, doi:10.1016/j.molcel.2011.07.013. This article has 160 citations and is from a highest quality peer-reviewed journal.

11. (maeda2024coldinduceddegradationof pages 7-8): Akari E. Maeda, Hiromi Matsuo, Tomoaki Muranaka, and Norihito Nakamichi. Cold-induced degradation of core clock proteins implements temperature compensation in the arabidopsis circadian clock. Science Advances, Sep 2024. URL: https://doi.org/10.1126/sciadv.adq0187, doi:10.1126/sciadv.adq0187. This article has 15 citations and is from a highest quality peer-reviewed journal.

12. (xie2014lnk1andlnk2 pages 2-4): Qiguang Xie, Peng Wang, Xian Liu, Li Yuan, Lingbao Wang, Chenguang Zhang, Yue Li, Hongya Xing, Liya Zhi, Zhiliang Yue, Chunsheng Zhao, C. Robertson McClung, and Xiaodong Xu. Lnk1 and lnk2 are transcriptional coactivators in the <i>arabidopsis</i> circadian oscillator. Jul 2014. URL: https://doi.org/10.1105/tpc.114.126573, doi:10.1105/tpc.114.126573. This article has 229 citations.

13. (xie2014lnk1andlnk2 pages 1-2): Qiguang Xie, Peng Wang, Xian Liu, Li Yuan, Lingbao Wang, Chenguang Zhang, Yue Li, Hongya Xing, Liya Zhi, Zhiliang Yue, Chunsheng Zhao, C. Robertson McClung, and Xiaodong Xu. Lnk1 and lnk2 are transcriptional coactivators in the <i>arabidopsis</i> circadian oscillator. Jul 2014. URL: https://doi.org/10.1105/tpc.114.126573, doi:10.1105/tpc.114.126573. This article has 229 citations.

14. (davies2013transcriptionfactorinteractions pages 111-117): SEW Davies. Transcription factor interactions at the promoter of the arabidopsis circadian clock gene lhy. Unknown journal, 2013.

15. (davies2013transcriptionfactorinteractions pages 107-111): SEW Davies. Transcription factor interactions at the promoter of the arabidopsis circadian clock gene lhy. Unknown journal, 2013.

16. (andronis2008theclockprotein pages 1-2): Christos Andronis, Simon Barak, Stephen M. Knowles, Shoji Sugano, and Elaine M. Tobin. The clock protein cca1 and the bzip transcription factor hy5 physically interact to regulate gene expression in arabidopsis. Molecular plant, 1 1:58-67, Jan 2008. URL: https://doi.org/10.1093/mp/ssm005, doi:10.1093/mp/ssm005. This article has 135 citations and is from a highest quality peer-reviewed journal.

17. (li2025transcriptionalactivationand pages 3-4): Jing Li, Ming-kang Yang, Jian Zeng, Liang Chen, and Wei Huang. Transcriptional activation and repression in the plant circadian clock: revisiting core oscillator feedback loops and output pathways. Plant communications, pages 101415, Jun 2025. URL: https://doi.org/10.1016/j.xplc.2025.101415, doi:10.1016/j.xplc.2025.101415. This article has 14 citations and is from a peer-reviewed journal.

18. (lau2011interactionofarabidopsis pages 1-2): On Sun Lau, Xi Huang, Jean-Benoit Charron, Jae-Hoon Lee, Gang Li, and Xing Wang Deng. Interaction of arabidopsis det1 with cca1 and lhy in mediating transcriptional repression in the plant circadian clock. Molecular cell, 43 5:703-12, Sep 2011. URL: https://doi.org/10.1016/j.molcel.2011.07.013, doi:10.1016/j.molcel.2011.07.013. This article has 160 citations and is from a highest quality peer-reviewed journal.

19. (lau2011interactionofarabidopsis pages 2-4): On Sun Lau, Xi Huang, Jean-Benoit Charron, Jae-Hoon Lee, Gang Li, and Xing Wang Deng. Interaction of arabidopsis det1 with cca1 and lhy in mediating transcriptional repression in the plant circadian clock. Molecular cell, 43 5:703-12, Sep 2011. URL: https://doi.org/10.1016/j.molcel.2011.07.013, doi:10.1016/j.molcel.2011.07.013. This article has 160 citations and is from a highest quality peer-reviewed journal.

20. (maeda2024coldinduceddegradationof pages 2-3): Akari E. Maeda, Hiromi Matsuo, Tomoaki Muranaka, and Norihito Nakamichi. Cold-induced degradation of core clock proteins implements temperature compensation in the arabidopsis circadian clock. Science Advances, Sep 2024. URL: https://doi.org/10.1126/sciadv.adq0187, doi:10.1126/sciadv.adq0187. This article has 15 citations and is from a highest quality peer-reviewed journal.

21. (maeda2024coldinduceddegradationof pages 1-2): Akari E. Maeda, Hiromi Matsuo, Tomoaki Muranaka, and Norihito Nakamichi. Cold-induced degradation of core clock proteins implements temperature compensation in the arabidopsis circadian clock. Science Advances, Sep 2024. URL: https://doi.org/10.1126/sciadv.adq0187, doi:10.1126/sciadv.adq0187. This article has 15 citations and is from a highest quality peer-reviewed journal.

22. (maeda2024coldinduceddegradationof pages 3-4): Akari E. Maeda, Hiromi Matsuo, Tomoaki Muranaka, and Norihito Nakamichi. Cold-induced degradation of core clock proteins implements temperature compensation in the arabidopsis circadian clock. Science Advances, Sep 2024. URL: https://doi.org/10.1126/sciadv.adq0187, doi:10.1126/sciadv.adq0187. This article has 15 citations and is from a highest quality peer-reviewed journal.

23. (davies2013transcriptionfactorinteractions pages 92-97): SEW Davies. Transcription factor interactions at the promoter of the arabidopsis circadian clock gene lhy. Unknown journal, 2013.