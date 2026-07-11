---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:47:28.019879'
end_time: '2026-06-22T04:47:30.958453'
duration_seconds: 2.94
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-2001237
  hypothesis_text: LGALS3 has negative regulation of extrinsic apoptotic signaling
    pathway (GO:2001237).
  term_context: '- Term: negative regulation of extrinsic apoptotic signaling pathway
    (GO:2001237)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[15]
  source_context_yaml: "term:\n  id: GO:2001237\n  label: negative regulation of extrinsic\
    \ apoptotic signaling pathway\nevidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
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
citation_count: 15
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has negative regulation of extrinsic apoptotic signaling pathway (GO:2001237).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has negative regulation of extrinsic apoptotic signaling pathway (GO:2001237).
Key context:
- Term: negative regulation of extrinsic apoptotic signaling pathway (GO:2001237)
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
- **Hypothesis slug:** function-support-go-2001237
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[15]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:2001237
  label: negative regulation of extrinsic apoptotic signaling pathway
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has negative regulation of extrinsic apoptotic signaling pathwa...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 15
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
  - Snippet 1 (score: 0.870)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.
  - Snippet 2 (score: 0.777)
    > While it is unclear how LGALS3 might mechanistically influence leukemic cell recovery and growth after therapy, perhaps regulation of these cellular processes are important in addition to the well documented role of LGALS3 in regulation of cell cycle and cell proliferation [1,2,13,14]. Many of the CD74 network associated biological processes involved immune regulation (Supplemental Table 3) though it is unclear if CD74 network regulates potential immune response in AML. Many of the CD74 network associated biological processes did include those involved in regulation of cell death and apoptosis (Supplemental Table 3). Of the 31 proteins correlated with CD74 expression, 19 are associated with the biological pathway regulation of cell death (GO.0010941) and 16 are associated with the biological pathway negative regulation of apoptotic process (GO.0043066). The raises the question of what the cross-talk is between the LGALS3 and CD74 networks? Gene expression analysis of CD74, CD44, and CLPP in the THP-1 LKO cells versus THP-1 cells with LGALS3 shRNA showed no or only slight changes in these genes (Fig. 7). Protein expression of CD74, CD44, and CLPP were similar in THP-1 LKO and THP-1 LGALS3 shRNA cells (data not shown). While LGALS3 supports AKT activation via RAS, CD74 would be expected to support AKT via MIF mediated signaling involving CD44 and/or CXCR4 [19][20][21][22][23][24][25][26][27]. Though the functional roles of LGALS3 and CD74 in this process are very different, each network would contribute to activation and perhaps may explain why patients with both active networks do so poorly (Fig. 9A  and B). Unfortunately, CXCR4 is not represented in the RPPA panel due to lack of validated antibody. However, CD44 is present and interestingly is most elevated in patients with active LGALS3 network and CD74 network (Fig. 8).
  - Snippet 3 (score: 0.755)
    > Galectin 3 (LGALS3) is a beta-galactoside binding protein that participates in diverse cellular processes that support cell growth and cell survival [1][2][3][4][5][6][7][8][9]. There are at least fourteen known galectin family members of which ten are found in mammalian cells [1]. There are three families of galectins based on structure but LGALS3 is unique in that it is the only member of the chimeric group [1]. LGALS3 is the only galectin which can form pentamers and this enables the galectin to form lattices and thus participate in endocytotic processes [1].
    > LGALS3 is an excellent example of a molecule that acts as a tumor promoter in the context of the entire tumor microenvironment by promoting survival of malignant cells, supporting metastasis, suppressing immune surveillance, and modulating inflammatory expression of chemokines/cytokines [1][2][3][4][5][6][7][8][9].
    > LGALS3 supports cell survival by diverse mechanisms. The galectin has been shown to associate with BCL2 via a NWGR motif common to both proteins to help the anti-apoptotic molecule support mitochondrial integrity during stress challenge [7][8][9]. LGALS3 also supports cell proliferation via the WNT signaling pathway. LGALS3 can bind beta Catenin and Axin and also supports beta catenin protein stability by promoting Protein Kinase B (AKT) suppression of GSK3 beta [10][11][12].
    > LGALS3 is critical for RAS signaling and thus supports Mitogen Activated Protein Kinase (MAPK) and AKT cascades [1,2,[12][13][14][15][16][17]. LGALS3 positively regulates BCL2 and MCL-1 gene and protein expression in AML cells by supporting both ERK and AKT pathways [1,2,[12][13][14][15][16][17].
  - Snippet 4 (score: 0.755)
    > LGALS3 positively regulates BCL2 and MCL-1 gene and protein expression in AML cells by supporting both ERK and AKT pathways [1,2,[12][13][14][15][16][17]. Suppression of LGALS3 by shRNA or with GCS-100 (an inhibitor of LGALS1 and LGALS3) blocks both AKT and ERK signaling pathways [15,17].
    > LGALS3 regulated pathways are involved in expression of genes and protein associated with cancer stem cells (CSC) and thus the galectin likely supports CSC [9]. Recent data suggests that LGALS3 supports malignant cell survival in AML [6,15,18]. In a cohort of Taiwanese AML patients, Cheng and colleagues reported that elevated LGALS3 mRNA was prognostic for poor survival outcome [18]. However, in that study the impact of LGALS3 protein expression or associations of the galectin with potential LGALS3 target proteins was not examined.
    > CD74 (also known as the invariant chain protein) is best known as a chaperone for major histocompatibility (MHC) Class II molecules involved in antigen presentation [19,20]. In addition to mediating MHC Class II molecule endocytosis, CD74 protects these molecules from proteolysis [19][20][21]. CD74 also has MHC Class II independent functions that involve the pro-inflammatory cytokine macrophage inhibitory factor (MIF) and cell surface signaling molecules CD44 and CXCR4 [19][20][21]. CD74 was found to bind MIF but CD74 alone is unable to initiate MIF signaling which requires either CD44 or CXCR4 [19][20][21][22][23]. CD74 dependent MIF signaling pathways include ERK, JNK, and AKT [24][25][26][27]. CD74 dependent MIF signaling has been shown to suppress p53 function and to activate NF kappa B [26,28].
  - Snippet 5 (score: 0.754)
    > The role of other galectins such as LGALS1 in AML biology is not clear.
    > LGALS1 may substitute for some LGALS3 functions particularly those involved in survival pathways as knock down of either LGALS1 or LGALS3 sensitized AML cells to BH3 mimetic drugs [15]. The failure of LGALS3 suppression to affect many of the RPPA identified proteins with the exception of PPP2R2A/B/C/D (Fig. 5) may reflect LGALS1 activity in these cells that may not be present in the primary AML cells. It is possible that many of the LGALS3 network proteins act to regulate LGALS3 rather than being regulated by the galectin. It is also possible that LGALS3 and some of the LGALS3 network proteins are subject to regulation by a yet unidentified common regulator(s). Further examination of the mechanism regulating the LGALS3 network is ongoing.
    > Network analysis from the data identifies a new extremely poor prognosis group based on the interaction between the LGALS3 and CD74 associated protein networks revealing potential biological pathways that may be critical in supporting AML cell survival. AML patients with both networks active are 8.5% of patients in the study (Fig. 9A) and thus this group may represent a sizeable population of AML patients. It is possible the two proteins regulate independent survival pathways that may have a synergistic effect on survival when both are active. The top ten biological processes associated with LGALS3 network include processes associated with cell metabolism (GO:0031325; GO:0032268; and GO:0032270), cell migration (GO:0030355), and response to growth factor stimulus (GO:0071363) and response to chemical stimulus (GO:0070887) (Supplemental Table 1). While it is unclear how LGALS3 might mechanistically influence leukemic cell recovery and growth after therapy, perhaps regulation of these cellular processes are important in addition to the well documented role of LGALS3 in regulation of cell cycle and cell proliferation [1,2,13,14].

### [2] Parthenolide leads to proteomic differences in thyroid cancer cells and promotes apoptosis
- Authors: Meng Cui, Zhe Wang, Letao Huang, Jia-He Wang
- Year: 2022
- Venue: BMC Complementary Medicine and Therapies
- URL: https://www.semanticscholar.org/paper/7f36ac62e89f19c15f02a3e0b01306e4f458dd67
- DOI: 10.1186/s12906-022-03579-0
- PMID: 35366876
- PMCID: 8977004
- Citations: 11
- Summary: Parthenolide may influence the biological behavior of human thyroid cancer cells by affecting the expression of proteins related to cell metabolism and DNA replication, leading to an anti-proliferative effect.
- Evidence snippets:
  - Snippet 1 (score: 0.830)
    > The above experiments confirmed that PTL can induce apoptosis of BCPAP cells, and in the proteomics clustering results, 6 proteins (IL1B, ITGA6, CASP8, GCLM, HMOX1 and HSPA1A) were classified into 'negative regulation of extrinsic apoptotic signaling pathway' (GO: 2001237). After bioinformatics screening, three were selected to further verify expression differences by PRM. HMOX1 and GCLM were up-regulated and IL1B was down-regulated in BCPAP cells treated with PTL (Fig. 7).

### [3] Dual RNA Sequencing Reveals Key Events When Different Giardia Life Cycle Stages Interact With Human Intestinal Epithelial Cells In Vitro
- Authors: L. Rojas, Jana Grüttner, S. Ma'ayeh, Feifei Xu, S. Svärd
- Year: 2022
- Venue: Frontiers in Cellular and Infection Microbiology
- URL: https://www.semanticscholar.org/paper/a07b7add52e16b284f33a3757df71a8f8338df7b
- DOI: 10.3389/fcimb.2022.862211
- PMID: 35573800
- PMCID: 9094438
- Citations: 12
- Influential citations: 1
- Summary: It is shown that different life cycle stages of Giardia induce different gene expression responses in the host cells and that the IECs in turn differentially affect the gene expression in trophozoites and early encysting cells.
- Evidence snippets:
  - Snippet 1 (score: 0.816)
    > Studies of giardiasis patients have shown an increased number of apoptotic cells in the duodenum (Troeger et al., 2007). Recent studies of Giardia-host cell interactions using 3D stem cellenriched organoid cultures from human duodenal biopsies and WB trophozoites show induction of apoptosis after 48 h interaction (Holthaus et al., 2021). WB parasites of all life-cycle stages up-regulate pro-apoptotic and anti-apoptotic genes (Table S1). This ambiguity was first observed when Giardia WB trophozoite-Caco-2 interactions were studied using microarrays (Roxström-Lindquist et al., 2005), and it was also observed during GS trophozoite infection of Caco-2 cells (Ma'ayeh et al., 2018). Differentially transcribed apoptosis-related genes are listed in Figure S4. Both intrinsic and extrinsic apoptosis pathway genes were identified as DEGs during infection. GO term enrichment analysis showed that the regulation of apoptotic process (GO:0042981) was enriched in up-regulated DEGs during all 3 time-points from all three life cycle stages. Extrinsic apoptosis pathway genes were differentially expressed (e.g., TNFRSF10A, B, and D) and GO term enrichment showed that tumor necrosis factor-mediated signaling pathway (GO:0033209) and negative regulation of extrinsic apoptotic signaling pathway (GO:2001237) were enriched for in the DEGs. This is in line with a recent report (Liu et al., 2020b) showing that Giardia trophozoites can activate CASP3/8 signaling pathways via activation of TNFR1 and K63 deubiquitination of RIP1, which in turn is caused by up-regulation of CYLD and A20. GO term enrichment analysis also detected the term intrinsic apoptotic signaling pathway in response to endoplasmic reticulum stress (GO:0070059).

### [4] Microarray assay of circular RNAs reveals cicRNA.7079 as a new anti-apoptotic molecule in spinal cord injury in mice.
- Authors: Ying Yao, Jingyu Wang, T. He, Heyangzi Li, Jue Hu et al.
- Year: 2020
- Venue: Brain research bulletin
- URL: https://www.semanticscholar.org/paper/8e327ffbb4c66488f7c21b3dc5f8bcd5321ffdae
- DOI: 10.1016/j.brainresbull.2020.08.004
- PMID: 32882320
- Citations: 24
- Summary: The anticipation of anti-apoptosis circRNA 7079 may provide potential research targets for SCI in mice and contribute to new insights into the mechanism of apoptosis after SCI.
- Evidence snippets:
  - Snippet 1 (score: 0.773)
    > the expression of downstream target genes. Our current study Our current study verified that lgals3 is the downstream target of the cicRNA.7079-mmu-miR-6953-5p axis. To date, the mechanisms of the regulation of lgals3 expression in CNS were barely known. In this study, we identified a new regulatory mechanism of lgals3 expression in motor neurons. The previous study reported that lgals3 was increased on day 14 after SCI in rats' spinal cord (Chih-Yen et al., 2011). In line with that, lgals3 was increased at day 3 after SCI in mice spinal cord in our study. Lgals3, has been described as a mediator of apoptosis. The anti-apoptotic role of lgals3 has been was demonstrated in peritoneal macrophages (Hsu et al., 2000), myocardial cells (Al-Salam et al., 2020), and melanoma cells (Wang et al., 2019a). Our study provided evidence that the anti-apoptotic effect of cicRNA.7079 was mediated by mmu-miR-6953-5p -lgals3 axis in motor neurons. Lgals3 containing the anti-death Asp-Trp-Gly-Arg (NWGR) motif, plays an anti-apoptotic effect possibly through its interaction with Bcl-2 family members, Akt-1, NF kappa-B, beta-cateninn, and cathepsin D proteins (Yang et al., 1996;Al-Salam et al., 2020;Akahani et al., 1997). Therefore, the detailed mechanism by which lgals3 regulates apoptosis in motor neurons needs to be further investigated.
    > Recently, circRNA expression profile in rat spinal cord at 6 h after SCI was identified by RNA-seq finding out that 99 circRNAs were up- Fig. 6. The apoptosis-related ceRNA network analysis. The top 30 apoptosis-related circRNAs were plotted as triangles. LncRNAs were plotted as rectangles. miRNAs were plotted as V-shapes.

### [5] Identification of programmed cell death-related genes and diagnostic biomarkers in endometriosis using a machine learning and Mendelian randomization approach
- Authors: Ziwei Xie, Yue He, Yuxin Feng, Xiaohong Wang
- Year: 2024
- Venue: Frontiers in Endocrinology
- URL: https://www.semanticscholar.org/paper/a437f1ce179ac605a4b4d5733d5e488db5fbabe5
- DOI: 10.3389/fendo.2024.1372221
- PMID: 39149122
- PMCID: 11324423
- Citations: 15
- Influential citations: 3
- Summary: This study systematically elucidated the molecular characteristics of PCD in EM and identified TNFSF12, AP3M1, and PDK2 as key biomarkers, providing new directions for the early diagnosis and personalized treatment of EM.
- Evidence snippets:
  - Snippet 1 (score: 0.748)
    > Functional annotation and pathway enrichment analyses were performed on the DPGs. The results of the GO enrichment analysis indicate that these genes are involved in multiple signaling pathways associated with PCD (Figure 2D). The pathways encompassed are the intrinsic apoptotic signaling pathway, regulation of apoptotic signaling pathway, regulation of autophagy, macroautophagy, intrinsic apoptotic signaling pathway triggered by DNA damage, extrinsic apoptotic signaling pathway, mitochondrial structure organization, apoptotic mitochondrial changes, negative regulation of apoptotic signaling pathway, and regulation of intrinsic apoptotic signaling pathway. The KEGG pathway enrichment analysis (Figure 2E) indicated that these genes are involved in pathways, such as lysosome, apoptosis, autophagy, and necroptosis.

### [6] Identification and Characterization of Non-Coding RNAs in Thymoma
- Authors: Guanglei Ji, R. Ren, Xichao Fang
- Year: 2021
- Venue: Medical Science Monitor : International Medical Journal of Experimental and Clinical Research
- URL: https://www.semanticscholar.org/paper/e0ad5ef5a9e860f17008417de010a1dc1b91e301
- DOI: 10.12659/MSM.929727
- PMID: 34219124
- PMCID: 8268976
- Citations: 15
- Influential citations: 2
- Summary: A network analysis of the lncRNA-mRNA-miRNA regulation axes identified a cluster of miRNAs upregulated in thymomas, that can trigger the expression of target protein-coding genes, and lead to the disruption of several biological pathways, including the PI3K-Akt signaling pathway, FoxO signaling pathways, and HIF-1 signaling pathway.
- Evidence snippets:
  - Snippet 1 (score: 0.740)
    > We constructed an lncRNA-mRNA-miRNA regulation network based on the gene co-expression correlation analysis between DELs, mRNAs, and DEMs identified in thymomas (Figure 7). In this network, the upregulated miRNA hsa-let-7a-3 exhibits interactions with 8 protein-coding genes (INSR, IGF1, IL10, IGF1R, ITGB3, COL5A2, ZNF322, PXDN, TGFBR1) and can increase their expressions. The majority of target genes of DELs and DEMs are enriched in several biological pathways, including the PI3K-Akt signaling pathway (P value=0.0), the FoxO signaling pathway (P value=0.0), the HIF-1 signaling pathway (P value=0.0), the proteoglycans in cancer (P value=0.01), and other cancer pathways (P value=0.01), the Supplementary Table 2 shows these details. Most target genes were associated with various GO terms, including immune response (GO: 0006955), hepatic immune response (GO: 0002384), positive regulation of DNA replication (GO: 0045740), positive regulation of cell proliferation (GO: 0008284), positive regulation of MAPK cascade (GO: 0043410), positive regulation of DNA replication (GO: 0045740), positive regulation of cell proliferation (GO: 0008284), negative regulation of extrinsic apoptotic signaling pathway (GO: 2001237), and negative regulation of apoptotic process (GO: 0043066). Supplementary Table 3 shows these details. Our network and pathway analyses show the overexpression of miRNA clusters activates the PI3K-Akt/FoxO/HIF-1/Rap-1 signaling pathway, suggesting that PI3K/Akt/HIF-1/ Rap-1 inhibitors may be therapeutic targets for thymoma patients. The hsa-let-7a family of miRNAs is thought to inhibit migration, invasion, and tumor growth by targeting the AKT2   e929727-12

### [7] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
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
  - Snippet 1 (score: 0.738)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly
  - Snippet 2 (score: 0.723)
    > To delineate the driving mechanism of LGALS3 for the malignant progression of HCC, the KEGG and GO analysis was conducted.The volcano plot and heatmap showed significantly differentially expressed genes between LGALS3 high-and low-expression groups (Figure S3A-B).The KEGG pathway analysis revealed that these LGALS3-related genes were enriched in the IL-17 signaling pathway, ECM-receptor interaction pathway, central carbon metabolism in cancer pathway, leukocyte transendothelial migration pathway and PI3K-Akt signaling pathway.Meanwhile, the GO analysis revealed that these genes were strongly associated with cell chemotaxis, leukocyte chemotaxis, regulation of leukocyte migration, as well as regulation of chemotaxis (Fig. 5A).Accumulating evidence has proven the immune system has an essential role in malignancy pathogenesis [17], and LGALS3 is closely correlated with CD163 + tumor-associated macrophages (TAM) in glioma [10].Therefore, we studied the association between LGALS3 level and the immune infiltration level in HCC.There was no statistical difference in immune cell infiltration levels over a number of LGALS3 copy numbers (Fig. 5B).Meanwhile, immune infiltration analysis revealed that expression of LGALS3 showed a significant positive association with several immune cell populations, involving CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, dendritic cell, as well as cancer-associated fibroblasts (CAFs) within HCC (Fig. 5C-E).Based on these results, we further evaluated the immune score in HCC patients with high and low LGALS3 expression.The scores of immune cells, including CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, and dendritic cell, were significantly higher in the high LGALS3 expression groups, as shown in Fig. 5F.Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].

### [8] Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins
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
  - Snippet 1 (score: 0.731)
    > Lgals3 has been implicated in the regulation of innate and adaptive immune responses, where it participates in the activation or differentiation of immune cells and contributes to phagocytic clearance of microorganisms and apoptotic cells by macrophages (117,118). Lgals3 has been reported to promote but also to inhibit T-cell apoptosis depending on whether it binds to glycoproteins on the cell surface (CD45 and CD71) or to intracellular ligands (Bcl-2) (119, 120). In the placenta, Lgals3 was detected in all trophoblastic lineages including villous cytotrophoblasts (CTB) and EVT with a reduction of Lgals3 expression observed from the VT to the trophoblastic cell columns (121). This pattern of Lgals3 expression correlates with the switch from a proliferative to a migratory trophoblast phenotype and while placental Lgals3 dysregulation has been associated with some obstetric complications including spontaneous or recurrent miscarriages, further studies are needed to understand its contribution to trophoblast biology (81,122). In addition to trophoblasts, Lgals3 is expressed by maternal decidual cells (73). While showing a different expression pattern, both Lgals1 and Lgals3 have been proposed to play a role in cell-cell and cell-matrix interactions of trophoblast during placentation (121). Studies of the importance of Lgals3 in murine pregnancy by Yang et al. indicate that Lgals3 is expressed in the luminal and glandular epithelium and that an increase in Lgals3 is required for proper embryo implantation (123). In addition, Lgals3 affects chemotaxis and morphology of endothelial cells and stimulates capillary tube formation and angiogenesis in vivo (124). Therefore, besides its proposed roles in embryo implantation, immune regulation and trophoblast-matrix interactions, Lgals3 has a potential role in placental angiogenesis.

### [9] Identification of Oncosuppressing Effects of Seven Selenoproteins in Thyroid Cancer: Implications for Distinct Roles of Selenoproteins in Tumorigenesis
- Authors: Yang Zhao, Pu Chen, Hong-jun Lv, Yuan Wu, Shu Liu et al.
- Year: 2021
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/13df7e615ebc2fa71ed470d2f3a02f8a65b931ef
- DOI: 10.21203/RS.3.RS-402154/V1
- Summary: This study confirms the distinct roles of the 25 selenoproteins in thyroid cancer pathogenesis, providing useful information to uncover the currently unknown functions of seleniproteins and open up the possibility for targeted regulation of individual selenobroteins for treatment of thyroid cancer.
- Evidence snippets:
  - Snippet 1 (score: 0.730)
    > KEGG analysis identi ed 8 pathways related to SELENOO in thyroid cancers, including hsa03013: RNA transport, hsa04668: TNF signaling pathway, hsa04550:
    > Signaling pathways regulating pluripotency of stem cells, hsa04141: Protein processing in endoplasmic reticulum, hsa04110: Cell cycle, hsa04144: Endocytosis, hsa00240: Pyrimidine metabolism, and hsa00230: Purine metabolism (Table 2).
    > With regards to SELENOV, 22 biological processes including GO:0055085 (transmembrane transport) and GO:0055114 (oxidation-reduction process) were enriched in the top 200 SELENOV-positive-correlated genes and 35 biological processes including GO: 0098609 (cell-cell adhesion), GO:0042060 (wound healing), GO: 0007155 (cell adhesion) and GO: 2001237 (negative regulation of extrinsic apoptotic signaling pathway) were enriched in the top 200 SELENOV-negatively-correlated genes by GO analysis (Table S13). The top 5 processes on each list were shown in Fig. 4F. In addition, 8 pathways including hsa04931: Insulin resistance, hsa04920: Adipocytokine signaling pathway, hsa04520: Adherens junction, hsa05205: Proteoglycans in cancer, hsa04512: ECM-receptor interaction, hsa05200: Pathways in cancer, hsa04390: Hippo signaling pathway, and hsa05412: Arrhythmogenic right ventricular cardiomyopathy (ARVC) were identi ed to be correlated with SELENOV (Table 2).

### [10] Bioinformatics-Based Identification of a circRNA-miRNA-mRNA Axis in Esophageal Squamous Cell Carcinomas
- Authors: Zhaojun Wang, Haifeng Li, Fajun Li, Xin Su, Junhang Zhang
- Year: 2020
- Venue: Journal of Oncology
- URL: https://www.semanticscholar.org/paper/d2dff21c189100a75d23e26ee2a4eef452807b2d
- DOI: 10.1155/2020/8813800
- PMID: 33061972
- PMCID: 7542503
- Citations: 13
- Influential citations: 1
- Summary: Support is provided for the possible mechanisms of disease progression in ESCC by discovering differentially expressed nonprotein-coding RNAs and genes with potential prognostic relevance in ES CC.
- Evidence snippets:
  - Snippet 1 (score: 0.711)
    > Genes.KEGG enrichment and GO analyses were performed for the target genes of the two DEMs (Figure 2).In the BP category, the "extrinsic apoptotic signaling pathway in absence of ligand," "negative regulation of anoikis," and "negative regulation of apoptotic process" were enriched.While "protein binding" was enriched according to the MF category, enrichment of the "nucleoplasm," "nucleus," and "cytosol" was shown in the CC category (Figure 3(b)).e KEGG pathway analysis revealed enrichment of the "focal adhesion," "estrogen signaling," "sphingolipid signaling," and "PI3K-Akt signaling" pathways (Figure 3(a)).

### [11] A Network Pharmacology Approach to Understanding the Mechanisms of Action of Traditional Medicine: Rheum L. for Diabetic Kidney Disease
- Authors: Jin Luo, C. Piao, De Jin, Li Wang, Xiaohua Zhao et al.
- Year: 2020
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/97072294d3d8475989fea00468baf914f0e68111
- DOI: 10.21203/rs.3.rs-76167/v1
- Summary: A network pharmacology-based strategy was proposed to elucidate the underlying multi-component, multi-target, and multi-pathway mode of action of Rheum L. in the treatment of diabetic kidney disease using a systems pharmacology approach.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > The 11 biological processes were mainly involved in in ammatory response, apoptosis, brosis, and peripheral circulation. The details are shown in Fig. 7. The processes were, in the aspect of cell proliferation: positive regulation of transcription from RNA polymerase II promoter (GO:0045944), positive regulation of cell proliferation (GO:0008284), transmembrane receptor protein tyrosine kinase signaling pathway (GO:0007169), and transcription, DNA-templated (GO:0006351);in the aspect of protein metabolism: negative regulation of protein binding (GO:0032091) and positive regulation of protein binding (GO:0032092); in the aspect of in ammatory response: response to oxidative stress (GO:0006979); in the aspect of apoptosis: negative regulation of extrinsic apoptotic signaling pathway (GO:2001237); and in the aspect of peripheral circulation regulation: glucose homeostasis(GO:0042593), regulation of blood pressure(GO:0008217), and blood coagulation(GO:0007596). Based on these ve main aspects, a complex multi-path synergetic effect may be the cause of the effect of Rheum L. on DKD.

### [12] Galectin-3 aggravates microglial activation and tau transmission in tauopathy
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
  - Snippet 1 (score: 0.710)
    > Interestingly, the 812 GAM genes shared 172 genes with the AD DAM genes (23) (Supplemental Figure 17A), including upregulated microglial activation genes (such as Clec7a, Cd68, Csf1, Apoe, and Cybb) and downregulated microglial homeostatic genes (such as P2ry12, TMEM119, Csf1r, Hexb, and Slc2a5). Collectively, GAM is a subset of microglia with several features similar to those of DAM (e.g., the enhanced inflammatory responses and protein translation processes) and some unique only to GAM (including the protein folding process, energy metabolism, transcription, and specific translation processes) (Figure 4L and Supplemental Figure 17,  B-F). Additionally, we conducted a comparative analysis between GAM in Tau22 mice and the DEGs in pTau-induced iMGLs, as well as the effects of Gal3 inhibition with TD139, to explore their potential relevance for future cross-species studies. Among the identified conservation of canonical pathways, pathways such as hepatic fibrosis signaling, Rho family GTPases, neuroinflammation, integrin, and IL8 signaling, were suppressed in the presence of TD139 (Supplemental Figure 18, A and B).
    > Loss of Gal3 protects against tauopathy. To assess the importance of Gal3 in tauopathies in vivo, we crossed Tau22 mice with Gal3 knockout mice (Tau22/Lgals3 -/-, Figure 5A). The knockout of findings suggest that the Lgals3-enriched Cluster 9 may play a pivotal role in pathways associated with EVs as evidenced by the iMGL study, and may potentially contribute to the intricate interplay between microglial activity and tau transmission.
    > Because not all microglia express Lgals3, we aimed to specifically characterize the Lgals3-positive and Lgals3-negative microglia. We define Lgals3-positive microglia as cells with Lgals3 expression levels greater than or equal to 1 average log Unique Molecular Identifier (UMI) count, which serves as a reference point.

### [13] Lgals3 Promotes Calcium Oxalate Crystal Formation and Kidney Injury Through Histone Lactylation‐Mediated FGFR4 Activation
- Authors: Zehua Ye, Yushi Sun, Songyuan Yang, Lei Li, Bojun Li et al.
- Year: 2025
- Venue: Advanced Science
- URL: https://www.semanticscholar.org/paper/adbfa30b5832407d200a5eade9196d41be08050e
- DOI: 10.1002/advs.202413937
- PMID: 39903812
- PMCID: 11947994
- Citations: 18
- Summary: Findings suggest that Lgals3 may play a key role in CaOx stone formation and kidney injury by interacting with PKM2 and promoting both H3K18la‐mediated gene transcription and activation.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > [23] The result of the present study revealed that Lgals3 exhibited several novel functions and mechanisms in the formation of kidney stones and the development of renal fibrosis (Figure 13). It was found that Lgals3 was highly expressed in CaOx crystal deposition and stimulated the activation of glycolysis during crystal deposition and renal fibrosis. Knockout or pharmacological inhibition of Lgals3 demonstrated a significant reduction of crystal deposition and renal fibrosis. In addition, IP-MS analysis identified PKM2, a key molecule in the regulation of glycolytic function, as the direct binding target of Lgals3. Furthermore, this study integrated analyses of CUT&Tag and RNA-seq and demonstrated that Lgals3mediated histone lactylation promoted FGFR4 expression during the formation of CaOx stones and renal fibrosis. [24] Lgals3 is considered a disease-associated biomarker and it is significantly increased in cases of acute myocardial infarction or AKI. [25,26] urthermore, recent investigations have shown that it has significant potential as a therapeutic target for various inflammatory and fibrotic illnesses, including lung or kidney fibrosis. [27] n this study, it was found that Lgals3 expression was increased in both mouse and human CaOx crystal kidney tissues. This study utilized Lgals3 −/-mice and demonstrated that Lgals3 deficiency alleviated CaOx crystal deposition and renal fibrosis. The deposition of CaOx crystals and the development of renal fibrosis are complex processes regulated by numerous genes and signaling pathways. RNA-seq and 4D-DIA proteomics were performed to detect alterations in mRNA and protein expression in Lgals3-deficient cells under COM stimulation. The KEGG analysis showed that Lgals3 deficiency primarily enriched metabolicrelated pathways, specifically glycolysis. When cells are exposed to various stimuli, the mitochondrial energy metabolism undergoes alterations, leading to significant activation of glycolysis, which in turn increases the overall energy supply. [28]

### [14] Characteristics of the PI3K/AKT and MAPK/ERK pathways involved in the maintenance of self-renewal in lung cancer stem-like cells
- Authors: Jingyuan Li, Jianyu Wang, D. Xie, Qin Pei, Xue Wan et al.
- Year: 2021
- Venue: International Journal of Biological Sciences
- URL: https://www.semanticscholar.org/paper/9302948464800646b146c0b29b812d6771909340
- DOI: 10.7150/ijbs.57871
- PMID: 33867839
- PMCID: 8040472
- Citations: 38
- Influential citations: 2
- Summary: A clinically relevant CSCs enrichment recognition model is constructed and a new insight is uncovered that PI3K/AKT and MAPK/ERK pathways as oncogenic signaling pathway and/or stem cell signaling pathway act distinctively and synergistically to regulate lung C SCs self-renewal.
- Evidence snippets:
  - Snippet 1 (score: 0.703)
    > We firstly evaluated the enrichment relationship between the stemness score and key molecules of PI3K/AKT pathway involving PIK3CA, AKT1, mTOR and MAPK/ERK pathway involving MAP2K1, MAP2K2, MAPK1 and MAPK3 (Figure 3A-B). The KEGG enrichment analysis revealed that PI3K/AKT pathway was markedly enriched in high stemness score group (Figure 3B, P < 0.05). Moreover, we conducted GO analysis to uncover the most valuable 10 clusters of enriched sets closely associated with proliferation, differentiation, apoptosis, as well as stemness and carcinogenicity characteristics. Notably, in the high stemness score group, the PI3K/AKT was significantly enriched in the biological process categories of negative regulation of stem cell differentiation, apoptotic process involved in morphogenesis, stem cell division, etc. (Figure 3C). And the MAPK/ERK pathway was enriched in positive regulation of extrinsic apoptotic signaling pathway, intrinsic apoptotic signaling pathway in response to DNA damage by p53 class mediator, negative regulation of intrinsic apoptotic signaling pathway, etc. (Figure 3D). Whereas, in the low stemness score group, PI3K/AKT pathway was enriched in regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway, regulation of mitochondrial membrane permeability involved in apoptotic process, positive regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway, etc. (Figure 3E). MAPK/ERK pathway was enriched in regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway, regulation of mitochondrial membrane permeability involved in apoptotic process, regulation of oxidative stress induced intrinsic apoptotic signaling pathway, etc. (Figure 3F). As for the crosstalk enrichment of these two pathways, PI3K/AKT pathway combined with MAPK/ERK pathway in high stemness score group were enriched in regulation of stem cell differentiation, negative regulation of intrinsic apoptotic signaling pathway, negative regulation of extrinsic apoptotic signaling pathway, etc. (Figure 3G).

### [15] A Preliminary Study to Investigate the Genetic Background of Longevity Based on Whole-Genome Sequence Data of Two Methuselah Dogs
- Authors: Dávid Jónás, Sára Sándor, K. Tátrai, B. Egyed, E. Kubinyi
- Year: 2020
- Venue: Frontiers in Genetics
- URL: https://www.semanticscholar.org/paper/3ac24db3f845e1915648e0d3a75f2c0ff22d5ae1
- DOI: 10.3389/fgene.2020.00315
- PMID: 32373156
- PMCID: 7176982
- Citations: 6
- Summary: A possible link between extreme longevity and the regulation of gene transcription/translation, which hypothesis should be further investigated in the future and could define an interesting direction for future research aiming to better understand longevity.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > Three example genes with missense mutations in protein domains as well as with some of the related GO terms are listed below:
    > 1. ENSCAFG00000003004: negative regulation of cell growth, negative regulation of apoptotic process; 2. ENSCAFG00000004892: regulation of apoptotic process, positive regulation of extrinsic apoptotic signaling pathway; 3. ENSCAFG00000019380: calcium ion transport, regulation of heart contraction, regulation of blood pressure, modulation of chemical synaptic transmission.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.