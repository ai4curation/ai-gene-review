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

- Gene symbol: ZTL
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: F4KAN2
Entry Name: F4KAN2_ARATH
Gene Name: ZTL
Locus Tag: At5g57360 {ECO:0000313|Araport:AT5G57360,
Gene Synonyms: ADAGIO 1 {ECO:0000313|EMBL:AED96892.1}, ADO1
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702 {ECO:0000313|EMBL:AED96892.1, ECO:0000313|Proteomes:UP000006548}
Subcellular Location: Nucleus
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


# Gene Research Report for GO Annotation Review: **ZEITLUPE (ZTL/ADO1)** in *Arabidopsis thaliana* (At5g57360; UniProt F4KAN2)

## 1. Executive summary

ZEITLUPE (ZTL; also known historically as ADAGIO1/ADO1) encodes a plant-specific blue-light-sensing F-box protein with a canonical **LOV–F-box–Kelch repeat** domain architecture. The best-supported core biochemical role of ZTL is as the **substrate recognition component of an SCF-type E3 ubiquitin ligase (SCF^ZTL)** that drives **26S proteasome-dependent degradation** of specific circadian clock proteins, particularly **TOC1 (PRR1)** and **PRR5**, thereby setting circadian period and oscillator robustness. Substrate recruitment is **light- and phosphorylation-dependent** (blue light stabilizes ZTL and inhibits turnover; hyperphosphorylated PRR5/TOC1 bind ZTL better), consistent with ZTL acting as a photoreceptor-coupled proteostasis regulator in the oscillator. (kiba2007targeteddegradationof pages 1-3, kiba2007targeteddegradationof pages 8-9, fujiwara2008posttranslationalregulationof pages 6-6, fujiwara2008posttranslationalregulationof pages 1-2)

Recent work extends ZTL’s influence beyond canonical clock components by implicating ZTL in proteasome-linked diel regulation of growth signaling proteins (e.g., persistent phosphorylated S6K in *ztl-3*), suggesting ZTL can couple clock/photoperiod information to TOR-dependent translational capacity. (boix202440sribosomalprotein pages 3-4, boix202440sribosomalprotein pages 8-9)

On cellular component/localization, the strongest direct evidence supports **cytosol-enriched ZTL** (and ZTL-LOV) and a key mechanistic function in **modulating nucleocytoplasmic partitioning of GIGANTEA (GI)** through LOV-dependent binding and sequestration; ZTL thereby indirectly impacts flowering-time networks that depend on GI nuclear functions. (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 5-7, kim2013thefboxprotein media fe7aa0b6)

Quantitatively, a 2024 *Science Advances* study provides strong, recent genetic evidence that ZTL is a major determinant of circadian period across temperatures, with **ztl mutants exhibiting periods ~1.7–3.6 h longer than wild type** depending on temperature regime, and explicitly links ZTL/LKP2-mediated clock protein degradation to temperature compensation. (maeda2024coldinduceddegradationof pages 7-8)

No evidence in the curated plant literature supports ZTL roles in apoptosis, pyroptosis, neuronal/synaptic biology, or inflammatory signaling (animal-specific processes); any such annotations would represent cross-kingdom over-extension. (fu2025apathogeneffector pages 6-7, kiba2007targeteddegradationof pages 1-3)

## 2. Molecular function

### 2.1 Core biochemical activity: SCF E3 ligase substrate adaptor (F-box protein)

**Definition (GO-relevant concept):** An F-box protein typically functions as a **substrate adaptor** in an **SCF (Skp1–Cullin–F-box–Rbx1) ubiquitin ligase**, recruiting specific substrates for polyubiquitination and subsequent 26S proteasome degradation.

**ZTL’s best-supported molecular function:** ZTL functions as a **blue-light-regulated F-box substrate adaptor** in an SCF E3 ligase that controls proteasome-mediated turnover of circadian proteins. (kiba2007targeteddegradationof pages 1-3, harmon2008cul1regulatestoc1 pages 1-2, suetsugu2013evolutionofthree pages 7-8)

Key experimental support includes:
- **PRR5 targeting:** PRR5 binds ZTL in vivo and in vitro in a PR-domain-dependent manner, and PRR5 half-life is shorter in dark conditions; the authors explicitly propose ZTL targets PRR5 for 26S proteasome degradation. (kiba2007targeteddegradationof pages 1-3, kiba2007targeteddegradationof pages 8-9)
- **TOC1 targeting and SCF dependence:** CUL1 function is required for TOC1 stability control, and reduced CUL1 activity phenocopies *ztl* long-period phenotypes, supporting TOC1 turnover as SCF-dependent with ZTL as F-box adaptor. (harmon2008cul1regulatestoc1 pages 1-2)
- **SCF complex membership evidence:** Experimental literature summarized in comparative analyses indicates ZTL co-immunoprecipitates with core SCF components (ASK1/CUL1/AtRBX1) and that SCF component perturbations phenocopy *ztl* circadian phenotypes. (suetsugu2013evolutionofthree pages 7-8)

### 2.2 Substrate specificity and experimentally supported interactors

**Canonical clock substrates (strongest support):**
- **PRR5**: Physical interaction (co-IP), interaction domain dependence (PR domain), and genetic dependence of *ztl* phenotypes on PRR5 support PRR5 as a direct ZTL substrate. (kiba2007targeteddegradationof pages 8-9, kiba2007targeteddegradationof pages 11-12, kiba2007targeteddegradationof pages 1-3)
- **TOC1 (PRR1)**: Established as an SCF^ZTL proteolysis target; ZTL/TOC1 interaction and SCF dependency is supported by CUL1 genetic evidence and by biochemical context in clock proteolysis studies. (harmon2008cul1regulatestoc1 pages 1-2, fujiwara2008posttranslationalregulationof pages 1-2)

**Non-substrate binding partners with strong mechanistic relevance:**
- **GIGANTEA (GI)**: ZTL binds GI via the LOV domain; ZTL or ZTL-LOV expression increases GI protein levels post-transcriptionally (~2–4×) and changes GI nucleocytoplasmic distribution. This is best interpreted as ZTL forming a functional complex with GI that impacts GI localization/stability. (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 7-8, kim2013thefboxprotein pages 5-7)

**Emerging/newer interactors:**
- **CHE (CCA1 HIKING EXPEDITION)**: A 2025 *Nature Communications* study provides multiple orthogonal assays showing ZTL binds CHE (pull-down, Y2H mapping, BiFC, MST; Kd ~90–386 nM), and shows a pathogen effector can disrupt this interaction to stabilize CHE (consistent with ZTL-mediated degradation). This strongly supports **physical interaction**; the extent to which CHE should be treated as a core ZTL substrate for GO requires careful consideration because the most direct link to ubiquitination/degradation is mechanistic inference rather than shown ubiquitination in the excerpted evidence. (fu2025apathogeneffector pages 6-7)

**Non-canonical growth/proteostasis target (2024):**
- **S6K (S6 kinase)**: In a 2024 *Plant Physiology* study, phosphorylated S6K levels showed abnormal persistence in *ztl-3* mutants, and the authors propose proteasome-dependent degradation shaping diel S6K dynamics. This is experimental genetic evidence that ZTL affects S6K phosphorylation/abundance patterns, but direct ZTL→S6K ubiquitination and binding evidence is not yet established in the excerpted text, making this a higher-risk MF extension than TOC1/PRR5. (boix202440sribosomalprotein pages 3-4, boix202440sribosomalprotein pages 8-9)

### 2.3 Activation/maturation and regulatory mechanisms

**Light regulation via LOV domain (blue light photoreception):**
- ZTL contains an N-terminal LOV domain (flavin-binding) that functions as a blue-light-regulated switch; **blue light inhibits in vivo degradation of ZTL and PRR5** and stabilizes these proteins, consistent with blue-light control of SCF^ZTL activity or substrate engagement. (fujiwara2008posttranslationalregulationof pages 1-2, fujiwara2008novelbluelight pages 1-2)

**Phosphorylation-dependent substrate recognition:**
- Hyperphosphorylated forms of PRR5 and TOC1 interact most strongly with ZTL, supporting a model where phosphorylation state modulates ZTL-mediated recruitment for proteolysis. (fujiwara2008posttranslationalregulationof pages 1-2)

**GI-dependent post-translational stabilization and complex dynamics:**
- ZTL and GI reciprocally affect each other’s stability and localization: ZTL or ZTL-LOV increases GI protein without changing GI mRNA, and ZTL’s LOV domain is required for GI binding and partitioning effects. (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 7-8)

**Chaperone-assisted maturation (annotation caution):**
- A 2024 review of GI notes HSP90 involvement in facilitating maturation of ZTL into an SCF^ZTL ligase complex, but this specific chaperone step is review-summarized in the evidence gathered here rather than directly demonstrated in the extracted primary results. (liu2024giganteaunveiledexploring pages 7-8)

## 3. Biological process roles

### 3.1 Circadian rhythm / circadian period control (core biological process)

ZTL is a central post-translational regulator of the Arabidopsis circadian oscillator, acting primarily through **protein turnover of TOC1 and PRR5**.

**Strongest recent quantitative evidence (2024):**
- In *Science Advances* (Sep 2024), **ztl mutants show a long circadian period across temperatures**, reported as **~1.7–3.6 h longer than wild type** depending on temperature conditions. The study provides explicit period measurements at low temperatures (e.g., at 15°C average period for *ztl* ≈ 27.1 h vs *lkp2* ≈ 25.7 h; at 12°C, *lkp2 ztl* ≈ 30.6 h) and integrates ZTL/LKP2-dependent turnover of TOC1/PRR5 into temperature compensation models. (maeda2024coldinduceddegradationof pages 7-8)

**Redundancy and oscillator robustness:**
- ZTL works partially redundantly with FKF1 and LKP2; higher-order mutants (e.g., *ztl fkf1* and *ztl fkf1 lkp2*) show increased stabilization of TOC1/PRR5 and more severe clock defects, supporting a shared function in turnover of evening factors and period determination. (baudry2010fboxproteinsfkf1 pages 1-2)

### 3.2 Photomorphogenesis / red-light seedling responses

ZTL impacts photomorphogenic responses through PRR5 turnover:
- PRR5 shows light-dependent half-life changes and ZTL-dependent instability; genetically, *prr5-1* partially suppresses *ztl* red-light hypersensitivity, linking the **ZTL→PRR5 degradation module** to red-light seedling phenotypes. (kiba2007targeteddegradationof pages 8-9, kiba2007targeteddegradationof pages 11-12)

This supports GO BP terms connected to **photomorphogenesis** or **seedling de-etiolation responses**, but with the mechanistic note that ZTL’s direct action is still ubiquitin-mediated proteolysis of clock/PRR proteins. (kiba2007targeteddegradationof pages 8-9)

### 3.3 Photoperiodic flowering-time regulation (indirect, network-mediated)

ZTL’s strongest support in flowering regulation is as a component of the **GI/FKF1/CO regulatory system**, largely through controlling stability/partitioning of GI and influencing CO stability indirectly.

- ZTL interacts with GI and FKF1 and is implicated in CONSTANS (CO) protein stability; a *ztl* mutant CO protein profile resembles that in *gi*, and GI stabilizes ZTL and FKF1 proteins. (song2014distinctrolesof pages 1-2)
- ZTL influences GI nuclear vs cytosolic pools; increased nuclear GI can enhance GI–FKF1 complex formation, providing a mechanistic route to flowering-time effects. (kim2013thefboxprotein pages 5-7, kim2013thefboxprotein pages 7-8)

These data support ZTL annotations in **regulation of photoperiodism/flowering time** but argue that such BP annotations should be framed as **regulatory** (not “required for flowering”) and tied to **clock/photoperiod protein stability control** rather than direct transcriptional activation. (kim2013thefboxprotein pages 5-7, song2014distinctrolesof pages 1-2)

### 3.4 Temperature compensation / temperature-related clock regulation

The 2024 *Science Advances* study positions ZTL (with LKP2) as a major contributor to maintaining circadian period across temperature variation through temperature-dependent degradation of TOC1/PRR5. (maeda2024coldinduceddegradationof pages 7-8)

This supports BP annotations such as **temperature compensation of circadian clock** or **regulation of circadian rhythm by temperature**, with strong recent quantitative genetic evidence. (maeda2024coldinduceddegradationof pages 7-8)

### 3.5 Emerging applications: clock–growth coupling via TOR/S6K

A 2024 *Plant Physiology* study connects ZTL to diel S6K regulation, proposing that ZTL affects proteasome-dependent degradation shaping S6K dynamics and thus contributing to daylength-dependent growth regulation. Experimentally, phosphorylated S6K levels are altered in *ztl-3*, consistent with ZTL-dependent proteostasis effects on a growth regulator. (boix202440sribosomalprotein pages 3-4, boix202440sribosomalprotein pages 8-9)

This line of evidence supports considering (with caution) BP annotations related to **regulation of growth in response to photoperiod** or **proteasome-mediated protein catabolism** in the context of metabolic integration; however, the direct biochemical step “ZTL ubiquitinates S6K” is not yet established in the excerpted evidence. (boix202440sribosomalprotein pages 3-4)

### 3.6 Immunity/stress intersections (annotation caution)

A 2025 *Nature Communications* paper shows a pathogen effector can disrupt ZTL–CHE binding, stabilizing CHE and perturbing development/immunity programs. This supports an intersection between clock protein turnover and immunity but does not justify animal-style inflammatory signaling annotations. (fu2025apathogeneffector pages 6-7)

## 4. Cellular localization and complexes

### 4.1 Best-supported localization

Although UniProt metadata often lists nuclear localization, the strongest direct evidence in the curated primary dataset supports **cytosol-enriched ZTL**:
- In Kim et al. 2013, GFP-tagged ZTL and ZTL-LOV show **cytosol-enriched fluorescence**, and ZTL influences the **cytosol vs nucleus distribution of GI** (increasing cytosolic GI and reducing nuclear GI). (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 5-7)

Primary image evidence for the ZTL-dependent shift in GI partitioning is present in the extracted figure regions showing fractionation and microscopy data (Figures 4–5). (kim2013thefboxprotein media fe7aa0b6, kim2013thefboxprotein media 1c2acaaa)

### 4.2 Complex membership

**SCF^ZTL complex:**
- ZTL acts as the substrate adaptor of an SCF-type complex that includes **Skp1-like ASK proteins, CUL1, and RBX1**, with functional dependence supported by CUL1 mutant phenocopy of *ztl* circadian defects. (harmon2008cul1regulatestoc1 pages 1-2, suetsugu2013evolutionofthree pages 7-8)

**GI–ZTL complex (LOV-mediated):**
- ZTL binds GI through its LOV domain; this interaction stabilizes GI post-transcriptionally and regulates GI partitioning, consistent with a functional cytosolic complex important for clock/photoperiod outputs. (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 5-7)

**ZTL-family network:**
- ZTL acts with its paralogs FKF1 and LKP2 in overlapping control of clock protein stability; genetic evidence supports partial redundancy and cooperative determination of clock robustness and period. (baudry2010fboxproteinsfkf1 pages 1-2)

## 5. Annotation-risk assessment (core vs context-specific; misannotation checks)

### 5.1 Core, high-confidence GO directions (recommended as “core function”)

1. **SCF E3 ubiquitin ligase substrate adaptor activity (F-box protein)** and related terms: strongly supported by SCF dependence and substrate-directed proteolysis data. (kiba2007targeteddegradationof pages 1-3, harmon2008cul1regulatestoc1 pages 1-2)
2. **Regulation of circadian rhythm / determination of circadian period** via TOC1/PRR5 turnover: strong genetic and mechanistic evidence including recent quantitative temperature-series data. (maeda2024coldinduceddegradationof pages 7-8, kiba2007targeteddegradationof pages 8-9)
3. **Blue light response / blue-light-regulated proteolysis** (photoreceptor-coupled turnover): supported by blue-light stabilization and LOV photoreceptor biology. (fujiwara2008posttranslationalregulationof pages 1-2, fujiwara2008novelbluelight pages 1-2)

### 5.2 Context-specific or higher-risk extensions (annotate cautiously)

1. **Direct nuclear localization**: while some clock substrates (PRRs) are nuclear-localized, ZTL itself is **cytosol-enriched** in primary imaging, and its key demonstrated localization function is to alter GI partitioning. CC annotations should avoid “exclusively nuclear”. (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 5-7)
2. **HSP90 chaperone complex membership / maturation mechanism**: present in review summaries; primary experimental support was not extracted here, so GO annotations implying direct chaperone-client maturation should be added only with direct evidence. (liu2024giganteaunveiledexploring pages 7-8)
3. **S6K as a ZTL substrate**: *ztl-3* affects S6K phosphorylation/abundance rhythms, but direct ZTL–S6K binding/ubiquitination is not established in the excerpt; annotate as an emerging regulatory connection rather than a confirmed direct substrate. (boix202440sribosomalprotein pages 3-4, boix202440sribosomalprotein pages 8-9)
4. **Immunity signaling**: ZTL–CHE interaction and pathogen effector interference supports clock–immunity crosstalk, but “inflammatory signaling” type annotations are not appropriate for plants. (fu2025apathogeneffector pages 6-7)

### 5.3 Explicit exclusion of unrelated processes requested

No evidence from the retrieved *Arabidopsis* ZTL literature supports roles in:
- **Apoptosis/developmental cell death programs in the animal sense**
- **Pyroptosis**
- **Neuronal functions or synaptic remodeling**
- **Inflammatory signaling pathways**

These terms are animal-centric and should be considered misannotation risks if present. (kiba2007targeteddegradationof pages 1-3, fu2025apathogeneffector pages 6-7)

## 6. Key literature (prioritized recent; includes URLs and publication dates)

### Recent and high-priority (2023–2024)

- **Maeda AE et al. (Sep 2024)**. *Cold-induced degradation of core clock proteins implements temperature compensation in the Arabidopsis circadian clock.* **Science Advances**. https://doi.org/10.1126/sciadv.adq0187 (maeda2024coldinduceddegradationof pages 7-8)
- **Boix M et al. (May 2024)**. *40S Ribosomal protein S6 kinase integrates daylength perception and growth regulation in Arabidopsis thaliana.* **Plant Physiology** 195:3039–3052. https://doi.org/10.1093/plphys/kiae254 (boix202440sribosomalprotein pages 3-4, boix202440sribosomalprotein pages 8-9)
- **Liu L et al. (Jan 2024)**. *GIGANTEA Unveiled: Exploring Its Diverse Roles and Mechanisms.* **Genes** 15:94. https://doi.org/10.3390/genes15010094 (review; use cautiously for direct mechanistic claims) (liu2024giganteaunveiledexploring pages 7-8)

### Recent (2025) mechanistic expansion relevant to substrate scope

- **Fu M et al. (Feb 2025)**. *A pathogen effector HaRxL10 hijacks the circadian clock component CHE to perturb both plant development and immunity.* **Nature Communications** 16. https://doi.org/10.1038/s41467-025-56787-w (ZTL–CHE binding evidence; pathogen interference) (fu2025apathogeneffector pages 6-7)

### Foundational primary evidence for core function (high-confidence)

- **Kiba T et al. (Aug 2007)**. *Targeted Degradation of PSEUDO-RESPONSE REGULATOR5 by an SCF^ZTL Complex Regulates Clock Function and Photomorphogenesis in Arabidopsis thaliana.* **The Plant Cell** 19:2516–2530. https://doi.org/10.1105/tpc.107.053033 (kiba2007targeteddegradationof pages 1-3, kiba2007targeteddegradationof pages 8-9)
- **Fujiwara S et al. (Aug 2008)**. *Post-translational Regulation of the Arabidopsis Circadian Clock through Selective Proteolysis and Phosphorylation of PRR Proteins.* **Journal of Biological Chemistry** 283:23073–23083. https://doi.org/10.1074/jbc.m803471200 (phosphorylation-dependent ZTL binding; blue light stabilization; PRR5 substrate) (fujiwara2008posttranslationalregulationof pages 1-2, fujiwara2008posttranslationalregulationof pages 6-6)
- **Harmon F et al. (Aug 2008)**. *CUL1 regulates TOC1 protein stability in the Arabidopsis circadian clock.* **The Plant Journal** 55:568–579. https://doi.org/10.1111/j.1365-313x.2008.03527.x (SCF dependence of TOC1 degradation; phenocopy of ztl) (harmon2008cul1regulatestoc1 pages 1-2)
- **Baudry A et al. (Mar 2010)**. *F-box proteins FKF1 and LKP2 act in concert with ZEITLUPE to control Arabidopsis clock progression.* **The Plant Cell** 22:606–622. https://doi.org/10.1105/tpc.109.072843 (redundancy among ZTL/FKF1/LKP2; TOC1/PRR5 stabilization) (baudry2010fboxproteinsfkf1 pages 1-2)
- **Kim J et al. (Oct 2013)**. *The F-box protein ZEITLUPE controls stability and nucleocytoplasmic partitioning of GIGANTEA.* **Development** 140:4060–4069. https://doi.org/10.1242/dev.096651 (ZTL cytosol enrichment; GI partitioning; LOV-dependent binding; flowering/circadian implications) (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 5-7, kim2013thefboxprotein media fe7aa0b6)
- **Song YH et al. (Nov 2014)**. *Distinct roles of FKF1, GI, and ZTL in regulation of CONSTANS stability in photoperiodic flowering.* **PNAS** 111:17672–17677. https://doi.org/10.1073/pnas.1415375111 (ZTL in GI/FKF1/CO network) (song2014distinctrolesof pages 1-2)

---

## Summary artifact

| GO aspect | Proposed annotation statement (plain language) | Evidence type | Key experimental support (1 line) | Key substrates/partners | Subcellular context | Best supporting citations |
|---|---|---|---|---|---|---|
| MF | Blue-light-regulated F-box protein that functions as the substrate-recognition subunit of an SCF E3 ubiquitin ligase | Direct primary | ZTL associates functionally with SCF machinery and loss of SCF components phenocopies long-period ztl defects; ZTL promotes proteasome-dependent turnover of clock proteins (harmon2008cul1regulatestoc1 pages 1-2, suetsugu2013evolutionofthree pages 7-8) | ASK1, CUL1, AtRBX1; TOC1, PRR5 | Predominantly cytosol-enriched; active in SCF complex and in GI-associated complexes | Harmon et al. 2008, *Plant Journal*, https://doi.org/10.1111/j.1365-313x.2008.03527.x; Suetsugu & Wada 2013, *Plant Cell Physiology*, https://doi.org/10.1093/pcp/pcs165 (harmon2008cul1regulatestoc1 pages 1-2, suetsugu2013evolutionofthree pages 7-8) |
| MF | Selectively binds PRR5 and TOC1 to target them for ubiquitin-proteasome-mediated degradation | Direct primary | PRR5 physically interacts with ZTL in vivo/in vitro in a PR-domain-dependent manner; PRR5 stability increases when ZTL is inactive, and TOC1 degradation requires SCF function (kiba2007targeteddegradationof pages 8-9, kiba2007targeteddegradationof pages 1-3, harmon2008cul1regulatestoc1 pages 1-2) | PRR5, TOC1 | Clock-associated cytosolic/nuclear proteostasis axis | Kiba et al. 2007, *Plant Cell*, https://doi.org/10.1105/tpc.107.053033; Harmon et al. 2008, *Plant Journal*, https://doi.org/10.1111/j.1365-313x.2008.03527.x (kiba2007targeteddegradationof pages 8-9, kiba2007targeteddegradationof pages 1-3, harmon2008cul1regulatestoc1 pages 1-2) |
| MF | Substrate recognition is enhanced for hyperphosphorylated forms of PRR5 and TOC1 | Direct primary | More highly phosphorylated PRR5 and TOC1 interact best with ZTL, indicating phosphorylation-sensitive substrate recruitment (fujiwara2008posttranslationalregulationof pages 1-2) | PRR5, TOC1, PRR3 | Likely where phosphorylated PRRs accumulate, including nucleus-associated clock protein pools | Fujiwara et al. 2008, *Journal of Biological Chemistry*, https://doi.org/10.1074/jbc.m803471200 (fujiwara2008posttranslationalregulationof pages 1-2) |
| MF | LOV-domain blue-light photoreceptor activity modulates ZTL stability and target turnover | Direct primary | Blue light inhibits in vivo degradation of ZTL and PRR5, and ZTL family proteins are flavin-binding LOV photoreceptors (fujiwara2008posttranslationalregulationof pages 1-2, fujiwara2008novelbluelight pages 1-2, ito2012lovdomaincontainingfbox pages 1-2) | FMN/flavin cofactor; GI; PRR5 | Cytosol-enriched LOV-domain complexes | Fujiwara et al. 2008, *JBC*, https://doi.org/10.1074/jbc.m803471200; Ito et al. 2012, *Molecular Plant*, https://doi.org/10.1093/mp/sss013 (fujiwara2008posttranslationalregulationof pages 1-2, fujiwara2008novelbluelight pages 1-2, ito2012lovdomaincontainingfbox pages 1-2) |
| MF | Binds GIGANTEA (GI) through its LOV domain and reciprocally stabilizes GI/ZTL protein pools | Direct primary | Full-length ZTL and ZTL-LOV bind GI and increase GI protein post-transcriptionally by ~2–4×; disruption alters GI partitioning and ZTL abundance (kim2013thefboxprotein pages 1-2, kim2013thefboxprotein pages 7-8, kim2013thefboxprotein pages 4-5) | GI | Cytosol-enriched GI–ZTL complex | Kim et al. 2013, *Development*, https://doi.org/10.1242/dev.096651 (kim2013thefboxprotein pages 1-2, kim2013thefboxprotein pages 7-8, kim2013thefboxprotein pages 4-5) |
| BP | Core circadian clock regulator that sets free-running period and oscillator robustness by controlling evening protein turnover | Direct primary | ztl mutants show long-period phenotypes; PRR5/TOC1 stabilization and higher-order ztl fkf1 lkp2 mutants further worsen clock defects (baudry2010fboxproteinsfkf1 pages 1-2, geng2006characterizationandfunctional pages 120-125) | TOC1, PRR5, FKF1, LKP2 | SCF^ZTL-linked clock protein turnover network | Baudry et al. 2010, *Plant Cell*, https://doi.org/10.1105/tpc.109.072843; foundational mutant analyses summarized in Geng 2006 thesis excerpt (baudry2010fboxproteinsfkf1 pages 1-2, geng2006characterizationandfunctional pages 120-125) |
| BP | Regulates photomorphogenesis, especially red-light seedling responses, partly through PRR5 degradation | Direct primary | prr5 partially suppresses ztl red-light hypersensitivity, linking the ZTL→PRR5 degradation module to de-etiolation/light-response phenotypes (kiba2007targeteddegradationof pages 8-9, kiba2007targeteddegradationof pages 11-12) | PRR5 | Seedling light-response context | Kiba et al. 2007, *Plant Cell*, https://doi.org/10.1105/tpc.107.053033 (kiba2007targeteddegradationof pages 8-9, kiba2007targeteddegradationof pages 11-12) |
| BP | Modulates photoperiodic flowering indirectly through GI/FKF1/CO network regulation rather than as the primary flowering activator | Direct primary + inferred network | ZTL interacts with GI, FKF1, and CO-related pathways; ZTL overexpression is associated with late flowering and altered GI partitioning that can affect CO stabilization (song2014distinctrolesof pages 1-2, kim2013thefboxprotein pages 7-8) | GI, FKF1, CO, CDFs | Cytosol–nucleus partitioning affecting photoperiod pathway components | Song et al. 2014, *PNAS*, https://doi.org/10.1073/pnas.1415375111; Kim et al. 2013, *Development*, https://doi.org/10.1242/dev.096651 (song2014distinctrolesof pages 1-2, kim2013thefboxprotein pages 7-8) |
| BP | Contributes to temperature compensation of the circadian clock via temperature-dependent control of TOC1/PRR5 abundance | Direct primary (2024) | Quantitative period shifts in ztl and lkp2 ztl mutants across 12–28°C support ZTL as a period-shortening factor in temperature compensation (maeda2024coldinduceddegradationof pages 7-8) | TOC1, PRR5, LKP2 | Clock protein degradation under low/high temperature regimes | Maeda et al. 2024, *Science Advances*, https://doi.org/10.1126/sciadv.adq0187 (maeda2024coldinduceddegradationof pages 7-8) |
| BP | Emerging role in diel proteostasis/growth coupling through regulation of S6K abundance/phosphorylation | Direct primary but still mechanistically emerging (2024) | In ztl-3 mutants, phosphorylated S6K remains abnormally high across the day; authors propose ZTL-dependent proteasome turnover of S6K at dusk (boix202440sribosomalprotein pages 8-9, boix202440sribosomalprotein pages 3-4) | S6K1/S6K-P; TOR pathway context | Diel protein turnover linked to growth/carbohydrate status | Boix et al. 2024, *Plant Physiology*, https://doi.org/10.1093/plphys/kiae254 (boix202440sribosomalprotein pages 8-9, boix202440sribosomalprotein pages 3-4) |
| BP | Possible immunity/clock crosstalk role via ZTL-mediated turnover of CHE, but this is not yet a core Arabidopsis GO assignment for ZTL | Direct primary for interaction; annotation-risk for process extension | CHE binds ZTL in multiple assays, and a pathogen effector disrupts CHE–ZTL interaction; this supports a clock-immunity interface but not a standalone inflammatory/apoptotic role (fu2025apathogeneffector pages 6-7) | CHE; HaRxL10 effector | Interaction observed in heterologous and biochemical systems; clock-associated context | Fu et al. 2025, *Nature Communications*, https://doi.org/10.1038/s41467-025-56787-w (fu2025apathogeneffector pages 6-7) |
| CC | Component of SCF^ZTL ubiquitin ligase complex | Direct primary + review-supported | ZTL co-immunoprecipitates with SCF components and depends on CUL1/AtRBX1 for TOC1-period regulation (harmon2008cul1regulatestoc1 pages 1-2, suetsugu2013evolutionofthree pages 7-8) | ASK1, CUL1, AtRBX1 | SCF ubiquitin ligase complex | Harmon et al. 2008, *Plant Journal*, https://doi.org/10.1111/j.1365-313x.2008.03527.x; Suetsugu & Wada 2013, *Plant Cell Physiology*, https://doi.org/10.1093/pcp/pcs165 (harmon2008cul1regulatestoc1 pages 1-2, suetsugu2013evolutionofthree pages 7-8) |
| CC | Best-supported localization is cytosol-enriched, with functional effects on nucleocytoplasmic partitioning of GI rather than exclusive nuclear residence | Direct primary | GFP-tagged ZTL/ZTL-LOV are cytosol enriched; ZTL shifts GI toward the cytosol and ztl mutants cause increased nuclear GI accumulation (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 7-8, kim2013thefboxprotein pages 5-7) | GI | Cytosol-enriched; affects GI nuclear/cytosolic balance | Kim et al. 2013, *Development*, https://doi.org/10.1242/dev.096651 (kim2013thefboxprotein pages 4-5, kim2013thefboxprotein pages 7-8, kim2013thefboxprotein pages 5-7) |
| CC | Functions in GI–ZTL protein complexes; HSP90-assisted maturation into SCF^ZTL is plausible but should be curated cautiously if only review-backed | Review/inferred in this evidence set | 2024 review summarizes that HSP90 carries GI and facilitates ZTL maturation, but direct primary HSP90 evidence was not extracted here (liu2024giganteaunveiledexploring pages 7-8) | GI, HSP90 | Cytosolic chaperone/assembly context | Liu et al. 2024, *Genes*, https://doi.org/10.3390/genes15010094 (liu2024giganteaunveiledexploring pages 7-8) |


*Table: This table summarizes candidate GO-relevant functions, processes, and localizations for Arabidopsis ZTL, distinguishing direct primary evidence from review-level or emerging inferences. It is designed to support annotation review by separating core conserved roles from newer or higher-risk extensions.*


References

1. (kiba2007targeteddegradationof pages 1-3): Takatoshi Kiba, Rossana Henriques, H. Sakakibara, and N. Chua. Targeted degradation of pseudo-response regulator5 by an scfztl complex regulates clock function and photomorphogenesis in arabidopsis thaliana[w]. The Plant Cell Online, 19:2516-2530, Aug 2007. URL: https://doi.org/10.1105/tpc.107.053033, doi:10.1105/tpc.107.053033. This article has 321 citations.

2. (kiba2007targeteddegradationof pages 8-9): Takatoshi Kiba, Rossana Henriques, H. Sakakibara, and N. Chua. Targeted degradation of pseudo-response regulator5 by an scfztl complex regulates clock function and photomorphogenesis in arabidopsis thaliana[w]. The Plant Cell Online, 19:2516-2530, Aug 2007. URL: https://doi.org/10.1105/tpc.107.053033, doi:10.1105/tpc.107.053033. This article has 321 citations.

3. (fujiwara2008posttranslationalregulationof pages 6-6): Sumire Fujiwara, Lei Wang, Linqu Han, Sung-Suk Suh, Patrice A. Salomé, C. Robertson McClung, and David E. Somers. Post-translational regulation of the arabidopsis circadian clock through selective proteolysis and phosphorylation of pseudo-response regulator proteins*. Journal of Biological Chemistry, 283:23073-23083, Aug 2008. URL: https://doi.org/10.1074/jbc.m803471200, doi:10.1074/jbc.m803471200. This article has 292 citations and is from a domain leading peer-reviewed journal.

4. (fujiwara2008posttranslationalregulationof pages 1-2): Sumire Fujiwara, Lei Wang, Linqu Han, Sung-Suk Suh, Patrice A. Salomé, C. Robertson McClung, and David E. Somers. Post-translational regulation of the arabidopsis circadian clock through selective proteolysis and phosphorylation of pseudo-response regulator proteins*. Journal of Biological Chemistry, 283:23073-23083, Aug 2008. URL: https://doi.org/10.1074/jbc.m803471200, doi:10.1074/jbc.m803471200. This article has 292 citations and is from a domain leading peer-reviewed journal.

5. (boix202440sribosomalprotein pages 3-4): Marc Boix, Alba Garcia-Rodriguez, Laia Castillo, Bernat Miró, Ferga Hamilton, Sanata Tolak, Adrián Pérez, Carolina Monte-Bello, Camila Caldana, and Rossana Henriques. 40s ribosomal protein s6 kinase integrates daylength perception and growth regulation in arabidopsis thaliana. Plant Physiology, 195:3039-3052, May 2024. URL: https://doi.org/10.1093/plphys/kiae254, doi:10.1093/plphys/kiae254. This article has 8 citations and is from a highest quality peer-reviewed journal.

6. (boix202440sribosomalprotein pages 8-9): Marc Boix, Alba Garcia-Rodriguez, Laia Castillo, Bernat Miró, Ferga Hamilton, Sanata Tolak, Adrián Pérez, Carolina Monte-Bello, Camila Caldana, and Rossana Henriques. 40s ribosomal protein s6 kinase integrates daylength perception and growth regulation in arabidopsis thaliana. Plant Physiology, 195:3039-3052, May 2024. URL: https://doi.org/10.1093/plphys/kiae254, doi:10.1093/plphys/kiae254. This article has 8 citations and is from a highest quality peer-reviewed journal.

7. (kim2013thefboxprotein pages 4-5): Jeongsik Kim, Ruishuang Geng, Richard A. Gallenstein, and David E. Somers. The f-box protein zeitlupe controls stability and nucleocytoplasmic partitioning of gigantea. Development, 140:4060-4069, Oct 2013. URL: https://doi.org/10.1242/dev.096651, doi:10.1242/dev.096651. This article has 124 citations and is from a domain leading peer-reviewed journal.

8. (kim2013thefboxprotein pages 5-7): Jeongsik Kim, Ruishuang Geng, Richard A. Gallenstein, and David E. Somers. The f-box protein zeitlupe controls stability and nucleocytoplasmic partitioning of gigantea. Development, 140:4060-4069, Oct 2013. URL: https://doi.org/10.1242/dev.096651, doi:10.1242/dev.096651. This article has 124 citations and is from a domain leading peer-reviewed journal.

9. (kim2013thefboxprotein media fe7aa0b6): Jeongsik Kim, Ruishuang Geng, Richard A. Gallenstein, and David E. Somers. The f-box protein zeitlupe controls stability and nucleocytoplasmic partitioning of gigantea. Development, 140:4060-4069, Oct 2013. URL: https://doi.org/10.1242/dev.096651, doi:10.1242/dev.096651. This article has 124 citations and is from a domain leading peer-reviewed journal.

10. (maeda2024coldinduceddegradationof pages 7-8): Akari E. Maeda, Hiromi Matsuo, Tomoaki Muranaka, and Norihito Nakamichi. Cold-induced degradation of core clock proteins implements temperature compensation in the arabidopsis circadian clock. Science Advances, Sep 2024. URL: https://doi.org/10.1126/sciadv.adq0187, doi:10.1126/sciadv.adq0187. This article has 15 citations and is from a highest quality peer-reviewed journal.

11. (fu2025apathogeneffector pages 6-7): Mengyao Fu, Yaoyu Zhou, Xin Zhang, Keyi Yang, Yufeng Xu, Xingwei Wang, Zhaodan Chen, Yu Wang, Yabo Shi, Lin Ma, Hanguang Liu, Yuhua Deng, Shujing Cheng, Jinfang Chu, Jingyi Song, Tongjun Sun, Yuanchao Wang, Wei Wang, and Mian Zhou. A pathogen effector harxl10 hijacks the circadian clock component che to perturb both plant development and immunity. Nature Communications, Feb 2025. URL: https://doi.org/10.1038/s41467-025-56787-w, doi:10.1038/s41467-025-56787-w. This article has 22 citations and is from a highest quality peer-reviewed journal.

12. (harmon2008cul1regulatestoc1 pages 1-2): Frank Harmon, Takato Imaizumi, and William M. Gray. Cul1 regulates toc1 protein stability in the arabidopsis circadian clock. The Plant journal : for cell and molecular biology, 55 4:568-79, Aug 2008. URL: https://doi.org/10.1111/j.1365-313x.2008.03527.x, doi:10.1111/j.1365-313x.2008.03527.x. This article has 61 citations.

13. (suetsugu2013evolutionofthree pages 7-8): Noriyuki Suetsugu and Masamitsu Wada. Evolution of three lov blue light receptor families in green plants and photosynthetic stramenopiles: phototropin, ztl/fkf1/lkp2 and aureochrome. Plant & cell physiology, 54 1:8-23, Dec 2013. URL: https://doi.org/10.1093/pcp/pcs165, doi:10.1093/pcp/pcs165. This article has 175 citations and is from a domain leading peer-reviewed journal.

14. (kiba2007targeteddegradationof pages 11-12): Takatoshi Kiba, Rossana Henriques, H. Sakakibara, and N. Chua. Targeted degradation of pseudo-response regulator5 by an scfztl complex regulates clock function and photomorphogenesis in arabidopsis thaliana[w]. The Plant Cell Online, 19:2516-2530, Aug 2007. URL: https://doi.org/10.1105/tpc.107.053033, doi:10.1105/tpc.107.053033. This article has 321 citations.

15. (kim2013thefboxprotein pages 7-8): Jeongsik Kim, Ruishuang Geng, Richard A. Gallenstein, and David E. Somers. The f-box protein zeitlupe controls stability and nucleocytoplasmic partitioning of gigantea. Development, 140:4060-4069, Oct 2013. URL: https://doi.org/10.1242/dev.096651, doi:10.1242/dev.096651. This article has 124 citations and is from a domain leading peer-reviewed journal.

16. (fujiwara2008novelbluelight pages 1-2): Sumire Fujiwara. Novel blue light receptors with an f-box: their direct control of the circadian clock and the flowering timing in arabidopsis. Plant Biotechnology, 25:123-129, Mar 2008. URL: https://doi.org/10.5511/plantbiotechnology.25.123, doi:10.5511/plantbiotechnology.25.123. This article has 9 citations and is from a peer-reviewed journal.

17. (liu2024giganteaunveiledexploring pages 7-8): Ling Liu, Yuxin Xie, Baba Salifu Yahaya, and Fengkai Wu. Gigantea unveiled: exploring its diverse roles and mechanisms. Genes, 15:94, Jan 2024. URL: https://doi.org/10.3390/genes15010094, doi:10.3390/genes15010094. This article has 15 citations.

18. (baudry2010fboxproteinsfkf1 pages 1-2): Antoine Baudry, Shogo Ito, Young Hun Song, Alexander A. Strait, Takatoshi Kiba, Sheen Lu, Rossana Henriques, José L. Pruneda-Paz, Nam-Hai Chua, Elaine M. Tobin, Steve A. Kay, and Takato Imaizumi. F-box proteins fkf1 and lkp2 act in concert with zeitlupe to control <i>arabidopsis</i> clock progression. The Plant Cell, 22:606-622, Mar 2010. URL: https://doi.org/10.1105/tpc.109.072843, doi:10.1105/tpc.109.072843. This article has 340 citations.

19. (song2014distinctrolesof pages 1-2): Young Hun Song, Daniel A. Estrada, Richard S. Johnson, Somi K. Kim, Sang Yeol Lee, Michael J. MacCoss, and Takato Imaizumi. Distinct roles of fkf1, gigantea, and zeitlupe proteins in the regulation of constans stability in arabidopsis photoperiodic flowering. Proceedings of the National Academy of Sciences, 111:17672-17677, Nov 2014. URL: https://doi.org/10.1073/pnas.1415375111, doi:10.1073/pnas.1415375111. This article has 228 citations and is from a highest quality peer-reviewed journal.

20. (kim2013thefboxprotein media 1c2acaaa): Jeongsik Kim, Ruishuang Geng, Richard A. Gallenstein, and David E. Somers. The f-box protein zeitlupe controls stability and nucleocytoplasmic partitioning of gigantea. Development, 140:4060-4069, Oct 2013. URL: https://doi.org/10.1242/dev.096651, doi:10.1242/dev.096651. This article has 124 citations and is from a domain leading peer-reviewed journal.

21. (ito2012lovdomaincontainingfbox pages 1-2): Shogo Ito, Young Hun Song, and Takato Imaizumi. Lov domain-containing f-box proteins: light-dependent protein degradation modules in arabidopsis. Molecular plant, 5 3:573-82, May 2012. URL: https://doi.org/10.1093/mp/sss013, doi:10.1093/mp/sss013. This article has 271 citations and is from a highest quality peer-reviewed journal.

22. (kim2013thefboxprotein pages 1-2): Jeongsik Kim, Ruishuang Geng, Richard A. Gallenstein, and David E. Somers. The f-box protein zeitlupe controls stability and nucleocytoplasmic partitioning of gigantea. Development, 140:4060-4069, Oct 2013. URL: https://doi.org/10.1242/dev.096651, doi:10.1242/dev.096651. This article has 124 citations and is from a domain leading peer-reviewed journal.

23. (geng2006characterizationandfunctional pages 120-125): R Geng. Characterization and functional analysis of zeitlupe protein in the regulation of the circadian clock and plant development. Unknown journal, 2006.