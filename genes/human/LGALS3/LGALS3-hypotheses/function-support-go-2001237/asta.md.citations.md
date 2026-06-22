# Citations for Research Query

**Query:** # Literature evidence for LGALS3 (Homo sapiens): LGALS3 has negative regulation of extrinsic apoptotic signaling pathway (GO:2001237).

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

**Provider:** asta
**Generated:** 2026-06-22T04:47:30.958453

1. P. Ruvolo, Chenyue W. Hu, Y. Qiu, V. Ruvolo, Robin L. Go et al. (2019). LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML. EBioMedicine. https://www.semanticscholar.org/paper/46bbdbcb4660389e13acba24499cc415d75f18e0
2. Meng Cui, Zhe Wang, Letao Huang, Jia-He Wang (2022). Parthenolide leads to proteomic differences in thyroid cancer cells and promotes apoptosis. BMC Complementary Medicine and Therapies. https://www.semanticscholar.org/paper/7f36ac62e89f19c15f02a3e0b01306e4f458dd67
3. L. Rojas, Jana Grüttner, S. Ma'ayeh, Feifei Xu, S. Svärd (2022). Dual RNA Sequencing Reveals Key Events When Different Giardia Life Cycle Stages Interact With Human Intestinal Epithelial Cells In Vitro. Frontiers in Cellular and Infection Microbiology. https://www.semanticscholar.org/paper/a07b7add52e16b284f33a3757df71a8f8338df7b
4. Ying Yao, Jingyu Wang, T. He, Heyangzi Li, Jue Hu et al. (2020). Microarray assay of circular RNAs reveals cicRNA.7079 as a new anti-apoptotic molecule in spinal cord injury in mice.. Brain research bulletin. https://www.semanticscholar.org/paper/8e327ffbb4c66488f7c21b3dc5f8bcd5321ffdae
5. Ziwei Xie, Yue He, Yuxin Feng, Xiaohong Wang (2024). Identification of programmed cell death-related genes and diagnostic biomarkers in endometriosis using a machine learning and Mendelian randomization approach. Frontiers in Endocrinology. https://www.semanticscholar.org/paper/a437f1ce179ac605a4b4d5733d5e488db5fbabe5
6. Guanglei Ji, R. Ren, Xichao Fang (2021). Identification and Characterization of Non-Coding RNAs in Thymoma. Medical Science Monitor : International Medical Journal of Experimental and Clinical Research. https://www.semanticscholar.org/paper/e0ad5ef5a9e860f17008417de010a1dc1b91e301
7. Yinghui Ren, Yongmei Qian, Qicheng Zhang, Xiaoping Li, Mingjiang Li et al. (2024). High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma. Cancer Cell International. https://www.semanticscholar.org/paper/552bd37c67dea75d0c33a9a0de2acdafcf0dcf6e
8. S. Blois, G. Dveksler, G. Vasta, N. Freitag, V. Blanchard et al. (2019). Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins. Frontiers in Immunology. https://www.semanticscholar.org/paper/68fad2b87411701fa708a1f49f8b918370486857
9. Yang Zhao, Pu Chen, Hong-jun Lv, Yuan Wu, Shu Liu et al. (2021). Identification of Oncosuppressing Effects of Seven Selenoproteins in Thyroid Cancer: Implications for Distinct Roles of Selenoproteins in Tumorigenesis. https://www.semanticscholar.org/paper/13df7e615ebc2fa71ed470d2f3a02f8a65b931ef
10. Zhaojun Wang, Haifeng Li, Fajun Li, Xin Su, Junhang Zhang (2020). Bioinformatics-Based Identification of a circRNA-miRNA-mRNA Axis in Esophageal Squamous Cell Carcinomas. Journal of Oncology. https://www.semanticscholar.org/paper/d2dff21c189100a75d23e26ee2a4eef452807b2d
11. Jin Luo, C. Piao, De Jin, Li Wang, Xiaohua Zhao et al. (2020). A Network Pharmacology Approach to Understanding the Mechanisms of Action of Traditional Medicine: Rheum L. for Diabetic Kidney Disease. https://www.semanticscholar.org/paper/97072294d3d8475989fea00468baf914f0e68111
12. Jian-Jing Siew, Hui-Mei Chen, Feng‐Lan Chiu, Chia-Wei Lee, Yao-Ming Chang et al. (2023). Galectin-3 aggravates microglial activation and tau transmission in tauopathy. The Journal of Clinical Investigation. https://www.semanticscholar.org/paper/8c77eea796475aa4e26a4051432bc4d4c021d847
13. Zehua Ye, Yushi Sun, Songyuan Yang, Lei Li, Bojun Li et al. (2025). Lgals3 Promotes Calcium Oxalate Crystal Formation and Kidney Injury Through Histone Lactylation‐Mediated FGFR4 Activation. Advanced Science. https://www.semanticscholar.org/paper/adbfa30b5832407d200a5eade9196d41be08050e
14. Jingyuan Li, Jianyu Wang, D. Xie, Qin Pei, Xue Wan et al. (2021). Characteristics of the PI3K/AKT and MAPK/ERK pathways involved in the maintenance of self-renewal in lung cancer stem-like cells. International Journal of Biological Sciences. https://www.semanticscholar.org/paper/9302948464800646b146c0b29b812d6771909340
15. Dávid Jónás, Sára Sándor, K. Tátrai, B. Egyed, E. Kubinyi (2020). A Preliminary Study to Investigate the Genetic Background of Longevity Based on Whole-Genome Sequence Data of Two Methuselah Dogs. Frontiers in Genetics. https://www.semanticscholar.org/paper/3ac24db3f845e1915648e0d3a75f2c0ff22d5ae1