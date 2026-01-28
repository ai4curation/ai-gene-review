---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T16:51:34.150420'
end_time: '2026-01-22T17:08:51.997466'
duration_seconds: 1037.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: COPG1
  gene_symbol: COPG1
  uniprot_accession: Q9Y678
  protein_description: 'RecName: Full=Coatomer subunit gamma-1; AltName: Full=Gamma-1-coat
    protein; Short=Gamma-1-COP;'
  gene_info: Name=COPG1; Synonyms=COPG;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the COPG family. .
  protein_domains: ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Clathrin/coatomer_adapt-like_N.
    (IPR002553); Clathrin_app_Ig-like_sf. (IPR013041); Coatomer/calthrin_app_sub_C.
    (IPR009028)
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
- **UniProt Accession:** Q9Y678
- **Protein Description:** RecName: Full=Coatomer subunit gamma-1; AltName: Full=Gamma-1-coat protein; Short=Gamma-1-COP;
- **Gene Information:** Name=COPG1; Synonyms=COPG;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the COPG family. .
- **Key Domains:** ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Clathrin/coatomer_adapt-like_N. (IPR002553); Clathrin_app_Ig-like_sf. (IPR013041); Coatomer/calthrin_app_sub_C. (IPR009028)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "COPG1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'COPG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **COPG1** (gene ID: COPG1, UniProt: Q9Y678) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# COPG1 (Coatomer Subunit Gamma-1): A Comprehensive Review

## Introduction and Overview

COPG1 encodes the gamma-1 subunit of the coat protein complex I (COPI), a key component of the vesicular transport machinery in eukaryotic cells. The gamma-1-COP protein (also known as γ1-COP) is one of seven subunits that constitute the coatomer complex, which mediates retrograde transport from the Golgi apparatus to the endoplasmic reticulum (ER) and facilitates intra-Golgi trafficking [beck-2009-COPI-review-summary]. COPI-coated vesicles are essential for maintaining the identity and function of secretory pathway compartments by ensuring the retrieval of ER-resident proteins and the cycling of membrane-associated machinery between compartments.

The coatomer exists as a stable cytosolic heptameric complex composed of α-, β-, β'-, γ-, δ-, ε-, and ζ-COP subunits that is recruited en bloc to Golgi membranes during vesicle formation [beck-2009-COPI-review-summary]. In mammals, the γ-COP subunit exists as two paralogs: γ1-COP (encoded by COPG1) and γ2-COP (encoded by COPG2), which share approximately 80% amino acid sequence identity [moelleken-2007-coatomer-isoforms-golgi-abstract]. While these paralogs are largely functionally redundant for essential cellular functions, recent research has revealed specific roles for γ1-COP, particularly in neuronal differentiation and immune cell function [bethune-2020-COPG1-COPG2-neuronal-abstract][bainter-2021-COPG1-immunodeficiency-abstract].

## Structural Organization of the Coatomer Complex

The coatomer complex can be conceptually subdivided into two subcomplexes: an outer-coat or B-subcomplex (comprising α-, β'-, and ε-COP) and an adaptor or F-subcomplex (comprising β-, γ-, δ-, and ζ-COP) [beck-2009-COPI-review-summary]. This organization bears striking resemblance to the heterotetrameric adaptor protein complexes (AP-1 through AP-4) that function in clathrin-mediated vesicle formation, reflecting the evolutionary relationship between these vesicular trafficking systems.

The γ-COP subunit consists of several structural domains with distinct functions. The N-terminal region adopts an α-solenoid fold comprising approximately fifteen α-helices, which serves as the primary Arf1-GTP binding interface [yu-2012-Arf1-coatomer-recruitment-abstract]. Crystal structure analysis of the γζ-COP subcomplex bound to Arf1-GTP revealed that Arf1 contacts helices α4 and α6 on the outer surface of γ-COP through a predominantly hydrophobic interface [yu-2012-Arf1-coatomer-recruitment-abstract]. Key interfacial residues include F71, T74, and I104 from γ-COP and F51, L77, and Y81 from Arf1.

The C-terminal region of γ-COP contains an appendage domain that adopts a fold similar to the α-appendage of the AP-2 adaptor complex [watson-2004-gamma-COP-appendage-abstract]. This appendage domain contains a protein-protein interaction site on its platform subdomain that serves as a binding interface for ArfGAP2 and ArfGAP3, regulatory proteins that catalyze GTP hydrolysis in Arf1 and thereby control vesicle uncoating [watson-2004-gamma-COP-appendage-abstract][weimer-2008-ArfGAP-differential-abstract].

## Molecular Function: Coatomer Recruitment and Membrane Binding

The assembly of COPI-coated vesicles is initiated by the small GTPase Arf1 (ADP-ribosylation factor 1), which cycles between an inactive GDP-bound cytosolic form and an active GTP-bound membrane-associated form [yu-2012-Arf1-coatomer-recruitment-abstract]. Arf1 activation is catalyzed by guanine nucleotide exchange factors (GEFs) such as GBF1, which trigger a conformational change allowing the insertion of Arf1's N-terminal amphipathic helix into the membrane bilayer.

Structural and biochemical studies have established that two Arf1-GTP molecules bind to each coatomer complex. One Arf1 molecule binds to the γζ-COP subcomplex, while a second binds to the βδ-COP subcomplex at a site common to both the γ- and β-COP subunits [yu-2012-Arf1-coatomer-recruitment-abstract]. Cryo-electron tomography studies at 9.2 Å resolution have revealed that these two Arf1 molecules occupy contrasting molecular environments within the assembled coat: the central Arf1 (termed γArf1) associates with γ-COP, while the peripheral Arf1 (termed βArf1) binds to both β-COP and δ-COP [dodonova-2017-COPI-structure-9A-abstract].

The γ-COP subunit also serves as a critical receptor for the p24 family of membrane proteins, which are major transmembrane components of COPI-coated vesicles [sohn-1996-p23-coatomer-binding-abstract]. The p23 protein, a founding member of this family, is enriched approximately 20-fold in COPI vesicles compared to donor Golgi membranes and is present in stoichiometric amounts with Arf1 and coatomer [sohn-1996-p23-coatomer-binding-abstract]. Photocrosslinking experiments demonstrated that under native conditions, the cytoplasmic domain of p23 interacts exclusively with the γ subunit of coatomer [harter-1998-p23-gamma-COP-abstract]. This interaction shares a binding site with the KKXX dilysine retrieval motif, indicating that γ-COP plays a central role in coupling cargo recognition to membrane recruitment [harter-1998-p23-gamma-COP-abstract].

## Cargo Recognition Mechanisms

COPI vesicles mediate the retrograde transport of transmembrane proteins bearing specific sorting signals in their cytoplasmic domains. The best-characterized sorting signals are dilysine motifs with the consensus sequences KKxx and KxKxx (where x represents any amino acid), which target ER-resident membrane proteins for Golgi-to-ER retrieval [jackson-2012-dilysine-COPI-abstract][ma-2013-dilysine-rules-abstract].

While early studies using photocrosslinking approaches suggested that γ-COP mediates dilysine motif binding under native conditions [harter-1998-p23-gamma-COP-abstract], subsequent structural and biochemical work has clarified that the primary dilysine-binding subunits are α-COP and β'-COP of the B-subcomplex [jackson-2012-dilysine-COPI-abstract][ma-2013-dilysine-rules-abstract]. Both subunits contain N-terminal WD-repeat domains (β-propeller structures) that directly recognize dilysine motifs through electrostatic interactions with acidic binding patches.

Crystal structures of α-COP and β'-COP bound to various retrieval motifs revealed that dilysine recognition involves lysine side-chain interactions with two acidic patches on the propeller surface [ma-2013-dilysine-rules-abstract]. Interestingly, KKxx and KxKxx motifs bind with different geometries, with their lysine residues transposed at the binding patches [ma-2013-dilysine-rules-abstract]. While α-COP and β'-COP show similar specificity for canonical KKxx and KxKxx motifs, only β'-COP recognizes the non-canonical RKxx signal [ma-2013-dilysine-rules-abstract]. Isothermal titration calorimetry measurements indicate that β'-COP binds the KxKxx motif with a dissociation constant of approximately 6.8 μM, with lower affinity for KKxx variants (approximately 85 μM) [jackson-2012-dilysine-COPI-abstract].

The γ-COP subunit contributes to cargo recognition through its interactions with the p24 family of membrane proteins, which contain both diphenylalanine (FF) and dibasic motifs in their cytoplasmic tails [nickel-1997-p23-cycling-abstract]. P24 proteins function as major membrane constituents of COPI vesicles and may serve as cargo receptors or as regulators of coatomer assembly dynamics [sohn-1996-p23-coatomer-binding-abstract].

## Regulation by ArfGAP Proteins

The γ-COP appendage domain plays a critical role in recruiting ArfGAP2 and ArfGAP3, the primary GAPs responsible for COPI vesicle uncoating [watson-2004-gamma-COP-appendage-abstract][weimer-2008-ArfGAP-differential-abstract]. These coat-dependent GAPs lack intrinsic membrane-binding capacity and instead are recruited to COPI vesicles through direct interactions with coatomer [weimer-2008-ArfGAP-differential-abstract]. In contrast, ArfGAP1 binds membranes independently through ALPS (ArfGAP1 Lipid Packing Sensor) motifs that sense membrane curvature.

Structural studies have revealed that ArfGAP2's catalytic domain localizes exclusively near the central γArf1 within the assembled COPI coat, positioned within a specialized niche formed by multiple coat subunits [dodonova-2017-COPI-structure-9A-abstract]. This spatial arrangement suggests a proofreading mechanism whereby coat dissociation occurs only after productive assembly, ensuring that premature uncoating does not occur during vesicle budding.

Coatomer binding stimulates the catalytic activity of both ArfGAP2 and ArfGAP3 more than 1,000-fold, and biochemical assays demonstrate that these GAPs show markedly higher activity in uncoating reactions compared to ArfGAP1 [weimer-2008-ArfGAP-differential-abstract]. Knockdown studies have established that both ArfGAP2 and ArfGAP3 are essential for proper COPI coat assembly on living cells, further underscoring the importance of the γ-COP-ArfGAP interaction for COPI function.

## Subcellular Localization and Isoform-Specific Distribution

Quantitative immunoelectron microscopy studies have revealed that the γ1-COP and γ2-COP paralogs show distinct subcellular distributions within the Golgi apparatus [moelleken-2007-coatomer-isoforms-golgi-abstract]. Approximately 70% of COPI coats containing γ1-COP are localized to the cis-Golgi, whereas the majority (>60%) of COPI coats containing γ2-COP are found in the trans-Golgi [moelleken-2007-coatomer-isoforms-golgi-abstract]. Biochemical analysis of coatomer isoform composition in mammalian cells revealed that γ1ζ1-coatomer represents approximately 50% of total coatomer, followed by γ2ζ1 (~30%), γ1ζ2 (~20%), and γ2ζ2 (<5%) [moelleken-2007-coatomer-isoforms-golgi-abstract].

The differential localization of γ1-COP and γ2-COP isoforms suggests specialized transport functions for different coatomer combinations. The preferential localization of p24 family proteins (p23, p24, and p27) at the cis-Golgi may explain the enrichment of γ1-containing coatomers in this compartment, as these membrane proteins serve as coatomer receptors and may have different affinities for γ1-COP versus γ2-COP [moelleken-2007-coatomer-isoforms-golgi-abstract].

## Paralog-Specific Functions in Neuronal Differentiation

While γ1-COP and γ2-COP are largely functionally redundant for essential cellular processes, recent research has revealed paralog-specific functions during neuronal differentiation [bethune-2020-COPG1-COPG2-neuronal-abstract]. Analysis of gene expression data demonstrated that Copg1, but not Copg2, is strongly upregulated as mouse embryonic stem cells differentiate into terminal neurons, suggesting a unique function for γ1-COP in neuronal biogenesis [bethune-2020-COPG1-COPG2-neuronal-abstract].

Knockout studies in P19 cells revealed that while disruption of either Copg1 or Copg2 slowed cell proliferation, only Copg1 knockout affected retinoic acid-mediated neuronal differentiation [bethune-2020-COPG1-COPG2-neuronal-abstract]. Specifically, Copg1 knockout cells formed loose embryoid bodies and exhibited reduced neurite outgrowth compared to wild-type or Copg2 knockout cells. Rescue experiments demonstrated that while increased expression of γ2-COP could compensate for the loss of γ1-COP in embryoid body formation, γ1-COP is specifically required for efficient neurite outgrowth—a function that γ2-COP cannot replicate [bethune-2020-COPG1-COPG2-neuronal-abstract].

These findings represent the first evidence of paralog-specific functions for a COPI subunit and suggest that the COPI trafficking machinery has specialized to support the unique demands of neuronal cells. The molecular basis for γ1-COP's specific role in neurite outgrowth remains to be fully elucidated but may involve differential interactions with cargo proteins or regulatory factors important for neuronal morphogenesis.

## Disease Associations: Combined Immunodeficiency and STING Pathway Activation

Mutations in COPG1 have been identified as the cause of a novel combined immunodeficiency syndrome [bainter-2021-COPG1-immunodeficiency-abstract]. Five Omani siblings with recurrent bacterial and viral infections, severe CD4+ T cell lymphopenia, and impaired humoral and cellular immunity were found to carry a homozygous missense mutation (p.K652E) in COPG1 [bainter-2021-COPG1-immunodeficiency-abstract]. This mutation disrupts the ability of coatomer to interact with the KDEL receptor, which is essential for the retrograde retrieval of KDEL-bearing ER-resident chaperones (such as BiP, calreticulin, and protein disulfide isomerase) from the Golgi to the ER.

The K652E mutation leads to mislocalization of ER chaperones to the Golgi apparatus, resulting in increased ER stress specifically in activated T and B cells [bainter-2021-COPG1-immunodeficiency-abstract]. Mouse models carrying the equivalent mutation displayed normal immune function under specific pathogen-free conditions but developed severe immunodeficiency upon exposure to diverse environmental microbes. Importantly, treatment with the chemical chaperone tauroursodeoxycholic acid (TUDCA), which relieves ER stress, corrected the immunologic defects in mutant mice, establishing that pathologic ER stress underpins the disease mechanism [bainter-2021-COPG1-immunodeficiency-abstract].

Independently, COPG1 deficiency has been linked to aberrant activation of the STING (Stimulator of Interferon Genes) innate immune signaling pathway [steiner-2022-COPI-STING-abstract]. CRISPR/Cas9-mediated deletion of COPG1 (or another COPI subunit, COPD) in cell culture models induced spontaneous type I interferon responses through the cGAS/STING pathway [steiner-2022-COPI-STING-abstract]. The mechanism involves defective retrograde trafficking of STING from the Golgi to the ER, leading to accumulation of active STING at the Golgi and constitutive downstream signaling.

These findings have important therapeutic implications, as treatment with the small molecule STING inhibitor H-151 reduced inflammation in patient cells and disease models [steiner-2022-COPI-STING-abstract]. This suggests that STING inhibition could be beneficial for COPA syndrome (caused by mutations in α-COP) and potentially other COPI-related inflammatory diseases.

## Biochemical Properties and Protein Interactions

The γ1-COP protein is a 97-kDa polypeptide that interacts with multiple partners essential for COPI function. The key protein interactions include:

1. **Arf1-GTP**: The N-terminal α-solenoid domain of γ-COP provides the primary binding site for membrane-associated Arf1-GTP, anchoring coatomer to the Golgi membrane [yu-2012-Arf1-coatomer-recruitment-abstract].

2. **ζ-COP**: The γ-COP and ζ-COP subunits form a stable subcomplex (γζ-COP) that is homologous to the AP adaptor complex medium and small subunits [yu-2012-Arf1-coatomer-recruitment-abstract].

3. **ArfGAP2/ArfGAP3**: The C-terminal appendage domain of γ-COP recruits these coat-dependent GAPs through its platform subdomain [watson-2004-gamma-COP-appendage-abstract][weimer-2008-ArfGAP-differential-abstract].

4. **p24 family proteins**: The cytoplasmic tails of p23 and related p24 proteins interact with γ-COP through a binding site that overlaps with dilysine motif recognition [harter-1998-p23-gamma-COP-abstract].

5. **KDEL receptor**: The KDEL receptor (KDELR) retrieves soluble ER-resident proteins bearing KDEL sequences, and its trafficking depends on COPI function. The K652E mutation in γ1-COP disrupts this interaction [bainter-2021-COPG1-immunodeficiency-abstract].

## Emerging Role in RNA Transport and Neuronal Function

Recent studies have revealed an unexpected function for COPI components in RNA transport, particularly in neurons. The COPI vesicle complex has been shown to bind specific RNAs and participate in their transport within axons [todd-2013-COPI-RNA-binding-abstract][peter-2011-COPI-SMN-axons-abstract]. Using formaldehyde-crosslinked immunoprecipitation followed by sequencing (FLRIP-Seq), researchers identified over 1,500 RNAs that associate with α-COP in motor neurons [todd-2013-COPI-RNA-binding-abstract]. These RNAs are enriched in G-quadruplex motifs and overlap significantly with fragile X mental retardation protein (FMRP)-associated transcripts, encoding proteins localized to the plasma membrane and cytoskeleton.

Different COPI subunits show selective RNA associations, with some transcripts binding differentially to γ1-COP versus γ2-COP, suggesting that coatomer isoforms may transport distinct RNA cargoes [todd-2013-COPI-RNA-binding-abstract]. The mechanism of RNA association appears to be indirect: α-COP binds to the survival motor neuron (SMN) protein, which in turn associates with RNA-binding proteins including hnRNP-R, hnRNP-Q, KSRP, and HuD. Thus, COPI likely serves as an upstream scaffold for attachment of multiple RNA-binding proteins [todd-2013-COPI-RNA-binding-abstract].

The functional significance of COPI-mediated RNA transport is underscored by studies of spinal muscular atrophy (SMA), a motor neuron disease caused by insufficient SMN protein. α-COP directly binds to SMN and co-localizes with SMN granules in growth cones and lamellipodia of neuronal cells [peter-2011-COPI-SMN-axons-abstract]. A subset of COPI-containing granules travels together with SMN within axons, and depletion of α-COP results in mislocalization of SMN and actin at the leading edge. These findings suggest that neurons utilize COPI vesicles to deliver essential cargo—including RNA and RNA-binding proteins—for motor neuron function and integrity.

The involvement of COPI in axonal transport may help explain the neurodegenerative phenotypes observed in COPI mutants. Mice with point mutations in δ-COP exhibit cerebellar ataxia due to Purkinje neuron degeneration, and mutations in COPI-associated proteins like Scyl1 cause motor neuron disease reminiscent of amyotrophic lateral sclerosis (ALS). The extreme cytoarchitecture of motor neurons and Purkinje cells—with enormous dendritic arbors and lengthy axons—may make them particularly sensitive to defects in intracellular trafficking.

## Evolutionary Conservation

The γ-COP subunit is highly conserved across eukaryotes, reflecting the fundamental importance of COPI-mediated trafficking for cellular homeostasis. The yeast ortholog of γ-COP, Sec21p, was identified in genetic screens for secretion mutants conducted in Randy Schekman's laboratory, work that contributed to the 2013 Nobel Prize in Physiology or Medicine. SEC21 is an essential gene required for protein transport from the ER to the Golgi, and the 105 kDa Sec21p protein participates in the yeast coatomer complex. Temperature-sensitive sec21 mutants exhibit striking, cargo-selective ER to Golgi transport defects, with some proteins (like carboxypeptidase Y and α-factor) blocked in the ER while others (invertase and HSP150) are secreted normally [watson-2004-gamma-COP-appendage-abstract].

The duplication event giving rise to the COPG1 and COPG2 paralogs occurred during vertebrate evolution. Both genes encode functional γ-COP proteins that can support essential COPI functions, but they have acquired specialized roles in certain cell types [bethune-2020-COPG1-COPG2-neuronal-abstract]. This functional diversification of paralogous coat proteins is analogous to the expansion of clathrin adaptor complexes (AP-1 through AP-5) that occurred during evolution of the endomembrane system.

## Open Questions

Several important questions regarding COPG1 function remain to be addressed:

1. **Molecular basis of paralog specificity**: What structural or biochemical differences between γ1-COP and γ2-COP account for the specific requirement for γ1-COP in neurite outgrowth? Identifying cargo proteins or regulatory factors that differentially interact with the two paralogs could provide mechanistic insight.

2. **Tissue-specific expression regulation**: How is the expression of COPG1 regulated during neuronal differentiation, and what transcription factors or signaling pathways control its upregulation in terminal neurons?

3. **KDEL receptor interaction site**: The K652E mutation that disrupts KDELR binding is located in a region not previously characterized structurally. Determining the precise binding interface between γ1-COP and KDELR would be valuable for understanding how this mutation causes disease.

4. **Role in other tissues**: Given the tissue-specific defects observed in COPG1-deficient mice (primarily affecting immune cells and neurons), are there other cell types with specific requirements for γ1-COP over γ2-COP?

5. **Therapeutic approaches**: Can ER stress-relieving agents like TUDCA, or STING inhibitors like H-151, be developed as treatments for COPG1-related immunodeficiency or inflammatory diseases?

6. **Cargo selectivity**: Do γ1-COP and γ2-COP show different selectivity for cargo proteins, and could this explain their differential localization within the Golgi stack?

## References

1. [beck-2009-COPI-review-summary] Beck R, Ravet M, Wieland FT, Cassel D. The COPI system: molecular mechanisms and function. FEBS Lett. 2009;583(17):2701-2709. doi:10.1016/j.febslet.2009.07.032

2. [moelleken-2007-coatomer-isoforms-golgi-abstract] Moelleken J, Malsam J, Betts MJ, et al. Differential localization of coatomer complex isoforms within the Golgi apparatus. Proc Natl Acad Sci USA. 2007;104(11):4425-4430. doi:10.1073/pnas.0611360104. PMID: 17360540

3. [bethune-2020-COPG1-COPG2-neuronal-abstract] Béthune J et al. A paralog-specific role of COPI vesicles in the neuronal differentiation of mouse pluripotent cells. Life Sci Alliance. 2020;3(9):e202000714. doi:10.26508/lsa.202000714. PMID: 32665377

4. [bainter-2021-COPG1-immunodeficiency-abstract] Bainter W et al. Combined immunodeficiency due to a mutation in the γ1 subunit of the coat protein I complex. J Clin Invest. 2021;131(3):e140494. doi:10.1172/JCI140494. PMID: 33529166

5. [yu-2012-Arf1-coatomer-recruitment-abstract] Yu X, Breitman M, Goldberg J. A structure-based mechanism for Arf1-dependent recruitment of coatomer to membranes. Cell. 2012;148(3):530-542. doi:10.1016/j.cell.2012.01.015. PMID: 22304919

6. [dodonova-2017-COPI-structure-9A-abstract] Dodonova SO, Aderhold P, Kopp J, et al. 9Å structure of the COPI coat reveals that the Arf1 GTPase occupies two contrasting molecular environments. eLife. 2017;6:e26691. doi:10.7554/eLife.26691. PMID: 28621666

7. [watson-2004-gamma-COP-appendage-abstract] Watson PJ, Frigerio G, Collins BM, Duden R, Owen DJ. Gamma-COP appendage domain - structure and function. Traffic. 2004;5(2):79-88. doi:10.1111/j.1600-0854.2004.00158.x. PMID: 14690497

8. [harter-1998-p23-gamma-COP-abstract] Harter C, Wieland FT. A single binding site for dilysine retrieval motifs and p23 within the γ subunit of coatomer. Proc Natl Acad Sci USA. 1998;95(20):11649-11654. doi:10.1073/pnas.95.20.11649. PMID: 9751720

9. [jackson-2012-dilysine-COPI-abstract] Jackson LP, Lewis M, Kent HM, et al. Molecular basis for recognition of dilysine trafficking motifs by COPI. Dev Cell. 2012;23(6):1255-1262. doi:10.1016/j.devcel.2012.10.017. PMID: 23177648

10. [ma-2013-dilysine-rules-abstract] Ma W, Goldberg J. Rules for the recognition of dilysine retrieval motifs by coatomer. EMBO J. 2013;32(7):926-937. doi:10.1038/emboj.2013.41. PMID: 23481256

11. [sohn-1996-p23-coatomer-binding-abstract] Sohn K, Orci L, Ravazzola M, et al. A major transmembrane protein of Golgi-derived COPI-coated vesicles involved in coatomer binding. J Cell Biol. 1996;135(5):1239-1248. doi:10.1083/jcb.135.5.1239. PMID: 8947548

12. [nickel-1997-p23-cycling-abstract] Nickel W, Sohn K, Bünning C, Wieland FT. p23, a major COPI-vesicle membrane protein, constitutively cycles through the early secretory pathway. Proc Natl Acad Sci USA. 1997;94(21):11393-11398. doi:10.1073/pnas.94.21.11393. PMID: 9326620

13. [weimer-2008-ArfGAP-differential-abstract] Weimer C, Beck R, Eckert P, et al. Differential roles of ArfGAP1, ArfGAP2, and ArfGAP3 in COPI trafficking. J Cell Biol. 2008;183(4):725-735. doi:10.1083/jcb.200806140. PMID: 19015319

14. [steiner-2022-COPI-STING-abstract] Steiner A, Hrovat-Schaale K, et al. Deficiency in coatomer complex I causes aberrant activation of STING signalling. Nat Commun. 2022;13(1):2321. doi:10.1038/s41467-022-29946-6. PMID: 35484149

15. [taylor-2023-COPI-structure-review-abstract] Taylor RJ, Tagiltsev G, Briggs JAG. The structure of COPI vesicles and regulation of vesicle turnover. FEBS Lett. 2023;597(6):819-835. doi:10.1002/1873-3468.14560. PMID: 36513395

16. [todd-2013-COPI-RNA-binding-abstract] Todd AG, Lin H, Ebert AD, Liu Y, Androphy EJ. COPI transport complexes bind to specific RNAs in neuronal cells. Hum Mol Genet. 2013;22(4):729-736. doi:10.1093/hmg/dds480. PMID: 23175440

17. [peter-2011-COPI-SMN-axons-abstract] Peter CJ, Evans M, Thayanithy V, et al. The COPI vesicle complex binds and moves with survival motor neuron within axons. Hum Mol Genet. 2011;20(9):1701-1711. doi:10.1093/hmg/ddr046. PMID: 21300694


## Citations

1. bainter-2021-COPG1-immunodeficiency-abstract.md
2. beck-2009-COPI-review-summary.md
3. bethune-2020-COPG1-COPG2-neuronal-abstract.md
4. dodonova-2017-COPI-structure-9A-abstract.md
5. harter-1998-p23-gamma-COP-abstract.md
6. jackson-2012-dilysine-COPI-abstract.md
7. ma-2013-dilysine-rules-abstract.md
8. moelleken-2007-coatomer-isoforms-golgi-abstract.md
9. nickel-1997-p23-cycling-abstract.md
10. peter-2011-COPI-SMN-axons-abstract.md
11. sohn-1996-p23-coatomer-binding-abstract.md
12. steiner-2022-COPI-STING-abstract.md
13. taylor-2023-COPI-structure-review-abstract.md
14. todd-2013-COPI-RNA-binding-abstract.md
15. watson-2004-gamma-COP-appendage-abstract.md
16. weimer-2008-ArfGAP-differential-abstract.md
17. yu-2012-Arf1-coatomer-recruitment-abstract.md