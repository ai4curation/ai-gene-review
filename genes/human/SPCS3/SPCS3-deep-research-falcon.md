---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T03:05:38.333130'
end_time: '2026-06-12T03:23:15.532453'
duration_seconds: 1057.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SPCS3
  gene_symbol: SPCS3
  uniprot_accession: P61009
  protein_description: 'RecName: Full=Signal peptidase complex subunit 3; AltName:
    Full=Microsomal signal peptidase 22/23 kDa subunit; Short=SPC22/23; Short=SPase
    22/23 kDa subunit;'
  gene_info: Name=SPCS3; Synonyms=SPC22; ORFNames=UNQ1841/PRO3567;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the SPCS3 family. .
  protein_domains: SPC3. (IPR007653); SPC22 (PF04573)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: SPCS3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: SPCS3-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000028 The overall architecture of the human
    signal peptidase complex (SPC) is illustrated across several figures. The **Graphical
    Abstrac'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P61009
- **Protein Description:** RecName: Full=Signal peptidase complex subunit 3; AltName: Full=Microsomal signal peptidase 22/23 kDa subunit; Short=SPC22/23; Short=SPase 22/23 kDa subunit;
- **Gene Information:** Name=SPCS3; Synonyms=SPC22; ORFNames=UNQ1841/PRO3567;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the SPCS3 family. .
- **Key Domains:** SPC3. (IPR007653); SPC22 (PF04573)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SPCS3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SPCS3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SPCS3** (gene ID: SPCS3, UniProt: P61009) in human.

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
- **UniProt Accession:** P61009
- **Protein Description:** RecName: Full=Signal peptidase complex subunit 3; AltName: Full=Microsomal signal peptidase 22/23 kDa subunit; Short=SPC22/23; Short=SPase 22/23 kDa subunit;
- **Gene Information:** Name=SPCS3; Synonyms=SPC22; ORFNames=UNQ1841/PRO3567;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the SPCS3 family. .
- **Key Domains:** SPC3. (IPR007653); SPC22 (PF04573)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SPCS3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SPCS3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SPCS3** (gene ID: SPCS3, UniProt: P61009) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive research report: Human **SPCS3** (UniProt **P61009**) / **SPC22/23**

### Executive summary
**SPCS3** encodes **signal peptidase complex subunit 3**, historically called the **microsomal signal peptidase 22/23 kDa subunit (SPC22/23)**. It is a **non-proteolytic/accessory subunit** of the **endoplasmic reticulum (ER) signal peptidase complex (SPC)**, an essential ER-membrane serine protease that removes N‑terminal signal peptides from secretory and membrane preproteins and can also cleave certain noncanonical membrane substrates. High-resolution structural proteomics places SPCS3 as a **luminal β‑sheet rich subunit** that **embraces and stabilizes** the catalytic SEC11 subunit and helps create a **membrane “TM window”** and **local membrane thinning** that contributes to signal-peptide selectivity. Recent functional work broadens SPC biology toward **membrane-protein quality control/ERAD coupling** and identifies contexts where SPCS3 is important in **virus–host interactions**, including **antiviral restriction of chikungunya virus** in macrophages (2023–2024) and interactions with rotavirus glycoprotein VP7. (liaci2021structureofthe pages 3-4, zanotti2023characterisationofthe pages 57-60, yao2024interactionofchikungunya pages 1-2)

### Gene/protein identity verification (mandatory)
- **Target identity matches UniProt P61009**: literature and structural work consistently refer to human **SPCS3** as **SPC22/23**, a subunit of the ER signal peptidase complex. (liaci2021structureofthe pages 1-3, liaci2021structureofthe pages 3-4)
- **Organism is Homo sapiens** in the key mechanistic structural study of the **human** SPC paralogs. (liaci2021structureofthe pages 1-3, liaci2021structureofthe pages 3-4)
- **Family/domain consistency**: SPCS3/SPC22/23 is described as a conserved eukaryotic SPC subunit with a **luminal β‑sandwich** domain and an ER membrane anchor; this aligns with the UniProt “SPCS3 family / SPC3” concept. (liaci2021structureofthe pages 3-4)

### 1) Key concepts and definitions (current understanding)

#### Signal peptidase complex (SPC): what it is
The **signal peptidase complex (SPC)** is an **ER-resident membrane protease** that removes N‑terminal **signal peptides** from newly translocated secretory and membrane proteins on the **luminal side** of the ER membrane. In humans, SPC exists as **two functional paralogs** that share accessory subunits but differ in the catalytic subunit: **SEC11A** or **SEC11C**. (liaci2021structureofthe pages 1-3, liaci2021structureofthe pages 3-4)

#### Where SPCS3 fits
SPCS3 (SPC22/23) is a **non-proteolytic (accessory) SPC subunit** that is nonetheless **required for catalytic function** because it stabilizes and positions the catalytic subunit within the assembled complex. (liaci2021structureofthe pages 3-4)

#### Signal peptide features and recognition rules
Signal peptides typically have (i) an N‑region, (ii) a hydrophobic **h‑region**, and (iii) a more polar **c‑region** containing the cleavage site. In a large empirical analysis used to interpret structural selectivity, human signal peptide **h‑regions were described as ~7–15 aa** and **c‑regions as ~3–7 aa**. (liaci2021structureofthe pages 3-4, liaci2021structureofthe pages 1-3)

### 2) Molecular function of SPCS3 and mechanism in the SPC

#### Primary function: structural/architectural subunit enabling signal peptide cleavage
Cryo‑EM and structural proteomics of the human SPC show that **SPC22/23 (SPCS3)** forms a **luminal, β‑sheet rich domain** (an “extended β‑sandwich”) that **embraces the catalytic SEC11 core**, creating a “globular luminal body consisting solely of β sheets.” This architecture helps position/stabilize the catalytic subunit near the membrane surface—providing a mechanistic explanation for why SPCS3 is required for catalysis despite being non-proteolytic. (liaci2021structureofthe pages 3-4)

#### Catalytic chemistry occurs in SEC11A/C (not SPCS3)
The SPC active site is in SEC11A or SEC11C and uses a **Ser–His–Asp catalytic triad**, with the active site positioned adjacent to the ER membrane. SPCS3 contributes indirectly by stabilizing the luminal architecture around this catalytic center. (liaci2021structureofthe pages 1-3)

#### “TM window” and membrane thinning model of selectivity
A key mechanistic insight is that the assembled SPC forms a **~15 Å wide lipid-filled “TM window”** in the membrane and locally **thins** the bilayer near the active site. This physical feature is proposed to act as a **molecular ruler** that favors **short hydrophobic segments** (signal peptides) over longer transmembrane helices, thereby helping ensure specificity across thousands of substrates. SPCS3 contributes a transmembrane helix to the architecture that frames this TM window. (liaci2021structureofthe pages 3-4, liaci2021structureofthe media 82778a29)

#### Post-translational cleavage and noncanonical membrane substrates
Beyond canonical cleavage of N‑terminal signal peptides during/after translocation, functional work supports that SPC can also cleave **noncanonical transmembrane-domain (TMD) substrates** post‑translationally on the luminal side of the ER membrane, including in a **quality-control context** (see below). SPCS3 is described as part of a minimal catalytic core with SEC11A/C in that model. (zanotti2023characterisationofthe pages 57-60, zanotti2023characterisationofthe pages 53-57)

### 3) Subcellular localization and topology

#### Localization
SPCS3/SPC22/23 is an **ER membrane** protein, with a large **luminal domain** exposed to the ER lumen as part of the luminal “body” of the SPC. (liaci2021structureofthe pages 3-4)

#### Glycosylation and luminal exposure
In the structural proteomics preparation, **98% of SPC22/23 molecules were N‑glycosylated at Asp141**, supporting luminal exposure of this region (consistent with ER lumen N‑glycosylation). (liaci2021structureofthe pages 3-4)

#### Visual evidence (SPC architecture)
Liaci et al. provide schematic and structural figures that label **SPC22/23 (SPCS3)** within the assembled human SPC and illustrate the **membrane thinning / TM window** concept. (liaci2021structureofthe media 82778a29, liaci2021structureofthe media 2d99ad67, liaci2021structureofthe media 5273058a)

### 4) Pathways and biological processes

#### Canonical pathway: ER co-/post-translational processing in the secretory pathway
SPCS3 acts in the **ER lumen-facing signal-peptide cleavage step**, which is required for maturation, folding, and trafficking of many secreted proteins and membrane proteins. (liaci2021structureofthe pages 1-3, liaci2021structureofthe pages 3-4)

#### Emerging pathway framing (2023): SPC as membrane-protein quality control coupled to ERAD
A 2023 functional characterization proposes that SPC performs **post‑translocational cleavage of certain membrane proteins** as a **quality-control mechanism** and connects this to ERAD by reporting interaction with the E3 ligase **Hrd1**. In this model, **SEC11A/C + SPCS3** constitute a **minimal catalytic core**, while other subunits may assemble or modulate cleavage for distinct functions. (zanotti2023characterisationofthe pages 57-60)

#### Isoform/substrate specificity: SEC11A vs SEC11C
A 2023 study on the tail-anchored protein **Jaw1** reports that the C‑terminal luminal region is cleaved after insertion by SPC, and that **SEC11A-containing SPC**, but **not SEC11C-containing SPC**, cleaves Jaw1—supporting functional specialization among SPC paralogs in cells. SPCS3 is part of both forms. (kozono2023cleavageofthe pages 1-4)

### 5) Recent developments and latest research (prioritizing 2023–2024)

#### 2024: SPCS3 as an antiviral restriction factor for chikungunya virus in macrophages
A 2024 **EMBO Journal** study identified **SPCS3** by proteomics as a **CHIKV E1-binding host factor with anti‑CHIKV activity** in THP‑1 derived human macrophages; mutation of CHIKV E1 residue **V220** attenuated E1 binding to SPCS3 (and eIF3k) and impaired virion production in macrophages. The study also links infection-driven relocalization of eIF3k to a cytoplasmic compartment where it associates with SPCS3. (yao2024interactionofchikungunya pages 1-2)

**Interpretation:** While SPC subunits are frequently proviral for ER-budding viruses, these macrophage data indicate SPCS3 can also participate in **innate restriction**—possibly by interfering with viral glycoprotein biogenesis/trafficking or by engaging quality-control pathways. The molecular mechanism remains to be resolved, but the direct viral glycoprotein interaction is experimentally supported. (yao2024interactionofchikungunya pages 1-2)

#### 2023 (preprint): quantitative restriction phenotype for SPCS3 against CHIKV
A 2023 bioRxiv study using AP‑MS and functional perturbations reported that **siRNA knockdown of SPCS3 restored CHIKV virion production by ~5‑fold** in THP‑1 derived macrophages, with the phenotype persisting when cells were transfected with CHIKV vRNA (supporting a post‑entry mechanism). (yao2023chikungunyavirusglycoproteins pages 4-6)

#### 2023: renewed emphasis on noncanonical substrates and quality control
Zanotti (2023) describes a broadened functional framework for SPC beyond canonical signal peptides, including identification of many potential cryptic cleavage sites and validation of multiple noncanonical membrane substrates; in that model, SPCS3 remains central as part of the catalytic core with SEC11A/C and contributes to cleavage of noncanonical substrates to varying extents. (zanotti2023characterisationofthe pages 53-57, zanotti2023characterisationofthe pages 57-60)

### 6) Current applications and real-world implementations

#### Host-directed antiviral concept (SPC pathway)
Multiple studies position the SPC pathway as a potential **host-directed antiviral target** because viruses that rely on ER signal peptide processing (e.g., flaviviruses) can be sensitive to disruption of SPC components. A canonical example is the definition of an ER signal peptide processing pathway required by flaviviruses using genome-wide CRISPR screening; SPC subunits including SPCS3 are part of this functional network. (alzahrani2022spcs1dependente2p7processing pages 2-3)

While the report above is centered on SPCS3 functional annotation, it is notable that SPC inhibition (e.g., with **cavinafungin**, discussed in the quality-control work) is used experimentally to block SPC-mediated cleavage, illustrating a chemical-biology route for interrogating the pathway. (zanotti2023characterisationofthe pages 57-60)

#### Proteomics/structural biology as functional annotation tools
The SPCS3 case illustrates a general, widely used implementation: **cryo-EM + native MS/top-down MS + XL-MS** define stoichiometry, topology, and mechanistic hypotheses for essential membrane complexes that are difficult to characterize genetically alone. (liaci2021structureofthe pages 3-4)

### 7) Expert opinions and authoritative analysis (evidence-based)

#### “Accessory” does not mean “dispensable”
A recurring point across structural and functional work is that SPCS3 is **non-proteolytic** but **mechanistically essential**: it provides a structural scaffold that positions the catalytic SEC11 active site at the correct membrane-proximal location and stabilizes the luminal architecture. This is a strong, mechanistically grounded interpretation because it is directly supported by the cryo‑EM model in which SPC22/23 physically “embraces” SEC11. (liaci2021structureofthe pages 3-4)

#### Modular SPC composition remains an open area
Zanotti (2023) suggests a model where **SEC11A/C + SPCS3** could form a core with conditionally assembling accessory subunits for specialized functions. This is consistent with observations of variable complex recovery in proteomics and with functional specialization for noncanonical substrates, but the precise assembly dynamics and which subunits define substrate classes remain incompletely resolved. (zanotti2023characterisationofthe pages 57-60)

### 8) Key statistics and data points (from recent and foundational studies)

- **Cryo‑EM resolution** for human SPC structural determination: ~**4.9 Å**. (liaci2021structureofthe pages 3-4)
- **TM window width**: ~**15 Å** (lipid-filled). (liaci2021structureofthe pages 3-4)
- **SPCS3 glycosylation**: **98%** N‑glycosylated at **Asp141** in HEK293-derived sample. (liaci2021structureofthe pages 3-4)
- **Signal peptide features** in the structural analysis context: h‑region **7–15 aa**, c‑region **3–7 aa**; longer hydrophobic segments (~**18–20 aa**) tend not to be cleaved by eukaryotic SPC. (liaci2021structureofthe pages 3-4, liaci2021structureofthe pages 7-8)
- **CHIKV restriction**: SPCS3 siRNA knockdown restores virion production by ~**5‑fold** in macrophages. (yao2023chikungunyavirusglycoproteins pages 4-6)
- **CHIKV AP‑MS scale**: **1157** proteins significantly enriched (Log2FC>0, p<0.05) in CHIKV/myc‑E2 purifications (2 experiments), with reported viral bait enrichment statistics. (yao2023chikungunyavirusglycoproteins pages 4-6)
- **Rotavirus VP7 interactome**: SPCS3 detected with **114 peptide counts** (SPCS2 190; SEC11A 70; SEC11C 31; SPCS1 13) among high-confidence VP7 interactors. (zhu2026signalpeptidasecomplex pages 2-5)
- **TCGA-HNSC expression study**: **518 tumors vs 44 normals**; SPCS3 upregulated in tumors but not clearly prognostic by median-split survival in the excerpt. (hu2022signalpeptidasecomplex pages 2-4)
- **OpenTargets disease association scores** (hypothesis-generating): e.g., neurodegenerative disease score ~**0.5268** and dengue disease score ~**0.4623** for SPCS3. (OpenTargets Search: -SPCS3)

### 9) Evidence summary table
The following table compiles the most actionable evidence for functional annotation.

| Topic | Key findings | Quantitative/statistical data | Primary source (first author, year) | URL/DOI |
|---|---|---|---|---|
| Identity / localization | Human **SPCS3** matches UniProt **P61009** and encodes **SPC22/23**, a non-proteolytic subunit of the **ER signal peptidase complex (SPC)**. Structural work places it in the ER membrane with a large **luminal β-sandwich** domain that embraces SEC11 and a TM helix contributing to the complex architecture. (liaci2021structureofthe pages 3-4, liaci2021structureofthe pages 1-3) | ER-resident heterotetrameric complex; SPCS3 luminal domain exposed to ER lumen. | Liaci, 2021 | https://doi.org/10.2139/ssrn.3778304 |
| SPC structure | Human SPC exists as **two paralogs** containing **SEC11A or SEC11C** plus **SPC12/SPCS1, SPC25/SPCS2, SPC22/23/SPCS3**. SPCS3 stabilizes the catalytic core and contributes to the lipid-filled TM window that helps determine signal-peptide selectivity. (liaci2021structureofthe pages 3-4, liaci2021structureofthe pages 1-3, liaci2021structureofthe media 82778a29) | Cryo-EM map ~**4.9 Å**; complex mass ~**84 kDa**; TM window ~**15 Å** wide; SEC11A/C share ~**80%** sequence identity. (liaci2021structureofthe pages 3-4) | Liaci, 2021 | https://doi.org/10.2139/ssrn.3778304 |
| Catalytic mechanism / substrate rules | The active site is in SEC11A/C, but SPCS3 is required structurally because its luminal β-sandwich “embraces” SEC11 and positions the active site near the luminal membrane surface. SPC specificity depends on **membrane thinning** and short signal-peptide hydrophobic segments rather than long TM helices. (liaci2021structureofthe pages 3-4, liaci2021structureofthe pages 1-3, liaci2021structureofthe media 2d99ad67) | SPCS3 N-glycosylated at **Asp141** in **98%** of molecules; signal-peptide **h-region 7–15 aa**, **c-region 3–7 aa**; regular TM helices of ~**18–20 aa** are generally excluded. (liaci2021structureofthe pages 3-4, liaci2021structureofthe pages 7-8) | Liaci, 2021 | https://doi.org/10.2139/ssrn.3778304 |
| Quality control / ERAD | 2023 work proposes SPC can act as a **membrane-protein quality-control enzyme**. In this model, **SEC11A/C + SPCS3** form a minimal catalytic core, while other subunits can modulate noncanonical cleavage. SPC was linked to **Hrd1** and ER-associated degradation of membrane proteins. (zanotti2023characterisationofthe pages 57-60, zanotti2023characterisationofthe pages 53-57) | ~**1,500** membrane proteins predicted to harbor cryptic SPC sites; noncanonical cleavage blocked by **cavinafungin**; individual perturbation of SPCS1/2/3 altered cleavage to varying extents. (zanotti2023characterisationofthe pages 57-60, zanotti2023characterisationofthe pages 53-57) | Zanotti, 2023 | https://doi.org/10.11588/heidok.00033417 |
| Substrate/isoform specificity in cells | SPC can process some noncanonical substrates beyond standard N-terminal signal peptides. A 2023 study showed **SEC11A-containing SPC**, not SEC11C-SPC, cleaves the ER/outer nuclear membrane tail-anchored protein **Jaw1**, supporting isoform-dependent substrate specificity. SPCS3 is part of both SPC isoforms. (kozono2023cleavageofthe pages 1-4) | Human SPC described as **SPCS1 + SPCS2 + SPCS3 + SEC11A/C** heterotetramer; Jaw1 cleavage assigned specifically to **SEC11A-SPC**. (kozono2023cleavageofthe pages 1-4) | Kozono, 2023 | https://doi.org/10.1242/jcs.260439 |
| Virus–host interactions: flaviviruses / HCV | Genetic screens and follow-up studies implicate SPCS3 and the SPC pathway in **Flaviviridae** infection, especially late-stage polyprotein processing and virion production. SPCS3 is consistently identified with other SPC subunits as a host factor in this pathway. (alzahrani2022spcs1dependente2p7processing pages 2-3) | CRISPR screen defined an SPC-dependent pathway required by flaviviruses; one SEC11-containing SPC paralog was **30–40×** less abundant in structural prep but both were catalytically competent in vitro. (liaci2021structureofthe pages 1-3, alzahrani2022spcs1dependente2p7processing pages 2-3) | Zhang, 2016; Alzahrani, 2022 | https://doi.org/10.1038/nature18625; https://doi.org/10.1371/journal.ppat.1010310 |
| Virus–host interactions: CHIKV restriction | In human macrophages, **SPCS3 binds CHIKV E1** and acts as an **antiviral/restriction factor** rather than a proviral factor. Mutation of the positively selected viral residue **E1 V220** weakens interaction with SPCS3 and impairs virion production. (yao2024interactionofchikungunya pages 1-2, yao2023chikungunyavirusglycoproteins pages 1-3) | AP-MS identified **1,157** significantly enriched proteins (**Log2FC > 0, p < 0.05**) in CHIKV/myc-E2 purifications; **SPCS3 knockdown restored virion production ~5-fold**; bait enrichments included **E2 Log2FC 5.84 (p=2.11×10^-5)**, **E1 Log2FC 4.09 (p=1.59×10^-3)**, **E3 Log2FC 2.99 (p=3.08×10^-2)**. (yao2023chikungunyavirusglycoproteins pages 4-6) | Yao, 2024; Yao, 2023 | https://doi.org/10.1038/s44318-024-00193-3; https://doi.org/10.1101/2023.05.29.542714 |
| Virus–host interactions: rotavirus VP7 | Rotavirus VP7 interactome studies identified **SPCS3** among the strongest SPC-family interactors, supporting a role in ER glycoprotein maturation/assembly of viral particles. (zhu2026signalpeptidasecomplex pages 2-5) | VP7 affinity purification identified **13** high-confidence interactors; peptide counts: **SPCS3 114**, **SPCS2 190**, **SEC11A 70**, **SEC11C 31**, **SPCS1 13**. VP7 signal peptide cleavage occurs between **Ala50–Gln51**. (zhu2026signalpeptidasecomplex pages 2-5) | Zhu, 2026 | https://doi.org/10.1371/journal.ppat.1013688 |
| Disease / cancer associations | In TCGA head and neck squamous cell carcinoma, **SPCS3 mRNA was upregulated in tumors** versus adjacent normal tissue, but unlike SEC11A it was **not clearly prognostic** by median-split survival analysis. (hu2022signalpeptidasecomplex pages 2-4) | Cohort sizes: **518** primary tumors, **44** adjacent normals; SPCS3 significant tumor upregulation reported, but no SPCS3-specific HR/p-value for survival provided in the excerpt. (hu2022signalpeptidasecomplex pages 2-4) | Hu, 2022 | https://doi.org/10.1371/journal.pone.0269166 |
| Database associations | Open Targets shows **modest, non-disease-defining associations** for SPCS3 across several conditions; these are useful as leads but not as strong evidence for a primary Mendelian disease role. (OpenTargets Search: -SPCS3) | Association scores: **neurodegenerative disease 0.5268**, **dengue disease 0.4623**, **brain aneurysm 0.2143**, **skeletal-system abnormality 0.2085**, **gastritis 0.1820**. (OpenTargets Search: -SPCS3) | Open Targets platform | https://platform.opentargets.org/target/ENSG00000129128 |


*Table: This table compiles the main experimentally supported findings for human SPCS3/SPC22/23, including structural role, mechanism, pathway context, and disease/infection associations. It highlights the most useful quantitative values for rapid functional annotation.*

### References (URLs and publication dates in evidence)
- Liaci AM et al. *Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage* (2021-01). https://doi.org/10.2139/ssrn.3778304 (liaci2021structureofthe pages 3-4)
- Kozono T et al. *Cleavage of the Jaw1 C-terminal region enhances its augmentative effect on the Ca2+ release via IP3 receptors* (2023-02). https://doi.org/10.1242/jcs.260439 (kozono2023cleavageofthe pages 1-4)
- Zanotti A. *Characterisation of the human signal peptidase complex as a quality control enzyme for membrane proteins* (2023-01). https://doi.org/10.11588/heidok.00033417 (zanotti2023characterisationofthe pages 53-57)
- Yao Z et al. *Interaction of chikungunya virus glycoproteins with macrophage factors controls virion production* (2024-09). https://doi.org/10.1038/s44318-024-00193-3 (yao2024interactionofchikungunya pages 1-2)
- Yao Z et al. *Chikungunya virus glycoproteins transform macrophages into productive viral dissemination vessels* (2023-05). https://doi.org/10.1101/2023.05.29.542714 (yao2023chikungunyavirusglycoproteins pages 4-6)
- Hu C et al. *SEC11A upregulation is a biomarker of poor prognosis in HNSC* (2022-06). https://doi.org/10.1371/journal.pone.0269166 (hu2022signalpeptidasecomplex pages 2-4)
- Open Targets (accessed via tool): https://platform.opentargets.org/target/ENSG00000129128 (OpenTargets Search: -SPCS3)



References

1. (liaci2021structureofthe pages 3-4): A. Manuel Liaci, Barbara Steigenberger, Sem Tamara, Paulo Cesar Telles de Souza, Mariska Gröllers-Mulderij, Patrick Ogrissek, Siewert Jan Marrink, Richard Scheltema, and Friedrich Förster. Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage. Jan 2021. URL: https://doi.org/10.2139/ssrn.3778304, doi:10.2139/ssrn.3778304. This article has 148 citations.

2. (zanotti2023characterisationofthe pages 57-60): Andrea Zanotti. Characterisation of the human signal peptidase complex as a quality control enzyme for membrane proteins. Text, Jan 2023. URL: https://doi.org/10.11588/heidok.00033417, doi:10.11588/heidok.00033417. This article has 0 citations and is from a peer-reviewed journal.

3. (yao2024interactionofchikungunya pages 1-2): Zhenlan Yao, Sangeetha Ramachandran, Serina Huang, Erin Kim, Yasaman Jami-Alahmadi, Prashant Kaushal, Mehdi Bouhaddou, James A Wohlschlegel, and Melody MH Li. Interaction of chikungunya virus glycoproteins with macrophage factors controls virion production. The EMBO Journal, 43:4625-4655, Sep 2024. URL: https://doi.org/10.1038/s44318-024-00193-3, doi:10.1038/s44318-024-00193-3. This article has 6 citations.

4. (liaci2021structureofthe pages 1-3): A. Manuel Liaci, Barbara Steigenberger, Sem Tamara, Paulo Cesar Telles de Souza, Mariska Gröllers-Mulderij, Patrick Ogrissek, Siewert Jan Marrink, Richard Scheltema, and Friedrich Förster. Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage. Jan 2021. URL: https://doi.org/10.2139/ssrn.3778304, doi:10.2139/ssrn.3778304. This article has 148 citations.

5. (liaci2021structureofthe media 82778a29): A. Manuel Liaci, Barbara Steigenberger, Sem Tamara, Paulo Cesar Telles de Souza, Mariska Gröllers-Mulderij, Patrick Ogrissek, Siewert Jan Marrink, Richard Scheltema, and Friedrich Förster. Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage. Jan 2021. URL: https://doi.org/10.2139/ssrn.3778304, doi:10.2139/ssrn.3778304. This article has 148 citations.

6. (zanotti2023characterisationofthe pages 53-57): Andrea Zanotti. Characterisation of the human signal peptidase complex as a quality control enzyme for membrane proteins. Text, Jan 2023. URL: https://doi.org/10.11588/heidok.00033417, doi:10.11588/heidok.00033417. This article has 0 citations and is from a peer-reviewed journal.

7. (liaci2021structureofthe media 2d99ad67): A. Manuel Liaci, Barbara Steigenberger, Sem Tamara, Paulo Cesar Telles de Souza, Mariska Gröllers-Mulderij, Patrick Ogrissek, Siewert Jan Marrink, Richard Scheltema, and Friedrich Förster. Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage. Jan 2021. URL: https://doi.org/10.2139/ssrn.3778304, doi:10.2139/ssrn.3778304. This article has 148 citations.

8. (liaci2021structureofthe media 5273058a): A. Manuel Liaci, Barbara Steigenberger, Sem Tamara, Paulo Cesar Telles de Souza, Mariska Gröllers-Mulderij, Patrick Ogrissek, Siewert Jan Marrink, Richard Scheltema, and Friedrich Förster. Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage. Jan 2021. URL: https://doi.org/10.2139/ssrn.3778304, doi:10.2139/ssrn.3778304. This article has 148 citations.

9. (kozono2023cleavageofthe pages 1-4): Takuma Kozono, Chifuyu Jogano, Wataru Okumura, Hiroyuki Sato, Hitomi Matsui, Tsubasa Takagi, Nobuaki Okumura, Toshifumi Takao, Takashi Tonozuka, and Atsushi Nishikawa. Cleavage of the jaw1 c-terminal region enhances its augmentative effect on the ca2+ release via ip3 receptors. Journal of cell science, Feb 2023. URL: https://doi.org/10.1242/jcs.260439, doi:10.1242/jcs.260439. This article has 4 citations and is from a domain leading peer-reviewed journal.

10. (yao2023chikungunyavirusglycoproteins pages 4-6): Zhenlan Yao, Sangeetha Ramachandran, Serina Huang, Yasaman Jami-Alahmadi, James A. Wohlschlegel, and Melody M.H. Li. Chikungunya virus glycoproteins transform macrophages into productive viral dissemination vessels. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.29.542714, doi:10.1101/2023.05.29.542714. This article has 2 citations.

11. (alzahrani2022spcs1dependente2p7processing pages 2-3): Nabeel Alzahrani, Ming-Jhan Wu, Carla F. Sousa, Olga V. Kalinina, Christoph Welsch, and MinKyung Yi. Spcs1-dependent e2-p7 processing determines hcv assembly efficiency. PLOS Pathogens, 18:e1010310, Feb 2022. URL: https://doi.org/10.1371/journal.ppat.1010310, doi:10.1371/journal.ppat.1010310. This article has 8 citations and is from a highest quality peer-reviewed journal.

12. (liaci2021structureofthe pages 7-8): A. Manuel Liaci, Barbara Steigenberger, Sem Tamara, Paulo Cesar Telles de Souza, Mariska Gröllers-Mulderij, Patrick Ogrissek, Siewert Jan Marrink, Richard Scheltema, and Friedrich Förster. Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage. Jan 2021. URL: https://doi.org/10.2139/ssrn.3778304, doi:10.2139/ssrn.3778304. This article has 148 citations.

13. (zhu2026signalpeptidasecomplex pages 2-5): Xuejiao Zhu, Enkai Li, Liliana Sanchez-Tacuba, Wandy Beatty, Bin Li, and Siyuan Ding. Signal peptidase complex mediates rotavirus vp7 processing and virion assembly. PLOS Pathogens, 22(3):e1013688, Mar 2026. URL: https://doi.org/10.1371/journal.ppat.1013688, doi:10.1371/journal.ppat.1013688. This article has 0 citations and is from a highest quality peer-reviewed journal.

14. (hu2022signalpeptidasecomplex pages 2-4): Chunmei Hu, Jiangang Fan, Gang He, Chuan Dong, Shijie Zhou, and Yun Zheng. Signal peptidase complex catalytic subunit sec11a upregulation is a biomarker of poor prognosis in patients with head and neck squamous cell carcinoma. PLoS ONE, 17:e0269166, Jun 2022. URL: https://doi.org/10.1371/journal.pone.0269166, doi:10.1371/journal.pone.0269166. This article has 5 citations and is from a peer-reviewed journal.

15. (OpenTargets Search: -SPCS3): Open Targets Query (-SPCS3, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (yao2023chikungunyavirusglycoproteins pages 1-3): Zhenlan Yao, Sangeetha Ramachandran, Serina Huang, Yasaman Jami-Alahmadi, James A. Wohlschlegel, and Melody M.H. Li. Chikungunya virus glycoproteins transform macrophages into productive viral dissemination vessels. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.29.542714, doi:10.1101/2023.05.29.542714. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](SPCS3-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000028 The overall architecture of the human signal peptidase complex (SPC) is illustrated across several figures. The **Graphical Abstrac](SPCS3-deep-research-falcon_artifacts/image-1.png)

## Citations

1. liaci2021structureofthe pages 3-4
2. liaci2021structureofthe pages 1-3
3. zanotti2023characterisationofthe pages 57-60
4. kozono2023cleavageofthe pages 1-4
5. yao2024interactionofchikungunya pages 1-2
6. yao2023chikungunyavirusglycoproteins pages 4-6
7. zhu2026signalpeptidasecomplex pages 2-5
8. hu2022signalpeptidasecomplex pages 2-4
9. zanotti2023characterisationofthe pages 53-57
10. liaci2021structureofthe pages 7-8
11. yao2023chikungunyavirusglycoproteins pages 1-3
12. https://doi.org/10.2139/ssrn.3778304
13. https://doi.org/10.11588/heidok.00033417
14. https://doi.org/10.1242/jcs.260439
15. https://doi.org/10.1038/nature18625;
16. https://doi.org/10.1371/journal.ppat.1010310
17. https://doi.org/10.1038/s44318-024-00193-3;
18. https://doi.org/10.1101/2023.05.29.542714
19. https://doi.org/10.1371/journal.ppat.1013688
20. https://doi.org/10.1371/journal.pone.0269166
21. https://platform.opentargets.org/target/ENSG00000129128
22. https://doi.org/10.1038/s44318-024-00193-3
23. https://doi.org/10.2139/ssrn.3778304,
24. https://doi.org/10.11588/heidok.00033417,
25. https://doi.org/10.1038/s44318-024-00193-3,
26. https://doi.org/10.1242/jcs.260439,
27. https://doi.org/10.1101/2023.05.29.542714,
28. https://doi.org/10.1371/journal.ppat.1010310,
29. https://doi.org/10.1371/journal.ppat.1013688,
30. https://doi.org/10.1371/journal.pone.0269166,