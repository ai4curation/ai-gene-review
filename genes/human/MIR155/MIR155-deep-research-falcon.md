---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T03:29:14.815285'
end_time: '2026-05-11T03:56:23.361626'
duration_seconds: 1628.55
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

Research the human microRNA gene MIR155 (miR-155; RNAcentral URS000062749E_9606) for Gene Ontology functional annotation. This is a microRNA/non-coding RNA, not a protein; do not infer protein domains or enzyme activity. Focus on its core molecular function as a guide RNA in miRNA-mediated post-transcriptional gene silencing, RISC association, immune and oncogenic regulatory contexts only where they clarify direct function, cellular localization, and GO terms directly supported by primary literature. Distinguish core function from downstream immune or cancer phenotypes, and provide citations for each major claim.

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

Research the human microRNA gene MIR155 (miR-155; RNAcentral URS000062749E_9606) for Gene Ontology functional annotation. This is a microRNA/non-coding RNA, not a protein; do not infer protein domains or enzyme activity. Focus on its core molecular function as a guide RNA in miRNA-mediated post-transcriptional gene silencing, RISC association, immune and oncogenic regulatory contexts only where they clarify direct function, cellular localization, and GO terms directly supported by primary literature. Distinguish core function from downstream immune or cancer phenotypes, and provide citations for each major claim.

# Research report: Gene Ontology (GO) functional annotation evidence for human MIR155 (miR‑155; RNAcentral URS000062749E_9606)

## 1. Key concepts and definitions (current understanding)

### 1.1 What MIR155 encodes
MIR155 is a *microRNA* (miRNA) gene that produces short (~22 nt) mature miRNA strands (classically annotated as miR‑155‑5p and miR‑155‑3p) that function as sequence-specific guide RNAs for Argonaute proteins within the RNA-induced silencing complex (RISC). Its molecular function is therefore not enzymatic; it is an RNA effector that confers targeting specificity to RISC via base-pairing to complementary sites in target RNAs.

### 1.2 What counts as GO-relevant “core function” for a miRNA gene
For a miRNA, GO-relevant *core* functions are those directly supported by experiments demonstrating:
- **Association with Argonaute/RISC** (cellular component and molecular function evidence), and
- **Direct, sequence-dependent targeting of RNAs** causing **post-transcriptional gene silencing** (biological process evidence), via mRNA destabilization and/or translational repression.

Immune and oncogenic roles are downstream phenotypic outcomes of altering gene networks; they are included here only insofar as they clarify direct molecular mechanism, location, and evidence-backed GO terms.

## 2. Primary-literature evidence supporting GO-relevant annotation for MIR155

### 2.1 Argonaute/RISC association (core molecular function and cellular component)

**Argonaute RIP in primary human macrophages (direct RISC loading evidence).** In primary human monocyte-derived macrophages, Simmonds (2019) immunoprecipitated Argonaute proteins (anti-Ago antibody 2A8) and measured miRNAs in the immunoprecipitate using absolute quantitation. The study reports that miR‑155‑3p was not detectable above background in resting cells but **after 2 h LPS stimulation it was recovered from the Argonaute IP**, consistent with **RISC association/loading** at the time of peak induction. The same approach detected miR‑155‑5p in Argonaute IP as well. Quantitatively, the study estimated **cellular copy numbers** in resting vs stimulated cells: miR‑155‑3p ~29±11 copies/cell at rest rising to **~767±137 copies/cell at 2 h LPS** (range 446–1,134); miR‑155‑5p ~1,315±417 (rest) rising to ~5,578±1,361 (2 h LPS). This provides direct biochemical evidence supporting annotation of MIR155 products to the **RNA-induced silencing complex** and to guide-RNA molecular function through Argonaute association. (simmonds2019transientupregulationof pages 11-12, simmonds2019transientupregulationof pages 12-14, simmonds2019transientupregulationof media a21bb4f5, simmonds2019transientupregulationof media 5691fff6)

**Argonaute2 RIP in human cells showing miR‑155 guide participation in an Ago2 miRNP.** In HT‑29 human colon cancer cells, Al‑Haidari et al. (2018) used Ago2 immunoprecipitation and qRT-PCR to show that **AntagomiR‑155‑5p reduced enrichment of both miR‑155‑5p and HuR (ELAVL1) mRNA in Ago2 immunoprecipitates**, indicating that miR‑155‑5p participates in Ago2-containing ribonucleoprotein complexes engaging a target mRNA. (alhaidari2018mir1555pcontrolscolon pages 28-29)

**Transcriptome-wide Argonaute CLIP mapping requires miR‑155 to direct Ago binding.** Loeb et al. (2012) used differential Argonaute HITS-CLIP (“AGO dCLIP”) comparing WT vs miR‑155 knockout activated CD4+ T cells to identify **miR‑155-dependent Ago-binding peaks**, demonstrating that the presence of miR‑155 directs Argonaute binding to specific RNA sites. (loeb2012transcriptomewidemir155binding pages 1-2, loeb2012transcriptomewidemir155binding pages 2-3)

### 2.2 miRNA-mediated post-transcriptional gene silencing (core biological process)

**Direct, miR‑155-dependent Argonaute binding correlates with repression.** Loeb et al. (2012) report that differential CLIP identified **191 miR‑155-dependent Ago binding sites in 175 genes (p<0.01)**, and that differential Ago binding **correlated with target downregulation** (p<0.05), supporting annotation to miRNA-mediated gene silencing and post-transcriptional regulation of gene expression. The study further reports that miR‑155–Ago complexes occupy **>300 canonical 3′UTR sites** with perfect 6–8 nt seed matches and that these canonical targets are strongly regulated by miR‑155. (loeb2012transcriptomewidemir155binding pages 2-3, loeb2012transcriptomewidemir155binding pages 7-8)

**Noncanonical targeting is common for miR‑155 (refines mechanistic understanding but still core guide function).** In the same Loeb et al. binding map, **~40% of miR‑155-dependent Ago binding sites lacked perfect seed matches**, implying widespread noncanonical interactions; these tended to produce more modest regulation. Reporter validation showed mutation of predicted noncanonical sites significantly reduced repression by miR‑155, supporting direct functional targeting even without perfect seed matches. This evidence informs annotation to miRNA-mediated silencing without over-specifying “seed-only” rules. (loeb2012transcriptomewidemir155binding pages 7-8, loeb2012transcriptomewidemir155binding pages 6-7)

**Direct sequence-element dependence in a miR‑155-guided interaction (context-dependent repression vs activation).** Al‑Haidari et al. (2018) provide direct evidence that miR‑155‑5p binds AU-rich elements in the HuR 3′UTR, validated using target-site blockers and ribonucleoprotein immunoprecipitation approaches. Notably, they observe context dependence (serum-starved vs serum-fed) where miR‑155‑5p can positively regulate HuR translation/mRNA levels under quiescence-like conditions; this does not negate the core GO process (post-transcriptional regulation via guide RNA), but cautions that “gene silencing” directionality may depend on cellular state and target context. (alhaidari2018mir1555pcontrolscolon pages 1-7, alhaidari2018mir1555pcontrolscolon pages 7-11)

### 2.3 Cellular localization / cellular component (what is directly supported)

**Supported: RISC / Argonaute-containing cytoplasmic effector complex.** Direct Argonaute immunoprecipitation in human macrophages provides strong evidence that miR‑155 strands are physically present in Argonaute/RISC complexes. This supports GO cellular component annotation to **RNA-induced silencing complex**. (simmonds2019transientupregulationof pages 11-12, simmonds2019transientupregulationof pages 12-14, simmonds2019transientupregulationof media a21bb4f5, simmonds2019transientupregulationof media 5691fff6)

**Not sufficiently supported in the current primary-evidence set: P-bodies, stress granules, extracellular vesicles.** Although many reviews and some non-miR‑155-specific literature connect Ago/miRNPs to P-bodies and EV biology, the retrieved primary evidence in this run does **not** provide a direct, miR‑155-specific demonstration (e.g., microscopy co-localization of miR‑155 with P-body markers; EV isolation plus miR‑155 quantification with rigorous controls) that would justify assigning MIR155 a GO cellular component annotation to P-body/stress granule or extracellular vesicle *as a core function*. (witten2020mir155asa pages 18-19, de2020amyloidbetaoligomers pages 25-30)

## 3. Evidence-based GO annotation summary (proposed terms and support)

The table below summarizes GO-relevant annotations derived from *direct evidence* in the primary literature available here and flags terms that are not currently well supported.

| GO aspect | GO term label (GO ID if known) | Evidence summary | miR-155 strand | Biological system | Supporting citations |
|---|---|---|---|---|---|
| MF | miRNA-mediated gene silencing by RNA binding | Argonaute RIP in primary human monocyte-derived macrophages using anti-Ago (2A8) recovered miR-155-3p and miR-155-5p from RISC; miR-155-3p was undetectable above background in resting cells but recovered after 2 h LPS, indicating direct guide-RNA association with Ago/RISC. | 3p, 5p | Primary human monocyte-derived macrophages | (simmonds2019transientupregulationof pages 11-12, simmonds2019transientupregulationof pages 12-14) |
| MF | RNA guide activity | Ago2-RIP/qRT-PCR in HT-29 cells showed antagomiR-155-5p reduced enrichment of both miR-155-5p and HuR mRNA in Ago2 immunoprecipitates, supporting direct guide-RNA function of miR-155-5p within Ago2-containing effector complexes. | 5p | HT-29 human colon cancer cells | (alhaidari2018mir1555pcontrolscolon pages 28-29, alhaidari2018mir1555pcontrolscolon pages 7-11) |
| BP | miRNA-mediated post-transcriptional gene silencing (GO:0035195) | Differential Ago HITS-CLIP/dCLIP comparing WT and miR-155-knockout activated CD4+ T cells identified 191 miR-155-dependent Ago-binding sites in 175 genes; loss of miR-155 reduced Ago occupancy and correlated with target downregulation/repression, providing transcriptome-wide evidence for miR-155-mediated silencing. | 5p | Activated murine CD4+ T cells | (loeb2012transcriptomewidemir155binding pages 1-2, loeb2012transcriptomewidemir155binding pages 2-3) |
| BP | post-transcriptional regulation of gene expression | In serum-starved HT-29 cells, target-site blocker and Ago2-RIP experiments showed miR-155-5p directly binds AU-rich elements in the HuR 3′UTR and regulates HuR mRNA levels/translation post-transcriptionally. | 5p | HT-29 human colon cancer cells | (alhaidari2018mir1555pcontrolscolon pages 1-7, alhaidari2018mir1555pcontrolscolon pages 7-11) |
| BP | gene silencing by miRNA | Transcriptome-wide Ago dCLIP showed miR-155 guides Ago to >300 canonical 3′UTR sites and many noncanonical sites; ~40% of miR-155-dependent Ago binding lacked perfect seed matches, indicating direct target repression can include noncanonical binding modes. | 5p | Activated murine primary T cells | (loeb2012transcriptomewidemir155binding pages 7-8, loeb2012transcriptomewidemir155binding pages 1-2) |
| CC | RNA-induced silencing complex | Anti-Ago immunoprecipitation followed by absolute miRNA quantification demonstrated miR-155-5p and inducible miR-155-3p are present in Ago-containing RISC in primary macrophages. | 3p, 5p | Primary human monocyte-derived macrophages | (simmonds2019transientupregulationof pages 11-12, simmonds2019transientupregulationof media a21bb4f5) |
| CC | cytoplasm | In HT-29 cells, miR-155-5p knockdown decreased cytoplasmic HuR expression; the study examines miR-155-5p-mediated post-transcriptional regulation of a cytoplasmic target context, but does not directly localize miR-155 RNA itself by imaging/fractionation, so support for cytoplasmic localization of MIR155/miR-155 is indirect and should be used cautiously. | 5p | HT-29 human colon cancer cells | (alhaidari2018mir1555pcontrolscolon pages 1-7) |
| CC | P-body / stress granule | No direct primary evidence in the provided context shows MIR155/miR-155 itself localized to P-bodies or stress granules by microscopy or specific fractionation; related literature in context concerns general Ago/P-body biology or non-miR-155-specific compartmentation and is insufficient for confident annotation of MIR155 to these CC terms. | — | — | (witten2020mir155asa pages 18-19) |
| CC | extracellular vesicle | The provided context includes review-level discussion and indirect/preprint evidence for extracellular or endosomal miR-155 contexts, but no high-confidence primary evidence sufficient here to assign MIR155 a GO cellular-component annotation to extracellular vesicle for core function. | — | — | (de2020amyloidbetaoligomers pages 25-30, witten2020mir155asa pages 18-19) |


*Table: This table maps proposed GO annotations for human MIR155/miR-155 to direct primary-literature evidence available in the current context. It highlights well-supported core functions and compartments while flagging localization terms that are not sufficiently supported for confident annotation.*

## 4. Recent developments (prioritizing 2023–2024) and how they relate to core GO function

### 4.1 Clinical translation of miR‑155 inhibition as a test of functional relevance (not GO core function)
A major recent-development theme is clinical translation of miR‑155 inhibition (anti-miR/antagomir strategies), most prominently **cobomarsen (MRG‑106)**.

A 2024 review of miRNA therapeutics describes **cobomarsen (MRG‑106) as an LNA-based antagomir of miR‑155**, noting a completed phase 1 trial and that phase 2 studies were initiated but at least two phase 2 trials were terminated; it also notes that at least one termination was due to business reasons rather than safety/efficacy concerns (as per ClinicalTrials.gov, accessed 20 Dec 2023). This literature is useful for “current applications” but does not replace primary biochemical evidence for GO annotation. (seyhan2024trialsandtribulations pages 16-17)

### 4.2 Subcellular compartmentalization is an active research area but remains difficult to convert into miR‑155-specific GO CC terms
Recent reviews increasingly emphasize miRNA localization heterogeneity (endosomes, ER-associated polysomes, etc.) and extracellular RNA transport, but miR‑155-specific localization evidence must be supported by rigorous primary experiments. A 2020 fractionation-based study (bioRxiv) describes optiprep gradient fractionation and reports measuring distribution of miR‑155 in endosomal fractions in Aβ-treated glial cells, illustrating methods that could support future GO CC annotation if replicated and validated. However, in this run, the relevant excerpt does not provide numeric outcomes sufficient to assert a specific GO CC term for MIR155 beyond RISC. (de2020amyloidbetaoligomers pages 25-30, de2020amyloidbetaoligomers pages 18-23)

## 5. Current applications and real-world implementations

### 5.1 Therapeutic inhibition: cobomarsen (MRG‑106)
ClinicalTrials.gov provides direct, citable implementation details for cobomarsen/MRG‑106 targeting miR‑155.

- **NCT02580552 (Phase 1, completed; n=66)**: dose-ranging safety/tolerability/PK study in MF (CTCL), CLL, DLBCL (ABC), ATLL. Routes included **intratumoral, subcutaneous, and intravenous** administration; exploratory endpoints included **miR‑155‑5p expression in MF skin lesions (qRT-PCR)** and dermatology-related QoL measures. Start date 2016‑02‑09; completion 2020‑10‑06. (NCT02580552 chunk 1, NCT02580552 chunk 2)
- **NCT03713320 (SOLAR; Phase 2; terminated; actual enrollment 37)**: randomized open-label study in mycosis fungoides comparing cobomarsen (IV infusion) vs vorinostat (oral). The record states termination was **“for business reasons, and not due to concerns regarding safety or lack of efficacy.”** Start 2019‑04‑02; completion 2020‑12‑01; registry indicates **results were posted** (results first post date 2022‑04‑08). (NCT03713320 chunk 1)

These trials provide real-world validation that miR‑155 can be modulated in patients, and they operationalize miR‑155’s role as a guide RNA in post-transcriptional regulation (pharmacodynamic readouts), but they do not define additional GO molecular functions beyond miRNA-mediated silencing.

| Application type | Agent/Assay | Target | Indication | Trial ID | Phase | Status | Enrollment | Route | Key endpoints/outcomes mentioned | Termination reason (if any) | Publication/registry URL | Supporting citations (context IDs) |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| Therapeutic | Cobomarsen (MRG-106), LNA-based anti-miR / ASO | miR-155 | Mycosis fungoides (CTCL), CLL, DLBCL, ATLL | NCT02580552 | Phase 1 | Completed | 66 | Intratumoral, subcutaneous, intravenous | Safety, tolerability, pharmacokinetics; exploratory outcomes included overall survival, miR-155-5p expression in MF skin lesions, neoplastic lymphoid-cell proportions, immune-cell subsets, Skindex-29 and pruritus measures; review sources describe early clinical improvement signals in CAILS, mSWAT, and Skindex-29 with no serious adverse events attributed to cobomarsen in early reports | Not applicable; completed study | https://clinicaltrials.gov/study/NCT02580552 ; https://doi.org/10.3390/cancers14061588 ; https://doi.org/10.3390/ijms25031469 | (NCT02580552 chunk 1, NCT02580552 chunk 2, smith2022clinicalapplicationsof pages 7-8, seyhan2024trialsandtribulations pages 16-17, witten2020mir155asa pages 14-15) |
| Therapeutic | Cobomarsen (MRG-106) vs active comparator (vorinostat) | miR-155 | Cutaneous T-cell lymphoma, mycosis fungoides | NCT03713320 | Phase 2 | Terminated | 37 | Cobomarsen: 2-hour intravenous infusion; comparator vorinostat: oral | Efficacy/safety outcomes included 50% improvement in mSWAT, pruritus medication utilization, PK endpoints (Cmax, AUC), and anti-drug antibody generation; registry states results were submitted/posted | “Terminated early for business reasons, and not due to concerns regarding safety or lack of efficacy.” | https://clinicaltrials.gov/study/NCT03713320 ; https://doi.org/10.3390/ijms25031469 | (NCT03713320 chunk 1, NCT03713320 chunk 2, seyhan2024trialsandtribulations pages 16-17) |
| Therapeutic | Cobomarsen (MRG-106) extension after SOLAR | miR-155 | Mycosis fungoides after SOLAR completion | NCT03837457 | Phase 2 | Terminated | 8 | Not available in provided context | Extension study identified in review/trial listings; no posted outcome details available in provided context | Not stated in provided context | https://clinicaltrials.gov/study/NCT03837457 ; https://doi.org/10.3390/ijms25031469 | (seyhan2024trialsandtribulations pages 16-17, piergentili2025targetingregulatorynoncoding pages 16-17) |
| Therapeutic/Translational | Cobomarsen (MRG-106) program summary in reviews | miR-155 | Lymphomas/leukemias including CTCL, CLL, DLBCL, ATLL | Program-level | Phase 1 completed; Phase 2 initiated/terminated | Mixed | — | Intratumoral, intravenous, subcutaneous reported across studies | Seyhan 2024 identifies cobomarsen as an LNA-based antagomir and notes completed phase 1 plus terminated phase 2 studies; Smith 2022 lists miRagen-sponsored ASO program and delivery routes; Witten & Slack 2020 describe reductions in miR-155 target-gene expression in biopsies and sustained improvements in lesion/quality-of-life metrics in early reports | Review states at least one terminated study ended for business reasons rather than safety/efficacy concerns | https://doi.org/10.3390/ijms25031469 ; https://doi.org/10.3390/cancers14061588 ; https://doi.org/10.1093/carcin/bgz183 | (seyhan2024trialsandtribulations pages 16-17, smith2022clinicalapplicationsof pages 7-8, witten2020mir155asa pages 13-14, witten2020mir155asa pages 14-15) |
| Diagnostic/biomarker | miR-155 expression assays / circulating or tissue miR-155 profiling | miR-155 | Hematologic malignancy and inflammatory-disease biomarker studies (observational and ancillary uses) | Multiple non-cobomarsen studies in registry | Observational / non-therapeutic | Ongoing, completed, or unknown depending on study | Varies | Biospecimen assay | Used as biomarker/prognostic or pharmacodynamic readout rather than direct therapeutic intervention; examples in provided context include lesion miR-155-5p qRT-PCR in NCT02580552 and review discussion of biomarker utility | Not applicable | https://clinicaltrials.gov/study/NCT02580552 ; https://doi.org/10.3390/ijms25031469 | (NCT02580552 chunk 2, seyhan2024trialsandtribulations pages 16-17) |


*Table: This table summarizes miR-155-targeting real-world applications, focusing on cobomarsen/MRG-106 clinical development and registry-level details. It is useful for linking therapeutic and biomarker use cases to specific trial phases, statuses, routes, and reported outcomes.*

## 6. Expert opinions and authoritative analysis (distinguishing core function from phenotype)

### 6.1 What authoritative sources emphasize about miR‑155
Authoritative reviews in hematologic malignancy emphasize miR‑155 as an oncogenic miRNA and summarize early clinical signals from cobomarsen, including improved lesion-burden and QoL metrics and lack of serious adverse events attributed to the drug in early reports. These expert analyses support clinical interest and translational feasibility but should be treated as secondary evidence relative to primary mechanistic studies for GO annotations. (witten2020mir155asa pages 14-15)

### 6.2 Separation of direct function from downstream immune/cancer phenotypes
The direct molecular function of MIR155 is **Argonaute-associated guide RNA function** that mediates post-transcriptional regulation (typically repression) of target RNAs. Immune activation, inflammation, and oncogenesis arise from downstream network effects of repressing many target transcripts and are better considered *phenotypic consequences* rather than direct GO molecular function. The dCLIP data show miR‑155 guides Ago to hundreds of sites in an endogenous, transcriptome-wide manner, supporting network-level regulatory capacity without implying new molecular activities beyond RNA-guided silencing. (loeb2012transcriptomewidemir155binding pages 7-8, loeb2012transcriptomewidemir155binding pages 2-3)

## 7. Relevant recent statistics and data

### 7.1 Quantitative miR‑155 abundance and RISC association
In primary human macrophages, absolute quantitation estimated mean copy numbers per cell and demonstrated inducible RISC association:
- miR‑155‑3p: ~29±11 copies/cell resting; **~767±137 copies/cell at 2 h LPS** (range 446–1,134)
- miR‑155‑5p: ~1,315±417 copies/cell resting; ~5,578±1,361 copies/cell at 2 h LPS
These data are directly relevant for GO annotation because they support that miR‑155 strands reach measurable abundance and are physically present in Argonaute immunoprecipitates at biologically relevant times. (simmonds2019transientupregulationof pages 11-12)

### 7.2 Clinical trial statistics (implementation-level)
- NCT02580552: **66 participants**, Phase 1, completed. (NCT02580552 chunk 1)
- NCT03713320: **37 participants**, Phase 2, terminated early for business reasons; results posted 2022‑04‑08 per registry. (NCT03713320 chunk 1)

## 8. Limitations of this evidence set for GO cellular-component expansion
Within the retrieved corpus, strong direct evidence exists for miR‑155 association with Argonaute/RISC and for miR‑155-guided post-transcriptional regulation. However, *miR‑155-specific* evidence for localization to P-bodies/stress granules or extracellular vesicles was not sufficiently explicit/quantitative in the extracted primary text to support confident GO cellular-component annotation to those compartments in this report. (witten2020mir155asa pages 18-19, de2020amyloidbetaoligomers pages 25-30)

## Key URLs (publication/registry)
- Simmonds RE. Wellcome Open Research (2019-03). https://doi.org/10.12688/wellcomeopenres.15065.1 (simmonds2019transientupregulationof pages 11-12)
- Al-Haidari A et al. Cancer Letters (2018-05). https://doi.org/10.1016/j.canlet.2018.02.026 (alhaidari2018mir1555pcontrolscolon pages 1-7)
- Loeb GB et al. Molecular Cell (2012-12). https://doi.org/10.1016/j.molcel.2012.10.002 (loeb2012transcriptomewidemir155binding pages 1-2)
- Seyhan AA. Int J Mol Sci (2024-01). https://doi.org/10.3390/ijms25031469 (seyhan2024trialsandtribulations pages 16-17)
- ClinicalTrials.gov NCT02580552. https://clinicaltrials.gov/study/NCT02580552 (NCT02580552 chunk 1)
- ClinicalTrials.gov NCT03713320. https://clinicaltrials.gov/study/NCT03713320 (NCT03713320 chunk 1)



References

1. (simmonds2019transientupregulationof pages 11-12): Rachel E. Simmonds. Transient up-regulation of mir-155-3p by lipopolysaccharide in primary human monocyte-derived macrophages results in risc incorporation but does not alter tnf expression. Wellcome Open Research, 4:43, Mar 2019. URL: https://doi.org/10.12688/wellcomeopenres.15065.1, doi:10.12688/wellcomeopenres.15065.1. This article has 21 citations.

2. (simmonds2019transientupregulationof pages 12-14): Rachel E. Simmonds. Transient up-regulation of mir-155-3p by lipopolysaccharide in primary human monocyte-derived macrophages results in risc incorporation but does not alter tnf expression. Wellcome Open Research, 4:43, Mar 2019. URL: https://doi.org/10.12688/wellcomeopenres.15065.1, doi:10.12688/wellcomeopenres.15065.1. This article has 21 citations.

3. (simmonds2019transientupregulationof media a21bb4f5): Rachel E. Simmonds. Transient up-regulation of mir-155-3p by lipopolysaccharide in primary human monocyte-derived macrophages results in risc incorporation but does not alter tnf expression. Wellcome Open Research, 4:43, Mar 2019. URL: https://doi.org/10.12688/wellcomeopenres.15065.1, doi:10.12688/wellcomeopenres.15065.1. This article has 21 citations.

4. (simmonds2019transientupregulationof media 5691fff6): Rachel E. Simmonds. Transient up-regulation of mir-155-3p by lipopolysaccharide in primary human monocyte-derived macrophages results in risc incorporation but does not alter tnf expression. Wellcome Open Research, 4:43, Mar 2019. URL: https://doi.org/10.12688/wellcomeopenres.15065.1, doi:10.12688/wellcomeopenres.15065.1. This article has 21 citations.

5. (alhaidari2018mir1555pcontrolscolon pages 28-29): Amr Al-Haidari, Anwar Algaber, Raed Madhi, Ingvar Syk, and Henrik Thorlacius. Mir-155-5p controls colon cancer cell migration via post-transcriptional regulation of human antigen r (hur). Cancer letters, 421:145-151, May 2018. URL: https://doi.org/10.1016/j.canlet.2018.02.026, doi:10.1016/j.canlet.2018.02.026. This article has 78 citations and is from a peer-reviewed journal.

6. (loeb2012transcriptomewidemir155binding pages 1-2): Gabriel B. Loeb, Aly A. Khan, David Canner, Joseph B. Hiatt, Jay Shendure, Robert B. Darnell, Christina S. Leslie, and Alexander Y. Rudensky. Transcriptome-wide mir-155 binding map reveals widespread noncanonical microrna targeting. Molecular cell, 48 5:760-70, Dec 2012. URL: https://doi.org/10.1016/j.molcel.2012.10.002, doi:10.1016/j.molcel.2012.10.002. This article has 403 citations and is from a highest quality peer-reviewed journal.

7. (loeb2012transcriptomewidemir155binding pages 2-3): Gabriel B. Loeb, Aly A. Khan, David Canner, Joseph B. Hiatt, Jay Shendure, Robert B. Darnell, Christina S. Leslie, and Alexander Y. Rudensky. Transcriptome-wide mir-155 binding map reveals widespread noncanonical microrna targeting. Molecular cell, 48 5:760-70, Dec 2012. URL: https://doi.org/10.1016/j.molcel.2012.10.002, doi:10.1016/j.molcel.2012.10.002. This article has 403 citations and is from a highest quality peer-reviewed journal.

8. (loeb2012transcriptomewidemir155binding pages 7-8): Gabriel B. Loeb, Aly A. Khan, David Canner, Joseph B. Hiatt, Jay Shendure, Robert B. Darnell, Christina S. Leslie, and Alexander Y. Rudensky. Transcriptome-wide mir-155 binding map reveals widespread noncanonical microrna targeting. Molecular cell, 48 5:760-70, Dec 2012. URL: https://doi.org/10.1016/j.molcel.2012.10.002, doi:10.1016/j.molcel.2012.10.002. This article has 403 citations and is from a highest quality peer-reviewed journal.

9. (loeb2012transcriptomewidemir155binding pages 6-7): Gabriel B. Loeb, Aly A. Khan, David Canner, Joseph B. Hiatt, Jay Shendure, Robert B. Darnell, Christina S. Leslie, and Alexander Y. Rudensky. Transcriptome-wide mir-155 binding map reveals widespread noncanonical microrna targeting. Molecular cell, 48 5:760-70, Dec 2012. URL: https://doi.org/10.1016/j.molcel.2012.10.002, doi:10.1016/j.molcel.2012.10.002. This article has 403 citations and is from a highest quality peer-reviewed journal.

10. (alhaidari2018mir1555pcontrolscolon pages 1-7): Amr Al-Haidari, Anwar Algaber, Raed Madhi, Ingvar Syk, and Henrik Thorlacius. Mir-155-5p controls colon cancer cell migration via post-transcriptional regulation of human antigen r (hur). Cancer letters, 421:145-151, May 2018. URL: https://doi.org/10.1016/j.canlet.2018.02.026, doi:10.1016/j.canlet.2018.02.026. This article has 78 citations and is from a peer-reviewed journal.

11. (alhaidari2018mir1555pcontrolscolon pages 7-11): Amr Al-Haidari, Anwar Algaber, Raed Madhi, Ingvar Syk, and Henrik Thorlacius. Mir-155-5p controls colon cancer cell migration via post-transcriptional regulation of human antigen r (hur). Cancer letters, 421:145-151, May 2018. URL: https://doi.org/10.1016/j.canlet.2018.02.026, doi:10.1016/j.canlet.2018.02.026. This article has 78 citations and is from a peer-reviewed journal.

12. (witten2020mir155asa pages 18-19): Lisa Witten and Frank J Slack. Mir-155 as a novel clinical target for hematological malignancies. Carcinogenesis, 41:2-7, Nov 2020. URL: https://doi.org/10.1093/carcin/bgz183, doi:10.1093/carcin/bgz183. This article has 119 citations and is from a peer-reviewed journal.

13. (de2020amyloidbetaoligomers pages 25-30): Dipayan De and Suvendra N. Bhattacharyya. Amyloid beta oligomers prevents lysosomal targeting of mirnp to stop its recycling and target cytokine repression in glial cells. bioRxiv, Dec 2020. URL: https://doi.org/10.1101/2020.12.24.424324, doi:10.1101/2020.12.24.424324. This article has 0 citations.

14. (seyhan2024trialsandtribulations pages 16-17): Attila A Seyhan. Trials and tribulations of microrna therapeutics. International Journal of Molecular Sciences, Jan 2024. URL: https://doi.org/10.3390/ijms25031469, doi:10.3390/ijms25031469. This article has 393 citations.

15. (de2020amyloidbetaoligomers pages 18-23): Dipayan De and Suvendra N. Bhattacharyya. Amyloid beta oligomers prevents lysosomal targeting of mirnp to stop its recycling and target cytokine repression in glial cells. bioRxiv, Dec 2020. URL: https://doi.org/10.1101/2020.12.24.424324, doi:10.1101/2020.12.24.424324. This article has 0 citations.

16. (NCT02580552 chunk 1):  Safety, Tolerability and Pharmacokinetics of MRG-106 in Patients With Mycosis Fungoides (MF), CLL, DLBCL or ATLL. miRagen Therapeutics, Inc.. 2016. ClinicalTrials.gov Identifier: NCT02580552

17. (NCT02580552 chunk 2):  Safety, Tolerability and Pharmacokinetics of MRG-106 in Patients With Mycosis Fungoides (MF), CLL, DLBCL or ATLL. miRagen Therapeutics, Inc.. 2016. ClinicalTrials.gov Identifier: NCT02580552

18. (NCT03713320 chunk 1):  SOLAR: Efficacy and Safety of Cobomarsen (MRG-106) vs. Active Comparator in Subjects With Mycosis Fungoides. miRagen Therapeutics, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03713320

19. (smith2022clinicalapplicationsof pages 7-8): Ellen S. Smith, Eric Whitty, Byunghee Yoo, Anna Moore, Lorenzo F. Sempere, and Zdravka Medarova. Clinical applications of short non-coding rna-based therapies in the era of precision medicine. Cancers, 14:1588, Mar 2022. URL: https://doi.org/10.3390/cancers14061588, doi:10.3390/cancers14061588. This article has 72 citations.

20. (witten2020mir155asa pages 14-15): Lisa Witten and Frank J Slack. Mir-155 as a novel clinical target for hematological malignancies. Carcinogenesis, 41:2-7, Nov 2020. URL: https://doi.org/10.1093/carcin/bgz183, doi:10.1093/carcin/bgz183. This article has 119 citations and is from a peer-reviewed journal.

21. (NCT03713320 chunk 2):  SOLAR: Efficacy and Safety of Cobomarsen (MRG-106) vs. Active Comparator in Subjects With Mycosis Fungoides. miRagen Therapeutics, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03713320

22. (piergentili2025targetingregulatorynoncoding pages 16-17): R. Piergentili and S. Sechi. Targeting regulatory noncoding rnas in human cancer: the state of the art in clinical trials. Pharmaceutics, Apr 2025. URL: https://doi.org/10.3390/pharmaceutics17040471, doi:10.3390/pharmaceutics17040471. This article has 4 citations.

23. (witten2020mir155asa pages 13-14): Lisa Witten and Frank J Slack. Mir-155 as a novel clinical target for hematological malignancies. Carcinogenesis, 41:2-7, Nov 2020. URL: https://doi.org/10.1093/carcin/bgz183, doi:10.1093/carcin/bgz183. This article has 119 citations and is from a peer-reviewed journal.

## Citations

1. seyhan2024trialsandtribulations pages 16-17
2. simmonds2019transientupregulationof pages 11-12
3. simmonds2019transientupregulationof pages 12-14
4. de2020amyloidbetaoligomers pages 25-30
5. de2020amyloidbetaoligomers pages 18-23
6. smith2022clinicalapplicationsof pages 7-8
7. piergentili2025targetingregulatorynoncoding pages 16-17
8. https://clinicaltrials.gov/study/NCT02580552
9. https://doi.org/10.3390/cancers14061588
10. https://doi.org/10.3390/ijms25031469
11. https://clinicaltrials.gov/study/NCT03713320
12. https://clinicaltrials.gov/study/NCT03837457
13. https://doi.org/10.1093/carcin/bgz183
14. https://doi.org/10.12688/wellcomeopenres.15065.1
15. https://doi.org/10.1016/j.canlet.2018.02.026
16. https://doi.org/10.1016/j.molcel.2012.10.002
17. https://doi.org/10.12688/wellcomeopenres.15065.1,
18. https://doi.org/10.1016/j.canlet.2018.02.026,
19. https://doi.org/10.1016/j.molcel.2012.10.002,
20. https://doi.org/10.1093/carcin/bgz183,
21. https://doi.org/10.1101/2020.12.24.424324,
22. https://doi.org/10.3390/ijms25031469,
23. https://doi.org/10.3390/cancers14061588,
24. https://doi.org/10.3390/pharmaceutics17040471,