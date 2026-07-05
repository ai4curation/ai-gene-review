---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T13:10:46.951023'
end_time: '2026-07-05T13:25:20.571681'
duration_seconds: 873.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ASL
  gene_symbol: ASL
  uniprot_accession: P04424
  protein_description: 'RecName: Full=Argininosuccinate lyase {ECO:0000303|PubMed:3391281};
    Short=ASAL; EC=4.3.2.1 {ECO:0000269|PubMed:11747432, ECO:0000269|PubMed:11747433,
    ECO:0000269|PubMed:9045711}; AltName: Full=Arginosuccinase;'
  gene_info: Name=ASL;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the lyase 1 family. Argininosuccinate lyase
  protein_domains: Arg_succ_lyase_C. (IPR029419); Argininosuccinate_lyase. (IPR009049);
    Fumarase/histidase_N. (IPR024083); Fumarate_lyase_CS. (IPR020557); Fumarate_lyase_fam.
    (IPR000362)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ASL-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P04424
- **Protein Description:** RecName: Full=Argininosuccinate lyase {ECO:0000303|PubMed:3391281}; Short=ASAL; EC=4.3.2.1 {ECO:0000269|PubMed:11747432, ECO:0000269|PubMed:11747433, ECO:0000269|PubMed:9045711}; AltName: Full=Arginosuccinase;
- **Gene Information:** Name=ASL;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the lyase 1 family. Argininosuccinate lyase
- **Key Domains:** Arg_succ_lyase_C. (IPR029419); Argininosuccinate_lyase. (IPR009049); Fumarase/histidase_N. (IPR024083); Fumarate_lyase_CS. (IPR020557); Fumarate_lyase_fam. (IPR000362)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ASL" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ASL' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ASL** (gene ID: ASL, UniProt: P04424) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P04424
- **Protein Description:** RecName: Full=Argininosuccinate lyase {ECO:0000303|PubMed:3391281}; Short=ASAL; EC=4.3.2.1 {ECO:0000269|PubMed:11747432, ECO:0000269|PubMed:11747433, ECO:0000269|PubMed:9045711}; AltName: Full=Arginosuccinase;
- **Gene Information:** Name=ASL;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the lyase 1 family. Argininosuccinate lyase
- **Key Domains:** Arg_succ_lyase_C. (IPR029419); Argininosuccinate_lyase. (IPR009049); Fumarase/histidase_N. (IPR024083); Fumarate_lyase_CS. (IPR020557); Fumarate_lyase_fam. (IPR000362)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ASL" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ASL' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ASL** (gene ID: ASL, UniProt: P04424) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Functional Annotation of Human ASL (Argininosuccinate Lyase)

## Gene and Protein Identity

The human *ASL* gene (UniProt: P04424) encodes argininosuccinate lyase (ASAL; EC 4.3.2.1), also known as arginosuccinase. The gene is located on chromosome 7 (7q11.21), spanning approximately 17,554 base pairs organized into 16 coding exons plus an exon 0 that encodes only the 5′ untranslated region (baruteau2019argininosuccinicaciduriarecent pages 1-6, erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5, baruteau2019argininosuccinicaciduriarecent pages 6-9). The encoded protein consists of 464 amino acids with a monomer molecular weight of approximately 52 kDa (nagamani2012argininosuccinatelyasedeficiency pages 2-3). ASL belongs to the lyase 1 family and is a member of the β-elimination/fumarate lyase superfamily, sharing structural homology with fumarase, aspartase, and adenylosuccinate lyase (chakraborty1999mutationalanalysisof pages 48-53, toth2000thestructureof pages 1-2).

The following table summarizes the key molecular and functional properties of human ASL:

| Property | Summary |
|---|---|
| Gene name | **ASL** (argininosuccinate lyase; argininosuccinase) in **Homo sapiens** (human) (baruteau2019argininosuccinicaciduriarecent pages 1-6, erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5) |
| UniProt accession | **P04424** |
| Chromosome location | **Chromosome 7**; reported as **7q11.21 / cen-q11.2**, with gene structure including exon 0 for 5' UTR and 16 coding exons (baruteau2019argininosuccinicaciduriarecent pages 1-6, erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5, baruteau2019argininosuccinicaciduriarecent pages 6-9) |
| Protein size | **464 aa**, about **52 kDa per monomer** (tetramer ~208 kDa) (nagamani2012argininosuccinatelyasedeficiency pages 2-3) |
| Quaternary structure | **Homotetramer** with **4 active sites**; each active site is formed at the interface of **three subunits** (chakraborty1999mutationalanalysisof pages 48-53, baruteau2019argininosuccinicaciduriarecent pages 1-6, nagamani2012argininosuccinatelyasedeficiency pages 2-3) |
| EC number | **EC 4.3.2.1** (argininosuccinate lyase) (baruteau2019argininosuccinicaciduriarecent pages 1-6) |
| Reaction catalyzed | Reversible cleavage of **argininosuccinate → L-arginine + fumarate**; this is the 4th step of the urea cycle and also supplies arginine in the citrulline-NO cycle (chakraborty1999mutationalanalysisof pages 36-42, baruteau2019argininosuccinicaciduriarecent pages 1-6, wu1998argininemetabolismnitric pages 2-3) |
| Substrate specificity | Physiologic substrate is **argininosuccinic acid (argininosuccinate)**; ASL is the only enzyme capable of generating endogenous arginine in mammalian cells (nagamani2012argininosuccinatelyasedeficiency pages 2-3, keshet2018arginineandthe pages 2-2) |
| Catalytic mechanism | **β-elimination (ElcB)** mechanism with a **carbanion intermediate**; elimination proceeds with **trans stereochemistry**, and C–N bond cleavage is likely rate-limiting (chakraborty1999mutationalanalysisof pages 36-42, chakraborty1999mutationalanalysisof pages 42-48) |
| Subcellular localization | **Cytosolic** enzyme; also functions in a compartmentalized **CAT1-ASS1-ASL-NOS** complex for arginine channeling to NOS (baruteau2019argininosuccinicaciduriarecent pages 1-6, baruteau2019argininosuccinicaciduriarecent pages 6-9, mori2004argininemetabolicenzymes pages 2-3) |
| Primary tissue expression | Expressed predominantly in **liver**; also present in **kidney (proximal tubules)**, brain, heart, muscle, skin, hematopoietic tissues, small intestine, pancreas, fibroblasts, and erythrocytes. Kidney is a major site of endogenous arginine synthesis (~60% net synthesis in adults) (baruteau2019argininosuccinicaciduriarecent pages 1-6, nagamani2012argininosuccinatelyasedeficiency pages 2-3, chakraborty1999mutationalanalysisof pages 36-42) |
| Pathway involvement | **Urea cycle:** supports ammonia detoxification/ureagenesis. **Citrulline-NO cycle:** regenerates arginine from citrulline to support nitric oxide synthesis by NOS (baruteau2019argininosuccinicaciduriarecent pages 1-6, mori2004argininemetabolicenzymes pages 1-2) |
| Superfamily / family membership | Member of the **β-elimination / fumarate-lyase-related superfamily**, related to **δ-crystallin**, fumarase, aspartase, and adenylosuccinate lyase; highly conserved across bacteria to mammals (chakraborty1999mutationalanalysisof pages 48-53, erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5, toth2000thestructureof pages 1-2) |
| Key catalytic residues | Frequently implicated catalytic residues include **H91, H162, K289, E296**; H162/K289/E296 are central to proton abstraction and charge-relay chemistry (chakraborty1999mutationalanalysisof pages 42-48, chakraborty1999mutationalanalysisof pages 48-53) |
| Disease association | Biallelic pathogenic variants cause **ASL deficiency (ASLD)**, also called **argininosuccinic aciduria (ASA)**, a urea-cycle disorder with hyperammonemia and broader systemic disease including neurocognitive and liver manifestations (baruteau2019argininosuccinicaciduriarecent pages 1-6, gurung2024mrnatherapycorrects pages 11-12, kho2023argininosuccinatelyasedeficiency pages 4-6) |


*Table: This table summarizes the core molecular, structural, biochemical, and disease-related properties of human argininosuccinate lyase (ASL). It is useful as a compact reference for functional annotation and for connecting ASL’s enzymatic role to its pathway context and disease relevance.*

## 1. Enzymatic Function: Reaction and Substrate Specificity

ASL catalyzes the reversible cleavage of L-argininosuccinate into L-arginine and fumarate (chakraborty1999mutationalanalysisof pages 36-42, baruteau2019argininosuccinicaciduriarecent pages 1-6, wu1998argininemetabolismnitric pages 2-3). This reaction represents the fourth step of the urea cycle and is the sole enzymatic means of generating endogenous arginine in mammalian cells (nagamani2012argininosuccinatelyasedeficiency pages 2-3, keshet2018arginineandthe pages 2-2). The physiological substrate is argininosuccinic acid (argininosuccinate), and the products are L-arginine and fumarate (nagamani2012argininosuccinatelyasedeficiency pages 2-3). Kinetic studies using the homologous duck δ II crystallin (which retains ASL activity) have reported a V_max of 3.47 μmol/min/mg protein and a K_m of 0.35 mM (chakraborty1999mutationalanalysisof pages 32-36). In bovine and human ASL, non-linear kinetics with negative cooperativity at high substrate concentrations have been observed, with potential allosteric regulation by GTP (chakraborty1999mutationalanalysisof pages 42-48).

The reaction proceeds via an E1cB (elimination, unimolecular, conjugate base) mechanism involving a carbanion intermediate (chakraborty1999mutationalanalysisof pages 36-42, chakraborty1999mutationalanalysisof pages 42-48). Catalysis is initiated by proton abstraction at the Cβ position of argininosuccinate, generating a carbanion intermediate, followed by proton donation at the guanidinium nitrogen concurrent with cleavage of the Cα–N bond. The elimination proceeds with trans stereochemistry, requiring five atoms (catalytic base, H, Cβ, Cα, and N) to be coplanar. C–N bond cleavage is the likely rate-limiting step, and fumarate release exceeds arginine release by an order of magnitude (chakraborty1999mutationalanalysisof pages 36-42, chakraborty1999mutationalanalysisof pages 42-48).

## 2. Protein Structure and Catalytic Architecture

ASL functions as a cytosolic homotetramer with a total molecular weight of approximately 208 kDa, containing four catalytically active sites (chakraborty1999mutationalanalysisof pages 48-53, baruteau2019argininosuccinicaciduriarecent pages 1-6, nagamani2012argininosuccinatelyasedeficiency pages 2-3). Each monomer adopts a predominantly α-helical fold organized into three domains. The active sites are formed at the interfaces of three different subunits within the tetramer, meaning that proper quaternary assembly is essential for enzymatic activity (chakraborty1999mutationalanalysisof pages 48-53, nagamani2012argininosuccinatelyasedeficiency pages 2-3). This multi-subunit active site architecture also underpins the phenomenon of intragenic complementation, whereby heterotetramers formed from two individually inactive mutant monomers can regain partial enzymatic function (baruteau2019argininosuccinicaciduriarecent pages 6-9, engel2012bacterialexpressionof pages 7-8).

Key catalytic residues include His162, which acts as the general base for proton abstraction; Lys289, which is absolutely conserved and stabilizes the carbanion intermediate; Glu296, which participates in a charge-relay network with His162 to enhance its basicity; and His91, which plays a role in substrate binding and catalysis (chakraborty1999mutationalanalysisof pages 42-48, chakraborty1999mutationalanalysisof pages 48-53). These residues are spatially distributed across different monomers but cluster together at the active site upon tetramer formation. Despite low overall sequence identity (approximately 15%) among superfamily members, three highly conserved regions that contribute these catalytic residues are maintained across all members of the fumarate lyase superfamily (chakraborty1999mutationalanalysisof pages 48-53).

## 3. Subcellular Localization and Tissue Distribution

ASL is a cytosolic enzyme (baruteau2019argininosuccinicaciduriarecent pages 1-6, chakraborty1999mutationalanalysisof pages 36-42, wu1998argininemetabolismnitric pages 2-3). It is predominantly expressed in the liver, where it functions as part of the hepatic urea cycle localized in periportal hepatocytes (baruteau2019argininosuccinicaciduriarecent pages 1-6, wu1998argininemetabolismnitric pages 5-6). However, ASL expression is ubiquitous and is also found at significant levels in the kidney (specifically in proximal tubules, where approximately 60% of net endogenous arginine synthesis occurs in adult mammals), brain, heart, skeletal muscle, skin, hematopoietic tissues, small intestine, pancreas, fibroblasts, and erythrocytes (baruteau2019argininosuccinicaciduriarecent pages 1-6, nagamani2012argininosuccinatelyasedeficiency pages 2-3, erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 3-4, chakraborty1999mutationalanalysisof pages 36-42).

Importantly, ASL is not only a soluble cytoplasmic enzyme but also participates in a multiprotein complex at specific subcellular locations. In endothelial cells, ASL has been shown to colocalize with the cationic amino acid transporter CAT1, argininosuccinate synthase (ASS1), and endothelial nitric oxide synthase (eNOS) in caveolae, forming a metabolon that channels arginine directly to NOS for nitric oxide (NO) production (baruteau2019argininosuccinicaciduriarecent pages 6-9, mori2004argininemetabolicenzymes pages 2-3). This compartmentalized complex is critical for efficient NO biosynthesis and has functional significance beyond what bulk arginine availability alone would predict.

## 4. Biochemical and Signaling Pathways

### 4.1 The Urea Cycle

ASL catalyzes the fourth of five enzymatic steps in the urea cycle, which is the primary pathway for detoxification of ammonia in mammals (baruteau2019argininosuccinicaciduriarecent pages 1-6). In this pathway, ammonia derived from amino acid catabolism is converted to urea through the sequential actions of carbamoyl phosphate synthetase I (CPS1), ornithine transcarbamylase (OTC), argininosuccinate synthase (ASS1), ASL, and arginase 1 (ARG1). The first two steps occur in the mitochondrial matrix, while ASS1, ASL, and ARG1 operate in the cytosol. ASL cleaves argininosuccinate to produce arginine, which is then hydrolyzed by arginase to yield urea and ornithine, completing the cycle. The fumarate released by ASL can enter the TCA cycle as an anaplerotic substrate (wu1998argininemetabolismnitric pages 2-3).

### 4.2 The Citrulline-NO Cycle

Beyond its role in ureagenesis, ASL functions as a critical component of the citrulline-NO cycle (also called the arginine-citrulline cycle), which supports nitric oxide synthesis (baruteau2019argininosuccinicaciduriarecent pages 1-6, mori2004argininemetabolicenzymes pages 1-2, mori2004argininemetabolicenzymes pages 2-3, keshet2018arginineandthe pages 2-2). In this pathway, ASS1 condenses citrulline (a byproduct of NOS activity) with aspartate to form argininosuccinate, which ASL then cleaves to regenerate arginine. Arginine is subsequently used by NOS to produce NO and citrulline, completing the cycle. This recycling mechanism is essential for sustained NO production in cells expressing all three NOS isoforms (neuronal nNOS, endothelial eNOS, and inducible iNOS) (mori2004argininemetabolicenzymes pages 1-2).

The citrulline-NO cycle has been demonstrated to be functional in multiple cell types, including activated macrophages, microglia, glial cells, neuronal PC12 cells, retinal pigment epithelial cells, and vascular endothelial cells (mori2004argininemetabolicenzymes pages 1-2). ASL and ASS are coinduced with iNOS during inflammatory stimulation in macrophages, and colocalize with both nNOS and eNOS in neurons and endothelial cells, respectively (mori2004argininemetabolicenzymes pages 2-3). The colocalization of ASL with eNOS in endothelial caveolae, as part of a multiprotein complex including CAT1 and ASS1, facilitates efficient arginine channeling that is essential for regulated NO production (baruteau2019argininosuccinicaciduriarecent pages 6-9, mori2004argininemetabolicenzymes pages 2-3).

### 4.3 Arginine as a Metabolic Nexus

Because ASL is the only enzyme in mammalian cells capable of generating endogenous arginine de novo, its product serves as a precursor for multiple biologically important pathways, including the synthesis of urea, NO, polyamines, proline, glutamate, creatine, and agmatine (nagamani2012argininosuccinatelyasedeficiency pages 2-3, erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 3-4, keshet2018arginineandthe pages 2-2). This positions ASL at a critical metabolic nexus linking nitrogen disposal, signaling, protein synthesis, and energy metabolism.

## 5. Evolutionary Conservation and Relationship to δ-Crystallin

ASL is highly evolutionarily conserved across species ranging from bacteria and yeast to plants and mammals (erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5, baruteau2019argininosuccinicaciduriarecent pages 6-9). Human and yeast ASL sequences share approximately 50% nucleotide identity and 54% amino acid identity (chakraborty1999mutationalanalysisof pages 36-42). Notably, ASL shares a common ancestral origin with avian δ-crystallins, which were recruited from an ancestral ASL gene to serve structural roles in the lens of birds and reptiles (erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5, chakraborty1999mutationalanalysisof pages 32-36). Of the two avian δ-crystallin isoforms (δI and δII), which share approximately 89% amino acid sequence identity, only δII retains catalytic ASL activity with kinetic parameters comparable to mammalian ASL, while δI has been specialized for a purely structural role (chakraborty1999mutationalanalysisof pages 32-36). This represents a classic example of gene sharing, where a single gene serves both enzymatic and structural functions. The conservation of ASL in birds, which lack a functional urea cycle, further demonstrates that ASL's role in arginine generation for protein synthesis and NO production is evolutionarily fundamental, independent of ureagenesis (erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5). Fifteen of the intron/exon boundaries are in identical positions between the rat ASL gene and chicken δ-crystallin genes, providing strong structural evidence for their shared origin (chakraborty1999mutationalanalysisof pages 32-36).

## 6. ASL Deficiency and Disease

### 6.1 Argininosuccinic Aciduria (ASA)

Biallelic pathogenic variants in *ASL* cause argininosuccinate lyase deficiency (ASLD; OMIM 207900), also known as argininosuccinic aciduria (ASA), an autosomal recessive urea cycle disorder (baruteau2019argininosuccinicaciduriarecent pages 1-6, kho2023argininosuccinatelyasedeficiency pages 1-2). ASLD presents as a spectrum of disease ranging from severe neonatal-onset hyperammonemia to late-onset and even asymptomatic forms. Approximately 140 pathogenic variants have been documented in the *ASL* gene, including missense, nonsense, insertion, deletion, and splicing mutations, with exons 4, 5, and 7 identified as mutational hotspots (erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5, baruteau2019argininosuccinicaciduriarecent pages 6-9). Three founder mutations have been identified in Saudi Arabian and Finnish populations (baruteau2019argininosuccinicaciduriarecent pages 6-9). A notable feature of ASLD is the phenomenon of intragenic complementation, whereby compound heterozygous patients may have milder phenotypes than expected from individual allelic effects, owing to the multi-subunit active site architecture (baruteau2019argininosuccinicaciduriarecent pages 6-9, engel2012bacterialexpressionof pages 7-8).

### 6.2 Beyond Hyperammonemia: NO Deficiency and Systemic Disease

A critical insight from recent research is that ASLD is not merely a disorder of ammonia detoxification but a systemic disease with neurocognitive, hepatic, and vascular manifestations that can occur independently of hyperammonemia (baruteau2019argininosuccinicaciduriarecent pages 1-6, kho2023argininosuccinatelyasedeficiency pages 1-2). This is attributable to ASL's role in the citrulline-NO cycle: loss of ASL leads to cell-autonomous NO deficiency because arginine cannot be regenerated intracellularly for NOS, even when extracellular arginine is available (kho2023argininosuccinatelyasedeficiency pages 4-6, kho2023argininosuccinatelyasedeficiency pages 6-7, kho2023argininosuccinatelyasedeficiency pages 2-4). A landmark study by Kho et al. (2023) demonstrated that ASL deficiency disrupts blood-brain barrier (BBB) integrity through NO-mediated dysregulation of tight junction claudin proteins, specifically causing upregulation of claudin-1 and downregulation of claudin-5 in brain microvascular endothelial cells (kho2023argininosuccinatelyasedeficiency pages 4-6, kho2023argininosuccinatelyasedeficiency pages 2-4, kho2023argininosuccinatelyasedeficiency pages 7-9). In vivo, hypomorphic ASL-deficient mice showed BBB leakage that was partially rescued by NO supplementation with sodium nitrite, establishing a direct mechanistic link between ASL-dependent NO production and BBB maintenance (kho2023argininosuccinatelyasedeficiency pages 6-7, kho2023argininosuccinatelyasedeficiency pages 9-10).

Additionally, Gurung et al. (2024) identified dysregulation of glutathione biosynthesis and oxidative stress as a novel pathophysiological mechanism in ASLD, with upregulated cysteine metabolism contrasting with glutathione depletion and downregulated antioxidant pathways in both patients and animal models (gurung2024mrnatherapycorrects pages 11-12, gurung2024mrnatherapycorrects pages 1-3).

### 6.3 Emerging Therapeutic Approaches

Several novel therapeutic strategies for ASLD are under active development:

**mRNA Therapy:** Gurung et al. (2024) demonstrated that human ASL mRNA encapsulated in lipid nanoparticles (LNP) corrected glutathione metabolism, improved chronic liver disease, and restored ureagenesis in ASL-deficient mouse models. Treatment from birth normalized plasma metabolites and liver ASL expression. The study also introduced [18F]FSPG PET as a noninvasive tool to monitor disease and therapeutic response (gurung2024mrnatherapycorrects pages 11-12, gurung2024mrnatherapycorrects pages 1-3). Independently, Daly et al. (2023) showed that nucleoside-modified ASL mRNA-LNP provided complete survival protection in ASL-deficient mice at 3 mg/kg administered twice weekly, with a favorable safety and immunogenicity profile (daly2023aslmrnalnptherapeutic pages 1-2, daly2023aslmrnalnptherapeutic pages 11-13).

**CRISPR Base Editing:** Jalil et al. (2024) demonstrated that CRISPR adenine base editors (ABE8e) delivered via lipid nanoparticles could correct the common c.1153C>T pathogenic variant in patient-derived primary fibroblasts, restoring ASL enzyme activity to approximately 59% of healthy donor levels and significantly reducing argininosuccinic acid accumulation (jalil2024geneticandfunctional pages 11-12).

These therapeutic advances underscore the dual enzymatic and structural roles of ASL—liver-directed therapies can address ureagenesis and hepatic disease, but the systemic NO-related manifestations, particularly neurological complications, remain a challenge that may require complementary approaches (daly2023aslmrnalnptherapeutic pages 13-15).

## 7. Summary

Human ASL (P04424) is a cytosolic homotetrameric enzyme that catalyzes the reversible β-elimination of argininosuccinate to yield arginine and fumarate via an E1cB mechanism with a carbanion intermediate. It operates at the intersection of two critical metabolic pathways—the urea cycle for ammonia detoxification and the citrulline-NO cycle for nitric oxide synthesis—and is the sole enzyme capable of endogenous arginine generation. ASL is expressed broadly across tissues, with highest levels in liver and kidney. Its participation in a multiprotein complex with ASS1 and NOS enables arginine channeling for regulated NO production in endothelial and other cell types. ASL is highly conserved from bacteria to mammals and shares evolutionary and structural origins with avian δ-crystallins. Loss-of-function mutations cause argininosuccinic aciduria, a systemic disorder with hyperammonemia, NO deficiency, glutathione dysregulation, and neurovascular complications including blood-brain barrier disruption. Recent therapeutic advances including mRNA-LNP and CRISPR base editing approaches show significant preclinical promise for correcting ASL deficiency.

References

1. (baruteau2019argininosuccinicaciduriarecent pages 1-6): Julien Baruteau, Carmen Diez‐Fernandez, Shaul Lerner, Giusy Ranucci, Paul Gissen, Carlo Dionisi‐Vici, Sandesh Nagamani, Ayelet Erez, and Johannes Häberle. Argininosuccinic aciduria: recent pathophysiological insights and therapeutic prospects. Journal of Inherited Metabolic Disease, 42:1147-1161, Nov 2019. URL: https://doi.org/10.1002/jimd.12047, doi:10.1002/jimd.12047. This article has 58 citations and is from a peer-reviewed journal.

2. (erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 4-5): Ayelet Erez, Sandesh C. Sreenath Nagamani, and Brendan Lee. Argininosuccinate lyase deficiency—argininosuccinic aciduria and beyond. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 157:45-53, Feb 2011. URL: https://doi.org/10.1002/ajmg.c.30289, doi:10.1002/ajmg.c.30289. This article has 132 citations.

3. (baruteau2019argininosuccinicaciduriarecent pages 6-9): Julien Baruteau, Carmen Diez‐Fernandez, Shaul Lerner, Giusy Ranucci, Paul Gissen, Carlo Dionisi‐Vici, Sandesh Nagamani, Ayelet Erez, and Johannes Häberle. Argininosuccinic aciduria: recent pathophysiological insights and therapeutic prospects. Journal of Inherited Metabolic Disease, 42:1147-1161, Nov 2019. URL: https://doi.org/10.1002/jimd.12047, doi:10.1002/jimd.12047. This article has 58 citations and is from a peer-reviewed journal.

4. (nagamani2012argininosuccinatelyasedeficiency pages 2-3): Sandesh C.S. Nagamani, Ayelet Erez, and Brendan Lee. Argininosuccinate lyase deficiency. May 2012. URL: https://doi.org/10.1038/gim.2011.1, doi:10.1038/gim.2011.1. This article has 174 citations and is from a highest quality peer-reviewed journal.

5. (chakraborty1999mutationalanalysisof pages 48-53): Anita R. Chakraborty, Alan Davidson, and P. Lynne Howell. Mutational analysis of amino acid residues involved in argininosuccinate lyase activity in duck delta ii crystallin. Biochemistry, 38 8:2435-43, Feb 1999. URL: https://doi.org/10.1021/bi982150g, doi:10.1021/bi982150g. This article has 36 citations and is from a peer-reviewed journal.

6. (toth2000thestructureof pages 1-2): Eric A Toth and Todd O Yeates. The structure of adenylosuccinate lyase, an enzyme with dual activity in the de novo purine biosynthetic pathway. Structure, 8 2:163-74, Feb 2000. URL: https://doi.org/10.1016/s0969-2126(00)00092-7, doi:10.1016/s0969-2126(00)00092-7. This article has 129 citations and is from a domain leading peer-reviewed journal.

7. (chakraborty1999mutationalanalysisof pages 36-42): Anita R. Chakraborty, Alan Davidson, and P. Lynne Howell. Mutational analysis of amino acid residues involved in argininosuccinate lyase activity in duck delta ii crystallin. Biochemistry, 38 8:2435-43, Feb 1999. URL: https://doi.org/10.1021/bi982150g, doi:10.1021/bi982150g. This article has 36 citations and is from a peer-reviewed journal.

8. (wu1998argininemetabolismnitric pages 2-3): Guoyao WU and Sidney M. MORRIS. Arginine metabolism: nitric oxide and beyond. The Biochemical journal, 336 ( Pt 1):1-17, Nov 1998. URL: https://doi.org/10.1042/bj3360001, doi:10.1042/bj3360001. This article has 3857 citations.

9. (keshet2018arginineandthe pages 2-2): Rom Keshet and Ayelet Erez. Arginine and the metabolic regulation of nitric oxide synthesis in cancer. Disease Models & Mechanisms, Aug 2018. URL: https://doi.org/10.1242/dmm.033332, doi:10.1242/dmm.033332. This article has 197 citations and is from a domain leading peer-reviewed journal.

10. (chakraborty1999mutationalanalysisof pages 42-48): Anita R. Chakraborty, Alan Davidson, and P. Lynne Howell. Mutational analysis of amino acid residues involved in argininosuccinate lyase activity in duck delta ii crystallin. Biochemistry, 38 8:2435-43, Feb 1999. URL: https://doi.org/10.1021/bi982150g, doi:10.1021/bi982150g. This article has 36 citations and is from a peer-reviewed journal.

11. (mori2004argininemetabolicenzymes pages 2-3): Masataka Mori and Tomomi Gotoh. Arginine metabolic enzymes, nitric oxide and infection. The Journal of nutrition, 134 10 Suppl:2820S-2825S;discussion2853S, Oct 2004. URL: https://doi.org/10.1093/jn/134.10.2820s, doi:10.1093/jn/134.10.2820s. This article has 215 citations.

12. (mori2004argininemetabolicenzymes pages 1-2): Masataka Mori and Tomomi Gotoh. Arginine metabolic enzymes, nitric oxide and infection. The Journal of nutrition, 134 10 Suppl:2820S-2825S;discussion2853S, Oct 2004. URL: https://doi.org/10.1093/jn/134.10.2820s, doi:10.1093/jn/134.10.2820s. This article has 215 citations.

13. (gurung2024mrnatherapycorrects pages 11-12): Sonam Gurung, Oskar Vilhelmsson Timmermand, Dany Perocheau, Ana Luisa Gil-Martinez, Magdalena Minnion, Loukia Touramanidou, Sherry Fang, Martina Messina, Youssef Khalil, Justyna Spiewak, Abigail R. Barber, Richard S. Edwards, Patricia Lipari Pinto, Patrick F. Finn, Alex Cavedon, Summar Siddiqui, Lisa Rice, Paolo G. V. Martini, Deborah Ridout, Wendy Heywood, Ian Hargreaves, Simon Heales, Philippa B. Mills, Simon N. Waddington, Paul Gissen, Simon Eaton, Mina Ryten, Martin Feelisch, Andrea Frassetto, Timothy H. Witney, and Julien Baruteau. Mrna therapy corrects defective glutathione metabolism and restores ureagenesis in preclinical argininosuccinic aciduria. Science translational medicine, 16:eadh1334-eadh1334, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adh1334, doi:10.1126/scitranslmed.adh1334. This article has 37 citations and is from a highest quality peer-reviewed journal.

14. (kho2023argininosuccinatelyasedeficiency pages 4-6): Jordan Kho, Urszula Polak, Ming-Ming Jiang, John D. Odom, Jill V. Hunter, Saima M. Ali, Lindsay C. Burrage, Sandesh C.S. Nagamani, Robia G. Pautler, Hannah P. Thompson, Akihiko Urayama, Zixue Jin, and Brendan Lee. Argininosuccinate lyase deficiency causes blood-brain barrier disruption via nitric oxide–mediated dysregulation of claudin expression. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168475, doi:10.1172/jci.insight.168475. This article has 13 citations and is from a domain leading peer-reviewed journal.

15. (chakraborty1999mutationalanalysisof pages 32-36): Anita R. Chakraborty, Alan Davidson, and P. Lynne Howell. Mutational analysis of amino acid residues involved in argininosuccinate lyase activity in duck delta ii crystallin. Biochemistry, 38 8:2435-43, Feb 1999. URL: https://doi.org/10.1021/bi982150g, doi:10.1021/bi982150g. This article has 36 citations and is from a peer-reviewed journal.

16. (engel2012bacterialexpressionof pages 7-8): Katharina Engel, Jean‐Marc Vuissoz, Sandra Eggimann, Murielle Groux, Christoph Berning, Liyan Hu, Vera Klaus, Dorothea Moeslinger, Saadet Mercimek‐Mahmutoglu, Sylvia Stöckler, Bendicht Wermuth, Johannes Häberle, and Jean‐Marc Nuoffer. Bacterial expression of mutant argininosuccinate lyase reveals imperfect correlation of in-vitro enzyme activity with clinical phenotype in argininosuccinic aciduria. Journal of Inherited Metabolic Disease, 35:133-140, Jan 2012. URL: https://doi.org/10.1007/s10545-011-9357-x, doi:10.1007/s10545-011-9357-x. This article has 21 citations and is from a peer-reviewed journal.

17. (wu1998argininemetabolismnitric pages 5-6): Guoyao WU and Sidney M. MORRIS. Arginine metabolism: nitric oxide and beyond. The Biochemical journal, 336 ( Pt 1):1-17, Nov 1998. URL: https://doi.org/10.1042/bj3360001, doi:10.1042/bj3360001. This article has 3857 citations.

18. (erez2011argininosuccinatelyasedeficiency—argininosuccinic pages 3-4): Ayelet Erez, Sandesh C. Sreenath Nagamani, and Brendan Lee. Argininosuccinate lyase deficiency—argininosuccinic aciduria and beyond. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 157:45-53, Feb 2011. URL: https://doi.org/10.1002/ajmg.c.30289, doi:10.1002/ajmg.c.30289. This article has 132 citations.

19. (kho2023argininosuccinatelyasedeficiency pages 1-2): Jordan Kho, Urszula Polak, Ming-Ming Jiang, John D. Odom, Jill V. Hunter, Saima M. Ali, Lindsay C. Burrage, Sandesh C.S. Nagamani, Robia G. Pautler, Hannah P. Thompson, Akihiko Urayama, Zixue Jin, and Brendan Lee. Argininosuccinate lyase deficiency causes blood-brain barrier disruption via nitric oxide–mediated dysregulation of claudin expression. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168475, doi:10.1172/jci.insight.168475. This article has 13 citations and is from a domain leading peer-reviewed journal.

20. (kho2023argininosuccinatelyasedeficiency pages 6-7): Jordan Kho, Urszula Polak, Ming-Ming Jiang, John D. Odom, Jill V. Hunter, Saima M. Ali, Lindsay C. Burrage, Sandesh C.S. Nagamani, Robia G. Pautler, Hannah P. Thompson, Akihiko Urayama, Zixue Jin, and Brendan Lee. Argininosuccinate lyase deficiency causes blood-brain barrier disruption via nitric oxide–mediated dysregulation of claudin expression. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168475, doi:10.1172/jci.insight.168475. This article has 13 citations and is from a domain leading peer-reviewed journal.

21. (kho2023argininosuccinatelyasedeficiency pages 2-4): Jordan Kho, Urszula Polak, Ming-Ming Jiang, John D. Odom, Jill V. Hunter, Saima M. Ali, Lindsay C. Burrage, Sandesh C.S. Nagamani, Robia G. Pautler, Hannah P. Thompson, Akihiko Urayama, Zixue Jin, and Brendan Lee. Argininosuccinate lyase deficiency causes blood-brain barrier disruption via nitric oxide–mediated dysregulation of claudin expression. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168475, doi:10.1172/jci.insight.168475. This article has 13 citations and is from a domain leading peer-reviewed journal.

22. (kho2023argininosuccinatelyasedeficiency pages 7-9): Jordan Kho, Urszula Polak, Ming-Ming Jiang, John D. Odom, Jill V. Hunter, Saima M. Ali, Lindsay C. Burrage, Sandesh C.S. Nagamani, Robia G. Pautler, Hannah P. Thompson, Akihiko Urayama, Zixue Jin, and Brendan Lee. Argininosuccinate lyase deficiency causes blood-brain barrier disruption via nitric oxide–mediated dysregulation of claudin expression. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168475, doi:10.1172/jci.insight.168475. This article has 13 citations and is from a domain leading peer-reviewed journal.

23. (kho2023argininosuccinatelyasedeficiency pages 9-10): Jordan Kho, Urszula Polak, Ming-Ming Jiang, John D. Odom, Jill V. Hunter, Saima M. Ali, Lindsay C. Burrage, Sandesh C.S. Nagamani, Robia G. Pautler, Hannah P. Thompson, Akihiko Urayama, Zixue Jin, and Brendan Lee. Argininosuccinate lyase deficiency causes blood-brain barrier disruption via nitric oxide–mediated dysregulation of claudin expression. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168475, doi:10.1172/jci.insight.168475. This article has 13 citations and is from a domain leading peer-reviewed journal.

24. (gurung2024mrnatherapycorrects pages 1-3): Sonam Gurung, Oskar Vilhelmsson Timmermand, Dany Perocheau, Ana Luisa Gil-Martinez, Magdalena Minnion, Loukia Touramanidou, Sherry Fang, Martina Messina, Youssef Khalil, Justyna Spiewak, Abigail R. Barber, Richard S. Edwards, Patricia Lipari Pinto, Patrick F. Finn, Alex Cavedon, Summar Siddiqui, Lisa Rice, Paolo G. V. Martini, Deborah Ridout, Wendy Heywood, Ian Hargreaves, Simon Heales, Philippa B. Mills, Simon N. Waddington, Paul Gissen, Simon Eaton, Mina Ryten, Martin Feelisch, Andrea Frassetto, Timothy H. Witney, and Julien Baruteau. Mrna therapy corrects defective glutathione metabolism and restores ureagenesis in preclinical argininosuccinic aciduria. Science translational medicine, 16:eadh1334-eadh1334, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adh1334, doi:10.1126/scitranslmed.adh1334. This article has 37 citations and is from a highest quality peer-reviewed journal.

25. (daly2023aslmrnalnptherapeutic pages 1-2): Owen Daly, Azita Josefine Mahiny, Sara Majeski, Kevin McClintock, Julia Reichert, Gábor Boros, Gábor Tamás Szabó, Jonas Reinholz, Petra Schreiner, Steve Reid, Kieu Lam, Marlen Lepper, Melanie Adler, Tracy Meffen, James Heyes, Katalin Karikó, Pete Lutwyche, and Irena Vlatkovic. Asl mrna-lnp therapeutic for the treatment of argininosuccinic aciduria enables survival benefit in a mouse model. Biomedicines, 11:1735, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061735, doi:10.3390/biomedicines11061735. This article has 4 citations.

26. (daly2023aslmrnalnptherapeutic pages 11-13): Owen Daly, Azita Josefine Mahiny, Sara Majeski, Kevin McClintock, Julia Reichert, Gábor Boros, Gábor Tamás Szabó, Jonas Reinholz, Petra Schreiner, Steve Reid, Kieu Lam, Marlen Lepper, Melanie Adler, Tracy Meffen, James Heyes, Katalin Karikó, Pete Lutwyche, and Irena Vlatkovic. Asl mrna-lnp therapeutic for the treatment of argininosuccinic aciduria enables survival benefit in a mouse model. Biomedicines, 11:1735, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061735, doi:10.3390/biomedicines11061735. This article has 4 citations.

27. (jalil2024geneticandfunctional pages 11-12): Sami Jalil, Timo Keskinen, Juhana Juutila, Rocio Sartori Maldonado, Liliya Euro, Anu Suomalainen, Risto Lapatto, Emilia Kuuluvainen, Ville Hietakangas, Timo Otonkoski, Mervi E. Hyvönen, and Kirmo Wartiovaara. Genetic and functional correction of argininosuccinate lyase deficiency using crispr adenine base editors. American Journal of Human Genetics, 111:714-728, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.004, doi:10.1016/j.ajhg.2024.03.004. This article has 21 citations and is from a highest quality peer-reviewed journal.

28. (daly2023aslmrnalnptherapeutic pages 13-15): Owen Daly, Azita Josefine Mahiny, Sara Majeski, Kevin McClintock, Julia Reichert, Gábor Boros, Gábor Tamás Szabó, Jonas Reinholz, Petra Schreiner, Steve Reid, Kieu Lam, Marlen Lepper, Melanie Adler, Tracy Meffen, James Heyes, Katalin Karikó, Pete Lutwyche, and Irena Vlatkovic. Asl mrna-lnp therapeutic for the treatment of argininosuccinic aciduria enables survival benefit in a mouse model. Biomedicines, 11:1735, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061735, doi:10.3390/biomedicines11061735. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](ASL-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. nagamani2012argininosuccinatelyasedeficiency pages 2-3
2. baruteau2019argininosuccinicaciduriarecent pages 1-6
3. chakraborty1999mutationalanalysisof pages 32-36
4. chakraborty1999mutationalanalysisof pages 42-48
5. chakraborty1999mutationalanalysisof pages 48-53
6. wu1998argininemetabolismnitric pages 2-3
7. mori2004argininemetabolicenzymes pages 1-2
8. mori2004argininemetabolicenzymes pages 2-3
9. chakraborty1999mutationalanalysisof pages 36-42
10. baruteau2019argininosuccinicaciduriarecent pages 6-9
11. jalil2024geneticandfunctional pages 11-12
12. daly2023aslmrnalnptherapeutic pages 13-15
13. toth2000thestructureof pages 1-2
14. keshet2018arginineandthe pages 2-2
15. gurung2024mrnatherapycorrects pages 11-12
16. kho2023argininosuccinatelyasedeficiency pages 4-6
17. engel2012bacterialexpressionof pages 7-8
18. wu1998argininemetabolismnitric pages 5-6
19. kho2023argininosuccinatelyasedeficiency pages 1-2
20. kho2023argininosuccinatelyasedeficiency pages 6-7
21. kho2023argininosuccinatelyasedeficiency pages 2-4
22. kho2023argininosuccinatelyasedeficiency pages 7-9
23. kho2023argininosuccinatelyasedeficiency pages 9-10
24. gurung2024mrnatherapycorrects pages 1-3
25. daly2023aslmrnalnptherapeutic pages 1-2
26. daly2023aslmrnalnptherapeutic pages 11-13
27. 18F
28. https://doi.org/10.1002/jimd.12047,
29. https://doi.org/10.1002/ajmg.c.30289,
30. https://doi.org/10.1038/gim.2011.1,
31. https://doi.org/10.1021/bi982150g,
32. https://doi.org/10.1016/s0969-2126(00
33. https://doi.org/10.1042/bj3360001,
34. https://doi.org/10.1242/dmm.033332,
35. https://doi.org/10.1093/jn/134.10.2820s,
36. https://doi.org/10.1126/scitranslmed.adh1334,
37. https://doi.org/10.1172/jci.insight.168475,
38. https://doi.org/10.1007/s10545-011-9357-x,
39. https://doi.org/10.3390/biomedicines11061735,
40. https://doi.org/10.1016/j.ajhg.2024.03.004,