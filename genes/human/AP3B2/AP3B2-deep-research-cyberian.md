---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T15:38:00.729770'
end_time: '2026-01-15T15:53:23.099787'
duration_seconds: 922.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AP3B2
  gene_symbol: AP3B2
  uniprot_accession: Q13367
  protein_description: 'RecName: Full=AP-3 complex subunit beta-2; AltName: Full=Adaptor
    protein complex AP-3 subunit beta-2; AltName: Full=Adaptor-related protein complex
    3 subunit beta-2; AltName: Full=Beta-3B-adaptin; AltName: Full=Clathrin assembly
    protein complex 3 beta-2 large chain; AltName: Full=Neuron-specific vesicle coat
    protein beta-NAP;'
  gene_info: Name=AP3B2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the adaptor complexes large subunit family.
  protein_domains: AP3_beta. (IPR026740); AP3B1/2_C. (IPR056314); AP3B_C. (IPR029390);
    AP_beta. (IPR026739); ARM-like. (IPR011989)
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
- **UniProt Accession:** Q13367
- **Protein Description:** RecName: Full=AP-3 complex subunit beta-2; AltName: Full=Adaptor protein complex AP-3 subunit beta-2; AltName: Full=Adaptor-related protein complex 3 subunit beta-2; AltName: Full=Beta-3B-adaptin; AltName: Full=Clathrin assembly protein complex 3 beta-2 large chain; AltName: Full=Neuron-specific vesicle coat protein beta-NAP;
- **Gene Information:** Name=AP3B2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the adaptor complexes large subunit family.
- **Key Domains:** AP3_beta. (IPR026740); AP3B1/2_C. (IPR056314); AP3B_C. (IPR029390); AP_beta. (IPR026739); ARM-like. (IPR011989)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AP3B2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AP3B2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AP3B2** (gene ID: AP3B2, UniProt: Q13367) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AP3B2: A Comprehensive Review of the Neuronal AP-3 Complex Beta Subunit

## Introduction

AP3B2 (adaptor-related protein complex 3 subunit beta-2), also known as beta-NAP (neuronal adaptin-like protein beta-subunit) or beta-3B-adaptin, is the neuron-specific beta subunit of the adaptor protein complex 3 (AP-3). This protein plays a critical role in vesicular trafficking, particularly in the biogenesis of synaptic vesicles from endosomes in neurons. The protein was first identified in 1995 as the target antigen in paraneoplastic cerebellar degeneration, establishing it as a neuron-specific vesicle coat protein closely related to beta-adaptin and beta-COP coat proteins [newman-1995-betanap-abstract].

The AP-3 complex is a heterotetrameric adaptor complex implicated in trafficking cargo proteins from the trans-Golgi network (TGN) and/or endosomes to lysosomes or lysosome-related organelles (LROs) [ma-2021-ap3-review-summary]. Unlike the ubiquitously expressed AP3B1 (beta3A) isoform, AP3B2 (beta3B) expression is restricted to neurons, where it serves specialized functions in synaptic vesicle biogenesis and neurotransmitter release. This tissue-specific expression pattern underlies the distinct neurological phenotypes observed in AP3B2 deficiency, which include epileptic encephalopathy and developmental delay, in contrast to the albinism and bleeding disorders caused by defects in the ubiquitous AP3B1 isoform [seong-2005-neuronal-ubiquitous-ap3-abstract].

## Structure and Domain Organization

AP3B2 is a large protein of approximately 1081 amino acids that serves as one of the two large subunits of the AP-3 complex. The AP-3 complex is a heterotetramer composed of two large adaptins (delta-type subunit AP3D1 and beta-type subunit AP3B1 or AP3B2), a medium adaptin (mu-type subunit AP3M1 or AP3M2), and a small adaptin (sigma-type subunit AP3S1 or AP3S2) [ma-2021-ap3-review-summary]. The structural organization of AP3B2 follows the general architecture of beta-adaptins, consisting of a trunk domain that participates in core complex formation, a flexible hinge region, and a C-terminal ear domain.

The domain architecture of AP3B2 includes several characterized regions. The N-terminal trunk domain (approximately amino acids 1-642) contributes to the formation of the protease-resistant core of the AP-3 complex together with fragments of the delta subunit and the full-length mu3 and sigma3 subunits. The hinge region (approximately amino acids 647-796 in beta3B) connects the trunk to the ear domain and contains multiple phosphorylation sites that are substrates for casein kinase I [faundez-2000-casein-kinase-abstract]. Sequence analysis has identified 13 D/EXXS consensus sites for casein kinase I clustered in the acidic hinge region of beta3B, compared to 22 such sites in beta3A. The C-terminal ear domain (approximately amino acids 799-1081 in beta3B) contains the clathrin-binding region and interacts with accessory proteins involved in vesicular transport.

InterPro domain analysis identifies several conserved features in AP3B2, including the AP3_beta domain (IPR026740), AP3B1/2_C domain (IPR056314), AP3B_C domain (IPR029390), the AP_beta domain (IPR026739), and ARM-like repeats (IPR011989). The protein belongs to the adaptor complexes large subunit family, sharing structural homology with beta-adaptins from other AP complexes while possessing unique features that contribute to AP-3-specific functions.

A 2024 study provided major structural insights into the AP-3 complex through cryo-EM analysis, elucidating the mechanism of clathrin-independent coat formation [dickinson-2024-ap3-structure-abstract]. This work revealed that dimerization of AP-3 is mediated by the small GTPase Arf1, using the same interface that mediates Arf polymerization. Notably, in humans, AP-3 delta has only a single isoform (AP3D1), whereas beta3 has multiple isoforms (AP3B1, AP3B2), which is the inverse of AP-1. The structural analysis identified a stepwise conformational activation mechanism: AP-3 is conformationally flexible upon initial membrane recruitment but becomes rigidified upon engagement with tyrosine-based cargo. Cargo binding precedes engagement with a second copy of Arf1, which "locks" the complex into a rigid conformation and templates initial dimerization of cargo-bound AP-3. Three distinct structural states were identified: AP-3 bound to a single Arf1 on the delta subunit, AP-3 bound to two Arf1 copies with LAMP1 cargo, and a dimer of the double-Arf1-cargo-AP-3 complex. These structures provide a detailed mechanistic framework for understanding how AP-3 functions as a clathrin-independent coat in endosomal compartments.

## Role in AP-3 Complex Assembly and Regulation

The assembly of the AP-3 complex requires the coordinated association of its four subunits. AP3B2 contributes to complex stability and membrane recruitment through multiple mechanisms. The trunk domain of AP3B2 participates in forming the core complex by interacting with the delta subunit (AP3D1) and providing a scaffold for the medium (mu3) and small (sigma3) subunits. This assembly results in a functional adaptor that can recognize cargo proteins and recruit coat machinery.

A critical regulatory mechanism involves the phosphorylation of the AP-3 beta3 subunit. Research has demonstrated that phosphorylation of the AP-3 adaptor complex is linked with synaptic vesicle coating, with phosphorylation occurring in the beta3 subunit by a kinase similar to casein kinase 1 alpha [faundez-2000-casein-kinase-abstract]. The kinase copurifies with neuronal-specific AP-3, and purified casein kinase I selectively phosphorylates both beta3A and beta3B subunits at their hinge domains. This phosphorylation event appears to facilitate coat assembly and stabilization during vesicle budding. Blocking casein kinase I activity reduces synaptic vesicle production in PC12 cells by approximately 50%, demonstrating the physiological relevance of this modification.

The membrane recruitment of AP-3 is regulated by the small GTPase ARF1 (ADP-ribosylation factor 1). In the presence of GTP-bound ARF1, AP-3 is recruited to membranes and undergoes a conformational change to an open state where both the YXXO and [DE]XXXL[LI] motif-binding sites become exposed for cargo recognition [ma-2021-ap3-review-summary]. This ARF-dependent recruitment mechanism ensures spatial and temporal control of AP-3-mediated trafficking.

## Cargo Recognition and Sorting Signals

The AP-3 complex, including the neuronal form containing AP3B2, recognizes two primary types of sorting signals in the cytoplasmic tails of transmembrane cargo proteins. The first is the tyrosine-based YXXO motif (where X is any amino acid and O is a bulky hydrophobic residue), which is recognized by the mu3 subunit. The second is the dileucine-based [DE]XXXL[LI] motif, which is recognized by the delta-sigma3 hemicomplex.

Structural studies have elucidated the molecular basis for signal recognition. The crystal structure of the C-terminal domain of mu3A in complex with a YXXO signal peptide reveals an immunoglobulin-like beta-sandwich organization with two subdomains that form the signal-binding pocket. This recognition mechanism is conserved among AP complexes, though AP-3 shows preferences for specific cargo proteins destined for lysosomes and lysosome-related organelles.

Key cargo proteins recognized by neuronal AP-3 include the zinc transporter ZnT3 and the chloride channel ClC-3. The ZnT3 cytosolic tail interacts selectively with AP-3 in cell-free assays, and this interaction is functionally significant for targeting ZnT3 to synaptic vesicles [salazar-2004-znt3-ap3-abstract]. Pharmacological disruption of AP-3-dependent versus AP-2-dependent synaptic-like microvesicle (SLMV) biogenesis preferentially reduces ZnT3 or synaptophysin targeting, respectively, demonstrating that these cargo proteins are sorted through distinct pathways. ClC-3 is similarly targeted to synaptic vesicles through the AP-3 pathway, and co-localization of ClC-3 and ZnT3 in common vesicle populations enables functional interactions that determine vesicle luminal composition.

In non-neuronal contexts, AP-3 also mediates trafficking of lysosomal membrane proteins such as LAMP-1 and LAMP-2, as well as melanocyte-specific proteins like tyrosinase. Inhibition of AP-3 function leads to misrouting of these proteins to the cell surface rather than to lysosomes or melanosomes. The dileucine signals in tyrosinase and the lysosomal membrane protein Limp-II were among the first cargo signals shown to bind AP-3.

## Cellular Localization and Trafficking Pathways

AP3B2 and the neuronal AP-3 complex exhibit a distinct subcellular localization pattern that differs from the ubiquitous AP-3 isoform. In neurons, AP3B2-containing complexes are preferentially targeted to neuronal processes, including axons and dendrites, while ubiquitous AP-3 (containing AP3B1) is restricted primarily to the cell body [seong-2005-neuronal-ubiquitous-ap3-abstract]. This differential localization underlies the specialized functions of neuronal AP-3 in synaptic vesicle biogenesis.

At the subcellular level, AP-3 is primarily associated with tubular endosomal compartments, the trans-Golgi network, and synaptic vesicle membranes. Quantitative immunoelectron microscopy has demonstrated that the majority of AP-3 immunoreactivity in both striatum and hippocampus localizes to presynaptic axonal compartments, where it regulates synaptic vesicle size and composition [newell-litwa-2010-striatum-hippocampus-abstract]. The localization to early endosomal tubular networks positions AP-3 to function in the sorting of cargo proteins from this compartment to synaptic vesicles.

The trafficking pathway mediated by neuronal AP-3 involves the budding of vesicles from endosomal membranes. This process requires ARF1, ATP, and the appropriate temperature, as demonstrated in reconstitution experiments using PC12 cell endosomes [faundez-1998-ap3-synaptic-vesicle-abstract]. Budding from washed membranes can be reconstituted with purified AP-3 and recombinant ARF1, establishing that AP-3 coating is sufficient for vesicle formation from endosomes. This pathway is distinct from the AP-2-dependent pathway of synaptic vesicle recycling from the plasma membrane.

## Neuronal Function and Synaptic Vesicle Biogenesis

The most significant function of AP3B2 lies in its role in synaptic vesicle biogenesis and neurotransmitter release. Unlike the ubiquitous AP3B1 isoform, which primarily mediates trafficking to lysosomes, the neuronal AP-3 complex containing AP3B2 generates synaptic vesicles from endosomes [faundez-1998-ap3-synaptic-vesicle-abstract]. This distinction has been demonstrated experimentally: only the neuronal form of AP-3 can produce synaptic vesicles from endosomes in vitro, although both isoforms can bind to purified synaptic vesicles in the presence of GTP-gamma-S.

Genetic studies using knockout mice have provided compelling evidence for the specialized functions of AP3B2. Mice lacking AP3B2 (Ap3b2-/-) exhibit complex neurological and behavioral impairments, including tonic-clonic seizures and hyperactivity, while maintaining normal coat color [seong-2005-neuronal-ubiquitous-ap3-abstract]. In contrast, mice lacking AP3B1 (Ap3b1-/-) display coat color dilution (light gray) due to impaired melanogenesis but show no neurological abnormalities. This phenotypic dichotomy reflects the tissue-specific expression and function of the two isoforms.

The loss of AP3B2 has profound effects on synaptic vesicle composition and function. Beta3B deficiency compromises synaptic zinc stores, as assessed by Timm's staining, and reduces the synaptic vesicle targeting of membrane proteins involved in zinc uptake, including ZnT3 and ClC-3 [seong-2005-neuronal-ubiquitous-ap3-abstract]. Interestingly, loss of the ubiquitous isoform (beta3A) has the opposite effect, significantly increasing synaptic zinc and zinc transporter content. This suggests that the two AP-3 isoforms exert concerted but opposing control over synaptic vesicle protein composition.

The impact of AP-3 on neurotransmitter release is complex and transmitter-specific. Studies have shown that AP-3 is required specifically for the release of dopamine but not glutamate, revealing an unrecognized linkage between the pathway of synaptic vesicle recycling and the properties of exocytosis. Furthermore, vesicles derived via the AP-3-dependent recycling pathway contribute specifically to asynchronous neurotransmitter release rather than the synchronous component [grabner-2014-asynchronous-release-abstract]. Selective elimination of AP-3-dependent vesicles diminishes asynchronous release, which affects the precision of postsynaptic firing in response to natural stimulation patterns.

A major advance in understanding AP3B2 function came from a 2023 Nature Neuroscience study that identified the molecular mechanism by which AP-3 influences high-frequency neurotransmitter release [xu-2023-atp8a1-flippase-abstract]. Neural systems encode information in the frequency of action potentials, but rapid synchronous release depletes synaptic vesicles, limiting release at high firing rates. The study demonstrated that in mouse hippocampal neurons and slices, AP-3 generates a subset of synaptic vesicles that respond specifically to high-frequency stimulation. Proteomics analysis identified the phospholipid flippase ATP8A1 and its auxiliary subunit TMEM30A as AP-3-dependent synaptic vesicle cargoes. Loss of ATP8A1 recapitulates the defect in synaptic vesicle mobilization at high frequency observed with loss of AP-3. The mechanism involves ATP8A1's flippase activity regulating the distribution of phosphatidylserine in synaptic vesicles, which in turn enables phosphatidylserine-dependent recruitment of synapsins by the cytoplasmically oriented phosphatidylserine. This discovery elucidates how neurons encode firing-rate information through distinct vesicle populations generated by AP-3.

The role of AP-3 in dopaminergic neurotransmission has also been clarified by recent work showing that AP-3 has two independent functions in dopamine neurons [jain-2023-phasic-dopamine-abstract]. First, AP-3 confers axonal polarity of dopamine release by targeting vesicular monoamine transporter 2 (VMAT2) to axons rather than dendrites. Second, AP-3 acting locally at nerve terminals produces synaptic vesicles that respond specifically to high-frequency stimulation. Conditional inactivation of VPS41, an AP-3-interacting protein, in dopamine neurons impairs reinforcement learning due to defective frequency-dependent dopamine release rather than reduced total dopamine output. These findings establish AP-3 as essential for the phasic dopamine signaling underlying learning and reward processing.

## Interaction with BLOC-1 Complex

The function of neuronal AP-3 is modulated by its interaction with the BLOC-1 (biogenesis of lysosome-related organelles complex-1) complex. Both AP-3 and BLOC-1 are associated with Hermansky-Pudlak syndrome in humans and have been implicated in synaptic vesicle biogenesis in animal models [newell-litwa-2009-bloc1-ap3-abstract]. The interaction between AP-3 and BLOC-1 complexes observed in non-neuronal cells is recapitulated in PC12 cells and mouse primary cultured neurons.

Interestingly, AP-3 and BLOC-1 differentially regulate presynaptic composition in a brain region-specific manner. BLOC-1 deficiencies selectively reduce AP-3 and AP-3 cargo immunoreactivity in presynaptic compartments within the dentate gyrus of the hippocampus but do not produce these phenotypes in the striatum [newell-litwa-2010-striatum-hippocampus-abstract]. This suggests that BLOC-1 acts as a brain region-specific regulator of AP-3 function.

The functional relationship between AP-3 and BLOC-1 is not obligatory for all cargo proteins. Both AP-3 isoforms recognize distinct as well as overlapping membrane protein cargoes independently of BLOC-1, and not all synaptic vesicle proteins reach synaptic vesicle pools through an AP-3-BLOC-1 route [newell-litwa-2009-bloc1-ap3-abstract]. This suggests multiple parallel pathways for synaptic vesicle protein sorting, with the AP-3-BLOC-1 pathway representing one specialized route.

## Disease Associations

### Developmental and Epileptic Encephalopathy 48 (DEE48)

The most significant disease association for AP3B2 is developmental and epileptic encephalopathy 48 (DEE48; OMIM #617276), a severe autosomal recessive neurological disorder. DEE48 was first described in 2016 when Assoum and colleagues identified homozygous or compound heterozygous mutations in AP3B2 as the cause of early-onset epileptic encephalopathy in 12 patients from 8 unrelated families [assoum-2016-dee48-abstract].

The clinical phenotype of DEE48 is characterized by a homogeneous presentation including severe global developmental delay with intellectual disability and absent speech, poor motor development with most patients unable to sit or walk, and onset of seizures typically before 9 months of age. The seizures are often refractory and may include hypsarrhythmia and status epilepticus. Additional features include postnatal microcephaly (in approximately 75% of cases), hypotonia, poor eye contact with optic atrophy, stereotypical hand movements, dyskinesia, and sleep disturbances. Notably, patients with DEE48 do not exhibit spasticity, albinism, or hematological symptoms, distinguishing this condition from Hermansky-Pudlak syndrome type 2 caused by AP3B1 mutations.

Brain imaging abnormalities in DEE48 may include enlarged ventricles, cerebral and cerebellar atrophy, and thin corpus callosum. Functional analysis of the mutations suggests a loss-of-function mechanism, consistent with the critical role of AP3B2 in neuronal synaptic vesicle trafficking and neurotransmitter release.

### Paraneoplastic Cerebellar Degeneration

AP3B2 was originally identified as the target antigen (beta-NAP) in paraneoplastic cerebellar degeneration [newman-1995-betanap-abstract]. Anti-Nb antibodies (now known as anti-AP3B2 antibodies) are markers of an autoimmune disorder characterized predominantly by gait instability. Patients may present with cerebellar, dorsal column, or sensory neuronal dysfunction, with symptoms including cerebellar ataxia, spinocerebellar ataxia, myelopathy, sensory neuronopathy, and autonomic neuropathy.

The diversity of neurological symptoms correlates with the extensive binding of AP3B2 antibodies to spinal cord gray matter, dorsal root ganglia, cerebellar cortex, and nucleus. Given its intracellular location, AP3B2 antibody is unlikely to be directly pathogenic; rather, it serves as a biomarker for CD8+ cytotoxic T cell-mediated damage. Immunotherapy may be warranted given reports of clinical improvement in some cases, though the disorder has historically been associated with subacute onset and limited response to treatment.

## Open Questions

Despite significant advances in understanding AP3B2 function, several important questions remain unresolved:

1. **Precise trafficking itinerary**: The exact sequence of steps by which AP-3 mediates cargo transport from the TGN or endosomes to synaptic vesicles has not been fully elucidated. Whether AP-3 vesicles fuse directly with forming synaptic vesicles or pass through intermediate compartments remains unclear.

2. **Coat dynamics**: The fate of AP-3 during vesicle maturation and whether AP-3 is recycled back to donor membranes after vesicle formation requires further investigation. Recent evidence suggests that AP-3 vesicles retain their coat after budding and complete uncoating occurs only after tethering at the destination membrane.

3. **Alternative coat proteins**: While clathrin can associate with AP-3, the identification of other coat proteins such as VPS41 raises questions about the complete molecular composition of the AP-3 vesicle coat and whether different coat assemblies serve distinct functions.

4. **Lipid interactions**: Direct interactions between AP-3 and membrane lipids have not been definitively identified. Understanding which phosphoinositides or other lipids regulate AP-3 recruitment and function could reveal new regulatory mechanisms.

5. **Therapeutic targets**: For DEE48 and related AP3B2-associated disorders, identifying therapeutic approaches that could compensate for loss of AP3B2 function or enhance alternative trafficking pathways represents an important translational goal.

6. **Region-specific effects**: The mechanisms underlying the differential effects of AP-3 loss in different brain regions (e.g., opposite effects on synaptic vesicle size in striatum versus dentate gyrus) warrant further investigation.

7. **Cargo specificity**: The complete repertoire of neuronal AP-3 cargoes and how cargo selection differs between neuronal and ubiquitous AP-3 isoforms remains to be fully characterized.

## References

- [newman-1995-betanap-abstract] Newman LS, McKeever MO, Okano HJ, Darnell RB. Beta-NAP, a cerebellar degeneration antigen, is a neuron-specific vesicle coat protein. Cell. 1995 Sep 8;82(5):773-83. PMID: 7545544. DOI: 10.1016/0092-8674(95)90474-3

- [faundez-1998-ap3-synaptic-vesicle-abstract] Faundez V, Horng JT, Kelly RB. A function for the AP3 coat complex in synaptic vesicle formation from endosomes. Cell. 1998 May 1;93(3):423-32. PMID: 9590176. DOI: 10.1016/s0092-8674(00)81170-8

- [faundez-2000-casein-kinase-abstract] Faundez VV, Kelly RB. The AP-3 complex required for endosomal synaptic vesicle biogenesis is associated with a casein kinase Ialpha-like isoform. Mol Biol Cell. 2000 Aug;11(8):2591-604. PMID: 10930456. PMCID: PMC14942. DOI: 10.1091/mbc.11.8.2591

- [salazar-2004-znt3-ap3-abstract] Salazar G, Love R, Werner E, et al. The zinc transporter ZnT3 interacts with AP-3 and it is preferentially targeted to a distinct synaptic vesicle subpopulation. Mol Biol Cell. 2004 Feb;15(2):575-87. PMID: 14657250. PMCID: PMC329249. DOI: 10.1091/mbc.e03-06-0401

- [seong-2005-neuronal-ubiquitous-ap3-abstract] Seong E, Wainer BH, Hughes ED, Saunders TL, Burmeister M, Faundez V. Genetic analysis of the neuronal and ubiquitous AP-3 adaptor complexes reveals divergent functions in brain. Mol Biol Cell. 2005 Jan;16(1):128-40. PMID: 15537701. PMCID: PMC539158. DOI: 10.1091/mbc.e04-10-0892

- [newell-litwa-2009-bloc1-ap3-abstract] Newell-Litwa K, Salazar G, Smith Y, Faundez V. Roles of BLOC-1 and adaptor protein-3 complexes in cargo sorting to synaptic vesicles. Mol Biol Cell. 2009 Mar;20(5):1441-53. PMID: 19116307. PMCID: PMC2649251. DOI: 10.1091/mbc.e08-05-0456

- [newell-litwa-2010-striatum-hippocampus-abstract] Newell-Litwa K, et al. Hermansky-Pudlak protein complexes, AP-3 and BLOC-1, differentially regulate presynaptic composition in the striatum and hippocampus. J Neurosci. 2010 Jan 20;30(3):820-31. PMID: 20089890. DOI: 10.1523/JNEUROSCI.3400-09.2010

- [grabner-2014-asynchronous-release-abstract] Grabner CP, et al. Vesicles derived via AP-3-dependent recycling contribute to asynchronous release and influence information transfer. Nat Commun. 2015 Nov;6:8530. PMID: 26449320. PMCID: PMC4239664. DOI: 10.1038/ncomms6530

- [assoum-2016-dee48-abstract] Assoum M, Philippe C, Isidor B, et al. Autosomal-Recessive Mutations in AP3B2, Adaptor-Related Protein Complex 3 Beta 2 Subunit, Cause an Early-Onset Epileptic Encephalopathy with Optic Atrophy. Am J Hum Genet. 2016 Dec 1;99(6):1368-1376. PMID: 27889060. PMCID: PMC5142104. DOI: 10.1016/j.ajhg.2016.10.009

- [ma-2021-ap3-review-summary] Ma Z, Islam MN, Xu T, Song E. AP-3 adaptor complex-mediated vesicle trafficking. Biophysics Reports. 2021;7(5):445-456. PMCID: PMC10235903. DOI: 10.52601/bpr.2021.200051

- [scheuber-2006-ap3-mossy-fiber-abstract] Scheuber A, et al. Loss of AP-3 function affects spontaneous and evoked release at hippocampal mossy fiber synapses. Proc Natl Acad Sci U S A. 2006 Oct 31;103(44):16562-7. PMID: 17056716. DOI: 10.1073/pnas.0603511103

- [xu-2023-atp8a1-flippase-abstract] Xu H, Oses-Prieto JA, Khvotchev M, Jain S, Liang J, Burlingame A, Edwards RH. Adaptor protein AP-3 produces synaptic vesicles that release at high frequency by recruiting phospholipid flippase ATP8A1. Nat Neurosci. 2023 Oct;26(10):1685-1700. PMID: 37723322. DOI: 10.1038/s41593-023-01434-0

- [jain-2023-phasic-dopamine-abstract] Jain S, Yee AG, Maas J, et al. Adaptor Protein-3 Produces Synaptic Vesicles that Release Phasic Dopamine. Proc Natl Acad Sci U S A. 2023 Sep;120(36):e2309843120. PMID: 37609166. PMCID: PMC10483624. DOI: 10.1073/pnas.2309843120

- [dickinson-2024-ap3-structure-abstract] A structure-based mechanism for initiation of AP-3 coated vesicle formation. Proc Natl Acad Sci U S A. 2024 Dec. PMID: 38895279. PMCID: PMC11670113. DOI: 10.1073/pnas.2411974121

- OMIM #617276: Developmental and Epileptic Encephalopathy 48 (DEE48). https://omim.org/entry/617276

- OMIM *602166: AP3B2 Gene Entry. https://omim.org/entry/602166

- UniProt Q13367: AP3B2 Human Entry. https://www.uniprot.org/uniprotkb/Q13367/entry

- GeneCards AP3B2: https://www.genecards.org/cgi-bin/carddisp.pl?gene=AP3B2


## Citations

1. assoum-2016-dee48-abstract.md
2. dickinson-2024-ap3-structure-abstract.md
3. faundez-1998-ap3-synaptic-vesicle-abstract.md
4. faundez-2000-casein-kinase-abstract.md
5. grabner-2014-asynchronous-release-abstract.md
6. jain-2023-phasic-dopamine-abstract.md
7. ma-2021-ap3-review-summary.md
8. newell-litwa-2009-bloc1-ap3-abstract.md
9. newell-litwa-2010-striatum-hippocampus-abstract.md
10. newman-1995-betanap-abstract.md
11. salazar-2004-znt3-ap3-abstract.md
12. scheuber-2006-ap3-mossy-fiber-abstract.md
13. seong-2005-neuronal-ubiquitous-ap3-abstract.md
14. xu-2023-atp8a1-flippase-abstract.md