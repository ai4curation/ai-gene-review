---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-30T19:43:45.807207'
end_time: '2026-01-30T19:46:08.125923'
duration_seconds: 142.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: atg38
  gene_symbol: atg38
  uniprot_accession: O94427
  protein_description: 'RecName: Full=PtdIns3K complex I subunit atg38 {ECO:0000305};
    AltName: Full=Meiotically up-regulated gene 167 protein;'
  gene_info: Name=atg38 {ECO:0000312|PomBase:SPBC660.08}; Synonyms=mug167; ORFNames=SPBC660.08
    {ECO:0000312|PomBase:SPBC660.08};
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the ATG38 family. .
  protein_domains: MIT_dom_sf. (IPR036181)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 53
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O94427
- **Protein Description:** RecName: Full=PtdIns3K complex I subunit atg38 {ECO:0000305}; AltName: Full=Meiotically up-regulated gene 167 protein;
- **Gene Information:** Name=atg38 {ECO:0000312|PomBase:SPBC660.08}; Synonyms=mug167; ORFNames=SPBC660.08 {ECO:0000312|PomBase:SPBC660.08};
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the ATG38 family. .
- **Key Domains:** MIT_dom_sf. (IPR036181)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atg38" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atg38' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atg38** (gene ID: atg38, UniProt: O94427) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# The ATG38 Protein: A Critical Fifth Subunit of the Autophagy-Specific Phosphatidylinositol 3-Kinase Complex I in Schizosaccharomyces pombe

## Executive Summary

ATG38, a 26 kilodalton protein encoded by the *atg38* gene (also known as *mug167* or *SPBC660.08*) in the fission yeast *Schizosaccharomyces pombe*, serves as an essential fifth subunit of the autophagy-specific phosphatidylinositol 3-kinase (PI3K) complex I that orchestrates the formation of autophagosomes during nutrient starvation and cellular stress responses[1][12][30]. This protein functions as a physical linkage mechanism connecting the Vps15–Vps34 catalytic arm and the Atg14–Vps30 regulatory arm of complex I, stabilizing the overall complex architecture and enabling efficient localization to the pre-autophagosomal structure (PAS)[12][30]. Structurally, Atg38 comprises an N-terminal MIT (microtubule interaction and transport) domain that mediates interactions with complex I subunits, an intrinsically disordered region, and a C-terminal coiled-coil homodimerization domain that is critical for both membrane targeting and PAS localization[17][27]. Functionally unique to *S. pombe*, Atg38 also contains a conserved Atg8-family-interacting motif (AIM) that directly engages with lipidated Atg8 on autophagosomal membranes, establishing a remarkable positive feedback loop that amplifies PI3K complex I recruitment and dramatically enhances autophagosome biogenesis efficiency[1]. This report provides a comprehensive analysis of Atg38's molecular organization, functional roles within autophagy, evolutionary context, and significance in cellular nutrient adaptation.

## Discovery and Identification of ATG38 in Fission Yeast

The *atg38* gene was identified through functional genomic screening approaches designed to uncover genes critical for autophagy regulation in *S. pombe*[12]. Initial discovery emerged from genetic suppressor screens examining the *isp6Δ* mutant, a strain lacking the vacuolar protease Isp6, which exhibits severe viability defects following nitrogen starvation[1]. When researchers applied piggyBac transposon-based mutagenesis to suppress this lethal phenotype, the resulting mutant strains revealed *atg38* as a critical autophagy gene whose disruption could partially rescue the *isp6Δ* lethality, suggesting that blocking autophagy could compensate for protease deficiency[1]. The protein product of *atg38* was initially uncharacterized and designated as the open reading frame YLR211c in budding yeast *Saccharomyces cerevisiae*, but subsequent work in fission yeast demonstrated its fundamental importance in macroautophagy[12].

The alternative designation of Atg38 as the meiotically up-regulated gene 167 (MUG167) protein reflects its identification in transcriptomic studies examining gene expression changes during the transition from vegetative growth to meiosis in fission yeast[3][43]. However, the primary function of Atg38 is not meiosis-specific; rather, it represents a housekeeping component of the autophagy machinery that is essential for both vegetative autophagy and the nitrogen starvation response that precedes sexual differentiation. The dual naming convention reflects the different experimental contexts in which the gene was discovered, highlighting how comprehensive functional characterization often emerges from multiple biological perspectives.

## Molecular Structure and Protein Architecture

The Atg38 protein exhibits a highly modular architecture comprising three major functional regions that mediate distinct aspects of its role in autophagy[17][27][30][55]. The complete protein spans 226 amino acids in *S. cerevisiae* (with similar length in *S. pombe*) and has an estimated molecular mass of approximately 26 kilodaltons[12][30]. The N-terminal region encompasses residues spanning roughly the first 78 amino acids and contains a MIT (microtubule interaction and transport) domain composed of three α-helices arranged in a characteristic bundle structure[17][27]. This MIT domain is highly conserved across eukaryotic Atg38 orthologs and serves as the primary determinant of interaction with other PI3K complex I components, specifically recognizing and binding to the Vps30-Atg14 subcomplex[17]. Hydrogen-deuterium exchange mass spectrometry (HDX-MS) studies have demonstrated that the Atg38 MIT domain undergoes significant protection from solvent exchange when bound to complex I, indicating intimate molecular contacts and conformational stabilization upon binding[17].

The central region of Atg38 consists of an intrinsically disordered region (IDR) containing connecting linkers that provide flexibility and may facilitate dynamic interactions with other autophagy machinery components[55]. This region separates the MIT domain from the C-terminal structure and contributes to the overall solubility and biochemical behavior of the protein in solution. The intrinsically disordered nature of this central segment distinguishes Atg38 from many other complex I components and may contribute functional flexibility in accommodating the conformational changes that accompany autophagosome biogenesis.

The C-terminal region, comprising residues approximately 120–226, contains predicted coiled-coil segments that organize into a distinctive homodimerization domain[12][30][55]. This C-terminal structure has been determined crystallographically at 2.2 Angstrom resolution and reveals a striking mushroom-like asymmetric homodimer architecture[27][38]. The homodimer consists of two distinct structural segments: a four-helix bundle "cap" structure at the N-terminal portion of the dimerization domain, and a parallel coiled-coil "stalk" at the C-terminal end[27][38]. Following the stalk in both yeast and mammalian orthologs is a helical extension termed the "tail" that may contribute to membrane interactions or recruitment mechanisms[55]. This distinctive three-segment architecture has no obvious structural parallels among other protein homodimerization domains and represents a novel fold discovered through structural characterization of Atg38.

The C-terminal coiled-coil domain is essential for multiple critical functions including homodimerization itself, localization to the pre-autophagosomal structure and autophagic puncta, and association with membranes[17][27][30][55]. When portions of the C-terminal domain are deleted—including disruptions of the cap, stalk, or tail segments—both homodimerization capacity and autophagosome formation efficiency are severely compromised[17][30]. The relative abundance of Atg38 protein within cells is comparable to or even exceeds that of the catalytic Vps34 or the regulatory Vps15 subunit, indicating that Atg38 is an invariably associated integral component of complex I rather than an auxiliary or substoichiometric factor[12][30].

## Atg38's Role in Phosphatidylinositol 3-Kinase Complex I Assembly and Stabilization

The fundamental biological role of Atg38 centers on its function as a physical linkage or "bridge" protein that maintains the integrity and assembly of the autophagy-specific PI3K complex I[12][30][42]. The PI3K complex I in both yeast and mammalian cells comprises four core subunits arranged in a characteristic Y-shaped architecture: the catalytic lipid kinase Vps34 (PIK3C3 in mammals), the regulatory pseudokinase Vps15 (PIK3R4 in mammals), the scaffolding protein Vps30/Atg6 (BECN1/Beclin 1 in mammals), and the autophagy-specific targeting subunit Atg14 (ATG14L in mammals)[2][10][12]. These four subunits form two functional arms: a catalytic arm composed of Vps15 and Vps34 that contains the kinase active site, and an adaptor arm consisting of Vps30 and Atg14 that mediates autophagy-specific functions and targeting[2][12].

In cells lacking functional Atg38, the autophagy-specific PI3K complex I undergoes dissociation into its component subcomplexes, specifically separating into the Vps15–Vps34 catalytic arm and the Vps30–Atg14 adaptor arm[12][30][42]. This dissociation is not merely a quantitative reduction in complex stability but represents a qualitative failure of complex assembly, suggesting that Atg38 provides essential structural determinants for maintaining complex quaternary structure. Biochemical analyses using gel filtration chromatography demonstrate that in wild-type cells, Vps34, Vps15, Vps30, Atg14, and Atg38 co-elute as a stable species with an apparent molecular weight of approximately 500 kilodaltons, consistent with a fully assembled complex I that includes the Atg38 subunit[12]. In contrast, *atg38*-deleted cells show reduced co-elution of these components and accumulation of the individual subcomplexes, confirming that Atg38 is required to maintain the overall complex structure.

The mechanism by which Atg38 stabilizes complex I has been elucidated through HDX-MS and crystallographic studies[17][27][38]. The N-terminal MIT domain of Atg38 binds primarily to the Vps30-Atg14 arm of complex I, specifically contacting the coiled-coil I regions of both Atg14 and Vps30[17]. This binding interaction appears to reinforce and potentially stabilize the existing coiled-coil interaction between Atg14 and Vps30 themselves. Notably, the second arm of the complex consisting of Vps15 and Vps34 does not appear to directly interact with Atg38 according to HDX-MS coverage; instead, the Vps34-Vps15 arm may be maintained in complex I through its established interactions with the Vps30-Atg14 arm, which is then stabilized by Atg38 binding[17]. This indirect stabilization mechanism represents an elegant solution for maintaining multi-arm assembly.

The C-terminal homodimerization domain of Atg38 also contributes to complex I stability through its role in organizing the overall architecture[27][30]. The Atg38 homodimer binds to a single complex I assembly with a stoichiometry of one homodimer (two Atg38 molecules) per complex I in yeast[27][38]. It is notable that mammalian NRBF2, the ortholog of yeast Atg38, exhibits somewhat different stoichiometry depending on the relative abundance of NRBF2 and complex I subunits; when complex I is more abundant than NRBF2, complex I molecules are homodimerized by a single NRBF2 homodimer in a 2:2 configuration, whereas when NRBF2 is more abundant, the stoichiometry shifts to 1:2 with one NRBF2 homodimer bridging a single complex I[38]. This stoichiometric flexibility in mammals may facilitate different modes of complex organization and regulation compared to the yeast system.

## Localization to the Pre-Autophagosomal Structure

A critical function of Atg38 is its role in directing the autophagy-specific PI3K complex I to the pre-autophagosomal structure (PAS), the perivacuolar site where autophagosome formation initiates[12][13][30][49]. The PAS represents the nucleation site for autophagosome biogenesis and serves as the organizational hub where multiple Atg proteins accumulate during starvation or nutrient deprivation[12][30]. Almost all characterized Atg proteins localize to the PAS, and this localization is a hallmark feature of autophagy activation, serving as both a functional necessity and a diagnostic marker for autophagy induction.

Atg38 localizes to the PAS in an Atg14-dependent manner[12][13][30], meaning that deletion of the *atg14* gene completely abolishes PAS accumulation of Atg38, demonstrating the critical importance of the Atg14-Atg38 interaction for proper subcellular targeting[12][30]. The PAS localization of Atg38 is also dependent on the Atg14-containing PI3K complex I itself; Atg38 does not localize to the PAS when other essential components of complex I are missing. Interestingly, under nutrient-rich conditions without autophagy induction, Atg38-GFP signals are detected on the vacuolar membrane in addition to the cytoplasm[42], suggesting that Atg38 has both PAS-associated and vacuolar membrane-associated pools. Upon autophagy induction by starvation, the PAS-associated pool becomes predominantly prominent as part of the organized Atg protein accumulation at this site[12].

The C-terminal coiled-coil domain of Atg38 plays a critical role in PAS localization and appears to mediate membrane association through contact with lipid bilayers[17][55]. When the C-terminal domain is deleted or disrupted, Atg38 fails to properly accumulate at autophagic puncta and remains predominantly in the soluble cytoplasmic fraction, as demonstrated by subcellular fractionation experiments[17]. Importantly, this defect in PAS localization of the C-terminal-deleted Atg38 cannot be overcome by robust overexpression, indicating that PAS targeting requires intrinsic structural information within the C-terminal region. The membrane-binding capacity of the C-terminal domain appears particularly important in yeast complex I, which lacks the mammalian BATS (Barkor/Atg14 autophagosome-targeting sequence) domain that is present in mammalian Atg14L and contributes to membrane curvature sensing in that system[54][55]. In yeast, Atg38's C-terminal domain may compensate by providing direct membrane-binding activity.

The targeting of Atg38 and complex I to the PAS is regulated by multiple upstream Atg proteins and signaling cascades[49]. Recent studies have revealed that complex I targeting involves cooperative interactions between Atg38 and multiple other factors: the Atg1 kinase complex (composed of Atg1, Atg13, and Atg101) serves as a recruitment scaffold at the PAS, Atg9 vesicles represent pre-autophagosomal intermediates that can interact with complex I, and the vacuolar membrane anchor protein Vac8 provides additional targeting determinants[49]. The Atg14–Vac8 interaction appears constitutive, while the Atg38–Atg1 complex interaction and the Vps30–Atg9 interaction are enhanced specifically upon macroautophagy induction in response to starvation and mTOR inhibition, demonstrating dynamic regulation of complex I targeting[49]. These cooperative interactions ensure that PI3K complex I recruitment to the PAS is tightly controlled and responsive to cellular nutrient status.

## The Atg38-Atg8 Interaction: A Unique Positive Feedback Loop in Fission Yeast

One of the most striking discoveries regarding Atg38 function emerged from detailed studies in *S. pombe*, which revealed that Atg38 contains a conserved Atg8-family-interacting motif (AIM) capable of directly engaging with the ubiquitin-like autophagy protein Atg8[1][31][45][57]. This finding was particularly notable because such an AIM-mediated interaction between Atg38 and Atg8 is highly conserved in Atg38 proteins from four fission yeast species (including *S. pombe*, *S. japonicus*, *S. cryophilus*, and *S. octosporus*) but is conspicuously absent from Atg38 orthologs in budding yeast *S. cerevisiae* and in mammalian NRBF2, indicating that this interaction represents a fission yeast-specific innovation[1][31].

The Atg8-family-interacting motif (AIM) in Atg38 spans 13 amino acids (residues 173–185 in *S. pombe* Atg38) and represents the most highly conserved region among Atg38 proteins from fission yeast species, demonstrating strong evolutionary selective pressure for maintenance of this sequence[1][31]. The AIM motif serves as a recognition element that binds to specific hydrophobic binding pockets on the surface of lipidated Atg8 (Atg8–PE), enabling recruitment of Atg38 to autophagosomal membranes where Atg8 resides following its conjugation to phosphatidylethanolamine[1][31]. Mutation of the AIM motif in Atg38 significantly reduces or abolishes the interaction with Atg8, providing direct evidence for the functional importance of this sequence. Importantly, the Atg8-binding activity of Atg38 is AIM-dependent and can be rescued or complemented by providing exogenous AIM sequences, demonstrating that the AIM motif itself is the core recognition determinant[1][31].

This Atg38-Atg8 interaction is functionally significant because it establishes a remarkable positive feedback loop between Atg8 and the PI3K complex I[1][31][45][57]. According to the classical model of autophagy, core Atg proteins are recruited to the PAS in a strict hierarchical manner, with upstream factors (like PI3K complex I) recruiting downstream factors (like Atg8) through sequential steps[1][31]. However, the Atg38-Atg8 interaction violates this unidirectional hierarchy by allowing the downstream component Atg8 to directly feedback and enhance recruitment of the upstream PI3K complex I through its interaction with Atg38[1][31][45]. This positive feedback loop functions as follows: initially, PI3K complex I (including Atg38) is recruited to the PAS through interactions with Atg1 complex scaffolds, Atg9 vesicles, and Vac8, allowing complex I to synthesize phosphatidylinositol 3-phosphate (PI3P)[1][49]. This PI3P recruits downstream Atg proteins including those required for Atg8 lipidation. Once Atg8 is lipidated and anchored to the autophagosomal membrane, the Atg38-Atg8 AIM-mediated interaction becomes operative, allowing Atg8–PE to recruit and stabilize additional Atg38 (and thus PI3K complex I) at the PAS, further amplifying PI3P generation and downstream cascade activation[1][31][45].

The functional consequences of disrupting the Atg38-Atg8 interaction are profound and demonstrate the biological importance of this positive feedback loop[1][31]. When the AIM motif of Atg38 is mutated, preventing Atg8 binding while preserving other Atg38 functions (as confirmed by demonstrating that mutant Atg38 protein levels are identical to wild-type), autophagy is substantially impaired[1][31]. Specifically, disruption of the Atg38-Atg8 interaction leads to reduced PAS accumulation of Atg38 itself, lower abundance of Atg14 at the PAS, and decreased localization of other downstream Atg proteins including Atg5, Atg16, and Atg18—all of which depend on Atg8 or Atg8-related factors for their recruitment[1][31]. The reduction in PAS accumulation of autophagy machinery components directly translates to functional defects in autophagosome formation: autophagosomes formed when the Atg38-Atg8 interaction is disrupted are markedly reduced in size compared to wild-type[1][31][39][45], and the autophagic flux (the rate of cargo turnover through autophagosomes) is correspondingly decreased[1][31].

To definitively demonstrate that the Atg38-Atg8 interaction specifically contributes to autophagy through its effect on PAS accumulation of Atg38 (and not through some indirect mechanism), researchers performed a remarkable rescue experiment[1][31]. They demonstrated that expressing an artificial Atg14-Atg8 AIM fusion protein could completely rescue the autophagy defect caused by loss of the native Atg38-Atg8 interaction[1][31]. This finding proves that the key functional requirement is establishing an interaction between some component of PI3K complex I (Atg38 or Atg14) and Atg8, demonstrating the flexibility and robustness of the positive feedback mechanism itself. The fact that Atg14 can functionally substitute for Atg38 when artificially engineered to interact with Atg8 demonstrates that the mechanistic requirement is for a physical link between PI3K complex I and Atg8, rather than any specific property unique to Atg38.

The positive feedback loop established by Atg38-Atg8 interaction serves to amplify and stabilize autophagosome formation, increasing the efficiency of the process[1][31][45]. By allowing downstream Atg8 to enhance recruitment of upstream PI3K complex I, the system creates a self-amplifying cascade that rapidly escalates autophagosome production once initial autophagy induction is triggered. This represents an elegant regulatory mechanism where the product of one step (Atg8–PE) actively enhances the catalytic step (PI3P synthesis by complex I) that produces the lipid required for Atg8 conjugation. Such positive feedback loops are common in biochemical regulation and often serve to accelerate responses and create sharp, switch-like activation kinetics. In the context of autophagy, this amplification mechanism ensures robust and efficient sequestration of cargo during nutrient starvation when rapid cellular adaptation is critical for survival.

## Phosphatidylinositol 3-Phosphate Generation and Downstream Autophagy Cascade

The ultimate enzymatic function of PI3K complex I, in which Atg38 participates as a structural subunit, is the generation of phosphatidylinositol 3-phosphate (PI3P) from phosphatidylinositol (PI) at the site of autophagosome formation[2][11][12][26]. The Vps34 catalytic subunit specifically phosphorylates the D-3 position (the 3-hydroxyl group) on the inositol ring of phosphatidylinositol, generating the signaling lipid PI3P with remarkable positional specificity[2][26]. This Vps34-catalyzed reaction represents the sole mechanism for generating PI3P from phosphatidylinositol in yeast cells; Vps34 is the only class III PI3-kinase present in yeast and is responsible for essentially all PI3P synthesis that supports both autophagy and vacuolar protein sorting[2][12][26][29].

The role of Atg38 in this enzymatic process is indirect but essential: by stabilizing complex I assembly and ensuring its proper localization to the PAS, Atg38 enables the Vps34 kinase to access its membrane substrate and function efficiently[12][30]. The PI3P generated by complex I at the PAS then serves as a spatial and temporal landmark that recruits multiple downstream autophagy factors[2][11][20][21]. Proteins containing specific PI3P-binding domains—including the PX domain, FYVE domain, and FRRG motif-containing domain—are recruited to sites of PI3P synthesis and accumulate at the PAS and expanding autophagosomal membrane[2][11]. Key downstream effectors include the Atg18-Atg2 complex, which localizes to PI3P through Atg18's binding to this lipid and plays crucial roles in tethering and lipid transfer between membranes during autophagosome expansion[2][21].

The accumulation of PI3P on the autophagosomal membrane enables a cascade of events essential for autophagosome biogenesis: the Atg16 complex (composed of Atg16, the ubiquitin-like conjugate Atg12-Atg5, and Atg21) is recruited through Atg21's recognition of PI3P, positioning the complex for its function as an E3-like ligase in the conjugation of the ubiquitin-like protein Atg8 to phosphatidylethanolamine[52]. This Atg8-PE conjugation is itself critical for further autophagosome membrane expansion, cargo selection, and eventual fusion with lysosomes[15][18][34]. The multivalent nature of PI3P recognition—through multiple distinct protein domains binding to the same lipid—enables coordinated recruitment of multiple protein complexes to ensure proper spatiotemporal organization of autophagosome biogenesis.

By disrupting Atg38 function and thus preventing proper complex I assembly and targeting, cellular PI3P synthesis at the PAS is significantly impaired[12][30]. This reduction in PI3P directly translates to defective recruitment of downstream Atg proteins and dramatically reduced autophagy efficiency. The severity of the autophagy defect in *atg38* mutants—approaching the severity of defects in genes encoding the core catalytic subunits Vps34 itself or the essential adaptor Atg14—underscores that Atg38 is not merely an auxiliary factor but rather a core structural component whose function is critical for the autophagy process.

## Functional Analysis and Autophagy Assays

Multiple complementary experimental approaches have been employed to characterize the functional role of Atg38 in autophagy[1][12][13][31]. The most direct evidence for Atg38's role in autophagy comes from measurement of autophagic flux using the well-established Pho8Δ60 assay, which has been adapted for use in fission yeast[1][31]. In this assay, a truncated, catalytically inactive alkaline phosphatase (Pho8Δ60) is expressed in cells and serves as a cargo for autophagy; this protein cannot be activated in the cytoplasm but becomes activated only after it is transported into the vacuole by autophagy. The alkaline phosphatase activity detected in vacuolar lysates thus serves as a quantitative measure of autophagosome-mediated delivery of cargo to the vacuole[1][31]. In wild-type *S. pombe* cells, Pho8Δ60 activity increases substantially in response to nitrogen starvation (a potent autophagy inducer), whereas in *atg38* deletion mutants, this starvation-induced increase in Pho8Δ60 activity is completely absent, demonstrating that Atg38 is absolutely required for autophagy under starvation stress[1][31].

Similarly, direct measurement of autophagy in *atg38* mutants using the CFP-Atg8 processing assay confirms these findings[1][31]. In this assay, Atg8 fused to cyan fluorescent protein (CFP) is expressed in cells, and when Atg8-CFP enters the vacuole via autophagy, the protease-resistant portion of CFP is generated through vacuolar degradation; accumulation of this free CFP fragment quantitatively reflects the autophagic flux[1][31]. Nitrogen starvation robustly induces accumulation of free CFP in wild-type cells but not in *atg38Δ* mutants, confirming that Atg38 is essential for starvation-induced autophagy[1][31]. When the Atg38 AIM motif is mutated to prevent Atg8 binding, the defect in autophagy is comparable to complete deletion of *atg38*, and this can be fully rescued by expressing an exogenous AIM sequence, demonstrating the specific importance of the Atg8-binding function of Atg38[1][31].

Complementary genetic analyses using the Tdh1-YFP processing assay provide additional quantitative evidence[1][31]. Tdh1, a glyceraldehyde-3-phosphate dehydrogenase fused to yellow fluorescent protein, is another autophagy cargo whose vacuolar transport can be quantitatively measured. Wild-type cells show robust nitrogen starvation-induced Tdh1-YFP processing, while *atg38* mutants show severely reduced or absent processing, confirming the consistent role of Atg38 across multiple autophagy assays[1][31].

Beyond flux measurements, microscopic analysis of autophagosome accumulation provides visual confirmation of Atg38's role[1][31][39][45]. When autophagosome formation is blocked at the final step of autophagosome-lysosome fusion (for example, by deletion of the *fsc1* gene encoding a factor involved in fusion), autophagosomes accumulate to high levels in wild-type cells but not in *fsc1Δ atg38Δ* double mutants, confirming that Atg38 is required for autophagosome formation itself[1][31]. Moreover, electron microscopy reveals that autophagosomes formed in the presence of disrupted Atg38-Atg8 interaction are markedly smaller than those in wild-type cells[1][31], correlating with the reduced amounts of Atg8 and other autophagy machinery components at the PAS.

## Hierarchy of PAS Organization and Atg38's Position

Understanding where Atg38 and PI3K complex I fit within the hierarchical assembly of autophagy-related proteins at the PAS has been a major goal of autophagy research[35][49][52]. A landmark study using systematic analysis of PAS organization in yeast established that Atg proteins are recruited to the PAS in a hierarchical manner, with certain upstream factors being absolutely required for recruitment of downstream factors[35]. This hierarchy begins with the autophagy-specific proteins Atg17, Atg29, and Atg31, which form a ternary scaffold complex that serves as the foundational platform for PAS organization[35]. The Atg1 kinase complex, containing Atg1, Atg13, and Atg101, localizes to the PAS dependent on this Atg17-Atg29-Atg31 platform and is positioned downstream in the hierarchy[35].

PI3K complex I, including Atg38, is positioned downstream of Atg1 and requires Atg9 vesicles for its recruitment to the PAS[35][49]. The downstream positioning of complex I in the classical hierarchy reflects its role in generating the PI3P that recruits numerous downstream effector proteins. However, the discovery of the Atg38-Atg8 positive feedback loop reveals that this hierarchy is more nuanced than a simple linear progression, with Atg8 (positioned far downstream in the classical hierarchy) able to feedback and enhance recruitment of upstream complex I components[1][31][45]. This finding has led to a revised understanding of PAS organization as involving both feed-forward and feedback regulatory loops that ensure efficient and amplified autophagosome formation once the process is initiated.

## Conservation and Evolution: Orthologs in Other Organisms

Atg38 proteins are conserved across diverse eukaryotic organisms, though with important functional variations in different lineages[1][17][27][30][37][38]. In budding yeast *Saccharomyces cerevisiae*, the orthologous protein is also referred to as Atg38 (encoded by YLR211c) and performs analogous structural functions in stabilizing PI3K complex I, providing a physical link between the Vps15-Vps34 and Atg14-Vps30 subcomplexes[12][30][38]. However, budding yeast Atg38 lacks the fission yeast-specific Atg8-family-interacting motif, indicating that the positive feedback loop function is a specialized addition in fission yeast lineages[1][31].

The mammalian ortholog of yeast Atg38 is designated NRBF2 (nuclear receptor binding factor 2), also known as COPR2 (corepressor of peroxisome proliferator-activated receptor gamma 2)[37][38][40][41][55]. Mammalian NRBF2, like yeast Atg38, comprises an N-terminal MIT domain, an intrinsically disordered region, and a C-terminal coiled-coil homodimerization domain, indicating conservation of overall structural organization[37][38][55]. NRBF2 performs the analogous function of stabilizing the mammalian autophagy-specific PI3K complex I, which consists of PIK3C3/VPS34, PIK3R4/VPS15, BECN1/Beclin 1, and ATG14L (the mammalian ortholog of Atg14)[37][38][41][51]. Importantly, mammalian ATG14L contains the BATS domain (Barkor/Atg14 autophagosome-targeting sequence), a membrane-binding domain absent from yeast Atg14, which may reduce the functional importance of NRBF2's C-terminal membrane-binding capacity in mammals compared to yeast[54][55].

The stoichiometry of NRBF2 binding to mammalian complex I differs from yeast Atg38 in that NRBF2 can potentially bridge two complex I assemblies under certain conditions, rather than binding only to a single complex I as in yeast[27][38][37]. This difference in stoichiometry may reflect functional requirements specific to mammalian cells and could have implications for higher-order organization of PI3K complex I in mammalian autophagy. Studies in mammalian cells have demonstrated that NRBF2 knockout mice show reduced autophagy, reduced PI3K complex I stability and activity, and impaired recovery from metabolic stress, confirming the essential role of NRBF2 in mammalian autophagy[37][40][41].

The Atg8-family-interacting motif that characterizes *S. pombe* Atg38 is notable by its absence from all currently characterized mammalian NRBF2 sequences and from budding yeast Atg38, suggesting that this fission yeast-specific adaptation represents a lineage-specific innovation in autophagy regulation[1][31]. This variation highlights how core autophagy machinery, while fundamentally conserved, has accumulated lineage-specific regulatory modifications that fine-tune autophagy responses to meet the particular metabolic and developmental requirements of different organisms.

## Regulation Through Post-Translational Modifications

Like many components of the autophagy machinery, Atg38 undergoes post-translational modifications that modulate its function and may represent important regulatory mechanisms[50]. Phosphorylation by the autophagy-initiating kinases Atg1 and ULK1 (the mammalian ortholog of Atg1) has been identified on multiple serine residues within Atg38[50]. Specifically, residues S96, S103, S109, and S133 on yeast Atg38 are phosphorylated by the Atg1 kinase, and mammalian NRBF2 is similarly phosphorylated by ULK1, although the precise functional consequences of these phosphorylation events have not been fully characterized[50]. These phosphorylation sites are positioned within or near the intrinsically disordered region that separates the MIT and coiled-coil domains, suggesting that phosphorylation in this region might modulate interactions with binding partners or alter protein conformation.

The biological logic of Atg1/ULK1-mediated phosphorylation of Atg38/NRBF2 likely involves coordinate signaling across multiple complex I subunits to enhance complex I activity and autophagosome formation upon starvation-induced autophagy activation[50]. During starvation, TORC1 kinase is inactivated, allowing Atg1/ULK1 to become activated and phosphorylate multiple autophagy substrates, including Atg13, FIP200 (in mammals), and subunits of PI3K complex I[50]. The phosphorylation of Atg38/NRBF2 by Atg1/ULK1 may enhance complex I localization to the PAS, stabilize interactions with other autophagy machinery components, or modify complex I enzymatic activity, though definitive functional studies on these phosphorylation sites remain to be conducted.

Interestingly, the role of phosphorylation in regulating Atg38/NRBF2 contrasts with the regulation of other complex I subunits: the complex I-specific subunits (Atg14, NRBF2, and UVRAG in mammalian complex II) are subject to regulation by both Atg1/ULK1 and mammalian mTOR kinase, while the core subunits Vps34 and Vps15 show more limited phosphorylation-based regulation[50]. This pattern suggests that specialized subunits like Atg38/NRBF2 serve as principal regulatory targets for fine-tuning complex I function, while the core catalytic machinery is regulated less extensively through phosphorylation.

## Biological Significance: Autophagy and Cellular Adaptation to Nitrogen Starvation

The primary biological context for Atg38 function is the cellular response to nutrient deprivation, particularly nitrogen starvation[1][12][44][47]. In *S. pombe*, as in other unicellular eukaryotes, nitrogen availability is a critical nutritional parameter that triggers profound changes in cellular fate and gene expression. When haploid cells of opposite mating types experience nitrogen starvation, they undergo sexual differentiation, a developmental process involving mating, meiosis, and sporulation that enables survival and transmission during unfavorable conditions[44][47][19]. Autophagy plays a critical role in this starvation-induced adaptation by providing a source of recycled nitrogen and carbon from existing cellular proteins and organelles[44][47].

Studies using autophagy-defective *atg38* mutants demonstrate that autophagy, and specifically the Atg38-mediated pathway of PI3K complex I assembly, is essential for survival during nitrogen starvation[1][12][44][47]. *atg38* mutants show severely compromised viability during prolonged nitrogen starvation compared to wild-type cells[1][12]. More strikingly, autophagy-defective mutants are sterile in the absence of exogenous nitrogen, meaning they cannot complete sexual differentiation, but restore fertility when nitrogen is supplied, indicating that the primary role of autophagy is to provide a nitrogen source[44][47]. This direct evidence demonstrates that autophagy-dependent protein degradation and nitrogen recycling by the Atg38-containing autophagy machinery is essential for maintaining the amino acid pools and nucleotide precursors required for the transcriptional and translational changes necessary for sexual differentiation.

The connection between autophagy and sexual differentiation in fission yeast illuminates a broader principle: developmental transitions often require rapid reorganization of cellular components and dramatic changes in gene expression, processes that demand substantial metabolic resources[44][47]. By enabling efficient autophagy through Atg38-mediated PI3K complex I assembly, cells can generate the biosynthetic precursors necessary to fuel the developmental process. The positive feedback loop established by the Atg38-Atg8 interaction appears designed to maximize autophagy efficiency precisely when such nutrient-generating capacity is most critically needed.

Beyond sexual differentiation, Atg38 function is important for basal autophagy under normal vegetative growth conditions and for autophagy induced by other starvation conditions such as carbon deprivation[12][13]. The substantial abundance of Atg38 protein—comparable to core catalytic and regulatory subunits—indicates that this protein is constitutively expressed and poised for rapid autophagy activation upon nutrient stress. This stands in contrast to some autophagy factors that are upregulated only upon starvation induction, suggesting that Atg38 levels are not a limiting factor for autophagy initiation.

## Structural Insights from Crystallography and Cryo-Electron Microscopy

High-resolution structural information on Atg38 has been obtained through X-ray crystallography of isolated domains and domains of the PI3K complex I containing Atg38[27][38][9]. The crystal structure of the C-terminal homodimerization domain of Atg38, determined at 2.2 Angstrom resolution, reveals the distinctive mushroom-like architecture described earlier[27][38][9]. This structure shows that the two Atg38 molecules in the homodimer are related by approximate C2 symmetry but actually form an asymmetric interface, with different interaction patterns on each side of the dimer[27][38]. The four-helix cap region forms a tight bundle stabilized by extensive hydrophobic interactions, while the parallel coiled-coil stalk region maintains the two Atg38 molecules in close apposition[27][38].

The asymmetry of the Atg38 homodimer structure is functionally significant because it suggests that the two Atg38 molecules may occupy non-equivalent positions within the complex I assembly, potentially interacting with different components or performing specialized functions[27][38]. One Atg38 molecule might preferentially contact the Vps30-Atg14 arm, while the other Atg38 in the homodimer assumes a different orientation or makes distinct contacts within the overall complex I architecture. This asymmetry contrasts with many other homodimeric proteins and likely reflects the specific functional requirements of Atg38 for stabilizing the complex I assembly.

Hydrogen-deuterium exchange mass spectrometry (HDX-MS) studies have provided complementary structural insights into how Atg38 interacts with the PI3K complex I in solution[17][27][38]. These experiments map the regions of Atg38 and complex I subunits that undergo changes in deuterium exchange upon Atg38 binding, thereby identifying interaction interfaces. HDX-MS reveals that the Atg38 MIT domain undergoes dramatic protection from deuterium exchange when complex I is present, confirming that this domain is deeply embedded in the complex and makes extensive molecular contacts[17]. The coiled-coil I regions of both Atg14 and Vps30 show protection from exchange in the presence of Atg38, indicating that these regions are involved in the binding interface[17]. The Atg38 C-terminal domain also shows changes in deuterium exchange patterns when bound to complex I, suggesting conformational changes or shielding from solvent upon complex formation[17].

Notably, the second arm of complex I (the Vps15-Vps34 catalytic arm) does not appear to undergo significant HDX changes upon Atg38 addition in most experiments, though technical limitations (incomplete sequence coverage) preclude definitive exclusion of direct Atg38-Vps15 or Atg38-Vps34 interactions[17]. The most parsimonious interpretation of the HDX data is that Atg38's MIT domain binds primarily to the Vps30-Atg14 arm, stabilizing this arm's structure and ensuring its proper orientation to interact with the Vps15-Vps34 arm through pre-existing Vps30-Vps34 and Atg14-Vps15 interactions[17].

The overall architecture of PI3K complex I including Atg38 has been visualized using electron microscopy at modest resolution (approximately 25 Angstrom), revealing the Y-shaped overall structure with Atg38 positioning toward the base of the complex near where the two arms converge[27][38]. This positioning is entirely consistent with Atg38's proposed role as a structural linker stabilizing interactions between the two functional arms of complex I.

## Comparison of Atg38 Function in S. pombe with Budding Yeast Orthologs

While both fission yeast *S. pombe* and budding yeast *S. cerevisiae* possess ATG38 genes encoding structurally similar proteins, functional differences have emerged between the two organisms[1][30][31][38][42]. The most striking difference is the presence of the Atg8-family-interacting motif in fission yeast Atg38 but not in budding yeast Atg38[1][31]. This difference suggests that the positive feedback loop between Atg38 and Atg8, which is functionally important in fission yeast, does not exist in budding yeast cells. This may reflect differences in the complexity or efficiency of autophagy machinery evolution between the two yeast species, or alternatively, budding yeast may employ alternative feedback regulatory mechanisms not yet identified.

Another potential difference relates to the relative roles of the Atg38 C-terminal domain in membrane association and targeting to the PAS[55]. In budding yeast, the orthologous Atg14 contains a C-terminal coiled-coil domain but not the mammalian-like BATS domain, making Atg38's C-terminal membrane-binding capacity potentially more critical for PAS targeting. In fission yeast, the situation may be similar, with Atg38's C-terminal domain bearing primary responsibility for membrane targeting. However, in mammalian systems where ATG14L contains the BATS domain, the functional importance of the NRBF2 C-terminal membrane-binding domain might be reduced, though not necessarily eliminated[54][55].

Despite these differences, the fundamental role of Atg38/NRBF2 as a structural stabilizer of PI3K complex I is conserved across all organisms studied, confirming that this represents an ancient and conserved function acquired early in eukaryotic evolution[12][30][38]. The lineage-specific modifications (such as the fission yeast AIM motif) represent relatively recent evolutionary additions that fine-tune complex I function for organism-specific requirements.

## Atg38's Role in Autophagy-Related Pathways Beyond Macroautophagy

While the primary and best-characterized function of Atg38 relates to macroautophagy (autophagy proper), the protein may also participate in related autophagy-like processes[1][44]. The Cvt pathway (cytoplasm-to-vacuole targeting), which operates in some unicellular eukaryotes including budding yeast, is a selective autophagy-like pathway that delivers hydrolytic enzymes to the vacuole in a cargo-protein-dependent manner[12][42]. This pathway shares many molecular components with macroautophagy, including most of the core Atg proteins, and requires PI3K complex I function[12][42]. When genetic interaction studies between *atg38* and *atg14* were performed, defects were observed in both macroautophagy and Cvt pathway function[42], suggesting that Atg38 contributes to both processes through its structural role in stabilizing PI3K complex I. However, fission yeast *S. pombe* lacks prominent Cvt pathway activity under typical laboratory conditions, so the primary autophagy-related process in which Atg38 functions is macroautophagy.

It is worth noting that recent studies have revealed non-autophagy roles for Atg proteins and autophagy machinery components in diverse cellular processes including immune signaling, secretion, and control of cell fate[15][40]. While specific non-autophagy functions of Atg38 have not yet been definitively demonstrated, the conservation of Atg38/NRBF2 across diverse eukaryotes and the observation that mammalian NRBF2 is important for cellular metabolic adaptation suggest that this protein may participate in broader cellular functions beyond classical macroautophagy. However, current evidence indicates that the primary biological role remains within the autophagy machinery.

## Experimental Approaches and Future Directions

The characterization of Atg38 has employed diverse experimental methodologies that have collectively provided a detailed understanding of this protein's structure and function[1][12][13][17][27][30][38]. Forward genetic screening, reverse genetics (gene deletion and mutation), biochemical co-immunoprecipitation and gel filtration chromatography, fluorescence microscopy, electron microscopy, crystallography, and mass spectrometry-based proteomics have all contributed to the current model of Atg38 function. The multi-pronged experimental approach has been essential because different techniques reveal complementary information: genetics establishes biological importance, biochemistry reveals direct molecular interactions, structural biology explains mechanistic details, and microscopy confirms subcellular localization and dynamics.

Future research directions that would further advance understanding of Atg38 include structural determination of full-length Atg38 in complex with other autophagy machinery components using cryo-electron microscopy; elucidation of the precise molecular mechanism by which the Atg38 homodimer bridges the two arms of complex I; investigation of potential non-autophagy functions of Atg38/NRBF2 in mammalian cells; characterization of the functional consequences of the various phosphorylation sites on Atg38; determination of whether additional post-translational modifications (ubiquitination, sumoylation, etc.) regulate Atg38; and structural and functional studies comparing the Atg8-binding interface of fission yeast Atg38 with other AIM-containing proteins to understand the diversity of AIM recognition mechanisms. Additionally, investigating how the positive feedback loop between Atg38-Atg8 in fission yeast compares to alternative feedback mechanisms in other organisms might reveal principles of autophagy regulation conserved across eukaryotes.

## Concluding Perspectives on Atg38 and the Evolution of Autophagy

Atg38 represents a particularly illustrative example of how fundamental cellular processes like autophagy evolve and diversify across eukaryotic lineages. The core structural role of Atg38/NRBF2 in stabilizing PI3K complex I appears to have been established early in eukaryotic evolution and has been conserved across yeast and mammals, indicating the fundamental importance of this function[12][30][38]. However, the acquisition of the Atg8-family-interacting motif in fission yeast Atg38 demonstrates that even highly conserved processes continue to accumulate regulatory innovations that fine-tune their operation. The positive feedback loop established by Atg38-Atg8 interaction likely confers enhanced efficiency or regulatory precision to fission yeast autophagy, potentially reflecting specific metabolic or developmental requirements of this organism.

The existence of distinct regulatory mechanisms in different organisms (the Atg38-Atg8 feedback loop in fission yeast versus alternative regulatory strategies in budding yeast or mammals) indicates that autophagy, while fundamental to eukaryotic cell biology, has been remodeled substantially across different lineages to meet lineage-specific needs[1][31][38]. This principle—conservation of core function combined with lineage-specific regulatory innovation—likely applies broadly to other cellular processes and provides insight into how evolution generates diversity while maintaining functional conservation.

From a cellular perspective, Atg38's role in establishing and maintaining efficient autophagy is critical for cellular survival during nutrient starvation, a condition likely experienced by unicellular organisms like fission yeast during natural growth and development. The multi-layered regulation of Atg38 through its position in the autophagy protein hierarchy, its participation in positive feedback loops with downstream autophagy factors, and its regulation through post-translational modifications all serve to ensure that autophagosome biogenesis is tightly controlled and maximally efficient when nutrient limitation threatens cell viability. Understanding Atg38 at molecular, cellular, and organismal levels thus provides insights into fundamental mechanisms of cellular adaptation and survival.

## Acknowledgments of Knowledge Gaps

Despite substantial progress in characterizing Atg38, important questions remain incompletely answered. The precise stoichiometry and three-dimensional organization of Atg38 within higher-order complexes remain incompletely defined, particularly regarding how multiple Atg38 molecules might cooperate to bridge multiple complex I assemblies or organize larger autophagic structures. The functional significance of the various phosphorylation sites identified on Atg38 has not been rigorously tested through mutation and functional analysis. The structural basis for membrane binding by the Atg38 C-terminal domain and how this contributes to PAS targeting remains incompletely characterized. The evolutionary origins and functional significance of the Atg8-family-interacting motif in fission yeast Atg38 remain unclear, as does the question of whether alternative feedback regulatory mechanisms exist in organisms lacking this motif. Finally, whether Atg38 participates in cellular processes beyond autophagy remains to be definitively established. These gaps represent opportunities for future research that will deepen understanding of autophagy regulation and cellular adaptation mechanisms.

---

# References Cited

[1] Atg38-Atg8 interaction in fission yeast establishes a positive feedback loop between Atg8 and the PtdIns3K complex I to promote efficient autophagosome formation
[2] PtdIns 3-Kinase orchestrates autophagosome formation in yeast 
[4] UniProt database: atg38 PtdIns3K complex I subunit atg38
[9] PDB-5kc1: Structure of the C-terminal dimerization domain of Atg38
[10] Beclin 1 forms two distinct phosphatidylinositol 3-kinase complexes
[12] Atg38 is required for autophagy-specific phosphatidylinositol 3-kinase complex I formation
[13] Atg38 localization and complex I assembly mechanisms
[15] Mechanisms and roles of membrane-anchored ATG8s
[17] Characterization of Atg38 and NRBF2, a fifth subunit of the autophagic Vps34/PIK3C3 complex
[18] Delineating the lipidated Atg8 structure
[19] Regulation of sexual differentiation initiation in *S. pombe*
[21] The Atg2-Atg18 complex tethers pre-autophagosomal membranes
[26] Activation mechanisms of the VPS34 complexes
[27] Structure of the C-terminal dimerization domain of Atg38 (5KC1)
[30] Atg38 provides a physical linkage between the Vps15–Vps34 and Atg14–Vps30 subcomplexes
[31] Atg38-Atg8 interaction in fission yeast establishes a positive feedback loop
[34] Blocking autophagosome closure manifests the roles of mammalian Atg8-family proteins
[35] Organization of the Pre-autophagosomal structure
[37] Dynamics and architecture of the NRBF2-containing PI3KC3-C1 complex
[38] Characterization of Atg38 and NRBF2, a fifth subunit of the autophagic Vps34/PIK3C3 complex
[39] Atg38-Atg8 interaction in fission yeast establishes a positive feedback loop
[40] Autophagy and autophagy-related proteins in CNS autoimmunity
[41] Mitochondrial Complex I activity is required for maximal autophagy
[42] Atg38 is required for autophagy-specific phosphatidylinositol 3-kinase complex I formation
[44] Fission yeast autophagy induced by nitrogen starvation generates a nitrogen source
[45] Atg38-Atg8 interaction in fission yeast establishes a positive feedback loop
[47] Fission yeast autophagy induced by nitrogen starvation
[49] The Atg1 complex, Atg9, and Vac8 recruit PI3K complex I to the pre-autophagosomal structure
[50] Activation mechanisms of the VPS34 complexes
[52] Two distinct mechanisms target the autophagy-related E3 complex Atg12-Atg5-Atg16
[54] Atg14: A Key Player in Orchestrating Autophagy
[55] Class III phosphatidylinositol 3-kinase complex I subunit NRBF2/Atg38

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC7595586/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC3067060/
3. https://research.bioinformatics.udel.edu/iptmnet/entry/O94427/
4. https://www.uniprot.org/uniprotkb/O94427/entry
5. https://journals.biologists.com/jcs/article/134/19/jcs258774/272452/Visual-detection-of-binary-ternary-and-quaternary
6. https://www.pombase.org/reference/PMID:27737912
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC7721316/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC5955796/
9. https://pdbj.org/emnavi/quick.php?id=pdb-5kc1
10. https://www.molbiolcell.org/doi/10.1091/mbc.e08-01-0080
11. https://febs.onlinelibrary.wiley.com/doi/10.1016/j.febslet.2010.01.011
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC3812978/
13. https://www.biomolther.org/journal/view.html?doi=10.4062%2Fbiomolther.2024.094
14. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1532050/full
15. https://www.yeastgenome.org/locus/S000004201
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC5103362/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC8525951/
18. https://pubmed.ncbi.nlm.nih.gov/38449372/
19. https://www.babraham.ac.uk/sites/default/files/media/files/20074568.pdf
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC6187169/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC413184/
22. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.13987
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC8846182/
24. https://pubmed.ncbi.nlm.nih.gov/31941401/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC8624279/
26. https://www.rcsb.org/structure/5KC1
27. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.783881/full
28. https://www.molbiolcell.org/doi/10.1091/mbc.E20-03-0191
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC3195510/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC3351336/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC12013414/
32. https://www.molbiolcell.org/doi/10.1091/mbc.e07-10-1048
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC2854269/
34. https://www.pnas.org/doi/10.1073/pnas.1603650113
35. https://pubmed.ncbi.nlm.nih.gov/27630019/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC5326760/
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC6298213/
38. https://rupress.org/jcb/article/203/2/299/37553/Atg38-is-required-for-autophagy-specific
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC2883940/
40. https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2443.2007.01041.x
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC5788524/
42. https://pubmed.ncbi.nlm.nih.gov/17295836/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC10337603/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC10549190/
45. https://elifesciences.org/articles/43088
46. https://www.yeastgenome.org/locus/S000004230
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC8726667/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC4593082/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC12758336/
50. https://www.pnas.org/doi/10.1073/pnas.1910960116
51. https://discovery.researcher.life/article/atg38-atg8-interaction-in-fission-yeast-establishes-a-positive-feedback-loop-to-promote-autophagy/205263a24f463d669072de89af363112
52. HDX-MS coverage; instead
53. the classical model of autophagy