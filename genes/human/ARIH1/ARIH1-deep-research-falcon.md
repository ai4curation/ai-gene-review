---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-05-11T21:17:56.304844'
end_time: '2026-05-11T21:17:56.306599'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ARIH1
  gene_symbol: ARIH1
  uniprot_accession: Q9Y4X5
  protein_description: 'RecName: Full=E3 ubiquitin-protein ligase ARIH1; EC=2.3.2.31
    {ECO:0000269|PubMed:15236971, ECO:0000269|PubMed:21532592, ECO:0000269|PubMed:27565346};
    AltName: Full=H7-AP2 {ECO:0000303|PubMed:10521492}; AltName: Full=HHARI {ECO:0000303|PubMed:11278816};
    AltName: Full=Monocyte protein 6 {ECO:0000303|Ref.10}; Short=MOP-6 {ECO:0000303|Ref.10};
    AltName: Full=Protein ariadne-1 homolog {ECO:0000303|Ref.3}; Short=ARI-1 {ECO:0000303|Ref.3};
    AltName: Full=UbcH7-binding protein {ECO:0000303|PubMed:11278816}; AltName: Full=UbcM4-interacting
    protein; AltName: Full=Ubiquitin-conjugating enzyme E2-binding protein 1 {ECO:0000303|PubMed:10521492};'
  gene_info: Name=ARIH1 {ECO:0000312|HGNC:HGNC:689}; Synonyms=ARI, MOP6 {ECO:0000303|Ref.10},
    UBCH7BP {ECO:0000303|PubMed:11278816}; ORFNames=HUSSY-27 {ECO:0000303|PubMed:11124703};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the RBR family. Ariadne subfamily.
  protein_domains: Ariadne. (IPR045840); ARIH1-like_UBL. (IPR048962); E3_UB_ligase_RBR.
    (IPR031127); IBR_dom. (IPR002867); TRIAD_supradom. (IPR044066)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9Y4X5
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase ARIH1; EC=2.3.2.31 {ECO:0000269|PubMed:15236971, ECO:0000269|PubMed:21532592, ECO:0000269|PubMed:27565346}; AltName: Full=H7-AP2 {ECO:0000303|PubMed:10521492}; AltName: Full=HHARI {ECO:0000303|PubMed:11278816}; AltName: Full=Monocyte protein 6 {ECO:0000303|Ref.10}; Short=MOP-6 {ECO:0000303|Ref.10}; AltName: Full=Protein ariadne-1 homolog {ECO:0000303|Ref.3}; Short=ARI-1 {ECO:0000303|Ref.3}; AltName: Full=UbcH7-binding protein {ECO:0000303|PubMed:11278816}; AltName: Full=UbcM4-interacting protein; AltName: Full=Ubiquitin-conjugating enzyme E2-binding protein 1 {ECO:0000303|PubMed:10521492};
- **Gene Information:** Name=ARIH1 {ECO:0000312|HGNC:HGNC:689}; Synonyms=ARI, MOP6 {ECO:0000303|Ref.10}, UBCH7BP {ECO:0000303|PubMed:11278816}; ORFNames=HUSSY-27 {ECO:0000303|PubMed:11124703};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the RBR family. Ariadne subfamily.
- **Key Domains:** Ariadne. (IPR045840); ARIH1-like_UBL. (IPR048962); E3_UB_ligase_RBR. (IPR031127); IBR_dom. (IPR002867); TRIAD_supradom. (IPR044066)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ARIH1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ARIH1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ARIH1** (gene ID: ARIH1, UniProt: Q9Y4X5) in human.

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
- **UniProt Accession:** Q9Y4X5
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase ARIH1; EC=2.3.2.31 {ECO:0000269|PubMed:15236971, ECO:0000269|PubMed:21532592, ECO:0000269|PubMed:27565346}; AltName: Full=H7-AP2 {ECO:0000303|PubMed:10521492}; AltName: Full=HHARI {ECO:0000303|PubMed:11278816}; AltName: Full=Monocyte protein 6 {ECO:0000303|Ref.10}; Short=MOP-6 {ECO:0000303|Ref.10}; AltName: Full=Protein ariadne-1 homolog {ECO:0000303|Ref.3}; Short=ARI-1 {ECO:0000303|Ref.3}; AltName: Full=UbcH7-binding protein {ECO:0000303|PubMed:11278816}; AltName: Full=UbcM4-interacting protein; AltName: Full=Ubiquitin-conjugating enzyme E2-binding protein 1 {ECO:0000303|PubMed:10521492};
- **Gene Information:** Name=ARIH1 {ECO:0000312|HGNC:HGNC:689}; Synonyms=ARI, MOP6 {ECO:0000303|Ref.10}, UBCH7BP {ECO:0000303|PubMed:11278816}; ORFNames=HUSSY-27 {ECO:0000303|PubMed:11124703};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the RBR family. Ariadne subfamily.
- **Key Domains:** Ariadne. (IPR045840); ARIH1-like_UBL. (IPR048962); E3_UB_ligase_RBR. (IPR031127); IBR_dom. (IPR002867); TRIAD_supradom. (IPR044066)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ARIH1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ARIH1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ARIH1** (gene ID: ARIH1, UniProt: Q9Y4X5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Human **ARIH1 (HHARI)** Functional Annotation (UniProt Q9Y4X5)

## 0) Target verification (critical)
The literature retrieved here consistently uses **ARIH1** to denote the human RBR-family E3 ligase **HHARI**, matching UniProt **Q9Y4X5** and the described **Ariadne/RBR** domain organization (RING1–IBR–RING2 plus Ariadne autoinhibitory region). (wang2023theunifyingcatalytic pages 1-2, smit2013ubiquitinchainformation pages 24-26)

## 1) Key concepts and definitions (current understanding)
### 1.1 ARIH1 is an RBR (RING-between-RING) E3 ubiquitin ligase
RBR E3 ligases are defined by a **RING1–IBR–RING2** module and use a **two-step** RING/HECT-hybrid catalytic mechanism. In step 1, a ubiquitin-charged E2 binds **RING1** and transfers ubiquitin to the E3’s **RING2 catalytic cysteine** (a **transthiolation** reaction). In step 2, ubiquitin is transferred from the E3~Ub thioester to a substrate lysine (aminolysis). This general mechanism explicitly includes **HHARI/ARIH1** as a canonical member. (wang2023theunifyingcatalytic pages 1-2)

### 1.2 Core reaction catalyzed and substrate specificity (functional definition)
**Reaction (EC 2.3.2.31)**: transfer of ubiquitin from an E2 conjugating enzyme to substrate proteins via an ARIH1~Ub thioester intermediate. In physiological contexts, the strongest mechanistic evidence supports ARIH1’s role as a **CRL-associated “priming” E3**, placing an activated ubiquitin transfer module next to substrates bound to **neddylated cullin-RING ligases (CRLs)**—particularly **SCF (CUL1–RBX1–SKP1–F-box)** complexes. This geometry is proposed to be especially important for **folded/spatially constrained substrates** that canonical RING-only mechanisms cannot efficiently ubiquitinate. (hornghetko2021ubiquitinligationto pages 1-2, lin2024diversityofstructure pages 1-3)

### 1.3 Neddylation and CRL–RBR “E3–E3” cooperation
A major current paradigm is that **neddylated CRLs recruit and activate ARIH-family RBR ligases**. Neddylation-induced conformational changes in cullins enable catalysis and can relieve ARIH autoinhibition; ARIH1 then performs the catalytic ubiquitin transfer while the CRL scaffold handles substrate recruitment and E2 positioning. (hornghetko2021ubiquitinligationto pages 1-2, lin2024diversityofstructure pages 1-3)

## 2) Molecular mechanism of ARIH1 (what it does and how)
### 2.1 Autoinhibition and activation
ARIH1/HHARI is **autoinhibited** by its **Ariadne domain** and becomes activated through interactions with **neddylated cullins/CRLs** (and in broader RBR literature, phosphorylation is also described as an activating input for HHARI). (wang2023theunifyingcatalytic pages 1-2, hornghetko2024noncanonicalassemblyneddylation pages 2-3)

### 2.2 E2 partners (E2-to-E3 handoff)
In the best-defined structural/biochemical pathway (SCF–ARIH1 E3–E3 super-assembly), ubiquitin is transferred from **UBE2L3 (UbcH7)** to the **ARIH1 catalytic cysteine** and then to an SCF-bound substrate. (hornghetko2021ubiquitinligationto pages 1-2)

### 2.3 Structural mechanism: SCF–ARIH1 E3–E3 super-assembly
Horn-Ghetko et al. resolved intermediates by cryo-EM that visualize the sequence: **E2~Ub → ARIH1 catalytic cysteine → substrate** in the context of a **neddylated SCF complex**. This provides direct mechanistic support that ARIH1 can function as a **catalytic partner** of CRLs rather than acting solely as a standalone E3. (hornghetko2021ubiquitinligationto pages 1-2)

Visual evidence supporting this mechanism is shown in the extracted figure panels (transition states and cycle schematic). (hornghetko2021ubiquitinligationto media a3b226ac, hornghetko2021ubiquitinligationto media f3b6a2dc)

### 2.4 2023 mechanistic consolidation for RBRs (including ARIH1)
A 2023 Nature Communications study synthesized “unifying” RBR features, including the requirement for an **open E2~Ub** and alignment of the **RING2 catalytic cysteine** for transthiolation. HHARI/ARIH1 is explicitly included among RBRs whose activation involves interactions with **neddylated cullins**. (wang2023theunifyingcatalytic pages 1-2)

## 3) Biological roles, pathways, and cellular localization
### 3.1 Proteostasis and cell-cycle control via CRL substrates
In the SCF context, ARIH1 supports ubiquitination of substrates presented by F-box proteins (examples include **phosphorylated cyclin E** and **p27**), and perturbations stabilize multiple CRL substrates; genome-scale screening evidence places ARIH1 among genes important for cell viability in the same neighborhood as core SCF/neddylation components. (hornghetko2021ubiquitinligationto pages 1-2)

### 3.2 EMT and cancer progression via hnRNP E1/PCBP1 stability
A mechanistically focused cancer study identified **hnRNP E1 (PCBP1)** as a direct ARIH1 substrate: ARIH1 promotes **K48-linked ubiquitination** and proteasomal degradation of hnRNP E1, and mutational analysis highlighted ubiquitinated lysines including **K23, K314, K351** with **K314R** increasing stability and reducing ubiquitination. (howley2022theubiquitine3 pages 1-3, howley2022theubiquitine3 pages 8-9)

Functionally, ARIH1 knockdown delayed EMT and reduced invasion/stemness and tumor outcomes, whereas ARIH1 overexpression promoted EMT/invasion phenotypes; the study reports quantitative elements including **74 enriched ARIH1 proximity interactors** and statistically significant in vivo/clinical comparisons (e.g., paired tumor vs metastasis IHC and xenograft endpoints with reported P-values). (howley2022theubiquitine3 pages 8-9, howley2022theubiquitine3 pages 6-8)

### 3.3 Translation control connections (context and evidence base)
ARIH1 has been linked to translation control contexts (including DNA damage–related translation arrest) in the cancer-focused ARIH1 study, and ARIH1/HHARI has been discussed in the 4EHP/eIF4E2 literature as associating with 4EHP under specific cellular conditions. However, in the retrieved evidence set, the most direct substrate-level and phenotype-level support is for **hnRNP E1** and **CRL/SCF substrates** rather than for a single definitive translation-factor substrate. (howley2022theubiquitine3 pages 1-3, smit2013ubiquitinchainformation pages 26-29)

### 3.4 Innate immune signaling (emerging/less mature evidence)
A recent preprint reports HHARI/ARIH1 as an activator of **RIG-I–mediated type I interferon** signaling in a **neddylation-dependent** manner. It reports that the **RING2 catalytic cysteine mutant (C357A)** abolishes the phenotype, that HHARI physically interacts with RIG-I, and that inhibiting neddylation (NAE inhibitor **MLN4924**) suppresses HHARI-driven responses (including IFNβ secretion and downstream signaling readouts). This supports a model where HHARI’s regulation by neddylated CRLs can be functionally coupled to antiviral signaling. Because this is a preprint, it should be treated as emerging rather than fully consolidated. (kontra2025theacidicnterminus pages 33-35, kontra2025theacidicnterminus pages 9-12)

### 3.5 Subcellular localization
In tumor/pathology and cell-based studies, ARIH1 was detected in both **cytoplasm and nucleus** by staining, consistent with a role in diverse protein quality control and regulatory circuits. In the core mechanistic work, ARIH1 localizes functionally through **complex formation** with neddylated CRL assemblies (e.g., SCF). (howley2022theubiquitine3 pages 6-8, hornghetko2021ubiquitinligationto pages 1-2)

## 4) Recent developments (prioritize 2023–2024)
### 4.1 2024: refined view of CRL geometry and catalytic partnering
A 2024 Current Opinion in Structural Biology review highlights ARIH1/ARIH2 as CRL-associated RBR ligases that can perform **priming** ubiquitination and emphasizes that neddylation can strongly accelerate CRL reactions (including an example of **~2000-fold acceleration** for a UBE2D-mediated reaction in the CRL context). It also articulates a functional division where ARIH1 is favored for substrates that are geometrically hard to reach for the E2 in a RING-only mechanism. (lin2024diversityofstructure pages 3-5)

### 4.2 2024: broader cullin–RBR chimeric assemblies
A 2024 Nature Structural & Molecular Biology study on the vertebrate-specific CUL9 complex discusses ARIH-family RBR catalytic principles and emphasizes ARIH1-like autoinhibition/activation logic involving **neddylated cullins** and **RBX RING** interactions, underscoring that cullin–RBR cooperation is a recurring design in the ubiquitin system. (hornghetko2024noncanonicalassemblyneddylation pages 2-3)

### 4.3 2023: mechanistic unification of the RBR family including HHARI
The 2023 Nature Communications paper consolidated structural/biochemical principles underlying RBR catalysis, explicitly positioning HHARI/ARIH1 as part of an RBR family that uses a conserved transthiolation-centered catalytic cycle and can be activated in the context of neddylated cullins. (wang2023theunifyingcatalytic pages 1-2)

## 5) Current applications and real-world implementations
### 5.1 Targeted protein degradation (TPD) and PROTAC ecosystem (ARIH1-adjacent)
While ARIH1 itself is not yet a common recruited ligase in marketed degraders, its core partner system—**cullin-RING ligases**—is central to real-world TPD. The 2024 structural review notes that **CRL2\u1d5bVHL** is a commonly used E3 ligase scaffold in PROTAC designs, highlighting the clinical/biotech relevance of CRLs. Because ARIH1 can act as a CRL catalytic partner for certain substrates, mechanistic understanding of ARIH1 expands the design space for how CRL-based ubiquitination can be engineered or inhibited. (lin2024diversityofstructure pages 3-5)

### 5.2 Neddylation as a pharmacologic lever (relevant to ARIH1 activation)
Because ARIH1 activation in multiple contexts depends on **neddylated CRLs**, neddylation is an actionable upstream node. In immune signaling experiments, neddylation inhibition with **MLN4924** suppressed HHARI/ARIH1-dependent phenotypes (preprint evidence). Conceptually, this points to neddylation as a potential therapeutic control point for processes where ARIH1 cooperates with CRLs, including CRL-driven proteostasis/cell-cycle and possibly innate immune signaling. (kontra2025theacidicnterminus pages 33-35)

### 5.3 Disease-oriented implementation: cancer progression mechanisms
ARIH1’s role in EMT and metastasis-like phenotypes (via hnRNP E1 stability control) positions it as a mechanistically grounded node for biomarker development or pathway intervention in oncology research settings. (howley2022theubiquitine3 pages 6-8, howley2022theubiquitine3 pages 1-3)

## 6) Expert synthesis and analysis (what authoritative sources imply)
### 6.1 Primary function (most strongly supported)
The strongest convergent evidence supports ARIH1 as a **catalytic RBR E3 that cooperates with neddylated CRLs** to enable ubiquitination of otherwise geometrically challenging substrates—acting as a “catalytic extender/primer” of CRL ubiquitination capacity rather than merely a standalone ligase. (hornghetko2021ubiquitinligationto pages 1-2, lin2024diversityofstructure pages 1-3)

### 6.2 Where the field is still uncertain
*Substrate scope:* Beyond SCF-presented substrates and hnRNP E1, ARIH1 substrate identification remains incomplete; reviews emphasize context dependence (substrate geometry, cullin identity, E2 choice). (lin2024diversityofstructure pages 1-3)

*Innate immunity:* HHARI/ARIH1–RIG-I signaling is supported by mechanistic perturbation in a preprint but awaits broader replication and peer-reviewed consolidation. (kontra2025theacidicnterminus pages 33-35)

### 6.3 Constraint/essentiality
Multiple lines of evidence are consistent with ARIH1 being fitness-relevant/essential: it appears as essential in cell-viability CRISPR screens in mechanistic work, and human population constraint commentary notes predicted loss-of-function variants are rare (preprint). (hornghetko2021ubiquitinligationto pages 1-2, kontra2025theacidicnterminus pages 9-12)

## 7) Relevant recent statistics and quantitative data (from available sources)
- Human E3 ligase repertoire: **>600 E3 ligases** cited in a 2023 review, providing scale/context for ARIH1 within the UPS. (jeong2023targetinge3ubiquitin pages 1-2)
- NEDD8 impact on CRL catalysis: a 2024 structural review reports neddylation can accelerate a UBE2D-mediated CRL reaction by **~2000-fold** (context for why neddylation-dependent ARIH activation is biologically potent). (lin2024diversityofstructure pages 3-5)
- ARIH1 interactome size in a focused cancer study: **74 enriched ARIH1 interactors** via miniTurboID proximity labeling/MS. (howley2022theubiquitine3 pages 8-9)
- Quantitative/statistical phenotypes in cancer models: reported significant differences across IHC comparisons (paired tests) and in vivo tumor/colonization outcomes with reported P-values and group sizes in the ARIH1–hnRNP E1 study. (howley2022theubiquitine3 pages 6-8)
- Innate immune signaling readouts (emerging): IFNβ ELISA plots show outputs scaled up to approximately **6,000 pg/mL** and suppression by **MLN4924 10 μM** in HHARI-driven assays (preprint). (kontra2025theacidicnterminus pages 36-36, kontra2025theacidicnterminus pages 33-35)

## 8) Database-level disease associations (hypothesis-generating)
Open Targets lists ARIH1 associations (varying strength and evidence counts) with broad disease categories including **neoplasm**, **aortic aneurysm**, **thoracic aortic aneurysm**, and **neurodegenerative disease**. These should be used as starting points for targeted literature review rather than as definitive causal claims. (OpenTargets Search: -ARIH1)

## Summary table
The following table consolidates ARIH1’s identity, mechanism, regulation, substrates, roles, and recent developments (with URLs and publication dates).

| Functional aspect | Specific details | Key evidence type | Primary supporting citations | Source URL + publication date |
|---|---|---|---|---|
| Identity / verified target | Human **ARIH1** encodes **HHARI** (also called Ariadne RBR E3 ubiquitin protein ligase 1), an **RBR-family** E3 ligase with **RING1–IBR–RING2** catalytic core plus an **Ariadne** autoinhibitory region; this matches UniProt Q9Y4X5 and the Ariadne subfamily annotation. | Structural/mechanistic paper; review | (wang2023theunifyingcatalytic pages 1-2, smit2013ubiquitinchainformation pages 24-26) | Wang et al., *Nat Commun* (2023-01), https://doi.org/10.1038/s41467-023-35871-z; Smit (2013, thesis/review-style source) |
| Domain architecture | RING1 recruits E2~Ub, IBR links the RBR scaffold, and RING2 contains the **catalytic cysteine** for transthiolation; the **Ariadne domain** restrains the catalytic module in an autoinhibited state until activation. | Structural biology; biochemical mechanism | (wang2023theunifyingcatalytic pages 1-2, hornghetko2024noncanonicalassemblyneddylation pages 2-3) | Wang et al., *Nat Commun* (2023-01), https://doi.org/10.1038/s41467-023-35871-z; Horn-Ghetko et al., *Nat Struct Mol Biol* (2024-04), https://doi.org/10.1038/s41594-024-01257-y |
| Catalytic mechanism | ARIH1 uses the canonical **RBR two-step mechanism**: ubiquitin is transferred from an E2 to the **RING2 catalytic cysteine** of ARIH1 by **transthiolation**, then from ARIH1 to substrate by aminolysis. | Cryo-EM; biochemistry; mechanistic review | (wang2023theunifyingcatalytic pages 1-2, hornghetko2021ubiquitinligationto pages 1-2) | Wang et al., *Nat Commun* (2023-01), https://doi.org/10.1038/s41467-023-35871-z; Horn-Ghetko et al., *Nature* (2021-02), https://doi.org/10.1038/s41586-021-03197-9 |
| Activation by neddylated CRLs | A key current model is that **neddylated cullin-RING ligases (CRLs)** activate ARIH1 by relieving autoinhibition and positioning ARIH1 for substrate ubiquitination. ARIH1 cooperates especially with **RBX1-containing CUL1/CUL2/CUL3** complexes. | Cryo-EM; structural/mechanistic review | (hornghetko2024noncanonicalassemblyneddylation pages 2-3, wang2023theunifyingcatalytic pages 1-2, lin2024diversityofstructure pages 1-3) | Horn-Ghetko et al., *Nat Struct Mol Biol* (2024-04), https://doi.org/10.1038/s41594-024-01257-y; Wang et al., *Nat Commun* (2023-01), https://doi.org/10.1038/s41467-023-35871-z; Lin & Komives, *Curr Opin Struct Biol* (2024-10), https://doi.org/10.1016/j.sbi.2024.102879 |
| E3–E3 super-assembly with SCF ligases | In a landmark model, **neddylated SCF (CUL1–RBX1–SKP1–F-box) complexes** and ARIH1 form an **E3–E3 super-assembly**. Cryo-EM visualized transfer from **UBE2L3 to the ARIH1 catalytic cysteine and then to SCF-bound substrate**, explaining how CRLs ubiquitinate geometrically difficult substrates. | Cryo-EM; chemical probes; biochemistry | (hornghetko2021ubiquitinligationto pages 1-2, hornghetko2021ubiquitinligationto media a3b226ac, hornghetko2021ubiquitinligationto media f3b6a2dc) | Horn-Ghetko et al., *Nature* (2021-02), https://doi.org/10.1038/s41586-021-03197-9 |
| E2 partners | ARIH1 is most strongly linked to **UBE2L3/UbcH7** as the donor E2 in the SCF–ARIH1 pathway; broader RBR work also uses **UbcH5B/UBE2D-family** conjugates to interrogate RBR catalysis, and older literature reported interaction with **UBE2L3 and UBE2L6**. | Cryo-EM; ITC/biochemistry; older interaction literature | (hornghetko2021ubiquitinligationto pages 1-2, wang2023theunifyingcatalytic pages 1-2, smit2013ubiquitinchainformation pages 26-29, kontra2025theacidicnterminus pages 37-37) | Horn-Ghetko et al., *Nature* (2021-02), https://doi.org/10.1038/s41586-021-03197-9; Wang et al., *Nat Commun* (2023-01), https://doi.org/10.1038/s41467-023-35871-z |
| Substrate class specificity | ARIH1 appears particularly important for **folded or spatially constrained CRL substrates** that a canonical RING E2 cannot easily reach; by contrast, some extended or disordered substrates can be ubiquitinated without ARIH1. | Mechanistic study; structural review | (hornghetko2021ubiquitinligationto pages 1-2, lin2024diversityofstructure pages 1-3) | Horn-Ghetko et al., *Nature* (2021-02), https://doi.org/10.1038/s41586-021-03197-9; Lin & Komives, *Curr Opin Struct Biol* (2024-10), https://doi.org/10.1016/j.sbi.2024.102879 |
| Representative CRL-linked substrates | In the SCF context, ARIH1 contributes to ubiquitination of substrates such as **phosphorylated cyclin E** and **p27**, and ARIH1 knockdown stabilizes multiple CRL substrates. | Cryo-EM; biochemical and cellular perturbation | (hornghetko2021ubiquitinligationto pages 1-2) | Horn-Ghetko et al., *Nature* (2021-02), https://doi.org/10.1038/s41586-021-03197-9 |
| Direct substrate: hnRNP E1 (PCBP1) | **hnRNP E1** is a validated ARIH1 substrate in breast cancer models. ARIH1 promotes **K48-linked ubiquitination** and proteasomal degradation; ubiquitinated lysines include **K23, K314, K351**, with **K314R** increasing stability and reducing ubiquitination. | Yeast 2-hybrid; miniTurboID proteomics; CHX chase; IP/immunoblot; mutagenesis | (howley2022theubiquitine3 pages 8-9, howley2022theubiquitine3 pages 1-3) | Howley et al., *Oncogene* (2022-01), https://doi.org/10.1038/s41388-022-02199-9 |
| Putative or previous substrate links | Earlier literature associated HHARI/ARIH1 with **4EHP/eIF4E2** and with degradation of **synphilin-1** and **SIM2** in cells, but these links are less central and generally less definitive than the CRL-priming and hnRNP E1 data. | Earlier cell-based studies; review | (smit2013ubiquitinchainformation pages 26-29) | Smit (2013, thesis/review-style source) |
| Translation control / proteostasis | Reviews of **4EHP/eIF4E2** note that under stress or DNA-damage contexts **HHARI/ARIH1 accumulates and associates with 4EHP**, linking ARIH1 to translational repression pathways; ARIH1 has also been implicated in DNA damage-induced translational arrest in cancer cells. | Review; prior cell biology | (howley2022theubiquitine3 pages 8-9) | Christie & Igreja, *FEBS J* (2023-11), https://doi.org/10.1111/febs.16275; Howley et al., *Oncogene* (2022-01), https://doi.org/10.1038/s41388-022-02199-9 |
| EMT / cancer progression | ARIH1 promotes **EMT**, invasion, stemness, and tumor progression in breast cancer models; ARIH1 knockdown delays EMT, reduces invasion, and lowers tumor formation, while overexpression has the opposite effect. | Cell assays; xenografts; IHC; proteomics | (howley2022theubiquitine3 pages 1-3, howley2022theubiquitine3 pages 6-8) | Howley et al., *Oncogene* (2022-01), https://doi.org/10.1038/s41388-022-02199-9 |
| Quantitative cancer-related findings | MiniTurboID proximity labeling identified **74 enriched ARIH1 interactors**; metastasis IHC analyses in matched samples reported significant ARIH1 elevation (**paired t-test P<0.05**), and xenograft or lung-colonization effects included significant differences (**for example, two-way ANOVA with Bonferroni, P<0.001 in reported experiments**). | Quantitative proteomics; pathology; in vivo assays | (howley2022theubiquitine3 pages 8-9, howley2022theubiquitine3 pages 6-8) | Howley et al., *Oncogene* (2022-01), https://doi.org/10.1038/s41388-022-02199-9 |
| Innate immunity / RIG-I signaling | Recent work links HHARI/ARIH1 to **RIG-I-mediated type I interferon signaling**. Catalytic activity is required (**C357A inactive**), the acidic N-terminus is important, HHARI can interact with **RIG-I**, and responses are strongly **neddylation-dependent**. | Preprint; cell signaling assays; co-IP; ELISA; microscopy | (kontra2025theacidicnterminus pages 9-12, kontra2025theacidicnterminus pages 33-35, kontra2025theacidicnterminus pages 36-37) | Kontra et al., *bioRxiv* (2025-02), https://doi.org/10.1101/2025.02.01.636034 |
| Quantitative immune findings | In interferon assays, HHARI increased **IFNβ secretion** with readouts scaled up to about **6,000 pg/mL** in figures; **MLN4924 (10 μM)** suppressed HHARI-dependent signaling, and **30 nM siRNA** against **DDX58/RIG-I** or **MAVS** reduced HHARI-driven responses. | ELISA; inhibitor studies; siRNA perturbation | (kontra2025theacidicnterminus pages 36-36, kontra2025theacidicnterminus pages 33-35, kontra2025theacidicnterminus pages 36-37) | Kontra et al., *bioRxiv* (2025-02), https://doi.org/10.1101/2025.02.01.636034 |
| Localization | ARIH1 is primarily an **intracellular** ligase acting in the **cytoplasm and nucleus**; tumor studies detected ARIH1 staining in both compartments, and functionally ARIH1 operates in multiprotein complexes with CRLs, RNA-binding factors, and signaling proteins. | IHC/cell biology; structural complex data | (howley2022theubiquitine3 pages 6-8, hornghetko2021ubiquitinligationto pages 1-2) | Howley et al., *Oncogene* (2022-01), https://doi.org/10.1038/s41388-022-02199-9; Horn-Ghetko et al., *Nature* (2021-02), https://doi.org/10.1038/s41586-021-03197-9 |
| Essentiality / constraint | ARIH1 behaves like an **essential or fitness-relevant UPS component** in several datasets: genome-wide CRISPR screens identified ARIH1 as important for cell viability, and gnomAD-based commentary notes that predicted human **loss-of-function variants are very rare**. | CRISPR screens; population genetics commentary | (hornghetko2021ubiquitinligationto pages 1-2, kontra2025theacidicnterminus pages 9-12) | Horn-Ghetko et al., *Nature* (2021-02), https://doi.org/10.1038/s41586-021-03197-9; Kontra et al., *bioRxiv* (2025-02), https://doi.org/10.1101/2025.02.01.636034 |
| Disease links / database-level associations | Open Targets lists low-to-moderate evidence links between ARIH1 and **neoplasm**, **aortic aneurysm**, **thoracic aortic aneurysm**, **neurodegenerative disease**, and **abruptio placentae**; these are hypothesis-generating rather than definitive functional assignments. | Database aggregation | (OpenTargets Search: -ARIH1) | Open Targets Platform query for ARIH1 (accessed via tool context; no publication date provided) |
| Key 2023 development | The 2023 mechanistic synthesis strengthened the view that **HHARI/ARIH1 conforms to a unifying RBR catalytic mechanism**, emphasizing the open E2~Ub conformation and allosteric activation features shared across RBR ligases. | High-impact mechanistic paper | (wang2023theunifyingcatalytic pages 1-2) | Wang et al., *Nat Commun* (2023-01), https://doi.org/10.1038/s41467-023-35871-z |
| Key 2024 developments | 2024 studies and reviews extended ARIH1 functional annotation by framing it as a **geometrically optimized catalytic partner for CRLs** and by generalizing ARIH-type cooperation across cullin ligase systems, including noncanonical cullin–RBR assemblies. | Structural review; primary structural paper | (hornghetko2024noncanonicalassemblyneddylation pages 2-3, lin2024diversityofstructure pages 1-3) | Horn-Ghetko et al., *Nat Struct Mol Biol* (2024-04), https://doi.org/10.1038/s41594-024-01257-y; Lin & Komives, *Curr Opin Struct Biol* (2024-10), https://doi.org/10.1016/j.sbi.2024.102879 |


*Table: This table summarizes verified identity, catalytic mechanism, activation, substrate biology, pathway roles, localization, and recent developments for human ARIH1/HHARI. It prioritizes 2023–2024 sources while retaining the key 2021 and 2022 primary papers that established major mechanistic and disease-relevant functions.*

## Key visual evidence
Cryo-EM intermediates and cycle schematics supporting the **SCF–ARIH1 E3–E3** ubiquitination mechanism (E2~Ub → ARIH1 catalytic cysteine → substrate) are shown in extracted panels. (hornghetko2021ubiquitinligationto media a3b226ac, hornghetko2021ubiquitinligationto media f3b6a2dc)

References

1. (wang2023theunifyingcatalytic pages 1-2): Xiangyi S. Wang, Thomas R. Cotton, Sarah J. Trevelyan, Lachlan W. Richardson, Wei Ting Lee, John Silke, and Bernhard C. Lechtenberg. The unifying catalytic mechanism of the ring-between-ring e3 ubiquitin ligase family. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35871-z, doi:10.1038/s41467-023-35871-z. This article has 65 citations and is from a highest quality peer-reviewed journal.

2. (smit2013ubiquitinchainformation pages 24-26): J Smit. Ubiquitin chain formation by rbr e3-ligases. Unknown journal, 2013.

3. (hornghetko2021ubiquitinligationto pages 1-2): Daniel Horn-Ghetko, David T. Krist, J. Rajan Prabu, Kheewoong Baek, Monique P. C. Mulder, Maren Klügel, Daniel C. Scott, Huib Ovaa, Gary Kleiger, and Brenda A. Schulman. Ubiquitin ligation to f-box protein targets by scf–rbr e3–e3 super-assembly. Nature, 590:671-676, Feb 2021. URL: https://doi.org/10.1038/s41586-021-03197-9, doi:10.1038/s41586-021-03197-9. This article has 199 citations and is from a highest quality peer-reviewed journal.

4. (lin2024diversityofstructure pages 1-3): Calvin P. Lin and Elizabeth A. Komives. Diversity of structure and function in cullin e3 ligases. Current Opinion in Structural Biology, 88:102879, Oct 2024. URL: https://doi.org/10.1016/j.sbi.2024.102879, doi:10.1016/j.sbi.2024.102879. This article has 14 citations and is from a peer-reviewed journal.

5. (hornghetko2024noncanonicalassemblyneddylation pages 2-3): Daniel Horn-Ghetko, Linus V. M. Hopf, Ishita Tripathi-Giesgen, Jiale Du, Sebastian Kostrhon, D. Tung Vu, Viola Beier, Barbara Steigenberger, J. Rajan Prabu, Luca Stier, Elias M. Bruss, Matthias Mann, Yue Xiong, and Brenda A. Schulman. Noncanonical assembly, neddylation and chimeric cullin–ring/rbr ubiquitylation by the 1.8 mda cul9 e3 ligase complex. Nature Structural & Molecular Biology, 31:1083-1094, Apr 2024. URL: https://doi.org/10.1038/s41594-024-01257-y, doi:10.1038/s41594-024-01257-y. This article has 13 citations and is from a highest quality peer-reviewed journal.

6. (hornghetko2021ubiquitinligationto media a3b226ac): Daniel Horn-Ghetko, David T. Krist, J. Rajan Prabu, Kheewoong Baek, Monique P. C. Mulder, Maren Klügel, Daniel C. Scott, Huib Ovaa, Gary Kleiger, and Brenda A. Schulman. Ubiquitin ligation to f-box protein targets by scf–rbr e3–e3 super-assembly. Nature, 590:671-676, Feb 2021. URL: https://doi.org/10.1038/s41586-021-03197-9, doi:10.1038/s41586-021-03197-9. This article has 199 citations and is from a highest quality peer-reviewed journal.

7. (hornghetko2021ubiquitinligationto media f3b6a2dc): Daniel Horn-Ghetko, David T. Krist, J. Rajan Prabu, Kheewoong Baek, Monique P. C. Mulder, Maren Klügel, Daniel C. Scott, Huib Ovaa, Gary Kleiger, and Brenda A. Schulman. Ubiquitin ligation to f-box protein targets by scf–rbr e3–e3 super-assembly. Nature, 590:671-676, Feb 2021. URL: https://doi.org/10.1038/s41586-021-03197-9, doi:10.1038/s41586-021-03197-9. This article has 199 citations and is from a highest quality peer-reviewed journal.

8. (howley2022theubiquitine3 pages 1-3): Breege V. Howley, Bidyut Mohanty, Annamarie Dalton, Simon Grelet, Joseph Karam, Toros Dincman, and Philip H. Howe. The ubiquitin e3 ligase arih1 regulates hnrnp e1 protein stability, emt and breast cancer progression. Oncogene, 41:1679-1690, Jan 2022. URL: https://doi.org/10.1038/s41388-022-02199-9, doi:10.1038/s41388-022-02199-9. This article has 40 citations and is from a domain leading peer-reviewed journal.

9. (howley2022theubiquitine3 pages 8-9): Breege V. Howley, Bidyut Mohanty, Annamarie Dalton, Simon Grelet, Joseph Karam, Toros Dincman, and Philip H. Howe. The ubiquitin e3 ligase arih1 regulates hnrnp e1 protein stability, emt and breast cancer progression. Oncogene, 41:1679-1690, Jan 2022. URL: https://doi.org/10.1038/s41388-022-02199-9, doi:10.1038/s41388-022-02199-9. This article has 40 citations and is from a domain leading peer-reviewed journal.

10. (howley2022theubiquitine3 pages 6-8): Breege V. Howley, Bidyut Mohanty, Annamarie Dalton, Simon Grelet, Joseph Karam, Toros Dincman, and Philip H. Howe. The ubiquitin e3 ligase arih1 regulates hnrnp e1 protein stability, emt and breast cancer progression. Oncogene, 41:1679-1690, Jan 2022. URL: https://doi.org/10.1038/s41388-022-02199-9, doi:10.1038/s41388-022-02199-9. This article has 40 citations and is from a domain leading peer-reviewed journal.

11. (smit2013ubiquitinchainformation pages 26-29): J Smit. Ubiquitin chain formation by rbr e3-ligases. Unknown journal, 2013.

12. (kontra2025theacidicnterminus pages 33-35): Ioanna Kontra, Harry Ward, Faith Vinluan, Rachel Lau, Vinothini Rajeeve, Pedro Cutillas, Benjamin Stieglitz, and Myles J. Lewis. The acidic n-terminus of hhari and neddylation are essential for the activation and maintenance of rig-i-mediated type i interferon response. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.01.636034, doi:10.1101/2025.02.01.636034. This article has 0 citations.

13. (kontra2025theacidicnterminus pages 9-12): Ioanna Kontra, Harry Ward, Faith Vinluan, Rachel Lau, Vinothini Rajeeve, Pedro Cutillas, Benjamin Stieglitz, and Myles J. Lewis. The acidic n-terminus of hhari and neddylation are essential for the activation and maintenance of rig-i-mediated type i interferon response. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.01.636034, doi:10.1101/2025.02.01.636034. This article has 0 citations.

14. (lin2024diversityofstructure pages 3-5): Calvin P. Lin and Elizabeth A. Komives. Diversity of structure and function in cullin e3 ligases. Current Opinion in Structural Biology, 88:102879, Oct 2024. URL: https://doi.org/10.1016/j.sbi.2024.102879, doi:10.1016/j.sbi.2024.102879. This article has 14 citations and is from a peer-reviewed journal.

15. (jeong2023targetinge3ubiquitin pages 1-2): Yelin Jeong, Ah-Reum Oh, Young Hoon Jung, HyunJoon Gi, Young Un Kim, and KyeongJin Kim. Targeting e3 ubiquitin ligases and their adaptors as a therapeutic strategy for metabolic diseases. Experimental &amp; Molecular Medicine, 55:2097-2104, Oct 2023. URL: https://doi.org/10.1038/s12276-023-01087-w, doi:10.1038/s12276-023-01087-w. This article has 56 citations and is from a peer-reviewed journal.

16. (kontra2025theacidicnterminus pages 36-36): Ioanna Kontra, Harry Ward, Faith Vinluan, Rachel Lau, Vinothini Rajeeve, Pedro Cutillas, Benjamin Stieglitz, and Myles J. Lewis. The acidic n-terminus of hhari and neddylation are essential for the activation and maintenance of rig-i-mediated type i interferon response. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.01.636034, doi:10.1101/2025.02.01.636034. This article has 0 citations.

17. (OpenTargets Search: -ARIH1): Open Targets Query (-ARIH1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

18. (kontra2025theacidicnterminus pages 37-37): Ioanna Kontra, Harry Ward, Faith Vinluan, Rachel Lau, Vinothini Rajeeve, Pedro Cutillas, Benjamin Stieglitz, and Myles J. Lewis. The acidic n-terminus of hhari and neddylation are essential for the activation and maintenance of rig-i-mediated type i interferon response. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.01.636034, doi:10.1101/2025.02.01.636034. This article has 0 citations.

19. (kontra2025theacidicnterminus pages 36-37): Ioanna Kontra, Harry Ward, Faith Vinluan, Rachel Lau, Vinothini Rajeeve, Pedro Cutillas, Benjamin Stieglitz, and Myles J. Lewis. The acidic n-terminus of hhari and neddylation are essential for the activation and maintenance of rig-i-mediated type i interferon response. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.01.636034, doi:10.1101/2025.02.01.636034. This article has 0 citations.

## Citations

1. wang2023theunifyingcatalytic pages 1-2
2. hornghetko2021ubiquitinligationto pages 1-2
3. lin2024diversityofstructure pages 3-5
4. hornghetko2024noncanonicalassemblyneddylation pages 2-3
5. kontra2025theacidicnterminus pages 33-35
6. lin2024diversityofstructure pages 1-3
7. smit2013ubiquitinchainformation pages 26-29
8. smit2013ubiquitinchainformation pages 24-26
9. kontra2025theacidicnterminus pages 9-12
10. kontra2025theacidicnterminus pages 36-36
11. kontra2025theacidicnterminus pages 37-37
12. kontra2025theacidicnterminus pages 36-37
13. https://doi.org/10.1038/s41467-023-35871-z;
14. https://doi.org/10.1038/s41594-024-01257-y
15. https://doi.org/10.1038/s41586-021-03197-9
16. https://doi.org/10.1038/s41594-024-01257-y;
17. https://doi.org/10.1016/j.sbi.2024.102879
18. https://doi.org/10.1038/s41586-021-03197-9;
19. https://doi.org/10.1038/s41467-023-35871-z
20. https://doi.org/10.1038/s41388-022-02199-9
21. https://doi.org/10.1111/febs.16275;
22. https://doi.org/10.1101/2025.02.01.636034
23. https://doi.org/10.1038/s41388-022-02199-9;
24. https://doi.org/10.1038/s41467-023-35871-z,
25. https://doi.org/10.1038/s41586-021-03197-9,
26. https://doi.org/10.1016/j.sbi.2024.102879,
27. https://doi.org/10.1038/s41594-024-01257-y,
28. https://doi.org/10.1038/s41388-022-02199-9,
29. https://doi.org/10.1101/2025.02.01.636034,
30. https://doi.org/10.1038/s12276-023-01087-w,