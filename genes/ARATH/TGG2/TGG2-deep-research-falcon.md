---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:29:47.798535'
end_time: '2026-09-30T06:44:11.342405'
duration_seconds: 863.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: TGG2
  gene_symbol: TGG2
  uniprot_accession: Q9C5C2
  protein_description: 'RecName: Full=Myrosinase 2 {ECO:0000250|UniProtKB:Q3ECS3};
    EC=3.2.1.147 {ECO:0000250|UniProtKB:Q3ECS3}; AltName: Full=Beta-glucosidase 37
    {ECO:0000303|PubMed:15604686}; Short=AtBGLU37 {ECO:0000303|PubMed:15604686}; AltName:
    Full=Sinigrinase 2 {ECO:0000250|UniProtKB:Q3ECS3}; AltName: Full=Thioglucosidase
    2 {ECO:0000250|UniProtKB:Q3ECS3}; Flags: Precursor;'
  gene_info: Name=TGG2 {ECO:0000250|UniProtKB:Q3ECS3}; Synonyms=BGLU37 {ECO:0000303|PubMed:15604686};
    OrderedLocusNames=At5g25980 {ECO:0000312|Araport:AT5G25980}; ORFNames=T1N24.18
    {ECO:0000312|EMBL:AAD40134.1};
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
citation_count: 40
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: TGG2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: TGG2-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: TGG2-deep-research-falcon_artifacts/artifact-02.md
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
- **UniProt Accession:** Q9C5C2
- **Protein Description:** RecName: Full=Myrosinase 2 {ECO:0000250|UniProtKB:Q3ECS3}; EC=3.2.1.147 {ECO:0000250|UniProtKB:Q3ECS3}; AltName: Full=Beta-glucosidase 37 {ECO:0000303|PubMed:15604686}; Short=AtBGLU37 {ECO:0000303|PubMed:15604686}; AltName: Full=Sinigrinase 2 {ECO:0000250|UniProtKB:Q3ECS3}; AltName: Full=Thioglucosidase 2 {ECO:0000250|UniProtKB:Q3ECS3}; Flags: Precursor;
- **Gene Information:** Name=TGG2 {ECO:0000250|UniProtKB:Q3ECS3}; Synonyms=BGLU37 {ECO:0000303|PubMed:15604686}; OrderedLocusNames=At5g25980 {ECO:0000312|Araport:AT5G25980}; ORFNames=T1N24.18 {ECO:0000312|EMBL:AAD40134.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the glycosyl hydrolase 1 family. .
- **Key Domains:** GH_1_N_CS. (IPR033132); GH_hydrolase_sf. (IPR017853); Glyco_hydro_1. (IPR001360); Glyco_hydro_1_AS. (IPR018120); Glyco_hydro_1 (PF00232)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TGG2" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TGG2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TGG2** (gene ID: TGG2, UniProt: Q9C5C2) in ARATH.

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
- **UniProt Accession:** Q9C5C2
- **Protein Description:** RecName: Full=Myrosinase 2 {ECO:0000250|UniProtKB:Q3ECS3}; EC=3.2.1.147 {ECO:0000250|UniProtKB:Q3ECS3}; AltName: Full=Beta-glucosidase 37 {ECO:0000303|PubMed:15604686}; Short=AtBGLU37 {ECO:0000303|PubMed:15604686}; AltName: Full=Sinigrinase 2 {ECO:0000250|UniProtKB:Q3ECS3}; AltName: Full=Thioglucosidase 2 {ECO:0000250|UniProtKB:Q3ECS3}; Flags: Precursor;
- **Gene Information:** Name=TGG2 {ECO:0000250|UniProtKB:Q3ECS3}; Synonyms=BGLU37 {ECO:0000303|PubMed:15604686}; OrderedLocusNames=At5g25980 {ECO:0000312|Araport:AT5G25980}; ORFNames=T1N24.18 {ECO:0000312|EMBL:AAD40134.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the glycosyl hydrolase 1 family. .
- **Key Domains:** GH_1_N_CS. (IPR033132); GH_hydrolase_sf. (IPR017853); Glyco_hydro_1. (IPR001360); Glyco_hydro_1_AS. (IPR018120); Glyco_hydro_1 (PF00232)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TGG2" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TGG2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TGG2** (gene ID: TGG2, UniProt: Q9C5C2) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive Research Report: TGG2 (At5g25980) Gene in Arabidopsis thaliana

### Gene Identity and Classification

TGG2 (THIOGLUCOSIDE GLUCOHYDROLASE 2, also designated BGLU37 or β-glucosidase 37) is encoded by the gene At5g25980 in *Arabidopsis thaliana* (wittstock2010glucosinolatebreakdownin pages 1-2, wittstock2010glucosinolatebreakdownin pages 2-4). The protein is a classical myrosinase (thioglucoside glucohydrolase, EC 3.2.1.147) belonging to glycosyl hydrolase family 1 (GH1) (lv2022thecellularand pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). TGG2 shares 72% sequence identity with its closest paralog TGG1 and 70% identity with TGG3, indicating that these classical myrosinases form a closely related tandem duplicate group on chromosome V (wittstock2010glucosinolatebreakdownin pages 2-4). TGG2 is evolutionarily classified as a QE-type myrosinase, distinguished by conserved glutamine and glutamate catalytic residues, which differentiates it from atypical EE-type myrosinases such as PEN2 that possess two glutamate residues (sugiyama2019atypicalmyrosinaseas pages 2-3).

### Primary Enzymatic Function and Catalytic Mechanism

TGG2 functions as a thioglucoside glucohydrolase that catalyzes the hydrolysis of glucosinolates, the characteristic sulfur-containing secondary metabolites of Brassicales plants (lv2022thecellularand pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). The enzyme employs a two-step retaining mechanism characteristic of GH1 enzymes, utilizing a (β/α)8 TIM-barrel fold structure (lv2022thecellularand pages 2-4). A catalytic glutamate residue performs nucleophilic attack on the thioglucosidic bond of the glucosinolate substrate, releasing the aglycone (thiohydroximate-O-sulfonate) and forming a covalent glucosyl–enzyme intermediate (lv2022thecellularand pages 2-4). Unlike typical GH1 β-glucosidases that use a glutamate as the catalytic acid/base, classical myrosinases including TGG2 contain a glutamine residue at this position (wittstock2010glucosinolatebreakdownin pages 1-2). This substitution necessitates ascorbate as an essential cofactor that acts as a proton donor to promote hydrolysis of the glucosyl–enzyme intermediate and release of glucose (lv2022thecellularand pages 2-4, chhajed2020glucosinolatebiosynthesisand pages 9-11, wittstock2010glucosinolatebreakdownin pages 1-2).

The aglycone product spontaneously loses sulfate and rearranges, typically forming isothiocyanates (wittstock2010glucosinolatebreakdownin pages 1-2). However, the final product spectrum depends on glucosinolate side-chain structure, pH, presence of ferrous ions, and interactions with specifier proteins, which can redirect the reaction toward alternative products including nitriles, epithionitriles, thiocyanates, or oxazolidine-2-thiones (chhajed2020glucosinolatebiosynthesisand pages 9-11).

### Substrate Specificity

TGG2 exhibits relatively broad substrate specificity toward glucosinolates (wittstock2010glucosinolatebreakdownin pages 2-4, sugiyama2019atypicalmyrosinaseas pages 6-7). Biochemical and genetic evidence indicates that TGG2, often assayed together with TGG1, shows preferential activity toward aliphatic glucosinolates including allyl glucosinolate (sinigrin), 3-butenyl glucosinolate, and 4-methylsulfinylbutyl glucosinolate (glucoraphanin), compared with hydroxyalkenyl glucosinolates such as 2(R)-2-hydroxy-3-butenyl glucosinolate and aromatic substrates like 2-phenylethyl glucosinolate (wittstock2010glucosinolatebreakdownin pages 2-4). TGG2 also hydrolyzes indole glucosinolates, although 4-methoxyindol-3-ylmethyl glucosinolate is processed more slowly than most aliphatic glucosinolates (wittstock2010glucosinolatebreakdownin pages 2-4). Together with TGG1, TGG2 accounts for rapid depletion of most endogenous glucosinolate species in rosette-leaf homogenates (sugiyama2019atypicalmyrosinaseas pages 6-7, wittstock2010glucosinolatebreakdownin pages 2-4). Proposed endogenous substrates based on overexpression studies include 4-methylthiobutyl glucosinolate, 4-methylpentyl glucosinolate, and 3-methylbutyl glucosinolate (chhajed2019chemodiversityofthe pages 5-6).

| Property | Details | Evidence Source |
|---|---|---|
| Enzyme classification | **Myrosinase 2 / thioglucoside glucohydrolase 2 / β-glucosidase 37 (TGG2/BGLU37); EC 3.2.1.147.** A classical **glycoside hydrolase family 1 (GH1)** myrosinase and member of the QE-type lineage, distinct from atypical EE-type myrosinases such as PEN2 and PYK10. | Wittstock & Burow, published January 2010 (wittstock2010glucosinolatebreakdownin pages 1-2); Sugiyama & Hirai, published August 2019 (sugiyama2019atypicalmyrosinaseas pages 2-3) |
| Catalytic mechanism | Cleaves the **S-glycosidic/thioglucosidic bond** of a glucosinolate through a retaining GH1 mechanism. A catalytic **glutamate** acts as the nucleophile and forms a covalent glucosyl–enzyme intermediate. Classical myrosinases contain **glutamine instead of the second catalytic glutamate** found in ordinary GH1 β-glucosidases; **ascorbate** supplies acid/base assistance and promotes hydrolysis of the intermediate and glucose release. Exact TGG2 residue numbers were not established in the cited sources. | Lv et al., published January 2022 (lv2022thecellularand pages 2-4); Wittstock & Burow, published January 2010 (wittstock2010glucosinolatebreakdownin pages 1-2); Chhajed et al., published November 2020 (chhajed2020glucosinolatebiosynthesisand pages 9-11) |
| Substrate specificity | The substrate class is **glucosinolates**, with comparatively broad specificity. Genetic and biochemical evidence supports activity toward endogenous leaf aliphatic and indole glucosinolates. TGG2-like activity is stronger toward **allyl glucosinolate (sinigrin), 3-butenyl glucosinolate, and 4-methylsulfinylbutyl glucosinolate (glucoraphanin)** than toward **2(R)-2-hydroxy-3-butenyl** and **2-phenylethyl glucosinolates**. Because many assays evaluated TGG1 and TGG2 jointly, these preferences should not be interpreted as an exclusive TGG2 substrate profile. | Wittstock & Burow, published January 2010 (wittstock2010glucosinolatebreakdownin pages 2-4); Chhajed et al., published May 2019 (chhajed2019chemodiversityofthe pages 5-6) |
| Reaction products | The immediate enzymatic products are **glucose** and an unstable **thiohydroximate-O-sulfonate aglycone**. After sulfate loss, the aglycone generally rearranges to an **isothiocyanate**; depending on substrate structure, pH, ferrous ions, and specifier proteins, downstream products can instead include **nitriles, epithionitriles, thiocyanates, or oxazolidine-2-thiones**. Product partitioning is therefore not determined by TGG2 alone. | Wittstock & Burow, published January 2010 (wittstock2010glucosinolatebreakdownin pages 1-2); Chhajed et al., published November 2020 (chhajed2020glucosinolatebiosynthesisand pages 9-11) |
| Protein structure | Expected to adopt the canonical GH1 **(β/α)8 TIM-barrel fold** containing the conserved classical-myrosinase catalytic architecture. TGG2 is most closely related to TGG1 among Arabidopsis classical myrosinases, with approximately **72% amino-acid identity**; the cited evidence describes the family fold rather than a TGG2-specific experimentally solved structure. | Lv et al., published January 2022 (lv2022thecellularand pages 2-4); Wittstock & Burow, published January 2010 (wittstock2010glucosinolatebreakdownin pages 2-4) |
| Post-translational modifications | TGG2 is an **N-glycosylated precursor protein**. Endogenous Arabidopsis TGG2 carries **exclusively oligomannosidic N-glycans**, consistent with its trafficking through the secretory system and accumulation in specialized myrosin-cell vacuoles. Its N-glycan profile resembles that of TGG1. | Liebminger et al., published December 2012 (liebminger2012myrosinasestgg1and pages 1-2, liebminger2012myrosinasestgg1and pages 4-5) |


*Table: Summary of the classification, catalytic mechanism, substrate range, products, structural framework, and glycosylation of Arabidopsis TGG2. The table distinguishes direct TGG2 evidence from conclusions inferred from classical GH1 myrosinases or joint TGG1/TGG2 experiments.*

### Subcellular Localization and Cellular Organization

TGG2 is localized in specialized vacuoles of myrosin cells, protein-accumulating idioblasts that are distributed along leaf veins and are particularly associated with the phloem (lv2022thecellularand pages 2-4, shirakawa2018specializedvacuolesof pages 2-4, ahuja2021theimagingof pages 1-2). Immunogold labeling and vacuolar proteomics have confirmed TGG2's presence in these specialized protein storage vacuoles, which display higher electron density than typical lytic vacuoles of surrounding mesophyll cells (wittstock2010glucosinolatebreakdownin pages 2-4, chhajed2019chemodiversityofthe pages 2-4, shirakawa2018specializedvacuolesof pages 2-4). This vacuolar sequestration is crucial for the "mustard oil bomb" defense strategy, as it maintains physical separation between TGG2 and its glucosinolate substrates, which are stored in distinct S-cells (sulfur-rich cells) or separate compartments (lv2022thecellularand pages 2-4, lv2022thecellularand pages 4-6, chhajed2019chemodiversityofthe pages 2-4).

TGG2 is synthesized as an N-glycosylated precursor protein that traffics through the secretory pathway and carries exclusively oligomannosidic N-glycans on its mature form (liebminger2012myrosinasestgg1and pages 1-2, liebminger2012myrosinasestgg1and pages 4-5). A fraction of TGG2 also occurs in low-speed-pelleting aggregates that may associate with ER bodies or protein complexes (wittstock2010glucosinolatebreakdownin pages 2-4). TGG2 specifically interacts with the myrosinase-associated protein MVP1, a trafficking component found in the tonoplast fraction, distinguishing it from TGG1, which does not show this interaction (agee2010modifiedvacuolephenotype1 pages 4-6, wittstock2010glucosinolatebreakdownin pages 2-4).

### Tissue-Specific Expression and Distribution

TGG2 is expressed predominantly in above-ground organs, including leaves, flowers, rosette tissue, and siliques, but is not detectably expressed in roots (agee2010modifiedvacuolephenotype1 pages 4-6, chhajed2019chemodiversityofthe pages 5-6, wittstock2010glucosinolatebreakdownin pages 1-2, liebminger2012myrosinasestgg1and pages 1-2). Within leaf tissue, TGG2 marks phloem-associated myrosin cells and idioblasts along veins (ahuja2021theimagingof pages 1-2). Importantly, TGG2 expression in stomatal guard cells is minimal or absent, contrasting sharply with TGG1, which is highly abundant in guard cells (zhao2008functionalproteomicsof pages 4-5, ahuja2021theimagingof pages 1-2). Guard-cell proteomic analyses detected 37 unique TGG1 peptides but only two unique TGG2 peptides in a single replicate, confirming that TGG2 is substantially less abundant than TGG1 in Col-0 rosette leaves overall (wittstock2010glucosinolatebreakdownin pages 2-4, zhao2008functionalproteomicsof pages 4-5).

TGG2 protein abundance varies developmentally and environmentally. During normal plant development, TGG2 protein levels and leaf myrosinase activity change, whereas TGG1 protein abundance remains relatively stable (brandt2018extendeddarknessinduces pages 5-8, brandt2018extendeddarknessinduces pages 1-2). Extended darkness increases TGG2 protein approximately 1.8-fold after three days and approximately twofold after seven days, associated with increased total myrosinase activity (brandt2018extendeddarknessinduces pages 5-8). Prolonged airborne methyl jasmonate treatment for five days significantly elevates TGG2 transcript abundance and protein levels in shoots (mirzaei2024longtermexposureto pages 4-6, mirzaei2024longtermexposureto pages 1-4).

| Category | Specific Location/Tissue | Expression Level | Key Characteristics |
|---|---|---|---|
| Subcellular localization | Specialized vacuoles of myrosin cells; detected by immunogold labeling and vacuolar proteomics in rosette leaves | Abundant within myrosin-cell protein-storage vacuoles | TGG2 is a vacuolar, glycosylated protein. Its sequestration helps separate myrosinase from glucosinolates until tissue disruption; some TGG2 also occurs in low-speed-pelleting aggregates, potentially reflecting protein complexes or association with endomembrane structures (wittstock2010glucosinolatebreakdownin pages 2-4, chhajed2019chemodiversityofthe pages 2-4, shirakawa2018specializedvacuolesof pages 2-4) |
| Cell-type specificity | Phloem-associated myrosin cells or idioblasts, especially along leaf veins and adjacent to glucosinolate-rich S-cells | High accumulation in specialized myrosin cells | TGG2 marks vascular-associated myrosin cells whose vacuoles function as vegetative protein-storage compartments. Most TGG2-specific reporter and proteomic evidence indicates little or no authentic expression in stomatal guard cells, although some reviews group TGG1 and TGG2 together there (zhao2008functionalproteomicsof pages 4-5, ahuja2021theimagingof pages 1-2, lv2022thecellularand pages 2-4, shirakawa2018specializedvacuolesof pages 2-4) |
| Tissue distribution | Leaves, flowers, rosette tissue, siliques, and other aerial tissues | Readily detectable in leaves and reproductive aerial organs; low or undetectable in roots | The distribution is consistent with TGG2 functioning as a principal shoot and leaf myrosinase positioned to activate foliar glucosinolates after herbivory or mechanical damage (agee2010modifiedvacuolephenotype1 pages 4-6, chhajed2019chemodiversityofthe pages 5-6, liebminger2012myrosinasestgg1and pages 1-2) |
| Organ-level expression | Above-ground organs, particularly rosette leaves and flowers | Strong aerial expression; developmentally and environmentally variable | TGG2 protein abundance changes with plant development and rises approximately 1.8-fold after three days and about twofold after seven days of extended darkness. Five-day airborne methyl-jasmonate exposure also increases TGG2 transcript and protein abundance in shoots (mirzaei2024longtermexposureto pages 4-6, brandt2018extendeddarknessinduces pages 5-8, brandt2018extendeddarknessinduces pages 1-2, mirzaei2024longtermexposureto pages 1-4) |
| Comparison with TGG1 | Both occur in aerial tissues and vacuoles of phloem-associated myrosin cells; TGG1 additionally accumulates strongly in guard cells | TGG2 is substantially less abundant than TGG1 in Col-0 rosette leaves and guard-cell preparations | The paralogs have overlapping biochemical functions but distinct spatial abundance. Guard-cell proteomics found 37 unique TGG1 peptides versus only two unique TGG2 peptides in one replicate, supporting TGG1—not TGG2—as the dominant guard-cell isoform; TGG2 also specifically interacts with the trafficking-associated protein MVP1 (wittstock2010glucosinolatebreakdownin pages 2-4, zhao2008functionalproteomicsof pages 4-5, agee2010modifiedvacuolephenotype1 pages 4-6) |


*Table: Summary of the cellular, subcellular, tissue, and organ-level distribution of Arabidopsis TGG2. The table also distinguishes its predominantly phloem-associated, vacuolar pattern from the stronger guard-cell expression of TGG1.*

### Biological Role in Plant Defense

TGG2 functions as a key component of the glucosinolate–myrosinase defense system, often called the "mustard oil bomb" (lv2022thecellularand pages 2-4, chhajed2020glucosinolatebiosynthesisand pages 9-11, wittstock2010glucosinolatebreakdownin pages 1-2). Under normal conditions, glucosinolates and myrosinases are spatially separated at the cellular and subcellular levels. Upon herbivore feeding, pathogen invasion, or mechanical tissue damage, this compartmentation is disrupted, allowing TGG2 to access and hydrolyze glucosinolates (lv2022thecellularand pages 2-4, lv2022thecellularand pages 4-6). The resulting toxic breakdown products—principally isothiocyanates and nitriles—can deter herbivores and inhibit pathogens (lv2022thecellularand pages 2-4, chhajed2019chemodiversityofthe pages 5-6, chhajed2020glucosinolatebiosynthesisand pages 9-11).

TGG2 contributes to defense against diverse herbivores, although its effectiveness varies with the attacking species. TGG1 and TGG2 together influence the feeding preference and growth performance of both generalist and specialist insects (chhajed2019chemodiversityofthe pages 5-6). The myrosinase system can also affect herbivores that sequester glucosinolates: plant myrosinases, including TGG2, reduce glucosinolate sequestration rates by specialized flea beetles by up to 50% through partial hydrolysis of ingested glucosinolates, although these beetles have evolved tolerance mechanisms (wittstock2010glucosinolatebreakdownin pages 2-4).

### Functional Redundancy with TGG1

TGG2 and TGG1 exhibit substantial functional redundancy in glucosinolate hydrolysis, particularly for aliphatic glucosinolates in leaf tissue (wittstock2010glucosinolatebreakdownin pages 2-4, liebminger2012myrosinasestgg1and pages 1-2). Single *tgg1* or *tgg2* knockout mutants retain considerable glucosinolate breakdown activity, as the remaining functional paralog can largely compensate (wittstock2010glucosinolatebreakdownin pages 2-4). In contrast, *tgg1 tgg2* double mutants eliminate detectable myrosinase activity toward exogenous allyl glucosinolate and prevent breakdown of endogenous aliphatic glucosinolates in disrupted leaves, demonstrating that these two classical myrosinases together account for the majority of foliar glucosinolate hydrolysis (wittstock2010glucosinolatebreakdownin pages 2-4). Residual breakdown of indole glucosinolates at lower rates in the double mutant indicates the existence of TGG1/TGG2-independent pathways, likely involving atypical myrosinases (wittstock2010glucosinolatebreakdownin pages 2-4).

Despite this redundancy, TGG2 and TGG1 differ in several important respects. TGG2 is generally less abundant than TGG1 in Col-0 rosette leaves (wittstock2010glucosinolatebreakdownin pages 2-4, zhao2008functionalproteomicsof pages 4-5). TGG1 is the dominant guard-cell myrosinase, while TGG2 is primarily phloem-associated (zhao2008functionalproteomicsof pages 4-5, ahuja2021theimagingof pages 1-2). TGG2 specifically interacts with the trafficking protein MVP1, whereas TGG1 does not (agee2010modifiedvacuolephenotype1 pages 4-6). These differences suggest distinct spatial contributions and potentially specialized regulatory mechanisms for each paralog within the overall myrosinase system.

### Role in Glucosinolate Turnover and Starvation Response

Recent evidence indicates that TGG2 participates in internal glucosinolate turnover during extended darkness and carbon starvation (brandt2018extendeddarknessinduces pages 5-8, brandt2018cysteinecatabolismand pages 92-97, brandt2018extendeddarknessinduces pages 8-9). When Arabidopsis plants are maintained in complete darkness for seven days, leaf glucosinolate content decreases substantially, particularly aliphatic methylthio-glucosinolates (brandt2018extendeddarknessinduces pages 5-8). This reduction is accompanied by increased myrosinase activity and strong induction of both TGG1 and TGG2 proteins (brandt2018extendeddarknessinduces pages 5-8, brandt2018cysteinecatabolismand pages 92-97, brandt2018extendeddarknessinduces pages 8-9). TGG2 protein abundance increases approximately 1.8-fold after three days and approximately twofold after seven days of darkness, even though overall protein degradation is occurring, indicating that TGG2 is specifically maintained and synthesized during the starvation response (brandt2018extendeddarknessinduces pages 5-8, brandt2018cysteinecatabolismand pages 103-106).

The coordinated induction of TGG2, increased nitrilase activity, and glucosinolate depletion suggest that internal glucosinolate breakdown may provide metabolizable substrates during carbon starvation, potentially releasing glucose and carbon-containing metabolites through the nitrilase-dependent pathway without generating toxic isothiocyanates (brandt2018extendeddarknessinduces pages 5-8, brandt2018extendeddarknessinduces pages 8-9). However, because both TGG1 and TGG2 are induced together, the specific contribution of TGG2 versus TGG1 to this process has not been definitively established (brandt2018cysteinecatabolismand pages 92-97, brandt2018extendeddarknessinduces pages 9-11).

In contrast, diurnal regulation of myrosinase activity appears to involve post-translational mechanisms. Myrosinase activity increases during the day and decreases at night in two-week-old plants, coinciding with higher daytime glucosinolate levels and enhanced sulfur incorporation, but TGG1 and TGG2 protein abundance do not show corresponding diurnal fluctuations (sugiyama2019atypicalmyrosinaseas pages 7-8, brandt2018cysteinecatabolismand pages 103-106). This suggests that short-term circadian control operates through unknown post-translational mechanisms, while long-term regulation under extended darkness involves transcriptional or translational induction of TGG2 (brandt2018cysteinecatabolismand pages 103-106, brandt2018extendeddarknessinduces pages 5-8).

### Regulation by Jasmonate Signaling

TGG2 responds to prolonged methyl jasmonate (MeJA) exposure, a hormone associated with wounding and defense responses (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 4-6, mirzaei2024longtermexposureto pages 1-4). Recent findings from 2024 reveal a dual regulatory mechanism: short-term (one-day) MeJA treatment produces weak TGG2 induction that depends on the canonical COI1 receptor and is largely absent in *coi1-16* and *myc2,3,4* mutants (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 4-6). In contrast, prolonged airborne MeJA exposure for five days significantly increases both TGG2 transcript abundance and protein levels in wild-type plants as well as in *coi1-16* and *myc2,3,4* mutants, demonstrating that sustained induction occurs through a COI1-independent and MYC2/3/4-independent pathway (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 4-6).

This long-term jasmonate response increases TGG2-associated myrosin cell area in some leaves but does not increase myrosin cell number or FAMA expression, suggesting that MeJA enhances TGG2 expression and possibly cell enlargement rather than promoting differentiation of new myrosin cells (mirzaei2024longtermexposureto pages 4-6, mirzaei2024longtermexposureto pages 9-12). The transcription factors responsible for the noncanonical long-term TGG2 induction pathway remain unidentified (mirzaei2024longtermexposureto pages 6-9). These findings provide evidence for an alternative jasmonate signaling pathway that can activate defense-related myrosinase expression independently of the well-characterized COI1–MYC2/3/4 module, although these results derive from a 2024 preprint and await independent confirmation (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 4-6).

| Biological Process | Role of TGG2 | Regulatory Factors | Phenotypic Effects |
|---|---|---|---|
| Plant defense against herbivores and pathogens | TGG2 is a classical leaf myrosinase in the glucosinolate–myrosinase “mustard oil bomb.” Tissue disruption brings the normally compartmentalized enzyme and glucosinolates together; TGG2 cleaves their thioglucosidic bond, initiating formation of isothiocyanates, nitriles, and related bioactive products that can deter or poison attackers. TGG1/TGG2 activity affects insect feeding, growth, and glucosinolate sequestration, although outcomes vary among herbivores. (chhajed2019chemodiversityofthe pages 5-6, chhajed2020glucosinolatebiosynthesisand pages 9-11, wittstock2010glucosinolatebreakdownin pages 1-2) | Activated chiefly by physical loss of cellular compartmentation during feeding or wounding. Product identity is further controlled by glucosinolate side-chain structure, pH, specifier proteins, and other interacting factors. (chhajed2020glucosinolatebiosynthesisand pages 9-11, wittstock2010glucosinolatebreakdownin pages 1-2) | Because of TGG1 redundancy, a **tgg2** single mutant has limited effects on bulk leaf glucosinolate activation. In contrast, **tgg1 tgg2** plants lack the two major foliar myrosinases and show markedly impaired damage-triggered glucosinolate hydrolysis. The defense consequence is attacker-dependent rather than universally increased susceptibility. (wittstock2010glucosinolatebreakdownin pages 2-4, sugiyama2019atypicalmyrosinaseas pages 6-7) |
| Glucosinolate turnover | TGG2 hydrolyzes a broad range of leaf glucosinolates. TGG1 and TGG2 together account for rapid depletion of most endogenous glucosinolates in disrupted rosette tissue and are especially important for aliphatic glucosinolate breakdown; some indole-glucosinolate turnover persists through other myrosinases. (wittstock2010glucosinolatebreakdownin pages 2-4) | Controlled by enzyme–substrate compartmentation, TGG2 abundance, developmental state, and potentially trafficking or binding factors such as MVP1. Daily changes in total myrosinase activity may involve post-translational regulation rather than corresponding changes in TGG2 abundance. (agee2010modifiedvacuolephenotype1 pages 4-6, sugiyama2019atypicalmyrosinaseas pages 7-8, brandt2018extendeddarknessinduces pages 9-11) | **tgg1** or **tgg2** single mutants retain substantial turnover, whereas the double mutant has no detectable activity toward exogenous allyl glucosinolate and fails to break down endogenous aliphatic glucosinolates efficiently after leaf disruption. Slower residual indole-glucosinolate degradation reveals parallel TGG1/TGG2-independent routes. (wittstock2010glucosinolatebreakdownin pages 2-4) |
| Starvation response | During prolonged darkness, TGG2 is maintained and induced while glucosinolate pools decline, implicating it—together with TGG1 and downstream nitrilases—in internal glucosinolate mobilization during carbon starvation. This may release glucose and carbon-containing metabolites, but a direct nutrient-recovery contribution uniquely attributable to TGG2 has not been proven. (brandt2018extendeddarknessinduces pages 5-8, brandt2018extendeddarknessinduces pages 8-9) | Extended darkness and carbohydrate starvation increase TGG2 protein abundance and total myrosinase activity. Short diurnal changes in activity occur without matching TGG2 abundance changes, indicating different long- and short-term regulatory mechanisms. (brandt2018extendeddarknessinduces pages 5-8, brandt2018extendeddarknessinduces pages 9-11) | After three days of darkness, TGG2 protein increased by approximately **1.8-fold**; after seven days, it increased by approximately **twofold**, alongside greater myrosinase activity and depletion of leaf glucosinolates. Causality remains unresolved because TGG1 and other catabolic enzymes are induced concurrently. (brandt2018extendeddarknessinduces pages 5-8, brandt2018extendeddarknessinduces pages 1-2) |
| Jasmonate signaling | TGG2 is a jasmonate-responsive defense enzyme rather than an established upstream jasmonate-signaling component. Sustained methyl jasmonate exposure increases TGG2 transcript and protein abundance, potentially expanding glucosinolate-activation capacity. (mirzaei2024longtermexposureto pages 1-4, mirzaei2024longtermexposureto pages 20-23) | A one-day methyl jasmonate response is weak and largely dependent on canonical **COI1** signaling. After five days, TGG2 induction persists in **coi1-16** and **myc2 myc3 myc4**, indicating a noncanonical COI1- and MYC2/3/4-independent route. FAMA expression and myrosin-cell number do not increase, and the alternative regulator remains unknown. These findings derive from a 2024 preprint and await independent confirmation. (mirzaei2024longtermexposureto pages 6-9, mirzaei2024longtermexposureto pages 4-6) | Five-day airborne methyl jasmonate treatment significantly raises TGG2 RNA and protein in wild type and canonical jasmonate-signaling mutants. Some leaves show enlarged myrosin-cell area, but not increased myrosin-cell number, arguing for altered expression or cell enlargement rather than wholesale differentiation of new myrosin cells. (mirzaei2024longtermexposureto pages 4-6, mirzaei2024longtermexposureto pages 9-12) |
| Redundancy with TGG1 | TGG2 and TGG1 are closely related, broad-spectrum classical myrosinases with largely overlapping catalytic roles in foliar aliphatic-glucosinolate hydrolysis. Their redundancy is incomplete: TGG2 is generally less abundant in Col-0 rosettes, is concentrated in phloem-associated myrosin cells, and specifically interacts with MVP1, whereas TGG1 is prominent in guard cells. (wittstock2010glucosinolatebreakdownin pages 2-4, zhao2008functionalproteomicsof pages 4-5, agee2010modifiedvacuolephenotype1 pages 4-6) | Compensation between the paralogs, unequal tissue abundance, cell-type-specific expression, and distinct protein interactions shape their relative contributions. Both can be induced by prolonged darkness and methyl jasmonate. (liebminger2012myrosinasestgg1and pages 1-2, brandt2018extendeddarknessinduces pages 5-8, mirzaei2024longtermexposureto pages 1-4) | Single knockouts generally retain bulk leaf myrosinase function, while **tgg1 tgg2** causes the strongest biochemical defect in aliphatic-glucosinolate breakdown. Stomatal and guard-cell structural phenotypes occur in single and double mutants, but interpretation of TGG2-specific effects is complicated by its low or disputed guard-cell expression and TGG1’s dominant abundance there. (wittstock2010glucosinolatebreakdownin pages 2-4, zhao2008functionalproteomicsof pages 4-5, ahuja2021theimagingof pages 3-6) |


*Table: Summary of TGG2’s experimentally supported roles in glucosinolate activation, defense, starvation-associated turnover, jasmonate response, and functional redundancy with TGG1. The table distinguishes established findings from interpretations that remain provisional.*

### Evolutionary and Structural Context

TGG2 belongs to the classical myrosinase lineage within glycosyl hydrolase family 1, a family characterized by the (β/α)8 TIM-barrel fold (lv2022thecellularand pages 2-4, wittstock2010glucosinolatebreakdownin pages 1-2). Classical myrosinases are thought to have evolved from ancestral β-O-glucosidases through adaptations that conferred specificity for S-glucosides (thioglucosides) rather than O-glucosides (wittstock2010glucosinolatebreakdownin pages 1-2). The QE-type catalytic signature (glutamine–glutamate) distinguishes classical myrosinases including TGG2 from atypical EE-type myrosinases (glutamate–glutamate) such as PEN2 and PYK10, which are thought to have arisen independently (sugiyama2019atypicalmyrosinaseas pages 2-3). TGG2 shows only 33% sequence identity with PEN2, reflecting this evolutionary divergence (wittstock2010glucosinolatebreakdownin pages 2-4).

Within the Arabidopsis genome, TGG2 (At5g25980) is most closely related to TGG1 (72% identity) and TGG3 (70% identity), forming a group of highly similar classical myrosinases on chromosome V (wittstock2010glucosinolatebreakdownin pages 2-4). TGG2 is more distantly related to the root-associated myrosinases TGG4 (57% identity), TGG5 (55% identity), and TGG6 (52% identity) (wittstock2010glucosinolatebreakdownin pages 2-4). This phylogenetic pattern reflects the tandem gene duplication events that generated the classical myrosinase family and the subsequent functional specialization of different members for specific tissues and defense roles (wittstock2010glucosinolatebreakdownin pages 1-2).

### Summary and Functional Integration

TGG2 is a classical thioglucoside glucohydrolase that serves as a principal leaf myrosinase in *Arabidopsis thaliana*, functioning within the glucosinolate–myrosinase "mustard oil bomb" defense system. The enzyme is localized in specialized vacuoles of phloem-associated myrosin cells, where it remains physically separated from glucosinolate substrates until tissue disruption by herbivores or pathogens triggers their interaction. Upon contact, TGG2 hydrolyzes glucosinolates using a two-step mechanism involving glutamate and glutamine catalytic residues with ascorbate as an essential cofactor, initiating formation of toxic isothiocyanates and nitriles that defend the plant.

TGG2 exhibits broad substrate specificity, preferentially hydrolyzing aliphatic glucosinolates such as allyl, 3-butenyl, and 4-methylsulfinylbutyl glucosinolates, while also processing indole glucosinolates. The enzyme functions largely redundantly with its close paralog TGG1 in aliphatic glucosinolate hydrolysis, although the two proteins differ in abundance, cellular distribution (TGG1 dominates in guard cells while TGG2 is phloem-associated), and protein interactions (TGG2 specifically binds MVP1).

Beyond its immediate defense role, TGG2 is regulated by environmental and developmental factors. Extended darkness and carbon starvation induce TGG2 protein accumulation approximately twofold, implicating it in glucosinolate turnover that may provide metabolic resources during starvation. Prolonged methyl jasmonate exposure increases TGG2 expression through both canonical COI1-dependent and novel COI1-independent pathways, enhancing the plant's capacity for glucosinolate-based chemical defense. These multiple regulatory mechanisms position TGG2 as a key enzyme integrating metabolic, developmental, and defense responses in Arabidopsis leaves.

References

1. (wittstock2010glucosinolatebreakdownin pages 1-2): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

2. (wittstock2010glucosinolatebreakdownin pages 2-4): Ute Wittstock and Meike Burow. Glucosinolate breakdown in arabidopsis: mechanism, regulation and biological significance. The Arabidopsis Book, 2010:e0134, Jan 2010. URL: https://doi.org/10.1199/tab.0134, doi:10.1199/tab.0134. This article has 382 citations and is from a peer-reviewed journal.

3. (lv2022thecellularand pages 2-4): Qiaoqiao Lv, Xifeng Li, Baofang Fan, Cheng Zhu, and Zhixiang Chen. The cellular and subcellular organization of the glucosinolate–myrosinase system against herbivores and pathogens. International Journal of Molecular Sciences, 23:1577, Jan 2022. URL: https://doi.org/10.3390/ijms23031577, doi:10.3390/ijms23031577. This article has 97 citations.

4. (sugiyama2019atypicalmyrosinaseas pages 2-3): Ryosuke Sugiyama and Masami Y. Hirai. Atypical myrosinase as a mediator of glucosinolate functions in plants. Frontiers in Plant Science, Aug 2019. URL: https://doi.org/10.3389/fpls.2019.01008, doi:10.3389/fpls.2019.01008. This article has 71 citations.

5. (chhajed2020glucosinolatebiosynthesisand pages 9-11): Shweta Chhajed, Islam Mostafa, Yan He, Maged Abou-Hashem, Maher El-Domiaty, and Sixue Chen. Glucosinolate biosynthesis and the glucosinolate–myrosinase system in plant defense. Agronomy, 10:1786, Nov 2020. URL: https://doi.org/10.3390/agronomy10111786, doi:10.3390/agronomy10111786. This article has 194 citations and is from a peer-reviewed journal.

6. (sugiyama2019atypicalmyrosinaseas pages 6-7): Ryosuke Sugiyama and Masami Y. Hirai. Atypical myrosinase as a mediator of glucosinolate functions in plants. Frontiers in Plant Science, Aug 2019. URL: https://doi.org/10.3389/fpls.2019.01008, doi:10.3389/fpls.2019.01008. This article has 71 citations.

7. (chhajed2019chemodiversityofthe pages 5-6): Shweta Chhajed, Biswapriya B. Misra, Nathalia Tello, and Sixue Chen. Chemodiversity of the glucosinolate-myrosinase system at the single cell type resolution. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00618, doi:10.3389/fpls.2019.00618. This article has 82 citations.

8. (liebminger2012myrosinasestgg1and pages 1-2): Eva Liebminger, Josephine Grass, Jakub Jez, Laura Neumann, Friedrich Altmann, and Richard Strasser. Myrosinases tgg1 and tgg2 from arabidopsis thaliana contain exclusively oligomannosidic n-glycans. Phytochemistry, 84:24-30, Dec 2012. URL: https://doi.org/10.1016/j.phytochem.2012.08.023, doi:10.1016/j.phytochem.2012.08.023. This article has 26 citations and is from a peer-reviewed journal.

9. (liebminger2012myrosinasestgg1and pages 4-5): Eva Liebminger, Josephine Grass, Jakub Jez, Laura Neumann, Friedrich Altmann, and Richard Strasser. Myrosinases tgg1 and tgg2 from arabidopsis thaliana contain exclusively oligomannosidic n-glycans. Phytochemistry, 84:24-30, Dec 2012. URL: https://doi.org/10.1016/j.phytochem.2012.08.023, doi:10.1016/j.phytochem.2012.08.023. This article has 26 citations and is from a peer-reviewed journal.

10. (shirakawa2018specializedvacuolesof pages 2-4): Makoto Shirakawa and Ikuko Hara-Nishimura. Specialized vacuoles of myrosin cells: chemical defense strategy in brassicales plants. Plant & cell physiology, 59 7:1309-1316, Jul 2018. URL: https://doi.org/10.1093/pcp/pcy082, doi:10.1093/pcp/pcy082. This article has 82 citations and is from a domain leading peer-reviewed journal.

11. (ahuja2021theimagingof pages 1-2): Ishita Ahuja, Ralph Kissen, Linh Hoang, Bjørnar Sporsheim, Kari K. Halle, Silje Aase Wolff, Samina Jam Nazeer Ahmad, Jam Nazeer Ahmad, and Atle M. Bones. The imaging of guard cells of thioglucosidase (tgg) mutants of arabidopsis further links plant chemical defence systems with physical defence barriers. Cells, 10:227, Jan 2021. URL: https://doi.org/10.3390/cells10020227, doi:10.3390/cells10020227. This article has 13 citations.

12. (chhajed2019chemodiversityofthe pages 2-4): Shweta Chhajed, Biswapriya B. Misra, Nathalia Tello, and Sixue Chen. Chemodiversity of the glucosinolate-myrosinase system at the single cell type resolution. Frontiers in Plant Science, May 2019. URL: https://doi.org/10.3389/fpls.2019.00618, doi:10.3389/fpls.2019.00618. This article has 82 citations.

13. (lv2022thecellularand pages 4-6): Qiaoqiao Lv, Xifeng Li, Baofang Fan, Cheng Zhu, and Zhixiang Chen. The cellular and subcellular organization of the glucosinolate–myrosinase system against herbivores and pathogens. International Journal of Molecular Sciences, 23:1577, Jan 2022. URL: https://doi.org/10.3390/ijms23031577, doi:10.3390/ijms23031577. This article has 97 citations.

14. (agee2010modifiedvacuolephenotype1 pages 4-6): April E. Agee, Marci Surpin, Eun Ju Sohn, Thomas Girke, Abel Rosado, Brian W. Kram, Clay Carter, Adam M. Wentzell, Daniel J. Kliebenstein, Hak Chul Jin, Ohkmae K. Park, Hailing Jin, Glenn R. Hicks, and Natasha V. Raikhel. Modified vacuole phenotype1 is an arabidopsis myrosinase-associated protein involved in endomembrane protein trafficking. Plant Physiology, 152:120-132, Oct 2010. URL: https://doi.org/10.1104/pp.109.145078, doi:10.1104/pp.109.145078. This article has 87 citations and is from a highest quality peer-reviewed journal.

15. (zhao2008functionalproteomicsof pages 4-5): Zhixin Zhao, Wei Zhang, B. Stanley, and S. Assmann. Functional proteomics of arabidopsis thaliana guard cells uncovers new stomatal signaling pathways[w][oa]. The Plant Cell Online, 20:3210-3226, Dec 2008. URL: https://doi.org/10.1105/tpc.108.063263, doi:10.1105/tpc.108.063263. This article has 340 citations.

16. (brandt2018extendeddarknessinduces pages 5-8): Saskia Brandt, Sara Fachinger, Takayuki Tohge, Alisdair R. Fernie, Hans-Peter Braun, and Tatjana M. Hildebrandt. Extended darkness induces internal turnover of glucosinolates in arabidopsis thaliana leaves. PLoS ONE, 13:e0202153, Aug 2018. URL: https://doi.org/10.1371/journal.pone.0202153, doi:10.1371/journal.pone.0202153. This article has 24 citations and is from a peer-reviewed journal.

17. (brandt2018extendeddarknessinduces pages 1-2): Saskia Brandt, Sara Fachinger, Takayuki Tohge, Alisdair R. Fernie, Hans-Peter Braun, and Tatjana M. Hildebrandt. Extended darkness induces internal turnover of glucosinolates in arabidopsis thaliana leaves. PLoS ONE, 13:e0202153, Aug 2018. URL: https://doi.org/10.1371/journal.pone.0202153, doi:10.1371/journal.pone.0202153. This article has 24 citations and is from a peer-reviewed journal.

18. (mirzaei2024longtermexposureto pages 4-6): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

19. (mirzaei2024longtermexposureto pages 1-4): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

20. (brandt2018cysteinecatabolismand pages 92-97): Saskia Sophie Brandt. Cysteine catabolism and glucosinolate turnover in arabidopsis thaliana. ArXiv, Jan 2018. URL: https://doi.org/10.15488/3090, doi:10.15488/3090. This article has 0 citations.

21. (brandt2018extendeddarknessinduces pages 8-9): Saskia Brandt, Sara Fachinger, Takayuki Tohge, Alisdair R. Fernie, Hans-Peter Braun, and Tatjana M. Hildebrandt. Extended darkness induces internal turnover of glucosinolates in arabidopsis thaliana leaves. PLoS ONE, 13:e0202153, Aug 2018. URL: https://doi.org/10.1371/journal.pone.0202153, doi:10.1371/journal.pone.0202153. This article has 24 citations and is from a peer-reviewed journal.

22. (brandt2018cysteinecatabolismand pages 103-106): Saskia Sophie Brandt. Cysteine catabolism and glucosinolate turnover in arabidopsis thaliana. ArXiv, Jan 2018. URL: https://doi.org/10.15488/3090, doi:10.15488/3090. This article has 0 citations.

23. (brandt2018extendeddarknessinduces pages 9-11): Saskia Brandt, Sara Fachinger, Takayuki Tohge, Alisdair R. Fernie, Hans-Peter Braun, and Tatjana M. Hildebrandt. Extended darkness induces internal turnover of glucosinolates in arabidopsis thaliana leaves. PLoS ONE, 13:e0202153, Aug 2018. URL: https://doi.org/10.1371/journal.pone.0202153, doi:10.1371/journal.pone.0202153. This article has 24 citations and is from a peer-reviewed journal.

24. (sugiyama2019atypicalmyrosinaseas pages 7-8): Ryosuke Sugiyama and Masami Y. Hirai. Atypical myrosinase as a mediator of glucosinolate functions in plants. Frontiers in Plant Science, Aug 2019. URL: https://doi.org/10.3389/fpls.2019.01008, doi:10.3389/fpls.2019.01008. This article has 71 citations.

25. (mirzaei2024longtermexposureto pages 6-9): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

26. (mirzaei2024longtermexposureto pages 9-12): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

27. (mirzaei2024longtermexposureto pages 20-23): Mohamadreza Mirzaei, Andisheh Poormassalehgoo, Kaichiro Endo, Ewa Dubas, and Kenji Yamada. Long-term exposure to methyl jasmonate increases myrosinases tgg1 and tgg2 in arabidopsis coi1 and myc2,3,4 mutants. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587911, doi:10.1101/2024.04.03.587911. This article has 0 citations.

28. (ahuja2021theimagingof pages 3-6): Ishita Ahuja, Ralph Kissen, Linh Hoang, Bjørnar Sporsheim, Kari K. Halle, Silje Aase Wolff, Samina Jam Nazeer Ahmad, Jam Nazeer Ahmad, and Atle M. Bones. The imaging of guard cells of thioglucosidase (tgg) mutants of arabidopsis further links plant chemical defence systems with physical defence barriers. Cells, 10:227, Jan 2021. URL: https://doi.org/10.3390/cells10020227, doi:10.3390/cells10020227. This article has 13 citations.

## Artifacts

- [Edison artifact artifact-00](TGG2-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](TGG2-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](TGG2-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. wittstock2010glucosinolatebreakdownin pages 2-4
2. sugiyama2019atypicalmyrosinaseas pages 2-3
3. lv2022thecellularand pages 2-4
4. wittstock2010glucosinolatebreakdownin pages 1-2
5. chhajed2020glucosinolatebiosynthesisand pages 9-11
6. chhajed2019chemodiversityofthe pages 5-6
7. ahuja2021theimagingof pages 1-2
8. brandt2018extendeddarknessinduces pages 5-8
9. mirzaei2024longtermexposureto pages 6-9
10. sugiyama2019atypicalmyrosinaseas pages 6-7
11. shirakawa2018specializedvacuolesof pages 2-4
12. chhajed2019chemodiversityofthe pages 2-4
13. lv2022thecellularand pages 4-6
14. zhao2008functionalproteomicsof pages 4-5
15. brandt2018extendeddarknessinduces pages 1-2
16. mirzaei2024longtermexposureto pages 4-6
17. mirzaei2024longtermexposureto pages 1-4
18. brandt2018cysteinecatabolismand pages 92-97
19. brandt2018extendeddarknessinduces pages 8-9
20. brandt2018cysteinecatabolismand pages 103-106
21. brandt2018extendeddarknessinduces pages 9-11
22. sugiyama2019atypicalmyrosinaseas pages 7-8
23. mirzaei2024longtermexposureto pages 9-12
24. mirzaei2024longtermexposureto pages 20-23
25. ahuja2021theimagingof pages 3-6
26. w
27. oa
28. https://doi.org/10.1199/tab.0134,
29. https://doi.org/10.3390/ijms23031577,
30. https://doi.org/10.3389/fpls.2019.01008,
31. https://doi.org/10.3390/agronomy10111786,
32. https://doi.org/10.3389/fpls.2019.00618,
33. https://doi.org/10.1016/j.phytochem.2012.08.023,
34. https://doi.org/10.1093/pcp/pcy082,
35. https://doi.org/10.3390/cells10020227,
36. https://doi.org/10.1104/pp.109.145078,
37. https://doi.org/10.1105/tpc.108.063263,
38. https://doi.org/10.1371/journal.pone.0202153,
39. https://doi.org/10.1101/2024.04.03.587911,
40. https://doi.org/10.15488/3090,