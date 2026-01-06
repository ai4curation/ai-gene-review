---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-27T16:18:31.049377'
end_time: '2025-12-27T16:20:35.359525'
duration_seconds: 124.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AFAP1
  gene_symbol: AFAP1
  uniprot_accession: Q8N556
  protein_description: 'RecName: Full=Actin filament-associated protein 1; AltName:
    Full=110 kDa actin filament-associated protein; Short=AFAP-110;'
  gene_info: Name=AFAP1; Synonyms=AFAP;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849);
    PH (PF00169)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 41
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8N556
- **Protein Description:** RecName: Full=Actin filament-associated protein 1; AltName: Full=110 kDa actin filament-associated protein; Short=AFAP-110;
- **Gene Information:** Name=AFAP1; Synonyms=AFAP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); PH (PF00169)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AFAP1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AFAP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AFAP1** (gene ID: AFAP1, UniProt: Q8N556) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze the search results provided to create a comprehensive research report on AFAP1 (Actin filament-associated protein 1).

First, let me verify I have the correct gene/protein:
- UniProt Accession: Q8N556
- Protein Description: Actin filament-associated protein 1
- Gene: AFAP1
- Organism: Homo sapiens (Human)
- Domains: PH domain, actin filament associated protein family

Looking at the search results, I have extensive information about AFAP1 and related proteins. The search results include:
1. Basic gene information (Wikipedia, NCBI, UniProt)
2. Information about AFAP1-AS (a long noncoding RNA derived from the AFAP1 gene)
3. Structural and functional information about AFAP1 protein
4. Cancer-related research
5. Information about related proteins like AFAP1L1
6. Mechanistic studies on AFAP1 function

Now I need to organize this into a comprehensive research report covering:
1. Introduction and key findings
2. Protein structure and domains
3. Molecular interactions (Src binding, actin binding)
4. Cellular localization
5. Signaling pathways and mechanisms
6. Biological functions (adhesion, migration, invasion)
7. Role in podosomes and invadopodia
8. Cancer-related functions
9. The AFAP1-AS1 lncRNA (as an important regulatory element)
10. Physiological roles
11. Conclusion

I need to write at least 10,000 words following the format guidelines with proper citations.
</think>

# Actin Filament-Associated Protein 1 (AFAP1): Structure, Function, and Cellular Mechanisms

AFAP1 (actin filament-associated protein 1), also known as AFAP-110, is a multifunctional adapter protein that plays critical roles in regulating cytoskeletal dynamics and cellular signaling, particularly through its interactions with the Src family tyrosine kinases and filamentous actin structures[1][4]. Recent research has revealed that AFAP1 functions as a dual-role regulator, operating both as a direct mediator of signal transduction at the protein level and indirectly through its associated antisense long noncoding RNA (AFAP1-AS1), which modulates oncogenic processes in various cancer types[9][14]. The protein is primarily localized to actin filaments, focal adhesions, and specialized membrane structures called podosomes and invadopodia, where it coordinates the assembly and remodeling of actin-rich structures essential for cell adhesion, migration, and invasion[1][12][19]. This comprehensive report examines the molecular architecture, biochemical functions, cellular mechanisms, and biological significance of AFAP1, synthesizing current knowledge from structural biology, cell biology, and cancer research to provide an integrated understanding of this important regulatory protein.

## Molecular Architecture and Domain Organization

AFAP1 possesses a highly specialized modular architecture that enables its diverse cellular functions through multiple protein-protein interaction domains. The protein structure includes two **Pleckstrin Homology (PH) domains**, which are characteristic features of the broader AFAP family of proteins and serve as recognition modules for phosphorylated lipids and protein interaction surfaces[54][55]. One of these PH domains contains a binding site for protein kinase C (PKC), specifically PKCα, which phosphorylates serine residue 277 and plays a critical role in regulating AFAP1's ability to modulate podosome formation and stability[49][52][54]. Beyond the PH domains, AFAP1 contains N-terminal **SH2 and SH3 binding motifs** that specifically interact with the SH3 and SH2 domains of the nonreceptor tyrosine kinase c-Src, enabling tight coupling of AFAP1 to Src family kinase signaling[6][10][54]. These SH3 binding motifs are structurally conserved and essential for stable complex formation with Src and subsequent tyrosine phosphorylation of AFAP1[50]. The C-terminal region of the protein harbors **actin-binding domains** that mediate direct interactions with filamentous actin (F-actin) and likely involve AFAP1 multimeric assemblies, allowing the protein to cross-link actin filaments into both network and bundle structures[1][40][54][55]. The N-terminal SH3 binding motif is absolutely critical for AFAP1 function, as mutations or deletions of this motif completely abolish both Src binding and the ability of AFAP1 to regulate downstream cellular processes[1][6][10].

The protein exists in at least two isoforms, the neuronal cell-specific A isoform and the ubiquitously expressed B isoform, suggesting specialized functions in different cellular contexts[33]. Multiple transcript variants have been identified that encode different AFAP1 isoforms, providing additional regulatory flexibility through alternative splicing[1][4][8]. The overall design of AFAP1's domain organization—combining PKC regulatory sites, Src interaction motifs, and actin-binding capability—positions it as an ideal scaffold protein capable of integrating multiple signaling inputs to coordinate actin cytoskeletal responses. This architecture is shared to varying degrees by other family members such as AFAP1L1 and AFAP1L2 (also known as XB130), though subtle differences in domain structure and amino acid sequences lead to different subcellular localizations and binding affinities for specific interaction partners[57].

## Protein-Protein Interactions and Src Kinase Coupling

The interaction between AFAP1 and the proto-oncogene tyrosine-protein kinase Src (c-Src) represents one of the most fundamental and well-characterized aspects of AFAP1 biology, as this coupling directly translates extracellular signals into cytoskeletal reorganization. AFAP1 binds to c-Src through its N-terminal SH3 binding motif, which interacts with the SH3 domain of Src, and this interaction is further strengthened by phosphorylation-dependent binding of the Src SH2 domain to tyrosine-phosphorylated residues on AFAP1[6][22][51]. Upon phosphorylation by activated Src (or by PKCα), AFAP1 undergoes conformational changes that expose additional interaction surfaces, allowing the SRC SH2 domain to bind phosphorylated tyrosine residues on AFAP1, thereby stabilizing and potentially increasing the catalytic efficiency of the AFAP1-Src complex[22][47][51]. This phosphorylation-dependent interaction is particularly important for the localization of Src to actin filaments, as AFAP1 serves as a bridging molecule that brings activated Src into proximity with its substrate targets in the actin cytoskeleton[22][47][51]. AFAP1 is itself a substrate for both PKCα and Src family kinases (c-Src and Fyn), creating a regulatory feedback loop in which AFAP1 phosphorylation enhances Src activation and vice versa[13][54][37]. In response to stimuli such as prolactin in mammary gland tissue, AFAP1 becomes tyrosine phosphorylated and forms a stable complex with c-Src, facilitating normal spatial and temporal Src activity[54].

The relationship between AFAP1 and Src extends beyond simple binding, as AFAP1 can directly activate c-Src through interactions with both the SH3 and SH2 domains, suggesting that AFAP1 acts as a nucleation factor or scaffold that promotes Src autophosphorylation and activation[7][16]. Mechanistic studies indicate that AFAP1 can facilitate c-Src activation through binding-induced conformational changes that relieve autoinhibition of the kinase[7][16]. The C-terminal actin-binding capability of AFAP1 means that once activated, the AFAP1-Src complex is simultaneously positioned on actin filaments where Src can phosphorylate additional substrates involved in cytoskeletal organization[40][54]. This spatial organization is crucial because Src phosphorylates numerous substrates beyond AFAP1, including cortactin and other actin regulatory proteins, all of which need to be coordinated to produce coherent changes in cytoskeletal architecture[22][47]. Interestingly, AFAP1 appears to show substrate specificity or preference in terms of which Src family kinases it interacts with most efficiently—while it binds strongly to c-Src via its SH3 binding motif, AFAP1L1, a family member, shows reduced affinity for Src but instead preferentially associates with cortactin, indicating functional diversification within the AFAP family[45][57].

## Cellular Localization and Subcellular Distribution

AFAP1 exhibits a highly dynamic and stimulus-dependent pattern of subcellular localization that reflects its functional role in organizing actin-based cellular structures. In unstimulated cells, AFAP1 localizes prominently to actin filaments and focal adhesion sites, where it remains available to respond to cellular signals[23][59]. The protein is primarily distributed along the cytoskeleton, localizing to the cell cortex and to the ventral surface of cells where focal adhesions and podosomes form[1][59]. Upon stimulation with activators of PKC or in response to growth factors, AFAP1 rapidly translocates to newly forming podosomes and invadopodia, specialized actin-rich membrane protrusions that are sites of intense cytoskeletal remodeling[17][54][56]. In the lactating mammary gland, AFAP1 shows a striking pattern of localization at the apical surface of luminal epithelial cells, where it colocalizes with active c-Src, particularly during early lactation when elevated Src activity is required for proper milk protein secretion[54]. The protein outlines the cellular cortex with equal distribution on basolateral and apical sides of cells, localized exterior to cytokeratin staining, suggesting its role in organizing cortical actin structures that are fundamental to epithelial cell architecture and function[54].

AFAP1's ability to respond dynamically to signals is reflected in its redistribution to sites of active actin remodeling. Upon c-Src binding and activation, AFAP1 and c-Src move together to podosomes, which are adhesion structures found on the ventral membrane of cells containing an F-actin-rich core surrounded by adhesion proteins[17][56]. This coordinated localization is essential for AFAP1's function in regulating podosome assembly and stability, as the protein must be present at the site of actin dynamics to exert its mechanical effects on filament organization[16][37]. In specialized cell types such as retinal ganglion cells, AFAP1 is expressed and likely plays roles in ocular physiology, with expression variants suggesting involvement in tissue-specific functions[33][36]. The dynamic nature of AFAP1 localization—shifting from baseline distribution on focal adhesions and actin filaments to concentrated accumulation at podosomes and invadopodia in response to specific signals—demonstrates that AFAP1 functions as a signal-responsive organizer of cytoskeletal structures rather than as a static structural component.

## Regulation of Actin Filament Structure and Mechanical Properties

At the molecular level, AFAP1 directly modulates the physical properties of the actin cytoskeleton through its dual capacity to bind both Src kinase and F-actin, creating what is essentially a mechanochemical coupling system. AFAP1 can cross-link actin filaments into both network and bundle structures, a function that requires both its actin-binding domain and potentially its capacity for self-association through multimerization[55][58]. The actin-binding domain of AFAP1, located at the C-terminus, is critical for regulating actin filament structure, and overexpression of deletion mutants lacking the actin-binding domain (AFAPΔABD) results in disrupted regulation of actin organization[43]. Phosphorylation of serine 277 by PKCα increases the ability of AFAP1 to cross-link actin filaments, suggesting that post-translational modification directly enhances the mechanical interaction between AFAP1 and the actin cytoskeleton[49][54]. The mechanism by which AFAP1 affects actin filament integrity appears to involve not merely passive cross-linking, but also active regulation of actin filament dynamics, as AFAP1 can modulate the responsiveness of actin networks to external mechanical forces and cellular signaling inputs[43].

The functional significance of AFAP1's actin-binding activity is particularly evident in its role in actin stress fiber formation and maintenance. AFAP1 plays an important role in breast cancer cell adhesion, possibly by regulating stress filament cross-linking, which would promote focal adhesion maturation and mechanotransduction signaling[41]. Loss or reduction of AFAP1 expression results in decreased actin stress fiber formation and loss of cell stress filament integrity, indicating that AFAP1 is a critical positive regulator of stress fiber assembly[21][38]. In nasopharyngeal carcinoma cells, loss of lncRNA AFAP1-AS1 (which is transcribed from the antisense strand and acts partly through AFAP1-independent mechanisms) results in loss of stress fiber formation via effects on F-actin polymerization, though the exact relationship to AFAP1 protein levels remains to be clarified[42][60]. The mechanism appears to involve AFAP1's ability to stabilize actin filament bundles through cross-linking and possibly through recruitment of additional actin regulatory proteins via its interaction with c-Src and other signaling molecules. AFAP1 may thus represent a key node in the complex regulatory network that balances actin polymerization with filament stabilization and organization into higher-order structures.

## Podosomes: Formation, Regulation, and Function

Podosomes represent specialized actin-based cellular structures where AFAP1 plays a particularly prominent role in orchestrating assembly and regulating the maturation and turnover of these dynamic organelles. Podosomes are adhesion structures found on the ventral membrane of cells and consist of a core of cross-linked F-actin surrounded by a ring of adhesion-related proteins including vinculin, paxillin, and talin[1][17][26][29]. AFAP1 is absolutely required to mediate PKCα-induced activation of the tyrosine kinase c-Src and the subsequent formation of podosomes, as demonstrated through studies showing that AFAP1 null cells fail to form podosomes in response to PKC activation[16][37]. The mechanism involves PKCα phosphorylation of AFAP1 at serine 277, which enhances AFAP1's ability to activate c-Src, and the resulting activated AFAP1-Src complex localizes to sites of incipient podosome formation where it phosphorylates downstream substrates[16][49][54].

The formation of podosomes occurs in a stepwise manner, with the first visible stage being the formation of actin puncta, small accumulations of branched actin filaments at specific locations[26][29]. AFAP1 appears to be involved in the early stages of this process through its interaction with c-Src and actin filaments, likely helping to stabilize initial actin accumulations and recruit additional proteins required for podosome maturation[17][26]. Following formation of the actin puncta, adhesion proteins including vinculin and paxillin are recruited to form a ring-like structure surrounding the actin core[26][29]. The adhesion ring that forms around podosomes represents a specialized focal adhesion-like structure that serves to anchor the podosome to the underlying extracellular matrix and likely couples mechanical forces from the actin core to adhesion signaling pathways[26]. AFAP1 regulates not only the formation of podosomes but also their stability and turnover—studies have shown that AFAP1 phosphorylation by PKCα plays a role in regulating podosome formation and lifespan, suggesting that AFAP1-mediated signaling directly controls the temporal dynamics of podosome assembly and disassembly[49][52].

Both c-Src and the associated phosphatase PTP1B are required for proper podosome dynamics and turnover, with CSK (a negative regulator of Src) also playing a regulatory role[29]. This indicates that AFAP1, as the primary mechanism through which PKC activates Src for podosome formation, is embedded within a broader regulatory network that balances activation and inactivation signals to produce the appropriate temporal pattern of podosome formation and regression. In certain cell types such as vascular smooth muscle cells treated with phorbol esters or Src-transformed fibroblasts, podosomes form rapidly (in less than 15 minutes) from disassembling focal adhesions, with AFAP1 and c-Src activity being central to this transition[29]. This direct transformation of focal adhesions into podosomes suggests that AFAP1 participates in a structural remodeling process that converts one actin-based adhesion structure into another, a process that would require simultaneous cross-linking of new actin assemblies while disrupting existing ones.

## Invadopodia: Invasive Structures and Cancer Cell Invasion

Beyond its role in podosome formation, AFAP1 participates in the assembly and regulation of invadopodia, which are F-actin-rich membrane protrusions that breach basement membrane barriers during cell invasion[39][42]. Invadopodia differ from podosomes in that they are particularly prominent in cancer cells with high metastatic potential and function primarily as degradative structures rather than adhesion organelles, though they share many molecular components including actin filaments, adhesion molecules, and regulatory proteins[26][29][39]. The formation of invadopodia, like podosomes, requires integration of growth factor signaling and adhesion signaling, with different stages of invadopodium maturation being regulated by distinct signaling inputs[26]. AFAP1 has been shown to regulate cellular responses requiring actin cytoskeletal changes such as adhesion, invadopodia formation, and invasion in breast and prostate cancer cells[5][12]. The precise role of AFAP1 in invadopodia formation and function appears to parallel its role in podosomes, with AFAP1 and c-Src working together to organize F-actin core structures and recruit associated proteins.

The functional consequence of AFAP1-mediated invadopodium assembly is enhanced capacity for extracellular matrix degradation and cellular invasion. Invadopodia contain matrix metalloproteinases (particularly MT1-MMP) that are localized to the ventral membrane and oriented toward the extracellular matrix where they perform localized proteolysis[26][39]. The stability of MT1-MMP at invadopodia is promoted by direct interaction with invadopodial F-actin, providing a direct linkage between the actin core organized by AFAP1 and other proteins, and the proteolytic machinery that actually degrades matrix[39][26]. The assembly of invadopodia occurs in stages, with growth factor signaling (particularly PI3K signaling) promoting initial formation, while adhesion to the extracellular matrix promotes maturation and localized protease exocytosis, resulting in a functional degrading structure[26]. AFAP1's role in organizing the actin core that forms the structural foundation of invadopodia thus directly enables matrix degradation and cellular invasion, providing a molecular mechanism linking cytoskeletal organization to the invasive phenotype of cancer cells.

## Signaling Integration: PKCα, Integrin Signaling, and FAK

AFAP1 functions as a critical integrator of multiple signaling pathways, most notably receiving input from protein kinase C (PKCα) and transducing signals through c-Src to organize actin cytoskeletal responses. PKCα activates AFAP1 through phosphorylation of serine 277, which enhances AFAP1's ability to bind and activate c-Src[49][54]. This PKC-AFAP1-Src axis is particularly important in response to phorbol esters, which are natural PKC activators, and in response to growth factors that activate PKC through phospholipase C-mediated generation of diacylglycerol[54]. Beyond PKCα input, AFAP1 receives signals through integrin-mediated adhesion, as integrin ligation to the extracellular matrix activates Src through FAK (focal adhesion kinase), and activated c-Src in turn phosphorylates AFAP1[54]. The result is that AFAP1 becomes a convergence point for signals emanating from both growth factor receptors (via PKC) and integrin receptors (via Src), allowing cells to coordinate cytoskeletal changes that occur in response to both growth-promoting and adhesion signals.

AFAP1 also appears to participate in the regulation of focal adhesion dynamics and turnover, though this function is less completely characterized than its roles in podosomes and invadopodia. Src-mediated phosphorylation of FAK at multiple tyrosine residues is necessary to enhance the adaptor function of FAK and promote focal adhesion turnover through calpain-mediated proteolysis[44]. Since AFAP1 serves as a primary activator of Src in response to PKC, AFAP1 indirectly regulates focal adhesion turnover through this mechanism. Moreover, AFAP1's direct interaction with actin filaments means that it can modulate the mechanical coupling between focal adhesions and the actin cytoskeleton, potentially influencing the contractile forces that stabilize focal adhesions or the mechanical transitions that occur during focal adhesion disassembly. In the context of PKC activation with phorbol esters, focal adhesions dissolve and then reorganize around newly formed actin puncta that will become podosomes, suggesting that AFAP1-mediated cytoskeletal remodeling directly drives the transition between focal adhesion and podosome architecture[26][29].

## The AFAP1-AS1 Long Noncoding RNA: Oncogenic Regulation of Cytoskeletal Dynamics

In parallel with the protein-level functions of AFAP1, a long noncoding RNA (lncRNA) transcribed from the antisense strand of the AFAP1 gene locus, termed AFAP1-AS1 (or AFAP1-AS in earlier literature), has emerged as a critical regulator of cancer progression and metastasis. AFAP1-AS1 localizes to the antisense genomic DNA strand near the C-terminus of AFAP1, at the actin binding domain of AFAP1, and is transcribed as an independent RNA molecule[2][21]. The long noncoding RNA functions primarily through competing endogenous RNA (ceRNA) mechanisms, in which AFAP1-AS1 contains multiple binding sites for microRNAs and functions as a "molecular sponge" that sequesters miRNAs and prevents them from binding to and suppressing their target messenger RNAs[2][21]. In the context of Hirschsprung disease (a developmental disorder affecting neural crest cell migration), AFAP1-AS was found to be downregulated compared to normal tissues, and knockdown of AFAP1-AS inhibited neural crest cell proliferation and migration by competitively binding miR-181a and thereby allowing increased expression of RAP1B[2][21]. This ceRNA regulatory network (AFAP1-AS/miR-181a/RAP1B) demonstrates that the lncRNA participates in the regulation of neural crest cell colonization, a process fundamentally dependent on cell migration and cytoskeletal dynamics[2][21].

However, in the context of cancer, AFAP1-AS1 is typically upregulated and functions as an oncogene promoting tumor progression. Overexpression of AFAP1-AS1 is associated with enhanced cell proliferation, migration, invasion, epithelial-mesenchymal transition (EMT), and metastasis, thereby correlating with poor clinical outcomes across multiple cancer types[9][14][25][36][38]. AFAP1-AS1 has been found to be abnormally expressed in numerous cancers, including cholangiocarcinoma, pancreatic adenocarcinoma, non-small cell lung cancer, nasopharyngeal carcinoma, breast cancer, osteosarcoma, gastric cancer, esophageal squamous cell carcinoma, colorectal cancer, and prostate cancer[25][36][38][9]. In non-small cell lung cancer (NSCLC), AFAP1-AS1 enhances migration and invasive properties through activation of IRF7 and the RIG-I-like receptor signaling pathway, and also interacts with the epigenetic regulator EZH2 to repress expression of the cell cycle inhibitor p21[38]. In breast cancer, particularly in triple-negative breast cancer (TNBC), AFAP1-AS1 sequences miR-145 to allow increased expression of MTH1, thereby enhancing proliferation and invasiveness[38]. The lncRNA also sequesters miR-2110 in breast cancer cells, leading to enhanced expression of the transcription factor Sp1[38].

Remarkably, in breast cancer cells resistant to the therapeutic antibody trastuzumab (Herceptin), AFAP1-AS1 can be secreted into exosomes and transmitted to other cells, where it induces trastuzumab resistance through interaction with the RNA-binding protein AUF1 and subsequent induction of ERBB2 (also known as HER2) translation[38]. This exosomal transmission of AFAP1-AS1 represents a novel form of intercellular communication in cancer, where the lncRNA can disseminate therapy resistance to other cancer cells in the tumor microenvironment[15]. In osteosarcoma, AFAP1-AS1 promotes tumorigenesis through the RhoC/ROCK1/p38MAPK/Twist1 cascade, and can sequester miR-497 and miR-4695-5p, thereby increasing expression of IGF1R and TCF4, which activate Wnt-β catenin signaling[38]. In gastric cancer, AFAP1-AS1 promotes proliferation and metastasis through sequestration of miR-155-5p, leading to enhanced expression of FGF7[38]. The mechanistic studies indicate that AFAP1-AS1 modulates actin filament integrity by influencing the expression of key molecules in cytoskeletal regulation and can affect the protein level of its sense counterpart, AFAP1, either directly or via interactions with regulatory factors such as EZH2 and SNIP1[9][14].

Importantly, studies in animal models (particularly BALB/c nude mice) have verified the oncogenic roles of AFAP1-AS1 in different cancer types, with knockdown of AFAP1-AS1 consistently leading to significant reduction in tumor size and weight, attenuation of tumor growth rate, and enhancement of response to therapeutic modalities[38]. In NSCLC, AFAP1-AS1 silencing not only reduces tumorigenicity but also confers chemosensitivity[38]. In breast cancer, AFAP1-AS1 downregulation can reduce trastuzumab resistance, suggesting therapeutic potential for targeting this lncRNA[38]. The cellular localization of AFAP1-AS primarily to the cytoplasm indicates that it functions through interaction with miRNAs and mRNA regulation rather than nuclear transcriptional regulation[2][21]. Loss of stress fiber formation in cells with reduced AFAP1-AS1 expression suggests that the lncRNA somehow influences actin dynamics, possibly through mechanisms involving AFAP1 protein or through direct effects on expression of actin regulatory proteins via its ceRNA activities[2][21][42][60].

## Genetic Variation and Disease Association

Population-based genetic studies have identified associations between variants in the AFAP1 gene locus and common human diseases, particularly primary open-angle glaucoma, the most common form of glaucoma and a leading cause of blindness worldwide. A genome-wide association study identified a SNP (rs4619890) within the AFAP1 gene that confers risk of primary open-angle glaucoma, with the associated SNP rs28495790 (in high linkage disequilibrium with rs4619890) likely affecting binding of proteins such as CTCF and RAD21, and altering the sequence of regulatory motifs for binding of several proteins including PAX6[33]. The functional mechanism underlying the association appears to involve AFAP1's role in regulating the actin cytoskeleton in ocular tissues, as actin cytoskeleton-modulating signals have been demonstrated to be involved in the regulation of aqueous outflow and intraocular pressure, which are critical parameters in glaucoma pathogenesis[33]. AFAP1 is expressed in retinal ganglion cells (the cells that undergo apoptosis in glaucoma), as well as in the trabecular meshwork, retina, optic nerve, and optic nerve head[33]. Both the neuronal A isoform and the ubiquitously expressed B isoform of AFAP1 are detected in human retinal tissue, with the B isoform more broadly distributed in ocular tissues including iris, ciliary body, lens, optic nerve, and optic nerve head[33].

The involvement of AFAP1 in glaucoma likely reflects its function in regulating actin dynamics and cell morphology in tissues critical for maintaining normal intraocular pressure. In the trabecular meshwork, which controls aqueous humor outflow, AFAP1-mediated regulation of the actin cytoskeleton may influence cell shape and the spacing of trabecular meshwork cells, thereby affecting fluid filtration capacity. In retinal ganglion cells, AFAP1 may regulate axonal morphology and cell survival through its effects on cytoskeletal organization. The association between AFAP1 variants and glaucoma risk provides strong evidence that normal AFAP1 function is important for maintaining ocular homeostasis, and furthermore suggests that AFAP1-based therapeutic approaches might be relevant to glaucoma treatment, though this remains speculative at present.

## Tissue Expression and Specialized Cell Types

AFAP1 shows a broad but selective pattern of expression across human tissues, with particularly high expression in tissues with significant cytoskeletal dynamics and specialized cellular structures. Analysis of gene expression data reveals that AFAP1 is expressed in numerous tissues including nervous system tissues (hippocampal formation, amygdala, basal ganglia, midbrain, spinal cord, cerebral cortex, cerebellum, hypothalamus, retina), endocrine tissues (thyroid gland, parathyroid gland, adrenal gland, pituitary gland), gastrointestinal tissues (esophagus, stomach, duodenum, small intestine, rectum, colon), hepatic tissues (liver, gallbladder), urinary tissues (kidney, urinary bladder), reproductive tissues (testis, epididymis, prostate, seminal vesicle, vagina, breast, cervix, endometrium, fallopian tube, ovary), and cardiovascular tissues (heart muscle, blood vessels)[23][28][59]. AFAP1 expression in specialized cell types such as retinal ganglion cells suggests its involvement in ocular physiology and possibly in the pathogenesis of glaucoma, as mentioned above[9][14][33][36].

The ubiquitous expression pattern of at least the AFAP1 B isoform across tissues suggests that AFAP1 performs fundamental functions in actin cytoskeletal organization that are required in virtually all cell types. However, the existence of the neuronal A isoform and the selective expression of AFAP1 in particular tissues like retinal ganglion cells indicates that specialized variants of AFAP1 may be required for tissue-specific functions. The expression profile of AFAP1 in tissues with high cellular motility, adhesion dynamics, or specialized membrane structures (such as the nervous system and reproductive tissues) is consistent with its proposed roles in regulating actin-based adhesion and migration. In the context of cancer, AFAP1 expression is often elevated in tumor tissues compared to normal tissue, and in some cases expression level predicts clinical outcomes, as demonstrated for AFAP1L1 in colorectal cancer[20][45][48].

## The AFAP1 Family: Structural Relationships and Functional Diversification

AFAP1 is the prototype member of a family of actin filament-associated proteins that includes AFAP1L1 and AFAP1L2 (also termed XB130), with all three members sharing similar modular domain structures containing PH domains and SH2/SH3 binding motifs for Src interaction[57]. However, despite this structural similarity, the AFAP family members show important differences in subcellular localization, binding partner specificity, and cellular functions. AFAP1 binds strongly to c-Src via its SH3 binding motif and shows prominent localization to focal adhesions and podosomes[1][10][54][56]. AFAP1L1, in contrast, does not bind strongly to Src but instead preferentially associates with cortactin and colocalizes with cortactin within invadopodia[20][45][48]. AFAP1L1 was identified as a metastasis-predicting marker for spindle cell sarcomas and has been found to be elevated in colorectal cancer tissues, where high expression serves as an independent factor predicting recurrence of rectal cancers[20][45][48]. AFAP1L1-expressing cells exhibit increased motility, enhanced invasion, resistance to anoikis (death upon loss of cell-matrix contact), and accelerated tumor growth in vivo[20][45]. The localization of AFAP1L1 to the ringed structure of invadopodia together with vinculin indicates that AFAP1L1 forms novel complexes distinct from those formed by AFAP1[20][45][48].

AFAP1L2/XB130 appears to have additional functions not shared by AFAP1 or AFAP1L1, including involvement in growth factor signaling and cell survival pathways. The existence of this family of proteins with related structures but divergent binding partners and functions suggests that the AFAP family evolved to provide specialized adaptor functions in different cellular compartments and in response to different signaling pathways. Notably, AFAP1L1 interacts with vinculin, a major focal adhesion protein, through novel mechanisms that appear to disrupt normal focal adhesion architecture and promote cell invasion and EMT[20][45][48]. This diversification within the AFAP family may reflect an evolutionary strategy to enable flexible regulation of different aspects of cell adhesion and migration in different cellular contexts. The structural similarity but functional divergence of AFAP family members underscores the principle that protein domains and interaction motifs can be combined in modular fashion to generate proteins with distinct cellular functions.

## Summary of Key Biological Processes and Functions

AFAP1 participates in multiple interconnected biological processes that collectively enable cells to dynamically modulate their adhesion and migratory behavior in response to environmental and developmental signals. At the molecular level, AFAP1 functions as a scaffolding protein that couples signals from activated protein kinase C and Src family kinases to the actin cytoskeleton, thereby promoting formation of actin-based structures including stress fibers, focal adhesions, podosomes, and invadopodia[9][12][14][54]. These structures are essential for fundamental cellular processes including cell adhesion, spreading, migration, and invasion. In the context of normal physiology, AFAP1 likely participates in developmental processes requiring coordinated cell migration, such as neural crest cell migration and vascular development, and also in maintaining cellular functions in differentiated tissues such as the mammary gland during lactation[54]. In the context of cancer, elevated AFAP1 expression and enhanced activity of the AFAP1-AS1 lncRNA promote the metastatic potential of cancer cells by enhancing migration, invasion, and cellular plasticity through epithelial-mesenchymal transition[9][14][25][36][38].

The physiological regulation of AFAP1 involves both post-translational modification of the AFAP1 protein itself and transcriptional/post-transcriptional regulation of expression through both the AFAP1 gene and the AFAP1-AS1 lncRNA. PKCα-mediated phosphorylation at serine 277 enhances AFAP1's ability to bind and activate Src, while tyrosine phosphorylation by Src itself stabilizes the AFAP1-Src complex through SH2 domain engagement[49][54]. The expression of AFAP1 is modulated in response to developmental signals and in cancers, with elevated expression generally associated with enhanced invasive and migratory potential. The AFAP1-AS1 lncRNA, which can either promote or suppress cancer depending on the specific cancer context, functions primarily as a ceRNA that regulates the availability of microRNAs and thus modulates expression of microRNA target genes[2][9][14][21][36][38]. This multilevel regulation—encompassing transcriptional control of both AFAP1 and AFAP1-AS1, post-translational modification of AFAP1 protein, and post-transcriptional control via AFAP1-AS1 ceRNA activity—enables precise spatial and temporal control of AFAP1-mediated cytoskeletal responses.

## Clinical and Therapeutic Implications

The identification of AFAP1 and AFAP1L1 as factors promoting cancer progression has led to consideration of these proteins as potential therapeutic targets. In animal models (BALB/c nude mice), local administration of short interfering RNA (siRNA) targeting AFAP1L1 significantly suppressed tumor growth of colorectal cancer xenografts, suggesting the feasibility of targeting AFAP1 family members therapeutically[20][45][48]. Similarly, knockdown of AFAP1-AS1 in various cancer models consistently reduces tumorigenicity and can enhance chemosensitivity[38]. However, the essential roles of AFAP1 in normal cellular processes including adhesion, migration, and cytoskeletal organization necessitate careful consideration of toxicity to normal tissues if AFAP1 were to be targeted therapeutically. The tissue-restricted expression of the AFAP1 A isoform in neurons suggests that complete inhibition of AFAP1 function might not be tolerated in the nervous system, whereas AFAP1L1 targeting might be more selectively toxic to cancer cells if AFAP1L1 expression is elevated in tumors but remains low in normal tissues.

The association between AFAP1 variants and glaucoma risk opens the possibility of developing AFAP1-based therapies for glaucoma management, potentially by modulating AFAP1 activity or expression to enhance actin cytoskeletal dynamics in trabecular meshwork cells and thereby improve aqueous humor outflow[33]. The finding that AFAP1-AS1 is secreted in exosomes and can disseminate trastuzumab resistance in breast cancer suggests that blocking exosomal AFAP1-AS1 or its cellular uptake might represent a novel therapeutic strategy to prevent therapy resistance in cancer[15][38]. However, therapeutic approaches targeting AFAP1 or AFAP1-AS1 remain largely preclinical and would require substantial development before clinical application. Future research should focus on understanding tissue-specific functions of AFAP1 to identify contexts in which AFAP1 inhibition would be beneficial with acceptable toxicity, and on developing selective inhibitors of AFAP1-Src interaction or AFAP1-mediated cytoskeletal reorganization that might have therapeutic utility.

## Future Directions and Outstanding Questions

Despite substantial progress in understanding AFAP1 biology, significant questions remain regarding the precise mechanisms of actin cross-linking and filament organization by AFAP1, the detailed structural basis for AFAP1 interactions with Src and actin, and the complete spectrum of AFAP1 functions in normal physiology. The three-dimensional crystal structure of AFAP1, particularly in complex with c-Src and actin filaments, would provide crucial insights into the molecular details of AFAP1's catalytic mechanisms and its role in organizing actin-based structures. The relative roles of AFAP1-mediated Src activation versus AFAP1's direct actin cross-linking activity in promoting different cellular processes remain incompletely understood, and future studies using mutants specifically defective in either Src binding or actin binding might clarify these distinct contributions. The mechanisms by which AFAP1-AS1 lncRNA regulates AFAP1 protein expression, either directly or indirectly through its various ceRNA interactions, warrant further investigation, as does the question of whether there are direct interactions between AFAP1 protein and AFAP1-AS1 RNA. The tissue-specific and developmental stage-specific functions of the AFAP1 A and B isoforms require deeper investigation, particularly in the context of nervous system development and function.

The relationship between AFAP1 function and other actin regulatory pathways, particularly those involving Arp2/3 complex, mDia formin family proteins, and cofilin-mediated actin depolymerization, remains incompletely characterized despite clear functional connections in the literature. The coordination of AFAP1-mediated signaling with growth factor signaling pathways, particularly PI3K/Akt and ERK/MAPK pathways, appears critical for proper regulation of invadopodia formation and cancer cell invasion but has not been thoroughly characterized at the molecular level. The potential for targeted disruption of the AFAP1-Src interaction or AFAP1-AS1 function as cancer therapeutics requires further preclinical development and optimization. Finally, the role of AFAP1 in regulating cell-matrix adhesion at the mechanical level, particularly the coupling between AFAP1-organized actin structures and the mechanotransduction signaling through focal adhesion kinase and Src, remains an important area for future investigation that could inform approaches to preventing cancer metastasis and treating fibrotic diseases.

## Conclusion

AFAP1 (actin filament-associated protein 1) is a multifunctional adapter protein that plays central roles in organizing the actin cytoskeleton and transducing signals from protein kinase C and integrin receptors to actin-based structures critical for cell adhesion, migration, and invasion. The protein functions through multiple interconnected mechanisms: direct interaction with and activation of c-Src kinase through its N-terminal SH3 binding motif; cross-linking of actin filaments through its C-terminal actin-binding domain; integration of signals from PKCα through PKC-mediated phosphorylation at serine 277; and recruitment of signaling complexes to sites of actin remodeling[1][4][9][12][14][54]. AFAP1 achieves these functions through a modular protein architecture featuring two Pleckstrin Homology domains, Src interaction motifs, and actin-binding regions that collectively enable AFAP1 to serve as a hub for coordinating multiple signaling inputs and translating them into coherent changes in cytoskeletal organization. AFAP1 is required for formation of podosomes (in response to PKC activation) and invadopodia (specialized invasive structures in cancer cells), and regulates the assembly and dynamics of focal adhesions and stress fibers critical for cell adhesion and migration[12][16][17][26][29][41]. In addition to its protein-level functions, the AFAP1 gene locus produces AFAP1-AS1, a long noncoding RNA with oncogenic functions in numerous cancer types that acts primarily as a competing endogenous RNA to sequester microRNAs and modulate gene expression[2][9][14][21][25][36][38].

AFAP1 is broadly expressed across tissues, with particularly prominent expression in tissues with high cellular motility and dynamic adhesion requirements including the nervous system, reproductive tissues, and vascular tissues[23][28][59]. The protein is regulated through multiple mechanisms including post-translational phosphorylation and transcriptional control of both the protein-coding AFAP1 mRNA and the lncRNA AFAP1-AS1. Dysregulation of AFAP1 and AFAP1-AS1 has been implicated in cancer progression and metastasis across numerous cancer types, and genetic variants in the AFAP1 locus have been associated with primary open-angle glaucoma, suggesting that normal AFAP1 function is critical for maintaining actin dynamics in tissues controlling intraocular pressure. Future research should aim to elucidate the three-dimensional structure of AFAP1 in complex with its binding partners, clarify the tissue-specific functions of AFAP1 isoforms, and develop approaches to selectively target AFAP1 function therapeutically with minimal toxicity to normal tissues. The remarkable functional versatility of AFAP1—coupling multiple signaling inputs to coordinate changes in actin filament organization across diverse cellular contexts—exemplifies how multidomain scaffold proteins achieve regulatory specificity through modular domain architecture and selective binding partner interactions.

## Citations

1. https://en.wikipedia.org/wiki/AFAP1
2. https://www.medsci.org/v14p1022.htm
3. https://zfin.org/ZDB-GENE-100316-6
4. https://www.ncbi.nlm.nih.gov/gene/60312
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC4302073/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3085893/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC11114525/
8. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=60312
9. https://maayanlab.cloud/Harmonizome/gene/AFAP1
10. https://www.uniprot.org/uniprotkb/Q8N556/entry
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC11772456/
12. https://www.oncotarget.com/article/16880/text/
13. https://onlinelibrary.wiley.com/doi/full/10.1002/cam4.237
14. https://pubchem.ncbi.nlm.nih.gov/protein/P12931
15. https://www.proteinatlas.org/ENSG00000196526-AFAP1
16. https://www.deciphergenomics.org/gene/afap1/overview/clinical-info
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC9509167/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC3711196/
19. https://pubmed.ncbi.nlm.nih.gov/31081081/
20. https://www.proteinatlas.org/ENSG00000196526-AFAP1/tissue
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC3085414/
22. https://www.europeanreview.org/wp/wp-content/uploads/3284-3290.pdf
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC1456526/
24. https://pubmed.ncbi.nlm.nih.gov/12058076/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC4177327/
26. https://www.pnas.org/doi/10.1073/pnas.2202723119
27. https://www.molbiolcell.org/doi/abs/10.1091/mbc.e02-01-0018
28. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.777849/full
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC5110387/
30. https://pubmed.ncbi.nlm.nih.gov/17520695/
31. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.681576/full
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC515031/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC4303145/
34. https://olink.com/assay/explore/oncology/proto-oncogene-tyrosine-protein-kinase-src
35. https://string-db.org/network/9031.ENSGALP00000036444
36. https://www.uniprot.org/uniprotkb/P12931/entry
37. https://stacks.cdc.gov/view/cdc/192171/cdc_192171_DS1.pdf
38. https://www.uniprot.org/uniprotkb/Q90738/entry
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC9835296/
40. https://platform.opentargets.org/target/ENSG00000196526
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC5885413/