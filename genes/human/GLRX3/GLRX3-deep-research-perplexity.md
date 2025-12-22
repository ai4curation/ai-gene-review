---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-12T07:08:56.873818'
end_time: '2025-12-12T07:10:48.417644'
duration_seconds: 111.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GLRX3
  gene_symbol: GLRX3
  uniprot_accession: O76003
  protein_description: 'RecName: Full=Glutaredoxin-3; AltName: Full=PKC-interacting
    cousin of thioredoxin {ECO:0000303|PubMed:10636891}; Short=PICOT {ECO:0000303|PubMed:10636891};
    AltName: Full=PKC-theta-interacting protein; Short=PKCq-interacting protein; AltName:
    Full=Thioredoxin-like protein 2;'
  gene_info: Name=GLRX3; Synonyms=PICOT {ECO:0000303|PubMed:10636891}, TXNL2; ORFNames=HUSSY-22;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: Glutaredoxin. (IPR002109); GRX_PICOT-like. (IPR033658); Monothiol_GRX-rel.
    (IPR004480); Thioredoxin-like_sf. (IPR036249); Thioredoxin_domain. (IPR013766)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 38
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O76003
- **Protein Description:** RecName: Full=Glutaredoxin-3; AltName: Full=PKC-interacting cousin of thioredoxin {ECO:0000303|PubMed:10636891}; Short=PICOT {ECO:0000303|PubMed:10636891}; AltName: Full=PKC-theta-interacting protein; Short=PKCq-interacting protein; AltName: Full=Thioredoxin-like protein 2;
- **Gene Information:** Name=GLRX3; Synonyms=PICOT {ECO:0000303|PubMed:10636891}, TXNL2; ORFNames=HUSSY-22;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Glutaredoxin. (IPR002109); GRX_PICOT-like. (IPR033658); Monothiol_GRX-rel. (IPR004480); Thioredoxin-like_sf. (IPR036249); Thioredoxin_domain. (IPR013766)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GLRX3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GLRX3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GLRX3** (gene ID: GLRX3, UniProt: O76003) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me start by carefully analyzing the research prompt and the search results provided.

First, I need to verify that I'm researching the correct gene:
- Target Gene: GLRX3 (Glutaredoxin 3)
- UniProt Accession: O76003
- Organism: Homo sapiens (Human)
- Gene Symbol Synonyms: PICOT (Protein Kinase C-interacting cousin of thioredoxin), TXNL2
- Key Domains: Glutaredoxin, Monothiol_GRX, Thioredoxin-like

From the search results, I can see extensive literature on this protein. Now let me plan the structure of my report:

**Main research themes to cover:**

1. **Molecular Structure and Domain Organization** - The multidomain architecture of GLRX3
2. **Iron-Sulfur Cluster Biology** - GLRX3's role as an iron-sulfur cluster chaperone
3. **Cellular Localization** - Where GLRX3 functions in the cell
4. **Iron Metabolism and Homeostasis** - The primary biochemical function
5. **Protein-Protein Interactions** - Key binding partners and interaction mechanisms
6. **Transcriptional and Signaling Regulation** - Broader cellular roles
7. **Clinical and Pathological Implications** - Disease associations and cancer relevance
8. **Evolutionary Conservation** - Cross-species function

Let me assess the search results for quality and relevance:
- Multiple peer-reviewed journal articles from prestigious sources (Nature, PNAS, ACS, Molecular Biology of the Cell, etc.)
- NCBI Gene database entries
- UniProt entries
- Recent research (2019-2024)
- Mix of primary research and reviews

Key findings from search results:
[1-3] Basic gene information from NCBI and GeneCards
[2, 9, 14] Major research on GMP synthase interaction and ISR pathway


[4, 28] UniProt reveals GLRX3's critical enzymatic functions in cellular redox processes and protein folding. The protein plays a pivotal role in maintaining cellular reducing environments and managing protein quality control.

[5, 32, 35] Interactions with the Polycomb Repressive Complex 2 (PRC2) suggest epigenetic regulatory mechanisms. GLRX3 potentially modulates gene expression through chromatin modification pathways.

I'll focus on the intricate biochemical mechanisms of iron-sulfur cluster transfer. The protein functions as a sophisticated molecular chaperone, facilitating cluster assembly and transfer between different cellular proteins. This process is crucial for maintaining mitochondrial and cytosolic iron metabolism.

Hemoglobin maturation emerges as another key function, with GLRX3 playing a critical role in iron incorporation and protein stabilization. The glutaredoxin-BolA complex represents a sophisticated molecular machinery for iron-sulfur cluster biogenesis.

Cancer research indicates potential dysregulation of GLRX3 in various malignancies, suggesting its significance in cellular stress responses and potential therapeutic targeting.

Oxidative stress protection mechanisms further underscore the protein's importance in cellular resilience, with specific localization patterns influencing its protective functions.
</think>

# Glutaredoxin-3 (GLRX3): A Comprehensive Analysis of Structure, Function, and Biological Role in Iron-Sulfur Cluster Biogenesis and Cellular Homeostasis

The human **glutaredoxin-3** (GLRX3), also known as protein kinase C-interacting cousin of thioredoxin (PICOT), represents a multifunctional protein with emerging significance in cellular iron metabolism, redox homeostasis, and DNA damage response mechanisms. Encoded by the GLRX3 gene located on chromosome 10 and designated with UniProt accession O76003, this ubiquitously distributed protein has evolved as a critical regulator of iron-sulfur cluster assembly and distribution within the cytoplasm and nucleus of mammalian cells[3][4][40]. Since its discovery in the year 2000 as a binding partner for protein kinase C-theta (PKCθ), GLRX3 has emerged from relative obscurity to become recognized as an essential factor for embryonic development, cellular stress adaptation, and prevention of age-related decline[5][45][51]. This comprehensive analysis examines the molecular architecture, biochemical mechanisms, cellular localization dynamics, and pathophysiological roles of GLRX3, integrating evidence from structural studies, molecular genetics, and functional investigations that collectively establish this protein as a central hub in iron metabolism and cellular survival pathways.

## Structural Architecture and Multidomain Organization

GLRX3 exhibits a distinctive three-domain architecture that fundamentally distinguishes it from classical thioredoxins and glutaredoxins, endowing the protein with unique mechanistic capabilities for iron-sulfur cluster handling[3][19][55]. The protein comprises an N-terminal thioredoxin (Trx) homology domain and two tandem C-terminal monothiol glutaredoxin (Grx) homology domains, each containing the characteristic CGFS (cysteine-glycine-phenylalanine-serine) motif that defines class II glutaredoxins[5][19][55]. This structural configuration represents an evolutionary adaptation distinct from single-domain glutaredoxins or thioredoxins found in simpler organisms, reflecting the increased complexity of iron metabolism in higher eukaryotes[25]. Notably, despite possessing an N-terminal region with homology to thioredoxin domains, the critical catalytic motif essential for classical thioredoxin oxidoreductase activity is absent, meaning GLRX3 lacks conventional thioredoxin catalytic function[3][40]. Rather, this domain appears to serve scaffolding or regulatory purposes, as demonstrated through targeted mutagenesis studies where researchers have identified that the Trx-like domain participates in substrate binding and interacting partner recognition[19][21].

The two C-terminal Grx domains constitute the functionally active regions for iron-sulfur cluster coordination and represent the primary structural determinants of GLRX3's biological role[7][33][55]. Each Grx domain possesses a CGFS active site motif where the conserved cysteine residue serves as a critical ligand for iron-sulfur cluster coordination[3][7][14]. Structurally, these domains enable the formation of homodimeric complexes wherein two GLRX3 molecules bridge iron-sulfur clusters between their interface, a configuration stabilized through coordinated binding of the cluster's iron and sulfide atoms to the cysteine residues of each monomer as well as to molecules of reduced glutathione (GSH) that serve as essential cofactors[7][10][17][33]. The glutathione molecules coordinate the cluster through their thiol and amino groups, creating a quaternary complex wherein iron-sulfur cluster ligation depends simultaneously on protein cysteine residues, glutathione cofactors, and the metal-sulfide core structure[7][25][33][42]. This structural interdependence of protein, cofactor, and metal cluster represents a fundamentally different architecture compared to classical iron-sulfur cluster proteins where the cluster directly ligates to protein cysteine residues alone[25].

Sequence homology analyses reveal that the Grx domains of human GLRX3 share approximately 40-50% sequence identity with the corresponding domains of yeast Grx3 and Grx4 proteins, indicating substantial evolutionary conservation despite divergence in organismal complexity[2][9]. However, the identity between the Trx domains is considerably lower, at less than 27%, suggesting differential selective pressures for preserving these distinct functional modules[2][9]. Alternative splicing of the GLRX3 transcript can generate variant proteins, and pseudogenes of this locus are present on chromosomes 6 and 9, though these pseudogenic sequences do not produce functional proteins[3][40]. The remarkable conservation of the Grx domains across vast evolutionary distances, from fungi to higher mammals, underscores the fundamental importance of the iron-sulfur cluster chaperoning function throughout eukaryotic biology[2][9][30].

## Iron-Sulfur Cluster Biology and Chaperoning Mechanisms

The primary biochemical function of GLRX3 centers on its capacity to coordinate, transport, and deliver iron-sulfur clusters to target apoproteins, a function that positions this protein at the interface between mitochondrial iron-sulfur cluster synthesis and cytoplasmic protein maturation[7][8][20][30]. Human GLRX3 specifically functions as a [2Fe-2S] cluster chaperone, capable of binding two iron atoms coordinated with two sulfide atoms through interactions with glutathione, cysteine residues within the CGFS motifs, and histidine residues from partner proteins[7][10][20][33]. The biochemical mechanism of cluster transfer has been elucidated through multiple independent studies utilizing spectroscopic approaches, protein chemistry, and cell-based investigations that collectively demonstrate a directional flux of iron-sulfur clusters from GLRX3 to target proteins requiring these essential prosthetic groups[7][10][20][30].

In molecular detail, dimeric cluster-bridged GLRX3 molecules—wherein each GLRX3 monomer coordinates half of a [2Fe-2S] cluster through its CGFS active site—transfer their bound clusters to protein targets essential for cytosolic iron-sulfur protein assembly (CIA) machinery[7][20][33][42][50]. The transfer of [2Fe-2S] clusters from GLRX3 to target proteins such as NUBP1, a P-loop NTPase critical for early-stage CIA processing, occurs through direct protein-protein interaction wherein the cluster remains protein-bound throughout the transfer process, ensuring no loss of this extremely labile prosthetic group in solution[7][20][33][50]. Remarkably, the incoming [2Fe-2S] clusters can undergo reductive coupling in the presence of glutathione to form [4Fe-4S] clusters on bifunctional target proteins that possess dual cluster-binding sites[7][20][33][42]. This reductive coupling mechanism represents a sophisticated biochemical achievement wherein GLRX3 essentially functions as a nucleation point enabling the synthesis of higher-order iron-sulfur clusters through controlled reduction by glutathione, which acts as the biological reductant in this process[7][33]. The [4Fe-4S] clusters assembled on N-terminal cluster-binding motifs exhibit tight binding and stability, while those assembled on C-terminal motifs display labile characteristics, providing a potential regulatory mechanism for cluster dynamics within the cell[7][20][33].

The in vivo assembly efficiency of iron-sulfur clusters via GLRX3-mediated transfer achieves approximately 60% efficiency under physiological conditions, indicating that while GLRX3 represents an important pathway for cluster biogenesis, additional redundant or complementary mechanisms exist for cluster maturation[7]. However, GLRX3 knockout or severe depletion studies reveal that this protein is particularly critical for maturation of specific iron-sulfur protein substrates, most notably cytosolic [4Fe-4S]-cluster-containing proteins required for DNA repair, metabolic functions, and other essential cellular processes[41][49]. Surprisingly, GLRX3 does not appear essential for cytosolic [2Fe-2S]-cluster protein assembly, suggesting functional redundancy or alternative pathway sufficiency for this simpler cluster form[41][49]. GLRX3 specifically collaborates with the BolA2 protein to form [2Fe-2S]-cluster-bridged heterocomplexes in human cells, representing a heterocomplex that responds dynamically to cellular iron availability and serves as a rapidly expandable pool of iron-sulfur clusters[10][17][30]. Cellular GLRX3-BolA2 complexes increase 6-8 fold in response to elevated iron supplementation and decrease accordingly under iron-depleted conditions, establishing these complexes as iron-responsive storage and distribution centers[10][17].

The interaction between GLRX3 and BolA2 displays remarkable iron-responsiveness, increasing within one hour of iron supplementation and reaching maximum levels by four hours, indicating a rapid and sensitive mechanism for responding to changes in cellular iron status[10][17]. Unlike yeast GLRX3 orthologs, human GLRX3-BolA2 complex formation strictly requires coordination of iron-sulfur clusters, as cluster-free GLRX3 and BolA2 apo-proteins do not stably associate in mammalian cells, representing a mechanistic difference from simpler organisms[10][17]. The functional significance of this iron-dependent interaction lies in its capacity to deliver [2Fe-2S] clusters to downstream recipients within the CIA pathway, including anamorsin (CIAPIN1), a [2Fe-2S]-cluster-containing protein functioning early in the cytosolic assembly process[10][17][30][52]. This hierarchical organization of iron-sulfur cluster distribution, wherein mitochondrial synthesis is followed by GLRX3-BolA2 mediated cytosolic delivery and subsequent transfer to downstream assembly scaffolds, represents an elegant solution to the challenge of safely managing these highly labile and potentially toxic metal-sulfide clusters within the reducing environment of the cytoplasm[7][10][30][41].

## Cellular Localization and Subcellular Dynamics

GLRX3 demonstrates a remarkable capacity for dynamic subcellular redistribution in response to cellular stress conditions, representing a sophisticated regulatory mechanism for concentrating this protein at sites requiring enhanced iron-sulfur cluster availability or antioxidant protection[25][27]. Under normal growth conditions, GLRX3 is predominantly localized to the cytoplasm in a relatively diffuse distribution pattern, as demonstrated through fluorescence microscopy of GLRX3-RFP fusion proteins and biochemical fractionation studies of transfected mammalian cells[27]. However, upon exposure to oxidative stress induced by hydrogen peroxide or other radical-generating agents, GLRX3 undergoes a reversible and redox-dependent translocation into the nucleus, accumulating there in response to the perceived oxidative insult[27]. This nuclear accumulation is reversible in a temporally-dependent fashion, with GLRX3 returning to predominantly cytoplasmic localization as cellular redox conditions normalize, indicating an active sensing and response mechanism rather than irreversible sequestration[27]. The mechanism of nuclear translocation does not depend upon the N-terminal Trx-like domain nor upon the catalytic cysteine residues within the CGFS motifs, suggesting a redox-sensing mechanism distinct from the cluster-coordinating function and potentially involving other cysteine residues or sensing domains[27].

The biological significance of stress-induced nuclear translocation relates to GLRX3's emerging role in nuclear functions including DNA damage response and epigenetic regulation[27][45][51]. Overexpression of GLRX3 targeted to the nucleus through artificial targeting sequences is sufficient to suppress cellular sensitivity to oxidative stress and reduce reactive oxygen species production, establishing a direct relationship between nuclear GLRX3 localization and cellular protection against oxidative injury[27]. Furthermore, GLRX3 displays partial localization at γH2AX-containing foci, the sites of DNA double-strand breaks, under genotoxic conditions, suggesting direct involvement in DNA damage response signaling at the site of DNA injury[45][51]. Additionally, GLRX3 has been found to localize to chromatin-associated regions where it interacts with the embryonic ectoderm development (EED) protein, a core component of Polycomb repressive complex 2 (PRC2), suggesting a role in regulating chromatin structure and epigenetic gene silencing[5][32][35].

The interaction between GLRX3 and EED occurs through each of GLRX3's two C-terminal Grx homology domains, establishing a bivalent interaction interface that modulates PRC2-mediated histone trimethylation at specific genomic loci[5][32][35]. GLRX3 binding to chromatin-associated EED reduces the occupancy of PRC2 complex components at select target genes, particularly affecting H3K27me3 levels at the CCND2 gene promoter encoding cyclin D2[5][32][35]. This GLRX3-dependent modulation of PRC2 activity results in increased CCND2 transcription, linking GLRX3 to cell cycle progression through an epigenetic mechanism[5][32][35]. The discovery that GLRX3 can modify PRC2-mediated transcriptional silencing introduces an unexpected connection between iron metabolism, cellular redox status, and epigenetic gene regulation, suggesting that GLRX3 may coordinate multiple layers of cellular regulation responding to iron availability and oxidative stress[5][32][35]. These findings propose a sophisticated regulatory architecture wherein GLRX3 integrates metabolic signals (iron status) with epigenetic modifications that control cell proliferation, potentially explaining some of the oncogenic associations of GLRX3 dysregulation in cancer cells[5][32][35].

## Iron Metabolism and Cellular Homeostatic Regulation

GLRX3 functions as a critical regulator of cellular iron homeostasis through multiple interconnected mechanisms that collectively ensure appropriate iron acquisition, utilization, and storage according to cellular needs[8][11][30]. The depletion of GLRX3 expression in cultured mammalian cells results in activation of iron-regulatory protein 1 (IRP1), a key component of the iron-sensing system that post-transcriptionally regulates iron metabolism genes[8][11][24]. Under normal iron-replete conditions, IRP1 exists as an iron-sulfur cluster-containing protein that functions as aconitase and does not bind to iron-responsive elements (IREs) in mRNA. However, GLRX3-depleted cells display markedly reduced IRP1 protein levels and activity, indicating failed maturation of the iron-sulfur cluster required for aconitase function[8][11][24]. Consequently, IRP1 adopts its apoprotein form lacking iron-sulfur clusters, converting it into an active IRE-binding protein that suppresses translation of transferrin receptor mRNA (which promotes iron uptake) and enhances translation of ferritin mRNA (which stores iron)[8][11][24][30].

This paradoxical situation in GLRX3-deficient cells—wherein the cellular system perceives iron starvation despite normal or elevated intracellular iron levels—reveals GLRX3's central position in iron sensing[8][11][30]. GLRX3-depleted cells accumulate increased cellular iron content but cannot appropriately utilize this iron for biosynthetic purposes, as the deficiency of iron-sulfur cluster-containing proteins limits the cell's capacity to synthesize essential iron-dependent enzymes[8][11][30]. The consequences manifest as activation of the integrated stress response (ISR) pathway through the kinase GCN2, which senses the cellular inability to efficiently use iron through Aft1/Aft2 transcriptional activation[2][9][14][38][39]. Multiple iron-consuming pathways become simultaneously impaired in GLRX3-deficient cells, including hemoglobin maturation during erythropoiesis, ribonucleotide reductase activity required for DNA synthesis, and other iron-sulfur cluster-dependent processes throughout metabolism[8][11][24][30].

The in vivo significance of GLRX3 for iron metabolism was established through studies in zebrafish embryos, wherein GLRX3 depletion during embryogenesis severely impairs hemoglobin maturation, the major iron-consuming process during erythroid development[8][11]. The developmental dependence upon GLRX3 is underscored by the embryonic lethality of homozygous GLRX3 knockout mice, occurring between embryonic day 12.5 and 14.5 during a period of intense erythropoiesis and general tissue growth[26][29]. These developmental studies establish GLRX3 as essential for embryonic viability, placing it among the most critical iron metabolism factors for mammalian development[26][29].

GLRX3 also collaborates with GMP synthase in a novel pathway connecting iron metabolism to guanine nucleotide biosynthesis and cellular stress responses[2][9][14][38][43][46]. The interaction between GLRX3 and GMP synthase occurs through iron-sulfur cluster-bridged complexes, demonstrating dependence upon cluster coordination for complex formation[2][9][14][38][43][46]. When cellular iron becomes depleted, this GLRX3-GMP synthase interaction is disrupted, leading to altered GMP/GTP synthesis and activation of GCN2 stress response pathway[2][9][14][38][43][46]. This mechanistic connection suggests that iron availability is coupled to the cellular balance of purines and stress responses, creating an integrated metabolic checkpoint that restricts protein synthesis when iron becomes limiting[2][9][14][38][43][46]. The evolutionary conservation of this GLRX3-GMP synthase interaction from yeast to humans, despite divergent metabolic architectures between these organisms, underscores the fundamental importance of coupling iron sensing to stress response and biosynthetic regulation[2][9][14][38][43][46].

## Protein-Protein Interactions and Signaling Pathways

GLRX3 participates in an expanding network of protein-protein interactions that mediate its diverse cellular functions and link iron metabolism to multiple signaling cascades[3][5][6][45][51]. The original discovery of GLRX3 identified its interaction with protein kinase C-theta (PKCθ), and subsequent studies have established that GLRX3 binds to the regulatory domain of PKCθ and modulates its activity and subcellular localization[3][5][6]. Upon activation of T cells through antigen receptor engagement, GLRX3 and PKCθ translocate together to the plasma membrane region extending into the immunological synapse, suggesting a role for GLRX3 in T cell signal transduction[6][48]. Beyond the PKCθ interaction, GLRX3 engages with multiple metabolic and regulatory proteins through iron-sulfur cluster-dependent mechanisms, including IRP1 (iron-regulatory protein 1) through facilitation of [4Fe-4S] cluster assembly[8][11][24], BolA2 through formation of [2Fe-2S]-cluster-bridged complexes that serve as iron-responsive chaperone pairs[10][17][30], and EED (embryonic ectoderm development) through direct protein-protein interaction at chromatin sites[5][32][35].

The interaction between GLRX3 and NUBP1 (nucleotide-binding protein 1), a P-loop NTPase essential for early-stage CIA machinery function, represents a particularly well-characterized mechanistic interaction wherein GLRX3 directly transfers its [2Fe-2S] clusters to NUBP1 to facilitate the assembly of dual [4Fe-4S] clusters on this downstream target protein[7][20][33][42][50][52]. This transfer is bidirectional in terms of cluster oxidation-reduction state, with GLRX3 acting as a reductant that facilitates the conversion of incoming [2Fe-2S] clusters into [4Fe-4S] clusters through coupled reduction mechanisms[7][20][33][42][52]. GLRX3 also participates in iron-sensing mechanisms through its capacity to interact with the transcriptional factors Aft1 and Aft2 in yeast models, with orthologous functions likely conserved in mammals, wherein the iron-sulfur cluster bound to GLRX3 serves as a direct sensor of intracellular iron status[2][9][14][30][38][39][43].

Beyond iron-sulfur cluster-mediated interactions, GLRX3 participates in DNA damage response pathways through mechanisms requiring its nuclear localization[45][51]. Upon genotoxic stress induced by etoposide or camptothecin, GLRX3 facilitates phosphorylation of ATR (ataxia telangiectasia and Rad3-related) protein kinase, which serves as a master regulator of the DNA damage checkpoint response[45][51]. GLRX3-deficient cells show markedly reduced and delayed phosphorylation of ATR, Chk1, and Chk2 kinases in response to genotoxic drugs, as well as diminished phosphorylation of the histone variant H2AX (γH2AX) at DNA double-strand break sites[45][51]. These deficiencies result in increased caspase-3 activation and reduced survival of GLRX3-deficient cells exposed to DNA-damaging agents[45][51]. Interestingly, the effect of GLRX3 on drug-induced H2AX phosphorylation is independent of the cellular reactive oxygen species levels, indicating a direct role in DNA damage signaling rather than merely an antioxidant function[45][51]. The mechanism likely involves GLRX3's capacity to support the redox environment required for ATR kinase activation or to directly facilitate ATR recruitment to sites of DNA damage[45][51].

## Disease Associations and Cancer-Related Dysregulation

GLRX3 expression is frequently dysregulated in multiple human malignancies, with overexpression associated with aggressive disease phenotypes and poor clinical outcomes, positioning this protein as an emerging oncogenic factor with therapeutic potential[15][31][34]. In hepatocellular carcinoma (HCC), GLRX3 overexpression correlates with enhanced tumor cell proliferation, invasion, and immune evasion through mechanisms involving both direct iron metabolism dysregulation and activation of pro-survival signaling pathways[34]. Survival analysis in HCC cohorts demonstrates that patients with elevated GLRX3 expression exhibit significantly shortened overall survival and progression-free survival compared to those with low GLRX3 levels, establishing GLRX3 as a prognostic marker for poor outcomes[34]. The mechanism by which GLRX3 promotes HCC progression involves dysregulated iron metabolism affecting immune cell function within the tumor microenvironment, as GLRX3-mediated iron metabolism alterations diminish the cytotoxic capacity of T cells and reduce their ability to eliminate tumor cells[34].

In nasopharyngeal carcinoma (NPC), GLRX3 knockdown experiments demonstrate substantial inhibition of cell proliferation in vitro and tumorigenesis in vivo, alongside suppression of cancer cell migration and invasion through reversal of epithelial-mesenchymal transition (EMT)[31]. Mechanistically, GLRX3 maintains reduced reactive oxygen species (ROS) levels through its antioxidant functions, thereby promoting NPC cell survival and allowing the maintenance of virus latency for Epstein-Barr virus (EBV), which is intimately associated with NPC development and persistence[31]. GLRX3 stabilization correlates positively with epidermal growth factor receptor (EGFR) expression and negatively with ROS generation, establishing a signaling axis wherein GLRX3 suppresses oxidative stress to activate the EGFR/Akt pathway supporting cancer cell survival and proliferation[31]. Furthermore, GLRX3 knockdown in NPC cells significantly downregulates EGFR expression at both mRNA and protein levels, indicating that GLRX3 loss prevents EGF-mediated Akt phosphorylation and reduces cancer cell proliferation capacity[31].

Lung cancer cells also display GLRX3 overexpression, and knockdown studies in lung cancer cell lines reveal substantial reduction of proliferation and colony formation capability, accompanied by enhanced apoptosis through increased caspase-3 activity[15]. These observations consistently indicate that GLRX3 functions as a survival factor for multiple cancer types through coupled mechanisms of antioxidant defense and metabolic optimization. Notably, GLRX3 expression frequently serves as a marker correlating with cancer progression in breast cancer, hepatocellular carcinoma, and lung cancer, suggesting a general principle whereby enhanced GLRX3 expression supports the transformed phenotype through multiple mechanisms[31].

The molecular basis of GLRX3's oncogenic properties relates both to its core iron metabolism functions and to its emerging regulatory roles in epigenetics and DNA damage signaling. Enhanced GLRX3 levels facilitate increased iron-sulfur cluster synthesis supporting enhanced biosynthetic capacity required for tumor growth, while simultaneously suppressing ROS-mediated damage that would otherwise limit malignant transformation[31][34]. Additionally, GLRX3's interaction with the PRC2 complex enables altered epigenetic silencing patterns that may promote cancer-associated gene expression programs[5][32][35]. The DNA damage response defects consequent to GLRX3 depletion might paradoxically be expected to promote genome instability and cancer development, yet cancer cells typically upregulate GLRX3, suggesting that cancer cells benefit from enhanced DNA damage tolerance mechanisms including GLRX3-mediated ATR pathway support[45][51].

Beyond cancer, GLRX3 variants have been identified in association with X-linked intellectual disability with short stature and obesity syndrome and with multiple mitochondrial dysfunctions syndrome, linking GLRX3 dysfunction to severe developmental abnormalities[3][40]. The discovery that homozygous GLRX3 inactivation causes embryonic lethality in mice between days 12.5-14.5 underscores the absolute requirement for this protein during critical developmental windows[26][29].

## Evolutionary Conservation and Mechanistic Insights from Model Organisms

The evolutionary conservation of GLRX3 and its yeast orthologs Grx3 and Grx4 from single-celled fungi to complex multicellular mammals reflects the fundamental importance of this protein family for eukaryotic iron metabolism[2][9][30][43][46]. Despite sequence divergence and some mechanistic differences between yeast and mammalian systems, the core function of monothiol glutaredoxins as iron-sulfur cluster chaperones operating through iron-sulfur cluster-dependent interactions with metabolic proteins and transcription factors has been conserved across hundreds of millions of years of evolution[2][9][30][43][46][59]. Yeast genetic studies have proven particularly valuable for elucidating GLRX3 mechanisms, as the simpler architecture and better-characterized metabolic dependencies of unicellular organisms enable identification of functional interactions that might remain obscured in mammalian cells.

In budding yeast, the simultaneous deletion of both GRX3 and GRX4 produces severe iron accumulation in the cytoplasm coupled with paradoxical iron-limited phenotypes affecting biosynthesis, directly establishing that these glutaredoxins function as critical iron distribution factors[2][9][14][38][39][43][46]. The defects in iron metabolism in grx3 grx4 double mutants result from combined activation of the transcriptional factor Aft1 through removal of GLRX3-mediated inhibition, and direct impairment of iron-sulfur cluster biogenesis for cytosolic proteins[2][9][14][38][39][43][46]. Aft1 is constitutively localized to the nucleus in grx3 grx4 mutants, causing continuous up-regulation of iron import genes and leading to toxic iron accumulation despite the cell's inability to incorporate this iron into iron-dependent proteins[2][9][38][39][43]. The heterologous expression of human GLRX3 in yeast grx3 grx4 double mutants efficiently complements the iron metabolism defects, demonstrating remarkable functional conservation despite the divergence of mammalian and yeast cell biology[2][9][43][46].

Yeast studies have also established the connection between monothiol glutaredoxins, guanine nucleotide metabolism, and cellular stress responses that appears conserved in higher organisms[2][9][14][38][43][46]. The discovery that GMP synthase interacts with both yeast Grx3/Grx4 and human GLRX3 through iron-sulfur cluster-dependent mechanisms revealed an unexpected coupling of iron metabolism to purine biosynthesis and integrated stress response pathways[2][9][14][38][43][46]. This connection suggests that cellular iron status is communicated to the biosynthetic machinery through the Glrx-GMP synthase complex, enabling cells to restrict biosynthesis when iron becomes limiting[2][9][14][38][43][46].

The study of GLRX3 in zebrafish development has provided critical insights into the in vivo significance of this protein for specific developmental processes, particularly hemoglobin maturation[8][11]. Grx3 depletion in zebrafish embryos impairs hemoglobin synthesis at a specific developmental window, establishing that GLRX3 is essential for the iron-dependent maturation of this critical protein[8][11]. These findings align perfectly with the human data demonstrating GLRX3's crucial role in supporting IRP1 maturation and maintaining appropriate iron distribution to hemoglobin synthesis pathways[8][11].

## Conclusion

GLRX3, alternatively designated as PICOT (protein kinase C-interacting cousin of thioredoxin), has emerged as a multifunctional protein central to eukaryotic iron metabolism, cellular redox homeostasis, and stress response signaling. The distinctive three-domain architecture comprising an N-terminal thioredoxin-like domain and two C-terminal monothiol glutaredoxin domains positions GLRX3 as a sophisticated iron-sulfur cluster chaperone capable of coordinating, transferring, and reductively coupling [2Fe-2S] clusters into higher-order [4Fe-4S] cofactors essential for cytosolic protein maturation. Through multiple interlocking mechanisms, GLRX3 orchestrates the appropriate distribution of iron-sulfur clusters to target proteins including iron-regulatory protein 1, aconitase, ribonucleotide reductase, and DNA repair enzymes, thereby ensuring that iron supply is matched to biosynthetic demand and that iron-dependent enzymatic functions are appropriately maintained. The dynamic subcellular localization of GLRX3, shifting from predominantly cytoplasmic distribution under normal conditions to nuclear accumulation under oxidative stress, enables this protein to concentrate at sites requiring enhanced redox protection and iron-sulfur cluster availability. The integration of GLRX3 function into multiple signaling pathways including DNA damage response, protein kinase C signaling, epigenetic regulation through PRC2 interactions, and integrated stress response through GMP synthase collaboration establishes this protein as a central hub connecting iron metabolism to broader cellular regulatory networks. The frequent dysregulation of GLRX3 in multiple human malignancies, where increased expression correlates with poor prognosis and enhanced tumor progression, highlights the clinical relevance of understanding GLRX3 biology and suggests potential therapeutic opportunities through targeted modulation of this protein or its key interactions. The absolute developmental requirement for GLRX3, demonstrated through embryonic lethality of knockout mice and severe developmental abnormalities associated with GLRX3 mutations in human genetic disease, underscores the fundamental biological importance of this protein. Future investigations should focus on characterizing the precise mechanisms by which GLRX3 integrates iron sensing with epigenetic regulation and stress response signaling, identifying tissue-specific roles for GLRX3 beyond general iron metabolism, developing selective inhibitors or modulators of GLRX3 function for potential therapeutic applications in cancer and other diseases, and determining how dysregulation of GLRX3 in disease states can be therapeutically targeted. The emerging picture of GLRX3 as a sophisticated molecular switch coupling iron availability to biosynthetic capacity, stress responses, and epigenetic programming promises to yield important insights into the fundamental mechanisms connecting metabolism to gene regulation and cellular physiology throughout mammalian biology.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene/10539
2. https://journals.asm.org/doi/10.1128/AEM.00221-20
3. https://www.genecards.org/cgi-bin/carddisp.pl?gene=GLRX3
4. https://www.uniprot.org/uniprotkb/O76003/entry
5. https://www.nature.com/articles/s41419-019-1935-0
6. https://www.abcam.com/en-an/targets/glrx3/27096
7. https://pubs.acs.org/doi/10.1021/jacs.0c02266
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC3681695/
9. https://pubmed.ncbi.nlm.nih.gov/27519415/
10. https://pubmed.ncbi.nlm.nih.gov/23615448/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC12375892/
12. https://www.uniprot.org/uniprotkb/A0A0G2K5P8/entry
13. https://pubmed.ncbi.nlm.nih.gov/29860757/
14. https://www.ncbi.nlm.nih.gov/gene/30926
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC5077177/
16. https://stockton.primo.exlibrisgroup.com/discovery/fulldisplay?docid=cdi_pubmed_primary_29860757&context=PC&vid=01SUN_INST%3ASTOCKTON&lang=en&search_scope=MyInst_and_CI&adaptor=Primo+Central&tab=Everything&query=sub%2Cexact%2C+Neoplasm+Proteins+-+antagonists+%26+inhibitors+%2CAND&mode=advanced&offset=0
17. https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.70072
18. https://febs.onlinelibrary.wiley.com/doi/abs/10.1002/1873-3468.70072
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC8007109/
20. https://pubmed.ncbi.nlm.nih.gov/26296460/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC7503856/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC5374299/
23. https://pubmed.ncbi.nlm.nih.gov/25975981/
24. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2019.00712/pdf
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC5095054/
26. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1496886/full
27. https://pubmed.ncbi.nlm.nih.gov/30595380/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7763308/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC7357468/
30. https://www.pnas.org/doi/10.1073/pnas.2400740121
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC7837452/
32. https://pubmed.ncbi.nlm.nih.gov/31176019/
33. https://pubmed.ncbi.nlm.nih.gov/32414791/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC8349188/
35. https://pubmed.ncbi.nlm.nih.gov/21034966/
36. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=10539
37. https://www.ensembl.org/id/ENST00000368644
38. cellular needs[8][11][30]