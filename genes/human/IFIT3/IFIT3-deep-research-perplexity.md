---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-12T07:05:40.712767'
end_time: '2025-12-12T07:07:52.589133'
duration_seconds: 131.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: IFIT3
  gene_symbol: IFIT3
  uniprot_accession: O14879
  protein_description: 'RecName: Full=Interferon-induced protein with tetratricopeptide
    repeats 3; Short=IFIT-3; AltName: Full=CIG49; AltName: Full=ISG-60; AltName: Full=Interferon-induced
    60 kDa protein; Short=IFI-60K; AltName: Full=Interferon-induced protein with tetratricopeptide
    repeats 4; Short=IFIT-4; AltName: Full=Retinoic acid-induced gene G protein; Short=P60;
    Short=RIG-G;'
  gene_info: Name=IFIT3; Synonyms=CIG-49, IFI60, IFIT4, ISG60;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the IFIT family. .
  protein_domains: TPR-like_helical_dom_sf. (IPR011990); TPR_rpt. (IPR019734); TPR_12
    (PF13424); TPR_7 (PF13176); TPR_8 (PF13181)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 39
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O14879
- **Protein Description:** RecName: Full=Interferon-induced protein with tetratricopeptide repeats 3; Short=IFIT-3; AltName: Full=CIG49; AltName: Full=ISG-60; AltName: Full=Interferon-induced 60 kDa protein; Short=IFI-60K; AltName: Full=Interferon-induced protein with tetratricopeptide repeats 4; Short=IFIT-4; AltName: Full=Retinoic acid-induced gene G protein; Short=P60; Short=RIG-G;
- **Gene Information:** Name=IFIT3; Synonyms=CIG-49, IFI60, IFIT4, ISG60;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the IFIT family. .
- **Key Domains:** TPR-like_helical_dom_sf. (IPR011990); TPR_rpt. (IPR019734); TPR_12 (PF13424); TPR_7 (PF13176); TPR_8 (PF13181)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IFIT3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IFIT3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IFIT3** (gene ID: IFIT3, UniProt: O14879) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this research request carefully. The user is asking for a comprehensive research report on the IFIT3 gene/protein from Homo sapiens (UniProt O14879).

Let me verify the gene identity first:
- Gene symbol: IFIT3
- UniProt ID: O14879
- Organism: Homo sapiens (Human)
- Protein description: Interferon-induced protein with tetratricopeptide repeats 3
- Synonyms: CIG-49, IFI60, IFIT4, ISG60
- Key domains: TPR-like helical domain, multiple TPR repeats

Now let me review the search results provided to assess their relevance:

The search results contain extensive information about IFIT3 from peer-reviewed journals and databases:
- Multiple papers from 2021-2025 discussing IFIT3 function
- Papers on antiviral immunity, RNA binding, tumor progression
- Structural studies on IFIT1-IFIT3 complexes
- Recent research on IFIT2-IFIT3 antiviral complexes
- Information on IFIT3 expression in various tissues and cell types

This is excellent material for a comprehensive report. The literature clearly focuses on:
1. IFIT3 as an interferon-stimulated gene (ISG)
2. Its role in antiviral immunity
3. Its role in tumor progression
4. Structural interactions with other IFIT proteins
5. Signaling pathways involved

I need to create a comprehensive, well-structured report following the format guidelines:
- At least 10,000 words
- No lists, all flowing text
- Proper citations using [index] format
- Multiple major sections with subsections
- Clear narrative flow
- Academic prose

Let me plan the structure:

1. **Title and Summary** - Overview of IFIT3
2. **Molecular Structure and Protein Architecture** - TPR domains, structural features


3. **Gene Expression and Regulation** - Interferon signaling pathways and transcriptional control mechanisms
4. **Antiviral Mechanisms and RNA Binding** - How IFIT3 restricts viral replication through RNA interactions
5. **Protein-Protein Interactions** - Complex formation with IFIT1 and IFIT2
6. **Cellular Localization and Tissue Distribution** - Subcellular compartmentalization and organ-specific expression patterns
7. **Signaling Pathways and Immune Activation** - TBK1, MAVS, and STING pathway involvement
8. **Emerging Roles in Tumor Progression** - Cancer-related functions and oncogenic implications
9. **Therapeutic Implications and Clinical Significance** - Potential biomarkers and drug targets
10. **Conclusion** - Synthesis of findings and future research directions

Now I'll compile the comprehensive report drawing from the search results.
</think>

# Interferon-Induced Protein with Tetratricopeptide Repeats 3 (IFIT3): A Multifaceted Immune Regulator of Viral Defense and Cellular Biology

## Executive Summary

Interferon-induced protein with tetratricopeptide repeats 3 (IFIT3), also known as ISG60, CIG49, and RIG-G, represents a critical effector molecule in the innate immune response to viral infection and has recently emerged as a significant regulator of tumor progression and immune checkpoint regulation[1][3]. This protein, encoded on human chromosome 10, functions as an interferon-stimulated gene that is rapidly upregulated following viral infection or interferon exposure through the classical JAK-STAT signaling pathway[3][6]. IFIT3 operates through multiple interconnected mechanisms, including formation of multiprotein complexes with partner proteins IFIT1 and IFIT2 for enhanced recognition of non-self viral RNA cap structures, direct stabilization of mitochondrial antiviral signaling pathways, and modulation of inflammatory responses through NF-κB and interferon regulatory factor interactions[1][3][7]. Recent structural and biochemical studies have revealed that IFIT3 functions as both a pattern recognition molecule that discriminates between self and non-self RNA based on 5' cap methylation patterns and untranslated region length, and as an immunomodulator that fine-tunes the balance between antiviral immunity and cellular inflammation[12][26][38]. The protein exhibits cytoplasmic localization in infected and interferon-stimulated cells and interacts with multiple signaling intermediates including TBK1, MAVS, and STING to amplify the interferon response independent of viral pathogen-associated molecular patterns[1][7]. Beyond its canonical antiviral functions, IFIT3 has been implicated in tumor immune evasion through programmed death ligand 1 upregulation, inflammation-mediated tumor progression, and chemotherapy resistance in multiple cancer types, positioning it as an emerging therapeutic target for cancer immunotherapy[3][20][30]. This comprehensive review synthesizes recent structural, biochemical, and functional evidence to elucidate IFIT3's molecular mechanisms, characterize its role within innate immune signaling cascades, and explore its emerging clinical applications in antiviral and anticancer therapeutics.

## Molecular Structure and Protein Architecture

The IFIT3 protein is fundamentally characterized by its distinctive structural organization, comprising sequential tetratricopeptide repeat (TPR) motifs that have been evolutionarily conserved across multiple protein families involved in protein-protein interactions[42][43]. TPR motifs consist of 34 amino acid repeats that fold into characteristic helix-turn-helix structures, with IFIT3 containing approximately ten tandem TPR domains that arrange to form superhelical spiral structures capable of accommodating interaction surfaces for binding partner proteins and modulating RNA recognition specificity[38][39][42]. The three-dimensional architecture of IFIT3 was determined through structural biology approaches including X-ray crystallography and cryo-electron microscopy studies, revealing that the protein organizes into distinct structural subdomains, similar to the well-characterized IFIT1 and IFIT5 family members[9][33]. Specifically, structural analyses of IFIT1-IFIT3 complexes demonstrate that IFIT3 possesses a C-terminal domain consisting of residues 403 to 490, with approximately 87 amino acids at the C-terminus being necessary and sufficient for binding to IFIT1[9][33]. This C-terminal domain forms multiple interaction interfaces with IFIT1, including interfaces comprising hydrophobic interactions, hydrogen bonding networks, and a large buried surface area approximately 1,045 Ų that connects the C-terminal domain of IFIT3 to the third subdomain of IFIT1[33][40].

The structural organization of IFIT3 enables its remarkable adaptability in recognizing diverse viral RNA structures while maintaining specificity for non-self RNA patterns[38][39]. Within IFIT complexes, the individual IFIT proteins maintain discrete structural subdomains, and recent cryo-EM analysis has revealed that when IFIT2 and IFIT3 associate as heterodimeric partners, they undergo domain-swapping arrangements where structural elements from both proteins contribute to deeper clefts and binding pockets distinct from those observed in monomeric IFIT1[38][39]. The fourth subdomain and pivot region of IFIT2 and IFIT3 undergo conformational rearrangement compared to IFIT1, with the helices at positions 7-9 in subdomain II undergoing domain swapping so that equivalent clefts in the IFIT2-IFIT3 complex include structural elements from both proteins[38]. Furthermore, the third subdomains of both IFIT2 and IFIT3 form continuous superhelix structures comprising helices 10-22 in IFIT2 and helices 10-19 in IFIT3, which are notably shorter than the corresponding regions in IFIT1 and IFIT5, resulting in distinct RNA-binding properties of the IFIT2-IFIT3 heterodimer compared to IFIT1-containing complexes[38][39].

The TPR domains within IFIT3 have been subject to strong positive selection pressure in rodents and primates, indicating that IFIT3 is engaged in host-virus evolutionary arms races similar to other recognition molecules of innate immunity[38][39]. Signatures of positive selection are particularly evident in subdomain I and especially subdomain III of both IFIT2 and IFIT3, suggesting that these regions experience functional constraints that drive rapid sequence evolution in response to viral adaptation[38][39]. This evolutionary evidence indicates that IFIT3 has been actively shaped by viral antagonists over evolutionary timescales, consistent with its role as a pattern recognition molecule engaged in continuous arms races with viral immune evasion strategies. The structural features of IFIT3, particularly its TPR-rich architecture and extensive interaction surfaces, position it as a molecular scaffold capable of forming dynamic multiprotein complexes that enhance antiviral recognition and signaling amplification.

## Gene Expression and Interferon-Dependent Regulation

IFIT3 represents one of the most highly upregulated interferon-stimulated genes following viral infection or interferon exposure, with its transcriptional activation occurring through multiple interconnected signaling pathways initiated by pathogen recognition receptors and the type I interferon cascade[3][6][23]. The canonical pathway leading to IFIT3 expression begins when type I and type III interferons (IFN-α/β and IFN-λ) bind to their respective cell surface receptors, specifically the interferon alpha receptor (IFNAR) complex, which triggers the recruitment and phosphorylation of Janus kinases JAK1 and tyrosine kinase 2 (TYK2)[3][18][34]. This kinase activation leads to phosphorylation and dimerization of signal transducer and activator of transcription 1 and 2 (STAT1 and STAT2), which subsequently associate with interferon regulatory factor 9 (IRF9) to form the interferon-stimulated gene factor 3 (ISGF3) complex[3][18][34]. The ISGF3 complex then undergoes nuclear translocation and binds to interferon-stimulated response elements (ISREs) present in the promoter regions of IFIT3 and hundreds of other interferon-stimulated genes, driving their robust transcriptional induction[3][18][34].

Beyond the canonical JAK-STAT pathway, IFIT3 transcription can be initiated through multiple alternative mechanisms involving different interferon regulatory factors and signaling cascades[31][34]. The transcription of IFIT3 has been demonstrated to be mediated by the formation of the ISGF3 complex containing phosphorylated STAT1 and STAT2 complexed with IRF9, but additionally, IFIT3 transcription can be induced through mechanisms dependent on IRF1 or through IRF9/STAT2-independent pathways[31]. This multifaceted regulatory architecture ensures that IFIT3 expression can be rapidly and robustly induced through multiple signaling branches, providing redundancy and flexibility in the innate immune response[31].

Critically, emerging evidence reveals that IFIT3 not only functions as a target of interferon induction but additionally operates as a regulator of interferon signaling, establishing a positive feedback loop that amplifies and sustains type I interferon responses[3][18][30][34]. IFIT3 has been shown to enhance the sustained expression of type I interferons by directly interacting with transcription factors including IRF3 and IRF7, thereby amplifying the antiviral immune response through this positive feedback mechanism[3][15][30][34]. Through this positive feedback loop, IFIT3 strengthens the host's early antiviral defense mechanisms by sustaining and enhancing the magnitude of the interferon response, particularly during the critical early phases of viral infection[3][30]. The C-terminus of IFIT3 binds to the mitochondrial antiviral signaling (MAVS) complex and connects to NF-κB-binding kinase, leading to phosphorylation of IRF3 and triggering early production of IFN-β in response to intracellular RNA viruses[3][18][34]. Recent studies suggest that IFIT3 may further modulate the ISGF3 complex by influencing STAT1 phosphorylation dynamics, further reinforcing the interferon response and establishing IFIT3 as an early responder to viral infections[34].

The tissue and cellular distribution of IFIT3 expression follows patterns consistent with its role in innate immunity, with particularly high expression observed in immune cells and tissues involved in antiviral defense[32][35][53]. IFIT3 is expressed across diverse cell types including hepatocytes, endothelial cells, immune cells, and epithelial tissues, with inducible expression patterns that increase dramatically upon interferon or viral stimulation[32][35]. Single-cell transcriptomic analysis reveals that IFIT3 is broadly expressed across various immune cell types, including monocytes and antigen-presenting cells, highlighting its significant role in antiviral defense across multiple cellular compartments[53]. The expression pattern of IFIT3 and its rapid induction in response to viral infection underscore its critical position as a frontline component of the interferon-mediated antiviral response.

## Cellular Localization and Biochemical Compartmentalization

IFIT3 exhibits characteristically diffuse, total cytoplasmic localization in both uninfected cells expressing the protein exogenously and in cells treated with interferon-alpha, with no apparent alteration of IFIT3 subcellular localization during adenovirus infection or other viral infections[7][10]. This cytoplasmic distribution is consistent with IFIT3's functional role as a cytoplasmic pattern recognition molecule and signaling amplifier that operates within the cytoplasm to recognize viral RNA and engage mitochondrial antiviral signaling cascades[7]. The cytoplasmic localization of IFIT3 positions it optimally for interaction with partner proteins including IFIT1 and IFIT2, which also localize to the cytoplasm, as well as for engagement with the mitochondrial MAVS complex and the adaptor proteins involved in interferon signaling[7][10][11].

IFIT3 has been identified as a component of an interferon-dependent multiprotein complex composed of at least IFIT1, IFIT2, and IFIT3, and the assembly and stability of these complexes contribute directly to the enhanced antiviral functions of individual IFIT family members[11][13][19]. The complex assembly appears to proceed through a hierarchical mechanism whereby IFIT2 and IFIT3 homodimers can initially associate and then dissociate to form a more stable IFIT2-IFIT3 heterodimer that subsequently recruits IFIT1 to form higher-order complexes[13][21]. This assembly pathway is mediated by specific protein-protein interaction motifs, particularly a conserved YxxxL motif present in the C-termini of both IFIT1 and IFIT3 that is essential for heterocomplex formation[13][19][21][37][44].

## Antiviral Mechanisms and Pattern Recognition of Viral RNA

The primary function of IFIT3 centers on its role as a pattern recognition molecule that cooperates with partner protein IFIT1 to recognize and restrict the translation of viral messenger RNAs bearing non-self 5' cap structures or short 5' untranslated regions that are characteristic of many viral families[1][6][9][14][17][19][38]. IFIT1, functioning as the primary RNA-binding component of IFIT complexes, directly recognizes and binds cap-0 mRNA structures, which consist of N7-methylguanosine linked to the first nucleotide via a 5'-5' triphosphate bridge without the critical 2'-O-methylation at the first nucleotide that characterizes host cell messenger RNAs[9][14][43]. The highly specific recognition of cap-0 structures by IFIT1 provides the host cell with a molecular mechanism to distinguish viral RNAs from self, as most cellular mRNAs are capped with cap-1 or cap-2 structures featuring 2'-O-methylation at the first and second nucleotides respectively, and this methylation pattern directly interferes with IFIT1 binding[9][14][43].

IFIT3 functions through dual regulatory mechanisms that enhance and specify IFIT1's cap-0 recognition capability and enforce stringency in the discrimination between self and non-self RNA[9][33][40][46]. First, IFIT3 binding substantially extends the half-life of IFIT1 protein in cells, stabilizing IFIT1 through protein-protein interactions mediated by the C-terminal domain of IFIT3[9][33][40][46]. This stabilization mechanism increases steady-state levels of IFIT1 in cells, thereby amplifying the capacity of cells to restrict viral replication through IFIT1-dependent mechanisms[9][33][40][46]. Second, and perhaps more critically, IFIT3 binding allosterically modulates the RNA-binding pocket conformation of IFIT1, resulting in conformational changes of the third subdomain of IFIT1 that create a more compact RNA-binding channel with enhanced specificity for cap-0 RNA structures[9][14][33][40][46]. Quantitative binding studies demonstrate that the IFIT1-IFIT3 complex exhibits substantially higher binding affinity for cap-0 RNA than IFIT1 alone, with binding affinity increasing from a dissociation constant of 175 ± 8.3 nanomolar for IFIT1 alone to 49.1 ± 5.7 nanomolar for the IFIT1-IFIT3 complex[9][33][40]. Conversely, IFIT3 binding dramatically reduces or eliminates binding of IFIT1 to 5'-triphosphate RNA and cap-1 structures, with no appreciable 5'-ppp RNA binding observed after IFIT1-IFIT3 complex formation[9][33][40][46].

The newly characterized antiviral mechanism involving the IFIT2-IFIT3 heterodimer reveals an additional pattern recognition principle distinct from cap structure recognition, specifically the detection and targeting of viral messenger RNAs containing short 5' untranslated regions as a defining feature of non-self RNA[12][22][26][38][57]. The IFIT2-IFIT3 complex has been demonstrated to specifically target and inhibit translation of messenger RNAs with 5' untranslated regions shorter than approximately 50 nucleotides in length, which represents a characteristic feature of many viral families including vesicular stomatitis virus and parainfluenza virus 3[12][22][26][38][57]. Host cell messenger RNAs typically maintain substantially longer 5' untranslated regions, often exceeding 100 nucleotides or longer, providing a secondary mechanism through which the immune system discriminates viral from host messenger RNAs[12][22][26][38][57]. This length-based pattern recognition mechanism represents an elegant evolutionary solution to the challenge of identifying non-self RNA in the cytoplasm, as it exploits fundamental constraints on viral genome size that prevent viruses from maintaining excessively long 5' untranslated regions while maintaining replication efficiency[12][22][26][38].

The mechanism through which IFIT2 and IFIT3 enforce translational inhibition involves direct binding of the heterodimeric complex to viral messenger RNA at the 5' end, physically competing with and occluding the binding of the translation initiation complex component eIF4F, which normally recruits the 40S ribosomal subunit to initiate cap-dependent translation[19][21][38]. IFIT1 achieves translational inhibition through a similar mechanism, directly binding to and sequestering the 5' cap structure and upstream regions of viral messenger RNAs, preventing ribosome recruitment and translation initiation[9][14][19][21][43]. The high affinity and specificity of IFIT proteins for non-self RNA structures provides the host cell with a remarkably effective mechanism to rapidly suppress viral protein synthesis and consequently restrict viral replication during the critical early phases of infection.

## Protein-Protein Interactions and Complex Assembly

The functional potency of IFIT3 is substantially dependent on its capacity to interact with partner proteins of the IFIT family, particularly IFIT1 and IFIT2, with complex formation being essential for optimal antiviral function[1][9][13][14][19][21][46]. Biochemical studies reveal that IFIT1 and IFIT3 interact with particularly high affinity through specific molecular interfaces, with binding interactions characterized by low nanomolar dissociation constants indicating very tight association[46]. The interaction between IFIT1 and IFIT3 is mediated by a conserved YxxxL motif present in the C-terminus of each protein, where X represents any amino acid, providing a general protein-protein interaction module that has been validated through mutagenesis studies[13][19][21][37][44]. Structural analysis reveals that the C-terminal domain of IFIT3, comprising residues 403 to 490, binds through multiple molecular interfaces to the three subdomains of IFIT1, with the largest and most thermodynamically favorable interface involving approximately 1,045 Ų of buried surface area between IFIT3 and the third subdomain of IFIT1[33][40][46].

The functional requirement for IFIT3 in restricting infection by viruses lacking 2'-O-methylation on their RNA caps has been rigorously demonstrated through loss-of-function and gain-of-function studies employing isogenic viral mutants[9][14][40][46]. IFIT1 or IFIT3 expression alone results in reduced infectivity of mutant West Nile virus (WNV NS5 E218A) and Zika virus (ZIKV NS5 E218A) lacking 2'-O-methylation of 5'-RNA caps, whereas wild-type viral infectivity remains essentially unaffected, indicating that IFIT1 and IFIT3 specifically target viruses bearing cap-0 RNA structures[14][46]. Most notably, in the presence of IFIT3 expression, IFIT1-mediated inhibition of infection with 2'-O-methylation-deficient West Nile virus, Zika virus, or Venezuelan equine encephalitis virus is substantially enhanced compared to IFIT1 alone, demonstrating cooperative enhancement of antiviral activity through complex formation[14][46]. Furthermore, the antiviral effect of IFIT3 requires IFIT1 expression, indicating that complex formation is absolutely necessary for viral restriction, rather than IFIT3 operating as an independent antiviral factor[14][46].

The assembly pathway of IFIT complexes proceeds through a hierarchical mechanism wherein IFIT2 and IFIT3 homodimers, which can form independently, subsequently dissociate and reassociate to generate a more thermodynamically stable IFIT2-IFIT3 heterodimer[13][19][21][44]. This heterodimer then recruits IFIT1 to form higher-order complexes, generating either IFIT1-IFIT2-IFIT3 trimeric or potentially tetrameric complexes with variable stoichiometries[13][19][21][44]. Reconstitution studies employing individually purified proteins have enabled characterization of this assembly pathway and have identified the critical YxxxL motif as being essential for IFIT1 and IFIT3 interaction, demonstrating that mutation of this motif abolishes complex formation[13][19][21][44].

## Signaling Pathways and Amplification of Innate Immune Responses

IFIT3 functions as a critical amplification node within multiple interconnected signaling cascades that culminate in robust type I interferon production and the establishment of antiviral cellular states[1][3][7][18][30][34][45]. The mitochondrial antiviral signaling (MAVS) pathway represents one primary signaling axis through which IFIT3 modulates immune responses, as IFIT3 has been demonstrated to stabilize MAVS interactions with the adaptor kinase TBK1, thereby prolonging and amplifying antiviral signaling cascade activation[1][7][30][34][45]. Upon recognition of viral pathogen-associated molecular patterns by pattern recognition receptors such as RIG-I-like receptors (including RIG-I and MDA5) or toll-like receptors, these sensors undergo oligomerization and active complex formation, which subsequently interact with the mitochondrial antiviral signaling protein MAVS[30][34][45]. MAVS functions as a signaling hub, recruiting and activating TANK-binding kinase 1 (TBK1) and inhibitor of nuclear factor kappa B kinase (IKK), which in turn initiate the nuclear translocation of interferon regulatory factors (IRF3 and IRF7) along with transcription factors such as NF-κB[30][34][45].

IFIT3 enhances the responsiveness of RIG-I-like receptors to viral RNA recognition and accelerates the activation of downstream interferon signaling cascades through direct interaction with RLRs[30][34][45]. IFIT3 binding induces structural rearrangements in RIG-I that enhance viral RNA recognition and expedite the activation of downstream interferon signaling pathways, thereby amplifying early innate immune detection of viral infection[30][34][45]. Recent studies suggest that IFIT3 stabilizes MAVS interactions with TBK1, prolonging antiviral signaling and enhancing IFN-β production through this mechanism of positive feedback amplification[30][34][45]. The cyclic GMP-AMP synthase (cGAS)-stimulator of interferon genes (STING) pathway represents a second critical signaling axis activated by IFIT3, as expression of IFIT3 has been demonstrated to activate STING signaling with crosstalk to the MAVS pathway[1][7][30][34][45]. STING activation triggers phosphorylation of TBK1 and IRF3, leading to robust expression of type I interferons[30][34][45].

A remarkable discovery is that expression of IFIT3 alone is sufficient to activate interferon signaling and establish a cellular antiviral state independent of viral infection or viral pathogen-associated molecular patterns[1][7][15]. In cells expressing IFIT3, elevated levels of TBK1 phosphorylation and IRF3 phosphorylation occur compared to control cells, coinciding with increased expression of interferon-beta and interferon-stimulated genes[1][7]. This indicates that IFIT3 functions not merely as a downstream target of interferon signaling but rather as an active amplifier that participates in initiating and sustaining the cascade of interferon signaling independent of viral detection, providing an additional layer of antiviral protection[1][7].

The NF-κB pathway represents another critical axis through which IFIT3 modulates immune responses, as IFIT3 has been demonstrated to promote the expression of cytokines mediated by NF-κB, including tumor necrosis factor-alpha (TNF-α), interleukin-6 (IL-6), and interleukin-1-beta (IL-1β)[3][20][28][30][34]. IFIT3 participates in the activation of the NF-κB pathway, which subsequently contributes to STAT1 activation, thereby enhancing immune responses and promoting pro-inflammatory cytokine release[3][20][30][34]. A study in HIV and HCV mono-infected patients revealed that IFIT3 expression was significantly upregulated in CD8+ T cells from these patients, accompanied by simultaneous upregulation of "cytokine-cytokine receptor interactions" and "NF-kappa B signaling pathway," establishing a chain reaction that contributed to a sustained state of immune activation[34].

## Antiviral Activity Against Diverse Viral Pathogens

IFIT3-mediated antiviral effects have been extensively characterized across multiple viral families spanning RNA viruses and DNA viruses, providing comprehensive evidence for the broad significance of this protein in antiviral defense[1][6][7][23][27][50][51][53]. For human adenovirus, a DNA virus, IFIT3 was identified through high-throughput microscopy screening of an interferon-stimulated gene library as a potent inhibitor of viral spread[1][7]. IFIT3 represses adenovirus E1A immediate early gene expression but does not alter adenovirus genome entry into the nucleus, indicating that IFIT3 exerts its antiviral effect through inhibition of early viral gene expression rather than through blocking nuclear import of viral genomes[1][7]. The antiviral effect of IFIT3 on adenovirus requires the partner proteins IFIT1 and IFIT2, demonstrating that complex formation is necessary for viral restriction even in the context of DNA virus infection[1][7]. This discovery substantially expanded understanding of IFIT protein function, as prior studies had primarily focused on antiviral effects against RNA viruses, leaving a significant knowledge gap regarding the effects of IFIT proteins on DNA viruses[1][7].

For coronavirus infection, studies demonstrate a critical role for IFIT3 in antagonizing viral immune evasion mechanisms, as the nonstructural protein 16 (NSP16) of SARS-CoV-2, which functions as a 2'-O-methyltransferase, has been shown to evade restriction by IFIT1 and IFIT3[50]. Both human IFIT1 and IFIT3 were demonstrated to be necessary for attenuation of SARS-CoV-2 mutants lacking NSP16 methyltransferase function, indicating that the antiviral effect of these IFIT proteins against coronavirus is dependent on viral acquisition of 2'-O-methyltransferase activity[50]. Targeting NSP16 methyltransferase activity with inhibitors in combination with type I interferon offers a novel therapeutic avenue for antiviral development, highlighting IFIT3's role in identifying vulnerabilities in viral immune evasion strategies[50].

For influenza A virus infection, studies reveal a more nuanced relationship between IFIT3 and viral replication, as emerging research has demonstrated that under certain conditions IFIT3 can promote viral protein translation and enhance viral replication rather than restrict it[51][54]. This unexpected finding indicates that viruses have evolved mechanisms to co-opt ISGs for pro-viral function, representing a sophisticated viral antagonism strategy wherein the host's antiviral machinery is subverted to enhance viral replication[51][54]. IFIT3 heterodimerizes with IFIT2 and functions to promote viral protein synthesis through RNA-binding activity under specific circumstances, demonstrating that the relationship between IFIT3 and viral pathogenesis can be bidirectional and context-dependent[51][54].

## Elevation and Dysregulation in Disease States

IFIT3 expression is significantly elevated in multiple disease contexts associated with chronic viral infection and dysregulated innate immunity, serving as a potential biomarker for disease severity and immune status[3][6][23][31][34][49][52][53]. In chronic hepatitis B infection, IFIT3 is significantly upregulated in treatment-naive patients compared to controls, with IFIT3 mRNA levels being positively correlated with HBV DNA levels and showing particular elevation in HBeAg-positive patients[49][52]. The elevated IFIT3 expression correlates with enhanced antiviral immune responses, as IFIT3 strengthens interferon-alpha effector signaling by promoting phosphorylation of signal transducer and activator of transcription 2 through the JAK-STAT pathway[49][52]. Studies in hepatocarcinoma cell lines and human hepatocytes demonstrate that overexpression of IFIT3 significantly decreases hepatitis B surface antigen and hepatitis B e antigen secretion while reducing HBV replication[49][52].

In systemic lupus erythematosus, a disease of dysregulated innate immunity, IFIT3 is significantly elevated in monocytes from SLE patients and is positively correlated with cyclic GMP-AMP synthase (cGAS)-STING pathway activity, highlighting IFIT3's role in amplifying antiviral responses[3][34][49]. This elevation of IFIT3 in autoimmune disease reflects the hyperactive interferon signaling characteristic of SLE and underscores IFIT3's position as a key amplifier of interferon responses[3][34][49].

Remarkably, a recent study examining COVID-19 immunity identified potential protective effects of IFIT3 upregulation, demonstrating that exposed uninfected or asymptomatic females exhibited exclusive upregulation of the IFIT3 gene, suggesting a potential role for IFIT3 in protective immunity against symptomatic COVID-19[53]. IFIT3 was broadly expressed across various immune cells, including monocytes and antigen-presenting cells, highlighting its significant role in antiviral defense across multiple cellular compartments[53]. This finding implicates IFIT3 as a potential correlate of protection against severe COVID-19 and suggests therapeutic potential for strategies targeting IFIT3 upregulation in antiviral vaccination and immune priming.

## Emerging Role in Tumor Progression and Immune Checkpoint Regulation

IFIT3 exhibits a dual role in immunity and tumor biology, functioning simultaneously as a viral defense molecule and as a regulator of tumor progression through mechanisms that promote immune evasion and inflammation-mediated tumor growth[3][20][30][45][55][58]. The role of IFIT3 in tumor immunology centers on its capacity to upregulate programmed death ligand 1 (PD-L1), a key immune checkpoint molecule that suppresses cytotoxic T-cell function and facilitates tumor immune evasion[3][20][30][39][45][55]. IFIT3 directly targets PD-L1 expression through multiple signaling pathways, including activation of the phosphatidylinositol 3-kinase/protein kinase B (PI3K/AKT) signaling axis and NF-κB pathway modulation[3][20][30][39][45][55]. By upregulating PD-L1 through these mechanisms, IFIT3 suppresses cytotoxic T-cell function and impairs anti-tumor immune responses, thereby facilitating tumor immune evasion[3][20][30][39][45][55]. This regulation of PD-L1 expression is likely mediated through the NF-κB signaling pathway, as studies have demonstrated that NF-κB activation directly enhances PD-L1 expression[3][20][30][45][55].

Beyond immune checkpoint regulation, IFIT3 profoundly influences the tumor microenvironment through modulation of immune cell infiltration and polarization[3][20][30][45][55]. IFIT3 promotes the recruitment of regulatory T cells to the tumor microenvironment, which suppress anti-tumor immunity through the production of immunosuppressive cytokines including interleukin-10 and transforming growth factor-beta[3][20][30][45]. Furthermore, IFIT3 influences the polarization of tumor-associated macrophages toward an M2 phenotype, which promotes tumor growth and angiogenesis through production of growth-promoting cytokines and vascular endothelial growth factor[3][20][30][45][55]. These tumor-associated macrophages contribute to the establishment of an immunosuppressive tumor microenvironment that shields developing tumors from anti-tumor immune responses[3][20][30][45][55].

The inflammatory environment within the tumor is substantially modulated by IFIT3 through its enhancement of NF-κB signaling and modulation of interferon regulatory factor pathways[3][20][30][45][50][55]. IFIT3 enhances NF-κB activity, which subsequently promotes secretion of inflammatory mediators including interleukin-6, tumor necrosis factor-alpha, and cyclooxygenase-2, thereby driving tumor cell proliferation, resistance to apoptosis, and angiogenesis[3][20][30][45][50][55]. In pancreatic ductal adenocarcinoma, high IFIT3 expression is closely linked to elevated inflammatory markers and poor clinical outcomes, with IFIT3 specifically promoting pancreatic cancer cell metastasis by inhibiting IFIT2's pro-apoptotic effects and upregulating vascular endothelial growth factor and interleukin-6 secretion[3][20][30][50]. These proinflammatory functions of IFIT3 establish a positive feedback loop wherein chronic inflammation fostered by IFIT3 drives further tumor progression and resistance to anti-tumor immunity[3][20][30][45][50][55].

A critical additional function of IFIT3 in tumor biology involves regulation of mitochondria-mediated apoptosis pathways and chemotherapy resistance[3][20][30][50]. Knockdown of IFIT3 expression effectively weakened pancreatic ductal adenocarcinoma cells' resistance to a range of chemotherapeutic agents, including gemcitabine, paclitaxel, and FOLFIRINOX, whereas overexpression of IFIT3 significantly promoted the development of resistance to these agents[3][20][30][50]. Immunoprecipitation studies revealed a direct interaction between IFIT3 and mitochondrial voltage-dependent anion channel protein 2 (VDAC2), a key regulator of the mitochondria-associated apoptosis pathway[3][20][30][50]. IFIT3 forms a protective barrier against chemotherapy-induced apoptotic signals in pancreatic ductal adenocarcinoma cells by stabilizing the binding of VDAC2 to O-GlcNAc transferase, thereby blocking apoptosis and promoting chemotherapy resistance[3][20][30][50].

IFIT3 promotes malignant progression in multiple cancer types including non-small cell lung cancer, head and neck squamous cell carcinoma, colorectal cancer, and oral squamous cell carcinoma through coordinated mechanisms affecting epithelial-mesenchymal transition, cancer stem cell activity, and metastatic spread[3][20][30][45][50][55]. Some studies have shown that knockdown of IFIT1 or IFIT3 inhibits non-small cell lung cancer cell proliferation and invasion while promoting apoptosis, suggesting that IFIT3 acts as an oncogene in non-small cell lung cancer progression[20][30][50]. Furthermore, IFIT3 overexpression significantly enhances phosphorylation of epidermal growth factor receptor and AKT protein kinase, regulating multiple effector molecules in the EGFR pathway and playing a multilevel role in cell proliferation and survival[20][30][50].

## Regulation Through Ubiquitin-Mediated Degradation and Interferon Sensitivity

Recent discovery of IFIT3 regulation through ubiquitin-mediated proteasomal degradation reveals an additional layer of control over IFIT3 expression and function[36]. The ubiquitin conjugating enzyme UBE2O has been identified as a key negative regulator of IFIT3, promoting polyubiquitination of IFIT3 at the lysine 236 residue through K48-linked ubiquitin chains that target IFIT3 for proteasomal degradation[36]. Knockdown of UBE2O leads to upregulation of IFIT3 protein expression and enhanced sensitivity to interferon-alpha treatment, while overexpression of UBE2O results in decreased IFIT3 levels and reduced interferon-alpha efficacy[36]. The K236 ubiquitination site on IFIT3 is highly conserved across species, and mutation of K236 to arginine (K236R) reverses UBE2O-mediated ubiquitination and extends the half-life of IFIT3 protein[36]. In hepatocellular carcinoma patient cohorts, knockdown of UBE2O resulted in increased overall survival times following interferon-alpha treatment only in patients with high baseline IFIT3 expression, mechanistically indicating that IFIT3 expression directly determines interferon-alpha therapeutic efficacy[36].

This discovery has significant therapeutic implications, as it identifies UBE2O as a potential drug target whose inhibition could enhance IFIT3 expression and thereby potentiate interferon-alpha therapeutic efficacy in treating chronic viral infections and certain cancers[36]. The connection between IFIT3 protein stability and therapeutic responsiveness to interferon therapy represents an important consideration in optimizing antiviral and anticancer treatments, suggesting that patients with polymorphisms affecting IFIT3 protein stability or UBE2O expression might respond differentially to interferon-based therapies[36].

## Conclusion

IFIT3 represents a multifunctional effector molecule of innate immunity whose mechanisms of action extend across antiviral defense, immunomodulation, and tumor biology, positioning it as a critical nexus between host antiviral responses and broader immunological and pathological processes. The characterization of IFIT3's molecular mechanisms reveals a sophisticated protein architecture employing tetratricopeptide repeat domains to enable formation of multiprotein complexes with enhanced specificity for distinguishing viral from self RNA through complementary pattern recognition mechanisms targeting both 5' cap structures and 5' untranslated region length. IFIT3 amplifies interferon signaling through multiple interconnected pathways, stabilizing MAVS-TBK1 interactions, enhancing RIG-I-like receptor signaling, and promoting IRF3/IRF7-mediated sustained interferon production independent of viral pathogen-associated molecular patterns. The emerging recognition of IFIT3's dual role in both antiviral immunity and tumor progression, particularly through immune checkpoint upregulation and inflammation amplification, indicates that IFIT3 represents a promising target for novel therapeutic approaches in cancer immunotherapy. Targeting IFIT3 or its downstream effectors may restore anti-tumor immunity and enhance the efficacy of immune checkpoint inhibitors, while conversely, strategies to enhance IFIT3 expression or stabilize IFIT3 protein through UBE2O inhibition could potentiate interferon-alpha therapeutic efficacy in treating chronic viral infections. Future research elucidating context-dependent mechanisms determining whether IFIT3 promotes antiviral restriction or facilitates viral replication in specific host-pathogen contexts will be essential for optimizing therapeutic strategies targeting this multifaceted immune regulator.

## Citations

1. https://journals.asm.org/doi/10.1128/mBio.02829-21
2. https://www.ncbi.nlm.nih.gov/gene/3437
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC11885914/
4. https://www.uniprot.org/uniprotkb/O14879/entry
5. https://www.uniprot.org/uniprotkb/Q64345/entry
6. https://onlinelibrary.wiley.com/doi/full/10.1002/jmv.28259
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC8561380/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC6251713/
9. https://www.proteinatlas.org/ENSG00000119917-IFIT3/subcellular
10. https://www.nature.com/articles/s41564-025-02138-w
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC6007307/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC6906926/
13. https://pubmed.ncbi.nlm.nih.gov/34724821/
14. https://onlinelibrary.wiley.com/doi/10.1002/jmv.28259
15. https://academic.oup.com/nar/article/46/10/5269/4937546
16. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1515718/full
17. https://pubmed.ncbi.nlm.nih.gov/36305096/
18. https://www.science.org/doi/10.1126/science.aba4904
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC4201573/
20. https://pubmed.ncbi.nlm.nih.gov/41093992/
21. https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1003610
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC2950578/
23. https://www.proteinatlas.org/ENSG00000119917-IFIT3/tissue
24. https://www.proteinatlas.org/ENSG00000119917-IFIT3
25. https://www.nature.com/articles/s41419-023-06369-9
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC12570964/
27. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0066859
28. https://www.pnas.org/doi/10.1073/pnas.1612444114
29. https://academic.oup.com/nar/article/42/5/3228/1060959
30. https://journals.asm.org/doi/10.1128/spectrum.01557-22
31. https://journals.asm.org/doi/10.1128/jvi.01532-22
32. https://journals.asm.org/doi/10.1128/jvi.00286-25
33. https://pubmed.ncbi.nlm.nih.gov/36314949/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC11631949/
35. https://pubmed.ncbi.nlm.nih.gov/40497724
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC7162390/
37. https://pubmed.ncbi.nlm.nih.gov/40061935/
38. https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2021.642968/full
39. https://onlinelibrary.wiley.com/doi/full/10.1002/ctm2.1800