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

- Gene symbol: BIK1
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: O48814
Entry Name: BIK1_ARATH
Gene Name: BIK1
Locus Tag: At2g39660 {ECO:0000312|Araport:AT2G39660}
Protein Name: Serine/threonine-protein kinase BIK1
EC Number: 2.7.11.1
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: (Microbial infection) Xanthomonas campestris effector AvrAC/XopAC-mediated uridylylation prevents activation by phosphorylation at the same residues, thus affecting immune responses and reducing defense responses toward X.campestris, mediating avrAC/XopAC virulence functions.
Subcellular Location: Cell membrane
Subunit: Interacts with FLS2 (PubMed:20404519, PubMed:20413097). Activation of FLS2 by flagellin (flg22) induces the dissociation of the complex (PubMed:20413097, PubMed:32404997). Interacts with BAK1 (PubMed:20404519). Interacts with the Xanthomonas campestris effector XopAC/AvrAC (PubMed:22504181). Interacts with CPK28 (PubMed:25525792). Interacts with PEPR1 (PubMed:23431184). Interacts with PP2C38 (PubMed:27494702). Interacts with BRI1 (PubMed:23818580). Interacts with RBOHD (PubMed:24629339). Binds to EFR when not phosphorylated at Ser-89 and Thr-90, in the absence of pathogen elicitor; dissociates upon pathogen-associated molecular pattern (PAMP)-triggered activation by EFR-mediated phosphorylation (PubMed:29649442). Interacts directly with and phosphorylates WRKY transcription factors in the nucleus involved in the jasmonic acid (JA) and salicylic acid (SA) regulation (e.g. WRKY33, WRKY50, WRKY51 and WRKY57) to modulate defense hormones during plant immunity (PubMed:29649442). Binds to ATL44/RHA3A and ATL45/RHA3B (PubMed:32404997). Binds to SIK1 to be phosphorylated and stabilized (PubMed:30212650).
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


## Gene Research Report for GO Annotation Review: **BIK1** (Arabidopsis thaliana; UniProt O48814; At2g39660)

### 1. Executive summary
BOTRYTIS-INDUCED KINASE 1 (BIK1) encodes a plasma-membrane-associated receptor-like cytoplasmic kinase (RLCK) that acts immediately downstream of multiple pattern-recognition receptors (PRRs) in Arabidopsis innate immunity, where it functions as a signaling hub connecting PRR activation to early defense outputs such as reactive oxygen species (ROS) production, Ca2+ signaling, and stomatal immunity. Core evidence from high-citation primary studies shows that BIK1 is an active serine/threonine kinase that **directly phosphorylates the NADPH oxidase RBOHD** at defined N-terminal residues (including S39 and S343), enabling the PAMP-triggered oxidative burst. (li2014thefls2associatedkinase pages 1-2, yasuhiro2014directregulationof pages 9-9)

Recent work (2023–2024) shifts part of the “current understanding” from a purely biochemical linear pathway to a spatiotemporally regulated module: (i) BIK1 **activation and stability are governed by multiple post-translational modifications** (PTMs), including PP2C38-dependent dephosphorylation, **S-nitrosylation at Cys80**, and a network of E3 ligases that ubiquitinate distinct BIK1 phospho-forms; and (ii) **BIK1 positioning in plasma membrane nanodomains** is actively organized by myosin XI (XIK), which promotes FLS2–BIK1 complex formation and robust signaling. (daniel2016thearabidopsisprotein pages 1-5, cui2024snitrosylationofa pages 5-6, bai2023bik1proteinhomeostasis pages 1-2, wang2024myosinximediatedbik1 pages 1-2)

For GO curation, the strongest “core” annotations are to **protein serine/threonine kinase activity**, **PRR-triggered immunity / defense response**, **positive regulation of ROS production**, and **plasma membrane-associated immune receptor complexes**. In contrast, claims about broad developmental roles, generalized “cell death” regulation, or animal-specific pathways (apoptosis, pyroptosis, neuronal/synaptic functions, inflammatory signaling) are not supported by the core mechanistic evidence base presented here and should be treated as out of scope or as indirect/pleiotropic unless backed by targeted Arabidopsis experiments. (yasuhiro2014directregulationof pages 1-2, daniel2016thearabidopsisprotein pages 1-5)

### 2. Molecular function
#### 2.1 Key concepts/definitions (current understanding)
**Receptor-like cytoplasmic kinases (RLCKs)** are non-transmembrane kinases that couple cell-surface receptors (PRRs) to intracellular signaling. In this framework, **BIK1 functions as a PRR-associated kinase**, rapidly phosphorylated upon ligand perception and then released from PRR complexes to phosphorylate downstream effectors. (yasuhiro2014directregulationof pages 1-2, daniel2016thearabidopsisprotein pages 1-5)

#### 2.2 Core biochemical activity and substrate specificity
**Kinase type:** Experimental data support BIK1 as an **active serine/threonine protein kinase**. (yasuhiro2014directregulationof pages 1-2, li2014thefls2associatedkinase pages 1-2)

**Direct substrate:** Two landmark 2014 studies provide direct evidence that BIK1 phosphorylates the NADPH oxidase **RBOHD**:
- BIK1 directly phosphorylates RBOHD (calcium independent) at key residues including **S39 and S343**, enhancing ROS production. (li2014thefls2associatedkinase pages 1-2)
- Complementary phosphoproteomic/targeted MS evidence identifies multiple BIK1-dependent sites on RBOHD including **S39, S339, S343** (and additional sites such as T123, S140, S347 in vitro), and links these sites to PAMP-induced phosphorylation within minutes after elicitation. (yasuhiro2014directregulationof pages 9-9, yasuhiro2014directregulationof pages 6-7)

**Quantitative/statistical notes:** In the Molecular Cell study, phosphorylation-site identification and dynamics were supported by targeted mass spectrometry (SRM) and functional testing of phospho-dead/mimic mutants, and ROS burst assays were quantified over tens of minutes with replicated leaf-disc measurements and strong statistical thresholds (e.g., ANOVA/Tukey, p < 0.001). (yasuhiro2014directregulationof pages 9-9)

#### 2.3 Activation and inactivation mechanisms (maturation/processing)
**PRR-complex phosphorylation and release:** BIK1 is described as constitutively associated with PRRs (e.g., FLS2 and EFR) and becomes rapidly phosphorylated and released upon PAMP perception. (yasuhiro2014directregulationof pages 1-2)

**Negative regulation by phosphatase PP2C38:** PP2C38 is identified as a negative regulator that dynamically associates with BIK1 and PRRs (FLS2/EFR) and impairs PAMP-induced BIK1 phosphorylation and BIK1-mediated RBOHD phosphorylation; upon PAMP perception PP2C38 is phosphorylated and dissociates, enabling full BIK1 activation. (daniel2016thearabidopsisprotein pages 1-5)

**Redox activation via S-nitrosylation (2024):** A 2024 Science Advances study reports that P/MAMP perception triggers a nitrosative burst leading to **S-nitrosylation of BIK1 at Cys80**, which promotes BIK1 phosphorylation/activation and stabilization and increases physical interaction with RBOHD, boosting ROS formation. The study uses targeted mutagenesis (e.g., **BIK1C80A**) and shows reduced ROS kinetics (measured over 60 minutes following flg22 treatment) and compromised resistance to a nonpathogenic bacterial strain in complementation assays. (cui2024snitrosylationofa pages 5-6)

**Ubiquitin-mediated control of BIK1 pools (2023–2024):** Recent evidence and synthesis describe a multi-E3 network that differentially ubiquitinates BIK1 depending on its phosphorylation state:
- PUB25/26: preferentially ubiquitinate **hypo-phosphorylated** BIK1 for degradation, acting as negative regulators of immune signaling. (bai2023bik1proteinhomeostasis pages 1-2, fu2024themultifacetedubiquitination pages 6-7)
- RGLG1/2 (Nature Communications 2023): preferentially associate with hypo-phosphorylated BIK1, promote BIK1 accumulation and BAK1–BIK1 association, and antagonize PUB25-mediated degradation; a reported phospho-mimic (**BIK1S236D/T237D**) shows resistance to PUB25 ubiquitination. (bai2023bik1proteinhomeostasis pages 1-2, bai2023bik1proteinhomeostasis pages 8-9)
- RHA3A/B: mediate PAMP-induced **monoubiquitination** of activated/hyperphosphorylated BIK1 (observed as an ~8 kDa shift consistent with monoubiquitination), promoting release from FLS2–BAK1 and internalization to endocytic vesicles to enable signaling. (fu2024themultifacetedubiquitination pages 6-7)
- PUB4: described as having dual roles, promoting degradation of non-activated BIK1 at rest while supporting accumulation/associations of activated BIK1 after PAMP perception. (bai2023bik1proteinhomeostasis pages 1-2, fu2024themultifacetedubiquitination pages 6-7)

**Site-level ubiquitination (from 2024 synthesis):** BIK1 has many lysines, and mutational/MS analyses implicate multiple ubiquitination sites (e.g., K31, K41, K95, K170, K186, K286, K337, K358, K366 among others), with multi-lysine mutants (e.g., “9KR”) substantially reducing monoubiquitination and dissociation from PRR complexes. (fu2024themultifacetedubiquitination pages 6-7, fu2024themultifacetedubiquitination pages 7-9)

**Proteolytic targeting by pathogen effectors:** In the immune context, bacterial type-III effectors can proteolytically cleave RLCKs; a recent synthesis notes AvrPphB cleavage of BIK1 in plant–pathogen interactions. This is not a normal maturation step for the host protein but a pathogen virulence strategy. (fu2024themultifacetedubiquitination pages 2-4, daniel2016thearabidopsisprotein pages 1-5)

### 3. Biological process roles
#### 3.1 Best-supported processes in Arabidopsis (direct evidence)
**Pattern-triggered immunity (PTI) / innate immune signaling:** BIK1 is repeatedly described as a PRR-associated kinase acting downstream of multiple PRRs (FLS2, EFR; also CERK1, PEPR1), linking PAMP perception to downstream defense signaling. (daniel2016thearabidopsisprotein pages 1-5, yasuhiro2014directregulationof pages 1-2)

**Positive regulation of the ROS burst:** Direct phosphorylation of RBOHD by BIK1 and requirement of BIK1-dependent RBOHD phosphosites for PAMP-triggered ROS bursts are central functional outputs, supported by both biochemical and genetic evidence (RBOHD phosphosite mutants, bik1-related mutants). (yasuhiro2014directregulationof pages 9-9, li2014thefls2associatedkinase pages 1-2)

**Stomatal immunity:** BIK1-dependent signaling through RBOHD is linked to stomatal movement that restricts bacterial entry, with impairment when BIK1 function (or its RBOHD phosphorylation) is compromised. (li2014thefls2associatedkinase pages 1-2, daniel2016thearabidopsisprotein pages 1-5)

**Early Ca2+ signaling:** BIK1 (with PBL1) is required for MAMP/DAMP-induced calcium elevations, positioning BIK1 in early signaling outputs beyond ROS. (li2014thefls2associatedkinase pages 1-2)

#### 3.2 Recent developments (2023–2024) refining process interpretation
**Immune homeostasis as a regulated “BIK1 pool” problem:** 2023–2024 work emphasizes that BIK1 is not simply “on/off,” but rather immune amplitude is tuned by the relative abundance of hypophosphorylated vs activated BIK1 and by distinct ubiquitin ligase modules (RGLG1/2 vs PUB25/26 vs RHA3A/B vs PUB4). This reframes some GO biological-process interpretation toward “regulation of protein stability/turnover in immune signaling” rather than only “defense response.” (bai2023bik1proteinhomeostasis pages 1-2, fu2024themultifacetedubiquitination pages 6-7)

**Redox–ROS coupling:** The 2024 S-nitrosylation mechanism provides a mechanistic bridge between a rapid nitrosative burst and the canonical ROS burst by directly modulating BIK1 activation and BIK1–RBOHD interaction, which is relevant to annotating regulation of ROS biosynthetic process and redox signaling. (cui2024snitrosylationofa pages 5-6)

**Spatial organization of signaling (nanodomain recruitment):** The 2024 PNAS study adds a cellular-systems layer: myosin XIK recruits/stabilizes BIK1 in FLS2-containing nanodomains, facilitating receptor complex assembly and full activation of BIK1-dependent responses. This supports cellular-component/biological-process annotations related to plasma membrane microdomains and regulation of receptor complex assembly. (wang2024myosinximediatedbik1 pages 1-2, wang2024myosinximediatedbik1 media 42cf9646)

#### 3.3 Current applications and real-world implementations
BIK1 is widely treated as a **central node for engineering or breeding disease resistance** because it integrates multiple PRR pathways and controls early defense outputs (ROS, Ca2+, stomatal closure). In practical terms, “applications” often focus on manipulating upstream PRRs/co-receptors, E3 ligases controlling BIK1 abundance, or signaling amplitude to enhance resistance while avoiding autoimmunity; recent work on ubiquitin homeostasis modules provides candidate intervention points (e.g., adjusting PUB25/26 or RGLG1/2 balance) to tune defense strength. (bai2023bik1proteinhomeostasis pages 1-2, fu2024themultifacetedubiquitination pages 4-6)

### 4. Cellular localization and complexes
#### 4.1 Best-supported subcellular localization
**Plasma membrane association:** BIK1 is consistently described as plasma-membrane-associated and PRR-complex associated. (yasuhiro2014directregulationof pages 1-2, daniel2016thearabidopsisprotein pages 1-5)

**Nanodomain localization (2024):** Imaging evidence supports enrichment of BIK1 in FLS2-containing plasma membrane nanodomains, promoted by myosin XIK. (wang2024myosinximediatedbik1 media 42cf9646, wang2024myosinximediatedbik1 pages 1-2)

**Endocytic trafficking:** RHA3A/B-dependent monoubiquitination is described as promoting internalization of BIK1 from the plasma membrane to endocytic vesicles for signaling activation (distinguished from FLS2 internalization for attenuation). (fu2024themultifacetedubiquitination pages 6-7)

**Nuclear localization (contextual):** A 2024 synthesis notes that BIK1 can localize to the nucleus and phosphorylate WRKY transcription factors, but also states uncertainty about how BIK1 translocates from plasma membrane to nucleus. This suggests nuclear localization should be curated cautiously unless supported by direct primary evidence in Arabidopsis tissues/conditions. (fu2024themultifacetedubiquitination pages 2-4)

#### 4.2 Complexes and direct interactors
**PRR-associated complexes:** BIK1 is described as constitutively associating with FLS2 and EFR (and with BAK1 in those receptor complexes), and also associating with CERK1 (chitin signaling) and PEPR1 pathways. (yasuhiro2014directregulationof pages 1-2, daniel2016thearabidopsisprotein pages 1-5)

**RBOHD complex:** BIK1 directly interacts with and phosphorylates RBOHD following PAMP perception. (yasuhiro2014directregulationof pages 1-2, li2014thefls2associatedkinase pages 1-2)

**Myosin XI (XIK)–organized complexes (2024):** XIK–BIK1 interaction and XIK-dependent confinement in nanodomains is proposed to stabilize immune receptor complex assembly. This provides a mechanistic basis for annotating BIK1 in a spatially organized plasma membrane signaling complex. (wang2024myosinximediatedbik1 pages 1-2, wang2024myosinximediatedbik1 media 97a839e6)

**Supporting figure evidence:** The PNAS 2024 figure panels show BIK1 colocalization with FLS2 at the plasma membrane and BIK1 recruitment to REM1.3-marked nanodomains, both reduced by myosin inhibition, plus a model summarizing myosin XI roles in BIK1 delivery and nanodomain immobilization. (wang2024myosinximediatedbik1 media 42cf9646, wang2024myosinximediatedbik1 media 7765405b, wang2024myosinximediatedbik1 media 97a839e6)

### 5. Annotation-risk assessment (core vs context-specific; over-extension risks)
#### 5.1 High-confidence “core function” annotations (recommended emphasis)
- **Protein serine/threonine kinase activity** (BIK1 is an active RLCK). (yasuhiro2014directregulationof pages 1-2, li2014thefls2associatedkinase pages 1-2)
- **Direct phosphorylation of RBOHD** (defined sites including S39/S343; strong mechanistic linkage to ROS). (li2014thefls2associatedkinase pages 1-2, yasuhiro2014directregulationof pages 9-9)
- **Positive regulation of PAMP-triggered ROS burst / PTI** and associated immune outputs such as stomatal immunity and early Ca2+ signaling. (li2014thefls2associatedkinase pages 1-2, daniel2016thearabidopsisprotein pages 1-5)
- **Cellular component: plasma membrane / PRR-associated complex**; plus **nanodomain association** supported by 2024 imaging. (yasuhiro2014directregulationof pages 1-2, wang2024myosinximediatedbik1 media 42cf9646)

#### 5.2 Context-specific regulatory annotations (valid but should be framed as regulation of BIK1 in immunity)
- **Negative regulation via phosphatase PP2C38** (dynamic association/dissociation). (daniel2016thearabidopsisprotein pages 1-5)
- **Redox regulation via S-nitrosylation at Cys80** (PTI-specific mechanism with clear phenotypes). (cui2024snitrosylationofa pages 5-6)
- **Ubiquitination-based homeostasis** (distinct E3 ligases act on distinct BIK1 pools; immune amplitude control). (bai2023bik1proteinhomeostasis pages 1-2, fu2024themultifacetedubiquitination pages 6-7)
- **Protein localization to nanodomains and receptor complex assembly regulated by myosin XIK** (a 2024 mechanistic addition). (wang2024myosinximediatedbik1 pages 1-2, wang2024myosinximediatedbik1 media 97a839e6)

#### 5.3 Over-extension risks / terms to avoid without additional direct evidence
- **Apoptosis, pyroptosis, mammalian inflammatory signaling, neuronal/synaptic remodeling:** These are animal-centric pathways and are not discussed in the primary BIK1 mechanistic literature examined here; thus annotations implying such processes are not justified for Arabidopsis BIK1 based on this evidence set. (yasuhiro2014directregulationof pages 1-2, daniel2016thearabidopsisprotein pages 1-5)
- **Generic “programmed cell death” claims:** Not supported by the cited mechanistic evidence; any such annotation would require direct Arabidopsis experiments showing BIK1-dependent cell death phenotypes under defined triggers, distinct from PTI outputs. (yasuhiro2014directregulationof pages 1-2)
- **Proteolytic processing as maturation:** Evidence for cleavage is presented as **pathogen effector-mediated targeting**, not host maturation/processing; thus avoid annotations implying normal proteolytic activation. (fu2024themultifacetedubiquitination pages 2-4)
- **Nuclear localization as a constitutive cellular component:** A 2024 synthesis mentions nuclear activity but also notes uncertainty on the mechanism; nuclear CC annotations should be conservative and evidence-driven (prefer primary nuclear localization data). (fu2024themultifacetedubiquitination pages 2-4)

### 6. Key literature (priority to 2023–2024; includes URLs and publication dates)

#### High-priority recent primary research (2023–2024)
1. **Bai et al. (Aug 2023)**. *BIK1 protein homeostasis is maintained by the interplay of different ubiquitin ligases in immune signaling*. **Nature Communications** 14. https://doi.org/10.1038/s41467-023-40364-0 (bai2023bik1proteinhomeostasis pages 1-2, bai2023bik1proteinhomeostasis pages 8-9)
2. **Wang et al. (Jun 2024)**. *Myosin XI-mediated BIK1 recruitment to nanodomains facilitates FLS2–BIK1 complex formation during innate immunity in Arabidopsis*. **PNAS** 121(25). https://doi.org/10.1073/pnas.2312415121 (wang2024myosinximediatedbik1 pages 1-2, wang2024myosinximediatedbik1 media 42cf9646)
3. **Cui et al. (Mar 2024)**. *S-nitrosylation of a receptor-like cytoplasmic kinase regulates plant immunity*. **Science Advances** 10(11). https://doi.org/10.1126/sciadv.adk3126 (cui2024snitrosylationofa pages 5-6)
4. **Fu et al. (Nov 2024)**. *The Multifaceted Ubiquitination of BIK1 During Plant Immunity in Arabidopsis thaliana*. **International Journal of Molecular Sciences** 25(22):12187. https://doi.org/10.3390/ijms252212187 (fu2024themultifacetedubiquitination pages 6-7)

#### Foundational mechanistic literature
5. **Kadota et al. (Apr 2014)**. *Direct regulation of the NADPH oxidase RBOHD by the PRR-associated kinase BIK1 during plant immunity*. **Molecular Cell** 54(1):43–55. https://doi.org/10.1016/j.molcel.2014.02.021 (yasuhiro2014directregulationof pages 9-9, yasuhiro2014directregulationof pages 6-7)
6. **Li et al. (Mar 2014)**. *The FLS2-associated kinase BIK1 directly phosphorylates the NADPH oxidase RbohD to control plant immunity*. **Cell Host & Microbe** 15(3):329–338. https://doi.org/10.1016/j.chom.2014.02.009 (li2014thefls2associatedkinase pages 1-2)
7. **Couto et al. (Aug 2016)**. *The Arabidopsis Protein Phosphatase PP2C38 Negatively Regulates the Central Immune Kinase BIK1*. **PLoS Pathogens** 12(8):e1005811. https://doi.org/10.1371/journal.ppat.1005811 (daniel2016thearabidopsisprotein pages 1-5)

---

### GO-oriented evidence summary table
The following table consolidates candidate GO terms with the strongest supporting evidence, including residues/mutants and primary references.

| GO aspect | Candidate GO term (plain text) | Key evidence/assay (1 phrase) | Key residues/mutants (if any) | Primary reference (authors/year/journal) with URL | Citation ID |
|---|---|---|---|---|---|
| MF | protein serine/threonine kinase activity | In vitro kinase assays and phosphosite mapping support BIK1 as an active RLCK kinase | Kinase-dead BIK1K105E noted in regulatory studies; ATP-pocket K105/K106 important | Kadota et al., 2014, Molecular Cell. https://doi.org/10.1016/j.molcel.2014.02.021 ; Li et al., 2014, Cell Host & Microbe. https://doi.org/10.1016/j.chom.2014.02.009 | (yasuhiro2014directregulationof pages 1-2, li2014thefls2associatedkinase pages 1-2) |
| MF | protein kinase activity acting on RBOHD | Direct phosphorylation of RBOHD by BIK1 shown by in vitro kinase/SRM and in vivo phosphosite analysis | RBOHD S39, T123, S140, S339, S343, S347; phospho-dead/mimic RBOHD mutants tested | Kadota et al., 2014, Molecular Cell. https://doi.org/10.1016/j.molcel.2014.02.021 ; Li et al., 2014, Cell Host & Microbe. https://doi.org/10.1016/j.chom.2014.02.009 | (yasuhiro2014directregulationof pages 9-9, yasuhiro2014directregulationof pages 6-7, li2014thefls2associatedkinase pages 1-2) |
| BP | positive regulation of reactive oxygen species production | flg22/PAMP-induced ROS burst reduced in bik1 mutants and RBOHD phosphosite mutants | bik1; bik1 pbl1; RBOHD S39A/S339A/S343A and phosphomimics | Kadota et al., 2014, Molecular Cell. https://doi.org/10.1016/j.molcel.2014.02.021 ; Li et al., 2014, Cell Host & Microbe. https://doi.org/10.1016/j.chom.2014.02.009 | (yasuhiro2014directregulationof pages 9-9, li2014thefls2associatedkinase pages 1-2, yasuhiro2014directregulationof pages 6-7) |
| BP | regulation of calcium ion influx during immune signaling | aequorin-based calcium assays show BIK1/PBL1 required for MAMP-induced calcium elevations | bik1; pbl1/cce5 | Li et al., 2014, Cell Host & Microbe. https://doi.org/10.1016/j.chom.2014.02.009 ; Ranf et al., 2014, BMC Plant Biology. https://doi.org/10.1186/s12870-014-0374-4 | (li2014thefls2associatedkinase pages 1-2, fu2024themultifacetedubiquitination pages 2-4) |
| CC | plasma membrane PRR complex | Co-IP/association studies show BIK1 constitutively associates with FLS2/EFR/BAK1 and dissociates after PAMP perception | FLS2, EFR, BAK1 complexes; CERK1 also associated | Kadota et al., 2014, Molecular Cell. https://doi.org/10.1016/j.molcel.2014.02.021 ; Couto et al., 2016, PLoS Pathogens. https://doi.org/10.1371/journal.ppat.1005811 | (yasuhiro2014directregulationof pages 1-2, daniel2016thearabidopsisprotein pages 1-5) |
| BP | negative regulation of BIK1 signaling by dephosphorylation | PP2C38 association/dissociation and reduced BIK1-dependent RBOHD phosphorylation | PP2C38 Ser77 phosphorylation; pp2c38 functional tests | Couto et al., 2016, PLoS Pathogens. https://doi.org/10.1371/journal.ppat.1005811 | (daniel2016thearabidopsisprotein pages 1-5) |
| BP | activation of BIK1 by S-nitrosylation | GSNO/flg22 assays show Cys80 S-nitrosylation promotes BIK1 phosphorylation, stability, and RBOHD interaction | BIK1C80A; BIK1CA | Cui et al., 2024, Science Advances. https://doi.org/10.1126/sciadv.adk3126 | (cui2024snitrosylationofa pages 5-6) |
| BP | regulation of BIK1 protein stability by ubiquitination | Genetic/biochemical analyses define opposing E3 ligases controlling hypo- vs activated BIK1 pools | PUB25/26; RGLG1/2; RHA3A/B; PUB4; BIK1S236D/T237D resistant to PUB25; BIK19KR | Bai et al., 2023, Nature Communications. https://doi.org/10.1038/s41467-023-40364-0 ; Fu et al., 2024, International Journal of Molecular Sciences. https://doi.org/10.3390/ijms252212187 | (bai2023bik1proteinhomeostasis pages 1-2, bai2023bik1proteinhomeostasis pages 8-9, fu2024themultifacetedubiquitination pages 4-6, fu2024themultifacetedubiquitination pages 6-7, fu2024themultifacetedubiquitination pages 9-10) |
| CC | plasma membrane nanodomain | Imaging/single-particle tracking show myosin XIK recruits BIK1 into FLS2-containing nanodomains | myosin XIK; BDM inhibition; REM1.3-marked nanodomains | Wang et al., 2024, PNAS. https://doi.org/10.1073/pnas.2312415121 | (wang2024myosinximediatedbik1 pages 1-2, wang2024myosinximediatedbik1 media 42cf9646) |
| BP | protein localization to plasma membrane nanodomain facilitating immune complex assembly | Myosin-dependent recruitment stabilizes FLS2–BIK1 complex formation and supports full BIK1-dependent defense output | myosin XIK; BDM-sensitive colocalization | Wang et al., 2024, PNAS. https://doi.org/10.1073/pnas.2312415121 | (wang2024myosinximediatedbik1 pages 1-2, wang2024myosinximediatedbik1 media 42cf9646, wang2024myosinximediatedbik1 media 97a839e6) |
| BP/CC | endocytosis/internalization following monoubiquitination | RHA3A/B-mediated monoubiquitination promotes release from FLS2-BAK1 and internalization to endocytic vesicles | BIK1 9KR; ubiquitin sites including K31, K41, K95, K170, K186, K286, K337, K358, K366 | Fu et al., 2024, International Journal of Molecular Sciences. https://doi.org/10.3390/ijms252212187 | (fu2024themultifacetedubiquitination pages 6-7, fu2024themultifacetedubiquitination pages 7-9) |


*Table: This table compiles high-confidence GO-relevant statements for Arabidopsis thaliana BIK1, emphasizing experimentally supported molecular function, biological process, and cellular component assignments. It is useful for annotation review because it links each candidate term to specific assays, residues or mutants, primary literature, and citable context IDs.*


References

1. (li2014thefls2associatedkinase pages 1-2): Lei Li, Meng Li, Liping Yu, Zhaoyang Zhou, Xiangxiu Liang, Zixu Liu, Gaihong Cai, Liyan Gao, Xiaojuan Zhang, Yingchun Wang, She Chen, and Jian-Min Zhou. The fls2-associated kinase bik1 directly phosphorylates the nadph oxidase rbohd to control plant immunity. Cell host & microbe, 15 3:329-38, Mar 2014. URL: https://doi.org/10.1016/j.chom.2014.02.009, doi:10.1016/j.chom.2014.02.009. This article has 964 citations and is from a highest quality peer-reviewed journal.

2. (yasuhiro2014directregulationof pages 9-9): Yasuhiro Kadota, Jan Sklenar, Paul Derbyshire, Lena Stransfeld, Shuta Asai, Vardis Ntoukakis, Jonathan DG Jones, Ken Shirasu, Frank Menke, Alexandra Jones, and Cyril Zipfel. Direct regulation of the nadph oxidase rbohd by the prr-associated kinase bik1 during plant immunity. Molecular cell, 54 1:43-55, Apr 2014. URL: https://doi.org/10.1016/j.molcel.2014.02.021, doi:10.1016/j.molcel.2014.02.021. This article has 1161 citations and is from a highest quality peer-reviewed journal.

3. (daniel2016thearabidopsisprotein pages 1-5): Daniel Couto, Roda Niebergall, Xiangxiu Liang, Christoph A Bücherl, Jan Sklenar, Alberto P Macho, Vardis Ntoukakis, Paul Derbyshire, Denise Altenbach, Dan Maclean, Silke Robatzek, Joachim Uhrig, Frank Menke, Jian-Min Zhou, and Cyril Zipfel. The arabidopsis protein phosphatase pp2c38 negatively regulates the central immune kinase bik1. PLoS Pathogens, Aug 2016. URL: https://doi.org/10.1371/journal.ppat.1005811, doi:10.1371/journal.ppat.1005811. This article has 160 citations and is from a highest quality peer-reviewed journal.

4. (cui2024snitrosylationofa pages 5-6): Beimi Cui, Qiaona Pan, Wenqiang Cui, Yiqin Wang, Verity I. P. Loake, Shuguang Yuan, Fengquan Liu, and Gary J. Loake. S-nitrosylation of a receptor-like cytoplasmic kinase regulates plant immunity. Science Advances, Mar 2024. URL: https://doi.org/10.1126/sciadv.adk3126, doi:10.1126/sciadv.adk3126. This article has 25 citations and is from a highest quality peer-reviewed journal.

5. (bai2023bik1proteinhomeostasis pages 1-2): Jiaojiao Bai, Yuanyuan Zhou, Jianhang Sun, Kexin Chen, Yufang Han, Ranran Wang, Yanmin Zou, Mingshuo Du, and Dongping Lu. Bik1 protein homeostasis is maintained by the interplay of different ubiquitin ligases in immune signaling. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40364-0, doi:10.1038/s41467-023-40364-0. This article has 33 citations and is from a highest quality peer-reviewed journal.

6. (wang2024myosinximediatedbik1 pages 1-2): Bingxiao Wang, Zhaoyang Zhou, Jian-Min Zhou, and Jiejie Li. Myosin xi-mediated bik1 recruitment to nanodomains facilitates fls2–bik1 complex formation during innate immunity in arabidopsis. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2312415121, doi:10.1073/pnas.2312415121. This article has 14 citations and is from a highest quality peer-reviewed journal.

7. (yasuhiro2014directregulationof pages 1-2): Yasuhiro Kadota, Jan Sklenar, Paul Derbyshire, Lena Stransfeld, Shuta Asai, Vardis Ntoukakis, Jonathan DG Jones, Ken Shirasu, Frank Menke, Alexandra Jones, and Cyril Zipfel. Direct regulation of the nadph oxidase rbohd by the prr-associated kinase bik1 during plant immunity. Molecular cell, 54 1:43-55, Apr 2014. URL: https://doi.org/10.1016/j.molcel.2014.02.021, doi:10.1016/j.molcel.2014.02.021. This article has 1161 citations and is from a highest quality peer-reviewed journal.

8. (yasuhiro2014directregulationof pages 6-7): Yasuhiro Kadota, Jan Sklenar, Paul Derbyshire, Lena Stransfeld, Shuta Asai, Vardis Ntoukakis, Jonathan DG Jones, Ken Shirasu, Frank Menke, Alexandra Jones, and Cyril Zipfel. Direct regulation of the nadph oxidase rbohd by the prr-associated kinase bik1 during plant immunity. Molecular cell, 54 1:43-55, Apr 2014. URL: https://doi.org/10.1016/j.molcel.2014.02.021, doi:10.1016/j.molcel.2014.02.021. This article has 1161 citations and is from a highest quality peer-reviewed journal.

9. (fu2024themultifacetedubiquitination pages 6-7): Junhong Fu, Huihui Wang, Yuling Chen, Chunguang Zhang, and Yanmin Zou. The multifaceted ubiquitination of bik1 during plant immunity in arabidopsis thaliana. International Journal of Molecular Sciences, 25:12187, Nov 2024. URL: https://doi.org/10.3390/ijms252212187, doi:10.3390/ijms252212187. This article has 4 citations.

10. (bai2023bik1proteinhomeostasis pages 8-9): Jiaojiao Bai, Yuanyuan Zhou, Jianhang Sun, Kexin Chen, Yufang Han, Ranran Wang, Yanmin Zou, Mingshuo Du, and Dongping Lu. Bik1 protein homeostasis is maintained by the interplay of different ubiquitin ligases in immune signaling. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40364-0, doi:10.1038/s41467-023-40364-0. This article has 33 citations and is from a highest quality peer-reviewed journal.

11. (fu2024themultifacetedubiquitination pages 7-9): Junhong Fu, Huihui Wang, Yuling Chen, Chunguang Zhang, and Yanmin Zou. The multifaceted ubiquitination of bik1 during plant immunity in arabidopsis thaliana. International Journal of Molecular Sciences, 25:12187, Nov 2024. URL: https://doi.org/10.3390/ijms252212187, doi:10.3390/ijms252212187. This article has 4 citations.

12. (fu2024themultifacetedubiquitination pages 2-4): Junhong Fu, Huihui Wang, Yuling Chen, Chunguang Zhang, and Yanmin Zou. The multifaceted ubiquitination of bik1 during plant immunity in arabidopsis thaliana. International Journal of Molecular Sciences, 25:12187, Nov 2024. URL: https://doi.org/10.3390/ijms252212187, doi:10.3390/ijms252212187. This article has 4 citations.

13. (wang2024myosinximediatedbik1 media 42cf9646): Bingxiao Wang, Zhaoyang Zhou, Jian-Min Zhou, and Jiejie Li. Myosin xi-mediated bik1 recruitment to nanodomains facilitates fls2–bik1 complex formation during innate immunity in arabidopsis. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2312415121, doi:10.1073/pnas.2312415121. This article has 14 citations and is from a highest quality peer-reviewed journal.

14. (fu2024themultifacetedubiquitination pages 4-6): Junhong Fu, Huihui Wang, Yuling Chen, Chunguang Zhang, and Yanmin Zou. The multifaceted ubiquitination of bik1 during plant immunity in arabidopsis thaliana. International Journal of Molecular Sciences, 25:12187, Nov 2024. URL: https://doi.org/10.3390/ijms252212187, doi:10.3390/ijms252212187. This article has 4 citations.

15. (wang2024myosinximediatedbik1 media 97a839e6): Bingxiao Wang, Zhaoyang Zhou, Jian-Min Zhou, and Jiejie Li. Myosin xi-mediated bik1 recruitment to nanodomains facilitates fls2–bik1 complex formation during innate immunity in arabidopsis. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2312415121, doi:10.1073/pnas.2312415121. This article has 14 citations and is from a highest quality peer-reviewed journal.

16. (wang2024myosinximediatedbik1 media 7765405b): Bingxiao Wang, Zhaoyang Zhou, Jian-Min Zhou, and Jiejie Li. Myosin xi-mediated bik1 recruitment to nanodomains facilitates fls2–bik1 complex formation during innate immunity in arabidopsis. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2312415121, doi:10.1073/pnas.2312415121. This article has 14 citations and is from a highest quality peer-reviewed journal.

17. (fu2024themultifacetedubiquitination pages 9-10): Junhong Fu, Huihui Wang, Yuling Chen, Chunguang Zhang, and Yanmin Zou. The multifaceted ubiquitination of bik1 during plant immunity in arabidopsis thaliana. International Journal of Molecular Sciences, 25:12187, Nov 2024. URL: https://doi.org/10.3390/ijms252212187, doi:10.3390/ijms252212187. This article has 4 citations.