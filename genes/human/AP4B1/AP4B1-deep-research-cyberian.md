---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T15:53:27.141863'
end_time: '2026-01-15T16:11:24.077822'
duration_seconds: 1076.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AP4B1
  gene_symbol: AP4B1
  uniprot_accession: Q9Y6B7
  protein_description: 'RecName: Full=AP-4 complex subunit beta-1 {ECO:0000305}; AltName:
    Full=AP-4 adaptor complex subunit beta; AltName: Full=Adaptor-related protein
    complex 4 subunit beta-1; AltName: Full=Beta subunit of AP-4; AltName: Full=Beta4-adaptin;'
  gene_info: Name=AP4B1 {ECO:0000312|HGNC:HGNC:572};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the adaptor complexes large subunit family.
  protein_domains: AP_beta. (IPR026739); AP_complex_bsu_1_2_4. (IPR016342); ARM-like.
    (IPR011989); ARM-type_fold. (IPR016024); B-adaptin_app_sub_C. (IPR015151)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9Y6B7
- **Protein Description:** RecName: Full=AP-4 complex subunit beta-1 {ECO:0000305}; AltName: Full=AP-4 adaptor complex subunit beta; AltName: Full=Adaptor-related protein complex 4 subunit beta-1; AltName: Full=Beta subunit of AP-4; AltName: Full=Beta4-adaptin;
- **Gene Information:** Name=AP4B1 {ECO:0000312|HGNC:HGNC:572};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the adaptor complexes large subunit family.
- **Key Domains:** AP_beta. (IPR026739); AP_complex_bsu_1_2_4. (IPR016342); ARM-like. (IPR011989); ARM-type_fold. (IPR016024); B-adaptin_app_sub_C. (IPR015151)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AP4B1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AP4B1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AP4B1** (gene ID: AP4B1, UniProt: Q9Y6B7) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AP4B1: Comprehensive Research Report on the Beta-1 Subunit of Adaptor Protein Complex 4

## Introduction and Summary

AP4B1 (Adaptor Related Protein Complex 4 Subunit Beta 1) encodes the beta-1 subunit of the adaptor protein complex 4 (AP-4), a heterotetrameric protein complex essential for intracellular membrane trafficking. The AP4B1 gene is located on chromosome 1p13.2 and produces a 739-amino acid protein with a molecular mass of approximately 83 kDa [dellangelica-1999-ap4-discovery-abstract]. The protein contains characteristic structural features including an N-terminal trunk region, a solvent-accessible hinge region, and a C-terminal ear (appendage) domain with high alpha-helical content [frazier-2016-tepsin-binding-abstract].

The AP-4 complex was discovered in 1999 through independent efforts by Dell'Angelica et al. and Hirst et al., who identified it as the fourth member of the adaptor protein complex family [dellangelica-1999-ap4-discovery-abstract][hirst-1999-ap4-characterization-abstract]. Unlike AP-1, AP-2, and AP-3, which function as clathrin-associated adaptors, AP-4 operates independently of clathrin and represents a distinct functional class within the adaptor protein family [park-guo-2014-ap-review-abstract]. The primary function of AP4B1, as part of the AP-4 complex, is to mediate the sorting and transport of specific transmembrane cargo proteins from the trans-Golgi network (TGN) to endosomes, the peripheral cytoplasm, and the basolateral membrane in polarized cells. Loss-of-function mutations in AP4B1 cause Spastic Paraplegia 47 (SPG47), a severe childhood-onset neurological disorder characterized by intellectual disability, progressive spasticity, and characteristic brain abnormalities [abou-jamra-2011-ap4b1-mutation-abstract].

## Gene Expression and Evolutionary Conservation

AP4B1 exhibits ubiquitous tissue expression with a 2.5-kb transcript detectable in all examined tissues; a minor 6-kb species appears in some tissues [dellangelica-1999-ap4-discovery-abstract]. Northern blot analysis confirms expression in all fetal and adult brain structures, and Western blot analysis demonstrates a protein of approximately 83 kDa that partitions as both a cytosolic and peripheral membrane protein [abou-jamra-2011-ap4b1-mutation-abstract]. Immunohistochemistry shows general cytoplasmic expression with a granular pattern reflecting association with the trans-Golgi network.

The AP-4 complex shows a distinctive evolutionary distribution among eukaryotes. While humans, mice, and the plant Arabidopsis thaliana possess all four AP complexes (AP-1 through AP-4), commonly used invertebrate model organisms including Drosophila melanogaster, Caenorhabditis elegans, Saccharomyces cerevisiae, and Schizosaccharomyces pombe have lost AP-4 and retain only AP-1, AP-2, and AP-3 [boehm-2001-adaptins-review-abstract]. This patchy distribution has historically limited experimental study of AP-4 function. Phylogenetic analyses indicate that AP-3 represents the basal complex, followed by AP-5, AP-4, and subsequently AP-1 and AP-2 [boehm-2001-adaptins-review-abstract]. Zebrafish (Danio rerio) have retained AP-4, making them a valuable model system for studying AP-4 function and the pathophysiology of AP-4 deficiency syndrome, with CRISPR-edited zebrafish showing phenotypes resembling human AP-4 deficiency.

## Structure of the AP-4 Complex and the Role of AP4B1

The AP-4 complex is composed of four subunits that assemble into an obligate heterotetramer: epsilon (ε, encoded by AP4E1), beta-4 (β4, encoded by AP4B1), mu-4 (μ4, encoded by AP4M1), and sigma-4 (σ4, encoded by AP4S1) [hirst-1999-ap4-characterization-abstract]. The complex architecture follows the general organization of AP complexes, with two large subunits (ε and β4), one medium subunit (μ4), and one small subunit (σ4). These subunits form a compact core with protruding hinge and ear domains that are crucial for cargo binding, accessory protein recruitment, and membrane association [park-guo-2014-ap-review-abstract].

The AP4B1-encoded β4 subunit is one of the two large subunits and shares structural homology with beta subunits of other AP complexes, although it is notably smaller than AP1B1, AP2B1, and AP3B1, appearing to lack most of the C-terminal hinge and/or ear domain found in its paralogs [dellangelica-1999-ap4-discovery-abstract]. The predicted AP4B1 protein contains several conserved motifs shared with other AP beta subunits, including a WIIGEY motif at amino acid position 500 and a KKLVYLY motif near the N-terminus. Structural analyses have revealed that the β4 appendage domain possesses only a C-terminal platform subdomain, lacking the N-terminal sandwich subdomain characteristic of AP-1 and AP-2 beta appendages [frazier-2016-tepsin-binding-abstract].

A critical function of the β4 subunit is its interaction with tepsin (also known as ENTHD2), the only known AP-4-specific accessory protein. Frazier et al. demonstrated that tepsin contains a conserved peptide motif ([GS]LFXG[ML]X[LV]) in its unstructured C-terminal region that binds specifically to the β4 ear domain [frazier-2016-tepsin-binding-abstract]. This interaction occurs at a conserved hydrophobic surface on the β4-ear platform fold, with critical residues I669, A670, and Y682 on β4 mediating the binding. The tepsin-β4 interaction has a dissociation constant of approximately 2.9 μM and exhibits 1:1 stoichiometry. Importantly, tepsin also binds to the ε subunit through a separate motif, creating bivalent interactions that may enable cross-linking of multiple AP-4 heterotetramers and contribute to AP-4 coat assembly [frazier-2016-tepsin-binding-abstract].

## AP-4 Complex Assembly and the AAGAB Chaperone

Recent work has revealed that AP-4 complex assembly is not spontaneous but requires assistance from the chaperone protein AAGAB (alpha- and gamma-adaptin-binding protein, also known as p34). Mattera et al. demonstrated that AAGAB directly binds to the ε and σ4 subunits of AP-4 and stabilizes both endogenous and recombinant AP-4 subunits by preventing their proteasomal degradation [mattera-2022-aagab-chaperone-abstract]. AAGAB-knockout cells exhibit reduced levels of AP-4 subunits and accumulation of ATG9A at the TGN, phenocopying the hallmarks of AP-4 deficiency. These findings establish AAGAB as a critical factor in AP-4 biogenesis, with implications for understanding both normal AP-4 function and potential therapeutic targets for AP-4 deficiency syndrome [mattera-2022-aagab-chaperone-abstract].

## Subcellular Localization and Membrane Recruitment

AP-4 localizes to the trans-Golgi network (TGN) and adjacent tubulovesicular membranes, as demonstrated by immunofluorescence microscopy showing a pattern of discrete perinuclear dots in HeLa cells [hirst-1999-ap4-characterization-abstract]. Unlike the clathrin-associated AP complexes, AP-4 does not colocalize with clathrin-coated structures, indicating its function in a distinct, clathrin-independent trafficking pathway [park-guo-2014-ap-review-abstract].

The membrane recruitment of AP-4 is regulated by the small GTPase ARF1 (ADP-ribosylation factor 1). Boehm et al. demonstrated that brefeldin A (BFA) treatment, which inhibits ARF-guanine nucleotide exchange factors, causes redistribution of AP-4 from the TGN to the cytosol, confirming ARF-dependence [boehm-2001-ap4-arf-abstract]. The molecular mechanism involves direct interactions between ARF1 and both the ε and μ4 subunits of AP-4. The ε subunit binds exclusively to the GTP-bound form of ARF1 through interactions with the switch I and switch II regions, providing high-affinity, regulated binding. In contrast, the μ4 subunit binds ARF1 regardless of nucleotide status and is less dependent on switch region residues, providing constitutive, low-affinity binding [boehm-2001-ap4-arf-abstract]. This dual-interaction mechanism suggests a novel mode of ARF1-adaptor interaction, where μ4 may mediate initial membrane sampling and ε enables GTP-dependent stabilization of AP-4 at the TGN.

## Cargo Recognition and Sorting Function

The primary function of AP-4 is to sort specific transmembrane cargo proteins into transport vesicles at the TGN for delivery to post-Golgi destinations. The μ4 subunit serves as the principal cargo-binding component, recognizing specific sorting signals in the cytoplasmic tails of cargo proteins. AP-4 recognizes a distinct type of tyrosine-based sorting signal with the consensus sequence YXXØE, where Ø represents a bulky hydrophobic residue [burgos-2010-app-sorting-abstract][mattera-2017-atg9a-export-abstract].

The best-characterized AP-4 cargoes include:

**ATG9A (Autophagy-related protein 9A)**: ATG9A is the sole multispanning transmembrane protein in the core autophagy machinery and has emerged as the major cargo of AP-4 [mattera-2017-atg9a-export-abstract][davies-2018-ap4-vesicles-abstract]. ATG9A interacts with AP-4 through a conserved YQRLE motif in its N-terminal cytosolic tail. AP-4 facilitates the export of ATG9A from the TGN to peripheral cellular compartments, including endosomes and sites of autophagosome formation. In AP-4-deficient cells, ATG9A accumulates at the TGN and is depleted from the peripheral cytoplasm, with whole-cell ATG9A protein levels increased 3-5 fold compared to controls [behne-2020-ap4-deficiency-abstract]. This mislocalization impairs autophagosome biogenesis and LC3B lipidation.

**APP (Amyloid Precursor Protein)**: Burgos et al. demonstrated that the YKFFE sequence in APP's cytosolic tail binds to the μ4 subunit of AP-4 [burgos-2010-app-sorting-abstract]. X-ray crystallographic analysis revealed that this signal binds to a site on μ4 distinct from the canonical YXXØ-binding site on μ2, representing a novel signal-adaptor interaction. AP-4 mediates the transport of APP from the TGN directly to early endosomes. Disruption of this interaction shifts APP distribution back to the TGN and enhances γ-secretase-mediated cleavage, increasing production of pathogenic amyloid-β peptide, suggesting AP-4 may have protective effects against amyloidogenesis [burgos-2010-app-sorting-abstract].

**SERINC1 and SERINC3**: Proteomic studies identified these multipass transmembrane proteins as AP-4 cargoes [davies-2018-ap4-vesicles-abstract]. Both proteins colocalize with ATG9A and exhibit altered localization in AP-4-deficient cells. Notably, SERINC proteins function as HIV-1 restriction factors and have lipid scramblase activity; their trafficking by AP-4 may have implications for membrane lipid asymmetry at target compartments.

**DAGLB (Diacylglycerol Lipase Beta)**: A landmark 2022 study by Davies et al. identified DAGLB as an AP-4 cargo protein with significant implications for neuronal development [davies-2022-daglb-endocannabinoid-abstract]. DAGLB is a serine lipase that hydrolyzes diacylglycerol (DAG) to generate 2-arachidonoylglycerol (2-AG), the most abundant endocannabinoid in the brain. During normal development, DAGLB is targeted to the axon where 2-AG signaling through CB1 and CB2 cannabinoid receptors drives axonal growth and guidance. In AP-4-deficient cells, DAGLB accumulates at the TGN and axonal DAGLB levels are reduced in patient neurons. Consequently, 2-AG levels are reduced by approximately 30% in the brains of AP-4 knockout mice, accompanied by a 20% reduction in arachidonic acid levels. This discovery establishes a new pathogenic mechanism in AP-4 deficiency syndrome: spatial dysregulation of endocannabinoid signaling contributing to axon growth defects [davies-2022-daglb-endocannabinoid-abstract].

**Glutamate Receptors**: Matsuda et al. demonstrated that AP-4 mediates the polarized sorting of AMPA-type glutamate receptors (AMPARs) and delta-2 glutamate receptors to the somatodendritic domain of neurons [matsuda-2008-ampa-receptor-abstract]. AP-4 binds to transmembrane AMPAR regulatory proteins (TARPs), facilitating selective trafficking. In AP-4β-/- neurons, TARPs and AMPA receptors mislocalize to axons and accumulate in autophagosomes, while NMDA receptors and metabotropic glutamate receptors remain properly localized, indicating the existence of AP-4-dependent and AP-4-independent sorting mechanisms.

**Sortilin and Lysosomal Receptors**: Recent work by Majumder et al. showed that AP-4 regulates the trafficking of Sortilin (SORT1) from the TGN to endo-lysosomes in neurons [majumder-2022-lysosome-abstract]. In AP-4-depleted neurons, Sortilin is retained in the TGN, leading to impaired trafficking of lysosomal enzymes including Cathepsin L and PPT-1. This results in lysosomes with compromised composition and function.

## Role in Polarized Trafficking

A significant function of AP-4 is mediating polarized protein sorting in both epithelial cells and neurons. Simmen et al. demonstrated that AP-4 binds to cytosolic signals known to mediate basolateral transport in epithelial cells [simmen-2002-basolateral-abstract]. When μ4 levels were depleted in MDCK cells, several basolateral proteins were mis-sorted to the apical surface, establishing AP-4 as a participant in basolateral sorting pathways.

In neurons, AP-4 is essential for maintaining the polarized distribution of proteins between somatodendritic and axonal compartments. Loss of AP-4 function results in the mislocalization of multiple proteins to the axonal compartment, including AMPA receptors, TARPs, delta-2 glutamate receptors, and low-density lipoprotein receptors [matsuda-2008-ampa-receptor-abstract]. This aberrant sorting leads to accumulation of these proteins in axonal autophagosomes and contributes to the neurological pathology observed in AP-4 deficiency.

## Connection to Autophagy Pathways

The identification of ATG9A as a major AP-4 cargo has established a clear link between AP-4 function and the autophagy pathway. ATG9A functions as a lipid scramblase and is essential for autophagosome biogenesis, cycling between the TGN and peripheral sites including phagophores and autophagosomes [mattera-2017-atg9a-export-abstract]. AP-4 promotes the signal-mediated export of ATG9A from the TGN to the peripheral cytoplasm, where ATG9A-positive vesicles congregate near autophagosomes and serve as the membrane reservoir for autophagosome expansion.

In AP-4-deficient cells, the failure to properly deliver ATG9A to peripheral sites leads to dysregulated autophagy. Mattera et al. demonstrated that AP-4 knockout cells exhibit impaired LC3B-II/LC3B-I conversion ratios and abnormal morphology of LC3B-positive structures [mattera-2017-atg9a-export-abstract]. Davies et al. further showed that RUSC2, an AP-4 accessory protein, facilitates the transport of AP-4-derived, ATG9A-positive vesicles from the TGN to the cell periphery via interactions with kinesin motors [davies-2018-ap4-vesicles-abstract].

The connection between AP-4 and autophagy is particularly relevant in neurons, where axonal autophagy is crucial for protein homeostasis and neuronal health. De Pace et al. demonstrated that in AP-4ε knockout mice, ATG9A is retained at the TGN and depleted from axons, leading to impaired autophagosome formation and accumulation of protein aggregates including mutant huntingtin [depace-2018-atg9a-mouse-abstract]. This "congenital disorder of autophagy" mechanism may contribute significantly to the neurodegeneration observed in AP-4 deficiency syndrome.

## Disease Associations: Spastic Paraplegia 47 (SPG47) and AP-4 Deficiency Syndrome

Loss-of-function mutations in AP4B1 cause Spastic Paraplegia 47 (SPG47), an autosomal recessive neurological disorder first described by Abou Jamra et al. in 2011 [abou-jamra-2011-ap4b1-mutation-abstract]. SPG47 is part of the broader "AP-4 deficiency syndrome," which encompasses four clinically similar conditions caused by mutations in any of the four AP-4 subunit genes: SPG47 (AP4B1), SPG50 (AP4M1), SPG51 (AP4E1), and SPG52 (AP4S1). The clinical similarity across these conditions reflects the fact that loss of any single subunit renders the entire AP-4 complex nonfunctional.

The clinical features of SPG47 have been comprehensively characterized by Ebrahimi-Fakhari et al. [ebrahimi-fakhari-2018-spg47-clinical-abstract]. Core manifestations include early developmental delay with motor delay (100%), intellectual disability (100%), neonatal or infantile hypotonia that progresses to spasticity (100%), severely delayed or absent speech development (94%), progression to spastic diplegia (89%), and loss of independent walking (88%). Approximately 73% of patients show thin corpus callosum on neuroimaging, 67% have delayed myelination or white matter loss, and 40% exhibit ventriculomegaly. A characteristic MRI signature includes thinning of the splenium of the corpus callosum, absent or thin anterior commissure, and the distinctive "ears of the grizzly bear sign" caused by signal abnormalities in the forceps minor.

The pathophysiology of AP-4 deficiency involves multiple mechanisms stemming from impaired cargo trafficking. The working model proposes that: (1) AP-4 is required for proper trafficking of ATG9A and other cargoes from the TGN; (2) loss-of-function variants lead to cargo accumulation at the TGN and depletion from peripheral/axonal compartments; (3) in the case of ATG9A, this impairs axonal autophagy; (4) reduced autophagy capacity leads to protein aggregate accumulation and axonal degeneration [behne-2020-ap4-deficiency-abstract][depace-2018-atg9a-mouse-abstract]. Additionally, the missorting of Sortilin impairs lysosome biogenesis [majumder-2022-lysosome-abstract], mislocalization of glutamate receptors may contribute to neuronal dysfunction [matsuda-2008-ampa-receptor-abstract], and reduced axonal DAGLB leads to impaired endocannabinoid signaling and axon growth defects [davies-2022-daglb-endocannabinoid-abstract].

Mouse models of AP-4 deficiency recapitulate key features of the human disease, including motor deficits, thin corpus callosum, and widespread axonal swellings throughout the central nervous system [depace-2018-atg9a-mouse-abstract]. Transmission electron microscopy reveals axonal swellings containing accumulations of membrane cisternae, organelles, and autophagosomes, consistent with impaired protein clearance mechanisms.

## Therapeutic Perspectives

Several therapeutic approaches are being investigated for AP-4 deficiency syndrome. Gene therapy represents a rational strategy given the loss-of-function nature of the disease. Preclinical studies have demonstrated that delivery of AAV9 vectors expressing human AP4B1 (AAV9/hAP4B1) into the cisterna magna of SPG47 mouse models leads to widespread gene transfer and restoration of multiple disease hallmarks. High-content screening has also identified small molecules that can partially restore ATG9A trafficking in patient-derived cells, providing proof-of-concept for pharmacological approaches.

An additional therapeutic avenue has emerged from the identification of DAGLB as an AP-4 cargo. Davies et al. demonstrated that treating patient-derived neurons with ABX-1431, a monoacylglycerol lipase (MGLL) inhibitor that prevents 2-AG degradation, rescued neurite growth defects [davies-2022-daglb-endocannabinoid-abstract]. This finding suggests that pharmacological modulation of endocannabinoid metabolism could provide symptomatic benefit in AP-4 deficiency syndrome, representing a more tractable therapeutic target than gene replacement.

## Open Questions

Several important questions remain regarding AP4B1 and AP-4 function:

1. **Complete cargo inventory**: While ATG9A, APP, SERINCs, DAGLB, and glutamate receptors have been identified as AP-4 cargoes, the complete repertoire of AP-4 cargo proteins remains incompletely defined. Additional cargoes may be relevant to disease pathophysiology.

2. **Tissue-specific functions**: Although AP-4 is ubiquitously expressed, the severe neurological phenotype of AP-4 deficiency suggests particular importance in neurons. The molecular basis for this neuronal selectivity is not fully understood.

3. **Tepsin function**: The precise role of tepsin in AP-4-mediated trafficking remains unclear. Whether tepsin functions as a structural component, a cargo adaptor, or both requires further investigation.

4. **Mechanism of coat assembly**: How AP-4 forms coats on vesicles in the absence of clathrin is poorly understood. The role of tepsin-mediated cross-linking of AP-4 complexes in this process requires elucidation.

5. **Relationship to other neurodegenerative diseases**: The connection between AP-4 deficiency and enhanced amyloid pathology observed in mouse models suggests potential relevance to Alzheimer's disease. The extent to which AP-4 dysfunction contributes to other neurodegenerative conditions warrants investigation.

6. **Compensatory mechanisms**: Why some cargo proteins are properly sorted in AP-4-deficient cells while others are mislocalized suggests the existence of parallel sorting pathways. Understanding these alternative mechanisms may reveal therapeutic targets.

7. **Long-term efficacy of gene therapy**: While preclinical gene therapy studies show promise, long-term efficacy and optimal timing of intervention (given the early-onset nature of SPG47) remain to be determined.

8. **Developmental vs. degenerative contributions**: The relative contributions of developmental defects (e.g., impaired endocannabinoid signaling during axon growth) versus progressive neurodegeneration (e.g., impaired autophagy) to the clinical phenotype require further clarification.

## References

1. **[abou-jamra-2011-ap4b1-mutation-abstract]** Abou Jamra R, Philippe O, Raas-Rothschild A, et al. Adaptor protein complex 4 deficiency causes severe autosomal-recessive intellectual disability, progressive spastic paraplegia, shy character, and short stature. Am J Hum Genet. 2011;88(6):788-795. DOI: 10.1016/j.ajhg.2011.04.019. PMID: 21620353.

2. **[behne-2020-ap4-deficiency-abstract]** Behne R, Teinert J, Wimmer M, et al. Adaptor protein complex 4 deficiency: a paradigm of childhood-onset hereditary spastic paraplegia caused by defective protein trafficking. Hum Mol Genet. 2020;29(2):320-334. DOI: 10.1093/hmg/ddz310. PMID: 31915823. PMCID: PMC7001721.

3. **[boehm-2001-ap4-arf-abstract]** Boehm M, Aguilar RC, Bonifacino JS. Functional and physical interactions of the adaptor protein complex AP-4 with ADP-ribosylation factors (ARFs). EMBO J. 2001;20(22):6265-6276. DOI: 10.1093/emboj/20.22.6265. PMID: 11707398. PMCID: PMC125733.

4. **[boehm-2001-adaptins-review-abstract]** Boehm M, Bonifacino JS. Adaptins: the final recount. Mol Biol Cell. 2001;12(10):2907-2920. DOI: 10.1091/mbc.12.10.2907. PMID: 11598180. PMCID: PMC60143.

5. **[burgos-2010-app-sorting-abstract]** Burgos PV, Mardones GA, Rojas AL, et al. Sorting of the Alzheimer's Disease Amyloid Precursor Protein Mediated by the AP-4 Complex. Dev Cell. 2010;18(3):425-436. DOI: 10.1016/j.devcel.2010.01.015. PMID: 20230749. PMCID: PMC2841041.

6. **[davies-2018-ap4-vesicles-abstract]** Davies AK, Itzhak DN, Edgar JR, et al. AP-4 vesicles contribute to spatial control of autophagy via RUSC-dependent peripheral delivery of ATG9A. Nat Commun. 2018;9(1):3958. DOI: 10.1038/s41467-018-06172-7. PMID: 30262884. PMCID: PMC6160451.

7. **[davies-2022-daglb-endocannabinoid-abstract]** Davies AK, Alecu JE, Ziegler M, et al. AP-4-mediated axonal transport controls endocannabinoid production in neurons. Nat Commun. 2022;13:1058. DOI: 10.1038/s41467-022-28609-w. PMID: 35217685. PMCID: PMC8881493.

8. **[dellangelica-1999-ap4-discovery-abstract]** Dell'Angelica EC, Mullins C, Bonifacino JS. AP-4, a novel protein complex related to clathrin adaptors. J Biol Chem. 1999;274(11):7278-7285. DOI: 10.1074/jbc.274.11.7278. PMID: 10066790.

9. **[depace-2018-atg9a-mouse-abstract]** De Pace R, Skirzewski M, Bhonsle-Deeng L, et al. Altered distribution of ATG9A and accumulation of axonal aggregates in neurons from a mouse model of AP-4 deficiency syndrome. PLOS Genet. 2018;14(4):e1007363. DOI: 10.1371/journal.pgen.1007363. PMID: 29698489. PMCID: PMC5940238.

10. **[ebrahimi-fakhari-2018-spg47-clinical-abstract]** Ebrahimi-Fakhari D, Cheng C, Dies K, et al. Clinical and genetic characterization of AP4B1-associated SPG47. Am J Med Genet A. 2018;176(2):311-318. DOI: 10.1002/ajmg.a.38561. PMID: 29193663.

11. **[frazier-2016-tepsin-binding-abstract]** Frazier MN, Davies AK, Voehler M, et al. Molecular Basis for the Interaction Between AP4 β4 and its Accessory Protein, Tepsin. Traffic. 2016;17(4):400-415. DOI: 10.1111/tra.12375. PMID: 26756312. PMCID: PMC4805503.

12. **[hirst-1999-ap4-characterization-abstract]** Hirst J, Bright NA, Rous B, Robinson MS. Characterization of a Fourth Adaptor-related Protein Complex. Mol Biol Cell. 1999;10(8):2787-2802. DOI: 10.1091/mbc.10.8.2787. PMID: 10436028. PMCID: PMC25515.

13. **[majumder-2022-lysosome-abstract]** Majumder P, Edmison D, Rodger C, et al. AP-4 regulates neuronal lysosome composition, function, and transport via regulating export of critical lysosome receptor proteins at the trans-Golgi network. Mol Biol Cell. 2022;33(12):ar102. DOI: 10.1091/mbc.E21-09-0473. PMID: 35976706. PMCID: PMC9635302.

14. **[mattera-2017-atg9a-export-abstract]** Mattera R, Park SY, De Pace R, et al. AP-4 mediates export of ATG9A from the trans-Golgi network to promote autophagosome formation. Proc Natl Acad Sci USA. 2017;114(50):E10697-E10706. DOI: 10.1073/pnas.1717327114. PMID: 29180427. PMCID: PMC5740629.

15. **[mattera-2022-aagab-chaperone-abstract]** Mattera R, De Pace R, Bonifacino JS. The adaptor protein chaperone AAGAB stabilizes AP-4 complex subunits. Mol Biol Cell. 2022;33(12):ar103. DOI: 10.1091/mbc.E22-05-0177. PMID: 35976721. PMCID: PMC9635299.

16. **[matsuda-2008-ampa-receptor-abstract]** Matsuda S, Miura E, Matsuda K, et al. Accumulation of AMPA receptors in autophagosomes in neuronal axons lacking adaptor protein AP-4. Neuron. 2008;57(5):730-745. DOI: 10.1016/j.neuron.2008.02.012. PMID: 18341993.

17. **[park-guo-2014-ap-review-abstract]** Park SY, Guo X. Adaptor protein complexes and intracellular transport. Biosci Rep. 2014;34(4):e00123. DOI: 10.1042/BSR20140069. PMID: 24975939. PMCID: PMC4114066.

18. **[simmen-2002-basolateral-abstract]** Simmen T, Höning S, Ober A, et al. AP-4 binds basolateral signals and participates in basolateral sorting in epithelial MDCK cells. Nat Cell Biol. 2002;4(2):154-159. DOI: 10.1038/ncb745. PMID: 11802162.


## Citations

1. abou-jamra-2011-ap4b1-mutation-abstract.md
2. behne-2020-ap4-deficiency-abstract.md
3. boehm-2001-adaptins-review-abstract.md
4. boehm-2001-ap4-arf-abstract.md
5. burgos-2010-app-sorting-abstract.md
6. davies-2018-ap4-vesicles-abstract.md
7. davies-2022-daglb-endocannabinoid-abstract.md
8. dellangelica-1999-ap4-discovery-abstract.md
9. depace-2018-atg9a-mouse-abstract.md
10. ebrahimi-fakhari-2018-spg47-clinical-abstract.md
11. frazier-2016-tepsin-binding-abstract.md
12. hirst-1999-ap4-characterization-abstract.md
13. majumder-2022-lysosome-abstract.md
14. matsuda-2008-ampa-receptor-abstract.md
15. mattera-2017-atg9a-export-abstract.md
16. mattera-2022-aagab-chaperone-abstract.md
17. park-guo-2014-ap-review-abstract.md
18. simmen-2002-basolateral-abstract.md