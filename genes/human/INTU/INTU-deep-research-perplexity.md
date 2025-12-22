---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-11T22:51:43.521526'
end_time: '2025-12-11T22:53:58.097145'
duration_seconds: 134.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: INTU
  gene_symbol: INTU
  uniprot_accession: Q9ULD6
  protein_description: 'RecName: Full=Protein inturned; AltName: Full=Inturned planar
    cell polarity effector homolog; AltName: Full=PDZ domain-containing protein 6;'
  gene_info: Name=INTU; Synonyms=KIAA1284, PDZD6, PDZK6;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the inturned family. .
  protein_domains: CCZ1/INTU/HSP4_longin_1. (IPR043987); CCZ1/INTU/HSP4_longin_3.
    (IPR043989); CCZ1/INTU_longin_2. (IPR043988); INTU. (IPR039151); PDZ. (IPR001478)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 58
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9ULD6
- **Protein Description:** RecName: Full=Protein inturned; AltName: Full=Inturned planar cell polarity effector homolog; AltName: Full=PDZ domain-containing protein 6;
- **Gene Information:** Name=INTU; Synonyms=KIAA1284, PDZD6, PDZK6;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the inturned family. .
- **Key Domains:** CCZ1/INTU/HSP4_longin_1. (IPR043987); CCZ1/INTU/HSP4_longin_3. (IPR043989); CCZ1/INTU_longin_2. (IPR043988); INTU. (IPR039151); PDZ. (IPR001478)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "INTU" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'INTU' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **INTU** (gene ID: INTU, UniProt: Q9ULD6) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking me to write a comprehensive research report on the human gene INTU (UniProt: Q9ULD6). Let me verify the information they've provided:

- UniProt Accession: Q9ULD6
- Protein Description: Protein inturned, also called Inturned planar cell polarity effector homolog, PDZ domain-containing protein 6
- Gene Name: INTU
- Synonyms: KIAA1284, PDZD6, PDZK6
- Organism: Homo sapiens (Human)
- Key Domains: Multiple longin domains and PDZ domains

Now, let me review the search results to understand what's known about INTU:

From the sources provided:
1. INTU is identified as an inturned planar cell polarity protein [1, 2]
2. It plays a key role in ciliogenesis and embryonic development [4]
3. It regulates cilia formation by controlling the organization of the apical actin cytoskeleton [4]
4. It's involved in embryonic digit morphogenesis, roof of mouth development, and tongue morphogenesis [16]
5. It's a component of the CPLANE (ciliogenesis and planar polarity effectors) complex [19, 22]
6. It has phosphatidylinositol binding activity, particularly binding to PI(3)P [16, 19]
7. It interacts with FUZ and WDPCP to form the CPLANE complex [19, 22, 53]
8. It has longin domains that are important for its function [9, 32]
9. It's involved in hedgehog signaling through its role in ciliogenesis [8, 10]
10. Mutations in INTU are associated with orofaciodigital syndrome XVII and short-rib thoracic dysplasia [34, 57]


11. It's involved in hair follicle differentiation through its role in primary cilia formation [8]
12. It's a GEF for Rab23, which is involved in basal body docking [43, 46]
13. It recruits IFT-A proteins to basal bodies [20, 49]
14. It localizes to the basal body and ciliary base [7, 16]

The literature confirms this is the correct gene. I should structure a comprehensive report covering INTU's function in ciliogenesis and planar cell polarity, its domain architecture, subcellular localization at the basal body, its role as a Rab23 GEF, and its involvement in developmental pathways including hedgehog signaling and morphogenesis. I'll also need to address the clinical significance of INTU mutations in ciliopathies and skeletal dysplasias, aiming for at least 10,000 words.
</think>

# The INTU Protein: A Critical Regulator of Ciliogenesis and Planar Cell Polarity

The inturned planar cell polarity protein, encoded by the human INTU gene (UniProt accession Q9ULD6), emerges as a multifunctional molecular regulator essential for primary cilium assembly, embryonic development, and the establishment of cellular polarity. This protein functions as a core component of the **ciliogenesis and planar polarity effectors (CPLANE) complex**, where it orchestrates the recruitment and organization of the intraflagellar transport machinery at the basal body while simultaneously regulating actin cytoskeletal dynamics critical for proper ciliary biogenesis and epithelial morphogenesis. Understanding INTU's diverse functions requires examination of its structural architecture, its role within the CPLANE complex, its integration into multiple signaling pathways including Hedgehog signaling, and its essential contributions to human development and tissue homeostasis.

## Structural Organization and Molecular Architecture of INTU

### Domain Architecture and Protein Composition

The INTU protein possesses a sophisticated structural organization defined by multiple functional domains that determine its biochemical properties and protein-protein interactions[1][2]. The protein contains several longin domains, which represent a conserved structural module first identified in SNARE proteins and subsequently recognized in vesicular trafficking regulators[32]. Specifically, INTU harbors three distinct longin domain repeats designated as the CCZ1/INTU/HSP4_longin_1, CCZ1/INTU_longin_2, and CCZ1/INTU/HSP4_longin_3 domains according to InterPro annotations[9]. These longin domains are flanked by additional structural elements that together create a modular architecture capable of mediating multiple protein-protein interactions. The presence of these conserved longin domains places INTU within a family of proteins known to regulate vesicular trafficking and membrane dynamics, though INTU's specific roles have evolved to encompass distinct functions in ciliogenesis.

Beyond its longin domains, INTU contains a PDZ domain, which represents a protein-protein interaction module consisting of approximately 80-90 amino acids that typically recognize and bind to short peptide sequences at the C-termini of target proteins[9]. However, the functional significance of this PDZ domain in INTU's ciliogenic role remains incompletely characterized compared to its roles in other PDZ-containing proteins. The protein's total molecular weight is approximately 110 kDa, rendering it a substantial regulatory hub capable of organizing multiple interaction partners simultaneously. This modular architecture enables INTU to function as a multi-valent scaffolding protein that can engage with numerous binding partners in a spatially and temporally coordinated manner.

### Protein Folding and Conformational States

Recent cryo-electron microscopy structural studies have illuminated the three-dimensional organization of INTU within the CPLANE complex[19][37]. These studies reveal that INTU adopts an extended conformation when bound within the CPLANE assembly, with its longin domains arrayed in specific orientations relative to other CPLANE subunits. The structural data indicate that INTU forms extensive interfaces with both Fuzzy (Fuz) and Wdpcp proteins, with particular emphasis on charge complementarity and shape matching at these interaction surfaces. Specifically, INTU contains negatively charged patches that interact with positively charged regions on Wdpcp, creating an electrostatically favorable interface that contributes substantially to complex stability[19]. This charge-based interaction scheme suggests that electrostatic complementarity serves as a primary organizing principle for CPLANE assembly.

The Intu-Fuz heterodimer represents a structurally defined subunit within the CPLANE complex that functions as a hexavalent-longin domain unit capable of engaging multiple downstream targets[43][46]. This dimeric pairing creates a functional unit with enhanced binding avidity compared to isolated subunits, enabling effective recruitment and activation of downstream effectors such as the small GTPase Rsg1. The cooperative binding properties of the Intu-Fuz heterodimer underscore how structural organization translates into enhanced biochemical function within larger protein assemblies.

## The CPLANE Complex: Assembly, Organization, and Function

### Composition and Hierarchical Assembly

The CPLANE complex represents a discrete, multi-subunit protein assembly composed of at least five protein components: INTU, Fuzzy (FUZ), Wdpcp (WDPCP), Jbts17 (JBTS17), and the small GTPase Rsg1 (CPLANE2)[19][22][49][53]. This complex exhibits hierarchical assembly properties, with evidence suggesting that different components are recruited to basal bodies in a sequential manner[22][49]. Recent structural and proteomic studies demonstrate that the CPLANE complex adopts a crescent-like or linear architecture with a subunit organization represented schematically as Wdpcp-Intu-Fuz-Rsg1[19][37][53]. Within this linear arrangement, INTU occupies a central position, mediating interactions between the peripheral Wdpcp protein and the downstream Fuz-Rsg1 module.

The CPLANE complex localizes predominantly to the basal body and the pericentriolar material surrounding the mother centriole, positioning it at the precise anatomical site where ciliogenesis is initiated[19][49][50]. This spatial localization proves critical, as INTU's function depends fundamentally on its recruitment to the basal body where it can engage with substrate proteins and participate in organizing the ciliary base. The stability and assembly of the CPLANE complex at the basal body is achieved through multivalent protein-protein interactions, with INTU serving as a critical organizational hub that maintains complex integrity through its extensive binding surfaces.

### INTU's Role in Guanine Nucleotide Exchange Factor Activity

A defining biochemical function of INTU, operating in concert with Fuzzy, involves its capacity to function as a guanine nucleotide exchange factor (GEF) for the small GTPase Rab23[43][46]. The Intu-Fuz heterodimer catalyzes the exchange of GDP for GTP on Rab23, thereby converting this small GTPase from its inactive GDP-bound state to its active GTP-bound form. This GEF activity depends critically on the structural organization of the Intu-Fuz complex, with the longin domains providing the essential binding surfaces for Rab23 engagement[43]. The catalytic mechanism involves reorientation of Rab23's nucleotide-binding pocket through INTU-Fuz-mediated conformational changes that facilitate nucleotide release and subsequent GTP binding.

Notably, emerging evidence suggests that INTU may function not solely as a GEF but potentially as an effector protein for the atypical GTPase Rsg1[37][50]. The interaction between INTU and Rsg1 appears to be GTP-dependent, with cryo-EM structural analysis revealing that Rsg1 binds to the INTU-Fuz complex in a manner characteristic of GTPase effector proteins rather than substrates[50]. This dual functionality—catalyzing nucleotide exchange on Rab23 while simultaneously serving as an effector of Rsg1—enables INTU to coordinate multiple signaling cascades essential for ciliogenesis.

## Phospholipid Binding and Membrane Recruitment

### Phosphatidylinositol 3-Phosphate Binding

A critical biochemical property of INTU involves its capacity to bind phosphatidylinositol phosphates with marked specificity for phosphatidylinositol 3-phosphate [PI(3)P][16][19]. Quantitative binding studies demonstrate that INTU displays highest affinity for PI(3)P, followed by lower affinity binding to phosphatidylinositol 4-phosphate and phosphatidylinositol 5-phosphate[16][19]. The N-terminal region of INTU, encompassing approximately the first 300 amino acids including the longin domains, contains the primary PI(3)P binding determinants[19]. This lipid-binding capability positions INTU as a lipid-binding adaptor capable of coupling membrane phospholipid signals to downstream effector recruitment.

The functional significance of INTU's PI(3)P binding capacity relates to the spatial organization of ciliogenesis. Phosphatidylinositol 3-phosphate accumulates predominantly at endosomal membranes and serves as a membrane landmark recognized by proteins containing PI(3)P-binding modules[24]. The presence of functional PI(3)P-binding capacity in INTU suggests that this protein may couple ciliary precursor trafficking through the endosomal system to their eventual recruitment to the basal body. This lipid-mediated recruitment mechanism provides a molecular explanation for how INTU-containing protein complexes become enriched at specific membrane compartments during ciliogenesis. Furthermore, ciliopathy-associated mutations that disrupt INTU's PI(3)P binding capacity impair both this lipid binding function and downstream recruitment of IFT-A proteins to basal bodies, demonstrating the functional importance of this interaction[19].

## Primary Ciliogenesis: INTU's Central Role

### The Multi-Step Process of Primary Cilium Assembly

Primary cilium biogenesis represents an intricate developmental process involving the sequential recruitment and organization of numerous protein components at the basal body[7][10][25]. INTU functions as a critical regulator at multiple stages of this process, from initial basal body positioning to mature ciliary axoneme extension. The formation of a primary cilium typically initiates when cells exit the cell cycle and enter G0 phase, whereupon the mother centriole undergoes a series of molecular modifications that render it competent to nucleate a ciliary microtubule axoneme[7][10].

The process of primary ciliogenesis can occur through two distinct cellular routes: an intracellular pathway observed in fibroblasts and other cell types, and an extracellular pathway characteristic of polarized epithelial cells in tissues such as the kidney[7]. In the intracellular pathway, the centrosome remains largely internal to the cell, with cilia emerging directly from this intracellular organelle. Conversely, in the extracellular pathway, the basal body must dock at the apical plasma membrane, a process requiring substantial cytoskeletal remodeling and spatial repositioning of the centrosome. INTU participates in both pathways, though its role proves particularly critical in the extracellular pathway where basal body docking requires precise spatial coordination.

### INTU and Actin Cytoskeletal Regulation

A key mechanism through which INTU promotes ciliogenesis involves its regulation of the apical actin cytoskeleton, the meshwork of actin filaments that underlies the apical epithelial cell surface[4][25][28]. The positioning and docking of basal bodies at the apical plasma membrane requires localized clearance of cortical actin filaments, creating a membrane domain permissive for basal body anchoring[25]. INTU promotes this actin remodeling through multiple mechanisms, including its interaction with the RhoA GTPase pathway. Specifically, evidence indicates that the CPLANE protein Fuzzy, which functions as an INTU binding partner, recruits the Rho GAP protein p190A to the basal body, where p190A antagonizes excessive actin polymerization by inactivating RhoA[23].

The actin-based movement and positioning of basal bodies prior to their apical docking constitutes another INTU-regulated process[25][28]. The centrosome undergoes migration from its initial position near the nucleus toward the apical cell surface through mechanisms involving both actin-myosin contractility and microtubule dynamics. INTU appears to coordinate these movements by facilitating the assembly of contractile actomyosin networks at appropriate cellular locations. When INTU function is disrupted, basal body migration is impaired and basal bodies fail to achieve their proper apical positioning, thereby precluding cilium formation. The importance of INTU-mediated actin regulation is underscored by studies in diverse cell types demonstrating that disruption of INTU leads to decreased ciliary length and reduced numbers of ciliated cells.

### Recruitment and Engagement of Intraflagellar Transport Machinery

The intraflagellar transport (IFT) system represents the primary molecular motor system responsible for transporting ciliary proteins and organizing ciliary structure[7][10][45][54]. The IFT complex comprises two major subcomplexes, IFT-A and IFT-B, each composed of multiple protein subunits organized into a functional assembly. INTU plays a critical role in recruiting the IFT-A complex to the basal body, a step essential for subsequent ciliary assembly. Specifically, knockdown or mutation of INTU leads to dramatic reduction in the localization of IFT-A subunits including Ift43, Ift139, and Ift121 to the basal body, preventing proper assembly of the ciliary axoneme[19][49][50].

This INTU-mediated IFT-A recruitment function depends critically on INTU's interactions with other CPLANE components and on its GTP-dependent association with Rsg1[49][50]. Proteomic studies employing affinity purification coupled to mass spectrometry have defined the INTU interactome at basal bodies, revealing that GTP-loaded Rsg1 associates strongly with all CPLANE subunits including INTU, while GDP-locked Rsg1 displays essentially no CPLANE association[50]. This GTP-dependent interaction mechanism suggests that nucleotide loading of Rsg1 represents a regulatory checkpoint controlling CPLANE function. The recruitment of IFT-A proteins by the CPLANE complex positions these motor-associated proteins at the basal body where they become incorporated into anterograde IFT trains that transport ciliary precursors along the microtubule axoneme toward the ciliary tip.

## Localization Within Cells and Subcellular Compartments

### Basal Body and Centriolar Localization

INTU localizes predominantly to the basal body and the pericentriolar material, the protein-rich zone immediately surrounding the centriole pair that comprises the centrosome[4][16]. This basal body localization proves essential for INTU's ciliogenic function, as disruption of basal body targeting impairs the ability of INTU to promote ciliary assembly. The mechanisms governing INTU recruitment to basal bodies remain incompletely elucidated but likely involve both direct interactions with basal body-localized proteins and indirect recruitment through CPLANE complex assembly. Within the basal body, INTU accumulates at distal end of the mother centriole, positioning it optimally for engaging with ciliary precursor recruitment machinery.

During the cell cycle, INTU localization shows dynamic redistribution. In cycling cells where ciliogenesis is suppressed, INTU levels are relatively low and its localization to basal bodies is correspondingly reduced. Conversely, when cells undergo G0/G1 transition and enter the quiescent state permissive for ciliogenesis, INTU levels increase and its basal body localization becomes prominent. This cell-cycle dependent regulation of INTU abundance and localization represents an important control point ensuring that ciliogenesis occurs exclusively in non-dividing cells.

### Subcellular Compartment Associations

Beyond its predominant basal body localization, INTU exhibits localization to additional cellular compartments including the cytosol, cytoskeleton, mitochondrion, nucleus, and plasma membrane according to computational subcellular localization predictions[16]. While the functional significance of these non-basal body localizations remains somewhat unclear, they may reflect INTU's participation in cellular processes beyond ciliogenesis or may represent trafficking intermediates en route to the basal body. The presence of predicted nuclear localization signals within the INTU sequence raises the possibility of INTU involvement in transcriptional regulation, though such nuclear functions remain largely unexplored.

The dynamic localization of INTU to different cellular compartments likely reflects its status as a multi-functional protein engaged in distinct cellular processes depending on cellular context. In ciliated epithelial cells, INTU concentrates at basal bodies and primarily functions in ciliogenesis. In non-ciliated cell types or in cells of specific lineages, INTU may be redirected to alternative cellular sites where it participates in other developmental or homeostatic processes.

## INTU in Hedgehog Signaling Pathways

### The Primary Cilium as a Hedgehog Signaling Hub

Primary cilia function as central organizing centers for hedgehog signal transduction, with ciliary membrane serving as the primary locale where hedgehog pathway components accumulate and signal transduction occurs[10][14]. The patched (Ptch) receptor and smoothened (Smo) co-receptor localize to the ciliary membrane where they mediate hedgehog ligand sensing and signal transmission. The transcription factor Gli, the central effector of hedgehog signaling, localizes to the cilium where its subcellular positioning determines pathway output[10][14]. INTU promotes hedgehog signaling indirectly through its essential role in primary cilium formation and maintenance.

Cells lacking functional INTU fail to assemble normal primary cilia, leading to profound defects in hedgehog signaling capacity[8][10]. This cilia-dependent regulation of hedgehog signaling explains many of the developmental abnormalities observed in INTU-deficient organisms, as hedgehog signaling plays absolutely essential roles in embryonic patterning, tissue growth, and cell fate determination. In particular, hedgehog signaling through Gli transcription factors controls proliferation and differentiation of numerous cell types during development, and disruption of this pathway through INTU loss leads to severe patterning defects.

### INTU's Regulatory Role in Hair Follicle Development

An illustrative example of INTU's indirect but critical role in hedgehog signaling manifests in hair follicle development[8]. During hair follicle morphogenesis, follicular epithelial cells must receive and respond appropriately to hedgehog ligands secreted by neighboring dermal papilla cells. INTU deletion specifically in follicular keratinocytes results in severe hair follicle differentiation defects without affecting the baseline organization or polarity of follicular cells, indicating that INTU's primary function in this context relates to cilia-dependent hedgehog signaling rather than to basal PCP pathway functions[8]. The hedgehog signaling defects resulting from INTU loss prevent the normal developmental progression from epithelial progenitor cells to mature, hair-producing follicular structures.

This follicle-specific phenotype contrasts with the minimal effects of INTU deletion on interfollicular epidermal differentiation, a finding that highlights the context-dependent and tissue-specific effects of INTU loss[8]. While hedgehog signaling occurs in both follicular and interfollicular epithelial compartments, INTU appears to play a rate-limiting role specifically in follicular contexts, suggesting that alternative pathways for hedgehog signaling or cilia-independent developmental processes may partially compensate for INTU loss in interfollicular epidermis.

## INTU and Planar Cell Polarity Signaling

### Distinction Between Core PCP and PCP Effector Functions

The planar cell polarity pathway encompasses two distinct molecular layers: the core PCP signaling machinery and tissue-specific PCP effectors[8][11][55]. The core PCP components including Frizzled, Vang/Strabismus, Disheveled, and Prickle establish and propagate cell polarity signals across epithelial tissues through asymmetric intercellular protein localization and non-canonical Wnt pathway activation[11][55]. INTU functions not as a core PCP component but rather as a tissue-specific PCP effector that translates core PCP signals into specific developmental outcomes[8]. This distinction proves important, as it explains why INTU mutations lead to tissue-specific developmental abnormalities rather than the broad polarity defects characteristic of core PCP gene mutations.

As a PCP effector functioning downstream of core PCP components, INTU receives polarity information encoded by the asymmetric distribution of core PCP proteins and converts this information into biological outputs specific to particular cell types and developmental contexts[8]. In follicular keratinocytes, INTU's primary output involves promoting ciliogenesis and thereby enabling hedgehog signaling, whereas in other cell types INTU's downstream functions may involve different processes entirely. This context-dependent functionality of INTU exemplifies how tissue-specific effectors translate universal polarity signals into tissue-appropriate developmental programs.

### INTU-Dependent PCP Signaling in Neural Tube Closure

The PCP signaling pathway plays essential roles during convergent extension movements that narrow and elongate the embryonic body axis during gastrulation and neurulation[27][30][55]. These convergent extension movements position cells in specific mediolateral orientations, facilitating coordinated cell intercalation and body axis elongation. INTU contributes to these processes through coordinated regulation of actin cytoskeleton organization and cell migration. Disruption of INTU leads to defective convergent extension movements and failure of the neural tube to close properly, resulting in neural tube defects such as spina bifida.

The PCP-dependent regulation of convergent extension by INTU involves RhoA-mediated actin remodeling downstream of the core PCP proteins[55]. The signaling cascade proceeds from asymmetrically localized core PCP components through Rho family GTPases to actin reorganization and consequent changes in cell shape and migratory behavior. INTU promotes actin organization changes necessary for proper convergent extension through mechanisms involving both direct regulation of Rho GTPase signaling and through its effects on ciliogenesis and cilia-dependent signaling processes.

## Embryonic Development and Morphogenesis

### Critical Roles in Digit, Orofacial, and Palatal Development

INTU serves essential functions during the morphogenesis of multiple embryonic structures, with particularly important roles in digit formation, development of the palate, and orofacial structure formation[16][34][57]. During digit morphogenesis, INTU regulates the growth, segmentation, and patterning of the developing digit primordia through its effects on cell proliferation and differentiation. Loss of INTU function leads to polydactyly (increased digit number), syndactyly (digit fusion), and brachydactyly (shortened digits), reflecting disrupted signaling pathways essential for normal digit patterning.

Palatal and orofacial development similarly depends on INTU-mediated signaling. During palatal shelf fusion, epithelial cells must undergo differentiation, establish proper tissue interactions, and coordinate movement of palatal shelves toward the midline. Defects in INTU function impair these processes, leading to cleft palate and other orofacial abnormalities. The tongue represents another anatomically derived structure dependent on proper INTU function, with INTU mutations causing tongue nodules, aberrant tongue development, and abnormal oral mucosa differentiation.

These developmental abnormalities in multiple non-ciliated tissues highlight that INTU participates in developmental processes extending beyond those involving primary cilia. While INTU's ciliogenic and hedgehog signaling functions likely contribute to some aspects of these developmental processes, additional cilia-independent functions of INTU likely also contribute. For example, INTU's effects on actin cytoskeleton organization and cell polarity may prove critical for epithelial morphogenesis regardless of whether cilia are present in particular cell types.

### Lung Development and Branching Morphogenesis

The lung undergoes branching morphogenesis during embryonic development, a process involving repeated division of the respiratory epithelium into progressively finer branches. This branching process depends critically on coordinated signaling between the respiratory epithelium and underlying mesenchyme, with participation from multiple signaling pathways including hedgehog, FGF, and Wnt signaling. INTU participates in lung branching morphogenesis through multiple mechanisms, including its role in hedgehog signaling and its effects on epithelial cell polarity and actin organization.

Disruption of INTU in respiratory epithelial cells leads to defective lung branching and reduced number of alveolar structures, ultimately resulting in respiratory insufficiency in severely affected individuals. The specific mechanisms through which INTU promotes lung branching remain incompletely characterized but likely involve both cilia-dependent regulation of hedgehog signaling and cilia-independent effects on epithelial cell organization.

## Clinical Significance and Human Disease Associations

### Orofaciodigital Syndrome Type XVII and Related Ciliopathies

Mutations in the INTU gene cause orofaciodigital syndrome type XVII (OFDS XVII), a skeletal ciliopathy characterized by a distinctive constellation of developmental abnormalities[34][57]. OFDS XVII presents with developmental delay, distinctive facial dysmorphism including a high-arched palate, tongue nodules and aberrant oral mucosa, skeletal abnormalities including polydactyly and syndactyly, short ribs, cardiac defects, brain malformations, and urinary tract abnormalities[34][57]. Affected individuals display typical features of skeletal ciliopathies, reflecting the widespread dependence of skeletal development on cilium-dependent signaling, particularly hedgehog signaling.

The clinical spectrum associated with INTU mutations encompasses both more severe presentations resembling short-rib thoracic dysplasia with polydactyly (SRTD20) and milder phenotypes with predominantly orofacial and digit involvement[34][57]. This phenotypic variability likely reflects differences in the severity of specific INTU mutations, with some mutations producing complete loss of function while others result in hypomorphic alleles producing residual INTU activity. Compound heterozygous mutations and homozygous mutations have both been documented in affected families.

### Pathogenic Variants and Functional Classification

INTU pathogenic variants associated with human disease include both truncating mutations producing premature stop codons and missense mutations affecting protein domains or protein-protein interaction surfaces[34][50][57]. Truncating mutations uniformly result in severe phenotypes, likely reflecting complete loss of INTU function. Missense mutations show more variable phenotypic consequences, with some missense changes causing severe disease while others result in milder phenotypes. Variants affecting the GTP-binding region of associated Rsg1, or variants that disrupt INTU's interaction interfaces with other CPLANE components, show particularly strong associations with severe disease.

One clinically significant INTU-associated mutation involves substitution of arginine at position 188 in human INTU (corresponding to aspartic acid at position 184 in Xenopus INTU), which disrupts basal body recruitment of the IFT-A2 subunit Ift43 and impairs basal body docking in experimental systems[50]. Multiple different INTU mutations have been documented in small patient cohorts, with the genetic variants identified to date predominantly occurring in families of South Asian or Middle Eastern descent, though this likely reflects publication bias rather than true geographic specificity.

### Bardet-Biedl Syndrome and Broader Ciliopathy Context

While INTU mutations specifically cause OFDS XVII and SRTD20, broader ciliopathy disorders including Bardet-Biedl syndrome (BBS) may involve secondary dysregulation of INTU function through disruption of upstream ciliary assembly pathways[29][53]. BBS, a complex pleiotropic disorder affecting multiple organ systems including kidney, retina, and skeletal system, often results from mutations in genes encoding IFT proteins or other ciliogenesis regulators. Since INTU functions downstream of and is dependent upon proper IFT complex assembly and basal body organization, disruption of these upstream processes secondarily impairs INTU function and can contribute to BBS pathogenesis.

This hierarchical organization of INTU's function within the broader ciliogenesis machinery indicates that therapeutic strategies aimed at improving INTU function must account for the status of upstream ciliogenesis regulators. Conversely, therapeutic interventions improving upstream IFT or basal body organization may incidentally improve INTU function and enhance ciliogenesis efficiency.

## Integration into Multiple Signaling Pathways

### Wnt Signaling and Ciliary Regulation

The interplay between primary cilia and Wnt signaling represents a critical regulatory node in vertebrate development and tissue homeostasis[10][11][14]. Primary cilia regulate both canonical (β-catenin-dependent) and non-canonical (PCP) Wnt signaling through multiple mechanisms, with ciliary localization of Wnt pathway components providing a spatial organizing principle. INTU participates in this cilia-Wnt signaling integration through its essential role in ciliary assembly. By promoting primary cilium formation, INTU enables cilia-dependent Wnt signaling, including regulation of the Hippo pathway which controls organ size and tissue growth.

Inactivation of INTU leads to loss or severe shortening of primary cilia, which in turn disrupts cilium-dependent Wnt signaling. This impairment of cilium-dependent Wnt signaling contributes substantially to the developmental abnormalities observed in INTU-deficient organisms, as Wnt signaling controls critical developmental processes including mesenchyme-epithelium interactions, cell proliferation, and tissue patterning.

### Hippo Pathway and Organ Size Control

The Hippo pathway functions as a critical regulator of organ size and tissue growth, with its activity substantially modulated by primary ciliary signaling[10][14]. The transcriptional co-activator YAP, a central Hippo pathway effector, undergoes phosphorylation and nuclear exclusion in cells with functional primary cilia, thereby suppressing YAP-dependent transcription and limiting organ growth. INTU promotes this Hippo pathway inhibition indirectly through its effects on primary cilium assembly, thereby serving as an important regulator of organ size.

This INTU-mediated regulation of the Hippo pathway explains why INTU-deficient organisms develop kidney cysts and why INTU mutations feature prominently among ciliopathy-associated genes. The loss of cilium-mediated Hippo pathway inhibition in INTU-deficient cells leads to excessive YAP activation, promoting inappropriate cell proliferation and cyst formation in organs such as the kidney where tissue size homeostasis depends critically on cilium-mediated Hippo signaling.

### Notch Signaling and Cell Fate Determination

Notch signaling, a primary cell fate determinant in epithelial tissues including epidermis, also integrates with ciliary signaling in complex ways[56][59]. Primary cilia may compartmentalize Notch signaling components or regulate their activation status through cilium-dependent mechanisms. INTU's role in promoting cilium assembly thereby influences Notch signaling-dependent cell fate decisions. In specific tissue contexts, such as hair follicle development, INTU's effects on cell fate may reflect both direct PCP pathway functions and indirect effects through cilium-dependent regulation of Notch signaling.

## Regulatory Mechanisms and Protein-Protein Interactions

### Interactions with Core CPLANE Complex Members

INTU engages in extensive protein-protein interactions with other CPLANE complex components, with these interactions proving essential for INTU's biological function[19][37][49][50]. The INTU-Fuzzy heterodimer represents a particularly important functional unit, with structural studies revealing that Intu and Fuz form complementary binding surfaces that stabilize each other within the complex. The interaction between INTU and Wdpcp involves both direct contacts between the INTU longin domains and the Wdpcp beta-propeller structure, and indirect interactions mediated by their common interactions with Fuzzy[19][37].

Critically, INTU's interaction with Rsg1 proves GTP-dependent, with GDP-locked Rsg1 showing essentially no binding to INTU or other CPLANE components[50]. This GTP-dependence suggests that Rsg1 nucleotide loading serves as a critical control point determining CPLANE complex assembly at the basal body. The GTP-dependent recruitment of INTU to basal bodies through Rsg1 interaction provides a molecular switch enabling regulated, signal-responsive CPLANE function rather than constitutive ciliary assembly machinery activity.

### Interactions with IFT-A Complex and Basal Body Proteins

Beyond CPLANE complex interactions, INTU engages directly or indirectly with multiple IFT-A complex subunits, facilitating recruitment of the IFT-A complex to basal bodies[19][20][49][50]. Proteomic studies combining immunoprecipitation with mass spectrometry have identified interactions between INTU and core IFT-A subunits including Ift139, Ift121, Ift122, Ift143, and Ift144[19]. These interactions likely occur both through direct engagement of INTU with IFT-A proteins and through bridging interactions provided by intermediate proteins. The recruitment of IFT-A to basal bodies by the CPLANE complex represents a critical regulatory step controlling the spatial and temporal assembly of ciliary IFT machinery.

INTU also interacts with basal body-associated proteins including transition zone proteins such as Fam92a, Cby1, and Dzip1[22][50]. These transition zone proteins establish the ciliary gate and regulate which proteins can enter the cilium, creating a diffusion barrier between the ciliary and cytoplasmic compartments. INTU's interactions with transition zone proteins suggest that CPLANE function may extend beyond its recognized roles in IFT recruitment to potentially include regulation of ciliary gate organization and ciliary protein selectivity.

### Post-Translational Modifications and Regulation

The regulation of INTU function through post-translational modifications remains largely unexplored, though several modalities seem probable. Phosphorylation of INTU by basal body-associated kinases may regulate its subcellular localization, protein-protein interactions, or biochemical activities. Aurora kinase A, which localizes to the basal body and plays critical roles in controlling ciliogenesis timing, represents a candidate INTU kinase, though this has not been formally demonstrated[10]. Similarly, ubiquitination of INTU may regulate its protein stability or subcellular localization in response to cellular signals.

Cell-cycle dependent degradation of INTU and other ciliogenesis-promoting proteins ensures that primary cilium assembly occurs exclusively in non-dividing cells. The mechanisms mediating this cell-cycle controlled INTU abundance likely involve proteasomal degradation directed by cell-cycle regulated E3 ligases, though the specific ubiquitin ligases remain to be identified. Understanding these regulatory mechanisms proves essential for comprehending how cells coordinate ciliary assembly with cell cycle progression.

## Comparative and Evolutionary Perspectives

### Conservation Across Metazoan Species

The INTU protein displays substantial sequence and functional conservation across diverse metazoan organisms, from simple invertebrates through to mammals[8][11]. This evolutionary conservation underscores the ancient origins and fundamental importance of INTU's ciliogenic functions. Homologous proteins in *Drosophila* (*inturned*), *Caenorhabditis elegans*, *Xenopus*, and zebrafish all participate in ciliary assembly and planar cell polarity signaling, though the specific developmental contexts where these functions prove critical vary among species.

In organisms lacking motile cilia, such as *Drosophila*, inturned's functions have evolved toward primarily regulating PCP signaling and actin cytoskeletal dynamics, reflecting the divergent roles of PCP signaling in invertebrate development[11]. Conversely, in organisms with substantial primary ciliary involvement in development and tissue homeostasis, such as vertebrates, INTU maintains prominent ciliogenic functions in addition to its PCP-related roles. This evolutionary trajectory suggests that INTU originated as a PCP effector regulating actin dynamics and that its ciliogenic functions evolved secondarily following the expansion of ciliary roles during vertebrate evolution.

### Structure-Function Relationships

The multiple longin domains present in INTU appear to represent an evolutionary elaboration of a simpler ancestral protein. The longin domains themselves likely originated through tandem duplication of an ancestral longin-containing protein, creating a multi-valent binding platform. This multi-domain architecture enables INTU to simultaneously engage multiple binding partners, a feat impossible for single-domain proteins. The presence of similar multi-longin domain arrangements in other trafficking regulators such as Hps1 and CCZ1 suggests that this architectural solution for creating multi-valent binding hubs has been selected for through evolution across multiple protein families.

## Future Research Directions and Therapeutic Implications

### Outstanding Questions Regarding INTU Function

Despite substantial progress in characterizing INTU's roles in ciliogenesis and development, several fundamental questions remain. The precise subcellular localization of INTU during different stages of ciliogenesis remains incompletely defined, and whether INTU undergoes relocalization as ciliogenesis progresses remains uncertain. The specific substrates of INTU GEF activity beyond Rab23 remain unknown, and whether INTU acts as a GEF for multiple Rab proteins requires investigation. The mechanisms controlling INTU recruitment to basal bodies and the identity of specific basal body localization signals within the INTU sequence require elucidation.

Additionally, the potential role of INTU in ciliary disassembly and resorption, processes equally important to ciliary assembly, has received minimal investigation. Whether INTU participates in regulating ciliary signaling output beyond its role in ciliary assembly awaits investigation. The possible role of INTU in regulating ciliary protein trafficking selectivity through its interactions with transition zone proteins represents another fertile area for future investigation.

### Therapeutic Potential and Disease Modulation

Understanding INTU's molecular functions holds substantial promise for developing therapeutic interventions for ciliopathy-associated diseases. Current therapeutic approaches for ciliopathies remain limited, as the underlying ciliary defects cannot yet be corrected pharmacologically. However, understanding the specific molecular lesions caused by particular INTU mutations may enable development of targeted therapeutics capable of rescuing specific defects. For instance, missense mutations affecting CPLANE complex assembly might be corrected through small molecules promoting complex stability, while mutations affecting lipid binding might be addressed through synthetic lipid analogs.

Furthermore, modulation of INTU function may provide therapeutic benefit even in ciliopathies not directly caused by INTU mutations. Enhancing INTU expression or activity might improve ciliary assembly efficiency in cells with partially defective ciliogenesis, potentially ameliorating disease manifestations in various ciliopathies. Conversely, in diseases characterized by inappropriate or excessive ciliogenesis-dependent signaling, inhibition of INTU activity might prove beneficial.

## Conclusion

The INTU protein emerges from comprehensive analysis of contemporary literature as a multifaceted regulator of critical developmental processes, occupying a central position within the CPLANE complex and serving as a primary determinant of ciliary assembly competence in diverse vertebrate cell types. Through its roles in recruiting and organizing intraflagellar transport machinery, regulating actin cytoskeletal dynamics, binding phospholipid membrane signals, and catalyzing nucleotide exchange on small GTPases, INTU orchestrates the formation of primary cilia essential for embryonic development, tissue homeostasis, and cilia-dependent signal transduction including hedgehog, Wnt, and Hippo pathway signaling. The protein's localization to basal bodies and the pericentriolar material positions it at the anatomical epicenter of ciliogenesis, enabling its direct participation in recruiting and organizing ciliary precursors. INTU's essential developmental roles are underscored by the severe developmental abnormalities resulting from INTU loss-of-function mutations, which cause orofaciodigital syndrome XVII and short-rib thoracic dysplasia with polydactyly, distinctive ciliopathy presentations affecting skeletal, orofacial, and organ development. The conservation of INTU's structure and function across diverse metazoan species highlights the evolutionary antiquity and fundamental importance of its roles in regulating both planar cell polarity signaling and, in vertebrates, the assembly of ciliary organelles essential for development and tissue function. Future investigations addressing the remaining questions regarding INTU's regulation, substrate specificity, and role in ciliary signaling output promise to reveal additional dimensions of INTU's cellular biology and may enable development of novel therapeutic approaches for ciliopathy-associated diseases.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=27152
2. https://www.uniprot.org/uniprotkb/H0YA54/entry
3. https://www.ncbi.nlm.nih.gov/gene/380614
4. https://www.uniprot.org/uniprotkb/Q9ULD6/entry
5. https://www.ncbi.nlm.nih.gov/gene/27152
6. https://maayanlab.cloud/Harmonizome/gene/INTU
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC11107551/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC3524640/
9. https://www.ebi.ac.uk/interpro/entry/pfam/PF19031/domain_architecture/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC11180893/
11. https://en.wikipedia.org/wiki/Planar_cell_polarity
12. https://www.uniprot.org/uniprotkb/B3M7Z8/entry
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC9252817/
14. https://www.nature.com/articles/s41392-023-01559-5
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC3595456/
16. https://www.genecards.org/cgi-bin/carddisp.pl?gene=INTU
17. https://pubmed.ncbi.nlm.nih.gov/22659135/
18. https://thebiogrid.org/interaction/1194262/ap2m1-intu.html
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9012472/
20. https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1006627
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC7247936/
22. https://www.nature.com/articles/s41467-025-61005-8
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC11006408/
24. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.13987
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC9189429/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC3631122/
27. https://www.ncbi.nlm.nih.gov/books/NBK542285/
28. https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/dvdy.724
29. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.653138/full
30. https://elifesciences.org/articles/108870
31. https://www.nature.com/articles/s41431-024-01619-6
32. https://pubmed.ncbi.nlm.nih.gov/26567219/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC8471410/
34. https://pubmed.ncbi.nlm.nih.gov/34623732/
35. https://www.nature.com/articles/s41467-017-01328-3
36. https://rupress.org/jcb/article/223/4/e202311140/276646/Positioning-centrioles-and-centrosomesCentrosome
37. https://www.science.org/doi/10.1126/sciadv.abn0832
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC3786140/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC4573840/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC12219219/
41. https://www.nature.com/articles/s41588-025-02400-1
42. https://www.proteinatlas.org/ENSG00000197079-KRT35
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC6864590/
44. https://insight.jci.org/articles/view/179468
45. https://www.nature.com/articles/s41467-023-37208-2
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC10009165/
47. https://pubmed.ncbi.nlm.nih.gov/40571631/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC8351562/
49. https://rupress.org/jcb/article/213/3/355/38674/Regulation-of-podocalyxin-trafficking-by-Rab-small
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC9221175/
51. https://www.nature.com/articles/s41594-022-00905-5
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC1839770/
53. https://pmc.ncbi.nlm.nih.gov/articles/PMC1472299/
54. https://elifesciences.org/articles/54445
55. https://pmc.ncbi.nlm.nih.gov/articles/PMC3754476/
56. https://www.malacards.org/card/short_rib_thoracic_dysplasia_20_with_polydactyly
57. InterPro annotations[9]
58. computational subcellular localization predictions[16]