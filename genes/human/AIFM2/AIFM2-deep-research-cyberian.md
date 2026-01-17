---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T14:31:18.134639'
end_time: '2026-01-15T14:49:12.326350'
duration_seconds: 1074.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AIFM2
  gene_symbol: AIFM2
  uniprot_accession: Q9BRQ8
  protein_description: 'RecName: Full=Ferroptosis suppressor protein 1 {ECO:0000303|PubMed:31634899,
    ECO:0000303|PubMed:31634900}; Short=FSP1 {ECO:0000303|PubMed:31634899, ECO:0000303|PubMed:31634900};
    EC=1.6.5.- {ECO:0000269|PubMed:31634899, ECO:0000269|PubMed:31634900, ECO:0000269|PubMed:35922516};
    AltName: Full=Apoptosis-inducing factor homologous mitochondrion-associated inducer
    of death {ECO:0000303|PubMed:11980907}; Short=AMID {ECO:0000303|PubMed:11980907};
    AltName: Full=p53-responsive gene 3 protein {ECO:0000303|PubMed:12135761};'
  gene_info: Name=AIFM2 {ECO:0000303|PubMed:26689472, ECO:0000312|HGNC:HGNC:21411};
    Synonyms=AMID {ECO:0000303|PubMed:11980907}, PRG3 {ECO:0000303|PubMed:12135761};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the FAD-dependent oxidoreductase family.
  protein_domains: FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); Pyr_redox_2
    (PF07992)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9BRQ8
- **Protein Description:** RecName: Full=Ferroptosis suppressor protein 1 {ECO:0000303|PubMed:31634899, ECO:0000303|PubMed:31634900}; Short=FSP1 {ECO:0000303|PubMed:31634899, ECO:0000303|PubMed:31634900}; EC=1.6.5.- {ECO:0000269|PubMed:31634899, ECO:0000269|PubMed:31634900, ECO:0000269|PubMed:35922516}; AltName: Full=Apoptosis-inducing factor homologous mitochondrion-associated inducer of death {ECO:0000303|PubMed:11980907}; Short=AMID {ECO:0000303|PubMed:11980907}; AltName: Full=p53-responsive gene 3 protein {ECO:0000303|PubMed:12135761};
- **Gene Information:** Name=AIFM2 {ECO:0000303|PubMed:26689472, ECO:0000312|HGNC:HGNC:21411}; Synonyms=AMID {ECO:0000303|PubMed:11980907}, PRG3 {ECO:0000303|PubMed:12135761};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the FAD-dependent oxidoreductase family.
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); Pyr_redox_2 (PF07992)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AIFM2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AIFM2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AIFM2** (gene ID: AIFM2, UniProt: Q9BRQ8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AIFM2/FSP1: A Comprehensive Review of Ferroptosis Suppressor Protein 1

## 1. Introduction and Summary

Apoptosis-inducing factor mitochondria-associated 2 (AIFM2), now more commonly known as Ferroptosis Suppressor Protein 1 (FSP1), is a flavoprotein oxidoreductase encoded by the AIFM2 gene (chromosome 10q22.1) in humans [ohiro-2002-prg3-abstract]. The protein belongs to the FAD-dependent oxidoreductase family and contains 373 amino acids with a molecular mass of approximately 40.5 kDa [ohiro-2002-prg3-abstract]. This protein has undergone a remarkable reconceptualization since its original discovery: initially characterized as a pro-apoptotic factor homologous to AIF, it is now understood to function primarily as a potent suppressor of ferroptosis, a form of iron-dependent regulated cell death driven by lipid peroxidation [doll-2019-fsp1-glutathione-abstract][bersuker-2019-coq-oxidoreductase-abstract].

The primary enzymatic function of FSP1 is to catalyze the NAD(P)H-dependent reduction of ubiquinone (coenzyme Q10, CoQ10) to ubiquinol (CoQ10H2), a lipophilic radical-trapping antioxidant that halts the propagation of lipid peroxides [bersuker-2019-coq-oxidoreductase-abstract][doll-2019-fsp1-glutathione-abstract]. Additionally, FSP1 reduces vitamin K to its hydroquinone form, providing another mechanism of ferroptosis suppression through a non-canonical vitamin K cycle [mishima-2022-vitamin-k-abstract]. The protein localizes primarily to the plasma membrane through N-terminal myristoylation, where it protects membrane lipids from peroxidation [bersuker-2019-coq-oxidoreductase-abstract]. The discovery of FSP1 as a parallel ferroptosis-suppressing system, independent of the canonical glutathione peroxidase 4 (GPX4) pathway, fundamentally changed the understanding of ferroptosis regulation and opened new therapeutic avenues for cancer treatment.

## 2. Discovery and Nomenclature History

The protein now known as FSP1 was independently discovered by multiple research groups under different names, reflecting its apparent involvement in various cellular processes. In 2002, Wu and colleagues at Peking University identified a novel AIF-homologous protein they named AMID (AIF-homologous Mitochondrion-associated Inducer of Death) [wu-2002-amid-abstract]. Their work demonstrated that AMID co-localized with mitochondria and, when overexpressed, induced caspase-independent and p53-independent apoptosis that was not inhibited by Bcl-2 [wu-2002-amid-abstract]. Concurrently, Ohiro et al. identified the same gene as PRG3 (p53-Responsive Gene 3), noting that it was induced specifically under p53-dependent apoptotic conditions in human colon cancer cells [ohiro-2002-prg3-abstract]. Interestingly, these early studies reported that an N-terminal deletion mutant lacking the putative oxidoreductase domain retained apoptotic activity, suggesting the enzymatic function was dispensable for the apoptotic pathway [ohiro-2002-prg3-abstract].

The paradigm shifted dramatically in October 2019 when two landmark papers published simultaneously in Nature revealed the protein's primary physiological function. Using a synthetic lethal CRISPR-Cas9 screen, Bersuker et al. at UC Berkeley identified AIFM2 as a potent ferroptosis resistance factor and renamed it Ferroptosis Suppressor Protein 1 (FSP1) [bersuker-2019-coq-oxidoreductase-abstract]. In parallel, Doll et al. from the Conrad laboratory at the Helmholtz Institute used an expression cloning approach to identify genes that could complement GPX4 loss and independently arrived at the same conclusion [doll-2019-fsp1-glutathione-abstract]. These studies established that FSP1's primary cellular function is to suppress lipid peroxidation and ferroptosis, rather than to promote apoptosis as originally proposed [doll-2019-fsp1-glutathione-abstract][bersuker-2019-coq-oxidoreductase-abstract].

## 3. Enzymatic Function and Catalytic Mechanism

FSP1 functions as a NAD(P)H-dependent quinone oxidoreductase, catalyzing the two-electron reduction of ubiquinone (CoQ10) to ubiquinol (CoQ10H2) [doll-2019-fsp1-glutathione-abstract][bersuker-2019-coq-oxidoreductase-abstract]. The reduced ubiquinol acts as a lipophilic radical-trapping antioxidant (RTA) that neutralizes lipid peroxyl radicals, thereby preventing the propagation of lipid peroxidation that would otherwise lead to ferroptosis [bersuker-2019-coq-oxidoreductase-abstract]. This reaction can be summarized as:

**CoQ10 (oxidized) + NAD(P)H + H+ → CoQ10H2 (reduced) + NAD(P)+**

Structural insights into FSP1 catalysis came from crystal structures of Gallus gallus FSP1 solved at 2.0 Å (substrate-free) and 2.6 Å (ubiquinone-bound) resolution [lv-2023-structural-insights-abstract]. The structure reveals three distinct domains: a FAD-binding domain, a NAD(P)H-binding domain (both shared with AIF and NADH oxidoreductases), and a characteristic carboxy-terminal domain [lv-2023-structural-insights-abstract]. The carboxy-terminal domain mediates functional dimerization of FSP1, forming a homodimer that is required for the assembly of FAD- and ubiquinone-binding pockets and for catalytic activity [lv-2023-structural-insights-abstract].

A unique feature of FSP1 structure is the ~25-degree rotation of the FAD isoalloxazine ring compared to all other known FAD-dependent oxidoreductases [lv-2023-structural-insights-abstract]. The homodimer creates two active sites located on opposite sides of the FAD cofactor: one responsible for ubiquinone reduction and another for a unique FAD hydroxylation reaction that generates 6-hydroxy-FAD [lv-2023-structural-insights-abstract]. This 6-hydroxy-FAD was identified as both an active cofactor of FSP1 and a potent anti-ferroptotic compound in its own right, adding another layer to FSP1's ferroptosis-suppressing mechanisms [lv-2023-structural-insights-abstract].

Beyond ubiquinone, FSP1 also efficiently reduces vitamin K (both menaquinone and phylloquinone) to their hydroquinone forms [mishima-2022-vitamin-k-abstract]. This vitamin K reductase activity is particularly significant because it explains the warfarin-resistant vitamin K reduction pathway: FSP1 mediates vitamin K reduction independently of the canonical VKORC1-mediated pathway that is inhibited by warfarin [mishima-2022-vitamin-k-abstract]. The reduced vitamin K hydroquinone (VKH2) functions as another potent radical-trapping antioxidant that prevents lipid peroxidation, representing a third anti-ferroptotic mechanism mediated by FSP1 [mishima-2022-vitamin-k-abstract]. FSP1 can also reduce vitamin E (α-tocopherol), either directly or indirectly through ubiquinol-mediated regeneration, further expanding its antioxidant capacity [mishima-2022-vitamin-k-abstract].

### Substrate Specificity and Kinetic Properties

FSP1 demonstrates broad substrate specificity within the quinone class of molecules. The known substrates include NADH and NADPH as electron donors, and CoQ10 (ubiquinone), CoQ1 (a short-chain ubiquinone analog), menadione (vitamin K3), and resazurin as electron acceptors [nakamura-2023-integrated-screens-abstract]. Kinetic analyses have been performed using resazurin reduction as a proxy for enzymatic activity, with reactions typically containing 100 nM recombinant human FSP1 protein [dasilva-2023-ifsp1-inhibition-abstract]. Lineweaver-Burk and Dixon plot analyses revealed that FSP1 inhibitors such as iFSP1 and viFSP1 are non-competitive inhibitors, meaning they can bind the enzyme regardless of substrate presence [nakamura-2023-integrated-screens-abstract].

Integrated chemical and genetic screens have provided detailed insights into FSP1's catalytic mechanism [nakamura-2023-integrated-screens-abstract]. Random mutagenesis studies identified conserved binding sites for the FAD and NAD(P)H cofactors and characterized critical proton-transfer mechanisms essential for catalysis. The development of two distinct classes of FSP1 inhibitors—iFSP1 targeting the quinone-binding pocket and viFSP1 targeting the NAD(P)H-binding pocket—confirmed the presence of two separate functional sites [nakamura-2023-integrated-screens-abstract]. Notably, iFSP1 is human-specific and does not effectively inhibit murine FSP1 due to species differences in an aromatic pocket, with F360 of human FSP1 being essential for iFSP1 binding [dasilva-2023-ifsp1-inhibition-abstract]. This species specificity has important implications for preclinical studies in mouse models.

## 4. Subcellular Localization and Membrane Association

The subcellular localization of FSP1 is critical for its anti-ferroptotic function. The protein contains a canonical N-terminal myristoylation motif, and this post-translational modification is essential for targeting FSP1 to cellular membranes [bersuker-2019-coq-oxidoreductase-abstract]. N-myristoylation involves the attachment of myristate, a 14-carbon saturated fatty acid, to the N-terminal glycine residue by N-myristoyltransferase (NMT), mediating dynamic protein-membrane interactions [bersuker-2019-coq-oxidoreductase-abstract].

Myristoylated FSP1 is primarily recruited to the plasma membrane, where it functions to reduce ubiquinone to ubiquinol at the site where lipid peroxidation most threatens cellular integrity [bersuker-2019-coq-oxidoreductase-abstract]. This membrane localization is absolutely required for ferroptosis suppression: the G2A mutant, which cannot be myristoylated, shows strongly affected localization and completely loses its ferroptosis-suppressive function [bersuker-2019-coq-oxidoreductase-abstract]. Importantly, fusion of a membrane-targeting sequence (Lyn11) to the G2A mutant restores its ability to suppress ferroptosis, confirming that membrane localization, rather than myristoylation per se, is the critical requirement [bersuker-2019-coq-oxidoreductase-abstract].

Beyond the plasma membrane, FSP1 also localizes to the periphery of lipid droplets (LDs) [nakamura-2023-phase-separation-abstract]. Recent work has revealed that LD-localized FSP1 plays a critical role in preventing neutral lipid peroxidation, a previously unrecognized function. By recycling CoQ10 to its antioxidant form at LDs, FSP1 prevents the accumulation of oxidized triacylglycerols and cholesteryl esters, thereby maintaining lipid droplet integrity and preventing LD-initiated ferroptosis when cells are loaded with polyunsaturated fatty acid-rich lipids.

The early characterization of AMID/AIFM2 suggested mitochondrial localization [wu-2002-amid-abstract], and indeed the protein can associate with the outer mitochondrial membrane despite lacking a canonical mitochondrial localization sequence [wu-2002-amid-abstract]. However, the predominant and functionally relevant localization for ferroptosis suppression is the plasma membrane. Interestingly, inhibition of myristoylation with compounds like IMP-366 not only abolishes the anti-ferroptosis function of FSP1 but also promotes its nuclear translocation via importin α2, suggesting complex regulation of FSP1 localization.

## 5. Role in Ferroptosis Suppression: Three Parallel Mechanisms

Three distinct mechanisms by which FSP1 suppresses ferroptosis have been elucidated, representing a comprehensive defense system against lipid peroxidation.

### The FSP1-CoQ10-NAD(P)H Pathway

The primary and best-characterized mechanism involves FSP1's oxidoreductase activity at the plasma membrane [doll-2019-fsp1-glutathione-abstract][bersuker-2019-coq-oxidoreductase-abstract]. FSP1 catalyzes the reduction of ubiquinone (CoQ10) to ubiquinol (CoQ10H2) using NAD(P)H as the electron donor. The resulting ubiquinol functions as a lipophilic radical-trapping antioxidant that directly scavenges lipid peroxyl radicals, breaking the chain reaction of lipid peroxidation [doll-2019-fsp1-glutathione-abstract]. This pathway operates entirely independently of the canonical GPX4/glutathione system, providing cells with a parallel defense mechanism. The physiological importance of this redundancy is evident in the observation that cancer cells with high FSP1 expression are resistant to GPX4 inhibitors [bersuker-2019-coq-oxidoreductase-abstract].

### The FSP1-Vitamin K-NAD(P)H Pathway

The second mechanism involves FSP1's vitamin K reductase activity [mishima-2022-vitamin-k-abstract]. FSP1 efficiently reduces vitamin K (menaquinone and phylloquinone) to their corresponding hydroquinones using NAD(P)H. These vitamin K hydroquinones function as potent radical-trapping antioxidants, similar to ubiquinol, preventing lipid peroxidation [mishima-2022-vitamin-k-abstract]. This pathway is warfarin-resistant, as it operates independently of the VKORC1 enzyme that is the target of warfarin [mishima-2022-vitamin-k-abstract]. The FSP1-vitamin K pathway represents a non-canonical vitamin K cycle with clear anti-ferroptotic function beyond vitamin K's classical role in blood coagulation [mishima-2022-vitamin-k-abstract].

### The FSP1-ESCRT-III Membrane Repair Pathway

A third mechanism involves FSP1's role in promoting ESCRT-III-dependent membrane repair. The ESCRT-III (Endosomal Sorting Complexes Required for Transport-III) machinery mediates membrane deformation and fission, and plays a role in repairing damaged plasma membranes. FSP1 has been shown to potentiate the recruitment of ESCRT-III subunits CHMP5 and CHMP6 to the plasma membrane following ferroptosis-inducing stress. Knockdown of FSP1 suppresses the membrane accumulation of these ESCRT-III components, while overexpression of CHMP5 can rescue cells from ferroptosis even when FSP1 is silenced. This pathway operates independently of CoQ10, suggesting that FSP1 has functions beyond its enzymatic activity.

## 6. Relationship to GPX4 and the Ferroptosis Defense Network

Prior to the discovery of FSP1's anti-ferroptotic function, GPX4 (glutathione peroxidase 4) was considered the sole master regulator of ferroptosis. GPX4 reduces lipid hydroperoxides to lipid alcohols using glutathione (GSH) as a cofactor, representing the canonical ferroptosis defense system [doll-2019-fsp1-glutathione-abstract]. The identification of FSP1 revealed that cells possess parallel, independent mechanisms to prevent ferroptosis.

The FSP1-CoQ10-NAD(P)H pathway operates as a stand-alone parallel system that cooperates with the GPX4-glutathione axis [doll-2019-fsp1-glutathione-abstract]. These two systems provide complementary protection: GPX4 directly reduces lipid hydroperoxides that have already formed, while FSP1 generates ubiquinol that scavenges lipid peroxyl radicals before they can propagate [doll-2019-fsp1-glutathione-abstract][bersuker-2019-coq-oxidoreductase-abstract]. The existence of this backup system explains why some cancer cells survive GPX4 inhibition—they upregulate or rely on FSP1-mediated protection [bersuker-2019-coq-oxidoreductase-abstract].

A third component of the ferroptosis defense network is dihydroorotate dehydrogenase (DHODH), a flavin-dependent mitochondrial enzyme that, in addition to its canonical role in pyrimidine biosynthesis, regenerates ubiquinol in the inner mitochondrial membrane. While FSP1 protects the plasma membrane and other extramitochondrial membranes, DHODH specifically protects the mitochondrial compartment. GPX4 provides protection across multiple compartments including the cytoplasm and mitochondrial matrix. This compartmentalization allows cells to mount context-specific responses depending on the source of oxidative stress.

## 7. Regulation of FSP1 Expression

FSP1 expression is regulated at the transcriptional level by several pathways, most notably the KEAP1-NRF2 antioxidant response pathway. Nuclear factor erythroid 2-related factor 2 (NRF2) is a master transcription factor that controls the expression of numerous antioxidant and cytoprotective genes. Under normal conditions, NRF2 is targeted for degradation by KEAP1 (Kelch-like ECH-associated protein 1); however, under oxidative stress or when KEAP1 is mutated (as frequently occurs in lung cancers), NRF2 accumulates and activates its target genes [koppula-2022-coq-fsp1-abstract][emmanuel-2022-nrf2-target-abstract].

Analysis of NRF2 ChIP-seq data revealed strong association between NRF2 and the FSP1 gene promoter [emmanuel-2022-nrf2-target-abstract]. Two antioxidant response elements (AREs), which are canonical NRF2 binding motifs, have been identified in the FSP1 promoter region, and ChIP-qPCR assays confirmed increased NRF2 binding to these AREs upon KEAP1 knockout [emmanuel-2022-nrf2-target-abstract]. Consequently, KEAP1 mutations, which are common in non-small cell lung cancer (NSCLC), lead to constitutive NRF2 activation and elevated FSP1 expression, contributing to ferroptosis and radiation resistance [koppula-2022-coq-fsp1-abstract].

The original identification of PRG3 (AIFM2) as a p53-responsive gene indicates that p53 can also regulate FSP1 expression [ohiro-2002-prg3-abstract]. A p53-responsive element was identified in the PRG3 gene, and expression was induced by activation of endogenous p53 [ohiro-2002-prg3-abstract]. This adds complexity to FSP1 regulation in cancer contexts where p53 is frequently mutated.

Myristoylation of FSP1 is also subject to regulation. N-myristoyltransferase 2 (NMT2) is the enzyme responsible for FSP1 myristoylation, and NADPH has been shown to interact with NMT2 and upregulate N-myristoylated FSP1 levels. This creates a connection between cellular NADPH levels and FSP1 membrane localization, linking metabolic state to ferroptosis sensitivity.

## 8. Therapeutic Implications and Cancer Relevance

The discovery that FSP1 mediates ferroptosis resistance has profound implications for cancer therapy. FSP1 expression levels correlate with ferroptosis resistance across hundreds of cancer cell lines, and the protein is highly expressed in various tumors [bersuker-2019-coq-oxidoreductase-abstract]. In lung cancer particularly, FSP1 expression is elevated in tumors with KEAP1 mutations, contributing to both chemotherapy and radiation resistance [koppula-2022-coq-fsp1-abstract].

The first FSP1-specific inhibitor, iFSP1, was identified through counter-screening approaches and inhibits human FSP1 with an EC50 of approximately 103 nM [bersuker-2019-coq-oxidoreductase-abstract]. In preclinical models, iFSP1 effectively induced ferroptosis in hepatocellular carcinoma (HCC) cells and suppressed tumor growth while also enhancing anti-tumor immune responses by increasing immune infiltration of dendritic cells, macrophages, and T cells. The combination of FSP1 inhibition with immune checkpoint inhibitors shows synergistic effects.

A novel class of FSP1 inhibitors, the 3-phenylquinazolinones (exemplified by icFSP1), was identified through small molecule library screening [nakamura-2023-phase-separation-abstract]. Unlike iFSP1, which competitively inhibits FSP1 enzymatic activity, icFSP1 promotes FSP1 phase separation and condensate formation, displacing FSP1 from membranes and thereby preventing its anti-ferroptotic function [nakamura-2023-phase-separation-abstract]. This mechanism requires FSP1's N-terminal myristoylation and intrinsically disordered regions. Importantly, icFSP1 impairs tumor growth in vivo and induces FSP1 condensates within tumors, representing a novel therapeutic strategy [nakamura-2023-phase-separation-abstract].

The combination of FSP1 inhibitors with GPX4 inhibitors shows synergistic effects in inducing ferroptosis, as cancer cells must then rely on neither defense pathway [doll-2019-fsp1-glutathione-abstract]. Similarly, combined inhibition of FSP1 and DHODH synergistically promotes ferroptosis by disabling both plasma membrane and mitochondrial CoQ10 reduction. These combination strategies are particularly relevant for cancers with KEAP1 mutations or high basal ferroptosis resistance.

Recent in vivo studies using genetically engineered mouse models have provided compelling evidence for FSP1's role in tumor biology. In lung adenocarcinoma models, tumor-specific loss-of-function of FSP1 resulted in increased lipid peroxidation and robust suppression of tumorigenesis, confirming that lung tumors are highly sensitive to ferroptosis. Importantly, across multiple preclinical models, FSP1 was required for ferroptosis protection in vivo but not in vitro, underscoring a heightened need to buffer lipid peroxidation under physiological conditions. High FSP1 expression is linked to worse prognosis in human lung adenocarcinoma, supporting its potential as both a therapeutic target and prognostic biomarker.

## 9. FSP1 in Neurodegeneration

Beyond cancer, ferroptosis has emerged as a significant contributor to neurodegenerative diseases, and FSP1's role as a ferroptosis suppressor has implications for understanding neurological pathology. The brain presents a unique environment for ferroptosis regulation due to its high oxygen consumption, abundant polyunsaturated fatty acids, and robust iron utilization for neurotransmitter synthesis and myelin formation, making the central nervous system especially vulnerable to ferroptotic damage.

Ferroptosis has been associated with the pathogenesis of Alzheimer's disease (AD), Parkinson's disease (PD), Huntington's disease, and amyotrophic lateral sclerosis. In AD, iron dysregulation and lipid peroxidation predominate in cortical and hippocampal regions, affecting both neurons and glial cells. In PD, the substantia nigra pars compacta (SNpc), where dopaminergic neurons are concentrated, shows particular susceptibility to ferroptotic damage. Regional differences in the expression of ferroptosis regulators, including FSP1, GPX4, and system Xc−, likely underlie these distinct regional vulnerabilities. Notably, diseases associated with AIFM2/FSP1 in curated databases include ovarian cancer and Parkinson's disease.

The regulation of FSP1 expression by NRF2 is particularly relevant in the neurological context, as NRF2 activation has emerged as a potential neuroprotective strategy. Since FSP1 is a target gene of NRF2, compounds that activate NRF2 signaling could potentially upregulate FSP1 expression and enhance protection against neuronal ferroptosis. This presents opportunities for therapeutic intervention in neurodegenerative conditions where ferroptosis contributes to disease progression.

## 10. Open Questions

Despite significant advances in understanding FSP1 biology, several important questions remain:

**Structural and mechanistic questions:** The crystal structures solved to date are from chicken FSP1, and human FSP1 structures would provide more direct insights into inhibitor design and species-specific differences in iFSP1 sensitivity. The mechanism by which FSP1 promotes ESCRT-III-dependent membrane repair independently of its enzymatic activity is not fully understood.

**Physiological roles beyond ferroptosis:** The original characterization of AMID/PRG3 as a pro-apoptotic protein raises questions about context-dependent functions. Under what conditions, if any, does FSP1 contribute to cell death rather than survival? The observation that oxidoreductase-dead mutants retained apoptotic activity [ohiro-2002-prg3-abstract] suggests functions independent of enzymatic activity that merit further investigation.

**Lipid droplet function:** The recent discovery of FSP1's role in protecting lipid droplets from neutral lipid peroxidation opens new avenues of investigation. How does FSP1 localization to lipid droplets versus plasma membrane affect its function, and how is this distribution regulated?

**Phase separation biology:** The discovery that FSP1 can undergo phase separation when displaced from membranes raises questions about whether this represents purely a loss-of-function phenotype or whether FSP1 condensates have biological functions [nakamura-2023-phase-separation-abstract].

**Therapeutic development:** The first-generation FSP1 inhibitor iFSP1 has limitations including species specificity (poor activity against mouse FSP1) and unfavorable pharmacological properties. Development of improved inhibitors suitable for clinical translation remains an active area of research. The identification of species-independent inhibitors (viFSP1) targeting the NAD(P)H-binding pocket represents progress in this direction.

**Biomarker potential:** Whether FSP1 expression levels could serve as predictive biomarkers for ferroptosis-inducing therapies remains to be validated in clinical settings. The correlation between FSP1 expression and ferroptosis resistance in cell lines needs confirmation in patient tumors.

**Immune implications:** Preliminary data suggest that FSP1 inhibition enhances anti-tumor immune responses, but the mechanisms linking ferroptosis to immunogenic cell death and immune activation require further investigation.

## 11. References

1. **[doll-2019-fsp1-glutathione-abstract]** Doll S, Freitas FP, Shah R, Aldrovandi M, et al. FSP1 is a glutathione-independent ferroptosis suppressor. *Nature*. 2019;575(7784):693-698. PMID: 31634899. DOI: 10.1038/s41586-019-1707-0

2. **[bersuker-2019-coq-oxidoreductase-abstract]** Bersuker K, Hendricks JM, Li Z, Magtanong L, Ford B, Tang PH, Roberts MA, Tong B, Maimone TJ, Zoncu R, Bassik MC, Nomura DK, Dixon SJ, Olzmann JA. The CoQ oxidoreductase FSP1 acts parallel to GPX4 to inhibit ferroptosis. *Nature*. 2019;575(7784):688-692. PMID: 31634900. PMCID: PMC6883167. DOI: 10.1038/s41586-019-1705-2

3. **[mishima-2022-vitamin-k-abstract]** Mishima E, Ito J, Wu Z, Nakamura T, Wahida A, Doll S, et al. A non-canonical vitamin K cycle is a potent ferroptosis suppressor. *Nature*. 2022;608(7924):778-783. PMID: 35922516. DOI: 10.1038/s41586-022-05022-3

4. **[lv-2023-structural-insights-abstract]** Lv Y, Liang C, Sun Q, Zhu J, Xu H, Li X, Li YY, Wang Q, Yuan H, Chu B, Zhu D. Structural insights into FSP1 catalysis and ferroptosis inhibition. *Nature Communications*. 2023;14:5933. PMID: 37739943. DOI: 10.1038/s41467-023-41626-7

5. **[wu-2002-amid-abstract]** Wu M, Xu LG, Li X, Zhai Z, Shu HB. AMID, an apoptosis-inducing factor-homologous mitochondrion-associated protein, induces caspase-independent apoptosis. *Journal of Biological Chemistry*. 2002;277(28):25617-25623. PMID: 11980907. DOI: 10.1074/jbc.M202285200

6. **[ohiro-2002-prg3-abstract]** Ohiro Y, Garkavtsev I, Kobayashi S, Sreekumar KR, Nantz R, Higashikubo BT, Duffy SL, Higashikubo R, Usheva A, Gius D, Kley N, Horikoshi N. A novel p53-inducible apoptogenic gene, PRG3, encodes a homologue of the apoptosis-inducing factor (AIF). *FEBS Letters*. 2002;524(1-3):163-171. PMID: 12135761. DOI: 10.1016/s0014-5793(02)03049-1

7. **[nakamura-2023-phase-separation-abstract]** Nakamura T, Hipp C, Mourão ASD, Borggräfe J, Aldrovandi M, Henkelmann B, Wanninger J, Mishima E, Lytton E, Emler D, Proneth B, Sattler M, Conrad M. Phase separation of FSP1 promotes ferroptosis. *Nature*. 2023;619(7969):371-377. PMID: 37380771. DOI: 10.1038/s41586-023-06255-6

8. **[koppula-2022-coq-fsp1-abstract]** Koppula P, Lei G, Zhang Y, Yan Y, Mao C, Kondiparthi L, Shi J, Liu X, Horbath A, Das M, Li W, Poyurovsky MV, Olszewski K, Gan B. A targetable CoQ-FSP1 axis drives ferroptosis- and radiation-resistance in KEAP1 inactive lung cancers. *Nature Communications*. 2022;13(1):2206. PMID: 35459868. DOI: 10.1038/s41467-022-29905-1

9. **[emmanuel-2022-nrf2-target-abstract]** Emmanuel N, Li H, Chen J, Zhang Y. FSP1, a novel KEAP1/NRF2 target gene regulating ferroptosis and radioresistance in lung cancers. *Oncotarget*. 2022;13:1136-1139. PMID: 36264074. DOI: 10.18632/oncotarget.28301

10. **[nakamura-2023-integrated-screens-abstract]** Nakamura T, Mishima E, Yamada N, Mourão ASD, Trümbach D, Doll S, Wanninger J, Lytton E, Sennhenn P, Xavier da Silva TN, Friedmann Angeli JP, Sattler M, Proneth B, Conrad M. Integrated chemical and genetic screens unveil FSP1 mechanisms of ferroptosis regulation. *Nature Structural & Molecular Biology*. 2023;30(11):1806-1815. PMID: 37957306. PMCID: PMC10643123. DOI: 10.1038/s41594-023-01136-y

11. **[dasilva-2023-ifsp1-inhibition-abstract]** Xavier da Silva TN, Schulte C, Alves AN, Maric HM, Friedmann Angeli JP. Molecular characterization of AIFM2/FSP1 inhibition by iFSP1-like molecules. *Cell Death & Disease*. 2023;14(4):281. PMID: 37080964. DOI: 10.1038/s41419-023-05787-z


## Citations

1. bersuker-2019-coq-oxidoreductase-abstract.md
2. bersuker-2019-coq-oxidoreductase-summary.md
3. dasilva-2023-ifsp1-inhibition-abstract.md
4. doll-2019-fsp1-glutathione-abstract.md
5. doll-2019-fsp1-glutathione-summary.md
6. emmanuel-2022-nrf2-target-abstract.md
7. koppula-2022-coq-fsp1-abstract.md
8. lv-2023-structural-insights-abstract.md
9. lv-2023-structural-insights-summary.md
10. mishima-2022-vitamin-k-abstract.md
11. mishima-2022-vitamin-k-summary.md
12. nakamura-2023-integrated-screens-abstract.md
13. nakamura-2023-phase-separation-abstract.md
14. nakamura-2023-phase-separation-summary.md
15. ohiro-2002-prg3-abstract.md
16. wu-2002-amid-abstract.md
17. wu-2002-amid-summary.md