---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T13:58:54.999490'
end_time: '2026-01-15T14:13:23.784749'
duration_seconds: 868.79
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AFAP1L1
  gene_symbol: AFAP1L1
  uniprot_accession: Q8TED9
  protein_description: 'RecName: Full=Actin filament-associated protein 1-like 1;
    Short=AFAP1-like protein 1;'
  gene_info: Name=AFAP1L1;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849);
    PH (PF00169)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8TED9
- **Protein Description:** RecName: Full=Actin filament-associated protein 1-like 1; Short=AFAP1-like protein 1;
- **Gene Information:** Name=AFAP1L1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); PH (PF00169)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AFAP1L1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AFAP1L1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AFAP1L1** (gene ID: AFAP1L1, UniProt: Q8TED9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AFAP1L1 (Actin Filament-Associated Protein 1-Like 1): A Comprehensive Review

## Introduction

AFAP1L1 (Actin Filament-Associated Protein 1-Like 1; UniProt: Q8TED9) is a human adaptor protein that functions as a critical regulator of actin cytoskeleton dynamics and cell invasion. Originally identified through a homology search of the human genome using the pleckstrin homology (PH) domain sequences of AFAP1, AFAP1L1 was recognized as the third member of the actin filament-associated protein (AFAP) family, which also includes AFAP1 (AFAP-110) and AFAP1L2 (XB130) [snyder-2011-afap1l1-invadosomes-abstract]. The gene is located on chromosome 5q33.1 and consists of 19 exons encoding a 768 amino acid protein with approximately 44% sequence identity to AFAP1 [snyder-2011-afap1l1-invadosomes-abstract].

As a non-enzymatic adaptor protein, AFAP1L1 does not catalyze biochemical reactions. Instead, it serves as a scaffold that links different components of cellular signaling complexes through multiple protein-binding motifs, thereby orchestrating cytoskeletal reorganization in response to upstream signals. The primary function of AFAP1L1 is to integrate signals from Src family tyrosine kinases and translate them into changes in actin cytoskeleton architecture, particularly at specialized actin-rich structures called invadosomes [tie-2016-sarcoma-invadopodia-abstract]. This function is essential for cell migration, invasion, and the formation of podosomes and invadopodia, making AFAP1L1 particularly relevant to cancer metastasis and pathological angiogenesis.

## Protein Structure and Domain Organization

AFAP1L1 possesses a characteristic modular domain architecture that enables its function as a signaling scaffold at the interface of actin dynamics and signal transduction. The protein contains several conserved domains shared with other AFAP family members, as well as unique features that confer distinct binding specificities [snyder-2011-afap1l1-invadosomes-abstract][xia-2016-xb130-adaptor-abstract].

The N-terminal region of AFAP1L1 contains a single SH3 binding motif with the sequence DLPPPLPNKP, which differs significantly from the dual SH3 binding motifs found in AFAP1 [snyder-2011-afap1l1-invadosomes-abstract]. This sequence variation is functionally significant: while AFAP1's SH3 binding motif preferentially interacts with the SH3 domain of the non-receptor tyrosine kinase cSrc, the AFAP1L1 SH3 binding motif exhibits approximately 9-fold higher affinity for cortactin's SH3 domain compared to cSrc [snyder-2011-afap1l1-invadosomes-abstract]. This preferential cortactin binding distinguishes AFAP1L1 from AFAP1 and suggests specialized functions in cortactin-dependent processes such as invadosome formation.

Two pleckstrin homology (PH) domains are positioned centrally within the protein, flanking a serine/threonine-rich region. These PH domains bind phosphoinositide lipids, particularly those generated at the plasma membrane by phosphoinositide 3-kinase (PI3K), enabling membrane recruitment and spatial regulation of AFAP1L1 function [tie-2016-sarcoma-invadopodia-abstract]. The PH domains of AFAP family members show high sequence conservation and form characteristic beta-barrel structures that mediate lipid interactions [snyder-2011-afap1l1-invadosomes-abstract].

The protein also contains two SH2 binding motifs that serve as docking sites for SH2 domain-containing proteins. Phosphorylation of tyrosine residues within these motifs creates binding sites for downstream effectors. Specifically, phospho-tyrosine 136 (pY136) binds the SH2 domain of Vav2, a guanine nucleotide exchange factor for Rho GTPases, while phospho-tyrosine 566 (pY566) binds the SH2 domain of Nck2, an adaptor protein that recruits actin-nucleating complexes [tie-2016-sarcoma-invadopodia-abstract].

The C-terminal region contains a leucine zipper motif that mediates intra- and inter-molecular interactions, enabling AFAP1L1 dimerization or multimerization, as well as a putative actin-binding domain that allows direct association with filamentous actin [snyder-2011-afap1l1-invadosomes-abstract]. This actin-binding capability is essential for AFAP1L1's localization to stress fibers and invadosomes.

## Subcellular Localization and Invadosome Association

AFAP1L1 localizes to specific subcellular compartments associated with dynamic actin structures, particularly invadosomes. Invadosomes is a collective term for podosomes (found in normal cells such as macrophages, osteoclasts, and smooth muscle cells) and invadopodia (found in cancer cells), which are actin-rich membrane protrusions specialized for extracellular matrix (ECM) degradation and cellular invasion [snyder-2011-afap1l1-invadosomes-abstract].

Fluorescence microscopy studies have demonstrated that AFAP1L1 decorates actin stress fibers and concentrates at punctate actin structures where it colocalizes with cortactin, a hallmark of invadosome localization [snyder-2011-afap1l1-invadosomes-abstract]. Upon overexpression in A7r5 rat aortic smooth muscle cells, AFAP1L1 can induce podosome formation without external stimulation, indicating that elevated AFAP1L1 levels are sufficient to trigger the cytoskeletal reorganization required for podosome assembly [snyder-2011-afap1l1-invadosomes-abstract].

In cancer cells, AFAP1L1 localizes to invadopodia, where it plays a critical role in regulating the machinery required for ECM degradation and cellular invasion. Studies in osteosarcoma cell lines have shown that AFAP1L1 knockdown disrupts invadopodia formation and inhibits phosphorylated myosin light chain 2 (MLC2) recruitment to filamentous actin structures [tie-2016-sarcoma-invadopodia-abstract]. This disruption impairs cell attachment, migration, and invasive capacity.

Immunohistochemical analysis of human tissues reveals differential expression patterns between AFAP1L1 and AFAP1. In breast tissue, AFAP1L1 is expressed in the contractile myoepithelial cell layer surrounding breast ducts and in the microvasculature [snyder-2011-afap1l1-invadosomes-abstract]. In colon, expression is detected in the mucous membrane, colonic crypts, and smooth muscle cell layer. Notably, AFAP1L1 shows unique expression in neuronal structures, particularly the dentate nucleus and Purkinje cell layer of the cerebellum, where it localizes along neuronal processes rather than cell bodies—a pattern distinct from AFAP1 [snyder-2011-afap1l1-invadosomes-abstract]. This tissue distribution suggests specialized functions in neuronal signaling and motor coordination pathways.

## Molecular Function and Signaling Mechanisms

AFAP1L1 functions as a signaling hub that integrates upstream kinase signals and translates them into coordinated cytoskeletal changes. The protein operates through phosphotyrosine-dependent mechanisms that link Src family kinase activation to actin dynamics regulation [tie-2016-sarcoma-invadopodia-abstract].

The interaction between AFAP1L1 and cortactin is central to its function. Cortactin is an actin nucleation-promoting factor that activates the Arp2/3 complex to initiate branched actin network formation. By preferentially binding cortactin through its SH3 binding motif, AFAP1L1 positions itself at sites of active actin polymerization where it can coordinate additional signaling inputs [snyder-2011-afap1l1-invadosomes-abstract].

Phosphorylation of AFAP1L1 by Src family kinases, particularly Lyn, creates docking sites for downstream effectors. The pY136-Vav2 interaction is particularly important, as Vav2 is a guanine nucleotide exchange factor (GEF) that activates Rho family GTPases including Rac and CDC42 [tie-2016-sarcoma-invadopodia-abstract][sun-2023-gastric-vav2-cdc42-abstract]. Through Vav2, AFAP1L1 regulates Rac activity and controls the downstream PAK1/2/3 (p21-activated kinases) pathway, which phosphorylates MLC kinase and MLC2 to regulate actomyosin contractility [tie-2016-sarcoma-invadopodia-abstract].

The pY566-Nck2 interaction provides an alternative signaling output by recruiting actin-nucleating complexes to sites of AFAP1L1 localization. Nck2 (also known as NCKβ or Grb4) is an adaptor protein that links receptor tyrosine kinases to downstream actin regulators including N-WASP and the Arp2/3 complex [tie-2016-sarcoma-invadopodia-abstract].

In gastric cancer cells, AFAP1L1 activates a specific signaling cascade involving VAV2, CDC42, and integrin α5 (ITGA5). Co-immunoprecipitation experiments confirmed the physical interaction between AFAP1L1 and VAV2, and demonstrated that this interaction activates CDC42 GTPase activity. Activated CDC42 promotes ITGA5 expression at the transcriptional level, leading to activation of integrin signaling through focal adhesion kinase (FAK) and ERK pathways [sun-2023-gastric-vav2-cdc42-abstract]. This signaling axis drives epithelial-to-mesenchymal transition (EMT) characterized by decreased E-cadherin and increased vimentin expression.

## Role in Cell Migration and Invasion

AFAP1L1 plays a critical role in regulating cell migration and invasion, processes that require dynamic remodeling of the actin cytoskeleton. The protein's function in these processes has been extensively characterized in cancer cells, where elevated AFAP1L1 expression promotes invasive behavior [tie-2016-sarcoma-invadopodia-abstract][sun-2023-gastric-vav2-cdc42-abstract].

Studies in sarcoma cells demonstrated that AFAP1L1 can transform cells and promote migration when co-expressed with active Lyn kinase. This co-expression profoundly influences cell morphology and movement, indicating that AFAP1L1 translates Src family kinase signals into morphological changes required for motility [tie-2016-sarcoma-invadopodia-abstract]. Conversely, knockdown of AFAP1L1 in osteosarcoma cell lines inhibits cell attachment, migration, and invasion, accompanied by disruption of invadopodia formation and impaired MLC2 phosphorylation at actin structures [tie-2016-sarcoma-invadopodia-abstract].

In gastric cancer cells, AFAP1L1 promotes proliferation, migration, and invasion in vitro, and enhances tumor growth and metastasis in vivo. These effects are mediated through the VAV2-CDC42-ITGA5 signaling axis and the induction of EMT [sun-2023-gastric-vav2-cdc42-abstract]. The functional importance of CDC42 activation is highlighted by experiments showing that ML141, a selective CDC42 GTPase inhibitor, can prevent tumor progression in cells with high AFAP1L1 expression.

Beyond cancer, AFAP1L1's actin cross-linking function has been shown to provide a physical barrier against Trypanosoma cruzi invasion. Knockdown of AFAP1L1 in host cells induces softening of actin filaments and facilitates parasite cell invasion and intracellular multiplication, demonstrating that AFAP1L1-mediated cytoskeletal integrity can function as a host defense mechanism [araujo-2016-trypanosoma-cruzi-abstract].

## Role in Angiogenesis and the YAP-DLL4-NOTCH Pathway

Recent research has identified AFAP1L1 as a regulator of pathological angiogenesis through a mechanism involving the YAP-DLL4-NOTCH signaling axis. This function extends AFAP1L1's significance beyond cancer cell invasion to include endothelial cell biology and blood vessel formation [ren-2023-hypoxia-neovascularization-abstract].

AFAP1L1 expression correlates positively with hypoxia signaling across multiple cancer types. Under hypoxic conditions, hypoxia-inducible factor 1 alpha (HIF-1α) directly activates AFAP1L1 transcription by binding to hypoxia response elements in the AFAP1L1 promoter [ren-2023-hypoxia-neovascularization-abstract]. This establishes AFAP1L1 as a hypoxia-responsive gene with potential roles in tumor adaptation to low oxygen environments.

Mechanistically, AFAP1L1 inhibits YAP phosphorylation, promoting YAP nuclear translocation where it suppresses DLL4 (Delta-like ligand 4) expression. DLL4 is a key ligand for Notch receptors, and reduced DLL4 expression alters Notch signaling in endothelial cells, leading to increased tip cell sprouting and angiogenesis [ren-2023-hypoxia-neovascularization-abstract]. When AFAP1L1 is knocked down, YAP becomes hyperphosphorylated and retained in the cytoplasm, resulting in increased DLL4 expression, enhanced Notch activation, and suppressed angiogenic sprouting.

Studies using endothelial cell-specific AFAP1L1 conditional knockout mice demonstrated that AFAP1L1 deletion reduces tumor growth and blood vessel formation. In three different models of ocular pathological neovascularization—oxygen-induced retinopathy, laser-induced choroidal neovascularization, and suture-induced corneal neovascularization—AFAP1L1 inhibition significantly reduced abnormal blood vessel formation [ren-2023-hypoxia-neovascularization-abstract]. These findings suggest AFAP1L1 as a potential therapeutic target for both solid tumors and neovascular eye diseases, offering an alternative to anti-VEGF therapies that face issues with drug resistance.

As an actin-associated protein, AFAP1L1 also influences endothelial cell morphology and filopodia formation, structures critical for directed cell migration during vessel sprouting. This cytoskeletal function may complement the YAP-DLL4-NOTCH signaling mechanism in regulating angiogenesis.

## Role in Cancer

AFAP1L1 has emerged as a significant factor in cancer biology, with elevated expression associated with tumor progression and poor prognosis across multiple cancer types. Unlike AFAP1 and AFAP1L2/XB130, AFAP1L1 shows consistent upregulation in several malignancies, positioning it as a potential biomarker and therapeutic target [sun-2023-gastric-vav2-cdc42-abstract][zhang-2018-lung-cancer-abstract].

In gastric cancer, systematic analysis of the AFAP family revealed that AFAP1L1 is the only family member significantly upregulated compared to normal gastric tissues. Elevated AFAP1L1 expression predicts poor prognosis and serves as an independent risk factor for patient survival [sun-2023-gastric-vav2-cdc42-abstract]. The protein promotes gastric cancer progression through the VAV2-CDC42-ITGA5 signaling pathway, driving EMT and enhancing invasive and metastatic potential.

In non-small cell lung cancer (NSCLC), AFAP1L1 functions as an oncogenic factor. Knockdown studies in A549 lung cancer cells demonstrated that AFAP1L1 depletion significantly inhibits cell cycle progression, increases apoptosis, and attenuates cell growth [zhang-2018-lung-cancer-abstract]. Mechanistically, AFAP1L1 knockdown triggers activation of p38 MAPK, decreases PRAS40 phosphorylation, and increases caspase-3 cleavage, indicating activation of stress response and apoptotic pathways. These findings suggest AFAP1L1 may serve as both a prognostic marker and therapeutic target in NSCLC.

In sarcomas, AFAP1L1 regulates cell migration, invasion, and invadopodia formation through phosphotyrosine-dependent pathways involving Lyn kinase, Vav2, and Nck2 [tie-2016-sarcoma-invadopodia-abstract]. The protein's ability to transform cells and promote migration when co-expressed with active kinases highlights its oncogenic potential in mesenchymal malignancies.

The angiogenesis-promoting function of AFAP1L1 through the YAP-DLL4-NOTCH axis adds another dimension to its role in cancer. By promoting tumor neovascularization under hypoxic conditions, AFAP1L1 may contribute to tumor growth and progression beyond its cell-autonomous effects on invasion and metastasis [ren-2023-hypoxia-neovascularization-abstract].

## Transcriptional Regulation

The transcriptional regulation of AFAP1L1 expression has been characterized, providing insight into how this gene is controlled in normal and pathological contexts. The proximal promoter region of AFAP1L1 contains tandem specificity protein (Sp) binding motifs at positions -86 to -76 that are essential for transcriptional activity [kajita-2012-sp3-transcription-abstract]. While both Sp1 and Sp3 transcription factors can activate the AFAP1L1 promoter in vitro, chromatin immunoprecipitation experiments demonstrated that Sp3 is the major transcription factor binding to the proximal promoter in AFAP1L1-positive cells [kajita-2012-sp3-transcription-abstract].

Treatment with mithramycin A, which inhibits Sp protein binding to GC-rich DNA sequences, effectively blocks Sp3 binding and reduces AFAP1L1 expression in a dose-dependent manner. Furthermore, siRNA knockdown of Sp3 significantly reduces AFAP1L1 expression and decreases cell invasion and migration in osteosarcoma cells [kajita-2012-sp3-transcription-abstract]. Sequence alignment of the 5'-flanking region of the AFAP1L1 gene across human, mouse, and rabbit revealed conserved Sp-binding sites, suggesting that this regulatory mechanism is evolutionarily maintained across mammals.

In addition to Sp3-mediated basal transcription, AFAP1L1 expression is regulated by hypoxia through HIF-1α. Under hypoxic conditions, HIF-1α directly activates AFAP1L1 transcription by binding to hypoxia response elements in the promoter [ren-2023-hypoxia-neovascularization-abstract]. This dual regulation—by Sp3 for basal expression and HIF-1α for hypoxia-induced expression—positions AFAP1L1 at the intersection of constitutive cellular functions and stress-responsive pathways.

## Evolutionary Conservation and Mouse Models

AFAP1L1 is evolutionarily conserved across vertebrates, with stringent orthologs identified in mouse (Afap1l1), rat, and zebrafish. The mouse ortholog (MGI:2147199) is located on chromosome 18 and shows high sequence conservation, particularly in the functionally critical domains including the PH domains, SH3 binding motif, and actin-binding region. Conservation of the Sp-binding sites in the promoter region across human, mouse, and rabbit further indicates functional conservation of transcriptional regulation [kajita-2012-sp3-transcription-abstract].

Mouse knockout studies have been instrumental in understanding AFAP1L1 function in vivo. The International Mouse Phenotyping Consortium (IMPC) has generated Afap1l1 knockout mice, with multiple alleles available including gene-trapped and targeted mutations. Interestingly, initial phenotyping of Afap1l1 knockout mice across 15 physiological systems revealed no significant overt phenotypes, suggesting either functional redundancy with other family members or that phenotypes may be context-dependent and manifest under specific challenges such as tumor development or wound healing.

More informative in vivo studies have employed tissue-specific knockdown approaches. Endothelial cell-specific AFAP1L1 knockdown using adeno-associated virus (AAV) vectors under control of the TIE promoter demonstrated that AFAP1L1 depletion in endothelium significantly reduces tumor growth and volume, decreases blood vessel formation, and inhibits pathological neovascularization in multiple ocular disease models [ren-2023-hypoxia-neovascularization-abstract]. Similarly, xenograft studies showed that AFAP1L1 knockdown inhibits formation of pulmonary and liver metastasis foci [sun-2023-gastric-vav2-cdc42-abstract]. These conditional knockdown studies reveal functions that may not be apparent in constitutive knockout models due to developmental compensation.

## Relationship to Other AFAP Family Members

The AFAP family comprises three members—AFAP1 (AFAP-110), AFAP1L1, and AFAP1L2 (XB130)—that share structural similarity but exhibit distinct functional properties and binding specificities [xia-2016-xb130-adaptor-abstract][snyder-2011-afap1l1-invadosomes-abstract].

All three family members were named by the Human Genome Project based on similarity in modular domain structure and amino acid sequence, particularly within their PH domains. They share conserved features including PH domains, SH2 binding motifs, and regions involved in actin association. However, significant differences exist in their SH3 binding properties, SH2 binding motif number, and C-terminal domains [xia-2016-xb130-adaptor-abstract].

AFAP1 contains dual SH3 binding motifs that preferentially bind cSrc, enabling it to function as a cSrc binding partner and actin cross-linking protein. In contrast, AFAP1L1's single SH3 binding motif preferentially binds cortactin rather than cSrc, suggesting specialized functions in cortactin-dependent processes [snyder-2011-afap1l1-invadosomes-abstract]. This differential binding is functionally significant: AFAP1 may primarily operate in Src-dependent signaling contexts, while AFAP1L1 may be more important for cortactin-mediated invadosome function.

AFAP1L2/XB130 represents a more divergent family member with only 35% identity to AFAP1. Unlike AFAP1 and AFAP1L1, XB130 does not efficiently bind actin filaments. Instead, XB130 has specialized functions including coupling the RET/PTC oncogenic kinase to PI3K signaling in thyroid cells and regulating cell survival through the PI3K/Akt pathway [xia-2016-xb130-adaptor-abstract]. XB130 also contains three SH2 binding motifs compared to the single motif in AFAP1 and AFAP1L1, enabling more extensive SH2-mediated protein interactions.

Tissue expression patterns also distinguish family members. While AFAP1 is expressed in mesenchymal tissues, AFAP1L1 shows unique expression in neuronal structures including the dentate nucleus and Purkinje cell layer of the cerebellum [snyder-2011-afap1l1-invadosomes-abstract]. This differential distribution suggests specialized roles for AFAP1L1 in neuronal signaling and motor coordination that are not shared with AFAP1.

## Open Questions

Several important questions about AFAP1L1 biology remain to be addressed:

1. **Structural biology**: No experimental crystal structure or cryo-EM structure of full-length AFAP1L1 or its individual domains has been reported, although AlphaFold provides a predicted structure (UniProt: Q8TED9). Experimental structural information would clarify how the protein integrates multiple signaling inputs, validate the predicted structure, and enable structure-based drug design.

2. **Neuronal function**: The unique expression of AFAP1L1 in the dentate nucleus and Purkinje cells suggests specialized neuronal functions that have not been characterized. What is the role of AFAP1L1 in neuronal signaling, synaptic plasticity, or motor coordination?

3. **Post-translational regulation**: Beyond the characterized tyrosine phosphorylation sites (pY136 and pY566), what other post-translational modifications regulate AFAP1L1 function? The serine/threonine-rich region between the PH domains suggests potential regulation by serine/threonine kinases.

4. **Cortactin interaction mechanism**: What is the precise structural basis for AFAP1L1's preferential binding to cortactin over cSrc? How does this interaction differ from AFAP1-cSrc binding?

5. **YAP regulation mechanism**: How does AFAP1L1 inhibit YAP phosphorylation? Does this involve direct interaction with Hippo pathway kinases (LATS1/2) or indirect effects through cytoskeletal changes?

6. **Therapeutic targeting**: Given AFAP1L1's role in cancer and angiogenesis, what are the most effective strategies for therapeutic inhibition? Targeting Sp3 to reduce AFAP1L1 transcription has been proposed [kajita-2012-sp3-transcription-abstract], but targeting the cortactin interaction, the phosphotyrosine signaling outputs, or the actin-binding domain may also be effective.

7. **Normal physiological functions**: IMPC knockout mice show no overt phenotypes across 15 physiological systems tested, suggesting redundancy or context-dependent functions. What challenges (wound healing, infection, tumorigenesis) would reveal essential functions?

8. **Redundancy with AFAP1**: To what extent can AFAP1 and AFAP1L1 compensate for each other's functions? In what contexts are their functions truly distinct? Double knockout studies would be informative.

## References

- [snyder-2011-afap1l1-invadosomes-abstract] Snyder BN, Cho Y, Qian Y, Coad JE, Cunnick J, Flynn D. AFAP1L1 is a novel adaptor protein of the AFAP family that interacts with cortactin and localizes to invadosomes. Eur J Cell Biol. 2011;90(2-3):259-71. PMID: 21051111. PMCID: PMC3085893. DOI: 10.1016/j.ejcb.2010.09.011

- [tie-2016-sarcoma-invadopodia-abstract] Tie SR, McCarthy DJ, Kendrick TS, Louw A, Le C, Satiaputra J, Kucera N, Phillips M, Ingley E. Regulation of sarcoma cell migration, invasion and invadopodia formation by AFAP1L1 through a phosphotyrosine-dependent pathway. Oncogene. 2016;35(16):2098-2111. PMID: 26212012. DOI: 10.1038/onc.2015.272

- [sun-2023-gastric-vav2-cdc42-abstract] Sun B, Ding B, Chen Y, Peng C, Chen X. AFAP1L1 promotes gastric cancer progression by interacting with VAV2 to facilitate CDC42-mediated activation of ITGA5 signaling pathway. J Transl Med. 2023;21(1):11. PMID: 36631800. PMCID: PMC9835296. DOI: 10.1186/s12967-023-03871-8

- [ren-2023-hypoxia-neovascularization-abstract] Ren JS, Bai W, Ding JJ, Ge HM, Wang SY, Chen X, Jiang Q. Hypoxia-induced AFAP1L1 regulates pathological neovascularization via the YAP-DLL4-NOTCH axis. J Transl Med. 2023;21(1):651. PMID: 37737201. PMCID: PMC10515434. DOI: 10.1186/s12967-023-04503-x

- [xia-2016-xb130-adaptor-abstract] Xia J, Luo N, Jiang S, Li Y, Chen W. XB130: A novel adaptor protein in cancer signal transduction (Review). Biomed Rep. 2016;4(3):300-304. PMID: 26998267. PMCID: PMC4774376. DOI: 10.3892/br.2016.588

- [zhang-2018-lung-cancer-abstract] Zhang Z, Zhou J, Wu X, Guo Z, Zhou Y, Zhou J, Xu J, Chen B. Actin Filament-Associated Protein 1-Like 1 Mediates Proliferation and Survival in Non-Small Cell Lung Cancer Cells. Med Sci Monit. 2018;24:1110-1118. PMID: 29463794. PMCID: PMC5772338. DOI: 10.12659/msm.907648

- [araujo-2016-trypanosoma-cruzi-abstract] de Araújo KCL, Teixeira TL, Machado FC, da Silva AA, Quintal APN, da Silva CV. AFAP-1L1-mediated actin filaments crosslinks hinder Trypanosoma cruzi cell invasion and intracellular multiplication. Acta Trop. 2016;162:167-170. PMID: 27392663. DOI: 10.1016/j.actatropica.2016.07.001

- [kajita-2012-sp3-transcription-abstract] Kajita Y, Kato T Jr, Tamaki S, Furu M, Takahashi R, Nagayama S, Aoyama T, Nishiyama H, Nakamura E, Katagiri T, Nakamura Y, Ogawa O, Toguchida J. The Transcription Factor Sp3 Regulates the Expression of a Metastasis-Related Marker of Sarcoma, Actin Filament-Associated Protein 1-Like 1 (AFAP1L1). PLoS One. 2012;7(11):e49709. PMID: 23166755. PMCID: PMC3498310. DOI: 10.1371/journal.pone.0049709


## Citations

1. araujo-2016-trypanosoma-cruzi-abstract.md
2. kajita-2012-sp3-transcription-abstract.md
3. ren-2023-hypoxia-neovascularization-abstract.md
4. ren-2023-hypoxia-neovascularization-summary.md
5. snyder-2011-afap1l1-invadosomes-abstract.md
6. snyder-2011-afap1l1-invadosomes-summary.md
7. sun-2023-gastric-vav2-cdc42-abstract.md
8. sun-2023-gastric-vav2-cdc42-summary.md
9. tie-2016-sarcoma-invadopodia-abstract.md
10. tie-2016-sarcoma-invadopodia-summary.md
11. xia-2016-xb130-adaptor-abstract.md
12. zhang-2018-lung-cancer-abstract.md