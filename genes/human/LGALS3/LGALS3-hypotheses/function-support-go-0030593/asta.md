---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:46:42.923885'
end_time: '2026-06-22T04:46:46.109519'
duration_seconds: 3.19
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0030593
  hypothesis_text: LGALS3 has neutrophil chemotaxis (GO:0030593).
  term_context: '- Term: neutrophil chemotaxis (GO:0030593)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[9]
  source_context_yaml: "term:\n  id: GO:0030593\n  label: neutrophil chemotaxis\n\
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

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has neutrophil chemotaxis (GO:0030593).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has neutrophil chemotaxis (GO:0030593).
Key context:
- Term: neutrophil chemotaxis (GO:0030593)
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
- **Hypothesis slug:** function-support-go-0030593
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[9]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0030593
  label: neutrophil chemotaxis
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has neutrophil chemotaxis (GO:0030593). Gene/protein: LGALS3. O...

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
  - Snippet 1 (score: 0.929)
    > To delineate the driving mechanism of LGALS3 for the malignant progression of HCC, the KEGG and GO analysis was conducted.The volcano plot and heatmap showed significantly differentially expressed genes between LGALS3 high-and low-expression groups (Figure S3A-B).The KEGG pathway analysis revealed that these LGALS3-related genes were enriched in the IL-17 signaling pathway, ECM-receptor interaction pathway, central carbon metabolism in cancer pathway, leukocyte transendothelial migration pathway and PI3K-Akt signaling pathway.Meanwhile, the GO analysis revealed that these genes were strongly associated with cell chemotaxis, leukocyte chemotaxis, regulation of leukocyte migration, as well as regulation of chemotaxis (Fig. 5A).Accumulating evidence has proven the immune system has an essential role in malignancy pathogenesis [17], and LGALS3 is closely correlated with CD163 + tumor-associated macrophages (TAM) in glioma [10].Therefore, we studied the association between LGALS3 level and the immune infiltration level in HCC.There was no statistical difference in immune cell infiltration levels over a number of LGALS3 copy numbers (Fig. 5B).Meanwhile, immune infiltration analysis revealed that expression of LGALS3 showed a significant positive association with several immune cell populations, involving CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, dendritic cell, as well as cancer-associated fibroblasts (CAFs) within HCC (Fig. 5C-E).Based on these results, we further evaluated the immune score in HCC patients with high and low LGALS3 expression.The scores of immune cells, including CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, and dendritic cell, were significantly higher in the high LGALS3 expression groups, as shown in Fig. 5F.Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].
  - Snippet 2 (score: 0.910)
    > Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].According to Table S1, the expression of LGALS3 was statistically positively correlated with several chemokines of immune cells, involving monocytes/macrophages (CCL2, CCL3, CCL5, CCL7, CCL13, CCL17, and CCL22), T lymphocytes (CCL2, CCL1, CCL17, and CCL22), eosinophils (CCL11, CCL26, CCL5, CCL7, CCL13, and CCL3), mast cells (CCR1, CCR2, CCR3, CCR4, CCR5, CXCR2, and CXCR4), and neutrophils (CXCL8).Taken together, these outcomes indicate that LGALS3 is positively associated with immune cell infiltration and cell chemotaxis and could have a crucial function in HCC tumor immune microenvironment.
    > LGALS3 expression correlation and immune cell biomarkers in HCC Next, we wanted to investigate the LGALS3 function in HCC tumor immunity further.Utilizing GEPIA databases, we studied the correlation between LGALS3 expression and immune cell biomarkers within HCC.
  - Snippet 3 (score: 0.809)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly
  - Snippet 4 (score: 0.787)
    > analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly higher immune cell scores and immune checkpoint expression levels. Finally, GSVA analysis was performed to predict potential signaling pathways linked to LGALS3 and HCP5 in immune evasion and metabolic reprogramming of HCC. Our findings indicated that the upregulation of LGALS3 via the HCP5/hsa-miR-27b-3p axis is associated with unfavorable prognosis and increased tumor immune infiltration in HCC.
  - Snippet 5 (score: 0.777)
    > Zhang et al. [14] suggested overexpression of LGALS3 promoted HCC bone metastasis and induced associated skeletal complications.Nevertheless, the expression, prognosis, epigenetic, and molecular regulatory mechanisms of LGALS3 in HCC have been incompletely studied.In addition, LGALS3 relation with immune infiltration in HCC TME has yet to be inadequately investigated.
    > This work began with a pan-cancer study of LGALS3 expression and its predictive value in a variety of human malignancies.We further explored the LGALS3 potential upstream regulatory noncoding RNAs (ncRNAs) involving microRNAs (miRNAs) as well as long noncoding RNAs (lncRNAs) throughout HCC.Subsequently, in HCC, a correlation analysis was investigated between LGALS3 and tumor immunity-related indicators involving cell chemotaxis, immune checkpoints, immune cell biomarkers, and infiltration.Eventually, the association between the expression of LGALS3 and signaling pathways was examined in HCC.Findings demonstrated that LGALS3 might have a role in the malignancy of HCC and immune cell infiltration via the HCP5/hsa-miR-27b-3p/ LGALS3 axis, suggesting that a novel HCP5/hsa-miR-27b-3p/LGALS3 axis could be a biomarker for prognosis and treatment target for HCC patients.
  - Snippet 6 (score: 0.750)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.
  - Snippet 7 (score: 0.707)
    > Next, the prognostic value of LGALS3 expression in the 23 kinds of cancer patients was then determined.Correlations between LGALS3 expression with OS (overall survival) were evaluated using the GEPIA2 database.In the OS study, only elevated LGALS3 expression indicated poorer survival for HCC patients (Fig. 2A).LGALS3 was not statistically significant for OS of 22 other cancer types patients.Furthermore, DSS (disease-specific survival) LGALS3 in predicting 1-, 3-, and 5-year OS. (H) ROC curve for LGALS3 in predicting 1-, 3-, and 5-year DSS.The higher values of AUC corresponding to higher predictive power.*p value < 0.05; ***p value < 0.001 was lesser in patients suffering from HCC having higher levels of LGALS3 expression (Fig. 2B).Next, we validated the expression levels of LGALS3 protein in HCC tissues using IF staining.As expected, HCC tumor demonstrated strong LGALS3 expression (Fig. 2C).These findings were further validated by qRT-PCR assay of tumor and adjacent normal tissues from 5 HCC patients.Here, LGALS3 expression was also significantly increased in the HCC tissues (Fig. 2D).In addition, LGALS3 expression was shown to be linked with the pathological stage of HCC, as illustrated in Fig. 2E.High expression of LGALS3 gene is associated with high tumor grade in HCC (Fig. 2F).Moreover, LGALS3 expression was significantly associated with OS and DSS in both univariate and multivariate analyses (Figure S2A-H).Time-dependent ROC analysis showed that the area under the ROC curve was 0.672 at 5 years of OS, and 0.691 at 5 years of DSS (Fig. 2G-H).Taken together, LGALS3 might function as a prospective biomarker for the prognosis of patients suffering from HCC.

### [2] Combined High—Throughput Proteomics and Random Forest Machine-Learning Approach Differentiates and Classifies Metabolic, Immune, Signaling and ECM Intra-Tumor Heterogeneity of Colorectal Cancer
- Authors: C. Contini, B. Manconi, A. Olianas, Giulia Guadalupi, Alessandra Schirru et al.
- Year: 2024
- Venue: Cells
- URL: https://www.semanticscholar.org/paper/b7d8516d42c8108cbdf59e6865a8fb424c450946
- DOI: 10.3390/cells13161311
- PMID: 39195201
- PMCID: 11352245
- Citations: 6
- Summary: Different metabolic strategies appeared to be adopted by the two CRC regions to uncouple the Krebs cycle and cytosolic glucose metabolism, promote lipogenesis, promote amino acid synthesis, down-regulate bioenergetics in mitochondria, and up-regulate oxidative stress.
- Evidence snippets:
  - Snippet 1 (score: 0.832)
    > The regulatory activity on the cytoskeleton carried out by N-WASP is fundamental for the motility of leukocytes. CgA and Gal-3 are associated with GO annotations concerning the chemotaxis of immune cells, including GO:0002551 "mast cell chemotaxis", GO:0002548 "monocyte chemotaxis", and GO:0030593 "neutrophil chemotaxis".

### [3] Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins
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
  - Snippet 1 (score: 0.770)
    > Lgals3 has been implicated in the regulation of innate and adaptive immune responses, where it participates in the activation or differentiation of immune cells and contributes to phagocytic clearance of microorganisms and apoptotic cells by macrophages (117,118). Lgals3 has been reported to promote but also to inhibit T-cell apoptosis depending on whether it binds to glycoproteins on the cell surface (CD45 and CD71) or to intracellular ligands (Bcl-2) (119, 120). In the placenta, Lgals3 was detected in all trophoblastic lineages including villous cytotrophoblasts (CTB) and EVT with a reduction of Lgals3 expression observed from the VT to the trophoblastic cell columns (121). This pattern of Lgals3 expression correlates with the switch from a proliferative to a migratory trophoblast phenotype and while placental Lgals3 dysregulation has been associated with some obstetric complications including spontaneous or recurrent miscarriages, further studies are needed to understand its contribution to trophoblast biology (81,122). In addition to trophoblasts, Lgals3 is expressed by maternal decidual cells (73). While showing a different expression pattern, both Lgals1 and Lgals3 have been proposed to play a role in cell-cell and cell-matrix interactions of trophoblast during placentation (121). Studies of the importance of Lgals3 in murine pregnancy by Yang et al. indicate that Lgals3 is expressed in the luminal and glandular epithelium and that an increase in Lgals3 is required for proper embryo implantation (123). In addition, Lgals3 affects chemotaxis and morphology of endothelial cells and stimulates capillary tube formation and angiogenesis in vivo (124). Therefore, besides its proposed roles in embryo implantation, immune regulation and trophoblast-matrix interactions, Lgals3 has a potential role in placental angiogenesis.

### [4] Macrophages secrete murinoglobulin-1 and galectin-3 to regulate neutrophil degranulation after myocardial infarction
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
  - Snippet 1 (score: 0.761)
    > while Lgals3 increased at MI day 7. The ratio of MUG1 to Lgals3 positively correlated with infarct wall thickness, revealing that MUG1 attenuated infarct wall thinning. In conclusion, macrophages at MI day 1 secrete MUG1 to limit and Lgals3 to accentuate neutrophil degranulation to regulate infarct wall thinning.
  - Snippet 2 (score: 0.750)
    > Inflammation presides early after myocardial infarction (MI) as a key event in cardiac wound healing. Ischemic cardiomyocytes secrete inflammatory cues to stimulate infiltration of leukocytes, predominantly macrophages and neutrophils. Infiltrating neutrophils degranulate to release a series of proteases including matrix metalloproteinase (MMP)-9 to break down extracellular matrix and remove necrotic myocytes to create space for the infarct scar to form. While neutrophil to macrophage communication has been explored, the reverse has been understudied. We used a proteomics approach to catalogue the macrophage secretome at MI day 1. Murinoglobulin-1 (MUG1) was the highest-ranked secreted protein (4.1-fold upregulated at MI day 1 vs. day 0 pre-MI cardiac macrophages, p = 0.004). By transcriptomics evaluation, galectin-3 (Lgals3) was 2.2-fold upregulated (p = 0.008) in MI day 1 macrophages. We explored the direct roles of MUG1 and Lgals3 on neutrophil degranulation. MUG1 blunted while Lgals3 amplified neutrophil degranulation in response to phorbol 12-myristate 13-acetate or interleukin-1β, as measured by MMP-9 secretion. Lgals3 itself also stimulated MMP-9 secretion. To determine if MUG1 regulated Lgals3, we co-stimulated neutrophils with MUG1 and Lgals3. MUG1 limited degranulation stimulated by Lgals3 by 64% (p < 0.001). In vivo, MUG1 was elevated in the infarct region at MI days 1 and 3, while Lgals3 increased at MI day 7. The ratio of MUG1 to Lgals3 positively correlated with infarct wall thickness, revealing that MUG1 attenuated infarct wall thinning. In conclusion, macrophages at MI day 1 secrete MUG1 to limit and Lgals

### [5] Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice
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
  - Snippet 1 (score: 0.728)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.

### [6] An Inflammation-Immunity Classifier of 11 Chemokines for Prediction of Overall Survival in Head and Neck Squamous Cell Carcinoma
- Authors: Yushan Liang, Guofei Feng, S. Zhong, Xiaoyu Gao, Yan Tong et al.
- Year: 2019
- Venue: Medical Science Monitor : International Medical Journal of Experimental and Clinical Research
- URL: https://www.semanticscholar.org/paper/ca1a2988b75211cc5296d7fc979460ada97a48d4
- DOI: 10.12659/MSM.915248
- PMID: 31203306
- PMCID: 6592142
- Citations: 5
- Summary: This 11-chemokine signature could serve as a reliable prognostic tool for HNSC patients and might be useful to guide individualized treatment or even gene target therapy for high-risk patients.
- Evidence snippets:
  - Snippet 1 (score: 0.728)
    > Gene functional analysis indicated 29 GO terms and 4 KEGG pathways which these 11 chemokines were enriched in (Figure 4A, 4B). The main 9 participating GO terms contained chemokine-mediated (GO: 0070098), inflammatory response (GO: 0006954), cellular response to interleukin-1 (GO: 00071347), neutrophil chemotaxis (GO: 0030593), cellular   response to tumor necrosis factor (GO: 0071356), lymphocyte chemotaxis (GO: 0048247), monocyte chemotaxis (GO: 0002548), chemokine activity (GO: 0008009), and CCR chemokine receptor (GO: 0048020). The key involved KEGG pathways were chemokine signaling pathway (Kegg: 04062), cytokinecytokine receptor (Kegg: 04060), NOD-like receptor signaling pathway (Kegg: 04621), and Malaria (Kegg: 05144).

### [7] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
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
  - Snippet 1 (score: 0.727)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.
  - Snippet 2 (score: 0.725)
    > Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated. Induction of PPP2R2A protein (Fig. 5) but not gene expression (Fig. 7) in THP-1 cells expressing LGALS3 shRNA suggests that LGALS3 acts directly on the PP2A subunits via a post-transcriptional mechanism in these cells. The TCGA data (Table 3) however suggests that there is a positive correlation between gene expression of LGALS3 and PPP2R2A suggesting that a common pathway may regulate the two genes. Fig. 8. Progeny clustering identified an optimal number of 4 distinct protein clusters for this ProFnGrp. Protein networks were generated and showed interactions between "core-proteins" (large nodes) and other probed proteins (small nodes) from the data set. Clustering method has been described in our previous publication (ref. [37]) and further information on these protein networks can be found on our website "Leukemia Profile Atlases", available at https://www.leukemiaatlas.org/. Progeny clustering identified one protein cluster with expression similar to that of the normal CD34+ samples which was designated as "normal-state" while three "leukemia-specific" protein patterns characterized by high expression individually of CD74, LGAL3, and a fourth state with both on. PPP2RA/B/C/D was the only LGALS3 network protein demonstrated to be directly regulated by LGALS3 in the THP-1 cells (Fig. 5). In our previous study we saw potent suppression of AKT signaling by LGALS3 inhibition, so perhaps the mechanism involves LGALS3 suppression of the AKT phosphatase [15]. However, we did not see suppression of LGALS3 affect other network proteins in the THP-1 cells (data not shown). The role of other galectins such as LGALS1 in AML biology is not clear.

### [8] Morphological and transcriptional insights into the role of histone phosphorylation-related genes in early development of the chicken duodenum
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
  - Snippet 1 (score: 0.725)
    > Notably, as broilers age (from D0 to D7), the intestinal VH increases accordingly, indicating a positive balance between intestinal cell proliferation and apoptosis (i.e., cell proliferation predominates over apoptosis). Through transcriptional network analysis, we identified eight histone phosphorylation-associated hub genes (LGALS3, ITGB2, IRF7, SOCS3, CSF1R, KIF23, SMC2, and DLGAP5) that mechanistically link epigenetic regulation to developmental programming.
    > LGALS3 (galectin-3) plays critical roles in macrophage chemotaxis, mucosal barrier maintenance, intestinal epithelial cell (IEC) apoptosis regulation, and inflammatory responses [21][22][23]. Our study revealed a 6.59-fold increase in LGALS3 gene expression in the duodenum at D7 compared to D0 (Supplement 6), with functional analysis confirming its involvement in macrophage chemotaxis (Supplement 7). These findings align with Sun et al [21], who reported that LGALS3 silencing in necrotizing enterocolitis models inhibited the TLR4/NF-κB pathway, subsequently reducing IEC apoptosis and inflammation [21]. Emerging evidence further suggests LGALS3' s protective functions through ER stress modulation, autophagy regulation, and inflammasome control in intestinal Behçet' s disease [22], along with its capacity to upregulate key mucosal barrier components (MUC2, Occludin, and ZO-1) [23]. Collectively, these observations suggest LGALS3 promotes duodenal development through: 1) mucosal barrier reinforcement via tight junction protein upregulation, 2) inflammatory control through TLR4/NF-κB-mediated macrophage regulation, and 3) cellular homeostasis maintenance via ER stress/autophagy pathways.

### [9] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
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
  - Snippet 1 (score: 0.714)
    > Scale bar: 10 μm. (I) Immunofluorescent analysis of the colocalization of LGALS3 with ubiquitin in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm. (J) Representative fluorescent images of CRC cells transiently expressing Mrfp-GFP-tandem fluorescent-tagged LGALS3 (tfGal3) followed by 0.50 μM periplocin treatment for 24 h. Scale bar: 10 μm. (K) Quantitative analysis of the GFP + RFP + or GFP − RFP + LGALS3 puncta in (J). (L) the relative decreased ratio of Magic Red intensity, relative increased ratio of LysoSensor Blue intensity, relative increased ratio of the interaction between LGALS3 and TRIM16, and relative increased ratio of LC3B-II protein level in DLD-1 cells following 0.50 μM periplocin treatment at different time periods. Results are representative of three independent experiments. Data are presented as mean ± SD. *P < 0.05, **P < 0.01, ***P < 0.001. for LGALS3 degradation, we generated lysine to arginine mutants of LGALS3 at K196 or Lys210 (LGALS3 K196R or LGALS3 K210R ). As shown in Figure 6I, the ubiquitinconjugated level of LGALS3 K196R mutant was comparable to the wild type (WT), whereas K210 mutation significantly decreased LGALS3 ubiquitination. These results suggest that periplocin elevates LGALS3 level by preventing K210 ubiquitination and proteasomal degradation. In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3.
  - Snippet 2 (score: 0.710)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.

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
  - Snippet 1 (score: 0.713)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [11] In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression
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
  - Snippet 1 (score: 0.711)
    > Finally, since LGALS3 (Galectin-3) has been shown to interact with O-glycans in the mucosal epithelium [30], and considering its overexpression observed by proteomics and further confirmed by PCR and WB analyses upon depletion of C1GALT1, we focused on the role of LGALS3 in EC by IHC.
    > A total of 151 out of 178 cores from 79 EC patients were considered adequate for LGALS3 expression assessment by IHC. Morphologic assessment of LGALS3 IHC staining characteristics revealed different staining patterns (Fig. 5 A). Out of the 151 evaluable cores, 45 (29.8%) showed absent LGALS3 expression. LGALS3 positive samples showed variable and low intensity protein expression (mean positive tumor cells per sample = 35.4%). A small subset of cores (13/151, 8.6%) demonstrated diffuse (> 90% positive tumor cells per sample) staining. LGALS3 score varied across histologic types, with serous and undifferentiated tumors displaying the highest protein expression (median IHC LGALS3 score = 10, 20, 50 and 55 for endometrioid, clear cell, serous and undifferentiated tumor types, respectively) (Fig. 5B). Interestingly, the aggressive histologic variants (clear cell, serous and undifferentiated) showed higher LGALS3 IHC scores than endometrioid variants (p value < 0.001). In addition, LGALS3 expression positively correlated with tumor grade. High grade tumors (G3) displayed higher protein expression (median LGALS3 IHC score = 30) compared to low grade tumors (median LGALS3 IHC score for G1/G2 tumors = 10). This finding was independent of histologic type, as similar results were observed when analyzing endometrioid tumors.
    > Finally, we interrogated the correlation between the expression levels of LGALS3 and C1GALT1.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.