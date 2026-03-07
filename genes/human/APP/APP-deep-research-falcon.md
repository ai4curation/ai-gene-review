---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T02:46:51.330324'
end_time: '2026-03-06T02:59:06.425305'
duration_seconds: 735.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: APP
  gene_symbol: APP
  uniprot_accession: P05067
  protein_description: 'RecName: Full=Amyloid-beta precursor protein {ECO:0000312|HGNC:HGNC:620};
    Short=APP {ECO:0000312|HGNC:HGNC:620}; AltName: Full=ABPP; AltName: Full=APPI;
    AltName: Full=Alzheimer disease amyloid A4 protein homolog; AltName: Full=Alzheimer
    disease amyloid protein; AltName: Full=Amyloid precursor protein {ECO:0000305};
    AltName: Full=Amyloid-beta (A4) precursor protein {ECO:0000250|UniProtKB:P12023};
    AltName: Full=Amyloid-beta A4 protein; AltName: Full=Cerebral vascular amyloid
    peptide; Short=CVAP; AltName: Full=PreA4; AltName: Full=Protease nexin-II; Short=PN-II;
    Contains: RecName: Full=N-APP; Contains: RecName: Full=Soluble APP-alpha {ECO:0000303|PubMed:10656250};
    Short=S-APP-alpha {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=Soluble
    APP-beta {ECO:0000303|PubMed:10656250}; Short=S-APP-beta {ECO:0000303|PubMed:10656250};
    Contains: RecName: Full=C99; AltName: Full=Beta-secretase C-terminal fragment
    {ECO:0000303|PubMed:10656250}; Short=Beta-CTF {ECO:0000303|PubMed:10656250}; Contains:
    RecName: Full=Amyloid-beta protein 42 {ECO:0000303|PubMed:8886002}; Short=Abeta42;
    AltName: Full=Beta-APP42; Contains: RecName: Full=Amyloid-beta protein 40 {ECO:0000303|PubMed:8886002};
    Short=Abeta40; AltName: Full=Beta-APP40; Contains: RecName: Full=C83; AltName:
    Full=Alpha-secretase C-terminal fragment {ECO:0000303|PubMed:10656250}; Short=Alpha-CTF
    {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=P3(42); Contains: RecName:
    Full=P3(40); Contains: RecName: Full=C80; Contains: RecName: Full=Gamma-secretase
    C-terminal fragment 59; AltName: Full=Amyloid intracellular domain 59; Short=AICD-59;
    Short=AID(59); AltName: Full=Gamma-CTF(59); Contains: RecName: Full=Gamma-secretase
    C-terminal fragment 57; AltName: Full=Amyloid intracellular domain 57; Short=AICD-57;
    Short=AID(57); AltName: Full=Gamma-CTF(57); Contains: RecName: Full=Gamma-secretase
    C-terminal fragment 50; AltName: Full=Amyloid intracellular domain 50; Short=AICD-50;
    Short=AID(50); AltName: Full=Gamma-CTF(50); Contains: RecName: Full=C31; Flags:
    Precursor;'
  gene_info: Name=APP {ECO:0000312|HGNC:HGNC:620}; Synonyms=A4 {ECO:0000303|PubMed:2881207},
    AD1 {ECO:0000312|HGNC:HGNC:620};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the APP family. {ECO:0000255|PROSITE-
  protein_domains: Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta.
    (IPR013803); Amyloid_glyco_Abeta_sf. (IPR037071); Amyloid_glyco_Cu-bd. (IPR011178)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P05067
- **Protein Description:** RecName: Full=Amyloid-beta precursor protein {ECO:0000312|HGNC:HGNC:620}; Short=APP {ECO:0000312|HGNC:HGNC:620}; AltName: Full=ABPP; AltName: Full=APPI; AltName: Full=Alzheimer disease amyloid A4 protein homolog; AltName: Full=Alzheimer disease amyloid protein; AltName: Full=Amyloid precursor protein {ECO:0000305}; AltName: Full=Amyloid-beta (A4) precursor protein {ECO:0000250|UniProtKB:P12023}; AltName: Full=Amyloid-beta A4 protein; AltName: Full=Cerebral vascular amyloid peptide; Short=CVAP; AltName: Full=PreA4; AltName: Full=Protease nexin-II; Short=PN-II; Contains: RecName: Full=N-APP; Contains: RecName: Full=Soluble APP-alpha {ECO:0000303|PubMed:10656250}; Short=S-APP-alpha {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=Soluble APP-beta {ECO:0000303|PubMed:10656250}; Short=S-APP-beta {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=C99; AltName: Full=Beta-secretase C-terminal fragment {ECO:0000303|PubMed:10656250}; Short=Beta-CTF {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=Amyloid-beta protein 42 {ECO:0000303|PubMed:8886002}; Short=Abeta42; AltName: Full=Beta-APP42; Contains: RecName: Full=Amyloid-beta protein 40 {ECO:0000303|PubMed:8886002}; Short=Abeta40; AltName: Full=Beta-APP40; Contains: RecName: Full=C83; AltName: Full=Alpha-secretase C-terminal fragment {ECO:0000303|PubMed:10656250}; Short=Alpha-CTF {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=P3(42); Contains: RecName: Full=P3(40); Contains: RecName: Full=C80; Contains: RecName: Full=Gamma-secretase C-terminal fragment 59; AltName: Full=Amyloid intracellular domain 59; Short=AICD-59; Short=AID(59); AltName: Full=Gamma-CTF(59); Contains: RecName: Full=Gamma-secretase C-terminal fragment 57; AltName: Full=Amyloid intracellular domain 57; Short=AICD-57; Short=AID(57); AltName: Full=Gamma-CTF(57); Contains: RecName: Full=Gamma-secretase C-terminal fragment 50; AltName: Full=Amyloid intracellular domain 50; Short=AICD-50; Short=AID(50); AltName: Full=Gamma-CTF(50); Contains: RecName: Full=C31; Flags: Precursor;
- **Gene Information:** Name=APP {ECO:0000312|HGNC:HGNC:620}; Synonyms=A4 {ECO:0000303|PubMed:2881207}, AD1 {ECO:0000312|HGNC:HGNC:620};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the APP family. {ECO:0000255|PROSITE-
- **Key Domains:** Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta. (IPR013803); Amyloid_glyco_Abeta_sf. (IPR037071); Amyloid_glyco_Cu-bd. (IPR011178)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "APP" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'APP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **APP** (gene ID: APP, UniProt: P05067) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P05067
- **Protein Description:** RecName: Full=Amyloid-beta precursor protein {ECO:0000312|HGNC:HGNC:620}; Short=APP {ECO:0000312|HGNC:HGNC:620}; AltName: Full=ABPP; AltName: Full=APPI; AltName: Full=Alzheimer disease amyloid A4 protein homolog; AltName: Full=Alzheimer disease amyloid protein; AltName: Full=Amyloid precursor protein {ECO:0000305}; AltName: Full=Amyloid-beta (A4) precursor protein {ECO:0000250|UniProtKB:P12023}; AltName: Full=Amyloid-beta A4 protein; AltName: Full=Cerebral vascular amyloid peptide; Short=CVAP; AltName: Full=PreA4; AltName: Full=Protease nexin-II; Short=PN-II; Contains: RecName: Full=N-APP; Contains: RecName: Full=Soluble APP-alpha {ECO:0000303|PubMed:10656250}; Short=S-APP-alpha {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=Soluble APP-beta {ECO:0000303|PubMed:10656250}; Short=S-APP-beta {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=C99; AltName: Full=Beta-secretase C-terminal fragment {ECO:0000303|PubMed:10656250}; Short=Beta-CTF {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=Amyloid-beta protein 42 {ECO:0000303|PubMed:8886002}; Short=Abeta42; AltName: Full=Beta-APP42; Contains: RecName: Full=Amyloid-beta protein 40 {ECO:0000303|PubMed:8886002}; Short=Abeta40; AltName: Full=Beta-APP40; Contains: RecName: Full=C83; AltName: Full=Alpha-secretase C-terminal fragment {ECO:0000303|PubMed:10656250}; Short=Alpha-CTF {ECO:0000303|PubMed:10656250}; Contains: RecName: Full=P3(42); Contains: RecName: Full=P3(40); Contains: RecName: Full=C80; Contains: RecName: Full=Gamma-secretase C-terminal fragment 59; AltName: Full=Amyloid intracellular domain 59; Short=AICD-59; Short=AID(59); AltName: Full=Gamma-CTF(59); Contains: RecName: Full=Gamma-secretase C-terminal fragment 57; AltName: Full=Amyloid intracellular domain 57; Short=AICD-57; Short=AID(57); AltName: Full=Gamma-CTF(57); Contains: RecName: Full=Gamma-secretase C-terminal fragment 50; AltName: Full=Amyloid intracellular domain 50; Short=AICD-50; Short=AID(50); AltName: Full=Gamma-CTF(50); Contains: RecName: Full=C31; Flags: Precursor;
- **Gene Information:** Name=APP {ECO:0000312|HGNC:HGNC:620}; Synonyms=A4 {ECO:0000303|PubMed:2881207}, AD1 {ECO:0000312|HGNC:HGNC:620};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the APP family. {ECO:0000255|PROSITE-
- **Key Domains:** Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta. (IPR013803); Amyloid_glyco_Abeta_sf. (IPR037071); Amyloid_glyco_Cu-bd. (IPR011178)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "APP" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'APP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **APP** (gene ID: APP, UniProt: P05067) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human APP (Amyloid-beta Precursor Protein; UniProt P05067)

## 0. Target verification (critical disambiguation)
The UniProt accession **P05067** corresponds to **human amyloid-beta precursor protein (APP)**, a **type I single-pass transmembrane glycoprotein** with major brain isoform **APP695** and additional KPI-containing isoforms (APP751/APP770). Multiple independent 2023–2024 sources explicitly describe this same human APP protein and its canonical secretase-dependent processing into sAPPα/sAPPβ, C83/C99, Aβ peptides, and AICD, matching the UniProt description and fragments list. (strope2024thereciprocalrelationship pages 3-4, masi2023thelabyrinthinelandscape pages 2-4, wang2024advancesinthe pages 2-4, martinezdrudis2024roleofpololike pages 32-36)

## 1. Key concepts & definitions (current understanding)

### 1.1 What APP is
APP is a **type I transmembrane protein** that undergoes extensive post-translational modification (e.g., glycosylation, phosphorylation) and is transported through the constitutive secretory system before surface delivery and endocytosis. (strope2024thereciprocalrelationship pages 3-4, martinezdrudis2024roleofpololike pages 32-36)

At the gene level, *APP* is located on **chromosome 21** and is alternatively spliced into multiple isoforms, with **APP695** predominant in neurons and longer isoforms (APP751/770) also present in non-neuronal cells. (strope2024thereciprocalrelationship pages 3-4, masi2023thelabyrinthinelandscape pages 2-4)

### 1.2 Canonical APP processing pathways
APP is proteolytically processed in two principal routes that are defined by the first cleavage event:

**Non-amyloidogenic pathway (α → γ):**
- **α-secretase** (often **ADAM10**) cleaves APP to release **sAPPα** and leave a membrane C-terminal fragment **C83 (CTFα)**.
- **γ-secretase** then cleaves C83 to generate **p3** and the **APP intracellular domain (AICD)**. (strope2024thereciprocalrelationship pages 3-4, baron2024regulationofamyloid pages 41-44, wang2024advancesinthe pages 2-4)

**Amyloidogenic pathway (β → γ):**
- **β-secretase (BACE1)** cleaves APP to release **sAPPβ** and leave **C99 (CTFβ)**.
- **γ-secretase** cleaves C99 to release **Aβ peptides** (that can oligomerize and deposit) and AICD. (strope2024thereciprocalrelationship pages 3-4, baron2024regulationofamyloid pages 41-44, wang2024advancesinthe pages 2-4)

A schematic summary of these pathways and products is shown in a recent cell-biology review figure. (wang2024advancesinthe media 1a611bbf)

### 1.3 Enzymology focus (substrates, specificity)
APP itself is not an enzyme; it is a **substrate** for multiple proteases. In functional-annotation terms, APP’s “primary biochemical function” in AD biology is best described as: **a membrane protein whose regulated proteolysis produces bioactive extracellular and intracellular fragments**, including Aβ species and signaling-competent AICD. (strope2024thereciprocalrelationship pages 3-4, wang2024advancesinthe pages 2-4)

## 2. Subcellular localization, trafficking, and where processing occurs

### 2.1 Trafficking route and compartmentalization
A current model emphasizes **trafficking-driven regulation** of APP processing:
- APP is synthesized in the **ER**, matures in the **Golgi/TGN**, and traffics to the **plasma membrane**, where only a minority of newly made APP appears (~**10%** at the surface in one reviewed estimate). (strope2024thereciprocalrelationship pages 3-4)
- APP undergoes **rapid endocytosis** into **endosomes** and is either recycled or directed to lysosomal degradation. (strope2024thereciprocalrelationship pages 3-4, masi2023thelabyrinthinelandscape pages 2-4)

### 2.2 Why localization matters for Aβ generation
Processing is **spatially segregated**:
- **α-secretase cleavage** is highlighted as occurring mainly at the **plasma membrane**.
- **β-secretase (BACE1)** is enriched in **acidic endosomal/lysosomal compartments**, making endocytosis and endosome residency key determinants of amyloidogenic processing. (strope2024thereciprocalrelationship pages 3-4, masi2023thelabyrinthinelandscape pages 2-4, martinezdrudis2024roleofpololike pages 32-36)

More recent cell-biology work also emphasizes that **co-localization of APP and secretases in the same membrane sub-compartment** is required for cleavage and that advanced imaging (including super-resolution approaches) is refining understanding of where APP and BACE1 co-reside. (wang2024advancesinthe pages 2-4, wang2024advancesinthe pages 1-2)

## 3. Physiological functions of APP and major biological processes

APP and its fragments are implicated in multiple physiological processes, particularly in neurons and synapses:

### 3.1 Synaptic development and function
APP is described as highly expressed at synapses and implicated in **synaptic development and function**, with knockout models showing synaptic and behavioral deficits, supporting an endogenous physiological role beyond pathology. (strope2024thereciprocalrelationship pages 3-4)

### 3.2 Adhesion- and receptor-like functions
Reviews highlight APP’s receptor-like and adhesion-associated roles, including motifs associated with **cell adhesion** and neurodevelopmental processes (synaptogenesis, neurite outgrowth). (strope2024thereciprocalrelationship pages 3-4, masi2023thelabyrinthinelandscape pages 11-13, baron2024regulationofamyloid pages 41-44)

### 3.3 Trophic activity of soluble APP fragments
The extracellular soluble fragment **sAPPα** is repeatedly described as **neurotrophic/neuroprotective** and often contrasted with sAPPβ as having stronger trophic effects. (masi2023thelabyrinthinelandscape pages 11-13, baron2024regulationofamyloid pages 41-44, masi2023thelabyrinthinelandscape pages 29-30)

### 3.4 Mitochondria- and bioenergetics-linked biology
A 2024 review stresses that APP, secretases, and APP processing products localize to multiple organelles (including **endosomes, ER, mitochondria, and ER–mitochondria contact sites**) and argues that relationships between APP metabolism and mitochondrial function remain incompletely resolved but are increasingly studied as part of AD-relevant cell physiology. (strope2024thereciprocalrelationship pages 3-4)

## 4. Recent developments (prioritizing 2023–2024)

### 4.1 “APP dyshomeostasis” framing beyond Aβ alone
A 2024 review argues that AD may reflect **“APP dyshomeostasis”** in which Aβ is important but not the only relevant output, emphasizing that APP dysfunction may impact multiple APP-mediated functions (signaling, synaptic plasticity, adhesion) and that therapeutic strategies beyond anti-Aβ remain underdeveloped. (sirisi2024appdyshomeostasisin pages 1-2)

### 4.2 Trafficking as a mechanistic bottleneck
The 2024 Biochemical Journal review emphasizes that **intracellular trafficking of APP and BACE1** is critical for regulating amyloidogenic processing and Aβ production and that familial AD mutations can impact these trafficking/processing relationships. (wang2024advancesinthe pages 1-2, wang2024advancesinthe pages 2-4)

### 4.3 Precision targeting of γ-secretase: modulation/stabilization vs inhibition
Two 2024 expert perspectives synthesize why early **γ-secretase inhibitors** failed clinically (notably via **Notch-related toxicities** due to γ-secretase’s many substrates), and argue for a precision approach:
- De Strooper & Karran propose **γ-secretase allosteric stabilizers (GSAS)** that increase processivity and shift the Aβ length distribution away from longer aggregation-prone peptides, conceptually opposite to effects of pathogenic presenilin mutations. (strooper2024newprecisionmedicine pages 1-2, strooper2024newprecisionmedicine pages 2-3)
- Wolfe highlights additional complexity: familial AD mutations may cause altered trimming dynamics or potentially harmful stabilization of stalled enzyme–substrate complexes, motivating careful design of modulators rather than broad inhibition. (wolfe2024γsecretaseonceand pages 3-4, wolfe2024γsecretaseonceand pages 1-3)

### 4.4 TBI and APP: convergence of injury biology and amyloidogenesis
A 2023 synthesis highlights that traumatic brain injury can increase expression of APP and amyloidogenic cleavage enzymes near injured axons, linking APP metabolism to post-injury neurodegenerative risk and emphasizing roles of fragments (e.g., sAPPα neuroprotection vs β-CTF/N-APP synaptotoxicity) and inflammatory signaling pathways. (masi2023thelabyrinthinelandscape pages 11-13, masi2023thelabyrinthinelandscape pages 29-30)

## 5. Current applications and real-world implementations

## 5.1 Blood-based biomarkers reflecting APP/Aβ brain pathology (2024)
Although APP is not typically measured directly in blood for clinical decision-making, **APP-derived Aβ peptides** (especially the **Aβ42/40 ratio**) are key components of plasma biomarker panels that aim to infer brain amyloid status (PET/CSF).

### (A) Trial-ready screening use (J-TRC and BioFINDER)
Niimi et al. (May 2024; Alzheimer’s Research & Therapy) evaluated plasma biomarkers against Aβ-PET in **J-TRC (n=474)** and **BioFINDER (n=177)**. Peak AUCs for detecting abnormal Aβ-PET reached **0.936–0.955** in J-TRC using models combining plasma Aβ measures and p-tau217 plus basic covariates (age/sex/APOE), with replication AUCs **0.914–0.938** in BioFINDER. (niimi2024combiningplasmaaβ pages 1-2)

**URL:** https://doi.org/10.1186/s13195-024-01469-w (May 2024). (niimi2024combiningplasmaaβ pages 1-2)

### (B) Memory-clinic implementation potential
Dyer et al. (Aug 2024; Alzheimer’s Research & Therapy) evaluated p-tau217 in a memory-clinic cohort (**n=108**, 64.8% Aβ+ by CSF). Plasma p-tau217 was **>3-fold higher** in Aβ+ vs Aβ− (median **12.4 pg/mL** vs **3.7 pg/mL**) and achieved **AUC 0.91** for detecting Aβ pathology. A two-threshold strategy could avoid **58–68%** of lumbar punctures in this setting (model-based estimate). (dyer2024performanceofplasma pages 1-2)

**URL:** https://doi.org/10.1186/s13195-024-01555-z (Aug 2024). (dyer2024performanceofplasma pages 1-2)

### (C) Commercial test validation: PrecivityAD2 (mass spectrometry)
Meyer et al. (Mar 2024; Alzheimer’s & Dementia) validated a high-throughput LC-MS/MS blood test combining **%p-tau217** with **Aβ42/40** (PrecivityAD2 / APS2) in **n=583** suspected-AD individuals (53% PET-positive). At APS2 cut point **47.5**, sensitivity was **88%** (95% CI 84–91%) and specificity **89%** (95% CI 84–92%), with ~**88% agreement** vs amyloid PET. Extremes of APS2 (>80 or <20) covered **69%** of the cohort and achieved ≥**95%** combined accuracy, while an intermediate category (9.6%) had PPV **92%** and NPV **91%** at observed prevalence 53.6%. (meyer2024clinicalvalidationof pages 10-12)

**URL:** https://doi.org/10.1002/alz.13764 (Mar 2024). (meyer2024clinicalvalidationof pages 1-2, meyer2024clinicalvalidationof pages 10-12)

## 5.2 Therapeutics that act downstream of APP: anti-Aβ monoclonal antibodies
Anti-Aβ antibodies do not target APP directly but operate on the downstream products of APP cleavage. Recent trial/implementation evidence reinforces the translational centrality of APP proteolysis.

### Donanemab (TRAILBLAZER-ALZ 2; subpopulation analysis)
Sato et al. (Apr 2024; Neurology and Therapy) report that in Japanese participants (**N=88**) of TRAILBLAZER-ALZ 2, donanemab showed **38.8–40.2%** slowing of progression on iADRS vs placebo (week 76). Amyloid plaque clearance to <**24.1 Centiloids** occurred in **83.3%** of donanemab-treated participants vs **0%** placebo. ARIA-E occurred in **22.2%** of donanemab-treated vs **2.3%** placebo, with **2.2% symptomatic** in donanemab-treated. (sato2024donanemabinjapanese pages 1-2)

**URL:** https://doi.org/10.1007/s40120-024-00604-x (Apr 2024). (sato2024donanemabinjapanese pages 1-2)

### Plaque reduction vs clinical benefit (cross-program synthesis)
A 2024 synthesis argues that across late-phase anti-Aβ IgG programs, **greater plaque reduction** (using SUVR/centiloid harmonization) associates with **better preservation of clinical function** on placebo-adjusted CDR-SB. (lian2024clarityonthe pages 29-33)

**URL:** https://doi.org/10.1038/s41380-023-02324-4 (published 2024 issue; Molecular Psychiatry). (lian2024clarityonthe pages 29-33)

## 6. Expert opinions and analysis (authoritative perspectives)

### 6.1 Consensus and controversy: amyloid hypothesis and what it implies for APP
Expert reviews emphasize that genetics (APP and presenilin mutations) strongly tie AD to APP processing and Aβ generation, yet clinical translation is complicated: anti-Aβ antibodies show **modest** cognitive slowing and carry safety risks (ARIA), and amyloid burden correlates imperfectly with cognition and mismatches tau topography, suggesting APP dyshomeostasis affects multiple dimensions of neuronal function. (sirisi2024appdyshomeostasisin pages 1-2, wolfe2024γsecretaseonceand pages 1-3)

### 6.2 Where the field is heading
Two convergent 2024 perspectives propose that success may require **(i) earlier intervention** and **(ii) more precise control of γ-secretase processivity**, avoiding broad inhibition that disrupts Notch and other substrates. De Strooper & Karran’s GSAS framing explicitly defines a next-generation mechanism-based prevention concept. (strooper2024newprecisionmedicine pages 1-2, strooper2024newprecisionmedicine pages 2-3)

## 7. Key statistics & data (selected highlights)

### 7.1 Biomarker performance (plasma, 2024)
- **J-TRC/BioFINDER detection of Aβ-PET positivity:** AUC up to **0.955** (J-TRC) and replicated AUC up to **0.938** (BioFINDER) using combined plasma biomarkers and covariates. (niimi2024combiningplasmaaβ pages 1-2)
- **PrecivityAD2 (APS2) vs PET:** sensitivity **88%**, specificity **89%**, PPV **92%** and NPV **91%** (intermediate category; prevalence 53.6%). (meyer2024clinicalvalidationof pages 10-12)
- **Memory-clinic p-tau217:** AUC **0.91**; p-tau217 ~**12.4 pg/mL** (Aβ+) vs **3.7 pg/mL** (Aβ−). (dyer2024performanceofplasma pages 1-2)
- **Preclinical PET classification improvements (AHEAD, 2024):** Aβ42/40 alone AUC **0.87**, p-tau217/np-tau217 ratio AUC **0.92**, combined model AUC **0.95**. (rissman2024plasmaaβ42aβ40and pages 1-2)

### 7.2 Therapeutic outcomes (anti-Aβ, 2024)
- **Donanemab (TRAILBLAZER-ALZ 2 Japan subpopulation):** iADRS slowing **38.8–40.2%**; amyloid clearance **83.3%** vs 0%; ARIA-E **22.2%** vs 2.3%. (sato2024donanemabinjapanese pages 1-2)

## 8. Evidence-supported functional annotation summary (for databases)

**Molecular function (annotation-style):** Type I transmembrane protein and protease substrate whose regulated proteolysis generates soluble ectodomains (sAPPα/sAPPβ), membrane CTFs (C83/C99), Aβ peptides, and AICD; fragment signaling and trafficking-dependent cleavage underpin both physiological synaptic functions and AD-related pathology. (strope2024thereciprocalrelationship pages 3-4, wang2024advancesinthe pages 2-4, wang2024advancesinthe media 1a611bbf)

**Biological processes:** Secretory trafficking and endocytosis; synapse development and plasticity; cell adhesion; production of amyloidogenic peptides via BACE1/γ-secretase; modulation of neuronal homeostasis and mitochondrial-linked physiology (area of active research). (strope2024thereciprocalrelationship pages 3-4, wang2024advancesinthe pages 2-4)

**Cellular components (where it acts):** ER/Golgi/TGN (biosynthesis and sorting), plasma membrane (surface residence and α-cleavage), endosomes/endo-lysosomal system (β-cleavage and sorting), with reported localization of APP and metabolites also in mitochondria and ER–mitochondria contacts in reviewed literature. (strope2024thereciprocalrelationship pages 3-4, masi2023thelabyrinthinelandscape pages 2-4)


---

## Summary Table

| Aspect | Current Understanding (2023–2024) | Key Quantitative Data | Key Sources |
| :--- | :--- | :--- | :--- |
| **Protein Identity & Structure** | Human APP (P05067) is a Type I transmembrane protein. Major neuronal isoform is APP695; others (APP751/770) contain KPI domains. Includes E1/E2 extracellular domains and a C-terminal internalization motif (YENPTY). | Gene: *APP* on Chr 21, ~400kbp, 18 exons. p3 fragment size ~3 kDa. | Strope & Wilkins, 2024 (strope2024thereciprocalrelationship pages 3-4); Masi et al., 2023 (masi2023thelabyrinthinelandscape pages 2-4); Martínez-Drudis, 2024 (martinezdrudis2024roleofpololike pages 32-36) |
| **Processing Pathways** | **Non-amyloidogenic**: $\alpha$-secretase (ADAM10) $\to$ sAPP$\alpha$ + C83. **Amyloidogenic**: $\beta$-secretase (BACE1) $\to$ sAPP$\beta$ + C99 $\to$ A$\beta$. $\gamma$-secretase cleavage generates AICD. "Allosteric stabilizers" (GSAS) proposed to fix processivity rather than inhibit enzyme. | Cleavage products: sAPP$\alpha$, sAPP$\beta$, C83, C99, A$\beta$, AICD. | Wang et al., 2024 (wang2024advancesinthe pages 2-4); De Strooper & Karran, 2024 (strooper2024newprecisionmedicine pages 1-2); Figure 1 (wang2024advancesinthe media 1a611bbf) |
| **Trafficking & Localization** | Traffics via secretory pathway (ER $\to$ Golgi $\to$ PM) and endocytic routes. Processing is spatially regulated: $\alpha$-cleavage mainly at PM; $\beta$-cleavage in acidic endosomes. | ~10% of nascent APP reaches cell surface. Super-resolution reveals low APP-BACE1 co-localization in secretory organelles. | Strope & Wilkins, 2024 (strope2024thereciprocalrelationship pages 3-4); Wang et al., 2024 (wang2024advancesinthe pages 2-4); Baron, 2024 (baron2024regulationofamyloid pages 41-44) |
| **Physiological Functions** | Synaptic formation, plasticity, and cell adhesion (synaptic adhesion molecule). sAPP$\alpha$ is neurotrophic/neuroprotective. Modulates mitochondrial function and bioenergetics. | - | Strope & Wilkins, 2024 (strope2024thereciprocalrelationship pages 3-4); Masi et al., 2023 (masi2023thelabyrinthinelandscape pages 29-30); Baron, 2024 (baron2024regulationofamyloid pages 41-44) |
| **Disease Relevance (AD)** | FAD mutations destabilize $\gamma$-secretase/substrate, increasing toxic long A$\beta$. APP/CTF accumulation at organelle contacts disrupts lysosomes. TBI upregulates APP/secretases. | Presenilin mutations affect A$\beta$ length spectrum. | De Strooper & Karran, 2024 (strooper2024newprecisionmedicine pages 1-2); Wang et al., 2024 (wang2024advancesinthe pages 2-4); Masi et al., 2023 (masi2023thelabyrinthinelandscape pages 11-13) |
| **Clinical Biomarkers** | Plasma p-tau217 and A$\beta$42/40 ratio accurately predict brain amyloid status (PET), reducing need for invasive tests. Used in "PrecivityAD2" and trials. | **AUC 0.94–0.96** for p-tau217/A$\beta$42 models; **88% Sensitivity / 89% Specificity** for PrecivityAD2 vs PET. | Niimi et al., 2024 (niimi2024combiningplasmaaβ pages 1-2); Meyer et al., 2024 (meyer2024clinicalvalidationof pages 1-2); Dyer et al., 2024 (dyer2024performanceofplasma pages 1-2) |
| **Therapeutic Targeting** | Anti-amyloid mAbs (Lecanemab, Donanemab) remove plaques and slow cognitive decline. Focus shifting from broad $\gamma$-secretase inhibitors to modulators/stabilizers (GSAS). | Donanemab slowed decline by **~38–40%** (iADRS) in early AD; **83.3%** of treated Japanese sub-cohort achieved clearance (<24.1 Centiloids). | Sato et al., 2024 (sato2024donanemabinjapanese pages 1-2); Ribeiro et al., 2024 (ribeiro2024therapeuticanalysisof pages 18-21); De Strooper & Karran, 2024 (strooper2024newprecisionmedicine pages 1-2) |


*Table: This table synthesizes current research (2023–2024) on the structure, processing, biological roles, and clinical applications associated with human APP, highlighting quantitative biomarker performance and therapeutic outcomes.*

## Key mechanistic figure (APP processing)
A figure depicting the non-amyloidogenic and amyloidogenic processing of APP (secretases and fragment products) is available from the Biochemical Journal 2024 review. (wang2024advancesinthe media 1a611bbf)


References

1. (strope2024thereciprocalrelationship pages 3-4): Taylor A. Strope and Heather M. Wilkins. The reciprocal relationship between amyloid precursor protein and mitochondrial function. Journal of Neurochemistry, 168:2275-2284, Jul 2024. URL: https://doi.org/10.1111/jnc.16183, doi:10.1111/jnc.16183. This article has 9 citations and is from a domain leading peer-reviewed journal.

2. (masi2023thelabyrinthinelandscape pages 2-4): Mirco Masi, Fabrizio Biundo, André Fiou, Marco Racchi, Alessia Pascale, and Erica Buoso. The labyrinthine landscape of app processing: state of the art and possible novel soluble app-related molecular players in traumatic brain injury and neurodegeneration. International Journal of Molecular Sciences, 24:6639, Apr 2023. URL: https://doi.org/10.3390/ijms24076639, doi:10.3390/ijms24076639. This article has 20 citations.

3. (wang2024advancesinthe pages 2-4): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 15 citations and is from a domain leading peer-reviewed journal.

4. (martinezdrudis2024roleofpololike pages 32-36): L Martínez-Drudis. Role of polo-like kinase 2 in the pathogenesis and treatment of alzheimer's disease. Unknown journal, 2024.

5. (baron2024regulationofamyloid pages 41-44): SKV Baron. Regulation of amyloid precursor protein processing pathway by β-secretase and its impact on alzheimer's disease physiopathology. Unknown journal, 2024.

6. (wang2024advancesinthe media 1a611bbf): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 15 citations and is from a domain leading peer-reviewed journal.

7. (wang2024advancesinthe pages 1-2): Jingqi Wang, Lou Fourriere, and Paul A. Gleeson. Advances in the cell biology of the trafficking and processing of amyloid precursor protein: impact of familial alzheimer's disease mutations. Biochemical Journal, 481:1297-1325, Sep 2024. URL: https://doi.org/10.1042/bcj20240056, doi:10.1042/bcj20240056. This article has 15 citations and is from a domain leading peer-reviewed journal.

8. (masi2023thelabyrinthinelandscape pages 11-13): Mirco Masi, Fabrizio Biundo, André Fiou, Marco Racchi, Alessia Pascale, and Erica Buoso. The labyrinthine landscape of app processing: state of the art and possible novel soluble app-related molecular players in traumatic brain injury and neurodegeneration. International Journal of Molecular Sciences, 24:6639, Apr 2023. URL: https://doi.org/10.3390/ijms24076639, doi:10.3390/ijms24076639. This article has 20 citations.

9. (masi2023thelabyrinthinelandscape pages 29-30): Mirco Masi, Fabrizio Biundo, André Fiou, Marco Racchi, Alessia Pascale, and Erica Buoso. The labyrinthine landscape of app processing: state of the art and possible novel soluble app-related molecular players in traumatic brain injury and neurodegeneration. International Journal of Molecular Sciences, 24:6639, Apr 2023. URL: https://doi.org/10.3390/ijms24076639, doi:10.3390/ijms24076639. This article has 20 citations.

10. (sirisi2024appdyshomeostasisin pages 1-2): Sònia Sirisi, Érika Sánchez-Aced, Olivia Belbin, and Alberto Lleó. App dyshomeostasis in the pathogenesis of alzheimer’s disease: implications for current drug targets. Alzheimer's Research & Therapy, Jun 2024. URL: https://doi.org/10.1186/s13195-024-01504-w, doi:10.1186/s13195-024-01504-w. This article has 30 citations and is from a domain leading peer-reviewed journal.

11. (strooper2024newprecisionmedicine pages 1-2): Bart de Strooper and Eric H. Karran. New precision medicine avenues to the prevention of alzheimer’s disease from insights into the structure and function of γ-secretases. The EMBO Journal, 43(6):887-903, Feb 2024. URL: https://doi.org/10.1038/s44318-024-00057-w, doi:10.1038/s44318-024-00057-w. This article has 33 citations.

12. (strooper2024newprecisionmedicine pages 2-3): Bart de Strooper and Eric H. Karran. New precision medicine avenues to the prevention of alzheimer’s disease from insights into the structure and function of γ-secretases. The EMBO Journal, 43(6):887-903, Feb 2024. URL: https://doi.org/10.1038/s44318-024-00057-w, doi:10.1038/s44318-024-00057-w. This article has 33 citations.

13. (wolfe2024γsecretaseonceand pages 3-4): Michael S. Wolfe. Γ-secretase: once and future drug target for alzheimer’s disease. Expert Opinion on Drug Discovery, 19:5-8, Nov 2024. URL: https://doi.org/10.1080/17460441.2023.2277350, doi:10.1080/17460441.2023.2277350. This article has 15 citations and is from a peer-reviewed journal.

14. (wolfe2024γsecretaseonceand pages 1-3): Michael S. Wolfe. Γ-secretase: once and future drug target for alzheimer’s disease. Expert Opinion on Drug Discovery, 19:5-8, Nov 2024. URL: https://doi.org/10.1080/17460441.2023.2277350, doi:10.1080/17460441.2023.2277350. This article has 15 citations and is from a peer-reviewed journal.

15. (niimi2024combiningplasmaaβ pages 1-2): Yoshiki Niimi, Shorena Janelidze, Kenichiro Sato, Naoki Tomita, Tadashi Tsukamoto, Takashi Kato, Kenji Yoshiyama, Hisatomo Kowa, Atsushi Iwata, Ryoko Ihara, Kazushi Suzuki, Kensaku Kasuga, Takeshi Ikeuchi, Kenji Ishii, Kengo Ito, Akinori Nakamura, Michio Senda, Theresa A. Day, Samantha C. Burnham, Leonardo Iaccarino, Michael J. Pontecorvo, Oskar Hansson, and Takeshi Iwatsubo. Combining plasma aβ and p-tau217 improves detection of brain amyloid in non-demented elderly. Alzheimer's Research & Therapy, May 2024. URL: https://doi.org/10.1186/s13195-024-01469-w, doi:10.1186/s13195-024-01469-w. This article has 61 citations and is from a domain leading peer-reviewed journal.

16. (dyer2024performanceofplasma pages 1-2): Adam H. Dyer, Helena Dolphin, Antoinette O’Connor, Laura Morrison, Gavin Sedgwick, Conor Young, Emily Killeen, Conal Gallagher, Aoife McFeely, Eimear Connolly, Naomi Davey, Paul Claffey, Paddy Doyle, Shane Lyons, Christine Gaffney, Ruth Ennis, Cathy McHale, Jasmine Joseph, Graham Knight, Emmet Kelly, Cliona O’Farrelly, Aoife Fallon, Sean O’Dowd, Nollaig M. Bourke, and Sean P. Kennelly. Performance of plasma p-tau217 for the detection of amyloid-β positivity in a memory clinic cohort using an electrochemiluminescence immunoassay. Alzheimer's Research & Therapy, Aug 2024. URL: https://doi.org/10.1186/s13195-024-01555-z, doi:10.1186/s13195-024-01555-z. This article has 27 citations and is from a domain leading peer-reviewed journal.

17. (meyer2024clinicalvalidationof pages 10-12): Matthew R. Meyer, Kristopher M. Kirmess, Stephanie Eastwood, Traci L. Wente‐Roth, Faith Irvin, Mary S. Holubasch, Venky Venkatesh, Ilana Fogelman, Mark Monane, Lucy Hanna, Gil D. Rabinovici, Barry A. Siegel, Rachel A. Whitmer, Charles Apgar, Randall J. Bateman, David M. Holtzman, Michael Irizarry, David Verbel, Pallavi Sachdev, Satoshi Ito, John Contois, Kevin E. Yarasheski, Joel B. Braunstein, Philip B. Verghese, and Tim West. Clinical validation of the precivityad2 blood test: a mass spectrometry‐based test with algorithm combining %p‐tau217 and aβ42/40 ratio to identify presence of brain amyloid. Alzheimer's & Dementia, 20:3179-3192, Mar 2024. URL: https://doi.org/10.1002/alz.13764, doi:10.1002/alz.13764. This article has 105 citations and is from a highest quality peer-reviewed journal.

18. (meyer2024clinicalvalidationof pages 1-2): Matthew R. Meyer, Kristopher M. Kirmess, Stephanie Eastwood, Traci L. Wente‐Roth, Faith Irvin, Mary S. Holubasch, Venky Venkatesh, Ilana Fogelman, Mark Monane, Lucy Hanna, Gil D. Rabinovici, Barry A. Siegel, Rachel A. Whitmer, Charles Apgar, Randall J. Bateman, David M. Holtzman, Michael Irizarry, David Verbel, Pallavi Sachdev, Satoshi Ito, John Contois, Kevin E. Yarasheski, Joel B. Braunstein, Philip B. Verghese, and Tim West. Clinical validation of the precivityad2 blood test: a mass spectrometry‐based test with algorithm combining %p‐tau217 and aβ42/40 ratio to identify presence of brain amyloid. Alzheimer's & Dementia, 20:3179-3192, Mar 2024. URL: https://doi.org/10.1002/alz.13764, doi:10.1002/alz.13764. This article has 105 citations and is from a highest quality peer-reviewed journal.

19. (sato2024donanemabinjapanese pages 1-2): Shoichiro Sato, Naohisa Hatakeyama, Shinji Fujikoshi, Sadao Katayama, Hideaki Katagiri, and John R. Sims. Donanemab in japanese patients with early alzheimer’s disease: subpopulation analysis of the trailblazer-alz 2 randomized trial. Neurology and Therapy, 13:677-695, Apr 2024. URL: https://doi.org/10.1007/s40120-024-00604-x, doi:10.1007/s40120-024-00604-x. This article has 18 citations and is from a domain leading peer-reviewed journal.

20. (lian2024clarityonthe pages 29-33): Yan Lian, Yu-Juan Jia, Joelyn Wong, Xin-Fu Zhou, Weihong Song, Junhong Guo, Colin L. Masters, and Yan-Jiang Wang. Clarity on the blazing trail: clearing the way for amyloid-removing therapies for alzheimer’s disease. Molecular Psychiatry, 29(2):297-305, Nov 2024. URL: https://doi.org/10.1038/s41380-023-02324-4, doi:10.1038/s41380-023-02324-4. This article has 23 citations and is from a highest quality peer-reviewed journal.

21. (rissman2024plasmaaβ42aβ40and pages 1-2): Robert A. Rissman, Oliver Langford, Rema Raman, Michael C. Donohue, Sara Abdel‐Latif, Matthew R. Meyer, Traci Wente‐Roth, Kristopher M. Kirmess, Jennifer Ngolab, Charisse N. Winston, Gustavo Jimenez‐Maggiora, Michael S. Rafii, Pallavi Sachdev, Tim West, Kevin E. Yarasheski, Joel B. Braunstein, Michael Irizarry, Keith A. Johnson, Paul S. Aisen, and Reisa A. Sperling. Plasma aβ42/aβ40 and phospho‐tau217 concentration ratios increase the accuracy of amyloid pet classification in preclinical alzheimer's disease. Alzheimer's & Dementia, 20:1214-1224, Nov 2024. URL: https://doi.org/10.1002/alz.13542, doi:10.1002/alz.13542. This article has 130 citations and is from a highest quality peer-reviewed journal.

22. (ribeiro2024therapeuticanalysisof pages 18-21): Gabriel França Ribeiro, Isabella Gaiarim de Andrade, Marcos Augusto Bustamante de Vasconcellos, Rayanne Cruz Rodrigues, Márcia Bandeira Bringel, Geovanna Cristina Gonçalves da Silva Cordeiro, Gabriel Abrantes Farias, Sandra Inês Lins de Abreu Mendes, Ana Carolina Barambo Wagner, Juliana Nunes Ferreira Nascimento, Dieckson de Oliveira Batista, Gabriele Luisa de Souza Cruz, Stephany Fernandes de Paiva, Thainara Ferreira Campos, and Thaise Freire Andrade. Therapeutic analysis of donanemab in the treatment of patients with alzheimer's disease. Caderno Pedagógico, 21:e7019, Aug 2024. URL: https://doi.org/10.54033/cadpedv21n8-207, doi:10.54033/cadpedv21n8-207. This article has 0 citations.

## Citations

1. strope2024thereciprocalrelationship pages 3-4
2. sirisi2024appdyshomeostasisin pages 1-2
3. dyer2024performanceofplasma pages 1-2
4. meyer2024clinicalvalidationof pages 10-12
5. sato2024donanemabinjapanese pages 1-2
6. lian2024clarityonthe pages 29-33
7. masi2023thelabyrinthinelandscape pages 2-4
8. martinezdrudis2024roleofpololike pages 32-36
9. wang2024advancesinthe pages 2-4
10. strooper2024newprecisionmedicine pages 1-2
11. baron2024regulationofamyloid pages 41-44
12. masi2023thelabyrinthinelandscape pages 29-30
13. masi2023thelabyrinthinelandscape pages 11-13
14. meyer2024clinicalvalidationof pages 1-2
15. ribeiro2024therapeuticanalysisof pages 18-21
16. wang2024advancesinthe pages 1-2
17. strooper2024newprecisionmedicine pages 2-3
18. https://doi.org/10.1186/s13195-024-01469-w
19. https://doi.org/10.1186/s13195-024-01555-z
20. https://doi.org/10.1002/alz.13764
21. https://doi.org/10.1007/s40120-024-00604-x
22. https://doi.org/10.1038/s41380-023-02324-4
23. https://doi.org/10.1111/jnc.16183,
24. https://doi.org/10.3390/ijms24076639,
25. https://doi.org/10.1042/bcj20240056,
26. https://doi.org/10.1186/s13195-024-01504-w,
27. https://doi.org/10.1038/s44318-024-00057-w,
28. https://doi.org/10.1080/17460441.2023.2277350,
29. https://doi.org/10.1186/s13195-024-01469-w,
30. https://doi.org/10.1186/s13195-024-01555-z,
31. https://doi.org/10.1002/alz.13764,
32. https://doi.org/10.1007/s40120-024-00604-x,
33. https://doi.org/10.1038/s41380-023-02324-4,
34. https://doi.org/10.1002/alz.13542,
35. https://doi.org/10.54033/cadpedv21n8-207,