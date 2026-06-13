---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T20:39:52.114682'
end_time: '2026-06-11T20:49:16.310727'
duration_seconds: 564.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: aroC
  gene_symbol: aroC
  uniprot_accession: Q88LU7
  protein_description: 'RecName: Full=Chorismate synthase {ECO:0000255|HAMAP-Rule:MF_00300};
    Short=CS {ECO:0000255|HAMAP-Rule:MF_00300}; EC=4.2.3.5 {ECO:0000255|HAMAP-Rule:MF_00300};
    AltName: Full=5-enolpyruvylshikimate-3-phosphate phospholyase {ECO:0000255|HAMAP-Rule:MF_00300};'
  gene_info: Name=aroC {ECO:0000255|HAMAP-Rule:MF_00300}; OrderedLocusNames=PP_1830;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the chorismate synthase family.
  protein_domains: Chorismate_synth. (IPR000453); Chorismate_synth_AroC_sf. (IPR035904);
    Chorismate_synthase_CS. (IPR020541); Chorismate_synt (PF01264)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: aroC-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88LU7
- **Protein Description:** RecName: Full=Chorismate synthase {ECO:0000255|HAMAP-Rule:MF_00300}; Short=CS {ECO:0000255|HAMAP-Rule:MF_00300}; EC=4.2.3.5 {ECO:0000255|HAMAP-Rule:MF_00300}; AltName: Full=5-enolpyruvylshikimate-3-phosphate phospholyase {ECO:0000255|HAMAP-Rule:MF_00300};
- **Gene Information:** Name=aroC {ECO:0000255|HAMAP-Rule:MF_00300}; OrderedLocusNames=PP_1830;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the chorismate synthase family.
- **Key Domains:** Chorismate_synth. (IPR000453); Chorismate_synth_AroC_sf. (IPR035904); Chorismate_synthase_CS. (IPR020541); Chorismate_synt (PF01264)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aroC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aroC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aroC** (gene ID: aroC, UniProt: Q88LU7) in PSEPK.

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
- **UniProt Accession:** Q88LU7
- **Protein Description:** RecName: Full=Chorismate synthase {ECO:0000255|HAMAP-Rule:MF_00300}; Short=CS {ECO:0000255|HAMAP-Rule:MF_00300}; EC=4.2.3.5 {ECO:0000255|HAMAP-Rule:MF_00300}; AltName: Full=5-enolpyruvylshikimate-3-phosphate phospholyase {ECO:0000255|HAMAP-Rule:MF_00300};
- **Gene Information:** Name=aroC {ECO:0000255|HAMAP-Rule:MF_00300}; OrderedLocusNames=PP_1830;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the chorismate synthase family.
- **Key Domains:** Chorismate_synth. (IPR000453); Chorismate_synth_AroC_sf. (IPR035904); Chorismate_synthase_CS. (IPR020541); Chorismate_synt (PF01264)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aroC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aroC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aroC** (gene ID: aroC, UniProt: Q88LU7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Functional Annotation of **aroC** (Chorismate synthase) in *Pseudomonas putida* KT2440 (UniProt Q88LU7; PP_1830)

## 1. Target verification (gene/protein identity)

The research target is **AroC (chorismate synthase; EC 4.2.3.5)** encoded by **aroC** and mapped (per the provided UniProt record) to ordered locus **PP_1830** in ***Pseudomonas putida* strain KT2440** (UniProt **Q88LU7**). The retrieved literature that mentions “aroC” in *Pseudomonas* metabolic engineering uses it consistently as a **shikimate-pathway gene encoding chorismate synthase** (e.g., included as a shikimate-pathway overexpression target in *P. putida* KT2440) and not as an unrelated gene, supporting correct symbol usage in this organism context (camposmagana2024combinatorialengineeringreveals pages 4-7).

**Limitation:** within the retrieved full texts, there is **little direct primary characterization explicitly citing PP_1830/Q88LU7**; therefore, organism-specific biochemical details for this exact protein are inferred from conserved AroC enzymology (family-level evidence) and *P. putida* KT2440 pathway-engineering studies.

## 2. Key concepts and definitions (current understanding)

### 2.1 Chorismate synthase (AroC): definition and core biochemical role

**Chorismate synthase (AroC; EC 4.2.3.5)** catalyzes the **terminal step of the shikimate pathway**, converting **5-enolpyruvylshikimate-3-phosphate (EPSP)** into **chorismate** with **elimination of inorganic phosphate** (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13). The enzymatic transformation is described as a **1,4-trans elimination** of the phosphate group from EPSP, which introduces a second double bond into the six-membered ring system to yield chorismate (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13).

Because chorismate is the **key branch-point metabolite** at the end of the shikimate pathway, AroC function is tightly tied to biosynthesis of **aromatic amino acids** and other chorismate-derived products (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13).

### 2.2 Substrate specificity and reaction stoichiometry

The canonical substrate is **EPSP**, and the product is **chorismate + phosphate** (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13). Structural/biochemical work in other taxa (e.g., fungal chorismate synthase) explicitly models/binds **EPSP** together with **FMNH2** at the active site and uses EPSP in enzyme assays, reinforcing EPSP as the functional substrate in chorismate synthases across organisms (rodriguesvendramini2019promisingnewantifungal pages 2-5).

### 2.3 Cofactor requirements and mechanistic features

Although the overall EPSP→chorismate conversion is an elimination with **no net redox change**, chorismate synthase requires **reduced flavin mononucleotide (FMNH2)** for catalysis (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13). A 2024 authoritative review summarizes that **monofunctional** chorismate synthases (e.g., from *E. coli* and higher plants) are unable to reduce FMN themselves and therefore depend on **externally supplied reduced FMN**, whereas some organisms (e.g., fungi/protozoa) have **bifunctional** enzymes capable of reducing FMN using **NADPH**, changing how FMNH2 is supplied (shende2024theshikimatepathway pages 11-13).

### 2.4 Quaternary structure and enzyme family context

Chorismate synthase is often **tetrameric**. For example, a mycobacterial chorismate synthase structure was solved with bound **FMN** and described as a **tetramer (dimer of dimers)** (nunes2020mycobacteriumtuberculosisshikimate pages 20-23). A fungal chorismate synthase was modeled as a **homotetramer** for docking/MD stability and ligand binding (rodriguesvendramini2019promisingnewantifungal pages 2-5). This supports a common structural theme that is relevant for conserved function.

## 3. Biological processes, pathways, and cellular location (functional annotation)

### 3.1 Pathway context: shikimate pathway and chorismate branch point

The shikimate pathway comprises seven steps that convert central carbon precursors (classically PEP and E4P) into **chorismate**, which then branches into multiple essential biosynthetic routes (nunes2020mycobacteriumtuberculosisshikimate pages 3-7). The product chorismate is a central node feeding the biosynthesis of **phenylalanine, tyrosine, and tryptophan**, and also contributes to other pathways, such as **PABA/folate-related metabolism** and quinone-related metabolites in microbes (guida2024aminoacidbiosynthesis pages 1-2, nunes2020mycobacteriumtuberculosisshikimate pages 3-7).

In *P. putida* KT2440 specifically, multiple engineering studies rely on increasing shikimate/chorismate supply to produce aromatic chemicals, demonstrating that chorismate availability (and therefore AroC activity upstream) is a key determinant of metabolic output in this chassis (yu2016metabolicengineeringof pages 1-3, dias2023fromdegraderto pages 8-11, camposmagana2024combinatorialengineeringreveals pages 7-11).

### 3.2 Likely subcellular localization

No direct experimental localization for **AroC (PP_1830/Q88LU7)** was retrieved from the available texts. However, given that chorismate synthase catalyzes a soluble step of central metabolism and the retrieved mechanistic/structural literature treats it as a soluble enzyme (with defined quaternary structure and bound flavin), the most consistent working annotation is that AroC functions as a **cytosolic enzyme** in bacteria.

**Evidence limitation:** because no explicit localization measurement for this *P. putida* enzyme was retrieved, the cytosolic localization should be treated as a **reasonable inference** rather than directly demonstrated in KT2440 within the cited sources.

## 4. Recent developments and latest research (prioritizing 2023–2024)

### 4.1 2024 state-of-the-art synthesis of shikimate-pathway enzymology

A 2024 **Natural Product Reports** review (covering 1997–2023) provides an up-to-date synthesis of shikimate pathway enzymology and highlights that chorismate synthase has been interrogated using kinetic isotope and structural biology methods, reiterating (i) the EPSP→chorismate phosphate-elimination chemistry and (ii) the essential requirement for **FMNH2** (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13). This is an authoritative, high-citation review source suitable for current “textbook-level” mechanistic statements.

### 4.2 2024 *P. putida* combinatorial tuning of shikimate genes (aroC included)

A 2024 bioRxiv preprint used a **design-of-experiments (Plackett–Burman) + linear modeling** approach to tune expression of nine factors in *P. putida* shikimate and pABA biosynthesis, explicitly including **aroC** among the genes amplified from KT2440 and tested at two expression levels (camposmagana2024combinatorialengineeringreveals pages 4-7). The authors report **pABA titers ranging from ~2 mg/L to ~232 mg/L** across their engineering cycle, with a reported best yield of **0.024 mol/mol glucose** (camposmagana2024combinatorialengineeringreveals pages 7-11). Critically for aroC functional annotation in a metabolic-engineering context, they report that **high aroC expression can be unfavorable** and conclude that **mild aroC overexpression** is preferable—consistent with aroC not necessarily being the dominant bottleneck compared with other steps like aroB (camposmagana2024combinatorialengineeringreveals pages 7-11).

### 4.3 2023 *P. putida* repurposing to produce gallic acid from glycerol

A 2023 study engineered *P. putida* KT2440 to produce **gallic acid** from glycerol and reported **346.7 ± 0.004 mg/L** final concentration after 72 h and an observed yield of **0.12 g gallic acid per g glycerol** (dias2023fromdegraderto pages 8-11). While the work did not directly manipulate aroC, it demonstrates the importance of driving flux through the shikimate/chorismate node and highlights NADPH-related considerations for high-yield routes (dias2023fromdegraderto pages 8-11).

## 5. Current applications and real-world implementations

### 5.1 Industrial biotechnology: routing chorismate to commodity and specialty aromatics

*Pseudomonas putida* KT2440 is used as a robust host for producing aromatic chemicals via chorismate-derived routes. A prominent example is production of **para-hydroxybenzoic acid (PHBA)** by expressing **E. coli ubiC (chorismate lyase)** to convert chorismate into PHBA, combined with a feedback-resistant **DAHP synthase (aroG D146N)** and deletion of competing chorismate-consuming/degrading pathways. This strategy achieved **1.73 g/L PHBA** with a **carbon yield of 18.1% (C-mol/C-mol)** in fed-batch fermentation (yu2016metabolicengineeringof pages 1-3). These data show that maintaining sufficient chorismate supply (which depends upstream on AroC) is central to industrial aromatic production in KT2440.

### 5.2 Synthetic biology “tuning” view of aroC

The 2024 DoE study implies that, at least for pABA production in KT2440, **aroC expression requires balance**: overexpression beyond a mild level may reduce performance (camposmagana2024combinatorialengineeringreveals pages 7-11). This kind of result is useful for functional annotation because it indicates aroC is embedded in a network where enzyme overabundance can create cofactor demands (e.g., reduced FMN supply), imbalances, or metabolic burden, even if the enzyme is essential for producing chorismate.

## 6. Expert opinions and analysis from authoritative sources

### 6.1 Why chorismate/shikimate metabolism is a key microbial vulnerability

A 2024 TB-focused review reiterates the **selective-targeting rationale** for shikimate pathway enzymes: the pathway is **absent in humans** and essential in certain pathogens such as *Mycobacterium tuberculosis*, and chorismate is a metabolic node for aromatic amino acids and other essential metabolites (guida2024aminoacidbiosynthesis pages 1-2). This expert framing supports the broad interpretation that enzymes upstream of chorismate (including AroC) underpin essential biosynthetic capacity in many microbes.

A 2024 Applied and Environmental Microbiology paper further validates the idea of targeting **chorismate-utilizing** enzymes (anthranilate synthase and aminodeoxychorismate synthase) as antibiotic targets, emphasizing desirable target features such as essentiality and lack of human homologs, and proposing that disrupting conserved protein–protein interactions could provide robust antibacterial strategies (funke2024validationofaminodeoxychorismate pages 1-2). While not about AroC directly, it illustrates the ongoing 2024 research emphasis on the **chorismate node** as an antimicrobial intervention point.

## 7. Relevant statistics and quantitative data from recent studies

### 7.1 Metabolic engineering performance metrics in *P. putida* KT2440

* **PHBA production (chorismate-derived):** 1.73 g/L titer; 18.1% C-mol/C-mol yield in non-optimized fed-batch (2016; still a widely cited benchmark for KT2440) (yu2016metabolicengineeringof pages 1-3).
* **pABA production:** ~2–232 mg/L titers reported in 2024 DoE study; best yield 0.024 mol/mol glucose; high aroC overexpression reported as unfavorable with recommendation for mild tuning (camposmagana2024combinatorialengineeringreveals pages 7-11, camposmagana2024combinatorialengineeringreveals pages 4-7).
* **Gallic acid production:** 346.7 ± 0.004 mg/L; observed yield 0.12 g/g glycerol (2023) (dias2023fromdegraderto pages 8-11).

### 7.2 Infectious disease / AMR burden statistics referenced in 2024 literature

* A 2024 TB drug-discovery review reports **10.6 million TB diagnoses** and **1.30 million deaths** in 2022, and ~**410,000 MDR/RR-TB cases** in 2022, providing the clinical motivation for pursuing new antibacterial targets including pathways like shikimate metabolism (guida2024aminoacidbiosynthesis pages 1-2).
* A 2024 MRSA-focused shikimate-kinase inhibitor paper cites **1.27 million deaths** in 2019 attributed to antimicrobial resistance (AMR) (riossoto2024inhibitionofshikimate pages 1-2).

## 8. Functional annotation summary for UniProt Q88LU7 (aroC; PP_1830)

**Primary molecular function:** Chorismate synthase (AroC) catalyzes **EPSP → chorismate + phosphate** via **1,4-trans elimination**; requires **reduced FMN (FMNH2)** for catalysis (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13).

**Biological process context:** terminal step of the **shikimate pathway** supplying **chorismate**, which serves as the precursor branch point for aromatic amino acids and other essential aromatic metabolites (guida2024aminoacidbiosynthesis pages 1-2, nunes2020mycobacteriumtuberculosisshikimate pages 3-7).

**Cellular location (best-supported annotation from available evidence):** likely **cytosolic**, but direct localization evidence for PP_1830/Q88LU7 in KT2440 was not retrieved in the available texts.

**Application relevance:** In *P. putida* KT2440, engineering of chorismate supply is central to bioproduction of aromatic products such as PHBA, pABA, and gallic acid; studies indicate that **balanced** expression of shikimate enzymes (including aroC) can matter for yield and titer (yu2016metabolicengineeringof pages 1-3, camposmagana2024combinatorialengineeringreveals pages 7-11, dias2023fromdegraderto pages 8-11).

---

## Summary table

| Aspect | Summary |
|---|---|
| Gene/protein identity | **aroC**; UniProt **Q88LU7**; ordered locus **PP_1830**; organism **Pseudomonas putida** strain **KT2440**; annotated as a chorismate synthase family protein in the user-supplied UniProt record. Direct organism-specific primary literature on PP_1830 itself appears limited, so some functional details below are inferred from conserved chorismate synthase biochemistry and family-level evidence plus *P. putida* pathway-engineering studies (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13, camposmagana2024combinatorialengineeringreveals pages 4-7). |
| Enzyme name / EC | **Chorismate synthase**; **EC 4.2.3.5**; terminal enzyme of the shikimate pathway in bacteria (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13). |
| Reaction catalyzed | **5-enolpyruvylshikimate-3-phosphate (EPSP) → chorismate + phosphate**; mechanistically described as a **1,4-trans elimination** of phosphate from EPSP, creating the second double bond in the ring system of chorismate (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13, rodriguesvendramini2019promisingnewantifungal pages 2-5). |
| Required cofactor(s) | Requires **reduced FMN (FMNH2)** for activity even though the overall reaction is not net redox. In many bacterial/plant **monofunctional** enzymes, FMN is reduced externally (often by a separate flavin reductase or reduced flavin supply), whereas **bifunctional** enzymes in some fungi/protozoa can reduce FMN themselves with **NADPH** (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13). |
| Pathway role | Catalyzes the **terminal step from EPSP to chorismate** in the shikimate pathway. **Chorismate** is the major branch-point precursor for **phenylalanine, tyrosine, tryptophan**, and additional metabolites such as **PABA/folate**, **ubiquinone/menaquinone-related products**, and other aromatic metabolites (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13, guida2024aminoacidbiosynthesis pages 1-2, nunes2020mycobacteriumtuberculosisshikimate pages 3-7). |
| Quaternary structure notes | Chorismate synthase is commonly reported as a **tetramer**; structural work on non-*P. putida* orthologs describes a homotetramer or tetrameric assembly important for ligand binding/stability (rodriguesvendramini2019promisingnewantifungal pages 2-5, nunes2020mycobacteriumtuberculosisshikimate pages 20-23). |
| Likely localization | No direct localization evidence for **PP_1830/Q88LU7** was retrieved here. Given its role in central aromatic biosynthesis and lack of membrane-targeting evidence in the gathered sources, the enzyme is most reasonably treated as a **cytosolic bacterial metabolic enzyme**, but this point should be considered an inference rather than a directly sourced *P. putida* measurement. |
| *P. putida* application: PHBA production | In *P. putida* KT2440, shikimate/chorismate flux was engineered toward **para-hydroxybenzoic acid (PHBA)** by expressing **E. coli ubiC** and feedback-resistant **aroG D146N**, with deletions of **pobA, pheA, trpE**, and **hexR**. Best reported performance: **1.73 g/L PHBA** and **18.1% C-mol/C-mol** carbon yield in non-optimized fed-batch fermentation (yu2016metabolicengineeringof pages 5-6, yu2016metabolicengineeringof pages 1-3). |
| *P. putida* application: pABA production / aroC tuning | A 2024 combinatorial-expression study in *P. putida* found **pABA titers spanning ~2–232 mg/L**. **High aroC overexpression** was reported to have an unfavorable or only mildly beneficial effect; the authors concluded **mild rather than maximal aroC expression** was preferable, while **aroB** emerged as a stronger bottleneck (camposmagana2024combinatorialengineeringreveals pages 7-11, camposmagana2024combinatorialengineeringreveals pages 4-7). |
| *P. putida* application: gallic acid production | Engineering of shikimate-pathway flux in *P. putida* KT2440 for **gallic acid** production from glycerol achieved **346.7 ± 0.004 mg/L** gallic acid and an observed yield of **0.12 g/g glycerol**; this study did not specifically manipulate aroC, but it demonstrates practical importance of chorismate-pathway flux control in this host (dias2023fromdegraderto pages 8-11). |


*Table: This table summarizes the verified identity, core enzymology, pathway context, and recent Pseudomonas putida engineering relevance of aroC/chorismate synthase. It is useful as a compact evidence-backed reference for the final research report.*

## URLs and publication dates for key cited sources

* Shende VV, Bauman KD, Moore BS. **“The shikimate pathway: gateway to metabolic diversity.”** *Natural Product Reports* (Jan **2024**). https://doi.org/10.1039/d3np00037k (shende2024theshikimatepathway pages 10-11, shende2024theshikimatepathway pages 11-13)
* Campos-Magaña MA et al. **“Combinatorial engineering reveals shikimate pathway bottlenecks in para-aminobenzoic acid production in Pseudomonas putida.”** *bioRxiv* (Jun **2024**). https://doi.org/10.1101/2024.06.17.599342 (camposmagana2024combinatorialengineeringreveals pages 7-11, camposmagana2024combinatorialengineeringreveals pages 4-7)
* Dias FMS et al. **“From degrader to producer: reversing the gallic acid metabolism of Pseudomonas putida KT2440.”** *International Microbiology* (Nov **2023**). https://doi.org/10.1007/s10123-022-00282-5 (dias2023fromdegraderto pages 8-11)
* Funke FJ, Schlee S, Sterner R. **“Validation of aminodeoxychorismate synthase and anthranilate synthase as novel targets…”** *Applied and Environmental Microbiology* (May **2024**). https://doi.org/10.1128/aem.00572-24 (funke2024validationofaminodeoxychorismate pages 1-2)
* Guida M et al. **“Amino Acid Biosynthesis Inhibitors in Tuberculosis Drug Discovery.”** *Pharmaceutics* (May **2024**). https://doi.org/10.3390/pharmaceutics16060725 (guida2024aminoacidbiosynthesis pages 1-2, guida2024aminoacidbiosynthesis pages 2-4)
* Rios-Soto L et al. **“Inhibition of Shikimate Kinase from MRSA by Benzimidazole Derivatives…”** *International Journal of Molecular Sciences* (May **2024**). https://doi.org/10.3390/ijms25105077 (riossoto2024inhibitionofshikimate pages 1-2)
* Yu S et al. **“Metabolic Engineering of Pseudomonas putida KT2440 for the Production of para-Hydroxy Benzoic Acid.”** *Frontiers in Bioengineering and Biotechnology* (Nov **2016**). https://doi.org/10.3389/fbioe.2016.00090 (yu2016metabolicengineeringof pages 1-3, yu2016metabolicengineeringof pages 5-6)


References

1. (camposmagana2024combinatorialengineeringreveals pages 4-7): Marco A Campos-Magaña, Sara Moreno-Paz, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering reveals shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.17.599342, doi:10.1101/2024.06.17.599342. This article has 0 citations.

2. (shende2024theshikimatepathway pages 10-11): Vikram V. Shende, Katherine D. Bauman, and Bradley S. Moore. The shikimate pathway: gateway to metabolic diversity. Natural product reports, 41:604-648, Jan 2024. URL: https://doi.org/10.1039/d3np00037k, doi:10.1039/d3np00037k. This article has 173 citations and is from a peer-reviewed journal.

3. (shende2024theshikimatepathway pages 11-13): Vikram V. Shende, Katherine D. Bauman, and Bradley S. Moore. The shikimate pathway: gateway to metabolic diversity. Natural product reports, 41:604-648, Jan 2024. URL: https://doi.org/10.1039/d3np00037k, doi:10.1039/d3np00037k. This article has 173 citations and is from a peer-reviewed journal.

4. (rodriguesvendramini2019promisingnewantifungal pages 2-5): Franciele Abigail Vilugron Rodrigues-Vendramini, Cidnei Marschalk, Marina Toplak, Peter Macheroux, Patricia de Souza Bonfim-Mendonça, Terezinha Inez Estivalet Svidzinski, Flavio Augusto Vicente Seixas, and Erika Seki Kioshima. Promising new antifungal treatment targeting chorismate synthase from <i>paracoccidioides brasiliensis</i>. Antimicrobial Agents and Chemotherapy, Jan 2019. URL: https://doi.org/10.1128/aac.01097-18, doi:10.1128/aac.01097-18. This article has 30 citations and is from a highest quality peer-reviewed journal.

5. (nunes2020mycobacteriumtuberculosisshikimate pages 20-23): José E. S. Nunes, Mario A. Duque, Talita F. de Freitas, Luiza Galina, Luis F. S. M. Timmers, Cristiano V. Bizarro, Pablo Machado, Luiz A. Basso, and Rodrigo G. Ducati. Mycobacterium tuberculosis shikimate pathway enzymes as targets for the rational design of anti-tuberculosis drugs. Molecules, 25:1259, Mar 2020. URL: https://doi.org/10.3390/molecules25061259, doi:10.3390/molecules25061259. This article has 74 citations.

6. (nunes2020mycobacteriumtuberculosisshikimate pages 3-7): José E. S. Nunes, Mario A. Duque, Talita F. de Freitas, Luiza Galina, Luis F. S. M. Timmers, Cristiano V. Bizarro, Pablo Machado, Luiz A. Basso, and Rodrigo G. Ducati. Mycobacterium tuberculosis shikimate pathway enzymes as targets for the rational design of anti-tuberculosis drugs. Molecules, 25:1259, Mar 2020. URL: https://doi.org/10.3390/molecules25061259, doi:10.3390/molecules25061259. This article has 74 citations.

7. (guida2024aminoacidbiosynthesis pages 1-2): Michela Guida, Chiara Tammaro, Miriana Quaranta, Benedetta Salvucci, Mariangela Biava, Giovanna Poce, and Sara Consalvi. Amino acid biosynthesis inhibitors in tuberculosis drug discovery. Pharmaceutics, 16:725, May 2024. URL: https://doi.org/10.3390/pharmaceutics16060725, doi:10.3390/pharmaceutics16060725. This article has 3 citations.

8. (yu2016metabolicengineeringof pages 1-3): Shiqin Yu, Manuel R. Plan, Gal Winter, and Jens O. Krömer. Metabolic engineering of pseudomonas putida kt2440 for the production of para-hydroxy benzoic acid. Frontiers in Bioengineering and Biotechnology, Nov 2016. URL: https://doi.org/10.3389/fbioe.2016.00090, doi:10.3389/fbioe.2016.00090. This article has 76 citations.

9. (dias2023fromdegraderto pages 8-11): Felipe M. S. Dias, Raoní K. Pantoja, José Gregório C. Gomez, and Luiziana F. Silva. From degrader to producer: reversing the gallic acid metabolism of pseudomonas putida kt2440. International Microbiology, 26:243-255, Nov 2023. URL: https://doi.org/10.1007/s10123-022-00282-5, doi:10.1007/s10123-022-00282-5. This article has 7 citations and is from a peer-reviewed journal.

10. (camposmagana2024combinatorialengineeringreveals pages 7-11): Marco A Campos-Magaña, Sara Moreno-Paz, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering reveals shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.17.599342, doi:10.1101/2024.06.17.599342. This article has 0 citations.

11. (funke2024validationofaminodeoxychorismate pages 1-2): Franziska Jasmin Funke, Sandra Schlee, and Reinhard Sterner. Validation of aminodeoxychorismate synthase and anthranilate synthase as novel targets for bispecific antibiotics inhibiting conserved protein-protein interactions. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00572-24, doi:10.1128/aem.00572-24. This article has 5 citations and is from a peer-reviewed journal.

12. (riossoto2024inhibitionofshikimate pages 1-2): Lluvia Rios-Soto, Alicia Hernández-Campos, David Tovar-Escobar, Rafael Castillo, Erick Sierra-Campos, Mónica Valdez-Solana, Alfredo Téllez-Valencia, and Claudia Avitia-Domínguez. Inhibition of shikimate kinase from methicillin-resistant staphylococcus aureus by benzimidazole derivatives. kinetic, computational, toxicological, and biological activity studies. International Journal of Molecular Sciences, 25:5077, May 2024. URL: https://doi.org/10.3390/ijms25105077, doi:10.3390/ijms25105077. This article has 8 citations.

13. (yu2016metabolicengineeringof pages 5-6): Shiqin Yu, Manuel R. Plan, Gal Winter, and Jens O. Krömer. Metabolic engineering of pseudomonas putida kt2440 for the production of para-hydroxy benzoic acid. Frontiers in Bioengineering and Biotechnology, Nov 2016. URL: https://doi.org/10.3389/fbioe.2016.00090, doi:10.3389/fbioe.2016.00090. This article has 76 citations.

14. (guida2024aminoacidbiosynthesis pages 2-4): Michela Guida, Chiara Tammaro, Miriana Quaranta, Benedetta Salvucci, Mariangela Biava, Giovanna Poce, and Sara Consalvi. Amino acid biosynthesis inhibitors in tuberculosis drug discovery. Pharmaceutics, 16:725, May 2024. URL: https://doi.org/10.3390/pharmaceutics16060725, doi:10.3390/pharmaceutics16060725. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](aroC-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. camposmagana2024combinatorialengineeringreveals pages 4-7
2. rodriguesvendramini2019promisingnewantifungal pages 2-5
3. shende2024theshikimatepathway pages 11-13
4. nunes2020mycobacteriumtuberculosisshikimate pages 20-23
5. nunes2020mycobacteriumtuberculosisshikimate pages 3-7
6. camposmagana2024combinatorialengineeringreveals pages 7-11
7. dias2023fromdegraderto pages 8-11
8. yu2016metabolicengineeringof pages 1-3
9. guida2024aminoacidbiosynthesis pages 1-2
10. funke2024validationofaminodeoxychorismate pages 1-2
11. riossoto2024inhibitionofshikimate pages 1-2
12. shende2024theshikimatepathway pages 10-11
13. yu2016metabolicengineeringof pages 5-6
14. guida2024aminoacidbiosynthesis pages 2-4
15. https://doi.org/10.1039/d3np00037k
16. https://doi.org/10.1101/2024.06.17.599342
17. https://doi.org/10.1007/s10123-022-00282-5
18. https://doi.org/10.1128/aem.00572-24
19. https://doi.org/10.3390/pharmaceutics16060725
20. https://doi.org/10.3390/ijms25105077
21. https://doi.org/10.3389/fbioe.2016.00090
22. https://doi.org/10.1101/2024.06.17.599342,
23. https://doi.org/10.1039/d3np00037k,
24. https://doi.org/10.1128/aac.01097-18,
25. https://doi.org/10.3390/molecules25061259,
26. https://doi.org/10.3390/pharmaceutics16060725,
27. https://doi.org/10.3389/fbioe.2016.00090,
28. https://doi.org/10.1007/s10123-022-00282-5,
29. https://doi.org/10.1128/aem.00572-24,
30. https://doi.org/10.3390/ijms25105077,