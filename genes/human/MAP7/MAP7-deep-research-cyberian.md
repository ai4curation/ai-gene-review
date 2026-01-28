---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T21:46:25.058731'
end_time: '2026-01-22T22:03:37.150576'
duration_seconds: 1032.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MAP7
  gene_symbol: MAP7
  uniprot_accession: Q14244
  protein_description: 'RecName: Full=Ensconsin; AltName: Full=Epithelial microtubule-associated
    protein of 115 kDa; Short=E-MAP-115; AltName: Full=Microtubule-associated protein
    7; Short=MAP-7;'
  gene_info: Name=MAP7;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the MAP7 family. .
  protein_domains: MAP7_domain-containing. (IPR051483); MAP7_fam. (IPR008604); MAP7
    (PF05672)
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
- **UniProt Accession:** Q14244
- **Protein Description:** RecName: Full=Ensconsin; AltName: Full=Epithelial microtubule-associated protein of 115 kDa; Short=E-MAP-115; AltName: Full=Microtubule-associated protein 7; Short=MAP-7;
- **Gene Information:** Name=MAP7;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the MAP7 family. .
- **Key Domains:** MAP7_domain-containing. (IPR051483); MAP7_fam. (IPR008604); MAP7 (PF05672)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MAP7" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MAP7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MAP7** (gene ID: MAP7, UniProt: Q14244) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MAP7 (Ensconsin): A Multifunctional Microtubule-Associated Protein and Essential Kinesin-1 Cofactor

## Introduction

Microtubule-associated protein 7 (MAP7), also known as ensconsin or E-MAP-115, is a ubiquitously expressed microtubule-associated protein that plays fundamental roles in microtubule organization, motor protein regulation, and intracellular transport. The protein was first isolated and characterized from HeLa cells by Bulinski and Bossler in 1994, who named it "ensconsin" because of its remarkably tenacious binding to microtubules—the term deriving from "ensconce," meaning to settle snugly or securely [bulinski-1994-ensconsin-abstract]. Independently, the same protein was identified as E-MAP-115 (epithelial microtubule-associated protein of 115 kDa) due to its prominent expression in epithelial cells.

MAP7 has emerged as a critical regulator of the kinesin-1 motor protein, functioning not merely as a passive microtubule-binding factor but as an essential cofactor required for kinesin-1-mediated cargo transport [barlan-2013-kinesin-cofactor-abstract]. This dual function—simultaneously associating with microtubules and activating motor proteins—positions MAP7 as a key coordinator of intracellular transport systems. The protein is encoded by the MAP7 gene located at chromosome 6q23.3 in humans and belongs to a family that includes three paralogs in mammals: MAP7D1, MAP7D2, and MAP7D3, with MAP7D1 showing the highest sequence conservation to the founding member [hooikaas-2019-map7-family-abstract].

## Protein Structure and Domain Organization

Human MAP7 is a 749-amino acid protein with a predicted molecular mass of approximately 84 kDa, although it migrates anomalously at 115 kDa on SDS-PAGE due to its high content of proline and charged residues [bulinski-1994-ensconsin-abstract]. The protein is organized into three principal domains: an N-terminal domain containing the first coiled-coil region (CC1) that mediates microtubule binding, a central P domain (proline-rich region) containing numerous potential phosphorylation sites, and a C-terminal domain containing the second coiled-coil (CC2) that interacts with kinesin-1 [tymanskyj-2018-axon-morphogenesis-abstract].

The N-terminal basic region is separated from an acidic C-terminal half by a stretch of amino acids rich in proline and alanine (termed the PAPA region). The N-terminal basic domain contains the primary microtubule-binding site, and detailed structural analysis has revealed that MAP7 exhibits binding that saturates its microtubule binding sites at an approximate molar ratio of 1:6 (ensconsin:tubulin) [bulinski-1994-ensconsin-abstract]. Unlike other characterized MAPs such as tau, MAP2, and MAP4, ensconsin's binding to microtubules displays remarkable salt resistance, remaining insensitive to moderate salt concentrations up to 0.6 M, suggesting a biochemically and functionally distinct mode of microtubule interaction.

Recent structural studies using cryo-electron microscopy and NMR spectroscopy have provided atomic-level insights into how MAP7 binds microtubules. The microtubule-binding domain (MTBD) forms a 130 angstrom-long alpha helix extending from approximately residue R66 to E148 that binds along the microtubule protofilament between the outer protofilament ridge and the inter-protofilament lateral contacts [adler-2024-mtbd-structure-abstract, ferro-2022-kinesin-structure-abstract]. Importantly, both strong and weak interactions between MAP7 and the microtubule lattice extend beyond a single tubulin dimer and include the tubulin C-terminal tails, which may contribute to the protein's unusually stable microtubule association.

## Microtubule Binding and Stabilization

Early characterization established ensconsin as a potent microtubule-stabilizing protein in vitro, capable of protecting microtubules against depolymerization by cold and calcium [bulinski-1994-ensconsin-abstract]. Immunofluorescence studies demonstrated ensconsin association with most or all microtubules in human epithelial, fibroblastic, and muscle cells. However, subsequent studies using fluorescent protein-tagged E-MAP-115 revealed a more nuanced picture of its function in living cells. Faire and colleagues demonstrated that E-MAP-115 "associated with the lattice of all microtubules immediately upon polymerization and dissociated concomitant with depolymerization" [faire-1999-emap115-dynamics-abstract]. Remarkably, even when cells expressed four to ten times normal levels of the protein, microtubule dynamics remained unchanged, leading the authors to conclude that "E-MAP-115 (ensconsin) is unlikely to function as a microtubule stabilizer in vivo" under normal physiological conditions.

This apparent paradox—potent stabilization in vitro but minimal effect on dynamics in vivo—has been resolved by more recent work demonstrating context-dependent functions of MAP7. In neuronal cells, MAP7 plays a critical role in microtubule stabilization specifically at branch junctions. Studies in developing rodent sensory neurons showed that MAP7 "binds to the acetylated and stable region of individual microtubules" and creates a stable boundary that prevents depolymerization while rescuing polymerization [tymanskyj-2019-branch-retraction-abstract]. This binding property is distinct from classical microtubule stabilizers in that MAP7 does not uniformly coat microtubules but rather preferentially associates with stable, acetylated segments while avoiding the dynamic plus ends containing tyrosinated tubulin. This selective binding creates a molecular boundary that protects branch junctions from retraction during axonal development.

## Kinesin-1 Activation and Recruitment

Perhaps the most significant function of MAP7 is its role as an essential cofactor for kinesin-1-mediated intracellular transport. Groundbreaking work by Barlan and colleagues demonstrated that "kinesin-1 requires ensconsin (MAP7, E-MAP-115), a ubiquitous microtubule-associated protein, for its primary function of organelle transport" [barlan-2013-kinesin-cofactor-abstract]. Using RNAi-mediated depletion in Drosophila S2 cells, they showed that ensconsin is critical for kinesin-1-dependent transport of mitochondria, peroxisomes, and ribonucleoprotein particles. Homozygous ensconsin deletion mutants cannot survive to adulthood, and this lethality results from a requirement for ensconsin in neuronal transport.

The mechanism by which MAP7 activates kinesin-1 involves relief of the motor's autoinhibition. In the absence of cargo or activating factors, kinesin-1 exists primarily in an inactive, autoinhibited conformation where the tail domain folds back to inhibit the motor domains. Importantly, unregulated kinesin-1 mutants that bypass autoinhibition do not require ensconsin for transport, demonstrating that ensconsin functions to relieve this autoinhibited state [barlan-2013-kinesin-cofactor-abstract]. Remarkably, an ensconsin N-terminal truncation that cannot bind microtubules is sufficient to activate organelle transport by kinesin-1, indicating that the activation function is separable from microtubule binding.

The C-terminal domain of MAP7 containing the second coiled-coil (CC2) mediates interaction with the stalk region of kinesin-1. This interaction both recruits kinesin-1 to microtubules and activates its motor activity. In vitro studies by Hooikaas and colleagues demonstrated that purified MAP7 increases the microtubule landing rate and processivity of kinesin-1 through transient association with the motor [hooikaas-2019-map7-family-abstract]. All four mammalian MAP7 family members bind kinesin-1 and work redundantly in HeLa cells to enable kinesin-1-dependent transport and microtubule recruitment.

Structural studies have revealed an unexpected complexity in how MAP7 regulates kinesin-1. The microtubule-binding domain of MAP7 partially overlaps with the binding site for kinesin-1 on the microtubule surface, creating a biphasic regulatory mechanism [ferro-2022-kinesin-structure-abstract]. At low MAP7 concentrations, facilitation of kinesin-1 motility dominates because MAP7's projection domain tethers the motor to the microtubule and prevents dissociation. At saturating MAP7 concentrations, however, inhibition predominates due to reduced available binding sites on the microtubule. This concentration-dependent regulation provides a mechanism for fine-tuning motor protein activity in different cellular contexts.

## Role in Organelle Transport and Motor Protein Competition

MAP7 profoundly influences the directionality and efficiency of organelle transport. Chaudhary and colleagues demonstrated that in the absence of MAP7, isolated phagosomes move equally in both directions along microtubules [chaudhary-2019-organelle-transport-abstract]. However, MAP7 dramatically shifts transport toward the microtubule plus-end, with approximately 80% of movements becoming plus-end directed. This bias does not result from changes in individual motor force output but rather from increased binding rates of kinesin-1 motors to microtubules, allowing more motors to engage simultaneously during cargo transport.

An important aspect of MAP7 function is its competitive relationship with other microtubule-associated proteins, particularly tau. Monroy and colleagues demonstrated that MAP7 and tau "compete for binding to microtubules" with MAP7 capable of displacing tau from the microtubule lattice [monroy-2018-map-competition-abstract]. The binding affinity of MAP7 for microtubules (KD = 0.47 +/- 0.06 microM) exceeds that of tau (KD = 1.56 +/- 0.16 microM), favoring MAP7 association when both proteins are present. This competition has functional consequences for motor protein recruitment: MAP7 promotes kinesin-1-based transport while both MAP7 and tau strongly inhibit kinesin-3 activity. Neither protein affects cytoplasmic dynein motility. This differential regulation of motor proteins by competing MAPs provides a mechanism for establishing distinct transport pathways in different cellular compartments.

The spatial segregation of MAP7 and tau in neurons supports this model of competitive regulation. In both Drosophila peripheral nervous system neurons and primary mouse neuronal cultures, MAP7 localizes within both dendrites and axons, while tau is predominantly restricted to axons [monroy-2018-map-competition-abstract]. This distribution suggests that MAP competition helps dictate access to microtubules and determines the correct distribution and balance of motor activity in polarized cells.

## Neuronal Functions and Axon Morphogenesis

MAP7 plays essential roles in neuronal development, particularly in axon and branch morphogenesis. Structure-function analysis in rat embryonic sensory neurons demonstrated that different MAP7 domains serve distinct functions in neurite development [tymanskyj-2018-axon-morphogenesis-abstract]. The C-terminal kinesin-interacting domain is required for axon and branch growth but not for branch formation, while both the N and P domains, which bind microtubules with different dissociation kinetics, are required for branch formation. MAP7 localizes specifically to branch sites through its N and P domain interactions.

Developmentally, MAP7 expression is regulated during sensory neuron maturation, and perturbation of this expression alters branch formation [tymanskyj-2018-axon-morphogenesis-abstract]. The protein enters nascent branches with a characteristic delay, consistent with a role in branch maturation rather than initiation. This delayed entry correlates with its preferential binding to stable, acetylated microtubules rather than the dynamic tyrosinated microtubules at growing tips.

MAP7 also modulates organelle transport dynamics within neurons. Expression of MAP7 increases the pause frequency and promotes directional switching during kinesin-mediated mitochondrial and peroxisomal transport [tymanskyj-2018-axon-morphogenesis-abstract]. This suggests a mechanism for diverting organelles into axon branches: by recruiting kinesin-1 to microtubules at branch points and promoting pause-speed switching, MAP7 may facilitate the delivery of cellular cargo to developing branch compartments.

## Muscle Function and Nuclear Positioning

Beyond neurons, MAP7 performs critical functions in skeletal muscle. Metzger and colleagues identified ensconsin/MAP7 and kinesin heavy chain (Khc/Kif5b) as "essential, evolutionarily conserved regulators of myonuclear positioning" in both Drosophila and mammalian myotubes [metzger-2012-nuclear-positioning-abstract]. In multinucleate muscle fibers, individual nuclei must be regularly positioned throughout the cell, and improperly positioned nuclei are a hallmark of diseases including centronuclear myopathies.

The physical interaction between MAP7 and kinesin enables nuclear positioning through a mechanism involving sliding of antiparallel microtubules. MAP7 crosslinks a microtubule to the tail of kinesin-1, which then reaches toward a second, antiparallel microtubule. The motor activity slides the two microtubules apart, resulting in nuclear spreading. Expression of the Kif5b motor domain fused to the MAP7 microtubule-binding domain rescues nuclear positioning defects in MAP7-depleted cells, demonstrating that both activities—motor function and microtubule binding—are required for this process.

Drosophila larvae with mutations in ensconsin display decreased locomotion and incorrect myonuclear positioning, phenotypes that can be rescued by muscle-specific expression of ensconsin [metzger-2012-nuclear-positioning-abstract]. This establishes that proper nuclear organization directly contributes to muscle function in a cell-autonomous manner.

## Epithelial Cell Differentiation and Polarization

MAP7 was originally named E-MAP-115 to reflect its predominant expression in cells of epithelial origin. The protein plays important roles during reorganization of microtubules during epithelial cell polarization and differentiation. Expression levels increase with epithelial cell polarization and differentiation, and the protein may contribute to the formation of intercellular contacts [vanier-2003-emap115-epithelial-abstract].

In human intestinal epithelial cells, three E-MAP-115 transcript variants encode isoforms of 115, 105, and 95 kDa, with distinct expression patterns during cell maturation. Two isoforms display an expression gradient inverse to the third as Caco-2 cells progress from proliferation through differentiation stages. In vivo, these proteins are expressed in both crypt and villus epithelial cells where they concentrate at the apical pole, consistent with a role in establishing or maintaining apical-basal polarity [vanier-2003-emap115-epithelial-abstract].

## Role in Spermatogenesis

E-MAP-115/MAP7 plays a critical role in male fertility, as demonstrated by gene trap mutagenesis studies in mice. Komada and colleagues identified E-MAP-115 as a retinoic acid-inducible gene with particularly high expression in testis [komada-2000-spermatogenesis-abstract]. Male mice homozygous for a null mutation in the E-MAP-115 gene were sterile due to morphological deformation of spermatid nuclei and subsequent gradual loss of germ cells. Importantly, microtubule associations in the mutant were morphologically abnormal in two critical structures: the manchette of spermatids and in Sertoli cells.

The manchette is a transient microtubule-based structure that forms around the elongating spermatid nucleus and is essential for nuclear shaping during spermiogenesis. Sertoli cells, which provide structural and nutritional support to developing germ cells, also rely on intact microtubule networks. The observation that E-MAP-115 mutation disrupts microtubules in both cell types is consistent with the protein's role in stabilizing microtubules and suggests that this function is particularly critical in the testicular microenvironment where complex morphological transformations depend on microtubule integrity.

The connection to retinoic acid signaling is noteworthy because retinoic acid is a critical regulator of spermatogenesis, governing the differentiation of spermatogonia, meiotic entry, and the timing of sperm release. The identification of E-MAP-115 as a retinoic acid-responsive gene positions it within this regulatory network, suggesting that microtubule organization during spermatogenesis is coordinated with broader developmental signals [komada-2000-spermatogenesis-abstract].

## Wnt Signaling and Cell Migration

Recent work has revealed an unexpected connection between MAP7 family proteins and non-canonical Wnt signaling. Kikuchi and colleagues demonstrated that MAP7 and MAP7D1 form an interdependent regulatory loop with Dishevelled (Dvl), the central signal transducer in Wnt pathways [kikuchi-2018-wnt-signaling-abstract]. In HeLa cells, MAP7/7D1 bind directly to Dishevelled, direct its cortical localization, and facilitate the cortical targeting of microtubule plus-ends in response to Wnt5a signaling.

This interaction is bidirectional: Wnt5a signaling promotes MAP7/7D1 movement toward microtubule plus-ends through a mechanism involving the kinesin-1 member Kif5b, while Dishevelled reciprocally stabilizes MAP7/7D1 proteins. Depletion of MAP7/7D1 causes failure in cortical targeting of microtubule plus-ends, which in turn leads to reduced actin and focal adhesion dynamics, ultimately resulting in defects in cell migration and adhesion [kikuchi-2018-wnt-signaling-abstract].

The evolutionary conservation of this mechanism is supported by studies in Drosophila, where the MAP7 ortholog ensconsin shows planar-polarized distribution in pupal wing epithelial cells and is required for proper localization of Drosophila Dishevelled (Dsh). Similarly, in mouse oviduct epithelial cells, MAP7/7D1 display planar-polarized distribution. This conservation across species suggests that the MAP7-Dishevelled interaction represents an ancient mechanism linking microtubule organization to planar cell polarity signaling.

## DNA Damage Response

An unexpected function of MAP7 has emerged from proteomic studies examining the DNA damage response. Dullovi and colleagues discovered that MAP7 and MAP7D1 interact with several DNA repair proteins, including the double-strand break repair factors RAD50, BRCA1, and 53BP1 [dullovi-2023-dna-repair-abstract]. These interactions are phosphorylation-dependent and regulated by the kinase CK2, with the interaction domain mapping to residues 144-300 of MAP7.

Functional studies revealed that downregulation of MAP7 and MAP7D1 leads to increased phosphorylation of p53 after gamma-irradiation, indicating enhanced DNA damage signaling. Furthermore, depletion of MAP7D1 causes a strong G1 cell cycle arrest, and knockdown of MAP7 and MAP7D1 in G1-arrested cells negatively affects DNA repair efficiency, recruitment of RAD50 to chromatin, and localization of 53BP1 to sites of damage [dullovi-2023-dna-repair-abstract].

These findings describe a novel function for MAP7 family proteins in cell cycle regulation and repair of DNA double-strand breaks, particularly during G1 phase when homologous recombination is unavailable and cells rely on non-homologous end joining. The mechanism by which cytoplasmic microtubule-associated proteins influence nuclear DNA repair processes remains to be fully elucidated but may involve trafficking of repair factors or coordination of cytoplasmic and nuclear responses to genotoxic stress.

## Cell Cycle Regulation and Mitosis

MAP7 function is regulated by phosphorylation during the cell cycle. During interphase, the protein is phosphorylated only on serine residues, but during mitosis it becomes phosphorylated on threonine as well. Ten Cdk1 phosphorylation sites (T/SP motifs) have been identified, six of which are located within the microtubule-binding domain. Phosphorylation of MAP7 downstream of Cdk1/cyclin B leads to inactivation of the protein in prophase, contributing to the reduction in interphase microtubule stability that is necessary for proper spindle assembly. Failure to destabilize microtubules in prophase leads to formation of microtubule clumps that interfere with spindle morphogenesis.

In Drosophila neural stem cells, MAP7/ensconsin promotes microtubule growth and centrosome separation, indicating a positive role in mitotic spindle organization. The protein helps control the length of microtubules in the mitotic spindle, contributing to proper chromosome segregation.

## Subcellular Localization

MAP7 localizes primarily to the cytoplasm in association with microtubules. The protein shows a dynamic association with microtubules, binding rapidly to newly polymerized microtubule lattice and dissociating upon depolymerization [faire-1999-emap115-dynamics-abstract]. In polarized epithelial cells, MAP7 concentrates at the apical pole where microtubule organizing centers are typically located.

In neurons, MAP7 localizes throughout dendrites and axons but shows enrichment at specific sites including branch junctions. The protein preferentially associates with stable, acetylated microtubule segments while avoiding the dynamic plus ends, creating a characteristic spatial distribution along the microtubule lattice [tymanskyj-2019-branch-retraction-abstract].

In muscle cells, MAP7 associates with microtubules that connect adjacent nuclei, facilitating the sliding mechanism that positions nuclei appropriately within multinucleate fibers [metzger-2012-nuclear-positioning-abstract].

## Evolutionary Conservation

The MAP7/ensconsin protein family is highly conserved across metazoans, with clear orthologs identified in both vertebrates and invertebrates. The Drosophila ensconsin protein shares significant sequence similarity with mammalian MAP7/E-MAP-115, particularly in two conserved regions designated ensconsin homology region 1 (EHR1) and EHR2. The N-terminal EHR1 region corresponds to the microtubule-binding domain, while EHR2 encompasses the C-terminal kinesin-binding region. Both mammalian and Drosophila proteins generate multiple isoforms through alternative splicing, particularly in the regions flanking EHR1 [barlan-2013-kinesin-cofactor-abstract].

Functional studies have confirmed that the essential role of ensconsin/MAP7 as a kinesin-1 cofactor is conserved across species. In Drosophila, ensconsin is required for all known kinesin-1-dependent processes, including proper polarization of the oocyte, nuclear positioning in muscle cells, and neuronal transport. Single-molecule motility assays using Drosophila ovary extract demonstrated that kinesin-1 recruitment to microtubules and subsequent motility are severely impaired without ensconsin [barlan-2013-kinesin-cofactor-abstract]. The phenotypic similarity between Drosophila ensconsin mutants and mammalian MAP7-depleted cells—including defects in myonuclear positioning and kinesin-dependent transport—underscores the ancient origin of this regulatory mechanism.

In mammals, the single ancestral MAP7 gene has undergone duplication to produce a family of four genes: MAP7, MAP7D1, MAP7D2, and MAP7D3. All four family members retain the ability to bind microtubules and interact with kinesin-1, but their distinct expression patterns and subtle biochemical differences suggest functional specialization [hooikaas-2019-map7-family-abstract]. MAP7D1 displays the highest sequence conservation with MAP7, while MAP7D3 has been shown to have higher affinity for kinesin-1 but lower affinity for microtubules compared to MAP7, and uniquely can be cotransported with the motor along microtubules. This diversification of the MAP7 family in mammals may allow for tissue-specific and context-dependent fine-tuning of kinesin-1-mediated transport.

## Open Questions

Several important questions about MAP7 function remain to be addressed:

1. **Isoform-specific functions**: While MAP7, MAP7D1, MAP7D2, and MAP7D3 share the ability to bind microtubules and recruit kinesin-1, their distinct expression patterns suggest non-redundant functions in specific cell types. The precise division of labor among family members, particularly in the nervous system, requires further investigation.

2. **Regulation by phosphorylation**: Beyond cell cycle-dependent phosphorylation by Cdk1, MAP7 contains numerous potential phosphorylation sites in its P domain. CK2 phosphorylation has been implicated in regulating MAP7 interactions with DNA repair proteins [dullovi-2023-dna-repair-abstract], but how phosphorylation by various kinases modulates MAP7 function across different cellular contexts remains incompletely understood.

3. **Role in human disease**: While mouse models demonstrate that MAP7 null mutations cause male sterility due to defective spermatogenesis [komada-2000-spermatogenesis-abstract] and defects in nuclear positioning are associated with centronuclear myopathies, direct connections between MAP7 mutations and specific human diseases have not been firmly established. Comprehensive analysis of human genetic variants in MAP7 is lacking.

4. **Concentration-dependent effects**: The biphasic regulation of kinesin-1 by MAP7—facilitation at low concentrations, inhibition at high concentrations—raises questions about how local MAP7 concentrations are controlled in cells to achieve appropriate motor activity.

5. **Mechanism of DNA damage response involvement**: The discovery that MAP7 interacts with DNA repair proteins and influences double-strand break repair in G1 phase [dullovi-2023-dna-repair-abstract] raises fundamental questions about how a cytoplasmic microtubule-associated protein contributes to nuclear DNA repair processes.

6. **Wnt signaling integration**: The reciprocal regulatory relationship between MAP7 and Dishevelled in non-canonical Wnt signaling [kikuchi-2018-wnt-signaling-abstract] suggests broader roles for MAP7 in developmental signaling. How MAP7 coordinates microtubule organization with planar cell polarity establishment across different tissue types warrants further investigation.

7. **Therapeutic potential**: Given the essential role of MAP7 in kinesin-1-mediated transport, understanding how to modulate this pathway could have implications for neurodegenerative diseases involving transport defects. Whether MAP7 or its interactions with kinesin-1 represent viable therapeutic targets remains to be explored.

## References

- [bulinski-1994-ensconsin-abstract]: Bulinski JC, Bossler A. (1994) Purification and characterization of ensconsin, a novel microtubule stabilizing protein. J Cell Sci. 107(Pt 10):2839-49. PMID: 7876351. DOI: 10.1242/jcs.107.10.2839

- [faire-1999-emap115-dynamics-abstract]: Faire K, Waterman-Storer CM, Gruber D, Masson D, Salmon ED, Bulinski JC. (1999) E-MAP-115 (ensconsin) associates dynamically with microtubules in vivo and is not a physiological modulator of microtubule dynamics. J Cell Sci. 112(Pt 23):4243-55. PMID: 10564643. DOI: 10.1242/jcs.112.23.4243

- [metzger-2012-nuclear-positioning-abstract]: Metzger T, Gache V, Xu M, Cadot B, Folker ES, Richardson BE, Gomes ER, Baylies MK. (2012) MAP and kinesin-dependent nuclear positioning is required for skeletal muscle function. Nature. 484(7392):120-4. PMID: 22425998. DOI: 10.1038/nature10914

- [barlan-2013-kinesin-cofactor-abstract]: Barlan K, Lu W, Gelfand VI. (2013) The microtubule-binding protein ensconsin is an essential cofactor of kinesin-1. Curr Biol. 23(4):317-22. PMID: 23394833. DOI: 10.1016/j.cub.2013.01.008

- [vanier-2003-emap115-epithelial-abstract]: Vanier MT, Deck P, Stutzmann J, Gendry P, Arnold C, Dirrig-Grosch S, Kedinger M, Launay JF. (2003) Expression and distribution of distinct variants of E-MAP-115 during proliferation and differentiation of human intestinal epithelial cells. Cell Motil Cytoskeleton. 55(4):221-31. PMID: 12845596. DOI: 10.1002/cm.10124

- [monroy-2018-map-competition-abstract]: Monroy BY, Sawyer DL, Ackermann BE, Borden MM, Tan TC, Ori-McKenney KM. (2018) Competition between microtubule-associated proteins directs motor transport. Nat Commun. 9(1):1487. PMID: 29662074. DOI: 10.1038/s41467-018-03909-2

- [tymanskyj-2018-axon-morphogenesis-abstract]: Tymanskyj SR, Yang BH, Verhey KJ, Ma L. (2018) MAP7 regulates axon morphogenesis by recruiting kinesin-1 to microtubules and modulating organelle transport. eLife. 7:e36374. PMID: 30132755. DOI: 10.7554/eLife.36374

- [tymanskyj-2019-branch-retraction-abstract]: Tymanskyj SR, Ma L. (2019) MAP7 Prevents Axonal Branch Retraction by Creating a Stable Microtubule Boundary to Rescue Polymerization. J Neurosci. 39(36):7118-7131. PMID: 31391261. DOI: 10.1523/JNEUROSCI.0775-19.2019

- [hooikaas-2019-map7-family-abstract]: Hooikaas PJ, Martin M, Muhlethaler T, et al. (2019) MAP7 family proteins regulate kinesin-1 recruitment and activation. J Cell Biol. 218(4):1298-1318. PMID: 30770434. DOI: 10.1083/jcb.201808065

- [chaudhary-2019-organelle-transport-abstract]: Chaudhary AR, Lu H, Krementsova EB, Bookwalter CS, Trybus KM, Hendricks AG. (2019) MAP7 regulates organelle transport by recruiting kinesin-1 to microtubules. J Biol Chem. 294(26):10160-10171. PMID: 31085585. DOI: 10.1074/jbc.RA119.008052

- [ferro-2022-kinesin-structure-abstract]: Ferro LS, Fang Q, Eshun-Wilson L, et al. (2022) Structural and functional insight into regulation of kinesin-1 by microtubule-associated protein MAP7. Science. 375(6578):268-272. PMID: 35050657. DOI: 10.1126/science.abf6154

- [adler-2024-mtbd-structure-abstract]: Adler A, Bangera M, Beugelink JW, Bahri S, van Ingen H, Moores CA, Baldus M. (2024) A structural and dynamic visualization of the interaction between MAP7 and microtubules. Nat Commun. 15(1):1574. PMID: 38431715. DOI: 10.1038/s41467-024-46260-5

- [komada-2000-spermatogenesis-abstract]: Komada M, McLean DJ, Griswold MD, Russell LD, Soriano P. (2000) E-MAP-115, encoding a microtubule-associated protein, is a retinoic acid-inducible gene required for spermatogenesis. Genes Dev. 14(11):1332-42. DOI: 10.1101/gad.14.11.1332

- [kikuchi-2018-wnt-signaling-abstract]: Kikuchi K, Nakamura A, Arata M, Shi D, Nakagawa M, Tanaka T, Uemura T, Fujimori T, Kikuchi A, Uezu A, Sakamoto Y, Nakanishi H. (2018) Map7/7D1 and Dvl form a feedback loop that facilitates microtubule remodeling and Wnt5a signaling. EMBO Rep. 19(7):e45471. PMID: 29880710. DOI: 10.15252/embr.201745471

- [dullovi-2023-dna-repair-abstract]: Dullovi A, Ozgencil M, Rajvee V, Tse WY, Cutillas PR, Martin SA, Horejsi Z. (2023) Microtubule-associated proteins MAP7 and MAP7D1 promote DNA double-strand break repair in the G1 cell cycle phase. iScience. 26(3):106107. PMID: 36852271. DOI: 10.1016/j.isci.2023.106107


## Citations

1. adler-2024-mtbd-structure-abstract.md
2. barlan-2013-kinesin-cofactor-abstract.md
3. bulinski-1994-ensconsin-abstract.md
4. chaudhary-2019-organelle-transport-abstract.md
5. dullovi-2023-dna-repair-abstract.md
6. faire-1999-emap115-dynamics-abstract.md
7. ferro-2022-kinesin-structure-abstract.md
8. hooikaas-2019-map7-family-abstract.md
9. kikuchi-2018-wnt-signaling-abstract.md
10. komada-2000-spermatogenesis-abstract.md
11. metzger-2012-nuclear-positioning-abstract.md
12. monroy-2018-map-competition-abstract.md
13. tymanskyj-2018-axon-morphogenesis-abstract.md
14. tymanskyj-2019-branch-retraction-abstract.md
15. vanier-2003-emap115-epithelial-abstract.md