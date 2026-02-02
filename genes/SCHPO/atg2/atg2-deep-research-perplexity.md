---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-30T19:41:40.969188'
end_time: '2026-01-30T19:43:41.551121'
duration_seconds: 120.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: atg2
  gene_symbol: atg2
  uniprot_accession: O94649
  protein_description: 'RecName: Full=Autophagy-related protein 2; AltName: Full=Meiotically
    up-regulated gene 36 protein;'
  gene_info: Name=atg2; Synonyms=mug36; ORFNames=SPBC31E1.01c, SPBC660.18c;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the ATG2 family. .
  protein_domains: ATG2. (IPR026849); ATG2_CAD (PF13329)
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
- **UniProt Accession:** O94649
- **Protein Description:** RecName: Full=Autophagy-related protein 2; AltName: Full=Meiotically up-regulated gene 36 protein;
- **Gene Information:** Name=atg2; Synonyms=mug36; ORFNames=SPBC31E1.01c, SPBC660.18c;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the ATG2 family. .
- **Key Domains:** ATG2. (IPR026849); ATG2_CAD (PF13329)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atg2" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atg2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atg2** (gene ID: atg2, UniProt: O94649) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Autophagy-Related Protein 2 (Atg2) in Schizosaccharomyces pombe: Structure, Function, and Mechanisms in Autophagosome Biogenesis

## Summary of Key Findings

Autophagy-related protein 2 (Atg2, UniProt O94649) from the fission yeast *Schizosaccharomyces pombe* is a large multifunctional protein representing one of the most evolutionarily conserved yet previously enigmatic components of the autophagy machinery. Recent structural and biochemical advances have revealed that Atg2 functions as a novel nonvesicular phospholipid transfer protein that mediates de novo autophagosome formation through dual mechanisms: physically tethering the endoplasmic reticulum (ER) to the expanding phagophore membrane while simultaneously transferring lipids between these two membrane compartments[1][7]. The protein localizes exclusively to contact sites between the ER exit sites (ERES) and the edge of the isolation membrane (IM), where it operates in complex with the phosphoinositide-binding protein Atg18 and the lipid scramblase Atg9 to coordinate the massive lipid redistribution required for autophagosome expansion. This discovery has fundamentally changed our understanding of how cells build the double-membrane autophagosomes during autophagy, revealing that lipid transfer proteins can directly mediate de novo organelle biogenesis rather than relying solely on vesicular trafficking mechanisms.

## Historical Discovery and Early Characterization of Atg2

### Initial Identification and Genetic Basis

The *atg2* gene was first identified in 1993 through a comprehensive screening of *Saccharomyces cerevisiae* autophagy-defective mutants that discovered thirteen autophagy genes, designated *apg* genes, which were later renamed to the *atg* nomenclature[1]. In *S. pombe*, the gene was identified through a large-scale screen for genes required for critical meiotic events and is also known by its alternative name *mug36* (meiotically up-regulated gene 36), reflecting its initial discovery in the context of meiotic processes[2][21]. Eight years after the initial identification, in the early 2000s, the *atg2* gene was formally cloned and sequenced, establishing that the protein product was essential for autophagosome formation during starvation-induced autophagy[1].

### Early Functional Recognition

Even before detailed molecular characterization, researchers recognized that Atg2 possessed unusual properties as a peripheral membrane protein with high affinity for membranes[1]. The protein's behavior during autophagy was distinctive: it accumulated at the preautophagosomal structure (PAS, also called the phagophore assembly site) and localized specifically to nascent autophagosomal structures during their formation and expansion. When the *atg2* gene was deleted in yeast strains, autophagy was severely impaired, resulting in accumulation of autophagic cargo and defective autophagosome formation. However, the precise molecular mechanism by which Atg2 contributed to autophagy remained mysterious for decades, earning it a reputation as one of the most poorly understood proteins in the autophagy field[1][7].

## Structural Organization and Molecular Architecture

### Full-Length Protein Architecture

Atg2 proteins are exceptionally large molecules, with *Schizosaccharomyces pombe* Atg2 comprising 1,646 amino acid residues, and mammalian ATG2A reaching 1,938 residues[2]. Despite these large sizes, the protein maintains a characteristic elongated, rod-like morphology that extends approximately 20 nanometers in length with a width of roughly 30 angstroms[8]. This extended structure is fundamentally different from the compact, globular folds typical of most proteins, instead resembling a long bridge or tunnel-like apparatus.

### Conserved Domains and Functional Modules

At the molecular level, Atg2 proteins are organized into distinct functional domains with remarkable conservation across eukaryotes. The most highly conserved region resides at the N-terminus, where a domain designated **Chorein_N** (named after its similarity to domains in the protein Chorein, also called VPS13) contains the primary lipid transfer module[1][8][9]. This Chorein_N domain has been crystallized from *Schizosaccharomyces pombe* Atg2 (designated SpAtg2^NR^) at 2.7 angstrom resolution, revealing a globular structure comprising a helical region and a twisted β-sheet that fold together to create a large hydrophobic cavity[1][50]. When phosphatidylethanolamine (PE), a major cellular glycerophospholipid, is mixed with the SpAtg2^NR^ domain in crystallization conditions, a complex forms in which the PE molecule binds with its acyl chains buried within the hydrophobic cavity while the phosphate head group remains exposed to the aqueous solvent[1][50].

The central region of Atg2 contains five repeat structures primarily composed of β-strands rich in hydrophobic residues, predicted to form β-jellyroll-like folds that create successive hydrophobic grooves or pathways[1][50]. These repeating structures are proposed to form a continuous hydrophobic channel extending through the rod-shaped molecule. At the C-terminal end, Atg2 proteins contain a specialized domain designated **ATG2_CAD** (a cysteine-alanine-aspartic acid triad region) that appears to form one of the membrane-binding surfaces in complex with the cofactor Atg18[1][7][28].

Two distinct membrane-binding regions have been identified through truncation analysis: one at the N-terminus involving amino acids 2-21, and another at the C-terminus spanning residues 1,347-1,592 in *S. cerevisiae* Atg2[1][7]. While each binding site alone is sufficient for binding to membranes, both sites are required for the membrane-tethering function, indicating that both tips of the elongated rod simultaneously engage with separate membrane bilayers[1][7][38].

### Amphipathic Helix Localization Region

In mammalian ATG2A and ATG2B proteins, and similarly conserved in other organisms, a region designated the **C-terminal localization region (CLR)** spanning amino acids 1,723-1,829 in ATG2A contains amphipathic α-helices that mediate both autophagosomal membrane association and localization to lipid droplets[16][49]. This region is distinct from the primary lipid transfer module but contributes importantly to proper subcellular targeting of the protein.

## Biochemical Functions: Lipid Transfer and Membrane Tethering

### Discovery of Lipid Transfer Activity

The recognition that Atg2 functions as a lipid transfer protein emerged from parallel structural and biochemical investigations conducted primarily between 2018 and 2020[1][7][8][9]. Purified mammalian ATG2A protein was shown to bind to liposomes in a phosphoinositide-independent manner, in contrast to other autophagy proteins such as WIPI4 that strictly require high percentages of phosphatidylinositol-3-phosphate (PI3P) for liposome binding[1][8]. This broader binding capability suggested a different molecular basis for Atg2 function.

When researchers performed classic biochemistry experiments mixing purified ATG2A with donor and acceptor liposomes containing fluorescently labeled lipids, they observed transfer of multiple lipid species between the liposomes, including phosphatidylethanolamine (PE), phosphatidylserine (PS), and phosphatidylinositol (PI)[8][9]. Critically, each individual ATG2A molecule can bind and transfer approximately twenty glycerophospholipid molecules simultaneously, distinguishing it from classic lipid transfer proteins that typically transfer one lipid molecule at a time[9]. This high-capacity binding is achieved through the extended hydrophobic cavity running the length of the elongated rod-shaped molecule.

### Lipid Transfer Kinetics and Rate Parameters

Quantitative analysis of ATG2A-mediated lipid transfer in *in vitro* assays revealed transfer rates of approximately 0.017 fluorescent-lipid molecules per protein per second in standard fluorescence-based assays[54]. When accounting for non-fluorescent lipid transfer, which occurs in parallel, the overall transfer rate could reach approximately 50-fold higher, estimating overall transfer rates of potentially 8-10 lipid molecules per protein per second[10][54]. However, even with these optimistic corrections, researchers recognized that the calculated transfer rates appeared insufficient to account for the tens of millions of lipids required to build an entire autophagosome in the observed timeframe of 5-10 minutes[10][54].

### Membrane Tethering Activity

In parallel with lipid transfer characterization, biochemical studies revealed that purified ATG2A exhibits robust **membrane-tethering (MT) activity**[1][7][8]. When ATG2A was incubated with small unilamellar vesicles (SUVs), dynamic light scattering experiments demonstrated a dramatic shift in the size distribution toward larger vesicles, indicating that ATG2A was bridging and clustering SUVs together[11][37][40]. The two tips of the elongated ATG2A molecule act independently to bind separate membranes, spacing them approximately 10-20 nanometers apart—a distance characteristic of organelle contact sites observed throughout the cell[11][40].

The membrane-tethering activity of ATG2A demonstrated preference for membranes containing lipids with **lipid-packing defects**, such as those rich in phosphatidylethanolamine (PE) or those with high membrane curvature[37][40][51]. Small unilamellar vesicles with high curvature were efficiently tethered by ATG2A, whereas large unilamelular vesicles (LUVs) with lower curvature were not tethered despite maintaining interaction with the protein[40]. This selectivity for high-curvature membranes proved functionally relevant, as both the expanding IM edge and the ERES naturally assume high-curvature geometries in cells[1][50].

### Substrate Specificity and Lipid Preference

While ATG2A can transfer multiple glycerophospholipid species, detailed studies examining lipid transfer efficiency revealed important substrate preferences[8][37][40][54]. Transfer occurred most efficiently for lipids with packing defects introduced by small head groups (such as PE) or for negatively charged lipids including phosphatidylserine (PS) and phosphatidylinositol (PI)[37][40][54]. The transfer efficiency depended strongly on both the lipid composition and the presentation geometry of the donor and acceptor membranes, with tethered membranes showing dramatically enhanced transfer rates compared to untethered membranes[37][40].

Notably, PI3P-enriched membranes (such as the nascent phagophore) served as preferred acceptor membranes for ATG2A-mediated lipid transfer, while the phosphoinositide-rich ER provided the donor compartment[8][40][54]. This directional preference, while not absolute, suggests that the phagophore-ER membrane contact sites and the local lipid compositions naturally favor the directionality of lipid flow required for autophagosome expansion[8][40][54].

## Protein Interactions and Complex Assembly

### The Atg2-Atg18 Complex

Atg2 functions as part of a larger molecular complex with the phosphoinositide-binding protein Atg18 (called WIPI1, WIPI2, or WIPI4 in mammalian cells)[1][7][15][26]. The Atg18 protein belongs to the PROPPIN (phosphoinositide-interacting protein) family and comprises seven WD40 repeats that fold into a characteristic β-propeller structure[26][38][53]. The Atg2-Atg18 complex was first recognized as a functional unit through genetic and cell biological studies, and the physical interaction was subsequently confirmed through biochemical approaches[26].

Recent structural studies revealed that Atg18 binding occurs near the C-terminal region of Atg2, with the 7AB loop of Atg18 serving as a key binding interface[26][29]. The crystal structure of *Schizosaccharomyces pombe* Atg18 determined at 2.8 angstrom resolution demonstrated that the 7AB loop located on the β-propeller structure provides a critical contact point for Atg2 interaction[26][29]. Disruption of this specific loop by deletion resulted in severely impaired Atg2 binding and loss of Atg2 localization to the phagophore assembly site, demonstrating the functional importance of this interaction[26][29].

Atg18 itself contains two phosphoinositide-binding sites: Site 1 located on blade 5 shows higher affinity for PI(3,5)P₂, while Site 2 on blade 6 exhibits stronger binding to PI(3)P[26][38][53]. The 6CD loop of Atg18 is particularly flexible and prone to forming an amphipathic helix that can insert into lipid bilayers, with this region being critical for the membrane scission activity attributed to the Atg2-Atg18 complex[26][53].

### Interaction with Atg9 and Lipid Scramblase Coupling

Emerging research has revealed that Atg2 physically interacts with Atg9, the transmembrane lipid scramblase protein embedded in autophagosomal and vesicular membranes[10][20][39]. The structural basis for this interaction involves alignment of the hydrophobic groove of ATG2A with the internal channel of ATG9A, suggesting direct hand-off of lipids between the transfer and scramblase activities[39]. This coupling represents an elegant solution to the challenge of asymmetric lipid distribution: ATG2 transfers lipids primarily to the outer leaflet of the nascent phagophore, while ATG9 scramblase activity equilibrates lipids between the inner and outer leaflets[20][39].

ATG9A forms a stable trimeric complex with a solvated central pore connected laterally to the cytosol through cavities within each protomer[20]. Molecular dynamics simulations and structural analysis suggest that the central pore of ATG9A can open laterally to accommodate lipid headgroups, enabling lipids to flip between membrane leaflets in an energy-independent manner[20]. The interaction between ATG2A and ATG9A creates a heterotetrameric complex that couples lipid transfer with lipid scrambling for bidirectional lipid distribution[39].

### Interaction with Atg1 Complex and Signaling

Recent studies discovered that the Atg2-Atg18 complex interacts with the Atg1 protein kinase complex, involving the C-terminal regions of Atg2[15][18]. This interaction appears to organize the spatial architecture of autophagosome nucleation sites and may coordinate signaling and lipid delivery processes during early autophagosome formation.

### Interaction with WIPI4 and PI3P Recognition

In mammalian cells, the WIPI4 protein (the mammalian ortholog of Atg18) associates with ATG2A to facilitate binding to PI3P-enriched phagophore membranes[8][11][40]. The ATG2A-WIPI4 complex exhibits asymmetric membrane binding capabilities through its two tips: the CAD tip binds PI3P-containing membranes via WIPI4, while the N tip can bind PI3P-free membranes such as the ER[11][40]. This asymmetric tethering geometry is particularly important, as it allows the complex to simultaneously recognize the distinct lipid compositions of the phagophore and ER compartments[11][40].

### Gabarap Interaction and Autophagosome Closure

Critical recent findings revealed that ATG2A contains a highly conserved **LC3 interaction region (LIR)** motif at amino acids 1,362-1,365 in ATG2A and 1,491-1,494 in ATG2B[16][55]. This LIR allows direct interaction with the Atg8/LC3/GABARAP family of proteins, which are ubiquitin-like proteins conjugated to phosphatidylethanolamine on autophagosomal membranes[55]. The ATG2A-GABARAP interaction proved essential for autophagosome closure rather than phagophore expansion, with mutations disrupting this interaction resulting in accumulation of unsealed phagophores[55]. Strikingly, this closure function is independent of the ATG2A-WIPI4 interaction required for lipid transfer and membrane tethering[55], demonstrating that Atg2 functions in two sequential, mechanistically independent steps of autophagosome biogenesis.

## Subcellular Localization and Membrane Contact Site Assembly

### Phagophore-ER Membrane Contact Sites (PERCS)

*Schizosaccharomyces pombe* Atg2, like its mammalian and budding yeast counterparts, localizes exclusively to contact sites between the ER and the edge of the expanding phagophore, designated **phagophore-ER contact sites (PERCS)** or more generally as **phagophore-ER membrane contact sites (PERMCSs)**[7][13][16]. These contact sites represent specialized regions where the two membranes are held in close apposition at distances of 10-20 nanometers, a geometry ideal for nonvesicular lipid transfer[7][13][16].

The localization of Atg2 to PERCS depends critically on several upstream factors[13]. The ER-exit site (ERES) component Sec13 and the TRAPPIII complex work cooperatively with Atg2 to establish and maintain these membrane contact sites[13]. Bimolecular fluorescence complementation (BiFC) studies demonstrated that Atg2 physically associates with Sec13, suggesting direct interaction between the autophagy machinery and ERES components[13]. Deletion of the *trs85* gene, which encodes a TRAPPIII complex component, reduced the BiFC signal between Sec13 and Atg2, indicating that TRAPPIII contributes to organizing the ERES localization at phagophore-ER contact sites[13].

### Temporal Dynamics of Atg2 Localization

Live-cell imaging studies in fission yeast revealed that newly formed PAS structures localize between the ER and the vacuole in most cases, with Atg2 appearing at the PAS immediately upon its formation[13]. This intimate spatial relationship between nascent phagophores and the ER suggests that the ER-phagophore contact site is not a late consequence of autophagosome formation but rather a primary determinant of autophagosome nucleation and early expansion[13]. At the PAS, Atg2-GFP forms punctate structures or small dots representing individual or clusters of autophagosome assembly sites[27].

### Phosphoinositide-Dependent Recruitment

The recruitment of Atg2 to autophagosomal structures depends on the generation of PI3P by the phosphatidylinositol 3-kinase (PI3K) complexes localized at the PAS[1][33]. Treatment of cells with wortmannin, a pharmacological inhibitor of class III PI3K, prevented the recruitment of Atg2/ATG2A to forming autophagosomes, while the upstream Atg1/ULK complex could still form[7][33]. This hierarchical organization indicates that ATG2 recruitment occurs downstream of PI3K activation and PI3P generation on the nascent phagophore[7][33].

The PI3P effector WIPI proteins (particularly WIPI4 in mammalian cells) are crucial for targeting ATG2A to the phagophore[8]. Overexpression of inactive WIPI4 mutants unable to bind PI3P prevented normal ATG2A recruitment, while providing excess wild-type WIPI4 enhanced ATG2A localization to autophagosomal structures[8].

## Atg2 in Autophagosome Formation and Expansion

### Role in Phagophore Elongation and Growth

The primary function of Atg2 in autophagy is to facilitate the dramatic expansion of the nascent isolation membrane or phagophore from its initial nucleation as a small crescent or cup-like structure into a large double-membrane autophagosome capable of enclosing cytoplasmic cargo. During the expansion phase, the phagophore grows from a few hundred nanometers in diameter to eventually reach sizes of 500-1500 nanometers depending on the cargo being engulfed[1][7][8].

In *atg2* deletion mutants of budding yeast, autophagosomes fail to expand properly and remain as small, immature structures, with cargo remaining protease-accessible rather than protected within sealed autophagosomes[1][45]. Similarly, in mammalian cells with simultaneous knockout of ATG2A and ATG2B, unclosed autophagic structures accumulate at the phagophore assembly sites, with the phagophore capable of forming but unable to expand and seal[33]. These observations directly implicate Atg2 in the critical expansion step rather than in the initial nucleation of the phagophore.

### Lipid Supply from ER to Phagophore

The model emerging from multiple lines of evidence indicates that Atg2 mediates the physical supply of lipids from the ER to the growing phagophore membrane. In 2017, researchers demonstrated that the movement of lipophilic dyes from the ER to IM precursors was completely blocked by deletion of Atg2, even when other early autophagy factors were present[1][7]. This direct evidence for Atg2-mediated lipid movement between the ER and phagophore provided the crucial experimental support for the lipid transfer model.

The proposed mechanism involves Atg2-mediated extraction of lipids from the curved membranes of the ER-exit sites and subsequent delivery to the expanding edge of the phagophore where they serve as building blocks for membrane expansion[1][7][8]. Given that autophagosomes must grow by incorporating millions of lipid molecules within minutes, the high-capacity lipid binding of ATG2 (approximately twenty lipids per molecule) represents a significant advantage over single-lipid-transfer proteins in achieving the necessary flux[9].

### Cooperation with Vps13 Proteins

Recent comprehensive studies revealed that the lipid transfer protein Vps13 cooperates with Atg2 at phagophore rims to ensure sufficient lipid delivery for autophagosome biogenesis[10]. Vps13 belongs to the same family of Chorein_N-domain proteins as Atg2 and localizes to the rims of approximately 90% of enlarged phagophores in wild-type cells[10]. Notably, Vps13 localization to forming autophagosomes does not require Atg2 or other core autophagy factors, suggesting parallel but independent recruitment of these two lipid transfer proteins[10].

The kinetic parameters revealed that Atg2-mediated phospholipid transfer (PLT) alone is not rate-limiting for autophagosome biogenesis[10]. Instead, the parallel action of Atg2 and Vps13 working at PERCS ensures sufficient lipid transfer rates to accommodate the rapid membrane expansion observed in living cells[10]. In the absence of Vps13, the number of Atg2 molecules at PERCS determines both the duration of autophagosome formation and the final size of forming autophagosomes, with an apparent *in vivo* transfer rate of approximately 200 phospholipids per Atg2 molecule per second[10].

## Mechanisms of Autophagosome Closure

### ATG2-GABARAP Interaction in Closure

Beyond its role in phagophore expansion through lipid transfer, Atg2 participates in a distinct process: the **closure or sealing** of the autophagosomal membrane[45][55]. The identification of a conserved LIR motif in ATG2A and ATG2B revealed direct interactions between ATG2 proteins and the Atg8/LC3/GABARAP family of autophagosomal proteins[55]. The ATG2A-GABARAP interaction appeared to function independently of the ATG2A-WIPI4 interaction required for lipid transfer[55].

In cells expressing ATG2A variants with mutations in the LIR motif (designated ATG2A-mLIR), the autophagy pathway exhibited severe defects in autophagosome closure despite retained ability to interact with WIPI4 and perform lipid transfer[55]. These mutant cells accumulated large numbers of unsealed, open autophagosomal structures containing Atg8/LC3 and other autophagy proteins but unable to form sealed compartments[55]. This separation-of-function analysis demonstrated that the ATG2-GABARAP interaction represents a mechanistically distinct closure pathway independent of lipid transfer activity[55].

### Molecular Mechanism of Closure

The precise molecular mechanism by which the ATG2-GABARAP interaction promotes autophagosome closure remains under investigation, but several possibilities have been proposed[45][55]. One hypothesis suggests that multimerization of the LC3/GABARAP proteins on the phagophore membrane, mediated through their interactions with Atg2, generates sufficient mechanical force or stabilization to promote membrane fusion and sealing[45][55]. The LC3/GABARAP proteins possess the ability to interact with both lipids and proteins, including other LC3/GABARAP molecules, suggesting capacity for forming higher-order assemblies[55].

Another possibility involves the spatial organization of membrane scission machinery at the site of the Atg2-GABARAP interaction[45]. The ESCRT complexes and other scission factors known to be required for autophagosome closure might be brought into proximity through interactions with ATG2 and its associated proteins[45].

## Biological Processes and Selective Autophagy

### Role in Bulk, Non-Selective Autophagy

*Schizosaccharomyces pombe* Atg2 is required for starvation-induced bulk autophagy, the non-selective degradation of cytoplasmic components in response to nutrient starvation[3][6][25]. During nitrogen starvation, Atg2-GFP rapidly accumulates at autophagosomal structures, and deletion of *atg2* severely impairs the autophagic response to nitrogen starvation[25].

### Role in Selective Organelle Autophagy

Beyond bulk autophagy, Atg2 is particularly important for **selective autophagy of organelles**, especially the autophagy of endoplasmic reticulum (ER) and mitochondrial compartments (termed ER-autophagy and mitophagy, respectively)[3][6]. Studies in fission yeast demonstrated that during nitrogen starvation, both ER-GFP and mitochondrial markers (mito-mCherry) are delivered into vacuoles in an Atg5-dependent manner, and this organelle autophagy is severely compromised in *atg20*, *atg24*, and related mutants[3]. While not all selective autophagy pathways show equivalent dependence on Atg2, the protein appears critical for efficient selective degradation of large organellar structures.

### Pexophagy and Peroxisome Degradation

In plant cells, Atg2 participates in **pexophagy**, the selective autophagy of peroxisomes[14][17]. Forward genetic screens in *Arabidopsis thaliana* identified *atg2* mutations as suppressors of *lon2* mutant phenotypes, with *lon2 atg2* double mutants displaying rescued peroxisomal morphology and function[14]. The LON2 protease catalyzes matrix protein turnover within peroxisomes, and when LON2 is absent, peroxisomes accumulate abnormal proteins and are targeted for pexophagic degradation through Atg2-dependent mechanisms[14][17].

Evidence suggests that hydrogen peroxide and oxidative stress signals peroxisomal dysfunction and trigger selective autophagic degradation through Atg2-dependent mechanisms[17]. The selective autophagy of peroxisomes represents a quality control mechanism maintaining functional peroxisomal populations and preventing accumulation of organelles with compromised redox balance[14][17].

## Evolutionary Conservation and Comparative Analysis

### Conservation Across Eukaryotic Kingdoms

The structure and function of Atg2 have proven remarkably conserved across eukaryotic organisms from simple yeasts to plants and animals. The budding yeast *Saccharomyces cerevisiae* Atg2 shares fundamental structural organization with *Schizosaccharomyces pombe* Atg2, mammalian ATG2A and ATG2B, and plant ATG2 proteins[1][7][9]. The core lipid transfer domain (Chorein_N) is particularly well-conserved, with structural studies demonstrating essentially identical architecture in yeast and mammalian proteins[1][8][9].

Mammalian cells express two ATG2 paralogs, ATG2A and ATG2B, that arose from gene duplication and show approximately 44.5% amino acid sequence identity to each other but only 15-16% identity to the budding yeast protein[33]. Despite these sequence divergences, the proteins maintain functional redundancy, with both being capable of rescue of autophagy defects in cells lacking either protein[33]. The dual redundancy of mammalian ATG2 proteins suggests that the lipid transfer and membrane tethering functions are sufficiently important to warrant multiple genetic copies in higher organisms[33].

### Chorein_N Domain Family

Atg2 belongs to a protein family united by their possession of the Chorein_N lipid transfer domain, which also includes the Vps13 family proteins (VPS13 in yeast and VPS13A, VPS13B, VPS13C, VPS13D in mammals)[12][31][34][56]. The N-terminal fragments of both Atg2 and Vps13 proteins sharing the Chorein_N domain show remarkable structural similarity despite low sequence conservation, with both folding into elongated molecules featuring large hydrophobic cavities[12][31][34][56]. The VPS13 proteins represent very large polypeptides (exceeding 3,000 amino acids in some cases) organized around repetitive β-groove (RBG) domains forming extended hydrophobic tunnels[56].

The shared architecture of the Chorein_N lipid transfer domain suggests that this represents an ancient lipid transfer module that was acquired early in eukaryotic evolution and subsequently deployed in multiple contexts involving membrane expansion and organellar biogenesis[12][31][34][56]. The discovery that both Atg2 and Vps13 function as high-capacity, bulk lipid transfer proteins distinguishes them from the previously characterized lipid transfer protein families, which typically transfer single lipids in a shuttle-like manner[12][31][34].

## Structural Models of Lipid Transfer Mechanism

### Bridge Model

The **bridge model** proposes that Atg2 stably tethers the phagophore and ER membranes through simultaneous binding of both membrane-binding tips, while lipids translocate through the internal cavity extending from one tip to the other[54]. In this model, lipids occupy the hydrophobic cavity and travel along the extended hydrophobic groove as if sliding through a tunnel, with their acyl chains remaining buried in the hydrophobic microenvironment while their polar head groups remain exposed to the cytosolic solution[1][50][54]. This mechanism would position Atg2 as a stable bridge mediating lipid transfer without requiring the protein itself to shuttle between membranes[54].

### Ferry Model

An alternative **ferry model** suggests that the N-terminal lipid transfer domain of Atg2 can function independently as a lipid shuttle, with the N-terminal fragment cycling between the ER and phagophore while the C-terminal regions anchor the complex to the phagophore through WIPI interactions[54]. This model is supported by observations that N-terminal fragments of ATG2A comprising only amino acids 1-345 can mediate lipid transfer *in vitro* and fully rescue autophagy defects in cells[9][36]. In the ferry model, the anchored C-terminal regions hold the complex at the contact site while the N-terminal lipid transfer domain dynamically interacts with both membranes[54].

Recent evidence suggests that both models may operate: a stable bridge architecture for efficient bulk lipid transfer combined with dynamic shuttling of the N-terminal domain to extract lipids from the ER and insert them into the phagophore[54].

### Hydrophobic Groove as Lipid Pathway

The structural evidence supports a model in which the continuous hydrophobic cavity or groove extending through the Atg2 rod acts as a dedicated pathway for lipid translocation[1][50]. The Chorein_N N-terminal domain, the five internal repeats, and the ATG2_CAD region collectively form this pathway, with lipid acyl chains sliding along the hydrophobic walls while the polar head groups remain solvated[1][50]. This contrasts with vesicular trafficking, where lipids would be packaged into membrane-enclosed compartments for transport, instead representing direct intermembrane transfer through a protein-mediated channel[1][50].

## Recent Discoveries and Emerging Model of Autophagosome Biogenesis

### Integration with Atg9 Scramblase Function

One of the most significant recent advances involved recognizing that Atg2 lipid transfer activity must be coupled with Atg9 lipid scramblase activity for effective autophagosome expansion[10][20][23][39]. While Atg2 can transfer lipids from the ER to the phagophore, it primarily inserts them into the outer leaflet of the phagophore membrane[20]. This would create severe lipid asymmetry incompatible with the bilayer geometry required for membrane expansion[20]. Atg9, which possesses lipid scramblase activity allowing energy-independent lipid flipping between membrane leaflets, solves this problem by equilibrating lipid distribution[20][23][39].

The physical interaction between Atg2 and Atg9 at the phagophore rim creates a minimal system for coordinated lipid transfer and scrambling[10][20][23][39]. Cryo-EM structural models suggest that the opening of Atg2's hydrophobic groove aligns with the internal channel of the Atg9 trimeric complex, allowing direct hand-off of lipids[39]. This coupling ensures that as Atg2 delivers lipids to the outer leaflet, Atg9 simultaneously equilibrates them between leaflets, preventing the osmotic stress and membrane disruption that would result from excessive outer leaflet expansion[20][39].

### TRAPPIII Complex Coordination

Recent studies in yeast revealed that the TRAPPIII tethering complex participates in establishing and organizing the phagophore-ER membrane contact sites where Atg2 operates[13]. TRAPPIII is a guanine nucleotide exchange factor (GEF) that activates the small GTPase Ypt1, and its recruitment to PERCS by interaction with Atg9 and other factors organizes the tethering machinery[13]. The interaction between TRAPPIII and Atg2 appears cooperative, with both complexes working to maintain the appropriate spacing and organization of phagophore-ER contact sites[13].

### Non-Rate-Limiting Nature of Atg2 Activity

A surprising finding emerging from quantitative live-cell imaging studies is that Atg2-mediated lipid transfer is **not rate-limiting** for autophagosome biogenesis in wild-type cells[10]. Instead, the parallel action of multiple lipid transfer proteins including Vps13 ensures that sufficient phospholipid delivery occurs to support the observed rates of autophagosome expansion[10]. The number of Atg2 molecules at individual phagophores correlates with the final size of the forming autophagosome, suggesting that Atg2 abundance becomes rate-limiting only in specialized circumstances or in the absence of other lipid transfer proteins[10].

## Biological Significance and Disease Implications

### Essential Role in Cellular Homeostasis

The essential requirement for Atg2 in autophagosome formation makes this protein critical for cellular homeostasis. Autophagy participates in degradation of damaged organelles, misfolded proteins, and pathogens, processes necessary for cellular health and survival during nutrient stress[1][7][8]. The inability to complete autophagosome formation in *atg2* mutants results in accumulation of autophagic cargo and defective clearance of damaged cellular components[1][33].

### Senescence and Cell Death

In plant cells, disruption of Atg2 function through mutagenesis results in **accelerated senescence**, exhibiting phenotypes characteristic of premature aging including accumulation of cellular damage and oxidative stress[44]. The silencing of *GmATG2* in soybean results in high levels of ubiquitinated protein accumulation and enhanced accumulation of polyubiquitinated protein aggregates, indicating that impaired autophagy leads to proteostasis failure[44]. These findings suggest that maintaining functional Atg2-mediated autophagy is essential for long-term cellular viability and the prevention of age-associated pathologies.

### Pathogenic Potential and Cancer Biology

Recent investigations have noted that ATG9B, a less well-characterized mammalian homolog that can functionally cooperate with ATG2A, has been implicated in tumorigenesis, particularly in hepatocellular carcinoma development[23]. While detailed mechanisms remain to be elucidated, the connection between autophagy dysfunction and cancer suggests that alterations in Atg2/ATG2 functions could contribute to malignant transformation[23].

## Comparative Analysis with Budding Yeast and Mammals

### Fission Yeast Specific Features

*Schizosaccharomyces pombe* Atg2 exhibits several features that distinguish it from better-characterized mammalian and budding yeast proteins. The fission yeast autophagy machinery shows important differences in the composition and organization of the Atg1 complex, with fission yeast requiring Atg11 for starvation-induced bulk autophagy, whereas budding yeast Atg11 is dispensable for this process[25]. These organismal differences suggest that the role and regulation of Atg2 may be somewhat specialized in fission yeast, though the core lipid transfer function is conserved.

### Mammalian Complexity and Redundancy

Mammals express both ATG2A and ATG2B, with these proteins showing redundant but also potentially specialized functions[33][39]. Both proteins can independently support autophagy, but combined deletion is required to completely block autophagy, indicating functional overlap[33]. The existence of two ATG2 paralogs in mammals potentially allows tissue-specific or temporally-regulated autophagy responses through selective expression of each isoform[33][39].

## Remaining Questions and Future Research Directions

### Open Questions Regarding Lipid Transfer Kinetics

Despite recent advances, several fundamental questions remain regarding the quantitative aspects of Atg2-mediated lipid transfer in living cells[54]. While *in vitro* lipid transfer rates have been measured, integrating these values with the known timecourse of autophagosome expansion and the total lipid content suggests that either additional mechanisms accelerate transfer, other lipid transfer proteins make essential contributions (as demonstrated for Vps13), or the *in vitro* assay conditions differ significantly from the cellular environment in ways that affect transfer rates[10][54].

### Mechanistic Basis of Lipid Selectivity

The substrate selectivity of Atg2 and whether different lipid species are transferred at differential rates remains an area for investigation[54]. While bulk lipid transfer is a primary function of the Chorein_N proteins, whether specific lipid compositions or species are preferentially transferred to support particular aspects of autophagosome formation (such as maintaining specific phosphoinositide distributions or enriching particular lipid species) requires further study[54].

### Structural Details of Full-Length Protein

Although the N-terminal lipid transfer domain and other regions of Atg2 have been structurally characterized, the complete three-dimensional structure of full-length Atg2 remains to be determined at atomic resolution[1][7][50]. The organization and connectivity of the five internal repeat domains, their precise role in forming the continuous hydrophobic cavity, and how these regions interact with binding partners remain subjects for future structural investigations[1][7].

## Conclusion

Autophagy-related protein 2 (Atg2) in *Schizosaccharomyces pombe* represents a remarkable example of how molecular characterization of conserved cellular machinery continues to reveal previously unsuspected mechanisms of cellular organization and membrane biology[1][7]. What was once recognized simply as an essential but enigmatic protein required for autophagosome formation has emerged as a sophisticated, multifunctional molecular device mediating both stable membrane tethering and high-capacity lipid transfer between organellar compartments[1][7][8]. The discovery that Atg2 functions as a lipid transfer protein has revolutionized our understanding of de novo autophagosome formation, providing a molecular mechanism for how cells can rapidly construct new membrane compartments through direct intermembrane lipid transport rather than relying exclusively on vesicular trafficking[1][7][8][9].

The structure of the rod-shaped Atg2 molecule with its two membrane-binding tips and extensive hydrophobic cavity has proven ideally suited to serve as a bridge simultaneously tethering the ER and phagophore while channeling lipids between these membrane systems[1][7][8]. The biochemical capacity of individual Atg2 molecules to bind and transfer approximately twenty lipid molecules at a time, combined with the parallel action of related lipid transfer proteins such as Vps13, provides sufficient phospholipid flux to support the documented rates of autophagosome expansion observed in living cells[9][10].

The recognition that Atg2 participates in both phagophore expansion through lipid transfer and in autophagosome closure through distinct interactions with GABARAP proteins has unveiled the sequential, mechanistically distinct steps of autophagosome biogenesis[45][55]. The physical coupling of Atg2 lipid transfer activity with Atg9 lipid scramblase function has provided insights into how cells manage the complex challenge of generating the vast asymmetric lipid bilayers characteristic of autophagosomes[10][20][23][39].

The evolutionary conservation of Atg2 function across eukaryotes from simple yeasts to plants and animals, combined with the shared architecture of the Chorein_N lipid transfer domain found in Vps13 and other proteins, suggests that this represents a fundamental mechanism of eukaryotic membrane biology. The participation of Atg2 in not only bulk autophagy but also selective autophagy of organelles such as mitochondria, ER, and peroxisomes indicates that this protein's lipid transfer function addresses a general cellular requirement for rapid membrane expansion during diverse biological processes[1][3][6][14][17].

Future investigations into the atomic-resolution structure of full-length Atg2, the molecular details of lipid selectivity, and the quantitative kinetics of lipid transfer in cellular contexts promise to further illuminate this essential aspect of eukaryotic cell biology. The continued characterization of Atg2 and related lipid transfer proteins contributes not only to fundamental understanding of autophagy and cellular homeostasis but also holds potential for therapeutic applications targeting autophagy dysregulation in diseases ranging from neurodegeneration to cancer.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC6511744/
2. https://www.uniprot.org/citations/16303567
3. https://journals.biologists.com/jcs/article/129/22/4289/55695/Atg20-and-Atg24-family-proteins-promote-organelle
4. https://www.uniprot.org/uniprotkb/O94649/entry
5. https://string-db.org/network/284812.Q96VG1
6. https://pubmed.ncbi.nlm.nih.gov/27737912/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC6625793/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC6548141/
9. https://rupress.org/jcb/article/222/7/e202211039/214069/Parallel-phospholipid-transfer-by-Vps13-and-Atg2
10. https://www.pnas.org/doi/10.1073/pnas.1811874115
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC7885529/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC12618252/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC3877801/
14. https://www.molbiolcell.org/doi/10.1091/mbc.E25-06-0273
15. https://journals.sagepub.com/doi/10.1177/25152564231183898
16. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2014.00139/full
17. https://pubmed.ncbi.nlm.nih.gov/41563375/?fc=None&ff=20260121191715&v=2.18.0.post22+67771e2
18. https://pubmed.ncbi.nlm.nih.gov/19200887/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC7718406/
20. https://www.pombase.org/gene/SPBC31E1.01c
21. http://reactome.org/content/detail/R-HSA-5676229
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC10936676/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC8997447/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC11073433/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC5712628/
26. https://www.uniprot.org/uniprotkb/O42651/entry
27. https://www.semanticscholar.org/paper/The-crystal-structure-of-Atg18-reveals-a-new-site-Lei-Tang/d5711eb98b0310b56874e3719861d74040718c1b
28. https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14741
29. https://pubmed.ncbi.nlm.nih.gov/34783437/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC1805099/
31. https://www.molbiolcell.org/doi/abs/10.1091/mbc.e11-09-0785
32. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.16280
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC4590589/
34. https://rupress.org/jcb/article/218/6/1787/61839/ATG2-transports-lipids-to-promote-autophagosome
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC3442503/
36. https://pubmed.ncbi.nlm.nih.gov/36347259/
37. https://elifesciences.org/articles/45777
38. https://www.yeastgenome.org/locus/S000005186
39. https://pdbj.org/emnavi/quick.php?id=emdb-15604
40. https://pombase.org/gene/SPBC31E1.01c
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC8584260/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC8616111/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC3362037/
44. https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14720
45. https://pubmed.ncbi.nlm.nih.gov/29113029/
46. https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.12901
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC6844533/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC7054675/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC10683392/
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC7681076/
51. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2020.00565/full
52. https://journals.sagepub.com/doi/abs/10.1177/25152564231211976
53. https://onlinelibrary.wiley.com/doi/10.1111/cas.15112