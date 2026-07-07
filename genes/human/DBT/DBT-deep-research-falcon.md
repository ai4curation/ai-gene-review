---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T19:27:16.319813'
end_time: '2026-07-05T19:57:27.859015'
duration_seconds: 1811.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: DBT
  gene_symbol: DBT
  uniprot_accession: P11182
  protein_description: 'RecName: Full=Lipoamide acyltransferase component of branched-chain
    alpha-keto acid dehydrogenase complex, mitochondrial {ECO:0000305}; EC=2.3.1.168
    {ECO:0000250|UniProtKB:P11181}; AltName: Full=52 kDa mitochondrial autoantigen
    of primary biliary cirrhosis {ECO:0000303|PubMed:2908870}; AltName: Full=Branched
    chain 2-oxo-acid dehydrogenase complex component E2 {ECO:0000303|PubMed:7543435,
    ECO:0000303|PubMed:9141421}; Short=BCOADC-E2 {ECO:0000303|PubMed:7543435, ECO:0000303|PubMed:9141421};
    AltName: Full=Branched-chain alpha-keto acid dehydrogenase complex component E2;
    Short=BCKAD-E2; Short=BCKADE2; Short=BCKDH-E2 {ECO:0000303|PubMed:37558654}; AltName:
    Full=Dihydrolipoamide acetyltransferase component of branched-chain alpha-keto
    acid dehydrogenase complex; AltName: Full=Dihydrolipoamide branched chain transacylase;
    AltName: Full=Dihydrolipoyllysine-residue (2-methylpropanoyl)transferase; Flags:
    Precursor;'
  gene_info: Name=DBT {ECO:0000312|HGNC:HGNC:2698}; Synonyms=BCATE2, BCKDHE2 {ECO:0000303|PubMed:37558654};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the 2-oxoacid dehydrogenase family.
  protein_domains: 2-oxoA_DH_lipoyl-BS. (IPR003016); 2-oxoacid_DH_actylTfrase. (IPR001078);
    2-oxoacid_DH_E2_comp. (IPR050743); Biotin_lipoyl. (IPR000089); CAT-like_dom_sf.
    (IPR023213)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 56
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: DBT-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P11182
- **Protein Description:** RecName: Full=Lipoamide acyltransferase component of branched-chain alpha-keto acid dehydrogenase complex, mitochondrial {ECO:0000305}; EC=2.3.1.168 {ECO:0000250|UniProtKB:P11181}; AltName: Full=52 kDa mitochondrial autoantigen of primary biliary cirrhosis {ECO:0000303|PubMed:2908870}; AltName: Full=Branched chain 2-oxo-acid dehydrogenase complex component E2 {ECO:0000303|PubMed:7543435, ECO:0000303|PubMed:9141421}; Short=BCOADC-E2 {ECO:0000303|PubMed:7543435, ECO:0000303|PubMed:9141421}; AltName: Full=Branched-chain alpha-keto acid dehydrogenase complex component E2; Short=BCKAD-E2; Short=BCKADE2; Short=BCKDH-E2 {ECO:0000303|PubMed:37558654}; AltName: Full=Dihydrolipoamide acetyltransferase component of branched-chain alpha-keto acid dehydrogenase complex; AltName: Full=Dihydrolipoamide branched chain transacylase; AltName: Full=Dihydrolipoyllysine-residue (2-methylpropanoyl)transferase; Flags: Precursor;
- **Gene Information:** Name=DBT {ECO:0000312|HGNC:HGNC:2698}; Synonyms=BCATE2, BCKDHE2 {ECO:0000303|PubMed:37558654};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the 2-oxoacid dehydrogenase family.
- **Key Domains:** 2-oxoA_DH_lipoyl-BS. (IPR003016); 2-oxoacid_DH_actylTfrase. (IPR001078); 2-oxoacid_DH_E2_comp. (IPR050743); Biotin_lipoyl. (IPR000089); CAT-like_dom_sf. (IPR023213)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DBT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DBT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DBT** (gene ID: DBT, UniProt: P11182) in human.

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
- **UniProt Accession:** P11182
- **Protein Description:** RecName: Full=Lipoamide acyltransferase component of branched-chain alpha-keto acid dehydrogenase complex, mitochondrial {ECO:0000305}; EC=2.3.1.168 {ECO:0000250|UniProtKB:P11181}; AltName: Full=52 kDa mitochondrial autoantigen of primary biliary cirrhosis {ECO:0000303|PubMed:2908870}; AltName: Full=Branched chain 2-oxo-acid dehydrogenase complex component E2 {ECO:0000303|PubMed:7543435, ECO:0000303|PubMed:9141421}; Short=BCOADC-E2 {ECO:0000303|PubMed:7543435, ECO:0000303|PubMed:9141421}; AltName: Full=Branched-chain alpha-keto acid dehydrogenase complex component E2; Short=BCKAD-E2; Short=BCKADE2; Short=BCKDH-E2 {ECO:0000303|PubMed:37558654}; AltName: Full=Dihydrolipoamide acetyltransferase component of branched-chain alpha-keto acid dehydrogenase complex; AltName: Full=Dihydrolipoamide branched chain transacylase; AltName: Full=Dihydrolipoyllysine-residue (2-methylpropanoyl)transferase; Flags: Precursor;
- **Gene Information:** Name=DBT {ECO:0000312|HGNC:HGNC:2698}; Synonyms=BCATE2, BCKDHE2 {ECO:0000303|PubMed:37558654};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the 2-oxoacid dehydrogenase family.
- **Key Domains:** 2-oxoA_DH_lipoyl-BS. (IPR003016); 2-oxoacid_DH_actylTfrase. (IPR001078); 2-oxoacid_DH_E2_comp. (IPR050743); Biotin_lipoyl. (IPR000089); CAT-like_dom_sf. (IPR023213)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DBT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DBT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DBT** (gene ID: DBT, UniProt: P11182) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: DBT (Dihydrolipoamide Branched-Chain Transacylase E2)

## Gene and Protein Identity

The human **DBT** gene (HGNC:2698; synonyms: BCATE2, BCKDHE2) encodes the **lipoamide acyltransferase component of the branched-chain alpha-keto acid dehydrogenase (BCKDH) complex** (UniProt: P11182), also referred to as BCKDH-E2, BCOADC-E2, or dihydrolipoamide branched-chain transacylase. The protein is classified under EC 2.3.1.168 and belongs to the 2-oxoacid dehydrogenase family. It is synthesized as a mitochondrial precursor protein of approximately 52 kDa and functions within the mitochondrial matrix (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3, ahn2015interactionofperoxiredoxin pages 4-7).

The following table summarizes the key molecular and functional properties of DBT:

| Property | Summary |
|---|---|
| Gene name | **DBT**; synonyms include **BCATE2** and **BCKDHE2** (UniProt P11182 context from prompt; function/disease literature confirms DBT as the E2 subunit of BCKDH) (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3) |
| Protein name | **Dihydrolipoamide branched-chain transacylase E2**; also called **branched-chain 2-oxo acid dehydrogenase complex component E2 / BCKDH-E2 / BCOADC-E2** (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3, rong2011epithelialcellspecificity pages 1-2) |
| UniProt ID | **P11182** (user-provided target identification) |
| EC number | **EC 2.3.1.168** (user-provided target identification; consistent with acyltransferase role summarized in literature) (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3) |
| Organism | **Homo sapiens (human)** (user-provided target identification; human disease literature on MSUD and PBC pertains to this ortholog) (billington2022genomicandbiochemical pages 1-3, margutti2020maplesyrupurine pages 1-2) |
| Chromosomal location | **Chromosome 1p31** (standard human gene annotation; not directly documented in the retrieved context set, so best treated as canonical database annotation rather than literature-derived) |
| Protein size | **Mitochondrial precursor protein; historically described as a ~52 kDa mitochondrial autoantigen in PBC** (exact residue length not established from retrieved contexts) (billington2022genomicandbiochemical pages 1-3, rong2011epithelialcellspecificity pages 1-2) |
| Subcellular localization | **Mitochondrial matrix / inner-mitochondrial multienzyme complex** involved in branched-chain amino acid oxidation (ahn2015interactionofperoxiredoxin pages 4-7, ahn2015interactionofperoxiredoxin pages 1-2) |
| Enzyme complex | Core **E2 transacylase** component of the **branched-chain α-ketoacid dehydrogenase (BCKDH/BCKDC) complex**, together with E1α/E1β and E3 subunits (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3, margutti2020maplesyrupurine pages 1-2) |
| Domain structure | E2 contains an **N-terminal lipoyl-bearing domain**, an **E1/E3-binding (subunit-binding) domain**, and a **C-terminal inner-core/catalytic domain**, linked by flexible regions (ahn2015interactionofperoxiredoxin pages 4-7, li2025proteinlipoylationin pages 3-4) |
| Catalytic function | **Acyltransferase/transacylase** that accepts the oxidized branched-chain acyl intermediate from E1 on its lipoyl arm and transfers the acyl group to **CoA**, yielding branched-chain acyl-CoA products (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3) |
| Substrates | Indirectly acts on the branched-chain α-ketoacids produced from BCAAs: **KIC** (from leucine), **KMV** (from isoleucine), and **KIV** (from valine), via transfer of their decarboxylated acyl groups to CoA (billington2022genomicandbiochemical pages 1-3, bo2024primaryrolesof pages 11-13) |
| Products | Corresponding **branched-chain acyl-CoA conjugates** plus reduced/reoxidized lipoyl intermediates as part of the overall oxidative decarboxylation cycle (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3) |
| Cofactor | **Covalently attached lipoic acid (lipoyl-lysine arm)**, which acts as a flexible swinging arm between active sites and is essential for catalysis (bo2024primaryrolesof pages 11-13, li2025proteinlipoylationin pages 3-4, arp2023reactivenitrogenspecies pages 1-4) |
| Complex assembly | DBT forms the **24-subunit E2 structural core** of BCKDH, serving as the scaffold for assembly of E1 and E3 components (ahn2015interactionofperoxiredoxin pages 4-7, billington2022genomicandbiochemical pages 1-3) |
| Regulatory interactions | **BDK/BCKDK** binds the E2 core/lipoyl-binding interface to phosphorylate and inhibit E1α; **PPM1K/PP2Cm** counteracts this by dephosphorylating E1α and reactivating the complex. E2/DBT is therefore central to regulatory docking and complex control (mann2021branchedchainaminoacids pages 9-11, white2018thebckdhkinase pages 9-11, flach2023smallmoleculebranchedchain pages 8-9, flach2023smallmoleculebranchedchain pages 10-11) |
| Disease associations | **MSUD type II (E2 deficiency)** from biallelic DBT defects; **primary biliary cholangitis/cirrhosis autoantigen** (BCOADC-E2); **cuproptosis-related lipoylated mitochondrial protein**; also implicated in **RNS-mediated metabolic inhibition** and cancer biomarker studies (billington2022genomicandbiochemical pages 1-3, rong2011epithelialcellspecificity pages 1-2, springer2024cuproptosisunravelingthe pages 2-4, arp2023reactivenitrogenspecies pages 4-6) |
| Key pathways | **Branched-chain amino acid catabolism** and broader **mitochondrial oxidative metabolism**; pathway intersects with lipid metabolism, insulin resistance biology, and mitochondrial stress/cell death signaling (mann2021branchedchainaminoacids pages 9-11, bo2024primaryrolesof pages 13-15, jiao2025copperinducedcelldeath pages 3-5) |


*Table: This table summarizes the core molecular, enzymatic, structural, and disease-related properties of human DBT/BCKDH-E2. It is useful as a compact reference for functional annotation and for linking DBT’s biochemical role to MSUD, autoimmunity, and recent mitochondrial stress research.*

## 1. Primary Enzymatic Function and Catalytic Mechanism

### 1.1 Reaction Catalyzed

DBT functions as the **E2 transacylase subunit** of the BCKDH complex, which catalyzes the **irreversible oxidative decarboxylation** of branched-chain alpha-keto acids (BCKAs) derived from the three branched-chain amino acids (BCAAs): leucine, isoleucine, and valine. Specifically, the substrates are α-ketoisocaproate (KIC, from leucine), α-keto-β-methylvalerate (KMV, from isoleucine), and α-ketoisovalerate (KIV, from valine) (billington2022genomicandbiochemical pages 1-3). The overall BCKDH complex reaction converts these BCKAs into their corresponding branched-chain acyl-CoA conjugates (isovaleryl-CoA, 2-methylbutyryl-CoA, and isobutyryl-CoA, respectively), CO₂, and NADH (bo2024primaryrolesof pages 11-13).

Within this multi-step reaction, DBT's specific catalytic role is to **transfer the acyl group** from the E1-catalyzed oxidative decarboxylation intermediate to **Coenzyme A (CoA)**, producing the branched-chain acyl-CoA product and regenerating the reduced lipoyl group on the E2 subunit (bo2024primaryrolesof pages 11-13, billington2022genomicandbiochemical pages 1-3). This transacylation step is essential for coupling the decarboxylation reaction (E1) with the electron transfer to NAD⁺ (E3).

### 1.2 Lipoic Acid Prosthetic Group and "Swinging Arm" Mechanism

DBT carries a covalently attached **lipoic acid cofactor** on a conserved lysine residue within its N-terminal lipoyl-bearing domain. This lipoyl-lysine moiety functions as a flexible **"swinging arm"** that oscillates between the active sites of the E1 and E3 subunits, shuttling reaction intermediates (li2025proteinlipoylationin pages 3-4). The lipoic arm cycles between its oxidized (lipoamide) and reduced (dihydrolipoamide) forms during catalysis: it accepts the acyl group from E1 in its oxidized form, transfers the acyl group to CoA at the E2 active site, and is then re-oxidized by the E3 subunit (dihydrolipoamide dehydrogenase, encoded by DLD) with concomitant reduction of NAD⁺ to NADH (arp2023reactivenitrogenspecies pages 1-4, li2025proteinlipoylationin pages 3-4).

### 1.3 Domain Architecture and Structural Core

Each DBT monomer contains three independently functional domains connected by flexible linker regions: (i) an **N-terminal lipoyl-bearing domain** that carries the lipoic acid cofactor, (ii) an **E1/E3-binding (subunit-binding) domain** that mediates interactions with the heterotetrameric E1 (α₂β₂, encoded by BCKDHA and BCKDHB) and E3 subunits, and (iii) a **C-terminal inner-core/catalytic domain** responsible for the transacylase reaction (ahn2015interactionofperoxiredoxin pages 4-7). Twenty-four identical DBT monomers assemble into a **24-meric cubic core** that serves as the structural scaffold of the entire BCKDH complex, with multiple copies of E1 and E3 subunits attached via the subunit-binding domains (ahn2015interactionofperoxiredoxin pages 4-7, billington2022genomicandbiochemical pages 1-3). This architecture is analogous to the E2 cores of the pyruvate dehydrogenase complex (PDH) and the oxoglutarate dehydrogenase complex (OGDC) (bo2024primaryrolesof pages 11-13).

## 2. Subcellular Localization

DBT is synthesized as a **mitochondrial precursor** (flagged as "Precursor" in UniProt) containing an N-terminal mitochondrial targeting sequence that directs the protein to the **mitochondrial matrix**, where it is cleaved upon import. The assembled BCKDH complex resides in the **inner mitochondrial compartment**, functioning as an inner-mitochondrial multienzyme complex involved in BCAA oxidative catabolism (ahn2015interactionofperoxiredoxin pages 4-7, ahn2015interactionofperoxiredoxin pages 1-2). Its mitochondrial localization places it at a key metabolic node connecting amino acid catabolism to the tricarboxylic acid (TCA) cycle and oxidative phosphorylation.

## 3. Biochemical Pathway: Branched-Chain Amino Acid Catabolism

### 3.1 Position in the BCAA Catabolic Pathway

BCAA catabolism proceeds through two initial shared enzymatic steps. First, **branched-chain aminotransferase (BCAT)** catalyzes the reversible transamination of BCAAs (leucine, isoleucine, valine) with α-ketoglutarate to produce the corresponding BCKAs and glutamate. Second, the **BCKDH complex** (containing DBT as its E2 core) catalyzes the irreversible, rate-limiting oxidative decarboxylation of BCKAs to branched-chain acyl-CoA intermediates (bo2024primaryrolesof pages 11-13, bo2024primaryrolesof pages 13-15). This step commits the carbon skeletons of BCAAs to further oxidation. The branched-chain acyl-CoA products subsequently enter distinct catabolic pathways, ultimately generating acetyl-CoA, succinyl-CoA, or acetoacetate, which feed into the TCA cycle, gluconeogenesis, or ketogenesis (bo2024primaryrolesof pages 11-13).

### 3.2 Regulation of the BCKDH Complex

The activity of the BCKDH complex is tightly regulated through a **reversible phosphorylation-dephosphorylation cycle** targeting the E1α subunit (BCKDHA). **BCKDH kinase (BDK/BCKDK)** phosphorylates E1α at Ser293 (and Ser303), thereby inactivating the complex. Conversely, **protein phosphatase 2Cm (PP2Cm/PPM1K)**, a Mg²⁺/Mn²⁺-dependent mitochondrial phosphatase, dephosphorylates E1α to reactivate the complex (mann2021branchedchainaminoacids pages 9-11, bo2024primaryrolesof pages 13-15, mann2021branchedchainaminoacids pages 12-13).

Critically, the **E2 core (DBT) plays a central role in this regulatory mechanism** by serving as the binding platform for BDK. BDK physically associates with the BCKDH complex through the E2 lipoyl-binding domain (LBD), and this interaction is required for BDK to access and phosphorylate E1α (flach2023smallmoleculebranchedchain pages 8-9, mann2021branchedchainaminoacids pages 9-11). BDK and PP2Cm compete for binding to the BCKDH complex, and their relative activities determine the phosphorylation state and thus the activity of the complex (mann2021branchedchainaminoacids pages 12-13, flach2023smallmoleculebranchedchain pages 1-2). Furthermore, maximal decarboxylation activity of the BCKDH complex depends on full lipoylation of the E2 subunit (mann2021branchedchainaminoacids pages 11-12).

Recent work by Flach et al. (2023) demonstrated that small-molecule BDK inhibitors can have opposing effects depending on how they modulate the BDK-E2 interaction. Thiophene-based inhibitors destabilize BDK's interaction with the E2 core, promoting BDK release and subsequent degradation, leading to sustained BCKA lowering. In contrast, thiazole-based inhibitors stabilize BDK on the E2 core, protecting BDK from degradation and paradoxically increasing BDK protein levels and BCKA accumulation (flach2023smallmoleculebranchedchain pages 8-9, flach2023smallmoleculebranchedchain pages 1-2, flach2023smallmoleculebranchedchain pages 10-11, flach2023smallmoleculebranchedchain pages 9-10). This highlights that E2/DBT is not merely a passive structural scaffold but an active participant in the regulatory dynamics of the BCKDH complex.

### 3.3 Broader Metabolic Connections

The BDK-PP2Cm regulatory axis integrating through the E2 core connects BCAA catabolism to broader metabolic pathways, including lipid metabolism via regulation of ATP-citrate lyase (ACL) (white2018thebckdhkinase pages 9-11, wang2026branchedchainaminoacids pages 4-6). Elevated circulating BCAAs and impaired BCKDH activity have been implicated in insulin resistance, type 2 diabetes, cardiovascular disease, and cancer (bo2024primaryrolesof pages 13-15).

## 4. Novel Regulatory Mechanisms and Recent Findings

### 4.1 Reactive Nitrogen Species (RNS) Inhibition via the Lipoic Arm

A 2023 study by Arp et al. revealed that **reactive nitrogen species (RNS) can substantially inhibit BCKDH by modifying the lipoic arm on the E2/DBT subunit**. The mechanism involves RNS reacting with cellular CoA to form S-nitrosyl-CoA (SNO-CoA), which binds to the E2 CoA-binding site and delivers inactivating S-modifications to the reduced thiols of the lipoic arm. This prevents the lipoic arm from cycling between its oxidized and reduced forms, thereby abolishing its catalytic function (arp2023reactivenitrogenspecies pages 4-6, arp2023reactivenitrogenspecies pages 1-4). Concentrations of SNO-CoA as low as 0.1 μM caused over 50% activity reduction. Importantly, total DBT protein levels remained stable, but functional lipoic arm levels decreased substantially, indicating a post-translational inactivation mechanism (arp2023reactivenitrogenspecies pages 4-6). The E2 lipoic arm modification also promoted secondary inhibition of the E3 subunit through trans-nitrosylation, amplifying the overall complex inhibition (arp2023reactivenitrogenspecies pages 8-10). In muscle cells stimulated with inflammatory cytokines, nitric oxide production led to strong inhibition of BCKDC activity and BCAA oxidation (arp2023reactivenitrogenspecies pages 18-20, arp2023reactivenitrogenspecies pages 6-8).

### 4.2 Interaction with Peroxiredoxin V Under Hypoxia

Ahn et al. (2015) identified DBT as a prominent interacting partner of **Peroxiredoxin V (Prdx V)** under hypoxic stress in mouse kidney. The interaction was enhanced approximately four-fold under hypoxia compared to normoxia, with a concomitant increase in DBT enzymatic activity (~1.5-fold) (ahn2015interactionofperoxiredoxin pages 1-2, ahn2015interactionofperoxiredoxin pages 2-4). The peroxidatic cysteine residue Cys48 of Prdx V was identified as the critical residue mediating the DBT interaction, as mutations at this site abolished hypoxia-enhanced binding (ahn2015interactionofperoxiredoxin pages 4-7, ahn2015interactionofperoxiredoxin pages 7-8). This suggests that the Prdx V-DBT interaction may regulate mitochondrial BCAA metabolism under oxidative stress conditions.

### 4.3 Cuproptosis and Lipoylated DBT

The discovery of **cuproptosis** as a novel copper-dependent form of cell death has brought new attention to DBT as a lipoylated mitochondrial protein. Cuproptosis involves copper ions directly binding to lipoylated components of the TCA cycle and related mitochondrial enzymes, causing abnormal aggregation of lipoylated proteins and destabilization of iron-sulfur cluster proteins, triggering proteotoxic stress and cell death (lai2024underlyingmechanismsof pages 11-13, springer2024cuproptosisunravelingthe pages 2-4). DBT is identified as one of the key lipoylated proteins involved in this pathway, alongside DLAT (dihydrolipoamide acetyltransferase of the PDH complex) (jiao2025copperinducedcelldeath pages 3-5). Notably, DBT is typically downregulated in various cancers including kidney renal clear cell carcinoma (KIRC), where reduced DBT expression correlates with worse prognosis (lai2024underlyingmechanismsof pages 11-13). The lipoylation status of DBT, mediated by lipoyl synthase (LIAS) and ferredoxin 1 (FDX1), is a critical determinant of susceptibility to copper-induced cell death (springer2024cuproptosisunravelingthe pages 4-6, springer2024cuproptosisunravelingthe pages 2-4).

## 5. Disease Associations

### 5.1 Maple Syrup Urine Disease (MSUD) Type II

Biallelic loss-of-function mutations in the **DBT gene** cause **MSUD type II** (OMIM 248610), an autosomal recessive disorder characterized by deficient BCKDH complex activity. This leads to toxic accumulation of BCAAs (particularly leucine) and BCKAs in blood and tissues. The cardinal clinical presentation is **neonatal-onset classical MSUD**, with hyperleucinemia causing brain swelling, encephalopathy, and death without treatment (billington2022genomicandbiochemical pages 1-3). Numerous pathogenic DBT variants have been identified across diverse populations, including nonsense, missense, frameshift, and in-frame deletion mutations affecting the E2 catalytic domains (billington2022genomicandbiochemical pages 1-3, campanholi2021molecularbasisof pages 1-2, ali2018fourteennewmutations pages 5-5, fang2021geneticanalysisby pages 5-7, nguyen2020identificationofnovel pages 2-4, margutti2020maplesyrupurine pages 1-2).

In a cohort of Central American ancestry, Billington et al. (2022) identified recurrent DBT variants—a deletion of exon 2 (c.48_171del) and a missense variant (p.Ser306Pro)—causing neonatal-onset, non-thiamine-responsive classical MSUD, likely reflecting a founder effect (billington2022genomicandbiochemical pages 1-3). Some DBT variants are thiamine-responsive and can result in milder clinical manifestations, though establishing definitive genotype-phenotype correlations remains challenging due to the rarity of the disease (fang2021geneticanalysisby pages 5-7).

A landmark 2025 study by Tejedor et al. reported the first **epigenetic mechanism** causing MSUD: hypermethylation of the DBT promoter led to transcriptional silencing and reduced DBT expression in a patient without detectable coding mutations. This epimutation was associated with altered three-dimensional chromatin conformation at the DBT locus, with the gene shifting from an active transcriptional hub to a closed chromatin state marked by H3K27me3 repressive histone marks (tejedor2025integrationofmulti‐omics pages 17-18, tejedor2025integrationofmulti‐omics pages 13-16, tejedor2025integrationofmulti‐omics pages 16-17, tejedor2025integrationofmulti‐omics pages 1-2). This finding expanded the molecular basis of MSUD beyond conventional genetic mutations to include epigenetic regulation.

### 5.2 Primary Biliary Cholangitis (PBC) Autoantigen

DBT (BCOADC-E2) is recognized as one of the **mitochondrial autoantigens** targeted by anti-mitochondrial antibodies (AMAs) in primary biliary cholangitis (formerly primary biliary cirrhosis). Approximately **57% of AMA-positive PBC patients** develop autoantibodies against BCOADC-E2, making it the second most commonly recognized autoantigen after PDC-E2 (rong2011epithelialcellspecificity pages 1-2, rong2011epithelialcellspecificity pages 5-7). The critical autoepitope resides within the lipoyl domain, specifically the lipoic acid-lysine bond (gulamhusein2018pathophysiologyofprimary pages 1-6). A key pathogenic mechanism involves the persistence of immunologically intact BCOADC-E2 within apoptotic bodies (apotopes) of human intrahepatic biliary epithelial cells (HiBECs). Unlike other cell types, HiBECs fail to degrade these mitochondrial antigens during apoptosis, exposing intact epitopes to the immune system and driving autoimmune responses selective for biliary epithelium (rong2011epithelialcellspecificity pages 4-5, rong2011epithelialcellspecificity pages 5-7, rong2011epithelialcellspecificity pages 7-8).

## 6. Summary

DBT encodes the E2 transacylase subunit that forms the 24-meric structural and catalytic core of the mitochondrial BCKDH complex. Its primary enzymatic function is to transfer branched-chain acyl groups from the E1-decarboxylated intermediate to CoA via its covalently attached lipoic acid swinging arm. DBT operates within the mitochondrial matrix as the rate-limiting step of BCAA catabolism and serves as the physical platform for regulatory kinase (BDK) and phosphatase (PP2Cm) binding that controls complex activity. Loss of DBT function causes MSUD type II, while its lipoylated form serves as both a PBC autoantigen and a mediator of cuproptosis. Recent research has revealed novel regulatory mechanisms including RNS-mediated lipoic arm inactivation, hypoxia-responsive interactions with Prdx V, and epigenetic silencing of the DBT promoter as a previously unrecognized cause of MSUD.

References

1. (bo2024primaryrolesof pages 11-13): Tomoki Bo and Junichi Fujii. Primary roles of branched chain amino acids (bcaas) and their metabolism in physiology and metabolic disorders. Molecules, 30:56, Dec 2024. URL: https://doi.org/10.3390/molecules30010056, doi:10.3390/molecules30010056. This article has 61 citations.

2. (billington2022genomicandbiochemical pages 1-3): Charles J. Billington, Kimberly A. Chapman, Eyby Leon, Beatrix W. Meltzer, Seth I. Berger, Matthew Olson, Robert A. Figler, Steve A. Hoang, Cui Wanxing, Brian R. Wamhoff, M. Sol Collado, and Kristina Cusmano‐Ozog. Genomic and biochemical analysis of repeatedly observed variants in dbt in individuals with maple syrup urine disease of central american ancestry. American Journal of Medical Genetics. Part a, 188:2738-2749, Jul 2022. URL: https://doi.org/10.1002/ajmg.a.62893, doi:10.1002/ajmg.a.62893. This article has 6 citations and is from a peer-reviewed journal.

3. (ahn2015interactionofperoxiredoxin pages 4-7): Sun Hee Ahn, Hee-Young Yang, Gia Buu Tran, Joseph Kwon, Kyu-Yeol Son, Suhee Kim, Quoc Thuong Dinh, Seunggon Jung, Ha-Mi Lee, Kyoung-Oh Cho, and Tae-Hoon Lee. Interaction of peroxiredoxin v with dihydrolipoamide branched chain transacylase e2 (dbt) in mouse kidney under hypoxia. Proteome Science, Feb 2015. URL: https://doi.org/10.1186/s12953-014-0061-2, doi:10.1186/s12953-014-0061-2. This article has 25 citations and is from a peer-reviewed journal.

4. (rong2011epithelialcellspecificity pages 1-2): Guanghua Rong, Renqian Zhong, Ana Lleo, Patrick S.C. Leung, Christopher L. Bowlus, Guo-Xiang Yang, Chen-Yen Yang, Ross L. Coppel, Aftab A. Ansari, Dean A. Cuebas, Howard J. Worman, Pietro Invernizzi, Gregory J. Gores, Gary Norman, Xiao-Song He, and Eric M. Gershwin. Epithelial cell specificity and apotope recognition by serum autoantibodies in primary biliary cirrhosis. Jul 2011. URL: https://doi.org/10.1002/hep.24355, doi:10.1002/hep.24355. This article has 78 citations and is from a highest quality peer-reviewed journal.

5. (margutti2020maplesyrupurine pages 1-2): Ana Vitoria Barban Margutti, Wilson Araújo Silva, Daniel Fantozzi Garcia, Greice Andreotti de Molfetta, Adriana Aparecida Marques, Tatiana Amorim, Vânia Mesquita Gadelha Prazeres, Raquel Tavares Boy da Silva, Irene Kazue Miura, João Seda Neto, Emerson de Santana Santos, Mara Lúcia Schmitz Ferreira Santos, Charles Marques Lourenço, Tássia Tonon, Fernanda Sperb-Ludwig, Carolina Fischinger Moura de Souza, Ida Vanessa Döederlein Schwartz, and José Simon Camelo. Maple syrup urine disease in brazilian patients: variants and clinical phenotype heterogeneity. Orphanet Journal of Rare Diseases, Nov 2020. URL: https://doi.org/10.1186/s13023-020-01590-7, doi:10.1186/s13023-020-01590-7. This article has 18 citations and is from a peer-reviewed journal.

6. (ahn2015interactionofperoxiredoxin pages 1-2): Sun Hee Ahn, Hee-Young Yang, Gia Buu Tran, Joseph Kwon, Kyu-Yeol Son, Suhee Kim, Quoc Thuong Dinh, Seunggon Jung, Ha-Mi Lee, Kyoung-Oh Cho, and Tae-Hoon Lee. Interaction of peroxiredoxin v with dihydrolipoamide branched chain transacylase e2 (dbt) in mouse kidney under hypoxia. Proteome Science, Feb 2015. URL: https://doi.org/10.1186/s12953-014-0061-2, doi:10.1186/s12953-014-0061-2. This article has 25 citations and is from a peer-reviewed journal.

7. (li2025proteinlipoylationin pages 3-4): Sainan Li, Yingchao Liu, Wanye Hu, Aoli Deng, Xueying Ren, Lulu Chen, Yajuan Lu, Yunyi Wu, Hangqi Huang, Jinghao Cao, Jing Du, Jun Xia, and Yanchun Li. Protein lipoylation in cancer: metabolic reprogramming and therapeutic potential. Cell Death Discovery, Sep 2025. URL: https://doi.org/10.1038/s41420-025-02718-z, doi:10.1038/s41420-025-02718-z. This article has 12 citations and is from a peer-reviewed journal.

8. (arp2023reactivenitrogenspecies pages 1-4): Nicholas L. Arp, Gretchen L. Seim, Jordyn Josephson, and Jing Fan. Reactive nitrogen species inhibit branched chain alpha-ketoacid dehydrogenase complex and impact muscle cell metabolism. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.31.551364, doi:10.1101/2023.07.31.551364. This article has 10 citations.

9. (mann2021branchedchainaminoacids pages 9-11): Gagandeep Mann, Stephen Mora, Glory Madu, and Olasunkanmi A. J. Adegoke. Branched-chain amino acids: catabolism in skeletal muscle and implications for muscle and whole-body metabolism. Frontiers in Physiology, Jul 2021. URL: https://doi.org/10.3389/fphys.2021.702826, doi:10.3389/fphys.2021.702826. This article has 312 citations.

10. (white2018thebckdhkinase pages 9-11): Phillip J. White, Robert W. McGarrah, Paul A. Grimsrud, Shih-Chia Tso, Wen-Hsuan Yang, Jonathan M. Haldeman, Thomas Grenier-Larouche, Jie An, Amanda L. Lapworth, Inna Astapova, Sarah A. Hannou, Tabitha George, Michelle Arlotto, Lyra B. Olson, Michelle Lai, Guo-Fang Zhang, Olga Ilkayeva, Mark A. Herman, R. Max Wynn, David T. Chuang, and Christopher B. Newgard. The bckdh kinase and phosphatase integrate bcaa and lipid metabolism via regulation of atp-citrate lyase. Cell metabolism, 27 6:1281-1293.e7, Jun 2018. URL: https://doi.org/10.1016/j.cmet.2018.04.015, doi:10.1016/j.cmet.2018.04.015. This article has 384 citations and is from a highest quality peer-reviewed journal.

11. (flach2023smallmoleculebranchedchain pages 8-9): Rachel J. Roth Flach, Eliza Bollinger, Allan R. Reyes, Brigitte Laforest, Bethany L. Kormos, Shenping Liu, Matthew R. Reese, Luis A. Martinez Alsina, Leanne Buzon, Yuan Zhang, Bruce Bechle, Amy Rosado, Parag V. Sahasrabudhe, John Knafels, Samit K. Bhattacharya, Kiyoyuki Omoto, John C. Stansfield, Liam D. Hurley, LouJin Song, Lina Luo, Susanne B. Breitkopf, Mara Monetti, Teresa Cunio, Brendan Tierney, Frank J. Geoly, Jake Delmore, C. Parker Siddall, Liang Xue, Ka N. Yip, Amit S. Kalgutkar, Russell A. Miller, Bei B. Zhang, and Kevin J. Filipski. Small molecule branched-chain ketoacid dehydrogenase kinase (bdk) inhibitors with opposing effects on bdk protein levels. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40536-y, doi:10.1038/s41467-023-40536-y. This article has 38 citations and is from a highest quality peer-reviewed journal.

12. (flach2023smallmoleculebranchedchain pages 10-11): Rachel J. Roth Flach, Eliza Bollinger, Allan R. Reyes, Brigitte Laforest, Bethany L. Kormos, Shenping Liu, Matthew R. Reese, Luis A. Martinez Alsina, Leanne Buzon, Yuan Zhang, Bruce Bechle, Amy Rosado, Parag V. Sahasrabudhe, John Knafels, Samit K. Bhattacharya, Kiyoyuki Omoto, John C. Stansfield, Liam D. Hurley, LouJin Song, Lina Luo, Susanne B. Breitkopf, Mara Monetti, Teresa Cunio, Brendan Tierney, Frank J. Geoly, Jake Delmore, C. Parker Siddall, Liang Xue, Ka N. Yip, Amit S. Kalgutkar, Russell A. Miller, Bei B. Zhang, and Kevin J. Filipski. Small molecule branched-chain ketoacid dehydrogenase kinase (bdk) inhibitors with opposing effects on bdk protein levels. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40536-y, doi:10.1038/s41467-023-40536-y. This article has 38 citations and is from a highest quality peer-reviewed journal.

13. (springer2024cuproptosisunravelingthe pages 2-4): Chloe Springer, Danish Humayun, and Rachid Skouta. Cuproptosis: unraveling the mechanisms of copper-induced cell death and its implication in cancer therapy. Cancers, 16:647, Feb 2024. URL: https://doi.org/10.3390/cancers16030647, doi:10.3390/cancers16030647. This article has 93 citations.

14. (arp2023reactivenitrogenspecies pages 4-6): Nicholas L. Arp, Gretchen L. Seim, Jordyn Josephson, and Jing Fan. Reactive nitrogen species inhibit branched chain alpha-ketoacid dehydrogenase complex and impact muscle cell metabolism. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.31.551364, doi:10.1101/2023.07.31.551364. This article has 10 citations.

15. (bo2024primaryrolesof pages 13-15): Tomoki Bo and Junichi Fujii. Primary roles of branched chain amino acids (bcaas) and their metabolism in physiology and metabolic disorders. Molecules, 30:56, Dec 2024. URL: https://doi.org/10.3390/molecules30010056, doi:10.3390/molecules30010056. This article has 61 citations.

16. (jiao2025copperinducedcelldeath pages 3-5): Yujuan Jiao, Hongxin Wang, Meng Zhu, Teng-fei Liu, Yuqi Li, Shuo Yang, Minghui Zhang, and Lei Zhang. Copper-induced cell death mechanisms and their role in the tumor microenvironment. Frontiers in Cell Death, Oct 2025. URL: https://doi.org/10.3389/fceld.2025.1628470, doi:10.3389/fceld.2025.1628470. This article has 8 citations.

17. (mann2021branchedchainaminoacids pages 12-13): Gagandeep Mann, Stephen Mora, Glory Madu, and Olasunkanmi A. J. Adegoke. Branched-chain amino acids: catabolism in skeletal muscle and implications for muscle and whole-body metabolism. Frontiers in Physiology, Jul 2021. URL: https://doi.org/10.3389/fphys.2021.702826, doi:10.3389/fphys.2021.702826. This article has 312 citations.

18. (flach2023smallmoleculebranchedchain pages 1-2): Rachel J. Roth Flach, Eliza Bollinger, Allan R. Reyes, Brigitte Laforest, Bethany L. Kormos, Shenping Liu, Matthew R. Reese, Luis A. Martinez Alsina, Leanne Buzon, Yuan Zhang, Bruce Bechle, Amy Rosado, Parag V. Sahasrabudhe, John Knafels, Samit K. Bhattacharya, Kiyoyuki Omoto, John C. Stansfield, Liam D. Hurley, LouJin Song, Lina Luo, Susanne B. Breitkopf, Mara Monetti, Teresa Cunio, Brendan Tierney, Frank J. Geoly, Jake Delmore, C. Parker Siddall, Liang Xue, Ka N. Yip, Amit S. Kalgutkar, Russell A. Miller, Bei B. Zhang, and Kevin J. Filipski. Small molecule branched-chain ketoacid dehydrogenase kinase (bdk) inhibitors with opposing effects on bdk protein levels. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40536-y, doi:10.1038/s41467-023-40536-y. This article has 38 citations and is from a highest quality peer-reviewed journal.

19. (mann2021branchedchainaminoacids pages 11-12): Gagandeep Mann, Stephen Mora, Glory Madu, and Olasunkanmi A. J. Adegoke. Branched-chain amino acids: catabolism in skeletal muscle and implications for muscle and whole-body metabolism. Frontiers in Physiology, Jul 2021. URL: https://doi.org/10.3389/fphys.2021.702826, doi:10.3389/fphys.2021.702826. This article has 312 citations.

20. (flach2023smallmoleculebranchedchain pages 9-10): Rachel J. Roth Flach, Eliza Bollinger, Allan R. Reyes, Brigitte Laforest, Bethany L. Kormos, Shenping Liu, Matthew R. Reese, Luis A. Martinez Alsina, Leanne Buzon, Yuan Zhang, Bruce Bechle, Amy Rosado, Parag V. Sahasrabudhe, John Knafels, Samit K. Bhattacharya, Kiyoyuki Omoto, John C. Stansfield, Liam D. Hurley, LouJin Song, Lina Luo, Susanne B. Breitkopf, Mara Monetti, Teresa Cunio, Brendan Tierney, Frank J. Geoly, Jake Delmore, C. Parker Siddall, Liang Xue, Ka N. Yip, Amit S. Kalgutkar, Russell A. Miller, Bei B. Zhang, and Kevin J. Filipski. Small molecule branched-chain ketoacid dehydrogenase kinase (bdk) inhibitors with opposing effects on bdk protein levels. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40536-y, doi:10.1038/s41467-023-40536-y. This article has 38 citations and is from a highest quality peer-reviewed journal.

21. (wang2026branchedchainaminoacids pages 4-6): Song-nan Wang, Yu-xi Liu, Gui-yan Sun, Xin Liu, Yue Sun, Yi-xi Ma, Shun-yu Ning, and Yan Shi. Branched-chain amino acids from plants and the metabolic syndrome: pathways and pharmacological applications. Frontiers in Nutrition, May 2026. URL: https://doi.org/10.3389/fnut.2026.1805807, doi:10.3389/fnut.2026.1805807. This article has 0 citations.

22. (arp2023reactivenitrogenspecies pages 8-10): Nicholas L. Arp, Gretchen L. Seim, Jordyn Josephson, and Jing Fan. Reactive nitrogen species inhibit branched chain alpha-ketoacid dehydrogenase complex and impact muscle cell metabolism. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.31.551364, doi:10.1101/2023.07.31.551364. This article has 10 citations.

23. (arp2023reactivenitrogenspecies pages 18-20): Nicholas L. Arp, Gretchen L. Seim, Jordyn Josephson, and Jing Fan. Reactive nitrogen species inhibit branched chain alpha-ketoacid dehydrogenase complex and impact muscle cell metabolism. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.31.551364, doi:10.1101/2023.07.31.551364. This article has 10 citations.

24. (arp2023reactivenitrogenspecies pages 6-8): Nicholas L. Arp, Gretchen L. Seim, Jordyn Josephson, and Jing Fan. Reactive nitrogen species inhibit branched chain alpha-ketoacid dehydrogenase complex and impact muscle cell metabolism. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.31.551364, doi:10.1101/2023.07.31.551364. This article has 10 citations.

25. (ahn2015interactionofperoxiredoxin pages 2-4): Sun Hee Ahn, Hee-Young Yang, Gia Buu Tran, Joseph Kwon, Kyu-Yeol Son, Suhee Kim, Quoc Thuong Dinh, Seunggon Jung, Ha-Mi Lee, Kyoung-Oh Cho, and Tae-Hoon Lee. Interaction of peroxiredoxin v with dihydrolipoamide branched chain transacylase e2 (dbt) in mouse kidney under hypoxia. Proteome Science, Feb 2015. URL: https://doi.org/10.1186/s12953-014-0061-2, doi:10.1186/s12953-014-0061-2. This article has 25 citations and is from a peer-reviewed journal.

26. (ahn2015interactionofperoxiredoxin pages 7-8): Sun Hee Ahn, Hee-Young Yang, Gia Buu Tran, Joseph Kwon, Kyu-Yeol Son, Suhee Kim, Quoc Thuong Dinh, Seunggon Jung, Ha-Mi Lee, Kyoung-Oh Cho, and Tae-Hoon Lee. Interaction of peroxiredoxin v with dihydrolipoamide branched chain transacylase e2 (dbt) in mouse kidney under hypoxia. Proteome Science, Feb 2015. URL: https://doi.org/10.1186/s12953-014-0061-2, doi:10.1186/s12953-014-0061-2. This article has 25 citations and is from a peer-reviewed journal.

27. (lai2024underlyingmechanismsof pages 11-13): Shiue-Wei Lai, Pei-Wei Weng, Vijesh Kumar Yadav, Narpati Wesa Pikatan, Chi-Tai Yeh, Ming-Shou Hsieh, and Chu-Lin Chou. Underlying mechanisms of novel cuproptosis-related dihydrolipoamide branched-chain transacylase e2 (dbt) signature in sunitinib-resistant clear-cell renal cell carcinoma. Aging, 16:2679-2701, Feb 2024. URL: https://doi.org/10.18632/aging.205504, doi:10.18632/aging.205504. This article has 7 citations and is from a peer-reviewed journal.

28. (springer2024cuproptosisunravelingthe pages 4-6): Chloe Springer, Danish Humayun, and Rachid Skouta. Cuproptosis: unraveling the mechanisms of copper-induced cell death and its implication in cancer therapy. Cancers, 16:647, Feb 2024. URL: https://doi.org/10.3390/cancers16030647, doi:10.3390/cancers16030647. This article has 93 citations.

29. (campanholi2021molecularbasisof pages 1-2): Diana Ruffato Resende Campanholi, Ana Vitoria Barban Margutti, Wilson A. Silva, Daniel F. Garcia, Greice A. Molfetta, Adriana A. Marques, Ida Vanessa Döederlein Schwartz, V. Cornejo, Valerie Hamilton, Gabriela Castro, Fernanda Sperb‐Ludwig, Ester S. Borges, and José S. Camelo. Molecular basis of various forms of maple syrup urine disease in chilean patients. Molecular Genetics & Genomic Medicine, May 2021. URL: https://doi.org/10.1002/mgg3.1616, doi:10.1002/mgg3.1616. This article has 10 citations and is from a peer-reviewed journal.

30. (ali2018fourteennewmutations pages 5-5): Ernie Zuraida Ali and Lock-Hock Ngu. Fourteen new mutations of bckdha, bckdhb and dbt genes associated with maple syrup urine disease (msud) in malaysian population. Dec 2018. URL: https://doi.org/10.1016/j.ymgmr.2018.08.006, doi:10.1016/j.ymgmr.2018.08.006. This article has 43 citations.

31. (fang2021geneticanalysisby pages 5-7): Xiaohua Fang, Xiaofan Zhu, Yin Feng, Ying Bai, Xuechao Zhao, Ning Liu, and Xiangdong Kong. Genetic analysis by targeted next-generation sequencing and novel variation identification of maple syrup urine disease in chinese han population. Scientific Reports, Sep 2021. URL: https://doi.org/10.1038/s41598-021-98357-2, doi:10.1038/s41598-021-98357-2. This article has 10 citations and is from a peer-reviewed journal.

32. (nguyen2020identificationofnovel pages 2-4): Thi T. N. Nguyen, Chi D. Vu, Ngoc L. Nguyen, Thi T. H. Nguyen, Ngoc K. Nguyen, and Huy H. Nguyen. Identification of novel mutations in bckdhb and dbt genes in vietnamese patients with maple sirup urine disease. Molecular Genetics & Genomic Medicine, Jun 2020. URL: https://doi.org/10.1002/mgg3.1337, doi:10.1002/mgg3.1337. This article has 3 citations and is from a peer-reviewed journal.

33. (tejedor2025integrationofmulti‐omics pages 17-18): Juan Ramón Tejedor, Alejandro Soriano‐Sexto, Leonardo Beccari, Natalia Castejón‐Fernández, Patricia Correcher, Lidia Sainz‐Ledo, Juan José Alba‐Linares, Rocío G. Urdinguio, Magdalena Ugarte, Agustín F. Fernández, Pilar Rodríguez‐Pombo, Mario F. Fraga, and Belén Pérez. Integration of multi‐omics layers empowers precision diagnosis through unveiling pathogenic mechanisms on maple syrup urine disease. Journal of Inherited Metabolic Disease, Dec 2025. URL: https://doi.org/10.1002/jimd.12829, doi:10.1002/jimd.12829. This article has 4 citations and is from a peer-reviewed journal.

34. (tejedor2025integrationofmulti‐omics pages 13-16): Juan Ramón Tejedor, Alejandro Soriano‐Sexto, Leonardo Beccari, Natalia Castejón‐Fernández, Patricia Correcher, Lidia Sainz‐Ledo, Juan José Alba‐Linares, Rocío G. Urdinguio, Magdalena Ugarte, Agustín F. Fernández, Pilar Rodríguez‐Pombo, Mario F. Fraga, and Belén Pérez. Integration of multi‐omics layers empowers precision diagnosis through unveiling pathogenic mechanisms on maple syrup urine disease. Journal of Inherited Metabolic Disease, Dec 2025. URL: https://doi.org/10.1002/jimd.12829, doi:10.1002/jimd.12829. This article has 4 citations and is from a peer-reviewed journal.

35. (tejedor2025integrationofmulti‐omics pages 16-17): Juan Ramón Tejedor, Alejandro Soriano‐Sexto, Leonardo Beccari, Natalia Castejón‐Fernández, Patricia Correcher, Lidia Sainz‐Ledo, Juan José Alba‐Linares, Rocío G. Urdinguio, Magdalena Ugarte, Agustín F. Fernández, Pilar Rodríguez‐Pombo, Mario F. Fraga, and Belén Pérez. Integration of multi‐omics layers empowers precision diagnosis through unveiling pathogenic mechanisms on maple syrup urine disease. Journal of Inherited Metabolic Disease, Dec 2025. URL: https://doi.org/10.1002/jimd.12829, doi:10.1002/jimd.12829. This article has 4 citations and is from a peer-reviewed journal.

36. (tejedor2025integrationofmulti‐omics pages 1-2): Juan Ramón Tejedor, Alejandro Soriano‐Sexto, Leonardo Beccari, Natalia Castejón‐Fernández, Patricia Correcher, Lidia Sainz‐Ledo, Juan José Alba‐Linares, Rocío G. Urdinguio, Magdalena Ugarte, Agustín F. Fernández, Pilar Rodríguez‐Pombo, Mario F. Fraga, and Belén Pérez. Integration of multi‐omics layers empowers precision diagnosis through unveiling pathogenic mechanisms on maple syrup urine disease. Journal of Inherited Metabolic Disease, Dec 2025. URL: https://doi.org/10.1002/jimd.12829, doi:10.1002/jimd.12829. This article has 4 citations and is from a peer-reviewed journal.

37. (rong2011epithelialcellspecificity pages 5-7): Guanghua Rong, Renqian Zhong, Ana Lleo, Patrick S.C. Leung, Christopher L. Bowlus, Guo-Xiang Yang, Chen-Yen Yang, Ross L. Coppel, Aftab A. Ansari, Dean A. Cuebas, Howard J. Worman, Pietro Invernizzi, Gregory J. Gores, Gary Norman, Xiao-Song He, and Eric M. Gershwin. Epithelial cell specificity and apotope recognition by serum autoantibodies in primary biliary cirrhosis. Jul 2011. URL: https://doi.org/10.1002/hep.24355, doi:10.1002/hep.24355. This article has 78 citations and is from a highest quality peer-reviewed journal.

38. (gulamhusein2018pathophysiologyofprimary pages 1-6): Aliya F. Gulamhusein and Gideon M. Hirschfield. Pathophysiology of primary biliary cholangitis. Jun 2018. URL: https://doi.org/10.1016/j.bpg.2018.05.012, doi:10.1016/j.bpg.2018.05.012. This article has 43 citations.

39. (rong2011epithelialcellspecificity pages 4-5): Guanghua Rong, Renqian Zhong, Ana Lleo, Patrick S.C. Leung, Christopher L. Bowlus, Guo-Xiang Yang, Chen-Yen Yang, Ross L. Coppel, Aftab A. Ansari, Dean A. Cuebas, Howard J. Worman, Pietro Invernizzi, Gregory J. Gores, Gary Norman, Xiao-Song He, and Eric M. Gershwin. Epithelial cell specificity and apotope recognition by serum autoantibodies in primary biliary cirrhosis. Jul 2011. URL: https://doi.org/10.1002/hep.24355, doi:10.1002/hep.24355. This article has 78 citations and is from a highest quality peer-reviewed journal.

40. (rong2011epithelialcellspecificity pages 7-8): Guanghua Rong, Renqian Zhong, Ana Lleo, Patrick S.C. Leung, Christopher L. Bowlus, Guo-Xiang Yang, Chen-Yen Yang, Ross L. Coppel, Aftab A. Ansari, Dean A. Cuebas, Howard J. Worman, Pietro Invernizzi, Gregory J. Gores, Gary Norman, Xiao-Song He, and Eric M. Gershwin. Epithelial cell specificity and apotope recognition by serum autoantibodies in primary biliary cirrhosis. Jul 2011. URL: https://doi.org/10.1002/hep.24355, doi:10.1002/hep.24355. This article has 78 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](DBT-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. billington2022genomicandbiochemical pages 1-3
2. bo2024primaryrolesof pages 11-13
3. li2025proteinlipoylationin pages 3-4
4. ahn2015interactionofperoxiredoxin pages 4-7
5. mann2021branchedchainaminoacids pages 11-12
6. bo2024primaryrolesof pages 13-15
7. arp2023reactivenitrogenspecies pages 4-6
8. arp2023reactivenitrogenspecies pages 8-10
9. jiao2025copperinducedcelldeath pages 3-5
10. lai2024underlyingmechanismsof pages 11-13
11. fang2021geneticanalysisby pages 5-7
12. gulamhusein2018pathophysiologyofprimary pages 1-6
13. rong2011epithelialcellspecificity pages 1-2
14. margutti2020maplesyrupurine pages 1-2
15. ahn2015interactionofperoxiredoxin pages 1-2
16. arp2023reactivenitrogenspecies pages 1-4
17. mann2021branchedchainaminoacids pages 9-11
18. white2018thebckdhkinase pages 9-11
19. flach2023smallmoleculebranchedchain pages 8-9
20. flach2023smallmoleculebranchedchain pages 10-11
21. springer2024cuproptosisunravelingthe pages 2-4
22. mann2021branchedchainaminoacids pages 12-13
23. flach2023smallmoleculebranchedchain pages 1-2
24. flach2023smallmoleculebranchedchain pages 9-10
25. wang2026branchedchainaminoacids pages 4-6
26. arp2023reactivenitrogenspecies pages 18-20
27. arp2023reactivenitrogenspecies pages 6-8
28. ahn2015interactionofperoxiredoxin pages 2-4
29. ahn2015interactionofperoxiredoxin pages 7-8
30. springer2024cuproptosisunravelingthe pages 4-6
31. campanholi2021molecularbasisof pages 1-2
32. ali2018fourteennewmutations pages 5-5
33. nguyen2020identificationofnovel pages 2-4
34. rong2011epithelialcellspecificity pages 5-7
35. rong2011epithelialcellspecificity pages 4-5
36. rong2011epithelialcellspecificity pages 7-8
37. https://doi.org/10.3390/molecules30010056,
38. https://doi.org/10.1002/ajmg.a.62893,
39. https://doi.org/10.1186/s12953-014-0061-2,
40. https://doi.org/10.1002/hep.24355,
41. https://doi.org/10.1186/s13023-020-01590-7,
42. https://doi.org/10.1038/s41420-025-02718-z,
43. https://doi.org/10.1101/2023.07.31.551364,
44. https://doi.org/10.3389/fphys.2021.702826,
45. https://doi.org/10.1016/j.cmet.2018.04.015,
46. https://doi.org/10.1038/s41467-023-40536-y,
47. https://doi.org/10.3390/cancers16030647,
48. https://doi.org/10.3389/fceld.2025.1628470,
49. https://doi.org/10.3389/fnut.2026.1805807,
50. https://doi.org/10.18632/aging.205504,
51. https://doi.org/10.1002/mgg3.1616,
52. https://doi.org/10.1016/j.ymgmr.2018.08.006,
53. https://doi.org/10.1038/s41598-021-98357-2,
54. https://doi.org/10.1002/mgg3.1337,
55. https://doi.org/10.1002/jimd.12829,
56. https://doi.org/10.1016/j.bpg.2018.05.012,