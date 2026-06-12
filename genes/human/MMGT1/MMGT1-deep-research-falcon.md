---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T01:26:07.612775'
end_time: '2026-06-12T01:46:08.158306'
duration_seconds: 1200.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MMGT1
  gene_symbol: MMGT1
  uniprot_accession: Q8N4V1
  protein_description: 'RecName: Full=ER membrane protein complex subunit 5 {ECO:0000305|PubMed:29242231};
    AltName: Full=Membrane magnesium transporter 1 {ECO:0000312|HGNC:HGNC:28100};
    AltName: Full=Transmembrane protein 32 {ECO:0000312|HGNC:HGNC:28100};'
  gene_info: Name=MMGT1 {ECO:0000312|HGNC:HGNC:28100}; Synonyms=EMC5 {ECO:0000303|PubMed:29242231},
    TMEM32 {ECO:0000312|HGNC:HGNC:28100};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the membrane magnesium transporter (TC 1.A.67)
  protein_domains: MMgT. (IPR018937); MMgT (PF10270)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: MMGT1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: MMGT1-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000020 Figure 1 shows the architecture of the
    human ER membrane protein complex (EMC). Subunit EMC5 is labeled in all panels
    (A-D). Panels'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8N4V1
- **Protein Description:** RecName: Full=ER membrane protein complex subunit 5 {ECO:0000305|PubMed:29242231}; AltName: Full=Membrane magnesium transporter 1 {ECO:0000312|HGNC:HGNC:28100}; AltName: Full=Transmembrane protein 32 {ECO:0000312|HGNC:HGNC:28100};
- **Gene Information:** Name=MMGT1 {ECO:0000312|HGNC:HGNC:28100}; Synonyms=EMC5 {ECO:0000303|PubMed:29242231}, TMEM32 {ECO:0000312|HGNC:HGNC:28100};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the membrane magnesium transporter (TC 1.A.67)
- **Key Domains:** MMgT. (IPR018937); MMgT (PF10270)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MMGT1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MMGT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MMGT1** (gene ID: MMGT1, UniProt: Q8N4V1) in human.

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
- **UniProt Accession:** Q8N4V1
- **Protein Description:** RecName: Full=ER membrane protein complex subunit 5 {ECO:0000305|PubMed:29242231}; AltName: Full=Membrane magnesium transporter 1 {ECO:0000312|HGNC:HGNC:28100}; AltName: Full=Transmembrane protein 32 {ECO:0000312|HGNC:HGNC:28100};
- **Gene Information:** Name=MMGT1 {ECO:0000312|HGNC:HGNC:28100}; Synonyms=EMC5 {ECO:0000303|PubMed:29242231}, TMEM32 {ECO:0000312|HGNC:HGNC:28100};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the membrane magnesium transporter (TC 1.A.67)
- **Key Domains:** MMgT. (IPR018937); MMgT (PF10270)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MMGT1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MMGT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MMGT1** (gene ID: MMGT1, UniProt: Q8N4V1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research Report: Human **MMGT1** (UniProt **Q8N4V1**) / **EMC5** / **TMEM32**

### Executive summary
Human MMGT1 (UniProt Q8N4V1) corresponds to **ER membrane protein complex subunit 5 (EMC5)**, an **integral ER membrane** component of the **ER membrane protein complex (EMC)**, a conserved membrane-protein-biogenesis machine that functions as a **co-/post-translational insertase** and broader **membrane-protein chaperone/quality-control factor**. Across the structural and mechanistic EMC literature reviewed here, **EMC5 is consistently treated as a core EMC subunit**, not as a validated independent magnesium transporter; no direct experimental evidence supporting Mg2+ transport by EMC5/MMGT1 was found in these sources. Key recent advances (2023–2024) place EMC/EMC5 in (i) preventing **mistranslocation/misinsertion** at the ER via a selectivity filter and (ii) **post-translational topology rectification** of C-terminal transmembrane domains (TMDs) in multipass proteins—potentially impacting **~250** proteins including Cys-loop ion channels important for neurotransmission. (pleiner2020structuralbasisfor pages 1-3, pleiner2023aselectivityfilter pages 19-23, wu2024emcrectifiesthe pages 1-2)

| Topic | Key takeaways | Key sources with year + URL |
|---|---|---|
| Identity / aliases | UniProt Q8N4V1 corresponds to human **MMGT1**, better known in the EMC literature as **EMC5** and also annotated as **TMEM32**. In primary EMC studies, the protein is consistently treated as an **ER membrane protein complex subunit**, not as a validated standalone Mg²⁺ transporter (pleiner2020structuralbasisfor pages 1-3, whittsette2022theendoplasmicreticulum pages 1-2). | Pleiner et al., 2020, *Science* — https://doi.org/10.1126/science.abb5008; Whittsette et al., 2022, *iScience* — https://doi.org/10.1016/j.isci.2022.104754; OpenTargets MMGT1 associations — https://platform.opentargets.org (OpenTargets Search: -MMGT1, pleiner2020structuralbasisfor pages 1-3, whittsette2022theendoplasmicreticulum pages 1-2) |
| Localization / topology | EMC5 is an **integral ER membrane** subunit of the mammalian EMC. Structural work indicates **two transmembrane helices**, association with **EMC6**, and a **cytosolic C-terminus**; EMC5 helps anchor cytosolic and membrane regions of the complex (hegde2022thefunctionstructure pages 13-14, hegde2022thefunctionstructure pages 19-20, pleiner2020structuralbasisfor pages 1-3). | Hegde, 2022, *Annu Rev Biochem* — https://doi.org/10.1146/annurev-biochem-032620-104553; Pleiner et al., 2020, *Science* — https://doi.org/10.1126/science.abb5008 (hegde2022thefunctionstructure pages 13-14, hegde2022thefunctionstructure pages 19-20, pleiner2020structuralbasisfor pages 1-3) |
| Molecular function | Current best-supported function is **structural/core subunit of the EMC insertase/chaperone machinery** that supports membrane protein biogenesis. EMC5 stabilizes weak transmembrane interfaces, especially in the EMC3–EMC6 core region, rather than catalyzing an enzymatic reaction of its own (pleiner2020structuralbasisfor pages 1-3, hegde2022thefunctionstructure pages 4-6). | Pleiner et al., 2020, *Science* — https://doi.org/10.1126/science.abb5008; Hegde, 2022, *Annu Rev Biochem* — https://doi.org/10.1146/annurev-biochem-032620-104553 (pleiner2020structuralbasisfor pages 1-3, hegde2022thefunctionstructure pages 4-6) |
| Mechanism | EMC acts as a **co-/post-translational insertase** using an EMC3/EMC6-lined **hydrophilic vestibule** plus cytosolic capture elements; EMC5 contributes to the backside groove/cleft with EMC3 and EMC6 and to assembly interfaces with EMC2/EMC8. EMC also appears to have **chaperone-like** roles beyond insertion (hegde2022thefunctionstructure pages 13-14, pleiner2020structuralbasisfor pages 1-3, hegde2022thefunctionstructure pages 20-22). | Pleiner et al., 2020, *Science* — https://doi.org/10.1126/science.abb5008; Hegde, 2022, *Annu Rev Biochem* — https://doi.org/10.1146/annurev-biochem-032620-104553 (hegde2022thefunctionstructure pages 13-14, pleiner2020structuralbasisfor pages 1-3, hegde2022thefunctionstructure pages 20-22) |
| Recent 2023–2024 developments | **Pleiner 2023** showed the EMC contains a **charge-based selectivity filter** that limits misinsertion of mitochondrial TA proteins and enforces topology, with EMC5 contributing to a cleft lined by EMC3/EMC5/EMC6. **Wu 2024** showed EMC performs **post-translational topology rectification** of C-terminal TMDs in multipass proteins and estimated this may affect **~250 proteins** (pleiner2023aselectivityfilter pages 19-23, pleiner2023aselectivityfilter pages 1-2, wu2024emcrectifiesthe pages 7-9, wu2024emcrectifiesthe pages 1-2, wu2024emcrectifiesthe pages 2-3). | Pleiner et al., 2023, *J Cell Biol* — https://doi.org/10.1083/jcb.202212007; Wu et al., 2024, *Nat Struct Mol Biol* — https://doi.org/10.1038/s41594-023-01120-6; Li et al., 2024, *Aging* — https://doi.org/10.18632/aging.205660 (pleiner2023aselectivityfilter pages 19-23, pleiner2023aselectivityfilter pages 1-2, wu2024emcrectifiesthe pages 7-9, wu2024emcrectifiesthe pages 1-2, wu2024emcrectifiesthe pages 2-3) |
| Disease / phenotypes / applications | EMC function is important for **GABAA receptor**, other ion-channel, and secretory-pathway proteostasis; EMC perturbation reduces receptor surface expression and can trigger ER stress/UPR. Overexpression of **EMC5+EMC6** rescued trafficking/function of pathogenic GABAA receptor variants, suggesting a possible **proteostasis-modulation** strategy rather than a direct MMGT1-targeted therapy (whittsette2022theendoplasmicreticulum pages 14-16, whittsette2022theendoplasmicreticuluma pages 35-41, whittsette2022theendoplasmicreticulum pages 1-2). | Whittsette et al., 2022, *iScience* — https://doi.org/10.1016/j.isci.2022.104754; OpenTargets MMGT1 disease associations — https://platform.opentargets.org (whittsette2022theendoplasmicreticulum pages 14-16, whittsette2022theendoplasmicreticuluma pages 35-41, whittsette2022theendoplasmicreticulum pages 1-2, OpenTargets Search: -MMGT1) |
| Quantitative stats | Examples: EMC4 knockdown reduced induced **GABAA receptor surface expression to <50%**; loss of EMC impaired GABRA1 C-tail glycosylation/insertion by **>50%**; EMC5+EMC6 overexpression increased surface α1 levels to **380%, 235%, 285%** for three pathogenic variants and raised peak currents up to **550%** in one assay. Ribosome-proximity profiling found **~53 enriched mRNAs**, and one proteomics study identified **21 proteins with ≥50% reduction** after EMC perturbation (wu2024emcrectifiesthe pages 3-4, whittsette2022theendoplasmicreticulum pages 14-16, hegde2022thefunctionstructure pages 19-20, wu2024emcrectifiesthe pages 2-3, whittsette2022theendoplasmicreticuluma pages 35-41). | Wu et al., 2024, *Nat Struct Mol Biol* — https://doi.org/10.1038/s41594-023-01120-6; Whittsette et al., 2022, *iScience* — https://doi.org/10.1016/j.isci.2022.104754; Hegde, 2022, *Annu Rev Biochem* — https://doi.org/10.1146/annurev-biochem-032620-104553 (wu2024emcrectifiesthe pages 3-4, whittsette2022theendoplasmicreticulum pages 14-16, hegde2022thefunctionstructure pages 19-20, wu2024emcrectifiesthe pages 2-3, whittsette2022theendoplasmicreticuluma pages 35-41) |


*Table: This table summarizes the most evidence-supported functional annotation for human MMGT1/EMC5 (UniProt Q8N4V1), emphasizing its role as an EMC core subunit in ER membrane protein biogenesis. It also highlights recent 2023–2024 mechanistic advances, disease relevance, and key quantitative findings.*

---

## 1. Target verification: correct gene/protein identity
### 1.1 Identity and nomenclature
The research target (UniProt Q8N4V1) aligns with the protein described in the human EMC literature as **EMC5**, a subunit of the ER membrane protein complex. Multiple EMC-focused sources describe EMC5 as one of the mammalian EMC subunits and a membrane-spanning/core component required for complex integrity and activity. (whittsette2022theendoplasmicreticulum pages 1-2, pleiner2020structuralbasisfor pages 1-3)

### 1.2 Ambiguity check: “MMGT1” as a magnesium transporter
Although UniProt/HGNC annotate Q8N4V1 with the name **membrane magnesium transporter 1 (MMGT1)**, the EMC structural/mechanistic literature assessed here does **not** present EMC5 as a standalone Mg2+ transporter and does not provide Mg2+ transport assays or Mg2+-flux phenotypes attributable specifically to EMC5. Instead, EMC5 is consistently treated as an EMC subunit supporting insertase/chaperone functions. (pleiner2020structuralbasisfor pages 1-3, whittsette2022theendoplasmicreticulum pages 1-2, hegde2022thefunctionstructure pages 13-14)

---

## 2. Key concepts and definitions (current understanding)
### 2.1 The ER membrane protein complex (EMC)
The EMC is an ER-localized, conserved multiprotein assembly implicated in membrane-protein biogenesis. Current consensus is that EMC has a clear role in **transmembrane domain (TMD) insertion** and additional, less fully resolved roles in later steps of membrane-protein folding/assembly (i.e., “membrane chaperone” functions). (hegde2022thefunctionstructure pages 1-2, hegde2022thefunctionstructure pages 20-22)

Structural work on yeast and human EMC indicates EMC behaves as a **TMD insertase**, mechanistically analogous in part to Oxa1/YidC-family insertases, featuring membrane-embedded conduits/vestibules that support movement of hydrophobic helices into the bilayer. (bai2020structureofthe pages 1-2, pleiner2020structuralbasisfor pages 1-3)

### 2.2 Where EMC5 fits in EMC: topology and role
EMC5 is an **integral membrane subunit** within the EMC membrane domain. A key structural synthesis places EMC5 on the “back side” of the conserved EMC3–EMC6 membrane core, contributing **two transmembrane domains (TMDs)** that associate with EMC6 and helping shape a hydrophobic groove across the membrane domain. (hegde2022thefunctionstructure pages 13-14)

In the human EMC cryo-EM structure, EMC5 helps anchor the complex, and its **C-terminal tail traverses through EMC2 to the cytosolic face**, indicating a cytosolic C-terminus and extensive cytosolic interface participation. (pleiner2020structuralbasisfor pages 1-3)

A representative structural overview figure from Pleiner et al. (Science, 2020) shows EMC5 as a labeled subunit in the overall architecture and within the core transmembrane region adjacent to the insertion vestibule. (pleiner2020structuralbasisfor media a3da7fb7)

---

## 3. Molecular function and mechanism
### 3.1 Primary function: contribution to an ER insertase/chaperone machine
The best-supported “molecular function” for EMC5/MMGT1 is not an enzymatic reaction or an independent transport activity; rather, EMC5 functions as a **structural and assembly-critical subunit** of the EMC, enabling the EMC’s insertase/chaperone roles in membrane protein biogenesis. (pleiner2020structuralbasisfor pages 1-3, whittsette2022theendoplasmicreticulum pages 1-2)

A specific mechanistic example is that EMC5 stabilizes a **poorly hydrophobic** transmembrane helix in EMC6: in the human EMC structure, EMC6 TM1 inserts only upon assembly with EMC5, implying EMC5 contributes to EMC’s ability to stabilize challenging membrane-embedded helices at subunit interfaces. (pleiner2020structuralbasisfor pages 1-3)

### 3.2 Insertase mechanism (structural model)
The human EMC structure supports a model in which substrate insertion requires a **methionine-rich cytosolic loop** and proceeds through an enclosed **hydrophilic vestibule** formed principally by EMC3 and EMC6. The complex may facilitate insertion through **local membrane thinning** and electrostatic features that lower the energetic barrier. EMC5 contributes to the integrity and architecture of the complex around this machinery. (pleiner2020structuralbasisfor pages 1-3, hegde2022thefunctionstructure pages 13-14)

### 3.3 Selectivity / topology control
In 2023, Pleiner et al. described the EMC as implementing a **charge-based selectivity filter** to limit misinsertion of mitochondrial tail-anchored proteins and to enforce topology (positive-inside rule) for certain substrates. In that work, a distinct hydrophobic cleft/crevice is described as being lined by residues from **EMC3, EMC5, and EMC6**, linking EMC5 directly to the intramembrane architecture relevant to selectivity. (pleiner2023aselectivityfilter pages 10-11, pleiner2023aselectivityfilter pages 19-23)

---

## 4. Subcellular localization and functional context
### 4.1 ER localization and ribosome proximity
The EMC is an ER membrane complex positioned to act during cotranslational and posttranslational stages of membrane protein biogenesis. Notably, ribosome-proximity profiling used an **EMC5 C-terminal BirA fusion** (indicating cytosolic exposure of the EMC5 C-terminus) to biotinylate nearby translating ribosomes. EMC-proximal ribosomes were enriched for secretory and membrane protein mRNAs, and refined analysis identified localized enrichment in **~53 mRNAs**, often mapping to regions encoding TMD bundles, consistent with transient EMC engagement during multipass biogenesis. (hegde2022thefunctionstructure pages 19-20)

### 4.2 Connections to ER proteostasis networks
EMC perturbation has been linked to ER homeostasis and quality-control pathways (e.g., UPR/ERAD connections) in multiple studies and is commonly discussed as a factor in membrane-protein folding and complex assembly beyond initial insertion. (hegde2022thefunctionstructure pages 4-6, hegde2022thefunctionstructure pages 20-22)

---

## 5. Recent developments (prioritizing 2023–2024)
### 5.1 2024: Post-translational insertion and topology rectification for multipass proteins
Wu et al. (Nature Structural & Molecular Biology; publication date Nov 2024; URL https://doi.org/10.1038/s41594-023-01120-6) reported that C-terminal TMDs near the stop codon can be inserted **post-translationally by EMC**, enabling **topology rectification** after partial release from the ribosome–translocon. They propose this sequential co-translational + post-translational mechanism may apply to **~250** multipass proteins, including Cys-loop pentameric ion channel subunits critical for neurotransmission. (wu2024emcrectifiesthe pages 1-2, wu2024emcrectifiesthe pages 7-9)

Quantitative findings in the provided excerpts include: impaired insertion/translocation readouts **>50%** in EMC-deficient systems (e.g., reduced glycosylation proxy in a GABRA1 C-tail reporter, and reduced protected fragment recovery), indicating substantial dependence on EMC for terminal-TMD insertion in tested substrates. (wu2024emcrectifiesthe pages 3-4)

Importantly for MMGT1/EMC5 annotation, functional impairments observed with EMC perturbation were phenocopied by loss of **core subunits including EMC5** (along with EMC2/EMC3/EMC6) in GABAA receptor-related assays, reinforcing EMC5 as a required core component. (wu2024emcrectifiesthe pages 2-3)

### 5.2 2023: EMC selectivity filter that limits misinsertion
Pleiner et al. (Journal of Cell Biology; May 2023; URL https://doi.org/10.1083/jcb.202212007) used mutagenesis and crosslinking to map a TA-substrate path and define a **charge barrier** at the vestibule entrance (in EMC3) that limits ER misinsertion of mitochondrial tail-anchored proteins and helps enforce topology for some multipass clients. EMC5 is part of a hydrophobic crevice/cleft described as being lined by **EMC3/EMC5/EMC6**, linking EMC5 to the intramembrane landscape that partitions insertion-competent vs non-productive surfaces. (pleiner2023aselectivityfilter pages 10-11, pleiner2023aselectivityfilter pages 19-23)

---

## 6. Current applications and real-world implementations
### 6.1 Proteostasis modulation for ion channel variants (example: GABAA receptors)
A concrete translationally relevant application of EMC biology is **modulating EMC subunits to improve folding/trafficking/function of disease-associated membrane proteins**. In an iScience 2022 study focused on GABAA receptor proteostasis, overexpression of EMC3 increased surface levels of pathogenic receptor variants to **260%, 285%, and 148%**, while co-expression of **EMC5+EMC6** increased surface levels to **380%, 235%, and 285%** (variant-dependent). Electrophysiological peak currents were also increased substantially (e.g., values reported include 270→550 pA in one condition), supporting functional rescue. (whittsette2022theendoplasmicreticulum pages 14-16)

This type of strategy is best interpreted as **targeting an ER biogenesis factor network** rather than directly targeting MMGT1 as a magnesium transporter. The reported effects are consistent with the EMC functioning as an insertase/chaperone for challenging multipass substrates, including neurotransmitter receptors relevant to neurological disease mechanisms. (whittsette2022theendoplasmicreticulum pages 14-16, wu2024emcrectifiesthe pages 2-3)

### 6.2 Assay and screening use cases
EMC function is commonly interrogated using (i) TMD insertion reporters (tail-anchored and multipass), (ii) glycosylation/protease-protection insertion readouts in semi-permeabilized cell systems, and (iii) ribosome-proximity profiling (using EMC5 C-terminus fusions) to map which nascent membrane proteins are translated near EMC. These approaches are deployed to define EMC clients and insertion logic, enabling broader client prediction and mechanistic hypotheses about ER quality control. (hegde2022thefunctionstructure pages 19-20, wu2024emcrectifiesthe pages 3-4)

---

## 7. Expert opinions and authoritative analysis
Hegde’s 2022 Annual Review synthesis emphasizes that EMC has an established role in TMD insertion, but also highlights open questions: substrate range is not fully defined, and “membrane chaperone” functions during later folding/assembly are plausible and attractive given the challenges of stabilizing moderately hydrophobic and/or polar TMDs until assembly partners arrive. This aligns with the mechanistic partitioning emerging from structural and crosslinking work (insertase vestibule vs other intramembrane surfaces). (hegde2022thefunctionstructure pages 19-20, hegde2022thefunctionstructure pages 4-6)

---

## 8. Disease and phenotype associations
### 8.1 Ion-channel and neurotransmission-related phenotypes (mechanism-linked)
Multiple lines of experimental evidence connect EMC integrity (including EMC5 as core subunit) to the biogenesis and surface expression of Cys-loop neurotransmitter receptors (e.g., GABAA receptors), with quantitative reductions in surface expression to **<50%** after EMC perturbation and substantial rescue by EMC subunit overexpression in variant contexts. These findings provide mechanistically grounded links to neurological disease mechanisms where receptor folding/trafficking is limiting. (wu2024emcrectifiesthe pages 2-3, whittsette2022theendoplasmicreticulum pages 14-16)

### 8.2 Curated disease associations (OpenTargets)
OpenTargets reports MMGT1 (ENSG00000169446) associations including “developmental disorder of mental health,” hypotonia, myocardial ischemia, and others, supported by PubMed-linked evidence (e.g., PMID 33057194 appears in the OpenTargets evidence list). These associations are curated/aggregated and should be interpreted as hypothesis-generating unless supported by direct functional genetics and mechanistic studies. (OpenTargets Search: -MMGT1)

---

## 9. Statistics and data highlights (from recent studies)
* **~250 multipass proteins** potentially requiring EMC-mediated post-translational topology rectification (Wu et al., 2024). (wu2024emcrectifiesthe pages 1-2)
* EMC perturbation can reduce GABAA receptor surface expression to **<50%** in a reported knockdown experiment (Wu et al., 2024). (wu2024emcrectifiesthe pages 2-3)
* EMC loss impairs insertion/translocation readouts by **>50%** for tested terminal-TMD insertion events (e.g., GABRA1 C-tail glycosylation proxy) (Wu et al., 2024). (wu2024emcrectifiesthe pages 3-4)
* EMC5+EMC6 overexpression raised surface levels of disease-associated GABAA receptor α1 variants to **380%, 235%, 285%** (Whittsette et al., 2022). (whittsette2022theendoplasmicreticulum pages 14-16)
* Ribosome-proximity profiling found **local enrichments in ~53 mRNAs** near EMC, and one proteomics study cited in the review identified **21 proteins** with **≥50% reduction** after EMC1 perturbation in Xenopus (Hegde, 2022 review). (hegde2022thefunctionstructure pages 19-20)

---

## 10. Practical functional annotation for MMGT1/Q8N4V1 (recommended)
**Name/function (best-supported):** ER membrane protein complex subunit 5 (EMC5), a core ER membrane component required for EMC assembly and function in membrane protein biogenesis. (pleiner2020structuralbasisfor pages 1-3, whittsette2022theendoplasmicreticulum pages 1-2)

**Primary molecular role:** Structural/assembly subunit enabling EMC insertase/selectivity/topology-rectification functions; contributes to intramembrane architecture (clefts/grooves) and cytosolic interfaces with EMC2/EMC8. (pleiner2020structuralbasisfor pages 1-3, pleiner2023aselectivityfilter pages 19-23)

**Localization:** Endoplasmic reticulum membrane; C-terminus cytosolic; two-pass membrane topology in EMC context. (hegde2022thefunctionstructure pages 13-14, hegde2022thefunctionstructure pages 19-20)

**Substrate specificity:** EMC5 itself is not a substrate-binding “enzyme”; EMC clients include subsets of tail-anchored proteins and diverse multipass proteins where EMC contributes to insertion, selectivity, and post-translational topology completion. (pleiner2020structuralbasisfor pages 1-3, wu2024emcrectifiesthe pages 1-2)

**Magnesium transport:** No direct evidence for Mg2+ transport by EMC5/MMGT1 was found in the EMC-focused primary and review sources retrieved here; any magnesium-transport annotation should be treated as tentative without independent transport assays. (pleiner2020structuralbasisfor pages 1-3, whittsette2022theendoplasmicreticulum pages 1-2)


References

1. (pleiner2020structuralbasisfor pages 1-3): Tino Pleiner, Giovani Pinton Tomaleri, Kurt Januszyk, Alison J. Inglis, Masami Hazu, and Rebecca M. Voorhees. Structural basis for membrane insertion by the human er membrane protein complex. Jul 2020. URL: https://doi.org/10.1126/science.abb5008, doi:10.1126/science.abb5008. This article has 192 citations and is from a highest quality peer-reviewed journal.

2. (pleiner2023aselectivityfilter pages 19-23): Tino Pleiner, Masami Hazu, Giovani Pinton Tomaleri, Vy N. Nguyen, Kurt Januszyk, and Rebecca M. Voorhees. A selectivity filter in the er membrane protein complex limits protein misinsertion at the er. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202212007, doi:10.1083/jcb.202212007. This article has 28 citations.

3. (wu2024emcrectifiesthe pages 1-2): Haoxi Wu, Luka Smalinskaitė, and Ramanujan S. Hegde. Emc rectifies the topology of multipass membrane proteins. Nature Structural & Molecular Biology, 31:32-41, Nov 2024. URL: https://doi.org/10.1038/s41594-023-01120-6, doi:10.1038/s41594-023-01120-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

4. (whittsette2022theendoplasmicreticulum pages 1-2): Angela L. Whittsette, Ya-Juan Wang, and Ting-Wei Mu. The endoplasmic reticulum membrane complex promotes proteostasis of gabaa receptors. iScience, 25:104754, Aug 2022. URL: https://doi.org/10.1016/j.isci.2022.104754, doi:10.1016/j.isci.2022.104754. This article has 14 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: -MMGT1): Open Targets Query (-MMGT1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (hegde2022thefunctionstructure pages 13-14): Ramanujan S. Hegde. The function, structure, and origins of the er membrane protein complex. Annual Review of Biochemistry, 91:651-678, Jun 2022. URL: https://doi.org/10.1146/annurev-biochem-032620-104553, doi:10.1146/annurev-biochem-032620-104553. This article has 65 citations and is from a domain leading peer-reviewed journal.

7. (hegde2022thefunctionstructure pages 19-20): Ramanujan S. Hegde. The function, structure, and origins of the er membrane protein complex. Annual Review of Biochemistry, 91:651-678, Jun 2022. URL: https://doi.org/10.1146/annurev-biochem-032620-104553, doi:10.1146/annurev-biochem-032620-104553. This article has 65 citations and is from a domain leading peer-reviewed journal.

8. (hegde2022thefunctionstructure pages 4-6): Ramanujan S. Hegde. The function, structure, and origins of the er membrane protein complex. Annual Review of Biochemistry, 91:651-678, Jun 2022. URL: https://doi.org/10.1146/annurev-biochem-032620-104553, doi:10.1146/annurev-biochem-032620-104553. This article has 65 citations and is from a domain leading peer-reviewed journal.

9. (hegde2022thefunctionstructure pages 20-22): Ramanujan S. Hegde. The function, structure, and origins of the er membrane protein complex. Annual Review of Biochemistry, 91:651-678, Jun 2022. URL: https://doi.org/10.1146/annurev-biochem-032620-104553, doi:10.1146/annurev-biochem-032620-104553. This article has 65 citations and is from a domain leading peer-reviewed journal.

10. (pleiner2023aselectivityfilter pages 1-2): Tino Pleiner, Masami Hazu, Giovani Pinton Tomaleri, Vy N. Nguyen, Kurt Januszyk, and Rebecca M. Voorhees. A selectivity filter in the er membrane protein complex limits protein misinsertion at the er. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202212007, doi:10.1083/jcb.202212007. This article has 28 citations.

11. (wu2024emcrectifiesthe pages 7-9): Haoxi Wu, Luka Smalinskaitė, and Ramanujan S. Hegde. Emc rectifies the topology of multipass membrane proteins. Nature Structural & Molecular Biology, 31:32-41, Nov 2024. URL: https://doi.org/10.1038/s41594-023-01120-6, doi:10.1038/s41594-023-01120-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

12. (wu2024emcrectifiesthe pages 2-3): Haoxi Wu, Luka Smalinskaitė, and Ramanujan S. Hegde. Emc rectifies the topology of multipass membrane proteins. Nature Structural & Molecular Biology, 31:32-41, Nov 2024. URL: https://doi.org/10.1038/s41594-023-01120-6, doi:10.1038/s41594-023-01120-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

13. (whittsette2022theendoplasmicreticulum pages 14-16): Angela L. Whittsette, Ya-Juan Wang, and Ting-Wei Mu. The endoplasmic reticulum membrane complex promotes proteostasis of gabaa receptors. iScience, 25:104754, Aug 2022. URL: https://doi.org/10.1016/j.isci.2022.104754, doi:10.1016/j.isci.2022.104754. This article has 14 citations and is from a peer-reviewed journal.

14. (whittsette2022theendoplasmicreticuluma pages 35-41): AL Whittsette. The endoplasmic reticulum membrane complex promotes trafficking and function of gabaa receptors. Unknown journal, 2022.

15. (wu2024emcrectifiesthe pages 3-4): Haoxi Wu, Luka Smalinskaitė, and Ramanujan S. Hegde. Emc rectifies the topology of multipass membrane proteins. Nature Structural & Molecular Biology, 31:32-41, Nov 2024. URL: https://doi.org/10.1038/s41594-023-01120-6, doi:10.1038/s41594-023-01120-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

16. (hegde2022thefunctionstructure pages 1-2): Ramanujan S. Hegde. The function, structure, and origins of the er membrane protein complex. Annual Review of Biochemistry, 91:651-678, Jun 2022. URL: https://doi.org/10.1146/annurev-biochem-032620-104553, doi:10.1146/annurev-biochem-032620-104553. This article has 65 citations and is from a domain leading peer-reviewed journal.

17. (bai2020structureofthe pages 1-2): Lin Bai, Qinglong You, Xiang Feng, Amanda Kovach, and Huilin Li. Structure of the er membrane complex, a transmembrane-domain insertase. Jun 2020. URL: https://doi.org/10.1038/s41586-020-2389-3, doi:10.1038/s41586-020-2389-3. This article has 164 citations and is from a highest quality peer-reviewed journal.

18. (pleiner2020structuralbasisfor media a3da7fb7): Tino Pleiner, Giovani Pinton Tomaleri, Kurt Januszyk, Alison J. Inglis, Masami Hazu, and Rebecca M. Voorhees. Structural basis for membrane insertion by the human er membrane protein complex. Jul 2020. URL: https://doi.org/10.1126/science.abb5008, doi:10.1126/science.abb5008. This article has 192 citations and is from a highest quality peer-reviewed journal.

19. (pleiner2023aselectivityfilter pages 10-11): Tino Pleiner, Masami Hazu, Giovani Pinton Tomaleri, Vy N. Nguyen, Kurt Januszyk, and Rebecca M. Voorhees. A selectivity filter in the er membrane protein complex limits protein misinsertion at the er. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202212007, doi:10.1083/jcb.202212007. This article has 28 citations.

## Artifacts

- [Edison artifact artifact-00](MMGT1-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000020 Figure 1 shows the architecture of the human ER membrane protein complex (EMC). Subunit EMC5 is labeled in all panels (A-D). Panels](MMGT1-deep-research-falcon_artifacts/image-1.png)

## Citations

1. hegde2022thefunctionstructure pages 13-14
2. pleiner2020structuralbasisfor pages 1-3
3. hegde2022thefunctionstructure pages 19-20
4. wu2024emcrectifiesthe pages 3-4
5. wu2024emcrectifiesthe pages 2-3
6. whittsette2022theendoplasmicreticulum pages 14-16
7. wu2024emcrectifiesthe pages 1-2
8. pleiner2023aselectivityfilter pages 19-23
9. whittsette2022theendoplasmicreticulum pages 1-2
10. hegde2022thefunctionstructure pages 4-6
11. hegde2022thefunctionstructure pages 20-22
12. pleiner2023aselectivityfilter pages 1-2
13. wu2024emcrectifiesthe pages 7-9
14. whittsette2022theendoplasmicreticuluma pages 35-41
15. hegde2022thefunctionstructure pages 1-2
16. bai2020structureofthe pages 1-2
17. pleiner2023aselectivityfilter pages 10-11
18. https://doi.org/10.1126/science.abb5008;
19. https://doi.org/10.1016/j.isci.2022.104754;
20. https://platform.opentargets.org
21. https://doi.org/10.1146/annurev-biochem-032620-104553;
22. https://doi.org/10.1126/science.abb5008
23. https://doi.org/10.1146/annurev-biochem-032620-104553
24. https://doi.org/10.1083/jcb.202212007;
25. https://doi.org/10.1038/s41594-023-01120-6;
26. https://doi.org/10.18632/aging.205660
27. https://doi.org/10.1038/s41594-023-01120-6
28. https://doi.org/10.1083/jcb.202212007
29. https://doi.org/10.1126/science.abb5008,
30. https://doi.org/10.1083/jcb.202212007,
31. https://doi.org/10.1038/s41594-023-01120-6,
32. https://doi.org/10.1016/j.isci.2022.104754,
33. https://doi.org/10.1146/annurev-biochem-032620-104553,
34. https://doi.org/10.1038/s41586-020-2389-3,