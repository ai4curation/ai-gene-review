---
provider: perplexity
model: sonar-deep-research
cached: true
start_time: '2025-11-03T21:38:22.531386'
end_time: '2025-11-03T21:38:22.532355'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: P20963
  gene_symbol: CD247
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 51
---

## Question

# Gene Research for Functional Annotation

Please provide a comprehensive research report on the gene CD247 (P20963) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function. 

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking for a comprehensive research report on the gene CD247 (which encodes the CD3ζ protein). Let me analyze the search results to plan my response.

Key topics to cover:
1. Basic gene information and structure
2. The CD247 protein structure and composition
3. Role in the TCR-CD3 complex
4. Signal transduction mechanisms through ITAMs
5. Molecular interactions with downstream signaling proteins
6. Assembly and stoichiometry of the TCR-CD3 complex
7. Localization and cellular distribution
8. Clinical and disease associations
9. Specialized functions in different T cell types
10. Regulatory mechanisms

Let me organize my thinking:

**Gene and Protein Basics:**
- CD247 (also known as CD3Z, CD3ζ) is located on chromosome 1 (1q22-q25)
- Encodes a 164 amino acid protein, molecular weight ~18.7 kDa
- Found in T cells and NK cells

**Primary Function:**
- CD247 is a key component of the TCR-CD3 complex
- Forms a homodimer (disulfide-linked) 
- Contains three ITAMs (immunoreceptor tyrosine-based activation motifs)
- Critical for T cell antigen receptor signaling

**Structure:**
- Contains transmembrane domain
- Has basic-rich stretch (BRS) and poly-proline regions in cytoplasmic tail
- Phospholipid-binding properties through the cytoplasmic domain

**Signal Transduction:**
- Upon TCR engagement, CD247 ITAMs are phosphorylated by Lck
- Phosphorylated ITAMs serve as docking sites for ZAP-70
- ZAP-70 activation leads to LAT phosphorylation
- Activates multiple downstream pathways: Ras-MEK-ERK, NF-κB, NFAT, AP-1
 
I'll focus on the complex's structural organization and pathological implications. The protein plays a crucial role in T cell receptor signaling through its intricate assembly and molecular interactions. Its positioning within the immune system involves precise structural configurations that enable critical cellular communication and activation processes.

The complex forms a tightly regulated multiprotein structure with specific stoichiometric relationships. Its membrane localization and interaction mechanisms are fundamental to immune cell responsiveness, with significant implications for understanding immune system disorders.

Pathologically, disruptions in CD247 can lead to profound immunological consequences. Mutations or downregulation can compromise T cell signaling, potentially triggering immunodeficiency or contributing to autoimmune conditions. The protein's sensitivity to inflammatory environments underscores its importance in maintaining immune system homeostasis.
</think>

# Comprehensive Functional Annotation of CD247: The Critical Signaling Component of the T Cell Receptor Complex

## Executive Summary

CD247, also known as CD3ζ or T-cell receptor zeta chain, encodes a 164-amino acid transmembrane protein that serves as an essential signaling component of the T cell antigen receptor-CD3 (TCR-CD3) complex. This protein is distinguished by its three immunoreceptor tyrosine-based activation motifs (ITAMs) contained within its cytoplasmic domain, making it a critical hub for signal transduction in T lymphocytes and natural killer cells[2][11][13]. The CD247 protein exists as a disulfide-linked homodimer and integrates with three CD3 chains (CD3γ, CD3δ, CD3ε) to create a multisubunit signaling apparatus that transduces antigen recognition signals across the cell membrane. Upon T cell receptor engagement by peptide-major histocompatibility complex (pMHC) molecules, CD247 undergoes phosphorylation-dependent activation that recruits the protein tyrosine kinase ZAP-70, ultimately activating downstream signaling cascades that drive T cell proliferation, cytokine production, and effector functions. Beyond its structural role in receptor assembly, CD247 exhibits dynamic conformational properties that enable ligand discrimination and fine-tuning of T cell responses. Dysregulation of CD247 expression and function is associated with cancer immunosuppression, chronic inflammatory diseases, and primary immunodeficiency disorders, making it a crucial biomarker and potential therapeutic target for immune-related pathologies.

## Molecular Structure and Genetic Organization

### Gene Organization and Chromosomal Location

The CD247 gene resides on the long arm of human chromosome 1 at the cytogenetic location 1q22-q25, specifically on the Crick (negative) strand of the DNA[13][22][34]. This genomic location has been assigned the NCBI gene identifier 919, and the gene is catalogued in the HGNC (HUGO Gene Nomenclature Committee) database as entry 1677. The CD247 gene produces at least two alternatively spliced transcript variants that encode distinct protein isoforms, with the primary isoform consisting of 164 amino acid residues[22][55]. The gene structure allows for alternative splicing events that generate variants with differing C-terminal regions, potentially affecting the composition of immunoreceptor tyrosine-based activation motifs available within specific isoforms[37][40].

### Protein Structure and Composition

The CD247 protein exhibits a canonical membrane protein architecture comprising several functionally distinct domains[2][11][13]. The protein begins with a predicted signal sequence spanning amino acids 1-21, which directs the nascent polypeptide to the endoplasmic reticulum during synthesis[3]. Following the signal sequence is a very short extracellular domain containing only nine amino acid residues that remains largely buried within the assembled TCR-CD3 complex and does not directly participate in antigen recognition[27][34]. This abbreviated extracellular region contrasts sharply with the CD3 epsilon, delta, and gamma chains, each of which contain immunoglobulin superfamily domains composed of beta-sheet structures typical of antigen recognition molecules[2][13].

The transmembrane domain of CD247, spanning amino acids approximately 31-51, contains a critical pair of acidic aspartic acid residues positioned at defined locations within the helical structure[9][25]. These acidic residues are essential for proper assembly of the CD247 homodimer and for subsequent incorporation of the ζζ dimer into the complete TCR-CD3 complex[9][25][28]. The transmembrane domains of both CD247 chains form a left-handed coiled coil structure stabilized by extensive polar contacts, creating a highly specific interface that represents only the second transmembrane dimer interface to be solved to atomic resolution[25]. The disulfide bond formed between cysteine residues at position 2 of each chain creates a covalently linked homodimer that is more stable than noncovalent dimer forms, though structural studies reveal that the covalent linkage primarily serves a stabilizing role after the proper dimer interface has already formed[25].

The cytoplasmic tail of CD247, extending from the transmembrane domain to the carboxyl terminus at position 164, represents the most functionally important region and contains remarkable structural and functional complexity[2][7][10]. This cytoplasmic domain encompasses approximately 113 amino acids densely packed with functional motifs. Most prominently, CD247 uniquely contains three complete immunoreceptor tyrosine-based activation motifs (ITAMs), each occupying roughly 26 amino acids[10][47]. ITAMs consist of conserved consensus sequences with the canonical structure YXXL/I-X₆₋₈-YXXL/I, where X represents any amino acid[2][10][47]. The three tandem ITAMs within CD247 (designated ζITAM-a, ζITAM-b, and ζITAM-c) collectively contain six tyrosine residues capable of phosphorylation, compared to the single ITAM (and thus two tyrosine residues) found in each of the CD3γ, CD3δ, and CD3ε chains[10][20][47].

Beyond the ITAM-containing regions, the CD247 cytoplasmic domain contains additional functionally important motifs[7][2]. A basic-rich stretch (BRS) sequence of positively charged residues, particularly enriched in lysine and arginine, occupies a signaling motif preceding the second ITAM[7]. This BRS region exhibits high affinity binding to phosphoinositide lipids, including phosphatidylinositol-3-phosphate (PtdIns(3)P), PtdIns(4)P, PtdIns(5)P, PtdIns(3,5)P₂, and PtdIns(3,4,5)P₃, thereby anchoring the CD247 cytoplasmic tail to the inner leaflet of the plasma membrane in resting T cells[7]. The CD247 cytoplasmic domain also contains a poly-proline rich region that can serve as a binding site for proteins containing Src homology 3 (SH3) domains, though this region shows lower affinity interactions with membranes compared to the BRS and ITAM-containing regions[7].

### Transmembrane Assembly Interface

The proper assembly of the TCR-CD3 complex depends critically on the transmembrane domain features of CD247, particularly the positioning of charged residues within the hydrophobic lipid bilayer environment[9][25][28]. Each of the two aspartic acid residues within the CD247 transmembrane domains interacts with charged residues from adjacent subunits through salt bridge formation and hydrogen bonding networks[25][28]. The CD247 homodimer interfaces with the TCRα transmembrane domain through a three-helix arrangement involving one basic TCRα residue (arginine at a defined position) and both acidic aspartic acid residues from the CD247 chains, effectively shielding these ionizable residues from the lipid bilayer interior[9][28]. This arrangement based on shielding of charged residues prevents their exposure to the hydrophobic environment, which would otherwise render proteins unstable in the membrane and subject to degradation[9]. The importance of this assembly principle is demonstrated by the finding that conservative substitutions of aspartic acid to asparagine significantly reduce complex assembly, while non-conservative substitutions entirely abolish TCR-CD3 complex formation[25][28].

## Role Within the T Cell Receptor-CD3 Complex

### Complex Architecture and Stoichiometry

The TCR-CD3 complex represents one of the most intricate membrane receptor structures known, comprising six distinct polypeptide chains organized in a highly specific stoichiometry[9][12][30]. The complex consists of one T cell receptor α/β heterodimer (in the majority of T cells expressing this receptor type) noncovalently associated with CD3γε, CD3δε, and CD3ζζ homodimers[2][11][12][30]. This 1:1:1:1 stoichiometry has been definitively established through biochemical isolation of intact radiolabeled protein complexes assembled in the endoplasmic reticulum[9][12]. Within this arrangement, the CD3γε and CD3δε heterodimers flank either side of the TCRαβ heterodimer, while the CD247-CD247 homodimer sits below the α/β heterodimer, with all components held together through both noncovalent interactions and in some cases disulfide bonding[2][11][30].

The TCRαβ heterodimer comprises two highly variable protein chains each containing two extracellular immunoglobulin domains (variable and constant regions) that together form the ligand-binding site[30][52]. Each TCR chain possesses a short cytoplasmic tail of only three amino acids, rendering the TCR structurally incapable of signal transduction on its own[2][11]. This structural inadequacy necessitates association with the invariant CD3 and CD247 chains, which contain the signaling-competent cytoplasmic domains. The physical organization of the complete TCR-CD3 complex reveals that when bound to peptide-MHC molecules, the entire complex exhibits a dimeric architecture whereby two TCR-CD3 complexes project outward from a central core formed by the CD3 and CD247 extracellular domains and transmembrane regions[30]. This ligand-dependent dimerization has important implications for signal initiation and amplification.

### Assembly Mechanism and Ordering Principles

Assembly of the TCR-CD3 complex follows a well-ordered, stepwise pathway that depends on specific interactions among transmembrane domains[9][12][28]. Early assembly stages involve the formation of CD3γ/ε and CD3δ/ε heterodimers through specific interactions between their extracellular immunoglobulin domains, with both CD3γ and CD3δ competing for binding to CD3ε through a shared binding interface[12]. These CD3 heterodimer pairs subsequently recruit TCRα and TCRβ chains respectively, establishing trimeric complexes that eventually merge following formation of the intrachain TCRα-β disulfide bond into hexameric εγβ-αδε complexes[12]. The CD247 homodimer incorporates as the final signaling module, with assembly requiring proper orientation of three basic and six acidic transmembrane residues organized into three distinct three-helix interfaces[9][28]. Each assembly step is controlled by the principle of shielding ionizable residues from the lipid environment, ensuring that only properly formed complexes remain stably integrated into the membrane[9].

The crucial role of CD247 in this assembly process is underscored by studies using CD247-deficient cell lines and organisms[14][17][56]. In CD247-deficient mice, all other TCR-CD3 components can assemble, but their cell surface expression is profoundly reduced, TCR signaling is severely impaired, and thymocyte development is substantially compromised[14][17][56]. The CD247 chain contributes a disproportionate amount of signaling capacity to the complex through its three ITAMs, providing six tyrosine phosphorylation sites compared to the two sites present in each CD3 component, for a total of ten ITAMs distributed throughout the six-chain complex[10][20][45][47].

## Biochemical Function in T Cell Activation

### Initiation of Signal Transduction Upon TCR Engagement

The primary biochemical function of CD247 is to serve as a critical link between extracellular ligand recognition by the TCRαβ chains and intracellular signaling machinery[2][11]. When the TCRαβ heterodimer engages a peptide-MHC complex displayed on an antigen-presenting cell, this binding event triggers conformational changes throughout the TCR-CD3 complex that render the ITAM tyrosine residues accessible to phosphorylation[10][2][47]. The initiation of ITAM phosphorylation requires the coordinated action of two Src family protein tyrosine kinases, Lck and Fyn[10][32]. Lck is recruited to the TCR-CD3 complex through its association with the co-receptor CD4 (on helper T cells) or CD8 (on cytotoxic T cells), which bind to non-variable regions of the MHC molecule[2][10]. This co-receptor binding brings Lck into spatial proximity with the CD247 ITAM tyrosine residues within the membrane microenvironment of the immunological synapse[10][32].

At the molecular level, Lck phosphorylates conserved tyrosine residues within each ITAM motif, converting them from tyrosine (Y) residues to phosphotyrosine (pY) residues[10][32][47]. This phosphorylation occurs in a sequential but coordinated manner across the multiple ITAMs present in the complex[10]. Importantly, the three ITAMs within CD247 are not phosphorylated simultaneously, but rather proceed through distinct phosphorylation intermediates[10]. Early in TCR stimulation, particularly at intermediate signal strengths, some ITAM tyrosines are phosphorylated while others remain unphosphorylated, generating partially phosphorylated CD247 species (notably the p21-ζ form detected by gel electrophoresis)[10][21][45]. These partially phosphorylated forms can still recruit ZAP-70 but preferentially bind inactive or weakly activated ZAP-70, potentially serving important regulatory functions[10][21][45]. Full phosphorylation of all ITAM tyrosines (generating the p23-ζ form) occurs only upon strong TCR cross-linking or stimulation with high-affinity agonist peptides[10]. This differential phosphorylation pattern provides a mechanism for ligand discrimination, allowing the immune system to distinguish between high-affinity (agonist), intermediate-affinity (weak agonist or partial agonist), and low-affinity (antagonist or null ligands) peptide-MHC complexes[10][21][45].

### Recruitment and Activation of ZAP-70 Kinase

The phosphorylated tyrosine residues within the CD247 ITAMs serve as high-affinity binding sites for the tandem SH2 domains of the ZAP-70 (zeta-chain-associated protein kinase 70) protein[2][8][10][11]. ZAP-70 preferentially binds to fully phosphorylated (or nearly fully phosphorylated) ITAM sequences, with each SH2 domain recognizing a single phosphotyrosine residue separated by one to three intervening amino acids[2][8][10]. This cooperative binding of the two ZAP-70 SH2 domains to the pYXXL sequences within an ITAM motif achieves high binding affinity and specificity[8][10]. Notably, CD247 is particularly important for ZAP-70 recruitment because it possesses multiple ITAM sites (three full ITAMs providing six phosphotyrosine sites), allowing ZAP-70 molecules to bind in tandem arrays along the CD247 cytoplasmic tail[2][11]. This multisite binding creates a concentration gradient of ZAP-70 at the membrane surface and enables cooperative recruitment of multiple ZAP-70 molecules[8][11].

Once recruited to the phosphorylated ITAMs, ZAP-70 itself becomes a substrate for Lck-mediated phosphorylation[8][10][11]. Lck phosphorylates specific tyrosine residues within the activation loop and interdomain region (particularly the interdomain between the two SH2 domains and the kinase domain) of ZAP-70, releasing an autoinhibitory conformation and converting the kinase into an actively phosphorylating enzyme[8][10]. The activated ZAP-70 kinase then phosphorylates downstream substrate proteins, most importantly the adapter protein LAT (linker for the activation of T cells)[8][11]. The positioning of CD247 and its multiple ITAMs ensures that ZAP-70 is recruited in proper spatial orientation to interact with Lck for its activation and to access its substrate proteins.

### LAT Phosphorylation and Downstream Signaling Complex Formation

ZAP-70, when recruited and activated through CD247 ITAM phosphorylation, phosphorylates nine conserved tyrosine residues within the cytoplasmic domain of the transmembrane adapter protein LAT[8][11]. Once phosphorylated, LAT serves as a scaffold protein displaying multiple tyrosine phosphorylation sites that recruit proteins bearing SH2 domains, including Grb2, Gads, and phospholipase Cγ1 (PLCγ1)[8][11][52]. This recruitment of multiple signaling molecules to LAT creates a critical signalosome platform that amplifies and diversifies downstream signaling[8][11][52]. The formation of this LAT-based signalosome initiates multiple interconnected signaling cascades that include the Ras-MEK-ERK pathway, phospholipase C activation leading to calcium mobilization, protein kinase C activation, and activation of the transcription factors NF-κB, NFAT, and AP-1[2][11][29][47].

The activation of the Ras-MEK-ERK pathway occurs through the recruitment of SOS (son of sevenless) guanine nucleotide exchange factor to LAT via the Grb2 adapter protein, leading to Ras activation and subsequent phosphorylation of the kinases MEK and ERK[26][52]. ERK phosphorylation is also promoted through a LAT-independent pathway involving the BAM32-PLCγ1-PAK1 complex that cooperates with Ras-dependent signals to fully activate ERK[26]. Phospholipase Cγ1 activation leads to the hydrolysis of phosphatidylinositol 4,5-bisphosphate (PIP₂) into diacylglycerol (DAG) and inositol 1,4,5-triphosphate (IP₃)[33][52][60]. IP₃ diffuses to the endoplasmic reticulum where it binds inositol 1,4,5-triphosphate receptors to trigger calcium release, while DAG remains membrane-bound and activates protein kinase C[33][52][60]. PKC activation leads to phosphorylation of IκB kinase, promoting the degradation of IκB and allowing nuclear translocation of NF-κB transcription factor[47][52]. Collectively, these signaling cascades culminate in the transcriptional and translational programs characteristic of T cell activation, including increased IL-2 production, upregulation of IL-2 receptors, cell cycle progression, differentiation into effector subsets, and expression of cytotoxic molecules[2][11][29][47].

## Structural Dynamics and Lipid Interactions

### Phospholipid-Dependent Conformational Switching

A sophisticated regulatory mechanism governing CD247 function involves its interactions with acidic phospholipids present in the inner leaflet of the plasma membrane[7][51][54]. In resting T cells, the CD247 cytoplasmic tail adopts a membrane-associated conformation with its basic-rich stretch and ITAM-containing regions inserted into the hydrophobic core of the lipid bilayer, rendering the critical tyrosine residues inaccessible to phosphorylation by Lck[7][54]. This resting conformation is stabilized through ionic interactions between positively charged lysine and arginine residues within the basic-rich stretches and negatively charged phosphatidylinositol lipid headgroups, particularly phosphatidylinositol 3,4,5-trisphosphate (PIP₃) and phosphatidylinositol 4,5-bisphosphate (PIP₂)[7][51][54]. The high-affinity binding of CD247 to these phosphoinositide lipids effectively sequesters the ITAM tyrosines within the membrane, preventing their phosphorylation and thus maintaining TCR signaling in the inactive state[7][54].

Upon TCR ligation by peptide-MHC, conformational changes in the extracellular TCR domain are transmitted through the transmembrane helices, inducing a lateral shift in the CD3ζ transmembrane position and promoting the dissociation of the CD247 cytoplasmic tail from the inner leaflet phospholipids[27][51][54]. This ligand-induced conformational transition exposes the ITAM tyrosine residues to the aqueous cytoplasmic environment, rendering them accessible targets for Lck-mediated phosphorylation[7][51][54]. The process represents an elegant molecular mechanism that couples extracellular antigen recognition to intracellular signaling activation. Notably, the structural studies of CD247 interacting with model lipid membranes demonstrate that the ITAM tyrosine side chains penetrate deeply into the hydrophobic acyl chain region of the lipid bilayer, while the backbone of the CD247 protein remains positioned at the interface between the lipid hydrophobic and hydrophilic regions[54]. This detailed positioning explains why phosphorylation of the membrane-embedded ITAM tyrosines is kinetically unfavorable and why dissociation from the membrane is a prerequisite for productive phosphorylation.

### Characterization of Multiple Conformational States

Advanced biophysical studies using atomic force microscopy and single-molecule force spectroscopy have revealed that CD247 exists in multiple conformational states with different degrees of "openness" of its three functional motifs (ITAM, basic-rich stretch, and poly-proline region)[54]. These conformational states arise from the heterogeneous lipid-binding properties of different regions within the CD247 cytoplasmic domain, with the two primary lipid-binding sites (BRS and the region surrounding ITAM domains) showing different affinities and kinetic properties for association and dissociation with membrane phospholipids[54]. Live-cell imaging experiments have demonstrated that different antigen stimuli (particularly stimuli of different intensities or different ligand affinities) stabilize CD247 in distinct conformational states[54]. This conformational heterogeneity provides a structural basis for the versatile signaling properties of the TCR, enabling the receptor to integrate information about ligand quantity and quality into distinct signaling outputs[54]. The conformational dynamics of CD247 represent a form of "allosteric regulation" whereby membrane lipids and extracellular ligands cooperatively control the structural state of the signaling complex.

## Alternate Splicing and Isoform-Specific Functions

### Characterization of CD247 Isoform Variants

The CD247 gene produces multiple protein isoforms through alternative splicing that affect the C-terminal region of the protein, with important consequences for ITAM composition and T cell function[37][40]. Three alternatively spliced variants have been characterized in mouse models, designated CD3ι (iota), CD3θ (theta), and CD3η (eta), which differ from the canonical CD3ζ (zeta) isoform in the C-terminal region such that the third ITAM motif is lost or substantially altered[37][40]. Detailed functional studies using retrovirus-mediated retrogenic technology, wherein specific CD247 isoforms are expressed in hematopoietic stem cells and transferred into immunodeficient mice, have revealed striking differences in how these isoforms support T cell development and activation[37][40].

Expression of the canonical CD3ζ isoform containing all three full-length ITAMs rescues normal thymic T cell development and peripheral T cell responses in CD247-deficient mice, establishing CD3ζ as fully competent for all examined T cell functions[37][40]. The CD3ι isoform, despite lacking the complete third ITAM, exhibits essentially normal T cell development and activation kinetics comparable to cells expressing CD3ζ, suggesting that the third ITAM is partially redundant or that CD3ι compensates through alternative mechanisms[37][40]. In striking contrast, mice reconstituted with CD3θ-expressing bone marrow completely fail to generate mature single-positive T cells, with development arrested at the double-negative stage, indicating that this isoform is functionally incompetent for TCR signaling[37][40]. The CD3η-expressing isoform produces a severe but less complete developmental phenotype, with thymocyte development substantially impaired, reduced TCR surface expression, decreased positive selection efficiency, and expansion of CD44-high populations expressing exhaustion markers[37][40].

Biochemical analysis of CD3η-expressing T cells reveals a selective impairment of PLCγ1 and Akt/mTOR activation following TCR stimulation, while ZAP-70 and ERK activation remain relatively intact[37][40]. This differential signaling pattern indicates that CD3η selectively disrupts certain downstream pathways while preserving others, suggesting that the third ITAM encoded specifically by CD3ζ has specialized signaling functions that cannot be fully compensated by the CD3 component ITAMs[37][40]. These observations underscore the importance of CD247 structure in supporting full T cell competence and suggest that alternative splicing of CD247 may provide a mechanism for immune regulation under specific physiological conditions.

## Cellular Localization and Membrane Organization

### Plasma Membrane Distribution and Immunological Synapse Localization

CD247, as a component of the integral TCR-CD3 membrane complex, exhibits subcellular localization exclusively at the plasma membrane of T lymphocytes and natural killer cells where it is expressed[2][11][13][22]. In resting T cells, CD247 is distributed throughout the cell surface in relatively diffuse patterns, though evidence suggests some degree of organization into membrane microdomains[2][38][41]. Upon engagement of the T cell with an antigen-presenting cell, the TCR-CD3 complex undergoes dynamic reorganization into a highly organized structure termed the immunological synapse[38][41]. The immunological synapse represents a specialized membrane domain at the T cell-antigen-presenting cell interface that concentrates TCR-CD3 complexes, signaling molecules, costimulatory receptors, and adhesion molecules into a spatially organized activation domain[38][41].

Within the immunological synapse, CD247-containing TCR-CD3 complexes accumulate in a central supramolecular activation cluster (cSMAC) surrounded by rings of adhesion molecules[38][41]. Lipid rafts, specialized membrane microdomains enriched in sphingolipids and cholesterol, accumulate at the immunological synapse and associate with TCR-CD3, costimulatory molecules like CD28, and adaptor proteins including LAT and Lck[38][41]. The recruitment of CD247-containing TCR-CD3 complexes into lipid raft-enriched synaptic regions appears critical for efficient signaling, as disruption of lipid raft organization impairs TCR-induced signaling[38][41]. Recent sophisticated imaging studies have revealed that the dynamics of CAR (chimeric antigen receptor)-mediated immune synapses depend critically on the lipid raft-association kinetics of the signaling machinery, with different costimulatory domains affecting the rate at which CAR molecules shuttle into and out of lipid raft compartments[41].

### Role in Synapse Formation and Membrane Lipid Organization

The presence of CD247 and its membrane-interactive properties contributes to proper immunological synapse formation and stability[7][38][41][51]. The phosphoinositide-binding properties of the CD247 basic-rich stretch are particularly important for directing TCR accumulation at the center of the immunological synapse[7]. Mutation of the CD247 basic-rich stretch in a manner that eliminates phosphoinositide binding significantly impairs TCR accumulation at the synaptic center while leaving proximal signaling pathways intact[7]. This indicates that phosphoinositide interactions with CD247 regulate the normal redistribution of the TCR following TCR signaling initiation and are necessary for proper spatial organization of the signaling complex[7]. The impairment of TCR redistribution, despite preserved early signaling events, suggests that CD247-lipid interactions govern the later stages of synaptic maturation and organization[7].

Computational modeling of TCR-CD3 complexes embedded in model membranes has revealed that the cytoplasmic regions of CD247 and CD3 chains undergo rapid association with the inner leaflet of the plasma membrane within the first 100 nanoseconds of simulation, forming coiled conformations that are dynamic but persistently membrane-bound[51]. These coiled conformations allow the ITAM-containing regions of CD247 to sample different spatial positions relative to the membrane, potentially facilitating interactions with membrane-anchored kinases while remaining generally inaccessible to soluble phosphatases[51]. The TCR-CD3 complex exhibits selective enrichment of certain phosphoinositide lipids, most notably PIP₂ and PIP₃, in its immediate lipid environment despite these lipids representing only 8% and 2% of membrane lipids respectively[51]. The cationic residues within the basic-rich stretches of CD3ε and CD247 dominate the interaction with these phosphoinositide lipids, creating localized domains of phosphoinositide enrichment at the TCR-CD3 locus[51].

## Clinical and Disease Associations

### Downregulation in Cancer and Chronic Inflammatory Diseases

CD247 expression undergoes selective downregulation in numerous malignant tumors and chronic inflammatory conditions, representing a key mechanism of immune escape and T cell dysfunction[5][24][31]. In ovarian cancer, comprehensive flow cytometry and immunohistochemistry studies have demonstrated that CD247 expression is significantly decreased in peripheral blood lymphocytes from cancer patients compared to healthy controls with benign ovarian cysts[5][24]. More dramatically, tumor-infiltrating lymphocytes in ovarian cancer tissue express substantially lower CD247 levels than lymphocytes from adjacent non-malignant tissue[5][24]. This selective downregulation of CD247 in tumor-infiltrating T cells correlates with impaired T cell effector functions, suggesting that the tumor microenvironment actively suppresses CD247 expression as an immune evasion strategy[5][24]. Importantly, CD247 expression levels correlate with tumor differentiation status and histological classification, and CD247⁺ tumor-infiltrating lymphocytes are significantly reduced in patients with lymph node metastasis compared to patients without metastatic spread[5][24].

The CD247 downregulation observed in ovarian cancer extends to multiple other malignancy types, including melanoma, cervical cancer, pancreatic cancer, breast cancer, and head and neck cancers[5][24][31]. In gastric cancer, oral cancer, melanoma, and esophageal cancer, higher expression of CD247 has been associated with better prognosis and improved 5-year survival rates, confirming the prognostic value of CD247 expression[24][31]. The mechanisms underlying CD247 downregulation in the tumor microenvironment remain incompletely understood but appear to involve secretion of immunosuppressive factors by tumor-associated macrophages, granulocytes, and myeloid-derived suppressor cells (MDSCs), which secrete arginase-1[5][24]. Arginase-1 enzymatic activity induces loss of CD247 expression and represents an important mechanism of T cell suppression in tumor-bearing hosts[5][24]. This understanding has prompted investigation of CD247-targeted treatment strategies as a potential approach to restore T cell function in cancer immunotherapy[5][24][31].

### Inflammatory Diseases and Autoimmune Conditions

CD247 expression is also dysregulated in chronic inflammatory conditions including HIV infection, tuberculosis, chronic hepatitis B infection, and various autoimmune diseases[31][43]. During chronic inflammation, T cell activation becomes suppressed, and this suppression is specifically associated with downregulation of CD247 while the remaining TCR-CD3 complex components (CD3δ, CD3ε, CD3γ) remain largely unaffected[2][11][14]. Notably, when inflammation is successfully treated with appropriate therapeutic interventions, CD247 levels normalize, suggesting that CD247 expression serves as a correlate for the functional status of T cell activation[2][11][14]. This observation has prompted investigation of CD247 as a potential biomarker for determining immune status and disease severity in conditions where traditional inflammation biomarkers like high-sensitivity C-reactive protein (hs-CRP) and tumor necrosis factor-alpha (TNF-α) lack T cell specificity[2][11][14].

In HIV-infected patients, CD247 downmodulation on Vγ9Vδ2 T lymphocytes appears to underlie the anergy (functional unresponsiveness) observed in this T cell population during chronic infection[31][43]. In tuberculosis patients, decreased expression of CD247 along with decreased expression of the nuclear transcription factor κB has been observed in peripheral T cells, with both markers returning to normal levels following successful antimicrobial treatment[31][43]. In chronic hepatitis B infection, deficient translocation of CD247, ZAP-70, and Grb2 to lipid raft membrane compartments has been documented as a hallmark of defective adaptive immune responses, suggesting that compartmentalization defects in addition to downregulation contribute to CD247-associated immune dysfunction[31][43].

CD247 genetic polymorphisms and epigenetic modifications have been associated with increased susceptibility to multiple autoimmune diseases[31][43][46]. Genome-wide association studies have identified CD247 as a new susceptibility locus for systemic sclerosis[31][43][46]. Polymorphisms in CD247 have been linked to type 1 diabetes and autoimmune thyroid disease in northern Swedish populations[31][43][46]. Epigenetic profiling has revealed changes in CD247 gene expression in CD4⁺ and CD8⁺ T cells from patients with Graves' disease, correlating with altered expression of genes associated with T cell receptor signaling[31][43][46]. These genetic and epigenetic associations suggest that variations in CD247 expression or function contribute to the loss of immune tolerance and T cell dysregulation characteristic of autoimmune disease pathogenesis.

### Primary Immunodeficiency Caused by CD247 Mutations

Mutations in the CD247 gene cause a rare form of severe combined immunodeficiency (SCID) designated as CD3ζ-deficiency or Immunodeficiency 25 (IMD25)[39][42]. In this autosomal recessive disorder, mutations that disrupt CD247 function result in severely impaired T and B cell development, opportunistic infections by bacteria, viruses, fungi, and protozoa, and failure to thrive[39][42][42]. Patients present before three months of age with characteristic features including low numbers of CD3⁺ T cells with very low TCR-CD3 surface expression, reduced naive T cell populations, elevated gamma-delta T cell percentages, and absent proliferative responses to mitogens[39][42]. Without adequate stem cell transplantation, CD247-deficiency SCID is fatal due to severe immunodeficiency[39][42]. The identification of CD247 mutations as a cause of SCID has illuminated the critical role of CD247 in T lymphocyte development, as defective CD247 function completely prevents proper TCR-CD3 assembly and cell surface expression, thereby blocking T cell development at early thymic stages[39][42].

## Specialized Functions in Different T Cell Populations

### Role in Intrathymic T Cell Differentiation

CD247 plays a specialized and critical role in intrathymic T cell differentiation, the developmental process whereby hematopoietic progenitors differentiate into mature, self-tolerant T lymphocytes within the thymus gland[3][6][13][16][22]. In CD247-deficient mice, thymic architecture becomes structurally abnormal, with the thymus containing primarily CD4⁻CD8⁻ (double-negative) thymocytes and TCR/CD3-very low CD4⁺CD8⁺ (double-positive) cells[14][17][56]. The progressive development from double-negative through double-positive to single-positive (CD4⁺CD8⁻ or CD4⁻CD8⁺) thymocytes occurs at profoundly reduced rates in the absence of CD247[14][17][56]. Single-positive thymocytes that do develop in CD247-deficient animals display very low surface TCR-CD3 expression and fail to respond appropriately to T cell receptor engagement signals[14][17][56]. These observations indicate that CD247 is essential for the signal transduction events that govern both the developmental progression through thymic checkpoints and the selection processes (positive and negative selection) that ensure the generation of a functional T cell repertoire[14][17][56].

### Intraepithelial Lymphocyte Maturation and Alternative Signaling

In a remarkable finding, intestinal intraepithelial lymphocytes (IELs), T cells that reside within the epithelial barrier of the small intestine and colon, exhibit a unique dependency relationship with CD247[14][56][59]. In CD247-deficient mice, while conventional thymus-derived T cells in the spleen and lymph nodes are profoundly depleted, intraepithelial lymphocytes within the intestine maintain relatively normal cell surface TCR-CD3 expression levels[14][56]. Careful immunoprecipitation experiments revealed that in CD247-deficient intestinal IELs, the TCR-CD3 complex incorporates the Fcε RI gamma-chain (the gamma-chain of the high-affinity IgE receptor), which belongs to the same gene family as CD247 and can form disulfide-linked dimers[14][49][56]. This Fcε RI gamma-chain substitution allows TCR surface expression but does not restore signaling capacity, as these cells failed to proliferate in response to TCR-specific antibodies, mitogens, or antigen stimulation despite expressing high levels of TCR[14][49][56]. These data demonstrate that intraepithelial lymphocytes mature through an alternative, extrathymic developmental pathway distinct from conventional thymic T cell development, and that while Fcε RI gamma-chain can partially substitute for CD247 in supporting TCR surface expression, it cannot replicate CD247's signaling functions[14][49][56][59].

This specialized physiology of intestinal IELs highlights the unique signaling requirements of this T cell population and suggests that CD247-dependent signaling is particularly important for TCR function in activated T cells. The observation that Fcε RI gamma-chain-expressing IELs can develop extrathymically but cannot respond to antigen underscores the importance of the multiple ITAMs within CD247 (three full ITAMs providing six tyrosine phosphorylation sites) compared to the single ITAM present in Fcε RI gamma-chain[14][49][56].

### Natural Killer Cell Expression and Function

CD247 is also expressed in natural killer cells, where it functions as part of the natural killer cell receptor complex[3][6][13][22]. In NK cells, CD247 is incorporated into signaling complexes associated with various activating and inhibitory NK receptors, where it plays analogous signal-transduction roles to its function in T cells[3][6]. The expression of CD247 in NK cells is particularly relevant for understanding how these innate lymphocytes integrate diverse activating and inhibitory signals to make decisions regarding lysis of target cells[3][6]. However, the specific details of CD247 function in NK cells and how its signaling differs from or complements the signaling of other adapter proteins like DAP12 (DNAX-activating protein of 12 kDa) in NK receptor complexes remain incompletely characterized in the available literature.

## Signaling Dynamics and ITAM Multiplicity

### Functional Significance of Multiple ITAMs

The presence of three functional ITAMs within CD247 represents a structural feature unique among the invariant signaling subunits of immune receptors and raises important questions about the specific roles of ITAM multiplicity in TCR signaling[10][20][45][48]. Research examining these questions has revealed that the ten ITAMs distributed throughout the TCR-CD3 complex (six within the two CD247 chains, plus one each in CD3γ, CD3δ, and CD3ε chains) collectively provide signal amplification, with the degree of amplification proportional to the number of engaged and phosphorylated ITAMs[10][20][45][48]. However, the mechanism of amplification appears more subtle than simple additive effects; rather, ITAM multiplicity increases the efficiency with which ligand binding is converted into intracellular signals[10][48]. Studies using transgenic mice in which all ten ITAMs have been replaced with a single ITAM sequence reveal substantial reductions in thymic cellularity and impaired CD4⁻CD8⁻ to CD4⁺CD8⁺ maturation due to low TCR expression and signaling[20]. However, remarkably, mice expressing a single ITAM sequence at all ten positions still retain some capacity for thymocyte development, indicating that ITAM diversity is not absolutely required but rather provides optimization of TCR signaling[20].

More recent evidence suggests that individual ITAM sequences have evolved specialized properties that allow discrimination between different signal contexts[45][20][48]. Specifically, the ζ-chain ITAMs (designated ζa, ζb, and ζc based on their position) appear to have distinct properties compared to the CD3 ITAMs[20][45]. The ζc ITAM appears particularly important for normal TCR signaling, as mice expressing the ζc ITAM sequence at all ten ITAM positions display near-normal TCR surface expression and signaling for both CD4 and CD8 thymocytes[20]. This finding suggests that the ζ-chain ITAMs have undergone optimization through evolution for particular signaling functions that may relate to ligand discrimination or other specialized roles[20].

### ITAM Phosphorylation Dynamics and Signal Quality

The temporal dynamics of ITAM phosphorylation have been shown to contain encoded information about ligand quality and quantity[21][45]. At early time-points following TCR stimulation with high-affinity ligands, CD247 undergoes rapid phosphorylation generating the fully phosphorylated p23-ζ form[21]. In contrast, TCR stimulation with intermediate-affinity ligands leads to the development of a plateau in the intensity and duration of fully phosphorylated CD247 p23-ζ[21]. Low-affinity ligand interactions generate only transient phosphorylation of CD247 ITAM tyrosines[21]. This differential temporal signature of ITAM phosphorylation provides a mechanism by which T cells can discriminate between ligands of different affinities even though all ligands may activate the same initial signaling cascade[21][45]. The mechanism appears to involve negative feedback regulation through recruitment of phosphatases such as SHP-1 (Src homology domain-containing protein tyrosine phosphatase 1), which dephosphorylates phosphotyrosine residues within the TCR complex[21][45]. The timing and efficiency of phosphatase recruitment depends on the signal intensity generated by the initial ITAM phosphorylation, creating a negative feedback loop that tunes the duration of signaling[21][45].

### Fine-Tuning Through SHP-1 Phosphatase Regulation

Detailed analysis of TCR affinity-dependent signaling dynamics has revealed that SHP-1 phosphatase activity negatively regulates both proximal and distal TCR signaling in an affinity-dependent manner[21]. In TCR-expressing T cell lines with engineered variations in TCR affinity (ranging from subphysiological through optimal to very high affinity), SHP-1 activity showed the most robust inhibition of ERK phosphorylation and other downstream signaling events in cells expressing very high-affinity TCRs[21]. Partial knockdown of SHP-1 using CRISPR/Cas9 technology resulted in upregulation of both phosphorylated CD247 (pCD3ζ) and phosphorylated ERK in a TCR affinity-dependent manner[21]. These results indicate that SHP-1 phosphatase is recruited to the TCR complex proportional to signal intensity, creating a negative feedback mechanism that dampens the strongest signaling responses[21]. The CD247 ITAMs appear to be particular targets of SHP-1, suggesting that dephosphorylation of CD247 tyrosine residues represents a key mechanism by which negative feedback regulates TCR signaling potency[21]. This sophisticated regulatory mechanism ensures that both weak and strong TCR signals remain within a productive signaling window and prevents the excessive activation that would otherwise result from high-affinity ligand engagement[21].

## Biomarker Applications and Therapeutic Potential

### Use as an Immune Status Biomarker

Given the selective downregulation of CD247 during chronic inflammation and its role as a correlate of T cell activation status, CD247 expression has been proposed as a potential biomarker for evaluating immune competence and disease severity in conditions characterized by T cell dysfunction[2][11][14][31]. Unlike general inflammation markers such as C-reactive protein or TNF-α that reflect systemic inflammation from multiple cell types, CD247 expression specifically indicates the functional status of T cell receptor signaling capacity[2][11][14]. This specificity makes CD247 potentially valuable for distinguishing true T cell immunosuppression from other causes of elevated inflammation markers[2][11][14]. In HIV infection, tuberculosis, and chronic viral hepatitis, measurement of CD247 levels in peripheral blood lymphocytes could provide information about the degree of T cell dysfunction and potentially allow monitoring of immune recovery following therapeutic interventions[31][43]. The normalization of CD247 levels following treatment of chronic inflammation suggests that CD247 could serve as a marker of successful immune restoration[2][11][14].

### Therapeutic Targeting of CD247

The critical role of CD247 in T cell activation and its downregulation in diseases featuring T cell suppression make CD247 an attractive therapeutic target[2][5][24][31]. One approach involves artificially increasing CD247 expression or signaling to restore T cell function in cancer or chronic infections characterized by T cell exhaustion[5][24][31]. Transgenic expression of chimeric antigen receptor containing a CD3-zeta signaling domain has been shown to recover hyporesponsive T cells to full effector functions, demonstrating the principle that enhancing CD247-based signaling can reverse T cell dysfunction[5][24]. Another therapeutic approach involves modulating CD247 phosphorylation or ITAM signaling through pharmacological means. Monoclonal antibodies directed against the TCR-CD3 complex, such as the anti-CD3 antibody OKT3, function partly through engaging CD247 and other CD3 components to deliver agonistic stimulation, and these agents remain in clinical use for certain immunological indications[30][52]. Bispecific T cell engager (BiTE) antibodies that bring T cells into contact with target cells while simultaneously engaging the TCR-CD3 complex through multiple CD247-containing complexes represent an emerging approach to achieve focal and prolonged T cell activation against specific tumor targets[47]. These and other CD247-targeted approaches represent promising avenues for future therapeutic development.

## Evolutionary Conservation and Comparative Structure

### Conservation Among Immune Receptor Families

The immunoreceptor tyrosine-based activation motif (ITAM) architecture present in CD247 represents an ancient and highly conserved feature of immune signaling that extends far beyond T cells[10][30][45][47][52]. ITAM-containing signaling subunits are found in diverse immune receptor complexes including B cell receptors, Fc receptors, NK cell receptors, and mast cell IgE receptors[10][30][45][47][52]. The conservation of this signaling architecture across such diverse receptor families indicates that the ITAM-based signal transduction mechanism represents a fundamental and essential solution to the problem of transmitting immune recognition signals across the cell membrane[10][30][45][47][52]. CD247 shares substantial sequence homology with the Fcε RI gamma-chain and other ITAM-containing adapter proteins, indicating common evolutionary origin from an ancestral immune signaling module[6][13][22][55]. The ability of Fcε RI gamma-chain to partially substitute for CD247 in allowing TCR surface expression (though without full signaling capacity) reflects this shared evolutionary heritage and structural similarity[14][49][56].

The TCR-CD3 complex architecture, with its combination of a variable antigen recognition module (TCRαβ or TCRγδ) coupled to invariant signaling modules (CD3 and CD247 chains), appears to represent the primordial design for immune antigen receptors, which was later adapted in the B cell receptor and Fc receptors[10][30][45][47][52]. This conserved architecture ensures reliable signal transduction from diverse antigen recognition structures to a stereotyped intracellular signaling cascade, providing a high degree of functional modularity in immune receptor evolution[10][30][45][47][52].

## Conclusion

CD247, encoding the T cell receptor zeta chain, represents a central molecular hub in the adaptive immune system, integrating extracellular antigen recognition by the TCRαβ or TCRγδ chains into intracellular signaling programs that govern T cell differentiation, activation, proliferation, and effector functions. Through its three immunoreceptor tyrosine-based activation motifs containing six phosphorylatable tyrosine residues, CD247 nucleates the recruitment and activation of the ZAP-70 kinase and downstream signaling complexes culminating in activation of the transcription factors NF-κB, NFAT, and AP-1[2][8][11][29][47]. The protein's sophisticated interactions with acidic phospholipids in the plasma membrane membrane provide a mechanism for differential ligand discrimination, enabling T cells to distinguish between agonist, partial agonist, and antagonist peptide-MHC complexes on the basis of signal intensity and duration[7][21][45][54]. The selective downregulation of CD247 in cancer and chronic inflammatory diseases represents a critical mechanism of immune escape and T cell dysfunction, making CD247 expression and function both an important biomarker and a promising therapeutic target[2][5][24][31][43]. Future research elucidating the precise molecular mechanisms governing CD247 activation, phosphorylation dynamics, phosphatase-mediated regulation, and isoform-specific functions will continue to yield insights into T cell biology and reveal new therapeutic opportunities for enhancing immune responses against cancer and chronic infections or restraining pathological immune responses in autoimmune disease[20][37][40][45][48].

## Citations

1. https://www.ncbi.nlm.nih.gov/gene/919
2. https://www.fortislife.com/resources/antibody-resources/cd247-cd3z-the-gatekeeper-of-t-cell-activation
3. https://go.drugbank.com/polypeptides/P20963
4. https://www.uniprot.org/uniprotkb/P20963/entry
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6940041/
6. https://pubchem.ncbi.nlm.nih.gov/protein/P20963
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC3110614/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC10525366/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC4515969/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC2869518/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC2198996/
12. https://www.abcam.com/en-us/targets/cd247/9649
13. https://pubmed.ncbi.nlm.nih.gov/8223495/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC5514760/
15. https://pubmed.ncbi.nlm.nih.gov/8223445/
16. https://www.pnas.org/doi/10.1073/pnas.2208058119
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC7592594/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC5568475/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC5694758/
20. https://www.genecards.org/cgi-bin/carddisp.pl?gene=CD247
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC3466601/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC3856398/
23. https://www.nature.com/articles/s41586-024-07439-4
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC3420808/
25. https://www.pnas.org/doi/10.1073/pnas.1420936111
26. https://onlinelibrary.wiley.com/doi/10.1111/sji.13170
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC85301/
28. https://pubmed.ncbi.nlm.nih.gov/1533389/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC2119993/
30. https://onlinelibrary.wiley.com/doi/pdf/10.1002/wmts.27
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC10872740/
32. https://pubmed.ncbi.nlm.nih.gov/15322154/
33. https://www.ncbi.nlm.nih.gov/gtr/conditions/C1857798
34. https://pubmed.ncbi.nlm.nih.gov/38117282/
35. https://www.science.org/doi/10.1126/sciadv.adq8114
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC10304095/
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC6678392/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC12058738/
39. https://onlinelibrary.wiley.com/doi/pdf/10.1111/sji.13170
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC9953819/
41. https://www.science.org/doi/10.1126/scisignal.aan1088
42. https://pubmed.ncbi.nlm.nih.gov/8805629/
43. https://www.proteinatlas.org/ENSG00000198821-CD247
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC8321403/
45. https://en.wikipedia.org/wiki/T-cell_receptor
46. https://www.nature.com/articles/cr201742
47. https://en.wikipedia.org/wiki/T-cell_surface_glycoprotein_CD3_zeta_chain
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC413941/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC8429457/
50. https://www.pnas.org/doi/10.1073/pnas.95.16.9459
51. https://pmc.ncbi.nlm.nih.gov/articles/PMC2293063/