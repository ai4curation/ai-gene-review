---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:45:38.988783'
end_time: '2026-06-22T04:45:42.404046'
duration_seconds: 3.42
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0031012
  hypothesis_text: LGALS3 has extracellular matrix (GO:0031012).
  term_context: '- Term: extracellular matrix (GO:0031012)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[1]
  source_context_yaml: "term:\n  id: GO:0031012\n  label: extracellular matrix\nevidence_type:\
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
citation_count: 16
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has extracellular matrix (GO:0031012).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has extracellular matrix (GO:0031012).
Key context:
- Term: extracellular matrix (GO:0031012)
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
- **Hypothesis slug:** function-support-go-0031012
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[1]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0031012
  label: extracellular matrix
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has extracellular matrix (GO:0031012). Gene/protein: LGALS3. Or...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 16
- Snippets retrieved: 20

## Relevant Papers

### [1] Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice
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
  - Snippet 1 (score: 0.870)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.
  - Snippet 2 (score: 0.808)
    > We previously observed that genomic loss of galectin-3 (Gal-3; encoded by Lgals3) in mice has a significant protective effect on age-related bone loss. Gal-3 has both intracellular and extracellular functionality, and we wanted to assess whether the affect we observed in the Lgals3 knockout (KO) mice could be attributed to the ability of Gal-3 to bind glycoproteins. Mutation of a highly conserved arginine to a serine in human Gal-3 (LGALS3-R186S) blocks glycan binding and secretion. We generated mice with the equivalent mutation (Lgals3-R200S) and observed a subsequent reduction in Gal-3 secretion from mouse embryonic fibroblasts and in circulating blood. When examining bone structure in aged mice, we noticed some similarities to the Lgals3-KO mice and some differences. First, we observed greater bone mass in Lgals3-R200S mutant mice, as was previously observed in Lgals3-KO mice. Like Lgals3-KO mice, significantly increased trabecular bone mass was only observed in female Lgals3-R200S mice. These results suggest that the greater bone mass observed is driven by the loss of extracellular Gal-3 functionality. However, the results from our cortical bone expansion data showed a sex-dependent difference, with only male Lgals3-KO mice having an increased response, contrasting with our earlier study. These notable sex differences suggest a potential role for sex hormones, most likely androgen signaling, being involved. In summary, our results suggest that targeting extracellular Gal-3 function may be a suitable treatment for age-related loss of bone mass.
    > Galectin-3 (Gal-3; encoded by Lgals3) is a protein that functions outside the cell to regulate glycoprotein secretion and turnover [1,2] and intracellularly in protein chaperoning and mRNA splicing [3,4]. We previously found that genomic deletion of Gal-3 in mice (Lgals3-KO) protects the mice against age-related [5] or sex-hormone deprivation bone loss [6]. A better understanding of the
  - Snippet 3 (score: 0.804)
    > expansion in males) likely reflect the role of extracellular Gal-3 loss in increasing bone mass. Conversely, the differences between the two models (tissue stiffness and lack of female cortical bone expansion) could reflect the role of intracellular Gal-3.
    > The female dominance of the cortical bone expansion in Lgals3-KO mice was further supported using a separate Lgals3 null allele (Lgals3-Δ), where females once again had significantly increased trabecular and cortical bone mass at 36 weeks, but male Lgals3-Δ had slight reductions in both cortical and trabecular bone mass. The apparent sex-dependency of the bone phenotype was most likely due to diminished bone mass accrual in Lgals3-KO males before 12 week of age [5,41], which led us to speculate that Lgals3-KO mice might have reduced androgen-induced cortical bone expansion during puberty [42].
    > However, in Lgals3-R200S mice, we observed a male dominant phenotype in cortical bone expansion. Our gonadectomy study suggested that global loss of Gal-3 may lead to reduced bioavailability of androgens [6]. This would reduce the ability of androgen to support bone mass accrual during puberty [42]. Altered sexhormone regulation in the Lgals3-KO mother during fetal development might also explain why a different skeletal phenotype (increased age-related bone loss) has been reported when comparing Lgals3-KO mice to litters of background matched wildtype-mice [43]. Studies looking at systemic changes in hormones and growth factors in Lgals3-KO and Lgals3-R200S mice would help answer this question. In addition, conditional knockout of Lgals3 at later developmental stages, such as pre-and postpuberty or in aged mice, and studies of pre-and postpubescent Lgals3-R200S mouse cortical bone growth, will further clarify the timing of when extracellular Gal-3 affects bone mass expansion. Values are expressed as mean AE SEM (n = 7-14); Holm-Sidak post-

### [2] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
- Authors: Tammy R. Chaudoin, S. Bonasera
- Year: 2018
- Venue: BMC Neuroscience
- URL: https://www.semanticscholar.org/paper/613a09b176431cdca195e6b3c439b4edbe4f92af
- DOI: 10.1186/s12868-018-0428-x
- Summary: P perturbation of behavioral circadian rhythms in Lgals3−/− mice is noted, with mice at both ages demonstrating greater variability in day-to-day performance of feeding, drinking, and movement compared to wildtype.
- Evidence snippets:
  - Snippet 1 (score: 0.823)
    > Galectins are an evolutionarily ancient family of proteins sharing a high binding affinity for carbohydrates with β-galactoside linkages. In the extracellular space, galectins interact (through a conserved carbohydrate recognition domain, aka CRD) with glycosylated proteins to mediate both cell-to-cell interactions and cell-to-matrix adhesion. Galectins are thus pattern recognition molecules specialized to distinguish carbohydrate moieties.
    > Within the galectin family, galectin-3 (also known as Lgals3) has unique properties. Its preferred ligand is N-acetyllactosamine [1]. It is also the only galectin containing a conserved N-domain as well as a single CRD domain. This N-domain allows Lgals3 not bound to a carbohydrate target to form multimeric complexes [2].
    > In this manner, low extracellular Lgals3 concentrations tend to inhibit extracellular interactions and adhesion [3], while high Lgals3 extracellular concentrations facilitate cellular adhesion [4,5]. Lgals3 affinity for ECM substrates is also modulated by phosphorylation at its Ser6 residue [6].
    > Lgals3 is an NFκB target gene [7]; Lgals3 protein is widely distributed throughout most tissue sites (as demonstrated by the TiGER Tissue specific gene expression and regulation database; [8]). Furthermore, within specific tissues, Lgals3 protein expression is widespread, with extracellular [9], membrane bound, cytoplasmic, and nuclear localizations (for review, see [10]).

### [3] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
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
  - Snippet 1 (score: 0.819)
    > Galectins are an evolutionarily ancient family of proteins sharing a high binding affinity for carbohydrates with β-galactoside linkages. In the extracellular space, galectins interact (through a conserved carbohydrate recognition domain, aka CRD) with glycosylated proteins to mediate both cell-to-cell interactions and cell-to-matrix adhesion. Galectins are thus pattern recognition molecules specialized to distinguish carbohydrate moieties.
    > Within the galectin family, galectin-3 (also known as Lgals3) has unique properties. Its preferred ligand is N-acetyllactosamine [1]. It is also the only galectin containing a conserved N-domain as well as a single CRD domain. This N-domain allows Lgals3 not bound to a carbohydrate target to form multimeric complexes [2].
    > In this manner, low extracellular Lgals3 concentrations tend to inhibit extracellular interactions and adhesion [3], while high Lgals3 extracellular concentrations facilitate cellular adhesion [4,5]. Lgals3 affinity for ECM substrates is also modulated by phosphorylation at its Ser6 residue [6].
    > Lgals3 is an NFκB target gene [7]; Lgals3 protein is widely distributed throughout most tissue sites (as demonstrated by the TiGER Tissue specific gene expression and regulation database; [8]). Furthermore, within specific tissues, Lgals3 protein expression is widespread, with extracellular [9], membrane bound, cytoplasmic, and nuclear localizations (for review, see [10]).

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
  - Snippet 1 (score: 0.813)
    > Lgals3 (also referred to as galectin-3) is considered a marker of macrophage-like cells. 13,31 Rong et al detected a population of VSMCs that expressed Lgals3 following cholesterol loading in vitro. 31 Recently, Alencar et al found that Lgals3 activation is not a specific marker of the differentiation of VSMCs to a macrophage-like state but rather it is a marker of VSMCs entering a transitional state, with increased expression of genes associated with stem cells that are capable of extracellular matrix remodeling. 16 Of note, similar to SEM-like cells, Lgals3 + cells also have increased expression of lymphocyte antigen 6 family member A and vascular cell adhesion molecule 1. Further studies to investigate if SEM-like cells are derived from Lgals3 + cells are warranted.
    > Using mouse, rat, and human models of cholesterolloading in VSMCs, Li et al found that SREBP1 (sterol regulatory-element binding protein-1) and Krüppel-like factor-15 induced up-and downregulation of Lgals3, respectively, via binding to the Lgals3 gene promoter (albeit at different sites). 45 Likewise, Lgals3 promoted SREBP1 gene expression, producing a feedforward loop upregulated by cholesterol loading. 45 Moreover, Lgals3 and SREBP1 downregulated myocardin-related transcription factor A expression in VSMCs. 45 In another study, Owsiany et al used a dual lineage tracing model and found that Lgals3 + VSMCs produce monocyte chemoattractant protein 1, a proinflammatory chemokine. 15 Knockout of monocyte chemoattractant protein 1 specifically in Lgals3 + VSMCs resulted in the formation of atherosclerotic lesions with a greater ACTA2 content in the fibrous cap and decreased Lgals3 + cell content, a feature of stable plaque. 15

### [5] Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy
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
  - Snippet 1 (score: 0.805)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [6] Beyond Colonoscopy: Exploring New Cell Surface Biomarkers for Detection of Early, Heterogenous Colorectal Lesions
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
  - Snippet 1 (score: 0.799)
    > Galectin 3, or LGALS3, is a member of the galectin family, a group of carbohydrate-binding lectins characterized by their binding affinity for beta-galactosides (85).
    > LGALS3 is expressed at the cell surface, where it interacts with the extracellular matrix, especially with glycoproteins, and has the ability to affect intracellular signaling pathways (42). LGALS3-expressing cells also possess higher ALDH1 activity, which often correlates with a dedifferentiated cancer stem cell phenotype, than do their LGALS3-negative counterparts (86).
    > The correlation of LGALS3 expression in CRC with clinical pathological characteristics has been explored in several immunohistochemical and RT-PCR studies. In one study, the IHC staining of CRC tissue (n=61) and normal adjacent tissue (n=23) samples showed significantly higher LGALS3 expression in cancer tissue (62.5%) versus normal cancer-adjacent tissue (13.0%) (41). In another study, 75% of CRC tissue samples stain high for LGALS3, and ten CRC cell lines were shown to have increased LGALS3 protein levels compared to HeLa cells (42).
    > LGALS3 expression varies according to cancer staging and the degree of differentiation of the adenocarcinoma. LGALS3 mRNA levels were higher in early stage colorectal cancers (58% in stage I) compared to advanced cancers (50% in stage IV) (43). Protein analysis found higher LGALS3 levels in primary adenocarcinomas than in metastatic adenocarcinomas, and stronger LGALS3 staining in well-differentiated tumor areas compared to poorly differentiated tumor areas (43). Conversely, colorectal adenocarcinomas may display higher levels of LGALS3 than do colorectal adenomas; one study sets the rate of colorectal adenocarcinoma expression of LGALS3 at 95% while only 73% of adenomas were positive for LGALS3 (43).

### [7] Prognostic risk analysis related to radioresistance genes in colorectal cancer
- Authors: Haoren Qin, Heng Zhang, Haipeng Li, Qiong Xu, Wan-jun Sun et al.
- Year: 2023
- Venue: Frontiers in Oncology
- URL: https://www.semanticscholar.org/paper/49a148168d686123fb072be1d332606425d67aa7
- DOI: 10.3389/fonc.2022.1100481
- PMID: 36741692
- PMCID: 9890073
- Citations: 11
- Summary: The risk score model built with five radioresistance genes in this study, including TNFRSF13C, CD36, ANGPTL4, LAMB3, and SERPINA1, showed favorable performance in prognosis prediction after radiotherapy for CRC.
- Evidence snippets:
  - Snippet 1 (score: 0.799)
    > Therefore, the cell adhesion and ECM-related DEGs were screened as candidate genes for subsequent analyses.
    > We cross-referenced the cell adhesion and extracellular matrixrelated genes with the above-mentioned DEGs by releasing all genes containing the following annotations or their subdivisions: GO:0031012 extracellular matrix; GO:0030198 GO:0031012 extracellular matrix; GO:0030198 extracellular matrix organization; GO:1903053 regulation of extracellular matrix organization; GO:0035426 extracellular matrix-cell signaling; GO:0007155 cell adhesion; GO:0030155 regulation of cell adhesion; GO:0007160 cell-matrix adhesion; and GO:0050840 extracellular matrix binding. A total of 94 overlapping genes from DEGs and ECM-related genes were retained as candidate genes for subsequent analysis (Figure 1G). For these 94 genes, the interaction network of the encoded proteins was mapped using the STRING database (Figure 1H).

### [8] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
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
  - Snippet 1 (score: 0.794)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.
  - Snippet 2 (score: 0.764)
    > Next, the prognostic value of LGALS3 expression in the 23 kinds of cancer patients was then determined.Correlations between LGALS3 expression with OS (overall survival) were evaluated using the GEPIA2 database.In the OS study, only elevated LGALS3 expression indicated poorer survival for HCC patients (Fig. 2A).LGALS3 was not statistically significant for OS of 22 other cancer types patients.Furthermore, DSS (disease-specific survival) LGALS3 in predicting 1-, 3-, and 5-year OS. (H) ROC curve for LGALS3 in predicting 1-, 3-, and 5-year DSS.The higher values of AUC corresponding to higher predictive power.*p value < 0.05; ***p value < 0.001 was lesser in patients suffering from HCC having higher levels of LGALS3 expression (Fig. 2B).Next, we validated the expression levels of LGALS3 protein in HCC tissues using IF staining.As expected, HCC tumor demonstrated strong LGALS3 expression (Fig. 2C).These findings were further validated by qRT-PCR assay of tumor and adjacent normal tissues from 5 HCC patients.Here, LGALS3 expression was also significantly increased in the HCC tissues (Fig. 2D).In addition, LGALS3 expression was shown to be linked with the pathological stage of HCC, as illustrated in Fig. 2E.High expression of LGALS3 gene is associated with high tumor grade in HCC (Fig. 2F).Moreover, LGALS3 expression was significantly associated with OS and DSS in both univariate and multivariate analyses (Figure S2A-H).Time-dependent ROC analysis showed that the area under the ROC curve was 0.672 at 5 years of OS, and 0.691 at 5 years of DSS (Fig. 2G-H).Taken together, LGALS3 might function as a prospective biomarker for the prognosis of patients suffering from HCC.

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
  - Snippet 1 (score: 0.793)
    > In the LGALS family, LGALS3 has a special domain that recognizes and binds to β-galactosides on cellular glycoproteins and glycolipids (5).
    > LGALS3 may be observed in the cytoplasm and in the nucleus as well as the extracellular matrix (6). It serves different biological functions, such as cell growth, cell adhesion, angiogenesis, and apoptosis (7).
    > LGALS3 can be expressed in different types of tumors, and accumulating evidence has proved that LGALS3 plays a vital role in tumorigenesis and development (6,(8)(9)(10)(11)(12)(13)(14)(15)(16). Recently, a study indicated that LGALS3 can promote the therapeutic resistance of glioblastoma and is related to tumor risk and prognosis (17). However, its prognostic significance needs to be further confirmed in large glioma samples, and, hitherto, no studies have explored the role of LGALS3 in the glioma immune microenvironment and its correlation with key molecular markers, including isocitrate dehydrogenase 1 (IDH1), alpha-thalassemia/mental retardation X-linked (ATRX), O-6methylguanine-DNA methyltransferase (MGMT), telomerase reverse transcriptase (TERT), and 1p19q.

### [10] Identification of an Internal Gene to the Human Galectin-3 Gene with Two Different Overlapping Reading Frames That Do Not Encode Galectin-3*
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
  - Snippet 1 (score: 0.774)
    > Human Rapid-Scan Gene Expression Panel was used to detect the alternative transcripts in various human tissues using RT-PCR. The primers used were designed to amplify a 923-or 629-bp fragment.
    > LGALS3 transcripts were detected as a 457-bp DNA and actin transcripts as a 640-bp DNA. PCR was performed using 0.25 ng or 2.5 ng (10ϫ) template cDNA.
    > average of other human proteins is 10 times lower. This rich content in tryptophans confers hydrophobic properties that may account for the membrane localization of the ORF2⅐EGFP protein (Fig. 6). Consistent with the mitochondrial localization of the ORF2⅐EGFP fusion protein, this sequence exhibits the common properties of mitochondrial-imported proteins such as the enrichment of arginine, leucine, and serine residues (36).
    > Tissue Specificity of galig Expression-Detection of galig transcripts in HOS cells and colon tumor cells revealed a low expression level. Based on this observation, the rationale that the appearance of galig transcripts may have resulted from a leaky transcription of a cryptic promoter rather than from an independently functioning promoter could not be excluded. Screening of several human tissues indicated clearly that galig is a tightly regulated gene whose expression is most efficient in leukocytes from peripheral blood. The low level of transcription in bone marrow indicates that galig is specifically expressed in mature forms of leukocytes. Whereas the precise quantification of galig mRNA has not been addressed in these experiments, it is clear that these transcripts are much less abundant than LGALS3 transcripts. This may not be surprising considering that LGALS3 is known to be highly expressed when activated (37,38). Indeed, the amount of LGALS3 transcripts appeared as abundant as those from actin genes. This shows a different type of regulation by the galig and LGALS3 promoters. In particular, muscle, stomach, and uterus, although expressing low levels of galig transcripts, revealed no LGALS3 transcripts, thus indicating an independent functioning of the two promoters.

### [11] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
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
  - Snippet 1 (score: 0.771)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.

### [12] In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression
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
  - Snippet 1 (score: 0.768)
    > However, opposite DNA methylation patterns (associated with a higher mutation rate in aggressive ECs) were found between type I and type II ECs, thus confirming the more aggressive phenotype of ECC-1 cells induced upon C1GALT1 depletion [82]. These data suggest that NCOA1 and DNMT3A levels might be used as biomarkers of EC malignancy. In contrast, dysregulation of ERCC3 (Excision repair cross-complementation group 3) levels has not been previously associated to EC, although different studies highlight the suppressor role of ERCC3 silencing in different cancers, as pancreatic or liver carcinomas [83,84].
    > Finally, LGALS3 (Galectin-3) is a protein that interacts with glycoproteins from the extracellular matrix in a galactose-dependent manner, favoring cell interactions, or with cytosolic or nuclear targets in a glycosylation independent manner [46]. Importantly, LGALS3 has been reported as EC marker [85][86][87], and as unfavorable marker for overall survival [73]. Here, we have found that the LGALS3 upregulation occurred in parallel to the downregulation of C1GALT1 both in vitro and in vivo in tumor tissue, with a significant negative correlation between them. Therefore, it can be suggested that LGALS3 upregulation in aggressive EC was a consequence of the downregulation of O-glycosylation in proteins from the extracellular matrix, which avoids LGALS3 interaction in the extracellular matrix of EC tumors, and as a compensatory effect an increase and release of LGALS3 should be produced.
    > In conclusion, quantitative proteomics of a well-characterized cellular model, where upon C1GALT1 depletion a more aggressive phenotype was induced, allow for the identification of proteins dysregulated in aggressive ECs and related pathways that might be of interest for a better understanding of the mechanisms undergoing EC pathogenesis related to O-glycosylation.

### [13] Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins
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
  - Snippet 1 (score: 0.768)
    > Lgals3 has been implicated in the regulation of innate and adaptive immune responses, where it participates in the activation or differentiation of immune cells and contributes to phagocytic clearance of microorganisms and apoptotic cells by macrophages (117,118). Lgals3 has been reported to promote but also to inhibit T-cell apoptosis depending on whether it binds to glycoproteins on the cell surface (CD45 and CD71) or to intracellular ligands (Bcl-2) (119, 120). In the placenta, Lgals3 was detected in all trophoblastic lineages including villous cytotrophoblasts (CTB) and EVT with a reduction of Lgals3 expression observed from the VT to the trophoblastic cell columns (121). This pattern of Lgals3 expression correlates with the switch from a proliferative to a migratory trophoblast phenotype and while placental Lgals3 dysregulation has been associated with some obstetric complications including spontaneous or recurrent miscarriages, further studies are needed to understand its contribution to trophoblast biology (81,122). In addition to trophoblasts, Lgals3 is expressed by maternal decidual cells (73). While showing a different expression pattern, both Lgals1 and Lgals3 have been proposed to play a role in cell-cell and cell-matrix interactions of trophoblast during placentation (121). Studies of the importance of Lgals3 in murine pregnancy by Yang et al. indicate that Lgals3 is expressed in the luminal and glandular epithelium and that an increase in Lgals3 is required for proper embryo implantation (123). In addition, Lgals3 affects chemotaxis and morphology of endothelial cells and stimulates capillary tube formation and angiogenesis in vivo (124). Therefore, besides its proposed roles in embryo implantation, immune regulation and trophoblast-matrix interactions, Lgals3 has a potential role in placental angiogenesis.

### [14] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
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
    > Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated. Induction of PPP2R2A protein (Fig. 5) but not gene expression (Fig. 7) in THP-1 cells expressing LGALS3 shRNA suggests that LGALS3 acts directly on the PP2A subunits via a post-transcriptional mechanism in these cells. The TCGA data (Table 3) however suggests that there is a positive correlation between gene expression of LGALS3 and PPP2R2A suggesting that a common pathway may regulate the two genes. Fig. 8. Progeny clustering identified an optimal number of 4 distinct protein clusters for this ProFnGrp. Protein networks were generated and showed interactions between "core-proteins" (large nodes) and other probed proteins (small nodes) from the data set. Clustering method has been described in our previous publication (ref. [37]) and further information on these protein networks can be found on our website "Leukemia Profile Atlases", available at https://www.leukemiaatlas.org/. Progeny clustering identified one protein cluster with expression similar to that of the normal CD34+ samples which was designated as "normal-state" while three "leukemia-specific" protein patterns characterized by high expression individually of CD74, LGAL3, and a fourth state with both on. PPP2RA/B/C/D was the only LGALS3 network protein demonstrated to be directly regulated by LGALS3 in the THP-1 cells (Fig. 5). In our previous study we saw potent suppression of AKT signaling by LGALS3 inhibition, so perhaps the mechanism involves LGALS3 suppression of the AKT phosphatase [15]. However, we did not see suppression of LGALS3 affect other network proteins in the THP-1 cells (data not shown). The role of other galectins such as LGALS1 in AML biology is not clear.
  - Snippet 2 (score: 0.766)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.

### [15] Lgals3 Promotes Calcium Oxalate Crystal Formation and Kidney Injury Through Histone Lactylation‐Mediated FGFR4 Activation
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
  - Snippet 1 (score: 0.766)
    > To investigate whether Lgals3 promoted kidney injury and renal fibrosis caused by CaOx crystal, a kidney-specific overexpression  system that overexpressed Lgals3 was utilized in mice (Figure S5A, Supporting Information). After four weeks of injection, the effectiveness of Lgals3 overexpression was confirmed by qPCR and Western blot (Figure S5B,C, Supporting Information). Subsequently, a CaOx kidney stone model was established (Figure 3A). The serum BUN and Creatinine results showed that Lgals3 overexpression migrates the kidney injury (Figure 3B,C). HE and Von Kossa staining found that Lgals3 overexpression aggravated kidney injury and CaOx crystal deposition (Figure 3D). In addition, pathology staining and Western blot analysis found that overexpression of Lgals3 significantly increased renal fibrosis and inflammation response caused by CaOx crystal deposition (Figure 3E,F; Figure S5D, Supporting Information).
    > An adenoviral vector encoding the Lgals3 gene was utilized in vitro to investigate the effects of Lgals3 overexpression. The overexpression efficiency was confirmed by Western blot (Figure S4B, Supporting Information). Western blot analysis and immunofluorescence staining of ROS found that overexpression of Lgals3 significantly increased the expression of fibrosis-related protein and ROS expression (Figure S4F,G, Supporting Information). Taken together, these results indicate that Lgals3 overexpression can promote CaOx crystal deposition and renal fibrosis.

### [16] Krüppel-like Factor 3 (KLF3/BKLF) Is Required for Widespread Repression of the Inflammatory Modulator Galectin-3 (Lgals3)*
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
  - Snippet 1 (score: 0.760)
    > Lgals3 Is Up-regulated in the Absence of KLF3-In studies of the role of KLF3 in hematopoiesis and red blood cell development, microarrays performed on Ter119 ϩ fetal liver cells lacking KLF3 revealed that the Lgals3 gene was consistently up-regulated in knockout animals (15). Because of the importance of galectin-3 in a number of biological settings, we undertook a fuller analysis of whether the expression of Lgals3 was altered in a range of mouse tissues in the absence of KLF3. Lgals3 mRNA levels were assessed in cultured murine embryonic fibroblasts (MEFs) as well as a series of primary tissues from wild-type and Klf3 Ϫ/Ϫ mice by quantitative real-time PCR. In primary and immortalized Klf3 Ϫ/Ϫ MEFs, Lgals3 mRNA was up-regulated 4.7-and 4.3-fold, respectively, compared with wild-type expression (Fig. 1A). Importantly, Lgals3 levels were also found to be elevated in a number of primary tissues dissected from KLF3-deficient mice (Fig. 1B). Derepression was most evident in Klf3 Ϫ/Ϫ subcutaneous (6.7-fold) and epididymal (3.3-fold) white adipose depots and in the heart (6.6-fold) and pancreas (4.2-fold).
    > Following the demonstration that Lgals3 is derepressed in Klf3 Ϫ/Ϫ tissues at the mRNA level, we next sought to determine whether this up-regulation was reflected at the protein level. Whole cell protein extracts were prepared from wild-type and Klf3 Ϫ/Ϫ fat depots and spleens, and the expression of galectin-3 protein was assessed by Western blotting (Fig. 1, C-F).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.