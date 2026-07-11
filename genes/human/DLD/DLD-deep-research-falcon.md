---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T19:27:49.226431'
end_time: '2026-07-05T19:55:08.904246'
duration_seconds: 1639.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: DLD
  gene_symbol: DLD
  uniprot_accession: P09622
  protein_description: 'RecName: Full=Dihydrolipoyl dehydrogenase, mitochondrial {ECO:0000305};
    EC=1.8.1.4 {ECO:0000269|PubMed:15712224, ECO:0000269|PubMed:16442803, ECO:0000269|PubMed:16770810,
    ECO:0000269|PubMed:17404228, ECO:0000269|PubMed:20160912, ECO:0000269|PubMed:20385101};
    AltName: Full=Dihydrolipoamide dehydrogenase; AltName: Full=Glycine cleavage system
    L protein; Flags: Precursor;'
  gene_info: Name=DLD {ECO:0000312|HGNC:HGNC:2898}; Synonyms=GCSL, LAD, PHE3;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the class-I pyridine nucleotide-disulfide
  protein_domains: Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188);
    FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156);
    Lipoamide_DH. (IPR006258)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 55
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: DLD-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: DLD-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P09622
- **Protein Description:** RecName: Full=Dihydrolipoyl dehydrogenase, mitochondrial {ECO:0000305}; EC=1.8.1.4 {ECO:0000269|PubMed:15712224, ECO:0000269|PubMed:16442803, ECO:0000269|PubMed:16770810, ECO:0000269|PubMed:17404228, ECO:0000269|PubMed:20160912, ECO:0000269|PubMed:20385101}; AltName: Full=Dihydrolipoamide dehydrogenase; AltName: Full=Glycine cleavage system L protein; Flags: Precursor;
- **Gene Information:** Name=DLD {ECO:0000312|HGNC:HGNC:2898}; Synonyms=GCSL, LAD, PHE3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the class-I pyridine nucleotide-disulfide
- **Key Domains:** Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156); Lipoamide_DH. (IPR006258)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DLD" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DLD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DLD** (gene ID: DLD, UniProt: P09622) in human.

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
- **UniProt Accession:** P09622
- **Protein Description:** RecName: Full=Dihydrolipoyl dehydrogenase, mitochondrial {ECO:0000305}; EC=1.8.1.4 {ECO:0000269|PubMed:15712224, ECO:0000269|PubMed:16442803, ECO:0000269|PubMed:16770810, ECO:0000269|PubMed:17404228, ECO:0000269|PubMed:20160912, ECO:0000269|PubMed:20385101}; AltName: Full=Dihydrolipoamide dehydrogenase; AltName: Full=Glycine cleavage system L protein; Flags: Precursor;
- **Gene Information:** Name=DLD {ECO:0000312|HGNC:HGNC:2898}; Synonyms=GCSL, LAD, PHE3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the class-I pyridine nucleotide-disulfide
- **Key Domains:** Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156); Lipoamide_DH. (IPR006258)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DLD" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DLD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DLD** (gene ID: DLD, UniProt: P09622) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human DLD (Dihydrolipoamide Dehydrogenase, Mitochondrial)

**Gene:** DLD (synonyms: GCSL, LAD, PHE3) | **UniProt:** P09622 | **EC:** 1.8.1.4 | **Organism:** Homo sapiens

---

## 1. Gene Identity and Protein Overview

The human *DLD* gene encodes dihydrolipoamide dehydrogenase (also known as dihydrolipoyl dehydrogenase, lipoamide dehydrogenase [LADH], or the E3 subunit), a flavin adenine dinucleotide (FAD)-dependent disulfide oxidoreductase belonging to the class-I pyridine nucleotide-disulfide oxidoreductase family (yan2023rolesofdihydrolipoamide pages 1-3). The mature protein functions as an obligate homodimer, with each monomer being approximately 50–54 kDa and comprising 474 amino acid residues after cleavage of the mitochondrial targeting sequence (szabo2019underlyingmolecularalterations pages 3-4, duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6). DLD is synthesized as a precursor with an N-terminal mitochondrial targeting peptide that is proteolytically removed upon import into the mitochondrial matrix, where it carries out its primary functions (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-4).

---

## 2. Enzymatic Function and Catalytic Mechanism

### 2.1 Primary Reaction

DLD catalyzes the NAD⁺-dependent oxidation of dihydrolipoamide to lipoamide:

**Dihydrolipoamide + NAD⁺ → Lipoamide + NADH + H⁺**

This reaction regenerates the oxidized lipoyl cofactor covalently attached to the E2 subunits (or H-protein in the glycine cleavage system) of its partner multienzyme complexes, while simultaneously producing NADH for the mitochondrial electron transport chain (yan2023rolesofdihydrolipoamide pages 1-3, szabo2023structuralandbiochemical pages 1-3, duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6).

### 2.2 Catalytic Mechanism

DLD employs a ping-pong bi-bi mechanism in which two half-reactions are spatially separated by the non-covalently bound FAD prosthetic group (szabo2019underlyingmolecularalterations pages 3-4, szabo2023structuralandbiochemical pages 1-3). The electron transfer pathway proceeds as follows:

1. **First half-reaction (si face of FAD):** The dihydrolipoamide substrate enters the active site through an approximately 10-Å-long hydrophobic channel. Electrons are transferred from the dithiol of dihydrolipoamide to the redox-active disulfide bond formed by Cys45 and Cys50, reducing it. The electrons then flow to the FAD isoalloxazine ring, reducing it to FADH₂ (szabo2023structuralandbiochemical pages 1-3, yan2023rolesofdihydrolipoamide pages 5-7).

2. **Second half-reaction (re face of FAD):** Electrons are transferred from FADH₂ to NAD⁺, producing NADH. The catalytic base His452′ from the adjacent monomer in the homodimer is critical for this step (szabo2023structuralandbiochemical pages 1-3).

A solvent-accessible H⁺/H₂O channel facilitates catalysis by providing an outlet for water molecules during substrate binding and hydrogen ion release during NAD⁺ reduction (szabo2019underlyingmolecularalterations pages 3-4). Importantly, both monomers contribute catalytically important residues to each active site, making the homodimeric assembly essential for function (szabo2023structuralandbiochemical pages 1-3).

### 2.3 Structural Organization

Each DLD monomer contains four distinct structural domains: (1) the FAD-binding domain (residues 1–149), (2) the NAD⁺/NADH-binding domain (residues 150–282), (3) the central domain (residues 283–350), and (4) the C-terminal interface domain (residues 351–474) (szabo2019underlyingmolecularalterations pages 3-4, duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6). The active site is divided by the FAD prosthetic group into two compartments: the lipoamide-binding site containing the redox-active Cys45-Cys50 disulfide, and the NAD⁺/NADH-binding site (szabo2019underlyingmolecularalterations pages 3-4). High-resolution crystal structures of wild-type human E3 have been determined at 1.75 Å resolution (szabo2019underlyingmolecularalterations pages 3-4).

---

## 3. Participation in Mitochondrial Multienzyme Complexes

DLD is unique among metabolic enzymes in serving as the shared E3 component of five distinct mitochondrial multienzyme systems (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, szabo2024mitochondrialalphaketoacid pages 1-6, yan2023rolesofdihydrolipoamide pages 1-3). In all of these, DLD performs the same terminal catalytic step: reoxidation of the dihydrolipoyl moiety on the E2 subunit (or H-protein) with concomitant reduction of NAD⁺ to NADH (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, szabo2023structuralandbiochemical pages 1-3).

| Complex Name | Abbreviation | Metabolic Pathway | Overall Reaction Catalyzed | E1 / E2 subunits (or analogous components) |
|---|---|---|---|---|
| Pyruvate dehydrogenase complex | PDHc | Carbohydrate metabolism; links glycolysis to the TCA cycle | Pyruvate + CoA + NAD+ → Acetyl-CoA + CO2 + NADH. DLD/E3 catalyzes the shared terminal step: oxidation of E2-bound dihydrolipoamide to lipoamide with reduction of NAD+ to NADH. | E1: pyruvate dehydrogenase (PDHA1/PDHB heterotetramer); E2: dihydrolipoamide S-acetyltransferase (DLAT). In human PDHc, E3 is tethered via E3-binding protein (PDHX/E3BP). (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, duarte2021dihydrolipoamidedehydrogenasepyruvate pages 2-4, brautigam2006structuralinsightinto pages 1-2, szabo2024mitochondrialalphaketoacid pages 16-19) |
| α-Ketoglutarate dehydrogenase complex | KGDHc | Tricarboxylic acid cycle | 2-Oxoglutarate + CoA + NAD+ → Succinyl-CoA + CO2 + NADH. DLD/E3 reoxidizes the lipoyl cofactor on E2 and transfers electrons to NAD+. | E1: 2-oxoglutarate dehydrogenase (OGDH/OGDHL family context); E2: dihydrolipoyl succinyltransferase (DLST). (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, szabo2024mitochondrialalphaketoacid pages 1-6, hansen2022theαketoglutaratedehydrogenase pages 2-4) |
| Branched-chain α-keto acid dehydrogenase complex | BCKDHc | Branched-chain amino acid catabolism (leucine, isoleucine, valine) | Branched-chain α-keto acids + CoA + NAD+ → branched-chain acyl-CoAs + CO2 + NADH. DLD/E3 performs the common final reoxidation of dihydrolipoamide and reduction of NAD+ to NADH. | E1: branched-chain α-keto acid dehydrogenase E1 (BCKDHA/BCKDHB); E2: dihydrolipoamide branched-chain transacylase E2 (DBT). (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, szabo2024mitochondrialalphaketoacid pages 1-6, yan2023rolesofdihydrolipoamide pages 1-3) |
| α-Ketoadipate dehydrogenase complex | KADHc | Lysine, hydroxylysine, and tryptophan catabolism | 2-Oxoadipate + CoA + NAD+ → glutaryl-CoA + CO2 + NADH. DLD/E3 again carries out the terminal lipoyl reoxidation/NADH-producing step. | E1: 2-oxoadipate dehydrogenase (DHTKD1); E2: shares the E2 component DLST with KGDHc in mammalian mitochondria. (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, szabo2024mitochondrialalphaketoacid pages 1-6) |
| Glycine cleavage system | GCS | Glycine degradation and mitochondrial one-carbon metabolism | Glycine + tetrahydrofolate + NAD+ → 5,10-methylene-THF + CO2 + NH3 + NADH. DLD functions as the L-protein, reoxidizing the reduced lipoyl moiety on H-protein while reducing NAD+ to NADH. | Analogous components rather than E1/E2: P-protein = glycine decarboxylase (GLDC), H-protein = GCSH, T-protein = aminomethyltransferase (AMT), L-protein = DLD. (yan2023rolesofdihydrolipoamide pages 1-3, kikuchi2008glycinecleavagesystem pages 2-5, leung2021glycinecleavagesystem pages 1-2) |


*Table: This table summarizes the mitochondrial enzyme systems that use human DLD as their shared E3/L-protein component. It highlights the pathway context, overall chemistry, and partner catalytic subunits/components needed to interpret DLD’s functional annotation.*

### 3.1 Pyruvate Dehydrogenase Complex (PDHc)

The human PDHc is a ~9.5 MDa macromolecular assembly with icosahedral symmetry, comprising approximately 30 E1p subunits, 60 E2p subunits, and 12 E3 homodimers, along with 12 copies of E3-binding protein (E3BP/PDHX) (brautigam2006structuralinsightinto pages 1-2, duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-4). PDHc catalyzes the irreversible oxidative decarboxylation of pyruvate to acetyl-CoA, linking glycolysis to the TCA cycle (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 2-4). In eukaryotic PDHc, DLD does not bind E2 directly; instead, it is tethered to the complex via E3BP, which contains a specific E3-binding domain (E3BD) that contacts the E3 homodimer across its 2-fold symmetry axis with extremely tight affinity (Kd ~7.8 × 10⁻²¹⁰ M) (brautigam2006structuralinsightinto pages 1-2, szabo2024mitochondrialalphaketoacid pages 16-19, brautigam2006structuralinsightinto pages 2-3). Recent in-situ cryo-electron tomography has revealed that up to 12 E3 homodimers localize primarily along the pentagonal openings of the PDHc core, and that the number of peripheral E1 and E3 components varies dynamically among individual PDHc particles, suggesting an activity regulation mechanism coordinating metabolic demands (wang2025dynamicsofthe pages 1-3).

### 3.2 α-Ketoglutarate Dehydrogenase Complex (KGDHc)

KGDHc catalyzes the rate-limiting step of the TCA cycle, converting α-ketoglutarate to succinyl-CoA. DLD serves as the E3 subunit alongside OGDH (E1) and DLST (E2) (szabo2024mitochondrialalphaketoacid pages 1-6, hansen2022theαketoglutaratedehydrogenase pages 2-4). This complex is particularly significant as a signaling hub controlling post-translational modifications (succinylation), hypoxic responses, and ROS homeostasis in mitochondria (hansen2022theαketoglutaratedehydrogenase pages 2-4).

### 3.3 Branched-Chain α-Keto Acid Dehydrogenase Complex (BCKDHc)

BCKDHc catalyzes the oxidative decarboxylation of branched-chain α-keto acids derived from leucine, isoleucine, and valine catabolism (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, szabo2024mitochondrialalphaketoacid pages 1-6).

### 3.4 α-Ketoadipate Dehydrogenase Complex (KADHc)

KADHc participates in the catabolism of lysine, hydroxylysine, and tryptophan (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6, szabo2024mitochondrialalphaketoacid pages 1-6).

### 3.5 Glycine Cleavage System (GCS)

In the GCS, DLD functions as the L-protein, catalyzing the final step of glycine degradation by reoxidizing the reduced lipoyl moiety on H-protein (GCSH) while reducing NAD⁺ to NADH. The overall GCS reaction yields CO₂, NH₃, 5,10-methylene-tetrahydrofolate, and NADH from glycine (kikuchi2008glycinecleavagesystem pages 2-5, leung2021glycinecleavagesystem pages 1-2). Unlike the E1/E2 nomenclature used for the α-keto acid dehydrogenase complexes, the GCS uses the designations P-protein (GLDC), H-protein (GCSH), T-protein (AMT), and L-protein (DLD) (leung2021glycinecleavagesystem pages 1-2).

---

## 4. Subcellular Localization

DLD is synthesized as a precursor protein in the cytosol and imported into the mitochondrial matrix, where its targeting peptide is cleaved to produce the mature enzyme (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-4, duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6). The mitochondrial matrix is the site of action for all five multienzyme complexes in which DLD participates (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-4, babady2007crypticproteolyticactivity pages 1-2). DLD is ubiquitously expressed across tissues, with particularly high expression in metabolically active organs including heart, kidney, liver, and brain (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6). Although DLD is predominantly a mitochondrial matrix enzyme, a non-mitochondrial isoform of DLDH has been reported in rat serum, representing a rare extra-mitochondrial occurrence (yan2023rolesofdihydrolipoamide pages 7-8).

---

## 5. Moonlighting (Non-Canonical) Functions

DLD is recognized as a moonlighting protein, possessing several non-canonical activities that emerge particularly under pathological conditions.

### 5.1 Diaphorase Activity

DLD exhibits NADH-specific diaphorase activity, catalyzing NADH oxidation using various electron acceptors including molecular oxygen (O₂), ferric iron, nitric oxide, and ubiquinone (yan2023rolesofdihydrolipoamide pages 1-3, babady2007crypticproteolyticactivity pages 1-2). This FAD- and NADH-dependent activity is believed to have a pro-oxidant role and increases when the mitochondrial matrix is acidified, such as during ischemia-reperfusion injury (babady2007crypticproteolyticactivity pages 4-5).

### 5.2 Proteolytic Activity

When the DLD homodimer is destabilized—by mutations, altered pH, or other conditions—the protein reveals a cryptic serine protease activity utilizing a catalytic dyad (Ser456–Glu431) located at the dimer interface (babady2007crypticproteolyticactivity pages 1-2, babady2007crypticproteolyticactivity pages 4-5). This proteolytic activity can cleave mitochondrial substrates such as frataxin, a protein involved in iron metabolism and antioxidant defense (babady2007crypticproteolyticactivity pages 5-6). Disease-causing mutations in the dimer interface domain (e.g., D444V, R447G) independently enhance this proteolytic activity (vaubel2011mutationsinthe pages 10-11).

### 5.3 Reactive Oxygen Species (ROS) Generation

DLD functions as a significant source of mitochondrial ROS. Its diaphorase activity reduces O₂ to superoxide radicals and Fe³⁺ to Fe²⁺, the latter catalyzing hydroxyl radical production through Fenton chemistry (babady2007crypticproteolyticactivity pages 1-2, vaubel2011mutationsinthe pages 1-2). DLD-dependent ROS generation is enhanced when NADH/NAD⁺ ratios are elevated and is a recognized contributor to oxidative damage in neurodegenerative conditions (vaubel2011mutationsinthe pages 1-2). However, DLD's ability to scavenge nitric oxide and reduce ubiquinone to ubiquinol suggests it may also exert antioxidant effects under certain conditions (babady2007crypticproteolyticactivity pages 1-2).

---

## 6. Role in Cuproptosis

A major recent discovery (2022–present) is DLD's involvement in cuproptosis, a copper-dependent form of regulated cell death. Genome-wide CRISPR screening identified DLD as one of seven genes (along with FDX1, LIAS, LIPT1, DLAT, PDHA1, and PDHB) whose knockout significantly mitigates copper-induced cytotoxicity (qi2023oncogenicroleof pages 1-2, chen2025roleandmechanisms pages 2-4). In the cuproptosis mechanism, excess intracellular copper binds to the thiol groups on lipoylated TCA cycle proteins, causing their aberrant oligomerization and triggering proteotoxic stress (zhao2024cuproptosisthenovel pages 3-4, chen2025mechanismsofcopper pages 2-3). DLD is essential for the lipoylation pathway that enables this copper-mediated protein aggregation (zhao2024cuproptosisthenovel pages 3-4).

Recent research has elucidated a more specific mechanism: activated DLD, induced by excess copper under alkaline mitochondrial pH conditions, drives NADH accumulation. Copper-mediated opening of the mitochondrial permeability transition pore (mPTP) facilitates NADH translocation to the cytosol, triggering NADH-reductive stress, which promotes aberrant purine biosynthesis, severe ATP depletion, and energy stress leading to cell death (zhang2026nadh‐reductivestressinduced pages 3-4, zhang2026nadh‐reductivestressinduced pages 7-8). Pharmacological inhibition of DLD with CPI-613 effectively blocks copper-induced NADH elevation and attenuates cuproptosis (zhang2026nadh‐reductivestressinduced pages 3-4).

---

## 7. Disease Associations

### 7.1 DLD Deficiency (OMIM #246900)

DLD deficiency is a rare autosomal recessive disorder caused by biallelic mutations in the *DLD* gene. Because DLD is shared among multiple metabolic complexes, its deficiency simultaneously impairs pyruvate oxidation, the TCA cycle, branched-chain amino acid catabolism, and glycine degradation (szabo2019underlyingmolecularalterations pages 4-5, szabo2024mitochondrialalphaketoacid pages 36-39).

Clinical presentations include:
- **Early-onset (neonatal):** Severe metabolic decompensation with lactic acidosis, hypoglycemia, hyperammonemia, encephalopathy, Leigh syndrome, hypertrophic cardiomyopathy, and often premature death (szabo2019underlyingmolecularalterations pages 4-5, szabo2024mitochondrialalphaketoacid pages 36-39, quinonez2013leighsyndromein pages 1-3).
- **Hepatic form:** Episodic liver failure with metabolic decompensation, generally longer survival (odievre2005anovelmutation pages 5-8, szabo2024mitochondrialalphaketoacid pages 36-39).
- **Myopathic form:** Riboflavin-responsive mitochondrial myopathy, recently recognized (staretzchacham2021theeffectsof pages 9-10, szabo2023structuralandbiochemical pages 21-22).

The most prevalent disease-causing variant, G194C (c.685G>T), is the Ashkenazi Jewish founder mutation with a carrier frequency of approximately 1:94 (szabo2019underlyingmolecularalterations pages 4-5, odievre2005anovelmutation pages 5-8). At least 14 disease-causing variants have been characterized, affecting various protein domains (szabo2019underlyingmolecularalterations pages 4-5). Structural studies have revealed that mutations in the dimer interface (e.g., D444V, R447G, R460G, E340K) are particularly severe because they not only reduce catalytic activity but also enhance ROS-generating and proteolytic moonlighting activities, thereby compounding pathology through oxidative damage to neighboring mitochondrial components including the lipoic acid cofactors of partner complexes (vaubel2011mutationsinthe pages 10-11, vaubel2011mutationsinthe pages 1-2).

| DLD mutation | Nucleotide change / alias | Structural / biochemical effect | Reported clinical phenotype | Key notes / population context |
|---|---|---|---|---|
| G194C | c.685G>T; historically also reported as p.G229C in precursor numbering | Common pathogenic variant; relatively minor local structural changes near substitution site, with nearby cofactor-binding residues largely preserved compared with more disruptive variants | Often associated with comparatively milder disease and later presentation; recurrent hepatic failure/liver-predominant phenotype reported; DLD deficiency overall can include lactic acidosis and neurologic involvement | Ashkenazi Jewish founder mutation; carrier frequency reported as ~1:94 in Ashkenazi Jews; also reported in Arab Muslim patients (szabo2019underlyingmolecularalterations pages 4-5, odievre2005anovelmutation pages 5-8, staretzchacham2021theeffectsof pages 9-10, szabo2023structuralandbiochemical pages 21-22) |
| D444V | mature-protein numbering; interface-domain variant | Dimer-interface mutation; enhanced ROS-generating and proteolytic/diaphorase moonlighting activities; promotes oxidative damage to mitochondrial targets | Severe DLD deficiency presentations, including liver disease and metabolic decompensation; contributes to severe clinical course through oxidative injury mechanisms | Reported in Ashkenazi Jewish patients; widely studied as a pathogenic interface mutation (vaubel2011mutationsinthe pages 10-11, babady2007crypticproteolyticactivity pages 5-6, vaubel2011mutationsinthe pages 1-2, staretzchacham2021theeffectsof pages 9-10) |
| R460G | — | Dimer-interface mutation; enhances diaphorase activity and ROS production | Severe multisystem disorder of infancy | Included among severe interface mutations linked to oxidative damage and profound infantile disease (szabo2019underlyingmolecularalterations pages 4-5, vaubel2011mutationsinthe pages 10-11, vaubel2011mutationsinthe pages 1-2) |
| R447G | — | Dimer-interface mutation; perturbs solvent-accessible channel leading to active site; enhances ROS, and in some studies proteolytic activity | Severe multisystem disorder / severe infantile disease | Structural and functional evidence supports interface destabilization as pathogenic mechanism (szabo2019underlyingmolecularalterations pages 4-5, vaubel2011mutationsinthe pages 10-11, vaubel2011mutationsinthe pages 1-2) |
| E340K | — | Mutation associated with altered cryptic activities; enhanced diaphorase activity and ROS production | Severe multisystem disorder of infancy | Disease severity likely reflects both enzyme deficiency and oxidative-damage mechanisms (szabo2023structuralandbiochemical pages 21-22, vaubel2011mutationsinthe pages 10-11, vaubel2011mutationsinthe pages 1-2) |
| P453L | — | Most deleterious structural change among analyzed variants; active site extensively compromised | Severe phenotype expected/associated with markedly impaired enzyme function | Identified as especially disruptive in crystallographic analysis (szabo2019underlyingmolecularalterations pages 3-4, szabo2019underlyingmolecularalterations pages 4-5) |
| G426E | — | Dimer-interface variant; alters local charge distribution and introduces dynamics at substitution site; minor structural changes but functionally important | Pathogenic DLD deficiency; severity variable | Illustrates that even subtle structural changes at interface can impair multienzyme-complex function (szabo2019underlyingmolecularalterations pages 3-4, szabo2019underlyingmolecularalterations pages 4-5) |
| I445M | — | Dimer-interface variant; perturbs H+/H2O channel to active site | Pathogenic DLD deficiency; associated with impaired catalysis | Channel perturbation provides a structural explanation for dysfunction (szabo2019underlyingmolecularalterations pages 3-4, szabo2023structuralandbiochemical pages 1-3) |
| I12T | — | Unstable protein retaining dimeric form but with markedly compromised forward/reverse LADH activity and reduced FAD affinity | Pathogenic DLD deficiency | N-terminal variant showing severe biochemical impairment without the same structural class as interface mutants (szabo2023structuralandbiochemical pages 1-3, szabo2019underlyingmolecularalterations pages 4-5) |
| M326V | — | Protein instability, functional dimer disassembly, significant FAD loss, virtually undetectable catalytic activity | Pathogenic DLD deficiency | Demonstrates loss-of-stability mechanism (szabo2023structuralandbiochemical pages 1-3, szabo2019underlyingmolecularalterations pages 4-5) |
| G101del | — | Protein instability, dimer disassembly, significant FAD loss, virtually undetectable catalytic activity | Pathogenic DLD deficiency; reported in myopathic / Leigh-related clinical literature | Strong example of instability-driven deficiency (szabo2023structuralandbiochemical pages 1-3, staretzchacham2021theeffectsof pages 9-10, szabo2023structuralandbiochemical pages 21-22) |
| I318T | — | Minor conformational perturbations with residual enzymatic activity retained | Pathogenic DLD deficiency with residual function | Supports genotype–biochemistry gradient rather than uniform complete loss of function (szabo2023structuralandbiochemical pages 1-3, szabo2019underlyingmolecularalterations pages 4-5) |
| I358T / I353T | I358T in structural literature; I353T reported clinically in one case | Minor conformational perturbations / residual activity for I358T; I353T reported as disease-causing in Leigh syndrome case report | I353T associated with episodic encephalopathy, lactic acidosis, hypoglycemia, learning disability, and Leigh syndrome; I358T supports a residual-activity model | Numbering may differ between reports due to precursor vs mature protein conventions (szabo2023structuralandbiochemical pages 1-3, quinonez2013leighsyndromein pages 4-6, quinonez2013leighsyndromein pages 1-3) |
| R482G | c.1444A>G | Novel pathogenic variant in highly conserved region | Neurological deterioration beginning at birth/early infancy, hyperlactatemia, hypotonia/rigidity/choreoathetoid movements, early death | Reported in siblings with atypical α-ketoglutarate dehydrogenase deficiency / DLD deficiency phenotype (odievre2005anovelmutation pages 5-8, odievre2005anovelmutation pages 1-3) |
| G136del | — | Previously reported pathogenic deletion | Reported with DLD deficiency; in compound heterozygosity with I353T in a patient with episodic encephalopathy, lactic acidosis, hypoglycemia, and Leigh syndrome | Established disease-causing mutation in prior literature (quinonez2013leighsyndromein pages 4-6, quinonez2013leighsyndromein pages 1-3) |


*Table: This table summarizes disease-causing human DLD variants, linking structural/biochemical effects to reported clinical phenotypes. It is useful for functional annotation because it connects specific residues and mechanistic defects to recognizable metabolic and neurologic presentations.*

### 7.2 Neurodegenerative Disease

DLD is implicated in neurodegeneration, particularly through the KGDHc axis. Reduced KGDHc activity is a consistent finding in Alzheimer's disease, and DLD heterozygous knockout animals show decreased ROS production from both forward and reverse electron flow (hansen2022theαketoglutaratedehydrogenase pages 2-4, OpenTargets Search: -DLD). Recent work has linked dysregulation of mitochondrial KGDHc, including DLD, to elevated lipid peroxidation in CHCHD2-linked Parkinson's disease models (OpenTargets Search: -DLD).

### 7.3 Cancer

Pan-cancer analysis has demonstrated that DLD is differentially expressed across multiple tumor types, with high expression in colon, liver, lung, stomach, renal, and ovarian cancers. In ovarian cancer, high DLD expression correlates with poorer prognosis. DLD regulates metabolic pathways by modulating the intracellular NAD⁺/NADH ratio, thereby influencing tumor cell proliferation (qi2023oncogenicroleof pages 1-2).

### 7.4 OpenTargets Disease Associations

Database analysis reveals strong DLD–disease associations for pyruvate dehydrogenase deficiency (association score 0.85), pyruvate dehydrogenase E3 deficiency (0.84), Leigh syndrome (0.64), neurodegenerative disease (0.53), and inflammatory bowel disease (0.52) (OpenTargets Search: -DLD).

---

## 8. Recent Developments (2023–2025)

Several recent advances have expanded our understanding of DLD:

1. **Structural pathomechanisms (2023):** Szabo et al. reported crystal structures of additional pathogenic hE3 variants (I318T at 2.89 Å, I358T at 2.44 Å), demonstrating a genotype-to-structure-to-phenotype continuum. Variants G101del and M326V cause dimer disassembly and FAD loss, while I318T and I358T show minor perturbations correlating with retained residual activity (szabo2023structuralandbiochemical pages 1-3).

2. **Comprehensive LADH deficiency review (2023):** Szabó and Ambrus provided an updated overview emphasizing that clinical severity often does not parallel enzymatic activity loss, implicating auxiliary pathomechanisms including stimulated ROS production and dissociation from multienzyme complexes (szabo2023structuralandbiochemical pages 1-3).

3. **α-Keto acid dehydrogenase complex review (2024):** A comprehensive review by Szabó et al. covered metabolic significance, enzymatic operation, moonlighting activities, and pathological relevance of all mitochondrial α-keto acid dehydrogenase complexes, consolidating current understanding of DLD's role across these systems (szabo2024mitochondrialalphaketoacid pages 1-6, szabo2024mitochondrialalphaketoacid pages 51-53, szabo2024mitochondrialalphaketoacid pages 16-19, szabo2024mitochondrialalphaketoacid pages 9-13).

4. **In-situ PDHc architecture (2025):** Wang et al. reported the first in-situ cryo-electron tomography structure of intact mammalian PDHc, revealing dynamic peripheral organization with an average of 21 E1 and up to 12 E3 components per complex, suggesting a novel activity-regulation mechanism through coordinated peripheral subunit numbers (wang2025dynamicsofthe pages 1-3).

5. **DLD in cuproptosis mechanism (2022–present):** The discovery that DLD is a key mediator of copper-dependent cell death has opened new research avenues, with recent work establishing that DLD activation drives NADH-reductive stress as a central mechanism of cuproptosis (zhang2026nadh‐reductivestressinduced pages 3-4).

---

## 9. Summary

Human DLD encodes a mitochondrial matrix-localized FAD-dependent disulfide oxidoreductase that serves as the shared E3 component of five major mitochondrial multienzyme complexes: PDHc, KGDHc, BCKDHc, KADHc, and the glycine cleavage system. Its primary enzymatic function is the NAD⁺-dependent oxidation of dihydrolipoamide to lipoamide via a ping-pong mechanism involving a redox-active Cys45-Cys50 disulfide and FAD cofactor. This reaction is essential for regenerating the lipoyl cofactor in each partner complex and for producing NADH for oxidative phosphorylation. DLD additionally possesses moonlighting activities including diaphorase, protease, and ROS-generating functions that become pathologically significant when the enzyme's homodimeric structure is destabilized. Mutations in *DLD* cause a rare but severe metabolic disorder affecting multiple central metabolic pathways, and DLD has recently emerged as a critical mediator of cuproptosis—a copper-dependent form of cell death with implications for neurodegeneration and cancer therapeutics.

References

1. (yan2023rolesofdihydrolipoamide pages 1-3): Liang-Jun Yan and Yucheng Wang. Roles of dihydrolipoamide dehydrogenase in health and disease. Antioxidants &amp; Redox Signaling, 39:794-806, Oct 2023. URL: https://doi.org/10.1089/ars.2022.0181, doi:10.1089/ars.2022.0181. This article has 29 citations and is from a domain leading peer-reviewed journal.

2. (szabo2019underlyingmolecularalterations pages 3-4): Eszter Szabo, Piotr Wilk, Balint Nagy, Zsofia Zambo, David Bui, Andrzej Weichsel, Palaniappa Arjunan, Beata Torocsik, Agnes Hubert, William Furey, William R Montfort, Frank Jordan, Manfred S Weiss, Vera Adam-Vizi, and Attila Ambrus. Underlying molecular alterations in human dihydrolipoamide dehydrogenase deficiency revealed by structural analyses of disease-causing enzyme variants. Human molecular genetics, 28:3339-3354, Jul 2019. URL: https://doi.org/10.1093/hmg/ddz177, doi:10.1093/hmg/ddz177. This article has 27 citations and is from a domain leading peer-reviewed journal.

3. (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6): I. F. Duarte, J. Caio, M. F. Moedas, L. A. Rodrigues, A. P. Leandro, I. A. Rivera, and M. F. B. Silva. Dihydrolipoamide dehydrogenase, pyruvate oxidation, and acetylation-dependent mechanisms intersecting drug iatrogenesis. Cellular and Molecular Life Sciences, 78:7451-7468, Oct 2021. URL: https://doi.org/10.1007/s00018-021-03996-3, doi:10.1007/s00018-021-03996-3. This article has 46 citations and is from a domain leading peer-reviewed journal.

4. (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-4): I. F. Duarte, J. Caio, M. F. Moedas, L. A. Rodrigues, A. P. Leandro, I. A. Rivera, and M. F. B. Silva. Dihydrolipoamide dehydrogenase, pyruvate oxidation, and acetylation-dependent mechanisms intersecting drug iatrogenesis. Cellular and Molecular Life Sciences, 78:7451-7468, Oct 2021. URL: https://doi.org/10.1007/s00018-021-03996-3, doi:10.1007/s00018-021-03996-3. This article has 46 citations and is from a domain leading peer-reviewed journal.

5. (szabo2023structuralandbiochemical pages 1-3): Eszter Szabo, Eva Nemes-Nikodem, Krisztina Rubina Vass, Zsofia Zambo, Eszter Zrupko, Beata Torocsik, Oliver Ozohanics, Balint Nagy, and Attila Ambrus. Structural and biochemical investigation of selected pathogenic mutants of the human dihydrolipoamide dehydrogenase. International Journal of Molecular Sciences, 24:10826, Jun 2023. URL: https://doi.org/10.3390/ijms241310826, doi:10.3390/ijms241310826. This article has 2 citations.

6. (yan2023rolesofdihydrolipoamide pages 5-7): Liang-Jun Yan and Yucheng Wang. Roles of dihydrolipoamide dehydrogenase in health and disease. Antioxidants &amp; Redox Signaling, 39:794-806, Oct 2023. URL: https://doi.org/10.1089/ars.2022.0181, doi:10.1089/ars.2022.0181. This article has 29 citations and is from a domain leading peer-reviewed journal.

7. (szabo2024mitochondrialalphaketoacid pages 1-6): Eszter Szabó, Bálint Nagy, András Czajlik, T. Komlódi, Olivér Ozohanics, László Tretter, and A. Ambrus. Mitochondrial alpha-keto acid dehydrogenase complexes: recent developments on structure and function in health and disease. Sub-cellular biochemistry, 104:295-381, 2024. URL: https://doi.org/10.1007/978-3-031-58843-3\_13, doi:10.1007/978-3-031-58843-3\_13. This article has 16 citations.

8. (duarte2021dihydrolipoamidedehydrogenasepyruvate pages 2-4): I. F. Duarte, J. Caio, M. F. Moedas, L. A. Rodrigues, A. P. Leandro, I. A. Rivera, and M. F. B. Silva. Dihydrolipoamide dehydrogenase, pyruvate oxidation, and acetylation-dependent mechanisms intersecting drug iatrogenesis. Cellular and Molecular Life Sciences, 78:7451-7468, Oct 2021. URL: https://doi.org/10.1007/s00018-021-03996-3, doi:10.1007/s00018-021-03996-3. This article has 46 citations and is from a domain leading peer-reviewed journal.

9. (brautigam2006structuralinsightinto pages 1-2): Chad A. Brautigam, R. Max Wynn, Jacinta L. Chuang, Mischa Machius, Diana R. Tomchick, and David T. Chuang. Structural insight into interactions between dihydrolipoamide dehydrogenase (e3) and e3 binding protein of human pyruvate dehydrogenase complex. Structure, 14 3:611-21, Mar 2006. URL: https://doi.org/10.1016/j.str.2006.01.001, doi:10.1016/j.str.2006.01.001. This article has 128 citations and is from a domain leading peer-reviewed journal.

10. (szabo2024mitochondrialalphaketoacid pages 16-19): Eszter Szabó, Bálint Nagy, András Czajlik, T. Komlódi, Olivér Ozohanics, László Tretter, and A. Ambrus. Mitochondrial alpha-keto acid dehydrogenase complexes: recent developments on structure and function in health and disease. Sub-cellular biochemistry, 104:295-381, 2024. URL: https://doi.org/10.1007/978-3-031-58843-3\_13, doi:10.1007/978-3-031-58843-3\_13. This article has 16 citations.

11. (hansen2022theαketoglutaratedehydrogenase pages 2-4): Grace E. Hansen and Gary E. Gibson. The α-ketoglutarate dehydrogenase complex as a hub of plasticity in neurodegeneration and regeneration. International Journal of Molecular Sciences, 23:12403, Oct 2022. URL: https://doi.org/10.3390/ijms232012403, doi:10.3390/ijms232012403. This article has 85 citations.

12. (kikuchi2008glycinecleavagesystem pages 2-5): Goro KIKUCHI, Yutaro MOTOKAWA, Tadashi YOSHIDA, and Koichi HIRAGA. Glycine cleavage system: reaction mechanism, physiological significance, and hyperglycinemia. Proceedings of the Japan Academy. Series B, Physical and biological sciences, 84 7:246-63, Jul 2008. URL: https://doi.org/10.2183/pjab.84.246, doi:10.2183/pjab.84.246. This article has 491 citations.

13. (leung2021glycinecleavagesystem pages 1-2): Kit-Yi Leung, Sandra C. P. De Castro, Gabriel L. Galea, Andrew J. Copp, and Nicholas D. E. Greene. Glycine cleavage system h protein is essential for embryonic viability, implying additional function beyond the glycine cleavage system. Frontiers in Genetics, Jan 2021. URL: https://doi.org/10.3389/fgene.2021.625120, doi:10.3389/fgene.2021.625120. This article has 32 citations and is from a peer-reviewed journal.

14. (brautigam2006structuralinsightinto pages 2-3): Chad A. Brautigam, R. Max Wynn, Jacinta L. Chuang, Mischa Machius, Diana R. Tomchick, and David T. Chuang. Structural insight into interactions between dihydrolipoamide dehydrogenase (e3) and e3 binding protein of human pyruvate dehydrogenase complex. Structure, 14 3:611-21, Mar 2006. URL: https://doi.org/10.1016/j.str.2006.01.001, doi:10.1016/j.str.2006.01.001. This article has 128 citations and is from a domain leading peer-reviewed journal.

15. (wang2025dynamicsofthe pages 1-3): Chen Wang, Cheng Ma, Yuanyou Xu, Shenghai Chang, Hangjun Wu, Chunlan Yan, Jinghua Chen, Yongping Wu, Shaoya An, Jiaqi Xu, Qin Han, Yujie Jiang, Zhinong Jiang, Xiakun Chu, Haichun Gao, Xing Zhang, and Yunjie Chang. Dynamics of the mammalian pyruvate dehydrogenase complex revealed by in-situ structural analysis. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56171-8, doi:10.1038/s41467-025-56171-8. This article has 17 citations and is from a highest quality peer-reviewed journal.

16. (babady2007crypticproteolyticactivity pages 1-2): Ngolela Esther Babady, Yuan-Ping Pang, Orly Elpeleg, and Grazia Isaya. Cryptic proteolytic activity of dihydrolipoamide dehydrogenase. Proceedings of the National Academy of Sciences, 104:6158-6163, Apr 2007. URL: https://doi.org/10.1073/pnas.0610618104, doi:10.1073/pnas.0610618104. This article has 164 citations and is from a highest quality peer-reviewed journal.

17. (yan2023rolesofdihydrolipoamide pages 7-8): Liang-Jun Yan and Yucheng Wang. Roles of dihydrolipoamide dehydrogenase in health and disease. Antioxidants &amp; Redox Signaling, 39:794-806, Oct 2023. URL: https://doi.org/10.1089/ars.2022.0181, doi:10.1089/ars.2022.0181. This article has 29 citations and is from a domain leading peer-reviewed journal.

18. (babady2007crypticproteolyticactivity pages 4-5): Ngolela Esther Babady, Yuan-Ping Pang, Orly Elpeleg, and Grazia Isaya. Cryptic proteolytic activity of dihydrolipoamide dehydrogenase. Proceedings of the National Academy of Sciences, 104:6158-6163, Apr 2007. URL: https://doi.org/10.1073/pnas.0610618104, doi:10.1073/pnas.0610618104. This article has 164 citations and is from a highest quality peer-reviewed journal.

19. (babady2007crypticproteolyticactivity pages 5-6): Ngolela Esther Babady, Yuan-Ping Pang, Orly Elpeleg, and Grazia Isaya. Cryptic proteolytic activity of dihydrolipoamide dehydrogenase. Proceedings of the National Academy of Sciences, 104:6158-6163, Apr 2007. URL: https://doi.org/10.1073/pnas.0610618104, doi:10.1073/pnas.0610618104. This article has 164 citations and is from a highest quality peer-reviewed journal.

20. (vaubel2011mutationsinthe pages 10-11): Rachael A. Vaubel, Pierre Rustin, and Grazia Isaya. Mutations in the dimer interface of dihydrolipoamide dehydrogenase promote site-specific oxidative damages in yeast and human cells. Journal of Biological Chemistry, 286:40232-40245, Nov 2011. URL: https://doi.org/10.1074/jbc.m111.274415, doi:10.1074/jbc.m111.274415. This article has 69 citations and is from a domain leading peer-reviewed journal.

21. (vaubel2011mutationsinthe pages 1-2): Rachael A. Vaubel, Pierre Rustin, and Grazia Isaya. Mutations in the dimer interface of dihydrolipoamide dehydrogenase promote site-specific oxidative damages in yeast and human cells. Journal of Biological Chemistry, 286:40232-40245, Nov 2011. URL: https://doi.org/10.1074/jbc.m111.274415, doi:10.1074/jbc.m111.274415. This article has 69 citations and is from a domain leading peer-reviewed journal.

22. (qi2023oncogenicroleof pages 1-2): Han Qi and Dongsheng Zhu. Oncogenic role of copper‑induced cell death‑associated protein dld in human cancer: a pan‑cancer analysis and experimental verification. Oncology Letters, Apr 2023. URL: https://doi.org/10.3892/ol.2023.13800, doi:10.3892/ol.2023.13800. This article has 26 citations and is from a peer-reviewed journal.

23. (chen2025roleandmechanisms pages 2-4): Hong Chen, Xie Wang, Jin Xing, Yue Pu, Hao Ye, Ying Ma, and Juan Zhang. Role and mechanisms of cuproptosis in the pathogenesis of wilson's disease (review). International Journal of Molecular Medicine, 56:1-13, May 2025. URL: https://doi.org/10.3892/ijmm.2025.5558, doi:10.3892/ijmm.2025.5558. This article has 13 citations and is from a peer-reviewed journal.

24. (zhao2024cuproptosisthenovel pages 3-4): Ruiwen Zhao, Olga Sukocheva, Edmund Tse, Margarita Neganova, Yulia Aleksandrova, Yufei Zheng, Hao Gu, Deyao Zhao, SabbaRao V. Madhunapantula, Xiaorong Zhu, Junqi Liu, and Ruitai Fan. Cuproptosis, the novel type of oxidation-induced cell death in thoracic cancers: can it enhance the success of immunotherapy? Cell Communication and Signaling : CCS, Jul 2024. URL: https://doi.org/10.1186/s12964-024-01743-2, doi:10.1186/s12964-024-01743-2. This article has 52 citations.

25. (chen2025mechanismsofcopper pages 2-3): Haoran Chen, Dongxuan Li, Huimin Zhang, Meiqi Zhang, Yumeng Lin, Haibei He, Aijun Liu, Shiming Shen, Yi Wang, and Zhongyu Han. Mechanisms of copper metabolism and cuproptosis: implications for liver diseases. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1633711, doi:10.3389/fimmu.2025.1633711. This article has 24 citations and is from a peer-reviewed journal.

26. (zhang2026nadh‐reductivestressinduced pages 3-4): Si‐Yi Zhang, Xing‐Hua Ren, Cheng‐Hong Zhang, and Zhan‐You Wang. Nadh‐reductive stress induced by dihydrolipoamide dehydrogenase activation contributes to cuproptosis. Advanced Science, Dec 2026. URL: https://doi.org/10.1002/advs.202520444, doi:10.1002/advs.202520444. This article has 1 citations and is from a peer-reviewed journal.

27. (zhang2026nadh‐reductivestressinduced pages 7-8): Si‐Yi Zhang, Xing‐Hua Ren, Cheng‐Hong Zhang, and Zhan‐You Wang. Nadh‐reductive stress induced by dihydrolipoamide dehydrogenase activation contributes to cuproptosis. Advanced Science, Dec 2026. URL: https://doi.org/10.1002/advs.202520444, doi:10.1002/advs.202520444. This article has 1 citations and is from a peer-reviewed journal.

28. (szabo2019underlyingmolecularalterations pages 4-5): Eszter Szabo, Piotr Wilk, Balint Nagy, Zsofia Zambo, David Bui, Andrzej Weichsel, Palaniappa Arjunan, Beata Torocsik, Agnes Hubert, William Furey, William R Montfort, Frank Jordan, Manfred S Weiss, Vera Adam-Vizi, and Attila Ambrus. Underlying molecular alterations in human dihydrolipoamide dehydrogenase deficiency revealed by structural analyses of disease-causing enzyme variants. Human molecular genetics, 28:3339-3354, Jul 2019. URL: https://doi.org/10.1093/hmg/ddz177, doi:10.1093/hmg/ddz177. This article has 27 citations and is from a domain leading peer-reviewed journal.

29. (szabo2024mitochondrialalphaketoacid pages 36-39): Eszter Szabó, Bálint Nagy, András Czajlik, T. Komlódi, Olivér Ozohanics, László Tretter, and A. Ambrus. Mitochondrial alpha-keto acid dehydrogenase complexes: recent developments on structure and function in health and disease. Sub-cellular biochemistry, 104:295-381, 2024. URL: https://doi.org/10.1007/978-3-031-58843-3\_13, doi:10.1007/978-3-031-58843-3\_13. This article has 16 citations.

30. (quinonez2013leighsyndromein pages 1-3): Shane C. Quinonez, Steven M. Leber, Donna M. Martin, Jess G. Thoene, and Jirair K. Bedoyan. Leigh syndrome in a girl with a novel dld mutation causing e3 deficiency. Pediatric neurology, 48 1:67-72, Jan 2013. URL: https://doi.org/10.1016/j.pediatrneurol.2012.09.013, doi:10.1016/j.pediatrneurol.2012.09.013. This article has 67 citations and is from a peer-reviewed journal.

31. (odievre2005anovelmutation pages 5-8): Marie-Hélène Odièvre, Dominique Chretien, Arnold Munnich, Brian H. Robinson, Renée Dumoulin, Sahben Masmoudi, Noman Kadhom, Agnès Rötig, Pierre Rustin, and Jean-Paul Bonnefont. A novel mutation in the dihydrolipoamide dehydrogenase e3 subunit gene (dld) resulting in an atypical form of α‐ketoglutarate dehydrogenase deficiency. Human Mutation, 25:323-324, Mar 2005. URL: https://doi.org/10.1002/humu.9319, doi:10.1002/humu.9319. This article has 112 citations and is from a domain leading peer-reviewed journal.

32. (staretzchacham2021theeffectsof pages 9-10): Orna Staretz-Chacham, Ben Pode-Shakked, Eyal Kristal, Smadar Yaala Abraham, Keren Porper, Ohad Wormser, Ilan Shelef, and Yair Anikster. The effects of a ketogenic diet on patients with dihydrolipoamide dehydrogenase deficiency. Nutrients, 13:3523, Oct 2021. URL: https://doi.org/10.3390/nu13103523, doi:10.3390/nu13103523. This article has 26 citations.

33. (szabo2023structuralandbiochemical pages 21-22): Eszter Szabo, Eva Nemes-Nikodem, Krisztina Rubina Vass, Zsofia Zambo, Eszter Zrupko, Beata Torocsik, Oliver Ozohanics, Balint Nagy, and Attila Ambrus. Structural and biochemical investigation of selected pathogenic mutants of the human dihydrolipoamide dehydrogenase. International Journal of Molecular Sciences, 24:10826, Jun 2023. URL: https://doi.org/10.3390/ijms241310826, doi:10.3390/ijms241310826. This article has 2 citations.

34. (quinonez2013leighsyndromein pages 4-6): Shane C. Quinonez, Steven M. Leber, Donna M. Martin, Jess G. Thoene, and Jirair K. Bedoyan. Leigh syndrome in a girl with a novel dld mutation causing e3 deficiency. Pediatric neurology, 48 1:67-72, Jan 2013. URL: https://doi.org/10.1016/j.pediatrneurol.2012.09.013, doi:10.1016/j.pediatrneurol.2012.09.013. This article has 67 citations and is from a peer-reviewed journal.

35. (odievre2005anovelmutation pages 1-3): Marie-Hélène Odièvre, Dominique Chretien, Arnold Munnich, Brian H. Robinson, Renée Dumoulin, Sahben Masmoudi, Noman Kadhom, Agnès Rötig, Pierre Rustin, and Jean-Paul Bonnefont. A novel mutation in the dihydrolipoamide dehydrogenase e3 subunit gene (dld) resulting in an atypical form of α‐ketoglutarate dehydrogenase deficiency. Human Mutation, 25:323-324, Mar 2005. URL: https://doi.org/10.1002/humu.9319, doi:10.1002/humu.9319. This article has 112 citations and is from a domain leading peer-reviewed journal.

36. (OpenTargets Search: -DLD): Open Targets Query (-DLD, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

37. (szabo2024mitochondrialalphaketoacid pages 51-53): Eszter Szabó, Bálint Nagy, András Czajlik, T. Komlódi, Olivér Ozohanics, László Tretter, and A. Ambrus. Mitochondrial alpha-keto acid dehydrogenase complexes: recent developments on structure and function in health and disease. Sub-cellular biochemistry, 104:295-381, 2024. URL: https://doi.org/10.1007/978-3-031-58843-3\_13, doi:10.1007/978-3-031-58843-3\_13. This article has 16 citations.

38. (szabo2024mitochondrialalphaketoacid pages 9-13): Eszter Szabó, Bálint Nagy, András Czajlik, T. Komlódi, Olivér Ozohanics, László Tretter, and A. Ambrus. Mitochondrial alpha-keto acid dehydrogenase complexes: recent developments on structure and function in health and disease. Sub-cellular biochemistry, 104:295-381, 2024. URL: https://doi.org/10.1007/978-3-031-58843-3\_13, doi:10.1007/978-3-031-58843-3\_13. This article has 16 citations.

## Artifacts

- [Edison artifact artifact-00](DLD-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](DLD-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. yan2023rolesofdihydrolipoamide pages 1-3
2. szabo2023structuralandbiochemical pages 1-3
3. szabo2019underlyingmolecularalterations pages 3-4
4. duarte2021dihydrolipoamidedehydrogenasepyruvate pages 2-4
5. wang2025dynamicsofthe pages 1-3
6. leung2021glycinecleavagesystem pages 1-2
7. duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-6
8. yan2023rolesofdihydrolipoamide pages 7-8
9. babady2007crypticproteolyticactivity pages 4-5
10. babady2007crypticproteolyticactivity pages 5-6
11. vaubel2011mutationsinthe pages 10-11
12. vaubel2011mutationsinthe pages 1-2
13. babady2007crypticproteolyticactivity pages 1-2
14. zhao2024cuproptosisthenovel pages 3-4
15. szabo2019underlyingmolecularalterations pages 4-5
16. qi2023oncogenicroleof pages 1-2
17. duarte2021dihydrolipoamidedehydrogenasepyruvate pages 4-4
18. yan2023rolesofdihydrolipoamide pages 5-7
19. szabo2024mitochondrialalphaketoacid pages 1-6
20. brautigam2006structuralinsightinto pages 1-2
21. szabo2024mitochondrialalphaketoacid pages 16-19
22. kikuchi2008glycinecleavagesystem pages 2-5
23. brautigam2006structuralinsightinto pages 2-3
24. chen2025roleandmechanisms pages 2-4
25. chen2025mechanismsofcopper pages 2-3
26. szabo2024mitochondrialalphaketoacid pages 36-39
27. quinonez2013leighsyndromein pages 1-3
28. odievre2005anovelmutation pages 5-8
29. staretzchacham2021theeffectsof pages 9-10
30. szabo2023structuralandbiochemical pages 21-22
31. quinonez2013leighsyndromein pages 4-6
32. odievre2005anovelmutation pages 1-3
33. szabo2024mitochondrialalphaketoacid pages 51-53
34. szabo2024mitochondrialalphaketoacid pages 9-13
35. LADH
36. https://doi.org/10.1089/ars.2022.0181,
37. https://doi.org/10.1093/hmg/ddz177,
38. https://doi.org/10.1007/s00018-021-03996-3,
39. https://doi.org/10.3390/ijms241310826,
40. https://doi.org/10.1007/978-3-031-58843-3\_13,
41. https://doi.org/10.1016/j.str.2006.01.001,
42. https://doi.org/10.3390/ijms232012403,
43. https://doi.org/10.2183/pjab.84.246,
44. https://doi.org/10.3389/fgene.2021.625120,
45. https://doi.org/10.1038/s41467-025-56171-8,
46. https://doi.org/10.1073/pnas.0610618104,
47. https://doi.org/10.1074/jbc.m111.274415,
48. https://doi.org/10.3892/ol.2023.13800,
49. https://doi.org/10.3892/ijmm.2025.5558,
50. https://doi.org/10.1186/s12964-024-01743-2,
51. https://doi.org/10.3389/fimmu.2025.1633711,
52. https://doi.org/10.1002/advs.202520444,
53. https://doi.org/10.1016/j.pediatrneurol.2012.09.013,
54. https://doi.org/10.1002/humu.9319,
55. https://doi.org/10.3390/nu13103523,