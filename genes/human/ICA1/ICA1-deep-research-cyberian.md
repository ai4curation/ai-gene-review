---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T18:09:05.099188'
end_time: '2026-01-22T18:26:39.816339'
duration_seconds: 1054.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ICA1
  gene_symbol: ICA1
  uniprot_accession: Q05084
  protein_description: 'RecName: Full=Islet cell autoantigen 1; AltName: Full=69 kDa
    islet cell autoantigen; Short=ICA69; AltName: Full=Islet cell autoantigen p69;
    Short=ICAp69; Short=p69;'
  gene_info: Name=ICA1;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: AH/BAR_dom_sf. (IPR027267); AH_dom. (IPR010504); Islet_autoAg_Ica1/Ica1-like.
    (IPR024114); Islet_autoAg_Ica1_C. (IPR006723); Arfaptin (PF06456)
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
- **UniProt Accession:** Q05084
- **Protein Description:** RecName: Full=Islet cell autoantigen 1; AltName: Full=69 kDa islet cell autoantigen; Short=ICA69; AltName: Full=Islet cell autoantigen p69; Short=ICAp69; Short=p69;
- **Gene Information:** Name=ICA1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AH/BAR_dom_sf. (IPR027267); AH_dom. (IPR010504); Islet_autoAg_Ica1/Ica1-like. (IPR024114); Islet_autoAg_Ica1_C. (IPR006723); Arfaptin (PF06456)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ICA1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ICA1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ICA1** (gene ID: ICA1, UniProt: Q05084) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ICA1 (Islet Cell Autoantigen 1): A Comprehensive Review

## Introduction and Summary

Islet cell autoantigen 1 (ICA1), also known as ICA69 or ICAp69, is a 483-amino acid protein originally identified as an autoantigen in type 1 diabetes mellitus [pietropaolo-1993-ica69-discovery-abstract]. Encoded by the ICA1 gene on chromosome 7p21.3, this protein has emerged as a multifunctional regulator with critical roles in dense-core vesicle biogenesis, neuroendocrine secretion, and membrane trafficking at the trans-Golgi network (TGN). ICA69 contains an N-terminal BAR (Bin/Amphiphysin/Rvs) domain that enables it to sense membrane curvature and facilitate vesicle budding, functions that are conserved from nematodes to humans [bhimsen-2000-ric19-abstract]. The protein is predominantly expressed in tissues with high secretory activity, including the brain, pancreas, and stomach mucosa, where it localizes to the Golgi complex and immature secretory granules [spitzenberger-2003-golgi-abstract].

ICA69 functions primarily through heterodimerization with PICK1 (protein interacting with C kinase 1), another BAR domain protein [cao-2013-pick1-ica69-trafficking-abstract]. These heteromeric complexes play essential roles in insulin granule formation and maturation in pancreatic beta cells. Knockout studies in mice have demonstrated that loss of either ICA69 or PICK1 leads to glucose intolerance, reduced insulin secretion, and accumulation of proinsulin, establishing these proteins as key regulators of metabolic homeostasis [cao-2013-pick1-ica69-trafficking-abstract]. Beyond its role in glucose metabolism, ICA69 has been implicated in neurotransmitter release, synaptic plasticity, and has been identified as a shared autoantigen in type 1 diabetes, Sjögren's syndrome, and potentially other autoimmune conditions [winer-2002-sjogren-abstract][fan-2014-multiorgan-autoimmunity-abstract]. Recent genetic studies have also linked ICA1 variants to autism spectrum disorder and schizophrenia [kushima-2018-cnv-asd-scz-abstract].

## Gene and Protein Structure

The human ICA1 gene spans approximately 296 kilobases on chromosome 7p21.3 and contains 21 exons that can produce multiple transcript variants through alternative splicing. The canonical protein product consists of 483 amino acids with a predicted molecular weight of approximately 69 kDa, hence the alternative designation ICA69 [pietropaolo-1993-ica69-discovery-abstract]. When the protein was first cloned in 1993, it showed no significant homology to any known sequences in GenBank, except for two short regions of limited similarity with bovine serum albumin [pietropaolo-1993-ica69-discovery-abstract].

Subsequent structural analyses revealed that ICA69 contains an N-terminal arfaptin homology/BAR domain superfamily region (approximately residues 1-250) that shares similarity with the ARF1-binding region of arfaptin proteins [spitzenberger-2003-golgi-abstract]. This domain adopts a banana-shaped, anti-parallel coiled-coil structure characteristic of BAR domain proteins, enabling it to sense and induce membrane curvature [cao-2013-pick1-ica69-trafficking-abstract]. Although no crystal structure of ICA69 itself has been published, its BAR domain structure has been inferred from homologous proteins; the crystal structure of Drosophila Amphiphysin BAR domain shows striking similarity to the GTPase-binding domain of Arfaptin 2, despite weak sequence conservation, suggesting a conserved structural fold across the BAR domain superfamily.

The C-terminal region of ICA69, designated ICAC (ICA69 C-terminal domain), is unique to the ICA69 protein family and contributes to protein-protein interactions and subcellular targeting [wang-2013-ica69-pkca-trafficking-abstract]. Importantly, the ICAC domain represents a functionally distinct module from the N-terminal BAR domain, with different binding properties. Studies have demonstrated that ICAC directly associates with PICK1 and plays a critical role in regulating the trafficking of the PICK1-PKCα (protein kinase C alpha) complex to the plasma membrane [wang-2013-ica69-pkca-trafficking-abstract]. Overexpression of ICAC specifically interferes with PKCα-mediated PICK1 translocation, whereas the BAR domain-containing region does not. This dual-domain architecture allows ICA69 to participate in both membrane curvature sensing (via the BAR domain) and signaling pathway regulation (via ICAC).

A paralogue of ICA1, designated ICA1L (ICA1-like), exists in vertebrates and shows similar domain architecture [he-2015-ica1l-pick1-acrosome-abstract]. While ICA69 is the predominant PICK1 binding partner in brain and pancreas, ICA1L serves this role in the testes, where it is essential for acrosome formation during spermiogenesis [he-2015-ica1l-pick1-acrosome-abstract]. The evolutionary conservation of the ICA69 family is remarkable, with the *Caenorhabditis elegans* homologue RIC-19 (resistance to inhibitors of cholinesterase-19) sharing 33% identity with human ICA69 across the conserved domains, including a 58% conserved stretch that likely represents critical functional motifs [bhimsen-2000-ric19-abstract].

## Subcellular Localization

ICA69 exhibits a complex subcellular distribution pattern that reflects its dynamic role in vesicular trafficking. The majority of the cellular ICA69 pool exists as a soluble cytosolic protein; however, a significant subpopulation associates with membranes, particularly those of the Golgi complex and immature secretory granules [spitzenberger-2003-golgi-abstract][bhimsen-2000-ric19-abstract]. Immunofluorescence microscopy in insulinoma INS-1 cells revealed that ICA69 is enriched in the perinuclear region, colocalizing with markers of the Golgi apparatus and, to a lesser extent, with immature insulin-containing secretory granules [spitzenberger-2003-golgi-abstract].

Immunoelectron microscopy studies confirmed this localization and provided a critical insight into the dynamics of ICA69 association with secretory granules: virtually no ICA69 immunogold labeling was observed on mature secretory granules near the plasma membrane [spitzenberger-2003-golgi-abstract]. This observation was subsequently explained by studies showing that ICA69 is present on immature granules near the TGN as part of PICK1-ICA69 heteromeric complexes, but dissociates from granules during maturation, leaving only PICK1 on mature granules [cao-2013-pick1-ica69-trafficking-abstract].

In neuronal tissue, subcellular fractionation of mouse brain demonstrated that while most ICA69 is cytosolic, a subpopulation is membrane-bound and coenriched with synaptic vesicles [bhimsen-2000-ric19-abstract]. In pancreatic beta cells, ICA69 displayed punctate distribution that was distinct from insulin-containing dense-core granules, suggesting association with synaptic-like microvesicles or immature granule compartments rather than mature secretory granules [bhimsen-2000-ric19-abstract]. The tissue distribution of ICA69 correlates with secretory activity, with the highest expression levels found in brain, pancreas, and stomach mucosa, moderate levels in heart and thyroid, and low or absent expression in skeletal muscle, placenta, spleen, and ovary [pietropaolo-1993-ica69-discovery-abstract].

## Molecular Function: Role in Dense-Core Vesicle Biogenesis

The primary molecular function of ICA69 is to regulate the biogenesis and maturation of dense-core vesicles (DCVs), also known as large dense-core vesicles (LDCVs), in neuroendocrine cells. This function is mediated through its BAR domain, which can sense and induce membrane curvature, and through its obligate partnership with PICK1 [cao-2013-pick1-ica69-trafficking-abstract]. The current model of ICA69 function, derived primarily from studies in pancreatic beta cells and *C. elegans* neurons, positions it as a key player in the early stages of DCV formation at the TGN.

PICK1 and ICA69 form tight heteromeric complexes in pancreatic beta cells and mutually depend on each other for normal expression and stability [cao-2013-pick1-ica69-trafficking-abstract]. PICK1 deficiency in mice causes complete loss of ICA69 protein, despite normal ICA69 mRNA levels, indicating that the proteins stabilize each other through heterodimerization [cao-2013-pick1-ica69-trafficking-abstract]. The PICK1-ICA69 heterodimer directly assists in the process of budding from the TGN and regulates maturation of insulin granules [pihlstrøm-2022-pick1-variants-diabetes-abstract]. During this process, the BAR domains of both proteins work in concert to generate the membrane curvature necessary for vesicle budding, while PICK1's PDZ domain couples cargo proteins to the nascent vesicle.

A key feature of ICA69 function is its transient association with secretory granules. The protein is present on immature secretory granules near the TGN but dissociates as granules mature [cao-2013-pick1-ica69-trafficking-abstract][spitzenberger-2003-golgi-abstract]. This dynamic behavior suggests that ICA69 functions specifically in the early stages of granule biogenesis—potentially in membrane budding, cargo sorting, or the initial stages of granule maturation—but is not required for the later steps of granule trafficking or exocytosis. Recent work using advanced microscopy techniques demonstrated that PICK1 transiently associates with immature secretory granules before departing via vesicular budding, and ICA69 likely follows a similar pattern as part of the heteromeric complex [pihlstrøm-2022-pick1-variants-diabetes-abstract].

## Lipid Binding and Membrane Interactions

The membrane-associated functions of ICA69 depend on its ability to bind phospholipids and sense membrane curvature through its BAR domain. Like other BAR domain proteins, ICA69 contains an amphipathic helix N-terminal to the BAR domain proper that contributes to phospholipid binding and membrane curvature sensing [pihlstrøm-2022-pick1-variants-diabetes-abstract]. The BAR domain adopts a crescent-shaped, positively charged concave surface that interacts with negatively charged lipid membranes, allowing it to both sense existing membrane curvature and actively induce curvature through electrostatic interactions.

Biochemical studies have demonstrated that the N-BAR domain of ICA69 (amino acids 1-234) can deform liposomes and induce tubular membrane structures in vitro. Within 10 minutes of incubation with liposomes, ICA69 induces tubular membrane structures; by 30 minutes, membrane vesicles become the predominant species, indicating that ICA69 can drive the complete membrane fission process [mallik-2017-drosophila-nmj-abstract]. This membrane-deforming activity is essential for its role in vesicle budding at the TGN.

The lipid binding properties of PICK1, and by extension the PICK1-ICA69 heterodimer, have been more extensively characterized. PICK1 directly binds to lipids, mainly phosphoinositides, via its BAR domain. Lipid binding of the PICK1 BAR domain is positively regulated by its PDZ domain and negatively regulated by its C-terminal acidic domain. In contrast to covalent lipid modifications like palmitoylation, the interaction of the PICK1-ICA69 complex with lipids is based on noncovalent electrostatic interactions, making the association with membranes highly dynamic. This allows the complex to be recruited to specific membrane regions when negatively charged lipids are enriched and to dissociate when the membrane becomes less charged—a property that likely underlies the transient association of ICA69 with maturing secretory granules.

Studies of PICK1 variants identified in diabetic patients have provided additional mechanistic insights. Four coding variants affecting positively charged arginine residues in the PICK1 BAR domain (R158Q, R185Q, R197Q, R247H) compromised membrane binding capacity [pihlstrøm-2022-pick1-variants-diabetes-abstract]. Paradoxically, these variants showed increased capacity to cause membrane fission, suggesting that the balance between membrane binding affinity and fission activity is critical for proper insulin granule biogenesis. Since PICK1-ICA69 heterodimers share similar lipid-binding properties, these findings have implications for understanding how the complex regulates membrane dynamics during DCV formation.

## Role in ER-Golgi Trafficking and Rab2 Interaction

Beyond its role in DCV biogenesis at the TGN, ICA69 also functions earlier in the secretory pathway as an effector of the small GTPase Rab2, which regulates COPI vesicle transport between the endoplasmic reticulum (ER) and the Golgi complex [buffa-2008-rab2-effector-abstract]. In insulinoma INS-1 cells, ICA69 binds to Rab2 in a GTP-dependent manner, and Rab2 recruits ICA69 to membranes. This interaction places ICA69 at a critical juncture in the secretory pathway, where cargo proteins destined for secretory granules transit from the ER to the Golgi.

Functional studies revealed that overexpression of either Rab2 or ICA69 in insulinoma cells impaired the anterograde transport of secretory granule protein precursors, including pro-ICA512 (a transmembrane protein of insulin granules) and chromogranin A (a major lumenal cargo of DCVs) [buffa-2008-rab2-effector-abstract]. This overexpression also reduced stimulated insulin secretion. These findings suggest that ICA69, in partnership with Rab2, regulates the flow of cargo through the early secretory pathway and that the stoichiometry of these interactions is important for proper secretory function.

The involvement of ICA69 in Rab2-mediated ER-Golgi trafficking connects it to the broader machinery of DCV maturation. In *C. elegans*, the ICA69 homologue RIC-19 was identified as a RAB-2 effector in genetic screens for genes involved in DCV cargo retention during maturation [bhimsen-2000-ric19-abstract]. Eight genes have been identified as essential for immature DCV remodeling and cargo maintenance: UNC-108/RAB-2, RIC-19/ICA69, VPS-50, VPS-51, VPS-52, VPS-53, RUND-1, and HID-1. This places ICA69/RIC-19 within a conserved molecular network controlling DCV biogenesis from nematodes to mammals.

## Role in Neuroendocrine Secretion and Synaptic Function

The demonstration that the *C. elegans* ICA69 homologue RIC-19 is required for normal neurotransmitter secretion provided the first functional evidence for ICA69's role in the regulated secretory pathway [bhimsen-2000-ric19-abstract]. The ric-19 deletion mutant exhibited striking resistance to aldicarb, an inhibitor of acetylcholinesterase. Since aldicarb resistance typically indicates reduced acetylcholine release, this phenotype demonstrated that RIC-19 is necessary for efficient neurotransmitter secretion. Importantly, the phenotype was rescued by transgenic expression of RIC-19, confirming the specificity of this function.

Studies in *Drosophila melanogaster* have extended these findings and revealed additional functions at the neuromuscular junction (NMJ). An RNAi screen targeting BAR-domain proteins identified ICA69 as one of the key regulators of morphological differentiation at the larval NMJ [mallik-2017-drosophila-nmj-abstract]. In Drosophila, ICA69 colocalizes with α-Spectrin at the NMJ and regulates the synaptic localization of ionotropic glutamate receptors (iGluRs). Full-length ICA69 induces filopodia formation in cultured cells, consistent with its membrane-deforming activity. Importantly, Rab2 functions genetically upstream of ICA69 in this context, regulating NMJ organization and iGluR targeting/retention by controlling ICA69 protein levels [mallik-2017-drosophila-nmj-abstract]. ICA69 mutants display reduced α-Spectrin immunoreactivity at the larval NMJ, indicating impaired cytoskeletal organization. These findings demonstrate that the Rab2-ICA69 pathway is evolutionarily conserved and plays a crucial role in synaptic organization across species.

In mammals, ICA69's role in neuronal function has been established through studies of ICA69 knockout mice. Recent work demonstrated that ICA69 is essential for activity-dependent synaptic strengthening, specifically long-term potentiation (LTP), a cellular mechanism underlying learning and memory [yang-2023-synaptic-plasticity-abstract]. ICA69 knockout mice showed selective deficits in LTP following theta-burst stimulation, with field excitatory postsynaptic potential amplitudes substantially reduced compared to wild-type mice for at least 90 minutes post-stimulation.

Remarkably, ICA69 knockout mice exhibited normal basal synaptic transmission. Postsynaptic AMPA receptor (AMPAR) levels remained normal, and miniature excitatory postsynaptic currents showed no differences between knockout and wild-type mice [yang-2023-synaptic-plasticity-abstract]. This indicates that ICA69 is specifically required for activity-dependent processes rather than constitutive synaptic function. The authors proposed that ICA69 facilitates forward trafficking of AMPAR-containing vesicles during LTP induction, drawing parallels to its established function in promoting insulin and growth hormone secretion in endocrine tissues.

The molecular mechanism underlying ICA69's role in synaptic plasticity involves regulation of PICK1 and protein kinase C alpha (PKCα) trafficking. Studies have shown that the C-terminal domain of ICA69 (ICAC) interacts with PICK1 and regulates the trafficking of the PICK1-PKCα complex to the plasma membrane [wang-2013-ica69-pkca-trafficking-abstract]. PKCα is a key kinase involved in the phosphorylation and internalization of AMPARs during long-term depression (LTD). MBP-ICAC fusion proteins significantly inhibited LTD at cerebellar Purkinje cell synapses, demonstrating that ICA69's regulation of PICK1-PKCα trafficking is functionally important for synaptic plasticity [wang-2013-ica69-pkca-trafficking-abstract]. Thus, ICA69 appears to serve as a bidirectional regulator of synaptic plasticity, affecting both LTP (through AMPAR insertion) and LTD (through PKCα-mediated AMPAR internalization), depending on the neuronal context and signaling state.

The behavioral consequences of ICA69 loss are significant. ICA69 knockout mice showed substantial learning and memory deficits in multiple cognitive tasks. In spatial memory tasks using the Y-maze, knockout mice showed discrimination indices near chance level (0.56 versus 0.70 for controls). Associative learning measured by inhibitory avoidance tasks was similarly impaired, with knockout animals showing no increased latency to enter the shock chamber 24 hours after training [yang-2023-synaptic-plasticity-abstract]. These findings establish ICA69 as an important regulator of cognitive function.

## Connection to Type 1 Diabetes and Autoimmunity

ICA69 was originally identified through its recognition by autoantibodies in sera from relatives of patients with insulin-dependent diabetes mellitus (IDDM, now called type 1 diabetes, T1D) who subsequently progressed to overt disease [pietropaolo-1993-ica69-discovery-abstract]. The researchers screened a human islet cDNA expression library with cytoplasmic islet cell antibody-positive sera and identified ICA69 as a novel autoantigen. Subsequently, it was shown that sera from T1D patient relatives specifically react with recombinant ICA69 protein.

While ICA69 is recognized as a T1D autoantigen, it is not among the four major autoantibody markers currently used for clinical prediction of T1D progression (insulin autoantibodies, GAD65 autoantibodies, IA-2 autoantibodies, and ZnT8 autoantibodies). Nevertheless, ICA69 autoimmunity contributes to the broader autoimmune response targeting pancreatic islets. The localization of ICA69 to the insulin secretory granule membrane and its role in insulin granule biogenesis explain why it becomes a target of the autoimmune response—it is a component of the very organelles that define beta cell identity and function.

Studies in NOD (non-obese diabetic) mice, a model of spontaneous autoimmune diabetes, have provided mechanistic insights into ICA69 autoimmunity [fan-2014-multiorgan-autoimmunity-abstract]. NOD mice immunized with ICA69 polypeptides exhibited exacerbated inflammation not only in the pancreatic islets but also in the salivary glands. This multi-organ autoimmunity reflects the expression pattern of ICA69 in multiple secretory tissues. Genetically modified mice with suboptimal thymic ICA69 expression (ICA69del/wt and Aire-ΔICA69 mice) showed inadequate central tolerance to ICA69, resulting in the escape of ICA69-reactive T cells to the periphery [fan-2014-multiorgan-autoimmunity-abstract]. These mice spontaneously developed coincident autoimmune responses affecting the pancreas, salivary glands, thyroid, and stomach.

The connection between ICA69 autoimmunity and Sjögren's syndrome, a chronic autoimmune disease characterized by lymphocytic infiltration and destruction of salivary and lacrimal glands, has been particularly well-characterized [winer-2002-sjogren-abstract]. Disruption of the ICA69 locus in NOD mice prevented lacrimal gland disease and greatly reduced salivary gland disease. T-cell and B-cell autoreactivity against ICA69 was found in patients with primary Sjögren's syndrome, and autoantibodies to ICA69 were detected in Western blots of patient sera. Importantly, treatment with an ICA69-targeted peptide vaccine successfully reduced established disease in mice, suggesting therapeutic potential [winer-2002-sjogren-abstract].

## Connection to Neurodevelopmental Disorders

Emerging genetic evidence has linked ICA1 to neurodevelopmental disorders, including autism spectrum disorder (ASD) and schizophrenia. The SFARI (Simons Foundation Autism Research Initiative) Gene database classifies ICA1 as a "strong candidate" autism gene with a score of 2 [sfari-2019-ica1-summary]. Multiple lines of evidence support this association:

First, rare inherited duplications of the 7p21 chromosomal locus that includes ICA1 have been identified in ASD probands across multiple independent studies [sfari-2019-ica1-summary]. Second, a rare de novo missense variant in ICA1 was identified in an ASD proband from the Simons Simplex Collection. Third, and most significantly, a CNV analysis of 1,108 ASD cases, 2,458 schizophrenia cases, and 2,095 controls from a Japanese population demonstrated significant enrichment of exonic CNVs affecting ICA1 in the combined neurodevelopmental disease cohort [kushima-2018-cnv-asd-scz-abstract]. Specifically, 6 CNVs were found in ASD/schizophrenia cases versus 0 in controls (odds ratio 9.19, P = 1.0×10⁻⁵).

The neurobiological basis for ICA1's involvement in neurodevelopmental disorders likely relates to its role in synaptic plasticity and learning [yang-2023-synaptic-plasticity-abstract]. The finding that ICA69 knockout mice have selective deficits in LTP and impaired learning and memory provides a plausible mechanism by which ICA1 dysfunction could contribute to cognitive symptoms in ASD and schizophrenia. Additionally, ICA69's role in DCV biogenesis could affect the release of neuromodulators and neuropeptides from dense-core vesicles, which are important for proper brain development and function.

## Emerging Roles in Cardiovascular Disease

Recent research has revealed unexpected functions for ICA69 beyond its established roles in vesicle biogenesis and neuroendocrine secretion. A 2022 study identified ICA69 as a regulator of ferroptosis in sepsis-induced cardiac dysfunction [kong-2022-ferroptosis-cardiac-abstract]. In lipopolysaccharide (LPS)-stimulated models, ICA69 expression increases significantly, and ICA69 deficiency in LPS-induced mice markedly improved survival and cardiac function while reducing inflammatory cytokines and ferroptotic markers.

Mechanistically, elevated ICA69 promotes STING (stimulator of interferon genes) trafficking, leading to increased lipid peroxidation and ferroptosis-mediated cardiac injury [kong-2022-ferroptosis-cardiac-abstract]. ICA69 knockdown reversed ferroptotic markers including prostaglandin endoperoxide synthase 2 (PTGS2), malondialdehyde (MDA), 4-hydroxynonenal (4HNE), glutathione peroxidase 4 (GPX4), and superoxide dismutase (SOD) levels. Clinically, higher ICA69 levels were found in peripheral blood mononuclear cells from septic patients, and ICA69 expression correlated positively with sepsis severity as measured by APACHE II scores.

This novel function of ICA69 in regulating STING trafficking and ferroptosis extends its known role as a trafficking regulator to a new cellular context. The mechanism may relate to ICA69's established function in membrane trafficking, with STING being another cargo whose trafficking is influenced by ICA69. These findings suggest that ICA69 could be a potential therapeutic target for sepsis-induced cardiomyopathy, though the precise relationship between this inflammatory role and its canonical function in DCV biogenesis requires further investigation.

## Open Questions

Several important questions about ICA69 function remain unanswered and warrant further investigation:

1. **Mechanism of granule dissociation**: What molecular signals trigger the dissociation of ICA69 from maturing secretory granules while PICK1 remains associated? Is this related to changes in membrane lipid composition, pH, or the acquisition of specific cargo proteins during maturation?

2. **Tissue-specific functions**: While ICA69 and PICK1 form heterodimers in brain and pancreas, and ICA1L-PICK1 heterodimers predominate in testis, what determines this tissue specificity? Are there additional ICA69 binding partners that confer tissue-specific functions?

3. **Therapeutic potential**: Given that ICA69-targeted peptide vaccination reduced Sjögren's syndrome in mice, could similar approaches be developed for T1D prevention in at-risk individuals? What are the risks of manipulating immunity to a widely expressed protein?

4. **Neurodevelopmental mechanisms**: How do ICA1 mutations contribute to ASD and schizophrenia at the cellular and circuit levels? Which neuronal subtypes are most affected by ICA69 dysfunction?

5. **Structural basis of PICK1-ICA69 interaction**: What is the precise structural arrangement of the PICK1-ICA69 BAR domain heterodimer? How does this differ from PICK1 homodimers, and how does this difference affect membrane binding and vesicle biogenesis?

6. **Additional GTPase interactions**: While ICA69 binds Rab2, does it also interact with other small GTPases such as ARF1, given its arfaptin homology? What is the full repertoire of ICA69 protein interactions?

7. **Role in growth hormone secretion**: Some evidence suggests ICA69 is involved in growth hormone secretion from pituitary somatotrophs. What is the specific mechanism, and does ICA69 dysfunction contribute to growth abnormalities?

## References

1. **[pietropaolo-1993-ica69-discovery-abstract]** Pietropaolo M, Castaño L, Babu S, Buelow R, Kuo YL, Martin S, Martin A, Powers AC, Prochazka M, Naggert J, et al. Islet cell autoantigen 69 kD (ICA69). Molecular cloning and characterization of a novel diabetes-associated autoantigen. J Clin Invest. 1993 Jul;92(1):359-71. PMID: 8326004. DOI: 10.1172/JCI116574

2. **[spitzenberger-2003-golgi-abstract]** Spitzenberger F, Pietropaolo S, Verkade P, Habermann B, Lacas-Gervais S, Mziaut H, Pietropaolo M, Solimena M. Islet cell autoantigen of 69 kDa is an arfaptin-related protein associated with the Golgi complex of insulinoma INS-1 cells. J Biol Chem. 2003 Jul 11;278(28):26166-73. PMID: 12682071. DOI: 10.1074/jbc.M213222200

3. **[buffa-2008-rab2-effector-abstract]** Buffa L, Fuchs E, Pietropaolo M, Barr F, Solimena M. ICA69 is a novel Rab2 effector regulating ER-Golgi trafficking in insulinoma cells. Eur J Cell Biol. 2008 Apr;87(4):197-209. PMID: 18187231. DOI: 10.1016/j.ejcb.2007.11.003

4. **[cao-2013-pick1-ica69-trafficking-abstract]** Cao M, Mao Z, Kam C, Xiao N, Cao X, Shen C, Cheng KKY, Xu A, Lee KM, Jiang L, Xia J. PICK1 and ICA69 control insulin granule trafficking and their deficiencies lead to impaired glucose tolerance. PLoS Biol. 2013 Apr 23;11(4):e1001541. PMID: 23630453. PMCID: PMC3635858. DOI: 10.1371/journal.pbio.1001541

5. **[he-2015-ica1l-pick1-acrosome-abstract]** He J, Xia M, Tsang WH, Chow KL, Xia J. ICA1L forms BAR-domain complexes with PICK1 and is crucial for acrosome formation in spermiogenesis. J Cell Sci. 2015 Oct 15;128(20):3822-36. PMID: 26306493. DOI: 10.1242/jcs.173534

6. **[pihlstrøm-2022-pick1-variants-diabetes-abstract]** Pihlstrøm HK, Bhuin R, Hansen SH, Bhowmik D, et al. Coding variants identified in patients with diabetes alter PICK1 BAR domain function in insulin granule biogenesis. J Clin Invest. 2022 Feb 15;132(4):e144904. PMID: 35077398. PMCID: PMC8884907. DOI: 10.1172/JCI144904

7. **[bhimsen-2000-ric19-abstract]** The Diabetes Autoantigen ICA69 and Its Caenorhabditis elegans Homologue, ric-19, Are Conserved Regulators of Neuroendocrine Secretion. Mol Biol Cell. 2000 Oct;11(10):3277-90. PMCID: PMC14991. DOI: 10.1091/mbc.11.10.3277

8. **[winer-2002-sjogren-abstract]** Winer S, Astsaturov I, Cheung R, Tsui H, Song A, Gaedigk R, Winer D, Sampson A, McKerlie C, Bookman A, Dosch HM. Primary Sjögren's syndrome and deficiency of ICA69. Lancet. 2002 Oct 5;360(9340):1063-9. PMID: 12383988. DOI: 10.1016/S0140-6736(02)11144-5

9. **[fan-2014-multiorgan-autoimmunity-abstract]** Fan Y, et al. Compromised central tolerance of ICA69 induces multiple organ autoimmunity. J Autoimmun. 2014 Sep;53:10-25. PMID: 25088457. DOI: 10.1016/j.jaut.2014.07.001

10. **[yang-2023-synaptic-plasticity-abstract]** Yang C, Bhinge A, et al. ICA69 regulates activity-dependent synaptic strengthening and learning and memory. Front Mol Neurosci. 2023;16:1171432. DOI: 10.3389/fnmol.2023.1171432

11. **[kushima-2018-cnv-asd-scz-abstract]** Kushima I, et al. Comparative Analyses of Copy-Number Variation in Autism Spectrum Disorder and Schizophrenia Reveal Etiological Overlap and Biological Insights. Cell Rep. 2018;24(11):2838-2856.

12. **[sfari-2019-ica1-summary]** SFARI Gene Database - ICA1 Entry. https://gene.sfari.org/database/human-gene/ICA1. Score 2 (Strong Candidate). Last updated October 1, 2019.

13. **[mallik-2017-drosophila-nmj-abstract]** Mallik B, Dwivedi MK, Mushtaq Z, Kumari M, Verma PK, Kumar V. Regulation of neuromuscular junction organization by Rab2 and its effector ICA69 in Drosophila. Development. 2017 Jun 1;144(11):2032-2044. PMID: 28455372. DOI: 10.1242/dev.145920

14. **[wang-2013-ica69-pkca-trafficking-abstract]** Wang Z, Wang YN, Sun CL, Yang D, Su LD, Xie YJ, Zhou L, Wang Y, Shen Y. C-terminal domain of ICA69 interacts with PICK1 and acts on trafficking of PICK1-PKCα complex and cerebellar plasticity. PLoS One. 2013 Dec 16;8(12):e83862. PMID: 24358315. DOI: 10.1371/journal.pone.0083862

15. **[kong-2022-ferroptosis-cardiac-abstract]** Kong C, Ni X, Wang Y, Zhang A, Zhang Y, Lin F, Li S, Lv Y, Zhu J, Yao X, Dai Q, Mo Y, Wang J. ICA69 aggravates ferroptosis causing septic cardiac dysfunction via STING trafficking. Cell Death Discov. 2022 Apr 9;8(1):187. PMID: 35397620. DOI: 10.1038/s41420-022-00957-y


## Citations

1. bhimsen-2000-ric19-abstract.md
2. buffa-2008-rab2-effector-abstract.md
3. cao-2013-pick1-ica69-trafficking-abstract.md
4. fan-2014-multiorgan-autoimmunity-abstract.md
5. he-2015-ica1l-pick1-acrosome-abstract.md
6. kong-2022-ferroptosis-cardiac-abstract.md
7. kushima-2018-cnv-asd-scz-abstract.md
8. mallik-2017-drosophila-nmj-abstract.md
9. pietropaolo-1993-ica69-discovery-abstract.md
10. pihlstrøm-2022-pick1-variants-diabetes-abstract.md
11. sfari-2019-ica1-summary.md
12. spitzenberger-2003-golgi-abstract.md
13. wang-2013-ica69-pkca-trafficking-abstract.md
14. winer-2002-sjogren-abstract.md
15. yang-2023-synaptic-plasticity-abstract.md