---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T23:11:25.743477'
end_time: '2026-01-23T23:20:59.155944'
duration_seconds: 573.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: THBS4
  gene_symbol: THBS4
  uniprot_accession: P35443
  protein_description: 'RecName: Full=Thrombospondin-4; Flags: Precursor;'
  gene_info: Name=THBS4; Synonyms=TSP4;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the thrombospondin family. .
  protein_domains: ConA-like_dom_sf. (IPR013320); EGF-like_Ca-bd_dom. (IPR001881);
    EGF-like_dom. (IPR000742); EGF_Ca-bd_CS. (IPR018097); Thrombospondin_3-like_rpt.
    (IPR003367)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P35443
- **Protein Description:** RecName: Full=Thrombospondin-4; Flags: Precursor;
- **Gene Information:** Name=THBS4; Synonyms=TSP4;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the thrombospondin family. .
- **Key Domains:** ConA-like_dom_sf. (IPR013320); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_dom. (IPR000742); EGF_Ca-bd_CS. (IPR018097); Thrombospondin_3-like_rpt. (IPR003367)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "THBS4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'THBS4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **THBS4** (gene ID: THBS4, UniProt: P35443) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Comprehensive Research Report: Thrombospondin-4 (THBS4/TSP-4)

**Gene:** THBS4 (also known as TSP4)
**UniProt Accession:** P35443
**Organism:** Homo sapiens (Human)
**Protein Family:** Thrombospondin family (Subgroup B)

## 1. Introduction and Overview

Thrombospondin-4 (TSP-4, encoded by the THBS4 gene) is a secreted extracellular matrix (ECM) glycoprotein belonging to the thrombospondin family of calcium-binding proteins. According to PubMed, the thrombospondin family comprises five members in vertebrates (TSP-1 through TSP-5), which are divided into two subgroups based on their oligomeric structure: subgroup A (TSP-1 and TSP-2) form trimers, while subgroup B (TSP-3, TSP-4, and TSP-5/COMP) form pentamers [adams-2004-thrombospondins-review-abstract]. TSP-4 has emerged as a multifunctional protein with roles extending far beyond simple ECM structural support, participating in tissue remodeling, cell-matrix interactions, synaptogenesis, angiogenesis, and intracellular stress responses [genaro-2023-tsp4-review-abstract].

The multidomain, pentameric structure of TSP-4 enables its interactions with numerous ECM components, cell surface receptors, and signaling molecules. This versatility allows TSP-4 to modulate diverse physiological processes including cell-cell and cell-ECM interactions, cell migration, proliferation, tissue remodeling, and neural synapse formation. Maladaptation of these processes in response to pathological insults can contribute to the development of cardiovascular diseases, skeletal disorders, tumor progression, and neurological disorders including chronic pain states [genaro-2023-tsp4-review-abstract].

## 2. Protein Structure and Domain Organization

TSP-4 exhibits a characteristic pentameric quaternary structure, which is essential for its biological functions. Electron microscopy studies have revealed that uncleaved TSP-4 appears as a large central particle with five smaller globules attached by elongated linker regions [narouz-ott-2000-binding-abstract]. The domain architecture of each TSP-4 monomer includes several functionally distinct regions.

### 2.1 Domain Organization

The TSP-4 monomer contains the following domains from N- to C-terminus:

1. **Signal Peptide**: Directs secretion of the nascent protein.

2. **N-terminal Heparin-Binding Domain**: This domain can be cleaved proteolytically from the rest of the molecule during post-translational processing [narouz-ott-2000-binding-abstract].

3. **Coiled-Coil Domain (CCD)**: Contains a highly conserved CQAC (Cys-Gln-Ala-Cys) motif that is critical for pentamerization through inter-subunit disulfide bond formation. Studies in zebrafish have demonstrated that mutation of this motif (CQAC→SQAS) prevents pentamer formation and abolishes TSP-4 localization to myotendinous junctions, demonstrating that pentamerization is essential for proper function [subramanian-2014-mtj-fulltext].

4. **EGF-like Domains**: These calcium-binding domains are critical for interaction with the voltage-gated calcium channel α2δ1 subunit (Cavα2δ1). The EGF-like domain has been identified as the key determinant for TSP-4's synaptogenic and pronociceptive activities. Intrathecal injection of TSP-4 fragment proteins containing only the EGF-like domain is sufficient to induce behavioral hypersensitivity similar to full-length TSP-4 [park-2018-egf-domain-abstract].

5. **Type 3 Thrombospondin Repeats**: These domains bind to the ER-luminal domain of activating transcription factor 6α (ATF6α), promoting its nuclear shuttling during endoplasmic reticulum stress responses [lynch-2012-er-stress-abstract].

6. **C-terminal Lectin-like (ConA-like) Domain**: The C-terminal domains mediate binding to collagens and other ECM proteins. The binding to collagenous proteins is enhanced by Zn2+, while binding to non-collagenous proteins is zinc-independent [narouz-ott-2000-binding-abstract].

### 2.2 Calcium Binding and Disease-Associated Polymorphisms

Calcium binding is critical for the structure and function of TSP family members. A well-characterized polymorphism in TSP-4, A387P, has been associated with premature cardiovascular disease. This amino acid substitution creates an additional calcium-binding site absent in the wild-type A387 form, potentially altering the protein's conformational dynamics and functional properties [stenina-2005-polymorphism-abstract].

## 3. Expression Patterns and Tissue Distribution

TSP-4 exhibits distinct expression patterns that differ from other thrombospondin family members. It is abundantly expressed in several tissues, with particularly high levels in:

- **Tendon**: TSP-4 is a major component of tendon ECM, where it regulates collagen fibril organization and size [frolova-2014-muscle-tendon-abstract].

- **Skeletal Muscle**: Higher levels of TSP-4 protein are associated with the microvasculature of red skeletal muscle with high oxidative metabolism. TSP-4 deficiency results in smaller soleus muscles and reduced grip strength [frolova-2014-muscle-tendon-abstract].

- **Heart**: TSP-4 expression increases dramatically in hypertrophic and failing hearts in both rodent models and humans [frolova-2012-cardiac-abstract].

- **Nervous System**: TSP-4 is expressed in neurons and astrocytes, and its levels increase in spinal cord and dorsal root ganglia following peripheral nerve injury [park-2016-pain-abstract].

- **Cartilage**: TSP-4 is a component of the collagen IX interactome in cartilage, where it contributes to matrix organization.

- **Blood**: TSP-4 is enriched in serum from young mice compared to old mice, suggesting a potential role in age-related physiological processes [gan-2019-synaptogenesis-abstract].

## 4. Subcellular Localization and Extracellular Functions

### 4.1 Extracellular Matrix Localization

As a secreted protein, TSP-4 is primarily localized to the extracellular matrix, where it serves as a scaffold for organizing other ECM components. At myotendinous junctions (MTJs), TSP-4 localizes to basement membranes and is required for proper laminin localization and integrin signaling activation [subramanian-2014-mtj-fulltext].

### 4.2 Intracellular Localization

A paradigm-shifting discovery revealed that TSP-4 also functions intracellularly within the endoplasmic reticulum (ER). Lynch et al. demonstrated that TSP-4 can function as an ER-resident effector of an adaptive ER stress response. In this context, TSP-4 binds to ATF6α via its type-3 repeat domain to promote ATF6α nuclear shuttling and activation of protective ER stress response genes [lynch-2012-er-stress-abstract].

## 5. Primary Molecular Functions

### 5.1 ECM Scaffold and Organizer

The primary function of TSP-4 is to serve as a scaffold protein that organizes the ECM. In its pentameric form, TSP-4 binds multiple ECM proteins including:

- **Collagens (I, II, V, VI)**: Major binding sites are located in the N- and C-terminal telopeptide regions of collagen I [narouz-ott-2000-binding-abstract].
- **Laminins**: Essential for proper laminin localization at MTJs [subramanian-2014-mtj-fulltext].
- **Fibronectin**: Binds through C-terminal domains.
- **Proteoglycans**: Affects glycosaminoglycan modifications in skeletal muscle [frolova-2014-muscle-tendon-abstract].

TSP-4 deficiency in mice leads to significantly larger tendon collagen fibrils, indicating its role in regulating fibril assembly and size [frolova-2014-muscle-tendon-abstract].

### 5.2 Integrin Signaling Ligand

TSP-4 contains a non-canonical KGD (Lys-Gly-Asp) integrin-binding motif, rather than the classical RGD sequence. This motif is required for TSP-4's ability to activate integrin signaling in muscle cells. Mutation of KGD to KGE abolishes TSP-4's ability to rescue muscle attachment defects, confirming the functional importance of this integrin-binding activity [subramanian-2014-mtj-fulltext]. TSP-4 is required for proper phosphorylation and activation of focal adhesion kinase (FAK) at myotendinous junctions.

### 5.3 Synaptogenic Factor

TSP-4 promotes synapse formation through interaction with the voltage-gated calcium channel α2δ1 subunit (Cavα2δ1). This interaction leads to:

- Increased excitatory synaptogenesis between sensory and spinal cord neurons
- Elevated VGlut2 and PSD95-positive puncta (markers of excitatory synapses)
- Increased frequency of miniature excitatory post-synaptic currents
- Increased dendritic arborization and synapse numbers [park-2016-pain-abstract] [gan-2019-synaptogenesis-abstract]

The EGF-like domain of TSP-4 is the molecular determinant responsible for these synaptogenic effects [park-2018-egf-domain-abstract].

### 5.4 Regulation of Calcium Channels

TSP-4 differentially regulates voltage-gated calcium channel activity in sensory neurons:

- **Decreases** N-type and L-type (high-voltage-activated) calcium currents
- **Increases** T-type (low-voltage-activated) calcium currents

These opposing effects contribute to elevated excitability in sensory neurons and are blocked by gabapentin, which binds to the α2δ1 subunit [pan-2016-calcium-channels-abstract].

## 6. Biological Processes and Pathways

### 6.1 Myotendinous Junction Assembly

TSP-4 is essential for the development and maintenance of myotendinous junctions, where muscles attach to tendons. In zebrafish, TSP-4 (Tsp4b) depletion causes muscle detachment upon contraction due to defects in laminin localization and reduced integrin signaling. Remarkably, human TSP4 can rescue muscle attachments in TSP-4-deficient zebrafish, demonstrating evolutionary conservation of this function and suggesting therapeutic potential for tendon repair [subramanian-2014-mtj-fulltext].

### 6.2 Cardiac Remodeling and Protection

TSP-4 plays a complex role in cardiac physiology. Its expression increases dramatically in response to cardiac stress, including pressure overload and myocardial infarction. Studies using TSP-4 knockout mice reveal that:

- TSP-4 deficiency leads to increased fibrosis under pressure overload
- Increased interstitial collagen deposition occurs in the absence of TSP-4
- TSP-4 regulates inflammatory and fibrotic gene expression
- TSP-4 is protective against pathological cardiac remodeling [frolova-2012-cardiac-abstract]

Cardiac-specific TSP-4 overexpression protects from myocardial injury through activation of an adaptive ER stress response mediated by ATF6α [lynch-2012-er-stress-abstract].

### 6.3 Endoplasmic Reticulum Stress Response

TSP-4 participates in an intracellular protective pathway during tissue stress. Within the ER, TSP-4 binds to ATF6α and promotes its nuclear shuttling, leading to:

- Activation of adaptive ER stress response genes
- Expansion of ER volume and downstream secretory vesicles
- Enhanced protein folding and quality control capacity
- Protection against cardiac maladaptation [lynch-2012-er-stress-abstract]

This pathway represents an important intracellular function distinct from TSP-4's extracellular ECM roles.

### 6.4 Angiogenesis

TSP-4 mediates pro-angiogenic effects of TGF-β1 in endothelial cells. Unlike TSP-1 and TSP-2 which are anti-angiogenic, TSP-4 promotes:

- Endothelial cell adhesion and migration
- Vascular network formation
- Tumor angiogenesis

TGF-β1 upregulates TSP-4 in microvascular endothelial cells through SMAD3 signaling. This upregulation is post-transcriptional (not via increased mRNA) and is specific to microvascular endothelial cells [muppala-2017-angiogenesis-abstract].

### 6.5 Neuropathic Pain

Peripheral nerve injury induces increased TSP-4 expression in spinal cord and dorsal root ganglia. TSP-4 contributes to neuropathic pain through:

- Interaction with Cavα2δ1 on sensory afferent terminals
- Promotion of excitatory synaptogenesis
- Induction of central sensitization
- Modulation of calcium channel activity

Gabapentin, which binds to Cavα2δ1, blocks TSP-4-induced behavioral hypersensitivity, explaining part of gabapentin's mechanism of action in treating neuropathic pain [park-2016-pain-abstract].

## 7. Experimental Evidence and Methodology

The functions of TSP-4 have been established through multiple lines of experimental evidence:

### Genetic Approaches
- **Knockout mice (Thbs4-/-)**: Revealed roles in cardiac remodeling, tendon collagen organization, and muscle function [frolova-2012-cardiac-abstract] [frolova-2014-muscle-tendon-abstract]
- **Morpholino knockdown in zebrafish**: Demonstrated essential role in MTJ formation [subramanian-2014-mtj-fulltext]
- **Transgenic overexpression**: Cardiac-specific TSP-4 transgenic mice showed protection from injury [lynch-2012-er-stress-abstract]

### Biochemical Studies
- **Surface plasmon resonance and ELISA**: Characterized TSP-4 binding to ECM proteins [narouz-ott-2000-binding-abstract]
- **Electron microscopy**: Revealed pentameric structure
- **Co-immunoprecipitation**: Demonstrated TSP-4/Cavα2δ1 interaction [park-2016-pain-abstract]

### Functional Assays
- **Electrophysiology**: Documented effects on calcium currents and synaptic transmission [pan-2016-calcium-channels-abstract]
- **Cell culture**: Assessed effects on adhesion, migration, and proliferation
- **In vivo models**: Matrigel plug and tumor angiogenesis assays [muppala-2017-angiogenesis-abstract]

## 8. Disease Associations

### Cardiovascular Disease
The A387P polymorphism in TSP-4 has been associated with increased risk of coronary artery disease in some populations. TSP-4 expression increases in heart failure, where it may play both protective and pathological roles depending on context [stenina-2005-polymorphism-abstract].

### Muscular Dystrophy
TSP-4 levels are elevated in patients with Duchenne muscular dystrophy, though the functional significance remains under investigation.

### Chronic Pain
Upregulation of TSP-4 after nerve injury contributes to neuropathic pain development, making it a potential therapeutic target.

### Cancer
TSP-4 promotes tumor angiogenesis and is associated with cancer progression in several tumor types.

## 9. Open Questions

Several important questions remain regarding TSP-4 biology:

1. **What regulates TSP-4 transcription?** While TGF-β1 regulates TSP-4 at the post-transcriptional level, the transcriptional regulators of THBS4 expression remain poorly characterized.

2. **How does TSP-4 traffic between extracellular and intracellular compartments?** The mechanisms controlling whether TSP-4 is secreted or retained in the ER for ATF6α signaling are unclear.

3. **What is the therapeutic potential of TSP-4?** Given its ability to rescue muscle attachment defects across species, TSP-4 may have applications in tendon repair, but clinical development has not advanced.

4. **How do TSP-4 functions differ from TSP-5/COMP?** Both are pentameric and share structural similarities, but their distinct tissue distributions suggest non-redundant functions that warrant further investigation.

5. **What are the age-related changes in TSP-4 function?** The enrichment of TSP-4 in young blood and its synaptogenic properties suggest potential roles in cognitive aging.

6. **How does the A387P polymorphism alter TSP-4 function in vivo?** While calcium-binding changes have been documented biochemically, the physiological consequences remain incompletely understood.

## 10. References

1. **[genaro-2023-tsp4-review-abstract]** Genaro K, Luo ZD. Pathophysiological roles of thrombospondin-4 in disease development. Semin Cell Dev Biol. 2023;155(Pt B):66-73. PMID: 37391348. DOI: https://doi.org/10.1016/j.semcdb.2023.06.007

2. **[lynch-2012-er-stress-abstract]** Lynch JM, Maillet M, Vanhoutte D, et al. A thrombospondin-dependent pathway for a protective ER stress response. Cell. 2012;149(6):1257-68. PMID: 22682248. DOI: https://doi.org/10.1016/j.cell.2012.03.050

3. **[subramanian-2014-mtj-fulltext]** Subramanian A, Schilling TF. Thrombospondin-4 controls matrix assembly during development and repair of myotendinous junctions. eLife. 2014;3:e02372. PMID: 24941943. DOI: https://doi.org/10.7554/eLife.02372

4. **[frolova-2012-cardiac-abstract]** Frolova EG, Sopko N, Blech L, et al. Thrombospondin-4 regulates fibrosis and remodeling of the myocardium in response to pressure overload. FASEB J. 2012;26(6):2363-73. PMID: 22362893. DOI: https://doi.org/10.1096/fj.11-190728

5. **[park-2016-pain-abstract]** Park J, Yu YP, Zhou CY, et al. Central Mechanisms Mediating Thrombospondin-4-induced Pain States. J Biol Chem. 2016;291(25):13335-48. PMID: 27129212. DOI: https://doi.org/10.1074/jbc.M116.723478

6. **[narouz-ott-2000-binding-abstract]** Narouz-Ott L, Maurer P, Nitsche DP, Smyth N, Paulsson M. Thrombospondin-4 binds specifically to both collagenous and non-collagenous extracellular matrix proteins via its C-terminal domains. J Biol Chem. 2000;275(47):37110-7. PMID: 10956668. DOI: https://doi.org/10.1074/jbc.M007223200

7. **[muppala-2017-angiogenesis-abstract]** Muppala S, Xiao R, Krukovets I, et al. Thrombospondin-4 mediates TGF-β-induced angiogenesis. Oncogene. 2017;36(36):5189-5198. PMID: 28481870. DOI: https://doi.org/10.1038/onc.2017.140

8. **[gan-2019-synaptogenesis-abstract]** Gan KJ, Südhof TC. Specific factors in blood from young but not old mice directly promote synapse formation and NMDA-receptor recruitment. Proc Natl Acad Sci U S A. 2019;116(25):12524-12533. PMID: 31160442. DOI: https://doi.org/10.1073/pnas.1902672116

9. **[adams-2004-thrombospondins-review-abstract]** Adams JC, Lawler J. The thrombospondins. Int J Biochem Cell Biol. 2004;36(6):961-8. PMID: 15094109. DOI: https://doi.org/10.1016/j.biocel.2004.01.004

10. **[frolova-2014-muscle-tendon-abstract]** Frolova EG, Drazba J, Krukovets I, et al. Control of organization and function of muscle and tendon by thrombospondin-4. Matrix Biol. 2014;37:35-48. PMID: 24589453. DOI: https://doi.org/10.1016/j.matbio.2014.02.003

11. **[park-2018-egf-domain-abstract]** Park JF, Yu YP, Gong N, Trinh VN, Luo ZD. The EGF-LIKE domain of thrombospondin-4 is a key determinant in the development of pain states due to increased excitatory synaptogenesis. J Biol Chem. 2018;293(42):16453-16463. PMID: 30194282. DOI: https://doi.org/10.1074/jbc.RA118.003591

12. **[stenina-2005-polymorphism-abstract]** Stenina OI, Ustinov V, Krukovets I, et al. Polymorphisms A387P in thrombospondin-4 and N700S in thrombospondin-1 perturb calcium binding sites. FASEB J. 2005;19(13):1893-5. PMID: 16148025. DOI: https://doi.org/10.1096/fj.05-3712fje

13. **[pan-2016-calcium-channels-abstract]** Pan B, Guo Y, Wu HE, et al. Thrombospondin-4 divergently regulates voltage-gated Ca2+ channel subtypes in sensory neurons after nerve injury. Pain. 2016;157(9):2068-2080. PMID: 27168360. DOI: https://doi.org/10.1097/j.pain.0000000000000612


## Citations

1. adams-2004-thrombospondins-review-abstract.md
2. frolova-2012-cardiac-abstract.md
3. frolova-2014-muscle-tendon-abstract.md
4. gan-2019-synaptogenesis-abstract.md
5. genaro-2023-tsp4-review-abstract.md
6. lynch-2012-er-stress-abstract.md
7. muppala-2017-angiogenesis-abstract.md
8. narouz-ott-2000-binding-abstract.md
9. pan-2016-calcium-channels-abstract.md
10. park-2016-pain-abstract.md
11. park-2018-egf-domain-abstract.md
12. stenina-2005-polymorphism-abstract.md
13. subramanian-2014-mtj-fulltext.md