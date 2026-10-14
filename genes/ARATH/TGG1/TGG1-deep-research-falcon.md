---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:27:23.946411'
end_time: '2026-09-30T06:43:21.473554'
duration_seconds: 957.53
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: TGG1
  gene_symbol: TGG1
  uniprot_accession: P37702
  protein_description: 'RecName: Full=Myrosinase 1 {ECO:0000303|PubMed:19703694};
    EC=3.2.1.147 {ECO:0000269|PubMed:19703694}; AltName: Full=Beta-glucosidase 38
    {ECO:0000303|PubMed:15604686}; Short=AtBGLU38 {ECO:0000303|PubMed:15604686}; EC=3.2.1.21
    {ECO:0000269|PubMed:19703694}; AltName: Full=Sinigrinase 1 {ECO:0000303|PubMed:19703694};
    AltName: Full=Thioglucosidase 1 {ECO:0000303|PubMed:19703694}; Flags: Precursor;'
  gene_info: Name=TGG1 {ECO:0000303|PubMed:19703694}; Synonyms=BGLU38 {ECO:0000303|PubMed:15604686};
    OrderedLocusNames=At5g26000 {ECO:0000312|Araport:AT5G26000}; ORFNames=T1N24.7
    {ECO:0000312|EMBL:AAD40143.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the glycosyl hydrolase 1 family. .
  protein_domains: GH_1_N_CS. (IPR033132); GH_hydrolase_sf. (IPR017853); Glyco_hydro_1.
    (IPR001360); Glyco_hydro_1_AS. (IPR018120); Glyco_hydro_1 (PF00232)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: TGG1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: TGG1-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: TGG1-deep-research-falcon_artifacts/artifact-02.md
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
- **UniProt Accession:** P37702
- **Protein Description:** RecName: Full=Myrosinase 1 {ECO:0000303|PubMed:19703694}; EC=3.2.1.147 {ECO:0000269|PubMed:19703694}; AltName: Full=Beta-glucosidase 38 {ECO:0000303|PubMed:15604686}; Short=AtBGLU38 {ECO:0000303|PubMed:15604686}; EC=3.2.1.21 {ECO:0000269|PubMed:19703694}; AltName: Full=Sinigrinase 1 {ECO:0000303|PubMed:19703694}; AltName: Full=Thioglucosidase 1 {ECO:0000303|PubMed:19703694}; Flags: Precursor;
- **Gene Information:** Name=TGG1 {ECO:0000303|PubMed:19703694}; Synonyms=BGLU38 {ECO:0000303|PubMed:15604686}; OrderedLocusNames=At5g26000 {ECO:0000312|Araport:AT5G26000}; ORFNames=T1N24.7 {ECO:0000312|EMBL:AAD40143.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the glycosyl hydrolase 1 family. .
- **Key Domains:** GH_1_N_CS. (IPR033132); GH_hydrolase_sf. (IPR017853); Glyco_hydro_1. (IPR001360); Glyco_hydro_1_AS. (IPR018120); Glyco_hydro_1 (PF00232)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TGG1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TGG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TGG1** (gene ID: TGG1, UniProt: P37702) in ARATH.

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
- **UniProt Accession:** P37702
- **Protein Description:** RecName: Full=Myrosinase 1 {ECO:0000303|PubMed:19703694}; EC=3.2.1.147 {ECO:0000269|PubMed:19703694}; AltName: Full=Beta-glucosidase 38 {ECO:0000303|PubMed:15604686}; Short=AtBGLU38 {ECO:0000303|PubMed:15604686}; EC=3.2.1.21 {ECO:0000269|PubMed:19703694}; AltName: Full=Sinigrinase 1 {ECO:0000303|PubMed:19703694}; AltName: Full=Thioglucosidase 1 {ECO:0000303|PubMed:19703694}; Flags: Precursor;
- **Gene Information:** Name=TGG1 {ECO:0000303|PubMed:19703694}; Synonyms=BGLU38 {ECO:0000303|PubMed:15604686}; OrderedLocusNames=At5g26000 {ECO:0000312|Araport:AT5G26000}; ORFNames=T1N24.7 {ECO:0000312|EMBL:AAD40143.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the glycosyl hydrolase 1 family. .
- **Key Domains:** GH_1_N_CS. (IPR033132); GH_hydrolase_sf. (IPR017853); Glyco_hydro_1. (IPR001360); Glyco_hydro_1_AS. (IPR018120); Glyco_hydro_1 (PF00232)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TGG1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TGG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TGG1** (gene ID: TGG1, UniProt: P37702) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: TGG1 (Myrosinase 1) from *Arabidopsis thaliana*

## Gene Identity and Classification

TGG1 (THIOGLUCOSIDE GLUCOHYDROLASE 1, At5g26000, also known as BGLU38) encodes Myrosinase 1 in *Arabidopsis thaliana* (UniProt accession P37702) (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). This classical plant myrosinase belongs to the glycoside hydrolase family 1 (GH1) and represents one of the most extensively characterized enzymes in the glucosinolate-myrosinase defense system (wittstock2010glucosinolatebreakdownin pages 1-2).

## Primary Enzymatic Function and Substrate Specificity

### Catalytic Reaction

TGG1 is a thioglucoside glucohydrolase (EC 3.2.1.147; EC 3.2.1.21) that catalyzes the hydrolysis of the thioglucosidic bond in glucosinolates (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). The reaction cleaves glucosinolates into D-glucose, sulfate, and an unstable aglycone intermediate (shazada2015studiesofexpression pages 6-10, wittstock2010glucosinolatebreakdownin pages 1-2). This aglycone spontaneously rearranges to form an isothiocyanate under default conditions, or can be redirected by specifier proteins to produce simple nitriles, epithionitriles, thiocyanates, or other derivatives depending on pH, cofactors, and associated proteins (wittstock2010glucosinolatebreakdownin pages 2-4, chhajed2020glucosinolatebiosynthesisand pages 9-11).

### Catalytic Mechanism

TGG1 employs a modified GH1-type retaining glycoside hydrolase mechanism (wittstock2010glucosinolatebreakdownin pages 1-2). Unlike conventional family-1 β-glucosidases, classical myrosinases replace the typical catalytic acid/base glutamate in the TFNEP motif with glutamine in a TI/LNQL/P-like sequence (wittstock2010glucosinolatebreakdownin pages 1-2). Ascorbate is proposed to substitute for the missing glutamate as the acid/base catalyst and serves as an essential cofactor, activating myrosinase activity at low concentrations while inhibiting at high concentrations (shazada2015studiesofexpression pages 6-10, chhajed2020glucosinolatebiosynthesisand pages 9-11).

### Substrate Specificity

Recombinant TGG1 exhibits clear substrate preferences among glucosinolates (wittstock2010glucosinolatebreakdownin pages 2-4). The enzyme displays strongest activity toward:
- **Allylglucosinolate (sinigrin)**: Km = 45 mM, Vmax = 2.2 μmol·min⁻¹·mg protein⁻¹
- **3-Butenylglucosinolate**
- **4-Methylsulfinylbutylglucosinolate**

These substrates are hydrolyzed at more than twice the rate of lower-activity substrates including 2(R)-2-hydroxy-3-butenylglucosinolate and 2-phenylethylglucosinolate (wittstock2010glucosinolatebreakdownin pages 2-4).

### Reaction Products and Biological Activity

The primary breakdown products under typical physiological conditions are isothiocyanates, which possess broad antimicrobial and anti-herbivore activity (somssich2025gunsinrosettes pages 3-4, wittstock2010glucosinolatebreakdownin pages 1-2). For example, hydrolysis of 4-methylsulfinylbutyl glucosinolate yields 4-methylsulfinylbutyl isothiocyanate (sulforaphane), a compound with demonstrated antimicrobial activity against fungi and bacteria (somssich2025gunsinrosettes pages 3-4). The specific product profile depends on the glucosinolate structure and the presence of specifier proteins such as epithiospecifier protein (ESP) or nitrile-specifier proteins (NSPs), which can redirect aglycone decomposition toward nitriles or other derivatives (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 8-9).

## Subcellular Localization and Tissue Expression

### Subcellular Compartmentation

TGG1 is primarily a vacuolar protein, as demonstrated by immunogold labeling and identification in the leaf vacuolar proteome (wittstock2010glucosinolatebreakdownin pages 2-4, liebminger2012myrosinasestgg1and pages 4-5). The protein contains an N-terminal signal peptide directing it through the secretory pathway and carries extensive N-glycosylation characteristic of vacuolar glycoproteins (liebminger2012myrosinasestgg1and pages 2-4, liebminger2012myrosinasestgg1and pages 1-2). TGG1 has also been detected in soluble fractions by differential centrifugation, suggesting the protein exists as a soluble luminal protein within vacuoles (wittstock2010glucosinolatebreakdownin pages 2-4). This vacuolar localization is functionally significant because it spatially separates the enzyme from its glucosinolate substrates until tissue disruption brings them into contact (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2).

### Tissue and Cellular Expression Patterns

TGG1 expression is predominantly restricted to above-ground organs (wittstock2010glucosinolatebreakdownin pages 1-2). At the cellular level, the enzyme shows particularly strong accumulation in:

1. **Stomatal Guard Cells**: TGG1 is exceptionally abundant in guard cells and has been described as one of the most abundant proteins in these cells (wittstock2010glucosinolatebreakdownin pages 2-4, rhaman2020myrosinasestgg1and pages 5-6). This localization positions TGG1 to participate in stomatal immunity and stress-responsive regulation of stomatal aperture.

2. **Myrosin Cells**: TGG1 accumulates in specialized idioblast cells called myrosin cells, located in the phloem parenchyma near vascular tissues (liebminger2012myrosinasestgg1and pages 4-5, rahman2018arabidopsismyrosinases;analysis pages 7-11, wittstock2010glucosinolatebreakdownin pages 1-2). These cells provide a compartmentalized storage system for myrosinase enzymes that can be rapidly deployed upon tissue damage.

3. **Phloem and Vascular Tissues**: TGG1 is expressed in phloem-associated cells, vascular bundle parenchyma, and leaf veins (rahman2018arabidopsismyrosinases;analysis pages 21-25, wittstock2010glucosinolatebreakdownin pages 1-2).

4. **Rosette Leaves**: Young rosette leaves represent a principal site of TGG1 protein accumulation, with myrosinase activity highest around three weeks of age and declining markedly in senescent leaves (wittstock2010glucosinolatebreakdownin pages 2-4).

5. **Reproductive Organs**: TGG1 protein or promoter activity has been detected in flowers, sepals, petals, gynoecia, anthers, and siliques, though generally at lower abundance than in rosette leaves (rahman2018arabidopsismyrosinases;analysis pages 17-21, rahman2018arabidopsismyrosinases;analysis pages 7-11).

### Post-Translational Modification: N-Glycosylation

TGG1 is extensively N-glycosylated, with all nine potential N-glycosylation sites occupied (liebminger2012myrosinasestgg1and pages 2-4, liebminger2012myrosinasestgg1and pages 1-2). Uniquely among many plant glycoproteins, TGG1 carries exclusively oligomannosidic N-glycans rather than complex or paucimannosidic structures (liebminger2012myrosinasestgg1and pages 2-4, liebminger2012myrosinasestgg1and pages 5-6). The predominant glycoform is Man5GlcNAc2, specifically the (M6M3)M isomer, accounting for approximately 56.8% of the glycan pool, with additional Man6–Man9 structures also present (liebminger2012myrosinasestgg1and pages 2-4, liebminger2012myrosinasestgg1and pages 4-5). These glycans are trimmed by Golgi α-mannosidases MNS1, MNS2, and MNS3, but are not further processed by N-acetylglucosaminyltransferase I to generate complex N-glycans (liebminger2012myrosinasestgg1and pages 5-6). The protein migrates at approximately 75 kDa on SDS-PAGE, with mobility varying according to glycan processing state (liebminger2012myrosinasestgg1and pages 2-4).

## Biochemical Pathways and Biological Processes

### The Glucosinolate-Myrosinase "Mustard Oil Bomb" Defense System

TGG1 is a central component of the glucosinolate-myrosinase defense system, often termed the "mustard oil bomb" (zhang2019overexpressingthemyrosinase pages 1-2, chhajed2020glucosinolatebiosynthesisand pages 9-11, somssich2025gunsinrosettes pages 3-4). Under normal conditions, glucosinolates are stored in S-cells of the vacuole, while myrosinases like TGG1 reside in separate myrosin cells (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). When herbivores chew plant tissue or pathogens penetrate cells, this spatial separation breaks down, allowing TGG1 to hydrolyze glucosinolates and release toxic or deterrent isothiocyanates and related compounds (somssich2025gunsinrosettes pages 3-4, wittstock2010glucosinolatebreakdownin pages 1-2).

### Defense Against Herbivores

TGG1-mediated glucosinolate hydrolysis provides protection against diverse herbivores including spider mites, caterpillars, and other chewing insects (chhajed2020glucosinolatebiosynthesisand pages 9-11, somssich2025gunsinrosettes pages 3-4). The isothiocyanate products are generally more toxic to generalist herbivores than alternative products like simple nitriles (wittstock2010glucosinolatebreakdownin pages 8-9). Genetic studies have demonstrated that plants carrying tgg1 tgg2 double mutations show increased susceptibility to herbivores, confirming the defensive role of these enzymes (wittstock2010glucosinolatebreakdownin pages 2-4). The breakdown products not only exert direct toxicity but can also deter oviposition and recruit parasitoid wasps through volatile signals, supporting indirect tritrophic defense (wittstock2010glucosinolatebreakdownin pages 8-9, wittstock2010glucosinolatebreakdownin pages 9-10).

### Pathogen Defense and Antimicrobial Activity

TGG1 contributes to broad-spectrum antimicrobial defense through the production of isothiocyanates with antibacterial and antifungal properties (somssich2025gunsinrosettes pages 3-4, chhajed2020glucosinolatebiosynthesisand pages 9-11). For instance, sulforaphane (4-methylsulfinylbutyl isothiocyanate) produced from 4-methylsulfinylbutyl glucosinolate accumulates in infected leaves and exhibits antimicrobial activity against various fungal and bacterial pathogens (somssich2025gunsinrosettes pages 3-4). Plants lacking both TGG1 and TGG2 show greater susceptibility to the fungal pathogen *Sclerotinia sclerotiorum*, supporting a direct defensive contribution (somssich2025gunsinrosettes pages 3-4).

### Stomatal Immunity Against Bacterial Pathogens

Recent research has revealed a critical role for TGG1 in stomatal immunity, particularly against bacterial pathogens like *Pseudomonas syringae* pv. tomato DC3000 (zhang2019overexpressingthemyrosinase pages 1-2, zhang2019overexpressingthemyrosinase pages 7-9). Guard-cell-enriched TGG1 links glucosinolate metabolism to pathogen-triggered stomatal closure, creating a physical barrier that restricts bacterial entry through natural leaf pores (zhang2019overexpressingthemyrosinase pages 1-2, zhang2019overexpressingthemyrosinase pages 9-12). Arabidopsis plants overexpressing a broccoli TGG1 homolog (BoTGG1) showed:

- More rapid stomatal closure upon pathogen challenge
- Prevention of pathogen-induced stomatal reopening
- Enhanced resistance to *P. syringae* DC3000
- Increased sensitivity to ABA and salicylic acid (SA)-induced closure
- Reduced sensitivity to auxin (IAA)-mediated inhibition of closure

These effects involved transcriptional regulation of ABA pathway negative regulators (ABI1, ABI2, PP2CA), SA-associated genes (NPR1, LOX1), and stomatal closure regulators (OST1, GHR1), ultimately activating the guard-cell anion channel SLAC1 to promote closure (zhang2019overexpressingthemyrosinase pages 7-9, zhang2019overexpressingthemyrosinase pages 9-12). Enhanced resistance persisted even in syringe-infiltration assays that bypass stomata, suggesting TGG1 also activates additional post-entry immune defenses, potentially through isothiocyanate-mediated antimicrobial activity or hypersensitive-response-associated programmed cell death (zhang2019overexpressingthemyrosinase pages 9-12).

### Guard Cell Signaling Pathways

TGG1 functions in complex guard-cell signaling networks beyond simple glucosinolate hydrolysis (rhaman2020myrosinasestgg1and pages 3-4, rhaman2020myrosinasestgg1and pages 12-13, rhaman2020myrosinasestgg1and pages 5-6). In ABA and methyl jasmonate (MeJA) signaling pathways, TGG1 and TGG2 act redundantly downstream of reactive oxygen species (ROS) and reactive carbonyl species (RCS) production, and upstream of cytosolic alkalization and Ca²⁺ elevation required for stomatal closure (rhaman2020myrosinasestgg1and pages 3-4, rhaman2020myrosinasestgg1and pages 6-7, rhaman2020myrosinasestgg1and pages 11-12).

Studies with the reactive carbonyl species acrolein demonstrated that either TGG1 or TGG2 alone is sufficient for acrolein-induced stomatal closure, but loss of both enzymes abolishes this response (rhaman2020myrosinasestgg1and pages 6-7). The tgg1 tgg2 double mutant fails to show normal acrolein-induced cytosolic Ca²⁺ elevation, while exogenous Ca²⁺ can still induce responses, placing the myrosinases upstream of Ca²⁺ signaling (rhaman2020myrosinasestgg1and pages 12-13, rhaman2020myrosinasestgg1and pages 11-12). Interestingly, because myrosinases are normally spatially separated from glucosinolates in intact cells, whether conventional glucosinolate hydrolysis is required for these signaling functions remains unresolved; TGG1 and TGG2 may interact directly with ABA signaling components through unknown mechanisms (rhaman2020myrosinasestgg1and pages 12-13).

A 2025 study further demonstrated that allyl isothiocyanate (AITC), a glucosinolate breakdown product, triggers stomatal closure, ROS production, nitric oxide generation, cytosolic alkalization, and Ca²⁺ oscillations in guard cells (oumaima2025tgg1andtgg2 pages 1-2). AITC induced closure in either single mutant but not in the tgg1 tgg2 double mutant, suggesting TGG1 and TGG2 act downstream of these early signals rather than merely generating the isothiocyanate.

### Functional Redundancy with TGG2

TGG1 and TGG2 are closely related, tandemly duplicated genes that function redundantly in glucosinolate breakdown and guard-cell signaling (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). Loss of either gene alone has minimal effect on glucosinolate hydrolysis in disrupted leaves, whereas the double mutant completely lacks detectable myrosinase activity toward exogenous allylglucosinolate and fails to break down endogenous aliphatic glucosinolates (wittstock2010glucosinolatebreakdownin pages 2-4). However, the two enzymes are not entirely identical in distribution: TGG1 is much more abundant in Col-0 rosette leaves and strongly enriched in guard cells, while TGG2 is more prominent in phloem-associated cells and reproductive organs (wittstock2010glucosinolatebreakdownin pages 2-4, rhaman2020myrosinasestgg1and pages 5-6, rahman2018arabidopsismyrosinases;analysis pages 17-21). This partial functional division allows coordinated but tissue-specific deployment of myrosinase activity across aerial organs.

## Recent Developments (2023–2025)

### Alternative Jasmonate Signaling Pathway

A groundbreaking 2024 study (published in *Frontiers in Plant Science* March 2026) discovered that prolonged airborne methyl jasmonate (MeJA) exposure induces TGG1 and TGG2 expression through a COI1-independent pathway (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 1-4, mirzaei2026longtermmethyljasmonate pages 1-2). After five days of MeJA treatment, TGG1 transcript and protein levels increased significantly even in coi1-16 and myc2,3,4 mutants, which lack the canonical JA-Ile–COI1–JAZ–MYC2/3/4 signaling pathway (mirzaei2024longtermexposureto pages 1-4, mirzaei2024longtermexposureto pages 9-12). This finding challenges the prevailing model of jasmonate-regulated defense gene expression and suggests that duration-dependent alternative regulatory mechanisms exist for TGG1 induction. The molecular identity of the alternative pathway remains unknown, though it appears distinct from FAMA-mediated myrosin-cell specification (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 9-12).

### Integration with Light and Developmental Signaling

A 2023 study demonstrated that the B-Box transcription factor AtBBX29 integrates photomorphogenesis with defense responses by promoting glucosinolate accumulation in *Arabidopsis* leaves. AtBBX29 upregulates MYB34 and MYB51, transcription factors involved in glucosinolate biosynthesis, and its overexpression increased resistance to both the necrotrophic fungus *Botrytis cinerea* and the herbivore *Spodoptera frugiperda*. This work highlights how light signaling pathways can coordinate with the glucosinolate-myrosinase system to modulate plant defense capacity.

### Glucosinolate Diversity and Microbiome Interactions

A 2024 *Nature Communications* study revealed that glucosinolate structural diversity shapes recruitment of leaf-associated bacteria in *Arabidopsis*. Different glucosinolate profiles (allyl-glucosinolate vs. 4-methylsulfinylbutyl-glucosinolate) selectively enriched specific bacterial taxa, likely through bacterial myrosinase specificity and subsequent metabolic cross-feeding among bacteria. This finding expands the ecological roles of the glucosinolate-myrosinase system beyond direct defense to include regulation of beneficial microbiome assembly.

### Contemporary Reviews and Perspectives

A comprehensive 2025 review in *Plant Physiology* characterized the glucosinolate-myrosinase system as part of *Arabidopsis*'s "chemical weapons arsenal" (somssich2025gunsinrosettes pages 3-4). This review emphasized the context-dependent nature of defense: for example, 8-methylsulfinyloctyl isothiocyanate showed stronger activity against *Sclerotinia sclerotiorum* than the shorter-chain sulforaphane, illustrating how side-chain structure fine-tunes antimicrobial specificity (somssich2025gunsinrosettes pages 3-4). The review also distinguished classical TGG enzymes from atypical myrosinases like PEN2, which have specialized roles in nonhost immunity and subcellular compartments.

## Summary Tables

| Property | TGG1 annotation or experimental finding | Evidence |
|---|---|---|
| Gene identity | **TGG1**; ordered locus **At5g26000**; synonym **BGLU38** | TGG1 is identified as the classical *Arabidopsis thaliana* myrosinase encoded by At5g26000/BGLU38. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| UniProt accession | **P37702** | Target identity specified for this report; literature independently associates TGG1 with At5g26000/BGLU38. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| Protein names | **Myrosinase 1**; **thioglucoside glucohydrolase 1**; **β-glucosidase 38**; **sinigrinase 1** | The literature consistently classifies TGG1 as a classical plant myrosinase/thioglucoside glucohydrolase. (wittstock2010glucosinolatebreakdownin pages 1-2) |
| Enzyme classification | Glycoside hydrolase family 1 (**GH1**) β-glycosidase; classical myrosinase | TGG1 belongs to the phylogenetically distinct family-I myrosinases and possesses the characteristic modified catalytic motif of this enzyme class. (wittstock2010glucosinolatebreakdownin pages 1-2) |
| EC numbers | **EC 3.2.1.147** (thioglucosidase/myrosinase); also annotated **EC 3.2.1.21** (β-glucosidase) | Its experimentally supported principal activity is glucosinolate thioglucoside hydrolysis. (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2) |
| Apparent molecular mass | Approximately **75 kDa** by SDS–PAGE for endogenous glycosylated TGG1 | Electrophoretic mobility varies with N-glycan processing, consistent with a heavily glycosylated mature protein. (liebminger2012myrosinasestgg1and pages 2-4) |
| Primary reaction | Glucosinolate + H₂O → **D-glucose + sulfate + an unstable thiohydroximate-derived aglycone**; the aglycone then rearranges or is redirected into several bioactive products | TGG1 cleaves the glucosinolate thioglucosidic bond; downstream product identity is not determined by TGG1 alone. (shazada2015studiesofexpression pages 6-10, wittstock2010glucosinolatebreakdownin pages 1-2) |
| Catalytic mechanism | Retaining GH1-type glycoside hydrolysis, modified in classical myrosinases by replacement of the usual catalytic acid/base glutamate with **glutamine** in a TI/LNQL/P-like motif; **ascorbate** is proposed to supply acid/base catalytic assistance | This glutamate-to-glutamine substitution and ascorbate dependence distinguish classical myrosinases from conventional GH1 β-glucosidases. (wittstock2010glucosinolatebreakdownin pages 1-2, chhajed2020glucosinolatebiosynthesisand pages 9-11) |
| Cofactor/modulator | **Ascorbate** activates myrosinase activity at low concentrations but can inhibit it at high concentrations | Ascorbate is both a catalytic activator and a concentration-dependent regulator. (shazada2015studiesofexpression pages 6-10) |
| Demonstrated assay substrate | **Allyl glucosinolate (sinigrin)** | TGG1 activity is commonly quantified by measuring glucose released from sinigrin. (shazada2015studiesofexpression pages 19-26, rahman2018arabidopsismyrosinases;analysis pages 25-30) |
| Reported sinigrin kinetics | **Kₘ = 45 mmol·L⁻¹**; **Vmax = 2.2 mmol·min⁻¹·mg protein⁻¹**, as reported for recombinant His-tagged TGG1 expressed in *Pichia pastoris* | Values should be interpreted in the context of the recombinant preparation and the units reported by the cited review. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| Preferred substrates in comparative assays | **Allyl glucosinolate**, **3-butenyl glucosinolate**, and **4-methylsulfinylbutyl glucosinolate** | These substrates were hydrolyzed at more than twice the rates observed for the lower-activity substrates in the same comparative assays. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| Lower-activity substrates | **2(R)-2-hydroxy-3-butenyl glucosinolate** and **2-phenylethyl glucosinolate** | TGG1 hydrolyzed these compounds less rapidly than allyl-, 3-butenyl-, and 4-methylsulfinylbutyl glucosinolates. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| Default downstream product | **Isothiocyanate** when the unstable aglycone rearranges without product-specifier activity | Isothiocyanates are generally the principal toxic or antimicrobial products of unredirected glucosinolate hydrolysis. (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2) |
| Alternative downstream products | **Simple nitriles, epithionitriles, thiocyanates, oxazolidine-2-thiones**, and substrate-specific secondary products such as goitrin or indole-3-carbinol | Product outcome depends on substrate side chain, pH, metal ions, glutathione, and specifier or associated proteins—not on TGG1 specificity alone. (wittstock2010glucosinolatebreakdownin pages 2-4, chhajed2020glucosinolatebiosynthesisand pages 9-11) |
| Example bioactive product | Hydrolysis of 4-methylsulfinylbutyl glucosinolate can yield **4-methylsulfinylbutyl isothiocyanate (sulforaphane)** | Sulforaphane and related isothiocyanates have antimicrobial activity, although production in planta reflects the combined glucosinolate–myrosinase system rather than TGG1 alone. (somssich2025gunsinrosettes pages 3-4) |
| N-glycosylation | TGG1 has **nine occupied N-glycosylation sites** and carries exclusively **oligomannosidic N-glycans** | Glycopeptide mass spectrometry found occupancy at every predicted site. (liebminger2012myrosinasestgg1and pages 2-4, liebminger2012myrosinasestgg1and pages 1-2) |
| Predominant N-glycan | **Man5GlcNAc2**, especially the (M6M3)M isomer; Man6–Man9 structures also occur | In wild type, Man5 represented **56.8%** of the reported glycan pool; glycan distributions shift in α-mannosidase mutants. (liebminger2012myrosinasestgg1and pages 2-4, liebminger2012myrosinasestgg1and pages 4-5) |
| N-glycan processing | Glycans are trimmed by Golgi α-mannosidases **MNS1, MNS2, and MNS3** but are not substantially converted into hybrid or complex plant N-glycans | The unusual oligomannose-only profile may reflect glycan inaccessibility, cell-specific processing, or sub-Golgi compartmentation. (liebminger2012myrosinasestgg1and pages 5-6, liebminger2012myrosinasestgg1and pages 1-2) |
| Functional significance of glycosylation | Not fully resolved; altered abundance and mobility in glycan-processing mutants suggest possible effects on **protein stability, maturation, or trafficking** | These consequences remain mechanistic hypotheses rather than fully established functions. (liebminger2012myrosinasestgg1and pages 2-4, liebminger2012myrosinasestgg1and pages 1-2) |


*Table: This table consolidates the verified identity, catalytic reaction, substrate preferences, reported kinetic parameters, product chemistry, and N-glycosylation of Arabidopsis TGG1. It distinguishes TGG1-catalyzed bond cleavage from downstream product selection controlled by chemical conditions and specifier proteins.*

| Localization or expression feature | TGG1 evidence and interpretation | Comparison with TGG2 |
|---|---|---|
| **Identity and broad distribution** | *Arabidopsis thaliana* TGG1 (At5g26000/BGLU38; UniProt P37702) is a classical glycoside-hydrolase-family-1 myrosinase expressed predominantly in aerial tissues. (wittstock2010glucosinolatebreakdownin pages 1-2) | TGG1 and TGG2 are closely related, tandemly duplicated classical myrosinases with overlapping expression and function in above-ground organs. (wittstock2010glucosinolatebreakdownin pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2) |
| **Vacuole** | Immunogold labeling and leaf-vacuolar proteomics support localization of TGG1 to vacuoles. Secretory-pathway targeting, N-glycosylation, and trafficking-mutant phenotypes further support its assignment as a vacuolar glycoprotein. (wittstock2010glucosinolatebreakdownin pages 2-4, liebminger2012myrosinasestgg1and pages 4-5, liebminger2012myrosinasestgg1and pages 2-4) | TGG2 is also principally associated with leaf vacuoles and follows a similar secretory-trafficking route. (liebminger2012myrosinasestgg1and pages 4-5, wittstock2010glucosinolatebreakdownin pages 2-4) |
| **Soluble fraction and localization uncertainty** | Differential centrifugation detected TGG1 in a soluble fraction, while computational predictions have suggested extracellular, chloroplast, or vacuolar targeting. The combined evidence favors a soluble protein within the vacuolar lumen, although potentially distinct pools remain unresolved. (wittstock2010glucosinolatebreakdownin pages 2-4) | TGG2 also occurs in vacuolar contexts, although trafficking-dependent aggregation may distinguish its behavior from TGG1 in intact cells. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| **Specialized myrosin cells** | TGG1 accumulates in specialized myrosin idioblasts located near veins and phloem-associated tissues. This organization helps spatially separate myrosinase from glucosinolate stores until tissue damage permits enzyme–substrate contact. (liebminger2012myrosinasestgg1and pages 4-5, rahman2018arabidopsismyrosinases;analysis pages 7-11, wittstock2010glucosinolatebreakdownin pages 1-2) | Both enzymes occur in the classical myrosin-cell system and jointly provide much of the myrosinase activity in disrupted leaves. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| **Stomatal guard cells** | TGG1 is exceptionally abundant in guard cells and has been described as one of their most abundant proteins. Proteomic, reporter, and functional evidence supports guard-cell expression, although some earlier transcript and antibody studies gave conflicting results. (wittstock2010glucosinolatebreakdownin pages 2-4, zhang2019overexpressingthemyrosinase pages 1-2, rhaman2020myrosinasestgg1and pages 5-6) | TGG1 is substantially more prominent than TGG2 in guard cells; TGG2 is generally reported as absent or much less abundant there, despite functional redundancy in guard-cell signaling assays. (wittstock2010glucosinolatebreakdownin pages 2-4, rhaman2020myrosinasestgg1and pages 5-6, rahman2018arabidopsismyrosinases;analysis pages 17-21) |
| **Phloem and vascular-associated cells** | TGG1 is expressed in phloem-associated cells, vascular-bundle parenchyma, leaf veins, and other vascular regions, placing it near glucosinolate-rich transport and storage tissues. (rahman2018arabidopsismyrosinases;analysis pages 21-25, wittstock2010glucosinolatebreakdownin pages 1-2) | TGG2 is strongly associated with phloem-adjacent cells and may make a proportionally larger contribution there than in guard cells. (wittstock2010glucosinolatebreakdownin pages 2-4, rhaman2020myrosinasestgg1and pages 5-6) |
| **Rosette leaves** | Rosette leaves are a principal site of TGG1 accumulation. TGG1 is the dominant classical myrosinase in Col-0 leaves and contributes strongly to foliar glucosinolate hydrolysis. (wittstock2010glucosinolatebreakdownin pages 2-4, rahman2018arabidopsismyrosinases;analysis pages 7-11) | TGG2 overlaps with TGG1 in leaves but is less abundant in Col-0 rosettes. Disruption of both genes is generally needed to abolish classical activity toward aliphatic glucosinolates in damaged leaves. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| **Leaf age and development** | Foliar myrosinase activity is highest in young rosette leaves—reported around three weeks of age—and declines markedly in senescent leaves. TGG1 reporter expression can shift from a broad pattern in young leaves toward vascular tissue and the leaf periphery during maturation. (wittstock2010glucosinolatebreakdownin pages 2-4, rahman2018arabidopsismyrosinases;analysis pages 17-21) | TGG1's greater leaf abundance makes it the likely principal contributor to the activity peak in young rosettes, although TGG2 provides overlapping activity. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| **Flowers and floral organs** | TGG1 protein or promoter activity has been detected in flowers and in sepals, petals, gynoecia, and anthers, although individual localization studies are not fully concordant. (rahman2018arabidopsismyrosinases;analysis pages 17-21, rahman2018arabidopsismyrosinases;analysis pages 7-11) | Both genes are expressed in flowers; TGG2 may be proportionally more prominent in reproductive organs than in vegetative rosette leaves. (rahman2018arabidopsismyrosinases;analysis pages 17-21, rahman2018arabidopsismyrosinases;analysis pages 7-11) |
| **Siliques** | TGG1 occurs in siliques, generally at lower abundance than in rosette leaves or flowers. (rahman2018arabidopsismyrosinases;analysis pages 17-21, rahman2018arabidopsismyrosinases;analysis pages 7-11, liebminger2012myrosinasestgg1and pages 1-2) | TGG2 is relatively prominent in siliques and flowers, suggesting complementary quantitative contributions across reproductive tissues. (rahman2018arabidopsismyrosinases;analysis pages 17-21, rahman2018arabidopsismyrosinases;analysis pages 7-11) |
| **Roots** | Authoritative surveys characterize TGG1 mainly as an aerial myrosinase and often report little or no root expression. Some promoter-reporter lines nevertheless detected localized main-root expression under particular ages or soil-grown conditions, probably reflecting developmental or experimental context rather than strong constitutive expression. (rahman2018arabidopsismyrosinases;analysis pages 14-17, liebminger2012myrosinasestgg1and pages 1-2, rahman2018arabidopsismyrosinases;analysis pages 17-21, wittstock2010glucosinolatebreakdownin pages 1-2) | TGG2 is likewise primarily aerial; root glucosinolate hydrolysis is more strongly associated with other myrosinases such as TGG4 and TGG5. (wittstock2010glucosinolatebreakdownin pages 1-2, rahman2018arabidopsismyrosinases;analysis pages 7-11) |
| **Seeds** | Evidence is inconsistent: established surveys describe TGG1 as absent from seeds, whereas some promoter–GUS experiments reported signal in mature embryo cotyledons or seed-associated tissues but not young seeds. Reporter activity should not be equated automatically with confirmed endogenous protein abundance. (rahman2018arabidopsismyrosinases;analysis pages 17-21, wittstock2010glucosinolatebreakdownin pages 1-2, rahman2018arabidopsismyrosinases;analysis pages 14-17) | Available evidence does not establish TGG1 or TGG2 as major seed-localized classical myrosinases. |
| **Stress-responsive expression** | Wounding can enhance reporter signal or apparent myrosin-cell formation near damaged areas. Pathogen-associated treatments and prolonged methyl jasmonate exposure can also elevate TGG1 expression or protein abundance in leaves. (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 1-4, rahman2018arabidopsismyrosinases;analysis pages 25-30, rahman2018arabidopsismyrosinases;analysis pages 17-21) | TGG2 is commonly induced alongside TGG1 during prolonged methyl jasmonate exposure, consistent with coordinated but nonidentical regulation. (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 1-4) |
| **Overall abundance and functional division** | TGG1 is most abundant in young rosette leaves and is particularly enriched in guard cells, specialized myrosin cells, and phloem/vascular-associated cells. This distribution supports both damage-triggered glucosinolate hydrolysis and intact-cell guard-cell signaling. (wittstock2010glucosinolatebreakdownin pages 2-4, rhaman2020myrosinasestgg1and pages 5-6) | TGG2 supplies overlapping catalytic capacity, especially in phloem-associated and reproductive tissues. Single mutants often retain substantial function, whereas double mutants reveal strong redundancy in foliar hydrolysis and guard-cell signaling. (wittstock2010glucosinolatebreakdownin pages 2-4, rhaman2020myrosinasestgg1and pages 3-4, rhaman2020myrosinasestgg1and pages 6-7) |


*Table: This table summarizes the subcellular, cellular, tissue-level, developmental, and stress-responsive distribution of Arabidopsis TGG1. It also distinguishes TGG1's strong enrichment in guard cells and young rosette leaves from the overlapping but nonidentical distribution of TGG2.*

| Biological role/process | TGG1 mechanism and pathway position | Experimental or biochemical evidence | Relevant targets/outcomes | Relationship with TGG2 | Key sources |
|---|---|---|---|---|---|
| Damage-activated chemical defense (“mustard oil bomb”) | TGG1 hydrolyzes the thioglucosidic bond of stored glucosinolates after tissue disruption, releasing glucose and an unstable aglycone. The aglycone usually rearranges to an isothiocyanate; specifier proteins can redirect it toward nitriles, epithionitriles, or thiocyanates. | Recombinant TGG1 preferentially hydrolyzes allyl-, 3-butenyl-, and 4-methylsulfinylbutyl-glucosinolates; these substrates are processed more than twice as rapidly as 2-hydroxy-3-butenyl- and 2-phenylethyl-glucosinolates. | Rapid production of reactive metabolites in damaged shoots; deterrence or toxicity toward herbivores and antimicrobial activity against pathogens. | Either single mutant retains substantial activity, whereas the double mutant lacks detectable sinigrin activity and fails to break down endogenous aliphatic glucosinolates in disrupted leaves. | (wittstock2010glucosinolatebreakdownin pages 2-4) |
| Isothiocyanate-mediated antimicrobial defense | Without product-specifier activity, TGG1-initiated hydrolysis favors electrophilic, lipophilic isothiocyanates. Hydrolysis of 4-methylsulfinylbutyl glucosinolate can yield sulforaphane. | Isothiocyanates are broadly antimicrobial; infected Arabidopsis leaves accumulate sulforaphane, while 8-methylsulfinyloctyl isothiocyanate showed stronger activity against *Sclerotinia sclerotiorum*. | Bacteria and fungi; chemical inhibition of infection and possible signaling or programmed-cell-death effects. | Greater susceptibility of the *tgg1 tgg2* double mutant to *S. sclerotiorum* supports a combined contribution, but individual products cannot generally be assigned uniquely to TGG1. | (somssich2025gunsinrosettes pages 3-4, zhang2019overexpressingthemyrosinase pages 9-12, wittstock2010glucosinolatebreakdownin pages 1-2) |
| Anti-herbivore defense | TGG1 converts relatively inert glucosinolate stores into toxic or deterrent compounds after feeding damage. Product identity depends on substrate side chain, pH, cofactors, and specifier proteins; isothiocyanates are generally more toxic to generalist chewing insects than corresponding simple nitriles. | Genetic and ecological studies associate TGG1/TGG2-dependent glucosinolate activation with resistance to spider mites and caterpillars. Nitriles may be less directly toxic but can deter oviposition or recruit parasitoids. | Two-spotted spider mites, caterpillars, and other chewing herbivores; direct toxicity, feeding deterrence, oviposition deterrence, and indirect tritrophic defense. | TGG1 and TGG2 act redundantly in shoot defense. Some indole-glucosinolate defenses, including a reported aphid antifeedant pathway, are TGG1/TGG2-independent. | (chhajed2020glucosinolatebiosynthesisand pages 9-11, somssich2025gunsinrosettes pages 3-4, wittstock2010glucosinolatebreakdownin pages 8-9) |
| Stomatal immunity against bacterial entry | Guard-cell-enriched TGG1 links glucosinolate metabolism to pathogen-triggered stomatal closure, strengthening the physical barrier at leaf pores and resisting pathogen-induced reopening. | Arabidopsis overexpressing broccoli **BoTGG1** closed stomata more rapidly and resisted reopening after challenge with *Pseudomonas syringae* pv. tomato DC3000. Resistance persisted after syringe infiltration that bypassed stomata, suggesting additional defenses. | *P. syringae* pv. tomato DC3000; reduced bacterial entry and enhanced post-entry resistance. | Mutant studies indicate overlapping TGG1/TGG2 signaling functions. Because the overexpression experiment used a broccoli homolog, it supports but does not prove every proposed endogenous AtTGG1 mechanism. | (zhang2019overexpressingthemyrosinase pages 1-2, zhang2019overexpressingthemyrosinase pages 7-9, zhang2019overexpressingthemyrosinase pages 9-12) |
| ABA- and MeJA-regulated guard-cell signaling | TGG1/TGG2 act downstream of reactive oxygen species and reactive carbonyl species, including acrolein, and upstream of cytosolic alkalization and Ca²⁺ elevation required for stomatal closure. | Acrolein induced closure in wild type and either single mutant but not in the *tgg1 tgg2* double mutant. The double mutant lacked normal acrolein-induced cytosolic Ca²⁺ elevation, whereas exogenous Ca²⁺ retained activity. | ABA- and methyl-jasmonate-mediated stress responses; stomatal closure can restrict pathogen entry and reduce water loss. | Either enzyme is sufficient for much of the response, while loss of both produces a clear signaling defect. Whether conventional glucosinolate hydrolysis is required in intact guard cells remains unresolved. | (rhaman2020myrosinasestgg1and pages 3-4, rhaman2020myrosinasestgg1and pages 12-13, rhaman2020myrosinasestgg1and pages 6-7, rhaman2020myrosinasestgg1and pages 11-12) |
| Salicylic-acid-associated stomatal defense | Elevated myrosinase activity increases sensitivity to SA-induced stomatal closure and enhances responses involving NPR1, OST1, GHR1, and downstream SLAC1 activation. | **BoTGG1**-overexpressing plants showed enhanced SA- and ABA-induced closure and stronger transient defense-gene responses during *P. syringae* infection. | Bacterial stomatal immunity; integration of specialized-metabolite activation with hormone-controlled pore regulation. | Evidence is strongest from TGG1-homolog overexpression; the division of endogenous signaling labor between AtTGG1 and AtTGG2 remains incompletely resolved. | (zhang2019overexpressingthemyrosinase pages 1-2, zhang2019overexpressingthemyrosinase pages 7-9) |
| Allyl-isothiocyanate guard-cell signaling | Allyl isothiocyanate triggers ROS and nitric oxide production, cytosolic alkalization, Ca²⁺ oscillations, and stomatal closure. TGG1/TGG2 appear to act downstream of these early signals rather than merely generating allyl isothiocyanate. | Allyl isothiocyanate at 50–100 µM induced closure in either single mutant but not in the double mutant, although early ROS, NO, pH, and Ca²⁺ responses occurred. | Links glucosinolate catabolites to stomatal behavior and potentially to defense against organisms entering through stomata. | The single- versus double-mutant phenotype demonstrates redundancy. A noncanonical signaling or protein-interaction function has been proposed but not established. | (oumaima2025tgg1andtgg2 pages 1-2) |
| Long-term jasmonate regulation | Prolonged airborne MeJA exposure increases TGG1 transcript and protein abundance. Induction can persist outside the canonical JA-Ile–COI1–JAZ–MYC2/3/4 route, suggesting a duration-dependent alternative pathway. | A 2024 preprint reported induction after five days in **coi1-16** and **myc2 myc3 myc4** mutants despite loss of standard jasmonate responses. The upstream regulator remained unknown. | Sustained preparation of leaf chemical defenses during prolonged wound or herbivory signaling. | TGG1 and TGG2 were co-induced, consistent with coordinated reinforcement of the shoot myrosinase system. The 2024 evidence was a preprint. | (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 1-4, mirzaei2024longtermexposureto pages 9-12) |
| Overall functional division with TGG2 | TGG1 supplies dominant myrosinase abundance in rosette leaves and guard cells, whereas TGG2 is more associated with phloem-related and reproductive tissues. Together they support glucosinolate activation and stress signaling across aerial organs. | Single knockouts often have mild biochemical or guard-cell phenotypes; double disruption abolishes major aliphatic-glucosinolate breakdown after leaf damage and impairs RCS-, ABA-, MeJA-, and allyl-isothiocyanate-associated closure. | Broad defense against herbivores, bacteria, and fungi, plus regulation of stress-responsive stomatal aperture. | Redundancy is substantial but incomplete because abundance and cell-type distribution differ. Available evidence does not require a stable TGG1–TGG2 physical complex. | (wittstock2010glucosinolatebreakdownin pages 2-4, rhaman2020myrosinasestgg1and pages 5-6, wittstock2010glucosinolatebreakdownin pages 1-2, rahman2018arabidopsismyrosinases;analysis pages 17-21) |


*Table: This table integrates TGG1’s chemical-defense role with its functions in stomatal immunity and hormone, ROS/RCS, and Ca²⁺ signaling. It also distinguishes direct evidence from homolog-overexpression studies and summarizes functional redundancy with TGG2.*

## Conclusions

TGG1 represents a multifunctional defense enzyme in *Arabidopsis thaliana* that operates through multiple mechanisms: (1) classical damage-activated glucosinolate hydrolysis producing toxic isothiocyanates for anti-herbivore and antimicrobial defense; (2) guard-cell-specific regulation of pathogen-triggered stomatal closure through integration with ABA, SA, and JA signaling pathways; and (3) participation in ROS/RCS/Ca²⁺ signaling cascades that may be independent of conventional glucosinolate hydrolysis. The enzyme's vacuolar localization in specialized myrosin cells and guard cells enables rapid deployment upon tissue damage while maintaining spatial separation from substrates in intact tissues. Recent discoveries of COI1-independent MeJA regulation and expanding roles in microbiome interactions highlight the continuing evolution of our understanding of this well-studied but still revealing enzyme system. The substantial but incomplete functional redundancy with TGG2, combined with distinct tissue-specific expression patterns, allows flexible and robust defense responses across developmental stages and environmental challenges.

References

1. (wittstock2010glucosinolatebreakdownin pages 2-4): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

2. (wittstock2010glucosinolatebreakdownin pages 1-2): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

3. (shazada2015studiesofexpression pages 6-10): NE Shazada. Studies of expression and analysis of recombinant arabidopsis myrosinases in pichia pastoris. Unknown journal, 2015.

4. (chhajed2020glucosinolatebiosynthesisand pages 9-11): Shweta Chhajed, Islam Mostafa, Yan He, Maged Abou-Hashem, Maher El-Domiaty, and Sixue Chen. Glucosinolate biosynthesis and the glucosinolate–myrosinase system in plant defense. Agronomy, 10:1786, Nov 2020. URL: https://doi.org/10.3390/agronomy10111786, doi:10.3390/agronomy10111786. This article has 194 citations and is from a peer-reviewed journal.

5. (somssich2025gunsinrosettes pages 3-4): Marc Somssich, Daniel J Kliebenstein, and Tonni Grube Andersen. Guns in rosettes: the arabidopsis chemical weapons arsenal. Plant Physiology, Sep 2025. URL: https://doi.org/10.1093/plphys/kiaf411, doi:10.1093/plphys/kiaf411. This article has 4 citations and is from a highest quality peer-reviewed journal.

6. (wittstock2010glucosinolatebreakdownin pages 8-9): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

7. (liebminger2012myrosinasestgg1and pages 4-5): Eva Liebminger, Josephine Grass, Jakub Jez, Laura Neumann, Friedrich Altmann, and Richard Strasser. Myrosinases tgg1 and tgg2 from arabidopsis thaliana contain exclusively oligomannosidic n-glycans. Phytochemistry, 84:24-30, Dec 2012. URL: https://doi.org/10.1016/j.phytochem.2012.08.023, doi:10.1016/j.phytochem.2012.08.023. This article has 26 citations and is from a peer-reviewed journal.

8. (liebminger2012myrosinasestgg1and pages 2-4): Eva Liebminger, Josephine Grass, Jakub Jez, Laura Neumann, Friedrich Altmann, and Richard Strasser. Myrosinases tgg1 and tgg2 from arabidopsis thaliana contain exclusively oligomannosidic n-glycans. Phytochemistry, 84:24-30, Dec 2012. URL: https://doi.org/10.1016/j.phytochem.2012.08.023, doi:10.1016/j.phytochem.2012.08.023. This article has 26 citations and is from a peer-reviewed journal.

9. (liebminger2012myrosinasestgg1and pages 1-2): Eva Liebminger, Josephine Grass, Jakub Jez, Laura Neumann, Friedrich Altmann, and Richard Strasser. Myrosinases tgg1 and tgg2 from arabidopsis thaliana contain exclusively oligomannosidic n-glycans. Phytochemistry, 84:24-30, Dec 2012. URL: https://doi.org/10.1016/j.phytochem.2012.08.023, doi:10.1016/j.phytochem.2012.08.023. This article has 26 citations and is from a peer-reviewed journal.

10. (rhaman2020myrosinasestgg1and pages 5-6): Mohammad Saidur Rhaman, Toshiyuki Nakamura, Yoshimasa Nakamura, Shintaro Munemasa, and Yoshiyuki Murata. Myrosinases, tgg1 and tgg2, redundantly function in reactive carbonyl species signaling in arabidopsis guard cells. Plant & cell physiology, 61:967-977, Mar 2020. URL: https://doi.org/10.1093/pcp/pcaa024, doi:10.1093/pcp/pcaa024. This article has 34 citations and is from a domain leading peer-reviewed journal.

11. (rahman2018arabidopsismyrosinases;analysis pages 7-11): MA Rahman. Arabidopsis myrosinases; analysis of developmental expression and effects of microorganisms. Unknown journal, 2018.

12. (rahman2018arabidopsismyrosinases;analysis pages 21-25): MA Rahman. Arabidopsis myrosinases; analysis of developmental expression and effects of microorganisms. Unknown journal, 2018.

13. (rahman2018arabidopsismyrosinases;analysis pages 17-21): MA Rahman. Arabidopsis myrosinases; analysis of developmental expression and effects of microorganisms. Unknown journal, 2018.

14. (liebminger2012myrosinasestgg1and pages 5-6): Eva Liebminger, Josephine Grass, Jakub Jez, Laura Neumann, Friedrich Altmann, and Richard Strasser. Myrosinases tgg1 and tgg2 from arabidopsis thaliana contain exclusively oligomannosidic n-glycans. Phytochemistry, 84:24-30, Dec 2012. URL: https://doi.org/10.1016/j.phytochem.2012.08.023, doi:10.1016/j.phytochem.2012.08.023. This article has 26 citations and is from a peer-reviewed journal.

15. (zhang2019overexpressingthemyrosinase pages 1-2): Kaixin Zhang, Hongzhu Su, Jianxin Zhou, Wenjie Liang, Desheng Liu, and Jing Li. Overexpressing the myrosinase gene tgg1 enhances stomatal defense against pseudomonas syringae and delays flowering in arabidopsis. Frontiers in Plant Science, Oct 2019. URL: https://doi.org/10.3389/fpls.2019.01230, doi:10.3389/fpls.2019.01230. This article has 37 citations.

16. (wittstock2010glucosinolatebreakdownin pages 9-10): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

17. (zhang2019overexpressingthemyrosinase pages 7-9): Kaixin Zhang, Hongzhu Su, Jianxin Zhou, Wenjie Liang, Desheng Liu, and Jing Li. Overexpressing the myrosinase gene tgg1 enhances stomatal defense against pseudomonas syringae and delays flowering in arabidopsis. Frontiers in Plant Science, Oct 2019. URL: https://doi.org/10.3389/fpls.2019.01230, doi:10.3389/fpls.2019.01230. This article has 37 citations.

18. (zhang2019overexpressingthemyrosinase pages 9-12): Kaixin Zhang, Hongzhu Su, Jianxin Zhou, Wenjie Liang, Desheng Liu, and Jing Li. Overexpressing the myrosinase gene tgg1 enhances stomatal defense against pseudomonas syringae and delays flowering in arabidopsis. Frontiers in Plant Science, Oct 2019. URL: https://doi.org/10.3389/fpls.2019.01230, doi:10.3389/fpls.2019.01230. This article has 37 citations.

19. (rhaman2020myrosinasestgg1and pages 3-4): Mohammad Saidur Rhaman, Toshiyuki Nakamura, Yoshimasa Nakamura, Shintaro Munemasa, and Yoshiyuki Murata. Myrosinases, tgg1 and tgg2, redundantly function in reactive carbonyl species signaling in arabidopsis guard cells. Plant & cell physiology, 61:967-977, Mar 2020. URL: https://doi.org/10.1093/pcp/pcaa024, doi:10.1093/pcp/pcaa024. This article has 34 citations and is from a domain leading peer-reviewed journal.

20. (rhaman2020myrosinasestgg1and pages 12-13): Mohammad Saidur Rhaman, Toshiyuki Nakamura, Yoshimasa Nakamura, Shintaro Munemasa, and Yoshiyuki Murata. Myrosinases, tgg1 and tgg2, redundantly function in reactive carbonyl species signaling in arabidopsis guard cells. Plant & cell physiology, 61:967-977, Mar 2020. URL: https://doi.org/10.1093/pcp/pcaa024, doi:10.1093/pcp/pcaa024. This article has 34 citations and is from a domain leading peer-reviewed journal.

21. (rhaman2020myrosinasestgg1and pages 6-7): Mohammad Saidur Rhaman, Toshiyuki Nakamura, Yoshimasa Nakamura, Shintaro Munemasa, and Yoshiyuki Murata. Myrosinases, tgg1 and tgg2, redundantly function in reactive carbonyl species signaling in arabidopsis guard cells. Plant & cell physiology, 61:967-977, Mar 2020. URL: https://doi.org/10.1093/pcp/pcaa024, doi:10.1093/pcp/pcaa024. This article has 34 citations and is from a domain leading peer-reviewed journal.

22. (rhaman2020myrosinasestgg1and pages 11-12): Mohammad Saidur Rhaman, Toshiyuki Nakamura, Yoshimasa Nakamura, Shintaro Munemasa, and Yoshiyuki Murata. Myrosinases, tgg1 and tgg2, redundantly function in reactive carbonyl species signaling in arabidopsis guard cells. Plant & cell physiology, 61:967-977, Mar 2020. URL: https://doi.org/10.1093/pcp/pcaa024, doi:10.1093/pcp/pcaa024. This article has 34 citations and is from a domain leading peer-reviewed journal.

23. (oumaima2025tgg1andtgg2 pages 1-2): Kadri Oumaima, Mohammad Shakhawat Hossain, Wenxiu Ye, Eiji Okuma, Mohammad Issak, Mohammad Mahbub Islam, Misugi Uraji, Yoshimasa Nakamura, Izumi C. Mori, Shintaro Munemasa, and Yoshiyuki Murata. Tgg1 and tgg2 mutations impair allyl isothiocyanate-mediated stomatal closure in arabidopsis thaliana. Protoplasma, 262:1023-1027, Feb 2025. URL: https://doi.org/10.1007/s00709-025-02039-z, doi:10.1007/s00709-025-02039-z. This article has 1 citations and is from a peer-reviewed journal.

24. (mirzaei2024longtermexposureto pages 6-9): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

25. (mirzaei2024longtermexposureto pages 1-4): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

26. (mirzaei2026longtermmethyljasmonate pages 1-2): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Shino Goto-Yamada, Ewa Dubas, and Kenji Yamada. Long-term methyl jasmonate exposure triggers coi1-independent induction of myrosinases tgg1 and tgg2 in arabidopsis. Frontiers in Plant Science, Mar 2026. URL: https://doi.org/10.3389/fpls.2026.1801473, doi:10.3389/fpls.2026.1801473. This article has 0 citations.

27. (mirzaei2024longtermexposureto pages 9-12): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

28. (shazada2015studiesofexpression pages 19-26): NE Shazada. Studies of expression and analysis of recombinant arabidopsis myrosinases in pichia pastoris. Unknown journal, 2015.

29. (rahman2018arabidopsismyrosinases;analysis pages 25-30): MA Rahman. Arabidopsis myrosinases; analysis of developmental expression and effects of microorganisms. Unknown journal, 2018.

30. (rahman2018arabidopsismyrosinases;analysis pages 14-17): MA Rahman. Arabidopsis myrosinases; analysis of developmental expression and effects of microorganisms. Unknown journal, 2018.

## Artifacts

- [Edison artifact artifact-00](TGG1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](TGG1-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](TGG1-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. wittstock2010glucosinolatebreakdownin pages 1-2
2. wittstock2010glucosinolatebreakdownin pages 2-4
3. somssich2025gunsinrosettes pages 3-4
4. wittstock2010glucosinolatebreakdownin pages 8-9
5. zhang2019overexpressingthemyrosinase pages 9-12
6. shazada2015studiesofexpression pages 6-10
7. chhajed2020glucosinolatebiosynthesisand pages 9-11
8. zhang2019overexpressingthemyrosinase pages 1-2
9. wittstock2010glucosinolatebreakdownin pages 9-10
10. zhang2019overexpressingthemyrosinase pages 7-9
11. mirzaei2024longtermexposureto pages 6-9
12. mirzaei2024longtermexposureto pages 1-4
13. mirzaei2026longtermmethyljasmonate pages 1-2
14. mirzaei2024longtermexposureto pages 9-12
15. shazada2015studiesofexpression pages 19-26
16. https://doi.org/10.1199/tab.0134,
17. https://doi.org/10.3390/agronomy10111786,
18. https://doi.org/10.1093/plphys/kiaf411,
19. https://doi.org/10.1016/j.phytochem.2012.08.023,
20. https://doi.org/10.1093/pcp/pcaa024,
21. https://doi.org/10.3389/fpls.2019.01230,
22. https://doi.org/10.1007/s00709-025-02039-z,
23. https://doi.org/10.1101/2024.04.03.587911,
24. https://doi.org/10.3389/fpls.2026.1801473,