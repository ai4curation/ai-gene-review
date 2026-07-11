---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:16:41.971216'
end_time: '2026-06-28T21:30:27.974733'
duration_seconds: 826.0
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24416
  interpro_name: Receptor Tyrosine Kinase
  interpro_short_name: RTK
  interpro_type: family
  interpro_integrated: IPR050122
  member_databases: Not specified
  n_proteins: '83290'
  n_taxa: '6103'
  n_subfamilies: '96'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The receptor tyrosine kinase family plays a crucial role in
    various cellular processes, including cell proliferation, differentiation, migration,
    and apoptosis. They act as cell-surface receptors for various ligands, such as
    fibroblast growth factors, insulin, and other growth factors, triggering intracellular
    signaling cascades that regulate embryonic development, the immune response, and
    the nervous system. Mutations or aberrant activation can lead to diseases like
    cancer. They are involved in angiogenesis, skeletal development, and maintaining
    vascular stability.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR24416-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24416-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR24416-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24416
- **Name:** Receptor Tyrosine Kinase
- **Short name:** RTK
- **Entry type:** family
- **Integrated into / parent:** IPR050122
- **Member database signatures:** Not specified
- **Scale:** 83290 proteins across 6103 taxa, 96 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The receptor tyrosine kinase family plays a crucial role in various cellular processes, including cell proliferation, differentiation, migration, and apoptosis. They act as cell-surface receptors for various ligands, such as fibroblast growth factors, insulin, and other growth factors, triggering intracellular signaling cascades that regulate embryonic development, the immune response, and the nervous system. Mutations or aberrant activation can lead to diseases like cancer. They are involved in angiogenesis, skeletal development, and maintaining vascular stability.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24416 (Receptor Tyrosine Kinase)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24416
- **Name:** Receptor Tyrosine Kinase
- **Short name:** RTK
- **Entry type:** family
- **Integrated into / parent:** IPR050122
- **Member database signatures:** Not specified
- **Scale:** 83290 proteins across 6103 taxa, 96 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The receptor tyrosine kinase family plays a crucial role in various cellular processes, including cell proliferation, differentiation, migration, and apoptosis. They act as cell-surface receptors for various ligands, such as fibroblast growth factors, insulin, and other growth factors, triggering intracellular signaling cascades that regulate embryonic development, the immune response, and the nervous system. Mutations or aberrant activation can lead to diseases like cancer. They are involved in angiogenesis, skeletal development, and maintaining vascular stability.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24416 (Receptor Tyrosine Kinase)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# InterPro2GO Annotation Review: PTHR24416 (Receptor Tyrosine Kinase Family)

## 1. Family Definition and Biochemistry

### 1.1 Structural Architecture

The Receptor Tyrosine Kinase (RTK) family (PTHR24416) encompasses single-pass transmembrane proteins with a characteristic modular architecture comprising: (i) a variable extracellular ligand-binding domain, (ii) a transmembrane α-helix, and (iii) an intracellular region containing a juxtamembrane regulatory region, a tyrosine kinase domain (TKD), and a C-terminal tail (ebrahimi2023receptortyrosinekinase pages 2-4, zhang2023receptortyrosinekinases pages 2-4). In humans, 58 RTKs have been identified and classified into 20 distinct subfamilies based primarily on their extracellular domain composition (ebrahimi2023receptortyrosinekinase pages 2-4, zhang2023receptortyrosinekinases pages 1-2). The extracellular regions are architecturally diverse, incorporating immunoglobulin-like domains, fibronectin type III repeats, cysteine-rich domains, EGF-like repeats, cadherin-like domains, and discoidin domains, depending on the subfamily (tomuleasa2024therapeuticadvancesof pages 2-3, bakhman2025structuralconservationand pages 1-4).

### 1.2 Kinase Domain Fold and Conserved Catalytic Residues

The intracellular TKD adopts the conserved bilobal protein kinase fold. As exemplified by EGFR, the N-terminal lobe contains five β-sheets and the catalytically critical αC-helix, while the larger C-terminal lobe consists of multiple α-helices (amelia2022structuralinsightand pages 3-5). The ATP-binding cleft lies between the two lobes beneath a conserved glycine-rich phosphate-binding loop (amelia2022structuralinsightand pages 3-5).

The catalytic mechanism depends on several universally conserved residues in active kinases:

- **Invariant lysine** (e.g., Lys721 in EGFR, Lys179 in PKA numbering): forms an essential salt bridge with the αC-helix glutamate and positions the γ-phosphate of ATP for phosphoryl transfer (reinhardt2023acriticalevaluation pages 2-3, amelia2022structuralinsightand pages 3-5).
- **Glutamate on the αC-helix** (e.g., Glu738 in EGFR): ion-pairs with the β3 lysine in the active conformation, stabilizing the catalytic site and the hydrophobic regulatory spine (reinhardt2023acriticalevaluation pages 2-3, paul2020genome‐wideandstructural pages 9-10, amelia2022structuralinsightand pages 3-5).
- **Catalytic aspartate in the HRD motif** (e.g., Asp812 in EGFR): acts as a catalytic base that hydrogen-bonds with the substrate hydroxyl group and facilitates nucleophilic attack on ATP (amelia2022structuralinsightand pages 3-5, paul2020genome‐wideandstructural pages 1-2).
- **DFG motif** (Asp-Phe-Gly): the aspartate in this motif coordinates Mg²⁺ ions essential for ATP binding; the phenylalanine forms part of the regulatory spine (reinhardt2023acriticalevaluation pages 2-3, amelia2022structuralinsightand pages 3-5, leroux2020renaissanceofallostery pages 2-2).

Together, the β3 lysine, HRD aspartate, and DFG aspartate constitute the "catalytic triad" of active protein kinases (paul2020genome‐wideandstructural pages 1-2). Loss of any of these residues, or substitution to non-canonical alternatives, is the hallmark defining pseudokinases (paul2020genome‐wideandstructural pages 13-14, paul2020genome‐wideandstructural pages 9-10, paul2020genome‐wideandstructural pages 1-2).

### 1.3 Activation Mechanism

RTKs are activated by ligand binding to their extracellular domains, which promotes receptor dimerization (or oligomerization) and subsequent trans-autophosphorylation of tyrosine residues within the activation loop and elsewhere on the intracellular domain (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 2-4). Phosphorylation of the activation loop relieves cis-autoinhibition, allowing the TKD to adopt an open, catalytically competent conformation that permits ATP and substrate access (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 2-4). Secondary autophosphorylation sites outside the kinase domain create docking sites for SH2- and PTB-domain-containing signaling proteins, propagating downstream cascades (jaradat2024targetingreceptortyrosine pages 3-4).

## 2. RTK Subfamily Classification

The following table provides a comprehensive overview of the 20 human RTK subfamilies, their members, biological functions, and annotation-relevant features including pseudokinase status.

| Class | Family name | Key members / receptors | Primary biological functions | Notable features |
|---|---|---|---|---|
| I | EGFR / ErbB | EGFR/ErbB1, ERBB2/HER2, ERBB3/HER3, ERBB4 | Cell proliferation, differentiation, survival; major epithelial growth-factor signaling | ERBB3/HER3 is a pseudokinase or very weak kinase-like RTK; important obligate dimerization partner in signaling (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2, sengupta2024connectingtheends pages 5-6, sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| II | Insulin receptor (IR) | INSR, IGF1R, IRR/INSRR | Carbohydrate, lipid and protein metabolism; growth control | Distinct pre-formed disulfide-linked receptor architecture relative to many other RTKs (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2, sengupta2024connectingtheends pages 5-6) |
| III | PDGFR | PDGFRA, PDGFRB, CSF1R, KIT, FLT3 | Tissue repair, hematopoiesis, cell proliferation, migration, angiogenesis | Includes stem-cell and hematopoietic receptors; strong disease relevance in myeloid and stromal tumors (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| IV | VEGFR | FLT1/VEGFR1, KDR/VEGFR2, FLT4/VEGFR3 | Angiogenesis, vascular development, lymphangiogenesis | Core vascular RTK family; major anti-angiogenic therapeutic targets (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| V | FGFR | FGFR1, FGFR2, FGFR3, FGFR4 | Embryonic development, tissue repair, skeletal development, proliferation | Broad developmental roles; recurrent fusions/mutations in cancer and skeletal disorders (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| VI | CCK / PTK7 | PTK7/CCK4 | Developmental signaling, cell polarity, migration; context-dependent proliferation control | PTK7 is catalytically inactive (pseudokinase) despite RTK architecture (jaradat2024targetingreceptortyrosine pages 3-4, ebrahimi2023receptortyrosinekinase pages 1-2, sengupta2024connectingtheends pages 5-6, sengupta2024connectingtheends pages 6-8, sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| VII | NGFR / Trk | NTRK1/TrkA, NTRK2/TrkB, NTRK3/TrkC | Neuronal development, survival, differentiation, synaptic function | Neurotrophin receptors; frequent oncogenic fusion partners (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| VIII | MET | MET, MST1R/RON | Cell growth, motility, morphogenesis, tissue regeneration | HGF/scatter-factor pathway family; strong roles in invasive growth programs (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| IX | EPHR / Eph | EPHA1-8, EPHA10, EPHB1-6 | Axon guidance, boundary formation, tissue patterning, synaptic plasticity | Largest RTK family; includes pseudokinase members such as EPHA10 and EPHB6; mediates cell-cell contact signaling (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2, sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| X | AXL / TAM | TYRO3, AXL, MERTK | Immune regulation, efferocytosis, tissue repair, survival signaling | Often immunosuppressive and pro-survival in tumors (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XI | TIE | TIE1, TEK/TIE2 | Angiogenesis, vascular remodeling, endothelial homeostasis | Endothelium-focused RTKs interacting with angiopoietins (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XII | RYK | RYK | Developmental signaling, especially Wnt-related patterning and axon guidance | Kinase domain lacks catalytic activity; functions as a pseudokinase/co-receptor (jaradat2024targetingreceptortyrosine pages 3-4, ebrahimi2023receptortyrosinekinase pages 1-2, sengupta2024connectingtheends pages 6-8, sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| XIII | DDR | DDR1, DDR2 | Extracellular matrix sensing, collagen response, adhesion, tissue remodeling | Unusual RTKs activated by collagen rather than soluble growth factors (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XIV | RET | RET | Embryogenesis, neural crest development, neuronal survival, kidney development | GDNF-family co-receptor system; major proto-oncogene in endocrine and lung cancers (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XV | ROS | ROS1 | Growth signaling, development; oncogenic when rearranged | Family represented by a single human receptor; best known through gene fusions in cancer (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XVI | LTK / ALK | ALK, LTK | Neuronal development, survival, immune-related functions | Clinically important oncogenic RTKs, especially ALK fusions and activating variants (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XVII | ROR | ROR1, ROR2 | Development, noncanonical Wnt signaling, metabolism, bone development | Commonly treated as pseudokinase/atypical kinase receptors, especially ROR1; important in developmental and cancer signaling (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2, sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| XVIII | MuSK | MUSK | Neuromuscular junction formation and maintenance | Highly specialized RTK essential for synapse organization in muscle (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XIX | LMR / AATYK | AATK/AATYK1, AATYK2, AATYK3 | Neuronal differentiation and signaling | Often listed as LMR/AATYK atypical receptor-like kinases; less canonical extracellular architecture in some classifications (zhang2023receptortyrosinekinases pages 1-2, ebrahimi2023receptortyrosinekinase pages 1-2) |
| XX | STYK1* | STYK1/NOK | Growth and oncogenic signaling (reported in some classifications) | Included as a 20th class in some modern summaries; atypical relative to classical ligand-activated cell-surface RTKs and not consistently represented across review tables (zhang2023receptortyrosinekinases pages 1-2, bakhman2025structuralconservationand pages 1-4) |


*Table: This table summarizes the human receptor tyrosine kinase classes, representative members, broad biological roles, and annotation-relevant caveats such as pseudokinase status. It is useful for judging whether any GO term could plausibly apply across the entire PTHR24416 family.*

## 3. Functional Divergence Across the Family

### 3.1 Radical Functional Heterogeneity

The 20 RTK subfamilies serve radically different biological roles. These include: carbohydrate/lipid/protein metabolism (insulin receptor family), angiogenesis and vascular development (VEGFR, Tie), neuronal development and survival (Trk, ALK/LTK), axon guidance and tissue boundary formation (Eph), skeletal development (FGFR), immune regulation and efferocytosis (TAM/AXL), neuromuscular junction formation (MuSK), extracellular matrix sensing (DDR), and developmental Wnt co-reception (RYK, ROR) (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2). This diversity means no single biological process GO term can accurately describe all family members.

### 3.2 Pseudokinase (Catalytically Dead) Members

Approximately 10% of metazoan RTKs are pseudokinases—they retain the bilobal kinase fold but lack one or more conserved catalytic residues and have lost phosphotransferase activity (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4). These pseudokinases signal through conformational switching, allosteric regulation of binding partners, and scaffolding functions rather than catalysis (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4).

| RTK name | Subfamily | Catalytic residue defects | ATP binding status | Signaling mechanism (non-catalytic) |
|---|---|---|---|---|
| PTK7 | CCK/PTK7 | Pseudokinase domain with loss/substitution of canonical catalytic residues required for phosphotransfer; classified as catalytically inactive RTK pseudokinase (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | Does not bind ATP (sheetz2021structuralinsightsinto pages 3-4) | Functions through kinase-independent scaffolding/co-receptor roles and allosteric regulation of signaling complexes rather than phosphotransfer (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| RYK | RYK | Tyrosine kinase domain lacks catalytic activity because of noncanonical substitutions in conserved kinase motifs; classified as RTK pseudokinase (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | Does not bind ATP (sheetz2021structuralinsightsinto pages 3-4) | Signals as a non-catalytic receptor/co-receptor, especially in developmental pathways, via protein interactions and conformational regulation rather than kinase activity (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| ErbB3 / HER3 | EGFR/ErbB | Multiple substitutions in canonical kinase catalytic motifs render it catalytically impaired/very weak relative to active ErbBs; categorized among RTK pseudokinases/kinase-impaired receptors (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | Binds ATP (sheetz2021structuralinsightsinto pages 3-4) | Functions mainly as an allosteric activator and dimerization partner within ErbB complexes; signaling depends primarily on heterodimerization and recruitment of downstream effectors rather than robust intrinsic catalysis (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| EphB6 | Eph | Catalytically dead Eph-family pseudokinase with substitutions/losses in conserved catalytic residues; noted to have major activation-loop deterioration in pseudokinase-focused work (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | Binds ATP (sheetz2021structuralinsightsinto pages 3-4) | Mediates catalysis-independent signaling through conformational/allosteric effects and receptor interactions within Eph/ephrin signaling systems (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4, sheetz2021structuralinsightsinto pages 15-16) |
| EphA10 | Eph | Vertebrate Eph-family pseudokinase derived from active Eph receptors; carries co-evolved sequence changes in motifs important for nucleotide binding/catalysis, consistent with loss of canonical kinase activity (sheetz2021structuralinsightsinto pages 1-3, shrestha2020cataloguingthedead pages 14-16) | Not clearly established in the cited evidence; pseudokinase status indicates impaired catalytic function, but ATP-binding status is not specified in the available context (sheetz2021structuralinsightsinto pages 1-3, shrestha2020cataloguingthedead pages 14-16) | Likely signals through catalysis-independent receptor interactions and conformational regulation, analogous to other RTK pseudokinases (sheetz2021structuralinsightsinto pages 1-3, shrestha2020cataloguingthedead pages 14-16) |
| ROR1 | ROR | RTK pseudokinase with substitutions in conserved catalytic motifs sufficient to abolish phosphotransfer competence (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | Does not bind ATP (sheetz2021structuralinsightsinto pages 3-4) | Functions in noncanonical receptor signaling via scaffolding/co-receptor behavior and conformational control rather than tyrosine phosphorylation (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |
| ROR2 | ROR | RTK pseudokinase/atypical kinase with disrupted canonical catalytic motifs; included among catalytically inactive RTK pseudokinases (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | Does not bind ATP (sheetz2021structuralinsightsinto pages 3-4) | Signals in developmental/Wnt-related pathways through kinase-independent receptor complex formation and allosteric regulation (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) |


*Table: This table summarizes key receptor tyrosine kinase pseudokinases, their catalytic defects, ATP-binding behavior, and non-catalytic signaling modes. It is useful for GO review because it shows why kinase-activity terms cannot be safely propagated to all members of the broad RTK family.*

Key examples include:
- **PTK7, RYK, ROR1, ROR2**: completely fail to bind ATP and lack catalytic activity (sheetz2021structuralinsightsinto pages 3-4).
- **ErbB3/HER3**: binds ATP but displays only very weak residual kinase activity; its signaling depends on heterodimerization with active ErbB family members, not on its own catalytic function (sheetz2021structuralinsightsinto pages 3-4).
- **EphB6**: binds ATP but is catalytically dead, lacking 14 activation loop residues including the conserved tyrosine (sheetz2021structuralinsightsinto pages 1-3).
- **EphA10**: vertebrate-specific pseudokinase derived from active Eph receptors through co-evolved sequence changes (sheetz2021structuralinsightsinto pages 1-3, shrestha2020cataloguingthedead pages 14-16).

These pseudokinases adopt conformations closely resembling the autoinhibited (inactive) state of their kinase-active homologs, yet maintain significant conformational dynamics enabling allosteric signaling (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4). Their ATP-binding pockets are typically occluded by aromatic residues, and alternative intra-domain interactions substitute for the absent canonical catalytic motifs (sheetz2021structuralinsightsinto pages 1-3).

### 3.3 Neo-functionalization Examples

Beyond simple loss of catalysis, several RTK subfamilies have undergone neo-functionalization:
- **DDR1/DDR2** are unique among RTKs in being activated by collagen rather than soluble growth factors, coupling them to extracellular matrix biology rather than classical growth factor signaling (jaradat2024targetingreceptortyrosine pages 3-4).
- **RYK** and **ROR1/ROR2** function primarily as co-receptors in Wnt signaling pathways, a fundamentally different biological axis from the canonical RTK-growth factor paradigm (jaradat2024targetingreceptortyrosine pages 3-4).
- **ErbB3/HER3** has been repurposed as an obligate allosteric activator in ErbB heterodimer complexes, making its role fundamentally different from that of a catalytic kinase (sheetz2021structuralinsightsinto pages 3-4).

## 4. Taxonomic Scope

### 4.1 Evolutionary Origin

RTK-related tyrosine kinase signaling is not restricted to metazoans. The choanoflagellate *Monosiga brevicollis*, a unicellular premetazoan, possesses a tyrosine kinase signaling network that is more elaborate and diverse than any known metazoan system (yeung2021evolutionoffunctional pages 13-14). Ancestral tyrosine kinase subgroups including SrcM, IRKL, and Csk originated in unicellular premetazoans and were subsequently co-opted for complex multicellular functions (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10).

### 4.2 Lineage-Specific Expansions

Different RTK subfamilies emerged at different evolutionary stages:
- **SrcM, IRKL, Tec, Csk** families are detected across diverse holozoan taxa including choanoflagellates and filastereans (yeung2021evolutionoffunctional pages 3-6).
- The **FPVR subgroup** (encompassing FGFR, PDGFR, VEGFR-related families) emerged later in eumetazoans after divergence from poriferans (yeung2021evolutionoffunctional pages 3-6).
- The **PVR subgroup** appears only in deuterostomes (yeung2021evolutionoffunctional pages 3-6).
- Lineage-specific RTK families exist in choanoflagellates (RTKA, RTKB, HMTK, RTKC), sponges (Src-Aque1), and nematodes (KIN6, KIN16), with generally low orthology to metazoan RTK networks (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10).

### 4.3 Implications for GO Annotation

The PTHR24416 entry covers 83,290 proteins across 6,103 taxa and 96 subfamilies. Given this extraordinary taxonomic breadth—spanning unicellular holozoans through vertebrates—and the presence of organism-specific RTK families with limited functional characterization, any process or component GO term mapped at this level risks propagating annotations to taxa where the relevant biology may be absent or fundamentally different (yeung2021evolutionoffunctional pages 13-14, yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10, yeung2021evolutionoffunctional pages 14-15).

## 5. InterPro2GO Mapping Appropriateness

### 5.1 Current Status

PTHR24416 currently has **no InterPro2GO terms mapped**. This report evaluates whether this absence is appropriate and whether any GO terms could or should be added.

### 5.2 Evaluation of Candidate GO Terms

| GO Term (potential) | GO ID | Aspect (MF/BP/CC) | Applies to ALL members? | Problematic members / exceptions | Recommended action |
|---|---|---|---|---|---|
| transmembrane receptor protein tyrosine kinase activity | GO:0004714 | MF | No | Pseudokinase RTKs lack catalytic activity, including PTK7, RYK, ROR1/2, EphB6, EphA10, and ErbB3/HER3-like weak/dead members; therefore not true for every match in this broad family (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4, sengupta2024connectingtheends pages 6-8) | REMOVE |
| protein tyrosine kinase activity | GO:0004713 | MF | No | Same issue as above; catalytic phosphotransfer is absent or severely reduced in multiple RTK subfamilies/pseudokinases, so this would over-annotate inactive family members (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4, reinhardt2023acriticalevaluation pages 2-3, paul2020genome‐wideandstructural pages 1-2) | REMOVE |
| ATP binding | GO:0005524 | MF | No | Some RTK pseudokinases fail to bind ATP altogether (PTK7, ROR1/2, RYK), while others may bind weakly or atypically; term is also extremely generic (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | REMOVE |
| protein phosphorylation | GO:0006468 | BP | No | Not all family members catalyze phosphorylation; even among active RTKs, downstream biology is diverse and this term adds little specificity at family level (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4, ebrahimi2023receptortyrosinekinase pages 2-4) | REMOVE |
| signal transduction | GO:0007165 | BP | Probably yes biologically, but too broad for useful family annotation | Although most RTKs or RTK-like pseudokinases participate in signaling, mechanisms vary radically across 20 subfamilies and across taxa; the term is uninformative and risks masking major divergence (jaradat2024targetingreceptortyrosine pages 3-4, sengupta2024connectingtheends pages 6-8, yeung2021evolutionoffunctional pages 13-14, yeung2021evolutionoffunctional pages 3-6) | KEEP_AS_NON_CORE |
| transmembrane signaling receptor activity | GO:0004888 | MF | Likely yes for the canonical family concept, but caution needed | Broadly consistent with shared architecture as membrane-spanning receptors that transmit extracellular cues; however some lineage-specific or highly derived members may challenge strict universality, and the term is still quite generic (ebrahimi2023receptortyrosinekinase pages 2-4, zhang2023receptortyrosinekinases pages 2-4, sengupta2024connectingtheends pages 6-8, yeung2021evolutionoffunctional pages 14-15) | KEEP_AS_NON_CORE |
| integral component of membrane | GO:0016021 | CC | Likely yes for canonical RTKs, but low information value | RTKs are classically single-pass membrane proteins; nevertheless this is a very generic location term with limited value for InterPro2GO review (ebrahimi2023receptortyrosinekinase pages 2-4, zhang2023receptortyrosinekinases pages 2-4) | KEEP_AS_NON_CORE |
| plasma membrane | GO:0005886 | CC | Usually, but not safely universal across all taxa/contexts | RTKs are generally cell-surface receptors in animals, but taxonomic breadth across holozoans and lineage-specific biology makes this less safe as a universal component term; also proteins can signal from endomembranes after trafficking/cleavage (yeung2021evolutionoffunctional pages 13-14, yeung2021evolutionoffunctional pages 3-6, sengupta2024connectingtheends pages 6-8) | KEEP_AS_NON_CORE |
| protein autophosphorylation | GO:0046777 | BP | No | Activation-loop or tail autophosphorylation is central for many active RTKs, but impossible for catalytically dead pseudokinases and not uniformly established across the whole family (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 2-4, sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4) | REMOVE |
| cell surface receptor signaling pathway | GO:0007166 | BP | Broadly plausible, but too heterogeneous for core mapping | Many RTKs and RTK pseudokinases transmit extracellular signals at the cell surface, yet pathways differ dramatically among subfamilies (insulin signaling, angiogenesis, axon guidance, Wnt co-reception, immune regulation), so the term is true only at an overly generic level (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2, sengupta2024connectingtheends pages 6-8, yeung2021evolutionoffunctional pages 13-14) | KEEP_AS_NON_CORE |


*Table: This table evaluates plausible GO terms for the broad PTHR24416 receptor tyrosine kinase family and indicates whether each is universal enough to annotate every matched protein. It is useful for deciding why the current absence of InterPro2GO mappings is largely justified and which terms, if any, could be retained only as non-core generic annotations.*

### 5.3 Analysis

**Molecular Function terms**: The most intuitive MF term for RTKs—"transmembrane receptor protein tyrosine kinase activity" (GO:0004714)—cannot be safely applied to all family members because ~10% of metazoan RTKs are pseudokinases that lack catalytic phosphotransferase activity entirely (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4). Similarly, "ATP binding" (GO:0005524) fails for PTK7, RYK, ROR1, and ROR2, which do not bind ATP (sheetz2021structuralinsightsinto pages 3-4). More generic terms like "transmembrane signaling receptor activity" (GO:0004888) are broadly plausible but carry minimal informational value (ebrahimi2023receptortyrosinekinase pages 2-4).

**Biological Process terms**: No single BP term captures the biology of all RTK subfamilies. The 20 subfamilies participate in radically different processes including carbohydrate metabolism, angiogenesis, neural development, axon guidance, immune regulation, neuromuscular junction formation, and Wnt signaling (jaradat2024targetingreceptortyrosine pages 3-4). Even high-level terms such as "signal transduction" (GO:0007165) or "cell surface receptor signaling pathway" (GO:0007166), while broadly true, are so generic as to be uninformative and would mask the critical functional diversity within the family.

**Cellular Component terms**: "Integral component of membrane" (GO:0016021) is consistent with the single-pass transmembrane architecture shared by canonical RTKs, but its low specificity provides minimal annotation value. "Plasma membrane" (GO:0005886) is not safely universal given that some RTKs undergo regulated intracellular trafficking, nuclear translocation, or shedding (sengupta2024connectingtheends pages 6-8).

## 6. Over-Annotation Verdict

### 6.1 Summary Assessment

The current absence of InterPro2GO mappings for PTHR24416 is **appropriate and sound**. This family-level PANTHER entry encompasses an extraordinarily heterogeneous superfamily of 83,290 proteins across 6,103 taxa and 96 subfamilies. Three major factors prevent any GO term from being universally appropriate:

1. **Catalytic heterogeneity**: ~10% of RTKs are pseudokinases that lack kinase activity and often cannot bind ATP, making catalytic MF terms systematically incorrect for these members (sheetz2021structuralinsightsinto pages 1-3, sheetz2021structuralinsightsinto pages 3-4).
2. **Functional heterogeneity**: The 20 subfamilies serve radically different biological roles across all major physiological systems, making any specific BP term applicable only to subsets (jaradat2024targetingreceptortyrosine pages 3-4, zhang2023receptortyrosinekinases pages 1-2).
3. **Taxonomic heterogeneity**: The family spans from unicellular holozoans to vertebrates, with lineage-specific expansions and limited cross-taxon functional conservation (yeung2021evolutionoffunctional pages 13-14, yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10).

### 6.2 Recommended GO Action Pattern

| Recommendation | Details |
|---|---|
| **Overall verdict** | **ACCEPT current state (no GO terms mapped)** — The absence of InterPro2GO mappings is well-justified for this highly heterogeneous family-level entry. |
| **Catalytic MF terms** (e.g., protein tyrosine kinase activity, ATP binding) | **REMOVE / DO NOT ADD** — Would over-annotate pseudokinase members. |
| **Generic MF terms** (e.g., transmembrane signaling receptor activity) | **KEEP_AS_NON_CORE at most** — Broadly true but too generic to add value; could be considered only if InterPro policy requires some annotation at this level. |
| **Specific BP terms** (e.g., protein phosphorylation, any specific signaling pathway) | **REMOVE / DO NOT ADD** — Only true for subsets; would systematically over-annotate. |
| **Generic CC terms** (e.g., integral component of membrane, plasma membrane) | **KEEP_AS_NON_CORE at most** — Low information value; broadly true for canonical members but not sufficiently specific to justify addition. |

### 6.3 Recommendations for InterPro

- **Maintain PTHR24416 without family-level GO terms.** GO terms should instead be pushed to the 96 child subfamily entries, where functional homogeneity is higher and catalytic/pseudokinase status can be accurately reflected.
- For active RTK subfamilies (e.g., EGFR active members, insulin receptor, FGFR), subfamily-specific entries could appropriately carry "transmembrane receptor protein tyrosine kinase activity" (GO:0004714), "ATP binding" (GO:0005524), and relevant process terms.
- For pseudokinase-containing subfamilies (e.g., PTK7, RYK, ROR), these catalytic terms must be excluded, and more appropriate terms describing their actual signaling mechanism (e.g., "transmembrane signaling receptor activity") should be used.
- Process-level GO terms (e.g., "axon guidance" for Eph receptors, "glucose homeostasis" for insulin receptors) should be mapped only at the subfamily level where biological specificity is justified.

In conclusion, the PTHR24416 entry's current lack of InterPro2GO mappings reflects an appropriate recognition that this broad family-level signature cannot support any GO term that is simultaneously true for all matched proteins and informative enough to be useful for annotation.

References

1. (ebrahimi2023receptortyrosinekinase pages 2-4): Nasim Ebrahimi, Elmira Fardi, Hajarossadat Ghaderi, Sahar Palizdar, Roya Khorram, Reza Vafadar, Masoud Ghanaatian, Fatemeh Rezaei-Tazangi, Payam Baziyar, Amirhossein Ahmadi, Michael R. Hamblin, and Amir Reza Aref. Receptor tyrosine kinase inhibitors in cancer. Cellular and Molecular Life Sciences, 80:1-18, Mar 2023. URL: https://doi.org/10.1007/s00018-023-04729-4, doi:10.1007/s00018-023-04729-4. This article has 169 citations and is from a domain leading peer-reviewed journal.

2. (zhang2023receptortyrosinekinases pages 2-4): Nan Zhang and Yongsheng Li. Receptor tyrosine kinases: biological functions and anticancer targeted therapy. MedComm, Dec 2023. URL: https://doi.org/10.1002/mco2.446, doi:10.1002/mco2.446. This article has 90 citations.

3. (zhang2023receptortyrosinekinases pages 1-2): Nan Zhang and Yongsheng Li. Receptor tyrosine kinases: biological functions and anticancer targeted therapy. MedComm, Dec 2023. URL: https://doi.org/10.1002/mco2.446, doi:10.1002/mco2.446. This article has 90 citations.

4. (tomuleasa2024therapeuticadvancesof pages 2-3): C. Tomuleasa, A. Țigu, R. Munteanu, C. Moldovan, D. Kegyes, Anca Onaciu, Diana Gulei, Gabriel Ghiaur, Hermann Einsele, and Carlo M. Croce. Therapeutic advances of targeting receptor tyrosine kinases in cancer. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01899-w, doi:10.1038/s41392-024-01899-w. This article has 278 citations and is from a peer-reviewed journal.

5. (bakhman2025structuralconservationand pages 1-4): Anna Fassler Bakhman, Rachel Kolodny, and Mickey Kosloff. Structural conservation and divergence across the receptor tyrosine kinase superfamily. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2024.12.31.630944, doi:10.1101/2024.12.31.630944. This article has 2 citations.

6. (amelia2022structuralinsightand pages 3-5): Tasia Amelia, Rahmana Emran Kartasasmita, Tomohiko Ohwada, and Daryono Hadi Tjahjono. Structural insight and development of egfr tyrosine kinase inhibitors. Molecules, 27:819, Jan 2022. URL: https://doi.org/10.3390/molecules27030819, doi:10.3390/molecules27030819. This article has 155 citations.

7. (reinhardt2023acriticalevaluation pages 2-3): Ronja Reinhardt and Thomas A Leonard. A critical evaluation of protein kinase regulation by activation loop autophosphorylation. eLife, Jul 2023. URL: https://doi.org/10.7554/elife.88210, doi:10.7554/elife.88210. This article has 88 citations and is from a domain leading peer-reviewed journal.

8. (paul2020genome‐wideandstructural pages 9-10): Anindita Paul and Narayanaswamy Srinivasan. Genome‐wide and structural analyses of pseudokinases encoded in the genome of <scp><i>arabidopsis thaliana</i></scp> provide functional insights. Aug 2020. URL: https://doi.org/10.1002/prot.25981, doi:10.1002/prot.25981. This article has 16 citations.

9. (paul2020genome‐wideandstructural pages 1-2): Anindita Paul and Narayanaswamy Srinivasan. Genome‐wide and structural analyses of pseudokinases encoded in the genome of <scp><i>arabidopsis thaliana</i></scp> provide functional insights. Aug 2020. URL: https://doi.org/10.1002/prot.25981, doi:10.1002/prot.25981. This article has 16 citations.

10. (leroux2020renaissanceofallostery pages 2-2): Alejandro E. Leroux and Ricardo M. Biondi. Renaissance of allostery to disrupt protein kinase interactions. Trends in biochemical sciences, 45:27-41, Jan 2020. URL: https://doi.org/10.1016/j.tibs.2019.09.007, doi:10.1016/j.tibs.2019.09.007. This article has 52 citations and is from a domain leading peer-reviewed journal.

11. (paul2020genome‐wideandstructural pages 13-14): Anindita Paul and Narayanaswamy Srinivasan. Genome‐wide and structural analyses of pseudokinases encoded in the genome of <scp><i>arabidopsis thaliana</i></scp> provide functional insights. Aug 2020. URL: https://doi.org/10.1002/prot.25981, doi:10.1002/prot.25981. This article has 16 citations.

12. (jaradat2024targetingreceptortyrosine pages 3-4): Sara K. Jaradat, Nehad M. Ayoub, Ahmed H. Al Sharie, and Julia M. Aldaod. Targeting receptor tyrosine kinases as a novel strategy for the treatment of triple-negative breast cancer. Technology in Cancer Research & Treatment, Jan 2024. URL: https://doi.org/10.1177/15330338241234780, doi:10.1177/15330338241234780. This article has 25 citations and is from a peer-reviewed journal.

13. (ebrahimi2023receptortyrosinekinase pages 1-2): Nasim Ebrahimi, Elmira Fardi, Hajarossadat Ghaderi, Sahar Palizdar, Roya Khorram, Reza Vafadar, Masoud Ghanaatian, Fatemeh Rezaei-Tazangi, Payam Baziyar, Amirhossein Ahmadi, Michael R. Hamblin, and Amir Reza Aref. Receptor tyrosine kinase inhibitors in cancer. Cellular and Molecular Life Sciences, 80:1-18, Mar 2023. URL: https://doi.org/10.1007/s00018-023-04729-4, doi:10.1007/s00018-023-04729-4. This article has 169 citations and is from a domain leading peer-reviewed journal.

14. (sengupta2024connectingtheends pages 5-6): Priyanka Sengupta, Russa Das, Piyali Majumder, and Debashis Mukhopadhyay. Connecting the ends: signaling via receptor tyrosine kinases and cytoskeletal degradation in neurodegeneration. Exploration of Neuroscience, 3:1-26, Feb 2024. URL: https://doi.org/10.37349/en.2024.00033, doi:10.37349/en.2024.00033. This article has 18 citations.

15. (sheetz2021structuralinsightsinto pages 1-3): Joshua B. Sheetz, Sebastian Mathea, Hanna Karvonen, Ketan Malhotra, Deep Chatterjee, Wilhelmiina Niininen, Robert Perttilä, Franziska Preuss, Krishna Suresh, Steven E. Stayrook, Yuko Tsutsui, Ravi Radhakrishnan, Daniela Ungureanu, Stefan Knapp, and Mark A. Lemmon. Structural insights into pseudokinase domains of receptor tyrosine kinases. The FASEB Journal, 35:390-405.e7, May 2021. URL: https://doi.org/10.1096/fasebj.2021.35.s1.02446, doi:10.1096/fasebj.2021.35.s1.02446. This article has 107 citations.

16. (sheetz2021structuralinsightsinto pages 3-4): Joshua B. Sheetz, Sebastian Mathea, Hanna Karvonen, Ketan Malhotra, Deep Chatterjee, Wilhelmiina Niininen, Robert Perttilä, Franziska Preuss, Krishna Suresh, Steven E. Stayrook, Yuko Tsutsui, Ravi Radhakrishnan, Daniela Ungureanu, Stefan Knapp, and Mark A. Lemmon. Structural insights into pseudokinase domains of receptor tyrosine kinases. The FASEB Journal, 35:390-405.e7, May 2021. URL: https://doi.org/10.1096/fasebj.2021.35.s1.02446, doi:10.1096/fasebj.2021.35.s1.02446. This article has 107 citations.

17. (sengupta2024connectingtheends pages 6-8): Priyanka Sengupta, Russa Das, Piyali Majumder, and Debashis Mukhopadhyay. Connecting the ends: signaling via receptor tyrosine kinases and cytoskeletal degradation in neurodegeneration. Exploration of Neuroscience, 3:1-26, Feb 2024. URL: https://doi.org/10.37349/en.2024.00033, doi:10.37349/en.2024.00033. This article has 18 citations.

18. (sheetz2021structuralinsightsinto pages 15-16): Joshua B. Sheetz, Sebastian Mathea, Hanna Karvonen, Ketan Malhotra, Deep Chatterjee, Wilhelmiina Niininen, Robert Perttilä, Franziska Preuss, Krishna Suresh, Steven E. Stayrook, Yuko Tsutsui, Ravi Radhakrishnan, Daniela Ungureanu, Stefan Knapp, and Mark A. Lemmon. Structural insights into pseudokinase domains of receptor tyrosine kinases. The FASEB Journal, 35:390-405.e7, May 2021. URL: https://doi.org/10.1096/fasebj.2021.35.s1.02446, doi:10.1096/fasebj.2021.35.s1.02446. This article has 107 citations.

19. (shrestha2020cataloguingthedead pages 14-16): Safal Shrestha, Dominic P. Byrne, John A. Harris, Natarajan Kannan, and Patrick A. Eyers. Cataloguing the dead: breathing new life into pseudokinase research. Mar 2020. URL: https://doi.org/10.1111/febs.15246, doi:10.1111/febs.15246. This article has 54 citations.

20. (yeung2021evolutionoffunctional pages 13-14): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

21. (yeung2021evolutionoffunctional pages 3-6): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

22. (yeung2021evolutionoffunctional pages 9-10): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

23. (yeung2021evolutionoffunctional pages 14-15): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR24416-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24416-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR24416-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. amelia2022structuralinsightand pages 3-5
2. jaradat2024targetingreceptortyrosine pages 3-4
3. sheetz2021structuralinsightsinto pages 3-4
4. sheetz2021structuralinsightsinto pages 1-3
5. yeung2021evolutionoffunctional pages 13-14
6. yeung2021evolutionoffunctional pages 3-6
7. ebrahimi2023receptortyrosinekinase pages 2-4
8. sengupta2024connectingtheends pages 6-8
9. zhang2023receptortyrosinekinases pages 2-4
10. zhang2023receptortyrosinekinases pages 1-2
11. tomuleasa2024therapeuticadvancesof pages 2-3
12. bakhman2025structuralconservationand pages 1-4
13. reinhardt2023acriticalevaluation pages 2-3
14. leroux2020renaissanceofallostery pages 2-2
15. ebrahimi2023receptortyrosinekinase pages 1-2
16. sengupta2024connectingtheends pages 5-6
17. sheetz2021structuralinsightsinto pages 15-16
18. shrestha2020cataloguingthedead pages 14-16
19. yeung2021evolutionoffunctional pages 9-10
20. yeung2021evolutionoffunctional pages 14-15
21. https://doi.org/10.1007/s00018-023-04729-4,
22. https://doi.org/10.1002/mco2.446,
23. https://doi.org/10.1038/s41392-024-01899-w,
24. https://doi.org/10.1101/2024.12.31.630944,
25. https://doi.org/10.3390/molecules27030819,
26. https://doi.org/10.7554/elife.88210,
27. https://doi.org/10.1002/prot.25981,
28. https://doi.org/10.1016/j.tibs.2019.09.007,
29. https://doi.org/10.1177/15330338241234780,
30. https://doi.org/10.37349/en.2024.00033,
31. https://doi.org/10.1096/fasebj.2021.35.s1.02446,
32. https://doi.org/10.1111/febs.15246,
33. https://doi.org/10.1093/molbev/msab272,