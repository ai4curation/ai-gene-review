---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-05-30T10:59:49.052842'
end_time: '2026-05-30T10:59:49.055826'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: hsp-12.3
  gene_symbol: hsp-12.3
  uniprot_accession: Q20164
  protein_description: 'SubName: Full=SHSP domain-containing protein {ECO:0000313|EMBL:CAA92770.1};'
  gene_info: Name=hsp-12.3 {ECO:0000313|EMBL:CAA92770.1, ECO:0000313|WormBase:F38E11.1};
    ORFNames=CELE_F38E11.1 {ECO:0000313|EMBL:CAA92770.1}, F38E11.1 {ECO:0000313|WormBase:F38E11.1};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the small heat shock protein (HSP20) family.
  protein_domains: A-crystallin/Hsp20_dom. (IPR002068); Alpha-crystallin/sHSP_animal.
    (IPR001436); HSP20-like_chaperone. (IPR008978); HSP20 (PF00011)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: hsp-12.3-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q20164
- **Protein Description:** SubName: Full=SHSP domain-containing protein {ECO:0000313|EMBL:CAA92770.1};
- **Gene Information:** Name=hsp-12.3 {ECO:0000313|EMBL:CAA92770.1, ECO:0000313|WormBase:F38E11.1}; ORFNames=CELE_F38E11.1 {ECO:0000313|EMBL:CAA92770.1}, F38E11.1 {ECO:0000313|WormBase:F38E11.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the small heat shock protein (HSP20) family.
- **Key Domains:** A-crystallin/Hsp20_dom. (IPR002068); Alpha-crystallin/sHSP_animal. (IPR001436); HSP20-like_chaperone. (IPR008978); HSP20 (PF00011)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hsp-12.3" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hsp-12.3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hsp-12.3** (gene ID: hsp-12.3, UniProt: Q20164) in worm.

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
- **UniProt Accession:** Q20164
- **Protein Description:** SubName: Full=SHSP domain-containing protein {ECO:0000313|EMBL:CAA92770.1};
- **Gene Information:** Name=hsp-12.3 {ECO:0000313|EMBL:CAA92770.1, ECO:0000313|WormBase:F38E11.1}; ORFNames=CELE_F38E11.1 {ECO:0000313|EMBL:CAA92770.1}, F38E11.1 {ECO:0000313|WormBase:F38E11.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the small heat shock protein (HSP20) family.
- **Key Domains:** A-crystallin/Hsp20_dom. (IPR002068); Alpha-crystallin/sHSP_animal. (IPR001436); HSP20-like_chaperone. (IPR008978); HSP20 (PF00011)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hsp-12.3" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hsp-12.3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hsp-12.3** (gene ID: hsp-12.3, UniProt: Q20164) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: *Caenorhabditis elegans* **hsp-12.3** (UniProt Q20164; ORF **F38E11.1**) — functional annotation

### 1) Target verification (gene/protein identity)
The literature retrieved here explicitly refers to **hsp-12.3** as the *C. elegans* small heat shock protein encoded by **ORF F38E11.1** (also referred to as Ce12.3), placing it in the **Hsp12 / small heat shock protein (sHSP)** group with an **α-crystallin domain** and a strongly reduced overall architecture compared with larger sHSPs. This matches the UniProt-provided identity for Q20164 (SHSP domain-containing protein; HSP20 family; α-crystallin/sHSP domain). (krause2013structuralandfunctional pages 29-32, ramsay2012investigatingtherolea pages 37-42)

### 2) Key concepts and current understanding

#### 2.1 Small heat shock proteins (sHSPs) and the α-crystallin domain
sHSPs are ATP-independent chaperone-like proteins classically associated with buffering proteotoxic stress. In *C. elegans*, Hsp-12 family proteins are described as **very small (~12 kDa)** proteins that retain the conserved **α-crystallin domain** but have **markedly shortened N-termini** and **little to no C-terminal tail**, i.e., a “minimal” sHSP architecture. (krause2013structuralandfunctional pages 29-32, ramsay2012investigatingtherolea pages 37-42)

#### 2.2 Oligomerization state and complex formation
Unlike many sHSPs that form larger multimeric assemblies, HSP-12.3 is reported to assemble as a **tetramer**, and is additionally reported to form **heterotetramers with HSP-12.2**. This suggests that HSP-12.3’s primary functional unit in vivo could involve partner-dependent assembly rather than the large polydisperse oligomers seen in many other sHSPs. (ramsay2012investigatingtherole pages 82-86, krause2013structuralandfunctional pages 29-32)

#### 2.3 Chaperone activity: in vitro “holdase” assays vs in vivo specialization
A recurring theme in the Hsp-12 family is that **standard in vitro aggregation-suppression assays may not detect robust activity** for some members. Recombinant **HSP-12.3 did not prevent citrate synthase aggregation** in a thermal unfolding assay, indicating **no detectable classical holdase activity under those conditions**. This negative result has been interpreted as consistent with the highly truncated termini (important for substrate binding/solubility in many sHSPs) and/or with specialized in vivo contexts not captured by the assay. (ramsay2012investigatingtherole pages 42-46, ramsay2012investigatingtherolea pages 42-46)

### 3) Regulation and pathways (signaling and transcriptional control)

#### 3.1 Insulin/IGF-1 signaling (IIS) → DAF-16/FOXO
Multiple sources treat **hsp-12.3 as an IIS/DAF-16-associated stress gene**: it is reported as **upregulated when daf-2/IIS is reduced** and **downregulated when daf-16 activity is reduced**, consistent with hsp-12.3 being among downstream DAF-16-linked stress/longevity effector genes (often cited alongside canonical targets such as sod-3 in the broader literature). (ramsay2012investigatingtherolea pages 82-86, ramsay2012investigatingtherolea pages 31-37)

#### 3.2 HPK-1 (homeodomain-interacting protein kinase) and stress/aging regulation
In a peer-reviewed study of **HPK-1** in stress responses and aging, **hsp-12.3 (F38E11.1)** is specifically noted among genes with **reduced expression** in **hpk-1 loss-of-function** animals (microarray Table S1 referenced in the paper). Although the excerpt available here does not provide a gene-specific fold change for hsp-12.3, the same study reports that loss of HPK-1 reduces survival after acute heat stress by **~25%**, and that HPK-1 and DAF-16 act in the same genetic pathway for lifespan regulation (no additive effect in daf-16; hpk-1). (berber2016homeodomaininteractingproteinkinase pages 9-10)

#### 3.3 Hypoxia response and HIF-1 (2024 development)
A 2024 genome-wide study of short-term hypoxia responses and HIF-1 binding reports **hsp-12.3** among **stress-response genes positively regulated by HIF-1 under short-term hypoxia** (listed in Table 1 category “Stress response”). In the excerpt available, the authors provide a category-level enrichment statistic (Bonferroni/FDR reported for that group) but not a gene-specific hsp-12.3 fold-change value, and the excerpt does not provide direct locus-level ChIP-seq binding evidence for hsp-12.3 (so “direct HIF-1 target” status cannot be confirmed from the provided text). (feng2024wholegenomeprofiling pages 4-6)

### 4) Subcellular localization and where the gene product acts
Direct, hsp-12.3-specific subcellular localization evidence was limited in the retrieved text excerpts. A structural/functional characterization of *C. elegans* Hsp12-family proteins reports immunostaining and developmental expression patterns primarily for Hsp12.6, with adult staining restricted to vulval cells and the spermatheca; the authors note antibody cross-reactivity suggesting similar localization for other family members such as Hsp12.3, but this remains **inferred rather than definitively demonstrated for Hsp-12.3**. (krause2013structuralandfunctional pages 29-32)

Given the lack of direct localization data for Hsp-12.3 in the extracted material, the most defensible current statement is that **Hsp-12.3 is a small cytosolic sHSP-family protein**, but its precise subcellular compartment(s) and tissue specificity require confirmation with gene-specific reporters or specific antibodies.

### 5) Functional roles and phenotypes

#### 5.1 Longevity and stress resistance (direct tests)
In the retrieved lifespan/RNAi testing described in a thesis focused on the paralog hsp-12.6, **hsp-12.3(RNAi) did not measurably alter lifespan** across several tested genetic backgrounds (including wild type and stress/longevity pathway mutant backgrounds). Importantly, the authors caution that RNAi specificity was not confirmed and propose that redundancy (including potential dependence on HSP-12.2/HSP-12.3 heterotetramer formation) could mask phenotypes; therefore these negative data should be considered **inconclusive rather than definitive evidence of no function**. (ramsay2012investigatingtherolea pages 82-86, ramsay2012investigatingtherole pages 82-86)

#### 5.2 Proteostasis mechanism: sequestration vs non-sequestration sHSP roles
A high-quality mechanistic study of conserved sHSP-mediated sequestration of misfolded proteins classifies **Hsp-12.3 as “sequestrase-negative”** in their assay framework (i.e., no complementation/sequestration activity detected in that system). The same work links sequestrase activity to specific sequence features in terminal extensions (including differences in average N- and C-terminal extension lengths between positive vs negative sHSPs), and notes that Hsp-12.3 lacks motifs/sequence features associated with sequestrase-positive behavior in their analyses. Functionally, this suggests Hsp-12.3 is unlikely to be a major driver of inclusion-forming sequestration, and instead may act via other sHSP mechanisms (or in specialized contexts not captured by that assay). (shrivastava2022thecytoprotectivesequestration pages 24-28, shrivastava2022thecytoprotectivesequestration pages 6-8)

#### 5.3 Age-dependent abundance (protein-level evidence)
Deep quantitative proteomics identified **HSP-12.3 among proteins that increase with age**. Specifically, the study reported **55 proteins** that increased with age; **25% (14/55)** increased to a greater extent in long-lived **daf-2(e1370)** mutants, and **HSP-12.3** is explicitly listed among this subset. This supports the interpretation that HSP-12.3 is part of the proteostasis/stress-protective remodeling associated with aging and IIS modulation at the **protein abundance** level, not only transcriptionally. (narayan2016deepproteomeanalysis pages 10-12)

### 6) Recent developments (prioritizing 2023–2024)

#### 6.1 2024: HIF-1/hypoxia genomics links hsp-12.3 to oxygen-stress response
The inclusion of hsp-12.3 in a 2024 HIF-1 hypoxia-responsive gene set expands its functional annotation beyond IIS/DAF-16-associated stress response, implicating it in the **cross-talk between hypoxia and proteostasis/stress programs**. However, the available excerpt does not specify whether HIF-1 regulation is direct (via ChIP peak at the locus) or indirect. (feng2024wholegenomeprofiling pages 4-6)

#### 6.2 2024: Multi-omics in disease-model worms highlights stress/detox regulatory architecture relevant to hsp genes
A 2024 *npj Science of Food* study in an Aβ-transgenic worm model (CL4176) emphasizes that transcriptomic changes under a neuroprotective intervention involve stress/detox and metabolism programs controlled by transcription factors including **DAF-16**, **SKN-1**, **PMK-1**, and others. While this paper’s excerpted pages do not provide a direct hsp-12.3 quantitative value, it provides current context for why hsp-family genes are frequently used as pathway readouts in real-world worm intervention experiments. (valdes2024invivoneuroprotective pages 10-11)

### 7) Current applications and real-world implementations

1. **Biomarker/readout of stress-response pathway activity.** Across aging, stress, and intervention studies, hsp-12.3 is repeatedly treated as a canonical stress gene whose expression reflects activity in conserved stress and longevity pathways (notably IIS/DAF-16 and, more recently, hypoxia/HIF-1 contexts). (ramsay2012investigatingtherolea pages 31-37, feng2024wholegenomeprofiling pages 4-6)
2. **Perturbation experiments.** hsp-12.3 is amenable to RNAi knockdown and has been tested in lifespan assays; the currently retrieved lifespan RNAi results are negative but flagged as technically and biologically non-definitive due to potential redundancy/complex formation with Hsp-12.2. (ramsay2012investigatingtherolea pages 82-86, ramsay2012investigatingtherole pages 82-86)
3. **Proteome-scale aging studies.** HSP-12.3 can serve as a protein-level marker in quantitative proteomics for age/IIS-dependent remodeling of the proteostasis network. (narayan2016deepproteomeanalysis pages 10-12)

### 8) Expert synthesis and limitations (authoritative analysis)
The most consistent, evidence-backed annotation is that HSP-12.3 is a **minimal α-crystallin-domain sHSP** that forms **tetramers/heterotetramers**, is **regulated in major stress/longevity transcriptional programs** (DAF-16-linked and HIF-1-linked), and shows **age- and daf-2-dependent abundance changes**, but has **unclear direct substrate specificity and unclear localization** based on currently retrieved text excerpts. (ramsay2012investigatingtherole pages 82-86, krause2013structuralandfunctional pages 29-32, feng2024wholegenomeprofiling pages 4-6, narayan2016deepproteomeanalysis pages 10-12)

Mechanistically, the evidence argues against classifying HSP-12.3 as a major “sequestrase” (inclusion-forming sequestration factor) in the framework of Shrivastava et al. 2022, and against strong generic holdase activity in the standard citrate synthase assay; this combination supports a model where HSP-12.3 has **context-specific or partner-dependent functions** (e.g., specific client proteins, specific tissues, or specific stress combinations) that remain to be precisely defined experimentally. (ramsay2012investigatingtherolea pages 42-46, shrivastava2022thecytoprotectivesequestration pages 24-28)

### 9) Evidence summary table
The table below consolidates the main annotation-relevant findings by evidence type, with citation IDs and DOIs/URLs where available.

| Aspect | Key finding | Evidence type | Study (author, year, journal) | Quantitative/statistical detail (if any) | URL/DOI (if present in paper metadata) | Citation ID to use |
|---|---|---|---|---|---|---|
| identity/domain | HSP-12.3 is the C. elegans small heat shock protein encoded by F38E11.1 (Ce12.3), belonging to the Hsp12/sHSP family and retaining the conserved α-crystallin domain with very short N-terminus and little or no C-terminal tail. | Sequence/structural annotation; comparative family analysis | Krause, 2013, unknown journal; Ramsay, 2012, unknown journal | Family proteins are ~12.2–12.6 kDa; α-crystallin core described as ~80–100 aa. | N/A | (krause2013structuralandfunctional pages 29-32, ramsay2012investigatingtherolea pages 37-42) |
| oligomerization | Unlike many sHSPs that form large multimers, HSP-12.3 is reported to assemble as a tetramer, and HSP-12.2/HSP-12.3 can form heterotetramers. | In vitro biochemistry / oligomerization analysis | Krause, 2013, unknown journal; Ramsay, 2012, unknown journal | Tetrameric organization reported for Hsp12 members except Hsp12.6 in recombinant preparations. | N/A | (krause2013structuralandfunctional pages 29-32, ramsay2012investigatingtherole pages 82-86) |
| in vitro chaperone activity | Recombinant HSP-12.3 did not prevent aggregation of thermally unfolding citrate synthase in standard assays, so no conventional in vitro chaperone activity was detected. | In vitro chaperone assay | Ramsay, 2012, unknown journal | Negative assay reported at 43°C with citrate synthase aggregation assay. | N/A | (ramsay2012investigatingtherole pages 42-46, ramsay2012investigatingtherolea pages 42-46) |
| regulation/pathways | hsp-12.3 is repeatedly described as a DAF-16/FOXO-associated insulin-signaling target, being upregulated when daf-2/IIS is reduced and downregulated when daf-16 activity is reduced; hpk-1 loss also reduces hsp-12.3 expression. | Transcriptomics / genetics | Ramsay, 2012, unknown journal; Berber et al., 2016, Scientific Reports | No gene-specific fold-change reported in extracted text; HPK-1 loss reduced post-stress survival by ~25% overall, while hsp-12.3 was among genes reduced in hpk-1(-). | https://doi.org/10.1038/srep19582 | (ramsay2012investigatingtherolea pages 82-86, berber2016homeodomaininteractingproteinkinase pages 9-10, ramsay2012investigatingtherolea pages 31-37) |
| hypoxia/HIF-1 | In 2024 whole-genome hypoxia profiling, hsp-12.3 was listed among stress-response genes positively regulated by HIF-1 under short-term hypoxia, but the supplied excerpt did not give an hsp-12.3-specific fold change or direct-target ChIP evidence. | RNA-seq / hypoxia transcriptomics | Feng, Qu & Powell-Coffman, 2024, PLOS ONE | Stress-response category significance Bonferroni/FDR = 7.88E-03; no per-gene hsp-12.3 value in provided text. | https://doi.org/10.1371/journal.pone.0295094 | (feng2024wholegenomeprofiling pages 4-6) |
| proteostasis/sequestration | In the evolutionary sequestration study, HSP-12.3 was classified as sequestrase-negative and lacked sequence features associated with sequestrase-positive sHSPs, arguing against a major role in inclusion-forming sequestration. | Comparative functional assay / sequence-feature analysis | Shrivastava et al., 2022, Journal of Cell Biology | Sequestrase-positive sHSPs had longer NTEs on average (39 vs 25 aa) and longer CTEs (21 vs 6 aa); Hsp-12.3 was in the “none” group for sequestrase activity. | https://doi.org/10.1083/jcb.202202149 | (shrivastava2022thecytoprotectivesequestration pages 24-28, shrivastava2022thecytoprotectivesequestration pages 6-8) |
| expression with age | HSP-12.3 protein abundance increases with age and is among age-increasing proteins that rise even more strongly in long-lived daf-2 mutants. | Deep quantitative proteomics | Narayan et al., 2016, Cell Systems | 55 proteins increased with age; 25% (14/55) increased to a much greater extent in daf-2(e1370), including HSP-12.3; >9,300 proteins were reproducibly identified per replicate. | https://doi.org/10.1016/j.cels.2016.06.011 | (narayan2016deepproteomeanalysis pages 10-12) |
| localization/tissue expression | Direct HSP-12.3 localization evidence is limited; cross-reactive antibody data suggest expression patterns similar to Hsp12-family proteins, while Hsp12.6 family staining in adults is restricted to vulval cells and spermatheca, so localization for HSP-12.3 remains inferred rather than definitive. | Immunostaining / family-level expression analysis | Krause, 2013, unknown journal | Hsp12.6 peaks in L1 and in adults localizes to vulval cells and spermatheca; explicit HSP-12.3 localization was not shown in the excerpt. | N/A | (krause2013structuralandfunctional pages 29-32, krause2013structuralandfunctional pages 1-8) |
| phenotypes/functional tests | hsp-12.3 RNAi did not measurably alter lifespan in several tested genetic backgrounds, but the result is considered inconclusive because RNAi specificity was not verified and redundancy with hsp-12.2/heterotetramerization could mask function. | Genetics / RNAi lifespan testing | Ramsay, 2012, unknown journal | No lifespan effect seen in N2, phsp-12.6::HSP-12.6::DSRED2, hsf-1(sy441), or daf-16(mu86) backgrounds in the reported experiments. | N/A | (ramsay2012investigatingtherolea pages 82-86, ramsay2012investigatingtherole pages 82-86) |


*Table: This table compiles the most relevant evidence found for C. elegans hsp-12.3/F38E11.1, organized by annotation-relevant aspects such as domain identity, regulation, localization, and functional testing. It is useful as a quick evidence map distinguishing direct findings from family-level inference and highlighting where data remain limited.*

### References (URLs/DOIs and publication dates where available)

- Feng D, Qu L, Powell-Coffman JA. **Whole genome profiling of short-term hypoxia induced genes and identification of HIF-1 binding sites provide insights into HIF-1 function in *C. elegans*.** *PLOS ONE*. **2024-05**. https://doi.org/10.1371/journal.pone.0295094 (feng2024wholegenomeprofiling pages 4-6)
- Berber S, et al. **Homeodomain-Interacting Protein Kinase (HPK-1) regulates stress responses and ageing in *C. elegans*.** *Scientific Reports*. **2016-01**. https://doi.org/10.1038/srep19582 (berber2016homeodomaininteractingproteinkinase pages 9-10)
- Shrivastava A, et al. **The cytoprotective sequestration activity of small heat shock proteins is evolutionarily conserved.** *Journal of Cell Biology*. **2022-09**. https://doi.org/10.1083/jcb.202202149 (shrivastava2022thecytoprotectivesequestration pages 24-28, shrivastava2022thecytoprotectivesequestration pages 6-8)
- Narayan V, et al. **Deep Proteome Analysis Identifies Age-Related Processes in *C. elegans*.** *Cell Systems*. **2016-08**. https://doi.org/10.1016/j.cels.2016.06.011 (narayan2016deepproteomeanalysis pages 10-12)

*Note:* Some sources retrieved as theses/unknown-journal texts (e.g., Ramsay 2012; Krause 2013) contained relevant Hsp-12.3 family characterization but did not include stable DOI metadata in the extracted segments. (ramsay2012investigatingtherolea pages 82-86, krause2013structuralandfunctional pages 29-32)

References

1. (krause2013structuralandfunctional pages 29-32): M Krause. Structural and functional characterization of small heat shock proteins of the nematode caenorhabditis elegans. Unknown journal, 2013.

2. (ramsay2012investigatingtherolea pages 37-42): LF Ramsay. Investigating the role of the small heat shock protein, hsp-12.6, in longevity in caenorhabditis elegans. Unknown journal, 2012.

3. (ramsay2012investigatingtherole pages 82-86): LF Ramsay. Investigating the role of the small heat shock protein, hsp-12.6, in longevity in caenorhabditis elegans. Unknown journal, 2012.

4. (ramsay2012investigatingtherole pages 42-46): LF Ramsay. Investigating the role of the small heat shock protein, hsp-12.6, in longevity in caenorhabditis elegans. Unknown journal, 2012.

5. (ramsay2012investigatingtherolea pages 42-46): LF Ramsay. Investigating the role of the small heat shock protein, hsp-12.6, in longevity in caenorhabditis elegans. Unknown journal, 2012.

6. (ramsay2012investigatingtherolea pages 82-86): LF Ramsay. Investigating the role of the small heat shock protein, hsp-12.6, in longevity in caenorhabditis elegans. Unknown journal, 2012.

7. (ramsay2012investigatingtherolea pages 31-37): LF Ramsay. Investigating the role of the small heat shock protein, hsp-12.6, in longevity in caenorhabditis elegans. Unknown journal, 2012.

8. (berber2016homeodomaininteractingproteinkinase pages 9-10): Slavica Berber, Mallory Wood, Estelle Llamosas, Priya Thaivalappil, Karen Lee, Bing Mana Liao, Yee Lian Chew, Aaron Rhodes, Duygu Yucel, Merlin Crossley, and Hannah R Nicholas. Homeodomain-interacting protein kinase (hpk-1) regulates stress responses and ageing in c. elegans. Scientific Reports, Jan 2016. URL: https://doi.org/10.1038/srep19582, doi:10.1038/srep19582. This article has 27 citations and is from a peer-reviewed journal.

9. (feng2024wholegenomeprofiling pages 4-6): Dingxia Feng, Long Qu, and Jo Anne Powell-Coffman. Whole genome profiling of short-term hypoxia induced genes and identification of hif-1 binding sites provide insights into hif-1 function in caenorhabditis elegans. PLOS ONE, 19:e0295094, May 2024. URL: https://doi.org/10.1371/journal.pone.0295094, doi:10.1371/journal.pone.0295094. This article has 8 citations and is from a peer-reviewed journal.

10. (shrivastava2022thecytoprotectivesequestration pages 24-28): Aseem Shrivastava, Carl Alexander Sandhof, Kevin Reinle, Areeb Jawed, Carmen Ruger-Herreros, Dominic Schwarz, Declan Creamer, Carmen Nussbaum-Krammer, Axel Mogk, and Bernd Bukau. The cytoprotective sequestration activity of small heat shock proteins is evolutionarily conserved. Sep 2022. URL: https://doi.org/10.1083/jcb.202202149, doi:10.1083/jcb.202202149. This article has 20 citations and is from a highest quality peer-reviewed journal.

11. (shrivastava2022thecytoprotectivesequestration pages 6-8): Aseem Shrivastava, Carl Alexander Sandhof, Kevin Reinle, Areeb Jawed, Carmen Ruger-Herreros, Dominic Schwarz, Declan Creamer, Carmen Nussbaum-Krammer, Axel Mogk, and Bernd Bukau. The cytoprotective sequestration activity of small heat shock proteins is evolutionarily conserved. Sep 2022. URL: https://doi.org/10.1083/jcb.202202149, doi:10.1083/jcb.202202149. This article has 20 citations and is from a highest quality peer-reviewed journal.

12. (narayan2016deepproteomeanalysis pages 10-12): Vikram Narayan, Tony Ly, Ehsan Pourkarimi, Alejandro Brenes Murillo, Anton Gartner, Angus I. Lamond, and Cynthia Kenyon. Deep proteome analysis identifies age-related processes in c. elegans. Cell Systems, 3:144-159, Aug 2016. URL: https://doi.org/10.1016/j.cels.2016.06.011, doi:10.1016/j.cels.2016.06.011. This article has 141 citations and is from a domain leading peer-reviewed journal.

13. (valdes2024invivoneuroprotective pages 10-11): Alberto Valdés, José David Sánchez-Martínez, Rocío Gallego, Elena Ibáñez, Miguel Herrero, and Alejandro Cifuentes. In vivo neuroprotective capacity of a dunaliella salina extract - comprehensive transcriptomics and metabolomics study. NPJ Science of Food, Jan 2024. URL: https://doi.org/10.1038/s41538-023-00246-7, doi:10.1038/s41538-023-00246-7. This article has 12 citations and is from a domain leading peer-reviewed journal.

14. (krause2013structuralandfunctional pages 1-8): M Krause. Structural and functional characterization of small heat shock proteins of the nematode caenorhabditis elegans. Unknown journal, 2013.

## Artifacts

- [Edison artifact artifact-00](hsp-12.3-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. berber2016homeodomaininteractingproteinkinase pages 9-10
2. feng2024wholegenomeprofiling pages 4-6
3. krause2013structuralandfunctional pages 29-32
4. narayan2016deepproteomeanalysis pages 10-12
5. valdes2024invivoneuroprotective pages 10-11
6. ramsay2012investigatingtherolea pages 37-42
7. ramsay2012investigatingtherole pages 82-86
8. ramsay2012investigatingtherole pages 42-46
9. ramsay2012investigatingtherolea pages 42-46
10. ramsay2012investigatingtherolea pages 82-86
11. ramsay2012investigatingtherolea pages 31-37
12. shrivastava2022thecytoprotectivesequestration pages 24-28
13. shrivastava2022thecytoprotectivesequestration pages 6-8
14. krause2013structuralandfunctional pages 1-8
15. https://doi.org/10.1038/srep19582
16. https://doi.org/10.1371/journal.pone.0295094
17. https://doi.org/10.1083/jcb.202202149
18. https://doi.org/10.1016/j.cels.2016.06.011
19. https://doi.org/10.1038/srep19582,
20. https://doi.org/10.1371/journal.pone.0295094,
21. https://doi.org/10.1083/jcb.202202149,
22. https://doi.org/10.1016/j.cels.2016.06.011,
23. https://doi.org/10.1038/s41538-023-00246-7,