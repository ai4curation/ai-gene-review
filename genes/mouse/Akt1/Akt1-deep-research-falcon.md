---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-03T23:48:20.560655'
end_time: '2026-05-04T00:04:09.247875'
duration_seconds: 948.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Akt1
  gene_symbol: Akt1
  uniprot_accession: P31750
  protein_description: 'RecName: Full=RAC-alpha serine/threonine-protein kinase; EC=2.7.11.1
    {ECO:0000269|PubMed:22057101, ECO:0000269|PubMed:23684622, ECO:0000269|PubMed:26235620,
    ECO:0000269|PubMed:26440888, ECO:0000269|PubMed:30504268}; AltName: Full=AKT1
    kinase; AltName: Full=Protein kinase B; Short=PKB; AltName: Full=Protein kinase
    B alpha; Short=PKB alpha; AltName: Full=Proto-oncogene c-Akt; AltName: Full=RAC-PK-alpha;
    AltName: Full=Thymoma viral proto-oncogene;'
  gene_info: Name=Akt1; Synonyms=Akt, Rac;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the protein kinase superfamily. AGC Ser/Thr
  protein_domains: AGC-kinase_C. (IPR000961); Akt1. (IPR034676); Kinase-like_dom_sf.
    (IPR011009); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P31750
- **Protein Description:** RecName: Full=RAC-alpha serine/threonine-protein kinase; EC=2.7.11.1 {ECO:0000269|PubMed:22057101, ECO:0000269|PubMed:23684622, ECO:0000269|PubMed:26235620, ECO:0000269|PubMed:26440888, ECO:0000269|PubMed:30504268}; AltName: Full=AKT1 kinase; AltName: Full=Protein kinase B; Short=PKB; AltName: Full=Protein kinase B alpha; Short=PKB alpha; AltName: Full=Proto-oncogene c-Akt; AltName: Full=RAC-PK-alpha; AltName: Full=Thymoma viral proto-oncogene;
- **Gene Information:** Name=Akt1; Synonyms=Akt, Rac;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the protein kinase superfamily. AGC Ser/Thr
- **Key Domains:** AGC-kinase_C. (IPR000961); Akt1. (IPR034676); Kinase-like_dom_sf. (IPR011009); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Akt1" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Akt1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Akt1** (gene ID: Akt1, UniProt: P31750) in mouse.

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
- **UniProt Accession:** P31750
- **Protein Description:** RecName: Full=RAC-alpha serine/threonine-protein kinase; EC=2.7.11.1 {ECO:0000269|PubMed:22057101, ECO:0000269|PubMed:23684622, ECO:0000269|PubMed:26235620, ECO:0000269|PubMed:26440888, ECO:0000269|PubMed:30504268}; AltName: Full=AKT1 kinase; AltName: Full=Protein kinase B; Short=PKB; AltName: Full=Protein kinase B alpha; Short=PKB alpha; AltName: Full=Proto-oncogene c-Akt; AltName: Full=RAC-PK-alpha; AltName: Full=Thymoma viral proto-oncogene;
- **Gene Information:** Name=Akt1; Synonyms=Akt, Rac;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the protein kinase superfamily. AGC Ser/Thr
- **Key Domains:** AGC-kinase_C. (IPR000961); Akt1. (IPR034676); Kinase-like_dom_sf. (IPR011009); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Akt1" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Akt1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Akt1** (gene ID: Akt1, UniProt: P31750) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research Report: Mouse Akt1 (UniProt P31750) — Functional Annotation and Current Understanding

### 0) Target verification (critical identity check)
The requested target is **mouse Akt1 (Mus musculus)**, UniProt **P31750**, described as **RAC‑alpha serine/threonine‑protein kinase (AKT1/PKBα)**. The retrieved literature used here addresses the **AKT/PKB family**, consistently describing AKT proteins as **AGC-family Ser/Thr kinases** with an **N‑terminal PH domain**, **central kinase domain**, and **C‑terminal hydrophobic motif/tail**, and uses canonical activation residues **Thr308** and **Ser473** that match the expected AKT1 architecture/function for mouse Akt1. Where sources address isoforms, **AKT1** is treated explicitly as the broadly expressed isoform distinct from **AKT2** and **AKT3**, and interpretations are restricted to AKT1 unless otherwise stated. (chu2026structuralandmechanistic pages 2-3, modi2023theroleof pages 1-2)

### 1) Key concepts and definitions (current consensus)

#### 1.1 What Akt1 is
Akt1 is a **protein kinase (EC 2.7.11.1)** in the **AGC Ser/Thr kinase** family. Canonically, AKT kinases phosphorylate Ser/Thr residues in substrates containing a **basophilic consensus motif** approximated as **R‑X‑R‑X‑X‑S/T‑φ** (φ = hydrophobic residue). (chu2026structuralandmechanistic pages 2-3)

#### 1.2 Catalyzed reaction and substrate specificity
Functionally, Akt1 catalyzes **ATP-dependent phosphorylation** of protein substrates on Ser/Thr. Its substrate repertoire is broad (>100 substrates are commonly reported for AKT family members), but repeatedly emphasized “well-established” targets include **GSK3**, **FOXO transcription factors**, and **TSC2**, with additional frequent mention of **PRAS40** as an mTORC1-regulatory substrate in pathway schematics. (chu2026structuralandmechanistic pages 2-3, leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4)

#### 1.3 Canonical activation mechanism (PI3K → PIP3 → Akt)
A central defining concept is that Akt activation is **membrane-coupled**:

1) **PI3K** produces **PIP3** at the plasma membrane.
2) **PIP3 binds PH domains** in **Akt** and **PDK1**, recruiting both to the plasma membrane.
3) **PDK1 phosphorylates Akt at Thr308** (activation loop) to yield **partial activation**.
4) **mTORC2 phosphorylates Akt at Ser473** (C-terminal hydrophobic motif) to yield **full activation**.

This sequence is summarized explicitly in multiple 2023–2024 reviews and in a 2023 primary mechanistic study, and is also captured visually in a PI3K/Akt/mTOR pathway diagram in a 2024 review (Figure 1). (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4, palma2023nuak1coordinatesgrowth pages 1-2, leiphrakpam2024pi3kaktmtorsignalingpathway media b35ad198)

#### 1.4 Negative regulation/termination
A key negative regulator is **PTEN**, which **opposes Akt activation** by converting **PIP3 to PIP2**, thereby reducing Akt membrane recruitment and pathway activation. (modi2023theroleof pages 1-2, chu2026structuralandmechanistic pages 3-4)

### 2) Functional roles, biological processes, and pathway placement

#### 2.1 Primary pathway role: central PI3K–Akt–mTOR signaling node
Across reviews, Akt is positioned as a central node coupling growth factor/RTK signaling to cellular programs of **growth, survival, metabolism, and protein synthesis**, with prominent functional coupling to **mTORC1** through phosphorylation of upstream regulators including **TSC2** and **PRAS40**. (chu2026structuralandmechanistic pages 1-2, leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4)

#### 2.2 Representative downstream processes (mechanistic examples)
* **Cell survival / anti-apoptosis**: Reviews emphasize Akt-mediated survival signaling through phosphorylation of multiple downstream targets and modulation of apoptotic regulators. (modi2023theroleof pages 2-3, caturano2024insulin–heartaxisbridging pages 2-3)
* **Metabolism (insulin signaling)**: In insulin-responsive contexts, Akt phosphorylates regulators including **TSC2**, **PRAS40**, and **GSK3**, linking insulin signaling to metabolism and mTORC1-regulated growth programs; cardiovascular-focused reviews highlight NO production through **NOS3/eNOS** as a downstream consequence. (caturano2024insulin–heartaxisbridging pages 2-3)
* **Transcriptional control via FOXO**: FOXO family members are repeatedly listed as Akt substrates; phosphorylation of FOXO can alter FOXO localization and transcriptional outputs (e.g., cytoplasmic sequestration in pathway summaries). (beker2026bmal1pi3kaktcrosstalkin pages 5-7, palma2023nuak1coordinatesgrowth pages 2-4)

### 3) Subcellular localization: where Akt1 acts

#### 3.1 Membrane recruitment as a localization-dependent activation step
A consensus concept is that **Akt activation requires recruitment to the plasma membrane** via **PH-domain binding to PIP3**, which positions Akt for phosphorylation by PDK1 and mTORC2. (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4, palma2023nuak1coordinatesgrowth pages 1-2)

#### 3.2 Cytoplasmic and nuclear action
Reviews describe Akt as mediating substrate phosphorylation in both **cytoplasm and nucleus**, consistent with signaling outputs ranging from metabolic enzymes to transcription factors. (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4)

#### 3.3 Compartmentalization and substrate selectivity (recent mechanistic evidence)
A 2023 primary study adds an important refinement: **subcellular compartmentalization can bias which Akt substrates are phosphorylated**.

*Palma et al., 2023 (Cell & Bioscience; Dec 2023; https://doi.org/10.1186/s13578-023-01185-2)* report that **NUAK1** is a regulator of growth factor–dependent Akt activation and is associated with **Rab5+ early endosomes** (not late endosomes/lysosomes in their assays). Pharmacologic inhibition or loss of NUAK1 **reduces Akt Ser473 phosphorylation** and preferentially reduces **FOXO1/3a phosphorylation (Thr24/Thr32)** while leaving **TSC2 Thr1462 phosphorylation** largely unaffected, supporting a model where **endosomal organization and mTORC2 localization** influence Akt substrate routing. (palma2023nuak1coordinatesgrowth pages 2-4, palma2023nuak1coordinatesgrowth pages 4-7, palma2023nuak1coordinatesgrowth pages 1-2)

*Note (limitation):* mitochondria-specific localization of Akt1 was not supported by the retrieved excerpts and is therefore not asserted here.

### 4) Isoform specificity (Akt1 vs Akt2 vs Akt3) — why it matters for annotation
A recurring expert consensus in 2023–2024 reviews is that AKT isoforms are not redundant:
* **Akt1** is broadly expressed and is commonly linked to **cell proliferation and survival** programs.
* **Akt2** is enriched in **insulin-sensitive tissues** and is closely tied to **glucose homeostasis/metabolic control**.
* **Akt3** is often emphasized in **brain** contexts (e.g., brain size/development and certain brain tumor contexts).

This isoform framing is important for functional annotation because many studies report “Akt” phosphorylation or activity readouts that may reflect a mixture of isoforms. (modi2023theroleof pages 1-2, chu2026structuralandmechanistic pages 2-3)

### 5) Recent developments (prioritizing 2023–2024)

#### 5.1 New regulators and location-specific Akt signaling (Dec 2023)
**NUAK1→mTORC2→Akt Ser473** regulation is proposed as a mechanism tuning growth-factor responses and substrate selection (FOXO-biased vs TSC2). This is a concrete 2023 addition to mechanistic understanding that intersects directly with “where in the cell” Akt signaling is executed. (palma2023nuak1coordinatesgrowth pages 2-4, palma2023nuak1coordinatesgrowth pages 4-7)

#### 5.2 Mutation/alteration statistics informing pathway targeting (Mar 2024)
In colorectal cancer, a 2024 review summarizes clinically relevant pathway alteration frequencies upstream of Akt:
* **PIK3CA somatic missense mutations occur in ~1/3 of CRC cases** during the adenoma–carcinoma transition.
* **Hotspot mutations (E542K, E545K, H1047R) comprise ~80%** of PIK3CA mutations.

These statistics motivate PI3K–Akt–mTOR axis targeting strategies and indicate how often Akt lies downstream of genetically activated signaling. (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4)

#### 5.3 Isoform-selective therapeutic logic supported by 2024 primary evidence (Oct 2024)
*Miller et al., Oncogene (Oct 2024; https://doi.org/10.1038/s41388-023-02875-4)* provide primary evidence that **PTEN status rewires PI3K/AKT isoform dependence** in prostate cancer models. They report that PTEN-deficient cells preferentially depend on **AKT2** (and sometimes AKT3), whereas PTEN re-expression shifts functional dependence toward **AKT1**; they operationalize this with isoform-selective inhibitors and specific concentrations (e.g., **AKT1 inhibitor A‑674563 100 nM**; **AKT2 inhibitor CCT‑128930 300 nM**; **PI3Kα inhibitor BYL‑719 5 nM**; **PI3Kβ inhibitor GSK‑2636771 25 nM**). This is a pragmatic 2024 result supporting **isoform-aware targeting** rather than assuming pan-AKT inhibition is optimal. (miller2024ptenregulatedpi3kp110and pages 2-3)

#### 5.4 Microbiome–metabolite modulation of insulin signaling that intersects Akt–mTOR wiring (Aug 2024)
*Du et al., PNAS (Aug 2024; https://doi.org/10.1073/pnas.2400385121)* report that a microbiota-derived tryptophan metabolite (**5‑HIAA**) is depleted in diet-induced insulin resistance and that **administering 5‑HIAA** improves glucose intolerance and preserves hepatic insulin sensitivity in mice, mechanistically via **AhR activation → increased TSC2 transcription → inhibition of mTORC1**, which intersects canonical insulin/PI3K/Akt pathway control of mTORC1 signaling. (du2024themicrobiotadependenttryptophan pages 1-2)

### 6) Current applications and real-world implementations

#### 6.1 Preclinical/experimental implementations in mouse and mammalian systems
**Mouse models and PTEN context** are used to test isoform dependencies and therapeutic combinations in oncology; PTEN-dependent shifts in AKT isoform reliance have been demonstrated in transgenic mouse-derived prostate cancer lines and human prostate cancer cell models. (miller2024ptenregulatedpi3kp110and pages 2-3)

In metabolism, HFD mouse models are used to test interventions (e.g., microbiota-linked metabolite supplementation) that converge on the insulin→Akt→mTOR axis. (du2024themicrobiotadependenttryptophan pages 1-2)

#### 6.2 Therapeutic modulation in neurological/cardiovascular injury contexts
A 2023 review synthesizes translational evidence that Akt signaling changes rapidly after TBI (on the order of minutes to days) and summarizes multiple interventions reported to modulate Akt/PI3K/mTOR signaling, including **valproic acid**, **simvastatin** (14-day regimen cited), **stachydrine**, and **sevoflurane**, discussed as approaches that may influence apoptosis, inflammation, and autophagy via Akt-linked mechanisms. (modi2023theroleof pages 2-3)

### 7) Expert opinions / analysis (from authoritative sources)

* Akt is repeatedly described as a **central hub** downstream of RTKs/PI3K and upstream of mTOR-driven programs; as a result, dysregulation is presented as mechanistically linked to diverse diseases (cancer, insulin resistance, neurological injury, cardiovascular disorders). (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4, caturano2024insulin–heartaxisbridging pages 2-3, modi2023theroleof pages 1-2)
* Reviews emphasize that **activation is multi-step and localization-dependent** (PIP3-dependent recruitment; PDK1/mTORC2 phosphorylation), which has direct implications for interpreting phospho-Akt biomarkers and for designing inhibitors that act at specific pathway nodes. (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4)
* A primary-study-driven expert inference emerging in 2023–2024 is that **subcellular compartmentalization can drive substrate selectivity**, meaning that “Akt activation” may not imply uniform phosphorylation of all substrates; rather, spatial organization (e.g., endosome/lysosome positioning and mTORC2 association) can route outputs toward FOXO-like targets versus TSC2-like targets. (palma2023nuak1coordinatesgrowth pages 4-7)

### 8) Relevant statistics and quantitative data (from recent sources)

* **CRC pathway genetics**: PIK3CA missense mutations in **~1/3** of CRC; common hotspots comprise **~80%** of PIK3CA mutations. (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4)
* **TBI epidemiology and Akt time-course**: worldwide annual TBI prevalence **200 per 100,000** and mortality **18 per 100,000**; Akt expression time-course post-TBI: **~15 min initiation**, **~4 h rise**, **4–24 h peak**, **~72 h decline**. (modi2023theroleof pages 2-3)
* **Implementation parameters for isoform targeting (preclinical)**: example inhibitor concentrations for AKT1 vs AKT2 and PI3K isoforms (AKT1i 100 nM, AKT2i 300 nM, p110αi 5 nM, p110βi 25 nM) and functional assay time windows (chemotaxis 16–24 h; invasion 24–48 h; lysates 48–72 h) used to demonstrate PTEN-dependent isoform reliance. (miller2024ptenregulatedpi3kp110and pages 2-3)

### 9) Summary tables
The following tables provide a compact synthesis of (i) core functional annotation details and (ii) 2023–2024 developments/applications.

| Topic | Evidence summary | Key citations |
|---|---|---|
| Identity/domains | Mouse Akt1 corresponds to RAC-alpha serine/threonine-protein kinase/PKBα in the AGC kinase family. The collected evidence describes AKT proteins as having an N-terminal PH domain, a central kinase domain, and a C-terminal regulatory tail/hydrophobic motif, which is consistent with the UniProt P31750 architecture. | (chu2026structuralandmechanistic pages 2-3, modi2023theroleof pages 1-2) |
| Catalytic activity | Akt1 is a serine/threonine protein kinase that recognizes basophilic substrate motifs of the form R-X-R-X-X-S/T-φ. Reported well-established AKT substrates include GSK3, FOXO transcription factors, TSC2, and PRAS40-linked mTORC1 regulation. | (chu2026structuralandmechanistic pages 2-3, chu2026structuralandmechanistic pages 1-2, leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4) |
| Activation mechanism | Canonical activation begins when PI3K generates PIP3, which recruits Akt through its PH domain to the plasma membrane together with PDK1. PDK1 phosphorylates Thr308 for partial activation, and mTORC2 phosphorylates Ser473 in the C-terminal hydrophobic region for full activation; the Thr308/Ser473 phosphorylation balance can influence substrate preference. | (chu2026structuralandmechanistic pages 3-4, leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4, palma2023nuak1coordinatesgrowth pages 1-2) |
| Key substrates/outputs | Evidence supports phosphorylation of FOXO1/3a, GSK3, TSC2, and PRAS40 as representative downstream events. These outputs connect Akt signaling to cell survival, proliferation, metabolism, and activation of mTORC1 through inhibition of negative regulators such as TSC2 and PRAS40. | (chu2026structuralandmechanistic pages 1-2, leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4, beker2026bmal1pi3kaktcrosstalkin pages 5-7) |
| Localization/compartmentalization | Akt activation depends on plasma-membrane recruitment by PIP3, but downstream signaling is not confined to that site. Evidence also indicates substrate-specific signaling in cytoplasm and nucleus, and a 2023 primary study links compartmentalization around early endosomes, lysosomes, and mTORC2 to differential phosphorylation of FOXO1/3a versus TSC2. | (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4, palma2023nuak1coordinatesgrowth pages 1-2, palma2023nuak1coordinatesgrowth pages 4-7) |
| Isoform specificity notes | The evidence identifies Akt1 as the broadly expressed isoform mainly associated with proliferation and survival, whereas Akt2 is more linked to insulin-responsive metabolism and Akt3 to brain/testis functions. A 2024 cancer study further supports isoform-specific wiring by showing PTEN-positive contexts depend more on AKT1, whereas PTEN-deficient metastatic contexts depend more on AKT2. | (chu2026structuralandmechanistic pages 2-3, modi2023theroleof pages 1-2, miller2024ptenregulatedpi3kp110and pages 1-2) |
| Negative regulation/termination | Negative regulation occurs upstream through PTEN, which dephosphorylates PIP3 and opposes Akt membrane recruitment/activation. Termination is also reported through phosphatases such as PP2A and PHLPP that reverse activating phosphorylations. | (chu2026structuralandmechanistic pages 3-4, modi2023theroleof pages 1-2) |


*Table: This table summarizes the core functional annotation points for mouse Akt1 (UniProt P31750) based strictly on the collected evidence snippets. It is useful as a compact reference for identity, mechanism, substrates, localization, isoform context, and negative regulation.*

| Source (first author, year) | Type (review/primary) | System/context | Key finding relevant to Akt1 function or targeting | Quantitative/statistical detail | URL/DOI |
|---|---|---|---|---|---|
| Modi, 2023 | Review | Neurological and cardiovascular pathologies; traumatic brain injury (TBI) emphasized | Summarizes Akt isoform biology, noting Akt1 as ubiquitous and associated with cell formation, apoptosis control, proliferation, angiogenesis, and tumor invasiveness; highlights therapeutic Akt upregulation/modulation as a translational strategy in TBI and related disorders (modi2023theroleof pages 1-2, modi2023theroleof pages 2-3) | TBI burden reported as annual prevalence 200/100,000 and mortality 18/100,000 worldwide; Akt expression starts ~15 min after TBI, rises to 4 h, peaks at 4–24 h, and subsides after ~72 h; Simvastatin regimen noted as 14 days (modi2023theroleof pages 2-3) | https://doi.org/10.26650/eurjbiol.2023.1240220 |
| Palma, 2023 | Primary | Growth-factor signaling in cultured cancer/HEK293T cells; mTORC2-Akt regulation | Demonstrates canonical Akt activation (PI3K→PIP3→PH-domain recruitment; PDK1 Thr308; mTORC2 Ser473) and identifies NUAK1 as a regulator of Akt Ser473 phosphorylation and substrate selectivity, preferentially affecting FOXO1/3a over TSC2; supports compartment-specific Akt signaling relevant to functional annotation and drug targeting (palma2023nuak1coordinatesgrowth pages 2-4, palma2023nuak1coordinatesgrowth pages 4-7, palma2023nuak1coordinatesgrowth pages 1-2) | NUAK1 inhibitor pretreatment 10 µM for 90 min; effects tracked over EGF stimulation windows including ~20–60 min; reduced Akt Ser473 and FOXO1/3a phosphorylation but not TSC2 in reported assays (palma2023nuak1coordinatesgrowth pages 2-4, palma2023nuak1coordinatesgrowth pages 4-7) | https://doi.org/10.1186/s13578-023-01185-2 |
| Leiphrakpam, 2024 | Review | Colorectal cancer (CRC) | Frames PI3K/Akt/mTOR as a therapeutic target in CRC; details Akt activation steps and downstream targets including PRAS40, TSC2, FOXO, and GSK3, supporting intervention at PI3K, Akt, and mTOR nodes (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4) | PIK3CA somatic missense mutations occur in ~1/3 of CRC cases; hotspot mutations E542K, E545K, H1047R account for ~80% of PIK3CA mutations (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4) | https://doi.org/10.3390/ijms25063178 |
| Giaccari, 2024 | Review | Mammalian ovary; fertility, PCOS, premature ovarian failure, ovarian cancer | Reviews PI3K/Akt as central to oogenesis, folliculogenesis, oocyte maturation, embryo development, and ovarian pathology; explicitly discusses use of inhibitors and activators to rebalance Akt signaling in ovarian disease contexts (giaccari2024anupdateon pages 1-2) | No specific quantitative/statistical values reported in the extracted context (giaccari2024anupdateon pages 1-2) | https://doi.org/10.3390/life14060722 |
| Caturano, 2024 | Review | Insulin signaling and cardiac physiology/pathophysiology | Summarizes canonical Akt activation and downstream phosphorylation of TSC2, PRAS40, GSK3, and NOS3/eNOS, linking Akt to cardiac metabolism, growth, survival, angiogenesis, vasorelaxation, and insulin-resistance biology (caturano2024insulin–heartaxisbridging pages 2-3) | No specific mutation-frequency or intervention statistics reported in the extracted context (caturano2024insulin–heartaxisbridging pages 2-3) | https://doi.org/10.3390/ijms25158369 |
| Miller, 2024 | Primary | Prostate cancer models, including transgenic mice and human PC cell lines | Shows PTEN status rewires PI3K/AKT isoform dependence: PTEN-deficient settings depend more on AKT2, whereas PTEN re-expression shifts dependency toward AKT1; supports isoform-selective targeting strategies rather than generic pan-AKT inhibition (miller2024ptenregulatedpi3kp110and pages 2-3) | Inhibitor conditions included A-674563 (AKT1i) 100 nM, CCT-128930 (AKT2i) 300 nM, BYL-719 (p110αi) 5 nM, GSK-2636771 (p110βi) 25 nM, Saracatinib 150 nM; sample sizes reported to provide >80% power; coefficient of variation 0.6; chemotaxis 16–24 h, invasion 24–48 h, lysate analysis 48–72 h post-transfection (miller2024ptenregulatedpi3kp110and pages 2-3) | https://doi.org/10.1038/s41388-023-02875-4 |
| Du, 2024 | Primary | High-fat-diet mouse model and human T2D-associated metabolite context | Identifies microbiota-derived 5-HIAA as a metabolite that improves glucose intolerance and preserves hepatic insulin sensitivity through AhR→TSC2→mTORC1 signaling, intersecting with insulin/PI3K/Akt pathway biology relevant to Akt-centered metabolic applications (du2024themicrobiotadependenttryptophan pages 1-2) | Qualitative effects reported in extracted context (improved glucose intolerance, obesity, hepatic insulin sensitivity), but no numerical phospho-Akt/pGSK3 statistics are provided in the retrieved excerpt (du2024themicrobiotadependenttryptophan pages 1-2) | https://doi.org/10.1073/pnas.2400385121 |


*Table: This table compiles recent 2023–2024 reviews and primary studies relevant to Akt1/PI3K/Akt/mTOR biology, emphasizing functional findings, translational applications, and quantitative details where available. It is useful for quickly identifying recent evidence on mechanism, disease relevance, and therapeutic targeting.*

### 10) Evidence and coverage limitations
1) The retrieved excerpts include robust support for **domain architecture**, **canonical activation**, **representative substrates**, and **compartmentalized signaling**, but do not provide sequence-level mapping explicitly to UniProt **P31750** within the text itself; identity is therefore anchored to the user-provided UniProt accession and the conserved AKT1 features documented in the sources. (chu2026structuralandmechanistic pages 2-3, modi2023theroleof pages 1-2)
2) Some recent primary studies (e.g., PNAS 2024 on 5‑HIAA) are represented here via abstract/limited excerpt; quantitative phospho-Akt effect sizes (e.g., fold changes, p-values) were not available in the retrieved text snippets and are not reported. (du2024themicrobiotadependenttryptophan pages 1-2)
3) While Akt biology is deeply developed, the current evidence set retrieved for this report does not include a mouse Akt1-specific subcellular localization dataset beyond plasma membrane recruitment and general cytoplasm/nucleus localization and the endosome/lysosome compartmentalization framework; additional targeted retrieval (e.g., Akt1 mitochondrial localization studies) would be required to expand the localization section beyond what is supported here.


References

1. (chu2026structuralandmechanistic pages 2-3): Nam Chu, Nhat Le, Ouada Nebie, and Sammi Yang. Structural and mechanistic basis of mtorc2 activation of protein kinase akt/pkb. Biochemical Journal, 483:375-389, Mar 2026. URL: https://doi.org/10.1042/bcj20253108, doi:10.1042/bcj20253108. This article has 1 citations and is from a domain leading peer-reviewed journal.

2. (modi2023theroleof pages 1-2): Akshat D. Modi, Aahmad Mahoon, and Dharmeshkumar M Modi. The role of akt signalling pathway in neurological and cardiovascular pathologies. European Journal of Biology, 82:95-108, Jun 2023. URL: https://doi.org/10.26650/eurjbiol.2023.1240220, doi:10.26650/eurjbiol.2023.1240220. This article has 3 citations.

3. (leiphrakpam2024pi3kaktmtorsignalingpathway pages 2-4): Premila Leiphrakpam and Chandrakanth Are. Pi3k/akt/mtor signaling pathway as a target for colorectal cancer treatment. International Journal of Molecular Sciences, 25:3178, Mar 2024. URL: https://doi.org/10.3390/ijms25063178, doi:10.3390/ijms25063178. This article has 179 citations.

4. (palma2023nuak1coordinatesgrowth pages 1-2): Mario Palma, Elizabeth Riffo, Alejandro Farias, Viviana Coliboro-Dannich, Luis Espinoza-Francine, Emilia Escalona, Roberto Amigo, José L. Gutiérrez, Roxana Pincheira, and Ariel F. Castro. Nuak1 coordinates growth factor-dependent activation of mtorc2 and akt signaling. Cell & Bioscience, Dec 2023. URL: https://doi.org/10.1186/s13578-023-01185-2, doi:10.1186/s13578-023-01185-2. This article has 9 citations and is from a peer-reviewed journal.

5. (leiphrakpam2024pi3kaktmtorsignalingpathway media b35ad198): Premila Leiphrakpam and Chandrakanth Are. Pi3k/akt/mtor signaling pathway as a target for colorectal cancer treatment. International Journal of Molecular Sciences, 25:3178, Mar 2024. URL: https://doi.org/10.3390/ijms25063178, doi:10.3390/ijms25063178. This article has 179 citations.

6. (chu2026structuralandmechanistic pages 3-4): Nam Chu, Nhat Le, Ouada Nebie, and Sammi Yang. Structural and mechanistic basis of mtorc2 activation of protein kinase akt/pkb. Biochemical Journal, 483:375-389, Mar 2026. URL: https://doi.org/10.1042/bcj20253108, doi:10.1042/bcj20253108. This article has 1 citations and is from a domain leading peer-reviewed journal.

7. (chu2026structuralandmechanistic pages 1-2): Nam Chu, Nhat Le, Ouada Nebie, and Sammi Yang. Structural and mechanistic basis of mtorc2 activation of protein kinase akt/pkb. Biochemical Journal, 483:375-389, Mar 2026. URL: https://doi.org/10.1042/bcj20253108, doi:10.1042/bcj20253108. This article has 1 citations and is from a domain leading peer-reviewed journal.

8. (modi2023theroleof pages 2-3): Akshat D. Modi, Aahmad Mahoon, and Dharmeshkumar M Modi. The role of akt signalling pathway in neurological and cardiovascular pathologies. European Journal of Biology, 82:95-108, Jun 2023. URL: https://doi.org/10.26650/eurjbiol.2023.1240220, doi:10.26650/eurjbiol.2023.1240220. This article has 3 citations.

9. (caturano2024insulin–heartaxisbridging pages 2-3): Alfredo Caturano, Raffaele Galiero, Erica Vetrano, Celestino Sardu, Luca Rinaldi, Vincenzo Russo, Marcellino Monda, Raffaele Marfella, and Ferdinando Carlo Sasso. Insulin–heart axis: bridging physiology to insulin resistance. International Journal of Molecular Sciences, 25:8369, Jul 2024. URL: https://doi.org/10.3390/ijms25158369, doi:10.3390/ijms25158369. This article has 44 citations.

10. (beker2026bmal1pi3kaktcrosstalkin pages 5-7): Mustafa C. Beker, Dirk M. Hermann, and Ertugrul Kilic. Bmal1-pi3k/akt crosstalk in ischemic injury and vascular repair: a circadian framework for neurovascular resilience. Exploration of Neuroscience, Mar 2026. URL: https://doi.org/10.37349/en.2026.1006127, doi:10.37349/en.2026.1006127. This article has 0 citations.

11. (palma2023nuak1coordinatesgrowth pages 2-4): Mario Palma, Elizabeth Riffo, Alejandro Farias, Viviana Coliboro-Dannich, Luis Espinoza-Francine, Emilia Escalona, Roberto Amigo, José L. Gutiérrez, Roxana Pincheira, and Ariel F. Castro. Nuak1 coordinates growth factor-dependent activation of mtorc2 and akt signaling. Cell & Bioscience, Dec 2023. URL: https://doi.org/10.1186/s13578-023-01185-2, doi:10.1186/s13578-023-01185-2. This article has 9 citations and is from a peer-reviewed journal.

12. (palma2023nuak1coordinatesgrowth pages 4-7): Mario Palma, Elizabeth Riffo, Alejandro Farias, Viviana Coliboro-Dannich, Luis Espinoza-Francine, Emilia Escalona, Roberto Amigo, José L. Gutiérrez, Roxana Pincheira, and Ariel F. Castro. Nuak1 coordinates growth factor-dependent activation of mtorc2 and akt signaling. Cell & Bioscience, Dec 2023. URL: https://doi.org/10.1186/s13578-023-01185-2, doi:10.1186/s13578-023-01185-2. This article has 9 citations and is from a peer-reviewed journal.

13. (miller2024ptenregulatedpi3kp110and pages 2-3): Karina A. Miller, Seamus Degan, Yanqing Wang, Joseph Cohen, Sheng Yu Ku, David W. Goodrich, and Irwin H. Gelman. Pten-regulated pi3k-p110 and akt isoform plasticity controls metastatic prostate cancer progression. Oncogene, 43:22-34, Oct 2024. URL: https://doi.org/10.1038/s41388-023-02875-4, doi:10.1038/s41388-023-02875-4. This article has 26 citations and is from a domain leading peer-reviewed journal.

14. (du2024themicrobiotadependenttryptophan pages 1-2): Wei Du, Shanshan Jiang, Shengxiang Yin, Rongjiang Wang, Chunling Zhang, Bin-Cheng Yin, Jialin Li, Li Li, Nan Qi, Ying Zhou, and Bang-Ce Ye. The microbiota-dependent tryptophan metabolite alleviates high-fat diet–induced insulin resistance through the hepatic ahr/tsc2/mtorc1 axis. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2400385121, doi:10.1073/pnas.2400385121. This article has 59 citations and is from a highest quality peer-reviewed journal.

15. (miller2024ptenregulatedpi3kp110and pages 1-2): Karina A. Miller, Seamus Degan, Yanqing Wang, Joseph Cohen, Sheng Yu Ku, David W. Goodrich, and Irwin H. Gelman. Pten-regulated pi3k-p110 and akt isoform plasticity controls metastatic prostate cancer progression. Oncogene, 43:22-34, Oct 2024. URL: https://doi.org/10.1038/s41388-023-02875-4, doi:10.1038/s41388-023-02875-4. This article has 26 citations and is from a domain leading peer-reviewed journal.

16. (giaccari2024anupdateon pages 1-2): Carlo Giaccari, Sevastiani Antonouli, George Anifandis, Sandra Cecconi, and Valentina Di Nisio. An update on physiopathological roles of akt in the reprodaktive mammalian ovary. Life, 14:722, Jun 2024. URL: https://doi.org/10.3390/life14060722, doi:10.3390/life14060722. This article has 26 citations.

## Citations

1. chu2026structuralandmechanistic pages 2-3
2. du2024themicrobiotadependenttryptophan pages 1-2
3. modi2023theroleof pages 2-3
4. giaccari2024anupdateon pages 1-2
5. modi2023theroleof pages 1-2
6. chu2026structuralandmechanistic pages 3-4
7. chu2026structuralandmechanistic pages 1-2
8. https://doi.org/10.1186/s13578-023-01185-2
9. https://doi.org/10.1038/s41388-023-02875-4
10. https://doi.org/10.1073/pnas.2400385121
11. https://doi.org/10.26650/eurjbiol.2023.1240220
12. https://doi.org/10.3390/ijms25063178
13. https://doi.org/10.3390/life14060722
14. https://doi.org/10.3390/ijms25158369
15. https://doi.org/10.1042/bcj20253108,
16. https://doi.org/10.26650/eurjbiol.2023.1240220,
17. https://doi.org/10.3390/ijms25063178,
18. https://doi.org/10.1186/s13578-023-01185-2,
19. https://doi.org/10.3390/ijms25158369,
20. https://doi.org/10.37349/en.2026.1006127,
21. https://doi.org/10.1038/s41388-023-02875-4,
22. https://doi.org/10.1073/pnas.2400385121,
23. https://doi.org/10.3390/life14060722,