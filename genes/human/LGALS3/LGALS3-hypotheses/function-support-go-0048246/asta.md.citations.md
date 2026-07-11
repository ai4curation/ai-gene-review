# Citations for Research Query

**Query:** # Literature evidence for LGALS3 (Homo sapiens): LGALS3 has macrophage chemotaxis (GO:0048246).

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

**Provider:** asta
**Generated:** 2026-06-22T04:47:16.130840

1. Yinghui Ren, Yongmei Qian, Qicheng Zhang, Xiaoping Li, Mingjiang Li et al. (2024). High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma. Cancer Cell International. https://www.semanticscholar.org/paper/552bd37c67dea75d0c33a9a0de2acdafcf0dcf6e
2. Wan-Ming Hu, Yuan-Zhong Yang, Tian Zhang, Changling Qin, Xuenong Li (2020). LGALS3 Is a Poor Prognostic Factor in Diffusely Infiltrating Gliomas and Is Closely Correlated With CD163+ Tumor-Associated Macrophages. Frontiers in Medicine. https://www.semanticscholar.org/paper/53b083f91a08aefebb5f9edaaa95625e2dc98f2b
3. Xiaofeng Li, Bing Yang (2025). Morphological and transcriptional insights into the role of histone phosphorylation-related genes in early development of the chicken duodenum. Animal Bioscience. https://www.semanticscholar.org/paper/b3da4d3a37ec0fae40140d0cf95db98d90b41079
4. Runji Chen, D. McVey, D. Shen, Xiaoxin Huang, Shu Ye (2023). Phenotypic Switching of Vascular Smooth Muscle Cells in Atherosclerosis. Journal of the American Heart Association: Cardiovascular and Cerebrovascular Disease. https://www.semanticscholar.org/paper/472c313e2214a97757712ab0a8b39b133bd6a6bc
5. S. Blois, G. Dveksler, G. Vasta, N. Freitag, V. Blanchard et al. (2019). Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins. Frontiers in Immunology. https://www.semanticscholar.org/paper/68fad2b87411701fa708a1f49f8b918370486857
6. E. Ragni, C. Perucca Orfei, P. De Luca, A. Colombini, M. Viganò et al. (2020). Secreted Factors and EV-miRNAs Orchestrate the Healing Capacity of Adipose Mesenchymal Stem Cells for the Treatment of Knee Osteoarthritis. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/7d8d9d140ae309da10710f17dc979236a67fb966
7. Philip K Farahat, Chino Kumagai-Cresse, Raquel L. Aragón, Feiyang Ma, Justin K. Amakor et al. (2025). Macrophage-derived Spp1 promotes intramuscular fat in dystrophic muscle. JCI Insight. https://www.semanticscholar.org/paper/25c265aed44730ce4b23491cd7ac24d8c3fcf94b
8. Upendra Chalise, M. Daseke, William J. Kalusche, Shelby R. Konfrst, Jocelyn R. Rodriguez-Paar et al. (2022). Macrophages secrete murinoglobulin-1 and galectin-3 to regulate neutrophil degranulation after myocardial infarction. Molecular Omics. https://www.semanticscholar.org/paper/446873a6222f1a5c4299cb80c95f7f9ff792e9f8
9. F. L. de Oliveira, Katia Carneiro, J. Brito, M. Cabanel, J. X. Pereira et al. (2017). Galectin-3, histone deacetylases, and Hedgehog signaling: Possible convergent targets in schistosomiasis-induced liver fibrosis. PLoS Neglected Tropical Diseases. https://www.semanticscholar.org/paper/6dc6d6f3529841361a1ccf76eac911be181636c7
10. K. Di Gregoli, M. Somerville, Rosaria Bianco, Anita C. Thomas, Aleksandra Frankow et al. (2020). Galectin-3 Identifies a Subset of Macrophages With a Potential Beneficial Role in Atherosclerosis. Arteriosclerosis, Thrombosis, and Vascular Biology. https://www.semanticscholar.org/paper/7cc49f01469f15e073d249c35f5b1deb45262ade
11. T. Sakurai, Toshiyuki Fukutomi, Sachiko Yamamoto, Eriko Nozaki, T. Kizaki (2021). Physical Activity Attenuates the Obesity-Induced Dysregulated Expression of Brown Adipokines in Murine Interscapular Brown Adipose Tissue. International Journal of Molecular Sciences. https://www.semanticscholar.org/paper/c62f909c1038a72ef7c427bfa9914983c22b5422