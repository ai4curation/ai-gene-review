---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-03T21:39:45.720171'
end_time: '2025-11-03T21:41:49.198213'
duration_seconds: 123.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: Q86WA8
  gene_symbol: LONP2
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 42
---

## Question

# Gene Research for Functional Annotation

Please provide a comprehensive research report on the gene LONP2 (Q86WA8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function. 

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this comprehensive query about LONP2 (Q86WA8). The user wants a detailed research report about this gene product in humans, with emphasis on:

1. Function - what does it do, what reactions does it catalyze, substrate specificity
2. Localization - where in/outside the cell it functions
3. Biological pathways - biochemical and signaling roles
4. Evidence - experimental, structural, evolutionary, bioinformatic
5. Precise studies prioritized over high-throughput

Let me organize what I found in the search results:

**Basic Information:**
- LONP2 (Lon peptidase 2, peroxisomal) encoded by gene on chromosome 16
- ATP-dependent serine protease
- Alternative names: LONP, LONPL, PLON, PSLON
- 852 amino acid sequence, ~95 kDa molecular weight
- Encoded from nucleus, synthesized in cytoplasm, targeted to peroxisomes

**Structure/Domains:**
- Lon N (substrate recognition) domain
- ATPase domain (Walker A and B motifs - conserved AAA+ region)
- Proteolytic domain (serine-lysine dyad for catalysis)
- PTS1 targeting signal at C-terminus

**Primary Function:**
- ATP-dependent protease mediating selective degradation of misfolded and unassembled polypeptides in peroxisomal matrix
- Both protease and chaperone activity
- Maintains peroxisome homeostasis
- Degrades oxidatively damaged proteins

**Localization:**
- Peroxisomal matrix, specifically concentrated in the dense crystalline core
- High expression in pancreas, kidney, liver

**Substrates:**
- Oxidatively damaged proteins
- TYSND1 (trypsin domain-containing 1 protease)
- Catalase
- PTS2-containing proteins (aids in processing)


- Misfolded polypeptides including casein variants

**Associated Pathways:**
- Peroxisomal protein quality control and fatty acid β-oxidation maintenance
- Oxidative stress and redox homeostasis regulation
- Lipid metabolism support
- circRNA-LONP2 involvement in endothelial dysfunction and atherosclerosis
- Cervical cancer tumorigenesis

**Disease Associations:**
- Buratti-Harel Syndrome (LONP2 mutations)
- Cervical cancer (upregulation)
- Bladder cancer (associated)
- Neurodegenerative conditions

**Supporting Evidence:**
- In vitro casein degradation assays demonstrate substrate specificity
- Fungal models (P. chrysogenum, H. polymorpha) established baseline protease function
- Recent mammalian cell studies (COS-7, U2OS) from 2023 characterized LONP2 depletion effects
- 2024 research linked circRNA-LONP2 to atherosclerosis pathology
- 2018 cervical cancer studies documented upregulation patterns

The experimental foundation spans multiple model systems and timeframes, with recent work expanding understanding of LONP2's role in both metabolic and disease contexts.
</think>

# Comprehensive Functional Annotation of LONP2: The Peroxisomal Lon Peptidase 2 in Human Biology

This report presents a detailed analysis of LONP2 (Lon peptidase 2, peroxisomal), encoded by the human LONP2 gene located on chromosome 16, with comprehensive coverage of its enzymatic function, structural organization, subcellular localization, metabolic roles, and involvement in both physiological and pathological processes. LONP2 is an ATP-dependent serine protease that serves as a critical regulator of peroxisomal protein quality control through selective degradation of misfolded and oxidatively damaged proteins. Operating within the peroxisomal matrix, particularly concentrated in the crystalline core where oxidative stress is most pronounced, LONP2 functions as both a protease and molecular chaperone to maintain protein homeostasis in this essential metabolic organelle. Beyond its canonical proteolytic role, emerging evidence demonstrates that LONP2 regulates peroxisomal fatty acid beta-oxidation, participates in lipid metabolism pathways, and influences cellular responses to oxidative stress. Furthermore, dysregulation of LONP2 expression and activity has been associated with multiple disease states including cervical carcinogenesis, endothelial dysfunction, and the neurodevelopmental disorder Buratti-Harel Syndrome. This comprehensive review synthesizes current understanding of LONP2 structure, function, regulation, and disease relevance based on experimental evidence, structural analysis, and evolutionary considerations.

## Structural Organization and Molecular Characterization of LONP2

### Primary Structure and Evolutionary Conservation

The human LONP2 protein is composed of 852 amino acids with a calculated molecular weight of approximately 95 kilodaltons in its mature form[12]. LONP2 belongs to the Lon A family of proteases, representing the primary form of Lon protease found across prokaryotes and eukaryotes[12]. The protein is encoded by the LONP2 gene from the nuclear genome on chromosome 16 and is synthesized on free ribosomes in the cytoplasm before being targeted to the peroxisomal compartment[12]. The evolutionary origin of LONP2 is particularly notable, as it represents an early gene duplication product of the mitochondrial LONP1 protease that was retained and specialized for peroxisomal function[53]. While LONP2 has been identified in diverse organisms including mammals, yeast, nematodes, and fungi such as Phaffia chrysogenum and Hansenula polymorpha, suggesting conservation across eukaryotic life, the peroxisomal Lon isoform appears less universally conserved than its mitochondrial counterpart, having not been physically detected in Drosophila melanogaster despite extensive characterization in most other model organisms[30].

### Functional Domains and Catalytic Architecture

The LONP2 protein exhibits a highly organized multi-domain architecture that orchestrates its diverse enzymatic and chaperone functions[12]. The N-terminal region contains the Lon N substrate recognition domain, which operates through a non-catalytically active serine residue that facilitates substrate binding rather than catalysis[12]. This substrate recognition domain plays a critical role in identifying target proteins for degradation and has been shown to be important for dodecamer assembly in related Lon proteases, suggesting that it may modulate substrate specificity through conformational changes[31]. The central ATPase domain contains the canonical Walker A and B motifs characteristic of AAA+ (ATPases Associated with diverse cellular Activities) proteases[12]. These Walker motifs are conserved three-dimensional protein structures that mediate ATP binding and hydrolysis, allowing LONP2 to harness the energy of ATP to power substrate unfolding and translocation[12]. The carboxyl-terminal proteolytic domain contains the catalytically active serine-lysine dyad responsible for peptide bond cleavage[12]. This serine-lysine catalytic pair represents a unique mechanistic approach among serine proteases, where the lysine acts as a general base to activate the serine nucleophile for attack on the carbonyl carbon of the scissile peptide bond[45].

### Peroxisomal Targeting and Subcellular Localization

LONP2 contains a C-terminal peroxisomal targeting signal (PTS1) consisting of the characteristic SKL (serine-lysine-leucine) or variant motif that directs the protein to peroxisomes[12]. The PTS1 sequence is recognized by the peroxisomal import receptor Pex5, which shuttles LONP2 across the peroxisomal membrane into the matrix[18]. Critically, unlike most organellar import signals that are removed during or immediately after translocation, the PTS1 sequence of LONP2 is preserved upon import into the peroxisome, suggesting that this targeting information may serve additional regulatory functions beyond initial targeting[18]. Ultracentrifugation studies using antibodies raised against the C-terminal region of LONP2 have demonstrated that this protease not only localizes to the peroxisomal matrix but specifically concentrates within the dense crystalline core of the organelle[30]. This concentration pattern is particularly instructive regarding LONP2's functional role. The crystalline core of mammalian liver peroxisomes is primarily composed of urate oxidase and is notably devoid of catalase and other oxidases[30]. Consequently, hydrogen peroxide accumulates in this sub-compartment and cannot be effectively degraded, leading to rapid oxidative damage of proteins in close proximity. The strategic positioning of LONP2 in this highly oxidizing microenvironment parallels the localization of mitochondrial Lon protease (LonP1) near the inner mitochondrial membrane, where both enzymes maintain high concentration and close proximity to proteins at risk of oxidative damage requiring rapid degradation[30].

In mammalian tissues, LONP2 is ubiquitously distributed throughout the body, with particularly elevated expression patterns in organs with high metabolic activity and oxidative burden[30]. Specifically, the pancreas, kidney, and liver show the highest levels of LONP2 expression[30], consistent with the lipid-metabolizing and energy-producing functions of these tissues. Additional analysis of tissue-specific expression patterns indicates substantial representation in tissues with specialized lipid metabolism requirements, including multiple brain regions, adipose tissue, and reproductive organs where ether lipid biosynthesis and fatty acid oxidation are particularly important[6].

## Enzymatic Function and Substrate Specificity of LONP2

### ATP-Dependent Proteolytic Mechanism

LONP2 functions as an ATP-dependent protease that mediates the selective degradation of misfolded and unassembled polypeptides within the peroxisomal matrix[4][10]. A fundamental characteristic of LONP2 as an ATP-dependent enzyme is that ATP hydrolysis is absolutely essential for proteolytic activity; in the absence of ATP, LONP2 exhibits less than 3% of its normal enzymatic activity[55]. The ATP-stimulated activity of LONP2 was originally discovered through in vitro studies employing the fungus Phaffia chrysogenum, where purified LONP2 rapidly degraded misfolded model substrates such as α-casein and β-casein specifically in the presence of ATP[7]. Quantitative measurements using resorufin-labeled β-casein as a fluorescent substrate demonstrated that LONP2 exhibited high proteolytic activity only upon ATP addition, establishing the strict requirement for ATP in the catalytic cycle[7]. As definitive proof of principle, mutagenesis of the catalytically active serine residue in the proteolytic domain rendered the enzyme completely non-functional, preventing substrate degradation even in the presence of both misfolded casein and ATP[7]. This catalytic mechanism whereby LONP2 utilizes ATP hydrolysis for substrate degradation appears to differ functionally from mitochondrial LonP1, which uses ATP hydrolysis to induce conformational changes in the proteolytic site rather than for direct substrate degradation[7]. Future studies employing non-hydrolysable ATP analogs are anticipated to clarify whether LONP2 uses ATP as a true substrate cofactor for degradation reactions or in a role more similar to LonP1's conformational activation mechanism.

### Substrate Recognition and Protein Specificity

The primary substrates targeted for degradation by LONP2 are proteins bearing oxidative damage or those misfolded due to post-translational processing defects. The recognition mechanism employed by LONP2 relies on the Lon N substrate recognition domain binding to oxidized proteins in which hydrophobic residues normally buried in the native protein core become exposed through protein unfolding[7]. This recognition pattern indicates that LONP2 functions as a general oxidative damage sensor rather than recognizing specific sequence motifs or structured domains. The binding of oxidized substrates to the non-catalytic serine residue in the Lon N domain facilitates productive enzyme-substrate complex formation that positions the substrate for translocation through the central pore of the LONP2 oligomer and into the catalytic chamber where proteolysis occurs[7].

Experimentally identified substrates of LONP2 in mammalian cells include the serine protease trypsin domain-containing 1 (Tysnd1), which itself is responsible for processing peroxisomal enzymes including acyl-coenzyme A oxidase 1 (ACOX1)[50][53]. The relationship between LONP2 and Tysnd1 is particularly notable; Tysnd1 undergoes self-cleavage to generate inactive fragments, which are subsequently degraded by LONP2[18]. This degradation may not reflect a specific substrate-enzyme pairing but rather LONP2's general affinity for proteins displaying exposed hydrophobic residues characteristic of proteolytic cleavage products and damaged proteins[18]. Additional characterized LONP2 substrates identified in fungal systems include catalase, the most abundant peroxisomal antioxidant, which undergoes oxidative damage and functional loss even at relatively low hydrogen peroxide concentrations[7]. Even at concentrations as low as 100 micromolar H₂O₂, catalase can experience approximately 40% loss of enzymatic function, and higher H₂O₂ levels exacerbate both catalase dysfunction and accumulation of non-functional proteins[7]. The peroxisome maintains high catalase concentrations and relies substantially on LONP2-mediated degradation of dysfunctional catalase to mitigate this progressive loss of catalytic capacity[7].

The substrate specificity of LONP2 appears to be primarily determined by exposure of hydrophobic amino acid residues rather than recognition of structured degron sequences, suggesting broad substrate range encompassing all oxidatively damaged peroxisomal proteins. This mechanism provides the peroxisomal matrix with a flexible quality control system capable of responding to diverse types of oxidative damage rather than requiring pre-specified targeting sequences for each substrate.

## Chaperone Functions and Protein Homeostasis Maintenance

### ATP-Independent Chaperone Activity

Beyond its primary role as a protease, LONP2 possesses distinct chaperone-like activity that operates independently of ATP hydrolysis and contributes to overall peroxisomal protein quality control[28]. When purified LONP2 was incubated with denatured citrate synthase under experimental conditions, the presence of Lon, independent of ATP, decreased protein aggregation by approximately 40% compared to control samples lacking the protease[28]. Complete inhibition of protein aggregation was achieved through increasing LONP2 concentrations, and enzymatic activity of the denatured substrate protein was successfully re-established following ATP addition, demonstrating that aggregation prevention occurred through a chaperone mechanism rather than through proteolytic degradation[28]. These findings establish that LONP2 possesses multifunctional characteristics, combining both ATP-dependent proteolytic and ATP-independent chaperone activities in a single polypeptide[28]. Unlike mitochondria, which contain comprehensive protein folding machinery including heat shock response proteins such as Hsp60 and mtHsp70, peroxisomes appear to lack dedicated chaperone systems, potentially because proteins are typically imported as fully folded entities[28]. The evolution of LONP2 as a bifunctional protein capable of acting as both an ATP-dependent protease and an ATP-independent chaperone may therefore represent an adaptation to the unique protein homeostasis requirements of the peroxisomal compartment[28].

The relationship between these two activities appears to be dynamically regulated according to cellular requirements[28]. During peroxisome biogenesis and normal metabolic states, the ATP-independent chaperone activity of LONP2 may assist in the correct folding and assembly of newly imported proteins. During periods of decreased metabolic need or in response to oxidative stress, the proteolytic activity of LONP2 becomes dominant, facilitating removal of unnecessary peroxisomal proteins through a combination of direct proteolysis and activation of autophagy-based degradation pathways including pexophagy[28]. This dynamic modulation of protease versus chaperone activity in response to metabolic state represents a sophisticated regulatory mechanism for peroxisomal homeostasis.

### Prevention of Protein Aggregation and Inclusion Body Formation

The pathological consequences of LONP2 loss extend to accumulation of insoluble protein aggregates and inclusion bodies within the peroxisomal matrix. Studies in the fungus Phaffia chrysogenum harboring deletion mutations of the peroxisomal Lon gene (pln) demonstrated marked increases in the accumulation of electron-dense protein aggregates, accompanied by increased peroxisome number and enlargement[30]. These protein aggregates were characterized as likely substrates for normal LONP2 degradation, indicating that loss of LONP2 directly results in accumulation of misfolded protein polymers[30]. This phenotype parallels the protein aggregates that arise in Caenorhabditis elegans mutants lacking the mitochondrial Lon homologue (PIM1), as well as in senescent cells lacking mitochondrial Lon activity, suggesting conservation of this quality control function across both organellar compartments and evolutionary distance[30]. The significance of preventing aggregate formation is underscored by the observation that protein aggregates are prevalent markers in senescent cells and are associated with cellular dysfunction, suggesting that LONP2-mediated prevention of aggregation is critical for maintaining peroxisomal and cellular health throughout the lifespan[30].

## Biological Roles in Peroxisomal Fatty Acid Metabolism

### Integration with Beta-Oxidation Pathways

Peroxisomes function as essential sites for the initial oxidation of very-long-chain fatty acids (VLCFAs) containing 20 or more carbons, as well as branched-chain and di- or tri-hydroxylated fatty acids that cannot be processed by mitochondrial beta-oxidation machinery[11][39]. The primary peroxisomal role in human physiology is catalyzing fatty acid beta-oxidation and, as a necessary byproduct of this oxidative process, generating both hydrogen peroxide and superoxide[2][5]. LONP2 maintains the functionality of this critical metabolic pathway by proteolytically degrading peroxisomal proteins damaged by the oxidative stress inherent to beta-oxidation. Through studies employing gene knockout approaches, LONP2 depletion has been shown to impair peroxisomal fatty acid metabolism through both direct proteolytic effects and indirect metabolic disruption[20]. The degradation of TYSND1 by LONP2 is particularly relevant to fatty acid metabolism maintenance; TYSND1 itself is responsible for the specific processing and post-translational modification of peroxisomal beta-oxidation enzymes, particularly ACOX1[18]. Loss of TYSND1 processing by LONP2 results in accumulation of immature beta-oxidation enzymes and diminished processing capacity for long-chain fatty acids[18][20].

Recent lipidomic analysis of cells with LONP2 silencing revealed dramatic alterations in lipid composition, including accumulation of very-long-chain fatty acid-containing lipids, altered phosphatidylcholine composition reflecting substantial fatty acyl side-chain remodeling, and increased sphingomyelins and cholesterol esters[20][36]. These lipidomic changes were notable for being partially cell-type specific, with COS-7 cells and U2OS cells showing different magnitudes and patterns of lipid disruption despite similar peroxisomal morphological changes[20][36]. This differential response suggests that peroxisomes exhibit substantial functional plasticity depending on tissue context and that the specific consequences of peroxisomal LONP2 loss may vary based on the particular lipid metabolic demands of different cell types and tissues[36].

### PTS2 Protein Processing and Import Regulation

LONP2 plays a direct role in peroxisomal protein import regulation through its involvement in processing peroxisomal targeting signal 2 (PTS2) containing proteins[15]. PTS2 represents the less common peroxisomal targeting sequence, comprising nine amino acids located on the N-terminus of target proteins and recognized by the PTS2 receptor Pex7[18]. Following translocation across the peroxisomal membrane, PTS2 sequences are often removed through proteolytic cleavage of the N-terminal targeting propeptide, and LONP2 may participate in this maturation process[27]. The functional significance of this PTS2-associated proteolysis appears to facilitate accumulation of processed proteins within the peroxisomal matrix by removing targeting sequences that otherwise might recycle these proteins back to the cytosol in complex with their import receptors[27]. For PTS1 proteins, the functional significance of peroxisomal processing remains less completely understood, as many PTS1 signal sequences are preserved following translocation and numerous PTS1-containing proteins remain catalytically active without proteolytic maturation, suggesting that processing may serve regulatory rather than activation functions[27].

## Regulation of Cellular Redox Homeostasis and Oxidative Stress Response

### Peroxisomal Contribution to Cellular ROS Generation and Management

Peroxisomes constitute a major but often underappreciated source of cellular oxidative stress, accounting for approximately 20% of total cellular oxygen consumption and contributing 35% of total hydrogen peroxide generation in mammalian tissues[11][23]. This substantial ROS production results from both the inevitable byproducts of fatty acid beta-oxidation (hydrogen peroxide) and from multiple peroxisomal oxidases including acyl-CoA oxidases and other oxidative enzymes that generate reactive oxygen species including superoxide and hydroxyl radicals as functional byproducts[11][23]. To maintain cellular homeostasis in the face of this oxidative burden, peroxisomes contain a sophisticated antioxidant defense system comprising catalase (the most abundant peroxisomal antioxidant and sole enzyme capable of catalyzing H₂O₂ dismutation), superoxide dismutase 1 (SOD1), peroxiredoxin 5 (Prx5), S-transferase kappa, epoxide hydrolase, and glutathione peroxidase (GPx)[11][23]. Notably, LonP2 has recently been identified alongside insulin-degrading enzyme and PEX11β as a peroxisomal protein that contributes to maintenance of peroxisomal redox homeostasis through mechanisms that extend beyond the canonical antioxidant enzymatic systems[11][23].

The accumulation of oxidatively damaged proteins within peroxisomes represents a critical threat to organellar and cellular function. Deficiencies in peroxisomal antioxidant proteins such as catalase can perturb the mitochondrial redox potential, indicating that peroxisomal dysfunction triggers effects that propagate to the mitochondrial compartment[11][23]. Furthermore, local oxidative damage to peroxisomes eventually results in mitochondrial dysfunction and cellular apoptosis, implicating peroxisomes as upstream initiators of mitochondrial ROS signaling and suggesting that peroxisomal quality control is paramount to cellular survival[11][23]. LONP2's role in preventing oxidative protein damage accumulation within peroxisomes is therefore critical to maintaining not only peroxisomal integrity but also broader cellular redox balance and mitochondrial function.

### Evidence for Proteotoxic Stress in LONP2-Deficient Cells

Recent mammalian cell studies employing acute LONP2 silencing via siRNA approaches have revealed that loss of LONP2 triggers cell-type-specific stress responses distinct from total loss of peroxisomal protein import[20][25]. In monkey kidney COS-7 cells with LONP2 knockdown, significant accumulation of mitochondrial reactive oxygen species was detected, measured by MitoSOX staining[25]. Additionally, LONP2-depleted COS-7 cells activated the integrated stress response (ISR), an evolutionary conserved eukaryotic signaling pathway that attenuates cap-dependent translation through phosphorylation of eukaryotic translation initiation factor 2 alpha (eIF2α)[25]. This ISR activation was accompanied by induction of multiple ISR effector transcription factors (ATF3, ATF4, ATF5, and CHOP encoded by DDIT3) and their downstream targets[25]. Consistent with ISR activation, dramatic reduction of protein synthesis was detected in LONP2-depleted COS-7 cells through puromycin pulse-labeling, a key consequence of eIF2α phosphorylation[25]. Global cellular stress in LONP2-depleted COS-7 cells was further evidenced by activation of apoptosis-associated cleaved caspases 3 and 7, increased DNA damage as monitored by γ2HAX phosphorylation, and induction of NF-κB, a regulator of innate immunity[25]. Remarkably, identical LONP2 depletion in human U2OS osteosarcoma cells did not induce these stress responses, demonstrating that the proteotoxic peroxisomal stress response activates the ISR in a cell-type-specific manner[25]. This differential response likely reflects distinct peroxisomal metabolic demands in different cell types, with certain tissues exhibiting greater dependence on LONP2-mediated proteostasis.

The differential transcriptomic responses observed between COS-7 and U2OS cells upon LONP2 silencing were striking, with over 7,000 differentially expressed genes identified in COS-7 cells compared to fewer than 300 genes in U2OS cells[25]. COS-7 cells specifically upregulated multiple genes involved in ribosome biogenesis, an unexpected finding given that ribosome biogenesis is generally suppressed under cellular stress conditions[25]. Expression of RRS1, a core mediator of ribosomal assembly, was increased at both the mRNA and protein levels in LONP2-depleted COS-7 cells[25]. This paradoxical upregulation of ribosomal biogenesis genes in the context of overall protein synthesis reduction suggests a complex cellular attempt to restore homeostasis through increased ribosomal capacity. The lipidomic changes described above further highlight that LONP2 loss disrupts multiple interconnected metabolic and signaling pathways depending on cell type and tissue context.

## Association with Disease States and Clinical Implications

### Buratti-Harel Syndrome and Neurodevelopmental Pathology

LONP2 mutations have been identified as causative genetic variants in Buratti-Harel Syndrome (BURHAS), an autosomal dominant neurodevelopmental disorder characterized by infantile hypotonia, global developmental delay, and impaired intellectual development[26][29]. Affected individuals present with infantile hypotonia apparent from early infancy, generalized developmental delay, and delays in motor, language, and speech development with mildly to moderately impaired intellectual function[26]. Many patients exhibit learning difficulties and attend special education programs, while more severely affected individuals show greater functional impairment[26]. Characteristic dysmorphic facial features include hypertelorism (widely spaced eyes), downslanting palpebral fissures, strabismus, and small low-set ears[26]. Additional clinical features frequently present include laryngomalacia with associated feeding difficulties and distal skeletal anomalies[26]. The association between LONP2 mutations and this neurodevelopmental phenotype implicates peroxisomal quality control specifically in proper brain development and function, suggesting that peroxisomal protein homeostasis is critical during neurodevelopmental processes.

The pathogenic mechanisms by which LONP2 mutations cause neurodevelopmental disease likely involve accumulation of misfolded proteins and oxidatively damaged peroxisomal proteins in neural tissues, particularly given the high metabolic demands and oxidative stress burden of the developing and mature nervous system. However, the precise molecular mechanisms by which LONP2 loss leads to the specific clinical features of BURHAS remain to be fully elucidated, representing an important area for further research.

### LONP2 Upregulation and Cervical Carcinogenesis

Multiple lines of evidence demonstrate that LONP2 is significantly upregulated in cervical cancer tissue and contributes to cervical tumorigenesis through mechanisms involving oxidative stress modulation[1][38]. Oncomine database analysis and immunohistochemical examination of tissue microarrays demonstrated that LONP2 expression is significantly upregulated in cervical cancer compared to normal cervical tissue, with expression levels approximately twofold higher in cancerous samples[38]. This upregulation showed significant associations with pathological type, pathological grade, and clinical stage of cervical cancer, though no association was detected with patient age or lymph node metastasis status[38]. Experimental knockdown of LONP2 using RNA interference in cervical cancer cell lines HeLa and SiHa reduced cell proliferation, impaired cell cycle progression, induced apoptosis, and decreased both migration and invasion capacity[38]. Notably, LONP2 knockdown reduced oxidative stress levels within cervical cancer cells as measured by ROS production through immunofluorescence and flow cytometry analysis[38]. These findings suggest that LONP2 promotes cervical tumorigenesis through modulation of intracellular oxidative stress levels, potentially enabling cancer cells to maintain metabolic flexibility and adaptive redox states that support tumor growth and metastatic progression[38].

The mechanism by which increased LONP2 activity supports tumorigenesis appears to involve enhanced degradation of oxidatively damaged proteins that would otherwise accumulate and trigger stress responses limiting cancer cell growth. By maintaining peroxisomal proteostasis despite the elevated metabolic activity and ROS production of cancer cells, LONP2 may enable cancer cells to tolerate the oxidative stress that would otherwise activate growth-limiting stress response pathways. This makes LONP2 a potential biomarker and therapeutic target for cervical cancer treatment[38].

### CircRNA-LONP2 and Endothelial Dysfunction in Atherosclerosis

Recent evidence reveals a novel functional role for circular RNA derived from the LONP2 locus (circRNA-LONP2) in modulating endothelial dysfunction and atherosclerosis progression, distinct from the role of linear LONP2 mRNA and protein[8]. Importantly, circRNA-LONP2, but not its linear transcript counterpart, emerged as the major cause of inflammation and oxidative stress in endothelial cells through its modulation of specific signaling pathways[8]. Oscillatory (disturbed) shear stress (OSS), the abnormal blood flow pattern that develops in regions of arterial branching and curvature and drives atherosclerosis development, upregulated circRNA-LONP2 expression in endothelial cells[8]. In contrast, laminar shear stress (LSS), the physiological blood flow pattern that protects arteries from atherosclerosis, downregulated circRNA-LONP2 expression[8]. This regulation of circRNA-LONP2 by hemodynamic shear stress represents a novel molecular mechanism linking blood flow patterns to atherosclerotic disease progression.

The molecular mechanism by which circRNA-LONP2 promotes endothelial inflammation involves suppression of microRNA-200a-3p (miR-200a-3p), which normally targets and degrades messenger RNAs for KEAP1, YAP1, and EZH2[8]. By sequestering miR-200a-3p, circRNA-LONP2 allows accumulation of KEAP1, which maintains the transcription factor NRF2 in an inactivated cytoplasmic state through ubiquitin-mediated degradation[8]. Under normal LSS conditions that reduce circRNA-LONP2, miR-200a-3p is liberated and degrades KEAP1 mRNA, allowing NRF2 to accumulate, translocate to the nucleus, and activate transcription of antioxidant response element-containing genes including HO-1 (heme oxygenase-1)[8]. This NRF2/HO-1 activation pathway suppresses oxidative stress and endothelial inflammation[8]. Conversely, under OSS conditions that upregulate circRNA-LONP2, this protective miR-200a-3p-mediated NRF2 activation is suppressed, leading to increased ROS production and endothelial cell inflammation, processes that accelerate atherosclerosis[8]. The identification of circRNA-LONP2 as a therapeutic target provides potential strategies for atherosclerosis prevention and treatment through endothelial-specific knockdown of circRNA-LONP2 or its downstream targets KEAP1, YAP1, or EZH2[8].

## Relationship to Mitochondrial Lon (LonP1) and Functional Divergence

### Comparative Structure and Functional Specialization

While LONP2 and mitochondrial Lon protease (LonP1) share substantial structural similarity and evolutionary origin, they exhibit important functional differences that reflect specialization to their respective organellar environments[3][12]. Both LonP1 and LonP2 contain conserved N-domains for substrate recognition, classical ATPase domains containing Walker A and B motifs, and C-terminal proteolytic domains with serine-lysine catalytic dyads[12]. However, a critical functional distinction concerns the role of ATP hydrolysis in catalysis. While both are ATP-stimulated enzymes, LonP1 appears to utilize ATP hydrolysis primarily to induce conformational changes in the proteolytic site to allow for substrate degradation, whereas LONP2 may employ ATP hydrolysis more directly in substrate degradation itself[7]. The exact mechanistic differences remain to be fully clarified through studies employing non-hydrolysable ATP analogs and biochemical analysis of the kinetic pathways.

LonP1 dysfunction has been extensively characterized in aging and disease, with studies establishing the importance of mitochondrial Lon in relation to oxidative stress, aging-related diseases, and cancer[32]. In contrast, little was historically known regarding the specific role of LonP2 in aging and age-related pathological changes in the peroxisome[3]. However, the recent recognition that peroxisome dysfunction is associated with multiple aging-related diseases indicates that peroxisomal protein quality control mechanisms including LONP2-mediated proteolysis represent a critical component of healthy aging[3].

### Cross-Compartment Communication and Metabolic Coordination

Although mitochondria and peroxisomes are both essential for fatty acid metabolism, particularly through their coordinated handling of different classes of fatty acids, relatively little work has focused on understanding the relationship between these two organelles or how age-dependent changes in one may detrimentally affect the other[3]. LONP2 and LonP1 may function as communication nodes between these metabolically interdependent organelles. Given the metabolic coordination between peroxisomes and mitochondria in fatty acid oxidation and the shared reliance on ATP-dependent quality control mechanisms, understanding the role of LONP2 in the aging peroxisome may help elucidate cellular causes for both peroxisomal and mitochondrial dysfunction[3]. This represents a promising area for future research into the origins of age-related metabolic decline and associated disease susceptibility.

## Emerging Concepts: Peroxisomal Proteostasis as a Systems-Level Regulatory Mechanism

### Integration of Multiple Cellular Pathways

Recent findings from transcriptomic and lipidomic studies of LONP2-depleted cells reveal that peroxisomal quality control through LONP2-mediated proteolysis functions not merely as a local compartmental homeostasis mechanism but as an integrator of multiple cellular processes[20][25]. The specific coupling of peroxisomal LONP2 activity to cholesterol trafficking, retinoic acid signaling, and ribosome biogenesis identified in mammalian cells suggests that peroxisomal proteostasis serves as a sensor of organellar metabolic state with outputs affecting multiple signaling and biosynthetic pathways[20][25]. The cell-type-specific nature of responses to LONP2 loss further indicates that the functional consequences of peroxisomal proteostasis are highly context-dependent, potentially explaining why peroxisomal disorders present with tissue-specific pathology.

### Evolutionary and Biophysical Insights

The hexameric ring architecture of Lon proteases, shared with other AAA+ proteases, enables formation of higher-order oligomeric states including dodecamers that modulate substrate specificity and degradation rates[31]. LONP2 likely assembles into similar ring structures with properties that can be regulated through oligomerization state. The concentration of LONP2 within the highly oxidizing peroxisomal crystalline core, where substrate proteins bearing hydrophobic residues characteristic of oxidative damage are most prevalent, represents an elegant evolutionary optimization positioning the protease where it is most needed.

## Conclusion and Future Directions

LONP2 represents a multifunctional ATP-dependent serine protease specialized for maintaining proteostasis in the peroxisomal matrix through selective degradation of oxidatively damaged and misfolded proteins and through ATP-independent chaperone activity[4][10][12]. Localized to the peroxisomal matrix and concentrated within the oxidizing crystalline core, LONP2 functions at the interface of peroxisomal fatty acid metabolism, redox homeostasis, and protein quality control[2][7][11][30]. Through its degradation of substrates including TYSND1, catalase, and other oxidatively damaged proteins, LONP2 maintains the functional capacity of peroxisomal metabolic pathways and prevents accumulation of protein aggregates that would compromise organellar and cellular function[7][18][30][53]. Beyond local proteolytic effects, emerging evidence demonstrates that LONP2 activity dynamically regulates multiple cellular processes including lipid metabolism, stress response pathways, and ribosomal biogenesis in a cell-type-dependent manner[20][25][36].

The disease associations of LONP2 dysregulation spanning the neurodevelopmental Buratti-Harel Syndrome, cancer-associated overexpression in cervical carcinogenesis, and the emerging role of circRNA-LONP2 in cardiovascular disease underscore the critical importance of proper LONP2 regulation to cellular and organismal health[8][26][38]. Future research elucidating the precise ATP utilization mechanism of LONP2, identifying the complete repertoire of LONP2 substrates and substrate recognition determinants, investigating the dynamic regulation of protease versus chaperone activity, and exploring the integration of LONP2 function with mitochondrial quality control and organellar cross-communication will significantly advance understanding of peroxisomal biology and provide insights into disease pathogenesis. Additionally, determining whether LONP2 can be therapeutically targeted in cancer and cardiovascular disease contexts while maintaining normal developmental and metabolic functions represents an important translational avenue warranting investigation.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene/83752
2. https://en.wikipedia.org/wiki/Lon_peptidase_2,_peroxisomal
3. https://onlinelibrary.wiley.com/doi/abs/10.1111/brv.12253
4. https://www.uniprot.org/uniprotkb/Q86WA8/entry
5. http://biogps.org/gene/83752/
6. https://www.proteinatlas.org/ENSG00000102910-LONP2
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC5159316/
8. https://www.jacc.org/doi/10.1016/j.jacbts.2024.02.019
9. https://www.uniprot.org/uniprotkb/F6T3M1/entry
10. https://www.nature.com/articles/s12276-020-00503-9
11. https://en.wikipedia.org/wiki/Peroxisomal_targeting_signal
12. https://geneglobe.qiagen.com/us/knowledge/gene/ENSG00000102910
13. https://www.genecards.org/cgi-bin/carddisp.pl?gene=LONP2
14. https://www.uniprot.org/uniprotkb/Q86WA8/publications
15. https://www.promega.ca/findmygene/genedetail.aspx?ncbiid=83752
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC10967733/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC10515011/
18. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.14704
19. https://pubmed.ncbi.nlm.nih.gov/16337203/
20. https://www.malacards.org/card/buratti_harel_syndrome
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC1794383/
22. https://rddc.tsinghua-gd.org/disease/BRT061
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC3670373/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC5183306/
25. https://pubmed.ncbi.nlm.nih.gov/23674680/
26. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2022.982564/full
27. https://pubmed.ncbi.nlm.nih.gov/29502128/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7829553/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC10309183/
30. https://experts.llu.edu/en/publications/cellular-levels-of-oxidative-stress-affect-the-response-of-cervic-2
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC3138309/
32. https://pubmed.ncbi.nlm.nih.gov/16584747/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC2443057/
34. https://v22.proteinatlas.org/ENSG00000102910-LONP2/tissue
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC11986505/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC3324771/
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC11658196/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC3108460/
39. https://www.pnas.org/doi/10.1073/pnas.95.18.10584
40. https://www.ncbi.nlm.nih.gov/books/n/eurekah/A21674/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC9961632/
42. cellular requirements[28]