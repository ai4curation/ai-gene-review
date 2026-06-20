---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-03T08:21:51.749386'
end_time: '2026-06-03T08:31:31.801894'
duration_seconds: 580.05
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: METEA
  gene_id: mllDE
  gene_symbol: mllDE
  uniprot_accession: C5B1I6
  protein_description: 'RecName: Full=Carrier domain-containing protein {ECO:0000259|PROSITE:PS50075};'
  gene_info: OrderedLocusNames=MexAM1_META1p4134 {ECO:0000313|EMBL:ACS41787.1};
  organism_full: Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805
    / NCIMB 9133 / AM1) (Methylobacterium extorquens).
  protein_family: Not specified in UniProt
  protein_domains: ACP-like_sf. (IPR036736); DUF6005. (IPR046047); PP-bd_ACP. (IPR009081);
    DUF6005 (PF19468); PP-binding (PF00550)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: mllDE-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: mllDE-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: "## Context ID: pqac-00000009 Figure 2a shows the methylolanthanin\
    \ (mll) biosynthetic gene cluster (META1p4129\u2013META1p4138) from Methylobacterium\
    \ extorquens AM1. "
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** C5B1I6
- **Protein Description:** RecName: Full=Carrier domain-containing protein {ECO:0000259|PROSITE:PS50075};
- **Gene Information:** OrderedLocusNames=MexAM1_META1p4134 {ECO:0000313|EMBL:ACS41787.1};
- **Organism (full):** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACP-like_sf. (IPR036736); DUF6005. (IPR046047); PP-bd_ACP. (IPR009081); DUF6005 (PF19468); PP-binding (PF00550)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mllDE" matches the protein description above**
2. **Verify the organism is correct:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mllDE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mllDE** (gene ID: mllDE, UniProt: C5B1I6) in METEA.

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
- **UniProt Accession:** C5B1I6
- **Protein Description:** RecName: Full=Carrier domain-containing protein {ECO:0000259|PROSITE:PS50075};
- **Gene Information:** OrderedLocusNames=MexAM1_META1p4134 {ECO:0000313|EMBL:ACS41787.1};
- **Organism (full):** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACP-like_sf. (IPR036736); DUF6005. (IPR046047); PP-bd_ACP. (IPR009081); DUF6005 (PF19468); PP-binding (PF00550)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mllDE" matches the protein description above**
2. **Verify the organism is correct:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mllDE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mllDE** (gene ID: mllDE, UniProt: C5B1I6) in METEA.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: **mllDE** (META1p4134; user-specified UniProt **C5B1I6**) in *Methylorubrum extorquens* AM1

## 0) Scope, identity verification, and evidence limitations
The gene symbol **mllDE** is verified in *Methylorubrum extorquens* AM1 (also referred to as *Methylobacterium extorquens* AM1 in the cited work) as a component of the **methylolanthanin (mll) biosynthetic gene cluster** spanning **META1p4129–META1p4138**, where **mllDE corresponds to META1p4134** in the cluster map and gene list. (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization media a750a99c)

The user-provided UniProt accession (**C5B1I6**) and domain annotations (ACP-like/PP-binding/DUF6005) could **not** be independently retrieved/validated with the available literature-retrieval tools in this run; therefore, this report treats those UniProt/domain details as **user-supplied context** and grounds functional statements primarily in **peer-reviewed/primary literature** and the **cluster-level inference rules** explicitly described therein. (zytnick2022discoveryandcharacterization pages 10-12)

## 1) Key concepts and definitions (current understanding as used in the mll literature)

### 1.1 Lanthanides, lanthanide-dependent methylotrophy, and the “Ln-switch”
Work on methylotrophs including *Methylorubrum* spp. describes an integrated lanthanide utilization framework in which lanthanide availability is linked to changes in expression of lanthanide-dependent enzymes and transport systems (often discussed as an “Ln3+ switch”), alongside uptake components such as TonB-dependent transporters and intracellular lanthanide-handling proteins (e.g., LanM/Lut-cluster context). (valdes2024anovelinsilico pages 1-2)

### 1.2 Metallophores and lanthanophores
Zytnick et al. report **methylolanthanin (MLL)** as a secreted small molecule that forms complexes with lanthanides and is required for normal lanthanide accumulation in *M. extorquens* AM1 under some conditions, positioning MLL as a **lanthanide-specific metallophore (“lanthanophore”)**. (zytnick2022discoveryandcharacterization pages 8-10)

### 1.3 Biosynthetic gene clusters (BGCs) and NRPS-independent siderophore-like pathways
The **mll** locus is described as a discrete genomic region (META1p4129–META1p4138) whose gene content includes transport-associated genes and a core biosynthetic module (**mllA/mllBC/mllDE/mllF**), and is reported as homologous in part to the **petrobactin biosynthetic asbABCDEF** locus (an NRPS-independent siderophore pathway). (zytnick2022discoveryandcharacterization pages 3-5)

## 2) Gene/protein context: where mllDE sits and what it most likely does

### 2.1 Genomic neighborhood and pathway placement
mllDE (META1p4134) lies within the **core biosynthetic region** of the mll BGC. The cluster schematic (Figure 2a) places mllDE adjacent to other biosynthetic genes (including mllA and mllBC) and upstream/downstream of additional cluster genes. (zytnick2022discoveryandcharacterization media a750a99c)

Transcriptomics indicates this locus is environmentally responsive to lanthanide bioavailability: in an RNA-seq comparison of growth with poorly soluble **Nd2O3** versus soluble **NdCl3**, the mll locus (META1p4129–META1p4138) shows **~32-fold average upregulation** and is among the most strongly induced regions. (zytnick2022discoveryandcharacterization pages 3-5)

### 2.2 Proposed molecular role of mllDE (inference strength: indirect)
No retrieved source provides a **gene-by-gene biochemical reaction** for **mllDE alone** (e.g., no purified mllDE enzyme assay, no single-gene knockout/complementation resolving mllDE’s specific catalytic step). Instead, mllDE is implicated through:

* **Cluster membership** in a pathway proven to synthesize methylolanthanin. (zytnick2022discoveryandcharacterization pages 5-8)
* **Homology-based inference**: mllA/mllBC/mllDE/mllF are described as homologous to petrobactin **asb** genes, supporting assignment of mllDE to an **NRPS-independent siderophore-like biosynthetic module** that has been repurposed for lanthanide chelation. (zytnick2022discoveryandcharacterization pages 3-5)
* **Bioinformatic signature rules** used to detect related loci: Zytnick et al. describe antiSMASH-style detection criteria involving **PP-binding** and **DUF6005 (PF19468)** signatures in petrobactin-like models. These rules support that **PP-binding/DUF6005-type functions exist within the mll-like biosynthetic architecture**, but they do **not** uniquely attribute those motifs to mllDE in the evidence excerpts available here. (zytnick2022discoveryandcharacterization pages 10-12)

Interpretation: based on the literature available in this run, the most defensible functional statement is that **mllDE encodes a component of the methylolanthanin biosynthetic machinery**, likely contributing to assembly/modification steps required to produce the final lanthanophore. (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 5-8)

## 3) Experimental evidence linking the mll cluster (and thus mllDE as a member gene) to function

### 3.1 Methylolanthanin is the product of the mll BGC
Zytnick et al. show that a molecular family detected in culture supernatants is present in a background strain but absent in a **ΔmxaFΔmll** mutant, and they purify/solve the structure of the product they name **methylolanthanin (MLL)**, demonstrating that the mll locus is necessary for production of this metabolite under their tested conditions. (zytnick2022discoveryandcharacterization pages 5-8)

### 3.2 Lanthanide binding and physiological role
Methylolanthanin forms lanthanide complexes observable by mass spectrometry (reported as complexes of the form **[MLL−H+ + Ln3+]2+** with La, Nd, and Lu). (zytnick2022discoveryandcharacterization pages 8-10)

Manipulating the mll locus changes lanthanide bioaccumulation:
* **Deletion** of mll reduces Nd accumulation (including a reported **~1.8-fold decrease** under NdCl3 in one assay) and a **~30% decrease** in lanthanide bioaccumulation in another comparison; (zytnick2022discoveryandcharacterization pages 10-12, zytnick2022discoveryandcharacterization pages 8-10)
* **Overexpression** of mll increases Nd accumulation by **~3.5-fold**; (zytnick2022discoveryandcharacterization pages 8-10)
* Exogenous addition of purified MLL (**50 nM**) increases maximal growth yield (OD) under **2 µM NdCl3** in tested strains. (zytnick2022discoveryandcharacterization pages 8-10)

Because **mllDE** is part of the deleted/overexpressed genomic region and core biosynthetic operon (Figure 2a), these phenotypes provide **pathway-level functional evidence** that indirectly supports mllDE’s participation in lanthanophore biosynthesis and lanthanide acquisition physiology. (zytnick2022discoveryandcharacterization pages 5-8, zytnick2022discoveryandcharacterization media a750a99c)

### 3.3 Regulatory/physiological context and quantitative expression changes
In addition to strong induction of the mll locus, Zytnick et al. report differential regulation of other lanthanide-responsive genes (e.g., upregulation magnitudes reported for **xoxF1 (~5-fold)**, **exaF (~3-fold)**, **pqqA2/3 (~4-fold)**, and **lutH (~9-fold)** under the tested comparisons). (zytnick2022discoveryandcharacterization pages 3-5)

## 4) Subcellular localization: what is known vs unknown
No retrieved source directly determines the **subcellular localization** of the mllDE gene product (e.g., cytosolic vs periplasmic, membrane association), nor does it present imaging/fractionation evidence for mllDE specifically. (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 10-12)

At the pathway level, the mll locus includes genes described as **TonB-dependent uptake components** in the same region (META1p4129–4131), consistent with a system where an extracellular or periplasmic trafficking step is coupled to outer-membrane transport; however, this does not specify where the mllDE-encoded protein acts. (zytnick2022discoveryandcharacterization pages 3-5)

## 5) Recent developments (prioritizing 2023–2024) and current research directions

### 5.1 2024 perspective: integration of lanthanophore systems with broader lanthanide uptake biology
A 2024 peer-reviewed study (Valdés et al., *Communications Biology*, publication date **Nov 2024**, DOI: **10.1038/s42003-024-07258-3**, URL: https://doi.org/10.1038/s42003-024-07258-3) discusses lanthanide-binding proteins (LanM homologs) and situates **methylolanthanin-type lanthanophore biosynthesis** within broader Ln uptake/handling systems (e.g., TonB-dependent transporters and “Ln3+ switch” regulatory context). While not providing new gene-specific biochemistry for mllDE, it represents a recent consolidation of mechanistic concepts relevant to why lanthanophore BGCs (including mll-like clusters) matter for lanthanide-dependent metabolism. (valdes2024anovelinsilico pages 1-2)

### 5.2 2023–2024 primary literature specific to mllDE
Within the tool-retrieved corpus for this run, **no 2023–2024 primary paper** was obtained that experimentally characterizes **mllDE (META1p4134) alone** (e.g., enzymology, structure, or targeted genetics). The most direct experimental evidence remains the cluster-level discovery/characterization study available here (bioRxiv 2022). (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 10-12)

## 6) Current applications and real-world implementations

### 6.1 Lanthanide recovery / biomining-relevant observations
Zytnick et al. report that *M. extorquens* AM1 responds to lanthanides at concentrations as low as **2.5 nM** and can **selectively bioaccumulate Nd from NdFeB magnets**, which they present as supportive of potential applications in lanthanide recovery/biomining; the mll locus contributes to bioaccumulation phenotypes, implying that methylolanthanin biosynthesis (and thus mllDE as a required biosynthetic gene) may be relevant to engineering or optimizing such processes. (zytnick2022discoveryandcharacterization pages 10-12)

### 6.2 Limits of application evidence for mllDE specifically
No retrieved source demonstrates a deployed industrial process specifically engineered around **mllDE** (e.g., pilot-scale lanthanide bioleaching using mllDE variants), and thus applications should currently be regarded as **prospective** and based on laboratory-scale phenotypes and conceptual integration with Ln uptake systems. (zytnick2022discoveryandcharacterization pages 10-12, valdes2024anovelinsilico pages 1-2)

## 7) Expert interpretation and functional annotation summary

### 7.1 Most defensible primary function statement (with evidence strength)
* **Primary function (strong, but pathway-level):** mllDE (META1p4134) is part of the **methylolanthanin biosynthetic gene cluster** required for synthesis of methylolanthanin, a lanthanide-binding metallophore that contributes to lanthanide bioaccumulation physiology in *M. extorquens* AM1. (zytnick2022discoveryandcharacterization pages 5-8, zytnick2022discoveryandcharacterization pages 8-10, zytnick2022discoveryandcharacterization media a750a99c)
* **Specific biochemical reaction/substrate specificity (unknown at gene level):** not established for mllDE alone in the retrieved literature. (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 10-12)
* **Cellular site of action (unknown at gene level):** not established for mllDE alone in the retrieved literature. (zytnick2022discoveryandcharacterization pages 3-5)

### 7.2 What would resolve mllDE’s function more precisely
Given the current evidence pattern (cluster-level knockout/overexpression), the next decisive steps would be (i) single-gene knockout/complementation of **mllDE**, and/or (ii) biochemical reconstitution of individual enzymatic steps in methylolanthanin assembly; however, such studies were not found in the retrieved set for this run. (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 5-8)

## 8) Evidence summary table

| Identifier(s) | Organism/strain | Genomic context (mll cluster boundaries and neighboring functions) | Proposed molecular role (inferred from homology/domain rules mentioned in evidence) | Experimental evidence (what was manipulated/measured) | Quantitative results | Notes/limitations | Key source (with year, venue, DOI/URL) |
|---|---|---|---|---|---|---|---|
| **mllDE**; **META1p4134**; user-provided **UniProt C5B1I6** | *Methylorubrum extorquens* AM1 (also referred to in source as *Methylobacterium extorquens* AM1) | Part of the **methylolanthanin (mll) biosynthetic gene cluster** spanning **META1p4129–META1p4138**. The cluster includes nearby TonB-dependent uptake-related genes **META1p4129–4131** and biosynthetic genes **META1p4132–4138**; Figure 2a places **mllDE** within the core biosynthetic operon alongside **mllA, mllBC, mllF, mllG, mllH, mllJ**. Neighboring functions include TonB-dependent uptake components and DUF-containing proteins (**META1p4136 DUF2218; META1p4138 DUF4142**) (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 5-8, zytnick2022discoveryandcharacterization media a750a99c) | **Not directly biochemically characterized at gene level.** By cluster homology, **mllA/mllBC/mllDE/mllF** are homologous to the **petrobactin asbABCDEF** locus, supporting assignment to an **NRPS-independent siderophore-like/lanthanophore biosynthetic module**. AntiSMASH-style rules for homologous loci required **IucA_IucC**, **AMP-binding**, **PP-binding (asbD)**, and **DUF6005 (asbE/PF19468)** signatures; these data support an inferred **carrier/PP-binding ACP-like role somewhere within the core mll biosynthetic machinery**, but the evidence snippets do **not** assign the PP-binding or DUF6005 motif specifically to **mllDE** alone (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 10-12) | Evidence is **cluster-level**, not gene-specific: researchers deleted the **mll locus** (in a **ΔmxaFΔmll** strain), overexpressed **mll biosynthetic genes** in trans (**pAZ1**), identified the product **methylolanthanin (MLL)** by UPLC-MS/MS and NMR, tested Ln-binding by MS, quantified intracellular Nd by ICP-MS, and tested rescue with exogenous purified MLL. No experiment in the snippets isolates **mllDE/META1p4134** alone (zytnick2022discoveryandcharacterization pages 8-10, zytnick2022discoveryandcharacterization pages 5-8, zytnick2022discoveryandcharacterization pages 3-5) | The **mll locus** was among the most induced under poorly soluble lanthanide conditions, with **~32-fold average upregulation** on **Nd2O3** versus **NdCl3**. **Deletion** of mll caused a **~30% decrease** in Ln bioaccumulation and a **~1.8-fold decrease** in Nd accumulation under NdCl3 in one assay; **overexpression** increased Nd accumulation by **~3.5-fold**. Exogenous **50 nM** MLL increased maximal OD under **2 µM NdCl3**; growth with **Nd2O3** in an overexpression background was reported as **0.026 h^-1** versus **0.037 h^-1** for ΔmxaF on NdCl3 (zytnick2022discoveryandcharacterization pages 8-10, zytnick2022discoveryandcharacterization pages 10-12, zytnick2022discoveryandcharacterization pages 3-5) | The symbol **mllDE** is mapped in the source to the AM1 mll cluster, but the available evidence does **not** provide a direct biochemical reaction, substrate specificity, localization, or domain assignment uniquely for **mllDE/C5B1I6**. Current support is therefore **indirect**, based on **cluster membership, homology, and pathway-level phenotypes** rather than purified-protein or knockout-complementation data for this single gene (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 10-12) | Zytnick et al. **2022**, **bioRxiv**, “Discovery and characterization of the first known biological lanthanide chelator,” DOI: **10.1101/2022.01.19.476857**, URL: **https://doi.org/10.1101/2022.01.19.476857** (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 8-10, zytnick2022discoveryandcharacterization pages 10-12, zytnick2022discoveryandcharacterization pages 5-8, zytnick2022discoveryandcharacterization media a750a99c) |


*Table: This table compiles the currently gathered evidence specific to mllDE/META1p4134 in Methylorubrum extorquens AM1. It distinguishes direct evidence from cluster-level inference, which is important because mllDE itself has not yet been individually characterized in the retrieved sources.*

## 9) Key visual evidence
A cluster schematic explicitly labeling **mllDE (META1p4134)** within the mll BGC is available (Figure 2a). (zytnick2022discoveryandcharacterization media a750a99c)

## 10) Primary sources cited (with publication dates and URLs)
1. Zytnick AM et al. **“Discovery and characterization of the first known biological lanthanide chelator.”** bioRxiv, **Jan 2022**. DOI: **10.1101/2022.01.19.476857**. URL: https://doi.org/10.1101/2022.01.19.476857 (zytnick2022discoveryandcharacterization pages 3-5, zytnick2022discoveryandcharacterization pages 8-10, zytnick2022discoveryandcharacterization pages 10-12, zytnick2022discoveryandcharacterization pages 5-8, zytnick2022discoveryandcharacterization media a750a99c)
2. Valdés JJ et al. **“A novel in-silico model explores LanM homologs among Hyphomicrobium spp.”** *Communications Biology*, **Nov 2024**. DOI: **10.1038/s42003-024-07258-3**. URL: https://doi.org/10.1038/s42003-024-07258-3 (valdes2024anovelinsilico pages 1-2)


References

1. (zytnick2022discoveryandcharacterization pages 3-5): Alexa M. Zytnick, Sophie M. Gutenthaler-Tietze, Allegra T. Aron, Zachary L. Reitz, Manh Tri Phi, Nathan M. Good, Daniel Petras, Lena J. Daumann, and N. Cecilia Martinez-Gomez. Discovery and characterization of the first known biological lanthanide chelator. bioRxiv, Jan 2022. URL: https://doi.org/10.1101/2022.01.19.476857, doi:10.1101/2022.01.19.476857. This article has 20 citations.

2. (zytnick2022discoveryandcharacterization media a750a99c): Alexa M. Zytnick, Sophie M. Gutenthaler-Tietze, Allegra T. Aron, Zachary L. Reitz, Manh Tri Phi, Nathan M. Good, Daniel Petras, Lena J. Daumann, and N. Cecilia Martinez-Gomez. Discovery and characterization of the first known biological lanthanide chelator. bioRxiv, Jan 2022. URL: https://doi.org/10.1101/2022.01.19.476857, doi:10.1101/2022.01.19.476857. This article has 20 citations.

3. (zytnick2022discoveryandcharacterization pages 10-12): Alexa M. Zytnick, Sophie M. Gutenthaler-Tietze, Allegra T. Aron, Zachary L. Reitz, Manh Tri Phi, Nathan M. Good, Daniel Petras, Lena J. Daumann, and N. Cecilia Martinez-Gomez. Discovery and characterization of the first known biological lanthanide chelator. bioRxiv, Jan 2022. URL: https://doi.org/10.1101/2022.01.19.476857, doi:10.1101/2022.01.19.476857. This article has 20 citations.

4. (valdes2024anovelinsilico pages 1-2): James J. Valdés, Daniel A. Petrash, and Kurt O. Konhauser. A novel in-silico model explores lanm homologs among hyphomicrobium spp. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07258-3, doi:10.1038/s42003-024-07258-3. This article has 3 citations and is from a peer-reviewed journal.

5. (zytnick2022discoveryandcharacterization pages 8-10): Alexa M. Zytnick, Sophie M. Gutenthaler-Tietze, Allegra T. Aron, Zachary L. Reitz, Manh Tri Phi, Nathan M. Good, Daniel Petras, Lena J. Daumann, and N. Cecilia Martinez-Gomez. Discovery and characterization of the first known biological lanthanide chelator. bioRxiv, Jan 2022. URL: https://doi.org/10.1101/2022.01.19.476857, doi:10.1101/2022.01.19.476857. This article has 20 citations.

6. (zytnick2022discoveryandcharacterization pages 5-8): Alexa M. Zytnick, Sophie M. Gutenthaler-Tietze, Allegra T. Aron, Zachary L. Reitz, Manh Tri Phi, Nathan M. Good, Daniel Petras, Lena J. Daumann, and N. Cecilia Martinez-Gomez. Discovery and characterization of the first known biological lanthanide chelator. bioRxiv, Jan 2022. URL: https://doi.org/10.1101/2022.01.19.476857, doi:10.1101/2022.01.19.476857. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](mllDE-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000009 Figure 2a shows the methylolanthanin (mll) biosynthetic gene cluster (META1p4129–META1p4138) from Methylobacterium extorquens AM1. ](mllDE-deep-research-falcon_artifacts/image-1.png)

## Citations

1. zytnick2022discoveryandcharacterization pages 10-12
2. valdes2024anovelinsilico pages 1-2
3. zytnick2022discoveryandcharacterization pages 8-10
4. zytnick2022discoveryandcharacterization pages 3-5
5. zytnick2022discoveryandcharacterization pages 5-8
6. MLL−H+ + Ln3+
7. https://doi.org/10.1038/s42003-024-07258-3
8. https://doi.org/10.1101/2022.01.19.476857**
9. https://doi.org/10.1101/2022.01.19.476857
10. https://doi.org/10.1101/2022.01.19.476857,
11. https://doi.org/10.1038/s42003-024-07258-3,