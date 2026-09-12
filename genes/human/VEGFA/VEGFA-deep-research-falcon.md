---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-30T02:37:26.826696'
end_time: '2026-05-30T02:46:26.729163'
duration_seconds: 539.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: VEGFA
  gene_symbol: VEGFA
  uniprot_accession: P15692
  protein_description: 'RecName: Full=Vascular endothelial growth factor A, long form;
    Short=L-VEGF {ECO:0000303|PubMed:11731620, ECO:0000303|PubMed:35455969}; AltName:
    Full=Vascular permeability factor; Short=VPF; Contains: RecName: Full=N-VEGF {ECO:0000303|PubMed:35455969};
    Contains: RecName: Full=VEGFA {ECO:0000303|PubMed:35455969}; Flags: Precursor;'
  gene_info: Name=VEGFA; Synonyms=VEGF;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the PDGF/VEGF growth factor family.
  protein_domains: Cystine-knot_cytokine. (IPR029034); PD_growth_factor_CS. (IPR023581);
    PDGF/VEGF_dom. (IPR000072); PDGF/VEGF_growth_factor. (IPR050507); VEGF_C. (IPR027928)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: VEGFA-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P15692
- **Protein Description:** RecName: Full=Vascular endothelial growth factor A, long form; Short=L-VEGF {ECO:0000303|PubMed:11731620, ECO:0000303|PubMed:35455969}; AltName: Full=Vascular permeability factor; Short=VPF; Contains: RecName: Full=N-VEGF {ECO:0000303|PubMed:35455969}; Contains: RecName: Full=VEGFA {ECO:0000303|PubMed:35455969}; Flags: Precursor;
- **Gene Information:** Name=VEGFA; Synonyms=VEGF;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PDGF/VEGF growth factor family.
- **Key Domains:** Cystine-knot_cytokine. (IPR029034); PD_growth_factor_CS. (IPR023581); PDGF/VEGF_dom. (IPR000072); PDGF/VEGF_growth_factor. (IPR050507); VEGF_C. (IPR027928)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VEGFA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VEGFA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VEGFA** (gene ID: VEGFA, UniProt: P15692) in human.

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
- **UniProt Accession:** P15692
- **Protein Description:** RecName: Full=Vascular endothelial growth factor A, long form; Short=L-VEGF {ECO:0000303|PubMed:11731620, ECO:0000303|PubMed:35455969}; AltName: Full=Vascular permeability factor; Short=VPF; Contains: RecName: Full=N-VEGF {ECO:0000303|PubMed:35455969}; Contains: RecName: Full=VEGFA {ECO:0000303|PubMed:35455969}; Flags: Precursor;
- **Gene Information:** Name=VEGFA; Synonyms=VEGF;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PDGF/VEGF growth factor family.
- **Key Domains:** Cystine-knot_cytokine. (IPR029034); PD_growth_factor_CS. (IPR023581); PDGF/VEGF_dom. (IPR000072); PDGF/VEGF_growth_factor. (IPR050507); VEGF_C. (IPR027928)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VEGFA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VEGFA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VEGFA** (gene ID: VEGFA, UniProt: P15692) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Human **VEGFA** (UniProt P15692) Functional Annotation and Translation

**Target verification (mandatory):** UniProt accession **P15692** corresponds to **human VEGFA (vascular endothelial growth factor A; VEGF-A)**, a member of the **PDGF/VEGF growth factor family** and the prototypic VEGF ligand driving angiogenesis through VEGF receptors. VEGFA biology includes (i) **secreted VEGF-A isoforms** produced by alternative splicing, and (ii) a hypoxia-associated **non-canonical long form (L-VEGF)** that can be proteolytically processed into a **secreted VEGF-A** fragment plus a distinct **nuclear N-terminal fragment (N-VEGF)**. (perezgutierrez2023biologyandtherapeutic pages 1-3, katsman2022nvegftheautoregulatory pages 1-3)

---

## 1) Key concepts, definitions, and current understanding

### 1.1 Core definition and primary function
**VEGF-A** is a **secreted dimeric growth factor** whose primary physiological role is to **activate endothelial cells** to support **vasculogenesis/angiogenesis** (development and remodeling of blood vessels) and to regulate vascular permeability. Mechanistically, VEGF-A ligands signal mainly through receptor tyrosine kinases **VEGFR1 (FLT1)** and **VEGFR2 (KDR/FLK1)**, with VEGFR2 functioning as the main pro-angiogenic signaling receptor. (perezgutierrez2023biologyandtherapeutic pages 1-3, perezgutierrez2023biologyandtherapeutic pages 5-6)

A key concept in VEGFA functional annotation is that it is not a single molecular species: **alternative splicing, extracellular processing, and even non-canonical translation** generate **forms with different diffusion/ECM retention properties and potentially different biological outputs**. (perezgutierrez2023biologyandtherapeutic pages 1-3, perezgutierrez2023biologyandtherapeutic pages 17-17)

### 1.2 Isoforms and processed products (secreted VEGF-A and L-VEGF/N-VEGF axis)
**Alternative splicing (canonical secreted isoforms):** VEGFA is encoded by a single **8-exon gene** that yields multiple secreted isoforms, classically including **VEGF121, VEGF165, VEGF189, VEGF206**. Isoform-specific inclusion of heparan-binding features drives different degrees of **extracellular matrix (ECM)/heparan sulfate proteoglycan (HSPG)** binding versus diffusibility. (perezgutierrez2023biologyandtherapeutic pages 1-3, perezgutierrez2023biologyandtherapeutic pages 5-6)

- **VEGF121** is described as **freely diffusible**. (perezgutierrez2023biologyandtherapeutic pages 5-6)
- **VEGF165** is **partly diffusible and partly HSPG-bound**, and ~half of secreted VEGF165 is diffusible while the remainder is HSPG-bound. (perezgutierrez2023biologyandtherapeutic pages 1-3)
- **Longer isoforms (e.g., VEGF189/206)** are largely **sequestered in the ECM** via heparin-binding regions. (perezgutierrez2023biologyandtherapeutic pages 5-6)

**Proteolytic processing (shorter bioactive forms):** VEGFA isoforms can be proteolytically processed into shorter fragments (for example **VEGF110/VEGF113**), contributing to control of VEGFA **bioavailability** and vascular patterning. (perezgutierrez2023biologyandtherapeutic pages 1-3, perezgutierrez2023biologyandtherapeutic pages 17-17)

**Alternative splice-forms with debated inhibitory biology:** So-called **VEGFxxxb** transcripts (e.g., **VEGF165b**) have been discussed as anti-angiogenic competitors, but an authoritative 2023 review emphasizes that such variants are better regarded as **weak agonists rather than antagonists**, and their endogenous existence/importance remains debated. (perezgutierrez2023biologyandtherapeutic pages 15-16, perezgutierrez2023biologyandtherapeutic pages 17-17)

**Non-canonical translation and proteolytic processing (L-VEGF → N-VEGF + VEGF-A):** Under hypoxia, a **long VEGF-A isoform (“L-VEGF”)** can be translated from a **non-canonical upstream CUG start codon**, adding an N-terminal extension. L-VEGF can then be proteolytically cleaved upstream of the canonical VEGF-A start to produce two products: **(i) secreted VEGF-A**, and **(ii) an N-terminal fragment “N-VEGF” that can translocate to the nucleus**. (katsman2022nvegftheautoregulatory pages 1-3, katsman2022nvegftheautoregulatory pages 10-13)

### 1.3 Receptors/co-receptors and downstream signaling pathways
**Receptors/co-receptors:** VEGF-A binds VEGF receptors **VEGFR1 and VEGFR2** and co-receptors **neuropilin-1 (NRP1) and neuropilin-2 (NRP2)**. Ligand binding triggers receptor **dimerization and transphosphorylation**. (perezgutierrez2023biologyandtherapeutic pages 5-6)

**VEGFR2 (KDR/FLK1) signaling outputs:** VEGFR2 activation engages multiple canonical pathways:
- **PLCγ → PKC → ERK1/2**, associated with endothelial proliferation, migration, and broader endothelial homeostasis programs (including pro-angiogenic responses). (perezgutierrez2023biologyandtherapeutic pages 5-6)
- **PI3K → AKT**, supporting survival and contributing to permeability regulation. (perezgutierrez2023biologyandtherapeutic pages 5-6)
- **FAK signaling**, linked to ECM adhesion and vascular permeability. (perezgutierrez2023biologyandtherapeutic pages 5-6)

**VEGFR1 (FLT1) as regulator/decoy:** VEGFR1 can act as a **decoy receptor** limiting the amount of VEGF-A available to activate VEGFR2 in physiological contexts, and is generally characterized by weaker downstream activation (for example limited PLCγ–PKC–MAPK activation). (li2025advancesinthe pages 1-2, perezgutierrez2023biologyandtherapeutic pages 5-6)

### 1.4 Regulation of VEGFA expression (hypoxia/HIF axis)
**Hypoxia-dependent transcription:** VEGFA is a canonical hypoxia-inducible gene regulated by **HIF1α/HIF2α** binding to a conserved hypoxia response element, and constitutive HIF stabilization (e.g., via loss of VHL function) can drive VEGFA upregulation even in normoxia. (perezgutierrez2023biologyandtherapeutic pages 5-6)

**HIF-independent mechanisms:** Hypoxic regulation can also occur through HIF-independent routes (for example KRAS-mediated mechanisms), and PI3K/AKT is implicated in hypoxia-induced VEGF expression in some contexts. (perezgutierrez2023biologyandtherapeutic pages 5-6)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 2023 authoritative synthesis: VEGFA isoform complexity + proteolysis + translation readthrough debates
A highly cited 2023 *Nature Reviews Molecular Cell Biology* review emphasizes that VEGFA signaling should be understood as a system controlled by **alternative splicing**, **proteolysis**, and additional mechanisms such as **translational readthrough**, and that isoform/processing diversity shapes VEGF potency, ECM interactions, and spatial patterning. (perezgutierrez2023biologyandtherapeutic pages 17-17, perezgutierrez2023biologyandtherapeutic pages 1-3)

This review also provides an expert perspective that proposed anti-angiogenic VEGFA splice variants (VEGFxxxb) are more consistent with **weak agonism** than antagonism and highlights ongoing debate around endogenous inhibitory isoforms, which is important when interpreting isoform-specific experiments or proposed isoform-specific therapeutics. (perezgutierrez2023biologyandtherapeutic pages 15-16, perezgutierrez2023biologyandtherapeutic pages 17-17)

### 2.2 2024 real-world pharmacovigilance: ocular adverse event reporting patterns for anti-VEGF drugs
A 2024 analysis using WHO’s VigiAccess/VigiBase spontaneous reporting data (retrieved through Jan 28, 2024) compiled **57,779** adverse-event reports for four commonly used anti-VEGF drugs for wet AMD: **ranibizumab (24,338), aflibercept (28,524), brolucizumab (4,065), faricimab (852)**. (li2024arealworlddata pages 2-4)

The most common system-organ-class categories were **eye disorders (43.56%)**, **general disorders/administration site conditions (34.47%)**, **injury/poisoning/procedural complications (13.36%)**, **infections/infestations (11.61%)**, and **nervous system disorders (9.99%)**, and reports were disproportionately recorded in older patients (highest in >75 years) and more frequently in females (67.83%). (li2024arealworlddata pages 1-2, li2024arealworlddata pages 4-5)

*Interpretation note:* These are **spontaneous reporting volumes**, not incidence rates, and are influenced by drug market duration and reporting behaviors. (li2024arealworlddata pages 2-4)

### 2.3 Emerging durable suppression strategies: gene therapy encoding anti-VEGF biologics (ClinicalTrials.gov)
A major translational development is **AAV-based ocular gene therapy** aiming to convert the eye into a long-term producer of anti-VEGF biologics, potentially reducing injection burden.

ClinicalTrials.gov records describe **ABBV-RGX-314 (RGX-314; surabgene lomparvovec)** as an AAV8 vector encoding an **anti-VEGF Fab** intended to provide sustained intraocular anti-VEGF expression after a single administration. (NCT03066258 chunk 1, NCT04704921 chunk 1)

Key registered trials include:
- **NCT03066258** (Phase 1/2a; **subretinal**; completed; enrolled ~42) dose-escalation with safety focus and follow-up to 104 weeks. (NCT03066258 chunk 1)
- **NCT04514653** (Phase 2; **suprachoroidal**; active not recruiting; enrolled 146) randomized dose-escalation versus ranibizumab, with BCVA and safety endpoints. (NCT04514653 chunk 1)
- **NCT04704921** (Phase 2b/3 pivotal; **subretinal**; active not recruiting; enrolled 671) comparing two RGX-314 dose levels to monthly ranibizumab; primary endpoint BCVA change at Week 54. (NCT04704921 chunk 1)
- **NCT05407636** (Phase 3; **subretinal**; recruiting; planned enrollment 714) comparing two RGX-314 dose levels to aflibercept; primary endpoint BCVA change at Week 54. (NCT05407636 chunk 1)

---

## 3) Localization: where VEGFA functions in/around the cell

### 3.1 Secreted VEGF-A: extracellular ligand with isoform-dependent matrix binding
Canonical VEGF-A isoforms are **secreted** and act predominantly in the **extracellular space** to activate VEGFRs on endothelial cells. A key localization principle is **bioavailability**:
- Some isoforms (e.g., VEGF121) are more diffusible.
- Others (e.g., VEGF189/206) are strongly ECM/HSPG-associated.
This shapes signaling gradients and patterning in tissues. (perezgutierrez2023biologyandtherapeutic pages 5-6, perezgutierrez2023biologyandtherapeutic pages 1-3)

### 3.2 L-VEGF/N-VEGF: intracellular processing and nuclear function
In the L-VEGF axis, VEGFA biology includes an intracellular/nuclear arm:
- L-VEGF is generated via **non-canonical CUG translation** under hypoxia and cleaved into secreted VEGF plus **N-VEGF**. (katsman2022nvegftheautoregulatory pages 1-3)
- **N-VEGF** is **retained intracellularly** and can **translocate to the nucleus**. (katsman2022nvegftheautoregulatory pages 1-3)

Primary experimental evidence shows that forcing N-VEGF into the nucleus (e.g., via NLS fusion) is sufficient to induce transcriptional programs including **Hif1α** and **VEGF-A isoforms** under normoxia, and that **genetic deletion** of N-VEGF changes a substantial fraction of the hypoxia-responsive transcriptome and increases susceptibility to hypoxia-associated apoptosis. (katsman2022nvegftheautoregulatory pages 6-7, katsman2022nvegftheautoregulatory pages 7-10)

---

## 4) Pathway context: biological processes and expert mechanistic synthesis

### 4.1 Angiogenesis, endothelial survival, and permeability as primary pathway-level roles
VEGF-A–VEGFR2 signaling integrates multiple endothelial functions, including **proliferation/migration** (PLCγ–PKC–ERK), **survival** (PI3K–AKT), and **adhesion/permeability** (FAK-related signaling), providing a mechanistic explanation for why VEGFA is both a developmental angiogenesis factor and a mediator of pathological neovascularization and edema. (perezgutierrez2023biologyandtherapeutic pages 5-6)

### 4.2 Expert opinion (authoritative review perspective)
The 2023 expert review by Pérez-Gutiérrez and Ferrara frames VEGFA as a pathway essential not only for disease angiogenesis but also for **adult organ homeostasis**, with clinical manipulation requiring careful balancing due to potential harms of VEGF insufficiency or excess. (perezgutierrez2023biologyandtherapeutic pages 15-16)

---

## 5) Current applications and real-world implementations

### 5.1 Ophthalmology: anti-VEGF for neovascular eye diseases
Anti-VEGF therapy has “markedly improved vision” in neovascular eye disease, but practical limitations include short intraocular durability and need for repeated injections, incomplete response in some patients, and procedural risks. (li2025advancesinthe pages 1-2)

**Real-world effectiveness and treatment intensity (injection frequency and outcomes):** Registry-scale analyses of routine practice demonstrate lower gains than randomized trials, consistent with undertreatment/discontinuation patterns.

A large IRIS-based real-world dataset summarized in a 2025 analysis reports typical injection frequencies around **5.6 (year 1), 3.4 (year 2), 3.1 (year 3)**, with mean BCVA change of only **+0.7 letters at year 1** and decline by **−3.1 letters by year 3**, and **>1/3 discontinuing by year 3**. (gyenes2025evaluationofthe pages 7-9)

In a six-year IRIS cohort (reported as **254,655 eyes**), mean BCVA changed **+3.0 letters at year 1** but net **−4.6 letters at 6 years**; injections averaged **7.2 (year 1)**, **5.6 (year 2)**, and **~4.2–4.6 per year** in years 3–6. In that cohort **38.8%** had treatment cessation and **32.3%** changed treatment; **58.5%** lost ≥10 letters at least once, and **14.5%** had sustained poor vision after a median 3.4 years. (gyenes2025evaluationofthe pages 7-9)

**Discontinuation in multi-center practice:** In an Italian multi-center cohort of **2,302** treatment-naïve nAMD patients starting therapy 2019–2021, **28.5% (655)** discontinued, with the most common discontinuation category being **clinical decision** (with subcategories including no signs of exudation and poor/non-response), followed by continuation elsewhere, death, and patient choice. (borrelli2025incidenceandreasons pages 1-2, borrelli2025incidenceandreasons pages 2-3)

### 5.2 Safety surveillance (real-world pharmacovigilance)
WHO-VigiAccess reporting for four anti-VEGF agents totaled **57,779** reports as of 2023, and the largest category was eye disorders (43.56%). (li2024arealworlddata pages 4-5)

### 5.3 Durable/one-time approaches: RGX-314 gene therapy (real-world implementation in development)
RGX-314/ABBV-RGX-314 is in late-stage clinical development with both **subretinal** and **suprachoroidal** delivery strategies, testing whether a one-time AAV8 gene therapy encoding an anti-VEGF Fab can maintain vision while reducing supplemental injection burden versus standard intravitreal anti-VEGF regimens. (NCT04514653 chunk 1, NCT04704921 chunk 1, NCT05407636 chunk 1)

---

## 6) Summary table (molecular forms → function → translation)

| Entity | How generated | Localization / bioavailability | Main receptors / co-receptors and pathway notes | Clinical relevance / examples | Key evidence citations |
|---|---|---|---|---|---|
| VEGF121 | Alternative splicing of the 8-exon human VEGFA gene | Freely diffusible; little/no heparan-sulfate proteoglycan (HSPG) sequestration compared with longer isoforms | VEGFA ligand for VEGFR1 and VEGFR2; signalling is dominated functionally by VEGFR2, which activates PLCγ-PKC-ERK, PI3K-AKT, and FAK programs controlling endothelial proliferation, migration, survival, and permeability; neuropilins can act as co-receptors for VEGFA isoforms | Core VEGFA biology underpinning anti-VEGF therapies used in oncology and neovascular eye disease | (perezgutierrez2023biologyandtherapeutic pages 5-6, perezgutierrez2023biologyandtherapeutic pages 1-3) |
| VEGF165 | Alternative splicing; canonical major pro-angiogenic isoform | Partly diffusible and partly HSPG/ECM-bound via exon 7-encoded heparin-binding features | Binds VEGFR1/VEGFR2 and can engage neuropilin co-receptors; often treated as the classic pro-angiogenic VEGFA subtype; VEGFR2 is the main pro-angiogenic signalling receptor, whereas VEGFR1 can limit VEGFA available to VEGFR2 | Central target context for ocular anti-VEGF therapy; VEGF/VEGFR2 axis is a main driver of retinal/fundus neovascularization and vision-preserving anti-VEGF treatment | (perezgutierrez2023biologyandtherapeutic pages 5-6, li2025advancesinthe pages 1-2, perezgutierrez2023biologyandtherapeutic pages 1-3) |
| VEGF189 / VEGF206 | Alternative splicing including longer C-terminal heparin-binding regions (exons 6/7 contributions) | Largely sequestered in extracellular matrix and on HSPGs; relatively less diffusible than VEGF121/165 | Same VEGFA receptor system, but ECM retention alters spatial signalling gradients and vascular patterning/bioavailability | Relevant to tissue patterning and local VEGFA availability; illustrates why different VEGFA forms may respond differently to release/proteolysis in disease tissues | (perezgutierrez2023biologyandtherapeutic pages 5-6, perezgutierrez2023biologyandtherapeutic pages 1-3) |
| VEGFxxxb / VEGF165b | Alternative splice variants with altered terminal sequence; reported inhibitory variants remain debated | Secreted isoform class; not primarily defined by ECM retention in the cited evidence | Can bind VEGFR2 but are now viewed in authoritative review as weak agonists rather than true antagonists; existence/physiological role of endogenous anti-angiogenic VEGFxxxb remains debated | Important for interpretation of isoform-specific therapeutic strategies, but not established as a straightforward endogenous anti-VEGF system | (perezgutierrez2023biologyandtherapeutic pages 17-17, lee2025vascularendothelialgrowth pages 3-4) |
| VEGF110 / VEGF113 fragments | Proteolytic processing of VEGFA isoforms into shorter bioactive fragments | Shorter bioactive forms with altered bioavailability relative to parent isoforms | Retain VEGF bioactivity within the VEGFR pathway; proteolysis is part of how VEGFA availability and vascular patterning are tuned | Shows that VEGFA function is controlled not only by splicing but also by extracellular processing; relevant to diseased matrix remodeling | (perezgutierrez2023biologyandtherapeutic pages 17-17, perezgutierrez2023biologyandtherapeutic pages 1-3) |
| L-VEGF | Non-canonical translation from an upstream CUG start codon under hypoxic conditions, producing a longer VEGF-A isoform with an N-terminal extension | Intracellular precursor form before cleavage; produced under hypoxia | Proteolytically cleaved upstream of the canonical VEGF start to yield secreted VEGF-A plus N-VEGF; supports a dual response in which one product acts extracellularly and the other intracellularly/nuclearly | Expands VEGFA functional annotation beyond secreted angiogenic ligand biology; relevant to hypoxia adaptation and possibly cancer/ischemic biology | (katsman2022nvegftheautoregulatory pages 1-3, katsman2022nvegftheautoregulatory pages 10-13) |
| N-VEGF | N-terminal fragment generated by proteolytic cleavage of L-VEGF | Retained intracellularly and mobilized to the nucleus; forced nuclear localization is sufficient to induce part of a hypoxia-like program even in normoxia | Does not function as the classic extracellular VEGFR ligand; instead acts as a nuclear/autoregulatory arm of VEGF-A, inducing genes including Hif1α and VEGF-A isoforms and supporting anti-apoptotic/hypoxia-survival programs; deletion increases hypoxia-related apoptosis | Important nuance for UniProt P15692 because the reviewed long-form precursor contains both secreted VEGFA and N-VEGF products; suggests VEGFA biology includes intracrine nuclear stress-response functions in addition to paracrine angiogenesis | (katsman2022nvegftheautoregulatory pages 1-3, katsman2022nvegftheautoregulatory pages 10-13, katsman2022nvegftheautoregulatory pages 6-7, katsman2022nvegftheautoregulatory pages 7-10) |
| Secreted VEGFA signalling axis (cross-isoform summary) | Combined output of VEGFA splicing, translation, and processing | Secreted into extracellular space, with isoform-dependent diffusibility vs ECM sequestration | VEGFR2 is the principal pro-angiogenic receptor; VEGFR1 has weaker signalling and important decoy/regulatory behavior; co-receptors NRP1/NRP2 enhance signalling context; downstream pathways include PLCγ-PKC-ERK, PI3K-AKT, and FAK | Foundation of approved anti-VEGF/anti-VEGFR treatment classes in oncology and ophthalmology; anti-VEGF therapy markedly improved outcomes in neovascular eye disease, though repeated injections and incomplete response remain limitations | (perezgutierrez2023biologyandtherapeutic pages 5-6, li2025advancesinthe pages 1-2, lee2025vascularendothelialgrowth pages 1-2) |
| Clinical translation: anti-VEGF drugs and gene therapy | Therapeutic blockade of VEGFA or VEGF-pathway signalling; emerging vectored anti-VEGF expression approaches | Drug delivery is systemic or intraocular depending on indication; ocular therapy is typically intravitreal, while gene therapy aims longer intraocular durability | Therapeutics target the VEGF pathway rather than one single endogenous isoform; review evidence notes approvals across ophthalmology/oncology and emerging gene-therapy approaches for nAMD such as RGX-314 in early clinical development | Real-world and trial context: anti-VEGF transformed neovascular eye disease care; recent cited review context notes RGX-314 phase 1/2a development and long-term outcomes analyses, highlighting current movement toward more durable VEGF-pathway suppression | (lee2025vascularendothelialgrowth pages 1-2, li2025advancesinthe pages 13-13, perezgutierrez2023biologyandtherapeutic pages 1-3) |


*Table: This table summarizes the main functional VEGFA products relevant to human UniProt P15692, including splice isoforms, proteolytic fragments, and the long-form L-VEGF/N-VEGF pathway. It also links these molecular forms to receptor signaling and current clinical translation in ophthalmology and oncology.*

---

## 7) Key takeaways for functional annotation of VEGFA (UniProt P15692)

1. **Primary molecular function:** VEGF-A is a **secreted signaling ligand** whose main biochemical role is **receptor binding/activation** (VEGFR1/VEGFR2 with neuropilin co-receptors), driving endothelial signaling through PLCγ–PKC–ERK, PI3K–AKT, and FAK-associated pathways to control angiogenesis, survival, and permeability. (perezgutierrez2023biologyandtherapeutic pages 5-6)
2. **Form-dependent bioavailability is central:** Alternative splicing and matrix binding (HSPG/ECM retention) are not peripheral details; they are core determinants of VEGFA spatial signaling and thus of phenotype. (perezgutierrez2023biologyandtherapeutic pages 1-3, perezgutierrez2023biologyandtherapeutic pages 5-6)
3. **VEGFA includes an intracrine/nuclear arm:** The **L-VEGF → N-VEGF** axis implies VEGFA can contribute directly to hypoxia adaptation through a nuclear fragment that reshapes gene expression and cell survival under hypoxic stress. (katsman2022nvegftheautoregulatory pages 1-3, katsman2022nvegftheautoregulatory pages 7-10)
4. **Clinical translation is mature yet evolving:** Anti-VEGF therapies are foundational in ophthalmology, but real-world data show injection burden, discontinuation, and suboptimal long-term outcomes; durable approaches including gene therapy (RGX-314) represent a major active implementation pathway. (gyenes2025evaluationofthe pages 7-9, borrelli2025incidenceandreasons pages 1-2, NCT04514653 chunk 1)

---

## Source details (URLs and publication dates)

- Pérez-Gutiérrez L, Ferrara N. **Biology and therapeutic targeting of vascular endothelial growth factor A.** *Nat Rev Mol Cell Biol.* **Jul 2023**. https://doi.org/10.1038/s41580-023-00631-w (perezgutierrez2023biologyandtherapeutic pages 1-3)
- Li C, Lu Y, Song Z, Liu Y. **A real-world data analysis of ocular adverse events linked to anti-VEGF drugs: a WHO-VigiAccess study.** *Front Pharmacol.* **Jul 2024**. https://doi.org/10.3389/fphar.2024.1398783 (li2024arealworlddata pages 1-2)
- Katsman M, et al. **N-VEGF, the autoregulatory arm of VEGF-A.** *Cells.* **Mar 2022**. https://doi.org/10.3390/cells11081289 (katsman2022nvegftheautoregulatory pages 1-3)
- ClinicalTrials.gov: **NCT03066258** (posted/updated metadata available on record; gene therapy RGX-314; subretinal; completed). https://clinicaltrials.gov/study/NCT03066258 (NCT03066258 chunk 1)
- ClinicalTrials.gov: **NCT04514653** (AAVIATE; suprachoroidal ABBV-RGX-314; active not recruiting). https://clinicaltrials.gov/study/NCT04514653 (NCT04514653 chunk 1)
- ClinicalTrials.gov: **NCT04704921** (ATMOSPHERE; subretinal ABBV-RGX-314; active not recruiting). https://clinicaltrials.gov/study/NCT04704921 (NCT04704921 chunk 1)
- ClinicalTrials.gov: **NCT05407636** (Phase 3; subretinal ABBV-RGX-314; recruiting). https://clinicaltrials.gov/study/NCT05407636 (NCT05407636 chunk 1)


References

1. (perezgutierrez2023biologyandtherapeutic pages 1-3): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 480 citations and is from a domain leading peer-reviewed journal.

2. (katsman2022nvegftheautoregulatory pages 1-3): Marina Katsman, Aviva Azriel, Guy Horev, Yitzhak Reizel, and Ben-Zion Levi. N-vegf, the autoregulatory arm of vegf-a. Cells, Mar 2022. URL: https://doi.org/10.3390/cells11081289, doi:10.3390/cells11081289. This article has 8 citations.

3. (perezgutierrez2023biologyandtherapeutic pages 5-6): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 480 citations and is from a domain leading peer-reviewed journal.

4. (perezgutierrez2023biologyandtherapeutic pages 17-17): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 480 citations and is from a domain leading peer-reviewed journal.

5. (perezgutierrez2023biologyandtherapeutic pages 15-16): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 480 citations and is from a domain leading peer-reviewed journal.

6. (katsman2022nvegftheautoregulatory pages 10-13): Marina Katsman, Aviva Azriel, Guy Horev, Yitzhak Reizel, and Ben-Zion Levi. N-vegf, the autoregulatory arm of vegf-a. Cells, Mar 2022. URL: https://doi.org/10.3390/cells11081289, doi:10.3390/cells11081289. This article has 8 citations.

7. (li2025advancesinthe pages 1-2): Huan Li and Xiong Huang. Advances in the molecular signaling mechanisms of vegf/vegfr2 in fundus neovascularization disease (review). Experimental and Therapeutic Medicine, 30:1-13, May 2025. URL: https://doi.org/10.3892/etm.2025.12893, doi:10.3892/etm.2025.12893. This article has 7 citations and is from a peer-reviewed journal.

8. (li2024arealworlddata pages 2-4): Chen Li, Yicheng Lu, Ziyue Song, and Yueqi Liu. A real-world data analysis of ocular adverse events linked to anti-vegf drugs: a who-vigiaccess study. Frontiers in Pharmacology, Jul 2024. URL: https://doi.org/10.3389/fphar.2024.1398783, doi:10.3389/fphar.2024.1398783. This article has 7 citations.

9. (li2024arealworlddata pages 1-2): Chen Li, Yicheng Lu, Ziyue Song, and Yueqi Liu. A real-world data analysis of ocular adverse events linked to anti-vegf drugs: a who-vigiaccess study. Frontiers in Pharmacology, Jul 2024. URL: https://doi.org/10.3389/fphar.2024.1398783, doi:10.3389/fphar.2024.1398783. This article has 7 citations.

10. (li2024arealworlddata pages 4-5): Chen Li, Yicheng Lu, Ziyue Song, and Yueqi Liu. A real-world data analysis of ocular adverse events linked to anti-vegf drugs: a who-vigiaccess study. Frontiers in Pharmacology, Jul 2024. URL: https://doi.org/10.3389/fphar.2024.1398783, doi:10.3389/fphar.2024.1398783. This article has 7 citations.

11. (NCT03066258 chunk 1):  Safety and Tolerability of RGX-314 (Investigational Product) Gene Therapy for Neovascular AMD Trial. REGENXBIO Inc.. 2017. ClinicalTrials.gov Identifier: NCT03066258

12. (NCT04704921 chunk 1):  Pivotal 1 Study of ABBV-RGX-314 (Also Known as RGX-314) Gene Therapy Administered Via Subretinal Delivery One Time in Participants With nAMD. AbbVie. 2020. ClinicalTrials.gov Identifier: NCT04704921

13. (NCT04514653 chunk 1):  RGX-314 Gene Therapy Administered in the Suprachoroidal Space for Participants With Neovascular Age-Related Macular Degeneration (nAMD). AbbVie. 2020. ClinicalTrials.gov Identifier: NCT04514653

14. (NCT05407636 chunk 1):  Pivotal 2 Study of RGX-314 Gene Therapy in Participants With nAMD. AbbVie. 2022. ClinicalTrials.gov Identifier: NCT05407636

15. (katsman2022nvegftheautoregulatory pages 6-7): Marina Katsman, Aviva Azriel, Guy Horev, Yitzhak Reizel, and Ben-Zion Levi. N-vegf, the autoregulatory arm of vegf-a. Cells, Mar 2022. URL: https://doi.org/10.3390/cells11081289, doi:10.3390/cells11081289. This article has 8 citations.

16. (katsman2022nvegftheautoregulatory pages 7-10): Marina Katsman, Aviva Azriel, Guy Horev, Yitzhak Reizel, and Ben-Zion Levi. N-vegf, the autoregulatory arm of vegf-a. Cells, Mar 2022. URL: https://doi.org/10.3390/cells11081289, doi:10.3390/cells11081289. This article has 8 citations.

17. (gyenes2025evaluationofthe pages 7-9): Andrea Gyenes, Lilla István, András Papp, Miklós Resch, Zsuzsa Récsán, Mónika Ecsedy, Zsuzsanna Szepessy, Antal Szabó, Balázs Lesch, György Barcsay, Ágnes Borbándy, Gábor László Sándor, Zoltán Z. Nagy, and Illés Kovács. Evaluation of the duration of good visual acuity during anti-vegf therapy for age-related macular degeneration in routine clinical practice. International Journal of Molecular Sciences, 26:10927, Nov 2025. URL: https://doi.org/10.3390/ijms262210927, doi:10.3390/ijms262210927. This article has 1 citations.

18. (borrelli2025incidenceandreasons pages 1-2): Enrico Borrelli, Claudio Foti, Lorena Ulla, Annamaria Porreca, Ugo Introini, Maria Oliva Grassi, Pasquale Viggiano, Mario Peronetti, Rebecca Toscani, Giacomo Boscia, Alba Chiara Termite, Carlo Gennaro, Paola Marolo, Francesco Boscia, Francesco Bandello, and Michele Reibaldi. Incidence and reasons for discontinuation of anti-vegf treatment in neovascular age-related macular degeneration. The British Journal of Ophthalmology, 109:875-881, Mar 2025. URL: https://doi.org/10.1136/bjo-2024-326152, doi:10.1136/bjo-2024-326152. This article has 10 citations.

19. (borrelli2025incidenceandreasons pages 2-3): Enrico Borrelli, Claudio Foti, Lorena Ulla, Annamaria Porreca, Ugo Introini, Maria Oliva Grassi, Pasquale Viggiano, Mario Peronetti, Rebecca Toscani, Giacomo Boscia, Alba Chiara Termite, Carlo Gennaro, Paola Marolo, Francesco Boscia, Francesco Bandello, and Michele Reibaldi. Incidence and reasons for discontinuation of anti-vegf treatment in neovascular age-related macular degeneration. The British Journal of Ophthalmology, 109:875-881, Mar 2025. URL: https://doi.org/10.1136/bjo-2024-326152, doi:10.1136/bjo-2024-326152. This article has 10 citations.

20. (lee2025vascularendothelialgrowth pages 3-4): Chunsik Lee, Myung-Jin Kim, Anil Kumar, Han-Woong Lee, Yunlong Yang, and Yonghwan Kim. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy, May 2025. URL: https://doi.org/10.1038/s41392-025-02249-0, doi:10.1038/s41392-025-02249-0. This article has 294 citations and is from a peer-reviewed journal.

21. (lee2025vascularendothelialgrowth pages 1-2): Chunsik Lee, Myung-Jin Kim, Anil Kumar, Han-Woong Lee, Yunlong Yang, and Yonghwan Kim. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy, May 2025. URL: https://doi.org/10.1038/s41392-025-02249-0, doi:10.1038/s41392-025-02249-0. This article has 294 citations and is from a peer-reviewed journal.

22. (li2025advancesinthe pages 13-13): Huan Li and Xiong Huang. Advances in the molecular signaling mechanisms of vegf/vegfr2 in fundus neovascularization disease (review). Experimental and Therapeutic Medicine, 30:1-13, May 2025. URL: https://doi.org/10.3892/etm.2025.12893, doi:10.3892/etm.2025.12893. This article has 7 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](VEGFA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. perezgutierrez2023biologyandtherapeutic pages 5-6
2. perezgutierrez2023biologyandtherapeutic pages 1-3
3. li2024arealworlddata pages 2-4
4. katsman2022nvegftheautoregulatory pages 1-3
5. perezgutierrez2023biologyandtherapeutic pages 15-16
6. li2025advancesinthe pages 1-2
7. gyenes2025evaluationofthe pages 7-9
8. li2024arealworlddata pages 4-5
9. li2024arealworlddata pages 1-2
10. perezgutierrez2023biologyandtherapeutic pages 17-17
11. katsman2022nvegftheautoregulatory pages 10-13
12. katsman2022nvegftheautoregulatory pages 6-7
13. katsman2022nvegftheautoregulatory pages 7-10
14. borrelli2025incidenceandreasons pages 1-2
15. borrelli2025incidenceandreasons pages 2-3
16. lee2025vascularendothelialgrowth pages 3-4
17. lee2025vascularendothelialgrowth pages 1-2
18. li2025advancesinthe pages 13-13
19. https://doi.org/10.1038/s41580-023-00631-w
20. https://doi.org/10.3389/fphar.2024.1398783
21. https://doi.org/10.3390/cells11081289
22. https://clinicaltrials.gov/study/NCT03066258
23. https://clinicaltrials.gov/study/NCT04514653
24. https://clinicaltrials.gov/study/NCT04704921
25. https://clinicaltrials.gov/study/NCT05407636
26. https://doi.org/10.1038/s41580-023-00631-w,
27. https://doi.org/10.3390/cells11081289,
28. https://doi.org/10.3892/etm.2025.12893,
29. https://doi.org/10.3389/fphar.2024.1398783,
30. https://doi.org/10.3390/ijms262210927,
31. https://doi.org/10.1136/bjo-2024-326152,
32. https://doi.org/10.1038/s41392-025-02249-0,