---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-24T23:26:16.330469'
end_time: '2025-11-24T23:29:09.622335'
duration_seconds: 173.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GADD45G
  gene_symbol: GADD45G
  uniprot_accession: O95257
  protein_description: 'RecName: Full=Growth arrest and DNA damage-inducible protein
    GADD45 gamma; AltName: Full=Cytokine-responsive protein CR6; AltName: Full=DNA
    damage-inducible transcript 2 protein; Short=DDIT-2;'
  gene_info: Name=GADD45G; Synonyms=CR6, DDIT2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the GADD45 family. .
  protein_domains: GADD45. (IPR024824); Ribosomal_eL30-like_sf. (IPR029064); Ribosomal_eL8/eL30/eS12/Gad45.
    (IPR004038); Ribosomal_L7Ae (PF01248)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 46
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O95257
- **Protein Description:** RecName: Full=Growth arrest and DNA damage-inducible protein GADD45 gamma; AltName: Full=Cytokine-responsive protein CR6; AltName: Full=DNA damage-inducible transcript 2 protein; Short=DDIT-2;
- **Gene Information:** Name=GADD45G; Synonyms=CR6, DDIT2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the GADD45 family. .
- **Key Domains:** GADD45. (IPR024824); Ribosomal_eL30-like_sf. (IPR029064); Ribosomal_eL8/eL30/eS12/Gad45. (IPR004038); Ribosomal_L7Ae (PF01248)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GADD45G" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GADD45G' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GADD45G** (gene ID: GADD45G, UniProt: O95257) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me carefully review this query and plan my response.

The user is asking me to research the gene GADD45G (UniProt accession O95257) in Homo sapiens. This is a critical research request that requires me to verify I'm researching the correct gene and provide a comprehensive, well-cited report.

Let me check the verification steps:
1. Gene symbol: GADD45G - This matches the target
2. Protein description: Growth arrest and DNA damage-inducible protein GADD45 gamma - The search results extensively cover this
3. Organism: Homo sapiens (Human) - Confirmed in my search results
4. Protein family: GADD45 family - The search results extensively discuss the GADD45 family
5. Key domains: GADD45, Ribosomal_eL30-like_sf, etc. - Confirmed in the structural analyses

Looking at my search results, I have extensive high-quality information:
- Multiple sources on structure and function [1, 19, 22, 25, 49]
- Cell cycle regulation mechanisms [9, 21, 24, 44, 47]
- Tumor suppression roles [3, 20, 43, 46]
- Sexual development [14, 17]
- Neurite outgrowth and neurodevelopment [8, 32, 35]
- Immune function [2, 6, 11, 16, 42, 48, 51]
- Stress responses [12, 33, 57]
- Myeloproliferative neoplasm pathogenesis [13, 31, 38, 41]
- Memory and learning [26, 29]
- Kidney disease [45]
- DNA repair [7, 10]
- Interactions with other proteins [7, 10, 15, 18, 22, 55, 58]
- Recent mechanistic studies on signaling pathways [8, 35]


- The search results are comprehensive and recent (many from 2024-2025 and late 2023). I can structure a detailed report covering the protein's molecular architecture, stress-response mechanisms including cell cycle arrest and DNA repair pathways, signaling cascades through p38/JNK and NF-κB, tissue-specific expression patterns, developmental functions in sexual determination and neurogenesis, tumor suppressive activities, immune regulatory roles, and disease associations including myeloproliferative neoplasms and kidney pathology.
</think>

# Comprehensive Molecular and Functional Analysis of GADD45G (Growth Arrest and DNA Damage-inducible Gamma) in Human Physiology and Pathology

**Summary of Key Findings:** GADD45G is a multifunctional stress-response protein encoded on human chromosome 9 that serves as a critical molecular sensor for cellular damage and stress conditions. This highly conserved 18 kilodalton acidic protein responds to environmental insults including ionizing radiation, DNA-damaging chemicals, and physiological stressors by mediating cell cycle arrest, promoting DNA repair processes, facilitating apoptosis, and regulating immune responses. GADD45G functions through dynamic protein-protein interactions with cell cycle regulators, DNA repair machinery, and mitogen-activated protein kinase cascades, with its activity regulated upstream by the nuclear factor-kappa B transcription factor. Recent investigations have revealed that reduced expression of GADD45G is frequently observed in multiple cancer types through epigenetic silencing mechanisms, establishing the protein as a novel tumor suppressor. Additionally, emerging research demonstrates essential roles for GADD45G in human sexual development, neural differentiation, and immune cell regulation, highlighting the protein as a multifaceted regulator with broad implications for human development, aging, and disease pathogenesis.

## Molecular Structure, Classification, and Evolutionary Context

GADD45G belongs to the growth arrest and DNA damage-inducible 45 protein family, which comprises three highly related members designated GADD45α, GADD45β, and GADD45γ (GADD45G) in humans[1][2][51]. The GADD45 family is characterized by small acidic proteins with a molecular weight of approximately 18 kilodaltons and exhibit 55 to 57 percent overall amino acid identity among family members[51]. These proteins are evolutionarily conserved across diverse organisms, from mammals to Drosophila, indicating fundamental biological importance that extends across eukaryotic lineages[33]. The remarkably high level of sequence conservation among GADD45 family members, particularly within specific functional domains, suggests that these proteins evolved early in eukaryotic history to perform critical cellular housekeeping functions related to stress response and genomic surveillance[51].

The three-dimensional structure of GADD45γ has been determined through X-ray crystallography, revealing an intricate architecture composed of an αβα sandwich configuration with a central five-stranded mixed β-sheet flanked by α-helices on both sides[22][55][58]. Specifically, the structure comprises five defined α-helices (designated α1 through α5) packed around a central core of β-strands[22][55][58]. The crystal structure reveals that GADD45γ forms functional dimers through a four-helix bundle interface involving conserved helices α2 and α3[22][55][58]. This dimerization interface is composed predominantly of hydrophobic residues in the region spanning residues Ile-76 to Leu-80 of helix α3 and residues Tyr-44 to Lys-48 of helix α2, with these highly conserved residues representing the most similar regions across all GADD45 family members[22][55][58]. The central region of the GADD45γ dimer contains a highly acidic patch where the protein mediates critical protein-protein interactions with cell cycle control proteins including cdc2, proliferating cell nuclear antigen (PCNA), and the cyclin-dependent kinase inhibitor p21[1][19][22][25][49]. Notably, the parallel dimer isoform represents the active functional form of GADD45γ[1][19][25][49]. Structural analysis has further demonstrated that GADD45 proteins possess sequence homology with the L7Ae/L30e/S12e superfamily of ribosomal proteins, suggesting potential nucleic acid binding capabilities that have been confirmed through biochemical studies[54].

Dimerization of GADD45γ is not merely a structural consequence but rather an absolute requirement for the protein's biological functions. Cell-based assays employing point mutations designed to compromise dimerization while preserving monomer structural integrity conclusively demonstrate that dimerization is essential for growth inhibition activity[22][55]. Specifically, mutation of leucine 80 to glutamic acid (L80E) blocks dimerization without compromising the three-dimensional fold of individual monomers, yet this mutation completely abolishes the protein's ability to inhibit cell growth[22][55]. These findings indicate that the dimer interface itself is directly required for functional efficacy, rather than dimerization serving merely as a mechanism for protein trafficking or localization[22][55].

## Tissue Distribution and Subcellular Localization

GADD45G exhibits a distinctive pattern of tissue distribution across human tissues, with quantitative variations reflecting differential physiological demands and stress exposure across organs[1][25][49]. The gene achieves highest expression levels in skeletal muscle, kidney, and liver tissues, tissues that experience substantial metabolic demands and oxidative stress[1][25][49]. In contrast, GADD45G maintains lower expression levels in the heart, brain, spleen, lung, and testis under basal conditions[1][25][49]. The protein is notably highly expressed in placental tissue, where it likely plays critical roles in managing the physiological stresses associated with fetal development and placental function[1][25][28][49]. In embryonic mouse tissues, Gadd45g expression patterns are observed in neural structures including the neural tube, cranial ganglia, dorsal root ganglia, and dorsal midbrain, indicating important functions during nervous system development[1][25][49]. During pituitary gland development, GADD45G functions as a growth suppressor, with loss of expression frequently detected in pituitary cancerous masses, suggesting tumor-suppressive functions in endocrine tissues[1].

At the subcellular level, GADD45G localizes to both the nucleus and cytoplasm, with the protein being highly acidic with a calculated isoelectric point between 4.0 and 4.2[51]. This dual localization permits the protein to exert regulatory functions in both nuclear processes involving DNA transactions and cytoplasmic signaling cascades that control cell survival and apoptosis[51]. The relatively low abundance of GADD45G under basal conditions in normal cells allows for rapid, dynamic responses to stress stimuli through swift transcriptional activation and posttranscriptional regulation[51]. This low basal expression combined with stress-inducible upregulation enables GADD45G to function as an effective molecular switch that can discriminate between normal physiological conditions and pathological stress states[2][6].

## Primary Function in Stress Response and Cell Cycle Checkpoint Control

GADD45G functions fundamentally as a cellular stress sensor that becomes rapidly induced in response to diverse forms of genotoxic and physiological stress[2][6][16][51]. The protein responds to environmental stresses by mediating activation of the p38 and c-Jun N-terminal kinase (JNK) mitogen-activated protein kinase pathways through interaction with the mitogen-activated protein kinase kinase kinase 4 (MTK1/MEKK4) kinase[1][4][19][25][49]. GADD45G is itself regulated upstream by the nuclear factor-kappa B (NF-κB) transcription factor[1][19][25][49]. The primary molecular function of GADD45G involves inhibiting cellular proliferation and preventing the replication of DNA containing unrepaired damage, thereby serving as a critical defense mechanism that maintains genomic integrity under stress conditions[1][2][6].

The most prominent function of GADD45G in cell cycle regulation involves activation of the G2/M checkpoint, the critical control point between the G2 phase of interphase and mitotic entry[1][9][19][24][25][49]. At the molecular level, GADD45G inhibits the kinase activity of the cdc2 (cyclin-dependent kinase 1) and cyclin B1 complex, which is absolutely required for transition from G2 to M phase[1][9][24][25][44][47]. Significantly, GADD45G inhibits cdc2/cyclin B1 kinase activity through a mechanism distinct from that employed by its family members GADD45α and GADD45β. Unlike GADD45α and GADD45β, which promote dissociation of the cdc2/cyclin B1 complex thereby inactivating it, GADD45G inhibits cdc2 kinase activity without disrupting the complex structure[47]. This distinction suggests that GADD45γ stabilizes an inactive conformation of the complex rather than promoting its disassembly[47]. This G2/M arrest occurs with a phenotype characteristic of cells arrested in early mitosis, including positive immunostaining with monoclonal antibodies recognizing mitotic phosphoproteins (MPM2 positivity), accumulation of cells with 4n DNA content, and in some cells, centrosome separation[9][21][44]. Experimental evidence demonstrates that increased expression of GADD45G via microinjection of expression vectors into primary human fibroblasts arrests approximately 44 percent of cells at the G2/M boundary at 24 hours, with this percentage increasing to approximately 83 percent by 72 hours post-injection[9][21][44].

The G2/M checkpoint function of GADD45G is particularly interesting in its stimulus specificity. Genetic and functional evidence demonstrates that GADD45G mediates G2/M checkpoints specifically in response to ultraviolet radiation and chemical mutagens such as methyl methanesulfonate, but not in response to ionizing radiation[9][21][44]. This stimulus-specificity indicates that mammalian cells employ multiple distinct G2/M checkpoint mechanisms, with GADD45G being essential for some but not all damage-induced checkpoints[9][44]. This observation suggests that the cell has evolved specialized stress-sensing pathways that discriminate between different types of DNA damage and employ appropriate checkpoint responses. For ultraviolet radiation or methyl methanesulfonate-induced damage, GADD45G-deficient cells are unable to mount an effective G2/M checkpoint, while cells with reduced endogenous GADD45G expression show impaired but not completely eliminated G2/M arrest following ultraviolet exposure[9][44].

## Molecular Interactions Mediating Cell Cycle Arrest and DNA Repair Functions

GADD45G exerts its effects through a complex interplay of physical interactions with multiple cellular proteins implicated in cell cycle regulation and stress response[12][47][51]. The protein directly interacts with the proliferating cell nuclear antigen (PCNA), a processivity factor essential for DNA replication and DNA repair processes[7][10][12][47]. The interaction between GADD45G and PCNA involves direct binding, with GADD45G competing with the cyclin-dependent kinase inhibitor p21 for binding to PCNA[7][10]. This competitive interaction is physiologically significant because p21 blocks the ability of GADD45G to bind to PCNA, suggesting a regulatory hierarchy in which different stress response proteins vie for access to PCNA[7]. Additionally, p21 appears to disrupt PCNA trimers whereas GADD45G has a lesser effect on trimer stability[7]. The interaction with PCNA positions GADD45G at sites of DNA damage undergoing repair, consistent with a role in coordinating DNA repair with cell cycle arrest[12][47]. The recruitment of GADD45G to PCNA at DNA lesions facilitates DNA excision repair processes[34].

GADD45G also directly interacts with cdc2/cyclin B1 complexes through physical binding to cdc2 itself, not to cyclin B1[12][47]. This selective binding allows GADD45G to specifically inhibit the kinase activity of the mitosis-promoting factor complex[12][47]. The interaction domain maps to the central region of GADD45G containing the highly acidic patch formed in the dimer interface[22][58]. GADD45G interacts with the cyclin-dependent kinase inhibitor p21, which is itself a universal cyclin-dependent kinase inhibitor involved in both G1/S and G2/M cell cycle arrest[12][47]. All three GADD45 family members interact with p21, and this interaction likely provides an additional layer of inhibition of cyclin-dependent kinases beyond the direct GADD45G-cdc2 interaction[12][47].

The interaction of GADD45G with MAP3K4 (mitogen-activated protein kinase kinase kinase 4), also known as MEKK4, represents a critical mechanistic link in GADD45G-mediated stress signaling[1][15][18][19][25][49]. GADD45G binding to MTK1/MEKK4 induces a conformational transition from a monomeric or inactive state to an active dimeric form that undergoes autophosphorylation at threonine 1493, leading to kinase activation[15][18]. This GADD45G-mediated activation of MEKK4 results in subsequent phosphorylation and activation of downstream p38 and JNK mitogen-activated protein kinases[15][18]. The MEKK4 activation represents one of the primary mechanisms by which GADD45G transduces stress signals to downstream effector pathways.

## Signaling Pathways and Downstream Effector Mechanisms

The p38 mitogen-activated protein kinase pathway represents one of the primary signaling cascades through which GADD45G mediates cellular responses to stress[2][6][11][16][42][48][51]. Multiple lines of evidence establish that GADD45G activates p38 MAPK through interaction with the upstream kinase MEKK4[2][11][16][42][48]. The activation of p38 MAPK has profound consequences for cellular physiology, including altered gene expression patterns, cell cycle control, and immune responses. In T cells specifically, GADD45β and GADD45γ enhance p38 MAPK activity through MEKK4 activation, leading to increased production of interferon-gamma (IFN-γ) and other pro-inflammatory cytokines[2][11][16][42][48][51]. This p38-mediated pathway proves crucial for T helper 1 (Th1) cell differentiation and immune responses to intracellular pathogens.

Interestingly, GADD45α exhibits opposite effects on p38 MAPK activity compared to GADD45β and GADD45γ[11][42][48]. While GADD45β and GADD45γ enhance kinase activity, GADD45α acts as a negative regulator of p38 MAPK in T cells[11][42][48]. GADD45α restrains T cell p38 activation by inhibiting phosphorylation of p38 at tyrosine residue 323 (Tyr323) and directly blocking Tyr323-phosphorylated p38 activity[11][42][48]. This inhibition occurs through suppression of Zap70 kinase rather than through inhibition of MKK6[11][42]. These opposing effects of GADD45 family members on p38 activity underscore the complexity and isoform-specific regulation of immune responses by this protein family.

The JNK mitogen-activated protein kinase pathway also plays a central role in GADD45G-mediated signaling and stress responses[2][11][16][42][48][51]. Like p38, JNK kinase is activated downstream of MEKK4 through the classical mitogen-activated protein kinase cascade[2][11][16][42][48]. GADD45γ promotes JNK-MAPK signaling pathway activation, with evidence demonstrating that under T cell receptor stimulation, GADD45γ-deficient T helper 1 cells show significantly reduced p38 and JNK MAPK activity, less interferon-gamma production, and deficient activation-induced cell death[11][16][42][48]. The JNK pathway activated by GADD45γ mediates T helper 1 cell functions including the production of pro-inflammatory mediators. In contrast to GADD45γ, GADD45β exerts opposite effects on the JNK pathway, attenuating JNK pathway signaling by blocking TNF-induced MKK7 activation, which sits immediately upstream of JNK[11][42]. This divergent regulation of JNK by different GADD45 family members provides a mechanism for fine-tuning immune responses.

Importantly, NF-κB regulation of GADD45G expression involves complex and sometimes contradictory mechanisms. In some cell types, NF-κB suppresses GADD45α and GADD45γ expression through c-Myc-dependent transcriptional regulation, thereby promoting cancer cell survival[3]. In cancer cells, inhibition of NF-κB results in upregulation of GADD45α and GADD45γ expression, which then mediates apoptosis through JNK pathway activation[3]. The upregulation of GADD45α and γ by NF-κB inhibition correlates with activation of c-Jun N-terminal kinase and induction of programmed cell death in cancer cells[3]. This pathway has important implications for understanding how cancer cells escape apoptosis through NF-κB-mediated suppression of GADD45 expression.

## Role in DNA Repair and Genomic Stability Maintenance

GADD45G participates in DNA repair processes through its interaction with proliferating cell nuclear antigen and its potential involvement in DNA demethylation and recognition of DNA modifications requiring repair[1][7][10][12][26][29]. The protein may recognize 5-methylcytosine as an alteration in DNA that requires repair and can guide rapid demethylation of methylcytosine in the promoter regions of learning-related genes and other stress-responsive genes through DNA repair mechanisms[1][29]. GADD45 proteins physically interact with thymine-DNA glycosylase (TDG), and evidence suggests GADD45 may promote TDG activity in the conversion of 5-methylcytosine to cytosine during active demethylation processes[29]. This epigenetic regulatory function represents an important mechanism by which GADD45G influences gene expression patterns in response to cellular stress and environmental stimuli.

The interaction of GADD45G with histone acetylation states and chromatin accessibility provides another mechanism through which the protein influences DNA repair and transcriptional regulation. GADD45G is recruited to mononucleosomes that have been altered by histone acetylation or ultraviolet radiation, where it interacts with core histones to alter DNA accessibility and facilitate relaxation and cleavage activity of topoisomerase[34]. This recruitment to damaged chromatin positions GADD45G to facilitate DNA repair processes in the context of chromatin structure. The recruitment of GADD45G to DNA lesion sites through PCNA interaction and the protein's subsequent promotion of histone modifications that enhance DNA accessibility represent interconnected mechanisms that coordinate DNA damage recognition with repair execution.

## Unique Role in Human-Specific Brain Development and Neurite Outgrowth

A particularly fascinating aspect of GADD45G biology involves its critical role in human-specific brain development that has contributed to the evolution of human cognitive capabilities[1][8][19][25][35][49]. Deletion of an enhancer sequence located near the GADD45G gene is associated with increased proliferation of neuronal cells, an effect that could account for part of the fundamental difference in neural development between humans and other primate species[1][19][35][49]. This human-specific regulatory deletion reduces GADD45G expression in the forebrain, thereby permitting more extensive brain growth and neuronal proliferation during human development[1][19][35][49]. This suggests that the unique regulation of GADD45G through evolutionarily derived enhancer deletion represents a molecular mechanism contributing to the expansion of human brain size and the development of human-specific cognitive capacities.

The GADD45G/p38 MAPK/CDC25B signaling pathway promotes neurite outgrowth in human neurons by facilitating microtubule polymerization, a fundamental process in neural network formation[8][35]. During neural network formation, particularly in the human fetal brain, active neurite outgrowth proves essential for establishing neuronal connectivity and functional brain circuits[8][35]. Neurite elongation fundamentally requires tubulin polymerization to construct microtubules that form the neuronal cytoskeleton[8][35]. The signaling mechanism involves GADD45G activation of p38 MAPK, which then phosphorylates and activates CDC25B phosphatase[8][35]. Activated CDC25B then catalyzes dephosphorylation of phosphorylated collapsin response mediator protein 2 (pCRMP2), which reduces phosphorylated CRMP2 levels and thereby promotes microtubule assembly[8][35]. This pathway ultimately enhances tubulin polymerization and promotes neurite outgrowth of human neuronal cells[8][35].

Experimental evidence demonstrates that GADD45G is highly expressed in developing human cerebral specimens, with expression patterns showing substantial temporal elevation during the period of active neurogenesis and neuronal differentiation[8][35]. In developing human fetal brain samples, GADD45G expression increased substantially during the period when neuronal differentiation and maturation actively proceed[8][35]. The GSK3β inhibitor-mediated differentiation of neural progenitor cells leads to marked induction of GADD45G expression coinciding with enhanced neurite outgrowth[8][35]. Notably, GADD45G expression reaches highest levels during early embryonic periods when neurogenesis is most active, suggesting that GADD45G plays a critical role in determining the functional and morphological characteristics of developing neurons[8][35]. Pharmacological enhancement of p38 MAPK/CDC25B signaling through use of the RK-682 phosphatase inhibitor, which inhibits phosphatases acting on p38 MAPK, promotes microtubule polymerization and neurite outgrowth by enhancing this signaling cascade[8][35].

GADD45G acts redundantly with GADD45A in controlling cell growth and enabling cells to transition from pluripotency toward differentiation during embryonic development[1][19][25][49]. In the Xenopus model system, GADD45G and GADD45A knockdowns are associated with improper gastrulation, defective head growth, and shortened embryonic axes[1][19][25][49]. The knockdown of both proteins together impairs the normal developmental transitions that allow cells to move from pluripotent states toward more specialized differentiated phenotypes[1][25][49].

## Critical Role in Sexual Development and Testis Determination

GADD45G plays an absolutely essential role in male sexual development that was revealed through knockout studies demonstrating that GADD45G deficiency causes profound disorders of sexual development in mammals[14][17]. In the male sexual development pathway, GADD45G is essential for activating the sex-determining region Y gene (SRY), leading to proper formation of the gonads and sex determination[1][19][25][49]. This could occur through GADD45G interaction with the p38 MAPK signaling pathway[1][19][25][49]. GADD45G−/− mice on a mixed 129/C57BL/6 genetic background showed varying degrees of disorders of sexual development, ranging from male infertility to an intersex phenotype to complete gonadal dysgenesis[14][17]. In contrast, when Gadd45g−/− mice were maintained on a pure C57BL/6 genetic background, all Gadd45g−/− XY mice were born as completely sex-reversed XY-females[14][17]. Importantly, lack of GADD45A and/or GADD45B did not affect primary sex determination or testis development, demonstrating that GADD45G possesses a unique function in this developmental process not shared by its family members[14][17].

The molecular mechanism of GADD45G-mediated sex determination involves the regulation of SRY expression. GADD45G expression occurs at similar levels in both female and male embryonic gonads and peaks around the time of sex differentiation at 11.5 days post-coitum[14][17]. The molecular cause of sex reversal in Gadd45g−/− XY mice involves the failure of Gadd45g-deficient XY gonads to achieve the SRY expression threshold necessary for testis differentiation, resulting instead in ovary and Müllerian duct development[14][17]. When SRY expression fails to reach threshold levels, the male developmental pathway cannot be initiated, and instead the female developmental pathway proceeds with granulosa cell differentiation and ovary formation[14][17]. Reduction of SOX9 expression, a downstream target of SRY signaling critical for Sertoli cell differentiation, causes primary male-to-female sex reversal in both mice and humans[14][17].

The molecular pathway through which GADD45G promotes SRY expression involves the p38 MAPK signaling cascade. Many known biological functions of GADD45G are mediated by its ability to bind and activate MAP3K4, and previous research by Bogani and colleagues demonstrated that MAP3K4-deficient mice exhibit male-to-female sex reversal caused by decreased SRY expression[14][17]. Sex reversal in GADD45G-deficient animals was recently associated with reduced phosphorylation of p38 MAPK and GATA4, a transcription factor involved in sex determination, suggesting that GADD45G is needed to promote MAP3K4-mediated activation of p38 signaling in murine embryonic gonadal somatic cells[14][17]. The precise molecular mechanism by which p38 MAPK phosphorylation leads to increased SRY transcription remains to be fully elucidated, but the pathway likely involves phosphorylation of GATA4 and other sex-determination-associated transcription factors.

The genetic basis of human male-to-female sex reversal remains unexplained in the majority of cases. GADD45G stands as a promising candidate gene in human non-syndromic male infertility and in partial or complete male-to-female primary sex reversal in 46,XY individuals[14][17]. The complete sex reversal phenotype observed in Gadd45g−/− mice combined with the fact that GADD45G is a key upstream activator of the master regulator SRY suggests substantial relevance to human sexual development disorders[14][17].

## Tumor Suppression Functions and Epigenetic Inactivation in Cancer

GADD45G functions as a tumor suppressor gene that is frequently inactivated through epigenetic mechanisms in multiple human cancer types[20][43][46]. In response to stress shock including heat shock and ultraviolet irradiation, GADD45G inhibits cell growth and induces apoptosis[20][43][46]. However, despite being ubiquitously expressed in all normal adult and fetal tissues, GADD45G undergoes transcriptional silencing or down-regulation and promoter hypermethylation in numerous tumor cell lines[20][43][46]. The CpG island of GADD45G, located in the commonly deleted region 9q22 of the human genome, becomes hypermethylated at frequencies of 85 percent in non-Hodgkin's lymphoma (11 of 13 cell lines), 50 percent in Hodgkin's lymphoma (3 of 6 cell lines), 73 percent in nasopharyngeal carcinoma (8 of 11 cell lines), 50 percent in cervical carcinoma (2 of 4 cell lines), 29 percent in esophageal carcinoma (5 of 17 cell lines), and 40 percent in lung carcinoma (2 of 5 cell lines)[20][43][46]. In contrast, GADD45G promoter hypermethylation is not detected in any immortalized normal epithelial cell lines, normal tissues, or peripheral blood mononuclear cells[20][43][46]. Aberrant methylation has been further frequently detected in primary lymphomas, although less frequently in primary carcinomas[20][43][46].

The silencing of GADD45G through epigenetic mechanisms can be reversed by 5-aza-2'-deoxycytidine treatment or genetic double knockout of the DNA methyltransferases DNMT1 and DNMT3B, indicating that a direct epigenetic mechanism mediated by DNA methylation underlies GADD45G silencing in these tumors[20][43][46]. Importantly, genetic inactivation of GADD45G through mutations in the coding sequence proves extremely rare, occurring in only 1 of 25 cell lines examined, indicating that genetic mutations rather than epigenetic silencing represent the infrequent mechanism of GADD45G inactivation[20][43][46]. This observation highlights that cancer cells preferentially employ reversible epigenetic modifications to silence GADD45G rather than accumulating irreversible genetic mutations.

GADD45G can be induced by heat shock or ultraviolet irradiation in unmethylated cell lines, yet this stress response is abolished when GADD45G promoter becomes hypermethylated[20][43][46]. Ectopic expression of GADD45G strongly suppresses tumor cell growth and colony formation in silenced cell lines, demonstrating that GADD45G possesses functional tumor-suppressive capacity[20][43][46]. These results establish GADD45G as a functional tumor suppressor that is frequently inactivated through epigenetic mechanisms in multiple cancers[20][43][46].

In hepatocellular carcinoma specifically, GADD45G acts as a tumor suppressor by promoting cell death or growth arrest through negative regulation of the JAK-STAT3 signaling pathway[1][19][27][30][49]. When GADD45G expression becomes low in liver cancer cells, the cells may bypass the growth arrest stage and continue proliferating uncontrollably[1][19][27][30][49]. The loss of GADD45G expression in hepatocellular carcinoma cell lines represents a pathogenic event allowing evasion of growth-suppressive pathways. Studies have demonstrated that GADD45G functions to negatively regulate JAK-STAT3 signaling and inhibit hepatocellular carcinoma growth, establishing a clear molecular mechanism for GADD45G-mediated tumor suppression in liver cancer[27][30].

Additionally, GADD45G functions as a growth suppressor in pituitary gland tissues, with loss of GADD45G expression frequently detected in pituitary cancerous masses[1]. In prostate cancer, GADD45G acts as a tumor suppressor with expression frequently reduced in cancerous cells[1]. Notably, vitamin D can induce the expression of GADD45G in prostate cancer cells, suggesting that GADD45G could potentially represent a therapeutic target for prostate cancer intervention[1].

## Immune Regulation and Inflammatory Responses

GADD45G plays multifaceted roles in both innate and adaptive immune responses through mechanisms involving p38 and JNK mitogen-activated protein kinase pathway activation[2][6][11][16][42][48][51]. GADD45 proteins modulate innate and adaptive immunity and play broader roles in inflammatory and autoimmune disease pathogenesis[2][6]. The stimulation of T cell receptor signaling increases the levels of GADD45β and GADD45γ in CD4+ T cells, driving inflammatory signaling for T helper 1 differentiation and interferon-gamma expression[2][16][51]. T cells transfected with GADD45β-retrovirus promote interferon-gamma secretion after IL-12 and IL-18 stimulation, thereby driving T helper 1 differentiation[2][6][11][16][51].

GADD45γ becomes strongly induced during T cell activation with expression levels higher in T helper 1 cells than in T helper 2 cells[11][16][42][48][51]. Under T cell receptor stimulation conditions, GADD45γ-deficient T helper 1 cells exhibit reduced p38 and JNK MAPK activity, less interferon-gamma production, and deficient activation-induced cell death[11][16][42][48][51]. Furthermore, lack of GADD45γ in mice reduces contact hypersensitivity responses of T helper 1 cells, with cell responses impaired even in in vivo models[11][16][42][48]. These data establish that GADD45γ mediates T helper 1 cell function by activating p38 and JNK pathways[11][16][42][48].

GADD45 family members promote differentiation of myeloid cells during immune responses. GADD45α and GADD45β promote the differentiation of myeloid cells and inhibit the proliferation of these terminally differentiated cells[2][6][16][51]. GADD45α and GADD45β promote recruitment, migration, reactive oxygen species production, phagocytosis, and adhesion of bone marrow-derived macrophages and granulocytes[2][6][16][51]. Notably, GADD45α and GADD45β deficiency led to higher proliferative capacity of immature myeloid cells, suggesting that GADD45 proteins may promote myeloid cell differentiation while preventing expansion of immature progenitor cells[2][6][16][51]. However, GADD45γ is not required for myeloid differentiation[2][16][51].

GADD45β and GADD45γ critically regulate the duration and magnitude of T helper 1-mediated autoimmune responses. CD4+ T cells lacking GADD45β can rapidly expand and invade the central nervous system in response to myelin immunization, provoking exacerbated and prolonged autoimmune encephalomyelitis in mice[59]. This finding indicates that GADD45β acts to limit the proliferation and survival of autoreactive T cells. Most dramatically, mice with compound deficiency in both GADD45β and GADD45γ spontaneously develop signs of autoimmune lymphoproliferative syndrome and systemic lupus erythematosus[59]. These findings identify the GADD45β and GADD45γ-mediated control of effector autoimmune lymphocytes as an attractive novel target for autoimmune disease therapy[59]. The role of GADD45 proteins in preventing excessive T cell activation and controlling self-reactive lymphocyte proliferation represents an important mechanism that prevents autoimmune disease development in normal individuals.

## Stress Response to Environmental and Physiological Stimuli

GADD45G expression is induced by diverse forms of environmental stress and physiological challenge. Environmental stressors including ionizing radiation and chemical mutagens rapidly induce GADD45 gene expression[2][6][16][36][51]. Both messenger RNA and protein levels of GADD45α increase rapidly following X-ray exposure in human cells, with both X-rays and gamma irradiation reported to induce GADD45α expression[16][36][51]. Inflammatory factors also potently induce GADD45 expression patterns. Bacterial endotoxin lipopolysaccharide induces GADD45β expression in vivo across a range of tissues including liver, spleen, lung, intestine, kidney, and heart, and also induces GADD45γ expression in lung tissue[2][16][51].

GADD45G becomes induced by acute hypertonicity stress in mammalian renal cells, a significant physiological challenge faced by cells in the inner medulla of the kidney exposed to hypertonic conditions[1][25][49]. Maximum induction of GADD45G occurs 16-18 hours after the onset of hypertonicity, with GADD45G induced more strongly (7-fold) than GADD45B (3-fold) and GADD45A (2-fold)[1][25][49]. Hypertonicity of various forms including sodium chloride, potassium chloride, sorbitol, or mannitol consistently induces GADD45 transcripts, whereas non-hypertonic hyperosmolality caused by urea has no effect[1][25][49]. This selective induction of GADD45 by true osmotic stress rather than chemical osmolytes suggests specific osmolarity-sensing mechanisms upstream of GADD45 activation[1][25][49]. The mechanism of hypertonic induction involves mRNA stabilization rather than transcriptional activation, as actinomycin D treatment that prevents new transcription does not prevent hypertonic GADD45 induction[1][25][49].

Inflammatory cytokines and immunosuppressive factors also regulate GADD45 expression. Transforming growth factor-beta, an immunosuppressive cytokine, induces GADD45β expression in mouse bone marrow mononuclear cells, lymphocyte cell lines, and mink lung epithelial cells[42]. Induction of GADD45α in placental explants by stressors or inflammatory cytokines can activate the JNK MAPK pathway[16][42][48][51]. These diverse inducers establish GADD45G as a broadly responsive sensor of cellular and physiological stress.

## Association with Kidney Disease and Renal Tubular Injury

Recent clinical evidence demonstrates that urinary GADD45G protein excretion is significantly associated with kidney disease progression in patients with IgA nephropathy, an important form of glomerulonephritis[45]. Univariate Cox regression analysis revealed that urinary GADD45G was significantly associated with deterioration of renal function, with a hazard ratio of 1.63[45]. Kaplan-Meier survival analysis demonstrated a significant difference in event-free survival for renal function deterioration between the highest urinary GADD45G tertile group and other tertile groups[45]. Receiver operating characteristic curve analysis indicated that urinary GADD45G exhibited good performance in predicting renal outcome with an optimal cut-off point of 1.67 μg/g creatinine, achieving a positive predictive value of 36.8 percent and a negative predictive value of 100 percent[45].

Immunohistochemical localization studies revealed that GADD45G is expressed across all pathologic grades of IgA nephropathy and is mainly detected in the cytoplasm of renal tubules, whereas no staining is observed in normal tissues[45]. GADD45G was previously demonstrated to be implicated in renal tubular injury in rodent disease models and plays a critical role in apoptotic pathways of renal tubular cells[45]. The renal cells expressing GADD45G at elevated levels are associated with tubular cell damage[1][25][49]. The data suggest that GADD45G is induced in renal tubular cells from the early pathogenic process of IgA nephropathy, which subsequently contributes to the occurrence of apoptosis of renal tubular cells, thereby leading to worsening of renal function[45].

## Memory, Learning, and Epigenetic Gene Regulation

GADD45γ plays a critical role in the consolidation of associative fear memory in the adult brain by regulating immediate early gene expression through DNA demethylation mechanisms[26]. During fear learning, GADD45γ serves to coordinate immediate early gene expression and subsequent memory consolidation by directing temporally specific changes in active DNA demethylation at promoter regions of plasticity-related immediate early genes[26]. The protein functions through its interaction with DNA double-strand break-mediated changes in DNA methylation[26]. A two-hit model of experience-dependent immediate early gene activity and learning emerges from these studies, comprising first a wave of immediate early gene expression governed by DNA double-strand breaks followed by rapid increase in DNA methylation, and second a wave of immediate early gene expression associated with recruitment of GADD45γ and active DNA demethylation at the same genomic sites[26]. This temporal pattern of demethylation proves necessary for memory consolidation[26].

Learning-induced GADD45γ expression in the prelimbic prefrontal cortex is required for formation of cued fear memory[26]. Specifically, GADD45γ temporally influences learning-induced immediate early gene expression in the prelimbic prefrontal cortex through its interaction with DNA double-strand break-mediated changes in DNA methylation[26]. Cued fear learning led to biphasic peaks of immediate early gene expression in the prelimbic prefrontal cortex, with a first peak occurring immediately after training and a second peak occurring 3-6 hours later[26]. This temporal pattern of double peaks in immediate early gene expression has been observed in earlier investigations showing that two waves of transcription are required for formation of hippocampal-dependent fear memory[26].

GADD45 proteins promote active DNA demethylation at learning-related genes by interacting with thymine-DNA glycosylase and potentially guiding removal of 5-methylcytosine modifications[29]. Through this mechanism, GADD45 facilitates the induction of genes involved in learning-related processes by promoting demethylation of their promoter regions[29]. Reduced methylation of plasticity-related genes including reelin and brain-derived neurotrophic factor has been documented in animal brains that have undergone learning experiences, suggesting that DNA demethylation contributes to memory formation[29].

## Recent Insights into Myeloproliferative Neoplasm Pathogenesis

Recent investigations have identified GADD45g insufficiency as a novel pathogenic driver of myeloproliferative neoplasms, a class of blood cancers arising from hematopoietic stem and progenitor cells[13][31][38][41]. Remarkably, GADD45g expression is expressed at significantly lower levels in patients with myeloproliferative neoplasms compared to normal individuals[13][31][38][41]. Critically, GADD45g expression levels are negatively correlated with higher clonogenic potential and inflammatory cytokine production in patient-derived cells[13][31][38][41]. GADD45g deficiency alone is sufficient to cause myeloproliferative neoplasm pathology in a mouse model, demonstrating a direct causative relationship[13][31][38][41].

GADD45g insufficiency exerts tumor-promoting activities through the activation of the RAC2-PAK1-PI3K-AKT signaling pathway in hematopoietic cells[13][31][38][41]. GADD45g shows direct interaction with RAC2 (a Rho-family small GTPase) but not with the closely related RAC1, despite their considerable homology and functional interchangeability in many contexts[13][31][38][41]. Both GADD45g and RAC2 exhibit perinuclear distribution patterns, with clear areas of colocalization evident in bone marrow cells and cord blood CD34+ cells, whereas RAC1 displays dispersed cellular locations with little perinuclear localization[13][31][38][41]. The distinct cellular localizations of RAC2 and RAC1 appear to be implicated in the specificity of binding selectivity[13][31][38][41].

GADD45g deficiency results in significant enhancement of PAK1 kinase activity in hematopoietic cells[13][31][38][41]. Consistent with these observations from primary murine bone marrow cells, knockdown of GADD45g in human myeloproliferative neoplasm cell lines (HEL and SET-2) resulted in enhanced activities of PI3K and AKT kinases, indicating that GADD45g insufficiency leads to activation of the PI3K-AKT signaling pathway[13][31][38][41]. Furthermore, downregulation of RAC2 by shRNA largely diminished both the activation of PAK1 and the PI3K-AKT cascade caused by GADD45g knockdown, reversing the enhancement of colony-forming capacity and inhibition of apoptosis induced by GADD45g loss[13][31][38][41]. These findings establish that GADD45g deficiency induces myeloproliferative neoplasm pathology through successive activations of RAC2, PAK1, and PI3K-AKT signaling cascades[13][31][38][41].

The molecular expression of GADD45g can be upregulated through epigenetic remodeling approaches. Treatment of myeloproliferative neoplasm cell lines with the DNA methyltransferase inhibitor decitabine increased GADD45g mRNA levels approximately twofold[13][31][38][41]. Additionally, treatment with the histone deacetylase inhibitor romidepsin, which enhances histone acetylation, upregulated histone H3 and H4 acetylation at the GADD45g promoter in both myeloproliferative neoplasm cell lines[13][31][38][41]. These findings suggest that histone deacetylation plays a significant role in epigenetically silencing GADD45g in myeloproliferative neoplasms, while promoter DNA methylation appears to play only a marginal role[13][31][38][41]. The ability to reactivate GADD45g expression through epigenetic therapeutic approaches suggests potential therapeutic opportunities for myeloproliferative neoplasm treatment through GADD45g reactivation.

## Stress Resistance and Aging Processes

In the model organism Drosophila melanogaster, GADD45 plays a key role in stress resistance and longevity regulation. Flies with constitutive and conditional D-GADD45 overexpression in the nervous system demonstrate enhanced stress resistance compared to control flies without overexpression[33]. Most studied stress factors, including oxidative stress from paraquat exposure, genotoxic stress from gamma irradiation, heat shock at 35 degrees Celsius, and starvation, increased D-GADD45 expression in wild-type flies[33]. The lifespan-extending effect of D-GADD45 overexpression was retained after exposure to chronic and acute gamma irradiation doses of 40 cGy and 30 Gy respectively[33]. Conversely, knockout of D-GADD45 resulted in significant reduction in lifespan, lack of radiation hormesis (adaptive stress resistance), and absent radioadaptive responses to preconditioning irradiation[33]. A dramatic decrease in spontaneous D-GADD45 expression occurs in the nervous system as organisms age, which may represent one of the causes of age-related deterioration of organismal stress resistance[33].

In male Drosophila, three to nine-fold D-GADD45 overexpression led to more efficient repair of cellular damage and increased resistance to oxidative stress, hyperthermia, and starvation[33]. The increased resistance to genotoxic stress after preconditioning with low-dose irradiation was reduced by 1.6 to 2.3-fold when D-GADD45 was mutant, establishing D-GADD45 as playing a key role in formation of stress response reactions to ionizing radiation exposure[33].

## Conclusion and Future Perspectives

GADD45G emerges from the extensive experimental literature as a multifunctional stress-response protein of fundamental importance to human cellular physiology, development, and disease prevention. The protein functions as a critical molecular sensor that detects diverse forms of cellular damage and physiological stress through mechanisms involving induction of the p38 and JNK mitogen-activated protein kinase cascades via activation of the MEKK4 kinase. At the mechanistic level, GADD45G exerts its effects through dynamic protein-protein interactions with cell cycle regulatory proteins including cdc2/cyclin B1 complexes and p21, DNA repair machinery components including PCNA, and upstream signaling molecules including MEKK4. These interactions are mediated through the highly acidic central region of the GADD45G dimer interface and require dimerization for full biological activity.

The G2/M cell cycle checkpoint function of GADD45G provides a critical defense mechanism that prevents replication of damaged DNA, thereby maintaining genomic stability and preventing propagation of mutations to daughter cells. The stimulus-specific nature of GADD45G-mediated checkpoints, in which the protein functions in response to ultraviolet radiation and chemical mutagens but not ionizing radiation, indicates that mammalian cells employ multiple distinct checkpoint mechanisms responsive to different damage types.

GADD45G functions as a tumor suppressor through epigenetic inactivation mechanisms that silence the gene in multiple human cancer types including lymphomas, nasopharyngeal carcinoma, and hepatocellular carcinoma. The frequency of epigenetic silencing in cancer cell lines compared to the rarity of genetic mutations suggests that cancer cells preferentially employ reversible modifications to disable tumor-suppressive functions, potentially permitting therapeutic reversal through epigenetic reactivation strategies. Recent discoveries regarding GADD45g insufficiency in myeloproliferative neoplasms through RAC2-PAK1-PI3K-AKT pathway activation represent emerging insights into previously underappreciated roles of GADD45G in hematopoietic malignancies.

The essential role of GADD45G in male sexual development through p38 MAPK-mediated regulation of SRY expression establishes the protein as a critical determinant of sexual differentiation, with potential relevance to human disorders of sexual development and male infertility. The human-specific enhancement of brain size through regulatory modification of GADD45G and its subsequent role in promoting neurite outgrowth through p38 MAPK/CDC25B-mediated microtubule polymerization highlight the protein's contribution to the evolution of human cognitive capabilities.

Emerging evidence indicates roles for GADD45G in immune cell regulation, memory consolidation through DNA demethylation mechanisms, kidney disease progression, and stress resistance that collectively establish GADD45G as a protein of remarkable functional versatility. Future research should focus on understanding the structural basis of GADD45G interactions with specific partner proteins, the mechanisms by which epigenetic modifications regulate GADD45G expression in disease states, and the potential therapeutic applications of GADD45G reactivation in cancer and hematologic malignancy treatment. The convergence of GADD45G functions across stress response, cell cycle control, development, immunity, and disease prevention positions this protein as a central node integrating diverse cellular signaling networks critical for human health and disease.

## Citations

1. https://en.wikipedia.org/wiki/GADD45G
2. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1513069/full
3. https://www.pnas.org/doi/10.1073/pnas.0402069101
4. https://www.genecards.org/cgi-bin/carddisp.pl?gene=GADD45G
5. https://www.ncbi.nlm.nih.gov/gene/10912
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC11903704/
7. https://pubmed.ncbi.nlm.nih.gov/7478510/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC9042895/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC22358/
10. https://pubmed.ncbi.nlm.nih.gov/7784094/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC2563007/
12. https://www.nature.com/articles/s41467-024-47297-2
13. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0058751
14. https://pubmed.ncbi.nlm.nih.gov/17242196/
15. https://pubmed.ncbi.nlm.nih.gov/23516551/
16. https://www.tandfonline.com/doi/full/10.1128/MCB.01435-06
17. https://pubmed.ncbi.nlm.nih.gov/16166418/
18. https://www.pnas.org/doi/10.1073/pnas.96.7.3706
19. https://www.pnas.org/doi/10.1073/pnas.0800086105
20. https://aacrjournals.org/clincancerres/article/11/18/6409/186083/GADD45-Deregulation-in-Cancer-Frequently
21. https://pubmed.ncbi.nlm.nih.gov/10362260/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC6363930/
23. https://onlinelibrary.wiley.com/doi/full/10.1002/hep.26628
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC3978120/
25. https://en.wikipedia.org/wiki/Epigenetics_in_learning_and_memory
26. https://pubmed.ncbi.nlm.nih.gov/23897841/
27. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0044207
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC3524218/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC3797964/
30. https://pubmed.ncbi.nlm.nih.gov/1990262/
31. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR024824/pathways/
32. https://www.medchemexpress.com/mce_publications/38582902.html
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC3762688/
34. https://www.uniprot.org/uniprotkb/Q5VZ88/entry
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC10998908/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC11673765/
37. https://aacrjournals.org/clincancerres/article/11/18/6442/186067/The-Stress-Responsive-Gene-GADD45G-Is-a-Functional
38. https://www.nature.com/articles/424742a
39. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=10912
40. https://pubmed.ncbi.nlm.nih.gov/14743220/
41. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0014500
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC4110750/
43. https://stacks.cdc.gov/view/cdc/195781
44. https://pubmed.ncbi.nlm.nih.gov/22058036/
45. https://rupress.org/jem/article/202/10/1341/52795/Gadd45-and-Gadd45-are-critical-for-regulating
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC4877482/