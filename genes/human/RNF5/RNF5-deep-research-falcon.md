---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T04:47:36.891883'
end_time: '2026-06-12T05:02:08.223244'
duration_seconds: 871.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RNF5
  gene_symbol: RNF5
  uniprot_accession: Q99942
  protein_description: 'RecName: Full=E3 ubiquitin-protein ligase RNF5 {ECO:0000305};
    EC=2.3.2.27 {ECO:0000269|PubMed:19269966, ECO:0000269|PubMed:19285439, ECO:0000269|PubMed:23093945};
    AltName: Full=RING finger protein 5 {ECO:0000303|PubMed:9533025}; AltName: Full=Ram1
    homolog {ECO:0000303|PubMed:16176924}; Short=HsRma1 {ECO:0000303|PubMed:16176924};'
  gene_info: Name=RNF5 {ECO:0000303|PubMed:9533025, ECO:0000312|HGNC:HGNC:10068};
    Synonyms=G16 {ECO:0000303|Ref.3}, NG2, RMA1 {ECO:0000303|PubMed:11329381};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the RNF5 family. .
  protein_domains: RNF5/RNF185-like. (IPR045103); Znf_RING. (IPR001841); Znf_RING/FYVE/PHD.
    (IPR013083); Znf_RING_CS. (IPR017907); zf-C3HC4_3 (PF13920)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: RNF5-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: RNF5-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000017 The document does not contain a schematic
    labeled as Figure 1 that summarizes the pathway; Figure 1 in this paper focuses
    on charac'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q99942
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase RNF5 {ECO:0000305}; EC=2.3.2.27 {ECO:0000269|PubMed:19269966, ECO:0000269|PubMed:19285439, ECO:0000269|PubMed:23093945}; AltName: Full=RING finger protein 5 {ECO:0000303|PubMed:9533025}; AltName: Full=Ram1 homolog {ECO:0000303|PubMed:16176924}; Short=HsRma1 {ECO:0000303|PubMed:16176924};
- **Gene Information:** Name=RNF5 {ECO:0000303|PubMed:9533025, ECO:0000312|HGNC:HGNC:10068}; Synonyms=G16 {ECO:0000303|Ref.3}, NG2, RMA1 {ECO:0000303|PubMed:11329381};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the RNF5 family. .
- **Key Domains:** RNF5/RNF185-like. (IPR045103); Znf_RING. (IPR001841); Znf_RING/FYVE/PHD. (IPR013083); Znf_RING_CS. (IPR017907); zf-C3HC4_3 (PF13920)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RNF5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RNF5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RNF5** (gene ID: RNF5, UniProt: Q99942) in human.

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
- **UniProt Accession:** Q99942
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase RNF5 {ECO:0000305}; EC=2.3.2.27 {ECO:0000269|PubMed:19269966, ECO:0000269|PubMed:19285439, ECO:0000269|PubMed:23093945}; AltName: Full=RING finger protein 5 {ECO:0000303|PubMed:9533025}; AltName: Full=Ram1 homolog {ECO:0000303|PubMed:16176924}; Short=HsRma1 {ECO:0000303|PubMed:16176924};
- **Gene Information:** Name=RNF5 {ECO:0000303|PubMed:9533025, ECO:0000312|HGNC:HGNC:10068}; Synonyms=G16 {ECO:0000303|Ref.3}, NG2, RMA1 {ECO:0000303|PubMed:11329381};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the RNF5 family. .
- **Key Domains:** RNF5/RNF185-like. (IPR045103); Znf_RING. (IPR001841); Znf_RING/FYVE/PHD. (IPR013083); Znf_RING_CS. (IPR017907); zf-C3HC4_3 (PF13920)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RNF5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RNF5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RNF5** (gene ID: RNF5, UniProt: Q99942) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: Human RNF5 (UniProt Q99942) functional annotation (2023–2024 emphasis)

### 0) Target verification (critical)
The requested target is **human RNF5** (ring finger protein 5), UniProt **Q99942**, also known as **RMA1**. Recent CFTR/ERAD and innate-immunity literature consistently describes RNF5 as an **ER-anchored/ER-embedded RING E3 ubiquitin ligase** with C-terminal transmembrane segment(s), matching the UniProt-provided identity and domain architecture (RING finger with membrane anchor). (okiyoneda2024targetingubiquitinationmachinery pages 4-7, brusa2023innovativestrategytoward pages 9-11, kamada2024herc3facilitateserad pages 1-2)

### 1) Key concepts and definitions (current understanding)

#### 1.1 Ubiquitination and E3 ligases
RNF5 functions as an **E3 ubiquitin ligase**, i.e., an enzyme that catalyzes transfer of ubiquitin from an E2 enzyme to substrate proteins, thereby modulating substrate fate (often proteasomal degradation depending on ubiquitin chain topology). In the contexts retrieved here, RNF5 is repeatedly linked to **proteasome-directed ubiquitination**, particularly in ER quality control and innate immune adaptor turnover. (ge2024rnf5inhibitingantiviral pages 4-5, okiyoneda2024targetingubiquitinationmachinery pages 4-7)

#### 1.2 ER-associated degradation (ERAD) and ER quality control (ERQC)
**ERAD** is the principal pathway for disposing of misfolded or unassembled proteins in the endoplasmic reticulum. RNF5 is one of several ER membrane E3 ligases that recognize misfolded membrane proteins and initiate ubiquitination, targeting them for extraction and degradation by the proteasome. In CFTR biology, RNF5 is described as an **ER-anchored E3** that detects folding/assembly defects at early biogenesis stages and contributes to degradation of misfolded CFTR variants such as F508del. (okiyoneda2024targetingubiquitinationmachinery pages 4-7, kamada2024herc3facilitateserad pages 1-2)

#### 1.3 Innate immune adaptor regulation (cGAS–STING and RIG-I/MAVS)
In antiviral innate immunity, adaptor proteins such as **STING (MITA)** and **MAVS (VISA)** drive type I interferon signaling. RNF5 is described as a **negative regulator** of these pathways by mediating ubiquitination and degradation of key adaptors (e.g., STING, MAVS) and downstream signaling proteins (e.g., IRF3 via recruitment mechanisms). (ge2024rnf5inhibitingantiviral pages 5-7, ge2024rnf5inhibitingantiviral pages 4-5)

### 2) RNF5 molecular function, localization, and substrate specificity

#### 2.1 Subcellular localization
Across multiple sources, RNF5 is described as **ER-anchored/ER-embedded** and membrane-associated, consistent with its principal roles in ERQC/ERAD and membrane-proximal innate signaling regulation. (okiyoneda2024targetingubiquitinationmachinery pages 4-7, kamada2024herc3facilitateserad pages 1-2)

#### 2.2 RNF5 in CFTR ERAD: substrate recognition and pathway placement
**CFTR-F508del** is a misfolding-prone variant targeted for ERAD. RNF5 is described as recognizing folding/assembly defects in CFTR, including defects sensed at the N-terminus, and operating **sequentially with CHIP** (RNF5 early; CHIP later/post-translational) in monitoring CFTR folding status. (okiyoneda2024targetingubiquitinationmachinery pages 4-7)

Mechanistic placement supported by several sources:
- RNF5 contributes to ubiquitination of **immature/core-glycosylated CFTR (Band B)** rather than the mature plasma-membrane form (Band C), consistent with an early ER quality-control role. (riepe2024smallmoleculecorrectorsdivert pages 3-4)
- RNF5 was described as recognizing N-terminal regions/MSD1 and initiating ubiquitin chain formation that can be **elongated by gp78/AMFR** to facilitate ERAD. (kamada2024herc3facilitateserad pages 1-2)
- RNF5 shows **redundancy/compensation** with RNF185 (another ER membrane E3), which helps explain why single-gene perturbations can yield modest stabilization. (riepe2024smallmoleculecorrectorsdivert pages 3-4, okiyoneda2024targetingubiquitinationmachinery pages 11-13)

#### 2.3 Innate immunity substrates: STING, MAVS, IRF3
A 2024 review focused on RNF5 in antiviral signaling summarizes that RNF5 promotes ubiquitination and degradation of **STING** and **MAVS**, thereby inhibiting antiviral innate immunity. (ge2024rnf5inhibitingantiviral pages 5-7, ge2024rnf5inhibitingantiviral pages 4-5)

Residue-level details reported (from sources cited within the 2024 MI study’s mechanistic background and consistent with the innate-immunity review):
- STING/MITA targeted at **K150** (degradative ubiquitination context). (wan2024ringfingerprotein pages 12-13, ge2024rnf5inhibitingantiviral pages 4-5)
- MAVS/VISA ubiquitination at **K362** and **K461** with proteasome-dependent degradation. (wan2024ringfingerprotein pages 12-13, ge2024rnf5inhibitingantiviral pages 4-5)
- Activated **IRF3** can be degraded in a complex where JMJD6 recruits RNF5, as summarized in the innate-immunity-focused review. (ge2024rnf5inhibitingantiviral pages 4-5)

#### 2.4 Autophagy-related regulation (ATG4B)
RNF5 has also been connected to autophagy regulation by controlling the stability of autophagy proteins. In the context of RNF5 inhibition strategies in CF, RNF5 inhibition (inh-2 and optimized analogues) is reported to increase **basal autophagy**, consistent with prior descriptions that RNF5 can promote **ATG4B degradation** and that RNF5 inhibitors interfere with this effect. (brusa2023innovativestrategytoward pages 9-11, brusa2023innovativestrategytoward pages 14-15)

#### 2.5 Cardiovascular signaling (ASK1)
A 2024 mouse/cardiomyocyte study proposes a cardioprotective role for RNF5, reporting that RNF5 downregulation occurs in infarcted heart tissue and that RNF5 knockout worsens myocardial infarction phenotypes, while RNF5 overexpression is protective; mechanistically, protection is attributed to inhibition of **ASK1 activation** (phosphorylation), though the directness of RNF5’s E3 action on ASK1 is not fully resolved in the provided excerpt. (wan2024ringfingerprotein pages 12-13)

### 3) Recent developments (prioritizing 2023–2024)

#### 3.1 Genome-wide CRISPR screens redefine RNF5’s role as important but partially redundant in CFTR-F508del ERAD (2024)
A 2024 Molecular Biology of the Cell study performed genome-wide CRISPR/Cas9 screens to identify machinery driving CFTR-F508del ERAD.
- **Scale**: **20,528 genes** screened; **207 high-confidence hits** at **FDR < 1%**. (riepe2024smallmoleculecorrectorsdivert pages 3-4)
- **Key result**: RNF5 was the **top E3 ligase hit**, but **RNF5 knockout only modestly reduced CFTR-F508del degradation**, supporting robustness and redundancy. (riepe2024smallmoleculecorrectorsdivert pages 3-4, riepe2024smallmoleculecorrectorsdivert pages 1-2)
- **Redundancy**: secondary screens in an RNF5 knockout background identified **RNF185** as a redundant ligase. (riepe2024smallmoleculecorrectorsdivert pages 3-4, okiyoneda2024targetingubiquitinationmachinery pages 11-13)
- **Quantitative kinetics**: CFTR-F508del reporter showed a degradation half-life of about **34 minutes** in the reported system. (riepe2024smallmoleculecorrectorsdivert pages 3-4)

A schematic (Figure 4A) from this work summarizes sequential folding states and proposes that small-molecule correctors stabilize folding states that are not RNF5 substrates. (riepe2024smallmoleculecorrectorsdivert media 192d3a11)

#### 3.2 Medicinal chemistry progress: thiadiazole RNF5 inhibitors that enhance mutant CFTR rescue (2023)
A 2023 Journal of Medicinal Chemistry study advanced RNF5 inhibition as a CF strategy.
- **Inhibitor scaffold**: inh-2 (1,2,4-thiadiazol-5-ylidene) described as a first-in-class RNF5 inhibitor, with SAR leading to improved analogues including **compound/analogue 16**. (brusa2023innovativestrategytoward pages 14-15, brusa2023innovativestrategytoward pages 1-3)
- **On-target validation**: analogue 16 improved CFTR rescue in control (NT siRNA) cells but **not** in **RNF5 siRNA** cells, consistent with RNF5-dependent activity. (brusa2023innovativestrategytoward pages 11-14)
- **Experimental concentrations** (useful for real-world reproducibility): compounds commonly tested at **5 μM**, with CFTR correctors used at **VX-809 1–3 μM**, **VX-445 3 μM**, and **VX-661 + VX-445 10 μM + 3 μM**; MG-132 used at **10 μM** for ubiquitination assays. (brusa2023innovativestrategytoward pages 11-14)
- **Autophagy link**: analogue 16 increased basal autophagy, consistent with RNF5 inhibition phenotypes. (brusa2023innovativestrategytoward pages 11-14, brusa2023innovativestrategytoward pages 14-15)

#### 3.3 Updated CF translational assessment: no ubiquitination-pathway drugs in CF clinical trials (2024 review)
A 2024 review focused on targeting ubiquitination machinery in CF notes that, despite long-standing interest, **no compounds targeting ubiquitination have entered clinical trials for CF** (at least as of June 2024 publication). (okiyoneda2024targetingubiquitinationmachinery pages 4-7)

The same review summarizes:
- RNF5 as an ER-anchored E3 that recognizes CFTR folding defects, pairs with E2 enzymes (e.g., UBE2J1), and acts sequentially with CHIP. (okiyoneda2024targetingubiquitinationmachinery pages 4-7)
- Preclinical results in which **in vivo suppression of RNF5** in F508del-CFTR transgenic mice improved intestinal malabsorption and increased CFTR activity in intestinal epithelial cells. (okiyoneda2024targetingubiquitinationmachinery pages 4-7)

#### 3.4 RNF5 as an innate-immunity node and potential host-directed antiviral target (2024 review)
A 2024 Frontiers in Immunology review describes RNF5 as a key modulator of antiviral signaling and virus life cycle through ubiquitination of host innate-immune proteins (STING, MAVS, IRF3) and also viral proteins (notably in SARS-CoV-2 and KSHV contexts). (ge2024rnf5inhibitingantiviral pages 5-7, ge2024rnf5inhibitingantiviral pages 7-9)

### 4) Current applications and real-world implementations

#### 4.1 Cystic fibrosis: modulating RNF5-mediated ubiquitination to rescue CFTR
The most concrete application in the retrieved corpus is RNF5 inhibition to stabilize immature F508del-CFTR and improve response to CFTR correctors.
- **Real-world relevance**: Over **80%** of people with CF carry the F508del mutation, making the pathway broadly relevant to CF therapeutics. (riepe2024smallmoleculecorrectorsdivert pages 1-2)
- **Implementation status**: RNF5 inhibitors (inh-2, analogue 16) have been tested in airway epithelial models and in combination with clinically used correctors, but **translation remains preclinical**, and reviews emphasize lack of clinical trials targeting ubiquitination in CF. (okiyoneda2024targetingubiquitinationmachinery pages 4-7, brusa2023innovativestrategytoward pages 11-14)

#### 4.2 Host-directed antiviral strategies
RNF5 modulation (both inhibition and activation) is discussed as a strategy to shift antiviral signaling and/or viral replication steps, but this is currently largely mechanistic/preclinical in the provided corpus. (ge2024rnf5inhibitingantiviral pages 5-7, ge2024rnf5inhibitingantiviral pages 7-9)

#### 4.3 Cardiovascular disease models
RNF5 has been proposed as a cardioprotective regulator in myocardial infarction via the ASK1 pathway, based on genetic manipulation in mice and cardiomyocyte models; translation to therapy is not yet demonstrated in the provided evidence. (wan2024ringfingerprotein pages 12-13)

### 5) Expert opinions and analysis (authoritative perspectives)

#### 5.1 CF field perspective: redundancy and risk-benefit constraints
The 2024 CF ubiquitination review emphasizes both the appeal and difficulty of targeting ubiquitination: blocking ubiquitination to stabilize mutant CFTR has been considered for a long time, but progress has been slow and clinical translation has not yet occurred. It also highlights that approved corrector combinations (e.g., Trikafta/Kaftrio) demonstrate the effectiveness of pharmacological chaperone approaches that do not broadly interfere with cell signaling. (okiyoneda2024targetingubiquitinationmachinery pages 4-7)

#### 5.2 Systems view from CRISPR genetics: RNF5 is a major node but not sufficient alone
The 2024 CRISPR screen study shows RNF5 is the top E3 hit for CFTR-F508del ERAD, but RNF5 loss produces only modest stabilization, consistent with **redundant E3 ligase networks** (RNF185 and others). This has practical implications: RNF5 inhibitors may need combination approaches or context-dependent use to yield clinically meaningful stabilization. (riepe2024smallmoleculecorrectorsdivert pages 3-4, okiyoneda2024targetingubiquitinationmachinery pages 11-13)

#### 5.3 Innate immunity perspective: RNF5 as a negative regulator of STING/MAVS
The 2024 RNF5 antiviral-immunity review frames RNF5 as a “novel means of modulating antiviral immunity,” emphasizing both host control mechanisms and viral exploitation of RNF5. This positions RNF5 as a plausible therapeutic lever, but also highlights pathway complexity and context-dependent outcomes. (ge2024rnf5inhibitingantiviral pages 5-7, ge2024rnf5inhibitingantiviral pages 7-9)

### 6) Relevant statistics and data points (recent studies)
- **CF genetics**: F508del is present in **>80%** of people with CF (reported in 2024 MBoC paper) and affects **~80%** of CF patients worldwide (reported in 2023 J Med Chem paper). (riepe2024smallmoleculecorrectorsdivert pages 1-2, brusa2023innovativestrategytoward pages 1-3)
- **CRISPR screen scale (2024)**: **20,528 genes** screened; **207 high-confidence hits** at **FDR < 1%**. (riepe2024smallmoleculecorrectorsdivert pages 3-4)
- **CFTR-F508del ERAD kinetics**: majority of reporter degraded with half-life ~**34 min** in the described system. (riepe2024smallmoleculecorrectorsdivert pages 3-4)
- **Drug/chemical biology concentrations used (2023)**: RNF5 inhibitors tested typically at **5 μM**; CFTR correctors VX-809 **1–3 μM**, VX-445 **3 μM**, VX-661 + VX-445 **10 μM + 3 μM**; MG-132 **10 μM**. (brusa2023innovativestrategytoward pages 11-14)
- **Open Targets disease association evidence (database aggregation)**: RNF5 is associated with multiple diseases including cystic fibrosis and neoplasms; example association scores shown in the retrieved Open Targets output include cystic fibrosis **0.4753**, neoplasm **0.1277**, glioblastoma multiforme **0.1098**, acute lymphoblastic leukemia **0.1049**, and experimental autoimmune encephalomyelitis **0.1039** (note: these are Open Targets model scores, not effect sizes from a single experiment). (OpenTargets Search: -RNF5)

### 7) Mechanistic summary figure
The following image provides a mechanistic synthesis of CFTR-F508del folding states and the proposed point at which RNF5-mediated ubiquitination targets early folding intermediates, while correctors stabilize RNF5-resistant states. (riepe2024smallmoleculecorrectorsdivert media 192d3a11)

### 8) Summary and functional annotation statement
Human RNF5 (UniProt Q99942) is best supported as an **ER-embedded RING E3 ubiquitin ligase** that (i) participates in **ER quality control/ERAD** of misfolded membrane proteins—most prominently **CFTR-F508del**—by acting at early biogenesis stages on immature ER-resident intermediates, in collaboration with specific E2 enzymes and partially redundant ER E3 ligases; and (ii) regulates **innate immunity** by promoting ubiquitination-dependent degradation of signaling adaptors such as **STING** and **MAVS**, thereby dampening antiviral interferon signaling; RNF5 also interfaces with **autophagy regulation** (e.g., ATG4B stability) and has emerging disease-model roles (e.g., **ASK1 signaling** in myocardial infarction). Recent 2023–2024 work positions RNF5 as an attractive but challenging therapeutic target because of **network redundancy** and the current gap between preclinical modulators (e.g., thiadiazole inhibitors) and clinical translation, particularly in cystic fibrosis. (ge2024rnf5inhibitingantiviral pages 5-7, okiyoneda2024targetingubiquitinationmachinery pages 4-7, riepe2024smallmoleculecorrectorsdivert pages 3-4, brusa2023innovativestrategytoward pages 11-14)

---

### Appendix: compact evidence map
| Biological context/pathway | RNF5 molecular action | Key substrates/partners and specific lysines/linkages when available | Subcellular localization context | Recent 2023–2024 findings/applications with quantitative details | Primary supporting source |
|---|---|---|---|---|---|
| ERAD / proteostasis | RING E3 ubiquitin ligase; ubiquitinates immature membrane proteins for proteasomal ERAD | CFTR N-terminus/MSD1 recognized; partners include UBE2J1, UBE2D3, RNF185, gp78/AMFR, HERC3; acts mainly on immature CFTR Band B (okiyoneda2024targetingubiquitinationmachinery pages 4-7, riepe2024smallmoleculecorrectorsdivert pages 3-4, okiyoneda2024targetingubiquitinationmachinery pages 11-13, kamada2024herc3facilitateserad pages 1-2) | ER-anchored / ER-embedded membrane ligase with C-terminal TM region(s) (okiyoneda2024targetingubiquitinationmachinery pages 4-7, brusa2023innovativestrategytoward pages 9-11, kamada2024herc3facilitateserad pages 1-2) | Genome-wide CRISPR screen assayed **20,528 genes** and found **207 high-confidence hits (FDR <1%)**; RNF5 was top E3 hit, UBE2D3 top E2; RNF5 KO had only modest effect, supporting pathway redundancy (riepe2024smallmoleculecorrectorsdivert pages 3-4) | *Small-molecule correctors divert CFTR-F508del from ERAD by stabilizing sequential folding states* (2024), https://doi.org/10.1091/mbc.e23-08-0336 |
| CFTR-F508del | Promotes ubiquitination and degradation of misfolded F508del-CFTR; early triage E3 in sequential ERQC | F508del-CFTR; sequential action with CHIP; RNF185 can compensate; correctors stabilize RNF5-resistant folding states (okiyoneda2024targetingubiquitinationmachinery pages 4-7, riepe2024smallmoleculecorrectorsdivert pages 3-4, okiyoneda2024targetingubiquitinationmachinery pages 11-13, riepe2024smallmoleculecorrectorsdivert media 192d3a11) | ER membrane / ERQC on nascent or immature CFTR before plasma-membrane maturation (okiyoneda2024targetingubiquitinationmachinery pages 4-7, riepe2024smallmoleculecorrectorsdivert pages 3-4, kamada2024herc3facilitateserad pages 1-2, riepe2024smallmoleculecorrectorsdivert media 192d3a11) | F508del occurs in **>80%** of people with CF / affects **~80%** of CF patients worldwide; RNF5 suppression improved intestinal malabsorption and CFTR activity in F508del-transgenic mice; no RNF5-targeting compounds reported in clinical trials in the provided context (okiyoneda2024targetingubiquitinationmachinery pages 4-7, riepe2024smallmoleculecorrectorsdivert pages 1-2, brusa2023innovativestrategytoward pages 1-3) | *Targeting ubiquitination machinery in cystic fibrosis: Where do we stand?* (2024), https://doi.org/10.1007/s00018-024-05295-z |
| CFTR-F508del therapeutic targeting | Pharmacologic RNF5 inhibition / degradation to reduce CFTR ubiquitination | inh-2 (first-in-class RNF5 inhibitor), analogue 16, FX12; analogue 16 effect lost with RNF5 siRNA, supporting on-target action (brusa2023innovativestrategytoward pages 11-14, brusa2023innovativestrategytoward pages 14-15, brusa2023innovativestrategytoward pages 1-3) | ER-associated RNF5 targeted indirectly by small molecules in airway epithelial cell models (brusa2023innovativestrategytoward pages 11-14, brusa2023innovativestrategytoward pages 14-15) | Compound testing commonly at **5 μM**; VX-809 **1–3 μM**, VX-445 **3 μM**, VX-661 + VX-445 **10 μM + 3 μM**, MG-132 **10 μM**; analogue 16 was among the most promising compounds (11, 16, 21) and improved rescue with ELX/TEZ/IVA in CFBE41o− cells; FX12 active in BHK cells but not differentiated primary airway epithelia (brusa2023innovativestrategytoward pages 11-14, brusa2023innovativestrategytoward pages 14-15, okiyoneda2024targetingubiquitinationmachinery pages 4-7) | *Innovative Strategy toward Mutant CFTR Rescue in Cystic Fibrosis: Design and Synthesis of Thiadiazole Inhibitors of the E3 Ligase RNF5* (2023), https://doi.org/10.1021/acs.jmedchem.3c00608 |
| Innate immunity: cGAS-STING / MAVS / IRF3 | E3 ligase that mainly promotes degradative ubiquitination of antiviral signaling adaptors; K48 linked for STING/MAVS in mammalian studies summarized in review | STING/MITA at **K150** (K48-linked); MAVS/VISA at **K362** and **K461**; activated IRF3 degraded after recruitment by JMJD6; viral proteins can hijack RNF5 and alter linkage usage (K27/K29/K63 also discussed in viral contexts) (wan2024ringfingerprotein pages 12-13, ge2024rnf5inhibitingantiviral pages 9-10, ge2024rnf5inhibitingantiviral pages 4-5) | ER-associated; MAVS regulation occurs in mitochondria-associated antiviral signaling context; STING at ER/ERGIC-associated innate immune membranes (ge2024rnf5inhibitingantiviral pages 9-10, ge2024rnf5inhibitingantiviral pages 4-5) | 2024 review emphasizes RNF5 as a negative regulator of antiviral innate immunity and a possible host-directed target; no clinical-stage RNF5 immune modulators reported in the provided context (ge2024rnf5inhibitingantiviral pages 5-7, ge2024rnf5inhibitingantiviral pages 9-10, ge2024rnf5inhibitingantiviral pages 4-5) | *RNF5: inhibiting antiviral immunity and shaping virus life cycle* (2024), https://doi.org/10.3389/fimmu.2023.1324516 |
| Autophagy | Regulates autophagy by targeting autophagy machinery components for degradation | ATG4B is a reported RNF5 substrate; inh-2 and analogue 16 increase basal autophagy consistent with blocking RNF5-mediated turnover; PTGDR2 can compete with ATG4B for RNF5 binding in gastric CSC context (brusa2023innovativestrategytoward pages 11-14, brusa2023innovativestrategytoward pages 9-11, brusa2023innovativestrategytoward pages 14-15) | ER-associated RNF5 with effects on cytosolic autophagy regulators (brusa2023innovativestrategytoward pages 9-11, brusa2023innovativestrategytoward pages 14-15) | Autophagy vacuoles increased with inh-2 and compounds 11/16/21; torin-1 used at **20 nM**, SAR-405 at **2 μM** in functional autophagy assays (brusa2023innovativestrategytoward pages 11-14) | *Innovative Strategy toward Mutant CFTR Rescue in Cystic Fibrosis: Design and Synthesis of Thiadiazole Inhibitors of the E3 Ligase RNF5* (2023), https://doi.org/10.1021/acs.jmedchem.3c00608 |
| Cardiovascular | Protective E3-ligase-associated role in stress signaling; inhibits ASK1 pathway in MI model | ASK1 pathway implicated; whether direct ubiquitination of ASK1 is established was unresolved in provided context (wan2024ringfingerprotein pages 12-13) | Cardiac cells/tissue; RNF5 downregulated in infarcted mouse heart and OGD-treated cardiomyocytes (wan2024ringfingerprotein pages 12-13) | 2024 mouse/cell study: RNF5 knockout worsened myocardial infarction-associated dysfunction, inflammation, and apoptosis, while overexpression was protective; quantitative effect sizes not provided in context (wan2024ringfingerprotein pages 12-13) | *RING finger protein 5 protects against acute myocardial infarction by inhibiting ASK1* (2024), https://doi.org/10.1186/s12872-024-04070-z |
| Oncology / other | Context-dependent E3 ligase affecting tumor signaling, proteostasis, and therapeutic response | EphA2/Eph receptors, paxillin, ATG4B; Open Targets links RNF5 to neoplasm, glioblastoma, ALL, cystic fibrosis, and EAE based on supporting literature (ge2024rnf5inhibitingantiviral pages 7-9, ge2024rnf5inhibitingantiviral pages 9-10, OpenTargets Search: -RNF5) | ER-associated ligase with downstream effects on signaling, migration, and transcriptional programs (ge2024rnf5inhibitingantiviral pages 7-9, ge2024rnf5inhibitingantiviral pages 9-10) | Open Targets evidence scores in provided context: cystic fibrosis association **0.4753**, neoplasm **0.1277**, glioblastoma **0.1098**, ALL **0.1049**, EAE **0.1039**; preclinical therapeutic interest noted in AML, KSHV/PEL, and breast-cancer signaling, but no clinical trials reported here (OpenTargets Search: -RNF5, ge2024rnf5inhibitingantiviral pages 9-10) | Open Targets disease-target associations for RNF5 (accessed via provided context) (OpenTargets Search: -RNF5) |


*Table: This table summarizes evidence-based functional annotation for human RNF5 (UniProt Q99942), organized by pathway context, molecular action, substrates, localization, and recent translational findings. It is useful as a compact reference for RNF5’s validated roles in ERAD, CFTR quality control, innate immunity, autophagy, cardiovascular biology, and disease associations.*

References

1. (okiyoneda2024targetingubiquitinationmachinery pages 4-7): Tsukasa Okiyoneda, Christian Borgo, Valentina Bosello Travain, Nicoletta Pedemonte, and Mauro Salvi. Targeting ubiquitination machinery in cystic fibrosis: where do we stand? Cellular and Molecular Life Sciences: CMLS, Jun 2024. URL: https://doi.org/10.1007/s00018-024-05295-z, doi:10.1007/s00018-024-05295-z. This article has 6 citations.

2. (brusa2023innovativestrategytoward pages 9-11): Irene Brusa, Elvira Sondo, Emanuela Pesce, Valeria Tomati, Dario Gioia, Federico Falchi, Beatrice Balboni, Jose Antonio Ortega Martínez, Marina Veronesi, Elisa Romeo, Natasha Margaroli, Maurizio Recanatini, Stefania Girotto, Nicoletta Pedemonte, Marinella Roberti, and Andrea Cavalli. Innovative strategy toward mutant cftr rescue in cystic fibrosis: design and synthesis of thiadiazole inhibitors of the e3 ligase rnf5. Journal of Medicinal Chemistry, 66:9797-9822, Jul 2023. URL: https://doi.org/10.1021/acs.jmedchem.3c00608, doi:10.1021/acs.jmedchem.3c00608. This article has 14 citations and is from a highest quality peer-reviewed journal.

3. (kamada2024herc3facilitateserad pages 1-2): Yuka Kamada, Yuko Ohnishi, Chikako Nakashima, Aika Fujii, Mana Terakawa, Ikuto Hamano, Uta Nakayamada, Saori Katoh, Noriaki Hirata, Hazuki Tateishi, Ryosuke Fukuda, Hirotaka Takahashi, Gergely L. Lukacs, and Tsukasa Okiyoneda. Herc3 facilitates erad of select membrane proteins by recognizing membrane-spanning domains. The Journal of Cell Biology, May 2024. URL: https://doi.org/10.1083/jcb.202308003, doi:10.1083/jcb.202308003. This article has 13 citations.

4. (ge2024rnf5inhibitingantiviral pages 4-5): Junyi Ge and Leiliang Zhang. Rnf5: inhibiting antiviral immunity and shaping virus life cycle. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1324516, doi:10.3389/fimmu.2023.1324516. This article has 9 citations and is from a peer-reviewed journal.

5. (ge2024rnf5inhibitingantiviral pages 5-7): Junyi Ge and Leiliang Zhang. Rnf5: inhibiting antiviral immunity and shaping virus life cycle. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1324516, doi:10.3389/fimmu.2023.1324516. This article has 9 citations and is from a peer-reviewed journal.

6. (riepe2024smallmoleculecorrectorsdivert pages 3-4): Celeste Riepe, Magda Wąchalska, Kirandeep K. Deol, Anais K. Amaya, Matthew H. Porteus, James A. Olzmann, and Ron R. Kopito. Small-molecule correctors divert cftr-f508del from erad by stabilizing sequential folding states. Molecular Biology of the Cell, Feb 2024. URL: https://doi.org/10.1091/mbc.e23-08-0336, doi:10.1091/mbc.e23-08-0336. This article has 10 citations and is from a domain leading peer-reviewed journal.

7. (okiyoneda2024targetingubiquitinationmachinery pages 11-13): Tsukasa Okiyoneda, Christian Borgo, Valentina Bosello Travain, Nicoletta Pedemonte, and Mauro Salvi. Targeting ubiquitination machinery in cystic fibrosis: where do we stand? Cellular and Molecular Life Sciences: CMLS, Jun 2024. URL: https://doi.org/10.1007/s00018-024-05295-z, doi:10.1007/s00018-024-05295-z. This article has 6 citations.

8. (wan2024ringfingerprotein pages 12-13): Hong Wan, Jianqing Zhang, Zhen Liu, Bizhen Dong, Zhangqian Tao, Guanglin Wang, and Chihua Wang. Ring finger protein 5 protects against acute myocardial infarction by inhibiting ask1. BMC Cardiovascular Disorders, Aug 2024. URL: https://doi.org/10.1186/s12872-024-04070-z, doi:10.1186/s12872-024-04070-z. This article has 4 citations and is from a peer-reviewed journal.

9. (brusa2023innovativestrategytoward pages 14-15): Irene Brusa, Elvira Sondo, Emanuela Pesce, Valeria Tomati, Dario Gioia, Federico Falchi, Beatrice Balboni, Jose Antonio Ortega Martínez, Marina Veronesi, Elisa Romeo, Natasha Margaroli, Maurizio Recanatini, Stefania Girotto, Nicoletta Pedemonte, Marinella Roberti, and Andrea Cavalli. Innovative strategy toward mutant cftr rescue in cystic fibrosis: design and synthesis of thiadiazole inhibitors of the e3 ligase rnf5. Journal of Medicinal Chemistry, 66:9797-9822, Jul 2023. URL: https://doi.org/10.1021/acs.jmedchem.3c00608, doi:10.1021/acs.jmedchem.3c00608. This article has 14 citations and is from a highest quality peer-reviewed journal.

10. (riepe2024smallmoleculecorrectorsdivert pages 1-2): Celeste Riepe, Magda Wąchalska, Kirandeep K. Deol, Anais K. Amaya, Matthew H. Porteus, James A. Olzmann, and Ron R. Kopito. Small-molecule correctors divert cftr-f508del from erad by stabilizing sequential folding states. Molecular Biology of the Cell, Feb 2024. URL: https://doi.org/10.1091/mbc.e23-08-0336, doi:10.1091/mbc.e23-08-0336. This article has 10 citations and is from a domain leading peer-reviewed journal.

11. (riepe2024smallmoleculecorrectorsdivert media 192d3a11): Celeste Riepe, Magda Wąchalska, Kirandeep K. Deol, Anais K. Amaya, Matthew H. Porteus, James A. Olzmann, and Ron R. Kopito. Small-molecule correctors divert cftr-f508del from erad by stabilizing sequential folding states. Molecular Biology of the Cell, Feb 2024. URL: https://doi.org/10.1091/mbc.e23-08-0336, doi:10.1091/mbc.e23-08-0336. This article has 10 citations and is from a domain leading peer-reviewed journal.

12. (brusa2023innovativestrategytoward pages 1-3): Irene Brusa, Elvira Sondo, Emanuela Pesce, Valeria Tomati, Dario Gioia, Federico Falchi, Beatrice Balboni, Jose Antonio Ortega Martínez, Marina Veronesi, Elisa Romeo, Natasha Margaroli, Maurizio Recanatini, Stefania Girotto, Nicoletta Pedemonte, Marinella Roberti, and Andrea Cavalli. Innovative strategy toward mutant cftr rescue in cystic fibrosis: design and synthesis of thiadiazole inhibitors of the e3 ligase rnf5. Journal of Medicinal Chemistry, 66:9797-9822, Jul 2023. URL: https://doi.org/10.1021/acs.jmedchem.3c00608, doi:10.1021/acs.jmedchem.3c00608. This article has 14 citations and is from a highest quality peer-reviewed journal.

13. (brusa2023innovativestrategytoward pages 11-14): Irene Brusa, Elvira Sondo, Emanuela Pesce, Valeria Tomati, Dario Gioia, Federico Falchi, Beatrice Balboni, Jose Antonio Ortega Martínez, Marina Veronesi, Elisa Romeo, Natasha Margaroli, Maurizio Recanatini, Stefania Girotto, Nicoletta Pedemonte, Marinella Roberti, and Andrea Cavalli. Innovative strategy toward mutant cftr rescue in cystic fibrosis: design and synthesis of thiadiazole inhibitors of the e3 ligase rnf5. Journal of Medicinal Chemistry, 66:9797-9822, Jul 2023. URL: https://doi.org/10.1021/acs.jmedchem.3c00608, doi:10.1021/acs.jmedchem.3c00608. This article has 14 citations and is from a highest quality peer-reviewed journal.

14. (ge2024rnf5inhibitingantiviral pages 7-9): Junyi Ge and Leiliang Zhang. Rnf5: inhibiting antiviral immunity and shaping virus life cycle. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1324516, doi:10.3389/fimmu.2023.1324516. This article has 9 citations and is from a peer-reviewed journal.

15. (OpenTargets Search: -RNF5): Open Targets Query (-RNF5, 38 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (ge2024rnf5inhibitingantiviral pages 9-10): Junyi Ge and Leiliang Zhang. Rnf5: inhibiting antiviral immunity and shaping virus life cycle. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1324516, doi:10.3389/fimmu.2023.1324516. This article has 9 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](RNF5-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000017 The document does not contain a schematic labeled as Figure 1 that summarizes the pathway; Figure 1 in this paper focuses on charac](RNF5-deep-research-falcon_artifacts/image-1.png)

## Citations

1. okiyoneda2024targetingubiquitinationmachinery pages 4-7
2. riepe2024smallmoleculecorrectorsdivert pages 3-4
3. wan2024ringfingerprotein pages 12-13
4. brusa2023innovativestrategytoward pages 11-14
5. riepe2024smallmoleculecorrectorsdivert pages 1-2
6. brusa2023innovativestrategytoward pages 9-11
7. okiyoneda2024targetingubiquitinationmachinery pages 11-13
8. brusa2023innovativestrategytoward pages 14-15
9. brusa2023innovativestrategytoward pages 1-3
10. https://doi.org/10.1091/mbc.e23-08-0336
11. https://doi.org/10.1007/s00018-024-05295-z
12. https://doi.org/10.1021/acs.jmedchem.3c00608
13. https://doi.org/10.3389/fimmu.2023.1324516
14. https://doi.org/10.1186/s12872-024-04070-z
15. https://doi.org/10.1007/s00018-024-05295-z,
16. https://doi.org/10.1021/acs.jmedchem.3c00608,
17. https://doi.org/10.1083/jcb.202308003,
18. https://doi.org/10.3389/fimmu.2023.1324516,
19. https://doi.org/10.1091/mbc.e23-08-0336,
20. https://doi.org/10.1186/s12872-024-04070-z,