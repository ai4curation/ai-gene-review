---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T19:57:23.982476'
end_time: '2026-09-25T20:08:32.816660'
duration_seconds: 668.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ABCD1
  gene_symbol: ABCD1
  uniprot_accession: P33897
  protein_description: 'RecName: Full=ATP-binding cassette sub-family D member 1 {ECO:0000312|HGNC:HGNC:61};
    EC=3.1.2.- {ECO:0000269|PubMed:29397936, ECO:0000269|PubMed:33500543}; EC=7.6.2.-
    {ECO:0000269|PubMed:11248239, ECO:0000269|PubMed:29397936, ECO:0000269|PubMed:33500543,
    ECO:0000305|PubMed:16946495, ECO:0000305|PubMed:23671276}; AltName: Full=Adrenoleukodystrophy
    protein {ECO:0000303|PubMed:10777694}; Short=ALDP {ECO:0000303|PubMed:16946495,
    ECO:0000303|PubMed:18757502};'
  gene_info: Name=ABCD1 {ECO:0000312|HGNC:HGNC:61}; Synonyms=ALD;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the ABC transporter superfamily. ABCD family.
  protein_domains: AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf.
    (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS.
    (IPR017871)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ABCD1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P33897
- **Protein Description:** RecName: Full=ATP-binding cassette sub-family D member 1 {ECO:0000312|HGNC:HGNC:61}; EC=3.1.2.- {ECO:0000269|PubMed:29397936, ECO:0000269|PubMed:33500543}; EC=7.6.2.- {ECO:0000269|PubMed:11248239, ECO:0000269|PubMed:29397936, ECO:0000269|PubMed:33500543, ECO:0000305|PubMed:16946495, ECO:0000305|PubMed:23671276}; AltName: Full=Adrenoleukodystrophy protein {ECO:0000303|PubMed:10777694}; Short=ALDP {ECO:0000303|PubMed:16946495, ECO:0000303|PubMed:18757502};
- **Gene Information:** Name=ABCD1 {ECO:0000312|HGNC:HGNC:61}; Synonyms=ALD;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the ABC transporter superfamily. ABCD family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf. (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ABCD1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ABCD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ABCD1** (gene ID: ABCD1, UniProt: P33897) in human.

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
- **UniProt Accession:** P33897
- **Protein Description:** RecName: Full=ATP-binding cassette sub-family D member 1 {ECO:0000312|HGNC:HGNC:61}; EC=3.1.2.- {ECO:0000269|PubMed:29397936, ECO:0000269|PubMed:33500543}; EC=7.6.2.- {ECO:0000269|PubMed:11248239, ECO:0000269|PubMed:29397936, ECO:0000269|PubMed:33500543, ECO:0000305|PubMed:16946495, ECO:0000305|PubMed:23671276}; AltName: Full=Adrenoleukodystrophy protein {ECO:0000303|PubMed:10777694}; Short=ALDP {ECO:0000303|PubMed:16946495, ECO:0000303|PubMed:18757502};
- **Gene Information:** Name=ABCD1 {ECO:0000312|HGNC:HGNC:61}; Synonyms=ALD;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the ABC transporter superfamily. ABCD family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf. (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ABCD1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ABCD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ABCD1** (gene ID: ABCD1, UniProt: P33897) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human **ABCD1 / ALDP (UniProt P33897)**: functional-annotation research report

## Executive conclusion

The target identity is verified. Human **ABCD1** (approved name *ATP-binding cassette subfamily D member 1*; also **ALD**; protein **ALDP**) corresponds to the supplied human UniProt entry **P33897**, not to a similarly named protein from another organism. Open Targets identifies the human gene as **ENSG00000101986**, and modern structural studies explicitly identify P33897 as human ABCD1/ALDP. Its reported ABCD-family membership, transmembrane ABC domain, and AAA+/nucleotide-binding domain agree with the supplied annotation. No conflicting same-symbol target was found. (OpenTargets Search: X-linked adrenoleukodystrophy-ABCD1, xiong2023structuralinsightsinto pages 1-2)

**Primary function:** ABCD1 is an ATP-powered importer in the **peroxisomal membrane**. Its best-established physiological loading substrates are CoA esters of saturated and monounsaturated very-long-chain fatty acids (VLCFAs), notably **C22:0-, C24:0-, C26:0- and C26:1-CoA**. It transfers these substrates—or products produced from them— from the cytosolic side toward the peroxisomal matrix, thereby supplying peroxisomal β-oxidation. Loss of ABCD1 causes X-linked adrenoleukodystrophy (X-ALD) by reducing VLCFA β-oxidation and accumulating VLCFAs in acyl-CoA and complex-lipid pools. (chen2022structuralbasisof pages 1-2, jia2022structuralandfunctional pages 3-4, bougneres2025revisitingthepathogenesis pages 36-38)

| Feature | Best-supported conclusion | Experimental basis | Key source/date |
|---|---|---|---|
| Identity | **Verified target:** human ABCD1, also called adrenoleukodystrophy protein (ALDP), UniProt **P33897**; not a similarly named non-human protein. It is an ABC transporter subfamily-D member linked causally to X-linked adrenoleukodystrophy (X-ALD). | Human protein purification and cryo-EM studies explicitly identify ABCD1/ALDP and P33897; human genetic evidence strongly associates ABCD1 loss of function with X-ALD. | Xiong et al., February 2023; Open Targets record (xiong2023structuralinsightsinto pages 1-2, OpenTargets Search: X-linked adrenoleukodystrophy-ABCD1) |
| Localization and topology | **Established:** an integral **peroxisomal membrane** half-transporter. Each 745-aa protomer has six transmembrane helices followed by a cytosolic nucleotide-binding/AAA+-ATPase domain; inward-facing states open to the cytosol and outward-facing states open to the peroxisomal lumen. | Topology experiments place the ATP-binding region on the cytosolic face; multiple cryo-EM structures directly resolve six helices per protomer and alternating cytosolic- and lumen-facing conformations. | Wanders et al., February 2007; Jia et al., November 2022; Xiong et al., February 2023 (wanders2007theperoxisomalabc pages 4-6, jia2022structuralandfunctional pages 1-3, xiong2023structuralinsightsinto pages 1-2) |
| Oligomeric state | **Best supported:** ABCD1 functions predominantly as a **homodimer**, with two half-transporters supplying the paired transmembrane and nucleotide-binding domains. Heterodimerization with other ABCD proteins has been reported, but its physiological importance is less certain. | Cryo-EM consistently resolves symmetric/domain-swapped ABCD1 homodimers; co-immunoprecipitation and FRET support homodimerization, whereas two-hybrid studies also permit heteromeric interactions. | Le et al., January 2022; Jia et al., November 2022 (le2022structuresofthe pages 1-2, wright2022expressionandpurification pages 48-52, jia2022structuralandfunctional pages 1-3) |
| Primary substrates and specificity | **Established:** ABCD1 recognizes CoA-activated saturated and monounsaturated very-long-chain fatty acids, especially **C22:0-, C24:0-, C26:0- and C26:1-CoA**. C22:0-, C24:0- and C26:0-CoA stimulate ATPase activity; acetyl-CoA does not. Specificity overlaps with ABCD2/3 but favors saturated and monounsaturated VLCFA-CoAs. | Purified-protein ATPase assays, cellular transport assays and substrate-bound cryo-EM structures. One study reported approximately 2 μM EC50 and approximately 200 mol Pi·min⁻¹·mol protein⁻¹ for C22:0-, C24:0- and C26:0-CoA; another reported an apparent C22:0-CoA Km of approximately 0.17 μM. | Chen et al., June 2022; Jia et al., November 2022 (chen2022structuralbasisof pages 1-2, jia2022structuralandfunctional pages 3-4, jia2022structuralandfunctional pages 1-3) |
| Direction and energy coupling | **Established:** ABCD1 mediates ATP-dependent import from the **cytosolic leaflet toward the peroxisomal matrix**, enabling peroxisomal β-oxidation. Substrate binding stimulates ATP hydrolysis, and ATP-driven nucleotide-binding-domain closure switches the transporter to a lumen-open state. Exact ATP/substrate transport stoichiometry remains unresolved. | ATPase inhibition and mutation studies plus inward- and outward-facing cryo-EM structures. Reported ATP Km values vary with preparation; one lipid-environment study found approximately 0.3 mM, while an N-terminally truncated construct gave 585 ± 55 μM. | Le et al., January 2022; Xiong et al., February 2023 (le2022structuresofthe pages 1-2, xiong2023structuralinsightsinto pages 1-2) |
| Structural mechanism and key residues | Two acyl-CoA molecules can bind the dimer. Their CoA headgroups occupy hydrophilic transmembrane cavities while hydrophobic acyl chains extend across the cavity or into the bilayer. **W339** is central to substrate binding and substrate-stimulated ATPase activity; M335, R401, S404, S226, L230, L249 and F252 also contact C26:0-CoA. The C-terminal coiled coil restrains ATPase activity. | Substrate-bound and nucleotide-bound cryo-EM structures, mutagenesis and ATPase assays; ATP closes the nucleotide-binding domains and opens a matrix-facing exit. | Chen et al., June 2022; Xiong et al., February 2023 (chen2022structuralbasisof pages 1-2, xiong2021atpandsubstrate pages 4-6, xiong2023structuralinsightsinto pages 1-2) |
| Transported chemical form and thioesterase question | **Unresolved:** acyl-CoA is clearly the cytosolic recognition substrate, but it is not conclusively established whether intact VLCFA-CoA crosses the membrane or whether ABCD1 hydrolyzes it and translocates free fatty acid and/or CoA. Intrinsic acyl-CoA thioesterase activity has been reported, yet ABCD1 lacks a recognizable conventional thioesterase domain and current structures do not define its catalytic chemistry. | Structural studies visualize bound acyl-CoA but generally infer transport from ATPase stimulation rather than directly tracing products across a membrane. Cleavage/re-esterification models rely partly on yeast and plant ABCD homologues. | Le et al., January 2022; Kawaguchi and Imanaka, August 2022; pathway synthesis (le2022structuresofthe pages 1-2, wright2022expressionandpurification pages 61-66) |
| Biochemical pathway consequence of loss | **Established core defect:** impaired import and peroxisomal β-oxidation produce accumulation of saturated VLCFAs—especially C24:0 and C26:0/C26:1—in acyl-CoAs and complex lipids. Patient fibroblast β-oxidation has been reported at approximately 30% of normal. Downstream membrane injury, oxidative stress, mitochondrial dysfunction and neuroinflammation are supported, but their causal ordering and the trigger for cerebral inflammation remain uncertain. | Patient biochemical studies, lipid measurements, ABCD1-deficient models and clinical tissue analyses; one review reports approximately 39-fold increased C26:0 in cerebral-ALD brain. | Parasar et al., June 2024; Zuo and Chen, November 2024 (parasar2024pathophysiologyofxlinked pages 3-5, bougneres2025revisitingthepathogenesis pages 36-38, zuo2024fromgeneto pages 1-2) |
| 2023–2024 research developments | The 2023 multi-state cryo-EM study refined the alternating-access mechanism and identified W339 and the inhibitory C-terminal coiled coil. In 2024, disease studies strengthened links among excess VLCFAs, redox-dependent DRP1 activation, mitochondrial fragmentation and axonal injury; peroxisomal-defect models also revealed disease-associated microglial transcriptional states. These downstream findings are mechanistically suggestive rather than proof of what initiates cerebral ALD. | High-resolution cryo-EM, patient fibroblasts, quantitative electron microscopy, C. elegans intervention studies and microglial RNA sequencing. | Xiong et al., February 2023; Raas et al., April 2023; Launay et al., May 2024 (xiong2023structuralinsightsinto pages 1-2, parasar2024pathophysiologyofxlinked pages 3-5) |
| Clinical implementation | **Current application:** C26:0-lysophosphatidylcholine dried-blood-spot newborn screening followed by ABCD1 sequencing enables presymptomatic MRI/adrenal surveillance. Early cerebral ALD can be treated with allogeneic HSCT or autologous CD34+ cells carrying lentiviral **ABCD1** (elivaldogene autotemcel/Skysona); the latter restores ABCD1-expressing hematopoietic descendants but does not correct every ABCD1-deficient tissue or reliably treat adrenal insufficiency/established myelopathy. Serious risks include myeloablative toxicity and insertional hematologic malignancy, so long-term monitoring and individualized benefit–risk assessment are essential. | By 2024, approximately 44 US states plus Washington, DC screened newborns. Phase 2/3 and phase 3 studies enrolled 32 and 35 participants, respectively; post-treatment myelodysplastic syndrome was associated with integrations near MECOM/PRDM16 in reported cases. | Aerts-Kaya and van Til, October 2023; Zuo and Chen, November 2024; NCT01896102 and NCT03852498 (zuo2024fromgeneto pages 8-10, NCT03852498 chunk 1, aertskaya2023geneandcellular pages 9-11) |


*Table: Concise evidence map distinguishing well-established molecular functions of human ABCD1 from unresolved transport chemistry and downstream disease mechanisms. It also highlights major 2023–2024 advances and clinical translation.*

## 1. Identity, architecture, and cellular location

ABCD1 is a 745-amino-acid member of the mammalian ABCD family. It is an ABC **half-transporter**: one polypeptide supplies a transmembrane domain containing six helices and one cytosolic nucleotide-binding domain (NBD). Two protomers therefore assemble to make a complete transporter. Cryo-EM consistently resolves a domain-swapped ABCD1 homodimer, while co-immunoprecipitation and FRET also support predominant homodimerization in cells. Interactions or heterodimers with ABCD2/ABCD3 have been reported, but their physiological contribution is less certain than that of the homodimer. (le2022structuresofthe pages 1-2, wright2022expressionandpurification pages 48-52, jia2022structuralandfunctional pages 1-3)

The protein is embedded in the **peroxisomal membrane**, with its ATP-binding domains exposed to the cytosol. Nucleotide-free structures are open toward the cytosol, whereas ATP-bound structures can open toward the peroxisomal lumen/matrix. This establishes the orientation expected for import from cytosolic substrate pools into peroxisomes. ABCD1 is therefore not a plasma-membrane exporter and should not be confused with lysosomal ABCD4. (wanders2007theperoxisomalabc pages 4-6, xiong2023structuralinsightsinto pages 1-2, jia2021structureinsightsof pages 5-8)

## 2. Substrate specificity and reaction

### 2.1 Best-supported substrates

Purified-protein ATPase assays, cellular transport experiments, and substrate-bound structures establish VLCFA-CoAs as ABCD1 ligands. Directly tested substrates include:

- behenoyl-CoA (**C22:0-CoA**),
- lignoceroyl-CoA (**C24:0-CoA**),
- hexacosanoyl-CoA (**C26:0-CoA**), and
- monounsaturated **C26:1-CoA**.

C22:0-, C24:0- and C26:0-CoA stimulated ATPase activity, whereas acetyl-CoA did not. One study reported similar apparent EC50 values of approximately **2 μM** and maximal activities near **200 mol Pi·min⁻¹·mol protein⁻¹** for the three saturated VLCFA-CoAs. Another preparation yielded an apparent C22:0-CoA Km of approximately **0.17 μM** and Vmax of **193 ± 8.2 mol Pi·min⁻¹·mol protein⁻¹**. Absolute values differ among detergent, liposome, nanodisc, and construct conditions, so they should not be treated as a single physiological constant. (chen2022structuralbasisof pages 1-2, jia2022structuralandfunctional pages 1-3)

ABCD1 preferentially handles saturated and monounsaturated VLCFA-CoAs, but specificity is not an absolute carbon-number cutoff. For example, C18:1-CoA stimulated ATPase activity in one lipid-environment preparation, whereas C22:6-CoA did not. Related ABCD2 and ABCD3 transporters have overlapping but distinguishable preferences, providing partial biochemical redundancy without fully replacing ABCD1 in vivo. (le2022structuresofthe pages 1-2)

### 2.2 ATP-coupled alternating-access mechanism

Substrate binds an inward-facing cavity accessible from the cytosol. ATP binding then brings the two NBDs together and rearranges the paired transmembrane domains into a matrix-facing state; ATP hydrolysis and product release reset the transporter. Basal ATPase activity in one nanodisc/detergent study was approximately **10 nmol·min⁻¹·mg⁻¹**, with ATP Km near **0.3 mM**. A differently truncated construct had ATP Km **585 ± 55 μM** and maximal basal turnover **29 ± 1 nmol·mg⁻¹·min⁻¹**, illustrating preparation dependence. Orthovanadate and ATPγS inhibit activity, and mutations in conserved ATPase machinery reduce turnover. (le2022structuresofthe pages 1-2, xiong2023structuralinsightsinto pages 1-2)

Structures show two acyl-CoA molecules bound per dimer. The polar CoA portions occupy hydrophilic transmembrane cavities, whereas the long hydrocarbon chains cross toward the opposite transmembrane domain or remain partly exposed to the surrounding bilayer. This arrangement explains how a membrane-embedded transporter can recognize an amphipathic lipid. (chen2022structuralbasisof pages 1-2)

Important substrate-contact residues include **W339**, M335, R401, S404, S226, L230, L249 and F252. W339 in TM5 is particularly important: mutation disrupts substrate binding and substrate-stimulated ATP hydrolysis. ABCD1 also has a distinctive C-terminal coiled coil that restrains NBD activity; deleting residues 686–745 increases ATPase activity. (xiong2021atpandsubstrate pages 4-6, xiong2023structuralinsightsinto pages 1-2)

### 2.3 Important unresolved issue: what actually crosses the membrane?

It is established that **VLCFA-CoA is the cytosolic loading/recognition substrate**. It is not yet conclusively established whether intact VLCFA-CoA is released into the peroxisomal matrix or whether ABCD1 hydrolyzes the thioester and transfers free fatty acid and possibly CoA separately. Intrinsic acyl-CoA thioesterase activity has been reported for ABCD proteins, prompting a model in which acyl-CoA is cleaved during import and the fatty acid is reactivated inside the peroxisome. However, ABCD1 lacks a recognizable conventional thioesterase domain, current structures do not identify definitive thioesterase chemistry, and much of the cleavage/re-esterification model derives from yeast and plant homologues. ATPase stimulation alone is also not a direct translocation assay. Consequently, annotations of both transporter activity and thioesterase activity are reasonable, but the transported chemical species and reaction sequence remain unsettled. (le2022structuresofthe pages 1-2, wright2022expressionandpurification pages 61-66)

## 3. Biochemical pathway and biological role

The core pathway is:

1. VLCFAs are generated by elongation or lipid turnover and activated to VLCFA-CoAs on the cytosolic side.
2. ABCD1 recognizes the CoA-activated lipid at the peroxisomal membrane.
3. ATP-driven alternating access delivers the lipid substrate—or hydrolysis product—toward the matrix.
4. Matrix enzymes conduct peroxisomal β-oxidation through dehydrogenation, hydration, a second dehydrogenation, and thiolytic cleavage, shortening the chain and producing acetyl-CoA-containing products.
5. Shortened products can undergo additional peroxisomal cycles or be transferred to mitochondria and other metabolic compartments.

Thus ABCD1 is the **membrane-entry gate** rather than one of the matrix β-oxidation enzymes. It connects cytosolic VLCFA metabolism to peroxisomal catabolism and thereby regulates the acyl-chain composition of phospholipids, sphingolipids, cholesterol esters and myelin lipids. (wright2022expressionandpurification pages 61-66, zuo2024fromgeneto pages 1-2)

## 4. Consequences of ABCD1 loss

Pathogenic loss-of-function variants reduce VLCFA entry into peroxisomes and β-oxidation. Patient fibroblast β-oxidation has been reported at approximately **30% of normal**. Saturated VLCFAs—especially C24:0 and C26:0—and C26:1 accumulate in activated acyl-CoA pools and in phosphatidylcholine, lysophosphatidylcholine, sphingolipids, gangliosides, cholesterol esters and myelin-associated lipids. One review reports approximately **39-fold higher C26:0** in cerebral-ALD brain than in controls. (parasar2024pathophysiologyofxlinked pages 3-5, bougneres2025revisitingthepathogenesis pages 36-38)

The best-supported downstream consequences are altered membrane properties, oxidative stress, disturbed mitochondrial respiration, axonal energetic failure, oligodendrocyte/myelin dysfunction, and inflammatory reprogramming of microglia and macrophages. These processes explain why the CNS white matter, long spinal tracts, peripheral nerves, adrenal cortex and testes are especially vulnerable. Nevertheless, VLCFA accumulation alone does not fully explain why one person develops rapidly inflammatory cerebral ALD while another with the same variant develops slowly progressive myelopathy. (parasar2024pathophysiologyofxlinked pages 3-5, zuo2024fromgeneto pages 1-2, bougneres2025revisitingthepathogenesis pages 22-24)

There is no robust genotype–phenotype correlation, and VLCFA concentration is diagnostic rather than reliably prognostic. Genetic modifiers, cell-specific epigenetics, environment, blood–brain-barrier state and stochastic multicellular interactions are leading explanations for clinical divergence. Reports of markedly different disease courses in people with the same mutation, including monozygotic twins, support this expert interpretation. (hillebrandUnknownyearinvestigatingaputative pages 10-13, zuo2024fromgeneto pages 1-2)

## 5. Recent research developments, 2023–2024

### 5.1 Structural resolution of the transport cycle

Xiong and colleagues’ peer-reviewed 2023 study reported six cryo-EM structures spanning four conformational states. It linked C26:0-CoA binding, W339-dependent substrate recognition, ATP-driven NBD closure, matrix-side opening, and inhibitory regulation by the C-terminal coiled coil. This is the most direct recent mechanistic advance in ABCD1 functional annotation. **Published February 2023:** https://doi.org/10.1038/s41392-022-01280-9. (xiong2023structuralinsightsinto pages 1-2)

### 5.2 Peroxisome–microglia connection

A 2023 RNA-sequencing study of microglial models with peroxisomal defects found broad reprogramming of lipid metabolism, immune, lysosomal and autophagy pathways, including a disease-associated-microglia-like signature and increased secretion of selected DAM proteins. This supports active microglial participation, but the models involved broader peroxisomal defects and do not prove that microglia initiate human cerebral ALD. **Published April 2023:** https://doi.org/10.3389/fnmol.2023.1170313.

### 5.3 Mitochondrial dynamics as a downstream therapeutic node

A 2024 *Brain* study found mitochondrial fragmentation in corticospinal axons of Abcd1-deficient mice. Excess VLCFAs induced redox-dependent DRP1-Ser616 phosphorylation and fragmentation in patient fibroblasts; the P110 peptide preserved mitochondrial morphology, while DRP1 RNA inhibition protected axons in a *C. elegans* model. This positions DRP1-dependent fission downstream of ABCD1/VLCFA dysfunction, but it remains a preclinical target rather than an established therapy. **Published May 2024:** https://doi.org/10.1093/brain/awae038.

A 2024 review also emphasizes modifier genes, microRNAs, mitochondrial dysfunction and oxidative stress, while acknowledging that the trigger for inflammatory cerebral conversion is unresolved. **Published June 2024:** https://doi.org/10.26502/jbb.2642-91280151. (parasar2024pathophysiologyofxlinked pages 3-5, parasar2024pathophysiologyofxlinked pages 10-11)

## 6. Current applications and real-world implementation

### 6.1 Diagnosis and newborn screening

The principal screening biomarker is **C26:0-lysophosphatidylcholine (C26:0-LysoPC)** measured by LC–MS/MS in dried blood spots, followed by ABCD1 sequencing and confirmatory biochemical/genetic evaluation. New York began newborn screening in 2013; X-ALD entered the US Recommended Uniform Screening Panel in 2016; and by 2024 approximately **44 US states plus Washington, DC** were screening. Screening is also implemented or developing internationally. (porcari2025currentadvancesand pages 4-5, zuo2024fromgeneto pages 8-10)

Screening does not predict phenotype. Its practical value is to enable adrenal surveillance, serial brain MRI before symptoms, rapid treatment of early inflammatory cerebral disease, family cascade testing and reproductive counseling. Variants of uncertain significance and detection of girls who may remain asymptomatic for decades require careful longitudinal interpretation. (porcari2025currentadvancesand pages 5-6, zuo2024fromgeneto pages 8-10)

### 6.2 Hematopoietic stem-cell transplantation

Allogeneic HSCT can arrest early active cerebral demyelination, probably because donor-derived myeloid cells repopulate brain macrophage/microglial compartments and supply functional ABCD1. Benefit depends strongly on treatment before major neurologic disability. Risks include graft-versus-host disease, graft failure, rejection, infection and conditioning toxicity. HSCT does not directly replace ABCD1 in every oligodendrocyte, neuron, adrenal cell or spinal axon and is not an established reversal treatment for advanced cerebral disease or chronic adrenomyeloneuropathy. (gornostal2025anaavbasedtherapy pages 2-4, parasar2024pathophysiologyofxlinked pages 10-11)

### 6.3 Elivaldogene autotemcel (eli-cel; Skysona/Lenti-D)

Eli-cel uses autologous CD34+ hematopoietic stem/progenitor cells transduced ex vivo with a lentiviral vector carrying functional human **ABCD1** cDNA. After myeloablative conditioning, cells are reinfused and generate ABCD1-expressing hematopoietic descendants, including brain myeloid cells. It avoids graft-versus-host disease but retains conditioning toxicity and vector-integration risk. It is intended for selected boys aged approximately 4–17 years with early, active cerebral ALD, not established myelopathy; it does not reliably prevent or correct adrenal insufficiency. (porcari2025currentadvancesand pages 5-6, zuo2024fromgeneto pages 5-7)

The completed phase 2/3 ALD-102 study enrolled **32** participants, and phase 3 ALD-104 enrolled **35**. ALD-104 used a single infusion after busulfan/fludarabine conditioning and assessed 24-month survival without six major functional disabilities. Earlier results in 17 treated boys reported **88% survival without major functional disability** at median **29.4 months**. (zuo2024fromgeneto pages 5-7, NCT03852498 chunk 1)

The major limitation is insertional oncogenesis. Myelodysplastic syndromes were linked to vector integration near **MECOM** and **PRDM16**, and subsequent reports include myeloid malignancies. Reviews stress that risk depends on vector architecture, promoter, disease context and integration pattern; lifelong blood-count and clonal surveillance is therefore required. Regulatory benefit–risk judgments have been restricted to patients with early cerebral disease lacking an appropriate donor, for whom untreated disease is rapidly devastating. (aertskaya2023geneandcellular pages 9-11)

### 6.4 Investigational pharmacology

Leriglitazone, a brain-penetrant PPARγ agonist, is being investigated as a pathway-modifying treatment rather than direct ABCD1 replacement. ClinicalTrials.gov identifies an active, non-recruiting phase 3 study in adult men with cerebral ALD, **NCT05819866**, with planned enrollment of **40**. Current evidence should therefore be described as investigational, not established clinical efficacy.

Other proposed strategies include increasing compensatory ABCD2 expression, reducing VLCFA synthesis/elongation, correcting oxidative and mitochondrial stress, and in-vivo AAV-mediated ABCD1 delivery. These remain less clinically mature than early HSCT or eli-cel.

## 7. Quantitative disease context

Published estimates vary with ascertainment. Recent reviews cite prevalence around **1 in 17,000 newborns** or approximately **1 in 20,000–21,000 males**. Male patients have very high lifetime risk of myelopathy; one authoritative model-system review estimated near **100%**, with approximately **60%** lifetime prevalence of cerebral white-matter lesions and about **80%** risk of adrenal insufficiency. Around **80% of women** with an ABCD1 pathogenic variant may eventually develop myelopathy, while adrenal and cerebral disease are uncommon in women. These are population-level estimates, not predictions for an individual. (wright2022expressionandpurification pages 61-66, zuo2024fromgeneto pages 1-2, porcari2025currentadvancesand pages 4-5)

## 8. Overall evidence assessment

**High-confidence annotation:** human ABCD1/P33897 is a peroxisomal membrane, homodimeric ABC half-transporter that uses ATP to import VLCFA-CoA-derived substrates for β-oxidation. Direct structural and biochemical evidence supports C22:0-, C24:0-, C26:0- and C26:1-CoA recognition and an alternating-access transport cycle.

**Moderate-confidence inference:** the pathway likely includes acyl-CoA hydrolysis and matrix-side reactivation, but direct product-resolved transport measurements are insufficient to establish exactly what crosses the membrane.

**Disease-level uncertainty:** ABCD1 loss and VLCFA accumulation are necessary causes of X-ALD, but neither variant class nor VLCFA burden explains cerebral inflammatory conversion. Consequently, C26:0-LysoPC is an excellent screening/diagnostic biomarker but not a reliable standalone prognostic biomarker. Current expert practice therefore combines biochemical diagnosis with lifelong adrenal, neurologic and MRI surveillance, reserving transplantation or gene therapy for appropriately selected early cerebral disease.

References

1. (OpenTargets Search: X-linked adrenoleukodystrophy-ABCD1): Open Targets Query (X-linked adrenoleukodystrophy-ABCD1, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (xiong2023structuralinsightsinto pages 1-2): Chao Xiong, Li-Na Jia, Wei-Xi Xiong, Xin-Tong Wu, Liu-Lin Xiong, Ting-Hua Wang, Dong Zhou, Zhen Hong, Zheng Liu, and Lin Tang. Structural insights into substrate recognition and translocation of human peroxisomal abc transporter aldp. Signal Transduction and Targeted Therapy, Feb 2023. URL: https://doi.org/10.1038/s41392-022-01280-9, doi:10.1038/s41392-022-01280-9. This article has 24 citations and is from a peer-reviewed journal.

3. (chen2022structuralbasisof pages 1-2): Zhi-Peng Chen, Da Xu, Liang Wang, Yao-Xu Mao, Yang Li, Meng-Ting Cheng, Cong-Zhao Zhou, Wen-Tao Hou, and Yuxing Chen. Structural basis of substrate recognition and translocation by human very long-chain fatty acid transporter abcd1. Nature Communications, Jun 2022. URL: https://doi.org/10.1038/s41467-022-30974-5, doi:10.1038/s41467-022-30974-5. This article has 46 citations and is from a highest quality peer-reviewed journal.

4. (jia2022structuralandfunctional pages 3-4): Yutian Jia, Yanming Zhang, Wenhao Wang, Jianlin Lei, Zhengxin Ying, and Guanghui Yang. Structural and functional insights of the human peroxisomal abc transporter aldp. eLife, Nov 2022. URL: https://doi.org/10.7554/elife.75039, doi:10.7554/elife.75039. This article has 16 citations and is from a domain leading peer-reviewed journal.

5. (bougneres2025revisitingthepathogenesis pages 36-38): Pierre Bougnères and C. Le Stunff. Revisiting the pathogenesis of x-linked adrenoleukodystrophy. Genes, May 2025. URL: https://doi.org/10.3390/genes16050590, doi:10.3390/genes16050590. This article has 11 citations.

6. (wanders2007theperoxisomalabc pages 4-6): Ronald J. A. Wanders, Wouter F. Visser, Carlo W. T. van Roermund, Stephan Kemp, and Hans R. Waterham. The peroxisomal abc transporter family. Pflügers Archiv - European Journal of Physiology, 453:719-734, Feb 2007. URL: https://doi.org/10.1007/s00424-006-0142-x, doi:10.1007/s00424-006-0142-x. This article has 156 citations.

7. (jia2022structuralandfunctional pages 1-3): Yutian Jia, Yanming Zhang, Wenhao Wang, Jianlin Lei, Zhengxin Ying, and Guanghui Yang. Structural and functional insights of the human peroxisomal abc transporter aldp. eLife, Nov 2022. URL: https://doi.org/10.7554/elife.75039, doi:10.7554/elife.75039. This article has 16 citations and is from a domain leading peer-reviewed journal.

8. (le2022structuresofthe pages 1-2): Le Thi My Le, James Robert Thompson, Phuoc Xuan Dang, Janarjan Bhandari, and Amer Alam. Structures of the human peroxisomal fatty acid transporter abcd1 in a lipid environment. Communications Biology, Jan 2022. URL: https://doi.org/10.1038/s42003-021-02970-w, doi:10.1038/s42003-021-02970-w. This article has 37 citations and is from a peer-reviewed journal.

9. (wright2022expressionandpurification pages 48-52): J Wright. Expression and purification of comatose, a plant peroxisomal abcd transporter, for functional and structural studies. Unknown journal, 2022.

10. (xiong2021atpandsubstrate pages 4-6): Chao Xiong, Li-Na Jia, Ming-He Shen, Wei-Xi Xiong, Liu-Lin Xiong, Ting-Hua Wang, Dong Zhou, Zheng Liu, and Lin Tang. Atp and substrate binding regulates conformational changes of human peroxisomal abc transporter aldp. bioRxiv, Oct 2021. URL: https://doi.org/10.1101/2021.10.14.464310, doi:10.1101/2021.10.14.464310. This article has 2 citations.

11. (wright2022expressionandpurification pages 61-66): J Wright. Expression and purification of comatose, a plant peroxisomal abcd transporter, for functional and structural studies. Unknown journal, 2022.

12. (parasar2024pathophysiologyofxlinked pages 3-5): Parveen Parasar, Navtej Kaur, and Jaspreet Singh. Pathophysiology of x-linked adrenoleukodystrophy: updates on molecular mechanisms. Journal of biotechnology and biomedicine, 7:277-288, Jun 2024. URL: https://doi.org/10.26502/jbb.2642-91280151, doi:10.26502/jbb.2642-91280151. This article has 17 citations.

13. (zuo2024fromgeneto pages 1-2): Xinxin Zuo and Zeyu Chen. From gene to therapy: a review of deciphering the role of abcd1 in combating x-linked adrenoleukodystrophy. Lipids in Health and Disease, Nov 2024. URL: https://doi.org/10.1186/s12944-024-02361-0, doi:10.1186/s12944-024-02361-0. This article has 14 citations and is from a peer-reviewed journal.

14. (zuo2024fromgeneto pages 8-10): Xinxin Zuo and Zeyu Chen. From gene to therapy: a review of deciphering the role of abcd1 in combating x-linked adrenoleukodystrophy. Lipids in Health and Disease, Nov 2024. URL: https://doi.org/10.1186/s12944-024-02361-0, doi:10.1186/s12944-024-02361-0. This article has 14 citations and is from a peer-reviewed journal.

15. (NCT03852498 chunk 1):  A Clinical Study to Assess the Efficacy and Safety of Gene Therapy for the Treatment of Cerebral Adrenoleukodystrophy (CALD). Genetix Biotherapeutics Inc.. 2019. ClinicalTrials.gov Identifier: NCT03852498

16. (aertskaya2023geneandcellular pages 9-11): Fatima Aerts-Kaya and Niek P. van Til. Gene and cellular therapies for leukodystrophies. Pharmaceutics, 15:2522, Oct 2023. URL: https://doi.org/10.3390/pharmaceutics15112522, doi:10.3390/pharmaceutics15112522. This article has 13 citations.

17. (jia2021structureinsightsof pages 5-8): Yutian Jia, Yanming Zhang, Jianlin Lei, and Guanghui Yang. Structure insights of the human peroxisomal abc transporter aldp. bioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.24.461756, doi:10.1101/2021.09.24.461756. This article has 2 citations.

18. (bougneres2025revisitingthepathogenesis pages 22-24): Pierre Bougnères and C. Le Stunff. Revisiting the pathogenesis of x-linked adrenoleukodystrophy. Genes, May 2025. URL: https://doi.org/10.3390/genes16050590, doi:10.3390/genes16050590. This article has 11 citations.

19. (hillebrandUnknownyearinvestigatingaputative pages 10-13): M Hillebrand. Investigating a putative link between cd36 polymorphism and neuroinflammation in x-linked adrenoleukodystrophy. Unknown journal, Unknown year.

20. (parasar2024pathophysiologyofxlinked pages 10-11): Parveen Parasar, Navtej Kaur, and Jaspreet Singh. Pathophysiology of x-linked adrenoleukodystrophy: updates on molecular mechanisms. Journal of biotechnology and biomedicine, 7:277-288, Jun 2024. URL: https://doi.org/10.26502/jbb.2642-91280151, doi:10.26502/jbb.2642-91280151. This article has 17 citations.

21. (porcari2025currentadvancesand pages 4-5): Giulia Stefania Porcari, John Warren Collyer, Laura Ann Adang, and Deepa Soundara Rajan. Current advances and challenges in gene therapies for neurologic disorders. Feb 2025. URL: https://doi.org/10.1212/nxg.0000000000200229, doi:10.1212/nxg.0000000000200229. This article has 23 citations.

22. (porcari2025currentadvancesand pages 5-6): Giulia Stefania Porcari, John Warren Collyer, Laura Ann Adang, and Deepa Soundara Rajan. Current advances and challenges in gene therapies for neurologic disorders. Feb 2025. URL: https://doi.org/10.1212/nxg.0000000000200229, doi:10.1212/nxg.0000000000200229. This article has 23 citations.

23. (gornostal2025anaavbasedtherapy pages 2-4): Ekaterina Gornostal, Almaqdad Alsalloum, Egor Degtyarev, Ekaterina Kuznetsova, Aygun Levashova, Daria Mishina, Natalia Mingaleva, Ali Mazloum, Viktor Bogdanov, Julia Krupinova, Sergey Mikhalkov, Irina Rybkina, Olga Mityaeva, and Pavel Volchkov. An aav-based therapy approach for neurological phenotypes of x-linked adrenoleukodystrophy. International Journal of Molecular Sciences, 26:11645, Dec 2025. URL: https://doi.org/10.3390/ijms262311645, doi:10.3390/ijms262311645. This article has 0 citations.

24. (zuo2024fromgeneto pages 5-7): Xinxin Zuo and Zeyu Chen. From gene to therapy: a review of deciphering the role of abcd1 in combating x-linked adrenoleukodystrophy. Lipids in Health and Disease, Nov 2024. URL: https://doi.org/10.1186/s12944-024-02361-0, doi:10.1186/s12944-024-02361-0. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](ABCD1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. le2022structuresofthe pages 1-2
2. chen2022structuralbasisof pages 1-2
3. xiong2023structuralinsightsinto pages 1-2
4. aertskaya2023geneandcellular pages 9-11
5. jia2022structuralandfunctional pages 3-4
6. bougneres2025revisitingthepathogenesis pages 36-38
7. wanders2007theperoxisomalabc pages 4-6
8. jia2022structuralandfunctional pages 1-3
9. wright2022expressionandpurification pages 48-52
10. xiong2021atpandsubstrate pages 4-6
11. wright2022expressionandpurification pages 61-66
12. parasar2024pathophysiologyofxlinked pages 3-5
13. zuo2024fromgeneto pages 1-2
14. zuo2024fromgeneto pages 8-10
15. jia2021structureinsightsof pages 5-8
16. bougneres2025revisitingthepathogenesis pages 22-24
17. parasar2024pathophysiologyofxlinked pages 10-11
18. porcari2025currentadvancesand pages 4-5
19. porcari2025currentadvancesand pages 5-6
20. gornostal2025anaavbasedtherapy pages 2-4
21. zuo2024fromgeneto pages 5-7
22. https://doi.org/10.1038/s41392-022-01280-9.
23. https://doi.org/10.3389/fnmol.2023.1170313.
24. https://doi.org/10.1093/brain/awae038.
25. https://doi.org/10.26502/jbb.2642-91280151.
26. https://doi.org/10.1038/s41392-022-01280-9,
27. https://doi.org/10.1038/s41467-022-30974-5,
28. https://doi.org/10.7554/elife.75039,
29. https://doi.org/10.3390/genes16050590,
30. https://doi.org/10.1007/s00424-006-0142-x,
31. https://doi.org/10.1038/s42003-021-02970-w,
32. https://doi.org/10.1101/2021.10.14.464310,
33. https://doi.org/10.26502/jbb.2642-91280151,
34. https://doi.org/10.1186/s12944-024-02361-0,
35. https://doi.org/10.3390/pharmaceutics15112522,
36. https://doi.org/10.1101/2021.09.24.461756,
37. https://doi.org/10.1212/nxg.0000000000200229,
38. https://doi.org/10.3390/ijms262311645,