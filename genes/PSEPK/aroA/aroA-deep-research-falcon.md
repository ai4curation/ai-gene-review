---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T20:39:52.113426'
end_time: '2026-06-11T20:52:12.952603'
duration_seconds: 740.84
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: aroA
  gene_symbol: aroA
  uniprot_accession: Q88M05
  protein_description: 'RecName: Full=3-phosphoshikimate 1-carboxyvinyltransferase
    {ECO:0000256|HAMAP-Rule:MF_00210}; EC=2.5.1.19 {ECO:0000256|HAMAP-Rule:MF_00210};
    AltName: Full=5-enolpyruvylshikimate-3-phosphate synthase {ECO:0000256|HAMAP-Rule:MF_00210};
    Short=EPSP synthase {ECO:0000256|HAMAP-Rule:MF_00210}; Short=EPSPS {ECO:0000256|HAMAP-Rule:MF_00210};'
  gene_info: Name=aroA {ECO:0000256|HAMAP-Rule:MF_00210}; OrderedLocusNames=PP_1770
    {ECO:0000313|EMBL:AAN67390.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the prephenate/arogenate dehydrogenase family.
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); Enolpyruvate_Tfrase_dom.
    (IPR001986); Enolpyruvate_Tfrase_sf. (IPR036968); EPSP_synthase. (IPR006264);
    EPSP_synthase_CS. (IPR023193)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: aroA-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88M05
- **Protein Description:** RecName: Full=3-phosphoshikimate 1-carboxyvinyltransferase {ECO:0000256|HAMAP-Rule:MF_00210}; EC=2.5.1.19 {ECO:0000256|HAMAP-Rule:MF_00210}; AltName: Full=5-enolpyruvylshikimate-3-phosphate synthase {ECO:0000256|HAMAP-Rule:MF_00210}; Short=EPSP synthase {ECO:0000256|HAMAP-Rule:MF_00210}; Short=EPSPS {ECO:0000256|HAMAP-Rule:MF_00210};
- **Gene Information:** Name=aroA {ECO:0000256|HAMAP-Rule:MF_00210}; OrderedLocusNames=PP_1770 {ECO:0000313|EMBL:AAN67390.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the prephenate/arogenate dehydrogenase family.
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); Enolpyruvate_Tfrase_dom. (IPR001986); Enolpyruvate_Tfrase_sf. (IPR036968); EPSP_synthase. (IPR006264); EPSP_synthase_CS. (IPR023193)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aroA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aroA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aroA** (gene ID: aroA, UniProt: Q88M05) in PSEPK.

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
- **UniProt Accession:** Q88M05
- **Protein Description:** RecName: Full=3-phosphoshikimate 1-carboxyvinyltransferase {ECO:0000256|HAMAP-Rule:MF_00210}; EC=2.5.1.19 {ECO:0000256|HAMAP-Rule:MF_00210}; AltName: Full=5-enolpyruvylshikimate-3-phosphate synthase {ECO:0000256|HAMAP-Rule:MF_00210}; Short=EPSP synthase {ECO:0000256|HAMAP-Rule:MF_00210}; Short=EPSPS {ECO:0000256|HAMAP-Rule:MF_00210};
- **Gene Information:** Name=aroA {ECO:0000256|HAMAP-Rule:MF_00210}; OrderedLocusNames=PP_1770 {ECO:0000313|EMBL:AAN67390.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the prephenate/arogenate dehydrogenase family.
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); Enolpyruvate_Tfrase_dom. (IPR001986); Enolpyruvate_Tfrase_sf. (IPR036968); EPSP_synthase. (IPR006264); EPSP_synthase_CS. (IPR023193)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aroA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aroA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aroA** (gene ID: aroA, UniProt: Q88M05) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: Functional annotation of **aroA / EPSP synthase** (UniProt **Q88M05**) in *Pseudomonas putida* KT2440

### Executive summary
The UniProt target **Q88M05** is annotated as **3‑phosphoshikimate 1‑carboxyvinyltransferase** (EC **2.5.1.19**), also called **5‑enolpyruvylshikimate‑3‑phosphate synthase (EPSPS)**, classically encoded by **aroA**. EPSPS catalyzes the transfer of the enolpyruvyl group from **phosphoenolpyruvate (PEP)** to **shikimate‑3‑phosphate (S3P)** to form **5‑enolpyruvylshikimate‑3‑phosphate (EPSP)** and **inorganic phosphate**, a penultimate step in the **shikimate pathway** leading to chorismate and aromatic amino acids. A key caveat for *P. putida* KT2440 is that historical pathway depictions contain an **annotation inconsistency** in which **PP1770** is labeled as “TyrA” and simultaneously described with an EPSPS-like name; this should not be conflated with the well-established bacterial meaning of **aroA = EPSPS**. The most direct KT2440-specific functional evidence recovered here is **pathway-engineering phenotypes**: tuning **aroA expression** affected flux to the aromatic-derived product **p‑aminobenzoic acid (pABA)**. 

### Target verification and ambiguity handling (critical)
**Verified target (user-supplied UniProt context):** UniProt **Q88M05**, gene name **aroA**, ordered locus **PP_1770**, organism ***Pseudomonas putida* KT2440**.

**Detected ambiguity in KT2440 literature:** In a KT2440 aromatic-pathway analysis, **PP1770** was presented in a pathway context as “**PP1770 or TyrA**” and described with dual functional labels including “**prephenate dehydrogenase, putative/3‑phosphoshikimate 1‑carboxyvinyltransferase**.” (molinahenares2009functionalanalysisof pages 2-4). This conflicts with the conventional assignment of **tyrA** to prephenate dehydrogenase and **aroA** to EPSPS, and it implies historical misannotation or figure-level conflation. Accordingly, this report treats **Q88M05 as aroA/EPSPS** (per UniProt target identity) and uses KT2440 papers only for statements they explicitly support.

| Category | Details | Quantitative data | Key sources (year; URL) | Notes |
|---|---|---:|---|---|
| Verified target identity | **UniProt Q88M05**; gene **aroA**; ordered locus **PP_1770**; organism **Pseudomonas putida KT2440** | — | Molina-Henares et al. 2009; https://doi.org/10.1111/j.1751-7915.2008.00062.x (molinahenares2009functionalanalysisof pages 2-4) | Literature for PP1770 in KT2440 exists, but direct biochemical characterization of Q88M05 in the retrieved sources is limited. |
| Core enzymatic function | **3-phosphoshikimate 1-carboxyvinyltransferase / 5-enolpyruvylshikimate-3-phosphate synthase (EPSPS; EC 2.5.1.19)** catalyzes **shikimate-3-phosphate (S3P) + phosphoenolpyruvate (PEP) → 5-enolpyruvylshikimate-3-phosphate (EPSP) + inorganic phosphate** | Reaction stoichiometry shown; glyphosate can inhibit by occupying the PEP site | Shende et al. 2024; https://doi.org/10.1039/d3np00037k (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 50-64) | Current mechanistic understanding places EPSPS as an enolpyruvyl transferase acting through a tetrahedral intermediate; glyphosate is a competitive PEP-site inhibitor. |
| Pathway context | EPSPS performs the **penultimate step of the shikimate pathway**, leading to **chorismate**, the common precursor for **phenylalanine, tyrosine, and tryptophan** biosynthesis | — | Shende et al. 2024; https://doi.org/10.1039/d3np00037k (shende2024theshikimatepathway pages 10-11); Molina-Henares et al. 2009; https://doi.org/10.1111/j.1751-7915.2008.00062.x (molinahenares2009functionalanalysisof pages 2-4) | In bacteria this is a **cytosolic metabolic enzyme** in central aromatic amino-acid biosynthesis, inferred from pathway/structural context (shende2024theshikimatepathway pages 50-64). |
| Annotation inconsistency to flag | PP1770 was reported in one KT2440 pathway source as **“PP1770 or TyrA”** with dual/ambiguous labeling including **“prephenate dehydrogenase, putative/3-phosphoshikimate 1-carboxyvinyltransferase”** | — | Molina-Henares et al. 2009; https://doi.org/10.1111/j.1751-7915.2008.00062.x (molinahenares2009functionalanalysisof pages 2-4) | This is the main inconsistency that requires caution; the user-supplied UniProt entry specifically identifies Q88M05 as **aroA/EPSPS**, so literature must not be conflated with true **tyrA/prephenate dehydrogenase** studies. |
| P. putida KT2440 engineering relevance | In KT2440 pABA pathway optimization, **aroA** was included among shikimate-pathway genes tuned by combinatorial expression to improve production | Best strain produced **185.4 mg/L pABA**; lowering aroA/aroK/aroQ/aroGD146N expression to native levels caused a **39.9% decrease** in pABA in top strain S12 | Campos-Magaña et al. 2025; https://doi.org/10.1186/s13036-025-00553-5 (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6, camposmagana2025combinatorialengineeringpinpoints pages 8-9) | Evidence supports aroA as a practical flux-control point in aromatic-pathway engineering in **P. putida**, although **aroB** was highlighted as the stronger bottleneck in that study. |
| Recent EPSPS developments (general) | Directed evolution platforms are being used to obtain EPSPS variants with both catalytic competence and glyphosate tolerance | One evolved EPSPS variant reached **Ki ≈ 1 mM** for glyphosate and **~2.5-fold improved enzymatic efficiency** versus the starting enzyme | Reed et al. 2024; https://doi.org/10.1073/pnas.2317027121 (reed2024evolvingdualtraitepsp pages 1-2) | This is not P. putida-specific, but it is highly relevant to modern functional interpretation and real-world use of EPSPS enzymes. |
| Recent mechanistic expansion (general) | A 2024 study showed **MurA** can also catalyze **S3P + PEP → EPSP + Pi** in bryophytes, revealing an alternative route to EPSP formation | MurA activity was **~100-fold lower** than EPSPS; MurA activity on S3P/PEP was **~8-fold higher** than on its canonical substrate pair | Caygill et al. 2024; https://doi.org/10.1073/pnas.2412997121 (caygill2024muracatalyzedsynthesisof pages 1-2, caygill2024muracatalyzedsynthesisof pages 6-7) | Important for interpreting glyphosate tolerance biology broadly; not evidence that KT2440 uses MurA for this role. |
| Glyphosate resistance relevance | In bacteria, resistance can arise through **target-site aroA mutations**, **EPSPS overproduction/gene amplification**, **transport/efflux changes**, or **glyphosate degradation/detoxification** | Example selection range for Salmonella target-site mutants: **0.35–2 g/L glyphosate** | Hertel et al. 2021; https://doi.org/10.1111/1462-2920.15534 (hertel2021molecularmechanismsunderlying pages 1-5, hertel2021molecularmechanismsunderlying pages 24-27, hertel2021molecularmechanismsunderlying pages 5-8, hertel2021molecularmechanismsunderlying pages 12-15) | These mechanisms frame how aroA function is exploited or bypassed under herbicide pressure. |


*Table: This table summarizes the verified identity, biochemical function, pathway role, annotation caveats, and applied relevance of the target protein UniProt Q88M05 / aroA / PP_1770 from Pseudomonas putida KT2440. It also includes recent quantitative findings useful for interpreting EPSPS function and engineering significance.*

### 1) Key concepts and definitions (current understanding)

#### 1.1 Enzyme name and EC definition
**EPSP synthase (EPSPS; EC 2.5.1.19)** is an enolpyruvyl transferase in the shikimate pathway that catalyzes:

**S3P + PEP → EPSP + Pi**

This penultimate step installs a second PEP-derived unit onto the shikimate scaffold to form EPSP, which is then converted to **chorismate** in the final shikimate-pathway step (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 50-64).

#### 1.2 Mechanism and inhibitor biology
A 2024 authoritative review describes EPSPS as an “alkyl transferase-type enzyme” operating through a **tetrahedral intermediate**, and emphasizes that EPSPS catalysis involves **C–O bond cleavage of PEP** (unusual among many PEP-utilizing enzymes, which often cleave P–O bonds) (shende2024theshikimatepathway pages 10-11). 

EPSPS is also the canonical molecular target of **glyphosate**, which competitively occupies the **PEP binding site**, thereby preventing normal turnover and starving the cell of downstream aromatic amino acids (shende2024theshikimatepathway pages 10-11, hertel2021molecularmechanismsunderlying pages 1-5).

#### 1.3 Enzyme classes (sequence/phenotype concepts)
The same 2024 review summarizes three EPSPS “classes”: **Class I** (often glyphosate-sensitive; found in plants and some bacteria), **Class II** (microbial; variable sensitivity), and **Class III** (microbial; low identity to *E. coli* EPSPS) (shende2024theshikimatepathway pages 10-11). This classification is widely used to interpret glyphosate sensitivity and potential resistance routes.

### 2) Biological role and pathway context in bacteria (with localization inference)

#### 2.1 Role in the shikimate pathway and aromatic amino acid synthesis
EPSPS catalyzes the **penultimate** reaction of the shikimate pathway, which produces **chorismate**, the common precursor for **phenylalanine, tyrosine, and tryptophan** biosynthesis (shende2024theshikimatepathway pages 10-11, molinahenares2009functionalanalysisof pages 2-4). Because these amino acids are foundational building blocks and also feed numerous downstream aromatic metabolites, aroA/EPSPS is typically central to anabolic metabolism in bacteria.

#### 2.2 Cellular localization
The retrieved sources do not explicitly state subcellular localization for bacterial EPSPS. However, EPSPS is treated as a **soluble metabolic enzyme** in core carbon/anabolic metabolism, and bacterial structural context (e.g., *E. coli* EPSPS with S3P and glyphosate bound) supports the interpretation that it functions in the **cytosol** rather than in membranes or secretion pathways (shende2024theshikimatepathway pages 50-64).

### 3) *Pseudomonas putida* KT2440-specific evidence (genetics, phenotypes, applications)

#### 3.1 KT2440 genetics/auxotrophy context available in retrieved literature
A genome-wide mutant-library screen in KT2440 identified many **conditionally essential** genes for growth on glucose minimal medium and recovered multiple **aromatic amino-acid auxotrophs**, including mutants in tryptophan biosynthesis genes (trpA/D/C/E/G/F) and downstream aromatic genes such as **pheA** and **tyrA** (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 6-7). In the retrieved text segments, **aroA/EPSPS itself is not explicitly reported** as an identified conditionally essential locus (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 6-7). This absence could reflect library coverage, essentiality preventing recovery, annotation differences, or that aroA is discussed elsewhere (e.g., supplement) not retrieved here.

Separately, an aromatic biosynthesis functional study reports targeted phenotypes for **pheA** and **tyrA** in the PP1769–PP1770 region and documents aromatic amino-acid rescue patterns, but it likewise does not provide direct aroA/EPSPS phenotypes in the supplied pages (molinahenares2009functionalanalysisof pages 6-7).

#### 3.2 Real-world implementation: KT2440 metabolic engineering leveraging aroA
A 2025 *P. putida* study optimizing production of the aromatic-derived compound **p‑aminobenzoic acid (pABA)** explicitly defines **aroA** as EPSPS (“3‑phosphoshikimate‑1‑carboxylvinyl transferase”) and places it in the shikimate pathway step converting **S3P → EPSP** (with PEP as donor) (camposmagana2025combinatorialengineeringpinpoints pages 2-4). 

Using a Design-of-Experiments (Plackett–Burman) combinatorial expression approach across multiple shikimate-pathway genes, pABA titers ranged from ~**2 mg/L** to **186.2 mg/L** in the initial screen (camposmagana2025combinatorialengineeringpinpoints pages 4-6). In their top strain (**S12**), pABA reached **185.40 mg/L**, and reducing expression of **aroA** (together with aroK, aroQ, and aroGD146N) back to native levels caused a **39.9% decrease** in pABA production (p = 0.001) (camposmagana2025combinatorialengineeringpinpoints pages 8-9). This provides KT2440-specific functional evidence that **aroA expression level contributes measurably to aromatic-pathway flux** toward a chorismate-derived product under engineered conditions.

### 4) Recent developments and latest research (prioritizing 2023–2024)

#### 4.1 2024: Directed evolution and structure-guided improvement of EPSPS function under glyphosate
A 2024 PNAS study developed a **synthetic yeast selection system** that enables simultaneous selection for **glyphosate tolerance** and retained/improved **catalytic efficiency** of EPSPS variants (reed2024evolvingdualtraitepsp pages 1-2). The study reports recovery of a mutant enzyme with **Ki near 1 mM** for glyphosate and approximately **2.5-fold improved enzymatic efficiency** relative to the starting enzyme (reed2024evolvingdualtraitepsp pages 1-2). This work illustrates a modern trend: treating EPSPS as an engineerable biocatalyst where the classic “resistance vs activity” tradeoff can be mitigated with selection design and structural interpretation (reed2024evolvingdualtraitepsp pages 1-2, reed2024evolvingdualtraitepsp pages 5-6).

#### 4.2 2024: Alternative enzymology for EPSP formation (MurA promiscuity) and glyphosate tolerance
A second 2024 PNAS study reports that **MurA** (canonically involved in peptidoglycan biosynthesis) can catalyze the **same net reaction as EPSPS** (S3P + PEP → EPSP + Pi) in the bryophyte *Marchantia polymorpha* (caygill2024muracatalyzedsynthesisof pages 1-2). Enzyme assays showed MurA activity on S3P/PEP was **~100-fold lower than EPSPS**, but **~8-fold higher** than MurA’s activity on its canonical UDP-GlcNAc/PEP substrate pair (caygill2024muracatalyzedsynthesisof pages 6-7). Genetic and heterologous-expression evidence linked this alternative activity to **glyphosate tolerance** (caygill2024muracatalyzedsynthesisof pages 1-2). Although this is not a KT2440 result, it expands the conceptual landscape for “EPSP-forming enzymes,” which is relevant when interpreting resistance and evolutionary possibilities.

#### 4.3 2024: Shikimate pathway review consolidating current mechanistic understanding
A 2024 *Natural Product Reports* review synthesizes EPSPS mechanism, inhibitor binding, structural information (including *E. coli* EPSPS complex with glyphosate; PDB 1G6S), and classification of enzyme classes relevant to predicting glyphosate sensitivity in different organisms (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 50-64). This is a high-authority source for current definitions and mechanistic consensus.

### 5) Expert opinions/authoritative synthesis and resistance framework

A domain-leading 2021 *Environmental Microbiology* review frames bacterial glyphosate resistance as arising via four broad mechanisms: (i) **reduced EPSPS sensitivity or increased EPSPS production**, (ii) **degradation** of glyphosate, (iii) **detoxification/modification**, and (iv) altered **transport** (reduced uptake/increased export) (hertel2021molecularmechanismsunderlying pages 1-5). This review provides concrete examples of aroA/EPSPS-associated target-site resistance (e.g., Pro101Ser; Gly96Ala) and emphasizes that **overproduction** (including amplification or promoter-up changes) can effectively titrate glyphosate (hertel2021molecularmechanismsunderlying pages 5-8). It also highlights non-target routes including transport and enzymatic modification (e.g., N-acetylation) that prevent EPSPS inhibition (hertel2021molecularmechanismsunderlying pages 12-15).

Quantitatively, the review reports laboratory selection of *Salmonella* aroA mutants under **0.35–2 g/L glyphosate**, illustrating the selection pressures under which target-site changes can arise (hertel2021molecularmechanismsunderlying pages 5-8).

### 6) Applications and real-world implementations

1. **Industrial/biotech strain engineering of aromatic products:** In *P. putida* KT2440, adjusting expression of shikimate-pathway genes including **aroA** is used to improve yields of chorismate-derived products such as **pABA** (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 8-9). This exemplifies aroA’s practical role as a flux-controlling node in aromatic anabolic pathways.

2. **Glyphosate tolerance engineering:** EPSPS variants (often bacterial-derived such as Agrobacterium CP4 EPSPS) are historically foundational for glyphosate-tolerant crops; modern 2024 work continues to refine EPSPS variants to improve both resistance and activity using high-throughput selection and structural analysis (hertel2021molecularmechanismsunderlying pages 5-8, reed2024evolvingdualtraitepsp pages 1-2).

3. **Environmental/clinical microbiology implications:** Because glyphosate targets EPSPS, environmental exposures can select for bacterial resistance via multiple mechanisms (target-site, transport, detoxification), potentially intersecting with broader stress-adaptation and resistance landscapes (hertel2021molecularmechanismsunderlying pages 1-5).

### 7) Limitations of the current evidence base for this specific UniProt protein
Despite extensive general knowledge on aroA/EPSPS, **direct experimental characterization of UniProt Q88M05 in *P. putida* KT2440** (purified enzyme kinetics, substrate specificity beyond the canonical S3P/PEP reaction, structure, or explicit knockout essentiality) was not found in the retrieved KT2440 primary literature segments. The report therefore relies on: (i) authoritative EPSPS mechanism reviews (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 50-64), and (ii) KT2440-specific engineering phenotypes involving **aroA expression** (camposmagana2025combinatorialengineeringpinpoints pages 8-9), while explicitly flagging KT2440 annotation inconsistencies (molinahenares2009functionalanalysisof pages 2-4).

### Key cited sources (with publication dates and URLs)
- Shende VV, Bauman KD, Moore BS. *The shikimate pathway: gateway to metabolic diversity.* **Natural Product Reports**. **Jan 2024**. https://doi.org/10.1039/d3np00037k (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 50-64)
- Reed KB et al. *Evolving dual-trait EPSP synthase variants using a synthetic yeast selection system.* **PNAS**. **Aug 2024**. https://doi.org/10.1073/pnas.2317027121 (reed2024evolvingdualtraitepsp pages 1-2, reed2024evolvingdualtraitepsp pages 5-6)
- Caygill S et al. *MurA-catalyzed synthesis of EPSP confers glyphosate tolerance in bryophytes.* **PNAS**. **Nov 2024**. https://doi.org/10.1073/pnas.2412997121 (caygill2024muracatalyzedsynthesisof pages 1-2, caygill2024muracatalyzedsynthesisof pages 6-7)
- Campos‑Magaña MA et al. *Combinatorial engineering pinpoints shikimate pathway bottlenecks in pABA production in Pseudomonas putida.* **Journal of Biological Engineering**. **Sep 2025**. https://doi.org/10.1186/s13036-025-00553-5 (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 8-9)
- Hertel R et al. *Molecular mechanisms underlying glyphosate resistance in bacteria.* **Environmental Microbiology**. **Jun 2021**. https://doi.org/10.1111/1462-2920.15534 (hertel2021molecularmechanismsunderlying pages 1-5, hertel2021molecularmechanismsunderlying pages 5-8, hertel2021molecularmechanismsunderlying pages 12-15)
- Molina‑Henares MA et al. *Functional analysis of aromatic biosynthetic pathways in Pseudomonas putida KT2440.* **Microbial Biotechnology**. **Dec 2009**. https://doi.org/10.1111/j.1751-7915.2008.00062.x (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 6-7)
- Molina‑Henares MA et al. *Identification of conditionally essential genes for growth of Pseudomonas putida KT2440 on minimal medium…* **Environmental Microbiology**. **Jun 2010**. https://doi.org/10.1111/j.1462-2920.2010.02166.x (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 6-7)


References

1. (molinahenares2009functionalanalysisof pages 2-4): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

2. (shende2024theshikimatepathway pages 10-11): Vikram V. Shende, Katherine D. Bauman, and Bradley S. Moore. The shikimate pathway: gateway to metabolic diversity. Natural product reports, 41:604-648, Jan 2024. URL: https://doi.org/10.1039/d3np00037k, doi:10.1039/d3np00037k. This article has 173 citations and is from a peer-reviewed journal.

3. (shende2024theshikimatepathway pages 50-64): Vikram V. Shende, Katherine D. Bauman, and Bradley S. Moore. The shikimate pathway: gateway to metabolic diversity. Natural product reports, 41:604-648, Jan 2024. URL: https://doi.org/10.1039/d3np00037k, doi:10.1039/d3np00037k. This article has 173 citations and is from a peer-reviewed journal.

4. (camposmagana2025combinatorialengineeringpinpoints pages 2-4): Marco A Campos-Magaña, Sara Moreno-Paz, Maria Martin-Pascual, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering pinpoints shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. Journal of Biological Engineering, Sep 2025. URL: https://doi.org/10.1186/s13036-025-00553-5, doi:10.1186/s13036-025-00553-5. This article has 0 citations and is from a peer-reviewed journal.

5. (camposmagana2025combinatorialengineeringpinpoints pages 4-6): Marco A Campos-Magaña, Sara Moreno-Paz, Maria Martin-Pascual, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering pinpoints shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. Journal of Biological Engineering, Sep 2025. URL: https://doi.org/10.1186/s13036-025-00553-5, doi:10.1186/s13036-025-00553-5. This article has 0 citations and is from a peer-reviewed journal.

6. (camposmagana2025combinatorialengineeringpinpoints pages 8-9): Marco A Campos-Magaña, Sara Moreno-Paz, Maria Martin-Pascual, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering pinpoints shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. Journal of Biological Engineering, Sep 2025. URL: https://doi.org/10.1186/s13036-025-00553-5, doi:10.1186/s13036-025-00553-5. This article has 0 citations and is from a peer-reviewed journal.

7. (reed2024evolvingdualtraitepsp pages 1-2): Kevin B. Reed, Wantae Kim, Hongyuan Lu, Clayton T. Larue, Shirley Guo, Sierra M. Brooks, Michael R. Montez, James M. Wagner, Y. Jessie Zhang, and Hal S. Alper. Evolving dual-trait epsp synthase variants using a synthetic yeast selection system. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2317027121, doi:10.1073/pnas.2317027121. This article has 7 citations and is from a highest quality peer-reviewed journal.

8. (caygill2024muracatalyzedsynthesisof pages 1-2): Samuel Caygill, Thomas Köcher, and Liam Dolan. Mura-catalyzed synthesis of 5-enolpyruvylshikimate-3-phosphate confers glyphosate tolerance in bryophytes. Proceedings of the National Academy of Sciences of the United States of America, Nov 2024. URL: https://doi.org/10.1073/pnas.2412997121, doi:10.1073/pnas.2412997121. This article has 10 citations and is from a highest quality peer-reviewed journal.

9. (caygill2024muracatalyzedsynthesisof pages 6-7): Samuel Caygill, Thomas Köcher, and Liam Dolan. Mura-catalyzed synthesis of 5-enolpyruvylshikimate-3-phosphate confers glyphosate tolerance in bryophytes. Proceedings of the National Academy of Sciences of the United States of America, Nov 2024. URL: https://doi.org/10.1073/pnas.2412997121, doi:10.1073/pnas.2412997121. This article has 10 citations and is from a highest quality peer-reviewed journal.

10. (hertel2021molecularmechanismsunderlying pages 1-5): Robert Hertel, Johannes Gibhardt, Marion Martienssen, Ramona Kuhn, and Fabian M. Commichau. Molecular mechanisms underlying glyphosate resistance in bacteria. Jun 2021. URL: https://doi.org/10.1111/1462-2920.15534, doi:10.1111/1462-2920.15534. This article has 67 citations and is from a domain leading peer-reviewed journal.

11. (hertel2021molecularmechanismsunderlying pages 24-27): Robert Hertel, Johannes Gibhardt, Marion Martienssen, Ramona Kuhn, and Fabian M. Commichau. Molecular mechanisms underlying glyphosate resistance in bacteria. Jun 2021. URL: https://doi.org/10.1111/1462-2920.15534, doi:10.1111/1462-2920.15534. This article has 67 citations and is from a domain leading peer-reviewed journal.

12. (hertel2021molecularmechanismsunderlying pages 5-8): Robert Hertel, Johannes Gibhardt, Marion Martienssen, Ramona Kuhn, and Fabian M. Commichau. Molecular mechanisms underlying glyphosate resistance in bacteria. Jun 2021. URL: https://doi.org/10.1111/1462-2920.15534, doi:10.1111/1462-2920.15534. This article has 67 citations and is from a domain leading peer-reviewed journal.

13. (hertel2021molecularmechanismsunderlying pages 12-15): Robert Hertel, Johannes Gibhardt, Marion Martienssen, Ramona Kuhn, and Fabian M. Commichau. Molecular mechanisms underlying glyphosate resistance in bacteria. Jun 2021. URL: https://doi.org/10.1111/1462-2920.15534, doi:10.1111/1462-2920.15534. This article has 67 citations and is from a domain leading peer-reviewed journal.

14. (molina‐henares2010identificationofconditionally pages 2-3): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 89 citations and is from a domain leading peer-reviewed journal.

15. (molina‐henares2010identificationofconditionally pages 6-7): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 89 citations and is from a domain leading peer-reviewed journal.

16. (molinahenares2009functionalanalysisof pages 6-7): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

17. (reed2024evolvingdualtraitepsp pages 5-6): Kevin B. Reed, Wantae Kim, Hongyuan Lu, Clayton T. Larue, Shirley Guo, Sierra M. Brooks, Michael R. Montez, James M. Wagner, Y. Jessie Zhang, and Hal S. Alper. Evolving dual-trait epsp synthase variants using a synthetic yeast selection system. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2317027121, doi:10.1073/pnas.2317027121. This article has 7 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](aroA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. molinahenares2009functionalanalysisof pages 2-4
2. shende2024theshikimatepathway pages 10-11
3. shende2024theshikimatepathway pages 50-64
4. reed2024evolvingdualtraitepsp pages 1-2
5. molinahenares2009functionalanalysisof pages 6-7
6. camposmagana2025combinatorialengineeringpinpoints pages 2-4
7. camposmagana2025combinatorialengineeringpinpoints pages 4-6
8. camposmagana2025combinatorialengineeringpinpoints pages 8-9
9. caygill2024muracatalyzedsynthesisof pages 1-2
10. caygill2024muracatalyzedsynthesisof pages 6-7
11. hertel2021molecularmechanismsunderlying pages 1-5
12. hertel2021molecularmechanismsunderlying pages 5-8
13. hertel2021molecularmechanismsunderlying pages 12-15
14. hertel2021molecularmechanismsunderlying pages 24-27
15. reed2024evolvingdualtraitepsp pages 5-6
16. https://doi.org/10.1111/j.1751-7915.2008.00062.x
17. https://doi.org/10.1039/d3np00037k
18. https://doi.org/10.1186/s13036-025-00553-5
19. https://doi.org/10.1073/pnas.2317027121
20. https://doi.org/10.1073/pnas.2412997121
21. https://doi.org/10.1111/1462-2920.15534
22. https://doi.org/10.1111/j.1462-2920.2010.02166.x
23. https://doi.org/10.1111/j.1751-7915.2008.00062.x,
24. https://doi.org/10.1039/d3np00037k,
25. https://doi.org/10.1186/s13036-025-00553-5,
26. https://doi.org/10.1073/pnas.2317027121,
27. https://doi.org/10.1073/pnas.2412997121,
28. https://doi.org/10.1111/1462-2920.15534,
29. https://doi.org/10.1111/j.1462-2920.2010.02166.x,