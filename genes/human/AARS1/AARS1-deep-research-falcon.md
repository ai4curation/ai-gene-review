---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T15:05:38.733044'
end_time: '2026-09-25T15:15:53.382343'
duration_seconds: 614.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AARS1
  gene_symbol: AARS1
  uniprot_accession: P49588
  protein_description: 'RecName: Full=Alanine--tRNA ligase, cytoplasmic {ECO:0000255|HAMAP-Rule:MF_03133};
    EC=6.1.1.7 {ECO:0000255|HAMAP-Rule:MF_03133, ECO:0000269|PubMed:25817015, ECO:0000269|PubMed:27622773,
    ECO:0000269|PubMed:27911835, ECO:0000269|PubMed:28493438}; AltName: Full=Alanyl-tRNA
    synthetase {ECO:0000255|HAMAP-Rule:MF_03133}; Short=AlaRS {ECO:0000255|HAMAP-Rule:MF_03133};
    AltName: Full=Protein lactyltransferase AARS1 {ECO:0000305}; EC=6.-.-.- {ECO:0000269|PubMed:38512451,
    ECO:0000269|PubMed:38653238, ECO:0000269|PubMed:39322678}; AltName: Full=Renal
    carcinoma antigen NY-REN-42;'
  gene_info: Name=AARS1 {ECO:0000303|PubMed:38653238, ECO:0000312|HGNC:HGNC:20}; Synonyms=AARS
    {ECO:0000255|HAMAP-Rule:MF_03133};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the class-II aminoacyl-tRNA synthetase family.
  protein_domains: aa-tRNA-synth_II/BPL/LPL. (IPR045864); Ala-tRNA-lgiase_IIc. (IPR002318);
    Ala-tRNA-ligase_IIc_anticod-bd. (IPR018162); Ala-tRNA-synth_IIc_core. (IPR018165);
    Ala-tRNA-synth_IIc_N. (IPR018164)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: AARS1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P49588
- **Protein Description:** RecName: Full=Alanine--tRNA ligase, cytoplasmic {ECO:0000255|HAMAP-Rule:MF_03133}; EC=6.1.1.7 {ECO:0000255|HAMAP-Rule:MF_03133, ECO:0000269|PubMed:25817015, ECO:0000269|PubMed:27622773, ECO:0000269|PubMed:27911835, ECO:0000269|PubMed:28493438}; AltName: Full=Alanyl-tRNA synthetase {ECO:0000255|HAMAP-Rule:MF_03133}; Short=AlaRS {ECO:0000255|HAMAP-Rule:MF_03133}; AltName: Full=Protein lactyltransferase AARS1 {ECO:0000305}; EC=6.-.-.- {ECO:0000269|PubMed:38512451, ECO:0000269|PubMed:38653238, ECO:0000269|PubMed:39322678}; AltName: Full=Renal carcinoma antigen NY-REN-42;
- **Gene Information:** Name=AARS1 {ECO:0000303|PubMed:38653238, ECO:0000312|HGNC:HGNC:20}; Synonyms=AARS {ECO:0000255|HAMAP-Rule:MF_03133};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the class-II aminoacyl-tRNA synthetase family.
- **Key Domains:** aa-tRNA-synth_II/BPL/LPL. (IPR045864); Ala-tRNA-lgiase_IIc. (IPR002318); Ala-tRNA-ligase_IIc_anticod-bd. (IPR018162); Ala-tRNA-synth_IIc_core. (IPR018165); Ala-tRNA-synth_IIc_N. (IPR018164)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AARS1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AARS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AARS1** (gene ID: AARS1, UniProt: P49588) in human.

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
- **UniProt Accession:** P49588
- **Protein Description:** RecName: Full=Alanine--tRNA ligase, cytoplasmic {ECO:0000255|HAMAP-Rule:MF_03133}; EC=6.1.1.7 {ECO:0000255|HAMAP-Rule:MF_03133, ECO:0000269|PubMed:25817015, ECO:0000269|PubMed:27622773, ECO:0000269|PubMed:27911835, ECO:0000269|PubMed:28493438}; AltName: Full=Alanyl-tRNA synthetase {ECO:0000255|HAMAP-Rule:MF_03133}; Short=AlaRS {ECO:0000255|HAMAP-Rule:MF_03133}; AltName: Full=Protein lactyltransferase AARS1 {ECO:0000305}; EC=6.-.-.- {ECO:0000269|PubMed:38512451, ECO:0000269|PubMed:38653238, ECO:0000269|PubMed:39322678}; AltName: Full=Renal carcinoma antigen NY-REN-42;
- **Gene Information:** Name=AARS1 {ECO:0000303|PubMed:38653238, ECO:0000312|HGNC:HGNC:20}; Synonyms=AARS {ECO:0000255|HAMAP-Rule:MF_03133};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the class-II aminoacyl-tRNA synthetase family.
- **Key Domains:** aa-tRNA-synth_II/BPL/LPL. (IPR045864); Ala-tRNA-lgiase_IIc. (IPR002318); Ala-tRNA-ligase_IIc_anticod-bd. (IPR018162); Ala-tRNA-synth_IIc_core. (IPR018165); Ala-tRNA-synth_IIc_N. (IPR018164)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AARS1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AARS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AARS1** (gene ID: AARS1, UniProt: P49588) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human AARS1 (UniProt P49588): Functional-Annotation Research Report

## Executive summary

**Identity is verified.** The requested protein is human **AARS1** (formerly *AARS*), UniProt **P49588**, the predominantly cytoplasmic alanyl-tRNA synthetase (AlaRS), not mitochondrial AARS2. The literature places AARS1 on chromosome 16 and classifies it as a class-II alanyl-tRNA synthetase with aminoacylation/tRNA-binding, editing, and C-terminal C-Ala/anticodon-binding regions, matching the family and InterPro domains supplied in the question. AARS2 is a separate, mitochondrially localized paralog; AARS2 findings were not treated as AARS1 findings. (mahmood2025yeastmodelsfor pages 4-6, gao2025aars1andaars2 pages 4-6, mahmood2025yeastmodelsfor pages 2-4)

AARS1’s established primary function is to generate cytoplasmic Ala-tRNA^Ala for ribosomal protein synthesis. It activates L-alanine with ATP and transfers alanine to the 3′ end of cognate tRNA^Ala. Specificity depends strongly on the G3:U70 wobble pair in the tRNA acceptor stem. Because AlaRS can also activate the chemically similar amino acids serine and glycine, its editing domain hydrolyzes mischarged Ser-tRNA^Ala and Gly-tRNA^Ala, protecting translational fidelity. (mahmood2025yeastmodelsfor pages 4-6, mahmood2025yeastmodelsfor pages 2-4)

Three major 2024 studies substantially expanded this annotation. They reported that AARS1 can sense L-lactate and use lactate plus ATP to catalyze protein lysine lactylation, including p53 and the nuclear YAP–TEAD complex. These findings connect high glycolytic lactate to tumor signaling, but remain newer and less broadly established than aminoacylation. A related Nature study identified both AARS1 and AARS2 as lactate sensors/global lactyltransferases; importantly, its direct cGAS-lactylation mechanism was demonstrated principally for **AARS2**, so cGAS inactivation should not presently be annotated as an AARS1-specific function. (zhou2026theroleof pages 12-14, gao2025aars1andaars2 pages 8-10, gao2025aars1andaars2 pages 6-8, gao2025aars1andaars2 pages 4-6)

| Annotation dimension | Best-supported conclusion | Key experimental evidence/model | Confidence / caveat |
|---|---|---|---|
| Identity versus AARS2 | **AARS1/P49588** is human cytoplasmic alanyl-tRNA synthetase; **AARS2** is the distinct mitochondrial paralog. | Human genetics, biochemical annotation, and compartment-specific studies consistently distinguish cytosolic AARS1 from mitochondrial AARS2. (gao2025aars1andaars2 pages 4-6, mahmood2025yeastmodelsfor pages 2-4) | **High.** Findings assigned to AARS2—especially mitochondrial effects—must not be transferred to AARS1. |
| Canonical aminoacylation | AARS1 catalyzes ATP-dependent charging of cytoplasmic tRNA^Ala: alanine + ATP → alanyl-AMP + PPi; alanyl-AMP + tRNA^Ala → Ala-tRNA^Ala + AMP. | Conserved AlaRS biochemistry and humanized-yeast complementation establish that AARS1 supplies Ala-tRNA^Ala for cytoplasmic translation. (mahmood2025yeastmodelsfor pages 2-4, kuo2025recessivepathogenicaars1 pages 1-3) | **High.** This is the primary, essential function. |
| tRNA^Ala specificity | The principal tRNA identity determinant is the conserved **G3:U70 wobble pair** in the acceptor stem, recognized during aminoacylation and proofreading. | Comparative structural and biochemical studies and humanized-yeast literature support conservation in human AARS1. (mahmood2025yeastmodelsfor pages 4-6) | **High**, although much residue-level evidence derives from conserved nonhuman AlaRS orthologs. |
| Ser/Gly proofreading | Because alanine is difficult to discriminate from serine and glycine, AARS1 can mischarge these amino acids and uses a **cis-editing domain** to hydrolyze Ser-tRNA^Ala and Gly-tRNA^Ala; AlaX proteins provide additional trans-editing. | Biochemical editing studies and evolutionary conservation; editing defects cause mistranslation, proteotoxic stress, and neurological phenotypes in models. (mahmood2025yeastmodelsfor pages 4-6, zhou2026theroleof pages 14-14) | **High** for conserved proofreading; quantitative human-cell kinetics are less extensive. |
| Domains and oligomeric architecture | Architecture comprises an N-terminal class-II aminoacylation/tRNA-binding region, central editing domain, and C-terminal **C-Ala/anticodon-binding** region. Human AARS1 can function predominantly as a **monomer**. | Domain mapping, conserved AlaRS structures, and functional complementation studies. (mahmood2025yeastmodelsfor pages 4-6, mahmood2025yeastmodelsfor pages 2-4) | **High** for domain organization; **moderate–high** for physiological monomer predominance because oligomerization may depend on conditions. |
| Cytoplasmic/nuclear localization | AARS1 is predominantly cytoplasmic but contains a C-terminal nuclear-localization signal. High lactate enhances KPNA4 association and nuclear import, enabling nuclear protein lactylation. | Cell fractionation/imaging and NLS-deletion experiments; 25 mM lactate induced nuclear translocation and global lactylation in reported in-vitro systems. (gao2025aars1andaars2 pages 4-6) | **High** for cytoplasmic localization; **moderate–high** for lactate-regulated nuclear trafficking, which may be context-dependent. |
| 2024 p53 lactylation | AARS1 was reported to sense L-lactate and ATP-dependently lactylate p53 at **K120 and K139**, reducing DNA binding, phase separation, and transcription of *PUMA* and *CDKN1A/p21*. | CRISPR screening, purified-enzyme assays, cancer cells, and animal tumor models; β-alanine antagonized lactate binding and reduced tumorigenesis. (zhou2026theroleof pages 12-14, gao2025aars1andaars2 pages 8-10) | **Emerging but strong primary evidence.** Oncogenic consequences principally apply to tumors retaining wild-type p53. |
| 2024 YAP/TEAD lactylation | Nuclear AARS1 uses lactate and ATP to lactylate and activate YAP–TEAD—reported sites include **YAP K90** and **TEAD1 K108**—forming a positive-feedback loop in gastric cancer. | Purified-protein assays, gastric-cancer cells, NLS-deletion rescue, tumor models, and patient-expression/prognosis analyses. (zhou2026theroleof pages 14-14, gao2025aars1andaars2 pages 8-10, gao2025aars1andaars2 pages 6-8) | **Emerging but strong.** Clinical association does not yet demonstrate benefit from AARS1-directed therapy. |
| 2024 cGAS finding | Both AARS1 and AARS2 were identified as L-lactate sensors/global lactyltransferases, but the demonstrated direct cGAS effector was **mainly AARS2**, which associated with, lactylated, and inactivated cGAS. | Lactate-binding and ATP-dependent lactylation assays, engineered lactyl-lysine incorporation, cultured cells, and knock-in mice. (zhou2026theroleof pages 12-14, gao2025aars1andaars2 pages 6-8, gao2025aars1andaars2 pages 4-6) | **High** for AARS1/2 lactate sensing and AARS2–cGAS action; insufficient to call this a direct AARS1-specific cGAS mechanism. |
| Genetic disease and clinical relevance | Monoallelic AARS1 variants cause dominant axonal neuropathy/CMT2N and can produce adult-onset white-matter disease; biallelic variants cause severe neurodevelopmental or multisystem disease through hypomorphic/loss-of-function alleles, sometimes with dominant-negative behavior. | Patient studies and humanized yeast: among 16 recessive missense variants tested, most showed variable loss of function; K81T and E99G also showed dominant-negative effects. (fu2026comprehensivepancanceranalysis pages 23-23, kuo2025recessivepathogenicaars1 pages 1-3) | **High** for gene–disease association. Mechanisms are allele-specific; impaired charging/editing does not explain every dominant neuropathy. |


*Table: Compact synthesis of established and emerging functional annotations for human AARS1 (UniProt P49588), with explicit separation from mitochondrial AARS2. Confidence notes distinguish canonical translation biology from newer lactyltransferase and disease-mechanism findings.*

## 1. Target verification and nomenclature

The symbol **AARS1** correctly corresponds to cytoplasmic alanine—tRNA ligase in *Homo sapiens*. Human nomenclature generally uses the “1” suffix for the cytoplasmic enzyme and “2” for the distinct mitochondrial enzyme. AARS1 is therefore the appropriate gene for UniProt P49588 and for the canonical cytoplasmic Ala-tRNA^Ala reaction; mitochondrial translation is served by AARS2. (gao2025aars1andaars2 pages 4-6, mahmood2025yeastmodelsfor pages 2-4)

The reported architecture comprises an N-terminal class-II aminoacylation region containing catalytic and tRNA-binding functions, an editing/proofreading domain, and a C-terminal C-Ala region involved in tRNA recognition and other regulatory functions. This agrees with the supplied aa-tRNA-synth_II, AlaRS-IIc core/N-terminal, editing-associated, and anticodon-binding annotations. Human AlaRS is reported to operate predominantly as a monomer, unlike the obligatory dimers characteristic of many class-II synthetases. (mahmood2025yeastmodelsfor pages 4-6, mahmood2025yeastmodelsfor pages 2-4)

## 2. Canonical biochemical function

### 2.1 Reaction and biological role

AARS1 supplies the cytoplasmic ribosome with alanine-charged tRNA through two coupled reactions:

1. **L-alanine + ATP → alanyl-AMP + PPi**
2. **Alanyl-AMP + tRNA^Ala → L-alanyl-tRNA^Ala + AMP**

The amino acid is esterified to the terminal adenosine of tRNA^Ala. The net reaction is therefore:

**L-alanine + ATP + tRNA^Ala → L-alanyl-tRNA^Ala + AMP + PPi.**

This is AARS1’s essential and best-established cellular function. Ala-tRNA^Ala enters the elongating ribosome and decodes alanine codons during cytoplasmic protein synthesis. Functional complementation data and the disease consequences of hypomorphic alleles support the indispensability of this reaction. (mahmood2025yeastmodelsfor pages 2-4, kuo2025recessivepathogenicaars1 pages 1-3)

### 2.2 Substrate specificity and tRNA recognition

AlaRS is unusual because the principal identity element for cognate tRNA is not primarily the anticodon but the **G3:U70 wobble base pair** in the acceptor stem. This element is recognized during both aminoacylation and proofreading. Consequently, tRNAs bearing an Ala-like acceptor-stem identity can become substrates even when their anticodons do not encode alanine; this explains why acceptor-stem discrimination and editing are central to AlaRS fidelity. (mahmood2025yeastmodelsfor pages 4-6)

The amino-acid substrate is physiologically L-alanine. However, alanine’s small side chain creates a difficult chemical-recognition problem: serine and glycine can enter the synthetic site and be transferred incorrectly to tRNA^Ala. AARS1 therefore achieves overall specificity through **selection plus proofreading**, rather than perfect exclusion at the synthetic site. (mahmood2025yeastmodelsfor pages 4-6)

### 2.3 Editing and translational quality control

The cis-editing domain hydrolyzes mischarged Ser-tRNA^Ala and Gly-tRNA^Ala before these species reach the ribosome. Free-standing AlaX-family trans-editing proteins provide an additional layer of protection. Editing failure permits serine-for-alanine or glycine-for-alanine substitution, producing proteome-wide mistranslation, misfolding, stress responses, and—in experimental systems—neurological degeneration. (mahmood2025yeastmodelsfor pages 4-6, zhou2026theroleof pages 14-14)

This distinction is important for functional annotation: AARS1 is both a **synthetase** and a **proofreading enzyme**. Aminoacylation generates the cognate translation substrate, whereas editing removes closely related, noncognate amino acids from tRNA^Ala.

## 3. Cellular localization and pathway context

### 3.1 Basal localization

AARS1 acts principally in the **cytoplasm**, where cytoplasmic tRNAs are charged for translation. This differentiates it from AARS2, which is targeted to mitochondria. AARS1 is broadly required because cytoplasmic translation occurs in essentially all nucleated cell types. (gao2025aars1andaars2 pages 4-6, mahmood2025yeastmodelsfor pages 2-4, kuo2025recessivepathogenicaars1 pages 1-3)

### 3.2 Regulated nuclear localization

AARS1 also contains a reported C-terminal nuclear-localization signal. Under high-lactate conditions, interaction with importin KPNA4 increases and AARS1 can accumulate in the nucleus. NLS-deletion experiments indicate that nuclear entry is required for the reported YAP–TEAD lactylation program. In reviewed experiments, 25 mM lactate promoted AARS1 nuclear translocation and global lactylation; reported physiological lactate spans approximately 0.5–20 mM, whereas some tumors may approach 40 mM. These concentrations emphasize that the nuclear function is most plausible in highly glycolytic or stressed settings rather than as AARS1’s universal basal role. (gao2025aars1andaars2 pages 4-6, gao2025aars1andaars2 pages 6-8)

### 3.3 Principal biochemical pathways

The strongest pathway annotation is:

**Alanine activation → tRNA^Ala aminoacylation → cytoplasmic translation**, coupled to **post-transfer editing → translational fidelity/proteostasis**.

When charging or editing is compromised, downstream responses can include reduced protein synthesis, mistranslation, unfolded-protein or integrated-stress responses, and tissue-selective neuronal or hepatic pathology. These are downstream consequences, not substitutes for the primary molecular function. (mahmood2025yeastmodelsfor pages 4-6, zhou2026theroleof pages 12-14, kuo2025recessivepathogenicaars1 pages 1-3)

## 4. Major 2024 development: AARS1 as a lactate sensor and protein lactyltransferase

### 4.1 Proposed reaction chemistry

Recent studies propose that AARS1 repurposes its adenylate-forming chemistry:

1. **L-lactate + ATP → lactyl-AMP + PPi**
2. **Lactyl-AMP + protein-Lys → protein-Lys-lactyl + AMP**

Thus, the acceptor changes from tRNA to a protein lysine side chain, while ATP-dependent carboxylate activation is retained. Reported AARS1 lactate-binding residues include M46, R77, N216, D239, and G241. These assignments and the wider substrate range are recent; independent structural and kinetic replication will be important for defining physiological specificity. (gao2025aars1andaars2 pages 4-6)

### 4.2 p53 lactylation

Zong and colleagues reported that AARS1 lactylates wild-type p53 at **K120 and K139**. The modification reduced p53 DNA binding and liquid–liquid phase separation and weakened transcription of *PUMA* and *CDKN1A/p21*, thereby suppressing apoptosis and cell-cycle arrest. β-Alanine competed with lactate binding, reduced p53 lactylation, and limited tumorigenesis in preclinical models. The interpretation is consequently restricted to tumors retaining functional wild-type p53; it may not apply to p53-null or many p53-mutant cancers. (gao2025aars1andaars2 pages 8-10, zhou2026theroleof pages 12-14)

Primary source: Zong et al., **Cell**, May 2024, “Alanyl-tRNA synthetase, AARS1, is a lactate sensor and lactyltransferase that lactylates p53 and contributes to tumorigenesis,” DOI: [10.1016/j.cell.2024.04.002](https://doi.org/10.1016/j.cell.2024.04.002). (zhou2026theroleof pages 12-14)

### 4.3 YAP–TEAD/Hippo signaling in gastric cancer

Ju and colleagues reported that lactate promotes AARS1 nuclear entry, after which AARS1 lactylates the YAP–TEAD transcriptional complex—reported sites include **YAP K90** and **TEAD1 K108**. Lactylation increased YAP–TEAD activity and proliferative gene expression. Because AARS1 itself was identified as a YAP–TEAD target, the authors proposed a positive-feedback loop: glycolytic lactate activates nuclear AARS1, AARS1 activates YAP–TEAD, and YAP–TEAD increases AARS1 expression. AARS1 was elevated in gastric cancer and associated with adverse prognosis, while an NLS-deficient AARS1 failed to restore the growth phenotype after AARS1 loss. (gao2025aars1andaars2 pages 8-10, gao2025aars1andaars2 pages 6-8, zhou2026theroleof pages 14-14)

Primary source: Ju et al., **Journal of Clinical Investigation**, March 2024, “The alanyl-tRNA synthetase AARS1 moonlights as a lactyltransferase to promote YAP signaling in gastric cancer,” DOI: [10.1172/JCI174587](https://doi.org/10.1172/JCI174587). (zhou2026theroleof pages 14-14)

### 4.4 AARS1/AARS2 and cGAS: required attribution caution

Li and colleagues identified AARS1 and AARS2 as conserved intracellular L-lactate sensors that bind lactate with micromolar affinity and stimulate global lysine lactylation. However, their detailed cGAS mechanism involved **AARS2**: lactate promoted AARS2–cGAS association, cGAS lactylation impaired condensate formation and DNA sensing, and lactyl-resistant genetic models protected innate immune surveillance. MCT1 blockade reduced cGAS lactylation in stressed mice and restored antiviral surveillance. This is strong evidence for the broader AARS1/2 lactate-sensing concept, but not sufficient to assign direct cGAS regulation specifically to P49588/AARS1. (zhou2026theroleof pages 12-14, gao2025aars1andaars2 pages 6-8, gao2025aars1andaars2 pages 4-6)

Primary source: Li et al., **Nature**, September 2024, 634:1229–1237, DOI: [10.1038/s41586-024-07992-y](https://doi.org/10.1038/s41586-024-07992-y). (zhou2026theroleof pages 12-14, fu2026comprehensivepancanceranalysis pages 23-23)

## 5. Human disease as functional evidence

### 5.1 Dominant neuropathy

Monoallelic AARS1 variants cause dominant axonal neuropathy, commonly designated Charcot–Marie–Tooth disease type 2N. Mechanisms are allele-dependent. Some variants reduce charging or destabilize the enzyme, but canonical loss of activity alone does not explain every dominant neuropathy. For aminoacylation-domain variants, structural loosening can create a neomorphic interaction with neuropilin-1, offering a gain-of-toxic-interaction mechanism. Accordingly, variant interpretation should assay aminoacylation, editing, stability, oligomerization, and abnormal protein interactions rather than presume a single mechanism. (mahmood2025yeastmodelsfor pages 4-6, zhou2026theroleof pages 12-14)

### 5.2 Recessive developmental and multisystem disease

Biallelic pathogenic variants are associated with severe neurodevelopmental disease, hypomyelination or white-matter abnormalities, progressive microcephaly, epileptic encephalopathy, tetraparesis, recurrent acute liver failure, and trichothiodystrophy-like presentations. These phenotypes generally fit partial loss of essential cytoplasmic charging or editing, often through combinations of nonfunctional and hypomorphic alleles; complete absence of an essential cytoplasmic synthetase is expected to be incompatible with viability. (zhou2026theroleof pages 12-14, kuo2025recessivepathogenicaars1 pages 1-3, zhou2026theroleof pages 14-14)

A recent systematic humanized-yeast study tested **16 recessive-disease missense variants**. Most produced variable loss of function, ranging from absent to markedly reduced growth. Among three severely nonfunctional variants tested for interference with wild-type protein, **K81T and E99G** showed both loss-of-function and dominant-negative behavior. The authors cautioned that yeast assays can yield false negatives and do not reliably predict genotype–phenotype severity. (kuo2025recessivepathogenicaars1 pages 1-3)

### 5.3 White-matter disease

AARS1 variants have also been implicated in adult-onset or expanded white-matter disease phenotypes. This association must be distinguished carefully from recessive **AARS2** leukodystrophy and from CSF1R-related adult-onset leukoencephalopathy. Relevant primary sources include Helman et al., **Genetics in Medicine**, December 2021, DOI: [10.1038/s41436-021-01286-8](https://doi.org/10.1038/s41436-021-01286-8), and subsequent AARS1 case literature. (fu2026comprehensivepancanceranalysis pages 23-23, zhou2026theroleof pages 14-14)

## 6. Current applications and translational status

### Molecular diagnosis

The strongest real-world application is genetic diagnosis. AARS1 belongs on panels for dominant axonal neuropathy/CMT, unexplained early-onset neurodevelopmental and hypomyelinating disease, recurrent acute liver failure with neurological involvement, and selected adult white-matter disorders. Functional assays—aminoacylation, editing, protein abundance/stability, humanized-yeast complementation, and dominant-negative testing—can support variant classification, but no single assay captures every disease mechanism. (fu2026comprehensivepancanceranalysis pages 23-23, kuo2025recessivepathogenicaars1 pages 1-3)

### Cancer biomarkers and therapeutics

AARS1 abundance and substrate lactylation are investigational biomarkers in gastric, duodenal, lung, and other cancers. Elevated AARS1 has been associated with tumor size, lymph-node involvement, stage, or adverse outcome in reported cohorts; however, these are primarily observational associations and should not yet guide routine oncology care. (gao2025aars1andaars2 pages 4-6, gao2025aars1andaars2 pages 6-8)

Proposed interventions include inhibiting AARS1’s lactate-binding/lactyltransferase activity, blocking its nuclear import, lowering intracellular lactate, inhibiting lactate transport, or reversing substrate lactylation. β-Alanine reduced the AARS1–p53 program in preclinical models, and alaninol or related mechanistic probes have been used experimentally. None constitutes an established AARS1-targeted human treatment, and indiscriminate inhibition risks compromising essential tRNA charging. The most attractive future strategy would selectively block the noncanonical lactyltransferase or trafficking function while preserving aminoacylation. (gao2025aars1andaars2 pages 8-10, gao2025aars1andaars2 pages 6-8)

## 7. Evidence assessment and expert interpretation

1. **Canonical status—high confidence:** cytoplasmic Ala-tRNA^Ala synthesis, G3:U70 recognition, and Ser/Gly editing are conserved, mechanistically coherent, and supported by genetics, biochemistry, and structural evolution. (mahmood2025yeastmodelsfor pages 4-6, mahmood2025yeastmodelsfor pages 2-4)
2. **Localization—high confidence for cytoplasm, context-dependent for nucleus:** cytoplasmic translation is the basal setting; lactate-regulated nuclear import is supported in tumor models but may not be universal. (gao2025aars1andaars2 pages 4-6)
3. **Lactyltransferase function—important but emerging:** three prominent 2024 reports support ATP-dependent lactylation, yet substrate breadth, endogenous kinetics, tissue thresholds, and separation from other enzymatic or nonenzymatic lactylation routes require further work. (zhou2026theroleof pages 12-14, gao2025aars1andaars2 pages 8-10, gao2025aars1andaars2 pages 4-6)
4. **Disease mechanism—allele-specific:** recessive disease often reflects reduced essential activity, whereas dominant neuropathy can involve dominant-negative or neomorphic interactions. Enzyme activity alone cannot classify every pathogenic allele. (mahmood2025yeastmodelsfor pages 4-6, kuo2025recessivepathogenicaars1 pages 1-3)
5. **Clinical translation—preclinical:** AARS1 is diagnostically actionable as a disease gene, but neither inherited AARS1 disorders nor AARS1-driven lactylation currently has a validated, approved gene-specific therapy. (gao2025aars1andaars2 pages 6-8, kuo2025recessivepathogenicaars1 pages 1-3)

## Conclusion

The most defensible functional annotation for human AARS1/P49588 is: **a predominantly cytoplasmic class-II alanyl-tRNA synthetase that uses ATP to charge G3:U70-containing tRNA^Ala with L-alanine and proofreads mischarged Ser/Gly-tRNA^Ala, thereby supplying accurate substrates for cytoplasmic translation.** A regulated nuclear pool has an emerging noncanonical role as an ATP-dependent L-lactate sensor and lysine lactyltransferase, with 2024 evidence for p53 and YAP–TEAD regulation in cancer. These newer functions are compelling but should remain explicitly separated from the mature canonical annotation and from AARS2-specific mitochondrial and cGAS mechanisms.

References

1. (mahmood2025yeastmodelsfor pages 4-6): Maria Mahmood, Emma Little, Nicole Girard, Fanqi Wu, Tristan N Samuels, Ilka U. Heinemann, and Noah M. Reynolds. Yeast models for charcot‐marie‐tooth disease‐causing aminoacyl‐trna synthetase alleles reveal the cellular basis of disease. Iubmb Life, Mar 2025. URL: https://doi.org/10.1002/iub.70017, doi:10.1002/iub.70017. This article has 7 citations and is from a peer-reviewed journal.

2. (gao2025aars1andaars2 pages 4-6): Lingyue Gao, Ji-Hua Guo, and Rong Jia. Aars1 and aars2: from protein synthesis to lactylation-driven oncogenesis. Biomolecules, 15:1323, Sep 2025. URL: https://doi.org/10.3390/biom15091323, doi:10.3390/biom15091323. This article has 16 citations.

3. (mahmood2025yeastmodelsfor pages 2-4): Maria Mahmood, Emma Little, Nicole Girard, Fanqi Wu, Tristan N Samuels, Ilka U. Heinemann, and Noah M. Reynolds. Yeast models for charcot‐marie‐tooth disease‐causing aminoacyl‐trna synthetase alleles reveal the cellular basis of disease. Iubmb Life, Mar 2025. URL: https://doi.org/10.1002/iub.70017, doi:10.1002/iub.70017. This article has 7 citations and is from a peer-reviewed journal.

4. (zhou2026theroleof pages 12-14): Xiao-Yan Zhou and Xing-Ju Zhou. The role of alanyl-trna synthetase 1 lactylation in tumors and other diseases. Discover Oncology, Feb 2026. URL: https://doi.org/10.1007/s12672-026-04549-5, doi:10.1007/s12672-026-04549-5. This article has 1 citations.

5. (gao2025aars1andaars2 pages 8-10): Lingyue Gao, Ji-Hua Guo, and Rong Jia. Aars1 and aars2: from protein synthesis to lactylation-driven oncogenesis. Biomolecules, 15:1323, Sep 2025. URL: https://doi.org/10.3390/biom15091323, doi:10.3390/biom15091323. This article has 16 citations.

6. (gao2025aars1andaars2 pages 6-8): Lingyue Gao, Ji-Hua Guo, and Rong Jia. Aars1 and aars2: from protein synthesis to lactylation-driven oncogenesis. Biomolecules, 15:1323, Sep 2025. URL: https://doi.org/10.3390/biom15091323, doi:10.3390/biom15091323. This article has 16 citations.

7. (kuo2025recessivepathogenicaars1 pages 1-3): Molly E. Kuo, Kira E. Jonatzke, Maclaine Parish, and Anthony Antonellis. Recessive, pathogenic aars1 variants display variable loss-of-function and dominant-negative effects. Disease Models & Mechanisms, Jun 2025. URL: https://doi.org/10.1242/dmm.052006, doi:10.1242/dmm.052006. This article has 3 citations and is from a domain leading peer-reviewed journal.

8. (zhou2026theroleof pages 14-14): Xiao-Yan Zhou and Xing-Ju Zhou. The role of alanyl-trna synthetase 1 lactylation in tumors and other diseases. Discover Oncology, Feb 2026. URL: https://doi.org/10.1007/s12672-026-04549-5, doi:10.1007/s12672-026-04549-5. This article has 1 citations.

9. (fu2026comprehensivepancanceranalysis pages 23-23): Tingting Fu, Ke Ni, Zhiye Wang, Sheng-Nan Sun, Yi Liu, and Qiang Wan. Comprehensive pan-cancer analysis of aars1, a newly identified lactyltransferase in human cancers. Cancer Cell International, Apr 2026. URL: https://doi.org/10.1186/s12935-026-04288-1, doi:10.1186/s12935-026-04288-1. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](AARS1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. mahmood2025yeastmodelsfor pages 4-6
2. zhou2026theroleof pages 12-14
3. zhou2026theroleof pages 14-14
4. mahmood2025yeastmodelsfor pages 2-4
5. fu2026comprehensivepancanceranalysis pages 23-23
6. 10.1016/j.cell.2024.04.002
7. 10.1172/JCI174587
8. 10.1038/s41586-024-07992-y
9. 10.1038/s41436-021-01286-8
10. https://doi.org/10.1016/j.cell.2024.04.002
11. https://doi.org/10.1172/JCI174587
12. https://doi.org/10.1038/s41586-024-07992-y
13. https://doi.org/10.1038/s41436-021-01286-8
14. https://doi.org/10.1002/iub.70017,
15. https://doi.org/10.3390/biom15091323,
16. https://doi.org/10.1007/s12672-026-04549-5,
17. https://doi.org/10.1242/dmm.052006,
18. https://doi.org/10.1186/s12935-026-04288-1,