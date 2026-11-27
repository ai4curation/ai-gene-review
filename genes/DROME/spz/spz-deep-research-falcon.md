---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:14:57.967155'
end_time: '2026-09-30T06:28:15.304038'
duration_seconds: 797.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: spz
  gene_symbol: spz
  uniprot_accession: P48607
  protein_description: 'RecName: Full=Protein spaetzle {ECO:0000312|FlyBase:FBgn0003495};
    AltName: Full=Protein spatzle {ECO:0000312|FlyBase:FBgn0003495}; Contains: RecName:
    Full=Protein spaetzle C-106; Flags: Precursor;'
  gene_info: Name=spz {ECO:0000312|FlyBase:FBgn0003495}; ORFNames=CG6134 {ECO:0000312|FlyBase:FBgn0003495};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: Cystine-knot_cytokine. (IPR029034); Spaetzle. (IPR032104); Spz/Toll_ligand-like.
    (IPR052444); Spaetzle (PF16077)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 51
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: spz-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: spz-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** P48607
- **Protein Description:** RecName: Full=Protein spaetzle {ECO:0000312|FlyBase:FBgn0003495}; AltName: Full=Protein spatzle {ECO:0000312|FlyBase:FBgn0003495}; Contains: RecName: Full=Protein spaetzle C-106; Flags: Precursor;
- **Gene Information:** Name=spz {ECO:0000312|FlyBase:FBgn0003495}; ORFNames=CG6134 {ECO:0000312|FlyBase:FBgn0003495};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Cystine-knot_cytokine. (IPR029034); Spaetzle. (IPR032104); Spz/Toll_ligand-like. (IPR052444); Spaetzle (PF16077)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "spz" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'spz' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **spz** (gene ID: spz, UniProt: P48607) in DROME.

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
- **UniProt Accession:** P48607
- **Protein Description:** RecName: Full=Protein spaetzle {ECO:0000312|FlyBase:FBgn0003495}; AltName: Full=Protein spatzle {ECO:0000312|FlyBase:FBgn0003495}; Contains: RecName: Full=Protein spaetzle C-106; Flags: Precursor;
- **Gene Information:** Name=spz {ECO:0000312|FlyBase:FBgn0003495}; ORFNames=CG6134 {ECO:0000312|FlyBase:FBgn0003495};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Cystine-knot_cytokine. (IPR029034); Spaetzle. (IPR032104); Spz/Toll_ligand-like. (IPR052444); Spaetzle (PF16077)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "spz" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'spz' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **spz** (gene ID: spz, UniProt: P48607) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Drosophila melanogaster Spaetzle (spz gene, UniProt P48607)

## Gene and Protein Identity

The *spz* gene (UniProt accession P48607) encodes **Spaetzle** (also spelled Spätzle), a secreted cytokine-like signaling protein in *Drosophila melanogaster*. The protein is produced as a precursor with multiple names including "Protein spaetzle," "Protein spatzle," and its mature processed form "Protein spaetzle C-106" (dine2022functionalcharacterizationof pages 26-32). Spaetzle belongs to the Spätzle family of cystine-knot domain-containing proteins and functions as the canonical extracellular ligand for Toll receptors (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2).

## Primary Molecular Function

**Spaetzle is not an enzyme.** It has no catalytic activity, does not process substrates, and exhibits no enzymatic substrate specificity (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2, edosa2020tmspz4playsan pages 1-3). Instead, Spaetzle functions as a **secreted, cytokine-like signaling ligand** that activates Toll receptors through direct protein-protein binding interactions (saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32, kato2023analysisofthe pages 1-2).

### Molecular Structure and Domains

Spaetzle is synthesized as an inactive precursor protein (pro-Spaetzle) with a characteristic domain architecture (saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32):

1. **N-terminal signal peptide**: Directs the nascent protein into the secretory pathway for extracellular release
2. **Regulatory prodomain** (~25 kDa): Masks receptor-binding determinants and maintains the protein in an inactive state
3. **C-terminal signaling domain (C-106)**: An approximately 106-amino acid, ~12 kDa domain containing the active receptor-binding region

The C-106 domain adopts a **cystine-knot fold**, a compact three-dimensional structure stabilized by disulfide bonds between conserved cysteine residues (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32). This structural motif is related to vertebrate neurotrophin growth factors such as nerve growth factor and is characteristic of cytokine-like signaling molecules (saucereau2021structureanddynamics pages 1-3, gangloff2021structureanddynamics pages 5-7). The mature, active form exists as a **disulfide-linked homodimer** with both intra- and interchain disulfide bonds stabilizing the structure (gangloff2021structureanddynamics pages 5-7, dine2022functionalcharacterizationof pages 26-32, miao2024identificationofimmunityrelated pages 8-9).

## Activation Mechanism and Processing

Spaetzle activation is a tightly regulated proteolytic process. The inactive pro-Spaetzle precursor must undergo extracellular cleavage to generate the active C-terminal ligand (nakano2023damagesensingmediated pages 5-6, dine2022functionalcharacterizationof pages 26-32, shan2023anevolutionarilyconserved pages 6-8). Processing occurs at a specific site near the junction between the prodomain and C-106 domain, typically containing an arginine-valine (Arg-Val) sequence (nakano2023damagesensingmediated pages 5-6).

### Context-Specific Processing Enzymes

Different serine proteases activate Spaetzle depending on the biological context (nakano2023damagesensingmediated pages 5-6, dine2022functionalcharacterizationof pages 26-32, shan2023anevolutionarilyconserved pages 6-8):

**During Embryonic Development:**
- **Easter**: The principal terminal protease that cleaves pro-Spaetzle during embryonic dorsoventral patterning (dine2022functionalcharacterizationof pages 26-32, dine2022functionalcharacterizationof pages 68-70)

**During Immune Responses:**
- **Spätzle-processing enzyme (SPE)**: The primary terminal protease activated by pathogen recognition cascades (nakano2023damagesensingmediated pages 5-6, dine2022functionalcharacterizationof pages 26-32, shan2023anevolutionarilyconserved pages 6-8)
- **MP1 (Melanization Protease 1)**: Can cleave pro-Spaetzle and may function redundantly with SPE (nakano2023damagesensingmediated pages 5-6, shan2023anevolutionarilyconserved pages 6-8)
- **Sp7 and Ser7**: Additional serine proteases capable of processing pro-Spaetzle (shan2023anevolutionarilyconserved pages 6-8)

**During Tissue Damage:**
- **Hayan and Persephone (Psh)**: Upstream serine proteases that can activate pro-Spaetzle in response to sterile tissue damage and reactive oxygen species (nakano2023damagesensingmediated pages 5-6, nakano2023damagesensingmediated pages 2-3, nakano2023damagesensingmediated pages 15-16, nakano2023damagesensingmediated pages 6-9)

Recent biochemical reconstitution studies from 2023 demonstrated that multiple proteases can act in an integrated network to generate active Spaetzle, with Grass, Psh, Hayan, and other components forming cascade pathways that respond to different microbial patterns and virulence factors (shan2023anevolutionarilyconserved pages 6-8).

## Receptor Binding and Toll Activation

The mature, cleaved Spaetzle C-106 domain binds to the extracellular portion of Toll receptors, specifically engaging the concave leucine-rich repeat (LRR) surface of the Toll ectodomain (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2, saucereau2021structureanddynamics pages 3-5). 

### Binding Mechanism

Structural studies from 2021-2022 using cryo-electron microscopy have revealed the molecular details of Spaetzle-Toll interactions (saucereau2021structureanddynamics pages 1-3, gangloff2021structureanddynamics pages 1-5, saucereau2022structureanddynamics pages 1-2, saucereau2021structureanddynamics pages 3-5):

- Spaetzle binds as a **covalent homodimer** through asymmetric contacts with the Toll receptor
- The interaction is characterized by **low affinity but high specificity**, with transient but functionally important binding dynamics (saucereau2021structureanddynamics pages 1-3, gangloff2021structureanddynamics pages 1-5)
- Binding involves the first ten leucine-rich repeats of Toll, with specific contacts including hydrogen bonds and salt bridges between conserved residues (saucereau2021structureanddynamics pages 3-5, gangloff2021structureanddynamics pages 5-7, gangloff2021structureanddynamics pages 7-9)
- Only one Spaetzle ligand is clearly resolved in many structural studies, suggesting **asymmetric activation** mechanisms (saucereau2021structureanddynamics pages 1-3, gangloff2021structureanddynamics pages 1-5, saucereau2022structureanddynamics pages 1-2)

### Receptor Reorganization

Spaetzle binding induces critical conformational changes in Toll receptors (saucereau2021structureanddynamics pages 1-3, gangloff2021structureanddynamics pages 1-5, saucereau2022structureanddynamics pages 1-2):

- In the absence of ligand, Toll receptors form **inactive head-to-head homodimers** with widely separated juxtamembrane regions (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2)
- Spaetzle binding breaks this symmetry and **brings receptor C-termini into proximity**, enabling association of intracellular TIR domains (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32)
- This spatial reorganization is the key structural requirement for downstream signal transduction (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2)

## Downstream Signaling Pathway

Activated Toll receptors initiate a conserved intracellular signaling cascade that leads to antimicrobial peptide production and other immune responses (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37, chowdhury2019tollfamilymembers pages 1-2):

| Pathway Component | Type | Function/Role | Location |
|---|---|---|---|
| Pro-Spätzle (Spz; P48607) | Inactive cytokine precursor | Secreted, disulfide-linked precursor containing an inhibitory prodomain and C-terminal cystine-knot signaling domain; it is not an enzyme or direct microbial sensor. (saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32) | Secretory pathway → extracellular space/hemolymph or embryonic perivitelline space |
| Spätzle-processing enzyme (SPE) / Easter | Serine protease | SPE cleaves pro-Spätzle during immune responses; Easter performs the corresponding terminal cleavage during embryonic dorsoventral patterning. Cleavage exposes the active C-terminal C-106 ligand. (nakano2023damagesensingmediated pages 5-6, dine2022functionalcharacterizationof pages 26-32, shan2023anevolutionarilyconserved pages 6-8) | Extracellular protease cascade |
| Mature Spätzle C-106 | Cytokine-like ligand | Disulfide-stabilized cystine-knot dimer that binds the Toll ectodomain and rearranges Toll receptors so their juxtamembrane and intracellular signaling regions approach one another. (saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32) | Extracellular |
| Toll (Toll-1) | Transmembrane receptor | Recognizes processed Spätzle through its extracellular leucine-rich-repeat domain; ligand-induced receptor reorganization activates the intracellular TIR domain. (saucereau2021structureanddynamics pages 3-5, kato2023analysisofthe pages 1-2) | Plasma membrane |
| MyD88 | Adaptor | Associates with the activated Toll TIR domain and nucleates the downstream death-domain signaling complex. (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 26-32) | Cytoplasmic face of plasma membrane |
| Tube | Scaffold/adaptor | Bridges MyD88 to Pelle through death-domain interactions, organizing the receptor-proximal signaling complex. (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37) | Cytoplasmic |
| Pelle | Serine/threonine kinase | Functions in the MyD88–Tube–Pelle complex and promotes phosphorylation and subsequent removal of the NF-κB inhibitor Cactus. (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37) | Cytoplasmic |
| Pellino | Positive signaling regulator | Positively regulates Pelle and supports propagation of Toll signaling. (lima2021evolutionoftoll pages 1-2) | Cytoplasmic |
| Cactus | IκB-like inhibitor | Retains Dorsal and Dif in the cytoplasm under resting conditions; Toll signaling promotes its phosphorylation, ubiquitylation, and proteasomal degradation. (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37) | Cytoplasmic |
| Dorsal | NF-κB-family transcription factor | After Cactus removal, enters nuclei; generates the graded transcriptional response used in embryonic dorsoventral patterning and also contributes to larval immune responses. (rahimi2021thedynamicsand pages 43-46, pechmann2021strikingparallelsbetween pages 16-18, dine2022functionalcharacterizationof pages 32-37) | Cytoplasmic when inhibited → nuclear when activated |
| Dif | NF-κB-family transcription factor | Translocates to nuclei after Cactus degradation and is a principal Toll-pathway transcription factor in adult systemic immunity. (dine2022functionalcharacterizationof pages 32-37, chowdhury2019tollfamilymembers pages 1-2) | Cytoplasmic when inhibited → nuclear when activated |
| Drosomycin | Antimicrobial-peptide target gene/effector | Canonical Toll-responsive antifungal peptide gene induced by Dorsal/Dif-dependent transcription. (lima2021evolutionoftoll pages 1-2, chowdhury2019tollfamilymembers pages 1-2) | Transcribed in nucleus; peptide secreted extracellularly |
| Other Toll-responsive AMP genes | Target genes/effectors | Encode additional antimicrobial effectors; their induction links extracellular Spätzle activation to systemic host defense, although the exact AMP repertoire varies by tissue and context. (kato2023analysisofthe pages 1-2, chowdhury2019tollfamilymembers pages 1-2) | Transcribed in nucleus; peptide products generally secreted extracellularly |


*Table: This table traces canonical signaling from extracellular pro-Spätzle processing through Toll, the MyD88–Tube–Pelle complex, Cactus removal, NF-κB activation, and antimicrobial-peptide expression. It also distinguishes the developmental and immune processing enzymes and locations of each step.*

**Key Signaling Components:**

1. **MyD88** (adaptor): Associates with activated Toll TIR domains and nucleates the signaling complex (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37, dine2022functionalcharacterizationof pages 26-32)
2. **Tube** (scaffold): Bridges MyD88 to Pelle through death domain interactions (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37)
3. **Pelle** (kinase): Serine/threonine kinase that promotes phosphorylation of the NF-κB inhibitor Cactus (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37)
4. **Cactus degradation**: Phosphorylated Cactus undergoes ubiquitylation and proteasomal degradation (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37)
5. **Dorsal and Dif** (transcription factors): NF-κB family members that translocate to the nucleus upon Cactus removal (lima2021evolutionoftoll pages 1-2, dine2022functionalcharacterizationof pages 32-37, chowdhury2019tollfamilymembers pages 1-2, kato2023analysisofthe pages 1-2)

**Transcriptional Targets:**

The pathway culminates in expression of antimicrobial peptide genes, with **drosomycin** being the best-characterized Toll-responsive antifungal peptide (lima2021evolutionoftoll pages 1-2, chowdhury2019tollfamilymembers pages 1-2, kato2023analysisofthe pages 1-2). Additional targets include cecropins and other AMPs, with the specific repertoire varying by tissue and developmental context (kato2023analysisofthe pages 1-2, chowdhury2019tollfamilymembers pages 1-2, saucereau2021structureanddynamics pages 7-9).

## Subcellular and Extracellular Localization

Spaetzle is a **secreted, extracellular protein** that functions outside cells (bae2021tenebriomolitorspätzle pages 5-8, miao2024identificationofimmunityrelated pages 8-9, jang2021tmspzlikeplaysa pages 2-4, edosa2020tmspz6isessential pages 8-11):

- The N-terminal signal peptide directs entry into the secretory pathway (bae2021tenebriomolitorspätzle pages 5-8, jang2021tmspzlikeplaysa pages 2-4)
- In **embryos**, Spaetzle is secreted into the **perivitelline space** between the embryo and vitelline membrane, where it establishes a dorsoventral gradient (rahimi2021thedynamicsand pages 43-46, pechmann2021strikingparallelsbetween pages 16-18, rahimi2021thedynamicsand pages 37-40)
- In **larvae and adults**, Spaetzle functions in the **hemolymph** and extracellular spaces associated with immune tissues (edosa2020tmspz6isessential pages 8-11, edosa2020tmspz6isessential pages 11-13)
- During **cell competition** in imaginal discs, Spaetzle acts locally within the enclosed epithelial lumen (alpar2018spatiallyrestrictedregulation pages 5-6)

### Tissue Expression

Expression patterns vary by developmental stage and context (bae2021tenebriomolitorspätzle pages 5-8, liu2023serpin1aandserpin6 pages 4-5, edosa2020tmspz6isessential pages 8-11, edosa2020tmspz6isessential pages 11-13):

- **Maternal contribution** provides Spaetzle for early embryonic patterning (rahimi2021thedynamicsand pages 43-46, pechmann2021strikingparallelsbetween pages 16-18)
- **Hemocytes** show particularly high expression during immune responses (edosa2020tmspz6isessential pages 8-11, edosa2020tmspz6isessential pages 11-13)
- **Fat body** and **gut** tissues express Spaetzle, especially upon microbial challenge (liu2023serpin1aandserpin6 pages 4-5, edosa2020tmspz6isessential pages 8-11)
- Expression is **induced** by infection, tissue damage, and stress conditions (edosa2020tmspz6isessential pages 8-11, edosa2020tmspz6isessential pages 11-13)

## Biological Processes and Functions

Spaetzle participates in multiple critical biological processes, with two major canonical roles and several emerging non-immune functions.

### 1. Embryonic Dorsoventral Patterning

Spaetzle is essential for establishing the dorsoventral axis of the early *Drosophila* embryo (rahimi2021thedynamicsand pages 43-46, rahimi2021thedynamicsand pages 4-8, pechmann2021strikingparallelsbetween pages 16-18, rahimi2021thedynamicsand pages 37-40, pechmann2021strikingparallelsbetween pages 24-26):

- Pro-Spaetzle is broadly distributed but is **ventrally activated** by Easter protease through a spatially restricted proteolytic cascade (pechmann2021strikingparallelsbetween pages 16-18, pechmann2021strikingparallelsbetween pages 24-26)
- Active Spaetzle forms a **ventral-to-dorsal gradient** in the perivitelline space (rahimi2021thedynamicsand pages 43-46, rahimi2021thedynamicsand pages 4-8, rahimi2021thedynamicsand pages 37-40)
- This gradient is refined by **ligand shuttling mechanisms** involving interactions between the active C-106 domain and its prodomain (rahimi2021thedynamicsand pages 43-46, rahimi2021thedynamicsand pages 4-8)
- Toll activation by the Spaetzle gradient generates **graded nuclear localization of Dorsal transcription factor**, providing positional information (rahimi2021thedynamicsand pages 43-46, rahimi2021thedynamicsand pages 4-8, pechmann2021strikingparallelsbetween pages 16-18, rahimi2021thedynamicsand pages 37-40)
- Differential Dorsal levels specify distinct cell fates along the dorsoventral axis, including mesoderm, neuroectoderm, and dorsal ectoderm (pechmann2021strikingparallelsbetween pages 16-18, pechmann2021strikingparallelsbetween pages 24-26)

### 2. Innate Immune Responses

Spaetzle is the key extracellular signal linking pathogen recognition to antimicrobial defense (dine2022functionalcharacterizationof pages 22-26, miao2024identificationofimmunityrelated pages 13-14, kato2023analysisofthe pages 1-2, dine2022functionalcharacterizationof pages 26-32):

**Pathogen Specificity:**
- The Spaetzle-Toll pathway responds primarily to **Gram-positive bacteria** and **fungi** (dine2022functionalcharacterizationof pages 22-26, kato2023analysisofthe pages 1-2, dine2022functionalcharacterizationof pages 26-32)
- **Lys-type peptidoglycan** from Gram-positive bacteria is recognized by PGRP-SA and GNBP1 (dine2022functionalcharacterizationof pages 22-26, miao2024identificationofimmunityrelated pages 13-14, kato2023analysisofthe pages 1-2)
- **β-1,3-glucans** from fungi are recognized by GNBP3 (dine2022functionalcharacterizationof pages 22-26, kato2023analysisofthe pages 1-2)
- Gram-negative bacteria can also activate the pathway, though typically more weakly than Gram-positive bacteria (miao2024identificationofimmunityrelated pages 13-14, edosa2020tmspz6isessential pages 11-13)

**Immune Cascade:**
1. Pathogen-associated molecular patterns trigger serine protease cascades
2. Terminal proteases (primarily SPE) cleave pro-Spaetzle to generate active ligand (dine2022functionalcharacterizationof pages 22-26, dine2022functionalcharacterizationof pages 26-32)
3. Active Spaetzle binds Toll receptors on hemocytes and fat body cells (dine2022functionalcharacterizationof pages 26-32, edosa2020tmspz6isessential pages 13-14)
4. Downstream signaling induces antimicrobial peptide genes, particularly the antifungal **drosomycin** (dine2022functionalcharacterizationof pages 22-26, dine2022functionalcharacterizationof pages 26-32, nakano2023damagesensingmediated pages 30-31)

### 3. Emerging Non-Immune Roles (Recent Findings 2023-2025)

Recent studies have revealed additional functions beyond classical immunity and development:

**Tissue Damage Sensing and Sterile Inflammation:**
A landmark 2023 study demonstrated that Spaetzle mediates responses to sterile tissue damage and apoptosis deficiency (nakano2023damagesensingmediated pages 2-3, nakano2023damagesensingmediated pages 15-16, nakano2023damagesensingmediated pages 6-9):
- Tissue damage and reactive oxygen species (ROS) activate Hayan and Persephone proteases (nakano2023damagesensingmediated pages 2-3, nakano2023damagesensingmediated pages 6-9)
- These proteases cleave pro-Spaetzle, triggering Toll pathway activation without infection (nakano2023damagesensingmediated pages 2-3, nakano2023damagesensingmediated pages 6-9)
- Genetically engineered uncleavable Spaetzle mutants confirmed that proteolytic activation is required for damage-induced Toll signaling (nakano2023damagesensingmediated pages 2-3, nakano2023damagesensingmediated pages 6-9)
- This damage-sensing mechanism contributes to tissue homeostasis and surveillance (nakano2023damagesensingmediated pages 2-3, nakano2023damagesensingmediated pages 6-9)

**Stress-Induced Neurodegeneration:**
A 2025 preprint reported that chronic stress activates Spaetzle-Toll-1 signaling in neurons, leading to neurodegeneration through glial phagocytosis (osaka2025aninnateimmune pages 13-17):
- Chronic light stress and mitochondrial dysfunction promote Spaetzle processing (osaka2025aninnateimmune pages 13-17)
- Toll-1 activation in stressed neurons induces expression of the glial phagocytic receptor Draper (osaka2025aninnateimmune pages 13-17)
- Excessive glial phagocytosis removes viable neurons, contributing to neurodegeneration (osaka2025aninnateimmune pages 13-17)
- This represents a novel non-cell-autonomous mechanism linking cellular stress to tissue degeneration (osaka2025aninnateimmune pages 13-17)

## Spaetzle Gene Family

*Drosophila melanogaster* possesses **six Spaetzle genes** (Spz1-7, with Spz3/4 sometimes grouped), indicating functional diversification through gene duplication (dine2022functionalcharacterizationof pages 26-32, lima2021evolutionoftoll pages 14-15, lima2021evolutionoftoll pages 5-7):

- **Spz1** (the canonical Spaetzle, P48607): Functions in both immunity and embryonic patterning (dine2022functionalcharacterizationof pages 26-32)
- **Spz2, Spz5**: Can bind multiple Toll receptors (Toll-1, Toll-6, Toll-7) and activate antimicrobial peptide expression (chowdhury2019tollfamilymembers pages 1-2, dine2022functionalcharacterizationof pages 26-32, gangloff2021structureanddynamics pages 9-11)
- **Spz5**: Has documented roles in neurotropism and nervous system development beyond immunity (dine2022functionalcharacterizationof pages 26-32, gangloff2021structureanddynamics pages 9-11)
- **Spz4, Spz6, Spz7**: Less well-characterized paralogs with distinct expression patterns (dine2022functionalcharacterizationof pages 26-32, lima2021evolutionoftoll pages 14-15, lima2021evolutionoftoll pages 5-7)

The paralogs show **receptor promiscuity**, with some ligands capable of activating multiple Toll family members, though the physiological significance of many interactions remains to be fully elucidated (chowdhury2019tollfamilymembers pages 1-2, dine2022functionalcharacterizationof pages 26-32, gangloff2021structureanddynamics pages 9-11).

## Summary of Key Functional Characteristics

| Functional characteristic | Evidence-based annotation for *Drosophila melanogaster* Spätzle (spz; UniProt P48607) |
|---|---|
| Protein type / classification | Secreted, cytokine-like signaling protein and canonical extracellular ligand of Toll-1; it is **not an enzyme** and has no catalytic reaction or substrate specificity. It belongs functionally to the Spätzle family of cystine-knot Toll ligands (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32). |
| Primary molecular function | After proteolytic activation, the mature C-terminal ligand binds the extracellular leucine-rich-repeat region of Toll-1 and induces receptor rearrangement or oligomerization, bringing the receptor’s juxtamembrane and intracellular signaling regions into proximity (saucereau2021structureanddynamics pages 1-3, saucereau2021structureanddynamics pages 3-5, dine2022functionalcharacterizationof pages 26-32). |
| Structural features and domains | Synthesized as a precursor containing an N-terminal signal peptide, an inhibitory/regulatory prodomain, and a C-terminal approximately 106-residue **C-106** signaling domain. C-106 adopts a disulfide-stabilized cystine-knot fold related to neurotrophin folds and forms the active dimeric ligand. These features agree with the Cystine-knot cytokine, Spaetzle, Spz/Toll-ligand-like, and PF16077 annotations supplied for P48607 (saucereau2021structureanddynamics pages 1-3, saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32). |
| Biosynthesis and processing | The signal peptide directs the nascent protein into the secretory pathway. Secreted pro-Spätzle remains inactive because its prodomain masks receptor-binding determinants. Cleavage at the prodomain–C-106 junction generates the mature C-terminal signaling fragment; the prodomain and C-106 can remain associated noncovalently after cleavage (saucereau2022structureanddynamics pages 1-2, dine2022functionalcharacterizationof pages 26-32). |
| Activation mechanism | Context-specific extracellular serine-protease cascades activate pro-Spätzle. Easter is the principal terminal processing protease during embryonic dorsoventral patterning, whereas Spätzle-processing enzyme (SPE) is the principal immune terminal protease. Recent biochemical and genetic studies also support partially redundant processing by MP1, Sp7, Ser7, Grass, Hayan, or Persephone-dependent routes under infection or sterile-damage conditions (nakano2023damagesensingmediated pages 5-6, shan2023anevolutionarilyconserved pages 6-8). |
| Binding partners / receptors | The best-established physiological receptor is Toll-1. Mature C-106, rather than uncleaved pro-Spätzle, binds Toll’s extracellular domain. Cell-based studies also report that Spz can engage Toll-7, but these broader receptor interactions are less firmly established physiologically than the canonical Spz–Toll-1 pair and should not be conflated with activities of paralogs such as Spz5 (dine2022functionalcharacterizationof pages 26-32, chowdhury2019tollfamilymembers pages 1-2). |
| Subcellular localization | A soluble, secreted extracellular ligand—not an integral membrane protein. During embryogenesis, pro-Spätzle and activated Spätzle act in the perivitelline space surrounding the embryo. During systemic immunity, processing and receptor engagement occur in extracellular compartments associated with the hemolymph and immune-responsive tissues; local extracellular activation also occurs in the wing-disc lumen during cell competition (pechmann2021strikingparallelsbetween pages 16-18, rahimi2021thedynamicsand pages 37-40, alpar2018spatiallyrestrictedregulation pages 5-6). |
| Expression pattern | Maternal Spätzle supplies the early embryo, where spatially restricted **activation**, rather than simply localized synthesis, generates the dorsoventral signal. In postembryonic contexts, spz is expressed in immune and epithelial tissues and can participate in systemic or locally restricted Toll signaling. Tissue-expression claims from other insects cannot be transferred directly to *D. melanogaster* (rahimi2021thedynamicsand pages 43-46, pechmann2021strikingparallelsbetween pages 16-18, alpar2018spatiallyrestrictedregulation pages 5-6). |
| Key biological processes | **Embryonic patterning:** ventrally restricted cleavage generates an active-Spätzle gradient that activates Toll and establishes graded nuclear Dorsal, specifying dorsoventral cell fates. **Innate immunity:** pathogen-recognition and virulence-sensing protease cascades activate Spätzle, leading through Toll–MyD88–Tube–Pelle to Cactus removal, nuclear Dorsal/Dif, and antimicrobial genes such as *drosomycin*. **Sterile tissue surveillance:** cleavage-dependent Spätzle signaling responds to injury, ROS, apoptosis deficiency, and cell competition (dine2022functionalcharacterizationof pages 22-26, rahimi2021thedynamicsand pages 43-46, lima2021evolutionoftoll pages 1-2, nakano2023damagesensingmediated pages 2-3, nakano2023damagesensingmediated pages 6-9). |


*Table: This table consolidates the molecular identity, structure, activation, localization, receptor interactions, and principal biological functions of Drosophila Spätzle (P48607). It distinguishes evidence specific to canonical spz from findings involving other Spätzle paralogs or insect species.*

## Conclusions

Spaetzle (spz, UniProt P48607) is a secreted, cytokine-like signaling protein—not an enzyme—that serves as the canonical activating ligand for Toll receptors in *Drosophila melanogaster*. Its primary molecular function is to bind Toll receptor ectodomains and induce conformational changes that enable downstream signaling. The protein is synthesized as an inactive precursor with an N-terminal signal peptide, regulatory prodomain, and C-terminal C-106 cystine-knot signaling domain. Context-specific serine protease cascades activate pro-Spaetzle by proteolytic cleavage, generating a mature disulfide-linked homodimer.

Functionally, Spaetzle operates in two major canonical contexts: (1) establishing the embryonic dorsoventral axis through spatially restricted activation and gradient formation, and (2) mediating innate immune responses to Gram-positive bacteria and fungi through activation of antimicrobial peptide transcription. The pathway proceeds through Toll→MyD88→Tube→Pelle→Cactus degradation→Dorsal/Dif nuclear translocation→antimicrobial gene expression.

Recent research (2023-2025) has expanded understanding of Spaetzle beyond immunity and development, revealing roles in tissue damage sensing, sterile inflammation, stress responses, and neurodegeneration. These findings establish Spaetzle as a versatile signaling molecule that integrates diverse inputs—pathogen recognition, tissue damage, oxidative stress—to coordinate cellular and organismal responses. The existence of six Spaetzle paralogues further suggests functional specialization, though the full scope of their distinct biological roles remains an active area of investigation.

References

1. (dine2022functionalcharacterizationof pages 26-32): H Zein El Dine. Functional characterization of anopheles gambiae spätzle gene family. Unknown journal, 2022.

2. (saucereau2021structureanddynamics pages 1-3): Yoann Saucereau, Tom H. Wilson, Matthew C. K. Tang, Martin C. Moncrieffe, Steven W. Hardwick, Dimitri Y. Chirgadze, Sandro G. Soares, Maria Jose Marcaida, Nick Gay, and Monique Gangloff. Structure and dynamics of toll immunoreceptor activation in the mosquito aedes aegypti. BioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.06.459066, doi:10.1101/2021.09.06.459066. This article has 0 citations.

3. (saucereau2022structureanddynamics pages 1-2): Yoann Saucereau, Tom H. Wilson, Matthew C. K. Tang, Martin C. Moncrieffe, Steven W. Hardwick, Dimitri Y. Chirgadze, Sandro G. Soares, Maria Jose Marcaida, Nick Gay, and Monique Gangloff. Structure and dynamics of toll immunoreceptor activation in the mosquito aedes aegypti. Nature Communications, Sep 2022. URL: https://doi.org/10.1038/s41467-022-32690-6, doi:10.1038/s41467-022-32690-6. This article has 23 citations and is from a highest quality peer-reviewed journal.

4. (edosa2020tmspz4playsan pages 1-3): Tariku Tesfaye Edosa, Yong Hun Jo, Maryam Keshavarz, Young Min Bae, Dong Hyun Kim, Yong Seok Lee, and Yeon Soo Han. Tmspz4 plays an important role in regulating the production of antimicrobial peptides in response to escherichia coli and candida albicans infections. International Journal of Molecular Sciences, 21:1878, Mar 2020. URL: https://doi.org/10.3390/ijms21051878, doi:10.3390/ijms21051878. This article has 30 citations.

5. (kato2023analysisofthe pages 1-2): Daiki Kato, Ken Miura, and Kakeru Yokoi. Analysis of the toll and spaetzle genes involved in toll pathway-dependent antimicrobial gene induction in the red flour beetle, tribolium castaneum (coleoptera; tenebrionidae). International Journal of Molecular Sciences, 24:1523, Jan 2023. URL: https://doi.org/10.3390/ijms24021523, doi:10.3390/ijms24021523. This article has 15 citations.

6. (gangloff2021structureanddynamics pages 5-7): Monique Gangloff, Yoann Saucereau, Thomas Wilson, Matthew Tang, Martin Moncrieffe, Steven Hardwick, Dimitri Chirgadze, Sandro Soares, Maria Marcaida, and Nicholas J. Gay. Structure and dynamics of pathway activation by the toll immunoreceptor from the viral mosquito vector aedes aegypti. ArXiv, Dec 2021. URL: https://doi.org/10.21203/rs.3.rs-1082903/v1, doi:10.21203/rs.3.rs-1082903/v1. This article has 0 citations.

7. (miao2024identificationofimmunityrelated pages 8-9): Zelong Miao, Chao Xiong, Yang Wang, Tisheng Shan, and Haobo Jiang. Identification of immunity-related genes distinctly regulated by manduca sexta spӓtzle-1/2 and escherichia coli peptidoglycan. Insect Biochemistry and Molecular Biology, 168:104108, May 2024. URL: https://doi.org/10.1016/j.ibmb.2024.104108, doi:10.1016/j.ibmb.2024.104108. This article has 6 citations and is from a peer-reviewed journal.

8. (nakano2023damagesensingmediated pages 5-6): Shotaro Nakano, Soshiro Kashio, Kei Nishimura, Asuka Takeishi, Hina Kosakamoto, Fumiaki Obata, Erina Kuranaga, Takahiro Chihara, Yoshio Yamauchi, Toshiaki Isobe, and Masayuki Miura. Damage sensing mediated by serine proteases hayan and persephone for toll pathway activation in apoptosis-deficient flies. PLOS Genetics, 19:e1010761, Jun 2023. URL: https://doi.org/10.1371/journal.pgen.1010761, doi:10.1371/journal.pgen.1010761. This article has 10 citations and is from a domain leading peer-reviewed journal.

9. (shan2023anevolutionarilyconserved pages 6-8): Tisheng Shan, Yang Wang, Krishna Bhattarai, and Haobo Jiang. An evolutionarily conserved serine protease network mediates melanization and toll activation in <i>drosophila</i>. Science Advances, Dec 2023. URL: https://doi.org/10.1126/sciadv.adk2756, doi:10.1126/sciadv.adk2756. This article has 64 citations and is from a highest quality peer-reviewed journal.

10. (dine2022functionalcharacterizationof pages 68-70): H Zein El Dine. Functional characterization of anopheles gambiae spätzle gene family. Unknown journal, 2022.

11. (nakano2023damagesensingmediated pages 2-3): Shotaro Nakano, Soshiro Kashio, Kei Nishimura, Asuka Takeishi, Hina Kosakamoto, Fumiaki Obata, Erina Kuranaga, Takahiro Chihara, Yoshio Yamauchi, Toshiaki Isobe, and Masayuki Miura. Damage sensing mediated by serine proteases hayan and persephone for toll pathway activation in apoptosis-deficient flies. PLOS Genetics, 19:e1010761, Jun 2023. URL: https://doi.org/10.1371/journal.pgen.1010761, doi:10.1371/journal.pgen.1010761. This article has 10 citations and is from a domain leading peer-reviewed journal.

12. (nakano2023damagesensingmediated pages 15-16): Shotaro Nakano, Soshiro Kashio, Kei Nishimura, Asuka Takeishi, Hina Kosakamoto, Fumiaki Obata, Erina Kuranaga, Takahiro Chihara, Yoshio Yamauchi, Toshiaki Isobe, and Masayuki Miura. Damage sensing mediated by serine proteases hayan and persephone for toll pathway activation in apoptosis-deficient flies. PLOS Genetics, 19:e1010761, Jun 2023. URL: https://doi.org/10.1371/journal.pgen.1010761, doi:10.1371/journal.pgen.1010761. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (nakano2023damagesensingmediated pages 6-9): Shotaro Nakano, Soshiro Kashio, Kei Nishimura, Asuka Takeishi, Hina Kosakamoto, Fumiaki Obata, Erina Kuranaga, Takahiro Chihara, Yoshio Yamauchi, Toshiaki Isobe, and Masayuki Miura. Damage sensing mediated by serine proteases hayan and persephone for toll pathway activation in apoptosis-deficient flies. PLOS Genetics, 19:e1010761, Jun 2023. URL: https://doi.org/10.1371/journal.pgen.1010761, doi:10.1371/journal.pgen.1010761. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (saucereau2021structureanddynamics pages 3-5): Yoann Saucereau, Tom H. Wilson, Matthew C. K. Tang, Martin C. Moncrieffe, Steven W. Hardwick, Dimitri Y. Chirgadze, Sandro G. Soares, Maria Jose Marcaida, Nick Gay, and Monique Gangloff. Structure and dynamics of toll immunoreceptor activation in the mosquito aedes aegypti. BioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.06.459066, doi:10.1101/2021.09.06.459066. This article has 0 citations.

15. (gangloff2021structureanddynamics pages 1-5): Monique Gangloff, Yoann Saucereau, Thomas Wilson, Matthew Tang, Martin Moncrieffe, Steven Hardwick, Dimitri Chirgadze, Sandro Soares, Maria Marcaida, and Nicholas J. Gay. Structure and dynamics of pathway activation by the toll immunoreceptor from the viral mosquito vector aedes aegypti. ArXiv, Dec 2021. URL: https://doi.org/10.21203/rs.3.rs-1082903/v1, doi:10.21203/rs.3.rs-1082903/v1. This article has 0 citations.

16. (gangloff2021structureanddynamics pages 7-9): Monique Gangloff, Yoann Saucereau, Thomas Wilson, Matthew Tang, Martin Moncrieffe, Steven Hardwick, Dimitri Chirgadze, Sandro Soares, Maria Marcaida, and Nicholas J. Gay. Structure and dynamics of pathway activation by the toll immunoreceptor from the viral mosquito vector aedes aegypti. ArXiv, Dec 2021. URL: https://doi.org/10.21203/rs.3.rs-1082903/v1, doi:10.21203/rs.3.rs-1082903/v1. This article has 0 citations.

17. (lima2021evolutionoftoll pages 1-2): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

18. (dine2022functionalcharacterizationof pages 32-37): H Zein El Dine. Functional characterization of anopheles gambiae spätzle gene family. Unknown journal, 2022.

19. (chowdhury2019tollfamilymembers pages 1-2): Munmun Chowdhury, Chun-Feng Li, Chun-Feng Li, Zhen He, Zhen He, Yuzhen Lu, Xu-Sheng Liu, Yufeng Wang, Y. Ip, M. Strand, Xiao-Qiang Yu, Xiao-Qiang Yu, and Xiao-Qiang Yu. Toll family members bind multiple spätzle proteins and activate antimicrobial peptide gene expression in drosophila. Journal of Biological Chemistry, 294:10172-10181, Jun 2019. URL: https://doi.org/10.1074/jbc.ra118.006804, doi:10.1074/jbc.ra118.006804. This article has 110 citations and is from a domain leading peer-reviewed journal.

20. (rahimi2021thedynamicsand pages 43-46): Neta Rahimi. The dynamics and precision of the spz/toll pathway in the drosophila embryo. Text, Jan 2021. URL: https://doi.org/10.34933/wis.000501, doi:10.34933/wis.000501. This article has 0 citations and is from a peer-reviewed journal.

21. (pechmann2021strikingparallelsbetween pages 16-18): Matthias Pechmann, Nathan James Kenny, Laura Pott, Peter Heger, Yen-Ta Chen, Thomas Buchta, Orhan Özüak, Jeremy Lynch, and Siegfried Roth. Striking parallels between dorsoventral patterning in drosophila and gryllus reveal a complex evolutionary history behind a model gene regulatory network. eLife, Mar 2021. URL: https://doi.org/10.7554/elife.68287, doi:10.7554/elife.68287. This article has 42 citations and is from a domain leading peer-reviewed journal.

22. (saucereau2021structureanddynamics pages 7-9): Yoann Saucereau, Tom H. Wilson, Matthew C. K. Tang, Martin C. Moncrieffe, Steven W. Hardwick, Dimitri Y. Chirgadze, Sandro G. Soares, Maria Jose Marcaida, Nick Gay, and Monique Gangloff. Structure and dynamics of toll immunoreceptor activation in the mosquito aedes aegypti. BioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.06.459066, doi:10.1101/2021.09.06.459066. This article has 0 citations.

23. (bae2021tenebriomolitorspätzle pages 5-8): Young Min Bae, Yong Hun Jo, Bharat Bhusan Patnaik, Bo Bae Kim, Ki Beom Park, Tariku Tesfaye Edosa, Maryam Keshavarz, Maryam Ali Mohammadie Kojour, Yong Seok Lee, and Yeon Soo Han. Tenebrio molitor spätzle 1b is required to confer antibacterial defense against gram-negative bacteria by regulation of antimicrobial peptides. Frontiers in Physiology, Nov 2021. URL: https://doi.org/10.3389/fphys.2021.758859, doi:10.3389/fphys.2021.758859. This article has 17 citations.

24. (jang2021tmspzlikeplaysa pages 2-4): H. Jang, B. Patnaik, Maryam Ali Mohammadie Kojour, Bo Bae Kim, Y. Bae, K. Park, Y. S. Lee, Hun-Jo Yong, and Ye-On-Soo Han. Tmspz-like plays a fundamental role in response to e. coli but not s. aureus or c. albican infection in tenebrio molitor via regulation of antimicrobial peptide production. International Journal of Molecular Sciences, 22:10888, Oct 2021. URL: https://doi.org/10.3390/ijms221910888, doi:10.3390/ijms221910888. This article has 25 citations.

25. (edosa2020tmspz6isessential pages 8-11): Tariku Tesfaye Edosa, Yong Hun Jo, Maryam Keshavarz, Young Min Bae, Dong Hyun Kim, Yong Seok Lee, and Yeon Soo Han. Tmspz6 is essential for regulating the immune response to escherichia coli and staphylococcus aureus infection in tenebrio molitor. Insects, 11:105, Feb 2020. URL: https://doi.org/10.3390/insects11020105, doi:10.3390/insects11020105. This article has 40 citations.

26. (rahimi2021thedynamicsand pages 37-40): Neta Rahimi. The dynamics and precision of the spz/toll pathway in the drosophila embryo. Text, Jan 2021. URL: https://doi.org/10.34933/wis.000501, doi:10.34933/wis.000501. This article has 0 citations and is from a peer-reviewed journal.

27. (edosa2020tmspz6isessential pages 11-13): Tariku Tesfaye Edosa, Yong Hun Jo, Maryam Keshavarz, Young Min Bae, Dong Hyun Kim, Yong Seok Lee, and Yeon Soo Han. Tmspz6 is essential for regulating the immune response to escherichia coli and staphylococcus aureus infection in tenebrio molitor. Insects, 11:105, Feb 2020. URL: https://doi.org/10.3390/insects11020105, doi:10.3390/insects11020105. This article has 40 citations.

28. (alpar2018spatiallyrestrictedregulation pages 5-6): Lale Alpar, Cora Bergantiños, and Laura A. Johnston. Spatially restricted regulation of spätzle/toll signaling during cell competition. Developmental cell, 46 6:706-719.e5, Sep 2018. URL: https://doi.org/10.1016/j.devcel.2018.08.001, doi:10.1016/j.devcel.2018.08.001. This article has 107 citations and is from a highest quality peer-reviewed journal.

29. (liu2023serpin1aandserpin6 pages 4-5): Huawei Liu, Jiahui Xu, Luoling Wang, Pengchao Guo, Zhangchen Tang, Xiaotong Sun, Xin Tang, Wei Wang, Lingyan Wang, Yang Cao, Qingyou Xia, and Ping Zhao. Serpin-1a and serpin-6 regulate the toll pathway immune homeostasis by synergistically inhibiting the spätzle-processing enzyme clip2 in silkworm, bombyx mori. PLOS Pathogens, 19:e1011740, Oct 2023. URL: https://doi.org/10.1371/journal.ppat.1011740, doi:10.1371/journal.ppat.1011740. This article has 32 citations and is from a highest quality peer-reviewed journal.

30. (rahimi2021thedynamicsand pages 4-8): Neta Rahimi. The dynamics and precision of the spz/toll pathway in the drosophila embryo. Text, Jan 2021. URL: https://doi.org/10.34933/wis.000501, doi:10.34933/wis.000501. This article has 0 citations and is from a peer-reviewed journal.

31. (pechmann2021strikingparallelsbetween pages 24-26): Matthias Pechmann, Nathan James Kenny, Laura Pott, Peter Heger, Yen-Ta Chen, Thomas Buchta, Orhan Özüak, Jeremy Lynch, and Siegfried Roth. Striking parallels between dorsoventral patterning in drosophila and gryllus reveal a complex evolutionary history behind a model gene regulatory network. eLife, Mar 2021. URL: https://doi.org/10.7554/elife.68287, doi:10.7554/elife.68287. This article has 42 citations and is from a domain leading peer-reviewed journal.

32. (dine2022functionalcharacterizationof pages 22-26): H Zein El Dine. Functional characterization of anopheles gambiae spätzle gene family. Unknown journal, 2022.

33. (miao2024identificationofimmunityrelated pages 13-14): Zelong Miao, Chao Xiong, Yang Wang, Tisheng Shan, and Haobo Jiang. Identification of immunity-related genes distinctly regulated by manduca sexta spӓtzle-1/2 and escherichia coli peptidoglycan. Insect Biochemistry and Molecular Biology, 168:104108, May 2024. URL: https://doi.org/10.1016/j.ibmb.2024.104108, doi:10.1016/j.ibmb.2024.104108. This article has 6 citations and is from a peer-reviewed journal.

34. (edosa2020tmspz6isessential pages 13-14): Tariku Tesfaye Edosa, Yong Hun Jo, Maryam Keshavarz, Young Min Bae, Dong Hyun Kim, Yong Seok Lee, and Yeon Soo Han. Tmspz6 is essential for regulating the immune response to escherichia coli and staphylococcus aureus infection in tenebrio molitor. Insects, 11:105, Feb 2020. URL: https://doi.org/10.3390/insects11020105, doi:10.3390/insects11020105. This article has 40 citations.

35. (nakano2023damagesensingmediated pages 30-31): Shotaro Nakano, Soshiro Kashio, Kei Nishimura, Asuka Takeishi, Hina Kosakamoto, Fumiaki Obata, Erina Kuranaga, Takahiro Chihara, Yoshio Yamauchi, Toshiaki Isobe, and Masayuki Miura. Damage sensing mediated by serine proteases hayan and persephone for toll pathway activation in apoptosis-deficient flies. PLOS Genetics, 19:e1010761, Jun 2023. URL: https://doi.org/10.1371/journal.pgen.1010761, doi:10.1371/journal.pgen.1010761. This article has 10 citations and is from a domain leading peer-reviewed journal.

36. (osaka2025aninnateimmune pages 13-17): Jiro Osaka, Toshiharu Ichinose, Mai Kanno, Satoko Hakeda-Suzuki, Takashi Suzuki, and Atsushi Sugie. An innate immune receptor toll-1 converts chronic light stress into glial-phagocytosis. bioRxiv, May 2026. URL: https://doi.org/10.1101/2025.09.03.673940, doi:10.1101/2025.09.03.673940. This article has 1 citations.

37. (lima2021evolutionoftoll pages 14-15): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

38. (lima2021evolutionoftoll pages 5-7): Letícia Ferreira Lima, André Quintanilha Torres, Rodrigo Jardim, Rafael Dias Mesquita, and Renata Schama. Evolution of toll, spatzle and myd88 in insects: the problem of the diptera bias. BMC Genomics, Jul 2021. URL: https://doi.org/10.1186/s12864-021-07886-7, doi:10.1186/s12864-021-07886-7. This article has 39 citations and is from a peer-reviewed journal.

39. (gangloff2021structureanddynamics pages 9-11): Monique Gangloff, Yoann Saucereau, Thomas Wilson, Matthew Tang, Martin Moncrieffe, Steven Hardwick, Dimitri Chirgadze, Sandro Soares, Maria Marcaida, and Nicholas J. Gay. Structure and dynamics of pathway activation by the toll immunoreceptor from the viral mosquito vector aedes aegypti. ArXiv, Dec 2021. URL: https://doi.org/10.21203/rs.3.rs-1082903/v1, doi:10.21203/rs.3.rs-1082903/v1. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](spz-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](spz-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. dine2022functionalcharacterizationof pages 26-32
2. nakano2023damagesensingmediated pages 5-6
3. shan2023anevolutionarilyconserved pages 6-8
4. lima2021evolutionoftoll pages 1-2
5. alpar2018spatiallyrestrictedregulation pages 5-6
6. osaka2025aninnateimmune pages 13-17
7. saucereau2021structureanddynamics pages 1-3
8. saucereau2022structureanddynamics pages 1-2
9. kato2023analysisofthe pages 1-2
10. gangloff2021structureanddynamics pages 5-7
11. miao2024identificationofimmunityrelated pages 8-9
12. dine2022functionalcharacterizationof pages 68-70
13. nakano2023damagesensingmediated pages 2-3
14. nakano2023damagesensingmediated pages 15-16
15. nakano2023damagesensingmediated pages 6-9
16. saucereau2021structureanddynamics pages 3-5
17. gangloff2021structureanddynamics pages 1-5
18. gangloff2021structureanddynamics pages 7-9
19. dine2022functionalcharacterizationof pages 32-37
20. chowdhury2019tollfamilymembers pages 1-2
21. rahimi2021thedynamicsand pages 43-46
22. pechmann2021strikingparallelsbetween pages 16-18
23. saucereau2021structureanddynamics pages 7-9
24. jang2021tmspzlikeplaysa pages 2-4
25. rahimi2021thedynamicsand pages 37-40
26. rahimi2021thedynamicsand pages 4-8
27. pechmann2021strikingparallelsbetween pages 24-26
28. dine2022functionalcharacterizationof pages 22-26
29. miao2024identificationofimmunityrelated pages 13-14
30. nakano2023damagesensingmediated pages 30-31
31. lima2021evolutionoftoll pages 14-15
32. lima2021evolutionoftoll pages 5-7
33. gangloff2021structureanddynamics pages 9-11
34. https://doi.org/10.1101/2021.09.06.459066,
35. https://doi.org/10.1038/s41467-022-32690-6,
36. https://doi.org/10.3390/ijms21051878,
37. https://doi.org/10.3390/ijms24021523,
38. https://doi.org/10.21203/rs.3.rs-1082903/v1,
39. https://doi.org/10.1016/j.ibmb.2024.104108,
40. https://doi.org/10.1371/journal.pgen.1010761,
41. https://doi.org/10.1126/sciadv.adk2756,
42. https://doi.org/10.1186/s12864-021-07886-7,
43. https://doi.org/10.1074/jbc.ra118.006804,
44. https://doi.org/10.34933/wis.000501,
45. https://doi.org/10.7554/elife.68287,
46. https://doi.org/10.3389/fphys.2021.758859,
47. https://doi.org/10.3390/ijms221910888,
48. https://doi.org/10.3390/insects11020105,
49. https://doi.org/10.1016/j.devcel.2018.08.001,
50. https://doi.org/10.1371/journal.ppat.1011740,
51. https://doi.org/10.1101/2025.09.03.673940,