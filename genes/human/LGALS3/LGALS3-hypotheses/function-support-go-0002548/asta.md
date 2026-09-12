---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:46:27.943155'
end_time: '2026-06-22T04:46:30.860784'
duration_seconds: 2.92
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0002548
  hypothesis_text: LGALS3 has monocyte chemotaxis (GO:0002548).
  term_context: '- Term: monocyte chemotaxis (GO:0002548)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[7]
  source_context_yaml: "term:\n  id: GO:0002548\n  label: monocyte chemotaxis\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033"
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
citation_count: 12
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has monocyte chemotaxis (GO:0002548).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has monocyte chemotaxis (GO:0002548).
Key context:
- Term: monocyte chemotaxis (GO:0002548)
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
- **Hypothesis slug:** function-support-go-0002548
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[7]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0002548
  label: monocyte chemotaxis
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has monocyte chemotaxis (GO:0002548). Gene/protein: LGALS3. Org...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 12
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
  - Snippet 1 (score: 0.933)
    > Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].According to Table S1, the expression of LGALS3 was statistically positively correlated with several chemokines of immune cells, involving monocytes/macrophages (CCL2, CCL3, CCL5, CCL7, CCL13, CCL17, and CCL22), T lymphocytes (CCL2, CCL1, CCL17, and CCL22), eosinophils (CCL11, CCL26, CCL5, CCL7, CCL13, and CCL3), mast cells (CCR1, CCR2, CCR3, CCR4, CCR5, CXCR2, and CXCR4), and neutrophils (CXCL8).Taken together, these outcomes indicate that LGALS3 is positively associated with immune cell infiltration and cell chemotaxis and could have a crucial function in HCC tumor immune microenvironment.
    > LGALS3 expression correlation and immune cell biomarkers in HCC Next, we wanted to investigate the LGALS3 function in HCC tumor immunity further.Utilizing GEPIA databases, we studied the correlation between LGALS3 expression and immune cell biomarkers within HCC.
  - Snippet 2 (score: 0.902)
    > To delineate the driving mechanism of LGALS3 for the malignant progression of HCC, the KEGG and GO analysis was conducted.The volcano plot and heatmap showed significantly differentially expressed genes between LGALS3 high-and low-expression groups (Figure S3A-B).The KEGG pathway analysis revealed that these LGALS3-related genes were enriched in the IL-17 signaling pathway, ECM-receptor interaction pathway, central carbon metabolism in cancer pathway, leukocyte transendothelial migration pathway and PI3K-Akt signaling pathway.Meanwhile, the GO analysis revealed that these genes were strongly associated with cell chemotaxis, leukocyte chemotaxis, regulation of leukocyte migration, as well as regulation of chemotaxis (Fig. 5A).Accumulating evidence has proven the immune system has an essential role in malignancy pathogenesis [17], and LGALS3 is closely correlated with CD163 + tumor-associated macrophages (TAM) in glioma [10].Therefore, we studied the association between LGALS3 level and the immune infiltration level in HCC.There was no statistical difference in immune cell infiltration levels over a number of LGALS3 copy numbers (Fig. 5B).Meanwhile, immune infiltration analysis revealed that expression of LGALS3 showed a significant positive association with several immune cell populations, involving CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, dendritic cell, as well as cancer-associated fibroblasts (CAFs) within HCC (Fig. 5C-E).Based on these results, we further evaluated the immune score in HCC patients with high and low LGALS3 expression.The scores of immune cells, including CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, and dendritic cell, were significantly higher in the high LGALS3 expression groups, as shown in Fig. 5F.Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].
  - Snippet 3 (score: 0.804)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly
  - Snippet 4 (score: 0.798)
    > analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly higher immune cell scores and immune checkpoint expression levels. Finally, GSVA analysis was performed to predict potential signaling pathways linked to LGALS3 and HCP5 in immune evasion and metabolic reprogramming of HCC. Our findings indicated that the upregulation of LGALS3 via the HCP5/hsa-miR-27b-3p axis is associated with unfavorable prognosis and increased tumor immune infiltration in HCC.
  - Snippet 5 (score: 0.771)
    > Zhang et al. [14] suggested overexpression of LGALS3 promoted HCC bone metastasis and induced associated skeletal complications.Nevertheless, the expression, prognosis, epigenetic, and molecular regulatory mechanisms of LGALS3 in HCC have been incompletely studied.In addition, LGALS3 relation with immune infiltration in HCC TME has yet to be inadequately investigated.
    > This work began with a pan-cancer study of LGALS3 expression and its predictive value in a variety of human malignancies.We further explored the LGALS3 potential upstream regulatory noncoding RNAs (ncRNAs) involving microRNAs (miRNAs) as well as long noncoding RNAs (lncRNAs) throughout HCC.Subsequently, in HCC, a correlation analysis was investigated between LGALS3 and tumor immunity-related indicators involving cell chemotaxis, immune checkpoints, immune cell biomarkers, and infiltration.Eventually, the association between the expression of LGALS3 and signaling pathways was examined in HCC.Findings demonstrated that LGALS3 might have a role in the malignancy of HCC and immune cell infiltration via the HCP5/hsa-miR-27b-3p/ LGALS3 axis, suggesting that a novel HCP5/hsa-miR-27b-3p/LGALS3 axis could be a biomarker for prognosis and treatment target for HCC patients.

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
  - Snippet 1 (score: 0.871)
    > The regulatory activity on the cytoskeleton carried out by N-WASP is fundamental for the motility of leukocytes. CgA and Gal-3 are associated with GO annotations concerning the chemotaxis of immune cells, including GO:0002551 "mast cell chemotaxis", GO:0002548 "monocyte chemotaxis", and GO:0030593 "neutrophil chemotaxis".

### [3] Phenotypic Switching of Vascular Smooth Muscle Cells in Atherosclerosis
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
  - Snippet 1 (score: 0.844)
    > Lgals3 (also referred to as galectin-3) is considered a marker of macrophage-like cells. 13,31 Rong et al detected a population of VSMCs that expressed Lgals3 following cholesterol loading in vitro. 31 Recently, Alencar et al found that Lgals3 activation is not a specific marker of the differentiation of VSMCs to a macrophage-like state but rather it is a marker of VSMCs entering a transitional state, with increased expression of genes associated with stem cells that are capable of extracellular matrix remodeling. 16 Of note, similar to SEM-like cells, Lgals3 + cells also have increased expression of lymphocyte antigen 6 family member A and vascular cell adhesion molecule 1. Further studies to investigate if SEM-like cells are derived from Lgals3 + cells are warranted.
    > Using mouse, rat, and human models of cholesterolloading in VSMCs, Li et al found that SREBP1 (sterol regulatory-element binding protein-1) and Krüppel-like factor-15 induced up-and downregulation of Lgals3, respectively, via binding to the Lgals3 gene promoter (albeit at different sites). 45 Likewise, Lgals3 promoted SREBP1 gene expression, producing a feedforward loop upregulated by cholesterol loading. 45 Moreover, Lgals3 and SREBP1 downregulated myocardin-related transcription factor A expression in VSMCs. 45 In another study, Owsiany et al used a dual lineage tracing model and found that Lgals3 + VSMCs produce monocyte chemoattractant protein 1, a proinflammatory chemokine. 15 Knockout of monocyte chemoattractant protein 1 specifically in Lgals3 + VSMCs resulted in the formation of atherosclerotic lesions with a greater ACTA2 content in the fibrous cap and decreased Lgals3 + cell content, a feature of stable plaque. 15
  - Snippet 2 (score: 0.785)
    > Knockout of monocyte chemoattractant protein 1 specifically in Lgals3 + VSMCs resulted in the formation of atherosclerotic lesions with a greater ACTA2 content in the fibrous cap and decreased Lgals3 + cell content, a feature of stable plaque. 15 Another study showed that deletion of the Has3 (smooth muscle cell hyaluronan synthase 3) gene in mouse promoted VSMC transition to a Lgals3 + state. 46

### [4] Activation of CD14+ Monocytes via the IFN-γ Signaling Pathway Is Associated with Immune-Related Adverse Events in Hepatocellular Carcinoma Patients Receiving PD-1 Inhibition Combination Therapy
- Authors: Yaoru Song, S.-W. Pan, Jiahe Tian, Yingying Yu, Siyu Wang et al.
- Year: 2024
- Venue: Biomedicines
- URL: https://www.semanticscholar.org/paper/b05a3ac750e4ab33f0d31bc2708c804f3502f743
- DOI: 10.3390/biomedicines12061140
- PMID: 38927347
- PMCID: 11201226
- Citations: 5
- Summary: The activation of monocytes induced by the IFN-γ signaling pathway is an important mechanism underlying the occurrence of irAEs in HCC patients receiving PD-1 inhibition combination therapy.
- Evidence snippets:
  - Snippet 1 (score: 0.835)
    > We used the AUCell-R package to score the target gene sets.With reference to the relevant literature, we used MONOCYTE CHEMOTAXIS (GO:0002548) for the monocyte chemotaxis score and TYPE II INTERFERON-MEDIATED SIGNALING PATHWAY (GO:0060333) for the IFN-γ signaling pathway score.

### [5] Macrophage-derived Spp1 promotes intramuscular fat in dystrophic muscle
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
  - Snippet 1 (score: 0.795)
    > Lgals3 clusters 2 and 3 expressed the highest Spp1. All Spp1-expressing clusters showed a drastic reduction in Spp1 in the cKO (Figure 2B, compare blue and green) (8). Lgals3-2 cells also expressed Arg1 while Lgals3-3 expressed Igf1 (11). The proportion of different monocyte/macrophage subtypes was evaluated in the 2 genotypes (Figure 2, C and D). While the proportion of Lgals3-3 and Lgals3-2 remained similar in the 2 genotypes, a mild increase in Lgals3-1 was observed in the cKO, while both monocyte subclusters slightly decreased in the cKO (Figure 2C). Although the overall number of macrophages increased in the cKO (mdx:969 vs cKO 4,028), cKO macrophages did not show large changes in the cellular frequency of subtypes (Figure 2D). Inflammatory genes were either unchanged or slightly reduced in the cKO, including the chemokines Ccl3 and Ccl4 (Figure 2F) and Tgfb1 (Supplemental Figure 2B). However, IFN genes such as Ifi207, Ifi204, and Isg15 were slightly increased in cKO monocytes (Figure 2F).

### [6] Secreted Factors and Extracellular Vesicles Account for the Immunomodulatory and Tissue Regenerative Properties of Bone-Marrow-Derived Mesenchymal Stromal Cells for Osteoarthritis
- Authors: E. Ragni, C. Perucca Orfei, L. de Girolamo
- Year: 2022
- Venue: Cells
- URL: https://www.semanticscholar.org/paper/b4611c0ee0053b5bd745e5c412143451f2f14a97
- DOI: 10.3390/cells11213501
- PMID: 36359897
- PMCID: 9658264
- Citations: 12
- Influential citations: 1
- Summary: The majority of identified molecules repress the activation of immune cells and the production of OA-related inflammatory mediators, as well as promote cartilage protection by acting on both chondrocytes homeostasis and extracellular matrix-degrading enzymes.
- Evidence snippets:
  - Snippet 1 (score: 0.790)
    > These were mainly associated with cluster 1 (Figure 4), which included leukocytes (30 overall factors, GO:0030595) and their subtypes: granulocytes (23, GO:0071621), lymphocytes (19, GO:0048247) and monocytes (17, GO:0002548) (Supplementary Figure S1 and Supplementary Table S1B for all analyzed factors). Interestingly, the leukocyte activation term was defined by several players (31, GO:0045321) without the identification of a specific cluster (Supplementary Figure S2 and Supplementary Table S1C for all analyzed factors). In this frame, lymphocytes (18, GO:0046649) and the subcategory T cells (12, GO:0042110) were the most present terms, followed by neutrophils (10, GO:0042119) and macrophages (4, GO:0042116). Using the online tool STRING, protein-protein interaction levels for 24 proteins of the BMSCs Cluster 1 related to the GO term "chemotaxis" for leukocytes, lymphocytes, monocytes and granulocytes were mined. The different colors represent the immune cell type the "chemotaxis" term is associated with. The blue connections are for proteins with known interactions based on curated databases; violet connections for proteins with experimentally determined interactions. Colorless nodes for proteins not related to the GO terms: leukocytes chemotaxis, lymphocytes chemotaxis, monocytes chemotaxis and granulocytes chemotaxis in the STRING database v 11.5. Empty nodes, proteins of unknown 3D structure; filled nodes, known or predicted 3D structure.

### [7] Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins
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
  - Snippet 1 (score: 0.755)
    > Lgals3 has been implicated in the regulation of innate and adaptive immune responses, where it participates in the activation or differentiation of immune cells and contributes to phagocytic clearance of microorganisms and apoptotic cells by macrophages (117,118). Lgals3 has been reported to promote but also to inhibit T-cell apoptosis depending on whether it binds to glycoproteins on the cell surface (CD45 and CD71) or to intracellular ligands (Bcl-2) (119, 120). In the placenta, Lgals3 was detected in all trophoblastic lineages including villous cytotrophoblasts (CTB) and EVT with a reduction of Lgals3 expression observed from the VT to the trophoblastic cell columns (121). This pattern of Lgals3 expression correlates with the switch from a proliferative to a migratory trophoblast phenotype and while placental Lgals3 dysregulation has been associated with some obstetric complications including spontaneous or recurrent miscarriages, further studies are needed to understand its contribution to trophoblast biology (81,122). In addition to trophoblasts, Lgals3 is expressed by maternal decidual cells (73). While showing a different expression pattern, both Lgals1 and Lgals3 have been proposed to play a role in cell-cell and cell-matrix interactions of trophoblast during placentation (121). Studies of the importance of Lgals3 in murine pregnancy by Yang et al. indicate that Lgals3 is expressed in the luminal and glandular epithelium and that an increase in Lgals3 is required for proper embryo implantation (123). In addition, Lgals3 affects chemotaxis and morphology of endothelial cells and stimulates capillary tube formation and angiogenesis in vivo (124). Therefore, besides its proposed roles in embryo implantation, immune regulation and trophoblast-matrix interactions, Lgals3 has a potential role in placental angiogenesis.

### [8] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
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
  - Snippet 1 (score: 0.750)
    > Scale bar: 10 μm. (I) Immunofluorescent analysis of the colocalization of LGALS3 with ubiquitin in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm. (J) Representative fluorescent images of CRC cells transiently expressing Mrfp-GFP-tandem fluorescent-tagged LGALS3 (tfGal3) followed by 0.50 μM periplocin treatment for 24 h. Scale bar: 10 μm. (K) Quantitative analysis of the GFP + RFP + or GFP − RFP + LGALS3 puncta in (J). (L) the relative decreased ratio of Magic Red intensity, relative increased ratio of LysoSensor Blue intensity, relative increased ratio of the interaction between LGALS3 and TRIM16, and relative increased ratio of LC3B-II protein level in DLD-1 cells following 0.50 μM periplocin treatment at different time periods. Results are representative of three independent experiments. Data are presented as mean ± SD. *P < 0.05, **P < 0.01, ***P < 0.001. for LGALS3 degradation, we generated lysine to arginine mutants of LGALS3 at K196 or Lys210 (LGALS3 K196R or LGALS3 K210R ). As shown in Figure 6I, the ubiquitinconjugated level of LGALS3 K196R mutant was comparable to the wild type (WT), whereas K210 mutation significantly decreased LGALS3 ubiquitination. These results suggest that periplocin elevates LGALS3 level by preventing K210 ubiquitination and proteasomal degradation. In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3.
  - Snippet 2 (score: 0.733)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.

### [9] LGALS3 Is a Poor Prognostic Factor in Diffusely Infiltrating Gliomas and Is Closely Correlated With CD163+ Tumor-Associated Macrophages
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
  - Snippet 1 (score: 0.743)
    > Background: Glioma, the most common brain tumor, is a heterogeneous group of glia-derived tumors, the majority of which have characteristics of diffuse infiltration and immunosuppression. The LGALS protein family is a large class of sugar-binding proteins. Among them, LGALS3 has been reported to promote tumor development and progression in some cancers. However, the clinical significance and biological functions of LGALS3 in glioma remain virtually unknown. The purpose of our research is to detect LGALS3 expression and its prognostic value in glioma and reveal the relationship between its expression and the clinico/molecular-pathological features of patients and immune cell infiltration. Methods: LGALS3 protein expression was examined by immunohistochemistry. The mRNA expression data of LGALS3 was downloaded and analyzed from TCGA and Rembrandt datasets. The association between LGALS3 and glioma clinically relevant diagnostic/molecular markers (IDH, 1p19q, ATRX, MGMT, and TERT) was examined using the Chi-Squared (χ2) test. The correlation between LGALS3 expression and the infiltration of multiple intra-tumoral immune cell types, including B cells (CD20), T cells (CD4 and CD8), macrophages (CD68), and M2 tumor-associated macrophages (CD163), was evaluated by Spearman correlation analysis. Kaplan-Meier analysis and the Cox regression analysis were applied to evaluate the prognostic value of LGALS3 in glioma. The log-rank test was used to evaluate Kaplan-Meier results for significance. Results: Out of all 304 glioma cases, LGALS3 protein was expressed in 125 glioma cases (41.1%, 125/304), with 69.2% (9/13) in WHO I, 9.8% (8/82) in WHO II, 34.2% (26/76) in WHO III, and 61.7% (82/133) in WHO IV. The expression of LGALS3 was correlated with patient age, WHO grade, PHH3 (mitosis), Ki67 index,
  - Snippet 2 (score: 0.738)
    > This may explain why LGALS3 positive glioma patients have a significantly shorter OS than LGALS3 negative patients, suggesting that LGALS3 may play a role in malignant progression in glioma through changing the immune microenvironment in glioma. Some studies have also confirmed that LGALS3 played a key role in glioma development through increasing cell motility and invasion (21,22). Vladimirova et al. (23) found that LGALS3 expression was mediated by Runx-2 transcription factors, which contributed to the malignant progression of glial tumors. Conversely, only Gordower et al. (24) reported that LGALS3 expression decreased as the WHO level increased in astrocytic tumors. We think the reason for this difference may be partially due to the small number of patient samples in their study. Moreover, online database analysis also verified our results. Patients with high expression of LGALS3 mRNA had a poor prognosis.
    > LGALS3 was closely related to IDH status, CD163+ TAMs and was mainly expressed in IDH wild-type glioma. It is worth noting that LGALS3 mRNA was highly expressed in the mesenchymal subtype, a more malignant TCGA GBM subtype with a higher tendency for recurrence, metastasis, and increased vascularity.
    > Most importantly, we found that LGALS3 was involved in the regulation of the glioma immune microenvironment, particularly CD163+ TAMs. There is growing evidence that complex tumor microenvironments contribute to the malignant progression of gliomas (25,26). Among the components of the tumor microenvironment, tumor-associated macrophages (TAMs) are considered to provide important support for tumor growth. Macrophages are divided into M1 and M2 subtypes according to their functions. Typically, CD68 is a general marker for macrophages, while CD163 is considered to be a highly specific marker for M2 type macrophages.
  - Snippet 3 (score: 0.733)
    > In the LGALS family, LGALS3 has a special domain that recognizes and binds to β-galactosides on cellular glycoproteins and glycolipids (5).
    > LGALS3 may be observed in the cytoplasm and in the nucleus as well as the extracellular matrix (6). It serves different biological functions, such as cell growth, cell adhesion, angiogenesis, and apoptosis (7).
    > LGALS3 can be expressed in different types of tumors, and accumulating evidence has proved that LGALS3 plays a vital role in tumorigenesis and development (6,(8)(9)(10)(11)(12)(13)(14)(15)(16). Recently, a study indicated that LGALS3 can promote the therapeutic resistance of glioblastoma and is related to tumor risk and prognosis (17). However, its prognostic significance needs to be further confirmed in large glioma samples, and, hitherto, no studies have explored the role of LGALS3 in the glioma immune microenvironment and its correlation with key molecular markers, including isocitrate dehydrogenase 1 (IDH1), alpha-thalassemia/mental retardation X-linked (ATRX), O-6methylguanine-DNA methyltransferase (MGMT), telomerase reverse transcriptase (TERT), and 1p19q.

### [10] Impairment of lysosomal quality control in Huntington disease
- Authors: P. Rusmini, F. Mina, M. Valenza, Martina Vitali, V. Ferrari et al.
- Year: 2025
- Venue: Cell Death & Disease
- URL: https://www.semanticscholar.org/paper/c874bbb3c9e6aa0a3f74519c022f3fa822daf4a8
- DOI: 10.1038/s41419-025-08103-z
- PMID: 41145409
- PMCID: 12559425
- Citations: 4
- Influential citations: 1
- Summary: TFEB and TFE3 are sequestered in muHTT aggregates, and muHTT proteins associates with LMP triggering the translocation of LGALS3 to the lumen of lysosomes, with a close relation between polyQ size and severity of these events.
- Evidence snippets:
  - Snippet 1 (score: 0.739)
    > In HD, high levels of LGALS3 have been found in plasma and brain of patients and mice. LGALS3 upregulation was observed in HD mice before the motor symptoms, in the microglia LGALS3 was found associated to damaged lysosomes and its suppression in microglia ameliorated the HD mice phenotype [36].
    > LGALS3 is emerging as a key factor for NDs for its intracellular role in lysosomal damage, but also for its functions linked to its secretion in the extracellular space. Many pieces of evidence suggest its detrimental role in neurodegeneration, even if a protective role of LGALS3 has been reported (reviewed in ref. [75]). LGALS3 mechanisms of action need further investigation but its pharmacological modulation might represent a valuable target for intervention for NDs. LGALS3 inhibitors have already been tested in metabolic and fibrotic diseases, and these approaches might be applied to NDs. 3′-bis-(4aryltriazol-1-yl) thiodigalactoside (GB039, formerly named TD139), a synthetic small molecule that antagonizes LGALS3 activity by binding to the carbohydrate recognition domain, was effective in idiopathic pulmonary fibrosis and retinal degeneration [76,77]. Pectins, plant cell wall polysaccharides, mostly obtained from citrus and apples, represent natural LGALS3 inhibitors [78,79].
    > In summary, our experiments suggest that LQC impairment might contribute to HD. Indeed, the LGALS3 accumulation observed in HD cellular models due to TFEB and TFE3 sequestration by muHTT inclusions causes LMP and lysophagy impairment, in turn, influences LQC.
    > Fig. 8 TFEB and TFE3 sequestration affects the LQC. A, B NSC-34 cells were transfected with wt or muHTT.

### [11] Citrus pectin modulates chicken peripheral blood mononuclear cell proteome in vitro
- Authors: G. Ávila, M. Bonnet, D. Viala, S. Déjean, G. Grilli et al.
- Year: 2024
- Venue: Poultry Science
- URL: https://www.semanticscholar.org/paper/6755550163f80e4863389b3402bd6ac0b5ac8aa0
- DOI: 10.1016/j.psj.2024.104293
- PMID: 39288719
- PMCID: 11421475
- Citations: 1
- Summary: The results provide a proteomics background to the anti-inflammatory activity of CP, demonstrating that the in vitro downregulation of phagocytosis and chemotaxis is related to changes in proteins related to the cytoskeleton.
- Evidence snippets:
  - Snippet 1 (score: 0.738)
    > Specifically, MARCKS has been shown to promote murine macrophage migration (Green et al., 2012), phagocytosis (Carballo et al., 1999), and proinflammatory cytokines production (Lee et al., 2015), confirming its involvement in modulating inflammation. Some proteins were also less abundant in the CP group. Galectin-3 (LGALS3) and galectin-8 (LGALS8) are ubiquitous carbohydrate-binding proteins (Brinchmann et al., 2018) that participate in several cellular processes, such as inflammation, immune responses, cell migration, autophagy, and cell signaling. In chickens, 5 members have been identified (Kaltner et al., 2011): LGALS3 and LGALS. LGALS3 is highly expressed in monocytes and macrophages and is a potent regulator of cell-extracellular matrix (ECM) and cell-cell interactions, migration, and phagocytosis (Lu et al., 2017). The decreased abundance of LGALS3 in the CP group is also remarkable, as mouse LGALS3 was downregulated by modified citrus pectin (MCP)-a derivative of citrus pectin (Kolatsi-Joannou et al., 2011). MCP also directly inhibits LGALS3, decreasing the adhesion of monocytes and macrophages (Lu et al., 2017). LGALS8 is involved in cytoskeleton reorganization processes, cell adhesion, and cell migration, as well as in autophagy and cytokines and chemokines expression (Gentilini et al., 2017;Johannes et al., 2018). Finally, we also identified proteins involved in the positive regulation of T and B cell proliferation (TFRC) (Ned et al., 2003) and human mononuclear cell migration (AHNAK2) (Zheng et al., 2021), further supporting the CP immune-modulatory function.

### [12] Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice
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
  - Snippet 1 (score: 0.733)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.