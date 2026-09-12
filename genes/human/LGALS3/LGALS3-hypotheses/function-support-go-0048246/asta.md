---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:47:13.080695'
end_time: '2026-06-22T04:47:16.130840'
duration_seconds: 3.05
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0048246
  hypothesis_text: LGALS3 has macrophage chemotaxis (GO:0048246).
  term_context: '- Term: macrophage chemotaxis (GO:0048246)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[13]
  source_context_yaml: "term:\n  id: GO:0048246\n  label: macrophage chemotaxis\n\
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

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has macrophage chemotaxis (GO:0048246).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has macrophage chemotaxis (GO:0048246).
Key context:
- Term: macrophage chemotaxis (GO:0048246)
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
- **Hypothesis slug:** function-support-go-0048246
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[13]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0048246
  label: macrophage chemotaxis
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has macrophage chemotaxis (GO:0048246). Gene/protein: LGALS3. O...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 11
- Snippets retrieved: 20

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
  - Snippet 1 (score: 0.980)
    > To delineate the driving mechanism of LGALS3 for the malignant progression of HCC, the KEGG and GO analysis was conducted.The volcano plot and heatmap showed significantly differentially expressed genes between LGALS3 high-and low-expression groups (Figure S3A-B).The KEGG pathway analysis revealed that these LGALS3-related genes were enriched in the IL-17 signaling pathway, ECM-receptor interaction pathway, central carbon metabolism in cancer pathway, leukocyte transendothelial migration pathway and PI3K-Akt signaling pathway.Meanwhile, the GO analysis revealed that these genes were strongly associated with cell chemotaxis, leukocyte chemotaxis, regulation of leukocyte migration, as well as regulation of chemotaxis (Fig. 5A).Accumulating evidence has proven the immune system has an essential role in malignancy pathogenesis [17], and LGALS3 is closely correlated with CD163 + tumor-associated macrophages (TAM) in glioma [10].Therefore, we studied the association between LGALS3 level and the immune infiltration level in HCC.There was no statistical difference in immune cell infiltration levels over a number of LGALS3 copy numbers (Fig. 5B).Meanwhile, immune infiltration analysis revealed that expression of LGALS3 showed a significant positive association with several immune cell populations, involving CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, dendritic cell, as well as cancer-associated fibroblasts (CAFs) within HCC (Fig. 5C-E).Based on these results, we further evaluated the immune score in HCC patients with high and low LGALS3 expression.The scores of immune cells, including CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, and dendritic cell, were significantly higher in the high LGALS3 expression groups, as shown in Fig. 5F.Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].
  - Snippet 2 (score: 0.947)
    > Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].According to Table S1, the expression of LGALS3 was statistically positively correlated with several chemokines of immune cells, involving monocytes/macrophages (CCL2, CCL3, CCL5, CCL7, CCL13, CCL17, and CCL22), T lymphocytes (CCL2, CCL1, CCL17, and CCL22), eosinophils (CCL11, CCL26, CCL5, CCL7, CCL13, and CCL3), mast cells (CCR1, CCR2, CCR3, CCR4, CCR5, CXCR2, and CXCR4), and neutrophils (CXCL8).Taken together, these outcomes indicate that LGALS3 is positively associated with immune cell infiltration and cell chemotaxis and could have a crucial function in HCC tumor immune microenvironment.
    > LGALS3 expression correlation and immune cell biomarkers in HCC Next, we wanted to investigate the LGALS3 function in HCC tumor immunity further.Utilizing GEPIA databases, we studied the correlation between LGALS3 expression and immune cell biomarkers within HCC.
  - Snippet 3 (score: 0.814)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly
  - Snippet 4 (score: 0.809)
    > analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly higher immune cell scores and immune checkpoint expression levels. Finally, GSVA analysis was performed to predict potential signaling pathways linked to LGALS3 and HCP5 in immune evasion and metabolic reprogramming of HCC. Our findings indicated that the upregulation of LGALS3 via the HCP5/hsa-miR-27b-3p axis is associated with unfavorable prognosis and increased tumor immune infiltration in HCC.
  - Snippet 5 (score: 0.792)
    > Zhang et al. [14] suggested overexpression of LGALS3 promoted HCC bone metastasis and induced associated skeletal complications.Nevertheless, the expression, prognosis, epigenetic, and molecular regulatory mechanisms of LGALS3 in HCC have been incompletely studied.In addition, LGALS3 relation with immune infiltration in HCC TME has yet to be inadequately investigated.
    > This work began with a pan-cancer study of LGALS3 expression and its predictive value in a variety of human malignancies.We further explored the LGALS3 potential upstream regulatory noncoding RNAs (ncRNAs) involving microRNAs (miRNAs) as well as long noncoding RNAs (lncRNAs) throughout HCC.Subsequently, in HCC, a correlation analysis was investigated between LGALS3 and tumor immunity-related indicators involving cell chemotaxis, immune checkpoints, immune cell biomarkers, and infiltration.Eventually, the association between the expression of LGALS3 and signaling pathways was examined in HCC.Findings demonstrated that LGALS3 might have a role in the malignancy of HCC and immune cell infiltration via the HCP5/hsa-miR-27b-3p/ LGALS3 axis, suggesting that a novel HCP5/hsa-miR-27b-3p/LGALS3 axis could be a biomarker for prognosis and treatment target for HCC patients.
  - Snippet 6 (score: 0.766)
    > Utilizing GEPIA databases, we studied the correlation between LGALS3 expression and immune cell biomarkers within HCC.Table S2 lists that LGALS3 demonstrated a significant positive association with various immune cell biomarkers, including B cell (CD19 and CD79A), CD4 + T cell (CD4), CD8 + T cell (CD8A and CD8B), neutrophil (ITGAM and CCR7), M1 macrophage (NOS2, IRF5, and PTGS2), M2 macrophage (CD163, VSIG4, and MS4A4A), dendritic cell (HLA-DPB1, HLA-DQB1, HLA-DRA, HLA-DPA1, CD1C, NRP1, and ITGAX) and CAFs (FAP, ACTA2, S100A4, PDPN, PDGFR, and CD70) in HCC.
    > Our results indicate that LGALS3 has a significant positive connection to the immune infiltration within HCC, especially CAFs.

### [2] LGALS3 Is a Poor Prognostic Factor in Diffusely Infiltrating Gliomas and Is Closely Correlated With CD163+ Tumor-Associated Macrophages
- Authors: Wan-Ming Hu, Yuan-Zhong Yang, Tian Zhang, Changling Qin, Xuenong Li
- Year: 2020
- Venue: Frontiers in Medicine
- URL: https://www.semanticscholar.org/paper/53b083f91a08aefebb5f9edaaa95625e2dc98f2b
- DOI: 10.3389/fmed.2020.00182
- PMID: 32528967
- PMCID: 7254797
- Citations: 18
- Influential citations: 1
- Summary: LGALS3 was an independent poor prognostic marker in diffusely infiltrating gliomas and was positively correlated with immune cell infiltration, particularly CD163+ tumor-associated macrophages in the TCGA dataset, Rembrandt dataset, and the SYSUCC cohort.
- Evidence snippets:
  - Snippet 1 (score: 0.856)
    > This may explain why LGALS3 positive glioma patients have a significantly shorter OS than LGALS3 negative patients, suggesting that LGALS3 may play a role in malignant progression in glioma through changing the immune microenvironment in glioma. Some studies have also confirmed that LGALS3 played a key role in glioma development through increasing cell motility and invasion (21,22). Vladimirova et al. (23) found that LGALS3 expression was mediated by Runx-2 transcription factors, which contributed to the malignant progression of glial tumors. Conversely, only Gordower et al. (24) reported that LGALS3 expression decreased as the WHO level increased in astrocytic tumors. We think the reason for this difference may be partially due to the small number of patient samples in their study. Moreover, online database analysis also verified our results. Patients with high expression of LGALS3 mRNA had a poor prognosis.
    > LGALS3 was closely related to IDH status, CD163+ TAMs and was mainly expressed in IDH wild-type glioma. It is worth noting that LGALS3 mRNA was highly expressed in the mesenchymal subtype, a more malignant TCGA GBM subtype with a higher tendency for recurrence, metastasis, and increased vascularity.
    > Most importantly, we found that LGALS3 was involved in the regulation of the glioma immune microenvironment, particularly CD163+ TAMs. There is growing evidence that complex tumor microenvironments contribute to the malignant progression of gliomas (25,26). Among the components of the tumor microenvironment, tumor-associated macrophages (TAMs) are considered to provide important support for tumor growth. Macrophages are divided into M1 and M2 subtypes according to their functions. Typically, CD68 is a general marker for macrophages, while CD163 is considered to be a highly specific marker for M2 type macrophages.
  - Snippet 2 (score: 0.791)
    > Background: Glioma, the most common brain tumor, is a heterogeneous group of glia-derived tumors, the majority of which have characteristics of diffuse infiltration and immunosuppression. The LGALS protein family is a large class of sugar-binding proteins. Among them, LGALS3 has been reported to promote tumor development and progression in some cancers. However, the clinical significance and biological functions of LGALS3 in glioma remain virtually unknown. The purpose of our research is to detect LGALS3 expression and its prognostic value in glioma and reveal the relationship between its expression and the clinico/molecular-pathological features of patients and immune cell infiltration. Methods: LGALS3 protein expression was examined by immunohistochemistry. The mRNA expression data of LGALS3 was downloaded and analyzed from TCGA and Rembrandt datasets. The association between LGALS3 and glioma clinically relevant diagnostic/molecular markers (IDH, 1p19q, ATRX, MGMT, and TERT) was examined using the Chi-Squared (χ2) test. The correlation between LGALS3 expression and the infiltration of multiple intra-tumoral immune cell types, including B cells (CD20), T cells (CD4 and CD8), macrophages (CD68), and M2 tumor-associated macrophages (CD163), was evaluated by Spearman correlation analysis. Kaplan-Meier analysis and the Cox regression analysis were applied to evaluate the prognostic value of LGALS3 in glioma. The log-rank test was used to evaluate Kaplan-Meier results for significance. Results: Out of all 304 glioma cases, LGALS3 protein was expressed in 125 glioma cases (41.1%, 125/304), with 69.2% (9/13) in WHO I, 9.8% (8/82) in WHO II, 34.2% (26/76) in WHO III, and 61.7% (82/133) in WHO IV. The expression of LGALS3 was correlated with patient age, WHO grade, PHH3 (mitosis), Ki67 index,
  - Snippet 3 (score: 0.782)
    > Spearman correlation analysis revealed that CD20+ B cells were not correlated with LGALS3 expression (Figure 3F), but significant positive correlations were found between the infiltration of CD4+ T cells (Figure 3G), CD8+ T cells (Figure 3H), CD68+ macrophages (Figure 3I), CD163+ TAMs (Figure 3J), and the expression of LGALS3. In addition, the number of CD163+ TAMs infiltration was strongly correlated with LGALS3 (R = 0.724) in our cohort (Figure 3J).
  - Snippet 4 (score: 0.774)
    > Typically, CD68 is a general marker for macrophages, while CD163 is considered to be a highly specific marker for M2 type macrophages. CD68+ macrophages are usually activated during antigen presentation and inflammatory responses, while CD163+ macrophages have a large number of anti-inflammatory cytokines that contribute to immunosuppression and promote tumor development. Multiple studies have shown that TAMs can actively suppress adaptive immunity, promote tumor growth, and angiogenesis, and are very similar to M2 macrophages (27,28). A previous study (29) confirmed that CD163+ TAMs played an important role in the biological process of glioma and that high expression of CD163 predicted poor prognosis in glioma patients. Another study suggested that the expression level of LGALS3 might affect macrophage infiltration in brain tumors (30), but only 16 GBM samples were used in their study. In the present study, we investigated the relationship between LGALS3 and TAMs in a large sample (304 glioma cases including 133 cases of GBM). We found that CD163+ TAMs were abundant in glioma, particularly in GBM and that LGALS3 was strongly correlated with the number of TAMs. GO and KEGG analyses also revealed that LGALS3 was involved in important inflammation and immune pathways, including cytokine signaling, NF-kappa B, NOD receptor, and the TNF signaling pathway. These results indicated that LGALS3 was involved in inflammatory and immune responses, which further contributed to malignant progression and shorter survival in glioma patients. However, the mechanism by which LGALS3 affects the glioma immune microenvironment and the exact pathways associated with LGALS3 in glioma need to be further explored in future studies.
    > In conclusion, we have shown that LGALS3 is a novel biomarker that is highly expressed in pilocytic astrocytoma, GBM, and IDH wild-type LGG. LGALS3 is associated with poor prognosis in diffusely infiltrating glioma and served as an important prognostic biomarker in LGG and GBM.

### [3] Morphological and transcriptional insights into the role of histone phosphorylation-related genes in early development of the chicken duodenum
- Authors: Xiaofeng Li, Bing Yang
- Year: 2025
- Venue: Animal Bioscience
- URL: https://www.semanticscholar.org/paper/b3da4d3a37ec0fae40140d0cf95db98d90b41079
- DOI: 10.5713/ab.25.0108
- PMID: 40506039
- PMCID: 12580959
- Citations: 1
- Summary: A novel paradigm wherein histone phosphorylation coordinates intestinal morphogenesis is established, providing mechanistic insights for optimizing poultry intestinal health and nutritional strategies.
- Evidence snippets:
  - Snippet 1 (score: 0.838)
    > Notably, as broilers age (from D0 to D7), the intestinal VH increases accordingly, indicating a positive balance between intestinal cell proliferation and apoptosis (i.e., cell proliferation predominates over apoptosis). Through transcriptional network analysis, we identified eight histone phosphorylation-associated hub genes (LGALS3, ITGB2, IRF7, SOCS3, CSF1R, KIF23, SMC2, and DLGAP5) that mechanistically link epigenetic regulation to developmental programming.
    > LGALS3 (galectin-3) plays critical roles in macrophage chemotaxis, mucosal barrier maintenance, intestinal epithelial cell (IEC) apoptosis regulation, and inflammatory responses [21][22][23]. Our study revealed a 6.59-fold increase in LGALS3 gene expression in the duodenum at D7 compared to D0 (Supplement 6), with functional analysis confirming its involvement in macrophage chemotaxis (Supplement 7). These findings align with Sun et al [21], who reported that LGALS3 silencing in necrotizing enterocolitis models inhibited the TLR4/NF-κB pathway, subsequently reducing IEC apoptosis and inflammation [21]. Emerging evidence further suggests LGALS3' s protective functions through ER stress modulation, autophagy regulation, and inflammasome control in intestinal Behçet' s disease [22], along with its capacity to upregulate key mucosal barrier components (MUC2, Occludin, and ZO-1) [23]. Collectively, these observations suggest LGALS3 promotes duodenal development through: 1) mucosal barrier reinforcement via tight junction protein upregulation, 2) inflammatory control through TLR4/NF-κB-mediated macrophage regulation, and 3) cellular homeostasis maintenance via ER stress/autophagy pathways.

### [4] Phenotypic Switching of Vascular Smooth Muscle Cells in Atherosclerosis
- Authors: Runji Chen, D. McVey, D. Shen, Xiaoxin Huang, Shu Ye
- Year: 2023
- Venue: Journal of the American Heart Association: Cardiovascular and Cerebrovascular Disease
- URL: https://www.semanticscholar.org/paper/472c313e2214a97757712ab0a8b39b133bd6a6bc
- DOI: 10.1161/JAHA.123.031121
- PMID: 37815057
- PMCID: 10757534
- Citations: 133
- Influential citations: 2
- Summary: This review article discusses the 9 VSMC phenotypes that have been reported in atherosclerotic lesions and classifies them into differentiated VSMCs, intermediately dedifferentiated VSMCs, and dedifferentiated VSMCs.
- Evidence snippets:
  - Snippet 1 (score: 0.835)
    > Lgals3 (also referred to as galectin-3) is considered a marker of macrophage-like cells. 13,31 Rong et al detected a population of VSMCs that expressed Lgals3 following cholesterol loading in vitro. 31 Recently, Alencar et al found that Lgals3 activation is not a specific marker of the differentiation of VSMCs to a macrophage-like state but rather it is a marker of VSMCs entering a transitional state, with increased expression of genes associated with stem cells that are capable of extracellular matrix remodeling. 16 Of note, similar to SEM-like cells, Lgals3 + cells also have increased expression of lymphocyte antigen 6 family member A and vascular cell adhesion molecule 1. Further studies to investigate if SEM-like cells are derived from Lgals3 + cells are warranted.
    > Using mouse, rat, and human models of cholesterolloading in VSMCs, Li et al found that SREBP1 (sterol regulatory-element binding protein-1) and Krüppel-like factor-15 induced up-and downregulation of Lgals3, respectively, via binding to the Lgals3 gene promoter (albeit at different sites). 45 Likewise, Lgals3 promoted SREBP1 gene expression, producing a feedforward loop upregulated by cholesterol loading. 45 Moreover, Lgals3 and SREBP1 downregulated myocardin-related transcription factor A expression in VSMCs. 45 In another study, Owsiany et al used a dual lineage tracing model and found that Lgals3 + VSMCs produce monocyte chemoattractant protein 1, a proinflammatory chemokine. 15 Knockout of monocyte chemoattractant protein 1 specifically in Lgals3 + VSMCs resulted in the formation of atherosclerotic lesions with a greater ACTA2 content in the fibrous cap and decreased Lgals3 + cell content, a feature of stable plaque. 15

### [5] Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins
- Authors: S. Blois, G. Dveksler, G. Vasta, N. Freitag, V. Blanchard et al.
- Year: 2019
- Venue: Frontiers in Immunology
- URL: https://www.semanticscholar.org/paper/68fad2b87411701fa708a1f49f8b918370486857
- DOI: 10.3389/fimmu.2019.01166
- PMID: 31231368
- PMCID: 6558399
- Citations: 56
- Influential citations: 7
- Summary: The relevance of galectin-glycan interactions as potential therapeutic targets in pregnancy disorders is discussed and the importance of angiogenesis during decidualization and in placenta formation is discussed.
- Evidence snippets:
  - Snippet 1 (score: 0.794)
    > Lgals3 has been implicated in the regulation of innate and adaptive immune responses, where it participates in the activation or differentiation of immune cells and contributes to phagocytic clearance of microorganisms and apoptotic cells by macrophages (117,118). Lgals3 has been reported to promote but also to inhibit T-cell apoptosis depending on whether it binds to glycoproteins on the cell surface (CD45 and CD71) or to intracellular ligands (Bcl-2) (119, 120). In the placenta, Lgals3 was detected in all trophoblastic lineages including villous cytotrophoblasts (CTB) and EVT with a reduction of Lgals3 expression observed from the VT to the trophoblastic cell columns (121). This pattern of Lgals3 expression correlates with the switch from a proliferative to a migratory trophoblast phenotype and while placental Lgals3 dysregulation has been associated with some obstetric complications including spontaneous or recurrent miscarriages, further studies are needed to understand its contribution to trophoblast biology (81,122). In addition to trophoblasts, Lgals3 is expressed by maternal decidual cells (73). While showing a different expression pattern, both Lgals1 and Lgals3 have been proposed to play a role in cell-cell and cell-matrix interactions of trophoblast during placentation (121). Studies of the importance of Lgals3 in murine pregnancy by Yang et al. indicate that Lgals3 is expressed in the luminal and glandular epithelium and that an increase in Lgals3 is required for proper embryo implantation (123). In addition, Lgals3 affects chemotaxis and morphology of endothelial cells and stimulates capillary tube formation and angiogenesis in vivo (124). Therefore, besides its proposed roles in embryo implantation, immune regulation and trophoblast-matrix interactions, Lgals3 has a potential role in placental angiogenesis.

### [6] Secreted Factors and EV-miRNAs Orchestrate the Healing Capacity of Adipose Mesenchymal Stem Cells for the Treatment of Knee Osteoarthritis
- Authors: E. Ragni, C. Perucca Orfei, P. De Luca, A. Colombini, M. Viganò et al.
- Year: 2020
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/7d8d9d140ae309da10710f17dc979236a67fb966
- DOI: 10.3390/ijms21051582
- PMID: 32111031
- PMCID: 7084308
- Citations: 67
- Influential citations: 1
- Summary: Light is shed about the way ASCs regulate cell homeostasis and regenerative pathways in an OA-resembling environment, therefore suggesting a rationale for the use of MSC-enriched clinical products, such as stromal vascular fraction and microfragmented adipose tissue, in joint pathologies.
- Evidence snippets:
  - Snippet 1 (score: 0.788)
    > 903, seven) and regulation of protein secretion (GO:0050708, 19) and, for the (ii) response to stimulus cascade-inflammatory response (GO:0006954, 31). Further, due to the reported role of ASCs in modulating synovial macrophages, the inflammatory response list was sifted through a Panther algorithm to identify specific and macrophage-related GO terms. A few terms emerged: macrophage chemotaxis (GO:0048246, two factors) and migration (GO:1905517), both defined by CCL3 and CCL5; the positive regulation of macrophage differentiation (GO:0045651) and regulation of macrophage differentiation (GO:0045649), both defined by CSF1 and TGFB1; the positive regulation of macrophage chemotaxis (GO:0010759, CCL5 and CSF1) and regulation of macrophage chemotaxis (GO:0010758, CSF1, CCL5 and MIF) and the positive regulation of macrophage activation (GO:0043032, CCL3 and IL13) and regulation of macrophage activation (GO:0043030, CCL3, IL13 and MIF). Eventually, to have a comprehensive overview of the entire dataset, in the inflammatory response terms, nine proteins of the > 10 ng group also fell (CCL2, CXCL10, CXCL5, EGFR, ICAM1, IGFBP4, IL6, TIMP1 and TNFRSF1A). CCL2 belonged to macrophage chemotaxis, LIF to the regulation of macrophage differentiation and IL1RL1 and IL6 to macrophage activation. Related to macrophages and their ability to migrate, monocyte chemotaxis (GO:0002548, IL6 and CCL2) emerged. Interestingly, other GO terms related with motility were identified, like leukocyte chemotaxis (GO:0030595, IL6, CCL2, CXCL5 and CXCL10); lymphoc

### [7] Macrophage-derived Spp1 promotes intramuscular fat in dystrophic muscle
- Authors: Philip K Farahat, Chino Kumagai-Cresse, Raquel L. Aragón, Feiyang Ma, Justin K. Amakor et al.
- Year: 2025
- Venue: JCI Insight
- URL: https://www.semanticscholar.org/paper/25c265aed44730ce4b23491cd7ac24d8c3fcf94b
- DOI: 10.1172/jci.insight.181946
- PMID: 40626359
- PMCID: 12288893
- Citations: 7
- Summary: A role for myeloid-derived Spp1 in the differentiation of stromal cells towards an adipogenic fate, leading to accumulation of intramuscular fat in dystrophic muscles is suggested.
- Evidence snippets:
  - Snippet 1 (score: 0.786)
    > Lgals3 clusters 2 and 3 expressed the highest Spp1. All Spp1-expressing clusters showed a drastic reduction in Spp1 in the cKO (Figure 2B, compare blue and green) (8). Lgals3-2 cells also expressed Arg1 while Lgals3-3 expressed Igf1 (11). The proportion of different monocyte/macrophage subtypes was evaluated in the 2 genotypes (Figure 2, C and D). While the proportion of Lgals3-3 and Lgals3-2 remained similar in the 2 genotypes, a mild increase in Lgals3-1 was observed in the cKO, while both monocyte subclusters slightly decreased in the cKO (Figure 2C). Although the overall number of macrophages increased in the cKO (mdx:969 vs cKO 4,028), cKO macrophages did not show large changes in the cellular frequency of subtypes (Figure 2D). Inflammatory genes were either unchanged or slightly reduced in the cKO, including the chemokines Ccl3 and Ccl4 (Figure 2F) and Tgfb1 (Supplemental Figure 2B). However, IFN genes such as Ifi207, Ifi204, and Isg15 were slightly increased in cKO monocytes (Figure 2F).

### [8] Macrophages secrete murinoglobulin-1 and galectin-3 to regulate neutrophil degranulation after myocardial infarction
- Authors: Upendra Chalise, M. Daseke, William J. Kalusche, Shelby R. Konfrst, Jocelyn R. Rodriguez-Paar et al.
- Year: 2022
- Venue: Molecular Omics
- URL: https://www.semanticscholar.org/paper/446873a6222f1a5c4299cb80c95f7f9ff792e9f8
- DOI: 10.1039/d1mo00519g
- PMID: 35230372
- PMCID: 8963000
- Citations: 18
- Summary: In conclusion, macrophages at MI day 1 secrete MUG1 to limit and Lgals3 to accentuate neutrophil degranulation to regulate infarct wall thinning.
- Evidence snippets:
  - Snippet 1 (score: 0.765)
    > Inflammation presides early after myocardial infarction (MI) as a key event in cardiac wound healing. Ischemic cardiomyocytes secrete inflammatory cues to stimulate infiltration of leukocytes, predominantly macrophages and neutrophils. Infiltrating neutrophils degranulate to release a series of proteases including matrix metalloproteinase (MMP)-9 to break down extracellular matrix and remove necrotic myocytes to create space for the infarct scar to form. While neutrophil to macrophage communication has been explored, the reverse has been understudied. We used a proteomics approach to catalogue the macrophage secretome at MI day 1. Murinoglobulin-1 (MUG1) was the highest-ranked secreted protein (4.1-fold upregulated at MI day 1 vs. day 0 pre-MI cardiac macrophages, p = 0.004). By transcriptomics evaluation, galectin-3 (Lgals3) was 2.2-fold upregulated (p = 0.008) in MI day 1 macrophages. We explored the direct roles of MUG1 and Lgals3 on neutrophil degranulation. MUG1 blunted while Lgals3 amplified neutrophil degranulation in response to phorbol 12-myristate 13-acetate or interleukin-1β, as measured by MMP-9 secretion. Lgals3 itself also stimulated MMP-9 secretion. To determine if MUG1 regulated Lgals3, we co-stimulated neutrophils with MUG1 and Lgals3. MUG1 limited degranulation stimulated by Lgals3 by 64% (p < 0.001). In vivo, MUG1 was elevated in the infarct region at MI days 1 and 3, while Lgals3 increased at MI day 7. The ratio of MUG1 to Lgals3 positively correlated with infarct wall thickness, revealing that MUG1 attenuated infarct wall thinning. In conclusion, macrophages at MI day 1 secrete MUG1 to limit and Lgals
  - Snippet 2 (score: 0.755)
    > while Lgals3 increased at MI day 7. The ratio of MUG1 to Lgals3 positively correlated with infarct wall thickness, revealing that MUG1 attenuated infarct wall thinning. In conclusion, macrophages at MI day 1 secrete MUG1 to limit and Lgals3 to accentuate neutrophil degranulation to regulate infarct wall thinning.

### [9] Galectin-3, histone deacetylases, and Hedgehog signaling: Possible convergent targets in schistosomiasis-induced liver fibrosis
- Authors: F. L. de Oliveira, Katia Carneiro, J. Brito, M. Cabanel, J. X. Pereira et al.
- Year: 2017
- Venue: PLoS Neglected Tropical Diseases
- URL: https://www.semanticscholar.org/paper/6dc6d6f3529841361a1ccf76eac911be181636c7
- DOI: 10.1371/journal.pntd.0005137
- PMID: 28231240
- PMCID: 5322873
- Citations: 31
- Summary: A possible involvement of Galectin-3 (Gal-3), histone deacetylases (HDACs), and Hedgehog (Hh) signaling with macrophage activation during Th1/Th2 immune responses, fibrogranuloma reaction, and tissue repair during schistosomiasis is suggested.
- Evidence snippets:
  - Snippet 1 (score: 0.756)
    > Indeed, considering that the first step of the infection is under the control of a macrophage, the outcome of the disease needs to be further investigated, including in the Lgals3-/-infected mice. The downmodulation of macrophages in Lgals3-/-infected mice during the first step of the infection could be directly associated with a type of fibrogranulomatous reaction in the liver and, consequently, drive profibrotic events during schistosomiasis.

### [10] Galectin-3 Identifies a Subset of Macrophages With a Potential Beneficial Role in Atherosclerosis
- Authors: K. Di Gregoli, M. Somerville, Rosaria Bianco, Anita C. Thomas, Aleksandra Frankow et al.
- Year: 2020
- Venue: Arteriosclerosis, Thrombosis, and Vascular Biology
- URL: https://www.semanticscholar.org/paper/7cc49f01469f15e073d249c35f5b1deb45262ade
- DOI: 10.1161/ATVBAHA.120.314252
- PMID: 32295421
- PMCID: 7253188
- Citations: 79
- Summary: A prominent protective role is revealed for galectin-3 in regulating macrophage polarization and invasive capacity and, therefore, delaying plaque progression.
- Evidence snippets:
  - Snippet 1 (score: 0.749)
    > Macrophage buildup within atherosclerotic lesions is at least, in part, due to enhanced monocyte/macrophage recruitment and is associated with the progression of plaques. 35 As macrophage (CD68-positive cells) content was increased within plaques of galectin-3 mice, we assessed galectin-3 modulation on macrophage accumulation in vitro and in vivo, as a surrogate indicator of steady-state invasion. The in vitro invasive capacity of macrophages from Lgals3 −/− mice was significantly increased in comparison to cells from Lgals3 +/+ wild-type mice (2.2-fold increase; P<0.001; Figure 3A). Conversely, the number of invading Lgals3 −/− macrophages was diminished through addition of exogenous recombinant galectin-3 compared with untreated cells (69%; P<0.001; Figure 3B). Furthermore, and consistent with our in vitro data, the number of macrophages recruited and accrued within implanted Matrigel-infused sponges was significantly increased within Lgals3 −/− mice in comparison to Lgals3 +/+ animals (1.6-fold increase; P<0.001; Figure 3C). These data support a key role for galectin-3 in retarding macrophage invasive capacity and may explain the observed increase in (CD68 positive) macrophage numbers within brachiocephalic plaques of Lgals 3 −/− :Apoe −/− mice.

### [11] Physical Activity Attenuates the Obesity-Induced Dysregulated Expression of Brown Adipokines in Murine Interscapular Brown Adipose Tissue
- Authors: T. Sakurai, Toshiyuki Fukutomi, Sachiko Yamamoto, Eriko Nozaki, T. Kizaki
- Year: 2021
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/c62f909c1038a72ef7c427bfa9914983c22b5422
- DOI: 10.3390/ijms221910391
- PMID: 34638731
- PMCID: 8508858
- Citations: 2
- Summary: Results indicate that PA attenuates the obesity-induced dysregulated expression of brown adipokines and suggests that Lgals3 and Lgal3bp are involved in brown adipocyte differentiation.
- Evidence snippets:
  - Snippet 1 (score: 0.748)
    > In the present study, we identified humoral factors from HB2 brown adipocytes similar to those reported by Villarroya et al. [30] using murine brown preadipocytes in BAT. Among these humoral factors, Ccl9, Lgals3, and Lgals3bp were found to be brown adipokines with gene expressions that were largely influenced by obesity and PA. Ccl9, which is also known as macrophage inflammatory protein 1-γ, is a chemokine belonging to the CC chemokine family [45] and is known to play an important role in anti-leukemia and bone resorption procedures. Although there are very few reports of the effect of Ccl9 on adipocytes, it is known to inhibit the differentiation of white adipocytes [46].
    > The Lgals3 protein (galectin-3) is involved in biological processes such as cell adhesion, inflammation, and apoptosis. Lgals3 is upregulated in the WAT and the BAT of obese mice and can attenuate insulin signaling in white adipocytes [41]. Furthermore, obese and diabetic individuals were shown to have higher blood levels of the Lgals3 protein, which parallels the deterioration of glucose homeostasis and suggests that Lgals3 may be involved in the development of obesity and type 2 diabetes [41]. In addition, studies using Lgals3 KO mice reported decreases in body and fat masses in HFD-fed Lgals3 KO mice by comparison with control mice [47]. However, another study using Lgals3 KO mice demonstrated that Lgals3 deficiency accelerates adiposity, levels of adipose tissue, and systemic inflammation associated with altered glucose homeostasis [48,49]. Additionally, Lgals3 is known to stimulate the differentiation of preadipocytes into mature white adipocytes in vitro [47]. On the other hand, human Lgals3bp has long been regarded as an important clinical tumor biomarker associated with disease diagnosis, negative prognosis, and poor response to therapy [50].

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.