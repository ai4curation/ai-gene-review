---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T16:11:28.109335'
end_time: '2026-01-15T16:26:36.185608'
duration_seconds: 908.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ARCN1
  gene_symbol: ARCN1
  uniprot_accession: P48444
  protein_description: 'RecName: Full=Coatomer subunit delta; AltName: Full=Archain;
    AltName: Full=Delta-coat protein; Short=Delta-COP;'
  gene_info: Name=ARCN1; Synonyms=COPD;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the adaptor complexes medium subunit family.
  protein_domains: AP2_Mu_C_sf. (IPR036168); AP_mu_sigma_su. (IPR022775); Coatomer_dsu.
    (IPR027059); Longin-like_dom_sf. (IPR011012); MHD. (IPR028565)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P48444
- **Protein Description:** RecName: Full=Coatomer subunit delta; AltName: Full=Archain; AltName: Full=Delta-coat protein; Short=Delta-COP;
- **Gene Information:** Name=ARCN1; Synonyms=COPD;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the adaptor complexes medium subunit family.
- **Key Domains:** AP2_Mu_C_sf. (IPR036168); AP_mu_sigma_su. (IPR022775); Coatomer_dsu. (IPR027059); Longin-like_dom_sf. (IPR011012); MHD. (IPR028565)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ARCN1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ARCN1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ARCN1** (gene ID: ARCN1, UniProt: P48444) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: ARCN1 (Coatomer Subunit Delta / Delta-COP)

**Gene:** ARCN1 (Archain 1)
**UniProt Accession:** P48444
**Synonyms:** COPD, delta-COP, delta-coat protein
**Organism:** Homo sapiens (Human)
**Chromosomal Location:** 11q23.3

## Introduction and Overview

ARCN1 encodes the delta subunit of coat protein complex I (COPI), commonly referred to as delta-COP or the delta subunit of coatomer. The protein is a 57 kDa subunit of the heptameric coatomer complex, which forms the protein coat of COPI-coated vesicles involved in intracellular membrane trafficking [fuchssteiner-1996-delta-cop-architecture-abstract]. Delta-COP belongs to the adaptor complexes medium subunit family and demonstrates significant structural homology to the mu subunits of clathrin-associated adaptor protein (AP) complexes [cosson-1996-delta-zeta-cop-retrieval-abstract]. This evolutionary relationship reflects the fundamental conservation of vesicular transport mechanisms across eukaryotes.

The primary function of delta-COP is to participate in the formation of COPI-coated vesicles that mediate retrograde transport from the Golgi apparatus to the endoplasmic reticulum (ER), as well as intra-Golgi transport between cisternae [popoff-2011-copi-budding-golgi-abstract]. This retrograde pathway is essential for retrieving ER-resident proteins that have escaped to the Golgi, maintaining the proper composition of ER and Golgi membranes, and recycling transport machinery components. Genetic studies in yeast have demonstrated that the delta-COP homolog (RET2) is essential for viability, and complete knockout of the gene is lethal [fuchssteiner-1996-delta-cop-architecture-abstract]. Cross-species complementation experiments have shown that bovine delta-COP can functionally substitute for yeast RET2, despite sharing only 34% sequence similarity, underscoring the deep evolutionary conservation of this protein's function [arakel-2016-delta-cop-helix-abstract].

## Structural Features and Domain Architecture

Delta-COP possesses a multi-domain architecture that reflects its diverse functional roles within the COPI coat. The protein contains three major structural regions: an N-terminal longin domain, a central region containing a critical amphipathic helix, and a C-terminal mu-homology domain (MHD) [arakel-2016-delta-cop-helix-abstract].

The N-terminal longin domain is essential for COPI function in the early secretory pathway. Functional studies using conditionally complemented yeast strains demonstrated that this domain cannot be deleted without complete loss of function [arakel-2016-delta-cop-helix-abstract]. The longin domain is thought to participate in membrane association and protein-protein interactions that are critical for coatomer assembly and function. Longin domains are found in a variety of proteins involved in vesicular trafficking and are characterized by their ability to adopt conformational changes that regulate protein activity.

A particularly significant discovery was the identification of a helix C-terminal to the longin domain that is specifically required for the retrieval of HDEL-bearing ER-luminal resident proteins [arakel-2016-delta-cop-helix-abstract]. This helix is positionally analogous to an unstructured linker in the AP2 clathrin adaptor complex that becomes helical and membrane-facing when the complex adopts its open, cargo-binding conformation. Based on its amphipathic nature, this helix may probe the membrane for lipid packing defects or mediate interactions with cargo molecules, thereby contributing to the stabilization of membrane-associated coatomer.

The C-terminal mu-homology domain (MHD) of delta-COP was crystallized at 2.15 angstrom resolution and shown to consist of two subdomains connected by unstructured linkers [dodonova-2017-copi-structure-arf1-abstract]. Structural comparison with mu subunits from clathrin adaptor complexes revealed significant differences in the positions of specific loops and beta-sheets, as well as changes in the relative positions of protein subdomains. These structural differences likely underlie the distinct cargo-binding specificities of delta-COP compared to AP complex mu subunits. Importantly, while the MHD is dispensable for core COPI function in the early secretory pathway, it participates in specific cargo recognition functions including binding to di-tryptophan (WXn[WF])-containing motifs found in proteins such as the Dsl1 tethering factor.

## Role in the COPI Coatomer Complex

The COPI coatomer is a stable heteroheptameric complex composed of seven subunits designated alpha (α), beta (β), beta-prime (β'), gamma (γ), delta (δ), epsilon (ε), and zeta (ζ)-COP [popoff-2011-copi-budding-golgi-abstract]. In yeast, these correspond to Ret1, Sec26, Sec27, Sec21, Ret2, Sec28, and Ret3, respectively. The coatomer can be conceptually divided into two subcomplexes that structurally and functionally resemble the inner and outer layers of clathrin-coated vesicles.

The F-subcomplex (adaptor-like subcomplex) consists of beta, gamma, delta, and zeta-COP subunits and is structurally homologous to tetrameric clathrin adaptor complexes (APs) [dodonova-2017-copi-structure-arf1-abstract]. Within this subcomplex, delta-COP is the structural homolog of the AP mu subunit, while zeta-COP corresponds to the sigma subunit. The B-subcomplex (cage-like subcomplex) comprises alpha, beta-prime, and epsilon-COP subunits and forms the outer coat layer analogous to the clathrin cage.

Two-hybrid analysis and immunoprecipitation experiments have identified specific pairwise interactions between coatomer subunits: alpha and epsilon-COPs; beta and delta-COPs; gamma and zeta-COPs; and alpha and beta'-COPs [fuchssteiner-1996-delta-cop-architecture-abstract]. The beta-delta interaction is particularly important as it positions delta-COP within the adaptor subcomplex and contributes to the overall architectural integrity of coatomer. Recent cryo-electron tomography studies at 9 angstrom resolution, combined with a 2.57 angstrom crystal structure of the beta-delta-COP complex, have provided detailed molecular insights into how these subunits assemble [dodonova-2017-copi-structure-arf1-abstract].

Unlike COPII-coated vesicles, where coat assembly occurs through sequential recruitment of inner and outer layer components, the entire COPI coatomer complex is recruited en bloc to membranes by activated Arf1-GTP [popoff-2011-copi-budding-golgi-abstract]. The structural studies revealed that Arf1 occupies two distinct molecular environments within the assembled coat. One Arf1 population (gamma-Arf1) is positioned at the center of the coat triad and is accessible to ArfGAP proteins that regulate GTP hydrolysis and coat disassembly. The other population (beta-Arf1) contacts both beta-COP and delta-COP subunits and is positioned such that it is unlikely to be directly regulated by ArfGAP [dodonova-2017-copi-structure-arf1-abstract]. The delta-COP helices directly contact Arf1's switch regions, helping to stabilize the GTP-bound active state.

## Cargo Recognition and Sorting Signals

Delta-COP participates in cargo recognition through multiple mechanisms, reflecting the diverse sorting signals recognized by the COPI coat. The best-characterized COPI cargo signals are C-terminal dilysine motifs (KKxx and KxKxx) that target type I transmembrane proteins for retrieval from post-ER compartments back to the ER [jackson-2012-dilysine-recognition-abstract]. However, dilysine motif recognition is primarily mediated by the WD-repeat domains of alpha-COP and beta'-COP rather than delta-COP. Structural studies have shown that these subunits contain acidic patches that form electrostatic contacts with the basic lysine residues of the cargo motifs.

Delta-COP, together with beta-COP, mediates recognition of a distinct class of sorting signals: arginine (R)-based ER localization signals [michelsen-2007-cargo-binding-beta-delta-abstract]. These signals are found on unassembled subunits of multimeric membrane proteins and function in quality control by retaining incompletely assembled complexes in the ER. Mutational analysis identified two highly conserved stretches within beta-COP (residues 318-338) and delta-COP (residues 388-413) that are required for R-based signal recognition. Importantly, combining mutations in both subunits abolished R-based signal recognition while leaving dilysine signal recognition intact, demonstrating that these are functionally separable cargo-binding sites [michelsen-2007-cargo-binding-beta-delta-abstract]. Homology modeling revealed that the binding site for R-based signals in the COPI adaptor trunk occupies the same structural position that recognizes YXXΦ signals in clathrin adaptor complexes, reflecting the evolutionary relationship between these coat systems.

The mu-homology domain of delta-COP also recognizes tryptophan-based motifs, particularly di-tryptophan sequences of the form WXn(1-6)[WF] [ren-2009-dsl1-tethering-abstract]. This cargo-binding specificity is important for interactions with the Dsl1 tethering complex at the ER membrane, as discussed below. Crystal structures of the yeast delta-COP MHD in complex with WxW and WxxF peptides (PDB: 5FJW, 5FJX) have revealed the molecular basis for this recognition.

## Subcellular Localization and Trafficking Routes

Delta-COP localizes to the cytoplasm and to Golgi membranes, where it is found predominantly in COPI-coated transport vesicles and in the budding regions of Golgi cisternae [fuchssteiner-1996-delta-cop-architecture-abstract]. The protein is a peripheral membrane protein that associates with the cytoplasmic face of membranes through recruitment of the entire coatomer complex by membrane-bound Arf1-GTP.

The COPI-mediated transport pathway encompasses several routes within the early secretory pathway [popoff-2011-copi-budding-golgi-abstract]. The primary function is retrograde transport from the Golgi to the ER, which serves to retrieve ER-resident proteins bearing KDEL (or HDEL in yeast) retrieval signals, recycle transport machinery including SNARE proteins and cargo receptors, and maintain the distinct protein and lipid compositions of ER and Golgi membranes. COPI vesicles also mediate intra-Golgi transport in both anterograde and retrograde directions, which is thought to contribute to Golgi cisternal maturation.

In the currently accepted model, COPI vesicles may form from multiple compartments including the ER-Golgi intermediate compartment (ERGIC), anterograde carriers moving toward the Golgi, and Golgi cisternae themselves. These vesicles can traffic to various destinations: from trans- to medial-Golgi, from medial- to cis-Golgi, from cis-Golgi to ERGIC, and from ERGIC back to the ER. The retrograde pathway is essential for maintaining the steady-state localization of resident proteins in each compartment.

## Tethering, Uncoating, and Membrane Fusion

A critical aspect of COPI vesicle function involves their recognition by tethering factors at the target membrane, followed by uncoating and membrane fusion. At the ER membrane, COPI-coated vesicles are captured by the Dsl1 tethering complex, a three-subunit complex belonging to the CATCHR (complexes associated with tethering containing helical rods) family [ren-2009-dsl1-tethering-abstract].

The Dsl1 complex forms a tower-like structure approximately 20 nm in height, with the Sec39 and Tip20 subunits forming the base anchored to ER SNAREs, and the Dsl1 subunit positioned at the top featuring a flexible lasso containing coatomer-binding motifs [ren-2009-dsl1-tethering-abstract]. Biochemical studies demonstrated that the central acidic domain of Dsl1, which contains tryptophan residues, binds directly to delta-COP [andag-2003-dsl1-copi-abstract]. Remarkably, Dsl1 uses the same domain to interact with both delta-COP and alpha-COP, employing a dual-specificity mechanism similar to accessory factors of clathrin coats.

The binding of Dsl1 to COPI subunits involves sites that are also used for internal coatomer interactions, leading to a model where Dsl1 binding promotes coat disassembly while simultaneously tethering the vesicle [andag-2003-dsl1-copi-abstract]. This dual function ensures that vesicle uncoating is coupled to appropriate targeting, preventing premature coat loss. The Dsl1 complex also accelerates SNARE complex formation in vitro, directly facilitating the membrane fusion step. Yeast mutants with defects in Dsl1/SNARE complex function accumulate large clusters of COPI-coated vesicles, demonstrating the essential nature of this tethering system for completing the retrograde transport cycle.

## Post-Translational Modifications and Regulation

Delta-COP is subject to post-translational modifications that may regulate its function within the COPI coat. Early biochemical studies demonstrated that beta-COP and delta-COP, but not other coatomer subunits, are phosphorylated on serine residues [sheff-1996-coatomer-phosphorylation-abstract]. Two-dimensional gel electrophoresis of coatomer purified from rat liver cytosol revealed considerable charge heterogeneity for delta-COP that was attributable to phosphorylation rather than distinct gene products. The functional significance of this phosphorylation was proposed to include regulation of coatomer assembly, membrane recruitment, or specificity of coatomer-organelle interactions.

Subsequent studies have implicated protein kinase A (PKA) in regulating COPI function through phosphorylation of multiple coatomer subunits. Anterograde ER-to-Golgi transport leads to PKA-mediated phosphorylation of alpha-, delta-, epsilon-, and zeta-COP, as well as actin cytoskeletal regulators [luo-2019-copi-ptm-regulation-abstract]. PKA activation by cAMP also increases binding of Arf1 to Golgi membranes, suggesting that phosphorylation coordinates coat recruitment with membrane dynamics. Beyond PKA, other kinases including Src, protein kinase C (PKC), AMPK, casein kinases, and LRRK2 have been implicated in modulating COPI trafficking through phosphorylation of coatomer components and associated proteins [luo-2019-copi-ptm-regulation-abstract].

The regulation of COPI vesicle dynamics also involves lipid-mediated mechanisms. While alpha-COP specifically binds phosphatidylinositol 3,4,5-trisphosphate (PtdIns(3,4,5)P3), the ArfGAP1 protein that triggers coat disassembly contains lipid-packing sensor motifs (ALPS) that sense membrane curvature. As membrane curvature increases toward that of a transport vesicle, ArfGAP1-catalyzed GTP hydrolysis in Arf1 and subsequent COPI coat disassembly accelerate dramatically. Additionally, the late stages of COPI vesicle fission require specific lipid geometries, with phosphatidic acid (PA) and diacylglycerol (DAG) with shortened acyl chains promoting membrane scission. These lipid requirements highlight how membrane biophysics and coat protein dynamics are intimately linked during vesicle biogenesis.

## Disease Associations and Physiological Consequences

Heterozygous loss-of-function mutations in ARCN1 cause a clinically recognizable syndrome designated short stature-micrognathia syndrome (SSMG; OMIM 617164) [izumi-2016-arcn1-craniofacial-abstract]. Affected individuals present with severe micrognathia, microcephalic dwarfism, rhizomelic (proximal limb) shortening, and mild developmental delay. Additional features may include intrauterine growth restriction, preterm birth, genitourinary malformations in males, and transient liver dysfunction with glycosylation abnormalities during illness. The phenotypic spectrum ranges from severe embryonic lethality to milder presentations without intellectual disability.

Functional studies have elucidated the molecular mechanisms underlying the disease. CRISPR/Cas9 genome editing experiments demonstrated that biallelic ARCN1 mutations are incompatible with cell survival, confirming that complete loss of function is lethal [izumi-2016-arcn1-craniofacial-abstract]. In patient-derived fibroblasts and siRNA knockdown models, reduced ARCN1 expression triggers the ER stress response, as evidenced by upregulation of ATF4, DDIT3 (CHOP), and HSPA5 (BiP). Critically, ARCN1 deficiency causes intracellular accumulation of type I collagen with reduced secretion, directly linking the COPI trafficking defect to the skeletal phenotype. The phenotypic resemblance to Stickler syndrome (a collagenopathy) supports the model that impaired collagen secretion underlies the craniofacial and skeletal manifestations.

The nur17 mouse, generated by ENU mutagenesis, carries a missense mutation (I422T) in Arcn1 that causes both coat color dilution and progressive cerebellar ataxia [xu-2010-nur17-mouse-abstract]. This mouse model provided the first direct demonstration of the physiological consequences of impaired ARCN1 function in mammalian tissues in vivo. Nur17 mice exhibit progressive Purkinje cell degeneration beginning around 2 months of age, with electron microscopy revealing abnormal protein accumulation in dendrites, ER stress marker (CHOP) accumulation, and neurofibrillary tangles. The coat color phenotype results from impaired maturation and glycosylation of Tyrp1, a melanosome protein, indicating altered ER-Golgi trafficking in melanocytes. Transgenic expression of wild-type Arcn1 completely rescued all phenotypes, confirming causality.

These disease studies highlight the essential role of delta-COP in human development, particularly for skeletogenesis (through collagen secretion), brain growth and neuronal maintenance (through protein quality control and trafficking), and pigmentation (through melanosome biogenesis).

Beyond genetic disease, COPI components including delta-COP have been identified as host dependency factors for various viral pathogens. Genome-wide RNAi screens consistently identify COPI subunits as required for the replication of influenza virus, enterovirus 71, chikungunya virus, and human papillomavirus (HPV). Delta-COP knockdown specifically reduces viral replication and blocks viral entry and trafficking to late endosomes. These findings underscore the broad cellular requirements for COPI-mediated transport and suggest that the vesicular trafficking pathway is a common target exploited by intracellular pathogens. Additionally, shRNA library screens have identified ARCN1 as a potential cancer therapeutic target, as its depletion preferentially inhibits growth of cancer cells compared to normal cells, possibly reflecting the heightened dependency of rapidly proliferating cells on efficient secretory pathway function.

## Open Questions

Several important questions remain regarding delta-COP function and regulation:

1. **Isoform-specific functions:** Multiple COPI coatomer isoforms exist due to alternative gamma-COP and zeta-COP paralogs. How delta-COP functions differentially within these isoforms, and whether isoform-specific localization to different Golgi cisternae influences cargo specificity, remains incompletely understood.

2. **Membrane curvature sensing:** The amphipathic helix C-terminal to the longin domain may sense membrane curvature or lipid packing defects. The precise mechanism by which this helix contributes to HDEL-receptor retrieval and whether it plays a role in vesicle budding or scission deserves further investigation.

3. **Cargo selectivity mechanisms:** While R-based signal recognition by beta/delta-COP has been characterized, the full repertoire of cargo recognized specifically by delta-COP versus other coatomer subunits is not completely defined.

4. **Tissue-specific requirements:** The nur17 mouse shows particular vulnerability of Purkinje neurons and melanocytes. Understanding why certain cell types are more sensitive to partial delta-COP dysfunction could reveal tissue-specific trafficking requirements.

5. **Therapeutic approaches:** For ARCN1-related syndrome, understanding whether pharmacological chaperones, ER stress modulators, or other interventions could ameliorate symptoms would have clinical significance.

6. **Regulation of delta-COP:** While serine phosphorylation of delta-COP has been documented, the specific phosphorylation sites, the kinases and phosphatases responsible, and the functional consequences of individual phosphorylation events remain to be fully characterized.

7. **Interplay with COPII:** How COPI and COPII coordinate at ER exit sites and ERGIC, and whether delta-COP participates in any cross-talk between these systems, requires further study.

## References

1. **fuchssteiner-1996-delta-cop-architecture-abstract**
   Faulstich D, Auerbach S, Orci L, et al. Architecture of coatomer: molecular characterization of delta-COP and protein interactions within the complex. *J Cell Biol.* 1996;135(1):53–61. PMID: 8858162. DOI: 10.1083/jcb.135.1.53

2. **cosson-1996-delta-zeta-cop-retrieval-abstract**
   Cosson P, Démollière C, Hennecke S, Duden R, Letourneur F. Delta- and zeta-COP, two coatomer subunits homologous to clathrin-associated proteins, are involved in ER retrieval. *EMBO J.* 1996;15(8):1792–1798. PMID: 8617224. PMCID: PMC450095

3. **izumi-2016-arcn1-craniofacial-abstract**
   Izumi K, Brett M, Nishi E, et al. ARCN1 Mutations Cause a Recognizable Craniofacial Syndrome Due to COPI-Mediated Transport Defects. *Am J Hum Genet.* 2016;99(2):451–459. PMID: 27476655. DOI: 10.1016/j.ajhg.2016.06.011

4. **xu-2010-nur17-mouse-abstract**
   Xu X, Kedlaya R, Higuchi H, et al. Mutation in Archain 1, a Subunit of COPI Coatomer Complex, Causes Diluted Coat Color and Purkinje Cell Degeneration. *PLoS Genet.* 2010;6(5):e1000956. PMID: 20502676. DOI: 10.1371/journal.pgen.1000956

5. **arakel-2016-delta-cop-helix-abstract**
   Arakel EC, Richter KP, Clancy A, Schwappach B. δ-COP contains a helix C-terminal to its longin domain key to COPI dynamics and function. *Proc Natl Acad Sci USA.* 2016;113(25):6916-21. PMID: 27298352. DOI: 10.1073/pnas.1603544113

6. **michelsen-2007-cargo-binding-beta-delta-abstract**
   Michelsen K, Schmid V, Metz J, et al. Novel cargo-binding site in the β and δ subunits of coatomer. *J Cell Biol.* 2007;179(2):209–217. PMID: 17954604. DOI: 10.1083/jcb.200704142

7. **dodonova-2017-copi-structure-arf1-abstract**
   Dodonova SO, Aderhold P, Kopp J, et al. 9Å structure of the COPI coat reveals that the Arf1 GTPase occupies two contrasting molecular environments. *eLife.* 2017;6:e26691. PMID: 28621666. DOI: 10.7554/eLife.26691

8. **popoff-2011-copi-budding-golgi-abstract**
   Popoff V, Adolf F, Brügger B, Wieland F. COPI Budding within the Golgi Stack. *Cold Spring Harb Perspect Biol.* 2011;3(11):a005231. PMID: 21844168. DOI: 10.1101/cshperspect.a005231

9. **andag-2003-dsl1-copi-abstract**
   Andag U, Schmitt HD. Dsl1p, an essential component of the Golgi-endoplasmic reticulum retrieval system in yeast, uses the same sequence motif to interact with different subunits of the COPI vesicle coat. *J Biol Chem.* 2003;278(51):51722-34. PMID: 14504276. DOI: 10.1074/jbc.M308740200

10. **ren-2009-dsl1-tethering-abstract**
    Ren Y, Yip CK, Tripathi A, et al. A Structure-Based Mechanism for Vesicle Capture by a Multi-Subunit Tethering Complex. *Cell.* 2009;139(6):1119–1129. PMID: 20005805. DOI: 10.1016/j.cell.2009.11.002

11. **jackson-2012-dilysine-recognition-abstract**
    Jackson LP, Lewis M, Kent HM, et al. Molecular Basis for Recognition of Dilysine Trafficking Motifs by COPI. *Dev Cell.* 2012;23(6):1255-62. PMID: 23177648. DOI: 10.1016/j.devcel.2012.10.017

12. **sheff-1996-coatomer-phosphorylation-abstract**
    Sheff D, Lowe M, Kreis TE, Mellman I. Biochemical heterogeneity and phosphorylation of coatomer subunits. *J Biol Chem.* 1996;271(12):7230-7236. PMID: 8636162. DOI: 10.1074/jbc.271.12.7230

13. **luo-2019-copi-ptm-regulation-abstract**
    Luo PM, Boyce M. Directing Traffic: Regulation of COPI Transport by Post-translational Modifications. *Front Cell Dev Biol.* 2019;7:190. PMID: 31572722. DOI: 10.3389/fcell.2019.00190


## Citations

1. andag-2003-dsl1-copi-abstract.md
2. arakel-2016-delta-cop-helix-abstract.md
3. cosson-1996-delta-zeta-cop-retrieval-abstract.md
4. dodonova-2017-copi-structure-arf1-abstract.md
5. fuchssteiner-1996-delta-cop-architecture-abstract.md
6. izumi-2016-arcn1-craniofacial-abstract.md
7. jackson-2012-dilysine-recognition-abstract.md
8. luo-2019-copi-ptm-regulation-abstract.md
9. michelsen-2007-cargo-binding-beta-delta-abstract.md
10. popoff-2011-copi-budding-golgi-abstract.md
11. ren-2009-dsl1-tethering-abstract.md
12. scoville-2007-arcn1-complement-abstract.md
13. sheff-1996-coatomer-phosphorylation-abstract.md
14. xu-2010-nur17-mouse-abstract.md