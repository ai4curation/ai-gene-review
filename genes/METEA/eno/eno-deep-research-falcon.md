---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-03T06:05:54.261569'
end_time: '2026-06-03T06:19:40.855342'
duration_seconds: 826.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: METEA
  gene_id: eno
  gene_symbol: eno
  uniprot_accession: C5AVP6
  protein_description: 'RecName: Full=Enolase {ECO:0000256|ARBA:ARBA00017068, ECO:0000256|HAMAP-Rule:MF_00318};
    EC=4.2.1.11 {ECO:0000256|ARBA:ARBA00012058, ECO:0000256|HAMAP-Rule:MF_00318};
    AltName: Full=2-phospho-D-glycerate hydro-lyase {ECO:0000256|HAMAP-Rule:MF_00318};
    AltName: Full=2-phosphoglycerate dehydratase {ECO:0000256|HAMAP-Rule:MF_00318};'
  gene_info: Name=eno {ECO:0000256|HAMAP-Rule:MF_00318, ECO:0000313|EMBL:ACS40732.1};
    OrderedLocusNames=MexAM1_META1p2984 {ECO:0000313|EMBL:ACS40732.1};
  organism_full: Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805
    / NCIMB 9133 / AM1) (Methylobacterium extorquens).
  protein_family: Belongs to the enolase family.
  protein_domains: Enolase. (IPR000941); Enolase-like_C_sf. (IPR036849); Enolase-like_N.
    (IPR029017); Enolase_C. (IPR020810); Enolase_CS. (IPR020809)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: eno-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** C5AVP6
- **Protein Description:** RecName: Full=Enolase {ECO:0000256|ARBA:ARBA00017068, ECO:0000256|HAMAP-Rule:MF_00318}; EC=4.2.1.11 {ECO:0000256|ARBA:ARBA00012058, ECO:0000256|HAMAP-Rule:MF_00318}; AltName: Full=2-phospho-D-glycerate hydro-lyase {ECO:0000256|HAMAP-Rule:MF_00318}; AltName: Full=2-phosphoglycerate dehydratase {ECO:0000256|HAMAP-Rule:MF_00318};
- **Gene Information:** Name=eno {ECO:0000256|HAMAP-Rule:MF_00318, ECO:0000313|EMBL:ACS40732.1}; OrderedLocusNames=MexAM1_META1p2984 {ECO:0000313|EMBL:ACS40732.1};
- **Organism (full):** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
- **Protein Family:** Belongs to the enolase family.
- **Key Domains:** Enolase. (IPR000941); Enolase-like_C_sf. (IPR036849); Enolase-like_N. (IPR029017); Enolase_C. (IPR020810); Enolase_CS. (IPR020809)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "eno" matches the protein description above**
2. **Verify the organism is correct:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'eno' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **eno** (gene ID: eno, UniProt: C5AVP6) in METEA.

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
- **UniProt Accession:** C5AVP6
- **Protein Description:** RecName: Full=Enolase {ECO:0000256|ARBA:ARBA00017068, ECO:0000256|HAMAP-Rule:MF_00318}; EC=4.2.1.11 {ECO:0000256|ARBA:ARBA00012058, ECO:0000256|HAMAP-Rule:MF_00318}; AltName: Full=2-phospho-D-glycerate hydro-lyase {ECO:0000256|HAMAP-Rule:MF_00318}; AltName: Full=2-phosphoglycerate dehydratase {ECO:0000256|HAMAP-Rule:MF_00318};
- **Gene Information:** Name=eno {ECO:0000256|HAMAP-Rule:MF_00318, ECO:0000313|EMBL:ACS40732.1}; OrderedLocusNames=MexAM1_META1p2984 {ECO:0000313|EMBL:ACS40732.1};
- **Organism (full):** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
- **Protein Family:** Belongs to the enolase family.
- **Key Domains:** Enolase. (IPR000941); Enolase-like_C_sf. (IPR036849); Enolase-like_N. (IPR029017); Enolase_C. (IPR020810); Enolase_CS. (IPR020809)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "eno" matches the protein description above**
2. **Verify the organism is correct:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'eno' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **eno** (gene ID: eno, UniProt: C5AVP6) in METEA.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: Functional annotation of **eno** (Enolase; EC 4.2.1.11) in *Methylorubrum extorquens* AM1 (METEA)

### 0) Executive summary
The target protein **UniProt C5AVP6** from *Methylorubrum extorquens* strain AM1 (formerly *Methylobacterium extorquens* AM1) is annotated as **enolase (eno)**, an enolase-family enzyme catalyzing the reversible dehydration of **D-2-phosphoglycerate (2-PG)** to **phosphoenolpyruvate (PEP)**, placing it in **central carbon metabolism** (glycolysis/gluconeogenesis). This assignment is strongly supported by conserved family/function logic and by organism-specific proteomic detection of enolase in AM1 cell extracts. AM1-specific studies in the accessible corpus do not provide spot-level quantitative fold-change data or direct biochemical assays for the specific AM1 enolase protein; therefore, substrate specificity/metal dependence/oligomeric state are best supported as **family-level properties** rather than AM1-measured values. Recent (2023–2024) literature most relevant to enolase emphasizes **moonlighting functions** (surface localization and plasminogen binding) in diverse bacteria—important as a cautionary note but not directly evidenced for AM1.

### 1) Target verification (mandatory identity checks)
**1.1. Gene symbol and protein description alignment**
The gene symbol **eno** matches the protein description “**Enolase**” (EC **4.2.1.11**) in the UniProt target definition provided by the user. In AM1-specific experimental literature, enolase is explicitly identified as “**enolase**” and discussed among central metabolic enzymes, consistent with this identity and not with an unrelated “eno”-named protein. (laukel2004comparisonofthe pages 16-17)

**1.2. Organism verification**
The organism context in the experimental proteomics evidence is *Methylobacterium extorquens* AM1 (the historical name corresponding to *Methylorubrum extorquens* AM1), matching the user-specified strain context. (laukel2004comparisonofthe pages 16-17)

**1.3. Family/domain consistency**
Enolase is a highly conserved enzyme of central metabolism across bacteria; the retrieved literature consistently treats it as such and describes canonical enolase structural organization (N- and C-terminal domains; dimer/octamer assemblies), aligning with an enolase-family protein. (satala2023therecruitmentand pages 8-10)

### 2) Key concepts and definitions (current understanding)

#### 2.1. Primary enzymatic function and reaction
Enolase functions in **glycolysis and gluconeogenesis** and catalyzes the **reversible conversion of D-2-phosphoglycerate (2-PGA/2-PG) to phosphoenolpyruvate (PEP)**. This is the defining biochemical activity for EC 4.2.1.11 and is explicitly stated in recent mechanistic descriptions. (o’kelly2024moonlightingonthe pages 1-2)

**Interpretation for AM1:** The UniProt C5AVP6 annotation as enolase implies the AM1 enzyme performs this canonical reaction in central carbon metabolism.

#### 2.2. Cellular localization: canonical vs “moonlighting”
A recent review on bacterial plasminogen recruitment describes enolase as “**a cytoplasmic enzyme classically involved in the glycolytic pathway**,” i.e., canonically an intracellular metabolic enzyme. (satala2023therecruitmentand pages 8-10)

However, multiple lines of evidence across bacteria show enolase can “moonlight” (perform additional functions beyond its canonical enzymatic role) when found in different localizations. A mechanistic review of moonlighting enzymes emphasizes that moonlighting often involves proteins being present in **different cellular localizations** and that functional switching can occur with modest structural changes. (gupta2023moonlightingenzymeswhen pages 2-3)

#### 2.3. Oligomeric state and structural organization (general bacterial enolase)
Bacterial enolase is reported to exist as a **dimer or octamer**, with each subunit containing a smaller **N-terminal** domain and larger **C-terminal** domain. (satala2023therecruitmentand pages 8-10)

For streptococcal enolase specifically, structural studies describe the octamer as “**an octamer formed from a tetramer of homodimers**,” giving a concrete organizational model (dimer → tetramer-of-dimers → octamer). (zhao2024identificationofplasminogenbinding pages 1-2)

**Important limitation for AM1:** These oligomeric-state statements are not AM1-specific measurements, but they support plausibility of typical enolase structural behavior for C5AVP6.

#### 2.4. Moonlighting concept: plasminogen binding on bacterial surfaces
A 2023 review frames bacterial enolase as the “best studied” bacterial plasminogen-binding protein and states that interaction between bacterial enolase and plasminogen can support microbial adherence to host cells and influence plasmin activity. (satala2023therecruitmentand pages 8-10)

A 2024 primary study in *Streptococcus suis* reports that “purified streptococcal surface enolase” can bind human plasminogen/plasmin and that engineered substitutions at predicted binding sites reduce binding while not affecting bacterial growth in vitro, linking specific residues to the moonlighting interaction. (zhao2024identificationofplasminogenbinding pages 1-2)

At the motif level, two broad plasminogen-binding determinants are repeatedly highlighted:
- **Surface-exposed lysine residues**, especially the **last two C-terminal lysines** in multiple species (review-level synthesis). (satala2023therecruitmentand pages 8-10)
- An **internal binding motif** (sequence example FYDKERKVY), described as a plasminogen-binding site in pneumococcal/streptococcal enolase literature. (zhao2024identificationofplasminogenbinding pages 1-2)

**Relevance to AM1:** *M. extorquens* AM1 is not a mammalian pathogen and no AM1-specific evidence of surface enolase or plasminogen binding was retrieved; therefore this should be treated as background biology and a caution against over-annotation.

### 3) Organism-specific evidence for **eno** in *Methylorubrum extorquens* AM1

#### 3.1. Experimental detection in the AM1 proteome
A differential proteomics study comparing AM1 growth under methylotrophic vs nonmethylotrophic conditions reports identification of **enolase** by 2D electrophoresis (2-DE) proteomics and lists enolase among enzymes identified in the study’s protein catalog (Table 1 referenced by the authors). (laukel2004comparisonofthe pages 16-17)

#### 3.2. Pathway placement: central metabolism interwoven with C1 assimilation
In discussing “assimilation of C1 units and central metabolism,” the same AM1 proteomics paper notes that pathways for C1 assimilation, PHB biosynthesis, and central metabolism are “highly interwoven,” and explicitly states: “Among these enzymes, we identified **enolase** …” alongside other central metabolic enzymes. (laukel2004comparisonofthe pages 16-17)

This supports assigning AM1 enolase to **central carbon flux** connecting glycolytic/gluconeogenic intermediates to downstream pathways required for growth on methanol and multicarbon substrates.

#### 3.3. Gene/protein identifier mapping available from the proteomics table excerpt
Within the retrieved Table 1 excerpt, enolase (“**Eno**”) appears in a gene list aligned with an **RMQ locus tag**; the excerpt most clearly supports an association of Eno with **RMQ04824** in the snippet’s alignment. (laukel2004comparisonofthe pages 5-5)

**Caution:** The snippet does not provide unambiguous mapping of spot IDs and expression ratios to enolase; further confirmation would require the full Table 1 in high resolution.

#### 3.4. Condition-dependent expression: what can and cannot be concluded
The AM1 proteomics paper reports strong induction for many methylotrophy-specific enzymes (e.g., serine cycle enzymes), but enolase is not highlighted in the retrieved text as one of the strongly induced methylotrophy proteins. (laukel2004comparisonofthe pages 16-17)

**Interpretation:** This is consistent with enolase behaving like a broadly required central-metabolism enzyme whose abundance may be less condition-specific than dedicated C1 assimilation enzymes; however, lack of explicit mention is not proof of no regulation.

### 4) Recent developments (2023–2024 prioritized)

#### 4.1. 2023–2024 enolase research most relevant to functional annotation: moonlighting and surface biology
Two 2023–2024 sources are particularly informative for *current understanding* of enolase beyond glycolysis:
- A 2023 review synthesizes bacterial mechanisms for plasminogen recruitment and provides a detailed structural discussion of enolase as a conserved cytoplasmic enzyme that can also exist as dimer/octamer and bind plasminogen via lysine residues and internal motifs. (satala2023therecruitmentand pages 8-10)
- A 2024 primary study uses CRISPR/Cas9-engineered point mutants of *S. suis* enolase to test predicted plasminogen-binding sites and links reduced plasminogen binding to reduced translocation across an endothelial monolayer in vitro, strengthening causal interpretation for enolase moonlighting in a pathogenic context. (zhao2024identificationofplasminogenbinding pages 1-2)

These are **not AM1-specific**, but they represent “latest research” on enolase function and localization in bacteria.

#### 4.2. 2024 mechanistic definition of enolase reaction and dimeric activity
A 2024 study on *Fasciola hepatica* enolase reiterates the canonical enzymatic role: a ~47 kDa enzyme in glycolysis/gluconeogenesis that reversibly converts **2-PGA to PEP**, and reports active homodimeric enzyme (~94 kDa) in recombinant form. While not bacterial, it provides a clear, recent, peer-reviewed definitional statement of the reaction and typical size/dimeric behavior of enolase. (o’kelly2024moonlightingonthe pages 1-2)

#### 4.3. What is missing for 2023–2024 AM1 eno specifically
Within the tool-accessible 2023–2024 corpus retrieved here, no AM1-focused 2023–2024 paper was found that explicitly centers **eno/enolase** (e.g., reporting differential expression, fitness/essentiality, or AM1 enolase biochemistry). This is a data-availability limitation of this run rather than strong evidence of absence in the broader literature.

### 5) Current applications and real-world implementations

#### 5.1. Functional annotation and systems biology
Because enolase is a conserved enzyme, **family-based annotation** (enolase family membership, EC 4.2.1.11 assignment) is commonly used in genome annotation pipelines. Organism-specific proteomic detection in AM1 supports that the encoded protein is expressed and participates in central metabolism. (laukel2004comparisonofthe pages 16-17)

#### 5.2. Pathogen biology (general) and translational implications
In pathogens, surface-localized enolase can contribute to host interaction by binding plasminogen and aiding dissemination. A 2024 study provides an example where mutating predicted plasminogen-binding sites reduced plasminogen binding and reduced translocation in a BBB model. (zhao2024identificationofplasminogenbinding pages 1-2)

**Relevance to AM1:** This is mainly a caution for annotation: “cell surface enolase/plasminogen binding” should not be assigned to AM1 without direct evidence.

### 6) Expert opinions and analysis from authoritative sources

#### 6.1. Enolase as a conserved cytoplasmic enzyme with context-dependent surface roles
A 2023 review emphasizes enolase’s canonical identity as a cytoplasmic glycolytic enzyme and synthesizes evidence for its role as a surface plasminogen receptor in many bacteria, with binding mediated by surface-exposed lysines and/or internal motifs; the review also highlights that conformation (e.g., octamer state) can affect exposure of binding epitopes. (satala2023therecruitmentand pages 8-10)

#### 6.2. Conceptual framing of moonlighting proteins
A 2023 conceptual review defines moonlighting proteins as single proteins with multiple independent functions not arising from gene fusion/splicing and notes that different **cellular localizations** are a major driver of functional switching. (gupta2023moonlightingenzymeswhen pages 2-3)

### 7) Statistics and quantitative data (recent studies)

#### 7.1. Quantitative/statistical evidence available in this run
- For AM1 enolase: the retrieved AM1 proteomics excerpts confirm identification but do **not** provide extractable quantitative fold-changes or spot intensities for enolase in the text chunks available. (laukel2004comparisonofthe pages 16-17, laukel2004comparisonofthe pages 5-5)

- For bacterial moonlighting enolase: the 2024 *S. suis* study reports that amino-acid substitutions in predicted plasminogen-binding sites reduced plasminogen/plasmin binding and reduced translocation across an endothelial cell monolayer, but the specific numeric binding or translocation values were not present in the excerpts retrieved here. (zhao2024identificationofplasminogenbinding pages 1-2)

**Therefore, this report intentionally avoids reporting numeric fold-changes or fitness coefficients that cannot be directly cited from retrieved text.**

### 8) Proposed functional annotation for METEA eno (UniProt C5AVP6)

**Recommended primary function (high confidence):**
- **Enolase (EC 4.2.1.11)**; catalyzes **2-phospho-D-glycerate ⇌ phosphoenolpyruvate** in glycolysis/gluconeogenesis; contributes to central carbon metabolism feeding into biomass and energy generation. (o’kelly2024moonlightingonthe pages 1-2, laukel2004comparisonofthe pages 16-17)

**Substrate specificity:**
- Consistent with canonical enolase activity on **2-phosphoglycerate** producing **PEP** (family-level conserved reaction). (o’kelly2024moonlightingonthe pages 1-2)

**Likely localization (primary annotation):**
- **Cytoplasmic**, consistent with enolase’s canonical role as a glycolytic enzyme. (satala2023therecruitmentand pages 8-10)

**Moonlighting/localization outside cytoplasm (do not assign without evidence):**
- While many bacteria display enolase on the surface as a plasminogen-binding protein, no evidence for this in AM1 was retrieved; this should not be included as an AM1 annotation without direct experimental support. (satala2023therecruitmentand pages 8-10, zhao2024identificationofplasminogenbinding pages 1-2)

### 9) Evidence summary table
| Evidence type | Finding (function/reaction, localization, pathways, expression/induction) | Organism/Context | Source (first author, year, journal) | URL/DOI | Notes/limitations |
|---|---|---|---|---|---|
| Database/homology | UniProt C5AVP6 annotates **eno / MexAM1_META1p2984** as **enolase** (EC 4.2.1.11), a member of the enolase family; catalyzes the canonical reversible conversion of **2-phospho-D-glycerate to phosphoenolpyruvate** in glycolysis/gluconeogenesis; domain architecture is consistent with enolase-family proteins. | *Methylorubrum extorquens* AM1 (formerly *Methylobacterium extorquens* AM1) | UniProt/InterPro-style annotation summarized from retrieved context and target description; supported by general enolase literature (O’Kelly 2024, PLOS Negl Trop Dis) | https://www.uniprot.org/uniprotkb/C5AVP6 ; https://doi.org/10.1371/journal.pntd.0012069 | Strong family-level inference, but not a direct AM1 biochemical assay for C5AVP6 in retrieved literature (o’kelly2024moonlightingonthe pages 1-2) |
| Experimental | Enolase was **identified by 2-DE proteomics** in AM1 cell extracts and listed among central metabolic enzymes detected in the proteome. | AM1 grown under methylotrophic and nonmethylotrophic conditions | Laukel, 2004, *PROTEOMICS* | https://doi.org/10.1002/pmic.200300713 | Confirms protein detection in AM1, but retrieved pages do not provide a direct quantitative fold-change or spot-specific abundance value for enolase (laukel2004comparisonofthe pages 16-17, laukel2004comparisonofthe pages 5-5) |
| Experimental + pathway interpretation | Authors explicitly place enolase among enzymes in **highly interwoven central metabolism**, alongside aconitase, β-ketothiolase, R-specific enoyl-CoA hydratase, and propionyl-CoA carboxylase, linking eno to carbon assimilation/central carbon flux rather than a specialized peripheral pathway. | AM1 central metabolism during methylotrophic vs succinate growth comparisons | Laukel, 2004, *PROTEOMICS* | https://doi.org/10.1002/pmic.200300713 | Useful for pathway assignment; still indirect for exact flux direction under each condition (laukel2004comparisonofthe pages 16-17) |
| Experimental (negative/limited expression evidence) | In the retrieved AM1 proteomics study, many **serine-cycle enzymes** were induced on methylotrophic growth, but **enolase was not singled out** as methylotrophy-induced in the text available. | Methanol vs succinate growth in AM1 | Laukel, 2004, *PROTEOMICS* | https://doi.org/10.1002/pmic.200300713 | Suggests enolase may behave as a constitutive central-metabolism enzyme; absence of explicit induction data in retrieved pages is not proof of no regulation (laukel2004comparisonofthe pages 16-17) |
| Localization inference (homology/general bacterial biology) | Canonical enolase is a **cytoplasmic** glycolytic enzyme in bacteria; no AM1-specific evidence for periplasmic, membrane, or extracellular localization was retrieved. | General bacterial enolase biology applied cautiously to AM1 | Satala, 2023, *Int J Mol Sci* | https://doi.org/10.3390/ijms241310436 | Appropriate for primary annotation, but not organism-specific localization proof for AM1 (satala2023therecruitmentand pages 8-10, satala2023therecruitmentand pages 7-8) |
| General mechanistic background | Enolase commonly requires **Mg2+** and can occur as **dimeric or octameric** assemblies in bacteria; these conserved properties support catalytic plausibility for C5AVP6 as an authentic enolase. | General bacterial/phylogenetic enolase literature | Quiroz-Castañeda, 2023, *Front Vet Sci*; Satala, 2023, *Int J Mol Sci* | https://doi.org/10.3389/fvets.2023.1225873 ; https://doi.org/10.3390/ijms241310436 | Generalized from other taxa; no AM1-specific metal-dependence or oligomerization assay retrieved (quirozcastaneda2023analternativevaccine pages 12-12, satala2023therecruitmentand pages 8-10, quirozcastaneda2023analternativevaccine pages 6-6) |
| General caution on moonlighting | Bacterial enolase can be **surface-exposed** and bind **plasminogen** in several pathogens, but no evidence for such moonlighting localization/function was retrieved for AM1, a nonpathogenic methylotroph. | Other bacteria, not AM1 | Zhao, 2024, *Front Cell Infect Microbiol*; Satala, 2023, *Int J Mol Sci* | https://doi.org/10.3389/fcimb.2024.1356628 ; https://doi.org/10.3390/ijms241310436 | Important not to over-transfer pathogenic moonlighting annotations to AM1 without direct evidence (zhao2024identificationofplasminogenbinding pages 1-2, satala2023therecruitmentand pages 8-10) |


*Table: This table summarizes the main functional annotation evidence for enolase (eno; UniProt C5AVP6) in Methylorubrum extorquens AM1, distinguishing direct AM1 experimental observations from family-level inference. It is useful for deciding which aspects of the annotation are strongly supported versus tentative.*

### 10) Key limitations of the current evidence set
1. **AM1-specific quantitative proteomics for enolase** (spot ID, fold-change methanol vs succinate) was not extractable from retrieved text; image extraction failed for the relevant table region. (laukel2004comparisonofthe pages 5-5)
2. **AM1-specific essentiality/fitness profiling** (e.g., RB-TnSeq/TnSeq) for eno was not available in the retrieved corpus during this run.
3. 2023–2024 literature was strongest for **general enolase moonlighting biology**, not AM1-specific enolase characterization.

### 11) Key cited sources (with URLs and publication dates)
- Laukel M. et al. “Comparison of the proteome of *Methylobacterium extorquens* AM1 grown under methylotrophic and nonmethylotrophic conditions.” **PROTEOMICS**. **May 2004**. https://doi.org/10.1002/pmic.200300713 (laukel2004comparisonofthe pages 16-17)
- Satala D. et al. “The Recruitment and Activation of Plasminogen by Bacteria—The Involvement in Chronic Infection Development.” **Int. J. Mol. Sci.** **Jun 2023**. https://doi.org/10.3390/ijms241310436 (satala2023therecruitmentand pages 8-10)
- Zhao T. et al. “Identification of plasminogen-binding sites in *Streptococcus suis* enolase…” **Front. Cell. Infect. Microbiol.** **Feb 22, 2024**. https://doi.org/10.3389/fcimb.2024.1356628 (zhao2024identificationofplasminogenbinding pages 1-2)
- Gupta M.N., Uversky V.N. “Moonlighting enzymes: when cellular context defines specificity.” **Cell. Mol. Life Sci.** **Apr 2023**. https://doi.org/10.1007/s00018-023-04781-0 (gupta2023moonlightingenzymeswhen pages 2-3)
- O’Kelly E. et al. “Moonlighting on the *Fasciola hepatica* tegument: Enolase…” **PLOS Negl Trop Dis.** **Aug 30, 2024**. https://doi.org/10.1371/journal.pntd.0012069 (o’kelly2024moonlightingonthe pages 1-2)


References

1. (laukel2004comparisonofthe pages 16-17): Markus Laukel, Michel Rossignol, Gisèle Borderies, Uwe Völker, and Julia A. Vorholt. Comparison of the proteome of methylobacterium extorquens am1 grown under methylotrophic and nonmethylotrophic conditions. PROTEOMICS, 4:1247-1264, May 2004. URL: https://doi.org/10.1002/pmic.200300713, doi:10.1002/pmic.200300713. This article has 66 citations and is from a peer-reviewed journal.

2. (satala2023therecruitmentand pages 8-10): Dorota Satala, Aneta Bednarek, Andrzej Kozik, Maria Rapala-Kozik, and Justyna Karkowska-Kuleta. The recruitment and activation of plasminogen by bacteria—the involvement in chronic infection development. International Journal of Molecular Sciences, 24:10436, Jun 2023. URL: https://doi.org/10.3390/ijms241310436, doi:10.3390/ijms241310436. This article has 16 citations.

3. (o’kelly2024moonlightingonthe pages 1-2): Eve O’Kelly, Krystyna Cwiklinski, Carolina De Marco Verissimo, Nichola Eliza Davies Calvani, Jesús López Corrales, Heather Jewhurst, Andrew Flaus, Richard Lalor, Judit Serrat, John P. Dalton, and Javier González-Miguel. Moonlighting on the fasciola hepatica tegument: enolase, a glycolytic enzyme, interacts with the extracellular matrix and fibrinolytic system of the host. PLOS Neglected Tropical Diseases, 18:e0012069, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012069, doi:10.1371/journal.pntd.0012069. This article has 9 citations and is from a domain leading peer-reviewed journal.

4. (gupta2023moonlightingenzymeswhen pages 2-3): Munishwar Nath Gupta and Vladimir N. Uversky. Moonlighting enzymes: when cellular context defines specificity. Cellular and Molecular Life Sciences, 80:1-23, Apr 2023. URL: https://doi.org/10.1007/s00018-023-04781-0, doi:10.1007/s00018-023-04781-0. This article has 66 citations and is from a domain leading peer-reviewed journal.

5. (zhao2024identificationofplasminogenbinding pages 1-2): Tiantong Zhao, Alex Gussak, Bart van der Hee, Sylvia Brugman, Peter van Baarlen, and Jerry M. Wells. Identification of plasminogen-binding sites in streptococcus suis enolase that contribute to bacterial translocation across the blood-brain barrier. Frontiers in Cellular and Infection Microbiology, Feb 2024. URL: https://doi.org/10.3389/fcimb.2024.1356628, doi:10.3389/fcimb.2024.1356628. This article has 10 citations.

6. (laukel2004comparisonofthe pages 5-5): Markus Laukel, Michel Rossignol, Gisèle Borderies, Uwe Völker, and Julia A. Vorholt. Comparison of the proteome of methylobacterium extorquens am1 grown under methylotrophic and nonmethylotrophic conditions. PROTEOMICS, 4:1247-1264, May 2004. URL: https://doi.org/10.1002/pmic.200300713, doi:10.1002/pmic.200300713. This article has 66 citations and is from a peer-reviewed journal.

7. (satala2023therecruitmentand pages 7-8): Dorota Satala, Aneta Bednarek, Andrzej Kozik, Maria Rapala-Kozik, and Justyna Karkowska-Kuleta. The recruitment and activation of plasminogen by bacteria—the involvement in chronic infection development. International Journal of Molecular Sciences, 24:10436, Jun 2023. URL: https://doi.org/10.3390/ijms241310436, doi:10.3390/ijms241310436. This article has 16 citations.

8. (quirozcastaneda2023analternativevaccine pages 12-12): Rosa Estela Quiroz-Castañeda, Hugo Aguilar-Díaz, and Itzel Amaro-Estrada. An alternative vaccine target for bovine anaplasmosis based on enolase, a moonlighting protein. Frontiers in Veterinary Science, Sep 2023. URL: https://doi.org/10.3389/fvets.2023.1225873, doi:10.3389/fvets.2023.1225873. This article has 8 citations and is from a peer-reviewed journal.

9. (quirozcastaneda2023analternativevaccine pages 6-6): Rosa Estela Quiroz-Castañeda, Hugo Aguilar-Díaz, and Itzel Amaro-Estrada. An alternative vaccine target for bovine anaplasmosis based on enolase, a moonlighting protein. Frontiers in Veterinary Science, Sep 2023. URL: https://doi.org/10.3389/fvets.2023.1225873, doi:10.3389/fvets.2023.1225873. This article has 8 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](eno-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. laukel2004comparisonofthe pages 16-17
2. satala2023therecruitmentand pages 8-10
3. gupta2023moonlightingenzymeswhen pages 2-3
4. zhao2024identificationofplasminogenbinding pages 1-2
5. laukel2004comparisonofthe pages 5-5
6. satala2023therecruitmentand pages 7-8
7. quirozcastaneda2023analternativevaccine pages 12-12
8. quirozcastaneda2023analternativevaccine pages 6-6
9. https://www.uniprot.org/uniprotkb/C5AVP6
10. https://doi.org/10.1371/journal.pntd.0012069
11. https://doi.org/10.1002/pmic.200300713
12. https://doi.org/10.3390/ijms241310436
13. https://doi.org/10.3389/fvets.2023.1225873
14. https://doi.org/10.3389/fcimb.2024.1356628
15. https://doi.org/10.1007/s00018-023-04781-0
16. https://doi.org/10.1002/pmic.200300713,
17. https://doi.org/10.3390/ijms241310436,
18. https://doi.org/10.1371/journal.pntd.0012069,
19. https://doi.org/10.1007/s00018-023-04781-0,
20. https://doi.org/10.3389/fcimb.2024.1356628,
21. https://doi.org/10.3389/fvets.2023.1225873,