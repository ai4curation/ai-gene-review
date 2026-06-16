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

- Gene symbol: EFR
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: C0LGT6
Entry Name: EFR_ARATH
Gene Name: EFR
Locus Tag: At5g20480 {ECO:0000312|Araport:AT5G20480}
Protein Name: LRR receptor-like serine/threonine-protein kinase EFR
EC Number: 2.7.11.1
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: Constitutes the pattern-recognition receptor (PPR) that determines the specific perception of elongation factor Tu (EF-Tu), a potent elicitor of the defense response to pathogen-associated molecular patterns (PAMPs); phosphorylates BIK1 upon elicitation to regulate immune responses such as defense hormone expression (e.g. jasmonic acid (JA) and salicylic acid (SA)) (PubMed:29649442). Reduces transformation by Rhizobium radiobacter probably by inducing plant defense during the interaction. Binding to the effector AvrPto1 from P.syringae blocks the downstream plant immune response while interaction with hopD2 decreases the phosphorylation level of EFR upon elf18 treatment. Specific endoplasmic reticulum quality control components (ERD2B, CRT3, UGGT and STT3A) are required for the biogenesis of EFR.
Subcellular Location: Cell membrane; Single-pass type I membrane protein. Endomembrane system; Single-pass type I membrane protein.
Subunit: Binds to Pseudomonas syringae AvrPto1 and (via the kinase and cytoplasmic domains) to hopD2. Interacts with SERK3/BAK1, SERK4/BKK1, SERK1 and SERK2 in a specific ligand-induced manner. Binds to IOS1 (PubMed:27317676). Binds to BIK1 in the absence of pathogen elicitor; dissociates upon pathogen-associated molecular pattern (PAMP)-triggered activation (PubMed:29649442).
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


# Gene Research Report for GO Annotation Review: **EFR (At5g20480)**, *Arabidopsis thaliana*

## 1. Executive summary
EF-TU RECEPTOR (EFR; At5g20480) encodes a plasma-membrane, single-pass leucine-rich repeat receptor-like kinase (LRR-RK) that functions as a pattern-recognition receptor (PRR) for the bacterial elongation factor Tu (EF‑Tu)–derived N-terminal peptides elf18/elf26, thereby initiating pattern-triggered immunity (PTI). EFR activation involves rapid ligand-induced recruitment of SERK-family co-receptors (especially BAK1/SERK3, also BKK1/SERK4 and others) and extensive phosphorylation dynamics in the receptor complex. Recent work (2024) shows that EFR signaling is not explained solely by “EFR kinase phosphorylates downstream substrates”; rather, EFR can act **non-catalytically** to allosterically activate the co-receptor kinase BAK1, enabling BAK1 to phosphorylate downstream cytosolic kinases such as BIK1. Key EFR phosphosites (Y836 and activation-loop S887/S888) are required for productive receptor-complex activation, while EFR’s own catalytic activity can be dispensable for antibacterial immunity in vivo. (muhlenbeck2024allostericactivationof pages 3-5, henning2024allostericactivationof pages 3-5, bender2021activationloopphosphorylation pages 1-2, bender2021activationloopphosphorylation pages 5-6)

EFR biogenesis is unusually dependent on endoplasmic reticulum (ER) quality control (ER-QC) and N-glycosylation factors (e.g., CRT3, UGGT, STT3A; and a separate SDF2–ERdj3B–BiP complex). Disruption of these ER-QC components reduces stable accumulation of functional EFR and impairs elf18/elf26 binding and signaling, highlighting an annotation-relevant distinction between *where the mature active receptor signals (plasma membrane)* and *where it is matured/inspected (ER)*. (nekrasov2009controlofthe pages 1-1, saijo2009receptorqualitycontrol pages 3-4)

Across the EFR-focused literature retrieved here, there is **no direct experimental support** for annotating EFR to apoptosis/animal-style inflammatory signaling, pyroptosis, neuronal functions, or stable nuclear localization; “cell death” appears mainly as a generic immune-context concept or linked to other signaling hubs (e.g., BAK1/BKK1), not as a demonstrated core EFR function. (roux2011thearabidopsisleucinerich pages 1-2, saijo2009receptorqualitycontrol pages 1-2)

## 2. Molecular function
### 2.1 Key concepts and definitions (current understanding)
**Pattern-recognition receptor (PRR)**: a host cell-surface receptor that recognizes conserved microbial molecules (MAMPs/PAMPs) and triggers innate immune responses. EFR is a prototypical Arabidopsis PRR for proteinaceous bacterial EF‑Tu epitopes (elf18/elf26). (roux2011thearabidopsisleucinerich pages 1-2, nekrasov2009controlofthe pages 1-1)

**Non-RD receptor kinase**: protein kinases lacking the canonical Arg in the HRD catalytic motif, frequently associated with innate immune signaling across kingdoms. EFR is a non-RD LRR-RK; its complex activation can rely on phosphorylation-driven conformational changes and co-receptor kinase activity, not necessarily EFR’s own catalysis. (bender2021activationloopphosphorylation pages 1-2, muhlenbeck2024allostericactivationof pages 1-2)

### 2.2 Core biochemical activity and substrate specificity
EFR is biochemically a receptor-like **Ser/Thr protein kinase** (EC 2.7.11.1) with an active kinase domain in vitro and ligand-induced phosphorylation in vivo, which supports GO molecular function annotation to protein kinase activity. (bender2021activationloopphosphorylation pages 1-2)

However, in planta genetics/functional complementation demonstrate that **EFR catalytic activity can be dispensable for elf18-triggered immune outputs and antibacterial immunity**: catalytically impaired mutants (e.g., D849N, K851E) can still support elf18-triggered ROS, MAPK activation, seedling growth inhibition and pathogen restriction, implying EFR has a non-catalytic signaling role within the receptor complex. (bender2021activationloopphosphorylation pages 2-3, bender2021activationloopphosphorylation pages 1-2, bender2021activationloopphosphorylation pages 5-6)

**Downstream phosphorylation and the BIK1 question (direct vs indirect):** the best-supported current model (2024) is that EFR (once appropriately phosphorylated at Y836 and S887/S888) promotes **BAK1 catalytic activation allosterically**, and BAK1 then performs key phosphorylations including **BIK1 trans-phosphorylation**; kinase-dead EFR still retains some capacity to enhance BAK1→BIK1 phosphorylation, supporting the “non-catalytic EFR” model. (henning2024allostericactivationof pages 3-5, henning2024allostericactivationof pages 2-3)

This is important for GO: the strongest evidence supports EFR as a PRR and complex activator, but **not** as the sole/primary kinase directly phosphorylating BIK1 under physiological conditions. (bender2021activationloopphosphorylation pages 2-3, henning2024allostericactivationof pages 3-5)

### 2.3 Activation/maturation mechanisms
#### Ligand perception and co-receptor recruitment
Elf18 perception triggers rapid receptor complex formation: EFR heteromerizes with BAK1 within ~5 minutes of elf18 treatment, and MS of EFR immunoprecipitates identifies multiple SERK-family peptides detected only after elf18 elicitation. (roux2011thearabidopsisleucinerich pages 2-3)

Proteomic immunoprecipitation shows ligand-enhanced co-purification consistent with stimulus-dependent recruitment, with marked spectral count increases for BAK1 and SERK4 after elf18 treatment (e.g., BAK1 0/0/2 → 9/2/7; SERK4 0/0/0 → 12/4/6 across replicates). (roux2011identificationandcharacterization pages 172-176)

#### Phosphorylation logic, phosphosites, and “non-catalytic” activation
Recent mechanistic work identifies specific required EFR phosphosites for receptor-complex activation: **EFR Y836** and activation-loop **S887/S888** are required for in vivo signaling; phospho-ablative mutants block ligand-induced BAK1 S612 phosphorylation (an active-complex marker). (henning2024allostericactivationof pages 3-5, henning2024allostericactivationof pages 2-3)

In a complementary study, phosphoproteomics identified **12 high-confidence Ser/Thr phosphorylation sites** on EFR, some detected only after elf18 stimulation, supporting ligand-triggered phosphoregulation. (bender2021activationloopphosphorylation pages 5-6)

### 2.4 Recent developments and expert analysis (2023–2024 priority)
A central 2024 advance is the proposed **conformational toggle/allosteric activation model**: BAK1 phosphorylates EFR in the activation loop to stabilize an active-like EFR conformation; EFR then allosterically enhances BAK1 activity (likely affecting BAK1 αC-helix positioning), enabling BAK1-driven phosphorylation of downstream targets such as BIK1. (muhlenbeck2024allostericactivationof pages 1-2)

This shifts interpretation of EFR from a purely catalytic kinase to a receptor whose **structural state and phosphorylation** determine its ability to activate co-receptors and transmit immune signals. (henning2024allostericactivationof pages 3-5)

## 3. Biological process roles
### 3.1 Best-supported processes in *Arabidopsis*
EFR-mediated recognition of elf18/elf26 triggers canonical PTI outputs: **Ca2+ influx/ion fluxes, ROS burst, MAPK and CDPK activation, defense gene induction, callose deposition, seedling growth inhibition**, and enhanced resistance to bacterial infection. (roux2011thearabidopsisleucinerich pages 1-2, bender2021activationloopphosphorylation pages 2-3, nekrasov2009controlofthe pages 1-1)

EFR is experimentally linked to **antibacterial immunity**, including induced resistance restricting *Pseudomonas syringae* pv. tomato DC3000 after elf18 pretreatment; this induced resistance is lost in efr mutants but retained in lines expressing catalytically impaired EFR variants. (bender2021activationloopphosphorylation pages 5-6)

EFR also contributes to reduced susceptibility to *Agrobacterium* transformation/interaction, consistent with PTI restricting transformation efficiency; in one assay, WT and catalytic-site complementation lines show ~**100-fold lower** GUS readout than the efr-1 knockout after *Agrobacterium*-mediated transient transformation. (bender2021activationloopphosphorylation pages 5-6)

### 3.2 Context-specific and “non-core” process claims
An OMV (outer membrane vesicle) priming study (2023) reports that mutations in EFR (as well as FLS2 and BAK1) **did not significantly affect OMV-mediated priming**, indicating that not all immune priming phenomena are EFR-dependent and cautioning against over-general “immune priming” annotations for EFR. (chalupowicz2023bacterialoutermembrane pages 1-2)

## 4. Cellular localization and complexes
### 4.1 Subcellular localization
EFR is a cell-surface transmembrane receptor whose mature signaling-competent pool functions at the **plasma membrane**. Defects in ER quality control cause ER retention and degradation rather than plasma-membrane accumulation. (nekrasov2009controlofthe pages 1-1)

Biochemical fractionation in an ER-QC study detected endogenous EFR in both **PM-enriched** and **ER/microsomal** fractions (EFR co-fractionated with PM and ER markers), consistent with transit through the secretory system and a biogenesis pool in ER/microsomes. (saijo2009receptorqualitycontrol pages 3-4)

### 4.2 Receptor complexes
#### Ligand-induced SERK co-receptor complex
EFR forms ligand-induced complexes with BAK1 and other SERK family members after elf18 elicitation, supporting a “receptor/co-receptor complex” cellular component concept. (roux2011thearabidopsisleucinerich pages 2-3, roux2011identificationandcharacterization pages 198-201)

#### ER quality-control and biogenesis dependencies
EFR is an ER-QC client: 
* CRT3 and UGGT are required for stable accumulation of functional EFR and for elf26 binding, with strong alleles causing reduced steady-state EFR protein without corresponding transcript decrease. (saijo2009receptorqualitycontrol pages 3-4)
* A distinct ER luminal complex **SDF2–ERdj3B–BiP** is required for plasma-membrane EFR accumulation; sdf2 mutants show ER retention and degradation of EFR. (nekrasov2009controlofthe pages 1-1)

These findings support separating CC annotations (PM for function; ER for maturation/quality control) and avoiding overstatement that EFR “localizes to ER” as its functional signaling site. (nekrasov2009controlofthe pages 1-1, saijo2009receptorqualitycontrol pages 3-4)

## 5. Annotation-risk assessment (GO curation guidance)
### 5.1 Core vs context-specific annotations
**Core function (high confidence):** PRR activity for EF‑Tu-derived elf peptides; PTI signaling at the plasma membrane; stimulus-dependent receptor complex formation with SERKs/BAK1. (roux2011thearabidopsisleucinerich pages 1-2, roux2011thearabidopsisleucinerich pages 2-3)

**Core mechanistic nuance (important for MF interpretation):** EFR has kinase activity in vitro, but **EFR catalytic activity is not strictly required** for antibacterial immunity; EFR’s key role may be structural/allosteric activation of BAK1 and organization of a productive signaling complex. (bender2021activationloopphosphorylation pages 2-3, henning2024allostericactivationof pages 3-5)

**Context-specific/downstream consequences (moderate confidence, annotate carefully):** reduction of *Agrobacterium*-mediated transformation (likely a PTI consequence), and additional phenotypes that are indirect outcomes of broad immune activation. (bender2021activationloopphosphorylation pages 5-6)

### 5.2 Avoiding over-extended or incorrect annotations
**Apoptosis / programmed cell death / pyroptosis / neuronal / inflammatory signaling:** No direct evidence in the retrieved EFR-centered studies supports these as EFR biological processes or molecular functions; “cell death” appears mainly as a general immune-system context or linked to other hubs, not EFR execution. (roux2011thearabidopsisleucinerich pages 1-2, saijo2009receptorqualitycontrol pages 1-2)

**Nucleus/cytosol localization:** No evidence here supports stable EFR localization to nucleus or cytosol. ER-associated degradation may involve cytosolic steps for misfolded proteins, but that does not justify cytosolic/nuclear CC annotations for functional EFR. (nekrasov2009controlofthe pages 1-1)

## 6. Key literature (URLs and publication dates)

### High-priority mechanistic and EFR-specific primary studies
1. **Mühlenbeck H. et al.** “Allosteric activation of the co-receptor BAK1 by the EFR receptor kinase initiates immune signaling.” *eLife* (Jul 2024). https://doi.org/10.7554/elife.92110 (henning2024allostericactivationof pages 3-5)
2. **Bender K.W. et al.** “Activation loop phosphorylation of a non-RD receptor kinase initiates plant innate immune signaling.” *PNAS* (Sep 2021). https://doi.org/10.1073/pnas.2108242118 (bender2021activationloopphosphorylation pages 1-2)
3. **Roux M. et al.** “The Arabidopsis LRR-RLKs BAK1/SERK3 and BKK1/SERK4 are required for innate immunity…” *The Plant Cell* (Jun 2011). https://doi.org/10.1105/tpc.111.084301 (roux2011thearabidopsisleucinerich pages 2-3)
4. **Saijo Y. et al.** “Receptor quality control in the endoplasmic reticulum for plant innate immunity.” *The EMBO Journal* (Nov 2009). https://doi.org/10.1038/emboj.2009.263 (saijo2009receptorqualitycontrol pages 3-4)
5. **Nekrasov V. et al.** “Control of the pattern-recognition receptor EFR by an ER protein complex in plant immunity.” *The EMBO Journal* (Nov 2009). https://doi.org/10.1038/emboj.2009.262 (nekrasov2009controlofthe pages 1-1)

### Recent contextual studies and reviews (authoritative expert synthesis)
6. **Bender K.W., Zipfel C.** “Paradigms of receptor kinase signaling in plants.” *Biochemical Journal* (Jun 2023). https://doi.org/10.1042/bcj20220372 (retrieved but not evidence-extracted here; see paper_search output) 
7. **Chalupowicz L. et al.** “Bacterial outer membrane vesicles induce a transcriptional shift…” *Journal of Extracellular Vesicles* (Jan 2023). https://doi.org/10.1002/jev2.12285 (chalupowicz2023bacterialoutermembrane pages 1-2)

## GO-focused synthesis table
| GO aspect (MF/BP/CC) | Proposed term | Evidence summary (1-2 clauses) | Key citations | Annotation risk notes |
|---|---|---|---|---|
| MF | pattern recognition receptor activity | EFR specifically perceives the bacterial EF-Tu epitope elf18/elf26 and initiates immune signaling; loss of EFR abolishes elf-ligand responsiveness. | (bender2021activationloopphosphorylation pages 2-3, roux2011thearabidopsisleucinerich pages 1-2, nekrasov2009controlofthe pages 1-1) | Core function; strongest MF annotation. Keep ligand specificity centered on EF-Tu-derived peptides, not broad all-bacteria recognition. |
| MF | protein serine/threonine kinase activity | EFR has an active cytoplasmic kinase domain in vitro and is phosphorylated in vivo, consistent with receptor kinase biochemistry. | (bender2021activationloopphosphorylation pages 1-2) | Support exists, but signaling output does not strictly require EFR catalytic activity in vivo; annotate cautiously as biochemical capability rather than sole signaling mechanism. |
| MF | non-RD receptor kinase signaling activity | EFR is a non-RD LRR-RK whose activation depends on phosphorylation-dependent conformational change rather than simple reciprocal catalysis. | (muhlenbeck2024allostericactivationof pages 1-2, henning2024allostericactivationof pages 1-2) | Useful mechanistic note for review, but may not map cleanly to a standard GO MF term; avoid inventing overly specific GO-like labels if unsupported in ontology. |
| BP | pattern-triggered immunity | elf18 perception by EFR triggers canonical PTI outputs including ROS burst, MAPK activation, Ca2+-linked signaling, defense gene induction, callose deposition, and seedling growth inhibition. | (roux2011thearabidopsisleucinerich pages 1-2, bender2021activationloopphosphorylation pages 5-6, bender2021activationloopphosphorylation pages 2-3, nekrasov2009controlofthe pages 1-1) | Core biological process; strongest BP annotation. |
| BP | defense response to bacterium | EFR contributes to antibacterial immunity and induced resistance, including restriction of Pseudomonas syringae pv. tomato DC3000 growth after elf18 pretreatment. | (bender2021activationloopphosphorylation pages 5-6, saijo2009receptorqualitycontrol pages 3-4) | Well supported; keep framed as bacterial defense, not generalized resistance to all pathogens. |
| BP | regulation of immune receptor signaling by receptor complex activation | Ligand perception drives rapid EFR association with BAK1/SERKs and activation-loop-dependent signaling, with BAK1 S612 phosphorylation marking active complexes. | (muhlenbeck2024allostericactivationof pages 3-5, henning2024allostericactivationof pages 3-5, roux2011thearabidopsisleucinerich pages 2-3) | Strong mechanistic process support; avoid overextending to direct phosphorylation of all downstream substrates by EFR. |
| BP | positive regulation of BAK1-mediated phosphorylation events | Recent work supports an allosteric model in which phosphorylated EFR promotes BAK1 activity and thereby BAK1-mediated BIK1 phosphorylation. | (muhlenbeck2024allostericactivationof pages 3-5, henning2024allostericactivationof pages 3-5, henning2024allostericactivationof pages 2-3) | Supported mechanistically, but context-specific and relatively specialized; not equivalent to direct EFR→BIK1 kinase-substrate annotation. |
| BP | protein maturation involved in receptor biogenesis | Functional EFR accumulation requires ER quality-control and N-glycosylation factors including CRT3, UGGT, STT3A, and SDF2-ERdj3B-BiP. | (nekrasov2009controlofthe pages 1-1, saijo2009receptorqualitycontrol pages 3-4, saijo2009receptorqualitycontrol pages 1-2) | Best treated as maturation/biogenesis dependency rather than EFR “performing” ERQC; avoid annotating EFR as an ERQC factor itself. |
| BP | negative regulation of Agrobacterium-mediated transformation | EFR-dependent immune activation reduces Agrobacterium transformation/transient transformation efficiency. | (bender2021activationloopphosphorylation pages 5-6) | Supported but context-specific; likely downstream consequence of immune activation rather than core dedicated function. |
| CC | plasma membrane | EFR is a surface-exposed transmembrane LRR-RK and the active signaling receptor functions at the plasma membrane. | (nekrasov2009controlofthe pages 1-1, saijo2009receptorqualitycontrol pages 3-4, roux2011thearabidopsisleucinerich pages 2-3) | Core CC annotation; strongest localization term. |
| CC | receptor complex | Upon elf18 treatment, EFR forms ligand-induced complexes with BAK1 and additional SERK family co-receptors. | (roux2011thearabidopsisleucinerich pages 2-3, roux2011identificationandcharacterization pages 172-176, roux2011identificationandcharacterization pages 198-201) | Strong support for signaling-complex membership; complex is stimulus-dependent. |
| CC | endoplasmic reticulum / endomembrane system | EFR is detected in ER/microsomal fractions during biogenesis and interacts with ER-QC machinery before plasma membrane accumulation. | (saijo2009receptorqualitycontrol pages 3-4, nekrasov2009controlofthe pages 1-1) | Appropriate as biogenesis/localization context; avoid implying the mature active receptor primarily signals from ER. |
| CC | cytosol / nucleus | No direct evidence in the retrieved EFR literature supports stable cytosolic or nuclear localization of EFR itself. | (nekrasov2009controlofthe pages 1-1, saijo2009receptorqualitycontrol pages 1-2, roux2011identificationandcharacterization pages 130-134) | Do not annotate EFR to cytosol or nucleus based on downstream partners such as BIK1. |
| BP | apoptosis / programmed cell death / hypersensitive response | Retrieved EFR-focused studies do not directly support EFR as an executor of apoptosis, PCD, HR, pyroptosis, or animal-style inflammatory pathways. | (nekrasov2009controlofthe pages 1-1, roux2011thearabidopsisleucinerich pages 1-2, saijo2009receptorqualitycontrol pages 1-2, chalupowicz2023bacterialoutermembrane pages 1-2) | Avoid overextension; cell-death mentions are generic immune-context statements or relate to BAK1/BKK1, not direct EFR function. |


*Table: This table summarizes conservative, evidence-based GO annotation proposals for Arabidopsis EFR (At5g20480). It highlights core functions and locations while flagging context-specific or unsupported annotations that should be avoided during review.*


References

1. (muhlenbeck2024allostericactivationof pages 3-5): Henning Mühlenbeck, Yuko Tsutsui, Mark A. Lemmon, Kyle W. Bender, and Cyril Zipfel. Allosteric activation of the co-receptor bak1 by the efr receptor kinase initiates immune signaling. Unknown journal, Nov 2024. URL: https://doi.org/10.7554/elife.92110.1, doi:10.7554/elife.92110.1.

2. (henning2024allostericactivationof pages 3-5): Henning Mühlenbeck, Yuko Tsutsui, Mark A Lemmon, Kyle W Bender, and Cyril Zipfel. Allosteric activation of the co-receptor bak1 by the efr receptor kinase initiates immune signaling. eLife, Jul 2024. URL: https://doi.org/10.7554/elife.92110, doi:10.7554/elife.92110. This article has 32 citations and is from a domain leading peer-reviewed journal.

3. (bender2021activationloopphosphorylation pages 1-2): Kyle W. Bender, Daniel Couto, Yasuhiro Kadota, Alberto P. Macho, Jan Sklenar, Paul Derbyshire, Marta Bjornson, Thomas A. DeFalco, Annalise Petriello, Maria Font Farre, Benjamin Schwessinger, Vardis Ntoukakis, Lena Stransfeld, Alexandra M. E. Jones, Frank L. H. Menke, and Cyril Zipfel. Activation loop phosphorylation of a non-rd receptor kinase initiates plant innate immune signaling. Proceedings of the National Academy of Sciences, Sep 2021. URL: https://doi.org/10.1073/pnas.2108242118, doi:10.1073/pnas.2108242118. This article has 30 citations and is from a highest quality peer-reviewed journal.

4. (bender2021activationloopphosphorylation pages 5-6): Kyle W. Bender, Daniel Couto, Yasuhiro Kadota, Alberto P. Macho, Jan Sklenar, Paul Derbyshire, Marta Bjornson, Thomas A. DeFalco, Annalise Petriello, Maria Font Farre, Benjamin Schwessinger, Vardis Ntoukakis, Lena Stransfeld, Alexandra M. E. Jones, Frank L. H. Menke, and Cyril Zipfel. Activation loop phosphorylation of a non-rd receptor kinase initiates plant innate immune signaling. Proceedings of the National Academy of Sciences, Sep 2021. URL: https://doi.org/10.1073/pnas.2108242118, doi:10.1073/pnas.2108242118. This article has 30 citations and is from a highest quality peer-reviewed journal.

5. (nekrasov2009controlofthe pages 1-1): Vladimir Nekrasov, Jing Li, Martine Batoux, Milena Roux, Zhao-Hui Chu, Severine Lacombe, Alejandra Rougon, Pascal Bittel, Marta Kiss-Papp, Delphine Chinchilla, H Peter van Esse, Lucia Jorda, Benjamin Schwessinger, Valerie Nicaise, Bart P H J Thomma, Antonio Molina, Jonathan D G Jones, and Cyril Zipfel. Control of the pattern‐recognition receptor efr by an er protein complex in plant immunity. The EMBO Journal, 28:3428-3438, Nov 2009. URL: https://doi.org/10.1038/emboj.2009.262, doi:10.1038/emboj.2009.262. This article has 362 citations.

6. (saijo2009receptorqualitycontrol pages 3-4): Yusuke Saijo, Nico Tintor, Xunli Lu, Philipp Rauf, Karolina Pajerowska-Mukhtar, Heidrun Häweker, Xinnian Dong, Silke Robatzek, and Paul Schulze-Lefert. Receptor quality control in the endoplasmic reticulum for plant innate immunity. The EMBO Journal, 28:3439-3449, Nov 2009. URL: https://doi.org/10.1038/emboj.2009.263, doi:10.1038/emboj.2009.263. This article has 310 citations.

7. (roux2011thearabidopsisleucinerich pages 1-2): Milena Roux, Benjamin Schwessinger, Catherine Albrecht, Delphine Chinchilla, Alexandra Jones, Nick Holton, Frederikke Gro Malinovsky, Mahmut Tör, Sacco de Vries, and Cyril Zipfel. The <i>arabidopsis</i> leucine-rich repeat receptor–like kinases bak1/serk3 and bkk1/serk4 are required for innate immunity to hemibiotrophic and biotrophic pathogens. Jun 2011. URL: https://doi.org/10.1105/tpc.111.084301, doi:10.1105/tpc.111.084301. This article has 851 citations.

8. (saijo2009receptorqualitycontrol pages 1-2): Yusuke Saijo, Nico Tintor, Xunli Lu, Philipp Rauf, Karolina Pajerowska-Mukhtar, Heidrun Häweker, Xinnian Dong, Silke Robatzek, and Paul Schulze-Lefert. Receptor quality control in the endoplasmic reticulum for plant innate immunity. The EMBO Journal, 28:3439-3449, Nov 2009. URL: https://doi.org/10.1038/emboj.2009.263, doi:10.1038/emboj.2009.263. This article has 310 citations.

9. (muhlenbeck2024allostericactivationof pages 1-2): Henning Mühlenbeck, Yuko Tsutsui, Mark A. Lemmon, Kyle W. Bender, and Cyril Zipfel. Allosteric activation of the co-receptor bak1 by the efr receptor kinase initiates immune signaling. Unknown journal, Nov 2024. URL: https://doi.org/10.7554/elife.92110.1, doi:10.7554/elife.92110.1.

10. (bender2021activationloopphosphorylation pages 2-3): Kyle W. Bender, Daniel Couto, Yasuhiro Kadota, Alberto P. Macho, Jan Sklenar, Paul Derbyshire, Marta Bjornson, Thomas A. DeFalco, Annalise Petriello, Maria Font Farre, Benjamin Schwessinger, Vardis Ntoukakis, Lena Stransfeld, Alexandra M. E. Jones, Frank L. H. Menke, and Cyril Zipfel. Activation loop phosphorylation of a non-rd receptor kinase initiates plant innate immune signaling. Proceedings of the National Academy of Sciences, Sep 2021. URL: https://doi.org/10.1073/pnas.2108242118, doi:10.1073/pnas.2108242118. This article has 30 citations and is from a highest quality peer-reviewed journal.

11. (henning2024allostericactivationof pages 2-3): Henning Mühlenbeck, Yuko Tsutsui, Mark A Lemmon, Kyle W Bender, and Cyril Zipfel. Allosteric activation of the co-receptor bak1 by the efr receptor kinase initiates immune signaling. eLife, Jul 2024. URL: https://doi.org/10.7554/elife.92110, doi:10.7554/elife.92110. This article has 32 citations and is from a domain leading peer-reviewed journal.

12. (roux2011thearabidopsisleucinerich pages 2-3): Milena Roux, Benjamin Schwessinger, Catherine Albrecht, Delphine Chinchilla, Alexandra Jones, Nick Holton, Frederikke Gro Malinovsky, Mahmut Tör, Sacco de Vries, and Cyril Zipfel. The <i>arabidopsis</i> leucine-rich repeat receptor–like kinases bak1/serk3 and bkk1/serk4 are required for innate immunity to hemibiotrophic and biotrophic pathogens. Jun 2011. URL: https://doi.org/10.1105/tpc.111.084301, doi:10.1105/tpc.111.084301. This article has 851 citations.

13. (roux2011identificationandcharacterization pages 172-176): M Roux. Identification and characterization of efr-interacting proteins. Unknown journal, 2011.

14. (chalupowicz2023bacterialoutermembrane pages 1-2): Laura Chalupowicz, Gideon Mordukhovich, Nofar Assoline, Leron Katsir, Noa Sela, and Ofir Bahar. Bacterial outer membrane vesicles induce a transcriptional shift in arabidopsis towards immune system activation leading to suppression of pathogen growth in planta. Journal of Extracellular Vesicles, Jan 2023. URL: https://doi.org/10.1002/jev2.12285, doi:10.1002/jev2.12285. This article has 39 citations and is from a domain leading peer-reviewed journal.

15. (roux2011identificationandcharacterization pages 198-201): M Roux. Identification and characterization of efr-interacting proteins. Unknown journal, 2011.

16. (henning2024allostericactivationof pages 1-2): Henning Mühlenbeck, Yuko Tsutsui, Mark A Lemmon, Kyle W Bender, and Cyril Zipfel. Allosteric activation of the co-receptor bak1 by the efr receptor kinase initiates immune signaling. eLife, Jul 2024. URL: https://doi.org/10.7554/elife.92110, doi:10.7554/elife.92110. This article has 32 citations and is from a domain leading peer-reviewed journal.

17. (roux2011identificationandcharacterization pages 130-134): M Roux. Identification and characterization of efr-interacting proteins. Unknown journal, 2011.