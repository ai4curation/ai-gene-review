---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T17:54:08.065994'
end_time: '2026-07-05T18:09:12.568474'
duration_seconds: 904.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: HGD
  gene_symbol: HGD
  uniprot_accession: Q93099
  protein_description: 'RecName: Full=Homogentisate 1,2-dioxygenase; EC=1.13.11.5
    {ECO:0000269|PubMed:8782815}; AltName: Full=Homogentisate oxygenase; AltName:
    Full=Homogentisic acid oxidase; AltName: Full=Homogentisicase;'
  gene_info: Name=HGD; Synonyms=HGO;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the homogentisate dioxygenase family.
  protein_domains: HgmA_C. (IPR046451); HgmA_N. (IPR046452); Homogentis_dOase. (IPR005708);
    RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf. (IPR011051)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: HGD-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: HGD-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q93099
- **Protein Description:** RecName: Full=Homogentisate 1,2-dioxygenase; EC=1.13.11.5 {ECO:0000269|PubMed:8782815}; AltName: Full=Homogentisate oxygenase; AltName: Full=Homogentisic acid oxidase; AltName: Full=Homogentisicase;
- **Gene Information:** Name=HGD; Synonyms=HGO;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the homogentisate dioxygenase family.
- **Key Domains:** HgmA_C. (IPR046451); HgmA_N. (IPR046452); Homogentis_dOase. (IPR005708); RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf. (IPR011051)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HGD" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HGD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HGD** (gene ID: HGD, UniProt: Q93099) in human.

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
- **UniProt Accession:** Q93099
- **Protein Description:** RecName: Full=Homogentisate 1,2-dioxygenase; EC=1.13.11.5 {ECO:0000269|PubMed:8782815}; AltName: Full=Homogentisate oxygenase; AltName: Full=Homogentisic acid oxidase; AltName: Full=Homogentisicase;
- **Gene Information:** Name=HGD; Synonyms=HGO;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the homogentisate dioxygenase family.
- **Key Domains:** HgmA_C. (IPR046451); HgmA_N. (IPR046452); Homogentis_dOase. (IPR005708); RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf. (IPR011051)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HGD" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HGD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HGD** (gene ID: HGD, UniProt: Q93099) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: HGD (Homogentisate 1,2-Dioxygenase) — Human Gene (UniProt Q93099)

## 1. Gene and Protein Identity

The human *HGD* gene (synonym: *HGO*) encodes homogentisate 1,2-dioxygenase (EC 1.13.11.5), also known as homogentisic acid oxidase or homogentisicase. The gene is located on chromosome 3q21-q23 and produces a 445-amino acid protein with a molecular weight of approximately 49,973 Da (vilboux2009mutationspectrumof pages 1-2, vijukumar2025acenturyof pages 13-17). HGD belongs to the homogentisate dioxygenase protein family and contains several characteristic domains including HgmA_C, HgmA_N, Homogentis_dOase, and the RmlC-like jellyroll/cupin superfold (OpenTargets Search: -HGD). The key properties of HGD are summarized below:

| Property | Value | Evidence |
|---|---|---|
| Gene name | **HGD** (synonym: **HGO**) | (OpenTargets Search: -HGD) |
| UniProt ID | **Q93099** | (OpenTargets Search: -HGD) |
| Recommended protein name | **Homogentisate 1,2-dioxygenase** | (OpenTargets Search: -HGD) |
| EC number | **1.13.11.5** | (OpenTargets Search: -HGD) |
| Protein family | **Homogentisate dioxygenase family** | (OpenTargets Search: -HGD) |
| Key domains | **HgmA_C, HgmA_N, Homogentis_dOase, RmlC-like_jellyroll, RmlC_Cupin_sf** | (OpenTargets Search: -HGD) |
| Amino-acid length | **445 aa** | (OpenTargets Search: -HGD, vilboux2009mutationspectrumof pages 1-2) |
| Molecular weight | **49,973 Da** | (vilboux2009mutationspectrumof pages 1-2) |
| Chromosomal location | **3q21-q23** | (vijukumar2025acenturyof pages 13-17, vijukumar2025acenturyof pages 10-13) |
| Quaternary structure | **Functional hexamer**, organized as a **dimer of trimers** | (vilboux2009mutationspectrumof pages 1-2) |
| Cofactor | **Fe(II)** non-heme iron | (traore2022chargemaintenanceduring pages 3-5, traore2022chargemaintenanceduring pages 26-38) |
| Active-site metal ligands | **His335, Glu341, His371** | (vilboux2009mutationspectrumof pages 1-2) |
| Primary substrate | **Homogentisate (homogentisic acid)** | (traore2022chargemaintenanceduring pages 3-5, milella2024alkaptonuriafrommolecular pages 2-4) |
| Reaction catalyzed | Oxidative ring cleavage of homogentisate with incorporation of molecular oxygen | (traore2022chargemaintenanceduring pages 3-5, traore2022chargemaintenanceduring pages 26-38) |
| Product | **Maleylacetoacetate** (also written **4-maleylacetoacetate**) | (traore2022chargemaintenanceduring pages 3-5, milella2024alkaptonuriafrommolecular pages 2-4, holme2013tyrosinemetabolism pages 2-4) |
| Pathway role | Enzyme in **phenylalanine/tyrosine catabolism**; acts downstream of **4-hydroxyphenylpyruvate dioxygenase (HPPD)** and upstream of maleylacetoacetate isomerization | (milella2024alkaptonuriafrommolecular pages 2-4, holme2013tyrosinemetabolism pages 2-4, holme2013tyrosinemetabolism pages 1-2) |
| Primary tissue expression | Mainly **liver** and **kidney** | (milella2024alkaptonuriafrommolecular pages 2-4, zatkova2020alkaptonuriacurrentperspectives pages 4-6) |
| Additional reported tissue expression | Prostate, small intestine, colon, chondrocytes, synoviocytes, osteoblasts, brain | (zatkova2020alkaptonuriacurrentperspectives pages 4-6) |
| Subcellular localization | **Cytoplasm / cytosol** | (milella2024alkaptonuriafrommolecular pages 2-4, zatkova2020alkaptonuriacurrentperspectives pages 4-6) |
| Disease association | **Alkaptonuria (AKU)** caused by HGD deficiency or pathogenic variants | (vilboux2009mutationspectrumof pages 1-2, milella2024alkaptonuriafrommolecular pages 2-4, zatkova2020alkaptonuriacurrentperspectives pages 4-6) |
| Mutation burden in disease | **212+ variants** reported by 2020; predominantly missense | (milella2024alkaptonuriafrommolecular pages 2-4, zatkova2020alkaptonuriacurrentperspectives pages 4-6) |


*Table: This table summarizes the core molecular, structural, biochemical, localization, and disease-related properties of human HGD/Homogentisate 1,2-dioxygenase. It is useful as a compact reference for the gene’s canonical function and medically relevant annotations.*

## 2. Enzymatic Reaction and Catalytic Mechanism

### 2.1 Reaction Catalyzed

HGD catalyzes the oxidative ring cleavage of homogentisate (2,5-dihydroxyphenylacetate, also called homogentisic acid) with the incorporation of molecular oxygen (O₂) to produce maleylacetoacetate (4-maleylacetoacetate) (traore2022chargemaintenanceduring pages 3-5, milella2024alkaptonuriafrommolecular pages 2-4). This reaction represents an essential step in the catabolism of the aromatic amino acids phenylalanine and tyrosine, converting an aromatic substrate into a linear dicarboxylic acid that can be further metabolized to fumarate and acetoacetate.

### 2.2 Iron Cofactor and Active Site

HGD is a nonheme Fe(II)-dependent dioxygenase. The active site iron is coordinated by two histidine residues (His335 and His371) and one glutamate residue (Glu341), together with a water molecule, forming a distorted square pyramidal coordination geometry (traore2022chargemaintenanceduring pages 3-5, vilboux2009mutationspectrumof pages 1-2). This iron coordination motif is critical for the enzyme's ability to activate molecular oxygen.

### 2.3 Catalytic Mechanism

Detailed mechanistic studies of HGD and related nonheme iron dioxygenases have elucidated the catalytic cycle. The substrate homogentisate binds to the Fe(II) center in a monodentate monoanionic fashion, with the ionized hydroxyl group interacting with the iron ion (traore2022chargemaintenanceduring pages 3-5, traore2022chargemaintenanceduring pages 5-6). The catalytic mechanism then proceeds through: (i) binding and activation of O₂ via electron transfer from Fe(II) to form an Fe(III)-superoxide intermediate; (ii) electron transfer from the aromatic substrate to the Fe(III) center, generating an Fe(II) species and a substrate semiquinone radical; (iii) formation of an alkylperoxo intermediate; and (iv) sequential oxygen atom insertion into the aromatic ring to yield the ring-opened product maleylacetoacetate (traore2022chargemaintenanceduring pages 3-5, traore2022chargemaintenanceduring pages 5-6). Charge maintenance at the iron center throughout the catalytic cycle — tuned by both the protein-derived carboxylate ligand and the substrate — is crucial for promoting each catalytic step (traore2022chargemaintenanceduring pages 26-38, traore2022chargemaintenanceduring pages 5-6).

### 2.4 Quaternary Structure

The crystal structure of human HGD reveals that the functional enzyme is a hexamer organized as a dimer of trimers (vilboux2009mutationspectrumof pages 1-2). Each protomer contains an active site with the Fe(II) cofactor. The hexameric assembly is essential for full catalytic activity, and disease-causing mutations can disrupt protomer interactions, folding, stability, or substrate binding (zatkova2020alkaptonuriacurrentperspectives pages 4-6).

## 3. Biochemical Pathway Context

HGD occupies a central position in the phenylalanine/tyrosine catabolic pathway. The complete degradation pathway consists of six enzymatic steps, with HGD catalyzing the fourth step:

| Step | Enzyme name | EC number | Substrate | Product | Associated disease when deficient |
|---|---|---|---|---|---|
| 1 | Phenylalanine hydroxylase (PAH) | EC 1.14.16.1 | L-Phenylalanine | L-Tyrosine | Phenylketonuria (PKU) |
| 2 | Tyrosine aminotransferase (TAT) | EC 2.6.1.5 | L-Tyrosine | 4-Hydroxyphenylpyruvate | Tyrosinemia type II |
| 3 | 4-Hydroxyphenylpyruvate dioxygenase (HPPD/HPD) | EC 1.13.11.27 | 4-Hydroxyphenylpyruvate | Homogentisate | Hawkinsinuria / Tyrosinemia type III; inhibited pharmacologically by nitisinone (NTBC) (milella2024alkaptonuriafrommolecular pages 2-4, holme2013tyrosinemetabolism pages 2-4, holme2013tyrosinemetabolism pages 1-2) |
| 4 | Homogentisate 1,2-dioxygenase (HGD) | EC 1.13.11.5 | Homogentisate | Maleylacetoacetate | Alkaptonuria (traore2022chargemaintenanceduring pages 3-5, milella2024alkaptonuriafrommolecular pages 2-4, vilboux2009mutationspectrumof pages 1-2) |
| 5 | Maleylacetoacetate isomerase (MAAI/GSTZ1) | EC 5.2.1.2 | Maleylacetoacetate | Fumarylacetoacetate | Maleylacetoacetate isomerase deficiency (rare); pathway context in tyrosine catabolism (milella2024alkaptonuriafrommolecular pages 2-4) |
| 6 | Fumarylacetoacetate hydrolase (FAH) | EC 3.7.1.2 | Fumarylacetoacetate | Fumarate + Acetoacetate | Tyrosinemia type I (milella2024alkaptonuriafrommolecular pages 2-4) |


*Table: This table summarizes the canonical tyrosine degradation pathway, highlighting where HGD acts and where nitisinone blocks the upstream HPPD step. It is useful for placing HGD within its metabolic context and linking each step to the major inborn error associated with enzyme deficiency.*

The upstream enzyme 4-hydroxyphenylpyruvate dioxygenase (HPPD; EC 1.13.11.27) converts 4-hydroxyphenylpyruvate to homogentisate, which serves as the direct substrate for HGD (milella2024alkaptonuriafrommolecular pages 2-4, holme2013tyrosinemetabolism pages 2-4). The product maleylacetoacetate is subsequently isomerized by maleylacetoacetate isomerase (MAAI/GSTZ1) to fumarylacetoacetate, which is then hydrolyzed by fumarylacetoacetate hydrolase (FAH) to fumarate and acetoacetate — metabolites that feed into the citric acid cycle and ketone body metabolism, respectively (milella2024alkaptonuriafrommolecular pages 2-4, holme2013tyrosinemetabolism pages 2-4, holme2013tyrosinemetabolism pages 1-2). Inherited defects have been identified at four of the five enzymatic steps of this pathway, and each step is associated with a distinct inborn error of metabolism (holme2013tyrosinemetabolism pages 1-2). The therapeutic agent nitisinone (NTBC), used to treat both tyrosinemia type I and alkaptonuria, acts by inhibiting the upstream enzyme HPPD, thereby blocking homogentisate production (milella2024alkaptonuriafrommolecular pages 2-4, holme2013tyrosinemetabolism pages 1-2).

## 4. Tissue Distribution and Subcellular Localization

### 4.1 Tissue Expression

HGD is predominantly expressed in the liver and kidneys, with mouse model studies confirming expression specifically in the kidney cortex (milella2024alkaptonuriafrommolecular pages 2-4, zatkova2020alkaptonuriacurrentperspectives pages 4-6). Beyond these primary sites, HGD expression has also been detected in prostate, small intestine, colon, chondrocytes, synoviocytes, osteoblasts, and brain (zatkova2020alkaptonuriacurrentperspectives pages 4-6). The liver and kidney represent the major sites of tyrosine catabolism, and accordingly harbor the highest levels of HGD activity.

### 4.2 Subcellular Localization

HGD functions as a cytosolic enzyme. The tyrosine catabolism pathway operates in the cytoplasm, and HGD, like the other enzymes in this catabolic sequence, is localized to the cytoplasmic compartment (milella2024alkaptonuriafrommolecular pages 2-4, zatkova2020alkaptonuriacurrentperspectives pages 4-6).

## 5. Disease Association: Alkaptonuria

### 5.1 Pathophysiology

Deficiency of HGD activity causes alkaptonuria (AKU; OMIM 203500), an autosomal recessive inborn error of metabolism first described in 1584 and later used by Sir Archibald Garrod in 1902 to illustrate the concept of Mendelian inheritance in humans (vilboux2009mutationspectrumof pages 1-2, vilboux2009mutationspectrumof pages 7-8). The global incidence is estimated at 1 in 250,000 to 1,000,000 live births (vilboux2009mutationspectrumof pages 1-2). When HGD activity is absent or severely deficient (requiring loss of >99% of enzyme activity for clinical manifestation), homogentisic acid accumulates in body fluids and tissues (vilboux2009mutationspectrumof pages 1-2, vilboux2009mutationspectrumof pages 7-8).

### 5.2 Clinical Manifestations

The earliest and most characteristic sign of AKU is darkened urine, resulting from HGA oxidation, observable from birth (abdelkhalek2023homogentisate12dioxygenase(hgd) pages 3-5, vilboux2009mutationspectrumof pages 2-3). The accumulated HGA undergoes auto-oxidation via semiquinone radical intermediates, producing a melanin-like ochronotic pigment through oxidative coupling mechanisms involving phenolic ether and biphenyl linkages (grasso2025ochronoticdepositionin pages 5-7, grasso2025ochronoticdepositionin pages 1-2). This pigment deposits in connective tissues, particularly cartilage, tendons, and sclera — a process known as ochronosis (milella2024alkaptonuriafrommolecular pages 2-4, milella2024alkaptonuriafrommolecular pages 4-6).

Progressive clinical complications include: (i) ochronotic arthropathy with cartilage degradation, joint pain, and early-onset osteoarthritis, often requiring surgical joint replacement of knees, hips, and shoulders; (ii) spinal degeneration with intervertebral disc calcification; (iii) cardiovascular involvement, notably aortic valve thickening and calcification, with 100% of patients over 65 years showing aortic stenosis; and (iv) renal and prostatic stones (milella2024alkaptonuriafrommolecular pages 2-4, vilboux2009mutationspectrumof pages 2-3).

### 5.3 Mutational Landscape

As of recent analyses, more than 200 different disease-associated HGD variants have been reported in the HGD Mutation Database from approximately 530+ AKU patients worldwide (milella2024alkaptonuriafrommolecular pages 2-4, zatkova2020alkaptonuriacurrentperspectives pages 4-6). These include approximately 65% missense variants, 14% splicing variants, 11% frameshift variants, 5% genomic deletions, and 4% nonsense variants. Mutations are distributed across all 14 exons but cluster preferentially in exons 3, 6, 8, and 13 (vilboux2009mutationspectrumof pages 1-2, zatkova2020alkaptonuriacurrentperspectives pages 4-6). Four highly recurrent mutations include p.M368V, p.G161R, c.174delA, and p.C120F (vilboux2009mutationspectrumof pages 7-8). Despite this extensive mutational burden, clear genotype-phenotype correlations have not been established (milella2024alkaptonuriafrommolecular pages 2-4). Recent work has continued to expand this catalogue, including a 2023 study identifying the first HGD variants in Egyptian patients, including a novel variant c.1079G>T (p.Gly360Val) (abdelkhalek2023homogentisate12dioxygenase(hgd) pages 3-5).

## 6. Therapeutic Developments

### 6.1 Nitisinone (NTBC) and the SONIA 2 Trial

The landmark SONIA 2 (Suitability of Nitisinone in Alkaptonuria 2) clinical trial was an international, multicenter, randomized, evaluator-blinded, no-treatment controlled trial enrolling 138 AKU patients aged ≥25 years, with a 12-month evaluation period followed by an additional 36-month treatment period (bernardini2025acomprehensivein pages 18-23, vijukumar2025acenturyof pages 6-10). The primary endpoint demonstrated that nitisinone reduced urinary homogentisic acid excretion by 99.7% compared to controls (85.7 μmol/L in the nitisinone group versus 26,027.9 μmol/L in untreated controls at 12 months) (vijukumar2025acenturyof pages 6-10, bernardini2025acomprehensivein pages 82-84). Over 48 months, nitisinone significantly slowed disease progression as measured by the AKU Severity Score Index (AKUSSI) (vijukumar2025acenturyof pages 6-10, vijukumar2025acenturyof pages 13-17). Based on these results, the European Medicines Agency (EMA) approved nitisinone (Orfadin) in September 2020 as the first disease-modifying treatment for adult patients with alkaptonuria (vijukumar2025acenturyof pages 13-17). Side effects include iatrogenic hypertyrosinemia with potential corneal keratopathy, managed through dietary protein restriction and monitoring (zatkova2020alkaptonuriacurrentperspectives pages 3-4). Research into safer second-generation HPPD inhibitors is ongoing (bernardini2025acomprehensivein pages 18-23).

### 6.2 Emerging Therapies

Enzyme replacement and gene therapy are being explored as future approaches for AKU, with a suitable mouse model available for preclinical testing (zatkova2020alkaptonuriacurrentperspectives pages 3-4). Studies on functional characterization of HGD variants using minigene splicing assays have been conducted to improve variant classification and support diagnosis, and to lay the foundation for future therapeutic strategies targeting splicing defects in AKU.

## 7. Non-Canonical ("Moonlighting") Function of HGD in Cancer

A recent and notable discovery has identified a moonlighting function for HGD beyond its canonical role in tyrosine catabolism. In small cell lung cancer (SCLC), HGD is highly upregulated under chemotherapeutic stress and catalyzes the oxidation of tryptophan to N-formylkynurenine (FK), bypassing the canonical tryptophan-degrading enzymes IDO1, IDO2, and TDO2, which are negligibly expressed in SCLC cells (shen2026hgdderivednformylkynureninepromotes pages 1-7, shen2026hgdderivednformylkynureninepromotes pages 20-24, shen2026hgdderivednformylkynureninepromotes pages 11-16). This function is strictly dependent on HGD's dioxygenase catalytic activity, as demonstrated by the failure of catalytically inactive HGD mutants (R225H and I216T) to produce FK (shen2026hgdderivednformylkynureninepromotes pages 11-16). The HGD-generated FK directly binds to the ER-shaping protein ATL2 (Atlastin-2), triggering its oligomerization and subsequent endoplasmic reticulum membrane remodeling, which maintains ER homeostasis and promotes chemoresistance via enhanced autophagosome formation (shen2026hgdderivednformylkynureninepromotes pages 1-7, shen2026hgdderivednformylkynureninepromotes pages 16-20). A selective HGD inhibitor (iTrp-HCl) was identified that specifically blocks HGD-driven FK accumulation without affecting canonical IDO/TDO-mediated tryptophan metabolism in normal tissues, representing a potential therapeutic strategy to overcome SCLC chemoresistance (shen2026hgdderivednformylkynureninepromotes pages 20-24).

## 8. Ochronotic Pigment Formation: Molecular Insights

Recent structural and biophysical studies have advanced understanding of ochronotic pigment formation. HGA polymerizes slowly at physiological pH (91% signal loss over 10 weeks at pH 7.4, 35°C) but rapidly under alkaline conditions (grasso2025ochronoticdepositionin pages 2-5). The polymerization process involves semiquinone radical intermediates, as confirmed by EPR spectroscopy, consistent with an oxidative coupling mechanism (grasso2025ochronoticdepositionin pages 5-7). The resulting pigments are polydisperse polymers (11–50 kDa) with strong negative charges, containing phenolic ether and biphenyl linkages as revealed by solid-state NMR (grasso2025ochronoticdepositionin pages 1-2). The diphenol ring of HGA is essential for polymerization, as its removal completely abolishes the reaction, while modifications to the –CH₂COOH group do not affect reactivity (grasso2025ochronoticdepositionin pages 5-7). In connective tissues, loss of protective glycosaminoglycans (GAGs) unmasks collagen-binding sites for HGA and its byproducts, facilitating irreversible pigment accumulation that contributes to cartilage degradation and premature osteoarthropathy (milella2024alkaptonuriafrommolecular pages 4-6, vijukumar2025acenturyof pages 10-13).

## 9. Summary

Human HGD encodes a cytosolic, nonheme Fe(II)-dependent dioxygenase that catalyzes the oxidative ring cleavage of homogentisate to maleylacetoacetate in the phenylalanine/tyrosine catabolic pathway. The enzyme assembles as a hexamer (dimer of trimers) with iron coordinated by His335, Glu341, and His371 at each active site. HGD is predominantly expressed in liver and kidney and carries out its function in the cytoplasm. Deficiency of HGD causes alkaptonuria, a rare autosomal recessive disorder with over 200 known pathogenic variants, characterized by ochronosis, progressive arthropathy, and cardiovascular complications. The SONIA 2 trial demonstrated that nitisinone, an inhibitor of the upstream enzyme HPPD, reduces urinary HGA by 99.7% and significantly slows disease progression, leading to EMA approval in 2020. Emerging research has revealed a non-canonical moonlighting function for HGD in oxidizing tryptophan to N-formylkynurenine in SCLC, promoting chemotherapy resistance via ATL2-mediated ER remodeling — a finding that positions HGD as a potential therapeutic target in oncology.

References

1. (vilboux2009mutationspectrumof pages 1-2): Thierry Vilboux, Michael Kayser, Wendy Introne, Pim Suwannarat, Isa Bernardini, Roxanne Fischer, Kevin O'Brien, Robert Kleta, Marjan Huizing, and William A. Gahl. Mutation spectrum of homogentisic acid oxidase (hgd) in alkaptonuria. Human Mutation, 30:1611-1619, Dec 2009. URL: https://doi.org/10.1002/humu.21120, doi:10.1002/humu.21120. This article has 120 citations and is from a domain leading peer-reviewed journal.

2. (vijukumar2025acenturyof pages 13-17): Abhishek Vijukumar, Kamaljeet ., Harkomal Singh, Tarun Kalra, and Bintoo Sharma. A century of alkaptonuria: evolving insights into a rare metabolic disorder. GenoMed Connect, Dec 2025. URL: https://doi.org/10.69709/genomc.2025.122212, doi:10.69709/genomc.2025.122212. This article has 0 citations.

3. (OpenTargets Search: -HGD): Open Targets Query (-HGD, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (vijukumar2025acenturyof pages 10-13): Abhishek Vijukumar, Kamaljeet ., Harkomal Singh, Tarun Kalra, and Bintoo Sharma. A century of alkaptonuria: evolving insights into a rare metabolic disorder. GenoMed Connect, Dec 2025. URL: https://doi.org/10.69709/genomc.2025.122212, doi:10.69709/genomc.2025.122212. This article has 0 citations.

5. (traore2022chargemaintenanceduring pages 3-5): Ephrahime S. Traore and Aimin Liu. Charge maintenance during catalysis in nonheme iron oxygenases. ACS catalysis, 12 10:6191-6208, May 2022. URL: https://doi.org/10.1021/acscatal.1c04770, doi:10.1021/acscatal.1c04770. This article has 29 citations and is from a highest quality peer-reviewed journal.

6. (traore2022chargemaintenanceduring pages 26-38): Ephrahime S. Traore and Aimin Liu. Charge maintenance during catalysis in nonheme iron oxygenases. ACS catalysis, 12 10:6191-6208, May 2022. URL: https://doi.org/10.1021/acscatal.1c04770, doi:10.1021/acscatal.1c04770. This article has 29 citations and is from a highest quality peer-reviewed journal.

7. (milella2024alkaptonuriafrommolecular pages 2-4): Maria Serena Milella, Michela Geminiani, Alfonso Trezza, Anna Visibelli, Daniela Braconi, and Annalisa Santucci. Alkaptonuria: from molecular insights to a dedicated digital platform. Cells, 13:1072, Jun 2024. URL: https://doi.org/10.3390/cells13121072, doi:10.3390/cells13121072. This article has 13 citations.

8. (holme2013tyrosinemetabolism pages 2-4): Elisabeth Holme and Grant A. Mitchell. Tyrosine metabolism. Physician's Guide to the Diagnosis, Treatment, and Follow-Up of Inherited Metabolic Diseases, pages 23-31, Jan 2013. URL: https://doi.org/10.1007/978-3-642-40337-8\_2, doi:10.1007/978-3-642-40337-8\_2. This article has 18 citations.

9. (holme2013tyrosinemetabolism pages 1-2): Elisabeth Holme and Grant A. Mitchell. Tyrosine metabolism. Physician's Guide to the Diagnosis, Treatment, and Follow-Up of Inherited Metabolic Diseases, pages 23-31, Jan 2013. URL: https://doi.org/10.1007/978-3-642-40337-8\_2, doi:10.1007/978-3-642-40337-8\_2. This article has 18 citations.

10. (zatkova2020alkaptonuriacurrentperspectives pages 4-6): Andrea Zatkova, Lakshminarayan Ranganath, and Ludevit Kadasi. Alkaptonuria: current perspectives. The Application of Clinical Genetics, 13:37-47, Jan 2020. URL: https://doi.org/10.2147/tacg.s186773, doi:10.2147/tacg.s186773. This article has 93 citations.

11. (traore2022chargemaintenanceduring pages 5-6): Ephrahime S. Traore and Aimin Liu. Charge maintenance during catalysis in nonheme iron oxygenases. ACS catalysis, 12 10:6191-6208, May 2022. URL: https://doi.org/10.1021/acscatal.1c04770, doi:10.1021/acscatal.1c04770. This article has 29 citations and is from a highest quality peer-reviewed journal.

12. (vilboux2009mutationspectrumof pages 7-8): Thierry Vilboux, Michael Kayser, Wendy Introne, Pim Suwannarat, Isa Bernardini, Roxanne Fischer, Kevin O'Brien, Robert Kleta, Marjan Huizing, and William A. Gahl. Mutation spectrum of homogentisic acid oxidase (hgd) in alkaptonuria. Human Mutation, 30:1611-1619, Dec 2009. URL: https://doi.org/10.1002/humu.21120, doi:10.1002/humu.21120. This article has 120 citations and is from a domain leading peer-reviewed journal.

13. (abdelkhalek2023homogentisate12dioxygenase(hgd) pages 3-5): Zeinab S. Abdelkhalek, Iman G. Mahmoud, Heba Omair, Mohamed Abdulhay, and Mohamed A. Elmonem. Homogentisate 1,2-dioxygenase (hgd) gene variants in young egyptian patients with alkaptonuria. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-41200-7, doi:10.1038/s41598-023-41200-7. This article has 7 citations and is from a peer-reviewed journal.

14. (vilboux2009mutationspectrumof pages 2-3): Thierry Vilboux, Michael Kayser, Wendy Introne, Pim Suwannarat, Isa Bernardini, Roxanne Fischer, Kevin O'Brien, Robert Kleta, Marjan Huizing, and William A. Gahl. Mutation spectrum of homogentisic acid oxidase (hgd) in alkaptonuria. Human Mutation, 30:1611-1619, Dec 2009. URL: https://doi.org/10.1002/humu.21120, doi:10.1002/humu.21120. This article has 120 citations and is from a domain leading peer-reviewed journal.

15. (grasso2025ochronoticdepositionin pages 5-7): Daniela Grasso, Valentina Balloni, Maria Camilla Baratto, Adele Mucci, Annalisa Santucci, and Andrea Bernini. Ochronotic deposition in alkaptonuria: semiquinone-mediated oxidative coupling and metabolic drivers of homogentisic acid accumulation. International Journal of Molecular Sciences, 26:9674, Oct 2025. URL: https://doi.org/10.3390/ijms26199674, doi:10.3390/ijms26199674. This article has 0 citations.

16. (grasso2025ochronoticdepositionin pages 1-2): Daniela Grasso, Valentina Balloni, Maria Camilla Baratto, Adele Mucci, Annalisa Santucci, and Andrea Bernini. Ochronotic deposition in alkaptonuria: semiquinone-mediated oxidative coupling and metabolic drivers of homogentisic acid accumulation. International Journal of Molecular Sciences, 26:9674, Oct 2025. URL: https://doi.org/10.3390/ijms26199674, doi:10.3390/ijms26199674. This article has 0 citations.

17. (milella2024alkaptonuriafrommolecular pages 4-6): Maria Serena Milella, Michela Geminiani, Alfonso Trezza, Anna Visibelli, Daniela Braconi, and Annalisa Santucci. Alkaptonuria: from molecular insights to a dedicated digital platform. Cells, 13:1072, Jun 2024. URL: https://doi.org/10.3390/cells13121072, doi:10.3390/cells13121072. This article has 13 citations.

18. (bernardini2025acomprehensivein pages 18-23): Giulia Bernardini, Alfonso Trezza, Elena Petricci, Giulia Romagnoli, Demetra Zambardino, Fabrizio Manetti, Daniela Braconi, Michela Geminiani, and Annalisa Santucci. A comprehensive in vitro and in silico approach for targeting 4-hydroxyphenyl pyruvate dioxygenase: towards new therapeutics for alkaptonuria. International Journal of Molecular Sciences, 26:3181, Mar 2025. URL: https://doi.org/10.3390/ijms26073181, doi:10.3390/ijms26073181. This article has 0 citations.

19. (vijukumar2025acenturyof pages 6-10): Abhishek Vijukumar, Kamaljeet ., Harkomal Singh, Tarun Kalra, and Bintoo Sharma. A century of alkaptonuria: evolving insights into a rare metabolic disorder. GenoMed Connect, Dec 2025. URL: https://doi.org/10.69709/genomc.2025.122212, doi:10.69709/genomc.2025.122212. This article has 0 citations.

20. (bernardini2025acomprehensivein pages 82-84): Giulia Bernardini, Alfonso Trezza, Elena Petricci, Giulia Romagnoli, Demetra Zambardino, Fabrizio Manetti, Daniela Braconi, Michela Geminiani, and Annalisa Santucci. A comprehensive in vitro and in silico approach for targeting 4-hydroxyphenyl pyruvate dioxygenase: towards new therapeutics for alkaptonuria. International Journal of Molecular Sciences, 26:3181, Mar 2025. URL: https://doi.org/10.3390/ijms26073181, doi:10.3390/ijms26073181. This article has 0 citations.

21. (zatkova2020alkaptonuriacurrentperspectives pages 3-4): Andrea Zatkova, Lakshminarayan Ranganath, and Ludevit Kadasi. Alkaptonuria: current perspectives. The Application of Clinical Genetics, 13:37-47, Jan 2020. URL: https://doi.org/10.2147/tacg.s186773, doi:10.2147/tacg.s186773. This article has 93 citations.

22. (shen2026hgdderivednformylkynureninepromotes pages 1-7): Weitao Shen, Ruibin Yi, Yueming Zhang, Jiayi Cai, Qingxi Zhang, Haoxuan Ying, Ting Wei, and Jian Zhang. Hgd-derived n-formylkynurenine promotes small cell lung cancer chemoresistance by activating atl2-mediated endoplasmic reticulum remodelling. Unknown journal, Jan 2026. URL: https://doi.org/10.21203/rs.3.rs-8510398/v1, doi:10.21203/rs.3.rs-8510398/v1.

23. (shen2026hgdderivednformylkynureninepromotes pages 20-24): Weitao Shen, Ruibin Yi, Yueming Zhang, Jiayi Cai, Qingxi Zhang, Haoxuan Ying, Ting Wei, and Jian Zhang. Hgd-derived n-formylkynurenine promotes small cell lung cancer chemoresistance by activating atl2-mediated endoplasmic reticulum remodelling. Unknown journal, Jan 2026. URL: https://doi.org/10.21203/rs.3.rs-8510398/v1, doi:10.21203/rs.3.rs-8510398/v1.

24. (shen2026hgdderivednformylkynureninepromotes pages 11-16): Weitao Shen, Ruibin Yi, Yueming Zhang, Jiayi Cai, Qingxi Zhang, Haoxuan Ying, Ting Wei, and Jian Zhang. Hgd-derived n-formylkynurenine promotes small cell lung cancer chemoresistance by activating atl2-mediated endoplasmic reticulum remodelling. Unknown journal, Jan 2026. URL: https://doi.org/10.21203/rs.3.rs-8510398/v1, doi:10.21203/rs.3.rs-8510398/v1.

25. (shen2026hgdderivednformylkynureninepromotes pages 16-20): Weitao Shen, Ruibin Yi, Yueming Zhang, Jiayi Cai, Qingxi Zhang, Haoxuan Ying, Ting Wei, and Jian Zhang. Hgd-derived n-formylkynurenine promotes small cell lung cancer chemoresistance by activating atl2-mediated endoplasmic reticulum remodelling. Unknown journal, Jan 2026. URL: https://doi.org/10.21203/rs.3.rs-8510398/v1, doi:10.21203/rs.3.rs-8510398/v1.

26. (grasso2025ochronoticdepositionin pages 2-5): Daniela Grasso, Valentina Balloni, Maria Camilla Baratto, Adele Mucci, Annalisa Santucci, and Andrea Bernini. Ochronotic deposition in alkaptonuria: semiquinone-mediated oxidative coupling and metabolic drivers of homogentisic acid accumulation. International Journal of Molecular Sciences, 26:9674, Oct 2025. URL: https://doi.org/10.3390/ijms26199674, doi:10.3390/ijms26199674. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](HGD-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](HGD-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. vilboux2009mutationspectrumof pages 1-2
2. zatkova2020alkaptonuriacurrentperspectives pages 4-6
3. milella2024alkaptonuriafrommolecular pages 2-4
4. holme2013tyrosinemetabolism pages 1-2
5. vilboux2009mutationspectrumof pages 7-8
6. vijukumar2025acenturyof pages 13-17
7. zatkova2020alkaptonuriacurrentperspectives pages 3-4
8. bernardini2025acomprehensivein pages 18-23
9. shen2026hgdderivednformylkynureninepromotes pages 11-16
10. shen2026hgdderivednformylkynureninepromotes pages 20-24
11. grasso2025ochronoticdepositionin pages 2-5
12. grasso2025ochronoticdepositionin pages 5-7
13. grasso2025ochronoticdepositionin pages 1-2
14. vijukumar2025acenturyof pages 10-13
15. traore2022chargemaintenanceduring pages 3-5
16. traore2022chargemaintenanceduring pages 26-38
17. holme2013tyrosinemetabolism pages 2-4
18. traore2022chargemaintenanceduring pages 5-6
19. vilboux2009mutationspectrumof pages 2-3
20. milella2024alkaptonuriafrommolecular pages 4-6
21. vijukumar2025acenturyof pages 6-10
22. bernardini2025acomprehensivein pages 82-84
23. shen2026hgdderivednformylkynureninepromotes pages 1-7
24. shen2026hgdderivednformylkynureninepromotes pages 16-20
25. https://doi.org/10.1002/humu.21120,
26. https://doi.org/10.69709/genomc.2025.122212,
27. https://doi.org/10.1021/acscatal.1c04770,
28. https://doi.org/10.3390/cells13121072,
29. https://doi.org/10.1007/978-3-642-40337-8\_2,
30. https://doi.org/10.2147/tacg.s186773,
31. https://doi.org/10.1038/s41598-023-41200-7,
32. https://doi.org/10.3390/ijms26199674,
33. https://doi.org/10.3390/ijms26073181,
34. https://doi.org/10.21203/rs.3.rs-8510398/v1,