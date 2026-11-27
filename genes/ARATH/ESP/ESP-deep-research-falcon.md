---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:29:48.064993'
end_time: '2026-09-30T06:44:08.074330'
duration_seconds: 860.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: ESP
  gene_symbol: ESP
  uniprot_accession: Q8RY71
  protein_description: 'RecName: Full=N-(sulfonatooxy)alkenimidothioic acid sulfate-lyase
    (epithionitrile-forming) {ECO:0000305}; EC=4.8.1.5 {ECO:0000269|PubMed:19224919,
    ECO:0000269|PubMed:23999604}; EC=4.8.1.6 {ECO:0000269|PubMed:11752388, ECO:0000269|PubMed:15845404,
    ECO:0000269|PubMed:22954730, ECO:0000269|PubMed:23999604}; AltName: Full=Epithionitrile-specifier
    protein {ECO:0000305}; AltName: Full=Epithiospecifier protein {ECO:0000303|PubMed:11752388,
    ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; Short=AtESP {ECO:0000303|PubMed:11752388,
    ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; AltName: Full=Protein
    EPITHIOSPECIFYING SENESCENCE REGULATOR {ECO:0000303|PubMed:17369373}; Short=AtESR
    {ECO:0000303|PubMed:17369373};'
  gene_info: Name=ESP {ECO:0000303|PubMed:11752388, ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336};
    Synonyms=ESR {ECO:0000303|PubMed:17369373}, TASTY {ECO:0000303|PubMed:17390109};
    OrderedLocusNames=At1g54040 {ECO:0000312|Araport:AT1G54040}; ORFNames=F15I1.12
    {ECO:0000312|EMBL:AAD25776.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Not specified in UniProt
  protein_domains: Kelch-typ_b-propeller. (IPR015915); Kelch_1. (IPR006652); Kelch_KLHDC2_KLHL20_DRC7
    (PF24681)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: ESP-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: ESP-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: ESP-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8RY71
- **Protein Description:** RecName: Full=N-(sulfonatooxy)alkenimidothioic acid sulfate-lyase (epithionitrile-forming) {ECO:0000305}; EC=4.8.1.5 {ECO:0000269|PubMed:19224919, ECO:0000269|PubMed:23999604}; EC=4.8.1.6 {ECO:0000269|PubMed:11752388, ECO:0000269|PubMed:15845404, ECO:0000269|PubMed:22954730, ECO:0000269|PubMed:23999604}; AltName: Full=Epithionitrile-specifier protein {ECO:0000305}; AltName: Full=Epithiospecifier protein {ECO:0000303|PubMed:11752388, ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; Short=AtESP {ECO:0000303|PubMed:11752388, ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; AltName: Full=Protein EPITHIOSPECIFYING SENESCENCE REGULATOR {ECO:0000303|PubMed:17369373}; Short=AtESR {ECO:0000303|PubMed:17369373};
- **Gene Information:** Name=ESP {ECO:0000303|PubMed:11752388, ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; Synonyms=ESR {ECO:0000303|PubMed:17369373}, TASTY {ECO:0000303|PubMed:17390109}; OrderedLocusNames=At1g54040 {ECO:0000312|Araport:AT1G54040}; ORFNames=F15I1.12 {ECO:0000312|EMBL:AAD25776.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Kelch-typ_b-propeller. (IPR015915); Kelch_1. (IPR006652); Kelch_KLHDC2_KLHL20_DRC7 (PF24681)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ESP" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ESP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ESP** (gene ID: ESP, UniProt: Q8RY71) in ARATH.

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
- **UniProt Accession:** Q8RY71
- **Protein Description:** RecName: Full=N-(sulfonatooxy)alkenimidothioic acid sulfate-lyase (epithionitrile-forming) {ECO:0000305}; EC=4.8.1.5 {ECO:0000269|PubMed:19224919, ECO:0000269|PubMed:23999604}; EC=4.8.1.6 {ECO:0000269|PubMed:11752388, ECO:0000269|PubMed:15845404, ECO:0000269|PubMed:22954730, ECO:0000269|PubMed:23999604}; AltName: Full=Epithionitrile-specifier protein {ECO:0000305}; AltName: Full=Epithiospecifier protein {ECO:0000303|PubMed:11752388, ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; Short=AtESP {ECO:0000303|PubMed:11752388, ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; AltName: Full=Protein EPITHIOSPECIFYING SENESCENCE REGULATOR {ECO:0000303|PubMed:17369373}; Short=AtESR {ECO:0000303|PubMed:17369373};
- **Gene Information:** Name=ESP {ECO:0000303|PubMed:11752388, ECO:0000303|PubMed:15845404, ECO:0000303|PubMed:18245336}; Synonyms=ESR {ECO:0000303|PubMed:17369373}, TASTY {ECO:0000303|PubMed:17390109}; OrderedLocusNames=At1g54040 {ECO:0000312|Araport:AT1G54040}; ORFNames=F15I1.12 {ECO:0000312|EMBL:AAD25776.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Kelch-typ_b-propeller. (IPR015915); Kelch_1. (IPR006652); Kelch_KLHDC2_KLHL20_DRC7 (PF24681)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ESP" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ESP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ESP** (gene ID: ESP, UniProt: Q8RY71) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: ESP Gene (At1g54040, UniProt Q8RY71) in Arabidopsis thaliana

## Gene Identity and Nomenclature

The ESP gene (locus At1g54040) encodes the epithiospecifier protein (EC 4.8.1.5 and 4.8.1.6), also known as **EPITHIOSPECIFYING SENESCENCE REGULATOR (ESR)** and **TASTY** (miao2007theantagonistfunction pages 1-3, koyama2013aregulatorycascade pages 9-10). This 341-amino-acid protein (UniProt Q8RY71) is a key modulator of glucosinolate metabolism and leaf senescence in Arabidopsis thaliana (wittstock2007tippingthescales pages 2-4, wittstock2007tippingthescales pages 1-2).

## Primary Enzymatic Function and Substrate Specificity

ESP is fundamentally a **product-specifying enzyme** rather than a primary glucosinolate hydrolase. It functions in close cooperation with myrosinase enzymes in the glucosinolate-myrosinase defense system (wittstock2007tippingthescales pages 2-4, witzel2019identificationandcharacterization pages 1-2, wittstock2007tippingthescales pages 4-5). The enzymatic mechanism proceeds through the following steps:

**Catalytic Mechanism:**
1. Myrosinase (thioglucosidase) first cleaves the thioglucosidic bond of intact glucosinolates, releasing glucose and generating an unstable thiohydroximate-O-sulfate aglucone intermediate (backenkohler2018ironisa pages 3-4, witzel2019identificationandcharacterization pages 1-2).

2. In the absence of ESP, this aglucone undergoes spontaneous Lossen-like rearrangement to form isothiocyanates (mustard oils), the default glucosinolate breakdown products (wittstock2007tippingthescales pages 1-2, kuchernig2012evolutionofspecifier pages 1-2).

3. ESP intercepts the unstable aglucone and redirects the reaction pathway toward alternative products, with product specificity determined by the glucosinolate side-chain structure (roman2020molecularmodelingof pages 7-8, roman2020molecularmodelingof pages 6-7, witzel2019identificationandcharacterization pages 1-2).

**Substrate Specificity:**
ESP acts on myrosinase-generated aglucones with distinct substrate preferences:

- **Alkenyl glucosinolates** (containing terminal C=C double bonds): ESP promotes formation of **epithionitriles** containing a three-membered thiirane ring. For example, 2-propenyl glucosinolate (sinigrin) is converted to 3,4-epithiobutyronitrile rather than 2-propenyl isothiocyanate (kissen2009nitrilespecifierproteinsinvolved pages 7-8, kissen2009nitrilespecifierproteinsinvolved pages 5-6, kissen2009nitrilespecifierproteinsinvolved pages 6-7, kissen2009nitrilespecifierproteinsinvolved pages 1-1).

- **Non-alkenyl glucosinolates** (alkyl, hydroxyalkyl, and indole glucosinolates): ESP directs formation of **simple nitriles** lacking the thiirane ring (roman2020molecularmodelingof pages 7-8, roman2020molecularmodelingof pages 6-7).

**Iron Cofactor Requirement:**
ESP is a non-heme iron protein requiring ferrous iron (Fe²⁺) for full catalytic activity (backenkohler2018ironisa pages 11-13). The Fe²⁺ cofactor is centrally bound and essential for epithionitrile formation through proposed sulfur transfer to the terminal double bond (backenkohler2018ironisa pages 3-4, witzel2019identificationandcharacterization pages 1-2, backenkohler2018ironisa pages 1-3). Purified recombinant ESP contains approximately 0.4–0.6 mol iron per mol protein monomer (backenkohler2018ironisa pages 7-9). EDTA chelation abolishes specifier activity, which is restored by excess Fe²⁺ (backenkohler2018ironisa pages 11-13).

## Structural Characterization

ESP adopts a **Kelch-repeat, six-bladed β-propeller** fold (backenkohler2018ironisa pages 3-4, roman2020molecularmodelingof pages 6-7). The putative iron-binding site resides in the central pore of this β-propeller structure and is defined by a conserved **EXXXDXXXH** amino acid motif (backenkohler2018ironisa pages 11-13, backenkohler2018ironisa pages 9-11). In AtESP, residues **Glu260 (E260)** and **Asp264 (D264)** have been experimentally validated as functionally critical for iron binding—substitution with glutamine and asparagine, respectively, strongly diminishes ESP activity (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 4-5). The histidine residue in this motif provides the third predicted iron ligand, forming an approximately bipyramidal coordination geometry with the aglucone thiolate and water molecules (backenkohler2018ironisa pages 9-11).

Unlike several Arabidopsis nitrile-specifier proteins (NSPs), ESP does not contain an N-terminal jacalin-related lectin domain, consisting primarily of the Kelch β-propeller structure (roman2020molecularmodelingof pages 6-7).

## Subcellular Localization and Tissue Distribution

| Feature | Evidence-based summary | Evidence |
|---|---|---|
| Subcellular localization | ESP is primarily cytosolic, consistent with its metabolic role, but is also detected in the nucleus. | (witzel2019identificationandcharacterization pages 9-11, miao2007theantagonistfunction pages 3-4, roman2020molecularmodelingof pages 7-8) |
| Tissue distribution | In aerial organs, ESP accumulates predominantly in epidermal cells, except in anthers. It is also detected in glucosinolate-rich S-cells of stems but not corresponding leaf S-cells. | (wittstock2007tippingthescales pages 2-4, roman2020molecularmodelingof pages 6-7) |
| Organs with highest activity | In the functional Landsberg erecta accession, the highest measured ESP activity occurs in pre-bolting rosette leaves and flowers; protein and activity are undetectable in roots despite trace root transcripts. | (roman2020molecularmodelingof pages 6-7) |
| Cellular function in cytosol | ESP acts with myrosinase on short-lived glucosinolate aglucones, redirecting product formation away from isothiocyanates toward epithionitriles from suitable alkenyl substrates or simple nitriles from other substrates. | (witzel2019identificationandcharacterization pages 1-2, roman2020molecularmodelingof pages 7-8, wittstock2007tippingthescales pages 2-4) |
| Cellular function in nucleus | Nuclear ESP/ESR binds the senescence-promoting transcription factor WRKY53 and inhibits its DNA-binding and reporter activity, thereby acting as a negative regulator of leaf senescence. | (miao2007theantagonistfunction pages 1-3, miao2007theantagonistfunction pages 7-9, miao2007theantagonistfunction pages 6-7) |
| Nuclear transport | ESP/ESR nuclear accumulation is WRKY53 dependent: it is excluded from the nucleus in WRKY53-knockout protoplasts, whereas coexpression with WRKY53 produces nuclear localization and interaction signals. | (miao2007theantagonistfunction pages 3-4, miao2007theantagonistfunction pages 9-10) |
| Ecotype variation | Functional ESP protein and activity occur in Landsberg erecta (Ler), whereas Columbia-0 (Col-0) lacks detectable ESP activity; a promoter-region deletion has been proposed to underlie the Col-0 defect. | (roman2020molecularmodelingof pages 6-7) |


*Table: This table integrates subcellular, cell-type, organ-level, and accession-specific evidence for Arabidopsis ESP. It distinguishes its cytosolic glucosinolate-specifier function from its WRKY53-associated nuclear role in senescence.*

ESP exhibits **dual subcellular localization** with distinct functions in each compartment:

**Cytosolic Function:**
ESP is primarily localized to the cytosol, where it performs its metabolic role as a glucosinolate-myrosinase system component (witzel2019identificationandcharacterization pages 9-11, roman2020molecularmodelingof pages 7-8). In the cytoplasm, ESP intercepts unstable glucosinolate aglucones and specifies product formation toward epithionitriles or nitriles depending on substrate structure (witzel2019identificationandcharacterization pages 1-2, roman2020molecularmodelingof pages 7-8, wittstock2007tippingthescales pages 2-4).

**Nuclear Function:**
ESP is also detected in the nucleus, where it serves a regulatory role in leaf senescence (miao2007theantagonistfunction pages 3-4, roman2020molecularmodelingof pages 7-8). Nuclear localization of ESP is WRKY53-dependent: in WRKY53-knockout protoplasts, ESP remains exclusively cytoplasmic, whereas coexpression with WRKY53 produces nuclear accumulation (miao2007theantagonistfunction pages 3-4, miao2007theantagonistfunction pages 9-10). This suggests WRKY53 actively recruits or facilitates ESP nuclear import.

**Tissue-Specific Expression:**
At the cellular level, ESP accumulates predominantly in **epidermal cells of above-ground organs**, with the notable exception of anthers (wittstock2007tippingthescales pages 2-4, roman2020molecularmodelingof pages 6-7). ESP is also detected in glucosinolate-containing S-cells of stems but not in corresponding S-cells of leaves (roman2020molecularmodelingof pages 6-7). The highest measured ESP activity occurs in **pre-bolting rosette leaves** and **flowers** in the functional Landsberg erecta (Ler) accession (roman2020molecularmodelingof pages 6-7). Despite trace transcript levels in roots, ESP protein and activity are undetectable in this organ, suggesting post-transcriptional regulation (roman2020molecularmodelingof pages 6-7).

## Role in Glucosinolate Metabolism Pathway

| Feature | ESP (At1g54040; UniProt Q8RY71) annotation | Evidence |
|---|---|---|
| Enzyme classification | **EC 4.8.1.5** and **EC 4.8.1.6**; a sulfate-lyase/product-specifier associated with glucosinolate breakdown rather than the thioglucosidase that initiates hydrolysis. | UniProt Q8RY71; ESP acts downstream of myrosinase on its unstable product (wittstock2007tippingthescales pages 2-4, kuchernig2012evolutionofspecifier pages 1-2) |
| Primary function | Redirects the unstable glucosinolate aglucone generated by myrosinase away from its default Lossen-like rearrangement to an isothiocyanate and toward nitrile-class products. ESP therefore specifies product identity rather than cleaving intact glucosinolate. | (witzel2019identificationandcharacterization pages 1-2, wittstock2007tippingthescales pages 1-2, wittstock2007tippingthescales pages 4-5) |
| Substrate specificity | Acts on myrosinase-generated aglucones. **Alkenyl glucosinolates** bearing a suitable terminal C=C bond support epithionitrile formation; aglucones from **alkyl, hydroxyalkyl, and indole glucosinolates** can be directed toward simple nitriles. Allyl/2-propenyl glucosinolate is an experimentally demonstrated substrate. | (kissen2009nitrilespecifierproteinsinvolved pages 7-8, roman2020molecularmodelingof pages 7-8, roman2020molecularmodelingof pages 6-7) |
| Products formed | Produces **epithionitriles from suitable alkenyl glucosinolates** and **simple nitriles from non-alkenyl substrates**. With 2-propenyl glucosinolate, recombinant AtESP promotes formation of **3,4-epithiobutyronitrile** instead of 2-propenyl isothiocyanate. | (kissen2009nitrilespecifierproteinsinvolved pages 5-6, kissen2009nitrilespecifierproteinsinvolved pages 1-1, kuchernig2012evolutionofspecifier pages 1-2) |
| Catalytic mechanism | Myrosinase first removes glucose, yielding a short-lived thiohydroximate-*O*-sulfate aglucone. ESP is proposed to bind and orient this intermediate so that glucosinolate-derived sulfur is transferred intramolecularly to the terminal alkene, creating the epithionitrile’s three-membered thiirane ring. Fe²⁺ likely coordinates the aglucone thiolate and enforces productive geometry; the complete chemical sequence remains unresolved. | (backenkohler2018ironisa pages 3-4, wittstock2007tippingthescales pages 4-5, witzel2019identificationandcharacterization pages 1-2) |
| Cofactor requirement | **Ferrous iron (Fe²⁺)** is the favored, centrally bound non-heme cofactor. Chelation reduces or abolishes specifier activity, excess Fe²⁺ restores it, and purified AtESP contains approximately **0.4–0.6 mol iron per mol protein monomer**. | (backenkohler2018ironisa pages 11-13, backenkohler2018ironisa pages 7-9) |
| Iron-binding site | A conserved **EXXXDXXXH** motif lies in the β-propeller’s central pore. In AtESP, **Glu260 (E260)** and **Asp264 (D264)** are functionally supported iron-site residues; substitution strongly reduces activity. The motif histidine—predicted as the third ligand—is separated from D264 by three residues, although its AtESP-specific coordination has less direct experimental support than E260/D264. | (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13, backenkohler2018ironisa pages 4-5) |
| Structural domain | A **Kelch-repeat, six-bladed β-propeller** protein. The putative Fe²⁺-binding/catalytic site occupies the central pore, while surrounding loops help determine aglucone positioning and hence epithionitrile-versus-nitrile product specificity. Unlike several Arabidopsis NSPs, AtESP is not described as carrying an N-terminal jacalin-related lectin domain. | (backenkohler2018ironisa pages 3-4, roman2020molecularmodelingof pages 6-7) |


*Table: Summary of the experimentally supported reaction, substrate and product specificity, iron dependence, and Kelch β-propeller architecture of Arabidopsis ESP. The table also distinguishes established findings from mechanistic details that remain provisional.*

ESP functions as a critical node in the **glucosinolate-myrosinase defense system**, a two-component activated chemical defense characteristic of the Brassicales (kissen2009nitrilespecifierproteinsinvolved pages 1-1, kuchernig2012evolutionofspecifier pages 1-2, wittstock2007tippingthescales pages 4-5). This system operates through strict spatial separation:

**Cellular Compartmentation:**
In intact plant tissue, glucosinolates are stored in vacuoles of sulfur-rich S-cells, while myrosinases reside in vacuoles of adjacent myrosin cells and guard cells (witzel2019identificationandcharacterization pages 1-2). ESP is localized in the cytosol of specific cell types, positioned to intercept the products of myrosinase-glucosinolate mixing after tissue disruption.

**Pathway Position:**
Upon tissue damage by herbivores or pathogens, glucosinolates and myrosinases mix, initiating the defense cascade:

1. **Glucosinolate hydrolysis:** Myrosinase cleaves the thioglucosidic bond, producing glucose and an unstable aglucone (wittstock2007tippingthescales pages 2-4, backenkohler2018ironisa pages 3-4).

2. **Product specification by ESP:** ESP binds the short-lived aglucone and determines product fate through Fe²⁺-dependent chemistry (wittstock2007tippingthescales pages 4-5, witzel2019identificationandcharacterization pages 1-2):
   - For alkenyl substrates: sulfur transfer to the terminal alkene creates the thiirane ring of epithionitriles
   - For non-alkenyl substrates: formation of simple nitriles

3. **Metabolic diversification:** By redirecting aglucone fate, ESP reduces isothiocyanate formation and increases production of alternative defensive compounds with distinct biological properties (witzel2019identificationandcharacterization pages 1-2, wittstock2007tippingthescales pages 2-4).

The iron cofactor is specifically required for epithionitrile formation, likely by positioning the aglucone thiolate and stabilizing reactive conformations needed for sulfur insertion into the double bond (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 1-3).

## Biological Roles and Regulatory Networks

| Aspect | ESP role or regulatory mechanism | Evidence |
|---|---|---|
| Primary biological role | Diversifies damage-activated chemical defense by redirecting myrosinase-generated glucosinolate aglucones away from default isothiocyanates and toward epithionitriles or simple nitriles. | Biochemical and evolutionary studies identify ESP as a product-specifying component of the glucosinolate–myrosinase system. (kissen2009nitrilespecifierproteinsinvolved pages 1-1, kuchernig2012evolutionofspecifier pages 1-2) |
| Secondary biological role | Acts as a negative regulator of leaf senescence, linking glucosinolate-associated defense, aging, and stress signaling. | ESP/ESR overexpression delays senescence, whereas loss of ESP/ESR accelerates it. (miao2007theantagonistfunction pages 1-3, koyama2013aregulatorycascade pages 9-10) |
| Defense mechanism | Changes the toxicity, volatility, and deterrent properties of glucosinolate breakdown mixtures by decreasing isothiocyanate formation and increasing nitrile or epithionitrile formation; ecological effects are substrate- and herbivore-dependent rather than universally protective. | ESP-dependent product selection affects plant–insect interactions, although direct defense by simple nitriles is not consistently supported. (wittstock2007tippingthescales pages 2-4, burow2009thegeneticbasis pages 1-2, kuchernig2012evolutionofspecifier pages 1-2) |
| Senescence mechanism | Physically associates with WRKY53 in the nucleus and inhibits WRKY53 DNA binding and reporter activity, thereby restraining transcription of senescence-promoting programs. | Supported by yeast two-hybrid, coimmunoprecipitation, bimolecular fluorescence complementation, reporter, EMSA, and genetic epistasis evidence. (miao2007theantagonistfunction pages 1-3, miao2007theantagonistfunction pages 7-9, miao2007theantagonistfunction pages 3-4, miao2007theantagonistfunction pages 6-7) |
| Hormonal regulation | ESP/ESR is induced through jasmonic-acid signaling involving JAR1 and COI1 and is opposed by salicylic-acid signaling; WRKY53 generally shows the reciprocal JA/SA response. | This antagonistic hormonal regulation connects ESP/ESR–WRKY53 activity with defense–senescence crosstalk. (miao2007theantagonistfunction pages 3-4, miao2007theantagonistfunction pages 4-5) |
| Transcriptional regulation | Class II ethylene-response-factor repressors AtERF4 and AtERF8 directly repress ESP/ESR expression during aging, relieving ESP-mediated inhibition of WRKY53 and promoting senescence. | ERF overexpression lowers ESP/ESR expression, while the *erf4 erf8* double mutant elevates it and displays delayed senescence; chromatin-immunoprecipitation supports direct targeting. (koyama2013aregulatorycascade pages 9-10, koyama2013aregulatorycascade pages 6-9, koyama2013aregulatorycascade pages 1-2) |
| Gene synonyms | **ESP** denotes EPITHIOSPECIFIER PROTEIN; **ESR** denotes EPITHIOSPECIFYING SENESCENCE REGULATOR; **TASTY** is another synonym for the same *Arabidopsis* locus, At1g54040. | The biochemical and senescence literature uses ESP/ESR for the same gene product; later regulatory work also associates the locus with TASTY. (miao2007theantagonistfunction pages 1-3, koyama2013aregulatorycascade pages 9-10) |
| Mutant phenotypes | Loss of ESP/ESR accelerates leaf senescence and removes or reduces ESP-dependent diversion of glucosinolate breakdown toward epithionitriles or nitriles, shifting the hydrolysis-product profile toward competing products such as isothiocyanates. | The senescence phenotype is genetically demonstrated; the metabolic consequence follows from ESP’s experimentally established product-specifier activity and accession-dependent absence of ESP activity. (miao2007theantagonistfunction pages 1-3, kissen2009nitrilespecifierproteinsinvolved pages 5-6, roman2020molecularmodelingof pages 6-7) |


*Table: This table summarizes the experimentally supported defense and senescence functions of Arabidopsis ESP/ESR/TASTY, including its hormonal and transcriptional regulation. It distinguishes established mechanisms from ecological effects that remain context dependent.*

ESP exhibits **dual biological functions** reflecting its cytoplasmic and nuclear localizations:

### 1. Chemical Defense Modulation

In the cytoplasm, ESP shapes the chemical defense response by diversifying glucosinolate breakdown products (kissen2009nitrilespecifierproteinsinvolved pages 1-1, kuchernig2012evolutionofspecifier pages 1-2). By promoting epithionitrile and nitrile formation at the expense of isothiocyanates, ESP alters the toxicity, volatility, and deterrent properties of defensive compounds encountered by herbivores (wittstock2007tippingthescales pages 2-4, wittstock2007tippingthescales pages 4-5).

However, the defensive effectiveness of ESP-derived products appears context-dependent. Feeding assays with generalist herbivores did not consistently support a direct defensive role for simple nitriles (wittstock2007tippingthescales pages 2-4, burow2009thegeneticbasis pages 1-2). Instead, volatile simple nitriles may function in **indirect defense** by serving as airborne signals that attract natural enemies of herbivores (wittstock2007tippingthescales pages 2-4). The ecological roles of epithionitriles, with their reactive thiirane rings, remain incompletely characterized (wittstock2007tippingthescales pages 2-4, kuchernig2012evolutionofspecifier pages 1-2).

### 2. Leaf Senescence Regulation

In the nucleus, ESP acts as a **negative regulator of leaf senescence** through direct interaction with the transcription factor WRKY53 (miao2007theantagonistfunction pages 1-3, miao2007theantagonistfunction pages 7-9). Multiple experimental approaches establish this interaction:

**Molecular Evidence:**
- Yeast two-hybrid screening identified ESP/ESR as a WRKY53-interacting protein (miao2007theantagonistfunction pages 3-4)
- In vitro coimmunoprecipitation confirmed physical association between GST-tagged ESP and His-tagged WRKY53 (miao2007theantagonistfunction pages 1-3)
- Bimolecular fluorescence complementation demonstrated nuclear interaction in vivo (miao2007theantagonistfunction pages 3-4)
- WRKY53-dependent nuclear recruitment of ESP was demonstrated by localization studies in knockout backgrounds (miao2007theantagonistfunction pages 9-10)

**Functional Mechanism:**
ESP inhibits WRKY53 DNA-binding activity in electrophoretic mobility shift assays and reduces WRKY53-dependent reporter gene expression (miao2007theantagonistfunction pages 7-9, miao2007theantagonistfunction pages 6-7). By restraining WRKY53 transcriptional activity, ESP delays the expression of senescence-associated genes and prolongs leaf lifespan (miao2007theantagonistfunction pages 1-3, koyama2013aregulatorycascade pages 9-10).

**Genetic Evidence:**
- ESP/ESR overexpression delays senescence, while esp/esr knockout accelerates it (miao2007theantagonistfunction pages 1-3, miao2007theantagonistfunction pages 4-5)
- WRKY53 overexpression accelerates senescence, while wrky53 knockout delays it (miao2007theantagonistfunction pages 5-6, miao2007theantagonistfunction pages 4-5)
- Epistasis analysis shows ESP overexpression has no additive effect in the wrky53 knockout background, indicating ESP acts through WRKY53 (miao2007theantagonistfunction pages 5-6)
- ESP overexpression in WRKY53-overexpressing plants restores wild-type senescence timing (miao2007theantagonistfunction pages 5-6, miao2007theantagonistfunction pages 4-5)

### Hormonal and Transcriptional Regulation

ESP expression is subject to complex hormonal and transcriptional control that integrates defense, stress, and developmental signals:

**Hormonal Regulation:**
ESP/ESR is **induced by jasmonic acid (JA)** through JAR1- and COI1-dependent signaling and is **repressed by salicylic acid (SA)** (miao2007theantagonistfunction pages 3-4, miao2007theantagonistfunction pages 4-5). WRKY53 shows reciprocal hormonal regulation: SA induces WRKY53, while JA represses it (miao2007theantagonistfunction pages 3-4). This antagonistic JA/SA control positions the ESP-WRKY53 module at the intersection of pathogen defense and senescence signaling (miao2007theantagonistfunction pages 1-3, miao2007theantagonistfunction pages 3-4).

**Transcriptional Regulation:**
Class II ethylene response factor (ERF) transcriptional repressors **AtERF4** and **AtERF8** directly repress ESP/ESR expression during aging (koyama2013aregulatorycascade pages 9-10, koyama2013aregulatorycascade pages 6-9, koyama2013aregulatorycascade pages 1-2). Chromatin immunoprecipitation demonstrates that AtERF4 and AtERF8 bind ESP/ESR regulatory regions (koyama2013aregulatorycascade pages 9-10). As plants age:

1. AtERF4 and AtERF8 accumulate and become active at both transcriptional and post-translational levels (koyama2013aregulatorycascade pages 10-11)
2. These ERFs repress ESP/ESR transcription (koyama2013aregulatorycascade pages 6-9)
3. Reduced ESP/ESR relieves inhibition of WRKY53 (koyama2013aregulatorycascade pages 9-10)
4. Activated WRKY53 promotes senescence-associated gene expression (koyama2013aregulatorycascade pages 10-11)

The *erf4 erf8* double mutant exhibits elevated ESP/ESR expression, delayed senescence, and reduced activation of WRKY30, WRKY53, and WRKY75 (koyama2013aregulatorycascade pages 6-9). Conversely, AtERF4 or AtERF8 overexpression reduces ESP/ESR expression and causes precocious senescence (koyama2013aregulatorycascade pages 9-10, koyama2013aregulatorycascade pages 1-2).

## Genetic Variation and Ecotype-Specific Activity

Functional ESP activity varies significantly among Arabidopsis ecotypes (roman2020molecularmodelingof pages 6-7). The **Landsberg erecta (Ler)** accession possesses functional ESP protein and activity, whereas **Columbia-0 (Col-0)** lacks detectable ESP activity despite expressing related nitrile-specifier proteins (roman2020molecularmodelingof pages 6-7). A 10-bp deletion in an ESP promoter transcription factor binding site has been proposed to underlie the Col-0 deficiency (roman2020molecularmodelingof pages 6-7). This natural variation affects both glucosinolate breakdown product profiles and senescence regulation, illustrating the physiological importance of ESP in ecotype-specific adaptation.

## Evolutionary Context

ESP belongs to a small family of specifier proteins in Arabidopsis that evolved to diversify glucosinolate breakdown products (kuchernig2012evolutionofspecifier pages 1-2, burow2009thegeneticbasis pages 1-2). Phylogenetic analyses indicate that **nitrile-specifier proteins (NSPs) represent the ancestral specifier activity**, with ESP (epithiospecifier) activity evolving from NSPs before the radiation of core Brassicaceae (kuchernig2012evolutionofspecifier pages 1-2). Arabidopsis possesses one ESP and five NSP genes (NSP1-NSP5), which promote simple nitrile but not epithionitrile formation (burow2009thegeneticbasis pages 1-2). 

Notably, herbivore-induced simple nitrile formation in Arabidopsis Col-0 rosette leaves is mediated primarily by **AtNSP1** rather than ESP (burow2009thegeneticbasis pages 1-2). AtNSP1 expression is strongly induced by herbivory, and nsp1 mutants lack both constitutive and herbivore-induced simple nitrile formation (burow2009thegeneticbasis pages 1-2, roman2020molecularmodelingof pages 7-8). This functional partitioning suggests that ESP's unique epithiospecifier activity provides selective advantages in specific ecological contexts, potentially through effects on specialized herbivores or as part of the senescence regulatory network.

## Current Understanding and Research Perspectives

The body of research on ESP/ESR/TASTY reveals a multifunctional protein with compartment-specific roles. Its **primary biochemical function** as an Fe²⁺-dependent glucosinolate product specifier is well established through recombinant protein studies, mutational analyses of iron-binding residues, and structural modeling (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13, backenkohler2018ironisa pages 4-5). The proposed catalytic mechanism involving Fe²⁺-mediated sulfur transfer to create epithionitrile rings is supported by substrate-specificity studies and iron-dependence experiments, though the complete chemical pathway remains to be fully elucidated (wittstock2007tippingthescales pages 4-5, witzel2019identificationandcharacterization pages 1-2).

The **nuclear regulatory function** is equally well documented through multiple complementary approaches demonstrating physical interaction with WRKY53, functional inhibition of WRKY53 DNA binding, and genetic epistasis establishing ESP as an upstream negative regulator of WRKY53-dependent senescence (miao2007theantagonistfunction pages 1-3, miao2007theantagonistfunction pages 4-5, miao2007theantagonistfunction pages 7-9, miao2007theantagonistfunction pages 3-4, miao2007theantagonistfunction pages 6-7). This dual functionality positions ESP at the interface of chemical defense and developmental aging, with hormonal regulation by JA and SA and transcriptional control by class II ERFs providing environmental responsiveness (miao2007theantagonistfunction pages 1-3, koyama2013aregulatorycascade pages 9-10, miao2007theantagonistfunction pages 3-4, koyama2013aregulatorycascade pages 6-9).

Recent work (2020-2024) has expanded understanding of specifier protein substrate specificity, particularly for indole glucosinolates, and has begun to characterize the rhizosphere and ecological implications of glucosinolate breakdown product diversity (roman2020molecularmodelingof pages 7-8, chroston2024formationofglucosinolatederived pages 107-109). However, key questions remain regarding the precise ecological roles of epithionitriles, the structural basis for ESP's substrate recognition, and the regulatory mechanisms controlling ESP's cytoplasmic versus nuclear partitioning beyond WRKY53-dependent recruitment.

## Summary

ESP (At1g54040, Q8RY71) is a 341-amino-acid Fe²⁺-dependent Kelch β-propeller protein that serves dual functions in Arabidopsis thaliana. In the cytoplasm, it acts as a product specifier in the glucosinolate-myrosinase defense system, redirecting unstable glucosinolate aglucones from isothiocyanates toward epithionitriles (from alkenyl glucosinolates with terminal double bonds) or simple nitriles (from non-alkenyl substrates). This Fe²⁺-catalyzed activity requires iron coordination by residues E260 and D264 in the protein's central pore and diversifies defensive chemistry. In the nucleus, ESP interacts with the WRKY53 transcription factor, inhibiting its DNA-binding activity and thereby acting as a negative regulator of leaf senescence. ESP expression is induced by jasmonic acid, repressed by salicylic acid and class II ERF transcriptional repressors, and varies among ecotypes. This dual functionality makes ESP a key integrator of chemical defense, developmental senescence, and hormonal signaling in Arabidopsis.

References

1. (miao2007theantagonistfunction pages 1-3): Ying Miao and Ulrike Zentgraf. The antagonist function of arabidopsis wrky53 and esr/esp in leaf senescence is modulated by the jasmonic and salicylic acid equilibrium. The Plant Cell Online, 19:819-830, Mar 2007. URL: https://doi.org/10.1105/tpc.106.042705, doi:10.1105/tpc.106.042705. This article has 417 citations.

2. (koyama2013aregulatorycascade pages 9-10): Tomotsugu Koyama, Haruka Nii, Nobutaka Mitsuda, Masaru Ohta, Sakihito Kitajima, Masaru Ohme-Takagi, and Fumihiko Sato. A regulatory cascade involving class ii ethylene response factor transcriptional repressors operates in the progression of leaf senescence. Plant Physiology, 162:991-1005, Apr 2013. URL: https://doi.org/10.1104/pp.113.218115, doi:10.1104/pp.113.218115. This article has 152 citations and is from a highest quality peer-reviewed journal.

3. (wittstock2007tippingthescales pages 2-4): Ute Wittstock and Meike Burow. Tipping the scales ‐ specifier proteins in glucosinolate hydrolysis. IUBMB Life, 59:744-751, Jan 2007. URL: https://doi.org/10.1080/15216540701736277, doi:10.1080/15216540701736277. This article has 127 citations and is from a peer-reviewed journal.

4. (wittstock2007tippingthescales pages 1-2): Ute Wittstock and Meike Burow. Tipping the scales ‐ specifier proteins in glucosinolate hydrolysis. IUBMB Life, 59:744-751, Jan 2007. URL: https://doi.org/10.1080/15216540701736277, doi:10.1080/15216540701736277. This article has 127 citations and is from a peer-reviewed journal.

5. (witzel2019identificationandcharacterization pages 1-2): Katja Witzel, Marua Abu Risha, Philip Albers, Frederik Börnke, and Franziska S. Hanschen. Identification and characterization of three epithiospecifier protein isoforms in brassica oleracea. Frontiers in Plant Science, Dec 2019. URL: https://doi.org/10.3389/fpls.2019.01552, doi:10.3389/fpls.2019.01552. This article has 43 citations.

6. (wittstock2007tippingthescales pages 4-5): Ute Wittstock and Meike Burow. Tipping the scales ‐ specifier proteins in glucosinolate hydrolysis. IUBMB Life, 59:744-751, Jan 2007. URL: https://doi.org/10.1080/15216540701736277, doi:10.1080/15216540701736277. This article has 127 citations and is from a peer-reviewed journal.

7. (backenkohler2018ironisa pages 3-4): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

8. (kuchernig2012evolutionofspecifier pages 1-2): Jennifer-Christin Kuchernig, Meike Burow, and U. Wittstock. Evolution of specifier proteins in glucosinolate-containing plants. BMC Evolutionary Biology, 12:127-127, Jul 2012. URL: https://doi.org/10.1186/1471-2148-12-127, doi:10.1186/1471-2148-12-127. This article has 112 citations and is from a domain leading peer-reviewed journal.

9. (roman2020molecularmodelingof pages 7-8): Juan Román, Dorian González, Mario Inostroza-Ponta, and Andrea Mahn. Molecular modeling of epithiospecifier and nitrile-specifier proteins of broccoli and their interaction with aglycones. Molecules, 25:772, Feb 2020. URL: https://doi.org/10.3390/molecules25040772, doi:10.3390/molecules25040772. This article has 23 citations.

10. (roman2020molecularmodelingof pages 6-7): Juan Román, Dorian González, Mario Inostroza-Ponta, and Andrea Mahn. Molecular modeling of epithiospecifier and nitrile-specifier proteins of broccoli and their interaction with aglycones. Molecules, 25:772, Feb 2020. URL: https://doi.org/10.3390/molecules25040772, doi:10.3390/molecules25040772. This article has 23 citations.

11. (kissen2009nitrilespecifierproteinsinvolved pages 7-8): Ralph Kissen and Atle M. Bones. Nitrile-specifier proteins involved in glucosinolate hydrolysis in arabidopsis thaliana*. Journal of Biological Chemistry, 284:12057-12070, May 2009. URL: https://doi.org/10.1074/jbc.m807500200, doi:10.1074/jbc.m807500200. This article has 176 citations and is from a domain leading peer-reviewed journal.

12. (kissen2009nitrilespecifierproteinsinvolved pages 5-6): Ralph Kissen and Atle M. Bones. Nitrile-specifier proteins involved in glucosinolate hydrolysis in arabidopsis thaliana*. Journal of Biological Chemistry, 284:12057-12070, May 2009. URL: https://doi.org/10.1074/jbc.m807500200, doi:10.1074/jbc.m807500200. This article has 176 citations and is from a domain leading peer-reviewed journal.

13. (kissen2009nitrilespecifierproteinsinvolved pages 6-7): Ralph Kissen and Atle M. Bones. Nitrile-specifier proteins involved in glucosinolate hydrolysis in arabidopsis thaliana*. Journal of Biological Chemistry, 284:12057-12070, May 2009. URL: https://doi.org/10.1074/jbc.m807500200, doi:10.1074/jbc.m807500200. This article has 176 citations and is from a domain leading peer-reviewed journal.

14. (kissen2009nitrilespecifierproteinsinvolved pages 1-1): Ralph Kissen and Atle M. Bones. Nitrile-specifier proteins involved in glucosinolate hydrolysis in arabidopsis thaliana*. Journal of Biological Chemistry, 284:12057-12070, May 2009. URL: https://doi.org/10.1074/jbc.m807500200, doi:10.1074/jbc.m807500200. This article has 176 citations and is from a domain leading peer-reviewed journal.

15. (backenkohler2018ironisa pages 11-13): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

16. (backenkohler2018ironisa pages 1-3): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

17. (backenkohler2018ironisa pages 7-9): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

18. (backenkohler2018ironisa pages 9-11): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

19. (backenkohler2018ironisa pages 4-5): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

20. (witzel2019identificationandcharacterization pages 9-11): Katja Witzel, Marua Abu Risha, Philip Albers, Frederik Börnke, and Franziska S. Hanschen. Identification and characterization of three epithiospecifier protein isoforms in brassica oleracea. Frontiers in Plant Science, Dec 2019. URL: https://doi.org/10.3389/fpls.2019.01552, doi:10.3389/fpls.2019.01552. This article has 43 citations.

21. (miao2007theantagonistfunction pages 3-4): Ying Miao and Ulrike Zentgraf. The antagonist function of arabidopsis wrky53 and esr/esp in leaf senescence is modulated by the jasmonic and salicylic acid equilibrium. The Plant Cell Online, 19:819-830, Mar 2007. URL: https://doi.org/10.1105/tpc.106.042705, doi:10.1105/tpc.106.042705. This article has 417 citations.

22. (miao2007theantagonistfunction pages 7-9): Ying Miao and Ulrike Zentgraf. The antagonist function of arabidopsis wrky53 and esr/esp in leaf senescence is modulated by the jasmonic and salicylic acid equilibrium. The Plant Cell Online, 19:819-830, Mar 2007. URL: https://doi.org/10.1105/tpc.106.042705, doi:10.1105/tpc.106.042705. This article has 417 citations.

23. (miao2007theantagonistfunction pages 6-7): Ying Miao and Ulrike Zentgraf. The antagonist function of arabidopsis wrky53 and esr/esp in leaf senescence is modulated by the jasmonic and salicylic acid equilibrium. The Plant Cell Online, 19:819-830, Mar 2007. URL: https://doi.org/10.1105/tpc.106.042705, doi:10.1105/tpc.106.042705. This article has 417 citations.

24. (miao2007theantagonistfunction pages 9-10): Ying Miao and Ulrike Zentgraf. The antagonist function of arabidopsis wrky53 and esr/esp in leaf senescence is modulated by the jasmonic and salicylic acid equilibrium. The Plant Cell Online, 19:819-830, Mar 2007. URL: https://doi.org/10.1105/tpc.106.042705, doi:10.1105/tpc.106.042705. This article has 417 citations.

25. (burow2009thegeneticbasis pages 1-2): Meike Burow, Anja Losansky, René Müller, Antje Plock, Daniel J. Kliebenstein, and Ute Wittstock. The genetic basis of constitutive and herbivore-induced esp-independent nitrile formation in arabidopsis. Plant Physiology, 149(1):561-574, Nov 2009. URL: https://doi.org/10.1104/pp.108.130732, doi:10.1104/pp.108.130732. This article has 190 citations and is from a highest quality peer-reviewed journal.

26. (miao2007theantagonistfunction pages 4-5): Ying Miao and Ulrike Zentgraf. The antagonist function of arabidopsis wrky53 and esr/esp in leaf senescence is modulated by the jasmonic and salicylic acid equilibrium. The Plant Cell Online, 19:819-830, Mar 2007. URL: https://doi.org/10.1105/tpc.106.042705, doi:10.1105/tpc.106.042705. This article has 417 citations.

27. (koyama2013aregulatorycascade pages 6-9): Tomotsugu Koyama, Haruka Nii, Nobutaka Mitsuda, Masaru Ohta, Sakihito Kitajima, Masaru Ohme-Takagi, and Fumihiko Sato. A regulatory cascade involving class ii ethylene response factor transcriptional repressors operates in the progression of leaf senescence. Plant Physiology, 162:991-1005, Apr 2013. URL: https://doi.org/10.1104/pp.113.218115, doi:10.1104/pp.113.218115. This article has 152 citations and is from a highest quality peer-reviewed journal.

28. (koyama2013aregulatorycascade pages 1-2): Tomotsugu Koyama, Haruka Nii, Nobutaka Mitsuda, Masaru Ohta, Sakihito Kitajima, Masaru Ohme-Takagi, and Fumihiko Sato. A regulatory cascade involving class ii ethylene response factor transcriptional repressors operates in the progression of leaf senescence. Plant Physiology, 162:991-1005, Apr 2013. URL: https://doi.org/10.1104/pp.113.218115, doi:10.1104/pp.113.218115. This article has 152 citations and is from a highest quality peer-reviewed journal.

29. (miao2007theantagonistfunction pages 5-6): Ying Miao and Ulrike Zentgraf. The antagonist function of arabidopsis wrky53 and esr/esp in leaf senescence is modulated by the jasmonic and salicylic acid equilibrium. The Plant Cell Online, 19:819-830, Mar 2007. URL: https://doi.org/10.1105/tpc.106.042705, doi:10.1105/tpc.106.042705. This article has 417 citations.

30. (koyama2013aregulatorycascade pages 10-11): Tomotsugu Koyama, Haruka Nii, Nobutaka Mitsuda, Masaru Ohta, Sakihito Kitajima, Masaru Ohme-Takagi, and Fumihiko Sato. A regulatory cascade involving class ii ethylene response factor transcriptional repressors operates in the progression of leaf senescence. Plant Physiology, 162:991-1005, Apr 2013. URL: https://doi.org/10.1104/pp.113.218115, doi:10.1104/pp.113.218115. This article has 152 citations and is from a highest quality peer-reviewed journal.

31. (chroston2024formationofglucosinolatederived pages 107-109): ECM Chroston. Formation of glucosinolate-derived nitriles in roots of arabidopsis thaliana: analytics of indole glucosinolate breakdown products and effects on the rhizosphere …. Unknown journal, 2024.

## Artifacts

- [Edison artifact artifact-00](ESP-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](ESP-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](ESP-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. backenkohler2018ironisa pages 11-13
2. backenkohler2018ironisa pages 7-9
3. backenkohler2018ironisa pages 9-11
4. roman2020molecularmodelingof pages 6-7
5. witzel2019identificationandcharacterization pages 1-2
6. wittstock2007tippingthescales pages 2-4
7. miao2007theantagonistfunction pages 3-4
8. miao2007theantagonistfunction pages 1-3
9. miao2007theantagonistfunction pages 9-10
10. miao2007theantagonistfunction pages 5-6
11. koyama2013aregulatorycascade pages 9-10
12. koyama2013aregulatorycascade pages 10-11
13. koyama2013aregulatorycascade pages 6-9
14. kuchernig2012evolutionofspecifier pages 1-2
15. burow2009thegeneticbasis pages 1-2
16. wittstock2007tippingthescales pages 1-2
17. wittstock2007tippingthescales pages 4-5
18. backenkohler2018ironisa pages 3-4
19. roman2020molecularmodelingof pages 7-8
20. kissen2009nitrilespecifierproteinsinvolved pages 7-8
21. kissen2009nitrilespecifierproteinsinvolved pages 5-6
22. kissen2009nitrilespecifierproteinsinvolved pages 6-7
23. kissen2009nitrilespecifierproteinsinvolved pages 1-1
24. backenkohler2018ironisa pages 1-3
25. backenkohler2018ironisa pages 4-5
26. witzel2019identificationandcharacterization pages 9-11
27. miao2007theantagonistfunction pages 7-9
28. miao2007theantagonistfunction pages 6-7
29. miao2007theantagonistfunction pages 4-5
30. koyama2013aregulatorycascade pages 1-2
31. chroston2024formationofglucosinolatederived pages 107-109
32. https://doi.org/10.1105/tpc.106.042705,
33. https://doi.org/10.1104/pp.113.218115,
34. https://doi.org/10.1080/15216540701736277,
35. https://doi.org/10.3389/fpls.2019.01552,
36. https://doi.org/10.1371/journal.pone.0205755,
37. https://doi.org/10.1186/1471-2148-12-127,
38. https://doi.org/10.3390/molecules25040772,
39. https://doi.org/10.1074/jbc.m807500200,
40. https://doi.org/10.1104/pp.108.130732,