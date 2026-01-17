---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T13:25:24.127211'
end_time: '2026-01-15T13:39:48.469740'
duration_seconds: 864.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ACTB
  gene_symbol: ACTB
  uniprot_accession: P60709
  protein_description: 'RecName: Full=Actin, cytoplasmic 1; EC=3.6.4.- {ECO:0000250|UniProtKB:P68137};
    AltName: Full=Beta-actin; Contains: RecName: Full=Actin, cytoplasmic 1, N-terminally
    processed;'
  gene_info: Name=ACTB;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the actin family. .
  protein_domains: Actin. (IPR004000); Actin/actin-like_CS. (IPR020902); Actin_CS.
    (IPR004001); ATPase_NBD. (IPR043129); Actin (PF00022)
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
- **UniProt Accession:** P60709
- **Protein Description:** RecName: Full=Actin, cytoplasmic 1; EC=3.6.4.- {ECO:0000250|UniProtKB:P68137}; AltName: Full=Beta-actin; Contains: RecName: Full=Actin, cytoplasmic 1, N-terminally processed;
- **Gene Information:** Name=ACTB;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the actin family. .
- **Key Domains:** Actin. (IPR004000); Actin/actin-like_CS. (IPR020902); Actin_CS. (IPR004001); ATPase_NBD. (IPR043129); Actin (PF00022)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ACTB" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ACTB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ACTB** (gene ID: ACTB, UniProt: P60709) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ACTB (Beta-Actin): Comprehensive Functional Annotation Report

## Introduction and Overview

Beta-actin (ACTB, UniProt: P60709) is one of the most abundant and evolutionarily conserved proteins in eukaryotic cells, serving as a fundamental building block of the cytoskeleton and participating in an remarkably diverse array of cellular processes[pollard-2016-actin-abps-abstract]. Encoded by the ACTB gene on human chromosome 7p22, beta-actin belongs to the actin protein family and is classified as a non-muscle cytoplasmic actin, distinguishing it from the four muscle-specific alpha-actins. Together with gamma-actin (encoded by ACTG1), beta-actin constitutes the cytoplasmic actin pool found in virtually all eukaryotic cell types[dominguez-2011-actin-structure-function-abstract].

Despite differing by only four biochemically similar amino acids near their N-termini, beta-actin and gamma-actin have evolved under strong selective pressure to maintain these small sequence differences, suggesting distinct functional roles for each isoform[patrinostro-2018-actb-essential-abstract]. The primary molecular function of beta-actin involves its ATP-dependent polymerization into filaments (F-actin) that provide structural support, generate mechanical forces, and serve as tracks for myosin motor proteins. However, beta-actin's functions extend far beyond the cytoskeleton, encompassing roles in nuclear transcription, chromatin remodeling, and signal transduction pathways[olave-2002-nuclear-actin-chromatin-abstract].

## Molecular Structure and Biochemistry

### Monomer Structure

The beta-actin monomer comprises 375 amino acids organized into four subdomains that form two major structural domains, fitting into a rectangular prism with dimensions of approximately 55 Å × 55 Å × 35 Å[dominguez-2011-actin-structure-function-abstract]. The protein contains two critical clefts between its domains: the nucleotide-binding cleft, which accommodates ATP or ADP, and the hydrophobic cleft (also termed the target-binding cleft), which constitutes the major binding site for most actin-binding proteins. This architectural arrangement allows actin to interact with dozens of regulatory proteins while maintaining its capacity for nucleotide-dependent polymerization[pollard-2016-actin-abps-abstract].

The high degree of conservation in actin structure across eukaryotes reflects the stringent functional constraints imposed by its interactions with numerous binding partners. Structural studies have revealed that actin monomers (G-actin) adopt a relatively "twisted" conformation, while incorporation into filaments induces a characteristic "flattening" involving a 12-13 degree propeller-like rotation of the outer domain relative to the inner domain[dominguez-2011-actin-structure-function-abstract].

### ATP Binding and Hydrolysis

Beta-actin functions as an ATPase (EC 3.6.4.-), though its enzymatic activity is intimately coupled to polymerization. ATP-bound G-actin preferentially assembles onto the barbed (plus) end of actin filaments, and polymerization dramatically accelerates the rate of ATP hydrolysis by approximately 40,000-fold compared to monomeric actin[korn-1987-actin-atp-hydrolysis-abstract]. This rate enhancement occurs because filament incorporation repositions the side chains of Gln137 and His161 within the active site, facilitating nucleophilic attack on the gamma-phosphate by an activated water molecule.

The hydrolysis reaction proceeds in two distinct steps: first, ATP is cleaved to ADP and inorganic phosphate (Pi), yielding a highly stable ADP·Pi-bound filament; second, the slower release of Pi destabilizes the filament and promotes depolymerization[korn-1987-actin-atp-hydrolysis-abstract]. This biphasic mechanism creates regulatory opportunities, as a transient "cap" of ATP-actin subunits exists at the rapidly growing barbed ends, while an ADP·Pi cap provides stabilization at steady state. The subsequent dissociation of phosphate marks subunits for preferential disassembly, particularly from the pointed (minus) end of filaments[pollard-2016-actin-abps-abstract].

## Actin Polymerization Dynamics and Treadmilling

### Filament Assembly

Actin filaments adopt a right-handed helical structure with 13 molecules repeating every six turns over a distance of 35.9 nm, generating filaments approximately 7 nm in diameter[dominguez-2011-actin-structure-function-abstract]. The inherent polarity of actin filaments—with structurally and kinetically distinct barbed and pointed ends—underlies the phenomenon of "treadmilling," whereby net assembly occurs at the barbed end while net disassembly occurs at the pointed end under steady-state conditions. This ATP-powered directional flux of subunits through filaments enables cells to generate pushing forces and reorganize their cytoskeleton without changing total filament length[korn-1987-actin-atp-hydrolysis-abstract].

The kinetic differences between filament ends are substantial: polymerization and depolymerization rates at the pointed end are much slower than at the barbed end, explaining why cells exploit the barbed end for rapid, regulated polymerization during processes such as cell motility and membrane protrusion[pollard-2017-actin-cytoskeleton-motility-abstract]. Recent cryo-electron microscopy studies have revealed that terminal subunits at the free barbed end adopt a "flat" F-actin conformation, while subunits at the free pointed end retain a "twisted" G-actin-like conformation, providing a structural basis for these kinetic asymmetries.

### Rho GTPase Signaling and Actin Regulation

The assembly and organization of actin filaments in response to extracellular signals is controlled by the Rho family of small GTPases, principally RhoA, Rac1, and Cdc42[tapon-1997-rho-rac-cdc42-abstract]. These signaling proteins act as molecular switches, cycling between inactive GDP-bound and active GTP-bound states, and each promotes distinct actin-based structures. RhoA controls the assembly of contractile actin stress fibers and focal adhesion complexes, Rac1 regulates actin accumulation at the plasma membrane to produce lamellipodia and membrane ruffles, and Cdc42 stimulates the formation of filopodia[tapon-1997-rho-rac-cdc42-abstract]. The coordination of these GTPases during cell migration is spatiotemporally precise: RhoA is activated at the cell edge synchronous with edge advancement, while Cdc42 and Rac1 are activated slightly behind the leading edge with a brief temporal delay.

The downstream effectors of Rho GTPases include WASP/WAVE family proteins, which activate the Arp2/3 complex to nucleate branched actin networks, and formins, which promote linear filament elongation. Activated Cdc42 and Rac1 bind to the CRIB (Cdc42/Rac interactive binding) motif within WASP and N-WASP, releasing these proteins from an autoinhibited conformation and enabling them to activate Arp2/3[tapon-1997-rho-rac-cdc42-abstract]. RhoA additionally regulates myosin light chain phosphatase and controls the synthesis of phosphatidylinositol 4,5-bisphosphate (PI(4,5)P2), a lipid second messenger that modulates the activity of numerous actin-binding proteins including profilin and cofilin.

### Regulation by Actin-Binding Proteins

The dynamic behavior of actin filaments in cells is orchestrated by a diverse array of actin-binding proteins that regulate virtually every aspect of the polymerization cycle[pollard-2016-actin-abps-abstract]. Profilin catalyzes nucleotide exchange on G-actin monomers, effectively recharging ADP-actin with ATP to prepare it for another round of polymerization. The Arp2/3 complex nucleates branched filament networks that are characteristic of lamellipodia, while formins and Ena/VASP proteins promote processive elongation at barbed ends. Capping proteins terminate filament growth by blocking barbed ends, and cofilin/ADF promotes filament disassembly by severing ADP-actin regions and enhancing pointed-end depolymerization.

Particularly relevant to beta-actin function is the observation that beta-actin, compared to gamma-actin, maintains a higher proportion of monomeric actin (G-actin) in cells[shubhan-2011-betaactin-growth-migration-abstract]. This G-actin pool is not merely a reserve for polymerization but actively participates in gene regulation through the serum response factor (SRF) pathway, as monomeric actin sequesters the SRF coactivator MAL (also known as MRTF-A) in the cytoplasm.

## Subcellular Localization and Cytoplasmic Functions

### Cell Motility and the Leading Edge

Beta-actin plays an essential role in cell motility, particularly at the leading edge of migrating cells where it concentrates in lamellipodia—thin, sheet-like protrusions driven by actin polymerization[pollard-2017-actin-cytoskeleton-motility-abstract]. The lamellipodium represents both the motor for cell advancement and the primary site of actin cytoskeleton construction, containing a dense network of branched actin filaments arranged with their barbed ends facing the membrane. Genetic studies have demonstrated that beta-actin knockout cells exhibit severely impaired migration velocity and reduced membrane protrusion dynamics[shubhan-2011-betaactin-growth-migration-abstract].

The specific enrichment of beta-actin at the leading edge is achieved through a remarkable post-transcriptional mechanism involving localization of beta-actin mRNA[singer-2001-beta-actin-mrna-localization-abstract]. A 54-nucleotide cis-acting element in the 3'-untranslated region of beta-actin mRNA, termed the "zipcode," directs transcript localization to the cell periphery. The zipcode is recognized by zipcode-binding protein 1 (ZBP1), which binds the mRNA in the nucleus and maintains it in a translationally repressed state during cytoplasmic transport[chua-2009-zbp1-mrna-localization-abstract]. Local translation of beta-actin mRNA at the leading edge ensures that newly synthesized protein is immediately available for incorporation into growing filaments, thereby spatially coupling protein synthesis to actin polymerization.

Disruption of beta-actin mRNA localization does not affect overall migration velocity but profoundly impairs directional persistence[singer-2001-beta-actin-mrna-localization-abstract]. This observation reveals that spatial control of beta-actin synthesis, rather than simply protein abundance, establishes cellular polarity and enables directional migration. The delocalization of beta-actin mRNA results in the dispersal of actin nucleation sites around the cell periphery rather than their concentration at the leading edge, leading to randomized protrusive activity and loss of persistent directionality.

### Cell Division and Cytokinesis

Beta-actin is enriched at the contractile ring during cell division, where it participates in the physical process of cytokinesis[shubhan-2011-betaactin-growth-migration-abstract]. Because beta-actin is more dynamic than gamma-actin, it may be specifically required for the rapid reorganization of the actin cytoskeleton during cell division. Consistent with this idea, beta-actin knockout cells exhibit increased frequencies of multinucleated cells and higher rates of apoptosis, suggesting defects in completing cytokinesis[shubhan-2011-betaactin-growth-migration-abstract]. The essential nature of beta-actin for cell division is underscored by the embryonic lethality of homozygous Actb knockout mice, which die before embryonic day 8.5.

## Nuclear Actin Functions

### Transcriptional Regulation

Beyond its cytoplasmic roles, significant amounts of beta-actin are present in the nucleus, where it participates in transcription by all three RNA polymerases[olave-2002-nuclear-actin-chromatin-abstract]. Nuclear actin facilitates pre-initiation complex assembly and transcription elongation, associating with the elongating RNA polymerase II complex through interactions with heterogeneous nuclear ribonucleoproteins (hnRNPs). The nuclear concentration of actin is regulated by dedicated import and export machinery, with IMPORTIN9 mediating nuclear entry and EXPORTIN6 driving nuclear exit. High nuclear actin levels generally correlate with elevated transcriptional activity.

### Chromatin Remodeling Complexes

One of the most significant discoveries regarding nuclear actin function was the identification of beta-actin as an integral component of mammalian SWI/SNF-like BAF chromatin remodeling complexes[olave-2002-nuclear-actin-chromatin-abstract]. The BAF complex is an ATP-dependent chromatin remodeler that regulates gene expression by repositioning nucleosomes and controlling chromatin accessibility. BRG1, the catalytic ATPase subunit of BAF, requires beta-actin for maximal ATPase activity, indicating that actin plays a direct role in the chromatin remodeling mechanism rather than serving merely as a structural component.

Beta-actin is also found in other chromatin remodeling complexes, including INO80 and TIP60, where it contributes to complex stability and function. Recent studies have demonstrated that loss of nuclear beta-actin induces compartment-level changes in three-dimensional genome architecture by altering the balance between BAF and Polycomb repressive complexes (PRCs)[tori-2021-betaactin-3d-genome-abstract]. This finding suggests that beta-actin acts as a regulator of epigenetic states and may influence cell fate decisions during development and in disease contexts such as cancer.

## Post-Translational Modifications

### Histidine Methylation at His73

One of the most extensively studied post-translational modifications of beta-actin is methylation of histidine 73 (His73), a modification known for over 50 years but whose enzymatic basis remained elusive until recently[wilkinson-2018-setd3-histidine-abstract]. SETD3 was identified as the physiological actin histidine methyltransferase responsible for this modification. Structural studies revealed that SETD3 recognizes and positions His73 within its catalytic pocket through an extensive network of protein-peptide interactions.

His73 methylation has functional consequences for actin behavior: it reduces the rate of nucleotide exchange on G-actin monomers and modestly accelerates filament assembly[wilkinson-2018-setd3-histidine-abstract]. The physiological importance of this modification was dramatically demonstrated by the phenotype of SETD3-knockout mice, in which females exhibit severely decreased litter sizes due to primary maternal dystocia—failure of uterine contractions during labor that is refractory to oxytocin induction. This phenotype reveals an essential role for actin His73 methylation in smooth muscle contractility.

### N-Terminal Modifications and Isoform-Specific Processing

The N-terminus of beta-actin undergoes competing modifications that influence filament dynamics and cell behavior[grazova-2018-actin-ptm-cinderella-abstract]. Beta-actin and gamma-actin differ by four amino acids at their N-termini: beta-actin contains Asp(1)-Asp(2)-Asp(3) and Val(10), whereas gamma-actin has Glu(1)-Glu(2)-Glu(3) and Ile(10)[vanri-2022-nterminal-processing-abstract]. These seemingly conservative substitutions have significant functional consequences, as beta-actin—but not gamma-actin—undergoes sequential removal of N-terminal aspartate residues, leading to truncated actin species that constitute approximately 1-3% of intracellular beta-actin.

The enzymes responsible for this N-terminal processing have been identified as ENPEP (glutamyl aminopeptidase) and DNPEP (aspartyl aminopeptidase)[vanri-2022-nterminal-processing-abstract]. CRISPR-mediated deletion of these enzymes abolishes most beta-actin N-terminal processing and results in measurable changes in F-actin levels, cell spreading, filopodia formation, and cell migration rates. This differential processing provides a biochemical mechanism for distinguishing between the two cytoplasmic actin isoforms and may contribute to their distinct subcellular localizations: gamma-actin predominantly localizes to the apical cortex and forms stiffer networks, while beta-actin is preferentially organized in stress fibers and at the leading edge[vanri-2022-nterminal-processing-abstract].

After removal of the initiator methionine, beta-actin can be either N-terminally acetylated by NAA80 or arginylated by arginyltransferase (ATE1). N-terminal arginylation is selective for beta-actin and does not occur on gamma-actin, representing the only known post-translational modification that distinguishes these highly similar isoforms[grazova-2018-actin-ptm-cinderella-abstract]. Arginylated beta-actin specifically relocates to the leading edge upon induction of cell migration, suggesting a role in establishing or maintaining cellular polarity. Although less than 1% of total cellular beta-actin is arginylated, local concentrations at sites of active migration may be substantially higher. Arginylated actin exhibits reduced polymerization rates compared to acetylated actin, particularly in formin-mediated elongation and Arp2/3-mediated nucleation, suggesting that this modification fine-tunes actin dynamics at specific subcellular locations.

### Lysine Methylation and Oxidation

Monomethylation of lysine 84 (K84me1) regulates the interaction between actin and myosin, affecting actomyosin-dependent processes. Demethylation of K84 by ALKBH4 is required for proper cleavage furrow ingression during cytokinesis and for normal cell migration. Additionally, actin can be regulated through oxidation of methionine residues (Met44 and Met47) by MICAL oxidases, which generate methionine sulfoxide and promote filament depolymerization. This oxidation is reversed by methionine sulfoxide reductases (MSRBs), which reduce the modification and enable actin repolymerization. This redox-dependent regulation provides a mechanism for coupling actin dynamics to cellular oxidative states.

## Interaction with Myosin and Force Generation

Beta-actin serves as the track for myosin motor proteins, which use ATP hydrolysis to generate force and movement along actin filaments[huxley-1954-sliding-filament-summary]. This interaction underlies muscle contraction, cytokinesis, and numerous other cellular processes requiring mechanical force. The sliding filament model, proposed independently by Huxley and Niedergerke and by Huxley and Hanson in 1954, established that muscle contraction results from the sliding of actin thin filaments past myosin thick filaments, powered by cyclic interactions between myosin heads and actin.

In striated muscle, the actin-myosin interaction is regulated by calcium-dependent binding of troponin to tropomyosin, which controls access of myosin heads to actin-binding sites. In non-muscle cells, cytoplasmic beta-actin interacts primarily with non-muscle myosin II (NMII), generating contractile forces that drive cell shape changes, adhesion dynamics, and migration. The proper regulation of these actomyosin interactions depends on the post-translational modification state of actin, as exemplified by the requirement for His73 methylation in smooth muscle contraction[wilkinson-2018-setd3-histidine-abstract].

## Disease Associations and Clinical Significance

### Baraitser-Winter Syndrome

De novo missense mutations in ACTB cause Baraitser-Winter syndrome type 1 (BRWS1), a developmental disorder characterized by distinct craniofacial features, ocular colobomata, and neuronal migration defects including pachygyria[riviere-2012-baraitser-winter-abstract]. The identification of ACTB mutations in this syndrome provided direct genetic evidence for actin's essential role in human neurodevelopment and demonstrated that even subtle amino acid substitutions in this highly conserved protein can have profound phenotypic consequences.

Baraitser-Winter syndrome type 2 is caused by mutations in ACTG1 (gamma-actin), and remarkably, mutations in either gene produce an indistinguishable clinical phenotype[riviere-2012-baraitser-winter-abstract]. This observation suggests that BRWS-causing mutations affect developmental functions shared by both cytoplasmic actins, likely involving their common roles in cell migration and morphogenesis. Additional features of BRWS include hearing loss, intellectual disability, seizures, and short stature, with ACTB mutations generally associated with more severe phenotypes than ACTG1 mutations.

### Hearing Loss

Both ACTB and ACTG1 are highly expressed in the stereocilia of auditory hair cells, where they form the structural core of these mechanosensory organelles. Studies in mice have demonstrated that beta-actin has an irreplaceable role in auditory function: mice engineered to express gamma-actin from the Actb locus develop progressive hearing loss due to inappropriate shortening of stereocilia[patrinostro-2018-actb-essential-abstract]. This phenotype reveals that despite their near-identical sequences, beta-actin and gamma-actin have non-redundant functions in specialized cell types.

Mutations in ACTG1 cause autosomal dominant progressive nonsyndromic hearing loss (DFNA20/26), and hearing impairment is also common in Baraitser-Winter syndrome patients with either ACTB or ACTG1 mutations. The mechanistic basis for these auditory phenotypes likely involves the critical role of cytoplasmic actins in stereocilia elongation and maintenance, processes that require precise regulation of actin filament dynamics.

### Cancer and Metastasis

Although traditionally regarded as a housekeeping gene, accumulating evidence indicates that ACTB is abnormally expressed in multiple cancers and plays active roles in tumor progression[chen-2021-actb-pancancer-abstract]. ACTB is up-regulated in the majority of tumor cells and tissues, and significant increases in beta-actin expression levels have been observed in highly invasive variants of several different tumor cell lines. Pan-cancer analyses have revealed that high ACTB expression correlates with poorer prognosis in multiple tumor types, including glioblastoma (GBM), head and neck squamous cell carcinoma (HNSC), kidney renal clear cell carcinoma (KIRC), lower grade glioma (LGG), liver hepatocellular carcinoma (LIHC), lung adenocarcinoma (LUAD), mesothelioma (MESO), skin cutaneous melanoma (SKCM), and uveal melanoma (UVM)[chen-2021-actb-pancancer-abstract].

The mechanistic basis for beta-actin's role in cancer involves its essential function in cell migration and invasion, processes that are co-opted during metastasis. Cell migration is commonly driven by actin polymerization at the leading edge, which provides the protrusive forces that push the membrane forward. ACTB deregulation affects the polymerization of actin at the leading edge in tumor cells, potentially accelerating tumor formation, invasion, and metastasis[chen-2021-actb-pancancer-abstract]. Inhibition of Rho family small GTPase signaling, which controls actin cytoskeleton reorganization, has been shown to suppress the migration and invasion of cancer cells, highlighting the actin cytoskeleton as a potential therapeutic target. Knockdown of ACTB in head and neck squamous carcinoma cells inhibited migration and invasion through effects on NF-κB and Wnt/β-catenin signaling pathways. These findings suggest that while beta-actin has traditionally been used as a normalization control in molecular studies, its expression is neither constant nor neutral in the context of malignancy.

## Open Questions

Despite extensive characterization, several fundamental questions about beta-actin biology remain unresolved. The precise mechanisms by which cells distinguish between beta-actin and gamma-actin during specific cellular processes are incompletely understood, particularly given their near-identical protein sequences. The four amino acid differences between these isoforms are confined to the N-terminus, yet they confer distinct functional properties and differential post-translational modification patterns that remain to be fully elucidated.

The role of nuclear actin in chromatin organization and gene regulation continues to be an active area of investigation. While beta-actin's incorporation into BAF and other chromatin remodeling complexes is well established, the mechanisms by which changes in nuclear actin affect three-dimensional genome architecture and how these changes translate into altered gene expression programs require further study. The interplay between nuclear actin and Polycomb repressive complexes in determining chromatin states represents a particularly intriguing area for future research.

The contribution of beta-actin post-translational modifications to human disease remains largely unexplored. Given the essential role of His73 methylation in smooth muscle function, it would be valuable to determine whether SETD3 dysfunction contributes to labor complications or other smooth muscle disorders in humans. Similarly, the potential involvement of aberrant actin arginylation or oxidation in cancer cell migration and metastasis warrants investigation.

Finally, the development of therapeutic strategies targeting actin dynamics remains challenging due to the essential and ubiquitous nature of actin functions. Understanding the isoform-specific and modification-specific roles of beta-actin may reveal opportunities for more selective interventions in diseases characterized by actin dysfunction.

## References

1. **pollard-2016-actin-abps-abstract**: Pollard TD. Actin and Actin-Binding Proteins. *Cold Spring Harb Perspect Biol.* 2016;8(8):a018226. DOI: 10.1101/cshperspect.a018226. PMID: 26988969. https://pubmed.ncbi.nlm.nih.gov/26988969/

2. **korn-1987-actin-atp-hydrolysis-abstract**: Korn ED, Carlier MF, Pantaloni D. Actin polymerization and ATP hydrolysis. *Science.* 1987;238(4827):638-44. DOI: 10.1126/science.3672117. PMID: 3672117. https://pubmed.ncbi.nlm.nih.gov/3672117/

3. **dominguez-2011-actin-structure-function-abstract**: Dominguez R, Holmes KC. Actin Structure and Function. *Annu Rev Biophys.* 2011;40:169-186. DOI: 10.1146/annurev-biophys-042910-155359. PMID: 21314430. https://pmc.ncbi.nlm.nih.gov/articles/PMC3130349/

4. **patrinostro-2018-actb-essential-abstract**: Patrinostro X, Roy P, Lindsay A, et al. Essential nucleotide- and protein-dependent functions of Actb/β-actin. *Proc Natl Acad Sci USA.* 2018;115(31):7973-7978. DOI: 10.1073/pnas.1807895115. PMID: 30012616. https://pmc.ncbi.nlm.nih.gov/articles/PMC6077724/

5. **shubhan-2011-betaactin-growth-migration-abstract**: Shemesh T, et al. β-Actin specifically controls cell growth, migration, and the G-actin pool. *Mol Biol Cell.* 2011;22(21):4047-4055. DOI: 10.1091/mbc.e11-06-0582. https://pmc.ncbi.nlm.nih.gov/articles/PMC3204067/

6. **olave-2002-nuclear-actin-chromatin-abstract**: Olave IA, Reck-Peterson SL, Crabtree GR. Nuclear actin and actin-related proteins in chromatin remodeling. *Annu Rev Biochem.* 2002;71:755-81. DOI: 10.1146/annurev.biochem.71.110601.135507. PMID: 12045110. https://pubmed.ncbi.nlm.nih.gov/12045110/

7. **riviere-2012-baraitser-winter-abstract**: Rivière JB, van Bon BW, Hoischen A, et al. De novo mutations in the actin genes ACTB and ACTG1 cause Baraitser-Winter syndrome. *Nat Genet.* 2012;44(4):440-444. DOI: 10.1038/ng.1091. PMID: 22366783. https://www.nature.com/articles/ng.1091

8. **wilkinson-2018-setd3-histidine-abstract**: Wilkinson AW, Diep J, Dai S, et al. SETD3 is an actin histidine methyltransferase that prevents primary dystocia. *Nature.* 2018;565(7739):372-376. DOI: 10.1038/s41586-018-0821-8. PMID: 30626964. https://www.nature.com/articles/s41586-018-0821-8

9. **singer-2001-beta-actin-mrna-localization-abstract**: Shiv IS, Singer RH, et al. The physiological significance of β-actin mRNA localization in determining cell polarity and directional motility. *Proc Natl Acad Sci USA.* 2001;98(9):4973-4978. DOI: 10.1073/pnas.121146098. https://www.pnas.org/doi/full/10.1073/pnas.121146098

10. **chua-2009-zbp1-mrna-localization-abstract**: Fehrenbacher KL, et al. Two ZBP1 KH domains facilitate β-actin mRNA localization, granule formation, and cytoskeletal attachment. *J Cell Biol.* 2003;160(1):77-87. DOI: 10.1083/jcb.200206003. PMID: 12507992. https://rupress.org/jcb/article/160/1/77/33113/

11. **pollard-2017-actin-cytoskeleton-motility-abstract**: Pollard TD, Cooper JA. The Actin Cytoskeleton and Actin-Based Motility. *Cold Spring Harb Perspect Biol.* 2018;10(1):a018218. DOI: 10.1101/cshperspect.a018218. https://pmc.ncbi.nlm.nih.gov/articles/PMC5749151/

12. **tori-2021-betaactin-3d-genome-abstract**: Tori A, et al. β-actin dependent chromatin remodeling mediates compartment level changes in 3D genome architecture. *Nat Commun.* 2021;12:5240. DOI: 10.1038/s41467-021-25596-2. https://www.nature.com/articles/s41467-021-25596-2

13. **grazova-2018-actin-ptm-cinderella-abstract**: Gresova H, et al. Actin Post-translational Modifications: The Cinderella of Cytoskeletal Control. *Trends Biochem Sci.* 2018;43(4):243-255. DOI: 10.1016/j.tibs.2018.12.008. https://www.cell.com/trends/biochemical-sciences/fulltext/S0968-0004(18)30259-7

14. **huxley-1954-sliding-filament-summary**: Huxley AF, Niedergerke R; Huxley HE, Hanson J. Structural Changes in Muscle During Contraction / Changes in the Cross-Striations of Muscle During Contraction. *Nature.* 1954;173:971-976.

15. **tapon-1997-rho-rac-cdc42-abstract**: Tapon N, Hall A. Rho, Rac and Cdc42 GTPases regulate the organization of the actin cytoskeleton. *Curr Opin Cell Biol.* 1997;9(1):86-92. DOI: 10.1016/s0955-0674(97)80156-1. PMID: 9013670. https://pubmed.ncbi.nlm.nih.gov/9013670/

16. **vanri-2022-nterminal-processing-abstract**: Vanri M, et al. Differential N-terminal processing of beta and gamma actin. *iScience.* 2022;25(10):105181. DOI: 10.1016/j.isci.2022.105181. PMCID: PMC9556930. https://pmc.ncbi.nlm.nih.gov/articles/PMC9556930/

17. **chen-2021-actb-pancancer-abstract**: Chen J, et al. A pan-cancer analysis of the prognostic and immunological role of β-actin (ACTB) in human cancers. *Bioengineered.* 2021;12(1):4746-4759. DOI: 10.1080/21655979.2021.1973220. PMCID: PMC8806805. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8806805/


## Citations

1. chen-2021-actb-pancancer-abstract.md
2. chua-2009-zbp1-mrna-localization-abstract.md
3. dominguez-2011-actin-structure-function-abstract.md
4. grazova-2018-actin-ptm-cinderella-abstract.md
5. huxley-1954-sliding-filament-summary.md
6. korn-1987-actin-atp-hydrolysis-abstract.md
7. olave-2002-nuclear-actin-chromatin-abstract.md
8. patrinostro-2018-actb-essential-abstract.md
9. pollard-2016-actin-abps-abstract.md
10. pollard-2017-actin-cytoskeleton-motility-abstract.md
11. riviere-2012-baraitser-winter-abstract.md
12. shubhan-2011-betaactin-growth-migration-abstract.md
13. singer-2001-beta-actin-mrna-localization-abstract.md
14. tapon-1997-rho-rac-cdc42-abstract.md
15. tori-2021-betaactin-3d-genome-abstract.md
16. vanri-2022-nterminal-processing-abstract.md
17. wilkinson-2018-setd3-histidine-abstract.md