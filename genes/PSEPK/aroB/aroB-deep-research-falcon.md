---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T20:39:52.113053'
end_time: '2026-06-11T20:48:04.491466'
duration_seconds: 492.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: aroB
  gene_symbol: aroB
  uniprot_accession: Q88CV2
  protein_description: 'RecName: Full=3-dehydroquinate synthase {ECO:0000255|HAMAP-Rule:MF_00110};
    Short=DHQS {ECO:0000255|HAMAP-Rule:MF_00110}; EC=4.2.3.4 {ECO:0000255|HAMAP-Rule:MF_00110};'
  gene_info: Name=aroB {ECO:0000255|HAMAP-Rule:MF_00110}; OrderedLocusNames=PP_5078;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the sugar phosphate cyclases superfamily.
  protein_domains: Dehydroquinate_synthase. (IPR050071); DHQ_synth_AroB. (IPR016037);
    DHQ_synth_fam. (IPR030963); DHQS/DOIS_N. (IPR030960); DHQS_C. (IPR056179)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: aroB-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88CV2
- **Protein Description:** RecName: Full=3-dehydroquinate synthase {ECO:0000255|HAMAP-Rule:MF_00110}; Short=DHQS {ECO:0000255|HAMAP-Rule:MF_00110}; EC=4.2.3.4 {ECO:0000255|HAMAP-Rule:MF_00110};
- **Gene Information:** Name=aroB {ECO:0000255|HAMAP-Rule:MF_00110}; OrderedLocusNames=PP_5078;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the sugar phosphate cyclases superfamily.
- **Key Domains:** Dehydroquinate_synthase. (IPR050071); DHQ_synth_AroB. (IPR016037); DHQ_synth_fam. (IPR030963); DHQS/DOIS_N. (IPR030960); DHQS_C. (IPR056179)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aroB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aroB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aroB** (gene ID: aroB, UniProt: Q88CV2) in PSEPK.

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
- **UniProt Accession:** Q88CV2
- **Protein Description:** RecName: Full=3-dehydroquinate synthase {ECO:0000255|HAMAP-Rule:MF_00110}; Short=DHQS {ECO:0000255|HAMAP-Rule:MF_00110}; EC=4.2.3.4 {ECO:0000255|HAMAP-Rule:MF_00110};
- **Gene Information:** Name=aroB {ECO:0000255|HAMAP-Rule:MF_00110}; OrderedLocusNames=PP_5078;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the sugar phosphate cyclases superfamily.
- **Key Domains:** Dehydroquinate_synthase. (IPR050071); DHQ_synth_AroB. (IPR016037); DHQ_synth_fam. (IPR030963); DHQS/DOIS_N. (IPR030960); DHQS_C. (IPR056179)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aroB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aroB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aroB** (gene ID: aroB, UniProt: Q88CV2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research Report: Functional Annotation of **aroB** (UniProt Q88CV2; locus **PP_5078**) in *Pseudomonas putida* KT2440

### 0) Target verification (mandatory)
The target protein is correctly identified as **3-dehydroquinate synthase (DHQS)** encoded by **aroB** in *Pseudomonas putida* KT2440. A KT2440 transcriptomics study explicitly maps the locus tag **PP_5078** to **aroB** and describes it as **3-dehydroquinate synthase** (“3-dehydroquinate synthase (aroB) (PP_5078)”). (lopezlara2020influenceofrehydration pages 2-4). Independent KT2440 metabolic-engineering literature also refers to **aroB** as encoding the native **3-dehydroquinate synthase** in the shikimate pathway. (ling2022muconicacidproduction pages 1-2). Authoritative pathway reviews define **AroB/DHQS** as **EC 4.2.3.4** and place it within the **sugar phosphate cyclase superfamily**, consistent with the UniProt-provided family/domain context. (derrer2013theshikimatepathway pages 3-4, derrer2013theshikimatepathway pages 4-5).

### 1) Key concepts and current understanding
#### 1.1 The shikimate pathway and the role of AroB/DHQS
The **shikimate pathway** is a conserved biosynthetic route (present in bacteria, fungi, algae, and plants but absent in animals) that converts central-carbon precursors into **chorismate**, the branch-point precursor for aromatic amino acids and many specialized metabolites. (shende2024theshikimatepathway pages 3-4). 

**AroB/DHQS (3-dehydroquinate synthase)** catalyzes the **second step** of the pathway: conversion of **3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP)** into **3-dehydroquinate (DHQ)**, which is the **first carbocyclic product** (and a key intermediate) of the shikimate pathway. (derrer2013theshikimatepathway pages 3-4, shende2024theshikimatepathway pages 3-4, maeda2012theshikimatepathway pages 7-8).

#### 1.2 Enzymatic reaction, substrate specificity, and products
Across authoritative reviews, DHQS is described as catalyzing:
- **Substrate:** DAHP (a sugar phosphate; often described as the pyranose form)  
- **Product:** **3-dehydroquinate (DHQ)** (carbocyclic intermediate)  
- **Phosphate:** phosphate chemistry is integral; phosphate is eliminated during the mechanism and inorganic phosphate is discussed as a product/activator in mechanistic descriptions. (dev2012structureandfunction pages 2-4, derrer2013theshikimatepathway pages 3-4).

The enzyme’s functional specificity is therefore primarily for **DAHP** within the shikimate pathway (i.e., it is not a broad-spectrum cyclase in this context but a dedicated shikimate-pathway enzyme). (derrer2013theshikimatepathway pages 3-4, shende2024theshikimatepathway pages 3-4).

#### 1.3 Cofactors and mechanistic steps
DHQS is widely characterized as an enzyme with an unusually complex, multi-step catalytic cascade occurring in a single active site:
- It uses **NAD+** catalytically (transient reduction to NADH and reoxidation back to NAD+), and requires a **divalent metal ion**, typically described as **Co2+ or Zn2+**. (derrer2013theshikimatepathway pages 3-4, dev2012structureandfunction pages 2-4, maeda2012theshikimatepathway pages 7-8, derrer2013theshikimatepathway pages 4-5).
- Mechanistic steps described in reviews include an ordered sequence of **alcohol oxidation**, **phosphate elimination**, **carbonyl reduction**, **ring opening**, and **intramolecular aldol condensation/cyclization** to yield DHQ. (dev2012structureandfunction pages 2-4, derrer2013theshikimatepathway pages 3-4, shende2024theshikimatepathway pages 3-4).

A high-level mechanistic consensus is that the enzyme initiates a redox-triggered cascade that yields the carbocycle while suppressing side reactions (“shunt” reactions). (shende2024theshikimatepathway pages 3-4).

#### 1.4 Quantitative enzymology (comparative, conserved bacterial DHQS)
While not specific to *P. putida* KT2440, bacterial DHQS enzymes share conserved chemistry and cofactor usage; thus kinetic data from well-studied bacterial homologs provide useful bounds on expected catalytic behavior. For *Mycobacterium tuberculosis* DHQS, a review summarizes reported values **KM(DAHP) = 6.3 µM**, **KM(NAD+) = 70 µM**, and **kcat ≈ 0.63 s−1**, and also notes EDTA sensitivity with best restoration by **Co2+** (and partial support by other divalent cations, with Zn often present). (nunes2020mycobacteriumtuberculosisshikimate pages 10-12).

### 2) aroB (PP_5078) functional annotation in *P. putida* KT2440
#### 2.1 Biological function and pathway placement
Given the direct PP_5078→aroB mapping and the conserved reaction, **aroB (PP_5078)** in KT2440 is best annotated as a **cytosolic metabolic enzyme of the shikimate pathway** catalyzing **DAHP → DHQ**. (lopezlara2020influenceofrehydration pages 2-4, derrer2013theshikimatepathway pages 3-4, shende2024theshikimatepathway pages 3-4).

In bacteria, the shikimate pathway supplies **chorismate**, which supports aromatic amino acid biosynthesis and numerous downstream aromatic metabolites. (shende2024theshikimatepathway pages 3-4). In *P. putida*, this central role underpins why aroB is frequently targeted in metabolic engineering to raise flux to aromatic products. (ling2022muconicacidproduction pages 1-2, camposmagana2024combinatorialengineeringreveals pages 1-4).

#### 2.2 Cellular localization and site of action
No retrieved source provided a direct experimental subcellular localization assay for KT2440 AroB (e.g., fractionation, microscopy tagging). However, the enzyme acts on soluble cytosolic metabolites (DAHP, NAD+, divalent cations), and DHQS is treated in the literature as a **soluble, intracellular (cytosolic) enzyme** of central metabolism. This inference is consistent with the enzyme’s chemistry and its use in intracellular pathway engineering. (derrer2013theshikimatepathway pages 3-4, dev2012structureandfunction pages 2-4, ling2022muconicacidproduction pages 1-2).

#### 2.3 Expression and physiological context in KT2440
In a KT2440 desiccation/rehydration transcriptome study, **aroB (PP_5078)** is reported among genes in an overrepresented amino-acid biosynthesis functional group and is described as **upregulated** during resuscitation after desiccation. (lopezlara2020influenceofrehydration pages 2-4). The same excerpt links this group to aromatic amino acid biosynthesis (phenylalanine/tyrosine), consistent with increased demand for shikimate-pathway flux during recovery. (lopezlara2020influenceofrehydration pages 2-4).

### 3) Recent developments and latest research (prioritizing 2023–2024)
#### 3.1 2024 mechanistic/structural synthesis of DHQS and pathway context
A 2024 *Natural Product Reports* review (“The shikimate pathway: gateway to metabolic diversity”) explicitly highlights that mechanistic proposals for DHQS are informed by **high-resolution crystal structures** of DHQS in complex with **metals, nicotinamide cofactors, and substrate-based inhibitors**, and summarizes DHQS as a multi-step enzyme stabilizing intermediates and minimizing off-pathway reactions. (shende2024theshikimatepathway pages 3-4). This consolidates the current understanding that DHQS is not merely a simple cyclase but a tightly choreographed redox-enabled cyclization catalyst.

#### 3.2 2024–2025 systems metabolic engineering in *P. putida*: aroB emerges as a bottleneck
A 2024 bioRxiv preprint applying combinatorial Design-of-Experiments (DoE) to *P. putida* shikimate and pABA pathways identifies **aroB expression** as a **significant limiting factor** for **para-aminobenzoic acid (pABA)** production. (camposmagana2024combinatorialengineeringreveals pages 1-4). Quantitatively, from 14 representative strains spanning a theoretical 512-combination design space, the authors report **2–186.2 mg/L** pABA in the initial screen and **232.1 mg/L** after a second engineering round guided by modeling. (camposmagana2024combinatorialengineeringreveals pages 1-4). A peer-reviewed continuation (2025) reports the same workflow and titers and again identifies **aroB** as a critical bottleneck (included here for completeness beyond the user’s 2024 window). (camposmagana2025combinatorialengineeringpinpoints pages 1-2).

This line of work supports an expert interpretation that, in *P. putida*, DHQS capacity can constrain carbon throughput through the shikimate node when production goals demand high chorismate-derived flux.

#### 3.3 2024 microbial production (other hosts) reinforces aroB as a common engineering lever
In 2024, *Corynebacterium crenatum* was engineered for L-tyrosine production by, among other interventions, overexpressing **aroB/aroD/aroE**. Reported titers reached **6.42 g/L** in shake flasks and **34.6 g/L** in fed-batch fermentation, with the mixed carbon-source strategy giving **16.9% higher** L-tyrosine than glucose alone in flask conditions. (yang2024metabolicengineeringof pages 1-3). While not *P. putida*, this is relevant as a recent demonstration of real-world pathway design where increasing flux through the DAHP→DHQ→shikimate segment (including DHQS) is part of achieving industrially relevant aromatic amino acid titers.

### 4) Current applications and real-world implementations
#### 4.1 *P. putida* KT2440 as a chassis for shikimate-derived bioproducts
A prominent implementation is muconic acid production in engineered *P. putida* KT2440. In this Nature Communications study (published Aug 2022; still actively cited as an implementation benchmark), the authors state that **overexpression of aroB encoding the native 3-dehydroquinate synthase** enabled efficient muconic acid production from mixed sugars. (ling2022muconicacidproduction pages 1-2). They report **33.7 g/L muconate**, **0.18 g/L/h productivity**, and **46% molar yield** (reported as **92% of maximum theoretical yield**). (ling2022muconicacidproduction pages 1-2). These data demonstrate industrially relevant titers/productivities and position aroB as a concrete intervention point in deployed strain designs.

#### 4.2 pABA as an industrial intermediate
pABA is described as a widely used industrial intermediate, and the 2024 DoE study in *P. putida* provides a quantitative example showing that systematic tuning of shikimate-pathway gene expression can move pABA titers across two orders of magnitude, with aroB identified as a key bottleneck. (camposmagana2024combinatorialengineeringreveals pages 1-4).

### 5) Expert opinions and analysis (authoritative synthesis)
Authoritative reviews emphasize two main reasons DHQS/AroB is strategically important:
1. **Pathway control point:** DHQS forms the **first carbocyclic intermediate** and sits early in the pathway, so it can become rate-limiting when high flux is required for aromatic amino acids or downstream specialized metabolites. (shende2024theshikimatepathway pages 3-4, camposmagana2024combinatorialengineeringreveals pages 1-4).
2. **Mechanistic complexity enabling inhibitor design:** DHQS has well-defined cofactor and metal requirements and multi-step chemistry; high-resolution structures with cofactors/inhibitors have informed mechanistic models, making DHQS a tractable enzyme for mechanistic interrogation and (in broader contexts) inhibitor development. (shende2024theshikimatepathway pages 3-4, derrer2013theshikimatepathway pages 4-5).

A practical interpretation consistent with recent *P. putida* engineering results is that **aroB expression/capacity often needs explicit optimization** in overproduction settings (e.g., pABA), and can be part of high-performing strain architectures (e.g., muconate). (camposmagana2024combinatorialengineeringreveals pages 1-4, ling2022muconicacidproduction pages 1-2).

### 6) Key statistics and quantitative data from studies (selected)
- **Muconate production in engineered *P. putida* KT2440** with aroB overexpression in the design: **33.7 g/L**, **0.18 g/L/h**, **46% molar yield (92% of theoretical maximum)**. Publication date: Aug 2022. URL: https://doi.org/10.1038/s41467-022-32296-y (ling2022muconicacidproduction pages 1-2).
- **pABA production in *P. putida*** DoE study: initial titers **2–186.2 mg/L**, improved to **232.1 mg/L** after a second engineering round; **aroB identified as bottleneck**. Preprint posted Jun 17, 2024. URL: https://doi.org/10.1101/2024.06.17.599342 (camposmagana2024combinatorialengineeringreveals pages 1-4).
- **Comparative bacterial DHQS kinetics (M. tuberculosis):** **KM(DAHP) 6.3 µM**, **KM(NAD+) 70 µM**, **kcat ~0.63 s−1**; metal dependence with best restoration by Co2+. Publication date: Mar 2020. URL: https://doi.org/10.3390/molecules25061259 (nunes2020mycobacteriumtuberculosisshikimate pages 10-12).

### 7) Summary of functional annotation (for database-style use)
- **Gene / locus / accession:** aroB / PP_5078 / UniProt Q88CV2 (verified in KT2440 context). (lopezlara2020influenceofrehydration pages 2-4)
- **Enzyme name / EC:** 3-dehydroquinate synthase (DHQS) / **EC 4.2.3.4**. (derrer2013theshikimatepathway pages 3-4, maeda2012theshikimatepathway pages 7-8)
- **Primary reaction:** **DAHP → 3-dehydroquinate (DHQ)** (second shikimate step; first carbocyclic product). (derrer2013theshikimatepathway pages 3-4, shende2024theshikimatepathway pages 3-4)
- **Cofactors:** catalytic **NAD+** and a **divalent metal** (commonly Co2+ or Zn2+). (dev2012structureandfunction pages 2-4, derrer2013theshikimatepathway pages 4-5)
- **Pathway:** shikimate pathway → chorismate → aromatic amino acids and diverse aromatic metabolites. (shende2024theshikimatepathway pages 3-4)
- **Cellular location (best-supported):** intracellular/cytosolic enzyme acting on soluble metabolites; direct KT2440 localization experiment not found in retrieved sources. (derrer2013theshikimatepathway pages 3-4, ling2022muconicacidproduction pages 1-2)

### 8) Evidence table (compiled)
| Evidence type | Organism/system | Key finding | Quantitative data (if any) | Publication (authors, year) | URL/DOI |
|---|---|---|---|---|---|
| identity | *Pseudomonas putida* KT2440 | PP_5078 is explicitly annotated as **aroB**, encoding **3-dehydroquinate synthase**; reported as upregulated during recovery from desiccation/rehydration, supporting the locus-to-function mapping for the target gene/protein (lopezlara2020influenceofrehydration pages 2-4) | Microarray study with triplicate analyses; numeric fold-change not given in excerpt (lopezlara2020influenceofrehydration pages 2-4) | López-Lara et al., 2020 | https://doi.org/10.1186/s13213-020-01596-3 |
| identity/pathway role | *Pseudomonas putida* KT2440 engineered for muconate production | The native **aroB** in *P. putida* KT2440 is identified as encoding **3-dehydroquinate synthase**; overexpression improved flux to shikimate-pathway-derived muconic acid (ling2022muconicacidproduction pages 1-2) | Muconate production reached **33.7 g/L**, **0.18 g/L/h**, **46% molar yield** (**92% of theoretical maximum**) in engineered strains that included aroB overexpression (ling2022muconicacidproduction pages 1-2) | Ling et al., 2022 | https://doi.org/10.1038/s41467-022-32296-y |
| mechanism | Bacterial DHQS/AroB (reviewed across taxa) | DHQS/AroB (EC 4.2.3.4) catalyzes conversion of **DAHP to 3-dehydroquinate (DHQ)**, the second step of the shikimate pathway and first carbocyclic intermediate-forming reaction; belongs to the **sugar phosphate cyclase superfamily** (derrer2013theshikimatepathway pages 3-4, shende2024theshikimatepathway pages 3-4) | Reaction-level annotation; no organism-specific kinetic value in these excerpts (derrer2013theshikimatepathway pages 3-4, shende2024theshikimatepathway pages 3-4) | Derrer et al., 2013; Shende et al., 2024 | https://doi.org/10.2741/4155; https://doi.org/10.1039/d3np00037k |
| mechanism/cofactors | Bacterial DHQS/AroB (reviewed across taxa) | Catalysis requires **NAD+** and a **divalent metal ion**; **Co2+** and **Zn2+** are the principal reported cofactors. Mechanism proceeds through oxidation, phosphate elimination, reduction, ring opening, and intramolecular aldol cyclization (derrer2013theshikimatepathway pages 3-4, dev2012structureandfunction pages 2-4, maeda2012theshikimatepathway pages 7-8, derrer2013theshikimatepathway pages 4-5) | Mechanistic sequence of ~5 chemical steps in one active site; catalytic NAD+ use noted (dev2012structureandfunction pages 2-4) | Dev et al., 2012; Derrer et al., 2013; Maeda & Dudareva, 2012 | https://doi.org/10.2174/157489312803900983; https://doi.org/10.2741/4155; https://doi.org/10.1146/annurev-arplant-042811-105439 |
| mechanism/kinetics | *Mycobacterium tuberculosis* DHQS (comparative authoritative source for conserved AroB chemistry) | AroB/DHQS performs multiple transformations in one active site; kinetics and metal dependence support the conserved bacterial mechanism for DHQS enzymes (nunes2020mycobacteriumtuberculosisshikimate pages 10-12) | **KM(DAHP) = 6.3 µM**, **KM(NAD+) = 70 µM**, **kcat ≈ 0.63 s⁻¹**; activity abolished by EDTA and best restored by **Co2+** (nunes2020mycobacteriumtuberculosisshikimate pages 10-12) | Nunes et al., 2020 | https://doi.org/10.3390/molecules25061259 |
| application | *Pseudomonas putida* pABA pathway engineering | Combinatorial engineering identified **aroB** expression as a **significant limiting factor / bottleneck** for para-aminobenzoic acid production in *P. putida*, making DHQS a practical intervention point in strain design (camposmagana2024combinatorialengineeringreveals pages 1-4, camposmagana2024combinatorialengineeringreveals pages 11-14) | Initial strain set produced **2–186.2 mg/L** pABA; second round reached **232.1 mg/L** (reported in related preprint/peer-reviewed continuation) (camposmagana2024combinatorialengineeringreveals pages 1-4, camposmagana2025combinatorialengineeringpinpoints pages 1-2) | Campos-Magaña et al., 2024; Campos-Magaña et al., 2025 | https://doi.org/10.1101/2024.06.17.599342; https://doi.org/10.1186/s13036-025-00553-5 |
| application | *Corynebacterium crenatum* metabolic engineering | Overexpression of **aroB** with **aroD/aroE** was part of a successful aromatic amino acid engineering strategy, showing broader real-world use of DHQS tuning in microbial biomanufacturing (yang2024metabolicengineeringof pages 1-3) | **6.42 g/L** L-tyrosine in shake flask; **34.6 g/L** in fed-batch; **16.9%** higher at 3:1 glucose:mannitol vs glucose alone (yang2024metabolicengineeringof pages 1-3) | Yang et al., 2024 | https://doi.org/10.1186/s12934-024-02564-1 |
| omics | *Pseudomonas putida* KT2440 under desiccation/rehydration | **aroB/PP_5078** was included among genes in an overrepresented amino-acid biosynthesis response, consistent with its role in aromatic amino acid precursor supply through the shikimate pathway (lopezlara2020influenceofrehydration pages 2-4) | Upregulation reported after **18 days desiccation** followed by **20 min** or **24 h** rehydration sampling; no fold-change in excerpt (lopezlara2020influenceofrehydration pages 2-4) | López-Lara et al., 2020 | https://doi.org/10.1186/s13213-020-01596-3 |


*Table: This table compiles key evidence verifying that Pseudomonas putida KT2440 PP_5078 is aroB encoding 3-dehydroquinate synthase, and summarizes its conserved reaction chemistry, cofactors, pathway role, omics support, and quantitative metabolic-engineering applications.*

### 9) Limitations of the current evidence set
- **Direct subcellular localization** (e.g., experimental cytosolic fractionation or fluorescent tagging in KT2440) was not identified in the retrieved texts; localization here is inferred from biochemical role and general bacterial shikimate pathway architecture. (derrer2013theshikimatepathway pages 3-4, ling2022muconicacidproduction pages 1-2)
- **Domain architecture / InterPro/Pfam features** for Q88CV2 were not directly extracted from primary literature in this run; however, the enzyme’s superfamily placement (sugar phosphate cyclase) and conserved mechanistic features are strongly supported by authoritative reviews. (derrer2013theshikimatepathway pages 3-4, derrer2013theshikimatepathway pages 4-5)


References

1. (lopezlara2020influenceofrehydration pages 2-4): Lilia I. López-Lara, Laura A. Pazos-Rojas, Lesther E. López-Cruz, Yolanda E. Morales-García, Verónica Quintero-Hernández, Jesús de la Torre, Pieter van Dillewijn, Jesús Muñoz-Rojas, and Antonino Baez. Influence of rehydration on transcriptome during resuscitation of desiccated pseudomonas putida kt2440. Annals of Microbiology, Sep 2020. URL: https://doi.org/10.1186/s13213-020-01596-3, doi:10.1186/s13213-020-01596-3. This article has 16 citations and is from a peer-reviewed journal.

2. (ling2022muconicacidproduction pages 1-2): Chen Ling, George L. Peabody, Davinia Salvachúa, Young-Mo Kim, Colin M. Kneucker, Christopher H. Calvey, Michela A. Monninger, Nathalie Munoz Munoz, Brenton C. Poirier, Kelsey J. Ramirez, Peter C. St. John, Sean P. Woodworth, Jon K. Magnuson, Kristin E. Burnum-Johnson, Adam M. Guss, Christopher W. Johnson, and Gregg T. Beckham. Muconic acid production from glucose and xylose in pseudomonas putida via evolution and metabolic engineering. Nature Communications, Aug 2022. URL: https://doi.org/10.1038/s41467-022-32296-y, doi:10.1038/s41467-022-32296-y. This article has 141 citations and is from a highest quality peer-reviewed journal.

3. (derrer2013theshikimatepathway pages 3-4): Bianca Derrer, P. Macheroux, and B. Kappes. The shikimate pathway in apicomplexan parasites: implications for drug development. Frontiers in bioscience, 18:944-69, Jun 2013. URL: https://doi.org/10.2741/4155, doi:10.2741/4155. This article has 37 citations and is from a peer-reviewed journal.

4. (derrer2013theshikimatepathway pages 4-5): Bianca Derrer, P. Macheroux, and B. Kappes. The shikimate pathway in apicomplexan parasites: implications for drug development. Frontiers in bioscience, 18:944-69, Jun 2013. URL: https://doi.org/10.2741/4155, doi:10.2741/4155. This article has 37 citations and is from a peer-reviewed journal.

5. (shende2024theshikimatepathway pages 3-4): Vikram V. Shende, Katherine D. Bauman, and Bradley S. Moore. The shikimate pathway: gateway to metabolic diversity. Natural product reports, 41:604-648, Jan 2024. URL: https://doi.org/10.1039/d3np00037k, doi:10.1039/d3np00037k. This article has 173 citations and is from a peer-reviewed journal.

6. (maeda2012theshikimatepathway pages 7-8): Hiroshi Maeda and Natalia Dudareva. The shikimate pathway and aromatic amino acid biosynthesis in plants. Jun 2012. URL: https://doi.org/10.1146/annurev-arplant-042811-105439, doi:10.1146/annurev-arplant-042811-105439. This article has 1905 citations and is from a domain leading peer-reviewed journal.

7. (dev2012structureandfunction pages 2-4): Aditya Dev, Satya Tapas, Shivendra Pratap, and Pravindra Kumar. Structure and function of enzymes of shikimate pathway. Current Bioinformatics, 7:374-391, Nov 2012. URL: https://doi.org/10.2174/157489312803900983, doi:10.2174/157489312803900983. This article has 20 citations and is from a peer-reviewed journal.

8. (nunes2020mycobacteriumtuberculosisshikimate pages 10-12): José E. S. Nunes, Mario A. Duque, Talita F. de Freitas, Luiza Galina, Luis F. S. M. Timmers, Cristiano V. Bizarro, Pablo Machado, Luiz A. Basso, and Rodrigo G. Ducati. Mycobacterium tuberculosis shikimate pathway enzymes as targets for the rational design of anti-tuberculosis drugs. Molecules, 25:1259, Mar 2020. URL: https://doi.org/10.3390/molecules25061259, doi:10.3390/molecules25061259. This article has 74 citations.

9. (camposmagana2024combinatorialengineeringreveals pages 1-4): Marco A Campos-Magaña, Sara Moreno-Paz, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering reveals shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.17.599342, doi:10.1101/2024.06.17.599342. This article has 0 citations.

10. (camposmagana2025combinatorialengineeringpinpoints pages 1-2): Marco A Campos-Magaña, Sara Moreno-Paz, Maria Martin-Pascual, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering pinpoints shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. Journal of Biological Engineering, Sep 2025. URL: https://doi.org/10.1186/s13036-025-00553-5, doi:10.1186/s13036-025-00553-5. This article has 0 citations and is from a peer-reviewed journal.

11. (yang2024metabolicengineeringof pages 1-3): Gang Yang, Sicheng Xiong, Mingzhu Huang, Bin Liu, Yanna Shao, and Xuelan Chen. Metabolic engineering of corynebacterium crenatum for enhanced l-tyrosine production from mannitol and glucose. Microbial Cell Factories, Oct 2024. URL: https://doi.org/10.1186/s12934-024-02564-1, doi:10.1186/s12934-024-02564-1. This article has 7 citations and is from a peer-reviewed journal.

12. (camposmagana2024combinatorialengineeringreveals pages 11-14): Marco A Campos-Magaña, Sara Moreno-Paz, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering reveals shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.17.599342, doi:10.1101/2024.06.17.599342. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](aroB-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. lopezlara2020influenceofrehydration pages 2-4
2. ling2022muconicacidproduction pages 1-2
3. shende2024theshikimatepathway pages 3-4
4. nunes2020mycobacteriumtuberculosisshikimate pages 10-12
5. camposmagana2024combinatorialengineeringreveals pages 1-4
6. camposmagana2025combinatorialengineeringpinpoints pages 1-2
7. yang2024metabolicengineeringof pages 1-3
8. dev2012structureandfunction pages 2-4
9. derrer2013theshikimatepathway pages 3-4
10. derrer2013theshikimatepathway pages 4-5
11. maeda2012theshikimatepathway pages 7-8
12. camposmagana2024combinatorialengineeringreveals pages 11-14
13. https://doi.org/10.1038/s41467-022-32296-y
14. https://doi.org/10.1101/2024.06.17.599342
15. https://doi.org/10.3390/molecules25061259
16. https://doi.org/10.1186/s13213-020-01596-3
17. https://doi.org/10.2741/4155;
18. https://doi.org/10.1039/d3np00037k
19. https://doi.org/10.2174/157489312803900983;
20. https://doi.org/10.1146/annurev-arplant-042811-105439
21. https://doi.org/10.1101/2024.06.17.599342;
22. https://doi.org/10.1186/s13036-025-00553-5
23. https://doi.org/10.1186/s12934-024-02564-1
24. https://doi.org/10.1186/s13213-020-01596-3,
25. https://doi.org/10.1038/s41467-022-32296-y,
26. https://doi.org/10.2741/4155,
27. https://doi.org/10.1039/d3np00037k,
28. https://doi.org/10.1146/annurev-arplant-042811-105439,
29. https://doi.org/10.2174/157489312803900983,
30. https://doi.org/10.3390/molecules25061259,
31. https://doi.org/10.1101/2024.06.17.599342,
32. https://doi.org/10.1186/s13036-025-00553-5,
33. https://doi.org/10.1186/s12934-024-02564-1,