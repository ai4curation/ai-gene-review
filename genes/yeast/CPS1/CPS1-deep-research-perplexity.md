---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-24T17:54:19.618871'
end_time: '2025-11-24T17:57:04.627438'
duration_seconds: 165.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: CPS1
  gene_symbol: CPS1
  uniprot_accession: P27614
  protein_description: 'RecName: Full=Carboxypeptidase S; EC=3.4.17.4; AltName: Full=GLY-X
    carboxypeptidase; AltName: Full=YSCS;'
  gene_info: Name=CPS1; Synonyms=CPS; OrderedLocusNames=YJL172W; ORFNames=J0510;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the peptidase M20A family. .
  protein_domains: ArgE/DapE_CS. (IPR001261); Bact_exopeptidase_dim_dom. (IPR036264);
    Pept_M20_carboxypep. (IPR017141); Pept_M20A. (IPR047177); Peptidase_M20. (IPR002933)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 48
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P27614
- **Protein Description:** RecName: Full=Carboxypeptidase S; EC=3.4.17.4; AltName: Full=GLY-X carboxypeptidase; AltName: Full=YSCS;
- **Gene Information:** Name=CPS1; Synonyms=CPS; OrderedLocusNames=YJL172W; ORFNames=J0510;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the peptidase M20A family. .
- **Key Domains:** ArgE/DapE_CS. (IPR001261); Bact_exopeptidase_dim_dom. (IPR036264); Pept_M20_carboxypep. (IPR017141); Pept_M20A. (IPR047177); Peptidase_M20. (IPR002933)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CPS1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CPS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CPS1** (gene ID: CPS1, UniProt: P27614) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze the search results and the query carefully to understand what I need to do.

The user is asking for a comprehensive research report on the gene CPS1 (UniProt: P27614) in Saccharomyces cerevisiae (Baker's yeast). The protein description is:
- RecName: Full=Carboxypeptidase S; EC=3.4.17.4
- Gene: CPS1 (YJL172W)
- Organism: Saccharomyces cerevisiae (strain ATCC 204508 / S288c)
- Protein Family: Peptidase M20A family
- Key Domains: ArgE/DapE_CS, Bact_exopeptidase_dim_dom, Pept_M20_carboxypep, Pept_M20A, Peptidase_M20

The user wants me to verify I'm researching the CORRECT gene first. Let me check:

1. Is the gene symbol "CPS1" correct? YES - The search results confirm this is the yeast carboxypeptidase S gene (YJL172W).
2. Is the organism correct? YES - All sources confirm this is Saccharomyces cerevisiae.
3. Do the protein family/domains align? YES - Sources confirm it's a zinc-dependent metallocarboxypeptidase of the M20 family.

Important note: I noticed that search result [26] mentions "CPS1 Gene - GeneCards" which describes a different CPS1 - the HUMAN carbamoyl phosphate synthetase 1, which is completely different from the yeast carboxypeptidase S. I need to be careful to only use information about the yeast carboxypeptidase S (P27614), not the human enzyme.

Looking at the search results provided, I have excellent sources on the yeast CPS1:
- [1], [2], [7], [8], [11], [12], [14], [19], [22], [23] - SGD (Saccharomyces Genome Database) and related sources on yeast CPS1


- [12], [14], [19], [32], [46] - Detailed review on "The proteolytic landscape of the yeast vacuole" by Hecht et al. provides context on vacuolar proteases
- [4], [10], [34], [52] - UniProt entries for CPS1 with structural and functional data
- [3] - A similar carboxypeptidase from Aspergillus niger for comparative analysis
- [6], [9], [35] - Information on related carboxypeptidases in other organisms
- [16], [17], [57] - Information on vacuolar proteases and related serine carboxypeptidases
- [20], [30], [51] - Gene regulation and expression patterns for CPS1
- [44], [47] - MVB sorting mechanisms and ubiquitination of CPS
- [45] - pH-dependent enzyme kinetics

I'm filtering out [26], [38], [41], [48], [56] since these reference the human carbamoyl phosphate synthetase 1, which is unrelated to the yeast carboxypeptidase I'm studying.

The key findings show CPS1 is a zinc-dependent metallocarboxypeptidase from the M20 family that localizes to the vacuole. Its primary role involves hydrolytic activity within the vacuolar proteolytic system, with regulation occurring at both the gene expression and post-translational modification levels through ubiquitination and MVB sorting pathways.
</think>

# Carboxypeptidase S (CPS1): Biochemical Function, Cellular Localization, and Role in Vacuolar Proteolysis in Saccharomyces cerevisiae

Carboxypeptidase S (CPS1), encoded by the YJL172W locus in Saccharomyces cerevisiae, is a zinc-dependent metallocarboxypeptidase belonging to the M20 family of metalloproteases that functions as a critical component of the yeast vacuolar degradation system.[12][14][19] This 64 kilodalton precursor protein is synthesized as an inactive zymogen in the endoplasmic reticulum, undergoes post-translational processing including glycosylation and ubiquitination, transits through the secretory pathway to the vacuole, and ultimately becomes a soluble vacuolar enzyme that contributes approximately 60% of the enzymatic activity required to hydrolyze dipeptide substrates including benzyloxycarbonyl-glycine-leucine (Cbz-Gly-Leu).[12][14][19] CPS1 exhibits substrate specificity preferentially directed toward peptides with hydrophobic C-terminal amino acids, particularly leucine and glycine residues, making it functionally complementary to other vacuolar proteases in degrading the diverse protein substrates that reach the vacuole through endocytosis and autophagy.[12][14][19] The enzyme's regulation by nutrient availability, particularly nitrogen limitation, its essential role in sporulation, and its participation in the recycling of amino acids from degraded proteins underscore its importance in cellular nitrogen metabolism and protein homeostasis.

## Protein Architecture and Molecular Classification

### Structural Organization and Evolutionary Context

Carboxypeptidase S belongs to the peptidase M20A subfamily of metalloproteases, a classification that reflects both its catalytic mechanism and evolutionary relationships with related peptidases.[12][19][22] The M20 family encompasses a diverse group of zinc-dependent exopeptidases and endopeptidases that share conserved structural features and catalytic strategies.[12][19] Within this family, CPS1 is specifically classified as belonging to a subgroup characterized by the presence of conserved domains designated as ArgE/DapE_CS, which represents a signature motif found in arginine-utilizing enzymes and diapeptidase E family members.[34][59] The protein contains multiple functional domains organized within its approximately 500-amino acid polypeptide sequence, including regions responsible for zinc binding, substrate recognition, and catalytic activity.[12][19] The presence of N-linked glycosylation sites in CPS1, particularly at asparagine residue 525, contributes to the mature enzyme's molecular weight and stability as it functions within the acidic vacuolar compartment.[52]

The evolutionary conservation of CPS1 structure becomes apparent when comparing it with other carboxypeptidases from fungi and higher organisms.[3][6][9] A newly characterized carboxypeptidase from Aspergillus niger designated CapA shares considerable structural homology with yeast CPS1, exhibiting a similar zinc-dependent mechanism and preference for hydrophobic C-terminal amino acids including leucine and phenylalanine.[3] The kinetic properties of the Aspergillus enzyme reveal fundamental principles applicable to understanding CPS1 function, including optimal catalytic activity at slightly acidic pH (6.0) and enhanced thermostability within physiological temperature ranges.[3] Human carboxypeptidases A and B display similar architectural organization with zinc coordination sites and substrate binding pockets that appear to have diverged through evolution to accommodate different specificity profiles.[6][9] The conservation of catalytic mechanisms across the metallocarboxypeptidase superfamily, despite substantial sequence divergence, attests to the evolutionary antiquity and biochemical utility of this proteolytic strategy.[6][9][55]

### Zinc Coordination and Catalytic Mechanism

The zinc ion at the active site of CPS1 serves as the central organizing element of the catalytic mechanism, coordinating substrate molecules and facilitating the nucleophilic attack necessary for peptide bond hydrolysis.[12][14][19] The zinc ion in CPS1, like other M20 family metalloproteases, is coordinated by multiple amino acid residues through a geometry that typically positions the metal ion to activate a water molecule for catalysis.[25][55][58] The activated zinc-coordinated water molecule then performs nucleophilic attack on the carbonyl carbon of the scissile peptide bond, forming a tetrahedral intermediate that is stabilized by interactions with active site residues.[55][58] Following stabilization and collapse of the tetrahedral intermediate, the C-terminal amino acid is released from the enzyme, generating a shorter peptide product and regenerating the enzyme for subsequent catalytic cycles.[55][58] The general acid-base catalysis performed by CPS1 depends critically on the zinc ion, as evidenced by the complete loss of enzymatic activity when the metal is chelated or removed, demonstrating that the metal ion is not merely a structural component but an integral participant in the catalytic mechanism.[55]

The substrate binding pocket of CPS1 exhibits selectivity for amino acid residues at the C-terminus of peptide substrates based on the chemical properties and spatial dimensions of the binding site.[12][14][32] The S1 subsite—the designation for the enzyme subsites that recognize amino acid positions relative to the scissile bond—in CPS1 appears to preferentially accommodate hydrophobic amino acids through hydrophobic interactions with aromatic residues lining the binding pocket.[12][32] The S1' subsite, which recognizes the penultimate amino acid of the substrate relative to the scissile bond, exhibits similarly hydrophobic character that facilitates productive binding of substrates containing hydrophobic residues at this position.[12][32] This dual specificity for hydrophobic residues at both the P1 and P1' positions confers upon CPS1 the ability to specifically recognize and degrade peptides derived from hydrophobic proteins, such as those released from membrane proteins or other hydrophobic cellular compartments.[12][14]

## Biological Function and Enzymatic Specificity

### Substrate Recognition and Catalytic Selectivity

Carboxypeptidase S catalyzes the hydrolysis of C-terminal peptide bonds in peptides and proteins, specifically removing the terminal amino acid from the carboxyl terminus of substrates.[12][14][19] The enzyme exhibits characteristic specificity that enables it to preferentially cleave peptides in which the penultimate amino acid is glycine or the C-terminal amino acid is leucine, as exemplified by its robust activity toward the synthetic dipeptide Cbz-Gly-Leu.[12][14][19][32] This preference for glycine in the penultimate position and leucine at the C-terminus reflects a fundamental aspect of CPS1's evolutionary specialization within the vacuolar degradation machinery, positioning it to degrade specific classes of peptide products generated by other vacuolar proteases.[12][14][19] The kinetic parameters of CPS1 demonstrate measurable affinity and catalytic efficiency toward diverse peptide substrates, although substrates lacking appropriate hydrophobic character at the C-terminus or penultimate position are cleaved with substantially reduced efficiency or not at all.[12][14]

In the context of natural cellular substrates, CPS1 functions as part of an integrated proteolytic system that sequentially modifies protein degradation products.[12][14][19][32] The vacuolar endoprotease proteinase B (PrB) generates peptide fragments through hydrolysis at internal sites within proteins, producing products with diverse C-terminal and penultimate amino acids.[12][14][32] These diverse peptide products become substrates for the exoproteases including CPS1, which contribute to complete degradation by progressively removing individual amino acids from peptide termini.[12][14][32] The substrate specificity of CPS1 overlaps partially with that of carboxypeptidase Y (CPY), another major vacuolar carboxypeptidase, with both enzymes contributing to hydrolysis of particular dipeptide substrates.[12][14][19][32] However, CPS1 exhibits distinct selectivity from CPY, with CPS1 showing greater preference for peptides containing glycine in the penultimate position, whereas CPY accommodates a broader array of hydrophobic amino acids at this position.[12][14][32] This complementary specificity pattern suggests that CPS1 and CPY have evolved to partition the substrate pool in the vacuole, with each enzyme specializing in particular substrate types that reflect the diversity of proteins undergoing degradation.

### Evidence for Substrate Specificity from Biochemical Studies

Direct biochemical evidence for the substrate preferences of CPS1 derives from classical studies utilizing synthetic peptide substrates and more recent approaches employing peptide library methodologies.[12][14][15][32][35] The isolation of the CPS1 gene was accomplished by selecting for yeast growth on media in which the dipeptide Cbz-Gly-Leu served as the sole source of nitrogen and leucine, a selection strategy that exploited the unique ability of CPS1-expressing strains to cleave this particular dipeptide and extract nutrients from it.[15][32] This genetic evidence provided the first strong indication of CPS1's specificity, establishing that the enzyme could effectively degrade a peptide with glycine in the penultimate position and leucine at the C-terminus.[15][32] Subsequent biochemical characterization confirmed that CPS1 contributes approximately sixty percent of the total enzymatic activity required to hydrolyze Cbz-Gly-Leu when measured in cell-free assays using yeast cell extracts or purified vacuolar enzymes.[12][14][32] In strains lacking carboxypeptidase Y (PRC1-deleted strains), CPS1 activity becomes essential for growth on media containing Cbz-Gly-Leu as the sole nitrogen and leucine source, demonstrating that CPS1 possesses sufficient enzymatic capacity to sustain this particular degradation function when acting independently.[12][14][32]

The comparison of CPS1 function with other characterized carboxypeptidases provides additional insights into the structural basis for substrate specificity within the metallocarboxypeptidase family.[6][9][35][55] Examination of kinetic data across human carboxypeptidases A, B, D, and E reveals a gradient of substrate specificity, with some enzymes exhibiting very restricted selectivity for particular amino acids while others display broader substrate promiscuity.[6][9][35] The restricted specificity observed in some carboxypeptidases correlates with structural features of the substrate binding pocket, particularly the identity and positioning of amino acids lining the S1 subsite that determines which C-terminal residues are accommodated.[6][9][35][55] Structure-function studies of human carboxypeptidase A reveal that large hydrophobic amino acids lining the S1 binding pocket account for the enzyme's preference for hydrophobic C-terminal residues.[6][9][55] By homology, the hydrophobic character of CPS1's binding pocket likely reflects similar structuring of the substrate binding site to accommodate hydrophobic C-terminal amino acids.[12][14]

## Cellular Localization and Subcellular Trafficking

### Targeting to the Vacuolar Lumen

Carboxypeptidase S functions within the lumen of the yeast vacuole, a compartment analogous to the mammalian lysosome that serves as the primary site of protein degradation and recycling within eukaryotic cells.[12][14][19][46] The vacuole represents a slightly acidic environment with pH approximately 6.2, in contrast to the cytosolic pH of approximately 7.2, creating conditions that favor the activity of CPS1 and other vacuolar hydrolases.[46] CPS1 is synthesized as a ~64 kilodalton precursor (preCPS1) in the endoplasmic reticulum as a type II transmembrane protein with a signal sequence spanning amino acids 20 through 40 that becomes inserted into the ER membrane during translation.[12][14][19][32] The orientation of the nascent CPS1 polypeptide within the ER membrane positions the C-terminus containing the catalytic domain facing the ER lumen, an orientation that facilitates transport of the enzyme through the secretory pathway.[12][14][19][32] During transit through the ER and Golgi apparatus, CPS1 undergoes post-translational modifications including N-linked glycosylation, acquiring N-linked glycans that contribute approximately 3 to 5 kilodaltons to the mature enzyme mass.[12][14][19][32]

The vacuolar targeting of CPS1 occurs through the carboxypeptidase Y (CPY) pathway, which represents one of two major routes for delivery of biosynthetic cargo proteins to the yeast vacuole.[12][14][19][46] This pathway differs mechanistically from the alkaline phosphatase (ALP) pathway, which delivers cargo directly from the trans-Golgi network to the vacuole through AP-3 adaptor complex-mediated vesicular transport.[12][14][19][46] In contrast, CPY pathway cargo including CPS1 traffics from the Golgi to early endosomes and subsequently to multivesicular bodies (MVBs), where the cargo proteins undergo ubiquitin-dependent internalization into the lumen of MVB internal vesicles through mechanisms dependent on ESCRT (Endosomal Sorting Complex Required for Transport) complexes.[12][14][19][44][46][47] The MVBs then fuse with the vacuole, releasing their internal vesicles into the vacuolar lumen where they undergo lysis, exposing cargo proteins including CPS1 to the vacuolar proteases.[12][14][19][44][46][47]

The ubiquitination of CPS1 plays a critical role in directing the enzyme into the MVB pathway, as ubiquitinated cargo is recognized by ESCRT protein Vps27, which initiates recruitment of additional ESCRT machinery to mediate cargo internalization.[12][14][19][44][46][47] CPS1 ubiquitination is accomplished through the action of the ubiquitin ligase Rsp5, which is recruited to CPS1 through adaptor proteins Tul1 and Bsd2 containing L/PPxY motifs that interact with the ubiquitin ligase.[12][14][19][46][47] The ubiquitination process requires the coordinated action of E1 ubiquitin-activating enzymes and E2 ubiquitin-conjugating enzymes together with the E3 ligase Rsp5, resulting in the attachment of ubiquitin polymers to lysine residues on the CPS1 surface.[12][14][19][46][47] Once in the MVB lumen following internalization, ubiquitinated CPS1 becomes accessible to deubiquitinating enzymes and vacuolar proteases.[12][14][19][44][46][47]

### Proteolytic Maturation in the Vacuolar Lumen

Upon arrival in the vacuolar lumen within the internal vesicles of multivesicular bodies, the membrane-bound precursor form of CPS1 undergoes proteolytic processing by the vacuolar proteinase A (PrA, also designated Pep4p), a principal vacuolar endoprotease that activates many vacuolar zymogens.[12][14][17][19][32] The PrA-catalyzed cleavage releases the soluble C-terminal catalytic domain of CPS1 from the membrane-anchored N-terminal portion, generating the active mature form of the enzyme that functions freely within the vacuolar lumen.[12][14][19][32] Two major forms of mature CPS1 are observed in yeast cells, with apparent molecular masses of 74 and 77 kilodaltons, representing CPS1 molecules modified with two or three N-linked glycans respectively.[12][14][19][32] Interestingly, even in its membrane-bound precursor form, CPS1 retains considerable catalytic activity, suggesting that the proteolytic processing event maximizes enzyme activity rather than initially generating it.[12][14][19] This phenomenon of retained activity in the zymogen form may represent an adaptation that allows some proteolytic function even before complete maturation, or alternatively may reflect the particular structural properties of the membrane-bound form that fortuitously preserve catalytic geometry.

The vacuolar localization of CPS1 provides critical spatial compartmentalization that protects cytosolic and secretory pathway proteins from inappropriate proteolytic degradation while concentrating CPS1 with its natural substrate pool.[12][14][19][46] The acidic pH of the vacuole, approximately 6.2, falls close to the apparent pH optimum for CPS1 activity as determined from studies of related carboxypeptidases and from direct measurements of CPS1 activity at varied pH in cell-free assays.[3][12][14][19] The somewhat acidic pH optimum reflects the ionizable amino acid residues in the CPS1 active site that must be appropriately protonated for catalytic activity, with deviations from the optimum pH resulting in diminished proton transfer and reduced catalytic turnover.[45] Additionally, the vacuolar environment maintains relatively high salt concentrations characteristic of the osmotically stressed vacuolar lumen, conditions that similarly favor the activity of CPS1 and other vacuolar proteases.[12][14][19][46]

## Participation in Vacuolar Proteolytic Networks

### Integration with Other Vacuolar Proteases

Carboxypeptidase S functions as one component of an integrated system of vacuolar proteases that collectively achieve comprehensive degradation of diverse protein substrates directed to the vacuole.[12][14][17][19][32][46] The vacuolar proteolytic system includes the major endoprotease proteinase B (PrB), which generates initial peptide products through hydrolysis at internal peptide bonds; carboxypeptidase Y (CPY), a broad-specificity exopeptidase complementary to CPS1; and aminopeptidase I (API or Ape1), a zinc-dependent metalloaminopeptidase that removes amino acids from peptide N-termini.[12][14][17][19][32][46] The initial degradation step performed by PrB produces peptides of varying lengths and sequence composition, creating a heterogeneous substrate pool that becomes further modified by the exoproteases CPS1, CPY, and other enzymatic activities.[12][14][17][19][32][46] CPS1 and CPY, operating as carboxypeptidases that sequentially remove C-terminal residues, work together with aminopeptidases to eventually reduce peptide substrates to individual amino acids that can be recycled by the cell.[12][14][17][19][32][46]

The functional specialization and complementary substrate specificities of CPS1 and CPY suggest that these two exoproteases have evolved to partition the degradation workload in response to the diversity of proteins undergoing vacuolar degradation.[12][14][19][32] CPY accommodates a broad array of hydrophobic C-terminal amino acids including alanine, glycine, valine, leucine, isoleucine, methionine, and phenylalanine, as well as some polar residues in certain contexts.[12][14][19][32] In contrast, CPS1 exhibits narrower selectivity, preferentially cleaving peptides in which glycine occupies the penultimate position and leucine or glycine occupies the C-terminal position.[12][14][19][32] This differentiation in specificity may reflect the relative abundance or importance of particular amino acid combinations in the natural proteinaceous substrates of the vacuole, allowing CPS1 to specialize on peptide products generated through prior proteolysis that create the preferred penultimate glycine-terminal leucine/glycine patterns.[12][14][19][32]

Evidence for functional redundancy between CPS1 and CPY comes from genetic studies examining growth phenotypes under conditions where peptides serve as sole nitrogen sources.[12][14][19][32][46] In wild-type yeast strains, both CPY and CPS1 contribute to degradation of Cbz-Gly-Leu, each accounting for approximately 40-60% of total hydrolytic activity toward this substrate.[12][14][19][32] When CPY is absent due to deletion of the PRC1 gene encoding carboxypeptidase Y, CPS1 becomes essential for growth on Cbz-Gly-Leu as the sole nitrogen and leucine source, demonstrating that CPS1 possesses sufficient catalytic capacity to compensate for the loss of CPY.[12][14][19][32] However, the reduced growth rate observed in prc1 mutants compared to wild-type cells even when CPS1 is functional suggests that CPS1 operates with reduced efficiency toward the Cbz-Gly-Leu substrate, and that the division of labor between these two carboxypeptidases normally reflects their distinct kinetic properties and substrate affinities.[12][14][19][32]

### Role in Autophagy and Cellular Nutrient Recycling

Carboxypeptidase S participates in the vacuolar degradation pathway called autophagy, a process through which cells envelop portions of cytoplasm or damaged organelles in double-membrane autophagosomes that fuse with the vacuole to deliver cargo for degradation and recycling.[12][14][16][17][19][39][46][57] During nutrient-limited conditions such as nitrogen starvation, cells activate autophagy to generate a pool of free amino acids through degradation of long-lived proteins, damaged organelles, and other cellular components.[12][14][16][17][39][46][57] The vacuolar proteases including CPS1 catalyze the degradation of autophagic cargo delivered to the vacuole, ultimately releasing amino acids that are transported back into the cytoplasm where they are re-utilized for synthesis of essential proteins required for stress adaptation and survival.[12][14][16][17][39][46][57] Evidence for CPS1's role in autophagy comes from studies demonstrating that cells deleted for both PRC1 and YBR139W (a newly characterized serine carboxypeptidase homologous to PRC1) exhibit defects in autophagic flux, including accumulation of incomplete autophagic body breakdown and reduced recovery of amino acid pools following nitrogen starvation.[16][17][57]

The process of vacuolar amino acid recycling during autophagy depends critically on the sequential enzymatic activities of the vacuolar proteolytic system.[12][14][16][17][39][46][57] Autophagic bodies deliver intact proteins to the vacuole, where PrB initiates degradation by cleaving peptide bonds at specific internal sites determined by the enzyme's substrate specificity.[12][14][17][46] The peptide fragments generated by PrB then become substrates for the exoproteases including CPS1, which progressively remove individual amino acids from peptide termini through sequential cleavage events.[12][14][17][46] The accumulation of intermediate peptide products when CPS1 or related carboxypeptidases are absent indicates that the peptide pool within the vacuole becomes sequestered, unable to be completely degraded to amino acids.[12][14][16][17][46][57] This sequestration represents a functional block in nutrient recovery, as amino acids remain trapped in partially degraded peptide products that cannot be efficiently transported across the vacuolar membrane for reuse by the cell.[12][14][16][17][46][57]

### Participation in Sporulation and Cellular Differentiation

Beyond its role in routine protein degradation, CPS1 participates in the specialized proteolytic program associated with yeast sporulation, a developmental process through which haploid yeast cells undergo meiosis to generate spores capable of surviving adverse environmental conditions.[12][14][19][32][46] Genetic studies examining sporulation frequency in mutant strains revealed that disruption of PrB activity produces a partial defect in sporulation, while combined disruption of PrB, CPY, and CPS1 activities completely abolishes sporulation, with cells unable to form functional spores.[12][14][19][32][46] This observation indicates that the complete suite of vacuolar proteases, including CPS1, becomes essential during the differentiation program leading to sporulation.[12][14][19][32][46] The specific proteolytic processes dependent on CPS1 during sporulation remain incompletely characterized, but likely involve the controlled degradation of particular proteins required for vegetative growth but not for spore development, as well as degradation of other proteins that would be incompatible with the dormant metabolic state of mature spores.[12][14][19][32][46]

The genetic evidence for CPS1's role in sporulation derives from systematic studies examining the phenotypes of protease-deficient yeast strains.[12][14][19][32][46] The fact that combined loss of PrB, CPY, and CPS1 activities completely blocks sporulation, whereas loss of any single protease still permits sporulation (albeit with reduced efficiency in the PrB mutant), suggests that substantial functional redundancy exists among these proteases during normal sporulation.[12][14][19][32][46] However, the cumulative requirement for all three proteases indicates that the proteolytic workload during sporulation is substantial and cannot be accommodated by any single protease acting alone.[12][14][19][32][46] This requirement may reflect the need to process large quantities of cytoplasmic proteins during differentiation or to accomplish particular proteolytic events that require the specific substrate selectivity properties of CPS1 in combination with those of other proteases.

## Gene Regulation and Nutrient-Responsive Expression

### Transcriptional Regulation Under Nitrogen Limitation

Expression of the CPS1 gene is regulated by nutrient availability, particularly the availability of nitrogen, reflecting the role of the encoded protein in nitrogen metabolism and amino acid recycling.[1][12][20][30][51] Studies of CPS1 gene expression under various nutrient conditions revealed that CPS1 transcription increases substantially when yeast cells are cultured in media with restricted nitrogen availability, a condition known as nitrogen limitation or N-starvation.[12][20][30][51] This nutrient-responsive regulation of CPS1 expression represents an adaptation whereby the cell anticipates the need for enhanced proteolytic capacity when exogenous nitrogen becomes scarce, as the cell must increasingly rely on degradation and recycling of endogenous proteins to sustain biosynthesis.[12][20][30][51] The molecular mechanisms underlying CPS1 transcriptional regulation involve the binding of transcription factors including nitrogen catabolite repression (NCR) factors such as GATA transcription factors to regulatory sequences in the CPS1 promoter.[1][12][20][30][51]

The promoter region of CPS1 contains multiple cis-acting regulatory elements that mediate the transcriptional response to changing nitrogen availability.[1][12][20][30][51] Detailed analysis of CPS1 promoter sequences identified a 162 base pair fragment located at positions -644 to -482 relative to the transcription start site that is important for the regulation of CPS1 expression in response to nitrogen status.[30][51] Deletion or mutation of this promoter region severely impairs CPS1 transcription even when cells are exposed to nitrogen-limited conditions, indicating that this element serves as a binding site for transcription factors that activate CPS1 expression under nitrogen limitation.[30][51] The binding of GATA factors and other transcriptional regulators to these promoter elements appears to integrate signals reflecting the cellular nitrogen status, with enhanced CPS1 transcription occurring when the cell detects inadequate nitrogen availability for optimal growth.[1][12][20][30][51]

The physiological significance of nutrient-responsive CPS1 expression becomes apparent when considering the metabolic context in which proteolysis operates.[12][20][30][51] Under nutrient-rich conditions with abundant exogenous nitrogen, cells preferentially synthesize proteins for growth and biosynthesis rather than degrading endogenous proteins, and CPS1 expression remains relatively low as proteolytic capacity is not limiting.[12][20][30][51] In contrast, when nitrogen becomes limiting, cells respond by upregulating the expression of proteases including CPS1 to increase the rate of protein degradation and amino acid recycling, thereby maximizing the recovery of nitrogen from endogenous proteins for use in biosynthesis of essential cellular components.[12][20][30][51] This regulatory logic ensures that protease expression is appropriately scaled to match the metabolic demands imposed by nutrient availability, preventing wasteful synthesis of excess proteolytic capacity during nutrient abundance while ensuring sufficient capacity during nutrient limitation.

### Integration with Broader Metabolic and Stress Responses

Beyond the direct regulation by nitrogen availability, CPS1 expression likely integrates signals from broader cellular stress responses and metabolic regulatory networks that respond to multiple environmental stresses including osmotic stress, oxidative stress, and energy limitation.[12][20][30][51] The yeast General Amino Acid Control (GAAC) pathway represents a conserved regulatory system through which cells detect amino acid limitation and activate a transcriptional program that promotes amino acid biosynthesis and protein degradation.[12][20][30][51] During amino acid limitation, the kinase Gcn2 becomes activated through recognition of uncharged (deacylated) transfer RNAs, and phosphorylates the translation initiation factor eIF2α, leading to a translational control mechanism that preferentially allows translation of ATF4-family transcription factors such as Gcn4.[12][20][30][51] These transcription factors then activate expression of amino acid biosynthetic enzymes and proteases including those required for recycling amino acids from protein degradation.[12][20][30][51]

The interconnection between CPS1 expression and broader nutrient-sensing pathways underscores the central role of proteolysis in cellular nutrition and stress adaptation.[12][20][30][51] When cells experience multiple simultaneous stresses—for example, both nitrogen and carbon limitation—the combined signaling through nutrient-sensing pathways such as the TOR kinase pathway and the GAAC pathway likely produces a synergistic upregulation of CPS1 and other proteases that maximizes the capacity for amino acid recycling.[12][20][30][51] This integrated regulation ensures that the yeast vacuolar proteolytic system responds dynamically to the ever-changing nutritional and environmental conditions encountered during the yeast lifecycle.

## Post-Translational Modifications and Processing

### Glycosylation and Protein Maturation

Post-translational modifications of CPS1 including N-linked glycosylation play important roles in enzyme stability, trafficking, and possibly catalytic efficiency within the vacuolar environment.[12][14][19][49][52] During transit through the endoplasmic reticulum, nascent CPS1 synthesized as a type II transmembrane protein undergoes N-linked glycosylation at conserved asparagine residues within the N-X-(S/T) sequon motif (where X represents any amino acid except proline), adding glucose-containing oligosaccharide structures to the nascent polypeptide.[12][14][19][49] These N-linked glycans become further modified during transit through the Golgi apparatus, where additional glucose residues are trimmed and mannosyl residues are added through the action of various glycosidases and glycosyltransferases.[12][14][19][49] The mature N-linked glycans on CPS1 contribute approximately 3 to 5 kilodaltons to the enzyme mass, accounting for the observed molecular weights of mature 74 and 77 kilodalton forms representing enzymatically active CPS1 with two or three N-linked glycans respectively.[12][14][19][49]

The presence of multiple N-linked glycosylation sites on CPS1 likely reflects the importance of these modifications for enzyme function within the harsh vacuolar environment.[12][14][19][49] N-linked glycans contribute to protein folding and stability, enhance resistance to proteolytic degradation, and facilitate recognition by trafficking machinery and sorting receptors.[12][14][19][49][52] The glycosylation of CPS1 may specifically protect the enzyme from inappropriate degradation by other vacuolar proteases, as the vacuole contains multiple proteases with overlapping substrate specificities that could potentially degrade CPS1 itself if the enzyme were not protected by glycosylation-mediated structural modifications.[12][14][19][49] Additionally, N-linked glycans may contribute to proper folding of the CPS1 polypeptide, ensuring that the three-dimensional structure of the active site and substrate-binding regions achieve the precise geometry required for catalysis.[12][14][19][49]

### Ubiquitination for Vacuolar Targeting

Ubiquitination of CPS1 constitutes a critical post-translational modification that marks the enzyme for internalization into multivesicular body internal vesicles through the ESCRT-dependent mechanism of selective ubiquitin-mediated cargo recognition.[12][14][19][44][46][47] The ubiquitin-protein conjugation process involves three enzymatic steps: first, ubiquitin-activating enzyme E1 activates ubiquitin in an ATP-dependent reaction, producing a high-energy ubiquitin adenylate intermediate; second, ubiquitin is transferred to a ubiquitin-conjugating enzyme E2; and third, the ubiquitin ligase E3 (in this case Rsp5) catalyzes transfer of ubiquitin from E2 to lysine residues on the CPS1 polypeptide.[12][14][19][44][46][47] Multiple ubiquitin molecules are conjugated to CPS1, forming ubiquitin polymers through ubiquitin-ubiquitin conjugation, with the majority of ubiquitin chain linkages occurring through lysine 63 of ubiquitin (K63-linked chains) rather than the lysine 48 linkages typically associated with proteasomal degradation.[12][14][19][44][46][47]

The polyubiquitination of CPS1 serves as a cellular "cargo code" that is recognized by ESCRT proteins containing ubiquitin-binding domains, enabling selective internalization of CPS1 into MVB internal vesicles.[12][14][19][44][46][47] The initial recognition occurs through binding of ubiquitinated CPS1 to Vps27, the first ESCRT protein in the pathway, which contains ubiquitin-interacting motifs (UIM) that specifically recognize ubiquitin moieties on target proteins.[12][14][19][44][46][47] Following recruitment of Vps27 to ubiquitinated CPS1 on the endosomal membrane, additional ESCRT complexes (ESCRT-I, ESCRT-II, and ESCRT-III) are sequentially recruited, ultimately forming a membrane-deforming machinery that drives invagination of the endosomal limiting membrane and internalization of CPS1-containing membrane domains into the interior of the multivesicular body.[12][14][19][44][46][47] The ubiquitination of CPS1 is reversible, as deubiquitinating enzymes present in the vacuolar lumen remove ubiquitin moieties following the fusion of MVBs with the vacuole, releasing free CPS1 and other ubiquitinated cargo into the vacuolar lumen where they become accessible to proteolytic and other enzymatic modifications.[12][14][19][44][46][47]

## Comparative Perspectives: CPS1 Among Carboxypeptidases

### Structural and Functional Relationships with Other Metalloproteases

Carboxypeptidase S occupies a specific position within the broader landscape of metalloproteases and carboxypeptidases characterized across diverse organisms, reflecting its specialized role in vacuolar degradation.[3][6][9][12][14][19][35][55] The M20 family of metalloproteases encompasses proteins from bacteria to humans that share a conserved mechanism of zinc-dependent catalysis and similar overall protein folds, despite substantial sequence divergence and specialization toward particular substrate classes.[3][6][9][12][19][35][55] Within the peptidase M20 family, CPS1 represents the vacuolar form of carboxypeptidase S, while other organisms contain related enzymes with similar substrate specificity and cellular function.[3][12][14][19] The comparison of CPS1 with carboxypeptidase CapA from Aspergillus niger reveals that fungal carboxypeptidases S show considerable conservation of substrate specificity, with both enzymes preferring hydrophobic C-terminal amino acids and exhibiting optimal catalytic activity at slightly acidic pH within the temperature range compatible with cellular metabolism.[3][12][14][19]

The mammalian carboxypeptidase A family comprises multiple members with distinct substrate specificities and cellular localizations, including CPA1 and CPA2 that participate in protein digestion in the pancreas, CPA4 that exhibits broad substrate specificity, and CPA6 that shows preference for large hydrophobic C-terminal amino acids.[6][9][35][55] Structural studies of human carboxypeptidase A combined with kinetic characterization of the substrate specificities of different CPA family members reveal that specificity differences among these enzymes correlate with variations in the architecture of the substrate-binding pocket.[6][9][35][55] Specifically, the amino acid residues that line the S1 binding pocket (which recognizes the C-terminal residue) show variation between different CPA enzymes, with hydrophobic residues in this pocket promoting cleavage of substrates with hydrophobic C-terminal amino acids.[6][9][35][55] This structure-function relationship applies broadly across the carboxypeptidase superfamily, suggesting that CPS1's specificity for glycine-containing peptides reflects specific features of its substrate-binding pocket that are distinct from those in the broader CPA family members.[6][9][35][55]

### Evolutionary Conservation of Catalytic Mechanisms

The evolutionary conservation of zinc-dependent catalytic mechanisms across carboxypeptidases from bacteria to humans attests to the fundamental utility and catalytic efficiency of this proteolytic strategy.[3][6][9][12][14][19][35][55] The metal-dependent hydrolysis mechanism evolved early in the history of life, with metallopeptidases being found in all domains of life including bacteria, archaea, and eukarya.[3][6][9][12][19][35][55][59] The conservation of catalytic mechanisms, substrate binding geometries, and even specific amino acid residues across these diverse organisms indicates that the structural scaffold for zinc-dependent proteolysis defines an optimal solution to the problem of catalyzing peptide bond hydrolysis under various cellular conditions.[3][6][9][12][19][35][55][59] CPS1, representing one specific variant of this ancient catalytic strategy, shows the characteristic features of zinc metalloproteases including zinc coordination by histidine and aspartate residues, activation of catalytic water molecules, and formation of tetrahedral intermediates during catalysis.[3][12][14][19][55]

The durability of zinc-dependent proteolytic mechanisms contrasts with the evolutionary lability of substrate specificity determinants, revealing how evolution has exploited a highly conserved catalytic scaffold to generate diverse enzymes with specialized functions.[3][6][9][12][14][19][35][55] Variations in the composition and structure of substrate-binding subsites (S1, S1', S2, etc.) create the diversity of specificity profiles observed across carboxypeptidases, with CPS1's apparent preference for glycine-containing peptides reflecting specific features of its substrate-binding pocket that likely diverged through positive selection in response to the particular protein substrates encountered in the yeast vacuole.[3][6][9][12][14][19][35][55] This pattern of conserved catalytic mechanism coupled with divergent specificity determinants represents a general principle of protease evolution that has generated the vast diversity of peptidases with specialized functions in diverse cellular contexts.

## Physiological Significance and Cellular Consequences of CPS1 Dysfunction

### Effects of CPS1 Loss on Cellular Phenotypes

The loss of CPS1 function produces measurable effects on yeast cellular phenotypes, particularly under conditions where protein degradation and amino acid recycling become metabolically important.[12][14][16][17][19][32][46][57] Yeast strains completely lacking CPS1 (cps1-null strains) show reduced growth rates under nutrient-limiting conditions, particularly when nitrogen becomes limiting, as these strains cannot efficiently degrade peptides containing the preferred CPS1 substrate motifs.[12][14][16][17][19][32][46] The growth defect becomes particularly pronounced when CPS1-null strains are simultaneously deficient in carboxypeptidase Y, indicating that the two enzymes provide overlapping but distinct proteolytic functions that become rate-limiting for growth when nitrogen restriction makes protein degradation essential.[12][14][16][17][19][32][46] The severity of growth impairment in CPS1 mutants depends substantially on the particular nutrient conditions imposed, with severe effects under nitrogen limitation but minimal effects during growth on standard complete media containing abundant nutrients.[12][14][16][17][19][32][46]

The selective toxicity of CPS1 loss under nitrogen limitation reflects the fundamental role of the enzyme in vacuolar nutrient recycling during stress conditions.[12][14][16][17][19][32][46][57] When exogenous nitrogen becomes limiting, CPS1-deficient cells activate autophagy and direct proteins to the vacuole for degradation, but the resulting peptide products undergo incomplete degradation due to the missing proteolytic activity of CPS1.[12][14][16][17][19][32][46][57] The accumulation of partially degraded peptide intermediates represents a metabolic burden, as these peptides cannot be efficiently transported across the vacuolar membrane to become available for cytosolic protein synthesis, and they cannot be further degraded to release their constituent amino acids.[12][14][16][17][19][32][46][57] This "proteolytic traffic jam" leads to inefficient nutrient recovery and reduced protein synthesis capacity, ultimately limiting the cell's ability to maintain essential protein levels and undergo the metabolic adaptations required for survival during nitrogen starvation.[12][14][16][17][19][32][46][57]

### Role of CPS1 in Maintaining Amino Acid Homeostasis

Beyond its role in routine degradation, CPS1 contributes to the maintenance of cellular amino acid homeostasis through its participation in the degradation and recycling of glutathione and related molecules containing amino acid constituents.[12][14][19][32][46] The yeast vacuole accumulates the metal-binding peptide glutathione as a strategy to sequester toxic heavy metals such as cadmium in the form of glutathione-metal conjugates, thereby detoxifying the metal and protecting cellular proteins from metal-induced damage.[12][14][19][32][46] The recycling of glutathione from these vacuolar conjugates occurs through a proteolytic pathway involving the action of vacuolar proteases, with different proteases targeting different cleavage sites within the glutathione molecule and its metal-conjugated forms.[12][14][19][32][46] CPS1, functioning as a carboxypeptidase with activity toward peptides containing hydrophobic residues, likely contributes to the degradation of glutathione-derived peptide products, although the precise pathway of glutathione recycling remains incompletely characterized.[12][14][19][32][46]

The metabolic importance of CPS1 in amino acid recycling becomes apparent in physiological contexts where cells experience heavy metal toxicity, as strains with reduced CPS1 activity (or strains deficient in both CPS1 and related proteases) show enhanced sensitivity to cadmium toxicity relative to wild-type cells.[12][14][19][32][46] The mechanistic basis for this cadmium sensitivity likely reflects impaired recycling of glutathione from vacuolar cadmium-glutathione conjugates, resulting in reduced available glutathione for biosynthesis of new glutathione molecules and formation of new metal-binding conjugates.[12][14][19][32][46] Interestingly, recent genetic evidence suggests that an alternative pathway for glutathione degradation exists through the action of cytosolic proteases including the dipeptidase Dug1 (another M20 family metalloprotease), indicating that cells possess redundant mechanisms for glutathione recycling that can partially compensate for loss of vacuolar proteolytic activity.[12][14][19][32][46]

## Conclusion and Unresolved Questions

Carboxypeptidase S represents a specialized zinc-dependent metalloprotease that functions as an integral component of the yeast vacuolar degradation machinery, contributing essential proteolytic capacity for the degradation of peptide products generated through the action of vacuolar endoproteases and for the recycling of amino acids during nutrient-limited conditions.[12][14][19][32][46] The enzyme exhibits characteristic substrate specificity preferentially directed toward peptides containing hydrophobic residues, particularly those with glycine in the penultimate position and leucine or glycine at the C-terminus, reflecting an evolutionary specialization toward particular peptide motifs likely prevalent in yeast protein degradation products.[12][14][19][32][46] CPS1 synthesis is regulated by nutrient availability, with nitrogen limitation triggering increased transcription through binding of GATA and related transcription factors to regulatory elements in the CPS1 promoter, and the protein undergoes complex post-translational processing including N-linked glycosylation and ubiquitin-dependent trafficking through the multivesicular body pathway to reach its final destination in the vacuolar lumen.[12][14][19][32][44][46][47][49] The physiological importance of CPS1 becomes apparent from genetic studies showing that CPS1 loss produces selective growth defects particularly under nitrogen-limiting conditions and during sporulation, reflecting the enzyme's role in protein degradation and amino acid recycling.[12][14][16][17][19][32][46][57]

Despite substantial progress in characterizing CPS1 structure and function, significant questions remain regarding the precise role of this enzyme in different cellular contexts and the complete substrate specificity profile under physiological conditions.[12][14][19][32][46] The extent to which CPS1 participates in degradation of specific cellular proteins targeted through selective autophagy (as opposed to bulk autophagy affecting diverse proteins) remains largely unexplored, as does the potential involvement of CPS1 in specialized proteolytic events during differentiation processes such as sporulation.[12][14][16][17][19][32][46][57] Additionally, the relative contribution of CPS1 versus other vacuolar and cytosolic proteases to the degradation of natural protein substrates in living cells remains quantitatively undefined, with most evidence deriving from in vitro studies using synthetic peptide substrates or from genetic studies showing epistatic relationships between different protease genes.[12][14][19][32][46] Future research employing contemporary proteomics approaches to comprehensively characterize the endogenous peptide substrates of CPS1 in living cells under various nutritional and stress conditions would substantially advance understanding of this enzyme's precise physiological role and may reveal unexpected substrates and cellular functions that have not yet been recognized.

## Citations

1. https://www.yeastgenome.org/locus/CPS1
2. https://www.yeastgenome.org/locus/YJL172W/go
3. https://www.nature.com/articles/s41598-021-98003-x
4. https://www.uniprot.org/uniprotkb/P27614/entry
5. https://string-db.org/network/4932.YJL172W
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC2992257/
7. https://frontend.qa.yeastgenome.org/locus/S000003708/protein
8. https://www.yeastgenome.org/locus/S000003708/homology
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC5683605/
10. https://www.tandfonline.com/doi/full/10.4161/cl.28023
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC2116205/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC4022603/
13. https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1432-1033.1991.tb15924.x
14. https://www.molbiolcell.org/doi/10.1091/mbc.E17-08-0516
15. https://microbialcell.com/researcharticles/a-cinderella-story-how-the-vacuolar-proteases-pep4-and-prb1-do-more-than-cleaning-up-the-cells-mass-degradation-processes/
16. https://www.tandfonline.com/doi/full/10.1080/15548627.2018.1545821
17. https://pubmed.ncbi.nlm.nih.gov/8511964/
18. https://www.molbiolcell.org/doi/10.1091/mbc.10.9.2879
19. https://d-scholarship.pitt.edu/16515/1/HechtETD2013.pdf
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC8862405/
21. https://www.genecards.org/cgi-bin/carddisp.pl?gene=CPS1
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC11302099/
23. https://onlinelibrary.wiley.com/doi/10.1002/humu.21406
24. https://www.proteinatlas.org/ENSG00000021826-CPS1
25. https://journals.asm.org/doi/pdf/10.1128/jb.179.17.5609-5613.1997
26. https://pubmed.ncbi.nlm.nih.gov/8416959/
27. https://www.kegg.jp/ssdb-bin/www_ssget?sci%3AB446_08655
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC3734572/
29. https://prosite.expasy.org/PDOC00613
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC4283407/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC7738762/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC9266641/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC3323777/
34. https://www.newenglandconsortium.org/carbamyl-phosphate-synthetase-i-deficiency-cps-i-deficiency
35. https://www.molbiolcell.org/content/18/7/2511.full.pdf
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC2762664/
37. https://chem.libretexts.org/Courses/Pacific_Union_College/Kinetics/09:_Enzyme_Kinetics/9.07:_The_Effect_of_pH_on_Enzyme_Kinetics
38. https://www.molbiolcell.org/doi/10.1091/mbc.e03-07-0473
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC3433913/
40. https://pubmed.ncbi.nlm.nih.gov/9553770/
41. https://pubmed.ncbi.nlm.nih.gov/7700231/
42. https://pubmed.ncbi.nlm.nih.gov/10506132/
43. https://www.yeastgenome.org/locus/S000004912
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC2767396/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC5921575/
46. https://pubs.acs.org/doi/10.1021/acs.jpcb.7b04431
47. https://www.ebi.ac.uk/interpro/entry/prosite/PS00759/
48. https://febs.onlinelibrary.wiley.com/doi/abs/10.1111/j.1432-1033.1993.tb18410.x