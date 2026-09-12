---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T13:56:27.363693'
end_time: '2026-09-08T14:09:25.570693'
duration_seconds: 778.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: WEE1
  gene_symbol: WEE1
  uniprot_accession: P30291
  protein_description: 'RecName: Full=Wee1-like protein kinase; Short=WEE1hu; EC=2.7.10.2
    {ECO:0000269|PubMed:7743995, ECO:0000269|PubMed:8428596}; AltName: Full=Wee1A
    kinase;'
  gene_info: Name=WEE1 {ECO:0000303|PubMed:8348613, ECO:0000312|HGNC:HGNC:12761};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: CC_SR_Kinase. (IPR050339); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom.
    (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: WEE1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P30291
- **Protein Description:** RecName: Full=Wee1-like protein kinase; Short=WEE1hu; EC=2.7.10.2 {ECO:0000269|PubMed:7743995, ECO:0000269|PubMed:8428596}; AltName: Full=Wee1A kinase;
- **Gene Information:** Name=WEE1 {ECO:0000303|PubMed:8348613, ECO:0000312|HGNC:HGNC:12761};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** CC_SR_Kinase. (IPR050339); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "WEE1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'WEE1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **WEE1** (gene ID: WEE1, UniProt: P30291) in human.

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
- **UniProt Accession:** P30291
- **Protein Description:** RecName: Full=Wee1-like protein kinase; Short=WEE1hu; EC=2.7.10.2 {ECO:0000269|PubMed:7743995, ECO:0000269|PubMed:8428596}; AltName: Full=Wee1A kinase;
- **Gene Information:** Name=WEE1 {ECO:0000303|PubMed:8348613, ECO:0000312|HGNC:HGNC:12761};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** CC_SR_Kinase. (IPR050339); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "WEE1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'WEE1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **WEE1** (gene ID: WEE1, UniProt: P30291) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human WEE1 (UniProt P30291): Functional-Annotation Research Report

## Executive summary

The requested target is correctly identified. **WEE1** in this report is the human **WEE1 G2-checkpoint kinase**, also called **Wee1A/WEE1hu**, corresponding to UniProt **P30291**. It is not the germ-cell-enriched paralogue **WEE2/Wee1B**, nor the membrane-associated related kinase **PKMYT1/Myt1**. Human WEE1 is a roughly 646–647-residue, predominantly nuclear protein with a large N-terminal regulatory region and a C-terminal protein-kinase domain. This architecture agrees with the supplied UniProt kinase-family and domain annotations. (mcgowan1995cellcycleregulation pages 2-3, zhu2017structuralbasisof pages 1-2, zhu2017structuralbasisof pages 8-10, mcgowan1995cellcycleregulation pages 6-8)

Its best-established biochemical function is ATP-dependent inhibitory phosphorylation of **CDK1 at Tyr15**, principally in the CDK1–cyclin-B complex. WEE1 also restrains **CDK2 through Tyr15 phosphorylation**, linking it to intra-S-phase replication control. WEE1 does not supply the adjacent inhibitory CDK1 Thr14 phosphorylation; PKMYT1 can phosphorylate both Thr14 and Tyr15. Consequently, WEE1 acts as a molecular brake on DNA replication and mitotic entry, opposing CDC25 phosphatases and preventing damaged or incompletely replicated chromosomes from entering mitosis. (zhang2025targetingwee1kinase pages 1-2, mcgowan1995cellcycleregulation pages 1-2, zhu2017structuralbasisof pages 1-2, mcgowan1995cellcycleregulation pages 6-8)

Clinically, WEE1 is being exploited as an oncology target. Inhibitors such as adavosertib/AZD1775 remove the CDK brake, causing excessive replication-origin firing, replication stress, premature mitosis, and replication or mitotic catastrophe. Results remain context-dependent: selected uterine-serous and CCNE1-amplified cancers have shown activity, whereas SETD2-selected monotherapy and adavosertib–olaparib produced limited overall activity. WEE1 inhibition remains investigational rather than established standard-of-care. (zhang2024targetingwee1kinase pages 7-9, maldonado2024aphaseii pages 1-2, hamilton2024adavosertibincombination pages 1-2, NCT03253679 chunk 1)

## 1. Mandatory identity verification

### 1.1 Symbol, protein, and organism

The literature target matches the supplied identity: **human WEE1/Wee1A**, a WEE-family cell-cycle kinase. Early full-length cloning established endogenous human WEE1 as a 647-amino-acid protein; later structural work used a 646-residue full-length construct, a one-residue discrepancy likely reflecting construct or sequence-version conventions rather than a different protein. The endogenous protein migrated at approximately 94 kDa by SDS-PAGE despite a lower sequence-predicted mass. (mcgowan1995cellcycleregulation pages 2-3, mcgowan1995cellcycleregulation pages 3-4, zhu2017structuralbasisof pages 8-10)

No relevant ambiguity was found. Comparative human studies explicitly distinguish:

- **WEE1/Wee1A:** ubiquitously expressed somatic-cell regulator and the target discussed here.
- **WEE2/Wee1B:** germ-cell-specific or enriched, with prominent meiotic functions.
- **PKMYT1/Myt1:** a structurally distinct, dual-specificity kinase associated with the ER–Golgi system that phosphorylates CDK1 Thr14 as well as Tyr15. (zhu2017structuralbasisof pages 1-2)

Open Targets independently maps approved symbol **WEE1** to human gene **ENSG00000166483**, named “WEE1 G2 checkpoint kinase,” further supporting the identifier match. Its broad disease-association scores should not, however, be interpreted as evidence of a specific causal disease function without inspecting the underlying studies. (OpenTargets Search: -WEE1)

### 1.2 Family and domains

The protein contains an extensive N-terminal noncatalytic region and a C-terminal kinase domain. Structural experiments used human WEE1 residues **291–575** as the kinase-domain construct, consistent with the supplied protein-kinase, ATP-binding, kinase-like, and Ser/Thr-kinase active-site domain annotations. Although commonly described functionally as a tyrosine kinase because its defining substrate site is CDK Tyr15, WEE1 belongs to the eukaryotic protein-kinase superfamily and can undergo phosphorylation on serine, threonine, and tyrosine residues. (zhu2017structuralbasisof pages 2-5, zhu2017structuralbasisof pages 8-10, mcgowan1995cellcycleregulation pages 6-8)

The regulatory region is functionally important. Isolated bacterially expressed WEE1 kinase-domain constructs were catalytically inactive toward CDK1 Tyr15, whereas full-length WEE1 expressed in mammalian cells was active and contained numerous phosphorylation sites. Full-length WEE1 had approximately 30-fold greater specific activity than WEE2 and 10-fold greater activity than Myt1 in the reported assay. These findings indicate that phosphorylation state and regions outside the catalytic core regulate productive activity. (zhu2017structuralbasisof pages 2-5, zhu2017structuralbasisof pages 1-2)

| Aspect | Best-supported annotation | Evidence type |
|---|---|---|
| Identity | UniProt **P30291** corresponds to human **WEE1 (Wee1A)**, a 646–647-aa WEE-family kinase; this is distinct from germ-cell-specific WEE2/Wee1B and ER–Golgi-associated PKMYT1. (mcgowan1995cellcycleregulation pages 2-3, zhu2017structuralbasisof pages 1-2, zhu2017structuralbasisof pages 8-10) | Full-length cDNA/protein characterization; comparative biochemical and structural analysis |
| Architecture | WEE1 contains a large N-terminal noncatalytic/regulatory region and a C-terminal protein-kinase domain; an experimentally used kinase-domain construct spans approximately residues **291–575**. (zhu2017structuralbasisof pages 8-10, mcgowan1995cellcycleregulation pages 6-8) | Sequence analysis; recombinant constructs; crystallography |
| Direct reaction and substrates | WEE1 catalyzes ATP-dependent inhibitory phosphorylation of **CDK1 Tyr15** and regulates **CDK2 through Tyr15 phosphorylation**. Direct peptide assays showed that human WEE1 does **not** phosphorylate adjacent CDK1 Thr14; PKMYT1 can phosphorylate both sites. (welburn2007howtyrosine15 pages 1-1, zhang2025targetingwee1kinase pages 1-2, zhu2017structuralbasisof pages 1-2, mcgowan1995cellcycleregulation pages 6-8) | Immunodepletion and kinase assays; site-specific peptide assays; structural enzymology |
| Localization | Full-length WEE1 localized predominantly to the **nucleus** and was excluded from **nucleoli** in transfected HeLa cells; weak endogenous nuclear staining was also observed. (mcgowan1995cellcycleregulation pages 6-8) | Indirect immunofluorescence microscopy in human cells |
| Pathway role | WEE1 opposes CDC25-mediated dephosphorylation to restrain CDK1–cyclin B and set the **G2/M mitotic-entry switch**. Its inhibition of CDK2 also limits replication-origin firing and replication stress during **S phase**. (zhang2025targetingwee1kinase pages 1-2, mcgowan1995cellcycleregulation pages 1-2, mcgowan1995cellcycleregulation pages 8-9) | Human-cell biochemistry and synchronization studies; mechanistic reviews |
| Translational status | WEE1 inhibitors—including **adavosertib/AZD1775** and newer agents such as azenosertib—remain investigational; registered studies are predominantly phase I/II rather than routine clinical implementation. (zhang2025targetingwee1kinase pages 15-17, hamilton2024adavosertibincombination pages 1-2, NCT04590248 chunk 1, NCT03253679 chunk 1) | Clinical-trial publications and ClinicalTrials.gov records |
| Key clinical lesson | Activity is context- and biomarker-dependent: favorable signals have occurred in selected uterine-serous and CCNE1-amplified cancers, whereas SETD2-selected monotherapy and an adavosertib–olaparib trial showed limited activity. Hematologic and gastrointestinal toxicities are recurrent constraints; WEE1 inhibition is **not established standard-of-care**. (zhang2024targetingwee1kinase pages 7-9, maldonado2024aphaseii pages 4-5, maldonado2024aphaseii pages 1-2, hamilton2024adavosertibincombination pages 1-2) | Phase I/II efficacy and safety data; contemporary expert synthesis |


*Table: Concise evidence-based annotation of human WEE1 identity, biochemical function, localization, pathway placement, and translational status. The table distinguishes experimentally established molecular properties from current clinical evidence.*

## 2. Primary molecular function

### 2.1 Catalyzed reaction

The core reaction can be represented as:

**ATP + CDK1–cyclin B → ADP + CDK1–cyclin B–pTyr15**

An analogous inhibitory reaction occurs on **CDK2 Tyr15**. Phosphorylation suppresses CDK activity rather than activating the substrate. (zhang2025targetingwee1kinase pages 1-2, mcgowan1995cellcycleregulation pages 1-2, zhu2017structuralbasisof pages 1-2)

Direct human-cell evidence is strong. Immunodepletion experiments showed that WEE1 accounted for most measurable CDC2/CDK1-directed tyrosine-kinase activity in HeLa lysates. Full-length WEE1 and its earlier truncated construct phosphorylated CDK1-region peptide substrates exclusively at Tyr15; no Thr14 phosphorylation was detected. Thus, the most precise functional annotation is **CDK inhibitory Tyr15 kinase**, not a general Thr14/Tyr15 kinase. (mcgowan1995cellcycleregulation pages 1-2, mcgowan1995cellcycleregulation pages 3-4, mcgowan1995cellcycleregulation pages 6-8)

### 2.2 Substrate specificity

**Primary substrate:** CDK1 complexed with cyclin B, phosphorylated at Tyr15. This modification prevents activation of the mitotic CDK module and delays G2-to-M progression. (mcgowan1995cellcycleregulation pages 1-2, zhu2017structuralbasisof pages 1-2)

**Second major substrate:** CDK2 at Tyr15. This restrains CDK2-driven S-phase progression and excessive replication-origin firing. Current models therefore treat WEE1 as both a G2/M checkpoint kinase and an intra-S-phase replication regulator. (zhang2025targetingwee1kinase pages 1-2, maldonado2024aphaseii pages 1-2, hamilton2024adavosertibincombination pages 1-2)

**Specificity relative to PKMYT1:** WEE1 is predominantly Tyr15-directed; PKMYT1 phosphorylates CDK1 Thr14 and Tyr15 and is associated with the ER–Golgi compartment. WEE2 can also phosphorylate CDK1 Tyr15 but has a different expression pattern and physiological emphasis. (zhu2017structuralbasisof pages 1-2, mcgowan1995cellcycleregulation pages 6-8)

A reported non-CDK substrate is histone **H2B Tyr37**, proposed to suppress histone transcription in late S phase. This is biologically interesting but less securely established as the defining function than CDK1/2 regulation, and it should remain a secondary annotation. (zhu2017structuralbasisof pages 1-2)

### 2.3 How Tyr15 phosphorylation inhibits CDKs

Crystallographic and kinetic analysis of Tyr15-phosphorylated CDK2–cyclin A showed two coupled inhibitory effects: steric obstruction of peptide-substrate binding and stabilization of a nonproductive orientation of ATP’s terminal phosphate. Tyr15 phosphorylation did not appreciably change ATP affinity or abolish intrinsic ATPase activity, and the phosphorylated enzyme retained trace protein-kinase activity. This provides a structural explanation for how WEE1 can suppress CDK catalytic output without simply preventing ATP binding. (welburn2007howtyrosine15 pages 1-1)

## 3. Cellular localization

Human WEE1 acts principally in the **nucleus**. In HeLa cells, both full-length p94WEE1 and the earlier truncated construct localized exclusively to nuclei and were excluded from nucleoli; weak endogenous nuclear staining was also observed. This result was obtained by indirect immunofluorescence and is the most direct localization evidence in the retrieved literature. (mcgowan1995cellcycleregulation pages 6-8)

Nuclear localization is consistent with WEE1’s functions in controlling nuclear CDK activity, replication, DNA-damage responses, and mitotic commitment. Localization is also useful diagnostically for distinguishing WEE1 from PKMYT1, whose characteristic localization is the ER–Golgi complex. (zhu2017structuralbasisof pages 1-2, mcgowan1995cellcycleregulation pages 6-8)

## 4. Pathway placement and biological processes

### 4.1 The WEE1–CDC25–CDK1 mitotic-entry switch

During interphase, cyclin-B-bound CDK1 accumulates in an inhibited state bearing Tyr15 and, in mammals, often Thr14 phosphorylation. WEE1 maintains Tyr15 phosphorylation, whereas CDC25 phosphatases remove the inhibitory phosphates. The balance between these opposing enzymes determines when CDK1–cyclin B becomes active and mitosis begins. (mcgowan1995cellcycleregulation pages 1-2, mcgowan1995cellcycleregulation pages 8-9)

Human synchronization experiments found WEE1 activity relatively constant through most of interphase but sharply reduced during mitosis, reciprocal to CDK1–cyclin-B activity. WEE1 protein remained present, arguing against degradation as the primary acute switch. Instead, reactivation when phosphatase inhibition was removed indicated that mitotic WEE1 suppression depends on phosphorylation. Coordinated WEE1 inhibition and CDC25 activation create a reinforcing transition from low to high CDK1 activity. (mcgowan1995cellcycleregulation pages 4-5, mcgowan1995cellcycleregulation pages 5-6, mcgowan1995cellcycleregulation pages 6-8, mcgowan1995cellcycleregulation pages 8-9)

### 4.2 DNA-damage checkpoint signaling

Under DNA damage or replication stress, the **ATR–CHK1** axis promotes a CDK-inhibitory state involving WEE1. WEE1-mediated CDK1 Tyr15 phosphorylation delays mitosis, allowing repair before chromosome segregation. CDC25 reverses this state during recovery. Loss or inhibition of WEE1 activates CDK1 prematurely, producing chromosome damage, centromere fragmentation, aberrant mitosis, and mitotic catastrophe. (zhang2025targetingwee1kinase pages 1-2, maldonado2024aphaseii pages 1-2)

A frequently stated therapeutic model is that TP53-deficient cancers, lacking an effective G1 checkpoint, become unusually dependent on the S/G2 checkpoints. This is biologically plausible and supported in several model systems, but TP53 status alone has not proven a universally reliable clinical-response biomarker. Contemporary expert assessments increasingly favor direct replication-stress features—particularly Cyclin-E1/CDK2 activation—over a simple “p53-deficient equals WEE1-sensitive” rule. (zhang2024targetingwee1kinase pages 7-9, zhang2024targetingwee1kinase pages 6-7)

### 4.3 Intra-S-phase replication control

WEE1 inhibition releases CDK2 from Tyr15 restraint. Excess CDK2 activity increases or mistimes replication-origin firing, reduces replication-fork processivity, consumes replication resources, and causes single-stranded DNA accumulation, fork collapse, DNA breakage, and replication catastrophe. Thus, WEE1 is not merely a G2/M gatekeeper: it also protects ongoing DNA synthesis. (zhang2025targetingwee1kinase pages 1-2, khamidullina2024keyproteinsof pages 14-16, hamilton2024adavosertibincombination pages 1-2)

The SETD2/H3K36me3 model illustrates this mechanism. SETD2 loss reduces H3K36 trimethylation and RRM2 expression, thereby lowering dNTP pools. Preclinical work predicted that WEE1 inhibition would further reduce RRM2/dNTP availability and selectively abolish replication in SETD2-deficient cells. However, the corresponding 2024 clinical trial did not validate SETD2 mutation or H3K36me3 loss as a robust single-agent selection biomarker. (maldonado2024aphaseii pages 2-3, maldonado2024aphaseii pages 1-2)

### 4.4 Additional pathway connections

WEE1 inhibition can impair RAD51-associated homologous recombination and increases replication-stress and DNA-damage markers including γH2AX and phosphorylated RPA32. This provides a mechanistic rationale for combinations with platinum agents, gemcitabine, topoisomerase-I payloads, PARP inhibitors, radiation, or experimental RAD51-directed therapies. Such combinations intensify DNA lesions while removing the checkpoint time needed to repair them. (khamidullina2024keyproteinsof pages 14-16)

## 5. Recent developments, emphasizing 2023–2024

### 5.1 Replication stress as the central therapeutic concept

A January 2024 review framed WEE1 and PKMYT1 as checkpoint dependencies in cancers with high replication stress. WEE1 inhibition activates CDK2, accelerates cell-cycle progression, and promotes replication abnormalities and death. Candidate sensitizing contexts include CCNE1 or MYC amplification and deficiencies in other DNA-damage-response branches, although clinical validation remains incomplete. **Khamidullina et al., January 2024, DOI:** https://doi.org/10.3390/ijms25021263. (khamidullina2024keyproteinsof pages 14-16)

### 5.2 CCNE1/Cyclin-E1 as a leading biomarker

CCNE1 amplification or Cyclin-E1 overexpression drives CDK2 activity and intrinsic replication stress, creating a mechanistically coherent dependence on WEE1. A completed phase II registry study, **NCT03253679**, enrolled 31 patients with advanced refractory CCNE1-amplified solid tumors; the associated multicenter paper was published online December 5, 2022 and in print March 20, 2023. The registry defined CCNE1 amplification using high-copy thresholds and was updated with results in 2023. (NCT03253679 chunk 1, NCT03253679 chunk 2)

Preclinical 2023 work also found frequent CCNE1 co-amplification among ERBB2-amplified gastric, endometrioid, and ovarian-serous cancers—37%, 43%, and 41%, respectively—and reported synergy between adavosertib and trastuzumab deruxtecan in HER2-expressing, Cyclin-E-amplified models. This supports combination testing but is not yet evidence of routine patient benefit. **DiPeri et al., 2023, DOI:** https://doi.org/10.1158/1078-0432.CCR-23-0103. (kim2025cycline1cdk2activation pages 13-14)

### 5.3 More selective next-generation inhibitors

Because adavosertib has meaningful toxicity and imperfect kinome selectivity, development has shifted toward agents such as azenosertib and other newer WEE1 inhibitors. Early pharmacodynamic studies use decreased CDK1 Tyr15 phosphorylation in surrogate tissue as evidence of target engagement. These agents remain in early clinical development; reliable predictive biomarkers and improved therapeutic windows are unresolved priorities. (kim2025cycline1cdk2activation pages 13-14, zhang2025targetingwee1kinase pages 15-17)

An important experimental caution is that MK-1775/adavosertib was reported to inhibit PLK1 with potency comparable to WEE1 in kinome profiling. Results obtained solely with this compound should therefore not automatically be attributed to WEE1 without genetic confirmation or orthogonal selective inhibitors. **Zhu et al., published August 9, 2017, DOI:** https://doi.org/10.1021/acs.jmedchem.7b00996. (zhu2017structuralbasisof pages 2-5, zhu2017structuralbasisof pages 8-10)

## 6. Current applications and real-world implementation

### 6.1 Experimental and research applications

WEE1 inhibition is widely used experimentally to:

1. release CDK1 Tyr15 inhibition and test G2/M-checkpoint dependence;
2. activate CDK2 and model replication catastrophe;
3. sensitize cells to DNA-damaging chemotherapy or radiation;
4. test synthetic-lethal hypotheses involving CCNE1, SETD2/H3K36me3, homologous-recombination repair, or PARP-inhibitor resistance; and
5. measure pharmacodynamic target engagement through loss of phospho-CDK1 Tyr15. (khamidullina2024keyproteinsof pages 14-16, kim2025cycline1cdk2activation pages 13-14, maldonado2024aphaseii pages 2-3)

### 6.2 Clinical implementation status

There is no evidence in the retrieved sources that a WEE1 inhibitor is established standard treatment. Clinical use is through phase I/II trials, generally as monotherapy in molecularly selected tumors or in combinations with chemotherapy, PARP inhibition, immunotherapy, or radiation. (zhang2025targetingwee1kinase pages 15-17, hamilton2024adavosertibincombination pages 1-2, NCT04590248 chunk 1, NCT03253679 chunk 1)

ClinicalTrials.gov records illustrate the landscape:

- **NCT04590248/ADAGIO:** completed phase IIb, single-arm adavosertib study in recurrent or persistent uterine serous carcinoma; actual enrollment 109, completion February 7, 2023, with registry results first posted August 14, 2023. https://clinicaltrials.gov/study/NCT04590248 (NCT04590248 chunk 1, NCT04590248 chunk 2)
- **NCT03253679:** completed phase II study in CCNE1-amplified refractory solid tumors; actual enrollment 31 and completion October 31, 2022, with results posted in 2023. https://clinicaltrials.gov/study/NCT03253679 (NCT03253679 chunk 1)
- **NCT03284385:** phase II SETD2-deficient solid-tumor study; actual enrollment 18. The retrieved current registry marks it active but not recruiting, even though its stage-1 efficacy cohort and 2024 publication reported no objective responses. https://clinicaltrials.gov/study/NCT03284385 (maldonado2024aphaseii pages 1-2, NCT03284385 chunk 1)

## 7. Quantitative clinical evidence

### 7.1 Gynecologic malignancies

A June 2024 authoritative review summarized several informative trials:

- In platinum-resistant/refractory high-grade serous ovarian cancer, adavosertib plus gemcitabine enrolled **99 patients** and improved median PFS from **3.0 to 4.6 months** and median OS from **7.2 to 11.4 months**, but increased grade ≥3 neutropenia and thrombocytopenia.
- A multi-chemotherapy trial of **94 patients** recorded three complete and 27 partial responses. Carboplatin plus weekly adavosertib produced the highest reported response rate, **66.7%**, with **100% disease control** and median PFS of **12.0 months**, at the cost of substantial hematologic toxicity.
- In recurrent uterine serous carcinoma, a 34-patient study reported one complete and nine partial responses—an ORR of **29.4%**—with **47.1% six-month PFS** and a **nine-month median response duration**. (zhang2024targetingwee1kinase pages 7-9, maldonado2024aphaseii pages 5-6)

In an earlier TP53-mutant, taxane/platinum-resistant ovarian study, 24 patients were enrolled and 21 evaluable; the reported remission rate was **43%**, median PFS **5.3 months**, and median OS **12.6 months**. Grade ≥3 thrombocytopenia and neutropenia occurred in **48%** and **37%**, respectively. These results support biological activity but also show the dose-limiting importance of marrow toxicity. (zhang2024targetingwee1kinase pages 6-7)

### 7.2 2024 SETD2-selected phase II trial

Maldonado et al. reported **NCT03284385** in July 2024. Eighteen patients were enrolled, nine with non-clear-cell-RCC solid tumors and nine with clear-cell RCC. There were **no objective responses**, so both cohorts stopped after stage 1. Minor regressions occurred in **4/18 (22%)**, and stable disease was the best response in **10/18 (56%)**; three patients maintained stable disease for more than four months and one remained treated beyond 24 months. Median PFS was **1.43 months** in the other-solid-tumor cohort and **3.77 months** in clear-cell RCC. (maldonado2024aphaseii pages 4-5, maldonado2024aphaseii pages 1-2)

Common adverse events were nausea (**59%**), anemia (**41%**), diarrhea (**41%**), and neutropenia (**41%**); **50%** experienced a grade ≥3 adverse event. Six of eight evaluable tumors lost H3K36me3, yet no clear relationship emerged between this marker and regression or treatment duration. The investigators concluded that compelling SETD2 synthetic-lethality data did not translate into robust clinical tumor regression. **Published July 2024; DOI:** https://doi.org/10.1158/2767-9764.CRC-24-0213. (maldonado2024aphaseii pages 4-5, maldonado2024aphaseii pages 5-6, maldonado2024aphaseii pages 1-2)

### 7.3 2024 adavosertib–olaparib phase Ib trial

Hamilton et al. enrolled **130 patients**: 120 in dose finding and 10 in small-cell-lung-cancer expansion. The recommended phase II schedule was adavosertib 200 mg once daily on days 1–3 and 8–10 plus continuous olaparib 200 mg twice daily in 21-day cycles. In dose-finding part A, overall ORR was **14.8%** (95% CI 8.7–22.9). In SCLC expansion, ORR was **11.1%**, disease-control rate **22.2%**, and median PFS **1.5 months**. (hamilton2024adavosertibincombination pages 1-2)

At the selected bid-MTD and once-daily RP2D schedules, common treatment-related events included fatigue, diarrhea, appetite loss, nausea, and anemia. In the SCLC cohort, **88.9%** experienced treatment-related adverse events, including thrombocytopenia in **66.7%** and anemia in **55.6%**. The investigators judged toxicity manageable but antitumor activity limited. **Published online November 1, 2024; DOI:** https://doi.org/10.1007/s11523-024-01102-8; trial **NCT02511795**. (hamilton2024adavosertibincombination pages 4-5, hamilton2024adavosertibincombination pages 1-2)

## 8. Expert assessment

The convergent expert view is that WEE1 is a well-validated cell-cycle and replication-stress target, but not yet a clinically validated target across cancers. Its molecular function is much more certain than its optimal therapeutic use. The strongest current rationale is to select tumors with measurable Cyclin-E1/CDK2 activation or another demonstrable replication-stress dependency and to use schedules or combinations that preserve antitumor stress while limiting marrow and gastrointestinal toxicity. (khamidullina2024keyproteinsof pages 14-16, kim2025cycline1cdk2activation pages 13-14, zhang2025targetingwee1kinase pages 15-17)

Three cautions are important:

1. **Biomarker hypotheses require clinical validation.** SETD2/H3K36me3 deficiency was compelling preclinically but failed to predict objective responses in the 2024 phase II study. (maldonado2024aphaseii pages 4-5, maldonado2024aphaseii pages 1-2)
2. **TP53 mutation is not sufficient by itself.** It may increase checkpoint dependence, but responses are heterogeneous and other replication-stress features appear important. (zhang2024targetingwee1kinase pages 7-9, zhang2024targetingwee1kinase pages 6-7)
3. **Chemical selectivity matters.** Adavosertib’s PLK1 activity complicates mechanistic interpretation, making genetic WEE1 perturbation and newer selective inhibitors valuable controls. (zhu2017structuralbasisof pages 2-5, zhu2017structuralbasisof pages 8-10)

## 9. Recommended functional annotation

**WEE1 is a predominantly nuclear, cell-cycle-regulated inhibitory CDK tyrosine kinase. It transfers phosphate from ATP to Tyr15 of CDK1–cyclin B and CDK2-containing complexes, suppressing CDK catalytic activity. Through CDK1 it delays mitotic entry and enforces the G2 DNA-damage checkpoint; through CDK2 it limits replication-origin firing and replication stress during S phase. WEE1 activity is high through interphase and suppressed during mitosis by a phosphorylation-dependent mechanism. Its inhibition can induce replication catastrophe and premature, damage-laden mitosis.** (zhang2025targetingwee1kinase pages 1-2, mcgowan1995cellcycleregulation pages 1-2, mcgowan1995cellcycleregulation pages 5-6, mcgowan1995cellcycleregulation pages 6-8, mcgowan1995cellcycleregulation pages 8-9)

Evidence confidence is **high** for identity, nuclear localization, CDK1 Tyr15 specificity, and G2/M regulation; **moderate-to-high** for CDK2/intra-S-phase control; and **context-dependent** for proposed cancer biomarkers and therapeutic efficacy.

References

1. (mcgowan1995cellcycleregulation pages 2-3): C.H. McGowan and P. Russell. Cell cycle regulation of human wee1. The EMBO Journal, 14:2166-2175, May 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb07210.x, doi:10.1002/j.1460-2075.1995.tb07210.x. This article has 422 citations.

2. (zhu2017structuralbasisof pages 1-2): Jin-Yi Zhu, Rebecca A. Cuellar, Norbert Berndt, Hee Eun Lee, Sanne H. Olesen, Mathew P. Martin, Jeffrey T. Jensen, Gunda I. Georg, and Ernst Schönbrunn. Structural basis of wee kinases functionality and inactivation by diverse small molecule inhibitors. Journal of medicinal chemistry, 60 18:7863-7875, Sep 2017. URL: https://doi.org/10.1021/acs.jmedchem.7b00996, doi:10.1021/acs.jmedchem.7b00996. This article has 118 citations and is from a highest quality peer-reviewed journal.

3. (zhu2017structuralbasisof pages 8-10): Jin-Yi Zhu, Rebecca A. Cuellar, Norbert Berndt, Hee Eun Lee, Sanne H. Olesen, Mathew P. Martin, Jeffrey T. Jensen, Gunda I. Georg, and Ernst Schönbrunn. Structural basis of wee kinases functionality and inactivation by diverse small molecule inhibitors. Journal of medicinal chemistry, 60 18:7863-7875, Sep 2017. URL: https://doi.org/10.1021/acs.jmedchem.7b00996, doi:10.1021/acs.jmedchem.7b00996. This article has 118 citations and is from a highest quality peer-reviewed journal.

4. (mcgowan1995cellcycleregulation pages 6-8): C.H. McGowan and P. Russell. Cell cycle regulation of human wee1. The EMBO Journal, 14:2166-2175, May 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb07210.x, doi:10.1002/j.1460-2075.1995.tb07210.x. This article has 422 citations.

5. (zhang2025targetingwee1kinase pages 1-2): Zhao Zhang, Ritika Harish, Naveed Elahi, Sawanjit Saini, Aamir Telia, Manjit Kundlas, Allexes Koroleva, Israel N. Umoh, Manpreet Lota, Meha Bilkhu, Aladdin Kawaiah, Manogna R. Allala, Armelle Leukeu, Emmanuel Nebuwa, Nadiya Sharifi, Anthony W. Ashton, Xuanmao Jiao, and Richard G. Pestell. Targeting wee1 kinase for breast cancer therapeutics: an update. Jun 2025. URL: https://doi.org/10.3390/ijms26125701, doi:10.3390/ijms26125701. This article has 11 citations.

6. (mcgowan1995cellcycleregulation pages 1-2): C.H. McGowan and P. Russell. Cell cycle regulation of human wee1. The EMBO Journal, 14:2166-2175, May 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb07210.x, doi:10.1002/j.1460-2075.1995.tb07210.x. This article has 422 citations.

7. (zhang2024targetingwee1kinase pages 7-9): Wenhao Zhang, Qingli Li, and Rutie Yin. Targeting wee1 kinase in gynecological malignancies. Drug Design, Development and Therapy, 18:2449-2460, Jun 2024. URL: https://doi.org/10.2147/dddt.s462056, doi:10.2147/dddt.s462056. This article has 19 citations.

8. (maldonado2024aphaseii pages 1-2): Edward Maldonado, W. Rathmell, G. I. Shapiro, N. Takebe, J. Rodon, D. Mahalingam, N. Trikalinos, Arash R Kaleblasty, M. Parikh, S. Boerner, Celene Balido, Gregor Krings, T. Burns, E. Bergsland, P. Munster, A. Ashworth, Patricia M. LoRusso, and Rahul R. Aggarwal. A phase ii trial of the wee1 inhibitor adavosertib in setd2-altered advanced solid tumor malignancies (nci 10170). Cancer Research Communications, 4:1793-1801, Jun 2024. URL: https://doi.org/10.1158/2767-9764.crc-24-0213, doi:10.1158/2767-9764.crc-24-0213. This article has 12 citations and is from a peer-reviewed journal.

9. (hamilton2024adavosertibincombination pages 1-2): Erika P. Hamilton, Gerald S. Falchook, Judy S. Wang, Siqing Fu, Amit M. Oza, Esteban Rodrigo Imedio, Sanjeev Kumar, Lone Ottesen, Ganesh M. Mugundu, Elza C. de Bruin, Mark J. O’Connor, Suzanne F. Jones, David R. Spigel, and Bob T. Li. Adavosertib in combination with olaparib in patients with refractory solid tumors: an open-label, dose-finding, and dose-expansion phase ib trial. Targeted Oncology, 19:879-892, Nov 2024. URL: https://doi.org/10.1007/s11523-024-01102-8, doi:10.1007/s11523-024-01102-8. This article has 18 citations and is from a peer-reviewed journal.

10. (NCT03253679 chunk 1):  AZD1775 in Treating Patients With Advanced Refractory Solid Tumors With CCNE1 Amplification. National Cancer Institute (NCI). 2019. ClinicalTrials.gov Identifier: NCT03253679

11. (mcgowan1995cellcycleregulation pages 3-4): C.H. McGowan and P. Russell. Cell cycle regulation of human wee1. The EMBO Journal, 14:2166-2175, May 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb07210.x, doi:10.1002/j.1460-2075.1995.tb07210.x. This article has 422 citations.

12. (OpenTargets Search: -WEE1): Open Targets Query (-WEE1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

13. (zhu2017structuralbasisof pages 2-5): Jin-Yi Zhu, Rebecca A. Cuellar, Norbert Berndt, Hee Eun Lee, Sanne H. Olesen, Mathew P. Martin, Jeffrey T. Jensen, Gunda I. Georg, and Ernst Schönbrunn. Structural basis of wee kinases functionality and inactivation by diverse small molecule inhibitors. Journal of medicinal chemistry, 60 18:7863-7875, Sep 2017. URL: https://doi.org/10.1021/acs.jmedchem.7b00996, doi:10.1021/acs.jmedchem.7b00996. This article has 118 citations and is from a highest quality peer-reviewed journal.

14. (welburn2007howtyrosine15 pages 1-1): Julie P.I. Welburn, Julie A. Tucker, Tim Johnson, Lisa Lindert, Marc Morgan, Antony Willis, Martin E.M. Noble, and Jane A. Endicott. How tyrosine 15 phosphorylation inhibits the activity of cyclin-dependent kinase 2-cyclin a*. Journal of Biological Chemistry, 282:3173-3181, Feb 2007. URL: https://doi.org/10.1074/jbc.m609151200, doi:10.1074/jbc.m609151200. This article has 148 citations and is from a domain leading peer-reviewed journal.

15. (mcgowan1995cellcycleregulation pages 8-9): C.H. McGowan and P. Russell. Cell cycle regulation of human wee1. The EMBO Journal, 14:2166-2175, May 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb07210.x, doi:10.1002/j.1460-2075.1995.tb07210.x. This article has 422 citations.

16. (zhang2025targetingwee1kinase pages 15-17): Zhao Zhang, Ritika Harish, Naveed Elahi, Sawanjit Saini, Aamir Telia, Manjit Kundlas, Allexes Koroleva, Israel N. Umoh, Manpreet Lota, Meha Bilkhu, Aladdin Kawaiah, Manogna R. Allala, Armelle Leukeu, Emmanuel Nebuwa, Nadiya Sharifi, Anthony W. Ashton, Xuanmao Jiao, and Richard G. Pestell. Targeting wee1 kinase for breast cancer therapeutics: an update. Jun 2025. URL: https://doi.org/10.3390/ijms26125701, doi:10.3390/ijms26125701. This article has 11 citations.

17. (NCT04590248 chunk 1):  A Study of Adavosertib as Treatment for Uterine Serous Carcinoma. AstraZeneca. 2020. ClinicalTrials.gov Identifier: NCT04590248

18. (maldonado2024aphaseii pages 4-5): Edward Maldonado, W. Rathmell, G. I. Shapiro, N. Takebe, J. Rodon, D. Mahalingam, N. Trikalinos, Arash R Kaleblasty, M. Parikh, S. Boerner, Celene Balido, Gregor Krings, T. Burns, E. Bergsland, P. Munster, A. Ashworth, Patricia M. LoRusso, and Rahul R. Aggarwal. A phase ii trial of the wee1 inhibitor adavosertib in setd2-altered advanced solid tumor malignancies (nci 10170). Cancer Research Communications, 4:1793-1801, Jun 2024. URL: https://doi.org/10.1158/2767-9764.crc-24-0213, doi:10.1158/2767-9764.crc-24-0213. This article has 12 citations and is from a peer-reviewed journal.

19. (mcgowan1995cellcycleregulation pages 4-5): C.H. McGowan and P. Russell. Cell cycle regulation of human wee1. The EMBO Journal, 14:2166-2175, May 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb07210.x, doi:10.1002/j.1460-2075.1995.tb07210.x. This article has 422 citations.

20. (mcgowan1995cellcycleregulation pages 5-6): C.H. McGowan and P. Russell. Cell cycle regulation of human wee1. The EMBO Journal, 14:2166-2175, May 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb07210.x, doi:10.1002/j.1460-2075.1995.tb07210.x. This article has 422 citations.

21. (zhang2024targetingwee1kinase pages 6-7): Wenhao Zhang, Qingli Li, and Rutie Yin. Targeting wee1 kinase in gynecological malignancies. Drug Design, Development and Therapy, 18:2449-2460, Jun 2024. URL: https://doi.org/10.2147/dddt.s462056, doi:10.2147/dddt.s462056. This article has 19 citations.

22. (khamidullina2024keyproteinsof pages 14-16): Alvina I. Khamidullina, Yaroslav E. Abramenko, Alexandra V. Bruter, and Victor V. Tatarskiy. Key proteins of replication stress response and cell cycle control as cancer therapy targets. Jan 2024. URL: https://doi.org/10.3390/ijms25021263, doi:10.3390/ijms25021263. This article has 78 citations.

23. (maldonado2024aphaseii pages 2-3): Edward Maldonado, W. Rathmell, G. I. Shapiro, N. Takebe, J. Rodon, D. Mahalingam, N. Trikalinos, Arash R Kaleblasty, M. Parikh, S. Boerner, Celene Balido, Gregor Krings, T. Burns, E. Bergsland, P. Munster, A. Ashworth, Patricia M. LoRusso, and Rahul R. Aggarwal. A phase ii trial of the wee1 inhibitor adavosertib in setd2-altered advanced solid tumor malignancies (nci 10170). Cancer Research Communications, 4:1793-1801, Jun 2024. URL: https://doi.org/10.1158/2767-9764.crc-24-0213, doi:10.1158/2767-9764.crc-24-0213. This article has 12 citations and is from a peer-reviewed journal.

24. (NCT03253679 chunk 2):  AZD1775 in Treating Patients With Advanced Refractory Solid Tumors With CCNE1 Amplification. National Cancer Institute (NCI). 2019. ClinicalTrials.gov Identifier: NCT03253679

25. (kim2025cycline1cdk2activation pages 13-14): Daehwan Kim, Heekyung Chung, Wen Liu, Kangjin Jeong, Tugba Y. Ozmen, Furkan Ozmen, Matthew J. Rames, Sangyub Kim, Xiao Guo, Nathan Jameson, Petrus R. de Jong, Steven Yea, Laurie Harford, Jiali Li, Cara A. Mathews, Deborah B. Doroshow, Vincent J. Charles, Doris Kim, Kimberlee Fischer, Ahmed A. Samatar, Adrian Jubb, Kevin D. Bunker, Kimberly Blackwell, Fiona Simpkins, Funda Meric-Bernstam, Gordon B. Mills, Olivier Harismendy, Jianhui Ma, and Mark R. Lackner. Cyclin e1/cdk2 activation defines a key vulnerability to wee1 kinase inhibition in gynecological cancers. NPJ Precision Oncology, Jan 2025. URL: https://doi.org/10.1038/s41698-024-00787-4, doi:10.1038/s41698-024-00787-4. This article has 25 citations and is from a peer-reviewed journal.

26. (NCT04590248 chunk 2):  A Study of Adavosertib as Treatment for Uterine Serous Carcinoma. AstraZeneca. 2020. ClinicalTrials.gov Identifier: NCT04590248

27. (NCT03284385 chunk 1):  Testing AZD1775 in Advanced Solid Tumors That Have a Mutation Called SETD2. National Cancer Institute (NCI). 2019. ClinicalTrials.gov Identifier: NCT03284385

28. (maldonado2024aphaseii pages 5-6): Edward Maldonado, W. Rathmell, G. I. Shapiro, N. Takebe, J. Rodon, D. Mahalingam, N. Trikalinos, Arash R Kaleblasty, M. Parikh, S. Boerner, Celene Balido, Gregor Krings, T. Burns, E. Bergsland, P. Munster, A. Ashworth, Patricia M. LoRusso, and Rahul R. Aggarwal. A phase ii trial of the wee1 inhibitor adavosertib in setd2-altered advanced solid tumor malignancies (nci 10170). Cancer Research Communications, 4:1793-1801, Jun 2024. URL: https://doi.org/10.1158/2767-9764.crc-24-0213, doi:10.1158/2767-9764.crc-24-0213. This article has 12 citations and is from a peer-reviewed journal.

29. (hamilton2024adavosertibincombination pages 4-5): Erika P. Hamilton, Gerald S. Falchook, Judy S. Wang, Siqing Fu, Amit M. Oza, Esteban Rodrigo Imedio, Sanjeev Kumar, Lone Ottesen, Ganesh M. Mugundu, Elza C. de Bruin, Mark J. O’Connor, Suzanne F. Jones, David R. Spigel, and Bob T. Li. Adavosertib in combination with olaparib in patients with refractory solid tumors: an open-label, dose-finding, and dose-expansion phase ib trial. Targeted Oncology, 19:879-892, Nov 2024. URL: https://doi.org/10.1007/s11523-024-01102-8, doi:10.1007/s11523-024-01102-8. This article has 18 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](WEE1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. zhu2017structuralbasisof pages 1-2
2. mcgowan1995cellcycleregulation pages 6-8
3. khamidullina2024keyproteinsof pages 14-16
4. hamilton2024adavosertibincombination pages 1-2
5. mcgowan1995cellcycleregulation pages 2-3
6. zhu2017structuralbasisof pages 8-10
7. mcgowan1995cellcycleregulation pages 1-2
8. maldonado2024aphaseii pages 1-2
9. mcgowan1995cellcycleregulation pages 3-4
10. zhu2017structuralbasisof pages 2-5
11. mcgowan1995cellcycleregulation pages 8-9
12. maldonado2024aphaseii pages 4-5
13. mcgowan1995cellcycleregulation pages 4-5
14. mcgowan1995cellcycleregulation pages 5-6
15. maldonado2024aphaseii pages 2-3
16. maldonado2024aphaseii pages 5-6
17. hamilton2024adavosertibincombination pages 4-5
18. https://doi.org/10.3390/ijms25021263.
19. https://doi.org/10.1158/1078-0432.CCR-23-0103.
20. https://doi.org/10.1021/acs.jmedchem.7b00996.
21. https://clinicaltrials.gov/study/NCT04590248
22. https://clinicaltrials.gov/study/NCT03253679
23. https://clinicaltrials.gov/study/NCT03284385
24. https://doi.org/10.1158/2767-9764.CRC-24-0213.
25. https://doi.org/10.1007/s11523-024-01102-8;
26. https://doi.org/10.1002/j.1460-2075.1995.tb07210.x,
27. https://doi.org/10.1021/acs.jmedchem.7b00996,
28. https://doi.org/10.3390/ijms26125701,
29. https://doi.org/10.2147/dddt.s462056,
30. https://doi.org/10.1158/2767-9764.crc-24-0213,
31. https://doi.org/10.1007/s11523-024-01102-8,
32. https://doi.org/10.1074/jbc.m609151200,
33. https://doi.org/10.3390/ijms25021263,
34. https://doi.org/10.1038/s41698-024-00787-4,