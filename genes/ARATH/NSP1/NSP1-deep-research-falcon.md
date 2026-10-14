---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:29:47.799151'
end_time: '2026-09-30T06:49:14.456492'
duration_seconds: 1166.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: NSP1
  gene_symbol: NSP1
  uniprot_accession: Q9SDM9
  protein_description: 'RecName: Full=Thiohydroximate-O-sulfate sulfur/sulfate-lyase
    (nitrile-forming) NSP1 {ECO:0000305}; EC=4.8.1.5 {ECO:0000269|PubMed:18987211,
    ECO:0000269|PubMed:19224919, ECO:0000269|PubMed:22954730}; AltName: Full=Jacalin-related
    lectin 28 {ECO:0000303|PubMed:18467340}; AltName: Full=Nitrile-specifier protein
    1 {ECO:0000303|PubMed:18987211}; Short=AtNSP1 {ECO:0000303|PubMed:18987211, ECO:0000303|PubMed:28479247};
    AltName: Full=Nitrile-specifier protein 3 {ECO:0000303|PubMed:19224919}; Short=AtNSP3
    {ECO:0000303|PubMed:19224919};'
  gene_info: Name=NSP1 {ECO:0000303|PubMed:18987211, ECO:0000303|PubMed:28479247};
    Synonyms=JAL28 {ECO:0000303|PubMed:18467340}, NSP3 {ECO:0000303|PubMed:19224919};
    OrderedLocusNames=At3g16400 {ECO:0000312|Araport:AT3G16400}; ORFNames=MDC8.2 {ECO:0000312|EMBL:BAB01138.1},
    T02O04.11 {ECO:0000312|EMBL:AAB63638.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the jacalin lectin family. {ECO:0000255|PROSITE-
  protein_domains: Jacalin-like_lectin_dom. (IPR001229); Jacalin-like_lectin_dom_plant.
    (IPR033734); Jacalin-like_lectin_dom_sf. (IPR036404); Kelch-typ_b-propeller. (IPR015915);
    Kelch_1. (IPR006652)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: NSP1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: NSP1-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q9SDM9
- **Protein Description:** RecName: Full=Thiohydroximate-O-sulfate sulfur/sulfate-lyase (nitrile-forming) NSP1 {ECO:0000305}; EC=4.8.1.5 {ECO:0000269|PubMed:18987211, ECO:0000269|PubMed:19224919, ECO:0000269|PubMed:22954730}; AltName: Full=Jacalin-related lectin 28 {ECO:0000303|PubMed:18467340}; AltName: Full=Nitrile-specifier protein 1 {ECO:0000303|PubMed:18987211}; Short=AtNSP1 {ECO:0000303|PubMed:18987211, ECO:0000303|PubMed:28479247}; AltName: Full=Nitrile-specifier protein 3 {ECO:0000303|PubMed:19224919}; Short=AtNSP3 {ECO:0000303|PubMed:19224919};
- **Gene Information:** Name=NSP1 {ECO:0000303|PubMed:18987211, ECO:0000303|PubMed:28479247}; Synonyms=JAL28 {ECO:0000303|PubMed:18467340}, NSP3 {ECO:0000303|PubMed:19224919}; OrderedLocusNames=At3g16400 {ECO:0000312|Araport:AT3G16400}; ORFNames=MDC8.2 {ECO:0000312|EMBL:BAB01138.1}, T02O04.11 {ECO:0000312|EMBL:AAB63638.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the jacalin lectin family. {ECO:0000255|PROSITE-
- **Key Domains:** Jacalin-like_lectin_dom. (IPR001229); Jacalin-like_lectin_dom_plant. (IPR033734); Jacalin-like_lectin_dom_sf. (IPR036404); Kelch-typ_b-propeller. (IPR015915); Kelch_1. (IPR006652)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NSP1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NSP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NSP1** (gene ID: NSP1, UniProt: Q9SDM9) in ARATH.

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
- **UniProt Accession:** Q9SDM9
- **Protein Description:** RecName: Full=Thiohydroximate-O-sulfate sulfur/sulfate-lyase (nitrile-forming) NSP1 {ECO:0000305}; EC=4.8.1.5 {ECO:0000269|PubMed:18987211, ECO:0000269|PubMed:19224919, ECO:0000269|PubMed:22954730}; AltName: Full=Jacalin-related lectin 28 {ECO:0000303|PubMed:18467340}; AltName: Full=Nitrile-specifier protein 1 {ECO:0000303|PubMed:18987211}; Short=AtNSP1 {ECO:0000303|PubMed:18987211, ECO:0000303|PubMed:28479247}; AltName: Full=Nitrile-specifier protein 3 {ECO:0000303|PubMed:19224919}; Short=AtNSP3 {ECO:0000303|PubMed:19224919};
- **Gene Information:** Name=NSP1 {ECO:0000303|PubMed:18987211, ECO:0000303|PubMed:28479247}; Synonyms=JAL28 {ECO:0000303|PubMed:18467340}, NSP3 {ECO:0000303|PubMed:19224919}; OrderedLocusNames=At3g16400 {ECO:0000312|Araport:AT3G16400}; ORFNames=MDC8.2 {ECO:0000312|EMBL:BAB01138.1}, T02O04.11 {ECO:0000312|EMBL:AAB63638.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the jacalin lectin family. {ECO:0000255|PROSITE-
- **Key Domains:** Jacalin-like_lectin_dom. (IPR001229); Jacalin-like_lectin_dom_plant. (IPR033734); Jacalin-like_lectin_dom_sf. (IPR036404); Kelch-typ_b-propeller. (IPR015915); Kelch_1. (IPR006652)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NSP1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NSP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NSP1** (gene ID: NSP1, UniProt: Q9SDM9) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: NSP1 (Nitrile-Specifier Protein 1) in Arabidopsis thaliana

## Gene Identity and Overview

NSP1 (At3g16400, UniProt Q9SDM9), also known as AtNSP1 or JAL28, encodes a nitrile-specifier protein 1 in *Arabidopsis thaliana* (burow2009thegeneticbasis pages 3-4). This gene is classified under EC 4.8.1.5 as a thiohydroximate-O-sulfate sulfur/sulfate-lyase (nitrile-forming) and belongs to the jacalin lectin family (backenkohler2018ironisa pages 3-4, burow2009thegeneticbasis pages 3-4). NSP1 was first characterized in 2009 through complementary genetic and biochemical studies that identified it as the major determinant of constitutive and herbivore-induced simple nitrile formation in Arabidopsis Columbia-0 rosette leaves (burow2009thegeneticbasis pages 3-4, burow2009thegeneticbasis pages 1-2).

| Characteristic | NSP1 / AtNSP1 summary | Evidence and qualification |
|---|---|---|
| Gene and organism | *Arabidopsis thaliana* **NSP1**, locus **At3g16400**; UniProt **Q9SDM9** | Experimental studies identify At3g16400 as the gene responsible for NSP1-dependent nitrile formation in Col-0 rosette leaves (burow2009thegeneticbasis pages 3-4) |
| Names and synonyms | Nitrile-specifier protein 1 (**NSP1**, **AtNSP1**); also annotated as **JAL28** and historically **NSP3** in the supplied UniProt record | “NSP3” is potentially confusing because current literature also discusses a separate Arabidopsis family member called AtNSP3; locus/accession should therefore accompany the symbol |
| Protein family | Glucosinolate **specifier-protein** family; jacalin-related lectin/Kelch-repeat protein | NSPs are related to epithiospecifier proteins but selectively promote simple nitriles rather than epithionitriles or thiocyanates (burow2009thegeneticbasis pages 1-2, kuchernig2012evolutionofspecifier pages 1-2) |
| Architecture and size | Chimeric protein containing N-terminal **jacalin-related lectin domain(s)** and a C-terminal Kelch-repeat region; the exact residue count was not established in the retrieved evidence excerpts | AtNSP1-family proteins possess one or two N-terminal jacalin-related domains and four or five Kelch domains; the latter assemble into a six-bladed β-propeller (backenkohler2018ironisa pages 3-4, burow2009thegeneticbasis pages 3-4) |
| Catalytic structure | The Kelch-repeat region forms a **six-bladed β-propeller** with a central active-site cavity | Structural and modeling work places the substrate/iron-binding center within the propeller; the role of the jacalin module in catalysis or carbohydrate binding remains unproven (backenkohler2018ironisa pages 3-4, burow2009thegeneticbasis pages 3-4) |
| Primary function | **Thiohydroximate-O-sulfate sulfur/sulfate-lyase (nitrile-forming), EC 4.8.1.5**; directs glucosinolate-derived aglucones toward simple nitriles | NSP1 is a product-specifying enzyme, not the enzyme that hydrolyzes intact glucosinolates (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, wittstock2010glucosinolatebreakdownin pages 9-10) |
| Coupled reaction | Myrosinase first cleaves the glucosinolate thioglucosidic bond, releasing glucose and a short-lived thiohydroximate-O-sulfate aglucone. NSP1 then promotes sulfur/sulfate loss and formation of the corresponding **simple nitrile**, competing with spontaneous Lossen rearrangement to an isothiocyanate | The substrate available directly to NSP1 is the unstable aglucone rather than intact glucosinolate; assays therefore couple NSP1 to myrosinase (roman2020molecularmodelingof pages 7-8, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2) |
| Product selectivity | Promotes **simple nitriles** but not epithionitriles or organic thiocyanates | This product profile distinguishes NSP1 from ESP and TFP specifier proteins (backenkohler2018ironisa pages 3-4, burow2009thegeneticbasis pages 1-2) |
| Cofactor | Centrally bound non-heme iron, most likely **Fe²⁺** | Specifier proteins contain a conserved **E-X₃-D-X₃-H** iron-binding motif. Direct mutational proof is strongest for AtNSP3 and related specifier proteins; equivalent Fe²⁺ coordination in AtNSP1 is supported by motif conservation and structural modeling rather than an AtNSP1-specific residue-mutagenesis series (backenkohler2018ironisa pages 9-11, backenkohler2018ironisa pages 13-15, backenkohler2018ironisa pages 1-3) |
| Proposed Fe²⁺ mechanism | Fe²⁺ is modeled as coordinating the aglucone thiolate sulfur, conserved acidic/histidine ligands, and water molecules, thereby positioning and stabilizing the reactive intermediate | The broad iron-dependent model is well supported, but the complete electronic and stepwise catalytic mechanism remains unresolved; AtNSP1 activity may retain iron tightly and was comparatively insensitive to EDTA in one study (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13) |
| Aliphatic substrate scope | Demonstrated activity with aglucones generated from **allyl/2-propenyl glucosinolate**, **4-methylsulfinylbutyl glucosinolate**, and **4-methylthiobutyl glucosinolate** | Allyl glucosinolate yields **3-butenenitrile** in coupled assays; activity across several aliphatic side chains indicates broad rather than narrow substrate acceptance (kissen2009nitrilespecifierproteinsinvolved pages 5-6, burow2009thegeneticbasis pages 3-4) |
| Aromatic substrate scope | Active with the aglucone generated from **benzyl glucosinolate** | Coupled myrosinase/AtNSP1 assays produce **2-phenylacetonitrile** instead of predominantly benzyl isothiocyanate (kissen2009nitrilespecifierproteinsinvolved pages 6-7) |
| Indole substrate scope | Controls nitrile formation from the major indole glucosinolates **I3M**, **1MOI3M**, and **4MOI3M** in tissue homogenates | NSP1 was the principal or exclusive NSP for these substrates in rosettes and the major contributor in roots (chroston2022theimpactof pages 12-14, chroston2022theimpactof pages 9-11) |
| Quantitative root phenotype | Loss of NSP1 reduced root nitriles derived from I3M, 1MOI3M, and 4MOI3M by approximately **80–90%**; wild-type nitrile proportions were about **40–50%** for I3M/1MOI3M products and about **90%** for 4MOI3M products | These data demonstrate both NSP1 dominance and substrate-dependent product partitioning in roots (chroston2022theimpactof pages 9-11) |
| Subcellular localization | Predominantly **cytoplasmic**; no evidence for secretion, membrane insertion, or vacuolar localization | Cytoplasmic prediction by TargetP/WoLF PSORT and absence from the rosette vacuolar proteome support this assignment, but direct NSP1 fluorescent-localization evidence was not identified (roman2020molecularmodelingof pages 7-8) |
| Tissue expression | Functional expression is established in **rosette leaves, roots, and seedlings**; combined NSP1/NSP3/NSP4 transcript data are highest in seedlings and roots | Some expression probes do not distinguish the tandemly related NSP genes, so organ-level transcript claims should be interpreted cautiously (wittstock2010glucosinolatebreakdownin pages 5-6, chroston2024formationofglucosinolatederiveda pages 25-28) |
| Rosette function | NSP1 is the major determinant of constitutive and herbivore-induced simple-nitrile formation and is solely responsible for detected indolic nitriles in rosette homogenates | Knockout and homogenate-product analyses provide direct genetic and biochemical evidence (burow2009thegeneticbasis pages 1-2, chroston2022theimpactof pages 1-2, chroston2022theimpactof pages 12-14) |
| Root function | NSP1 is the major contributor to indolic nitrile formation; residual activity in an nsp1 mutant probably reflects another root NSP, with NSP4 favored over NSP3 | An nsp3 mutant showed no detectable product-profile change under the tested conditions (chroston2022theimpactof pages 1-2, chroston2022theimpactof pages 12-14, chroston2022theimpactof pages 9-11) |
| Regulation | **Constitutive** activity occurs in untreated Col-0 rosettes; NSP1 transcript/activity is **locally induced by herbivore feeding**, including *Pieris rapae* attack | Herbivory-associated induction parallels increased simple-nitrile formation, establishing a regulated role in damage-activated chemical defense (wittstock2010glucosinolatebreakdownin pages 5-6, wittstock2010glucosinolatebreakdownin pages 9-10, burow2009thegeneticbasis pages 6-7) |
| Biological consequence | Shifts glucosinolate breakdown away from generally more reactive isothiocyanates toward chemically and biologically distinct nitriles, thereby changing the output of the glucosinolate–myrosinase defense system | Some nitriles act as phytoalexins or defense signals and are generally less directly toxic than corresponding isothiocyanates, but these activities are product-specific and should not all be attributed uniquely to NSP1 (chroston2024formationofglucosinolatederived pages 25-28, ting2020theroleof pages 2-3, burow2009thegeneticbasis pages 1-2) |


*Table: A consolidated evidence table for Arabidopsis NSP1 (At3g16400/Q9SDM9), covering identity, architecture, catalytic reaction, cofactor, substrate range, localization, expression, and regulation. It distinguishes direct NSP1 evidence from family-level structural or mechanistic inference.*

## Primary Enzymatic Function and Catalytic Mechanism

### Reaction Catalyzed

NSP1 functions as a product-specifying enzyme in the glucosinolate-myrosinase defense system (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, wittstock2010glucosinolatebreakdownin pages 9-10). Critically, NSP1 does not hydrolyze intact glucosinolates; instead, it acts on the unstable thiohydroximate-O-sulfate aglucone intermediate generated by myrosinase-catalyzed glucosinolate hydrolysis (roman2020molecularmodelingof pages 7-8, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2). NSP1 promotes sulfur/sulfate loss from this aglucone and directs formation of simple nitriles, competing with the spontaneous Lossen rearrangement that would otherwise yield isothiocyanates (backenkohler2018ironisa pages 3-4, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2).

The coupled reaction proceeds as follows: Myrosinases (β-thioglucoside glucohydrolases) first cleave the thioglucosidic bond of glucosinolates, releasing glucose and producing a short-lived aglucone intermediate (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, wittstock2010glucosinolatebreakdownin pages 1-2). NSP1 then intercepts this intermediate, redirecting its breakdown pathway from isothiocyanate toward simple nitrile formation (kissen2009nitrilespecifierproteinsinvolved pages 5-6, burow2009thegeneticbasis pages 3-4). This product-specifying activity distinguishes NSP1 from related specifier proteins: whereas epithiospecifier proteins (ESPs) promote epithionitrile formation and thiocyanate-forming proteins (TFPs) generate organic thiocyanates, NSP1 exclusively promotes simple nitriles (backenkohler2018ironisa pages 3-4, burow2009thegeneticbasis pages 1-2).

### Iron Cofactor and Mechanism

NSP1 requires ferrous iron (Fe²⁺) as an essential cofactor for catalytic activity (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 9-11, backenkohler2018ironisa pages 1-3). The iron is coordinated by a conserved EXXXDXXXH motif located in the central cavity of the Kelch-repeat β-propeller structure (backenkohler2018ironisa pages 9-11, backenkohler2018ironisa pages 13-15, backenkohler2018ironisa pages 1-3). Although direct mutagenesis studies have been most extensively performed on the related proteins TaTFP and AtNSP3, establishing that residues corresponding to E266, D270, and H274 (TaTFP numbering) or E386, D390, and H394 (AtNSP3 numbering) are essential for iron binding and activity, the conservation of this motif strongly supports an analogous Fe²⁺-binding arrangement in NSP1 (backenkohler2018ironisa pages 9-11, backenkohler2018ironisa pages 1-3).

The proposed catalytic mechanism involves iron coordination of the aglucone thiolate sulfur, conserved acidic and histidine ligands, and water molecules in an approximately octahedral geometry (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 4-5). This arrangement positions and stabilizes the reactive aglucone intermediate, facilitating the nitrile-forming reaction (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 11-13). Notably, NSP1 activity appears to retain iron relatively tightly and was comparatively insensitive to EDTA chelation in at least one study, suggesting high cofactor affinity (backenkohler2018ironisa pages 11-13).

### Substrate Specificity

NSP1 exhibits broad substrate specificity across multiple glucosinolate classes:

**Aliphatic glucosinolates:** NSP1 demonstrates activity with aglucones derived from allyl (2-propenyl) glucosinolate, producing 3-butenenitrile (kissen2009nitrilespecifierproteinsinvolved pages 5-6, kissen2009nitrilespecifierproteinsinvolved pages 7-8), as well as 4-methylsulfinylbutyl glucosinolate and 4-methylthiobutyl glucosinolate (burow2009thegeneticbasis pages 3-4).

**Aromatic glucosinolates:** NSP1 redirects benzyl glucosinolate-derived aglucones toward formation of 2-phenylacetonitrile (kissen2009nitrilespecifierproteinsinvolved pages 6-7).

**Indole glucosinolates:** Recent studies (2022) established that NSP1 controls nitrile formation from the three major Arabidopsis indole glucosinolates: indol-3-ylmethyl glucosinolate (I3M), 1-methoxyindol-3-ylmethyl glucosinolate (1MOI3M), and 4-methoxyindol-3-ylmethyl glucosinolate (4MOI3M) (chroston2022theimpactof pages 1-2, chroston2022theimpactof pages 12-14, chroston2022theimpactof pages 9-11). The substrate-dependent product partitioning varies considerably: in wild-type Arabidopsis roots, approximately 40–50% of I3M- and 1MOI3M-derived products are nitriles, whereas about 90% of 4MOI3M-derived products form nitriles (chroston2022theimpactof pages 9-11).

## Subcellular Localization

NSP1 is predominantly localized in the cytoplasm (roman2020molecularmodelingof pages 7-8). This localization is supported by computational predictions using WoLF PSORT and TargetP algorithms, as well as proteomic evidence showing that NSPs are absent from vacuolar proteomes of rosette leaves (roman2020molecularmodelingof pages 7-8). The cytoplasmic localization is functionally appropriate, as it positions NSP1 to encounter myrosinase-generated glucosinolate aglucones after tissue disruption breaks down the compartmental barriers that normally separate glucosinolates (stored in vacuoles) from myrosinases and NSPs (roman2020molecularmodelingof pages 7-8, wittstock2010glucosinolatebreakdownin pages 1-2).

## Glucosinolate-Myrosinase Defense Pathway

> **1. Compartmentation in intact tissue.** Arabidopsis stores glucosinolates separately from the myrosinases that activate them, preventing uncontrolled production of reactive breakdown products. NSP1 is predicted to be cytoplasmic rather than vacuolar or secreted, positioning it to participate when cellular compartmentation is disrupted. (roman2020molecularmodelingof pages 7-8, wittstock2010glucosinolatebreakdownin pages 1-2)
>
> **2. Damage activates the system.** Herbivory, chewing, or mechanical disruption breaks cellular barriers and mixes glucosinolates with myrosinases—the activation principle commonly called the glucosinolate–myrosinase system or “mustard-oil bomb.” NSP1 expression and NSP1-dependent nitrile formation also increase locally after herbivore feeding. (burow2009thegeneticbasis pages 1-2, wittstock2010glucosinolatebreakdownin pages 9-10, wittstock2010glucosinolatebreakdownin pages 1-2)
>
> **3. Myrosinase performs the initiating hydrolysis.** A myrosinase cleaves the glucosinolate’s thioglucosidic bond, releasing glucose and generating a short-lived thiohydroximate-O-sulfate aglucone. NSP1 does not hydrolyze the intact glucosinolate; consequently, biochemical assays must supply both glucosinolate and myrosinase to generate NSP1’s actual substrate. (roman2020molecularmodelingof pages 7-8, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, wittstock2010glucosinolatebreakdownin pages 9-10)
>
> **4. The unstable aglucone is the metabolic branch point.** Without a specifier protein, the aglucone ordinarily undergoes spontaneous Lossen-type rearrangement to the corresponding isothiocyanate. The side-chain structure, reaction environment, and presence of a specifier protein determine which final product predominates. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, wittstock2010glucosinolatebreakdownin pages 2-4)
>
> **5. NSP1 redirects the branch toward simple nitriles.** NSP1 acts on the myrosinase-generated aglucone as an Fe²⁺-dependent nitrile-specifier enzyme, promoting sulfur/sulfate loss and formation of a simple nitrile at the expense of isothiocyanate formation. Unlike epithiospecifier and thiocyanate-forming proteins, NSP1 does not promote epithionitriles or organic thiocyanates. Its demonstrated scope includes aglucones from aliphatic, aromatic, and indole glucosinolates. (kissen2009nitrilespecifierproteinsinvolved pages 5-6, burow2009thegeneticbasis pages 3-4, kissen2009nitrilespecifierproteinsinvolved pages 6-7, backenkohler2018ironisa pages 13-15, eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2)
>
> **6. NSP1 therefore changes—not merely activates—the defense chemistry.** Isothiocyanates are generally reactive, broadly toxic antimicrobial and anti-herbivore compounds, whereas simple nitriles are often less directly toxic and can have product-specific roles as phytoalexins, ecological signals, or immune-response modulators. Some nitriles can also be hydrolyzed by nitrilases to carboxylic acids; indole-3-acetonitrile can thereby feed into indole-3-acetic-acid metabolism. These downstream effects are nitrile-specific and should not all be attributed uniquely to NSP1. (wittstock2010glucosinolatebreakdownin pages 9-10, chroston2024formationofglucosinolatederived pages 25-28, ting2020theroleof pages 2-3, ting2020theroleof pages 1-2)


*Blockquote: This stepwise pathway traces glucosinolate activation from compartment disruption through myrosinase hydrolysis and shows where NSP1 redirects the unstable aglucone from isothiocyanates toward simple nitriles. It also distinguishes NSP1’s product-specifying role from myrosinase activity and summarizes the differing biological consequences of the products.*

NSP1 functions within the glucosinolate-myrosinase defense system, often referred to as the "mustard-oil bomb" (wittstock2010glucosinolatebreakdownin pages 1-2). In intact Arabidopsis tissue, glucosinolates are stored separately from their activating enzymes, preventing spontaneous breakdown (wittstock2010glucosinolatebreakdownin pages 1-2). Upon tissue damage caused by herbivory, mechanical disruption, or pathogen attack, cellular compartmentation is breached, allowing glucosinolates to mix with myrosinases (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, wittstock2010glucosinolatebreakdownin pages 1-2).

Classical myrosinases (TGG1 and TGG2 in leaves; TGG4 and TGG5 in roots) catalyze hydrolysis of the thioglucosidic bond, generating the unstable aglucone intermediate (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). NSP1 then redirects this intermediate from the default isothiocyanate pathway toward simple nitrile formation (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2, roman2020molecularmodelingof pages 7-8). The resulting nitriles can serve multiple biological functions: direct defense compounds, signaling molecules in immune responses, or substrates for nitrilase-mediated conversion to carboxylic acids, including the auxin indole-3-acetic acid (IAA) from indole-3-acetonitrile (wittstock2010glucosinolatebreakdownin pages 9-10, chroston2024formationofglucosinolatederived pages 25-28).

## Protein Structure and Evolutionary Context

### Domain Architecture

NSP1 possesses a chimeric architecture combining N-terminal jacalin-related lectin (JRL) domains with C-terminal Kelch repeat domains (burow2009thegeneticbasis pages 3-4). The protein contains one or two jacalin-related lectin domains, which share evolutionary ancestry with putative Arabidopsis mannose-binding proteins (MBPs) (burow2009thegeneticbasis pages 3-4). These jacalin domains are followed by four or five Kelch domains (each approximately 44–56 amino acids) that assemble into a six-bladed β-propeller structure (backenkohler2018ironisa pages 3-4, burow2009thegeneticbasis pages 3-4).

The Kelch-repeat β-propeller forms the catalytic core, with the active site located in the central cavity containing the conserved iron-binding EXXXDXXXH motif (backenkohler2018ironisa pages 3-4, backenkohler2018ironisa pages 13-15). While the precise role of the N-terminal jacalin domains in NSP1 function remains uncertain, these domains may contribute to protein interactions, carbohydrate recognition, or regulatory functions (mbudu2026biochemicalcharacterizationof pages 11-12, eggermont2017genome‐widescreeningfor pages 5-7).

### Evolutionary Relationships

Phylogenetic analyses indicate that nitrile-specifier proteins represent the ancestral specifier protein activity, with epithiospecifier proteins (ESPs) and thiocyanate-forming proteins (TFPs) evolving subsequently (kuchernig2012evolutionofspecifier pages 1-2). NSP1 belongs to the AtNSP1-cluster in phylogenetic trees, distinct from the AtNSP5-cluster and the ESP/TFP cluster (kuchernig2012evolutionofspecifier pages 1-2). The specifier protein family likely arose before the radiation of core Brassicaceae, and evidence suggests that these proteins evolved under purifying selection, indicating functional constraint (kuchernig2012evolutionofspecifier pages 1-2).

## Expression Pattern and Regulation

### Tissue-Specific Expression

NSP1 is expressed in multiple Arabidopsis tissues, including rosette leaves, roots, and seedlings (wittstock2010glucosinolatebreakdownin pages 5-6, chroston2024formationofglucosinolatederiveda pages 25-28, roman2020molecularmodelingof pages 7-8). Expression profiling data (which sometimes cannot distinguish among the tandemly arranged NSP1, NSP3, and NSP4 genes) indicate that combined NSP transcript levels are highest in seedlings and roots (wittstock2010glucosinolatebreakdownin pages 5-6, roman2020molecularmodelingof pages 7-8).

### Functional Tissue Specificity

**Rosette leaves:** NSP1 is the major determinant of simple nitrile formation in rosette leaves and is solely responsible for detectable indolic nitrile formation in rosette homogenates (burow2009thegeneticbasis pages 1-2, chroston2022theimpactof pages 1-2, chroston2022theimpactof pages 12-14). Knockout studies demonstrate that loss of NSP1 eliminates both constitutive and herbivore-induced simple nitrile production in this tissue (burow2009thegeneticbasis pages 1-2).

**Roots:** In roots, NSP1 is the major contributor to indolic nitrile formation, reducing nitriles derived from I3M, 1MOI3M, and 4MOI3M by approximately 80–90% in nsp1 mutants (chroston2022theimpactof pages 9-11). However, residual nitrile formation in nsp1-deficient roots suggests contribution from additional root-expressed NSPs, most likely NSP4 rather than NSP3, as nsp3 mutants showed no detectable product-profile differences (chroston2022theimpactof pages 1-2, chroston2022theimpactof pages 12-14, chroston2022theimpactof pages 9-11).

### Inducible Expression

NSP1 exhibits both constitutive and inducible expression (burow2009thegeneticbasis pages 1-2, wittstock2010glucosinolatebreakdownin pages 9-10). In Arabidopsis rosette leaves, NSP1 is strongly induced by herbivore feeding, particularly by larvae of the specialist herbivore *Pieris rapae* (cabbage white butterfly) (wittstock2010glucosinolatebreakdownin pages 5-6, wittstock2010glucosinolatebreakdownin pages 9-10, burow2009thegeneticbasis pages 6-7). This herbivore-induced expression correlates with increased simple nitrile formation in damaged leaf tissue (wittstock2010glucosinolatebreakdownin pages 5-6, wittstock2010glucosinolatebreakdownin pages 9-10), establishing NSP1 as a regulated component of the damage-activated defense response.

## Biological Functions and Defense Roles

### Product Differentiation: Nitriles versus Isothiocyanates

NSP1 fundamentally alters the chemical output of the glucosinolate-myrosinase defense system by shifting product formation from isothiocyanates to nitriles (burow2009thegeneticbasis pages 1-2, chroston2022theimpactof pages 1-2). This product diversification has significant biological consequences, as isothiocyanates and nitriles possess distinct physicochemical properties and biological activities (ting2020theroleof pages 2-3, chroston2022theimpactof pages 1-2).

**Isothiocyanates** are generally reactive, broadly toxic compounds with strong antimicrobial and herbivore-deterrent activities (chroston2024formationofglucosinolatederived pages 25-28, ting2020theroleof pages 2-3, burow2009thegeneticbasis pages 1-2). They are effective chemical defenses but can also be phytotoxic at high concentrations, causing stomatal closure, cell death, microtubule disruption, and glutathione depletion (ting2020theroleof pages 2-3).

**Nitriles** are typically less directly toxic than their corresponding isothiocyanates but possess distinct biological activities (chroston2024formationofglucosinolatederived pages 25-28, ting2020theroleof pages 2-3, burow2009thegeneticbasis pages 1-2). Some indole-derived nitriles, including indole-3-acetonitrile and 1-methoxyindole-3-acetonitrile, function as phytoalexins against plant-pathogenic fungi (chroston2024formationofglucosinolatederived pages 25-28, chroston2024formationofglucosinolatederiveda pages 25-28). Additionally, the glucosinolate-derived nitrile 3-butenenitrile (3BN) can activate plant immune responses, inducing nitric oxide production, reactive oxygen species accumulation, stomatal closure, and production of defense-associated metabolites and hormones (salicylic acid and jasmonic acid) (ting2020theroleof pages 2-3, ting2020theroleof pages 1-2). Pretreatment with 3BN enhances resistance to necrotrophic pathogens including *Pectobacterium carotovorum* and *Botrytis cinerea* (ting2020theroleof pages 1-2).

### Metabolic Integration

Nitriles produced through NSP1 activity can undergo further metabolism via nitrilase-catalyzed hydrolysis to carboxylic acids and ammonia (wittstock2010glucosinolatebreakdownin pages 9-10). Notably, indole-3-acetonitrile can be converted to indole-3-acetic acid (IAA), the primary auxin in plants, potentially linking glucosinolate breakdown to growth regulation and stress responses (chroston2024formationofglucosinolatederived pages 25-28, chroston2024formationofglucosinolatederiveda pages 25-28).

### Ecological and Defense Trade-offs

Evidence suggests that NSP1-dependent nitrile formation may not function primarily as a direct toxin-based defense (burow2009thegeneticbasis pages 1-2). Instead, NSP1 activity may represent an adaptive strategy that produces less phytotoxic defense compounds while maintaining antimicrobial activity and enabling signaling functions (ting2020theroleof pages 2-3, burow2009thegeneticbasis pages 1-2). This product diversification likely influences plant-insect interactions and contributes to the metabolic flexibility of the glucosinolate defense system (burow2009thegeneticbasis pages 1-2).

## Recent Developments (2022-2024)

### Detailed Tissue-Specific Product Profiling

Chroston et al. (2022) provided the first comprehensive analytical method for quantifying both nitriles and carbinols from indole glucosinolate breakdown in Arabidopsis tissue homogenates (chroston2022theimpactof pages 1-2). This work established that carbinols are more dominant in rosette homogenates than in root homogenates and confirmed that NSP1 is solely responsible for indolic nitrile formation in rosettes while serving as the major contributor in roots (chroston2022theimpactof pages 1-2, chroston2022theimpactof pages 12-14, chroston2022theimpactof pages 9-11).

### Expanded NSP Family Functions

A 2023 study by Zhai et al. revealed that the related family member NSP2 has functions extending beyond glucosinolate breakdown (zhai2023nitrilespecificproteinnsp2 pages 1-2, zhai2023nitrilespecificproteinnsp2 pages 2-4). NSP2 was shown to interact with the MAP kinase MPK3 and participate in plant disease resistance through effects on pathogenesis-related gene expression, reactive oxygen burst, and hormone signaling pathways (zhai2023nitrilespecificproteinnsp2 pages 1-2, zhai2023nitrilespecificproteinnsp2 pages 2-4). This finding suggests that NSP family members, including potentially NSP1, may have broader roles in plant immunity beyond their well-characterized specifier activities.

### Cross-Species NSP Characterization

Mbudu et al. (2026) characterized nitrile-specifier proteins from *Brassica oleracea* vegetables, confirming Fe²⁺-dependence and demonstrating differential substrate specificities among NSP isoforms (mbudu2026biochemicalcharacterizationof pages 11-12). This work supports the conservation of the iron-dependent mechanism across Brassicaceae species and highlights substrate-specific adaptations among NSP family members.

### Rhizosphere and Root Defense

Multiple recent studies (2022-2024) have emphasized the importance of NSPs, including NSP1, in root defense and rhizosphere interactions (chroston2024formationofglucosinolatederived pages 25-28, chroston2024formationofglucosinolatederiveda pages 25-28). Root-expressed NSP1 contributes to the production of nitriles that may influence rhizosphere microbial communities and provide below-ground chemical defense (chroston2024formationofglucosinolatederiveda pages 25-28, chroston2024formationofglucosinolatederived pages 25-28, chroston2024formationofglucosinolatederivedb pages 25-28).

## Summary and Conclusions

NSP1 (At3g16400) is a well-characterized Fe²⁺-dependent enzyme that plays a critical role in diversifying the chemical output of the Arabidopsis glucosinolate-myrosinase defense system. By redirecting glucosinolate-derived aglucones from isothiocyanate formation toward simple nitrile formation, NSP1 fundamentally alters the defensive chemistry available to the plant. The enzyme exhibits broad substrate specificity encompassing aliphatic, aromatic, and indole glucosinolates, and functions in multiple tissues including rosette leaves and roots, where it shows both constitutive and herbivore-inducible expression.

The structural architecture of NSP1, combining jacalin lectin and Kelch-repeat domains, reflects its evolutionary position as an ancestral member of the specifier protein family. The Fe²⁺ cofactor coordinated by conserved residues in the Kelch-domain β-propeller is essential for NSP1's product-specifying activity. Recent research continues to reveal tissue-specific nuances of NSP1 function and suggests that the NSP family may have broader roles in plant immunity beyond glucosinolate metabolism.

Understanding NSP1 function provides insight into how plants fine-tune their chemical defenses through product diversification, balancing toxicity, signaling, and metabolic integration to optimize responses to diverse environmental challenges.

## Key References (Selected)

**Foundational characterization:**
- Burow et al. (2009). Plant Physiology 149:561-574. doi:10.1104/pp.108.130732
- Kissen & Bones (2009). Journal of Biological Chemistry 284:12057-12070. doi:10.1074/jbc.m807500200
- Wittstock & Burow (2010). The Arabidopsis Book 2010:e0134. doi:10.1199/tab.0134

**Iron cofactor and mechanism:**
- Backenköhler et al. (2018). PLoS ONE 13:e0205755. doi:10.1371/journal.pone.0205755
- Eisenschmidt-Bönn et al. (2019). The Plant Journal 99:329-343. doi:10.1111/tpj.14327

**Recent tissue-specific analyses:**
- Chroston et al. (2022). Molecules 27:8042. doi:10.3390/molecules27228042

**Biological functions:**
- Ting et al. (2020). Frontiers in Plant Science 11:257. doi:10.3389/fpls.2020.00257

**Recent NSP family advances:**
- Zhai et al. (2023). Plants 12:2857. doi:10.3390/plants12152857

References

1. (burow2009thegeneticbasis pages 3-4): Meike Burow, Anja Losansky, René Müller, Antje Plock, Daniel J. Kliebenstein, and Ute Wittstock. The genetic basis of constitutive and herbivore-induced esp-independent nitrile formation in arabidopsis. Plant Physiology, 149(1):561-574, Nov 2009. URL: https://doi.org/10.1104/pp.108.130732, doi:10.1104/pp.108.130732. This article has 190 citations and is from a highest quality peer-reviewed journal.

2. (backenkohler2018ironisa pages 3-4): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

3. (burow2009thegeneticbasis pages 1-2): Meike Burow, Anja Losansky, René Müller, Antje Plock, Daniel J. Kliebenstein, and Ute Wittstock. The genetic basis of constitutive and herbivore-induced esp-independent nitrile formation in arabidopsis. Plant Physiology, 149(1):561-574, Nov 2009. URL: https://doi.org/10.1104/pp.108.130732, doi:10.1104/pp.108.130732. This article has 190 citations and is from a highest quality peer-reviewed journal.

4. (kuchernig2012evolutionofspecifier pages 1-2): Jennifer-Christin Kuchernig, Meike Burow, and U. Wittstock. Evolution of specifier proteins in glucosinolate-containing plants. BMC Evolutionary Biology, 12:127-127, Jul 2012. URL: https://doi.org/10.1186/1471-2148-12-127, doi:10.1186/1471-2148-12-127. This article has 112 citations and is from a domain leading peer-reviewed journal.

5. (eisenschmidt‐bonn2019structuraldiversificationduring pages 1-2): Daniela Eisenschmidt‐Bönn, Nicola Schneegans, Anita Backenköhler, Ute Wittstock, and Wolfgang Brandt. Structural diversification during glucosinolate breakdown: mechanisms of thiocyanate, epithionitrile and simple nitrile formation. The Plant Journal, 99:329-343, Apr 2019. URL: https://doi.org/10.1111/tpj.14327, doi:10.1111/tpj.14327. This article has 61 citations.

6. (wittstock2010glucosinolatebreakdownin pages 9-10): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

7. (roman2020molecularmodelingof pages 7-8): Juan Román, Dorian González, Mario Inostroza-Ponta, and Andrea Mahn. Molecular modeling of epithiospecifier and nitrile-specifier proteins of broccoli and their interaction with aglycones. Molecules, 25:772, Feb 2020. URL: https://doi.org/10.3390/molecules25040772, doi:10.3390/molecules25040772. This article has 23 citations.

8. (backenkohler2018ironisa pages 9-11): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

9. (backenkohler2018ironisa pages 13-15): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

10. (backenkohler2018ironisa pages 1-3): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

11. (backenkohler2018ironisa pages 11-13): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

12. (kissen2009nitrilespecifierproteinsinvolved pages 5-6): Ralph Kissen and Atle M. Bones. Nitrile-specifier proteins involved in glucosinolate hydrolysis in arabidopsis thaliana*. Journal of Biological Chemistry, 284:12057-12070, May 2009. URL: https://doi.org/10.1074/jbc.m807500200, doi:10.1074/jbc.m807500200. This article has 176 citations and is from a domain leading peer-reviewed journal.

13. (kissen2009nitrilespecifierproteinsinvolved pages 6-7): Ralph Kissen and Atle M. Bones. Nitrile-specifier proteins involved in glucosinolate hydrolysis in arabidopsis thaliana*. Journal of Biological Chemistry, 284:12057-12070, May 2009. URL: https://doi.org/10.1074/jbc.m807500200, doi:10.1074/jbc.m807500200. This article has 176 citations and is from a domain leading peer-reviewed journal.

14. (chroston2022theimpactof pages 12-14): Eleanor C. M. Chroston, Annika Hielscher, Matthias Strieker, and Ute Wittstock. The impact of nitrile-specifier proteins on indolic carbinol and nitrile formation in homogenates of arabidopsis thaliana. Molecules, 27:8042, Nov 2022. URL: https://doi.org/10.3390/molecules27228042, doi:10.3390/molecules27228042. This article has 3 citations.

15. (chroston2022theimpactof pages 9-11): Eleanor C. M. Chroston, Annika Hielscher, Matthias Strieker, and Ute Wittstock. The impact of nitrile-specifier proteins on indolic carbinol and nitrile formation in homogenates of arabidopsis thaliana. Molecules, 27:8042, Nov 2022. URL: https://doi.org/10.3390/molecules27228042, doi:10.3390/molecules27228042. This article has 3 citations.

16. (wittstock2010glucosinolatebreakdownin pages 5-6): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

17. (chroston2024formationofglucosinolatederiveda pages 25-28): ECM Chroston. Formation of glucosinolate-derived nitriles in roots of arabidopsis thaliana: analytics of indole glucosinolate breakdown products and effects on the rhizosphere …. Unknown journal, 2024.

18. (chroston2022theimpactof pages 1-2): Eleanor C. M. Chroston, Annika Hielscher, Matthias Strieker, and Ute Wittstock. The impact of nitrile-specifier proteins on indolic carbinol and nitrile formation in homogenates of arabidopsis thaliana. Molecules, 27:8042, Nov 2022. URL: https://doi.org/10.3390/molecules27228042, doi:10.3390/molecules27228042. This article has 3 citations.

19. (burow2009thegeneticbasis pages 6-7): Meike Burow, Anja Losansky, René Müller, Antje Plock, Daniel J. Kliebenstein, and Ute Wittstock. The genetic basis of constitutive and herbivore-induced esp-independent nitrile formation in arabidopsis. Plant Physiology, 149(1):561-574, Nov 2009. URL: https://doi.org/10.1104/pp.108.130732, doi:10.1104/pp.108.130732. This article has 190 citations and is from a highest quality peer-reviewed journal.

20. (chroston2024formationofglucosinolatederived pages 25-28): ECM Chroston. Formation of glucosinolate-derived nitriles in roots of arabidopsis thaliana: analytics of indole glucosinolate breakdown products and effects on the rhizosphere …. Unknown journal, 2024.

21. (ting2020theroleof pages 2-3): Hieng-Ming Ting, Boon Huat Cheah, Yu-Cheng Chen, Pei-Min Yeh, Chiu-Ping Cheng, Freddy Kuok San Yeo, Ane Kjersti Vie, Jens Rohloff, Per Winge, Atle M. Bones, and Ralph Kissen. The role of a glucosinolate-derived nitrile in plant immune responses. Frontiers in Plant Science, Mar 2020. URL: https://doi.org/10.3389/fpls.2020.00257, doi:10.3389/fpls.2020.00257. This article has 46 citations.

22. (wittstock2010glucosinolatebreakdownin pages 1-2): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

23. (backenkohler2018ironisa pages 4-5): Anita Backenköhler, Daniela Eisenschmidt, Nicola Schneegans, Matthias Strieker, Wolfgang Brandt, and Ute Wittstock. Iron is a centrally bound cofactor of specifier proteins involved in glucosinolate breakdown. PLoS ONE, 13:e0205755, Nov 2018. URL: https://doi.org/10.1371/journal.pone.0205755, doi:10.1371/journal.pone.0205755. This article has 40 citations and is from a peer-reviewed journal.

24. (kissen2009nitrilespecifierproteinsinvolved pages 7-8): Ralph Kissen and Atle M. Bones. Nitrile-specifier proteins involved in glucosinolate hydrolysis in arabidopsis thaliana*. Journal of Biological Chemistry, 284:12057-12070, May 2009. URL: https://doi.org/10.1074/jbc.m807500200, doi:10.1074/jbc.m807500200. This article has 176 citations and is from a domain leading peer-reviewed journal.

25. (wittstock2010glucosinolatebreakdownin pages 2-4): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

26. (ting2020theroleof pages 1-2): Hieng-Ming Ting, Boon Huat Cheah, Yu-Cheng Chen, Pei-Min Yeh, Chiu-Ping Cheng, Freddy Kuok San Yeo, Ane Kjersti Vie, Jens Rohloff, Per Winge, Atle M. Bones, and Ralph Kissen. The role of a glucosinolate-derived nitrile in plant immune responses. Frontiers in Plant Science, Mar 2020. URL: https://doi.org/10.3389/fpls.2020.00257, doi:10.3389/fpls.2020.00257. This article has 46 citations.

27. (mbudu2026biochemicalcharacterizationof pages 11-12): Kudzai Gracious Mbudu, Katja Witzel, Ute Wittstock, Frederik Börnke, and Franziska Sabine Hanschen. Biochemical characterization of two brassica oleracea nitrile-specifier proteins. Frontiers in Plant Science, Jan 2026. URL: https://doi.org/10.3389/fpls.2026.1740844, doi:10.3389/fpls.2026.1740844. This article has 0 citations.

28. (eggermont2017genome‐widescreeningfor pages 5-7): Lore Eggermont, Bruno Verstraeten, and Els J.M. Van Damme. Genome‐wide screening for lectin motifs in arabidopsis thaliana. The Plant Genome, Jul 2017. URL: https://doi.org/10.3835/plantgenome2017.02.0010, doi:10.3835/plantgenome2017.02.0010. This article has 62 citations.

29. (zhai2023nitrilespecificproteinnsp2 pages 1-2): Tingting Zhai, J. Teng, Xintong Fan, Shao-Xuan Yu, Chen Wang, Xingqi Guo, Wei Yang, and Shuxin Zhang. Nitrile-specific protein nsp2 and its interacting protein mpk3 synergistically regulate plant disease resistance in arabidopsis. Plants, 12:2857, Aug 2023. URL: https://doi.org/10.3390/plants12152857, doi:10.3390/plants12152857. This article has 5 citations.

30. (zhai2023nitrilespecificproteinnsp2 pages 2-4): Tingting Zhai, J. Teng, Xintong Fan, Shao-Xuan Yu, Chen Wang, Xingqi Guo, Wei Yang, and Shuxin Zhang. Nitrile-specific protein nsp2 and its interacting protein mpk3 synergistically regulate plant disease resistance in arabidopsis. Plants, 12:2857, Aug 2023. URL: https://doi.org/10.3390/plants12152857, doi:10.3390/plants12152857. This article has 5 citations.

31. (chroston2024formationofglucosinolatederivedb pages 25-28): ECM Chroston. Formation of glucosinolate-derived nitriles in roots of arabidopsis thaliana: analytics of indole glucosinolate breakdown products and effects on the rhizosphere …. Unknown journal, 2024.

## Artifacts

- [Edison artifact artifact-00](NSP1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](NSP1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. burow2009thegeneticbasis pages 3-4
2. kissen2009nitrilespecifierproteinsinvolved pages 6-7
3. chroston2022theimpactof pages 9-11
4. roman2020molecularmodelingof pages 7-8
5. backenkohler2018ironisa pages 11-13
6. wittstock2010glucosinolatebreakdownin pages 1-2
7. kuchernig2012evolutionofspecifier pages 1-2
8. burow2009thegeneticbasis pages 1-2
9. ting2020theroleof pages 2-3
10. ting2020theroleof pages 1-2
11. wittstock2010glucosinolatebreakdownin pages 9-10
12. chroston2022theimpactof pages 1-2
13. mbudu2026biochemicalcharacterizationof pages 11-12
14. backenkohler2018ironisa pages 3-4
15. backenkohler2018ironisa pages 9-11
16. backenkohler2018ironisa pages 13-15
17. backenkohler2018ironisa pages 1-3
18. kissen2009nitrilespecifierproteinsinvolved pages 5-6
19. chroston2022theimpactof pages 12-14
20. wittstock2010glucosinolatebreakdownin pages 5-6
21. chroston2024formationofglucosinolatederiveda pages 25-28
22. burow2009thegeneticbasis pages 6-7
23. chroston2024formationofglucosinolatederived pages 25-28
24. backenkohler2018ironisa pages 4-5
25. kissen2009nitrilespecifierproteinsinvolved pages 7-8
26. wittstock2010glucosinolatebreakdownin pages 2-4
27. chroston2024formationofglucosinolatederivedb pages 25-28
28. https://doi.org/10.1104/pp.108.130732,
29. https://doi.org/10.1371/journal.pone.0205755,
30. https://doi.org/10.1186/1471-2148-12-127,
31. https://doi.org/10.1111/tpj.14327,
32. https://doi.org/10.1199/tab.0134,
33. https://doi.org/10.3390/molecules25040772,
34. https://doi.org/10.1074/jbc.m807500200,
35. https://doi.org/10.3390/molecules27228042,
36. https://doi.org/10.3389/fpls.2020.00257,
37. https://doi.org/10.3389/fpls.2026.1740844,
38. https://doi.org/10.3835/plantgenome2017.02.0010,
39. https://doi.org/10.3390/plants12152857,