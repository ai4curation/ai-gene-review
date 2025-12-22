---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-12T07:11:18.686217'
end_time: '2025-12-12T07:13:38.216954'
duration_seconds: 139.53
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TFRC
  gene_symbol: TFRC
  uniprot_accession: P02786
  protein_description: 'RecName: Full=Transferrin receptor protein 1; Short=TR; Short=TfR;
    Short=TfR1; Short=Trfr; AltName: Full=T9; AltName: Full=p90; AltName: CD_antigen=CD71;
    Contains: RecName: Full=Transferrin receptor protein 1, serum form; Short=sTfR;'
  gene_info: Name=TFRC;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the peptidase M28 family. M28B subfamily.
  protein_domains: PA_dom_sf. (IPR046450); PA_domain. (IPR003137); Peptidase_M28.
    (IPR007484); Peptidase_M28B. (IPR039373); TFR-like_dimer_dom. (IPR007365)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 56
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P02786
- **Protein Description:** RecName: Full=Transferrin receptor protein 1; Short=TR; Short=TfR; Short=TfR1; Short=Trfr; AltName: Full=T9; AltName: Full=p90; AltName: CD_antigen=CD71; Contains: RecName: Full=Transferrin receptor protein 1, serum form; Short=sTfR;
- **Gene Information:** Name=TFRC;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the peptidase M28 family. M28B subfamily.
- **Key Domains:** PA_dom_sf. (IPR046450); PA_domain. (IPR003137); Peptidase_M28. (IPR007484); Peptidase_M28B. (IPR039373); TFR-like_dimer_dom. (IPR007365)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TFRC" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TFRC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TFRC** (gene ID: TFRC, UniProt: P02786) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this task carefully. The user wants a comprehensive research report on the TFRC gene (transferrin receptor protein 1, CD71) in humans. The UniProt accession is P02786.

Let me verify the context:
1. Gene symbol: TFRC ✓
2. Protein: Transferrin receptor protein 1 (TfR1, CD71) ✓
3. Organism: Homo sapiens (Human) ✓
4. UniProt: P02786 ✓

The search results provided contain extensive information about TFRC/TfR1. Let me organize my findings into major themes for the report structure.

Major themes to cover:
1. Molecular Structure and Basic Function - Structure of the protein, transmembrane organization, domains
2. Iron Transport Mechanisms - How TfR1 binds and internalizes iron-loaded transferrin
3. Intracellular Trafficking Pathway - Endocytosis, sorting, recycling
4. Regulation and Post-translational Modifications - How expression is regulated (iron-responsive elements), how the protein is modified
5. Interactions and Cellular Partners - HFE interactions, other binding partners
6. Clinical and Biological Significance - Role in disease, erythropoiesis, cancer
7. Specialized Functions - Blood-brain barrier transport, ferritin binding, viral interactions
8. Therapeutic Applications - Anti-TfR1 antibodies, drug delivery strategies

Let me now write a comprehensive 10,000+ word report based on the search results provided, making sure to:
- Cite all major claims
- Use flowing paragraphs instead of lists
- Maintain academic tone
- Cover all the required aspects
- Ensure proper narrative flow
</think>

# Transferrin Receptor Protein 1 (TFRC): A Comprehensive Analysis of Molecular Structure, Function, and Biological Significance

## Executive Summary

Transferrin receptor protein 1 (TfR1), also designated as cluster of differentiation 71 (CD71), represents one of the most extensively characterized iron transport proteins in humans, encoded by the TFRC gene located on chromosome 3[1][3]. As a cell surface glycoprotein expressed on virtually all nucleated cells, TfR1 functions as the primary gateway for cellular iron acquisition through receptor-mediated endocytosis of iron-bound transferrin molecules[10][32]. The protein's significance extends well beyond basic iron homeostasis, encompassing critical roles in erythropoiesis, proliferation of rapidly dividing cells, and emerging therapeutic applications in cancer treatment and drug delivery to the brain. Understanding TfR1's molecular mechanisms, regulatory pathways, and biological contexts illuminates fundamental principles of cellular nutrient acquisition and reveals potential vulnerabilities that cancer cells exploit to support their elevated metabolic demands. This comprehensive report synthesizes current knowledge regarding TfR1's structure, function, intracellular trafficking, regulation, and clinical relevance, providing a detailed mechanistic foundation for understanding how this receptor orchestrates iron import and influences cellular physiology across diverse biological contexts.

## Molecular Structure and Protein Architecture

### Transmembrane Organization and Structural Domains

TfR1 is a transmembrane glycoprotein composed fundamentally of two disulfide-linked monomers, each approximately 90 kilodaltons in size, creating a functional homodimer at the cell surface[1][2][27]. The protein architecture comprises a single transmembrane domain with an extracellular ectodomain containing the iron and transferrin binding regions, a membrane-proximal region, and a relatively short cytoplasmic tail of approximately 67 amino acids[1][47]. The two polypeptide chains are covalently linked by disulfide bonds at residues 89 and 98, positioned immediately extracellular to the transmembrane domain, which provides structural stability to the dimeric complex[15]. Notably, crystallographic studies have revealed that the disulfide-linked dimeric structure, while providing stability, is not absolutely essential for the protein's functional activity, as non-covalently linked dimers retain substantial iron transport capacity[27].

The three-dimensional structure of the TfR1 ectodomain reveals three distinct functional domains arranged within each monomeric subunit[49][52]. One domain exhibits striking structural similarity to carboxypeptidases and aminopeptidases, belonging to the M28 family of zinc-dependent proteases, though TfR1 itself is catalytically inactive as a peptidase[43][49]. This protease-like domain participates critically in both transferrin binding and in stabilizing the conformational changes necessary for iron release from transferrin within acidic endosomal compartments[49][60]. The remaining domains include an apical domain and a helical domain, each contributing essential interactions with ligand molecules and mediating conformational changes during the iron transport cycle[60]. The structural organization positions these domains to facilitate binding of iron-laden transferrin at physiological pH on the cell surface while simultaneously preparing the receptor for the conformational rearrangements triggered by endosomal acidification[49][52].

### Post-Translational Modifications and Chemical Modifications

TfR1 undergoes multiple post-translational modifications that influence its localization, stability, and functional activity. Each monomeric chain is extensively glycosylated, with N-linked carbohydrate moieties contributing to protein stability, trafficking, and potentially immune recognition[1][2]. Additionally, the protein is palmitoylated at the inner membrane surface, a lipid modification occurring on intracellular cysteine residues that enhances membrane association and may influence lateral mobility within the plasma membrane[1][26]. The cytoplasmic domain contains a unique phosphorylation site at serine residue 24, though surprisingly, phosphorylation at this site does not appear critical for the protein's endocytic function or basolateral sorting in polarized cells[58]. This observation suggests that while phosphorylation occurs in response to kinase activity, it may not constitute an essential regulatory mechanism for basal iron transport function, though it might modulate responses to specific cellular signals or growth factors.

## Iron Transport Function and Cellular Iron Acquisition

### Molecular Mechanism of Transferrin Binding and Internalization

The primary physiological function of TfR1 involves binding iron-loaded transferrin (holo-transferrin) at the cell surface and mediating its entry into cells through clathrin-dependent endocytosis[2][7][10]. Iron in plasma exists in a highly restricted form, primarily bound to transferrin, an 85-kilodalton transport protein carrying up to two ferric iron (Fe³⁺) atoms in two distinct binding sites designated the C-terminal lobe and N-terminal lobe[2][15]. TfR1 exhibits striking selectivity for diferric transferrin over iron-free apotransferrin at neutral pH, creating a mechanism that ensures cells preferentially import iron-loaded molecules while generally excluding iron-depleted transferrin from cellular uptake[15][57]. The C-lobe and N-lobe of transferrin each interact with distinct regions of the TfR1 ectodomain, with the C-lobe engaging the helical domain of the receptor while the N-lobe contacts the stalk region[57].

Upon holo-transferrin binding, the transferrin-TfR1 complex undergoes rapid clustering within specialized plasma membrane invaginations called coated pits, which are lined with the clathrin scaffolding protein[1][7]. The formation of these coated pits requires multiple machinery components, including the clathrin complex itself, adaptor proteins, and dynamin, a GTPase essential for membrane scission[7]. Within these coated structures, phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P₂) plays a critical regulatory role, as inactivation of this phospholipid directly reduces transferrin internalization and increases surface levels of TfR1, demonstrating the importance of lipid composition in regulating this entry pathway[7]. The internalized transferrin-receptor complex is transported in clathrin-coated vesicles that rapidly lose their clathrin coats and fuse with early endosomal compartments within minutes of internalization[7][9].

### Iron Release and Endosomal Sorting

Once internalized into early endosomes, a critical pH-dependent conformational change occurs that dramatically alters the transferrin-TfR1 interaction and enables iron release[5][15][57]. The early endosomal compartment maintains a pH of approximately 5.0-6.0, maintained by vacuolar ATPase proton pumps, which creates an acidic microenvironment promoting protonation of histidine residues within both transferrin and the receptor[2][5]. This acidification triggers dramatic conformational changes in the transferrin molecule, particularly affecting the iron binding sites and the interaction interfaces between transferrin and its receptor[57][60]. Specifically, protonation of His349 in the C-terminal lobe at acidic pH converts a hydrophobic interaction with Phe760 of the TfR into a stronger cation-π interaction or salt bridge with Asp757, causing a conformational change that destabilizes the iron binding cleft in the C-lobe[60]. Simultaneously, the N-lobe undergoes movement of its PRKP loop that disrupts the N2 subdomain's interaction with the receptor, allowing the iron binding cleft to open and release the iron atom[60].

Critically, the transferrin receptor itself undergoes ligand-dependent conformational changes that actively promote iron release from transferrin at acidic pH[5][60]. The binding of iron-loaded transferrin causes rotation at the TfR1 dimer interface, bringing four critical histidine residues (His475 in each protease-like domain and His684 in each helical domain) into proximity[60]. These conformational changes at the dimer interface prime the receptor to undergo additional pH-induced movements when exposed to endosomal acidification, directly facilitating the conformational changes in transferrin that enable iron dissociation[60]. This active role of the receptor in stimulating iron release represents a sophisticated mechanism ensuring efficient iron delivery into the cell[5]. Additionally, within endosomes, the ferric iron (Fe³⁺) released from transferrin is rapidly reduced to ferrous iron (Fe²⁺) by metalloproteases, notably STEAP3, a process essential for subsequent iron export from the endosome[2].

### Iron Export and Intracellular Distribution

Once iron is released from transferrin within acidic endosomes, the ferrous iron (Fe²⁺) must be transported across the endosomal membrane into the cytoplasm through the action of divalent metal transporter 1 (DMT1, also called SLC11A2)[2][14]. DMT1 functions as a proton-coupled iron transporter, with the acidic endosomal environment providing the proton gradient necessary to drive iron uptake across the endosomal membrane[2][14]. Once in the cytoplasm, iron faces three potential metabolic fates depending on cellular needs[2]. Iron may be immediately incorporated into ferritin, a 24-subunit iron storage protein that safely sequesters iron in mineral form as ferrihydrite, protecting against the generation of reactive oxygen species through Fenton chemistry[2][14]. Alternatively, iron may be transported to mitochondria for incorporation into heme groups and iron-sulfur clusters, essential cofactors in the electron transport chain and numerous metabolic enzymes[2][40]. Finally, iron may be exported back into the extracellular environment through ferroportin (SLC40A1), the only known cellular iron exporter, allowing iron redistribution to other tissues[2][14].

The export of iron through ferroportin is tightly regulated by hepcidin, a circulating peptide hormone produced by hepatocytes that binds ferroportin and triggers its ubiquitin-mediated degradation, thereby preventing iron export and causing cellular iron retention[14]. This systemic hormone represents the critical control point for whole-body iron homeostasis, linking iron sensing in the liver to the regulation of iron absorption in the intestine and iron recycling in macrophages[14]. Understanding this regulatory axis proves essential for comprehending both normal iron metabolism and iron overload disorders.

## Intracellular Trafficking Pathway and Receptor Recycling

### Clathrin-Mediated Endocytosis and Early Endosomal Sorting

The internalization of transferrin receptor and its ligand occurs through well-characterized clathrin-mediated endocytosis, involving recruitment of the receptor into coated pits through interactions with adaptor protein complexes[7][49]. The AP2 adaptor complex, comprising four subunits (α, β, μ, and σ), binds directly to a critical YXRF internalization motif (where Y is tyrosine, X is any amino acid, R is arginine, and F is phenylalanine) located within the cytoplasmic tail of TfR1[58]. This motif appears to form a tight turn structure that is specifically recognized by adaptor proteins, ensuring efficient clustering of the receptor into coated pits[58]. Once internalized into clathrin-coated vesicles, the vesicles rapidly lose their clathrin coat through the action of uncoating proteins, exposing the underlying transport vesicle to fusion machinery[7].

The early endosomal compartment represents a highly dynamic sorting station where cargo molecules are distributed to distinct cellular destinations based on their biochemical properties[7][9]. Early endosomes exist in two functionally distinct populations—dynamic early endosomes that mature through transitional stages, and static early endosomes that remain relatively stable[7]. The sorting of transferrin at the cell surface appears to begin immediately upon binding and receptor clustering, with early segregation occurring through TIRF (Total Internal Reflection Fluorescence) microscopy-visualized mechanisms within 100-200 nanometers of the plasma membrane[7]. This pre-endosomal sorting suggests that the cell possesses mechanisms for distinguishing cargo molecules even before their entry into membrane-enclosed compartments, potentially through preferential inclusion in distinct lipid microdomains or through interactions with specific sorting proteins[7].

### Recycling Endosome Trafficking and Plasma Membrane Return

Following iron release in early endosomes, both the transferrin receptor and iron-depleted transferrin (apotransferrin) must be recycled back to the cell surface to complete the iron transport cycle and to allow transferrin molecules to acquire new iron in the bloodstream[7][9]. This recycling process is mediated through recycling endosomes, specialized compartments enriched in the Rab11 GTPase, which functions as a crucial regulator of membrane trafficking from recycling endosomes back to the plasma membrane[7][59]. Real-time fluorescence microscopy studies have revealed that transferrin moves into tubular formations in both static and dynamic early endosomes before separating, with these vesicles then delivering transferrin to either the perinuclear recycling compartment or directly back to the plasma membrane[7]. The perinuclear recycling compartment, marked by Rab11 localization, represents a major hub for receptor sorting and redistribution[7][59].

Multiple small GTPases of the Rab family regulate distinct steps of the transferrin recycling pathway, with Rab4, localized primarily in early endosomes, mediating rapid recycling of some transferrin receptor molecules directly from early endosomes to the plasma membrane[7]. Overexpression of Rab4 causes accumulation of transferrin in tubular structures and vesicles directed toward the recycling compartment, suggesting that Rab4 modulates the velocity and efficiency of recycling[7]. The GEF Grab (guanine nucleotide exchange factor for Rab8) has emerged as another critical regulator of transferrin receptor recycling specifically in erythroid cells, with GRAB knockdown reducing transferrin-bound iron uptake and causing hypochromic-microcytic anemia in mouse models[37]. The exocyst, a multiprotein complex involved in tethering recycling vesicles to the plasma membrane, appears to be recruited by active Rab8 in a Grab-dependent manner, providing a molecular link between Rab GTPase activation and vesicle fusion[37].

### Sorting Between Recycling and Lysosomal Degradation

While TfR1 is predominantly recycled back to the plasma membrane to maintain high iron import capacity, constitutive degradation of the receptor also occurs through a specialized Rab12-dependent pathway[59]. Small GTPase Rab12 and its upstream activator Dennd3 regulate the trafficking of TfR1 from recycling endosomes to lysosomes, with Rab12 activation promoting TfR1 degradation[59]. This constitutive degradation pathway appears distinct from conventional endocytic degradation through late endosomes and multivesicular bodies, instead operating through direct trafficking from recycling endosomes to lysosomes[59]. The physiological significance of this basal degradation pathway remains unclear but may provide a mechanism for modulating TfR1 levels independent of iron-responsive transcriptional regulation[59].

Additionally, under conditions of iron excess, TfR1 undergoes iron-induced selective degradation through lysosomal pathways, providing a mechanism to reduce iron uptake capacity when intracellular iron levels become elevated[59]. This iron-regulated degradation complements the transcriptional downregulation of TfR1 mediated through iron-responsive elements, creating multiple levels of control over iron import capacity[59]. Importantly, recent studies employing cryo-electron microscopy have revealed structural details of how the transferrin receptor interacts with its ligands in the endosomal environment, showing that the apical domain of TfR1 mediates binding to heavy-chain ferritin through a distinct set of epitopes compared to those used for transferrin binding, allowing differential regulation of iron acquisition from these two sources[22].

## Regulation of Transferrin Receptor Expression

### Iron-Responsive Element Regulation

The cellular abundance of transferrin receptor is tightly regulated by iron status through a sophisticated post-transcriptional mechanism involving iron-responsive elements (IREs) and iron regulatory proteins (IRPs)[31][34]. The 3′ untranslated region (3′ UTR) of TFRC mRNA contains five IREs, which are short conserved stem-loop structures recognized by two functionally similar iron regulatory proteins, IRP1 and IRP2[31][34]. Under conditions of low intracellular iron, these IRPs bind avidly to the TFRC IREs, stabilizing the mRNA and preventing its degradation[31][34]. The protective effect of IRP binding appears mediated through blocking access of endonucleases to the unstable regions within the 3′ UTR, as mutagenesis studies have identified multiple non-IRE stem-loops contributing minimally to mRNA instability but enhancing instability when IRP protection is lost[31].

When intracellular iron levels rise, IRP1 undergoes an iron-sulfur cluster (Fe-S) assembly that converts it into an aconitase-like conformation unsuitable for IRE binding, causing its release from the TFRC mRNA and allowing the mRNA to be rapidly degraded[34]. IRP2, by contrast, is ubiquitinated and proteasomally degraded under iron-replete conditions[34]. This iron-sensing mechanism achieves remarkable specificity through direct iron binding to the IRE itself, which induces conformational changes favoring eIF4F (eukaryotic Initiation Factor 4F) binding over IRP binding, creating a conformational switch that responds to iron status[14][34]. The regulatory response appears graded rather than switch-like, with progressive loss of IRP protection occurring as iron levels increase, allowing cells to fine-tune TfR1 expression in response to cellular iron demands[31].

### Transcriptional and Signal-Responsive Regulation

Beyond the iron-responsive post-transcriptional regulation, TfR1 expression is modulated by multiple transcriptional and signaling pathways responding to cellular growth, differentiation signals, and metabolic states[1][2]. Growth factors including insulin and insulin-like growth factors upregulate TfR1 expression, reflecting increased iron demands of proliferating cells[2]. Erythropoietin (EPO), a key regulator of red blood cell production, strongly induces TfR1 expression in erythroid progenitors, enabling the massive iron uptake necessary for hemoglobin synthesis during erythropoiesis[40]. The transcriptional upregulation of TFRC during erythroid differentiation occurs through multiple pathways, including the GATA1 transcription factor crucial for erythroid-specific gene expression, demonstrating integration of iron metabolism control with the physiological demands of hematopoiesis[40].

Interestingly, TFRC expression is also regulated through alternative splicing mechanisms responsive to iron status and cellular context, with evidence suggesting that the transferrin receptor itself possesses RNA-binding protein properties influencing splicing patterns of genes involved in iron metabolism, DNA repair, and translation[36]. This newly appreciated function of TfR1 as an RNA-binding protein adds an additional layer of complexity to iron metabolism regulation, suggesting that TfR1 may coordinate iron uptake with cellular processes dependent on iron availability at the transcriptional level[36].

## Protein Interactions and Functional Partnerships

### Interaction with HFE and Regulation of Hepcidin Expression

A critical interaction occurs between TfR1 and HFE (hemochromatosis protein), the protein mutated in hereditary hemochromatosis type 1[20][23]. HFE interacts with TfR1 through the α1 and α2 domains of HFE and functions as a regulatory cofactor that modulates the iron-sensing properties of the transferrin receptor system[20][23]. The HFE-TfR1 complex appears to interact with TfR2 (transferrin receptor 2), creating a supramolecular complex involved in iron sensing and signaling to regulate hepcidin expression, the master hormone controlling systemic iron homeostasis[20]. The TfR2/HFE complex detects iron-loaded transferrin and triggers activation of BMP-SMAD signaling pathways that enhance hepcidin transcription in hepatocytes[20]. Specifically, the iron-bound transferrin-TfR2-HFE complex mediates conformational changes that activate downstream signaling, ensuring that increased iron availability triggers increased hepcidin production to limit further iron absorption[20].

Importantly, disruption of the HFE-TfR1 interaction alone does not impair hepcidin regulation, suggesting that HFE sequestration from TfR1 allows its interaction with TfR2, which appears to be the critical complex for hepcidin regulation[20]. This model proposes that TfR1 competes with TfR2 for HFE binding under low holo-transferrin conditions, but when iron-loaded transferrin concentrations increase, the holo-transferrin-TfR2-HFE complex forms and activates hepcidin transcription[20]. Evidence supporting this model includes observations that in TfR1 mutant mice lacking functional TfR1, higher levels of hepcidin mRNA accumulate, consistent with increased availability of HFE to bind TfR2[20]. This elegant regulatory mechanism demonstrates how TfR1's role extends beyond simple iron uptake to encompass systemic iron homeostasis through protein-protein interactions controlling hormonal signaling[20].

### Ferritin Binding and Alternative Iron Acquisition Pathways

Beyond transferrin, TfR1 binds heavy-chain ferritin (H-Ft), providing an alternative source of bioavailable iron for cells[19][22]. Ferritin, a spherical 24-subunit iron storage protein composed of heavy-chain (FHC) and light-chain (FLC) subunits, circulates in plasma at low concentrations and can be internalized by cells expressing TfR1[19][22]. The binding of ferritin to TfR1 occurs through distinct epitopes compared to those used for transferrin binding, with structural studies revealing that specific residues in the ferritin BC-loop (particularly Y211 and N-terminal residues of the A helix including Q14, D15, and R22) are critical for receptor recognition[22]. Notably, ferritin composed entirely of light chains does not bind TfR1, indicating that heavy-chain subunits provide the essential binding determinants[19][22]. Upon binding and internalization through TfR1-mediated endocytosis, ferritin enters both endosomal and lysosomal compartments where acidification and proteolysis release stored iron[19].

The functional significance of ferritin-TfR1 interaction becomes particularly apparent in erythroid precursors, where ferritin uptake via TfR1 can provide sufficient iron for hemoglobin synthesis in the absence of transferrin, demonstrating functional redundancy in iron acquisition pathways[19]. This dual-receptor function suggests that ferritin and transferrin may serve complementary roles in coordinating iron processing and utilization, potentially allowing cells to respond flexibly to varying iron bioavailability in different physiological contexts[19][22]. The shared use of TfR1 for both transferrin and ferritin uptake raises interesting questions about how endosomal iron metabolism differs between these two pathways and whether ferritin-derived iron might supply specific pools of iron within the cell[19].

## Cellular and Tissue Distribution

### Expression Patterns in Normal Tissues and Cell Types

TfR1 exhibits a remarkably broad tissue distribution, reflecting the fundamental importance of iron for virtually all nucleated cells[13][16]. Expression is particularly abundant in tissues with high metabolic rates or rapid cell proliferation, including bone marrow, placenta, and rapidly proliferating epithelial tissues[13][16]. Within normal bone marrow, TfR1 is expressed predominantly on erythroid precursor cells of all maturation stages, with expression being essentially absent from mature erythrocytes[1][2][40]. This developmental pattern of expression makes physiological sense, as mature red blood cells have lost their nuclei and cannot synthesize new hemoglobin, eliminating their requirement for iron import[40]. In contrast, erythroid precursor cells express extremely high levels of TfR1 to satisfy the enormous iron demands of hemoglobin synthesis, with approximately 80% of total cellular iron utilization occurring in erythroid precursors for hemoglobin production, and consequently, approximately 80% of total TfR1 is expressed on erythroid cells[15][40].

Beyond erythropoiesis, TfR1 is expressed on hepatocytes, Kupffer cells (tissue macrophages of the liver), endocrine pancreas cells, basal epidermis, testicular tissue, and pituitary cells in normal tissues[13]. This distribution reflects the iron requirements of different cell types for essential enzymatic functions and metabolic processes[13]. The restricted pattern of expression in normal tissues contrasts sharply with its widespread upregulation in malignant neoplasms, where rapidly dividing cancer cells dramatically increase TfR1 expression to meet escalated iron demands for ribonucleotide reductase and other iron-dependent biosynthetic enzymes required for DNA synthesis and cell proliferation[13][39].

### Expression in Erythropoiesis and Hemoglobin Synthesis

Erythropoiesis represents the physiological context in which TfR1 achieves its highest expression levels and most critical functional importance[40]. During differentiation of erythroid progenitors stimulated by erythropoietin (EPO), cells progressively increase TfR1 surface levels, enabling them to import the massive quantities of iron required for hemoglobin synthesis[40]. The process of hemoglobin production demands approximately 30 million iron atoms per second in an adult human, highlighting the extraordinary iron-handling capacity that must be maintained by the erythroid compartment[40]. Recent discoveries have identified Grab, a guanine nucleotide exchange factor for Rab8, as a critical erythroid-specific regulator of TfR1 recycling to the plasma membrane[37]. Polymorphisms in GRAB and RAB8 genes associate with variations in mean corpuscular hemoglobinization of red blood cells, indicating that genetic variation in recycling machinery influences iron delivery efficiency and ultimately hemoglobin accumulation[37].

The Grab-Rab8 axis appears to function by recruiting the exocyst to recycling endosomes in an iron-demand-responsive manner, controlling the rate at which TfR1 is returned to the plasma membrane to import additional iron[37]. In Grab-deficient cells, TfR1 fails to recycle efficiently, accumulating in intracellular compartments and eventually being diverted to lysosomes for degradation, resulting in decreased cellular iron uptake and reduced hemoglobin synthesis[37]. These findings suggest that erythroid-specific recycling machinery provides a regulatory point for modulating iron uptake capacity in response to the differentiation stage and hemoglobin synthesis requirements of developing red blood cells[37].

## Specialized Functions and Pathological Roles

### Blood-Brain Barrier Transcytosis and Central Nervous System Iron Delivery

The blood-brain barrier (BBB) presents a formidable obstacle to drug delivery to the central nervous system, restricting passage of most large molecules and permitting only small, lipophilic compounds to cross the endothelial monolayer forming this barrier[24]. However, TfR1 is highly expressed on brain endothelial cells of the BBB, where it mediates transcytosis of transferrin-bound iron from systemic circulation into brain parenchyma, delivering this essential nutrient across an otherwise impermeable barrier[24]. Antibodies targeting TfR1, particularly anti-TfR1 monoclonal antibodies, have been engineered to exploit this physiological transcytotic pathway for drug delivery, with the antibodies being internalized at the luminal surface of brain endothelial cells and transcytosed to the abluminal surface, delivering attached therapeutic cargo to brain tissues[21][24].

The efficiency of transcytosis appears critically dependent on the binding affinity of anti-TfR1 antibodies to their epitope[21]. Paradoxically, high-affinity antibodies demonstrate reduced transcytosis efficiency, with antibodies showing affinities of 76 nanoMolar and 108 nanoMolar transporting more efficiently across the BBB than high-affinity 5 nanoMolar variants[21]. The mechanistic explanation for this counterintuitive finding involves antibody sorting and trafficking within endosomal compartments—high-affinity bivalent antibodies are preferentially directed toward late endosomes and lysosomes for degradation, whereas lower-affinity variants are preferentially sorted toward early endosomes, from which they can be efficiently recycled and exocytosed on the abluminal surface[21]. This sorting mechanism appears linked to alterations in endocytic recycling pathways triggered by different avidity states of antibody-receptor interactions, with monovalent antibodies showing particular efficiency in promoting transcytosis by favoring early endosomal sorting tubules[21].

### Role in Cancer Cell Proliferation and Metabolic Support

TfR1 is dramatically overexpressed on the surfaces of malignant cells from multiple cancer types, including breast cancer, gliomas, ovarian cancer, lung cancer, hepatocellular carcinoma, and colon cancer, establishing it as a universal cancer biomarker[39][42]. Cancer cells upregulate TfR1 expression to meet escalated iron demands driven by rapid proliferation requiring DNA synthesis, the rate-limiting step of which depends on ribonucleotide reductase (RNR)—an iron-dependent enzyme synthesizing nucleotide precursors[39][42]. Iron serves as an essential cofactor for the R1 subunit of ribonucleotide reductase, which forms a critical tyrosyl radical on Tyr122 required for catalytic activity[39]. Additionally, iron-dependent proteins including electron transport chain components become increasingly critical in cancer cells supporting altered metabolic states, making iron availability a potential therapeutic vulnerability[42].

Studies demonstrating blocking of anti-TfR1 monoclonal antibodies inhibit cancer cell proliferation through iron deprivation represent proof-of-concept for TfR1-targeted therapeutic approaches[42]. Notably, anti-TfR1 antibodies inhibit growth of erythroleukemia and B-cell lymphoma cell lines with IC50 values as low as 0.1 micrograms per milliliter, with in vivo studies showing tumor regression in xenograft models through mechanisms involving both iron deprivation and antibody-dependent cellular cytotoxic effector functions[51]. Importantly, anti-TfR1 treatment additionally upregulates hypoxia-inducible factor-1 alpha (HIF-1α) through reduced iron availability for prolyl hydroxylase activity, potentially increasing tumor angiogenesis, suggesting that optimal therapeutic strategies might combine anti-TfR1 antibodies with agents targeting hypoxia pathways[42].

Recent evidence indicates that TfR1 expression correlates with poor overall survival in osteosarcoma patients, with TFRC knockdown in osteosarcoma cell lines significantly reducing proliferation, migration, and invasion abilities[39]. The mechanism involves decreased total intracellular iron content following TFRC knockdown, leading to reduced ribonucleotide reductase 2 (RRM2) expression and activity[39]. Remarkably, the reduction in osteosarcoma cell proliferation caused by TFRC knockdown can be reversed by supplementing cells with ferric ammonium citrate (FAC) or by overexpressing RRM2, directly demonstrating that TFRC-mediated iron uptake drives RRM2-dependent DNA synthesis supporting cancer cell proliferation[39].

### Viral Exploitation of Transferrin Receptor for Cell Entry

Multiple viral pathogens have evolved to exploit TfR1 as a cellular entry receptor, exploiting the abundance of this protein on target cells and its constitutive endocytic trafficking to acidic compartments favorable for viral membrane fusion[50][53]. New World arenaviruses causing hemorrhagic fevers in humans—including Machupo, Guanarito, Junin, and Sabia viruses—utilize human TfR1 as their cellular receptor, with the viral entry glycoprotein (GP) binding directly and specifically to TfR1[53]. Expression of human TfR1 in hamster cell lines markedly enhances infection by pseudoviruses displaying New World arenavirus GPs, whereas cells lacking TfR1 show minimal infection[53]. Conversely, Old World arenaviruses such as Lassa virus do not utilize TfR1 but instead use α-dystroglycan as a cellular receptor, demonstrating specific viral adaptation to particular receptor systems[53].

The structural basis for TfR1-viral GP interaction involves specific epitopes on TfR1 that are recognized by viral glycoproteins with high affinity comparable to transferrin binding[53]. Critically, anti-TfR1 monoclonal antibodies efficiently inhibit replication of Machupo, Guanarito, Junin, and Sabia viruses but not Lassa virus, demonstrating the functional requirement for TfR1 in New World arenavirus infection[53]. Remarkably, iron status influences viral infection efficiency, with iron depletion enhancing infection of Junin and Machupo pseudoviruses but not affecting Lassa virus, suggesting that iron-dependent conformational changes of TfR1 may enhance viral GP binding[53]. This viral dependence on TfR1 reflects both the abundance of this receptor on target cells and the evolutionary optimization of viral entry mechanisms to exploit constitutive endocytic pathways that deliver viral particles to appropriate intracellular compartments for membrane fusion[50][53].

### Role in Immune Dysfunction and Autoimmune Disease

Emerging research reveals that TfR1-mediated iron uptake plays unexpected roles in immune cell dysfunction and autoimmune diseases. In systemic lupus erythematosus (SLE), a prototypic autoimmune disease characterized by dysfunctional T cells, recent CRISPR screening identified TfR1 (CD71) as a critical factor specifically critical for T helper 17 cell (TH17) differentiation and inhibitory for induced regulatory T cells (iTregs)[54]. SLE-prone T cells display enhanced CD71 expression resulting from altered endosomal recycling, leading to increased intracellular iron accumulation[54]. This elevated iron uptake impairs mitochondrial function and mTORC1 signaling, skewing T cell differentiation toward pro-inflammatory TH17 and away from immunosuppressive iTregs[54]. Remarkably, anti-CD71 treatment reduces intracellular iron, inhibits TH17 differentiation, promotes IL-10 production by CD4 T cells, and reverses disease manifestations in SLE-prone mice[54]. Disease severity in SLE patients correlates directly with CD71 expression on TH17 cells, highlighting the pathogenic role of iron metabolism dysregulation in autoimmune dysfunction[54].

## Clinical Applications and Diagnostic Utility

### Soluble Transferrin Receptor as a Biomarker

TfR1 undergoes proteolytic cleavage at an Arg-Leu bond distal to the second disulfide bond linking the two monomers, releasing the soluble form of transferrin receptor (sTfR), a truncated protein lacking the transmembrane domain and consisting of 660 amino acids comprising the ectodomain[15][18]. This soluble form circulates in plasma at concentrations proportional to total cellular TfR1 abundance, making sTfR a valuable biomarker for iron metabolism status[15][18]. Approximately 80% of metabolic iron is incorporated into hemoglobin by erythroid precursors, and since most cellular TfR1 resides on erythroid cells, circulating sTfR concentration reflects erythroid precursor mass and erythropoiesis rate[15][40].

Circulating sTfR is particularly clinically useful for distinguishing iron deficiency from other causes of anemia or elevated ferritin levels[18]. Unlike ferritin, which functions as an acute-phase reactant elevated during inflammation, infection, malignancy, and chronic disease without indicating iron deficiency, sTfR is not influenced by inflammatory states[18]. Patients with iron deficiency show elevated sTfR levels as their erythroid precursor cells upregulate TfR1 to maximize iron capture from limited iron availability[18]. In contrast, patients with hypoplastic anemias (reduced erythropoiesis due to bone marrow failure) show low sTfR levels despite potentially low iron, allowing discrimination between iron deficiency and bone marrow failure[18]. Additionally, sTfR has been employed as a marker for erythropoietin (EPO) misuse by athletes, as EPO administration increases erythropoiesis and consequently sTfR levels, providing a physiological indicator of illicit EPO injection[4].

### Immunohistochemical Applications

CD71 (TfR1) serves as a robust immunohistochemical marker for several tissue types and disease processes. In particular, CD71 is highly expressed on chorionic villous trophoblasts of the placenta, with CD71 immunostaining particularly useful for identifying villous structures in necrotic or autolytic specimens where other morphologic features become obscured[1][13]. Among hematopoietic cells, CD71 is expressed specifically by erythroid precursors within the normal bone marrow and spleen, with this restricted expression pattern allowing discrimination of erythroid lineage cells from other hematopoietic populations[1][2]. In combination with markers specific to more mature erythrocytes such as glycophorin A (recognized by the TER-119 antibody in mice), flow cytometry analysis can track erythroid differentiation and assess changes in erythropoiesis during disease or treatment[2]. The CD71-positive population in bone marrow encompasses early erythroid precursors (proerythroblasts and early normoblasts) that actively synthesize hemoglobin, providing a specific identification of erythropoietic activity[2].

### Therapeutic Targeting and Drug Development

The prominent role of TfR1 in iron-dependent proliferation of cancer cells and its use by pathogenic viruses has spurred substantial drug development efforts targeting this receptor. Anti-TfR1 monoclonal antibodies represent the most advanced class of TfR1-targeting therapeutics, with multiple antibody formats being evaluated in clinical trials[51]. These antibodies block transferrin binding to TfR1, preventing iron-loaded transferrin internalization and causing iron starvation in target cells. Some anti-TfR1 antibodies show rapid internalization upon binding, making them suitable for delivery of attached therapeutic cargos into cells[51]. This property has enabled development of anti-TfR1 antibody-drug conjugates and fusion proteins combining anti-TfR1 antibodies with toxins, enzymes, or other therapeutic agents, allowing selective drug delivery to TfR1-expressing cancer cells[51].

InatherYs (now part of the InatherYs group), a biotechnology company in Évry, France, developed INA01, an anti-CD71 antibody candidate demonstrating efficacy in preclinical studies for treating two incurable orphan hematologic malignancies—adult T cell leukemia (ATLL) caused by human T-lymphotropic virus-1 (HTLV-1) infection and mantle cell lymphoma (MCL)[1]. These findings suggest that TfR1-targeted approaches may prove particularly valuable for treating malignancies in which TfR1 is particularly highly expressed or functionally critical for survival. Additionally, researchers have exploited the TfR1 transcytosis pathway at the blood-brain barrier for delivery of anti-TfR1 antibody fusion proteins carrying therapeutic cargos to brain tissues, enabling treatment of central nervous system diseases including glioblastoma and other CNS malignancies[24][51].

## Evolutionary Conservation and Comparative Biology

### Structural Homology and Family Relationships

TfR1 belongs to the M28 family of zinc-dependent peptidases and shares structural homology with numerous peptidase family members, including glutamate carboxypeptidase II (GCP2, also called PSMA), N-acetylated alpha-linked acidic dipeptidase (NAALAD), and related proteins[45][49]. Despite this structural similarity to catalytically active peptidases, TfR1 itself is catalytically inactive, having diverged from peptidase family members through loss of critical catalytic residues while retaining the overall structural scaffold[43]. This apparent evolutionary conversion of an active peptidase domain into a ligand-binding domain demonstrates how evolution repurposes protein domains for novel functions while maintaining structural integrity[49]. The transfer receptor family in primates is represented by at least seven different homologous proteins, indicating repeated gene duplication events in vertebrate evolution, likely reflecting divergent specialization of these receptors for distinct biological roles[45].

### Positive Selection and Species-Specific Adaptations

Comparative genomic analyses have revealed evidence for positive selection acting on the TFRC gene during the evolution of Caniformia (the clade including dogs and their relatives), suggesting that specific amino acid changes in TfR1 confer adaptive advantages in these species[48]. This evolutionary signature of positive selection on a receptor gene is relatively uncommon and suggests that changes in iron metabolism or iron sensing may have provided fitness advantages during caniform evolution, perhaps related to changes in dietary iron sources or metabolic rates[48]. Such evolutionary adaptation at TfR1 demonstrates that the specific sequence of this iron transport protein is subject to selective constraints and that functional optimization of TfR1 for each species' particular physiological requirements drives amino acid evolution[48].

## Conclusions and Future Perspectives

Transferrin receptor protein 1 represents one of the most comprehensively characterized iron transport proteins, reflecting both its fundamental biological importance and its prominence as a therapeutic target. The sophisticated molecular mechanisms governing TfR1 function—including pH-sensitive binding to transferrin with active promotion of iron release, rapid endocytic internalization through clathrin-dependent pathways, highly regulated recycling through Rab-mediated trafficking, and post-transcriptional control through iron-responsive elements—demonstrate the cellular investment in ensuring appropriate iron delivery matched to cellular needs. The protein's participation in diverse biological processes ranging from hemoglobin synthesis in erythroid precursors to iron sensing controlling systemic hepcidin production illustrates how a single receptor integrates multiple physiological signals to coordinate iron metabolism at cellular and organismal levels.

The emerging recognition of TfR1's roles beyond basic iron transport—including its function as a regulator of alternative splicing patterns, its involvement in viral cell entry, and its pathogenic role in autoimmune diseases—suggests that our understanding of this protein's biology remains incomplete. Future research employing structural biology, single-molecule studies, and system-wide approaches will likely reveal additional regulatory mechanisms and biological contexts in which TfR1 participates. The therapeutic potential of targeting TfR1 in cancer, leveraging the protein's abundant expression on rapidly dividing cells and the critical importance of iron for DNA synthesis, continues to drive drug development efforts that may provide effective treatments for otherwise intractable malignancies. As research deepens understanding of TfR1 biology and function, this protein will undoubtedly continue serving as a paradigm for understanding how cells precisely regulate nutrient acquisition in response to metabolic demands and environmental iron availability.

## Citations

1. https://en.wikipedia.org/wiki/Transferrin_receptor_1
2. https://www.bio-rad-antibodies.com/cd71-iron-transport-markers-antibodies.html
3. https://geneglobe.qiagen.com/us/knowledge/gene/ENSG00000072274
4. https://www.uniprot.org/uniprotkb/P02786/entry
5. https://pubmed.ncbi.nlm.nih.gov/16271884/
6. https://www.ncbi.nlm.nih.gov/gene/7037
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC3288267/
8. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=7037
9. https://onlinelibrary.wiley.com/doi/10.1111/tra.70006?af=R
10. https://www.nature.com/articles/s12276-025-01436-x
11. https://www.uniprot.org/uniprotkb/A0A8V8TM46/entry
12. https://arxiv.org/pdf/2412.14131.pdf
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC498283/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC4783254/
15. https://www.rndsystems.com/resources/articles/soluble-transferrin-receptor-stfr
16. https://www.proteinatlas.org/ENSG00000072274-TFRC/tissue
17. https://ashpublications.org/blood/article/141/4/422/486971/Regulation-of-iron-homeostasis-by-hepatocyte-TfR1
18. https://www.mayocliniclabs.com/test-catalog/overview/84283
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC2840523/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC2673483/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC6175443/
22. https://www.nature.com/articles/s41467-019-09098-w
23. https://portlandpress.com/biochemj/article/373/1/145/43889/Evidence-for-the-interaction-of-the-hereditary
24. https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2018.01019/full
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC4036340/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC99597/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC401153/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC4786429/
29. https://www.nature.com/articles/s41392-023-01720-0
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC4931119/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC3459860/
32. https://en.wikipedia.org/wiki/Iron_response_element
33. https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2023.1176118/full
34. https://ashpublications.org/blood/article/140/10/1061/486472/Grab-and-go-transferrin-uptake-in-erythropoiesis
35. https://medlineplus.gov/genetics/condition/hereditary-hemochromatosis/
36. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1567216/full
37. https://pubmed.ncbi.nlm.nih.gov/33352721/
38. https://www.ncbi.nlm.nih.gov/books/NBK1349/
39. https://pubmed.ncbi.nlm.nih.gov/16510596/
40. https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi?INPUT_TYPE=live&SEQUENCE=NP_003225.2
41. https://g2p.broadinstitute.org/gene/TFRC
42. https://pubmed.ncbi.nlm.nih.gov/17160644/
43. https://www.ebi.ac.uk/merops/cgi-bin/pepsum?id=M28.972%3Btype%3DP
44. https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1002666
45. https://pubmed.ncbi.nlm.nih.gov/10531064/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC7412275/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC6512944/
48. https://www.rcsb.org/structure/1cx8
49. https://www.nature.com/articles/nature05539
50. https://www.science.org/doi/10.1126/sciimmunol.abq0178
51. https://www.pnas.org/doi/10.1073/pnas.0409719102
52. https://www.pnas.org/doi/10.1073/pnas.2207461120
53. https://pmc.ncbi.nlm.nih.gov/articles/PMC2134874/
54. https://pmc.ncbi.nlm.nih.gov/articles/PMC413385/
55. https://pmc.ncbi.nlm.nih.gov/articles/PMC3265927/
56. https://www.pnas.org/doi/10.1073/pnas.1105786108