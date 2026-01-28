---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T23:00:54.729514'
end_time: '2026-01-23T23:11:17.950465'
duration_seconds: 623.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: THBS2
  gene_symbol: THBS2
  uniprot_accession: P35442
  protein_description: 'RecName: Full=Thrombospondin-2; Flags: Precursor;'
  gene_info: Name=THBS2; Synonyms=TSP2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the thrombospondin family. .
  protein_domains: ConA-like_dom_sf. (IPR013320); EGF-like_Ca-bd_dom. (IPR001881);
    EGF-like_dom. (IPR000742); EGF_dom. (IPR024731); Thrombospondin_3-like_rpt. (IPR003367)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P35442
- **Protein Description:** RecName: Full=Thrombospondin-2; Flags: Precursor;
- **Gene Information:** Name=THBS2; Synonyms=TSP2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the thrombospondin family. .
- **Key Domains:** ConA-like_dom_sf. (IPR013320); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_dom. (IPR000742); EGF_dom. (IPR024731); Thrombospondin_3-like_rpt. (IPR003367)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "THBS2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'THBS2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **THBS2** (gene ID: THBS2, UniProt: P35442) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Thrombospondin-2 (THBS2/TSP2): A Comprehensive Functional Annotation

## 1. Introduction and Overview

Thrombospondin-2 (TSP2, also known as THBS2; UniProt: P35442) is a secreted, trimeric glycoprotein belonging to the thrombospondin family of matricellular proteins. Unlike structural matrix proteins that provide mechanical support to tissues, TSP2 functions primarily by modulating cell-matrix interactions and influencing the bioavailability of proteases and growth factors in the pericellular environment [bornstein-2000-tsp2-matricellular-abstract]. The protein is synthesized as a precursor of approximately 1172 amino acids in humans and is processed to its mature form upon secretion into the extracellular space.

TSP2 is closely related to thrombospondin-1 (TSP1) and shares substantial structural homology with it, forming the "subgroup A" of the thrombospondin family [calabro-2014-tsp2-ecm-assembly-abstract]. However, TSP2 differs from TSP1 in its temporal and spatial expression patterns and in certain critical functional properties, most notably its inability to activate latent TGF-β [simantov-2005-cd36-antiangiogenic-abstract]. The primary functions of TSP2 include: (1) regulation of extracellular matrix (ECM) assembly and collagen fibrillogenesis; (2) inhibition of angiogenesis through interactions with endothelial cell receptors; (3) modulation of matrix metalloproteinase-2 (MMP2) levels and activity; and (4) regulation of cell-matrix adhesion. These functions make TSP2 a critical regulator of wound healing, tissue repair, bone remodeling, and cardiovascular homeostasis [lawler-2012-angiogenesis-regulation-abstract].

## 2. Protein Structure and Domain Architecture

TSP2 is a homotrimeric protein, with each monomer of approximately 130-150 kDa connected by disulfide bonds. The modular architecture of TSP2, shared with TSP1, consists of distinct functional domains arranged from the N-terminus to C-terminus [kvansakul-2004-tsp1-structure-abstract]:

**N-terminal domain (NTD):** This globular domain at the amino terminus contains heparin-binding sites and is involved in interactions with cell surface proteoglycans. The N-terminal region is essential for multimerization into the characteristic trimeric structure.

**Procollagen/von Willebrand factor type C (vWC) domain:** This domain is thought to participate in protein-protein interactions during ECM assembly.

**Three thrombospondin type 1 repeats (TSRs):** Also known as properdin-like repeats, these domains are critical for several TSP2 functions including anti-angiogenic activity and interaction with MMP2 [bein-2000-tsp-mmp2-interaction-abstract]. The TSRs contain the CSVTCG (or similar) sequences that are recognized by the scavenger receptor CD36. Importantly, TSP2 contains three TSRs that mediate its antiangiogenic properties through CD36, but unlike TSP1, TSP2 lacks the KRFK sequence required for activation of latent TGF-β [simantov-2005-cd36-antiangiogenic-abstract].

**Three EGF-like repeats:** These calcium-binding domains (IPR001881, IPR000742, IPR024731) participate in protein-protein interactions and contribute to the structural organization of the signature domain.

**Calcium-binding type 3 repeats (T3 repeats):** TSP2 contains 13 calcium-binding type 3 repeats (IPR003367), which form a "wire" structure that is critically dependent on calcium ions for proper folding. Crystal structure analysis has revealed that two DxDxDGxxDxxD motifs per repeat each encapsulate two calcium ions in a novel arrangement [kvansakul-2004-tsp1-structure-abstract]. The availability of RGD motifs for cell attachment is modulated by calcium loading, providing a mechanism for conformational regulation of TSP2 function.

**C-terminal lectin-like domain (CTD):** This globular domain contains a ConA-like lectin fold (IPR013320) and participates in cell-matrix interactions. The CTD forms a β-sandwich structure and contains four strictly conserved calcium-binding sites.

The trimeric assembly of the C-terminal region is necessary for cell spreading and fascin spike organization, indicating that proper oligomerization is essential for biological activity [kvansakul-2004-tsp1-structure-abstract].

## 3. Molecular Functions and Receptor Interactions

### 3.1 Regulation of Matrix Metalloproteinase-2 (MMP2)

One of the most well-characterized molecular functions of TSP2 is its regulation of MMP2 levels in the extracellular environment. TSP2 physically interacts with MMP2 through its type 1 repeats (TSRs), which bind to the gelatin-binding domain of MMP2 [bein-2000-tsp-mmp2-interaction-abstract]. This interaction does not directly inhibit MMP2 enzymatic activity; rather, TSP2 facilitates the clearance of MMP2 from the extracellular space through receptor-mediated endocytosis.

The mechanism of MMP2 clearance involves the low-density lipoprotein receptor-related protein (LRP), a scavenger receptor that mediates the internalization of TSP2 [yang-2001-lrp-mmp2-clearance-abstract]. TSP2 forms a complex with MMP2, and this complex is internalized via LRP, effectively reducing extracellular MMP2 levels. In TSP2-null mice, this clearance mechanism is disrupted, leading to a two-fold increase in extracellular MMP2 levels. The elevated MMP2 contributes to several phenotypes observed in TSP2-null mice, including abnormal collagen fibrillogenesis, altered cell adhesion, and increased angiogenesis [yang-2000-mmp2-adhesion-abstract].

### 3.2 CD36-Mediated Antiangiogenic Activity

TSP2 is a potent endogenous inhibitor of angiogenesis, exerting its effects primarily through the scavenger receptor CD36 [simantov-2005-cd36-antiangiogenic-abstract]. Using the corneal pocket assay, researchers demonstrated that TSP-2 did not inhibit bFGF-induced angiogenesis in CD36-null mice, confirming the essential role of CD36 in mediating TSP2's antiangiogenic activity. TSP2 binds to CD36 through the amino acid region 93-120, the same region that mediates TSP1 binding.

The TSP2-CD36 interaction triggers intracellular signaling cascades that result in inhibition of endothelial cell migration, proliferation, and survival, while promoting apoptosis [lawler-2012-angiogenesis-regulation-abstract]. CD36 and β1 integrins collaborate to transmit these signals, and these receptors appear to associate with VEGFR2 to form a platform for integration of positive and negative signals for angiogenesis. Histidine-rich glycoprotein (HRGP) can act as a "decoy" receptor that binds TSP2 with high affinity and blocks its antiangiogenic activity, suggesting a physiological mechanism for modulating TSP2 function [simantov-2005-cd36-antiangiogenic-abstract].

### 3.3 FGF2 Binding and Sequestration

Recent studies have identified fibroblast growth factor 2 (FGF2) as an important binding partner for TSP2 [rusnati-2018-fgf2-binding-abstract]. TSP2 binds FGF2 with high affinity (Kd = 1.3 nM) through its calcium-binding type III repeats domain. The minimal FGF2-binding sequence was identified as the GVTDEKD peptide in repeat 3C. This interaction is inhibited by calcium and heparin.

The functional consequence of TSP2-FGF2 binding is impairment of FGF2's ability to interact with its cellular receptors, including heparan sulfate proteoglycans and FGFR-1. By sequestering FGF2, TSP2 reduces the bioavailability of this proangiogenic growth factor, contributing to TSP2's antiangiogenic properties. This mechanism is shared with TSP1, indicating conservation of this growth factor regulatory function within the subgroup A thrombospondins [rusnati-2018-fgf2-binding-abstract].

### 3.4 CD47 and Integrin Interactions

In addition to CD36, TSP2 interacts with CD47 (also known as integrin-associated protein) and various integrins [lawler-2012-angiogenesis-regulation-abstract]. CD47 is involved in the suppression of nitric oxide (NO) signaling, which contributes to the antiangiogenic and anti-inflammatory effects of TSP2. Both CD36 and CD47 are implicated in the suppression of NO, providing multiple mechanisms for TSP2 to modulate vascular function.

Integrins, particularly αvβ3 and β1 integrins, also serve as receptors for TSP2 effects on cell adhesion and migration [lawler-2012-angiogenesis-regulation-abstract]. Studies in pancreatic cancer have shown that THBS2 binds to integrin αvβ3/CD36 and activates the MAPK pathway in cancer cells [nan-2022-pdac-abstract from the search results].

## 4. Cellular Localization and Expression

### 4.1 Subcellular Localization

TSP2 is synthesized in the endoplasmic reticulum and secreted into the extracellular space. The protein contains a signal peptide at its N-terminus that directs it to the secretory pathway. Upon secretion, TSP2 is deposited in the extracellular matrix, where it exerts its matricellular functions. TSP2 does not become an integral structural component of the ECM but rather modulates cell-matrix interactions from its position in the pericellular environment [bornstein-2000-tsp2-matricellular-abstract].

### 4.2 Tissue Distribution

In normal adult tissues, TSP2 expression is relatively low but can be detected in various connective tissues. The synthesis of TSP2 occurs primarily in connective tissues during development and growth. In the adult, TSP2 expression is markedly induced in response to tissue injury, during wound healing, and in association with tumor growth [bornstein-2000-tsp2-matricellular-abstract].

Key sites of TSP2 expression include:

- **Skin and dermis:** Fibroblasts are the major cellular source of TSP2 in skin, and expression is upregulated during wound healing [kunkemoeller-2019-diabetic-wound-abstract]
- **Bone:** TSP2 is expressed by osteoblasts and their progenitors, with particularly high expression during skeletal development and fracture repair [delany-2009-bone-remodeling-abstract]
- **Cardiovascular system:** TSP2 is expressed in the myocardium and blood vessels, where it plays essential roles in maintaining matrix integrity [schroen-2004-cardiac-tsp2-abstract]
- **Eye:** TSP2 is expressed in various ocular tissues including the trabecular meshwork, where it may influence intraocular pressure regulation

The temporal expression pattern of TSP2 differs from that of TSP1. While TSP1 is often expressed early in response to injury and is present in platelets (providing an immediate source upon vascular damage), TSP2 expression typically peaks later during the repair process, coinciding with the remodeling phase of wound healing [bornstein-2000-tsp2-matricellular-abstract].

## 5. Biological Processes and Signaling Pathways

### 5.1 Extracellular Matrix Assembly and Collagen Fibrillogenesis

TSP2 plays a critical role in regulating ECM assembly and collagen fibrillogenesis without being an integral component of collagen fibrils [calabro-2014-tsp2-ecm-assembly-abstract]. TSP2-null mice display striking abnormalities in connective tissue architecture, including fragile skin, abnormally large collagen fibrils with irregular contours in skin and tendon, and laxity of ligaments [bornstein-2000-tsp2-matricellular-abstract].

Recent mechanistic studies have revealed that TSP2 influences collagen fibrillogenesis through regulation of lysyl oxidase (LOX), an enzyme essential for collagen cross-linking [calabro-2019-mir29-lox-abstract]. TSP2 knockout mice show decreased LOX levels in skin, which manifests as increased fibrillar collagen solubility and decreased levels of LOX-mediated cross-linking. These changes are mediated indirectly through miR-29, a major regulator of ECM proteins and LOX, as miR-29 expression is increased in TSP2-null tissues. Thus, TSP2 contributes to ECM production and assembly by suppressing miR-29 and maintaining adequate LOX levels.

In bone, TSP2 deficiency leads to a brittle bone phenotype characterized by altered collagen fibril morphology and increased detergent-extractable type I collagen [manley-2015-bone-collagen-abstract]. Transmission electron microscopy revealed less intensely stained collagen fibrils with altered morphology in TSP2-null bone, indicating that TSP2 is required for optimal collagen fibrillogenesis in skeletal tissue.

### 5.2 Wound Healing and Tissue Repair

TSP2 is a critical regulator of the wound healing response. Paradoxically, TSP2-null mice exhibit accelerated wound healing with minimal scarring, suggesting that under normal conditions TSP2 functions to modulate and potentially restrain the healing process [kyriakides-2001-sponge-granuloma-abstract]. TSP2-null wounds show increased angiogenesis, enhanced granulation tissue formation, and altered extracellular matrix remodeling.

The accelerated healing in TSP2-null mice is associated with elevated levels of MMP-2, MMP-9, and soluble VEGF in wounds [maclauchlan-2009-wound-healing-abstract]. However, TSP2-null wound fibroblasts show reduced ability to contract collagen gels, indicating complex effects on wound contracture. The phenotype of TSP2-null mice in wound healing contrasts with that of TSP1-null mice, which show delayed healing with prolonged inflammation [agah-2002-double-null-abstract from search results].

In pathological conditions such as diabetes, elevated TSP2 expression contributes to impaired wound healing. Hyperglycemia increases TSP2 expression in fibroblasts through activation of the hexosamine pathway and NF-κB signaling [kunkemoeller-2019-diabetic-wound-abstract]. Diabetic TSP2-deficient mice exhibit improved healing compared to diabetic control mice, characterized by accelerated re-epithelialization and increased blood vessel maturation, suggesting that targeting TSP2 may be a therapeutic strategy for diabetic wound management.

### 5.3 Angiogenesis Regulation

TSP2 is one of the most potent endogenous inhibitors of angiogenesis identified to date. The antiangiogenic activity of TSP2 involves multiple mechanisms [lawler-2012-angiogenesis-regulation-abstract]:

1. **Direct effects on endothelial cells:** TSP2 inhibits endothelial cell migration, proliferation, and survival while promoting apoptosis through CD36 and CD47 signaling
2. **VEGF antagonism:** TSP2 antagonizes VEGF activity, in part through receptor cross-talk at the plasma membrane
3. **FGF2 sequestration:** TSP2 binds and sequesters FGF2, reducing its bioavailability for proangiogenic signaling
4. **MMP regulation:** By facilitating MMP2 clearance, TSP2 limits matrix degradation necessary for endothelial cell migration and vessel sprouting

These antiangiogenic properties have been exploited in tumor models, where TSP2 overexpression suppresses tumor growth through inhibition of tumor angiogenesis [de-fraipont-2001-tsp-angiogenesis from search results].

### 5.4 Bone Formation and Remodeling

TSP2 plays important roles in skeletal development and bone remodeling. TSP2-null mice have higher cortical bone volume and increased endosteal bone growth, attributed to expansion of the osteoblast progenitor cell pool [delany-2009-bone-remodeling-abstract]. However, these progenitors display deficits in osteoblastic differentiation potential, with delayed formation of mineralized matrix in vitro.

TSP2 influences the proportion of cartilage and bone during fracture healing [taylor-2009-fracture-healing-abstract]. TSP2-null mice show 30% more bone and 40% less cartilage by 10 days post-fracture compared to wild-type controls. This phenotype is attributed to increased vascularization in TSP2-null fracture calluses, which increases tissue oxygenation and shifts mesenchymal cell fate toward osteoblastic rather than chondrocytic differentiation. TSP2-null mice are also resistant to bone loss associated with ovariectomy, suggesting a role in estrogen-dependent bone regulation [hankenson-2010-bone-regulation-abstract].

### 5.5 Cardiovascular Function

TSP2 is essential for maintaining the structural integrity of the cardiac matrix [schroen-2004-cardiac-tsp2-abstract]. In a seminal study, researchers found that TSP2 expression was selectively elevated in hypertrophied hearts that were prone to progress to heart failure. Angiotensin II treatment induced fatal cardiac rupture in 70% of TSP2-null mice, while surviving animals developed heart failure—phenotypes not observed in wild-type mice. This dramatic finding demonstrates that TSP2 is necessary for the myocardium to cope with increased mechanical loading.

The protective function of TSP2 in the heart is attributed to its regulation of MMP activity. TSP2-null hearts showed markedly elevated MMP-2 and MMP-9 activity following angiotensin II treatment, leading to excessive matrix degradation and loss of structural integrity. Thus, TSP2 serves as a crucial regulator of the balance between matrix synthesis and degradation in the stressed myocardium [schroen-2004-cardiac-tsp2-abstract].

## 6. Role in Disease

### 6.1 Cancer

TSP2 has been implicated in various cancers with context-dependent effects. In many solid tumors, TSP2 expression correlates with reduced angiogenesis and improved prognosis due to its antiangiogenic properties. However, in some cancer types, elevated TSP2 expression is associated with poor outcomes.

In gastric cancer, THBS2 is overexpressed in cancer-associated fibroblasts (CAFs) and contributes to immune checkpoint blockade resistance through promotion of immunosuppressive tumor microenvironment features [li-2024-gastric-cancer-abstract from search results]. THBS2+ matrix CAFs facilitate recruitment of tissue-resident macrophages and their transformation into SPP1+ tumor-associated macrophages via the complement C3-C3AR1 axis.

In colorectal cancer, the lncRNA RP11-417E7.1 promotes metastasis by activating THBS2 transcription, which then activates the Wnt/β-catenin pathway and facilitates M2 macrophage polarization [liu-2024-crc-abstract from search results].

TSP2 has shown potential as a diagnostic biomarker, particularly in pancreatic ductal adenocarcinoma (PDAC) where elevated serum TSP2 levels correlate with tumor progression [nan-2022-pdac-abstract from search results].

### 6.2 Diabetic Complications

As discussed above, elevated TSP2 expression in diabetes contributes to impaired wound healing. TSP2 expression is increased in diabetic mice and in skin from patients with diabetes [kunkemoeller-2019-diabetic-wound-abstract]. Therapeutic strategies aimed at reducing TSP2 levels may improve wound healing outcomes in diabetic patients.

### 6.3 Cardiovascular Disease

TSP2 has been identified as a potential biomarker for heart failure risk. Elevated plasma TSP2 levels predict incident heart failure and are associated with echocardiographic traits indicative of cardiac remodeling [nayor-2020-biomarkers-abstract from search results]. The essential role of TSP2 in maintaining cardiac matrix integrity makes it a potential therapeutic target for preventing adverse cardiac remodeling.

## 7. Open Questions

Despite significant progress in understanding TSP2 function, several important questions remain:

1. **Tissue-specific regulation of TSP2 expression:** While TSP2 is induced in response to injury, the specific transcription factors and signaling pathways that control TSP2 expression in different tissues remain incompletely characterized. The regulation of TSP2 expression differs substantially from TSP1, reflecting distinct promoter sequences, but the functional significance of these differences requires further investigation.

2. **Relative contributions of different TSP2 domains:** TSP2 contains multiple functional domains that interact with different binding partners. The relative importance of each domain for specific biological functions, and whether there is crosstalk between domains, is not fully understood.

3. **TSP2 and TGF-β:** Unlike TSP1, TSP2 lacks the ability to activate latent TGF-β and may even competitively inhibit TSP1-mediated TGF-β activation. The consequences of this differential activity for tissue homeostasis and disease remain to be fully elucidated.

4. **Cell type-specific effects:** TSP2 affects multiple cell types including fibroblasts, endothelial cells, and osteoblasts. Understanding how TSP2 exerts different effects on different cell types will be important for developing targeted therapeutic interventions.

5. **Therapeutic applications:** Given its roles in angiogenesis, wound healing, and matrix remodeling, TSP2 or TSP2-derived peptides have therapeutic potential. However, the dual effects of TSP2 in different contexts (e.g., beneficial antiangiogenic effects in tumors but potentially detrimental effects in diabetic wound healing) present challenges for therapeutic development.

6. **Relationship with aging:** TSP2 levels increase in aged tissues, but the consequences of this increased expression for age-related tissue dysfunction require further investigation [agah-2004-aging-abstract from search results].

7. **Signaling pathway integration:** How TSP2-initiated signals integrate with other signaling pathways, particularly those controlling ECM homeostasis and angiogenesis, remains an active area of investigation.

## 8. References

1. **bornstein-2000-tsp2-matricellular:** Bornstein P, Armstrong LC, Hankenson KD, Kyriakides TR, Yang Z. Thrombospondin 2, a matricellular protein with diverse functions. Matrix Biol. 2000 Dec;19(7):557-68. DOI: https://doi.org/10.1016/s0945-053x(00)00104-9 PMID: 11102746

2. **calabro-2014-tsp2-ecm-assembly:** Calabro NE, Kristofik NJ, Kyriakides TR. Thrombospondin-2 and extracellular matrix assembly. Biochim Biophys Acta. 2014 Aug;1840(8):2396-402. DOI: https://doi.org/10.1016/j.bbagen.2014.01.013 PMID: 24440155 PMCID: PMC4074560

3. **lawler-2012-angiogenesis-regulation:** Lawler PR, Lawler J. Molecular basis for the regulation of angiogenesis by thrombospondin-1 and -2. Cold Spring Harb Perspect Med. 2012 May;2(5):a006627. DOI: https://doi.org/10.1101/cshperspect.a006627 PMID: 22553494 PMCID: PMC3331684

4. **yang-2000-mmp2-adhesion:** Yang Z, Kyriakides TR, Bornstein P. Matricellular proteins as modulators of cell-matrix interactions: adhesive defect in thrombospondin 2-null fibroblasts is a consequence of increased levels of matrix metalloproteinase-2. Mol Biol Cell. 2000 Oct;11(10):3353-64. DOI: https://doi.org/10.1091/mbc.11.10.3353 PMID: 11029041 PMCID: PMC14997

5. **simantov-2005-cd36-antiangiogenic:** Simantov R, Febbraio M, Silverstein RL. The antiangiogenic effect of thrombospondin-2 is mediated by CD36 and modulated by histidine-rich glycoprotein. Matrix Biol. 2005 Jan;24(1):27-34. DOI: https://doi.org/10.1016/j.matbio.2004.11.005 PMID: 15748999

6. **bein-2000-tsp-mmp2-interaction:** Bein K, Simons M. Thrombospondin type 1 repeats interact with matrix metalloproteinase 2. Regulation of metalloproteinase activity. J Biol Chem. 2000 Oct 13;275(41):32167-73. DOI: https://doi.org/10.1074/jbc.M003834200 PMID: 10900205

7. **yang-2001-lrp-mmp2-clearance:** Yang Z, Strickland DK, Bornstein P. Extracellular matrix metalloproteinase 2 levels are regulated by the low density lipoprotein-related scavenger receptor and thrombospondin 2. J Biol Chem. 2001 Mar 16;276(11):8403-8. DOI: https://doi.org/10.1074/jbc.M008925200 PMID: 11113133

8. **schroen-2004-cardiac-tsp2:** Schroen B, Heymans S, Sharma U, et al. Thrombospondin-2 is essential for myocardial matrix integrity: increased expression identifies failure-prone cardiac hypertrophy. Circ Res. 2004 Aug 20;95(5):515-22. DOI: https://doi.org/10.1161/01.RES.0000141019.20332.3e PMID: 15284191

9. **rusnati-2018-fgf2-binding:** Rusnati M, Borsotti P, Moroni E, et al. The calcium-binding type III repeats domain of thrombospondin-2 binds to fibroblast growth factor 2 (FGF2). Angiogenesis. 2019 Feb;22(1):133-144. DOI: https://doi.org/10.1007/s10456-018-9644-3 PMID: 30168023

10. **calabro-2019-mir29-lox:** Calabro NE, Barrett A, Chamorro-Jorganes A, et al. Thrombospondin-2 regulates extracellular matrix production, LOX levels, and cross-linking via downregulation of miR-29. Matrix Biol. 2019 Sep;82:71-85. DOI: https://doi.org/10.1016/j.matbio.2019.03.002 PMID: 30876926 PMCID: PMC6710120

11. **kunkemoeller-2019-diabetic-wound:** Kunkemoeller B, Bancroft T, Xing H, et al. Elevated Thrombospondin 2 Contributes to Delayed Wound Healing in Diabetes. Diabetes. 2019 Oct;68(10):2016-2023. DOI: https://doi.org/10.2337/db18-1001 PMID: 31391172 PMCID: PMC6754242

12. **kvansakul-2004-tsp1-structure:** Kvansakul M, Adams JC, Hohenester E. Structure of a thrombospondin C-terminal fragment reveals a novel calcium core in the type 3 repeats. EMBO J. 2004 Mar 24;23(6):1223-33. DOI: https://doi.org/10.1038/sj.emboj.7600166 PMID: 15014436 PMCID: PMC381422

13. **taylor-2009-fracture-healing:** Taylor DK, Meganck JA, Terkhorn S, et al. Thrombospondin-2 influences the proportion of cartilage and bone during fracture healing. J Bone Miner Res. 2009 Jun;24(6):1043-54. DOI: https://doi.org/10.1359/jbmr.090101 PMID: 19123916 PMCID: PMC3276350

14. **delany-2009-bone-remodeling:** Delany AM, Hankenson KD. Thrombospondin-2 and SPARC/osteonectin are critical regulators of bone remodeling. J Cell Commun Signal. 2009 Dec;3(3-4):227-38. DOI: https://doi.org/10.1007/s12079-009-0076-0 PMID: 19862642 PMCID: PMC2778593

15. **hankenson-2010-bone-regulation:** Hankenson KD, Sweetwyne MT, Shitaye H, Posey KL. Thrombospondins and novel TSR-containing proteins, R-spondins, regulate bone formation and remodeling. Curr Osteoporos Rep. 2010 Jun;8(2):68-76. DOI: https://doi.org/10.1007/s11914-010-0017-0 PMID: 20425613

16. **kyriakides-2001-sponge-granuloma:** Kyriakides TR, Zhu YH, Yang Z, Huynh G, Bornstein P. Altered extracellular matrix remodeling and angiogenesis in sponge granulomas of thrombospondin 2-null mice. Am J Pathol. 2001 Oct;159(4):1255-62. DOI: https://doi.org/10.1016/S0002-9440(10)62512-6 PMID: 11583953 PMCID: PMC1850515

17. **maclauchlan-2009-wound-healing:** Maclauchlan S, Skokos EA, Agah A, et al. Enhanced angiogenesis and reduced contraction in thrombospondin-2-null wounds is associated with increased levels of matrix metalloproteinases-2 and -9, and soluble VEGF. J Histochem Cytochem. 2009 Apr;57(4):301-13. DOI: https://doi.org/10.1369/jhc.2008.952689 PMID: 19029404 PMCID: PMC2664984

18. **manley-2015-bone-collagen:** Manley E, Perosky JE, Khoury BM, Reddy AB, Kozloff KM, Alford AI. Thrombospondin-2 deficiency in growing mice alters bone collagen ultrastructure and leads to a brittle bone phenotype. J Appl Physiol. 2015 Oct 15;119(8):872-81. DOI: https://doi.org/10.1152/japplphysiol.00340.2015 PMID: 26272319 PMCID: PMC4610004

19. **zhang-2020-cardiovascular:** Zhang K, Li M, Yin L, Fu G, Liu Z. Role of thrombospondin-1 and thrombospondin-2 in cardiovascular diseases (Review). Int J Mol Med. 2020 May;45(5):1275-1293. DOI: https://doi.org/10.3892/ijmm.2020.4507 PMID: 32323748 PMCID: PMC7138268

20. **bornstein-2004-injury-response:** Bornstein P, Agah A, Kyriakides TR. The role of thrombospondins 1 and 2 in the regulation of cell-matrix interactions, collagen fibril formation, and the response to injury. Int J Biochem Cell Biol. 2004 Jun;36(6):1115-25. DOI: https://doi.org/10.1016/j.biocel.2004.01.012 PMID: 15094126


## Citations

1. bein-2000-tsp-mmp2-interaction-abstract.md
2. bornstein-2000-tsp2-matricellular-abstract.md
3. calabro-2014-tsp2-ecm-assembly-abstract.md
4. calabro-2019-mir29-lox-abstract.md
5. delany-2009-bone-remodeling-abstract.md
6. hankenson-2010-bone-regulation-abstract.md
7. kunkemoeller-2019-diabetic-wound-abstract.md
8. kvansakul-2004-tsp1-structure-abstract.md
9. kyriakides-2001-sponge-granuloma-abstract.md
10. lawler-2012-angiogenesis-regulation-abstract.md
11. maclauchlan-2009-wound-healing-abstract.md
12. manley-2015-bone-collagen-abstract.md
13. rusnati-2018-fgf2-binding-abstract.md
14. schroen-2004-cardiac-tsp2-abstract.md
15. simantov-2005-cd36-antiangiogenic-abstract.md
16. taylor-2009-fracture-healing-abstract.md
17. yang-2000-mmp2-adhesion-abstract.md
18. yang-2001-lrp-mmp2-clearance-abstract.md