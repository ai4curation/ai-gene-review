---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-04T17:00:55.753994'
end_time: '2026-07-04T17:22:13.093109'
duration_seconds: 1277.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: tax-2
  gene_symbol: tax-2
  uniprot_accession: G5EEE2
  protein_description: 'SubName: Full=Cyclic nucleotide-binding domain-containing
    protein {ECO:0000313|EMBL:CAB04328.1};'
  gene_info: Name=tax-2 {ECO:0000313|EMBL:CAB04328.1, ECO:0000313|WormBase:F36F2.5};
    ORFNames=CELE_F36F2.5 {ECO:0000313|EMBL:CAB04328.1}, F36F2.5 {ECO:0000313|WormBase:F36F2.5};
  organism_full: Caenorhabditis elegans.
  protein_family: Not specified in UniProt
  protein_domains: CNG_cation_channel. (IPR050866); cNMP-bd_CS. (IPR018488); cNMP-bd_dom.
    (IPR000595); cNMP-bd_dom_sf. (IPR018490); Ion_trans_dom. (IPR005821)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: tax-2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: tax-2-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** G5EEE2
- **Protein Description:** SubName: Full=Cyclic nucleotide-binding domain-containing protein {ECO:0000313|EMBL:CAB04328.1};
- **Gene Information:** Name=tax-2 {ECO:0000313|EMBL:CAB04328.1, ECO:0000313|WormBase:F36F2.5}; ORFNames=CELE_F36F2.5 {ECO:0000313|EMBL:CAB04328.1}, F36F2.5 {ECO:0000313|WormBase:F36F2.5};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CNG_cation_channel. (IPR050866); cNMP-bd_CS. (IPR018488); cNMP-bd_dom. (IPR000595); cNMP-bd_dom_sf. (IPR018490); Ion_trans_dom. (IPR005821)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tax-2" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tax-2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tax-2** (gene ID: tax-2, UniProt: G5EEE2) in worm.

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
- **UniProt Accession:** G5EEE2
- **Protein Description:** SubName: Full=Cyclic nucleotide-binding domain-containing protein {ECO:0000313|EMBL:CAB04328.1};
- **Gene Information:** Name=tax-2 {ECO:0000313|EMBL:CAB04328.1, ECO:0000313|WormBase:F36F2.5}; ORFNames=CELE_F36F2.5 {ECO:0000313|EMBL:CAB04328.1}, F36F2.5 {ECO:0000313|WormBase:F36F2.5};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CNG_cation_channel. (IPR050866); cNMP-bd_CS. (IPR018488); cNMP-bd_dom. (IPR000595); cNMP-bd_dom_sf. (IPR018490); Ion_trans_dom. (IPR005821)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tax-2" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tax-2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tax-2** (gene ID: tax-2, UniProt: G5EEE2) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: *tax-2* (UniProt G5EEE2) in *Caenorhabditis elegans*

## 1. Gene Identity and Protein Overview

The *tax-2* gene (locus F36F2.5, also designated CELE_F36F2.5) in *Caenorhabditis elegans* encodes the β (B-type) subunit of a cyclic nucleotide-gated (CNG) cation channel (mckemy2007temperaturesensingacross pages 3-4, ferkey2021chemosensorysignaltransduction pages 14-15). This assignment is fully consistent with the UniProt G5EEE2 entry, which lists domains for CNG_cation_channel (IPR050866), cNMP-binding domain (IPR000595), cNMP-binding domain superfamily (IPR018490), cNMP-binding domain signature (IPR018488), and ion transport domain (IPR005821). The gene name *tax-2* derives from its original identification in screens for mutants with abnormal thermotaxis (thermotaxis abnormal), though the gene has subsequently been shown to play essential roles in multiple sensory modalities.

TAX-2 partners with TAX-4 (the α subunit) to form the principal heteromeric CNG channel required for sensory transduction across a broad array of *C. elegans* sensory neurons (bargmann2006chemosensationinc. pages 10-12, ferkey2021chemosensorysignaltransduction pages 14-15). The TAX-2/TAX-4 channel is structurally most similar to vertebrate rod photoreceptor CNG channels (mckemy2007temperaturesensingacross pages 3-4).

## 2. Molecular Function and Channel Biophysics

### 2.1 Primary Function

TAX-2 functions as the obligate β subunit of a heteromeric cGMP-gated nonselective cation channel. The channel is directly gated by intracellular cyclic GMP (cGMP), converting changes in intracellular cGMP concentration—produced or consumed by upstream guanylyl cyclases and phosphodiesterases—into ion flux across the plasma membrane, thereby depolarizing sensory neurons and permitting calcium entry (mckemy2007temperaturesensingacross pages 3-4, li2024inhibitionofa pages 6-7, bargmann2006chemosensationinc. pages 10-12).

### 2.2 Subunit Composition and Biophysical Properties

Heterologous expression studies (in HEK293 cells) have established the following key biophysical properties:

- **TAX-4 homomeric channels** can form functional channels independently, exhibiting high cGMP sensitivity (K_D ≈ 4 × 10⁻⁷ M) with poor sensitivity to cAMP (mckemy2007temperaturesensingacross pages 3-4).
- **TAX-2 cannot form functional channels on its own** (mckemy2007temperaturesensingacross pages 3-4).
- **TAX-2/TAX-4 heteromeric channels** exhibit approximately 25-fold reduced cGMP sensitivity compared to TAX-4 homomers while maintaining selectivity for cGMP over cAMP (mckemy2007temperaturesensingacross pages 3-4). They are highly permeable to calcium but less sensitive to divalent ion block than TAX-4 homomers (mckemy2007temperaturesensingacross pages 3-4). TAX-4 homomeric channels stay open approximately seven times longer than heteromeric TAX-4/TAX-2 channels, with heteromeric channels having approximately 10-fold lower cGMP affinity (ferkey2021chemosensorysignaltransduction pages 14-15).

These properties indicate that TAX-2 modulates channel kinetics and sensitivity, likely tuning the dynamic range of sensory responses in vivo. The following table summarizes the biophysical comparison:

| Property | TAX-4 Homomeric Channel | TAX-2/TAX-4 Heteromeric Channel |
|---|---|---|
| cGMP sensitivity (KD) | High sensitivity; KD ≈ 4 × 10⁻⁷ M for cGMP (mckemy2007temperaturesensingacross pages 3-4) | ~25-fold lower cGMP sensitivity than TAX-4 alone; still cGMP-gated (mckemy2007temperaturesensingacross pages 3-4) |
| cAMP sensitivity | Poor sensitivity to cAMP; strongly prefers cGMP (mckemy2007temperaturesensingacross pages 3-4) | Retains selectivity for cGMP over cAMP (mckemy2007temperaturesensingacross pages 3-4) |
| Calcium permeability | Calcium permeable (mckemy2007temperaturesensingacross pages 3-4) | Highly calcium permeable; supports Ca²⁺ influx in sensory transduction (mckemy2007temperaturesensingacross pages 3-4) |
| Divalent ion block sensitivity | More sensitive to divalent ion block (mckemy2007temperaturesensingacross pages 3-4) | Less sensitive to divalent ion block than TAX-4 alone (mckemy2007temperaturesensingacross pages 3-4) |
| Ability to form functional channels independently | Yes; TAX-4 alone can form a functional channel in heterologous expression systems (mckemy2007temperaturesensingacross pages 3-4) | Yes as a co-expressed heteromer; requires both TAX-2 and TAX-4 for this channel composition (mckemy2007temperaturesensingacross pages 3-4, ferkey2021chemosensorysignaltransduction pages 14-15) |
| Open time | Longer open time; about 7-fold longer than heteromeric TAX-2/TAX-4 channels (ferkey2021chemosensorysignaltransduction pages 14-15) | Shorter open time than TAX-4 homomers (ferkey2021chemosensorysignaltransduction pages 14-15) |
| Structural similarity | CNG channel α-like subunit; channel complex is structurally similar to rod photoreceptor CNG channels (mckemy2007temperaturesensingacross pages 3-4) | Heteromeric CNG channel most similar to rod photoreceptor channels; TAX-2 is the β-subunit partner (mckemy2007temperaturesensingacross pages 3-4) |


*Table: This table compares the key biophysical features of TAX-4 homomeric channels and TAX-2/TAX-4 heteromeric channels in C. elegans. It is useful for distinguishing the specific functional contribution of TAX-2 as the β-subunit in the sensory CNG channel complex.*

### 2.3 Alternative Subunit Partnerships

Recent work has revealed that TAX-2 can function either with TAX-4 or with alternative α subunits such as CNG-3. In AFD thermosensory neurons, TAX-2 is required for tactile-dependent locomotion modulation, but TAX-4 is dispensable for this process, suggesting that TAX-2 can pair with CNG-3 or other α subunits to form functionally distinct channel complexes depending on the sensory context (rosero2026afdthermosensoryneurons pages 13-14).

## 3. Expression Pattern and Subcellular Localization

### 3.1 Neuronal Expression

TAX-2 is expressed in a broad set of sensory neurons in the amphid and other sensory organs of *C. elegans*. These include AWC (olfactory neurons for volatile attractants), ASE (gustatory neurons for water-soluble chemicals and salts), AWB (olfactory avoidance neurons for volatile repellents), AFD (thermosensory neurons), BAG (CO₂-sensing neurons), ASG, ASI, ASJ, ASK (chemosensory and neuroendocrine neurons), and ADE neurons (ferkey2021chemosensorysignaltransduction pages 14-15, mckemy2007temperaturesensingacross pages 3-4, rosero2026afdthermosensoryneurons pages 14-15). TAX-2/TAX-4 channels are also expressed in body cavity neurons AQR, PQR, and URX, which function as oxygen sensors exposed to pseudocoelomic fluid (menini2009theneurobiologyof pages 36-38).

### 3.2 Subcellular Localization

TAX-2 protein is localized to **sensory cilia and dendritic structures** of sensory neurons—the precise sites where environmental stimuli are transduced into electrical signals (mckemy2007temperaturesensingacross pages 3-4, bargmann2006chemosensationinc. pages 10-12). The channel is primarily found in cilia rather than in axonal compartments (bargmann2006chemosensationinc. pages 10-12). The specific subdomain localization within cilia is neuron-specific and functionally important (ferkey2021chemosensorysignaltransduction pages 14-15). Notably, *tax-2* and *tax-4* mutant cilia retain normal structural morphology, normal dye uptake, and normal intraflagellar transport, demonstrating that the channel functions downstream of ciliary structure rather than being required for cilia formation per se (li2024inhibitionofa pages 7-8).

The following table summarizes TAX-2 expression across neuron types and the corresponding sensory modalities:

| Neuron | Sensory Modality | Upstream Guanylyl Cyclase(s) | Biological Process | Key Evidence/References |
|---|---|---|---|---|
| AWC | Olfaction; volatile attractants | ODR-1, DAF-11 | Odor-evoked cGMP signaling gates TAX-2/TAX-4 to drive chemotaxis; also contributes to activity-dependent gene expression and odor plasticity | tax-2 expressed in AWC; TAX-2/TAX-4 act downstream of GPCR/G protein signaling with ODR-1 and DAF-11 in AWC olfaction (bargmann2006chemosensationinc. pages 10-12, ferkey2021chemosensorysignaltransduction pages 14-15) |
| ASE | Gustation; water-soluble chemicals, salt, alkalinity | GCY-14 for alkalinity; other ASE rGCs not fully specified here | Salt chemotaxis and pH/alkalinity responses require TAX-2/TAX-4-mediated cGMP signaling | tax-2 expressed in ASE; TAX-2/TAX-4 required for chemotaxis to water-soluble compounds and calcium responses to NaCl/pH changes (bargmann2006chemosensationinc. pages 10-12, ferkey2021chemosensorysignaltransduction pages 14-15, bargmann2006chemosensationinc. pages 1-3) |
| AWB | Olfactory avoidance; volatile repellents | Not clearly resolved in the retrieved evidence; cGMP pathway upstream likely includes GPCR-regulated GC signaling | Avoidance of volatile repellents and modulation of odor responses | tax-2 expressed in AWB; TAX-2/TAX-4 required for AWB-mediated avoidance and localize to sensory cilia; PDE-5 also modulates AWB olfactory signaling (bargmann2006chemosensationinc. pages 10-12, ferkey2021chemosensorysignaltransduction pages 14-15, galande2025rolesofcyclic pages 12-13) |
| AFD | Thermosensation | GCY-8, GCY-18, GCY-23 | Thermotaxis and thermotransduction through cGMP-triggered opening of TAX-2/TAX-4, causing Ca2+ fluctuations | tax-2 expressed in AFD; TAX-2/TAX-4 localized to cilia/dendrites; AFD thermosensation uses GCY-8/18/23 upstream of the channel (mckemy2007temperaturesensingacross pages 3-4, galande2025rolesofcyclic pages 15-16) |
| BAG | CO2 sensing; also implicated in O2-related circuit functions | GCY-9 | CO2-evoked sensory signaling and behavioral plasticity | tax-2 expressed in BAG; recent pathway summaries place GCY-9 upstream of TAX-2/TAX-4 in BAG CO2 signaling (rosero2026afdthermosensoryneurons pages 14-15, ferkey2021chemosensorysignaltransduction pages 14-15, galande2025rolesofcyclic pages 15-16) |
| AQR/PQR/URX | Oxygen sensing / aerotaxis | GCY-35, GCY-36 | Body-cavity neuron O2 sensing; cGMP opens TAX-2/TAX-4 to control aerotaxis | TAX-2/TAX-4 function downstream of soluble guanylyl cyclases GCY-35/36 in AQR/PQR/URX oxygen sensing (menini2009theneurobiologyof pages 36-38, galande2025rolesofcyclic pages 7-9) |
| ASG | Chemosensory / sensory integration | Not specified in retrieved evidence | Likely participates in TAX-2/TAX-4-dependent sensory signaling; specific pathway assignment remains limited in the retrieved literature | tax-2 expression reported in ASG, but neuron-specific upstream GC and process were not defined in the retrieved evidence (ferkey2021chemosensorysignaltransduction pages 14-15) |
| ASI | Neuroendocrine chemosensory signaling | DAF-11 implicated in dauer/pheromone-related cGMP signaling | Dauer regulation, sensory integration, and regulation of daf-7 expression | tax-2 expressed in ASI; TAX-2/TAX-4 contribute to dauer-related cGMP signaling and regulation of sensory gene expression/neuroendocrine outputs (ferkey2021chemosensorysignaltransduction pages 19-20, ferkey2021chemosensorysignaltransduction pages 14-15) |
| ASJ | Sensory/neuroendocrine signaling; thermo/photo-related cGMP pathways in broader literature | Not clearly specified in retrieved tax-2-centered evidence | Regulation of daf-7 expression and sensory-state signaling; recent PDE literature implicates ASJ cGMP dynamics | tax-2 expression reported in ASJ; channel complex regulates gene expression including daf-7 in ASJ/ASI, but specific upstream GC was not resolved in the retrieved evidence (ferkey2021chemosensorysignaltransduction pages 14-15, galande2025rolesofcyclic pages 9-10) |
| ASK | Chemosensory / pheromone-related signaling | DAF-11 implicated in pheromone/dauer context | Dauer pheromone signaling and sensory integration | tax-2 expressed in ASK; DAF-11 and G proteins act in pheromone signaling contexts where TAX-2/TAX-4 function downstream in dauer-related pathways (ferkey2021chemosensorysignaltransduction pages 19-20, ferkey2021chemosensorysignaltransduction pages 14-15) |
| ADE | Sensory neuron; modality not well defined here | Not specified in retrieved evidence | tax-2 expression indicates possible CNG-dependent sensory signaling, but a precise TAX-2-specific function in ADE was not resolved in the retrieved sources | ADE listed among tax-2-expressing neurons; specific upstream GC and function not defined in retrieved evidence (rosero2026afdthermosensoryneurons pages 14-15, ferkey2021chemosensorysignaltransduction pages 14-15) |


*Table: This table summarizes where TAX-2 is expressed in C. elegans and links each neuron type to its sensory modality, likely upstream guanylyl cyclases, and major biological roles. It is useful for mapping TAX-2 onto specific cGMP-dependent sensory circuits while distinguishing well-supported assignments from areas where evidence remains limited.*

## 4. Signaling Pathways

TAX-2/TAX-4 channels serve as the critical downstream effector in multiple cGMP-dependent sensory transduction cascades. The general signaling logic is conserved across modalities: an environmental stimulus activates guanylyl cyclases (either receptor-type or soluble), elevating intracellular cGMP, which directly gates TAX-2/TAX-4 channels to allow cation influx and neuronal depolarization.

### 4.1 Chemosensation (Olfaction and Gustation)

In AWC olfactory neurons, odorants are detected by G protein-coupled receptors (GPCRs) that activate the Gα protein ODR-3. ODR-3 regulates cGMP levels by activating receptor guanylyl cyclases ODR-1 and DAF-11 (which likely function as heterodimers), and/or modulating phosphodiesterases. The resulting increase in cGMP directly opens TAX-2/TAX-4 channels to depolarize the neuron (bargmann2006chemosensationinc. pages 10-12). In ASE gustatory neurons, TAX-2/TAX-4 channels are required for calcium flux responses to NaCl concentration changes and pH stimuli (ferkey2021chemosensorysignaltransduction pages 14-15). *tax-2* mutants are defective in AWC-mediated chemotaxis to volatile odors, ASE-mediated chemotaxis to water-soluble attractants, and AWB-mediated avoidance of volatile repellents (bargmann2006chemosensationinc. pages 10-12).

### 4.2 Thermosensation

In AFD thermosensory neurons, temperature-responsive receptor guanylyl cyclases GCY-8, GCY-18, and GCY-23 produce cGMP in response to warming, which gates TAX-2/TAX-4 channels and promotes intracellular Ca²⁺ fluctuations necessary for thermotaxis behavior (mckemy2007temperaturesensingacross pages 3-4). *tax-2* mutants show thermotactic deficits similar to those observed after AFD neuron ablation (mckemy2007temperaturesensingacross pages 3-4).

### 4.3 Oxygen Sensing (Aerotaxis)

In body cavity neurons AQR, PQR, and URX, dissolved oxygen activates soluble guanylyl cyclases GCY-35 and GCY-36, producing cGMP that opens TAX-2/TAX-4 channels to mediate aerotaxis behavior (menini2009theneurobiologyof pages 36-38, galande2025rolesofcyclic pages 7-9).

### 4.4 CO₂ Sensing

In BAG neurons, the soluble guanylyl cyclase GCY-9 produces cGMP in response to CO₂, activating TAX-2/TAX-4 channels for CO₂-evoked behavioral responses (galande2025rolesofcyclic pages 15-16).

### 4.5 Negative Feedback by Phosphodiesterases

Cyclic nucleotide phosphodiesterases PDE-1, PDE-2, and PDE-5 hydrolyze cGMP to provide negative feedback regulation of TAX-2/TAX-4 channel activity. In PQR oxygen-sensing neurons, PDE-1 restores cGMP to baseline after oxygen stimulation (galande2025rolesofcyclic pages 7-9). In AFD thermosensory neurons, PDE-1 and PDE-5 regulate cGMP in neuronal receptive endings, while PDE-2 is required for recovery and adaptation phases of thermotransduction (galande2025rolesofcyclic pages 15-16, galande2025rolesofcyclic pages 7-9, galande2025rolesofcyclic pages 12-13). In AWB olfactory neurons, PDE-5 modulates responses to low concentrations of odorants (galande2025rolesofcyclic pages 12-13). Complete disruption of PDE activity (quadruple pde-1:pde-2:pde-3:pde-5 mutants) results in elevated cGMP levels and loss of chemotactic responses to alkaline pH, phenocopying TAX-2/TAX-4 channel defects (galande2025rolesofcyclic pages 13-15).

## 5. Downstream Physiological Roles

### 5.1 Dauer Formation

*tax-2* mutants exhibit a weak dauer-constitutive (Daf-c) phenotype, particularly at high temperatures, indicating a role in the cGMP signaling branch of dauer formation (fielenbach2008c.elegansdauer pages 3-5, bargmann2006chemosensationinc. pages 10-12, fielenbach2008c.elegansdauer pages 2-3). This phenotype is less severe than that of *daf-11* guanylyl cyclase mutants, which produce potent Daf-c phenotypes, placing TAX-2/TAX-4 downstream of DAF-11 in the dauer signaling pathway (fielenbach2008c.elegansdauer pages 2-3). The cGMP pathway intersects with insulin/IGF-1-like signaling (IIS) and TGF-β signaling to control the dauer decision (fielenbach2008c.elegansdauer pages 3-5).

### 5.2 Longevity

Loss of TAX-2/TAX-4 channel function extends *C. elegans* lifespan. Mutations in *tax-2* extend lifespan particularly at low temperatures (lin2017longevitycontrolby pages 1-2). The *tax-4(p678)* mutation extends mean lifespan from approximately 19 to 30 days (li2024inhibitionofa pages 6-7). Mechanistically, suppressed CNG channel activity on sensory cilia non-cell-autonomously activates the unfolded protein response of the endoplasmic reticulum (UPR^ER) in intestinal cells through the IRE-1–XBP-1 signaling pathway, promoting resistance to age-dependent protein aggregation and extending lifespan (li2024inhibitionofa pages 6-7, li2024inhibitionofa pages 1-2). This establishes a sensory neuron-to-intestine signaling axis mediated by TAX-2/TAX-4 channel activity.

### 5.3 Activity-Dependent Gene Expression

TAX-2/TAX-4 channels regulate activity-dependent gene expression in sensory neurons. In AWC neurons, channel activity controls expression of the receptor gene *str-2*, which is important for odor discrimination and olfactory neuron identity specification (ferkey2021chemosensorysignaltransduction pages 14-15, bargmann2006chemosensationinc. pages 10-12). In ASI and ASJ neurons, the channels regulate expression of *daf-7* (TGF-β), a key neuroendocrine signal for dauer and reproductive growth decisions (ferkey2021chemosensorysignaltransduction pages 14-15).

### 5.4 Tactile-Dependent Behavioral Modulation

A recent study has uncovered an unexpected role for TAX-2 in the AFD thermosensory neuron beyond its canonical function in temperature detection: TAX-2 mediates tactile-dependent locomotion modulation. Intriguingly, TAX-4 is dispensable for this process, and TAX-2 may function with alternative α subunits such as CNG-3 in this context (rosero2026afdthermosensoryneurons pages 13-14). This modulation requires electrical synapses (innexins) between AFD and the AIB interneuron, indicating integration of TAX-2-dependent signals into broader circuit-level processing.

## 6. Genetic Alleles and Mutant Phenotypes

Several *tax-2* alleles have been characterized: *tax-2(p694)* is the canonical loss-of-function allele used in most studies of CNG channel function and sensory signaling (li2024inhibitionofa pages 7-8); *tax-2(p691)* and *tax-2(ot25)* are additional alleles (hill2024molecularandneuronal pages 84-89). The engineered phosphomutant *tax-2(oy191[S727A])* has been investigated in the context of rapid temperature adaptation in AFD neurons, where it does not affect rapid adaptation responses (hill2024molecularandneuronal pages 84-89). This suggests that phosphorylation of Ser727 may regulate other aspects of TAX-2 function or contribute to slower forms of sensory plasticity.

## 7. Evolutionary Context

TAX-2 is structurally most similar to β subunits of CNG channels expressed in vertebrate rod photoreceptors (mckemy2007temperaturesensingacross pages 3-4). The TAX-2/TAX-4 heteromeric channel shares homology with human CNG channels (li2024inhibitionofa pages 6-7). The conservation of cGMP-gated channel-dependent sensory transduction from nematodes to vertebrates underscores the ancient evolutionary origin of this signaling mechanism. Orthologs of *tax-2* and *tax-4* in parasitic nematodes such as *Brugia malayi* can partially rescue sensory defects in *C. elegans* mutants, confirming functional conservation across nematode species (rosero2026afdthermosensoryneurons pages 13-14).

## 8. Summary

*tax-2* encodes the β subunit of the principal cGMP-gated cation channel in *C. elegans* sensory neurons. Together with the α subunit TAX-4, it forms a heteromeric channel localized to sensory cilia that serves as the critical downstream effector in multiple cGMP-dependent signal transduction pathways. These pathways mediate chemosensation, thermosensation, oxygen sensing, and CO₂ sensing. The channel is gated by cGMP produced by specific guanylyl cyclases (ODR-1/DAF-11 for chemosensation; GCY-8/18/23 for thermosensation; GCY-35/36 for O₂; GCY-9 for CO₂), with signal termination provided by phosphodiesterases PDE-1, PDE-2, and PDE-5. Beyond acute sensory transduction, TAX-2/TAX-4 channel activity influences activity-dependent gene expression, dauer developmental decisions, and organismal lifespan through non-cell-autonomous activation of the UPR^ER in intestinal cells. TAX-2 can also partner with alternative α subunits such as CNG-3 for context-specific functions, revealing a previously unappreciated combinatorial logic in CNG channel function in this organism.

References

1. (mckemy2007temperaturesensingacross pages 3-4): David D. McKemy. Temperature sensing across species. Pflügers Archiv - European Journal of Physiology, 454:777-791, Jan 2007. URL: https://doi.org/10.1007/s00424-006-0199-6, doi:10.1007/s00424-006-0199-6. This article has 115 citations.

2. (ferkey2021chemosensorysignaltransduction pages 14-15): Denise M Ferkey, Piali Sengupta, and Noelle D L’Etoile. Chemosensory signal transduction in caenorhabditis elegans. Genetics, Mar 2021. URL: https://doi.org/10.1093/genetics/iyab004, doi:10.1093/genetics/iyab004. This article has 162 citations and is from a domain leading peer-reviewed journal.

3. (bargmann2006chemosensationinc. pages 10-12): Cornelia Bargmann. Chemosensation in c. elegans. WormBook : the online review of C. elegans biology, pages 1-29, Oct 2006. URL: https://doi.org/10.1895/wormbook.1.123.1, doi:10.1895/wormbook.1.123.1. This article has 1160 citations.

4. (li2024inhibitionofa pages 6-7): Dongdong Li, Di Chen, Wei Li, and Guangshuo Ou. Inhibition of a cyclic nucleotide-gated channel on neuronal cilia activates unfolded protein response in intestinal cells to promote longevity. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2321228121, doi:10.1073/pnas.2321228121. This article has 3 citations and is from a highest quality peer-reviewed journal.

5. (rosero2026afdthermosensoryneurons pages 13-14): Manuel Rosero and Jihong Bai. Afd thermosensory neurons mediate tactile-dependent locomotion modulation in c. elegans. Apr 2026. URL: https://doi.org/10.7554/elife.106496, doi:10.7554/elife.106496. This article has 0 citations.

6. (rosero2026afdthermosensoryneurons pages 14-15): Manuel Rosero and Jihong Bai. Afd thermosensory neurons mediate tactile-dependent locomotion modulation in c. elegans. Apr 2026. URL: https://doi.org/10.7554/elife.106496, doi:10.7554/elife.106496. This article has 0 citations.

7. (menini2009theneurobiologyof pages 36-38): A. Menini. The neurobiology of olfaction. ArXiv, pages 1-418, Nov 2009. URL: https://doi.org/10.1201/9781420071993, doi:10.1201/9781420071993. This article has 142 citations.

8. (li2024inhibitionofa pages 7-8): Dongdong Li, Di Chen, Wei Li, and Guangshuo Ou. Inhibition of a cyclic nucleotide-gated channel on neuronal cilia activates unfolded protein response in intestinal cells to promote longevity. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2321228121, doi:10.1073/pnas.2321228121. This article has 3 citations and is from a highest quality peer-reviewed journal.

9. (bargmann2006chemosensationinc. pages 1-3): Cornelia Bargmann. Chemosensation in c. elegans. WormBook : the online review of C. elegans biology, pages 1-29, Oct 2006. URL: https://doi.org/10.1895/wormbook.1.123.1, doi:10.1895/wormbook.1.123.1. This article has 1160 citations.

10. (galande2025rolesofcyclic pages 12-13): Kranti K. Galande and Rick H. Cote. Roles of cyclic nucleotide phosphodiesterases in signal transduction pathways in the nematode caenorhabditis elegans. Cells, 14:1174, Jul 2025. URL: https://doi.org/10.3390/cells14151174, doi:10.3390/cells14151174. This article has 4 citations.

11. (galande2025rolesofcyclic pages 15-16): Kranti K. Galande and Rick H. Cote. Roles of cyclic nucleotide phosphodiesterases in signal transduction pathways in the nematode caenorhabditis elegans. Cells, 14:1174, Jul 2025. URL: https://doi.org/10.3390/cells14151174, doi:10.3390/cells14151174. This article has 4 citations.

12. (galande2025rolesofcyclic pages 7-9): Kranti K. Galande and Rick H. Cote. Roles of cyclic nucleotide phosphodiesterases in signal transduction pathways in the nematode caenorhabditis elegans. Cells, 14:1174, Jul 2025. URL: https://doi.org/10.3390/cells14151174, doi:10.3390/cells14151174. This article has 4 citations.

13. (ferkey2021chemosensorysignaltransduction pages 19-20): Denise M Ferkey, Piali Sengupta, and Noelle D L’Etoile. Chemosensory signal transduction in caenorhabditis elegans. Genetics, Mar 2021. URL: https://doi.org/10.1093/genetics/iyab004, doi:10.1093/genetics/iyab004. This article has 162 citations and is from a domain leading peer-reviewed journal.

14. (galande2025rolesofcyclic pages 9-10): Kranti K. Galande and Rick H. Cote. Roles of cyclic nucleotide phosphodiesterases in signal transduction pathways in the nematode caenorhabditis elegans. Cells, 14:1174, Jul 2025. URL: https://doi.org/10.3390/cells14151174, doi:10.3390/cells14151174. This article has 4 citations.

15. (galande2025rolesofcyclic pages 13-15): Kranti K. Galande and Rick H. Cote. Roles of cyclic nucleotide phosphodiesterases in signal transduction pathways in the nematode caenorhabditis elegans. Cells, 14:1174, Jul 2025. URL: https://doi.org/10.3390/cells14151174, doi:10.3390/cells14151174. This article has 4 citations.

16. (fielenbach2008c.elegansdauer pages 3-5): Nicole Fielenbach and Adam Antebi. C. elegans dauer formation and the molecular basis of plasticity. Genes & development, 22 16:2149-65, Aug 2008. URL: https://doi.org/10.1101/gad.1701508, doi:10.1101/gad.1701508. This article has 741 citations and is from a highest quality peer-reviewed journal.

17. (fielenbach2008c.elegansdauer pages 2-3): Nicole Fielenbach and Adam Antebi. C. elegans dauer formation and the molecular basis of plasticity. Genes & development, 22 16:2149-65, Aug 2008. URL: https://doi.org/10.1101/gad.1701508, doi:10.1101/gad.1701508. This article has 741 citations and is from a highest quality peer-reviewed journal.

18. (lin2017longevitycontrolby pages 1-2): Chih-Ta Lin, Chun-Wei He, Tzu-Ting Huang, and Chun-Liang Pan. Longevity control by the nervous system: sensory perception, stress response and beyond. Translational Medicine of Aging, 1:41-51, Oct 2017. URL: https://doi.org/10.1016/j.tma.2017.07.001, doi:10.1016/j.tma.2017.07.001. This article has 9 citations.

19. (li2024inhibitionofa pages 1-2): Dongdong Li, Di Chen, Wei Li, and Guangshuo Ou. Inhibition of a cyclic nucleotide-gated channel on neuronal cilia activates unfolded protein response in intestinal cells to promote longevity. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2321228121, doi:10.1073/pnas.2321228121. This article has 3 citations and is from a highest quality peer-reviewed journal.

20. (hill2024molecularandneuronal pages 84-89): Tyler J Hill. Molecular and neuronal mechanisms underlying rapid experience-dependent plasticity in a single thermosensory neuron. Text, Jan 2024. URL: https://doi.org/10.48617/etd.1088, doi:10.48617/etd.1088. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](tax-2-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](tax-2-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. mckemy2007temperaturesensingacross pages 3-4
2. ferkey2021chemosensorysignaltransduction pages 14-15
3. rosero2026afdthermosensoryneurons pages 13-14
4. menini2009theneurobiologyof pages 36-38
5. li2024inhibitionofa pages 7-8
6. galande2025rolesofcyclic pages 15-16
7. galande2025rolesofcyclic pages 7-9
8. galande2025rolesofcyclic pages 12-13
9. galande2025rolesofcyclic pages 13-15
10. lin2017longevitycontrolby pages 1-2
11. li2024inhibitionofa pages 6-7
12. hill2024molecularandneuronal pages 84-89
13. rosero2026afdthermosensoryneurons pages 14-15
14. ferkey2021chemosensorysignaltransduction pages 19-20
15. galande2025rolesofcyclic pages 9-10
16. li2024inhibitionofa pages 1-2
17. S727A
18. https://doi.org/10.1007/s00424-006-0199-6,
19. https://doi.org/10.1093/genetics/iyab004,
20. https://doi.org/10.1895/wormbook.1.123.1,
21. https://doi.org/10.1073/pnas.2321228121,
22. https://doi.org/10.7554/elife.106496,
23. https://doi.org/10.1201/9781420071993,
24. https://doi.org/10.3390/cells14151174,
25. https://doi.org/10.1101/gad.1701508,
26. https://doi.org/10.1016/j.tma.2017.07.001,
27. https://doi.org/10.48617/etd.1088,