---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T02:56:17.832877'
end_time: '2026-07-07T03:26:53.643067'
duration_seconds: 1835.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CPT2
  gene_symbol: CPT2
  uniprot_accession: P23786
  protein_description: 'RecName: Full=Carnitine O-palmitoyltransferase 2, mitochondrial
    {ECO:0000305}; EC=2.3.1.21 {ECO:0000269|PubMed:20538056}; AltName: Full=Carnitine
    palmitoyltransferase II; Short=CPT II; Flags: Precursor;'
  gene_info: Name=CPT2 {ECO:0000312|HGNC:HGNC:2330}; Synonyms=CPT1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the carnitine/choline acetyltransferase family.
  protein_domains: Carn_acyl_trans. (IPR000542); Carn_acyl_trans_N. (IPR042572); CAT-like_dom_sf.
    (IPR023213); Cho/carn_acyl_trans. (IPR039551); Cho/carn_acyl_trans_2. (IPR042231)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 45
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CPT2-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P23786
- **Protein Description:** RecName: Full=Carnitine O-palmitoyltransferase 2, mitochondrial {ECO:0000305}; EC=2.3.1.21 {ECO:0000269|PubMed:20538056}; AltName: Full=Carnitine palmitoyltransferase II; Short=CPT II; Flags: Precursor;
- **Gene Information:** Name=CPT2 {ECO:0000312|HGNC:HGNC:2330}; Synonyms=CPT1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the carnitine/choline acetyltransferase family.
- **Key Domains:** Carn_acyl_trans. (IPR000542); Carn_acyl_trans_N. (IPR042572); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans. (IPR039551); Cho/carn_acyl_trans_2. (IPR042231)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CPT2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CPT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CPT2** (gene ID: CPT2, UniProt: P23786) in human.

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
- **UniProt Accession:** P23786
- **Protein Description:** RecName: Full=Carnitine O-palmitoyltransferase 2, mitochondrial {ECO:0000305}; EC=2.3.1.21 {ECO:0000269|PubMed:20538056}; AltName: Full=Carnitine palmitoyltransferase II; Short=CPT II; Flags: Precursor;
- **Gene Information:** Name=CPT2 {ECO:0000312|HGNC:HGNC:2330}; Synonyms=CPT1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the carnitine/choline acetyltransferase family.
- **Key Domains:** Carn_acyl_trans. (IPR000542); Carn_acyl_trans_N. (IPR042572); CAT-like_dom_sf. (IPR023213); Cho/carn_acyl_trans. (IPR039551); Cho/carn_acyl_trans_2. (IPR042231)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CPT2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CPT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CPT2** (gene ID: CPT2, UniProt: P23786) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: CPT2 (Carnitine O-Palmitoyltransferase 2, Mitochondrial)

**Gene:** CPT2 | **UniProt:** P23786 | **EC:** 2.3.1.21 | **Organism:** Homo sapiens

## 1. Gene and Protein Identity

CPT2 (Carnitine O-palmitoyltransferase 2, mitochondrial; also known as CPT II) is encoded by the *CPT2* gene (HGNC:2330) in humans. The protein belongs to the carnitine/choline acetyltransferase family and is synthesized as a 658-amino acid precursor containing an N-terminal mitochondrial targeting sequence that is cleaved during import into the mitochondrion (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 2-4, virmani2015thecarnitinepalmitoyl pages 4-5). Unlike the CPT1 family, which comprises three tissue-specific isoforms (CPT1A, CPT1B, CPT1C), CPT2 exists as a single, ubiquitously expressed isoform, with particularly high expression in energy-demanding tissues such as heart, liver, and skeletal muscle (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 1-3, duan2024theroleof pages 4-5, ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4). The mature protein has a molecular weight of approximately 71 kDa (schreurs2010regulatoryenzymesof pages 2-3).

## 2. Enzymatic Function and Reaction

### 2.1 Catalyzed Reaction

CPT2 catalyzes the final step of the mitochondrial carnitine shuttle system. The enzyme performs a transesterification reaction, converting acylcarnitines back into their corresponding acyl-CoA thioesters while releasing free L-carnitine (violante2010carnitinepalmitoyltransferase2 pages 1-2, duan2024theroleof pages 2-4):

**Acylcarnitine + CoA ⇌ Acyl-CoA + L-Carnitine**

This reaction is reversible and energy-neutral (virmani2015thecarnitinepalmitoyl pages 3-4). In the physiological forward direction, CPT2 regenerates acyl-CoA within the mitochondrial matrix, enabling the acyl chain to enter the β-oxidation spiral for energy production (knottnerus2018disordersofmitochondrial pages 2-3, schlaepfer2020cpt1amediatedfatoxidation pages 32-32). Under certain conditions, such as accumulation of intramitochondrial acyl-CoA species in fatty acid oxidation disorders, CPT2 can operate in the reverse direction, converting acyl-CoAs to acylcarnitines for export from the mitochondria (violante2010carnitinepalmitoyltransferase2 pages 1-2, violante2010carnitinepalmitoyltransferase2 pages 4-4).

### 2.2 Substrate Specificity

Detailed substrate specificity studies using recombinant human CPT2 expressed in yeast have revealed important insights into the enzyme's preferences (violante2010carnitinepalmitoyltransferase2 pages 4-4, violante2010carnitinepalmitoyltransferase2 pages 3-4):

- **Preferred substrates:** CPT2 is active with medium-chain (C8–C12) and long-chain (C14–C18) acyl-CoA esters, with C10–C14 chains representing the most efficiently processed substrates (violante2010carnitinepalmitoyltransferase2 pages 4-4, violante2010carnitinepalmitoyltransferase2 pages 1-2).
- **Long-chain substrates:** The enzyme also efficiently handles common long-chain species such as C12-CoA and C16-CoA (palmitoyl-CoA) and shows activity toward certain unsaturated acyl-CoAs (cis-5 and cis-9 species) and mitochondrial β-oxidation intermediates including 3-hydroxy and 3-keto-palmitoyl-CoA (violante2010carnitinepalmitoyltransferase2 pages 3-4).
- **Poor substrates:** CPT2 shows virtually no activity with short-chain or very-long-chain acyl-CoAs. Notably, trans-2-enoyl-CoA intermediates are very poor substrates, demonstrating only 1–1.5% of the activity observed with corresponding straight-chain acyl-CoAs, and these intermediates act as competitive inhibitors (violante2010carnitinepalmitoyltransferase2 pages 4-4, violante2010carnitinepalmitoyltransferase2 pages 3-4).
- **Non-substrates:** Branched-chain amino acid oxidation intermediates are not processed by CPT2. Among peroxisomal substrates, only 4,8-dimethylnonanoyl-CoA shows reactivity, while pristanoyl-CoA is not accepted (violante2010carnitinepalmitoyltransferase2 pages 3-4, violante2010carnitinepalmitoyltransferase2 pages 4-4).

These specificity characteristics have important implications for acylcarnitine profiling in the diagnosis of metabolic disorders (violante2010carnitinepalmitoyltransferase2 pages 4-4).

## 3. Subcellular Localization and Membrane Topology

CPT2 is localized to the **inner mitochondrial membrane (IMM)** with its catalytic domain oriented toward the **mitochondrial matrix** (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 1-3, duan2024theroleof pages 2-4, rufer2009structuralinsightinto pages 2-4). Crystal structures of rat CPT2, solved at 1.6–2.6 Å resolution by two independent groups, have confirmed that the protein is monomeric and peripherally associated with the inner membrane rather than being a transmembrane protein like CPT1 (rufer2009structuralinsightinto pages 5-7, rufer2009structuralinsightinto pages 4-5).

A distinctive structural feature unique to CPT2 among carnitine acyltransferases is a **membrane-anchoring insertion** comprising residues Asn179–Asn208, which forms a pair of anti-parallel helices that insert into the inner leaflet of the inner mitochondrial membrane (rufer2009structuralinsightinto pages 5-7). This insertion mediates membrane association but does not span the bilayer. CPT2 adopts a hairpin polytopic conformation with only a 27-residue loop predicted to be exposed to the intermembrane space (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 1-3). The protein is more lightly attached to the inner membrane compared to CPT1's firm anchoring to the outer membrane via two transmembrane domains (duan2024theroleof pages 4-5).

CPT2 is synthesized as a precursor protein with an N-terminal signal sequence that directs its import into the mitochondrion; this targeting peptide is cleaved during translocation (virmani2015thecarnitinepalmitoyl pages 4-5).

## 4. Structural Features and Catalytic Mechanism

### 4.1 Domain Architecture

The overall fold of CPT2 consists of N-terminal and C-terminal domains, each containing a **six-stranded central antiparallel β-sheet** surrounded by α-helices—a fold shared with other carnitine acyltransferases including CrAT and carnitine octanoyltransferase (rufer2009structuralinsightinto pages 5-7, duan2024theroleof pages 4-5).

### 4.2 Active Site

The active site of CPT2 is positioned at the interface between the N-terminal and C-terminal domains. It forms a **Y-shaped tunnel** with three binding sites for CoA, acyl, and carnitine moieties, with both the acyl and CoA tunnels opening to the protein surface (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4). Key catalytic and binding residues include:

- **His372:** A conserved catalytic histidine essential for catalytic activity, forming hydrogen bonds with substrates (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4).
- **Ser590:** Part of a conserved Ser-Thr-Ser motif that hydrogen bonds to carbonyl groups (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4).
- **Tyr486, Ser488, Thr499:** Bind the carboxylic group of carnitine (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4).
- **Arg498:** Forms strong interactions with Asp376 and Ser373 to position active-site residues for catalysis (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4).

A crystallized CPT2 structure (PDB: 2DEB) complexed with CoA and palmitate has provided further structural insights into substrate binding (volpicella2025carnitineoacetyltransferaseas pages 8-9).

## 5. Role in the Carnitine Shuttle and Fatty Acid β-Oxidation

### 5.1 The Carnitine Shuttle System

CPT2 functions as the terminal enzyme of the three-component carnitine shuttle, which transports long-chain fatty acids across the mitochondrial membranes for β-oxidation (duan2024theroleof pages 2-4, knottnerus2018disordersofmitochondrial pages 2-3):

1. **CPT1** (outer mitochondrial membrane): Converts cytosolic long-chain acyl-CoA to acylcarnitine, releasing CoA. This is the rate-limiting, malonyl-CoA-regulated step.
2. **CACT/SLC25A20** (inner mitochondrial membrane transporter): Translocates acylcarnitines across the inner membrane in exchange for free carnitine.
3. **CPT2** (inner mitochondrial membrane, matrix side): Reconverts acylcarnitines back to acyl-CoA by transferring the acyl group from carnitine to intramitochondrial CoA, releasing free carnitine for recycling.

The regenerated acyl-CoA then enters the β-oxidation spiral within the mitochondrial matrix, ultimately producing acetyl-CoA units that feed into the tricarboxylic acid (TCA) cycle for ATP production (virmani2015thecarnitinepalmitoyl pages 3-4, schlaepfer2020cpt1amediatedfatoxidation pages 32-32). The complete oxidation of a single palmitate molecule through this system yields approximately 106 ATP molecules, substantially exceeding the ~30 ATP produced from glucose metabolism (virmani2015thecarnitinepalmitoyl pages 3-4).

### 5.2 Regulation

A critical distinction between CPT2 and CPT1 is their regulation. CPT1 is the main regulatory point for fatty acid oxidation, being allosterically inhibited by malonyl-CoA (the first committed intermediate of fatty acid synthesis), thereby coordinating the inverse regulation of fatty acid synthesis and oxidation (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4, schreurs2010regulatoryenzymesof pages 2-3, duan2024theroleof pages 2-4). In contrast, wild-type CPT2 is **not subject to allosteric inhibition by malonyl-CoA** and is considered constitutively active rather than rate-limiting (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4, schreurs2010regulatoryenzymesof pages 2-3). However, CPT2 expression and activity levels can vary in response to physiological status (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4).

## 6. Evolutionary Context

Phylogenetic analysis reveals that CPT2 and CPT1, despite their functional partnership in the carnitine shuttle, are actually the **most distantly related genes** within the carnitine and choline acyltransferase family (hoek2018evolutionaryanalysisof pages 1-6). CPT2 is most closely related to yeast cytosolic carnitine transferases Sc-YAT1 and Sc-YAT2, whereas CPT1 shares closer ancestry with the intramitochondrial yeast enzyme Sc-CAT2 (hoek2018evolutionaryanalysisof pages 15-20, hoek2018evolutionaryanalysisof pages 1-6).

Remarkably, CPT2 and CPT1 underwent a **subcellular localization switch** during evolution relative to their ancestral yeast counterparts (hoek2018evolutionaryanalysisof pages 15-20, hoek2018evolutionaryanalysisof pages 6-10). Unlike CPT1, CPT2 did not undergo the isoform-expanding gene duplications seen in the CPT1 lineage, consistent with its constitutive, unregulated nature (hoek2018evolutionaryanalysisof pages 15-20). CPT2 shows relatively short evolutionary branch lengths, indicating stable protein sequences over evolutionary time (hoek2018evolutionaryanalysisof pages 10-15). The human CPT2 cDNA and protein sequences share approximately 85% and 82% similarity, respectively, with the rat orthologue (duan2024theroleof pages 4-5).

## 7. Disease Associations

### 7.1 CPT2 Deficiency

CPT2 deficiency (OMIM #255110, #600649, #608836) is an autosomal recessive inborn error of mitochondrial long-chain fatty acid oxidation. It represents the **most common inherited disorder of fatty acid metabolism affecting skeletal muscle** (castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7). The estimated incidence from newborn screening programs in Australia, Germany, and the USA is approximately **1:750,000 to 1:2,000,000**, with over 300 patients described in the literature (knottnerus2018disordersofmitochondrial pages 5-6).

Three clinical phenotypes are recognized, representing a spectrum of disease severity (elgharbawy2018inbornerrorsof pages 6-8, lu2024recurrentrhabdomyolysiscaused pages 4-4, thuillier2003correlationbetweengenotype pages 1-2):

- **Lethal neonatal form:** The most severe presentation, manifesting within days of birth with liver failure, hypoketotic hypoglycemia, cardiomyopathy, seizures, dysmorphic features, cystic renal dysplasia, and neuronal migration defects. Universally fatal, typically within the first month of life (lu2024recurrentrhabdomyolysiscaused pages 4-4, thuillier2003correlationbetweengenotype pages 1-2).
- **Severe infantile hepatocardiomuscular form:** Emerges within the first year of life with liver failure, cardiomyopathy, peripheral myopathy, seizures, and hypoglycemia, often triggered by fasting, stress, or infection. Life-threatening with poor prognosis (elgharbawy2018inbornerrorsof pages 6-8, lu2024recurrentrhabdomyolysiscaused pages 4-4).
- **Adult/myopathic form:** The most common phenotype (~192 of 245 reported cases in one review), characterized by recurrent episodes of exercise-induced myalgia, rhabdomyolysis, and myoglobinuria. Attacks are triggered by prolonged exercise, fasting, cold exposure, febrile illness, or infection. Physical examination and muscle appearance are typically normal between episodes. This form predominantly affects males (>75%) and does not affect longevity (elgharbawy2018inbornerrorsof pages 6-8, castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7, lu2024recurrentrhabdomyolysiscaused pages 2-3).

### 7.2 Mutational Landscape

Over 60 mutations in the CPT2 gene have been identified, with most being private mutations (lehmann2017musclecarnitinepalmitoyltransferase pages 1-3, knottnerus2018disordersofmitochondrial pages 6-7). The **p.S113L (c.338C>T) mutation** is the most prevalent, accounting for approximately 64% of variant alleles in the myopathic form and found in up to 90% of patients in either homozygous or compound heterozygous state (lehmann2017musclecarnitinepalmitoyltransferase pages 1-3, lu2024recurrentrhabdomyolysiscaused pages 3-4). Other notable mutations include p.P50H, p.F383Y, and p.V368I, the latter two accounting for 31.2% of alleles in the severe infantile form (lu2024recurrentrhabdomyolysiscaused pages 3-4, thuillier2003correlationbetweengenotype pages 1-2).

### 7.3 S113L Thermolability Mechanism

The common S113L variant demonstrates a distinctive **thermolabile mechanism**: at normal body temperature (37°C), the mutant enzyme displays normal catalytic activity and long-chain fatty acid oxidation flux appears normal in fibroblasts (lehmann2017musclecarnitinepalmitoyltransferase pages 1-3, knottnerus2018disordersofmitochondrial pages 6-7). However, at elevated temperatures (40–45°C), the S113L variant shows markedly accelerated enzyme inactivation and significantly reduced activity compared to wild-type (knottnerus2018disordersofmitochondrial pages 6-7, lehmann2017musclecarnitinepalmitoyltransferase pages 3-6). Molecular dynamics simulations revealed that the S113L mutation increases backbone flexibility at the mutation site (residues S110–L121), causing conformational changes in the binding pocket that alter substrate and inhibitor interactions (lehmann2017musclecarnitinepalmitoyltransferase pages 3-6). Additionally, the S113L mutant shows **abnormal sensitivity to malonyl-CoA inhibition**, meaning that even under fasting conditions when malonyl-CoA levels should decrease to permit fatty acid oxidation, the mutant enzyme remains significantly inhibited (lehmann2017musclecarnitinepalmitoyltransferase pages 3-6, lehmann2017musclecarnitinepalmitoyltransferase pages 6-8). Natural substrates such as palmitoyl-L-carnitine can partially stabilize the S113L variant (lehmann2017musclecarnitinepalmitoyltransferase pages 3-6).

### 7.4 CPT2 in Cancer

Recent research (2023–2024) has revealed **context-dependent roles for CPT2 in cancer biology**. CPT2 acts as a pro-carcinogenic factor in chronic lymphocytic leukemia (CLL), epithelial ovarian cancer, gastrointestinal cancer, and triple-negative breast cancer, promoting proliferation, migration, invasion, and chemoresistance (duan2024theroleof pages 11-12, duan2024theroleof pages 9-11). Conversely, CPT2 underexpression promotes cancer progression in hepatocellular carcinoma and colorectal cancer through mechanisms involving ROS signaling, glycolytic metabolism, and the Wnt/β-catenin pathway (duan2024theroleof pages 11-12).

At the post-translational level, recent work has identified that **CPT2 lactylation by AARS2** under hypoxic conditions inhibits oxidative phosphorylation by restricting fatty acid oxidation, while SIRT3-mediated reversal of this modification reactivates OXPHOS (duan2024theroleof pages 15-17). HRD1 has been identified as an E3 ubiquitin ligase for CPT2 in triple-negative breast cancer, though protein-level regulation of CPT2 remains understudied (duan2024theroleof pages 15-17).

### 7.5 CPT2 in NAFLD and Hepatocarcinogenesis

CPT2 dysfunction has been linked to nonalcoholic fatty liver disease (NAFLD)/metabolic dysfunction-associated fatty liver disease (MAFLD), where loss of CPT-II activity on the inner mitochondrial membrane leads to impaired long-chain fatty acid β-oxidation, lipid accumulation, and potential progression toward hepatocarcinogenesis involving liver cancer stem cell activation and the Wnt/β-catenin pathway (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 2-4).

## 8. Summary

The following table provides a consolidated overview of CPT2's key molecular, biochemical, and clinical properties:

| Category | Key property | Summary | Evidence |
|---|---|---|---|
| Gene/protein identity | Human target verification | **CPT2** encodes **carnitine O-palmitoyltransferase 2, mitochondrial** (CPT II), the inner-mitochondrial-membrane enzyme of the carnitine shuttle; it is distinct from CPT1 isoforms despite historical naming confusion in some resources. | (duan2024theroleof pages 2-4, ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4, ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 1-3) |
| Protein family | Family membership | CPT2 belongs to the **carnitine/choline acyltransferase family** and is evolutionarily distinct from CPT1 proteins, despite their complementary function in the shuttle. | (rufer2009structuralinsightinto pages 5-7, hoek2018evolutionaryanalysisof pages 15-20, hoek2018evolutionaryanalysisof pages 1-6) |
| Isoforms/expression | Tissue distribution | CPT2 is reported as a **single, ubiquitously expressed isoform**, with comparatively high functional importance in energy-demanding tissues such as heart, liver, and skeletal muscle. | (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 1-3, duan2024theroleof pages 4-5, ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4) |
| Core biochemical function | Enzymatic role | CPT2 catalyzes the **final step of the carnitine shuttle**, regenerating mitochondrial **acyl-CoA** from **acylcarnitine** and releasing **free L-carnitine**, thereby enabling long-chain fatty acid β-oxidation. | (violante2010carnitinepalmitoyltransferase2 pages 1-2, duan2024theroleof pages 2-4, knottnerus2018disordersofmitochondrial pages 2-3) |
| Reaction | Catalyzed chemistry | The reaction is reversible and can be written as **acylcarnitine + CoA ⇌ acyl-CoA + carnitine**; under some experimental conditions CPT2 can also catalyze the reverse direction with acyl-CoA + carnitine. | (violante2010carnitinepalmitoyltransferase2 pages 3-4, virmani2015thecarnitinepalmitoyl pages 3-4, duan2024theroleof pages 2-4) |
| Physiologic substrates | Main substrate class | CPT2 primarily handles **medium- to long-chain fatty acyl groups**, especially those entering mitochondria for oxidation after CPT1/CACT-mediated transport. | (violante2010carnitinepalmitoyltransferase2 pages 1-2, schlaepfer2020cpt1amediatedfatoxidation pages 32-32) |
| Substrate specificity | Chain-length preference | Human CPT2 shows activity across about **C8-C20**, with **C10-C14** reported as preferred and robust activity for common long-chain substrates such as C12 and C16 species. | (violante2010carnitinepalmitoyltransferase2 pages 4-4, violante2010carnitinepalmitoyltransferase2 pages 3-4) |
| Specificity limits | Poor/negative substrates | CPT2 has **very low activity toward short-chain and very-long-chain substrates**, poor activity toward **trans-2-enoyl-CoA** intermediates, and does **not** significantly process branched-chain amino acid oxidation intermediates. | (violante2010carnitinepalmitoyltransferase2 pages 1-2, violante2010carnitinepalmitoyltransferase2 pages 3-4, violante2010carnitinepalmitoyltransferase2 pages 4-4) |
| Pathway role | Carnitine shuttle | CPT2 works with **CPT1** on the outer mitochondrial membrane and **CACT/SLC25A20** on the inner membrane to move long-chain fatty acid equivalents into the matrix for oxidation. | (knottnerus2018disordersofmitochondrial pages 2-3, virmani2015thecarnitinepalmitoyl pages 4-5, schlaepfer2020cpt1amediatedfatoxidation pages 32-32) |
| Cellular localization | Organelle/subcompartment | CPT2 is localized to the **inner mitochondrial membrane** and functions on the **matrix side/intramitochondrial space**, consistent with regeneration of β-oxidation-competent acyl-CoA inside mitochondria. | (duan2024theroleof pages 2-4, rufer2009structuralinsightinto pages 2-4, virmani2015thecarnitinepalmitoyl pages 3-4) |
| Membrane topology | Membrane association | Structural studies indicate CPT2 is **monomeric** and associated with the inner membrane through a **membrane-anchoring insertion** that inserts into the **inner leaflet** rather than spanning the membrane like CPT1. | (rufer2009structuralinsightinto pages 4-5, rufer2009structuralinsightinto pages 5-7) |
| Precursor processing | Mitochondrial targeting | CPT2 is synthesized as a **precursor protein** with an **N-terminal targeting sequence** that is cleaved during mitochondrial import/localization. | (virmani2015thecarnitinepalmitoyl pages 4-5, duan2024theroleof pages 4-5) |
| Structural organization | Domain architecture | CPT2 has **N-terminal and C-terminal domains**, each built around a **six-stranded antiparallel β-sheet** surrounded by α-helices, with the active site located at the domain interface. | (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4, rufer2009structuralinsightinto pages 5-7) |
| Active-site architecture | Ligand-binding tunnel | The enzyme contains a **Y-shaped tunnel** accommodating **CoA**, **acyl**, and **carnitine** moieties; this architecture helps explain chain-length selectivity and acyltransferase chemistry. | (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4, rufer2009structuralinsightinto pages 5-7) |
| Catalytic residues | Key residues/mechanism | Important structural/catalytic residues include **His372**, **Ser590**, and carnitine-binding residues such as **Tyr486, Ser488, Thr499**, with **Arg498** helping position active-site elements. | (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4) |
| Regulation vs CPT1 | Malonyl-CoA sensitivity | Unlike CPT1, CPT2 is generally described as **not allosterically inhibited by malonyl-CoA** and is **not the main rate-limiting regulatory step** of fatty acid entry into mitochondria. | (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4, schreurs2010regulatoryenzymesof pages 2-3, duan2024theroleof pages 2-4) |
| Evolution | Relationship to CPT1 | CPT2 and CPT1 are functionally linked but **evolutionarily distant** within the acyltransferase family; CPT2 appears to have undergone a distinct evolutionary trajectory without the isoform-expanding duplications seen for CPT1. | (hoek2018evolutionaryanalysisof pages 15-20, hoek2018evolutionaryanalysisof pages 1-6, hoek2018evolutionaryanalysisof pages 10-15) |
| Human disease | Deficiency syndrome | **CPT2 deficiency** is a rare autosomal recessive long-chain fatty acid oxidation disorder with three major forms: **neonatal lethal**, **severe infantile hepatocardiomuscular**, and **adult/myopathic**. | (elgharbawy2018inbornerrorsof pages 6-8, lu2024recurrentrhabdomyolysiscaused pages 4-4, thuillier2003correlationbetweengenotype pages 1-2) |
| Clinical manifestations | Major phenotypes | Severe forms feature **hypoketotic hypoglycemia, liver dysfunction/failure, cardiomyopathy, renal/cerebral anomalies**, whereas the common myopathic form causes **exercise-induced myalgia, rhabdomyolysis, and myoglobinuria** with normal intervals between attacks. | (elgharbawy2018inbornerrorsof pages 6-8, castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7, knottnerus2018disordersofmitochondrial pages 5-6) |
| Disease epidemiology | Recent summary statistics | Literature summaries report **>300 described patients** and newborn-screening-based incidence estimates around **1:750,000 to 1:2,000,000**, although ascertainment is incomplete. | (lu2024recurrentrhabdomyolysiscaused pages 2-3, knottnerus2018disordersofmitochondrial pages 5-6) |
| Mutational landscape | Common variants | More than **60 CPT2 mutations** have been reported; **p.S113L** is the most common mutation in the myopathic form, accounting for roughly **64% of variant alleles** in one 2024 literature summary and up to **90%** in older cohorts/reviews. | (lu2024recurrentrhabdomyolysiscaused pages 3-4, lehmann2017musclecarnitinepalmitoyltransferase pages 1-3, knottnerus2018disordersofmitochondrial pages 6-7) |
| Variant mechanism | S113L effect | The common **S113L** variant is often **thermolabile** rather than catalytically dead at baseline, showing reduced stability and increased inhibition susceptibility under metabolic stress, helping explain attacks during fever, exercise, fasting, or cold exposure. | (lehmann2017musclecarnitinepalmitoyltransferase pages 1-3, lehmann2017musclecarnitinepalmitoyltransferase pages 3-6, lehmann2017musclecarnitinepalmitoyltransferase pages 6-8) |
| Recent research directions | 2023-2024 developments | Recent work links CPT2 dysfunction or altered expression to **NAFLD/MAFLD and hepatocarcinogenesis**, and cancer literature describes **context-dependent roles** for CPT2, acting as either tumor-promoting or tumor-suppressive depending on tissue context. | (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 2-4, duan2024theroleof pages 11-12, duan2024theroleof pages 15-17) |


*Table: This table summarizes the main molecular, biochemical, structural, and clinical properties of human CPT2. It is useful as a compact reference for functional annotation and for distinguishing CPT2’s core mitochondrial fatty-acid-oxidation role from disease and emerging cancer-related findings.*

In summary, CPT2 is the inner mitochondrial membrane enzyme that catalyzes the final step of the carnitine shuttle, reconverting acylcarnitines to acyl-CoA within the mitochondrial matrix to enable long-chain fatty acid β-oxidation. It is a single-isoform, ubiquitously expressed enzyme with substrate preference for medium- to long-chain (C8–C18) acyl species. Unlike CPT1, CPT2 is constitutively active and not allosterically regulated by malonyl-CoA under normal physiological conditions. Deficiency of CPT2 causes a spectrum of disease from fatal neonatal multiorgan failure to the most common inherited muscular lipid metabolism disorder, with the thermolabile S113L variant underlying the majority of myopathic cases. Emerging research highlights additional roles for CPT2 in cancer metabolism and liver disease pathogenesis.


References

1. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 2-4): Min Yao, Ping Zhou, Yan-Yan Qin, Li Wang, and Dengbing Yao. Mitochondrial carnitine palmitoyltransferase-ii dysfunction: a possible novel mechanism for nonalcoholic fatty liver disease in hepatocarcinogenesis. World Journal of Gastroenterology, 29:1765-1778, Mar 2023. URL: https://doi.org/10.3748/wjg.v29.i12.1765, doi:10.3748/wjg.v29.i12.1765. This article has 14 citations.

2. (virmani2015thecarnitinepalmitoyl pages 4-5): Ashraf Virmani, Luigi Pinto, Otto Bauermann, Saf Zerelli, Andreas Diedenhofen, Zbigniew K. Binienda, Syed F. Ali, and Feike R. van der Leij. The carnitine palmitoyl transferase (cpt) system and possible relevance for neuropsychiatric and neurological conditions. Molecular Neurobiology, 52:826-836, Jun 2015. URL: https://doi.org/10.1007/s12035-015-9238-7, doi:10.1007/s12035-015-9238-7. This article has 81 citations and is from a peer-reviewed journal.

3. (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 1-3): Simona M. Ceccarelli, Odile Chomienne, Marcel Gubler, and Arduino Arduini. Carnitine palmitoyltransferase (cpt) modulators: a medicinal chemistry perspective on 35 years of research. Journal of medicinal chemistry, 54 9:3109-52, Apr 2011. URL: https://doi.org/10.1021/jm100809g, doi:10.1021/jm100809g. This article has 129 citations and is from a highest quality peer-reviewed journal.

4. (duan2024theroleof pages 4-5): Yanxia Duan, Jiaxin Liu, Ailin Li, Chang Liu, Guang Shu, and Gang Yin. The role of the cpt family in cancer: searching for new therapeutic strategies. Biology, 13:892, Nov 2024. URL: https://doi.org/10.3390/biology13110892, doi:10.3390/biology13110892. This article has 16 citations.

5. (ceccarelli2011carnitinepalmitoyltransferase(cpt) pages 3-4): Simona M. Ceccarelli, Odile Chomienne, Marcel Gubler, and Arduino Arduini. Carnitine palmitoyltransferase (cpt) modulators: a medicinal chemistry perspective on 35 years of research. Journal of medicinal chemistry, 54 9:3109-52, Apr 2011. URL: https://doi.org/10.1021/jm100809g, doi:10.1021/jm100809g. This article has 129 citations and is from a highest quality peer-reviewed journal.

6. (schreurs2010regulatoryenzymesof pages 2-3): M. Schreurs, F. Kuipers, and F. R. Van Der Leij. Regulatory enzymes of mitochondrial β‐oxidation as targets for treatment of the metabolic syndrome. Obesity Reviews, 11:380-388, May 2010. URL: https://doi.org/10.1111/j.1467-789x.2009.00642.x, doi:10.1111/j.1467-789x.2009.00642.x. This article has 371 citations and is from a peer-reviewed journal.

7. (violante2010carnitinepalmitoyltransferase2 pages 1-2): Sara Violante, Lodewijk IJlst, Henk van Lenthe, Isabel Tavares de Almeida, Ronald J. Wanders, and Fátima V. Ventura. Carnitine palmitoyltransferase 2: new insights on the substrate specificity and implications for acylcarnitine profiling. Biochimica et biophysica acta, 1802 9:728-32, Sep 2010. URL: https://doi.org/10.1016/j.bbadis.2010.06.002, doi:10.1016/j.bbadis.2010.06.002. This article has 64 citations.

8. (duan2024theroleof pages 2-4): Yanxia Duan, Jiaxin Liu, Ailin Li, Chang Liu, Guang Shu, and Gang Yin. The role of the cpt family in cancer: searching for new therapeutic strategies. Biology, 13:892, Nov 2024. URL: https://doi.org/10.3390/biology13110892, doi:10.3390/biology13110892. This article has 16 citations.

9. (virmani2015thecarnitinepalmitoyl pages 3-4): Ashraf Virmani, Luigi Pinto, Otto Bauermann, Saf Zerelli, Andreas Diedenhofen, Zbigniew K. Binienda, Syed F. Ali, and Feike R. van der Leij. The carnitine palmitoyl transferase (cpt) system and possible relevance for neuropsychiatric and neurological conditions. Molecular Neurobiology, 52:826-836, Jun 2015. URL: https://doi.org/10.1007/s12035-015-9238-7, doi:10.1007/s12035-015-9238-7. This article has 81 citations and is from a peer-reviewed journal.

10. (knottnerus2018disordersofmitochondrial pages 2-3): Suzan J. G. Knottnerus, Jeannette C. Bleeker, Rob C. I. Wüst, Sacha Ferdinandusse, Lodewijk IJlst, Frits A. Wijburg, Ronald J. A. Wanders, Gepke Visser, and Riekelt H. Houtkooper. Disorders of mitochondrial long-chain fatty acid oxidation and the carnitine shuttle. Reviews in Endocrine & Metabolic Disorders, 19:93-106, Mar 2018. URL: https://doi.org/10.1007/s11154-018-9448-1, doi:10.1007/s11154-018-9448-1. This article has 385 citations and is from a peer-reviewed journal.

11. (schlaepfer2020cpt1amediatedfatoxidation pages 32-32): Isabel R Schlaepfer and Molishree Joshi. Cpt1a-mediated fat oxidation, mechanisms and therapeutic potential. Endocrinology, Jan 2020. URL: https://doi.org/10.1210/endocr/bqz046, doi:10.1210/endocr/bqz046. This article has 807 citations and is from a domain leading peer-reviewed journal.

12. (violante2010carnitinepalmitoyltransferase2 pages 4-4): Sara Violante, Lodewijk IJlst, Henk van Lenthe, Isabel Tavares de Almeida, Ronald J. Wanders, and Fátima V. Ventura. Carnitine palmitoyltransferase 2: new insights on the substrate specificity and implications for acylcarnitine profiling. Biochimica et biophysica acta, 1802 9:728-32, Sep 2010. URL: https://doi.org/10.1016/j.bbadis.2010.06.002, doi:10.1016/j.bbadis.2010.06.002. This article has 64 citations.

13. (violante2010carnitinepalmitoyltransferase2 pages 3-4): Sara Violante, Lodewijk IJlst, Henk van Lenthe, Isabel Tavares de Almeida, Ronald J. Wanders, and Fátima V. Ventura. Carnitine palmitoyltransferase 2: new insights on the substrate specificity and implications for acylcarnitine profiling. Biochimica et biophysica acta, 1802 9:728-32, Sep 2010. URL: https://doi.org/10.1016/j.bbadis.2010.06.002, doi:10.1016/j.bbadis.2010.06.002. This article has 64 citations.

14. (rufer2009structuralinsightinto pages 2-4): Arne C. Rufer, Ralf Thoma, and Michael Hennig. Structural insight into function and regulation of carnitine palmitoyltransferase. Cellular and Molecular Life Sciences, 66:2489-2501, May 2009. URL: https://doi.org/10.1007/s00018-009-0035-1, doi:10.1007/s00018-009-0035-1. This article has 113 citations and is from a domain leading peer-reviewed journal.

15. (rufer2009structuralinsightinto pages 5-7): Arne C. Rufer, Ralf Thoma, and Michael Hennig. Structural insight into function and regulation of carnitine palmitoyltransferase. Cellular and Molecular Life Sciences, 66:2489-2501, May 2009. URL: https://doi.org/10.1007/s00018-009-0035-1, doi:10.1007/s00018-009-0035-1. This article has 113 citations and is from a domain leading peer-reviewed journal.

16. (rufer2009structuralinsightinto pages 4-5): Arne C. Rufer, Ralf Thoma, and Michael Hennig. Structural insight into function and regulation of carnitine palmitoyltransferase. Cellular and Molecular Life Sciences, 66:2489-2501, May 2009. URL: https://doi.org/10.1007/s00018-009-0035-1, doi:10.1007/s00018-009-0035-1. This article has 113 citations and is from a domain leading peer-reviewed journal.

17. (volpicella2025carnitineoacetyltransferaseas pages 8-9): Mariateresa Volpicella, Maria Noemi Sgobba, Luna Laera, Anna Lucia Francavilla, Danila Imperia De Luca, Lorenzo Guerra, Ciro Leonardo Pierri, and Anna De Grassi. Carnitine o-acetyltransferase as a central player in lipid and branched-chain amino acid metabolism, epigenetics, cell plasticity, and organelle function. Biomolecules, 15:216, Feb 2025. URL: https://doi.org/10.3390/biom15020216, doi:10.3390/biom15020216. This article has 22 citations.

18. (hoek2018evolutionaryanalysisof pages 1-6): Marjanne D. van der Hoek, Ole Madsen, Jaap Keijer, and Feike R. van der Leij. Evolutionary analysis of the carnitine- and choline acyltransferases suggests distinct evolution of cpt2 versus cpt1 and related variants. Biochimica et Biophysica Acta (BBA) - Molecular and Cell Biology of Lipids, 1863(8):909-918, Aug 2018. URL: https://doi.org/10.1016/j.bbalip.2018.05.001, doi:10.1016/j.bbalip.2018.05.001. This article has 10 citations and is from a peer-reviewed journal.

19. (hoek2018evolutionaryanalysisof pages 15-20): Marjanne D. van der Hoek, Ole Madsen, Jaap Keijer, and Feike R. van der Leij. Evolutionary analysis of the carnitine- and choline acyltransferases suggests distinct evolution of cpt2 versus cpt1 and related variants. Biochimica et Biophysica Acta (BBA) - Molecular and Cell Biology of Lipids, 1863(8):909-918, Aug 2018. URL: https://doi.org/10.1016/j.bbalip.2018.05.001, doi:10.1016/j.bbalip.2018.05.001. This article has 10 citations and is from a peer-reviewed journal.

20. (hoek2018evolutionaryanalysisof pages 6-10): Marjanne D. van der Hoek, Ole Madsen, Jaap Keijer, and Feike R. van der Leij. Evolutionary analysis of the carnitine- and choline acyltransferases suggests distinct evolution of cpt2 versus cpt1 and related variants. Biochimica et Biophysica Acta (BBA) - Molecular and Cell Biology of Lipids, 1863(8):909-918, Aug 2018. URL: https://doi.org/10.1016/j.bbalip.2018.05.001, doi:10.1016/j.bbalip.2018.05.001. This article has 10 citations and is from a peer-reviewed journal.

21. (hoek2018evolutionaryanalysisof pages 10-15): Marjanne D. van der Hoek, Ole Madsen, Jaap Keijer, and Feike R. van der Leij. Evolutionary analysis of the carnitine- and choline acyltransferases suggests distinct evolution of cpt2 versus cpt1 and related variants. Biochimica et Biophysica Acta (BBA) - Molecular and Cell Biology of Lipids, 1863(8):909-918, Aug 2018. URL: https://doi.org/10.1016/j.bbalip.2018.05.001, doi:10.1016/j.bbalip.2018.05.001. This article has 10 citations and is from a peer-reviewed journal.

22. (castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7): Efrain Castillo, Debbie Medina, and Nick Schoenmann. Myopathic carnitine palmitoyltransferase ii (cpt ii) deficiency: a rare cause of acute kidney injury and cardiomyopathy. Cureus, Oct 2023. URL: https://doi.org/10.7759/cureus.46595, doi:10.7759/cureus.46595. This article has 6 citations.

23. (knottnerus2018disordersofmitochondrial pages 5-6): Suzan J. G. Knottnerus, Jeannette C. Bleeker, Rob C. I. Wüst, Sacha Ferdinandusse, Lodewijk IJlst, Frits A. Wijburg, Ronald J. A. Wanders, Gepke Visser, and Riekelt H. Houtkooper. Disorders of mitochondrial long-chain fatty acid oxidation and the carnitine shuttle. Reviews in Endocrine & Metabolic Disorders, 19:93-106, Mar 2018. URL: https://doi.org/10.1007/s11154-018-9448-1, doi:10.1007/s11154-018-9448-1. This article has 385 citations and is from a peer-reviewed journal.

24. (elgharbawy2018inbornerrorsof pages 6-8): Areeg El-Gharbawy and Jerry Vockley. Inborn errors of metabolism with myopathy. Apr 2018. URL: https://doi.org/10.1016/j.pcl.2017.11.006, doi:10.1016/j.pcl.2017.11.006. This article has 130 citations and is from a peer-reviewed journal.

25. (lu2024recurrentrhabdomyolysiscaused pages 4-4): Chih-Hsuan Lu, Chia-Feng Yang, Yun-Ru Chen, Yann-Jang Chen, Yung-Hsiu Lu, and Dau-Ming Niu. Recurrent rhabdomyolysis caused by palmitoyltransferase ii (cpt-2) deficiency but complete normal acylcarnitine profile: a patient presentation and review of the literature. Molecular Genetics and Metabolism Reports, 41:101151, Dec 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101151, doi:10.1016/j.ymgmr.2024.101151. This article has 4 citations.

26. (thuillier2003correlationbetweengenotype pages 1-2): Laure Thuillier, Hidayeth Rostane, Veronique Droin, France Demaugre, Michèle Brivet, Noman Kadhom, Carina Prip-Buus, Stéphanie Gobin, Jean-Marie Saudubray, and Jean-Paul Bonnefont. Correlation between genotype, metabolic data, and clinical presentation in carnitine palmitoyltransferase 2 (cpt2) deficiency. Human Mutation, 21:493-501, May 2003. URL: https://doi.org/10.1002/humu.10201, doi:10.1002/humu.10201. This article has 136 citations and is from a domain leading peer-reviewed journal.

27. (lu2024recurrentrhabdomyolysiscaused pages 2-3): Chih-Hsuan Lu, Chia-Feng Yang, Yun-Ru Chen, Yann-Jang Chen, Yung-Hsiu Lu, and Dau-Ming Niu. Recurrent rhabdomyolysis caused by palmitoyltransferase ii (cpt-2) deficiency but complete normal acylcarnitine profile: a patient presentation and review of the literature. Molecular Genetics and Metabolism Reports, 41:101151, Dec 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101151, doi:10.1016/j.ymgmr.2024.101151. This article has 4 citations.

28. (lehmann2017musclecarnitinepalmitoyltransferase pages 1-3): Diana Lehmann, Leila Scholle, Dina Robaa, and Stephan Zierz. Muscle carnitine palmitoyltransferase ii deficiency: a review of enzymatic controversy and clinical features. International Journal of Molecular Sciences, Jan 2017. URL: https://doi.org/10.3390/ijms18010082, doi:10.3390/ijms18010082. This article has 45 citations.

29. (knottnerus2018disordersofmitochondrial pages 6-7): Suzan J. G. Knottnerus, Jeannette C. Bleeker, Rob C. I. Wüst, Sacha Ferdinandusse, Lodewijk IJlst, Frits A. Wijburg, Ronald J. A. Wanders, Gepke Visser, and Riekelt H. Houtkooper. Disorders of mitochondrial long-chain fatty acid oxidation and the carnitine shuttle. Reviews in Endocrine & Metabolic Disorders, 19:93-106, Mar 2018. URL: https://doi.org/10.1007/s11154-018-9448-1, doi:10.1007/s11154-018-9448-1. This article has 385 citations and is from a peer-reviewed journal.

30. (lu2024recurrentrhabdomyolysiscaused pages 3-4): Chih-Hsuan Lu, Chia-Feng Yang, Yun-Ru Chen, Yann-Jang Chen, Yung-Hsiu Lu, and Dau-Ming Niu. Recurrent rhabdomyolysis caused by palmitoyltransferase ii (cpt-2) deficiency but complete normal acylcarnitine profile: a patient presentation and review of the literature. Molecular Genetics and Metabolism Reports, 41:101151, Dec 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101151, doi:10.1016/j.ymgmr.2024.101151. This article has 4 citations.

31. (lehmann2017musclecarnitinepalmitoyltransferase pages 3-6): Diana Lehmann, Leila Scholle, Dina Robaa, and Stephan Zierz. Muscle carnitine palmitoyltransferase ii deficiency: a review of enzymatic controversy and clinical features. International Journal of Molecular Sciences, Jan 2017. URL: https://doi.org/10.3390/ijms18010082, doi:10.3390/ijms18010082. This article has 45 citations.

32. (lehmann2017musclecarnitinepalmitoyltransferase pages 6-8): Diana Lehmann, Leila Scholle, Dina Robaa, and Stephan Zierz. Muscle carnitine palmitoyltransferase ii deficiency: a review of enzymatic controversy and clinical features. International Journal of Molecular Sciences, Jan 2017. URL: https://doi.org/10.3390/ijms18010082, doi:10.3390/ijms18010082. This article has 45 citations.

33. (duan2024theroleof pages 11-12): Yanxia Duan, Jiaxin Liu, Ailin Li, Chang Liu, Guang Shu, and Gang Yin. The role of the cpt family in cancer: searching for new therapeutic strategies. Biology, 13:892, Nov 2024. URL: https://doi.org/10.3390/biology13110892, doi:10.3390/biology13110892. This article has 16 citations.

34. (duan2024theroleof pages 9-11): Yanxia Duan, Jiaxin Liu, Ailin Li, Chang Liu, Guang Shu, and Gang Yin. The role of the cpt family in cancer: searching for new therapeutic strategies. Biology, 13:892, Nov 2024. URL: https://doi.org/10.3390/biology13110892, doi:10.3390/biology13110892. This article has 16 citations.

35. (duan2024theroleof pages 15-17): Yanxia Duan, Jiaxin Liu, Ailin Li, Chang Liu, Guang Shu, and Gang Yin. The role of the cpt family in cancer: searching for new therapeutic strategies. Biology, 13:892, Nov 2024. URL: https://doi.org/10.3390/biology13110892, doi:10.3390/biology13110892. This article has 16 citations.

## Artifacts

- [Edison artifact artifact-00](CPT2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. schreurs2010regulatoryenzymesof pages 2-3
2. virmani2015thecarnitinepalmitoyl pages 3-4
3. rufer2009structuralinsightinto pages 5-7
4. duan2024theroleof pages 4-5
5. virmani2015thecarnitinepalmitoyl pages 4-5
6. volpicella2025carnitineoacetyltransferaseas pages 8-9
7. hoek2018evolutionaryanalysisof pages 1-6
8. hoek2018evolutionaryanalysisof pages 15-20
9. hoek2018evolutionaryanalysisof pages 10-15
10. castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7
11. knottnerus2018disordersofmitochondrial pages 5-6
12. lehmann2017musclecarnitinepalmitoyltransferase pages 3-6
13. duan2024theroleof pages 11-12
14. duan2024theroleof pages 15-17
15. yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 2-4
16. duan2024theroleof pages 2-4
17. knottnerus2018disordersofmitochondrial pages 2-3
18. rufer2009structuralinsightinto pages 2-4
19. rufer2009structuralinsightinto pages 4-5
20. hoek2018evolutionaryanalysisof pages 6-10
21. elgharbawy2018inbornerrorsof pages 6-8
22. lu2024recurrentrhabdomyolysiscaused pages 4-4
23. thuillier2003correlationbetweengenotype pages 1-2
24. lu2024recurrentrhabdomyolysiscaused pages 2-3
25. lehmann2017musclecarnitinepalmitoyltransferase pages 1-3
26. knottnerus2018disordersofmitochondrial pages 6-7
27. lu2024recurrentrhabdomyolysiscaused pages 3-4
28. lehmann2017musclecarnitinepalmitoyltransferase pages 6-8
29. duan2024theroleof pages 9-11
30. https://doi.org/10.3748/wjg.v29.i12.1765,
31. https://doi.org/10.1007/s12035-015-9238-7,
32. https://doi.org/10.1021/jm100809g,
33. https://doi.org/10.3390/biology13110892,
34. https://doi.org/10.1111/j.1467-789x.2009.00642.x,
35. https://doi.org/10.1016/j.bbadis.2010.06.002,
36. https://doi.org/10.1007/s11154-018-9448-1,
37. https://doi.org/10.1210/endocr/bqz046,
38. https://doi.org/10.1007/s00018-009-0035-1,
39. https://doi.org/10.3390/biom15020216,
40. https://doi.org/10.1016/j.bbalip.2018.05.001,
41. https://doi.org/10.7759/cureus.46595,
42. https://doi.org/10.1016/j.pcl.2017.11.006,
43. https://doi.org/10.1016/j.ymgmr.2024.101151,
44. https://doi.org/10.1002/humu.10201,
45. https://doi.org/10.3390/ijms18010082,