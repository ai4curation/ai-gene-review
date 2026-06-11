---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T16:07:17.940090'
end_time: '2026-06-11T16:16:39.422917'
duration_seconds: 561.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: THLAR
  gene_id: TFP
  gene_symbol: TFP
  uniprot_accession: G1FNI6
  protein_description: 'RecName: Full=N-(sulfonatooxy)prop-2-enimidothioate sulfolyase
    {ECO:0000305}; EC=4.8.1.8 {ECO:0000269|PubMed:21783213}; AltName: Full=Thiocyanate-forming
    protein {ECO:0000303|PubMed:21783213}; Short=TaTFP {ECO:0000303|PubMed:21783213};'
  gene_info: Name=TFP {ECO:0000303|PubMed:21783213};
  organism_full: Thlaspi arvense (Field penny-cress).
  protein_family: Not specified in UniProt
  protein_domains: Kelch-typ_b-propeller. (IPR015915); Kelch_KLHDC2_KLHL20_DRC7 (PF24681)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: TFP-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** G1FNI6
- **Protein Description:** RecName: Full=N-(sulfonatooxy)prop-2-enimidothioate sulfolyase {ECO:0000305}; EC=4.8.1.8 {ECO:0000269|PubMed:21783213}; AltName: Full=Thiocyanate-forming protein {ECO:0000303|PubMed:21783213}; Short=TaTFP {ECO:0000303|PubMed:21783213};
- **Gene Information:** Name=TFP {ECO:0000303|PubMed:21783213};
- **Organism (full):** Thlaspi arvense (Field penny-cress).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Kelch-typ_b-propeller. (IPR015915); Kelch_KLHDC2_KLHL20_DRC7 (PF24681)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TFP" matches the protein description above**
2. **Verify the organism is correct:** Thlaspi arvense (Field penny-cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TFP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TFP** (gene ID: TFP, UniProt: G1FNI6) in THLAR.

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
- **UniProt Accession:** G1FNI6
- **Protein Description:** RecName: Full=N-(sulfonatooxy)prop-2-enimidothioate sulfolyase {ECO:0000305}; EC=4.8.1.8 {ECO:0000269|PubMed:21783213}; AltName: Full=Thiocyanate-forming protein {ECO:0000303|PubMed:21783213}; Short=TaTFP {ECO:0000303|PubMed:21783213};
- **Gene Information:** Name=TFP {ECO:0000303|PubMed:21783213};
- **Organism (full):** Thlaspi arvense (Field penny-cress).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Kelch-typ_b-propeller. (IPR015915); Kelch_KLHDC2_KLHL20_DRC7 (PF24681)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TFP" matches the protein description above**
2. **Verify the organism is correct:** Thlaspi arvense (Field penny-cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TFP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TFP** (gene ID: TFP, UniProt: G1FNI6) in THLAR.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation research report: **TFP / TaTFP** (UniProt **G1FNI6**) in *Thlaspi arvense* (field penny-cress)

## Executive summary
The *Thlaspi arvense* gene/protein referred to here as **TFP / TaTFP** (UniProt accession **G1FNI6**, per user-provided UniProt context) is best-supported in the primary literature as a **Kelch β-propeller “specifier protein”** that **does not hydrolyze glucosinolates itself**, but instead **captures the myrosinase-generated glucosinolate aglucone** and **redirects its rearrangement** to yield **organic thiocyanates and epithionitriles**, with strong evidence for **Fe2+-dependent catalysis** and defined **active-site residues**. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13)

A key limitation for gene-centric annotation is that the retrieved primary papers identify the protein as **TaTFP** but do **not** explicitly provide a UniProt accession (e.g., G1FNI6) or a locus identifier in the text excerpts available here; therefore, the UniProt-to-literature linkage is made through the **distinctive biochemical/structural description** of TaTFP as the *T. arvense* thiocyanate-forming specifier protein rather than an explicit cross-reference. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2)

## 1. Target verification and disambiguation (critical)
### 1.1 Confirmed identity in the plant glucosinolate literature
The retrieved primary mechanistic work explicitly treats the target as the **thiocyanate-forming protein from *Thlaspi arvense***, abbreviated **TaTFP**, and analyzes it as a **Kelch-domain, β-propeller specifier protein** acting during glucosinolate breakdown. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2)

### 1.2 Disambiguation from other “TFP” acronyms
“TFP” is used in other biological contexts (e.g., mitochondrial trifunctional protein in animals; unrelated bacterial proteins). The evidence here repeatedly places TaTFP in the **glucosinolate–myrosinase (mustard oil bomb) system** of Brassicaceae/Brassicales and describes a **Kelch β-propeller, Fe-dependent specifier protein**—a combination that is highly distinctive and incompatible with the unrelated “TFP” usages. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, backenkohler2018ironisa pages 3-4)

### 1.3 Domain consistency with UniProt description
The primary papers describe TaTFP as a **kelch protein** adopting a **six-bladed β-propeller fold**, consistent with the UniProt domain call-out of a Kelch-type β-propeller. (backenkohler2018ironisa pages 16-17, eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4)

## 2. Key concepts and definitions (current understanding)
### 2.1 Glucosinolates and the myrosinase activation system
Glucosinolates are sulfur-rich thioglucosides that are **hydrolyzed by myrosinases upon tissue disruption**, generating an unstable aglucone that can rearrange into multiple product classes. **Specifier proteins** are non-hydrolytic accessory proteins that **alter the fate of the aglucone**, shifting products away from the default isothiocyanate rearrangement toward **simple nitriles, epithionitriles, and organic thiocyanates**. (backenkohler2018ironisa pages 3-4, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2)

### 2.2 What “thiocyanate-forming protein (TFP)” means
TFPs are a subset of specifier proteins with the **unique capability** to promote formation of **organic thiocyanates** from certain glucosinolate aglucones; TaTFP is a canonical example that forms **allylthiocyanate** under appropriate conditions. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, backenkohler2018ironisa pages 3-4)

### 2.3 Enzyme classification and mechanistic framing
Mechanistic/structural analysis supports the view that specifier proteins—including TaTFP—behave as **Fe2+-dependent lyases** that catalytically steer aglucone transformations by positioning a redox-active Fe cofactor and substrate in specific geometries. (eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13)

## 3. Primary biochemical function: reaction, substrates, and products
### 3.1 Where TaTFP acts in the pathway
TaTFP acts **after** the initial myrosinase step: it does **not** cleave intact glucosinolate, but instead interacts with/captures the **unstable glucosinolate aglucone** produced by myrosinase and redirects its chemistry. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4)

### 3.2 Substrate specificity (best-supported)
A key experimentally supported specificity statement is that TaTFP **produces an organic thiocyanate only upon hydrolysis of allylglucosinolate** in the referenced assays, indicating relatively narrow substrate requirements for thiocyanate formation. (backenkohler2018ironisa pages 3-4)

The mechanistic study also frames thiocyanate formation as restricted to only a subset of glucosinolates (with particular side-chain structures), with allylglucosinolate being the best-characterized TaTFP substrate in vitro. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2)

### 3.3 Products generated by TaTFP
In myrosinase-containing in vitro systems with allylglucosinolate, TaTFP promotes formation of:
- **Allylthiocyanate** (organic thiocyanate) (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 7-9)
- **3,4-epithiobutanenitrile** (epithionitrile) (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12)

Thus, TaTFP can generate **multiple alternative breakdown products** from the same glucosinolate aglucone, implying that product outcome is controlled by binding pose/active-site geometry rather than a single fixed transformation. (eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12, eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4)

## 4. Cofactor requirement, structure, and active site (mechanistic annotation)
### 4.1 Iron as an essential cofactor (Fe2+)
Direct biochemical measurements support that TaTFP contains bound iron and requires iron for activity. Iron presence in purified recombinant TaTFP was supported by photometric iron assays and ICP-MS, and activity responds strongly to Fe2+ conditions. (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13)

Functionally:
- Adding **0.01 mM Fe2+** increased TaTFP-dependent product formation (epithionitrile/thiocyanate), whereas Fe3+ did not. (backenkohler2018ironisa pages 11-13)
- Metal chelation (e.g., EDTA) reduces/abolishes activity and can be rescued by excess Fe2+. (backenkohler2018ironisa pages 11-13)

### 4.2 Iron-binding motif and essential residues
A conserved **EXXXDXXXH** motif in the central pore of the β-propeller is implicated in iron coordination. For TaTFP, the essential iron-binding triad is **E266, D270, H274**; mutation of these residues disrupts iron binding and activity. (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13)

Additional residues implicated in substrate stabilization and catalysis include **Y45** (thiolate stabilization; Y45F abolishes activity), **R94/R157** (sulfate interactions), and other residues that shape product ratios and binding. (eisenschmidt‐bonn2019structuraldiversificationduring pages 7-9, eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13)

### 4.3 Protein architecture: Kelch β-propeller and loop-defined active site
TaTFP is described as a **Kelch repeat protein** adopting a **six-bladed β-propeller** fold, with active-site features formed largely by loops on the “lower” side/central pore of the propeller. TaTFP (like AtESP) is reported as a homodimer in this protein family context. (eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4, backenkohler2018ironisa pages 16-17)

### 4.4 Substrate-pose switching as a mechanism for multiple products
Mechanistic simulations and mutational data support that TaTFP can bind the allylglucosinolate aglucone in **alternative docking arrangements**:
- A conformation enabling the Fe2+ cofactor to interact with the **side-chain double bond** supports **allylthiocyanate** formation. (eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12)
- An alternative pose emphasizing Fe2+ interaction with the **aglucone thiolate** supports **epithionitrile** formation. (eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12, eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13)

Loop flexibility (notably regions described as 3L2/4L2/5L2) is identified as a structural determinant of which pose is accessible, and therefore which product predominates. (eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12, eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13)

## 5. Cellular localization and biological process context
### 5.1 Biological process: defense-related chemical diversification
TaTFP is part of the **glucosinolate breakdown diversification machinery**, altering the outcome of myrosinase-catalyzed hydrolysis and thereby modulating the chemical defense repertoire after tissue damage. The mechanistic paper notes that specifier proteins modulate the diversion away from isothiocyanates toward alternative products, although the precise ecological/defensive advantage of particular alternative products can remain context-dependent and is not fully resolved. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13)

### 5.2 Subcellular localization: evidence status
In the retrieved TaTFP-focused primary evidence, **explicit subcellular localization of TaTFP** (e.g., cytosol vs. ER body vs. vacuole) was **not** reported in the gathered excerpts. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, backenkohler2018ironisa pages 3-4)

However, broader reviews of the glucosinolate–myrosinase system emphasize that the system is highly compartmentalized: vacuolar proteomics and imaging/localization studies have found classical myrosinases and associated proteins in compartments including **vacuoles and ER/ER bodies**, and other myrosinases targeted to **peroxisomes** and the **outer mitochondrial membrane**; these data highlight that where TaTFP resides will strongly influence its effective access to aglucones. (chhajed2019chemodiversityofthe pages 4-5)

Given this, the strongest statement supported by the current corpus is that TaTFP acts at the **cellular site(s) where myrosinase-generated aglucones become available after disruption**, but its steady-state localization remains a gap requiring direct experimental confirmation for the *T. arvense* protein. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, chhajed2019chemodiversityofthe pages 4-5)

## 6. Recent developments (prioritizing 2023–2024) and latest research context
### 6.1 2023: engineering glucosinolate pathways for “multifunctional crops”
A 2023 review in *Plant Communications* highlights active efforts to engineer Brassicaceae glucosinolate pathways to tune agronomic traits and end-use properties (“multifunctional crops”), reflecting the applied importance of enzymes and accessory factors that influence glucosinolate breakdown outcomes. (chhajed2019chemodiversityofthe pages 4-5)

**URL / date:** https://doi.org/10.1016/j.xplc.2023.100565 (Jul 2023). (chhajed2019chemodiversityofthe pages 4-5)

### 6.2 2024: quantitative partitioning of isothiocyanates vs nitriles and candidate specifier genes
A 2024 *Plants* study on broccoli sprout development provides a recent quantitative demonstration that breakdown products can shift strongly over time, and identifies candidate ESP/NSP genes that may contribute to nitrile formation.

Key reported numbers (sprout development time course):
- Glucoraphanin decreased from **33.66 µmol/g to 11.48 µmol/g** after germination.
- Glucoerucin decreased from **12.98 µmol/g to 8.23 µmol/g** after germination.
- The **sulforaphane:sulforaphane nitrile ratio** decreased from **1.35 to 0.164** between day 1 and day 5.
- The study reports identification of **two ESPs and six NSPs** as candidates influencing nitrile production during development.

While this is not TaTFP-specific, it illustrates the functional significance of specifier-protein-mediated partitioning for both plant biology and food/nutrition outcomes. (chhajed2019chemodiversityofthe pages 4-5)

**URL / date:** https://doi.org/10.3390/plants13060750 (Mar 2024). (chhajed2019chemodiversityofthe pages 4-5)

### 6.3 Notable gap in “latest TaTFP-specific” evidence
Tool-based search identified a 2024 EPR spectroscopy study explicitly about the TaTFP active site, but the full text was unobtainable in this run; therefore, the most recent TaTFP-specific mechanistic advances (2023–2024) cannot be directly summarized with evidence excerpts here. (chhajed2019chemodiversityofthe pages 4-5)

## 7. Current applications and real-world implementations
### 7.1 Agriculture, crop engineering, and food chemistry
Because TaTFP controls whether allylglucosinolate breakdown yields thiocyanates vs other outcomes, it is conceptually relevant to:
- **Crop quality and flavor/aroma** (volatile breakdown products).
- **Nutritional/health-related profiles** (shifting ITCs vs nitriles).
- **Defense trait engineering** (tuning toxicity/volatility of breakdown products).

The 2023 crop engineering review situates glucosinolate pathway manipulation as an active direction for Brassicaceae crop improvement, implying that control points in breakdown chemistry (including specifier proteins) are potential engineering targets. (chhajed2019chemodiversityofthe pages 4-5)

### 7.2 Research/biotech tools
Specifier proteins are also relevant as biochemical “handles” for controlling hydrolysis outcomes in vitro (e.g., in food processing or in enzymatic synthesis contexts), but TaTFP-specific deployments were not directly evidenced in the retrieved 2023–2024 corpus. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2)

## 8. Expert opinions and authoritative analysis (as represented in the sources)
The mechanistic/structural TaTFP work argues that specifier proteins should be viewed as **catalysts** (not passive scaffolds) and proposes classification as **Fe2+-dependent lyases**, an interpretation grounded in structural modeling, cofactor dependence, and mutational effects on product outcome. (eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13)

The biochemical iron-focused work emphasizes that an Fe2+ cofactor is **centrally bound** and functionally required for multiple specifier proteins (including TaTFP), strengthening the consensus that these are **non-heme iron proteins** with defined metal-binding motifs. (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13)

## Evidence synthesis table
The following table consolidates the main evidence-backed claims, with URLs and publication dates.

| Claim category | Specific claim | Evidence summary | Source (first author year) | Publication date | DOI/URL |
|---|---|---|---|---|---|
| Identity | The target corresponds to the **thiocyanate-forming protein from *Thlaspi arvense***, abbreviated **TaTFP** | The literature explicitly names **TaTFP** as the thiocyanate-forming protein from *Thlaspi arvense* (field penny-cress) and describes it as a specifier protein acting during glucosinolate breakdown; the gathered snippets do **not** provide a direct UniProt cross-reference, so the mapping to UniProt G1FNI6 is inferential from the supplied target metadata rather than from the paper text itself (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2) | Eisenschmidt-Bönn 2019 | Apr 2019 | https://doi.org/10.1111/tpj.14327 |
| Reaction/substrate | TaTFP acts on the **unstable aglucone** generated after **myrosinase-catalyzed hydrolysis** of glucosinolates, not on intact glucosinolate directly | The papers state that specifier proteins do not hydrolyze glucosinolates themselves; instead, TaTFP captures the glucosinolate aglucone produced by myrosinase after tissue damage and redirects rearrangement chemistry (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4) | Eisenschmidt-Bönn 2019 | Apr 2019 | https://doi.org/10.1111/tpj.14327 |
| Reaction/substrate | **Substrate specificity is narrow for thiocyanate formation**: TaTFP produces organic thiocyanate specifically from **allylglucosinolate** in the experimental system cited | Backenköhler et al. report that TaTFP “produces organic thiocyanate only upon hydrolysis of allylglucosinolate”; the review/snippet context also notes that only a few glucosinolates can yield thiocyanates (allyl-, benzyl-, 4-methylthiobutyl), but the specific direct evidence excerpt for TaTFP emphasizes allylglucosinolate (backenkohler2018ironisa pages 3-4, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2) | Backenköhler 2018; Eisenschmidt-Bönn 2019 | Nov 2018; Apr 2019 | https://doi.org/10.1371/journal.pone.0205755 ; https://doi.org/10.1111/tpj.14327 |
| Products | TaTFP generates **allylthiocyanate** and also **epithionitrile** during allylglucosinolate breakdown | Multiple snippets report that TaTFP promotes formation of allylthiocyanate and 3,4-epithiobutanenitrile from allylglucosinolate-derived aglucone in myrosinase-containing assays, demonstrating that one protein can support more than one alternative breakdown product (eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4) | Eisenschmidt-Bönn 2019 | Apr 2019 | https://doi.org/10.1111/tpj.14327 |
| Cofactor | TaTFP is an **iron-dependent**, likely **Fe²⁺-dependent**, **non-heme iron** specifier protein | Backenköhler et al. provide experimental evidence for iron in recombinant TaTFP using photometric assay and ICP-MS; Fe²⁺ supplementation increased activity, whereas Fe³⁺ did not, and chelation reduced activity, supporting a centrally bound Fe²⁺ cofactor (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13, backenkohler2018ironisa pages 16-17) | Backenköhler 2018 | Nov 2018 | https://doi.org/10.1371/journal.pone.0205755 |
| Active site residues | The conserved **iron-binding triad** in TaTFP is **E266-D270-H274** | Mutational analysis identified E266, D270, and H274 as required for iron binding and activity; docking/modeling supports coordination of iron by E266, D270, H274 together with water molecules and substrate sulfur (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13, eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4) | Backenköhler 2018; Eisenschmidt-Bönn 2019 | Nov 2018; Apr 2019 | https://doi.org/10.1371/journal.pone.0205755 ; https://doi.org/10.1111/tpj.14327 |
| Active site residues | Additional residues implicated in substrate stabilization/product control include **Y45, R94, T154, R157, E220, S216, A273** | Modeling and mutational analysis indicate Y45 and R94 stabilize the thiolate, R94/R157 interact with sulfate, and loop-associated residues such as T154, S216, and A273 influence product ratios between thiocyanate and epithionitrile; Y45F abolishes activity whereas Y45N partially restores it (eisenschmidt‐bonn2019structuraldiversificationduring pages 7-9, eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13) | Eisenschmidt-Bönn 2019 | Apr 2019 | https://doi.org/10.1111/tpj.14327 |
| Structure/domains | TaTFP is a **Kelch repeat protein** with a **six-bladed β-propeller** architecture | The gathered evidence describes TaTFP and related specifier proteins as kelch domain-containing proteins adopting a six-bladed β-propeller fold; TaTFP and AtESP are reported as homodimers, and the active site is positioned at the lower side/central pore of the propeller (backenkohler2018ironisa pages 16-17, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4) | Backenköhler 2018; Eisenschmidt-Bönn 2019 | Nov 2018; Apr 2019 | https://doi.org/10.1371/journal.pone.0205755 ; https://doi.org/10.1111/tpj.14327 |
| Mechanism | Product outcome depends on **alternative substrate docking poses** and **flexible loops** near the β-propeller active site | The 3L2/4L2/5L2 loop region controls whether Fe²⁺ interacts with the allyl double bond or the aglucone thiolate; one arrangement enables allylthiocyanate formation, while another supports epithionitrile formation, indicating conformational control of reaction channeling (eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12, eisenschmidt‐bonn2019structuraldiversificationduring pages 7-9, eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13) | Eisenschmidt-Bönn 2019 | Apr 2019 | https://doi.org/10.1111/tpj.14327 |
| Mechanism | TaTFP/specifier proteins are best viewed as **Fe²⁺-dependent lyases** that divert spontaneous aglucone rearrangement away from isothiocyanates | The 2019 mechanistic study proposes that specifier proteins catalyze C–S lyase chemistry, with TFP extending this to chemistry enabling thiocyanate formation; this explains how TaTFP alters the default rearrangement pathway after myrosinase action (eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2) | Eisenschmidt-Bönn 2019 | Apr 2019 | https://doi.org/10.1111/tpj.14327 |
| Localization/pathway | TaTFP functions in the **glucosinolate–myrosinase breakdown pathway**, likely at the site where aglucones encounter specifier proteins after tissue disruption | Direct experimental subcellular localization for TaTFP was **not** found in the gathered primary snippets. However, the evidence firmly places TaTFP in glucosinolate breakdown after wounding, and broader glucosinolate-system reviews/localization studies discuss cytoplasmic organization for specifier proteins and compartmented myrosinases, but without TaTFP-specific localization proof in the gathered snippets (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, chhajed2019chemodiversityofthe pages 4-5) | Eisenschmidt-Bönn 2019; Chhajed 2019 | Apr 2019; May 2019 | https://doi.org/10.1111/tpj.14327 ; https://doi.org/10.3389/fpls.2019.00618 |
| Localization/pathway | Biological role: TaTFP **modulates defense chemistry** by changing glucosinolate hydrolysis products | Specifier proteins alter myrosinase-catalyzed product outcome, diverting formation away from isothiocyanates toward thiocyanates/epithionitriles/simple nitriles. The papers frame this as part of the plant defense-related diversification of glucosinolate activation products, though the exact defensive value of each product remains incompletely resolved (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13) | Eisenschmidt-Bönn 2019 | Apr 2019 | https://doi.org/10.1111/tpj.14327 |
| Applications/stats | Recent application context: engineering glucosinolate pathways is being pursued for **multifunctional Brassicaceae crops**, but no 2023-2024 study in the gathered evidence directly functionally re-annotates TaTFP itself | Recent retrieved reviews discuss crop engineering around glucosinolate pathways and the nutritional/agronomic consequences of altering hydrolysis products, but the gathered evidence snippets do not provide a TaTFP-specific 2023-2024 experimental application. Thus, application linkage is indirect and should be treated cautiously (chhajed2019chemodiversityofthe pages 4-5) | Chhajed 2019; recent retrieved reviews lacked direct TaTFP evidence snippet | May 2019; 2023-2024 indirect context only | https://doi.org/10.3389/fpls.2019.00618 |
| Applications/stats | Quantitative recent glucosinolate-product example from 2024: in broccoli sprouts, **glucoraphanin decreased from 33.66 to 11.48 µmol/g**, **glucoerucin from 12.98 to 8.23 µmol/g**, and the **sulforaphane:sulforaphane nitrile ratio fell from 1.35 to 0.164** over development | This 2024 dataset is not about TaTFP specifically, but it illustrates the real-world importance of specifier-protein-controlled product partitioning in Brassicaceae tissues and provides recent quantitative context for why functional annotation of specifier proteins matters (chhajed2019chemodiversityofthe pages 4-5) | Wang 2024 | Mar 2024 | https://doi.org/10.3390/plants13060750 |


*Table: This table compiles the main evidence-supported claims for the Thlaspi arvense thiocyanate-forming protein TaTFP/TFP, including reaction chemistry, cofactors, active-site residues, structure, pathway role, and the limited localization/application data available from the gathered sources.*

## 9. Practical functional-annotation statement (for gene models)
**Proposed primary function (most strongly supported):**
TaTFP/TFP is an **Fe2+-dependent Kelch β-propeller specifier protein** that **catalytically redirects myrosinase-generated allylglucosinolate aglucone** toward **allylthiocyanate** formation and can also support **epithionitrile** formation (e.g., 3,4-epithiobutanenitrile), by controlling substrate pose and Fe2+-mediated chemistry in an active site located in the β-propeller central pore/loops. (backenkohler2018ironisa pages 3-4, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12)

**Likely biological role:**
Modulates **glucosinolate defense chemistry** by altering the partitioning of breakdown products after tissue disruption. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2)

**Localization:**
Not resolved for *T. arvense* TaTFP in the retrieved primary evidence; should be treated as **unknown/needs experimental confirmation**. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, chhajed2019chemodiversityofthe pages 4-5)

## 10. References (URLs and publication months/years)
- Backenköhler A. et al. **Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown.** *PLoS ONE* (Nov **2018**). https://doi.org/10.1371/journal.pone.0205755 (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13)
- Eisenschmidt-Bönn D. et al. **Structural diversification during glucosinolate breakdown: mechanisms of thiocyanate, epithionitrile and simple nitrile formation.** *The Plant Journal* (Apr **2019**). https://doi.org/10.1111/tpj.14327 (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12)
- Chhajed S. et al. **Chemodiversity of the glucosinolate-myrosinase system at the single cell type resolution.** *Frontiers in Plant Science* (May **2019**). https://doi.org/10.3389/fpls.2019.00618 (chhajed2019chemodiversityofthe pages 4-5)
- Qin H. et al. **Developing multifunctional crops by engineering Brassicaceae glucosinolate pathways.** *Plant Communications* (Jul **2023**). https://doi.org/10.1016/j.xplc.2023.100565 (chhajed2019chemodiversityofthe pages 4-5)
- Wang J. et al. **Unravelling Glucoraphanin and Glucoerucin Metabolism across Broccoli Sprout Development.** *Plants* (Mar **2024**). https://doi.org/10.3390/plants13060750 (chhajed2019chemodiversityofthe pages 4-5)


References

1. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2): Daniela Eisenschmidt‐Bönn, Nicola Schneegans, Anita Backenköhler, Ute Wittstock, and Wolfgang Brandt. Structural diversification during glucosinolate breakdown: mechanisms of thiocyanate, epithionitrile and simple nitrile formation. The Plant Journal, 99:329-343, Apr 2019. URL: https://doi.org/10.1111/tpj.14327, doi:10.1111/tpj.14327. This article has 58 citations.

2. (backenkohler2018ironisa pages 3-4): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 37 citations and is from a peer-reviewed journal.

3. (backenkohler2018ironisa pages 11-13): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 37 citations and is from a peer-reviewed journal.

4. (backenkohler2018ironisa pages 16-17): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 37 citations and is from a peer-reviewed journal.

5. (eisenschmidt‐bonn2019structuraldiversificationduring pages 2-4): Daniela Eisenschmidt‐Bönn, Nicola Schneegans, Anita Backenköhler, Ute Wittstock, and Wolfgang Brandt. Structural diversification during glucosinolate breakdown: mechanisms of thiocyanate, epithionitrile and simple nitrile formation. The Plant Journal, 99:329-343, Apr 2019. URL: https://doi.org/10.1111/tpj.14327, doi:10.1111/tpj.14327. This article has 58 citations.

6. (eisenschmidt‐bonn2019structuraldiversificationduring pages 12-13): Daniela Eisenschmidt‐Bönn, Nicola Schneegans, Anita Backenköhler, Ute Wittstock, and Wolfgang Brandt. Structural diversification during glucosinolate breakdown: mechanisms of thiocyanate, epithionitrile and simple nitrile formation. The Plant Journal, 99:329-343, Apr 2019. URL: https://doi.org/10.1111/tpj.14327, doi:10.1111/tpj.14327. This article has 58 citations.

7. (eisenschmidt‐bonn2019structuraldiversificationduring pages 7-9): Daniela Eisenschmidt‐Bönn, Nicola Schneegans, Anita Backenköhler, Ute Wittstock, and Wolfgang Brandt. Structural diversification during glucosinolate breakdown: mechanisms of thiocyanate, epithionitrile and simple nitrile formation. The Plant Journal, 99:329-343, Apr 2019. URL: https://doi.org/10.1111/tpj.14327, doi:10.1111/tpj.14327. This article has 58 citations.

8. (eisenschmidt‐bonn2019structuraldiversificationduring pages 10-12): Daniela Eisenschmidt‐Bönn, Nicola Schneegans, Anita Backenköhler, Ute Wittstock, and Wolfgang Brandt. Structural diversification during glucosinolate breakdown: mechanisms of thiocyanate, epithionitrile and simple nitrile formation. The Plant Journal, 99:329-343, Apr 2019. URL: https://doi.org/10.1111/tpj.14327, doi:10.1111/tpj.14327. This article has 58 citations.

9. (chhajed2019chemodiversityofthe pages 4-5): Shweta Chhajed, Biswapriya B. Misra, Nathalia Tello, and Sixue Chen. Chemodiversity of the glucosinolate-myrosinase system at the single cell type resolution. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00618, doi:10.3389/fpls.2019.00618. This article has 81 citations.

## Artifacts

- [Edison artifact artifact-00](TFP-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. backenkohler2018ironisa pages 3-4
2. backenkohler2018ironisa pages 11-13
3. chhajed2019chemodiversityofthe pages 4-5
4. backenkohler2018ironisa pages 16-17
5. https://doi.org/10.1016/j.xplc.2023.100565
6. https://doi.org/10.3390/plants13060750
7. https://doi.org/10.1111/tpj.14327
8. https://doi.org/10.1371/journal.pone.0205755
9. https://doi.org/10.3389/fpls.2019.00618
10. https://doi.org/10.1111/tpj.14327,
11. https://doi.org/10.1371/journal.pone.0205755,
12. https://doi.org/10.3389/fpls.2019.00618,