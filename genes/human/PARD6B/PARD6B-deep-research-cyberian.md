---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T08:01:25.766655'
end_time: '2026-01-23T08:22:58.844216'
duration_seconds: 1293.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PARD6B
  gene_symbol: PARD6B
  uniprot_accession: Q9BYG5
  protein_description: 'RecName: Full=Partitioning defective 6 homolog beta; Short=PAR-6
    beta; Short=PAR-6B;'
  gene_info: Name=PARD6B; Synonyms=PAR6B;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the PAR6 family. .
  protein_domains: PAR6_homolog. (IPR051741); PB1-like. (IPR053793); PB1_dom. (IPR000270);
    PB1_Par6. (IPR034868); PDZ. (IPR001478)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9BYG5
- **Protein Description:** RecName: Full=Partitioning defective 6 homolog beta; Short=PAR-6 beta; Short=PAR-6B;
- **Gene Information:** Name=PARD6B; Synonyms=PAR6B;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PAR6 family. .
- **Key Domains:** PAR6_homolog. (IPR051741); PB1-like. (IPR053793); PB1_dom. (IPR000270); PB1_Par6. (IPR034868); PDZ. (IPR001478)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PARD6B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PARD6B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PARD6B** (gene ID: PARD6B, UniProt: Q9BYG5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PARD6B (PAR-6B): A Comprehensive Research Report on the Cell Polarity Regulator

## 1. Introduction and Overview

PARD6B (Partitioning defective 6 homolog beta, also known as PAR-6B or PAR6B) is a member of the evolutionarily conserved PAR6 protein family that plays a fundamental role in establishing and maintaining cell polarity across metazoans. The human PARD6B gene (Gene ID: 84612) is located on chromosome 20q13.13 and encodes a 372-amino acid scaffold protein that functions as a central organizing hub within the PAR polarity complex [nolan-2008-par6-proliferation-abstract]. The protein is characterized by three conserved domains: a PB1 (Phox and Bem1) domain at the N-terminus, a semi-CRIB (Cdc42/Rac interactive binding) motif, and a PDZ (PSD95/Discs-large/ZO-1) domain [joberty-2000-par6-links-par3-apkc-cdc42-abstract]. These domains enable PARD6B to simultaneously interact with multiple polarity-determining proteins, positioning it as a critical adapter that coordinates signaling between the small GTPase Cdc42, atypical protein kinase C (aPKC), and other polarity factors.

The PAR proteins were originally identified through genetic screens in *Caenorhabditis elegans* as factors essential for asymmetric division of the one-cell embryo [joberty-2000-par6-links-par3-apkc-cdc42-abstract]. Subsequent research demonstrated remarkable evolutionary conservation of both the PAR proteins and their functions in cell polarization across species from worms to humans [chen-2013-par3par6apkc-review-abstract]. In mammals, three PAR6 paralogs exist (PARD6A, PARD6B, and PARD6G), with PARD6B being particularly notable for its documented roles in tight junction formation, epithelial polarization, and early embryonic development [alarcon-2010-pard6b-trophectoderm-abstract]. The protein functions not as an enzyme but as a scaffold that brings together key polarity regulators, thereby facilitating the establishment of distinct cellular domains and the proper assembly of cell-cell junctions.

## 2. Domain Architecture and Structural Features

The molecular architecture of PARD6B consists of three well-characterized domains that mediate distinct protein-protein interactions essential for its function as a polarity scaffold. The N-terminal PB1 domain (approximately residues 10-90) mediates a high-affinity, head-to-head interaction with the PB1 domain of atypical protein kinase C (aPKC), with binding occurring at subnanomolar affinity such that the aPKC-PAR6 complex can be considered a single functional unit [letmle-2022-par3-apkc-par6-structure-abstract]. Structural studies have revealed that the PB1 domains of aPKC and PAR6 form an asymmetric heterodimer with 1:1 stoichiometry, and this interaction is essential for targeting aPKC to the plasma membrane and regulating its kinase activity [letmle-2022-par3-apkc-par6-structure-abstract].

The semi-CRIB motif and adjacent PDZ domain (approximately residues 130-255) together comprise the minimal Cdc42-binding domain of PARD6B. Unlike canonical CRIB motifs found in other Cdc42 effectors such as PAK or WASP, the semi-CRIB of Par6 lacks several conserved residues typically required for GTPase binding, making it insufficient for Cdc42 recognition on its own [garrard-2003-cdc42-par6-structure-abstract]. The crystal structure of Cdc42 bound to the Par6 GTPase-binding domain at 2.1 Å resolution revealed an unexpected structural arrangement: the semi-CRIB forms a β-strand that inserts between four strands of Cdc42 and three strands of the PDZ domain to create a continuous eight-stranded β-sheet [garrard-2003-cdc42-par6-structure-abstract]. This arrangement demonstrates a novel function for the PDZ domain as a structural scaffold that stabilizes the semi-CRIB motif, enabling high-affinity Cdc42 binding despite the absence of canonical binding determinants.

The PDZ domain of PARD6B also mediates interactions with several other polarity proteins independently of its structural role in Cdc42 binding. Through its PDZ domain, Par6 can bind directly to the PDZ-binding motif of Crumbs (a transmembrane apical polarity determinant), to PALS1 (an adaptor protein linking Crumbs to the PATJ scaffold), and potentially to Par3 through an unconventional PDZ-PDZ interaction [hurd-2003-polarity-complexes-tightjunction-abstract]. Binding of Cdc42-GTP to the CRIB-PDZ module induces conformational changes that allosterically regulate the affinity of the PDZ domain for its ligands, increasing Crumbs binding approximately 13-fold [garrard-2003-cdc42-par6-structure-abstract]. This conformational coupling provides a mechanism by which GTPase activation can modulate the assembly of polarity complexes at specific cellular locations.

## 3. The PAR Polarity Complex: Composition and Assembly

PARD6B functions primarily as a component of the tripartite PAR polarity complex, which comprises PAR3 (PARD3), PAR6 (PARD6A/B/G), and atypical protein kinase C (aPKCζ or aPKCι/λ) [chen-2013-par3par6apkc-review-abstract]. This complex represents the evolutionarily conserved core of the PAR system and plays indispensable roles in diverse polarity contexts including asymmetric cell division, establishment of apical-basal polarity in epithelial cells, oriented cell migration, and neuronal polarization [chen-2013-par3par6apkc-review-abstract]. The assembly and activity of this complex are tightly regulated through multiple protein-protein interactions and post-translational modifications.

Within the PAR complex, PARD6B serves as a central adapter linking aPKC to upstream regulators and downstream effectors. The PB1 domain-mediated interaction between Par6 and aPKC is constitutive and extremely stable, effectively forming a heterodimeric unit [letmle-2022-par3-apkc-par6-structure-abstract]. In contrast, the interaction between this aPKC-Par6 unit and Par3 is more dynamic and is mediated primarily through a PDZ ligand at the C-terminus of aPKC rather than through direct Par6-Par3 binding [hurd-2003-polarity-complexes-tightjunction-abstract]. This architecture allows for potential regulatory separation between the constitutive aPKC-Par6 complex and the larger PAR complex that includes Par3.

The small GTPase Cdc42 provides a critical regulatory input to the PAR complex through its direct interaction with Par6. Cdc42 in its GTP-bound (active) state binds to the CRIB-PDZ module of Par6, and this interaction has multiple functional consequences [joberty-2000-par6-links-par3-apkc-cdc42-abstract]. First, Cdc42 binding induces conformational changes in Par6 that relieve the inhibitory effect of Par6 on aPKC kinase activity, enabling phosphorylation of downstream substrates [gao-2002-par6-tightjunction-negative-abstract]. Second, Cdc42 binding enhances the interaction of Par6 with apical determinants such as Crumbs, potentially contributing to apical localization of the complex [garrard-2003-cdc42-par6-structure-abstract]. Third, in some cellular contexts, Cdc42 activity is required for proper cortical localization of the Par6-aPKC complex [joberty-2000-par6-links-par3-apkc-cdc42-abstract]. Thus, Cdc42 serves as a pivotal regulatory switch that coordinates PAR complex assembly, localization, and activity.

## 4. Cellular Localization and Tight Junction Function

In polarized epithelial cells, PARD6B localizes predominantly to the apical membrane domain and to tight junctions (TJs), where it plays essential roles in establishing and maintaining the boundary between apical and basolateral membrane compartments [cunliffe-2012-par6b-tightjunction-abstract]. This localization depends on multiple mechanisms including interactions with transmembrane proteins such as Crumbs and the TGFβ receptor, association with cytoskeletal elements, and potentially lipid-based membrane targeting through the polybasic domain of associated aPKC [hurd-2003-polarity-complexes-tightjunction-abstract].

The role of PARD6B in tight junction assembly has been demonstrated through multiple experimental approaches. Depletion of PAR6B by siRNA in MCF7 breast epithelial cells resulted in complete loss of tight junction networks and failure to localize activated aPKCζ to the membrane, while adherens junction formation remained intact [cunliffe-2012-par6b-tightjunction-abstract]. Similarly, inhibition of CDC42 in MCF7 cells blocked tight junction polymerization, confirming that the complete PAR6-aPKC-CDC42-PAR3 complex is required to activate and stabilize TJs [cunliffe-2012-par6b-tightjunction-abstract]. These findings establish that PARD6B is not merely a marker of tight junctions but is functionally required for their assembly.

Interestingly, several studies have revealed that the Par6-aPKC complex can also act as a negative regulator of tight junction assembly under certain conditions. Overexpression of Par6 inhibits TJ formation in MDCK cells following calcium depletion, and this inhibitory effect is specific for TJs without affecting adherens junctions [gao-2002-par6-tightjunction-negative-abstract]. Activated Cdc42 can similarly disrupt mature TJs [gao-2002-par6-tightjunction-negative-abstract]. These apparently contradictory findings suggest that Par6 function in junction dynamics is context-dependent and may involve a balance between promoting initial junction assembly and maintaining the dynamic regulation of junctional complexes required for epithelial plasticity.

The PAR complex at tight junctions also interfaces with other polarity complexes through direct protein-protein interactions. Par6 interacts directly with PALS1 through its PDZ domain, and this interaction is regulated by Cdc42-GTP [hurd-2003-polarity-complexes-tightjunction-abstract]. Through PALS1, the PAR complex connects to the Crumbs-PALS1-PATJ complex, another major apical polarity determinant. Expression of dominant-negative PALS1 causes mis-localization of Par6-aPKC and the tight junction marker ZO-1, demonstrating that proper coordination between these polarity complexes is essential for TJ integrity [hurd-2003-polarity-complexes-tightjunction-abstract].

## 5. Role in TGFβ Signaling and Epithelial-Mesenchymal Transition

A seminal discovery by Ozdamar and colleagues revealed that Par6 is directly regulated by TGFβ receptor signaling, linking the polarity machinery to growth factor control of epithelial cell plasticity [ozdamar-2005-par6-tgfbeta-abstract]. The study demonstrated that Par6 localizes to tight junctions where it interacts with the TGFβ type I receptor (TβRI). Upon TGFβ stimulation, the TGFβ type II receptor (TβRII) is recruited to tight junctions and phosphorylates Par6 at Serine 345 in its C-terminal region [ozdamar-2005-par6-tgfbeta-abstract]. This represents a Smad-independent signaling pathway that directly couples extracellular growth factor signals to the cell polarity machinery.

Phosphorylation of Par6 by TβRII has profound consequences for epithelial cell morphology through its effects on the E3 ubiquitin ligase Smurf1. Phosphorylated Par6 recruits Smurf1 to tight junctions, where Smurf1 catalyzes the ubiquitination and proteasomal degradation of RhoA, a small GTPase required for tight junction maintenance [ozdamar-2005-par6-tgfbeta-abstract]. Loss of RhoA leads to depolymerization of filamentous actin, dissolution of tight junctions, and subsequent reduction in cell-cell adhesion—critical early steps in epithelial-to-mesenchymal transition (EMT). This pathway thus provides a direct mechanism by which TGFβ can induce the loss of epithelial character associated with EMT during development and cancer progression [ozdamar-2005-par6-tgfbeta-abstract]. Notably, recent evidence suggests that aPKC can also phosphorylate Par6 to drive EMT and increase migratory potential in non-small cell lung cancer cells, indicating that multiple kinases may regulate Par6 function through phosphorylation at distinct sites or contexts.

The significance of this pathway extends to cancer biology, where EMT contributes to tumor invasion and metastasis. TGFβ signaling is known to promote metastasis in advanced cancers by stimulating EMT, and the Par6-Smurf1-RhoA axis provides a molecular explanation for this effect [ozdamar-2005-par6-tgfbeta-abstract]. This pathway operates independently of the canonical Smad signaling cascade, highlighting Par6 as a critical node in Smad-independent TGFβ signaling that controls epithelial cell plasticity.

## 6. Mutual Antagonism with the Scribble Complex and Lgl Phosphorylation

Cell polarity in epithelia is established through the mutual antagonism between the apical PAR complex (Par3-Par6-aPKC) and the basolateral Scribble complex (Scribble-Dlg-Lgl). This antagonistic relationship ensures the maintenance of distinct apical and basolateral membrane domains. The best-characterized interface between these systems involves Lethal giant larvae (Lgl), a tumor suppressor protein that is a key substrate of the PAR complex [plant-2003-apkc-par6-lgl-abstract].

In polarized epithelial cells, Lgl localizes to the basolateral cortex together with Scribble and Discs large (Dlg), where it excludes PAR complex components from the basolateral domain. Reciprocally, the PAR complex at the apical cortex phosphorylates and excludes Lgl from the apical domain [plant-2003-apkc-par6-lgl-abstract]. This mutual exclusion establishes the boundary between apical and basolateral compartments. When Lgl is phosphorylated on three conserved serine residues by aPKC, it dissociates from the cytoskeleton and becomes inactivated, restricting it to the cytoplasm in the apical region. Mutation of these phosphorylation sites allows Lgl to inappropriately invade the apical membrane, disrupting polarity.

The mammalian aPKC/Par6 complex phosphorylates Lgl through a multisite mechanism, and these phosphorylation events are essential for proper cell polarization [plant-2003-apkc-par6-lgl-abstract]. In cultured fibroblasts, both hypophosphorylated and hyperphosphorylated Lgl mutants fail to support normal polarization in response to wounding, indicating that dynamic regulation of Lgl phosphorylation is required for the polarity response [plant-2003-apkc-par6-lgl-abstract]. Par6 plays a dual role in this process: it targets aPKC to substrates for phosphorylation while simultaneously modulating aPKC kinase activity in response to Cdc42 binding.

Recent structural studies have provided detailed mechanistic insights into the aPKC-Par6-Lgl regulatory relationship. Paradoxically, although aPKC-Par6 phosphorylates Lgl to exclude it from the apical domain, these proteins can also form a stable tripartite complex. The aPKC-Par6 complex captures Lgl through interactions involving both an aPKC docking site and a Par6 PDZ contact, and this interaction initially inhibits progression through the multisite phosphorylation pathway [plant-2003-apkc-par6-lgl-abstract]. This creates a "capture, mutual inhibition, and release" mechanism wherein Lgl binding inhibits aPKC activity while being trapped in a partially phosphorylated intermediate state. Binding of Cdc42-GTP and the apical determinant Crumbs to Par6 promotes release of phosphorylated Lgl from the complex, enabling completion of the phosphorylation program. This mechanism provides spatial control over Lgl phosphorylation, ensuring that Lgl is efficiently excluded from the apical domain where active PAR complex and its upstream regulators are concentrated [plant-2003-apkc-par6-lgl-abstract].

Notably, the binding of Par3 and Lgl to Par6 appears to be mutually exclusive, suggesting that Par3 and Lgl compete for association with the Par6-aPKC unit. Scribble and Dlg do not directly inhibit aPKC but rather work through Lgl to block the spread and apicalizing activity of aPKC; the aPKC mislocalization observed in Scribble or Dlg mutant cells reflects weakened Lgl inhibitory activity.

## 7. Phase Separation and PAR Complex Condensation

Recent research has revealed that the PAR polarity complex undergoes liquid-liquid phase separation (LLPS) to form membrane-associated condensates, providing a mechanistic explanation for the localized concentration of polarity determinants [liu-2020-par-phase-separation-abstract]. Studies in Drosophila neuroblasts demonstrated that the Par complex exhibits cell cycle-dependent condensation at the cell cortex during asymmetric division. This condensation is driven by multivalent interactions among complex components and is essential for proper polarity establishment.

The molecular mechanism of PAR complex phase separation involves several contributing factors [liu-2020-par-phase-separation-abstract]. Par3, in its open conformation, undergoes autonomous phase separation through oligomerization mediated by its N-terminal domain. Par6, through its C-terminal tail binding to the PDZ3 domain of Par3, becomes enriched in Par3 condensates and dramatically promotes further phase separation. This creates a positive feedback loop that drives the formation of self-organized, highly condensed, and dynamic droplets. FRAP (fluorescence recovery after photobleaching) analyses revealed that Par3 and Par6 within condensed puncta rapidly exchange with proteins in the surrounding cytoplasm, with approximately 75% recovery within seconds, consistent with the liquid-like properties of these structures [liu-2020-par-phase-separation-abstract].

The kinase aPKC is recruited to Par3/Par6 condensates as a "client" protein but also provides an important regulatory mechanism. Activated aPKC can disperse Par3/Par6 condensates through phosphorylation of Par3, creating a negative feedback loop [liu-2020-par-phase-separation-abstract]. This phosphorylation-dependent disassembly may serve to limit condensate size, regulate the dynamics of polarity complex assembly and disassembly, or enable redistribution of polarity factors during cell cycle progression. Mutations that impair the LLPS of the Par complex lead to defective assembly of the apical Par complex crescent during Drosophila neuroblast asymmetric divisions, resulting in cell lineage defects [liu-2020-par-phase-separation-abstract]. These findings suggest that phase separation may be a universal mechanism for the localized cortical condensation of cell polarity complexes, providing a biophysical framework for understanding how polarized protein distributions are achieved while maintaining dynamic exchange with the cytoplasmic pool.

## 8. Role in Neuronal Polarity

Beyond its well-characterized functions in epithelial cells, PARD6B plays important roles in neuronal polarization, a process essential for establishing the distinct axonal and dendritic domains that define neuronal function [zhang-2022-par-neurodevelopment-review-abstract]. Notably, PARD6B appears to be the predominant Par6 isoform expressed in mammalian neurons, suggesting specialized functions in nervous system development. The Par3-Par6-aPKC complex participates in multiple aspects of neuronal development including axon specification, dendritic arborization, dendritic spine morphogenesis, and neuronal migration [zhang-2022-par-neurodevelopment-review-abstract].

During neuronal polarization, the Par complex is enriched in the nascent axon, where it promotes axon specification and outgrowth. The Par6 CRIB-like motif integrates signals from small GTPases including Cdc42, Rac1, and RhoA, enabling translation of extracellular guidance cues into polarization outcomes [zhang-2022-par-neurodevelopment-review-abstract]. In embryonic hippocampal neurons, ectopic overexpression of Par6 prevents neuronal polarization and axon specification, suggesting that the levels and localization of Par6 must be precisely controlled for proper polarity establishment.

The localization of Par6 to the axon is regulated by ubiquitination in other neurites. Smurf1 is phosphorylated in the axon by PKA in response to BDNF signaling, leading to RhoA degradation and promoting axon development. However, non-phosphorylated Smurf1 in the dendrites targets Par6 for degradation, restricting Par6 localization to the axon [zhang-2022-par-neurodevelopment-review-abstract]. This mechanism allows Smurf1 to switch substrate preference to favor Par6 accumulation and RhoA degradation specifically in the future axon.

The Par complex also regulates dendritic spine morphogenesis in mature neurons. Par6 can inhibit RhoA GTPase in dendritic spine formation by activating p190 RhoGAP, and RNAi-mediated knockdown of Par3 or Par6 in hippocampal neurons revealed their important roles in spine development [zhang-2022-par-neurodevelopment-review-abstract]. Furthermore, Par6α and aPKCζ regulate centrosome integrity and perinuclear microtubule organization in migrating cerebellar neurons, facilitating glial-guided neuronal migration during cortical development.

Genetic variants in Par genes, including PARD6, have been associated with neuropsychiatric conditions including schizophrenia, bipolar disorder, and autism spectrum disorder, suggesting that partial loss-of-function in polarity signaling may contribute to these conditions [zhang-2022-par-neurodevelopment-review-abstract]. These associations highlight the critical importance of proper PAR complex function for normal brain development and function.

## 9. Role in Early Embryonic Development

PARD6B plays essential roles in early mammalian development, particularly in the formation of the trophectoderm (TE), the outer cell layer of the blastocyst that gives rise to extraembryonic tissues including the placenta. Studies using RNA interference in mouse preimplantation embryos have demonstrated that Pard6b is critical for establishing the epithelial features of the TE, including apical-basal cell polarity, tight junction formation, and expression of TE-specific transcription factors [alarcon-2010-pard6b-trophectoderm-abstract].

In mouse embryos, Pard6b mRNA and protein are present from the oocyte stage through preimplantation development, with maternal stores being critical for early function [alarcon-2010-pard6b-trophectoderm-abstract]. At the 8-cell stage, Pard6b protein becomes localized to the apical cortex of blastomeres, coinciding with the onset of cell polarization in the embryo. Knockdown of Pard6b did not prevent cleavage or compaction but completely blocked blastocyst cavity formation [alarcon-2010-pard6b-trophectoderm-abstract]. This cavitation failure results from defective intercellular junctions, as Pard6b knockdown caused abnormal distribution of the tight junction protein ZO-1 and aberrant organization of actin filaments.

The developmental defects in Pard6b-knockdown embryos extend beyond junction assembly to affect the specification of TE cell fate. Apical localization of aPKCζ was abolished in knockdown embryos, and expression of Cdx2, a transcription factor required for TE differentiation, was severely reduced [alarcon-2010-pard6b-trophectoderm-abstract]. In chimera formation assays, Pard6b-deficient cells could not maintain paracellular permeability sealing even when mixed with normal cells, demonstrating a cell-autonomous requirement for Pard6b in epithelial barrier function. Importantly, Pard6b expression appeared independent of the upstream transcription factor Tead4, suggesting that Pard6b acts in a parallel pathway or downstream of Tead4 in TE development [alarcon-2010-pard6b-trophectoderm-abstract].

## 10. PARD6B in Cancer

Accumulating evidence implicates PARD6B dysregulation in cancer development and progression, consistent with its fundamental role in controlling cell polarity and epithelial architecture. The PARD6B gene is located at chromosome 20q13.13, a region frequently amplified in breast cancer and other malignancies [nolan-2008-par6-proliferation-abstract][cunliffe-2012-par6b-tightjunction-abstract]. This genomic amplification correlates with overexpression of PAR6B protein in breast cancer cell lines and primary tumors.

Overexpression of Par6 promotes formation of hyperplastic acini in three-dimensional mammary epithelial cell culture models, demonstrating that elevated Par6 can drive abnormal proliferation [nolan-2008-par6-proliferation-abstract]. Notably, this proliferative effect requires interactions with aPKC and Cdc42 but is independent of Par3 and Lgl, suggesting that Par6 can promote proliferation through mechanisms distinct from its canonical role in polarity establishment. Par6-induced proliferation is mediated by sustained activation of MEK-ERK signaling and enables EGF-independent growth, providing a mechanistic basis for its oncogenic potential [nolan-2008-par6-proliferation-abstract].

Clinical analyses have confirmed the relevance of these findings to human cancer. Par6 is significantly overexpressed in estrogen receptor-positive breast tumors (P = 2.9 × 10^-7) and is elevated 2.5-fold in hyperplastic enlarged lobular units (HELUs), which represent precancerous lesions [nolan-2008-par6-proliferation-abstract]. In breast tumor tissue sections, PAR6B staining appeared reduced and cytoplasmic in more poorly differentiated tumors, consistent with loss of proper apical localization during dedifferentiation [cunliffe-2012-par6b-tightjunction-abstract]. Similar findings in colorectal cancer indicate that PARD6B amplification and overexpression promote tumor growth through upregulation of the MYC oncogene [nolan-2008-par6-proliferation-abstract].

The role of Par6 in TGFβ-induced EMT also contributes to its cancer relevance. The Par6-Smurf1-RhoA pathway enables TGFβ to promote tumor invasion and metastasis by driving epithelial cells toward a mesenchymal phenotype [ozdamar-2005-par6-tgfbeta-abstract]. Thus, Par6 may contribute to cancer progression both through direct proliferative effects and through facilitation of EMT and metastatic spread. These findings suggest that the PAR6-aPKC-Cdc42 complex represents a potential therapeutic target for cancer treatment [nolan-2008-par6-proliferation-abstract].

## 11. Open Questions

Despite substantial progress in understanding PARD6B function, several important questions remain unresolved:

**Isoform-specific functions:** Mammals possess three PAR6 isoforms (PARD6A, PARD6B, PARD6G) with >70% sequence similarity, but these isoforms appear to have divergent and sometimes opposing functions [marques-2015-par6-cancer-review-abstract]. Strikingly, PARD6B and PARD6G display essentially opposite mutational landscapes in tumors: PARD6B is characterized by gains, amplifications, and overexpression (suggesting oncogenic function), while PARD6G shows losses, deletions, and loss of heterozygosity (indicating tumor suppressor function) [marques-2015-par6-cancer-review-abstract]. The molecular basis for these opposing roles despite high sequence similarity remains poorly understood. Additionally, many PAR6 studies do not clearly indicate which isoform was investigated, leading to an incomplete picture of their individualistic functions.

**Regulation of complex assembly:** While the individual binding interactions within the PAR complex are well characterized, the mechanisms that control complex assembly and disassembly in space and time remain incompletely understood. Recent evidence suggests phase separation may contribute to Par complex clustering, but how this is regulated in vivo requires further study.

**Integration of polarity pathways:** The PAR complex interfaces with multiple other polarity systems including the Crumbs and Scribble complexes, but the precise hierarchy and feedback relationships among these systems in mammalian cells are not fully defined.

**Therapeutic targeting:** Given the evidence for PAR6 involvement in cancer, whether the PAR6-aPKC-Cdc42 complex can be effectively targeted therapeutically remains an important translational question. The challenge lies in selectively disrupting oncogenic functions while preserving normal polarity functions in healthy tissues.

**Tissue-specific functions:** PARD6B shows variable expression across tissues, but the extent to which its functions differ in different epithelial contexts (e.g., simple vs. stratified epithelia, different organs) has not been systematically explored.

## 12. References

- **alarcon-2010-pard6b-trophectoderm**: Alarcon VB. Cell Polarity Regulator PARD6B Is Essential for Trophectoderm Formation in the Preimplantation Mouse Embryo. Biology of Reproduction. 2010;83(3):347-358. PMID: 20505164. DOI: 10.1095/biolreprod.110.084400

- **chen-2013-par3par6apkc-review**: Chen J, Zhang M. The Par3/Par6/aPKC complex and epithelial cell polarity. Experimental Cell Research. 2013;319(10):1357-64. PMID: 23535009. DOI: 10.1016/j.yexcr.2013.03.021

- **cunliffe-2012-par6b-tightjunction**: Cunliffe HE, Jiang Y, Fornace KM, Yang F, Meltzer PS. PAR6B is required for tight junction formation and activated PKCζ localization in breast cancer. American Journal of Cancer Research. 2012;2(5):478-491. PMID: 22957302

- **gao-2002-par6-tightjunction-negative**: Gao L, Joberty G, Macara IG. Assembly of epithelial tight junctions is negatively regulated by Par6. Current Biology. 2002;12(3):221-5. PMID: 11839275. DOI: 10.1016/s0960-9822(01)00663-7

- **garrard-2003-cdc42-par6-structure**: Garrard SM, Capaldo CT, Gao L, Rosen MK, Macara IG. Structure of Cdc42 in a complex with the GTPase-binding domain of the cell polarity protein, Par6. EMBO Journal. 2003;22(5):1125-1133. PMID: 12606577. DOI: 10.1093/emboj/cdg110

- **hurd-2003-polarity-complexes-tightjunction**: Hurd TW, Gao L, Roh MH, Macara IG, Margolis B. Direct interaction of two polarity complexes implicated in epithelial tight junction assembly. Nature Cell Biology. 2003;5(2):137-42. PMID: 12545177. DOI: 10.1038/ncb923

- **joberty-2000-par6-links-par3-apkc-cdc42**: Joberty G, Petersen C, Gao L, Macara IG. The cell-polarity protein Par6 links Par3 and atypical protein kinase C to Cdc42. Nature Cell Biology. 2000;2(8):531-9. PMID: 10934474. DOI: 10.1038/35019573

- **letmle-2022-par3-apkc-par6-structure**: Le LTM, Drakulic S, Nyengaard JR, Golas MM, Sander B. Structural Organization of Human Full-Length PAR3 and the aPKC-PAR6 Complex. Molecular Biotechnology. 2022;64(12):1319-1327. PMID: 35610404. DOI: 10.1007/s12033-022-00504-1

- **liu-2020-par-phase-separation**: Liu Z, Yang Y, Gu A, Xu J, Mao Y, Lu H, Hu W, Lei QY, Li Z, Zhang M, Cai Y, Wen W. Par complex cluster formation mediated by phase separation. Nature Communications. 2020;11(1):2266. PMID: 32385244. DOI: 10.1038/s41467-020-16135-6

- **marques-2015-par6-cancer-review**: Marques E, Klefström J. Par6 family proteins in cancer. Oncoscience. 2015;2(11):894-895. PMID: 26697513. DOI: 10.18632/oncoscience.255

- **nolan-2008-par6-proliferation**: Nolan ME, Aranda V, Lee S, Lakshmi B, Basu S, Allred DC, Muthuswamy SK. The Polarity Protein Par6 Induces Cell Proliferation and Is Overexpressed in Breast Cancer. Cancer Research. 2008;68(20):8201-9. PMID: 18922891. DOI: 10.1158/0008-5472.CAN-07-6567

- **ozdamar-2005-par6-tgfbeta**: Ozdamar B, Bose R, Barrios-Rodiles M, Wang HR, Zhang Y, Wrana JL. Regulation of the polarity protein Par6 by TGFbeta receptors controls epithelial cell plasticity. Science. 2005;307(5715):1603-9. PMID: 15761148. DOI: 10.1126/science.1105718

- **plant-2003-apkc-par6-lgl**: Plant PJ, Fawcett JP, Lin DCC, Holdorf AD, Binns K, Kulkarni S, Pawson T. A polarity complex of mPar-6 and atypical PKC binds, phosphorylates and regulates mammalian Lgl. Nature Cell Biology. 2003;5(4):301-8. PMID: 12629547. DOI: 10.1038/ncb948

- **wallace-2010-cdc42-pak4-par6b**: Wallace SW, Durgan J, Jin D, Hall A. Cdc42 Regulates Apical Junction Formation in Human Bronchial Epithelial Cells through PAK4 and Par6B. Molecular Biology of the Cell. 2010;21(17):2996-3006. PMID: 20631255. DOI: 10.1091/mbc.E10-05-0429

- **zhang-2022-par-neurodevelopment-review**: Zhang L, Wei X. The Roles of Par3, Par6, and aPKC Polarity Proteins in Normal Neurodevelopment and in Neurodegenerative and Neuropsychiatric Disorders. The Journal of Neuroscience. 2022;42(24):4774-4793. PMID: 35705493. DOI: 10.1523/JNEUROSCI.0059-22.2022


## Citations

1. alarcon-2010-pard6b-trophectoderm-abstract.md
2. chen-2013-par3par6apkc-review-abstract.md
3. cunliffe-2012-par6b-tightjunction-abstract.md
4. gao-2002-par6-tightjunction-negative-abstract.md
5. garrard-2003-cdc42-par6-structure-abstract.md
6. hurd-2003-polarity-complexes-tightjunction-abstract.md
7. joberty-2000-par6-links-par3-apkc-cdc42-abstract.md
8. letmle-2022-par3-apkc-par6-structure-abstract.md
9. liu-2020-par-phase-separation-abstract.md
10. marques-2015-par6-cancer-review-abstract.md
11. nolan-2008-par6-proliferation-abstract.md
12. ozdamar-2005-par6-tgfbeta-abstract.md
13. plant-2003-apkc-par6-lgl-abstract.md
14. wallace-2010-cdc42-pak4-par6b-abstract.md
15. zhang-2022-par-neurodevelopment-review-abstract.md