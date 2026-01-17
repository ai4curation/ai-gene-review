---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T15:22:26.258436'
end_time: '2026-01-15T15:37:52.383001'
duration_seconds: 926.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AP3B1
  gene_symbol: AP3B1
  uniprot_accession: O00203
  protein_description: 'RecName: Full=AP-3 complex subunit beta-1; AltName: Full=Adaptor
    protein complex AP-3 subunit beta-1; AltName: Full=Adaptor-related protein complex
    3 subunit beta-1; AltName: Full=Beta-3A-adaptin; AltName: Full=Clathrin assembly
    protein complex 3 beta-1 large chain;'
  gene_info: Name=AP3B1; Synonyms=ADTB3A;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the adaptor complexes large subunit family.
  protein_domains: AP3_beta. (IPR026740); AP3B1/2_C. (IPR056314); AP3B1_Ser. (IPR029394);
    AP3B_C. (IPR029390); AP_beta. (IPR026739)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O00203
- **Protein Description:** RecName: Full=AP-3 complex subunit beta-1; AltName: Full=Adaptor protein complex AP-3 subunit beta-1; AltName: Full=Adaptor-related protein complex 3 subunit beta-1; AltName: Full=Beta-3A-adaptin; AltName: Full=Clathrin assembly protein complex 3 beta-1 large chain;
- **Gene Information:** Name=AP3B1; Synonyms=ADTB3A;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the adaptor complexes large subunit family.
- **Key Domains:** AP3_beta. (IPR026740); AP3B1/2_C. (IPR056314); AP3B1_Ser. (IPR029394); AP3B_C. (IPR029390); AP_beta. (IPR026739)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AP3B1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AP3B1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AP3B1** (gene ID: AP3B1, UniProt: O00203) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AP3B1: AP-3 Complex Subunit Beta-1

## Introduction

AP3B1 (Adaptor Related Protein Complex 3 Subunit Beta 1) encodes the beta-3A subunit of the adaptor protein complex 3 (AP-3), a heterotetrameric coat protein complex that plays a fundamental role in intracellular membrane trafficking. The protein functions as a critical component of the cellular machinery that directs cargo proteins from the trans-Golgi network (TGN) and/or endosomes to lysosomes and lysosome-related organelles (LROs) [ma-2021-ap3-vesicle-review-abstract]. The AP3B1 gene is located on human chromosome 5q14.1 and encodes a 1094 amino acid protein that is essential for proper vesicle formation and cargo sorting in essentially all cell types, with particularly important roles in specialized secretory cells including melanocytes, platelets, and neurons [genereviews-hps-summary].

The discovery that AP3B1 mutations cause Hermansky-Pudlak syndrome type 2 (HPS2) in humans, and that the pearl mouse serves as an excellent animal model for this disorder, established the physiological importance of this gene in organelle biogenesis [feng-1999-pearl-abstract]. The syndrome is characterized by a triad of oculocutaneous albinism, bleeding diathesis due to platelet storage pool deficiency, and uniquely among HPS subtypes, immunodeficiency arising from neutropenia and impaired cytotoxic lymphocyte function [omim-hps2-summary]. Understanding AP3B1 function has illuminated fundamental mechanisms of vesicular trafficking and continues to inform therapeutic approaches for HPS2 and related disorders.

## Structure of the AP-3 Complex and the Role of AP3B1

The AP-3 complex belongs to a family of five heterotetrameric adaptor protein complexes (AP-1 through AP-5) that mediate cargo selection and vesicle formation at various intracellular membrane compartments [bonifacino-2014-ap-complexes-review-abstract]. Each AP complex consists of four subunits: two large adaptins (approximately 90-130 kDa), one medium adaptin (approximately 47 kDa), and one small adaptin (approximately 17-20 kDa). For AP-3, these are the delta (δ) subunit encoded by AP3D1, the beta-3 (β3) subunit encoded by AP3B1 or AP3B2, the mu-3 (μ3) subunit encoded by AP3M1 or AP3M2, and the sigma-3 (σ3) subunit encoded by AP3S1 or AP3S2 [ma-2021-ap3-vesicle-review-abstract].

The assembled AP-3 complex adopts a structure resembling "Mickey Mouse," with a compact core ("head") formed by the N-terminal trunk domains of the large subunits along with the medium and small subunits, and two flexible "ear" appendage domains at the C-termini of the large subunits connected by hinge regions [bonifacino-2014-ap-complexes-review-abstract]. Recent cryo-electron microscopy studies have revealed that, uniquely among AP complexes, AP-3 exists in a constitutively open, active conformation, with the cargo-binding domain of the μ3 subunit conformationally free even in the soluble state [begley-2024-ap3-structure-abstract]. This contrasts with AP-1 and AP-2, which require substantial conformational changes upon membrane recruitment to expose their cargo-binding sites.

The AP3B1-encoded β3A subunit is expressed ubiquitously across tissues, forming what is termed AP-3A, while the neuron-specific β3B isoform (encoded by AP3B2) assembles into AP-3B exclusively in neurons [ma-2021-ap3-vesicle-review-abstract]. This tissue-specific distribution underlies the distinct functions of AP-3 in ubiquitous versus neuronal trafficking pathways.

The AP3B1 protein itself contains three main structural domains: an N-terminal trunk domain that contributes to the AP-3 core, a flexible hinge region, and a C-terminal ear (or appendage) domain [peden-2002-ap3-assembly-abstract]. Unlike yeast AP-3, human AP-3 subunits including β3A are predicted by AlphaFold2 to have folded ear domains at the C-termini of their disordered hinges. The hinge and ear domains of β3A are important for AP-3 function, as demonstrated by studies showing that truncation of these regions impairs cargo sorting. Interestingly, the clathrin-binding site within the β3A hinge is dispensable for AP-3 function, as a point mutation eliminating clathrin binding (β3A817AAA) provides full functional rescue of LAMP-1 sorting in AP-3-deficient cells [peden-2002-ap3-assembly-abstract]. This suggests that AP-3's ability to bind clathrin, while detectable biochemically, may not be essential for its cellular trafficking functions.

The ear domains of AP complex large subunits typically recruit accessory proteins to membrane coats. In the case of AP-3, an unusual regulatory mechanism has been discovered involving the δ-ear domain and the σ3 subunit. The ear domain of the δ subunit interacts with σ3, and this intramolecular interaction interferes with AP-3 binding to Arf1 (but not with cargo signal recognition), thereby inhibiting AP-3 membrane recruitment both in vitro and in vivo [peden-2004-ear-core-interaction-abstract]. This ear-core interaction represents a novel autoinhibitory mechanism that regulates when AP-3 engages with membranes during lysosome-related organelle biogenesis.

## Molecular Function and Cargo Recognition

The primary molecular function of the AP-3 complex, including the AP3B1 subunit, is to recognize and sort transmembrane cargo proteins bearing specific cytoplasmic sorting signals and to facilitate their incorporation into nascent transport vesicles. AP-3 recognizes two principal classes of sorting signals: tyrosine-based YXXΦ motifs (where Φ is a bulky hydrophobic amino acid) and dileucine-based [DE]XXXL[LI] motifs [shen-2013-mu3a-structure-abstract].

The YXXΦ signals are recognized by the μ3 subunit of AP-3. Crystallographic analysis of the μ3A C-terminal domain at 1.85 Å resolution revealed that YXXΦ signals bind in an extended conformation to subdomain A of μ3A, at a location similar to the corresponding binding site on the μ2 subunit of AP-2 [shen-2013-mu3a-structure-abstract]. However, μ3A binds YXXΦ signals with relatively low affinity (14-19 μM), approximately ten-fold weaker than μ2, due to fewer stabilizing interactions. Additionally, the surface electrostatic potential of μ3A is less basic than that of μ2, explaining why AP-3 preferentially associates with intracellular membranes having less acidic phosphoinositides compared to the plasma membrane where AP-2 predominates [shen-2013-mu3a-structure-abstract].

The dileucine-based [DE]XXXL[LI] signals, in contrast, are recognized by a composite binding site formed at the interface of the δ and σ3 subunits, rather than by any single subunit [bonifacino-2014-ap-complexes-review-abstract]. This dual-subunit recognition mechanism is conserved among AP-1, AP-2, and AP-3 complexes, although each recognizes slightly different variations of the consensus motif. The requirement for an acidic residue (D or E) four positions upstream of the dileucine pair is particularly important for AP-3 recognition, as demonstrated by studies showing that conservative mutations at this position eliminate AP-3 binding.

## Membrane Recruitment and Vesicle Formation

The recruitment of AP-3 to membranes is a tightly regulated process dependent on the small GTPase ADP-ribosylation factor 1 (Arf1). Foundational biochemical studies demonstrated that AP-3 association with membranes in vitro is enhanced by GTPγS (a non-hydrolyzable GTP analog) and inhibited by brefeldin A, an inhibitor of Arf1 guanine nucleotide exchange factors [ooi-1998-arf1-ap3-recruitment-abstract]. Recombinant myristoylated Arf1-GTP directly promotes AP-3 membrane association, establishing that Arf1-GTP is the primary regulator of AP-3 membrane recruitment. Among Arf family members, Arf1 is the most potent activator, with Arf3 showing weaker effects and Arf5 having minimal activity [ooi-1998-arf1-ap3-recruitment-abstract].

Recent structural studies have elucidated the stepwise mechanism of AP-3 activation and coat polymerization [begley-2024-ap3-structure-abstract]. The initial membrane recruitment is driven by Arf1-GTP binding to the δ subunit of AP-3 (rather than the β3 subunit, as occurs with AP-1). In this initially recruited conformation, AP-3 is flexibly tethered to the membrane and its cargo-binding domain remains dynamic. Upon engagement of cargo proteins, AP-3 adopts a fixed position and the complex rigidifies, which stabilizes a second Arf1-binding site on the β3 subunit. Binding of a second Arf1 molecule then provides the template for AP-3 dimerization, initiating coat polymerization [begley-2024-ap3-structure-abstract]. This mechanism elegantly links cargo sorting to coat assembly, ensuring that vesicle formation proceeds only when appropriate cargo is present.

Unlike AP-1 and AP-2, which are clearly associated with clathrin coats, the relationship between AP-3 and clathrin remains incompletely understood. While biochemical evidence demonstrates AP-3-clathrin association, AP-3 can also function in a clathrin-independent manner [ma-2021-ap3-vesicle-review-abstract]. The identification of two amphipathic helices in AP-3 (in the δ and μ3 subunits) that insert into the lipid bilayer suggests that AP-3 directly contributes to membrane deformation during coat assembly, potentially forming tubular structures on endosomal membranes without requiring classical clathrin lattices [begley-2024-ap3-structure-abstract].

## Subcellular Localization and Trafficking Pathways

The AP-3 complex localizes primarily to a tubular endosomal compartment and mediates cargo transport from these tubular endosomes to late endosomes, lysosomes, and lysosome-related organelles [bonifacino-2014-ap-complexes-review-abstract]. This localization distinguishes AP-3 from AP-1 (TGN and endosomes to lysosomes), AP-2 (plasma membrane endocytosis), AP-4 (TGN to endosomes), and AP-5 (late endosomes). Quantitative immunoelectron microscopy studies have demonstrated that only approximately 4% of AP-3 labeling appears at the trans-Golgi network, while 43% is associated with endosomal tubules, establishing that AP-3 functions primarily at endosomal compartments [thiele-2004-ap3-endosome-localization-abstract].

AP-3 recognizes and sorts a variety of lysosomal membrane proteins to their destination organelles. The most well-characterized cargo proteins include the lysosome-associated membrane proteins LAMP-1 and LAMP-2, the lysosomal integral membrane protein LIMP-II, and the tetraspanin CD63 [thiele-2004-ap3-endosome-localization-abstract]. Quantitative analysis reveals that LAMP-1 and LAMP-2 show enrichment factors of 8.5-fold and 3.6-fold respectively in AP-3-positive membrane domains. Loss of functional AP-3 leads to defects in lysosomal protein trafficking, with the most obvious phenotype being increased surface expression of these integral lysosomal membrane proteins. In AP-3-deficient cells, both LAMP-1 and CD63 display 1.8 to 3.3-fold increased surface levels and enhanced recycling back to the plasma membrane [thiele-2004-ap3-endosome-localization-abstract]. CD63 binds strongly to the μ3 subunit through its C-terminal GYEVM motif, and AP-3 is required for efficient delivery of CD63 to lysosomes via an intracellular route that bypasses early endosomes.

In melanocytes, AP-3 localizes to clathrin-coated buds on tubular early endosomes positioned near melanosomes [theriault-2001-tyrosinase-abstract]. Studies in HPS2 melanocytes lacking functional AP-3 revealed that the complex is specifically required for trafficking of tyrosinase, the rate-limiting enzyme in melanin synthesis, from endosomes to melanosomes. In AP-3-deficient cells, tyrosinase accumulates inappropriately in vacuolar and multivesicular endosomes rather than reaching melanosomes [theriault-2001-tyrosinase-abstract]. Importantly, tyrosinase-related protein 1 (TYRP1) traffics normally to melanosomes in AP-3-deficient cells, demonstrating that AP-3 mediates only a subset of the trafficking routes to melanosomes while other pathways, including the AP-1/KIF13A pathway for TYRP1, function independently [raposo-2006-hps-melanocytes-abstract].

## Cooperation with BLOC Complexes

The AP-3 complex functions in concert with biogenesis of lysosome-related organelles complexes (BLOCs), particularly BLOC-1 and BLOC-2. Physical and functional interactions between AP-3 and BLOC-1 facilitate the trafficking of cargo proteins including CD63 and TYRP1 [blazi-2006-bloc1-ap3-interaction-abstract]. The stability of the BLOC-1/AP-3 assembly is regulated by GTP, suggesting involvement of GTPases in controlling their association and dissociation cycles.

Both BLOC-1 and BLOC-2 localize to early endosome-associated tubules as determined by immunoelectron microscopy, representing previously uncharacterized components of the endosomal protein trafficking machinery [blazi-2006-bloc1-ap3-interaction-abstract]. While BLOC-1 and AP-3 cooperate in trafficking certain cargos, they also have distinct functions: AP-3 can function independently of BLOC-1, as evidenced by the more severe phenotype of AP-3/BLOC-1 double mutant mice compared to BLOC-1-deficient mice alone. Tyrosinase represents a likely cargo trafficked by the AP-3-dependent, BLOC-1-independent pathway [blazi-2006-bloc1-ap3-interaction-abstract].

## Neuronal Functions of AP-3

The brain expresses both ubiquitous (AP-3A, containing β3A encoded by AP3B1) and neuronal-specific (AP-3B, containing β3B encoded by AP3B2) forms of the AP-3 complex. Studies in mice and in vitro reconstitution experiments have demonstrated that only the neuronal form of AP-3 can generate synaptic vesicles from endosomes, despite being the minority form quantitatively in brain tissue [daniele-2001-neuronal-ap3-abstract].

In neurons, neuronal AP-3 concentrates in varicosities along axonal processes, distinct from the localization of AP-2/clathrin at synaptic terminals. Loss of neuronal AP-3 function produces neurological abnormalities including seizures, balance problems, and hearing defects, demonstrating that synaptic vesicle biogenesis from endosomes requires this specific AP-3 form [daniele-2001-neuronal-ap3-abstract]. Neuronal AP-3 is required for proper localization of synaptic vesicle proteins including zinc transporter 3 (ZnT3), chloride channel 3 (ClC-3), and vesicular monoamine transporter 2 (VMAT2) to synaptic vesicles [ma-2021-ap3-vesicle-review-abstract].

The ubiquitous AP-3A complex (containing AP3B1) also has important neuronal functions distinct from AP-3B. Analysis of subcellular distribution of AP-3 and its cargo proteins indicates that the functions of the two AP-3 complexes are distinct and divergent, with concerted nonredundant functions controlling levels of membrane proteins in synaptic vesicles [ma-2021-ap3-vesicle-review-abstract].

## Role in Lysosome-Related Organelle Biogenesis

The essential role of AP3B1 in lysosome-related organelle (LRO) biogenesis is dramatically illustrated by Hermansky-Pudlak syndrome type 2 (HPS2), which results from loss-of-function mutations in AP3B1 [omim-hps2-summary]. LROs are cell type-specific organelles that share features with conventional lysosomes but have specialized functions, including melanosomes (pigment storage in melanocytes), platelet dense granules (storage of small molecules for hemostasis), and lytic granules (storage of cytotoxic proteins in cytotoxic T lymphocytes and natural killer cells) [genereviews-hps-summary].

In melanocytes, AP-3 deficiency results in mislocalization of tyrosinase to abnormal multivesicular endosomal structures rather than melanosomes, explaining the hypopigmentation phenotype [theriault-2001-tyrosinase-abstract][raposo-2006-hps-melanocytes-abstract]. In platelets, AP3B1 mutations cause absence of dense granules, which normally store ADP, ATP, serotonin, calcium, and polyphosphate required for the second wave of platelet aggregation, resulting in bleeding diathesis [genereviews-hps-summary]. In cytotoxic lymphocytes, AP-3 deficiency disrupts trafficking of proteins required for lytic granule function, impairing cytotoxic activity against target cells [omim-hps2-summary].

## Disease Associations: Hermansky-Pudlak Syndrome Type 2

Hermansky-Pudlak syndrome type 2 (HPS2; OMIM 608233) is caused by biallelic loss-of-function mutations in AP3B1 and represents approximately 5% of all HPS cases [genereviews-hps-summary]. The syndrome was first molecularly characterized through positional cloning of the pearl mouse mutation in 1999 [feng-1999-pearl-abstract], followed by identification of human AP3B1 mutations in HPS2 patients.

HPS2 is distinguished from the other nine HPS subtypes by the presence of immunodeficiency in addition to the common features of albinism and bleeding tendency. The immunodeficiency manifests as congenital neutropenia and impaired natural killer (NK) cell and cytotoxic T lymphocyte (CTL) function [omim-hps2-summary]. The neutropenia results from defective trafficking of neutrophil elastase, which is normally transported to primary granules in an AP3-dependent manner. In the absence of functional AP3, neutrophil elastase is mislocalized and fails to function properly. NK cell and CTL cytotoxicity are impaired because lytic granules cannot properly traffic cytotoxic proteins to the immunological synapse [omim-hps2-summary].

Mutations in AP3B1 include nonsense mutations, frameshift deletions and insertions, splice site mutations affecting pre-mRNA splicing, and large genomic deletions and inversions [genereviews-hps-summary]. The pearl mouse, carrying a large internal tandem duplication in Ap3b1, remains an important model for HPS2, exhibiting hypopigmentation, platelet storage pool deficiency, and lysosomal abnormalities [feng-1999-pearl-abstract]. Mass spectrometry studies in HPS2 patients have demonstrated near-complete absence of all AP-3 complex subunits, indicating that loss of AP3B1 destabilizes the entire heterotetrameric complex.

## Evolutionary Conservation

The AP-3 adaptor complex is evolutionarily conserved across eukaryotes, with orthologs identified in organisms ranging from budding yeast (Saccharomyces cerevisiae) to Drosophila melanogaster to mammals. The complex consists of evolutionarily conserved subunits: β3, δ, μ3, and σ3, with the basic architecture and cargo-sorting functions maintained across species. In budding yeast, AP-3 carries cargo directly from the trans-Golgi to the lysosomal vacuole, while in mammals it mediates more complex trafficking through endosomal intermediates [ma-2021-ap3-vesicle-review-abstract].

The discovery that the Drosophila garnet gene encodes a protein closely related to the δ subunit of AP-3 provided early evidence for the conserved function of this complex, as garnet mutations lead to reduced eye pigmentation due to defective pigment granule biogenesis. Similarly, mutations in AP-3 subunits in mice (pearl, mocha) and humans (HPS2) all result in defects in lysosome-related organelle biogenesis, demonstrating functional conservation despite hundreds of millions of years of divergent evolution.

Despite this overall conservation, there are notable structural differences between yeast and mammalian AP-3. In yeast, the β3 and δ hinges are intrinsically disordered and lack folded ear domains, while human AP-3 subunits including β3A (AP3B1) and β3B (AP3B2) are predicted to have folded ear domains at the C-termini of their disordered hinges. The absence of ear domains in yeast AP-3 may reflect evolutionary divergence in the accessory proteins that interact with AP-3 coats in different organisms. Functional studies show that when either the β3 or δ hinge is truncated in yeast, AP-3 is recruited to the Golgi but vesicle budding is impaired and cargoes are mistargeted, demonstrating the importance of these regions across species.

## Open Questions

Despite substantial progress in understanding AP3B1 and AP-3 function, several important questions remain:

1. **Clathrin-dependent versus independent mechanisms:** While AP-3 can associate with clathrin, it also appears to function independently. The relative contributions of clathrin-dependent and clathrin-independent AP-3 trafficking to different cargo proteins and different cell types remains incompletely understood.

2. **Additional coat proteins:** VPS41, a component of the HOPS complex, has been suggested to function as an alternative coat protein with AP-3 in dense core vesicle biogenesis. The full repertoire of proteins that cooperate with AP-3 in coat formation requires further investigation.

3. **Fate of AP-3 during vesicle maturation:** The temporal dynamics of AP-3 association with and dissociation from maturing vesicles, and the regulatory mechanisms controlling this cycle, are not fully characterized.

4. **Lipid requirements:** The specific lipid composition required for AP-3 function and how lipid modifications regulate AP-3 activity at different membrane compartments needs further investigation.

5. **Therapeutic approaches:** Whether restoration of AP-3 function through gene therapy or small molecule approaches could ameliorate HPS2 phenotypes remains to be determined. Recent structural insights may facilitate development of targeted therapeutics.

6. **Tissue-specific functions:** The relative contributions of AP-3A (containing AP3B1) versus AP-3B (containing AP3B2) to different trafficking pathways in the brain and whether AP3B1 has functions beyond those attributable to the assembled AP-3 complex warrant further study.

## References

* [feng-1999-pearl-abstract] Feng L et al. (1999). The beta3A subunit gene (Ap3b1) of the AP-3 adaptor complex is altered in the mouse hypopigmentation mutant pearl, a model for Hermansky-Pudlak syndrome and night blindness. Human Molecular Genetics 8(2):323-330. PMID: 9931340. DOI: 10.1093/hmg/8.2.323. https://pubmed.ncbi.nlm.nih.gov/9931340/

* [begley-2024-ap3-structure-abstract] Begley MJ, Aragon M, Baker RW (2024). A structure-based mechanism for initiation of AP-3 coated vesicle formation. Proceedings of the National Academy of Sciences. PMID: 38895279. DOI: 10.1073/pnas.2411974121. https://pmc.ncbi.nlm.nih.gov/articles/PMC11670113/

* [theriault-2001-tyrosinase-abstract] Thériault LL et al. (2001). AP-3 Mediates Tyrosinase but Not TRP-1 Trafficking in Human Melanocytes. Molecular Biology of the Cell 12(8):2511-2520. PMID: 11452004. PMC: PMC55657. https://pmc.ncbi.nlm.nih.gov/articles/PMC55657/

* [ma-2021-ap3-vesicle-review-abstract] Ma MQ, Islam SM, Xu G, Song Y (2021). AP-3 adaptor complex-mediated vesicle trafficking. Biophysics Reports 7(5):399-415. DOI: 10.52601/bpr.2021.200051. PMC: PMC10235903. https://pmc.ncbi.nlm.nih.gov/articles/PMC10235903/

* [bonifacino-2014-ap-complexes-review-abstract] Bonifacino JS (2014). Adaptor protein complexes and intracellular transport. PMC: PMC4114066. https://pmc.ncbi.nlm.nih.gov/articles/PMC4114066/

* [blazi-2006-bloc1-ap3-interaction-abstract] Di Pietro SM et al. (2006). BLOC-1 interacts with BLOC-2 and the AP-3 complex to facilitate protein trafficking on endosomes. Molecular Biology of the Cell 17(9):4027-4038. PMID: 16837549. https://pubmed.ncbi.nlm.nih.gov/16837549/

* [daniele-2001-neuronal-ap3-abstract] (2001). The Neuronal Form of Adaptor Protein-3 Is Required for Synaptic Vesicle Formation from Endosomes. Journal of Neuroscience 21(20):8034-8044. PMID: 11588176. PMC: PMC6763874. https://pmc.ncbi.nlm.nih.gov/articles/PMC6763874/

* [genereviews-hps-summary] GeneReviews: Hermansky-Pudlak Syndrome. NCBI Bookshelf NBK1287. https://www.ncbi.nlm.nih.gov/books/NBK1287/

* [omim-hps2-summary] OMIM Entry 608233: Hermansky-Pudlak Syndrome Type 2. https://omim.org/entry/608233

* [shen-2013-mu3a-structure-abstract] Shen J et al. (2013). Structural basis for the recognition of tyrosine-based sorting signals by the μ3A subunit of the AP-3 adaptor complex. Journal of Biological Chemistry 288(16):11434-11442. PMID: 23404500. PMC: PMC3611023. DOI: 10.1074/jbc.M112.438697. https://pmc.ncbi.nlm.nih.gov/articles/PMC3611023/

* [raposo-2006-hps-melanocytes-abstract] Huizing M et al. (2006). Melanocytes Derived from Patients with Hermansky-Pudlak Syndrome Types 1, 2, and 3 Have Distinct Defects in Cargo Trafficking. Journal of Investigative Dermatology. PMC: PMC1635963. https://pmc.ncbi.nlm.nih.gov/articles/PMC1635963/

* [ooi-1998-arf1-ap3-recruitment-abstract] Ooi CE, Dell'Angelica EC, Bonifacino JS (1998). ADP-Ribosylation Factor 1 (ARF1) Regulates Recruitment of the AP-3 Adaptor Complex to Membranes. Journal of Cell Biology 142(2):391-402. PMID: 9679139. PMC: PMC2133064. https://pmc.ncbi.nlm.nih.gov/articles/PMC2133064/

* [peden-2004-ear-core-interaction-abstract] Peden AA et al. (2004). An Ear-Core Interaction Regulates the Recruitment of the AP-3 Complex to Membranes. Developmental Cell 7(4):559-569. PMID: 15469849. DOI: 10.1016/j.devcel.2004.08.020. https://pubmed.ncbi.nlm.nih.gov/15469849/

* [peden-2002-ap3-assembly-abstract] Peden AA et al. (2002). Assembly and function of AP-3 complexes in cells expressing mutant subunits. Journal of Cell Biology. PMC: PMC2199225. https://pmc.ncbi.nlm.nih.gov/articles/PMC2199225/

* [thiele-2004-ap3-endosome-localization-abstract] Thiele C, Bhullar RP et al. (2004). Localization of the AP-3 adaptor complex defines a novel endosomal exit site for lysosomal membrane proteins. Journal of Cell Biology. PMID: 15051738. PMC: PMC2172074. https://pmc.ncbi.nlm.nih.gov/articles/PMC2172074/

* NCBI Gene Database: AP3B1 adaptor related protein complex 3 subunit beta 1. Gene ID: 8546. https://www.ncbi.nlm.nih.gov/gene/8546

* UniProt Entry O00203: AP3B1_HUMAN. https://www.uniprot.org/uniprotkb/O00203/entry


## Citations

1. begley-2024-ap3-structure-abstract.md
2. blazi-2006-bloc1-ap3-interaction-abstract.md
3. bonifacino-2014-ap-complexes-review-abstract.md
4. daniele-2001-neuronal-ap3-abstract.md
5. feng-1999-pearl-abstract.md
6. genereviews-hps-summary.md
7. ma-2021-ap3-vesicle-review-abstract.md
8. omim-hps2-summary.md
9. ooi-1998-arf1-ap3-recruitment-abstract.md
10. peden-2002-ap3-assembly-abstract.md
11. peden-2004-ear-core-interaction-abstract.md
12. raposo-2006-hps-melanocytes-abstract.md
13. shen-2013-mu3a-structure-abstract.md
14. theriault-2001-tyrosinase-abstract.md
15. thiele-2004-ap3-endosome-localization-abstract.md