---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T13:57:12.112565'
end_time: '2026-09-30T14:10:43.798935'
duration_seconds: 811.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: GSTU20
  gene_symbol: GSTU20
  uniprot_accession: Q8L7C9
  protein_description: 'RecName: Full=Glutathione S-transferase U20 {ECO:0000303|PubMed:12090627};
    Short=AtGSTU20 {ECO:0000303|PubMed:12090627}; EC=2.5.1.18 {ECO:0000269|PubMed:17220357,
    ECO:0000269|PubMed:28223489}; AltName: Full=FIN219-interacting protein 1 {ECO:0000303|PubMed:17220357};
    AltName: Full=GST class-tau member 20 {ECO:0000303|PubMed:12090627};'
  gene_info: Name=GSTU20 {ECO:0000303|PubMed:12090627}; Synonyms=FIP1 {ECO:0000303|PubMed:17220357};
    OrderedLocusNames=At1g78370 {ECO:0000312|Araport:AT1G78370}; ORFNames=F3F9.11
    {ECO:0000312|EMBL:AAF71798.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the GST superfamily. Tau family. .
  protein_domains: Glutathione-S-Trfase_C-like. (IPR010987); Glutathione-S-Trfase_C_sf.
    (IPR036282); Glutathione_S-Trfase. (IPR040079); Glutathione_S-Trfase_N. (IPR004045);
    GST_C_Tau. (IPR045074)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: GSTU20-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: GSTU20-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q8L7C9
- **Protein Description:** RecName: Full=Glutathione S-transferase U20 {ECO:0000303|PubMed:12090627}; Short=AtGSTU20 {ECO:0000303|PubMed:12090627}; EC=2.5.1.18 {ECO:0000269|PubMed:17220357, ECO:0000269|PubMed:28223489}; AltName: Full=FIN219-interacting protein 1 {ECO:0000303|PubMed:17220357}; AltName: Full=GST class-tau member 20 {ECO:0000303|PubMed:12090627};
- **Gene Information:** Name=GSTU20 {ECO:0000303|PubMed:12090627}; Synonyms=FIP1 {ECO:0000303|PubMed:17220357}; OrderedLocusNames=At1g78370 {ECO:0000312|Araport:AT1G78370}; ORFNames=F3F9.11 {ECO:0000312|EMBL:AAF71798.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the GST superfamily. Tau family. .
- **Key Domains:** Glutathione-S-Trfase_C-like. (IPR010987); Glutathione-S-Trfase_C_sf. (IPR036282); Glutathione_S-Trfase. (IPR040079); Glutathione_S-Trfase_N. (IPR004045); GST_C_Tau. (IPR045074)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GSTU20" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GSTU20' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GSTU20** (gene ID: GSTU20, UniProt: Q8L7C9) in ARATH.

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
- **UniProt Accession:** Q8L7C9
- **Protein Description:** RecName: Full=Glutathione S-transferase U20 {ECO:0000303|PubMed:12090627}; Short=AtGSTU20 {ECO:0000303|PubMed:12090627}; EC=2.5.1.18 {ECO:0000269|PubMed:17220357, ECO:0000269|PubMed:28223489}; AltName: Full=FIN219-interacting protein 1 {ECO:0000303|PubMed:17220357}; AltName: Full=GST class-tau member 20 {ECO:0000303|PubMed:12090627};
- **Gene Information:** Name=GSTU20 {ECO:0000303|PubMed:12090627}; Synonyms=FIP1 {ECO:0000303|PubMed:17220357}; OrderedLocusNames=At1g78370 {ECO:0000312|Araport:AT1G78370}; ORFNames=F3F9.11 {ECO:0000312|EMBL:AAF71798.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the GST superfamily. Tau family. .
- **Key Domains:** Glutathione-S-Trfase_C-like. (IPR010987); Glutathione-S-Trfase_C_sf. (IPR036282); Glutathione_S-Trfase. (IPR040079); Glutathione_S-Trfase_N. (IPR004045); GST_C_Tau. (IPR045074)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GSTU20" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GSTU20' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GSTU20** (gene ID: GSTU20, UniProt: Q8L7C9) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive Research Report: GSTU20 (At1g78370, UniProt Q8L7C9) in Arabidopsis thaliana

### Gene Identity and Classification

GSTU20, also known as FIN219-interacting protein 1 (FIP1), is a tau-class glutathione S-transferase encoded by the *At1g78370* locus in *Arabidopsis thaliana* (chen2017structuralbasisof pages 1-1, sylvestregonon2019functionalstructuraland pages 14-16). The protein belongs to the GST superfamily, specifically the tau (GSTU) family, and carries the EC number 2.5.1.18, consistent with its glutathione S-transferase activity (chen2017structuralbasisof pages 3-4). GSTU20 adopts the canonical homodimeric GST structure, with each protomer containing an N-terminal thioredoxin-like domain and a C-terminal all-helical domain (sylvestregonon2019functionalstructuraland pages 8-9). Multiple crystal structures are available (PDB entries 5ECS, 5ECR, 5ECQ, and related structures), providing detailed structural information about this protein (sylvestregonon2019functionalstructuraland pages 8-9).

> **GSTU20/FIP1 has two experimentally supported roles in *Arabidopsis thaliana*.** As a cytosolic tau-class glutathione S-transferase, it contributes to glutathione-dependent core formation in aliphatic glucosinolate biosynthesis; *gstu20* mutants show substantial, selective reductions in aliphatic glucosinolates, particularly in leaves and seeds (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, choi2024elongatedhypocotyl5 pages 1-2, zhang2022arabidopsisglutathionestransferasesgstf11 pages 6-8).
>
> Independently, GSTU20/FIP1 is a regulatory partner of the jasmonate-amido synthetase FIN219/JAR1. It binds FIN219 directly (Kd = 1.27 ± 0.20 μM), remodels its active-site conformation, and increases its adenylation activity and capacity to produce bioactive JA–Ile (chen2017structuralbasisof pages 3-4, chen2017structuralbasisof pages 4-6, chen2017structuralbasisof pages 1-1).
>
> Because GSTU20 expression is induced by phytochrome A-dependent far-red light, the FIN219–FIP1 module provides a mechanistic bridge between environmental light perception, jasmonate signaling, and defense-related metabolism. Whether GSTU20’s glucosinolate-catalytic and FIN219-regulatory activities are directly coordinated in vivo remains unresolved (sylvestregonon2019functionalstructuraland pages 13-14).


*Blockquote: GSTU20/FIP1 couples a catalytic contribution to aliphatic glucosinolate biosynthesis with allosteric activation of FIN219-dependent jasmonate signaling. Together, these roles connect far-red-light responses with chemical defense metabolism.*

### Primary Enzymatic Function and Substrate Specificity

#### Glucosinolate Biosynthesis

The primary established enzymatic function of GSTU20 is its critical role in aliphatic glucosinolate (GSL) biosynthesis. Using CRISPR/Cas9-generated knockout mutants, Zhang et al. (2022) demonstrated that GSTU20 is essential for normal aliphatic glucosinolate production (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, zhang2022arabidopsisglutathionestransferasesgstf11 pages 1-2). Two independent *gstu20* null alleles (*gstu20-1* and *gstu20-2*) exhibited substantial reductions in aliphatic glucosinolate levels in both leaves and mature seeds, while indolic glucosinolate levels remained unchanged (zhang2022arabidopsisglutathionestransferasesgstf11 pages 6-8). This establishes pathway-class specificity for GSTU20's function.

#### Catalytic Mechanism

GSTU20 functions during the core structure formation phase of aliphatic glucosinolate biosynthesis. The enzyme catalyzes or facilitates the glutathione (GSH)-conjugation reaction that converts aliphatic precursors into S-alkylthiohydroximate intermediates (choi2024elongatedhypocotyl5 pages 1-2). Glutathione-derived conjugates serve as the sulfur donor for formation of the glucosinolate core structure, and GSTU20 catalyzes the attachment of GSH to substantial metabolic intermediates in this pathway (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10). The reaction occurs upstream of GAMMA-GLUTAMYL PEPTIDASE 1 (GGP1), which processes the glutathione-conjugated intermediate in subsequent steps (choi2024elongatedhypocotyl5 pages 1-2).

GSTU20 contains a conserved glutathione-binding pocket (G-site) with key residues including K40, E66, and S67 that coordinate GSH binding (chen2017structuralbasisof pages 3-4). While the protein retains measurable glutathione S-transferase activity, its activity against standard assay substrates is substantially weaker than reference GSTs such as *Schistosoma japonicum* GST (chen2017structuralbasisof pages 3-4). This suggests that GSTU20 has evolved specialized substrate specificity for glucosinolate pathway intermediates rather than broad-spectrum conjugation activity.

#### Functional Importance and Redundancy

Among GSTs involved in glucosinolate metabolism, GSTU20 plays the predominant role compared to the related enzyme GSTF11. The *gstu20* mutants show greater losses of aliphatic glucosinolates than *gstf11* mutants, and GSTU20 disruption causes more extensive transcriptome changes (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, zhang2022arabidopsisglutathionestransferasesgstf11 pages 1-2). However, GSTU20 and GSTF11 have partially overlapping functions, as evidenced by the observation that the double mutant *gstf11 gstu20* exhibits an additive or synergistic reduction in aliphatic glucosinolates greater than either single mutant alone (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, zhang2022arabidopsisglutathionestransferasesgstf11 pages 2-3). Importantly, the double mutant still produces some aliphatic glucosinolates, indicating that additional GST isoforms contribute to this pathway (zhang2022arabidopsisglutathionestransferasesgstf11 pages 10-11). This evidence supports a model in which GSTU20 and GSTF11 function in a dosage-dependent manner, with GSTU20 being the more important contributor (zhang2022arabidopsisglutathionestransferasesgstf11 pages 1-2, zhang2022arabidopsisglutathionestransferasesgstf11 pages 2-3).

### Regulatory Role as FIN219-Interacting Protein

#### Protein-Protein Interaction

Beyond its enzymatic role in glucosinolate biosynthesis, GSTU20 functions as a regulatory protein under its alternative designation FIP1 (FIN219-interacting protein 1). GSTU20/FIP1 directly binds to FIN219 (also known as JAR1/AtGH3.11), a jasmonate-amido synthetase that produces bioactive jasmonoyl-isoleucine (JA-Ile) (chen2017structuralbasisof pages 1-3, chen2017structuralbasisof pages 1-1). The interaction has been confirmed through multiple approaches including yeast two-hybrid, pull-down assays, co-immunoprecipitation, and quartz crystal microbalance measurements, with a measured dissociation constant (Kd) of 1.27 ± 0.20 μM (chen2017structuralbasisof pages 3-4, chen2017structuralbasisof pages 1-3).

#### Structural Basis of Regulation

High-resolution crystal structures of the FIN219–FIP1 complex have revealed the molecular mechanism of this regulatory interaction (chen2017structuralbasisof pages 3-4, chen2017structuralbasisof pages 1-1). FIP1 binds to FIN219's C-terminal domain through a helix–helix interface, with FIP1 helices α6–α8 contacting FIN219 helices α16–α17 (chen2017structuralbasisof pages 1-3). Key ionic contacts involve FIN219 residues R451 and K456 interacting with FIP1 residues E168 and D201, stabilized by additional hydrogen bonds (chen2017structuralbasisof pages 1-3, chen2017structuralbasisof pages 7-8).

The binding of FIP1 induces a major conformational rearrangement in FIN219. The C-terminal domain of FIN219 rotates and inserts into the N-terminal active-site groove, with helices α20 and α21 partially occluding the approximately 250 Å² substrate-entry opening (chen2017structuralbasisof pages 3-4, chen2017structuralbasisof pages 1-1). This conformational change repositions the ATP-binding region and remodels the architecture of the hormone/substrate-binding site (chen2017structuralbasisof pages 3-4, chen2017structuralbasisof pages 7-8).

#### Enhanced Catalytic Activity

The structural reorganization induced by FIP1 binding has profound functional consequences. FIP1 binding approximately doubles FIN219's adenylation activity, with measured increases of approximately twofold in maximum binding capacity (Bmax) and 2.3-fold in maximum velocity (Vmax) compared to FIN219 alone (chen2017structuralbasisof pages 4-6). The interaction also increases FIN219's affinity for jasmonic acid (JA), as reflected by lower dissociation constants (chen2017structuralbasisof pages 4-6). 

Mechanistically, FIP1 binding promotes an ordered substrate-binding mechanism in which JA must bind first, followed by ATP and isoleucine (chen2017structuralbasisof pages 4-6). The resulting conformational state positions substrates and catalytic residues more favorably for adenylation and subsequent thioesterification, ultimately increasing production of the bioactive hormone JA-Ile (chen2017structuralbasisof pages 6-7). Thus, while FIN219 is the enzyme that directly catalyzes JA-amino acid conjugation, GSTU20/FIP1 serves as an essential allosteric activator that enhances FIN219's biosynthetic capacity (chen2017structuralbasisof pages 1-1, chen2017structuralbasisof pages 3-4, chen2017structuralbasisof pages 7-8).

### Integration of Light Signaling and Hormone Biosynthesis

#### Phytochrome A-Dependent Regulation

GSTU20 expression is strongly regulated by light quality, particularly far-red light. Transcriptional induction of GSTU20 occurs under far-red irradiation, and this induction is abolished in *phytochrome A* (*phyA*) mutants, demonstrating that GSTU20 acts downstream of or in association with phytochrome A-mediated light signaling (sylvestregonon2019functionalstructuraland pages 13-14). This light-responsive regulation is relatively specific to GSTU20; transcriptome analyses indicate that GSTU20 shows comparatively weak transcriptional responses to the broad panel of abiotic stresses that typically induce other GSTU family members (sylvestregonon2019functionalstructuraland pages 13-14).

The FIN219–FIP1 interaction thus provides a molecular mechanism linking environmental light perception to jasmonate hormone biosynthesis. Under far-red light conditions, increased GSTU20/FIP1 expression leads to enhanced FIN219 activity and greater production of JA-Ile, thereby modulating jasmonate-dependent responses according to light conditions (chen2017structuralbasisof pages 7-8, chen2017structuralbasisof pages 1-3). This represents a direct connection between light signaling and defense metabolism, as both jasmonates and glucosinolates are important defensive compounds (lin2025theroleof pages 6-8, galle2019plantglutathionetransferases pages 5-7).

#### Photomorphogenic Phenotypes

Genetic studies using both gain-of-function and loss-of-function approaches have revealed GSTU20's role in developmental processes. Both GSTU20 overexpression lines and *gstu20* knockdown/knockout lines exhibit hyposensitivity to continuous far-red light and show delayed flowering under long-day photoperiod conditions (ugalde2025diversificationofglutathione pages 7-8). This indicates that proper GSTU20 dosage is required for normal photomorphogenic responses. Additionally, GSTU20 affects light-regulated cell elongation and flowering time, linking it to fundamental developmental processes (sylvestregonon2019functionalstructuraland pages 13-14, sylvestregonon2019functionalstructuraland pages 14-16).

Notably, despite the pronounced biochemical phenotypes in glucosinolate metabolism, *gstu20* mutants show no obvious morphological abnormalities under standard growth conditions (zhang2022arabidopsisglutathionestransferasesgstf11 pages 6-8). This separation of biochemical and morphological phenotypes suggests that GSTU20's metabolic functions are important for defense but not essential for basic vegetative growth and development under non-stress conditions.

### Subcellular Localization

GSTU20 is primarily localized to the cytoplasm/cytosol (zhang2022arabidopsisglutathionestransferasesgstf11 pages 3-6). This localization is consistent with both of its established functions: the cytosolic steps of glucosinolate biosynthesis and the interaction with FIN219 for jasmonate synthesis, which also occurs in the cytosol. The cytosolic localization distinguishes GSTU20 from organellar processes and positions it at a key metabolic hub where defense compound biosynthesis, hormone signaling, and light-responsive regulation converge.

### Expression Patterns and Tissue Distribution

GSTU20 exhibits tissue-specific expression patterns that provide insights into its physiological roles. Expression is highest in siliques (developing seeds) and relatively weak in leaves (zhang2022arabidopsisglutathionestransferasesgstf11 pages 3-6). Some expression analyses have also reported root-enriched expression for GSTU family members including GSTU20 (sylvestregonon2019functionalstructuraland pages 11-12). This expression pattern, with high levels in reproductive tissues, may reflect the importance of glucosinolate accumulation in seeds for protection of the next generation.

The tissue-specific expression pattern is complementary to that of GSTF11, which shows a different distribution (zhang2022arabidopsisglutathionestransferasesgstf11 pages 3-6). This spatial separation may contribute to the non-redundant functions of these two GSTs, with each playing more important roles in different tissues or developmental stages.

### Biological Processes and Signaling Pathways

| Function Category | Specific Role/Activity | Evidence Type | Key Findings with citations |
|---|---|---|---|
| Molecular identity | Tau-class glutathione S-transferase GSTU20; also called FIN219-interacting protein 1 (FIP1) | UniProt-aligned literature identity; crystallography | The protein is *Arabidopsis thaliana* GSTU20/FIP1 (At1g78370), a homodimeric tau-class GST with canonical N-terminal thioredoxin-like and C-terminal helical GST domains—not a similarly named protein from another organism. Multiple GSH-bound structures are available (PDB 5ECS, 5ECR, 5ECQ and related entries) (chen2017structuralbasisof pages 1-1, sylvestregonon2019functionalstructuraland pages 14-16, sylvestregonon2019functionalstructuraland pages 8-9) |
| Enzymatic activity | Glutathione-dependent transferase activity | Recombinant-enzyme assay; GSH-bound crystal structures | GSTU20 binds GSH through a conserved G-site involving residues including K40, E66 and S67 and has measurable transferase activity, although activity against the assay substrate was substantially weaker than that of the reference *Schistosoma japonicum* GST. Its native physiological substrate spectrum has not been comprehensively determined (chen2017structuralbasisof pages 3-4) |
| Specialized metabolism | Promotes aliphatic glucosinolate biosynthesis | CRISPR/Cas9 genetics; targeted metabolite profiling; transcriptomics | Two premature-stop *gstu20* alleles strongly reduced aliphatic glucosinolates in leaves and mature seeds without significantly changing indolic glucosinolates. The defect was generally stronger than in *gstf11*, and the double mutant showed an additive or synergistic reduction, establishing partly overlapping but non-redundant functions (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, zhang2022arabidopsisglutathionestransferasesgstf11 pages 1-2, zhang2022arabidopsisglutathionestransferasesgstf11 pages 6-8) |
| Proposed physiological reaction | GSH conjugation during glucosinolate core formation | Pathway placement; mutant metabolomics; contemporary pathway synthesis | GSTU20 is placed at the glutathione-conjugation stage of aliphatic glucosinolate core biosynthesis, upstream of GGP1-mediated processing. GSH-derived conjugates provide sulfur for formation of the S-alkylthiohydroximate intermediate; however, the exact GSTU20-selective electrophilic precursor and purified-enzyme kinetic constants have not been established directly (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, choi2024elongatedhypocotyl5 pages 1-2, zhang2022arabidopsisglutathionestransferasesgstf11 pages 10-11) |
| Functional specificity | Stronger contribution than GSTF11, but not the sole pathway GST | Single- and double-mutant comparison | *gstu20* mutants lose more aliphatic glucosinolates and show broader transcriptomic changes than *gstf11* mutants. Residual glucosinolate production in the double mutant implies participation by additional GST isoforms, so GSTU20 is important but neither sufficient nor absolutely required for pathway flux (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, zhang2022arabidopsisglutathionestransferasesgstf11 pages 2-3, zhang2022arabidopsisglutathionestransferasesgstf11 pages 10-11) |
| Protein interaction | Direct binding to FIN219/JAR1/AtGH3.11 | Yeast two-hybrid; pull-down; co-immunoprecipitation; quartz-crystal microbalance; X-ray crystallography | GSTU20/FIP1 binds the C-terminal region of FIN219 with a dissociation constant of 1.27 ± 0.20 micromolar. FIP1 helices α6–α8 contact FIN219 helices α16–α17; ionic and hydrogen-bond contacts include FIP1 E168 and D201 with FIN219 R451 and K456 (chen2017structuralbasisof pages 3-4, chen2017structuralbasisof pages 1-3, chen2017structuralbasisof pages 6-7) |
| Regulatory activity | Allosteric activation of FIN219 | Complex structures; ligand-binding and enzyme-kinetic measurements | FIP1 binding rotates and reorganizes FIN219's C-terminal domain, remodels the ATP/hormone-binding region and changes substrate-entry geometry. The complex approximately doubled adenylation activity and produced about twofold higher maximum binding capacity and 2.3-fold higher maximum velocity than FIN219 alone while increasing JA affinity (chen2017structuralbasisof pages 1-1, chen2017structuralbasisof pages 4-6) |
| Jasmonate pathway | Enhances FIN219-dependent JA–amino-acid conjugation, especially JA-Ile formation | Structural biochemistry; catalytic assays | FIN219—not GSTU20 itself—is the jasmonate-amido synthetase that uses JA, ATP and isoleucine to form bioactive JA-Ile. GSTU20 acts as its regulatory partner, favoring an enhanced-activity state and thereby connecting GSTU20 to downstream COI1–JAZ jasmonate signaling (chen2017structuralbasisof pages 1-1, chen2017structuralbasisof pages 6-7, chen2017structuralbasisof pages 3-4) |
| Light signaling | Component of phytochrome A-dependent far-red signaling | Expression analysis; gain- and loss-of-function genetics | Far-red irradiation induces GSTU20 expression, whereas the induction is impaired in a *phyA* mutant. GSTU20 therefore acts downstream of or in association with phyA and links far-red perception to FIN219-dependent jasmonate regulation (sylvestregonon2019functionalstructuraland pages 13-14) |
| Developmental phenotype | Modulates far-red sensitivity, cell elongation and flowering time | Overexpression and knockdown/knockout phenotyping | Both GSTU20 overexpression and reduced-expression lines were reported as hyposensitive to continuous far-red light and delayed in flowering under long days, indicating that correct GSTU20 dosage is required for normal signaling. Reviews also associate the locus with light-regulated seedling development and cell elongation (sylvestregonon2019functionalstructuraland pages 14-16, ugalde2025diversificationofglutathione pages 7-8, sylvestregonon2019functionalstructuraland pages 13-14) |
| Metabolic phenotype | Selective loss of aliphatic rather than indolic glucosinolates | UPLC metabolite profiling | Most measured aliphatic glucosinolate classes declined in *gstu20* leaves, with 5MSOP reported as an exception; aliphatic glucosinolates also fell in seeds. Indolic glucosinolate abundance did not change significantly, supporting pathway-class specificity (zhang2022arabidopsisglutathionestransferasesgstf11 pages 6-8) |
| General morphology | No conspicuous growth abnormality under standard conditions | Whole-plant phenotyping | Despite marked glucosinolate defects, *gstu20-1* and *gstu20-2* plants showed no obvious morphological abnormalities under the tested growth conditions. This separates the robust biochemical phenotype from broad developmental impairment (zhang2022arabidopsisglutathionestransferasesgstf11 pages 6-8, zhang2022arabidopsisglutathionestransferasesgstf11 pages 3-6) |
| Subcellular localization | Predominantly cytosolic | Subcellular-localization dataset summarized in the glucosinolate study | GSTU20 is reported primarily in the cytoplasm, consistent with cytosolic glucosinolate-conjugate processing and interaction with FIN219. The available evidence does not support secretion, membrane insertion or primary organellar residence (zhang2022arabidopsisglutathionestransferasesgstf11 pages 3-6) |
| Tissue expression | Tissue-dependent expression, including high silique expression | Public-expression datasets; study-specific expression analysis | The glucosinolate study reported high expression in siliques and weak expression in leaves; broader GST expression analyses suggested root enrichment. Because datasets and normalization schemes differ, precise tissue rankings should be treated cautiously rather than merged into a single definitive profile (zhang2022arabidopsisglutathionestransferasesgstf11 pages 3-6, sylvestregonon2019functionalstructuraland pages 11-12) |
| Stress-response context | More specialized than a generic stress-inducible GST | AtGenExpress meta-analysis; review synthesis | GSTU20 showed comparatively weak transcriptional changes across a broad abiotic-stress panel, while far-red/phyA regulation was clearer. General tau-GST functions in xenobiotic detoxification or peroxide reduction should therefore not be assigned specifically to GSTU20 without direct isoform-level evidence (sylvestregonon2019functionalstructuraland pages 13-14, sylvestregonon2019functionalstructuraland pages 9-11) |
| Integrated biological role | Connects sulfur-containing defense metabolism with light–hormone crosstalk | Convergent genetic, metabolomic, structural and biochemical evidence | The best-supported model assigns GSTU20 two experimentally grounded functions: a catalytic contribution to glutathione-dependent aliphatic glucosinolate biosynthesis and a noncanonical protein-regulatory role that activates FIN219-mediated JA-Ile synthesis during far-red signaling. Whether these functions are mechanistically coordinated in vivo remains unresolved (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, chen2017structuralbasisof pages 1-1, sylvestregonon2019functionalstructuraland pages 13-14) |


*Table: This table summarizes the experimentally supported enzymatic, regulatory, developmental and localization roles of Arabidopsis GSTU20/FIP1. It also distinguishes direct evidence from pathway assignments and unresolved substrate-specificity questions.*

GSTU20 participates in multiple interconnected biological processes:

1. **Defense Metabolism**: Through its role in aliphatic glucosinolate biosynthesis, GSTU20 contributes to the production of sulfur-containing defensive secondary metabolites that protect against herbivores and pathogens (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10, choi2024elongatedhypocotyl5 pages 1-2).

2. **Jasmonate Signaling**: Via its interaction with FIN219, GSTU20 enhances production of JA-Ile, the bioactive jasmonate that binds to the COI1 receptor and triggers degradation of JAZ repressor proteins, thereby activating jasmonate-responsive gene expression (chen2017structuralbasisof pages 1-1, chen2017structuralbasisof pages 3-4).

3. **Light Signal Transduction**: As a phytochrome A-responsive gene, GSTU20 participates in far-red light signaling pathways that regulate photomorphogenesis (sylvestregonon2019functionalstructuraland pages 13-14, galle2019plantglutathionetransferases pages 5-7, lin2025theroleof pages 6-8).

4. **Developmental Regulation**: GSTU20 affects cell elongation and flowering time, integrating light and hormone signals to coordinate developmental transitions (ugalde2025diversificationofglutathione pages 7-8, sylvestregonon2019functionalstructuraland pages 13-14).

The integration of these processes represents a sophisticated regulatory network in which environmental light cues influence both hormone biosynthesis and defense compound production. Whether GSTU20's dual enzymatic and regulatory functions are mechanistically coordinated in vivo remains an open question for future research (sylvestregonon2019functionalstructuraland pages 13-14).

### Current Research Context (2023-2025)

Recent studies continue to reveal the importance of GSTU20 in plant metabolism. The 2024 study by Choi et al. placed GSTU20 within the broader regulatory network controlling glucosinolate biosynthesis, showing how light signaling factors such as HY5 interact with histone deacetylases to regulate glucosinolate genes including GSTU20 (choi2024elongatedhypocotyl5 pages 1-2). The 2025 review by Ugalde et al. highlighted GSTU20 as an example of functional diversification within the plant GST family, emphasizing its dual catalytic and regulatory roles (ugalde2025diversificationofglutathione pages 2-4, ugalde2025diversificationofglutathione pages 7-8). Lin et al. (2025) discussed GSTU20/FIP1 in the context of GST-mediated integration of light signaling with plant growth regulation (lin2025theroleof pages 6-8).

### Summary

GSTU20 (FIP1) exemplifies functional diversification within the plant glutathione S-transferase superfamily. Rather than serving solely as a detoxification enzyme, GSTU20 has evolved two specialized roles: (1) a catalytic function in aliphatic glucosinolate biosynthesis, where it facilitates glutathione conjugation during core structure formation, and (2) a regulatory function as an allosteric activator of the jasmonate-amido synthetase FIN219, enhancing production of bioactive JA-Ile. Both functions are integrated with light signaling through phytochrome A-mediated transcriptional regulation. This dual functionality positions GSTU20 as a molecular integrator connecting environmental light perception, hormone biosynthesis, and defensive secondary metabolism. The protein functions in the cytosol, shows tissue-specific expression with enrichment in reproductive tissues, and contributes to photomorphogenic development including regulation of flowering time and cell elongation. Loss of GSTU20 causes selective reductions in aliphatic glucosinolates without affecting plant morphology under standard conditions, indicating specialized rather than essential housekeeping functions.

References

1. (chen2017structuralbasisof pages 1-1): Chun-Yen Chen, Sih-Syun Ho, Tzu-Yen Kuo, Hsu-Liang Hsieh, and Yi-Sheng Cheng. Structural basis of jasmonate-amido synthetase fin219 in complex with glutathione s-transferase fip1 during the ja signal regulation. Proceedings of the National Academy of Sciences, 114:E1815-E1824, Feb 2017. URL: https://doi.org/10.1073/pnas.1609980114, doi:10.1073/pnas.1609980114. This article has 37 citations and is from a highest quality peer-reviewed journal.

2. (sylvestregonon2019functionalstructuraland pages 14-16): Elodie Sylvestre-Gonon, Simon R. Law, Mathieu Schwartz, Kevin Robe, Olivier Keech, Claude Didierjean, Christian Dubos, Nicolas Rouhier, and Arnaud Hecker. Functional, structural and biochemical features of plant serinyl-glutathione transferases. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00608, doi:10.3389/fpls.2019.00608. This article has 126 citations.

3. (chen2017structuralbasisof pages 3-4): Chun-Yen Chen, Sih-Syun Ho, Tzu-Yen Kuo, Hsu-Liang Hsieh, and Yi-Sheng Cheng. Structural basis of jasmonate-amido synthetase fin219 in complex with glutathione s-transferase fip1 during the ja signal regulation. Proceedings of the National Academy of Sciences, 114:E1815-E1824, Feb 2017. URL: https://doi.org/10.1073/pnas.1609980114, doi:10.1073/pnas.1609980114. This article has 37 citations and is from a highest quality peer-reviewed journal.

4. (sylvestregonon2019functionalstructuraland pages 8-9): Elodie Sylvestre-Gonon, Simon R. Law, Mathieu Schwartz, Kevin Robe, Olivier Keech, Claude Didierjean, Christian Dubos, Nicolas Rouhier, and Arnaud Hecker. Functional, structural and biochemical features of plant serinyl-glutathione transferases. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00608, doi:10.3389/fpls.2019.00608. This article has 126 citations.

5. (zhang2022arabidopsisglutathionestransferasesgstf11 pages 8-10): Aiqin Zhang, Rui Luo, Jiawen Li, Rongqing Miao, Hui An, Xiufeng Yan, and Qiuying Pang. Arabidopsis glutathione-s-transferases gstf11 and gstu20 function in aliphatic glucosinolate biosynthesis. Frontiers in Plant Science, Jan 2022. URL: https://doi.org/10.3389/fpls.2021.816233, doi:10.3389/fpls.2021.816233. This article has 29 citations.

6. (choi2024elongatedhypocotyl5 pages 1-2): Dasom Choi, Seong-Hyeon Kim, Da-Min Choi, Heewon Moon, Jeong-Il Kim, Enamul Huq, and Dong-Hwan Kim. Elongated hypocotyl 5 interacts with histone deacetylase 9 to suppress glucosinolate biosynthesis in arabidopsis. Plant physiology, 196:1340-1355, May 2024. URL: https://doi.org/10.1093/plphys/kiae284, doi:10.1093/plphys/kiae284. This article has 22 citations and is from a highest quality peer-reviewed journal.

7. (zhang2022arabidopsisglutathionestransferasesgstf11 pages 6-8): Aiqin Zhang, Rui Luo, Jiawen Li, Rongqing Miao, Hui An, Xiufeng Yan, and Qiuying Pang. Arabidopsis glutathione-s-transferases gstf11 and gstu20 function in aliphatic glucosinolate biosynthesis. Frontiers in Plant Science, Jan 2022. URL: https://doi.org/10.3389/fpls.2021.816233, doi:10.3389/fpls.2021.816233. This article has 29 citations.

8. (chen2017structuralbasisof pages 4-6): Chun-Yen Chen, Sih-Syun Ho, Tzu-Yen Kuo, Hsu-Liang Hsieh, and Yi-Sheng Cheng. Structural basis of jasmonate-amido synthetase fin219 in complex with glutathione s-transferase fip1 during the ja signal regulation. Proceedings of the National Academy of Sciences, 114:E1815-E1824, Feb 2017. URL: https://doi.org/10.1073/pnas.1609980114, doi:10.1073/pnas.1609980114. This article has 37 citations and is from a highest quality peer-reviewed journal.

9. (sylvestregonon2019functionalstructuraland pages 13-14): Elodie Sylvestre-Gonon, Simon R. Law, Mathieu Schwartz, Kevin Robe, Olivier Keech, Claude Didierjean, Christian Dubos, Nicolas Rouhier, and Arnaud Hecker. Functional, structural and biochemical features of plant serinyl-glutathione transferases. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00608, doi:10.3389/fpls.2019.00608. This article has 126 citations.

10. (zhang2022arabidopsisglutathionestransferasesgstf11 pages 1-2): Aiqin Zhang, Rui Luo, Jiawen Li, Rongqing Miao, Hui An, Xiufeng Yan, and Qiuying Pang. Arabidopsis glutathione-s-transferases gstf11 and gstu20 function in aliphatic glucosinolate biosynthesis. Frontiers in Plant Science, Jan 2022. URL: https://doi.org/10.3389/fpls.2021.816233, doi:10.3389/fpls.2021.816233. This article has 29 citations.

11. (zhang2022arabidopsisglutathionestransferasesgstf11 pages 2-3): Aiqin Zhang, Rui Luo, Jiawen Li, Rongqing Miao, Hui An, Xiufeng Yan, and Qiuying Pang. Arabidopsis glutathione-s-transferases gstf11 and gstu20 function in aliphatic glucosinolate biosynthesis. Frontiers in Plant Science, Jan 2022. URL: https://doi.org/10.3389/fpls.2021.816233, doi:10.3389/fpls.2021.816233. This article has 29 citations.

12. (zhang2022arabidopsisglutathionestransferasesgstf11 pages 10-11): Aiqin Zhang, Rui Luo, Jiawen Li, Rongqing Miao, Hui An, Xiufeng Yan, and Qiuying Pang. Arabidopsis glutathione-s-transferases gstf11 and gstu20 function in aliphatic glucosinolate biosynthesis. Frontiers in Plant Science, Jan 2022. URL: https://doi.org/10.3389/fpls.2021.816233, doi:10.3389/fpls.2021.816233. This article has 29 citations.

13. (chen2017structuralbasisof pages 1-3): Chun-Yen Chen, Sih-Syun Ho, Tzu-Yen Kuo, Hsu-Liang Hsieh, and Yi-Sheng Cheng. Structural basis of jasmonate-amido synthetase fin219 in complex with glutathione s-transferase fip1 during the ja signal regulation. Proceedings of the National Academy of Sciences, 114:E1815-E1824, Feb 2017. URL: https://doi.org/10.1073/pnas.1609980114, doi:10.1073/pnas.1609980114. This article has 37 citations and is from a highest quality peer-reviewed journal.

14. (chen2017structuralbasisof pages 7-8): Chun-Yen Chen, Sih-Syun Ho, Tzu-Yen Kuo, Hsu-Liang Hsieh, and Yi-Sheng Cheng. Structural basis of jasmonate-amido synthetase fin219 in complex with glutathione s-transferase fip1 during the ja signal regulation. Proceedings of the National Academy of Sciences, 114:E1815-E1824, Feb 2017. URL: https://doi.org/10.1073/pnas.1609980114, doi:10.1073/pnas.1609980114. This article has 37 citations and is from a highest quality peer-reviewed journal.

15. (chen2017structuralbasisof pages 6-7): Chun-Yen Chen, Sih-Syun Ho, Tzu-Yen Kuo, Hsu-Liang Hsieh, and Yi-Sheng Cheng. Structural basis of jasmonate-amido synthetase fin219 in complex with glutathione s-transferase fip1 during the ja signal regulation. Proceedings of the National Academy of Sciences, 114:E1815-E1824, Feb 2017. URL: https://doi.org/10.1073/pnas.1609980114, doi:10.1073/pnas.1609980114. This article has 37 citations and is from a highest quality peer-reviewed journal.

16. (lin2025theroleof pages 6-8): Chen Lin, Zidan Zhang, Zhao Zhang, Yuxiang Long, Xuwen Shen, Jinghao Zhang, and Youping Wang. The role of glutathione s-transferase in the regulation of plant growth, and responses to environmental stresses. Phyton, 94:583-601, Jan 2025. URL: https://doi.org/10.32604/phyton.2025.063086, doi:10.32604/phyton.2025.063086. This article has 24 citations.

17. (galle2019plantglutathionetransferases pages 5-7): Ágnes Gallé, Zalán Czékus, Krisztina Bela, Edit Horváth, Attila Ördög, Jolán Csiszár, and Péter Poór. Plant glutathione transferases and light. Frontiers in Plant Science, Jan 2019. URL: https://doi.org/10.3389/fpls.2018.01944, doi:10.3389/fpls.2018.01944. This article has 97 citations.

18. (ugalde2025diversificationofglutathione pages 7-8): José M. Ugalde, Manjeera Nath, Stephan Wagner, and Andreas J. Meyer. Diversification of glutathione transferases in plants and their role in oxidative stress defense. Biological chemistry, Jul 2025. URL: https://doi.org/10.1515/hsz-2025-0111, doi:10.1515/hsz-2025-0111. This article has 22 citations and is from a peer-reviewed journal.

19. (zhang2022arabidopsisglutathionestransferasesgstf11 pages 3-6): Aiqin Zhang, Rui Luo, Jiawen Li, Rongqing Miao, Hui An, Xiufeng Yan, and Qiuying Pang. Arabidopsis glutathione-s-transferases gstf11 and gstu20 function in aliphatic glucosinolate biosynthesis. Frontiers in Plant Science, Jan 2022. URL: https://doi.org/10.3389/fpls.2021.816233, doi:10.3389/fpls.2021.816233. This article has 29 citations.

20. (sylvestregonon2019functionalstructuraland pages 11-12): Elodie Sylvestre-Gonon, Simon R. Law, Mathieu Schwartz, Kevin Robe, Olivier Keech, Claude Didierjean, Christian Dubos, Nicolas Rouhier, and Arnaud Hecker. Functional, structural and biochemical features of plant serinyl-glutathione transferases. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00608, doi:10.3389/fpls.2019.00608. This article has 126 citations.

21. (sylvestregonon2019functionalstructuraland pages 9-11): Elodie Sylvestre-Gonon, Simon R. Law, Mathieu Schwartz, Kevin Robe, Olivier Keech, Claude Didierjean, Christian Dubos, Nicolas Rouhier, and Arnaud Hecker. Functional, structural and biochemical features of plant serinyl-glutathione transferases. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00608, doi:10.3389/fpls.2019.00608. This article has 126 citations.

22. (ugalde2025diversificationofglutathione pages 2-4): José M. Ugalde, Manjeera Nath, Stephan Wagner, and Andreas J. Meyer. Diversification of glutathione transferases in plants and their role in oxidative stress defense. Biological chemistry, Jul 2025. URL: https://doi.org/10.1515/hsz-2025-0111, doi:10.1515/hsz-2025-0111. This article has 22 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](GSTU20-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](GSTU20-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. chen2017structuralbasisof pages 3-4
2. sylvestregonon2019functionalstructuraland pages 8-9
3. sylvestregonon2019functionalstructuraland pages 13-14
4. chen2017structuralbasisof pages 1-3
5. chen2017structuralbasisof pages 4-6
6. chen2017structuralbasisof pages 6-7
7. ugalde2025diversificationofglutathione pages 7-8
8. sylvestregonon2019functionalstructuraland pages 11-12
9. lin2025theroleof pages 6-8
10. chen2017structuralbasisof pages 1-1
11. sylvestregonon2019functionalstructuraland pages 14-16
12. chen2017structuralbasisof pages 7-8
13. galle2019plantglutathionetransferases pages 5-7
14. sylvestregonon2019functionalstructuraland pages 9-11
15. ugalde2025diversificationofglutathione pages 2-4
16. https://doi.org/10.1073/pnas.1609980114,
17. https://doi.org/10.3389/fpls.2019.00608,
18. https://doi.org/10.3389/fpls.2021.816233,
19. https://doi.org/10.1093/plphys/kiae284,
20. https://doi.org/10.32604/phyton.2025.063086,
21. https://doi.org/10.3389/fpls.2018.01944,
22. https://doi.org/10.1515/hsz-2025-0111,