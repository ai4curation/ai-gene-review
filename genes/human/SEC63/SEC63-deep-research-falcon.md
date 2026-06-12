---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T02:42:01.779079'
end_time: '2026-06-12T03:04:53.974052'
duration_seconds: 1372.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SEC63
  gene_symbol: SEC63
  uniprot_accession: Q9UGP8
  protein_description: 'RecName: Full=Translocation protein SEC63 homolog; AltName:
    Full=DnaJ homolog subfamily C member 23 {ECO:0000303|PubMed:18663603};'
  gene_info: Name=SEC63 {ECO:0000303|PubMed:28375157, ECO:0000312|HGNC:HGNC:21082};
    Synonyms=DNAJC23 {ECO:0000303|PubMed:18663603}, SEC63L;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: C2_domain_sf. (IPR035892); DnaJ_domain. (IPR001623); Ig_E-set.
    (IPR014756); J_dom_sf. (IPR036869); Sec63-dom. (IPR004179)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: SEC63-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: SEC63-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000016 The requested visual summaries can be
    found in Figure 2 and Table 1 of the document. - **Figure 2** is a pie chart that
    displays th'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9UGP8
- **Protein Description:** RecName: Full=Translocation protein SEC63 homolog; AltName: Full=DnaJ homolog subfamily C member 23 {ECO:0000303|PubMed:18663603};
- **Gene Information:** Name=SEC63 {ECO:0000303|PubMed:28375157, ECO:0000312|HGNC:HGNC:21082}; Synonyms=DNAJC23 {ECO:0000303|PubMed:18663603}, SEC63L;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_domain_sf. (IPR035892); DnaJ_domain. (IPR001623); Ig_E-set. (IPR014756); J_dom_sf. (IPR036869); Sec63-dom. (IPR004179)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SEC63" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SEC63' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SEC63** (gene ID: SEC63, UniProt: Q9UGP8) in human.

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
- **UniProt Accession:** Q9UGP8
- **Protein Description:** RecName: Full=Translocation protein SEC63 homolog; AltName: Full=DnaJ homolog subfamily C member 23 {ECO:0000303|PubMed:18663603};
- **Gene Information:** Name=SEC63 {ECO:0000303|PubMed:28375157, ECO:0000312|HGNC:HGNC:21082}; Synonyms=DNAJC23 {ECO:0000303|PubMed:18663603}, SEC63L;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_domain_sf. (IPR035892); DnaJ_domain. (IPR001623); Ig_E-set. (IPR014756); J_dom_sf. (IPR036869); Sec63-dom. (IPR004179)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SEC63" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SEC63' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SEC63** (gene ID: SEC63, UniProt: Q9UGP8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Human **SEC63** (UniProt **Q9UGP8**; gene **SEC63**, synonyms **DNAJC23/SEC63L**) — functional annotation and disease relevance

## 0. Target verification (critical identity checks)
The evidence assembled matches the intended target: **human SEC63** (also referred to as **DNAJC23**), an **endoplasmic reticulum (ER) membrane** J-domain co-chaperone that functions as an accessory factor of the **Sec61 translocon** in conjunction with Sec62 and the luminal Hsp70 **BiP**. Human SEC63 contains a **J-domain** (Hsp40/DnaJ-type), is part of the **Sec61/Sec62/Sec63** machinery, and is repeatedly discussed in the context of **autosomal dominant polycystic liver disease (ADPLD)** in human genetics literature. (lang2022signalpeptidefeatures pages 19-21, schorr2020identificationofsignal pages 13-14, jung2021emergingviewon pages 9-10, yang2023geneticspectrumof pages 1-3)

## 1. Key concepts and definitions (current understanding)

### 1.1 Sec61 translocon and ER protein entry
The **Sec61 complex** is the universally conserved protein-conducting channel in the ER membrane responsible for translocating hydrophilic polypeptide segments into the ER lumen and integrating hydrophobic transmembrane segments into the lipid bilayer. It operates with partner complexes to coordinate targeting and translocation of secretory and membrane proteins. (itskanov2023mechanismofprotein pages 1-3)

A recurring quantitative framing is that **~one-third of mammalian polypeptides/proteome** enter the ER through Sec61-dependent pathways. (okeefe2020membranetranslocationat pages 1-3)

### 1.2 Sec62/Sec63 as translocon accessory factors
Sec62 and Sec63 form an **accessory complex** that associates with Sec61 and **modulates channel gating** and substrate handling. Classical models emphasized a split between **SRP-dependent co-translational** import and **Sec62/Sec63-dependent post-translational** import; however, mammalian evidence supports roles for Sec62/Sec63 in assisting certain substrates even during **co-translational** translocation when signal peptides are “more demanding” (e.g., less hydrophobic). (jung2021emergingviewon pages 1-3, okeefe2020membranetranslocationat pages 1-3)

### 1.3 What SEC63 is (and is not)
SEC63 is best viewed as a **protein translocation regulator** rather than an enzyme. Its primary molecular function is to help the Sec61 channel open and to coordinate luminal chaperone assistance via its **J-domain**, enabling efficient ER import for substrates with **weak/slowly gating signal peptides**. (lang2022signalpeptidefeatures pages 19-21, schorr2020identificationofsignal pages 13-14, okeefe2020membranetranslocationat pages 1-3)

## 2. SEC63 protein features: domains, topology, and localization

### 2.1 Domain evidence in human cells
A human functional study identified an **N-terminal J-domain (aa 23–91)** and a **G/F region (aa 92–127)** in SEC63, consistent with assignment to the DnaJ/Hsp40 co-chaperone family. (schorr2020identificationofsignal pages 13-14)

### 2.2 Conserved topology and structural features (ortholog structural context)
High-resolution cryo-EM studies of the eukaryotic Sec complex (yeast) show Sec63 as an **integral membrane protein** with **three transmembrane segments**, an **ER-luminal J-domain**, and a large cytosolic region containing a fibronectin type III-like (Ig/FN3) architecture that contacts Sec61 loops and contributes to **opening (“priming”) of the Sec61 lateral gate**. Although these structures are yeast, reviews emphasize which elements are conserved and provide the mechanistic framework widely applied to metazoan SEC63 function. (itskanov2019structureofthe pages 1-2, wu2019structureofthe pages 1-2)

### 2.3 Subcellular location
SEC63 functions at the **ER membrane translocon**. Reviews in the mammalian context describe Sec63 associating with Sec61 and Sec62 in ER membranes, consistent with SEC63’s primary site of action being the ER. (jung2021emergingviewon pages 7-9, okeefe2020membranetranslocationat pages 1-3)

## 3. Primary function and mechanism (SEC63 in ER protein translocation)

### 3.1 Core functional role: Sec61 gating and translocation assistance
Mechanistically, Sec63 is positioned to **promote/enable Sec61 channel opening** (including lateral gate opening) for substrates whose signal peptides do not efficiently gate Sec61 on their own. Sec63 is also described as mediating translocation of a **broader range of precursors than Sec62**, suggesting a central role in supporting multiple import modes and client classes. (jung2021emergingviewon pages 9-10)

### 3.2 J-domain/BiP coupling and directional transport
SEC63’s **J-domain** provides an Hsp40-like co-chaperone function that couples Sec61 gating to luminal chaperone action. In yeast structural and mechanistic models, the luminal J-domain activates the Hsp70 (BiP/Kar2) cycle to promote binding to incoming substrates and reduce backsliding, contributing a luminal “pulling/ratcheting” component to translocation. Human-focused work supports that SEC63 participates in **Sec62/Sec63/BiP-dependent import** and that removing the SEC63 J-domain reduces dependence of at least one substrate (ERj3) on Sec62/Sec63/BiP. (wu2019structureofthe pages 1-2, schorr2020identificationofsignal pages 13-14, lang2022signalpeptidefeatures pages 19-21)

## 4. Substrate specificity and pathway context

### 4.1 Signal peptide features that drive Sec62/Sec63 dependence
Mammalian studies emphasize that Sec62/Sec63 dependence is **substrate-specific** and often linked to signal peptide features:
- **Longer but less hydrophobic** signal peptide hydrophobic regions
- Lower polarity properties of the signal peptide C-region
- In some clients, a **positively charged cluster** downstream of the signal peptide contributes to dependence
These features align with a model where Sec63 (often with Sec62 and sometimes BiP) helps “weak” signals achieve productive Sec61 gating. (lang2022signalpeptidefeatures pages 19-21, okeefe2020membranetranslocationat pages 1-3)

### 4.2 Quantitative proteomics defining SEC63 impact and candidate clients
Two complementary datasets provide quantitative functional constraints on SEC63’s contribution to the human secretory pathway:

**(i) Short-term HeLa depletion study (limited immediate proteome impact)**
- **6,655 proteins quantified** by MS
- **34 proteins** significantly changed with Sec63 depletion (**21 decreased**, **13 increased**)
- Decreased proteins were enriched for **signal peptides (2×)**, **N-glycosylation (2.6×)**, and **membrane proteins (2.8×)**, consistent with a focused effect on secretory/membrane precursor biogenesis. (schorr2020identificationofsignal pages 3-7)

**(ii) HEK293 gene-disruption context (broader steady-state remodeling)**
- In HEK293, Sec63 deficiency was reported to affect steady-state levels of **302 proteins** (**199 decreased**, **103 increased**).
- Overlap with Sec62 effects included **22 precursor polypeptides** negatively affected by both Sec62 and Sec63 perturbation (**11 with cleavable signal peptides, 11 with transmembrane helices**). (lang2022signalpeptidefeatures pages 19-21, schorr2020identificationofsignal pages 7-8)

Interpretation: SEC63 appears to be a **general translocon cofactor** whose acute depletion may show a limited short-term footprint in some cell contexts, while longer-term loss can produce broader remodeling consistent with central involvement in ER protein biogenesis. (lang2022signalpeptidefeatures pages 19-21, schorr2020identificationofsignal pages 3-7)

## 5. Pathways and biological processes linked to SEC63 function

### 5.1 ER proteostasis and secretory pathway biogenesis
SEC63 functions within ER protein biogenesis, affecting co- and post-translational import steps by coordinating Sec61 gating with chaperone action. This directly places SEC63 in pathways governing **secretory and membrane protein production**, which includes many glycoproteins that require proper ER entry for folding and maturation. (itskanov2023mechanismofprotein pages 1-3, okeefe2020membranetranslocationat pages 1-3)

### 5.2 Mechanistic link to polycystin biogenesis (PC1/PC2)
Recent disease-focused reviews frame SEC63 (with other ER quality-control and protein-processing genes such as PRKCSH, GANAB, ALG8/ALG9, SEC61B) as affecting hepatic (and sometimes renal) cystogenesis by impairing the production/function of **polycystin-1 (PC1)** and **polycystin-2 (PC2)** or facilitating their degradation. This proposes a functional bridge from translocon-level defects to organ-level cyst phenotypes. (mahboobipour2024clinicalmanifestationepidemiology pages 1-2, mizuno2024geneticanalysisof pages 1-2)

## 6. Recent developments and latest research (prioritizing 2023–2024)

### 6.1 2024 severe-PLD cohort genetics (Japan; Kidney360)
A 2024 whole-exome sequencing study of **severe PLD** (hTLV >1800 ml/m) enrolled **49 patients** and found pathogenic/suspected pathogenic variants in **44/49 (90%)**. Among genetically solved cases, SEC63 accounted for **1/44 (2%)**; ADPLD-related genes collectively represented **~20%** of the cohort. The study also provides practical variant-filtering criteria (e.g., **MAF <1e-4 in gnomAD**) and approaches for adjudicating missense variants and identifying heterozygous deletions. (mizuno2024geneticanalysisof pages 1-2)

Visual evidence from the same paper summarizes gene distribution and patient-level clinical/genetic details (Figure 2, Table 1). (mizuno2024geneticanalysisof media 7f91773b, mizuno2024geneticanalysisof media 3666ec3e, mizuno2024geneticanalysisof media 669179d2)

### 6.2 2024 PLD review (Orphanet Journal of Rare Diseases)
A 2024 review reiterates SEC63’s placement among **ER quality-control/protein processing genes** that can cause PLD and summarizes clinical practice: diagnosis is primarily imaging-based, and genetic testing is not mandatory for all patients but can be useful for complex cases and prognosis/stratification. It also summarizes available treatments (somatostatin analogs, interventional/surgical procedures, transplantation) and highlights multiple investigational targets grounded in mechanistic pathways. (mahboobipour2024clinicalmanifestationepidemiology pages 1-2)

### 6.3 2023–2024 focus on “missing heritability” and two-hit mechanisms
A 2023 genetics-focused report emphasizes that known ADPLD genes (including SEC63) explain only **~30–45%** of ADPLD cases, motivating gene discovery and careful variant interpretation. It also highlights **loss of heterozygosity (LOH)** in cyst epithelium as a demonstrated mechanism for PRKCSH- and **SEC63-associated** disease, supporting a **two-hit** model for cyst initiation. (boerrigter2023heterozygosityofalg9 pages 8-10)

### 6.4 2023 mechanistic synthesis for Sec61 partner complexes
A 2023 Cold Spring Harbor Perspectives review summarizes emerging models from cryo-EM and functional studies explaining how the Sec61 channel operates with partner complexes (explicitly including Sec62–Sec63) to activate translocation, provide driving force, and couple translocation to downstream processes. (itskanov2023mechanismofprotein pages 1-3)

## 7. Current applications and real-world implementations

### 7.1 Diagnostic genetics and testing strategies
Across recent reviews and cohorts, SEC63 is treated as a **major ADPLD locus** (with PRKCSH). Clinical practice increasingly favors **NGS panels** (PKD + ciliopathy genes) or exome sequencing when phenotype overlaps complicate classification, rather than older linkage approaches. (yang2023geneticspectrumof pages 1-3, boerrigter2023heterozygosityofalg9 pages 8-10)

Practical implementations documented in the 2024 cohort include explicit filtering thresholds (e.g., **MAF <1e-4**), ACMG adjudication of nontruncating variants, and complementary approaches for copy number changes (qPCR confirmation of suspected deletions). (mizuno2024geneticanalysisof pages 1-2)

### 7.2 Imaging-based diagnostic criteria for PLD/ADPLD in practice
The 2024 Orphanet review states PLD diagnosis is mainly imaging-based and that identification of **>20 hepatic cysts** commonly confirms PLD. (mahboobipour2024clinicalmanifestationepidemiology pages 1-2)

A genetics cohort assembly strategy from 2023 used **>10 hepatic cysts** as an inclusion threshold for PLD (for gene discovery after excluding known gene variants). (boerrigter2023novelα13glucosyltransferasevariants pages 2-3)

### 7.3 Pathway-informed therapeutic directions
While SEC63 itself is not currently a direct drug target in PLD, 2024 reviews outline treatment and investigational approaches based on downstream mechanisms (e.g., ER quality control, signaling pathways). Standard-of-care options include **somatostatin analogs** and interventional/surgical approaches, with liver transplantation as a definitive option for severe cases. (mahboobipour2024clinicalmanifestationepidemiology pages 1-2)

## 8. Expert opinions and analysis (authoritative synthesis)

### 8.1 Consensus mechanistic model for SEC63 function
Across mechanistic reviews, the dominant model is that SEC63 (often with Sec62) provides **substrate-selective assistance** to Sec61 gating, especially for weak signal peptides, and couples translocation to luminal chaperone action via its **J-domain** and **BiP**. (okeefe2020membranetranslocationat pages 1-3, lang2022signalpeptidefeatures pages 19-21, wu2019structureofthe pages 1-2)

### 8.2 Disease mechanism consensus for SEC63-associated ADPLD
Recent PLD genetic reviews converge on SEC63 as a **major ADPLD gene**, where pathogenic variants can act through ER protein biogenesis defects that diminish functional polycystin pathways and promote hepatic cystogenesis. The two-hit/LOH model is viewed as a plausible cellular mechanism for cyst formation in SEC63-linked disease. (yang2023geneticspectrumof pages 1-3, mahboobipour2024clinicalmanifestationepidemiology pages 1-2, boerrigter2023heterozygosityofalg9 pages 8-10)

## 9. Relevant statistics and data (selected highlights)
- **~1/3 of mammalian polypeptides** enter the ER via Sec61 (context for SEC63 function). (okeefe2020membranetranslocationat pages 1-3)
- **SEC63 domain evidence:** J-domain aa **23–91**, G/F region aa **92–127** (human study). (schorr2020identificationofsignal pages 13-14)
- **Proteomics (HeLa, short-term):** 6,655 proteins quantified; **34** significantly changed (**21 down**, **13 up**). (schorr2020identificationofsignal pages 3-7)
- **Proteomics (HEK293, deficiency):** **302 proteins** altered (**199 down**, **103 up**); **22 shared Sec62/Sec63 clients** (11 SP, 11 TMH). (lang2022signalpeptidefeatures pages 19-21, schorr2020identificationofsignal pages 7-8)
- **ADPLD explained fraction:** known ADPLD genes account for only **~30–45%** of cases. (boerrigter2023heterozygosityofalg9 pages 8-10)
- **Severe PLD cohort (Japan 2024):** 49 enrolled; **44/49 (90%)** genetically solved; **SEC63 1/44 (2%)** among solved; ADPLD-related genes collectively **20%**. (mizuno2024geneticanalysisof pages 1-2)

## 10. Evidence summary table
The following artifact consolidates the evidence for SEC63 functional annotation, including domains, mechanism, substrate specificity, localization, and disease links, plus 2023–2024 clinical updates.

| Aspect | Key points | Representative evidence & quantitative data | Key sources with year, DOI URL, and citeable context IDs |
|---|---|---|---|
| identity/domains/topology | Target identity matches **human SEC63 / DNAJC23 / SEC63L**, the mammalian homolog of yeast Sec63 and a component of the **Sec61-associated Sec62/Sec63 translocon**. Evidence supports a **J-domain protein** with additional **G/F region** and conserved Sec63/Brl/FN3-containing architecture inferred from human and ortholog studies. | Human evidence identifies an **N-terminal J-domain (aa 23–91)** and **G/F domain (aa 92–127)** in SEC63. Review/structural evidence from conserved eukaryotic Sec63 describes an **integral ER membrane protein with 3 TMs**, **N-terminus luminal**, **C-terminus cytosolic**, a **luminal J-domain between TM2 and TM3**, and a **large cytosolic C-terminal Brl/FN3-containing region** that contacts Sec61. Human Sec63 is explicitly described as the human homolog of yeast Sec63 and a defined component of the Sec61/Sec62/Sec63 complex. (schorr2020identificationofsignal pages 13-14, jung2021emergingviewon pages 4-7, itskanov2019structureofthe pages 1-2, jung2021emergingviewon pages 7-9) | Schorr et al. 2020, https://doi.org/10.1111/febs.15274 (schorr2020identificationofsignal pages 13-14); Jung & Kim 2021, https://doi.org/10.3390/ijms222312757 (jung2021emergingviewon pages 4-7, jung2021emergingviewon pages 7-9); Itskanov & Park 2019, https://doi.org/10.1126/science.aav6740 (itskanov2019structureofthe pages 1-2) |
| molecular function | SEC63 is an **ER translocon accessory factor / protein translocation regulator**, not an enzyme. Its primary function is to assist **Sec61 channel gating** and **ER import/insertion** of selected secretory and membrane protein precursors. | Sec63 is reported to sit at the **back-side/cytosolic side of Sec61** and **widen/open the Sec61 pore/lateral gate**. Structural evidence indicates Sec63 interactions with Sec61 “prime” the channel for translocation of **low-hydrophobicity signal sequences**. Functional depletion studies show impaired translocation of specific substrates such as **preproapelin**, and Sec63 is described as mediating translocation of **broader types of precursors than Sec62**. (jung2021emergingviewon pages 9-10, wu2019structureofthe pages 1-2, jung2021emergingviewon pages 7-9) | Wu et al. 2019, https://doi.org/10.1038/s41586-018-0856-x (wu2019structureofthe pages 1-2); Jung & Kim 2021, https://doi.org/10.3390/ijms222312757 (jung2021emergingviewon pages 7-9, jung2021emergingviewon pages 9-10) |
| mechanism with BiP | SEC63 functions as a **J-domain/Hsp40-type co-chaperone** that cooperates with **BiP (ER Hsp70)** during ER translocation. | Human complementation/functional evidence shows SEC63 contains a **J-domain** required for translocation of ERj3, and depletion of **Sec62, Sec63, or BiP** causes accumulation of pre-ERj3 precursor. Reviews propose that Sec63 supports Sec61 opening **by recruiting BiP to Sec61α loop 7** and/or by direct effects on Sec61 gating. Conserved ortholog structural work shows the **luminal J-domain activates BiP** to bind incoming substrates and prevent backsliding. (schorr2020identificationofsignal pages 13-14, lang2022signalpeptidefeatures pages 19-21, wu2019structureofthe pages 1-2, jung2021emergingviewon pages 4-7) | Schorr et al. 2020, https://doi.org/10.1111/febs.15274 (schorr2020identificationofsignal pages 13-14); Lang et al. 2022, https://doi.org/10.3389/fphys.2022.833540 (lang2022signalpeptidefeatures pages 19-21); Wu et al. 2019, https://doi.org/10.1038/s41586-018-0856-x (wu2019structureofthe pages 1-2); Jung & Kim 2021, https://doi.org/10.3390/ijms222312757 (jung2021emergingviewon pages 4-7) |
| substrate specificity | SEC63-dependent clients are enriched for precursors with **weak/slowly gating signal peptides** and sometimes **positively charged mature-region clusters** downstream of the signal peptide. | In intact human cells, one study identified **22 novel Sec62/Sec63 substrates** in addition to confirming ERj3. Shared features included **longer but less hydrophobic SP H-regions** and **lower SP C-region polarity**; a weak SP plus a downstream positive cluster can drive dependence. Quantitative proteomics in HEK293 cells showed **302 proteins affected by Sec63 deficiency** (**199 decreased, 103 increased**), with **22 precursor polypeptides negatively affected by both Sec62 and Sec63** (**11 with SP, 11 with TMH**). In a shorter HeLa knockdown experiment, **6,655 proteins** were quantified and only **34 changed significantly** (**21 decreased, 13 increased**), with enrichment among decreased proteins for **SPs (2-fold)**, **N-glycoproteins (2.6-fold)**, and **membrane proteins (2.8-fold)**. (lang2022signalpeptidefeatures pages 19-21, schorr2020identificationofsignal pages 3-7, schorr2020identificationofsignal pages 7-8) | Schorr et al. 2020, https://doi.org/10.1111/febs.15274 (schorr2020identificationofsignal pages 3-7, schorr2020identificationofsignal pages 7-8); Lang et al. 2022, https://doi.org/10.3389/fphys.2022.833540 (lang2022signalpeptidefeatures pages 19-21) |
| localization | SEC63 is an **endoplasmic reticulum membrane** protein acting at the **ER translocon**; topology places the **J-domain in the ER lumen** and a large **cytosolic C-terminus** on the cytosolic face. | Human and conserved eukaryotic evidence place Sec63 in the **ER membrane** associated with **Sec61 and Sec62**. The C-terminal region mediates **cytosolic interactions** (e.g., with Sec62 and nucleoredoxin), whereas the **J-domain is luminal** and functionally linked to BiP. Co-immunoprecipitation identified lumenal partners such as **calumenin** and **reticulocalbin**, consistent with ER-lumen exposure of part of the protein. (jung2021emergingviewon pages 4-7, jung2021emergingviewon pages 9-10, jung2021emergingviewon pages 7-9) | Jung & Kim 2021, https://doi.org/10.3390/ijms222312757 (jung2021emergingviewon pages 4-7, jung2021emergingviewon pages 7-9, jung2021emergingviewon pages 9-10) |
| disease association ADPLD | Heterozygous **loss-of-function SEC63 variants** are a well-established cause of **autosomal dominant polycystic liver disease (ADPLD)** / isolated polycystic liver disease. Mechanistically, SEC63 belongs to the ER quality-control/translocation group of PLD genes that affect maturation/abundance of polycystin proteins. | Open Targets lists SEC63 associations with **autosomal dominant polycystic liver disease**, **polycystic liver disease 1**, and **isolated polycystic liver disease**. Reviews state that **PRKCSH and SEC63 are the two major ADPLD genes**. PLD reviews further note that ER quality-control genes including **SEC63** can impair production/function of **PC1/PC2** or facilitate their degradation, promoting hepatic cystogenesis. Clinical overviews report the most prevalent genes in isolated PLD are **PRKCSH and SEC63**, accounting together for about **20%–41%** of cases in cited literature. (OpenTargets Search: -SEC63, daverkausenfischer2024erresidentcochaperonesin pages 112-114) | Open Targets SEC63 associations (OpenTargets Search: -SEC63); Mahboobipour et al. 2024, https://doi.org/10.1186/s13023-024-03187-w (daverkausenfischer2024erresidentcochaperonesin pages 112-114); Jeong & Park 2023, https://doi.org/10.7180/kmj.23.128 (daverkausenfischer2024erresidentcochaperonesin pages 112-114); Yang et al. 2023, https://doi.org/10.1053/j.akdh.2023.04.004 (daverkausenfischer2024erresidentcochaperonesin pages 112-114) |
| recent research/2023-2024 clinical genetics & cohorts | Recent literature emphasizes **clinical genetics**, **cohort-based etiology**, and broader PLD mechanisms rather than brand-new SEC63 molecular biochemistry. | A 2024 Japanese severe-PLD cohort sequenced **49 patients** and found pathogenic/suspected pathogenic variants in **44/49 (90%)**. Gene distribution among solved cases: **PKD1 20/44 (45%)**, **PKD2 15/44 (34%)**, **PRKCSH 5/44 (11%)**, **GANAB 2/44 (5%)**, **SEC63 1/44 (2%)**, **ALG8 1/44 (2%)**; authors concluded **ADPLD-related genes represented 20%** of severe PLD cases. A 2023 genetics review states **PRKCSH and SEC63 are the two major ADPLD genes**, and recommends **next-generation sequencing panels** for overlapping PKD/PLD phenotypes. A 2023 translational study found a conserved **TGFβ–ECM–integrin axis** across human liver cysts from ADPKD and ADPLD, highlighting downstream pathways shared across causal genes including ER-translocation genes such as SEC63. (daverkausenfischer2024erresidentcochaperonesin pages 112-114) | Mizuno et al. 2024, https://doi.org/10.34067/kid.0000000000000461 (daverkausenfischer2024erresidentcochaperonesin pages 112-114); Yang et al. 2023, https://doi.org/10.1053/j.akdh.2023.04.004 (daverkausenfischer2024erresidentcochaperonesin pages 112-114); Waddell et al. 2023, https://doi.org/10.1126/scitranslmed.abq5930 (daverkausenfischer2024erresidentcochaperonesin pages 112-114) |


*Table: This table summarizes evidence-based functional annotation for human SEC63 (UniProt Q9UGP8), focusing on its translocon role, BiP-linked mechanism, substrate specificity, localization, and polycystic liver disease relevance. It highlights both mechanistic studies and recent 2023–2024 clinical genetics data.*

## 11. Key URLs (publication date prioritized where available)
- Itskanov & Park. *Mechanism of Protein Translocation by the Sec61 Translocon Complex.* Cold Spring Harbor Perspect Biol. **Aug 2023**. https://doi.org/10.1101/cshperspect.a041250 (itskanov2023mechanismofprotein pages 1-3)
- Mizuno et al. *Genetic Analysis of Severe Polycystic Liver Disease in Japan.* Kidney360. **May 2024**. https://doi.org/10.34067/kid.0000000000000461 (mizuno2024geneticanalysisof pages 1-2)
- Mahboobipour et al. *Clinical manifestation, epidemiology, genetic basis, potential molecular targets, and current treatment of polycystic liver disease.* Orphanet J Rare Dis. **Apr 2024**. https://doi.org/10.1186/s13023-024-03187-w (mahboobipour2024clinicalmanifestationepidemiology pages 1-2)
- Yang et al. *Genetic Spectrum of Polycystic Kidney and Liver Diseases and the Resulting Phenotypes.* Adv Kidney Dis Health. **Sep 2023**. https://doi.org/10.1053/j.akdh.2023.04.004 (yang2023geneticspectrumof pages 1-3)
- Boerrigter et al. *Heterozygosity of ALG9 in Association with Autosomal Dominant Polycystic Liver Disease.* Genes. **Sep 2023**. https://doi.org/10.3390/genes14091755 (boerrigter2023heterozygosityofalg9 pages 8-10)
- Schorr et al. *Identification of signal peptide features for substrate specificity in human Sec62/Sec63-dependent ER protein import.* FEBS J. **Mar 2020**. https://doi.org/10.1111/febs.15274 (schorr2020identificationofsignal pages 3-7)
- O’Keefe & High. *Membrane translocation at the ER: with a little help from my friends.* FEBS J. **Apr 2020**. https://doi.org/10.1111/febs.15309 (okeefe2020membranetranslocationat pages 1-3)

## 12. Limitations and notes on evidence scope
- Several mechanistic structural statements about Sec63 (e.g., three-TM architecture, pore opening) are derived from **yeast Sec complex cryo-EM** and interpreted as conserved for metazoans; direct high-resolution structures of the full mammalian Sec62/Sec63/Sec61 assembly were not retrieved in the current evidence set. (itskanov2019structureofthe pages 1-2, wu2019structureofthe pages 1-2)
- SEC63 clinical genetics is well represented in 2023–2024 reviews and cohorts, but primary 2004–2012 discovery papers for SEC63-linked ADPLD were not retrieved as full text here; conclusions are therefore based on recent review synthesis and modern cohorts plus explicit LOH statements from 2023 literature. (boerrigter2023heterozygosityofalg9 pages 8-10, yang2023geneticspectrumof pages 1-3)


References

1. (lang2022signalpeptidefeatures pages 19-21): Sven Lang, Duy Nguyen, Pratiti Bhadra, Martin Jung, Volkhard Helms, and Richard Zimmermann. Signal peptide features determining the substrate specificities of targeting and translocation components in human er protein import. Frontiers in Physiology, Jul 2022. URL: https://doi.org/10.3389/fphys.2022.833540, doi:10.3389/fphys.2022.833540. This article has 31 citations.

2. (schorr2020identificationofsignal pages 13-14): Stefan Schorr, Duy Nguyen, Sarah Haßdenteufel, Nagarjuna Nagaraj, Adolfo Cavalié, Markus Greiner, Petra Weissgerber, Marisa Loi, Adrienne W. Paton, James C. Paton, Maurizio Molinari, Friedrich Förster, Johanna Dudek, Sven Lang, Volkhard Helms, and Richard Zimmermann. Identification of signal peptide features for substrate specificity in human sec62/sec63‐dependent er protein import. The FEBS Journal, 287:4612-4640, Mar 2020. URL: https://doi.org/10.1111/febs.15274, doi:10.1111/febs.15274. This article has 51 citations.

3. (jung2021emergingviewon pages 9-10): Sung-jun Jung and Hyun Kim. Emerging view on the molecular functions of sec62 and sec63 in protein translocation. International Journal of Molecular Sciences, 22:12757, Nov 2021. URL: https://doi.org/10.3390/ijms222312757, doi:10.3390/ijms222312757. This article has 38 citations.

4. (yang2023geneticspectrumof pages 1-3): Hana Yang, Cynthia J. Sieben, Rachel S. Schauer, and Peter C. Harris. Genetic spectrum of polycystic kidney and liver diseases and the resulting phenotypes. Advances in kidney disease and health, 30 5:397-406, Sep 2023. URL: https://doi.org/10.1053/j.akdh.2023.04.004, doi:10.1053/j.akdh.2023.04.004. This article has 30 citations.

5. (itskanov2023mechanismofprotein pages 1-3): Samuel Itskanov and Eunyong Park. Mechanism of protein translocation by the sec61 translocon complex. Cold Spring Harbor perspectives in biology, 15:a041250, Aug 2023. URL: https://doi.org/10.1101/cshperspect.a041250, doi:10.1101/cshperspect.a041250. This article has 66 citations and is from a peer-reviewed journal.

6. (okeefe2020membranetranslocationat pages 1-3): Sarah O'Keefe and Stephen High. Membrane translocation at the er: with a little help from my friends. The FEBS Journal, 287:4607-4611, Apr 2020. URL: https://doi.org/10.1111/febs.15309, doi:10.1111/febs.15309. This article has 14 citations.

7. (jung2021emergingviewon pages 1-3): Sung-jun Jung and Hyun Kim. Emerging view on the molecular functions of sec62 and sec63 in protein translocation. International Journal of Molecular Sciences, 22:12757, Nov 2021. URL: https://doi.org/10.3390/ijms222312757, doi:10.3390/ijms222312757. This article has 38 citations.

8. (itskanov2019structureofthe pages 1-2): Samuel Itskanov and Eunyong Park. Structure of the posttranslational sec protein-translocation channel complex from yeast. Science, 363:84-87, Jan 2019. URL: https://doi.org/10.1126/science.aav6740, doi:10.1126/science.aav6740. This article has 106 citations and is from a highest quality peer-reviewed journal.

9. (wu2019structureofthe pages 1-2): Xudong Wu, Cerrone Cabanos, and Tom A. Rapoport. Structure of the post-translational protein translocation machinery of the er membrane. Dec 2019. URL: https://doi.org/10.1038/s41586-018-0856-x, doi:10.1038/s41586-018-0856-x. This article has 150 citations and is from a highest quality peer-reviewed journal.

10. (jung2021emergingviewon pages 7-9): Sung-jun Jung and Hyun Kim. Emerging view on the molecular functions of sec62 and sec63 in protein translocation. International Journal of Molecular Sciences, 22:12757, Nov 2021. URL: https://doi.org/10.3390/ijms222312757, doi:10.3390/ijms222312757. This article has 38 citations.

11. (schorr2020identificationofsignal pages 3-7): Stefan Schorr, Duy Nguyen, Sarah Haßdenteufel, Nagarjuna Nagaraj, Adolfo Cavalié, Markus Greiner, Petra Weissgerber, Marisa Loi, Adrienne W. Paton, James C. Paton, Maurizio Molinari, Friedrich Förster, Johanna Dudek, Sven Lang, Volkhard Helms, and Richard Zimmermann. Identification of signal peptide features for substrate specificity in human sec62/sec63‐dependent er protein import. The FEBS Journal, 287:4612-4640, Mar 2020. URL: https://doi.org/10.1111/febs.15274, doi:10.1111/febs.15274. This article has 51 citations.

12. (schorr2020identificationofsignal pages 7-8): Stefan Schorr, Duy Nguyen, Sarah Haßdenteufel, Nagarjuna Nagaraj, Adolfo Cavalié, Markus Greiner, Petra Weissgerber, Marisa Loi, Adrienne W. Paton, James C. Paton, Maurizio Molinari, Friedrich Förster, Johanna Dudek, Sven Lang, Volkhard Helms, and Richard Zimmermann. Identification of signal peptide features for substrate specificity in human sec62/sec63‐dependent er protein import. The FEBS Journal, 287:4612-4640, Mar 2020. URL: https://doi.org/10.1111/febs.15274, doi:10.1111/febs.15274. This article has 51 citations.

13. (mahboobipour2024clinicalmanifestationepidemiology pages 1-2): Amir Ali Mahboobipour, Moein Ala, Javad Safdari Lord, and Arash Yaghoobi. Clinical manifestation, epidemiology, genetic basis, potential molecular targets, and current treatment of polycystic liver disease. Orphanet Journal of Rare Diseases, Apr 2024. URL: https://doi.org/10.1186/s13023-024-03187-w, doi:10.1186/s13023-024-03187-w. This article has 20 citations and is from a peer-reviewed journal.

14. (mizuno2024geneticanalysisof pages 1-2): Hiroki Mizuno, Whitney Besse, Akinari Sekine, Kelly T. Long, Shigekazu Kurihara, Yuki Oba, Masayuki Yamanouchi, Eiko Hasegawa, Tatsuya Suwabe, Naoki Sawa, Yoshifumi Ubara, Stefan Somlo, and Junichi Hoshino. Genetic analysis of severe polycystic liver disease in japan. Kidney360, 5:1106-1115, May 2024. URL: https://doi.org/10.34067/kid.0000000000000461, doi:10.34067/kid.0000000000000461. This article has 1 citations and is from a peer-reviewed journal.

15. (mizuno2024geneticanalysisof media 7f91773b): Hiroki Mizuno, Whitney Besse, Akinari Sekine, Kelly T. Long, Shigekazu Kurihara, Yuki Oba, Masayuki Yamanouchi, Eiko Hasegawa, Tatsuya Suwabe, Naoki Sawa, Yoshifumi Ubara, Stefan Somlo, and Junichi Hoshino. Genetic analysis of severe polycystic liver disease in japan. Kidney360, 5:1106-1115, May 2024. URL: https://doi.org/10.34067/kid.0000000000000461, doi:10.34067/kid.0000000000000461. This article has 1 citations and is from a peer-reviewed journal.

16. (mizuno2024geneticanalysisof media 3666ec3e): Hiroki Mizuno, Whitney Besse, Akinari Sekine, Kelly T. Long, Shigekazu Kurihara, Yuki Oba, Masayuki Yamanouchi, Eiko Hasegawa, Tatsuya Suwabe, Naoki Sawa, Yoshifumi Ubara, Stefan Somlo, and Junichi Hoshino. Genetic analysis of severe polycystic liver disease in japan. Kidney360, 5:1106-1115, May 2024. URL: https://doi.org/10.34067/kid.0000000000000461, doi:10.34067/kid.0000000000000461. This article has 1 citations and is from a peer-reviewed journal.

17. (mizuno2024geneticanalysisof media 669179d2): Hiroki Mizuno, Whitney Besse, Akinari Sekine, Kelly T. Long, Shigekazu Kurihara, Yuki Oba, Masayuki Yamanouchi, Eiko Hasegawa, Tatsuya Suwabe, Naoki Sawa, Yoshifumi Ubara, Stefan Somlo, and Junichi Hoshino. Genetic analysis of severe polycystic liver disease in japan. Kidney360, 5:1106-1115, May 2024. URL: https://doi.org/10.34067/kid.0000000000000461, doi:10.34067/kid.0000000000000461. This article has 1 citations and is from a peer-reviewed journal.

18. (boerrigter2023heterozygosityofalg9 pages 8-10): Melissa M. Boerrigter, Renée Duijzer, René H. M. te Morsche, and Joost P. H. Drenth. Heterozygosity of alg9 in association with autosomal dominant polycystic liver disease. Genes, 14:1755, Sep 2023. URL: https://doi.org/10.3390/genes14091755, doi:10.3390/genes14091755. This article has 4 citations.

19. (boerrigter2023novelα13glucosyltransferasevariants pages 2-3): Melissa M. Boerrigter, René H. M. te Morsche, Hanka Venselaar, Nikki Pastoors, Anja M. Geerts, Anne Hoorens, and Joost P. H. Drenth. Novel α-1,3-glucosyltransferase variants and their broad clinical polycystic liver disease spectrum. Genes, 14:1652, Aug 2023. URL: https://doi.org/10.3390/genes14081652, doi:10.3390/genes14081652. This article has 3 citations.

20. (jung2021emergingviewon pages 4-7): Sung-jun Jung and Hyun Kim. Emerging view on the molecular functions of sec62 and sec63 in protein translocation. International Journal of Molecular Sciences, 22:12757, Nov 2021. URL: https://doi.org/10.3390/ijms222312757, doi:10.3390/ijms222312757. This article has 38 citations.

21. (OpenTargets Search: -SEC63): Open Targets Query (-SEC63, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

22. (daverkausenfischer2024erresidentcochaperonesin pages 112-114): LV Daverkausen-Fischer. Er-resident co-chaperones in mammalian cells a critical analysis of experimental data published on structure, localization, regulation and function. Unknown journal, 2024.

## Artifacts

- [Edison artifact artifact-00](SEC63-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000016 The requested visual summaries can be found in Figure 2 and Table 1 of the document. - **Figure 2** is a pie chart that displays th](SEC63-deep-research-falcon_artifacts/image-1.png)

## Citations

1. itskanov2023mechanismofprotein pages 1-3
2. okeefe2020membranetranslocationat pages 1-3
3. schorr2020identificationofsignal pages 13-14
4. jung2021emergingviewon pages 9-10
5. schorr2020identificationofsignal pages 3-7
6. mizuno2024geneticanalysisof pages 1-2
7. mahboobipour2024clinicalmanifestationepidemiology pages 1-2
8. itskanov2019structureofthe pages 1-2
9. wu2019structureofthe pages 1-2
10. lang2022signalpeptidefeatures pages 19-21
11. jung2021emergingviewon pages 4-7
12. daverkausenfischer2024erresidentcochaperonesin pages 112-114
13. yang2023geneticspectrumof pages 1-3
14. jung2021emergingviewon pages 1-3
15. jung2021emergingviewon pages 7-9
16. schorr2020identificationofsignal pages 7-8
17. https://doi.org/10.1111/febs.15274
18. https://doi.org/10.3390/ijms222312757
19. https://doi.org/10.1126/science.aav6740
20. https://doi.org/10.1038/s41586-018-0856-x
21. https://doi.org/10.3389/fphys.2022.833540
22. https://doi.org/10.1186/s13023-024-03187-w
23. https://doi.org/10.7180/kmj.23.128
24. https://doi.org/10.1053/j.akdh.2023.04.004
25. https://doi.org/10.34067/kid.0000000000000461
26. https://doi.org/10.1126/scitranslmed.abq5930
27. https://doi.org/10.1101/cshperspect.a041250
28. https://doi.org/10.3390/genes14091755
29. https://doi.org/10.1111/febs.15309
30. https://doi.org/10.3389/fphys.2022.833540,
31. https://doi.org/10.1111/febs.15274,
32. https://doi.org/10.3390/ijms222312757,
33. https://doi.org/10.1053/j.akdh.2023.04.004,
34. https://doi.org/10.1101/cshperspect.a041250,
35. https://doi.org/10.1111/febs.15309,
36. https://doi.org/10.1126/science.aav6740,
37. https://doi.org/10.1038/s41586-018-0856-x,
38. https://doi.org/10.1186/s13023-024-03187-w,
39. https://doi.org/10.34067/kid.0000000000000461,
40. https://doi.org/10.3390/genes14091755,
41. https://doi.org/10.3390/genes14081652,