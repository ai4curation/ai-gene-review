---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-30T19:39:30.435403'
end_time: '2026-01-30T19:41:36.618102'
duration_seconds: 126.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: atg16
  gene_symbol: atg16
  uniprot_accession: O94656
  protein_description: 'RecName: Full=Autophagy protein 16;'
  gene_info: Name=atg16; ORFNames=SPBC405.05;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the ATG16 family. .
  protein_domains: Not specified in UniProt
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 52
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O94656
- **Protein Description:** RecName: Full=Autophagy protein 16;
- **Gene Information:** Name=atg16; ORFNames=SPBC405.05;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the ATG16 family. .
- **Key Domains:** Not specified in UniProt

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atg16" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atg16' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atg16** (gene ID: atg16, UniProt: O94656) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Comprehensive Functional Analysis of the Autophagy-Related Protein 16 (ATG16) from Schizosaccharomyces pombe

The autophagy-related protein 16 (ATG16), encoded by the *atg16* gene in *Schizosaccharomyces pombe* (fission yeast, UniProt accession O94656), serves as a critical structural and catalytic scaffold protein in the autophagy pathway. This protein forms an essential complex with ATG12 and ATG5 that functions as an E3-like ubiquitin ligase to facilitate the conjugation of the ubiquitin-like protein ATG8 to phosphatidylethanolamine during autophagosome biogenesis. Beyond its canonical role in autophagy, ATG16 participates in membrane tethering, proteasome-autophagy crosstalk, and non-canonical autophagy pathways. The protein's localization to the pre-autophagosomal structure (PAS) and its dynamic interactions with various regulatory proteins enable precise spatiotemporal control of autophagosome formation. This report synthesizes current knowledge of ATG16 function, structure, and mechanisms of action, with emphasis on experimental evidence and evolutionary conservation.

## Protein Identity and Gene Characterization

The *atg16* gene in *Schizosaccharomyces pombe* encodes autophagy protein 16, a conserved component of the autophagy machinery[1][4]. The gene is identified with the systematic designation SPBC405.05 and produces a protein with UniProt accession O94656[1][4]. The fission yeast ATG16 represents an evolutionarily distant homolog of well-characterized mammalian ATG16L1 and budding yeast (*Saccharomyces cerevisiae*) Atg16, with the yeast proteins sharing fundamental structural organization and functional properties that have been conserved across eukaryotes[19][38]. Notably, *S. pombe* is estimated to have diverged from *S. cerevisiae* more than 500 million years ago, yet autophagy factors have remained substantially conserved, underscoring the ancient and essential nature of this cellular pathway[19].

The *atg16* gene was originally identified through genome-wide screens designed to uncover autophagy-related genes in fission yeast[19]. Prior to systematic characterization, three core autophagy components—Atg10, Atg14, and Atg16—had not been identified in *S. pombe*, despite being well-characterized in budding yeast[19]. The discovery of these genes completed the roster of expected core autophagy machinery components in fission yeast and permitted comprehensive characterization of the autophagy system across a diverse yeast species[19]. The identification of Atg16 in fission yeast was particularly significant because it demonstrated that this protein family represents a genuinely conserved component of autophagosome biogenesis machinery across evolutionarily distant organisms.

## Structural Organization and Domain Architecture

The ATG16 protein exhibits a modular domain architecture that has been preserved throughout eukaryotic evolution[10][21][35]. The fission yeast Atg16 protein, like its mammalian counterpart ATG16L1, contains an N-terminal domain responsible for binding to the ATG12–ATG5 conjugate, followed by a coiled-coil domain essential for protein oligomerization[35]. In mammals, ATG16L1 additionally contains a C-terminal WD40 domain composed of seven repeats of the WD40 motif, though this domain is absent in yeast Atg16 proteins[24][35][43]. The core Atg5-binding motif, termed the AFIM (Atg5-interacting motif), adopts an alpha-helical conformation that mediates specific recognition by the ATG5 protein[24]. Crystal structural analysis of yeast Atg5 complexed with the N-terminal region of Atg16 revealed that the N-terminal region of Atg16 exhibits a helical structure and binds within a groove formed by the ubiquitin-like domains and helix-rich regions of Atg5[10][24].

The coiled-coil domain of Atg16 functions in mediating protein-protein interactions essential for complex assembly. This domain exhibits coiled-coil propensity and contains conserved leucine residues that mediate homodimerization through a leucine zipper-like mechanism[16][32]. The coiled-coil architecture is crucial because ATG16 must form higher-order oligomeric complexes with the ATG12–ATG5 conjugate to execute its full biological function[21]. In yeast, the Atg16 protein forms a homodimer that further associates with a single Atg12–Atg5 conjugate to generate an asymmetric heteromeric complex[10]. The functional significance of Atg16 homodimerization has been demonstrated through mutagenic disruption of the leucine zipper, which prevents dimer formation and causes complete loss of autophagy function despite normal expression and localization of the protein[16][32].

The membrane-binding capability of Atg16 derives from an amphipathic alpha helix located in the central region of the protein (approximately amino acid residues 113–131 in yeast, based on structural analysis of related proteins)[16][32]. This amphipathic helix exhibits a strong hydrophobic face that inserts into lipid bilayers, thereby anchoring the protein to membrane structures[16][32]. The distinct structural regions of Atg16—the Atg5-binding domain at the N-terminus, the leucine zipper dimerization domain, and the amphipathic membrane-binding helix—represent functionally independent modules that can be separated experimentally to define specific roles[16][32]. In fission yeast, these structural features are preserved, suggesting that the *S. pombe* Atg16 protein maintains the essential functional architecture required for autophagosome biogenesis across eukaryotic cells.

## The ATG12–ATG5–ATG16 Complex: Assembly and Stoichiometry

The ATG12–ATG5–ATG16 complex represents one of the most critical assemblies in the autophagy pathway, functioning as a specialized E3-like ubiquitin ligase[2][8][9][27]. This complex is assembled through sequential conjugation reactions beginning with the covalent attachment of ATG12 to ATG5, catalyzed by the E1-like enzyme ATG7 and the E2-like enzyme ATG10[9][27][39]. The resulting ATG12–ATG5 conjugate then associates non-covalently with ATG16, which is recruited to this complex through its N-terminal AFIM domain[4][10][25]. The assembly process has been characterized in detail through biochemical reconstitution studies and structural analysis, revealing that all three components are required to generate a functional E3 ligase capable of promoting ATG8 lipidation[8][9].

The stoichiometry of the ATG12–ATG5–ATG16 complex has been determined through multiple experimental approaches including gel filtration chromatography, cross-linking mass spectrometry, and crystallographic analysis[10][24][25]. In mammalian cells, the complex forms a large oligomeric assembly with an apparent molecular mass of approximately 800 kilodaltons[24][43][55]. This size is consistent with a complex composed of multiple copies of the ATG12–ATG5 conjugate associated with a homodimeric or higher oligomeric form of ATG16L1[24][43][55]. In yeast, Atg16 forms a homodimer that associates with the Atg12–Atg5 conjugate to generate approximately a 350 kilodalton complex[4][21]. The difference in stoichiometry between mammalian and yeast systems reflects variations in ATG16 oligomerization capacity, as mammalian ATG16L1 can form higher-order multimers more readily than yeast Atg16[24].

The assembly of this complex is essential for autophagy function, as demonstrated by the observation that mutations disrupting any interface within the complex—whether between ATG12 and ATG5, between ATG5 and ATG16, or within the Atg16 homodimer—completely abolish autophagy[16][32][34][43]. Furthermore, the spatial organization of the complex is important; the three-dimensional arrangement of the ATG12–ATG5–ATG16 assembly determines its ability to position substrates correctly for the lipidation reaction[25][29]. The coiled-coil domain and homodimeric organization of ATG16 appear to provide multiple membrane-binding surfaces, potentially allowing one ATG16 dimer to engage multiple membrane locations and thereby facilitate membrane tethering and vesicle clustering[31][32].

## Recruitment to the Pre-Autophagosomal Structure: Dual Pathways

ATG16 must be recruited to the site of autophagosome biogenesis—the pre-autophagosomal structure (PAS)—to execute its catalytic and scaffolding functions. Recent research has revealed that this recruitment occurs through two distinct, partially redundant mechanisms, each contributing specific functions to autophagy initiation[17][28][34][51][54]. The first mechanism operates through phosphatidylinositol 3-phosphate (PI3P) binding and involves the WIPI proteins (WD repeat domain phosphoinositide-interacting proteins, also known as Atg18 in yeast)[7][37][38]. The second mechanism is less well-characterized but involves direct interaction between the ATG16 complex and the ATG1 kinase complex through the N-terminal region of ATG12[17][28][34][51][54].

The PI3P-dependent recruitment pathway is initiated when the class III phosphatidylinositol 3-kinase (PI3K) complex produces PI3P at nascent autophagosomal membranes[7][37][38]. In mammalian cells, the WIPI2 protein binds directly to the WIPI2-interacting region (W2IR) of ATG16L1, which spans approximately residues 207–230[7][13]. Crystal structural analysis of the WIPI2–ATG16L1 complex revealed that the W2IR adopts an alpha-helical conformation and binds within an electropositive and hydrophobic groove located between beta-propeller blades 2 and 3 of WIPI2[7][13]. This interaction is highly specific; mutations at the WIPI2 binding interface significantly reduce or block the recruitment of the ATG12–ATG5–ATG16L1 complex to synthetic membranes in vitro and impair LC3 lipidation[7][13]. In fission yeast, the multiple Atg18/WIPI proteins—Atg18a, Atg18b, and Atg18c—play distinct roles in autophagy, with Atg18a being uniquely required for the targeting of the Atg12–Atg5·Atg16 complex[38]. Atg18a appears to serve as a binding platform for the recruitment of the Atg12–Atg5·Atg16 complex to the PAS in *S. pombe*[38].

The second recruitment mechanism discovered through recent research demonstrates that the Atg16 complex interacts with the Atg1 kinase complex via the N-terminal region of Atg12[17][28][34][51][54]. This interaction was demonstrated through co-immunoprecipitation experiments showing that the Atg16 complex, which requires intact Atg5 and Atg12 to form, physically associates with components of the Atg1 complex including Atg17[17][28][34]. The N-terminal 56 amino acids of Atg12 are specifically required for this interaction; deletion of this region (Atg12ΔN56) completely abolishes binding to the Atg1 complex while leaving the conjugation of Atg12 to Atg5 and the interaction with Atg16 intact[17][28][34]. The Atg1 complex serves as a scaffold for PAS organization and appears to represent the earliest-acting complex in autophagosome biogenesis; therefore, this Atg12-dependent recruitment mechanism is proposed to represent a PI3P-independent, early targeting pathway that precedes the PI3P-dependent pathway mediated by Atg21/WIPI proteins[17][28][34][51][54].

Importantly, these two recruitment pathways exhibit functional redundancy such that disruption of either pathway alone results in only partial autophagy defects, but simultaneous disruption of both pathways completely abolishes PAS localization of the Atg16 complex and prevents autophagy[17][28][34][51][54]. When cells or yeast strains lack both Atg21 and the Atg12 N-terminal region, the Atg16 complex cannot localize to the PAS and autophagy is completely blocked[17][28][34]. This redundancy ensures robust autophagosome formation under diverse cellular conditions and provides flexibility in the timing of Atg16 recruitment relative to other autophagy machinery components[17][28][34][51][54].

## Membrane Binding and Tethering: Molecular Mechanisms

ATG16 functions as a peripheral membrane-binding protein through its amphipathic alpha helix and contributes to membrane organization and vesicle clustering during autophagosome biogenesis. The membrane-binding characteristics of ATG16 have been dissected through subcellular fractionation experiments, in vitro liposome sedimentation assays, and reconstitution studies using giant unilamellar vesicles[8][11][16][31][32]. These studies reveal that ATG16, when in complex with ATG5 and ATG12, efficiently binds to lipid membranes, while the ATG12–ATG5 conjugate alone exhibits severely reduced membrane binding[8][11][31]. This observation indicates that ATG16 activation of membrane binding by ATG5 is a fundamental regulatory mechanism—ATG16 association with the ATG12–ATG5 conjugate unmasks a membrane-binding surface on ATG5 that is otherwise occluded by ATG12 conjugation[8][11][31].

The mechanism by which ATG16 activates membrane binding appears to involve both direct membrane interaction and relief of inhibition by ATG12[8][11][16][31][32]. When ATG16 associates with the ATG12–ATG5 conjugate through its N-terminal AFIM domain, a conformational change occurs that exposes hydrophobic residues on ATG5 required for lipid interaction[8][11][31][32]. ATG16 itself contributes to membrane binding through its amphipathic helix, and since ATG16 forms a homodimer, this dimerization may provide multiple membrane-binding surfaces or create a more extensive lipid-binding interface[16][31][32]. In vitro studies using giant unilamellar vesicles demonstrate that the ATG12–ATG5–ATG16 complex causes massive aggregation and clustering of vesicles in a manner that is entirely dependent on ATG16[8][11][31]. The clustering and tethering function of ATG16 appears to be mediated through the formation of bridges between membrane surfaces, as the homodimeric nature of ATG16 would allow a single dimer to contact multiple lipid bilayers simultaneously[8][31][32].

The functional significance of membrane binding by ATG16 is demonstrated by the observation that mutations preventing membrane association (such as the K160E/R171E double mutant of yeast Atg5, or disruption of the amphipathic helix in Atg16) result in severe autophagy defects despite normal PAS recruitment[8][11][31]. Cells expressing these membrane-binding-deficient mutants fail to efficiently promote ATG8 lipidation and show impaired formation of autophagosomes[8][11][31]. Furthermore, membrane binding is essential for the delivery of the ATG8-loaded E2 enzyme ATG3 to the lipid substrate phosphatidylethanolamine, suggesting that the ATG16 complex functions as a scaffold that brings together the catalytic machinery (Atg7, Atg3, and the lipid substrate) on the membrane surface[8][31][49]. This brings the substrate into proximity with the catalytic machinery, thereby greatly accelerating the lipidation reaction and specifying the location where ATG8 conjugation occurs[8][25][31][49].

## Catalytic Function in the ATG8 Lipidation Cascade

The primary catalytic role of the ATG16 complex involves facilitating the conjugation of the ubiquitin-like protein ATG8 to phosphatidylethanolamine (PE), a critical lipidation reaction essential for autophagosome biogenesis[2][9][25][27][49]. This reaction proceeds through a series of sequential enzymatic steps analogous to ubiquitin conjugation, except that the ultimate target is a lipid rather than a protein lysine residue[9][27][49]. The pathway involves four key enzymatic activities: the E1-like enzyme ATG7, which activates ATG8; the E2-like enzyme ATG3, which receives ATG8 via a thioester bond; the E3-like enzyme complex ATG12–ATG5–ATG16, which catalyzes the final transfer; and specific lipases or deconjugases that reverse the reaction when needed[9][27][30][49].

The ATG12–ATG5–ATG16 complex functions as an E3-like enzyme analogous to ubiquitin ligases, but with a critical difference: rather than catalyzing peptide bond formation between substrate and target lysine as in ubiquitination, it catalyzes ester bond formation between the carboxyl terminus of ATG8 and the primary amino group of the PE headgroup[9][27][49][52]. Biochemical reconstitution of this reaction using purified components and synthetic liposomes demonstrates that the E3 complex is absolutely required for efficient ATG8 lipidation[8][9][11][25]. The E3 complex enhances the catalytic activity of the E2 enzyme ATG3 through allosteric mechanisms; in the absence of E3, ATG3 exhibits very low activity in transferring ATG8 to PE, but when the full E3 complex is present, the lipidation reaction is dramatically accelerated[8][11][25][49].

The molecular mechanism by which the E3 complex enhances E2 activity has been clarified through structural and biochemical studies. The ATG12 component of the E3 complex directly interacts with ATG3 and positions this E2 enzyme optimally relative to the PE substrate on the membrane[25][49]. The ATG5 component provides membrane-binding activity that brings the entire catalytic assembly to the membrane surface where the PE substrate resides[8][11][31]. The ATG16 component amplifies membrane binding through its homodimeric organization and amphipathic helix[16][31][32]. Furthermore, ATG16 may function in specifying the site of ATG8 lipidation by clustering membrane regions and ensuring that ATG8 conjugation occurs at autophagy-relevant membranes rather than throughout the cell[25][29].

Recent structural and biophysical studies have revealed that multiple members of the ATG8/LC3-GABARAP family are substrates for this lipidation pathway in mammalian cells[29][52]. The efficiency of lipidation varies among these different ATG8 homologs, with GABARAP subfamily proteins generally being conjugated more efficiently than LC3 subfamily proteins when studied in vitro[29]. The E3 complex increases and speeds up lipidation of all family members and also increases the capacity of lipidated ATG8 family proteins to induce vesicle tethering and fusion[29]. However, interestingly, the E3 complex appears to restrict the fusion-promoting activity of lipidated ATG8 proteins, suggesting that the E3 may facilitate controlled membrane expansion during the elongation phase of autophagosome biogenesis by promoting tethering while constraining premature fusion[29].

## Autophagy-Independent Functions and Crosstalk Pathways

Although ATG16 is best characterized for its role in canonical autophagy, emerging evidence indicates that this protein participates in autophagy-independent cellular functions and mediates crosstalk between autophagy and other cellular degradation pathways[2][15][20]. The ubiquitin proteasome system (UPS) and autophagy represent the two major cellular degradation pathways; growing evidence suggests that ATG16 and other autophagy machinery proteins regulate the balance between these systems and even mediate their functional coordination[2][15][36].

One important autophagy-independent function of ATG16 involves LC3-associated phagocytosis (LAP), a non-canonical autophagy pathway that occurs downstream of phagocytosis and does not require core autophagy initiation factors[15][20]. LAP has been shown to require the WD40 domain of mammalian ATG16L1, but not factors required for canonical autophagy such as ULK1, AMBRA1, ATG14, or FIP200[15][20]. This compartmentalization of function demonstrates that the WD40 domain of ATG16L1 is a critical module for non-canonical autophagy functions distinct from canonical autophagosome biogenesis[20]. The WD40 domain serves to recruit ATG16L1 to single-membrane endolysosomal compartments rather than double-membrane autophagosomes, representing a novel membrane recruitment mechanism distinct from the WIPI2/PI3P-dependent recruitment to canonical autophagosomes[20].

ATG16 also participates in crosstalk with the ubiquitin proteasome system through its interaction with the selective autophagy adaptor p62/SQSTM1 and its role in proteaphagy—the autophagic degradation of proteasomes themselves[2][15][36]. In plants, proteaphagy has been demonstrated to involve ATG16 homologs and appears to be mediated by direct recognition of proteasomal subunits through interaction with autophagy machinery[2]. The selective autophagy adaptor p62/SQSTM1 acts as a bridge between the ubiquitinated cargo destined for proteasomal degradation and the autophagy machinery, and this process appears to require the ATG16-containing complex[2][36].

The relationship between autophagy and the proteasome system is bidirectional; inhibition of autophagy leads to accumulation of p62 and impaired clearance of ubiquitinated proteins through the proteasome, despite proteasomal catalytic activity remaining normal[2][36]. This suggests that autophagy, and specifically ATG16-dependent processes, facilitate delivery of substrates to the proteasome or prevent sequestration of these substrates in aggregates that are inaccessible to proteasomal degradation[2][36]. The p62-mediated targeting of ubiquitinated protein aggregates to autophagy depends on interaction with LC3/ATG8 through the LC3-interacting region (LIR) domain of p62, and the ability of p62 to interact with the ubiquitin proteasome complex suggests that ATG16-containing autophagosomal membranes may preferentially sequence certain UPS substrates[2][36].

## Cellular Localization and Subcellular Dynamics

The subcellular localization of ATG16 undergoes dynamic changes during the autophagy cycle, reflecting its recruitment to and dissociation from sites of autophagosome biogenesis. In vegetative (non-starved) cells, ATG16 is predominantly cytosolic, with only a small fraction localized to the perivacuolar PAS[41]. Upon induction of autophagy through nutrient starvation, ATG16 rapidly forms punctate structures that colocalize with other Atg proteins, particularly ATG8 and ATG5[38][41]. These puncta represent the PAS, where multiple autophagy factors concentrate to drive autophagosome biogenesis[14][41][57]. Quantitative analysis of autophagy protein stoichiometry at the PAS in yeast reveals that ATG16 is present at relatively low abundance compared to other Atg proteins such as ATG8, suggesting that ATG16 may function at limiting concentrations[41].

The dynamic localization of ATG16 to punctate structures is absolutely dependent on the presence of other autophagy machinery components[17][28][34][38]. In *S. pombe*, deletion of *atg18a* (encoding the WIPI protein) blocks PAS recruitment of both Atg5 and Atg16, preventing the formation of autophagosomal structures[38]. Similarly, disruption of the Atg12-dependent recruitment pathway through deletion of the N-terminal region of Atg12 prevents PAS localization of Atg16[17][28][34]. This strict dependence on recruitment mechanisms ensures that ATG16 localizes only to sites where autophagosome formation is occurring and where the proper lipid and protein substrates are assembled[17][28][34][38].

Following the nucleation and initial expansion of the phagophore, ATG16 is thought to remain associated with the expanding membrane, but this has not been directly visualized in most systems. The timing of ATG16 association with autophagosomal membranes appears to be relatively transient; ATG16 is recruited early in phagophore biogenesis during the nucleation and expansion phases but may be released as the phagophore matures and closes to form a sealed autophagosome[25][41]. This transient association is consistent with the reversible nature of ATG8 lipidation, which is catalyzed by the ATG16-containing E3 complex but can be reversed by deconjugating enzymes[30]. The recycling of ATG16 and other autophagy machinery proteins from completed autophagosomes back to cytosolic pools or to the PAS for reuse represents an important aspect of autophagy flux[30][41].

The membrane dynamics and localization of ATG16 are regulated by post-translational modifications including phosphorylation[2][9][27]. In mammalian cells, the ATG12–ATG5–ATG16L1 complex can be phosphorylated at specific residues, and these modifications appear to regulate both its recruitment to autophagosomes and its catalytic activity[2]. In yeast, phosphorylation of Ser139 in ATG12 promotes complex formation, whereas methylation of Lys151 in ATG16 inhibits complex assembly in cardiomyocytes[2]. These regulatory modifications provide additional layers of control over ATG16 function, allowing cells to modulate autophagy flux in response to distinct environmental signals and metabolic states.

## Structural Basis of ATG16 Function and Evolutionary Conservation

The structural features of ATG16 that mediate its biological functions have been conserved throughout eukaryotic evolution, from single-celled yeasts to multicellular organisms[10][19][24][35]. Comparative structural analysis of Atg16 proteins from *S. cerevisiae*, *S. pombe*, and mammals reveals conservation of the N-terminal Atg5-binding domain, the central coiled-coil dimerization domain, and in mammals, the C-terminal WD40 repeats[10][24][35][43]. The AFIM motif responsible for Atg5 binding is particularly well-conserved, with key residues such as Arg-35 and Phe-46 (in yeast Atg16) being absolutely critical for both Atg5 interaction and autophagy function[10].

The crystal structure of the yeast Atg5–Atg16(1-46) complex at 1.97 Angstrom resolution reveals the atomic basis of Atg5-Atg16 interaction[10]. The structure shows that Atg5 comprises two ubiquitin-like domains flanking a helix-rich domain; the N-terminal region of Atg16 binds within a groove formed by these three domains of Atg5[10]. In vitro analysis demonstrated that Arg-35 and Phe-46 of Atg16 are crucial for this interaction, and Atg16 mutants with changes at these residues fail to localize to the PAS and cannot restore autophagy in Atg16-deficient cells[10]. Furthermore, these critical Atg16 residues are positioned such that they form hydrophobic and electrostatic interactions with complementary surfaces on Atg5, explaining the high specificity of this interaction[10].

The coiled-coil domain of ATG16, which mediates homodimerization, has been subject to detailed structural and functional analysis[16][32][35]. Crystallographic studies of the isolated coiled-coil domain (amino acids 55–142 in yeast Atg16) demonstrate that this region forms a parallel coiled-coil dimer stabilized by hydrophobic interactions between leucine residues at the "a" and "d" positions of the heptad repeat pattern characteristic of coiled-coils[16][32]. Mutation of critical leucine residues (L71A, L75A, L85A, L99A) that mediate the coiled-coil interaction prevents dimer formation and completely abolishes autophagy function, demonstrating the biological necessity of Atg16 homodimerization[16][32].

The membrane-binding amphipathic helix of ATG16 (approximately residues 113–131 in yeast) contains a characteristic pattern of hydrophobic and polar residues consistent with insertion into lipid bilayers[16][32]. The hydrophobic face of this helix comprises hydrophobic amino acids (leucines and isoleucines) that favorably interact with the acyl chains of membrane lipids, while the polar face contains charged and polar residues that interact with the aqueous environment and lipid headgroups[16][32]. This amphipathic organization allows ATG16 to stably anchor to membranes without forming a transmembrane helix; instead, it functions as a peripheral membrane protein[16][32]. The critical importance of this domain is demonstrated by point mutations that disrupt membrane binding, which result in loss of autophagy function despite normal expression, localization to the PAS, and binding to Atg5[8][11][16][31][32].

## Disease Associations and Functional Variants

The ATG16L1 gene has achieved clinical significance through its association with Crohn's disease, a chronic inflammatory bowel disease affecting millions of people worldwide[44][47]. Multiple genome-wide association studies have identified the Thr300Ala (T300A) polymorphism in ATG16L1 as one of the most frequently associated genetic variants with Crohn's disease susceptibility[44][47]. The T300A mutation results in enhanced degradation of ATG16L1 via caspase-3-mediated cleavage, leading to reduced steady-state levels of ATG16L1 protein and decreased autophagic flux[44][47]. This reduced autophagy impairs several antimicrobial and immune functions, including diminished clearance of intracellular bacteria and altered secretion of antimicrobial peptides by intestinal Paneth cells[44][47].

Studies in genetically modified mice have revealed that the T300A variant affects both gut microbial composition and immune cell populations in a manner consistent with impaired autophagy[44]. Mice expressing the T300A allele display alterations in bacterial abundance, with increases in specific bacterial species including *Bacteroides ovatus*[44]. Furthermore, these mice show elevated Th17 and Th1 T cell populations in the gut-associated lymphoid tissue, suggesting enhanced pro-inflammatory immune responses[44]. These changes occur before overt disease symptoms develop, indicating that the autophagy defect associated with T300A creates a predisposing condition for inflammatory disease[44]. The functional consequence of reduced ATG16L1 abundance is impaired bacterial sequestration through xenophagy and altered innate immune responses to microbial products[44].

The structural basis for the association of T300A with disease susceptibility has been clarified through biochemical studies demonstrating that this position is a caspase-3 cleavage site[44]. During cellular stress or certain inflammatory responses, activated caspase-3 cleaves ATG16L1 at the T300A position, releasing the C-terminal WD40 domain from the remainder of the protein[44]. The resulting protein fragments exhibit reduced ability to promote autophagy and inflammatory responses, creating a molecular basis for the observed disease phenotype[44]. The T300A mutation enhances the rate of caspase-3-mediated cleavage relative to the wild-type threonine, explaining why the polymorphism represents a loss-of-function variant[44].

Beyond the T300A variant, other disease associations have been identified for ATG16L2, a mammalian-specific isoform of ATG16L[2][43][55]. A study examining ATG16L2 expression in multiple sclerosis (MS) patients found that both mRNA and protein levels of ATG16L2 were decreased in MS patient samples compared to healthy controls[2]. This observation suggests that ATG16L2 may play an important role in autophagy of T cells and may serve as a potential biomarker for predicting relapse rates in MS patients, although further investigation is required[2]. The identification of disease associations with ATG16 variants and isoforms underscores the fundamental importance of this protein in immune homeostasis and inflammatory regulation.

## Evolutionary Perspectives and Comparative Biology

The conservation of ATG16 across eukaryotic organisms from single-celled yeasts to mammals reflects the ancient origin and essential nature of autophagy in cellular homeostasis[19][38][39][46]. Systematic comparative analysis of autophagy factors across yeast species, including *S. cerevisiae* and *S. pombe*, reveals that core autophagy components including ATG16 have been maintained with high fidelity across evolutionary time despite 500 million years of divergence[19][38]. The evolutionary conservation extends to the organization of the ATG12–ATG5–ATG16 complex and the fundamental mechanisms of autophagosome biogenesis, suggesting that these processes represent evolutionarily optimal solutions to the cellular problem of protein degradation and recycling[19][38][39].

Comparative studies between yeast and mammalian autophagy have revealed both conserved and divergent aspects of ATG16 function[19][38]. While the basic structural features and biochemical activities of ATG16 are highly conserved, mammalian systems have evolved additional complexity through the presence of multiple isoforms (ATG16L1 and ATG16L2) and the WD40 domain present only in mammals[43][55]. The WD40 domain of ATG16L1 enables distinct functions including participation in non-canonical autophagy processes, suggesting that mammalian evolution has elaborated the basic yeast ATG16 scaffold to perform additional cellular tasks[20][43]. The identification of ATG16 and other autophagy factors in ancient lineages such as plants and protists indicates that autophagy predates the diversification of eukaryotes and likely arose as a fundamental mechanism for intracellular protein homeostasis in the earliest eukaryotic cells[46].

The comparative analysis of autophagy mechanisms across plants and animals reveals important principles about autophagy evolution[46]. In plants such as *Arabidopsis thaliana*, mutants defective in ATG genes including *atg16* homologs show severe phenotypes including early senescence, starvation sensitivity, and accumulation of protein aggregates, similar to the phenotypes observed in yeast and mammalian systems[46]. This conservation of phenotype despite substantial evolutionary divergence underscores the fundamental importance of the autophagy machinery in eukaryotic cell biology[46]. The identification of autophagy-independent functions of ATG16 in both mammalian and plant systems suggests that these functions may represent conserved, non-redundant roles of ATG16 beyond its canonical autophagy function[46].

## Integration into Broader Autophagy Networks

ATG16 functions as a critical hub integrating multiple aspects of autophagy regulation and membrane dynamics. The protein interacts with numerous other autophagy factors beyond those already discussed, including FIP200, which recruits ATG16L1 to sites of phagophore initiation in mammalian cells, and RAB33B, a small GTPase involved in membrane trafficking[13][21][25]. The interaction of ATG16L1 with FIP200 occurs through a distinct binding site (approximately residues 239–246 in ATG16L1) that is spatially adjacent to but separate from the WIPI2 binding site, suggesting that multiple recruitment pathways converge on distinct regions of ATG16L1[13][25]. The interplay between FIP200 and WIPI2 binding to ATG16L1 remains incompletely understood, but evidence suggests that FIP200 binding alone is insufficient to support autophagy, whereas binding to both FIP200 and WIPI2 is required for efficient autophagosome formation[13][25].

The TRIM16 protein has been identified as a scaffold that facilitates autophagy-mediated clearance of protein aggregates through interaction with multiple autophagy factors including ATG16L1[33]. TRIM16 promotes formation of protein aggregates under stress conditions and simultaneously facilitates autophagic degradation of these aggregates by assembling a platform that brings together core autophagic machinery components including ULK1 (autophagy initiation), ATG16L1 (elongation), and LC3B (completion)[33]. This function of TRIM16 illustrates how ATG16L1 participates in broader cellular stress responses beyond the basal autophagy that occurs during nutrient starvation[33].

## Conclusion

The *atg16* gene in *Schizosaccharomyces pombe* encodes a highly conserved autophagy protein that functions as a critical structural and catalytic component of the autophagy machinery. ATG16 assembles with ATG12 and ATG5 to form a specialized E3-like ubiquitin ligase that catalyzes the conjugation of the ubiquitin-like protein ATG8 to phosphatidylethanolamine during autophagosome biogenesis. The protein exhibits multiple distinct functional domains: an N-terminal ATG5-binding domain, a central coiled-coil homodimerization domain, and an amphipathic membrane-binding helix. ATG16 localizes to the pre-autophagosomal structure through two partially redundant recruitment mechanisms—a PI3P-dependent pathway mediated by WIPI/Atg18 proteins and a PI3P-independent pathway mediated by interaction with the Atg1 kinase complex. At the PAS, ATG16 functions in membrane tethering and clustering while simultaneously promoting the catalytic transfer of ATG8 to PE, thereby simultaneously organizing membranes and decorating them with lipidated autophagy markers.

Beyond canonical autophagy, emerging evidence indicates that ATG16 participates in autophagy-independent cellular functions including non-canonical autophagy pathways and crosstalk with the ubiquitin proteasome system. The disease association of ATG16L1 variants with Crohn's disease and multiple sclerosis demonstrates the biological significance of this protein in immune homeostasis. The structural features and biochemical mechanisms of ATG16 have been conserved throughout eukaryotic evolution, from single-celled yeasts to mammals, reflecting the fundamental importance of autophagy in cellular homeostasis. Future investigations into ATG16 regulation, its interactions with newly discovered autophagy factors, and its role in disease pathogenesis will likely reveal additional dimensions of ATG16 function and provide insights into the basic mechanisms controlling cellular degradation and recycling pathways.

## Citations

1. https://www.pombase.org/gene/SPBC405.05
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6356889/
3. https://dnaconda.riken.jp/search/SPD_pombe/Sp03/Sp03F02.html
4. https://www.uniprot.org/uniprotkb/O94656/entry
5. https://www.uniprot.org/uniprotkb/Q676U5/entry
6. https://www.cusabio.com/Recombinant-Protein/Recombinant-Schizosaccharomyces-pombe-Meiotic-chromosome-segregation-protein-C4-637693.html
7. https://elifesciences.org/articles/70372
8. https://pubmed.ncbi.nlm.nih.gov/23064152/
9. https://pubmed.ncbi.nlm.nih.gov/24070470/
10. https://www.ebi.ac.uk/thornton-srv/databases/cgi-bin/pdbsum/GetPage.pl?pdbcode=2dym
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC3590266/
12. https://www.yeastgenome.org/locus/S000004769
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC2366851/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC7173070/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC7924733/
16. https://elifesciences.org/articles/43088
17. https://journals.biologists.com/jcs/article-pdf/133/20/jcs249227/3512148/jcs249227.pdf
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC3738441/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC5813257/
20. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.15833
21. https://www.pombase.org/reference/PMID:23950735
22. https://journals.biologists.com/dev/article/144/21/3990/48186/Drosophila-Atg16-promotes-enteroendocrine-cell
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC4502675/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC2366860/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC3877172/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC2529362/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC9894987/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC3427254/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC6138442/
30. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0076237
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC5415757/
32. http://reactome.org/content/detail/R-HSA-5676229
33. https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1003715
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC4846508/
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC9620852/
36. https://rupress.org/jcb/article/182/1/129/45336/Quantitative-analysis-of-autophagy-related-protein
37. https://www.yeastgenome.org/locus/ATG12
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC3288023/
39. https://elifesciences.org/articles/39982
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC6899017/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC8615172/
42. https://academic.oup.com/ecco-jcc/article/15/Supplement_1/S155/6286095
43. https://www.molbiolcell.org/doi/full/10.1091/mbc.E03-09-0704?view=long&pmid=14699058
44. https://dc.uthsc.edu/dissertations/514/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC7265318/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC4111135/
47. https://journals.biologists.com/jcs/article/128/2/193/55240/Membrane-dynamics-in-autophagosome-biogenesis
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC6405243/
49. https://pubmed.ncbi.nlm.nih.gov/25484072/
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC6028034/
51. https://www.bmbreports.org/journal/download_pdf.php?spage=129&volume=48&number=3
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC6243101/