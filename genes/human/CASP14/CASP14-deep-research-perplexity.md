---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-23T16:46:36.472345'
end_time: '2025-11-23T16:48:51.978752'
duration_seconds: 135.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CASP14
  gene_symbol: CASP14
  uniprot_accession: P31944
  protein_description: 'RecName: Full=Caspase-14; Short=CASP-14; EC=3.4.22.-; Contains:
    RecName: Full=Caspase-14 subunit p17, mature form; Contains: RecName: Full=Caspase-14
    subunit p10, mature form; Contains: RecName: Full=Caspase-14 subunit p20, intermediate
    form; Contains: RecName: Full=Caspase-14 subunit p8, intermediate form; Flags:
    Precursor;'
  gene_info: Name=CASP14;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the peptidase C14A family. .
  protein_domains: Caspase-like_dom_sf. (IPR029030); Caspase_cys_AS. (IPR033139);
    Pept_C14. (IPR002398); Pept_C14_caspase. (IPR011600); Pept_C14_p10. (IPR002138)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 44
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P31944
- **Protein Description:** RecName: Full=Caspase-14; Short=CASP-14; EC=3.4.22.-; Contains: RecName: Full=Caspase-14 subunit p17, mature form; Contains: RecName: Full=Caspase-14 subunit p10, mature form; Contains: RecName: Full=Caspase-14 subunit p20, intermediate form; Contains: RecName: Full=Caspase-14 subunit p8, intermediate form; Flags: Precursor;
- **Gene Information:** Name=CASP14;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the peptidase C14A family. .
- **Key Domains:** Caspase-like_dom_sf. (IPR029030); Caspase_cys_AS. (IPR033139); Pept_C14. (IPR002398); Pept_C14_caspase. (IPR011600); Pept_C14_p10. (IPR002138)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CASP14" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CASP14' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CASP14** (gene ID: CASP14, UniProt: P31944) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this research query carefully. The user is asking for a comprehensive research report on the CASP14 gene (UniProt: P31944) in humans. They've provided me with extensive search results on this topic.

First, let me verify that I'm looking at the correct gene:
- Gene symbol: CASP14 
- Protein: Caspase-14
- UniProt: P31944
- Organism: Homo sapiens (Human)
- Protein family: peptidase C14A family, cysteine-aspartic acid protease (caspase) family
- EC number: 3.4.22.- (a protease)

Looking through the search results, I can see extensive documentation about CASP14:
- It's encoded on chromosome 19 [1][4]
- It's a member of the caspase family of cysteine-aspartic acid proteases [1][3][9]
- It's uniquely expressed in terminally differentiating keratinocytes [1][10]
- It's involved in keratinocyte terminal differentiation and cornification, NOT apoptosis [7][10]
- It plays a crucial role in skin barrier formation [8][10]
- It processes filaggrin into natural moisturizing factors [8]

The literature is abundant and specific to this gene. I have plenty of material to work with.

Let me plan my report structure:

1. **Title and Introduction** - Overview of Caspase-14
2. **Molecular Structure and Classification** - What type of protein it is, domain architecture
3. **Expression and Localization** - Where and when it's expressed
4. **Enzymatic Properties and Activation Mechanism** - How it's activated, unusual features
5. **Substrate Specificity and Catalytic Function** - What it cleaves and why
6. **Primary Biological Function: Keratinocyte Differentiation and Cornification** - Its main role


7. **Role in Skin Barrier Formation** - Exploring its critical function in maintaining epidermal integrity
8. **Enzymatic Interactions** - Investigating key molecular targets and processing mechanisms
9. **Pathological Implications** - Examining potential disease associations and genetic variations
10. **Comparative Genomics** - Tracing evolutionary conservation across species
11. **Research Synthesis** - Integrating current understanding and future research directions

I'll develop a comprehensive scientific narrative that captures the nuanced molecular biology of this fascinating protein.
</think>

# Caspase-14: A Unique Non-Apoptotic Protease Essential for Epidermal Barrier Function

Caspase-14 (CASP14) represents a distinctive member of the cysteine-aspartic acid protease family that has evolved specialized functions in skin biology, fundamentally diverging from the canonical apoptotic roles of other caspases. Unlike its widely-studied family members that orchestrate programmed cell death through apoptosis, **caspase-14 functions as an essential protease in keratinocyte terminal differentiation and cornification**, a unique form of developmentally-regulated cell death that generates the protective epidermal barrier of mammalian skin.[1][10][38] The discovery and characterization of caspase-14 has revealed that caspases possess functional versatility beyond their classical association with inflammation and apoptosis, establishing this enzyme as a paradigm for understanding context-dependent protease function in tissue-specific cellular differentiation programs.[32][38] Recent research utilizing knockout mouse models, structural studies, and clinical observations of human patients with CASP14 mutations has illuminated the precise enzymatic mechanisms through which caspase-14 processes its substrates and maintains skin homeostasis, while simultaneously raising questions about the evolutionary pressures that led to the loss of this gene in aquatic mammals.[37][40]

## Molecular Classification and Domain Architecture of Caspase-14

Caspase-14 is encoded by the CASP14 gene located on human chromosome 19p13.1 and belongs to the cysteine-aspartic acid protease (caspase) family, a group of 11 proteolytically active caspases plus caspase-14 in humans.[1][9] The caspase family is structurally unified by a catalytic domain architecture conserved over at least 650 million years of evolution, yet caspase-14 possesses several unique structural features that distinguish it from other family members.[30] **The caspase family is classified into multiple functional groups based on their domain organization and biological roles**, with caspase-14 notably belonging to the subset of caspases with either short or absent pro-domains, similar to the executioner caspases-3, -6, and -7.[9][56] However, in striking contrast to these executioner caspases that participate in apoptotic cascades, caspase-14 remains catalytically inactive in the context of standard apoptotic stimuli, positioning it as a functionally distinct protease despite its structural classification.[36]

The native caspase-14 procaspase is synthesized as a single polypeptide chain with a molecular weight of approximately 28 kilodaltons and lacks a defined N-terminal prodomain like caspases-3, -6, and -7, being instead composed entirely of a catalytic domain.[44] This catalytic domain architecture consists of a large subunit (approximately 20 kDa) and a small subunit (approximately 10 kDa) connected by an intersubunit linker region that undergoes proteolytic cleavage during enzyme maturation.[22][59] The active site of caspase-14, like all caspases, contains a critical catalytic dyad comprising a cysteine residue (Cys258 in human caspase-14) and a histidine residue that together form the core catalytic machinery.[15][56] This cysteine-histidine dyad is positioned within a substrate-binding pocket that contains several loops designated L1-L4 and L2' prime, which create a binding surface that determines both the specificity and kinetics of substrate recognition.[15][56] The five loops forming the active site region demonstrate varying degrees of conservation across mammalian caspases, with L1 and L3 being relatively conserved while L2 and L4 are highly divergent—a structural variation that directly contributes to differences in substrate specificity between caspase family members.[56]

A remarkable feature distinguishing caspase-14 from other caspases is its unusual mechanism of proteolytic activation and its exceptional requirement for specific environmental conditions to achieve catalytic activity. **In contrast to most caspases that undergo cleavage at conserved aspartic acid residues to separate the large and small subunits**, caspase-14 is cleaved at a non-canonical position between isoleucine 152 and lysine 153 in the human enzyme, suggesting processing by a trypsin-like serine protease rather than by another caspase.[18][22] This unique cleavage site location indicates that caspase-14 has diverged from the standard caspase activation mechanism, acquiring evolutionary specialization for a different proteolytic pathway adapted to its unique tissue context.[3][22] Furthermore, caspase-14 requires proteolytic cleavage within the catalytic domain followed by dimerization and the ordering of mobile active site loops to achieve catalytic competence, necessitating high concentrations of kosmotropic salts such as sodium citrate for enzymatic activity in vitro.[3][18] The requirement for kosmotropic salts—which induce partial desolvation of the protein to a more compact, catalytically active state—is believed to mirror the unique ionic and osmotic environment of the stratum corneum of the epidermis where caspase-14 physiologically functions.[32][45]

## Tissue-Specific Expression Pattern and Subcellular Localization

Caspase-14 expression exhibits an extraordinarily restricted tissue distribution compared to other caspase family members, being present almost exclusively in terminally differentiating epithelial tissues undergoing cornification. **The CASP14 gene is expressed primarily in suprabasal layers of the epidermis, particularly in the granular and cornified layers, as well as in hair follicles and sebaceous glands.[1][2][26][38]** The expression pattern is notably absent in non-cornifying epithelia such as the oral mucosa epithelium, sweat gland ducts, and nail matrix keratinocytes, demonstrating remarkable tissue specificity correlated with the cornification process.[19][26][38][44] In addition to cutaneous tissues, minor expression of caspase-14 has been detected in the murine esophagus, forestomach, and Hassall's bodies of the thymus gland, all tissues characterized by the presence of stratified cornifying epithelium, further supporting the association between caspase-14 expression and the cornification program.[18][44]

Within the epidermis, the spatial distribution of caspase-14 reveals important clues about its functional role in keratinocyte differentiation. **In the granular layer, the penultimate living layer of the epidermis, caspase-14 is associated with the nucleus, keratohyalin granules (the storage compartments for profilaggrin), and desmosomes (cell-cell adhesion structures).[38][44]** As keratinocytes transition from the granular layer into the stratum corneum—a process known as cornification—caspase-14 remains in the cytoplasm of the resulting corneocytes (dead, anucleate cells) where it remains connected to corneodesmosomes (modified desmosomal structures in cornified cells) and nuclear remnants.[38][44] The differential subcellular localization of caspase-14 between the granular layer and stratum corneum suggests distinct temporal phases of enzymatic activity and substrate engagement during the cornification process.[13][44]

Critically, **caspase-14 activation and expression begin during embryonic development synchronously with epidermal barrier formation**, representing an essential developmental program. Caspase-14 expression is initiated from embryonic day 14.5 or 15.5 in murine development, with proteolytic processing commencing from embryonic day 17.5, coinciding precisely with formation of the epidermal stratum corneum.[26][38][44][48] This developmental timing establishes caspase-14 as a component of the intrinsic genetic program governing skin barrier formation in utero, with the protease playing a critical role in generating the initial physical barrier that protects developing mammals from amniotic fluid.[38]

At the molecular level, the transcription of the CASP14 gene is upregulated during terminal differentiation of keratinocytes through transcription factor-mediated mechanisms. **Transcription factors specifically active during keratinocyte terminal differentiation are required to regulate CASP14 promoter activity**, and the promoter region contains at least two potential AP-1 (activator protein-1) binding sites that respond to differentiation signals.[32][45] Ceramides have been identified as stimulators of CASP14 upregulation, with sphingoid bases and ceramides increasing intracellular caspase-14 protein levels through pathways involving p38 and c-jun N-terminal protein kinase (JNK) signaling.[44] Additionally, vitamin D3 (1α,25-dihydroxycholecalciferol) promotes caspase-14 expression in a dose-dependent manner through active nuclear receptor signaling, whereas retinoic acid antagonizes this effect by suppressing caspase-14 expression, providing pharmacological mechanisms to modulate caspase-14 activity for therapeutic purposes.[49][52]

## Enzymatic Properties and Activation Mechanism

The activation of caspase-14 represents a fundamentally distinct mechanism compared to other caspase family members, involving multiple proteolytic steps catalyzed by different proteases and requiring specific environmental conditions for catalytic competence. **The primary protease responsible for cleaving human procaspase-14 between isoleucine 152 and lysine 153 remains unidentified, though evidence suggests involvement of a trypsin-like or elastase-like serine protease rather than another caspase family member.[18][22]** Notably, kallikrein-related peptidase-7 (KLK7), a serine protease abundant in terminally differentiated keratinocytes, has been implicated in the carboxy-terminal truncation of the large subunit of caspase-14, suggesting that KLK7 participates in post-translational modification of the caspase-14 enzyme following initial proteolytic activation.[20][22] The identification of KLK7 involvement represents an important advance in understanding the cascade of proteolytic events generating active caspase-14, as this establishes a multi-enzyme activation system whereby different proteases perform sequential modifications to progressively generate a fully active enzyme.

Following initial proteolytic cleavage at isoleucine 152/lysine 153, the processed caspase-14 requires additional modifications and conformational changes to achieve enzymatic activity. **Proteolytic cleavage in the catalytic domain is followed by dimerization of processed caspase-14, which is required for proteolytic activity, followed by high concentrations of kosmotropic salts such as sodium citrate to induce both dimerization stabilization and ordering of the mobile active site loops required for substrate binding and catalysis.[18][22][48]** The unique requirement for kosmotropic salts represents an extraordinary adaptation to the specific biochemical milieu of the stratum corneum, which is an exceptionally dehydrated tissue with low water content (15-25% at the skin surface compared to 45% at the transitional layer) and high ionic strength created by the accumulation of natural moisturizing factors.[45] This observation suggests that evolution has adapted caspase-14 to remain largely inactive in the aqueous, neutral pH environment of living keratinocytes but to become highly active in the desiccated, ionic environment of the stratum corneum where it performs its primary biological function.

A crucial distinction between caspase-14 and apoptotic caspases emerges when examining its response to classical apoptotic stimuli. **Although both human and mouse caspase-14 efficiently cleave the fluorescent peptide substrate WEHD-amc (a canonical caspase substrate), only mouse caspase-14 cleaves IETD-amc as efficiently as human caspase-14 cleaves WEHD-amc, revealing species-specific differences in substrate preference.[3][32]** These substrate preferences, determined through positional scanning substrate combinatorial library approaches, classify human caspase-14 as possessing an inflammatory caspase-like profile with preference for tryptophan or tyrosine in the S4 subsite, while mouse caspase-14 displays substrate preferences more similar to apoptotic initiator caspases with greater tolerance for β-branched and aromatic amino acids.[12][32] However, when differentiated keratinocytes expressing caspase-14 are treated with apoptotic stimuli such as TNF/CHX, UVB radiation, or staurosporine, caspase-14 remains unprocessed despite robust activation of caspase-3 and cleavage of caspase-3 substrates, demonstrating that caspase-14 is excluded from classical apoptotic signaling pathways even though it may theoretically possess substrate-recognizing capabilities compatible with some apoptotic substrates.[36]

## Substrate Specificity and Catalytic Function

The substrate specificity of caspase-14 has been systematically determined through biochemical approaches combining positional scanning peptide libraries with identification of physiological protein substrates cleaved within intact cells and tissues. **Human caspase-14 preferentially recognizes and cleaves substrates containing the consensus motif [WY]-X-X-D (where W or Y represents tryptophan or tyrosine, X represents any amino acid, and D represents aspartate, with cleavage occurring immediately after the aspartate residue as is characteristic of all caspases).[3][12][35]** The S4 specificity pocket of caspase-14 has evolved to preferentially accommodate bulky aromatic residues rather than the smaller, branched residues favored by apoptotic executioner caspases, creating a molecular sieve that channels the enzyme toward specific substrates in the cornifying keratinocyte environment.[3][12]

The primary physiological substrate of caspase-14 is **profilaggrin (also called filaggrin-1 or FLG), a large, insoluble protein consisting of a calcium-binding A domain, a B domain, and multiple tandem repeats of filaggrin functional units.**[8][10] Profilaggrin is synthesized in the granular layer of the epidermis and accumulates in keratohyalin granules, where it undergoes dephosphorylation and proteolytic processing into individual filaggrin molecules.[28][38] These filaggrin molecules then aggregate and stabilize keratin intermediate filaments, creating a mechanically robust keratin network that forms the structural foundation of corneocytes and the stratum corneum barrier.[10][28][38] **Caspase-14 has been demonstrated to directly cleave both profilaggrin and processed filaggrin molecules in vitro and in vivo, with identification of two specific caspase-14 cleavage sites within the filaggrin molecule.**[8][25] The cleavage of filaggrin by caspase-14 exposes cleavage sites accessible to other proteases, including endopeptidases and exopeptidases, facilitating the terminal proteolytic degradation of filaggrin into free hygroscopic amino acids and peptides that accumulate as natural moisturizing factors.[8][32]

The pathway of filaggrin degradation into natural moisturizing factors represents one of the most critical functions of caspase-14 in maintaining skin homeostasis. **Following initial cleavage by caspase-14, filaggrin fragments are further processed through deimination (conversion of arginine to citrulline by peptidylarginine deiminases) and subsequent enzymatic degradation into free amino acids including ornithine, citrulline, pyrrolidone carboxylic acid (PCA, derived from glutamine), urocanic acid (UCA), and other hygroscopic compounds collectively termed natural moisturizing factors (NMFs).**[8][25][43] These natural moisturizing factors accumulate in the stratum corneum where they function as osmolytes, drawing water into the tissue and maintaining epidermal hydration essential for preserving the mechanical and permeability barrier properties of the skin.[8][10][28] The critical importance of this pathway is evidenced by studies of caspase-14-deficient mice and human patients with CASP14 mutations, which show dramatic reductions in NMF content, particularly decreased urocanic acid and pyrrolidone carboxylic acid levels.[8][25][43]

Beyond filaggrin processing, caspase-14 has been demonstrated to cleave additional substrates involved in epidermal barrier function and denucleation. **Caspase-14 cleaves the inhibitor of caspase-activated DNase (ICAD, also known as DFF45 or CAD/DFF DNA-binding protein), liberating caspase-activated DNase (CAD) to enter keratinocyte nuclei and facilitate DNA fragmentation during cornification.**[7][19][33] This mechanism parallels that observed in classical apoptosis but is restricted to differentiated, cornifying keratinocytes where caspase-14 activity is concentrated, ensuring that this cell death pathway occurs only in the appropriate cellular context.[7][33] Additionally, **caspase-14 cleaves and activates mesotrypsin (also known as serine protease 3 or PRSS3)**, promoting the conversion of mesotrypsinogen to its active form through cleavage near an enterokinase recognition sequence.[21][24][33] Mesotrypsin subsequently activates saposin, a regulatory factor of the intercellular lipid-dependent permeability barrier of the epidermis, establishing a regulatory cascade wherein caspase-14 coordinates multiple enzymatic modifications essential for barrier formation.[21][24]

## Keratinocyte Terminal Differentiation and Cornification

The primary biological function of caspase-14 is **orchestrating the programmed cell death of keratinocytes known as cornification or corneoptosis, a unique developmental process distinct from apoptosis that generates the protective outer layer of skin**.[38][44][51] Cornification represents a highly coordinated developmental program wherein living keratinocytes located in the basal and spinous layers of the epidermis progressively migrate upward through the granular layer and finally differentiate into anucleate, mechanically resistant corneocytes that form the stratum corneum.[10][38][44] This process involves profound cellular reorganization including accumulation of structural proteins, cross-linking of proteins into a cornified envelope, selective proteolysis of structural proteins, and eventual extrusion of cellular organelles including the nucleus—a process fundamentally different from the fragmented nuclear morphology and cytoplasmic membrane blebbing characteristic of apoptosis.[28][38][44]

**Caspase-14 expression and activation coincide precisely with the formation of normal stratum corneum both during embryonic skin development and in organotypic skin cultures grown in vitro**, providing direct evidence that this protease is a component of the genetic program regulating terminal keratinocyte differentiation.[10][32][38] In embryonic development, caspase-14 processing begins around embryonic day 17.5 in mice, at the exact developmental stage when the epidermal barrier becomes functionally competent to protect the developing embryo from the aquatic environment of the amniotic sac.[38][44] When caspase-14-deficient mice are examined during early development, the timing of barrier formation is not significantly altered, suggesting that other proteases may partially compensate for caspase-14 loss, yet the defective stratum corneum composition documented in postnatal life suggests that caspase-14 becomes increasingly critical for maintaining barrier homeostasis after birth.[55]

The involvement of caspase-14 in denucleation—the process of nuclear degradation and removal during cornification—has emerged as a critical function coordinating with filaggrin degradation. **Multiple pathways are involved in DNA degradation during keratinocyte terminal differentiation, including both a caspase-14-mediated pathway that liberates caspase-activated DNase (CAD) through ICAD cleavage and a filaggrin N-terminal fragment-dependent pathway that independently promotes nuclear degradation.**[7][19][33] These pathways operate cooperatively and are interdependent—knockdown of both caspase-14 and mesotrypsin results in significant accumulation of remnant nuclei in the cornified layer of skin equivalent models.[7][19][33] Immunohistochemical analysis of human skin from patients with atopic dermatitis and psoriasis reveals that both caspase-14 and mesotrypsin are markedly downregulated in parakeratotic areas where nuclei persist abnormally in the stratum corneum, establishing a direct correlation between caspase-14/mesotrypsin expression and successful nuclear degradation during cornification.[7][19][33]

## Skin Barrier Formation and Protective Functions

Caspase-14 plays essential roles in maintaining the structural and functional integrity of the epidermal barrier, protecting mammals from excessive transepidermal water loss and environmental damage. **Targeted deletion of Casp14 in mice leads to an increase in transepidermal water loss (TEWL), incomplete processing of filaggrin, a decline in filaggrin breakdown products such as urocanic acid and pyrrolidone carboxylic acid, and substantially increased sensitivity to UVB-induced photodamage.**[8][25][39] Specifically, caspase-14-deficient epidermis demonstrates a highly characteristic phenotype including shiny, lichenified skin with altered stratum corneum composition, significantly more alveolar keratohyalin granules indicating abnormal filaggrin storage and processing, and markedly reduced skin hydration levels.[39] These animals display increased susceptibility to formation of cyclobutane pyrimidine dimers (CPDs) following UVB irradiation, leading to elevated levels of UVB-induced apoptosis in the epidermis and reduced capacity of the stratum corneum to act as a UV filter.[39]

The UV-protective function of caspase-14 likely operates through multiple mechanisms related to the correct composition and structure of the stratum corneum. **Removal of the stratum corneum from caspase-14-deficient mice indicates that caspase-14 controls the UVB-scavenging capacity of the stratum corneum specifically**, suggesting that the altered protein composition resulting from defective filaggrin processing changes the optical and UV-absorbing properties of the outer epidermal layers.[39] Urocanic acid, one of the major natural moisturizing factors generated from filaggrin through caspase-14 action, possesses UV-absorbing properties and may contribute directly to the photoprotective function of the stratum corneum.[25][39] The reduced levels of natural moisturizing factors in caspase-14-deficient skin also result in diminished epidermal hydration, which compromises the mechanical and permeability barrier properties essential for withstanding environmental stress.[8][25]

**Human patients carrying loss-of-function mutations in CASP14 develop autosomal recessive congenital ichthyosis 12 (ARCI12), characterized by non-erythematous fine whitish scales distributed over the body, defective cornification, and impaired skin barrier function.**[31][40][51] These patients entirely lack functional caspase-14 protein and exhibit clinical phenotypes largely consistent with observations in knockout mouse models, confirming that caspase-14 dysfunction results in specific barrier defects. Whole-exome sequencing has identified small deletions in CASP14 in ichthyosis patients, revealing that genetic variations affecting caspase-14 expression and function are associated with inherited disorders of cornification.[11][31]

## Additional Enzymatic Substrates and Biological Pathways

Beyond its well-characterized role in filaggrin processing and denucleation, caspase-14 participates in broader networks of proteolytic regulation within the cornifying keratinocyte. **Recent evidence suggests that caspase-14 may cleave additional substrates among cornification-associated proteins, with loricrin, involucrin, and keratins (K1, K10, K18) identified as potential targets based on structural analysis of caspase cleavage site recognition preferences and their involvement in cornification.**[58] However, definitive demonstration of direct caspase-14-mediated cleavage of these proteins requires isolation of natural cleavage products from stratum corneum tissue or in vitro cleavage assays with purified substrates—evidence that remains incomplete for most proposed substrates beyond filaggrin.

The discovery that caspase-14 activates mesotrypsin reveals an important regulatory relationship wherein caspase-14 controls the activity of a related serine protease with complementary functions in barrier formation. **Mesotrypsin (PRSS3) is processed from its inactive mesotrypsinogen precursor through activation by several proteases including cathepsin B, caspase-14, and enterokinase, with caspase-14 cleavage occurring near a DDDDKI enterokinase recognition sequence.**[21][24][33] Once activated, mesotrypsin generates profilaggrin N-terminal fragments that translocate into keratinocyte nuclei and promote DNA degradation through mechanisms distinct from CAD-mediated fragmentation.[21][24][33] This functional specialization wherein caspase-14 directly activates mesotrypsin and facilitates its access to profilaggrin substrates illustrates the sophisticated multi-enzyme coordination required to successfully execute the cornification program.

The remarkable finding that human and mouse caspase-14 possess different substrate preferences despite 80% identity in their catalytic domains suggests that even subtle evolutionary divergence in active site structure creates functionally distinct enzymes.[3][32] **Mouse caspase-14 shows broader substrate preferences similar to apoptotic initiator caspases, cleaving both IETD and WEHD peptide substrates with similar efficiency, whereas human caspase-14 preferentially cleaves WEHD-based substrates with much higher catalytic efficiency than IETD-based substrates.**[3][12][32] This divergence raises the intriguing possibility that human and mouse caspase-14 have evolved to process distinct physiological substrates optimized for the specific cornification strategies of their respective species, warranting careful interpretation of findings from mouse knockout models when extrapolating to human biology.

## Dysregulation in Disease States

The expression and activity of caspase-14 are significantly dysregulated in various skin disease states, suggesting that defects in the cornification program contribute to pathogenesis. **In psoriatic skin lesions, caspase-14 expression is dramatically decreased in parakeratotic regions (areas where nuclei persist abnormally in the stratum corneum), with parakeratotic areas showing very low levels of caspase-14 compared to normal stratum corneum.**[36][38][49][51] Topical treatment of psoriatic lesions with vitamin D3 analogues results in a decrease in psoriatic phenotype accompanied by an increase in caspase-14 expression, suggesting that restoring normal caspase-14 levels and activity may contribute to therapeutic benefit in psoriasis.[49][52] Similarly, **in atopic dermatitis, decreased CASP14 expression has been demonstrated to correlate with impaired skin barrier function**, indicating that reduced caspase-14 expression may contribute to the barrier defects characteristic of this common inflammatory disorder.[34][51]

These disease associations raise important therapeutic questions about whether caspase-14 can be manipulated as a therapeutic target to improve barrier function in chronic skin diseases. The finding that vitamin D3 promotes caspase-14 expression while retinoic acid antagonizes it provides pharmacological tools to experimentally modulate caspase-14 activity.[49][52] Additionally, the discovery that Chaenomeles sinensis (a medicinal fruit extract) and potentially other natural compounds can enhance caspase-14 expression through upregulation of kallikreins involved in caspase-14 maturation offers additional avenues for therapeutic intervention.[23] The clinical test demonstrating that skin treated to increase caspase-14 levels shows reduction of transepidermal water loss under UV stress conditions supports the concept that pharmacological enhancement of caspase-14 activity may provide therapeutic benefit in barrier-compromised skin conditions.[42]

Interestingly, high CASP14 expression has been documented in triple-negative breast cancer (TNBC), where it correlates with proliferation, a TNBC phenotype, and cancer stemness properties.[5][57][60] This finding represents a striking contrast to its role in promoting terminal differentiation and cell death in the epidermis, suggesting that caspase-14 may possess context-dependent functions in different cell types or that high expression in cancer may reflect expression of undifferentiated cell populations rather than functionally active enzyme.[5][57][60]

## Evolutionary Perspective and Comparative Genomics

The evolutionary trajectory of caspase-14 provides remarkable insights into the relationship between gene function, tissue architecture, and environmental adaptation across mammalian species. **Gene knockout studies, evolutionary genomic analysis, and the association of human CASP14 mutations with ichthyosis collectively indicate that caspase-14 is functionally associated with the barrier function of mammalian skin and the establishment of terrestrial life.**[27][37] Analysis of caspase-14 orthologs across diverse mammalian species reveals that this protease is conserved in most mammals, with caspase-14 present in monotremes (platypus and echidna), though with some species possessing multiple paralogs resulting from gene duplication events.[27]

The evolutionary loss of caspase-14 in cetaceans (whales and dolphins) represents a particularly illuminating case study in the relationship between gene function and environmental adaptation. **All cetaceans investigated—including bottlenose dolphin, harbour porpoise, and fin whale—have completely lost functional CASP14 genes, whereas their closest terrestrial relative, the hippopotamus, retains intact CASP14.**[27][37] This loss parallels alterations in epidermal structure in cetaceans, which display a dramatically thickened and incompletely cornified epidermis adapted to fully aquatic life, suggesting that the cornification processes dependent on caspase-14 are unnecessary or even disadvantageous in the aquatic environment.[27][37] Interestingly, **filaggrin (FLG) and caspase-14 have not strictly co-evolved during the evolution of cetaceans—filaggrin is conserved in dolphins but lost in whales, whereas caspase-14 is lost in all cetaceans, indicating that these proteins are not absolutely interdependent despite their functional association in terrestrial mammals.**[27][37]

Further evidence for divergent evolution of caspase-14 and filaggrin emerges from analysis of aquatic sirenians (manatees and dugongs). **The manatee has retained functional FLG and CASP14 genes, whereas the dugong contains premature stop codons in FLG and a pseudogenized CASP14 gene disrupted by frameshift mutations, representing convergent evolution of skin barrier gene loss in different lineages of aquatic mammals.**[40] These evolutionary patterns suggest that the land-to-water transition of aquatic mammals was associated with modifications of the epidermal barrier at the molecular level, with loss of the terrestrial cornification program genes becoming selectively advantageous when the thick, insulating skin barrier characteristic of terrestrial mammals is no longer necessary for survival in an aqueous environment.

## Evolutionary Conservation and Structural Specialization in Caspase-14-Like Proteases

Caspase-14 belongs to a subfamily of caspase-like proteases that share distinctive structural features and expression patterns. **In contrast to the prodomain-containing caspase-14, caspase-15 contains a prodomain predicted to assume a pyrin fold, and caspase-16 features a prodomain with unique sequence similarity to the catalytic domain, representing a diverse group of caspase-14-like proteases that have not been comprehensively discussed in previous reviews.**[27][59] These three caspases have evolved from a common ancestral caspase divergent from the CARD-containing pyroptotic caspases and the DED-containing initiator caspases, establishing a distinct evolutionary lineage specialized for tissue-specific proteolytic functions.[27]

The catalytic domain of caspase-14 is predicted to assume the characteristic caspase-hemoglobinase fold, an ancient protein fold conserved for at least 650 million years from which evolved all modern caspases.[30][56] **The folding landscape of caspase-14 was established early in caspase evolution and has been retained for over 650 million years, with partially folded monomeric or dimeric intermediates providing mechanisms for evolutionary changes affecting stability of extant caspases while retaining the overall caspase-hemoglobinase fold.**[30] Comparative structural studies reveal that different effector caspases demonstrate varying kinetic stability, with caspase-6 being most stable and caspase-7 least stable, with the folding landscape of caspase-7 being more similar to the ancestral caspase, consistent with phylogenetic data showing caspase-7 is closest to the common ancestor.[30]

## Specialized Features of Caspase-14 Activation and Regulation

Caspase-14 possesses several regulatory features that distinguish it from other caspases and ensure its activation occurs exclusively in the cornifying keratinocyte environment. The requirement for kosmotropic salts appears to provide a specificity mechanism ensuring that caspase-14 remains catalytically inactive in the aqueous environment of living keratinocytes but becomes highly active in the dehydrated, osmotically concentrated stratum corneum.[3][18][45] This "chemical compartmentalization" of enzyme activity represents an elegant regulatory strategy wherein the enzyme is expressed as a latent form in the granular layer but becomes progressively activated only as keratinocytes transition into the increasingly dehydrated stratum corneum environment.[45]

Kallikrein-related peptidase-7 (KLK7), a serine protease abundant in terminally differentiated keratinocytes and the stratum corneum, has been identified as a key regulator of caspase-14 maturation. **The regulation of procaspase-14 maturation during terminal differentiation is a unique two-step process involving KLK7 generating an intermediate form of caspase-14, with KLK7 being itself activated by cleavage of KLK5 (another kallikrein involved in cornification).**[20][22] This enzymatic cascade establishes a hierarchical activation system wherein upstream kallikreins sequentially activate downstream proteases including KLK7, which then facilitates caspase-14 maturation, creating a coordinated temporal progression of proteolytic activation events during cornification.[20][22]

## Specialized Role in Nuclear Degradation During Terminal Differentiation

The role of caspase-14 in nuclear degradation has emerged as increasingly important following discovery that caspase-14-deficient mice are prone to development of parakeratosis under conditions triggering epidermal hyperproliferation. **Caspase-14 deficiency predisposes mice to parakeratosis—the persistent presence of nuclei in the cornified layer—in the imiquimod-induced psoriasis-like model, suggesting that caspase-14 becomes increasingly critical for maintaining nuclear breakdown under inflammatory conditions.**[51] Although basic nuclear degradation was not initially observed to be impaired in caspase-14-deficient mice under normal homeostatic conditions, more recent findings reveal subtle defects in nuclear organization and persistence of nuclear DNA under inflammatory stress, indicating that caspase-14 plays a conditional role in ensuring complete nuclear removal during cornification.[7][33]

The ICAD/CAD system represents one clear mechanism through which caspase-14 facilitates nuclear DNA degradation. **Purified caspase-14 from human cornified cell extracts causes limited proteolysis of ICAD (the inhibitor of caspase-activated DNase), releasing degradation products of 32, 27, and 11 kDa that appear similar to those generated by caspase-3, followed by accumulation of caspase-activated DNase (CAD) in the nuclei of terminally differentiated keratinocytes.**[19][46] The ICAD-degrading activity of caspase-14 is observed only in the presence of kosmotropic salt, consistent with the requirement for high ionic strength for general caspase-14 enzymatic activity, and addition of the caspase inhibitor zVAD-fmk strongly suppresses ICAD degradation by caspase-14, confirming the specificity of this proteolytic activity.[19][46] However, the broader denucleation process appears to require both the caspase-14-dependent ICAD/CAD pathway and the filaggrin N-terminal fragment-dependent pathway, with knockdown studies demonstrating that inhibition of either pathway alone leaves some nuclei intact, but downregulation of both pathways results in widespread persistence of nuclei in the cornified layer.[19][33]

## Conclusion: Synthesis and Future Perspectives

Caspase-14 represents a remarkable example of how evolution has adapted protease enzymes to specialized cellular contexts, diverging fundamentally from the canonical apoptotic functions of related caspase family members to instead coordinate the unique form of programmed cell death termed cornification. **This protease is essential for proper keratinocyte terminal differentiation, executing a sophisticated multi-enzyme program that includes filaggrin processing to generate natural moisturizing factors, denucleation through dual ICAD-dependent and filaggrin-dependent pathways, and cross-protease communication to activate mesotrypsin and regulate saposin activation in the context of epidermal barrier formation.**[1][7][8][10][38] The tissue-restricted expression pattern, specialized activation mechanism requiring kosmotropic salt conditions, and unique proteolytic specificity profile demonstrate how evolution has optimized this enzyme for the specific chemical and physical environment of the stratum corneum while maintaining it catalytically dormant in the aqueous cytoplasmic environment of living keratinocytes.

The clinical relevance of caspase-14 dysfunction is clearly established through studies of human CASP14 mutations causing ichthyosis and observations of altered caspase-14 expression in common skin diseases including psoriasis and atopic dermatitis. Future therapeutic development targeting caspase-14 represents a promising avenue for improving skin barrier function in these chronic conditions, with vitamin D3 analogues, kallikrein-based activators, and natural compounds such as Chaenomeles sinensis extracts providing initial proof-of-concept that caspase-14 activity can be pharmacologically enhanced. Conversely, the expression of caspase-14 in triple-negative breast cancer raises important questions about potential non-canonical functions of this protease in cancer biology that warrant further investigation.

Remaining outstanding questions include identification of the primary protease responsible for the initial cleavage of procaspase-14 at the isoleucine 152/lysine 153 position, comprehensive mapping of all physiological caspase-14 substrates beyond filaggrin and ICAD, elucidation of the precise mechanisms through which altered filaggrin degradation compromises barrier function beyond reduced natural moisturizing factors, and the potential therapeutic manipulation of caspase-14 activity in chronic inflammatory skin diseases. The evolutionary loss of caspase-14 in cetaceans and sirenians suggests that cornification can be extensively remodeled or eliminated when environmental pressures select against terrestrial barrier proteins, but the retention of functional caspase-14 in the manatee and of filaggrin in dolphins indicates complex, context-dependent gene evolution in aquatic mammals that remains incompletely understood. As our understanding of caspase-14 biochemistry, cell biology, and evolutionary trajectory continues to advance, this unique protease will likely emerge as an increasingly important therapeutic target for improving skin barrier function and treating cornification-associated diseases.

## Citations

1. https://en.wikipedia.org/wiki/Caspase_14
2. https://www.bgee.org/gene/ENSG00000105141
3. https://pubs.acs.org/doi/abs/10.1021/bi0498048
4. https://www.ncbi.nlm.nih.gov/gene/23581
5. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=23581
6. https://pubmed.ncbi.nlm.nih.gov/15301553/
7. https://www.nature.com/articles/cddis2014145
8. https://pubmed.ncbi.nlm.nih.gov/21654840/
9. https://www.nature.com/articles/cdd201744
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC2234247/
11. https://www.medicaljournals.se/acta/content/html/10.2340/00015555-2510
12. https://pubmed.ncbi.nlm.nih.gov/15557211/
13. https://www.nature.com/articles/cdd200959
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC8886984/
15. https://journals.sagepub.com/doi/10.1369/jhc.4A6300.2004?icid=int.sj-full-text.similar-articles.4
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC2943529/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC12292325/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC4001300/
19. https://pubmed.ncbi.nlm.nih.gov/22825846/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC4106320/
21. https://www.scirp.org/journal/paperinformation?paperid=140090
22. https://www.nature.com/articles/s41598-024-63271-w
23. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0310464
24. https://dental.washington.edu/wp-content/media/ohs/Review-Derm-Sinica.pdf
25. https://pubmed.ncbi.nlm.nih.gov/15556625/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC8628267/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC5797567/
28. https://www.uniprot.org/uniprotkb/P31944/entry
29. https://www.nature.com/articles/4400785
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC4437054/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC8197544/
32. https://pubmed.ncbi.nlm.nih.gov/17515931/
33. https://www.nature.com/articles/s41598-024-60099-2
34. https://pubmed.ncbi.nlm.nih.gov/11121154/
35. https://pubmed.ncbi.nlm.nih.gov/22672275/
36. https://journals.sagepub.com/doi/10.1369/jhc.4A6300.2004
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC1618612/
38. https://pubmed.ncbi.nlm.nih.gov/15331408/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC11581258/
40. https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1360248/full
41. https://www.nature.com/articles/s41421-025-00791-3
42. https://pubmed.ncbi.nlm.nih.gov/28570747/
43. https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.a.20234
44. https://onlinelibrary.wiley.com/doi/abs/10.1002/jso.24705