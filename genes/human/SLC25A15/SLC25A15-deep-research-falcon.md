---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T13:41:11.566354'
end_time: '2026-07-05T13:56:54.667433'
duration_seconds: 943.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SLC25A15
  gene_symbol: SLC25A15
  uniprot_accession: Q9Y619
  protein_description: 'RecName: Full=Mitochondrial ornithine transporter 1; AltName:
    Full=Solute carrier family 25 member 15;'
  gene_info: Name=SLC25A15 {ECO:0000312|HGNC:HGNC:10985}; Synonyms=ORC1 {ECO:0000303|PubMed:12807890},
    ORNT1 {ECO:0000303|PubMed:10369256}; ORFNames=SP1855;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the mitochondrial carrier (TC 2.A.29) family.
  protein_domains: MCP_dom_sf. (IPR023395); MCP_transmembrane. (IPR018108); Mitochondrial_Carrier.
    (IPR050567); Mito_carr (PF00153)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: SLC25A15-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: SLC25A15-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q9Y619
- **Protein Description:** RecName: Full=Mitochondrial ornithine transporter 1; AltName: Full=Solute carrier family 25 member 15;
- **Gene Information:** Name=SLC25A15 {ECO:0000312|HGNC:HGNC:10985}; Synonyms=ORC1 {ECO:0000303|PubMed:12807890}, ORNT1 {ECO:0000303|PubMed:10369256}; ORFNames=SP1855;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the mitochondrial carrier (TC 2.A.29) family.
- **Key Domains:** MCP_dom_sf. (IPR023395); MCP_transmembrane. (IPR018108); Mitochondrial_Carrier. (IPR050567); Mito_carr (PF00153)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SLC25A15" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SLC25A15' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SLC25A15** (gene ID: SLC25A15, UniProt: Q9Y619) in human.

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
- **UniProt Accession:** Q9Y619
- **Protein Description:** RecName: Full=Mitochondrial ornithine transporter 1; AltName: Full=Solute carrier family 25 member 15;
- **Gene Information:** Name=SLC25A15 {ECO:0000312|HGNC:HGNC:10985}; Synonyms=ORC1 {ECO:0000303|PubMed:12807890}, ORNT1 {ECO:0000303|PubMed:10369256}; ORFNames=SP1855;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the mitochondrial carrier (TC 2.A.29) family.
- **Key Domains:** MCP_dom_sf. (IPR023395); MCP_transmembrane. (IPR018108); Mitochondrial_Carrier. (IPR050567); Mito_carr (PF00153)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SLC25A15" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SLC25A15' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SLC25A15** (gene ID: SLC25A15, UniProt: Q9Y619) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: SLC25A15 (Mitochondrial Ornithine Transporter 1 / ORC1 / ORNT1)

## 1. Gene and Protein Identity

SLC25A15 (Solute Carrier Family 25 Member 15) encodes Mitochondrial Ornithine Transporter 1, also known as Ornithine Carrier 1 (ORC1) or ORNT1 (UniProt: Q9Y619). It is a member of the mitochondrial carrier family (SLC25/TC 2.A.29), a large family of transport proteins embedded in the inner mitochondrial membrane that facilitate the translocation of diverse small molecules between the mitochondrial intermembrane space and the matrix (palmieri2013themitochondrialtransporter pages 3-6). The gene is located on human chromosome 13q14 and encodes a 301 amino acid protein (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).

The following table summarizes the key properties of SLC25A15/ORC1:

| Property | Summary |
|---|---|
| Gene name | **SLC25A15** (solute carrier family 25 member 15) (OpenTargets Search: -SLC25A15, gutierrezaguilar2013physiologicalandpathological pages 3-4) |
| Aliases | **ORC1**, **ORNT1** (gutierrezaguilar2013physiologicalandpathological pages 3-4, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) |
| Protein name | **Mitochondrial ornithine transporter 1** / **ornithine carrier 1 (ORC1)** (gao2024cancertherapeuticpotential pages 6-7, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) |
| UniProt ID | **Q9Y619** (provided target identity) |
| Chromosomal location | **13q14** / chromosome 13 locus reported for human **SLC25A15** (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, tessa2009identificationofnovel pages 3-4) |
| Protein length | **301 amino acids** (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) |
| Subcellular localization | **Inner mitochondrial membrane**; carrier with N- and C-termini exposed to the cytosolic/intermembrane-space side (tessa2009identificationofnovel pages 5-6, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) |
| Primary substrates | **L-ornithine, L-citrulline, L-arginine, L-lysine**; transport is stereoselective for the L-forms in ORC1 (monne2012substratespecificityof pages 1-2, monne2012substratespecificityof pages 3-4) |
| Transport mechanism | **Electroneutral antiport**, classically exchanging **cytosolic ornithine** for **matrix citrulline + H+** in a strict 1:1 mode (gao2024cancertherapeuticpotential pages 6-7, monne2012substratespecificityof pages 3-4, palmieri2020diseasescausedby pages 13-15) |
| Tissue expression | Highest/major expression reported in **liver, pancreas, lung, kidney**; broader tissue expression also noted (gutierrezaguilar2013physiologicalandpathological pages 3-4, ahmed2024theroleof pages 16-18) |
| Key substrate-binding / mechanistic residues | **E77, R179, E180** directly contribute to substrate binding; **W224** and **R275** help couple binding to conformational change/translocation (monne2012substratespecificityof pages 1-2, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, monne2012substratespecificityof pages 7-8) |
| Structural class | Member of the **mitochondrial carrier family (SLC25)** with **6 transmembrane α-helices** and tripartite architecture (tessa2009identificationofnovel pages 5-6, palmieri2013themitochondrialtransporter pages 3-6) |
| Associated disease | **Hyperornithinemia-hyperammonemia-homocitrullinuria (HHH) syndrome** / ornithine translocase deficiency (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, palmieri2020diseasescausedby pages 13-15, OpenTargets Search: -SLC25A15) |
| Paralogues / related compensatory carriers | **ORC2 / SLC25A2**: 87% identical paralogue with lower affinity and broader substrate range; **ORNT3 / SLC25A29**: related basic amino acid carrier that can rescue ornithine metabolism in HHH fibroblasts (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9, gutierrezaguilar2013physiologicalandpathological pages 3-4, camacho2009thehumanand pages 6-7) |


*Table: This table summarizes the core identity, localization, transport properties, structural determinants, disease relevance, and related paralogues of human SLC25A15/ORC1. It is useful as a compact reference for functional annotation and pathway interpretation.*

## 2. Primary Transport Function and Substrate Specificity

SLC25A15/ORC1 functions as an **electroneutral antiporter** at the inner mitochondrial membrane, catalyzing the **1:1 exchange of cytoplasmic L-ornithine for mitochondrial matrix L-citrulline plus a proton (H+)** (palmieri2020diseasescausedby pages 13-15, monne2012substratespecificityof pages 3-4). This transport is the physiologically essential step that bridges the mitochondrial and cytoplasmic segments of the urea cycle (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, cunningham202020000picometersunder pages 4-5). The proton co-transport neutralizes the positive charge of ornithine during the exchange process, rendering the transport electrically neutral (gao2024cancertherapeuticpotential pages 6-7).

The substrate specificity of ORC1 is restricted to the **L-forms of ornithine, citrulline, lysine, and arginine** (monne2012substratespecificityof pages 1-2). Among these, ORC1 shows highest affinity for L-ornithine, followed by L-arginine and L-lysine (mentel2021learningfromyeast pages 20-21). The stereospecificity for L-isomers is a distinguishing feature of ORC1 compared to ORC2, which can also transport D-isomers and histidine (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9, mentel2021learningfromyeast pages 21-22). ORC1 operates as a strict 1:1 antiporter, meaning it exchanges substrates in a one-to-one stoichiometric ratio across the membrane (monne2012substratespecificityof pages 3-4).

Transport activity has been characterized through reconstitution of bacterially expressed ORC1 protein into proteoliposomes, enabling detailed kinetic and substrate specificity measurements (tessa2009identificationofnovel pages 1-2, tessa2009identificationofnovel pages 3-4).

## 3. Protein Structure and Transport Mechanism

ORC1 adopts the characteristic **tripartite architecture** of the SLC25 mitochondrial carrier family, consisting of three tandemly repeated homologous domains, each approximately 100 amino acids in length and containing two hydrophobic transmembrane stretches (palmieri2013themitochondrialtransporter pages 3-6). The protein forms a barrel-like structure composed of **six transmembrane α-helices (H1–H6)** arranged counter-clockwise that surround a central cavity open toward the cytosolic (intermembrane space) side (tessa2009identificationofnovel pages 5-6, palmieri2013themitochondrialtransporter pages 3-6). Three additional short α-helices (h12, h34, h56) lie parallel to the membrane plane on the matrix side (tessa2009identificationofnovel pages 5-6). Both the N- and C-termini are exposed on the cytosolic side (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).

### 3.1 Substrate Binding Site

The substrate binding site is located within the central cavity and consists of **three major contact points** (monne2012substratespecificityof pages 1-2, monne2012substratespecificityof pages 2-3):

- **Contact Point I**: Glu-77 (E77) likely interacts with the terminal amino group of the substrate side chain (monne2012substratespecificityof pages 1-2, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).
- **Contact Point II**: Arg-179 (R179) and Glu-180 (E180) bind the Cα carboxylate and amino group of the substrates, respectively. R179 is a critical determinant of substrate specificity — the difference between R179 (in ORC1) and Q179 (in ORC2) is largely responsible for the differing substrate profiles of the two isoforms, and swapping this single residue can interchange their substrate specificities (monne2012substratespecificityof pages 1-2, monne2012substratespecificityof pages 3-4, monne2012substratespecificityof pages 8-9).
- **Contact Point III**: Arg-275 (R275), a highly conserved residue, is connected to R179 through Trp-224 (W224) via cation-π interactions, and is important for triggering substrate-induced conformational changes required for translocation (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, monne2012substratespecificityof pages 7-8).

Additional residues Asn-74 (N74) and Asn-78 (N78) contribute to the substrate binding pocket (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, monne2012substratespecificityof pages 7-8).

### 3.2 Gating and Transport Cycle

Transport follows a **"single binding center gated pore" model** (also described as an alternating-access mechanism) involving opening and closing of gates on the cytoplasmic and matrix sides to alternately expose the common substrate binding site (monne2012substratespecificityof pages 1-2). Three characteristic signature sequence motifs (PFDTMK, PTELVK, and PVDCIK) contain proline residues that kink the odd-numbered transmembrane helices (tessa2009identificationofnovel pages 5-6). A **salt-bridge network** formed by charged residues (D31-K131, K34-D231, K234-E128) closes the cavity on the matrix side and constitutes the matrix gate (tessa2009identificationofnovel pages 5-6, palmieri2013themitochondrialtransporter pages 3-6). Substrate binding to R179, as the rate-limiting step, triggers conformational changes that open the matrix gate, allowing substrate translocation (monne2012substratespecificityof pages 8-9).

The structural model of ORC1 was built based on the crystal structure of the bovine ADP/ATP carrier (tessa2009identificationofnovel pages 5-6, monne2012substratespecificityof pages 2-3).

## 4. Role in the Urea Cycle and Ornithine Metabolism

The urea cycle is a metabolic pathway that detoxifies nitrogen by converting ammonia into urea, operating across both the mitochondrial matrix and the cytoplasm of hepatocytes. SLC25A15/ORC1 provides the **essential transport link** between these two compartments by importing cytoplasmic ornithine into the mitochondrial matrix while simultaneously exporting citrulline to the cytoplasm (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, palmieri2020diseasescausedby pages 13-15, cunningham202020000picometersunder pages 4-5).

In the mitochondrial matrix, imported ornithine serves as a substrate for **ornithine transcarbamylase (OTC)**, which combines ornithine with carbamyl phosphate (produced by carbamoyl phosphate synthetase I) to generate citrulline (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11). The citrulline produced is then exported to the cytoplasm via ORC1, where **argininosuccinate synthase** reacts citrulline with ATP and aspartate to generate argininosuccinate, continuing the cytoplasmic portion of the urea cycle (cunningham202020000picometersunder pages 4-5).

Beyond the urea cycle, ORC1 also supports **arginine biosynthesis and polyamine synthesis**, as export of mitochondrial ornithine to the cytosol provides the substrate for ornithine decarboxylase, a key enzyme in polyamine production (mentel2021learningfromyeast pages 20-21, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9).

## 5. Subcellular Localization and Tissue Expression

ORC1 is an **integral membrane protein of the inner mitochondrial membrane** (tessa2009identificationofnovel pages 5-6, palmieri2013themitochondrialtransporter pages 3-6). It is expressed broadly across tissues, with highest expression levels reported in **liver, pancreas, lung, and kidney** (gutierrezaguilar2013physiologicalandpathological pages 3-4, ahmed2024theroleof pages 16-18). Expression in the liver is particularly important given that the urea cycle is principally operative in periportal hepatocytes (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9). Expression has also been noted in testes, small intestine, and other organs (cai2026argininetransportersin pages 10-12, gutierrezaguilar2013physiologicalandpathological pages 3-4).

## 6. Paralogues and Functional Redundancy

Three human mitochondrial carriers can transport ornithine:

- **ORC2/SLC25A2 (ORNT2)**: Shares 87% sequence identity with ORC1 but has **lower affinity** for ornithine and citrulline and **broader substrate specificity**, including the ability to transport histidine, homocitrulline, and D-isomers of amino acids (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9, arco2005newmitochondrialcarriers pages 10-11). ORC2 expression is consistently lower than ORC1 in all tissues examined (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9, gutierrezaguilar2013physiologicalandpathological pages 3-4). ORC2 originated through retrotransposition and orthologues are found only in mammalian genomes (arco2005newmitochondrialcarriers pages 10-11).

- **SLC25A29 (ORNT3)**: A related basic amino acid carrier that can rescue ornithine metabolism in fibroblasts from HHH syndrome patients, demonstrating compensatory capacity (camacho2009thehumanand pages 6-7, mentel2021learningfromyeast pages 21-22). ORNT3 shows higher expression in the central nervous system than in the liver, suggesting tissue-specific compensatory roles (camacho2009thehumanand pages 6-7).

The redundancy provided by ORC2 and SLC25A29 may explain the variable severity and relatively milder phenotypes of HHH syndrome compared to deficiencies in urea cycle enzymes themselves (mentel2021learningfromyeast pages 20-21, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9, arco2005newmitochondrialcarriers pages 10-11).

## 7. Disease Associations

### 7.1 HHH Syndrome (Hyperornithinemia-Hyperammonemia-Homocitrullinuria)

Loss-of-function mutations in SLC25A15 cause **HHH syndrome** (OMIM #238970), a rare autosomal recessive disorder of the urea cycle (palmieri2020diseasescausedby pages 13-15, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11). Over 100 patients have been identified worldwide, with major prevalence clusters in Canada, Italy, and Japan (palmieri2020diseasescausedby pages 13-15). The molecular pathogenesis proceeds through a defined cascade:

1. **Impaired ornithine transport** into mitochondria reduces the availability of ornithine for OTC in the matrix (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).
2. **Cytoplasmic ornithine accumulates** (hyperornithinemia) while mitochondrial ornithine is depleted (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).
3. **Urea cycle dysfunction** leads to ammonia accumulation (hyperammonemia) (palmieri2020diseasescausedby pages 13-15, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).
4. Accumulated carbamyl phosphate reacts with **lysine to form homocitrulline** (homocitrullinuria), a hallmark metabolite (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, tunalı2014anovelmutation pages 1-2).
5. High cytoplasmic ornithine **inhibits arginine-glycine amidotransferase (AGAT)**, causing secondary creatine deficiency, which compounds neurological vulnerability (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).
6. Excessive ornithine and homocitrulline cause **protein and lipid oxidation**, impairing brain oxidative phosphorylation and Krebs cycle function (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).

Clinical manifestations include acute episodes of vomiting, confusion, and coma; chronic features include developmental delay, intellectual disability, spastic paraplegia, cerebellar ataxia, seizures, and pyramidal dysfunction (palmieri2020diseasescausedby pages 13-15, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11). More than 35 disease-causing mutations have been identified (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11).

The following table summarizes the spectrum of known pathogenic mutations:

| Mutation | Type | Residual transport activity | Structural location | Population prevalence / recurrence | Functional/pathogenic note |
|---|---|---:|---|---|---|
| **F188del** | In-frame deletion | Defective; markedly reduced activity | Likely TM4 / pore region | ~30% of reported HHH patients; enriched in French-Canadian cases (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16) | One of the two most common HHH alleles; affects a residue lining the internal translocation pore, consistent with impaired substrate translocation (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) |
| **R179\*** (also reported as **R179X**) | Nonsense | Predicted null | Contact-point II / pore-facing region, near matrix gate | ~15% of reported HHH patients; recurrent in Japanese and Middle Eastern/Palestinian families (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, tessa2009identificationofnovel pages 3-4, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16, dweikat2022clinicalheterogeneityof pages 9-9) | Truncates ORC1; residue 179 is a key determinant of substrate recognition in wild-type ORC1, so loss is expected to abolish transport (monne2012substratespecificityof pages 1-2, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) |
| **M37R** | Missense | ~0% (virtually incapable of transport) | TM1 / matrix salt-bridge network region (H1) (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) | Novel/reported in HHH families; no major founder prevalence stated (tessa2009identificationofnovel pages 6-8) | Disrupts salt-bridge networks critical for carrier gating and strongly impairs transport of ornithine, arginine, lysine, and citrulline (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) |
| **L71Q** | Missense | Reduced; within reported mutant range of ~4–19% of wild type | TM2 / H2 helix package (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) | Reported in HHH families; no major founder prevalence stated (tessa2009identificationofnovel pages 6-8) | Hydrophilic substitution perturbs H2 helix packing and carrier structural integrity (tessa2009identificationofnovel pages 6-8) |
| **A15V** | Missense | Nearly abolished / dramatically inhibited | N-terminal region / early TM1 vicinity (tunalı2014anovelmutation pages 1-2) | Identified in a Turkish patient (tunalı2014anovelmutation pages 1-2, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16) | Functional assay showed near-complete loss of ornithine transport, supporting pathogenicity (tunalı2014anovelmutation pages 1-2) |
| **G27E** | Missense | Defective; exact % not stated | TM1 / pore-proximal region | Recurrent in Japanese patients; also reported in Palestinian families (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16, dweikat2022clinicalheterogeneityof pages 9-9) | Associated with decreased ornithine transport activity in liver mitochondria/ORC1 deficiency (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16, dweikat2022clinicalheterogeneityof pages 9-9) |
| **G216S** | Missense | Reduced; within reported mutant range of ~4–19% of wild type | Likely TM5 / pore-facing region (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) | Reported in HHH families (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 3-4) | Alters carrier structure/function and contributes to markedly reduced transport (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) |
| **T272I** | Missense | Reduced; within reported mutant range of ~4–19% of wild type | TM6 region (tessa2009identificationofnovel pages 6-8) | Reported in HHH families (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 3-4) | Causes steric interference with crucial intramolecular interactions required for catalytic function (tessa2009identificationofnovel pages 6-8) |
| **L283F** | Missense | Reduced; within reported mutant range of ~4–19% of wild type | TM6 region / late C-terminal helix (tessa2009identificationofnovel pages 6-8) | Reported in HHH families (tessa2009identificationofnovel pages 6-8) | Bulky substitution likely perturbs helix packing and transport pathway geometry (tessa2009identificationofnovel pages 6-8) |
| **E180K** | Missense | Pathogenic; exact residual % not stated | Contact-point II substrate-binding site near residue R179 (monne2012substratespecificityof pages 1-2, cunningham202020000picometersunder pages 4-5, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) | Reported missense HHH allele (cunningham202020000picometersunder pages 4-5) | E180 is a key substrate-binding residue in wild-type ORC1; substitution is expected to disrupt ligand recognition and translocation (monne2012substratespecificityof pages 1-2, martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11) |
| **F188D** | Missense | Pathogenic; exact residual % not stated | Around residue 188 in pore/TM4 region (cunningham202020000picometersunder pages 4-5) | Reported missense HHH allele (cunningham202020000picometersunder pages 4-5) | Missense change near the recurrent F188 hotspot; associated with HHH syndrome and impaired urea-cycle transport (cunningham202020000picometersunder pages 4-5) |
| **P126R** | Missense | Defective; exact % not stated | Likely TM3 / central cavity region (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16) | Reported in affected families (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16) | Likely disrupts conserved carrier helix geometry important for alternating-access transport (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16, tessa2009identificationofnovel pages 5-6) |
| **R275X** | Nonsense | Predicted null | TM6 / contact-point III vicinity; R275 is mechanistically important in wild type (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, monne2012substratespecificityof pages 7-8) | Reported in affected families (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16) | Premature stop removes C-terminal region; wild-type Arg275 contributes to substrate-triggered conformational change (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, monne2012substratespecificityof pages 7-8) |
| **T32R** | Missense | Defective; exact % not stated | TM1 / matrix-gate neighborhood (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16, tessa2009identificationofnovel pages 5-6) | Reported in affected families (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16) | Likely perturbs local charge environment near matrix-side gating residues (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16, tessa2009identificationofnovel pages 5-6) |
| **p.K245X** | Nonsense | Predicted null | C-terminal half / likely TM5-TM6 region (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) | Identified among 13 mutations in HHH families (tessa2009identificationofnovel pages 5-6, tessa2009identificationofnovel pages 3-4) | Premature truncation expected to abolish functional carrier assembly/transport (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) |
| **p.S175fsX192** | Frameshift | Predicted null | Mid-protein / around TM4 entry (tessa2009identificationofnovel pages 5-6) | Reported in HHH families (tessa2009identificationofnovel pages 5-6) | Frameshift with premature termination; expected severe loss of ORC1 function (tessa2009identificationofnovel pages 5-6) |
| **c.552-555delTTTC (p.Phe185SerfsTer8)** | Frameshift deletion | Predicted null | Around residue 185 / pore hotspot region (dweikat2022clinicalheterogeneityof pages 9-9) | Novel homozygous variant in 9 Palestinian patients (dweikat2022clinicalheterogeneityof pages 9-9) | Expected nonsense-mediated decay or severely truncated protein; expands the HHH molecular spectrum (dweikat2022clinicalheterogeneityof pages 9-9) |
| **c.446delG (p.Ser149ThrfsTer45)** | Frameshift deletion | Predicted null | Mid-protein / central carrier region (dweikat2022clinicalheterogeneityof pages 9-9) | Recurrent homozygous variant in 4 Palestinian patients (dweikat2022clinicalheterogeneityof pages 9-9) | Frameshift expected to abrogate transporter function; associated with marked clinical heterogeneity despite shared genotype (dweikat2022clinicalheterogeneityof pages 9-9) |
| **Overall missense class** | Missense | Typically ~4–19% of wild-type transport, except severe alleles such as M37R (~0%) and A15V (near-abolished) (tessa2009identificationofnovel pages 5-6, tessa2009identificationofnovel pages 1-2, tunalı2014anovelmutation pages 1-2) | Frequently in transmembrane helices H1–H6 and residues protruding into the internal pore (tessa2009identificationofnovel pages 6-8, tessa2009identificationofnovel pages 5-6) | No clear genotype-phenotype correlation overall (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, tessa2009identificationofnovel pages 1-2) | Many pathogenic residues cluster in the translocation pore or gating networks, interfering with substrate binding, helix movement, or conformational switching (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11, tessa2009identificationofnovel pages 6-8, monne2012substratespecificityof pages 7-8) |


*Table: This table summarizes representative disease-causing SLC25A15 variants reported in hyperornithinemia-hyperammonemia-homocitrullinuria syndrome, including mutation class, functional impact, structural context, and recurrence. It is useful for connecting genotype to transporter mechanism and clinical interpretation.*

### 7.2 Cancer Associations

Emerging evidence implicates SLC25A15 in cancer biology in a context-dependent manner:

- **Hepatocellular carcinoma (HCC)**: ORC1 is downregulated in HCC and functions as a **tumor suppressor**. Its downregulation leads to ammonia accumulation, which activates mTORC1, promotes glutamine uptake, and redirects glutamine metabolism toward reductive carboxylation and de novo lipogenesis, thereby driving HCC progression. ORC1 downregulation also confers resistance to anti-PD-L1 therapy (ahmed2024theroleof pages 16-18).

- **Diffuse large B-cell lymphoma (DLBCL)**: In contrast, SLC25A15 is **highly expressed** in DLBCL where it serves as a survival factor. It supports purine nucleotide homeostasis and genomic stability; its downregulation leads to impaired purine nucleotide synthesis, dGTP depletion, and DNA damage, identifying it as a potential metabolic vulnerability and therapeutic target (su2026pufabiflavone pages 12-14, su2026pufabiflavone pages 7-12, su2026pufabiflavone pages 1-2).

OpenTargets disease-target association analysis confirms strong associations of SLC25A15 with ornithine translocase deficiency (score 0.85) and HHH syndrome (score 0.84), as well as weaker associations with inflammatory bowel disease and autoimmune CNS disorders (OpenTargets Search: -SLC25A15).

## 8. Summary

SLC25A15/ORC1 is the principal human mitochondrial ornithine transporter, embedded in the inner mitochondrial membrane, where it catalyzes the electroneutral 1:1 antiport exchange of cytoplasmic L-ornithine for mitochondrial L-citrulline plus a proton. Its primary biological role is to bridge the mitochondrial and cytoplasmic reactions of the urea cycle, ensuring both ornithine availability for OTC in the matrix and citrulline export for argininosuccinate synthase in the cytosol. The protein adopts the canonical six-transmembrane-helix architecture of the SLC25 family, with substrate binding determined by key residues at three contact points (E77, R179/E180, R275). Loss-of-function mutations cause HHH syndrome, a rare urea cycle disorder, while emerging evidence points to context-dependent roles in cancer metabolism. Paralogous carriers ORC2 and SLC25A29 provide partial functional redundancy that may modulate disease severity.

References

1. (palmieri2013themitochondrialtransporter pages 3-6): Ferdinando Palmieri. The mitochondrial transporter family slc25: identification, properties and physiopathology. Molecular aspects of medicine, 34 2-3:465-84, Apr 2013. URL: https://doi.org/10.1016/j.mam.2012.05.005, doi:10.1016/j.mam.2012.05.005. This article has 740 citations and is from a highest quality peer-reviewed journal.

2. (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 9-11): Diego Martinelli, Daria Diodato, Emanuela Ponzi, Magnus Monné, Sara Boenzi, Enrico Bertini, Giuseppe Fiermonte, and Carlo Dionisi-Vici. The hyperornithinemia–hyperammonemia-homocitrullinuria syndrome. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0242-9, doi:10.1186/s13023-015-0242-9. This article has 121 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: -SLC25A15): Open Targets Query (-SLC25A15, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (gutierrezaguilar2013physiologicalandpathological pages 3-4): Manuel Gutiérrez-Aguilar and Christopher P. Baines. Physiological and pathological roles of mitochondrial slc25 carriers. The Biochemical journal, 454 3:371-86, Sep 2013. URL: https://doi.org/10.1042/bj20121753, doi:10.1042/bj20121753. This article has 178 citations.

5. (gao2024cancertherapeuticpotential pages 6-7): Renzhuo Gao, Dan Zhou, Xingpeng Qiu, Jiayi Zhang, Daya Luo, Xiaohong Yang, Caiyun Qian, and Zhuoqi Liu. Cancer therapeutic potential and prognostic value of the slc25 mitochondrial carrier family: a review. Cancer Control : Journal of the Moffitt Cancer Center, Jan 2024. URL: https://doi.org/10.1177/10732748241287905, doi:10.1177/10732748241287905. This article has 12 citations.

6. (tessa2009identificationofnovel pages 3-4): Alessandra Tessa, Giuseppe Fiermonte, Carlo Dionisi-Vici, Eleonora Paradies, Matthias R. Baumgartner, Yin-Hsiu Chien, Carmela Loguercio, Helene Ogier de Baulny, Marie-Cecile Nassogne, Manuel Schiff, Federica Deodato, Giancarlo Parenti, S. Lane Rutledge, M. Antonia Vilaseca, Mariarosa A.B. Melone, Gioacchino Scarano, Luiz Aldamiz-Echevarría, Guy Besley, John Walter, Eugenia Martinez-Hernandez, Jose M. Hernandez, Ciro L. Pierri, Ferdinando Palmieri, and Filippo M. Santorelli. Identification of novel mutations in the slc25a15 gene in hyperornithinemia‐hyperammonemia‐homocitrullinuria (hhh) syndrome: a clinical, molecular, and functional study. Human Mutation, 30:741-748, May 2009. URL: https://doi.org/10.1002/humu.20930, doi:10.1002/humu.20930. This article has 88 citations and is from a domain leading peer-reviewed journal.

7. (tessa2009identificationofnovel pages 5-6): Alessandra Tessa, Giuseppe Fiermonte, Carlo Dionisi-Vici, Eleonora Paradies, Matthias R. Baumgartner, Yin-Hsiu Chien, Carmela Loguercio, Helene Ogier de Baulny, Marie-Cecile Nassogne, Manuel Schiff, Federica Deodato, Giancarlo Parenti, S. Lane Rutledge, M. Antonia Vilaseca, Mariarosa A.B. Melone, Gioacchino Scarano, Luiz Aldamiz-Echevarría, Guy Besley, John Walter, Eugenia Martinez-Hernandez, Jose M. Hernandez, Ciro L. Pierri, Ferdinando Palmieri, and Filippo M. Santorelli. Identification of novel mutations in the slc25a15 gene in hyperornithinemia‐hyperammonemia‐homocitrullinuria (hhh) syndrome: a clinical, molecular, and functional study. Human Mutation, 30:741-748, May 2009. URL: https://doi.org/10.1002/humu.20930, doi:10.1002/humu.20930. This article has 88 citations and is from a domain leading peer-reviewed journal.

8. (monne2012substratespecificityof pages 1-2): Magnus Monné, Daniela Valeria Miniero, Lucia Daddabbo, Alan J. Robinson, Edmund R.S. Kunji, and Ferdinando Palmieri. Substrate specificity of the two mitochondrial ornithine carriers can be swapped by single mutation in substrate binding site. Journal of Biological Chemistry, 287:7925-7934, Mar 2012. URL: https://doi.org/10.1074/jbc.m111.324855, doi:10.1074/jbc.m111.324855. This article has 65 citations and is from a domain leading peer-reviewed journal.

9. (monne2012substratespecificityof pages 3-4): Magnus Monné, Daniela Valeria Miniero, Lucia Daddabbo, Alan J. Robinson, Edmund R.S. Kunji, and Ferdinando Palmieri. Substrate specificity of the two mitochondrial ornithine carriers can be swapped by single mutation in substrate binding site. Journal of Biological Chemistry, 287:7925-7934, Mar 2012. URL: https://doi.org/10.1074/jbc.m111.324855, doi:10.1074/jbc.m111.324855. This article has 65 citations and is from a domain leading peer-reviewed journal.

10. (palmieri2020diseasescausedby pages 13-15): Ferdinando Palmieri, Pasquale Scarcia, and Magnus Monné. Diseases caused by mutations in mitochondrial carrier genes slc25: a review. Biomolecules, 10:655, Apr 2020. URL: https://doi.org/10.3390/biom10040655, doi:10.3390/biom10040655. This article has 135 citations.

11. (ahmed2024theroleof pages 16-18): Amer Ahmed, Giorgia Natalia Iaconisi, Daria Di Molfetta, Vincenzo Coppola, Antonello Caponio, Ansu Singh, Aasia Bibi, Loredana Capobianco, Luigi Palmieri, Vincenza Dolce, and Giuseppe Fiermonte. The role of mitochondrial solute carriers slc25 in cancer metabolic reprogramming: current insights and future perspectives. International Journal of Molecular Sciences, 26:92, Dec 2024. URL: https://doi.org/10.3390/ijms26010092, doi:10.3390/ijms26010092. This article has 18 citations.

12. (monne2012substratespecificityof pages 7-8): Magnus Monné, Daniela Valeria Miniero, Lucia Daddabbo, Alan J. Robinson, Edmund R.S. Kunji, and Ferdinando Palmieri. Substrate specificity of the two mitochondrial ornithine carriers can be swapped by single mutation in substrate binding site. Journal of Biological Chemistry, 287:7925-7934, Mar 2012. URL: https://doi.org/10.1074/jbc.m111.324855, doi:10.1074/jbc.m111.324855. This article has 65 citations and is from a domain leading peer-reviewed journal.

13. (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 8-9): Diego Martinelli, Daria Diodato, Emanuela Ponzi, Magnus Monné, Sara Boenzi, Enrico Bertini, Giuseppe Fiermonte, and Carlo Dionisi-Vici. The hyperornithinemia–hyperammonemia-homocitrullinuria syndrome. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0242-9, doi:10.1186/s13023-015-0242-9. This article has 121 citations and is from a peer-reviewed journal.

14. (camacho2009thehumanand pages 6-7): Josée A Camacho and Natalia Rioseco-Camacho. The human and mouse slc25a29 mitochondrial transporters rescue the deficient ornithine metabolism in fibroblasts of patients with the hyperornithinemia-hyperammonemia-homocitrullinuria (hhh) syndrome. Jul 2009. URL: https://doi.org/10.1203/pdr.0b013e3181a283c1, doi:10.1203/pdr.0b013e3181a283c1. This article has 41 citations and is from a domain leading peer-reviewed journal.

15. (cunningham202020000picometersunder pages 4-5): Corey N Cunningham and Jared Rutter. 20,000 picometers under the omm: diving into the vastness of mitochondrial metabolite transport. EMBO reports, Apr 2020. URL: https://doi.org/10.15252/embr.202050071, doi:10.15252/embr.202050071. This article has 48 citations and is from a highest quality peer-reviewed journal.

16. (mentel2021learningfromyeast pages 20-21): Marek Mentel, Petra Chovančíková, Igor Zeman, and Peter Polčic. Learning from yeast about mitochondrial carriers. Microorganisms, 9:2044, Sep 2021. URL: https://doi.org/10.3390/microorganisms9102044, doi:10.3390/microorganisms9102044. This article has 7 citations.

17. (mentel2021learningfromyeast pages 21-22): Marek Mentel, Petra Chovančíková, Igor Zeman, and Peter Polčic. Learning from yeast about mitochondrial carriers. Microorganisms, 9:2044, Sep 2021. URL: https://doi.org/10.3390/microorganisms9102044, doi:10.3390/microorganisms9102044. This article has 7 citations.

18. (tessa2009identificationofnovel pages 1-2): Alessandra Tessa, Giuseppe Fiermonte, Carlo Dionisi-Vici, Eleonora Paradies, Matthias R. Baumgartner, Yin-Hsiu Chien, Carmela Loguercio, Helene Ogier de Baulny, Marie-Cecile Nassogne, Manuel Schiff, Federica Deodato, Giancarlo Parenti, S. Lane Rutledge, M. Antonia Vilaseca, Mariarosa A.B. Melone, Gioacchino Scarano, Luiz Aldamiz-Echevarría, Guy Besley, John Walter, Eugenia Martinez-Hernandez, Jose M. Hernandez, Ciro L. Pierri, Ferdinando Palmieri, and Filippo M. Santorelli. Identification of novel mutations in the slc25a15 gene in hyperornithinemia‐hyperammonemia‐homocitrullinuria (hhh) syndrome: a clinical, molecular, and functional study. Human Mutation, 30:741-748, May 2009. URL: https://doi.org/10.1002/humu.20930, doi:10.1002/humu.20930. This article has 88 citations and is from a domain leading peer-reviewed journal.

19. (monne2012substratespecificityof pages 2-3): Magnus Monné, Daniela Valeria Miniero, Lucia Daddabbo, Alan J. Robinson, Edmund R.S. Kunji, and Ferdinando Palmieri. Substrate specificity of the two mitochondrial ornithine carriers can be swapped by single mutation in substrate binding site. Journal of Biological Chemistry, 287:7925-7934, Mar 2012. URL: https://doi.org/10.1074/jbc.m111.324855, doi:10.1074/jbc.m111.324855. This article has 65 citations and is from a domain leading peer-reviewed journal.

20. (monne2012substratespecificityof pages 8-9): Magnus Monné, Daniela Valeria Miniero, Lucia Daddabbo, Alan J. Robinson, Edmund R.S. Kunji, and Ferdinando Palmieri. Substrate specificity of the two mitochondrial ornithine carriers can be swapped by single mutation in substrate binding site. Journal of Biological Chemistry, 287:7925-7934, Mar 2012. URL: https://doi.org/10.1074/jbc.m111.324855, doi:10.1074/jbc.m111.324855. This article has 65 citations and is from a domain leading peer-reviewed journal.

21. (cai2026argininetransportersin pages 10-12): Xichen Cai, Li Shang, Yue-Qin Li, Ya Cao, and Feng Shi. Arginine transporters in human cancers: emerging mechanisms and clinical implications. Biomolecules, 16:132, Jan 2026. URL: https://doi.org/10.3390/biom16010132, doi:10.3390/biom16010132. This article has 2 citations.

22. (arco2005newmitochondrialcarriers pages 10-11): A. del Arco and J. Satrústegui. New mitochondrial carriers: an overview. Cellular and Molecular Life Sciences CMLS, 62:2204-2227, Aug 2005. URL: https://doi.org/10.1007/s00018-005-5197-x, doi:10.1007/s00018-005-5197-x. This article has 114 citations.

23. (tunalı2014anovelmutation pages 1-2): Nagehan Ersoy Tunalı, Carlo M.T. Marobbio, N. Ozan Tiryakioğlu, Giuseppe Punzi, Seha K. Saygılı, Hasan Önal, and Ferdinando Palmieri. A novel mutation in the slc25a15 gene in a turkish patient with hhh syndrome: functional analysis of the mutant protein. Molecular Genetics and Metabolism, 112(1):25-29, May 2014. URL: https://doi.org/10.1016/j.ymgme.2014.03.002, doi:10.1016/j.ymgme.2014.03.002. This article has 34 citations and is from a peer-reviewed journal.

24. (martinelli2015thehyperornithinemia–hyperammonemiahomocitrullinuriasyndrome pages 16-16): Diego Martinelli, Daria Diodato, Emanuela Ponzi, Magnus Monné, Sara Boenzi, Enrico Bertini, Giuseppe Fiermonte, and Carlo Dionisi-Vici. The hyperornithinemia–hyperammonemia-homocitrullinuria syndrome. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0242-9, doi:10.1186/s13023-015-0242-9. This article has 121 citations and is from a peer-reviewed journal.

25. (dweikat2022clinicalheterogeneityof pages 9-9): Imad Dweikat and Reham Khalaf-Nazzal. Clinical heterogeneity of hyperornithinemia-hyperammonemia-homocitrullinuria syndrome in thirteen palestinian patients and report of a novel variant in the slc25a15 gene. Frontiers in Genetics, Nov 2022. URL: https://doi.org/10.3389/fgene.2022.1004598, doi:10.3389/fgene.2022.1004598. This article has 7 citations and is from a peer-reviewed journal.

26. (tessa2009identificationofnovel pages 6-8): Alessandra Tessa, Giuseppe Fiermonte, Carlo Dionisi-Vici, Eleonora Paradies, Matthias R. Baumgartner, Yin-Hsiu Chien, Carmela Loguercio, Helene Ogier de Baulny, Marie-Cecile Nassogne, Manuel Schiff, Federica Deodato, Giancarlo Parenti, S. Lane Rutledge, M. Antonia Vilaseca, Mariarosa A.B. Melone, Gioacchino Scarano, Luiz Aldamiz-Echevarría, Guy Besley, John Walter, Eugenia Martinez-Hernandez, Jose M. Hernandez, Ciro L. Pierri, Ferdinando Palmieri, and Filippo M. Santorelli. Identification of novel mutations in the slc25a15 gene in hyperornithinemia‐hyperammonemia‐homocitrullinuria (hhh) syndrome: a clinical, molecular, and functional study. Human Mutation, 30:741-748, May 2009. URL: https://doi.org/10.1002/humu.20930, doi:10.1002/humu.20930. This article has 88 citations and is from a domain leading peer-reviewed journal.

27. (su2026pufabiflavone pages 12-14): Chang Su, Guige Lu, Lijia Ou, Liang Liang, Caiqin Wang, Yizi He, Ruolan Zeng, Yajun Li, Hui Zhou, and Ling Xiao. Puf, a biflavone monomer, triggers dna damage through slc25a15 downregulation and purine metabolic suppression in dlbcl. Journal of Translational Medicine, Feb 2026. URL: https://doi.org/10.1186/s12967-026-07797-9, doi:10.1186/s12967-026-07797-9. This article has 0 citations and is from a peer-reviewed journal.

28. (su2026pufabiflavone pages 7-12): Chang Su, Guige Lu, Lijia Ou, Liang Liang, Caiqin Wang, Yizi He, Ruolan Zeng, Yajun Li, Hui Zhou, and Ling Xiao. Puf, a biflavone monomer, triggers dna damage through slc25a15 downregulation and purine metabolic suppression in dlbcl. Journal of Translational Medicine, Feb 2026. URL: https://doi.org/10.1186/s12967-026-07797-9, doi:10.1186/s12967-026-07797-9. This article has 0 citations and is from a peer-reviewed journal.

29. (su2026pufabiflavone pages 1-2): Chang Su, Guige Lu, Lijia Ou, Liang Liang, Caiqin Wang, Yizi He, Ruolan Zeng, Yajun Li, Hui Zhou, and Ling Xiao. Puf, a biflavone monomer, triggers dna damage through slc25a15 downregulation and purine metabolic suppression in dlbcl. Journal of Translational Medicine, Feb 2026. URL: https://doi.org/10.1186/s12967-026-07797-9, doi:10.1186/s12967-026-07797-9. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](SLC25A15-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](SLC25A15-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. palmieri2013themitochondrialtransporter pages 3-6
2. gao2024cancertherapeuticpotential pages 6-7
3. monne2012substratespecificityof pages 1-2
4. mentel2021learningfromyeast pages 20-21
5. monne2012substratespecificityof pages 3-4
6. tessa2009identificationofnovel pages 5-6
7. monne2012substratespecificityof pages 8-9
8. arco2005newmitochondrialcarriers pages 10-11
9. camacho2009thehumanand pages 6-7
10. palmieri2020diseasescausedby pages 13-15
11. tessa2009identificationofnovel pages 6-8
12. tunalı2014anovelmutation pages 1-2
13. dweikat2022clinicalheterogeneityof pages 9-9
14. ahmed2024theroleof pages 16-18
15. gutierrezaguilar2013physiologicalandpathological pages 3-4
16. tessa2009identificationofnovel pages 3-4
17. monne2012substratespecificityof pages 7-8
18. mentel2021learningfromyeast pages 21-22
19. tessa2009identificationofnovel pages 1-2
20. monne2012substratespecificityof pages 2-3
21. cai2026argininetransportersin pages 10-12
22. su2026pufabiflavone pages 12-14
23. su2026pufabiflavone pages 7-12
24. su2026pufabiflavone pages 1-2
25. https://doi.org/10.1016/j.mam.2012.05.005,
26. https://doi.org/10.1186/s13023-015-0242-9,
27. https://doi.org/10.1042/bj20121753,
28. https://doi.org/10.1177/10732748241287905,
29. https://doi.org/10.1002/humu.20930,
30. https://doi.org/10.1074/jbc.m111.324855,
31. https://doi.org/10.3390/biom10040655,
32. https://doi.org/10.3390/ijms26010092,
33. https://doi.org/10.1203/pdr.0b013e3181a283c1,
34. https://doi.org/10.15252/embr.202050071,
35. https://doi.org/10.3390/microorganisms9102044,
36. https://doi.org/10.3390/biom16010132,
37. https://doi.org/10.1007/s00018-005-5197-x,
38. https://doi.org/10.1016/j.ymgme.2014.03.002,
39. https://doi.org/10.3389/fgene.2022.1004598,
40. https://doi.org/10.1186/s12967-026-07797-9,