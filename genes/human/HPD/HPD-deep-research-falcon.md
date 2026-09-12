---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T17:53:58.498257'
end_time: '2026-07-05T18:17:43.282072'
duration_seconds: 1424.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: HPD
  gene_symbol: HPD
  uniprot_accession: P32754
  protein_description: 'RecName: Full=4-hydroxyphenylpyruvate dioxygenase; EC=1.13.11.27
    {ECO:0000269|PubMed:1339442, ECO:0000269|PubMed:34047349}; AltName: Full=4-hydroxyphenylpyruvic
    acid oxidase; Short=4HPPD; Short=HPD; Short=HPPDase; AltName: Full=N(6)-adenosine-methyltransferase
    HPD {ECO:0000305|PubMed:41317403}; EC=2.1.1.348 {ECO:0000269|PubMed:41317403};'
  gene_info: Name=HPD; Synonyms=PPD;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the 4HPPD family. .
  protein_domains: 4OHPhenylPyrv_dOase. (IPR005956); 4OHPhenylPyrv_dOase_C. (IPR041735);
    4OHPhenylPyrv_dOase_N. (IPR041736); Glyas_Bleomycin-R_OHBP_Dase. (IPR029068);
    Glyas_Fos-R_dOase_dom. (IPR004360)
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
  path: HPD-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: HPD-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** P32754
- **Protein Description:** RecName: Full=4-hydroxyphenylpyruvate dioxygenase; EC=1.13.11.27 {ECO:0000269|PubMed:1339442, ECO:0000269|PubMed:34047349}; AltName: Full=4-hydroxyphenylpyruvic acid oxidase; Short=4HPPD; Short=HPD; Short=HPPDase; AltName: Full=N(6)-adenosine-methyltransferase HPD {ECO:0000305|PubMed:41317403}; EC=2.1.1.348 {ECO:0000269|PubMed:41317403};
- **Gene Information:** Name=HPD; Synonyms=PPD;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the 4HPPD family. .
- **Key Domains:** 4OHPhenylPyrv_dOase. (IPR005956); 4OHPhenylPyrv_dOase_C. (IPR041735); 4OHPhenylPyrv_dOase_N. (IPR041736); Glyas_Bleomycin-R_OHBP_Dase. (IPR029068); Glyas_Fos-R_dOase_dom. (IPR004360)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HPD" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HPD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HPD** (gene ID: HPD, UniProt: P32754) in human.

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
- **UniProt Accession:** P32754
- **Protein Description:** RecName: Full=4-hydroxyphenylpyruvate dioxygenase; EC=1.13.11.27 {ECO:0000269|PubMed:1339442, ECO:0000269|PubMed:34047349}; AltName: Full=4-hydroxyphenylpyruvic acid oxidase; Short=4HPPD; Short=HPD; Short=HPPDase; AltName: Full=N(6)-adenosine-methyltransferase HPD {ECO:0000305|PubMed:41317403}; EC=2.1.1.348 {ECO:0000269|PubMed:41317403};
- **Gene Information:** Name=HPD; Synonyms=PPD;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the 4HPPD family. .
- **Key Domains:** 4OHPhenylPyrv_dOase. (IPR005956); 4OHPhenylPyrv_dOase_C. (IPR041735); 4OHPhenylPyrv_dOase_N. (IPR041736); Glyas_Bleomycin-R_OHBP_Dase. (IPR029068); Glyas_Fos-R_dOase_dom. (IPR004360)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HPD" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HPD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HPD** (gene ID: HPD, UniProt: P32754) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: HPD (4-Hydroxyphenylpyruvate Dioxygenase) — Human Gene (UniProt P32754)

## 1. Gene and Protein Identity

The HPD gene (also known as PPD) encodes 4-hydroxyphenylpyruvate dioxygenase (4-HPPD, EC 1.13.11.27), a 393 amino acid cytosolic enzyme with a molecular mass of approximately 45 kDa (farrera2022thehumanglyoxalase pages 7-8, trezza2024molecularandevolution pages 1-2). The gene is located on chromosome 12q24.31 and comprises 14 exons, with two known isoforms, the major functional protein being the 393-residue form (farrera2022thehumanglyoxalase pages 7-8). HPD is a member of the vicinal oxygen chelate (VOC)/glyoxalase superfamily, sharing the characteristic βαβββ glyoxalase fold structural motif with other family members (farrera2022thehumanglyoxalase pages 1-3, farrera2022thehumanglyoxalase pages 18-25). The enzyme is conserved across all eukaryotes and is also found in bacteria (farrera2022thehumanglyoxalase pages 8-10).

The following table summarizes the key properties of HPD:

| Property | HPD summary |
|---|---|
| Gene name | **HPD** (4-hydroxyphenylpyruvate dioxygenase) (farrera2022thehumanglyoxalase pages 8-10, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 1-2) |
| UniProt ID | **P32754** |
| Protein size | **393 aa**, ~**40–50 kDa** (~45 kDa) (trezza2024molecularandevolution pages 1-2) |
| Chromosomal location | **12q24.31** (farrera2022thehumanglyoxalase pages 7-8) |
| EC number | **EC 1.13.11.27** (4-hydroxyphenylpyruvate dioxygenase) (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) |
| Enzyme class | **Fe(II)-dependent non-heme oxygenase**; an α-keto-acid-dependent oxygenase/dioxygenase (trezza2024molecularandevolution pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) |
| Substrate | **4-hydroxyphenylpyruvate (4-HPP / HPP / pHPP)** (trezza2024molecularandevolution pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) |
| Product | **Homogentisate / homogentisic acid (HGA)** (trezza2024molecularandevolution pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 7-8) |
| Cofactors / reaction requirements | **Fe(II)** and **molecular oxygen** are required; **ascorbate** helps maintain the iron in the reduced ferrous state (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 6-7) |
| Active-site metal ligands / key catalytic residues | **His183, His266, Glu349** coordinate Fe(II) and are central to catalysis (trezza2024molecularandevolution pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) |
| Oligomeric state | **Homodimer** (trezza2024molecularandevolution pages 1-2) |
| Subcellular localization | Primarily **cytosolic** (farrera2022thehumanglyoxalase pages 8-10, farrera2022thehumanglyoxalase pages 7-8) |
| Primary tissue expression | Highest in **liver**, with smaller amounts in **kidney**; largely liver/kidney-enriched (farrera2022thehumanglyoxalase pages 8-10, wilson2021expressionoftyrosine pages 6-7) |
| Structural family | Member of the **vicinal oxygen chelate (VOC)/glyoxalase superfamily**; shares the glyoxalase fold and divalent-metal-binding architecture (farrera2022thehumanglyoxalase pages 1-3, farrera2022thehumanglyoxalase pages 18-25) |
| Domain/architecture notes | Two VOC domains; active site formed in the conserved C-terminal region; C-terminal tail acts as a catalytic gate (trezza2024molecularandevolution pages 1-2, trezza2024molecularandevolution pages 4-6) |
| Pathway role | Catalyzes the **second step of tyrosine degradation**, downstream of **TAT** and upstream of **HGD** and **FAH** (neuckermans2019arobustbacterial pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) |
| Associated inherited diseases | **Tyrosinemia type III** and **hawkinsinuria** (alsharhan2020disordersofphenylalanine pages 31-33, holme2013tyrosinemetabolism pages 2-4) |
| Representative disease features | Tyrosinemia III: elevated tyrosine with neurologic features such as seizures/ataxia/developmental delay and typically no liver disease; Hawkinsinuria: infantile failure to thrive and metabolic acidosis, often improving after infancy (alsharhan2020disordersofphenylalanine pages 31-33, holme2013tyrosinemetabolism pages 2-4) |
| Key therapeutic inhibitor | **Nitisinone (NTBC)**, a potent reversible competitive HPD inhibitor used clinically in **HT1** and used/off-label or investigational in **AKU** to reduce HGA (neuckermans2019arobustbacterial pages 1-2, bernardini2025acomprehensivein pages 82-84) |
| Recent moonlighting activity | UniProt additionally annotates a recently reported **N(6)-adenosine-methyltransferase** activity (**EC 2.1.1.348**); the primary paper was not retrievable here, so this function should be regarded as **very recent and not yet independently evaluated in this report** (UniProt-provided context; see also unobtainable Wang et al. reference noted during search) |


*Table: This table summarizes the core biochemical, structural, localization, pathway, disease, and therapeutic properties of human HPD/4-hydroxyphenylpyruvate dioxygenase. It is useful as a compact reference for the main facts that support functional annotation of UniProt P32754.*

## 2. Primary Enzymatic Function and Catalytic Mechanism

### 2.1 Reaction Catalyzed

HPD catalyzes the oxidative decarboxylation and hydroxylation of 4-hydroxyphenylpyruvate (4-HPP) to produce homogentisate (homogentisic acid, HGA), which represents the second enzymatic step in the tyrosine catabolism pathway (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3, neuckermans2019arobustbacterial pages 1-2). The enzyme belongs to the class of Fe(II)-dependent, non-heme α-keto acid-dependent oxygenases, though it is unusual within this class in that its α-keto acid moiety is part of the substrate itself rather than being an external cofactor such as α-ketoglutarate (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3). Only two substrates are required: the small molecule substrate 4-HPP and molecular oxygen (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3). Ascorbate serves an auxiliary role in maintaining the active-site iron in the catalytically competent Fe(II) state (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 1-2, alsharhan2020disordersofphenylalanine pages 31-33).

### 2.2 Catalytic Mechanism

The catalytic mechanism involves a complex, multi-step transformation. After 4-HPP binds to the Fe(II) center in the active site, the iron shifts from six- to five-coordinate geometry, enabling molecular oxygen binding (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 7-9). The reaction then proceeds through the following major steps:

1. **Oxidative decarboxylation:** Dioxygen attacks the Fe(II)-substrate complex to form a ferric superoxide intermediate, which rearranges to a peracid. Heterolytic cleavage of the peroxide bond generates a highly reactive Fe(IV)=O (ferryl-oxo) species with concomitant release of CO₂, producing p-hydroxyphenylacetate (pHPA) as a bound intermediate (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 7-8, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 6-7).

2. **Aromatic ring hydroxylation:** The Fe(IV)=O species performs electrophilic attack on the aromatic ring at position C-1, generating an arene oxide (benzene oxide) intermediate—a long-postulated species that was experimentally supported by Gunsior et al. (2004) (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 10-11, gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 9-10).

3. **1,2-Migration (NIH shift):** The carboxymethyl side chain migrates from C-1 to the adjacent ring carbon through what is termed the NIH shift, leading to rearomatization and production of the final hydroquinone product, homogentisate (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 7-8).

Both atoms of oxygen from molecular O₂ are incorporated into the product, confirming dioxygenase activity (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 1-2). Several catalytic steps remain experimentally inaccessible, and alternative mechanistic routes have been proposed through computational density functional theory studies (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 7-8).

### 2.3 Active Site and Key Residues

The catalytic iron is coordinated by the conserved 2-His-1-carboxylate facial triad composed of His183, His266, and Glu349, with additional coordination sites occupied by water molecules (trezza2024molecularandevolution pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3, gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 4-5). Glu349 is critical for both Fe(II)/substrate complex formation and dioxygen activation, with variants at this position retaining only 5–10% residual activity (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3). His266 regulates the geometry of the reactive oxygen intermediate, while His183 plays a role in protecting the active site from oxidative damage (trezza2024molecularandevolution pages 1-2). Active site residues Phe337, Asn216, and Pro214 function in substrate positioning rather than direct catalysis (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 9-10).

## 3. Protein Structure

Human HPD exists as a homodimer and contains two VOC (vicinal oxygen chelate) domains: VOC 1 (residues 18–149) and VOC 2 (residues 180–338) (trezza2024molecularandevolution pages 1-2). The primary structure divides into a variable N-terminal region of unknown function and a conserved C-terminal region that exclusively forms the active site (trezza2024molecularandevolution pages 1-2). The active site is buried within a barrel-like β-sheet structure (trezza2024molecularandevolution pages 8-10).

A distinctive feature of mammalian HPD is the C-terminal tail (residues 375–393), which functions as a dynamic gate controlling substrate access to the active site (trezza2024molecularandevolution pages 1-2, trezza2024molecularandevolution pages 4-6). A 2024 molecular dynamics and evolutionary study by Trezza et al. elucidated this gating mechanism in detail, showing that the wild-type enzyme transitions between two stable conformational states: an "open" (inactive) state where the active site is solvent-accessible, and a "closed" (active) state where the tail covers the active site and isolates the bound substrate during catalysis (trezza2024molecularandevolution pages 4-6, trezza2024molecularandevolution pages 6-8). Key residues involved in this gating include Gln375, Arg378, Tyr221, Lys39, and Met393, which form a hydrogen bond network (trezza2024molecularandevolution pages 2-4, trezza2024molecularandevolution pages 4-6). Mutations at Q375 and R378 abolish enzyme activity by locking the C-terminal tail in the open conformation (trezza2024molecularandevolution pages 2-4, trezza2024molecularandevolution pages 6-8). This C-terminal gating tail appears to be unique to the mammalian class of 4-HPPD enzymes (trezza2024molecularandevolution pages 10-12).

No complete full-length 3D crystal structure of human HPD has been determined experimentally; the most commonly used template is PDB 5EC3 (2.10 Å resolution), with the structure modeled computationally for the terminal tail region (trezza2024molecularandevolution pages 2-4, trezza2024molecularandevolution pages 10-12). A crystal structure is available at PDB 3ISQ (farrera2022thehumanglyoxalase pages 18-25).

## 4. Subcellular Localization and Tissue Expression

HPD is primarily a **cytosolic** enzyme (farrera2022thehumanglyoxalase pages 8-10, farrera2022thehumanglyoxalase pages 7-8, alsharhan2020disordersofphenylalanine pages 31-33). Its enzymatic activity occurs in the cytoplasm, where it utilizes ascorbic acid as a stabilizing natural cofactor (alsharhan2020disordersofphenylalanine pages 31-33).

HPD expression is highly tissue-restricted. The enzyme is expressed almost exclusively in the **liver** and **kidneys**, with the liver showing the highest expression levels (farrera2022thehumanglyoxalase pages 8-10, farrera2022thehumanglyoxalase pages 7-8, wilson2021expressionoftyrosine pages 6-7, wilson2021expressionoftyrosine pages 1-3). Studies in mouse tissue confirmed that 4-Hppd mRNA is most abundant in liver, with smaller amounts in kidney and low-level expression detectable in other tissues (wilson2021expressionoftyrosine pages 6-7, wilson2021expressionoftyrosine pages 1-3). This tissue distribution pattern is consistent with the liver being the primary organ for tyrosine catabolism.

## 5. Position in the Tyrosine Catabolism Pathway

HPD catalyzes the second step in the five-step tyrosine degradation pathway, one of the major amino acid catabolic pathways in mammals. The complete pathway and associated disease deficiencies are summarized below:

| Step | Enzyme (gene) | Reaction | Disease associated with deficiency | Nitisinone action |
|---|---|---|---|---|
| 1 | Tyrosine aminotransferase (**TAT**) | Tyrosine → 4-hydroxyphenylpyruvate (colemontsvroninks2020oxidativestressglutathione pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) | Tyrosinemia type II | No |
| 2 | 4-hydroxyphenylpyruvate dioxygenase (**HPD**) | 4-hydroxyphenylpyruvate → homogentisate (neuckermans2019arobustbacterial pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) | Tyrosinemia type III / Hawkinsinuria (alsharhan2020disordersofphenylalanine pages 31-33, holme2013tyrosinemetabolism pages 2-4) | **Yes — nitisinone inhibits HPD at this step** (neuckermans2019arobustbacterial pages 1-2) |
| 3 | Homogentisate 1,2-dioxygenase (**HGD**) | Homogentisate → 4-maleylacetoacetate (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3, holme2013tyrosinemetabolism pages 2-4) | Alkaptonuria | No |
| 4 | Maleylacetoacetate isomerase (**MAI / GSTZ1**) | 4-maleylacetoacetate → 4-fumarylacetoacetate (colemontsvroninks2020oxidativestressglutathione pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3) | Not specified in the cited pathway sources | No |
| 5 | Fumarylacetoacetate hydrolase (**FAH**) | 4-fumarylacetoacetate → fumarate + acetoacetate (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3, holme2013tyrosinemetabolism pages 2-4) | Tyrosinemia type I (colemontsvroninks2020oxidativestressglutathione pages 1-2, alsharhan2020disordersofphenylalanine pages 23-26) | No |


*Table: This table summarizes the five core enzymatic steps of tyrosine degradation, highlighting where HPD functions and where nitisinone exerts its therapeutic effect. It also links key enzyme deficiencies to their associated inherited metabolic disorders.*

In the sequential pathway, tyrosine aminotransferase (TAT) first converts L-tyrosine to 4-hydroxyphenylpyruvate. HPD then catalyzes the conversion of this intermediate to homogentisate. Downstream, homogentisate 1,2-dioxygenase (HGD) performs a ring-opening reaction to produce 4-maleylacetoacetate, which is isomerized by maleylacetoacetate isomerase (MAI/GSTZ1) to 4-fumarylacetoacetate. Finally, fumarylacetoacetate hydrolase (FAH) cleaves this compound to yield fumarate and acetoacetate, both of which enter the TCA cycle and energy metabolism (colemontsvroninks2020oxidativestressglutathione pages 1-2, santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3).

## 6. Disease Associations and Clinical Significance

### 6.1 Tyrosinemia Type III

Loss-of-function mutations in HPD cause **tyrosinemia type III** (TYR3), an extremely rare autosomal recessive disorder with fewer than six identified patients at the time of review (scott2006thegenetictyrosinemias pages 5-6). Clinical features include elevated blood tyrosine, mild developmental delay, seizures, ataxia, and in some cases autism (alsharhan2020disordersofphenylalanine pages 31-33). Importantly, unlike tyrosinemia type I, there is no liver involvement and no reported skin or ocular changes (scott2006thegenetictyrosinemias pages 5-6). The mutation p.Tyr160Cys (c.479A>G) has been identified in affected patients (alsharhan2020disordersofphenylalanine pages 31-33). Management involves a diet low in phenylalanine and tyrosine, along with ascorbic acid supplementation (scott2006thegenetictyrosinemias pages 5-6).

### 6.2 Hawkinsinuria

**Hawkinsinuria** is a distinct disorder caused by specific HPD mutations that alter rather than abolish catalytic activity, resulting in an autosomal dominant inheritance pattern—unusual for a metabolic enzyme deficiency (alsharhan2020disordersofphenylalanine pages 31-33, scott2006thegenetictyrosinemias pages 5-6). The p.Ala33Thr mutation is common in hawkinsinuria families, and p.Asn241Ser (c.722A>G) has been identified in multiple patients (alsharhan2020disordersofphenylalanine pages 31-33, holme2013tyrosinemetabolism pages 2-4). The pathogenic mechanism involves the mutant enzyme's inability to complete the rearrangement step, resulting in formation of a reactive quinol acetate (epoxide) intermediate instead of homogentisate. This reactive intermediate reacts with thiols (including cysteine and glutathione) to form hawkinsin, a diagnostic urinary metabolite (holme2013tyrosinemetabolism pages 2-4). Clinical features include failure to thrive, chronic metabolic acidosis, and sparse fine hair in infancy, with symptoms typically resolving spontaneously around age one (alsharhan2020disordersofphenylalanine pages 31-33, holme2013tyrosinemetabolism pages 8-9).

### 6.3 HPD as a Therapeutic Target: Nitisinone

HPD is the molecular target of **nitisinone (NTBC/Orfadin)**, a β-triketone compound that acts as a potent, reversible, competitive inhibitor (neuckermans2019arobustbacterial pages 1-2, scott2006thegenetictyrosinemias pages 2-3). At therapeutic doses of approximately 1 mg/kg/day, nitisinone achieves plasma concentrations sufficient to inhibit >99.9% of HPD enzymatic activity (scott2006thegenetictyrosinemias pages 2-3). By blocking HPD, nitisinone prevents formation of homogentisate and all downstream toxic metabolites.

In **hereditary tyrosinemia type I** (HT1), caused by FAH deficiency, nitisinone prevents accumulation of the hepatotoxic metabolites fumarylacetoacetate, maleylacetoacetate, and succinylacetone, thereby averting liver failure, renal damage, and neurological crises (neuckermans2019arobustbacterial pages 1-2, colemontsvroninks2020oxidativestressglutathione pages 1-2). It has been a life-saving treatment since 1992, with FDA approval in 2002, and early treatment initiated through newborn screening prevents hepatic cancer development (holme2013tyrosinemetabolism pages 7-8, alsharhan2020disordersofphenylalanine pages 23-26).

In **alkaptonuria** (AKU), caused by HGD deficiency, nitisinone reduces homogentisic acid levels by up to 99.7%, as demonstrated in the SONIA-2 clinical trial, potentially preventing ochronotic pigment deposition in joints and tissues (bernardini2025acomprehensivein pages 6-9, bernardini2025acomprehensivein pages 82-84). However, nitisinone treatment induces secondary hypertyrosinemia, requiring dietary protein restriction (neuckermans2019arobustbacterial pages 1-2, holme2013tyrosinemetabolism pages 7-8). Newer triketone-based HPPD inhibitors with improved pharmacological profiles are being actively developed (neuckermans2019arobustbacterial pages 1-2).

## 7. Structural Superfamily Context

HPD is one of six members of the human glyoxalase gene family, which share the VOC superfamily fold characterized by bidentate coordination of substrate to a divalent metal center using vicinal oxygen atoms (farrera2022thehumanglyoxalase pages 1-3). Despite this shared structural motif, glyoxalase family members are functionally diverse: HPD functions in amino acid metabolism, methylmalonyl-CoA epimerase (MCEE) in primary metabolism, and glyoxalase 1 (GLO1) in aldehyde detoxification (farrera2022thehumanglyoxalase pages 1-3). HPD (393 amino acids) is larger than GLO1 (184 aa), MCEE (176 aa), and GLOD5 (160 aa), but smaller than GLOD4 (502 aa) (farrera2022thehumanglyoxalase pages 18-25).

## 8. Emerging Non-Canonical Functions

### 8.1 Role in Cancer Metabolism

Beyond its canonical role in tyrosine catabolism, HPD has been implicated in cancer metabolism. In lung cancer, HPD was found to be overexpressed in 83.3% of patient tumor tissues, with higher expression correlating with poor overall survival (shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 2-4). Mechanistically, HPD promotes oxidative pentose phosphate pathway (PPP) flux through the LKB1-AMPK/HDAC10/G6PD signaling axis: HPD-mediated tyrosine catabolism increases acetyl-CoA production, fueling histone acetylation modifications that enhance G6PD transcription. Simultaneously, HPD stimulates LKB1-AMPK signaling, which phosphorylates HDAC10 and promotes its translocation from the nucleus to the cytoplasm, further regulating histone acetylation at the G6PD promoter (shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 1-2, shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 7-10, shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 4-7). Knockdown of HPD decreases PPP flux, reduces RNA biosynthesis, increases reactive oxygen species, and attenuates tumor growth (shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 1-2, shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 2-4).

### 8.2 Recently Reported N(6)-Adenosine Methyltransferase Activity

A very recent and notable development is the annotation in UniProt (based on PubMed:41317403) of a previously unrecognized **N(6)-adenosine-methyltransferase** activity for HPD (EC 2.1.1.348). According to the UniProt annotation and the corresponding reference (Wang et al., *Advanced Science*, 2026), HPD functions as an m⁶A methyltransferase that protects colorectal cancer cells from ferroptotic cell death by m⁶A methylation of SLC7A11 and GPX4 mRNAs. This represents a remarkable moonlighting function for a well-characterized metabolic enzyme. However, the primary publication was not accessible for detailed evaluation in this report, and this finding should be considered very recent and awaiting independent validation.

## 9. Summary

HPD (4-hydroxyphenylpyruvate dioxygenase) is a well-characterized Fe(II)-dependent, non-heme oxygenase that catalyzes the conversion of 4-hydroxyphenylpyruvate to homogentisate as the second step in the cytosolic tyrosine degradation pathway, predominantly in the liver and kidneys. The enzyme functions as a homodimer with a unique C-terminal gating mechanism that regulates active-site access. Mutations in HPD cause two rare inherited metabolic diseases: tyrosinemia type III (autosomal recessive) and hawkinsinuria (autosomal dominant). HPD is also the molecular target of nitisinone, a clinically important drug used in the treatment of hereditary tyrosinemia type I and, investigationally, alkaptonuria. Emerging research has uncovered additional roles for HPD in cancer metabolism through the pentose phosphate pathway, and a very recently reported moonlighting activity as an m⁶A RNA methyltransferase represents a potentially significant new dimension of HPD biology that remains to be fully characterized.

References

1. (farrera2022thehumanglyoxalase pages 7-8): Dominique O. Farrera and James J. Galligan. The human glyoxalase gene family in health and disease. Chemical research in toxicology, 35:1766-1776, Sep 2022. URL: https://doi.org/10.1021/acs.chemrestox.2c00182, doi:10.1021/acs.chemrestox.2c00182. This article has 46 citations and is from a domain leading peer-reviewed journal.

2. (trezza2024molecularandevolution pages 1-2): Alfonso Trezza, Ancuta Birgauan, Michela Geminiani, Anna Visibelli, and Annalisa Santucci. Molecular and evolution in silico studies unlock the h4-hppd c-terminal tail gating mechanism. Biomedicines, 12:1196, May 2024. URL: https://doi.org/10.3390/biomedicines12061196, doi:10.3390/biomedicines12061196. This article has 4 citations.

3. (farrera2022thehumanglyoxalase pages 1-3): Dominique O. Farrera and James J. Galligan. The human glyoxalase gene family in health and disease. Chemical research in toxicology, 35:1766-1776, Sep 2022. URL: https://doi.org/10.1021/acs.chemrestox.2c00182, doi:10.1021/acs.chemrestox.2c00182. This article has 46 citations and is from a domain leading peer-reviewed journal.

4. (farrera2022thehumanglyoxalase pages 18-25): Dominique O. Farrera and James J. Galligan. The human glyoxalase gene family in health and disease. Chemical research in toxicology, 35:1766-1776, Sep 2022. URL: https://doi.org/10.1021/acs.chemrestox.2c00182, doi:10.1021/acs.chemrestox.2c00182. This article has 46 citations and is from a domain leading peer-reviewed journal.

5. (farrera2022thehumanglyoxalase pages 8-10): Dominique O. Farrera and James J. Galligan. The human glyoxalase gene family in health and disease. Chemical research in toxicology, 35:1766-1776, Sep 2022. URL: https://doi.org/10.1021/acs.chemrestox.2c00182, doi:10.1021/acs.chemrestox.2c00182. This article has 46 citations and is from a domain leading peer-reviewed journal.

6. (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 1-2): Annalisa Santucci, Giulia Bernardini, Daniela Braconi, Elena Petricci, and Fabrizio Manetti. 4-hydroxyphenylpyruvate dioxygenase and its inhibition in plants and animals: small molecules as herbicides and agents for the treatment of human inherited diseases. Journal of medicinal chemistry, 60 10:4101-4125, Feb 2017. URL: https://doi.org/10.1021/acs.jmedchem.6b01395, doi:10.1021/acs.jmedchem.6b01395. This article has 117 citations and is from a highest quality peer-reviewed journal.

7. (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 2-3): Annalisa Santucci, Giulia Bernardini, Daniela Braconi, Elena Petricci, and Fabrizio Manetti. 4-hydroxyphenylpyruvate dioxygenase and its inhibition in plants and animals: small molecules as herbicides and agents for the treatment of human inherited diseases. Journal of medicinal chemistry, 60 10:4101-4125, Feb 2017. URL: https://doi.org/10.1021/acs.jmedchem.6b01395, doi:10.1021/acs.jmedchem.6b01395. This article has 117 citations and is from a highest quality peer-reviewed journal.

8. (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 7-8): Annalisa Santucci, Giulia Bernardini, Daniela Braconi, Elena Petricci, and Fabrizio Manetti. 4-hydroxyphenylpyruvate dioxygenase and its inhibition in plants and animals: small molecules as herbicides and agents for the treatment of human inherited diseases. Journal of medicinal chemistry, 60 10:4101-4125, Feb 2017. URL: https://doi.org/10.1021/acs.jmedchem.6b01395, doi:10.1021/acs.jmedchem.6b01395. This article has 117 citations and is from a highest quality peer-reviewed journal.

9. (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 1-2): Michele Gunsior, Jacques Ravel, Gregory L. Challis, and Craig A. Townsend. Engineering p-hydroxyphenylpyruvate dioxygenase to a p-hydroxymandelate synthase and evidence for the proposed benzene oxide intermediate in homogentisate formation. Biochemistry, 43 3:663-74, Jan 2004. URL: https://doi.org/10.1021/bi035762w, doi:10.1021/bi035762w. This article has 102 citations and is from a peer-reviewed journal.

10. (santucci20174hydroxyphenylpyruvatedioxygenaseand pages 6-7): Annalisa Santucci, Giulia Bernardini, Daniela Braconi, Elena Petricci, and Fabrizio Manetti. 4-hydroxyphenylpyruvate dioxygenase and its inhibition in plants and animals: small molecules as herbicides and agents for the treatment of human inherited diseases. Journal of medicinal chemistry, 60 10:4101-4125, Feb 2017. URL: https://doi.org/10.1021/acs.jmedchem.6b01395, doi:10.1021/acs.jmedchem.6b01395. This article has 117 citations and is from a highest quality peer-reviewed journal.

11. (wilson2021expressionoftyrosine pages 6-7): Peter J. M. Wilson, Lakshminarayan R. Ranganath, George Bou‐Gharios, James A. Gallagher, and Juliette H. Hughes. Expression of tyrosine pathway enzymes in mice demonstrates that homogentisate 1,2‐dioxygenase deficiency in the liver is responsible for homogentisic acid‐derived ochronotic pigmentation. JIMD Reports, 58:52-60, Nov 2021. URL: https://doi.org/10.1002/jmd2.12184, doi:10.1002/jmd2.12184. This article has 10 citations and is from a peer-reviewed journal.

12. (trezza2024molecularandevolution pages 4-6): Alfonso Trezza, Ancuta Birgauan, Michela Geminiani, Anna Visibelli, and Annalisa Santucci. Molecular and evolution in silico studies unlock the h4-hppd c-terminal tail gating mechanism. Biomedicines, 12:1196, May 2024. URL: https://doi.org/10.3390/biomedicines12061196, doi:10.3390/biomedicines12061196. This article has 4 citations.

13. (neuckermans2019arobustbacterial pages 1-2): Jessie Neuckermans, Alan Mertens, Dinja De Win, Ulrich Schwaneberg, and Joery De Kock. A robust bacterial assay for high-throughput screening of human 4-hydroxyphenylpyruvate dioxygenase inhibitors. Scientific Reports, Oct 2019. URL: https://doi.org/10.1038/s41598-019-50533-1, doi:10.1038/s41598-019-50533-1. This article has 32 citations and is from a peer-reviewed journal.

14. (alsharhan2020disordersofphenylalanine pages 31-33): Hind Alsharhan and Can Ficicioglu. Disorders of phenylalanine and tyrosine metabolism. Translational Science of Rare Diseases, 5:3-58, Jul 2020. URL: https://doi.org/10.3233/trd-200049, doi:10.3233/trd-200049. This article has 41 citations.

15. (holme2013tyrosinemetabolism pages 2-4): Elisabeth Holme and Grant A. Mitchell. Tyrosine metabolism. Physician's Guide to the Diagnosis, Treatment, and Follow-Up of Inherited Metabolic Diseases, pages 23-31, Jan 2013. URL: https://doi.org/10.1007/978-3-642-40337-8\_2, doi:10.1007/978-3-642-40337-8\_2. This article has 18 citations.

16. (bernardini2025acomprehensivein pages 82-84): Giulia Bernardini, Alfonso Trezza, Elena Petricci, Giulia Romagnoli, Demetra Zambardino, Fabrizio Manetti, Daniela Braconi, Michela Geminiani, and Annalisa Santucci. A comprehensive in vitro and in silico approach for targeting 4-hydroxyphenyl pyruvate dioxygenase: towards new therapeutics for alkaptonuria. International Journal of Molecular Sciences, 26:3181, Mar 2025. URL: https://doi.org/10.3390/ijms26073181, doi:10.3390/ijms26073181. This article has 0 citations.

17. (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 7-9): Michele Gunsior, Jacques Ravel, Gregory L. Challis, and Craig A. Townsend. Engineering p-hydroxyphenylpyruvate dioxygenase to a p-hydroxymandelate synthase and evidence for the proposed benzene oxide intermediate in homogentisate formation. Biochemistry, 43 3:663-74, Jan 2004. URL: https://doi.org/10.1021/bi035762w, doi:10.1021/bi035762w. This article has 102 citations and is from a peer-reviewed journal.

18. (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 10-11): Michele Gunsior, Jacques Ravel, Gregory L. Challis, and Craig A. Townsend. Engineering p-hydroxyphenylpyruvate dioxygenase to a p-hydroxymandelate synthase and evidence for the proposed benzene oxide intermediate in homogentisate formation. Biochemistry, 43 3:663-74, Jan 2004. URL: https://doi.org/10.1021/bi035762w, doi:10.1021/bi035762w. This article has 102 citations and is from a peer-reviewed journal.

19. (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 9-10): Michele Gunsior, Jacques Ravel, Gregory L. Challis, and Craig A. Townsend. Engineering p-hydroxyphenylpyruvate dioxygenase to a p-hydroxymandelate synthase and evidence for the proposed benzene oxide intermediate in homogentisate formation. Biochemistry, 43 3:663-74, Jan 2004. URL: https://doi.org/10.1021/bi035762w, doi:10.1021/bi035762w. This article has 102 citations and is from a peer-reviewed journal.

20. (gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 4-5): Michele Gunsior, Jacques Ravel, Gregory L. Challis, and Craig A. Townsend. Engineering p-hydroxyphenylpyruvate dioxygenase to a p-hydroxymandelate synthase and evidence for the proposed benzene oxide intermediate in homogentisate formation. Biochemistry, 43 3:663-74, Jan 2004. URL: https://doi.org/10.1021/bi035762w, doi:10.1021/bi035762w. This article has 102 citations and is from a peer-reviewed journal.

21. (trezza2024molecularandevolution pages 8-10): Alfonso Trezza, Ancuta Birgauan, Michela Geminiani, Anna Visibelli, and Annalisa Santucci. Molecular and evolution in silico studies unlock the h4-hppd c-terminal tail gating mechanism. Biomedicines, 12:1196, May 2024. URL: https://doi.org/10.3390/biomedicines12061196, doi:10.3390/biomedicines12061196. This article has 4 citations.

22. (trezza2024molecularandevolution pages 6-8): Alfonso Trezza, Ancuta Birgauan, Michela Geminiani, Anna Visibelli, and Annalisa Santucci. Molecular and evolution in silico studies unlock the h4-hppd c-terminal tail gating mechanism. Biomedicines, 12:1196, May 2024. URL: https://doi.org/10.3390/biomedicines12061196, doi:10.3390/biomedicines12061196. This article has 4 citations.

23. (trezza2024molecularandevolution pages 2-4): Alfonso Trezza, Ancuta Birgauan, Michela Geminiani, Anna Visibelli, and Annalisa Santucci. Molecular and evolution in silico studies unlock the h4-hppd c-terminal tail gating mechanism. Biomedicines, 12:1196, May 2024. URL: https://doi.org/10.3390/biomedicines12061196, doi:10.3390/biomedicines12061196. This article has 4 citations.

24. (trezza2024molecularandevolution pages 10-12): Alfonso Trezza, Ancuta Birgauan, Michela Geminiani, Anna Visibelli, and Annalisa Santucci. Molecular and evolution in silico studies unlock the h4-hppd c-terminal tail gating mechanism. Biomedicines, 12:1196, May 2024. URL: https://doi.org/10.3390/biomedicines12061196, doi:10.3390/biomedicines12061196. This article has 4 citations.

25. (wilson2021expressionoftyrosine pages 1-3): Peter J. M. Wilson, Lakshminarayan R. Ranganath, George Bou‐Gharios, James A. Gallagher, and Juliette H. Hughes. Expression of tyrosine pathway enzymes in mice demonstrates that homogentisate 1,2‐dioxygenase deficiency in the liver is responsible for homogentisic acid‐derived ochronotic pigmentation. JIMD Reports, 58:52-60, Nov 2021. URL: https://doi.org/10.1002/jmd2.12184, doi:10.1002/jmd2.12184. This article has 10 citations and is from a peer-reviewed journal.

26. (colemontsvroninks2020oxidativestressglutathione pages 1-2): Haaike Colemonts-Vroninks, Jessie Neuckermans, Lionel Marcelis, Paul Claes, Steven Branson, Georges Casimir, Philippe Goyens, Geert A. Martens, Tamara Vanhaecke, and Joery De Kock. Oxidative stress, glutathione metabolism, and liver regeneration pathways are activated in hereditary tyrosinemia type 1 mice upon short-term nitisinone discontinuation. Genes, 12:3, Dec 2020. URL: https://doi.org/10.3390/genes12010003, doi:10.3390/genes12010003. This article has 17 citations.

27. (alsharhan2020disordersofphenylalanine pages 23-26): Hind Alsharhan and Can Ficicioglu. Disorders of phenylalanine and tyrosine metabolism. Translational Science of Rare Diseases, 5:3-58, Jul 2020. URL: https://doi.org/10.3233/trd-200049, doi:10.3233/trd-200049. This article has 41 citations.

28. (scott2006thegenetictyrosinemias pages 5-6): C. Ronald Scott. The genetic tyrosinemias. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 142C:121-126, May 2006. URL: https://doi.org/10.1002/ajmg.c.30092, doi:10.1002/ajmg.c.30092. This article has 256 citations.

29. (holme2013tyrosinemetabolism pages 8-9): Elisabeth Holme and Grant A. Mitchell. Tyrosine metabolism. Physician's Guide to the Diagnosis, Treatment, and Follow-Up of Inherited Metabolic Diseases, pages 23-31, Jan 2013. URL: https://doi.org/10.1007/978-3-642-40337-8\_2, doi:10.1007/978-3-642-40337-8\_2. This article has 18 citations.

30. (scott2006thegenetictyrosinemias pages 2-3): C. Ronald Scott. The genetic tyrosinemias. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 142C:121-126, May 2006. URL: https://doi.org/10.1002/ajmg.c.30092, doi:10.1002/ajmg.c.30092. This article has 256 citations.

31. (holme2013tyrosinemetabolism pages 7-8): Elisabeth Holme and Grant A. Mitchell. Tyrosine metabolism. Physician's Guide to the Diagnosis, Treatment, and Follow-Up of Inherited Metabolic Diseases, pages 23-31, Jan 2013. URL: https://doi.org/10.1007/978-3-642-40337-8\_2, doi:10.1007/978-3-642-40337-8\_2. This article has 18 citations.

32. (bernardini2025acomprehensivein pages 6-9): Giulia Bernardini, Alfonso Trezza, Elena Petricci, Giulia Romagnoli, Demetra Zambardino, Fabrizio Manetti, Daniela Braconi, Michela Geminiani, and Annalisa Santucci. A comprehensive in vitro and in silico approach for targeting 4-hydroxyphenyl pyruvate dioxygenase: towards new therapeutics for alkaptonuria. International Journal of Molecular Sciences, 26:3181, Mar 2025. URL: https://doi.org/10.3390/ijms26073181, doi:10.3390/ijms26073181. This article has 0 citations.

33. (shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 2-4): Changliang Shan, Zhaoliang Lu, Zhen Li, Hao Sheng, Jun Fan, Qi Qi, Shuangping Liu, and Shuai Zhang. 4-hydroxyphenylpyruvate dioxygenase promotes lung cancer growth via pentose phosphate pathway (ppp) flux mediated by lkb1-ampk/hdac10/g6pd axis. Cell Death &amp; Disease, Jul 2019. URL: https://doi.org/10.1038/s41419-019-1756-1, doi:10.1038/s41419-019-1756-1. This article has 80 citations and is from a peer-reviewed journal.

34. (shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 1-2): Changliang Shan, Zhaoliang Lu, Zhen Li, Hao Sheng, Jun Fan, Qi Qi, Shuangping Liu, and Shuai Zhang. 4-hydroxyphenylpyruvate dioxygenase promotes lung cancer growth via pentose phosphate pathway (ppp) flux mediated by lkb1-ampk/hdac10/g6pd axis. Cell Death &amp; Disease, Jul 2019. URL: https://doi.org/10.1038/s41419-019-1756-1, doi:10.1038/s41419-019-1756-1. This article has 80 citations and is from a peer-reviewed journal.

35. (shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 7-10): Changliang Shan, Zhaoliang Lu, Zhen Li, Hao Sheng, Jun Fan, Qi Qi, Shuangping Liu, and Shuai Zhang. 4-hydroxyphenylpyruvate dioxygenase promotes lung cancer growth via pentose phosphate pathway (ppp) flux mediated by lkb1-ampk/hdac10/g6pd axis. Cell Death &amp; Disease, Jul 2019. URL: https://doi.org/10.1038/s41419-019-1756-1, doi:10.1038/s41419-019-1756-1. This article has 80 citations and is from a peer-reviewed journal.

36. (shan20194hydroxyphenylpyruvatedioxygenasepromotes pages 4-7): Changliang Shan, Zhaoliang Lu, Zhen Li, Hao Sheng, Jun Fan, Qi Qi, Shuangping Liu, and Shuai Zhang. 4-hydroxyphenylpyruvate dioxygenase promotes lung cancer growth via pentose phosphate pathway (ppp) flux mediated by lkb1-ampk/hdac10/g6pd axis. Cell Death &amp; Disease, Jul 2019. URL: https://doi.org/10.1038/s41419-019-1756-1, doi:10.1038/s41419-019-1756-1. This article has 80 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](HPD-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](HPD-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. farrera2022thehumanglyoxalase pages 7-8
2. farrera2022thehumanglyoxalase pages 8-10
3. trezza2024molecularandevolution pages 1-2
4. gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 7-9
5. gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 1-2
6. gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 9-10
7. trezza2024molecularandevolution pages 8-10
8. trezza2024molecularandevolution pages 10-12
9. farrera2022thehumanglyoxalase pages 18-25
10. alsharhan2020disordersofphenylalanine pages 31-33
11. neuckermans2019arobustbacterial pages 1-2
12. scott2006thegenetictyrosinemias pages 5-6
13. holme2013tyrosinemetabolism pages 2-4
14. scott2006thegenetictyrosinemias pages 2-3
15. farrera2022thehumanglyoxalase pages 1-3
16. wilson2021expressionoftyrosine pages 6-7
17. trezza2024molecularandevolution pages 4-6
18. bernardini2025acomprehensivein pages 82-84
19. gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 10-11
20. gunsior2004engineeringphydroxyphenylpyruvatedioxygenase pages 4-5
21. trezza2024molecularandevolution pages 6-8
22. trezza2024molecularandevolution pages 2-4
23. wilson2021expressionoftyrosine pages 1-3
24. colemontsvroninks2020oxidativestressglutathione pages 1-2
25. alsharhan2020disordersofphenylalanine pages 23-26
26. holme2013tyrosinemetabolism pages 8-9
27. holme2013tyrosinemetabolism pages 7-8
28. bernardini2025acomprehensivein pages 6-9
29. https://doi.org/10.1021/acs.chemrestox.2c00182,
30. https://doi.org/10.3390/biomedicines12061196,
31. https://doi.org/10.1021/acs.jmedchem.6b01395,
32. https://doi.org/10.1021/bi035762w,
33. https://doi.org/10.1002/jmd2.12184,
34. https://doi.org/10.1038/s41598-019-50533-1,
35. https://doi.org/10.3233/trd-200049,
36. https://doi.org/10.1007/978-3-642-40337-8\_2,
37. https://doi.org/10.3390/ijms26073181,
38. https://doi.org/10.3390/genes12010003,
39. https://doi.org/10.1002/ajmg.c.30092,
40. https://doi.org/10.1038/s41419-019-1756-1,