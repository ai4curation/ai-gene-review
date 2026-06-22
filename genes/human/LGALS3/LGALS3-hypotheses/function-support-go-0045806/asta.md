---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:46:57.745966'
end_time: '2026-06-22T04:47:01.096905'
duration_seconds: 3.35
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0045806
  hypothesis_text: LGALS3 has negative regulation of endocytosis (GO:0045806).
  term_context: '- Term: negative regulation of endocytosis (GO:0045806)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[11]
  source_context_yaml: "term:\n  id: GO:0045806\n  label: negative regulation of endocytosis\n\
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

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has negative regulation of endocytosis (GO:0045806).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has negative regulation of endocytosis (GO:0045806).
Key context:
- Term: negative regulation of endocytosis (GO:0045806)
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
- **Hypothesis slug:** function-support-go-0045806
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[11]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0045806
  label: negative regulation of endocytosis
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has negative regulation of endocytosis (GO:0045806). Gene/prote...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 11
- Snippets retrieved: 20

## Relevant Papers

### [1] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
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
  - Snippet 1 (score: 0.768)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.
  - Snippet 2 (score: 0.757)
    > To determine if LGALS3 may be involved in regulation of the gene expression of the proteins most positively correlated with LGALS3 expression, we utilized THP-1 cells that expressed control lentiviral plasmid (LKO) and THP-1 cells that expressed LGALS3 shRNA. qRT-PCR analysis of cDNA generated from RNA from these cells revealed that there was 90% reduction of LGALS3 expression by the shRNA (Fig. 7). However, suppression of LGALS3 did not result in a major alteration of expression of ATG7, ITGAL, CCND3, PRKCA, PARP1,  LGALS3 expression positively correlates with ATG7 and ITGAL and negatively correlates with SSBP2 and ERG in AML. CBioportal software was used to compare RNASeq measured gene expression of LGALS3 with ATG7, ITGAL, SSBP2, ERG, and other genes (listed in Table 3) in AML samples in the TCGA dataset from ref. [39].
  - Snippet 3 (score: 0.749)
    > LGALS3 were similarly correlated with gene expression, we utilized cBioPortal software (http://www.cbioportal.org/) to query the TCGA AML database that derived from the 2013 New England Journal of Medicine publication [39]. Of the top nine unmodified proteins that were positively correlated with LGALS3 protein expression, expression of genes for eight proteins (ATG7, ITGAL, MAP2K1, MAPK1, JMJD6, CCND3, VASP, and PRKCA) were significantly higher (q value b0.05) in AML cells with elevated LGALS3 expression in the TCGA database (Fig. 6; Table 3).Expression of LCK was not correlated with LGALS3 (q value = 0.282; Table 3). Of the top nine unmodified proteins that were negatively correlated with LGALS3 protein expression, expression of genes for seven proteins (SSBP2, ERG, KIT, PPP2R2A, PARP1, MYC, and TRIM24) were significantly lower (q value b0.05) in AML cells with elevated LGALS3 expression (Fig. 6; Table 3). Expression of SMAD1 trended lower in cells with elevated LGALS3 (q value = 0.0726; Table 3). Expression of NR4A1 was actually higher in cells with elevated LGALS3 (q value = 0.0399; Table 3). At present, it is not clear if LGALS3 regulates gene expression of any of these genes, whether any of the network proteins may serve as a regulator of LGALS3 gene expression, or whether there is a yet unidentified common regulator to the genes in the LGALS3 RPPA network. To determine if LGALS3 may be involved in regulation of the gene expression of the proteins most positively correlated with LGALS3 expression, we utilized THP-1 cells that expressed control lentiviral plasmid (LKO) and THP-1 cells that expressed LGALS3 shRNA.
  - Snippet 4 (score: 0.747)
    > Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated. Induction of PPP2R2A protein (Fig. 5) but not gene expression (Fig. 7) in THP-1 cells expressing LGALS3 shRNA suggests that LGALS3 acts directly on the PP2A subunits via a post-transcriptional mechanism in these cells. The TCGA data (Table 3) however suggests that there is a positive correlation between gene expression of LGALS3 and PPP2R2A suggesting that a common pathway may regulate the two genes. Fig. 8. Progeny clustering identified an optimal number of 4 distinct protein clusters for this ProFnGrp. Protein networks were generated and showed interactions between "core-proteins" (large nodes) and other probed proteins (small nodes) from the data set. Clustering method has been described in our previous publication (ref. [37]) and further information on these protein networks can be found on our website "Leukemia Profile Atlases", available at https://www.leukemiaatlas.org/. Progeny clustering identified one protein cluster with expression similar to that of the normal CD34+ samples which was designated as "normal-state" while three "leukemia-specific" protein patterns characterized by high expression individually of CD74, LGAL3, and a fourth state with both on. PPP2RA/B/C/D was the only LGALS3 network protein demonstrated to be directly regulated by LGALS3 in the THP-1 cells (Fig. 5). In our previous study we saw potent suppression of AKT signaling by LGALS3 inhibition, so perhaps the mechanism involves LGALS3 suppression of the AKT phosphatase [15]. However, we did not see suppression of LGALS3 affect other network proteins in the THP-1 cells (data not shown). The role of other galectins such as LGALS1 in AML biology is not clear.
  - Snippet 5 (score: 0.704)
    > To assess whether LGALS3 acts directly on the various LGALS3 correlated proteins identified by RPPA, we utilized THP-1 transductant cells that express control shRNA (LKO) or LGALS3 shRNA that we have previously described [15]. At least in THP-1 cells, in most cases LGALS3 did not regulate protein expression of many of the LGALS3 associated proteins including ATG7, ITGAL, SSBP2, or ERG (Fig. 5; data not shown). At present, it is not clear whether these proteins act to regulate LGALS3 expression or if LGALS3 shares common regulators with these proteins. However, one exception was the PP2A B subunit family PPP2R2A/B/C/D. Suppression of LGALS3 resulted in near 2× fold increase in expression of the PP2A B subunits (Fig. 5) which is consistent
    > LGALS3 expression is prognostic for poor survival outcome in some AML populations. Kaplan Meir curves for overall survival (A) and remission duration (B) in the total AML patients studied are presented. Kaplan Meir curvrves for overall survival among the AML patient population that achieved complete remission (C) and for survival after relapse (D) are also included. with the negative correlation found between the proteins by RPPA (Fig. 3).
  - Snippet 6 (score: 0.696)
    > LGALS3 positively regulates BCL2 and MCL-1 gene and protein expression in AML cells by supporting both ERK and AKT pathways [1,2,[12][13][14][15][16][17]. Suppression of LGALS3 by shRNA or with GCS-100 (an inhibitor of LGALS1 and LGALS3) blocks both AKT and ERK signaling pathways [15,17].
    > LGALS3 regulated pathways are involved in expression of genes and protein associated with cancer stem cells (CSC) and thus the galectin likely supports CSC [9]. Recent data suggests that LGALS3 supports malignant cell survival in AML [6,15,18]. In a cohort of Taiwanese AML patients, Cheng and colleagues reported that elevated LGALS3 mRNA was prognostic for poor survival outcome [18]. However, in that study the impact of LGALS3 protein expression or associations of the galectin with potential LGALS3 target proteins was not examined.
    > CD74 (also known as the invariant chain protein) is best known as a chaperone for major histocompatibility (MHC) Class II molecules involved in antigen presentation [19,20]. In addition to mediating MHC Class II molecule endocytosis, CD74 protects these molecules from proteolysis [19][20][21]. CD74 also has MHC Class II independent functions that involve the pro-inflammatory cytokine macrophage inhibitory factor (MIF) and cell surface signaling molecules CD44 and CXCR4 [19][20][21]. CD74 was found to bind MIF but CD74 alone is unable to initiate MIF signaling which requires either CD44 or CXCR4 [19][20][21][22][23]. CD74 dependent MIF signaling pathways include ERK, JNK, and AKT [24][25][26][27]. CD74 dependent MIF signaling has been shown to suppress p53 function and to activate NF kappa B [26,28].
  - Snippet 7 (score: 0.692)
    > The role of other galectins such as LGALS1 in AML biology is not clear.
    > LGALS1 may substitute for some LGALS3 functions particularly those involved in survival pathways as knock down of either LGALS1 or LGALS3 sensitized AML cells to BH3 mimetic drugs [15]. The failure of LGALS3 suppression to affect many of the RPPA identified proteins with the exception of PPP2R2A/B/C/D (Fig. 5) may reflect LGALS1 activity in these cells that may not be present in the primary AML cells. It is possible that many of the LGALS3 network proteins act to regulate LGALS3 rather than being regulated by the galectin. It is also possible that LGALS3 and some of the LGALS3 network proteins are subject to regulation by a yet unidentified common regulator(s). Further examination of the mechanism regulating the LGALS3 network is ongoing.
    > Network analysis from the data identifies a new extremely poor prognosis group based on the interaction between the LGALS3 and CD74 associated protein networks revealing potential biological pathways that may be critical in supporting AML cell survival. AML patients with both networks active are 8.5% of patients in the study (Fig. 9A) and thus this group may represent a sizeable population of AML patients. It is possible the two proteins regulate independent survival pathways that may have a synergistic effect on survival when both are active. The top ten biological processes associated with LGALS3 network include processes associated with cell metabolism (GO:0031325; GO:0032268; and GO:0032270), cell migration (GO:0030355), and response to growth factor stimulus (GO:0071363) and response to chemical stimulus (GO:0070887) (Supplemental Table 1). While it is unclear how LGALS3 might mechanistically influence leukemic cell recovery and growth after therapy, perhaps regulation of these cellular processes are important in addition to the well documented role of LGALS3 in regulation of cell cycle and cell proliferation [1,2,13,14].
  - Snippet 8 (score: 0.679)
    > However, CD44 is present and interestingly is most elevated in patients with active LGALS3 network and CD74 network (Fig. 8). LGALS3 has been shown to be critical for CD44 endocytosis so LGALS3 would be expected to promote CD44 surface expression [54]. In AML cells with LGALS3 supported CD44 surface expression, CD74 would be predicted to augment signaling mediated by CD44.
    > LGALS3 is well known as an immune regulatory molecule that suppresses host anti-tumor immune surveillance by diverse mechanisms [1,2,55].
    > LGALS3 blocks or at least dampens immune cell function by reducing surface expression of glycosylated T cell receptor in T cells and preventing NK cell receptor binding to antigen [1,2]. LGALS3 has emerged as a critical component in MSC in AML patients to impact response to therapy [56]. It is likely that LGALS3 secreted from MSC and other support cells in the AML microenvironment negatively impacts immune surveillance in AML patients. It is yet to be determined if LGALS3 derived from the leukemia cells plays a role as an immune response inhibitor in AML.
    > LGALS9 is emerging as an important immune checkpoint inhibitor molecule as a TIM-3 binding partner [2,57]. LGALS9 also regulates T cell function as a CD44 binding partner [58]. Whereas LGALS3 binding to CD44 promotes metastasis, LGALS9 binding to CD44 suppresses this process [59,60]. Future RPPA studies to determine the role of LGALS9 and galectins other than LGALS3 are warranted.
    > For the first time, an at risk AML population has been found that is associated with active LGALS3 and active CD74 networks (Fig. 9A and  B). At present, it is unclear which if any proteins within the LGALS3 or CD74 networks is driving this phenomenon. CD44, SPP1, and CLPP are highly induced in the patient cohort with both networks active compared to patients with normal-like state (Fig. 8).
  - Snippet 9 (score: 0.662)
    > While it is unclear how LGALS3 might mechanistically influence leukemic cell recovery and growth after therapy, perhaps regulation of these cellular processes are important in addition to the well documented role of LGALS3 in regulation of cell cycle and cell proliferation [1,2,13,14]. Many of the CD74 network associated biological processes involved immune regulation (Supplemental Table 3) though it is unclear if CD74 network regulates potential immune response in AML. Many of the CD74 network associated biological processes did include those involved in regulation of cell death and apoptosis (Supplemental Table 3). Of the 31 proteins correlated with CD74 expression, 19 are associated with the biological pathway regulation of cell death (GO.0010941) and 16 are associated with the biological pathway negative regulation of apoptotic process (GO.0043066). The raises the question of what the cross-talk is between the LGALS3 and CD74 networks? Gene expression analysis of CD74, CD44, and CLPP in the THP-1 LKO cells versus THP-1 cells with LGALS3 shRNA showed no or only slight changes in these genes (Fig. 7). Protein expression of CD74, CD44, and CLPP were similar in THP-1 LKO and THP-1 LGALS3 shRNA cells (data not shown). While LGALS3 supports AKT activation via RAS, CD74 would be expected to support AKT via MIF mediated signaling involving CD44 and/or CXCR4 [19][20][21][22][23][24][25][26][27]. Though the functional roles of LGALS3 and CD74 in this process are very different, each network would contribute to activation and perhaps may explain why patients with both active networks do so poorly (Fig. 9A  and B). Unfortunately, CXCR4 is not represented in the RPPA panel due to lack of validated antibody. However, CD44 is present and interestingly is most elevated in patients with active LGALS3 network and CD74 network (Fig. 8).

### [2] Comparative Proteomic Profiling of Tumor-Associated Proteins in Human Gastric Cancer Cells Treated with Pectolinarigenin
- Authors: Ho Jeong Lee, Venu Venkatarame Gowda Saralamma, S. Kim, S. Ha, P. Vetrivel et al.
- Year: 2018
- Venue: Nutrients
- URL: https://www.semanticscholar.org/paper/630404664201d86cc15f629d5770143629ee1859
- DOI: 10.3390/nu10111596
- PMID: 30380781
- PMCID: 6265996
- Citations: 18
- Summary: Pectolinarigenin, a natural flavonoid that is present in citrus fruits, has been reported to exhibit antitumor effects in several cancers, and proteomic analysis provides vital information about target proteins that are important for PEC-induced cell death in gastric cancer cells.
- Evidence snippets:
  - Snippet 1 (score: 0.717)
    > In order to understand the biological relevance of PEC regulated proteins, as shown in Figure 10A,B and Table 3, the gene ontology (GO) terms for biological processes were investigated for all identified proteins. The GO results demonstrated that the highest associations were with the biological processes regulation of the epidermal growth factor receptor signaling pathway (GO: 0042058), related cell cycle (GO: 0007049), and negative regulation of endocytosis (GO: 0045806) in PEC-treated AGS cells. Apoptotic process (GO: 0006915), M phase of mitotic cell cycle (GO: 0000087), cell death (GO: 0008219), positive regulation of receptor-mediated endocytosis (GO: 0048260), and positive regulation of macrophage fusion (GO: 0034241) in PEC-treated MKN28 cells.
    > Figure 10. Gene ontology analysis of (A) AGS and (B) MKN28 cells. The pie charts representing the distribution of the identified proteins according to their biological process. Gene ontology analyses of the determined proteins were assigned according to their biological function, using the web-based tool at GeneCodis (http://genecodis.cnb.csic.es).

### [3] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
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
  - Snippet 1 (score: 0.717)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.
  - Snippet 2 (score: 0.676)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly

### [4] Krüppel-like Factor 3 (KLF3/BKLF) Is Required for Widespread Repression of the Inflammatory Modulator Galectin-3 (Lgals3)*
- Authors: Alexander J. Knights, Jinfen. J. Yik, Hanapi Mat Jusoh, Laura J. Norton, Alister P. W. Funnell et al.
- Year: 2016
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/dce84b7faec66ad9234b04f596d036ed32078971
- DOI: 10.1074/jbc.M116.715748
- PMID: 27226561
- Citations: 27
- Influential citations: 1
- Summary: It is shown that the zinc finger transcription factor Krüppel-like factor 3 (KLF3) directly represses galectin-3 transcription, and mechanistic insights into the regulation of Lgals3 are provided, demonstrating that C-terminal binding protein (CtBP) is required to drive optimal KLF3-mediated silencing.
- Evidence snippets:
  - Snippet 1 (score: 0.717)
    > Lgals3 Is Up-regulated in the Absence of KLF3-In studies of the role of KLF3 in hematopoiesis and red blood cell development, microarrays performed on Ter119 ϩ fetal liver cells lacking KLF3 revealed that the Lgals3 gene was consistently up-regulated in knockout animals (15). Because of the importance of galectin-3 in a number of biological settings, we undertook a fuller analysis of whether the expression of Lgals3 was altered in a range of mouse tissues in the absence of KLF3. Lgals3 mRNA levels were assessed in cultured murine embryonic fibroblasts (MEFs) as well as a series of primary tissues from wild-type and Klf3 Ϫ/Ϫ mice by quantitative real-time PCR. In primary and immortalized Klf3 Ϫ/Ϫ MEFs, Lgals3 mRNA was up-regulated 4.7-and 4.3-fold, respectively, compared with wild-type expression (Fig. 1A). Importantly, Lgals3 levels were also found to be elevated in a number of primary tissues dissected from KLF3-deficient mice (Fig. 1B). Derepression was most evident in Klf3 Ϫ/Ϫ subcutaneous (6.7-fold) and epididymal (3.3-fold) white adipose depots and in the heart (6.6-fold) and pancreas (4.2-fold).
    > Following the demonstration that Lgals3 is derepressed in Klf3 Ϫ/Ϫ tissues at the mRNA level, we next sought to determine whether this up-regulation was reflected at the protein level. Whole cell protein extracts were prepared from wild-type and Klf3 Ϫ/Ϫ fat depots and spleens, and the expression of galectin-3 protein was assessed by Western blotting (Fig. 1, C-F).

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
  - Snippet 1 (score: 0.701)
    > Lgals3 has been implicated in the regulation of innate and adaptive immune responses, where it participates in the activation or differentiation of immune cells and contributes to phagocytic clearance of microorganisms and apoptotic cells by macrophages (117,118). Lgals3 has been reported to promote but also to inhibit T-cell apoptosis depending on whether it binds to glycoproteins on the cell surface (CD45 and CD71) or to intracellular ligands (Bcl-2) (119, 120). In the placenta, Lgals3 was detected in all trophoblastic lineages including villous cytotrophoblasts (CTB) and EVT with a reduction of Lgals3 expression observed from the VT to the trophoblastic cell columns (121). This pattern of Lgals3 expression correlates with the switch from a proliferative to a migratory trophoblast phenotype and while placental Lgals3 dysregulation has been associated with some obstetric complications including spontaneous or recurrent miscarriages, further studies are needed to understand its contribution to trophoblast biology (81,122). In addition to trophoblasts, Lgals3 is expressed by maternal decidual cells (73). While showing a different expression pattern, both Lgals1 and Lgals3 have been proposed to play a role in cell-cell and cell-matrix interactions of trophoblast during placentation (121). Studies of the importance of Lgals3 in murine pregnancy by Yang et al. indicate that Lgals3 is expressed in the luminal and glandular epithelium and that an increase in Lgals3 is required for proper embryo implantation (123). In addition, Lgals3 affects chemotaxis and morphology of endothelial cells and stimulates capillary tube formation and angiogenesis in vivo (124). Therefore, besides its proposed roles in embryo implantation, immune regulation and trophoblast-matrix interactions, Lgals3 has a potential role in placental angiogenesis.

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
  - Snippet 1 (score: 0.692)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.

### [7] Identification of an Internal Gene to the Human Galectin-3 Gene with Two Different Overlapping Reading Frames That Do Not Encode Galectin-3*
- Authors: M. Guittaut, Stéphane Charpentier, Thierry Normand, Martine Dubois, J. Raimond et al.
- Year: 2001
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/75ca62f4b6eb66b3bcdac062664da410941fdcaa
- DOI: 10.1074/JBC.M002523200
- PMID: 11160123
- Citations: 37
- Influential citations: 6
- Summary: It is demonstrated that these transcripts arise from an internal gene embedded within LGALS3 and named galig (Galectin-3 internal gene), which appears to be tightly regulated and principally activated in leukocytes from peripheral blood.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > Human Rapid-Scan Gene Expression Panel was used to detect the alternative transcripts in various human tissues using RT-PCR. The primers used were designed to amplify a 923-or 629-bp fragment.
    > LGALS3 transcripts were detected as a 457-bp DNA and actin transcripts as a 640-bp DNA. PCR was performed using 0.25 ng or 2.5 ng (10ϫ) template cDNA.
    > average of other human proteins is 10 times lower. This rich content in tryptophans confers hydrophobic properties that may account for the membrane localization of the ORF2⅐EGFP protein (Fig. 6). Consistent with the mitochondrial localization of the ORF2⅐EGFP fusion protein, this sequence exhibits the common properties of mitochondrial-imported proteins such as the enrichment of arginine, leucine, and serine residues (36).
    > Tissue Specificity of galig Expression-Detection of galig transcripts in HOS cells and colon tumor cells revealed a low expression level. Based on this observation, the rationale that the appearance of galig transcripts may have resulted from a leaky transcription of a cryptic promoter rather than from an independently functioning promoter could not be excluded. Screening of several human tissues indicated clearly that galig is a tightly regulated gene whose expression is most efficient in leukocytes from peripheral blood. The low level of transcription in bone marrow indicates that galig is specifically expressed in mature forms of leukocytes. Whereas the precise quantification of galig mRNA has not been addressed in these experiments, it is clear that these transcripts are much less abundant than LGALS3 transcripts. This may not be surprising considering that LGALS3 is known to be highly expressed when activated (37,38). Indeed, the amount of LGALS3 transcripts appeared as abundant as those from actin genes. This shows a different type of regulation by the galig and LGALS3 promoters. In particular, muscle, stomach, and uterus, although expressing low levels of galig transcripts, revealed no LGALS3 transcripts, thus indicating an independent functioning of the two promoters.

### [8] LGALS3 (galectin 3) mediates an unconventional secretion of SNCA/α-synuclein in response to lysosomal membrane damage by the autophagic-lysosomal pathway in human midbrain dopamine neurons
- Authors: Kevin J. Burbidge, D. J. Rademacher, Jessica E Mattick, Stephanie R. Zack, A. Grillini et al.
- Year: 2021
- Venue: Autophagy
- URL: https://www.semanticscholar.org/paper/cc5e102f7ebd04ebabcf3db8dfc995e5999c4629
- DOI: 10.1080/15548627.2021.1967615
- PMID: 34612142
- PMCID: 9196737
- Citations: 49
- Summary: A human midbrain dopamine (mDA) neuronal culture model is used to provide evidence in support of a cellular mechanism that explains the cell-to-cell transfer of pathological forms of SNCA that are observed in PD and it is demonstrated that LGALS3 (galectin 3) mediates the release of S NCA following vesicular damage.
- Evidence snippets:
  - Snippet 1 (score: 0.682)
    > Galectin recruitment to damaged vesicles leads to their recognition by autophagic adapter proteins and, subsequently, to their degradation via autophagy [25][26][27]. We and others have demonstrated that fibrillar forms of SNCA, MAPT/tau and other amyloids can induce vesicle damage following endocytosis, leading to the recruitment of LGALS3, LGALS8, autophagic adaptors, and effector proteins [6,[28][29][30]. When postmortem brain tissue from five PD patients was stained for LGALS3 and SNCA phosphorylated at serine 129 (p-S129) to identify LBs, a majority of the examined LBs displayed LGALS3 coronas [28]. The presence of LGALS3 in LBs suggests a history of membrane damage.
    > Accumulating evidence reveals that the biological functions of galectin proteins are central to the ALP impairment that occurs in PD and other neurodegenerative diseases [31][32][33][34][35]. The Deretic group demonstrated that the re-localization of LGALS3, LGALS8, and LGALS9 to damaged lysosomal compartments coordinates the cellular autophagic response [36][37][38][39][40]. Specifically, in combination with ULK1, TRIM16 (tripartite motif containing 16), and ATG16L1, LGALS3 facilitates the recruitment of autophagic adaptors, receptors, and effectors to damaged lysosomal membranes [38,40]. A recent genome-wide association study reported that single nucleotide polymorphisms in LGALS3 (gene transcript) are associated with an increased risk of PD [35]. Additionally, increased LGALS3 in the cerebrospinal fluid of PD patients has been reported [31,34,41].
    > Recent studies have also demonstrated that galectins and proteins normally associated with ALP degradation also act to promote an unconventional secretory mechanism referred to as secretory autophagy [39,42,43].

### [9] Beyond Colonoscopy: Exploring New Cell Surface Biomarkers for Detection of Early, Heterogenous Colorectal Lesions
- Authors: Saleh M. Ramezani, Arianna Parkhideh, P. Bhattacharya, M. Farach-Carson, D. Harrington
- Year: 2021
- Venue: Frontiers in Oncology
- URL: https://www.semanticscholar.org/paper/4b48091d0ad86a2121491218707db23e88605000
- DOI: 10.3389/fonc.2021.657701
- PMID: 34290978
- PMCID: 8287259
- Citations: 13
- Summary: This review contextualizes existing and emergent CRC surface biomarkers and assess each’s potential as a candidate marker for early marker-based detection of CRC lesions and presents an overview of recent advances in imaging techniques useful for visual detection of surface biomarker detection.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > Galectin 3, or LGALS3, is a member of the galectin family, a group of carbohydrate-binding lectins characterized by their binding affinity for beta-galactosides (85).
    > LGALS3 is expressed at the cell surface, where it interacts with the extracellular matrix, especially with glycoproteins, and has the ability to affect intracellular signaling pathways (42). LGALS3-expressing cells also possess higher ALDH1 activity, which often correlates with a dedifferentiated cancer stem cell phenotype, than do their LGALS3-negative counterparts (86).
    > The correlation of LGALS3 expression in CRC with clinical pathological characteristics has been explored in several immunohistochemical and RT-PCR studies. In one study, the IHC staining of CRC tissue (n=61) and normal adjacent tissue (n=23) samples showed significantly higher LGALS3 expression in cancer tissue (62.5%) versus normal cancer-adjacent tissue (13.0%) (41). In another study, 75% of CRC tissue samples stain high for LGALS3, and ten CRC cell lines were shown to have increased LGALS3 protein levels compared to HeLa cells (42).
    > LGALS3 expression varies according to cancer staging and the degree of differentiation of the adenocarcinoma. LGALS3 mRNA levels were higher in early stage colorectal cancers (58% in stage I) compared to advanced cancers (50% in stage IV) (43). Protein analysis found higher LGALS3 levels in primary adenocarcinomas than in metastatic adenocarcinomas, and stronger LGALS3 staining in well-differentiated tumor areas compared to poorly differentiated tumor areas (43). Conversely, colorectal adenocarcinomas may display higher levels of LGALS3 than do colorectal adenomas; one study sets the rate of colorectal adenocarcinoma expression of LGALS3 at 95% while only 73% of adenomas were positive for LGALS3 (43).

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
  - Snippet 1 (score: 0.671)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [11] Gene Prioritization for Imaging Genetics Studies Using Gene Ontology and a Stratified False Discovery Rate Approach
- Authors: R. Baldock, A. Ferguson, W. M. Brown, Sejal Patel, M Mallar Chakravarty et al.
- Year: 2016
- Venue: Frontiers in Neuroinformatics
- URL: https://www.semanticscholar.org/paper/9a53e7ac6c4f67e80679c6eb8016c4ccced3d7c9
- DOI: 10.3389/fninf.2016.00014
- PMID: 27092072
- PMCID: 4823264
- Citations: 8
- Influential citations: 1
- Summary: A novel method that utilizes Gene Ontology, an online database, to select and prioritize certain genes, employing a stratified false discovery rate (sFDR) approach to investigate their associations with imaging phenotypes is developed.
- Evidence snippets:
  - Snippet 1 (score: 0.665)
    > Therefore the parent term that is regulated was selected, in this case the term "receptormediated endocytosis, " and the parent term that regulates a biological process but does not specify positive or negative regulation ("regulation of receptor-mediated endocytosis") is removed-shown in a yellow box -because the child term is more specific in terms of explaining how it is regulating the parent term (e.g., negative regulation of receptor-mediated endocytosis), Figure 3C.
    > Step 4: Quick GO was used to extract all the genes that are associated to the OGO terms (as displayed in Figure 4 in green boxes) in the pruned "transport system" network. SNPs from these genes were extracted from the ENIGMA2 and ADNI1 (Supplementary Section 2) dataset using a reference file containing the start and end positions of the transcribed gene portion according to the Homo sapiens build 37 protein and coding genes from National Center for Biotechnology Information (NCBI). This list of SNPs formed the priority list for sFDR.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.