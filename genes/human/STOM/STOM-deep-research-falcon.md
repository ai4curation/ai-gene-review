---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-14T17:12:42.068481'
end_time: '2025-12-14T17:20:21.226990'
duration_seconds: 459.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: STOM
  gene_symbol: STOM
  uniprot_accession: P27105
  protein_description: 'RecName: Full=Stomatin {ECO:0000312|HGNC:HGNC:3383}; AltName:
    Full=Erythrocyte band 7 integral membrane protein {ECO:0000303|PubMed:1883838};
    AltName: Full=Erythrocyte membrane protein band 7.2 {ECO:0000312|HGNC:HGNC:3383};
    AltName: Full=Protein 7.2b {ECO:0000303|PubMed:8825639};'
  gene_info: Name=STOM {ECO:0000312|HGNC:HGNC:3383}; Synonyms=BND7 {ECO:0000312|HGNC:HGNC:3383},
    EPB72 {ECO:0000303|PubMed:8825639};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the band 7/mec-2 family. .
  protein_domains: Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf.
    (IPR036013); Band_7/stomatin-like_CS. (IPR018080); Stomatin_HflK_fam. (IPR001972)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P27105
- **Protein Description:** RecName: Full=Stomatin {ECO:0000312|HGNC:HGNC:3383}; AltName: Full=Erythrocyte band 7 integral membrane protein {ECO:0000303|PubMed:1883838}; AltName: Full=Erythrocyte membrane protein band 7.2 {ECO:0000312|HGNC:HGNC:3383}; AltName: Full=Protein 7.2b {ECO:0000303|PubMed:8825639};
- **Gene Information:** Name=STOM {ECO:0000312|HGNC:HGNC:3383}; Synonyms=BND7 {ECO:0000312|HGNC:HGNC:3383}, EPB72 {ECO:0000303|PubMed:8825639};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the band 7/mec-2 family. .
- **Key Domains:** Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf. (IPR036013); Band_7/stomatin-like_CS. (IPR018080); Stomatin_HflK_fam. (IPR001972)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STOM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STOM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STOM** (gene ID: STOM, UniProt: P27105) in human.

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
- **UniProt Accession:** P27105
- **Protein Description:** RecName: Full=Stomatin {ECO:0000312|HGNC:HGNC:3383}; AltName: Full=Erythrocyte band 7 integral membrane protein {ECO:0000303|PubMed:1883838}; AltName: Full=Erythrocyte membrane protein band 7.2 {ECO:0000312|HGNC:HGNC:3383}; AltName: Full=Protein 7.2b {ECO:0000303|PubMed:8825639};
- **Gene Information:** Name=STOM {ECO:0000312|HGNC:HGNC:3383}; Synonyms=BND7 {ECO:0000312|HGNC:HGNC:3383}, EPB72 {ECO:0000303|PubMed:8825639};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the band 7/mec-2 family. .
- **Key Domains:** Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf. (IPR036013); Band_7/stomatin-like_CS. (IPR018080); Stomatin_HflK_fam. (IPR001972)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STOM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STOM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STOM** (gene ID: STOM, UniProt: P27105) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

Plan and verification
- Target identity: STOM encodes human stomatin (UniProt P27105), historically identified as erythrocyte “band 7/band 7.2” integral membrane protein. It belongs to the SPFH (stomatin–prohibitin–flotillin–HflK/C) superfamily and contains the Band-7/stomatin-like domain, consistent with the UniProt domains provided. Human organism context applies throughout. Supporting literature below uses human erythrocytes or cross-species SPFH principles with explicit human relevance (e.g., RBC studies, human GLUT1 links) (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, murphy2004erythrocytedetergentresistantmembrane pages 1-2, lu2024molecularmechanismof pages 1-3).

Comprehensive research report on human STOM (stomatin; UniProt P27105)

1) Key concepts and definitions
- Molecular identity and family: Stomatin is an integral membrane-associated scaffolding protein of the SPFH superfamily (stomatin, prohibitin, flotillin, HflK/C) that organizes cholesterol-rich, detergent-resistant plasma-membrane microdomains (“rafts”) and regulates associated transporters and channels. In erythrocytes it corresponds to band 7/band 7.2 protein (historical nomenclature) (https://doi.org/10.1182/blood-2010-12-326645; https://doi.org/10.1182/blood-2003-09-3165; https://doi.org/10.1101/2024.05.25.595881) (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, murphy2004erythrocytedetergentresistantmembrane pages 1-2, lu2024molecularmechanismof pages 1-3).
- Canonical functions: (i) membrane microdomain scaffolding; (ii) modulation of transporters and ion channels (notably GLUT1 in erythrocytes; ASIC/ENaC/DEG family and pannexin-1 in neurons/other cells are modulated by stomatin-domain proteins); (iii) potential roles in mechanosensation via SPFH family mechanisms (https://doi.org/10.1182/blood-2010-12-326645; https://doi.org/10.1152/ajprenal.00546.2019) (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, carattino2020acidsensingionchannels pages 1-6).
- Subcellular localization: Stomatin is enriched in detergent-resistant membrane (DRM) fractions of human erythrocyte membranes (rafts) and is part of the plasma membrane macrocomplex landscape (https://doi.org/10.1182/blood-2003-09-3165) (murphy2004erythrocytedetergentresistantmembrane pages 1-2).

2) Current understanding of molecular mechanisms and complexes
- Membrane microdomains and SPFH architecture: SPFH proteins share a conserved SPFH domain followed by a long coiled-coil that mediates oligomerization and membrane association (often via palmitoylation/myristoylation and cholesterol interaction motifs). Recent structural work on human flotillin (another SPFH member) shows alternating FLOT1/FLOT2 hetero-oligomers assembling into a dome-shaped 44-mer that encage ~30 nm patches of the cytoplasmic leaflet, offering a mechanistic paradigm for SPFH scaffolds that likely generalizes to stomatin’s microdomain organization (https://doi.org/10.1101/2024.05.25.595881; bioRxiv, 2024) (lu2024molecularmechanismof pages 1-3).
- Stomatin oligomerization and domain organization (emerging): Cryo-EM of human stomatin suggests 16-mer bowl-shaped oligomers that cluster on membranes and increase lipid order, consistent with a direct role in organizing functional microdomains (bioRxiv 2025; https://doi.org/10.1101/2025.08.30.673307). Super-resolution imaging reports stomatin clusters ~50–150 nm in diameter in cells; polymerization-deficient mutants fail to enhance lipid order, supporting a polymerization-dependent scaffolding mechanism (yan2025structuralroleof pages 1-5, yan2025structuralroleof pages 28-33, yan2025structuralroleof pages 5-9, yan2025structuralroleof pages 9-13, yan2025structuralroleof pages 33-40, yan2025structuralroleof pages 22-26). Although 2025 and preprint, these data are congruent with SPFH microdomain models anchored by 2024 flotillin cryo-EM (lu2024molecularmechanismof pages 1-3).
- RBC raft biology and selective cargo: In human erythrocytes, stomatin is a major DRM component alongside band 3 (SLC4A1) and flotillins. During P. falciparum infection, some DRM proteins (flotillins) are recruited to the parasitophorous vacuole, while others (band 3, stomatin) are excluded, indicating selective raft protein uptake and highlighting stomatin’s membrane microdomain context (https://doi.org/10.1182/blood-2003-09-3165) (murphy2004erythrocytedetergentresistantmembrane pages 1-2).

3) Transporters/channels regulated by stomatin and pathway placement
- GLUT1 (SLC2A1) in erythrocytes: Stomatin associates with erythrocyte GLUT1; this association has been reported to switch GLUT1′s preference toward L-dehydroascorbic acid (DHA) transport during terminal erythroid maturation, a primate strategy to import vitamin C equivalents. In stomatin-deficient cryohydrocytosis (sdCHC), pathogenic SLC2A1 variants produce RBCs that lack stomatin and exhibit both impaired glucose transport and a cation leak when mutant GLUT1 is expressed in oocytes, defining a GLUT1-linked hereditary stomatocytosis variant (Blood, 2011; https://doi.org/10.1182/blood-2010-12-326645). These data establish a functional STOM–GLUT1 axis with physiological consequences in RBCs (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, flatt2011stomatindeficientcryohydrocytosisresults pages 12-12).
- ASICs/ENaC/DEG family: In mammals, stomatin-domain proteins are part of the protein networks that modulate acid-sensing ion channels (ASICs), which are involved in mechanotransduction, nociception, and chemoreception. Reviews emphasize their association within membrane microdomains and tethering networks, placing stomatin proteins as modulators of ASIC gating/trafficking in sensory neurons (Am J Physiol-Renal Physiol 2020; https://doi.org/10.1152/ajprenal.00546.2019) (carattino2020acidsensingionchannels pages 1-6).

4) Subcellular localization and tissue distribution
- Erythrocytes: Stomatin is abundant in human erythrocyte membranes, enriched in DRM (raft) fractions, and often studied as part of the RBC membrane macrocomplex milieu (https://doi.org/10.1182/blood-2003-09-3165) (murphy2004erythrocytedetergentresistantmembrane pages 1-2).
- Developmental dynamics: During reticulocyte maturation, stomatin is reduced through endocytic/exosomal pathways; its levels define erythroid maturation states in some studies (Blood 2011; contextual citations within) (flatt2011stomatindeficientcryohydrocytosisresults pages 12-12).
- Other tissues/cells: While detailed human tissue distribution was not directly quantified in the retrieved 2023–2024 sources, SPFH roles are broadly conserved across cell types; flotillin structural data (2024) and stomatin oligomerization (2025 preprint) indicate generalizable membrane-scaffold functions beyond erythrocytes (https://doi.org/10.1101/2024.05.25.595881; https://doi.org/10.1101/2025.08.30.673307) (lu2024molecularmechanismof pages 1-3, yan2025structuralroleof pages 1-5).

5) Disease associations and clinical relevance
- Stomatin-deficient cryohydrocytosis (sdCHC; hereditary stomatocytosis variant): Patients harbor SLC2A1 mutations; RBCs lack stomatin and display cold-induced cation leak, hemolytic anemia, hepatosplenomegaly, and neurological manifestations typical of GLUT1 deficiency. Heterologous expression of mutant GLUT1 recapitulates cation leak and transport defects. sdCHC establishes a clinico-genetic link between GLUT1 and stomatin deficiency at the RBC membrane (Blood, 2011; https://doi.org/10.1182/blood-2010-12-326645) (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, flatt2011stomatindeficientcryohydrocytosisresults pages 12-12).
- Broader hydration disorders: Reviews of erythrocyte hydration disorders highlight GLUT1, SLC4A1, RHAG, PIEZO1, KCNN4 as key contributors and contextualize stomatin within the RBC membrane network; OHSt/RHAG variants produce monovalent cation leaks, with stomatin loss noted in some phenotypes, reinforcing its diagnostic/molecular milieu (Blood, 2017; https://doi.org/10.1182/blood-2017-04-590810) (gallagher2017disordersoferythrocyte pages 1-5).

6) Recent developments (emphasis 2023–2024) and expert perspectives
- RBC GLUT1 knockout study (2024): CRISPR-engineered human erythroblasts and primary CD34+ progenitors generated reticulocytes lacking GLUT1. Despite GLUT1’s abundance (~200,000 copies/cell; ~10% of RBC membrane protein mass), complete absence did not impede erythroblast proliferation, differentiation, enucleation, or reticulocyte membrane composition/deformability, though metabolic adaptations, increased osmotic fragility, and oxidative stress hallmarks were noted. This study recapitulates that reduced GLUT1 expression alone does not cause anemia in GLUT1 deficiency, and it explicitly situates GLUT1 within a membrane complex with stomatin/adducin/dematin in human RBCs (bioRxiv, 2024; https://doi.org/10.1101/2024.01.10.574621). These data refine expectations of the stomatin–GLUT1 axis by separating erythropoiesis and mechanics from metabolism and antioxidant capacity in the absence of GLUT1 (freire2024completeabsenceof pages 1-3, freire2024completeabsenceof pages 3-5).
- SPFH structural paradigm (2024): Cryo-EM of human flotillin complexes (3.57 Å) demonstrates large dome/ring oligomers that segregate ~30 nm membrane microdomains, supporting a general SPFH-based mechanism for microdomain formation and protein sequestration relevant to stomatin (bioRxiv, 2024; https://doi.org/10.1101/2024.05.25.595881) (lu2024molecularmechanismof pages 1-3).
- Emerging stomatin structural insights (2025 preprint): Cryo-EM and cell imaging suggest human stomatin forms 16-mer bowls, organizes 50–150 nm microdomains, and increases lipid order, offering a plausible structural basis for stomatin’s raft scaffolding and cargo regulation (https://doi.org/10.1101/2025.08.30.673307). While outside the 2023–2024 window and preprint, the findings align with the 2024 flotillin structures and with historical RBC raft evidence (yan2025structuralroleof pages 1-5, yan2025structuralroleof pages 28-33, yan2025structuralroleof pages 5-9, yan2025structuralroleof pages 9-13, yan2025structuralroleof pages 33-40).
- ASICs and stomatin-domain proteins (2020 review, with 2023–2024 ASIC literature context): Reviews underscore stomatin-domain proteins as part of ASIC regulatory networks in sensory neurons and other tissues, integrating mechanotransduction and chemosensation in lipid-raft contexts (Am J Physiol-Renal Physiol, 2020; https://doi.org/10.1152/ajprenal.00546.2019) (carattino2020acidsensingionchannels pages 1-6).

7) Current applications and real-world implementations
- Hematology diagnostics and mechanistic models: Stomatin serves as a biochemical marker in RBC DRM fractions and is informative in classifying hereditary stomatocytosis subtypes with membrane-protein macrocomplex defects (Blood, 2011; Blood, 2017). Selective recruitment/exclusion of raft proteins (e.g., stomatin excluded) during malaria infection of RBCs provides an experimental model to probe host–pathogen interactions and raft function (Blood, 2004; https://doi.org/10.1182/blood-2003-09-3165) (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, gallagher2017disordersoferythrocyte pages 1-5, murphy2004erythrocytedetergentresistantmembrane pages 1-2).
- Membrane microdomain scaffolds as targets: Structural definition of SPFH complexes (flotillin, 2024) supports rational exploration of microdomain-modulating strategies (e.g., cholesterol/raft perturbation) in trafficking and signaling, with translational implications across cell types (https://doi.org/10.1101/2024.05.25.595881) (lu2024molecularmechanismof pages 1-3).

8) Relevant statistics and quantitative data
- Abundance of GLUT1 in human RBCs: ~200,000 copies per cell, accounting for ~10% of total RBC membrane protein mass; stomatin is part of the same RBC membrane macro-environment (bioRxiv, 2024; https://doi.org/10.1101/2024.01.10.574621) (freire2024completeabsenceof pages 1-3).
- DRM composition in RBCs: Band 3 and stomatin reflect bulk DRM mass; flotillin-1/-2 and peroxiredoxin-2 are additional DRM constituents (Blood, 2004; https://doi.org/10.1182/blood-2003-09-3165) (murphy2004erythrocytedetergentresistantmembrane pages 1-2).
- SPFH microdomain dimensions: Flotillin complex encloses ~30 nm circular membrane patches (bioRxiv, 2024; https://doi.org/10.1101/2024.05.25.595881). Stomatin clusters reported at ~50–150 nm (preprint, 2025; https://doi.org/10.1101/2025.08.30.673307) (lu2024molecularmechanismof pages 1-3, yan2025structuralroleof pages 33-40).

9) Expert analysis and synthesis
- Primary role: Stomatin is best defined as a membrane microdomain scaffold/regulator rather than an enzyme or classical transporter. Its most strongly supported, specific interaction in human biology is with GLUT1 in erythrocytes, where it contributes to substrate preference switching toward DHA during maturation and participates in macrocomplex organization affecting ion homeostasis. The sdCHC entity links stomatin absence and GLUT1 dysfunction with cation leaks and hemolysis, underscoring functional coupling between raft scaffolds and solute transport (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, flatt2011stomatindeficientcryohydrocytosisresults pages 12-12).
- Broader signaling roles: Through SPFH-mediated oligomerization and raft organization, stomatin can influence the biophysical environment of ion channels and transporters (ASICs, pannexin-1, AE1 macrocomplex neighbors), providing a mechanistic basis for pleiotropic influences on mechanosensation and chemosensation described for stomatin-domain proteins (carattino2020acidsensingionchannels pages 1-6, murphy2004erythrocytedetergentresistantmembrane pages 1-2).
- 2023–2024 priorities: The 2024 human RBC GLUT1 knockout work refines the clinical interpretation of GLUT1 deficiency vis-à-vis RBCs and highlights that absence of GLUT1 (and thus loss of any stomatin–GLUT1 interaction) can be tolerated in erythroid differentiation, while altering metabolic resilience. Parallel SPFH structural advances (flotillin) provide a generalizable template for stomatin’s microdomain architecture, now complemented by emerging stomatin cryo-EM in 2025 preprints (freire2024completeabsenceof pages 1-3, lu2024molecularmechanismof pages 1-3, yan2025structuralroleof pages 1-5).

10) Gaps and future directions (brief)
- High-resolution human stomatin structures in peer-reviewed journals and in the 2023–2024 window remain a gap; preprint data are promising but require validation. Quantitative, in vivo human evidence for stomatin’s modulation of specific channels (e.g., ASICs) and transporters beyond GLUT1 in defined tissues remains to be elaborated.

References (URLs and years)
- Flatt et al., Blood, 2011. “Stomatin-deficient cryohydrocytosis results from mutations in SLC2A1.” https://doi.org/10.1182/blood-2010-12-326645 (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, flatt2011stomatindeficientcryohydrocytosisresults pages 12-12).
- Murphy et al., Blood, 2004. “Erythrocyte detergent-resistant membrane proteins…” https://doi.org/10.1182/blood-2003-09-3165 (murphy2004erythrocytedetergentresistantmembrane pages 1-2).
- Carattino & Montalbetti, Am J Physiol-Renal Physiol, 2020. “Acid-sensing ion channels in sensory signaling.” https://doi.org/10.1152/ajprenal.00546.2019 (carattino2020acidsensingionchannels pages 1-6).
- Gallagher, Blood, 2017. “Disorders of erythrocyte hydration.” https://doi.org/10.1182/blood-2017-04-590810 (gallagher2017disordersoferythrocyte pages 1-5).
- Freire et al., bioRxiv, 2024. “Complete absence of GLUT1 does not impair human terminal erythroid differentiation.” https://doi.org/10.1101/2024.01.10.574621 (freire2024completeabsenceof pages 1-3, freire2024completeabsenceof pages 3-5).
- Lu et al., bioRxiv, 2024. “Molecular mechanism of the flotillin complex in membrane microdomain organization.” https://doi.org/10.1101/2024.05.25.595881 (lu2024molecularmechanismof pages 1-3).
- Yan et al., bioRxiv, 2025. “Structural role of stomatin in organizing functional membrane microdomains.” https://doi.org/10.1101/2025.08.30.673307 (yan2025structuralroleof pages 1-5, yan2025structuralroleof pages 28-33, yan2025structuralroleof pages 5-9, yan2025structuralroleof pages 9-13, yan2025structuralroleof pages 33-40, yan2025structuralroleof pages 22-26).

Conclusion
Human stomatin (STOM) is a membrane microdomain scaffold of the SPFH family, abundant in erythrocyte rafts and mechanistically positioned to regulate transporter and ion channel function through oligomeric organization of lipid-ordered domains. The stomatin–GLUT1 interaction in RBCs is the clearest, historically supported example, relevant to substrate preference (DHA transport) and to pathophysiology in sdCHC. Recent 2024 studies advance our understanding of RBC membrane biology (GLUT1 deletion tolerance) and SPFH architecture (flotillin cryo-EM), while 2025 preprints supply direct structural hypotheses for human stomatin assemblies that align with the broader SPFH paradigm (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3, murphy2004erythrocytedetergentresistantmembrane pages 1-2, freire2024completeabsenceof pages 1-3, lu2024molecularmechanismof pages 1-3, yan2025structuralroleof pages 1-5).

References

1. (flatt2011stomatindeficientcryohydrocytosisresults pages 1-3): Joanna F. Flatt, Hélène Guizouarn, Nicholas M. Burton, Franck Borgese, Richard J. Tomlinson, Robert J. Forsyth, Stephen A. Baldwin, Bari E. Levinson, Philippe Quittet, Patricia Aguilar-Martinez, Jean Delaunay, Gordon W. Stewart, and Lesley J. Bruce. Stomatin-deficient cryohydrocytosis results from mutations in slc2a1: a novel form of glut1 deficiency syndrome. Blood, 118 19:5267-77, Nov 2011. URL: https://doi.org/10.1182/blood-2010-12-326645, doi:10.1182/blood-2010-12-326645. This article has 103 citations and is from a highest quality peer-reviewed journal.

2. (murphy2004erythrocytedetergentresistantmembrane pages 1-2): Sean C. Murphy, Benjamin U. Samuel, Travis Harrison, Kaye D. Speicher, David W. Speicher, Marion E. Reid, Rainer Prohaska, Philip S. Low, Michael J. Tanner, Narla Mohandas, and Kasturi Haldar. Erythrocyte detergent-resistant membrane proteins: their characterization and selective uptake during malarial infection. Blood, 103 5:1920-8, Mar 2004. URL: https://doi.org/10.1182/blood-2003-09-3165, doi:10.1182/blood-2003-09-3165. This article has 192 citations and is from a highest quality peer-reviewed journal.

3. (lu2024molecularmechanismof pages 1-3): Ming-Ao Lu, Yunwen Qian, Liangwen Ma, Qiang Guo, and Ning Gao. Molecular mechanism of the flotillin complex in membrane microdomain organization. bioRxiv, May 2024. URL: https://doi.org/10.1101/2024.05.25.595881, doi:10.1101/2024.05.25.595881. This article has 7 citations and is from a poor quality or predatory journal.

4. (carattino2020acidsensingionchannels pages 1-6): Marcelo D. Carattino and Nicolas Montalbetti. Acid-sensing ion channels in sensory signaling. American Journal of Physiology-Renal Physiology, 318:F531-F543, Mar 2020. URL: https://doi.org/10.1152/ajprenal.00546.2019, doi:10.1152/ajprenal.00546.2019. This article has 46 citations and is from a peer-reviewed journal.

5. (yan2025structuralroleof pages 1-5): Lu Yan, Xinyue Zhou, Meiqi Li, Chenxi Wang, Bailong Xiao, Peng Xi, Peng Zou, and Ning Gao. Structural role of stomatin in organizing functional membrane microdomains. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.08.30.673307, doi:10.1101/2025.08.30.673307. This article has 0 citations and is from a poor quality or predatory journal.

6. (yan2025structuralroleof pages 28-33): Lu Yan, Xinyue Zhou, Meiqi Li, Chenxi Wang, Bailong Xiao, Peng Xi, Peng Zou, and Ning Gao. Structural role of stomatin in organizing functional membrane microdomains. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.08.30.673307, doi:10.1101/2025.08.30.673307. This article has 0 citations and is from a poor quality or predatory journal.

7. (yan2025structuralroleof pages 5-9): Lu Yan, Xinyue Zhou, Meiqi Li, Chenxi Wang, Bailong Xiao, Peng Xi, Peng Zou, and Ning Gao. Structural role of stomatin in organizing functional membrane microdomains. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.08.30.673307, doi:10.1101/2025.08.30.673307. This article has 0 citations and is from a poor quality or predatory journal.

8. (yan2025structuralroleof pages 9-13): Lu Yan, Xinyue Zhou, Meiqi Li, Chenxi Wang, Bailong Xiao, Peng Xi, Peng Zou, and Ning Gao. Structural role of stomatin in organizing functional membrane microdomains. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.08.30.673307, doi:10.1101/2025.08.30.673307. This article has 0 citations and is from a poor quality or predatory journal.

9. (yan2025structuralroleof pages 33-40): Lu Yan, Xinyue Zhou, Meiqi Li, Chenxi Wang, Bailong Xiao, Peng Xi, Peng Zou, and Ning Gao. Structural role of stomatin in organizing functional membrane microdomains. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.08.30.673307, doi:10.1101/2025.08.30.673307. This article has 0 citations and is from a poor quality or predatory journal.

10. (yan2025structuralroleof pages 22-26): Lu Yan, Xinyue Zhou, Meiqi Li, Chenxi Wang, Bailong Xiao, Peng Xi, Peng Zou, and Ning Gao. Structural role of stomatin in organizing functional membrane microdomains. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.08.30.673307, doi:10.1101/2025.08.30.673307. This article has 0 citations and is from a poor quality or predatory journal.

11. (flatt2011stomatindeficientcryohydrocytosisresults pages 12-12): Joanna F. Flatt, Hélène Guizouarn, Nicholas M. Burton, Franck Borgese, Richard J. Tomlinson, Robert J. Forsyth, Stephen A. Baldwin, Bari E. Levinson, Philippe Quittet, Patricia Aguilar-Martinez, Jean Delaunay, Gordon W. Stewart, and Lesley J. Bruce. Stomatin-deficient cryohydrocytosis results from mutations in slc2a1: a novel form of glut1 deficiency syndrome. Blood, 118 19:5267-77, Nov 2011. URL: https://doi.org/10.1182/blood-2010-12-326645, doi:10.1182/blood-2010-12-326645. This article has 103 citations and is from a highest quality peer-reviewed journal.

12. (gallagher2017disordersoferythrocyte pages 1-5): Patrick G. Gallagher. Disorders of erythrocyte hydration. Blood, 130 25:2699-2708, Dec 2017. URL: https://doi.org/10.1182/blood-2017-04-590810, doi:10.1182/blood-2017-04-590810. This article has 141 citations and is from a highest quality peer-reviewed journal.

13. (freire2024completeabsenceof pages 1-3): CM Freire, NR King, M Dzieciatkowska, D Stephenson, PL Moura, J.G.G Dobbe, GJ Streekstra, A D’Alessandro, AM Toye, and TJ Satchwell. Complete absence of glut1 does not impair human terminal erythroid differentiation. bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.10.574621, doi:10.1101/2024.01.10.574621. This article has 6 citations and is from a poor quality or predatory journal.

14. (freire2024completeabsenceof pages 3-5): CM Freire, NR King, M Dzieciatkowska, D Stephenson, PL Moura, J.G.G Dobbe, GJ Streekstra, A D’Alessandro, AM Toye, and TJ Satchwell. Complete absence of glut1 does not impair human terminal erythroid differentiation. bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.10.574621, doi:10.1101/2024.01.10.574621. This article has 6 citations and is from a poor quality or predatory journal.

## Citations

1. murphy2004erythrocytedetergentresistantmembrane pages 1-2
2. lu2024molecularmechanismof pages 1-3
3. carattino2020acidsensingionchannels pages 1-6
4. flatt2011stomatindeficientcryohydrocytosisresults pages 12-12
5. gallagher2017disordersoferythrocyte pages 1-5
6. freire2024completeabsenceof pages 1-3
7. flatt2011stomatindeficientcryohydrocytosisresults pages 1-3
8. yan2025structuralroleof pages 1-5
9. yan2025structuralroleof pages 28-33
10. yan2025structuralroleof pages 5-9
11. yan2025structuralroleof pages 9-13
12. yan2025structuralroleof pages 33-40
13. yan2025structuralroleof pages 22-26
14. freire2024completeabsenceof pages 3-5
15. https://doi.org/10.1182/blood-2010-12-326645;
16. https://doi.org/10.1182/blood-2003-09-3165;
17. https://doi.org/10.1101/2024.05.25.595881
18. https://doi.org/10.1152/ajprenal.00546.2019
19. https://doi.org/10.1182/blood-2003-09-3165
20. https://doi.org/10.1101/2024.05.25.595881;
21. https://doi.org/10.1101/2025.08.30.673307
22. https://doi.org/10.1182/blood-2010-12-326645
23. https://doi.org/10.1182/blood-2017-04-590810
24. https://doi.org/10.1101/2024.01.10.574621
25. https://doi.org/10.1182/blood-2010-12-326645,
26. https://doi.org/10.1182/blood-2003-09-3165,
27. https://doi.org/10.1101/2024.05.25.595881,
28. https://doi.org/10.1152/ajprenal.00546.2019,
29. https://doi.org/10.1101/2025.08.30.673307,
30. https://doi.org/10.1182/blood-2017-04-590810,
31. https://doi.org/10.1101/2024.01.10.574621,