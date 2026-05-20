---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T22:03:47.749752'
end_time: '2026-05-10T22:15:56.523375'
duration_seconds: 728.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PKM
  gene_symbol: PKM
  uniprot_accession: P14618
  protein_description: 'RecName: Full=Pyruvate kinase PKM; EC=2.7.1.40 {ECO:0000269|PubMed:15996096,
    ECO:0000269|PubMed:1854723, ECO:0000269|PubMed:20847263}; AltName: Full=Cytosolic
    thyroid hormone-binding protein {ECO:0000303|PubMed:2813362}; Short=CTHBP {ECO:0000303|PubMed:2813362};
    AltName: Full=Opa-interacting protein 3 {ECO:0000303|PubMed:9466265}; Short=OIP-3
    {ECO:0000303|PubMed:9466265}; AltName: Full=Pyruvate kinase 2/3; AltName: Full=Pyruvate
    kinase muscle isozyme; AltName: Full=Threonine-protein kinase PKM2 {ECO:0000305};
    EC=2.7.11.1 {ECO:0000269|PubMed:22901803, ECO:0000269|PubMed:24120661}; AltName:
    Full=Thyroid hormone-binding protein 1; Short=THBP1; AltName: Full=Tumor M2-PK;
    AltName: Full=Tyrosine-protein kinase PKM2 {ECO:0000305}; EC=2.7.10.2 {ECO:0000269|PubMed:22306293,
    ECO:0000269|PubMed:24120661}; AltName: Full=p58;'
  gene_info: Name=PKM; Synonyms=OIP3 {ECO:0000303|PubMed:9466265}, PK2, PK3, PKM2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the pyruvate kinase family. .
  protein_domains: Pyr_Knase. (IPR001697); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813);
    Pyrv_kinase-like_dom_sf. (IPR040442); Pyrv_Knase-like_insert_dom_sf. (IPR011037);
    Pyrv_Knase_AS. (IPR018209)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P14618
- **Protein Description:** RecName: Full=Pyruvate kinase PKM; EC=2.7.1.40 {ECO:0000269|PubMed:15996096, ECO:0000269|PubMed:1854723, ECO:0000269|PubMed:20847263}; AltName: Full=Cytosolic thyroid hormone-binding protein {ECO:0000303|PubMed:2813362}; Short=CTHBP {ECO:0000303|PubMed:2813362}; AltName: Full=Opa-interacting protein 3 {ECO:0000303|PubMed:9466265}; Short=OIP-3 {ECO:0000303|PubMed:9466265}; AltName: Full=Pyruvate kinase 2/3; AltName: Full=Pyruvate kinase muscle isozyme; AltName: Full=Threonine-protein kinase PKM2 {ECO:0000305}; EC=2.7.11.1 {ECO:0000269|PubMed:22901803, ECO:0000269|PubMed:24120661}; AltName: Full=Thyroid hormone-binding protein 1; Short=THBP1; AltName: Full=Tumor M2-PK; AltName: Full=Tyrosine-protein kinase PKM2 {ECO:0000305}; EC=2.7.10.2 {ECO:0000269|PubMed:22306293, ECO:0000269|PubMed:24120661}; AltName: Full=p58;
- **Gene Information:** Name=PKM; Synonyms=OIP3 {ECO:0000303|PubMed:9466265}, PK2, PK3, PKM2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the pyruvate kinase family. .
- **Key Domains:** Pyr_Knase. (IPR001697); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813); Pyrv_kinase-like_dom_sf. (IPR040442); Pyrv_Knase-like_insert_dom_sf. (IPR011037); Pyrv_Knase_AS. (IPR018209)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PKM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PKM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PKM** (gene ID: PKM, UniProt: P14618) in human.

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
- **UniProt Accession:** P14618
- **Protein Description:** RecName: Full=Pyruvate kinase PKM; EC=2.7.1.40 {ECO:0000269|PubMed:15996096, ECO:0000269|PubMed:1854723, ECO:0000269|PubMed:20847263}; AltName: Full=Cytosolic thyroid hormone-binding protein {ECO:0000303|PubMed:2813362}; Short=CTHBP {ECO:0000303|PubMed:2813362}; AltName: Full=Opa-interacting protein 3 {ECO:0000303|PubMed:9466265}; Short=OIP-3 {ECO:0000303|PubMed:9466265}; AltName: Full=Pyruvate kinase 2/3; AltName: Full=Pyruvate kinase muscle isozyme; AltName: Full=Threonine-protein kinase PKM2 {ECO:0000305}; EC=2.7.11.1 {ECO:0000269|PubMed:22901803, ECO:0000269|PubMed:24120661}; AltName: Full=Thyroid hormone-binding protein 1; Short=THBP1; AltName: Full=Tumor M2-PK; AltName: Full=Tyrosine-protein kinase PKM2 {ECO:0000305}; EC=2.7.10.2 {ECO:0000269|PubMed:22306293, ECO:0000269|PubMed:24120661}; AltName: Full=p58;
- **Gene Information:** Name=PKM; Synonyms=OIP3 {ECO:0000303|PubMed:9466265}, PK2, PK3, PKM2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the pyruvate kinase family. .
- **Key Domains:** Pyr_Knase. (IPR001697); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813); Pyrv_kinase-like_dom_sf. (IPR040442); Pyrv_Knase-like_insert_dom_sf. (IPR011037); Pyrv_Knase_AS. (IPR018209)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PKM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PKM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PKM** (gene ID: PKM, UniProt: P14618) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive Research Report: Human **PKM** (UniProt **P14618**) — Functional Annotation, Regulation, and Translational Relevance (2023–2024 prioritized)

### 1) Gene/protein identification and definitions (verification)

**Target verified:** The gene symbol **PKM** in this report refers specifically to **human pyruvate kinase PKM (pyruvate kinase M1/2)** consistent with UniProt accession **P14618**, a member of the pyruvate kinase family catalyzing the terminal step of glycolysis. Multiple retrieved sources explicitly tie “PKM/PKM2” to UniProt **P14618** and to pyruvate-kinase biochemical/structural hallmarks (e.g., glycolytic PEP→pyruvate ATP-generating step; pyruvate-kinase oligomerization; FBP allostery). (nandi2023identificationofresidues pages 10-12, li2024theregulatorynetwork pages 1-2, jemal2024nonmetabolicenzymefunction pages 1-2)

**Key definitions:**
- **PKM1 / PKM2 isoenzymes:** The PKM gene produces two major protein isoforms via **mutually exclusive alternative splicing** of a single exon: **exon 9** vs **exon 10**. (li2024theregulatorynetwork pages 1-2, oleaflores2024musclespecificpyruvatekinase pages 1-5)
- **Canonical enzymatic role:** Pyruvate kinase catalyzes transfer of phosphate from **phosphoenolpyruvate (PEP)** to **ADP**, producing **pyruvate + ATP** (EC 2.7.1.40), the final ATP-generating step of glycolysis. (hu2024roleofpyruvate pages 2-4, oleaflores2024musclespecificpyruvatekinase pages 1-5)
- **Moonlighting/noncanonical functions:** Particularly for **PKM2**, literature describes additional roles beyond metabolite conversion, including nuclear functions and kinase-like activities that interface with gene regulation and signaling. (wang2024pkm2functionsas pages 4-6, jemal2024nonmetabolicenzymefunction pages 6-8)

### 2) Core biochemistry: catalytic reaction, substrate specificity, and pathway role

**Catalyzed reaction (primary molecular function):**
PKM catalyzes the terminal glycolytic step: **PEP + ADP → pyruvate + ATP**. This reaction couples high-energy phosphate transfer to ATP production and is a principal flux-control point in glycolysis. (hu2024roleofpyruvate pages 2-4, oleaflores2024musclespecificpyruvatekinase pages 1-5)

**Pathway placement and functional implication:**
Because this step is both terminal and ATP-generating, changes in PKM activity (and especially PKM2 oligomeric state) can shift how upstream glycolytic intermediates accumulate and are diverted toward **biosynthetic side pathways** (a central concept in proliferative metabolism). (hu2024roleofpyruvate pages 2-4, li2021discoveryoffunctional pages 2-3)

### 3) Isoforms, alternative splicing, and cell-state specificity

**Alternative splicing mechanism (PKM1 vs PKM2):**
A 2024 review focused on tumor splicing networks summarizes the canonical exon usage: PKM pre-mRNA splicing produces **PKM1 and PKM2**, where **PKM1 excludes exon 10** and **PKM2 excludes exon 9** (i.e., reciprocal inclusion of exon 9 vs exon 10). (li2024theregulatorynetwork pages 1-2)

**Tissue/cell-state tendencies:**
- **PKM1** is reported as predominant in **heart, skeletal muscle, brain, and mature sperm** (more differentiated/high oxidative contexts). (li2024theregulatorynetwork pages 1-2)
- **PKM2** is enriched in **proliferating/anabolic cells** and in many tumors. (li2024theregulatorynetwork pages 1-2)

**Regulatory control of splicing (recent synthesis):**
The 2024 Biomolecules review emphasizes that splicing factors (notably hnRNP-centered networks and PTBP1-linked regulation) are core determinants of the **PKM1/PKM2 balance** in tumor progression, and that epigenetic/RNA-level mechanisms can influence whether cells use PKM1-linked oxidative metabolism or PKM2-linked glycolytic programs. (li2024theregulatorynetwork pages 1-2, li2024theregulatorynetwork pages 7-8)

### 4) Allostery, oligomerization, and quantitative regulatory features (current understanding + 2023 advances)

**Oligomeric states as functional switches:**
PKM1 is commonly described as a **constitutively active tetramer**, whereas PKM2 is conformationally plastic, interconverting between high-activity tetramers and lower-activity dimer/monomer states. This tetramer–dimer equilibrium is repeatedly invoked to explain why PKM2 can support either ATP production or anabolic rewiring (via reduced catalytic flux at the last glycolytic step). (li2021discoveryoffunctional pages 2-3, hu2024roleofpyruvate pages 2-4)

**Allosteric activation by fructose-1,6-bisphosphate (FBP):**
A transcript/isoform-focused analysis summarizes that tetrameric PKM2 is allosterically activated by **FBP**, which stabilizes the tetramer, whereas FBP release promotes conversion toward lower-activity forms. (li2021discoveryoffunctional pages 2-3)

**Amino-acid sensing and allosteric communication (2023 primary data):**
Nandi & Dey (PLOS ONE, **2023-03-10**) dissected how amino acids modulate PKM2 via a dedicated amino-acid (AA) binding pocket and transmission to the active site, providing quantitative binding/affinity effects and linking them to activity and oligomer state. Key quantitative observations include:
- For the **R106A** variant, ADP binding affinities in the presence of inhibitory AAs were markedly weakened (e.g., Val Kd ~1.2 mM; Cys Kd ~2.9 mM) vs no-AA condition (Kd = 257±24 μM). (nandi2023identificationofresidues pages 10-12)
- PEP binding affinity could shift strongly depending on AA ligand class, with activator AAs (Asn/Asp) improving PEP binding (e.g., ~9.5 μM → ~1 μM), whereas inhibitory AAs (Val/Cys) weakened binding (e.g., ~26–100 μM). (nandi2023identificationofresidues pages 10-12)
- Size-exclusion chromatography showed mutation-dependent changes in oligomer equilibrium; for example, **N70D** exhibited a tetramer plus dimer/monomer mixture without AAs, and activating AAs (Asn/Asp) increased tetrameric population consistent with activation. (nandi2023identificationofresidues pages 10-12)

These findings refine “PKM2 as a nutrient sensor” into a more mechanistically grounded picture in which distinct AA ligands perturb substrate affinities and oligomeric state through a defined signal-transmission path. (nandi2023identificationofresidues pages 10-12)

### 5) Subcellular localization: cytosolic glycolysis vs nuclear functions

**Primary localization for canonical function:**
PKM’s glycolytic role is cytosolic, consistent with glycolysis occurring in the cytoplasm. (hu2024roleofpyruvate pages 2-4)

**Nuclear PKM2 and triggers for nuclear translocation (2024 reviews):**
Recent 2024 reviews summarize that **PKM2**, particularly in non-tetrameric forms, can translocate to the nucleus where it acts in transcriptional and signaling regulation:
- In a sepsis-focused review, Hu et al. report that **ERK1/2 phosphorylation at S37** (with downstream prolyl isomerization) promotes PKM2 nuclear translocation and supports interaction with transcriptional regulators such as **HIF‑1α** and **STAT3**, linking metabolic state to inflammatory gene programs. (hu2024roleofpyruvate pages 2-4)
- In a breast-cancer-focused review, EGFR signaling is summarized as a driver of nuclear import: **EGFR activation results in PKM2 nuclear translocation**, facilitated via **importin α5**. (jemal2024nonmetabolicenzymefunction pages 8-9)
- The same review emphasizes the functional importance of **dimeric PKM2** in nuclear localization and downstream biological effects. (jemal2024nonmetabolicenzymefunction pages 6-8)

### 6) Noncanonical functions: kinase-like activities and signaling integration (2024 key advance)

#### 6.1 PKM2 as a PEP-dependent histidine kinase (major 2024 primary advance)

Wang et al. (EMBO J, **2024-05**) provide direct evidence that PKM2 “moonlights” as a **histidine kinase**:
- PKM2 catalyzes **PGAM1 histidine-11 (H11) phosphorylation** in a **PEP-dependent** manner, which is required for PGAM1 activity and supports glycolysis shunt fluxes in cancer contexts. (wang2024pkm2functionsas pages 1-2, wang2024pkm2functionsas pages 4-6)
- **Oligomeric-state dependence:** monomeric/dimeric PKM2 efficiently phosphorylates/activates PGAM1, whereas tetrameric PKM2 is ineffective. Stabilizing PKM2 tetramers (e.g., **TEPP46**) reduces PKM2–PGAM1 interaction and H11 phosphorylation. (wang2024pkm2functionsas pages 4-6)
- **Tumor-selective interaction pattern:** PKM2–PGAM1 interaction was observed across multiple tumor cell lines and was reported as barely detectable in several untransformed cell types, consistent with a model where this crosstalk is preferentially engaged in tumor metabolic rewiring. (wang2024pkm2functionsas pages 1-2)

This work is important for functional annotation because it operationally distinguishes the **canonical kinase transfer (to ADP)** from a distinct, noncanonical **PEP-dependent protein phosphorylation** activity that depends on PKM2 de-tetramerization. (wang2024pkm2functionsas pages 4-6)

#### 6.2 Nuclear “protein kinase”/transcriptional cofactor roles summarized in 2024 reviews

The 2024 Frontiers in Oncology review synthesizes literature in which nuclear PKM2 influences pathways via kinase-like functions or coactivator roles, including modulation of β-catenin transactivation and STAT3 phosphorylation-related signaling programs, and highlights that blocking nuclear translocation is a recurring therapeutic concept. (jemal2024nonmetabolicenzymefunction pages 6-8, jemal2024nonmetabolicenzymefunction pages 8-9)

A 2024 preprint on myoblast differentiation further summarizes that PKM2 has been implicated in **histone H3 phosphorylation (H3T11)** in cancer cells, and reports roles for Pkm1/Pkm2 in chromatin regulator dynamics during differentiation (noting Pkm2 dependence for incorporation of phospho-H3 marks at myogenic promoters and a role for Pkm1 in nuclear localization of Dpf2). (oleaflores2024musclespecificpyruvatekinase pages 1-5)

### 7) Current applications and real-world implementations (biomarkers/diagnostics; translational targeting)

#### 7.1 Proteomics biomarker exploration (2023–2024)

**(a) Oral squamous cell carcinoma (OSCC) saliva proteomics (2024):**
Remori et al. (Int J Mol Sci, **2024-10**, DOI: https://doi.org/10.3390/ijms252011120) analyzed saliva proteomics (10 OSCC vs 20 controls) and used a workflow combining univariate/multivariate selection and protein–protein interaction filtering.
- They report 172 differentially abundant proteins leading to a connected subset (48 proteins) to prioritize candidates; **PKM (P14618)** is explicitly highlighted as an altered glycolytic enzyme proposed as a candidate marker for follow-up validation. (remori2024predictionoforal pages 6-8)
- The authors emphasize the need for future validation cohorts to establish diagnostic performance (sensitivity/specificity), i.e., PKM is a candidate rather than a validated clinical biomarker in this dataset. (remori2024predictionoforal pages 6-8)

**(b) Perinatal asphyxia / neonatal hypoxic–ischemic encephalopathy (HIE) plasma proteomics (2023):**
Yip et al. (Biomolecules, **2023-09**, DOI: https://doi.org/10.3390/biom13101471) performed plasma proteomics in neonates with HIE.
- Study design includes 22 moderate-severe HIE newborns treated with therapeutic hypothermia (TH), with comparison groups including 10 mild HIE and 10 normal cord-blood samples (per paper abstract context; quantitative table shown for sHIE+ vs mHIE). (yip2023newbornswithfavourable pages 11-12)
- In the “most reliable proteins” table comparing favorable-outcome severe HIE (sHIE+) vs mild HIE (mHIE), **PKM (P14618-2)** is listed with **log2FC = 0.95** and **p = 3.09 × 10^-2**. (yip2023newbornswithfavourable pages 11-12)

This positions PKM as part of a **metabolic enzyme signature** associated with clinical outcome stratification in a specific neonatal critical care context (early-stage discovery/association rather than a validated clinical test). (yip2023newbornswithfavourable pages 11-12)

**(c) Saliva collection protocol affecting detectability of metabolic proteins (2023):**
Foratori-Junior et al. (Cells, **2023-05**, DOI: https://doi.org/10.3390/cells12101389) report that stimulated saliva sampling reduces or eliminates detection of multiple proteins involved in glycolysis/glucose metabolism, and specifically notes pyruvate kinase as reduced/absent in stimulated saliva in pregnancy cohorts with obesity. This is a practical methodological consideration for “real-world” biomarker work involving PKM/PKM2. (foratorijunior2023istherea pages 16-17)

**(d) Follicular fluid proteomics and embryo development context (2024):**
Przewocki et al. (Int J Mol Sci, **2024-08**, DOI: https://doi.org/10.3390/ijms25158431) analyzed 110 follicular-fluid samples from 50 oocyte donors, identifying 2182 proteins and noting protein–protein interaction patterns in which PKM2 appears as a node interacting with stress-response proteins (e.g., HSPA8). This supports that PKM2 is detectable in human reproductive biofluids and may be relevant to predictive modeling, although the excerpted text emphasizes network interpretation more than effect sizes for PKM specifically. (przewocki2024follicularfluidproteomic pages 7-8)

#### 7.2 Therapeutic targeting concepts (expert synthesis, 2024)

Two recurring expert concepts in 2024 reviews are:
1) **Shift PKM2 toward the tetrameric enzymatically active state** (or preserve canonical activity) to reduce noncanonical nuclear functions and proliferative rewiring. (hu2024roleofpyruvate pages 2-4)
2) **Block nuclear translocation** and downstream transcriptional/oncogenic signaling axes (e.g., EGFR→importin α5; ERK1/2 S37 pathway). (hu2024roleofpyruvate pages 2-4, jemal2024nonmetabolicenzymefunction pages 8-9)

Examples mentioned in reviews include small molecules and natural products proposed to inhibit PKM2 expression, nuclear entry, or downstream signaling (e.g., shikonin’s reported interference with residues around R399/400 and a putative NLS; and the concept of covalent activation promoting tetramers to block nuclear functions). (jemal2024nonmetabolicenzymefunction pages 6-8, hu2024roleofpyruvate pages 2-4)

### 8) Disease associations (database-level evidence)

Open Targets reports disease–target associations for **PKM** (ENSG00000067225) across cancer and inflammation-related disease groupings (e.g., neoplasm; hepatocellular carcinoma; neuroinflammatory disorder), supported by multiple literature evidence items. This provides a high-level, integrative pointer that PKM is repeatedly observed in disease-linked evidence streams, though it does not replace mechanistic interpretation. (OpenTargets Search: -PKM)

### 9) Limitations and evidence-quality notes

- Several “noncanonical kinase” claims in reviews synthesize heterogeneous primary literature; for functional annotation, the strongest recent direct mechanistic advance in the provided corpus is the **EMBO J 2024** demonstration of **PEP-dependent histidine kinase activity toward PGAM1** with clear oligomer-state dependence. (wang2024pkm2functionsas pages 4-6)
- Biomarker studies cited here are largely discovery-stage proteomics; they highlight PKM as differentially abundant or associated with outcomes, but **clinical diagnostic performance metrics** (AUC, sensitivity/specificity) for PKM alone are not established in the extracted text. (remori2024predictionoforal pages 6-8, yip2023newbornswithfavourable pages 11-12)

---

### Evidence map summary table

| Topic | Key points | Best recent sources (2023-2024 prioritized) |
|---|---|---|
| Identity | Human **PKM** encodes pyruvate kinase M1/2 (UniProt **P14618**), a pyruvate kinase family enzyme catalyzing the terminal glycolytic step; PKM2 is the most discussed isoform in proliferative and cancer contexts, while PKM1 is prominent in differentiated tissues. PKM contains conserved pyruvate-kinase domains and an FBP allosteric site in the C-domain. (jemal2024nonmetabolicenzymefunction pages 1-2, li2021discoveryoffunctional pages 2-3) | Jemal et al., **2024-10**, *Front Oncol* — https://doi.org/10.3389/fonc.2024.1450325 (jemal2024nonmetabolicenzymefunction pages 1-2); Li et al., **2021-01**, *Cancers* — https://doi.org/10.3390/cancers13020348 (li2021discoveryoffunctional pages 2-3) |
| Isoforms | **PKM1 vs PKM2 arise by mutually exclusive splicing of exon 9 and exon 10**: PKM1 includes **exon 9** and excludes exon 10; PKM2 includes **exon 10** and excludes exon 9. PKM1 is enriched in heart, muscle, brain, and mature sperm; PKM2 is enriched in proliferating/anabolic cells and most tumor cells. (li2024theregulatorynetwork pages 1-2, oleaflores2024musclespecificpyruvatekinase pages 1-5, li2021discoveryoffunctional pages 2-3) | Li et al., **2024-05**, *Biomolecules* — https://doi.org/10.3390/biom14050566 (li2024theregulatorynetwork pages 1-2); Olea-Flores et al., **2024-04**, *bioRxiv* — https://doi.org/10.1101/2024.04.10.588959 (oleaflores2024musclespecificpyruvatekinase pages 1-5) |
| Catalytic reaction | Canonical enzymatic function: **phosphoenolpyruvate (PEP) + ADP → pyruvate + ATP**. This is the final ATP-producing step of glycolysis and a major control point in glycolytic flux. (hu2024roleofpyruvate pages 2-4, oleaflores2024musclespecificpyruvatekinase pages 1-5, hu2024roleofpyruvate pages 1-2) | Hu et al., **2024-08**, *Mol Med Rep* — https://doi.org/10.3892/mmr.2024.13309 (hu2024roleofpyruvate pages 2-4); Olea-Flores et al., **2024-04**, *bioRxiv* — https://doi.org/10.1101/2024.04.10.588959 (oleaflores2024musclespecificpyruvatekinase pages 1-5) |
| Allostery & oligomerization | **PKM1 is constitutively active and predominantly tetrameric**; **PKM2 interconverts between high-activity tetramers and lower-activity dimers/monomers**. **FBP** stabilizes tetrameric PKM2. Amino acids can also tune PKM2 allostery: Asn/Asp favor activation, whereas Val/Cys can inhibit activity by altering substrate affinity and oligomeric state. In tumors, low-activity dimeric PKM2 is often linked to anabolic rewiring/Warburg metabolism. (li2021discoveryoffunctional pages 2-3, nandi2023identificationofresidues pages 10-12, li2024theregulatorynetwork pages 1-2, hu2024roleofpyruvate pages 2-4) | Nandi & Dey, **2023-03**, *PLOS ONE* — https://doi.org/10.1371/journal.pone.0282508 (nandi2023identificationofresidues pages 10-12); Hu et al., **2024-08**, *Mol Med Rep* — https://doi.org/10.3892/mmr.2024.13309 (hu2024roleofpyruvate pages 2-4) |
| Noncanonical kinase roles | Beyond glycolysis, PKM2 has reported **protein-kinase / histone-kinase / transcriptional coactivator** functions. A major recent advance is the **EMBO Journal 2024** report that **PKM2 acts as a PEP-dependent histidine kinase**, phosphorylating **PGAM1 H11**; **monomeric/dimeric PKM2**, but not tetrameric PKM2, efficiently catalyzed this event, and **TEPP46** reduced PKM2–PGAM1 interaction/H11 phosphorylation. PKM2 has also been linked to histone H3 phosphorylation and regulation of HIF-1α, β-catenin, STAT3, c-Myc, NF-κB, and MST1 pathways. (wang2024pkm2functionsas pages 4-6, wang2024pkm2functionsas pages 1-2, jemal2024nonmetabolicenzymefunction pages 6-8, jemal2024nonmetabolicenzymefunction pages 5-6, jemal2024nonmetabolicenzymefunction pages 10-10, oleaflores2024musclespecificpyruvatekinase pages 1-5) | Wang et al., **2024-05**, *EMBO J* — https://doi.org/10.1038/s44318-024-00110-8 (wang2024pkm2functionsas pages 4-6); Jemal et al., **2024-10**, *Front Oncol* — https://doi.org/10.3389/fonc.2024.1450325 (jemal2024nonmetabolicenzymefunction pages 6-8) |
| Subcellular localization | PKM is primarily **cytosolic** for canonical glycolysis, but **PKM2 can accumulate in the nucleus** where it supports transcriptional regulation and noncanonical signaling. Recent reviews summarize explicit nuclear-entry triggers: **ERK1/2-dependent phosphorylation at S37** promotes nuclear translocation, and **EGFR activation promotes PKM2 nuclear import via importin α5**. Nuclear localization is especially associated with **dimeric PKM2**. (hu2024roleofpyruvate pages 2-4, jemal2024nonmetabolicenzymefunction pages 6-8, jemal2024nonmetabolicenzymefunction pages 8-9, jemal2024nonmetabolicenzymefunction pages 5-6) | Hu et al., **2024-08**, *Mol Med Rep* — https://doi.org/10.3892/mmr.2024.13309 (hu2024roleofpyruvate pages 2-4); Jemal et al., **2024-10**, *Front Oncol* — https://doi.org/10.3389/fonc.2024.1450325 (jemal2024nonmetabolicenzymefunction pages 8-9) |
| Applications & biomarkers | PKM/PKM2 is being explored as a **biomarker** and **therapeutic target**, especially in oncology and inflammatory disease. In **OSCC saliva proteomics** (10 patients, 20 controls), PKM was among altered glycolytic proteins proposed for follow-up biomarker validation, though sensitivity/specificity were not yet established. In neonatal HIE plasma proteomics, **PKM (P14618-2)** was increased in favorable-outcome severe HIE versus mild HIE (**log2FC 0.95, p=3.09×10^-2**). In pregnancy saliva proteomics, pyruvate kinase was reduced/absent in stimulated saliva, supporting **unstimulated saliva** as the better discovery matrix. (remori2024predictionoforal pages 6-8, yip2023newbornswithfavourable pages 11-12, foratorijunior2023istherea pages 16-17) | Remori et al., **2024-10**, *Int J Mol Sci* — https://doi.org/10.3390/ijms252011120 (remori2024predictionoforal pages 6-8); Yip et al., **2023-09**, *Biomolecules* — https://doi.org/10.3390/biom13101471 (yip2023newbornswithfavourable pages 11-12); Foratori-Junior et al., **2023-05**, *Cells* — https://doi.org/10.3390/cells12101389 (foratorijunior2023istherea pages 16-17) |
| Recent 2023-2024 advances | Key recent advances include: (1) **amino-acid allosteric signal-transmission mapping** in PKM2 (2023); (2) updated **hnRNP/PTBP1-centered splicing-regulation networks** controlling PKM1/PKM2 balance in tumors (2024); (3) **PEP-dependent histidine kinase activity of PKM2 toward PGAM1 H11** with oligomer-state dependence (2024); and (4) disease-focused reviews highlighting strategies to **stabilize tetrameric PKM2 or block nuclear translocation**. (nandi2023identificationofresidues pages 10-12, li2024theregulatorynetwork pages 1-2, wang2024pkm2functionsas pages 4-6, hu2024roleofpyruvate pages 2-4, jemal2024nonmetabolicenzymefunction pages 6-8) | Nandi & Dey, **2023-03**, *PLOS ONE* — https://doi.org/10.1371/journal.pone.0282508 (nandi2023identificationofresidues pages 10-12); Li et al., **2024-05**, *Biomolecules* — https://doi.org/10.3390/biom14050566 (li2024theregulatorynetwork pages 1-2); Wang et al., **2024-05**, *EMBO J* — https://doi.org/10.1038/s44318-024-00110-8 (wang2024pkm2functionsas pages 4-6); Hu et al., **2024-08**, *Mol Med Rep* — https://doi.org/10.3892/mmr.2024.13309 (hu2024roleofpyruvate pages 2-4) |


*Table: This table summarizes the verified identity, core biochemistry, regulation, localization, and recent 2023-2024 advances for human PKM/PKM2 (UniProt P14618). It is useful as a compact evidence map for distinguishing canonical glycolytic roles from newer noncanonical signaling and biomarker findings.*


References

1. (nandi2023identificationofresidues pages 10-12): Suparno Nandi and Mishtu Dey. Identification of residues involved in allosteric signal transmission from amino acid binding site of pyruvate kinase muscle isoform 2. PLOS ONE, 18:e0282508, Mar 2023. URL: https://doi.org/10.1371/journal.pone.0282508, doi:10.1371/journal.pone.0282508. This article has 3 citations and is from a peer-reviewed journal.

2. (li2024theregulatorynetwork pages 1-2): Yuchao Li, Shuwei Zhang, Yuexian Li, Junchao Liu, Qian Li, Wenli Zang, and Yaping Pan. The regulatory network of hnrnps underlying regulating pkm alternative splicing in tumor progression. Biomolecules, 14:566, May 2024. URL: https://doi.org/10.3390/biom14050566, doi:10.3390/biom14050566. This article has 11 citations.

3. (jemal2024nonmetabolicenzymefunction pages 1-2): Mohammed Jemal, Mamaru Getinet, Gashaw Azanaw Amare, Bantayehu Addis Tegegne, Temesgen Baylie, Enyew Fenta Mengistu, Enatnesh Essa Osman, Nuredin Chura Waritu, and Adane Adugna. Non-metabolic enzyme function of pyruvate kinase m2 in breast cancer. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1450325, doi:10.3389/fonc.2024.1450325. This article has 7 citations.

4. (oleaflores2024musclespecificpyruvatekinase pages 1-5): Monserrat Olea-Flores, Tapan Sharma, Odette Verdejo-Torres, Imaru DiBartolomeo, Paul R. Thompson, Teresita Padilla-Benavides, and Anthony N. Imbalzano. Muscle-specific pyruvate kinase isoforms, pkm1 and pkm2, regulate mammalian swi/snf proteins and histone 3 phosphorylation during myoblast differentiation. BioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.10.588959, doi:10.1101/2024.04.10.588959. This article has 12 citations.

5. (hu2024roleofpyruvate pages 2-4): Yifei Hu, Jing Tang, Qiao Xu, Zenghui Fang, Rongqing Li, Mengxuan Yang, Jie Zhao, and Xin Chen. Role of pyruvate kinase m2 in regulating sepsis (review). Molecular Medicine Reports, Aug 2024. URL: https://doi.org/10.3892/mmr.2024.13309, doi:10.3892/mmr.2024.13309. This article has 5 citations and is from a peer-reviewed journal.

6. (wang2024pkm2functionsas pages 4-6): Yang Wang, Hengyao Shu, Yanzhao Qu, Xin Jin, Jia Liu, Wanting Peng, Lihua Wang, Miao Hao, Mingjie Xia, Zhexuan Zhao, Kejian Dong, Yao Di, Miaomiao Tian, Fengqi Hao, Chaoyi Xia, Wenxia Zhang, Xueqing Ba, Yunpeng Feng, and Min Wei. Pkm2 functions as a histidine kinase to phosphorylate pgam1 and increase glycolysis shunts in cancer. The EMBO Journal, 43:2368-2396, May 2024. URL: https://doi.org/10.1038/s44318-024-00110-8, doi:10.1038/s44318-024-00110-8. This article has 31 citations.

7. (jemal2024nonmetabolicenzymefunction pages 6-8): Mohammed Jemal, Mamaru Getinet, Gashaw Azanaw Amare, Bantayehu Addis Tegegne, Temesgen Baylie, Enyew Fenta Mengistu, Enatnesh Essa Osman, Nuredin Chura Waritu, and Adane Adugna. Non-metabolic enzyme function of pyruvate kinase m2 in breast cancer. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1450325, doi:10.3389/fonc.2024.1450325. This article has 7 citations.

8. (li2021discoveryoffunctional pages 2-3): Xiangyu Li, Woonghee Kim, Muhammad Arif, Chunxia Gao, Andreas Hober, David Kotol, Linnéa Strandberg, Björn Forsström, Åsa Sivertsson, Per Oksvold, Hasan Turkez, Morten Grøtli, Yusuke Sato, Haruki Kume, Seishi Ogawa, Jan Boren, Jens Nielsen, Mathias Uhlen, Cheng Zhang, and Adil Mardinoglu. Discovery of functional alternatively spliced pkm transcripts in human cancers. Cancers, 13:348, Jan 2021. URL: https://doi.org/10.3390/cancers13020348, doi:10.3390/cancers13020348. This article has 19 citations.

9. (li2024theregulatorynetwork pages 7-8): Yuchao Li, Shuwei Zhang, Yuexian Li, Junchao Liu, Qian Li, Wenli Zang, and Yaping Pan. The regulatory network of hnrnps underlying regulating pkm alternative splicing in tumor progression. Biomolecules, 14:566, May 2024. URL: https://doi.org/10.3390/biom14050566, doi:10.3390/biom14050566. This article has 11 citations.

10. (jemal2024nonmetabolicenzymefunction pages 8-9): Mohammed Jemal, Mamaru Getinet, Gashaw Azanaw Amare, Bantayehu Addis Tegegne, Temesgen Baylie, Enyew Fenta Mengistu, Enatnesh Essa Osman, Nuredin Chura Waritu, and Adane Adugna. Non-metabolic enzyme function of pyruvate kinase m2 in breast cancer. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1450325, doi:10.3389/fonc.2024.1450325. This article has 7 citations.

11. (wang2024pkm2functionsas pages 1-2): Yang Wang, Hengyao Shu, Yanzhao Qu, Xin Jin, Jia Liu, Wanting Peng, Lihua Wang, Miao Hao, Mingjie Xia, Zhexuan Zhao, Kejian Dong, Yao Di, Miaomiao Tian, Fengqi Hao, Chaoyi Xia, Wenxia Zhang, Xueqing Ba, Yunpeng Feng, and Min Wei. Pkm2 functions as a histidine kinase to phosphorylate pgam1 and increase glycolysis shunts in cancer. The EMBO Journal, 43:2368-2396, May 2024. URL: https://doi.org/10.1038/s44318-024-00110-8, doi:10.1038/s44318-024-00110-8. This article has 31 citations.

12. (remori2024predictionoforal pages 6-8): Veronica Remori, Manuel Airoldi, Tiziana Alberio, Mauro Fasano, and Lorenzo Azzi. Prediction of oral cancer biomarkers by salivary proteomics data. International Journal of Molecular Sciences, 25:11120, Oct 2024. URL: https://doi.org/10.3390/ijms252011120, doi:10.3390/ijms252011120. This article has 9 citations.

13. (yip2023newbornswithfavourable pages 11-12): Ping K. Yip, Michael Bremang, Ian Pike, Vennila Ponnusamy, Adina T. Michael-Titus, and Divyen K. Shah. Newborns with favourable outcomes after perinatal asphyxia have upregulated glucose metabolism-related proteins in plasma. Biomolecules, 13:1471, Sep 2023. URL: https://doi.org/10.3390/biom13101471, doi:10.3390/biom13101471. This article has 4 citations.

14. (foratorijunior2023istherea pages 16-17): Gerson Aparecido Foratori-Junior, Talita Mendes Oliveira Ventura, Larissa Tercilia Grizzo, Bruno Gualtieri Jesuino, Ana Virgínia Santana Sampaio Castilho, Marília Afonso Rabelo Buzalaf, and Silvia Helena de Carvalho Sales-Peres. Is there a difference in the proteomic profile of stimulated and unstimulated saliva samples from pregnant women with/without obesity and periodontitis? Cells, 12:1389, May 2023. URL: https://doi.org/10.3390/cells12101389, doi:10.3390/cells12101389. This article has 15 citations.

15. (przewocki2024follicularfluidproteomic pages 7-8): Janusz Przewocki, Dominik Kossiński, Adam Łukaszuk, Grzegorz Jakiel, Izabela Wocławek-Potocka, Stanisław Ołdziej, and Krzysztof Łukaszuk. Follicular fluid proteomic analysis to identify predictive markers of normal embryonic development. International Journal of Molecular Sciences, 25:8431, Aug 2024. URL: https://doi.org/10.3390/ijms25158431, doi:10.3390/ijms25158431. This article has 8 citations.

16. (OpenTargets Search: -PKM): Open Targets Query (-PKM, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

17. (hu2024roleofpyruvate pages 1-2): Yifei Hu, Jing Tang, Qiao Xu, Zenghui Fang, Rongqing Li, Mengxuan Yang, Jie Zhao, and Xin Chen. Role of pyruvate kinase m2 in regulating sepsis (review). Molecular Medicine Reports, Aug 2024. URL: https://doi.org/10.3892/mmr.2024.13309, doi:10.3892/mmr.2024.13309. This article has 5 citations and is from a peer-reviewed journal.

18. (jemal2024nonmetabolicenzymefunction pages 5-6): Mohammed Jemal, Mamaru Getinet, Gashaw Azanaw Amare, Bantayehu Addis Tegegne, Temesgen Baylie, Enyew Fenta Mengistu, Enatnesh Essa Osman, Nuredin Chura Waritu, and Adane Adugna. Non-metabolic enzyme function of pyruvate kinase m2 in breast cancer. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1450325, doi:10.3389/fonc.2024.1450325. This article has 7 citations.

19. (jemal2024nonmetabolicenzymefunction pages 10-10): Mohammed Jemal, Mamaru Getinet, Gashaw Azanaw Amare, Bantayehu Addis Tegegne, Temesgen Baylie, Enyew Fenta Mengistu, Enatnesh Essa Osman, Nuredin Chura Waritu, and Adane Adugna. Non-metabolic enzyme function of pyruvate kinase m2 in breast cancer. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1450325, doi:10.3389/fonc.2024.1450325. This article has 7 citations.

## Citations

1. li2024theregulatorynetwork pages 1-2
2. li2021discoveryoffunctional pages 2-3
3. nandi2023identificationofresidues pages 10-12
4. hu2024roleofpyruvate pages 2-4
5. jemal2024nonmetabolicenzymefunction pages 8-9
6. jemal2024nonmetabolicenzymefunction pages 6-8
7. oleaflores2024musclespecificpyruvatekinase pages 1-5
8. remori2024predictionoforal pages 6-8
9. yip2023newbornswithfavourable pages 11-12
10. foratorijunior2023istherea pages 16-17
11. przewocki2024follicularfluidproteomic pages 7-8
12. jemal2024nonmetabolicenzymefunction pages 1-2
13. li2024theregulatorynetwork pages 7-8
14. hu2024roleofpyruvate pages 1-2
15. jemal2024nonmetabolicenzymefunction pages 5-6
16. jemal2024nonmetabolicenzymefunction pages 10-10
17. https://doi.org/10.3390/ijms252011120
18. https://doi.org/10.3390/biom13101471
19. https://doi.org/10.3390/cells12101389
20. https://doi.org/10.3390/ijms25158431
21. https://doi.org/10.3389/fonc.2024.1450325
22. https://doi.org/10.3390/cancers13020348
23. https://doi.org/10.3390/biom14050566
24. https://doi.org/10.1101/2024.04.10.588959
25. https://doi.org/10.3892/mmr.2024.13309
26. https://doi.org/10.1371/journal.pone.0282508
27. https://doi.org/10.1038/s44318-024-00110-8
28. https://doi.org/10.1371/journal.pone.0282508,
29. https://doi.org/10.3390/biom14050566,
30. https://doi.org/10.3389/fonc.2024.1450325,
31. https://doi.org/10.1101/2024.04.10.588959,
32. https://doi.org/10.3892/mmr.2024.13309,
33. https://doi.org/10.1038/s44318-024-00110-8,
34. https://doi.org/10.3390/cancers13020348,
35. https://doi.org/10.3390/ijms252011120,
36. https://doi.org/10.3390/biom13101471,
37. https://doi.org/10.3390/cells12101389,
38. https://doi.org/10.3390/ijms25158431,