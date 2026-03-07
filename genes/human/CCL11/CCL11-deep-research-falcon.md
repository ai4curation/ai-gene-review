---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T03:10:19.457115'
end_time: '2026-03-06T03:20:07.995637'
duration_seconds: 588.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CCL11
  gene_symbol: CCL11
  uniprot_accession: P51671
  protein_description: 'RecName: Full=Eotaxin; AltName: Full=C-C motif chemokine 11;
    AltName: Full=Eosinophil chemotactic protein; AltName: Full=Small-inducible cytokine
    A11; Flags: Precursor;'
  gene_info: Name=CCL11; Synonyms=SCYA11;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the intercrine beta (chemokine CC) family.
  protein_domains: Chemokine_b/g/d. (IPR039809); Chemokine_CC_CS. (IPR000827); Chemokine_IL8-like_dom.
    (IPR001811); Interleukin_8-like_sf. (IPR036048); IL8 (PF00048)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P51671
- **Protein Description:** RecName: Full=Eotaxin; AltName: Full=C-C motif chemokine 11; AltName: Full=Eosinophil chemotactic protein; AltName: Full=Small-inducible cytokine A11; Flags: Precursor;
- **Gene Information:** Name=CCL11; Synonyms=SCYA11;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the intercrine beta (chemokine CC) family.
- **Key Domains:** Chemokine_b/g/d. (IPR039809); Chemokine_CC_CS. (IPR000827); Chemokine_IL8-like_dom. (IPR001811); Interleukin_8-like_sf. (IPR036048); IL8 (PF00048)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CCL11" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CCL11' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CCL11** (gene ID: CCL11, UniProt: P51671) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Research report: Human **CCL11** (Eotaxin-1) functional annotation (UniProt **P51671**)

## 1) Verification of gene/protein identity (mandatory)
The UniProt accession **P51671** corresponds to human **CCL11**, commonly called **eotaxin‑1** and historically described as an **eosinophil chemotactic protein**; recent reviews continue to use these exact names and position it within the **CC chemokine** family (i.e., C‑C motif ligand 11). (wang2024spotlightonproinflammatory pages 6-7, wang2025emergingrolesof pages 4-5)

Functionally, the dominant, high‑affinity receptor is **CCR3**, which is repeatedly described as the principal receptor mediating canonical eotaxin‑1 biology (eosinophil recruitment/activation) and is consistent with CCL11 being a secreted chemokine ligand rather than an enzyme or transporter. (wang2025emergingrolesof pages 4-5, xie2024immunologicaspectsof pages 9-10)

## 2) Key concepts and definitions (current understanding)
### 2.1 What CCL11 is
CCL11 is a **chemokine ligand** that forms gradients in tissues and is best known for **selective recruitment of eosinophils** in type‑2/allergic inflammation. (wang2025emergingrolesof pages 4-5, wang2025emergingrolesof pages 2-4)

### 2.2 Canonical receptor axis (CCL11 → CCR3)
CCR3 is described as the **main/high‑affinity receptor** for CCL11 and as a **G‑protein‑coupled receptor** whose signaling is associated with **intracellular calcium mobilization**, supporting chemotaxis and activation in CCR3+ immune cells. (wang2025emergingrolesof pages 4-5)

In asthma-focused synthesis, **CCR3 is selectively activated** by eotaxin‑1 (CCL11) (as well as eotaxin‑2/CCL24 and eotaxin‑3/CCL26), and CCR3 activation—together with endothelial adhesion molecules—facilitates eosinophil recruitment from blood into lung tissues. (xie2024immunologicaspectsof pages 9-10)

### 2.3 Noncanonical/secondary receptor interactions
A recent focused review summarizes additional functional interactions: CCL11 can act as a **CCR5 agonist** (and can induce CCR5 internalization in monocytes/macrophages) and has **complex/controversial CCR2 activity** (reported as partial agonist in some settings or as a natural antagonist in others). (wang2025emergingrolesof pages 4-5)

### 2.4 Cellular sources and inducibility
Across recent reviews, CCL11 production is attributed to many cell types, including **eosinophils**, **T and B cells**, **fibroblasts**, **epithelial cells**, **endothelial cells**, **macrophages**, and in CNS discussions also **microglia**. (wang2024spotlightonproinflammatory pages 6-7, wang2025emergingrolesof pages 2-4)

Type‑2 cytokines are repeatedly cited as upstream inducers; for example, Th2 cytokines **IL‑4, IL‑10, and IL‑13** induce CCL11 production in a 2024 review of chemokines in cognitive impairment. (wang2024spotlightonproinflammatory pages 6-7)

## 3) Primary molecular function, pathways, and localization
### 3.1 Primary function: chemotaxis (not enzymatic catalysis)
CCL11 is not an enzyme; its primary biochemical role is **chemokine signaling** as a soluble ligand that binds chemokine receptors and orchestrates **directed cell migration** and related activation programs.

### 3.2 Extracellular localization and tissue-to-tissue trafficking
CCL11 is treated in recent literature as an **extracellular, secreted** mediator that can function in blood and tissues and—importantly for CNS indications—can be **transported from blood to brain via the blood–brain barrier (BBB)**. (wang2024spotlightonproinflammatory pages 6-7)

### 3.3 Allergic airway disease: eosinophil recruitment and extravasation
A 2024 asthma immunology review describes a mechanistic module in which eotaxin‑1 (CCL11) selectively activates **CCR3** and, together with endothelial adhesion molecule expression—especially **VCAM‑1** and **ICAM‑1**—supports recruitment/extravasation of eosinophils from blood into lung mucosa and interstitium. (xie2024immunologicaspectsof pages 9-10)

A more mechanistic, multi-context synthesis highlights airway‑relevant producers and inductive pathways: bronchial epithelial cells can be induced via **IL‑4/STAT6**, and airway smooth muscle cells via **IL‑17A‑driven MAPK pathways (p38/JNK/ERK)**; eosinophils themselves can be major sources, supporting an **autocrine chemotactic loop**. (wang2025emergingrolesof pages 2-4)

### 3.4 Neuroinflammation/cognitive impairment: CCR3–NOX‑1–ROS axis in microglia
A 2024 Frontiers in Immunology review frames CCL11 as an **aging/accelerated aging immune marker** and summarizes mechanistic links to cognition: CCL11 can contribute to cognitive impairment by **inhibiting neurogenesis**, **reducing synaptic density**, and promoting neuronal cytotoxicity. (wang2024spotlightonproinflammatory pages 6-7, wang2024spotlightonproinflammatory pages 7-8)

Mechanistically, the same review proposes a microglial pathway in which CCL11 binding to **CCR3 on microglia** upregulates **NOX‑1**, increases **microglial ROS**, and drives inflammation-associated neuronal injury/death. (wang2024spotlightonproinflammatory pages 6-7)

### 3.5 Angiogenesis and remodeling (CCR3 on endothelial cells; PI3K/Akt and MAPKs)
A recent mechanistic synthesis describes evidence that CCL11 can act on **CCR3+ endothelial cells** to promote angiogenic responses and can signal through pathways including **PI3K/Akt** and **ERK/p38**, and can upregulate matrix remodeling enzymes (e.g., MMP-2/3) in a CCR3-dependent fashion. (wang2025emergingrolesof pages 7-9)

## 4) Recent developments (prioritizing 2023–2024)
### 4.1 2023: Recombinant CCL11 can induce pro-oxidant DNA damage responses and senescence programs in human lung fibroblasts
Lavandoski et al. (Frontiers in Immunology; **published Oct 2023**; https://doi.org/10.3389/fimmu.2023.1243537) tested recombinant human CCL11 (rhCCL11) in **MRC‑5 human lung fibroblasts**.

Key findings include:
- High‑dose rhCCL11 (500 ng/10^5 cells/mL) induced **ROS overproduction within 60 minutes** and persisting up to 4 hours (p<0.05). (lavandoski2023eotaxin1ccl11promotescellular pages 5-7)
- rhCCL11 increased DNA damage response markers at 2 hours, with increased **γH2AX** (% positive p<0.0001; MFI p=0.005) and **phospho‑TP53** (% positive p<0.0001; MFI p=0.0352), resolving by 24 hours. (lavandoski2023eotaxin1ccl11promotescellular pages 5-7)
- A 24‑hour rhCCL11 exposure increased **SA‑β‑gal** senescence readout (percentage p=0.0481; MFI p=0.0229) and reduced proliferation marker **Ki‑67** (p=0.0192). (lavandoski2023eotaxin1ccl11promotescellular pages 5-7)
- rhCCL11 also promoted a pro-inflammatory senescence-associated secretory phenotype (SASP), increasing **CCL11 secretion** (p<0.0001) and increasing **IL‑6** (p=0.0005) and **IL‑8** (p=0.0008). (lavandoski2023eotaxin1ccl11promotescellular pages 5-7)

These data extend CCL11 functional annotation beyond chemotaxis by supporting direct, receptor-mediated (or receptor-associated) cellular stress programs in structural lung cells relevant to chronic airway disease biology. (lavandoski2023eotaxin1ccl11promotescellular pages 5-7)

**Visual evidence from the primary paper:** cropped panels for ROS kinetics and DNA-damage marker flow cytometry are available. (lavandoski2023eotaxin1ccl11promotescellular media 88940820, lavandoski2023eotaxin1ccl11promotescellular media ba4c996b)

### 4.2 2024: CCL11 in neuro-immune mechanisms of cognitive impairment
Wang et al. (Frontiers in Immunology; **published Jul 2024**; https://doi.org/10.3389/fimmu.2024.1421076) provides a 2024 review synthesis emphasizing that CCL11 can cross the BBB and engage CCR3 on CNS cells, and highlights microglial oxidative mechanisms (NOX‑1 → ROS) as a plausible route to neurotoxicity. (wang2024spotlightonproinflammatory pages 6-7)

### 4.3 2024: CCL11/CCR3 in asthma immune translation
Xie et al. (Frontiers in Immunology; **published Oct 2024**; https://doi.org/10.3389/fimmu.2024.1478624) integrates CCL11 into the type‑2 asthma effector framework in which CCR3 activation by eotaxins enables eosinophil recruitment, coordinated with IL‑4/IL‑13-driven endothelial adhesion molecule priming (VCAM‑1/ICAM‑1). (xie2024immunologicaspectsof pages 9-10)

## 5) Current applications and real-world implementations
### 5.1 Clinical biomarker use case: traumatic brain injury (TBI)
Negrin et al. (Journal of Clinical Medicine; **published Jul 2024**; https://doi.org/10.3390/jcm13144218) evaluated serum eotaxin (CCL11) in a matched polytrauma cohort.

Reported performance characteristics include:
- **ROC AUC = 0.718** for admission eotaxin level identifying TBI (limited clinical utility). (negrin2024differencesineotaxin pages 1-2, negrin2024differencesineotaxin pages 9-10)
- A cutoff of **154 pg/mL** yielded **sensitivity 0.707** and **specificity 0.683**. (negrin2024differencesineotaxin pages 1-2)
- Odds of prevalent TBI increased **10.5% per 20 pg/mL increase** in admission eotaxin. (negrin2024differencesineotaxin pages 1-2)

This is a concrete example of CCL11 deployment as an acute-care biomarker candidate, with quantified performance. (negrin2024differencesineotaxin pages 1-2)

### 5.2 Clinical trials/registries measuring eotaxin/CCL11
ClinicalTrials.gov includes observational implementations where eotaxin/CCL11 is an analyte:

- **NCT06211244** (Sponsor: Tungs’ Taichung Metroharbour Hospital) “Association of Serum Eotaxin Levels and Markers of Myocardiac Injury in Hemodialysis Patients” (Status: **Completed**; **Start 2024-05-02**, **Completion 2024-12-31**; Enrollment 291). Primary outcome: serum eotaxin biomarker analysis by ELISA; includes secondary inflammatory/oxidative injury markers (IL‑6, MCP‑1, 8‑isoprostane) and cardiac injury marker hs‑troponin I. (NCT06211244 chunk 1)

- **NCT03521882** (Royal Devon and Exeter NHS Foundation Trust) “Timed Interval Measurement of Eotaxin in Stroke Study” (Status: **Completed**; Start 2017-05-22; Completion 2019-05-30). Primary outcome: **plasma eotaxin concentration** tracked across 0–7 days after stroke-like presentations to define kinetics/feasibility for larger studies. (NCT03521882 chunk 1)

These registry entries reflect real-world implementation of CCL11 measurement as a clinical research biomarker rather than a therapeutic product. (NCT06211244 chunk 1, NCT03521882 chunk 1)

## 6) Expert opinions and authoritative synthesis (what reviews converge on)
Across recent reviews, there is strong consensus that:
1) **CCL11–CCR3** is the core axis for eosinophil recruitment/activation in type‑2 inflammation, with CCL11 being one of the eotaxins that selectively activate CCR3. (xie2024immunologicaspectsof pages 9-10, wang2025emergingrolesof pages 4-5)
2) CCL11 has **pleiotropic context-dependent biology** beyond eosinophil chemotaxis (e.g., tissue remodeling/angiogenesis, CNS effects), and may act via CCR3 on non-hematopoietic cells and through additional chemokine receptors in certain contexts (CCR5; CCR2 disputed). (wang2025emergingrolesof pages 7-9, wang2025emergingrolesof pages 4-5)
3) In CNS contexts, CCL11 is increasingly discussed as part of **inflammatory aging** frameworks and neuroinflammation, including oxidative stress mechanisms in microglia. (wang2024spotlightonproinflammatory pages 6-7)

## 7) Key statistics/data points (recent studies)
- **TBI biomarker performance (2024):** AUC 0.718; cutoff 154 pg/mL; sensitivity 0.707; specificity 0.683; +10.5% odds of TBI per 20 pg/mL eotaxin increase. (negrin2024differencesineotaxin pages 1-2, negrin2024differencesineotaxin pages 9-10)
- **rhCCL11 mechanistic cell biology (2023):** ROS induction within 60 min (p<0.05); γH2AX and p‑TP53 induction at 2h (p<0.0001 for % positive; MFI p=0.005 and p=0.0352); SA‑β‑gal increase at 24h (p=0.0481; MFI p=0.0229); Ki‑67 reduction (p=0.0192); increased IL‑6 (p=0.0005) and IL‑8 (p=0.0008). (lavandoski2023eotaxin1ccl11promotescellular pages 5-7)

## 8) Summary: functional annotation statement (for databases)
**CCL11 (eotaxin‑1)** is a secreted CC chemokine ligand whose canonical function is **CCR3‑dependent chemotaxis and activation** of eosinophils (and other CCR3+ type‑2 immune cells), central to **type‑2/allergic inflammation** including asthma, where eosinophil extravasation is coordinated with endothelial adhesion pathways. (xie2024immunologicaspectsof pages 9-10, wang2025emergingrolesof pages 4-5)

Beyond leukocyte trafficking, recent primary and review evidence supports roles in (i) **neuroinflammation and cognitive impairment** via BBB trafficking and microglial **CCR3–NOX‑1–ROS** signaling, and (ii) **tissue remodeling/angiogenesis** via CCR3+ endothelial signaling (e.g., PI3K/Akt, ERK/p38) and matrix remodeling programs. (wang2024spotlightonproinflammatory pages 6-7, wang2025emergingrolesof pages 7-9)

Finally, recombinant CCL11 can directly induce **pro-oxidant DNA damage signaling and senescence-associated phenotypes** in human lung fibroblasts, suggesting a mechanistic link between chronic inflammatory chemokines and structural-cell aging programs relevant to airway disease. (lavandoski2023eotaxin1ccl11promotescellular pages 5-7, lavandoski2023eotaxin1ccl11promotescellular media 88940820)

---

| Functional Context | Key Receptor & Signaling | Producing Cells / Inducers | Target Cells & Outcomes | Key Evidence / Statistics | Recent Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Allergic Airway Disease** | **CCR3** (High affinity, primary); **CCR5** (agonist); **CCR2** (antagonist/partial). Signals via $Ca^{2+}$ mobilization (wang2025emergingrolesof pages 4-5). | Eosinophils (autocrine), Epithelium (**IL-4**/**STAT6**), Smooth Muscle (**IL-17A**/**MAPK**) (wang2025emergingrolesof pages 2-4). | **Eosinophils**, Basophils, Th2 cells. Drives chemotaxis, activation, and Th2 polarization (wang2025emergingrolesof pages 5-7). | Elevated CCR3/CCL11 correlates with asthma severity. CCR3 mediates extravasation via VCAM-1 interaction (xie2024immunologicaspectsof pages 9-10). | [Wang et al. 2025](https://doi.org/10.3390/ijms26104662) (wang2025emergingrolesof pages 1-2)<br>[Xie et al. 2024](https://doi.org/10.3389/fimmu.2024.1478624) (xie2024immunologicaspectsof pages 9-10) |
| **Neuroinflammation & Cognitive Decline** | **CCR3** (Microglia). Upregulates **NOX-1**, increasing ROS production (wang2024spotlightonproinflammatory pages 6-7). | Neurons, Astrocytes, Microglia. Induced by **IL-4**, **IL-13**, aging factors (wang2024spotlightonproinflammatory pages 6-7). | Microglia, Neurons. Inhibits neurogenesis, reduces synaptic density, promotes cytotoxicity (wang2024spotlightonproinflammatory pages 6-7). | Anti-CCL11 Ab improved motor outcomes in PD mice (wang2024spotlightonproinflammatory pages 6-7). Plasma from aged mice impairs memory in young mice (wang2024spotlightonproinflammatory pages 7-8). | [Wang et al. 2024](https://doi.org/10.3389/fimmu.2024.1421076) (wang2024spotlightonproinflammatory pages 6-7) |
| **Angiogenesis & Tissue Remodeling** | **CCR3** (Endothelial). Signals via **PI3K/Akt**, **ERK/p38 MAPK** (wang2025emergingrolesof pages 7-9). | Endothelial cells, Fibroblasts (wang2025emergingrolesof pages 2-4). | Endothelial cells. Promotes chemotaxis, vascularization, and ECM remodeling (**MMP-2/3**) (wang2025emergingrolesof pages 7-9). | Recombinant CCL11 directly induces angiogenic responses *in vivo* and promotes HUVEC vascularization (wang2025emergingrolesof pages 7-9). | [Wang et al. 2025](https://doi.org/10.3390/ijms26104662) (wang2025emergingrolesof pages 7-9) |
| **Cellular Senescence** | **CCR3**. Activates DNA Damage Response (**p-p53**, **$\gamma$H2AX**) via ROS (lavandoski2023eotaxin1ccl11promotescellular pages 5-7). | Lung Fibroblasts (Autocrine loop) (lavandoski2023eotaxin1ccl11promotescellular pages 5-7). | Fibroblasts. Induces senescence (SA-$\beta$-gal), reduces proliferation (Ki-67), SASP secretion (IL-6/8) (lavandoski2023eotaxin1ccl11promotescellular pages 5-7). | rhCCL11 (500 ng/mL) increased ROS (<60 min) and $\gamma$H2AX ($p<0.0001$, 2h); increased SA-$\beta$-gal at 24h ($p=0.048$) (lavandoski2023eotaxin1ccl11promotescellular pages 5-7). | [Lavandoski et al. 2023](https://doi.org/10.3389/fimmu.2023.1243537) (lavandoski2023eotaxin1ccl11promotescellular pages 5-7) |
| **TBI Biomarker** | N/A (Systemic detection). | Brain tissue (sole source after TBI) (negrin2024differencesineotaxin pages 1-2). | Systemic circulation (Diagnostic marker). | Cutoff 154 pg/mL for TBI diagnosis: Sens 0.707, Spec 0.683, **AUC 0.718**. Odds +10.5% per 20 pg/mL increase (negrin2024differencesineotaxin pages 9-10). | [Negrin et al. 2024](https://doi.org/10.3390/jcm13144218) (negrin2024differencesineotaxin pages 1-2, negrin2024differencesineotaxin pages 9-10) |
| **Clinical Trials** | N/A | Patient Serum/Plasma levels. | Hemodialysis; Stroke patients. | **NCT06211244** (2024): Serum Eotaxin/Myocardiac injury. **NCT03521882**: Plasma Eotaxin kinetics in stroke (NCT06211244 chunk 1, NCT03521882 chunk 1). | [ClinicalTrials.gov](https://clinicaltrials.gov) (NCT06211244 chunk 1, NCT03521882 chunk 1) |


*Table: A summary of human CCL11 functions, mechanisms, and clinical relevance based on recent literature, highlighting its dual roles in allergic inflammation and aging-associated pathologies.*

## References (URLs and publication dates)
- Lavandoski P. et al. **Eotaxin‑1/CCL11 promotes cellular senescence in human-derived fibroblasts through pro-oxidant and pro-inflammatory pathways.** *Frontiers in Immunology*. **Oct 2023**. https://doi.org/10.3389/fimmu.2023.1243537 (lavandoski2023eotaxin1ccl11promotescellular pages 5-7)
- Wang C. et al. **Spotlight on pro-inflammatory chemokines: regulators of cellular communication in cognitive impairment.** *Frontiers in Immunology*. **Jul 2024**. https://doi.org/10.3389/fimmu.2024.1421076 (wang2024spotlightonproinflammatory pages 6-7)
- Xie C. et al. **Immunologic aspects of asthma: from molecular mechanisms to disease pathophysiology and clinical translation.** *Frontiers in Immunology*. **Oct 2024**. https://doi.org/10.3389/fimmu.2024.1478624 (xie2024immunologicaspectsof pages 9-10)
- Negrin L.L. et al. **Differences in Eotaxin Serum Levels between Polytraumatized Patients with and without Concomitant Traumatic Brain Injury—A Matched Pair Analysis.** *Journal of Clinical Medicine*. **Jul 2024**. https://doi.org/10.3390/jcm13144218 (negrin2024differencesineotaxin pages 1-2)
- ClinicalTrials.gov. **NCT06211244**. “Association of Serum Eotaxin Levels and Markers of Myocardiac Injury in Hemodialysis Patients.” **Start 2024‑05‑02; Completed; Completion 2024‑12‑31.** https://clinicaltrials.gov/study/NCT06211244 (NCT06211244 chunk 1)
- ClinicalTrials.gov. **NCT03521882**. “Timed Interval Measurement of Eotaxin in Stroke Study.” **Completed; last update posted 2020‑11‑06.** https://clinicaltrials.gov/study/NCT03521882 (NCT03521882 chunk 1)


References

1. (wang2024spotlightonproinflammatory pages 6-7): Chenxu Wang, Jiayi Wang, Zhichao Zhu, Jialing Hu, and Yong Lin. Spotlight on pro-inflammatory chemokines: regulators of cellular communication in cognitive impairment. Frontiers in Immunology, Jul 2024. URL: https://doi.org/10.3389/fimmu.2024.1421076, doi:10.3389/fimmu.2024.1421076. This article has 26 citations and is from a peer-reviewed journal.

2. (wang2025emergingrolesof pages 4-5): Jiaqi Wang, Kwan Man, and Kevin Tak-Pan Ng. Emerging roles of c-c motif ligand 11 (ccl11) in cancers and liver diseases: mechanisms and therapeutic implications. International Journal of Molecular Sciences, 26:4662, May 2025. URL: https://doi.org/10.3390/ijms26104662, doi:10.3390/ijms26104662. This article has 7 citations.

3. (xie2024immunologicaspectsof pages 9-10): Cong Xie, Jingyan Yang, Aman Gul, Yifan Li, Rui Zhang, Maimaititusun Yalikun, Xiaotong Lv, Yuhan Lin, Qingli Luo, and Huijuan Gao. Immunologic aspects of asthma: from molecular mechanisms to disease pathophysiology and clinical translation. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1478624, doi:10.3389/fimmu.2024.1478624. This article has 42 citations and is from a peer-reviewed journal.

4. (wang2025emergingrolesof pages 2-4): Jiaqi Wang, Kwan Man, and Kevin Tak-Pan Ng. Emerging roles of c-c motif ligand 11 (ccl11) in cancers and liver diseases: mechanisms and therapeutic implications. International Journal of Molecular Sciences, 26:4662, May 2025. URL: https://doi.org/10.3390/ijms26104662, doi:10.3390/ijms26104662. This article has 7 citations.

5. (wang2024spotlightonproinflammatory pages 7-8): Chenxu Wang, Jiayi Wang, Zhichao Zhu, Jialing Hu, and Yong Lin. Spotlight on pro-inflammatory chemokines: regulators of cellular communication in cognitive impairment. Frontiers in Immunology, Jul 2024. URL: https://doi.org/10.3389/fimmu.2024.1421076, doi:10.3389/fimmu.2024.1421076. This article has 26 citations and is from a peer-reviewed journal.

6. (wang2025emergingrolesof pages 7-9): Jiaqi Wang, Kwan Man, and Kevin Tak-Pan Ng. Emerging roles of c-c motif ligand 11 (ccl11) in cancers and liver diseases: mechanisms and therapeutic implications. International Journal of Molecular Sciences, 26:4662, May 2025. URL: https://doi.org/10.3390/ijms26104662, doi:10.3390/ijms26104662. This article has 7 citations.

7. (lavandoski2023eotaxin1ccl11promotescellular pages 5-7): Patrícia Lavandoski, Vinícius Pierdoná, Rafael Moura Maurmann, Lucas Kich Grun, Fatima T. C. R. Guma, and Florencia María Barbé-Tuana. Eotaxin-1/ccl11 promotes cellular senescence in human-derived fibroblasts through pro-oxidant and pro-inflammatory pathways. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1243537, doi:10.3389/fimmu.2023.1243537. This article has 29 citations and is from a peer-reviewed journal.

8. (lavandoski2023eotaxin1ccl11promotescellular media 88940820): Patrícia Lavandoski, Vinícius Pierdoná, Rafael Moura Maurmann, Lucas Kich Grun, Fatima T. C. R. Guma, and Florencia María Barbé-Tuana. Eotaxin-1/ccl11 promotes cellular senescence in human-derived fibroblasts through pro-oxidant and pro-inflammatory pathways. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1243537, doi:10.3389/fimmu.2023.1243537. This article has 29 citations and is from a peer-reviewed journal.

9. (lavandoski2023eotaxin1ccl11promotescellular media ba4c996b): Patrícia Lavandoski, Vinícius Pierdoná, Rafael Moura Maurmann, Lucas Kich Grun, Fatima T. C. R. Guma, and Florencia María Barbé-Tuana. Eotaxin-1/ccl11 promotes cellular senescence in human-derived fibroblasts through pro-oxidant and pro-inflammatory pathways. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1243537, doi:10.3389/fimmu.2023.1243537. This article has 29 citations and is from a peer-reviewed journal.

10. (negrin2024differencesineotaxin pages 1-2): Lukas L. Negrin, Robin Ristl, Gregor Wollner, and Stefan Hajdu. Differences in eotaxin serum levels between polytraumatized patients with and without concomitant traumatic brain injury—a matched pair analysis. Journal of Clinical Medicine, 13:4218, Jul 2024. URL: https://doi.org/10.3390/jcm13144218, doi:10.3390/jcm13144218. This article has 2 citations.

11. (negrin2024differencesineotaxin pages 9-10): Lukas L. Negrin, Robin Ristl, Gregor Wollner, and Stefan Hajdu. Differences in eotaxin serum levels between polytraumatized patients with and without concomitant traumatic brain injury—a matched pair analysis. Journal of Clinical Medicine, 13:4218, Jul 2024. URL: https://doi.org/10.3390/jcm13144218, doi:10.3390/jcm13144218. This article has 2 citations.

12. (NCT06211244 chunk 1):  Association of Serum Eotaxin Levels and Markers of Myocardiac Injury in Hemodialysis Patients. Tungs' Taichung Metroharbour Hospital. 2024. ClinicalTrials.gov Identifier: NCT06211244

13. (NCT03521882 chunk 1):  Timed Interval Measurement of Eotaxin in Stroke Study. Royal Devon and Exeter NHS Foundation Trust. 2017. ClinicalTrials.gov Identifier: NCT03521882

14. (wang2025emergingrolesof pages 5-7): Jiaqi Wang, Kwan Man, and Kevin Tak-Pan Ng. Emerging roles of c-c motif ligand 11 (ccl11) in cancers and liver diseases: mechanisms and therapeutic implications. International Journal of Molecular Sciences, 26:4662, May 2025. URL: https://doi.org/10.3390/ijms26104662, doi:10.3390/ijms26104662. This article has 7 citations.

15. (wang2025emergingrolesof pages 1-2): Jiaqi Wang, Kwan Man, and Kevin Tak-Pan Ng. Emerging roles of c-c motif ligand 11 (ccl11) in cancers and liver diseases: mechanisms and therapeutic implications. International Journal of Molecular Sciences, 26:4662, May 2025. URL: https://doi.org/10.3390/ijms26104662, doi:10.3390/ijms26104662. This article has 7 citations.

## Citations

1. wang2025emergingrolesof pages 4-5
2. xie2024immunologicaspectsof pages 9-10
3. wang2024spotlightonproinflammatory pages 6-7
4. wang2025emergingrolesof pages 2-4
5. wang2025emergingrolesof pages 7-9
6. negrin2024differencesineotaxin pages 1-2
7. wang2025emergingrolesof pages 5-7
8. wang2025emergingrolesof pages 1-2
9. wang2024spotlightonproinflammatory pages 7-8
10. negrin2024differencesineotaxin pages 9-10
11. Wang et al. 2025
12. Xie et al. 2024
13. Wang et al. 2024
14. Lavandoski et al. 2023
15. Negrin et al. 2024
16. ClinicalTrials.gov
17. https://doi.org/10.3389/fimmu.2023.1243537
18. https://doi.org/10.3389/fimmu.2024.1421076
19. https://doi.org/10.3389/fimmu.2024.1478624
20. https://doi.org/10.3390/jcm13144218
21. https://doi.org/10.3390/ijms26104662
22. https://clinicaltrials.gov
23. https://clinicaltrials.gov/study/NCT06211244
24. https://clinicaltrials.gov/study/NCT03521882
25. https://doi.org/10.3389/fimmu.2024.1421076,
26. https://doi.org/10.3390/ijms26104662,
27. https://doi.org/10.3389/fimmu.2024.1478624,
28. https://doi.org/10.3389/fimmu.2023.1243537,
29. https://doi.org/10.3390/jcm13144218,