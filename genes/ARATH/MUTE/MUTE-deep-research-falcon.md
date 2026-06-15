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

- Gene symbol: MUTE
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q9M8K6
Entry Name: MUTE_ARATH
Gene Name: MUTE
Protein Name: Transcription factor MUTE
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: Transcription factor. Together with FMA and SPCH, regulates the stomata formation. Required for the differentiation of stomatal guard cells, by promoting successive asymmetric cell divisions and the formation of guard mother cells. Promotes the conversion of the leaf epidermis into stomata.
Subcellular Location: Nucleus
Subunit: Homodimer.
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


## Gene Research Report for GO Annotation Review: **MUTE (Arabidopsis thaliana)**

**Target**: MUTE (UniProt Q9M8K6; MUTE_ARATH)  
**Protein**: Transcription factor MUTE (stomatal-lineage bHLH)  
**Primary GO curation goal**: identify *core* molecular function(s), the best-supported biological process roles, and the cellular component/complex context; flag over-extended annotations.

### 1. Executive summary
MUTE is a stomatal-lineage basic helix–loop–helix (bHLH) transcription factor that functions as a *stage-specific fate switch* in Arabidopsis leaf epidermis. The strongest experimental and integrative evidence places MUTE at the transition from meristemoid self-renewal/asymmetric divisions to guard mother cell (GMC) commitment, after which a single symmetric division produces paired guard cells. This role is executed through nuclear DNA binding—primarily as a heterodimer with SCRM/ICE1-family bHLH partners—and through cooperation with chromatin-remodeling machinery to activate lineage-appropriate gene expression programs. (liu2023cellfateprogramming pages 1-2, liu2024bhlhtranscriptionfactors pages 5-7)

Two major 2023–2024 advances refine the mechanistic picture relevant to GO annotation. First, genome-wide chromatin and TF-binding analyses indicate that MUTE (with SCRM) can bind targets in nucleosome-occupied/repressed chromatin and coordinate with SWI/SNF remodelers and the histone acetyltransferase HAC1 during fate commitment, consistent with pioneer-like properties and an “epigenome + TF” model of stomatal differentiation. (liu2024bhlhtranscriptionfactors pages 5-7, liu2024bhlhtranscriptionfactors pages 13-15)

Second, a 2024 chemical genetics study identified **Stomidazolone**, a small molecule that binds the MUTE C-terminal ACT-like (ACTL) domain and disrupts SCRM–MUTE heterodimerization, producing dose-dependent meristemoid arrest and reduced stomatal differentiation; this provides direct biochemical evidence for an ACTL-mediated dimerization/partner-selectivity mechanism and demonstrates a real-world research tool to perturb MUTE-dependent differentiation. (nakagawa2024chemicalinhibitionof pages 1-2, nakagawa2024chemicalinhibitionof pages 2-3)

No evidence in the retrieved recent literature supports roles for Arabidopsis MUTE in apoptosis, neuronal biology, inflammatory signaling, pyroptosis, or synaptic remodeling; these processes are animal-centric and would be inappropriate for MUTE based on current evidence. (liu2024bhlhtranscriptionfactors pages 5-7, liu2023cellfateprogramming pages 4-5)

### 2. Molecular function
#### 2.1 Key concepts and definitions (GO-relevant)
- **bHLH transcription factor**: DNA-binding transcription regulators with a basic region that recognizes cis-regulatory motifs and an HLH region that mediates dimerization. In the stomatal lineage, stage-specific bHLHs (SPCH→MUTE→FAMA) act sequentially, and their effective DNA binding commonly occurs as heterodimers with SCRM/ICE1-family partners. (zhou2024molecularmechanismsfor pages 2-4, liu2023cellfateprogramming pages 1-2)
- **Heterodimeric “core DNA-binding unit”**: Recent genome-wide analyses support that stomatal bHLHs function in constrained heterodimer configurations (e.g., MUTE–SCRM) that impose motif/spacing rules at bound loci and that cooperative binding is a key determinant of specificity and potency. (liu2023cellfateprogramming pages 5-7, liu2024bhlhtranscriptionfactors pages 13-15)

#### 2.2 Core biochemical activity and substrate specificity
**Core activity**: sequence-specific transcription regulation via nuclear DNA binding (no catalytic substrate). Evidence includes ChIP-seq-defined binding of stomatal bHLHs (including MUTE) to cis-regulatory elements and coordinated transcriptional programs observed in scRNA-seq data during lineage transitions. (liu2023cellfateprogramming pages 2-4, liu2024bhlhtranscriptionfactors pages 5-7)

MUTE-bound CREs are often relatively inaccessible in early lineage contexts and can be nucleosome-occupied and marked by repressive histone modifications (H3K27me3), implying that MUTE participates in activating genes embedded in repressed chromatin during fate commitment. (liu2024bhlhtranscriptionfactors pages 5-7)

**Direct targets supported in retrieved evidence** (best-supported, but note that “directness” varies by source type):
- **FAMA** is described as a likely/direct target within integrated ChIP-seq and regulatory models, and is positioned downstream in the stomatal bHLH cascade. (liu2023cellfateprogramming pages 5-7)
- Review syntheses highlight MUTE-dependent activation of **CYCD5** (to drive the GMC symmetric division) coupled to induction of inhibitors such as **FAMA** and **FLP** to restrict division number, and induction of **ERL1** as feedback. (zhou2024molecularmechanismsfor pages 2-4, wakeel2021speechlessandmute pages 3-5)

**Annotation implication**: A GO Molecular Function consistent with the evidence is “sequence-specific DNA-binding transcription factor activity” (and/or “transcription regulator activity”) rather than any enzymatic function; there is no evidence in the retrieved sources for catalytic substrate specificity.

#### 2.3 Activation / maturation mechanism
There is no evidence here for proteolytic processing or maturation of MUTE as an activation requirement. Instead, regulation is best supported through:

1) **Partner-dependent activation (heterodimerization)**: MUTE forms functional heterodimers with SCRM-family bHLHs; disrupting this interaction abolishes differentiation outputs. (nakagawa2024chemicalinhibitionof pages 7-8, nakagawa2024chemicalinhibitionof pages 9-10)

2) **ACTL-domain-mediated partner selectivity and chemical perturbation**: Stomidazolone binds the MUTE ACTL domain and perturbs SCRM–MUTE heterodimerization both in vitro and in plant cells. Quantitatively, preincubation with Stomidazolone weakened SCRM–MUTE binding by ~100-fold (BLI: Kd ~7.5 nM → ~856.5 nM; ITC: ~9.5 nM → ~900 nM). (nakagawa2024chemicalinhibitionof pages 7-8)

3) **Upstream signaling context (MAPK cascade)**: Reviews summarize that YDA–MKK–MPK signaling downstream of receptor/ligand modules can suppress stomatal bHLH activity; however, in the retrieved evidence, this is more pathway-contextual than a MUTE-specific post-translational maturation mechanism. (zhou2024molecularmechanismsfor pages 10-11, wakeel2021speechlessandmute pages 3-5)

### 3. Biological process roles
#### 3.1 Current understanding (core BP)
The best-supported biological process for MUTE in Arabidopsis is the **meristemoid-to-guard mother cell transition**, i.e., terminating amplifying asymmetric divisions of meristemoids and promoting commitment to GMC fate, followed by coordination of the single symmetric division that generates guard cells. (giannoutsou2025guardiansofwater pages 6-8, zhou2024molecularmechanismsfor pages 2-4)

Genome-wide chromatin/TB-binding work further supports that MUTE drives fate commitment by enabling activation of a new phase of transcriptional regulation at targets that are initially in a more repressed chromatin state, consistent with a commitment switch. (liu2024bhlhtranscriptionfactors pages 5-7, liu2024bhlhtranscriptionfactors pages 13-15)

#### 3.2 Recent developments (2023–2024)
**Chromatin and epigenetic machinery as integral components of the MUTE program**: In Arabidopsis stomatal development, bHLH targets can reside in repressive chromatin and MUTE/SCRM binding is associated with nucleosome-occupied regions. The 2024 PLOS Biology study proposes that recruitment of SWI/SNF chromatin remodelers and HAC1 supports chromatin opening and sustained target expression during differentiation. (liu2024bhlhtranscriptionfactors pages 13-15, liu2024bhlhtranscriptionfactors pages 5-7)

**Chemical control of the MUTE step**: Stomidazolone treatment produces dose-dependent inhibition of stomatal differentiation with large increases in meristemoids, matching a blockade at the MUTE-dependent commitment step. Reported changes include stomatal decreases of ~24.45%, 59.50%, 69.53% and meristemoid increases of ~315.8%, 801.5%, 647.6% at 20, 50, and 100 μM. (nakagawa2024chemicalinhibitionof pages 2-3)

#### 3.3 Applications and real-world implementations
**Crop engineering direction (review-level evidence)**: A 2024 Development review discusses leveraging stomatal developmental genetics—including SMF factors and their network wiring—to generate crop varieties with optimized stomatal traits for resilience under climate change, including CRISPR/Cas-based modification strategies that tune stomatal density and related physiological traits. These examples are presented as applied implementations/proposals rather than MUTE-specific Arabidopsis phenotypes. (chua2024stomataldevelopmentin pages 12-13)

**Tool compound for research and potential developmental manipulation**: Stomidazolone constitutes a concrete in vivo chemical tool to perturb stomatal differentiation by directly targeting MUTE dimerization, and engineered Stomidazolone-resistant MUTE variants demonstrate on-target engagement. (nakagawa2024chemicalinhibitionof pages 1-2, nakagawa2024chemicalinhibitionof pages 10-11)

### 4. Cellular localization and complexes
#### 4.1 Subcellular localization
The strongest evidence supports **nuclear localization** of MUTE in stomatal-lineage cells:
- A MUTE promoter-driven nuclear reporter (MUTEpro::nucYFP) is used to monitor MUTE nuclear localization/expression in differentiating meristemoids, including under Stomidazolone conditions. (nakagawa2024chemicalinhibitionof pages 2-3, nakagawa2024chemicalinhibitionof media 2b410197)
- MUTEpro::MUTE-GFP signals are observed in nuclei of late meristemoids; these constructs rescue mute phenotypes in the cited work, supporting that the nuclear fusion is functional. (nakagawa2024chemicalinhibitionof pages 10-11, nakagawa2024chemicalinhibitionof pages 10-10)

There is no affirmative evidence in the retrieved set for primary cytosolic/cytoplasmic localization as the active functional compartment.

#### 4.2 Complexes / interaction partners
**Core partner(s)**: MUTE heterodimerizes with **SCRM/ICE1-family bHLHs** (SCRM and/or SCRM2), supported by interaction assays including Y2H and nuclear BiFC/rBiFC readouts, and by functional disruption with Stomidazolone. (nakagawa2024chemicalinhibitionof pages 7-8, nakagawa2024chemicalinhibitionof pages 9-10)

**Functional association with chromatin remodelers**: Proximity labeling and genetic dependency analyses support that stomatal bHLH-driven fate programs involve SWI/SNF components and HAC1; these are best viewed as functional co-factors associated with bHLH-dependent chromatin opening, rather than a single fully defined stable macromolecular complex with fixed composition. (liu2023cellfateprogramming pages 4-5, liu2024bhlhtranscriptionfactors pages 13-15)

### 5. Annotation-risk assessment (core vs over-extended)
#### 5.1 High-confidence, core annotations (recommended)
**Molecular Function (MF)**
- Sequence-specific DNA-binding transcription factor activity / transcription regulator activity (bHLH family). (liu2023cellfateprogramming pages 2-4, liu2024bhlhtranscriptionfactors pages 5-7)

**Biological Process (BP)**
- Stomatal lineage cell fate commitment; meristemoid-to-GMC transition; stomatal development / stomatal complex development; regulation of asymmetric→symmetric division transitions within stomatal lineage. (giannoutsou2025guardiansofwater pages 6-8, zhou2024molecularmechanismsfor pages 2-4)

**Cellular Component (CC)**
- Nucleus (functional TF localization supported by nuclear reporters/fusions). (nakagawa2024chemicalinhibitionof pages 10-11, nakagawa2024chemicalinhibitionof media 2b410197)

#### 5.2 Moderate-confidence / context-dependent annotations (use with caution)
- “Chromatin remodeling” or “regulation of chromatin accessibility” as BP terms: recent evidence argues MUTE/SCRM functionally cooperates with SWI/SNF/HAC1 and shows pioneer-like binding; however, whether MUTE should itself be directly annotated to chromatin remodeling processes depends on GO evidence standards (direct participation vs enabling recruitment). (liu2024bhlhtranscriptionfactors pages 13-15, liu2023cellfateprogramming pages 4-5)
- “Response to environmental stimulus” terms (CO2/temperature/drought): reviews emphasize that environmental signaling modulates stomatal development networks and that engineering stomatal traits is a climate-resilience strategy, but these are not MUTE-specific causal phenotypes in Arabidopsis in the retrieved evidence and are likely over-extended if assigned directly to MUTE. (chua2024stomataldevelopmentin pages 12-13, zhou2024molecularmechanismsfor pages 10-11)

#### 5.3 Likely erroneous or unsupported annotations (avoid)
- Apoptosis, pyroptosis, inflammatory signaling, neuronal/synaptic remodeling: no evidence in the retrieved corpus supports these processes for MUTE, and they are generally animal-specific. (liu2024bhlhtranscriptionfactors pages 5-7, liu2023cellfateprogramming pages 4-5)
- Cytosol/cytoplasm as primary active location: current evidence emphasizes nuclear localization and genome-binding/chromatin-based function. (nakagawa2024chemicalinhibitionof pages 10-10, liu2024bhlhtranscriptionfactors pages 5-7)
- Proteolytic maturation/processing: no evidence in the retrieved sources that MUTE requires proteolytic processing to become active. (nakagawa2024chemicalinhibitionof pages 1-2)

### 6. Key literature (prioritizing 2023–2024)
Below are authoritative sources used for this report; URLs are DOI links and publication dates are as provided in the retrieved metadata.

1) **Nakagawa et al.** “Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bHLH heterodimer via an ACT-Like domain.” *Nature Communications* (Publication date: **Oct 2024**). https://doi.org/10.1038/s41467-024-53214-4  
   Key contributions: ACTL-domain mechanism; quantitative biophysics; nuclear reporters; dose-response phenotypes; engineered resistance. (nakagawa2024chemicalinhibitionof pages 1-2, nakagawa2024chemicalinhibitionof pages 7-8, nakagawa2024chemicalinhibitionof pages 10-11, nakagawa2024chemicalinhibitionof pages 2-3)

2) **Liu et al.** “bHLH transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during Arabidopsis stomatal development.” *PLOS Biology* (Publication date: **Aug 2024**). https://doi.org/10.1371/journal.pbio.3002770  
   Key contributions: TF–chromatin state coupling; pioneer-like binding; SWI/SNF and HAC1 cooperation model; example direct targets. (liu2024bhlhtranscriptionfactors pages 5-7, liu2024bhlhtranscriptionfactors pages 13-15)

3) **Chua & Lau** “Stomatal development in the changing climate.” *Development* (Publication date: **Oct 2024**). https://doi.org/10.1242/dev.202681  
   Key contributions: updated review of environmental control and applications in crop improvement; context for SMF network use in engineering. (chua2024stomataldevelopmentin pages 12-13)

4) **Zhou et al.** “Molecular Mechanisms for Regulating Stomatal Formation across Diverse Plant Species.” *International Journal of Molecular Sciences* (Publication date: **Sep 2024**). https://doi.org/10.3390/ijms251910403  
   Key contributions: mechanistic synthesis of SPCH→MUTE→FAMA; heterodimer partners; cell-cycle and feedback nodes (CYCD5, ERL1, FLP/FAMA). (zhou2024molecularmechanismsfor pages 2-4, zhou2024molecularmechanismsfor pages 10-11)

5) **Liu et al.** “Cell Fate Programming by Transcription Factors and Epigenetic Machinery in Stomatal Development.” *bioRxiv* (Preprint posted: **Aug 2023**). https://doi.org/10.1101/2023.08.23.554515  
   Key contributions: foundational analyses on nucleosome-occupied targets, MUTE-induced chromatin changes, and proximity labeling evidence for remodeler association (preprint version of later peer-reviewed work). (liu2023cellfateprogramming pages 4-5)

6) **Wakeel et al.** “SPEECHLESS and MUTE Mediate Feedback Regulation of Signal Transduction during Stomatal Development.” *Plants* (Publication date: **Feb 2021**). https://doi.org/10.3390/plants10030432  
   Key contributions: pathway and feedback framing for MUTE (ERL1/EPF2 nodes; MAPK pathway context). (wakeel2021speechlessandmute pages 3-5)

---

### GO-focused evidence table
| Claim (GO-relevant) | Evidence type/assay | Key quantitative/statistical data (if any) | Best citation(s) (with paper title, year, DOI URL) | Notes for annotation-risk (core vs over-extended) |
|---|---|---|---|---|
| **Molecular function evidence:** MUTE is a **stomatal-lineage bHLH transcription factor** that binds cis-regulatory DNA together with SCRM/ICE1-family partners and activates transcription during fate transition. | ChIP-seq, scRNA-seq integration, motif analysis, MNase-seq, inducible expression; in planta and genomic assays show MUTE-bound CREs, often in closed chromatin, with cooperative binding with SCRM. | No single catalytic substrate; DNA-binding is sequence/motif-based. MUTE induction reduced nucleosome density at targets within **4 h**. | *bHLH transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during Arabidopsis stomatal development* (2024), https://doi.org/10.1371/journal.pbio.3002770 (liu2024bhlhtranscriptionfactors pages 5-7, liu2024bhlhtranscriptionfactors pages 13-15); *Cell Fate Programming by Transcription Factors and Epigenetic Machinery in Stomatal Development* (2023), https://doi.org/10.1101/2023.08.23.554515 (liu2023cellfateprogramming pages 4-5, liu2023cellfateprogramming pages 2-4) | **Core MF.** Strong support for sequence-specific transcription regulator / DNA-binding TF role. **Do not over-annotate enzyme activity or substrate-specific catalysis**; evidence supports transcriptional/chromatin regulatory function, not classical catalytic biochemistry. |
| **Key downstream targets:** MUTE promotes GMC transition and single symmetric division by activating stomatal/cell-cycle regulators including **CYCD5**, **FAMA**, **FLP**, and induces **ERL1** feedback. | Review synthesis from genetic, transcriptional, and downstream network studies; ChIP-seq/scRNA-seq support for shared bHLH targets; FAMA identified as a likely direct target. | Qualitative network logic: CYCD5 induction promotes division; FAMA/FLP restrict further divisions; no quantitative fold-change given in gathered excerpts. | *Molecular Mechanisms for Regulating Stomatal Formation across Diverse Plant Species* (2024), https://doi.org/10.3390/ijms251910403 (zhou2024molecularmechanismsfor pages 2-4); *Speechless and Mute Mediate Feedback Regulation of Signal Transduction during Stomatal Development* (2021), https://doi.org/10.3390/plants10030432 (wakeel2021speechlessandmute pages 3-5); *Cell Fate Programming by Transcription Factors and Epigenetic Machinery in Stomatal Development* (2023), https://doi.org/10.1101/2023.08.23.554515 (liu2023cellfateprogramming pages 5-7) | **Core BP-network support**, but direct GO target-based annotation should be cautious unless target-specific direct binding/perturbation is explicit. Safer to annotate upstream process roles than many individual “positive regulation of X gene expression” terms. |
| **Activation/regulation mechanisms:** MUTE function depends on **heterodimerization via its ACT-like (ACTL) domain** with SCRM-family bHLHs; Stomidazolone directly binds MUTE ACTL and perturbs SCRM–MUTE interaction. Upstream MAPK signaling is reported to negatively regulate the stomatal bHLH module. | Y2H, rBiFC/BiFC in nuclei, BLI, ITC, docking, site-directed mutagenesis, chemical genetics, in planta rescue/resistance assays; review evidence for MAPK-pathway control. | Stomidazolone increased SCRM–MUTE dissociation constant from about **7.5 nM to 856.5 nM** (BLI) and about **9.5 nM to 900 nM** (ITC); Arabidopsis seedlings showed stomatal decreases of **24.45%, 59.50%, 69.53%** and meristemoid increases of **315.8%, 801.5%, 647.6%** at **20/50/100 μM**. | *Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bHLH heterodimer via an ACT-Like domain* (2024), https://doi.org/10.1038/s41467-024-53214-4 (nakagawa2024chemicalinhibitionof pages 7-8, nakagawa2024chemicalinhibitionof pages 10-11, nakagawa2024chemicalinhibitionof pages 1-2, nakagawa2024chemicalinhibitionof pages 9-10, nakagawa2024chemicalinhibitionof pages 2-3); *Molecular Mechanisms for Regulating Stomatal Formation across Diverse Plant Species* (2024), https://doi.org/10.3390/ijms251910403 (zhou2024molecularmechanismsfor pages 10-11) | **Core mechanistic support** for dimerization-dependent TF activity. **Do not annotate proteolytic maturation or covalent activation**: no evidence for proteolytic processing; MAPK regulation is pathway-contextual and less direct than ACTL-mediated partner selection. |
| **Biological process roles:** MUTE is required for **meristemoid-to-guard mother cell transition**, termination of amplifying asymmetric divisions, promotion of GMC fate, and coordination of the **single symmetric division** leading toward paired guard cells/stomata. | Mutant phenotype, overexpression, lineage analysis, review synthesis, scRNA-seq and chromatin studies. | Loss of function causes continued asymmetric divisions / arrested meristemoids; overexpression converts epidermal cells to GMC-like fate and eventual paired guard cells. No unified numerical penetrance in gathered excerpts. | *bHLH transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during Arabidopsis stomatal development* (2024), https://doi.org/10.1371/journal.pbio.3002770 (liu2024bhlhtranscriptionfactors pages 5-7); *Stomatal development in the changing climate* (2024), https://doi.org/10.1242/dev.202681 (chua2024stomataldevelopmentin pages 12-13); *Molecular Mechanisms for Regulating Stomatal Formation across Diverse Plant Species* (2024), https://doi.org/10.3390/ijms251910403 (zhou2024molecularmechanismsfor pages 2-4); *Guardians of Water and Gas Exchange* (2025), https://doi.org/10.3390/plants14152405 (giannoutsou2025guardiansofwater pages 6-8) | **Highest-confidence GO BP area.** Appropriate for stomatal lineage progression, stomatal complex development, cell fate commitment/differentiation. **Avoid broad whole-plant stress annotations** unless directly tied to developmental mechanism. |
| **Cellular component/localization:** Active MUTE is **nuclear** in stomatal-lineage cells; evidence supports DNA/chromatin-associated function rather than cytosolic/cytoplasmic residence. | MUTEpro::nucYFP reporter, MUTEpro::MUTE-GFP rescue lines with confocal imaging; ChIP-seq/MNase-seq imply chromatin association. | Confocal imaging shows MUTE-GFP/nucYFP in nuclei of differentiating meristemoids; no quantitative localization ratio reported. | *Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bHLH heterodimer via an ACT-Like domain* (2024), https://doi.org/10.1038/s41467-024-53214-4 (nakagawa2024chemicalinhibitionof pages 10-11, nakagawa2024chemicalinhibitionof pages 2-3, nakagawa2024chemicalinhibitionof media 2b410197, nakagawa2024chemicalinhibitionof pages 10-10); *bHLH transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during Arabidopsis stomatal development* (2024), https://doi.org/10.1371/journal.pbio.3002770 (liu2024bhlhtranscriptionfactors pages 5-7) | **Core CC.** Nuclear annotation is well supported. **Cytoplasm/cytosol annotations are not supported by gathered evidence** and would be risky unless based on separate direct localization experiments. |
| **Complex/interaction partners:** MUTE forms functional **heterodimers with SCRM/ICE1 and SCRM2**; the MUTE–SCRM module associates with chromatin-remodeling machinery including **SWI/SNF components** and **HAC1**. | Y2H, rBiFC/BiFC, BLI, ITC, TurboID proximity labeling, Y2H confirmation for remodeler interactions; structural modeling. | Drug perturbation data show strong quantitative weakening of SCRM–MUTE binding; remodeler associations are supported qualitatively rather than stoichiometrically. | *Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bHLH heterodimer via an ACT-Like domain* (2024), https://doi.org/10.1038/s41467-024-53214-4 (nakagawa2024chemicalinhibitionof pages 7-8, nakagawa2024chemicalinhibitionof pages 1-2, nakagawa2024chemicalinhibitionof pages 9-10); *Cell Fate Programming by Transcription Factors and Epigenetic Machinery in Stomatal Development* (2023), https://doi.org/10.1101/2023.08.23.554515 (liu2023cellfateprogramming pages 4-5, liu2023cellfateprogramming pages 5-7); *bHLH transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during Arabidopsis stomatal development* (2024), https://doi.org/10.1371/journal.pbio.3002770 (liu2024bhlhtranscriptionfactors pages 13-15) | **Heterodimer with SCRM-family partner is core.** Association with SWI/SNF/HAC1 is well supported for functional cooperation, but GO complex annotations should be cautious because stable stoichiometric complex identity is less firmly defined than dimerization with SCRM/SCRM2. |
| **Applications:** MUTE/SMF knowledge is being leveraged for **stomatal trait engineering** and chemical control of stomatal differentiation; crop studies and reviews highlight editing of stomatal regulators/paralogs to tune density, transpiration, photosynthesis, and drought resilience. Stomidazolone is a research tool for selective perturbation of the MUTE step. | 2024 reviews summarizing crop engineering examples; 2024 chemical-biology primary study demonstrating selective developmental inhibition. | Stomidazolone caused dose-dependent stomatal reduction and meristemoid accumulation in Arabidopsis at **20–100 μM**. Review excerpts cite paralog editing/CRISPR applications but do not provide numeric field-performance data in gathered passages. | *Stomatal development in the changing climate* (2024), https://doi.org/10.1242/dev.202681 (chua2024stomataldevelopmentin pages 12-13); *The tomato genome encodes SPCH, MUTE, and FAMA candidates that can replace the endogenous functions of their Arabidopsis orthologs* (2019), https://doi.org/10.3389/fpls.2019.01300 (ortega2019thetomatogenome pages 1-2); *Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bHLH heterodimer via an ACT-Like domain* (2024), https://doi.org/10.1038/s41467-024-53214-4 (nakagawa2024chemicalinhibitionof pages 2-3) | **Not for direct GO function annotation.** Useful translational context only. Avoid inferring endogenous biological-process terms such as drought tolerance or climate adaptation directly onto Arabidopsis MUTE without gene-specific causal evidence in the target organism. |


*Table: This table summarizes GO-relevant evidence for Arabidopsis thaliana MUTE, emphasizing experimentally supported molecular function, biological process, localization, and interaction data while flagging annotation risks. It is designed to support careful GO annotation review using recent primary and review literature.*

**Image-supported evidence**: Nuclear localization and dose-dependent stomatal/meristemoid phenotypes under Stomidazolone treatment are supported by figure panels retrieved from Nakagawa et al. 2024. (nakagawa2024chemicalinhibitionof media 2b410197)


References

1. (liu2023cellfateprogramming pages 1-2): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Cell fate programming by transcription factors and epigenetic machinery in stomatal development. bioRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.23.554515, doi:10.1101/2023.08.23.554515. This article has 8 citations.

2. (liu2024bhlhtranscriptionfactors pages 5-7): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Bhlh transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during arabidopsis stomatal development. Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002770, doi:10.1371/journal.pbio.3002770. This article has 20 citations and is from a highest quality peer-reviewed journal.

3. (liu2024bhlhtranscriptionfactors pages 13-15): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Bhlh transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during arabidopsis stomatal development. Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002770, doi:10.1371/journal.pbio.3002770. This article has 20 citations and is from a highest quality peer-reviewed journal.

4. (nakagawa2024chemicalinhibitionof pages 1-2): Ayami Nakagawa, Krishna Mohan Sepuru, Shu Jan Yip, Hyemin Seo, Calvin M. Coffin, Kota Hashimoto, Zixuan Li, Yasutomo Segawa, Rie Iwasaki, Hiroe Kato, Daisuke Kurihara, Yusuke Aihara, Stephanie Kim, Toshinori Kinoshita, Kenichiro Itami, Soon-Ki Han, Kei Murakami, and Keiko U. Torii. Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bhlh heterodimer via an act-like domain. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53214-4, doi:10.1038/s41467-024-53214-4. This article has 8 citations and is from a highest quality peer-reviewed journal.

5. (nakagawa2024chemicalinhibitionof pages 2-3): Ayami Nakagawa, Krishna Mohan Sepuru, Shu Jan Yip, Hyemin Seo, Calvin M. Coffin, Kota Hashimoto, Zixuan Li, Yasutomo Segawa, Rie Iwasaki, Hiroe Kato, Daisuke Kurihara, Yusuke Aihara, Stephanie Kim, Toshinori Kinoshita, Kenichiro Itami, Soon-Ki Han, Kei Murakami, and Keiko U. Torii. Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bhlh heterodimer via an act-like domain. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53214-4, doi:10.1038/s41467-024-53214-4. This article has 8 citations and is from a highest quality peer-reviewed journal.

6. (liu2023cellfateprogramming pages 4-5): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Cell fate programming by transcription factors and epigenetic machinery in stomatal development. bioRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.23.554515, doi:10.1101/2023.08.23.554515. This article has 8 citations.

7. (zhou2024molecularmechanismsfor pages 2-4): Wenqi Zhou, Jieshan Liu, Wenjin Wang, Yongsheng Li, Zixu Ma, Haijun He, Xiaojuan Wang, Xiaorong Lian, Xiaoyun Dong, Xiaoqiang Zhao, and Yuqian Zhou. Molecular mechanisms for regulating stomatal formation across diverse plant species. International Journal of Molecular Sciences, 25:10403, Sep 2024. URL: https://doi.org/10.3390/ijms251910403, doi:10.3390/ijms251910403. This article has 12 citations.

8. (liu2023cellfateprogramming pages 5-7): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Cell fate programming by transcription factors and epigenetic machinery in stomatal development. bioRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.23.554515, doi:10.1101/2023.08.23.554515. This article has 8 citations.

9. (liu2023cellfateprogramming pages 2-4): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Cell fate programming by transcription factors and epigenetic machinery in stomatal development. bioRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.23.554515, doi:10.1101/2023.08.23.554515. This article has 8 citations.

10. (wakeel2021speechlessandmute pages 3-5): Abdul Wakeel, Lin Wang, and Ming Xu. Speechless and mute mediate feedback regulation of signal transduction during stomatal development. Plants, 10:432, Feb 2021. URL: https://doi.org/10.3390/plants10030432, doi:10.3390/plants10030432. This article has 11 citations.

11. (nakagawa2024chemicalinhibitionof pages 7-8): Ayami Nakagawa, Krishna Mohan Sepuru, Shu Jan Yip, Hyemin Seo, Calvin M. Coffin, Kota Hashimoto, Zixuan Li, Yasutomo Segawa, Rie Iwasaki, Hiroe Kato, Daisuke Kurihara, Yusuke Aihara, Stephanie Kim, Toshinori Kinoshita, Kenichiro Itami, Soon-Ki Han, Kei Murakami, and Keiko U. Torii. Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bhlh heterodimer via an act-like domain. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53214-4, doi:10.1038/s41467-024-53214-4. This article has 8 citations and is from a highest quality peer-reviewed journal.

12. (nakagawa2024chemicalinhibitionof pages 9-10): Ayami Nakagawa, Krishna Mohan Sepuru, Shu Jan Yip, Hyemin Seo, Calvin M. Coffin, Kota Hashimoto, Zixuan Li, Yasutomo Segawa, Rie Iwasaki, Hiroe Kato, Daisuke Kurihara, Yusuke Aihara, Stephanie Kim, Toshinori Kinoshita, Kenichiro Itami, Soon-Ki Han, Kei Murakami, and Keiko U. Torii. Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bhlh heterodimer via an act-like domain. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53214-4, doi:10.1038/s41467-024-53214-4. This article has 8 citations and is from a highest quality peer-reviewed journal.

13. (zhou2024molecularmechanismsfor pages 10-11): Wenqi Zhou, Jieshan Liu, Wenjin Wang, Yongsheng Li, Zixu Ma, Haijun He, Xiaojuan Wang, Xiaorong Lian, Xiaoyun Dong, Xiaoqiang Zhao, and Yuqian Zhou. Molecular mechanisms for regulating stomatal formation across diverse plant species. International Journal of Molecular Sciences, 25:10403, Sep 2024. URL: https://doi.org/10.3390/ijms251910403, doi:10.3390/ijms251910403. This article has 12 citations.

14. (giannoutsou2025guardiansofwater pages 6-8): E. Giannoutsou, I-D S Adamakis, and D. Samakovli. Guardians of water and gas exchange: adaptive dynamics of stomatal development and patterning. Plants, Aug 2025. URL: https://doi.org/10.3390/plants14152405, doi:10.3390/plants14152405. This article has 4 citations.

15. (chua2024stomataldevelopmentin pages 12-13): Li Cong Chua and On Sun Lau. Stomatal development in the changing climate. Development (Cambridge, England), Oct 2024. URL: https://doi.org/10.1242/dev.202681, doi:10.1242/dev.202681. This article has 38 citations.

16. (nakagawa2024chemicalinhibitionof pages 10-11): Ayami Nakagawa, Krishna Mohan Sepuru, Shu Jan Yip, Hyemin Seo, Calvin M. Coffin, Kota Hashimoto, Zixuan Li, Yasutomo Segawa, Rie Iwasaki, Hiroe Kato, Daisuke Kurihara, Yusuke Aihara, Stephanie Kim, Toshinori Kinoshita, Kenichiro Itami, Soon-Ki Han, Kei Murakami, and Keiko U. Torii. Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bhlh heterodimer via an act-like domain. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53214-4, doi:10.1038/s41467-024-53214-4. This article has 8 citations and is from a highest quality peer-reviewed journal.

17. (nakagawa2024chemicalinhibitionof media 2b410197): Ayami Nakagawa, Krishna Mohan Sepuru, Shu Jan Yip, Hyemin Seo, Calvin M. Coffin, Kota Hashimoto, Zixuan Li, Yasutomo Segawa, Rie Iwasaki, Hiroe Kato, Daisuke Kurihara, Yusuke Aihara, Stephanie Kim, Toshinori Kinoshita, Kenichiro Itami, Soon-Ki Han, Kei Murakami, and Keiko U. Torii. Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bhlh heterodimer via an act-like domain. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53214-4, doi:10.1038/s41467-024-53214-4. This article has 8 citations and is from a highest quality peer-reviewed journal.

18. (nakagawa2024chemicalinhibitionof pages 10-10): Ayami Nakagawa, Krishna Mohan Sepuru, Shu Jan Yip, Hyemin Seo, Calvin M. Coffin, Kota Hashimoto, Zixuan Li, Yasutomo Segawa, Rie Iwasaki, Hiroe Kato, Daisuke Kurihara, Yusuke Aihara, Stephanie Kim, Toshinori Kinoshita, Kenichiro Itami, Soon-Ki Han, Kei Murakami, and Keiko U. Torii. Chemical inhibition of stomatal differentiation by perturbation of the master-regulatory bhlh heterodimer via an act-like domain. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53214-4, doi:10.1038/s41467-024-53214-4. This article has 8 citations and is from a highest quality peer-reviewed journal.

19. (ortega2019thetomatogenome pages 1-2): Alfonso Ortega, Alberto de Marcos, Jonatan Illescas-Miranda, Montaña Mena, and Carmen Fenoll. The tomato genome encodes spch, mute, and fama candidates that can replace the endogenous functions of their arabidopsis orthologs. Frontiers in Plant Science, Oct 2019. URL: https://doi.org/10.3389/fpls.2019.01300, doi:10.3389/fpls.2019.01300. This article has 43 citations.