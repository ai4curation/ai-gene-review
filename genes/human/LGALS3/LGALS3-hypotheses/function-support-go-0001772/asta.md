---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:46:21.281259'
end_time: '2026-06-22T04:46:24.012974'
duration_seconds: 2.73
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0001772
  hypothesis_text: LGALS3 has immunological synapse (GO:0001772).
  term_context: '- Term: immunological synapse (GO:0001772)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[6]
  source_context_yaml: "term:\n  id: GO:0001772\n  label: immunological synapse\n\
    evidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    query_char_limit: 500
    paper_limit: 50
    snippet_limit: 20
    snippet_paper_limit: 50
    restrict_snippets_to_papers: false
    paper_fields: title,abstract,authors,year,url,venue,journal,tldr,publicationDate,citationCount,influentialCitationCount,externalIds
    publication_date_range: ''
    venues: ''
    inserted_before: ''
citation_count: 11
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has immunological synapse (GO:0001772).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has immunological synapse (GO:0001772).
Key context:
- Term: immunological synapse (GO:0001772)
- Existing evidence type: IBA
- Original reference: GO_REF:0000033

Retrieve primary experimental papers that directly test this claim for
LGALS3 (or a well-supported ortholog): assays, mutant phenotypes,
localisation, interactions, or structures.

<!--
The lines above are deliberately first so length-limited retrieval providers
(e.g. asta, which truncates the query to ~500 characters) search on the gene
and its biology rather than on the curation boilerplate below.
-->

## How to use this prompt

You are searching for **independent literature support for the single
gene-function hypothesis stated above**. The hypothesis is a plain claim that a
gene product has a particular molecular function, biological role, or cellular
location. Find primary (or well-justified orthologous) evidence that **confirms
or refutes** that claim for this specific gene.

This is a recall-oriented search: surface every plausible piece of supporting
evidence, but make each candidate **independently checkable** so a downstream
curator or agent can filter false positives. This is not a general gene
overview, and any prior curation decision shown in the context is intentionally
neutralised — judge the hypothesis on the external evidence, not on the existing
annotation.

A common use of this template is confirming annotations that currently rest only
on phylogenetic inference (evidence code IBA, propagated from PANTHER
`GO_REF:0000033`), but it applies to any gene-function hypothesis.

## Focus

- **Focus type:** function_support
- **Hypothesis slug:** function-support-go-0001772
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[6]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0001772
  label: immunological synapse
evidence_type: IBA
original_reference_id: GO_REF:0000033
```

## Research Objective

Find the strongest available **independent** evidence bearing on whether the
hypothesis is true for LGALS3. Prioritise, in order:

1. Direct experimental evidence in LGALS3 itself (the named gene in the
   named organism): assays, mutant phenotypes, localisation, interactions,
   structures.
2. Direct experimental evidence in a clearly orthologous gene, where the
   orthology is well established and the function is expected to be conserved.
3. Strong indirect or computational evidence (domain architecture, conserved
   motifs, structural homology, operon/pathway context), reported
   conservatively.

Prefer **PMID** citations; include **DOI** citations when no PMID is available.
Treat reviews and database records as orientation only — cite the underlying
primary papers wherever possible.

**Expect false positives.** This pipeline is tuned for recall, so a downstream
curator/agent will sift your results. For every candidate you must therefore
provide an **exact verbatim snippet** from the source that can be checked, plus
enough context (organism, assay, gene actually studied) to detect paralog
confusion, wrong-organism carry-over, or claims that are really about a
different gene.

## Required Output

### Executive Judgment

State whether independent support exists: **supported** (with strong primary
evidence), **partially / indirectly supported**, **unresolved** (no independent
evidence found), or **refuted**. One short paragraph; lead with the verdict.

### Evidence Matrix

A table with one row per candidate evidence item:

- Citation (PMID preferred; DOI otherwise)
- Gene/protein actually studied (and organism) — flag if it is an ortholog or a paralog
- Evidence type (direct assay, mutant phenotype, localization, interaction, structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies
- Exact verbatim snippet to verify (quote the source)
- Key finding in your own words
- Confidence and the most important caveat (false-positive risk)

### Best Supporting References

List the 1–3 references most suitable to add to the review's `supported_by`
for this hypothesis, each with the exact snippet a curator should confirm. If
none qualify, say so explicitly.

### Conflicts and Alternatives

Note any evidence that contradicts the hypothesis or that points to paralog
confusion, organism-specific differences, isoform-specific findings, or
database carry-over.

### Knowledge Gaps

If no adequate independent evidence exists, state what was searched, why the gap
matters, and what evidence or experiment would resolve it.


## Output

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has immunological synapse (GO:0001772). Gene/protein: LGALS3. O...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 11
- Snippets retrieved: 19

## Relevant Papers

### [1] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
- Authors: Yinghui Ren, Yongmei Qian, Qicheng Zhang, Xiaoping Li, Mingjiang Li et al.
- Year: 2024
- Venue: Cancer Cell International
- URL: https://www.semanticscholar.org/paper/552bd37c67dea75d0c33a9a0de2acdafcf0dcf6e
- DOI: 10.1186/s12935-024-03309-1
- PMID: 38643145
- PMCID: 11031979
- Citations: 13
- Summary: It is hypothesized that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC and the upregulation of LGALS3 via the HCP5/hsa-miR-27b-3p axis is associated with unfavorable prognosis and increased tumor immune infiltration in HCC.
- Evidence snippets:
  - Snippet 1 (score: 0.759)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly
  - Snippet 2 (score: 0.737)
    > analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly higher immune cell scores and immune checkpoint expression levels. Finally, GSVA analysis was performed to predict potential signaling pathways linked to LGALS3 and HCP5 in immune evasion and metabolic reprogramming of HCC. Our findings indicated that the upregulation of LGALS3 via the HCP5/hsa-miR-27b-3p axis is associated with unfavorable prognosis and increased tumor immune infiltration in HCC.
  - Snippet 3 (score: 0.737)
    > The immune checkpoint molecules have a vital function in immune surveillance, immune escape, as well as immune editing [19].To further determine the possible oncogenic function of LGALS3 in HCC, the association between LGALS3 and several immunological checkpoints was evaluated.LGALS3 expression showed a significant positive association with CD274, TIGIT, PDCD1, HAVCR2, CTLA4, LAG3, as well as PDCD1LG2 after adjustment for tumor purity in HCC (Fig. 6A-B).Moreover, based on GEPIA2, the same positive association was identified between LGALS3 and these immune checkpoints (Fig. 6C-D).Furthermore, we found that the expression of these immune checkpoints was significantly upregulated in the high LGALS3 expression groups, as shown in Fig. 6E.These findings imply that tumor immune escape may have a role in LGALS3-mediated HCC carcinogenesis.
  - Snippet 4 (score: 0.727)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.
  - Snippet 5 (score: 0.691)
    > To delineate the driving mechanism of LGALS3 for the malignant progression of HCC, the KEGG and GO analysis was conducted.The volcano plot and heatmap showed significantly differentially expressed genes between LGALS3 high-and low-expression groups (Figure S3A-B).The KEGG pathway analysis revealed that these LGALS3-related genes were enriched in the IL-17 signaling pathway, ECM-receptor interaction pathway, central carbon metabolism in cancer pathway, leukocyte transendothelial migration pathway and PI3K-Akt signaling pathway.Meanwhile, the GO analysis revealed that these genes were strongly associated with cell chemotaxis, leukocyte chemotaxis, regulation of leukocyte migration, as well as regulation of chemotaxis (Fig. 5A).Accumulating evidence has proven the immune system has an essential role in malignancy pathogenesis [17], and LGALS3 is closely correlated with CD163 + tumor-associated macrophages (TAM) in glioma [10].Therefore, we studied the association between LGALS3 level and the immune infiltration level in HCC.There was no statistical difference in immune cell infiltration levels over a number of LGALS3 copy numbers (Fig. 5B).Meanwhile, immune infiltration analysis revealed that expression of LGALS3 showed a significant positive association with several immune cell populations, involving CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, dendritic cell, as well as cancer-associated fibroblasts (CAFs) within HCC (Fig. 5C-E).Based on these results, we further evaluated the immune score in HCC patients with high and low LGALS3 expression.The scores of immune cells, including CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, and dendritic cell, were significantly higher in the high LGALS3 expression groups, as shown in Fig. 5F.Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].
  - Snippet 6 (score: 0.690)
    > Next, the prognostic value of LGALS3 expression in the 23 kinds of cancer patients was then determined.Correlations between LGALS3 expression with OS (overall survival) were evaluated using the GEPIA2 database.In the OS study, only elevated LGALS3 expression indicated poorer survival for HCC patients (Fig. 2A).LGALS3 was not statistically significant for OS of 22 other cancer types patients.Furthermore, DSS (disease-specific survival) LGALS3 in predicting 1-, 3-, and 5-year OS. (H) ROC curve for LGALS3 in predicting 1-, 3-, and 5-year DSS.The higher values of AUC corresponding to higher predictive power.*p value < 0.05; ***p value < 0.001 was lesser in patients suffering from HCC having higher levels of LGALS3 expression (Fig. 2B).Next, we validated the expression levels of LGALS3 protein in HCC tissues using IF staining.As expected, HCC tumor demonstrated strong LGALS3 expression (Fig. 2C).These findings were further validated by qRT-PCR assay of tumor and adjacent normal tissues from 5 HCC patients.Here, LGALS3 expression was also significantly increased in the HCC tissues (Fig. 2D).In addition, LGALS3 expression was shown to be linked with the pathological stage of HCC, as illustrated in Fig. 2E.High expression of LGALS3 gene is associated with high tumor grade in HCC (Fig. 2F).Moreover, LGALS3 expression was significantly associated with OS and DSS in both univariate and multivariate analyses (Figure S2A-H).Time-dependent ROC analysis showed that the area under the ROC curve was 0.672 at 5 years of OS, and 0.691 at 5 years of DSS (Fig. 2G-H).Taken together, LGALS3 might function as a prospective biomarker for the prognosis of patients suffering from HCC.
  - Snippet 7 (score: 0.687)
    > Zhang et al. [14] suggested overexpression of LGALS3 promoted HCC bone metastasis and induced associated skeletal complications.Nevertheless, the expression, prognosis, epigenetic, and molecular regulatory mechanisms of LGALS3 in HCC have been incompletely studied.In addition, LGALS3 relation with immune infiltration in HCC TME has yet to be inadequately investigated.
    > This work began with a pan-cancer study of LGALS3 expression and its predictive value in a variety of human malignancies.We further explored the LGALS3 potential upstream regulatory noncoding RNAs (ncRNAs) involving microRNAs (miRNAs) as well as long noncoding RNAs (lncRNAs) throughout HCC.Subsequently, in HCC, a correlation analysis was investigated between LGALS3 and tumor immunity-related indicators involving cell chemotaxis, immune checkpoints, immune cell biomarkers, and infiltration.Eventually, the association between the expression of LGALS3 and signaling pathways was examined in HCC.Findings demonstrated that LGALS3 might have a role in the malignancy of HCC and immune cell infiltration via the HCP5/hsa-miR-27b-3p/ LGALS3 axis, suggesting that a novel HCP5/hsa-miR-27b-3p/LGALS3 axis could be a biomarker for prognosis and treatment target for HCC patients.

### [2] Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice
- Authors: Kevin A. Maupin, Daniel T. Dick, Vari Vivarium, Transgenics Core, B. Williams
- Year: 2020
- Venue: FEBS Open Bio
- URL: https://www.semanticscholar.org/paper/6ab62ea9acc6fef617d0b1f237c1a477f45b05c7
- DOI: 10.1002/2211-5463.13483
- PMID: 36062328
- PMCID: 9527582
- Citations: 2
- Summary: The results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3, while the cortical bone phenotypeof Lgal3- KO mice may have also been influenced by Loss of intracellular galECTin- 3.
- Evidence snippets:
  - Snippet 1 (score: 0.725)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.

### [3] Galectin-3 aggravates microglial activation and tau transmission in tauopathy
- Authors: Jian-Jing Siew, Hui-Mei Chen, Feng‐Lan Chiu, Chia-Wei Lee, Yao-Ming Chang et al.
- Year: 2023
- Venue: The Journal of Clinical Investigation
- URL: https://www.semanticscholar.org/paper/8c77eea796475aa4e26a4051432bc4d4c021d847
- DOI: 10.1172/JCI165523
- PMID: 37988169
- PMCID: 10786694
- Citations: 24
- Influential citations: 1
- Summary: It is shown that Gal3 was upregulated in the microglia of humans and mice with tauopathy, and is a potential therapeutic target for tauopathy.
- Evidence snippets:
  - Snippet 1 (score: 0.700)
    > In particular, the knockout of Gal3 normalized 348 DEG genes between Tau22/Lgals3 +/+ and WT mice (Figure 6, A and B and Supplemental Table 7). Further GO enrichment analysis revealed that the upregulated DEGs of Tau22/Lgals3 +/+ versus WT mice were enriched in multiple processes, including metabolic processes, oxidative reduction processes, and immune system processes (Figure 6, C and D). Importantly, the downregulated DEGs by Lgals3 deletion within the context of Tau22 were primarily enriched in immune responses and the production of cytokines and chemokines (Figure 6E). Conversely, the downregulated DEGs in Tau22/Lgals3 -/-versus Tau22/Lgals3 +/+ mice were enriched in processes including nervous system development, protein phosphorylation, synapse assembly, and learning (Supplemental Figure 21, E and F). No specific enriched processes were identified for the upregulated DEGs in Tau22/Lgals3 -/- versus Tau22/Lgals3 +/+ mice. These findings are consistent with what were observed in human iMGLs, confirming that Gal3 plays a principal role in governing the microglia-mediated immune response in tauopathy.
    > We next categorized these DEGs by their enriched cell type based on the Tabula Muris Consortium database (39) (Supplemental Figure 21D), and, as predicted, we found that the largest population of DEGs identified between Tau22/Lgals3 -/-and Tau22/Lgals3 +/+ mice was enriched in microglia (21.3%; Supple-cells (Figure 8). When encountering pathological tau, microglia become active and release Gal3 into the extracellular space either directly or via EVs (Figure 3O). Under the tested conditions, we found that Gal3 directly facilitated the aggregation of pTau into β-pleated-sheet structures (Figure 3L). This interaction between pTau and Gal3 may occur in EVs and/or the extracellular space between microglia and neurons.
  - Snippet 2 (score: 0.685)
    > Importantly, the loss of Gal3 also prevented the learning and memory deficits present in Tau22/Lgals3 +/+ mice (33) to a great extent, as assessed by the Morris water maze test (Figure 5, H and I). Consistent with the GAM gene analysis (Figure 4, H and I), the number and level of CD68-positive microglia in Tau22/Lgals3 -/-mice were indeed lower than those in Tau22/Lgals3 +/+ mice (Figure 5, J and K), suggesting a key role of Gal3 in microglial activation. Given that synaptic loss is a feature of tauopathy that is also presented in Tau22 mice (33), we performed immunofluorescence staining of synapses at the CA1 region using VGLUT1 and Homer1 as presynaptic and postsynaptic markers, respectively. Our data showed that Gal3 knockout rescued the number of synapses assessed by the colocalization of VGLUT1 and Homer1 (Figure 5, L and M and Supplemental Figure 20, A and B). This finding suggests that GAM mediates the loss of synapses in Tau22 mice.
    > To further delineate the protective role of Gal3 depletion in tauopathy, we analyzed the gene expression profiles of the hippocampi of Tau22/Lgals3 -/-mice and corresponding controls using bulk RNA-Seq. In total, 3,770 DEGs were identified between Tau22/Lgals3 +/+ and WT mice, and 868 DEGs were identified between Tau22/Lgals3 -/-and Tau22/Lgals3 +/+ mice (Supplemental Figure 21, A-D). In particular, the knockout of Gal3 normalized 348 DEG genes between Tau22/Lgals3 +/+ and WT mice (Figure 6, A and B and Supplemental Table 7).

### [4] The deficiency of galectin-3 in stromal cells leads to enhanced tumor growth and bone marrow metastasis
- Authors: J. X. Pereira, Maria Carolina Braga Azeredo, Felipe Sá Martins, R. Chammas, F. L. Oliveira et al.
- Year: 2016
- Venue: BMC Cancer
- URL: https://www.semanticscholar.org/paper/5f5ef422f3c44fa24a457d97d0c915ae8188a279
- DOI: 10.1186/s12885-016-2679-1
- PMID: 27526676
- PMCID: 4986277
- Citations: 12
- Influential citations: 1
- Summary: It is demonstrated for the first time that the absence of galectin-3 in the host microenvironment favors the growth of the primary tumors, the metastatic spread to the inguinal lymph nodes and bone marrow colonization by metastatic 4T1 tumor cells.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > We next investigated whether galectin-3 could influence the development of metastasis to the lymph node. Therefore, 28 days post orthotopic injection (p.o.i) of 4T1 cells in Lgals3+/+ or Lgals3−/− mice, the lymph nodes were excised and the presence of CK-19 positive cells was analyzed by immunohistochemistry. We observed that 4T1 cells (CK-19+) were predominantly present in the capsule of the draining lymph node in Lgals3+/+ mice (Fig. 3a) whereas in Lgals3−/− mice, CK-19+ cells were organized as "sheets-like" within the lymph node parenchyma and also found in the capsule (Fig. 3b). Moreover, we evaluated the presence of lymph node metastasis in Lgals3+/+ and Lgals3−/− mice using the 6-thioguanine clonogenic assay and found significant fewer metastasis in Lgals3+/+ mice in comparison to Lgals3−/− mice, both 21 and 28 days p.o.i. (Fig. 3c, p < 0,05). Interestingly though, we also found an increased CK-19 mRNA levels in Lgals3−/− mice at an earlier stage (15 days) p.o.i. (Fig. 3d, p < 0,05). These results suggest that Lgals3−/− mice are more permissive for 4T1 tumor cells dissemination to the inguinal lymph nodes.
    > Galectin-3-deficient bone marrow microenvironment supports more efficiently the growth of metastatic 4T1
    > We have previously described that Lgals3−/− mice presented structural and functional differences in the bone marrow [17]. Likewise, in this study we confirmed differences in terms of cellularity and projections of bone tissue inside the cavity between Balb/c Lgals3+/+ and Lgals3 −/− mice (Fig. 4a and b).

### [5] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
- Authors: P. Ruvolo, Chenyue W. Hu, Y. Qiu, V. Ruvolo, Robin L. Go et al.
- Year: 2019
- Venue: EBioMedicine
- URL: https://www.semanticscholar.org/paper/46bbdbcb4660389e13acba24499cc415d75f18e0
- DOI: 10.1016/j.ebiom.2019.05.025
- PMID: 31105032
- PMCID: 6604360
- Citations: 25
- Influential citations: 2
- Summary: The data suggest that the LGALS3 network and the CD74 network each support AML cell survival and the two networks may cooperate in a novel high risk AML population.
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.

### [6] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
- Authors: Kui Wang, Shuyue Fu, Lixia Dong, Dingyue Zhang, Mao Wang et al.
- Year: 2023
- Venue: Autophagy
- URL: https://www.semanticscholar.org/paper/3dadfc351823c4e325e65c171ab3765871189c80
- DOI: 10.1080/15548627.2023.2239042
- PMID: 37471054
- Citations: 35
- Influential citations: 2
- Summary: It is shown that periplocin exhibits promising anticancer activity against CRC both in vitro and in vivo, and is indicated as a potential therapeutic option for the treatment of CRC.
- Evidence snippets:
  - Snippet 1 (score: 0.695)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.
  - Snippet 2 (score: 0.693)
    > Scale bar: 10 μm. (I) Immunofluorescent analysis of the colocalization of LGALS3 with ubiquitin in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm. (J) Representative fluorescent images of CRC cells transiently expressing Mrfp-GFP-tandem fluorescent-tagged LGALS3 (tfGal3) followed by 0.50 μM periplocin treatment for 24 h. Scale bar: 10 μm. (K) Quantitative analysis of the GFP + RFP + or GFP − RFP + LGALS3 puncta in (J). (L) the relative decreased ratio of Magic Red intensity, relative increased ratio of LysoSensor Blue intensity, relative increased ratio of the interaction between LGALS3 and TRIM16, and relative increased ratio of LC3B-II protein level in DLD-1 cells following 0.50 μM periplocin treatment at different time periods. Results are representative of three independent experiments. Data are presented as mean ± SD. *P < 0.05, **P < 0.01, ***P < 0.001. for LGALS3 degradation, we generated lysine to arginine mutants of LGALS3 at K196 or Lys210 (LGALS3 K196R or LGALS3 K210R ). As shown in Figure 6I, the ubiquitinconjugated level of LGALS3 K196R mutant was comparable to the wild type (WT), whereas K210 mutation significantly decreased LGALS3 ubiquitination. These results suggest that periplocin elevates LGALS3 level by preventing K210 ubiquitination and proteasomal degradation. In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3.

### [7] In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression
- Authors: A. Montero‐Calle, Á. López-Janeiro, Marta L. Mendes, Daniel Perez-Hernandez, Irene Echevarría et al.
- Year: 2023
- Venue: Cellular Oncology
- URL: https://www.semanticscholar.org/paper/92b64e01bcb30f7457ddb8cc4be26de8b0c7cf69
- DOI: 10.1007/s13402-023-00778-w
- PMID: 36745330
- PMCID: 10205863
- Citations: 19
- Summary: C1GALT1 stably depleted ECC-1 cells mimic an EC aggressive phenotype observed in patients and might be useful for the identification and validation of EC markers of progression.
- Evidence snippets:
  - Snippet 1 (score: 0.694)
    > Finally, since LGALS3 (Galectin-3) has been shown to interact with O-glycans in the mucosal epithelium [30], and considering its overexpression observed by proteomics and further confirmed by PCR and WB analyses upon depletion of C1GALT1, we focused on the role of LGALS3 in EC by IHC.
    > A total of 151 out of 178 cores from 79 EC patients were considered adequate for LGALS3 expression assessment by IHC. Morphologic assessment of LGALS3 IHC staining characteristics revealed different staining patterns (Fig. 5 A). Out of the 151 evaluable cores, 45 (29.8%) showed absent LGALS3 expression. LGALS3 positive samples showed variable and low intensity protein expression (mean positive tumor cells per sample = 35.4%). A small subset of cores (13/151, 8.6%) demonstrated diffuse (> 90% positive tumor cells per sample) staining. LGALS3 score varied across histologic types, with serous and undifferentiated tumors displaying the highest protein expression (median IHC LGALS3 score = 10, 20, 50 and 55 for endometrioid, clear cell, serous and undifferentiated tumor types, respectively) (Fig. 5B). Interestingly, the aggressive histologic variants (clear cell, serous and undifferentiated) showed higher LGALS3 IHC scores than endometrioid variants (p value < 0.001). In addition, LGALS3 expression positively correlated with tumor grade. High grade tumors (G3) displayed higher protein expression (median LGALS3 IHC score = 30) compared to low grade tumors (median LGALS3 IHC score for G1/G2 tumors = 10). This finding was independent of histologic type, as similar results were observed when analyzing endometrioid tumors.
    > Finally, we interrogated the correlation between the expression levels of LGALS3 and C1GALT1.

### [8] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
- Authors: Tammy R. Chaudoin, S. Bonasera
- Year: 2018
- Venue: BMC Neuroscience
- URL: https://www.semanticscholar.org/paper/26255eafb963932be62ecb55d4943930217cb63f
- DOI: 10.1186/s12868-018-0428-x
- PMID: 29716523
- PMCID: 5930520
- Citations: 7
- Influential citations: 1
- Summary: P perturbation of behavioral circadian rhythms in Lgals3−/− mice is noted, with mice at both ages demonstrating greater variability in day-to-day performance of feeding, drinking, and movement compared to wildtype.
- Evidence snippets:
  - Snippet 1 (score: 0.692)
    > atlases suggest that Lgals3 expression (at low-to-moderate levels) occurs in both pre-and post-natal brain, and has been localized to regions involved in motor behavior generation, including the cortex, striatum, cerebellum, and spinal cord. We thus argue that Lgals3 loss alters mouse motor function, either through its impact on motor development or through altered neuronal signaling in CNS regions that regulate or produce motor behavior. Further studies examining the consequences of Lgals3 loss at synaptic, neuronal, ensemble, and tissue levels of organization will be required to determine the precise mechanisms underlying this functional loss. Grey bands depict periods where mouse cohorts were tested in the home cage monitoring system. Note that neither axis begins at 0. Sampling interval for x-axis is 7 days except where noted by breakpoints
    > As mentioned earlier, Lgals3 has been implicated in a large number of physiological tasks at both a cellular and organwide level of organization. It is thus notable that mice with complete loss of Lgals3 function demonstrate relatively few behavioral differences when compared to wildtype C57BL/6J mice. This finding suggests that, at least in the mouse, there is some genetic redundancy regarding Lgals3 function. Studies of galectin evolution focusing on intron/exon organization as well as sequence identity suggest that duplication of ancestral galectin genes in animal lineages preceding the first teleost fish [62] provided the precursors for what has become a large vertebrate protein family [63]. There is also data suggesting that galectins may be able to substitute for one another in specific circumstances. For example, Lgals1 may compensate for Lgals3 loss at the spliceosome [64]. Extracellular Lgals1 also regulates T cell apoptosis in a manner similar to that of extracellular Lgals3 [65]. The behavioral phenotype arising from Lgals3 functional loss thus identifies neuronal loci and processes where there is no compensation for gene loss.

### [9] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
- Authors: Tammy R. Chaudoin, S. Bonasera
- Year: 2018
- Venue: BMC Neuroscience
- URL: https://www.semanticscholar.org/paper/613a09b176431cdca195e6b3c439b4edbe4f92af
- DOI: 10.1186/s12868-018-0428-x
- Summary: P perturbation of behavioral circadian rhythms in Lgals3−/− mice is noted, with mice at both ages demonstrating greater variability in day-to-day performance of feeding, drinking, and movement compared to wildtype.
- Evidence snippets:
  - Snippet 1 (score: 0.691)
    > atlases suggest that Lgals3 expression (at low-to-moderate levels) occurs in both pre-and post-natal brain, and has been localized to regions involved in motor behavior generation, including the cortex, striatum, cerebellum, and spinal cord. We thus argue that Lgals3 loss alters mouse motor function, either through its impact on motor development or through altered neuronal signaling in CNS regions that regulate or produce motor behavior. Further studies examining the consequences of Lgals3 loss at synaptic, neuronal, ensemble, and tissue levels of organization will be required to determine the precise mechanisms underlying this functional loss. Grey bands depict periods where mouse cohorts were tested in the home cage monitoring system. Note that neither axis begins at 0. Sampling interval for x-axis is 7 days except where noted by breakpoints
    > As mentioned earlier, Lgals3 has been implicated in a large number of physiological tasks at both a cellular and organwide level of organization. It is thus notable that mice with complete loss of Lgals3 function demonstrate relatively few behavioral differences when compared to wildtype C57BL/6J mice. This finding suggests that, at least in the mouse, there is some genetic redundancy regarding Lgals3 function. Studies of galectin evolution focusing on intron/exon organization as well as sequence identity suggest that duplication of ancestral galectin genes in animal lineages preceding the first teleost fish [62] provided the precursors for what has become a large vertebrate protein family [63]. There is also data suggesting that galectins may be able to substitute for one another in specific circumstances. For example, Lgals1 may compensate for Lgals3 loss at the spliceosome [64]. Extracellular Lgals1 also regulates T cell apoptosis in a manner similar to that of extracellular Lgals3 [65]. The behavioral phenotype arising from Lgals3 functional loss thus identifies neuronal loci and processes where there is no compensation for gene loss.

### [10] Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy
- Authors: Mi Guan, Yanping Ma, S. Shah, G. Romano
- Year: 2016
- Venue: Oncolytic Virotherapy
- URL: https://www.semanticscholar.org/paper/9f79d851e32ad25e83c0a2d64e12919bf81a89f8
- DOI: 10.2147/OV.S99856
- PMID: 27579295
- PMCID: 4996252
- Citations: 4
- Summary: This review focuses on the strategy of biomarkers for the production of novel TMN oncolytic therapeutics, which may improve the specificity of targeting of tumor cells and limit adverse effects in patients.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [11] SMURF1 controls the PPP3/calcineurin complex and TFEB at a regulatory node for lysosomal biogenesis
- Authors: Qin Xia, Hanfei Zheng, Yang Li, Wanting Xu, Chengwei Wu et al.
- Year: 2023
- Venue: Autophagy
- URL: https://www.semanticscholar.org/paper/7ab13fe72fa12a55aa9304ce52199d1494c8974a
- DOI: 10.1080/15548627.2023.2267413
- PMID: 37909662
- PMCID: 11062382
- Citations: 20
- Summary: This study showed that SMURF1 affected lysosomal biogenesis in response to lysosomal damage by preventing TFEB nuclear translocation, and determined that LLOMe-mediated TFEB nuclear import is dependent on SMURF1 under the condition of MTORC1 inhibition.
- Evidence snippets:
  - Snippet 1 (score: 0.685)
    > Immunofluorescence assay showed that PPP3R1 was also recruited to lysosomes upon LLOMe treatment in a LGALS3-dependent manner (Figure S4A).To identify the role of PPP3R1 in the formation of complex, as expected, we first found that PPP3CB directly binds with PPP3R1 in a LLOMe-enhanced manner (Figure 6A, B).Considering that PPP3CB was directly associated with LGALS3, we also checked the interaction between PPP3R1 and LGALS3.The results showed that PPP3R1 indirectly binds with LGALS3 (Figure 6C).Similarly, LLOMe treatment also promoted the binding affinity between PPP3R1 and LGALS3 (Figure 6D).We next mapped the key interaction domain of LGALS3 with PPP3R1, and showed the NT domain of LGALS3 was essential for the association with PPP3R1 (Figure 6E, F).Furthermore, overexpression of PPP3CB increased, suppression of PPP3CB abolished, the interactions of PPP3R1 and LGALS3 (Figure 6G, H), suggesting PPP3CB is also the bridge for the interaction between LGALS3 and PPP3R1.Interestingly, we also detected that SMURF1 indirectly interacted with PPP3R1, but not MCOLN1, in a LLOMe-enhanced manner (Figure S4B-E).Given that both SMURF1 and PPP3R1 were indirectly bound with the NT domain of LGALS3, we asked whether SMURF1 affected the interactions between PPP3R1 and LGALS3.Our data indicated that suppression of SMURF1 decreased, overexpression of SMURF1 increased, the interactions of PPP3R1 and LGALS3 (Figure 6I, J), suggesting SMURF1 promotes the recruitment of PPP3R1 by LGALS3.We next mapped the key HECT domain of SMURF1 which was essential for interaction with PPP3R1 (Figure 6K, L).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.