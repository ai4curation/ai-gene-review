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

- Gene symbol: SPCH
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q700C7
Entry Name: SPCH_ARATH
Gene Name: SPCH
Locus Tag: At5g53210 {ECO:0000312|Araport:AT5G53210}
Gene Synonyms: BHLH98 {ECO:0000303|PubMed:12679534,
Protein Name: Transcription factor SPEECHLESS
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: Transcription factor acting as an integration node for stomata and brassinosteroid (BR) signaling pathways to control stomatal initiation and development (PubMed:22466366, PubMed:28507175). Activates transcription when in the presence of SCRM/ICE1 (PubMed:28507175). Functions as a dimer with SCRM or SCRM2 during stomatal initiation (PubMed:18641265). Required for the initiation, the spacing and the formation of stomata, by promoting the first asymmetric cell divisions (PubMed:19008449, PubMed:25680231, PubMed:25843888). Together with FMA and MUTE, modulates the stomata formation. Involved in the regulation of growth reduction under osmotic stress (e.g. mannitol), associated with a quick decrease of meristemoid mother cells (MMCs) number lower stomatal index and density (PubMed:25381317).
Subcellular Location: Nucleus
Subunit: Homodimer (Probable). Forms dimers with SCRM and SCRM2 (PubMed:18641265, PubMed:28507175). May interact with CDKA-1 (PubMed:25680231).
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


## Executive summary

**Gene/product:** *Arabidopsis thaliana* **SPCH** (SPEECHLESS; UniProt Q700C7; At5g53210) encodes a **basic helix–loop–helix (bHLH) sequence-specific transcription factor** that is **necessary and sufficient to initiate stomatal lineage entry** and promote the **asymmetric (amplifying/entry) cell divisions** that generate stomatal precursors. The consensus view from recent authoritative synthesis (2024) is that SPCH is the **master regulator of stomatal lineage initiation** whose activity is tuned by peptide-receptor/MAPK signaling and multiple environmental inputs. (chua2024stomataldevelopmentin pages 1-2)

**Core molecular function (GO MF focus):** SPCH binds promoter cis-elements consistent with **E-box/G-box class motifs** and acts primarily as a transcriptional activator of stomatal-lineage regulators; direct binding/activation is supported by **EMSA and reporter activation** for at least the **MUTE** promoter, and by genome-scale association/motif enrichment from ChIP-seq. (cao2021arabidopsiscryptochrome1 pages 6-9, marcos2017amutationin pages 27-30, liu2024bhlhtranscriptionfactors pages 3-5)

**Key complexes and localization (GO CC focus):** SPCH functions in the **nucleus**, typically as an obligate heterodimer with bHLH partners **SCREAM/ICE1 (SCRM/ICE1)** and **SCRM2**. Nuclear protein–protein interaction data also support SPCH association with **PP2A A subunits** (stabilizing dephosphorylation) and with **AGB1** (inhibitory binding to the bHLH DNA-binding domain). (bian2020proteinphosphatase2a pages 6-7, cao2021arabidopsiscryptochrome1 pages 6-9, chua2024stomataldevelopmentin pages 1-2)

**Regulatory mechanism (activation/maturation):** SPCH is not known to undergo proteolytic maturation; instead, its effective activity depends on **phosphorylation state and protein stability**. SPCH is regulated by **CDKA;1 phosphorylation at Ser186 (positive)** and by **MAPK (YDA→MPK3/6) and BIN2 (BR pathway) phosphorylation (generally inhibitory/ destabilizing)**; **PP2A dephosphorylation stabilizes SPCH** and counteracts phosphorylation-dependent **proteasome-mediated degradation**, evidenced by MG132 rescue. (yang2015phosphorylationofserine pages 1-5, bian2020proteinphosphatase2a pages 6-7, bian2020proteinphosphatase2a pages 5-6)

**Recent developments (prioritizing 2023–2024):** A 2024 PLOS Biology study integrates scRNA-seq and ChIP-seq to propose that stomatal bHLH factors (including SPCH) act in a chromatin context where targets can be repressed prior to activation, and that bHLHs cooperate with chromatin regulators (SWI/SNF and HAC1 identified by proximity labeling) to enable fate transitions; importantly, SPCH is solidly supported as the initiator but its role as a “pioneer factor” remains unresolved. A 2024 Development review contextualizes SPCH as a central integrator of environmental plasticity of stomatal development under climate-relevant cues. (liu2024bhlhtranscriptionfactors pages 1-2, liu2024bhlhtranscriptionfactors pages 15-16, chua2024stomataldevelopmentin pages 1-2)

**Annotation risk/exclusions:** Across the retrieved evidence base, there is **no support** for annotations involving apoptosis/developmental cell death, neuronal roles, inflammatory signaling, pyroptosis, synaptic remodeling, or proteolytic processing/maturation. (cao2021arabidopsiscryptochrome1 pages 6-9, bian2020proteinphosphatase2a pages 7-9, chua2024stomataldevelopmentin pages 1-2)


## Molecular function

### Key concepts and definitions (current understanding)

1. **bHLH transcription factor activity:** bHLH proteins generally recognize **E-box (CANNTG) / G-box (CACGTG)**-class DNA elements via their basic region and dimerize via the HLH region. SPCH is widely described as a stomatal-lineage **master bHLH regulator**. (chua2024stomataldevelopmentin pages 1-2, marcos2017amutationin pages 1-5)

2. **Sequence specificity and direct promoter binding:** A Plant Physiology study analyzing SPCH genomic binding reports that SPCH binds proximal promoters genome-wide and that binding sites are enriched for an **E-box motif variant “CDCGTG”** (degenerate code: D=A/G/T), consistent with canonical bHLH preferences. (marcos2017amutationin pages 27-30)

3. **Transcriptional activation with partner bHLHs:** SPCH’s transcriptional activity is commonly modeled as requiring heterodimerization with SCRM/ICE1 family partners (SCRM/ICE1 and SCRM2), consistent with bHLH behavior and genetic requirement. (chua2024stomataldevelopmentin pages 1-2, chen2020speechlessspeaksloudly pages 1-2)

### Core biochemical activity and substrate specificity

SPCH is best curated as:

- **Sequence-specific DNA binding (E-box/G-box-like motifs)**, and
- **RNA polymerase II transcription factor activity** regulating stomatal-lineage gene expression.

**Direct experimental support:**

- **EMSA:** recombinant GST-SPCH binds the **MUTE promoter** DNA probe in a concentration-dependent manner. (cao2021arabidopsiscryptochrome1 pages 6-9)
- **Dual-luciferase reporter:** SPCH activates the **MUTE promoter**, and AGB1 can suppress this activation (functional readout of TF activity). (cao2021arabidopsiscryptochrome1 pages 6-9)

### Partners influencing activity (expert/authoritative analyses)

- **SCRM/ICE1 and SCRM2:** SPCH acts with these bHLH partners to drive stomatal lineage transitions, with genetic evidence that loss of both SCRM/ICE1 and SCRM2 eliminates stomatal formation. (chen2020speechlessspeaksloudly pages 1-2, chua2024stomataldevelopmentin pages 1-2)
- **AGB1 (G-protein β subunit):** AGB1 physically binds SPCH via the **N-terminal bHLH-containing region** and inhibits SPCH’s DNA-binding and transcriptional output in vitro/in vivo assays, providing a mechanistic route for signaling crosstalk. (cao2021arabidopsiscryptochrome1 pages 6-9)


## Biological process roles

### Strongest experimentally supported roles in *Arabidopsis*

1. **Stomatal lineage initiation / stomatal precursor cell formation:**
   - The 2024 Development review emphasizes SPCH as a master TF essential for stomatal precursor formation; loss-of-function *spch* mutants lack stomatal precursors/stomata (seedling lethal), while increased activity (e.g., MAPK-insensitive SPCH) drives extra divisions. (chua2024stomataldevelopmentin pages 1-2)

2. **Asymmetric cell division in stomatal lineage:**
   - SPCH promotes the entry and amplifying asymmetric divisions that generate meristemoids and stomatal lineage ground cells. (chua2024stomataldevelopmentin pages 1-2, fung2025multiscaledynamicsinfluence pages 1-2)

3. **Stomatal patterning/spacing via feedback to signaling:**
   - SPCH is described as controlling spacing/patterning through direct regulation of EPF2–TMM–ERECTA-family signaling components (network-level feedback restricting excessive initiation). (chen2020speechlessspeaksloudly pages 2-4)

### Environmental plasticity (recent authoritative synthesis)

The 2024 Development review frames stomatal development as climate-sensitive and highlights SPCH as a key node modulated by abiotic cues, with specific cited evidence including osmotic stress reducing SPCH protein abundance and ABA acting through EPF–SPCH-associated pathways. (chua2024stomataldevelopmentin pages 12-13)

A key mechanistic example of transcriptional control by temperature is provided by a primary study showing **PIF4 directly binds the SPCH promoter and represses SPCH at warm temperatures**, reducing stomatal production, positioning SPCH as an integration point for temperature signaling. (lau2018directcontrolof pages 1-3)

### Chromatin and transcriptional-phase logic (2023–2024 research)

A 2024 PLOS Biology study integrating scRNA-seq/ChIP-seq/MNase-seq supports a model where stomatal fate transitions involve **bHLH binding to targets that can be embedded in repressive chromatin prior to activation**, and identifies candidate chromatin machinery (SWI/SNF, HAC1) that physically associates with stomatal bHLHs; knockdown of these factors disrupts activation of bHLH targets and causes stomatal defects. (liu2024bhlhtranscriptionfactors pages 1-2, liu2024bhlhtranscriptionfactors pages 3-5)

Notably, the same study indicates that while later bHLH complexes (e.g., MUTE-SCRM, FAMA-SCRM) show evidence consistent with accessing/restructuring repressive chromatin, whether **SPCH itself** has biochemical “pioneer-factor” activity remains **unclear**, so chromatin-remodeling annotations should be conservative. (liu2024bhlhtranscriptionfactors pages 15-16)


## Cellular localization and complexes

### Best-supported subcellular localization

**Nucleus:** Multiple orthogonal assays support SPCH function and physical interactions in the nucleus.

- **PP2A-SPCH BiFC** signals localize to nuclei in tobacco epidermal cells, supporting nuclear association of SPCH with PP2A A-subunits. (bian2020proteinphosphatase2a pages 6-7, bian2020proteinphosphatase2a media 4c45dadc)
- **SPCH-AGB1 BiFC** shows nuclear fluorescence using an RFP-H2B nuclear marker. (cao2021arabidopsiscryptochrome1 pages 6-9)
- In stomatal lineage cells, SPCH transcriptional reporters (nuclear) are broadly present, while SPCH translational fusions are restricted to specific precursor states, supporting nuclear function with strong protein-level regulation. (yang2015phosphorylationofserine pages 5-8)

### Complexes

- **SPCH–SCRM/ICE1 and SPCH–SCRM2 heterodimers:** Widely supported as functional units in stomatal development; SPCH–ICE1 interaction is used as a positive control in BiFC assays. (chen2020speechlessspeaksloudly pages 1-2, bian2020proteinphosphatase2a pages 6-7)
- **SPCH–PP2A (A subunit) nuclear complex:** Supported by yeast two-hybrid, BiFC, and pull-down assays; functional data show PP2A stabilizes SPCH. (bian2020proteinphosphatase2a pages 6-7, bian2020proteinphosphatase2a pages 5-6)
- **SPCH–AGB1 nuclear interaction:** Supported by yeast two-hybrid, pull-down, split-LUC, BiFC, and co-IP; has functional consequence of inhibiting SPCH DNA binding and transcriptional activation. (cao2021arabidopsiscryptochrome1 pages 6-9)


## Annotation-risk assessment

### Core function vs context-specific roles

- **Core, high-confidence:** stomatal lineage initiation; stomatal precursor asymmetric divisions; nuclear bHLH transcription factor activity; partnership with SCRM/ICE1 family partners. (chua2024stomataldevelopmentin pages 1-2, chen2020speechlessspeaksloudly pages 1-2)

- **Well supported but network/context dependent:** stomatal spacing/patterning via signaling feedback; environmental plasticity roles where SPCH is regulated by external cues (temperature via PIF4; osmotic stress via reduced SPCH protein; ABA-linked regulation discussed in 2024 review). These should typically be curated as **regulation of stomatal development in response to stimulus**, not as direct broad stress-response master roles. (lau2018directcontrolof pages 1-3, chua2024stomataldevelopmentin pages 12-13)

- **Chromatin remodeling:** Evidence supports cooperation of stomatal bHLHs with chromatin regulators for fate transitions, but direct assignment of SPCH to “chromatin remodeling” as a molecular function may be over-extended because SPCH’s pioneer capacity is explicitly described as unclear in the 2024 PLOS Biology work. (liu2024bhlhtranscriptionfactors pages 15-16, liu2024bhlhtranscriptionfactors pages 1-2)

### Activation/maturation mechanism

- **No proteolytic maturation:** SPCH regulation is best described as **phosphorylation-state control** and **proteasome-mediated degradation**, not cleavage activation. MG132 rescues SPCH loss when PP2A is inhibited, supporting a phosphorylation→proteasome axis. (bian2020proteinphosphatase2a pages 6-7, bian2020proteinphosphatase2a media 4c45dadc)

### Explicit exclusions requested

No retrieved evidence supports any role for SPCH in apoptosis, developmental cell death, neuronal biology, inflammatory signaling, pyroptosis, synaptic remodeling, or related animal processes. Such annotations should be avoided as biologically inappropriate and unsupported. (cao2021arabidopsiscryptochrome1 pages 6-9, bian2020proteinphosphatase2a pages 7-9)


## Summary evidence table (for GO review)

| Aspect | Recommended GO annotation wording (plain English) | Key experimental evidence (assay types) | Key citations with year and URL | Notes/risks (core vs context-specific; transferability; over-annotation cautions) |
|---|---|---|---|---|
| Molecular function | Sequence-specific DNA-binding transcription factor activity at stomatal-lineage genes, recognizing E-box/G-box-like cis-elements | EMSA showing SPCH binding to the MUTE promoter; Dual-LUC showing transcriptional activation; ChIP-seq target association with enriched E-box variant (CDCGTG); Y1H/G-box bait testing (cao2021arabidopsiscryptochrome1 pages 6-9, marcos2017amutationin pages 27-30, marcos2017amutationin pages 33-36) | Cao et al., 2021, JIPB, https://doi.org/10.1111/jipb.13168; de Marcos et al., 2017, Plant Physiol, https://doi.org/10.1104/pp.17.00615 (cao2021arabidopsiscryptochrome1 pages 6-9, marcos2017amutationin pages 27-30, marcos2017amutationin pages 33-36) | Core function. Best kept at transcription factor/DNA-binding level; avoid overly specific motif claims beyond E-box/G-box-like enrichment because direct biochemical specificity remains incompletely resolved across all targets (marcos2017amutationin pages 27-30, marcos2017amutationin pages 1-5) |
| Molecular function | Transcriptional activator of stomatal-lineage regulatory genes, including direct promotion of MUTE and other lineage regulators | Dual-LUC activation of MUTE promoter by SPCH; ChIP-seq/RNA-seq integration identifying direct targets; review synthesis of direct regulation of EPF2, TMM, ERf, BASL, POLAR (cao2021arabidopsiscryptochrome1 pages 6-9, chen2020speechlessspeaksloudly pages 2-4, liu2024bhlhtranscriptionfactors pages 1-2) | Cao et al., 2021, https://doi.org/10.1111/jipb.13168; Chen et al., 2020, https://doi.org/10.3389/fpls.2020.00114; Liu et al., 2024, https://doi.org/10.1371/journal.pbio.3002770 (cao2021arabidopsiscryptochrome1 pages 6-9, chen2020speechlessspeaksloudly pages 2-4, liu2024bhlhtranscriptionfactors pages 1-2) | Core, but target-by-target annotations should be restricted to experimentally supported direct targets in Arabidopsis. Do not generalize all downstream transcriptome changes as direct SPCH action. |
| Biological process | Required for stomatal lineage initiation and specification of meristemoid mother cell/meristemoid identity | Loss-of-function spch mutants lack stomatal precursors/stomata; overexpression causes ectopic entry divisions; single-cell and genetic studies place SPCH at lineage entry (chua2024stomataldevelopmentin pages 1-2, liu2024bhlhtranscriptionfactors pages 15-16) | Chua & Lau, 2024, Development, https://doi.org/10.1242/dev.202681; Liu et al., 2024, https://doi.org/10.1371/journal.pbio.3002770 (chua2024stomataldevelopmentin pages 1-2, liu2024bhlhtranscriptionfactors pages 15-16) | Strongest core BP annotation. Appropriate for direct GO assignment in Arabidopsis. |
| Biological process | Promotes asymmetric cell division in the stomatal lineage | Genetic phenotypes of null and overexpression lines; SPCH maintenance in meristemoids and degradation in SLGCs correlates with division potential; regulation of polarity/division genes BASL and POLAR summarized from direct-target studies (fung2025multiscaledynamicsinfluence pages 1-2, chen2020speechlessspeaksloudly pages 2-4, chen2020speechlessspeaksloudly pages 1-2) | Fung et al., 2025, Nat Commun, https://doi.org/10.1038/s41467-025-57730-9; Chen et al., 2020, https://doi.org/10.3389/fpls.2020.00114 (fung2025multiscaledynamicsinfluence pages 1-2, chen2020speechlessspeaksloudly pages 2-4, chen2020speechlessspeaksloudly pages 1-2) | Core developmental role. If annotating “asymmetric cell division,” keep within stomatal lineage context; avoid broad organism-wide asymmetric division annotations. |
| Biological process | Contributes to stomatal patterning/spacing through EPF2–TMM–ERf feedback-linked transcriptional control | Direct target/review synthesis linking SPCH to EPF2, TMM, ERf and negative feedback restricting initiation; mutant/overexpression patterning phenotypes (chen2020speechlessspeaksloudly pages 2-4) | Chen et al., 2020, https://doi.org/10.3389/fpls.2020.00114 (chen2020speechlessspeaksloudly pages 2-4) | Well supported but somewhat one step more network-level than lineage entry. Suitable if curated carefully as stomatal spacing/patterning, not generic epidermal patterning. |
| Biological process | Integrates environmental and hormonal signals to modulate stomatal development, including temperature, osmotic stress, and ABA-linked pathways | Warm temperature: PIF4 directly represses SPCH promoter; osmotic stress lowers SPCH protein abundance; 2024 review summarizes ABA action through EPF–SPCH pathway (lau2018directcontrolof pages 1-3, chua2024stomataldevelopmentin pages 12-13) | Lau et al., 2018, Curr Biol, https://doi.org/10.1016/j.cub.2018.02.054; Chua & Lau, 2024, https://doi.org/10.1242/dev.202681 (lau2018directcontrolof pages 1-3, chua2024stomataldevelopmentin pages 12-13) | Context-specific/modulatory, not core biochemical function. Safer to annotate as regulation of stomatal development in response to environmental stimulus rather than direct drought/ABA master role unless primary evidence is specific. |
| Biological process | Cooperates with chromatin-remodeling machinery during stomatal cell-fate transitions | ChIP-seq/scRNA-seq/MNase-seq integration; proximity labeling identifying SWI/SNF and HAC1 interactors; stage-specific knockdown of remodelers causing failure to activate bHLH targets and stomatal defects (liu2024bhlhtranscriptionfactors pages 1-2, liu2024bhlhtranscriptionfactors pages 3-5) | Liu et al., 2024, PLOS Biol, https://doi.org/10.1371/journal.pbio.3002770; Kim et al., 2022, Nat Plants, https://doi.org/10.1038/s41477-022-01304-w (liu2024bhlhtranscriptionfactors pages 1-2, liu2024bhlhtranscriptionfactors pages 3-5, kim2022dynamicchromatinaccessibility pages 1-2) | Use caution: strong evidence for cooperation with chromatin machinery, but direct annotation of SPCH to chromatin remodeling itself may overreach. Better framed as regulation of transcription/cell fate with chromatin-remodeler cooperation. |
| Cellular component | Nucleus | BiFC nuclear signal for SPCH-AGB1 and SPCH-PP2A-A interactions; promoter-binding and transcriptional assays consistent with nuclear function; translational nuclear reporters in lineage cells (cao2021arabidopsiscryptochrome1 pages 6-9, bian2020proteinphosphatase2a pages 6-7, yang2015phosphorylationofserine pages 18-23) | Cao et al., 2021, https://doi.org/10.1111/jipb.13168; Bian et al., 2020, PNAS, https://doi.org/10.1073/pnas.1912075117; Yang et al., 2015, Mol Plant, https://doi.org/10.1016/j.molp.2014.12.014 (cao2021arabidopsiscryptochrome1 pages 6-9, bian2020proteinphosphatase2a pages 6-7, yang2015phosphorylationofserine pages 18-23) | Strong CC annotation. No good evidence here for stable cytosolic localization of active SPCH. |
| Cellular component | Active as part of nuclear bHLH transcription factor complexes with SCRM/ICE1 and SCRM2 | Genetic requirement of SCRM/ICE1 and SCRM2; positive-control BiFC for SPCH-ICE1; multiple reviews and primary studies place heterodimers at stomatal-lineage transitions (chen2020speechlessspeaksloudly pages 1-2, chua2024stomataldevelopmentin pages 1-2, marcos2017amutationin pages 1-5) | Chen et al., 2020, https://doi.org/10.3389/fpls.2020.00114; Chua & Lau, 2024, https://doi.org/10.1242/dev.202681; de Marcos et al., 2017, https://doi.org/10.1104/pp.17.00615 (chen2020speechlessspeaksloudly pages 1-2, chua2024stomataldevelopmentin pages 1-2, marcos2017amutationin pages 1-5) | Complex membership is strong, but exact stoichiometry and whether homodimerization is biologically relevant remain less certain; prioritize heterodimer annotations. |
| Regulation | SPCH activity and abundance are regulated by phosphorylation: MAPK/YDA and BIN2 generally inhibit/stabilize less, whereas CDKA;1 Ser186 phosphorylation promotes activity | In vitro kinase assays; phospho-deficient/phospho-mimic transgenes; genetic interactions with cdka;1 and BR treatments; mutant phenotypic rescue by S186D (yang2015phosphorylationofserine pages 1-5, yang2015phosphorylationofserine pages 5-8) | Yang et al., 2015, Mol Plant, https://doi.org/10.1016/j.molp.2014.12.014; de Marcos et al., 2017, https://doi.org/10.1104/pp.17.00615 (yang2015phosphorylationofserine pages 1-5, yang2015phosphorylationofserine pages 5-8, marcos2017amutationin pages 1-5) | Regulation annotation is strong, but wording should not imply one universal phosphorylation outcome; effects are site- and pathway-specific. |
| Regulation | PP2A stabilizes SPCH by dephosphorylation and opposes proteasome-dependent degradation | Cantharidin sensitivity of SPCH-CFP; MG132 rescue; Y2H, BiFC, pull-down of SPCH with PP2A A subunits; phosphodeficient SPCH less sensitive to PP2A inhibition (bian2020proteinphosphatase2a pages 5-6, bian2020proteinphosphatase2a pages 6-7, bian2020proteinphosphatase2a media 4c45dadc) | Bian et al., 2020, PNAS, https://doi.org/10.1073/pnas.1912075117 (bian2020proteinphosphatase2a pages 5-6, bian2020proteinphosphatase2a pages 6-7, bian2020proteinphosphatase2a media 4c45dadc) | Strong post-translational regulation evidence. This supports regulation of protein stability/dephosphorylation, not proteolytic processing/maturation. |
| Regulation | AGB1 negatively regulates SPCH DNA-binding and transcriptional output | Y2H, pull-down, split-LUC, BiFC, co-IP; EMSA showing reduced SPCH-DNA binding with AGB1; Dual-LUC repression of SPCH activation of MUTE promoter (cao2021arabidopsiscryptochrome1 pages 6-9) | Cao et al., 2021, JIPB, https://doi.org/10.1111/jipb.13168 (cao2021arabidopsiscryptochrome1 pages 6-9) | Best interpreted as a regulatory interaction affecting SPCH function. Avoid annotating AGB1 as an obligate SPCH complex for core activity. |
| Negative evidence/Exclusions | No support for apoptosis, programmed cell death, neuronal function, inflammatory signaling, pyroptosis, or synaptic remodeling | Literature reviewed is confined to stomatal development, transcriptional control, phosphorylation, and chromatin cooperation; no experimental mention of these processes (bian2020proteinphosphatase2a pages 7-9, chen2020speechlessspeaksloudly pages 1-2, chua2024stomataldevelopmentin pages 1-2, cao2021arabidopsiscryptochrome1 pages 6-9) | Bian et al., 2020, https://doi.org/10.1073/pnas.1912075117; Chen et al., 2020, https://doi.org/10.3389/fpls.2020.00114; Chua & Lau, 2024, https://doi.org/10.1242/dev.202681; Cao et al., 2021, https://doi.org/10.1111/jipb.13168 (bian2020proteinphosphatase2a pages 7-9, chen2020speechlessspeaksloudly pages 1-2, chua2024stomataldevelopmentin pages 1-2, cao2021arabidopsiscryptochrome1 pages 6-9) | Exclude such annotations as unsupported and biologically inappropriate for this plant transcription factor. |
| Negative evidence/Exclusions | No evidence for proteolytic maturation/processing; evidence supports phosphorylation-dependent degradation instead | MG132 rescue of CT-induced SPCH loss; discussions consistently describe degradation/stability control, not cleavage activation (bian2020proteinphosphatase2a pages 6-7, bian2019signalingeventsin pages 39-43) | Bian et al., 2020, https://doi.org/10.1073/pnas.1912075117 (bian2020proteinphosphatase2a pages 6-7, bian2019signalingeventsin pages 39-43) | Do not annotate proteolytic processing or maturation. If relevant, annotate regulation of protein stability/degradation only. |
| Negative evidence/Exclusions | Cytosolic/cytosol localization is not well supported for the active protein; nucleus is the best-supported site of action | Nuclear BiFC with PP2A and AGB1; promoter binding and transcription factor assays; no explicit evidence for stable active cytosolic pool in retrieved literature (cao2021arabidopsiscryptochrome1 pages 6-9, bian2020proteinphosphatase2a pages 6-7, bian2019signalingeventsin pages 39-43) | Cao et al., 2021, https://doi.org/10.1111/jipb.13168; Bian et al., 2020, https://doi.org/10.1073/pnas.1912075117 (cao2021arabidopsiscryptochrome1 pages 6-9, bian2020proteinphosphatase2a pages 6-7, bian2019signalingeventsin pages 39-43) | Avoid adding cytosol/cytoplasm CC terms without direct localization data. Some transient synthesis/trafficking is possible biologically, but not supported here for GO annotation. |


*Table: This table summarizes evidence-based GO annotation recommendations for Arabidopsis SPCH, distinguishing core stomatal-lineage functions from context-dependent regulatory roles and unsupported annotations. It is designed to support conservative, citation-traceable curation decisions.*


## Current applications and real-world implementations

While SPCH itself is a basic research target in *Arabidopsis*, its pathway is actively used as an **engineering handle to tune stomatal density/patterning** for climate resilience in crops. One recent example is **cis-regulatory editing of SPCH orthologs** (e.g., in tomato) to create alleles with altered stomatal development responses to environmental cues; this underscores translational interest in SPCH-centered developmental control modules, although these data are outside *Arabidopsis* GO annotation transfer without explicit orthology evidence. (nir2023targetingeditingof, not in evidence context; therefore not cited for claims beyond general translational framing)

Chemical biology also targets stomatal bHLH networks (e.g., perturbing bHLH heterodimers) to modulate development, suggesting future applications in controllable stomatal trait manipulation; however, detailed SPCH-specific chemical inhibitors were not directly evidenced in the retrieved SPCH primary sources used here. (nakagawa2024chemicalinhibitionof, not in evidence context)


## Key literature (prioritizing 2023–2024, plus foundational mechanistic studies)

1. **Chua LC, Lau OS.** *Stomatal development in the changing climate.* **Development**. **Oct 2024**. https://doi.org/10.1242/dev.202681 (chua2024stomataldevelopmentin pages 1-2)
2. **Liu A et al.** *bHLH transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during Arabidopsis stomatal development.* **PLOS Biology**. **Aug 2024**. https://doi.org/10.1371/journal.pbio.3002770 (liu2024bhlhtranscriptionfactors pages 1-2)
3. **Cao X et al.** *Arabidopsis cryptochrome 1 promotes stomatal development through repression of AGB1 inhibition of SPEECHLESS DNA-binding activity.* **J Integr Plant Biol**. **Oct 2021**. https://doi.org/10.1111/jipb.13168 (cao2021arabidopsiscryptochrome1 pages 6-9)
4. **Bian C et al.** *Protein phosphatase 2A promotes stomatal development by stabilizing SPEECHLESS in Arabidopsis.* **PNAS**. **May 2020**. https://doi.org/10.1073/pnas.1912075117 (bian2020proteinphosphatase2a pages 6-7)
5. **Yang K-Z et al.** *Phosphorylation of Serine 186 of bHLH Transcription Factor SPEECHLESS Promotes Stomatal Development in Arabidopsis.* **Molecular Plant**. **May 2015**. https://doi.org/10.1016/j.molp.2014.12.014 (yang2015phosphorylationofserine pages 1-5)
6. **de Marcos A et al.** *A mutation in the bHLH domain of the SPCH transcription factor uncovers a BR-dependent mechanism for stomatal development.* **Plant Physiology**. **May 2017**. https://doi.org/10.1104/pp.17.00615 (marcos2017amutationin pages 27-30)
7. **Lau OS et al.** *Direct Control of SPEECHLESS by PIF4 in the High-Temperature Response of Stomatal Development.* **Current Biology**. **Apr 2018**. https://doi.org/10.1016/j.cub.2018.02.054 (lau2018directcontrolof pages 1-3)


### Statistics and quantitative data highlights (from primary studies)

- **PP2A inhibition reduces SPCH protein-positive cells:** In seedlings with translational **SPCHpro::SPCH-CFP**, PP2A inhibitor cantharidin caused a reduction in SPCH-CFP-positive cells after **1 h (13.8% CT vs 19.7% DMSO)** and a stronger reduction after **4 h (5.2% CT vs 19.7% DMSO)**, while transcriptional reporter expression remained stable—consistent with post-translational control. (bian2020proteinphosphatase2a pages 5-6)
- **Proteasome dependence:** MG132 co-treatment “almost fully” restored SPCH-CFP under PP2A inhibition, supporting proteasome-mediated degradation when SPCH is hyperphosphorylated. (bian2020proteinphosphatase2a pages 6-7, bian2020proteinphosphatase2a media 4c45dadc)



References

1. (chua2024stomataldevelopmentin pages 1-2): Li Cong Chua and On Sun Lau. Stomatal development in the changing climate. Development (Cambridge, England), Oct 2024. URL: https://doi.org/10.1242/dev.202681, doi:10.1242/dev.202681. This article has 38 citations.

2. (cao2021arabidopsiscryptochrome1 pages 6-9): Xiaoli Cao, Pengbo Xu, Yao Liu, Guangqiong Yang, Minqing Liu, Li Chen, Yingyu Cheng, Pengbo Xu, Langxi Miao, Zhilei Mao, Wenxiu Wang, Shuang Kou, Tongtong Guo, and Hongquan Yang. <i>arabidopsis</i> cryptochrome 1 promotes stomatal development through repression of agb1 inhibition of speechless dna‐binding activity. Oct 2021. URL: https://doi.org/10.1111/jipb.13168, doi:10.1111/jipb.13168. This article has 21 citations and is from a peer-reviewed journal.

3. (marcos2017amutationin pages 27-30): Alberto de Marcos, Anaxi Houbaert, Magdalena Triviño, Dolores Delgado, Mar Martín-Trillo, Eugenia Russinova, Carmen Fenoll, and Montaña Mena. A mutation in the bhlh domain of the spch transcription factor uncovers a br-dependent mechanism for stomatal development. Plant Physiology, 174:823-842, May 2017. URL: https://doi.org/10.1104/pp.17.00615, doi:10.1104/pp.17.00615. This article has 43 citations and is from a highest quality peer-reviewed journal.

4. (liu2024bhlhtranscriptionfactors pages 3-5): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Bhlh transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during arabidopsis stomatal development. PLOS Biology, 22:e3002770, Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002770, doi:10.1371/journal.pbio.3002770. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (bian2020proteinphosphatase2a pages 6-7): Chao Bian, Xiaoyu Guo, Yi Zhang, Lu Wang, Tongda Xu, Alison DeLong, and Juan Dong. Protein phosphatase 2a promotes stomatal development by stabilizing speechless in arabidopsis. Proceedings of the National Academy of Sciences, 117:13127-13137, May 2020. URL: https://doi.org/10.1073/pnas.1912075117, doi:10.1073/pnas.1912075117. This article has 49 citations and is from a highest quality peer-reviewed journal.

6. (yang2015phosphorylationofserine pages 1-5): Ke-Zhen Yang, Min Jiang, Ming Wang, Shan Xue, Ling-Ling Zhu, Hong-Zhe Wang, Jun-Jie Zou, Eun-Kyoung Lee, Fred Sack, and Jie Le. Phosphorylation of serine 186 of bhlh transcription factor speechless promotes stomatal development in arabidopsis. Molecular plant, 8 5:783-95, May 2015. URL: https://doi.org/10.1016/j.molp.2014.12.014, doi:10.1016/j.molp.2014.12.014. This article has 66 citations and is from a highest quality peer-reviewed journal.

7. (bian2020proteinphosphatase2a pages 5-6): Chao Bian, Xiaoyu Guo, Yi Zhang, Lu Wang, Tongda Xu, Alison DeLong, and Juan Dong. Protein phosphatase 2a promotes stomatal development by stabilizing speechless in arabidopsis. Proceedings of the National Academy of Sciences, 117:13127-13137, May 2020. URL: https://doi.org/10.1073/pnas.1912075117, doi:10.1073/pnas.1912075117. This article has 49 citations and is from a highest quality peer-reviewed journal.

8. (liu2024bhlhtranscriptionfactors pages 1-2): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Bhlh transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during arabidopsis stomatal development. PLOS Biology, 22:e3002770, Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002770, doi:10.1371/journal.pbio.3002770. This article has 20 citations and is from a highest quality peer-reviewed journal.

9. (liu2024bhlhtranscriptionfactors pages 15-16): Ao Liu, Andrea Mair, Juliana L. Matos, Macy Vollbrecht, Shou-Ling Xu, and Dominique C. Bergmann. Bhlh transcription factors cooperate with chromatin remodelers to regulate cell fate decisions during arabidopsis stomatal development. PLOS Biology, 22:e3002770, Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002770, doi:10.1371/journal.pbio.3002770. This article has 20 citations and is from a highest quality peer-reviewed journal.

10. (bian2020proteinphosphatase2a pages 7-9): Chao Bian, Xiaoyu Guo, Yi Zhang, Lu Wang, Tongda Xu, Alison DeLong, and Juan Dong. Protein phosphatase 2a promotes stomatal development by stabilizing speechless in arabidopsis. Proceedings of the National Academy of Sciences, 117:13127-13137, May 2020. URL: https://doi.org/10.1073/pnas.1912075117, doi:10.1073/pnas.1912075117. This article has 49 citations and is from a highest quality peer-reviewed journal.

11. (marcos2017amutationin pages 1-5): Alberto de Marcos, Anaxi Houbaert, Magdalena Triviño, Dolores Delgado, Mar Martín-Trillo, Eugenia Russinova, Carmen Fenoll, and Montaña Mena. A mutation in the bhlh domain of the spch transcription factor uncovers a br-dependent mechanism for stomatal development. Plant Physiology, 174:823-842, May 2017. URL: https://doi.org/10.1104/pp.17.00615, doi:10.1104/pp.17.00615. This article has 43 citations and is from a highest quality peer-reviewed journal.

12. (chen2020speechlessspeaksloudly pages 1-2): Liang Chen, Zhongliang Wu, and Suiwen Hou. Speechless speaks loudly in stomatal development. Frontiers in Plant Science, Feb 2020. URL: https://doi.org/10.3389/fpls.2020.00114, doi:10.3389/fpls.2020.00114. This article has 52 citations.

13. (fung2025multiscaledynamicsinfluence pages 1-2): Hannah F. Fung, Gabriel O. Amador, Renee Dale, Yan Gong, Macy Vollbrecht, Joel M. Erberich, Andrea Mair, and Dominique C. Bergmann. Multi-scale dynamics influence the division potential of stomatal lineage ground cells in arabidopsis. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-57730-9, doi:10.1038/s41467-025-57730-9. This article has 7 citations and is from a highest quality peer-reviewed journal.

14. (chen2020speechlessspeaksloudly pages 2-4): Liang Chen, Zhongliang Wu, and Suiwen Hou. Speechless speaks loudly in stomatal development. Frontiers in Plant Science, Feb 2020. URL: https://doi.org/10.3389/fpls.2020.00114, doi:10.3389/fpls.2020.00114. This article has 52 citations.

15. (chua2024stomataldevelopmentin pages 12-13): Li Cong Chua and On Sun Lau. Stomatal development in the changing climate. Development (Cambridge, England), Oct 2024. URL: https://doi.org/10.1242/dev.202681, doi:10.1242/dev.202681. This article has 38 citations.

16. (lau2018directcontrolof pages 1-3): On Sun Lau, Zhuojun Song, Zimin Zhou, Kelli A. Davies, Jessica Chang, Xin Yang, Shenqi Wang, Doris Lucyshyn, Irene Hui Zhuang Tay, Philip A. Wigge, and Dominique C. Bergmann. Direct control of speechless by pif4 in the high-temperature response of stomatal development. Current Biology, 28:1273-1280.e3, Apr 2018. URL: https://doi.org/10.1016/j.cub.2018.02.054, doi:10.1016/j.cub.2018.02.054. This article has 190 citations and is from a highest quality peer-reviewed journal.

17. (bian2020proteinphosphatase2a media 4c45dadc): Chao Bian, Xiaoyu Guo, Yi Zhang, Lu Wang, Tongda Xu, Alison DeLong, and Juan Dong. Protein phosphatase 2a promotes stomatal development by stabilizing speechless in arabidopsis. Proceedings of the National Academy of Sciences, 117:13127-13137, May 2020. URL: https://doi.org/10.1073/pnas.1912075117, doi:10.1073/pnas.1912075117. This article has 49 citations and is from a highest quality peer-reviewed journal.

18. (yang2015phosphorylationofserine pages 5-8): Ke-Zhen Yang, Min Jiang, Ming Wang, Shan Xue, Ling-Ling Zhu, Hong-Zhe Wang, Jun-Jie Zou, Eun-Kyoung Lee, Fred Sack, and Jie Le. Phosphorylation of serine 186 of bhlh transcription factor speechless promotes stomatal development in arabidopsis. Molecular plant, 8 5:783-95, May 2015. URL: https://doi.org/10.1016/j.molp.2014.12.014, doi:10.1016/j.molp.2014.12.014. This article has 66 citations and is from a highest quality peer-reviewed journal.

19. (marcos2017amutationin pages 33-36): Alberto de Marcos, Anaxi Houbaert, Magdalena Triviño, Dolores Delgado, Mar Martín-Trillo, Eugenia Russinova, Carmen Fenoll, and Montaña Mena. A mutation in the bhlh domain of the spch transcription factor uncovers a br-dependent mechanism for stomatal development. Plant Physiology, 174:823-842, May 2017. URL: https://doi.org/10.1104/pp.17.00615, doi:10.1104/pp.17.00615. This article has 43 citations and is from a highest quality peer-reviewed journal.

20. (kim2022dynamicchromatinaccessibility pages 1-2): Eun-Deok Kim, Michael W. Dorrity, Bridget A. Fitzgerald, Hyemin Seo, Krishna Mohan Sepuru, Christine Queitsch, Nobutaka Mitsuda, Soon-Ki Han, and Keiko U. Torii. Dynamic chromatin accessibility deploys heterotypic cis/trans-acting factors driving stomatal cell-fate commitment. Nature Plants, 8:1453-1466, Dec 2022. URL: https://doi.org/10.1038/s41477-022-01304-w, doi:10.1038/s41477-022-01304-w. This article has 33 citations and is from a highest quality peer-reviewed journal.

21. (yang2015phosphorylationofserine pages 18-23): Ke-Zhen Yang, Min Jiang, Ming Wang, Shan Xue, Ling-Ling Zhu, Hong-Zhe Wang, Jun-Jie Zou, Eun-Kyoung Lee, Fred Sack, and Jie Le. Phosphorylation of serine 186 of bhlh transcription factor speechless promotes stomatal development in arabidopsis. Molecular plant, 8 5:783-95, May 2015. URL: https://doi.org/10.1016/j.molp.2014.12.014, doi:10.1016/j.molp.2014.12.014. This article has 66 citations and is from a highest quality peer-reviewed journal.

22. (bian2019signalingeventsin pages 39-43): Chao Bian. Signaling events in arabidopsis stomatal development and patterning. ArXiv, Jan 2019. URL: https://doi.org/10.7282/t3-m1ft-r605, doi:10.7282/t3-m1ft-r605. This article has 0 citations.