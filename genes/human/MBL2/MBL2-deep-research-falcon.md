Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for GO Annotation Review

## Target

- Gene symbol: MBL2
- Organism: Homo sapiens

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q96TF9
Entry Name: MBL2_HUMAN
Gene Name: MBL2
Gene Synonyms: COLEC1 {ECO:0000303|PubMed:15145932}, MBL
Protein Name: Mannose-binding protein C
Organism: Homo sapiens (Human)
NCBI Taxonomy ID: 9606
Function: Calcium-dependent lectin, which acts as a pattern recognition receptor that initiates the lectin pathway of the complement system, a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system (PubMed:14515269, PubMed:22966085, PubMed:7634089, PubMed:9087411). Specifically recognizes and binds the mannose moiety of carbohydrates on the pathogen surface, activating the MASP1 serine protease and initiating the proteolytic cascade of the lectin complement pathway (PubMed:22966085, PubMed:2573758, PubMed:6643429, PubMed:8082295, PubMed:9087411). Upon SARS coronavirus-2/SARS-CoV-2 infection, activates the complement lectin pathway which leads to the inhibition SARS-CoV-2 infection and a reduction of the induced inflammatory response (PubMed:35102342). May bind DNA (PubMed:15145932).
Subcellular Location: Secreted
Subunit: (Microbial infection) Interacts with SARS coronavirus-2/SARS- CoV-2 Spike glycoprotein homotrimer; the interaction is calcium- dependent and modulated by Spike glycoprotein glycosylation state.
======================

## Research Objective

Prepare a comprehensive literature-backed research report for GO annotation review of the target gene.

Focus on:

1. The core biochemical activity of the gene product and any substrate specificity.
2. The activation or maturation mechanism of the protein, including proteolytic processing if relevant.
3. The best-supported subcellular localization and complexes where the active protein functions.
4. The strongest experimentally supported biological processes in the target organism, or in very close orthologs when transfer is justified.
5. Which annotations appear to reflect core function versus context-specific, pleiotropic, or over-extended roles.
6. Any evidence bearing on apoptosis, developmental cell death, neuronal roles, inflammatory signaling, pyroptosis, synaptic remodeling, protein processing, and localization to cytoplasm, cytosol, nucleus, or signaling complexes.

## Output Requirements

Structure the report as:

1. Executive summary
2. Molecular function
3. Biological process roles
4. Cellular localization and complexes
5. Annotation-risk assessment
6. Key literature

Use citations for all substantive claims.


# Research Report: MBL2 (Mannose-Binding Protein C, Homo sapiens)

## 1. Executive Summary
Mannose-binding lectin 2 (MBL2) encodes a secreted collectin that serves as a principal pattern-recognition molecule in the human innate immune system, mediates complement lectin pathway activation, and contributes to the opsonic clearance of pathogens. MBL2 forms higher-order oligomeric complexes, binds carbohydrates in a calcium-dependent manner with defined substrate specificity, and interacts with MASP proteases to initiate downstream complement activation. The predominant subcellular localization is the extracellular compartment (serum/plasma), with biosynthesis occurring in hepatocytes. The core biological roles—complement activation and innate immune defense—are strongly supported, whereas apoptosis-related, developmental, or neuronal roles are unsupported or context-specific. The following sections detail molecular functions, biological processes, localization, annotation risks, and reference literature, supported by comprehensive tables and current evidence.

## 2. Molecular Function
| Aspect | Summary for human MBL2 protein | Evidence / notes | Citation |
|---|---|---|---|
| Core biochemical activity | Secreted soluble pattern-recognition lectin that binds carbohydrates in a **calcium-dependent** manner and initiates the **lectin pathway of complement** after target recognition | MBL is described as a circulating host-defense protein and collectin whose CRDs require calcium; target binding triggers complement activation through associated MASPs | (takahashi2006themannosebindinglectin pages 1-2, jack2001mannose‐bindinglectintargeting pages 1-2, dobo2024thelectinpathway pages 1-2) |
| Substrate specificity | Recognizes microbial or exposed glycans containing **D-mannose, N-acetylglucosamine, L-fucose, and glucose**; discriminates against **D-galactose** | Binding depends on coordination to the 3′ and 4′ hydroxyls of suitable sugars in the pyranose ring; recent lectin-pathway reviews also summarize recognition of carbohydrate-based ligands on pathogens | (jack2001mannose‐bindinglectintargeting pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Domain structure | Each polypeptide contains an **N-terminal cysteine-rich region**, **collagen-like domain**, **α-helical neck/coiled-coil region**, and **C-terminal C-type carbohydrate-recognition domain (CRD)** | This architecture underlies trimer formation, ligand recognition, and MASP binding through the collagen-like stalk | (larsen2004diseaseassociatedmutationsin pages 1-2, takahashi2006themannosebindinglectin pages 1-2, cedzynski2023collectinsandficolins pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Higher-order assembly / oligomerization | Functional MBL circulates as **multimers of homotrimers**; reported oligomeric species include **trimers, tetramers, and larger higher-order oligomers/hexamers**, with full activity requiring higher-order assemblies | Human serum contains multiple oligomeric forms; wild-type recombinant human MBL formed covalently linked higher oligomers of ~300–450 kDa corresponding to ~12–18 chains (4–6 structural units). Variant alleles impair oligomerization and reduce ligand binding/complement activation | (takahashi2006themannosebindinglectin pages 1-2, jack2001mannose‐bindinglectintargeting pages 1-2, larsen2004diseaseassociatedmutationsin pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Structural basis of oligomerization | The **collagen-like Gly-X-Y repeats** and N-terminal region are critical for correct multimer assembly | Disease-associated mutations in the collagenous region disrupt higher-order oligomerization, lowering ligand binding and downstream complement activity | (larsen2004diseaseassociatedmutationsin pages 1-2) |
| Key interacting partners: MASPs | Forms complexes with **MASP-1, MASP-2, and MASP-3**; upon ligand binding, associated proteases become activated to drive lectin-pathway signaling | Recent review: PRM–MASP complexes target lectin-pathway activation; MASP-1 autoactivation and MASP-2 activation/cleavage of C4 and C2 are highlighted in current and foundational reviews | (dobo2024thelectinpathway pages 1-2, cedzynski2023collectinsandficolins pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Key interacting partners: ficolins / lectin-pathway PRMs | MBL acts in the same lectin-pathway recognition module as **ficolins** and other collectins; these PRMs share MASP-associated complement activation logic rather than being obligate direct binding partners of MBL itself | Reviews group MBL and ficolins as topologically/functionally related lectin-pathway PRMs that complex with MASPs and initiate complement on pathogen surfaces | (dobo2024thelectinpathway pages 1-2, cedzynski2023collectinsandficolins pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Key interacting partners: calreticulin | Experimental support exists for MBL-mediated **opsonophagocytosis via cell-surface calreticulin** in vertebrate systems | Direct calreticulin interaction was shown in an early vertebrate model, supporting an evolutionarily conserved opsonic role; this is supportive but not primary human MBL2 complement-core evidence | (mu2020mannosebindinglectinpossesses pages 1-2) |
| Biological output most directly linked to molecular function | **Complement activation, opsonization/agglutination, and promotion of phagocytic clearance** of pathogens; can also recognize altered-self targets such as apoptotic cells | MBL binding to microbes activates purified C4 and supports opsonophagocytosis; additional literature supports binding to apoptotic cells and uptake by dendritic cells/macrophages | (jack2001mannose‐bindinglectintargeting pages 1-2, nauta2004opsonizationwithc1q pages 1-2, takahashi2006themannosebindinglectin pages 1-2) |


*Table: This table summarizes the best-supported molecular properties of human MBL2, including carbohydrate-binding activity, domain organization, oligomerization, and principal functional partners. It is useful for distinguishing core complement-related functions from broader or less direct interaction claims.*

## 3. Biological Process Roles
| Process / candidate annotation | Category | Evidence summary | Strength of evidence | Annotation risk | GO review recommendation | Citation |
|---|---|---|---|---|---|---|
| Lectin pathway of complement activation | Core / well-supported | MBL is a lectin-pathway pattern-recognition molecule that complexes with MASPs; upon ligand binding, MASP activation triggers cleavage of C4 and C2 and initiates complement cascade | Strong | Low | Keep as core process annotation | (dobo2024thelectinpathway pages 1-2, cedzynski2023collectinsandficolins pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Complement activation, lectin pathway | Core / well-supported | Recent and foundational reviews consistently describe MBL as a principal initiator of lectin-pathway complement activation in humans | Strong | Low | Keep | (dobo2024thelectinpathway pages 1-2, takahashi2006themannosebindinglectin pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Innate immune response / host defense against microbes | Core / well-supported | MBL is a circulating innate immune pattern-recognition molecule that recognizes microbial glycans and contributes to early host defense | Strong | Low | Keep, but prefer specific child terms where possible | (takahashi2006themannosebindinglectin pages 1-2, jack2001mannose‐bindinglectintargeting pages 1-2, cedzynski2023collectinsandficolins pages 1-2) |
| Pathogen recognition | Core / well-supported | MBL binds repeating sugar arrays on microbial surfaces and viral glycans, including SARS-CoV-2 spike glycans | Strong | Low | Keep as recognition-related process if supported by ontology term mapping | (jack2001mannose‐bindinglectintargeting pages 1-2, andrade2024highproductionmbl2 pages 1-2, bayarriolmos2024unravelingtheimpact pages 1-2) |
| Opsonization | Core / well-supported | MBL binding promotes complement deposition and microbial targeting for clearance; reviews explicitly frame MBL as an opsonic molecule | Strong | Low | Keep | (jack2001mannose‐bindinglectintargeting pages 1-2, mu2020mannosebindinglectinpossesses pages 1-2, nauta2004opsonizationwithc1q pages 1-2) |
| Opsonophagocytosis / promotion of phagocytic clearance | Core to near-core, but sometimes context-dependent | Strong support exists that MBL enhances phagocytic uptake of targets, including pathogens and apoptotic cells, though some direct mechanistic work is outside human systems | Moderate to strong | Low-Medium | Keep with evidence-based caution; prefer when direct target-clearance evidence is available | (jack2001mannose‐bindinglectintargeting pages 1-2, mu2020mannosebindinglectinpossesses pages 1-2, nauta2004opsonizationwithc1q pages 1-2) |
| Agglutination of microbes | Supported but narrower | MBL can agglutinate microbial targets; strong mechanistic support exists, but this may be narrower than most core GO biological process annotations | Moderate | Medium | Use only if specific experimental support is desired | (mu2020mannosebindinglectinpossesses pages 1-2, jack2001mannose‐bindinglectintargeting pages 1-2) |
| Apoptotic cell clearance | Context-specific | MBL binds apoptotic cells and enhances their uptake by dendritic cells/macrophages; evidence supports a role, but this is not as central or universally established as complement activation | Moderate | Medium | Accept only as non-core/context-dependent annotation | (nauta2004opsonizationwithc1q pages 1-2, takahashi2006themannosebindinglectin pages 1-2) |
| Clearance of altered self / dead cell-derived material | Context-specific | Reviews note recognition of altered-self antigens, apoptotic cells, and free DNA, suggesting broader homeostatic clearance roles | Moderate | Medium | Use cautiously; ensure direct evidence matches annotation specificity | (takahashi2006themannosebindinglectin pages 1-2, nauta2004opsonizationwithc1q pages 1-2) |
| Modulation of inflammatory response | Context-specific | MBL has been described as modulating inflammation, and apoptotic-cell uptake studies suggest immunomodulatory effects; however, effects are context-dependent and often indirect | Moderate | Medium | Keep only with narrow, evidence-matched wording | (takahashi2006themannosebindinglectin pages 1-2, nauta2004opsonizationwithc1q pages 1-2, andrade2024highproductionmbl2 pages 1-2) |
| Antiviral defense against SARS-CoV-2 | Context-specific but increasingly supported | MBL binds SARS-CoV-2 spike, activates lectin pathway, and is associated with antiviral effects in experimental and genetic studies; still pathogen-context-specific rather than universal core annotation | Moderate to strong | Medium | Consider as context-specific host defense annotation, not replacement for core complement roles | (andrade2024highproductionmbl2 pages 1-2, bayarriolmos2024unravelingtheimpact pages 1-2) |
| Developmental process / embryonic development | Unsupported or questionable for MBL2 specifically | Recent lectin-pathway reviews mention moonlighting developmental roles for certain lectin-pathway components, but not strong direct evidence that human MBL2 itself has a core developmental function | Weak | High | Avoid for MBL2 unless direct species-specific evidence is provided | (dobo2024thelectinpathway pages 1-2) |
| Neuronal function / synaptic remodeling | Unsupported or questionable | No direct evidence identified in retrieved MBL2 literature supporting neuronal or synaptic roles in human MBL2 | Weak / absent | High | Do not annotate | (dobo2024thelectinpathway pages 1-2, takahashi2006themannosebindinglectin pages 1-2) |
| Pyroptosis | Unsupported or questionable | No direct evidence identified that MBL2 itself executes or specifically regulates pyroptosis; inflammatory literature mentions pyroptosis broadly in infection contexts but not as a core MBL2 process | Weak / absent | High | Do not annotate | (andrade2024highproductionmbl2 pages 1-2, bayarriolmos2024unravelingtheimpact pages 1-2) |
| Apoptosis / developmental cell death as direct effector | Unsupported or over-extended | MBL2 may recognize apoptotic cells for clearance, but this is distinct from directly causing apoptosis or mediating developmental cell death | Weak for direct role | High | Do not annotate to apoptosis/cell death execution terms | (nauta2004opsonizationwithc1q pages 1-2, takahashi2006themannosebindinglectin pages 1-2) |
| Cytoplasm localization | Unsupported or questionable | Human MBL2 is synthesized for secretion and functions extracellularly in serum/plasma and complement complexes, not as a cytoplasmic effector | Strong evidence against as active-site localization | High | Do not annotate localization to cytoplasm | (zhou2016hepatocytesakey pages 1-2, takahashi2006themannosebindinglectin pages 1-2) |
| Cytosol localization | Unsupported or questionable | Active MBL2 is a secreted extracellular protein; cytosolic localization is not supported for mature functional protein | Strong evidence against | High | Do not annotate | (zhou2016hepatocytesakey pages 1-2, takahashi2006themannosebindinglectin pages 1-2) |
| Nuclear localization | Unsupported or questionable | No retrieved evidence supports nuclear localization of human MBL2; reports instead emphasize secreted/circulating function | Weak / absent | High | Do not annotate | (takahashi2006themannosebindinglectin pages 1-2, zhou2016hepatocytesakey pages 1-2) |


*Table: This table summarizes biological process candidates for human MBL2 and separates core complement-related functions from context-specific and over-extended annotations. It is useful for GO review because it highlights which terms are strongly supported versus which carry medium or high annotation risk.*

## 4. Cellular Localization and Complexes
| Entity / candidate annotation | Category | Summary | Evidence strength | Annotation risk | GO review recommendation | Citation |
|---|---|---|---|---|---|---|
| Secreted | Well-supported localization | Mature human MBL2 is a soluble secreted collectin released into circulation and functioning as an extracellular pattern-recognition molecule | Strong | Low | Keep as core cellular component/localization annotation | (takahashi2006themannosebindinglectin pages 1-2, zhou2016hepatocytesakey pages 1-2) |
| Extracellular space | Well-supported localization | MBL2 acts outside cells in the fluid phase, recognizing microbial and altered-self glycans and initiating lectin-pathway complement activation | Strong | Low | Keep | (dobo2024thelectinpathway pages 1-2, takahashi2006themannosebindinglectin pages 1-2, cedzynski2023collectinsandficolins pages 1-2) |
| Blood plasma / serum | Well-supported localization | Human MBL2 circulates in serum/plasma as oligomeric multimers and complement-activating complexes | Strong | Low | Keep with plasma/serum-compatible extracellular term if available | (takahashi2006themannosebindinglectin pages 1-2, jack2001mannose‐bindinglectintargeting pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Hepatocyte secretory pathway | Synthesis location | The liver is the major source of MBL synthesis; hepatocytes produce and secrete MBL as an innate immune plasma protein | Strong | Low-Medium | Appropriate for biosynthetic context, but distinguish synthesis site from mature functional location | (takahashi2006themannosebindinglectin pages 1-2, zhou2016hepatocytesakey pages 1-2) |
| Endoplasmic reticulum / secretory lumen in hepatocytes | Synthesis location (inferred) | Because MBL2 is synthesized and secreted by hepatocytes, it necessarily traverses the canonical ER-Golgi secretory pathway; this is a biosynthetic inference rather than a direct mature localization claim | Moderate | Medium | Use cautiously; better as pathway/biogenesis context than primary steady-state location of active protein | (takahashi2006themannosebindinglectin pages 1-2, zhou2016hepatocytesakey pages 1-2) |
| MBL2-MASP-1 complex | Well-supported protein complex | MBL forms calcium-dependent lectin-pathway complexes with MASP-1; MASP-1 contributes to early protease activation in lectin-pathway initiation | Strong | Low | Keep as lectin-pathway complex association | (dobo2024thelectinpathway pages 1-2, cedzynski2023collectinsandficolins pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| MBL2-MASP-2 complex | Well-supported protein complex | MBL associates with MASP-2, the key protease responsible for cleavage of C4 and C2 after lectin-pathway target recognition | Strong | Low | Keep as core functional complex | (dobo2024thelectinpathway pages 1-2, jack2001mannose‐bindinglectintargeting pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| MBL2-MASP-3 complex | Supported protein complex | MBL can associate with MASP-3 as part of lectin-pathway recognition complexes, although MASP-3 has less direct role in canonical C4/C2 cleavage than MASP-2 | Strong | Low-Medium | Keep if complex membership is being annotated; avoid overstating direct catalytic role in core lectin initiation | (dobo2024thelectinpathway pages 1-2, cedzynski2023collectinsandficolins pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| MBL2-containing lectin-pathway recognition complex | Well-supported protein complex | MBL functions as a pattern-recognition molecule in oligomeric complexes with MASPs in the extracellular complement system | Strong | Low | Keep as high-confidence complex-level annotation | (dobo2024thelectinpathway pages 1-2, cedzynski2023collectinsandficolins pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2) |
| Cytoplasm | Unsupported localization | Retrieved evidence supports secretion and extracellular function, not cytoplasmic residence of the mature active protein | Strong evidence against | High | Do not annotate | (takahashi2006themannosebindinglectin pages 1-2, zhou2016hepatocytesakey pages 1-2) |
| Cytosol | Unsupported localization | No evidence in the retrieved literature supports cytosolic localization of functional mature MBL2; its biology is secretory/extracellular | Strong evidence against | High | Do not annotate | (takahashi2006themannosebindinglectin pages 1-2, zhou2016hepatocytesakey pages 1-2) |
| Nucleus | Unsupported localization | No direct evidence identified for nuclear localization; published evidence instead emphasizes circulating extracellular function | Weak / absent support | High | Do not annotate | (takahashi2006themannosebindinglectin pages 1-2, zhou2016hepatocytesakey pages 1-2) |
| Synapse / synaptic compartment | Unsupported localization | No retrieved evidence supports localization of human MBL2 to synapses or neural subcellular compartments | Weak / absent support | High | Do not annotate | (dobo2024thelectinpathway pages 1-2, takahashi2006themannosebindinglectin pages 1-2) |


*Table: This table summarizes the best-supported cellular localizations and protein complexes for human MBL2, while distinguishing biosynthetic context from mature functional localization. It also flags unsupported intracellular and synaptic annotations that present high GO annotation risk.*

## 5. Annotation-risk Assessment
- **Core functional annotations** such as extracellular localization, complement lectin pathway activation, and innate immune recognition/opsonization are strongly supported by structural, genetic, and functional studies (takahashi2006themannosebindinglectin pages 1-2, jack2001mannose‐bindinglectintargeting pages 1-2, dobo2024thelectinpathway pages 1-2, yongqing2012mannosebindinglectinserine pages 1-2).
- **Apoptotic cell clearance and inflammation modulation** are context-dependent, supported but with a medium annotation risk, and may be annotated as secondary functions (nauta2004opsonizationwithc1q pages 1-2).
- **Annotations for roles in apoptosis execution, pyroptosis, developmental cell death, neuron/synapse, or cytoplasm/cytosol/nucleus localization** are not supported and present a high annotation risk; these should not be included without new evidence (zhou2016hepatocytesakey pages 1-2).

## 6. Key Literature
- Dobó J, Kocsis A, Farkas B, et al. (2024). The Lectin Pathway of the Complement System—Activation, Regulation, Disease Connections and Interplay with Other (Proteolytic) Systems. Int J Mol Sci 25:1566. https://doi.org/10.3390/ijms25031566 (dobo2024thelectinpathway pages 1-2)
- Takahashi K, Ip WKE, Michelow IC, Ezekowitz RAB. (2006). The mannose-binding lectin: a prototypic pattern recognition molecule. Curr Opin Immunol 18:16–23. https://doi.org/10.1016/j.coi.2005.11.014 (takahashi2006themannosebindinglectin pages 1-2)
- Jack DL, Klein NJ, Turner MW. (2001). Mannose-binding lectin: targeting the microbial world for complement attack and opsonophagocytosis. Immunol Rev 180:86–99. https://doi.org/10.1034/j.1600-065x.2001.1800108.x (jack2001mannose‐bindinglectintargeting pages 1-2)
- Larsen F, Madsen HO, Sim RB, Koch C, Garred P. (2004). Disease-associated Mutations in Human Mannose-binding Lectin Compromise Oligomerization and Activity of the Final Protein. J Biol Chem 279:21302–21311. https://doi.org/10.1074/jbc.m400520200 (larsen2004diseaseassociatedmutationsin pages 1-2)
- Cedzyński M, Świerzko AS. (2023). Collectins and ficolins in neonatal health and disease. Front Immunol 14:1328658. https://doi.org/10.3389/fimmu.2023.1328658 (cedzynski2023collectinsandficolins pages 1-2)
- Yongqing T, Drentin N, Duncan RC, Wijeyewickrema LC, Pike RN. (2012). Mannose-binding lectin serine proteases and associated proteins of the lectin pathway of complement: Two genes, five proteins and many functions? Biochim Biophys Acta 1824:253-262. https://doi.org/10.1016/j.bbapap.2011.05.021 (yongqing2012mannosebindinglectinserine pages 1-2)
- Mu L, Yin X, Wu H, et al. (2020). Mannose-Binding Lectin Possesses Agglutination Activity and Promotes Opsonophagocytosis of Macrophages with Calreticulin Interaction in an Early Vertebrate. J Immunol 205:3443-3455. https://doi.org/10.4049/jimmunol.2000256 (mu2020mannosebindinglectinpossesses pages 1-2)
- Zhou Z, Xu MJ, Gao B. (2016). Hepatocytes: a key cell type for innate immunity. Cell Mol Immunol 13:301-315. https://doi.org/10.1038/cmi.2015.97 (zhou2016hepatocytesakey pages 1-2)
- Andrade LV, de Souza Sá MV, Vasconcelos B, et al. (2024). High production MBL2 polymorphisms protect against COVID-19 complications in critically ill patients: A retrospective cohort study. Heliyon 10:e23670. https://doi.org/10.1016/j.heliyon.2023.e23670 (andrade2024highproductionmbl2 pages 1-2)
- Bayarri-Olmos R, Sutta A, Rosbjerg A, et al. (2024). Unraveling the impact of SARS-CoV-2 mutations on immunity: insights from innate immune recognition to antibody and T cell responses. Front Immunol 15:1412873. https://doi.org/10.3389/fimmu.2024.1412873 (bayarriolmos2024unravelingtheimpact pages 1-2)
- Nauta AJ, Castellano G, Xu W, et al. (2004). Opsonization with C1q and Mannose-Binding Lectin Targets Apoptotic Cells to Dendritic Cells. J Immunol 173:3044-3050. https://doi.org/10.4049/jimmunol.173.5.3044 (nauta2004opsonizationwithc1q pages 1-2)

This report is based on the best available evidence from 2023-2024 and foundational studies, with each major claim directly supported by cited sources. Artifact tables provide systematic support for the key annotation decisions required for GO review.

References

1. (takahashi2006themannosebindinglectin pages 1-2): Kazue Takahashi, WK Eddie Ip, Ian C Michelow, and R Alan B Ezekowitz. The mannose-binding lectin: a prototypic pattern recognition molecule. Current Opinion in Immunology, 18:16-23, Feb 2006. URL: https://doi.org/10.1016/j.coi.2005.11.014, doi:10.1016/j.coi.2005.11.014. This article has 279 citations and is from a peer-reviewed journal.

2. (jack2001mannose‐bindinglectintargeting pages 1-2): Dominic L. Jack, Nigel J. Klein, and Malcolm W. Turner. Mannose‐binding lectin: targeting the microbial world for complement attack and opsonophagocytosis. Immunological Reviews, 180:86-99, Apr 2001. URL: https://doi.org/10.1034/j.1600-065x.2001.1800108.x, doi:10.1034/j.1600-065x.2001.1800108.x. This article has 440 citations and is from a domain leading peer-reviewed journal.

3. (dobo2024thelectinpathway pages 1-2): József Dobó, Andrea Kocsis, Bence Farkas, Flóra Demeter, László Cervenak, and Péter Gál. The lectin pathway of the complement system—activation, regulation, disease connections and interplay with other (proteolytic) systems. International Journal of Molecular Sciences, 25:1566, Jan 2024. URL: https://doi.org/10.3390/ijms25031566, doi:10.3390/ijms25031566. This article has 98 citations.

4. (yongqing2012mannosebindinglectinserine pages 1-2): Tang Yongqing, Nicole Drentin, Renee C. Duncan, Lakshmi C. Wijeyewickrema, and Robert N. Pike. Mannose-binding lectin serine proteases and associated proteins of the lectin pathway of complement: two genes, five proteins and many functions? Biochimica et biophysica acta, 1824 1:253-62, Jan 2012. URL: https://doi.org/10.1016/j.bbapap.2011.05.021, doi:10.1016/j.bbapap.2011.05.021. This article has 130 citations.

5. (larsen2004diseaseassociatedmutationsin pages 1-2): Flemming Larsen, Hans O. Madsen, Robert B. Sim, Claus Koch, and Peter Garred. Disease-associated mutations in human mannose-binding lectin compromise oligomerization and activity of the final protein*. Journal of Biological Chemistry, 279:21302-21311, May 2004. URL: https://doi.org/10.1074/jbc.m400520200, doi:10.1074/jbc.m400520200. This article has 273 citations and is from a domain leading peer-reviewed journal.

6. (cedzynski2023collectinsandficolins pages 1-2): Maciej Cedzyński and Anna S. Świerzko. Collectins and ficolins in neonatal health and disease. Frontiers in Immunology, Dec 2023. URL: https://doi.org/10.3389/fimmu.2023.1328658, doi:10.3389/fimmu.2023.1328658. This article has 17 citations and is from a peer-reviewed journal.

7. (mu2020mannosebindinglectinpossesses pages 1-2): Liangliang Mu, Xiaoxue Yin, Hairong Wu, Yang Lei, Kailiang Han, Jinfeng Mo, Zheng Guo, Jun Li, and Jianmin Ye. Mannose-binding lectin possesses agglutination activity and promotes opsonophagocytosis of macrophages with calreticulin interaction in an early vertebrate. The Journal of Immunology, 205:3443-3455, Dec 2020. URL: https://doi.org/10.4049/jimmunol.2000256, doi:10.4049/jimmunol.2000256. This article has 41 citations.

8. (nauta2004opsonizationwithc1q pages 1-2): Alma J. Nauta, Giuseppe Castellano, Wei Xu, Andrea M. Woltman, Maria C. Borrias, Mohamed R. Daha, Cees van Kooten, and Anja Roos. Opsonization with c1q and mannose-binding lectin targets apoptotic cells to dendritic cells1. The Journal of Immunology, 173:3044-3050, Sep 2004. URL: https://doi.org/10.4049/jimmunol.173.5.3044, doi:10.4049/jimmunol.173.5.3044. This article has 322 citations.

9. (andrade2024highproductionmbl2 pages 1-2): Lorena Viana de Andrade, Mirela Vanessa de Souza Sá, Beatriz Vasconcelos, Luydson Richardson Silva Vasconcelos, Ricardo Khouri, Carlos Dornels Freire de Souza, Anderson da Costa Armstrong, and Rodrigo Feliciano do Carmo. High production mbl2 polymorphisms protect against covid-19 complications in critically ill patients: a retrospective cohort study. Heliyon, 10:e23670, Jan 2024. URL: https://doi.org/10.1016/j.heliyon.2023.e23670, doi:10.1016/j.heliyon.2023.e23670. This article has 8 citations.

10. (bayarriolmos2024unravelingtheimpact pages 1-2): Rafael Bayarri-Olmos, Adrian Sutta, Anne Rosbjerg, Mie Mandal Mortensen, Charlotte Helgstrand, Per Franklin Nielsen, Laura Pérez-Alós, Beatriz González-García, Laust Bruun Johnsen, Finn Matthiesen, Thomas Egebjerg, Cecilie Bo Hansen, Alessandro Sette, Alba Grifoni, Ricardo da Silva Antunes, and Peter Garred. Unraveling the impact of sars-cov-2 mutations on immunity: insights from innate immune recognition to antibody and t cell responses. Frontiers in Immunology, Dec 2024. URL: https://doi.org/10.3389/fimmu.2024.1412873, doi:10.3389/fimmu.2024.1412873. This article has 4 citations and is from a peer-reviewed journal.

11. (zhou2016hepatocytesakey pages 1-2): Zhou Zhou, Ming-Jiang Xu, and Bin Gao. Hepatocytes: a key cell type for innate immunity. Cellular and Molecular Immunology, 13:301-315, Dec 2016. URL: https://doi.org/10.1038/cmi.2015.97, doi:10.1038/cmi.2015.97. This article has 635 citations and is from a peer-reviewed journal.